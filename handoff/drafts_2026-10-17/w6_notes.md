# W6 notes (dark sector for the corrected metric) — derived by hand 2026-10-17, to be re-derived in sympy

Metric: g = diag(e^{-2a4} b4 cot^2 z, e^{2a4} (x3), -1, -e^{-2a4} b4 (sin^2 z)^{1/6} (x3)), z = 6 H x0 real.
* sqrt|g| = e^{-a4} b4^2 |cot z| |sin z|^{1/2}; with |sin z| = e^{6Hy}, dy = cot z dx0: sqrt|g| |dx0| = e^{-a4} b4^2 e^{3Hy} |dy|.
* Expansion rates (d/dx4 of ln of the scale factor): x0 and x5..x7: h4 = u/2 - a4' (u = b4'/b4); x1..x3: a4'.
  On the history a4 = H x4, b4 = e^{(4/3) H x4}: h4 = -H/3 (f = e^{-a4/3}).
* Conservation, diagonal T = diag(p0, p3 x3, -rho, p_t x3) depending on (x4, x0):
  d4 rho = -3 a4' (rho + p3) - h4 (rho + p0) - 3 h4 (rho + p_t)  (= -4 h4 (rho + p0) when p0 = p_t; a4-equations.json
  generalSource.energyExchange).  Check against own Christoffels in sympy.
* Integrated (E = int sqrt|g_7| rho per coordinate cell = Vol_7 2 int e^{3Hy} rho dy, Vol_7 = ell^3 v_t e^{-a4} b4^2):
  dE/dx4 = -3 a4' P3 - h4 (P0 + 3 Pt); on the history dE/da4 = -3 P3 + Pt + P0/3 (ks-theory.json emt.energyChange).
* Observer (3-space, a = e^{a4}), normalisation A/B (extra times and hidden direction per unit coordinate volume / fixed
  coordinate period): rho_4 = E e^{-3 a4} (per proper 3-volume) => w_eff = -1 - (1/3) d ln rho_4/d ln a
  = -(1/3) d ln E/d a4 = (3 P3 - Pt - P0/3)/(3E) = P3/E - Pt/(3E) - P0/(9E).
  Free fold-band gas: E ~ e^{-a4} (eps = e^{-a4} |k|), P3 = E/3, Pt = P0 = 0 => w_eff(A) = 1/3 (radiation-like).
  General h4: w_eff(A) = P3/E + (h4/(3 a4'))(P0 + 3 Pt)/E.
* Normalisation C (per unit proper 7-volume, i.e. the proper 8-density): rho_8 = E/Vol_7 ~ E e^{a4} b4^{-2}: to be
  derived (the old s-term: w_eff(C) = w_eff(A) - s (Vol_7 rate)/(3 a4') ... re-derive exactly).
* Condensate (homogeneous, x0-independent): needs the field-theory record (Revision/theory, W1: S = e^{a4} b4^{-2} S0 per
  field_equations_a4 fields.condensate_S_law) — re-derive rho, p for the condensate and its w.
* Read before W6: derive/derive_effective.py (546 lines), compute/compute_eos.py (434), independent/independent_free_gas.py
  (343), dirac16complex00/ (python/derive_eos.py, independent_numerics.py, tests), dark_sector/wolfram (b4 checks),
  B4_PROVENANCE.md; pairing/kohn_sham t3_rust_demo.py (key emtIntegrals_2Vol7_int_e3Hy), t3_reference_demo.py;
  notebooks/src/kohn_sham_states.py, dark_sector_hypotheses.py, lovelock_gkd.py (19 Rust checks -> 27).
* independent_free_gas.py: still the metric of 2026-10-14 (kappa = e^{-Hy - a4}, Z2 brane, ks-b4-wolfram K2). Rewrite:
  h_j = j[-(i/f) sigma1 d_y + m sigma2 + kappa k sigma3], kappa = e^{-a4}, f = e^{-a4/3}; fold conditions theta = 0, pi;
  Chebyshev collocation; the occupied fold band is exact (eps = kappa |k|, chi = (e^{f m y}, 0)), so E = e^{-a4} E(0)
  and w_eff(A) = 1/3 exactly for the free gas (check it from the Hellmann-Feynman d eps/d a4 = -eps + kinetic term
  (1 - beta/2)... re-derive: d h/d a4 = j[(i/f)(df/da4)/f sigma1 d_y ... ] — do it in sympy); the bulk band levels
  sqrt(M^2 + (n pi/(f L))^2) depend on a4 through f (box-like), w_eff of a bulk quantum from -(1/3) d ln eps/d a4.
* Hand derivations (2026-10-17, to verify in sympy; C = cot z, W = (sin^2)^{1/12}, C' = -6H(1 + C^2), W'/W = H C, exact
  for every real z with sin z != 0):
  - x0 conservation: d0 p0 + 3 (W'/W)(p0 - p_t) = d0 p0 + 3 H cot z (p0 - p_t)  ==> p0_y + 3H (p0 - p_t) = 0 (A4 of ks_source).
  - h4/a4' = beta/2 - 1; dE/da4 = -3 P3 - (beta/2 - 1)(P0 + 3 Pt)  (beta = 4/3: -3 P3 + Pt + P0/3).
  - rho_4 = E/(e^{3a4} (e^{-4a4} b4^2)^s): s = 0 (A, B: per proper 3-volume), s = 1 (C: per proper 7-volume,
    Vol_7 = e^{-a4} b4^2 = e^{(2 beta - 1) a4}); w_eff(s) = -(1/3) dlnE/da4 - (s/3)(4 - 2 beta);
    w_eff(A) = P3/E + (beta/2 - 1)(P0 + 3 Pt)/(3E); w_eff(C) = w_eff(A) - (4 - 2 beta)/3 = w_eff(A) - 4/9 at beta = 4/3.
  - Free fold-band gas: P3 = E/3, Pt = P0 = 0: w_eff(A) = 1/3 exactly, w_eff(C) = -1/9.
  - Condensate (homogeneous): S = S0 e^{a4} b4^{-2} (a4-equations.json fields.condensate_S_law), rho = m S + lambda S^2/2,
    p3 = p_t = p0 = lambda S^2/2; E = Vol_7 rho = m S0 + (lambda/2) S0^2/Vol_7; dE/da4 = -(2 beta - 1) P (consistent with
    the identity: -3P - (beta/2 - 1) 4P = (1 - 2 beta) P); w_eff(A) = ((2 beta - 1)/3) w_c (5/9 w_c at beta = 4/3),
    w_c = p/rho; w_eff(C) = w_eff(A) - 4/9.
  - Flat-limit mode: omega^2 = M^2 + k^2 e^{-2a4} + l^2 e^{2a4}/b4 - q^2 e^{2a4}/b4 (l: hidden, space-like; q: extra
    times); the fold band eps = e^{-a4}|k| behaves as a massless 3-space quantum (radiation-like).
  - Einstein: G^x4_x0 = 0 identically (the corrected metric); compute G^x1_x1 - G^x5_x5 and w_exp from the record.
  - Replace "author_weights_b4_branch" by the history's required source (a4-equations.json
    exponentialHistory.authorWeights.historySource_kappaT_minus_Lam): the history is a prescribed background.
* DRAFT scratchpad/w6/derive_effective.py (2026-10-17 05:20): 37/37 with REVISION_DIR=<repo>/Revision, 5 s; outputs go to
  scratchpad/outputs, scratchpad/reports (not the repo). One error found and fixed in the draft: sqrt|g| has W^3 = |sin|^(1/2)
  (first written W^6). To do in W6: review every check text; move into place; then compute_eos.py (new w_eff formulas,
  normalisation C = A - 4/9, the condensate w_eff(A) = (5/9) w_c, the fold-band gas w_eff(A) = 1/3 exactly) and
  independent_free_gas.py; dirac16complex00; dark_sector/wolfram (b4-era: keep as record or retire?); notebooks; pairing T3.
* dirac16complex00 (725 + 418 + 92 lines, eos-theory.json 527): reads a4-equations.json KEY b4 (removed in W2) and
  derive_effective's author_weights_b4_branch: broken until W6. Rewrite with generalSource and
  fields.dirac16complex00.homogeneousCondensate (S = e^{a4} b4^{-2} S0).
* compute_eos.py: every number tied to the old record (N = 136, 688; E ~ e^{-2 a4} for N = 8; w_eff(C) = w_eff(A) - 1/3);
  rewrite data-driven from the new dense history (N = 8, 592, 2352), with the new formulas.
* pairing/kohn_sham (T3, SPEC section 9): the theorem (verify_t3.wls, check_t3.py) and both demos use the old block equation
  (K = e^{-Hy - a4}|k|, brane parities, Vol_7 e^{(3/2) beta a4}); re-derive T3 for h_j = j[-(i/f) sigma1 d_y + M sigma2 +
  kappa k sigma3] + v with the fold conditions theta = 0, pi (the map M -> -M exchanges them?) and the tip theta -> pi;
  then the demos (key emtIntegrals_2Vol7_int_e3Hy; Vol_7 = ell^3 v_t e^{(5/3) a4}).
* independent_free_gas.py rewrite plan: h_{+1} = [[kappa k, (1/f) D + M], [M - (1/f) D, -kappa k]], kappa = e^{-a4},
  f = e^{-a4/3} (equivalently the old problem on [-f L, 0] with constant kappa); d h/d a4 = -kappa k sigma3 + (1/3) x
  (the kinetic block [[0, D/f], [-D/f, 0]]) (1 - beta/2 = 1/3); exact k = 0 spectra in f L; fold band eps = kappa k
  exactly (chi = (e^{f M y}, 0)), so dE/da4 = -E and w_eff(A) = 1/3 for the free gas; drop ks-b4-wolfram (K2 is a
  statement of the withdrawn metric). The bulk band: eps ~ sqrt(M^2 + (p/f)^2 + ...) GROWS as f shrinks: w_eff(A) =
  -(1/3) d ln eps/d a4 can be NEGATIVE (-> -1/9 for p/f >> M): do NOT presume the old dark-matter 1/3 -> 0 law; compute
  and state what the numbers give. compute_eos draft in scratchpad/w6/compute_eos.py (untested: needs the new dense CSV).
* T3 in the corrected metric (hand check): sigma2 h_j(M) sigma2 = h_{-j}(-M) for every f and constant kappa (sigma2
  sigma1 sigma2 = -sigma1, sigma2 sigma3 sigma2 = -sigma3); sigma2 (a, i b) = (b, i a): the fold conditions b(0) = 0 <->
  a(0) = 0 are exchanged and the tip b(-L) = 0 -> a(-L) = 0 (theta -> pi). So T3 holds in the same form; update
  check_t3.py / verify_t3.wls (block equation with 1/f, kappa = e^{-a4}, "brane" -> fold, ks-theory.json keys) and the demos.
* check_t3.py ok_stated looks for the OLD hamiltonian string "h_j=j[-isigma1d/dy+M_eff(y)sigma2+kappa(y)ksigma3]+v_v(y)";
  ks-theory.json now states "h_j = j[-(i/f) sigma1 d/dy + M_eff(y) sigma2 + kappa k sigma3] + v_v(y), kappa = e^{-a4}, f = ...":
  update the stated-form test and h_block (with 1/f; kappa constant) in check_t3.py and verify_t3.wls (W6).
* dark_sector/wolfram/verify_dark_sector_b4.wls (D1-D8, metric of 2026-10-14 via MetricB4.wl): write an independent Wolfram
  twin for the corrected metric (verify_dark_sector.wls: sqrt|g|, conservation with h4, w_eff A/B/C, condensate with the
  author's T16 (S ~ e^{a4} b4^{-2}), flat-mode gas, the record's history source, condensate drift e^{-(5/3) a4}); keep the
  b4 version as a record of the withdrawn metric (gate rows dark-b4-*), as verify_ks_b4.wls.
* DRAFT scratchpad/w6/patch_check_t3.py (h_block with 1/f, stated form, map with a general f); still to do by hand: the ODE
  check (chi' = f N chi), the "brane"/Z2 texts -> fold conditions, verify_t3.wls likewise, both demos.
* notebooks/src/kohn_sham_states.py:825 and tests/test_revision_notebooks.py:171 pin report check counts (ks-reference.json 38 -> 39 after H12; ks-rust-solver.json -> 45; others): update in W6.
* dirac16complex00/python/derive_eos.py sections to redo for the corrected metric: A1 conservation (own Christoffels; the
  local model gl = [e^{-2a4} b4, e^{2a4} x3, -1, -e^{-2a4} b4 x3], sqrt|g| = e^{-a4} b4^2); A2 observer N1 (per extra-time
  and hidden coordinate volume) and N2 (per proper 7-volume): w_eff(N2) = w_eff(N1) - (4 - 2 beta)/3; A3 condensate with
  the author's T16 (A = B - (u - a4'/2) I16, B = -M g4 + (3/2) H e^{a4} b4^{-1/2} g4 g0; C A + A^T C = -2 (u - a4'/2) C ->
  S ~ e^{a4} b4^{-2}; K_x4 = M S), the required source of the history from exponentialHistory.authorWeights (grows with kk),
  "condensate cannot source the history" (S ~ e^{-(5/3) a4} decays); A4 plane waves (hidden momentum l in the flat frame:
  h^2 = (m^2 + k^2 + l^2 - q^2)?); A5 WKB gases: rho ~ omega n, n ~ e^{a4} b4^{-2}, eps = w_eff(N1) per component; A6 models
  M1-M5 (numbers via mpmath): re-derive every number.
* Carry-overs for dirac16complex00 (hand, to verify): per WKB component (Q = Krein charge per coordinate cell, constant)
  E = omega Q, so w_eff(N1) = -(1/3) d ln omega/d a4 = (k_p^2 + (1 - beta/2) q_p^2 - (1 - beta/2) l_p^2)/(3 omega^2) (l: the
  hidden momentum, new in the corrected metric; it LOWERS w_eff and can make it negative: the bulk-band effect);
  q_p ~ a^{1 - beta/2} = a^{1/3} as before; N2 shift -(4 - 2 beta)/3 = -4/9 (before: -1 + beta/2 = -1/3); so M2 N2 tangent
  w0 = -4/9 + r/3, M3: -4/9 + (1/9) s a^(2/3)/(1 - s a^(2/3)); condensate: w_eff(N1) = ((2 beta - 1)/3) w_c = (5/9) w_c,
  u ~ e^{-(5/3) a4}; the phantom window of the ratio w_c is unchanged (lambda S/m in (-2, -1)), but w_eff(N2) = (5/9) w_c - 4/9
  < -1 needs w_c < -1: the same window. The ghost bound: w_eff(N2)(1) >= -4/9 - G/3 -> G >= 3 (0.861 - 4/9) = 1.2497.
* DRAFT scratchpad/w6/d00/python/derive_eos.py (patched by w6/d00_patch_A1A2.py, _A3.py, _A5A6.py, _main.py): 48/48 with
  REVISION_DIR, 3.6 s, outputs in scratchpad/w6/d00_out. New: conservation with h4 (every real z, C/W rules), N1/N2
  (shift -4/9), condensate S ~ e^{a4} b4^{-2} (author's T16, any gravity coefficient), history_required_source (anisotropic:
  kappa (p3 - p0) = -9 kk^2/16 + 1069 kk/432 + 2015/972), condensate_cannot_source_history, WKB with n = e^{a4} b4^{-2},
  models with SHIFT_N2 (M2 tangent (-2749/9000, 81037/500000); ghost bound G >= 3749/3000). Still to do: independent_numerics.py
  (418 lines), the unit tests (92 lines), eos-theory.json regenerated, README, the Wolfram twin.
* dirac16complex00/python/independent_numerics.py (implementation B, numpy): local-model ODE gamma^(x4) d4 phi + (u - a4'/2)
  gamma^(x4) phi + i e^{-a4} k gamma^(x1) phi + i e^{a4} b4^{-1/2} q gamma^(x5) phi = m phi (the term (3/2) H e^{a4} b4^{-1/2}
  gamma^(x0) of the hidden direction dropped, the local-model APPROXIMATION, stated); conserved Krein charge per coordinate
  volume e^{-a4} b4^2 Q (before b4^{3/2} Q); models with SHIFT_N2 = -4/9; B_positive_models_bounded >= -4/9; compare with
  the new eos-theory.json.
* implementation B patch list (independent_numerics.py): step factor exp(-0.75 u dx) -> exp(-(BETA - 0.5) EPS dx) (also in
  diag: dphi = -i h phi - (BETA - 0.5) EPS phi); b4f(lna) = exp(1.5 BETA lna) -> exp((2 BETA - 1) lna) (Q e^{-a4} b4^2 and
  rho e^{-a4} b4^2 constant); conservation rhs (isotropic, p3 = L0 - K1/3, p_t = L0 - K5/3, p0 = L0):
  rhs = -EPS (3 rho + 3 L0 - K1) - (BETA/2 - 1) EPS (4 rho + 4 L0 - K5); model_w: e = p3 + (BETA/2 - 1)(p0 + 3 p_t)/3,
  N2 = N1 - (4 - 2 BETA)/3, N2_dilution unchanged; B_positive_models_bounded >= -4/9 - TOL_W; growth rate
  sqrt(s a^(2/3) - 1) - (BETA - 1/2) EPS; every text (b4^(3/2), (3/4) b4'/b4, sin^{1/3}).
* DRAFT scratchpad/w6/d00/python/independent_numerics.py (w6/d00_patch_B.py): 32/32 against the draft A outputs, 8 s
  (REVISION_DIR; reads scratchpad/w6/d00/eos-theory.json = the draft A's). Still: the unit tests, README, eos-theory.json
  regenerated in place, the Wolfram twin.
* dirac16complex00 tests: update test_key_numbers (M2 (-2749/9000, 81037/500000); M3 w0 -3583/9000, wa -196963/4500000;
  M4 N2 tangent w0 -0.398111111111, wa -0.0666666666667; M5 fit [1/2,1] (-0.443790594178, -0.32308292878), crossings [];
  condensate key historyRequiredSource instead of branchRequiredSource; beta text) and test_readme_cites_the_numbers
  (README rewrite: 461/600, 264037/403037, 57963/264037, -382/441, the new M2 wa 0.162074 (unchanged), -0.0437696, 3749/3000, ...).
* The Wolfram twin verify_dark_sector.wls: build on Revision/metric_warped/wolfram/MetricWarped.wl (the corrected metric,
  MWNormal/MWZeroQ exact for every real z, symbols sv, cv, w) and RevisionFieldTheory.wl (rftGam, the author's T16), and
  a4-equations.json (generalSource, exponentialHistory.authorWeights, fields.dirac16complex00.homogeneousCondensate):
  D1 sqrt|g| = e^{-a4} b4^2 |cot z| |sin z|^{1/2}; D2 conservation with h4; D3 w_eff general (s = 0, 1) with the -(4 - 2 beta)/3
  shift; D4 condensate with T16 (A = B - (u - a4'/2) I16); D5 flat-mode gas with hidden momentum; D6 the record's history
  source (anisotropic, condensate cannot source it); D7 the condensate drift u ~ e^{-(5/3) a4}, wa = (10/3) u/(2 + u)^2.
* DRAFT scratchpad/w6/verify_dark_sector.wls: 7/7 (6 s) with REVISION_DIR=<repo>/Revision (Windows path) and
  EOS00_JSON=<draft eos-theory.json>; D6 cross-checks the dirac16complex00 record (key condensate.historyRequiredSource, sympy
  "**" powers converted). In W6: put it in Revision/dark_sector/wolfram/, gate row (dark-wolfram), provenance row (index row 31
  is the b4 one: add a row or extend), keep verify_dark_sector_b4.wls as the record of the withdrawn metric.
* T3 rework (pairing/kohn_sham): verify_t3.wls (251 lines) and check_t3.py: hBlock with 1/f (f a positive constant on the
  slice), kappa constant (the map holds for general kappa(y) anyway), ODE chi' = f N chi; "brane parities"/Z2 orbifold ->
  the fold conditions theta = 0, pi (the map exchanges them; ks-theory.json boundaryConditions.fold); the Z2-mirror check
  (P_A chi(y) = sigma3 chi(-y), line ~187) is a statement of the withdrawn construction: replace by the fold statement
  (the two halves of a cell, both conditions filled, ASSUMED); weight w_Z2 -> the fold weight; hypotheses H1, H3 texts;
  verify_t3_completion.wls (140 lines) and check_t3_completion.py likewise; t3-theory.json regenerated.
* verify_t3.wls details: H1 text (b4 enters h_j through f now), H3 (Z2 orbifold, weight w_Z2 = 1/2) -> the fold of
  ks-theory.json boundaryConditions.fold (READ it: what weight do the two fold conditions carry? both filled), S1/S5 (brane
  parities, the Z2 mirror copy P_A chi(y) = sigma3 chi(-y)) -> decide from boundaryConditions.fold whether the other half
  of the cell is an image (z -> pi - z) and what it carries; check T3_z2_mirror_copy... must be replaced, not kept;
  the profiles' "2 Vol_7 int e^(6Hy)" -> e^(3Hy); Psi_16 ansatz e^(-3Hy) b4^(-3/4) -> the record's half-density factor
  e^{-(3/2)Hy} e^{a4/2} b4^{-1} (ks-theory.json sectorAndAnsatz.orbital16); the not_established texts.
* IMPORTANT (T3 and the pairing documents, W6/W7): ks-theory.json boundaryConditions.fold: "a spinor continuous across the
  fold has the same chi(y) on both halves" - the corrected metric has NO Z2 mirror copy carrying -m (that was the orbifold of
  the metric of 2026-10-14). So T3's S5 and the check T3_z2_mirror_copy_carries_minus_m_plus_lambda describe a construction
  that no longer exists: REMOVE them (do not re-word); state instead: the fold conditions theta = 0, pi (both filled, w = 1/2)
  are exchanged by the map (T3_fold_conditions_exchanged), both halves of a cell carry the same state. T3 itself (the map
  (m, lambda, theta) -> (-m, +lambda, pi - theta) between two Kohn-Sham problems) still holds. The documents
  PAIR_CREATION_PROOFS and DIRAC16COMPLEX_FIELD_THEORY must not claim a mirror universe with -m from the brane any more.
* notebooks (W6): kohn_sham_states.py (1029 lines: N = 136/688 -> 592/2352, the key e6Hy -> e3Hy, "brane band" -> fold band,
  figure 1 (the fold band eps = e^{-a4}|k| redshifts exactly), the profile figure text (e^{6Hy} -> e^{3Hy}), pinned report
  counts ks-reference.json 39, ks-rust-solver.json 45), dark_sector_hypotheses.py (1820), lovelock_gkd.py (1359; 19 -> 27
  Rust checks); then build/check with Revision/notebooks/tools/build_notebooks.py; PROVENANCE files.
* pairing T1/T2/Q (Revision/pairing: python/check_pairing.py, wolfram/RevisionPairing.wl + verify_pairing.wls,
  pairing-theory.json): recompute in the corrected metric (vielbein e^x0 = e^{-a4} b4^{1/2} cot z (signed), e^xi = e^{a4},
  e^x4 = 1, e^xt = e^{-a4} b4^{1/2} (sin^2 z)^{1/12}; canonical spin connection); z -> pi - z is still an isometry
  (cot^2 and (sin^2)^{1/6} even under it) and g00, sqrt|g| still vanish at z = pi/2; every real z (the W1 normal forms);
  check texts "metric of SPEC section 1 with b4(x4)" -> corrected metric; "Z2 brane at z = pi/2" -> the fold (T2's mirror is
  the isometry z -> pi - z, keep it as an isometry statement, not as an orbifold).
* DRAFT scratchpad/w6/t3/check_t3.py (patch_check_t3_full.py + patch_check_t3_part2.py): 10/10 against the new
  ks-theory.json (mirror check removed, T3.fold_conditions_exchanged reads boundaryConditions.fold); compare.t3_theory pending
  until verify_t3.wls is redone with the same 10 names (T3_fold_conditions_exchanged; no T3_z2_mirror...).
* DRAFT scratchpad/w6/t3w/wolfram/verify_t3.wls (patch_verify_t3.py): 9/9 (REVISION_DIR, Windows path; writes t3-theory.json
  and reports into scratchpad/w6/t3w); the sympy draft against it: 12/12 (compare.t3_theory.* PASS). Still for T3: the
  completion pair (check_t3_completion.py, verify_t3_completion.wls), the demos (t3_rust_demo.py: key e3Hy, Vol_7, texts;
  t3_reference_demo.py), pairing/kohn_sham/README.md, the provenance.
* t3_reference_demo.py (480 lines) MONKEYPATCHES ks_fd.sector_arrays with its own sector_arrays_general (line ~93) that still
  uses kap = exp(-H y - a4) (the OLD kappa) and no 1/f: rebuild it from the corrected ks_fd.sector_arrays (finv on bs and
  dphi, kappa = e^{-a4} constant) and generalise only the frame (tip_pi); its own orbitals_ext_patched likewise; texts
  (Vol_7 e^{(5/3) a4}, fold). t3_rust_demo.py: key emtIntegrals_2Vol7_int_e3Hy, texts (Vol_7, fold, e^(3Hy)).
* DRAFT scratchpad/w6/patch_t3_reference_demo.py: the numerics of sector_arrays_general (kappa = e^{-a4} constant, 1/f on
  bs and dphi); orbitals_ext_patched needs no f (frame only). Texts still to do; run the demo (both members on 3 grids) in W6.
* t3_rust_demo.py texts (W6): the docstring (b4 does not enter h_j; Vol_7 e^{(3/2) beta a4,0}; sin^{1/6} z; brane),
  "background" (Vol_7 = ell^3 v_t e^{2 a4,0} - inconsistent even before), the t3_equal text (2 Vol_7 int e^(6Hy)), the members
  text (brane parities -> fold conditions), the control text (zero modes (e^(-f m y), 0) at the tip), not_established (ASSUMED
  Z2 brane -> both fold conditions filled, ASSUMED). Key emtIntegrals_2Vol7_int_e6Hy -> e3Hy (8 places).
* DRAFT scratchpad/w6/t3w/wolfram/verify_t3_completion.wls (patch_verify_t3_completion.py + ..._completion2.py): 3/3
  (the zero mode is (E^(f M y), 0) with the hidden scale; the first try with E^(M y) FAILED as it should). The sympy
  completion draft scratchpad/w6/t3/check_t3_completion.py (patch_check_t3_completion.py): make its zero-mode part use
  e^{f M y} too (it still uses f = 1 there); run after the two demos.
* check_pairing.py (1103 lines) W6 patch: Geometry f = [s0 e^{-a4} sqrt(b4) cot z] + [e^{a4}] x3 + [1] + [e^{-a4} sqrt(b4) S6] x3
  (S6 = sin^{1/6} z on the patches z in (0, pi/2), s0 = +1, and (pi/2, pi), s0 = -1, where sin z > 0: (sin^2)^{1/12} = S6);
  geometry.brane_degenerate: sqrtg = e^{-a4} b4^2 cot z sin^{1/2} z (patch), g00 -> 0 and sqrtg -> 0 at z = pi/2 (rename to
  geometry.fold_degenerate); geometry.connection_depends_on_b4 unchanged (the extra-time vielbein is the same on the
  patch); mirror isometry z -> pi - z holds (cot^2, sin^{1/3} even); texts (SPEC section 1 metric, "Z2 brane" -> the fold);
  RevisionPairing.wl + verify_pairing.wls likewise; pairing-theory.json regenerated.
* 2026-10-17 drafts: w6/patch_check_pairing2.py (remaining texts, NOT_ESTABLISHED with the tokens 'across the fold' and
  'degenerate', comparison topics renamed), w6/patch_verify_pairing.py (verify_pairing.wls + RevisionPairing.wl: EPrim =
  diag(e^-a4 b4^(1/2) cot z, e^a4 x3, 1, e^-a4 b4^(1/2) sin^(1/6) z x3), gAuthor with (Sin^2)^(1/6), sqrtgPrim = e^-a4 b4^2
  cot z sin^(1/2) z, REVISION_DIR) -> copies in w6/pairing/{python,wolfram}; NOT RUN yet (pairing-wolfram budget 280 s,
  pairing-sympy 240 s: run after the W5 commit, one at a time).  w6/patch_t3_rust_demo.py (key e3Hy x12, texts) applied to
  w6/t3demo/t3_rust_demo.py.  t3_reference_demo.py: N = 136 is HARD-CODED in spec_list (lines 229, 231) and in the texts
  (lines 22-23, 410, 418): use N_mid from parameters.json (592); the exact image spectra test is at a4,0 = 0 (f = 1).
* RUN-TIME RISK (W6): the gate row t3-rust-demo (320 s, long) solves 3 members x 210 states of the NEW matrix (N up to
  2352; the canonical matrix alone needed two parts of ~130 s): expect ~800 s -> split into parts with a cache (like the
  solver's --part) BEFORE running it; t3-reference-demo (170 s) with N = 592 instead of 136: measure on one state first.
* compute_eos draft (w6/compute_eos.py) on the new dense history (2026-10-17 07:0x): 13/13, 0.5 s; free gas w_eff(A) = 1/3 exactly, interacting N = 592/2352 w_eff(A) in [0.3306, 0.3361], C in [-0.1139, -0.1083]; N = 8 w_eff(A) in [0.232, 0.408]; condensate w_eff(A) = -0.4244, C = -0.8689, wa = -1.2479; gas tangent |wa| <= 0.0039.
* independent_free_gas draft (w6/independent_free_gas.py) on the new dense history (2026-10-17): 3/10, 92 s. FAILS: fold_band_dispersion (the even level of h_(+1) is NOT e^(-a4)|k|: deviation 2.24), hence aufbau, energy_vs_rust (22x), w_eff, cpl. The exact k = 0 spectra pass (4e-14). Debug in W6: the boundary rows of the collocation for k != 0 (fold b(0) = 0, tip b(-L) = 0) or the sector/sign convention of h_j at k != 0 (the fold-band orbital (e^(f m y), 0) must be an exact eigenvector with eps = +kappa k for j = +1). Runtime 92 s: keep under 423 s.
* w6/patch_d00_tests.py applied to w6/d00/tests/ (key numbers of draft A; README citations 3749/3000, -4/9, 'corrected': the README rewrite must contain them).
* independent_free_gas FIX (2026-10-17): the collocation leaves at eps = kappa k a 2-dim eigenspace (the fold-band orbital (e^{f m y}, 0) and a spurious polynomial partner with b = 0); eig returned mixtures and the resolution filter rejected both, so the fold band was missing for k != 0. Fixed in w6/independent_free_gas.py: eigenvalues clustered (1e-9 relative), inside a cluster the right singular vectors of the Chebyshev tails give the candidates, the resolution test keeps the resolved ones; a component below 1e-12 of the other is not tail-tested. Probe: the fold-band level found once with d eps/d a4 = -eps at a4 = 0, 1, 2.
* notebooks/src/kohn_sham_states.py rewrite plan (W6): 4.1 the corrected metric (g00 = e^{-2a4} b4 cot^2 z, g_ii = e^{2a4},
  g_tt = -e^{-2a4} b4 (sin^2 z)^{1/6}, every real z; Vol_7 = ell^3 v_t e^{(5/3) a4}); 4.2 h_j with 1/f and kappa = e^{-a4}
  constant (no b4^{-3/4} factor story: the record's half-density factor), 4.3 N = 8, 592, 2352 (closed fold-band shells),
  effective coupling lambda_hat e^{-(5/3) a4,0}; 4.4 the fold (both conditions filled, ASSUMED) instead of the Z2 brane;
  section 7 SERIES (N136_lamp1 -> N592_lamp1, N688_lam0 -> N2352_lam0, THERMAL_ID N592_lamp1_a10_T20); every key
  emtIntegrals_2Vol7_int_e6Hy -> e3Hy (lines 677, 732, 742, 774, 943); section 9.2 pinned counts (ks-reference.json 39,
  ks-rust-solver.json 45, determinism 14, mermin roots 5, crosscheck: from the report); figure 1 "brane band" -> fold band
  (eps = e^{-a4}|k| exactly); figure 2 profile weight e^{-3Hy} (was e^{-6Hy}), N592 file; figure 3/4 series names; the
  closing summary (line ~1006). Then build/check with Revision/notebooks/tools/build_notebooks.py and the PROVENANCE files.
* independent_free_gas draft: 10/10 after the fix (104 s single-threaded; gate row dark16-independent budget 180 s): exact k = 0 spectra (the zero mode is the resolved member of its pair, no longer inserted in that check), fold band to 5e-14, E vs Rust 3.5e-13, w_eff(A) = 1/3 to 1.2e-13, CPL vs primary 3.7e-11; bulk band w_eff(A) from 0.3187 (a4 = -3) to -0.0811 (a4 = 4), sign change between -0.5 and -0.25.
