# Provenance of the dark-sector change to the corrected metric (version 2)

Written 2026-10-17. This file records how the dark-sector record of the Revision (Hypothesis:
`Revision/dark_sector/dirac16complex/`; Hypothesis00: `Revision/dark_sector/dirac16complex00/`; the independent Wolfram
verification `Revision/dark_sector/wolfram/verify_dark_sector.wls`) was moved from the metric of 2026-10-14 with b4(x4)
(`Revision/dark_sector/B4_PROVENANCE.md`, now the record of a withdrawn metric) to the corrected primordial metric of
2026-10-16 (version 2), and the evidence that the move was made correctly: where every formula comes from, which
independent computations confirm each critical step, the commits, the sha256 of every script and output, and a
complete re-run on 2026-10-17 that reproduced every committed output byte for byte. It is also the
execution-provenance file of `verify_dark_sector.wls`.

## 1. The order and the metric

The user's orders of 2026-10-16 (`Revision/SPEC.md` section 1, version 2; `HANDOFF.md` 0.10: "go ahead with the
recomputation using the corrected metric", phase W6): the metric is

```text
diag( E^(-2 a4[x4]) b4[x4] Cot[z]^2,            (x0, the hidden direction, space-like)
      E^(2 a4[x4])                     (x3: x1, x2, x3),
      -1                               (x4),
      -E^(-2 a4[x4]) b4[x4] (Sin[z]^2)^(1/6)  (x3: x5, x6, x7) ),     z = 6 H x0 real;
```

b4(x4) > 0 is a function of x4 (never 1); version 1 of the remedy (g44 = -Sin[z]^(1/3)) and the metric of 2026-10-14 are
withdrawn. The three extra times x5, x6, x7 deflate exponentially (scale factor e^(-a4) b4^(1/2) (sin^2 z)^(1/12)), and
the hidden direction shrinks with them (e^(-a4) b4^(1/2) |cot z|). The numerical history is kept,
a4 = H x4, b4 = e^((4/3) H x4) (beta = 4/3), a PRESCRIBED background.

## 2. The chain of the change, and what confirms each step

"A" and "B" are the two implementations of dirac16complex00 (`python/derive_eos.py`, sympy exact; and
`python/independent_numerics.py`, the 16-component field equation integrated numerically); "W" is the Wolfram
verification `verify_dark_sector.wls`, which shares no code with the Python scripts; "I" is the independent free-gas
implementation `independent/independent_free_gas.py` (Chebyshev collocation, no solver output except for the final
comparison).

| step | result (corrected metric) | computed by | confirmed independently by |
| --- | --- | --- | --- |
| volume | sqrt\|g\| = e^(-a4) b4^2 \|cot z\| \|sin z\|^(1/2); the proper 7-volume of a cell grows like e^(-a4) b4^2 = e^((2 beta - 1) a4) | `derive_effective.py`, `sqrt_det_g`, `proper_volume_elements` | W: D1_volume; A: `local_model_volume` |
| conservation | d4 rho = -3 a4' (rho + p3) - h4 (rho + p0) - 3 h4 (rho + p_t), h4 = b4'/(2 b4) - a4'; p0_y + 3 H (p0 - p_t) = 0; integrated dE/da4 = -3 P3 - (beta/2 - 1)(P0 + 3 Pt) | `derive_effective.py`, `conservation_x4_identity`, `conservation_equals_a4_record`, `integrated_identity_dE_dx4` | W: D2_conservation; A: `conservation_x4_corrected_metric`; the Kohn-Sham solvers (`emt_energy_change_dE_da4`) |
| observer | w_eff = P3/E + (beta/2 - 1)(P0 + 3 Pt)/(3E) - s (4 - 2 beta)/3; s = 0 (A, B, N1), s = 1 (C, N2): N2 = N1 - 4/9 on the history | `derive_effective.py`, `w_eff_general_normaliser` | W: D3_w_eff_general; A: `observer_N1_weff_identity`, `observer_N2_weff_identity` |
| history | the history needs an ANISOTROPIC source that grows with x4: kappa (p3 - p0) = -9 k^2/16 + 1069 k/432 + 2015/972, kappa p0 - Lambda = kappa p_t - Lambda = 79 k/16 - 497/144, k = e^((2/3) H x4) (author's weights, Lambda = -10) | A: `history_required_source` (from `Revision/field_equations_a4/a4-equations.json`) | W: D6_history_source_anisotropic; `derive_effective.py`, `record_history_needs_a_source` |
| Kohn-Sham gas | the free states are exact fold-band gases (eps = e^(-a4) \|k\|): w_eff(A) = 1/3, w_eff(C) = -1/9 | `compute_eos.py`, `free_gas_exact_fold_band` (on the dense history of `run_ks_history.py`) | I: `free_gas_w_eff_one_third`, `fold_band_radiation_law`; `derive_effective.py`, `fold_band_quantum_w_eff`; W: D5_kinetic_gas |
| condensate | S = S0 e^(a4) b4^(-2) (S Vol_7 constant); u = lambda S/m ~ e^(-(5/3) a4); the ratio drifts, wa = (10/3) u/(2 + u)^2 = -28077/12500 at u = -382/441 | A: `condensate_S_T16`, `condensate_ratio_drift_at_unite_value`; `derive_effective.py`, `condensate_scaling` | W: D4_condensate_T16, D7_condensate_drift; `compute_eos.py`, `condensate_drifts` |
| condensate as a source | isotropic (p3 = p_t = p0) and decaying, while the history needs an anisotropic growing source: no condensate is it | A: `condensate_cannot_source_history` | W: D6 (the anisotropy) |
| models | positive models w_eff(N2) >= -4/9; M2 (-2749/9000, 81037/500000), M3 (-3583/9000, -196963/4500000) exactly; the Unite w0 needs G >= 3749/3000; no crossing of -1 by M2 to M5 | A (sympy exact, mpmath 30 digits) | B: `B_positive_models_bounded`, `B_vs_A_M*`; the notebook `dark_sector_hypotheses` (exact Fractions) |
| bulk band | the massive bulk band is blueshifted by the shrinking hidden direction: w_eff(A) falls from 0.318721 (a4 = -3) through 0 to -0.081074 (a4 = 4) | I: `bulk_band_w_eff` | `derive_effective.py`, `extra_time_momentum_blueshift` (the rate 1 - beta/2) |

## 3. The commits (all pushed to https://github.com/once-ere/Dirac_claude.git, branch main)

| commit | what |
| --- | --- |
| `13f9fb9` | W5 (work in progress): the Kohn-Sham record of the corrected metric, with the dense history `run_ks_history.py` (615 states, 8 checks) |
| `6e228a8` | `derive_effective.py` (37 checks), dirac16complex00 A (48 checks) and B (32 checks), its tests and README, `verify_dark_sector.wls` (7 checks; the b4 twin reads the frozen copy `reference_2026_10_14/eos-theory-b4.json` and still passes 8/8) |
| `0aa3c29` | W5: the Kohn-Sham record regenerated after H15 (the dense history byte-identical) |
| `aff492a` | the automatic snapshot at the stop of 2026-10-17: `compute_eos.py` (13 checks), `independent_free_gas.py` (10 checks) on the regenerated dense history, the README of dirac16complex |
| `0a40e13`, `3f70915`, `a1c95cc`, `0a0be28` | the text-only corrections of a read-only audit of the W6 deliverables (READMEs, comments, check-detail texts; no check, verdict or count changed) and the b4-twin report regenerated after the correction of its D7 detail text |
| (the W6 commit) | this file, after the complete re-run of section 5 |

## 4. What changed in the results (metric of 2026-10-14 with b4(x4) against the corrected metric)

| quantity | metric of 2026-10-14 (withdrawn) | corrected metric, history beta = 4/3 |
| --- | --- | --- |
| w_eff(C) - w_eff(A) | -1 + beta/2 = -1/3 | -(4 - 2 beta)/3 = -4/9 |
| conservation | dE/da4 = -3 X - (3/2) beta Pt | dE/da4 = -3 P3 + Pt + P0/3 |
| the Kohn-Sham gas (N != 8) | brane band; over all gas series w_eff(A) in [0.2928, 0.3268], rising toward 1/3, w_eff(C) in [-0.0405, -0.0065] | free: exact fold band, w_eff(A) = 1/3 and w_eff(C) = -1/9 exactly; interacting: w_eff(A) in [0.330585, 0.336132], w_eff(C) in [-0.113860, -0.108312] |
| condensate | S ~ b4^(-3/2), u ~ e^(-2 a4); ratio wa = -84231/31250 | S ~ e^(a4) b4^(-2), u ~ e^(-(5/3) a4); ratio wa = -28077/12500 |
| condensate at the ratio -0.764, under C | -0.843, wa = -1.797 | -0.868889, wa = -1.247867 |
| gas + lambda = 0 condensate, C | w_eff(C) >= -1/3 | w_eff(C) >= -0.444111 >= -4/9 |
| closest scan point to the Unite pair | C: (-0.580, -0.676), distance 0.291 | C: (-0.7056, -0.6397), distance 0.1604 (the pure condensate with w_c = -0.47 today, CHOSEN) |
| M2 N2 tangent | (-583/3000, 81037/500000) | (-2749/9000, 81037/500000) |
| M3 N2 tangent | (-287/1000, -196963/4500000) | (-3583/9000, -196963/4500000) |
| bound of positive models (N2) | -1/3 | -4/9 |
| Unite w0 under N2 | needs G >= 1583/1000 | needs G >= 3749/3000 |
| the source of the history | constant: kappa (rho, p3, p_t, p0) = (-2/27, -2/9, -22/27, -14/27) | anisotropic and growing (section 2) |
| the bulk band | dust-like, 0.2396 → 0.0023 | blueshifted, 0.318721 → -0.081074 |
| check counts | 39, 8, 15, 10, 49, 32, Wolfram 8 | 37, 8, 13, 10, 48, 32, Wolfram 7 |

Neither hypothesis is established by either record. The parameters of M2 to M5 were CHOSEN on the withdrawn b4 = 1
record (by construction, NOT predictions) and are kept so that the effect of each metric is seen directly.

## 5. The re-run of 2026-10-17 (the evidence that the committed record is what the scripts produce)

On 2026-10-17, after the commits of section 3, every producer was run again in the working tree, in this order, each
bounded by `timeout -k 5 423` (Windows 11 Pro for Workstations, Python 3.14.5, Wolfram 15.0.1; the Rust solver built
with cargo 1.91). After each step `git status --short -- Revision/dark_sector` showed no change of a record: every
committed output was reproduced byte for byte (the dense history from a fresh work folder).

| command (repository root) | exit | time | checks | record changed |
| --- | --- | --- | --- | --- |
| `python Revision/dark_sector/dirac16complex/derive/derive_effective.py` | 0 | 2.7 s | 37/37 | no |
| `python Revision/dark_sector/dirac16complex/compute/run_ks_history.py --solver <ks_solver> --jobs 22 --work <scratch> --part 1/3` | 0 | 22.7 s | - | no |
| the same with `--part 2/3` | 0 | 22.9 s | - | no |
| the same with `--part 3/3` | 0 | 22.4 s | - | no |
| `python Revision/dark_sector/dirac16complex/compute/run_ks_history.py --solver <ks_solver> --jobs 22 --work <scratch>` (the assembly) | 0 | 0.7 s | 8/8 | no |
| `python Revision/dark_sector/dirac16complex/compute/compute_eos.py` | 0 | 0.3 s | 13/13 | no |
| `python Revision/dark_sector/dirac16complex/independent/independent_free_gas.py` | 0 | 80.0 s | 10/10 | no |
| `python Revision/dark_sector/dirac16complex00/python/derive_eos.py` | 0 | 2.0 s | 48/48 | no |
| `python Revision/dark_sector/dirac16complex00/python/independent_numerics.py` | 0 | 6.8 s | 32/32 | no |
| `python -m unittest Revision/dark_sector/dirac16complex00/tests/test_dark_sector_dirac16complex00.py` | 0 | 8.7 s | Ran 4 tests OK | no |
| `wolframscript -file Revision/dark_sector/wolfram/verify_dark_sector.wls` | 0 | 3.3 s | 7/7 | no |
| `wolframscript -file Revision/dark_sector/wolfram/verify_dark_sector_b4.wls` (the twin of the withdrawn metric) | 0 | 2.8 s | 8/8 | no |

## 6. The sha256 of every file of the record (2026-10-17)

| file | bytes | sha256 |
| --- | --- | --- |
| `Revision/dark_sector/dirac16complex/README.md` | 17472 | `3fb51b15314c0433cbbef655bc797af2e9ec978ab96bc6a56b379e90cd4b0fa7` |
| `Revision/dark_sector/dirac16complex/derive/derive_effective.py` | 38365 | `9846036f0ed16c87882810e7147585ea9cfb17760127e8a64ffbb3b6232782ce` |
| `Revision/dark_sector/dirac16complex/compute/run_ks_history.py` | 19277 | `49afb3120643be1302a4450a802affe1eeef3ee62836918f853b3231b1704bfc` |
| `Revision/dark_sector/dirac16complex/compute/compute_eos.py` | 25532 | `f61cf567245e0dca1921e310e6543fc2b266999a681d822001dcac831702bee2` |
| `Revision/dark_sector/dirac16complex/independent/independent_free_gas.py` | 21366 | `e97cda68dcb28d5254c3471b1d62f725062c7b2c5638db147934a308771f8951` |
| `Revision/dark_sector/dirac16complex/outputs/effective-formulas.json` | 5797 | `07c00451e84fd0642be3092d1ac734ffbe6f8ee55f0b0a5a0b19253283024ebe` |
| `Revision/dark_sector/dirac16complex/outputs/ks-history-dense.csv` | 190473 | `658454be04dead5ef1c2037327fe9d80f4882a72457571d7325379ff4d44ff9b` |
| `Revision/dark_sector/dirac16complex/outputs/eos-history.csv` | 174977 | `77639409ba6846da06fa5e648d8fdaee3471cb04b17d936ab42d5aa2d294d5e4` |
| `Revision/dark_sector/dirac16complex/outputs/eos-summary.json` | 57664 | `c6a56e2f76331d6bbd5171e9069efcf24d827670bb9a1b152fb554cea79d07a7` |
| `Revision/dark_sector/dirac16complex/outputs/independent-free-gas.json` | 22248 | `2061cc4b337f8a4c1a9557caf76ff56c1e43416062297e72d5458ad5437bf3f9` |
| `Revision/dark_sector/dirac16complex/reports/derivation-checks.json` | 11090 | `89fe8cdffcf01c2edad22f313d0130e5195e92a0d7c1e84fbb410476a6cbc9cd` |
| `Revision/dark_sector/dirac16complex/reports/ks-history-run.json` | 3575 | `50c671fa0b5a681661685eae46b5ab73b565bcb02f6d6b470e6c6470aa6fb70f` |
| `Revision/dark_sector/dirac16complex/reports/eos-checks.json` | 3991 | `443f48736bbe7901430b59f3deeff38efdc7687eb7b7d18c3f92b441f6293cd3` |
| `Revision/dark_sector/dirac16complex/reports/independent-checks.json` | 3043 | `226d0457e9944183fecea1971aef5a4ed12b3f0d6eb8ab1b020c56fa79289a7e` |
| `Revision/dark_sector/dirac16complex00/README.md` | 14756 | `f2d20e4c01c4ccac28f738cc6055f1a10f4cffb68b99bd15e348beb64a555553` |
| `Revision/dark_sector/dirac16complex00/python/derive_eos.py` | 49529 | `92e41c184155fc58aafbc23ac33dbca6b95562d9f5d6d82d4b79aec36af46242` |
| `Revision/dark_sector/dirac16complex00/python/independent_numerics.py` | 22360 | `85cac5a261b0e5ed5180c9b8f6044cd0997dbd03ef52e92b6980454ae924765d` |
| `Revision/dark_sector/dirac16complex00/eos-theory.json` | 21987 | `f24a778b9af3c81ed4c6b05b0157db36096c1ec2f04266cb439d9430c02418a1` |
| `Revision/dark_sector/dirac16complex00/results/independent-numerics.json` | 6290 | `2dc8ccc2cba4b826d31485522758c86483a8fc99ce23a80af40d34a6963dc1ed` |
| `Revision/dark_sector/dirac16complex00/reports/python-derive-eos.json` | 14919 | `ef39d9fb0319f060a7abd07a5c3dc5e1f74b591e912ccc7a41a95fe170625981` |
| `Revision/dark_sector/dirac16complex00/reports/python-independent-numerics.json` | 10155 | `ca3e2014f23b367f9ef1a91f2dc5039327ed35bf4fee9ab82b678731d21f5b9b` |
| `Revision/dark_sector/dirac16complex00/tests/test_dark_sector_dirac16complex00.py` | 4439 | `0954403be1534e75a43dddacd612f2dd170dbea59de63a655578f5985275c62e` |
| `Revision/dark_sector/wolfram/verify_dark_sector.wls` | 9876 | `9d0ca6a9bc12438c55e92d9eeab915a442dd9be9c30d4ccd7e72976a38f631c2` |
| `Revision/dark_sector/reports/wolfram-dark-sector.json` | 2591 | `1fdc801742c2fbf9f345253fe6d61b8d90b4230af01adf9151ba2722cd16385e` |
| `Revision/dark_sector/wolfram/verify_dark_sector_b4.wls` | 10252 | `b8367aa2f4dcab8a51f83847fedbb47d67f29be79f6655e9a577c8f22d0d2ecb` |
| `Revision/dark_sector/reference_2026_10_14/eos-theory-b4.json` | 22095 | `7ab0fcbd8bd4fdc39be91b8fa39ff76c83715e7bdd08b8326eb9809249ecd2ac` |
| `Revision/dark_sector/reports/wolfram-dark-sector-b4.json` | 2442 | `0ecd6023ec62e2c4d24c123353968c639b15e0a131095f2cad75a0d4973c434d` |

## 7. The WolframScript file `verify_dark_sector.wls` (execution provenance)

Run from the repository root: `wolframscript -file Revision/dark_sector/wolfram/verify_dark_sector.wls`. It builds the
corrected metric, its volume element and conservation law and the condensate with the author's T16
(`Revision/algebra/gammas.json` through `Revision/theory/wolfram/RevisionFieldTheory.wl`), reads the recorded history
source of `Revision/field_equations_a4/a4-equations.json` and `Revision/dark_sector/dirac16complex00/eos-theory.json`, and
prints one line per check (D1 to D7) and `7/7 checks passed`; it writes
`Revision/dark_sector/reports/wolfram-dark-sector.json` (UTF-8, LF, no time stamps). Exit code 0 iff all pass. It changes
nothing else on the computer; no network, no licence or agreement dialog. The twin `verify_dark_sector_b4.wls` of the
withdrawn metric reads the frozen `reference_2026_10_14/eos-theory-b4.json` (sha256 pinned in the script) and is kept as
that record (`B4_PROVENANCE.md`).

## 8. What this provenance does not show

* That either hypothesis is true: on the corrected metric no Kohn-Sham state and no positive-energy mode population
  gives a dark-energy value; the only values near the Unite w0 come from a condensate with lambda < 0 through its CHOSEN
  value, while its ratio drifts, and no source of the history selects it.
* That the history is a solution with the Kohn-Sham gas or a condensate as its source: the history is PRESCRIBED, and the
  source it requires (section 2) is neither (OPEN).
* Byte identity on another computer or with other package versions (all runs here: Windows 11, the versions above).
