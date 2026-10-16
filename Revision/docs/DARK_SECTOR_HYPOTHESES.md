# Dark-sector hypotheses for dirac16complex and dirac16complex00: the equation of state seen from 3-space

## Hypothesis and Hypothesis00 investigated in the author's primordial gravitational field with exponentially deflating extra times and the second metric function $b_4(x_4)$: the observer assumption, the method, the results for each field, the comparison with the Supernovae Unite values, the verdicts and what remains open

## Abstract

The author asked on 2026-10-01 that two hypotheses be investigated: that dirac16complex (Hypothesis) and dirac16complex00 (Hypothesis00) provide a possible physical mechanism for a time-varying dark-energy equation of state and/or a time-varying dark-matter equation of state. This document reports what the Revision computation found for the author's metric of 2026-10-14, in which the three extra-time components carry the second function $b_4(x_4)$; $b_4$ is a function of $x_4$, and every result below is computed with it (the earlier record used $b_4 = 1$; it is withdrawn and quoted only for comparison). Every number is read from a named Revision report. The history of the numbers is $a_4 = Hx_4$ with $b_4(x_4) = b_4(0)\,e^{(4/3)Hx_4}$: with the author's weights it is the history that the mixed $(x_4, x_0)$ field equation allows for a source without a $T^{x_4}{}_{x_0}$ component, and the author's equations then require the constant source $\kappa(\rho, p_3, p_t, p_0) = (-2/27, -2/9, -22/27, -14/27)$. The equation of state that a 3-space observer infers is not fixed by the field equations alone: the extra times $x_5, x_6, x_7$ are time-like and deflate exponentially, and the 4-dimensional density $\rho_4$ needs an ASSUMPTION about how the observer normalises over them. For the three stated definitions (A), (B) and (C) the dilution-inferred equation of state obeys exactly $w_{\rm eff} = X/E - s + (\beta/2)(P_t/E + s)$ with $X = P_3 - P_t$, $\beta = d\ln b_4/da_4$, $s = 0$ for (A), (B) and $s = 1$ for (C); on the history ($\beta = 4/3$) every verdict moves by exactly $-1/3$ between (A, B) and (C). dirac16complex: the computed Kohn-Sham gas (615 instantaneous states along the history, solved at the coupling that $b_4$ dictates) is radiation-like, with $w_{\rm eff}(A)$ rising toward $1/3$ (0.2929 to 0.3183 for $N = 688$, $\lambda = 0$); the dark-matter-like fall from $1/3$ toward 0 occurs for quanta of the massive bulk band (0.239626 to 2.268e-03 for one shell), which the computed ground states do not populate; under (C) the gas has $w_{\rm eff}$ between -0.040430 and -0.006905, close to 0 and not dark-energy-like; nothing computed comes near the Unite pair $(w_0, w_a) = (-0.861, -0.60)$ (closest distance 0.291, with a drifting condensate) and no computed state crosses $w = -1$. dirac16complex00: a positive-energy gas of good-sector modes has the dark-matter-like law $1/3 \to 0$ under (B), independent of $b_4$; every positive-energy model has $w_{\rm eff}(C) \geq -1/3$ as long as its modes have real frequencies, so the Unite values are out of reach without a ghost-like component, and $w_0 = -0.861$ needs a ghost fraction of at least 1583/1000 of the total energy. The condensate's ratio drifts with $b_4$: it equals the Unite constant $w = -0.764$ at $\lambda S/m = -382/441$ only at one instant. A model with as many tuned parameters as matched numbers reproduces them by construction and is NOT a prediction. This record establishes neither Hypothesis nor Hypothesis00; it states what each field can and cannot produce under its stated assumptions.

## 1. The hypotheses and the short answer

The author's hypotheses, quoted from `Revision/README.md`:

- “Hypothesis: dirac16complex provides a possible physical mechanism for a time-varying dark energy equation of state and/or a possible physical mechanism for a time-varying dark matter equation of state, both of which you will investigate.”
- “Hypothesis00: dirac16complex00 provides [the same], both of which you will investigate.”

`Revision/SPEC.md` section 8 makes both hypotheses questions to be INVESTIGATED, not assumed: for each field, the equation of state seen by a 3-space observer as the extra times deflate and 3-space inflates (the condensate, the Kohn-Sham gas, mixtures), its time dependence, the CPL parameters, and the comparison with the Supernovae Unite values. Section 11 of the same file records the lead's analysis, to be checked; section 8 of this document checks it point by point.

The short answer (details and records in sections 3 to 9):

1. The observer's $\rho_4$ is an ASSUMPTION (section 3). Every verdict below is stated for each definition; on the history with $b_4(x_4)$ the definitions differ by exactly $1/3$.
2. dirac16complex, dark matter: a time-varying dark-matter-like equation of state ($w_{\rm eff}$ falling from $1/3$ toward 0 under (A, B)) is present in the theory for quanta of the massive bulk band, independent of $b_4$, not in the computed Kohn-Sham ground states, whose gas is radiation-like.
3. dirac16complex, dark energy: not found. Under (C) the gas has $w_{\rm eff}$ between -0.040430 and -0.006905, close to 0; only a drifting condensate gives negative values, with a strongly thawing slope; no Kohn-Sham state comes near the Unite pair or crosses $w = -1$, and a drifting $\lambda < 0$ condensate crosses $-1$ toward the past (section 5.5).
4. dirac16complex00, dark matter: a positive-energy gas of good-sector modes has the time-varying law $1/3 \to 0$ under (B) and in the ratio $p_3/\rho$, independent of $b_4$.
5. dirac16complex00, dark energy: not with positive energies: $w_{\rm eff}(C) \geq -1/3$ for positive-energy content with real frequencies; the Unite $w_0$ needs a ghost-like component larger than the positive energy.
6. On the history $a_4 = Hx_4$ the observer's expansion itself reads $w_{\rm exp} = -1$ exactly, for every $b_4(x_4)$.

## 2. Setting and conventions

### 2.1 The author's metric and coordinates

The coordinates are the author's, $x_0, x_1, \dots, x_7$, in the author's order (`Dirac_Einstein-Lovelock_4+4_Nash.nb`, input cell In[48]: `X = {x0[], x1[], x2[], x3[], x4[], x5[], x6[], x7[]}`): $x_0$ is the hidden space direction, with $z = 6Hx_0 \in (0,\pi/2)$ and $H > 0$ the author's constant, $x_1, x_2, x_3$ are ordinary 3-space (inflating), $x_4$ is the time, and $x_5, x_6, x_7$ are the three extra times, which are time-like and DEFLATE exponentially as $a_4$ increases. (Until 2026-10-14 this record named them $x_1, \dots, x_8$, with the hidden direction $x_8$ listed last; the user ordered the author's coordinates on 2026-10-14.) The metric is the author's of 2026-10-14 (input cells In[97] to In[102] of that notebook),

$$
\begin{aligned}
ds^2 = {} & \cot^2 z\,dx_0^2 + e^{2a_4(x_4)}\sin^{1/3}z\,\big(dx_1^2+dx_2^2+dx_3^2\big) - dx_4^2 \\
& - e^{-2a_4(x_4)}\,b_4(x_4)\sin^{1/3}z\,\big(dx_5^2+dx_6^2+dx_7^2\big) ,
\end{aligned}
$$

of signature (4,4), with $\sqrt{|g|} = b_4^{3/2}\cos z$ and $b_4(x_4) > 0$ a function of $x_4$. The 3-space scale factor is $e^{a_4}\sin^{1/6}z$ and the extra-time scale factor $e^{-a_4}b_4^{1/2}\sin^{1/6}z$. The observer's scale factor is $a = e^{a_4 - a_{4,\rm today}}$, normalised to $a = 1$ at a chosen “today” $a_{4,\rm today}$ (a free parameter); $b_4$ does not enter it. Along a history $\beta = d\ln b_4/da_4 = b_4'/(a_4'b_4)$. The Kohn-Sham records use the hidden coordinate $y = \ln(\sin z)/(6H)$. The record that reads the author's notebook, without evaluating it, is `Revision/dark_sector/reports/author-notebook-inputs.json` (`author_notebook_inputs.wls`): 147 cells, 113 input cells, and the only cell not in the version of the user's order of 2026-10-14 (commit b13373c) is In[137], the input $X$ alone, which displays the coordinate list.

### 2.2 The two fields and the energy-momentum tensor

dirac16complex is $\Psi$: 16 complex anticommuting components, a Pin(4,4) spinor, quantised canonically; its energy-momentum tensor is an operator, and the numbers below are expectation values in the instantaneous Kohn-Sham states of the good sector (no extra-time momentum), in the positive realisation of the good sector (with the ASSUMED brane condition and the chosen tip condition of the Kohn-Sham record, which make its blocks self-adjoint; the field-theory record constructs the positive realisation explicitly only for single good-sector momenta with frozen coefficients). dirac16complex00 is $\Phi$: 16 complex commuting components that transform as a Pin(4,4) spinor, a classical field; its energy-momentum tensor is the classical bilinear, whose energy has both signs (Krein-signed energies, section 6.2). Both fields have the Lagrangian of `Revision/SPEC.md` section 3 with $U(S) = \frac{\lambda}{2}S^2$, $S = \bar\Psi\Psi$, and the gravity term $\gamma^\mu\Omega_\mu = 3H\gamma^{(x_0)} + \frac34(b_4'/b_4)\gamma^{(x_4)}$. The energy density is $\rho = -T^{x_4}{}_{x_4}$ and the pressures are $p_\mu = T^\mu{}_\mu$ (no sum): $p_3$ of 3-space, $p_t$ of the extra times and $p_0$ of the hidden direction. For homogeneous on-shell states $\rho = mS + U$ and $p = SU' - U$. For a state of the Kohn-Sham record, $E$, $P_3$, $P_t$ and $P_0$ are the proper 7-volume integrals of $\rho$, $p_3$, $p_t$ and $p_0$ per unit coordinate volume, and $X = P_3 - P_t$.

### 2.3 The Unite values and the CPL convention

The author's private PDF (not part of the repository; only these numbers are used) gives the Supernovae Unite constant-$w$ fit $w = -0.764$ and the CPL fit $w(a) = w_0 + w_a(1-a)$ with $(w_0, w_a) = (-0.861, -0.60)$. In the deep past the CPL line tends to $w_0 + w_a = -1.461$ (quoted as -1.46), which is phantom; the line crosses $w = -1$ at $a = 461/600 = 0.7683$ ($z = 139/461$; record `unite_crossing_point`). In this convention thawing means $w_a < 0$ ($w$ rises from near $-1$) and freezing $w_a > 0$; the formula decides (the PDF's table states the opposite signs).

The CPL tangent of a model is $w_0 = w(1)$, $w_a = -dw/da$ at $a = 1$. The fits are least squares of $w(a)$ over $a \in [1/2, 1]$ or $[1/3, 1]$ (record `cpl_least_squares_rule`). The “constant $w$” of a model is the mean of $w(a)$ over the range, a PROXY: applied to the Unite CPL line itself it gives -1.011 on $[1/2, 1]$ and -1.061 on $[1/3, 1]$ (record `unite_line_fit_proxy`), so it is not the supernova constant-$w$ fit -0.764, which weights the data. No supernova likelihood, distance fit or covariance is computed anywhere in this record.

### 2.4 The history with $b_4(x_4)$

The numbers are computed on $a_4 = Hx_4$ (the author's $A = 1$) with $b_4(x_4) = b_4(0)\,e^{(4/3)Hx_4}$, that is $\beta = 4/3$ and $b_4 \propto a^{4/3}$. The reason (records `author_weights_b4_branch`, `D6_author_weights_branch`): with the author's weights $w_1 = 1$, $w_2 = 1/32$, $w_3 = 1/1152$, $\Lambda = 10$ the $(x_4, x_0)$ component of the field equations is $\cot z\,\beta_v\,Q(\alpha, \beta_v)$ with $\alpha = a_4'/H$, $\beta_v = b_4'/(Hb_4)$ (`Revision/metric_b4/results/vacuum-b4.json`); a source without a $T^{x_4}{}_{x_0}$ component, and every source of this record is one, needs $\beta_v Q = 0$. On $a_4 = Hx_4$ the component is $\frac{3}{64}\beta_v^2(3\beta_v - 4)\cot z$, which vanishes for a constant $b_4$ and for $\beta_v = 4/3$, $d\ln b_4/da_4 = 4/3$. The extra-time scale factor is then $e^{-a_4}b_4^{1/2} \propto a^{-1/3}$: the extra times still deflate exponentially. In Einstein gravity a $b_4(x_4)$ needs $T^{x_4}{}_{x_0} = \frac32 H\cot z\,b_4'/(\kappa b_4) \neq 0$ (`einstein_mixed_component_b4`), which no source of this record has. On this history the author's equations require the constant source

$$
\kappa\,(\rho,\ p_3,\ p_t,\ p_0) = \Big(-\frac{2}{27},\ -\frac{2}{9},\ -\frac{22}{27},\ -\frac{14}{27}\Big),
$$

computed twice: from the field equations of `Revision/field_equations_a4/a4-equations.json` (key b4), which with the author's weights reproduce the author's vacuum first (`author_weights_vacuum_recovered`, `branch_required_source`), and directly from the author's Lovelock tensors (`D7_branch_required_source`). It satisfies both conservation identities with $b_4$. A condensate cannot be this source (its $S$ decays like $b_4^{-3/2}$; `condensate_cannot_source_branch`), and the Kohn-Sham states are not admissible sources (section 10). The history is therefore a PRESCRIBED BACKGROUND for test fields.

## 3. The observer assumption: $\rho_4$ and the definitions (A), (B), (C)

### 3.1 Exact identities

The proper 7-volume element of a slice $x_4 = $ const is $b_4^{3/2}\cos z$: the inflation $e^{3a_4}$ of the proper 3-volume is compensated exactly by the factor $e^{-3a_4}$ of the proper extra-time volume $e^{-3a_4}b_4^{3/2}$, and the 7-volume changes with $x_4$ through $b_4$. The conservation law $\nabla_\mu T^\mu{}_\nu = 0$ for a diagonal $T(x_0, x_4)$, re-derived from the author's metric with Christoffel symbols computed anew in sympy and in Wolfram, gives

$$
\frac{d\rho}{dx_4} = -3a_4'(p_3 - p_t) - \frac32\,\frac{b_4'}{b_4}\,(\rho + p_t),\qquad
\frac{dE}{da_4} = -3X - \frac32\,\beta P_t ,
$$

and $dp_0/dx_0 + 3H\cot z\,(2p_0 - p_3 - p_t) = 0$, free of $b_4$. The records of the volumes and of these identities (the negative control: the form without the $b_4$ term fails):

| record | record | record |
| --- | --- | --- |
| `sqrt_det_g_equals_b4_three_halves_cos_z` | `proper_7_volume_element_b4` | `proper_3_and_extra_time_volume_scalings_b4` |
| `local_model_volume_b4` | `D1_volume_b4` | `conservation_x4_identity_b4` |
| `conservation_x0_identity` | `conservation_other_components_vanish` | `conservation_equals_a4_record_b4` |
| `conservation_x4_author_metric_b4` | `conservation_x0_author_metric` | `D2_conservation_b4` |
| `conservation_negative_control` | `integrated_identity_dE_dx4_b4` | `hidden_coordinate_dy_dx0` |
| `conservation_x0_in_y_form` |  |  |

The 3-space observer averages over the hidden direction with the weight $\cos z$, which does not depend on $x_4$ (record `observer_hidden_average_commutes`); the factor $b_4^{3/2}$ of the proper weight is written out below. The extra times are time-like, so the observer's 4-dimensional density needs a normalisation over them. Three are recorded:

- (A) the extra times are compact with a fixed coordinate period, i.e. closed time-like directions; $\rho_4 = E/(\text{proper 3-volume}) \propto E\,e^{-3a_4}$;
- (B) the extra times are non-compact and $\rho_4$ is taken per unit extra-time COORDINATE volume; $\rho_4 \propto E\,e^{-3a_4}$;
- (C) $\rho_4$ is taken per unit PROPER 7-volume (equivalently per unit proper extra-time volume $e^{-3a_4}b_4^{3/2}$); $\rho_4 \propto E\,b_4^{-3/2}$.

With the dilution-inferred equation of state $w_{\rm eff} = -1 - \frac13\,d\ln\rho_4/d\ln a$ the conservation identity gives exactly (records `w_eff_A_b4`, `w_eff_B_equals_w_eff_A_b4`, `w_eff_C_b4`, `w_eff_general_normaliser_b4`, `D3_w_eff_general_b4`)

$$
w_{\rm eff} = \frac{X}{E} - s + \frac{\beta}{2}\Big(\frac{P_t}{E} + s\Big),\qquad s = 0\ \text{(A, B)},\quad s = 1\ \text{(C)} .
$$

So $w_{\rm eff}(A) = w_{\rm eff}(B) = X/E + (\beta/2)P_t/E$ and $w_{\rm eff}(C) = w_{\rm eff}(A) - 1 + \beta/2$: on the history every verdict moves by exactly $-1/3$ between (A, B) and (C). The whole difference to the withdrawn $b_4 = 1$ formulas ($X/E$ and $X/E - 1$) is the $\beta$ term (`w_eff_difference_to_withdrawn_record`). The dirac16complex00 record names the same two scalings N1 (per unit extra-time coordinate volume, $\rho_4 = e^{-3a_4}b_4^{3/2}\langle\rho\rangle$, the scaling of (A) and (B)) and N2 (per unit proper 7-volume, $\rho_4 = \langle\rho\rangle$, definition (C)), with $w_{\rm eff}(N1) = w_3 - w_t + (\beta/2)w_t$ and $w_{\rm eff}(N2) = w_{\rm eff}(N1) - 1 + \beta/2$ for isotropic sources (records `observer_N1_weff_identity_b4`, `observer_N2_weff_identity_b4`). Below, (B) stands for (A) and (B) together and for N1, and (C) for N2. The ratio $w = p_3/\rho$ does not depend on the normalisation. `Revision/SPEC.md` section 11 writes $\rho_4 \sim \rho_8\,c^3$ with $c$ the extra-time scale factor: with $c = e^{-a_4}b_4^{1/2}$ that is definition (B).

### 3.2 How every verdict depends on the assumption

The rho_4 normalisation is an ASSUMPTION about the observer, not a consequence of the field equations, and this record does not choose one. The same state reads differently under each (history $\beta = 4/3$):

| state (records) | $w_{\rm eff}$ under (A), (B) | $w_{\rm eff}$ under (C) | ratio $p_3/\rho$ |
| --- | --- | --- | --- |
| homogeneous condensate (`condensate_w_eff_b4`) | $(2/3)\,w_c$; 0 for $\lambda = 0$ | $-1/3 + (2/3)\,w_c$ | $w_c = \lambda S/(2m+\lambda S)$, drifting |
| massless quanta (`massless_mode_w_eff`) | $1/3$, radiation | $0$ | $1/3$ |
| massive quanta, flat limit (`massive_mode_w_eff_law`) | $k^2/(3(M^2a^2+k^2))$: $1/3 \to 0$ | $0 \to -1/3$ | as (A), (B) for $q = 0$ |
| Kohn-Sham gas, $N = 688$, $\lambda = 0$ (section 5.2) | 0.2929 to 0.3183 | -0.0404 to -0.0150 | 0.2929 to 0.3183 |

INTERPRETATION (labelled): supernova distances measure the dilution-inferred $w_{\rm eff}$ of a 4-dimensional Friedmann observer, which agrees with the ratio $p_3/\rho$ only when no energy is exchanged with the extra times. Whether (A), (B), (C) or none of them describes such an observer is not decided by any equation of this record. Under (A) the extra times are closed time-like directions; under (B) and (C) they are non-compact and a normalisation is a choice.

### 3.3 The expansion-inferred equation of state

An observer who reads $a(t) = e^{a_4(x_4)}$ with $t = x_4$ ($g_{44} = -1$) and 4-dimensional Friedmann equations infers $w_{\rm exp} = -1 - \frac23\,a_4''/a_4'^2$ (record `expansion_inferred_w`); $b_4$ does not enter the observer's scale factor. In Einstein gravity $G^{x_1}{}_{x_1} - G^{x_5}{}_{x_5} = 2a_4'' + 3a_4'u - v/2 - u^2/4$ with $u = b_4'/b_4$, $v = b_4''/b_4$ (computed from the metric and equal to the record; `einstein_space_minus_extra_time_b4`), so $w_{\rm exp} = -1 - (\kappa(p_3 - p_t) - 3a_4'u + v/2 + u^2/4)/(3a_4'^2)$ for an admissible homogeneous source (`expansion_inferred_w_einstein_b4`). On the history $a_4 = Hx_4$ the observer's Hubble rate $a_4' = H$ is constant and $w_{\rm exp} = -1$ exactly, with no time variation, for every $b_4(x_4)$.

## 4. Method

### 4.1 Exact derivations first

Every effective formula is derived exactly (sympy) for the metric with $b_4(x_4)$ before any number is computed: `derive_effective.py` for dirac16complex (39 checks, `Revision/dark_sector/dirac16complex/reports/derivation-checks.json`) and `derive_eos.py` (implementation A) for dirac16complex00 (49 checks, `Revision/dark_sector/dirac16complex00/reports/python-derive-eos.json`). Both re-derive the conservation identities from the author's metric with their own Christoffel symbols; the dirac16complex00 side uses the author's gammas T16 of `Revision/algebra/gammas.json` (record `gammas_clifford_author_T16`). The key formulas are verified a second time in Wolfram from the author's metric, the author's Lovelock tensors and the author's T16 (`verify_dark_sector_b4.wls`, 8 checks, `Revision/dark_sector/reports/wolfram-dark-sector-b4.json`). Labels: EXACT means verified by exact symbolic computation in a named check; APPROXIMATION, ASSUMPTION and INTERPRETATION are marked where they apply.

### 4.2 The conservation identities as checks of the numerics

The exact identities of section 3.1 test every numerical history. For the Kohn-Sham gas: $dE/da_4 = -3X - 2P_t$ ($\beta = 4/3$) with fourth-order differences of $E$ against the solver's energy-momentum integrals, maximal relative deviation 6.351e-06 (the truncation error of the stencil on the $N = 8$ interacting series, whose $E$ falls like $e^{-2a_4}$, is about 6.7e-06; record `conservation_with_b4_term`); the $b_4$-free identity of the withdrawn record fails on the interacting series, by 1.630e+00 (`conservation_without_b4_term_fails`): the $b_4$ term is required by the solver's own numbers; integrated with Simpson's rule, 3.585e-07 (`conservation_integrated_simpson`); $dw_{\rm eff}/da_4$ two ways, 6.394e-07 for the gas and 3.532e-05 at the end slices of the $N = 8$ series (one-sided stencils; `derivative_two_ways`); the hidden-direction identity $p_{0,y} + 6Hp_0 = 3H(p_3 + p_t)$ in every state, 1.951e-08 (`y_conservation_every_state`). For dirac16complex00 the independent implementation B checks along each run that the Krein charge per coordinate volume $b_4^{3/2}Q$ is conserved (drift at most 1.2612134e-13), that the solution is on shell ($|L_0|$ at most 1.3322676e-15) and that the conservation identity with the $b_4$ term holds (relative residual at most 4.7810141e-08 by finite differences; records `B_run_*_invariants`).

### 4.3 The Kohn-Sham history (dirac16complex)

In the metric with $b_4$ the good-sector state is $\Psi = b_4^{-3/4}\chi$, where $\chi$ solves the $b_4$-free good-sector equation (`Revision/kohn_sham/reports/ks-b4-wolfram.json`); the mean field $\lambda S$ has $S = b_4^{-3/2}\bar\chi\chi$, and the solver's exchange functional is quadratic in the densities, so $\chi$ solves that equation at the coupling $\lambda_{\rm eff} = \hat\lambda\,e^{-2a_4}$ on the history, with $\hat\lambda = \lambda\,b_4(0)^{-3/2}$ the calibrated couplings of the Kohn-Sham record; the integrals $E, P_3, P_t, P_0$ are those of $\chi$. `run_ks_history.py` runs the Revision Rust Kohn-Sham solver (`Revision/kohn_sham/solver`, its single-state command, read-only use) at the 41 slices $a_4 = 0, 0.05, \dots, 2$ for $N = 8, 136, 688$ and the five calibrated couplings $\hat\lambda = 0, \pm\lambda_1, \pm\lambda_2$ per $N$, each at its $\lambda_{\rm eff}$: 615 runs (15 series x 41 slices), with $H = m = 1$, $L = 3$, tip $\theta = 0$, $T = 0$ (records `all_runs_succeeded`, `coupling_follows_b4`). The history is a PRESCRIBED BACKGROUND: the gas is a test field without back-reaction, and the states are instantaneous (adiabatic) ground states. At $a_4 = 0$ ($\lambda_{\rm eff} = \hat\lambda$) the 15 states equal the committed Kohn-Sham record, maximal relative deviation 0.000e+00 (`a4_0_states_equal_committed_record`); the $\lambda = 0$ series do not feel $b_4$ and equal the record at all five committed slices (`lambda0_series_independent_of_b4`); the occupied label set is the same at all 41 slices of every series, so the instantaneous ground states are the adiabatically continued states (`occupied_labels_fixed_along_history`); the particle number holds to 2.442e-15 (`particle_number_every_state`). `compute_eos.py` evaluates $w_{\rm eff}$ for the three definitions with the $b_4$ terms, the ratios, CPL tangents and fits, the condensate, mixtures and the Unite comparison (15 checks).

An INDEPENDENT second implementation, `independent_free_gas.py` (numpy; Chebyshev collocation with $n = 96$ and Hellmann-Feynman level derivatives; no solver output used except for the final comparison), treats the free gas ($\lambda = 0$, which does not feel $b_4$; `free_gas_independent_of_b4`). It reproduces the exact $k = 0$ spectra to 1.421e-14 (`exact_k0_spectra`), is converged ($n = 96$ against 128: 6.01e-15 in $E$, `collocation_converged`), reproduces the solver's $E(a_4)$ over 82 states to 1.897e-12 (`energy_vs_rust_solver`), $w_{\rm eff}(A) = X/E$ to 1.492e-12 (`w_eff_vs_primary`) and the CPL tangents to 4.027e-07 (`cpl_tangent_vs_primary`).

### 4.4 Condensates

The homogeneous condensate is an exact solution for both fields and every $b_4$: $b_4^{3/2}S$ is constant, $\rho = mS + \lambda S^2/2$ and $p_3 = p_t = p_0 = \lambda S^2/2$ (records `condensate_rho_p`, `condensate_b4_scaling`, `condensate_rho_p_w`). For dirac16complex00 it solves $d_4\Phi = \mathcal{A}\Phi$ with $\mathcal{A} = -\gamma^{(x_4)}(M - 3H\gamma^{(x_0)}) - \frac34(b_4'/b_4)$, $M = m + U'(S)$; $C\mathcal{A} + \mathcal{A}^TC = -\frac32(b_4'/b_4)C$ for the author's T16, so $b_4^{3/2}S$ is constant, and $K_{x_4} = MS$ exactly (records `condensate_S_b4_T16`, `condensate_K4_equals_MS_T16`, `D4_condensate_b4_T16`, with the negative control `condensate_negative_control`). The ratio drifts: $dw/da_4 = -3\beta m\lambda S/(2m + \lambda S)^2$ (`condensate_ratio_time_dependence_b4`, `condensate_observer_b4`, `D8_condensate_drift`).

### 4.5 Modes and Krein-signed energies (dirac16complex00)

For a plane wave with physical 3-momentum $k$ and extra-time momentum $q$ in the frozen local frame, $h^2 = (m^2 + k^2 - q^2)I_{16}$, so $\omega^2 = m^2 + k^2 - q^2$: the extra times are time-like and $q$ enters with the opposite sign (`mode_dispersion_h_squared`). $Bh$ is Hermitian, so the charge density $Q = \Phi^\dagger B\Phi$ is the Krein form of the frozen-frame evolution and is conserved by it (`mode_generator_B_selfadjoint`). On the real-frequency eigenspaces of the test cases of section 6.2, $T^\mu{}_\nu = k^\mu k_\nu Q/\omega$ exactly, so $\rho = \omega Q$: the energy has the sign of $\omega Q$. In the deflating field the physical extra-time momentum is $q\,e^{a_4}b_4^{-1/2} \propto a^{1 - \beta/2}$ (`extra_time_momentum_blueshift_b4`), $a^{1/3}$ on the history.

### 4.6 Gases, mixtures and wave packets

dirac16complex00: adiabatic (WKB) gases of plane-wave modes in the deflating local model, an APPROXIMATION: the warp $\sin^{1/6}z$ and $\tan z$ are frozen at a fixed hidden position (wavelengths short compared with $1/H$), the Krein charge of each mode per coordinate volume is an adiabatic invariant, and the superposition is incoherent. Each component has $\rho_i = \omega_iQ_ib_4^{-3/2}$ and $\varepsilon_i = w_{\rm eff}(B)_i = (k_p^2 + (1 - \beta/2)q_p^2)/(3\omega_i^2) \geq 0$ for $\beta < 2$, independent of the sign of $Q$ (records `wkb_mode_gas_conservation_b4`, `wkb_epsilon_sign_free_b4`); a mixture has $w_{\rm eff}(B) = \sum\varepsilon_i\rho_i/\sum\rho_i$ and $w_{\rm eff}(C) = w_{\rm eff}(B) - 1 + \beta/2$ (`mixture_weighted_average_b4`). Implementation B integrates the full 16-component field equation of the local model with the author's T16, including the $b_4$ term $\frac34(b_4'/b_4)\gamma^{(x_4)}$ (exact Krein-preserving exponential midpoint step times the exact factor of the $b_4$ term, $H/m = 10^{-3}$, adiabatic), and rebuilds the models from its solutions; spatial averages of superpositions equal the sums of the mode contributions (`B_superposition_average`). dirac16complex: mixtures of the Kohn-Sham gas with a condensate, $w_{\rm eff} = \sum_iX_i/\sum_iE_i - s + (\beta/2)(\sum_iP_{t,i}/\sum_iE_i + s)$ (`mixture_general_b4`); the kinetic gas of flat-limit modes satisfies the identity with $b_4$ (`flat_mode_gas_conservation_b4`, `D5_kinetic_gas_b4`).

### 4.7 Phantom conditions

dirac16complex: $w_{\rm eff}(C) + 1 = X/E + (\beta/2)(1 + P_t/E)$; with $\beta > 0$ and $P_t/E \geq -1$ a value below $-1$ needs $X/E < 0$; with $E > 0$ this needs $P_t > P_3$, which no real-frequency mode supplies (per mode $X = (k_p^2 + q_p^2)/(3\omega) \geq 0$, with $p_3 \geq 0$ and $p_t \leq 0$), otherwise $E < 0$ together with $X > 0$ (records `phantom_condition_b4`, `flat_mode_X_nonnegative`). Negative $E$ is not specific to a negative-norm (Krein) sector in the canonical Kohn-Sham record: there the interacting $N = 8$, $\lambda > 0$ good-sector states have $E < 0$, with $X = 0$ exactly (section 5.2), from the interaction energy of the canonical uniform-gas exchange functional ($E = 0$ at $\lambda = 0$). With the exact Fock exchange in place of that functional, solved self-consistently (the exact-Fock variant of the Kohn-Sham record, `Revision/kohn_sham/results/exx/exact-fock-variant.csv`), the same $N = 8$ states have $\lvert E\rvert \leq 2.04 \times 10^{-13}$ (computed at the canonical slices $a_4 = 0, 0.5, 1, 1.5, 2$, with the same $E$ at each); the exact exchange evaluated to first order on the canonical orbitals still leaves $E < 0$, of smaller magnitude. This negative $E$ is therefore a property of the approximate functional; good-sector states with $E < 0$ are not established beyond it. For free modes $E < 0$ needs a negative Krein charge, outside the positive good-sector realisation (OPEN). dirac16complex00 (EXACT within the WKB model): if every component has $\rho_i \geq 0$ and a real frequency, then $w_{\rm eff}(B) \geq 0$ and $w_{\rm eff}(C) \geq -1 + \beta/2 = -1/3$ at every $a$ at which these conditions hold (an extra-time mode loses its real frequency past its turning point $a_*$, section 6.3); going below $-1/3$, and in particular crossing $-1$, needs a component of negative classical energy. A condensate ratio is phantom exactly for $\lambda S/m \in (-2, -1)$ (`condensate_phantom_interval`), at an instant: on the history $\lambda S/m$ falls like $e^{-2a_4}$.

## 5. Results for dirac16complex

Records: `Revision/dark_sector/dirac16complex/reports/` and `Revision/dark_sector/dirac16complex/outputs/eos-summary.json`.

### 5.1 The condensate

$X = 0$ and $P_t/E = w_c$, so $w_{\rm eff}(A) = w_{\rm eff}(B) = (\beta/2)w_c$ and $w_{\rm eff}(C) = -1 + (\beta/2)(1 + w_c)$, with the ratio $w_c = \lambda S/(2m + \lambda S)$ drifting because $b_4^{3/2}S$ is constant (`condensate_w_eff_b4`, `condensate_ratio_w`, `condensate_b4_scaling`). The ratio equals the Unite constant $w = -0.764$ at $\lambda S/m = -382/441 = -0.866213151927$, with $\rho/(mS) = 0.566893424036$, so $\rho > 0$ if and only if $mS > 0$ (`condensate_ratio_equal_unite_constant_w`, `condensate_ratio_value`). This value of $\lambda S/m$ is CHOSEN to give -0.764: one parameter tuned to one number. On the history it holds at one instant only: $\lambda S/m$ falls like $e^{-2a_4}$, and at that value the ratio has $w_a = -2.695392$ (thawing sign); $w_{\rm eff}(A) = (2/3)w_c = -0.509333$ and $w_{\rm eff}(C) = -1/3 + (2/3)w_c = -0.842667$, both with $w_a = -1.796928$ (`condensate_drifts_with_b4`). For $\lambda S/m < 0$ the condensate energy $mS_0(1 + u/2)$ reaches 0 in the past.

### 5.2 The Kohn-Sham gas

- The occupied levels lie on the brane band, which is massless at $k = 0$ (the brane zero mode at $\varepsilon = 0$, slope $c\,e^{-a_4}$ with $c = 1.9051482536$ at small $k$; `brane_band_slope`). The gas therefore redshifts like radiation, not like dust: $d\ln E/da_4$ goes from -0.8787 at $a_4 = 0$ to -0.9549 at $a_4 = 2$ ($N = 688$, $\lambda = 0$), toward the radiation value $-1$.
- Over all $N = 136, 688$ series and all slices, $w_{\rm eff}(A) = X/E + (2/3)P_t/E$ lies in [0.292903, 0.326429] and rises monotonically toward $1/3$ (`gas_radiation_like_band`, `gas_X_over_E_rises_toward_one_third`).
- $N = 688$, $\lambda = 0$: $w_{\rm eff}(A) = w_{\rm eff}(B)$ goes from 0.2929 to 0.3183 and $w_{\rm eff}(C)$ from -0.0404 to -0.0150. The ratio $w_3 = P_3/E$ equals $X/E$ up to $|P_t/E| \leq 0.002$ over the $N = 136, 688$ series ($P_t$ is the integrated interaction part; it vanishes at $\lambda = 0$). The hidden-direction ratio $w_{x_0} = P_0/E$ goes from 0.3535 to 0.6482: a pressure that the 3-space observer does not see as pressure.
- CPL tangents ($N = 688$, $\lambda = 0$):

| $a_{4,\rm today}$ | 0.5 | 1 | 1.5 | 2 |
| --- | --- | --- | --- | --- |
| $w_0$ under (C) | -0.0370 | -0.0315 | -0.0240 | -0.0150 |
| $w_a$ (every definition) | -0.00905 | -0.01292 | -0.01701 | -0.01775 |

  ($w_0$ under (A), (B) is $w_0(C) + 1/3$.) Least-squares fits at $a_{4,\rm today} = 2$: over $a \in [1/2, 1]$, $w_a = -0.02424$ and constant proxy $-0.0205$ under (C); over $[1/3, 1]$, $w_a = -0.02648$ and $-0.0229$.
- Over all $N = 136, 688$ series: tangent $w_a$ in [-0.017766, -0.009043], fitted $w_a$ in [-0.026521, -0.019590], $w_{\rm eff}(C)$ in [-0.040430, -0.006905] (`gas_cpl_thawing_sign_small`, `gas_C_near_zero_on_b4_history`): the thawing sign, with magnitudes far below the Unite 0.60, and $w_{\rm eff}(C)$ close to 0, dust-like, not a dark-energy value (the withdrawn $b_4 = 1$ record had -0.707 to -0.672).
- $N = 8$ with $\lambda \neq 0$ (only the $k = 0$ brane zero modes, pure interaction energy at $\hat\lambda e^{-2a_4}$): $P_3 = P_t$ ($X = 0$); $E(2)/E(0)$ in [0.018402, 0.019031] ($e^{-4} = 0.018316$); $P_t/E$ in [0.931316, 0.999997], so $w_{\rm eff}(A) = (2/3)P_t/E$ in [0.620877, 0.666665] and $w_{\rm eff}(C) = w_{\rm eff}(A) - 1/3$; $E < 0$ for $\lambda > 0$ (`n8_interacting_zero_modes_dilute_with_b4`; a property of the canonical uniform-gas exchange functional, section 4.7). $N = 8$ with $\lambda = 0$ has $E = 0$: no equation of state.

### 5.3 The bulk band (independent implementation)

The massive bulk band (odd brane parity, $\varepsilon(0)$ = 1.292292828069 = the bulk edge) shows the dark-matter-like law: for the lowest odd-parity level of the $n_2 = 1$ shell, $w_{\rm eff}(A)$ falls monotonically from 0.239626 at $a_4 = -3$ to 2.268e-03 at $a_4 = 4$, asymptotically like $1/a$ (the ratio $w(4)/w(3.75) = 0.765177$ against $e^{-0.25} = 0.778801$: a linear term of $\varepsilon(k)$ at small $k$); the brane-band level of the same shell stays in [0.291594, 0.333275], tending to $1/3$ (records `bulk_band_dark_matter_law`, `brane_band_radiation_law`; free gas, $\lambda = 0$, which does not feel $b_4$). The canonical $T = 0$ states ($N \leq 688$) are filled below the bulk edge and do not populate that band.

### 5.4 Mixtures with a condensate

For a radiation-like gas ($X = E/3$, $P_t = 0$, independent of $b_4$) plus a $\lambda = 0$ condensate ($E = mS_0$, constant for every $b_4$), $w_{\rm eff}(A) = \frac13\,r/(1+r)$ with $r = r_0/a$ and $w_{\rm eff}(C) = w_{\rm eff}(A) - 1 + \beta/2$ (`mixture_radiation_condensate_cpl_b4`); $w_{\rm eff}(C) = -0.861$ at $a = 1$ needs $\beta$ in (-0.388667, 0.278000], so on the history ($\beta = 4/3$) no such mixture exists: there $w_{\rm eff}(C)$ lies in $[-1/3, 0)$ (`mixture_C_matching_w0_unite_b4`). With the computed gas ($N = 688$, $\lambda = 0$, $a_{4,\rm today} = 2$):

- with a $\lambda = 0$ condensate, $w_{\rm eff}(C) \geq -0.333015$ at every slice and gas fraction: neither -0.861 nor a constant -0.764 is reached (`mixture_C_cannot_reach_unite_w0_with_lambda0_condensate`; on the withdrawn record a CHOSEN gas fraction gave $w_{\rm eff}(C) = -0.861$ with a freezing slope);
- with a condensate of any ratio $w_c \in [-3, 0.99]$ today, drifting with $b_4$, any gas fraction and $a_{4,\rm today} \in \{0.5, 1, 1.5, 2\}$, the closest points to the Unite pair $(-0.861, -0.60)$ are $(-0.3, -0.78)$ in the ratio definition (distance 0.5891697548245), $(-0.2733333333333, -0.7708)$ under (A), (B) (distance 0.6119842735815) and $(-0.58, -0.6758666666667)$ under (C) (distance 0.2910614215438, the pure condensate with $w_c = -0.37$ today); among mixtures with $|w_0 + 0.861| \leq 0.1$ the slope $w_a$ is at most -2.639515126434 under (C) (`mixture_scan_three_definitions_b4`).

### 5.5 Phantom and crossing of $-1$

No computed Kohn-Sham state crosses $w = -1$: every state with $E \neq 0$ has $X \geq 0$ and $P_t/E \geq -1$, so $w_{\rm eff}(C) \geq -1 + \beta/2$ for $E > 0$. The exception is not a Kohn-Sham state: a condensate has $X = 0$ and $P_t/E = w_c$, so $w_{\rm eff}(C) = -1/3 + (2/3)w_c$ is below $-1$ exactly while its ratio is, $\lambda S/m \in (-2, -1)$ (`condensate_phantom_interval`, `condensate_observer_b4`); with $\lambda < 0$ and $mS > 0$ (positive energy, attractive self-interaction) the drift $\lambda S/m \propto e^{-2a_4}$ carries it into that window toward the past, for $\lambda S/m = -382/441$ today from $a = \sqrt{382/441} = 0.9307$ back to $a = \sqrt{191/441} = 0.6581$, where its energy vanishes. The $N = 8$, $\lambda > 0$ states have $E < 0$ (from the canonical uniform-gas exchange functional; section 4.7), $X = 0$ and $P_t/E$ in [0.931316, 0.999997], so $w_{\rm eff}(C) = (2/3)P_t/E - 1/3$ between 0.2875 and 0.3333; the 41 $N = 8$, $\lambda = 0$ states have $E = 0$ and no equation of state (section 5.2). On the history the expansion reads $w_{\rm exp} = -1$ exactly (section 3.3).

## 6. Results for dirac16complex00

Records:

- the reports in `Revision/dark_sector/dirac16complex00/reports/`;
- implementation A: `Revision/dark_sector/dirac16complex00/eos-theory.json`;
- the independent implementation B, the field-equation runs: `Revision/dark_sector/dirac16complex00/results/independent-numerics.json`.

### 6.1 The condensate

As for dirac16complex: $b_4^{3/2}S$ constant, $w_{\rm eff}(B) = (2/3)w$, $w_{\rm eff}(C) = -1/3 + (2/3)w$, the ratio $w = \lambda S/(2m + \lambda S)$ drifting (`condensate_observer_b4`). The ratio equals -0.764 at $\lambda S/m = -382/441$ (CHOSEN), which with $\rho > 0$ needs $mS > 0$ and $\lambda < 0$, a negative potential $U$ (`condensate_ratio_equals_unite_constant_w`); there its $w_a$ is $-84231/31250 = -2.695392$ (`condensate_ratio_drift_at_unite_value`); it is phantom exactly while $\lambda S/m \in (-2, -1)$, and then $w_{\rm eff}(C) < -1$ as well; the drift carries a $\lambda < 0$ condensate into that window toward the past (section 5.5). The condensate is not the source of the history: the author's equations need the constant source of section 2.4, while $S$ decays like $b_4^{-3/2} \propto e^{-2Hx_4}$ (`condensate_cannot_source_branch`); in Einstein gravity a $b_4(x_4)$ needs $T^{x_4}{}_{x_0} \neq 0$, which a condensate does not have. The observer's expansion reads $w_{\rm exp} = -1$ exactly on $a_4 = Hx_4$.

### 6.2 Modes, Krein-signed energies and growing modes

For the three test cases $(m, k, q) = (3, 4, 0)$, $(5, 0, 3)$ and $(4, 4, 4)$, with $\omega = \pm5$, $\pm4$ and $\pm4$, every real-frequency eigenspace has dimension 8 and a Krein form of signature (4,4), and on it $\rho = \omega Q$ exactly (records `mode_krein_inertia_*`, `mode_emt_*`, negative control `mode_emt_negative_control`): at every real frequency there are modes of both energy signs. Implementation B confirms it: at $\omega = 1.25$ the vectors with $Q = +1$ and $Q = -1$ have $\rho = +1.25$ and $-1.25$ (`B_krein_signed_energy`). The general statement is the Krein-inertia theorem of `Revision/pairing`.

For $q^2 > m^2 + k^2$ the modes grow: for $(m, k, q) = (3, 0, 5)$, $\omega = 4i$; the growing eigenspace is Krein-neutral ($Q = 0$, $\rho = 0$) with a growing extra-time pressure $p_5 = -mS$ (`growing_mode_krein_neutral`, `growing_mode_extra_time_pressure`). In the deflating field the physical extra-time momentum $q\,a\,b_4^{-1/2} \propto a^{1/3}$ grows, so every mode with $q \neq 0$ reaches a turning point $a_*$ and then grows: the deflation drives the growth. Implementation B, past the turning point $a_* = 6.2639848$ of the mode of M3: growth rate $d\ln|\phi|/dx_4 = 0.30893327$ against the WKB rate $\sqrt{sa^{2/3} - 1} - \frac34 b_4'/b_4 = 0.31165344$ (`B_growth_rate`); the amplitude grows by a factor $10^{16.20}$ between $a = 5.5$ and $7.4$, and the energy density becomes large and negative ($\rho/Q$ = -4.3193205e+29 at $a = 7.4$, for $H/m = 10^{-3}$).

### 6.3 The models M1 to M5

Each model is normalised to $\rho_{\rm tot} = 1$ at $a = 1$; definition (C) unless stated. The models keep the physical parameters of the withdrawn $b_4 = 1$ record, where they were CHOSEN to reproduce Unite numbers; on the history with $b_4(x_4)$ they no longer reproduce them.

| model | content | parameters |
| --- | --- | --- |
| M1 | condensate (exact solution for every $a_4$, $b_4$) | $\lambda S/m$ free; the ratio is $-0.764$ at $\lambda S/m = -382/441$ at one instant (CHOSEN) |
| M2 | positive-energy good-sector gas, $q = 0$ | $k^2/(k^2+m^2) = 417/1000$ at $a = 1$, CHOSEN on the withdrawn record for $w_0 = -0.861$ |
| M3 | positive-energy extra-time mode, $k = 0$ | $s = q_p^2/m^2 = 417/1417$, CHOSEN on the withdrawn record for $w_0 = -0.861$ |
| M4 | condensate + positive extra-time mode | $s = 264037/403037$ and $\Omega_q = 57963/264037$, both CHOSEN on the withdrawn record to solve tangent $= (-0.861, -0.60)$ |
| M5 | M4-type + GHOST: massless modes of negative classical energy | $G = 3/10$ of the total at $a = 1$ (a stated choice); $s$ and $\Omega_q$ CHOSEN on the withdrawn record so that its fit over $[1/2, 1]$ was $(-0.861, -0.60)$ |

The resulting CPL numbers under (C) on the history (tangent; least-squares fit over $[1/2, 1]$; constant proxy):

| model | tangent $w_0$ | tangent $w_a$ | fit $w_0$ | fit $w_a$ | proxy | crosses $-1$ on $[1/3, 1]$? |
| --- | --- | --- | --- | --- | --- | --- |
| M1 | $-1/3 + 2w/3$ | $8u/(3(2+u)^2)$ | drifts | drifts | drifts | no |
| M2 | -0.1943 | +0.162074 | -0.1988 | 0.2173 | -0.1445 | no |
| M3 | -0.2870 | -0.043770 | -0.2871 | -0.0420 | -0.2976 | no |
| M4 | -0.2870 | -0.066667 | -0.2882 | -0.0502 | -0.3007 | no |
| M5 | -0.3465 | -0.1964 | -0.3327 | -0.3231 | -0.4135 | no |

M2 is freezing ($w_a > 0$), M3, M4 and M5 have the thawing sign ($w_a < 0$); none reaches the Unite pair or crosses $-1$ on $[1/3, 1]$; the column says nothing about $a > 1$, and past the turning point $a_*$ of an extra-time mode (M3: 6.2640, M4: 1.8859, M5: 2.3375) the frequency of that mode is imaginary and the bound of section 4.7 does not apply. On the withdrawn record the M4 tangent and the M5 fit equal the Unite pair by construction. Records:

| record | record | record |
| --- | --- | --- |
| `M2_tangent_exact_b4` | `M3_tangent_exact_b4` | `M4_withdrawn_tuning_on_b4_history` |
| `positive_models_bounded_by_minus_one_third` | `unite_w0_requires_dominant_ghost` | `M5_withdrawn_composition_on_b4_history` |
| `unite_line_fit_proxy` | `unite_crossing_point` | `condensate_ratio_drift_at_unite_value` |

Notes:

- M2 under (B) and in the ratio: tangent $(0.139, 0.162074)$, the law $w_{\rm eff}(B) = \frac13k^2/(k^2 + m^2a^2)$ from $1/3$ to 0, independent of $b_4$: a time-varying dark-matter-like equation of state. Exactly, under (C), $(w_0, w_a) = (-583/3000, 81037/500000)$.
- M3: $\omega^2 = m^2(1 - sa^{2/3})$ and $w_{\rm eff}(C) = -\frac13 + \frac19\,sa^{2/3}/(1 - sa^{2/3}) \geq -1/3$ for $a < a_*$; exactly $(w_0, w_a) = (-287/1000, -196963/4500000)$; the turning point is at $a_* = (1417/417)^{3/2} = 6.2640$, in the future (withdrawn record: $(-0.861, -0.393926)$, $a_* = 1.843$).
- M4: on the history its $w_{\rm eff}(C)$ has the minimum -0.33280216468 over $a = 1/300, \dots, 1$; it reaches its turning point at $a_* = 1.8859$ and then grows.
- M5: $s = 0.5678$, $\Omega_q = 0.5947$, condensate fraction $\Omega_c = 0.7053$; on the history no crossing of $-1$ on $[1/3, 1]$ (the withdrawn record had one, at $a = 0.779$); its turning point is at $a_* = 2.3375$.
- The positive models are bounded: the minima of $w_{\rm eff}(C)$ over $a = 1/300, \dots, 1$ are -0.194333333333, -0.332598868774 and -0.33280216468 for M2, M3, M4, all $\geq -1/3$ (`positive_models_bounded_by_minus_one_third`).
- The Unite $w_0$ needs a dominant ghost: a ghost component lowers $w_{\rm eff}(C)(1)$ by at most $G/3$ and positive components raise it, so $w_0 = -0.861$ needs $G \geq 1583/1000$; for condensate + ghost the total energy then vanishes at $a = G/(1 + G) = 1583/2583$ inside $[1/2, 1]$, where $w_{\rm eff}$ diverges (`unite_w0_requires_dominant_ghost`).

### 6.4 The independent implementation B

B rebuilds M2 to M5 from solutions of the 16-component field equation with the $b_4$ term; all tangents, fits and constant proxies agree with implementation A to within 2.2666232e-05 (records `B_vs_A_*`). B also measures $w_{\rm eff}(C)$ directly from the dilution of the proper density of its solutions, independently of the formula of section 3.1; the two agree to within 4.0240551e-05 (`B_dilution_equals_formula_*`). The condensate dilutes with $b_4^{3/2}$: $b_4^{3/2}\rho$ is constant to 1.2610746e-13 while $\rho$ changes by a relative range 0.91990032 over $a \in [0.3, 1.06]$ (`B_condensate_dilutes_with_b4`). M5 has no crossing of $-1$ (`B_vs_A_M5_crossing`). By bisection on the field-equation solutions B finds $s = 0.29429162$ for M3 (A: $417/1417 = 0.2942837$; `B_solve_M3_s`), and the positive models have $w_{\rm eff}(C) \geq$ -0.31820563 on $a \in [0.35, 1]$ (`B_positive_models_bounded`).

## 7. Comparison with the Unite values

| Unite value | dirac16complex | dirac16complex00 | by construction? |
| --- | --- | --- | --- |
| constant $w = -0.764$ | condensate ratio at $\lambda S/m = -382/441$ at one instant (8-dimensional ratio, drifting with $w_a = -2.695392$) | condensate ratio at $\lambda S/m = -382/441$, $\lambda < 0$, at one instant | yes: one parameter for one number |
| $w_0 = -0.861$ | not reached with a $\lambda = 0$ condensate ($w_{\rm eff}(C) \geq -0.333015$); a drifting condensate under (C) reaches it only with $w_a \leq$ -2.639515126434 | not reached by positive models ($w_{\rm eff}(C) \geq -1/3$); needs a ghost fraction $\geq 1583/1000$ | the condensate value is chosen; no positive model reaches it |
| $(w_0, w_a) = (-0.861, -0.60)$ | not reached: closest distance 0.2910614215438 under (C) | not reached; on the withdrawn record M4 (tangent) and M5 (fit) reached it by construction | on the withdrawn record: two parameters for two numbers |
| phantom past, crossing of $-1$ at $a = 0.7683$ | no crossing in any Kohn-Sham state; a drifting $\lambda < 0$ condensate crosses at $a = 0.9307$ (for $-382/441$ today) | no crossing in M2 to M5; M1 ($\lambda < 0$) as for dirac16complex | the condensate value is chosen; the ghost fraction is a stated choice |

A model with as many tuned parameters as matched numbers reproduces them by construction and is NOT a prediction. No parameter of M2 to M5, of the mixtures or of the condensate ratio is selected by the field equations; nothing in this record selects their populations. A ghost (negative-energy) component is a ghost-like sector, not an established physical state: dirac16complex00 has one at every real frequency, and its classical energy is unbounded below (the classical form of the spin-statistics problem of a commuting field with a first-order Lagrangian).

What is not tuned: the signs and the ranges. For positive-energy content with real frequencies $w_{\rm eff}(C) \geq -1/3$ on the history in the WKB model of dirac16complex00 (section 4.7; for M3 and M4 before the turning point $a_*$ of the extra-time mode), and every computed dirac16complex state has $X \geq 0$ (section 5.5); the computed dirac16complex gas has the thawing sign with $\lvert w_a\rvert \leq 0.026521$ and $w_{\rm eff}(C)$ close to 0.

## 8. The lead's analysis (SPEC section 11), checked point by point

1. “The 7-volume of the metric is constant.” CORRECTED for the metric with $b_4$: the proper 7-volume element is $b_4^{3/2}\cos z$, independent of $a_4$ but changing with $x_4$ through $b_4$ (`proper_7_volume_element_b4`, `local_model_volume_b4`); it was constant only on the withdrawn $b_4 = 1$ metric.
2. “The effective 4-dimensional density is $\rho_4 \sim \rho_8c^3$.” With $c = e^{-a_4}b_4^{1/2}$ this is definition (B) (with (A) of the same scaling). It is an ASSUMPTION about the observer: definition (C), per unit proper 7-volume, is equally consistent with the field equations and shifts every $w_{\rm eff}$ by exactly $-1 + \beta/2$, $-1/3$ on the history (section 3).
3. “Non-relativistic quanta give dust, relativistic quanta radiation.” CONFIRMED under (A), (B) in the flat (warp-free) limit for every $b_4$: a massive mode with $q = 0$ has $w_{\rm eff} = k^2/(3(M^2a^2 + k^2))$, $1/3 \to 0$, and a massless one $1/3$ (`massive_mode_w_eff_law`, `massless_mode_w_eff`, `massive_mode_cpl_tangent`); the Kohn-Sham gas has $d\ln E/da_4$ approaching $-1$ (section 5.2).
4. “A Kohn-Sham gas whose 3-momenta redshift has a time-varying equation of state from $1/3$ towards 0.” NOT FOUND in the computed states: the occupied levels lie on the massless brane band and $w_{\rm eff}(A)$ RISES toward $1/3$ (section 5.2). The falling law is present for quanta of the massive bulk band (section 5.3), which the computed ground states do not populate. For dirac16complex00 the falling law holds for a positive-energy gas of good-sector modes (M2). The hidden-direction pressure ($w_{x_0}$ = 0.3535 to 0.6482) and the extra-time pressure were computed; the 3-space observer does not see them as pressure.
5. “A homogeneous condensate has constant $w$ while $\rho_4 \sim a^{-3}$; the ratio and $w_{\rm eff} = 0$ disagree; 4-dimensional energy is exchanged with the extra dimensions.” CORRECTED for the metric with $b_4$: $b_4^{3/2}S$ is constant, so the condensate's ratio drifts and, for $\lambda \neq 0$, $w_{\rm eff}(B) = (\beta/2)w \neq 0$ (`condensate_w_eff_b4`, `condensate_observer_b4`); for $\lambda = 0$, $w_{\rm eff}(B) = 0$ and $w_{\rm eff}(C) = -1/3$. The exchange reading is an INTERPRETATION of the disagreement between the ratio and the dilution.
6. “Whether any state gives a time-varying dark-energy equation of state near the Unite values must be computed.” COMPUTED: for dirac16complex no computed state comes near the Unite pair in any definition (section 5); for dirac16complex00 no positive-energy model gives dark-energy-like values on the history (sections 6.3 and 7).
7. “Crossing $w = -1$ needs negative kinetic energy, which the indefinite (Krein) energy of the extra-time sector and the commuting field dirac16complex00 may supply.” EXAMINED. Positive-energy extra-time momentum does NOT supply it: its pressure $p_t \leq 0$ increases $X$, so it moves $w_{\rm eff}$ up, not down (`flat_mode_X_nonnegative`, `wkb_epsilon_sign_free_b4`; M3 has $w \geq -1/3$ before its turning point $a_* = 6.2640$). What is needed is negative classical ENERGY: dirac16complex00 has it at every real frequency (Krein signature (4,4)), and on the history it would have to exceed the positive energy (section 6.3), as a ghost-like sector. For dirac16complex no computed state has $X < 0$; the only states with $E < 0$ ($N = 8$, $\lambda > 0$, negative with the canonical uniform-gas exchange functional; with the exact Fock exchange solved self-consistently $\lvert E\rvert \leq 2.04 \times 10^{-13}$, section 4.7) have $X = 0$ exactly. Modes of dirac16complex with extra-time momentum lie outside the good sector and are OPEN.

## 9. Verdicts

### 9.1 dirac16complex (Hypothesis)

- Dark matter. Under (A), (B): a time-varying dark-matter-like equation of state, $w_{\rm eff}$ falling from $1/3$ toward 0, is present in the theory for quanta of the massive bulk band (0.239626 at $a_4 = -3$ to 2.268e-03 at $a_4 = 4$ for one shell; the flat-limit law is exact and independent of $b_4$). It is NOT present in the computed Kohn-Sham ground states, whose brane-band gas is radiation-like with $w_{\rm eff}$ rising toward $1/3$. A $\lambda = 0$ condensate is dust-like ($w_{\rm eff}(B) = 0$).
- Dark energy. Not found on the history with $b_4(x_4)$: under (C) the gas has $w_{\rm eff}(C)$ in [-0.040430, -0.006905] with a thawing-sign slope (tangent $w_a$ in [-0.017766, -0.009043], fitted in [-0.026521, -0.019590]); only a drifting condensate gives negative values, with $w_a$ near $-1.8$ to $-2.7$; the Unite constant $w = -0.764$ is matched only by the 8-dimensional ratio of a tuned condensate at one instant. No computed state crosses $w = -1$.
- On the history the observer's expansion reads $w_{\rm exp} = -1$ exactly.

### 9.2 dirac16complex00 (Hypothesis00)

- Dark matter. Under (B) and in the ratio $p_3/\rho$: a positive-energy gas of good-sector modes has the time-varying law from $1/3$ to 0 (M2), independent of $b_4$; a $\lambda = 0$ condensate is dust-like.
- Dark energy without ghosts. Not on the history with $b_4(x_4)$: positive-energy content with real frequencies has $w_{\rm eff}(C) \geq -1/3$ (section 4.7; M2: -0.1943, M3 and M4: -0.2870 today); for M3 and M4 this holds before the turning point $a_*$ of the extra-time mode (M3: 6.2640, M4: 1.8859). The thawing slope of the extra-time mode is small (M3: -0.043770) because its physical momentum grows only like $a^{1/3}$; past $a_*$ the mode grows without bound and its energy density becomes large and negative (implementation B).
- Phantom and crossing of $-1$. Impossible with positive-energy components of real frequency (section 4.7); the Unite $w_0$ alone needs, from such components, a component of negative classical energy larger than the positive energy ($G \geq 1583/1000$), a ghost-like sector. The exception is a condensate with $\lambda < 0$ and $mS > 0$: while its drifting ratio lies in the window $\lambda S/m \in (-2, -1)$ the observer reads $w_{\rm eff}(C) = -1/3 + (2/3)w_c < -1$ (section 5.5); its value is CHOSEN and no source of the history selects it.
- The source of the history: the author's equations need the constant source $\kappa(\rho, p_3, p_t, p_0) = (-2/27, -2/9, -22/27, -14/27)$ (a negative energy density for $\kappa > 0$); no condensate is it.

### 9.3 The hypotheses

This record establishes neither Hypothesis nor Hypothesis00. What it shows, under its stated assumptions, on the author's metric with $b_4(x_4)$: both fields contain time-varying equations of state of the dark-matter type under definition (B) (dirac16complex only for bulk-band quanta, which the computed states do not populate); no dark-energy-like value arises from positive-energy content under any definition; the Unite numbers are not reproduced, and on the withdrawn $b_4 = 1$ record they were reproduced only by models whose parameters were chosen to reproduce them. Nothing in this record establishes that either field is dark energy or dark matter.

## 10. What remains open

1. A self-consistent history with an admissible source. No recorded Kohn-Sham state is an admissible source of the author's metric: its energy-momentum tensor depends on $x_0$ and violates the algebraic condition of the field equations, and the history is a prescribed background (the 6 checks of `Revision/field_equations_a4/reports/ks-source-conditions.json`, among them `ks_profiles_depend_on_x0`, `ks_profiles_violate_algebraic_condition` and, for the metric with $b_4$, `ks_verdict_holds_for_every_b4`). The source that the author's equations require on the history (section 2.4) is not constructed from the fields of this record; a condensate is not it.
2. Populated bulk-band or thermal states along the history (fixed entropy); only $T = 0$ ground states and $a_4 \in [0, 2]$ (the solver's validated range) are computed; $b_4(0)$ enters only through $\hat\lambda$.
3. Modes of dirac16complex with extra-time momentum (outside the good sector; only their flat-limit sign structure is derived) and the non-adiabatic (time-dependent) Kohn-Sham problem.
4. For dirac16complex00: configurations that depend on $x_0$ are not consistent sources of the metric; the WKB model freezes the hidden-direction warp; the growing modes make the Cauchy problem ill-posed, and nothing here cures that; no quantum treatment (a classical field).
5. Which normalisation of $\rho_4$, if any, describes a physical 3-space observer; the value of $a_{4,\rm today}$.
6. What would select the populations of M2 to M5, the mixture fractions or the condensate's $\lambda S/m$.
7. A supernova likelihood (distances, covariances): no fit to data is part of this record.
8. Histories with $\beta < 0$, on which the $b_4$ term lowers $w_{\rm eff}$; no source of this record selects one.

## 11. Verification records

### 11.1 Reports and their counts

Every check has a name, a verdict and a detail. Counts at the time of writing (the publication test re-reads them):

| report | checks | PASS | FAIL |
| --- | --- | --- | --- |
| `Revision/dark_sector/dirac16complex/reports/derivation-checks.json` | 39 | 39 | 0 |
| `Revision/dark_sector/dirac16complex/reports/ks-history-run.json` | 7 | 7 | 0 |
| `Revision/dark_sector/dirac16complex/reports/eos-checks.json` | 15 | 15 | 0 |
| `Revision/dark_sector/dirac16complex/reports/independent-checks.json` | 10 | 10 | 0 |
| `Revision/dark_sector/dirac16complex00/reports/python-derive-eos.json` | 49 | 49 | 0 |
| `Revision/dark_sector/dirac16complex00/reports/python-independent-numerics.json` | 32 | 32 | 0 |
| `Revision/dark_sector/reports/wolfram-dark-sector-b4.json` | 8 | 8 | 0 |
| `Revision/field_equations_a4/reports/ks-source-conditions.json` | 6 | 6 | 0 |

### 11.2 Checks per report

The tables list every check of the seven dark-sector reports; every one has the verdict PASS.

**dirac16complex, derive_effective.py** (39 checks):

| check | check | check |
| --- | --- | --- |
| `sqrt_det_g_equals_b4_three_halves_cos_z` | `proper_7_volume_element_b4` | `proper_3_and_extra_time_volume_scalings_b4` |
| `conservation_x4_identity_b4` | `conservation_x0_identity` | `conservation_other_components_vanish` |
| `conservation_equals_a4_record_b4` | `hidden_coordinate_dy_dx0` | `conservation_x0_in_y_form` |
| `integrated_identity_dE_dx4_b4` | `w_eff_A_b4` | `w_eff_B_equals_w_eff_A_b4` |
| `w_eff_C_b4` | `w_eff_general_normaliser_b4` | `w_eff_difference_to_withdrawn_record` |
| `condensate_rho_p` | `condensate_b4_scaling` | `condensate_ratio_w` |
| `condensate_ratio_time_dependence_b4` | `condensate_w_eff_b4` | `condensate_ratio_equal_unite_constant_w` |
| `flat_mode_mass_shell_b4` | `flat_mode_gas_conservation_b4` | `flat_mode_X_nonnegative` |
| `massive_mode_w_eff_law` | `massive_mode_cpl_tangent` | `massless_mode_w_eff` |
| `extra_time_momentum_blueshift_b4` | `mixture_general_b4` | `mixture_radiation_condensate_cpl_b4` |
| `mixture_C_matching_w0_unite_b4` | `cpl_least_squares_rule` | `unite_deep_past` |
| `expansion_inferred_w` | `einstein_mixed_component_b4` | `einstein_space_minus_extra_time_b4` |
| `expansion_inferred_w_einstein_b4` | `author_weights_b4_branch` | `phantom_condition_b4` |

**dirac16complex, run_ks_history.py** (7 checks):

| check | check | check |
| --- | --- | --- |
| `all_runs_succeeded` | `a4_0_states_equal_committed_record` | `lambda0_series_independent_of_b4` |
| `coupling_follows_b4` | `occupied_labels_fixed_along_history` | `y_conservation_every_state` |
| `particle_number_every_state` |  |  |

**dirac16complex, compute_eos.py** (15 checks):

| check | check | check |
| --- | --- | --- |
| `formulas_input_present` | `dense_history_complete` | `conservation_with_b4_term` |
| `conservation_without_b4_term_fails` | `conservation_integrated_simpson` | `derivative_two_ways` |
| `gas_radiation_like_band` | `gas_X_over_E_rises_toward_one_third` | `gas_C_near_zero_on_b4_history` |
| `n8_interacting_zero_modes_dilute_with_b4` | `condensate_ratio_value` | `condensate_drifts_with_b4` |
| `mixture_C_cannot_reach_unite_w0_with_lambda0_condensate` | `mixture_scan_three_definitions_b4` | `gas_cpl_thawing_sign_small` |

**dirac16complex, independent_free_gas.py** (10 checks):

| check | check | check |
| --- | --- | --- |
| `exact_k0_spectra` | `brane_band_slope` | `collocation_converged` |
| `aufbau_closed_shells` | `energy_vs_rust_solver` | `w_eff_vs_primary` |
| `cpl_tangent_vs_primary` | `bulk_band_dark_matter_law` | `brane_band_radiation_law` |
| `free_gas_independent_of_b4` |  |  |

**dirac16complex00, derive_eos.py (A)** (49 checks):

| check | check | check |
| --- | --- | --- |
| `gammas_clifford_author_T16` | `conservation_negative_control` | `conservation_x4_author_metric_b4` |
| `conservation_x0_author_metric` | `conservation_other_components_vanish` | `conservation_x4_local_model_b4` |
| `local_model_volume_b4` | `observer_N1_weff_identity_b4` | `observer_N2_weff_identity_b4` |
| `observer_hidden_average_commutes` | `condensate_S_b4_T16` | `condensate_negative_control` |
| `condensate_K4_equals_MS_T16` | `condensate_rho_p_w` | `condensate_observer_b4` |
| `condensate_phantom_interval` | `condensate_ratio_equals_unite_constant_w` | `condensate_ratio_drift_at_unite_value` |
| `author_weights_vacuum_recovered` | `branch_required_source` | `condensate_cannot_source_branch` |
| `mode_dispersion_h_squared` | `mode_generator_B_selfadjoint` | `mode_emt_negative_control` |
| `mode_krein_inertia_m3_k4_q0_pos` | `mode_emt_m3_k4_q0_pos` | `mode_krein_inertia_m3_k4_q0_neg` |
| `mode_emt_m3_k4_q0_neg` | `mode_krein_inertia_m5_k0_q3_pos` | `mode_emt_m5_k0_q3_pos` |
| `mode_krein_inertia_m5_k0_q3_neg` | `mode_emt_m5_k0_q3_neg` | `mode_krein_inertia_m4_k4_q4_pos` |
| `mode_emt_m4_k4_q4_pos` | `mode_krein_inertia_m4_k4_q4_neg` | `mode_emt_m4_k4_q4_neg` |
| `growing_mode_krein_neutral` | `growing_mode_extra_time_pressure` | `wkb_mode_gas_conservation_b4` |
| `wkb_epsilon_sign_free_b4` | `mixture_weighted_average_b4` | `unite_line_fit_proxy` |
| `unite_crossing_point` | `M2_tangent_exact_b4` | `M3_tangent_exact_b4` |
| `M4_withdrawn_tuning_on_b4_history` | `positive_models_bounded_by_minus_one_third` | `unite_w0_requires_dominant_ghost` |
| `M5_withdrawn_composition_on_b4_history` |  |  |

**dirac16complex00, independent_numerics.py (B)** (32 checks):

| check | check | check |
| --- | --- | --- |
| `B_clifford_numeric` | `B_krein_matrix` | `B_krein_signed_energy` |
| `B_superposition_average` | `B_run_kmode_invariants` | `B_run_q3_invariants` |
| `B_run_q4_invariants` | `B_run_q5_invariants` | `B_run_cond_invariants` |
| `B_run_ghost_invariants` | `B_ghost_negative_energy` | `B_condensate_dilutes_with_b4` |
| `B_vs_A_M2_N2` | `B_vs_A_M2_N1` | `B_vs_A_M2_ratio` |
| `B_dilution_equals_formula_M2` | `B_vs_A_M3_N2` | `B_vs_A_M3_N1` |
| `B_vs_A_M3_ratio` | `B_dilution_equals_formula_M3` | `B_vs_A_M4_N2` |
| `B_vs_A_M4_N1` | `B_vs_A_M4_ratio` | `B_dilution_equals_formula_M4` |
| `B_vs_A_M5_N2` | `B_vs_A_M5_N1` | `B_vs_A_M5_ratio` |
| `B_dilution_equals_formula_M5` | `B_vs_A_M5_crossing` | `B_solve_M3_s` |
| `B_positive_models_bounded` | `B_growth_rate` |  |

**dark sector, verify_dark_sector_b4.wls (Wolfram)** (8 checks):

| check | check | check |
| --- | --- | --- |
| `D1_volume_b4` | `D2_conservation_b4` | `D3_w_eff_general_b4` |
| `D4_condensate_b4_T16` | `D5_kinetic_gas_b4` | `D6_author_weights_branch` |
| `D7_branch_required_source` | `D8_condensate_drift` |  |

### 11.3 Re-verification for this document

For this document (2026-10-15) the seven dark-sector scripts were run in the order of section 12 on the committed inputs (`Revision/kohn_sham/results`, `Revision/algebra/gammas.json`, `Revision/field_equations_a4/a4-equations.json`, `Revision/metric_b4/results`) with the built Revision Rust solver: 39 of 39, 7 of 7, 15 of 15, 10 of 10, 49 of 49, 32 of 32 and 8 of 8 checks passed, and every output and report file was byte-identical over two runs. The Kohn-Sham source-conditions report (6 of 6) is the committed file. The reports cited in this document are the committed files.

## 12. Reproduction

From the repository root, in this order. Each script exits 0 only if all its checks pass; its outputs are LF and two runs are byte-identical. The dirac16complex scripts write into their own `outputs/` and `reports/` folders, and each reads the outputs of the scripts before it; `run_ks_history.py` needs the built Rust solver (`--solver PATH` selects another binary). The dirac16complex00 scripts accept `--out DIR`, and `independent_numerics.py` reads implementation A's `eos-theory.json` for its comparison; the Wolfram verifier reads `eos-theory.json` for its comparison of the required source. The second unittest command and the PDF command are each one command; the backslash is the line continuation of a POSIX shell. Python needs numpy and sympy (no scipy).

```text
cargo build --release --manifest-path Revision/kohn_sham/solver/Cargo.toml
python Revision/dark_sector/dirac16complex/derive/derive_effective.py
python Revision/dark_sector/dirac16complex/compute/run_ks_history.py
python Revision/dark_sector/dirac16complex/compute/compute_eos.py
python Revision/dark_sector/dirac16complex/independent/independent_free_gas.py
python Revision/dark_sector/dirac16complex00/python/derive_eos.py
python Revision/dark_sector/dirac16complex00/python/independent_numerics.py
wolframscript -file Revision/dark_sector/wolfram/verify_dark_sector_b4.wls
python -m unittest \
    Revision/dark_sector/dirac16complex00/tests/test_dark_sector_dirac16complex00.py -v
python scripts/build_provenance_pdf.py Revision/docs/DARK_SECTOR_HYPOTHESES.md \
    --developer-layout --specifications Revision/pdf-specifications.json
python -m unittest Revision/tests/test_dark_sector_hypotheses_publication.py -v
```

Expected output and run times measured for this document (2026-10-15, a development machine shared with other jobs; on an idle machine the times are shorter):

| command | last line of the output | time |
| --- | --- | --- |
| `derive_effective.py` | 39/39 checks pass | 3.6 s |
| `run_ks_history.py` | PASS - particle_number_every_state (the seventh of 7 PASS lines) | 24 s |
| `compute_eos.py` | 15/15 checks pass | 0.3 s |
| `independent_free_gas.py` | 10/10 checks pass | 77 s |
| `derive_eos.py` | derive_eos: 49/49 checks pass | 3.5 s |
| `independent_numerics.py` | independent_numerics: 32/32 checks pass | 6.7 s |
| `verify_dark_sector_b4.wls` | 8/8 checks passed | 5.2 s |
| `test_dark_sector_dirac16complex00.py` | OK (4 tests) | 11 s |
| `build_provenance_pdf.py` | provenance_pdf=OK | 5 s |
| `test_dark_sector_hypotheses_publication.py` | OK (skipped=1); with REVISION_PDF_REBUILD=1: OK | below 1 s; 5 s |

The cargo build was not re-timed (the solver was already built). The PDF build runs the Markdown-to-LaTeX builder twice (with different hash seeds), runs pdflatex three times into each of two fresh directories, requires warning-free logs and byte-identical PDFs, and checks the PDF against its entry `dark-sector-hypotheses` in `Revision/pdf-specifications.json` (the Revision registry; the registry of the earlier stages is not touched).

## 13. What is proved, computed, assumed and not established

### 13.1 Proved (exact, by symbolic computation in the named checks)

1. For the author's metric with $b_4(x_4)$: the proper 7-volume element $b_4^{3/2}\cos z$; the conservation identities $d\rho/dx_4 = -3a_4'(p_3 - p_t) - \frac32(b_4'/b_4)(\rho + p_t)$ and $dp_0/dx_0 + 3H\cot z(2p_0 - p_3 - p_t) = 0$ for diagonal sources $T(x_0, x_4)$ (sympy and Wolfram).
2. The observer identity $w_{\rm eff} = X/E - s + (\beta/2)(P_t/E + s)$ for the normalisations (A), (B) ($s = 0$) and (C) ($s = 1$), and its N1/N2 form for dirac16complex00.
3. The condensate: an exact homogeneous solution of both fields with $b_4^{3/2}S$ constant, its drifting ratio, $w_{\rm eff}(B) = (\beta/2)w$ and $w_{\rm eff}(C) = -1 + (\beta/2)(1 + w)$; the ratio $-0.764$ at $\lambda S/m = -382/441$ at an instant; the phantom window $(-2, -1)$.
4. The history: with the author's weights a source without $T^{x_4}{}_{x_0}$ allows $d\ln b_4/da_4 = 4/3$ on $a_4 = Hx_4$, and there needs the constant source $\kappa(\rho, p_3, p_t, p_0) = (-2/27, -2/9, -22/27, -14/27)$ (two independent computations); no condensate is it; in Einstein gravity a $b_4(x_4)$ needs $T^{x_4}{}_{x_0} \neq 0$.
5. The flat-limit mode laws (massive $1/3 \to 0$ independent of $b_4$, massless $1/3$, $X \geq 0$ for real frequencies) and the expansion-inferred $w_{\rm exp}$, $-1$ exactly on $a_4 = Hx_4$ for every $b_4$.
6. dirac16complex00: on the three test eigenspaces, dimension 8, Krein signature (4,4) and $\rho = \omega Q$; the growing eigenspace is Krein-neutral; within the WKB model, positive-energy components of real frequency give $w_{\rm eff}(B) \geq 0$ and $w_{\rm eff}(C) \geq -1 + \beta/2$; the exact tangents of M2 and M3 on the history; the ghost fraction $1583/1000$ needed for the Unite $w_0$.

### 13.2 Computed (numerical, with the stated tolerances and two implementations)

The Kohn-Sham gas along the history with $b_4(x_4)$ (615 states at $\lambda_{\rm eff} = \hat\lambda e^{-2a_4}$; radiation-like, $w_{\rm eff}(A)$ in [0.292903, 0.326429] rising toward $1/3$; $w_{\rm eff}(C)$ in [-0.040430, -0.006905]), with the conservation identity including the $b_4$ term; its CPL tangents and fits, the mixtures and the scans; the bulk-band law (independent implementation); the models M2 to M5 on the history; implementation B of dirac16complex00 (field-equation runs with the $b_4$ term, agreement with A to within 2.2666232e-05, $w_{\rm eff}$ from the dilution of the proper density, the growth past the turning point).

### 13.3 Assumed

1. The normalisation (A), (B) or (C) of $\rho_4$: an ASSUMPTION about the observer; every verdict is stated for each.
2. The history $a_4 = Hx_4$, $b_4 = b_4(0)e^{(4/3)Hx_4}$ as a PRESCRIBED BACKGROUND (test fields, no back-reaction); the instantaneous (adiabatic) Kohn-Sham states; $a_{4,\rm today}$; $b_4(0)$ through $\hat\lambda$.
3. The Z2 brane at $z = \pi/2$ (ASSUMED) and the filling convention of `Revision/kohn_sham/ks-theory.json`. The canonical uniform-gas exchange functional of the Kohn-Sham states is an APPROXIMATION; with the exact Fock exchange solved self-consistently the $N = 8$, $\lambda > 0$ states have $\lvert E\rvert \leq 2.04 \times 10^{-13}$ (section 4.7).
4. The WKB/local model of dirac16complex00 (frozen warp, adiabatic Krein charges, incoherent superposition): an APPROXIMATION, measured by implementation B.
5. The populations, fractions and condensate parameters of every model: CHOSEN (those of M2 to M5 on the withdrawn record to reproduce the Unite numbers there).

### 13.4 Not established

1. A dark-energy or dark-matter mechanism of either field: this record establishes neither Hypothesis nor Hypothesis00, and nothing in this record establishes that either field is dark energy or dark matter.
2. Any Unite value as an output of the field equations: no positive-energy content reaches them on the history, and every match of the withdrawn record was by construction (sections 6.3 and 7).
3. That the ghost-like sector of dirac16complex00 is a physical state; that a time-varying dark-matter equation of state arises in the computed dirac16complex states; that any computed state crosses $w = -1$; that any good-sector state of dirac16complex has $E < 0$ beyond the canonical uniform-gas exchange functional (section 4.7).
4. A fit to supernova data; a self-consistent cosmological history; a source of the fields of this record for the history with $b_4(x_4)$; the open problems of section 10.
