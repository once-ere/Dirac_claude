# dark_sector/dirac16complex — the Hypothesis for dirac16complex (SPEC sections 8 and 11)

Revision code only (no-mixing rule of `Revision/SPEC.md` section 0: nothing from the old stages is used). Every number
below is an output of the scripts in this folder (files named in brackets).

**The author's coordinates and metric** (`Dirac_Einstein-Lovelock_4+4_Nash.nb`, In[48]: `X = {x0[], ..., x7[]}`;
In[97]-In[102]):

    g = diag(cot^2 z, e^{2 a4} sin^{1/3} z (x1, x2, x3), -1, -e^{-2 a4} b4 sin^{1/3} z (x5, x6, x7)),   z = 6 H x0.

x0 = the hidden space direction, z in (0, pi/2), y = ln(sin z)/(6H); x1, x2, x3 = ordinary 3-space (scale factor
e^{a4} sin^{1/6} z); x4 = the time; **x5, x6, x7 = the three extra times, time-like, which DEFLATE EXPONENTIALLY**
(scale factor e^{-a4} b4^{1/2} sin^{1/6} z). **b4 is a function of x4 (never 1).** The record before 2026-10-14 used
b4 = 1; it is withdrawn, and its numbers are quoted below only as "withdrawn" for comparison. The 3-space observer's
scale factor is a = e^{a4} (normalised a = 1 at a chosen "today" a4_today; a = e^{a4 - a4_today}); b4 does not enter it.

**The history of the numbers.** a4 = H x4 (A = 1, the author's solution) and **b4(x4) = b4(0) e^{(4/3) H x4}**, i.e.
beta = d ln b4/d a4 = 4/3 (b4 ~ a^{4/3}). With the author's weights (w1 = 1, w2 = 1/32, w3 = 1/1152) the mixed (x4, x0)
field equation of a source without a T^x4_x0 component is beta_v Q(alpha, beta_v) = 0
(`Revision/metric_b4/results/vacuum-b4.json`); on a4 = H x4 it allows a constant b4 or exactly d ln b4/d a4 = 4/3
(check `author_weights_b4_branch`). The extra-time scale factor is then e^{-a4} b4^{1/2} ~ a^{-1/3}: the extra times
still deflate exponentially. In Einstein gravity a b4(x4) needs T^x4_x0 = (3/2) H cot z b4'/(kappa b4) != 0, which no
source of this record has (check `einstein_mixed_component_b4`). The history is PRESCRIBED (test fields).

**Hypothesis (to be investigated, not assumed):** dirac16complex provides a possible physical mechanism for a
time-varying dark-energy and/or dark-matter equation of state.

## Files

| file | role |
| --- | --- |
| `derive/derive_effective.py` | sympy: every effective formula derived exactly for the metric with b4(x4) before any number is computed → `outputs/effective-formulas.json`, `reports/derivation-checks.json` (39 checks) |
| `compute/run_ks_history.py` | the Kohn-Sham gas on the history with b4(x4): the Revision Rust solver (`Revision/kohn_sham/solver`, command `single`, read-only use) at a4 = 0, 0.05, ..., 2 for N = 8, 136, 688 and the five calibrated couplings, each at lambda_eff = lambda_hat e^{-2 a4} (615 states) → `outputs/ks-history-dense.csv`, `reports/ks-history-run.json` (7 checks) |
| `compute/compute_eos.py` | w_eff for the three normalisations with the b4 terms, the ratios, CPL tangents and fits, the condensate, mixtures, the Unite comparison → `outputs/eos-history.csv`, `outputs/eos-summary.json`, `reports/eos-checks.json` (15 checks) |
| `independent/independent_free_gas.py` | INDEPENDENT second implementation (numpy, Chebyshev collocation + Hellmann-Feynman, no solver output used except for the final comparison) of the key numbers of the free gas; the bulk (massive) band → `outputs/independent-free-gas.json`, `reports/independent-checks.json` (10 checks) |

Run from the repository root, in this order (each exits 0 only if all its checks pass; outputs are LF and two runs
are byte-identical):

```text
python Revision/dark_sector/dirac16complex/derive/derive_effective.py        # ~4 s
python Revision/dark_sector/dirac16complex/compute/run_ks_history.py         # ~25 s (needs the built Rust solver)
python Revision/dark_sector/dirac16complex/compute/compute_eos.py            # ~1 s
python Revision/dark_sector/dirac16complex/independent/independent_free_gas.py   # ~1.3 min
```

The Rust solver binary is built with `cargo build --release --manifest-path Revision/kohn_sham/solver/Cargo.toml`
(`run_ks_history.py --solver PATH` selects another binary). Python needs numpy and sympy (no scipy).

## Exact results (derive_effective.py, 39/39)

* Volumes: sqrt|g| = b4^{3/2} cos z; the proper 7-volume element of a slice is b4^{3/2} cos z (no a4: the 3-space
  inflation e^{3 a4} is compensated by e^{-3 a4}; it changes with x4 through b4). Proper extra-time volume
  e^{-3 a4} b4^{3/2}.
* Conservation, re-derived from the metric (own Christoffel symbols) for T = diag(p0, p3, p3, p3, -rho, p_t, p_t,
  p_t)(x4, x0) and equal to `Revision/field_equations_a4/a4-equations.json` (key b4) at T^x4_x0 = 0:
  **d rho/d x4 = -3 a4' (p3 - p_t) - (3/2)(b4'/b4)(rho + p_t)**; **d p0/d x0 + 3 H cot z (2 p0 - p3 - p_t) = 0**
  (no b4) ⇔ p0_y + 6 H p0 = 3 H (p3 + p_t). Integrated: **dE/da4 = -3 (P3 - Pt) - (3/2) beta Pt**, with E, P3, Pt the
  proper 7-volume integrals of rho, p3, p_t per unit coordinate volume.
* **rho_4 is an ASSUMPTION about the observer** (the extra times are time-like): (A) the extra times are compact
  with a fixed coordinate period, i.e. closed time-like directions; (B) they are non-compact and rho_4 is taken per
  unit extra-time coordinate volume; (C) rho_4 is taken per unit proper 7-volume (equivalently per unit proper
  extra-time volume e^{-3 a4} b4^{3/2}). With w_eff = -1 - (1/3) d ln rho_4/d ln a and X = P3 - Pt:

  **w_eff = X/E - s + (beta/2)(Pt/E + s): w_eff(A) = w_eff(B) = X/E + (beta/2) Pt/E, w_eff(C) = X/E - 1 + (beta/2)(Pt/E + 1)**.

  On the history (beta = 4/3): w_eff(C) = w_eff(A) - 1/3. The whole difference to the withdrawn b4 = 1 formulas
  (X/E and X/E - 1) is the beta term.
* Condensate (exact homogeneous solution for every b4): **b4^{3/2} S is constant**, rho = m S + lambda S^2/2,
  p3 = p_t = p0 = lambda S^2/2. X = 0, Pt/E = w_c = lambda S/(2 m + lambda S): w_eff(A) = w_eff(B) = (beta/2) w_c,
  w_eff(C) = -1 + (beta/2)(1 + w_c), and the ratio drifts, d w_c/d a4 = -3 beta m lambda S/(2 m + lambda S)^2 (on the
  history lambda S/m ~ e^{-2 a4}). The ratio equals the Unite constant-w value -0.764 at lambda S/m = -382/441 at one
  instant (rho = m S (1 + u/2) > 0 iff m S > 0); it is the 8-dimensional ratio, not the observer's dilution-inferred w,
  which is -1/3 + (2/3) w_c under C: below -1 exactly while the drifting ratio is below -1 (u in (-2, -1)), for
  u = -382/441 today from a = 0.9307 back to a = 0.6581, where E_c reaches 0.
* Free mode in the flat (warp-free) limit (labelled; used for signs and limits only): omega^2 = M^2 + k^2 e^{-2a4}
  - q^2 e^{2a4}/b4 (k: 3-momentum, q: extra-time momentum; physical q_p = q e^{a4} b4^{-1/2} ~ a^{1 - beta/2}); the
  kinetic gas of such modes satisfies the b4 conservation identity exactly; per mode X = (k_p^2 + q_p^2)/(3 omega)
  >= 0. A q = 0 mode does not feel b4: w_eff(A) = k^2/(3 (M^2 a^2 + k^2)): 1/3 → 0 (CPL tangent w0 = x/(3(1+x)),
  wa = 2x/(3(1+x)^2) > 0, x = k^2/M^2); a massless one has X/E = 1/3.
* Phantom: w_eff(C) + 1 = X/E + (beta/2)(1 + Pt/E); with beta > 0 and Pt/E >= -1 a value below -1 needs X/E < 0,
  which needs P_t > P3 with E > 0 (no real-frequency mode supplies it) or E < 0 together with X > 0. With Pt/E < -1 it
  needs neither: a condensate (X = 0, Pt/E = w_c) reads w_eff(C) < -1 exactly while u lies in (-2, -1). Negative E is
  not specific to a negative-norm (Krein) sector in the canonical Kohn-Sham record: there the interacting N = 8,
  lambda > 0 good-sector states have E < 0, from the interaction energy of the canonical uniform-gas exchange
  functional. With the exact Fock exchange solved self-consistently (the exact-Fock variant,
  `Revision/kohn_sham/results/exx/exact-fock-variant.csv`, at the canonical slices) the same states have
  |E| <= 2.04e-13: this negative E is a property of the approximate functional (OPEN beyond it).
* Expansion-inferred w of an observer who reads a(t) = e^{a4(x4)} with 4-dimensional Friedmann equations:
  w_exp = -1 - (2/3) a4''/a4'^2; Einstein: G^x1_x1 - G^x5_x5 = 2 a4'' + 3 a4' b4'/b4 - b4''/(2 b4) - b4'^2/(4 b4^2)
  (from the metric, equal to the record), so w_exp = -1 - (kappa (p3 - p_t) - 3 a4' u + v/2 + u^2/4)/(3 a4'^2),
  u = b4'/b4, v = b4''/b4. **On the history a4 = H x4 the observer's w_exp = -1 exactly, for every b4(x4).**
* Mixtures: w_eff = sum X_i/sum E_i - s + (beta/2)(sum Pt_i/sum E_i + s). A radiation-like gas plus a lambda = 0
  condensate (E = m S0, constant for every b4): w_eff(C) = w_eff(A) - 1 + beta/2; w_eff(C) = -0.861 at a = 1 needs
  beta in (-583/1500, 139/500] — not the history's beta = 4/3.

## The Kohn-Sham gas on the history with b4(x4)

In the metric with b4 the good-sector state is Psi = b4^{-3/4} X, where X solves the b4-free good-sector equation
(`Revision/kohn_sham/reports/ks-b4-wolfram.json`, K1 and K2); the mean field lambda S has S = b4^{-3/2} X-bar X and the
solver's functional is quadratic in the densities, so X solves that equation at **lambda_eff = lambda_hat e^{-2 a4}**
(lambda_hat = lambda b4(0)^{-3/2} = the calibrated couplings of `Revision/kohn_sham/results/parameters.json`), and the
integrals E, P3, Pt, P0 are those of X (the proper volume element b4^{3/2} cos z cancels the b4^{-3/2} of the
densities). The same N, T = 0, canonical numerics, H = m = 1, L = 3, tip theta = 0 are solved at 41 slices a4 in
[0, 2] [`reports/ks-history-run.json`, 7/7]: at a4 = 0 (lambda_eff = lambda_hat) all 15 states equal the committed
Kohn-Sham record (deviation 0); the lambda = 0 series equal it at all five committed slices (no b4 dependence); the
occupied label set is the same at all 41 slices of every series; y-conservation holds to 1.95e-8.

* **Conservation with b4** [`reports/eos-checks.json`, 15/15]: dE/da4 = -3 (P3 - Pt) - 2 Pt holds to 6.4e-6 (the
  truncation error of the 4th-order stencil on the N = 8 interacting series, whose E falls like e^{-2 a4}, is about
  6.7e-6; 1.2e-7 for the gas), and to 3.6e-7 integrated (Simpson). **The b4-free identity of the withdrawn record
  fails** on the interacting series (relative deviation 1.63): the b4 term is required by the solver's own numbers.
* **The occupied levels lie on the brane band, which is massless at k = 0** (slope c e^{-a4}, c = 1.9051482536 at
  small k). The gas redshifts like radiation: d ln E/d a4 goes from -0.879 (a4 = 0) to -0.955 (a4 = 2) for N = 688,
  lambda = 0.
* w_eff(A) = w_eff(B) = X/E + (2/3) Pt/E lies in [0.2929, 0.3264] over all N = 136, 688 series and slices and **rises
  monotonically toward 1/3** (|Pt/E| <= 1.1e-4). **w_eff(C) = w_eff(A) - 1/3 lies in [-0.0404, -0.0069]: close to 0
  (dust-like), not a dark-energy value** (withdrawn b4 = 1: -0.707 → -0.682). The hidden-direction ratio
  wx0 = P0/E = 0.35 → 0.65 is a pressure the 3-space observer does not see.
* CPL tangent (N = 688, lambda = 0), a4_today = 0.5, 1, 1.5, 2: wa = -0.0090, -0.0129, -0.0170, -0.0178, with
  w0(C) = -0.0370, -0.0315, -0.0240, -0.0150 (w0(A) = w0(C) + 1/3). Least-squares CPL fits over a in [1/2, 1] and
  [1/3, 1] (a4_today = 2): wa(C) = -0.024, -0.026; constant-w fits w(C) = -0.021, -0.023. Over all N = 136, 688
  series: tangent wa in [-0.0178, -0.0090], fitted wa in [-0.0265, -0.0196] [`outputs/eos-summary.json`, check
  `gas_cpl_thawing_sign_small`].
* **N = 8 with lambda != 0** (only the k = 0 zero modes, pure interaction energy at lambda_hat e^{-2 a4}): P3 = Pt
  (X = 0), E(2)/E(0) = 0.0184-0.0190 (e^{-4} = 0.0183), Pt/E in [0.931, 1.000]: w_eff(A) = (2/3) Pt/E in
  [0.621, 0.667], w_eff(C) in [0.288, 0.333] (withdrawn b4 = 1: E constant, w_eff(A) = 0, w_eff(C) = -1). N = 8 with
  lambda = 0 has E = 0: no equation of state.
* **Expected time-varying dark-matter equation of state (1/3 → 0): not found in the computed states.** A falling
  w_eff appears for quanta of the massive BULK band (odd brane parity, eps(0) = 1.2922928281 = the bulk edge): for
  the n2 = 1 shell w_eff(A) falls monotonically from 0.2396 (a4 = -3) to 0.0023 (a4 = 4), asymptotically like 1/a
  [`outputs/independent-free-gas.json`]; these free quanta (lambda = 0, q = 0) do not feel b4, so the law is the same
  on the history with b4(x4) (check `free_gas_independent_of_b4`). The T = 0 states (N <= 688) are filled below the
  bulk edge and do not populate that band.
* Independent check [`reports/independent-checks.json`, 10/10]: energies of the independent collocation vs the Rust
  solver 1.9e-12, w_eff 1.5e-12, CPL tangents 4.0e-7.

## The condensate, mixtures and the Unite comparison

* **The condensate drifts with b4** (lambda S/m ~ e^{-2 a4}): at the u that gives the ratio -0.764 today, its wa is
  -2.695 (thawing sign); w_eff(A) = (2/3) w_c = -0.509 and w_eff(C) = -1/3 + (2/3) w_c = -0.843, both with wa = -1.797
  (check `condensate_drifts_with_b4`). For u < 0 the condensate energy m S0 (1 + u/2) reaches 0 in the past, at
  a4 = a4_today - (1/2) ln(2/|u_today|).
* Gas (N = 688, lambda = 0) + lambda = 0 condensate: w_eff(C) >= -1/3 at every slice and gas fraction: neither -0.861
  nor a constant -0.764 is reached (withdrawn b4 = 1: a gas fraction 0.4367 gave w_eff(C) = -0.861 with wa = +0.067).
* Gas + a drifting condensate of any ratio w_c in [-3, 0.99] today, any gas fraction, a4_today in {0.5, 1, 1.5, 2}:
  the closest points to the Unite pair (-0.861, -0.60) are, ratio definition: (-0.300, -0.780), distance 0.589;
  A, B: (-0.273, -0.771), distance 0.612; C: (-0.580, -0.676), distance 0.291 (the pure condensate with w_c = -0.37
  today). Among mixtures with |w0 + 0.861| <= 0.1 the slope wa is at most -2.64 (C), far below -0.60
  [`outputs/eos-summary.json`, mixture_scan].
* **Verdict on the Hypothesis for dirac16complex on the metric with b4(x4) (labelled INTERPRETATION of the computed
  numbers):**
  (i) a time-varying DARK-MATTER-like equation of state (w_eff(A) falling toward 0: 0.240 at a4 = -3 to 0.0023 at
  a4 = 4 for one shell) is present in the theory for quanta of the massive bulk band, independent of b4, not in the
  computed ground states, whose brane-band gas is radiation-like (w_eff(A) rising toward 1/3);
  (ii) with b4(x4) = b4(0) e^{(4/3) H x4} the gas is NOT dark-energy-like under any normalisation: w_eff(C) is close to
  0 (-0.040 to -0.007), w_eff(A) near 1/3; only the drifting condensate gives negative values (w_eff(C) = -0.843 at
  the ratio -0.764) and then with a strongly thawing slope (wa = -1.80); nothing computed comes near the Unite pair
  (w0, wa) = (-0.861, -0.60) (closest distance 0.291) or its phantom past (w0 + wa = -1.461);
  (iii) no computed Kohn-Sham state has w_eff(C) < -1; a drifting lambda < 0 condensate has, while u lies in (-2, -1)
  (Pt/E = w_c < -1 there; for u = -382/441 today from a = 0.9307 back to a = 0.6581);
  (iv) on the prescribed history the observer's expansion itself reads w_exp = -1 exactly.

## Status and limits (honesty rule)

* The history a4 = H x4, b4 = b4(0) e^{(4/3) H x4} is a PRESCRIBED BACKGROUND (test fields without back-reaction).
  It is allowed by the mixed equation of the author's weights for a source without T^x4_x0; the source the author's
  equations then require is constant, kappa (rho, p3, p_t, p0) = (-2/27, -2/9, -22/27, -14/27)
  (`Revision/dark_sector/dirac16complex00/eos-theory.json`, check `branch_required_source` of
  `reports/python-derive-eos.json` there); no source of this record is it: the Kohn-Sham states are not admissible
  sources (`Revision/field_equations_a4/reports/ks-source-conditions.json`) and a condensate decays like b4^{-3/2}.
* The Z2 brane is ASSUMED; the filling of the positive branch and the zero modes is the CONVENTION of
  `Revision/kohn_sham/ks-theory.json`; the normalisation A, B or C of rho_4 is an ASSUMPTION about the observer;
  a4_today is a free parameter; b4(0) enters only through lambda_hat; only T = 0 states and a4 in [0, 2] (the
  solver's validated range) are used.
* OPEN: a self-consistent history with an admissible source; populated bulk-band or thermal states along the
  history (fixed entropy); modes with extra-time momentum (outside the good sector; only their flat-limit sign
  structure is derived here); the non-adiabatic problem.
