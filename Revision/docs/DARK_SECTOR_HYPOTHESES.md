# Dark-sector hypotheses for dirac16complex and dirac16complex00: the equation of state seen from 3-space

## Hypothesis and Hypothesis00 investigated in the author's primordial gravitational field with exponentially deflating extra times: the observer assumption, the method, the results for each field, the comparison with the Supernovae Unite values, the verdicts and what remains open

## Abstract

The author asked on 2026-10-01 that two hypotheses be investigated: that dirac16complex (Hypothesis) and dirac16complex00 (Hypothesis00) provide a possible physical mechanism for a time-varying dark-energy equation of state and/or a time-varying dark-matter equation of state. This document reports what the Revision computation found; every number is read from a named Revision report. The equation of state that a 3-space observer infers is not fixed by the field equations alone: the extra times $x_5, x_6, x_7$ are time-like and deflate exponentially, and the 4-dimensional density $\rho_4$ needs an ASSUMPTION about how the observer normalises over them. For the three stated definitions (A), (B) and (C) the dilution-inferred equation of state obeys exactly $w_{\rm eff}(A) = w_{\rm eff}(B) = X/E$ and $w_{\rm eff}(C) = X/E - 1$ with $X = P_3 - P_t$, so every verdict moves by exactly $-1$ between (A, B) and (C). dirac16complex: the computed Kohn-Sham gas (615 instantaneous states along the prescribed history) is radiation-like, with $X/E$ rising toward $1/3$ (0.2929 to 0.3183 for $N = 688$, $\lambda = 0$); the dark-matter-like fall from $1/3$ toward 0 occurs for quanta of the massive bulk band (0.239626 to 2.268e-03 for one shell), which the computed ground states do not populate; under (C) the gas has $w_{\rm eff}$ between -0.707107 and -0.671895 with a thawing-sign slope of magnitude at most 0.030371, and mixtures with a condensate are freezing; nothing computed comes near the Unite pair $(w_0, w_a) = (-0.861, -0.60)$ and no computed state crosses $w = -1$. dirac16complex00: a positive-energy gas of good-sector modes has the dark-matter-like law $1/3 \to 0$ under (B); under (C) one- and two-parameter models are thawing or freezing with $w \geq -1$ as long as every mode has a real frequency (for the thawing models M3 and M4 only before the turning point of their extra-time mode); the model M4 reproduces the Unite CPL tangent exactly because its two free parameters were CHOSEN to solve the two tangent conditions; a crossing of $w = -1$ requires a component of negative classical energy, a ghost-like sector (model M5). The Unite constant $w = -0.764$ is matched only by a constant condensate ratio with a tuned $\lambda S/m = -382/441$ or by a tuned mixture. A model with as many tuned parameters as matched numbers reproduces them by construction and is NOT a prediction. This record establishes neither Hypothesis nor Hypothesis00; it states what each field can and cannot produce under its stated assumptions.

## 1. The hypotheses and the short answer

The author's hypotheses, quoted from `Revision/README.md`:

- “Hypothesis: dirac16complex provides a possible physical mechanism for a time-varying dark energy equation of state and/or a possible physical mechanism for a time-varying dark matter equation of state, both of which you will investigate.”
- “Hypothesis00: dirac16complex00 provides [the same], both of which you will investigate.”

`Revision/SPEC.md` section 8 makes both hypotheses questions to be INVESTIGATED, not assumed: for each field, the equation of state seen by a 3-space observer as the extra times deflate and 3-space inflates (the condensate, the Kohn-Sham gas, mixtures), its time dependence, the CPL parameters, and the comparison with the Supernovae Unite values. Section 11 of the same file records the lead's analysis, to be checked; section 8 of this document checks it point by point.

The short answer (details and records in sections 3 to 9):

1. The observer's $\rho_4$ is an ASSUMPTION (section 3). Under the definitions (A) and (B) a state is dust-like or radiation-like; under (C) the same state is cosmological-constant-like or quintessence-like. Every verdict below is stated for each definition.
2. dirac16complex, dark matter: a time-varying dark-matter-like equation of state ($w_{\rm eff}$ falling from $1/3$ toward 0 under (A, B)) is present in the theory for quanta of the massive bulk band, not in the computed Kohn-Sham ground states, whose gas is radiation-like.
3. dirac16complex, dark energy: only under (C), with $w_{\rm eff}$ between -0.707107 and -0.671895 and a thawing-sign slope far below the Unite 0.60; nothing computed comes near the Unite pair or crosses $w = -1$.
4. dirac16complex00, dark matter: a positive-energy gas of good-sector modes has the time-varying law $1/3 \to 0$ under (B) and in the ratio $p_3/\rho$.
5. dirac16complex00, dark energy: only under (C); thawing or freezing with $w \geq -1$ for positive-energy content with real frequencies (for the thawing models M3 and M4 only before the turning point $a_*$ of their extra-time mode, section 6.3); the Unite CPL tangent and the Unite fit are reproduced only by models whose parameters were CHOSEN to reproduce them, and the crossing of $-1$ only with a ghost-like component.
6. On the prescribed history $a_4 = AHx_4$ (the only history a condensate allows) the observer's expansion itself reads $w_{\rm exp} = -1$ exactly.

## 2. Setting and conventions

### 2.1 The author's metric and coordinates

The coordinates are named as the author names them: $x_1, x_2, x_3$ are ordinary 3-space (inflating), $x_4$ is the time, $x_5, x_6, x_7$ are the three extra times, which are time-like and DEFLATE exponentially as $a_4$ increases, and $x_8$ is the hidden space direction, with $z = 6Hx_8 \in (0,\pi/2)$ and $H > 0$ the author's constant. The metric of `Revision/SPEC.md` section 1 is

$$
\begin{aligned}
ds^2 = {} & e^{2a_4(x_4)}\sin^{1/3}z\,\big(dx_1^2+dx_2^2+dx_3^2\big) - dx_4^2 \\
& - e^{-2a_4(x_4)}\sin^{1/3}z\,\big(dx_5^2+dx_6^2+dx_7^2\big) + \cot^2 z\,dx_8^2 ,
\end{aligned}
$$

of signature (4,4), with $\sqrt{|g|} = \cos z$. The 3-space scale factor is $e^{a_4}\sin^{1/6}z$ and the extra-time scale factor $e^{-a_4}\sin^{1/6}z$. The observer's scale factor is $a = e^{a_4 - a_{4,\rm today}}$, normalised to $a = 1$ at a chosen “today” $a_{4,\rm today}$ (a free parameter). The Kohn-Sham records use the hidden coordinate $y = \ln(\sin z)/(6H)$.

### 2.2 The two fields and the energy-momentum tensor

dirac16complex is $\Psi$: 16 complex anticommuting components, a Pin(4,4) spinor, quantised canonically; its energy-momentum tensor is an operator, and the numbers below are expectation values in the instantaneous Kohn-Sham states of the good sector (no extra-time momentum), in the positive realisation of the good sector (with the ASSUMED brane condition and the chosen tip condition of the Kohn-Sham record, which make its blocks self-adjoint; the field-theory record constructs the positive realisation explicitly only for single good-sector momenta with frozen coefficients). dirac16complex00 is $\Phi$: 16 complex commuting components that transform as a Pin(4,4) spinor, a classical field; its energy-momentum tensor is the classical bilinear, whose energy has both signs (Krein-signed energies, section 6.2). Both fields have the Lagrangian of `Revision/SPEC.md` section 3 with $U(S) = \frac{\lambda}{2}S^2$, $S = \bar\Psi\Psi$. The energy density is $\rho = -T^{x_4}{}_{x_4}$ and the pressures are $p_\mu = T^\mu{}_\mu$ (no sum): $p_3$ of 3-space, $p_t$ of the extra times and $p_8$ of the hidden direction. For homogeneous on-shell states $\rho = mS + U$ and $p = SU' - U$. For a state of the Kohn-Sham record, $E$, $P_3$, $P_t$ and $P_8$ are the proper 7-volume integrals of $\rho$, $p_3$, $p_t$ and $p_8$, and $X = P_3 - P_t$.

### 2.3 The Unite values and the CPL convention

The author's private PDF (not part of the repository; only these numbers are used) gives the Supernovae Unite constant-$w$ fit $w = -0.764$ and the CPL fit $w(a) = w_0 + w_a(1-a)$ with $(w_0, w_a) = (-0.861, -0.60)$. In the deep past the CPL line tends to $w_0 + w_a = -1.461$ (quoted as -1.46), which is phantom; the line crosses $w = -1$ at $a = 461/600 = 0.7683$ ($z = 139/461$; record `unite_crossing_point`). In this convention thawing means $w_a < 0$ ($w$ rises from near $-1$) and freezing $w_a > 0$; the formula decides (the PDF's table states the opposite signs).

The CPL tangent of a model is $w_0 = w(1)$, $w_a = -dw/da$ at $a = 1$. The fits are least squares of $w(a)$ over $a \in [1/2, 1]$ or $[1/3, 1]$ (record `cpl_least_squares_rule`). The “constant $w$” of a model is the mean of $w(a)$ over the range, a PROXY: applied to the Unite CPL line itself it gives -1.011 on $[1/2, 1]$ and -1.061 on $[1/3, 1]$ (record `unite_line_fit_proxy`), so it is not the supernova constant-$w$ fit -0.764, which weights the data. No supernova likelihood, distance fit or covariance is computed anywhere in this record.

## 3. The observer assumption: $\rho_4$ and the definitions (A), (B), (C)

### 3.1 Exact identities

The proper 7-volume element of a slice $x_4 = $ const is $\cos z$, independent of $a_4$: the inflation $e^{3a_4}$ of the proper 3-volume is compensated exactly by the deflation $e^{-3a_4}$ of the proper extra-time volume (records `proper_7_volume_element_independent_of_a4`, `proper_3_and_extra_time_volume_scalings`, `local_model_volume_constant`). The conservation law $\nabla_\mu T^\mu{}_\nu = 0$ for a diagonal $T(x_4, x_8)$, re-derived from the author's metric with Christoffel symbols computed anew, gives (records `conservation_x4_identity`, `conservation_x8_identity`, `conservation_other_components_vanish`, `conservation_x4_author_metric`, `conservation_x8_author_metric`, with the negative control `conservation_negative_control`)

$$
\frac{d\rho}{dx_4} = -3a_4'\,(p_3 - p_t),\qquad
\frac{dp_8}{dx_8} + 3H\cot z\,(2p_8 - p_3 - p_t) = 0,\qquad
\frac{dE}{da_4} = -3\,(P_3 - P_t) = -3X .
$$

The 3-space observer averages over the hidden direction with the weight $\sqrt{|g|} = \cos z$, which does not depend on $x_4$ (record `observer_hidden_average_commutes`). The extra times are time-like, so the observer's 4-dimensional density needs a normalisation over them. Three are recorded:

- (A) the extra times are compact with a fixed coordinate period, i.e. closed time-like directions; $\rho_4 = E/(\text{proper 3-volume}) \propto E\,e^{-3a_4}$;
- (B) the extra times are non-compact and $\rho_4$ is taken per unit extra-time COORDINATE volume; $\rho_4 \propto E\,e^{-3a_4}$;
- (C) $\rho_4$ is taken per unit PROPER 7-volume (equivalently per unit proper extra-time volume); $\rho_4 \propto E$.

With the dilution-inferred equation of state $w_{\rm eff} = -1 - \frac13\,d\ln\rho_4/d\ln a$ the conservation identity gives exactly (records `w_eff_A_equals_X_over_E`, `w_eff_B_equals_w_eff_A`, `w_eff_C_equals_X_over_E_minus_1`, `w_eff_general_normaliser`)

$$
w_{\rm eff}(A) = w_{\rm eff}(B) = \frac{X}{E},\qquad w_{\rm eff}(C) = \frac{X}{E} - 1,\qquad
\text{in general } \rho_4 \propto E\,e^{-3(1-s)a_4}:\ w_{\rm eff} = \frac{X}{E} - s .
$$

The dirac16complex00 record names the same two scalings N1 (per unit extra-time coordinate volume, $\rho_4 = e^{-3a_4}\langle\rho\rangle$, the scaling of (A) and (B)) and N2 (per unit proper 7-volume, $\rho_4 = \langle\rho\rangle$, definition (C)), with $w_{\rm eff}(N1) = w_3 - w_t$ and $w_{\rm eff}(N2) = w_{\rm eff}(N1) - 1$ for isotropic sources (records `observer_N1_weff_identity`, `observer_N2_weff_identity`). Below, (B) stands for (A) and (B) together and for N1, and (C) for N2. The ratio $w = p_3/\rho$ does not depend on the normalisation. `Revision/SPEC.md` section 11 writes $\rho_4 \sim \rho_8\,c^3$ with $c = e^{-a_4}$: that is definition (B).

### 3.2 How every verdict depends on the assumption

The rho_4 normalisation is an ASSUMPTION about the observer, not a consequence of the field equations, and this record does not choose one. The same state reads differently under each:

| state (records) | $w_{\rm eff}$ under (A), (B) | $w_{\rm eff}$ under (C) | ratio $p_3/\rho$ |
| --- | --- | --- | --- |
| homogeneous condensate (`condensate_w_eff`) | 0, dust-like | $-1$, cosmological-constant-like | $\lambda S/(2m+\lambda S)$, constant |
| massless quanta (`massless_mode_w_eff`) | $1/3$, radiation | $-2/3$ | $1/3$ |
| massive quanta, flat limit (`massive_mode_w_eff_law`) | $k^2/(3(M^2a^2+k^2))$: $1/3 \to 0$ | $-2/3 \to -1$ | as (A), (B) for $q = 0$ |
| Kohn-Sham gas, $N = 688$, $\lambda = 0$ (section 5.2) | 0.2929 to 0.3183 | -0.7071 to -0.6817 | 0.2929 to 0.3183 |

INTERPRETATION (labelled): supernova distances measure the dilution-inferred $w_{\rm eff}$ of a 4-dimensional Friedmann observer, which agrees with the ratio $p_3/\rho$ only when no energy is exchanged with the extra times ($p_t = 0$ under (B)). Whether (A), (B), (C) or none of them describes such an observer is not decided by any equation of this record. Under (A) the extra times are closed time-like directions; under (B) and (C) they are non-compact and a normalisation is a choice.

### 3.3 The expansion-inferred equation of state

An observer who reads $a(t) = e^{a_4(x_4)}$ with $t = x_4$ ($g_{44} = -1$) and 4-dimensional Friedmann equations infers $w_{\rm exp} = -1 - \frac23\,a_4''/a_4'^2$ (record `expansion_inferred_w`); in Einstein gravity $w_{\rm exp} = -1 - \kappa(p_3 - p_t)/(3a_4'^2)$ for an admissible homogeneous source (both records `expansion_inferred_w_einstein`). On the linear member $a_4 = AHx_4$, the history of the Kohn-Sham record and the only history a condensate allows ($p_3 = p_t$), the observer's Hubble rate $a_4' = AH$ is constant and $w_{\rm exp} = -1$ exactly, with no time variation.

## 4. Method

### 4.1 Exact derivations first

Every effective formula is derived exactly (sympy) before any number is computed: `derive_effective.py` for dirac16complex (30 checks, `Revision/dark_sector/dirac16complex/reports/derivation-checks.json`) and `derive_eos.py` (implementation A) for dirac16complex00 (49 checks, `Revision/dark_sector/dirac16complex00/reports/python-derive-eos.json`). Both re-derive the conservation identities from the author's metric with their own Christoffel symbols; the dirac16complex00 side uses the author's gammas T16 of `Revision/algebra/gammas.json` (record `gammas_clifford_author_T16`). Labels: EXACT means verified by exact symbolic computation in a named check; APPROXIMATION, ASSUMPTION and INTERPRETATION are marked where they apply.

### 4.2 The conservation identities as checks of the numerics

The exact identities of section 3.1 test every numerical history. For the Kohn-Sham gas: $dE/da_4 = -3X$ with fourth-order differences of $E$ against the solver's energy-momentum integrals, maximal relative deviation 1.235e-07 (record `conservation_dE_da4_equals_minus_3X`); integrated with Simpson's rule, 1.927e-08 (`conservation_integrated_simpson`); $d(X/E)/da_4$ two ways, 1.397e-06 (`derivative_two_ways`); the hidden-direction identity $p_{8,y} + 6Hp_8 = 3H(p_3 + p_t)$ in every state, 1.951e-08 (`y_conservation_every_state`). For dirac16complex00 the independent implementation B checks along each run that the Krein charge is conserved (drift at most 1.8378632e-12), that the solution is on shell ($|L_0|$ at most 1.1657342e-15) and that the conservation identity of section 3.1 holds (relative residual at most 4.8268616e-07 by finite differences; records `B_run_*_invariants`).

### 4.3 The Kohn-Sham history (dirac16complex)

`run_ks_history.py` runs the Revision Rust Kohn-Sham solver (`Revision/kohn_sham/solver`, its single-state command, read-only use) at the 41 slices $a_4 = 0, 0.05, \dots, 2$ for $N = 8, 136, 688$ and the five calibrated couplings $\lambda = 0, \pm\lambda_1, \pm\lambda_2$ per $N$: 615 runs (15 series x 41 slices), with $H = m = 1$, $L = 3$, tip $\theta = 0$, $T = 0$ (record `all_runs_succeeded`). The history $a_4 = AHx_4$ is a PRESCRIBED BACKGROUND: the gas is a test field without back-reaction, and the states are instantaneous (adiabatic) ground states. The 75 committed states of `Revision/kohn_sham/results` are reproduced with maximal relative deviation 0.000e+00 (`committed_slices_reproduced`); the occupied label set is the same at all 41 slices of every series, so the instantaneous ground states are the adiabatically continued states (`occupied_labels_fixed_along_history`); the particle number holds to 2.299e-15 (`particle_number_every_state`). `compute_eos.py` evaluates $w_{\rm eff}$ for the three definitions, the ratios, CPL tangents and fits, condensate, mixtures and the Unite comparison (13 checks).

An INDEPENDENT second implementation, `independent_free_gas.py` (numpy; Chebyshev collocation with $n = 96$ and Hellmann-Feynman level derivatives; no solver output used except for the final comparison), reproduces the exact $k = 0$ spectra to 1.421e-14 (`exact_k0_spectra`), is converged ($n = 96$ against 128: 6.01e-15 in $E$, `collocation_converged`), reproduces the solver's $E(a_4)$ over 82 states to 1.897e-12 (`energy_vs_rust_solver`), $w_{\rm eff} = X/E$ to 1.492e-12 (`w_eff_vs_primary`) and the CPL tangents to 4.027e-07 (`cpl_tangent_vs_primary`).

### 4.4 Condensates

The homogeneous condensate is an exact solution for both fields: $S$ is constant, $\rho = mS + \lambda S^2/2$ and $p_3 = p_t = p_8 = \lambda S^2/2$ (records `condensate_rho_p`, `condensate_satisfies_both_identities`, `condensate_rho_p_w`). For dirac16complex00 it is $\Phi = e^{\mathcal{A}x_4}\chi$ with $\mathcal{A} = -\gamma^{(x_4)}(M - 3H\gamma^{(x_8)})$, $M = m + U'(S)$; $C\mathcal{A} + \mathcal{A}^TC = 0$ for the author's T16, so $S$ is constant, and $K_{x_4} = MS$ exactly (records `condensate_S_constant_T16`, `condensate_K4_equals_MS_T16`, with the negative control `condensate_negative_control`). As a source of the field equations for $a_4$ the condensate allows only the linear member $a_4 = AHx_4 + a_0$ ($p_3 = p_t$ forces $a_4'' = 0$).

### 4.5 Modes and Krein-signed energies (dirac16complex00)

For a plane wave with 3-momentum $k$ and extra-time momentum $q$ in the frozen local frame, $h^2 = (m^2 + k^2 - q^2)I_{16}$, so $\omega^2 = m^2 + k^2 - q^2$: the extra times are time-like and $q$ enters with the opposite sign (`mode_dispersion_h_squared`). $Bh$ is Hermitian, so the charge density $Q = \Phi^\dagger B\Phi$ is the Krein form of the frozen-frame evolution and is conserved by it (`mode_generator_B_selfadjoint`). On the real-frequency eigenspaces of the test cases of section 6.2, $T^\mu{}_\nu = k^\mu k_\nu Q/\omega$ exactly, so $\rho = \omega Q$: the energy has the sign of $\omega Q$.

### 4.6 Gases, mixtures and wave packets

dirac16complex00: adiabatic (WKB) gases of plane-wave modes in the deflating local model, an APPROXIMATION: the warp $\sin^{1/6}z$ and $\tan z$ are frozen at a fixed hidden position (wavelengths short compared with $1/H$), the Krein charge of each mode is an adiabatic invariant, and the superposition is incoherent. Each component has $\rho_i = \omega_iQ_i$, $p_3 = k^2Q/(3a^2\omega)$, $p_t = -q^2a^2Q/(3\omega)$ and $\varepsilon_i = w_{\rm eff}(B)_i = (k^2/a^2 + q^2a^2)/(3\omega_i^2) \geq 0$, independent of the sign of $Q$ (records `wkb_mode_gas_conservation`, `wkb_epsilon_sign_free`); a mixture has $w_{\rm eff}(B) = \sum\varepsilon_i\rho_i/\sum\rho_i$ (`mixture_weighted_average`). Implementation B integrates the full 16-component field equation of the local model with the author's T16 (exact Krein-preserving exponential midpoint step, $AH/m = 10^{-3}$, adiabatic) and rebuilds the models from its solutions; spatial averages of superpositions equal the sums of the mode contributions (`B_superposition_average`). dirac16complex: mixtures of the Kohn-Sham gas with a condensate, $w_{\rm eff} = \sum_iX_i/\sum_iE_i - s$.

### 4.7 Phantom conditions

dirac16complex: $w_{\rm eff}(C) < -1$, equivalently $w_{\rm eff}(A) < 0$, holds if and only if $X/E < 0$; with $E > 0$ this needs $P_t > P_3$, which no real-frequency mode supplies (per mode $X = (k^2e^{-2a_4} + q^2e^{2a_4})/(3\omega) \geq 0$, with $p_3 \geq 0$ and $p_t \leq 0$), otherwise $E < 0$ together with $X > 0$ (records `phantom_condition`, `flat_mode_X_nonnegative`; `phantom_condition` verifies the identity $w_{\rm eff}(C) + 1 = X/E$, not the origin of a negative $E$). Negative $E$ is not specific to a negative-norm (Krein) sector in the canonical Kohn-Sham record: there the interacting $N = 8$, $\lambda > 0$ good-sector states have $E < 0$, with $X = 0$ exactly (section 5.2), from the interaction energy of the canonical uniform-gas exchange functional ($E = 0$ at $\lambda = 0$). With the exact Fock exchange in place of that functional, solved self-consistently (the exact-Fock variant of the Kohn-Sham record, `Revision/kohn_sham/results/exx/exact-fock-variant.csv`), the same $N = 8$ states have $\lvert E\rvert \leq 2.04 \times 10^{-13}$; the exact exchange evaluated to first order on the canonical orbitals still leaves $E < 0$, of smaller magnitude. This negative $E$ is therefore a property of the approximate functional; good-sector states with $E < 0$ are not established beyond it. For free modes $E < 0$ needs a negative Krein charge, outside the positive good-sector realisation (OPEN). dirac16complex00 (EXACT within the WKB model): if every component has $\rho_i \geq 0$ and a real frequency, then $w_{\rm eff}(B) \geq 0$ and $w_{\rm eff}(C) \geq -1$ at every $a$ at which these conditions hold (an extra-time mode loses its real frequency past its turning point $a_*$, section 6.3); a crossing of $-1$ needs a component of negative classical energy. The only phantom without a negative energy density is the constant ratio of a condensate: $p/\rho < -1$ exactly for $\lambda S/m \in (-2, -1)$ (`condensate_phantom_interval`).

## 5. Results for dirac16complex

Records: `Revision/dark_sector/dirac16complex/reports/` and `Revision/dark_sector/dirac16complex/outputs/eos-summary.json`.

### 5.1 The condensate

$X = 0$, so $w_{\rm eff}(A) = w_{\rm eff}(B) = 0$ (dust-like dilution $a^{-3}$) and $w_{\rm eff}(C) = -1$; the ratio is $w = \lambda S/(2m + \lambda S)$; all are constant ($w_a = 0$ in every definition; `condensate_w_eff`, `condensate_ratio_w`). The ratio equals the Unite constant $w = -0.764$ at $\lambda S/m = -382/441 = -0.866213151927$, with $\rho/(mS) = 0.566893424036$, so $\rho > 0$ if and only if $mS > 0$ (`condensate_ratio_equal_unite_constant_w`, `condensate_ratio_value`). This value of $\lambda S/m$ is CHOSEN to give -0.764: one parameter tuned to one number. It is the constant 8-dimensional ratio, not the observer's dilution-inferred $w_{\rm eff}$, which is 0 or -1.

### 5.2 The Kohn-Sham gas

- The occupied levels lie on the brane band, which is massless at $k = 0$ (the brane zero mode at $\varepsilon = 0$, slope $c\,e^{-a_4}$ with $c = 1.9051482536$ at small $k$; `brane_band_slope`). The gas therefore redshifts like radiation, not like dust: $d\ln E/da_4$ goes from -0.8787 at $a_4 = 0$ to -0.9549 at $a_4 = 2$ ($N = 688$, $\lambda = 0$), toward the radiation value $-1$.
- Over all $N = 136, 688$ series and all slices, $X/E$ lies in [0.292893, 0.328105] and rises monotonically toward $1/3$ (`gas_radiation_like_band`, `gas_X_over_E_rises_toward_one_third`).
- $N = 688$, $\lambda = 0$: $w_{\rm eff}(A) = w_{\rm eff}(B)$ goes from 0.2929 to 0.3183 and $w_{\rm eff}(C)$ from -0.7071 to -0.6817. The ratio $w_3 = P_3/E$ equals $X/E$ up to $|P_t/E| \leq 0.002$ over the $N = 136, 688$ series ($P_t$ is the integrated interaction part; it vanishes at $\lambda = 0$). The hidden-direction ratio $w_8 = P_8/E$ goes from 0.3535 to 0.6482: a pressure that the 3-space observer does not see as pressure.
- CPL tangents ($N = 688$, $\lambda = 0$):

| $a_{4,\rm today}$ | 0.5 | 1 | 1.5 | 2 |
| --- | --- | --- | --- | --- |
| $w_0$ under (C) | -0.7037 | -0.6982 | -0.6907 | -0.6817 |
| $w_a$ (every definition) | -0.00905 | -0.01292 | -0.01701 | -0.01775 |

  ($w_0$ under (A), (B) is $w_0(C) + 1$.) Least-squares fits at $a_{4,\rm today} = 2$: over $a \in [1/2, 1]$, $w_a = -0.02424$ and constant proxy $-0.6872$ under (C); over $[1/3, 1]$, $w_a = -0.02648$ and $-0.6895$.
- Over all $N = 136, 688$ series: tangent $w_a$ in [-0.020523, -0.008894], fitted $w_a$ in [-0.030371, -0.018132], $w_{\rm eff}(C)$ in [-0.707107, -0.671895] (`gas_cpl_thawing_sign_small`): the thawing sign, with magnitudes far below the Unite 0.60.
- $N = 8$ with $\lambda \neq 0$ (only the $k = 0$ brane zero modes): $E$ constant and $P_3 = P_t$, so $w_{\rm eff}(A) = 0$ and $w_{\rm eff}(C) = -1$, constant, with $E < 0$ for $\lambda > 0$ (`n8_interacting_zero_modes_constant`; a property of the canonical uniform-gas exchange functional, section 4.7). $N = 8$ with $\lambda = 0$ has $E = 0$: no equation of state.

### 5.3 The bulk band (independent implementation)

The massive bulk band (odd brane parity, $\varepsilon(0)$ = 1.292292828069 = the bulk edge) shows the dark-matter-like law: for the lowest odd-parity level of the $n_2 = 1$ shell, $w_{\rm eff}(A)$ falls monotonically from 0.239626 at $a_4 = -3$ to 2.268e-03 at $a_4 = 4$, asymptotically like $1/a$ (the ratio $w(4)/w(3.75) = 0.765177$ against $e^{-0.25} = 0.778801$: a linear term of $\varepsilon(k)$ at small $k$); the brane-band level of the same shell stays in [0.291594, 0.333275], tending to $1/3$ (records `bulk_band_dark_matter_law`, `brane_band_radiation_law`; free gas, $\lambda = 0$, on the prescribed history). The canonical $T = 0$ states ($N \leq 688$) are filled below the bulk edge and do not populate that band.

### 5.4 Mixtures with a condensate

In every definition the mixture's $w$ moves toward the condensate's value as the gas redshifts: $w_a > 0$, freezing. Exactly, for a radiation-like gas ($X = E/3$) plus a condensate, $w_{\rm eff}(A) = \frac13\,r/(1+r)$ with $r = r_0/a$, $w_0 = r_0/(3(r_0+1))$ and $w_a = r_0/(3(r_0+1)^2) > 0$ (`mixture_radiation_condensate_cpl`); $w_{\rm eff}(C) = -0.861$ today needs $r_0 = 417/583 = 0.715265866209$, CHOSEN for that purpose, and then $w_a = 0.081037$, not $-0.60$ (`mixture_C_matching_w0_unite`). With the computed gas ($N = 688$, $\lambda = 0$, $a_{4,\rm today} = 2$) under (C):

- the gas fraction 0.436703 is CHOSEN so that $w_{\rm eff}(C) = -0.861$ today; then $w_a = 0.067014 > 0$, freezing (`mixture_C_w0_unite_has_positive_wa`);
- the gas fraction 0.6807148417136 is CHOSEN so that the constant-$w$ proxy over $[1/3, 1]$ equals -0.764; the CPL fit of that mixture is $(w_0, w_a) = (-0.7841, 0.0603)$, opposite in the sign of $w_a$ to the Unite fit (`mixture_C_constant_w_unite_reachable_only_with_freezing_cpl`; the proxy caveat of section 2.3 applies);
- in the ratio definition, with a condensate of any constant ratio $w_c \in [-3, 1]$, any gas fraction and $a_{4,\rm today} \in \{0.5, 1, 1.5, 2\}$, the smallest $w_a$ among mixtures with $|w_0 + 0.861| \leq 0.1$ is 0 (the pure condensate), and the Unite pair is never closer than 0.600001 (`ratio_mixture_scan_cannot_reach_unite_wa`).

### 5.5 Phantom and crossing of $-1$

No computed state crosses $w = -1$: every state with $E \neq 0$ has $X \geq 0$. All of them have $E > 0$ except the $N = 8$, $\lambda > 0$ states, which have $E < 0$ (from the canonical uniform-gas exchange functional; section 4.7) and $X = 0$ exactly ($w_{\rm eff}(C) = -1$, $w_{\rm eff}(A) = 0$); the 41 $N = 8$, $\lambda = 0$ states have $E = 0$ and no equation of state (section 5.2). On the prescribed history the expansion reads $w_{\rm exp} = -1$ exactly (section 3.3).

## 6. Results for dirac16complex00

Records:

- the reports in `Revision/dark_sector/dirac16complex00/reports/`;
- implementation A: `Revision/dark_sector/dirac16complex00/eos-theory.json`;
- the independent implementation B, the field-equation runs: `Revision/dark_sector/dirac16complex00/results/independent-numerics.json`.

### 6.1 The condensate

As for dirac16complex: $w_{\rm eff}(B) = 0$, $w_{\rm eff}(C) = -1$, ratio $\lambda S/(2m + \lambda S)$, all constant. The ratio equals -0.764 at $\lambda S/m = -382/441$ (CHOSEN), which with $\rho > 0$ needs $mS > 0$ and $\lambda < 0$, a negative potential $U$ (`condensate_ratio_equals_unite_constant_w`); it is phantom exactly for $\lambda S/m \in (-2, -1)$. For a condensate that is the self-consistent source of the linear member ($A = a_4'/H$),

$$
\kappa(\rho + p) = -(a_4'^2 + H^2)\big[6\alpha_1 - 48\alpha_2(a_4'^2 + 5H^2) + 432\alpha_3(a_4'^4 + 2a_4'^2H^2 + 5H^4)\big]
$$

(`linear_member_rho_plus_p_factorises`). In Einstein gravity $\rho + p = -6(1 + A^2)H^2/\kappa$, so the source has the constant ratio $w = -1 - 6(1 + A^2)H^2/(\kappa\rho)$, which is phantom ($w < -1$) exactly when $\kappa\rho > 0$ (`linear_member_einstein_phantom_ratio`, whose detail states the hypotheses $\kappa > 0$ and $\rho > 0$), and $w > -1$ for $\kappa\rho < 0$. The sign of $\kappa\rho$ is not free: on the linear member the $x_4$ constraint of the record gives $\kappa\rho = -(3A^2 + 21)H^2 - \Lambda$ (`Revision/field_equations_a4/a4-equations.json`, keys `linearMember/rhoEinstein` and `einstein/allowedA4`), so that $w = -1 + 6(1 + A^2)H^2/((3A^2 + 21)H^2 + \Lambda)$, which is phantom exactly when $\Lambda < -(21 + 3A^2)H^2$. The hypotheses $\kappa > 0$, $\rho > 0$ of the check therefore need such a negative $\Lambda$; for $\Lambda = 0$ the ratio is $w = (A^2 - 5)/(A^2 + 7) > -1$, not phantom. The sign of $\kappa$ itself is not fixed by this record (the Kohn-Sham source study `Revision/field_equations_a4/ks_source`, which concerns a different source, the Kohn-Sham gas, examines $\kappa$ of either sign; there too $\Lambda = 0$ forces $\sigma_0 = \kappa\bar\rho(0)/H^2 < 0$). The observer's expansion reads $w_{\rm tot} = -1$ exactly (`expansion_inferred_w_einstein`).

### 6.2 Modes, Krein-signed energies and growing modes

For the three test cases $(m, k, q) = (3, 4, 0)$, $(5, 0, 3)$ and $(4, 4, 4)$, with $\omega = \pm5$, $\pm4$ and $\pm4$, every real-frequency eigenspace has dimension 8 and a Krein form of signature (4,4), and on it $\rho = \omega Q$ exactly (records `mode_krein_inertia_*`, `mode_emt_*`, negative control `mode_emt_negative_control`): at every real frequency there are modes of both energy signs. Implementation B confirms it: at $\omega = 1.25$ the vectors with $Q = +1$ and $Q = -1$ have $\rho = +1.25$ and $-1.25$ (`B_krein_signed_energy`). The general statement is the Krein-inertia theorem of `Revision/pairing`.

For $q^2 > m^2 + k^2$ the modes grow: for $(m, k, q) = (3, 0, 5)$, $\omega = 4i$; the growing eigenspace is Krein-neutral ($Q = 0$, $\rho = 0$) with a growing extra-time pressure $p_5 = -mS$ (`growing_mode_krein_neutral`, `growing_mode_extra_time_pressure`). In the deflating field the physical extra-time momentum $qa$ grows, so every mode with $q \neq 0$ reaches a turning point $a_*$ and then grows: the deflation drives the growth. Implementation B, past the turning point $a_* = 1.8433886$ of the mode of M3: growth rate $d\ln|\phi|/dx_4 = 0.54337468$ against the WKB rate 0.55114035 (`B_growth_rate`); the amplitude grows by a factor $10^{32.17}$ between $a = 1.5$ and $2.2$, and the energy density becomes large and negative ($\rho/Q$ = -2.9228317e+61 at $a = 2.2$, for $AH/m = 10^{-3}$).

### 6.3 The models M1 to M5

Each model is normalised to $\rho_{\rm tot} = 1$ at $a = 1$; definition (C) unless stated. In every model the parameters marked CHOSEN were fixed so that the model reproduces a Unite number; that number is then an input, not an output.

| model | content | CHOSEN parameters |
| --- | --- | --- |
| M1 | condensate (exact solution for every $a_4$) | $\lambda S/m$ free; the ratio is $-0.764$ at $\lambda S/m = -382/441$ (CHOSEN) |
| M2 | positive-energy good-sector gas, $q = 0$ | $k^2/(k^2+m^2) = 417/1000$ at $a = 1$, CHOSEN for $w_0 = -0.861$ |
| M3 | positive-energy extra-time mode, $k = 0$ | $s = q^2/m^2 = 417/1417$, CHOSEN for $w_0 = -0.861$ |
| M4 | condensate + positive extra-time mode | $s = 264037/403037$ and $\Omega_q = 57963/264037$, both CHOSEN to solve tangent $= (-0.861, -0.60)$ |
| M5 | M4-type + GHOST: massless modes of negative classical energy | $G = 3/10$ of the total at $a = 1$ (a stated choice); $s$ and $\Omega_q$ CHOSEN so that the fit over $[1/2, 1]$ is $(-0.861, -0.60)$ |

The resulting CPL numbers under (C) (tangent; least-squares fit over $[1/2, 1]$; constant proxy):

| model | tangent $w_0$ | tangent $w_a$ | fit $w_0$ | fit $w_a$ | proxy | crosses $-1$ on $[1/3, 1]$? |
| --- | --- | --- | --- | --- | --- | --- |
| M1 | -1 | 0 | -1 | 0 | -1 | no |
| M2 | -0.861 | +0.162074 | -0.8655 | 0.2173 | -0.8112 | no |
| M3 | -0.861 | -0.393926 | -0.8734 | -0.2196 | -0.9283 | no |
| M4 | -0.861 | -0.600 | -0.8832 | -0.2203 | -0.9383 | no |
| M5 | -0.8396 | -1.0399 | -0.861 | -0.600 | -1.011 | at $a = 0.7791$ |

M2 is freezing ($w_a > 0$), M3 and M4 are thawing ($w_a < 0$); the M4 tangent and the M5 fit equal the Unite pair by construction. The last column is the crossing search of the record on $1/3 \leq a \leq 1$; it says nothing about $a > 1$, and past the turning point $a_*$ of an extra-time mode (M3: 1.8434, M4: 1.2355, M5: 1.3271) the frequency of that mode is imaginary and the bound of section 4.7 does not apply (see the notes below). Records:

| record | record | record |
| --- | --- | --- |
| `M2_tangent_exact` | `M3_tangent_exact` | `M4_parameters_exact` |
| `M4_tangent_equals_unite` | `M4_never_phantom` | `M5_fit_equals_unite` |
| `M5_crosses_minus_1` | `M5_without_ghost_no_crossing` | `unite_line_fit_proxy` |

Notes:

- M2 under (B) and in the ratio: tangent $(0.139, 0.162074)$, the law $w_{\rm eff}(B) = \frac13k^2/(k^2 + m^2a^2)$ from $1/3$ to 0: a time-varying dark-matter-like equation of state. Exactly, $w_a = 81037/500000$.
- M3: $w_{\rm eff}(C) = -1 + \frac13\,sa^2/(1 - sa^2) \geq -1$ for $a < a_*$; $w_a = -196963/500000$; the turning point is at $a_* = \sqrt{1417/417} = 1.8434$, in the future. Past it the frequency of the mode is imaginary, the mode grows (`B_growth_rate`) and its energy density becomes large and negative ($\rho/Q = -2.9 \times 10^{61}$ at $a = 2.2$ in implementation B, `Revision/dark_sector/dirac16complex00/results/independent-numerics.json`), so the bound $w_{\rm eff}(C) \geq -1$ does not extend past $a_*$.
- M4: $s = 0.6551$, $\Omega_q = 0.2195$. Its actual $w(a)$ does not cross $-1$ on $a \in [1/300, 1]$: the minimum of $w_{\rm eff}(C)$ over $a = 1/300, \dots, 1$ is -0.999999214228; by section 4.7 the bound $w_{\rm eff}(C) \geq -1$ holds up to the turning point $a_*$ of its extra-time mode. The phantom past $w_0 + w_a = -1.461$ belongs to the linear CPL extrapolation, not to the model. Its own fit over $[1/2, 1]$ is not the Unite pair. Its extra-time mode reaches its turning point at $a_* = 1.2355$ and then grows without bound; past $a_*$ its frequency is imaginary, section 4.7 does not apply, and $w \geq -1$ is not established there. Under (B) or in the ratio, M4 is not dark energy ($w \geq 0$).
- M5: $s = 0.5678$, $\Omega_q = 0.5947$, condensate fraction $\Omega_c = 0.7053$; the crossing of $-1$ is at $a = 0.7791$ (Unite line: 0.7683); its turning point is at $a_* = 1.3271$. Without its ghost component M5 does not cross $-1$. INTERPRETATION: because $s$ and $\Omega_q$ were chosen so that the fit over $[1/2, 1]$ equals the Unite line, a crossing close to the line's crossing is expected and is not an independent agreement.

### 6.4 The independent implementation B

B rebuilds M2 to M5 from solutions of the 16-component field equation; all tangents, fits and constant proxies agree with implementation A to within 0.00083082726 (records `B_vs_A_*`). The M5 crossing comes out at $a$ = 0.77905405 (A: 0.77909966367; `B_vs_A_M5_crossing`). By bisection on the field-equation solutions B finds $s = 0.29426353$ for M3 (A: $417/1417$) and $s = 0.65505409$, $\Omega_q = 0.21946024$ for M4 (`B_solve_M3_s`, `B_solve_M4`).

## 7. Comparison with the Unite values

| Unite value | dirac16complex | dirac16complex00 | by construction? |
| --- | --- | --- | --- |
| constant $w = -0.764$ | condensate ratio at $\lambda S/m = -382/441$ (8-dimensional ratio; $w_{\rm eff}$ is 0 or -1); (C) mixture with gas fraction 0.6807148417136 (constant proxy; CPL slope $+0.0603$) | condensate ratio at $\lambda S/m = -382/441$, $\lambda < 0$ | yes: one parameter for one number |
| $w_0 = -0.861$ | (C) mixture with gas fraction 0.436703: $w_a = 0.067014$, freezing | M2 ($w_a = +0.162074$), M3 ($w_a = -0.393926$) | yes: one parameter for one number |
| $(w_0, w_a) = (-0.861, -0.60)$ | not reached: (C) gas $\lvert w_a\rvert \leq 0.030371$; ratio mixtures never closer than 0.600001 | M4 tangent exactly; M5 fit over $[1/2, 1]$ exactly | yes: two parameters for two numbers |
| phantom past, crossing of $-1$ at $a = 0.7683$ | no crossing in any computed state | only M5, with a ghost-like component: crossing at $a = 0.7791$ | the fit is by construction; the ghost fraction is a stated choice |

A model with as many tuned parameters as matched numbers reproduces them by construction and is NOT a prediction. No parameter of M2 to M5, of the mixtures or of the condensate ratio is selected by the field equations; nothing in this record selects their populations. A ghost (negative-energy) component is a ghost-like sector, not an established physical state: dirac16complex00 has one at every real frequency, and its classical energy is unbounded below (the classical form of the spin-statistics problem of a commuting field with a first-order Lagrangian).

What is not tuned: the signs and the ranges. For positive-energy content with real frequencies $w_{\rm eff}(C) \geq -1$ in the WKB model of dirac16complex00 (section 4.7; for M3 and M4 this means before the turning point $a_*$ of the extra-time mode), and every computed dirac16complex state has $X \geq 0$ (section 5.5); the computed dirac16complex gas has the thawing sign with $\lvert w_a\rvert \leq 0.030371$; condensate-gas mixtures are freezing; M4, tuned to the Unite tangent, does not cross $-1$ before its turning point $a_* = 1.2355$ (checked on $a \in [1/300, 1]$).

## 8. The lead's analysis (SPEC section 11), checked point by point

1. “The 7-volume of the metric is constant.” CONFIRMED exactly: the proper 7-volume element is $\cos z$, independent of $a_4$ (`proper_7_volume_element_independent_of_a4`, `local_model_volume_constant`).
2. “The effective 4-dimensional density is $\rho_4 \sim \rho_8c^3$.” This is definition (B) (with (A) of the same scaling). It is an ASSUMPTION about the observer: definition (C), per unit proper 7-volume, is equally consistent with the field equations and shifts every $w_{\rm eff}$ by exactly $-1$ (section 3).
3. “Non-relativistic quanta give dust, relativistic quanta radiation.” CONFIRMED under (A), (B) in the flat (warp-free) limit: a massive mode has $w_{\rm eff} = k^2/(3(M^2a^2 + k^2))$, $1/3 \to 0$, and a massless one $1/3$ (`massive_mode_w_eff_law`, `massless_mode_w_eff`); the Kohn-Sham gas has $d\ln E/da_4$ approaching $-1$ (section 5.2).
4. “A Kohn-Sham gas whose 3-momenta redshift has a time-varying equation of state from $1/3$ towards 0.” NOT FOUND in the computed states: the occupied levels lie on the massless brane band and $w_{\rm eff}(A)$ RISES toward $1/3$ (section 5.2). The falling law is present for quanta of the massive bulk band (section 5.3), which the computed ground states do not populate. For dirac16complex00 the falling law holds for a positive-energy gas of good-sector modes (M2). The hidden-direction pressure ($w_8$ = 0.3535 to 0.6482) and the extra-time pressure ($|P_t/E| \leq 0.002$) were computed; the 3-space observer does not see them as pressure.
5. “A homogeneous condensate has constant $w$ while $\rho_4 \sim a^{-3}$; the ratio and $w_{\rm eff} = 0$ disagree; 4-dimensional energy is exchanged with the extra dimensions.” CONFIRMED exactly for both fields under (B) (`condensate_w_eff`, `condensate_rho_p_w`); under (C) $w_{\rm eff} = -1$. The exchange reading is an INTERPRETATION of the disagreement between the ratio and the dilution.
6. “Whether any state gives a time-varying dark-energy equation of state near the Unite values must be computed.” COMPUTED: for dirac16complex no computed state comes near the Unite pair in any definition (section 5); for dirac16complex00 only definition (C) gives dark-energy-like values, and the Unite numbers are reached only by tuned models (sections 6.3 and 7).
7. “Crossing $w = -1$ needs negative kinetic energy, which the indefinite (Krein) energy of the extra-time sector and the commuting field dirac16complex00 may supply.” EXAMINED. Positive-energy extra-time momentum does NOT supply it: its pressure $p_t \leq 0$ increases $X$, so it moves $w_{\rm eff}$ up, not down (`flat_mode_X_nonnegative`, `wkb_epsilon_sign_free`; M3 has $w \geq -1$ before its turning point $a_* = 1.8434$). What is needed is negative classical ENERGY: dirac16complex00 has it at every real frequency (Krein signature (4,4)), and with it the crossing occurs (M5), as a ghost-like sector. For dirac16complex no computed state has $X < 0$; the only states with $E < 0$ ($N = 8$, $\lambda > 0$, negative only with the canonical uniform-gas exchange functional, section 4.7) have $X = 0$ exactly. Modes of dirac16complex with extra-time momentum lie outside the good sector and are OPEN.

## 9. Verdicts

### 9.1 dirac16complex (Hypothesis)

- Dark matter. Under (A), (B): a time-varying dark-matter-like equation of state, $w_{\rm eff}$ falling from $1/3$ toward 0, is present in the theory for quanta of the massive bulk band (0.239626 at $a_4 = -3$ to 2.268e-03 at $a_4 = 4$ for one shell; the flat-limit law is exact). It is NOT present in the computed Kohn-Sham ground states, whose brane-band gas is radiation-like with $w_{\rm eff}$ rising toward $1/3$. A condensate is dust-like ($w_{\rm eff} = 0$, constant).
- Dark energy. Only under (C): the gas has $w_{\rm eff}(C)$ in [-0.707107, -0.671895] with a thawing-sign slope (tangent $w_a$ in [-0.020523, -0.008894], fitted in [-0.030371, -0.018132]), far from the Unite pair; condensate-gas mixtures are freezing; the Unite constant $w = -0.764$ is matched only by the constant 8-dimensional ratio of a tuned condensate or by a tuned (C) mixture whose CPL slope has the opposite sign. No computed state crosses $w = -1$.
- On the prescribed history the observer's expansion reads $w_{\rm exp} = -1$ exactly.

### 9.2 dirac16complex00 (Hypothesis00)

- Dark matter. Under (B) and in the ratio $p_3/\rho$: a positive-energy gas of good-sector modes has the time-varying law from $1/3$ to 0 (M2); a condensate is dust-like. Under (C) the same states look like dark energy instead.
- Dark energy without ghosts. Only under (C), as freezing (M2, $w \geq -1$ at every $a$) or thawing (M3, M4) evolution; for M3 and M4, $w \geq -1$ holds only before the turning point $a_*$ of the extra-time mode (M3: $a_* = 1.8434$, exactly from its closed form; M4: $a_* = 1.2355$, by section 4.7, checked numerically on $a \in [1/300, 1]$). The thawing is driven by the deflation, which blueshifts the extra-time momentum, and the same mode grows without bound past its turning point: its frequency is imaginary there, section 4.7 does not apply, and for M3 the energy density becomes large and negative (implementation B); past $a_*$ the bound $w \geq -1$ is not established. M4 reproduces the Unite CPL tangent by construction, and its $w$ does not cross $-1$ before its turning point.
- Phantom and crossing of $-1$. Impossible with positive-energy components of real frequency (section 4.7); they occur only with a component of negative classical energy (M5, with a 30 % ghost fraction chosen and a fit tuned to the Unite line). The only phantom without negative energy density is the constant ratio of a condensate with $\lambda S/m \in (-2, -1)$, which is not the observer's $w_{\rm eff}$.
- Backreacted condensate (Einstein gravity): the linear member, a constant ratio $w < -1$ for $\kappa\rho > 0$ ($w > -1$ for $\kappa\rho < 0$); the record's $x_4$ constraint fixes $\kappa\rho = -(3A^2 + 21)H^2 - \Lambda$, so the ratio is phantom exactly when $\Lambda < -(21 + 3A^2)H^2$ and lies above $-1$ for $\Lambda = 0$ (section 6.1), and $w_{\rm tot} = -1$ exactly from the expansion; a time-varying total $w$ needs $a_4'' \neq 0$, i.e. $p_3 \neq p_t$, which no condensate gives.

### 9.3 The hypotheses

This record establishes neither Hypothesis nor Hypothesis00. What it shows, under its stated assumptions: both fields contain time-varying equations of state of the dark-matter type under definition (B) (dirac16complex only for bulk-band quanta, which the computed states do not populate); dark-energy-like values arise only under definition (C); the Unite numbers are reproduced only by models whose parameters were chosen to reproduce them; and the phantom crossing only with a ghost-like sector of dirac16complex00. Nothing in this record establishes that either field is dark energy or dark matter.

## 10. What remains open

1. A self-consistent (non-linear) $a_4$ history with an admissible source. No recorded Kohn-Sham state is an admissible source of the author's metric: its energy-momentum tensor depends on $x_8$ and violates $p_3 + p_t = 2p_8$, and the history is a prescribed background (the 5 checks of `Revision/field_equations_a4/reports/ks-source-conditions.json`, among them `ks_profiles_depend_on_x8` and `ks_profiles_violate_algebraic_condition`). The truncated integration of the $a_4$ equations with the averaged Kohn-Sham source is an approximation and is not used here. The condensate is an exact source only on the linear member.
2. Populated bulk-band or thermal states along the history (fixed entropy); only $T = 0$ ground states and $a_4 \in [0, 2]$ (the solver's validated range) are computed.
3. Modes of dirac16complex with extra-time momentum (outside the good sector; only their flat-limit sign structure is derived) and the non-adiabatic (time-dependent) Kohn-Sham problem.
4. For dirac16complex00: configurations that depend on $x_8$ are not consistent sources of the metric; the WKB model freezes the hidden-direction warp; the growing modes make the Cauchy problem ill-posed, and nothing here cures that; no quantum treatment (a classical field).
5. Which normalisation of $\rho_4$, if any, describes a physical 3-space observer; the value of $a_{4,\rm today}$.
6. What would select the populations of M2 to M5, the mixture fractions or the condensate's $\lambda S/m$.
7. A supernova likelihood (distances, covariances): no fit to data is part of this record.

## 11. Verification records

### 11.1 Reports and their counts

Every check has a name, a verdict and a detail. Counts at the time of writing (the publication test re-reads them):

| report | checks | PASS | FAIL |
| --- | --- | --- | --- |
| `Revision/dark_sector/dirac16complex/reports/derivation-checks.json` | 30 | 30 | 0 |
| `Revision/dark_sector/dirac16complex/reports/ks-history-run.json` | 5 | 5 | 0 |
| `Revision/dark_sector/dirac16complex/reports/eos-checks.json` | 13 | 13 | 0 |
| `Revision/dark_sector/dirac16complex/reports/independent-checks.json` | 9 | 9 | 0 |
| `Revision/dark_sector/dirac16complex00/reports/python-derive-eos.json` | 49 | 49 | 0 |
| `Revision/dark_sector/dirac16complex00/reports/python-independent-numerics.json` | 28 | 28 | 0 |
| `Revision/field_equations_a4/reports/ks-source-conditions.json` | 5 | 5 | 0 |

### 11.2 Checks per report

The tables list every check of the six dark-sector reports; every one has the verdict PASS.

**dirac16complex, derive_effective.py** (30 checks):

| check | check | check |
| --- | --- | --- |
| `sqrt_det_g_equals_cos_z` | `proper_7_volume_element_independent_of_a4` | `proper_3_and_extra_time_volume_scalings` |
| `conservation_x4_identity` | `conservation_x8_identity` | `conservation_other_components_vanish` |
| `hidden_coordinate_dy_dx8` | `conservation_x8_in_y_form` | `integrated_identity_dE_da4` |
| `w_eff_A_equals_X_over_E` | `w_eff_B_equals_w_eff_A` | `w_eff_C_equals_X_over_E_minus_1` |
| `w_eff_general_normaliser` | `condensate_rho_p` | `condensate_satisfies_both_identities` |
| `condensate_ratio_w` | `condensate_w_eff` | `condensate_ratio_equal_unite_constant_w` |
| `flat_mode_mass_shell` | `flat_mode_X_nonnegative` | `massive_mode_w_eff_law` |
| `massive_mode_cpl_tangent` | `massless_mode_w_eff` | `mixture_radiation_condensate_cpl` |
| `mixture_C_matching_w0_unite` | `cpl_least_squares_rule` | `unite_deep_past` |
| `expansion_inferred_w` | `expansion_inferred_w_einstein` | `phantom_condition` |

**dirac16complex, run_ks_history.py** (5 checks):

| check | check | check |
| --- | --- | --- |
| `all_runs_succeeded` | `committed_slices_reproduced` | `occupied_labels_fixed_along_history` |
| `y_conservation_every_state` | `particle_number_every_state` |  |

**dirac16complex, compute_eos.py** (13 checks):

| check | check | check |
| --- | --- | --- |
| `formulas_input_present` | `dense_history_complete` | `conservation_dE_da4_equals_minus_3X` |
| `conservation_integrated_simpson` | `derivative_two_ways` | `gas_radiation_like_band` |
| `gas_X_over_E_rises_toward_one_third` | `n8_interacting_zero_modes_constant` | `condensate_ratio_value` |
| `mixture_C_w0_unite_has_positive_wa` | `mixture_C_constant_w_unite_reachable_only_with_freezing_cpl` | `ratio_mixture_scan_cannot_reach_unite_wa` |
| `gas_cpl_thawing_sign_small` |  |  |

**dirac16complex, independent_free_gas.py** (9 checks):

| check | check | check |
| --- | --- | --- |
| `exact_k0_spectra` | `brane_band_slope` | `collocation_converged` |
| `aufbau_closed_shells` | `energy_vs_rust_solver` | `w_eff_vs_primary` |
| `cpl_tangent_vs_primary` | `bulk_band_dark_matter_law` | `brane_band_radiation_law` |

**dirac16complex00, derive_eos.py (A)** (49 checks):

| check | check | check |
| --- | --- | --- |
| `gammas_clifford_author_T16` | `conservation_negative_control` | `conservation_x4_author_metric` |
| `conservation_x8_author_metric` | `conservation_other_components_vanish` | `conservation_x4_local_model` |
| `local_model_volume_constant` | `observer_N1_weff_identity` | `observer_N2_weff_identity` |
| `observer_hidden_average_commutes` | `condensate_S_constant_T16` | `condensate_negative_control` |
| `condensate_K4_equals_MS_T16` | `condensate_rho_p_w` | `condensate_phantom_interval` |
| `condensate_ratio_equals_unite_constant_w` | `linear_member_rho_plus_p_factorises` | `linear_member_einstein_phantom_ratio` |
| `expansion_inferred_w_einstein` | `mode_dispersion_h_squared` | `mode_generator_B_selfadjoint` |
| `mode_emt_negative_control` | `mode_krein_inertia_m3_k4_q0_pos` | `mode_emt_m3_k4_q0_pos` |
| `mode_krein_inertia_m3_k4_q0_neg` | `mode_emt_m3_k4_q0_neg` | `mode_krein_inertia_m5_k0_q3_pos` |
| `mode_emt_m5_k0_q3_pos` | `mode_krein_inertia_m5_k0_q3_neg` | `mode_emt_m5_k0_q3_neg` |
| `mode_krein_inertia_m4_k4_q4_pos` | `mode_emt_m4_k4_q4_pos` | `mode_krein_inertia_m4_k4_q4_neg` |
| `mode_emt_m4_k4_q4_neg` | `growing_mode_krein_neutral` | `growing_mode_extra_time_pressure` |
| `wkb_mode_gas_conservation` | `wkb_epsilon_sign_free` | `mixture_weighted_average` |
| `unite_line_fit_proxy` | `unite_crossing_point` | `M2_tangent_exact` |
| `M3_tangent_exact` | `M4_parameters_exact` | `M4_tangent_equals_unite` |
| `M4_never_phantom` | `M5_fit_equals_unite` | `M5_crosses_minus_1` |
| `M5_without_ghost_no_crossing` |  |  |

**dirac16complex00, independent_numerics.py (B)** (28 checks):

| check | check | check |
| --- | --- | --- |
| `B_clifford_numeric` | `B_krein_matrix` | `B_krein_signed_energy` |
| `B_superposition_average` | `B_run_kmode_invariants` | `B_run_q3_invariants` |
| `B_run_q4_invariants` | `B_run_q5_invariants` | `B_run_cond_invariants` |
| `B_run_ghost_invariants` | `B_ghost_negative_energy` | `B_condensate_rho_constant` |
| `B_vs_A_M2_N2` | `B_vs_A_M2_N1` | `B_vs_A_M2_ratio` |
| `B_vs_A_M3_N2` | `B_vs_A_M3_N1` | `B_vs_A_M3_ratio` |
| `B_vs_A_M4_N2` | `B_vs_A_M4_N1` | `B_vs_A_M4_ratio` |
| `B_vs_A_M5_N2` | `B_vs_A_M5_N1` | `B_vs_A_M5_ratio` |
| `B_vs_A_M5_crossing` | `B_solve_M3_s` | `B_solve_M4` |
| `B_growth_rate` |  |  |

### 11.3 Re-verification for this document

For this document (2026-10-08) the six dark-sector scripts were re-run in the order of section 12 on a copy of the committed dark-sector folder, with the committed inputs (`Revision/kohn_sham/results`, `Revision/algebra/gammas.json`, `Revision/field_equations_a4/a4-equations.json`) and the built Revision Rust solver: 30 of 30, 5 of 5, 13 of 13, 9 of 9, 49 of 49 and 28 of 28 checks passed, and all thirteen output and report files were byte-identical to the committed files. The Kohn-Sham source-conditions checker, re-run the same way, passed 5 of 5 checks with a byte-identical report. The reports cited in this document are the committed files.

## 12. Reproduction

From the repository root, in this order. Each script exits 0 only if all its checks pass; its outputs are LF and two runs are byte-identical. The dirac16complex scripts write into their own `outputs/` and `reports/` folders, and each reads the outputs of the scripts before it; `run_ks_history.py` needs the built Rust solver (`--solver PATH` selects another binary). The dirac16complex00 scripts accept `--out DIR`, and `independent_numerics.py` reads implementation A's `eos-theory.json` for its comparison. The second unittest command and the PDF command are each one command; the backslash is the line continuation of a POSIX shell. Python needs numpy and sympy (no scipy).

```text
cargo build --release --manifest-path Revision/kohn_sham/solver/Cargo.toml
python Revision/dark_sector/dirac16complex/derive/derive_effective.py
python Revision/dark_sector/dirac16complex/compute/run_ks_history.py
python Revision/dark_sector/dirac16complex/compute/compute_eos.py
python Revision/dark_sector/dirac16complex/independent/independent_free_gas.py
python Revision/dark_sector/dirac16complex00/python/derive_eos.py
python Revision/dark_sector/dirac16complex00/python/independent_numerics.py
python -m unittest \
    Revision/dark_sector/dirac16complex00/tests/test_dark_sector_dirac16complex00.py -v
python Revision/field_equations_a4/python/check_ks_source_conditions.py
python scripts/build_provenance_pdf.py Revision/docs/DARK_SECTOR_HYPOTHESES.md \
    --developer-layout --specifications Revision/pdf-specifications.json
python -m unittest Revision/tests/test_dark_sector_hypotheses_publication.py -v
```

Expected output and run times measured for this document (2026-10-08, a development machine shared with other jobs; on an idle machine the times are shorter):

| command | last line of the output | time |
| --- | --- | --- |
| `derive_effective.py` | 30/30 checks pass | 7.8 s |
| `run_ks_history.py` | PASS - particle_number_every_state (the fifth of 5 PASS lines) | 85.1 s |
| `compute_eos.py` | 13/13 checks pass | 0.9 s |
| `independent_free_gas.py` | 9/9 checks pass | 190.4 s |
| `derive_eos.py` | derive_eos: 49/49 checks pass | 27.4 s |
| `independent_numerics.py` | independent_numerics: 28/28 checks pass | 32.5 s |
| `test_dark_sector_dirac16complex00.py` | OK (4 tests) | 44 s |
| `check_ks_source_conditions.py` | pass 5/5; wrote ... | 1.2 s |
| `build_provenance_pdf.py` | provenance_pdf=OK | 5 s |
| `test_dark_sector_hypotheses_publication.py` | OK (skipped=1); with REVISION_PDF_REBUILD=1: OK | below 1 s; 5 s |

The cargo build was not re-timed (the solver was already built). The PDF build runs the Markdown-to-LaTeX builder twice (with different hash seeds), runs pdflatex three times into each of two fresh directories, requires warning-free logs and byte-identical PDFs, and checks the PDF against its entry `dark-sector-hypotheses` in `Revision/pdf-specifications.json` (the Revision registry; the registry of the earlier stages is not touched).

## 13. What is proved, computed, assumed and not established

### 13.1 Proved (exact, by symbolic computation in the named checks)

1. The proper 7-volume element is $\cos z$, independent of $a_4$; the conservation identities $d\rho/dx_4 = -3a_4'(p_3 - p_t)$ and $dp_8/dx_8 + 3H\cot z(2p_8 - p_3 - p_t) = 0$ for diagonal sources $T(x_4, x_8)$ in the author's metric.
2. The observer identities $w_{\rm eff}(A) = w_{\rm eff}(B) = X/E$ and $w_{\rm eff}(C) = X/E - 1$ (and $w_{\rm eff}(N1) = w_3 - w_t$, $w_{\rm eff}(N2) = w_{\rm eff}(N1) - 1$), for each stated normalisation.
3. The condensate: an exact homogeneous solution of both fields with constant $\rho$, $p$ and ratio; $w_{\rm eff} = 0$ under (B) and $-1$ under (C); the ratio $-0.764$ at $\lambda S/m = -382/441$; the phantom window $(-2, -1)$; for the self-consistent linear member the factorised $\kappa(\rho + p)$ and, in Einstein gravity, the constant ratio, phantom exactly when $\kappa\rho > 0$, that is (by the record's $x_4$ constraint $\kappa\rho = -(3A^2 + 21)H^2 - \Lambda$) exactly when $\Lambda < -(21 + 3A^2)H^2$, and above $-1$ for $\Lambda = 0$; and $w_{\rm tot} = -1$.
4. The flat-limit mode laws (massive $1/3 \to 0$, massless $1/3$, $X \geq 0$ for real frequencies) and the expansion-inferred $w_{\rm exp}$, $-1$ exactly on the linear member.
5. dirac16complex00: on the three test eigenspaces, dimension 8, Krein signature (4,4) and $\rho = \omega Q$; the growing eigenspace is Krein-neutral; within the WKB model, positive-energy components of real frequency give $w_{\rm eff}(B) \geq 0$ and $w_{\rm eff}(C) \geq -1$; the exact model parameters and tangents of M2, M3 and M4.

### 13.2 Computed (numerical, with the stated tolerances and two implementations)

The Kohn-Sham gas along the prescribed history (615 states; radiation-like, $X/E$ in [0.292893, 0.328105] rising toward $1/3$), its CPL tangents and fits, the mixtures and the ratio scan; the bulk-band law (independent implementation); the M5 fit, its crossing and its ghost dependence; implementation B of dirac16complex00 (field-equation runs, agreement with A to within 0.00083082726, the growth past the turning point).

### 13.3 Assumed

1. The normalisation (A), (B) or (C) of $\rho_4$: an ASSUMPTION about the observer; every verdict is stated for each.
2. The history $a_4 = AHx_4$ as a PRESCRIBED BACKGROUND (test fields, no back-reaction); the instantaneous (adiabatic) Kohn-Sham states; $a_{4,\rm today}$.
3. The Z2 brane at $z = \pi/2$ (ASSUMED) and the filling convention of `Revision/kohn_sham/ks-theory.json`.
4. The WKB/local model of dirac16complex00 (frozen warp, adiabatic Krein charges, incoherent superposition): an APPROXIMATION, measured by implementation B.
5. The populations, fractions and condensate parameters of every model: CHOSEN, several of them to reproduce the Unite numbers.

### 13.4 Not established

1. A dark-energy or dark-matter mechanism of either field: this record establishes neither Hypothesis nor Hypothesis00, and nothing in this record establishes that either field is dark energy or dark matter.
2. Any Unite value as an output of the field equations: every match is by construction (sections 6.3 and 7).
3. That the ghost-like sector of dirac16complex00 is a physical state; that a time-varying dark-matter equation of state arises in the computed dirac16complex states; that any computed state crosses $w = -1$ without a component of negative classical energy.
4. A fit to supernova data; a self-consistent cosmological history; the open problems of section 10.
