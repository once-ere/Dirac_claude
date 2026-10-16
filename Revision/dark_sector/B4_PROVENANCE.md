# Provenance of the dark-sector change to the metric with b4(x4)

Written 2026-10-15. This file records how the whole dark-sector record of the Revision (Hypothesis:
`Revision/dark_sector/dirac16complex/`; Hypothesis00: `Revision/dark_sector/dirac16complex00/`; the
independent Wolfram verification `Revision/dark_sector/wolfram/`; the document
`Revision/docs/DARK_SECTOR_HYPOTHESES.*`; the Revision notebook `dark_sector_hypotheses`) was changed from
the withdrawn metric with b4 = 1 to the author's metric with the function b4(x4), and the evidence that the
change was made correctly: where every formula comes from, which independent computations confirm each
critical step, the commits, the sha256 of every script and output, and a complete re-run on 2026-10-15 that
reproduced every committed output byte for byte. It is also the execution-provenance file of the two
WolframScript files of `Revision/dark_sector/wolfram/` (row 31 of `provenance/EXECUTION_PROVENANCE_INDEX.md`).

## 1. The order and the source

The user's order (2026-10-14 and 2026-10-15): read `Dirac_Einstein-Lovelock_4+4_Nash.nb`; the coordinates
are X = {x0[], x1[], ..., x7[]} (In[48]); the metric is

```text
diag( Cot[6 H x0]^2,
      E^(2 a4[x4]) Sin[6 H x0]^(1/3)  (x3: x1, x2, x3),
      -1                              (x4),
      -E^(-2 a4[x4]) b4[x4] Sin[6 H x0]^(1/3)  (x3: x5, x6, x7) );
```

make this change throughout the dark-sector hypotheses, recompute every affected quantity, push each one
immediately, and create a provenance that proves the change. The user's correction of 2026-10-15:
"b4 is a function of x4; b4 is NEVER 1". Everything below therefore uses a non-constant b4(x4); b4 = 1 appears
only as the WITHDRAWN earlier record, for comparison.

The source was read, not retyped. `Revision/dark_sector/wolfram/author_notebook_inputs.wls` reads the
author's notebook with `Import[file, "Notebook"]` as an expression, converts each input box with
`ToExpression[box, StandardForm, HoldForm]` (held: no input of the author is evaluated; no front end) and
writes every cell with its label, its text in InputForm and its sha256 into
`Revision/dark_sector/reports/author-notebook-inputs.json`:

* the working-tree notebook (sha256 `74ccb8220365a66c5b42651b58ddd6b3d85739351cd27845023b07074a759bc9`):
  147 cells, 113 input cells; the pinned version of commit `b13373c` (sha256
  `4f2d83b53e4a35696e1ed4d0569f4cabbfc7463d0036c36ae5534bd6e549aafb`, git blob
  `ef25c4d148912cdbc0f80ac118d4c0e6077e6f66`): 146 cells; the only cell not in the pinned version is the input
  `HoldForm[X]`; no cell of the pinned version is missing;
* In[48]: `HoldForm[X = {x0[], x1[], x2[], x3[], x4[], x5[], x6[], x7[]}]` (cell sha256
  `2725721cb7092956f33a6654623867abf7d0e1b16035c9367c86d679bc189c06`);
* In[97]: `β3 = Exp[2*a4[x4[]]]`, `β1 = Sin[6*H*x0[]]^(1/3)`, `β2 = Cot[6*H*x0[]]^2`,
  `DiagonalMatrix[Flatten[{{β2}, β1*{β3, β3, β3}, {-1}, (-β1)*b4[x4[]]*{1/β3, 1/β3, 1/β3}}]]` - exactly the
  metric above, with b4 a function of x4.

The author's notebook was never modified, never staged and never evaluated by this work.

## 2. The chain of the change, and what confirms each step

Every step was computed by at least two independent routes. "A" and "B" are the two implementations of
dirac16complex00; "W" is the Wolfram verification `verify_dark_sector_b4.wls`, which starts from the author's
metric (`Revision/metric_b4/wolfram/MetricB4.wl`), the Lovelock tensors E_(1..3) of
`Revision/metric_b4/results/metric-b4.json` (equal to the author's stored outputs, `verify_metric_b4.wls`) and the
author's T16 (`Revision/algebra/gammas.json`), and shares no code with the Python scripts.

| step | result | computed by | confirmed independently by |
| --- | --- | --- | --- |
| volume | sqrt\|g\| = b4^(3/2) cos z; proper extra-time volume e^(-3 a4) b4^(3/2) sin^(1/2) z | `derive_effective.py` (sympy, own Christoffel symbols), check `sqrt_det_g_equals_b4_three_halves_cos_z` | W: D1_volume_b4; A: `local_model_volume_b4` |
| conservation | d rho/d x4 = -3 a4' (p3 - p_t) - (3/2)(b4'/b4)(rho + p_t); integrated dE/da4 = -3 X - (3/2) beta Pt | `derive_effective.py`, `conservation_equals_a4_record_b4` (equal to `Revision/field_equations_a4/a4-equations.json`, key b4) | W: D2_conservation_b4; numerically on the solver's states: `compute_eos.py` `conservation_with_b4_term` 2.460e-06 and `conservation_without_b4_term_fails` 1.630; the notebook (same numbers) |
| observer | w_eff = X/E - s + (beta/2)(Pt/E + s), s = 0 (A, B, N1), s = 1 (C, N2) | `derive_effective.py`, `w_eff_*_b4` | W: D3_w_eff_general_b4; A: `observer_N1_weff_identity_b4`, `observer_N2_weff_identity_b4` |
| history | with the author's weights (w1 = 1, w2 = 1/32, w3 = 1/1152, Lambda = 10) the mixed (x4, x0) equation of a diagonal source is beta_v Q = 0, Q = 6 beta (3 beta - 4) at alpha = 1: d ln b4/d a4 in {0, 4/3}; b4 is not constant, so b4 = b4(0) e^((4/3) H x4), beta = 4/3 | `derive_effective.py`, `author_weights_b4_branch` | W: D6_author_weights_branch ((3/64) be^2 (3 be - 4) cot z from the author's E_(k)) |
| required source | on that history the author's equations need the constant kappa (rho, p3, p_t, p0) = (-2/27, -2/9, -22/27, -14/27) | A: `branch_required_source` (a4-equations generalSource with alpha_k = w_k/H^(2k), Lam = -10) | W: D7_branch_required_source (from the author's E_(k)); the notebook checks its conservation and p3 + p_t = 2 p0 exactly |
| Kohn-Sham states | Psi = e^(ik.x) W^(-3) b4^(-3/4) chi, the slice Hamiltonian does not contain b4; the record (since 2026-10-16) works with lambda_hat = lambda b4(0)^(-3/2) and Vol_7(a4) = ell^3 v_t e^(2 a4), equivalently lambda_eff = lambda_hat e^(-2 a4) in the fixed cell | `run_ks_history.py` on `Revision/kohn_sham/ks-theory.json` (sectorAndAnsatz, densities; Wolfram 51/51, sympy 63/63; section 10) | `run_ks_history.py` checks `committed_slices_equal_committed_record` (max dev <= 1e-13), `lambda0_series_independent_of_b4`, `cell_volume_follows_b4`, `lambda_eff_form_agrees` (2.0e-13); the notebook re-solves 123 states bit for bit |
| free gas | the lambda = 0 gas does not feel b4; w_eff(C) = w_eff(A) - 1/3 | `compute_eos.py` | `independent_free_gas.py` (numpy, Chebyshev collocation, no solver output except for the comparison), `free_gas_independent_of_b4`; W: D5_kinetic_gas_b4 |
| condensate | b4^(3/2) S constant; u = lambda S/m ~ e^(-2 a4); the ratio u/(2 + u) drifts, wa = 4u/(2 + u)^2 | A: `condensate_S_b4_T16`, `condensate_observer_b4`, `condensate_ratio_drift_at_unite_value` (-84231/31250) | W: D4_condensate_b4_T16 and D8_condensate_drift; B: `B_condensate_dilutes_with_b4` (time integration of the 16-component equation); `compute_eos.py` `condensate_drifts_with_b4`; the notebook in exact fractions |
| modes | omega^2 = m^2 + k^2 e^(-2 a4) - q^2 e^(2 a4)/b4; q_p ~ a^(1 - beta/2) = a^(1/3) | `derive_effective.py` `extra_time_momentum_blueshift_b4`; A: `wkb_*_b4` | W: D5; B: the propagator of `independent_numerics.py` with q_p(a4) = q e^((1 - beta/2) a4) |
| models | positive models w_eff(N2) >= -1 + beta/2 = -1/3; M2 (-583/3000, 81037/500000), M3 (-287/1000, -196963/4500000) exactly; the Unite w0 needs G >= 1583/1000 | A (sympy exact, mpmath 30 digits) | B: `B_positive_models_bounded`; the notebook: exact dual-number tangents in Fraction arithmetic |

## 3. The commits (all pushed to https://github.com/once-ere/Dirac_claude.git, branch main)

| commit | what |
| --- | --- |
| `e9d1751` | dirac16complex: every effective formula derived for the metric with b4(x4) (`derive_effective.py`, 39 checks) |
| `0f73748` | dirac16complex: the Kohn-Sham gas on the history with b4(x4) (`run_ks_history.py`, 615 states, 7 checks) |
| `3932af4` | dirac16complex: the equation of state on the history with b4(x4) (`compute_eos.py`, 15 checks) |
| `0f969b1` | dirac16complex: the independent free-gas implementation on the history with b4(x4) (10 checks) |
| `98cf574` | dirac16complex00: implementations A (49 checks) and B (32 checks) and the tests for b4(x4) |
| `4cb9b7d` | both READMEs for the metric with b4(x4) and the history b4 ~ a^(4/3) |
| `019337d`, `3324b56` | the independent Wolfram verification (8 checks) and the non-evaluating reader of the author's notebook |
| `65d954c` | `Revision/docs/DARK_SECTOR_HYPOTHESES.md/.tex/.pdf` for b4(x4) (27 pages, registered), the publication test |
| `e6113b0` | the Revision notebook `dark_sector_hypotheses` for b4(x4) (46 checks, byte-identical rebuilds) |
| (this commit) | this provenance file, row 31 of the execution-provenance index, the notebook test and README |

## 4. What changed in the results (withdrawn b4 = 1 against b4(x4))

| quantity | withdrawn record (b4 = 1) | metric with b4(x4), history beta = 4/3 |
| --- | --- | --- |
| w_eff(C) - w_eff(A) | -1 | -1 + beta/2 = -1/3 |
| Kohn-Sham gas N = 688, 136 (lambda = 0), w_eff(C) | [-0.707094, -0.673602] | [-0.040427, -0.006935] (all gas series, with the couplings recalibrated on the history on 2026-10-16: [-0.040541, -0.006532]; before: [-0.040430, -0.006905]) |
| N = 8 interacting zero modes | E constant; w_eff(A) = 0, w_eff(C) = -1 | E ~ e^(-2 a4) (E(2)/E(0) = 0.018402); w_eff(A) = (2/3) Pt/E in [0.660463, 0.666665] |
| conservation | dE/da4 = -3X | dE/da4 = -3X - 2Pt (the b4-free law misses by 1.630 of max\|E\|) |
| condensate | constant; ratio wa = 0 | drifts: ratio wa = -84231/31250 = -2.695392 at the u that gives -0.764 today; w_eff(C) = -316/375 with wa = -28077/15625 |
| gas + lambda = 0 condensate, C | w0 = -0.861 at gas fraction 0.436703 (wa = +0.067014) | w_eff(C) >= -0.333015 >= -1/3: the Unite values are not reached |
| scans with a condensate | ratio definition only; distance to the Unite pair >= 0.600001 | three definitions with a drifting condensate; closest under C at 0.2910614215438 |
| M2 N2 tangent | (-861/1000, 81037/500000) | (-583/3000, 81037/500000) |
| M3 N2 tangent | (-861/1000, -196963/500000) | (-287/1000, -196963/4500000) |
| M4 N2 tangent (same parameters) | (-861/1000, -3/5) = the Unite pair, by construction | (-287/1000, -1/15) |
| M5 N2 fit over [1/2, 1] (same composition, G = 3/10) | (-0.861, -0.60), crossing of -1 at a = 0.779 | (-0.332679, -0.323083), no crossing |
| Unite w0 under N2 | reachable with G = 3/10 | needs a ghost fraction G >= 1583/1000 |
| check counts | 30, 5, 13, 9, 49, 28 | 39, 7, 15, 10, 49, 32, and Wolfram 8 |

Neither hypothesis is established by either record. The parameters of M2 to M5 were CHOSEN on the withdrawn
record (by construction, NOT predictions) and are kept so that the effect of b4(x4) is seen directly.

## 5. The re-run of 2026-10-15 (the evidence that the committed record is what the scripts produce)

On 2026-10-15, after all the commits of section 3 up to `e6113b0`, every producer was run again in the
working tree, in this order, each bounded by `timeout 423` (Windows 11 Pro for Workstations, Python 3.14.5,
WolframScript 1.14.0; the Rust solver built with cargo 1.91.1). After each step `git status --short --
Revision/dark_sector` was empty: every committed output was reproduced byte for byte.

| command (repository root) | exit | time | checks | record changed |
| --- | --- | --- | --- | --- |
| `python Revision/dark_sector/dirac16complex/derive/derive_effective.py` | 0 | 3.4 s | 39/39 | no |
| `python Revision/dark_sector/dirac16complex/compute/run_ks_history.py` | 0 | 34.9 s | 7/7 | no |
| `python Revision/dark_sector/dirac16complex/compute/compute_eos.py` | 0 | 0.2 s | 15/15 | no |
| `python Revision/dark_sector/dirac16complex/independent/independent_free_gas.py` | 0 | 77.0 s | 10/10 | no |
| `python Revision/dark_sector/dirac16complex00/python/derive_eos.py` | 0 | 3.7 s | 49/49 | no |
| `python Revision/dark_sector/dirac16complex00/python/independent_numerics.py` | 0 | 6.8 s | 32/32 | no |
| `python -m unittest Revision/dark_sector/dirac16complex00/tests/test_dark_sector_dirac16complex00.py` | 0 | 10.1 s | 4 tests OK | no |
| `wolframscript -file Revision/dark_sector/wolfram/verify_dark_sector_b4.wls` | 0 | 4.5 s | 8/8 | no |
| `wolframscript -file Revision/dark_sector/wolfram/author_notebook_inputs.wls Dirac_Einstein-Lovelock_4+4_Nash.nb <scratch>/pinned.nb` (with `git show b13373c:Dirac_Einstein-Lovelock_4+4_Nash.nb > <scratch>/pinned.nb` first) | 0 | 3.8 s | `author_notebook_inputs=OK` | no |

The same day the Revision notebook was built twice and checked once (`build_notebooks.py build` and `check
dark_sector_hypotheses`, 13.1 s to 15.1 s each): byte-identical notebooks and 129 byte-identical output files
(`Revision/notebooks/dark_sector_hypotheses.PROVENANCE.md`, section 7). Each script had been run twice when it
was committed, with byte-identical outputs.

## 6. The sha256 of every file of the record (2026-10-15, after the correction of section 9)

| file | bytes | sha256 |
| --- | --- | --- |
| `Revision/dark_sector/dirac16complex/README.md` | 16101 | `60bf649289df5cd90bfd08ed93a94e821dfbfef7fdb399fdd3d08ace7e9647ba` |
| `Revision/dark_sector/dirac16complex/derive/derive_effective.py` | 37898 | `156c4635cdd0ead748477a017940914293950fa360faf97a11935a98226fcc42` |
| `Revision/dark_sector/dirac16complex/compute/run_ks_history.py` | 13002 | `469a21c70115ca9e6f5f78dfd03733612c2ecf03f6cc07b6c604e23428f99d0e` |
| `Revision/dark_sector/dirac16complex/compute/compute_eos.py` | 27260 | `1bc9d9e2110e5365ddbbe1d042d2abffb76875eebc0e41abfac11c23625ed5b1` |
| `Revision/dark_sector/dirac16complex/independent/independent_free_gas.py` | 18072 | `b1aaba9031fcc7a03cdc43be39214b61c4e2eedc8daeffa693964a76518b10dd` |
| `Revision/dark_sector/dirac16complex/outputs/effective-formulas.json` | 5871 | `aa15a8198973517ea0c206b12377afa0f29246ea4c19503dd28c37f5785a8c2c` |
| `Revision/dark_sector/dirac16complex/outputs/ks-history-dense.csv` | 172574 | `5eee937e5d2626a77ffa5d04abe1fd6440a8a475653202340da5f86c96a92642` |
| `Revision/dark_sector/dirac16complex/outputs/eos-history.csv` | 173429 | `1ab8d52364fa8ede9ba6ff0459a9dabfea882fdff43d34f58d06a858695eb4f2` |
| `Revision/dark_sector/dirac16complex/outputs/eos-summary.json` | 58444 | `ee2ad6074ac7fe45d3c1bce0e6c9c9de51d18267208a0fb54ababef480d9e66c` |
| `Revision/dark_sector/dirac16complex/outputs/independent-free-gas.json` | 21031 | `14fc4660185988472825406b1fad5582537e11210a846550fe8cdcae5716299f` |
| `Revision/dark_sector/dirac16complex/reports/derivation-checks.json` | 11423 | `67427eaa3e496e4e07adde7bf560b932b68a35a40e54e83b2d8c00e5d054a1a1` |
| `Revision/dark_sector/dirac16complex/reports/ks-history-run.json` | 2573 | `873aa221ea313cf1be4425e3b1558ffb44b7f7e71a1a1f931b0f7ea0b075c9f0` |
| `Revision/dark_sector/dirac16complex/reports/eos-checks.json` | 5229 | `b0dce83a31874eb2c77fc790ec2f425544e56256249c1631378a41327fc05059` |
| `Revision/dark_sector/dirac16complex/reports/independent-checks.json` | 2764 | `bb475ad3f21db751bc002a6589d2a87af6b21fe29c5c04cb116f2238eb728232` |
| `Revision/dark_sector/dirac16complex00/README.md` | 15631 | `91bc77a573546f8a581e12d6b7177f22ae8846d61c7288088b88165f8a8a3d56` |
| `Revision/dark_sector/dirac16complex00/python/derive_eos.py` | 49903 | `56b2b83569c1d27f429af72a8624a713d502ef3713315f2f900ba11fb63dc17e` |
| `Revision/dark_sector/dirac16complex00/python/independent_numerics.py` | 22089 | `d69b1e7957df4a31e5a21d1bf644038b9c9c788a784df61c985c98aa87825b66` |
| `Revision/dark_sector/dirac16complex00/eos-theory.json` | 22095 | `7ab0fcbd8bd4fdc39be91b8fa39ff76c83715e7bdd08b8326eb9809249ecd2ac` |
| `Revision/dark_sector/dirac16complex00/results/independent-numerics.json` | 6341 | `4ab3ea5d4f108d7c3dcd93c66327b0c73d3b8d0852ffeb3197db57a8444c00dd` |
| `Revision/dark_sector/dirac16complex00/reports/python-derive-eos.json` | 15084 | `0ed88e5a872621e0054651a43a5d5588c0ea7b4d9e33920653839837ea73e784` |
| `Revision/dark_sector/dirac16complex00/reports/python-independent-numerics.json` | 10052 | `e620b2c0bf97f06ef081078bee1b26a84798b0acdc8979f3f5838d6ccb22e40a` |
| `Revision/dark_sector/dirac16complex00/tests/test_dark_sector_dirac16complex00.py` | 4275 | `e5650b871b5145a0d1225aec6e98b090ff49f1d76f91b158ec86ffd2d79ae9f8` |
| `Revision/dark_sector/wolfram/verify_dark_sector_b4.wls` | 9919 | `43b290c56276ad32c2c1650f38663d000e8de1d9ef530a806632e93f9f70460f` |
| `Revision/dark_sector/wolfram/author_notebook_inputs.wls` | 4103 | `b8240ab72dbceed0fcda4673a5b72b4e13c9e18968a8e1653e0bf95317284267` |
| `Revision/dark_sector/reports/wolfram-dark-sector-b4.json` | 2392 | `273e91939ba39dd8baa8b6f687e1e0110d927a1ec6de2250e90217032e3734f1` |
| `Revision/dark_sector/reports/author-notebook-inputs.json` | 40312 | `c43f70544c3b51dcce474b8181a75add8b5bb8ced088c3571b32e30f0128f782` |
| `Revision/docs/DARK_SECTOR_HYPOTHESES.md` | | `7b7549c2ae1be99eba66d3c7ed0e0228b79babb9fb23afb414ae0382ef894cb0` |
| `Revision/docs/DARK_SECTOR_HYPOTHESES.tex` | | `9d71f61f3a76f2a5a538c5b46bf6dd4d9c5b33c7f3b6c10f0c330bcfc6a620d6` |
| `Revision/docs/DARK_SECTOR_HYPOTHESES.pdf` | | `87c023b34e6dfef49baef1845ca923d7eff7309fd0a95de6278a0dce33bd6f97` |
| `Revision/notebooks/dark_sector_hypotheses.ipynb` | 472097 | `ddee8168475df239cc0eade3fa5f50c933a344bb8b5c97f0d00227cc1460c2c8` |

The two Markdown/LaTeX sources are pinned by `Revision/tests/test_dark_sector_hypotheses_publication.py`
(30 tests), which also checks that every number the document quotes is in a committed report.

## 7. The two WolframScript files (execution provenance)

* `verify_dark_sector_b4.wls` (sha256 `43b290c56276ad32c2c1650f38663d000e8de1d9ef530a806632e93f9f70460f`).
  Run from the repository root: `wolframscript -file Revision/dark_sector/wolfram/verify_dark_sector_b4.wls`.
  Reads `Revision/metric_b4/wolfram/MetricB4.wl` (the author's metric), `Revision/metric_b4/results/metric-b4.json`
  (the Lovelock tensors E_(1..3)), `Revision/theory/wolfram/RevisionFieldTheory.wl` with
  `Revision/algebra/gammas.json` (the author's T16) and `Revision/dark_sector/dirac16complex00/eos-theory.json`
  (the recorded branch source, for D7). Prints one line per check (D1 to D8) and `8/8 checks passed`; writes
  `Revision/dark_sector/reports/wolfram-dark-sector-b4.json` (UTF-8, LF, no time stamps). Exit code 0 iff all
  pass. 4.5 s on 2026-10-15; two runs byte-identical. Changes nothing else on the computer; no network, no
  licence or agreement dialog.
* `author_notebook_inputs.wls` (sha256 `b8240ab72dbceed0fcda4673a5b72b4e13c9e18968a8e1653e0bf95317284267`).
  Run from the repository root:
  `git show b13373c:Dirac_Einstein-Lovelock_4+4_Nash.nb > <scratch>/pinned.nb`, then
  `wolframscript -file Revision/dark_sector/wolfram/author_notebook_inputs.wls Dirac_Einstein-Lovelock_4+4_Nash.nb <scratch>/pinned.nb`.
  Reads both notebook files without evaluating them; prints `author_notebook_inputs=OK`; writes
  `Revision/dark_sector/reports/author-notebook-inputs.json`. 3.8 s on 2026-10-15; two runs byte-identical.
  The scratch copy is the only file it needs outside the repository; it writes nothing else.

## 8. What this provenance does not show

* That either hypothesis is true: on the history with b4(x4) no Kohn-Sham state and no positive-energy mode
  population gives a dark-energy value; the only negative values without a ghost come from a condensate with
  lambda < 0, through its CHOSEN value and while its ratio drifts (it reads w_eff(C) < -1 in the phantom window
  toward the past, section 9), and no source of the history selects it.
* That the history is a solution with the Kohn-Sham gas as its source: the history is PRESCRIBED, and the
  source it requires (section 2) is neither the gas nor the condensate (OPEN).
* Byte identity on another computer or with other package versions (all runs here: Windows 11, the versions
  above).

## 9. A correction made later on 2026-10-15

Writing the textbook chapter on this record, I found statements that had been carried over from the withdrawn
b4 = 1 reasoning. With b4 = 1 the observer read a condensate as w_eff(A) = 0 and w_eff(C) = -1, whatever its ratio,
so a phantom ratio was "not the observer's w_eff". With b4(x4) the observer reads w_eff(C) = -1/3 + (2/3) w_c
(`condensate_observer_b4`), which is below -1 exactly while the ratio is (`condensate_phantom_interval`:
lambda S/m in (-2, -1)). The ratio drifts, lambda S/m ~ e^(-2 a4), so a condensate with lambda < 0 and m S > 0
(positive energy, attractive self-interaction) moves into that window toward the past: for -382/441 today from
a = sqrt(382/441) = 0.9307 back to a = sqrt(191/441) = 0.6581, where its energy vanishes. The record had said
"phantom ... only at an instant", "it is not the observer's w_eff" and "no crossing in M1 to M5"; these were wrong
for M1 (the condensate) and are corrected in:

* `derive_eos.py` (the text `ghost` of `eos-theory.json`; re-run: 49/49, every other byte of `eos-theory.json`, the
  report and implementation B's outputs unchanged; B re-run 32/32 byte-identical; the unittest OK);
* both READMEs (the condensate items, the phantom item and the verdicts of dirac16complex and dirac16complex00);
* `Revision/docs/DARK_SECTOR_HYPOTHESES.md` (sections 1, 5.5, 6.1, 7 and 9.2), its .tex and its PDF (rebuilt twice,
  byte-identical, 27 pages, 0 warnings, registered), and its publication test (new pins; the crossing window
  asserted from `eos-theory.json`);
* the Revision notebook (the detail of `condensate_phantom_window` and two sentences; rebuilt and checked
  byte-identical; its 129 output files unchanged).

No number of the record changed and no check changed its count or verdict: the corrected statement follows from
the two checks named above, which were already in the record.

A second correction of the same afternoon: the document and the README of dirac16complex read the record's smallest
w_a among the drifting-condensate mixtures with w0 within 0.1 of the Unite w0 (-2.639515126434 under C) as a bound
("only with w_a <= -2.64", "at most -2.64"). It is a minimum, not a bound. `compute_eos.py` now records the largest
value as well (key `max_wa_with_w0_within_0p1_of_unite` of `mixture_scan`; the check
`mixture_scan_three_definitions_b4` requires it below -1, and its detail prints both ends): under C every such
mixture has w_a between -2.639515126434 and -1.41320438962 (ratio definition: -3.800209088911 to -2.685081787855;
A, B: -4.848176262726 to -3.262703276443), all far from the Unite -0.60. `compute_eos.py` was run twice (15/15,
byte-identical); only `eos-summary.json` (the new key) and `eos-checks.json` (that detail) changed. The document
(rebuilt twice, byte-identical, 27 pages, 0 warnings, registered), the README, the publication test and the
Revision notebook (which reproduces the scan, now with the new key; rebuilt and checked byte-identical) were updated.

## 10. The Kohn-Sham record moved to b4(x4) (2026-10-16)

The dark sector of 2026-10-15 solved the Kohn-Sham states of this history with the solver of the record of that day,
whose own states were those of the withdrawn metric b4 = 1: it passed lambda_eff = lambda_hat e^(-2 a4) to `single`
and took lambda_hat from the calibrated couplings of the b4 = 1 record. On 2026-10-16 the Kohn-Sham record itself was
moved to the history with b4 (`HANDOFF.md` 0.9, phase 4; `Revision/kohn_sham/solver/README.md`, "The metric with
b4(x4)"): `single --lambda` now means lambda_hat, the solver uses the cell volume Vol_7(a4) = ell^3 v_t e^{2 a4}, and the
calibration rule applied to the new history gives lambda_1 = 0.01946, 0.01206, 0.006645 and lambda_2 = 0.05838, 0.03617,
0.01993 (N = 8, 136, 688; before 0.01946, 0.0009298, 0.0001846 and 0.05838, 0.002789, 0.0005538). Changes:

* `dirac16complex/compute/run_ks_history.py` passes lambda_hat; its checks are now 8: `committed_slices_equal_committed_record`
  (all 15 series at the five committed slices, 300 integrals, deviation 0; replaces `a4_0_states_equal_committed_record`),
  `cell_volume_follows_b4` (every run used ell^3 v_t e^{2 a4}, 2.2e-16; replaces `coupling_follows_b4`) and the new
  `lambda_eff_form_agrees` (the 48 interacting states at the committed slices a4 > 0 solved again in the coordinate-cell
  form `single --beta 0 --lambda lambda_eff`: E_KS, E, P3, Pt, P0 agree to 2.0e-13). Run: 46 s (12 jobs), 8/8; the
  columns `beta` and `Vol7` were added to `outputs/ks-history-dense.csv`.
* `compute_eos.py`: 15/15. Changed numbers (interacting N = 136, 688 series): w_eff(A) in [0.292793, 0.326802] (before
  [0.292903, 0.326429]), |Pt/E| <= 1.8e-3 (before 1.1e-4), w_eff(C) in [-0.040541, -0.006532] (before [-0.040430,
  -0.006905]), tangent wa in [-0.019170, -0.008787] (before [-0.017766, -0.009043]), fitted wa in [-0.028228, -0.019171]
  (before [-0.026521, -0.019590]); d w_eff/da4 two ways 1.366e-06 (before 6.394e-07). The lambda = 0 series and the
  mixtures with the N = 688, lambda = 0 gas are the same (their numbers differ at most in the 13th significant digit,
  the rounding of Vol_7 against 1/Vol_7); the N = 8 series are the same in substance (lambda_hat and the history are
  unchanged for N = 8). No verdict changed: the gas is radiation-like under A and B and close to 0 under C, not a
  dark-energy value; the Unite values are not reached.
* The README, the document `Revision/docs/DARK_SECTOR_HYPOTHESES` (with its publication test) and the notebook
  `Revision/notebooks/dark_sector_hypotheses.ipynb` (its `run_one` passes lambda_hat; 123 rows bit for bit) were
  updated; the textbook chapters that quote these numbers follow in phase 9 of `HANDOFF.md` 0.9.
