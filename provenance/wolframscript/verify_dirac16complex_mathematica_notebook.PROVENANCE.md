# Execution provenance: the headless verifier of the Stage-3 Mathematica notebook (WolframScript)

Set: `scripts/verify_dirac16complex_mathematica_notebook.wls`, which evaluates the notebook `notebooks/Dirac16ComplexDarkSector.nb` without a notebook window (old Stage 3, the dark-sector numerics).

Verified on 2026-10-02 at commit `c2b33ccd16edb9c8b46585d0db6b2911a1f5d84e`, and verified again on 2026-10-07 at commit `8cbd03a02f7771bce9e199f5d48cd41a979f1f06` after the verification workflow was restarted, with Wolfram 15.0.1 and WolframScript 1.14.0 on Windows 11. No file of this set, no input and no committed output changed between the two commits. Verdict: **EXECUTES OK**. Every successful run printed `dirac16complex_mathematica_notebook=OK` with 37 of 37 cells evaluated, no message and **49 of 49 checks true**, and exited with code 0. The 9 files that a run rewrites (the report `mathematica-report.json` and 8 PNG figures) were **byte-identical** to the committed ones in all 10 successful runs from 5 fresh clones (7 runs on 2026-10-02, 3 runs on 2026-10-07), and therefore also between the runs. A run takes 4 to 7 minutes on a lightly loaded computer and up to 10 minutes on a fully loaded one. **It needs a lot of memory:** the Wolfram kernel reached a peak working set of 35,243 to 35,247 MiB (34.4 GiB, 37.0 billion bytes; Part 4.4). No defect of the set was found, and no file of the set was changed. Part 6 records five observations about the environment. It also records a second verification on 2026-10-02 (clones E and L, run R1), which corrected seven statements of an earlier version of this record, and the verification of 2026-10-07 (clone S, runs S1 to S3).

## 1. What this set is and what it computes

**In plain words.** The Stage-3 study of this repository solves the field equation of `dirac16complex` in five model universes, called EXP-1 to EXP-5. `dirac16complex` is a field with 16 complex Grassmann components in eight dimensions: four space-like and four time-like directions. A Rust program, `studies/dirac16complex_cosmology`, does the solving with the CVODE solver and writes its results as CSV and JSON files into `artifacts/dirac16complex/numerics/exp1` to `exp5`; these files are committed. A Mathematica notebook, `notebooks/Dirac16ComplexDarkSector.nb`, checks those committed results independently in the Wolfram Language. A notebook is a text file that holds Wolfram Language code in *cells*; normally you open it in the desktop program Wolfram (formerly Mathematica) and evaluate it there. **This set is the program that evaluates the notebook for you without any window** (that is what "headless" means), decides whether everything passed, and says so in its last printed line and in its exit code. With the free Wolfram Engine, which has no notebook window, this is how you evaluate the notebook.

**What the verifier does, step by step** (read from its 87 lines):

1. It finds the repository root: the parent of the folder that holds the script. The folder you are in does not matter for this.
2. It reads its command-line arguments. An optional first argument is the notebook to evaluate; without it, it uses `notebooks/Dirac16ComplexDarkSector.nb` in the repository root. The optional argument `--verbose` makes it print the wall time of every cell. A literal `--` among the arguments is ignored.
3. If the notebook file does not exist, it prints `ERROR: missing notebook: <path>` and `dirac16complex_mathematica_notebook=FAILED` and exits with code 2. It then reads the notebook (`Import[path, "Notebook"]`); if that fails, it prints `ERROR: notebook import failed` and the FAILED line and exits with code 2.
4. It collects the code of every cell of style `Input`. There must be exactly **37**; otherwise it prints `ERROR: expected 37 input cells, found <n>` and the FAILED line and exits with code 1 **before evaluating anything**.
5. It evaluates the 37 cells one after the other, in one Wolfram kernel, exactly as Mathematica would evaluate them top to bottom. During the evaluation the variable `$Dirac16RepositoryRoot` holds the repository root; the notebook's first cell uses it to find every file. Each cell is wrapped in `Check[..., $Failed]`: **any message** (a warning or error printed by the kernel) makes that cell count as failed, and the text of the message is recorded. A failed cell does not stop the run; the remaining cells are still evaluated.
6. After the last cell, it reads the variable `notebookChecks` that the notebook's cell 36 creates. This is a list of 49 named checks, each `True` or `False`. There must be exactly **49** entries, and all must be `True`.
7. It prints its summary lines (Part 4.1) and exits with code **0** if no cell failed, no message was issued, there are 49 checks and all are true; otherwise it prints the details and exits with code **1**.

**The verifier does not compare anything with the committed files.** It checks only that the notebook ran cleanly and that the notebook's own 49 checks are true. Whether the report and the figures it rewrites are byte-identical to the committed ones is a separate check that you make yourself (Part 3.6, check 3); the Stage-3 gate makes it in its step `stage3-27-mathematica-unchanged`.

**What the notebook computes.** The notebook has 72 cells: 1 title, 11 section headings, 23 text cells and the 37 Input cells. Its explanations are in the text cells. The 37 Input cells, in the order in which they are evaluated, with the wall time of each cell measured with `--verbose` on the verification machine (run B1, Part 6):

| Cell | Section | What it does | Time (s) |
| --- | --- | --- | --- |
| 1 | Repository, packages and committed outputs | sets the paths from `$Dirac16RepositoryRoot`; loads the Stage-1 packages `wolfram/Dirac16ComplexAlgebra.wl` and `wolfram/Dirac16ComplexGeometry.wl`; creates `artifacts/dirac16complex/numerics/figures/mathematica/` if it is missing; reads the five `summary.json` files | 0.43 |
| 2 | Clifford data | 10 exact identities of the sixteen-by-sixteen gamma matrices, of `C` and of `B` | 0.12 |
| 3 | Clifford data | reads the matrices `GAMMA`, `CHARGE`, `CHIRALITY` and `B_IMAG` back from the Rust source `studies/dirac16complex_cosmology/src/generated.rs` and requires them to equal the package matrices exactly; compares the fixture hash recorded there with the SHA-256 of `artifacts/dirac16complex/arbitrary-field/algebra-fixture.json` (7 checks) | 0.20 |
| 4 | Tools | symbolic tools: the reduction of the covariant field equation to a mode equation, the Christoffel symbols and the mixed Einstein tensor of a metric | 0.00 |
| 5 | Tools | numerical tools: reading CSV files, the 32-real layout of a spinor, the 9-point finite-difference test `fdCheck`, `NDSolve` wrappers | 0.01 |
| 6 to 9 | EXP-1 (primordial field) | symbolic reduction and Einstein tensor; background file check with `NIntegrate`; 26 runs checked by finite differences, `NDSolve` and the exact propagator; 6 checks | 0.17, 4.07, 3.42, 0.02 |
| 10 to 12 | EXP-2 (8D Einstein cosmology) | symbolic reduction, Einstein tensor and closed-form solution; 3 runs re-integrated forward and backward, one backward run at 24-digit precision; 5 checks | 0.24, 67.34, 0.00 |
| 13 to 15 | EXP-3 (late universe, dark energy) | symbolic reduction and Friedmann equations; 10 runs re-integrated; negative control and 4 checks | 0.09, 11.86, 0.05 |
| 16 to 20 | EXP-4 (dark matter, pair creation) | symbolic reduction; 4 thermal modes re-integrated (two of them over 10^5 time units); kinetic theory with `NIntegrate`; 10 pair-creation modes; 5 checks | 0.07, 217.39, 0.47, 22.89, 0.00 |
| 21 to 23 | EXP-5 (extra-time instability) | symbolic reduction; 4 runs re-integrated, one at 32-digit precision, WKB growth; 4 checks | 0.08, 11.94, 0.00 |
| 24 | The Rust binary | runs `studies/dirac16complex_cosmology/target/release/dirac16complex_cosmology.exe print-config` (without `.exe` on macOS and Linux) with `RunProcess`; requires exit code 0, last line `SUCCESS`, and the printed fixture hash and tolerances equal to the committed ones (6 checks) | 0.05 |
| 25 | Figures | plot style and the PNG export function, which removes the PNG text chunk "Creation Time" so that repeated runs give the same bytes | 0.01 |
| 26 to 33 | Figures | the 8 figures, written as PNG files (cell 26 includes the start of the Wolfram front end, which draws them) | 8.28, 0.15, 0.12, 0.13, 0.08, 0.11, 0.24, 0.17 |
| 34 | Report | a table of the measured deviations | 0.00 |
| 35 | Report | the run parameters quoted in the text cells must equal the committed `summary.json` values (1 check) | 0.00 |
| 36 | Report | collects the 49 checks in `notebookChecks` (the last one: all 8 figures exist) and writes `artifacts/dirac16complex/numerics/mathematica-report.json` | 0.01 |
| 37 | Report | returns a `Failure` object if any check is false | 0.00 |

The sum is 350 s. Three cells take 88 % of the time: cell 17 (EXP-4 thermal modes, 62 %), cell 11 (EXP-2, 19 %) and cell 19 (EXP-4 pair creation, 7 %).

**The 49 checks**, with the names they have in `notebookChecks` and in the `checks` object of the report:

| Group | Count | Names |
| --- | --- | --- |
| Clifford algebra | 10 | `algebra_cliffordRelations`, `algebra_geometryPackageUsesSameGammas`, `algebra_chargeIsGamma0123`, `algebra_kreinIsMinusIChargeGamma4`, `algebra_kreinHermitianInvolution`, `algebra_scalarDensityOperatorBC`, `algebra_kineticOperatorBCGamma4`, `algebra_hamiltonianSquaredIsE2`, `algebra_hamiltonianHermitianInGoodSector`, `algebra_hamiltonianKreinPseudoHermitian` |
| Constants compiled into the Rust program | 7 | `rustConstants_gammaEntryCount`, `rustConstants_rustGammasEqualPackage`, `rustConstants_rustChargeEqualsPackage`, `rustConstants_rustChiralityEqualsPackage`, `rustConstants_rustKreinEqualsPackage`, `rustConstants_fixtureGammasEqualPackage`, `rustConstants_fixtureHashEqualsGeneratedHash` |
| EXP-1 | 6 | `exp1SymbolicReduction`, `exp1BackgroundFile`, `exp1FiniteDifferenceRHS`, `exp1NDSolveAgreement`, `exp1Observables`, `exp1ProfileIndependence` |
| EXP-2 | 5 | `exp2SymbolicReduction`, `exp2FiniteDifferenceRHS`, `exp2NDSolveAgreement`, `exp2NDSolveAccuracy`, `exp2RustMatchesClosedForm` |
| EXP-3 | 4 | `exp3SymbolicReduction`, `exp3FiniteDifferenceRHS`, `exp3NDSolveAgreement`, `exp3ClosedForms` |
| EXP-4 | 5 | `exp4SymbolicReduction`, `exp4InitialStates`, `exp4ThermalNDSolveAgreement`, `exp4KineticTheory`, `exp4PairNDSolveAgreement` |
| EXP-5 | 4 | `exp5SymbolicReduction`, `exp5FiniteDifferenceRHS`, `exp5NDSolveAgreement`, `exp5WKBGrowth` |
| The Rust program (`print-config`) | 6 | `engine_binaryFound`, `engine_exitCodeZero`, `engine_lastLineSUCCESS`, `engine_printedFixtureHashMatches`, `engine_summariesRecordFixtureHash`, `engine_printedTolerancesMatchSummaries` |
| Prose and figures | 2 | `textParametersMatchSummaries`, `figuresExported` |

**About the matrix `C`.** In this notebook `C` (named `chargeC` in the code, `CHARGE` in the Rust constants) is a sixteen-by-sixteen **matrix**, `C = gamma^0 gamma^1 gamma^2 gamma^3`. It is used in the Dirac adjoint `Psibar = Psi^dagger C`, and the Krein matrix is `B = -i C gamma^4`; checks `algebra_chargeIsGamma0123`, `algebra_kreinIsMinusIChargeGamma4` and `rustConstants_rustChargeEqualsPackage` verify these matrices exactly. The notebook performs no charge-conjugation operation on fields. `Conjugate[u]` appears only inside inner products of the form `u^dagger M u` (energies, densities, norms) and in the phase alignment of two spinors; `ConjugateTranspose` appears only in the Hermiticity checks of matrices.

**Documents that cite this set or its results.**

* `provenance/DIRAC16COMPLEX_DARK_SECTOR_NUMERICS.md` (with its `.tex` and `.pdf`): the abstract ("all 49 checks of a Mathematica notebook"), Section 11.2 "The Mathematica notebook" (the file table lists the verifier as the script that "evaluates it headless", the table of the maximum deviations, and the 8 Mathematica figures embedded in the verification sections 6.6, 7.6, 8.6, 9.6, 10.6 and in 11.2), Section 13 "Verification summary" (the count of 49 checks), Section 14 "Files and hashes" and Section 15 "Reproduction", which gives the command `wolframscript -file scripts/verify_dirac16complex_mathematica_notebook.wls` and says that the run rewrites `mathematica-report.json` and the figures "byte-identically". This verification confirms that statement.
* `provenance/DIRAC16COMPLEX_STUDENT_GUIDE.md` (`.tex`, `.pdf`), Section 11 "The Mathematica notebook (optional)": the same command, the expected last lines, and a run time of "about 4 to 7 minutes on the test computer, up to 10 minutes while other programs kept it busy". The measured 4.2 to 6.9 minutes of 2026-10-02, and 8.6 to 10.0 minutes of 2026-10-07 on a fully loaded computer (Part 4.4), fall in that range.
* `provenance/DIRAC16COMPLEX_TEXTBOOK.md` (`.tex`, `.pdf`) and its chapters `provenance/textbook/chapters/00-how-to-read.md` (claim L29: 49 checks of the Mathematica notebook, status COMPUTED), `10-numerical-ode.md` (Section 10.11: the figure `cross_check_deviations.png` and the negative controls read from `mathematica-report.json`), `11-dark-sector-experiments.md` (Section 11.5: 49 of 49 checks) and `19-reproducing-everything.md` (Section 19.8: the verifier is one of the files the Stage-3 gate uses).
* The Stage-3 gates `scripts/verify_stage3_dark_sector.ps1` and `scripts/verify_stage3_dark_sector.sh`, steps `stage3-26-mathematica-notebook` (runs this verifier with no argument) and `stage3-27-mathematica-unchanged` (requires the report and the 8 figures to be byte-identical to a snapshot taken at the start of the gate, ignoring only the key `engine.binary` of the report).
* `tests/test_d16c_student_guide_publication.py` (test `test_mathematica_counts`): requires the verifier to contain `expectedInputCount = 37` and `expectedCheckCount = 49`, and the committed report to have 49 true checks and 8 figures. `tests/test_d16c_numerics_publication.py` compares numbers of the committed report with the Stage-3 document.
* `artifacts/dirac16complex/numerics/mathematica-report.json` itself: its `generatedBy` field names the notebook, its builder and this verifier.
* `scripts/build_dirac16complex_mathematica_notebook.wls`, the builder that writes the notebook (a different set with its own provenance file, `provenance/wolframscript/build_dirac16complex_mathematica_notebook.PROVENANCE.md`). The builder only writes the notebook file; it never evaluates it. Its write steps were made to fail with exit code 1 when a file cannot be written (commit `3f0a577`, 2026-10-02); on 2026-10-07 the changed builder still wrote a notebook byte-identical to the committed one (Part 6).
* `scripts/verify_dirac16complex_ks_mathematica_notebook.wls`, the headless verifier of the Stage-4 notebook `notebooks/Dirac16ComplexKohnSham.nb`, names this verifier as its pattern in its header. It does not run this verifier.

## 2. Files

### 2.1 The script

| File | Role | sha256 | Size |
| --- | --- | --- | --- |
| `scripts/verify_dirac16complex_mathematica_notebook.wls` | the verifier (this set; unchanged since commit `fbec4d7` of 2026-09-25) | `eba66d9297f933d348f25a0fa0d2c31a2cfd2a4db258325d21c3b6c4a1e32a7d` | 87 lines, 4452 bytes, ASCII, LF line ends, ends with a newline |

The set has no other script and no package of its own.

### 2.2 Inputs

Everything the run reads, with the sha256 at commit `c2b33cc`. "Lines" counts line-feed characters. The table is also exact at commit `8cbd03a`: on 2026-10-07 a script read every row of the table and hashed each file in a fresh clone of `8cbd03a`, and all 59 files agreed in sha256, bytes and lines (Part 6).

**When each input was last changed** (measured with `git log -1 -- <file>`):

* the notebook in commit `fbec4d7` (2026-09-25 13:04 -0700). That commit also last wrote the committed report and the 8 figures of Part 2.3.
* the two packages and 52 of the CSV and JSON files in `6c0bfad` (2026-09-25 11:46 -0700).
* `generated.rs` and `algebra-fixture.json` in `78b4a5f` (2026-09-25 10:09 -0700).
* `exp4/summary.json` and `exp4/pair_spectrum.csv` in `571f9a7` (2026-09-26 16:58 -0700). This is **after** the committed report and figures were generated. `exp4/summary.json` was also changed in between, in `4480b06` (2026-09-25 17:39 -0700).

These two later changes leave everything the notebook reads unchanged:

* `pair_spectrum.csv` gained three columns at the end (`a_end_smooth`, `beta2_end_smooth`, `beta2_adiabatic_end_smooth`). Its first 11 columns kept the same value in all 321 rows, and the notebook selects columns by name (`m`, `node`, `k`, `beta2_end`).
* `summary.json` gained 116 keys and lost the 5 keys `pair.masses[i].nA3Adiabatic`. It changed 22 values: the pair-creation results `pair.masses[i].nA3`, `rhoA3End`, `wFrozenSpectrumAtA1` and `wEnd`, and `solverTotals.steps` and `rhsEvaluations`. The notebook reads from this file only `parameters`, `verdict`, `fixture.sha256` and `tolerances.rtol`, and none of these changed.

This is why the committed report and figures, which were generated at `fbec4d7`, are still reproduced byte for byte at `c2b33cc` and at `8cbd03a` (Part 6).

| File | Read by | sha256 | Bytes | Lines |
| --- | --- | --- | --- | --- |
| `notebooks/Dirac16ComplexDarkSector.nb` | the verifier (the 37 Input cells) | `708804e7f4bb902221418ebcfcbbb5e91abcc9bf4773f067bfa61e6f2e304ffe` | 354930 | 5048 (no newline after the last line) |
| `wolfram/Dirac16ComplexAlgebra.wl` | cell 1 (`Get`) | `ba0d00c818fa3707f04f7b2a7478b0c635fbf9fdaaa08b2e036d2704180f2262` | 82215 | 1299 |
| `wolfram/Dirac16ComplexGeometry.wl` | cell 1 (`Get`) | `f5b674665eee4000750161e6ab6312c38bfac9da7a17450a2b3bdd88ef292af2` | 71636 | 997 |
| `studies/dirac16complex_cosmology/src/generated.rs` | cell 3 | `29631bcd9e737b5fe57a41ae2750c7637e31580974577d34b26ada45c560a3ba` | 17391 | 239 |
| `artifacts/dirac16complex/arbitrary-field/algebra-fixture.json` | cell 3 (content and SHA-256) | `8b4f15462ca4d61ef6ec0e72f04c8a77d23ce8bcabc9b6ce19f921c90e02653b` | 213133 | 18440 |
| `artifacts/dirac16complex/numerics/exp1/summary.json` | cells 1, 7, 8, 26, 27, 35 | `f8886625011a35c5ea31c89ffb623e4c6b0678adc300fc4b725179808601272a` | 54498 | 1627 |
| `artifacts/dirac16complex/numerics/exp1/background_A1.csv` | cells 7, 27 | `72bd5d384aeba962399298a43116d0856f9f030957e67b62c8c66693d493bd0f` | 87497 | 202 |
| `artifacts/dirac16complex/numerics/exp1/background_A2.csv` | cells 7, 27 | `6af0c40f2129eaed6df24f36d8df102a506a4d178bd5af58c5d92ae5d4fe22fb` | 87497 | 202 |
| `artifacts/dirac16complex/numerics/exp1/run_A1_K0_pos_Bp.csv` and `run_A2_K0_pos_Bp.csv` | cell 8 | `65f3d5eb2ed50135d800847824b3e1578a00702152c3dd64c951ac878560e460` (both) | 261696 | 202 |
| `.../exp1/run_A1_K0_pos_Bm.csv` and `run_A2_K0_pos_Bm.csv` | cell 8 | `d4d656dc8c8185dba84194d4d50a07e76492f1d2ef86ca27165878631a0eef1f` (both) | 261919 | 202 |
| `.../exp1/run_A1_K0_neg_Bp.csv` and `run_A2_K0_neg_Bp.csv` | cell 8 | `682116b7fdfc4f177e9f2c52827e87e8f0a294e1f0a47850aeb0604b4a712443` (both) | 262824 | 202 |
| `.../exp1/run_A1_K0_mix.csv` and `run_A2_K0_mix.csv` | cell 8 | `ec2e042b87ee574dc0ef3c32a5241e32cd9b18c3c0cd5eb1a492f05be1c47dfb` (both) | 264376 | 202 |
| `.../exp1/run_A1_K0p5_pos_Bp.csv` and `run_A2_K0p5_pos_Bp.csv` | cell 8 | `073ba39a2b6fb46426a1771e2dd80c1b8d81fb6f4d4f9a0d90b9e756934c543c` (both) | 262583 | 202 |
| `.../exp1/run_A1_K0p5_pos_Bm.csv` and `run_A2_K0p5_pos_Bm.csv` | cell 8 | `4866ad7cd5772608b92393d3d329fac935237ed19e18763ff070d0e70cfec956` (both) | 262825 | 202 |
| `.../exp1/run_A1_K0p5_neg_Bp.csv` and `run_A2_K0p5_neg_Bp.csv` | cell 8 | `fe46e88017ffb9b47fa4c5828f25322273e60e00d387d92860c60a1ae370a5f3` (both) | 264241 | 202 |
| `.../exp1/run_A1_K0p5_mix.csv` and `run_A2_K0p5_mix.csv` | cell 8 | `a932ea73d3487f1fd3eb4b1d5c4d64476312b10c32ff0d5223cb95174b81b6e8` (both) | 264606 | 202 |
| `.../exp1/run_A1_K2_pos_Bp.csv` and `run_A2_K2_pos_Bp.csv` | cell 8 | `9fd75876efe3a60a5cb0a67e256f5cfd5a938937e92814601af1d429387a1ced` (both) | 262579 | 202 |
| `.../exp1/run_A1_K2_pos_Bm.csv` and `run_A2_K2_pos_Bm.csv` | cell 8 | `ca38bffcd4789bc44c6ebad3df0355d52a2a12ce7ba1503a47a2c092e5c78f09` (both) | 262664 | 202 |
| `.../exp1/run_A1_K2_neg_Bp.csv` and `run_A2_K2_neg_Bp.csv` | cell 8 | `60baea6eba425757bf21a4d8973e555e7d95c5ad9455bfc80d4e00a5393555c1` (both) | 264329 | 202 |
| `.../exp1/run_A1_K2_mix.csv` and `run_A2_K2_mix.csv` | cells 8, 26 | `dabaf32fe63166ed9cd8a0d46f41cd7966f6b53351243c5d81a8652625b391b3` (both) | 264666 | 202 |
| `.../exp1/run_A1_K0p5_pos_Bp_lambda0p5.csv` and `run_A2_K0p5_pos_Bp_lambda0p5.csv` | cell 8 | `2ff5aa5f634cf7d9a09952997a5e225c552100715b3476056f0136080cfb9a52` (both) | 262567 | 202 |
| `artifacts/dirac16complex/numerics/exp2/summary.json` | cells 1, 11, 35 | `c8f7ecd95f7414f81e2569be7a41f2127d0c1cbd3a7a07b2c0dbcb667c43d5d0` | 16239 | 411 |
| `.../exp2/run_x0_0.csv` | cell 11 | `a9ed3272c5ee7b96f76f056b2b0cb0b59a3e29ab7055510fed7aa3fe6ca9f71d` | 714882 | 512 |
| `.../exp2/run_x0_m0p4.csv` | cell 11 | `a2108e2cf1a09dee950e17444de835e2c8e2726f902de2ef34267fcc661d0b2f` | 716609 | 512 |
| `.../exp2/run_x0_0p5.csv` | cell 11 | `e3c0f829981298d2bb7bbcca2004c11b505db501a3d90327c01028638b05f7af` | 714595 | 512 |
| `artifacts/dirac16complex/numerics/exp3/summary.json` | cells 1, 14, 15, 35 | `7bfedf4bd5e5765c171dcc71896e4a9f481bfedfeafa6ddae04b924ca31081ee` | 35847 | 1068 |
| `.../exp3/run_x0_m0p462654_mu3.csv` | cells 14, 15 | `7f696ee4b840ecfbc7bcb313ec60ecc57a02f924af80a5bdd3dc265d7971d624` | 372429 | 243 |
| `.../exp3/run_x0_m0p462654_mu7.csv` | cell 14 | `97bfb6c736b0dfd3e94ffb076a4eccd5a762455c75bf6b96371668a82ab32ae5` | 372389 | 243 |
| `.../exp3/run_x0_m0p433107_mu3.csv` | cell 14 | `2849674de5ce63193399237b09a3e06722e7d615896805e459abeceef80b9505` | 381741 | 249 |
| `.../exp3/run_x0_m0p433107_mu7.csv` | cell 14 | `9fb641d7bc2d3646d46f80f74dc1778eb21255e476f0f4fd89854248ba856257` | 381687 | 249 |
| `.../exp3/run_x0_m0p3_mu3.csv` | cell 14 | `27b7cfd34446dc630fafb00f6b557e9168e186f4f97acf163c1b936baceb407b` | 436004 | 284 |
| `.../exp3/run_x0_m0p3_mu7.csv` | cell 14 | `c243b3eda126d81aa10c90dbdac06fcab56deb9373af3320c2a3001fb783dfa5` | 435954 | 284 |
| `.../exp3/run_x0_m0p2_mu3.csv` | cell 14 | `5a47dd6946a5b379faf44e99c4540f1df6b4f8899ccc915a25d5fd448a65b632` | 494812 | 322 |
| `.../exp3/run_x0_m0p2_mu7.csv` | cell 14 | `650ab9acc928664de88224e95e995a33601d741535844f9ff08f8d2e3689a9cb` | 494770 | 322 |
| `.../exp3/run_x0_0_mu3.csv` | cell 14 | `9dfdb94a2020081869e35ffc86e8676ce9b53a180a0625351219fcbad3708c63` | 739774 | 482 |
| `.../exp3/run_x0_0_mu7.csv` | cell 14 | `6bce853deeb8ebef9e07cdb40bccb4772299af233591480c631e5528541ed2bc` | 739572 | 482 |
| `artifacts/dirac16complex/numerics/exp4/summary.json` | cells 1, 16, 35 | `c648518ed5ba4693bf6d271de3ee294a330daf9f15e669e17fa43519c1a9f8ec` | 30906 | 814 |
| `.../exp4/thermal_modes.csv` | cell 17 | `f9ae33f20d079cf679ecc3dffc528d78bf7dae937bf0be6245e5938dfeb6a5ed` | 3256013 | 2929 |
| `.../exp4/thermal_eos.csv` | cells 18, 30 | `133bf3663fb730a958e531e07e6f9086ca8f2debbf3248705bfe59a5be485b8a` | 29518 | 62 |
| `.../exp4/pair_modes.csv` | cell 19 | `1d8a871be085ef8263ff712fda9fd6cb1e08c1ff2152e5c70898eba5b51d31aa` | 2844263 | 2561 |
| `.../exp4/pair_spectrum.csv` | cells 19, 31 | `be59b6901eaaa4498cd81342f70db6c94896cd6362381ff868b4409eebf1184f` | 108014 | 321 |
| `artifacts/dirac16complex/numerics/exp5/summary.json` | cells 1, 22, 35 | `bbddd4d4e0303c72d8d13494e2f4a54a730f0687fdba54a240156c7b0cfb1746` | 7381 | 219 |
| `.../exp5/run_q0p05_Cp.csv` | cell 22 | `6b3b0bfb210c25792d2cee266ba3e1a518398d3ae96f242d6f71a3da5eda2a27` | 611355 | 602 |
| `.../exp5/run_q0p05_Cm.csv` | cell 22 | `c97184ad5c60a787e84ebbdd32459090bd2a210e0301b8a2c8ad7225e93521d6` | 613143 | 602 |
| `.../exp5/run_q0p1_Cp.csv` | cell 22 | `f11b22c767edb9b15d822a7493abc8af4730d4bd0005048b7cf67a9ceae24c86` | 611476 | 602 |
| `.../exp5/run_q0p1_Cm.csv` | cell 22 | `4ba950feb743ba286f4989edb26ea7f591dbd6e1a8b1fe9486124bae40d93fd2` | 613109 | 602 |

`...` stands for `artifacts/dirac16complex/numerics`. That is 59 files with 23,585,029 bytes in all (58 files and 23,230,099 bytes besides the notebook). The 13 EXP-1 runs with amplitude A = 2 are byte-identical to their A = 1 twins, as the table shows; this is what check `exp1ProfileIndependence` tests (the spinor equation does not contain the background profile).

**One input that is not in the repository: the compiled Rust program** `studies/dirac16complex_cosmology/target/release/dirac16complex_cosmology.exe` (Windows; without `.exe` on macOS and Linux). Cell 24 runs it once as `dirac16complex_cosmology print-config` with the repository root as working directory. You build it yourself (Part 3.4). Its bytes are not reproducible from clone to clone: the three builds of this verification (clones A, B and C) had three different sha256 (`381f6ff1...`, `4a8c0278...` and `69b1526b...`) at the same size of 1,721,344 bytes, because the program contains the absolute path of the folder it was built in (the string `cloneA` occurs 14 times in the first one). The build of 2026-10-07 (clone S, Part 6) had a fourth sha256, `53149a2d...`, at the same size. This does not matter: the notebook uses only what `print-config` prints, and those 31 lines were byte-identical in the four clones (sha256 `02b053b9a4d5c2113f204de33fe885e785801ddfbc2c20b83442d2a6156d1594`).

The run reads no other file of the repository. It needs no Python, and, apart from the possible download of an optional Wolfram component described in Part 5, no internet access.

### 2.3 Outputs

Every run **overwrites** these 9 committed files (default notebook; the paths are fixed in the notebook and do not depend on the notebook argument):

| File | sha256 (committed, and after every successful run) | Bytes |
| --- | --- | --- |
| `artifacts/dirac16complex/numerics/mathematica-report.json` | `6047dd48cad77fbcf45486046cb19e0a98fddd6ef0db9181459431d7d39062d6` | 15352 (415 lines, ASCII, tab-indented, LF, ends with a newline) |
| `artifacts/dirac16complex/numerics/figures/mathematica/exp1_mixed_state_rho_p0.png` | `08bca286ef833db3699dee6091d86b9269c645c9aa3b356c97be51c09274f6df` | 103859 (1162 x 837 pixels) |
| `artifacts/dirac16complex/numerics/figures/mathematica/exp1_einstein_requirement.png` | `d392d7c998dad666a14b0d7acc155cf2035c712f9df13c9c909591be7f255516` | 71122 (1162 x 837) |
| `artifacts/dirac16complex/numerics/figures/mathematica/exp2_anisotropy_fractions.png` | `638763e14ffd8b20c3d238c0819878d1f775538ffcf80c7a396916750bae8a4c` | 77277 (1162 x 837) |
| `artifacts/dirac16complex/numerics/figures/mathematica/exp3_equation_of_state.png` | `e83e62a6c9c85ed3c38c4a4f182f2cab34117ccf68c2c83c00ceb12f52fd1b2d` | 88761 (1162 x 870) |
| `artifacts/dirac16complex/numerics/figures/mathematica/exp4_thermal_equation_of_state.png` | `e242eb85ab77ab1b148af9dc32dc0f5447d97a3ae6ada34f0a09909d5d1bbd50` | 57732 (1162 x 837) |
| `artifacts/dirac16complex/numerics/figures/mathematica/exp4_pair_spectrum.png` | `7549dad887438e4e0f30a3f2cac1f2fd9964f0ed41189db844b6c4a08f23ec45` | 79820 (1162 x 837) |
| `artifacts/dirac16complex/numerics/figures/mathematica/exp5_hilbert_norm_growth.png` | `6495b0f0aaf5fcd5b4e67fd197b95d514cd3ed676de394778020d46967eff520` | 73883 (1162 x 837) |
| `artifacts/dirac16complex/numerics/figures/mathematica/cross_check_deviations.png` | `3d2cb511b1da0b5d33ee39ad595f4f5c91e2dc26de18d83e08fab735b2e036b6` | 49527 (1162 x 664) |

The PNG files are 8-bit RGB images whose only text chunk is `Software: Created with the Wolfram Language : www.wolfram.com`; the notebook removes the chunk `Creation Time`, which would otherwise change from run to run. The report contains no time stamps and no absolute paths.

If the folder `artifacts/dirac16complex/numerics/figures/mathematica/` is missing, cell 1 creates it. Nothing else is written into the repository.

## 3. How to run it

### 3.1 What you need

| What | Why | Tested version |
| --- | --- | --- |
| The Wolfram Engine (free) or Wolfram/Mathematica, with WolframScript | evaluates the notebook | Wolfram 15.0.1, WolframScript 1.14.0 |
| Git | downloads the repository and the solver engine, and compares the results with the committed files | 2.51.2.windows.1 |
| Rust (rustup, cargo) and a C linker | builds the Rust program that cell 24 runs | cargo and rustc 1.91.1 |
| **About 35 GiB (37 GB) of free memory (RAM)** | the kernel's working set reached 35,246 MiB in cell 17 (Part 4.4) | the verification machine has 191.4 GiB (205.6 GB) |
| About 640 MB of free disk (1 MB = 1,000,000 bytes) | repository 538 MB (of which 134 MB Git history), solver engine 83 MB, Rust build 16 MB | measured with `du -sb`: 637 MB in all |
| An internet connection | only to download Wolfram, Rust, the repository and the solver engine; the run itself needs none | |

You do **not** need Python, Jupyter or a notebook window. Type every command below exactly as shown. A line in a grey box is one command: type it and press Enter.

### 3.2 Install the Wolfram Engine (free) or Wolfram/Mathematica, and WolframScript

You need two programs. The first is the Wolfram Language *kernel*, the program that does the computing. The second is *WolframScript*, the command `wolframscript`, which runs a script file with the kernel.

**Option 1: the free Wolfram Engine for Developers.**

1. In a web browser, open https://www.wolfram.com/engine/ and download the Wolfram Engine for your operating system. You need a free Wolfram ID (an e-mail address and a password) and the free developer licence offered on that page. Create both when asked, and read the licence terms.
2. Install it.
   * Windows: run the downloaded installer and accept the defaults. Instead, in PowerShell, you can type `winget install --id WolframResearch.WolframEngine -e`. On 2026-10-02, `winget show --id WolframResearch.WolframEngine -e` listed version 15.0.0 for this package; the installer was not executed for this record. The installer also installs WolframScript and adds it to the PATH. Afterwards, close every PowerShell window and open a new one.
   * macOS: open the downloaded `.dmg` file and follow its instructions: drag the application into Applications and open it once.
   * Linux: open a terminal in the download folder and run the downloaded installer with `sudo bash <name of the downloaded file>.sh`, accepting the defaults.
   * If after the installation the command `wolframscript` is "not recognized" or "not found" (most likely on macOS and Linux), download and install WolframScript separately from https://www.wolfram.com/wolframscript/, then open a new terminal. The download is a `.msi` file for Windows and a `.pkg` file for macOS. For Linux it is a `.deb` file (install with `sudo apt install ./<file>.deb`) or a `.rpm` file (install with `sudo dnf install ./<file>.rpm`).
3. Activate it. In a terminal (PowerShell on Windows, Terminal on macOS and Linux), type

   ```
   wolframscript -activate
   ```

   and enter your Wolfram ID and password when asked. If you see the prompt `In[1]:=` instead, the engine is already active: type `Quit[]` and press Enter.

**Option 2: Wolfram (formerly Mathematica), the desktop product.** A licensed installation contains the kernel and, on Windows and Linux, also `wolframscript`. Start the desktop program once to activate it. If `wolframscript` is not found (typically on macOS), install WolframScript separately as in step 2 above.

**Test the installation.** In a new terminal, type

```
wolframscript -code '$Version'
```

It must print the kernel version, for example `15.0.1 for Microsoft Windows (64-bit) (July 2, 2026)` on the verification machine. The single quotes matter on macOS and Linux, because they stop the shell from replacing `$Version`; they are also correct in PowerShell. `wolframscript -version` prints the WolframScript version, for example `WolframScript 1.14.0 for Microsoft Windows (64-bit)`.

### 3.3 Install Git and Rust

**Windows 11, in PowerShell.** First install the Microsoft C++ build tools (the linker that Rust needs on Windows), then the other tools:

```
winget install --id Microsoft.VisualStudio.2022.BuildTools -e --override "--wait --passive --add Microsoft.VisualStudio.Workload.VCTools --includeRecommended"
winget install --id Git.Git -e
winget install --id Microsoft.PowerShell -e
winget install --id Rustlang.Rustup -e
```

Close every terminal, open a new one, and type `rustup default stable`. (These installers were not executed for this record; on 2026-10-02 `winget show` listed rustup 1.29.1.) The Windows commands below were tested in **PowerShell 7** (the program `pwsh`, installed by the third line). If you have only the older Windows PowerShell 5.1, which blocks scripts by default, run the solver set-up script of Part 3.4 as `powershell -ExecutionPolicy Bypass -File scripts/setup_solver.ps1 -Platform win11` instead (not tested for this record).

**macOS, in Terminal.** Install the command line developer tools (they contain Git and the linker), then Rust, and load Rust into the current terminal:

```
xcode-select --install
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source "$HOME/.cargo/env"
```

**Linux (Ubuntu or Debian), in a terminal:**

```
sudo apt update
sudo apt install -y git curl build-essential
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source "$HOME/.cargo/env"
```

Check: `git --version` and `cargo --version` must each print a version number.

### 3.4 Get the repository, the solver engine, and build the Rust program

Do this once.

**On Windows, first choose a folder with a short path**, for example `C:\src`. To create it and go there, type `mkdir C:\src` and then `cd C:\src`. The full path of the repository folder may have **at most 156 characters**; with a longer path the build below fails with `LNK1104` (Part 3.7). `C:\src\Dirac_claude` has 19 characters. After cloning, you can check the length by typing `(Get-Location).Path.Length` in PowerShell in the repository folder. On macOS and Linux there is no such limit.

In the folder where you want the repository, type:

```
git clone https://github.com/once-ere/Dirac_claude.git
cd Dirac_claude
```

The clone took 9 seconds on the verification machine. Type every command below in this folder, the *repository root*: the folder that contains `scripts`, `notebooks`, `wolfram` and `studies`. The repository's `.gitattributes` turns off line-end conversion, so every file arrives with exactly the committed bytes, even when Git is set up with `core.autocrlf=true` (as on the verification machine).

**Fetch the pinned solver engine** (83 MB, a few seconds). The Rust program cannot be built without it. Windows, in PowerShell 7:

```
pwsh -NoProfile -File scripts/setup_solver.ps1 -Platform win11
```

macOS, Linux, and Git Bash on Windows:

```
bash scripts/setup_solver.sh win11
```

It must print these three lines (measured: 5.0 to 5.8 s in PowerShell, 4.7 s in Git Bash):

```
solver_platform=win11
solver_commit=a8fdff459adfe181573d7924b18bffbdf378fdb3
solver_setup=OK
```

If you run the set-up a second time, the engine is already there. The first two lines are the same, the last line is `solver_setup=ALREADY-PRESENT` and the exit code is 0 (measured: 0.3 s in PowerShell, 1.9 s in Git Bash). **This also means success.** If instead the scripts report an error ending in `remove it and rerun`, delete the folder `vendor/rustSolveIt` and run the set-up again. There are two such errors: `vendor/rustSolveIt is an incomplete checkout (an interrupted or failed download)` and `vendor/rustSolveIt is at <commit>, expected <commit>`. The PowerShell script writes `vendor\rustSolveIt` instead. Both errors exit with code 1. (These two errors were read from the scripts, not tested.) To delete the folder, type `Remove-Item -Recurse -Force vendor/rustSolveIt` in PowerShell, or `rm -rf vendor/rustSolveIt` on macOS and Linux.

Use the argument `win11` on every platform; it is the engine that produced the committed results. (For this notebook the choice of engine does not change any number: the notebook runs the program only to print its configuration, cell 24.)

**Build the Rust program** (the same command in every shell; measured 8.6 to 13 s):

```
cargo build --manifest-path studies/dirac16complex_cosmology/Cargo.toml --release
```

The last line must start with `Finished`. The program is then `studies/dirac16complex_cosmology/target/release/dirac16complex_cosmology.exe` on Windows, and the same path without `.exe` on macOS and Linux. You can try it: on Windows, `studies/dirac16complex_cosmology/target/release/dirac16complex_cosmology.exe print-config`; on macOS and Linux, `studies/dirac16complex_cosmology/target/release/dirac16complex_cosmology print-config`. It prints 31 lines of settings; the last one must be `SUCCESS`. **If you skip the build, the verifier fails** (Part 3.7, second row).

### 3.5 Run it

The usage line in the script's header is

```
wolframscript -file scripts/verify_dirac16complex_mathematica_notebook.wls [notebook.nb] [--verbose]
```

The square brackets mean that both arguments are optional; you do not type the brackets. Without a notebook argument the verifier evaluates `notebooks/Dirac16ComplexDarkSector.nb`, which is what you want.

**Windows PowerShell** (tested with PowerShell 7.6.6):

```
wolframscript -file scripts/verify_dirac16complex_mathematica_notebook.wls
$LASTEXITCODE
```

**macOS Terminal (zsh) or Linux terminal (bash)**, and also Git Bash on Windows (tested):

```
wolframscript -file scripts/verify_dirac16complex_mathematica_notebook.wls
echo $?
```

The second line prints the exit code, which must be `0`. The run takes 4 to 7 minutes, and up to about 10 minutes when the computer is busy with other work (Part 4.4); during that time nothing is printed; the 8 result lines appear together at the end. Do not close the terminal and do not press Ctrl+C. To time it, type `Measure-Command { wolframscript -file scripts/verify_dirac16complex_mathematica_notebook.wls | Out-Host }` in PowerShell, or put `time ` in front of the command in bash or zsh.

**Variants (all tested).**

* `wolframscript -file scripts/verify_dirac16complex_mathematica_notebook.wls --verbose` also prints one line per cell, for example `cell 17 time=217.39000000000001 failed=False messages=0`, before the result lines. With this flag WolframScript itself also prints three lines of its own on the error stream: `Performing '-file' parsing. File->scripts/verify_dirac16complex_mathematica_notebook.wls`, `Local Evaluation` and `Using wolfram.exe at:"C:/Program Files/Wolfram Research/Wolfram/15.0.1/wolfram.exe"` (on Windows). They are harmless.
* `wolframscript -file scripts/verify_dirac16complex_mathematica_notebook.wls notebooks/Dirac16ComplexDarkSector.nb` names the notebook explicitly and gives the same result. A relative notebook path is taken relative to the folder you are in.
* You may run the script from another folder if you give its full path, for example `wolframscript -file C:\Users\you\Dirac_claude\scripts\verify_dirac16complex_mathematica_notebook.wls`: the script finds the repository from its own location. A *relative* script path, however, works only from the repository root (Part 3.7).

### 3.6 Check the result

Checks 1, 2 and 4 must succeed on every computer. Check 3 is exact only on Windows with Wolfram 15.0.1. On macOS and Linux it shows one expected difference, explained at its end.

1. **The printed lines** must be those of Part 4.1, ending with `dirac16complex_mathematica_notebook=OK`, with `failed_evaluation_count=0`, `message_count=0`, `notebook_check_count=49` and `failed_notebook_check_count=0`.
2. **The exit code** must be `0`. Do not rely on the exit code alone: if WolframScript cannot even find the script, it prints `Failed to open file at path: ...` and still gives exit code 0 (Part 3.7). Always read the last line.
3. **The rewritten files equal the committed ones (Windows).** Type

   ```
   git status --porcelain
   ```

   On Windows it must print nothing. (The folders `vendor/rustSolveIt` and `studies/dirac16complex_cosmology/target` that your preparation created do not appear, because Git ignores them.) For a stricter check of the report, print its sha256 fingerprint, which must be `6047dd48cad77fbcf45486046cb19e0a98fddd6ef0db9181459431d7d39062d6`:
   * Windows PowerShell: `(Get-FileHash artifacts/dirac16complex/numerics/mathematica-report.json -Algorithm SHA256).Hash` (PowerShell prints the same value in capital letters, `6047DD48...`);
   * macOS: `shasum -a 256 artifacts/dirac16complex/numerics/mathematica-report.json`;
   * Linux and Git Bash: `sha256sum artifacts/dirac16complex/numerics/mathematica-report.json`.

   The fingerprints of the 8 figures are in Part 2.3.

   **On macOS and Linux this check never gives an empty result, and that is expected.** The report records the program's file name in its key `engine.binary`, and there the name has no `.exe`. So `git status --porcelain` prints ` M artifacts/dirac16complex/numerics/mathematica-report.json`, and the report's sha256 differs from `6047dd48...`. Type `git diff artifacts/dirac16complex/numerics/mathematica-report.json`. It should show the committed line `"binary":"studies/dirac16complex_cosmology/target/release/dirac16complex_cosmology.exe",` replaced by the same line without `.exe`. Other numbers may also differ in their last digits, and PNG files may be listed as changed (Part 4.5); neither is a failure. On macOS and Linux, and with any Wolfram version other than 15.0.1, only checks 1, 2 and 4 decide. (This was read from the notebook's code, cell 24 and cell 36; it was not tested on macOS or Linux.)
4. **The summary lines of the report.** Windows PowerShell:

   ```
   Select-String -Path artifacts/dirac16complex/numerics/mathematica-report.json -Pattern '"checkCount"|"verdict"'
   ```

   macOS, Linux and Git Bash:

   ```
   grep -E '"checkCount"|"verdict"' artifacts/dirac16complex/numerics/mathematica-report.json
   ```

   The output must contain `"checkCount":49,` and `"verdict":"SUCCESS"` (PowerShell puts the file name and line numbers 413 and 414 in front).
5. **Look at the figures** (optional): open the 8 PNG files in `artifacts/dirac16complex/numerics/figures/mathematica/` with any image viewer. In each, dots are the Rust results and lines the Mathematica recomputation; they lie on top of each other.

### 3.7 If it fails

| What you see | Likely cause | What to do |
| --- | --- | --- |
| `wolframscript` is not recognized / `command not found` | WolframScript is not installed or not on the PATH | Install it (Part 3.2). On Windows you can add its folder for the current session with `$env:Path += ";C:\Program Files\Wolfram Research\WolframScript"`. On macOS and Linux, find it with `find / -name wolframscript -type f 2>/dev/null` and add its folder with `export PATH="<folder>:$PATH"`. |
| `Part::take: Cannot take positions -3 through -1 in {}.` above the result lines, then `failed_evaluation_count=1`, `message_count=1`, `failed_notebook_check_count=5`, `failed_cells=24`, `messages=cell 24: HoldForm[Part::take]`, `failed_checks=engine_binaryFound,engine_exitCodeZero,engine_lastLineSUCCESS,engine_printedFixtureHashMatches,engine_printedTolerancesMatchSummaries`, `dirac16complex_mathematica_notebook=FAILED`, exit code 1 (measured, run C1) | The Rust program was not built, so cell 24 found no program to run | Build it (Part 3.4). This failed run has **overwritten the committed report** with a report whose verdict is `FAILURE` (13 lines differ: the engine checks are `false`, `exitCode` is `-1`, `lastLine` is empty); all other numbers and the 8 figures were unchanged. Restore it with `git checkout -- artifacts/dirac16complex/numerics/mathematica-report.json` and run the verifier again. |
| `No more memory available.`, `Mathematica kernel has shut down.`, `Try quitting other applications and then retry.`, then `The product exited because an error occurred. For a product older than 12.1, this can mean that the product is unregistered.`, exit code 1, **no** result lines (measured, run B2, with the kernel limited to 8 GiB: it stopped after 44 s, in cell 11) | Not enough memory: the run needs about 35 GiB, that is 37 GB (Part 4.4) | Close other programs, or use a computer with more memory. The memory need cannot be lowered without changing the notebook. Because the kernel stopped before cell 26, no file was changed. With less memory than needed, the operating system may instead move memory to disk; the run then becomes very slow (not tested). |
| `Failed to open file at path: scripts/verify_dirac16complex_mathematica_notebook.wls`, exit code **0** (measured) | You are not in the repository root | `cd` into the `Dirac_claude` folder (Part 3.4) and run again. Note that the exit code 0 is misleading here: WolframScript did not run anything. |
| `ERROR: missing notebook: <path>` and `dirac16complex_mathematica_notebook=FAILED`, exit code 2 (measured) | The notebook argument names a file that does not exist | Leave out the argument, or correct the path. |
| ``error: failed to load manifest for dependency `cvode_rs` `` ... `The system cannot find the path specified. (os error 3)` from `cargo build`, exit code 101 (measured) | The solver engine was not fetched | Run the set-up script of Part 3.4 first, then build. |
| ``error: linker `link.exe` not found`` from `cargo build` (Windows; not tested) | The Microsoft C++ build tools are missing | Install them (first line of the Windows commands in Part 3.3), open a new terminal, build again. |
| ``error: linking with `link.exe` failed: exit code: 1104`` with `LINK : fatal error LNK1104: cannot open file '...\target\release\deps\libdirac16complex_cosmology-<16 hex digits>.rlib'` (or `...\target\release\deps\dirac16complex_cosmology.exe`), then ``error: could not compile `dirac16complex_cosmology` ``, from `cargo build` (Windows, exit code 101; measured) | The path of the repository folder is too long. The Microsoft linker cannot open a file whose full path has 260 characters or more. This happens even when Windows long paths are switched on (`LongPathsEnabled` was 1 on the verification machine). The longest path the linker opens is the repository path plus 103 characters, so the repository path may have at most 156 characters. Measured: a 139-character repository path built. Paths of 163 characters (the `.rlib` was named) and 179 characters (the `.exe` was named) failed. A build folder with an `.rlib` path of exactly 259 characters built; one of 260 characters failed. | Type `(Get-Location).Path.Length` in the repository folder to see its length. Clone the repository again into a short folder, for example `C:\src` (`mkdir C:\src`, `cd C:\src`, then the commands of Part 3.4), and build there. |
| A request for a Wolfram ID, or a message that the kernel is not activated or that no licence is available | The engine was never activated, or the licence expired | Run `wolframscript -activate` once (Part 3.2). The free Engine renews its licence over the internet from time to time. |
| A message that too many kernels are running, or that a kernel could not be launched | The free licence limits how many kernels may run at the same time | Close other Wolfram programs and run again. This verifier needs one kernel for 4 to 10 minutes. |
| `ERROR: expected 37 input cells, found <n>` or `ERROR: expected 49 notebook checks, found <n>` | The notebook was changed (for example saved from Mathematica after editing) | Restore it with `git checkout -- notebooks/Dirac16ComplexDarkSector.nb`. |
| Any other `messages=...` line, `failed_cells=...` or `failed_checks=...`, verdict FAILED | A check of the physics failed, or a committed input was changed | `git status --porcelain` shows which files differ from the committed ones; restore them with `git checkout -- <file>`. If nothing was changed and you use another Wolfram version (Part 4.5), report the printed lines. |
| Everything is OK, but `git status --porcelain` shows ` M artifacts/dirac16complex/numerics/mathematica-report.json` or a changed PNG | Another Wolfram version or another operating system (Part 4.5) | This alone is not a failure: the verdict decides. `git diff artifacts/dirac16complex/numerics/mathematica-report.json` shows which values changed. Restore the committed files with `git checkout -- artifacts/dirac16complex/numerics`. |

## 4. Expected output

### 4.1 Printed lines and exit code

A successful run prints exactly these 8 lines on standard output and nothing on standard error:

```
input_cell_count=37
failed_evaluation_count=0
message_count=0
notebook_check_count=49
failed_notebook_check_count=0
report=<repository root>\artifacts\dirac16complex\numerics\mathematica-report.json
elapsed_seconds=<about 250 to 560>
dirac16complex_mathematica_notebook=OK
```

**The exit code is 0.** What the lines mean:

| Line | Meaning | Must be |
| --- | --- | --- |
| `input_cell_count` | Input cells found in the notebook | 37 |
| `failed_evaluation_count` | cells that returned `$Failed` or issued a message | 0 |
| `message_count` | different messages issued by the kernel | 0 |
| `notebook_check_count` | entries of `notebookChecks` | 49 |
| `failed_notebook_check_count` | checks that are not `True` | 0 |
| `report` | the absolute path of the report written by cell 36 (`missing` if no report exists) | your clone's path |
| `elapsed_seconds` | wall time of the verifier itself, rounded to whole seconds | it varies |
| last line | the verdict | `OK` |

`<repository root>` stands for the absolute path of your clone, for example `C:\Users\you\Dirac_claude`. On macOS and Linux the path uses `/` instead of `\` (expected; not tested). On Windows the lines end with CR LF. Within one clone the output is byte-identical from run to run except for the number in `elapsed_seconds`; between clones the folder name in the `report=` line differs as well.

When something fails, up to three detail lines come before the verdict, `failed_cells=<cell numbers>`, `messages=cell <n>: <message> | ...` and `failed_checks=<names>`, and a kernel message is usually also printed by the kernel itself where it occurs, above the summary lines. A wrong number of checks adds `ERROR: expected 49 notebook checks, found <n>`. The verdict is then `dirac16complex_mathematica_notebook=FAILED` and the exit code 1 (2 if the notebook cannot be found or read). Part 3.7 shows the measured output of the most likely failures.

With `--verbose`, 37 lines `cell <n> time=<seconds> failed=False messages=0` come first (the times of Part 1), and WolframScript writes its three diagnostic lines (Part 3.5) on standard error.

### 4.2 The report

`artifacts/dirac16complex/numerics/mathematica-report.json` is a JSON file with the keys `schemaVersion`, `generatedBy`, `provenance`, `wolframVersion`, `fixtureSha256`, `inputs`, `method`, `algebra`, `rustConstants`, `textParameters`, `exp1` to `exp5`, `engine`, `figures`, `checks`, `checkCount` and `verdict`. Its last lines are

```
	"checkCount":49,
	"verdict":"SUCCESS"
}
```

Some of the numbers it records (the largest deviation over all runs and components; NDSolve is the Mathematica recomputation, Rust the committed CVODE result):

| JSON key | Value |
| --- | --- |
| `exp1.runCount`, `exp2.runCount`, `exp3.runCount`, `exp5.runCount` | 26, 3, 10, 4 |
| `exp1.ndsolve.maxAbsStateDeviationVsRust` | 2.916040187095348e-09 |
| `exp1.ndsolve.maxExactErrorNDSolve` (against the exact propagator) | 4.2609999463210144e-14 |
| `exp1.finiteDifference.negativeControlFlippedMassMaxRelativeResidual` (must be large: a deliberately wrong equation) | 1.189755436191342 |
| `exp2.ndsolve.lnScaleMaxAbsDeviation` | 3.16273771616693e-08 |
| `exp2.ndsolve.spinorMaxPhaseAlignedDeviation` | 4.155225482244046e-10 |
| `exp3.ndsolve.spinorMaxAbsDeviation` | 2.1177233744396062e-08 |
| `exp3.finiteDifference.negativeControlFlippedMassMaxRelativeResidual` | 2.0000021448170178 |
| `exp4.thermal.maxPhaseAlignedDeviation` | 5.878093784505048e-08 |
| `exp4.kineticTheory.pModeSumMaxRelativeDeviation` | 1.869218924631168e-05 |
| `exp4.pair.maxBeta2RelativeDeviation` | 1.89931302797119e-09 |
| `exp5.ndsolve.maxRelativeStateDeviation` | 3.337481785773072e-08 |
| `exp5.ndsolve.ndsolveSelfRelativeError` (machine against 32-digit precision) | 1.7534292544040567e-14 |
| `fixtureSha256` | 8b4f15462ca4d61ef6ec0e72f04c8a77d23ce8bcabc9b6ce19f921c90e02653b |
| `wolframVersion` | 1.5e1 (that is 15.0, the value of `$VersionNumber`) |
| `engine.binary` | studies/dirac16complex_cosmology/target/release/dirac16complex_cosmology.exe |

All these values were the same, to the last digit, in every run of Part 6, because the whole file was byte-identical. The Stage-3 document quotes them rounded (its Section 11.2).

### 4.3 The figures

The 8 PNG files of Part 2.3: the EXP-1 mixed state (density frozen, pressure oscillating), the Einstein requirement of the primordial field (always negative), the EXP-2 anisotropy fractions, the EXP-3 equation of state against the Unite CPL line, the EXP-4 thermal equation of state and pair spectrum, the EXP-5 norm growth against WKB, and a bar chart of the digits of agreement between NDSolve and Rust for each experiment. In all of them, dots are the committed Rust results and lines the Mathematica recomputation.

### 4.4 Run time and memory

**Run time** on the verification machine (24 cores, Windows 11; 8 to 14 Wolfram kernels of other verification jobs were busy at the same time, and up to three of the runs below overlapped): 302 to 414 seconds of wall-clock time for the first 6 successful runs (median 352 s, about 6 minutes; the fastest, 302 s, was the only one that did not overlap with another run of this record; Part 6 lists every run). The re-verification run R1 took 252 seconds (`elapsed_seconds=249`). It ran while only one other Wolfram kernel was busy. The three runs of 2026-10-07 (S1 to S3) took 518, 561 and 599 seconds (`elapsed_seconds` 512, 552 and 593). During them the processor load of the computer was 100 % (measured with `Win32_Processor.LoadPercentage`), and 7 to 15 Wolfram kernels of other verification jobs were running (counted at four moments), among them runs of the Stage-4 notebook verifier. So expect 4 to 7 minutes on a lightly loaded computer and up to 10 minutes on a busy one. The verifier's own `elapsed_seconds` is 2 to 4 seconds less, because it does not include the start of the kernel (6 to 9 seconds less in runs S1 to S3, whose wall times also include up to 2 seconds of delay of the measuring script). Three cells take 88 % of the time (Part 1): cell 17, EXP-4 thermal modes, about 217 s; cell 11, EXP-2, about 67 s; cell 19, EXP-4 pair creation, about 23 s.

**Memory.** The Wolfram kernel `wolfram.exe` reached a **peak working set of 35,243 to 35,247 MiB** (34.4 GiB, that is 37.0 billion bytes) in every run in which it was measured, and a **peak committed memory of 35,627 to 35,630 MiB** (34.8 GiB; run B3, measured with a Windows job object, and runs S2 and S3, measured as the kernel's peak private bytes, `PeakPagedMemorySize64`). The working set sampled once per second (run A2) shows where: it rises to 17,862 MiB during cell 11 (EXP-2, about 50 s after the start), falls back to about 0.4 GiB, and then rises twice during cell 17 (EXP-4 thermal modes, which are integrated with dense output over up to 10^5 time units), to 27,867 MiB at about 129 s and to 35,246 MiB at about 202 s, each time falling back to about 0.5 GiB. Everything else needs less than 7 GiB. Runs S2 and S3 showed the same two peaks, later because the computer was busy (in S3: 17,360 MiB at 91 s, 35,247 MiB at about 366 s). The other processes are small: `wolframscript.exe` 16.7 MiB, the front end `WolframNB.exe` 163 to 165 MiB, the converters `NBImport.exe` 15 MiB and `XML.exe` 14 MiB, the licence query of WolframScript 68 MiB and the front end's helper kernel 127 MiB (Part 5, Processes).

**So you need a computer on which about 35 GiB (37 GB) of memory are free.** With the kernel limited to 8 GiB the run stopped after 44 s with `No more memory available.` (Part 3.7). A computer with 64 GB of memory is comfortable. Computers with 32 GB or less were not tested.

### 4.5 Other Wolfram versions and operating systems

Only Wolfram 15.0.1 on Windows 11 was tested. Expected differences elsewhere (not tested):

* `wolframVersion` in the report records the kernel's `$VersionNumber`, so another version changes that value.
* On macOS and Linux the program has no `.exe`, so `engine.binary` in the report reads `studies/dirac16complex_cosmology/target/release/dirac16complex_cosmology`. The Stage-3 gate ignores this one key for that reason.
* `NDSolve`, `NIntegrate` and `MatrixExp` of another version or on another processor can differ in the last digits, which changes the bytes of the report but, with the tolerances of the 49 checks, should not change the verdict.
* The PNG files are drawn by the Wolfram front end with the font Arial. Another operating system, other fonts or another version will usually give other bytes. The Stage-3 student guide records that even on the verification machine, with a different user profile folder, four of the eight figures differed from the committed ones in a few dozen pixels.

In all these cases, the verdict line decides whether the verification passed. Use `git diff artifacts/dirac16complex/numerics/mathematica-report.json` to see which values changed, and restore the committed files with `git checkout -- artifacts/dirac16complex/numerics`.

## 5. Side effects

* **Overwritten in the repository** (every run that reaches cells 26 to 36; Part 2.3): `artifacts/dirac16complex/numerics/mathematica-report.json` and the 8 PNG files in `artifacts/dirac16complex/numerics/figures/mathematica/`. After a successful run on the verification machine they had exactly the committed bytes, so `git status` stayed empty; only their modification times changed. **A failed run can leave a different report behind**: without the built program, the report was rewritten with the verdict `FAILURE` (run C1). A run stopped before cell 26 (for example by lack of memory, run B2, or by Ctrl+C) changes nothing; one stopped between cells 26 and 36 has rewritten some figures but not the report.
* **Created in the repository:** nothing by the verifier, except the folder `artifacts/dirac16complex/numerics/figures/mathematica/` if it is missing. After every run, `git status --porcelain --untracked-files=all --ignored` listed only `vendor/rustSolveIt/` and `studies/dirac16complex_cosmology/target/`, which your preparation (Part 3.4) created and which Git ignores (83 MB and 16 MB).
* **Not touched:** the notebook `notebooks/Dirac16ComplexDarkSector.nb` (the verifier reads it but never saves it), every input of Part 2.2, and the committed Rust results.
* **Temporary files.** The kernel's temporary folder (`$TemporaryDirectory`, normally `%TEMP%` on Windows) was empty after a run that was given a fresh one (runs B1 and S3). WolframScript keeps the console output it relays in short-lived files `tmp_<10 characters>` in `%LOCALAPPDATA%\Wolfram\WolframScript\WolframScriptTemporary\` on Windows; other WolframScript jobs were active at the same time, so these files could not be attributed one by one, and none of the files left there after the runs contained this verifier's output. The Wolfram front end, started for the PNG export, appends 25 lines of start-up information to its log `%LOCALAPPDATA%\Wolfram\Logs\FrontEnd\system.log` (measured for run B1) and updates its cache folder `%LOCALAPPDATA%\Wolfram\FrontEnd\15.0 Caches\`. The modification times of `%APPDATA%\Wolfram\WolframScript\WolframScript.conf` and of the paclet manager's file `%APPDATA%\Wolfram\Paclets\Configuration\managerData_15.0.1.0.pmd2` also changed during the runs; with other Wolfram jobs active, this cannot be attributed to this verifier with certainty. None of these files belongs to the repository. The locations on macOS and Linux were not examined.
* **Processes.** One `wolframscript.exe` starts one Wolfram kernel `wolfram.exe` (`-runfirst ... $EvaluationEnvironment="Script" ... -linkmode Connect`). The kernel starts the converter programs `NBImport.exe` and `XML.exe` (the notebook import), the front end `WolframNB.exe /b /min -server` (no visible window) for the first PNG export, and the Rust program once for `print-config` (cell 24, a fraction of a second). All of them end with the run. The kernel counts against the licence's limit on simultaneous kernels. Two more Wolfram processes were seen in the process tree of run S3 (and the second one also in run S2): just before the kernel, WolframScript starts `wolfram.exe -wlbanner -licenseinfo`, a licence query that ended within 2 seconds; and the front end starts its own helper kernel `wolfram -pacletreadonly -sandbox -noinit -pwfile "...\Configuration\Licensing\playerpass" ...` (peak working set 127 MiB), which ended with the run.
* **Memory:** about 35 GiB at the peak (Part 4.4). Other programs on the computer may be slowed down while it lasts.
* **Network.** The verifier and the notebook make no network access of their own. On the verification machine, the Wolfram setting `$AllowInternet` (whether Wolfram may use the internet) was `True` when it was checked on 2026-10-02:
  * `wolframscript -code '$AllowInternet'` printed `True`.
  * A test script whose first line is `#!/usr/bin/env wolframscript` runs in the same context as the verifier. It printed `{True, Script}` for `{$AllowInternet, $EvaluationEnvironment}`.
  * The paclet manager's file `%APPDATA%\Wolfram\Paclets\Configuration\managerData_15.0.1.0.pmd2` stores `"AllowInternet" -> True`.

  An earlier version of this record said `False`. That value was not reproduced, and the context in which it was read is not known. On 2026-10-07, after runs S1 to S3, `wolframscript -code '{$AllowInternet, PacletFind["ImageMetadataTools"]}'` printed `{True, {}}`.

  The notebook's text notes that the first PNG export in a headless kernel may try to install the optional component (paclet) `ImageMetadataTools`. The message that reports its failure (``ImportExport`RegisterFormat::interr``) is quieted by name. Although Wolfram was allowed to use the internet, `PacletFind["ImageMetadataTools"]` returned `{}` after all runs, including after run R1 (Part 6). So no such paclet was downloaded or installed, and the outputs were still byte-identical. WolframScript or the kernel may contact Wolfram's licence server. Network traffic was not monitored.
* **Restoring the committed state:**

  ```
  git checkout -- artifacts/dirac16complex/numerics/mathematica-report.json artifacts/dirac16complex/numerics/figures/mathematica
  ```

  (tested after the failed run C1: the report had its committed sha256 again). To remove the solver engine and the build as well: Windows PowerShell `Remove-Item -Recurse -Force vendor/rustSolveIt, studies/dirac16complex_cosmology/target`; macOS and Linux `rm -rf vendor/rustSolveIt studies/dirac16complex_cosmology/target`.

## 6. Verification record

* **Date:** 2026-10-02.
* **Commit verified:** `c2b33ccd16edb9c8b46585d0db6b2911a1f5d84e`, the head of `main` on https://github.com/once-ere/Dirac_claude.git when the fresh clones were made. When the files were last changed:

  * the verifier and the notebook in `fbec4d7` (2026-09-25 13:04 -0700). That commit also last wrote the committed report and the 8 figures.
  * the two packages and 52 CSV and JSON inputs in `6c0bfad`.
  * `generated.rs` and `algebra-fixture.json` in `78b4a5f`.
  * `exp4/summary.json` and `exp4/pair_spectrum.csv` in `571f9a7` (2026-09-26 16:58 -0700), after the committed outputs were generated. `exp4/summary.json` was also changed in `4480b06`.

  These two later changes appended CSV columns and summary keys, and changed summary values that the notebook does not read (Part 2.2). The runs below reproduced the committed report and figures byte for byte. Four fresh clones (A, B, C, D) were made with `git clone https://github.com/once-ere/Dirac_claude.git`; **no uncommitted file was copied into any of them**, because no file of this set or its inputs had uncommitted changes. In A, B and C the solver engine was fetched (`scripts/setup_solver.ps1 -Platform win11` in A and B, `bash scripts/setup_solver.sh win11` in C) and the Rust program built (`cargo build --manifest-path studies/dirac16complex_cosmology/Cargo.toml --release`); D received neither and served only for the error messages of Part 3.7. Later the same day, two more fresh clones, E and L, were made for the re-verification after the review (below).
* **Environment:**
  * Windows 11 Pro for Workstations 10.0.26200 (build 26200.9457), 24 logical processors, 191.4 GB of memory;
  * Wolfram 15.0.1 for Microsoft Windows (64-bit) (July 2, 2026), Professional licence; WolframScript 1.14.0;
  * cargo and rustc 1.91.1 (toolchain stable-x86_64-pc-windows-msvc); PowerShell 7.6.6; Git 2.51.2.windows.1 with its Git Bash.

  Python 3.14 was used only for the measurement helpers (hashes, JSON comparison), not by this set.
* **That the notebook is the builder's output.** In clone B, `scripts/build_dirac16complex_mathematica_notebook.wls` wrote a notebook outside the clone that was byte-identical to the committed `notebooks/Dirac16ComplexDarkSector.nb` (sha256 `708804e7...4ffe`); so the code of the 37 Input cells is exactly the code written in that builder, which was read in full for this record.
* **Runs** (all from the repository root of a fresh clone unless stated; "identical" means that all 9 rewritten files were byte-identical to the committed ones, and hence to every other identical run):

| Run | Clone | Shell / command form | Exit | Wall time | Peak kernel memory | Verdict, checks | Outputs |
| --- | --- | --- | --- | --- | --- | --- | --- |
| A1 | A | PowerShell 7 (started by a measuring script with the arguments of the typed command), default | 0 | 350.1 s (`elapsed_seconds=348`) | 35,245 MiB working set | OK, 49/49 | identical |
| A2 | A | the same, second run in the same clone | 0 | 340.5 s (337) | 35,246 MiB working set | OK, 49/49 | identical; standard output identical to A1 except `elapsed_seconds` |
| B1 | B | PowerShell 7 (measuring script), `--verbose`, with a fresh empty `TEMP` folder | 0 | 353.0 s (350) | 35,247 MiB working set | OK, 49/49 | identical; 37 cell-time lines; TEMP folder empty afterwards |
| B2 | B | `wolframscript -file ...` inside a PowerShell 7 script, kernel limited to 8 GiB by a job object (deliberate failure) | 1 | 43.6 s | 8,192 MiB committed (the limit) | none: `No more memory available.` | no file changed |
| B3 | B | `wolframscript -file ...` inside a PowerShell 7 script, memory measured by a job object with a limit (150 GiB) that was never reached | 0 | 414 s (411) | 35,629 MiB committed | OK, 49/49 | identical |
| C1 | C | PowerShell 7 (measuring script), `--verbose`, **Rust program not built** (deliberate failure) | 1 | 356.8 s (353) | 35,246 MiB working set | FAILED, 44/49 (5 engine checks false), 1 message in cell 24 | report rewritten with verdict FAILURE (13 lines differ); 8 figures identical; restored with `git checkout` |
| C2 | C | Git Bash, explicit notebook argument `notebooks/Dirac16ComplexDarkSector.nb`, `time` | 0 | 374.6 s (371) | not measured | OK, 49/49 | identical |
| A3 | A | PowerShell 7 typed command (inside `Measure-Command`), run from **another folder** (the parent of the clone) with the absolute path of the script | 0 | 301.7 s (298) | not measured | OK, 49/49 | identical; nothing was written into the folder the command was typed in |
| R1 | E | Git Bash, default command, re-verification after the review (07:26:16 to 07:30:28 -0700) | 0 | 252 s (249) | 35,246 MiB working set (sampled with `Get-Process` during the run) | OK, 49/49 | identical (all 9 sha256 equal to Part 2.3); standard error empty |

  In every successful run standard error was empty (except the three WolframScript lines with `--verbose`), and `git status --porcelain --untracked-files=all` printed nothing afterwards.
* **Check counts:** 49 of 49 notebook checks true, 37 of 37 cells evaluated, 0 failed evaluations and 0 messages, in each of the 7 successful runs; the 9 output files were byte-identical to the committed ones in 7 of 7 successful runs (63 of 63 file comparisons). In the deliberately failed run C1 the 8 figures were identical as well, and the report differed only in the 13 lines of the engine checks and the verdict.
* **Re-verification after the review (2026-10-02, 07:15 to 07:35 -0700).** A reviewer reported seven inaccurate or incomplete statements in an earlier version of this record. Each one was measured again in new fresh clones of `c2b33cc`. No uncommitted file was copied into them. Clone E's repository path has 139 characters; clone L's has 179 characters. The measurements:
  1. *Input history (Part 2.2).* `git log -1` was run for all 69 files of the set: the script, the 59 inputs and the 9 outputs. `git merge-base --is-ancestor` showed that `fbec4d7` is an ancestor of `571f9a7`. `pair_spectrum.csv` was compared column by column, and `summary.json` key by key, between `fbec4d7`, `4480b06` and `571f9a7`. Every `summaries[...]` access in the notebook builder was listed.
  2. *Input totals.* A script read every row of the table in Part 2.2 and hashed each file in clone E. It found 59 files and 23,585,029 bytes, and every sha256, byte count and line count agreed with the table.
  3. *`$AllowInternet`.* It was `True` before and after run R1, and no ImageMetadataTools paclet was installed (Part 5).
  4. *macOS and Linux (Part 3.6, check 3).* Builder line 770 chooses the program name without `.exe` when `$OperatingSystem` is not `"Windows"`, and line 1000 writes that name into `engine.binary`. The committed report holds the Windows name with `.exe`. This difference cannot occur on Windows, so it was not tested.
  5. *Solver set-up.* In clone E, `setup_solver.ps1` printed `solver_setup=OK` (5.0 s). Running it again printed `solver_setup=ALREADY-PRESENT` (0.3 s). `bash scripts/setup_solver.sh win11` then also printed `ALREADY-PRESENT` (1.9 s). The exit code was 0 every time.
  6. *Path length (Part 3.7).* `cargo build` succeeded in clone E (8.6 s). In clone L it failed with `LNK1104` and exit code 101 (7.3 s); `LongPathsEnabled` was 1. In clone E, `CARGO_TARGET_DIR` was then set to two build folders whose `.rlib` paths have exactly 259 and 260 characters. The first build succeeded (10.3 s) and the second failed with `LNK1104`.
  7. *Disk use.* `du -sb` in clone E after the set-up and the build gave 637,445,791 bytes in all. Of these, `.git` has 133,534,691, `vendor/rustSolveIt` 82,908,696, and the build folder `target` 16,480,157.

  Run R1 (table above) then confirmed that the set still executes and reproduces all 9 committed outputs byte for byte. The seven statements were corrected in this file. No file of the set was changed.
* **Fixes made:** none to the set. No execution defect of this set was found. This provenance file was corrected after the review (previous bullet).
* **Open discrepancies:** none in the results. Five observations about the environment, recorded for the student and for the maintainers:
  1. *Memory.* The run needs about 35 GiB of memory (Part 4.4). The Stage-3 documents give the run time of the Mathematica notebook but not its memory need.
  2. *`--` and `--verbose`.* The comments of the Stage-3 gates say that WolframScript 1.14.0 drops `--` and every argument after it. Measured: that is true for a script file whose first line is not `#!/usr/bin/env wolframscript`. This verifier begins with that line, and then WolframScript passes every argument, including `--`, `--verbose` and arguments after `--`, to the script (tested: `... .wls -- notebooks/NoSuch.nb` printed `ERROR: missing notebook: ...\notebooks\NoSuch.nb` and exited with 2), and the verifier ignores the `--` itself. With such a first line, `--verbose` also switches on WolframScript's own diagnostic lines on standard error. With a test file without that first line, `--verbose` and everything after `--` did not reach the script.
  3. *A misleading exit code of WolframScript.* When the script file cannot be opened (a wrong folder), WolframScript 1.14.0 prints `Failed to open file at path: ...` and exits with code 0, in PowerShell and in Git Bash. Read the verdict line, not only the exit code.
  4. *The Rust program's bytes* differ from clone to clone because they contain the build folder's path (Part 2.2); this has no effect on the results.
  5. *The path length on Windows.* `cargo build` of the Rust program fails with `LNK1104` (exit code 101) when the repository path has more than 156 characters (Part 3.7). This happens although `LongPathsEnabled` is 1. Cargo and rustc create the longer paths without trouble; the Microsoft linker `link.exe` is the step that cannot open them. This limit is not a defect of this set, which only needs the built program. Other documents already warn about it. `provenance/DIRAC16COMPLEX_STUDENT_GUIDE.md` has a Section 4.1, "Choose a short folder", which says that "the build creates paths about 105 characters below the repository root", and a row about `LNK1104` in its troubleshooting table. `provenance/DIRAC16COMPLEX_TEXTBOOK.md` warns about it in its Section 19.4. This record adds the measured limit: at most 156 characters for the repository path, with paths of 103 characters below the repository root. On the verification machine, a clone in a deeply nested scratch folder hit this limit.
