# Execution provenance: the Stage-3 dark-sector Jupyter notebook

Set: `notebooks/dirac16complex_dark_sector.ipynb` with its builder `notebooks/build_dirac16complex_notebook.py`, its headless runner `notebooks/run_notebook.py` and its auditor `notebooks/check_notebook.py` (old Stage 3, "dark-sector numerics"). The notebook drives the Rust simulator `studies/dirac16complex_cosmology`, which you must build first against the pinned SUNDIALS engine that `scripts/setup_solver.ps1` (or `scripts/setup_solver.sh`) downloads, and it calls the Python analysis `scripts/analyze_dirac16complex_exp3.py`.

Verified on 2026-10-02 at commit `c2b33ccd16edb9c8b46585d0db6b2911a1f5d84e` of https://github.com/once-ere/Dirac_claude.git, and verified again on 2026-10-07 at commit `72fc9ffc4a10328080a5778cc8a8c6e689aeaca6` (the head of `main` on GitHub when that verification started; no file that the notebook runs or reads changed between the two commits). Result: the notebook EXECUTES OK with both executors, Jupyter's `nbconvert` and the repository's `run_notebook.py`: exit code 0, 71 of 71 gauntlet assertions passed, last line `ALL CHECKS PASSED`. The auditor `check_notebook.py` also passes (exit code 0, verdict `SUCCESS`). Every output reproduces the committed files byte for byte: the executed notebook, the 17 figures, `notebook-report.json` and the 65 files written into `build/notebook-run/`. On 2026-10-02 this held in two runs from fresh clones, one through Git Bash and one through PowerShell, and again in two further runs from fresh clones in which the private Python environment was installed exactly as Part 3.6 says (Part 6.5). On 2026-10-07 it held again in two new runs from fresh clones of `72fc9ff`, each with a new private environment installed exactly as Part 3.6 says, one through Git Bash and one through PowerShell (Part 6.6). The only output that is never byte-identical is Jupyter's own executed copy `build/nbconvert/dirac16complex_dark_sector.ipynb`, which by design records execution timestamps (and, on Windows, uses CRLF line endings); its content (every printed character and every image) is identical. No file of the repository had to be changed. The details are in Part 6.

This file is written for a student who has never used Jupyter, a Python environment or Rust. Everything you need to run the notebook is in this file; you do not have to read any other file first.

## 1. What this notebook is and what it computes

**The physics in plain words.** The project studies a field called "dirac16complex": a field with 16 complex components (a "spinor") whose values are not ordinary numbers but anticommuting *Grassmann* numbers (theta1 theta2 = -theta2 theta1), as they must be for a fermion field (a field whose quanta behave like electrons). The field lives in an 8-dimensional space-time with 4 space-like and 4 time-like directions. The coordinates are x0, ..., x7; x4 is the time in which everything evolves, x1, x2, x3 are ordinary 3-dimensional space, x0 is a hidden space direction and x5, x6, x7 are three extra time directions. The flat metric is eta = diag(+1, +1, +1, +1, -1, -1, -1, -1). Counting always starts at 0.

Stage 3 of the project asks one question: **can this field behave like the dark matter or the dark energy of cosmology?** Dark matter behaves like a pressureless gas ("dust", equation of state w = p/rho = 0); dark energy has a negative pressure (w close to -1) that makes the expansion of the universe accelerate. The supernova compilation called "Unite" in the project's input material describes dark energy by w0 = -0.861 and wa = -0.60 in the formula w(a) = w0 + wa (1 - a), where a is the scale factor (a = 1 today).

The question is answered by five numerical experiments. In each one the field equations reduce to a system of ordinary differential equations (ODEs) in the time, and the ODEs are integrated by CVODE, the variable-step ODE solver of the SUNDIALS library, inside the Rust program `studies/dirac16complex_cosmology` (the "simulator"). The notebook itself never integrates an ODE: it runs the simulator, checks its output, recomputes the physics independently with numpy and draws the figures.

| Experiment | Background | Question | What the committed outputs (reproduced here) say |
| --- | --- | --- | --- |
| EXP-1 | the primordial "pair-creation" field of the author's original notebook | what do the energy density rho, the pressure p and w of the field do there, and what source would Einstein's equations need? | the field is exactly frozen (rho constant to 4.2e-9); the primordial field would need a source with negative energy, rho_req <= -21 H^2/kappa |
| EXP-2 | homogeneous 8-dimensional cosmology solved together with 8-dimensional Einstein gravity | does a self-gravitating condensate of the field make the universe isotropic? | from a Kasner singularity to isotropic 8-dimensional dust (H_i t -> 2/7); the extra times turn from shrinking to growing |
| EXP-3 | 4-dimensional late universe, extra dimensions frozen | can the condensate's self-interaction reproduce the Unite dark energy (w0, wa)? | no: tuned to w0 = -0.861 it has wa = -4.81, its energy density turns negative at redshift z = 0.293 and the universe bounces at z = 0.388; excluded as the Unite dark energy |
| EXP-4 | expanding 3-space (radiation era; de Sitter followed by radiation) | do the quanta of the field behave like dark matter, and how many are created by the expansion? | a thermal gas goes from w = 0.3329 at a = 1 to w = 0.0359 at a = 100 (radiation to dust); pairs are created for mass m > 0 and none for m = 0 |
| EXP-5 | shrinking extra times | why must physics be restricted to modes without extra-time momentum? | such modes grow faster than any exponential (u^dagger u reaches 1.3e16), in agreement with a WKB estimate |

**What the notebook does, cell by cell.** The notebook has 23 cells: 15 markdown cells (the explanations, the equations, how to run it, the conclusions) and 8 code cells. When it is executed, the 8 code cells do this:

1. **Driver.** Finds the repository folder (it walks up from the current folder until it finds `studies/dirac16complex_cosmology/Cargo.toml`), finds the built simulator (the environment variable `DIRAC16_BIN` first, then `studies/dirac16complex_cosmology/target/release/dirac16complex_cosmology.exe` on Windows or `.../dirac16complex_cosmology` elsewhere), loads the exact integer gamma matrices from `artifacts/dirac16complex/arbitrary-field/algebra-fixture.json`, verifies six algebra identities (the Clifford relations, C = gamma^0 gamma^1 gamma^2 gamma^3, B = -i C gamma^4, B^2 = 1, B Hermitian, B C = -i gamma^4) with deviation exactly 0, and configures matplotlib so that the PNG files are reproducible (Agg backend, 100 dpi, no software stamp).
2. **`print-config`.** The simulator prints its own constants, tolerances, fixture hash and state layouts, and must end with the line `SUCCESS`.
3. to 7. **EXP-1 to EXP-5.** Each cell runs one simulator subcommand (`exp1` ... `exp5`) into the scratch folder `build/notebook-run/expN/`; the simulator prints its own self-checks as `PASS - ...` lines and must end with `SUCCESS`. The cell then compares every file the simulator wrote byte for byte with the committed file in `artifacts/dirac16complex/numerics/expN/`, recomputes the key physics independently from the raw spinor columns (numpy), draws its figures into `artifacts/dirac16complex/numerics/figures/` (printing `figure <name> sha256 <hash>` and showing the image) and prints the key numbers. The EXP-3 cell also runs `scripts/analyze_dirac16complex_exp3.py` (least-squares fits of w0 and wa, a fine scan of the coupling x0, distance-modulus fits; numpy only) into `build/notebook-run/exp3/` and compares its three files value by value with the committed ones (relative 1e-6, absolute 1e-8). The EXP-4 cell is the long one: about 3.4e8 CVODE steps on up to 8 threads.
8. **Gauntlet.** 71 assertions, each printed as `PASS - <name>: <detail>`. If one fails, the cell stops with an `AssertionError` and the notebook fails. The cell ends with the line `ALL CHECKS PASSED`.

**What is recomputed and what is only re-read.** Every execution re-runs the simulator (6 runs: `print-config` and the 5 experiments), re-runs the EXP-3 analysis (the 7th "program run"), redoes all of the notebook's own numpy recomputations and redraws all 17 figures. It does **not** re-run the five independent Python checkers `scripts/check_dirac16complex_exp1.py` ... `exp5.py`. The gauntlet re-reads their committed reports `artifacts/dirac16complex/numerics/expN/python-check-report.json` (167 checks in all), the committed `numerics-summary.json`, the Stage-1 summary and the two Stage-2 reports, and asserts that those committed files say SUCCESS and are consistent (same fixture hash, same totals).

**The 71 gauntlet assertions.** The value in brackets is what the verification runs measured (identical in both runs and equal to the committed notebook).

| Assertion | What must hold [measured] |
| --- | --- |
| `all_runs_success` | all 7 program runs exited with code 0 and every simulator run ended with `SUCCESS` [7 runs] |
| `fresh_program_outputs_byte_identical` | every file the simulator wrote equals the committed file byte for byte [exp1 29/29, exp2 4/4, exp3 11/11, exp4 13/13, exp5 5/5] |
| `fresh_analysis_outputs_numerically_equal` | the 3 EXP-3 analysis files equal the committed ones value by value (relative 1e-6, absolute 1e-8) [3/3; they were in fact byte-identical] |
| `fixture_hash_consistent` | the sha256 of `algebra-fixture.json` is the one recorded in the 5 fresh summaries, the 5 committed checker reports and `numerics-summary.json` [`8b4f15462ca4d61e...`] |
| `stage1_physics_verified` | the committed Stage-1 summary has no failed check and no disagreement [153/153] |
| `stage2_mode_reduction_verified` | the committed Stage-2 reports confirm the exact mode reduction used by EXP-1 |
| `algebra_relations_exact` | the six algebra identities of the driver cell hold exactly [0.0] |
| `exp1_rust_self_checks` ... `exp5_rust_self_checks` (5 assertions) | every self-check of the simulator is true and its verdict is SUCCESS [10/10, 15/15, 14/14, 23/23, 7/7] |
| `exp1_python_checker` ... `exp5_python_checker` (5 assertions) | every check of the committed checker report is true, including repeat-run byte identity and refined-tolerance convergence [25/25, 35/35, 32/32, 54/54, 21/21] |
| `exp3_analysis_checks` | the 10 internal validations of the EXP-3 analysis are true [10/10] |
| `numerics_summary` | the committed totals are consistent and have no failure [69 Rust + 167 Python + 10 analysis checks] |
| `exp1_background_recomputed` | a4, a4', a4'', the scale factors and the required Einstein source recomputed from the closed-form window, to 1e-12 [3.6e-15] |
| `exp1_einstein_source_negative` | the source Einstein's equations would need has negative energy [max rho_req = -21.000000] |
| `exp1_seven_volume_constant` | abs(V/V0 - 1) <= 1e-13 [6.7e-16] |
| `exp1_observables_recomputed` | rho, p_j, S, M_eff, both kinetic/potential splits, w and the norms recomputed from the raw spinor, to 1e-12 [8.9e-16] |
| `exp1_exact_propagator` | the spinor equals the exact solution exp(-i h t) u0 to 1e-7 [3.12e-09] |
| `exp1_rho_frozen` | rho stays constant to 1e-8 in all 26 runs [4.19e-09] |
| `exp1_eigenstate_pressure_and_S_frozen` | for energy eigenstates p_0 and S stay constant to 1e-8 [2.64e-09] |
| `exp1_norms_conserved` | Hilbert and Krein norms conserved to 1e-8 [2.70e-09] |
| `exp1_profile_independence` | the two primordial profiles A = 1 and A = 2 give the same spinor, to 1e-12 [0.0e+00] |
| `exp1_eigenmode_laws` | rho = E, p_0 = K^2/E, S = 1/E, KE_L = PE_L = E/2, w = K^2/(7 E^2), to 1e-8 [1.4e-17] |
| `exp1_lambda_self_consistent_mass` | the notebook's own fixed-point iteration gives the simulator's self-consistent mass, to 1e-12 [1.473482664064202, difference 0.0e+00] |
| `exp1_mixed_state_oscillation` | the oscillation range of p_0 of the mixed state equals the simulator's to 1e-9, and the committed checker's exact-solution deviation is below 1e-8 [0.803028; 3.7e-10] |
| `exp2_columns_recomputed` | Theta, V, s(u), S, M_eff, rho, p, KE_L, PE_L and the bound recomputed from the state, to 1e-9 [2.4e-13] |
| `exp2_constraint_preserved` | the Hamiltonian constraint holds to 1e-9 relative [1.26e-10] |
| `exp2_SV_constant` | S V is conserved to 1e-9 [4.03e-10] |
| `exp2_exact_volume` | V(t) equals the exact quadratic and H_i V the exact straight line, to 1e-9 [1.0e-10; 5.0e-10] |
| `exp2_bound_identity` | Theta^2 - 3 H_a^2 - 2 kappa rho = H_b^2 + 3 H_c^2 + 2 (constraint residual), to 1e-9 [1.5e-14] |
| `exp2_kasner_exponents` | the Kasner exponents of the singularity: closed form against the summary to 1e-12, extrapolated from CVODE to 1e-6 [0.0e+00; 2.9e-07] |
| `exp2_late_time_isotropic_dust` | abs(H_i (t - t_s) - 2/7) <= 1e-3 at the end [1.1e-04] |
| `exp2_theta_bound_positive_energy` | Theta/(3 H_a) > 1/sqrt(3) wherever rho > 0, and the dust run keeps w_eff > -1 + 1/sqrt(3) [0.6127; -0.3873] |
| `exp2_bound_fails_only_with_negative_energy` | the bound fails only on rows with rho < 0 (reported, not hidden) [0.3437] |
| `exp2_phantom_iff_negative_kinetic_energy` | w < -1 with rho > 0 exactly where KE_L < 0 [14 rows] |
| `exp3_sigma_from_spinor` | the density ratio sigma from the spinor equals a^-3 to 1e-8, and the state's ln sigma to 1e-12 [2.5e-09; 2.0e-14] |
| `exp3_closed_forms` | rho, p, E, KE_L, PE_L equal their closed forms, to 1e-8 [2.8e-09; 2.2e-09] |
| `exp3_norms_conserved` | the spinor norms u^dagger u and u^dagger B u are conserved to 1e-8 [2.5e-09] |
| `exp3_mu_independence` | the runs with mu = 3 and mu = 7 agree to 1e-8 [4.8e-09] |
| `exp3_distance_quadrature` | the notebook's own Gauss-Legendre comoving distance equals the CVODE one to 1e-8 [1.7e-09] |
| `exp3_tangent_cpl` | w0 = x0/(1+x0), wa = 3 x0/(1+x0)^2 equal the analysis to 1e-5 [0.0e+00] |
| `exp3_x0_reproduces_unite_w0` | x0 = w0/(1 - w0) gives the canonical couplings to 1e-6 [4.9e-07] |
| `exp3_roots_q0_cs2` | the zero of rho_psi, the crossing of w = -1, the bounce, q0 and the sound speed recomputed, to 1e-9 [7.8e-16] |
| `exp3_requested_fits_undefined_for_x0_negative` | the requested fits over the Unite ranges do not exist for x0 < 0 (pole, bounce); reported |
| `exp3_unite_constant_w_projections_recorded` | the constant-w projections of the Unite curve are finite and recorded (a record, not a verdict), and the comparison curves are recomputed to 1e-9 [-1.0277; -0.9115] |
| `exp4_grid_and_weights` | the 48-node Gauss-Legendre grid and the Fermi-Dirac weights recomputed, to 1e-12 [5.7e-15] |
| `exp4_mode_sums_recomputed` | rho, p, KE_H, PE_H recomputed from the raw spinors, to 1e-9 [4.8e-15] |
| `exp4_rho_matches_kinetic_theory` | the mode-sum rho equals kinetic theory to 1e-6 [1.98e-08] |
| `exp4_pressure_matches_kinetic_plus_free_wave` | p agrees with kinetic theory to 1e-4 and inside the predicted interference envelope (ratio below 1) [1.87e-05; ratio 0.28] |
| `exp4_unitarity` | abs(u^dagger u - 1) <= 1e-6 for every thermal mode [2.4e-07] |
| `exp4_w_radiation_to_dust` | w(a = 1) within 0.005 of 1/3 and w(a = 100) < 0.05 [0.3329; 0.0359] |
| `exp4_gas_weighted_beta_below_1e-6` | the gas-weighted pair weight stays below 1e-6 [3.7e-08] |
| `exp4_massless_no_production` | no pairs for m = 0: max abs(beta_k)^2 <= 1e-10 [8.5e-25] |
| `exp4_massive_production` | pairs for every m > 0: n a^3 > 1e-4 [1.454e-03, 4.990e-03, 4.412e-03, 2.421e-03] |
| `exp4_number_density_recomputed` | n a^3 recomputed from the spectrum, to 1e-9 [9.0e-12] |
| `exp4_produced_gas_eos` | the equation of state of the produced gas recomputed to 1e-9, and it ends with w < 0.001 for every m > 0 [8.9e-16] |
| `exp4_kink_tail` | the high-momentum tail matches the formula (m k/(4 E^4))^2 within 0.35 [0.042] |
| `exp5_norms_recomputed` | u^dagger u and u^dagger B u recomputed from the raw spinors, to 1e-12 [6.7e-16] |
| `exp5_energy_turns_imaginary_at_tstar` | E^2 = m^2 - q^2 e^(2Ht) and t* = ln(m/q)/H recomputed, to 1e-12 [2.8e-16] |
| `exp5_krein_conserved` | the Krein norm u^dagger B u is conserved to 1e-8 (relative to max(u^dagger u, 1)) [1.1e-09] |
| `exp5_wkb_leading` | growth agrees with leading-order WKB to 1e-2 [1.03e-03] |
| `exp5_wkb_first_order` | growth agrees with first-order WKB to 2e-3 [2.47e-04] |
| `exp5_super_exponential` | the late growth rate exceeds the early one by more than 5 [14.04] |
| `figures_written` | exactly the 17 required figures were written and their hashes re-read from disk [17] |
| `prose_numbers_match_reports` | each of the 78 numbers quoted in the notebook's text equals the reports to half a unit of its last printed digit [78] |

(The table has 63 rows; the two rows marked "(5 assertions)" stand for 5 assertions each, so the total is 63 - 2 + 10 = 71.)

Besides the 71 assertions the output contains other checks: the 6 algebra lines of the driver cell, the simulator's own 69 `PASS - ...` self-check lines (10 + 15 + 14 + 23 + 7) and the analysis' 10 `check_...=true` lines. In total a successful run prints 140 lines that begin with `PASS - ` and none that begin with `FAIL`.

**Documents that cite its results.**

* `provenance/DIRAC16COMPLEX_DARK_SECTOR_NUMERICS.md` (and its `.tex` and `.pdf`), the Stage-3 document: Section 5.4 "Notebooks and figures", Section 11.1 "The Jupyter notebook" (23 cells, the 62 byte-identical files, the value-by-value rule), Section 14 "Files and hashes", Section 15 "Reproduction"; it embeds the 17 figures.
* `provenance/DIRAC16COMPLEX_STUDENT_GUIDE.md` (and `.tex`, `.pdf`): Section 10 "The Jupyter notebook" (23 cells, 71 assertions, the commands and their expected output); it embeds 3 of the figures.
* `provenance/DIRAC16COMPLEX_TEXTBOOK.md` (and `.tex`, `.pdf`) and its chapters `provenance/textbook/chapters/11-dark-sector-experiments.md` (Sections 11.5 and 11.18: "71 assertions") and `19-reproducing-everything.md` (Section 19.8); the figures are embedded in chapters 08, 09, 10 and 11 of the textbook.
* `README.md` (the Stage-3 row and the Stage-3 gate).

**Programs that read its outputs.** `artifacts/dirac16complex/numerics/notebook-report.json` (written by the auditor) is read by the unit tests `tests/test_d16c_numerics_publication.py` and `tests/test_d16c_student_guide_publication.py`, and by the Stage-3 gates `scripts/verify_stage3_dark_sector.ps1` and `scripts/verify_stage3_dark_sector.sh`, whose steps `stage3-20` to `stage3-25` execute this notebook with both executors and require the fresh report to equal the committed one and the 17 figures to be unchanged. This is why the figures and the report must be reproduced byte for byte.

## 2. Files

All files of the repository are stored with LF line endings; the repository's `.gitattributes` line `* -text` makes git store and check out every file byte for byte, so the sha256 values below are the same on Windows, macOS and Linux. Lines, bytes and sha256 are those of commit `c2b33cc`. They are unchanged at commit `72fc9ff`: on 2026-10-07 every row of the tables of this file that carries a sha256 (135 rows, in Parts 2.1, 2.2, 2.3 and 6.3) was checked again against a fresh clone of `72fc9ff`, with no mismatch in sha256, bytes or lines.

### 2.1 The notebook and the programs it uses

| File | Role | Lines | Bytes | sha256 |
| --- | --- | --- | --- | --- |
| `notebooks/dirac16complex_dark_sector.ipynb` | the notebook, committed with its outputs (23 cells, 8 of them code; kernel `python3`) | 3204 | 2149978 | `5cd2befc1862041c0047c3d38db1dcc182aa47dde8db0cd571a2023fbc9ac5f0` |
| `notebooks/build_dirac16complex_notebook.py` | writes the notebook without outputs (standard library only; not run when you execute the notebook) | 2597 | 151986 | `9c233bd2e615ab118b2d638117f013a48db94bd880e33dca7a216d2f17eecf75` |
| `notebooks/run_notebook.py` | the repository's headless runner: executes the code cells, writes the outputs back only if every cell succeeded | 125 | 4503 | `ef5bbd8c082f2e17ed2c894788f5f9edd791a23ecb25ebe266881fe2d7cff40c` |
| `notebooks/check_notebook.py` | the auditor: 11 rules per executed copy, cross-check of two executions, writes `notebook-report.json` | 312 | 15293 | `9578987a542e124445927305bd35a91b3c8b27c21c1b50b645d48a8b536b5874` |
| `scripts/analyze_dirac16complex_exp3.py` | the EXP-3 analysis (numpy, own Nelder-Mead), run by the EXP-3 cell | 914 | 44699 | `4d179160d3ae2a5155167725350de069d17a9590521023c54e28b40e0542a4d2` |
| `scripts/setup_solver.ps1` | downloads the pinned engine into `vendor/rustSolveIt` (PowerShell) | 61 | 2423 | `d50ad2cc8aeb9f1d316a736aa466712ab12eed76925ec3105cbc0c81fdc54fb3` |
| `scripts/setup_solver.sh` | the same for bash (Git Bash, macOS, Linux) | 75 | 3002 | `9100b589bcbf2ab3e51c7d06087a5f27d2eff51d121a968475d11d054e819a6a` |
| `requirements-stage3.txt` | the pinned Python packages | 14 | 658 | `8edbc7a8e6d624411505ffeaa303608a7b23fc169f9fce5566c9359387930660` |
| `.cargo/config.toml` | adds `-C target-feature=+fma` to every Rust build below the repository root | 4 | 194 | `99c33150307443ab865e8732017dda6cf2fae032e11ca50a7a386cacbb7f68ce` |
| `studies/dirac16complex_cosmology/Cargo.toml` | the simulator's manifest (path dependencies on the engine's crates `sundials_core` and `cvode_rs`) | 18 | 658 | `71c88d6d0327a9fa90424e334032c14e5598c3fa619f36be01a3c9f358abcb6c` |
| `studies/dirac16complex_cosmology/Cargo.lock` | the locked dependency list (no crates.io package) | 22 | 358 | `5b07fb4d98910c297604c76f771d95ccec44cda33498b9cd3ea67516ff730aaf` |
| `studies/dirac16complex_cosmology/src/main.rs` | the command line: `print-config`, `exp1` ... `exp5`, `all`; `--output DIR`; last line `SUCCESS` or `FAILURE` | 170 | 5888 | `80b0cea995588d14d8ddbb0db1388b2f7019dbda0f70aff9ae20f02a95a0eedf` |
| `studies/dirac16complex_cosmology/src/lib.rs` | shared types, constants and the run context | 259 | 10106 | `319dceb692afa71ce69088200e2b5df006503d86f56247d8e3bb39eefef3320f` |
| `studies/dirac16complex_cosmology/src/generated.rs` | the gamma matrices, C, B and the fixture hash, generated from `algebra-fixture.json` (compiled in) | 239 | 17391 | `29631bcd9e737b5fe57a41ae2750c7637e31580974577d34b26ada45c560a3ba` |
| `studies/dirac16complex_cosmology/src/spinor.rs` | 16x16 complex linear algebra of the mode equations | 640 | 20839 | `5c13e534ff7d79cd90d351e519f81141b16750d067147b154925a10d0d1e9764` |
| `studies/dirac16complex_cosmology/src/driver.rs` | the reusable CVODE driver | 582 | 19799 | `eaeca5f1280ee2ed8fd34bf4febafce5954a1a3299b6483aded9ae3c8ed740a4` |
| `studies/dirac16complex_cosmology/src/output.rs` | the deterministic CSV and JSON writers | 267 | 9076 | `2cc311eecaea066fba7d49d5141e443227b45f84a9d4ef35078b8d7536c5d59b` |
| `studies/dirac16complex_cosmology/src/exp1.rs` | EXP-1, the primordial field | 903 | 31950 | `034c186104c22bce8df332af0aed63c795fe81e4f83d639e44d65681215c8823` |
| `studies/dirac16complex_cosmology/src/exp2.rs` | EXP-2, 8D Einstein gravity with the condensate | 1337 | 52475 | `8c321c36815d1d541bda9308ca0de5800cd67756a23d3339a32f72568b178830` |
| `studies/dirac16complex_cosmology/src/exp3.rs` | EXP-3, the condensate as dark energy | 1374 | 49780 | `2e16c9781859820910984f31522fc3ada8c10fd493a40f668898a1d7257cd008` |
| `studies/dirac16complex_cosmology/src/exp4.rs` | EXP-4, Fermi gas and pair creation (up to 8 threads) | 2922 | 111153 | `47338b0cd9e8bf7eedb0c02994c72efee194e34f0916399773b26fe4df007a03` |
| `studies/dirac16complex_cosmology/src/exp5.rs` | EXP-5, the extra-time sector | 507 | 18458 | `8670787337f58d31d9f2870224168eb82ec216e8cb59edf6532076df12f695aa` |

The Rust simulator also needs the SUNDIALS engine, which is **not** in the repository: `scripts/setup_solver.ps1` / `.sh` downloads the repository https://github.com/once-ere/rustSolveIt_Win11_SUNDIALS_7_8_0 at the pinned commit `a8fdff459adfe181573d7924b18bffbdf378fdb3` into `vendor/rustSolveIt` (git-ignored; only the folders `sundials_rs` and `planet_Mercury/notebook` are checked out). The simulator uses its crates `sundials_rs/crates/sundials_core` and `sundials_rs/crates/cvode_rs`. It needs nothing from crates.io (no other download during the build).

The builder `notebooks/build_dirac16complex_notebook.py` is **not** run when you execute the notebook. It writes the notebook *without* outputs (23 cells, sha256 `d0f1683451128818c838eeec9049b27dc3943c4f5d5eb2edb73cc1d544c0adef`, 2562 lines) next to itself, overwriting the executed notebook. Run it only if you change the notebook's text or code, and then execute the notebook again with `run_notebook.py` (Part 3.10). On 2026-10-02 the builder was run twice on a copy outside the repository: both builds were byte-identical, and they equal the committed notebook with its outputs removed (same cells, same ids, same metadata). On 2026-10-07 the same was done again with the builder of commit `72fc9ff`: two builds of 0.6 s each, exit code 0, the line `built ...dirac16complex_dark_sector.ipynb (23 cells, 8 code cells, 78 quoted numbers)`, both with sha256 `d0f1683451128818c838eeec9049b27dc3943c4f5d5eb2edb73cc1d544c0adef` (2562 lines, 173345 bytes); the committed notebook with its outputs and execution counts removed and written in the builder's format has exactly these bytes.

### 2.2 Inputs the notebook reads

The simulator reads no data file: the gamma matrices are compiled into it (`src/generated.rs`). The EXP-3 analysis reads only the fresh files that the simulator has just written (`build/notebook-run/exp3/summary.json` and its 10 CSV files). The notebook itself reads these 75 committed files (62 + 3 compared with the fresh outputs, 10 re-read by the gauntlet or the driver cell):

| File | Role | Lines | Bytes | sha256 |
| --- | --- | --- | --- | --- |
| `artifacts/dirac16complex/arbitrary-field/algebra-fixture.json` | exact integer gamma matrices, C and B (cell 1) | 18440 | 213133 | `8b4f15462ca4d61ef6ec0e72f04c8a77d23ce8bcabc9b6ce19f921c90e02653b` |
| `artifacts/dirac16complex/arbitrary-field/stage1-summary.json` | Stage-1 check counts (gauntlet stage1_physics_verified, quoted 153) | 1531 | 45576 | `a65972b5a52f947d9bee9f67e09f7151fff617c03f496ba313e07db168c10770` |
| `artifacts/dirac16complex/primordial-field/wolfram-primordial-report.json` | Stage-2 mode-reduction checks (gauntlet) | 190 | 13638 | `a0164273df62f2e15463160680fd6e27bee717d969be949526231a5e47fdd8a2` |
| `artifacts/dirac16complex/primordial-field/python-primordial-report.json` | Stage-2 mode-reduction checks (gauntlet) | 3078 | 91797 | `2d9cc593bd7812be7500820237d31e5836c5fc561853122382eb4de8e35fb55b` |
| `artifacts/dirac16complex/numerics/numerics-summary.json` | Stage-3 totals 69/167/10 (gauntlet numerics_summary) | 2441 | 104722 | `af91bbe05ae512a699286fe64a45a06b5906d1776aa82e17a708de9788fb2c88` |
| `artifacts/dirac16complex/numerics/exp1/python-check-report.json` | exp1 Python checker report (gauntlet exp1_python_checker) | 54 | 1918 | `840fc6fb8797fa66cd043a199357b599c6b2202cbeef426f0ed9058d318fafe4` |
| `artifacts/dirac16complex/numerics/exp2/python-check-report.json` | exp2 Python checker report (gauntlet exp2_python_checker) | 209 | 7549 | `756af8dfaff3dc146109e4833cd75223bf97d828881ccac0ef5c0b686975f0ef` |
| `artifacts/dirac16complex/numerics/exp3/python-check-report.json` | exp3 Python checker report (gauntlet exp3_python_checker) | 80 | 3109 | `f4a1ea92195f490e4dc0054af62ef0d05767f92aae4da4a046cd59d3430b025f` |
| `artifacts/dirac16complex/numerics/exp4/python-check-report.json` | exp4 Python checker report (gauntlet exp4_python_checker) | 238 | 11889 | `59302eaa00d26957b388a97ea8dd2b3c9ad8b997ae996f05f40ee92971473edb` |
| `artifacts/dirac16complex/numerics/exp5/python-check-report.json` | exp5 Python checker report (gauntlet exp5_python_checker) | 48 | 1723 | `bf7d379b6cf41da6984c1a3490aec5ffedf968295ee52c2c06dcb4f5d8128e03` |
| `artifacts/dirac16complex/numerics/exp1/background_A1.csv` | committed exp1 output, compared byte for byte with the fresh run | 202 | 87497 | `72bd5d384aeba962399298a43116d0856f9f030957e67b62c8c66693d493bd0f` |
| `artifacts/dirac16complex/numerics/exp1/background_A2.csv` | committed exp1 output, compared byte for byte with the fresh run | 202 | 87497 | `6af0c40f2129eaed6df24f36d8df102a506a4d178bd5af58c5d92ae5d4fe22fb` |
| `artifacts/dirac16complex/numerics/exp1/run_A1_K0_pos_Bp.csv` | committed exp1 output, compared byte for byte with the fresh run | 202 | 261696 | `65f3d5eb2ed50135d800847824b3e1578a00702152c3dd64c951ac878560e460` |
| `artifacts/dirac16complex/numerics/exp1/run_A1_K0_pos_Bm.csv` | committed exp1 output, compared byte for byte with the fresh run | 202 | 261919 | `d4d656dc8c8185dba84194d4d50a07e76492f1d2ef86ca27165878631a0eef1f` |
| `artifacts/dirac16complex/numerics/exp1/run_A1_K0_neg_Bp.csv` | committed exp1 output, compared byte for byte with the fresh run | 202 | 262824 | `682116b7fdfc4f177e9f2c52827e87e8f0a294e1f0a47850aeb0604b4a712443` |
| `artifacts/dirac16complex/numerics/exp1/run_A1_K0_mix.csv` | committed exp1 output, compared byte for byte with the fresh run | 202 | 264376 | `ec2e042b87ee574dc0ef3c32a5241e32cd9b18c3c0cd5eb1a492f05be1c47dfb` |
| `artifacts/dirac16complex/numerics/exp1/run_A1_K0p5_pos_Bp.csv` | committed exp1 output, compared byte for byte with the fresh run | 202 | 262583 | `073ba39a2b6fb46426a1771e2dd80c1b8d81fb6f4d4f9a0d90b9e756934c543c` |
| `artifacts/dirac16complex/numerics/exp1/run_A1_K0p5_pos_Bm.csv` | committed exp1 output, compared byte for byte with the fresh run | 202 | 262825 | `4866ad7cd5772608b92393d3d329fac935237ed19e18763ff070d0e70cfec956` |
| `artifacts/dirac16complex/numerics/exp1/run_A1_K0p5_neg_Bp.csv` | committed exp1 output, compared byte for byte with the fresh run | 202 | 264241 | `fe46e88017ffb9b47fa4c5828f25322273e60e00d387d92860c60a1ae370a5f3` |
| `artifacts/dirac16complex/numerics/exp1/run_A1_K0p5_mix.csv` | committed exp1 output, compared byte for byte with the fresh run | 202 | 264606 | `a932ea73d3487f1fd3eb4b1d5c4d64476312b10c32ff0d5223cb95174b81b6e8` |
| `artifacts/dirac16complex/numerics/exp1/run_A1_K2_pos_Bp.csv` | committed exp1 output, compared byte for byte with the fresh run | 202 | 262579 | `9fd75876efe3a60a5cb0a67e256f5cfd5a938937e92814601af1d429387a1ced` |
| `artifacts/dirac16complex/numerics/exp1/run_A1_K2_pos_Bm.csv` | committed exp1 output, compared byte for byte with the fresh run | 202 | 262664 | `ca38bffcd4789bc44c6ebad3df0355d52a2a12ce7ba1503a47a2c092e5c78f09` |
| `artifacts/dirac16complex/numerics/exp1/run_A1_K2_neg_Bp.csv` | committed exp1 output, compared byte for byte with the fresh run | 202 | 264329 | `60baea6eba425757bf21a4d8973e555e7d95c5ad9455bfc80d4e00a5393555c1` |
| `artifacts/dirac16complex/numerics/exp1/run_A1_K2_mix.csv` | committed exp1 output, compared byte for byte with the fresh run | 202 | 264666 | `dabaf32fe63166ed9cd8a0d46f41cd7966f6b53351243c5d81a8652625b391b3` |
| `artifacts/dirac16complex/numerics/exp1/run_A1_K0p5_pos_Bp_lambda0p5.csv` | committed exp1 output, compared byte for byte with the fresh run | 202 | 262567 | `2ff5aa5f634cf7d9a09952997a5e225c552100715b3476056f0136080cfb9a52` |
| `artifacts/dirac16complex/numerics/exp1/run_A2_K0_pos_Bp.csv` | committed exp1 output, compared byte for byte with the fresh run | 202 | 261696 | `65f3d5eb2ed50135d800847824b3e1578a00702152c3dd64c951ac878560e460` |
| `artifacts/dirac16complex/numerics/exp1/run_A2_K0_pos_Bm.csv` | committed exp1 output, compared byte for byte with the fresh run | 202 | 261919 | `d4d656dc8c8185dba84194d4d50a07e76492f1d2ef86ca27165878631a0eef1f` |
| `artifacts/dirac16complex/numerics/exp1/run_A2_K0_neg_Bp.csv` | committed exp1 output, compared byte for byte with the fresh run | 202 | 262824 | `682116b7fdfc4f177e9f2c52827e87e8f0a294e1f0a47850aeb0604b4a712443` |
| `artifacts/dirac16complex/numerics/exp1/run_A2_K0_mix.csv` | committed exp1 output, compared byte for byte with the fresh run | 202 | 264376 | `ec2e042b87ee574dc0ef3c32a5241e32cd9b18c3c0cd5eb1a492f05be1c47dfb` |
| `artifacts/dirac16complex/numerics/exp1/run_A2_K0p5_pos_Bp.csv` | committed exp1 output, compared byte for byte with the fresh run | 202 | 262583 | `073ba39a2b6fb46426a1771e2dd80c1b8d81fb6f4d4f9a0d90b9e756934c543c` |
| `artifacts/dirac16complex/numerics/exp1/run_A2_K0p5_pos_Bm.csv` | committed exp1 output, compared byte for byte with the fresh run | 202 | 262825 | `4866ad7cd5772608b92393d3d329fac935237ed19e18763ff070d0e70cfec956` |
| `artifacts/dirac16complex/numerics/exp1/run_A2_K0p5_neg_Bp.csv` | committed exp1 output, compared byte for byte with the fresh run | 202 | 264241 | `fe46e88017ffb9b47fa4c5828f25322273e60e00d387d92860c60a1ae370a5f3` |
| `artifacts/dirac16complex/numerics/exp1/run_A2_K0p5_mix.csv` | committed exp1 output, compared byte for byte with the fresh run | 202 | 264606 | `a932ea73d3487f1fd3eb4b1d5c4d64476312b10c32ff0d5223cb95174b81b6e8` |
| `artifacts/dirac16complex/numerics/exp1/run_A2_K2_pos_Bp.csv` | committed exp1 output, compared byte for byte with the fresh run | 202 | 262579 | `9fd75876efe3a60a5cb0a67e256f5cfd5a938937e92814601af1d429387a1ced` |
| `artifacts/dirac16complex/numerics/exp1/run_A2_K2_pos_Bm.csv` | committed exp1 output, compared byte for byte with the fresh run | 202 | 262664 | `ca38bffcd4789bc44c6ebad3df0355d52a2a12ce7ba1503a47a2c092e5c78f09` |
| `artifacts/dirac16complex/numerics/exp1/run_A2_K2_neg_Bp.csv` | committed exp1 output, compared byte for byte with the fresh run | 202 | 264329 | `60baea6eba425757bf21a4d8973e555e7d95c5ad9455bfc80d4e00a5393555c1` |
| `artifacts/dirac16complex/numerics/exp1/run_A2_K2_mix.csv` | committed exp1 output, compared byte for byte with the fresh run | 202 | 264666 | `dabaf32fe63166ed9cd8a0d46f41cd7966f6b53351243c5d81a8652625b391b3` |
| `artifacts/dirac16complex/numerics/exp1/run_A2_K0p5_pos_Bp_lambda0p5.csv` | committed exp1 output, compared byte for byte with the fresh run | 202 | 262567 | `2ff5aa5f634cf7d9a09952997a5e225c552100715b3476056f0136080cfb9a52` |
| `artifacts/dirac16complex/numerics/exp1/summary.json` | committed exp1 output, compared byte for byte with the fresh run | 1627 | 54498 | `f8886625011a35c5ea31c89ffb623e4c6b0678adc300fc4b725179808601272a` |
| `artifacts/dirac16complex/numerics/exp2/run_x0_0.csv` | committed exp2 output, compared byte for byte with the fresh run | 512 | 714882 | `a9ed3272c5ee7b96f76f056b2b0cb0b59a3e29ab7055510fed7aa3fe6ca9f71d` |
| `artifacts/dirac16complex/numerics/exp2/run_x0_m0p4.csv` | committed exp2 output, compared byte for byte with the fresh run | 512 | 716609 | `a2108e2cf1a09dee950e17444de835e2c8e2726f902de2ef34267fcc661d0b2f` |
| `artifacts/dirac16complex/numerics/exp2/run_x0_0p5.csv` | committed exp2 output, compared byte for byte with the fresh run | 512 | 714595 | `e3c0f829981298d2bb7bbcca2004c11b505db501a3d90327c01028638b05f7af` |
| `artifacts/dirac16complex/numerics/exp2/summary.json` | committed exp2 output, compared byte for byte with the fresh run | 411 | 16239 | `c8f7ecd95f7414f81e2569be7a41f2127d0c1cbd3a7a07b2c0dbcb667c43d5d0` |
| `artifacts/dirac16complex/numerics/exp3/run_x0_m0p462654_mu3.csv` | committed exp3 output, compared byte for byte with the fresh run | 243 | 372429 | `7f696ee4b840ecfbc7bcb313ec60ecc57a02f924af80a5bdd3dc265d7971d624` |
| `artifacts/dirac16complex/numerics/exp3/run_x0_m0p462654_mu7.csv` | committed exp3 output, compared byte for byte with the fresh run | 243 | 372389 | `97bfb6c736b0dfd3e94ffb076a4eccd5a762455c75bf6b96371668a82ab32ae5` |
| `artifacts/dirac16complex/numerics/exp3/run_x0_m0p433107_mu3.csv` | committed exp3 output, compared byte for byte with the fresh run | 249 | 381741 | `2849674de5ce63193399237b09a3e06722e7d615896805e459abeceef80b9505` |
| `artifacts/dirac16complex/numerics/exp3/run_x0_m0p433107_mu7.csv` | committed exp3 output, compared byte for byte with the fresh run | 249 | 381687 | `9fb641d7bc2d3646d46f80f74dc1778eb21255e476f0f4fd89854248ba856257` |
| `artifacts/dirac16complex/numerics/exp3/run_x0_m0p3_mu3.csv` | committed exp3 output, compared byte for byte with the fresh run | 284 | 436004 | `27b7cfd34446dc630fafb00f6b557e9168e186f4f97acf163c1b936baceb407b` |
| `artifacts/dirac16complex/numerics/exp3/run_x0_m0p3_mu7.csv` | committed exp3 output, compared byte for byte with the fresh run | 284 | 435954 | `c243b3eda126d81aa10c90dbdac06fcab56deb9373af3320c2a3001fb783dfa5` |
| `artifacts/dirac16complex/numerics/exp3/run_x0_m0p2_mu3.csv` | committed exp3 output, compared byte for byte with the fresh run | 322 | 494812 | `5a47dd6946a5b379faf44e99c4540f1df6b4f8899ccc915a25d5fd448a65b632` |
| `artifacts/dirac16complex/numerics/exp3/run_x0_m0p2_mu7.csv` | committed exp3 output, compared byte for byte with the fresh run | 322 | 494770 | `650ab9acc928664de88224e95e995a33601d741535844f9ff08f8d2e3689a9cb` |
| `artifacts/dirac16complex/numerics/exp3/run_x0_0_mu3.csv` | committed exp3 output, compared byte for byte with the fresh run | 482 | 739774 | `9dfdb94a2020081869e35ffc86e8676ce9b53a180a0625351219fcbad3708c63` |
| `artifacts/dirac16complex/numerics/exp3/run_x0_0_mu7.csv` | committed exp3 output, compared byte for byte with the fresh run | 482 | 739572 | `6bce853deeb8ebef9e07cdb40bccb4772299af233591480c631e5528541ed2bc` |
| `artifacts/dirac16complex/numerics/exp3/summary.json` | committed exp3 output, compared byte for byte with the fresh run | 1068 | 35847 | `7bfedf4bd5e5765c171dcc71896e4a9f481bfedfeafa6ddae04b924ca31081ee` |
| `artifacts/dirac16complex/numerics/exp4/thermal_grid.csv` | committed exp4 output, compared byte for byte with the fresh run | 49 | 10455 | `dcce4d2aa03beab13936921c280c71f463354c3734be005a36898ae76f0b8f10` |
| `artifacts/dirac16complex/numerics/exp4/thermal_modes.csv` | committed exp4 output, compared byte for byte with the fresh run | 2929 | 3256013 | `f9ae33f20d079cf679ecc3dffc528d78bf7dae937bf0be6245e5938dfeb6a5ed` |
| `artifacts/dirac16complex/numerics/exp4/thermal_spin.csv` | committed exp4 output, compared byte for byte with the fresh run | 245 | 271806 | `bee360bea87888d6e63ce44b615613a5360dba548879a56aa3a30666d2dee917` |
| `artifacts/dirac16complex/numerics/exp4/thermal_antiparticle.csv` | committed exp4 output, compared byte for byte with the fresh run | 62 | 68320 | `f41cdeacc9964f76d0a595eae4582678730b6db30c59cc843aabb3532329e30e` |
| `artifacts/dirac16complex/numerics/exp4/thermal_adiabatic_vacuum.csv` | committed exp4 output, compared byte for byte with the fresh run | 123 | 135966 | `bb594ca157c404c0d5284476ddd3e8597a6e2f259f9c2d97c221cf9556684ca3` |
| `artifacts/dirac16complex/numerics/exp4/thermal_eos.csv` | committed exp4 output, compared byte for byte with the fresh run | 62 | 29518 | `133bf3663fb730a958e531e07e6f9086ca8f2debbf3248705bfe59a5be485b8a` |
| `artifacts/dirac16complex/numerics/exp4/pair_grid.csv` | committed exp4 output, compared byte for byte with the fresh run | 65 | 9346 | `8634f58729c13ce4d8f8eddab46ebb0a40b1d7e161b780c347b3ebb3688ecf25` |
| `artifacts/dirac16complex/numerics/exp4/pair_modes.csv` | committed exp4 output, compared byte for byte with the fresh run | 2561 | 2844263 | `1d8a871be085ef8263ff712fda9fd6cb1e08c1ff2152e5c70898eba5b51d31aa` |
| `artifacts/dirac16complex/numerics/exp4/pair_antiparticle.csv` | committed exp4 output, compared byte for byte with the fresh run | 25 | 27040 | `07c5e7d1e7baf98fa76ba79874e33f3e8aeeb867e421d0c06e8e412761bf6ffb` |
| `artifacts/dirac16complex/numerics/exp4/pair_spectrum.csv` | committed exp4 output, compared byte for byte with the fresh run | 321 | 108014 | `be59b6901eaaa4498cd81342f70db6c94896cd6362381ff868b4409eebf1184f` |
| `artifacts/dirac16complex/numerics/exp4/pair_eos.csv` | committed exp4 output, compared byte for byte with the fresh run | 306 | 95318 | `209da35a1b488c686f9c6bb4f0de00746c8ad09ddd5c3036887b9b646399f4c1` |
| `artifacts/dirac16complex/numerics/exp4/pair_history.csv` | committed exp4 output, compared byte for byte with the fresh run | 36 | 5073 | `7497d740ea0ce72cd0b6579a2104e0fd3ae350018feb9d0228cf046961e69ea2` |
| `artifacts/dirac16complex/numerics/exp4/summary.json` | committed exp4 output, compared byte for byte with the fresh run | 814 | 30906 | `c648518ed5ba4693bf6d271de3ee294a330daf9f15e669e17fa43519c1a9f8ec` |
| `artifacts/dirac16complex/numerics/exp5/run_q0p05_Cp.csv` | committed exp5 output, compared byte for byte with the fresh run | 602 | 611355 | `6b3b0bfb210c25792d2cee266ba3e1a518398d3ae96f242d6f71a3da5eda2a27` |
| `artifacts/dirac16complex/numerics/exp5/run_q0p05_Cm.csv` | committed exp5 output, compared byte for byte with the fresh run | 602 | 613143 | `c97184ad5c60a787e84ebbdd32459090bd2a210e0301b8a2c8ad7225e93521d6` |
| `artifacts/dirac16complex/numerics/exp5/run_q0p1_Cp.csv` | committed exp5 output, compared byte for byte with the fresh run | 602 | 611476 | `f11b22c767edb9b15d822a7493abc8af4730d4bd0005048b7cf67a9ceae24c86` |
| `artifacts/dirac16complex/numerics/exp5/run_q0p1_Cm.csv` | committed exp5 output, compared byte for byte with the fresh run | 602 | 613109 | `4ba950feb743ba286f4989edb26ea7f591dbd6e1a8b1fe9486124bae40d93fd2` |
| `artifacts/dirac16complex/numerics/exp5/summary.json` | committed exp5 output, compared byte for byte with the fresh run | 219 | 7381 | `bbddd4d4e0303c72d8d13494e2f4a54a730f0687fdba54a240156c7b0cfb1746` |
| `artifacts/dirac16complex/numerics/exp3/fits.json` | committed EXP-3 analysis output, compared value by value | 2616 | 79212 | `84aad4a5e48b23588fca0b2b2328e3d6db6b9b0b94e35175caaaa41ba0e14b58` |
| `artifacts/dirac16complex/numerics/exp3/fits_scan.csv` | committed EXP-3 analysis output, compared value by value | 492 | 184799 | `d655595dacd053a348b069e8981f2b458d4cfe578d0a5c61fd9768fb3ad080f7` |
| `artifacts/dirac16complex/numerics/exp3/fits_mu_scan.csv` | committed EXP-3 analysis output, compared value by value | 51 | 10796 | `bfb7b1dcb0851b57f234416393e2527676438de107fd1940fb402a85a0202667` |

### 2.3 Outputs

| Output | Written by | Committed? | What it is |
| --- | --- | --- | --- |
| `build/notebook-run/exp1/` ... `exp5/` (62 files: the files listed above under `exp1` ... `exp5` except the checker reports and the analysis files) | the simulator, during every execution | no (scratch; `build/` is git-ignored) | the fresh CSV and JSON outputs of the five experiments |
| `build/notebook-run/exp3/fits.json`, `fits_scan.csv`, `fits_mu_scan.csv` | the EXP-3 analysis, during every execution | no (scratch) | the fresh fits |
| `artifacts/dirac16complex/numerics/figures/*.png` (17 files, listed below) | every execution | **yes: overwritten** | the figures |
| `build/nbconvert/dirac16complex_dark_sector.ipynb` | `python -m nbconvert ... --output-dir build/nbconvert` | no (scratch) | Jupyter's executed copy |
| `notebooks/dirac16complex_dark_sector.ipynb` | `python notebooks/run_notebook.py ...` (only if every cell succeeds) | **yes: overwritten** | the executed notebook, outputs written in place |
| `artifacts/dirac16complex/numerics/notebook-report.json` | `python notebooks/check_notebook.py ... --report ...` | **yes: overwritten** | the audit record |

The committed outputs that an execution rewrites, with their sha256 (a correct run on Windows rewrites every one of them with exactly these bytes):

| File | Bytes | sha256 |
| --- | --- | --- |
| `artifacts/dirac16complex/numerics/figures/exp1_einstein_requirement.png` | 108698 | `42475d956a3c63fbbef0cea4da32ec5d886c4b7a00fc9f46075baea2f84b3191` |
| `artifacts/dirac16complex/numerics/figures/exp1_frozen_observables.png` | 135941 | `719b7bc3220da6a7a3c85829b8848fa17c97e4b27c9b0d53fc40af98c8e6d934` |
| `artifacts/dirac16complex/numerics/figures/exp2_eos_constraint.png` | 88921 | `36207840f68c0a2b8f1bfefa240fc7a0b5c382c354b7876623eb50051b321638` |
| `artifacts/dirac16complex/numerics/figures/exp2_hubble.png` | 142345 | `af815eb061bcd44d93b39d897c15c6e4a3a81cc1fd5315322db2ab7620fff2c8` |
| `artifacts/dirac16complex/numerics/figures/exp2_volume_density.png` | 108499 | `097750e8b52828ee25a700e3698db11c1ca206b39326ab3f349eb7c187302e19` |
| `artifacts/dirac16complex/numerics/figures/exp3_distance_modulus.png` | 97782 | `014181b9e5526af14a120a7ffdde1550057c20ca5f985c15c2be8241b03112b2` |
| `artifacts/dirac16complex/numerics/figures/exp3_ke_pe.png` | 68273 | `71275e8777920ef2405ea5e1b5d45e23c5bd8d8aa6d7a3f6e2fa25e4dea0e8de` |
| `artifacts/dirac16complex/numerics/figures/exp3_rho_psi.png` | 83919 | `93d296d6b58dbd0f0df9e706099b599620403b494eb9ad813faaa6bb64933ea5` |
| `artifacts/dirac16complex/numerics/figures/exp3_w0wa_plane.png` | 70171 | `16afd9a42370d3343d60a9f6cea453f9eefa280bf56e64d9cc30d52a03df96a1` |
| `artifacts/dirac16complex/numerics/figures/exp3_w_of_a.png` | 67374 | `c5d9e35378948d87fc6978c894628dcba93a9b9bf9f176a68850ee19a290a3f2` |
| `artifacts/dirac16complex/numerics/figures/exp4_pair_density.png` | 89313 | `30031fb2982d0a358c0999ec86a14a5db369abf02414b9bc6200bced05a950e9` |
| `artifacts/dirac16complex/numerics/figures/exp4_pair_spectra.png` | 86685 | `41e136628e5c70d4709687ece0c46807825be80b6ec07256d7ba6786e293151f` |
| `artifacts/dirac16complex/numerics/figures/exp4_thermal_scaling.png` | 48392 | `0db10806f00d3a706b131586d0a191cf6c4b786dc5d5b6ceaa4f158022aafa04` |
| `artifacts/dirac16complex/numerics/figures/exp4_thermal_split.png` | 39718 | `d4b8ac3c2c18637e0f2f7a70722b7795091b08180ae61a9288af6c15845dfd1e` |
| `artifacts/dirac16complex/numerics/figures/exp4_thermal_w.png` | 76158 | `0de3ee0fc58bbcdd438313aa77c14789b4ec43a0c41ac505396ea4e39cc5fdad` |
| `artifacts/dirac16complex/numerics/figures/exp5_growth.png` | 74471 | `b5c7546f94f6226e2c99bd1bbbf62af330b94ef5d20c1b13a93fc7a6b453f38f` |
| `artifacts/dirac16complex/numerics/figures/exp5_krein.png` | 64111 | `78570341b44825997c549a14d21a44733aab9897f7ad4c428ce54bdec53a28df` |
| `artifacts/dirac16complex/numerics/notebook-report.json` | 17415 | `7cf06b0f3693819aeed61e018ebb455387b642e9062f4f14e70c9512d71334cb` |
| `notebooks/dirac16complex_dark_sector.ipynb` | 2149978 | `5cd2befc1862041c0047c3d38db1dcc182aa47dde8db0cd571a2023fbc9ac5f0` |

## 3. How to run it

These instructions are complete. They were executed literally on Windows 11 (Part 6); the macOS and Linux commands are the standard equivalents and were not executed on 2026-10-02.

### 3.1 What you need

* A computer with Windows 10 or 11, macOS or Linux, about 1.5 GB of free disk space (the clone needs about 510 MB including its git history, the private Python environment of Part 3.6 about 440 MB, the engine 80 MB, the build 16 MB, the scratch outputs 25 MB) and an internet connection for the downloads (the notebook itself uses no network). The processor matters for one detail: the verified computers have x86-64 processors (Intel or AMD); on a Mac with an Apple processor (M1 or later) read the notes for Apple silicon in Parts 3.7 and 3.8.
* **Git**, to download the repository and the engine.
* **Rust** (the `cargo` and `rustc` programs) and, on Windows, Microsoft's C++ build tools, which provide the linker `link.exe`.
* **Python 3.11 or newer** (3.14.5 was used) with the packages listed in Part 3.6.
* No Wolfram software is needed.

### 3.2 Install Git

* Windows: install "Git for Windows" from https://git-scm.com/download/win (accept the defaults; it also installs "Git Bash"), or in PowerShell: `winget install --id Git.Git -e`.
* macOS: in Terminal, `xcode-select --install` (installs git with Apple's command line tools).
* Linux: `sudo apt install git` (Debian, Ubuntu) or `sudo dnf install git` (Fedora).

Check: `git --version` prints a version (2.51.2 was used).

### 3.3 Install Rust

* Windows: download and run `rustup-init.exe` from https://rustup.rs (or `winget install Rustlang.Rustup`). Accept the default toolchain `stable-x86_64-pc-windows-msvc`. If it says that the Visual Studio C++ build tools are missing, let it install them (the "Desktop development with C++" workload). Close and reopen PowerShell afterwards.
* macOS: `xcode-select --install` (the C linker), then `curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh` and `source "$HOME/.cargo/env"`.
* Linux: `sudo apt install build-essential` (the C linker; Fedora: `sudo dnf install gcc`), then `curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh` and `source "$HOME/.cargo/env"`.

Check: `cargo --version` and `rustc --version`. The verification used cargo 1.91.1 and rustc 1.91.1. To use exactly that compiler: `rustup toolchain install 1.91.1`, and build with `cargo +1.91.1 build --release` instead of `cargo build --release` in Part 3.8.

### 3.4 Install Python

* Windows: install Python 3.14 from https://www.python.org/downloads/ and tick "Add python.exe to PATH" in the first window of the installer (or `winget install Python.Python.3.14`). Close and reopen PowerShell.
* macOS: the installer from https://www.python.org/downloads/ (or `brew install python@3.14`).
* Linux: your distribution's Python 3.11 or newer with its venv module, for example `sudo apt install python3 python3-venv`.

Check: `python --version` (Windows) or `python3 --version` (macOS, Linux) prints 3.11 or newer.

### 3.5 Download the repository into a SHORT folder

On Windows the full path of the repository folder must be at most about 150 characters long. The build writes files 103 characters deeper (for example `studies\dirac16complex_cosmology\target\release\deps\libdirac16complex_cosmology-20513573899aa199.rlib`), and the Microsoft linker cannot open a path of 260 characters or more. This was observed on 2026-10-02 (Part 6): a clone at a 161-character path failed with `LINK : fatal error LNK1104: cannot open file ...rlib`. `C:\src\Dirac_claude` is fine.

Windows PowerShell:

```
New-Item -ItemType Directory -Force C:\src | Out-Null
Set-Location C:\src
git clone https://github.com/once-ere/Dirac_claude.git
Set-Location C:\src\Dirac_claude
```

macOS and Linux (Terminal), or Git Bash on Windows:

```
mkdir -p ~/src && cd ~/src
git clone https://github.com/once-ere/Dirac_claude.git
cd Dirac_claude
```

Every command below is typed in this folder, the **repository root** (the folder that contains `notebooks`, `studies` and `scripts`), unless it says otherwise. To reproduce exactly the verified state, also run `git checkout 72fc9ffc4a10328080a5778cc8a8c6e689aeaca6`, the commit of the latest verification (this leaves you on a "detached HEAD", which is fine for running; the earlier verified commit `c2b33ccd16edb9c8b46585d0db6b2911a1f5d84e` contains the same files of this set).

### 3.6 Create a private Python environment and install the packages

A private environment (a "venv") keeps these package versions away from the rest of your computer. Create it **outside** the repository folder (a `.venv` folder inside the repository would show up in `git status`).

Windows PowerShell:

```
python -m venv "$HOME\venvs\dirac16"
& "$HOME\venvs\dirac16\Scripts\Activate.ps1"
```

If PowerShell answers "running scripts is disabled on this system", run `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass` (it applies to this window only) and repeat the second line.

Git Bash on Windows:

```
python -m venv ~/venvs/dirac16
source ~/venvs/dirac16/Scripts/activate
```

macOS and Linux:

```
python3 -m venv ~/venvs/dirac16
source ~/venvs/dirac16/bin/activate
```

The prompt now starts with `(dirac16)`, and `python` means the environment's Python on every system. Then, from the repository root, type these three commands (the second one is long: type or paste it as one single line):

```
python -m pip install --upgrade pip
python -m pip install -r requirements-stage3.txt pillow==12.2.0 contourpy==1.3.3 cycler==0.12.1 fonttools==4.63.0 kiwisolver==1.5.0 packaging==26.2 pyparsing==3.3.2 python-dateutil==2.9.0.post0 ipython==9.7.0 jupyter_client==8.6.3 jupyter_core==5.9.1 pyzmq==27.1.0 tornado==6.5.2
python -m pip install nbconvert==7.16.6 jupyterlab==4.4.10
```

`requirements-stage3.txt` pins `numpy==2.4.6`, `matplotlib==3.11.0`, `sympy==1.14.0`, `nbformat==5.10.4`, `nbclient==0.10.2` and `ipykernel==7.1.0`. The rest of the second command fixes the versions of matplotlib's helper packages (Pillow, the package with which matplotlib writes the PNG files, and contourpy, cycler, fonttools, kiwisolver, packaging, pyparsing and python-dateutil) and of the packages of the Jupyter kernel (IPython, jupyter_client, jupyter_core, pyzmq, tornado); the third command adds Jupyter's executor nbconvert and JupyterLab. Every one of these 21 named packages then has exactly the version of the verification computer (Part 6.1). Without the extra pins of the second command pip would install the newest helper versions (on 2026-10-02, for example, Pillow 12.3.0 instead of 12.2.0), and a future Pillow could change the bytes of the PNG files. The further packages that pip installs because the named ones need them (80 on 2026-10-02, for example jupyter_server, jsonschema and traitlets) are not fixed: pip takes their newest compatible versions. On 2026-10-02, 50 of them had newer versions than on the verification computer, and every output of the notebook was still byte-identical (Part 6.5). On 2026-10-07 the first command upgraded pip from 26.1.1 to 26.2.1, the environment again held 101 packages (the 21 named ones in exactly the versions of Part 6.1, and 80 further ones, 51 of them newer than on the verification computer, for example jupyter_server 2.21.1, traitlets 5.16.1, pygments 2.21.0), and every output was again byte-identical (Part 6.6). The notebook needs numpy and matplotlib; the two executors need nbformat, nbclient, nbconvert and ipykernel; JupyterLab is only for the interactive route (Part 3.13). With other versions of the named packages the assertions still pass, but the figures, and therefore the executed notebook, may then differ in their bytes. pip downloads about 86 MB of packages, and the environment then occupies about 440 MB. Every time you open a new terminal, activate the environment again (the second command of your system above) before you run the notebook.

### 3.7 Download the solver engine

Windows PowerShell:

```
pwsh -NoProfile -File scripts/setup_solver.ps1 -Platform win11
```

(With the older Windows PowerShell 5.1 instead of PowerShell 7: `powershell -ExecutionPolicy Bypass -File scripts/setup_solver.ps1 -Platform win11`.)

Git Bash on Windows, macOS and Linux:

```
bash scripts/setup_solver.sh win11
```

Always pass `win11`, also on macOS and Linux. The committed outputs were produced with the Windows 11 engine, and only that engine reproduces them byte for byte. The macOS and Linux engines (`macos`, `linux`, or no argument) contain a different mathematical library: every check of the simulator still passes with them, but the notebook stops at the assertion `fresh_program_outputs_byte_identical`. **Apple silicon** (a Mac with an M1 or later processor): pass `win11` there too, but know that no recorded verification has run this combination. All recorded byte-for-byte reproductions were made on x86-64 processors (Windows 11, and Ubuntu on the same x86-64 computer); whether the program reproduces the committed files bit for bit on an Apple processor has not been checked. The build there also prints a warning about `+fma` (Part 3.8). On Windows run the `.sh` script only from Git Bash. In PowerShell or cmd the word `bash` can start the WSL Linux subsystem instead (`C:\Windows\System32\bash.exe`); use the `.ps1` script there.

### 3.8 Build the simulator

All systems:

```
cd studies/dirac16complex_cosmology
cargo build --release
cd ../..
```

The build must be started inside `studies/dirac16complex_cosmology` (or anywhere below the repository root), so that cargo finds the repository's `.cargo/config.toml`, which adds the compiler option `-C target-feature=+fma` that the committed numbers assume. The program is written to `studies/dirac16complex_cosmology/target/release/dirac16complex_cosmology.exe` (Windows) or `.../dirac16complex_cosmology` (macOS, Linux), and that is where the notebook looks for it.

Two environment variables must not be set while you build. `RUSTFLAGS` would replace the `+fma` option. `CARGO_TARGET_DIR` would make cargo write the program into another folder, where the notebook does not find it (Part 3.14). They are normally not set. To be sure, remove both for the current window before you type the three commands above; if you have already built, remove them and build again. In PowerShell, type `Remove-Item Env:RUSTFLAGS, Env:CARGO_TARGET_DIR -ErrorAction SilentlyContinue`. In Git Bash, macOS and Linux, type `unset RUSTFLAGS CARGO_TARGET_DIR`. Neither command prints anything.

**Apple silicon.** `+fma` is the name of an instruction-set extension of x86-64 processors (Intel and AMD). rustc has no option of that name for the ARM processors of Apple-silicon Macs, so there it ignores the option and prints a warning. The warning does not stop the build (Part 4.2).

### 3.9 Execute the notebook with Jupyter's executor (headless)

This is the standard way to run a notebook without opening it. Jupyter starts a Python "kernel" (the program that executes the cells), runs every cell from top to bottom and writes an executed copy into `build/nbconvert/`; your notebook file itself is not changed. All systems, one line:

```
python -m nbconvert --to notebook --execute notebooks/dirac16complex_dark_sector.ipynb --output-dir build/nbconvert --ExecutePreprocessor.timeout=3600 --ExecutePreprocessor.startup_timeout=600
```

`timeout=3600` allows each cell one hour (the EXP-4 cell needs about two minutes); `startup_timeout=600` gives the kernel ten minutes to start instead of 60 seconds, which matters on a busy computer. If the `jupyter` command is on your PATH, `jupyter nbconvert` followed by the same options is the same command.

### 3.10 Execute it with the repository's runner (writes the outputs into the notebook)

```
python notebooks/run_notebook.py notebooks/dirac16complex_dark_sector.ipynb
```

This runner needs only the Python standard library besides numpy and matplotlib. It executes every code cell in order, shows everything the cells print while they run, and writes the outputs (text and images) back into `notebooks/dirac16complex_dark_sector.ipynb`, **but only if every cell succeeded**. Add `--quiet` before the notebook path to suppress the live output.

### 3.11 Audit both executions

```
python notebooks/check_notebook.py notebooks/dirac16complex_dark_sector.ipynb --also build/nbconvert/dirac16complex_dark_sector.ipynb --report artifacts/dirac16complex/numerics/notebook-report.json
```

The auditor checks 11 rules on each executed copy: the how-to-run text is present, there are no cross-references, every code cell has an explanation of at least 80 characters before it, the required headings exist, nothing interactive, execution counts 1 to 8, no error output and a passed gauntlet, every printed figure hash equals the PNG on disk, kernel `python3`, the determinism settings, and validity against the notebook file format. It then checks that both executions printed identical gauntlet results and figure hashes, and writes the report.

### 3.12 Confirm that nothing changed

```
git status --porcelain
```

On Windows with the versions above this prints **nothing**: the executed notebook, the 17 figures and the report were rewritten with exactly their committed bytes. The scratch folders `build/`, `vendor/` and `target/` are git-ignored and therefore not listed.

To compare the 65 fresh files in `build/notebook-run/` with the committed ones yourself, Windows PowerShell:

```
$run = (Resolve-Path build/notebook-run).Path; Get-ChildItem $run -Recurse -File | ForEach-Object { $rel = $_.FullName.Substring($run.Length + 1); $ref = Join-Path 'artifacts/dirac16complex/numerics' $rel; if ((Get-FileHash $_.FullName).Hash -eq (Get-FileHash $ref).Hash) { "identical  $rel" } else { "DIFFERENT  $rel" } }
```

Git Bash, macOS and Linux:

```
(cd build/notebook-run && find . -type f | sort) | while read -r f; do if cmp -s "build/notebook-run/$f" "artifacts/dirac16complex/numerics/$f"; then echo "identical  $f"; else echo "DIFFERENT  $f"; fi; done
```

Both print 65 lines, all `identical`.

### 3.13 Run it interactively in JupyterLab (optional)

```
python -m jupyterlab notebooks/dirac16complex_dark_sector.ipynb
```

A browser tab opens with the notebook (if none opens, copy the address that starts with `http://localhost:8888/lab?token=` from the terminal into your browser). If you are asked to choose a kernel, choose **Python 3 (ipykernel)**. Click into the first cell and press **Shift+Enter** repeatedly (each press runs one cell and moves to the next), or use the menu Run, Run All Cells. A cell that is running shows `[*]` at its left; the EXP-4 cell takes about two minutes. The notebook finds the repository by itself, although JupyterLab starts it in the folder `notebooks`. Saving the notebook from JupyterLab (Ctrl+S) rewrites the file with JupyterLab's own metadata and the new outputs, so `git status` will normally list it as modified afterwards; Part 5.6 shows how to restore it. If you do not want to change the file, close the tab without saving. To stop JupyterLab, press Ctrl+C twice in the terminal.

### 3.14 If something fails

| What you see | Cause and fix |
| --- | --- |
| `LINK : fatal error LNK1104: cannot open file '...\target\release\deps\libdirac16complex_cosmology-....rlib'` during `cargo build` (Windows) | the folder path is too long for the Microsoft linker; clone the repository again into a short folder such as `C:\src` (Part 3.5) |
| `error: linker 'link.exe' not found` (Windows) or `linker 'cc' not found` (Linux) | the C/C++ build tools are missing; install them (Part 3.3) |
| `error: failed to load manifest for dependency 'cvode_rs'` ... `failed to read ...vendor\rustSolveIt\sundials_rs\crates\cvode_rs\Cargo.toml` ... `The system cannot find the path specified. (os error 3)` | the engine has not been downloaded; run Part 3.7, then build again |
| `vendor/rustSolveIt is at <sha>, expected a8fdff45...; remove it and rerun`, or `vendor/rustSolveIt is an incomplete checkout` | an engine of another platform or an interrupted download is present; delete the folder `vendor/rustSolveIt` (PowerShell `Remove-Item -Recurse -Force vendor/rustSolveIt`, other shells `rm -rf vendor/rustSolveIt`) and run Part 3.7 again |
| ``warning: unknown and unstable feature specified for `-Ctarget-feature`: `fma` `` and `'+fma' is not a recognized feature for this target (ignoring feature)` during `cargo build` (Mac with Apple silicon) | expected on ARM processors: `+fma` is an x86-64 option, and rustc ignores it there (Part 3.8). It is only a warning and should not stop the build (Part 4.2); wait for the line `Finished ...` |
| `FAIL notebooks\dirac16complex_dark_sector.ipynb (cell 1): RuntimeError('dirac16complex_cosmology binary not found - build it first: ...')` and `0 ok, 1 failed` | the notebook looks for the program only in `studies/dirac16complex_cosmology/target/release/`, or at the full path given in the environment variable `DIRAC16_BIN`. One cause is that the simulator has not been built yet: run Part 3.8. The other is that it was built into another folder because the environment variable `CARGO_TARGET_DIR` was set. Remove the variable (PowerShell `Remove-Item Env:CARGO_TARGET_DIR`, other shells `unset CARGO_TARGET_DIR`) and run Part 3.8 again; this was tested on 2026-10-02 (Part 6.5). Setting `DIRAC16_BIN` to the full path of the program built elsewhere also works, and with a program built as in Part 3.8 every check still passes. But the notebook then prints that path in its line `simulator  : ...`. If the program lies outside the repository, that is the full path, including the name of your user folder. The notebook that the runner writes then differs from the committed one in that one line, and `git status --porcelain` lists `notebooks/dirac16complex_dark_sector.ipynb` as modified. The figures, the report and all 65 scratch files are not affected. Restore the notebook with `git checkout -- notebooks/dirac16complex_dark_sector.ipynb` |
| `RuntimeError: start the notebook inside the Dirac_claude repository` | the command was started outside the repository; `cd` to the repository root |
| `The term 'jupyter' is not recognized` (PowerShell), `jupyter: command not found`, or `Jupyter command 'jupyter-nbconvert' not found.` | the folder with the Jupyter commands is not on your PATH (this happens when packages were installed with `pip install --user`); use `python -m nbconvert ...` and `python -m jupyterlab ...` as written above, or activate the private environment of Part 3.6 |
| `Python was not found; run without arguments to install from the Microsoft Store` (Windows), or typing `python` opens the Microsoft Store | Python is not installed or not on PATH; install it as in Part 3.4 with "Add python.exe to PATH" ticked, then close and reopen PowerShell |
| `No module named nbconvert` / `No module named numpy` | the packages are not installed in the Python you are using; activate the environment and repeat the `pip install` lines of Part 3.6 |
| `nbclient.exceptions.CellExecutionError` with `ModuleNotFoundError: No module named 'numpy'` in the first code cell (`---> 11 import numpy as np`), printed by nbconvert, although `python -c "import numpy"` works | Jupyter ran the cells in another Python installation. nbconvert starts the `python3` kernel definition that it finds first, a small file called `kernel.json`. The definition that ipykernel installs names just `python`, and Jupyter replaces that word by the Python that runs nbconvert. So normally the cells run in your Python, whichever `python` comes first on PATH. The error appears when another Python installation has registered its own `python3` kernel in your personal Jupyter folder, for example with `python -m ipykernel install --user`. Its `kernel.json` contains the full path of that other Python, and that Python has no numpy. To see which definition is used, type `python -m jupyter_client.kernelspecapp list`. It prints the folder of the `python3` kernel; the first entry of `"argv"` in the file `kernel.json` in that folder is the Python the cells run in. Any one of these four fixes it. (a) Run nbconvert in the activated private environment of Part 3.6: there Jupyter prefers the environment's own definition. This does not help if the environment variable `JUPYTER_PATH` is set, or `JUPYTER_PREFER_ENV_PATH` is set to 0; remove them for the window (PowerShell `Remove-Item Env:JUPYTER_PATH, Env:JUPYTER_PREFER_ENV_PATH -ErrorAction SilentlyContinue`, other shells `unset JUPYTER_PATH JUPYTER_PREFER_ENV_PATH`). (b) Register the kernel again for the Python you use: `python -m ipykernel install --user`. This replaces the personal `python3` definition with one that names your Python. (c) If nothing else needs the other definition, remove it: `python -m jupyter_client.kernelspecapp remove python3 -y`. (d) Use the runner of Part 3.10, which needs no kernel and always uses the Python that runs it. All four were tested on 2026-10-02 (Part 6.5) |
| `ERROR: ResolutionImpossible` from pip, with `some packages in these conflicts have no matching distributions available for your environment: anyio` (or another package name), after an earlier line `WARNING: Skipping page https://pypi.org/simple/anyio/ because the GET request got Content-Type: Unknown` | a temporary download failure of the package index, not a real conflict between versions (it happened once on 2026-10-02). Type the same pip command again |
| `WARNING: Cache entry deserialization failed, entry ignored` (several times) during the second pip command | harmless: pip's download cache on your computer was written by an older pip version, so pip ignores those entries and downloads the packages again. Seen in both runs of 2026-10-07 after pip had upgraded itself to 26.2.1; both installations succeeded and `python -m pip check` printed `No broken requirements found.` |
| `RuntimeError: Kernel didn't respond in 60 seconds` | the computer was too busy when the kernel started; keep the option `--ExecutePreprocessor.startup_timeout=600` and run again |
| `RuntimeWarning: Proactor event loop does not implement add_reader family of methods required for zmq` (Windows, nbconvert) | harmless; it is printed on every Windows run and changes nothing |
| `FAIL - fresh_program_outputs_byte_identical` and an `AssertionError` in the gauntlet cell | the simulator's files differ from the committed ones: the engine is not the `win11` one, `RUSTFLAGS` replaced the `+fma` option, or the source was changed. Run `git status`, delete `vendor/rustSolveIt`, run Part 3.7 with `win11` and Part 3.8 again. On a Mac with Apple silicon the cause may instead be the processor, because no recorded verification has tested that combination (Part 3.7). If there the simulator printed every one of its self-checks as `PASS` and only this assertion fails, your installation is not broken: the committed files were produced on an x86-64 processor |
| `Illegal instruction` or the simulator crashes immediately (very old x86 processors) | the `+fma` option needs a processor with FMA instructions (Intel since 2013, AMD since 2012) |
| `UnicodeEncodeError` while output is printed | set `PYTHONUTF8=1` (PowerShell `$env:PYTHONUTF8 = "1"`, other shells `export PYTHONUTF8=1`) and run again |
| `git status` lists the 17 figures and the notebook as modified on macOS or Linux | expected if the gauntlet passed: matplotlib writes PNG files whose bytes differ between operating systems (Part 4.7); restore with Part 5.6 |

## 4. Expected output

### 4.1 Downloading the engine (Part 3.7)

```
solver_platform=win11
solver_commit=a8fdff459adfe181573d7924b18bffbdf378fdb3
solver_setup=OK
```

Exit code 0. A second call prints `solver_setup=ALREADY-PRESENT` instead of the last line.

### 4.2 Building (Part 3.8)

```
   Compiling sundials_core v7.8.0 (...)
   Compiling cvode_rs v7.8.0 (...)
   Compiling dirac16complex_cosmology v0.1.0 (...)
    Finished `release` profile [optimized] target(s) in 7.97s
```

On x86-64 processors (Intel and AMD: most Windows PCs, Intel Macs, most Linux PCs) there is no warning (the crate turns every warning about its own code into an error), and the exit code is 0. On a Mac with Apple silicon, expect a warning about `+fma` in addition; it should not stop the build. This was not run on a Mac. What was run, on 2026-10-02 on the verification computer with rustc 1.91.1, is the compilation of a minimal program for Apple silicon (target `aarch64-apple-darwin`; Part 6.5). It printed exactly these lines and exited with code 0, and the same happened for Linux on ARM processors (target `aarch64-unknown-linux-gnu`):

```
warning: unknown and unstable feature specified for `-Ctarget-feature`: `fma`
  |
  = note: it is still passed through to the codegen backend, but use of this feature might be unsound and the behavior of this feature can change in the future
  = help: consider filing a feature request

'+fma' is not a recognized feature for this target (ignoring feature)
'+fma' is not a recognized feature for this target (ignoring feature)
warning: 1 warning emitted
```

In a cargo build these lines may appear once for each of the three compiled crates, and cargo prints its own summary instead of the last line. This warning is not about the crate's own code, so the crate's rule against warnings does not turn it into an error. rustc still exited with code 0 when the minimal program contained `#![deny(warnings)]`, as the crate does, and also with `-D warnings` on the command line.

### 4.3 Jupyter's executor (Part 3.9)

nbconvert prints only its own progress, not the notebook's output. On Windows:

```
[NbConvertApp] Making directory build/nbconvert
[NbConvertApp] Converting notebook notebooks/dirac16complex_dark_sector.ipynb to notebook
C:\...\site-packages\zmq\_future.py:718: RuntimeWarning: Proactor event loop does not implement add_reader family of methods required for zmq. ...
  self._get_loop()
[NbConvertApp] Writing 2153532 bytes to build\nbconvert\dirac16complex_dark_sector.ipynb
```

The first line appears only when the folder does not exist yet; the two warning lines appear only on Windows; macOS and Linux print `build/nbconvert/...` with forward slashes. The number in the last line counts characters (on Windows the file on disk is larger, because every line ends in CR LF), and it is slightly different in every run: it was 2153532 in run 1 and 2153425 in run 2 (and 2153599 and 2153686 in the two runs of 2026-10-07), because the kernel splits the printed text into a different number of pieces depending on timing. Exit code 0. The notebook's own output is inside the copy: open it in JupyterLab or audit it (Part 3.11).

### 4.4 The repository's runner (Part 3.10)

The runner shows everything the cells print, in this order. The driver cell prints four lines (the repository was found, without printing its folder name; the simulator `studies/dirac16complex_cosmology/target/release/dirac16complex_cosmology.exe`, without `.exe` on macOS and Linux, or the path given in `DIRAC16_BIN` if that environment variable is set (Part 4.7); the output folder `build/notebook-run`; the fixture's sha256 `8b4f15462ca4d61ef6ec0e72f04c8a77d23ce8bcabc9b6ce19f921c90e02653b`) and then the six algebra lines, each ending in `max deviation = 0.0e+00`. `print-config` prints 30 configuration lines and `SUCCESS`. Then each experiment prints `== expN ==`, its simulator self-checks, a statistics line and `SUCCESS`, followed by the notebook's comparison line:

```
exp1: solver_steps=33866 rhs_evaluations=34950 files=29 verdict=SUCCESS
SUCCESS
exp1: 29/29 freshly written files are byte-identical to artifacts/dirac16complex/numerics/exp1/
exp2: solver_steps=1779784 rhs_evaluations=1781396 files=4 verdict=SUCCESS
SUCCESS
exp2: 4/4 freshly written files are byte-identical to artifacts/dirac16complex/numerics/exp2/
exp3: solver_steps=6074 rhs_evaluations=10115 files=11 verdict=SUCCESS
SUCCESS
exp3: 11/11 freshly written files are byte-identical to artifacts/dirac16complex/numerics/exp3/
check_count=10
failed_check_count=0
exp3-analysis: 3/3 freshly written files equal the committed ones value by value (relative 1e-06, absolute 1e-08) in artifacts/dirac16complex/numerics/exp3/
exp4: solver_steps=339071692 rhs_evaluations=511425232 files=13 verdict=SUCCESS
SUCCESS
exp4: 13/13 freshly written files are byte-identical to artifacts/dirac16complex/numerics/exp4/
exp5: solver_steps=2548 rhs_evaluations=4800 files=5 verdict=SUCCESS
SUCCESS
exp5: 5/5 freshly written files are byte-identical to artifacts/dirac16complex/numerics/exp5/
```

Each experiment cell also prints its recomputed numbers and one line `figure <name>.png sha256 <hash>` per figure (17 in all, with the hashes of the table in Part 2.3). The gauntlet prints 71 lines that begin with `PASS - `, from `PASS - all_runs_success: 7 program runs, every one exited 0 (simulator runs ended with SUCCESS)` to `PASS - prose_numbers_match_reports: 78 numbers quoted in the markdown re-read from the reports`. The runner ends with (Windows prints the backslash; macOS and Linux print `notebooks/...`):

```
ALL CHECKS PASSED
ok notebooks\dirac16complex_dark_sector.ipynb (8 cells)
1 ok, 0 failed
```

Exit code 0. If a cell fails, the runner prints `FAIL <notebook> (cell <n>): <error>` and `0 ok, 1 failed`, exits with code 1 and leaves the notebook file unchanged.

### 4.5 The audit (Part 3.11)

```
ok notebooks\dirac16complex_dark_sector.ipynb: all structure and execution rules pass (23 cells, 8 code cells, 71 gauntlet checks, 17 figures)
ok build\nbconvert\dirac16complex_dark_sector.ipynb: all structure and execution rules pass (23 cells, 8 code cells, 71 gauntlet checks, 17 figures)
ok cross-check: both executions printed identical gauntlet results and figure hashes
wrote artifacts/dirac16complex/numerics/notebook-report.json (verdict SUCCESS)
```

Exit code 0 (1 if any rule fails; each failing rule is then listed as `  - R<n>: ...`).

### 4.6 Check counts in one place

| Where | Count |
| --- | --- |
| driver cell, exact algebra | 6 lines, all `0.0e+00` |
| simulator self-checks (`PASS - ` lines) | 69: exp1 10, exp2 15, exp3 14, exp4 23, exp5 7; 6 `SUCCESS` lines (print-config and 5 experiments) |
| EXP-3 analysis | 10 `check_...=true`, `check_count=10`, `failed_check_count=0` |
| fresh files equal to the committed ones | 62 of 62 byte-identical (simulator), 3 of 3 value by value (analysis; in fact byte-identical) |
| figures | 17, each hash printed and re-read |
| gauntlet | 71 of 71 `PASS`, then `ALL CHECKS PASSED` |
| numbers quoted in the text and re-read from the reports | 78 |
| auditor | 11 rules on each of 2 executions, plus the cross-check; verdict `SUCCESS` |
| all `PASS - ` lines of one execution | 140, no `FAIL` |

### 4.7 The output files and how to check each

* `notebooks/dirac16complex_dark_sector.ipynb` (after Part 3.10): sha256 `5cd2befc1862041c0047c3d38db1dcc182aa47dde8db0cd571a2023fbc9ac5f0`, 2149978 bytes. Check: `git status --porcelain` does not list it, or compute the hash (PowerShell `Get-FileHash notebooks/dirac16complex_dark_sector.ipynb`, which prints the hash in capitals; Git Bash and Linux `sha256sum notebooks/dirac16complex_dark_sector.ipynb`; macOS `shasum -a 256 notebooks/dirac16complex_dark_sector.ipynb`).
* The 17 figures: the hashes of Part 2.3; `git status --porcelain` does not list them.
* `artifacts/dirac16complex/numerics/notebook-report.json`: sha256 `7cf06b0f3693819aeed61e018ebb455387b642e9062f4f14e70c9512d71334cb`. Its summary:

  ```
  python -c "import json; r = json.load(open('artifacts/dirac16complex/numerics/notebook-report.json', encoding='utf-8')); print(r['verdict'], r['gauntlet']['passed'], 'of', r['gauntlet']['count'], 'gauntlet checks,', len(r['figures']), 'figures,', len(r['executions']), 'executions')"
  ```

  prints `SUCCESS 71 of 71 gauntlet checks, 17 figures, 2 executions`.
* `build/notebook-run/`: 65 files, all byte-identical to the committed files of the same name in `artifacts/dirac16complex/numerics/` (commands in Part 3.12).
* `build/nbconvert/dirac16complex_dark_sector.ipynb`: about 2.1 MB. It is never byte-identical to the committed notebook, because nbconvert records the start and end time of every cell, writes the kernel's full `language_info` (including the Python version) and, on Windows, writes CRLF line endings. Its content is checked by the auditor (Part 3.11), which requires the same gauntlet results and figure hashes as the runner's copy. On 2026-10-02 a stricter comparison was also made (Part 6.3): apart from those three differences, every printed character and every image is identical to the committed notebook.

The executed notebook equals the committed one only if the simulator is found at its normal place, `studies/dirac16complex_cosmology/target/release/`. If the environment variable `DIRAC16_BIN` points to the program somewhere else (Part 3.14), the driver cell prints that path in its line `simulator  : ...`, as the full path if the program lies outside the repository. This was tested on 2026-10-02 with a program in a folder outside the clone (Part 6.5). The gauntlet (71 of 71), the audit (`SUCCESS`), the 17 figures, the report and the 65 scratch files were unchanged. But the notebook written by the runner differed from the committed file in exactly that one line, and `git status --porcelain` printed ` M notebooks/dirac16complex_dark_sector.ipynb`. Restore it with `git checkout -- notebooks/dirac16complex_dark_sector.ipynb`. With an unset `DIRAC16_BIN` and a normal build (Part 3.8) this cannot happen.

On macOS and Linux (not verified on 2026-10-02) the project's own Stage-3 records state the following for Linux on an x86-64 processor (Ubuntu 24.04 under WSL2 on the verification computer), with the `win11` engine and the pinned versions. The simulator's files are byte-identical there too, and the gauntlet and the audit pass, but all 17 PNG files (and hence the executed notebook and the report) differ in their bytes, because matplotlib writes different PNG bytes there. The executed notebook also differs there in one printed line, the simulator path, which has no `.exe` outside Windows. The project's records contain no run on macOS. On a Mac with Apple silicon, even the byte identity of the simulator's files is untested (Part 3.7).

### 4.8 Run times

Measured on the verification computer (Intel Core Ultra 9 275HX, 24 logical processors, 191 GB memory, Windows 11; other jobs kept the processor about 90 % busy during the runs):

| Step | Run 1 (Git Bash) | Run 2 (PowerShell) | Peak memory (whole process tree) |
| --- | --- | --- | --- |
| `git clone` (Part 3.5) | 11.2 s | 8.8 s | 316 MiB / 314 MiB |
| engine download (Part 3.7) | 5.2 s | 4.8 s | 110 MiB / 181 MiB |
| `cargo build --release` (Part 3.8) | 8.1 s | 8.9 s | 345 MiB / 334 MiB |
| Jupyter's executor (Part 3.9) | 136.2 s | 163.1 s | 309 MiB / 342 MiB |
| the runner `run_notebook.py` (Part 3.10) | 123.9 s | 154.6 s | 159 MiB / 160 MiB |
| the audit (Part 3.11) | 2.8 s | 1.3 s | 55 MiB / 53 MiB |
| all six steps | 287.4 s | 341.5 s | |

Peak memory is the largest sum of the working sets of all processes of the step (the command, the Jupyter kernel and the simulator), sampled every 0.25 s, run 1 / run 2.

The two private-environment runs of Part 6.5 (run 3 Git Bash / run 4 PowerShell, the two running at the same time on the same busy computer) took: `git clone` 11.2 s / 9.6 s; creating the environment (`python -m venv`) 7.1 s / 6.4 s; the three pip commands of Part 3.6: 6.9 s, 69.1 s and 20.0 s in both runs; engine download 6.4 s / 7.0 s; `cargo build --release` 10.0 s / 9.5 s; Jupyter's executor 139.6 s / 140.4 s; the runner 147.6 s / 144.8 s; the audit 1.2 s / 1.1 s. pip found every package in its download cache on that computer. On a computer that has never installed them, pip first downloads about 86 MB, which adds the download time of your connection.

Inside one execution almost all the time is the EXP-4 cell (from the per-cell timestamps of the nbconvert copy of run 1: driver 0.5 s, print-config 0.0 s, EXP-1 2.0 s, EXP-2 8.1 s, EXP-3 6.7 s, EXP-4 113.0 s, EXP-5 0.5 s, gauntlet 0.3 s). On an idle computer expect somewhat less; the interactive route takes as long as one execution.

The two runs of 2026-10-07 (Part 6.6: run 6 in Git Bash, run 7 in PowerShell, started at the same time) ran while the processor was 100 % busy with other jobs (several Wolfram kernels of other verifications), so every step took longer. Run 6 / run 7: `git clone` 20.6 s / 19.7 s; `python -m venv` 16.9 s / 14.5 s; the three pip commands of Part 3.6 17.2 s, 141.6 s and 46.9 s / 17.4 s, 141.7 s and 47.3 s; engine download 17.7 s / 18.3 s; `cargo build --release` 22.7 s / 21.5 s (cargo's own line `Finished ... in 20.22s` / `19.89s`); Jupyter's executor 272.6 s / 268.5 s; the runner 217.4 s / 213.3 s; the audit 7.9 s / 4.9 s; the whole sequence, including the extra checks of the verification, 849.7 s / 841.4 s. Peak memory (the largest sum of the working sets of the step's whole process tree, sampled every 0.5 s; in run 7 the tree also includes the PowerShell host that ran each step, which explains why run 7's values are 40 to 105 MiB higher): clone 335 / 403 MiB, build 353 / 393 MiB, Jupyter's executor 344 / 449 MiB, runner 185 / 265 MiB, audit 76 / 150 MiB. Per cell, from the timestamps of the nbconvert copies: driver 2.7 s / 2.2 s, print-config 0.1 s / 0.1 s, EXP-1 3.9 s / 3.6 s, EXP-2 13.1 s / 13.5 s, EXP-3 11.6 s / 11.8 s, EXP-4 222.2 s / 220.3 s, EXP-5 1.1 s / 1.2 s, gauntlet 0.5 s / 0.5 s. So on a computer whose processor is fully used by other programs, expect the EXP-4 cell to take about four minutes.

## 5. Side effects

### 5.1 Files and folders created (all git-ignored)

* `vendor/rustSolveIt/` (about 80 MB; the engine, Part 3.7).
* `studies/dirac16complex_cosmology/target/` (about 16 MB; the build, Part 3.8).
* `build/notebook-run/exp1/` ... `exp5/` (65 files, about 23 MB; rewritten by every execution; another folder can be chosen with the environment variable `DIRAC16_NB_OUTPUT`, relative to the repository root).
* `build/nbconvert/dirac16complex_dark_sector.ipynb` (about 2.1 MB; Part 3.9).
* With JupyterLab only: `notebooks/.ipynb_checkpoints/` (git-ignored) and JupyterLab's workspace files in your home folder.

### 5.2 Committed files OVERWRITTEN

* Every execution (nbconvert, runner or JupyterLab) rewrites the 17 committed figures in `artifacts/dirac16complex/numerics/figures/`.
* `run_notebook.py` rewrites `notebooks/dirac16complex_dark_sector.ipynb` (only if every cell succeeded).
* `check_notebook.py --report` rewrites `artifacts/dirac16complex/numerics/notebook-report.json`.
* Saving from JupyterLab rewrites `notebooks/dirac16complex_dark_sector.ipynb`.
* The builder (not part of a run) rewrites `notebooks/dirac16complex_dark_sector.ipynb` without outputs.

On Windows with the pinned versions all of these come out byte-identical, so `git status --porcelain` stays empty. Nothing else in the repository is written: the simulator writes only below `build/notebook-run/`. Its default output folder would be the committed `artifacts/dirac16complex/numerics/`, but the notebook always passes `--output build/notebook-run`.

### 5.3 Temporary files and files outside the repository

* nbconvert writes a kernel connection file `kernel-<id>.json` into Jupyter's runtime folder (Windows `%APPDATA%\jupyter\runtime`, Linux `~/.local/share/jupyter/runtime`, macOS `~/Library/Jupyter/runtime`) and deletes it at the end; the kernel keeps its command history in memory only.
* matplotlib creates its font cache (Windows `%USERPROFILE%\.matplotlib`, Linux `~/.cache/matplotlib`, macOS `~/.matplotlib`) the first time it is used on a computer.
* `cargo build` uses temporary folders in the system temporary directory and removes them.
* The interactive route also writes IPython's history (`~/.ipython/profile_default/history.sqlite`).
* The private environment of Part 3.6 lives in `~/venvs/dirac16` (about 440 MB; delete the folder to remove it); pip keeps downloaded packages in its cache. The environment contains its own `python3` kernel definition (`share/jupyter/kernels/python3` inside it); nothing is registered in your personal Jupyter folder.

### 5.4 Processes

* nbconvert starts one Jupyter kernel (a `python -m ipykernel_launcher` process) and stops it at the end. The runner executes the cells in its own process.
* Each execution starts the simulator 6 times (`print-config`, `exp1` ... `exp5`) and the analysis once (`python scripts/analyze_dirac16complex_exp3.py --output build/notebook-run`). The EXP-4 run uses up to 8 threads; the other runs one.
* No Wolfram kernel is started, and no Wolfram software is used.

### 5.5 Network

Only for the setup: `git clone` (Part 3.5), the engine download (Part 3.7), and the installation of Python packages and Rust. Executing the notebook uses no network.

### 5.6 How to restore the committed state

From the repository root, all systems:

```
git checkout -- notebooks/dirac16complex_dark_sector.ipynb artifacts/dirac16complex/numerics/figures artifacts/dirac16complex/numerics/notebook-report.json
```

To remove the scratch outputs, PowerShell `Remove-Item -Recurse -Force build/notebook-run, build/nbconvert`; other shells `rm -rf build/notebook-run build/nbconvert`. To remove the engine and the build as well, delete `vendor/rustSolveIt` and `studies/dirac16complex_cosmology/target` the same way (you then have to repeat Parts 3.7 and 3.8 before the next run). `git status --porcelain --ignored` lists everything that is not committed.

## 6. Verification record

### 6.1 What was verified, where and with what

* Date: 2026-10-02.
* Commit: `c2b33ccd16edb9c8b46585d0db6b2911a1f5d84e` (the head of `main` on GitHub at the time; both fresh clones checked it out).
* Uncommitted files copied into the clones: none (no uncommitted file of the working copy belongs to this set).
* Computer: Intel Core Ultra 9 275HX, 24 logical processors, 191 GB memory, Windows 11 Pro for Workstations 10.0.26200. Other jobs kept the processor about 90 % busy.
* Software: Python 3.14.5 with numpy 2.4.6, matplotlib 3.11.0 (with its helpers pillow 12.2.0, contourpy 1.3.3, cycler 0.12.1, fonttools 4.63.0, kiwisolver 1.5.0, packaging 26.2, pyparsing 3.3.2, python-dateutil 2.9.0.post0), sympy 1.14.0, nbformat 5.10.4, nbclient 0.10.2, nbconvert 7.16.6, ipykernel 7.1.0, IPython 9.7.0, jupyter_client 8.6.3, jupyter_core 5.9.1, pyzmq 27.1.0, tornado 6.5.2, jupyterlab 4.4.10; cargo 1.91.1 and rustc 1.91.1 (`stable-x86_64-pc-windows-msvc`) with the Microsoft linker 14.51.36231; git 2.51.2.windows.1; PowerShell 7.6.6; GNU bash 5.2.37 (Git Bash). The interpreter was `C:\Python314\python.exe`; for runs 1 and 2 the packages were already installed in its per-user package folder (`%APPDATA%\Python\Python314\site-packages`, the folder that `pip install --user` uses), with exactly the versions named in Part 3.6. Runs 1 and 2 therefore did not use the private environment, and no Python package was downloaded for them. Runs 3 and 4 (Part 6.5) executed the commands of Part 3.6 in new private environments.
* Engine: `vendor/rustSolveIt` at `a8fdff459adfe181573d7924b18bffbdf378fdb3` (`solver_setup=OK` in both runs).
* Environment: no `DIRAC16_BIN`, `DIRAC16_NB_OUTPUT`, `RUSTFLAGS` or `CARGO_TARGET_DIR` was set; `PYTHONDONTWRITEBYTECODE` was removed so that the runs behaved as in a student's shell.

### 6.2 The two runs

Each run started from an empty folder with `git clone https://github.com/once-ere/Dirac_claude.git`, then followed Parts 3.7 to 3.12 literally, from the repository root of the clone:

* **Run 1, Git Bash route**: `bash scripts/setup_solver.sh win11`; `cd studies/dirac16complex_cosmology` and `cargo build --release`; `python -m nbconvert --to notebook --execute ...` (Part 3.9); `python notebooks/run_notebook.py ...`; `python notebooks/check_notebook.py ... --also ... --report ...`.
* **Run 2, PowerShell route**: `pwsh -NoProfile -File scripts/setup_solver.ps1 -Platform win11`; the same build; `jupyter nbconvert --to notebook --execute ...` with the per-user Jupyter folder `%APPDATA%\Python\Python314\Scripts` put on PATH for the session (the fix of Part 3.14 for "jupyter not found"); the same runner and audit.

`git status --porcelain` was recorded after the clone, after the build, after nbconvert, after the runner and after the audit, and it was empty every time in both runs. (Run 1 saved each result in a file, and all five files are empty. Run 2 saved them with PowerShell's `Set-Content`, which creates no file when there is no output; no file was created, the sha256 snapshots after each step in Part 6.3 confirm the same state, and a final `git status --porcelain` typed by hand printed nothing.) At the end `git status --porcelain --ignored` listed exactly `build/`, `studies/dirac16complex_cosmology/target/` and `vendor/` in both clones. Calling the engine download a second time in the run-2 clone printed `solver_setup=ALREADY-PRESENT`, and building a second time took 0.02 s and changed nothing.

| Step | Run 1 | Run 2 |
| --- | --- | --- |
| `git clone` | exit 0, HEAD `c2b33cc` | exit 0, HEAD `c2b33cc` |
| engine download | exit 0 (`bash scripts/setup_solver.sh win11`), `solver_setup=OK` | exit 0 (`pwsh -NoProfile -File scripts/setup_solver.ps1 -Platform win11`), `solver_setup=OK` |
| `cargo build --release` | exit 0, no warning, `Finished ... in 7.97s` | exit 0, no warning, `Finished ... in 8.81s` |
| Jupyter's executor | exit 0 (`python -m nbconvert ...`), `Writing 2153532 bytes` | exit 0 (`jupyter nbconvert ...`), `Writing 2153425 bytes` |
| the runner | exit 0; 140 `PASS - ` lines, 0 `FAIL`, 6 `SUCCESS`; `ALL CHECKS PASSED`; `1 ok, 0 failed` | exit 0; 140 `PASS - ` lines, 0 `FAIL`, 6 `SUCCESS`; `ALL CHECKS PASSED`; `1 ok, 0 failed` |
| the audit | exit 0; both copies `ok` (23 cells, 8 code cells, 71 gauntlet checks, 17 figures), `ok cross-check`, verdict `SUCCESS` | exit 0; the same four lines |

### 6.3 Byte identity of every output

| Output | sha256 | Result |
| --- | --- | --- |
| `notebooks/dirac16complex_dark_sector.ipynb` | `5cd2befc1862041c0047c3d38db1dcc182aa47dde8db0cd571a2023fbc9ac5f0` | rewritten by the runner; identical to the committed file at all 3 stages of both runs (6 comparisons) |
| `artifacts/dirac16complex/numerics/notebook-report.json` | `7cf06b0f3693819aeed61e018ebb455387b642e9062f4f14e70c9512d71334cb` | rewritten by the audit; identical at all 3 stages of both runs (6 comparisons) |
| `artifacts/dirac16complex/numerics/figures/exp1_einstein_requirement.png` | `42475d956a3c63fbbef0cea4da32ec5d886c4b7a00fc9f46075baea2f84b3191` | rewritten by both executors; identical after nbconvert, after the runner and at the end, both runs (6 comparisons) |
| `artifacts/dirac16complex/numerics/figures/exp1_frozen_observables.png` | `719b7bc3220da6a7a3c85829b8848fa17c97e4b27c9b0d53fc40af98c8e6d934` | rewritten by both executors; identical after nbconvert, after the runner and at the end, both runs (6 comparisons) |
| `artifacts/dirac16complex/numerics/figures/exp2_eos_constraint.png` | `36207840f68c0a2b8f1bfefa240fc7a0b5c382c354b7876623eb50051b321638` | rewritten by both executors; identical after nbconvert, after the runner and at the end, both runs (6 comparisons) |
| `artifacts/dirac16complex/numerics/figures/exp2_hubble.png` | `af815eb061bcd44d93b39d897c15c6e4a3a81cc1fd5315322db2ab7620fff2c8` | rewritten by both executors; identical after nbconvert, after the runner and at the end, both runs (6 comparisons) |
| `artifacts/dirac16complex/numerics/figures/exp2_volume_density.png` | `097750e8b52828ee25a700e3698db11c1ca206b39326ab3f349eb7c187302e19` | rewritten by both executors; identical after nbconvert, after the runner and at the end, both runs (6 comparisons) |
| `artifacts/dirac16complex/numerics/figures/exp3_distance_modulus.png` | `014181b9e5526af14a120a7ffdde1550057c20ca5f985c15c2be8241b03112b2` | rewritten by both executors; identical after nbconvert, after the runner and at the end, both runs (6 comparisons) |
| `artifacts/dirac16complex/numerics/figures/exp3_ke_pe.png` | `71275e8777920ef2405ea5e1b5d45e23c5bd8d8aa6d7a3f6e2fa25e4dea0e8de` | rewritten by both executors; identical after nbconvert, after the runner and at the end, both runs (6 comparisons) |
| `artifacts/dirac16complex/numerics/figures/exp3_rho_psi.png` | `93d296d6b58dbd0f0df9e706099b599620403b494eb9ad813faaa6bb64933ea5` | rewritten by both executors; identical after nbconvert, after the runner and at the end, both runs (6 comparisons) |
| `artifacts/dirac16complex/numerics/figures/exp3_w0wa_plane.png` | `16afd9a42370d3343d60a9f6cea453f9eefa280bf56e64d9cc30d52a03df96a1` | rewritten by both executors; identical after nbconvert, after the runner and at the end, both runs (6 comparisons) |
| `artifacts/dirac16complex/numerics/figures/exp3_w_of_a.png` | `c5d9e35378948d87fc6978c894628dcba93a9b9bf9f176a68850ee19a290a3f2` | rewritten by both executors; identical after nbconvert, after the runner and at the end, both runs (6 comparisons) |
| `artifacts/dirac16complex/numerics/figures/exp4_pair_density.png` | `30031fb2982d0a358c0999ec86a14a5db369abf02414b9bc6200bced05a950e9` | rewritten by both executors; identical after nbconvert, after the runner and at the end, both runs (6 comparisons) |
| `artifacts/dirac16complex/numerics/figures/exp4_pair_spectra.png` | `41e136628e5c70d4709687ece0c46807825be80b6ec07256d7ba6786e293151f` | rewritten by both executors; identical after nbconvert, after the runner and at the end, both runs (6 comparisons) |
| `artifacts/dirac16complex/numerics/figures/exp4_thermal_scaling.png` | `0db10806f00d3a706b131586d0a191cf6c4b786dc5d5b6ceaa4f158022aafa04` | rewritten by both executors; identical after nbconvert, after the runner and at the end, both runs (6 comparisons) |
| `artifacts/dirac16complex/numerics/figures/exp4_thermal_split.png` | `d4b8ac3c2c18637e0f2f7a70722b7795091b08180ae61a9288af6c15845dfd1e` | rewritten by both executors; identical after nbconvert, after the runner and at the end, both runs (6 comparisons) |
| `artifacts/dirac16complex/numerics/figures/exp4_thermal_w.png` | `0de3ee0fc58bbcdd438313aa77c14789b4ec43a0c41ac505396ea4e39cc5fdad` | rewritten by both executors; identical after nbconvert, after the runner and at the end, both runs (6 comparisons) |
| `artifacts/dirac16complex/numerics/figures/exp5_growth.png` | `b5c7546f94f6226e2c99bd1bbbf62af330b94ef5d20c1b13a93fc7a6b453f38f` | rewritten by both executors; identical after nbconvert, after the runner and at the end, both runs (6 comparisons) |
| `artifacts/dirac16complex/numerics/figures/exp5_krein.png` | `78570341b44825997c549a14d21a44733aab9897f7ad4c428ce54bdec53a28df` | rewritten by both executors; identical after nbconvert, after the runner and at the end, both runs (6 comparisons) |
| `build/notebook-run/exp1/` (29 simulator files) | each equal to the committed file of the same name in `artifacts/dirac16complex/numerics/` | 29/29 byte-identical in both runs, written by nbconvert's execution and again by the runner's (174 comparisons) |
| `build/notebook-run/exp2/` (4 simulator files) | each equal to the committed file of the same name in `artifacts/dirac16complex/numerics/` | 4/4 byte-identical in both runs, written by nbconvert's execution and again by the runner's (24 comparisons) |
| `build/notebook-run/exp3/` (11 simulator files) | each equal to the committed file of the same name in `artifacts/dirac16complex/numerics/` | 11/11 byte-identical in both runs, written by nbconvert's execution and again by the runner's (66 comparisons) |
| `build/notebook-run/exp3/` (3 EXP-3 analysis files) | each equal to the committed file of the same name in `artifacts/dirac16complex/numerics/` | 3/3 byte-identical in both runs, written by nbconvert's execution and again by the runner's (18 comparisons) |
| `build/notebook-run/exp4/` (13 simulator files) | each equal to the committed file of the same name in `artifacts/dirac16complex/numerics/` | 13/13 byte-identical in both runs, written by nbconvert's execution and again by the runner's (78 comparisons) |
| `build/notebook-run/exp5/` (5 simulator files) | each equal to the committed file of the same name in `artifacts/dirac16complex/numerics/` | 5/5 byte-identical in both runs, written by nbconvert's execution and again by the runner's (30 comparisons) |
| `build/nbconvert/dirac16complex_dark_sector.ipynb` | run 1 `c04bc405257ad30e180e4ee7efb2e5726908ada1978d34e415d9fc052ad24853`, run 2 `052afcd9eed6eaaff5686f1ba4fee25286e14c91aaca2badff6467ccd1b8fa0f` | not byte-identical (by design: timestamps, `language_info`, CRLF on Windows, timing-dependent splitting of the printed text); normalised content identical to the committed notebook and between the runs |

How the nbconvert copies were compared: byte for byte, and then with a normalised comparison that ignores only (N1) the per-cell `execution` timestamps of nbclient, (N2) the notebook's `language_info`, which the kernel fills in, (N3) the way the printed text is split into separate stream outputs, (N4) the text alternative of an image (`<Figure name.png>` from the runner, `<IPython.core.display.Image object>` from Jupyter) and (N5) line endings (the JSON is parsed). Never ignored: cell sources, cell ids, execution counts, every printed character of every cell, the order of text and images, every PNG image (byte for byte), error and stderr outputs, the kernel specification and all other metadata. The repository's own auditor additionally compared the gauntlet results and figure hashes of the two executors in each run (`ok cross-check`). The Stage-3 gate's comparison program `scripts/verify_stage3_dark_sector_audit.py notebook` was also run on run 1's fresh report and notebook: `stage3_notebook_report=equal to the committed report except the notebook paths: 2 executions, gauntlet 71/71, 17 figures with the committed sha256`, `stage3_notebook_executed_copy_byte_identical_to_committed=yes`, `stage3_audit_notebook=OK`.

### 6.4 Problems met during the verification, and fixes

* **A first attempt failed for a reason outside the repository.** The first clone sat at a 161-character path. `cargo build --release` stopped with `LINK : fatal error LNK1104: cannot open file '...\target\release\deps\libdirac16complex_cosmology-20513573899aa199.rlib'` (exit code 101) although that file existed (2,945,618 bytes): its path had 264 characters, and the Microsoft linker cannot open paths of 260 characters or more, even with Windows long paths enabled (they were). Repeating the build failed identically, which rules out a temporary file lock. Both verification runs then used a short clone folder (the `.rlib` path had 251 characters) and built without error. This is a property of the Windows toolchain, not of the repository; Part 3.5 and Part 3.14 tell the student how to avoid it.
* In the same first attempt the measuring script started `bash` through Python, and on Windows that started WSL's `C:\Windows\System32\bash.exe` instead of Git Bash. The engine download still succeeded (`solver_setup=OK`, with the harmless WSL message `wsl: Failed to translate ...`). The two verification runs used Git Bash and PowerShell explicitly; Part 3.7 warns about this.
* Also observed: `python -m jupyter nbconvert` answers `Jupyter command 'jupyter-nbconvert' not found.` when the packages are installed per user (with `pip install --user`) and their `Scripts` folder is not on PATH. `python -m nbconvert` and `python -m jupyterlab` work regardless (Part 3.14).
* Fixes made to files of this set: **none**. No file of the repository was changed by this verification apart from adding this provenance file.

### 6.5 Second verification on 2026-10-02: the private environment, the kernel, `DIRAC16_BIN` and Apple silicon

A review of the first version of this file found four statements that were not exactly true. Each was re-checked on the same computer: by runs in fresh clones of commit `c2b33ccd16edb9c8b46585d0db6b2911a1f5d84e`, with no uncommitted file copied in, and, for Apple silicon, with rustc. The file was then corrected. No file of the repository other than this one was changed.

| Review point | What was wrong in the first version | Corrected in |
| --- | --- | --- |
| package versions | Part 3.6 said its commands install "exactly the versions of the verification". That was true only for the 8 packages named in it. Followed literally in a new environment on 2026-10-02, the old commands installed 100 packages, 59 of them in other versions than the verification computer had. Among them were Pillow 12.3.0 (verification 12.2.0), contourpy 1.4.0 (1.3.3), fonttools 4.66.1 (4.63.0), kiwisolver 1.5.1 (1.5.0), packaging 26.3 (26.2), pyparsing 3.3.3 (3.3.2), IPython 9.17.1 (9.7.0), jupyter_client 8.10.0 (8.6.3), pyzmq 27.2.0 (27.1.0), tornado 6.5.10 (6.5.2) and traitlets 5.16.1 (5.14.3). The reviewer reported that the notebook run in such an environment still gave byte-identical outputs. | Part 3.6: the second pip command now also fixes the 13 packages that matplotlib and the kernel depend on |
| `No module named 'numpy'` in nbconvert | the cause given was "the kernel definition runs whatever `python` comes first on PATH". That is false. jupyter_client 8.6.3 (`manager.py`, `format_kernel_cmd`) replaces a kernel command `python` by the Python that runs nbconvert. The error needs a kernel definition that names another Python by its full path. | Part 3.14 |
| `DIRAC16_BIN` | Part 3.14 recommended `DIRAC16_BIN` without saying that the executed notebook then prints that path, differs from the committed file and is listed by `git status` | Parts 3.8, 3.14, 4.4, 4.7 |
| Apple silicon | Part 4.2 promised "No warning" on every computer, but `+fma` is unknown to rustc on ARM processors. Part 3.7 did not say that no recorded verification has run the `win11` engine on Apple silicon. | Parts 3.1, 3.7, 3.8, 3.14, 4.2, 4.7 |

**Runs 3 and 4: the private environment, installed exactly as in Part 3.6.** Each run started from an empty folder with `git clone`. It created a new environment with `python -m venv` (in the scratch folder of the verification instead of `~/venvs/dirac16`) and activated it: run 3 in Git Bash with `source .../Scripts/activate`, run 4 in PowerShell 7 with `& ...\Scripts\Activate.ps1`. It then typed the three pip commands of Part 3.6 and followed Parts 3.7 to 3.12 literally. Run 3 used `python -m nbconvert` and `bash scripts/setup_solver.sh win11`. Run 4 used `jupyter nbconvert` (the environment's own `jupyter.exe`) and `pwsh -NoProfile -File scripts/setup_solver.ps1 -Platform win11`. The two runs ran at the same time.

| Step | Run 3 (Git Bash) | Run 4 (PowerShell) |
| --- | --- | --- |
| `git clone` | exit 0, HEAD `c2b33cc` | exit 0, HEAD `c2b33cc` |
| the three pip commands | exit 0 each; nothing uninstalled; `python -m pip check` prints `No broken requirements found.` | the same |
| versions | all 21 packages named in Part 3.6 have exactly the versions of Part 6.1. Of the other 80 installed packages, 30 have the verification computer's version and 50 a newer one (for example anyio 4.15.1, jupyter_server 2.21.1, jsonschema 4.26.0, traitlets 5.16.1) | identical list to run 3 |
| `python -m jupyter_client.kernelspecapp list` | `python3` in the environment's own folder `...\share\jupyter\kernels\python3`, whose `kernel.json` names just `python` | the same, in its own environment |
| engine download, build | exit 0, `solver_setup=OK`; exit 0, no warning, `Finished ... in 9.77s` | exit 0, `solver_setup=OK`; exit 0, no warning, `Finished ... in 9.42s` |
| Jupyter's executor | exit 0, `Writing 2153435 bytes` | exit 0, `Writing 2153425 bytes` |
| the runner | exit 0; 140 `PASS - ` lines, 0 `FAIL`, 6 `SUCCESS`; `ALL CHECKS PASSED`; `1 ok, 0 failed` | the same |
| the audit | exit 0; both copies `ok` (23 cells, 8 code cells, 71 gauntlet checks, 17 figures), `ok cross-check`, verdict `SUCCESS` | the same |
| `git status --porcelain` | empty after the clone, after the installation, after the build, after nbconvert, after the runner and after the audit | the same |
| `git status --porcelain --ignored` at the end | exactly `build/`, `studies/dirac16complex_cosmology/target/`, `vendor/` | the same |

Byte identity in runs 3 and 4 was checked after nbconvert, after the runner and at the end. All 19 committed outputs (the notebook `5cd2befc...`, the report `7cf06b0f...` and the 17 figures with the sha256 of Part 2.3) were identical to the committed files at all three points of both runs. All 65 files of `build/notebook-run/` were byte-identical to the committed files after both executions of both runs. Jupyter's own copies (run 3 `a03c63775a825d339582265f680b0d8f9d770a129ffd0056f919820a151a4016`, run 4 `1b8923b7c0ced56c91765bb8c5b1e5649e20aacd7175d5a41d8578dbff4923c4`) are not byte-identical, by design. With the normalised comparison of Part 6.3 they are identical to the committed notebook: all 8 execution counts, every printed character and all 17 images byte for byte. Measured times are in Part 4.8.

**The kernel experiments (review point 2).** These used a one-cell notebook that prints the Python it runs in and imports numpy. A second Python without numpy was made for them: a separate private environment with only `ipykernel==7.1.0`. The personal Jupyter folder was redirected to a scratch folder with the environment variable `JUPYTER_DATA_DIR`, so the computer's real Jupyter configuration was not touched.

* K1. No other kernel was registered. The numpy-less Python was put FIRST on PATH, and nbconvert was started by `C:\Python314\python.exe`. Result: exit 0. The cell ran in `C:\Python314\python.exe` and imported numpy 2.4.6. The order of PATH plays no role.
* K2. The numpy-less Python registered its kernel with `python -m ipykernel install --user`. Its `kernel.json` then began with that Python's full path. `python -m jupyter_client.kernelspecapp list` (system Python) showed this definition for `python3`. nbconvert then stopped with exit 1 and `ModuleNotFoundError: No module named 'numpy'`. The real notebook in a fresh clone (run 5 below) failed the same way after 7.2 s: `nbclient.exceptions.CellExecutionError`, `Cell In[1], line 11`, `---> 11 import numpy as np`. `git status --porcelain` stayed empty.
* K3. Same registration, but nbconvert was run in the activated private environment of runs 3 and 4. `kernelspecapp list` showed the environment's own `python3`, and the cell ran in the environment's Python: exit 0, numpy 2.4.6.
* K4. Same as K3, but with `JUPYTER_PREFER_ENV_PATH=0`, or with the foreign definition in a folder named by `JUPYTER_PATH`. Both failed with the numpy error inside the environment too. This is why fix (a) of Part 3.14 says to remove these two variables.
* K5. The fixes (b), (c) and (d) of Part 3.14, each tried with the foreign definition registered again. `python -m ipykernel install --user` from the system Python rewrote the definition with `C:\Python314\python.exe`, and nbconvert gave exit 0 with numpy. `python -m jupyter_client.kernelspecapp remove python3 -y` printed `Removed ...`. The next `python3` found was then the one in the per-user Python folder (`%APPDATA%\Python\share\jupyter\kernels\python3`), whose `kernel.json` names just `python`, and nbconvert gave exit 0 with numpy. `python notebooks/run_notebook.py` printed `1 ok, 0 failed`.

**Run 5: `CARGO_TARGET_DIR` and `DIRAC16_BIN` (review point 3).** This used a fresh clone, the system Python of Part 6.1 and Git Bash.

* Built with `CARGO_TARGET_DIR` set to a folder outside the clone: exit 0, 7.4 s. No `target` folder was created in `studies/dirac16complex_cosmology`. The driver cell alone stopped with `RuntimeError('dirac16complex_cosmology binary not found - build it first: ...')`.
* After `unset CARGO_TARGET_DIR` and building again (5.8 s), the driver cell printed `simulator  : studies/dirac16complex_cosmology/target/release/dirac16complex_cosmology.exe`. This is the fix given in Parts 3.8 and 3.14. The two programs differ in 20 of their 1,721,344 bytes.
* With `DIRAC16_BIN` set to the program in the outside folder, the full sequence of Parts 3.9 to 3.11 ran. nbconvert: exit 0, 113.2 s. Runner: exit 0, 126.5 s, 140 `PASS - ` lines, `ALL CHECKS PASSED`. Audit: exit 0, verdict `SUCCESS`. The 17 figures, the report and all 65 scratch files were byte-identical to the committed ones. The notebook was not: `git diff --stat` showed `1 file changed, 1 insertion(+), 1 deletion(-)`, and the changed line was `simulator  : C:\Users\...\c\tdir\release\dirac16complex_cosmology.exe` (the full path, including the user name). `git status --porcelain` printed ` M notebooks/dirac16complex_dark_sector.ipynb`. After the committed notebook was written back from git, `git status --porcelain` was empty again.

**Apple silicon (review point 4).** No Mac was available, so the macOS route is still not run. Compiling the real program for a Mac needs Apple's linker and Rust's standard library for that target, and neither is on the verification computer. What was checked with rustc 1.91.1:

* `rustc --print target-features --target aarch64-apple-darwin` lists `neon`, `fp-armv8` and `aggressive-fma`, but no `fma`. For `x86_64-apple-darwin` it lists `fma`.
* A minimal program (no standard library) was compiled with `-C target-feature=+fma`. For `aarch64-apple-darwin` and `aarch64-unknown-linux-gnu`, rustc printed the warning lines of Part 4.2 and exited with 0, also with `#![deny(warnings)]` in the program and with `-D warnings` on the command line. For `x86_64-apple-darwin` and `x86_64-unknown-linux-gnu` it printed nothing and exited with 0.
* The engine's own `vendor/rustSolveIt/sundials_rs/.cargo/config.toml` applies `+fma` only for `target_arch = "x86_64"`. The repository's `.cargo/config.toml` applies it on every processor. The repository's file was left unchanged: other parts of the repository share it, the warning did not stop rustc in the tests above, and on x86-64 the two files give the same option.

**Problem met during the second verification.** In the separate environment that followed the OLD commands of Part 3.6 (to record which versions they install), the third pip command once stopped with `ERROR: ResolutionImpossible` and `no matching distributions available for your environment: anyio`. Before that, pip had printed `WARNING: Skipping page https://pypi.org/simple/anyio/ because the GET request got Content-Type: Unknown`. Repeating the same command succeeded after 20 s. This is the temporary index failure listed in Part 3.14. Runs 3 and 4 were not affected.

Fixes made to files of this set in the second verification: **none**. Only this provenance file was corrected.

### 6.6 Third verification on 2026-10-07: commit `72fc9ff`, runs 6 and 7

**Why.** By 2026-10-07 the head of `main` had moved 13 commits on, to `72fc9ffc4a10328080a5778cc8a8c6e689aeaca6` (`git ls-remote` on GitHub confirmed it as the head when the verification started; the later commits of that day, which were snapshots of other work, changed no file of this set apart from this provenance file). `git diff --stat c2b33cc 72fc9ff` over every file this notebook runs or reads (`notebooks/`, `scripts/analyze_dirac16complex_exp3.py`, `scripts/setup_solver.*`, `requirements-stage3.txt`, `.cargo/`, `studies/dirac16complex_cosmology/`, `artifacts/dirac16complex/`, `.gitattributes`, `.gitignore`) lists only three files of `artifacts/dirac16complex/pair-creation/`, which the notebook does not read, and the addition of this provenance file and of the Kohn-Sham notebook's provenance file. The notebook was nevertheless executed again from the beginning, as a student would.

**What, where and with what.**

* Date: 2026-10-07. Commit: `72fc9ffc4a10328080a5778cc8a8c6e689aeaca6`; both fresh clones checked it out.
* Uncommitted files copied into the clones: none. The uncommitted changes of the working copy that day (four provenance files of Wolfram script sets) do not belong to this set.
* Computer: the one of Part 6.1, now with Windows 11 Pro for Workstations 10.0.26300 (an operating-system update since 2026-10-02). Other jobs, among them several Wolfram kernels, kept the processor 100 % busy during both runs.
* Software: as in Part 6.1 (Python 3.14.5, cargo and rustc 1.91.1, git 2.51.2.windows.1, PowerShell 7.6.6, GNU bash 5.2.37). The Python packages were NOT taken from the computer: each run created a new private environment with `python -m venv` (outside the clone, in the verification's scratch folder instead of `~/venvs/dirac16`), activated it and typed the three pip commands of Part 3.6 literally. pip upgraded itself from 26.1.1 to 26.2.1. Each environment then held 101 packages, the 21 named in Part 3.6 in exactly the versions of Part 6.1; `python -m pip freeze` printed identical lists in both runs; `python -m pip check` printed `No broken requirements found.`; `python -m jupyter_client.kernelspecapp list` showed `python3` in the environment's own folder `share\jupyter\kernels\python3`.
* Environment: `RUSTFLAGS`, `CARGO_TARGET_DIR`, `DIRAC16_BIN`, `DIRAC16_NB_OUTPUT`, `JUPYTER_PATH`, `JUPYTER_PREFER_ENV_PATH` and `PYTHONDONTWRITEBYTECODE` were removed for every step.
* Clone folders: 146 characters long, so the longest build path had 249 characters, below the linker limit of Part 3.5.

**The runs.** Each started from an empty folder with `git clone https://github.com/once-ere/Dirac_claude.git`, then followed Parts 3.6 to 3.11 literally from the repository root of the clone, each step as a separate command of the run's shell.

* **Run 6, Git Bash route**: `source .../Scripts/activate` before every Python command; `bash scripts/setup_solver.sh win11`; `cd studies/dirac16complex_cosmology` and `cargo build --release`; `python -m nbconvert --to notebook --execute ...` (Part 3.9); `python notebooks/run_notebook.py ...`; `python notebooks/check_notebook.py ... --also ... --report ...`; the summary command of Part 4.7; the engine download once more.
* **Run 7, PowerShell route**: `& ...\Scripts\Activate.ps1` before every Python command; `pwsh -NoProfile -File scripts/setup_solver.ps1 -Platform win11`; the same build; `jupyter nbconvert --to notebook --execute ...` (the environment's own `jupyter.exe`); the same runner, audit, summary and second engine download.

| Step | Run 6 (Git Bash) | Run 7 (PowerShell) |
| --- | --- | --- |
| `git clone` | exit 0, HEAD `72fc9ff` | exit 0, HEAD `72fc9ff` |
| `python -m venv`, the three pip commands, `pip check` | exit 0 each; `Successfully installed pip-26.2.1`; several harmless `WARNING: Cache entry deserialization failed, entry ignored` (Part 3.14); `No broken requirements found.` | the same |
| engine download | exit 0; `solver_platform=win11`, `solver_commit=a8fdff459adfe181573d7924b18bffbdf378fdb3`, `solver_setup=OK` | the same |
| `cargo build --release` | exit 0, no warning, the three `Compiling` lines of Part 4.2, `Finished ... in 20.22s` | exit 0, no warning, `Finished ... in 19.89s` |
| Jupyter's executor | exit 0; the lines of Part 4.3 including the Proactor warning; `Writing 2153599 bytes` | exit 0; `Writing 2153686 bytes` |
| the runner | exit 0; 346 lines; 140 `PASS - ` lines (71 of them the gauntlet), 0 `FAIL`, 6 `SUCCESS`; the comparison lines of Part 4.4 with the same solver statistics (exp1 33866 steps ... exp4 339071692 steps, exp5 2548 steps) and `29/29`, `4/4`, `11/11`, `3/3`, `13/13`, `5/5`; 17 `figure ...` lines; `ALL CHECKS PASSED`; `ok notebooks\dirac16complex_dark_sector.ipynb (8 cells)`; `1 ok, 0 failed` | exit 0; printed output byte-identical to run 6 |
| the audit | exit 0; the four lines of Part 4.5, verdict `SUCCESS` | the same |
| summary command of Part 4.7 | `SUCCESS 71 of 71 gauntlet checks, 17 figures, 2 executions` | the same |
| engine download again | `solver_setup=ALREADY-PRESENT` | the same |
| `git status --porcelain` | empty after each of the 15 steps | the same |
| `git status --porcelain --ignored` at the end | exactly `build/`, `studies/dirac16complex_cosmology/target/`, `vendor/` | the same |

**Byte identity.** After nbconvert, after the runner and after the audit, the 19 committed outputs (the notebook, `notebook-report.json` and the 17 figures) were compared with the committed versions in git (`git hash-object` of the file against the blob of `HEAD`): 19 of 19 identical at all three points of both runs (114 comparisons), with the sha256 values of Part 2.3. The 65 files of `build/notebook-run/` were compared with the committed files of the same name: 65 of 65 byte-identical at all three points of both runs (390 comparisons; the scratch files were written by nbconvert's execution and written again by the runner's). Jupyter's own copies are not byte-identical, by design: run 6 sha256 `0598dea71fdf6d9c32fd70a6ce412c2511894080016ac623668787249551e23d` (2156952 bytes, all 3353 lines ending in CR LF), run 7 `5483f6cdc5982320608250f84793b63b84c085c0dfa930051403e4175f2ce055` (2157045 bytes, 3359 lines, CR LF). With the normalised comparison of Part 6.3 (ignoring only N1 to N5) each is identical to the committed notebook (execution counts 1 to 8, every printed character, all 17 images byte for byte), and the two are identical to each other; their `language_info` records Python 3.14.5. The Stage-3 gate's comparison program `scripts/verify_stage3_dark_sector_audit.py notebook`, run in each clone with the fresh report and notebook against the versions of `HEAD` (extracted with `git show`), printed `stage3_notebook_report=equal to the committed report except the notebook paths: 2 executions, gauntlet 71/71, 17 figures with the committed sha256`, `stage3_notebook_executed_copy_byte_identical_to_committed=yes` and `stage3_audit_notebook=OK` (exit code 0).

**Temporary files.** Jupyter's runtime folder `%APPDATA%\jupyter\runtime` held no kernel connection file from these runs afterwards (nbconvert deletes its file). No `__pycache__` folder appeared in the clones.

**Measured times and memory** are in Part 4.8.

Problems met: none, apart from the harmless pip warning and the longer run times on the fully loaded processor. Fixes made to files of this set: **none**. Only this provenance file was updated (the header, Parts 2, 3.5, 3.6, 3.14, 4.3, 4.8 and 6.6).

### 6.7 Open discrepancies

None for this set. Not verified on 2026-10-02 or 2026-10-07:

* the macOS and Linux routes;
* on Apple silicon, the build warning inside a full `cargo build` (it was reproduced only with a minimal program) and whether the `win11` engine reproduces the committed files byte for byte there;
* the interactive JupyterLab route of Part 3.13, which was not clicked through. JupyterLab runs the cells in the same kind of kernel as nbconvert, and the nbconvert executions were verified.
