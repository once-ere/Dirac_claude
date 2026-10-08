# dark_sector/dirac16complex — the Hypothesis for dirac16complex (SPEC sections 8 and 11)

Revision code only (no-mixing rule of `Revision/SPEC.md` section 0: nothing from the old stages is used). Every number
below is an output of the scripts in this folder (files named in brackets). Coordinates as the author names them:
x1, x2, x3 = ordinary 3-space (scale factor e^{a4} sin^{1/6} z); x4 = the time; **x5, x6, x7 = the three extra
times, time-like, which DEFLATE EXPONENTIALLY** (scale factor e^{-a4} sin^{1/6} z, a4 increasing); x8 = the hidden
space direction, z = 6 H x8 in (0, pi/2), y = ln(sin z)/(6H). The 3-space observer's scale factor is a = e^{a4}
(normalised a = 1 at a chosen "today" a4_today; a = e^{a4 - a4_today}).

**Hypothesis (to be investigated, not assumed):** dirac16complex provides a possible physical mechanism for a
time-varying dark-energy and/or dark-matter equation of state.

## Files

| file | role |
| --- | --- |
| `derive/derive_effective.py` | sympy: every effective formula derived exactly before any number is computed → `outputs/effective-formulas.json`, `reports/derivation-checks.json` (30 checks) |
| `compute/run_ks_history.py` | the Kohn-Sham gas on a dense history: the Revision Rust solver (`Revision/kohn_sham/solver`, command `single`, read-only use) at a4 = 0, 0.05, ..., 2 for N = 8, 136, 688 and the five calibrated couplings (615 states) → `outputs/ks-history-dense.csv`, `reports/ks-history-run.json` (5 checks) |
| `compute/compute_eos.py` | w_eff for the three normalisations, the ratios, CPL tangents and fits, condensate, mixtures, Unite comparison → `outputs/eos-history.csv`, `outputs/eos-summary.json`, `reports/eos-checks.json` (13 checks) |
| `independent/independent_free_gas.py` | INDEPENDENT second implementation (numpy, Chebyshev collocation + Hellmann-Feynman, no solver output used except for the final comparison) of the key numbers; the bulk (massive) band → `outputs/independent-free-gas.json`, `reports/independent-checks.json` (9 checks) |

Run from the repository root, in this order (each exits 0 only if all its checks pass; outputs are LF and two runs
are byte-identical):

```text
python Revision/dark_sector/dirac16complex/derive/derive_effective.py        # ~3 s
python Revision/dark_sector/dirac16complex/compute/run_ks_history.py         # ~2 min (needs the built Rust solver)
python Revision/dark_sector/dirac16complex/compute/compute_eos.py            # ~1 s
python Revision/dark_sector/dirac16complex/independent/independent_free_gas.py   # ~2.5 min
```

The Rust solver binary is built with `cargo build --release --manifest-path Revision/kohn_sham/solver/Cargo.toml`
(`run_ks_history.py --solver PATH` selects another binary). Python needs numpy and sympy (no scipy).

## Exact results (derive_effective.py, 30/30)

* Volumes: sqrt|g| = cos z; the proper 7-volume element of a slice x4 = const is cos z, independent of a4 (the
  3-space inflation e^{3 a4} is compensated by the extra-time deflation e^{-3 a4}).
* Conservation, re-derived from the metric (own Christoffel symbols) for T = diag(p3, p3, p3, -rho, p_t, p_t, p_t,
  p8)(x4, x8): nabla_mu T^mu_x4 = 0 ⇔ **d rho/d x4 = -3 a4' (p3 - p_t)**; nabla_mu T^mu_x8 = 0 ⇔
  **d p8/d x8 + 3 H cot z (2 p8 - p3 - p_t) = 0** ⇔ p8_y + 6 H p8 = 3 H (p3 + p_t) (the form the Kohn-Sham solver
  checks); the other components vanish identically. Integrated: dE/da4 = -3 (P3 - Pt), with E, P3, Pt the proper
  7-volume integrals of rho, p3, p_t.
* **rho_4 is an ASSUMPTION about the observer** (the extra times are time-like): (A) the extra times are compact
  with a fixed coordinate period, i.e. closed time-like directions; (B) they are non-compact and rho_4 is taken per
  unit extra-time coordinate volume; (C) rho_4 is taken per unit proper 7-volume (equivalently per unit proper
  extra-time volume). With w_eff = -1 - (1/3) d ln rho_4/d ln a and X = P3 - Pt:

  **w_eff(A) = w_eff(B) = X/E,   w_eff(C) = X/E - 1**   (exactly; general normaliser: X/E - s, s = 0 or 1).

  The verdict depends on the choice by exactly -1: the same state is "dust/radiation-like" under A and B and
  "cosmological-constant-like" under C.
* Condensate (the exact homogeneous solution): rho = m S + lambda S^2/2, p3 = p_t = p8 = lambda S^2/2, S constant:
  X = 0, so w_eff(A) = w_eff(B) = 0 and w_eff(C) = -1, ratio w = lambda S/(2 m + lambda S); all constant (wa = 0).
  The ratio equals the Unite constant-w value -0.764 at lambda S/m = -382/441 (rho = m S (1 + u/2) > 0 iff m S > 0),
  but it is the 8-dimensional ratio, not the observer's dilution-inferred w.
* Free mode in the flat (warp-free) limit (labelled; used for signs and limits only): omega^2 = M^2 + k^2 e^{-2a4}
  - q^2 e^{2a4} (k: 3-momentum, q: extra-time momentum); per mode X = (k^2 e^{-2a4} + q^2 e^{2a4})/(3 omega) >= 0
  (p3 >= 0, p_t <= 0). A massive mode has w_eff(A) = k^2/(3 (M^2 a^2 + k^2)): 1/3 → 0 (CPL tangent
  w0 = x/(3(1+x)), wa = 2x/(3(1+x)^2) > 0, x = k^2/M^2); a massless one has X/E = 1/3.
* Phantom: w_eff(C) < -1 (or w_eff(A) < 0) iff X/E < 0, which needs P_t > P3 with E > 0 (no real-frequency mode
  supplies it) or E < 0 (negative-norm, Krein sector).
* Expansion-inferred w of an observer who reads a(t) = e^{a4(x4)} with 4-dimensional Friedmann equations:
  w_exp = -1 - (2/3) a4''/a4'^2; Einstein case -1 - kappa (p3 - p_t)/(3 a4'^2); **on the linear history
  a4 = A H x4 (the history of the Kohn-Sham record and the only one the condensate allows) w_exp = -1 exactly.**

## The Kohn-Sham gas (instantaneous states along the prescribed history)

Inputs: the same states as `Revision/kohn_sham/results` (H = m = 1, L = 3, tip theta = 0, T = 0, N = 8, 136, 688,
lambda = 0, ±lambda_1, ±lambda_2 per N), solved at 41 slices a4 in [0, 2]. The 75 committed states are reproduced
bit for bit; the occupied label set is the same at all 41 slices of every series (the instantaneous ground states
are the adiabatically continued states); y-conservation holds to 2.0e-8; dE/da4 = -3 (P3 - Pt) holds to 1.2e-7
(4th-order differences) and 1.9e-8 (Simpson) [`reports/ks-history-run.json`, `reports/eos-checks.json`].

* **The occupied levels lie on the brane band, which is massless at k = 0** (the brane zero mode at eps = 0, slope
  c e^{-a4} with c = 1.9051482536 at small k). The gas therefore redshifts like radiation, not like dust: d ln E/d a4
  goes from -0.879 (a4 = 0) to -0.955 (a4 = 2) for N = 688, lambda = 0.
* X/E lies in [0.2929, 0.3281] over all N = 136, 688 series and slices and **rises monotonically toward 1/3** (the
  band becomes linear as the 3-momenta redshift): w_eff(A) = w_eff(B) = 0.2929 → 0.3183 (N = 688, lambda = 0),
  w_eff(C) = -0.7071 → -0.6817. The ratio w3 = P3/E equals X/E up to |Pt/E| <= 0.002 (Pt = int e_int; 0 at
  lambda = 0). The hidden-direction ratio w8 = P8/E = 0.35 → 0.65 is a pressure the 3-space observer does not see.
* CPL tangent (N = 688, lambda = 0), a4_today = 0.5, 1, 1.5, 2: wa = -0.0090, -0.0129, -0.0170, -0.0178, with
  w0(C) = -0.704, -0.698, -0.691, -0.682 (w0(A) = w0(C) + 1). Least-squares CPL fits over a in [1/2, 1] and
  [1/3, 1] (a4_today = 2): wa = -0.024, -0.026; constant-w fits w(C) = -0.687, -0.690. Over all N = 136, 688
  series: tangent wa in [-0.0205, -0.0089], fitted wa in [-0.0304, -0.0181], w_eff(C) in [-0.7071, -0.6719]
  [`outputs/eos-summary.json`, check `gas_cpl_thawing_sign_small`].
* **Expected time-varying dark-matter equation of state (1/3 → 0): not found in the recorded states.** A falling
  w_eff appears for quanta of the massive BULK band (odd brane parity, eps(0) = 1.2922928281 = the bulk edge): for
  the n2 = 1 shell w_eff(A) falls monotonically from 0.2396 (a4 = -3) to 0.0023 (a4 = 4), asymptotically like 1/a (a linear term of
  eps(k) at small k) [`outputs/independent-free-gas.json`]. The canonical T = 0 states (N <= 688) are filled below
  the bulk edge and do not populate that band; a gas of bulk-band quanta would show the dark-matter-like law.
* N = 8 with lambda != 0 (only the k = 0 zero modes): E constant, P3 = Pt: w_eff(A) = 0, w_eff(C) = -1, constant
  (E < 0 for lambda > 0). N = 8 with lambda = 0 has E = 0: no equation of state.

## Mixtures (gas N = 688, lambda = 0, plus a condensate) and the Unite comparison

* In every definition the mixture's w moves toward the condensate's value as the gas redshifts: wa > 0 (freezing).
  Normalisation C: w_eff(C) = -0.861 today (a4_today = 2) needs a gas fraction 0.4367 and then has wa = +0.067
  (Unite: -0.60). A constant-w fit over a in [1/3, 1] equal to -0.764 needs a gas fraction 0.6807; its CPL fit is
  (w0, wa) = (-0.784, +0.060).
* Ratio definition with a condensate of any constant ratio w_c in [-3, 1], any gas fraction and a4_today in
  {0.5, 1, 1.5, 2}: among mixtures with |w0 + 0.861| <= 0.1 the smallest wa is 0 (the pure condensate); the Unite
  pair (-0.861, -0.60) is never closer than 0.60.
* **Verdict on the Hypothesis for dirac16complex (labelled INTERPRETATION of the computed numbers):**
  (i) a time-varying DARK-MATTER-like equation of state (w_eff(A) falling toward 0: 0.240 at a4 = -3 to 0.0023 at
  a4 = 4 for one shell; the flat-limit law 1/3 → 0 is exact) is present in the theory for quanta of the massive bulk
  band, not in the computed ground states, whose brane-band gas is radiation-like (w_eff(A) rising toward 1/3);
  (ii) a time-varying DARK-ENERGY-like equation of state appears only under the normalisation C, where the gas has
  w_eff(C) between -0.71 and -0.67 with a thawing-sign slope of magnitude <= 0.021 (tangent) and <= 0.031 (fits),
  far from 0.60, and mixtures with
  the condensate are freezing; nothing computed comes near the Unite thawing pair (w0, wa) = (-0.861, -0.60) or its
  phantom past (w0 + wa = -1.461); the Unite constant w = -0.764 is matched only by the constant 8-dimensional ratio
  of a condensate or by a C-normalised mixture whose CPL slope has the opposite sign;
  (iii) no computed state crosses w = -1 (X >= 0 and E > 0 for all except N = 8, lambda > 0, where X = 0 exactly);
  (iv) on the prescribed history the observer's expansion itself reads w_exp = -1 exactly.

## Status and limits (honesty rule)

* The Kohn-Sham history a4 = A H x4 is a PRESCRIBED BACKGROUND (test field without back-reaction): the Kohn-Sham
  states are not admissible sources of the a4 equations (`Revision/field_equations_a4/reports/ks-source-conditions.json`).
  The condensate is an exact solution only on the linear member.
* The Z2 brane is ASSUMED; the filling of the positive branch and the zero modes is the CONVENTION of
  `Revision/kohn_sham/ks-theory.json`; the normalisation A, B or C of rho_4 is an ASSUMPTION about the observer;
  a4_today is a free parameter; only T = 0 states and a4 in [0, 2] (the solver's validated range) are used.
* OPEN: a self-consistent (non-linear) a4 history with an admissible source; populated bulk-band or thermal states
  along the history (fixed entropy); modes with extra-time momentum (outside the good sector; only their flat-limit
  sign structure is derived here); the non-adiabatic problem.
