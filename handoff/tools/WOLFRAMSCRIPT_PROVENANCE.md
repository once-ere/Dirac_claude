# Execution provenance: the design-phase probes `probe1.wls` and `probe2.wls` (WolframScript)

Set: `handoff/tools/probe1.wls` and `handoff/tools/probe2.wls`, two short "probe" scripts written during the design phase of the dirac16complex work (2026-09-25).

Verified on 2026-10-02 at commit `c2b33ccd16edb9c8b46585d0db6b2911a1f5d84e`, and verified again on 2026-10-07 at commits `d278c49e54f1561e693de4ffc415f6c11107f577` and `72fc9ffc4a10328080a5778cc8a8c6e689aeaca6` of https://github.com/once-ere/Dirac_claude.git (the two probe files are byte-identical in all three commits; they have not changed since 2026-09-25). Result: both scripts EXECUTE OK, on both dates. Each one exits with code 0, writes nothing on the error stream, writes no file in the repository (WolframScript's own temporary files are deleted at the end of a normal run, Part 5), and printed byte-identical output in every captured run (two runs in a fresh clone, a third run in a second fresh clone, further runs made to measure memory, processes and temporary files and to test the student commands of Part 3, and a re-check of the side effects after an independent review; only Windows PowerShell 5.1 saves the same lines with a different encoding, UTF-16, Part 3.3). probe1 prints 30 `True` results and the one expected `False`, and its integer results 1, 16, 1 and 2 are the expected ones. One of its printed lines (line 15) is garbled by a bug in the probe's own code. The identity that line was meant to show is true, and it was checked separately (Part 4.3). Every result printed by probe2 agrees with the closed forms recorded in the project's contract, and its single `False` is the expected one. Part 1.6 answers whether the probes are still needed: no result of the repository depends on them; they are kept as a historical record. The re-verification of 2026-10-07 (two fresh clones, two required runs of each probe in the first clone and a third in the second, plus further runs) printed the same bytes again (sha256 `6291e51c...` for probe1 and `a95e77d8...` for probe2 in every captured run), with exit code 0, an empty error stream and no file changed in the clones; it also showed that the gamma matrices built by the probes are exactly the author's own eight real 16 x 16 Dirac matrices as extracted from the author's notebook (Part 1.2). The details are in Part 6.

This file is written for a student who has never used Wolfram software. Everything you need to run the two probes is in this file; you do not have to read any other file first.

## 1. What this set is and what it computes

### 1.1 What a "probe" is here

Before the project's verified programs were written, small throw-away scripts ("probes") were written in the scratch folder of the design session. They tested the key mathematical facts quickly and exactly, before larger programs were built on those facts. Three probes were written. probe1 and probe2 finished and printed their results. probe3 (a heavy symbolic computation) was too slow (more than 45 minutes, according to the Stage-1 workflow prompt quoted in Part 1.7) and was not kept. On 2026-09-25 the two finished probes were copied unchanged into the repository's restart kit `handoff/` (commit `29883fdb6b64e5026a3d0d86088fe6c7645fa4d7`, "Add restart kit"), and they have not changed since.

The probes are not polished programs:

* they have no header, no usage line and no comments that explain them (this file explains them);
* they read no file and write no file: they only **print** lines on the screen;
* they never decide "pass" or "fail" themselves: the exit code is 0 even when a printed result is `False`, so **you must read the printed lines** and compare them with Part 4;
* they print the Wolfram Language's own warning messages (`Solve::svars`, `General::stop`) in the middle of the output. These warnings are expected and harmless (Part 4.1).

The shipped, documented verifiers that replaced them are listed in Part 1.6.

### 1.2 The physics in plain words

The project studies a field called "dirac16complex": a field with 16 components (a "spinor") in an 8-dimensional space-time with coordinates x0, ..., x7. Four directions are space-like and four are time-like: the flat metric is eta = diag(+1, +1, +1, +1, -1, -1, -1, -1). In the original notebook x0 is a hidden space-like coordinate, x1, x2, x3 are ordinary space, x4 is the time in which the field evolves, and x5, x6, x7 are further time-like coordinates. (The probes count everything from 0. The project's newer "Revision" record calls the probes' index 0 "x8" and keeps the names x1, ..., x7 for indices 1, ..., 7.)

A field of this kind needs eight 16 x 16 matrices gamma^0, ..., gamma^7 (the "gamma matrices"). They must satisfy the **Clifford relations** gamma^a gamma^b + gamma^b gamma^a = 2 eta^ab I (I is the identity matrix). The original notebook builds them from small 4 x 4 building blocks (the project calls this the "split-octonion picture"). All their entries are the integers 0, 1 and -1, so they are **real** matrices. In the probes they are called `T[0]`, ..., `T[7]`. They are exactly the author's own matrices: on 2026-10-07 the probe's `T[0]`, ..., `T[7]`, `sig16`, the chirality matrix `chi` and the metric `eta` were compared, entry by entry, with the matrices `T16A[0..7]`, `sigma16`, `T16A[8]` and `eta4488` that `provenance/dirac_matrices/extract_from_author_notebook.wls` evaluated directly from the author's input cells of `Pair_Creation_of_Universes_WaveFunctionOfUniverse-4+4-Einstein-Lovelock-Nash.nb` (the committed file `provenance/dirac_matrices/author_notebook_T16.json`, described in `provenance/dirac matrices.md`), and all of them are equal; so are the projection matrices 2 P_L = I16 - chi and 2 P_R = I16 + chi of that file (Part 6).

* **probe1** checks the *algebra* of these matrices: the Clifford relations, which matrices are symmetric or antisymmetric, the matrix C (called `sig16`) used to form Psibar = Psi^dagger C, the chirality matrix, the relation to a second, independent construction of the gamma matrices (the "dirac-main" tensor-product picture), irreducibility, and the matrix B = -i C gamma^4.
* **probe2** checks the *geometry* of the original notebook's "primordial" gravitational field: the metric g = diag(cot^2 z, s^(1/3) e^(2 a4) (3 times), -1, -s^(1/3) e^(-2 a4) (3 times)) with z = 6 H x0, s = sin z and an arbitrary function a4 of t = H x4. For this metric it computes the vielbein (the "square root" of the metric), the Christoffel symbols, the spin connection, the covariant constancy of the curved gamma matrices, the curvature and the Einstein tensor. It also shows that the notebook's way of contracting the spin connection is wrong. probe2 works fully symbolically: its results hold for every x0 in the range 0 < 6 H x0 < pi/2, every H > 0, every x4 and every function a4.

Both probes compute **exactly**: integers, fractions and symbolic formulas, never floating-point numbers.

### 1.3 What probe1 computes, line by line

probe1 first rebuilds the notebook's matrices exactly as the original notebook does: two 4 x 4 families `s4[h]` and `t4[h]` (h = 1, 2, 3) from the Levi-Civita symbol, the 8 x 8 matrices `tau[0..7]` and `taub[0..7]` (taub[A] = sig . tau[A]^T . sig with sig = [[0, I4], [I4, 0]]), the 16 x 16 gamma matrices `T[A] = [[0, taub[A]], [tau[A], 0]]`, and `sig16 = diag(-sig, sig)`. Then it prints these lines (numbers are the line numbers of the printed output, Part 4.1):

| Line | Printed label | What is computed | Expected result |
| --- | --- | --- | --- |
| 1 | `tau-clifford` | (tau[A] taub[B] + tau[B] taub[A])/2 = eta_AB I8 for all 64 pairs A, B | `True` |
| 2 | `T16 clifford` | (T[A] T[B] + T[B] T[A])/2 = eta_AB I16 for all 64 pairs: the Clifford relations | `True` |
| 3 | `sig16==T0T1T2T3` | sig16 equals the product gamma^0 gamma^1 gamma^2 gamma^3 | `True` |
| 4 | `[1] sig16.T antisym` | (C gamma^a)^T = -C gamma^a for a = 0..7 (the "expression [1]" of the original task) | eight `True` |
| 5 | `sig16 symmetric`, `sig16^2==1` | C^T = C and C C = I16 | `True`, `True` |
| 6 | `sig16.S antisym all` | C S^ab is antisymmetric for all a, b, where S^ab = (gamma^a gamma^b - gamma^b gamma^a)/4 are the 28 generators of the spin group | `True` |
| 7 | `sig16.{T,S} symmetric all` | C (gamma^c S^ab + S^ab gamma^c) is symmetric for all 512 triples c, a, b | `True` |
| 8 | `sig16.[T,S] antisym all` | C (gamma^c S^ab - S^ab gamma^c) is antisymmetric for all 512 triples | `True` |
| 9 | `chirality block-diag`, `diag=` | the chirality matrix chi = gamma^0 gamma^1 ... gamma^7 is block-diagonal (no entries linking the upper 8 and the lower 8 components: `True`), and its diagonal (printed) is eight -1 followed by eight +1: the upper 8 spinor components have chirality -1, the lower 8 have +1 | `True`, `{-1 (8 times), 1 (8 times)}` |
| 11 | (warning) | `Solve::svars`, see Part 4.1 | expected |
| 12 | `intertwiner free params` | the second construction gam[1..8] (tensor products of the 2 x 2 matrices P = {{0,1},{1,0}}, N2 = {{0,1},{-1,0}}, G = {{1,0},{0,-1}} and I2) is related to the notebook's by a matrix K with gam[a] K = K T[a] for all a. `Solve` finds all such K; the number of free constants is printed | `1` (K is unique up to a factor) |
| 13 | `rank K` | the rank of K with its free constant set to 1 | `16` (K is invertible: the two constructions are equivalent) |
| 14 | `K sig16 K^-1 == C_dm ?` | K C K^-1 equals C_dm = gam[1] gam[2] gam[3] gam[4], the C matrix of the second construction; the opposite sign is also tested | `True`, then `False` for "== -C_dm" (the `False` is the expected answer) |
| 15 | `K^T C_dm K proportional to sig16` | meant to show that K^T C_dm K is a multiple of C; **the printed expression is garbled** by a bug in the probe (Part 4.3) | a very long line (14234 characters) |
| 17 | (warning) | `Solve::svars` | expected |
| 18 | `Pin commutant dim (over C)` | the number of independent complex 16 x 16 matrices that commute with all eight gamma matrices | `1` (only multiples of I16: the 16 components form one irreducible block) |
| 20, 22 | (warnings) | `Solve::svars` and `General::stop` | expected |
| 23 | `Spin commutant dim (over C)` | the same for the 28 spin generators S^ab | `2` (the two chirality halves, 8 + 8 components, are separate, inequivalent irreducible blocks) |
| 24 | `B hermitian`, `B^2==1`, `eigen` | B = -i C gamma^4 is Hermitian, B B = I16, and its eigenvalues are eight -1 and eight +1. (B is the matrix of the charge density Psi^dagger B Psi of the field's U(1) current.) | `True`, `True`, `{-1 (8 times), 1 (8 times)}` |
| 25 | `[sig16,B]==0`, `Bsig16 == -I T4` | C and B commute, and B C = -i gamma^4 | `True`, `True` |
| 26 | `T symmetric (A<4)/antisym(A>=4)` | gamma^0..gamma^3 are symmetric and gamma^4..gamma^7 antisymmetric | eight `True` |

Lines 10, 16, 19 and 21 are empty lines that belong to the warnings.

### 1.4 What probe2 computes, line by line

probe2 rebuilds the gamma matrices as probe1 does. It then defines the metric g of Part 1.2 and the diagonal vielbein e_mu^a = diag(cot z, s^(1/6) e^(a4) (3 times), 1, s^(1/6) e^(-a4) (3 times)). From them it computes the Christoffel symbols Gamma^rho_mu_nu, the spin connection omega_mu^a_b (from the "vielbein postulate"), the lowered connection omega_mu_ab = eta_ac omega_mu^c_b, two candidate spinor connections and the Einstein tensor. Every result is simplified with the assumptions 0 < 6 H x0 < pi/2 and H > 0. In the printed formulas, `Derivative[1][a4][H*x4]` means a4'(t) (the first derivative of a4 at t = H x4) and `Derivative[2][a4][H*x4]` means a4''(t).

| Line | Printed label | What is computed | Expected result |
| --- | --- | --- | --- |
| 1 | `g==e eta e^T` | the metric equals e eta e^T | `True` |
| 2 | `vielbein postulate zero` | the set of all distinct values of d_mu e_nu^a - Gamma^rho_mu_nu e_rho^a + omega_mu^a_b e_nu^b (512 components) | `{0}` (all zero) |
| 3 | `omega_{mu ab} antisym` | the set of values of omega_mu_ab + omega_mu_ba | `{0}` |
| 4 | `nonzero lowered components` | how many of the 512 components omega_mu_ab are not zero | `24` |
| 5 | `D_mu T^nu = 0 with CORRECT Omega` | the values of D_mu gamma^nu = d_mu gamma^nu + Gamma^nu_mu_lambda gamma^lambda + [Omega_mu, gamma^nu] with Omega_mu = (1/2) omega_mu_ab S^ab | `{0}`: the curved gamma matrices are covariantly constant, as they must be |
| 6 | `D_mu T^nu = 0 with NOTEBOOK contraction` | the same with the original notebook's contraction (1/2) omega_mu^a_b S^ab, which mixes an upper and a lower index without eta | `False` (expected: with the notebook's contraction the gamma matrices are NOT covariantly constant; for a pair of one space-like and one time-like frame index omega_mu^a_b is symmetric, so this contraction silently deletes every boost-type part of the connection) |
| 7 | `T^mu Omega_mu (correct) = c0 T^0 + c4 T^4 ?  c0,c4 =` | the coefficients of gamma^0 and gamma^4 in gamma^mu Omega_mu | `{3*H, 0}` |
| 8 | `residual` | gamma^mu Omega_mu has no other part, so gamma^mu Omega_mu = 3 H gamma^0 exactly (a4 drops out) | `True` |
| 9 | `T^mu Omega_mu (notebook contraction) coefficients` | the same coefficients with the notebook's contraction | `{(3*H)/2, (3*H*Derivative[1][a4][H*x4])/2}`, i.e. (3H/2)(gamma^0 + a4' gamma^4) |
| 10 | `sqrt|g| =` | the square root of the absolute value of the determinant of g | `Cos[6*H*x0]` (it does not depend on x4: the 7-dimensional volume is constant in time) |
| 11 | `Ricci scalar =` | the scalar curvature R | `6*H^2*(-7 + Derivative[1][a4][H*x4]^2)`, i.e. R = 6 H^2 (a4'^2 - 7) |
| 12 | `G^mu_nu diagonal =` | the eight diagonal components of the Einstein tensor G^mu_nu = R^mu_nu - (R/2) delta^mu_nu, in the order mu = 0..7 | G^0_0 = -3H^2(a4'^2 - 5); G^i_i = H^2(15 - 3a4'^2 + a4'') for i = 1, 2, 3; G^4_4 = 3H^2(7 + a4'^2); G^j_j = H^2(15 - 3a4'^2 - a4'') for j = 5, 6, 7 |
| 13 | `G^mu_nu offdiag =` | the values of all off-diagonal components | `{0}` |

These are exactly the closed forms recorded with the mark [VERIFIED] in section 9 of the project's contract `handoff/specs/CONTRACT.md`. (The contract also draws a consequence that the probe does not compute: under 8-dimensional Einstein gravity G^mu_nu = kappa T^mu_nu this field would need a negative energy density -3H^2(7 + a4'^2)/kappa.)

### 1.5 A note on charge conjugation

The probes do **not** compute any charge conjugation. The matrix `sig16` = C is the matrix used to form Psibar = Psi^dagger C (the "adjoint" or "charge" matrix); it is not a charge-conjugation operation. Charge conjugation is a **matrix** operation. The project's lead check `Revision/lead_checks/charge_conjugation_and_u1.py` (12 of 12 checks true in its committed report) writes it as Psi^c = calC Psibar^T = calC C Psi*, with a 16 x 16 matrix calC. It requires that Psi^c solve the field equation whenever Psi does, either with the same mass (sign +) or with the mass reversed (sign -). For each sign the lead check finds a one-dimensional space of solutions, so for each sign the matrix calC is unique up to a nonzero factor:

* calC_+ = C keeps the mass. Because C C = I16, it gives Psi^c = Psi*, which is nothing but plain complex conjugation. Every gamma matrix here is real, so for a real field (Psi* = Psi) this map does nothing at all; and for the quantised field it turns the matrix B of the anticommutator {Psi, Psi^dagger} = B delta into -B.
* calC_- = Gamma C gives Psi^c = Gamma Psi* and reverses the mass (m -> -m). It is the conjugation that preserves {Psi, Psi^dagger} = B delta of the quantised field, and on real fields it is the real matrix map Psi -> Gamma Psi together with m -> -m. This is the nontrivial matter <-> antimatter map of the theory.

Here Gamma = gamma^0 gamma^1 ... gamma^7 is exactly the chirality matrix chi that probe1 prints in line 9 (this was checked on 2026-10-02: the Revision record's matrices `C` and `Gamma` equal the probe's `sig16` and `chi` entry by entry). The statements of this section were also checked on 2026-10-02 with the probe's own matrices (Part 6): the matrices M with M (gamma^a)* = +gamma^a M for all a are the multiples of I16, and those with M (gamma^a)* = -gamma^a M are the multiples of Gamma; the map Psi -> M Psi* (for the quantised field Psi* is the column of the adjoint operators, Psi^dagger written as a column) preserves {Psi, Psi^dagger} = B delta exactly when M B^T M^dagger = B, which holds for M = Gamma and fails for M = I16 (it gives -B); and Gamma^T C gamma^a Gamma = -C gamma^a for every a, Gamma^T C Gamma = C.

### 1.6 Are the probes still needed?

**For reproducing results: no.** No program, gate, test or document builder of the repository runs the probes or reads their output, and no committed file was produced by them. Every statement they print has been proved again by the shipped verifiers `scripts/verify_dirac16complex_algebra.wls`, `scripts/verify_dirac16complex_geometry.wls` and `scripts/verify_dirac16complex_primordial.wls`. These verifiers have headers with usage lines, write JSON reports and set an exit code (0 only when every check is true). Their committed reports contain the following checks, all `true` (read again on 2026-10-07 at commit `72fc9ff`: every check named below is present and `true`, and all 21 checks of the algebra report, all 43 of the geometry report and all 126 of the primordial report are `true`):

| Probe statement | Shipped check (committed report) |
| --- | --- |
| probe1 lines 1, 2 (Clifford relations) | `ALG_clifford` in `artifacts/dirac16complex/arbitrary-field/wolfram-algebra-report.json` (from `scripts/verify_dirac16complex_algebra.wls`); `ALG_cliffordRelations` in `wolfram-geometry-report.json` |
| probe1 lines 3, 5 (C = gamma^0..gamma^3, C^T = C, C^2 = 1) | `ALG_chargeMatrix` |
| probe1 line 4 (expression [1]) | `ALG_expression1` |
| probe1 lines 6, 7, 8 | `ALG_spinTransposeProperties` |
| probe1 line 9 (chirality) | `ALG_chirality` |
| probe1 lines 12, 13, 14 (intertwiner, rank 16, K C K^-1 = C_dm) | `ALG_cliffordPictureIntertwiner` (measurements `intertwinerDimension` 1, `rank` 16, `KCKinverseEqualsCdm` true) |
| probe1 line 18 (Pin commutant 1) | `ALG_pinIrreducibleComplex` |
| probe1 line 23 (Spin commutant 2) | `ALG_spinDecomposition` |
| probe1 lines 24, 25 (B) | `ALG_chargeFormB` |
| probe1 line 26 | `ALG_gammaTransposeSymmetry` |
| probe1 line 15 (K^T C_dm K proportional to C) | **not a named shipped check.** It follows from the shipped fact K C K^-1 = C_dm together with K^T K = 4 I16, and it was verified directly on 2026-10-02: K^T C_dm K = 4 C for the probe's K, and = 4 c^2 C for every K = c K1 (Part 4.3) |
| probe2 lines 1, 10 | `P_metric_vielbeinProduct`, `P_metric_sqrtAbsDetG_cosz` in `artifacts/dirac16complex/primordial-field/wolfram-primordial-report.json` (from `scripts/verify_dirac16complex_primordial.wls`, which works symbolically in an exact ring plus exact point checks) |
| probe2 lines 2, 3, 4 | `P_spinconn_vielbeinPostulate512`, `P_spinconn_antisymmetry`, `P_spinconn_count24`; at exact points also `GEO_vielbeinPostulate_G2`, `GEO_omegaAntisymmetry_G2`, `GEO_primordialInvariants_G2` (geometry report) |
| probe2 lines 5, 6 | `P_gammaConst_DmuGammaNuZero64`, `P_gammaConst_notebookContractionFails`; `GEO_gammaCovariantConstancy_G2`, `GEO_notebookContractionFails_G2` |
| probe2 lines 7, 8, 9 | `P_Omega_gammaSlash3Hgamma0`; `GEO_diagonalSlashFormula_G2` and the geometry measurements `G2.p1.notebookSlashEqualsThreeHalfHTimesGamma0PlusA1Gamma4` (true at all three points) |
| probe2 lines 11, 12, 13 | `P_einstein_ricciScalar`, `P_einstein_GmixedClosedForms`, `P_einstein_offDiagonalZero`; `GEO_primordialInvariants_G2` |

The probe's matrices are also identical to the project's committed exact fixture `artifacts/dirac16complex/arbitrary-field/algebra-fixture.json`. This was checked on 2026-10-02 and again on 2026-10-07: `T[a]` = `gamma`, `sig16` = `C`, `chi` = `chirality`, `B` = `B`, `gam` = `gammaClifford`, and the probe's K (free constant 1) = `K_clifford` exactly. On 2026-10-07 they were also found identical to the author's own matrices extracted from the author's notebook (`provenance/dirac_matrices/author_notebook_T16.json`, Part 1.2).

**As a historical record: yes, they are worth keeping unchanged.** They are the evidence behind the [VERIFIED] marks that `handoff/specs/CONTRACT.md` placed in its sections 1, 2, 3, 4, 8 and 9 during the design phase. The Stage-1 and Stage-2 workflow scripts in `handoff/workflows/` tell their agents to copy code from them, and the shipped package `wolfram/Dirac16ComplexGeometry.wl` says in its section 1 that its gamma matrices are a "copied construction of the design probe". Deleting the probes would not change any result, but it would leave those references without a target. Do not use the probes as verifiers: they give no pass/fail exit code and write no report. Use the shipped verifiers named above instead.

### 1.7 Which documents cite the probes

* `handoff/specs/CONTRACT.md`, line 5: "[VERIFIED] ... proved by exact WolframScript computation in the design phase (scratchpad probes probe1/2/3)", with the [VERIFIED] marks of sections 1 (gamma matrices, C, expression [1], spin-generator properties, chirality, the intertwiner compatibility: probe1 lines 1-9, 12-14 and 26), 2 (the Pin and Spin commutants: probe1 lines 18 and 23), 3 item 4 (the notebook contraction fails in the primordial field: probe2 lines 5 and 6), 4 (covariant constancy of the gamma matrices: probe2 line 5), 8 (the matrix B: probe1 lines 24 and 25) and 9 (the primordial field's invariants and Einstein tensor: probe2 lines 1-4, 7, 8 and 10-13). Line 138 mentions probe3, which was never completed; the identity it was meant to prove (the divergence identity) is proved by the shipped checks `GEO_divergenceIdentity_G1`, `GEO_divergenceIdentity_G2` and `P_gammaConst_divergenceIdentity`.
* `handoff/workflows/stage1-build-dirac16complex-wf_64819362-2a3.js` (lines 16 and 54) and `handoff/workflows/stage2-build-primordial-wf_de6a8e13-a3a.js` (line 14): the agent prompts of the Stage-1 and Stage-2 build workflows ("Design-phase probes that already passed (reuse their code)").
* `HANDOFF.md` (the words "the handoff probes" in its description of the execution-provenance workflow; the line number changes often because `HANDOFF.md` is updated often: line 92 on 2026-10-02, line 155 at commit `2c05210` on 2026-10-07) and `Revision/workflows/execution_provenance.js` (line 44 on 2026-10-07; its item `handoff-probes`): the task that produced this provenance file.
* `wolfram/Dirac16ComplexGeometry.wl`, line 89: its section 1 builds the "notebook gammas (copied construction of the design probe)", i.e. the construction of probe1.
* The execution-provenance files `provenance/wolframscript/verify_dirac16complex_algebra.PROVENANCE.md` and `provenance/wolframscript/verify_dirac16complex_geometry.PROVENANCE.md` cite *this provenance file* (as a document that names their checks as the shipped proofs of the probes' statements); they do not run the probes.

The words "design probe(s)" in `scripts/check_dirac16complex_kohn_sham_theory.py` (lines 37 and 954), in its report `artifacts/dirac16complex/kohn-sham/python-theory-report.json` (line 331) and in `studies/dirac16complex_kohn_sham/src/exchange.rs` (lines 33 and 361) refer to the Python Kohn-Sham probes `handoff/tools/ks_probe.py` and `ks_probe2.py` (the matrix J = A0 A1 A4 and the filled single-k shell), not to probe1 or probe2, which compute neither. No published document (`provenance/*.md` including `provenance/dirac matrices.md`, `.tex`, `.pdf`, the textbook) names probe1 or probe2; the published documents cite the shipped verifiers of Part 1.6. (Searched again with `git grep` at commit `2c05210` on 2026-10-07.)

## 2. Files

The program files (pure ASCII with LF line endings; the repository's `.gitattributes` line `* -text` makes git store and check out every file byte for byte, so the sha256 values below are the same on Windows, macOS and Linux):

| File | Role | Lines | Bytes | sha256 |
| --- | --- | --- | --- | --- |
| `handoff/tools/probe1.wls` | algebra probe (Part 1.3) | 49 | 3426 | `c51edfda3870c8d71c7434dd1cf8379eca5e9e5d09ba3e5a4d8622dbd3318591` |
| `handoff/tools/probe2.wls` | primordial-geometry probe (Part 1.4) | 43 | 3679 | `0d17960e1d6992cf6ba7ed628a17149d6b1813f7f96b24848a158905f9c873cd` |

Both files have been unchanged since commit `29883fdb6b64e5026a3d0d86088fe6c7645fa4d7` (2026-09-25).

**Inputs.** None. The probes read no file of the repository, no data file, no package and nothing from the network. They contain no `Get`, `Needs`, `Import`, `Export`, `Put`, `Save`, `Write`, `Run`, `RunProcess`, `URL...`, `SetDirectory`, `Exit` or `Parallel...` call (checked on 2026-10-02 by searching both files). Apart from the probe file itself, only the files of the Wolfram installation are used.

**Outputs.** No file. Each probe only prints lines on the standard output (the screen): 26 lines for probe1 and 13 lines for probe2 (Part 4). Nothing is printed on the error stream. (While a probe runs, WolframScript keeps two temporary files of its own outside the repository and deletes them at the end; Part 5.) If you want to keep the printed lines, your terminal can save them into a file (Part 3.3); that file is created by the terminal, not by the probe.

## 3. How to run it

### 3.1 Install the Wolfram Engine (free) or Wolfram/Mathematica, and WolframScript

You need two programs: the Wolfram Language *kernel* (the computing engine) and *WolframScript* (the command `wolframscript`, which runs a script file with the kernel). The verification used the kernel version 15.0.1 and WolframScript 1.14.0.

**Option 1: the free Wolfram Engine for Developers.**

1. In a web browser open https://www.wolfram.com/engine/ and download the Wolfram Engine for your operating system. You need a free Wolfram ID (an e-mail address and a password) and the free developer licence offered on that page. Create both when asked, and read the licence terms.
2. Install it.
   * Windows: run the downloaded `.exe` file and accept the defaults. The installer normally also installs WolframScript and adds it to the PATH. Close every PowerShell window and open a new one afterwards.
   * macOS: open the downloaded `.dmg` file and follow its instructions (drag the application into Applications and open it once).
   * Linux: open a terminal in the download folder and run the downloaded installer with `sudo bash <name of the downloaded file>.sh`, accepting the defaults.
   * If after the installation the command `wolframscript` is "not recognized" or "not found" (most likely on macOS and Linux), download and install WolframScript separately from https://www.wolfram.com/wolframscript/ (Windows `.msi`, macOS `.pkg`, Linux `.deb` with `sudo apt install ./<file>.deb` or `.rpm` with `sudo dnf install ./<file>.rpm`), and open a new terminal.
3. Activate it. In a terminal (PowerShell on Windows, the Terminal application on macOS, a terminal window on Linux) type

   ```
   wolframscript -activate
   ```

   and enter your Wolfram ID and password when asked. (Running `wolframscript` without options on an engine that is not yet activated normally asks the same questions. If it shows the prompt `In[1]:=` instead, the engine is already active: type `Quit[]` and press Enter.) The activation needs an internet connection once.

**Option 2: Wolfram (formerly Mathematica), the desktop product.** If you have a licensed Wolfram or Mathematica installation, it contains the kernel; on Windows and Linux it also installs `wolframscript`. Start the desktop program once to activate it. If `wolframscript` is not found (typically on macOS), install WolframScript separately from https://www.wolfram.com/wolframscript/ as in step 2 above.

**Test the installation.** In a new terminal type

```
wolframscript -code '$Version'
```

It must print the kernel version, for example `15.0.1 for Microsoft Windows (64-bit) (July 2, 2026)` on the verification machine. The single quotes matter on macOS and Linux (they stop the shell from replacing `$Version`); in PowerShell they are also correct. If several versions are installed, `wolframscript` uses the newest one. `wolframscript -configure` prints its settings file; the line `WOLFRAMSCRIPT_KERNELPATH=...` names the kernel (a leading `//` means that this is the automatic choice).

**Which version.** Only version 15.0.1 was tested. Another version should print the same `True`/`False` results and the same mathematics, but it may word the warning messages differently or arrange the symbolic formulas of probe2 differently (Part 4.6).

**Kernels.** Each probe uses one Wolfram kernel (WolframScript sometimes also starts a short licence query, Part 5) and no parallel kernels. If you run both probes at the same time, two kernels run at once.

### 3.2 Get the repository

Install git if you do not have it (Windows: https://git-scm.com/download/win; macOS: type `xcode-select --install` in Terminal; Debian/Ubuntu Linux: `sudo apt install git`). Then, in the folder where you want the repository:

```
git clone https://github.com/once-ere/Dirac_claude.git
cd Dirac_claude
```

The whole clone takes about 670 MB on disk, of which about 195 MB are the `.git` folder (measured on 2026-10-07; on 2026-10-02 it was about 519 MB with a 128 MB `.git`: the repository grows). Every command below is typed in this folder, the *repository root* (the folder that contains `handoff`, `scripts`, `wolfram` and `artifacts`). Instead of git you may also download the ZIP archive from the GitHub page (button "Code", "Download ZIP") and unpack it. In that case `git status` is not available.

### 3.3 Run it

**The simplest way: print the results on the screen.** The probes take no arguments. In Windows PowerShell, in the macOS Terminal (zsh) and in a Linux terminal (bash) the commands are the same two lines:

```
wolframscript -file handoff/tools/probe1.wls
wolframscript -file handoff/tools/probe2.wls
```

Each command prints its lines within a few seconds, or up to about 20 seconds on a busy computer (Part 4.5), and then returns to the prompt. probe1's line 15 is 14234 characters long and fills the screen with matrices; this is expected (Part 4.3).

**Recommended: save the output and check it.** The commands below save the printed lines in the folder `build/probes/`. git ignores this folder (rule `/build/` in `.gitignore`). The commands then count the `True` and `False` results, print the sha256 fingerprints of the saved files, and show the output with the long line shortened.

Windows (PowerShell 7, the command `pwsh`; see the note below for the older "Windows PowerShell 5.1"):

```
New-Item -ItemType Directory -Force build/probes | Out-Null
wolframscript -file handoff/tools/probe1.wls > build/probes/probe1.txt
"probe1 exit code: $LASTEXITCODE"
wolframscript -file handoff/tools/probe2.wls > build/probes/probe2.txt
"probe2 exit code: $LASTEXITCODE"
"probe1 True=" + (Select-String -CaseSensitive -Path build/probes/probe1.txt -Pattern 'True' -AllMatches).Matches.Count + " False=" + (Select-String -CaseSensitive -Path build/probes/probe1.txt -Pattern 'False' -AllMatches).Matches.Count
"probe2 True=" + (Select-String -CaseSensitive -Path build/probes/probe2.txt -Pattern 'True' -AllMatches).Matches.Count + " False=" + (Select-String -CaseSensitive -Path build/probes/probe2.txt -Pattern 'False' -AllMatches).Matches.Count
(Get-FileHash -Algorithm SHA256 build/probes/probe1.txt).Hash.ToLower()
(Get-FileHash -Algorithm SHA256 build/probes/probe2.txt).Hash.ToLower()
Get-Content build/probes/probe1.txt | ForEach-Object { if ($_.Length -gt 100) { $_.Substring(0, 100) + " ... (" + $_.Length + " characters)" } else { $_ } }
Get-Content build/probes/probe2.txt
```

It must print `probe1 exit code: 0`, `probe2 exit code: 0`, `probe1 True=30 False=1`, `probe2 True=2 False=1`, the two sha256 values

```
6291e51c4fab85bd7b8f28604432acda406bc6b795b078edb67fe4299c49b4ff
a95e77d829ed37e4ee6622a81dd6b58b890e08e1ac11ad883c0d6a4c92e66771
```

and then the 26 lines of probe1 and the 13 lines of probe2 shown in Part 4.1 and Part 4.2.

*Note for Windows PowerShell 5.1* (the blue "Windows PowerShell" that comes with Windows, `$PSVersionTable.PSVersion` 5.1): the same block works and prints the same exit codes, counts and lines, but its `>` writes the files in UTF-16 instead of plain ASCII. The two sha256 values are therefore different there: `1560967bd95718d3e54e2a2a8589244cfd774e8bb21da22f40c8f82c9433f037` for probe1 and `78417905ab7000df9008316873f889e9a34fad41a5afcca16317e9be26965732` for probe2 (measured with Windows PowerShell 5.1.26100 on 2026-10-02). To get the plain-text files and the first pair of values, install PowerShell 7 (https://aka.ms/powershell) and use `pwsh`.

macOS (Terminal, zsh) and Linux (bash):

```
mkdir -p build/probes
wolframscript -file handoff/tools/probe1.wls > build/probes/probe1.txt
echo "probe1 exit code: $?"
wolframscript -file handoff/tools/probe2.wls > build/probes/probe2.txt
echo "probe2 exit code: $?"
echo "probe1 True=$(grep -o True build/probes/probe1.txt | wc -l) False=$(grep -o False build/probes/probe1.txt | wc -l)"
echo "probe2 True=$(grep -o True build/probes/probe2.txt | wc -l) False=$(grep -o False build/probes/probe2.txt | wc -l)"
cut -c1-100 build/probes/probe1.txt
cat build/probes/probe2.txt
```

It must print `probe1 exit code: 0`, `probe2 exit code: 0`, the counts 30 and 1 for probe1 and 2 and 1 for probe2 (on macOS `wc -l` puts spaces before the numbers, for example `probe1 True=      30 False=       1`), and the lines of Part 4.1 (cut after 100 characters) and Part 4.2.

To compare the fingerprint of the saved output, remove the carriage-return characters first. The verification machine (Windows) ends every printed line with CR LF; macOS and Linux normally end lines with LF only.

* Linux: `tr -d '\r' < build/probes/probe1.txt | sha256sum` and `tr -d '\r' < build/probes/probe2.txt | sha256sum`
* macOS: `tr -d '\r' < build/probes/probe1.txt | shasum -a 256` and `tr -d '\r' < build/probes/probe2.txt | shasum -a 256`

The expected values are

```
1376db2a4873c55d77bc821d42ab93b8b4ea8898a543d75890e0108a8c353e3c  (probe1)
ce5345c727c4ca0b009186aa6c2e48841403bf8ace5e3389c27726f998e49b16  (probe2)
```

These two values were computed on Windows from the measured output with the CR characters removed (and the same commands in Git Bash on Windows printed them). Runs on macOS and Linux were not made, so treat them as the expected values; if they differ, compare the lines with Part 4 instead.

### 3.4 Optional: see the identity that line 15 was meant to show

probe1's line 15 is garbled (Part 4.3). The following command loads probe1 (it prints all 26 lines again) and then evaluates the intended statement, K^T C_dm K = 4 C, correctly. In PowerShell 7 (`pwsh`), in the macOS Terminal (zsh) and in a Linux terminal (bash) type

```
wolframscript -code 'Get["handoff/tools/probe1.wls"]; Transpose[K1].Cdm.K1 == 4 sig16'
```

In the older Windows PowerShell 5.1 the double quotes inside must be written as `\"`, because that shell removes them when it starts a program:

```
wolframscript -code 'Get[\"handoff/tools/probe1.wls\"]; Transpose[K1].Cdm.K1 == 4 sig16'
```

The last printed line must be `True`. (Tested on 2026-10-02: the first form in PowerShell 7 and in Git Bash, the second form in Windows PowerShell 5.1. The forms cannot be swapped: the first form in Windows PowerShell 5.1, and the second form in PowerShell 7, print an error or `$Failed` instead of `True`.)

### 3.5 If it fails

| What you see | Cause and fix |
| --- | --- |
| PowerShell: `The term 'wolframscript' is not recognized`; macOS/Linux: `command not found: wolframscript` | WolframScript is not installed or not on the PATH. Open a new terminal after the installation. On Windows the program is in `C:\Program Files\Wolfram Research\WolframScript\`; add that folder to the PATH or install again. On macOS and Linux install WolframScript separately (Part 3.1, step 2). |
| `Failed to open file at path: handoff/tools/probe1.wls` and nothing else (the exit code is still 0) | You are not in the repository root. Change into the folder that contains `handoff` (`cd Dirac_claude`) and run again. (Measured: WolframScript prints this message on the error stream and still returns exit code 0, so always look at the printed lines.) |
| A message containing "licence"/"license", "password", "activate", "kernel limit", "too many kernels", "maximum number of" or "could not launch/start/connect" | The kernel is not activated, or your licence allows fewer kernels at the same time than are running. Run `wolframscript -activate` again; close other Wolfram programs and notebooks; wait 30 seconds and run again. |
| Lines starting with `Solve::svars` and `General::stop` | Expected. `Solve` is asked for all matrices K (or all commuting matrices) with 256 unknowns; the answer has free constants, and `Solve` warns that it cannot fix every unknown. The free constants are exactly what lines 12, 18 and 23 count. |
| Line 15 is a huge expression with `-4/{{0, -1, ...}} . 0` | Expected: a bug in the probe (Part 4.3). The intended identity is true (Part 3.4). |
| A `False` where Part 4 shows `True`, or different numbers | The probe files may have been changed. Compare their sha256 values with Part 2 (`Get-FileHash -Algorithm SHA256 handoff/tools/probe1.wls` in PowerShell, `shasum -a 256 handoff/tools/probe1.wls` on macOS, `sha256sum handoff/tools/probe1.wls` on Linux). If they differ, run `git checkout -- handoff/tools/probe1.wls handoff/tools/probe2.wls` or clone again. If they are the committed ones, note your Wolfram version (`wolframscript -code '$Version'`) and report the line. |
| The counts are right but the sha256 of the saved file differs | Most likely the line endings (macOS/Linux: use the `tr -d '\r'` commands of Part 3.3), the UTF-16 files of Windows PowerShell 5.1 (Part 3.3), or another Wolfram version (Part 4.6). |
| PowerShell says the path to `build/probes/probe1.txt` could not be found | The folder does not exist yet: run the `New-Item` line first. |
| A run takes much longer than about 10 seconds | The kernel starts slowly when the computer is busy (most of the time of a run is the start of the kernel, Part 4.5; on the busy verification machine one probe2 run took 19.5 s). Let it finish. If you stop it with Ctrl+C, nothing in the repository is changed. |

## 4. Expected output

### 4.1 probe1: the 26 printed lines

Exactly these 26 lines are printed on the standard output; nothing is printed on the error stream. Line 15 is shortened here: it really has 14234 characters, which are shown in full nowhere in this file. The beginning shown is what the PowerShell command of Part 3.3 prints.

```
tau-clifford: True
T16 clifford: True
sig16==T0T1T2T3: True
[1] sig16.T antisym: {True, True, True, True, True, True, True, True}
sig16 symmetric: True  sig16^2==1: True
sig16.S antisym all: True
sig16.{T,S} symmetric all: True
sig16.[T,S] antisym all: True
chirality block-diag: True diag={-1, -1, -1, -1, -1, -1, -1, -1, 1, 1, 1, 1, 1, 1, 1, 1}

Solve::svars: Equations may not give solutions for all "solve" variables.
intertwiner free params: 1
rank K: 16
K sig16 K^-1 == C_dm ? True   == -C_dm ? False
K^T C_dm K proportional to sig16: {{0, 0, 0, 0, -4/{{0, -1, 0, 0, 0, 0, 0, -1, -1, 0, 0, 0, 0, 0, -1 ... (14234 characters)

Solve::svars: Equations may not give solutions for all "solve" variables.
Pin commutant dim (over C): 1

Solve::svars: Equations may not give solutions for all "solve" variables.

General::stop: Further output of Solve::svars will be suppressed during this calculation.
Spin commutant dim (over C): 2
B hermitian: True B^2==1: True eigen: {-1, -1, -1, -1, -1, -1, -1, -1, 1, 1, 1, 1, 1, 1, 1, 1}
[sig16,B]==0: True Bsig16 == -I T4: True
T symmetric (A<4)/antisym(A>=4): {True, True, True, True, True, True, True, True}
```

Summary: 18 result lines, 4 warning lines and 4 empty lines; 30 times `True`, once `False` (line 14, the expected answer to "== -C_dm"), the integers 1, 16, 1, 2 (lines 12, 13, 18, 23), and two lists of eight -1 followed by eight +1 (lines 9 and 24). With the warnings as shown, every result is the expected one of Part 1.3. The output file is 15288 bytes with CR LF line ends on Windows (15262 bytes with LF).

### 4.2 probe2: the 13 printed lines

```
g==e eta e^T: True
vielbein postulate zero: {0}
omega_{mu ab} antisym: {0}
nonzero lowered components: 24
D_mu T^nu = 0 with CORRECT Omega: {0}
D_mu T^nu = 0 with NOTEBOOK contraction: False
T^mu Omega_mu (correct) = c0 T^0 + c4 T^4 ?  c0,c4 = {3*H, 0}
residual: True
T^mu Omega_mu (notebook contraction) coefficients: {(3*H)/2, (3*H*Derivative[1][a4][H*x4])/2}
sqrt|g| = Cos[6*H*x0]
Ricci scalar = 6*H^2*(-7 + Derivative[1][a4][H*x4]^2)
G^mu_nu diagonal = {-3*H^2*(-5 + Derivative[1][a4][H*x4]^2), H^2*(15 - 3*Derivative[1][a4][H*x4]^2 + Derivative[2][a4][H*x4]), H^2*(15 - 3*Derivative[1][a4][H*x4]^2 + Derivative[2][a4][H*x4]), H^2*(15 - 3*Derivative[1][a4][H*x4]^2 + Derivative[2][a4][H*x4]), 3*H^2*(7 + Derivative[1][a4][H*x4]^2), -(H^2*(-15 + 3*Derivative[1][a4][H*x4]^2 + Derivative[2][a4][H*x4])), -(H^2*(-15 + 3*Derivative[1][a4][H*x4]^2 + Derivative[2][a4][H*x4])), -(H^2*(-15 + 3*Derivative[1][a4][H*x4]^2 + Derivative[2][a4][H*x4]))}
G^mu_nu offdiag = {0}
```

Summary: 13 result lines, no warnings. There are 2 `True`, 1 `False` (line 6, the expected failure of the notebook's contraction), 4 zero sets `{0}`, the count 24 and 5 symbolic results, all as in Part 1.4. The output file is 981 bytes with CR LF line ends on Windows (968 bytes with LF).

### 4.3 The garbled line 15 of probe1

The code of that line is

```
Print["K^T C_dm K proportional to sig16: ", Simplify[Transpose[K1].Cdm.K1]/Transpose[K1].Cdm.K1[[1,1]] ];
```

In the Wolfram Language the matrix product `.` binds more tightly than the division `/`, and `[[1,1]]` (take the entry in row 1, column 1) binds to `K1` alone. The expression is therefore read as (checked with `FullForm`)

```
Simplify[Transpose[K1].Cdm.K1] / (Transpose[K1].Cdm.(K1[[1,1]]))
```

and not as the intended "K^T C_dm K divided by its own entry (1,1)". Here K1[[1,1]] = 0 (the first nonzero entry of K1 is in row 1, column 9). The denominator is therefore the unevaluated product "16 x 16 matrix . 0". Every nonzero entry of the numerator is printed as `-4/{{...}} . 0` or `4/{{...}} . 0`, and every zero entry as `0`. Even with the intended brackets the line would divide by zero, because the (1,1) entry of K^T C_dm K is also 0.

The numerator itself is readable in the printed line: the entries -4 stand in rows 1-8 at columns 5, 6, 7, 8, 1, 2, 3, 4, and the entries +4 in rows 9-16 at columns 13, 14, 15, 16, 9, 10, 11, 12. That is exactly 4 times sig16 = diag(-sig, sig). The intended statement is true and was verified separately on 2026-10-02 (Part 3.4 and Part 6): K1^T C_dm K1 = 4 sig16; for the general solution K = c K1, K^T C_dm K = 4 c^2 sig16; and K1^T K1 = 4 I16 (K1/2 is an orthogonal matrix).

The probe was **not** changed. This is not an execution defect: the script runs, and the defect is in what one of its lines computes. The probe is a historical record whose sha256 identifies the code that was run in the design phase. No shipped result depends on this line.

### 4.4 Exit code and what it means

Both probes end with exit code **0** in every run. The probes never set the exit code themselves, so 0 only means "the script ran to its end"; it would also be 0 if a result were `False`, and even when the file is not found (Part 3.5). Judge the run by the printed lines: the counts `probe1 True=30 False=1` and `probe2 True=2 False=1` of Part 3.3, the integers and formulas of Part 4.1 and Part 4.2, and, on Windows with PowerShell 7 or Git Bash, the sha256 values `6291e51c4fab85bd7b8f28604432acda406bc6b795b078edb67fe4299c49b4ff` (probe1) and `a95e77d829ed37e4ee6622a81dd6b58b890e08e1ac11ad883c0d6a4c92e66771` (probe2) of the saved output.

### 4.5 Run time and memory

Measured on the verification machine (Intel Core Ultra 9 275HX, 24 cores, 191 GB RAM, Windows 11 Pro for Workstations, build 10.0.26200 on 2026-10-02 and 10.0.26300 on 2026-10-07, Wolfram 15.0.1, WolframScript 1.14.0). Wolfram kernels of other jobs were running at the same time (eight `wolfram.exe` processes at one moment on 2026-10-02; between 2 and 15 on 2026-10-07).

| Probe | Date | Wall time of the runs (from start of `wolframscript` to its end) | Kernel processor time | Peak working set of the kernel |
| --- | --- | --- | --- | --- |
| probe1 | 2026-10-02 | 2.58 s, 3.59 s, 3.32 s (the three required runs); 3.99 s, 4.35 s and 4.84 s in measurement runs; 4.93 s, 5.21 s, 5.26 s, 5.00 s and 5.28 s in the monitored runs of the re-check (Part 6) | 7.2 s (one measurement) | 143.8 MiB and 148.3 MiB (two measurements) |
| probe1 | 2026-10-07 | 5.76 s, 6.12 s, 7.39 s (runs V1, V2, V3); 7.12 s (socket-monitored run) and 9.60 s (marker run) | 10.6 s, 9.5 s, 7.9 s (V1 to V3) | 156.4 MiB, 156.3 MiB, 156.3 MiB (V1 to V3) |
| probe2 | 2026-10-02 | 5.90 s (while probe1 ran at the same time), 4.14 s, 5.45 s (the three required runs); 5.19 s, 6.78 s and 7.70 s in measurement runs; 6.90 s, 6.00 s and 7.57 s in the monitored runs of the re-check (Part 6) | 5.0 s (one measurement) | 144.2 MiB and 150.1 MiB (two measurements) |
| probe2 | 2026-10-07 | 7.81 s, 8.41 s, 9.84 s (runs V1, V2, V3); 19.48 s (socket-monitored run), 11.34 s (marker run), 9.20 s, 7.46 s and 8.23 s (settings-file timing runs) | 5.2 s in each of V1 to V3 | 156.1 MiB, 156.1 MiB, 156.3 MiB (V1 to V3) |

Most of this time is the start of the Wolfram kernel: on the same busy machine a trivial `wolframscript -code '1+1'` took 4.2 s and 5.5 s on 2026-10-02, and 6.5 s and 3.9 s on 2026-10-07. Expect a few seconds per probe, and up to about 10 seconds (in one run of 2026-10-07 about 20 seconds) on a busy or slower computer; the machine was busier on 2026-10-07 than on 2026-10-02, which most likely explains the longer times (the printed output was identical). WolframScript itself used about 16.6 MiB (16.5 to 16.6 MiB on 2026-10-07), and the short licence query (Part 5) 49.8 to 60.6 MiB. The kernel's processor time can exceed the wall time because the kernel uses several threads (for example in its linear algebra). The memory values are the peak working sets of the processes (Windows `PeakWorkingSetSize`), read every 0.1 s while the probe ran; 1 MiB = 1048576 bytes.

### 4.6 Other Wolfram versions and other operating systems

Only Wolfram 15.0.1 on Windows was tested. With another version the `True`/`False` results, the integers and the mathematics must be the same. The wording of the `Solve::svars` and `General::stop` warnings, their number, and the arrangement of the symbolic formulas of probe2 (for example `-7 + a4'^2` versus `a4'^2 - 7`) may differ. Check the meaning against Part 1.4 then, not the bytes. On macOS and Linux the lines normally end with LF only (Part 3.3).

## 5. Side effects

**Files in the repository.** None. The probes create, change and delete no file. After each of the required runs (Part 6) `git status --porcelain --untracked-files=all` printed nothing, and a search for files modified during a probe2 run (everything outside `.git` newer than a marker file made just before the run) found none. On 2026-10-07 the same held again: `git status --porcelain --untracked-files=all --ignored` printed nothing in either clone after the required runs, and a search of the whole clone (including `.git`) for files newer than a marker file made before a probe1 run followed by a probe2 run found none. Nothing in the repository is overwritten, so there is no committed output to restore.

* With the save commands of Part 3.3 your terminal creates `build/probes/probe1.txt` and `build/probes/probe2.txt` (and the folders `build/` and `build/probes/` if missing). `build/` is ignored by git: `git status --porcelain` stays empty, and `git status --porcelain --ignored` shows `!! build/` (or the two files). Remove them with `Remove-Item -Recurse -Force build/probes` (PowerShell) or `rm -rf build/probes` (macOS, Linux).
* If you ever changed a probe file by accident, restore it with `git checkout -- handoff/tools/probe1.wls handoff/tools/probe2.wls`.

**Temporary files.** None in the system temporary folder. In the verification runs with `TEMP` and `TMP` pointing to an empty private folder, the folder was still empty afterwards. While the probe runs, WolframScript keeps two temporary files in `%LOCALAPPDATA%\Wolfram\WolframScript\WolframScriptTemporary` (on Windows normally `C:\Users\<your user name>\AppData\Local\Wolfram\WolframScript\WolframScriptTemporary`): an empty `tmp_<10 characters>` file created at the start, and a `tmp_<10 characters>` spool file holding the printed output. It deletes both when the run ends normally. Measured in 8 monitored runs (probe1 4 times, probe2 twice, a trivial one-line script twice; the folder was listed every 30 ms and also watched for create and delete events). The empty file appeared 0.05 to 0.11 s after the start, before the kernel was started, and no process held it open. The spool file appeared 2.7 to 3.5 s after the start, and the Windows Restart Manager showed that the run's own kernel held it open (3 runs). It grew to the size of the printed output (15288 bytes for probe1, 981 bytes for probe2) and began with the first printed line. Both files disappeared at the same moment, when the run ended. A run that is stopped by force leaves both files behind. This was measured twice: when the `wolframscript` process was killed during a probe2 run, its kernel ended at once, and the empty file and the spool file (holding the lines printed so far) stayed in the folder. Such leftover files are harmless and may be deleted. Files left in this folder by other Wolfram runs are not caused by the probes. During the verification the folder held 36 to 44 such files of other jobs, and files of other jobs appeared in it and disappeared while the probes ran. WolframScript also rewrites its small settings file `%APPDATA%\Wolfram\WolframScript\WolframScript.conf` at every start; its content did not change (same sha256 before and after a run), only its modification time. During the verification the modification time of the Wolfram per-user folder `%APPDATA%\Wolfram\Paclets\Temporary` also changed. Other Wolfram jobs were running at the same time, so it was not established whether the probes caused this. On macOS and Linux WolframScript keeps the corresponding files in your user profile (not examined in this verification).

**Processes.** `wolframscript` starts one Wolfram kernel process. On the verification machine this is `wolfram.exe`, started with `-runfirst ... $EvaluationEnvironment="Script" ... -linkmode Connect -linkname <5 characters>_shm -mathlink`, so it talks to WolframScript through shared memory. The kernel runs for the whole probe and exits at the end. In 4 of the 7 runs whose processes were observed in the first pass, and in all 8 probe runs of the re-check (Part 6), WolframScript also started a second, short-lived `wolfram.exe` (about 0.1 s of processor time, peak working set 50 to 68 MiB, measured in the first pass). In the two cases where its command line could be read before it ended (one in each pass), it was `wolfram.exe -wlbanner -licenseinfo` (a licence query), started 0.15 s and 0.43 s before the kernel. No parallel kernels are started.

**Network.** None (no access to other machines). The probes contain no network call. There is no connection to any other machine. At every start the kernel briefly opens internal loopback TCP socket pairs (127.0.0.1 to 127.0.0.1, both ends owned by the kernel process), each listed together with one bound socket. This also happens for a trivial script, and no remote address and no UDP endpoint appear. Measured in 8 runs in which the socket tables were read every 20 ms (probe1 3 times, probe2 3 times, the trivial script `Pause[3]; Print["triv-done"]` twice). In every run the kernel opened exactly three such loopback connections, one after the other, between 1.65 and 2.68 s after the start, each visible for 0.07 to 0.26 s. In one run the set-up of the first connection was caught: a listening socket on 127.0.0.1 only (which other machines cannot reach) and the connect from 127.0.0.1. The slower Windows listing `Get-NetTCPConnection` also shows, next to such a connection, one socket in the state `Bound` with the address 0.0.0.0 and the port of one end of the pair. This was seen in all 10 runs where that listing was used; `Bound` is not a listening state. No socket of `wolframscript.exe` or of the licence query, no IPv6 socket and no UDP endpoint was seen, and no address other than 127.0.0.1 and 0.0.0.0 appeared. The first check of this verification (one snapshot per run, 1.5 s after the start) saw none of these connections, because it was taken before they open (Part 6). (Activating a Wolfram licence, Part 3.1, needs the internet once; that is not part of the probes.)

**Restoring the committed state.** Nothing has to be restored after a run. After the clean-up command above, `git status --porcelain --ignored` must print nothing (if you created no other ignored files).

## 6. Verification record

* Date: 2026-10-02.
* Commit verified: `c2b33ccd16edb9c8b46585d0db6b2911a1f5d84e` of https://github.com/once-ere/Dirac_claude.git (branch `main`; the remote's `main` pointed to this commit during the verification). The two probe files have been unchanged since commit `29883fdb6b64e5026a3d0d86088fe6c7645fa4d7` (2026-09-25), and in both clones they had the sha256 values of Part 2.
* Environment: Windows 11 Pro for Workstations 10.0.26200, Intel Core Ultra 9 275HX (24 cores), 191 GB RAM; Wolfram 15.0.1 for Microsoft Windows (64-bit) (July 2, 2026), kernel `C:/Program Files/Wolfram Research/Wolfram/15.0.1/wolfram.exe`; WolframScript 1.14.0; PowerShell 7.6.6, Windows PowerShell 5.1.26100.9444 and Git Bash (git 2.51.2); a Professional Wolfram licence. Other Wolfram jobs ran on the machine at the same time.
* Fresh clones: two separate `git clone https://github.com/once-ere/Dirac_claude.git` into empty scratch folders (`clone1`, `clone2`). No uncommitted file was copied into them: the probes need no other file, and the author's working tree had no uncommitted change to `handoff/tools/`.
* Command of every required run, from the clone root (the probes have no usage line; this is the plain WolframScript invocation): `wolframscript -file handoff/tools/probe1.wls` and `wolframscript -file handoff/tools/probe2.wls`, with the standard output and the error stream captured in files outside the clone.

| Run | Probe | Clone | Started (UTC) | Wall time | Exit code | Standard output | stdout sha256 | Error stream |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | probe1 | `clone1` | 13:16:40 | 2.58 s | 0 | 26 lines, 15288 bytes | `6291e51c4fab85bd7b8f28604432acda406bc6b795b078edb67fe4299c49b4ff` | empty |
| 1 | probe2 | `clone1` | 13:17:07 | 5.90 s | 0 | 13 lines, 981 bytes | `a95e77d829ed37e4ee6622a81dd6b58b890e08e1ac11ad883c0d6a4c92e66771` | empty |
| 2 | probe1 | `clone1` | 13:17:10 | 3.59 s | 0 | 26 lines, 15288 bytes | `6291e51c...` (identical) | empty |
| 2 | probe2 | `clone1` | 13:17:27 | 4.14 s | 0 | 13 lines, 981 bytes | `a95e77d8...` (identical) | empty |
| 3 | probe1 | `clone2` | 13:18:25 | 3.32 s | 0 | 26 lines, 15288 bytes | `6291e51c...` (identical) | empty |
| 3 | probe2 | `clone2` | 13:18:29 | 5.45 s | 0 | 13 lines, 981 bytes | `a95e77d8...` (identical) | empty |

Runs 1 and 2 are the two required runs from a fresh clone; run 3 repeats them in a second fresh clone.

* Further runs in the clones, made for the measurements of Parts 4.5 and 5:
  * memory runs started from PowerShell 7 with `Start-Process` (probe1 4.35 s, probe2 7.70 s; exit code 0; peak working sets of Part 4.5);
  * process and network snapshot runs (probe2 6.78 s, probe1 4.84 s; exit code 0; kernel processor time 5.0 s and 7.2 s). The single socket snapshot of each of these runs, taken 1.5 s after the start, listed no socket; the re-check below shows that it was taken before the kernel opens its loopback connections;
  * runs with `TEMP` and `TMP` set to an empty private folder (probe1 3.99 s, probe2 5.19 s; exit code 0; the folder stayed empty);
  * a probe1 run during which the WolframScript spool folder was watched (Part 5; exit code not recorded);
  * three probe1 runs in which the child processes of `wolframscript` were listed (Part 5; their output was discarded and their exit codes were not recorded).

  The standard output of every one of these runs except the three child-process listing runs was captured, and it has the sha256 of the table above.
* Student commands. The command blocks of Part 3.3 and Part 3.4 were copied out of this file by a program and executed literally, each time after deleting `build/`:
  * the PowerShell 7 block in `clone1` (`pwsh -NoProfile -File`, started 13:35:20 UTC; 9.7 s for the whole block): exit codes 0, `probe1 True=30 False=1`, `probe2 True=2 False=1`, the two sha256 values of Part 3.3, and then exactly the 26 lines of Part 4.1 (line 15 shortened as shown there) and the 13 lines of Part 4.2 (compared line by line by the program);
  * the macOS/Linux block in `clone2` with Git Bash (11.4 s): the same exit codes and counts; `sha256sum` of its two saved files gave the two values of Part 3.3, and the two Linux `tr -d '\r'` commands gave `1376db2a...` and `ce5345c7...` as stated;
  * the same PowerShell block under Windows PowerShell 5.1 in `clone1`: the same exit codes and counts, and UTF-16 files with the two sha256 values given in the note of Part 3.3;
  * the first command of Part 3.4 in PowerShell 7 and in Git Bash, and the second in Windows PowerShell 5.1: each printed `True` as its last line. (Swapped, the first form in Windows PowerShell 5.1 lost its inner double quotes, and the second form in PowerShell 7 printed `$Failed`.)
  * An earlier version of the PowerShell block (without `-CaseSensitive`, 13.8 s) and of the bash block (9.8 s) gave the same results.
  * A probe started from a folder that is not the repository root printed `Failed to open file at path: handoff/tools/probe1.wls` on the error stream with exit code 0. Started from inside `handoff/tools` as `wolframscript -file probe2.wls`, probe2 printed its normal output.
* Byte identity: the probes write no output file, so there is no committed output to compare with. The printed output of every captured probe1 run is byte-identical (11 runs: the 3 of the table, 4 of the further runs above (memory, snapshot, private `TEMP`, spool watch) and the 4 student-block runs in PowerShell 7 and Git Bash), and so is the printed output of every captured probe2 run (10 runs: 3 of the table, 3 further runs and 4 student-block runs). The PowerShell 7 and Git Bash redirections give identical bytes (CR LF line ends, ASCII). Only Windows PowerShell 5.1 gives different bytes, because it writes UTF-16 (Part 3.3). The 5 probe1 runs and the 3 probe2 runs of the re-check below printed the same bytes again.
* Results ("check counts"): probe1 printed 30 `True`, 1 `False` (the expected negative answer of line 14), the integers 1, 16, 1, 2 and the two expected spectra: every result is as expected, and line 15 is garbled (Part 4.3). probe2 printed 2 `True`, 1 `False` (the expected failure of the notebook contraction), 4 zero sets, the count 24 and the symbolic results, all equal to the closed forms of section 9 and the [VERIFIED] statements of sections 3 and 4 of `handoff/specs/CONTRACT.md`.
* Additional checks made for this record, without changing any file (separate WolframScript files in the scratch folder, run in `clone2` after loading the probe with `Get`):
  * the intended identity of probe1 line 15: `Transpose[K1].Cdm.K1 == 4 sig16` gave True; for K = c K1, K^T C_dm K - 4 c^2 sig16 = 0 gave True; `Transpose[K1].K1 == 4 IdentityMatrix[16]` gave True; `FullForm` showed the parsing of Part 4.3;
  * probe1's `T[a]`, `sig16`, `chi`, `B`, `gam` and `K1` equal the committed fixture `artifacts/dirac16complex/arbitrary-field/algebra-fixture.json` (`gamma`, `C`, `chirality`, `B`, `gammaClifford`, `K_clifford`) entry by entry;
  * with Python: the Revision record `Revision/algebra/gammas.json` has `C` equal to the fixture's `C` and `Gamma` equal to the fixture's `chirality` (= probe1's `chi`), and its gamma matrices for x1..x7, x8 equal the fixture's gamma^1..gamma^7, gamma^0.
* `git status --porcelain --untracked-files=all` in both clones after the required runs: empty. After the student blocks, `git status --porcelain --ignored` shows only the ignored `build/` files.
* Re-check after an independent review (2026-10-02, 14:08 to 14:17 UTC). A reviewer ran the probes again in a fresh clone of the same commit and reported four errors in this file: the network paragraph of Part 5 (the kernel does open loopback sockets), the temporary-files paragraph of Part 5 (two files per run, not one), the incomplete list of CONTRACT.md sections in Parts 1.6 and 1.7, and a self-contradictory Part 1.5. All four were confirmed and corrected in this file. The measurements were made in a third fresh clone (`git clone https://github.com/once-ere/Dirac_claude.git`, commit `c2b33ccd16edb9c8b46585d0db6b2911a1f5d84e`, no uncommitted file copied), with the monitoring scripts kept in the scratch folder outside the clone:
  * runs: probe1 5 times and probe2 3 times (`wolframscript -file handoff/tools/probe1.wls` or `probe2.wls`, started in the clone root), and the trivial script `Pause[3]; Print["triv-done"]` (a file outside the clone) twice. Every run ended with exit code 0 and an empty error stream; every probe1 output had the sha256 `6291e51c...` and every probe2 output the sha256 `a95e77d8...` of the table above; the run times are in Part 4.5. About 12 other WolframScript jobs ran on the machine at the same time;
  * sockets: in 8 of these runs the TCP and UDP tables (IPv4 and IPv6) were read every 20 ms, through the Windows functions GetExtendedTcpTable and GetExtendedUdpTable, for every process started by the run; in all 10 runs `Get-NetTCPConnection` and `Get-NetUDPEndpoint` were also read every 0.25 to 0.5 s. The results are those of Part 5 ("Network");
  * temporary files: in 8 runs the folder WolframScriptTemporary was listed every 30 ms and watched for create and delete events; in 3 of them the Windows Restart Manager was asked which processes held each new file open. The results are those of Part 5 ("Temporary files"). Two runs with the environment variable LOCALAPPDATA set to an empty private folder were meant to separate the probes' files from those of other jobs. WolframScript ignored the variable (nothing was written to the private folder), so these two runs count only for the printed output and the sockets;
  * forced stop: twice, probe2 was started and its `wolframscript` process was killed (`Stop-Process -Force`) 4.7 s and 4.9 s after the start. The kernel ended at once (it was gone 0.02 s after the kill in the run where this was timed). The output printed up to then (394 and 20 bytes) is the beginning of the normal output, and the empty file and the spool file stayed in WolframScriptTemporary. These four leftover files were deleted afterwards. Two earlier attempts of this test stopped with an error in the test script itself before the kill, so their two probe2 runs went to their normal end without being observed (their output was not kept);
  * charge conjugation (Part 1.5): a WolframScript file that loads probe1 with `Get` and then tests each statement of Part 1.5 with the probe's own matrices printed `True` for every statement (4.4 s). The lead check `python Revision/lead_checks/charge_conjugation_and_u1.py`, run in the clone, gave 12 of 12 PASS and wrote its report again byte for byte (sha256 `a2628e6d5afaf41c15fcf05afa95fc42f152894626c22efcd687de304ad604f2`, the committed value);
  * CONTRACT.md: `grep -n VERIFIED handoff/specs/CONTRACT.md` shows [VERIFIED] marks in lines 31, 34, 35, 37, 38 and 43 (section 1), 59 and 63 (section 2), 88 (section 3), 110 (section 4), 177 (section 8) and 200 (section 9), besides the explanation in lines 4 and 5. Part 1.7 lists the probe lines behind each of them;
  * `git status --porcelain --untracked-files=all --ignored` in the clone after all these runs: empty.
* Fixes made: none to the set. No execution defect was found, and no file of the set was changed. After the review this provenance file itself was corrected: Part 1.5, the section lists of Parts 1.6 and 1.7, the run times of Part 4.5, the temporary files, processes and network of Part 5, and this record.
* Open discrepancy: probe1's printed line 15 is garbled (operator precedence and a division by a zero entry, Part 4.3). The statement it was meant to show is true. The probe was left unchanged on purpose, because it is a historical design-phase record and no result depends on that line.
