# dark_sector/dirac16complex — the Hypothesis for dirac16complex (SPEC sections 8 and 11)

Revision code only (no-mixing rule of `Revision/SPEC.md` section 0: nothing from the old stages is used). Every number
below is an output of the scripts in this folder or of the Revision file named with it (files named in brackets).

**The corrected primordial metric of 2026-10-16 (version 2; `Revision/SPEC.md` section 1), in the author's coordinates
{x0, ..., x7}:**

    g = diag(e^{-2 a4} b4 cot^2 z, e^{2 a4} (x1, x2, x3), -1, -e^{-2 a4} b4 (sin^2 z)^{1/6} (x5, x6, x7)),   z = 6 H x0 real.

x0 = the hidden space direction, y = ln|sin z|/(6H), the fold cos z = 0 at y = 0 joins the two halves of a cell;
x1, x2, x3 = ordinary 3-space (scale factor e^{a4}, no warp); x4 = the time; **x5, x6, x7 = the three extra times,
time-like, which DEFLATE EXPONENTIALLY** (scale factor e^{-a4} b4^{1/2} (sin^2 z)^{1/12}); the hidden direction has the
scale factor e^{-a4} b4^{1/2} |cot z| and shrinks with them. **b4 is a function of x4 (never 1).** The metrics of
2026-10-14 (with sin^{1/3} z in 3-space) and its version 1 of 2026-10-16 are withdrawn; their records are in the git
history (the Wolfram verification of the withdrawn metric of 2026-10-14,
`Revision/dark_sector/wolfram/verify_dark_sector_b4.wls`, is kept and documented in
`Revision/dark_sector/B4_PROVENANCE.md`; the provenance of this record for the corrected metric, with a complete re-run, is
`Revision/dark_sector/CORRECTED_METRIC_PROVENANCE.md`). The 3-space observer's scale factor is a = e^{a4} (normalised a = 1 at a
chosen "today" a4_today; a = e^{a4 - a4_today}); b4 does not enter it.

**The history of the numbers.** a4 = H x4 and **b4(x4) = e^{(4/3) H x4}** (b4(0) = 1), beta = d ln b4/d a4 = 4/3: the
extra-time scale factor is e^{-a4} b4^{1/2} ~ a^{-1/3}, the extra times deflate exponentially. In the corrected metric
the field equations admit no off-diagonal source and require p0 = p_t; with the author's Lovelock weights this history
needs an ANISOTROPIC source that grows with x4 (`Revision/field_equations_a4/a4-equations.json`,
exponentialHistory.authorWeights; check `record_history_needs_a_source`), which no source of this record supplies: the
history is PRESCRIBED (test fields without back-reaction).

**Hypothesis (to be investigated, not assumed):** dirac16complex provides a possible physical mechanism for a
time-varying dark-energy and/or dark-matter equation of state.

## Files

| file | role |
| --- | --- |
| `derive/derive_effective.py` | sympy: every effective formula derived exactly for the corrected metric before any number is computed → `outputs/effective-formulas.json`, `reports/derivation-checks.json` (37 checks) |
| `compute/run_ks_history.py` | the Kohn-Sham gas on the history: the Revision Rust solver (`Revision/kohn_sham/solver`, command `single`, read-only use) at a4 = 0, 0.05, ..., 2 for N = 8, 592, 2352 and the five couplings lambda_hat = 0, ±lambda_1, ±lambda_2 (lambda_1, lambda_2 calibrated in `Revision/kohn_sham/results/parameters.json`), each with the cell volume Vol_7(a4) = ell^3 v_t e^{(5/3) a4} and the hidden scale f = e^{-a4/3} of the record (615 states; equivalently the coordinate cell at lambda_eff = lambda_hat e^{-(5/3) a4}, solved too at the committed slices as a check) → `outputs/ks-history-dense.csv`, `reports/ks-history-run.json` (8 checks) |
| `compute/compute_eos.py` | w_eff for the three normalisations, the ratios, CPL tangents and fits, the condensate, mixtures, the Unite comparison → `outputs/eos-history.csv`, `outputs/eos-summary.json`, `reports/eos-checks.json` (13 checks) |
| `independent/independent_free_gas.py` | INDEPENDENT second implementation (numpy, Chebyshev collocation + Hellmann-Feynman, no solver output used except for the final comparison) of the key numbers of the free gas; the bulk (massive) band → `outputs/independent-free-gas.json`, `reports/independent-checks.json` (10 checks) |
| `../wolfram/verify_dark_sector.wls` | the independent Wolfram twin for the corrected metric (D1 volume, D2 conservation, D3 general w_eff, D4 condensate with the author's T16, D5 kinetic gas, D6 the anisotropic history source, D7 condensate drift) → `../reports/wolfram-dark-sector.json` (7 checks; gate step dark-wolfram) |

Run from the repository root, in this order (each exits 0 only if all its checks pass; outputs are LF and two runs
are byte-identical):

```text
python Revision/dark_sector/dirac16complex/derive/derive_effective.py        # ~4 s
python Revision/dark_sector/dirac16complex/compute/run_ks_history.py --jobs 22 --work <scratch> --part 1/3   # and 2/3, 3/3
python Revision/dark_sector/dirac16complex/compute/run_ks_history.py --jobs 22 --work <scratch>              # the assembly
python Revision/dark_sector/dirac16complex/compute/compute_eos.py            # ~1 s
python Revision/dark_sector/dirac16complex/independent/independent_free_gas.py   # ~85 s
```

The dense history runs in three parts of about 22 s and an assembly of 0.7 s (2026-10-17, 22 workers; one invocation
without `--part` computes everything at once). The Rust solver binary is built with
`cargo build --release --manifest-path Revision/kohn_sham/solver/Cargo.toml` (`run_ks_history.py --solver PATH`
selects another binary). Python needs numpy and sympy (no scipy).

## Exact results (derive_effective.py, 37/37)

* Volumes: sqrt|g| = e^{-a4} b4^2 |cot z| |sin z|^{1/2}; proper 3-volume e^{3 a4}, proper extra-time volume
  e^{-3 a4} b4^{3/2} |sin z|^{1/2}, proper hidden length e^{-a4} b4^{1/2} |cot z| dx0 = f |dy| with f = e^{-a4} b4^{1/2};
  the proper 7-volume of a cell grows like e^{-a4} b4^2 = e^{(2 beta - 1) a4} (check `proper_volume_elements`).
* Conservation, re-derived from the metric for T = diag(p0, p3, p3, p3, -rho, p_t, p_t, p_t)(x4, x0) and equal to
  `Revision/field_equations_a4/a4-equations.json`: **d rho/d x4 = -3 a4' (rho + p3) - h4 (rho + p0) - 3 h4 (rho + p_t)**,
  h4 = b4'/(2 b4) - a4' (the expansion rate of the hidden direction and of each extra time); **d p0/d x0 + 3 H cot z
  (p0 - p_t) = 0** ⇔ p0_y + 3 H (p0 - p_t) = 0. Integrated: **dE/da4 = -3 P3 - (beta/2 - 1)(P0 + 3 Pt)**, at beta = 4/3
  dE/da4 = -3 P3 + Pt + P0/3, with E, P3, Pt, P0 the proper 7-volume integrals of rho, p3, p_t, p0 per unit coordinate
  volume.
* **rho_4 is an ASSUMPTION about the observer** (the extra times are time-like): (A) the extra times and the hidden
  direction are compact with a fixed coordinate period, i.e. the extra times are closed time-like directions and the
  hidden direction x0 a closed space-like one; (B) rho_4 is taken per unit of their coordinate volume; (C) rho_4 is
  taken per unit proper 7-volume. With w_eff = -1 - (1/3) d ln rho_4/d ln a:

  **w_eff = P3/E + (beta/2 - 1)(P0 + 3 Pt)/(3E) - s (4 - 2 beta)/3: w_eff(A) = w_eff(B) (s = 0), w_eff(C) (s = 1)**.

  On the history (beta = 4/3): w_eff(A) = P3/E - (P0 + 3 Pt)/(9E) and w_eff(C) = w_eff(A) - 4/9.
* Condensate (exact homogeneous solution for every a4, b4): **S = S0 e^{a4} b4^{-2}** (S Vol_7 constant),
  rho = m S + lambda S^2/2, p3 = p_t = p0 = lambda S^2/2; w_c = lambda S/(2 m + lambda S); w_eff(A) = w_eff(B) =
  ((2 beta - 1)/3) w_c = (5/9) w_c, w_eff(C) = (5/9) w_c - 4/9; the ratio drifts, lambda S falls like e^{(1 - 2 beta) a4}
  = e^{-(5/3) a4}. The ratio equals the Unite constant-w value -0.764 at lambda S/m = -382/441 at one instant
  (`condensate_ratio_equal_unite_constant_w`); it is the 8-dimensional ratio, not the observer's dilution-inferred w.
* The fold band of the Kohn-Sham record, eps = e^{-a4} |k| exactly, is a massless 3-space quantum: w_eff(A) = 1/3 for
  every b4, w_eff(C) = 1/3 - 4/9 = -1/9 (check `fold_band_quantum_w_eff`). Free mode in the flat (warp-free) limit
  (labelled; used for signs and limits only): a mode with l = q = 0 (no hidden and no extra-time momentum) does not
  feel b4, w_eff(A) = k^2/(3 (M^2 a^2 + k^2)): 1/3 → 0 (CPL tangent w0 = x/(3(1+x)), wa = 2x/(3(1+x)^2) > 0,
  x = k^2/M^2); the momenta along the deflating extra times and the hidden direction BLUESHIFT,
  d ln q_p/d a4 = 1 - beta/2 (q_p ~ a^{1/3} on the history).
* Phantom: w_eff(C) < -1 needs P3/E - (P0 + 3 Pt)/(9E) < -5/9 at beta = 4/3; a real-frequency kinetic gas has P3 >= 0,
  Pt <= 0, P0 >= 0, so with E > 0 it needs a large hidden kinetic pressure P0 > 9 E (P3/E + 5/9), or E < 0
  (check `phantom_condition`).
* Expansion-inferred w of an observer who reads a(t) = e^{a4(x4)} with 4-dimensional Friedmann equations:
  w_exp = -1 - (2/3) a4''/a4'^2. **On the history a4 = H x4 the observer's w_exp = -1 exactly, for every b4(x4).**
* Mixtures: w_eff is linear in (P3, Pt, P0) at fixed E. The fold-band gas plus a lambda = 0 condensate (E = m S0,
  constant for every a4, b4): under A w = (1/3) r/(1 + r), r = r0/a; w_eff(C) = -0.861 at a = 1 needs beta in
  (417/2000, 1417/2000], not the history's beta = 4/3, where this mixture lies in [-4/9, -1/9)
  (check `mixture_C_matching_w0_unite`).

## The Kohn-Sham gas on the history

In the corrected metric the good-sector state is Psi = e^{ik.x} e^{-(3/2)Hy} e^{a4/2} b4^{-1} chi, and chi solves the slice
Hamiltonian h_j = j[-(i/f) sigma1 d_y + M_eff sigma2 + kappa k sigma3] + v_v with f = e^{-a4} b4^{1/2} and the constant
kappa = e^{-a4} (`Revision/kohn_sham/ks-theory.json`); the Kohn-Sham record works with **lambda_hat = lambda b4(0)^{-2}**
(the calibrated couplings of `Revision/kohn_sham/results/parameters.json`: 157.7, 2.131, 0.5363 and 473.1, 6.393, 1.609
for N = 8, 592, 2352) and the cell volume Vol_7(a4) = ell^3 v_t e^{(5/3) a4}, so the effective coupling lambda_hat/Vol_7
falls like e^{-(5/3) a4}. Equivalently (a state depends on the coupling and the cell only through lambda/Vol) the state is
that of the coordinate cell ell^3 v_t at **lambda_eff = lambda_hat e^{-(5/3) a4}** with the same f and kappa. The same N,
T = 0, canonical numerics, H = m = 1, L = 3, tip theta = 0 are solved at 41 slices a4 in [0, 2]
[`reports/ks-history-run.json`, 8/8]: at the five committed slices all 15 series equal the committed Kohn-Sham record
(deviation 0, `committed_slices_equal_committed_record`); every run used Vol_7 = ell^3 v_t e^{(5/3) a4}
(`cell_volume_follows_b4`); the coordinate-cell form at lambda_eff gives the same E_KS, E, P3, Pt, P0 to 8.159e-13 in the
48 interacting states at the committed slices a4 > 0 (`lambda_eff_form_agrees`); the occupied label set is the same at
all 41 slices of every series; y-conservation holds to 5.751e-10.

* **The free gas is an exact fold-band gas** [`reports/ks-history-run.json`, `lambda0_series_exact_fold_band`;
  `reports/eos-checks.json`, `free_gas_exact_fold_band`]: every occupied orbital is the fold-band orbital
  (e^{f M y}, 0) with eps = e^{-a4} |k| or a k = 0 zero mode, so for N = 592 and 2352 at lambda = 0, P3/E = 1/3 and
  Pt/E = P0/E = 0 to 7.8e-16 and E e^{a4} is constant to 3.1e-15: **w_eff(A) = 1/3 exactly (radiation-like),
  w_eff(C) = -1/9, wa = 0**. N = 8 at lambda = 0 has E = 0 (the zero modes): no equation of state.
* **Conservation** [`reports/eos-checks.json`, 13/13]: dE/da4 = -3 P3 + Pt + P0/3 holds to 2.103e-06 of max|E|
  (4th-order differences on the dense grid) and to 2.208e-07 integrated (Simpson); d w_eff(A)/da4 two ways to 1.410e-06.
* **The interacting gas** (N = 592, 2352, lambda != 0; 8 series): E > 0 at every slice; w_eff(A) in [0.330585, 0.336132],
  w_eff(C) in [-0.113860, -0.108312]; Pt/E in [-3.240e-02, 3.024e-02], P0/E in [-1.192e-01, 1.114e-01] (the hidden and
  extra-time pressures that a 3-space observer does not see as pressure). CPL over all gas series: tangent wa in
  [-0.003892, 0.003904], fitted wa in [-0.002392, 0.002261] (check `gas_cpl_far_from_unite`).
* **N = 8 with lambda != 0** (only the k = 0 zero modes, pure interaction energy): E has the sign of -lambda at every
  slice; P3 = Pt, P3/E in [0.948351, 0.998955]; w_eff(A) in [0.232167, 0.408203] (check `n8_interacting_states`).
* **Expected time-varying dark-matter equation of state (1/3 → 0): not found.** The computed ground states fill the
  fold band (radiation-like, w_eff(A) = 1/3). The massive BULK band (the lowest odd level of the n2 = 1 shell,
  |k| = 0.25, eps = 1.316253 at a4 = 0; the bulk edge, the lowest odd k = 0 level, is 1.292292828069 at a4 = 0) does
  not follow the dust-like law either: the shrinking hidden direction raises the bulk level like 1/f = e^{a4/3}, so
  w_eff(A) = -(1/3) d ln eps/d a4 falls monotonically from 0.318721 (a4 = -3) to -0.081074 (a4 = 4), changing sign
  between a4 = -0.5 and -0.25, toward -1/9 when the hidden momentum dominates [`outputs/independent-free-gas.json`,
  bulkBand_n2_1; `reports/independent-checks.json`, check `bulk_band_w_eff`]. No T = 0 state of the record (N = 8,
  592, 2352) occupies an odd-parity (bulk) level (the committed level files
  `Revision/kohn_sham/results/ground/levels/*.csv`; the occupied label set, parity included, is fixed along the
  history, check `occupied_labels_fixed_along_history`, 15 of 15 series); the interacting levels are shifted
  (N = 2352, lambda_hat = -1.609: Fermi level 1.301468 at a4 = 0, above the free edge 1.292293 but below that state's
  lowest odd level 1.401451).
* Independent check [`reports/independent-checks.json`, 10/10]: energies of the independent collocation vs the Rust
  solver 3.568e-13 (82 states), w_eff 1.220e-13, CPL tangents 2.737e-11; the fold-band level e^{-a4}|k| to 4.58e-14.

## The condensate, mixtures and the Unite comparison

* **The condensate drifts** (lambda S/m ~ e^{-(5/3) a4}): at the u that gives the ratio -0.764 today its wa is -2.24616
  (thawing sign); w_eff(A) = (5/9) w_c = -0.424444 and w_eff(C) = (5/9) w_c - 4/9 = -0.868889, both with
  wa = -1.247867 (check `condensate_drifts`). For -2 < u_today < 0 the condensate energy E = m S0 (1 + u/2)
  (u = lambda S/m ~ e^{-(5/3) a4}) reaches 0 in the past, at a4 = a4_today - (3/5) ln(2/|u_today|) (it follows from
  checks `condensate_rho_p` and `condensate_scaling`); for u_today <= -2 it is already <= 0 today.
* Gas (N = 2352, lambda = 0) + lambda = 0 condensate: w_eff(C) >= -0.444111 >= -4/9 at every slice and gas fraction:
  neither -0.861 nor a constant -0.764 is reached (check `mixture_C_cannot_reach_unite_w0_with_lambda0_condensate`).
* Gas + a drifting condensate of any ratio w_c in [-3, 0.99] today, any gas fraction, a4_today in {0.5, 1, 1.5, 2}: the
  closest points to the Unite pair (-0.861, -0.60) are, ratio definition: (-0.35, -0.7875), distance 0.5443; A, B:
  (-0.3, -0.77), distance 0.5862; C: (-0.7056, -0.6397), distance 0.1604 (the pure condensate with w_c = -0.47 today at
  a4_today = 0.5, CHOSEN). Every mixture with |w0 + 0.861| <= 0.1 has wa between -1.780 and -0.829 (C), -3.136 and
  -2.159 (ratio), -4.448 and -3.006 (A, B) [`outputs/eos-summary.json`, mixture_scan].
* **Verdict on the Hypothesis for dirac16complex on the corrected metric (labelled INTERPRETATION of the computed
  numbers):**
  (i) no time-varying DARK-MATTER-like equation of state (w_eff(A) falling from 1/3 toward 0) is found: the computed
  gas is an exact fold-band gas with w_eff(A) = 1/3, and the massive bulk band, blueshifted by the shrinking hidden
  direction, falls through 0 to negative values;
  (ii) the gas is NOT dark-energy-like under any normalisation: w_eff(C) = -1/9 (free) or between -0.1139 and -0.1083
  (interacting), w_eff(A) near 1/3; only the drifting condensate gives values near the Unite w0 (w_eff(C) = -0.869 at
  the ratio -0.764, with wa = -1.25), and the closest CHOSEN pure condensate to the Unite pair lies at the distance 0.160
  ((-0.706, -0.640)): a tuned value, not a prediction;
  (iii) no computed Kohn-Sham state has w_eff(C) < -1; a drifting lambda < 0 condensate has w_eff(C) < -1 while
  u = lambda S/m lies in (-2, -1) (`Revision/dark_sector/dirac16complex00/reports/python-derive-eos.json`, check
  `condensate_phantom_interval`);
  (iv) on the prescribed history the observer's expansion itself reads w_exp = -1 exactly.

## Status and limits (honesty rule)

* The history a4 = H x4, b4 = e^{(4/3) H x4} is a PRESCRIBED BACKGROUND (test fields without back-reaction): with the
  author's weights it needs the anisotropic source of `a4-equations.json` (kappa (p3 - p0) = -9 kk^2/16 +
  1069 kk/432 + 2015/972, kk = e^{(2/3) H x4}; `Revision/dark_sector/dirac16complex00/eos-theory.json`, check
  `history_required_source` of `reports/python-derive-eos.json` there); no source of this record supplies it: the
  Kohn-Sham states are not admissible sources (`Revision/field_equations_a4/reports/ks-source-conditions.json`) and
  every condensate is isotropic and decays.
* Both fold conditions are filled (ASSUMED); the filling of the positive branch and the zero modes is the CONVENTION of
  `Revision/kohn_sham/ks-theory.json`; the normalisation A, B or C of rho_4 is an ASSUMPTION about the observer;
  a4_today is a free parameter; b4(0) enters only through lambda_hat; only T = 0 states are used, and the Kohn-Sham
  states only at a4 in [0, 2] (the solver's validated range); the single-level bulk-band study of
  `independent_free_gas.py` (independent collocation, not the solver) runs over a4 in [-3, 4].
* OPEN: a self-consistent history with an admissible source; populated bulk-band or thermal states along the
  history (fixed entropy); modes with extra-time momentum (outside the good sector; only their flat-limit sign
  structure is derived here); the non-adiabatic problem.
