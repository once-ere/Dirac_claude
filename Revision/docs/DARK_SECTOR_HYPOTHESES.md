# Dark-sector hypotheses for dirac16complex and dirac16complex00: the equation of state seen from 3-space

## Hypothesis and Hypothesis00 investigated in the author's primordial gravitational field with exponentially deflating extra times, in the corrected metric of 2026-10-16 (version 2) with the two functions $a_4(x_4)$ and $b_4(x_4)$: the observer assumption, the method, the results for each field, the comparison with the Supernovae Unite values, the verdicts and what remains open

## Abstract

The author asked on 2026-10-01 that two hypotheses be investigated: that dirac16complex (Hypothesis) and dirac16complex00 (Hypothesis00) provide a possible physical mechanism for a time-varying dark-energy equation of state and/or a time-varying dark-matter equation of state. This document reports what the Revision computation found for the corrected primordial metric of 2026-10-16 (version 2; `Revision/SPEC.md` section 1),

$$
g = \mathrm{diag}\big(e^{-2a_4}b_4\cot^2 z,\ e^{2a_4}\,(\times3),\ -1,\ -e^{-2a_4}b_4(\sin^2 z)^{1/6}\,(\times3)\big),\qquad z = 6Hx_0\ \text{real},
$$

in which the hidden direction shrinks with the extra times; $b_4$ is a function of $x_4$, and every result below is computed with it. The metric of 2026-10-14 and its version 1 of 2026-10-16 are withdrawn, and no number of this document comes from their records. Every number is read from a named Revision report. The history of the numbers is $a_4 = Hx_4$ with $b_4(x_4) = b_4(0)\,e^{(4/3)Hx_4}$, a PRESCRIBED background kept from the earlier record: with the author's weights it needs an anisotropic source that grows with $x_4$, which no field of this record supplies. The equation of state that a 3-space observer infers is not fixed by the field equations alone: the extra times $x_5, x_6, x_7$ are time-like and deflate exponentially, and the 4-dimensional density $\rho_4$ needs an ASSUMPTION about how the observer normalises over them and over the hidden direction. For the three stated definitions (A), (B) and (C) the dilution-inferred equation of state obeys exactly $w_{\rm eff} = P_3/E + (\beta/2 - 1)(P_0 + 3P_t)/(3E) - s\,(4 - 2\beta)/3$ with $\beta = d\ln b_4/da_4$, $s = 0$ for (A), (B) and $s = 1$ for (C); on the history ($\beta = 4/3$) every verdict moves by exactly $-4/9$ between (A, B) and (C). dirac16complex: the computed Kohn-Sham gas (615 instantaneous states along the history, solved at the coupling that the growing cell dictates) is radiation-like: without interaction it is an exact fold-band gas with $w_{\rm eff}(A) = 1/3$ exactly at every slice and $w_{\rm eff}(C) = -1/9$, and with interaction $w_{\rm eff}(A)$ stays in [0.330585, 0.336132]; the massive bulk band, blue-shifted by the shrinking hidden direction, does not follow the dust-like law $1/3 \to 0$ (its $w_{\rm eff}(A)$ falls from 0.318721 to -0.081074 for one shell), and the computed ground states do not populate it; nothing computed comes near the Unite pair $(w_0, w_a) = (-0.861, -0.60)$ except a drifting condensate with a CHOSEN ratio (closest distance 0.1604394909208, under (C)), and no computed Kohn-Sham state crosses $w = -1$. dirac16complex00, in the WKB model (no hidden momentum, an APPROXIMATION): a positive-energy gas of good-sector modes has the dark-matter-like law $1/3 \to 0$ under (B), independent of $b_4$, and every positive-energy mode gas with real frequencies has $w_{\rm eff}(C) \geq -4/9$, so such gases reach the Unite $w_0$ only with a ghost-like component, and $w_0 = -0.861$ needs a ghost fraction of at least 3749/3000 of the total energy; the exception is a condensate with $\lambda < 0$ and $mS > 0$ (positive energy, not a mode gas), whose $w_{\rm eff}(C) = (5/9)w - 4/9$ is -0.868889 at the CHOSEN ratio -0.764. The condensate's ratio drifts: it equals the Unite constant $w = -0.764$ at $\lambda S/m = -382/441$ only at one instant. A model with as many tuned parameters as matched numbers reproduces them by construction and is NOT a prediction. This record establishes neither Hypothesis nor Hypothesis00; it states what each field can and cannot produce under its stated assumptions.

## 1. The hypotheses and the short answer

The author's hypotheses, quoted from `Revision/README.md`:

- “Hypothesis: dirac16complex provides a possible physical mechanism for a time-varying dark energy equation of state and/or a possible physical mechanism for a time-varying dark matter equation of state, both of which you will investigate.”
- “Hypothesis00: dirac16complex00 provides [the same], both of which you will investigate.”

`Revision/SPEC.md` section 8 makes both hypotheses questions to be INVESTIGATED, not assumed: for each field, the equation of state seen by a 3-space observer as the extra times deflate and 3-space inflates (the condensate, the Kohn-Sham gas, mixtures), its time dependence, the CPL parameters, and the comparison with the Supernovae Unite values. Section 11 of the same file records the lead's analysis, to be checked; section 8 of this document checks it point by point.

The short answer (details and records in sections 3 to 9):

1. The observer's $\rho_4$ is an ASSUMPTION (section 3). Every verdict below is stated for each definition; on the history the definitions (A, B) and (C) differ by exactly $4/9$.
2. dirac16complex, dark matter: not found. The computed free Kohn-Sham gas is an exact fold-band gas with $w_{\rm eff}(A) = 1/3$ at every slice (radiation-like, with no time variation), the interacting gas stays near $1/3$, and the massive bulk band, which the computed ground states do not populate, falls through 0 to negative values instead of approaching 0 (section 5.3). The dust-like law $1/3 \to 0$ holds exactly only for a flat-limit 3-space quantum without hidden or extra-time momentum.
3. dirac16complex, dark energy: not found in the computed states. Under (C) the free gas has $w_{\rm eff}(C) = -1/9$ and the interacting gas lies in [-0.113860, -0.108312]; only a drifting condensate with a CHOSEN ratio gives values near the Unite $w_0$, with a slope steeper than the Unite slope; no Kohn-Sham state crosses $w = -1$, and a drifting $\lambda < 0$ condensate crosses $-1$ toward the past (section 5.5).
4. dirac16complex00, dark matter: a positive-energy gas of good-sector modes (WKB model, no hidden momentum) has the time-varying law $1/3 \to 0$ under (B) and in the ratio $p_3/\rho$, independent of $b_4$; the same law holds for the flat-limit 3-space quanta of dirac16complex (item 2).
5. dirac16complex00, dark energy: not with positive-energy mode gases: $w_{\rm eff}(C) \geq -4/9$ for them in the WKB model (real frequencies, no hidden momentum), and from them the Unite $w_0$ needs a ghost-like component larger than the positive energy; only the condensate with a CHOSEN $\lambda S/m < 0$ and $mS > 0$ gives values near the Unite $w_0$ (section 6.1).
6. On the history $a_4 = Hx_4$ the observer's expansion itself reads $w_{\rm exp} = -1$ exactly, for every $b_4(x_4)$.

## 2. Setting and conventions

### 2.1 The corrected metric and the author's coordinates

The coordinates are the author's, $x_0, x_1, \dots, x_7$, in the author's order (`Dirac_Einstein-Lovelock_4+4_Nash.nb`, input cell In[48]: `X = {x0[], x1[], x2[], x3[], x4[], x5[], x6[], x7[]}`): $x_0$ is the hidden space-like direction, with $z = 6Hx_0$ real (every real value) and $H > 0$ the author's constant; $x_1, x_2, x_3$ are ordinary 3-space (inflating); $x_4$ is the time; and $x_5, x_6, x_7$ are the three extra times, which are time-like and DEFLATE exponentially as $a_4$ increases. The metric is the corrected metric of 2026-10-16 (version 2; `Revision/SPEC.md` section 1; the record of the correction is `Revision/metric_warped/`),

$$
\begin{aligned}
ds^2 = {} & e^{-2a_4(x_4)}\,b_4(x_4)\cot^2 z\,dx_0^2 + e^{2a_4(x_4)}\big(dx_1^2+dx_2^2+dx_3^2\big) - dx_4^2 \\
& - e^{-2a_4(x_4)}\,b_4(x_4)\,(\sin^2 z)^{1/6}\,\big(dx_5^2+dx_6^2+dx_7^2\big) ,
\end{aligned}
$$

of signature (4,4) wherever $\sin z\cos z \neq 0$, with $b_4(x_4) > 0$ a function of $x_4$ and $(\sin^2 z)^{1/6}$ the positive root, so that the metric is defined for every real $z$ with $\sin z \neq 0$ (no branch of $\sin z$ is chosen). It differs from the withdrawn metric of 2026-10-14 in two entries: the hidden direction carries the factor $e^{-2a_4}b_4$ of the extra times, and 3-space carries no warp. The volume element is $\sqrt{|g|} = e^{-a_4}b_4^2\lvert\cot z\rvert\,\lvert\sin z\rvert^{1/2}$ (`sqrt_det_g`; every $x_0$ derivative is taken with rules valid on both signs of $\sin z$, `x0_derivative_rules_every_real_z`). The 3-space scale factor is $e^{a_4}$; the extra-time scale factor is $e^{-a_4}b_4^{1/2}(\sin^2 z)^{1/12}$, and the hidden direction has the scale factor $e^{-a_4}b_4^{1/2}\lvert\cot z\rvert$: it shrinks with the extra times. The observer's scale factor is $a = e^{a_4 - a_{4,\rm today}}$, normalised to $a = 1$ at a chosen “today” $a_{4,\rm today}$ (a free parameter); $b_4$ does not enter it. Along a history $\beta = d\ln b_4/da_4 = b_4'/(a_4'b_4)$. The Kohn-Sham records use the hidden coordinate $y = \ln\lvert\sin z\rvert/(6H)$ (`hidden_coordinate_dy_dx0`): in a Kohn-Sham cell $y \in [-L, 0]$, the fold $\cos z = 0$ at $y = 0$ joins the two halves of a cell, and $y = -L$ is the tip. Both halves of a cell carry the same reduced spinor (`Revision/kohn_sham/ks-theory.json`, boundaryConditions.fold): the corrected metric has no $Z_2$ orbifold and no mirror copy carrying $-m$. The record that reads the author's notebook, without evaluating it, is `Revision/dark_sector/reports/author-notebook-inputs.json` (`author_notebook_inputs.wls`): 147 cells, 113 input cells.

### 2.2 The two fields and the energy-momentum tensor

dirac16complex is $\Psi$: 16 complex anticommuting components, a Pin(4,4) spinor, quantised canonically; its energy-momentum tensor is an operator, and the numbers below are expectation values in the instantaneous Kohn-Sham states of the good sector (no extra-time momentum), in the positive realisation of the good sector (with the ASSUMED filling of both fold conditions and the chosen tip condition of the Kohn-Sham record, which make its blocks self-adjoint; the field-theory record constructs the positive realisation explicitly only for single good-sector momenta with constant coefficients). dirac16complex00 is $\Phi$: 16 complex commuting components that transform as a Pin(4,4) spinor, a classical field; its energy-momentum tensor is the classical bilinear, whose energy has both signs (Krein-signed energies, section 6.2). Both fields have the Lagrangian of `Revision/SPEC.md` section 3 with $U(S) = \frac{\lambda}{2}S^2$, $S = \bar\Psi\Psi$; in the corrected metric the gravity term of the Dirac operator is $\gamma^\mu\Omega_\mu = \frac32He^{a_4}b_4^{-1/2}\gamma^{(x_0)} + (b_4'/b_4 - \frac12a_4')\gamma^{(x_4)}$. The energy density is $\rho = -T^{x_4}{}_{x_4}$ and the pressures are $p_\mu = T^\mu{}_\mu$ (no sum): $p_3$ of 3-space, $p_t$ of the extra times and $p_0$ of the hidden direction. For homogeneous on-shell states $\rho = mS + U$ and $p = SU' - U$. For a state of the Kohn-Sham record, $E$, $P_3$, $P_t$ and $P_0$ are the proper 7-volume integrals of $\rho$, $p_3$, $p_t$ and $p_0$ per unit coordinate volume.

### 2.3 The Unite values and the CPL convention

The author's private PDF (not part of the repository; only these numbers are used) gives the Supernovae Unite constant-$w$ fit $w = -0.764$ and the CPL fit $w(a) = w_0 + w_a(1-a)$ with $(w_0, w_a) = (-0.861, -0.60)$. In the deep past the CPL line tends to $w_0 + w_a = -1.461$ (quoted as -1.46), which is phantom; the line crosses $w = -1$ at $a = 461/600 = 0.7683$ ($z = 139/461$; record `unite_crossing_point`). In this convention thawing means $w_a < 0$ ($w$ rises from near $-1$) and freezing $w_a > 0$; the formula decides (the PDF's table states the opposite signs).

The CPL tangent of a model is $w_0 = w(1)$, $w_a = -dw/da$ at $a = 1$. The fits are least squares of $w(a)$ over $a \in [1/2, 1]$ or $[1/3, 1]$ (record `cpl_least_squares_rule`). The “constant $w$” of a model is the mean of $w(a)$ over the range, a PROXY: applied to the Unite CPL line itself it gives -1.011 on $[1/2, 1]$ and -1.061 on $[1/3, 1]$ (record `unite_line_fit_proxy`), so it is not the supernova constant-$w$ fit -0.764, which weights the data. No supernova likelihood, distance fit or covariance is computed anywhere in this record.

### 2.4 The history: a PRESCRIBED background

The numbers are computed on $a_4 = Hx_4$ (the author's $A = 1$) with $b_4(x_4) = b_4(0)\,e^{(4/3)Hx_4}$ and $b_4(0) = 1$, that is $\beta = 4/3$ and $b_4 \propto a^{4/3}$. The extra-time scale factor is then $e^{-a_4}b_4^{1/2} \propto a^{-1/3}$: the extra times deflate exponentially, and the hidden direction shrinks with them. The history is kept from the earlier record for continuity (`Revision/SPEC.md` section 1; `Revision/kohn_sham/ks-theory.json`, adiabaticity.historyBeta = 4/3): the field equations of the corrected metric do not select it. In the corrected metric the left-hand sides of the field equations have no off-diagonal component, for every $a_4(x_4)$, $b_4(x_4)$ and every real $z$, and their hidden and extra-time components are equal, so an admissible source is diagonal, independent of $x_0$ and has $p_0 = p_t$ (in Einstein gravity: `einstein_no_mixed_component`). With the author's weights $w_1 = 1$, $w_2 = 1/32$, $w_3 = 1/1152$ and $\Lambda = -10$ ($H = 1$) this history needs the source (`record_history_needs_a_source`, `history_required_source`; the Wolfram verification reads the same source from `Revision/field_equations_a4/a4-equations.json`, confirms its anisotropy and that the dirac16complex00 record states it, `D6_history_source_anisotropic`)

$$
\begin{aligned}
-\kappa\rho - \Lambda &= -\tfrac{9}{16}\xi^2 + \tfrac{161}{24}\xi + \tfrac{121}{432} ,\qquad
\kappa p_3 - \Lambda = -\tfrac{9}{16}\xi^2 + \tfrac{1601}{216}\xi - \tfrac{5359}{3888} ,\\
\kappa p_0 - \Lambda &= \kappa p_t - \Lambda = \tfrac{79}{16}\xi - \tfrac{497}{144} ,\qquad \xi = e^{2a_4}/b_4 = e^{(2/3)Hx_4} .
\end{aligned}
$$

It is anisotropic, $\kappa(p_3 - p_0) = -\tfrac{9}{16}\xi^2 + \tfrac{1069}{432}\xi + \tfrac{2015}{972} \neq 0$, it grows with $x_4$, it satisfies the conservation identity of section 3.1 exactly, and its energy density changes sign along the history: $\kappa\rho = 3.57407$ at $a_4 = 0$ and $\kappa\rho = -7.63383$ at $a_4 = 2$ (`ks_history_is_a_prescribed_background`). A condensate cannot be this source: every condensate is isotropic ($p_3 = p_t = p_0$) and its $S$ decays like $e^{-(5/3)a_4}$ (`condensate_cannot_source_history`), and the Kohn-Sham states are not admissible sources (section 10). The history is therefore a PRESCRIBED BACKGROUND for test fields.

## 3. The observer assumption: $\rho_4$ and the definitions (A), (B), (C)

### 3.1 Exact identities

The proper 3-volume of a slice $x_4 = $ const grows like $e^{3a_4}$, the proper extra-time volume shrinks like $e^{-3a_4}b_4^{3/2}$ and the proper hidden length is $f\lvert dy\rvert$ with $f = e^{-a_4}b_4^{1/2}$; the proper 7-volume of a cell therefore changes like $e^{-a_4}b_4^2 = e^{(2\beta - 1)a_4}$, like $e^{(5/3)a_4}$ on the history (`proper_volume_elements`). The conservation law $\nabla_\mu T^\mu{}_\nu = 0$ for a diagonal $T(x_0, x_4)$, re-derived from the corrected metric with Christoffel symbols computed anew in sympy and in Wolfram, gives, with $h_4 = b_4'/(2b_4) - a_4'$ the expansion rate of the hidden direction and of each extra time,

$$
\frac{d\rho}{dx_4} = -3a_4'(\rho + p_3) - h_4(\rho + p_0) - 3h_4(\rho + p_t),\qquad
\frac{dE}{da_4} = -3P_3 - \Big(\frac{\beta}{2} - 1\Big)(P_0 + 3P_t) ,
$$

and $dp_0/dx_0 + 3H\cot z\,(p_0 - p_t) = 0$, free of $a_4$ and $b_4$ (in $y$: $p_{0,y} + 3H(p_0 - p_t) = 0$). On the history $dE/da_4 = -3P_3 + P_t + P_0/3$: the 3-space pressure and the pressures of the shrinking extra times and the shrinking hidden direction change the energy with opposite signs. The records of the volumes and of these identities (the negative control: the form without the terms of the hidden direction and the extra times fails):

| record | record | record |
| --- | --- | --- |
| `sqrt_det_g` | `x0_derivative_rules_every_real_z` | `proper_volume_elements` |
| `local_model_volume` | `D1_volume` | `conservation_x4_identity` |
| `conservation_x0_identity` | `conservation_other_components_vanish` | `conservation_equals_a4_record` |
| `conservation_x4_corrected_metric` | `conservation_x0_corrected_metric` | `conservation_x4_local_model` |
| `D2_conservation` | `conservation_negative_control` | `integrated_identity_dE_dx4` |
| `integrated_identity_equals_ks_theory` | `hidden_coordinate_dy_dx0` | `conservation_x0_in_y_form` |

The 3-space observer averages over the hidden direction with the weight $\lvert\cot z\rvert\,\lvert\sin z\rvert^{1/2}$, which does not depend on $x_4$ (record `observer_hidden_average_commutes`); the factor $e^{-a_4}b_4^2$ of the proper weight is written out below. The extra times are time-like, so the observer's 4-dimensional density needs a normalisation over them and over the hidden direction. Three are recorded:

- (A) the extra times and the hidden direction are compact with a fixed coordinate period, i.e. the extra times are closed time-like directions and the hidden direction a closed space-like one; $\rho_4 = E/(\text{proper 3-volume}) \propto E\,e^{-3a_4}$;
- (B) they are non-compact and $\rho_4$ is taken per unit COORDINATE volume of the extra times and the hidden direction; $\rho_4 \propto E\,e^{-3a_4}$;
- (C) $\rho_4$ is taken per unit PROPER 7-volume; $\rho_4 \propto E\,e^{a_4}b_4^{-2}$.

In general $\rho_4 \propto E\,e^{-3a_4}(e^{-4a_4}b_4^2)^{-s}$. With the dilution-inferred equation of state $w_{\rm eff} = -1 - \frac13\,d\ln\rho_4/d\ln a$ the conservation identity gives exactly (records `w_eff_A`, `w_eff_B_equals_w_eff_A`, `w_eff_C`, `w_eff_general_normaliser`, `D3_w_eff_general`)

$$
w_{\rm eff} = \frac{P_3}{E} + \Big(\frac{\beta}{2} - 1\Big)\frac{P_0 + 3P_t}{3E} - s\,\frac{4 - 2\beta}{3},\qquad s = 0\ \text{(A, B)},\quad s = 1\ \text{(C)} .
$$

So on the history $w_{\rm eff}(A) = w_{\rm eff}(B) = P_3/E - (P_0 + 3P_t)/(9E)$ and $w_{\rm eff}(C) = w_{\rm eff}(A) - 4/9$: every verdict moves by exactly $-4/9$ between (A, B) and (C). The pressures of the hidden direction and of the extra times enter with the factor $\beta/2 - 1$, which is $-1/3$ on the history: a positive hidden pressure lowers $w_{\rm eff}$, a negative extra-time pressure raises it. The dirac16complex00 record names the same two scalings N1 (per unit coordinate volume of the extra times and the hidden direction, $\rho_4 = e^{-4a_4}b_4^2\langle\rho\rangle$, the scaling of (A) and (B)) and N2 (per unit proper 7-volume, $\rho_4 = \langle\rho\rangle$, definition (C)), with $w_{\rm eff}(N1) = w_3 + (\beta/2 - 1)(w_{x_0} + 3w_t)/3$ and $w_{\rm eff}(N2) = w_{\rm eff}(N1) - (4 - 2\beta)/3$ for isotropic sources, $w_{x_0} = p_0/\rho$ (records `observer_N1_weff_identity`, `observer_N2_weff_identity`). Below, (B) stands for (A) and (B) together and for N1, and (C) for N2. The ratio $w = p_3/\rho$ does not depend on the normalisation. `Revision/SPEC.md` section 11 writes $\rho_4 \sim \rho_8\,c^3$ with $c$ the extra-time scale factor; in the corrected metric the hidden direction has the same scale factor $c = e^{-a_4}b_4^{1/2}$, and definition (B) is $\rho_4 = c^4\langle\rho\rangle$ (section 8).

### 3.2 How every verdict depends on the assumption

The rho_4 normalisation is an ASSUMPTION about the observer, not a consequence of the field equations, and this record does not choose one. The same state reads differently under each (history $\beta = 4/3$):

| state (records) | $w_{\rm eff}$ under (A), (B) | $w_{\rm eff}$ under (C) | ratio $p_3/\rho$ |
| --- | --- | --- | --- |
| homogeneous condensate (`condensate_w_eff`) | $(5/9)\,w_c$; 0 for $\lambda = 0$ | $-4/9 + (5/9)\,w_c$ | $w_c = \lambda S/(2m+\lambda S)$, drifting |
| fold-band quanta, $\varepsilon = e^{-a_4}\lvert k\rvert$ (`fold_band_quantum_w_eff`) | $1/3$, radiation | $-1/9$ | $1/3$ |
| massive 3-space quanta, flat limit, no hidden or extra-time momentum (`massive_mode_w_eff_law`) | $k^2/(3(M^2a^2+k^2))$: $1/3 \to 0$ | $-1/9 \to -4/9$ | as (A), (B) |
| free Kohn-Sham gas, $N = 592, 2352$ (section 5.2) | $1/3$ exactly | $-1/9$ exactly | $1/3$ |
| interacting Kohn-Sham gas, $N = 592, 2352$ (section 5.2) | 0.330585 to 0.336132 | -0.113860 to -0.108312 | 0.311799 to 0.353369 |

INTERPRETATION (labelled): supernova distances measure the dilution-inferred $w_{\rm eff}$ of a 4-dimensional Friedmann observer, which agrees with the ratio $p_3/\rho$ only when no energy is exchanged with the extra times and the hidden direction. Whether (A), (B), (C) or none of them describes such an observer is not decided by any equation of this record. Under (A) the extra times are closed time-like directions; under (B) and (C) they are non-compact and a normalisation is a choice.

### 3.3 The expansion-inferred equation of state

An observer who reads $a(t) = e^{a_4(x_4)}$ with $t = x_4$ ($g_{44} = -1$, no warp of 3-space) and 4-dimensional Friedmann equations infers $w_{\rm exp} = -1 - \frac23\,a_4''/a_4'^2$ (record `expansion_inferred_w`); $b_4$ does not enter the observer's scale factor. In Einstein gravity the corrected metric has no mixed component, $R^{x_4}{}_{x_0} = 0$ for every $a_4$, $b_4$ and every real $z$, and $G^{x_0}{}_{x_0} = G^{x_5}{}_{x_5}$, so a source needs $p_0 = p_t$ (`einstein_no_mixed_component`); $G^{x_1}{}_{x_1} - G^{x_5}{}_{x_5} = \frac12\big(6H^2\xi - 4a_4'^2 + 9a_4'u + 4a_4'' - 2u^2 - v\big)$ with $u = b_4'/b_4$, $v = u' = b_4''/b_4 - u^2$ and $\xi = e^{2a_4}/b_4$ (computed from the metric and equal to the record; `einstein_space_minus_extra_time`), so $w_{\rm exp} = \big(6H^2\xi - 10a_4'^2 + 9a_4'u - 2\kappa p_3 + 2\kappa p_t - 2u^2 - v\big)/(6a_4'^2)$ for an admissible homogeneous source (`expansion_inferred_w_einstein`). On the history $a_4 = Hx_4$ the observer's Hubble rate $a_4' = H$ is constant and $w_{\rm exp} = -1$ exactly, with no time variation, for every $b_4(x_4)$.

## 4. Method

### 4.1 Exact derivations first

Every effective formula is derived exactly (sympy) for the corrected metric with general $a_4(x_4)$, $b_4(x_4)$ and every real $z$ before any number is computed: `derive_effective.py` for dirac16complex (37 checks, `Revision/dark_sector/dirac16complex/reports/derivation-checks.json`) and `derive_eos.py` (implementation A) for dirac16complex00 (48 checks, `Revision/dark_sector/dirac16complex00/reports/python-derive-eos.json`). Both re-derive the conservation identities from the corrected metric with their own Christoffel symbols; the dirac16complex00 side uses the author's gammas T16 of `Revision/algebra/gammas.json` (record `gammas_clifford_author_T16`). The key formulas are verified a second time in Wolfram from the corrected metric and the author's T16 (`verify_dark_sector.wls`, 7 checks, `Revision/dark_sector/reports/wolfram-dark-sector.json`). Its twin `verify_dark_sector_b4.wls` (`Revision/dark_sector/reports/wolfram-dark-sector-b4.json`, 8 checks) is the Wolfram record of the withdrawn metric of 2026-10-14; it is kept so that the withdrawn record stays reproducible (`Revision/dark_sector/B4_PROVENANCE.md`), and no number or check of this document comes from it. Labels: EXACT means verified by exact symbolic computation in a named check; APPROXIMATION, ASSUMPTION and INTERPRETATION are marked where they apply.

### 4.2 The conservation identities as checks of the numerics

The exact identities of section 3.1 test every numerical history. For the Kohn-Sham gas: $dE/da_4 = -3P_3 + P_t + P_0/3$ ($\beta = 4/3$) with fourth-order differences of $E$ on the dense grid (h = 0.05) against the solver's energy-momentum integrals, maximal deviation 2.103e-06 of $\max\lvert E\rvert$ (interior slices, every series with $E \neq 0$; record `conservation_identity`); integrated with Simpson's rule, 2.208e-07 (`conservation_integrated_simpson`); $dw_{\rm eff}/da_4$ two ways, 1.410e-06 (`derivative_two_ways`); the hidden-direction identity $p_{0,y} + 3H(p_0 - p_t) = 0$ in every state, maximal relative residual 5.751e-10 (the solver's own; `y_conservation_every_state`). The free series satisfy the identity in closed form: $E \propto e^{-a_4}$, $P_3 = E/3$, $P_t = P_0 = 0$ (section 5.2). For dirac16complex00 the independent implementation B checks along each run that the Krein charge per coordinate volume $e^{-a_4}b_4^2Q$ is conserved (drift at most 9.8449027e-14), that the solution is on shell ($|L_0|$ at most 1.2212453e-15) and that the conservation identity with $h_4$ holds (relative residual at most 5.542778e-08 by finite differences; records `B_run_*_invariants`).

### 4.3 The Kohn-Sham history (dirac16complex)

In the corrected metric the good-sector state is $\Psi = e^{ik\cdot x}e^{-(3/2)Hy}e^{a_4/2}b_4^{-1}\chi$, and $\chi$ solves the slice Hamiltonian $h_j = j\big[-(i/f)\sigma_1\partial_y + M_{\rm eff}\sigma_2 + e^{-a_4}k\,\sigma_3\big] + v_v$ with the hidden scale $f = e^{-a_4}b_4^{1/2}$ ($e^{-a_4/3}$ on the history) and the momentum weight $e^{-a_4}$ (called $\kappa$ in `Revision/kohn_sham/ks-theory.json`); $b_4$ enters the densities through the proper 7-volume of the cell, $\mathrm{Vol}_7 = \ell^3v_te^{-a_4}b_4^2$. The Kohn-Sham record (`Revision/kohn_sham`, moved to the corrected metric in phase W5) works with $\hat\lambda = \lambda\,b_4(0)^{-2}$, the calibrated couplings $\lambda_1 = 157.7, 2.131, 0.5363$ and $\lambda_2 = 473.1, 6.393, 1.609$ for $N = 8, 592, 2352$, and the cell volume $\mathrm{Vol}_7(a_4) = \ell^3v_te^{(5/3)a_4}$, so the effective coupling falls like $e^{-(5/3)a_4}$: the state is that of the fixed coordinate cell at $\lambda_{\rm eff} = \hat\lambda\,e^{-(5/3)a_4}$ with the same $f$ and momentum weight (the coupling-volume scaling in `ks-theory.json`); the integrals $E, P_3, P_t, P_0$ are the physical ones. `run_ks_history.py` runs the Revision Rust Kohn-Sham solver (`Revision/kohn_sham/solver`, its single-state command, read-only use) at the 41 slices $a_4 = 0, 0.05, \dots, 2$ for $N = 8, 592, 2352$ and the five couplings $\hat\lambda = 0, \pm\lambda_1, \pm\lambda_2$ per $N$: 615 runs (15 series x 41 slices), with $H = m = 1$, $L = 3$, tip $\theta = 0$, $T = 0$ (records `all_runs_succeeded`, `cell_volume_follows_b4`; every run used the cell volume of the history, maximal relative deviation 4.441e-16); the coordinate-cell form at $\lambda_{\rm eff}$ gives the same energies and pressures to 8.159e-13 in the 48 states of the interacting series at the committed slices $a_4 > 0$ (`lambda_eff_form_agrees`). The history is a PRESCRIBED BACKGROUND: the gas is a test field without back-reaction, and the states are instantaneous (adiabatic) ground states. At the five committed slices the 300 integrals of the 15 series equal the committed Kohn-Sham record, maximal relative deviation 0.000e+00 (`committed_slices_equal_committed_record`); the free series are exact fold-band gases (`lambda0_series_exact_fold_band`, section 5.2); the occupied label set is the same at all 41 slices for 15 of 15 series, so the instantaneous ground states are the adiabatically continued states (`occupied_labels_fixed_along_history`); the particle number holds to 2.554e-15 (`particle_number_every_state`). `compute_eos.py` evaluates $w_{\rm eff}$ for the three definitions, the ratios, CPL tangents and fits, the condensate, mixtures and the Unite comparison (13 checks).

An INDEPENDENT second implementation, `independent_free_gas.py` (numpy; Chebyshev collocation with n = 96 and Hellmann-Feynman level derivatives with the kinetic term $(1 - \beta/2)\partial_y/f$; no solver output used except for the final comparison), treats the free gas ($\lambda = 0$). It reproduces the exact $k = 0$ spectra to 4.086e-14 (`exact_k0_spectra`) and the fold-band level $\varepsilon = e^{-a_4}\lvert k\rvert$ to 4.58e-14, with its Hellmann-Feynman derivative $d\varepsilon/da_4 = -\varepsilon$ to 5.55e-15 (`fold_band_dispersion`); it is converged ($n = 96$ against 128: 1.05e-14 in $E$, `collocation_converged`) and fills closed shells with a gap above (`aufbau_closed_shells`); it reproduces the solver's $E(a_4)$ over 82 states to 3.568e-13 (`energy_vs_rust_solver`), $w_{\rm eff}(A)$ to 1.220e-13 (`w_eff_vs_primary`), $w_{\rm eff}(A) = 1/3$ at every slice to 1.23e-13 (`free_gas_w_eff_one_third`) and the CPL tangents to 2.737e-11 (`cpl_tangent_vs_primary`).

### 4.4 Condensates

The homogeneous condensate is an exact solution of dirac16complex00 for every $a_4$, $b_4$ (`condensate_S_T16`, `D4_condensate_T16`): $S = S_0e^{a_4}b_4^{-2}$, so $S\,\mathrm{Vol}_7$ is constant, $\rho = mS + \lambda S^2/2$ and $p_3 = p_t = p_0 = \lambda S^2/2$ (records `condensate_rho_p`, `condensate_scaling`, `condensate_rho_p_w`). For dirac16complex, the quantised $\Psi$, the same form is the mean-field condensate of the expectation values: it takes $\langle U(S)\rangle = U(\langle S\rangle)$, which is ASSUMED (the two differ in general, and the trace identity of the quantised field is ASSUMED, not proved; `Revision/field_equations_a4/a4-equations.json`, fields.dirac16complex), and it is consistent with both conservation identities (`condensate_scaling`). For dirac16complex00 it solves $d_4\Phi = \mathcal{A}\Phi$ with $\mathcal{A} = \mathcal{B} - (b_4'/b_4 - a_4'/2)I_{16}$, $\mathcal{B} = -M\gamma^{(x_4)} + \frac32He^{a_4}b_4^{-1/2}\gamma^{(x_4)}\gamma^{(x_0)}$ and $M = m + U'(S)$; $C\mathcal{A} + \mathcal{A}^TC = -2(b_4'/b_4 - a_4'/2)C$ for the author's T16, so $S = S_0e^{a_4}b_4^{-2}$, and $K_{x_4} = MS$ exactly (records `condensate_S_T16`, `condensate_K4_equals_MS_T16`, `D4_condensate_T16`, with the negative control `condensate_negative_control`). The ratio drifts: $dw_c/da_4 = (1 - 2\beta)\,2m\lambda S/(2m + \lambda S)^2$, and on the history $\lambda S/m$ falls like $e^{-(5/3)a_4}$ (`condensate_ratio_time_dependence`, `condensate_observer`, `D7_condensate_drift`).

### 4.5 Modes and Krein-signed energies (dirac16complex00)

For a plane wave with physical 3-momentum $k$ and extra-time momentum $q$ in the local frame with constant coefficients, $h^2 = (m^2 + k^2 - q^2)I_{16}$, so $\omega^2 = m^2 + k^2 - q^2$: the extra times are time-like and $q$ enters with the opposite sign (`mode_dispersion_h_squared`). $Bh$ is Hermitian, so the charge density $Q = \Phi^\dagger B\Phi$ is the Krein form of this evolution and is conserved by it (`mode_generator_B_selfadjoint`). On the real-frequency eigenspaces of the test cases of section 6.2, $T^\mu{}_\nu = k^\mu k_\nu Q/\omega$ exactly, so $\rho = \omega Q$: the energy has the sign of $\omega Q$. In the deflating field the physical extra-time momentum $q\,e^{a_4}b_4^{-1/2}$ and the physical hidden momentum $l\,e^{a_4}b_4^{-1/2}$ both grow like $a^{1 - \beta/2}$ (`extra_time_momentum_blueshift`), like $a^{1/3}$ on the history: the deflation blue-shifts them.

### 4.6 Gases, mixtures and wave packets

dirac16complex00: adiabatic (WKB) gases of plane-wave modes in the deflating local model, an APPROXIMATION: the warp $(\sin^2 z)^{1/12}$ and $\cot z$ are held fixed at a fixed hidden position (wavelengths short compared with $1/H$), the modes carry no hidden momentum, the Krein charge of each mode per coordinate volume is an adiabatic invariant, and the superposition is incoherent. Each component has $\rho_i = \omega_iQ_in$ with $n = e^{a_4}b_4^{-2}$ and $\varepsilon_i = w_{\rm eff}(B)_i = (k_p^2 + (1 - \beta/2)q_p^2)/(3\omega_i^2) \geq 0$ for $\beta < 2$, independent of the sign of $Q$ (records `wkb_mode_gas_conservation`, `wkb_epsilon_sign_free`); a mixture has $w_{\rm eff}(B) = \sum\varepsilon_i\rho_i/\sum\rho_i$ and $w_{\rm eff}(C) = w_{\rm eff}(B) - (4 - 2\beta)/3$ (`mixture_weighted_average`). Implementation B integrates the full 16-component field equation of the local model with the author's T16 in the corrected metric, including the gravity term $(b_4'/b_4 - a_4'/2)$ (integrated exactly) and the blue-shift of the extra-time momentum, with the exact Krein-preserving exponential midpoint step and $H/m = 10^{-3}$ (adiabatic), and rebuilds the models from its solutions; spatial averages of superpositions equal the sums of the mode contributions, while the pointwise interference range is 0.27738092 (`B_superposition_average`). dirac16complex: $w_{\rm eff}$ is linear in $(P_3, P_t, P_0)$ at fixed $E$, so a mixture of the gas with a condensate has $w_{\rm eff} = \sum_iP_{3,i}/\sum_iE_i + (\beta/2 - 1)\sum_i(P_{0,i} + 3P_{t,i})/(3\sum_iE_i) - s(4 - 2\beta)/3$; the kinetic gas of flat-limit modes, with $\rho = n\omega$, $p_3 = nk_p^2/(3\omega)$, $p_0 = nl_p^2/\omega$, $p_t = -nq_p^2/(3\omega)$ and $n \propto e^{a_4}b_4^{-2}$, satisfies the identity of section 3.1 exactly (`flat_mode_mass_shell`, `flat_mode_gas_conservation`, `D5_kinetic_gas`).

### 4.7 Phantom conditions

dirac16complex: $w_{\rm eff}(C) + 1 = P_3/E + (\beta/2 - 1)(P_0 + 3P_t)/(3E) + (2\beta - 1)/3$; at $\beta = 4/3$ a value $w_{\rm eff}(C) < -1$ needs $P_3/E - (P_0 + 3P_t)/(9E) < -5/9$, and $w_{\rm eff}(A) < -1$ needs it below $-1$. A real-frequency kinetic gas has $P_3 \geq 0$, $P_t \leq 0$ and $P_0 \geq 0$, so with $E > 0$ a value below $-1$ under (C) needs a large hidden kinetic pressure, $P_0 > 9E(P_3/E + 5/9)$, otherwise $E < 0$ (records `phantom_condition`, `flat_mode_gas_conservation`): for $E > 0$ and $\beta < 2$ extra-time momentum raises $w_{\rm eff}$, hidden momentum lowers it. Negative $E$ is not specific to a negative-norm (Krein) sector in the canonical Kohn-Sham record: there the interacting $N = 8$ good-sector states have $E$ of the sign of $-\lambda$ (section 5.2), from the interaction energy of the canonical uniform-gas exchange functional (the $N = 8$, $\lambda = 0$ states have $E = 0$). With the exact Fock exchange in place of that functional, solved self-consistently (the exact-Fock variant of the Kohn-Sham record, `Revision/kohn_sham/results/exx/exact-fock-variant.csv`), the same $N = 8$ states have $\lvert E\rvert \leq 4.98 \times 10^{-12}$ (computed at the canonical slices $a_4 = 0, 0.5, 1, 1.5, 2$, zero within the solver's self-consistency at each: it stops at a maximal residual $\leq 10^{-11}$, and the record requires energies to agree to $N \times 10^{-11}$; `Revision/kohn_sham/reports/ks-crosscheck.json`); the exact exchange evaluated to first order on the canonical orbitals still leaves $E < 0$ for $\lambda > 0$, of smaller magnitude. This negative $E$ is therefore a property of the approximate functional; good-sector states with $E < 0$ are not established beyond it. For free modes $E < 0$ needs a negative Krein charge, outside the positive good-sector realisation (OPEN). dirac16complex00 (EXACT within the WKB model): if every component has $\rho_i \geq 0$ and a real frequency, then $w_{\rm eff}(B) \geq 0$ and $w_{\rm eff}(C) \geq -(4 - 2\beta)/3 = -4/9$ at every $a$ at which these conditions hold (an extra-time mode loses its real frequency past its turning point $a_*$, section 6.3); going below $-4/9$, and in particular crossing $-1$, needs a component of negative classical energy. The exception is a condensate with $\lambda < 0$ and $mS > 0$: it has positive energy but is not a mode gas, and its $w_{\rm eff}(B) = (5/9)w$ is negative, so the theorem does not cover it. A condensate ratio is phantom exactly for $\lambda S/m \in (-2, -1)$ (`condensate_phantom_interval`), and because $w_{\rm eff}(C) = (5/9)(1 + w_c) - 1$ the observer then reads $w_{\rm eff}(C) < -1$ as well, at an instant: on the history $\lambda S/m$ falls like $e^{-(5/3)a_4}$.

## 5. Results for dirac16complex

Records: `Revision/dark_sector/dirac16complex/reports/` and `Revision/dark_sector/dirac16complex/outputs/eos-summary.json`.

### 5.1 The condensate

$P_3 = P_t = P_0 = w_cE$, so $w_{\rm eff}(A) = w_{\rm eff}(B) = ((2\beta - 1)/3)\,w_c = (5/9)\,w_c$ and $w_{\rm eff}(C) = (5/9)\,w_c - 4/9$, with the ratio $w_c = \lambda S/(2m + \lambda S)$ drifting because $S\,\mathrm{Vol}_7$ is constant (`condensate_w_eff`, `condensate_ratio_w`, `condensate_scaling`). The ratio equals the Unite constant $w = -0.764$ at $\lambda S/m = -382/441 = -0.866213151927$, with $\rho/(mS) = 0.566893424036$, so $\rho > 0$ if and only if $mS > 0$ (`condensate_ratio_equal_unite_constant_w`, `condensate_ratio_value`). This value of $\lambda S/m$ is CHOSEN to give -0.764: one parameter tuned to one number. On the history it holds at one instant only: $\lambda S/m$ falls like $e^{-(5/3)a_4}$, and at that value the ratio has $w_a = -2.246160$ (thawing sign); $w_{\rm eff}(A) = (5/9)\,w_c = -0.424444$ and $w_{\rm eff}(C) = (5/9)\,w_c - 4/9 = -0.868889$, both with $w_a = -1.247867$ (`condensate_drifts`). Under (C) this CHOSEN condensate lies near the Unite $w_0$, with a slope steeper than the Unite $w_a = -0.60$: a tuned value, not a prediction. For $-2 < \lambda S/m < 0$ today the condensate energy $mS_0(1 + u/2)$, $u = \lambda S/m$, reaches 0 in the past; for $\lambda S/m \leq -2$ today it is already $\leq 0$ today.

### 5.2 The Kohn-Sham gas

- The free gas is an exact fold-band gas. At $\lambda = 0$ every occupied orbital is the fold-band orbital $(e^{fMy}, 0)$ with $\varepsilon = e^{-a_4}\lvert k\rvert$, or a $k = 0$ zero mode; over the 123 states of the three free series $E_{\rm KS}(a_4) = E_{\rm KS}(0)e^{-a_4}$, $\int p_3 = \int\rho/3$ and $\int p_0 = \int p_t = 0$ to 2.333e-15 (`lambda0_series_exact_fold_band`). For $N = 592$ and 2352, $P_3/E = 1/3$ and $P_t/E = P_0/E = 0$ to 7.8e-16 and $E\,e^{a_4}$ is constant to 3.1e-15 at every slice: $w_{\rm eff}(A) = w_{\rm eff}(B) = 1/3$ exactly (radiation-like, with no time variation; it does not fall toward 0, dust), $w_{\rm eff}(C) = 1/3 - 4/9 = -1/9$ and $w_a = 0$ (`free_gas_exact_fold_band`, `fold_band_quantum_w_eff`). The $N = 8$, $\lambda = 0$ states have $E = P_3 = P_t = P_0 = 0$ (the $k = 0$ fold zero modes have $\varepsilon = 0$ and no interaction): no equation of state.
- The interacting gas ($N = 592, 2352$, $\lambda \neq 0$; 8 series): $E > 0$ at every slice; $w_{\rm eff}(A)$ in [0.330585, 0.336132], $w_{\rm eff}(C) = w_{\rm eff}(A) - 4/9$ in [-0.113860, -0.108312]; $P_t/E$ in [-3.240e-02, 3.024e-02] and $P_0/E$ in [-1.192e-01, 1.114e-01] (`interacting_gas_ranges`): pressures of the extra times and of the hidden direction that the 3-space observer does not see as pressure. The ratio $w_3 = P_3/E$ lies in [0.311799, 0.353369].
- CPL tangents of the interacting series $N = 2352$, $\hat\lambda = +\lambda_1$:

| $a_{4,\rm today}$ | 0.5 | 1 | 1.5 | 2 |
| --- | --- | --- | --- | --- |
| $w_0$ under (C) | -0.1110 | -0.1107 | -0.1106 | -0.1106 |
| $w_a$ (every definition) | -0.000743 | -0.000467 | -0.000098 | 0.000258 |

  ($w_0$ under (A), (B) is $w_0(C) + 4/9$.) Least-squares fits at $a_{4,\rm today} = 2$: over $a \in [1/2, 1]$, $w_a = 0.000046$ and constant proxy $-0.1106$ under (C); over $[1/3, 1]$, $w_a = -0.000144$ and $-0.1106$.
- Over all gas series ($N \neq 8$, every $\lambda$): tangent $w_a$ in [-0.003892, 0.003904], fitted $w_a$ in [-0.002392, 0.002261], $w_{\rm eff}(C)$ in [-0.113860, -0.108312] (`gas_cpl_far_from_unite`): magnitudes of $w_a$ far below the Unite 0.60, and $w_{\rm eff}(C)$ never near -0.861.
- $N = 8$ with $\lambda \neq 0$ (only the $k = 0$ levels, pure interaction energy at $\hat\lambda e^{-(5/3)a_4}$): $E$ has the sign of $-\lambda$ at every slice, $P_3/E$ in [0.948351, 0.998955] and $w_{\rm eff}(A)$ in [0.232167, 0.408203] (`n8_interacting_states`); $P_3 = P_t$ (the ratios $w_3$ and $w_t$ of these series coincide); the hidden-direction ratio $P_0/E$ lies in [2.117340, 3.823722], so the hidden-direction pressure exceeds $E$ in magnitude; $w_{\rm eff}(C) = w_{\rm eff}(A) - 4/9$ lies in [-0.212277, -0.036242]. $E < 0$ for $\lambda > 0$ is a property of the canonical uniform-gas exchange functional (section 4.7).

### 5.3 The bulk band (independent implementation)

The massive bulk band (odd fold parity; its lowest level at $a_4 = 0$ is the bulk edge 1.292292828069, `exact_k0_spectra`) does not show the dust-like law. For the lowest odd-parity level of the $n_2 = 1$ shell along $a_4 \in [-3, 4]$ (where $f = e^{-a_4/3}$ runs from 2.7183 to 0.2636), $w_{\rm eff}(A) = -\frac13\,d\ln\varepsilon/da_4$ falls monotonically from 0.318721 at $a_4 = -3$ to -0.081074 at $a_4 = 4$ and changes sign between $a_4 = -0.5$ and $a_4 = -0.25$: the shrinking hidden direction raises the bulk level like $1/f = e^{a_4/3}$, so $w_{\rm eff}(A)$ tends to $-1/9$ when the hidden momentum dominates (`bulk_band_w_eff`; free gas, $\lambda = 0$). The fold-band level of the same shell has $w_{\rm eff}(A) = 1/3$ at every $a_4$, to 2.87e-12 (`fold_band_radiation_law`). No canonical $T = 0$ state ($N = 8, 592, 2352$) occupies an odd-parity (bulk) level (the committed level files `Revision/kohn_sham/results/ground/levels`; the occupied label set, parity included, is fixed along the history, `occupied_labels_fixed_along_history`): the free states are filled below the bulk edge, and the interaction shifts the levels without filling the bulk band.

### 5.4 Mixtures with a condensate

For the fold-band gas ($P_3 = E/3$, $P_t = P_0 = 0$, $E \propto 1/a$ for every $b_4$) plus a $\lambda = 0$ condensate ($E = mS_0$, constant for every $b_4$), $w_{\rm eff}(A) = \frac13\,r/(1+r)$ with $r = r_0/a$, tangent $w_0 = r_0/(3(1 + r_0))$ and $w_a = r_0/(3(1 + r_0)^2) > 0$ (freezing), and $w_{\rm eff}(C) = w_{\rm eff}(A) - (4 - 2\beta)/3$ (`mixture_fold_band_gas_condensate_cpl`); $w_{\rm eff}(C) = -0.861$ at $a = 1$ needs $\beta$ in (417/2000, 1417/2000] = (0.208500, 0.708500], so on the history ($\beta = 4/3$) no such mixture exists: there $w_{\rm eff}(C)$ of this mixture lies in [-4/9, -1/9) (`mixture_C_matching_w0_unite`). With the computed free gas ($N = 2352$, $\lambda = 0$):

- with a $\lambda = 0$ condensate, $w_{\rm eff}(C) \geq -0.444111$ at every slice and gas fraction: neither -0.861 nor a constant -0.764 is reached (`mixture_C_cannot_reach_unite_w0_with_lambda0_condensate`);
- with a condensate of any ratio $w_c \in [-3, 0.99]$ today, drifting ($\lambda S/m \propto e^{-(5/3)a_4}$), any gas fraction in $[0, 1]$ and $a_{4,\rm today} \in \{0.5, 1, 1.5, 2\}$, the closest scanned points to the Unite pair $(-0.861, -0.60)$ are those of the next three items (`mixture_scan_three_definitions`);
- $(-0.35, -0.7875)$ in the ratio definition (distance 0.5443135585304);
- $(-0.3, -0.77)$ under (A), (B) (distance 0.5861919480853);
- $(-0.7055555555556, -0.6397222222222)$ under (C) (distance 0.1604394909208: the pure condensate with $w_c = -0.47$ today, gas fraction 0, CHOSEN);
- every mixture with $|w_0 + 0.861| \leq 0.1$ has $w_a$ between -1.779879740253 and -0.8286111111111 under (C) (between -3.136 and -2.159381216106 in the ratio definition, between -4.447785313931 and -3.006388888889 under (A), (B)): steeper than the Unite $-0.60$ in every definition.

### 5.5 Phantom and crossing of $-1$

No computed Kohn-Sham state crosses $w = -1$: the smallest $w_{\rm eff}(C)$ of the 14 series with $E \neq 0$ is -0.212277 ($N = 8$), and no computed state meets the phantom condition of section 4.7. The exception is not a Kohn-Sham state: a condensate has $w_{\rm eff}(C) = (5/9)(1 + w_c) - 1$, below $-1$ exactly while its ratio is, $\lambda S/m \in (-2, -1)$ (`condensate_phantom_interval`, `condensate_observer`); with $\lambda < 0$ and $mS > 0$ (positive energy, attractive self-interaction) the drift $\lambda S/m \propto e^{-(5/3)a_4}$ carries it into that window toward the past, for $\lambda S/m = -382/441$ today from $a = (382/441)^{3/5} = 0.917434069855$ back to $a = (191/441)^{3/5} = 0.605280756393$, where its energy vanishes (`Revision/dark_sector/dirac16complex00/eos-theory.json`, key ghost). The $N = 8$, $\lambda > 0$ states have $E < 0$ (from the canonical uniform-gas exchange functional; section 4.7) and $w_{\rm eff}(C)$ between -0.212277 and -0.036242; the 41 $N = 8$, $\lambda = 0$ states have $E = 0$ and no equation of state (section 5.2). On the history the expansion reads $w_{\rm exp} = -1$ exactly (section 3.3).

## 6. Results for dirac16complex00

Records:

- the reports in `Revision/dark_sector/dirac16complex00/reports/`;
- implementation A: `Revision/dark_sector/dirac16complex00/eos-theory.json`;
- the independent implementation B, the field-equation runs: `Revision/dark_sector/dirac16complex00/results/independent-numerics.json`.

### 6.1 The condensate

As for dirac16complex: $S = S_0e^{a_4}b_4^{-2}$, $w_{\rm eff}(B) = (5/9)\,w$, $w_{\rm eff}(C) = (5/9)\,w - 4/9$, the ratio $w = \lambda S/(2m + \lambda S)$ drifting (`condensate_observer`). The ratio equals -0.764 at $\lambda S/m = -382/441$ (CHOSEN), which with $\rho > 0$ needs $mS > 0$ and $\lambda < 0$, a negative potential $U$ (`condensate_ratio_equals_unite_constant_w`); there its $w_a$ is $-28077/12500 = -2.24616$, and $w_{\rm eff}(B)$ and $w_{\rm eff}(C)$ have $w_a = -1.24786666667$ (`condensate_ratio_drift_at_unite_value`); it is phantom exactly while $\lambda S/m \in (-2, -1)$, and then $w_{\rm eff}(C) < -1$ as well; the drift carries a $\lambda < 0$ condensate into that window toward the past (section 5.5). The condensate is not the source of the history: the author's equations need the anisotropic, growing source of section 2.4, while every condensate is isotropic and its $S$ decays like $e^{-(5/3)a_4}$ (`condensate_cannot_source_history`). The observer's expansion reads $w_{\rm exp} = -1$ exactly on $a_4 = Hx_4$.

### 6.2 Modes, Krein-signed energies and growing modes

For the three test cases $(m, k, q) = (3, 4, 0)$, $(5, 0, 3)$ and $(4, 4, 4)$, with $\omega = \pm5$, $\pm4$ and $\pm4$, every real-frequency eigenspace has dimension 8 and a Krein form of signature (4,4), and on it $\rho = \omega Q$ exactly (records `mode_krein_inertia_*`, `mode_emt_*`, negative control `mode_emt_negative_control`): at every real frequency there are modes of both energy signs. Implementation B confirms it: at $\omega = 1.25$ the vectors with $Q = +1$ and $Q = -1$ have $\rho = +1.25$ and $-1.25$ (`B_krein_signed_energy`). The general statement, in flat 4+4 space, is the Krein-inertia theorem of `Revision/pairing`.

For $q^2 > m^2 + k^2$ the modes grow: for $(m, k, q) = (3, 0, 5)$, $\omega = 4i$; the growing eigenspace is Krein-neutral ($Q = 0$, $\rho = 0$) with a growing extra-time pressure $p_5 = -mS$ (`growing_mode_krein_neutral`, `growing_mode_extra_time_pressure`). In the deflating field the physical extra-time momentum $q\,e^{a_4}b_4^{-1/2} \propto a^{1/3}$ grows, so every mode with $q \neq 0$ reaches a turning point $a_*$ and then grows: the deflation drives the growth. Implementation B, past the turning point $a_* = 6.2639848$ of the mode of M3: growth rate $d\ln|\phi|/dx_4 = 0.30909994$ over $a \in [7.0, 7.4]$ against the WKB rate $\sqrt{sa^{2/3} - 1} - (b_4'/b_4 - a_4'/2) = 0.3118201$ at the mean $a$ (`B_growth_rate`); the amplitude grows by a factor $10^{16.22}$ between $a = 5.5$ and $7.4$, and the energy density becomes large and negative ($\rho/Q$ = -4.76839e+29 at $a = 7.4$, for $H/m = 10^{-3}$).

### 6.3 The models M1 to M5

Each model is normalised to $\rho_{\rm tot} = 1$ at $a = 1$; definition (C) unless stated. The models keep the physical parameters of the withdrawn $b_4 = 1$ record, where they were CHOSEN to reproduce Unite numbers; on the history of the corrected metric they no longer reproduce them, and keeping them unchanged shows the effect of the corrected metric directly.

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
| M1 | $-4/9 + 5w/9$ | $\frac{50u}{27(2+u)^2}$ | drifts | drifts | drifts | for $\lambda S/m$ in $(-2, -1)$ |
| M2 | -0.3054 | +0.162074 | -0.3099 | 0.2173 | -0.2556 | no |
| M3 | -0.3981 | -0.043770 | -0.3982 | -0.0420 | -0.4087 | no |
| M4 | -0.3981 | -0.066667 | -0.3993 | -0.0502 | -0.4118 | no |
| M5 | -0.4577 | -0.1964 | -0.4438 | -0.3231 | -0.5246 | no |

M2 is freezing ($w_a > 0$), M3, M4 and M5 have the thawing sign ($w_a < 0$); none of M2 to M5 reaches the Unite pair or crosses $-1$ on $[1/3, 1]$; the column says nothing about $a > 1$, and past the turning point $a_*$ of an extra-time mode (M3: 6.2640, M4: 1.8859, M5: 2.3375) the frequency of that mode is imaginary and the bound of section 4.7 does not apply. On the withdrawn record the M4 tangent and the M5 fit equal the Unite pair by construction. Records:

| record | record | record |
| --- | --- | --- |
| `M2_tangent_exact` | `M3_tangent_exact` | `M4_former_tuning_on_the_history` |
| `positive_models_bounded_by_minus_four_ninths` | `unite_w0_requires_dominant_ghost` | `M5_former_composition_on_the_history` |
| `unite_line_fit_proxy` | `unite_crossing_point` | `condensate_ratio_drift_at_unite_value` |

Notes:

- M2 under (B) and in the ratio: tangent $(0.139, 0.162074)$, the law $w_{\rm eff}(B) = \frac13k^2/(k^2 + m^2a^2)$ from $1/3$ to 0, independent of $b_4$: a time-varying dark-matter-like equation of state. Exactly, under (C), $(w_0, w_a) = (-2749/9000, 81037/500000) = (-4/9 + r/3, (2/3)r(1 - r))$ with $r = 417/1000$.
- M3: $\omega^2 = m^2(1 - sa^{2/3})$ and $w_{\rm eff}(C) = -\frac49 + \frac19\,sa^{2/3}/(1 - sa^{2/3}) \geq -4/9$ for $a < a_*$; exactly $(w_0, w_a) = (-3583/9000, -196963/4500000)$; the turning point is at $a_* = (1417/417)^{3/2} = 6.2640$, in the future.
- M4: on the history its $w_{\rm eff}(C)$ has the minimum -0.443913275792 over $a = 1/300, \dots, 1$; it reaches its turning point at $a_* = 1.8859$ and then grows.
- M5: $s = 0.5678$, $\Omega_q = 0.5947$, condensate fraction $\Omega_c = 0.7053$; on the history its fit over $[1/2, 1]$ is (-0.443790594178, -0.32308292878), with $w_0$ above the Unite -0.861, and there is no crossing of $-1$ on $[1/3, 1]$; its turning point is at $a_* = 2.3375$.
- The positive models are bounded: the minima of $w_{\rm eff}(C)$ over $a = 1/300, \dots, 1$ are -0.305444444444, -0.443709979885 and -0.443913275792 for M2, M3, M4, all $\geq -4/9$ (`positive_models_bounded_by_minus_four_ninths`).
- Within the WKB mode model (positive components with $\varepsilon_i \geq 0$: mode gases and $\lambda = 0$ condensates, `mixture_weighted_average`) the Unite $w_0$ needs a dominant ghost: a ghost component lowers $w_{\rm eff}(C)(1)$ by at most $G/3$ and such components raise it, so $w_0 = -0.861$ needs $G \geq 3749/3000$; for condensate + ghost the total energy then vanishes at $a = G/(1 + G) = 3749/6749$ inside $[1/2, 1]$, where $w_{\rm eff}$ diverges (`unite_w0_requires_dominant_ghost`).

### 6.4 The independent implementation B

B rebuilds M2 to M5 from solutions of the 16-component field equation in the corrected metric; all tangents, fits and constant proxies agree with implementation A to within 2.2072418e-05 (records `B_vs_A_*`). B also measures $w_{\rm eff}(C)$ directly from the dilution of the proper density of its solutions, independently of the formula of section 3.1; the two agree to within 2.7779535e-05 at $a = 1/2, 3/4, 1$ (`B_dilution_equals_formula_*`). The condensate dilutes with the proper 7-volume: $e^{-a_4}b_4^2\rho$ is constant to 9.8449027e-14 while $\rho$ changes by a relative range 0.87800024 over $a \in [0.3, 1.06]$ (`B_condensate_dilutes`). The ghost component of M5 has $\rho < 0$ along the whole run, $\rho(1.06) = -0.11509411$ (`B_ghost_negative_energy`). M5 has no crossing of $-1$, on a grid of 67 points in $[0.34, 1]$ (`B_vs_A_M5_crossing`). By bisection on the field-equation solutions B finds $s = 0.29428947$ for M3 (A: $417/1417 = 0.2942837$; `B_solve_M3_s`), and the positive models M2, M3, M4 have $w_{\rm eff}(C) \geq$ -0.42931652 on $a \in [0.35, 1]$ (`B_positive_models_bounded`).

## 7. Comparison with the Unite values

| Unite value | dirac16complex | dirac16complex00 | by construction? |
| --- | --- | --- | --- |
| constant $w = -0.764$ | condensate ratio at $\lambda S/m = -382/441$ at one instant (8-dimensional ratio, drifting with $w_a = -2.246160$) | condensate ratio at $\lambda S/m = -382/441$, $\lambda < 0$, at one instant | yes: one parameter for one number |
| $w_0 = -0.861$ | not reached by the gas ($w_{\rm eff}(C) = -1/9$ free, $\geq -0.113860$ interacting) or with a $\lambda = 0$ condensate ($w_{\rm eff}(C) \geq -0.444111$); a drifting condensate with a chosen ratio comes within 0.1 of it under (C) (with the ratio -0.764 today: $w_{\rm eff}(C) = -0.868889$), with $w_a$ between -1.779879740253 and -0.8286111111111 | not reached by the positive models M2 to M4 ($w_{\rm eff}(C) \geq -4/9$; from them it needs a ghost fraction $\geq 3749/3000$); M1 ($\lambda < 0$, CHOSEN ratio) as for dirac16complex | the condensate value is chosen; no positive-energy mode gas reaches it |
| $(w_0, w_a) = (-0.861, -0.60)$ | not reached: closest scanned point at the distance 0.1604394909208 under (C), a pure condensate with a chosen ratio | not reached; on the withdrawn record M4 (tangent) and M5 (fit) reached it by construction | on the withdrawn record: two parameters for two numbers |
| phantom past, crossing of $-1$ at $a = 0.7683$ | no crossing in any Kohn-Sham state; a drifting $\lambda < 0$ condensate crosses at $a = 0.917434069855$ (for $-382/441$ today) | no crossing in M2 to M5; M1 ($\lambda < 0$) as for dirac16complex | the condensate value is chosen; the ghost fraction is a stated choice |

A model with as many tuned parameters as matched numbers reproduces them by construction and is NOT a prediction. No parameter of M2 to M5, of the mixtures or of the condensate ratio is selected by the field equations; nothing in this record selects their populations. A ghost (negative-energy) component is a ghost-like sector, not an established physical state: dirac16complex00 has one at every real frequency, and its classical energy is unbounded below (the classical form of the spin-statistics problem of a commuting field with a first-order Lagrangian).

What is not tuned: the signs and the ranges. For positive-energy mode gases with real frequencies $w_{\rm eff}(C) \geq -4/9$ on the history in the WKB model of dirac16complex00 (section 4.7; for M3 and M4 before the turning point $a_*$ of the extra-time mode; a $\lambda < 0$ condensate is not covered), and no computed dirac16complex state meets the phantom condition (section 5.5); the computed dirac16complex gas has $\lvert w_a\rvert \leq 0.003904$ and $w_{\rm eff}(C)$ between -0.113860 and -0.108312, or $-1/9$ exactly without interaction.

## 8. The lead's analysis (SPEC section 11), checked point by point

1. “The 7-volume of the metric is constant when $b_4$ is.” CORRECTED for the corrected metric: the proper 7-volume element is $e^{-a_4}b_4^2\lvert\cot z\rvert\,\lvert\sin z\rvert^{1/2}$, so the proper 7-volume of a cell changes with $x_4$ like $e^{-a_4}b_4^2$, like $e^{(5/3)a_4}$ on the history (`sqrt_det_g`, `proper_volume_elements`, `local_model_volume`): the 3-space factor $e^{3a_4}$ and the extra-time factor $e^{-3a_4}b_4^{3/2}$ are joined by the factor $e^{-a_4}b_4^{1/2}$ of the hidden direction, which shrinks with the extra times, so for constant $b_4$ the 7-volume would shrink like $e^{-a_4}$; it is constant only where $e^{-a_4}b_4^2$ is.
2. “The effective 4-dimensional density is $\rho_4 \sim \rho_8c^3$.” CORRECTED: in the corrected metric the hidden direction has the scale factor $c = e^{-a_4}b_4^{1/2}$ of the extra times, and the density per unit coordinate volume of the extra times and the hidden direction is $\rho_4 = c^4\langle\rho\rangle = e^{-4a_4}b_4^2\langle\rho\rangle$: definition (B), with (A) of the same scaling (`observer_N1_weff_identity`). It is an ASSUMPTION about the observer: definition (C), per unit proper 7-volume, is equally consistent with the field equations and shifts every $w_{\rm eff}$ by exactly $-(4 - 2\beta)/3$, $-4/9$ on the history (section 3).
3. “Non-relativistic quanta give dust, relativistic quanta radiation.” CONFIRMED under (A), (B) only for 3-space quanta in the flat (warp-free) limit without hidden or extra-time momentum, for every $b_4$: such a massive mode has $w_{\rm eff} = k^2/(3(M^2a^2 + k^2))$, $1/3 \to 0$, and a massless one, like the fold band, $1/3$ (`massive_mode_w_eff_law`, `massive_mode_cpl_tangent`, `fold_band_quantum_w_eff`). NOT CONFIRMED for the massive bulk band of the cell: its levels carry hidden momentum, which the deflation blue-shifts ($d\ln l_p/da_4 = 1 - \beta/2$; `extra_time_momentum_blueshift`), and its $w_{\rm eff}(A)$ falls through 0 to negative values (section 5.3).
4. “A Kohn-Sham gas whose 3-momenta redshift has a time-varying equation of state from $1/3$ towards 0.” NOT FOUND in the computed states: the free gas is an exact fold-band gas with $w_{\rm eff}(A) = 1/3$ exactly at every slice (`free_gas_w_eff_one_third`), the interacting gas stays in [0.330585, 0.336132] (section 5.2), and the bulk band, which the computed ground states do not populate, does not follow the law (section 5.3). For dirac16complex00 the falling law holds for a positive-energy gas of good-sector modes (WKB model, no hidden momentum; M2), the counterpart of the flat-limit 3-space quanta of item 3. The hidden-direction and extra-time pressures were computed ($P_0/E$ in [-1.192e-01, 1.114e-01] and $P_t/E$ in [-3.240e-02, 3.024e-02] for the interacting gas, zero for the free gas, $P_0/E$ in [2.117340, 3.823722] for $N = 8$); the 3-space observer does not see them as pressure.
5. “A homogeneous condensate has constant $w$ while $\rho_4 \sim a^{-3}$; the ratio and $w_{\rm eff} = 0$ disagree; 4-dimensional energy is exchanged with the extra dimensions.” CORRECTED for the corrected metric: $S\,\mathrm{Vol}_7$ is constant ($S = S_0e^{a_4}b_4^{-2}$), so for $\lambda \neq 0$ the condensate's ratio drifts and $w_{\rm eff}(B) = ((2\beta - 1)/3)\,w = (5/9)\,w \neq 0$ (`condensate_w_eff`, `condensate_observer`); for $\lambda = 0$, $w_{\rm eff}(B) = 0$ ($\rho_4 \propto a^{-3}$) and $w_{\rm eff}(C) = -4/9$. The exchange reading is an INTERPRETATION of the disagreement between the ratio and the dilution.
6. “Whether any state gives a time-varying dark-energy equation of state near the Unite values must be computed.” COMPUTED: for dirac16complex no computed Kohn-Sham state comes near the Unite pair in any definition; only a drifting condensate with a CHOSEN ratio does, at the distance 0.1604394909208 under (C) (section 5.4); for dirac16complex00 none of the positive-energy models M2 to M4 goes below $-4/9$ over $a = 1/300, \dots, 1$ (`positive_models_bounded_by_minus_four_ninths`; sections 6.3 and 7); the condensate M1 does for $\lambda < 0$ and $mS > 0$, at a CHOSEN $\lambda S/m$ (sections 6.1 and 5.5).
7. “Crossing $w = -1$ needs negative kinetic energy, which the indefinite (Krein) energy of the extra-time sector and the commuting field dirac16complex00 may supply.” EXAMINED. Positive-energy extra-time momentum does NOT supply it: its pressure $p_t \leq 0$ enters with the factor $\beta/2 - 1 < 0$, so it moves $w_{\rm eff}$ up, not down (`phantom_condition`, `wkb_epsilon_sign_free`; M3 has $w_{\rm eff}(C) \geq -4/9$ before its turning point $a_* = 6.2640$). A positive hidden kinetic pressure lowers $w_{\rm eff}$, but below $-1$ under (C) only if $P_0 > 9E(P_3/E + 5/9)$, which no computed state has. What a mode gas needs is negative classical ENERGY: dirac16complex00 has it at every real frequency (Krein signature (4,4)), and on the history it would have to exceed the positive energy ($G \geq 3749/3000$, section 6.3), as a ghost-like sector. The exception is a condensate with $\lambda < 0$ and $mS > 0$ (positive energy, attractive self-interaction, not a mode gas), whose drifting ratio, at a CHOSEN value today, crosses $-1$ toward the past (section 5.5). For dirac16complex the only states with $E < 0$ ($N = 8$, $\lambda > 0$, negative with the canonical uniform-gas exchange functional; with the exact Fock exchange solved self-consistently $\lvert E\rvert \leq 4.98 \times 10^{-12}$, section 4.7) have $w_{\rm eff}(C) \geq -0.212277$. Modes of dirac16complex with extra-time momentum lie outside the good sector and are OPEN.

## 9. Verdicts

### 9.1 dirac16complex (Hypothesis)

- Dark matter. Not found. Under (A), (B) the computed free gas is an exact fold-band gas with $w_{\rm eff} = 1/3$ exactly at every slice (radiation-like, with no time variation), the interacting gas lies in [0.330585, 0.336132], and the massive bulk band, which the computed ground states do not populate, falls from 0.318721 at $a_4 = -3$ through 0 to -0.081074 at $a_4 = 4$ for one shell, toward $-1/9$, instead of approaching 0. The dust-like law $1/3 \to 0$ is exact only for a flat-limit 3-space quantum without hidden or extra-time momentum (independent of $b_4$). A $\lambda = 0$ condensate is dust-like under (B) ($w_{\rm eff}(B) = 0$).
- Dark energy. Not found in the computed states: under (C) the free gas has $w_{\rm eff}(C) = -1/9$ and the interacting gas lies in [-0.113860, -0.108312], with tangent $w_a$ in [-0.003892, 0.003904] and fitted $w_a$ in [-0.002392, 0.002261]; only a drifting condensate with a CHOSEN $\lambda S/m$ gives values near the Unite $w_0$ ($w_{\rm eff}(C) = -0.868889$ at the ratio -0.764 today, with $w_a = -1.247867$), and the closest scanned point to the Unite pair lies at the distance 0.1604394909208; the Unite constant $w = -0.764$ is matched only by the 8-dimensional ratio of a tuned condensate at one instant. No computed Kohn-Sham state crosses $w = -1$.
- On the history the observer's expansion reads $w_{\rm exp} = -1$ exactly.

### 9.2 dirac16complex00 (Hypothesis00)

- Dark matter. Under (B) and in the ratio $p_3/\rho$: a positive-energy gas of good-sector modes (WKB model, no hidden momentum) has the time-varying law from $1/3$ to 0 (M2), independent of $b_4$; a $\lambda = 0$ condensate is dust-like.
- Dark energy without ghosts. Not from positive-energy mode gases on the history with $b_4(x_4)$ (WKB model, real frequencies, no hidden momentum): they have $w_{\rm eff}(C) \geq -4/9$ (section 4.7; M2: -0.3054, M3 and M4: -0.3981 today); for M3 and M4 this holds before the turning point $a_*$ of the extra-time mode (M3: 6.2640, M4: 1.8859). Only the condensate with a CHOSEN $\lambda S/m < 0$ and $mS > 0$ gives values near the Unite $w_0$ ($w_{\rm eff}(C) = -0.868889$ at the ratio -0.764 today, $w_a = -1.24786666667$; section 6.1): a tuned value, not a prediction. The thawing slope of the extra-time mode is small (M3: -0.043770) because its physical momentum grows only like $a^{1/3}$; past $a_*$ the mode grows without bound and its energy density becomes large and negative (implementation B).
- Phantom and crossing of $-1$. Impossible with positive-energy mode components of real frequency in the WKB model (section 4.7); the Unite $w_0$ alone needs, from such components, a component of negative classical energy larger than the positive energy ($G \geq 3749/3000$), a ghost-like sector. The exception is a condensate with $\lambda < 0$ and $mS > 0$: while its drifting ratio lies in the window $\lambda S/m \in (-2, -1)$ the observer reads $w_{\rm eff}(C) = (5/9)(1 + w_c) - 1 < -1$ (section 5.5); its value is CHOSEN and no source of the history selects it.
- The source of the history: the author's equations need the anisotropic source of section 2.4, which grows with $x_4$ and whose energy density changes sign along the history; no condensate is it.

### 9.3 The hypotheses

This record establishes neither Hypothesis nor Hypothesis00. What it shows, under its stated assumptions, on the corrected metric with $b_4(x_4)$: in the WKB model without hidden momentum (an APPROXIMATION; section 10, item 4) a positive-energy good-sector gas of dirac16complex00 has the dark-matter-type law under definition (B) (M2); the same flat-limit law holds for the 3-space quanta of dirac16complex (`massive_mode_w_eff_law`), but neither the computed dirac16complex states nor its bulk band show it; no positive-energy mode gas of dirac16complex00 in the WKB model (no hidden momentum) goes below $-4/9$ under any definition, and no computed dirac16complex state does; a gas of dirac16complex bulk-band quanta, which no computed state populates, would go below $-4/9$ under (C), since its $w_{\rm eff}(A)$ is negative at every sampled $a_4 \geq -0.25$ (section 5.3); values near the Unite $w_0$ arise only from a condensate with a CHOSEN $\lambda S/m < 0$, with a slope steeper than the Unite slope; the Unite numbers are not reproduced, and on the withdrawn $b_4 = 1$ record they were reproduced only by models whose parameters were chosen to reproduce them. Nothing in this record establishes that either field is dark energy or dark matter.

## 10. What remains open

1. A self-consistent history with an admissible source. No recorded Kohn-Sham state is an admissible source of the corrected metric: its energy-momentum tensor depends on $x_0$ for every nonzero state, and the interacting states violate $p_0 = p_t$; the history is a prescribed background (the 5 checks of `Revision/field_equations_a4/reports/ks-source-conditions.json`: `ks_profiles_depend_on_x0`, which holds for every $a_4$ and $b_4$, `ks_hidden_pressure_condition`, `ks_offdiagonal_condition`, `ks_history_is_a_prescribed_background` and `ks_zero_source_states_listed`). The source that the author's equations require on the history (section 2.4) is not constructed from the fields of this record; a condensate is not it.
2. Populated bulk-band or thermal states along the history (fixed entropy); only $T = 0$ ground states and, for the Kohn-Sham states, $a_4 \in [0, 2]$ (the solver's validated range) are computed; the single-level bulk-band study of `independent_free_gas.py` (independent collocation, not the solver) runs over $a_4 \in [-3, 4]$; $b_4(0)$ enters only through $\hat\lambda$.
3. Modes of dirac16complex with extra-time momentum (outside the good sector; only their flat-limit sign structure is derived) and the non-adiabatic (time-dependent) Kohn-Sham problem.
4. For dirac16complex00: configurations that depend on $x_0$ are not consistent sources of the metric; the WKB model holds the warp fixed and carries no hidden momentum (the blue-shift of the bulk band of section 5.3 is not in its gases); the growing modes make the Cauchy problem ill-posed, and nothing here cures that; no quantum treatment (a classical field).
5. Which normalisation of $\rho_4$, if any, describes a physical 3-space observer; the value of $a_{4,\rm today}$.
6. What would select the populations of M2 to M5, the mixture fractions or the condensate's $\lambda S/m$.
7. A supernova likelihood (distances, covariances): no fit to data is part of this record.
8. Other histories: the shift between (A, B) and (C) is $-(4 - 2\beta)/3$ and the weight of the hidden and extra-time pressures is $\beta/2 - 1$, so the verdicts depend on $\beta$; no source of this record selects a history. The filling of both fold conditions is ASSUMED and the tip condition is chosen.

## 11. Verification records

### 11.1 Reports and their counts

Every check has a name, a verdict and a detail. Counts at the time of writing (the publication test re-reads them):

| report | checks | PASS | FAIL |
| --- | --- | --- | --- |
| `Revision/dark_sector/dirac16complex/reports/derivation-checks.json` | 37 | 37 | 0 |
| `Revision/dark_sector/dirac16complex/reports/ks-history-run.json` | 8 | 8 | 0 |
| `Revision/dark_sector/dirac16complex/reports/eos-checks.json` | 13 | 13 | 0 |
| `Revision/dark_sector/dirac16complex/reports/independent-checks.json` | 10 | 10 | 0 |
| `Revision/dark_sector/dirac16complex00/reports/python-derive-eos.json` | 48 | 48 | 0 |
| `Revision/dark_sector/dirac16complex00/reports/python-independent-numerics.json` | 32 | 32 | 0 |
| `Revision/dark_sector/reports/wolfram-dark-sector.json` | 7 | 7 | 0 |
| `Revision/field_equations_a4/reports/ks-source-conditions.json` | 5 | 5 | 0 |

### 11.2 Checks per report

The tables list every check of the seven dark-sector reports of the corrected metric; every one has the verdict PASS.

**dirac16complex, derive_effective.py** (37 checks):

| check | check | check |
| --- | --- | --- |
| `x0_derivative_rules_every_real_z` | `sqrt_det_g` | `proper_volume_elements` |
| `hidden_coordinate_dy_dx0` | `conservation_x4_identity` | `conservation_x0_identity` |
| `conservation_other_components_vanish` | `conservation_x0_in_y_form` | `conservation_equals_a4_record` |
| `integrated_identity_dE_dx4` | `integrated_identity_equals_ks_theory` | `w_eff_A` |
| `w_eff_B_equals_w_eff_A` | `w_eff_C` | `w_eff_general_normaliser` |
| `condensate_rho_p` | `condensate_scaling` | `condensate_ratio_w` |
| `condensate_ratio_time_dependence` | `condensate_w_eff` | `condensate_ratio_equal_unite_constant_w` |
| `flat_mode_mass_shell` | `flat_mode_gas_conservation` | `massive_mode_w_eff_law` |
| `massive_mode_cpl_tangent` | `fold_band_quantum_w_eff` | `extra_time_momentum_blueshift` |
| `mixture_fold_band_gas_condensate_cpl` | `mixture_C_matching_w0_unite` | `cpl_least_squares_rule` |
| `unite_deep_past` | `expansion_inferred_w` | `einstein_no_mixed_component` |
| `einstein_space_minus_extra_time` | `expansion_inferred_w_einstein` | `record_history_needs_a_source` |
| `phantom_condition` |  |  |

**dirac16complex, run_ks_history.py** (8 checks):

| check | check | check |
| --- | --- | --- |
| `all_runs_succeeded` | `committed_slices_equal_committed_record` | `lambda0_series_exact_fold_band` |
| `cell_volume_follows_b4` | `lambda_eff_form_agrees` | `occupied_labels_fixed_along_history` |
| `y_conservation_every_state` | `particle_number_every_state` |  |

**dirac16complex, compute_eos.py** (13 checks):

| check | check | check |
| --- | --- | --- |
| `formulas_input_present` | `dense_history_complete` | `conservation_identity` |
| `conservation_integrated_simpson` | `derivative_two_ways` | `free_gas_exact_fold_band` |
| `interacting_gas_ranges` | `n8_interacting_states` | `condensate_ratio_value` |
| `condensate_drifts` | `mixture_C_cannot_reach_unite_w0_with_lambda0_condensate` | `mixture_scan_three_definitions` |
| `gas_cpl_far_from_unite` |  |  |

**dirac16complex, independent_free_gas.py** (10 checks):

| check | check | check |
| --- | --- | --- |
| `exact_k0_spectra` | `fold_band_dispersion` | `collocation_converged` |
| `aufbau_closed_shells` | `energy_vs_rust_solver` | `w_eff_vs_primary` |
| `free_gas_w_eff_one_third` | `cpl_tangent_vs_primary` | `bulk_band_w_eff` |
| `fold_band_radiation_law` |  |  |

**dirac16complex00, derive_eos.py (A)** (48 checks):

| check | check | check |
| --- | --- | --- |
| `gammas_clifford_author_T16` | `conservation_negative_control` | `conservation_x4_corrected_metric` |
| `conservation_x0_corrected_metric` | `conservation_other_components_vanish` | `conservation_x4_local_model` |
| `local_model_volume` | `observer_N1_weff_identity` | `observer_N2_weff_identity` |
| `observer_hidden_average_commutes` | `condensate_S_T16` | `condensate_negative_control` |
| `condensate_K4_equals_MS_T16` | `condensate_rho_p_w` | `condensate_observer` |
| `condensate_phantom_interval` | `condensate_ratio_equals_unite_constant_w` | `condensate_ratio_drift_at_unite_value` |
| `history_required_source` | `condensate_cannot_source_history` | `mode_dispersion_h_squared` |
| `mode_generator_B_selfadjoint` | `mode_emt_negative_control` | `mode_krein_inertia_m3_k4_q0_pos` |
| `mode_emt_m3_k4_q0_pos` | `mode_krein_inertia_m3_k4_q0_neg` | `mode_emt_m3_k4_q0_neg` |
| `mode_krein_inertia_m5_k0_q3_pos` | `mode_emt_m5_k0_q3_pos` | `mode_krein_inertia_m5_k0_q3_neg` |
| `mode_emt_m5_k0_q3_neg` | `mode_krein_inertia_m4_k4_q4_pos` | `mode_emt_m4_k4_q4_pos` |
| `mode_krein_inertia_m4_k4_q4_neg` | `mode_emt_m4_k4_q4_neg` | `growing_mode_krein_neutral` |
| `growing_mode_extra_time_pressure` | `wkb_mode_gas_conservation` | `wkb_epsilon_sign_free` |
| `mixture_weighted_average` | `unite_line_fit_proxy` | `unite_crossing_point` |
| `M2_tangent_exact` | `M3_tangent_exact` | `M4_former_tuning_on_the_history` |
| `positive_models_bounded_by_minus_four_ninths` | `unite_w0_requires_dominant_ghost` | `M5_former_composition_on_the_history` |

**dirac16complex00, independent_numerics.py (B)** (32 checks):

| check | check | check |
| --- | --- | --- |
| `B_clifford_numeric` | `B_krein_matrix` | `B_krein_signed_energy` |
| `B_superposition_average` | `B_run_kmode_invariants` | `B_run_q3_invariants` |
| `B_run_q4_invariants` | `B_run_q5_invariants` | `B_run_cond_invariants` |
| `B_run_ghost_invariants` | `B_ghost_negative_energy` | `B_condensate_dilutes` |
| `B_vs_A_M2_N2` | `B_vs_A_M2_N1` | `B_vs_A_M2_ratio` |
| `B_dilution_equals_formula_M2` | `B_vs_A_M3_N2` | `B_vs_A_M3_N1` |
| `B_vs_A_M3_ratio` | `B_dilution_equals_formula_M3` | `B_vs_A_M4_N2` |
| `B_vs_A_M4_N1` | `B_vs_A_M4_ratio` | `B_dilution_equals_formula_M4` |
| `B_vs_A_M5_N2` | `B_vs_A_M5_N1` | `B_vs_A_M5_ratio` |
| `B_dilution_equals_formula_M5` | `B_vs_A_M5_crossing` | `B_solve_M3_s` |
| `B_positive_models_bounded` | `B_growth_rate` |  |

**dark sector, verify_dark_sector.wls (Wolfram)** (7 checks):

| check | check | check |
| --- | --- | --- |
| `D1_volume` | `D2_conservation` | `D3_w_eff_general` |
| `D4_condensate_T16` | `D5_kinetic_gas` | `D6_history_source_anisotropic` |
| `D7_condensate_drift` |  |  |

### 11.3 Re-verification for this document

The reports cited in this document are the committed files of phases W5 and W6 (2026-10-17), in which the seven dark-sector scripts of section 12 were moved to the corrected metric and run on the committed inputs (`Revision/kohn_sham/results` of phase W5, `Revision/algebra/gammas.json`, `Revision/field_equations_a4/a4-equations.json`) with the built Revision Rust solver: 37 of 37, 8 of 8, 13 of 13, 10 of 10, 48 of 48, 32 of 32 and 7 of 7 checks passed. The dense Kohn-Sham history (`run_ks_history.py`), the Kohn-Sham source-conditions report (5 of 5) and the exact-Fock variant were committed with the Kohn-Sham record of phase W5, the other reports in phase W6. No script was re-run for this document; its publication test re-reads every count and every quoted number from the committed files.

## 12. Reproduction

From the repository root, in this order. Each script exits 0 only if all its checks pass; its outputs are LF and two runs are byte-identical (the folder READMEs). The dirac16complex scripts write into their own `outputs/` and `reports/` folders, and each reads the outputs of the scripts before it; `run_ks_history.py` needs the built Rust solver (`--solver PATH` selects another binary, `--jobs N` the number of parallel runs) and runs in three parts into a work folder and an assembly (one invocation without `--part` computes everything at once). The dirac16complex00 scripts accept `--out DIR`, and `independent_numerics.py` reads implementation A's `eos-theory.json` for its comparison; the Wolfram verifier reads `eos-theory.json` for its comparison of the required source. Each `run_ks_history.py` command, the second unittest command and the PDF command are each one command; the backslash is the line continuation of a POSIX shell. Python needs numpy and sympy (no scipy).

```text
cargo build --release --manifest-path Revision/kohn_sham/solver/Cargo.toml
python Revision/dark_sector/dirac16complex/derive/derive_effective.py
python Revision/dark_sector/dirac16complex/compute/run_ks_history.py \
    --work build/revision/ks-history-work --part 1/3
python Revision/dark_sector/dirac16complex/compute/run_ks_history.py \
    --work build/revision/ks-history-work --part 2/3
python Revision/dark_sector/dirac16complex/compute/run_ks_history.py \
    --work build/revision/ks-history-work --part 3/3
python Revision/dark_sector/dirac16complex/compute/run_ks_history.py \
    --work build/revision/ks-history-work
python Revision/dark_sector/dirac16complex/compute/compute_eos.py
python Revision/dark_sector/dirac16complex/independent/independent_free_gas.py
python Revision/dark_sector/dirac16complex00/python/derive_eos.py
python Revision/dark_sector/dirac16complex00/python/independent_numerics.py
wolframscript -file Revision/dark_sector/wolfram/verify_dark_sector.wls
python -m unittest \
    Revision/dark_sector/dirac16complex00/tests/test_dark_sector_dirac16complex00.py -v
python scripts/build_provenance_pdf.py Revision/docs/DARK_SECTOR_HYPOTHESES.md \
    --developer-layout --specifications Revision/pdf-specifications.json
python -m unittest Revision/tests/test_dark_sector_hypotheses_publication.py -v
```

Expected output and run times, as the folder READMEs state them (2026-10-17) and, where they state none, the time budget of the step in the Revision gate (`Revision/verify_revision.sh`):

| command | last line of the output | time |
| --- | --- | --- |
| `derive_effective.py` | 37/37 checks pass | about 4 s |
| `run_ks_history.py` | PASS - particle_number_every_state (the eighth of 8 PASS lines of the assembly) | about 22 s per part and 0.7 s for the assembly (22 workers) |
| `compute_eos.py` | 13/13 checks pass | about 1 s |
| `independent_free_gas.py` | 10/10 checks pass | about 85 s |
| `derive_eos.py` | derive_eos: 48/48 checks pass | about 4 s |
| `independent_numerics.py` | independent_numerics: 32/32 checks pass | about 8 s |
| `verify_dark_sector.wls` | 7/7 checks passed | gate budget 10 s |
| `test_dark_sector_dirac16complex00.py` | OK (4 tests) | gate budget 30 s |
| `build_provenance_pdf.py` | provenance_pdf=OK | gate budget 30 s |
| `test_dark_sector_hypotheses_publication.py` | OK (skipped=1); with REVISION_PDF_REBUILD=1: OK | below 1 s without the rebuild |

The PDF build runs the Markdown-to-LaTeX builder twice (with different hash seeds), runs pdflatex three times into each of two fresh directories, requires warning-free logs and byte-identical PDFs, and checks the PDF against its entry `dark-sector-hypotheses` in `Revision/pdf-specifications.json` (the Revision registry; the registry of the earlier stages is not touched).

## 13. What is proved, computed, assumed and not established

### 13.1 Proved (exact, by symbolic computation in the named checks)

1. For the corrected metric with $b_4(x_4)$ and every real $z$ with $\sin z \neq 0$ (`x0_derivative_rules_every_real_z`): the proper 7-volume element $e^{-a_4}b_4^2\lvert\cot z\rvert\,\lvert\sin z\rvert^{1/2}$; the conservation identities $d\rho/dx_4 = -3a_4'(\rho + p_3) - h_4(\rho + p_0) - 3h_4(\rho + p_t)$ and $dp_0/dx_0 + 3H\cot z\,(p_0 - p_t) = 0$ for diagonal sources $T(x_0, x_4)$ (sympy and Wolfram); in Einstein gravity no mixed component and $G^{x_0}{}_{x_0} = G^{x_5}{}_{x_5}$.
2. The observer identity $w_{\rm eff} = P_3/E + (\beta/2 - 1)(P_0 + 3P_t)/(3E) - s\,(4 - 2\beta)/3$ for the normalisations (A), (B) ($s = 0$) and (C) ($s = 1$), and its N1/N2 form for dirac16complex00.
3. The condensate: an exact homogeneous solution of dirac16complex00 (for dirac16complex the mean-field form, with $\langle U(S)\rangle = U(\langle S\rangle)$ ASSUMED) with $S\,\mathrm{Vol}_7$ constant, $S = S_0e^{a_4}b_4^{-2}$, its drifting ratio, $w_{\rm eff}(B) = ((2\beta - 1)/3)\,w$ and $w_{\rm eff}(C) = w_{\rm eff}(B) - (4 - 2\beta)/3$; the ratio $-0.764$ at $\lambda S/m = -382/441$ at an instant; the phantom window $(-2, -1)$, in which the observer also reads $w_{\rm eff}(C) < -1$ on the history.
4. The history: with the author's weights it needs the anisotropic source of section 2.4, which grows with $x_4$ (sympy; the Wolfram verification confirms its anisotropy and the agreement of the two records); no condensate is it.
5. The flat-limit mode laws (massive $1/3 \to 0$ without hidden or extra-time momentum, independent of $b_4$; massless and fold-band quanta $1/3$; the blue-shift $1 - \beta/2$ of the hidden and extra-time momenta) and the expansion-inferred $w_{\rm exp}$, $-1$ exactly on $a_4 = Hx_4$ for every $b_4$.
6. dirac16complex00: on the three test eigenspaces, dimension 8, Krein signature (4,4) and $\rho = \omega Q$; the growing eigenspace is Krein-neutral; within the WKB model, positive-energy components of real frequency give $w_{\rm eff}(B) \geq 0$ and $w_{\rm eff}(C) \geq -(4 - 2\beta)/3$; the exact tangents of M2 and M3 on the history; the ghost fraction $3749/3000$ that such positive components need for the Unite $w_0$ (a $\lambda < 0$ condensate is not such a component).

### 13.2 Computed (numerical, with the stated tolerances and two implementations)

The Kohn-Sham gas along the history with $b_4(x_4)$ (615 states at $\hat\lambda$ in the cell growing like $e^{(5/3)a_4}$, i.e. at $\lambda_{\rm eff} = \hat\lambda e^{-(5/3)a_4}$ in the fixed cell; the free gas an exact fold-band gas with $w_{\rm eff}(A) = 1/3$; the interacting gas with $w_{\rm eff}(A)$ in [0.330585, 0.336132] and $w_{\rm eff}(C)$ in [-0.113860, -0.108312]), with the conservation identity including the terms of the hidden direction and the extra times; its CPL tangents and fits, the mixtures and the scans; the bulk band (independent implementation); the models M2 to M5 on the history; implementation B of dirac16complex00 (field-equation runs in the corrected metric, agreement with A to within 2.2072418e-05, $w_{\rm eff}$ from the dilution of the proper density, the growth past the turning point).

### 13.3 Assumed

1. The normalisation (A), (B) or (C) of $\rho_4$: an ASSUMPTION about the observer; every verdict is stated for each.
2. The history $a_4 = Hx_4$, $b_4 = b_4(0)e^{(4/3)Hx_4}$ as a PRESCRIBED BACKGROUND (test fields, no back-reaction); the instantaneous (adiabatic) Kohn-Sham states; $a_{4,\rm today}$; $b_4(0)$ through $\hat\lambda$.
3. The filling of both fold conditions at the fold $y = 0$ (ASSUMED), the tip condition $\theta = 0$ at $y = -L$ (chosen) and the filling convention of `Revision/kohn_sham/ks-theory.json`. The canonical uniform-gas exchange functional of the Kohn-Sham states is an APPROXIMATION; with the exact Fock exchange solved self-consistently the $N = 8$, $\lambda > 0$ states have $\lvert E\rvert \leq 4.98 \times 10^{-12}$ (section 4.7).
4. The WKB/local model of dirac16complex00 (warp held fixed, no hidden momentum, adiabatic Krein charges, incoherent superposition): an APPROXIMATION, measured by implementation B.
5. The populations, fractions and condensate parameters of every model: CHOSEN (those of M2 to M5 on the withdrawn record to reproduce the Unite numbers there; the condensate ratio closest to the Unite pair in the scan of section 5.4).
6. The condensate of dirac16complex in its mean-field form, $\langle U(S)\rangle = U(\langle S\rangle)$ (section 4.4): ASSUMED.

### 13.4 Not established

1. A dark-energy or dark-matter mechanism of either field: this record establishes neither Hypothesis nor Hypothesis00, and nothing in this record establishes that either field is dark energy or dark matter.
2. Any Unite value as an output of the field equations: no positive-energy mode gas reaches them on the history, a condensate matches a single Unite number only with a CHOSEN $\lambda S/m$ and never the pair, and every match of the withdrawn record was by construction (sections 5.4, 6.3 and 7).
3. That the ghost-like sector of dirac16complex00 is a physical state; that a time-varying dark-matter equation of state arises in the computed dirac16complex states or in its bulk band; that any computed state crosses $w = -1$; that any good-sector state of dirac16complex has $E < 0$ beyond the canonical uniform-gas exchange functional (section 4.7).
4. A fit to supernova data; a self-consistent cosmological history; a source of the fields of this record for the history with $b_4(x_4)$; the open problems of section 10.
