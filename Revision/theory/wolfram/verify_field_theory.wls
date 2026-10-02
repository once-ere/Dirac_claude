#!/usr/bin/env wolframscript
(* ::Package:: *)

(* verify_field_theory.wls

   Driver for Revision/theory/wolfram/RevisionFieldTheory.wl (Revision/SPEC.md, sections 1-4 and 6).
   Writes, deterministically (LF line endings, no time stamps):
     Revision/theory/reports/wolfram-field-theory.json   every check with name, verdict, detail
     Revision/theory/field-theory.json                   the exact formulas for the documents
   Usage:  wolframscript -file Revision/theory/wolfram/verify_field_theory.wls
   Every check is exact symbolic algebra (no floating point).  Both statistics are treated:
   "G" = dirac16complex (explicit Grassmann algebra, N = 2 generators theta_1, theta_2 and their
   conjugates), "C" = dirac16complex00 (commuting complex components).  Exit code 0 if every check
   passes, 1 otherwise.
*)

$here = DirectoryName[$InputFileName];
$theoryDir = FileNameJoin[{$here, ".."}];
$revDir = FileNameJoin[{$theoryDir, ".."}];
Get[FileNameJoin[{$here, "RevisionFieldTheory.wl"}]];
rftLoadFixture[FileNameJoin[{$revDir, "algebra", "gammas.json"}]];

t0 = AbsoluteTime[]; tSec = t0;
section[name_] := (Print["[", Round[AbsoluteTime[] - tSec, 0.1], " s] -> ", name]; tSec = AbsoluteTime[]);
checks = {};
addCheck[name_String, ok_, detail_String] := (
  AppendTo[checks, <|"name" -> name, "verdict" -> If[TrueQ[ok], "PASS", "FAIL"], "detail" -> detail|>];
  Print[If[TrueQ[ok], "PASS  ", "FAIL  "], name]);
formulas = {};
wl[e_] := ToString[e, InputForm];
addFormula[key_String, desc_String, e_] := AppendTo[formulas, <|"key" -> key, "description" -> desc, "wl" -> wl[e]|>];
addFormulaText[key_String, desc_String, text_String] := AppendTo[formulas, <|"key" -> key, "description" -> desc, "wl" -> text|>];
statName["G"] = "dirac16complex (Grassmann)"; statName["C"] = "dirac16complex00 (commuting)";
stats = {"G", "C"};
g = rftGam; eta = rftEta; id16 = rftI16; z16 = rftZ16; Cm = rftC; Bm = rftB;
X = rftX; f = rftF; sg = rftSqrtG0;
a4p = Derivative[1][a4][x4];

(* ================================================================== the exact zero test *)
addCheck["zero_test_sanity",
  rftZeroQ[ph[1] @@ X (Sin[6 H x8]^2 + Cos[6 H x8]^2 - 1)] && !rftZeroQ[ph[1] @@ X] && !rftZeroQ[pf[x8]] &&
  rftZeroQ[U'[ph[1] @@ X phc[1] @@ X] ph[2] @@ X - ph[2] @@ X U'[phc[1] @@ X ph[1] @@ X]] && rftZeroQ[E^a4[x4] E^-a4[x4] - 1] &&
  rftZeroQ[cA[1] H - cA[1] H Cot[6 H x8] Tan[6 H x8]] && !rftZeroQ[D[ph[1] @@ X, x1] - D[ph[1] @@ X, x2]] && !rftZeroQ[H Sin[6 H x8]^(1/6) - H] &&
  !rftZeroQ[ph[1] @@ X (Sin[6 H x8]^2 + Cos[6 H x8]^2)],
  "the exact zero test (field functions, their derivatives and U-expressions as independent polynomial variables; coefficients reduced with Sin z = w^6, w > 0, Cos^2 = 1 - Sin^2) " <>
  "returns True on identities and False on nonzero expressions in a set of control cases"];

(* ================================================================== 0. fixture *)
section["fixture"];
addCheck["fixture_Clifford_relation",
  And @@ Flatten[Table[g[[a]] . g[[b]] + g[[b]] . g[[a]] == 2 eta[[a, b]] id16, {a, 8}, {b, 8}]] && rftEtaFixture == Diagonal[eta],
  "the gammas read from Revision/algebra/gammas.json satisfy {gamma^a, gamma^b} = 2 eta^ab I16 with eta = diag(1,1,1,-1,-1,-1,-1,1) (order x1..x8), as recorded in the fixture"];
addCheck["fixture_C_B_S_consistent",
  Cm == g[[8]] . g[[1]] . g[[2]] . g[[3]] && Bm == -I Cm . g[[4]] && rftChir == Dot @@ g[[{8, 1, 2, 3, 4, 5, 6, 7}]] &&
  And @@ Flatten[Table[rftS[[a, b]] == (1/4) (g[[a]] . g[[b]] - g[[b]] . g[[a]]), {a, 8}, {b, 8}]] &&
  Transpose[Cm] == Cm && Cm . Cm == id16 && And @@ Table[Transpose[Cm . g[[a]]] == -Cm . g[[a]], {a, 8}],
  "C = gamma^(x8) gamma^(x1) gamma^(x2) gamma^(x3) (real symmetric, C^2 = 1, C gamma^a antisymmetric), B = -i C gamma^(x4), Gamma = gamma^(x8) gamma^(x1)...gamma^(x7), S^ab = (1/4)[gamma^a, gamma^b], all as decoded from the fixture"];

(* ================================================================== 1. geometry *)
section["geometry"];
rftBuildGeometry[];
Gm = rftGamma0;
addCheck["metric_is_the_authors",
  rftZeroQ[rftG0 - rftMetricAuthor] && rftZeroQ[Transpose[rftE0] . eta . rftE0 - rftMetricAuthor],
  "g = e^T eta e with the diagonal vielbein e^a_mu = f_a delta^a_mu, f(x1,x2,x3) = E^a4 Sin[z]^(1/6), f(x4) = 1, f(x5,x6,x7) = E^-a4 Sin[z]^(1/6), f(x8) = Cot[z], z = 6 H x8, reproduces the author's metric of SPEC section 1 entry by entry"];
addCheck["vielbein_inverse",
  rftZeroQ[rftE0 . rftEinv0 - IdentityMatrix[8]] &&
  rftZeroQ[Table[Sum[rftEinv0[[mu, a]] rftEinv0[[nu, a]] eta[[a, a]], {a, 8}] - rftGinv0[[mu, nu]], {mu, 8}, {nu, 8}]],
  "e^a_mu e_a^nu = delta and e_a^mu e_b^nu eta^ab = g^munu (inverse vielbein e_a^mu = delta_a^mu / f_a)"];
detG = Det[rftG0];
addCheck["sqrt_det_g_is_cos_z",
  rftZeroQ[detG - Cos[rftZ]^2] && Simplify[Cos[rftZ] > 0, rftAssumptions] && rftZeroQ[Times @@ f - Cos[rftZ]],
  "det g = Cos[z]^2 (four negative entries), so sqrt|det g| = f1...f8 = Sin[z] Cot[z] = Cos[z] > 0 on 0 < z < Pi/2; it does not depend on x4: the 3-space inflation e^(3 a4) and the extra-time deflation e^(-3 a4) compensate in the volume"];
addCheck["degenerate_at_H_0",
  Limit[Sin[6 H x8]^(1/3), H -> 0] === 0 && Limit[Cot[6 H x8]^2, H -> 0, Direction -> "FromAbove", Assumptions -> x8 > 0] === Infinity,
  "at fixed x8 and H -> 0+ the entries g11 = g22 = g33 -> 0, g55 = g66 = g77 -> 0 and g88 -> infinity: H = 0 is not a metric of the family (a degenerate limit); every statement below assumes H > 0 and 0 < z < Pi/2"];
gamNZ = DeleteCases[Flatten[Table[{l, mm, n, rftSimp[Gm[[l, mm, n]]]}, {l, 8}, {mm, 8}, {n, mm, 8}], 2], {_, _, _, 0}];
addFormula["christoffel_nonzero", "nonzero Christoffel symbols {l, m, n, Gamma^l_mn} (m <= n; Gamma^l_nm = Gamma^l_mn), indices 1..8 = x1..x8", gamNZ];
addCheck["christoffel_count",
  Length[gamNZ] == 25,
  "the Levi-Civita connection has " <> ToString[Length[gamNZ]] <> " independent nonzero symbols Gamma^l_mn (m <= n): listed in field-theory.json (christoffel_nonzero)"];
Rm = rftRiemann[Gm];
Ric = Table[Sum[Rm[[r, s, r, n]], {r, 8}], {s, 8}, {n, 8}];
RicMixed = Table[Sum[rftGinv0[[mu, s]] Ric[[s, nu]], {s, 8}], {mu, 8}, {nu, 8}];
Rs = Sum[RicMixed[[mu, mu]], {mu, 8}];
RsSimp = rftSimp[Rs];
addCheck["ricci_scalar",
  rftZeroQ[Rs - 6 (a4p^2 - 7 H^2)],
  "Ricci scalar R = g^sn R^r_srn = 6 (a4'^2 - 7 H^2) (convention R^r_smn = d_m Gamma^r_ns - d_n Gamma^r_ms + Gamma^r_ml Gamma^l_ns - Gamma^r_nl Gamma^l_ms)"];
ricExpected = DiagonalMatrix[{-6 H^2 + a4''[x4], -6 H^2 + a4''[x4], -6 H^2 + a4''[x4], 6 a4p^2,
   -6 H^2 - a4''[x4], -6 H^2 - a4''[x4], -6 H^2 - a4''[x4], -6 H^2}];
addCheck["ricci_mixed_components",
  rftZeroQ[RicMixed - ricExpected],
  "R^mu_nu is diagonal: R^1_1 = R^2_2 = R^3_3 = a4'' - 6 H^2, R^4_4 = 6 a4'^2, R^5_5 = R^6_6 = R^7_7 = -a4'' - 6 H^2, R^8_8 = -6 H^2 (in particular R^4_8 = R^8_4 = 0)"];
addFormula["ricci_mixed_diagonal", "R^mu_mu (no sum), mu = x1..x8; all off-diagonal R^mu_nu vanish", Diagonal[ricExpected]];
addFormula["ricci_scalar", "Ricci scalar R", 6 (a4p^2 - 7 H^2)];
addCheck["never_flat_for_H_positive",
  rftZeroQ[RicMixed[[8, 8]] + 6 H^2] && Simplify[-6 H^2 < 0, H > 0],
  "R^(x8)_(x8) = -6 H^2 < 0 for every H > 0 and every function a4: the metric is curved for every admissible H, whatever a4 is (a4 constant included)"];

(* ================================================================== 2. spin connection *)
section["spin connection"];
omMix = rftOmegaMix0; omLow = rftOmegaLow0; Om = rftOm0; gup = rftGup0;
addCheck["vielbein_postulate",
  rftZeroQ[Table[D[rftE0[[a, nu]], X[[mu]]] - Sum[Gm[[l, mu, nu]] rftE0[[a, l]], {l, 8}] + Sum[omMix[[mu, a, b]] rftE0[[b, nu]], {b, 8}], {mu, 8}, {a, 8}, {nu, 8}]],
  "d_mu e^a_nu - Gamma^l_mu,nu e^a_l + omega_mu^a_b e^b_nu = 0 for all 512 components, with omega_mu^a_b = e^a_nu (d_mu e_b^nu + Gamma^nu_mu,l e_b^l)"];
addCheck["omega_antisymmetric",
  rftZeroQ[Table[omLow[[mu, a, b]] + omLow[[mu, b, a]], {mu, 8}, {a, 8}, {b, 8}]],
  "omega_mu,ab = eta_ac omega_mu^c_b = -omega_mu,ba (metric compatibility)"];
omNZ = DeleteCases[Flatten[Table[{mu, a, b, rftSimp[omLow[[mu, a, b]]]}, {mu, 8}, {a, 8}, {b, a + 1, 8}], 2], {_, _, _, 0}];
omExpected = Join[
  Flatten[Table[{{i, i, 4, E^a4[x4] Sin[rftZ]^(1/6) a4p}, {i, i, 8, H E^a4[x4] Sin[rftZ]^(1/6)}}, {i, 1, 3}], 1],
  Flatten[Table[{{t, 4, t, -E^(-a4[x4]) Sin[rftZ]^(1/6) a4p}, {t, t, 8, -H E^(-a4[x4]) Sin[rftZ]^(1/6)}}, {t, 5, 7}], 1]];
addCheck["omega_components",
  Length[omNZ] == 12 && Sort[omNZ[[All, 1 ;; 3]]] == Sort[omExpected[[All, 1 ;; 3]]] &&
  And @@ Table[rftZeroQ[omLow[[Sequence @@ e[[1 ;; 3]]]] - e[[4]]], {e, omExpected}],
  "exactly 12 independent nonzero omega_mu,ab (a < b): for i = x1, x2, x3: omega_i,(i)(x4) = a4' E^a4 Sin[z]^(1/6), omega_i,(i)(x8) = H E^a4 Sin[z]^(1/6); " <>
  "for t = x5, x6, x7: omega_t,(x4)(t) = -a4' E^-a4 Sin[z]^(1/6), omega_t,(t)(x8) = -H E^-a4 Sin[z]^(1/6); omega_x4 = omega_x8 = 0. " <>
  "Every component is a4' or H times a nonvanishing factor"];
addFormula["omega_nonzero", "nonzero omega_mu,ab = eta_ac omega_mu^c_b as {mu, a, b, value} with a < b (omega_mu,ba = -omega_mu,ab); frame indices a, b = 1..8 aligned with x1..x8", omExpected];
addCheck["Omega_components",
  rftZeroQ[Om - Table[Sum[If[e[[1]] == mu, e[[4]] (1/2) g[[e[[2]]]] . g[[e[[3]]]], 0], {e, omExpected}], {mu, 8}]] &&
  rftZeroQ[Om[[4]]] && rftZeroQ[Om[[8]]],
  "Omega_mu = (1/2) omega_mu,ab S^ab = sum_(a<b) omega_mu,ab (1/2) gamma^a gamma^b: Omega_xi = (1/2) E^a4 Sin[z]^(1/6) (a4' gamma^(xi) gamma^(x4) + H gamma^(xi) gamma^(x8)) for i = 1, 2, 3; " <>
  "Omega_xt = -(1/2) E^-a4 Sin[z]^(1/6) (a4' gamma^(x4) gamma^(xt) + H gamma^(xt) gamma^(x8)) for t = 5, 6, 7; Omega_x4 = Omega_x8 = 0"];
addFormulaText["Omega_components",
  "the spinor connection Omega_mu = (1/2) omega_mu,ab S^ab",
  "Omega_xi = (1/2) E^a4[x4] Sin[6 H x8]^(1/6) (a4'[x4] g[xi].g[x4] + H g[xi].g[x8]) (i = 1, 2, 3); Omega_xt = -(1/2) E^-a4[x4] Sin[6 H x8]^(1/6) (a4'[x4] g[x4].g[xt] + H g[xt].g[x8]) (t = 5, 6, 7); Omega_x4 = Omega_x8 = 0; g[xa] = gamma^(xa) (frame gammas of the fixture)"];
covConst = Table[D[gup[[n]], X[[mu]]] + Sum[Gm[[n, mu, l]] gup[[l]], {l, 8}] + Om[[mu]] . gup[[n]] - gup[[n]] . Om[[mu]], {mu, 8}, {n, 8}];
addCheck["gamma_covariantly_constant",
  rftZeroQ[covConst],
  "D_mu gamma^nu = d_mu gamma^nu + Gamma^nu_mu,l gamma^l + [Omega_mu, gamma^nu] = 0 for all 64 (mu, nu), gamma^nu = e_a^nu gamma^a (the canonical connection is the one that makes the gammas covariantly constant)"];
addCheck["S_rotates_gamma_with_omega",
  rftZeroQ[Table[Om[[mu]] . g[[c]] - g[[c]] . Om[[mu]] + Sum[omMix[[mu, c, b]] g[[b]], {b, 8}], {mu, 8}, {c, 8}]],
  "[Omega_mu, gamma^c] = -omega_mu^c_b gamma^b (the frame form of covariant constancy)"];
(* spin curvature *)
Fsp[mu_, nu_] := D[Om[[nu]], X[[mu]]] - D[Om[[mu]], X[[nu]]] + Om[[mu]] . Om[[nu]] - Om[[nu]] . Om[[mu]];
Rframe[a_, b_, mu_, nu_] := Sum[eta[[a, a]] rftE0[[a, r]] Rm[[r, s, mu, nu]] rftEinv0[[s, b]], {r, 8}, {s, 8}];
addCheck["spin_curvature_equals_Riemann",
  rftZeroQ[Table[Fsp[mu, nu] - (1/2) Sum[Rframe[a, b, mu, nu] rftS[[a, b]], {a, 8}, {b, 8}], {mu, 8}, {nu, mu + 1, 8}]],
  "[D_mu, D_nu] Psi = (d_mu Omega_nu - d_nu Omega_mu + [Omega_mu, Omega_nu]) Psi = (1/2) R_ab,mu,nu S^ab Psi with R_ab,mu,nu = eta_aa e^a_r R^r_s,mu,nu e_b^s, all 28 pairs: " <>
  "the integrability (compatibility) condition of the spinor connection; it also shows that Omega cannot vanish in any frame unless the Riemann tensor vanishes (flat space)"];

(* gamma^mu Omega_mu *)
section["gamma^mu Omega_mu"];
gO = Sum[gup[[mu]] . Om[[mu]], {mu, 8}];
perDir = Table[gup[[mu]] . Om[[mu]], {mu, 8}];
coefDir = Table[Simplify[Tr[g[[a]] . perDir[[mu]]]/(16 eta[[a, a]])], {mu, 8}, {a, 8}];
addCheck["gammaOmega_equals_3H_gamma_x8",
  rftZeroQ[gO - 3 H g[[8]]],
  "gamma^mu Omega_mu = 3 H gamma^(x8) exactly (a constant matrix; independent of a4, x4 and x8)"];
addCheck["gammaOmega_x4_terms_cancel",
  And @@ Table[rftZeroQ[perDir[[mu]] - (a4p/2 g[[4]] + H/2 g[[8]])], {mu, 1, 3}] &&
  And @@ Table[rftZeroQ[perDir[[mu]] - (-a4p/2 g[[4]] + H/2 g[[8]])], {mu, 5, 7}] &&
  rftZeroQ[perDir[[4]]] && rftZeroQ[perDir[[8]]],
  "per direction (no sum): gamma^(xi) Omega_xi = (a4'/2) gamma^(x4) + (H/2) gamma^(x8) for each inflating 3-space direction i = 1, 2, 3, and " <>
  "gamma^(xt) Omega_xt = -(a4'/2) gamma^(x4) + (H/2) gamma^(x8) for each deflating extra time t = 5, 6, 7; gamma^(x4) Omega_x4 = gamma^(x8) Omega_x8 = 0. " <>
  "The x4-direction (time) terms +3 a4'/2 (3 inflating) and -3 a4'/2 (3 deflating) cancel exactly; the hidden-direction terms of all six directions add: 6 x H/2 = 3 H"];
addFormula["gammaOmega_per_direction", "the matrices gamma^mu Omega_mu (no sum) for mu = x1..x8 as coefficients of gamma^(x4) and gamma^(x8): {mu, coefficient of gamma^(x4), coefficient of gamma^(x8)}",
  Table[{mu, coefDir[[mu, 4]], coefDir[[mu, 8]]}, {mu, 8}]];
addFormula["gammaOmega_total", "gamma^mu Omega_mu (sum over mu); g[x8] = gamma^(x8)", 3 H gamma["x8"]];
addCheck["gammaOmega_divergence_form",
  rftZeroQ[gO - 1/(2 sg) Sum[D[sg gup[[mu]], X[[mu]]], {mu, 8}]] &&
  rftZeroQ[Table[gup[[mu]] . Om[[mu]] + Om[[mu]] . gup[[mu]], {mu, 8}]],
  "{gamma^mu, Omega_mu} = 0 for each mu separately (Omega_mu contains only S^(mu b)), hence gamma^mu Omega_mu = (1/(2 sqrt g)) d_mu (sqrt g gamma^mu); " <>
  "for this metric (1/(2 sqrt g)) d_x8(sqrt g e_8^x8) gamma^(x8) = (1/(2 Cos z)) d_x8 (Sin z) gamma^(x8) = 3 H gamma^(x8), and d_x4 (sqrt g e_4^x4) = d_x4 Cos z = 0"];

(* ================================================================== 3. fields and Lagrangian *)
section["Lagrangian, both statistics"];
fld = Association[Table[st -> <|"Psi" -> rftField[st], "Psic" -> rftFieldC[st]|>, {st, stats}]];
Ldata = Association[Table[st -> Module[{P = fld[st]["Psi"], Pc = fld[st]["Psic"]},
  <|"L0" -> rftL0[st, rftGeo0, P, Pc], "L" -> rftLag[st, rftGeo0, P, Pc], "Lu" -> rftLagUnsym[st, rftGeo0, P, Pc],
    "E" -> rftE[st, rftGeo0, P, Pc], "Ebar" -> rftEbar[st, rftGeo0, P, Pc], "S" -> rftSbil[st, P, Pc]|>], {st, stats}]];
grassKeysOK = Sort[Keys[Ldata["G"]["L"]]] == Sort[{{1, 3}, {1, 4}, {2, 3}, {2, 4}, {1, 2, 3, 4}}];
addCheck["grassmann_algebra_structure",
  gMul[gTheta[1], gTheta[2]] == <|{1, 2} -> 1|> && gMul[gTheta[2], gTheta[1]] == <|{1, 2} -> -1|> && gMul[gTheta[1], gTheta[1]] == <||> &&
  gConj[gMul[gTheta[1], gTheta[2]]] == gMul[gThetaBar[2], gThetaBar[1]] && gConj[gConj[<|{1, 4} -> c1 + I c2|>]] == <|{1, 4} -> c1 + I c2|> &&
  grassKeysOK && !gZeroQ[gMul[Ldata["G"]["S"], Ldata["G"]["S"]]] && gMul[gMul[Ldata["G"]["S"], Ldata["G"]["S"]], Ldata["G"]["S"]] == <||>,
  "explicit Grassmann algebra on theta_1, theta_2, thetabar_1, thetabar_2: theta_i theta_j = -theta_j theta_i, theta_i^2 = 0, conj(theta_1 theta_2) = thetabar_2 thetabar_1, conj conj = id; " <>
  "Psi_A = sum_k ph[A,k](x) theta_k; L has components only on thetabar_k theta_l (bilinear) and theta_1 theta_2 thetabar_1 thetabar_2 (quartic); S = Psibar Psi is even with S^2 != 0 and S^3 = 0, so U = u1 S + (lam/2) S^2 is the most general potential"];
Do[With[{L = Ldata[st]["L"]},
  addCheck["L_real_" <> st, sZeroQ[st, If[st === "G", gAdd[{gConj[L], gScal[-1, L]}], sConj[st, L] - L]],
    "L* = L exactly for " <> statName[st] <> If[st === "G",
      " (the involution reverses the order of Grassmann factors; U = u1 S + (lam/2) S^2 with real u1, lam)",
      " (ph <-> phc, i -> -i; U a real function)"] <>
    ": C real symmetric, C gamma^a real antisymmetric and S^T C + C S = 0 make the symmetrised kinetic term and Psibar Psi real without a factor i"]], {st, stats}];
Do[With[{P = fld[st]["Psi"], Pc = fld[st]["Psic"]},
  Module[{div, lhs},
    div = sAdd[st, Table[sD[st, sScal[st, sg, sDot[st, Pc, matVec[st, Cm . gup[[mu]], P]]], X[[mu]]], {mu, 8}]];
    lhs = sAdd[st, {Ldata[st]["L"], sScal[st, -1, Ldata[st]["Lu"]], sScal[st, 1/2, div]}];
    addCheck["L_total_divergence_to_unsymmetrised_" <> st, sZeroQ[st, lhs],
      "L = sqrt g [Psibar gamma^mu D_mu Psi - m S - U] - (1/2) d_mu (sqrt g Psibar gamma^mu Psi) exactly, for " <> statName[st] <>
      ": the two forms differ by a total divergence and give the same field equations"]]], {st, stats}];
Do[With[{P = fld[st]["Psi"], Pc = fld[st]["Psic"]},
  Module[{Lflat, geoFlat},
    geoFlat = <|"sqrtg" -> sg, "gup" -> gup, "Om" -> Table[z16, {8}]|>;
    Lflat = rftLag[st, geoFlat, P, Pc];
    addCheck["L_spin_connection_drops_out_" <> st, sZeroQ[st, sAdd[st, {Ldata[st]["L"], sScal[st, -1, Lflat]}]],
      "for this diagonal metric Psibar {gamma^mu, Omega_mu} Psi = 0 term by term, so L = sqrt g [(1/2)(Psibar gamma^mu d_mu Psi - d_mu Psibar gamma^mu Psi) - m S - U] exactly (" <>
      statName[st] <> "); the canonical spin connection reaches the field equations through d_mu(sqrt g gamma^mu) = 2 sqrt g gamma^mu Omega_mu (variation of the derivative terms), " <>
      "and the unsymmetrised form contains it explicitly"]]], {st, stats}];
addFormulaText["Lagrangian",
  "Lagrangian density for both statistics (SPEC section 3), Psibar = Psi^dagger C, S = Psibar Psi, sqrt g = Cos[z]",
  "L = Cos[z] [ (1/2) sum_mu (Psibar gamma^mu D_mu Psi - (D_mu Psibar) gamma^mu Psi) - m S - U(S) ] = Cos[z] [ (1/2) sum_a (1/f_a) (Psibar gamma^(a) d_a Psi - d_a Psibar gamma^(a) Psi) - m S - U(S) ]; f_(1,2,3) = E^a4 Sin[z]^(1/6), f_4 = 1, f_(5,6,7) = E^-a4 Sin[z]^(1/6), f_8 = Cot[z]"];

(* ================================================================== 4. Euler-Lagrange equations *)
section["Euler-Lagrange equations"];
ELc = <||>; ELp = <||>;
Do[Module[{L = Ldata[st]["L"], E1 = Ldata[st]["E"], Eb = Ldata[st]["Ebar"], CE, okc = True, okp = True},
  CE = matVec[st, Cm, E1];
  If[st === "C",
    Do[ELc[{st, A}] = rftVarDer[st, L, phc[A]]; ELp[{st, A}] = rftVarDer[st, L, ph[A]];
      okc = okc && rftZeroQ[ELc[{st, A}] - sg CE[[A]]];
      okp = okp && rftZeroQ[ELp[{st, A}] + sg Eb[[A]]], {A, 16}],
    Do[ELc[{st, A, k}] = rftVarDer[st, L, phc[A, k]]; ELp[{st, A, k}] = rftVarDer[st, L, ph[A, k]];
      okc = okc && gZeroQ[gAdd[{ELc[{st, A, k}], gScal[-sg, gMul[gThetaBar[k], CE[[A]]]]}]];
      okp = okp && gZeroQ[gAdd[{ELp[{st, A, k}], gScal[-sg, gMul[gTheta[k], Eb[[A]]]]}]], {A, 16}, {k, rftGN}]];
  addCheck["EL_Psibar_" <> st, okc,
    If[st === "G",
      "for every A = 1..16 and k = 1, 2: dL/dphc[A,k] - d_mu dL/d(d_mu phc[A,k]) = thetabar_k sqrt g (C E)_A with E = gamma^mu D_mu Psi - (m + U'(S)) Psi, U'(S) = u1 + lam S (explicit Grassmann algebra): the field equation is gamma^mu D_mu Psi = (m + U'(S)) Psi",
      "for every A = 1..16: dL/dPhi*_A - d_mu dL/d(d_mu Phi*_A) = sqrt g (C E)_A with E = gamma^mu D_mu Phi - (m + U'(S)) Phi (general U): the field equation is gamma^mu D_mu Phi = (m + U'(S)) Phi"]];
  addCheck["EL_Psi_" <> st, okp,
    If[st === "G",
      "for every A, k: dL/dph[A,k] - d_mu dL/d(d_mu ph[A,k]) = theta_k sqrt g Ebar_A with Ebar = (D_mu Psibar) gamma^mu + (m + U'(S)) Psibar (sign from moving theta_k to the left): the adjoint equation (D_mu Psibar) gamma^mu = -(m + U'(S)) Psibar",
      "for every A: dL/dPhi_A - d_mu dL/d(d_mu Phi_A) = -sqrt g Ebar_A with Ebar = (D_mu Phibar) gamma^mu + (m + U'(S)) Phibar: the adjoint equation (D_mu Phibar) gamma^mu = -(m + U'(S)) Phibar"]]], {st, stats}];
Do[Module[{E1 = Ldata[st]["E"], Eb = Ldata[st]["Ebar"], conjE},
  conjE = vecMat[st, sConj[st, #] & /@ E1, Cm];
  addCheck["adjoint_equation_is_Dirac_conjugate_" <> st,
    And @@ Table[sZeroQ[st, sAdd[st, {conjE[[A]], Eb[[A]]}]], {A, 16}],
    "E^dagger C = -Ebar exactly for " <> statName[st] <> " (uses C gamma^a C = -(gamma^a)^T, Omega^T C = -C Omega, U' real): the adjoint equation is the Dirac conjugate of the field equation"]], {st, stats}];

(* explicit Dirac operator *)
Do[With[{P = fld[st]["Psi"]},
  Module[{lhs, rhs},
    lhs = rftDirac[st, rftGeo0, P];
    rhs = vAdd[st, Fold[vAdd[st, #1, #2] &, Table[matVec[st, g[[a]]/f[[a]], vD[st, P, X[[a]]]], {a, 8}]], matVec[st, 3 H g[[8]], P]];
    addCheck["Dirac_operator_explicit_" <> st, And @@ Table[sZeroQ[st, sAdd[st, {lhs[[A]], sScal[st, -1, rhs[[A]]]}]], {A, 16}],
      "gamma^mu D_mu Psi = E^-a4 Sin[z]^(-1/6) (gamma^(x1) d1 + gamma^(x2) d2 + gamma^(x3) d3) Psi + gamma^(x4) d4 Psi + E^a4 Sin[z]^(-1/6) (gamma^(x5) d5 + gamma^(x6) d6 + gamma^(x7) d7) Psi + Tan[z] gamma^(x8) d8 Psi + 3 H gamma^(x8) Psi, for " <> statName[st]]]], {st, stats}];
addFormulaText["field_equation",
  "the Euler-Lagrange equation (both statistics), z = 6 H x8, V = m + U'(S)",
  "E^-a4[x4] Sin[z]^(-1/6) (g[x1] d1 + g[x2] d2 + g[x3] d3) Psi + g[x4] d4 Psi + E^a4[x4] Sin[z]^(-1/6) (g[x5] d5 + g[x6] d6 + g[x7] d7) Psi + Tan[z] g[x8] d8 Psi + 3 H g[x8] Psi = (m + U'(S)) Psi"];
addFormulaText["adjoint_equation",
  "the adjoint equation (both statistics); for this metric D_mu Psibar = d_mu Psibar - Psibar Omega_mu",
  "E^-a4 Sin[z]^(-1/6) (d1 Psibar g[x1] + d2 Psibar g[x2] + d3 Psibar g[x3]) + d4 Psibar g[x4] + E^a4 Sin[z]^(-1/6) (d5 Psibar g[x5] + d6 Psibar g[x6] + d7 Psibar g[x7]) + Tan[z] d8 Psibar g[x8] + 3 H Psibar g[x8] = -(m + U'(S)) Psibar"];
(* 16 explicit components with inert symbols *)
compStr = Table[Module[{terms = {}},
   Do[If[g[[a, A, B]] =!= 0, AppendTo[terms, g[[a, A, B]]/f[[a]] dd[rftCoordNames[[a]], Psi[B]]]], {a, 8}, {B, 16}];
   Do[If[g[[8, A, B]] =!= 0, AppendTo[terms, 3 H g[[8, A, B]] Psi[B]]], {B, 16}];
   wl[Total[terms] == V Psi[A]]], {A, 16}];
AppendTo[formulas, <|"key" -> "field_equation_components", "description" -> "the 16 component equations (gamma^mu D_mu Psi)_A = V Psi_A, A = 1..16 (rows of the fixture gammas), V = m + U'(S); dd[xa, Psi[B]] = d Psi_B / d xa", "wl" -> compStr|>];
blk[a_] := {g[[a]][[1 ;; 8, 9 ;; 16]], g[[a]][[9 ;; 16, 1 ;; 8]]};
addCheck["block_form",
  And @@ Table[g[[a]][[1 ;; 8, 1 ;; 8]] == ConstantArray[0, {8, 8}] && g[[a]][[9 ;; 16, 9 ;; 16]] == ConstantArray[0, {8, 8}], {a, 8}] &&
  rftChir == ArrayFlatten[{{-IdentityMatrix[8], 0}, {0, IdentityMatrix[8]}}],
  "every gamma^a = {{0, tb_a}, {t_a, 0}} is block off-diagonal in the chiral split Psi = (psi_-, psi_+) (Gamma = diag(-1, 1)): the field equation is the pair " <>
  "sum_a (1/f_a) tb_a d_a psi_+ + 3 H tb_8 psi_+ = V psi_- and sum_a (1/f_a) t_a d_a psi_- + 3 H t_8 psi_- = V psi_+ (blocks in field-theory.json)"];
AppendTo[formulas, <|"key" -> "field_equation_blocks",
  "description" -> "block form: Psi = (psi_minus (rows 1..8, Gamma = -1), psi_plus (rows 9..16, Gamma = +1)); gamma^(xa) = {{0, tb[xa]}, {t[xa], 0}}; equations sum_a (1/f_a) tb[xa] d_a psi_plus + 3 H tb[x8] psi_plus = V psi_minus and sum_a (1/f_a) t[xa] d_a psi_minus + 3 H t[x8] psi_minus = V psi_plus; listed {xa, tb, t}",
  "wl" -> Table[wl[{rftCoordNames[[a]], blk[a][[1]], blk[a][[2]]}], {a, 8}]|>];
(* evolution form *)
Do[With[{P = fld[st]["Psi"], Pc = fld[st]["Psic"]},
  Module[{S = Ldata[st]["S"], rest, d4},
    rest = vAdd[st, Fold[vAdd[st, #1, #2] &, Table[If[a == 4, Table[sZero[st], {16}], matVec[st, g[[a]]/f[[a]], vD[st, P, X[[a]]]]], {a, 8}]], matVec[st, 3 H g[[8]], P]];
    d4 = matVec[st, -g[[4]], vAdd[st, rftVPsi[st, S, P], vScal[st, -1, rest]]];
    addCheck["evolution_form_" <> st,
      g[[4]] . g[[4]] == -id16 &&
      And @@ Table[sZeroQ[st, sAdd[st, {matVec[st, g[[4]], vAdd[st, vD[st, P, x4], vScal[st, -1, d4]]][[A]], sScal[st, -1, Ldata[st]["E"][[A]]]}]], {A, 16}],
      "(gamma^(x4))^2 = -1, so the field equation is equivalent to the first-order evolution equation d4 Psi = -gamma^(x4) [(m + U'(S)) Psi - sum_(a != 4) (1/f_a) gamma^(a) d_a Psi - 3 H gamma^(x8) Psi] " <>
      "(exact: gamma^(x4) (d4 Psi - RHS) = E): the slices x4 = const are non-characteristic (g^44 = -1 != 0), " <> statName[st]]]], {st, stats}];

(* ================================================================== 5. non-triviality *)
section["non-triviality"];
Do[With[{P = fld[st]["Psi"], Pc = fld[st]["Psic"]},
  Module[{geoNoOm, Enoom, diff},
    geoNoOm = <|"sqrtg" -> sg, "gup" -> gup, "Om" -> Table[z16, {8}]|>;
    Enoom = rftE[st, geoNoOm, P, Pc];
    diff = vAdd[st, Ldata[st]["E"], vScal[st, -1, Enoom], vScal[st, -1, matVec[st, 3 H g[[8]], P]]];
    addCheck["nontriviality_" <> If[st === "G", "1_dirac16complex", "2_dirac16complex00"],
      (And @@ Table[sZeroQ[st, diff[[A]]], {A, 16}]) && !(And @@ Table[sZeroQ[st, matVec[st, 3 H g[[8]], P][[A]]], {A, 16}]) &&
      !rftZeroQ[1/f[[1]] - 1] && !rftZeroQ[1/f[[5]] - 1] && !rftZeroQ[1/f[[8]] - 1],
      "NON-TRIVIALITY [" <> If[st === "G", "1", "2"] <> "] for " <> statName[st] <> ": the spin-connection part of the Euler-Lagrange equation is exactly " <>
      "(gamma^mu D_mu - gamma^mu d_mu) Psi = gamma^mu Omega_mu Psi = 3 H gamma^(x8) Psi, nonzero for every H > 0 and every a4 (a4 constant included) and every Psi != 0 " <>
      "(gamma^(x8) is invertible); in addition the vielbein enters every derivative term, gamma^mu d_mu = E^-a4 Sin[z]^(-1/6) gamma^(xi) d_i + gamma^(x4) d4 + E^a4 Sin[z]^(-1/6) gamma^(xt) d_t + Tan[z] gamma^(x8) d8 " <>
      "(none of the factors is identically 1). The a4'-terms of the spin connection cancel between the 3 inflating and the 3 deflating directions (check gammaOmega_x4_terms_cancel); " <>
      "a4 enters through the vielbein factors E^-+a4 of the 3-space and extra-time derivatives. All gravitational terms vanish together only if Omega_mu = 0 for all mu, " <>
      "which by spin_curvature_equals_Riemann requires a flat metric; R^(x8)_(x8) = -6 H^2 shows the metric is never flat for H > 0 (H = 0 itself is a degenerate limit, check degenerate_at_H_0)"]]], {st, stats}];
addCheck["Omega_vanishes_iff_a4prime_and_H_vanish",
  And @@ Table[Module[{v = e[[4]], fac}, fac = If[FreeQ[v, a4p], v/H, v/a4p];
     FreeQ[fac, a4p] && FreeQ[fac /. rftZ -> zz, H] && (rftZeroQ[fac^12 - E^(12 a4[x4]) Sin[rftZ]^2] || rftZeroQ[fac^12 - E^(-12 a4[x4]) Sin[rftZ]^2])], {e, omExpected}],
  "each of the 12 nonzero omega_mu,ab is either a4' or H times a factor +-E^(+-a4) Sin[z]^(1/6) that never vanishes on 0 < z < Pi/2: " <>
  "the a4'-part of Omega_mu vanishes iff a4 is constant and its H-part iff H = 0; for H > 0 the spin connection never vanishes"];

(* ================================================================== 6. self-consistency: current, integrability *)
section["current and integrability"];
Do[With[{P = fld[st]["Psi"], Pc = fld[st]["Psic"]},
  Module[{J, divJ, rhs, Eb = Ldata[st]["Ebar"], E1 = Ldata[st]["E"]},
    J = Table[sScal[st, -I, sDot[st, Pc, matVec[st, Cm . gup[[mu]], P]]], {mu, 8}];
    divJ = sAdd[st, Table[sD[st, sScal[st, sg, J[[mu]]], X[[mu]]], {mu, 8}]];
    rhs = sScal[st, -I sg, sAdd[st, {sDot[st, Eb, P], sDot[st, rftPsibar[st, Pc], E1]}]];
    addCheck["current_real_" <> st, And @@ Table[sZeroQ[st, If[st === "G", gAdd[{gConj[J[[mu]]], gScal[-1, J[[mu]]]}], sConj[st, J[[mu]]] - J[[mu]]]], {mu, 8}],
      "J^mu = -i Psibar gamma^mu Psi is real (Hermitian) for " <> statName[st] <> " (-i C gamma^a is Hermitian)"];
    addCheck["current_conservation_identity_" <> st, sZeroQ[st, sAdd[st, {divJ, sScal[st, -1, rhs]}]],
      "d_mu (sqrt g J^mu) = -i sqrt g (Ebar Psi + Psibar E) exactly (off shell), so nabla_mu J^mu = 0 on shell, for " <> statName[st]];
    addCheck["charge_density_is_Krein_form_" <> st, sZeroQ[st, sAdd[st, {J[[4]], sScal[st, -1, sDot[st, Pc, matVec[st, Bm, P]]]}]],
      "J^(x4) = Psi^dagger B Psi with B = -i C gamma^(x4) (Hermitian, signature (8,8)): the conserved charge Q = integral of Cos[z] Psi^dagger B Psi d^7x is an indefinite form, " <> statName[st]]]], {st, stats}];
addFormulaText["current", "conserved current and its identity (both statistics)",
  "J^mu = -i Psibar gamma^mu Psi; d_mu (Cos[z] J^mu) = -i Cos[z] (Ebar Psi + Psibar E); J^x4 = Psi^dagger B Psi; Q = Integral Cos[z] Psi^dagger B Psi dx1 dx2 dx3 dx5 dx6 dx7 dx8"];
(* Lichnerowicz *)
Do[With[{P = fld[st]["Psi"]},
  Module[{Dop, DD, box, lhs, res, cc},
    Dop[w_] := Fold[vAdd[st, #1, #2] &, Table[matVec[st, gup[[mu]], vAdd[st, vD[st, w, X[[mu]]], matVec[st, Om[[mu]], w]]], {mu, 8}]];
    DD = Table[vAdd[st, vD[st, P, X[[nu]]], matVec[st, Om[[nu]], P]], {nu, 8}];
    box = Fold[vAdd[st, #1, #2] &, Table[vScal[st, rftGinv0[[mu, mu]],
       vAdd[st, vD[st, DD[[mu]], X[[mu]]], matVec[st, Om[[mu]], DD[[mu]]], vScal[st, -1, Fold[vAdd[st, #1, #2] &, Table[vScal[st, Gm[[l, mu, mu]], DD[[l]]], {l, 8}]]]]], {mu, 8}]];
    lhs = Dop[Dop[P]];
    res = vAdd[st, lhs, vScal[st, -1, box], vScal[st, 1/4 Rs, P]];
    addCheck["Lichnerowicz_identity_" <> st, And @@ Table[sZeroQ[st, res[[A]]], {A, 16}],
      "(gamma^mu D_mu)^2 Psi = g^mu,nu (D_mu D_nu Psi - Gamma^l_mu,nu D_l Psi) - (R/4) Psi with R = 6 (a4'^2 - 7 H^2), for a general " <> statName[st] <>
      " (exact): the second-order consequence of the field equations is consistent with the curvature (integrability)"]]], {st, stats}];
addFormulaText["Lichnerowicz", "second-order identity (both statistics)",
  "(gamma^mu D_mu)^2 Psi = g^mu,nu (D_mu D_nu - Gamma^l_mu,nu D_l) Psi - (R/4) Psi, R = 6 (a4'[x4]^2 - 7 H^2)"];

(* ================================================================== 7. negative control: Majorana-type Lg *)
section["Majorana-type Lg"];
Module[{PsiR, Lg, cur, divc, okEL = True, PhiR, LgC, okC = True, ELC, mass},
  PsiR = Table[gAdd[Table[<|{k} -> phr[A, k] @@ X|>, {k, rftGN}]], {A, 16}];
  Lg = gScal[sg, gAdd[Table[sDot["G", PsiR, matVec["G", Cm . gup[[mu]], vAdd["G", vD["G", PsiR, X[[mu]]], matVec["G", Om[[mu]], PsiR]]]], {mu, 8}]]];
  cur = Table[gScal[sg/2, sDot["G", PsiR, matVec["G", Cm . gup[[mu]], PsiR]]], {mu, 8}];
  divc = gAdd[Table[gD[cur[[mu]], X[[mu]]], {mu, 8}]];
  Do[okEL = okEL && gZeroQ[rftVarDer["G", Lg, phr[A, k]]], {A, 16}, {k, rftGN}];
  mass = sDot["G", PsiR, matVec["G", Cm, PsiR]];
  addCheck["Majorana_Lg_total_derivative_grassmann",
    gZeroQ[gAdd[{Lg, gScal[-1, divc]}]] && !gZeroQ[Lg] && okEL && mass == <||>,
    "for REAL anticommuting components Psi_A = sum_k phr[A,k](x) theta_k (explicit Grassmann algebra, N = 2): sqrt g Psi^T C gamma^mu D_mu Psi = d_mu ((1/2) sqrt g Psi^T C gamma^mu Psi) exactly; " <>
    "it is not zero, but it is a total derivative: all 32 Euler-Lagrange expressions vanish identically (no field equation). Also Psi^T C Psi = 0 (C symmetric). " <>
    "This is why the notebook's Majorana-type Lg[] cannot serve and the Dirac-type L with Psibar = Psi^dagger C is used"];
  PhiR = Table[phr[A] @@ X, {A, 16}];
  LgC = sg Sum[PhiR . Cm . gup[[mu]] . (D[PhiR, X[[mu]]] + Om[[mu]] . PhiR), {mu, 8}];
  Do[ELC = rftVarDerExpr[LgC, phr[A]];
     okC = okC && rftZeroQ[ELC - 2 sg (Cm . Sum[gup[[mu]] . (D[PhiR, X[[mu]]] + Om[[mu]] . PhiR), {mu, 8}])[[A]]], {A, 16}];
  addCheck["Majorana_Lg_commuting_control",
    okC && rftZeroQ[Table[PhiR . Cm . gup[[mu]] . PhiR, {mu, 8}]],
    "control: for REAL COMMUTING components the same Lg gives the nontrivial Euler-Lagrange expression 2 sqrt g (C gamma^mu D_mu Phi)_A (a massless equation) while Phi^T C gamma^mu Phi = 0 identically: " <>
    "Lg is a total derivative exactly for anticommuting real components"]];

(* ================================================================== 8. energy-momentum tensor *)
section["energy-momentum tensor by vielbein variation"];
bilM[st_, Pc_, M_, P_] := sDot[st, Pc, matVec[st, Cm . M, P]];
Tdata = <||>;
Do[Module[{P = fld[st]["Psi"], Pc = fld[st]["Psic"], L0 = Ldata[st]["L0"], pb, Bmat, canon, Sig, Aten, divA, Tvar, Tsym, okF = True, okSym = True, tt},
  tt = AbsoluteTime[];
  pb = rftPsibar[st, Pc];
  Bmat = Table[sAdd[st, {sDot[st, vecMat[st, pb, gup[[r]]], rftDPsi[st, rftGeo0, P, s]], sScal[st, -1, sDot[st, vecMat[st, rftDPsibar[st, rftGeo0, Pc, s], gup[[r]]], P]]}], {r, 8}, {s, 8}];
  Sig[n_, r_] := (1/4) (gup[[n]] . gup[[r]] - gup[[r]] . gup[[n]]);
  Aten = Table[If[Length[Union[{l, n, r}]] < 3, sZero[st], bilM[st, Pc, gup[[l]] . Sig[n, r] + Sig[n, r] . gup[[l]], P]], {l, 8}, {n, 8}, {r, 8}];
  divA = Table[sScal[st, 1/sg, sAdd[st, Table[sD[st, sScal[st, sg, Aten[[l, n, r]]], X[[l]]], {l, 8}]]], {n, 8}, {r, 8}];
  canon[n_, mu_] := sAdd[st, {If[n == mu, L0, sZero[st]], sScal[st, -1/2, Bmat[[n, mu]]]}];
  (* closed-form variation result: canon - (1/4) g_mu,rho nabla_l A^(l n rho) (diagonal metric: rho = mu) *)
  Tvar = Table[sScal[st, f[[mu]], rftTvar[st, mu, n, P, Pc, L0]], {n, 8}, {mu, 8}];   (* T^n_mu = T^n_b e^b_mu, b = mu *)
  Print["   ", st, " vielbein variations: ", Round[AbsoluteTime[] - tt, 0.1], " s"];
  Do[okF = okF && sZeroQ[st, sAdd[st, {Tvar[[n, mu]], sScal[st, -1, canon[n, mu]], sScal[st, rftG0[[mu, mu]]/4, divA[[n, mu]]]}]], {n, 8}, {mu, 8}];
  Tsym = Table[sAdd[st, {If[n == mu, L0, sZero[st]], sScal[st, -1/4, Bmat[[n, mu]]], sScal[st, -1/4 rftG0[[mu, mu]] rftGinv0[[n, n]], Bmat[[mu, n]]]}], {n, 8}, {mu, 8}];
  (* symmetric part of T_var (indices up: T^(n r) = T^n_mu g^(mu r)) equals T_sym *)
  Do[okSym = okSym && sZeroQ[st, sAdd[st, {sScal[st, rftGinv0[[r, r]], Tvar[[n, r]]], sScal[st, rftGinv0[[n, n]], Tvar[[r, n]]], sScal[st, -2 rftGinv0[[r, r]], Tsym[[n, r]]]}]], {n, 8}, {r, n, 8}];
  Tdata[st] = <|"Tvar" -> Tvar, "Tsym" -> Tsym, "Bmat" -> Bmat, "divA" -> divA|>;
  addCheck["T_vielbein_variation_closed_form_" <> st, okF,
    "for all 64 components (" <> statName[st] <> "), T^nu_mu := e^b_mu (1/sqrt g) delta S / delta e^b_nu (exact first-order variation of sqrt g, gamma^mu and the spin connection, functional derivative in h(x)) equals " <>
    "delta^nu_mu L0 - (1/2)(Psibar gamma^nu D_mu Psi - D_mu Psibar gamma^nu Psi) - (1/4) g_mu,rho nabla_l (Psibar {gamma^l, Sigma^(nu rho)} Psi), Sigma^(nu rho) = (1/4)[gamma^nu, gamma^rho], L0 = L/sqrt g; " <>
    "the last term (totally antisymmetric spin density) comes from the variation of the spin connection"];
  addCheck["T_symmetric_part_Belinfante_" <> st, okSym,
    "the symmetric part of the variation tensor, (T^(nu rho) + T^(rho nu))/2, equals T_sym^(nu rho) = g^(nu rho) L0 - (1/4)(Psibar gamma^nu D^rho Psi + Psibar gamma^rho D^nu Psi - D^rho Psibar gamma^nu Psi - D^nu Psibar gamma^rho Psi) for all 36 pairs (" <> statName[st] <> ")"]],
  {st, stats}];
addFormulaText["T_variation", "energy-momentum tensor from the vielbein variation (both statistics), T^nu_mu = e^b_mu (1/sqrt g) dS/de^b_nu, L0 = L/sqrt g",
  "T^nu_mu = delta^nu_mu L0 - (1/2) (Psibar gamma^nu D_mu Psi - D_mu Psibar gamma^nu Psi) - (1/4) g_mu,rho nabla_l (Psibar {gamma^l, Sigma^(nu rho)} Psi), Sigma^(nu rho) = (1/4) [gamma^nu, gamma^rho]"];
addFormulaText["T_symmetric", "symmetric (Belinfante) energy-momentum tensor = symmetric part of the variation tensor = the variation tensor on shell",
  "T^nu_mu = delta^nu_mu L0 - (1/4) (Psibar gamma^nu D_mu Psi - D_mu Psibar gamma^nu Psi + Psibar gamma_mu D^nu Psi - D^nu Psibar gamma_mu Psi)"];

section["Noether identities"];
Do[Module[{P = fld[st]["Psi"], Pc = fld[st]["Psic"], Tvar = Tdata[st]["Tvar"], heads, ELterm, okD = True, okL = True, Tb, lhs, el},
  (* Tb[nu, b] = T^nu_b = T^nu_mu e_b^mu (b = mu) *)
  Tb[n_, b_] := sScal[st, 1/f[[b]], Tvar[[n, b]]];
  If[st === "C",
    ELterm[lamb_] := sAdd[st, Join[Table[ELp[{st, A}] D[ph[A] @@ X, X[[lamb]]], {A, 16}], Table[ELc[{st, A}] D[phc[A] @@ X, X[[lamb]]], {A, 16}]]],
    ELterm[lamb_] := gAdd[Flatten[Table[{gScal[D[ph[A, k] @@ X, X[[lamb]]], ELp[{st, A, k}]], gScal[D[phc[A, k] @@ X, X[[lamb]]], ELc[{st, A, k}]]}, {A, 16}, {k, rftGN}]]]];
  Do[lhs = sAdd[st, {
      sAdd[st, Table[sD[st, sScal[st, sg, Tvar[[mu, lamb]]], X[[mu]]], {mu, 8}]],
      sScal[st, -sg, sAdd[st, Table[sScal[st, D[f[[mu]], X[[lamb]]], Tb[mu, mu]], {mu, 8}]]],
      sScal[st, -1, ELterm[lamb]]}];
    okD = okD && sZeroQ[st, lhs], {lamb, 8}];
  addCheck["Noether_identity_diffeomorphisms_" <> st, okD,
    "for each lambda = x1..x8 (" <> statName[st] <> ", general fields, off shell): d_mu (sqrt g T^mu_lambda) - sqrt g T^mu_a d_lambda e^a_mu = sum over all component functions phi of EL_phi d_lambda phi " <>
    "(EL_phi = the Euler-Lagrange expression of phi); this is the identity of the invariance of the action under coordinate changes"];
  (* local Lorentz: lambda_ab = 1 = -lambda_ba *)
  Do[Module[{dP, dPc, t1, elL},
      dP = rftS[[a, b]]; dPc = rftS[[a, b]];
      t1 = sScal[st, sg, sAdd[st, {sScal[st, eta[[a, a]] f[[b]], Tb[b, a]], sScal[st, -eta[[b, b]] f[[a]], Tb[a, b]]}]];
      elL = If[st === "C",
        Total[Table[ELp[{st, A}] (dP . (ph[#] @@ X & /@ Range[16]))[[A]] + ELc[{st, A}] (dPc . (phc[#] @@ X & /@ Range[16]))[[A]], {A, 16}]],
        gAdd[Flatten[Table[{gScal[(dP . Table[ph[B, k] @@ X, {B, 16}])[[A]], ELp[{st, A, k}]], gScal[(dPc . Table[phc[B, k] @@ X, {B, 16}])[[A]], ELc[{st, A, k}]]}, {A, 16}, {k, rftGN}]]]];
      okL = okL && sZeroQ[st, sAdd[st, {t1, elL}]]], {a, 8}, {b, a + 1, 8}];
  addCheck["Noether_identity_local_Lorentz_" <> st, okL,
    "for all 28 frame rotations lambda_ab = -lambda_ba (" <> statName[st] <> ", off shell): sqrt g T^mu_a lambda^a_c e^c_mu + sum_phi EL_phi delta phi = 0 with delta e^a_mu = lambda^a_c e^c_mu, delta Psi = +(1/2) lambda_ab S^ab Psi, delta Psibar = -(1/2) lambda_ab Psibar S^ab (the spinor rotation that keeps Psibar gamma^mu Psi invariant): " <>
    "the antisymmetric part T^[ab] is a combination of the Euler-Lagrange expressions, so T^mu_nu is symmetric on shell and equals T_sym"]], {st, stats}];
addCheck["conservation_on_shell_general",
  And @@ Table[Lookup[First[Select[checks, #["name"] == n &], <|"verdict" -> "FAIL"|>], "verdict"] == "PASS",
    {n, Flatten[Table[{"Noether_identity_diffeomorphisms_" <> st, "Noether_identity_local_Lorentz_" <> st, "T_symmetric_part_Belinfante_" <> st}, {st, stats}]]}],
  "consequence for both statistics: on shell (all EL_phi = 0) T^mu_nu = T_sym^mu_nu is symmetric and d_mu(sqrt g T^mu_lambda) - sqrt g T^mu_a d_lambda e^a_mu = 0, " <>
  "which for symmetric T is sqrt g nabla_mu T^mu_lambda = 0 (Gamma^r_mu,lambda T^mu_r = (1/2) d_lambda g_mu,r T^mu r = T^mu_a d_lambda e^a_mu): exact conservation for general solutions"];

section["EMT components"];
Do[Module[{P = fld[st]["Psi"], Pc = fld[st]["Psic"], L0 = Ldata[st]["L0"], Tsym = Tdata[st]["Tsym"], Bmat = Tdata[st]["Bmat"], K, okDiag = True, S = Ldata[st]["S"], E1 = Ldata[st]["E"], Eb = Ldata[st]["Ebar"], okK},
  K[mu_] := sScal[st, 1/(2 f[[mu]]), sAdd[st, {bilM[st, Pc, g[[mu]], vD[st, P, X[[mu]]]], sScal[st, -1, sDot[st, vecMat[st, vD[st, rftPsibar[st, Pc], X[[mu]]], g[[mu]]], P]]}]];
  Do[okDiag = okDiag && sZeroQ[st, sAdd[st, {Tsym[[mu, mu]], sScal[st, -1, L0], K[mu]}]] && sZeroQ[st, sAdd[st, {Tdata[st]["Tvar"][[mu, mu]], sScal[st, -1, Tsym[[mu, mu]]]}]], {mu, 8}];
  addCheck["T_diagonal_components_" <> st, okDiag,
    "T^mu_mu (no sum) = L0 - K_mu with K_mu = (1/(2 f_mu)) (Psibar gamma^(mu) d_mu Psi - d_mu Psibar gamma^(mu) Psi): no spin-connection term survives in the diagonal components " <>
    "(Psibar {gamma^mu, Omega_mu} Psi = 0); the variation tensor and T_sym agree on the diagonal (" <> statName[st] <> ")"];
  okK = sZeroQ[st, sAdd[st, {L0, sScal[st, -1, sAdd[st, Table[K[mu], {mu, 8}]]], sScal[st, m, S], rftPot[st, S]}]] &&
    sZeroQ[st, sAdd[st, {sAdd[st, Table[K[mu], {mu, 8}]], sScal[st, -1/2, sDot[st, rftPsibar[st, Pc], E1]], sScal[st, 1/2, sDot[st, Eb, P]],
      sScal[st, -1, If[st === "C", (m + U'[S]) S, gMul[sAdd[st, {gScalar[m + u1], gScal[lam, S]}], S]]]}]];
  addCheck["EMT_trace_" <> st,
    sZeroQ[st, sAdd[st, {sAdd[st, Table[Tsym[[mu, mu]], {mu, 8}]], sScal[st, -7, sAdd[st, Table[K[mu], {mu, 8}]]], sScal[st, 8 m, S], sScal[st, 8, rftPot[st, S]]}]],
    "trace T^mu_mu (sum) = 7 sum_mu K_mu - 8 (m S + U(S)) exactly (" <> statName[st] <> "); with kinetic_sum_on_shell it is -m S + 7 S U' - 8 U on shell"];
  addCheck["kinetic_sum_on_shell_" <> st, okK,
    "L0 = sum_mu K_mu - m S - U(S) and sum_mu K_mu = (m + U'(S)) S + (1/2)(Psibar E - Ebar Psi) exactly (" <> statName[st] <> "): on shell the total kinetic term is (m + U'(S)) S and L0 = S U'(S) - U(S)"]], {st, stats}];
addFormulaText["EMT_diagonal", "diagonal components (no sum), both statistics; K_mu = kinetic term of direction mu",
  "K_mu = (1/(2 f_mu)) (Psibar gamma^(mu) d_mu Psi - d_mu Psibar gamma^(mu) Psi); L0 = sum_mu K_mu - m S - U(S); T^mu_mu = L0 - K_mu; rho = -T^x4_x4 = -sum_(mu != x4) K_mu + m S + U; p3 = T^x1_x1 (= T^x2_x2 = T^x3_x3 for isotropic states) = sum_(mu != x1) K_mu - m S - U; p_t = T^x5_x5 = sum_(mu != x5) K_mu - m S - U; p8 = T^x8_x8 = sum_(mu != x8) K_mu - m S - U"];
addFormulaText["EMT_kinetic_potential", "split into kinetic (derivative) and potential parts",
  "T^nu_mu = T_kin^nu_mu + T_pot^nu_mu, T_pot^nu_mu = -delta^nu_mu (m S + U(S)), T_kin^nu_mu = delta^nu_mu sum_l K_l - (1/4)(Psibar gamma^nu D_mu Psi - D_mu Psibar gamma^nu Psi + Psibar gamma_mu D^nu Psi - D^nu Psibar gamma_mu Psi); potential energy density rho_pot = m S + U, potential pressure p_pot = -(m S + U) in every direction"];
addFormulaText["EMT_trace", "trace",
  "T^mu_mu (sum) = 8 L0 - sum_mu K_mu = 7 sum_mu K_mu - 8 (m S + U); on shell = 7 (m + U') S - 8 (m S + U) = -m S + 7 S U' - 8 U"];
addFormulaText["EMT_homogeneous_on_shell", "homogeneous states (Psi depends on x4 only): K_mu = 0 for mu != x4 and K_x4 = (m + U') S on shell",
  "rho = m S + U(S); p3 = p_t = p8 = S U'(S) - U(S); w = (S U' - U)/(m S + U); for U = (lam/2) S^2: rho = m S + lam S^2/2, p = lam S^2/2, w = lam S/(2 m + lam S)"];
addFormulaText["EMT_offdiagonal_x4_x8", "the x4-x8 component of the symmetric tensor (Omega_x4 = Omega_x8 = 0)",
  "T^x4_x8 = -(1/4) (B48 - Cot[z] B84), B48 = Psibar gamma^(x4) d8 Psi - d8 Psibar gamma^(x4) Psi, B84 = Psibar gamma^(x8) d4 Psi - d4 Psibar gamma^(x8) Psi; T^x8_x4 = -Tan[z]^2 T^x4_x8 (T_x4x8 = T_x8x4)"];
Do[Module[{Tsym = Tdata[st]["Tsym"], P = fld[st]["Psi"], Pc = fld[st]["Psic"], B48, B84, ok},
  B48 = sAdd[st, {bilM[st, Pc, g[[4]], vD[st, P, x8]], sScal[st, -1, sDot[st, vecMat[st, vD[st, rftPsibar[st, Pc], x8], g[[4]]], P]]}];
  B84 = sAdd[st, {bilM[st, Pc, g[[8]], vD[st, P, x4]], sScal[st, -1, sDot[st, vecMat[st, vD[st, rftPsibar[st, Pc], x4], g[[8]]], P]]}];
  ok = sZeroQ[st, sAdd[st, {Tsym[[4, 8]], sScal[st, 1/4, B48], sScal[st, -Cot[rftZ]/4, B84]}]] &&
       sZeroQ[st, sAdd[st, {Tsym[[8, 4]], sScal[st, Tan[rftZ]^2, Tsym[[4, 8]]]}]];
  addCheck["T_x4_x8_component_" <> st, ok,
    "T^x4_x8 = -(1/4)(B48 - Cot[z] B84), B48 = Psibar gamma^(x4) d8 Psi - d8 Psibar gamma^(x4) Psi, B84 = Psibar gamma^(x8) d4 Psi - d4 Psibar gamma^(x8) Psi, and T^x8_x4 = g^88 g_44 T^x4_x8 = -Tan[z]^2 T^x4_x8 (" <> statName[st] <> ")"]], {st, stats}];
(* energy exchange: nabla_mu T^mu_x4 for a diagonal T depending on x4 only *)
Module[{rhoF, p3F, ptF, p8F, Tdiag, div4},
  Tdiag = DiagonalMatrix[{p3F[x4], p3F[x4], p3F[x4], -rhoF[x4], ptF[x4], ptF[x4], ptF[x4], p8F[x4]}];
  div4 = Sum[D[sg Tdiag[[mu, 4]], X[[mu]]], {mu, 8}]/sg - Sum[Gm[[r, mu, 4]] Tdiag[[mu, r]], {mu, 8}, {r, 8}];
  addCheck["energy_exchange_equation",
    rftZeroQ[div4 - (-rhoF'[x4] - 3 a4p (p3F[x4] - ptF[x4]))],
    "for a diagonal homogeneous T^mu_nu = diag(p3, p3, p3, -rho, p_t, p_t, p_t, p8) depending on x4 only: nabla_mu T^mu_x4 = -rho' - 3 a4' (p3 - p_t); " <>
    "conservation gives d rho/d x4 = -3 a4' (p3 - p_t): energy flows between 3-space and the extra times unless p3 = p_t (sqrt g does not depend on x4)"];
  addFormulaText["energy_exchange", "conservation for a homogeneous diagonal T = diag(p3, p3, p3, -rho, p_t, p_t, p_t, p8)(x4)",
    "nabla_mu T^mu_x4 = -rho'[x4] - 3 a4'[x4] (p3 - p_t) = 0, i.e. d rho/d x4 = -3 a4'[x4] (p3 - p_t)"]];

(* ================================================================== 9. exact solutions *)
section["exact solutions and conservation"];
(* chi' = M chi, M = -m g4 + mu g4.g8, M^2 = (mu^2 - m^2) I; P = Cosh[k x4] + Sinh[k x4]/k M *)
Mmat[mm_, mu_] := -mm g[[4]] + mu g[[4]] . g[[8]];
Pmat[mm_, mu_, kk_] := Cosh[kk x4] id16 + Sinh[kk x4]/kk Mmat[mm, mu];
addCheck["solution_matrix_square",
  Mmat[mm, mu] . Mmat[mm, mu] == (mu^2 - mm^2) id16 && And @@ Table[Transpose[Mmat[mm, mu]] . Cm + Cm . Mmat[mm, mu] == z16, {1}],
  "M = -m gamma^(x4) + mu gamma^(x4) gamma^(x8) satisfies M^2 = (mu^2 - m^2) I16 and M^T C + C M = 0, so exp(M x4) = Cosh[k x4] I + (Sinh[k x4]/k) M with k^2 = mu^2 - m^2 and every bilinear chi^dagger C exp(M x4)... is constant"];
(* exact zero test with the relations Cosh^2 = 1 + Sinh^2 (argument kk x4) and kk^2 = k2 (k2 free of the constants cA, cAc),
   applied coefficient by coefficient of the polynomial in the constants cA[..], cAc[..] *)
zeroQK[e_, kk_, k2_] := Module[{t, vars, coefs, red},
  t = Expand[PowerExpand[e /. rftTrigRules] /. {Cosh[kk x4] -> chv, Sinh[kk x4] -> shv}];
  If[t === 0, Return[True]];
  vars = Union[Cases[t, (cA | cAc)[__], {0, Infinity}]];
  coefs = If[vars === {}, {t}, Last /@ CoefficientRules[t, vars]];
  red[c_] := Module[{u = Expand[Numerator[Together[c]]]},
    u = rftReduceCos[u];
    u = Expand[u /. chv^n_Integer /; n >= 2 :> (1 + shv^2)^Quotient[n, 2] chv^Mod[n, 2]];
    u = Expand[u /. kk^n_Integer /; n >= 2 :> k2^Quotient[n, 2] kk^Mod[n, 2]];
    u = Expand[u /. chv^n_Integer /; n >= 2 :> (1 + shv^2)^Quotient[n, 2] chv^Mod[n, 2]];
    rftReduceCos[u]];
  And @@ (red[#] === 0 & /@ coefs)];
gZeroQK[a_Association, kk_, k2_] := And @@ (zeroQK[#, kk, k2] & /@ Values[a]);
sZeroQK["C", e_, kk_, k2_] := zeroQK[e, kk, k2]; sZeroQK["G", e_, kk_, k2_] := gZeroQK[e, kk, k2];
(* T_sym, divergence and field equation for a given explicit field *)
TsymOf[st_, P_, Pc_] := Module[{pb = rftPsibar[st, Pc], L0, Bm2},
  L0 = rftL0[st, rftGeo0, P, Pc];
  Bm2 = Table[sAdd[st, {sDot[st, vecMat[st, pb, gup[[r]]], rftDPsi[st, rftGeo0, P, s]], sScal[st, -1, sDot[st, vecMat[st, rftDPsibar[st, rftGeo0, Pc, s], gup[[r]]], P]]}], {r, 8}, {s, 8}];
  Table[sAdd[st, {If[n == mu, L0, sZero[st]], sScal[st, -1/4, Bm2[[n, mu]]], sScal[st, -1/4 rftG0[[mu, mu]] rftGinv0[[n, n]], Bm2[[mu, n]]]}], {n, 8}, {mu, 8}]];
divT[st_, T_] := Table[sAdd[st, {
    sScal[st, 1/sg, sAdd[st, Table[sD[st, sScal[st, sg, T[[mu, nu]]], X[[mu]]], {mu, 8}]]],
    sScal[st, -1, sAdd[st, Flatten[Table[If[Gm[[r, mu, nu]] === 0, sZero[st], sScal[st, Gm[[r, mu, nu]], T[[mu, r]]]], {mu, 8}, {r, 8}]]]]}], {nu, 8}];
Block[{U = Function[s, lam s^2/2], u1 = 0},
  (* (i) linear, x4 and x8 dependent: Psi = Sin[z]^al P(m, mu, k) chi, mu = 3 H (2 al + 1), lam = 0 *)
  Do[Module[{muv = 3 H (2 al + 1), Psol, Pcsol, Eres, T, dv, k2, J, divJ, okE, okT, okJ},
    k2 = muv^2 - mm^2;
    Block[{lam = 0, m = mm},
      If[st === "C",
        Psol = Sin[rftZ]^al Pmat[mm, muv, kk] . Table[cA[A], {A, 16}];
        Pcsol = Sin[rftZ]^al Pmat[mm, muv, kk] . Table[cAc[A], {A, 16}],
        Psol = Table[gAdd[Table[<|{k} -> (Sin[rftZ]^al Pmat[mm, muv, kk] . Table[cA[B, k], {B, 16}])[[A]]|>, {k, rftGN}]], {A, 16}];
        Pcsol = Table[gAdd[Table[<|{k + rftGN} -> (Sin[rftZ]^al Pmat[mm, muv, kk] . Table[cAc[B, k], {B, 16}])[[A]]|>, {k, rftGN}]], {A, 16}]];
      Eres = rftE[st, rftGeo0, Psol, Pcsol];
      okE = And @@ Table[sZeroQK[st, Eres[[A]], kk, k2], {A, 16}];
      T = TsymOf[st, Psol, Pcsol];
      dv = divT[st, T];
      okT = And @@ Table[sZeroQK[st, dv[[nu]], kk, k2], {nu, 8}];
      J = Table[sScal[st, -I, bilM[st, Pcsol, gup[[mu]], Psol]], {mu, 8}];
      divJ = sAdd[st, Table[sD[st, sScal[st, sg, J[[mu]]], X[[mu]]], {mu, 8}]];
      okJ = sZeroQK[st, divJ, kk, k2];
      addCheck["exact_solution_x4_x8_" <> st, okE && okT && okJ && !sZeroQK[st, T[[4, 4]], kk, k2],
        "exact solution (" <> statName[st] <> ", U = 0): Psi = Sin[z]^al (Cosh[k x4] + Sinh[k x4]/k M) chi with constant chi (16 free complex constants" <>
        If[st === "G", " per Grassmann generator", ""] <> "), M = -m gamma^(x4) + 3 H (2 al + 1) gamma^(x4) gamma^(x8), k^2 = 9 H^2 (2 al + 1)^2 - m^2, al arbitrary; " <>
        "it satisfies the field equation for every a4 (a test of the terms Tan[z] gamma^(x8) d8 and 3 H gamma^(x8)), and nabla_mu T_sym^mu_nu = 0 for all 8 nu and d_mu(sqrt g J^mu) = 0 hold exactly at it. " <>
        "Honest scope: at these solutions the pressures and the momentum density vanish (on shell L0 = 0 for U = 0, K_mu = 0 for mu != x4, T^x4_x8 = 0) and rho = -T^x4_x4 = m S is constant in x4, " <>
        "so the conservation test is weak; the general proof is the pair of Noether identities"]]],
    {st, stats}];
  (* (ii) nonlinear homogeneous: commuting Psi = P(m + lam S0, 3H) chi, S0 = chi^dagger C chi *)
  Module[{chi = Table[cA[A], {A, 16}], chic = Table[cAc[A], {A, 16}], S0, meff, Psol, Pcsol, Eres, T, dv, k2, okE, okT, rho, p, okRP, Sx},
    S0 = chic . Cm . chi; k2 = 9 H^2 - me^2;
    (* the effective mass me = m + lam S0 is the parameter: m = me - lam S0 *)
    Psol = Pmat[me, 3 H, kk] . chi; Pcsol = Pmat[me, 3 H, kk] . chic;
    Sx = rftSbil["C", Psol, Pcsol];
    Block[{m = me - lam S0},
    Eres = rftE["C", rftGeo0, Psol, Pcsol];
    okE = And @@ Table[zeroQK[Eres[[A]], kk, k2], {A, 16}] && zeroQK[Sx - S0, kk, k2];
    T = TsymOf["C", Psol, Pcsol]; dv = divT["C", T];
    okT = And @@ Table[zeroQK[dv[[nu]], kk, k2], {nu, 8}];
    okRP = zeroQK[-T[[4, 4]] - (m S0 + lam S0^2/2), kk, k2] && And @@ Table[zeroQK[T[[mu, mu]] - lam S0^2/2, kk, k2], {mu, {1, 2, 3, 5, 6, 7, 8}}]];
    addCheck["exact_solution_nonlinear_homogeneous_C", okE && okT && okRP,
      "exact nonlinear solution of dirac16complex00 with U = (lam/2) S^2: Phi = (Cosh[k x4] + Sinh[k x4]/k M) chi, M = -(m + lam S0) gamma^(x4) + 3 H gamma^(x4) gamma^(x8), S0 = chi^dagger C chi, k^2 = 9 H^2 - (m + lam S0)^2 (checked with the effective mass m + lam S0 as the parameter): " <>
      "S = S0 is constant, the field equation holds, nabla_mu T^mu_nu = 0 for all nu, and the diagonal components are T^x4_x4 = -rho, T^mu_mu = p (mu != x4) with rho = m S0 + lam S0^2/2 = m S + U, p = lam S0^2/2 = S U' - U exactly (homogeneous on-shell forms)"]];
  (* (iii) nonlinear homogeneous Grassmann: Psi = sum_k theta_k [P chi_k + lam S0 dP/dm chi_k] *)
  Module[{chik, chick, Pm, dPm, S0g, Psol, Pcsol, Eres, T, dv, k2 = 9 H^2 - m^2, okE, okT, okRP, S0x, Sx},
    chik = Table[Table[cA[B, k], {B, 16}], {k, rftGN}]; chick = Table[Table[cAc[B, k], {B, 16}], {k, rftGN}];
    Pm = Pmat[m, 3 H, kk];
    dPm = D[Pmat[mm, 3 H, kk], mm] /. mm -> m;
    dPm = dPm + (D[Pmat[m, 3 H, kq], kq] /. kq -> kk) (-m/kk);
    S0g = gAdd[Flatten[Table[gMul[<|{k1 + rftGN} -> 1|>, <|{k2i} -> chick[[k1]] . Cm . chik[[k2i]]|>], {k1, rftGN}, {k2i, rftGN}]]];
    Psol = Table[gAdd[Flatten[Table[{<|{k} -> (Pm . chik[[k]])[[A]]|>, gScal[lam, gMul[S0g, <|{k} -> (dPm . chik[[k]])[[A]]|>]]}, {k, rftGN}]]], {A, 16}];
    Pcsol = gConj /@ Psol;
    Sx = rftSbil["G", Psol, Pcsol];
    Eres = rftE["G", rftGeo0, Psol, Pcsol];
    okE = And @@ Table[gZeroQK[Eres[[A]], kk, k2], {A, 16}] && gZeroQK[gAdd[{Sx, gScal[-1, S0g]}], kk, k2] && !gZeroQK[gMul[S0g, S0g], kk, k2];
    T = TsymOf["G", Psol, Pcsol]; dv = divT["G", T];
    okT = And @@ Table[gZeroQK[dv[[nu]], kk, k2], {nu, 8}];
    okRP = gZeroQK[gAdd[{gScal[-1, T[[4, 4]]], gScal[-m, S0g], gScal[-lam/2, gMul[S0g, S0g]]}], kk, k2] &&
      And @@ Table[gZeroQK[gAdd[{T[[mu, mu]], gScal[-lam/2, gMul[S0g, S0g]]}], kk, k2], {mu, {1, 2, 3, 5, 6, 7, 8}}];
    addCheck["exact_solution_nonlinear_homogeneous_G", okE && okT && okRP,
      "exact nonlinear solution of dirac16complex (explicit Grassmann algebra, N = 2) with U = (lam/2) S^2: Psi = sum_k [exp(M_m x4) + lam S0 d/dm exp(M_m x4)] chi_k theta_k with S0 = sum_kl thetabar_k theta_l chi_k^dagger C chi_l " <>
      "(the expansion of exp(M_(m + lam S0) x4) terminates because S0^2 Psi = 0): S = S0 (even, nilpotent, S0^2 != 0), the field equation holds, nabla_mu T^mu_nu = 0, " <>
      "rho = m S0 + (lam/2) S0^2 and p3 = p_t = p8 = (lam/2) S0^2 as Grassmann-algebra elements (the classical Grassmann EMT; its numbers come from the quantum expectation values of section 6)"]];
];

(* ================================================================== 10. canonical quantisation (dirac16complex) *)
section["canonical quantisation"];
Module[{LG = Ldata["G"]["L"], P = fld["G"]["Psi"], Pc = fld["G"]["Psic"], okPi = True, K, piRow},
  piRow = vScal["G", sg/2, vecMat["G", Pc, Cm . g[[4]]]];
  Do[okPi = okPi && gZeroQ[gAdd[{rftPartialD["G", LG, ph[A, k], 4], gScal[-1, gMul[piRow[[A]], gTheta[k]]]}]], {A, 16}, {k, rftGN}];
  addCheck["canonical_momentum",
    okPi && Cm . g[[4]] == I Bm,
    "dL/d(d4 ph[A,k]) = pi_A theta_k with pi_A = (1/2) Cos[z] (Psi^dagger C gamma^(x4))_A = (i/2) Cos[z] (Psi^dagger B)_A (the momentum conjugate to Psi_A as a right derivative; C gamma^(x4) = i B): " <>
    "pi depends on Psi^dagger only, a second-class constraint as for Dirac's field"];
  K = sg Cm . g[[4]];
  addCheck["first_order_form_and_anticommutator",
    ConjugateTranspose[Cm . g[[4]]] == -Cm . g[[4]] && I Inverse[Cm . g[[4]]] == Bm && Bm . Bm == id16 && rftZeroQ[K - I sg Bm],
    "up to a total divergence L = Psi^dagger K d4 Psi - (terms without d4), K = Cos[z] C gamma^(x4) = i Cos[z] B (C gamma^(x4) anti-Hermitian with i (C gamma^(x4))^-1 = B; invertible since g^44 != 0); " <>
    "the canonical (Dirac-bracket) anticommutator is {Psi_A(x), Psi^dagger_C(y)} = i (K^-1)_AC delta^7(x - y) = B_AC delta^7(x - y)/sqrt|g| on a slice x4 = const (exact: i K^-1 = B/Cos[z])"]];
(* Heisenberg equation reproduces the field equation *)
Module[{Phi = rftField["C"], Phic = rftFieldC["C"], Hd, flow, d4sol, ok, S},
  S = Phic . Cm . Phi;
  Hd = sg (Phic . (m Cm) . Phi - Sum[If[a == 4, 0, Phic . Cm . gup[[a]] . (D[Phi, X[[a]]] + Om[[a]] . Phi)], {a, 8}] + U[S]);
  flow = Table[-I Sum[Bm[[A, Cc]] rftVarDerExpr[Hd, phc[Cc]]/sg, {Cc, 16}], {A, 16}];
  d4sol = -g[[4]] . ((m + U'[S]) Phi - Sum[If[a == 4, 0, gup[[a]] . (D[Phi, X[[a]]] + Om[[a]] . Phi)], {a, 8}]);
  ok = rftZeroQ[flow - d4sol] && rftZeroQ[Simplify[rftLagUnsym["C", rftGeo0, Phi, Phic] - (Phic . (sg Cm . g[[4]]) . D[Phi, x4] - Hd)]];
  addCheck["Heisenberg_equation_reproduces_field_equation", ok,
    "with the Hamiltonian density Hd = Cos[z] [Psi^dagger (m C - sum_(a != 4) C gamma^a D_a) Psi + U(S)] (so that the unsymmetrised L = Psi^dagger K d4 Psi - Hd exactly) and {Psi, Psi^dagger} = B delta^7/sqrt g, " <>
    "the Heisenberg equation d4 Psi = i[H, Psi] = -i B (1/sqrt g) dHd/dPsi^dagger equals -gamma^(x4) [(m + U'(S)) Psi - sum_(a != 4) gamma^a D_a Psi], the field equation solved for d4 Psi (exact, general U; " <>
    "the operator ordering of U'(S) Psi is that of the classical expression)"]];
Module[{ev = Eigenvalues[Bm], um, vneg},
  vneg = First[Select[NullSpace[Bm + id16], True &]];
  um = vneg/Sqrt[Conjugate[vneg] . vneg];
  addCheck["no_positive_inner_product",
    ConjugateTranspose[Bm] == Bm && Count[ev, 1] == 8 && Count[ev, -1] == 8 && Simplify[Conjugate[um] . Bm . um] == -1,
    "B is Hermitian with eigenvalues +1 (x8) and -1 (x8); for the exact unit vector u = " <> wl[um] <> " (B u = -u) the smeared operator X = sum_A u_A^* Psi_A(f) has {X, X^dagger} = (u^dagger B u) ||f||^2 = -||f||^2. " <>
    "If Psi^dagger were the adjoint in a space with positive inner product, {X, X^dagger} = X X^dagger + X^dagger X would be a positive operator (<phi|{X,X^dagger}|phi> = ||X^dagger phi||^2 + ||X phi||^2 >= 0): contradiction. " <>
    "Hence the canonical anticommutator in signature (4,4) forces an indefinite (Krein) inner product; the positive representation uses the Hilbert adjoint chi = Psi^dagger B with {Psi_A, chi_C} = (B B)_AC = delta_AC"]];
(* good sector, flat frozen coefficients *)
Module[{beta = -I g[[4]], al, hk, ks, kt, okH, okT},
  al[a_] := -g[[4]] . g[[a]];
  hk = mm beta + Sum[kv[a] al[a], {a, {1, 2, 3, 5, 6, 7, 8}}];
  okH = ConjugateTranspose[beta] == beta && And @@ Table[ConjugateTranspose[al[a]] == al[a], {a, {1, 2, 3, 8}}] &&
    And @@ Table[ConjugateTranspose[al[a]] == -al[a], {a, {5, 6, 7}}] &&
    And @@ Flatten[Table[al[a] . al[b] + al[b] . al[a] == 2 KroneckerDelta[a, b] (-eta[[4, 4]] eta[[a, a]]) id16, {a, {1, 2, 3, 5, 6, 7, 8}}, {b, {1, 2, 3, 5, 6, 7, 8}}]] &&
    And @@ Table[beta . al[a] + al[a] . beta == z16, {a, {1, 2, 3, 5, 6, 7, 8}}] && beta . beta == id16;
  addCheck["mode_hamiltonian_good_sector",
    okH && Expand[hk . hk - (mm^2 + kv[1]^2 + kv[2]^2 + kv[3]^2 + kv[8]^2 - kv[5]^2 - kv[6]^2 - kv[7]^2) id16] == z16 && Tr[hk] == 0,
    "frozen-coefficient (flat-frame) plane waves Psi = u exp(i k.x - i E x4): E u = h_k u with h_k = m beta + sum_a k_a alpha^a, beta = -i gamma^(x4), alpha^a = -gamma^(x4) gamma^a; " <>
    "beta and alpha^(x1,x2,x3,x8) are Hermitian, alpha^(x5,x6,x7) anti-Hermitian, {alpha^a, alpha^b} = 2 delta^ab (-eta^44 eta^aa), {alpha, beta} = 0, beta^2 = 1; h_k^2 = (m^2 + k1^2 + k2^2 + k3^2 + k8^2 - k5^2 - k6^2 - k7^2) I, Tr h_k = 0. " <>
    "In the GOOD SECTOR (k5 = k6 = k7 = 0, nothing depends on the extra times) h_k is Hermitian with real eigenvalues +-E (8 each); with extra-time momentum E^2 = m^2 + k_s^2 - k_t^2 is negative for k_t^2 > m^2 + k_s^2: those modes grow exponentially in x4"];
  addCheck["mode_hamiltonian_Krein_selfadjoint",
    Expand[Bm . hk - (ConjugateTranspose[hk] /. Conjugate[q_] :> q) . Bm] == z16 &&
    Bm . (mm Cm) == mm beta && And @@ Table[Bm . (-I Cm . g[[a]]) == al[a], {a, {1, 2, 3, 5, 6, 7, 8}}],
    "B h_k = h_k^dagger B for all real m, k (h_k^dagger taken with m, k real; the Krein norm u^dagger B u is conserved by every mode, also those that grow); the mode Hamiltonian density is Psi^dagger (m C - i C k_a gamma^a) Psi = chi h_k Psi with chi = Psi^dagger B (B m C = m beta, B (-i C gamma^a) = alpha^a)"]];
(* curved good sector: weighted Hermiticity, the role of 3 H gamma^(x8) *)
Module[{u = Table[ph[A] @@ X, {A, 16}], uc = Table[phc[A] @@ X, {A, 16}], v = Table[qv[A] @@ X, {A, 16}], hOp, hOpC, Mm, lhs, divs, rest, lhsNoH, lhsB, divsB},
  Mm[a_] := I g[[4]] . g[[a]];
  hOp[w_, withH_] := mm (-I g[[4]]) . w + Sum[If[a == 4, 0, (1/f[[a]]) Mm[a] . D[w, X[[a]]]], {a, 8}] + withH 3 H Mm[8] . w;
  hOpC[w_, withH_] := mm (I g[[4]]) . w + Sum[If[a == 4, 0, (1/f[[a]]) Conjugate[Mm[a]] . D[w, X[[a]]]], {a, 8}] + withH 3 H Conjugate[Mm[8]] . w;
  lhs = sg (uc . hOp[v, 1] - hOpC[uc, 1] . v);
  divs = Sum[D[sg/f[[a]] uc . Mm[a] . v, X[[a]]], {a, {1, 2, 3, 8}}];
  rest = Sum[sg/f[[a]] (uc . Mm[a] . D[v, X[[a]]] - D[uc, X[[a]]] . Mm[a] . v), {a, {5, 6, 7}}];
  lhsNoH = sg (uc . hOp[v, 0] - hOpC[uc, 0] . v);
  addCheck["good_sector_hermiticity_curved",
    rftZeroQ[lhs - divs - rest] && rftZeroQ[lhsNoH - divs - rest + 6 H Cos[rftZ] uc . Mm[8] . v] &&
    rftZeroQ[Cos[rftZ] (pf[x8] (Tan[rftZ] D[qf[x8], x8] + 3 H qf[x8]) + (Tan[rftZ] D[pf[x8], x8] + 3 H pf[x8]) qf[x8]) - D[Sin[rftZ] pf[x8] qf[x8], x8]],
    "the curved mode operator h = m (-i gamma^(x4)) + sum_(a != 4) (1/f_a) i gamma^(x4) gamma^(a) d_a + 3 i H gamma^(x4) gamma^(x8) (i d4 Psi = h Psi for U = 0) satisfies, for general u, v, " <>
    "Cos[z] (u^dagger h v - (h u)^dagger v) = sum_(a = 1,2,3,8) d_a (Cos[z]/f_a u^dagger M_a v) + sum_(t = 5,6,7) (Cos[z]/f_t)(u^dagger M_t d_t v - d_t u^dagger M_t v), M_a = i gamma^(x4) gamma^(a): " <>
    "in the GOOD SECTOR (no extra-time dependence) h is therefore symmetric for the measure Cos[z] d^7x up to the boundary terms Cos[z]/f_a u^dagger M_a v (formal Hermiticity; the x8 term Sin[z] u^dagger M_8 v does not vanish at the patch end z = Pi/2, so Hermiticity needs a boundary condition there, see Revision/theory/reports/wolfram-scope.json); without the spin-connection term 3 H gamma^(x8) a remainder -6 H Cos[z] u^dagger M_8 v survives " <>
    "(Cos[z] [p (Tan z d8 + 3H) q + ((Tan z d8 + 3H) p) q] = d8 (Sin[z] p q)): for the measure Cos[z] dx8 and the variables Psi the gravitational term is what makes the hidden-direction operator formally antisymmetric (in the variables Sin[z]^(1/2) Psi with the measure dy no such term is needed)"];
  lhsB = sg (uc . Bm . hOp[v, 1] - hOpC[uc, 1] . Bm . v);
  divsB = Sum[If[a == 4, 0, D[sg/f[[a]] uc . Bm . Mm[a] . v, X[[a]]]], {a, 8}];
  addCheck["Krein_form_conserved_curved",
    rftZeroQ[lhsB - divsB],
    "Cos[z] (u^dagger B h v - (h u)^dagger B v) = sum_(a != 4) d_a (Cos[z]/f_a u^dagger B M_a v) for general u, v (all seven slice directions): h is formally self-adjoint for the Krein form integral Cos[z] u^dagger B v d^7x in the whole theory, i.e. up to these boundary terms (they need boundary conditions, in particular at the patch end z = Pi/2)"]];
(* explicit Fock space in the good sector: m = 3, k1 = 4, E = 5 *)
Module[{beta = -I g[[4]], al1, h, E0 = 5, up, vn, gs, U16, W, apply, expect, vac, st1, std, okC, eH, Ms, okRule, Q, okQ, nb = 16, bitsOf},
  al1 = -g[[4]] . g[[1]];
  h = 3 beta + 4 al1;
  gs[vs_] := Module[{out = {}, w}, Do[w = v - Sum[(Conjugate[o] . v) o, {o, out}]; w = Simplify[w/Sqrt[Simplify[Conjugate[w] . w]]]; AppendTo[out, w], {v, vs}]; out];
  up = gs[NullSpace[h - E0 id16]]; vn = gs[NullSpace[h + E0 id16]];
  U16 = Transpose[Join[up, vn]];   (* columns u_0..u_7, v_0..v_7 *)
  okC = Simplify[U16 . ConjugateTranspose[U16]] == id16 && Length[up] == 8 && Length[vn] == 8;
  (* fermionic Fock space of 16 modes: mode p < 8 = b_p, mode 8 + s = d_s; a_p = b_p (p < 8), a_(8+s) = d_s^* *)
  annih[p_][state_Association] := Merge[KeyValueMap[Function[{s, c}, If[BitGet[s, p] == 1, <|s - 2^p -> (-1)^DigitCount[BitAnd[s, 2^p - 1], 2, 1] c|>, <||>]], state], Total];
  creat[p_][state_Association] := Merge[KeyValueMap[Function[{s, c}, If[BitGet[s, p] == 0, <|s + 2^p -> (-1)^DigitCount[BitAnd[s, 2^p - 1], 2, 1] c|>, <||>]], state], Total];
  aOp[p_] := If[p < 8, annih[p], creat[p]];
  aDag[p_] := If[p < 8, creat[p], annih[p]];
  inner[s1_Association, s2_Association] := Total[KeyValueMap[Function[{s, c}, Conjugate[c] Lookup[s2, s, 0]], s1]];
  expect[Wm_, state_] := Simplify[Sum[If[Wm[[p + 1, q + 1]] === 0, 0, Wm[[p + 1, q + 1]] inner[state, aDag[p][aOp[q][state]]]], {p, 0, 15}, {q, 0, 15}]];
  vac = <|0 -> 1|>; st1 = creat[0][vac]; std = creat[8][vac];
  W[M_] := Simplify[ConjugateTranspose[U16] . (Bm . M) . U16];   (* chi B M Psi = a^dagger (U^dagger B M U) a *)
  eH = W[Bm . h];   (* chi h Psi, i.e. M = B h *)
  Ms = {Cm, -I Cm . g[[4]], -I Cm . g[[1]], Cm . g[[2]] . g[[3]], Table[If[A <= Bv, Mod[3 A + 5 Bv, 7] - 3, Mod[3 Bv + 5 A, 7] - 3], {A, 16}, {Bv, 16}]};
  okRule = And @@ Table[Simplify[expect[W[M], st1] - expect[W[M], vac] - Conjugate[up[[1]]] . Bm . M . up[[1]]] == 0 &&
      Simplify[expect[W[M], std] - expect[W[M], vac] + Conjugate[vn[[1]]] . Bm . M . vn[[1]]] == 0, {M, Ms}];
  okQ = Simplify[expect[W[Bm], st1] - expect[W[Bm], vac]] == 1 && Simplify[expect[W[Bm], std] - expect[W[Bm], vac]] == -1;
  addCheck["Fock_space_good_sector_example",
    okC && Simplify[expect[eH, st1] - expect[eH, vac]] == E0 && Simplify[expect[eH, std] - expect[eH, vac]] == E0 && Simplify[expect[eH, vac]] == -8 E0 && okQ && okRule &&
    Simplify[inner[st1, st1]] == 1 && Simplify[inner[std, std]] == 1,
    "explicit fermionic Fock space (2^16 occupation states, positive inner product) for one good-sector momentum, m = 3, k = (4, 0, 0, 0) along x1, E = 5: " <>
    "Psi = sum_s (b_s u_s + d_s^* v_s) with exact orthonormal eigenvectors of h_k (completeness U U^dagger = I, so {Psi_A, chi_C} = delta_AC); " <>
    "the Hamiltonian chi h_k Psi has vacuum value -8 E (the filled sea), normal-ordered energy +E for the particle b_0^*|0> AND for the antiparticle d_0^*|0>; charge Psi^dagger B Psi = chi Psi gives +1 and -1; " <>
    "the expectation-value rule <u|:Psi^dagger M Psi:|u> = u^dagger B M u (particle) and -v^dagger B M v (antiparticle) holds exactly for M = C, -i C gamma^(x4), -i C gamma^(x1), C gamma^(x2) gamma^(x3) and a dense integer matrix"]];
addFormulaText["quantisation",
  "canonical quantisation of dirac16complex (SPEC section 6), x4 the evolution time",
  "pi_A = (i/2) Cos[z] (Psi^dagger B)_A; K = Cos[z] C gamma^(x4) = i Cos[z] B; {Psi_A(x), Psi^dagger_C(y)}_(x4 = y4) = B_AC delta^7(x - y)/Cos[z]; B = -i C gamma^(x4), B^dagger = B, B^2 = 1, signature (8,8); " <>
  "no positive inner product with Psi^dagger the adjoint (Krein space, fundamental symmetry B); positive representation chi = Psi^dagger B, {Psi_A, chi_C} = delta_AC; " <>
  "Heisenberg: d4 Psi = -i B (1/Cos[z]) dHd/dPsi^dagger = -gamma^(x4) [(m + U') Psi - sum_(a != 4) gamma^a D_a Psi]; good sector (no x5, x6, x7 dependence): h Hermitian for Cos[z] d^7x, positive Fock space, " <>
  "normal-ordered H = sum E (b^* b + d^* d) >= 0 per momentum; expectation-value rule <Psi^dagger M Psi> = u^dagger B M u (u^dagger u = 1, positive-energy good-sector u); EMT operator T^mu_nu = :T^mu_nu[Psi, Psi^dagger = chi B]: (normal ordered), <T> by the same rule; " <>
  "extra-time modes: E^2 = m^2 + k_s^2 - k_t^2 < 0 for k_t^2 > m^2 + k_s^2, growing as exp(|E| x4)"];

(* ================================================================== formulas: statements *)
addFormulaText["nontriviality",
  "NON-TRIVIALITY [1] (dirac16complex) and [2] (dirac16complex00): exact content of checks nontriviality_1_dirac16complex, nontriviality_2_dirac16complex00, gammaOmega_x4_terms_cancel, Omega_vanishes_iff_a4prime_and_H_vanish, never_flat_for_H_positive, spin_curvature_equals_Riemann",
  "gamma^mu D_mu Psi - gamma^mu d_mu Psi = gamma^mu Omega_mu Psi = 3 H gamma^(x8) Psi (nonzero for every H > 0, every a4, every Psi != 0); per direction gamma^(xi) Omega_xi = (a4'/2) gamma^(x4) + (H/2) gamma^(x8) (i = 1, 2, 3, inflating) and gamma^(xt) Omega_xt = -(a4'/2) gamma^(x4) + (H/2) gamma^(x8) (t = 5, 6, 7, deflating): the time-direction terms cancel (3 a4'/2 - 3 a4'/2 = 0), the hidden-direction terms add (6 H/2 = 3 H); " <>
  "Omega_mu = 0 for all mu iff a4' = 0 and H = 0 (H = 0 is a degenerate limit of the metric); [D_mu, D_nu] = (1/2) R_ab,mu,nu S^ab, and R^x8_x8 = -6 H^2 != 0: no frame removes Omega, the metric is never flat for H > 0"];
addFormulaText["majorana_negative_control",
  "the notebook's Majorana-type Lagrangian with real components (checks Majorana_Lg_total_derivative_grassmann, Majorana_Lg_commuting_control)",
  "anticommuting real Psi: sqrt g Psi^T C gamma^mu D_mu Psi = d_mu ((1/2) sqrt g Psi^T C gamma^mu Psi) (a total derivative; no field equation; Psi^T C Psi = 0); commuting real Phi: Euler-Lagrange expression 2 sqrt g C gamma^mu D_mu Phi and Phi^T C gamma^mu Phi = 0"];
addFormulaText["exact_solutions",
  "exact solutions used as test points (checks exact_solution_*)",
  "(i) U = 0: Psi = Sin[z]^al (Cosh[k x4] + Sinh[k x4]/k M) chi, M = -m g[x4] + 3 H (2 al + 1) g[x4].g[x8], k^2 = 9 H^2 (2 al + 1)^2 - m^2 (any a4); " <>
  "(ii) U = (lam/2) S^2, homogeneous: Psi = (Cosh[k x4] + Sinh[k x4]/k M) chi, M = -(m + lam S0) g[x4] + 3 H g[x4].g[x8], S0 = chi^dagger C chi, k^2 = 9 H^2 - (m + lam S0)^2 (commuting); " <>
  "Grassmann: Psi = sum_k [exp(M_m x4) + lam S0 d/dm exp(M_m x4)] chi_k theta_k, S0 = sum_kl thetabar_k theta_l chi_k^dagger C chi_l; at (ii): rho = m S0 + lam S0^2/2, p3 = p_t = p8 = lam S0^2/2"];
addFormulaText["equation_of_state_definitions", "pressures and equations of state from the diagonal components (SPEC section 4)",
  "rho = -T^x4_x4, p3 = T^x1_x1, p_t = T^x5_x5, p8 = T^x8_x8; w3 = p3/rho, w_t = p_t/rho, w8 = p8/rho; homogeneous on shell: w3 = w_t = w8 = (S U' - U)/(m S + U)"];
addFormulaText["hidden_direction_hermiticity", "role of the spin-connection term in the quantum theory (check good_sector_hermiticity_curved)",
  "Cos[z] [p (Tan[z] d8 + 3 H) q + ((Tan[z] d8 + 3 H) p) q] = d8 (Sin[z] p q): the operator Tan[z] d8 + 3 H is antisymmetric for the measure Cos[z] dx8 up to the boundary term Sin[z] p q, which does not vanish at z = Pi/2; without 3 H the mode operator is not formally Hermitian for this measure and these variables (Psi = Sin[z]^(-1/2) chi with the measure dy needs no such term)"];

(* ================================================================== formulas: geometry *)
addFormula["metric", "the author's metric (SPEC section 1), coordinates x1..x8", rftMetricAuthor];
addFormula["vielbein_diagonal", "f_a in e^a_mu = f_a delta^a_mu, a = x1..x8", f];
addFormula["sqrt_det_g", "sqrt|det g|", Cos[6 H x8]];
addFormula["eta", "frame metric eta_ab, order x1..x8", Diagonal[eta]];

(* ================================================================== reports *)
section["writing outputs"];
jstr[s_String] := "\"" <> StringReplace[s, {"\\" -> "\\\\", "\"" -> "\\\"", "\n" -> "\\n"}] <> "\"";
writeLF[path_, text_String] := Module[{s = OpenWrite[path, BinaryFormat -> True, CharacterEncoding -> "UTF-8"]},
  BinaryWrite[s, ToCharacterCode[text, "UTF-8"]]; Close[s]];
nPass = Count[checks, c_ /; c["verdict"] == "PASS"]; nTot = Length[checks];
report = StringJoin[
  "{\n",
  "  \"report\": ", jstr["Revision field theory (SPEC sections 1-4, 6): vielbein, canonical spin connection, Lagrangian, Euler-Lagrange equations, non-triviality [1] and [2], current, energy-momentum tensor, canonical quantisation; both statistics, verified exactly in WolframScript"], ",\n",
  "  \"producer\": ", jstr["Revision/theory/wolfram/verify_field_theory.wls"], ",\n",
  "  \"package\": ", jstr["Revision/theory/wolfram/RevisionFieldTheory.wl"], ",\n",
  "  \"fixture\": ", jstr["Revision/algebra/gammas.json"], ",\n",
  "  \"statistics\": ", jstr["G = dirac16complex: 16 complex anticommuting components, explicit Grassmann algebra with generators theta_1, theta_2 and their conjugates; C = dirac16complex00: 16 complex commuting components"], ",\n",
  "  \"coordinates\": ", jstr["x1, x2, x3 = 3-space; x4 = time; x5, x6, x7 = the exponentially deflating extra times; x8 = the hidden direction; z = 6 H x8 in (0, Pi/2), H > 0"], ",\n",
  "  \"summary\": {\"passed\": ", ToString[nPass], ", \"failed\": ", ToString[nTot - nPass], ", \"total\": ", ToString[nTot], "},\n",
  "  \"checks\": [\n",
  StringRiffle[("    {\"name\": " <> jstr[#["name"]] <> ", \"verdict\": " <> jstr[#["verdict"]] <> ", \"detail\": " <> jstr[#["detail"]] <> "}") & /@ checks, ",\n"],
  "\n  ]\n}\n"];
fjson[fm_] := Module[{w = fm["wl"]},
  "    {\"key\": " <> jstr[fm["key"]] <> ", \"description\": " <> jstr[fm["description"]] <> ", \"wl\": " <>
  If[ListQ[w], "[\n" <> StringRiffle[("      " <> jstr[#]) & /@ w, ",\n"] <> "\n    ]", jstr[w]] <> "}"];
formulaText = StringJoin[
  "{\n",
  "  \"description\": ", jstr["Exact formulas of the Revision field theory (SPEC sections 1-4, 6) for the author's primordial metric, for the documents. Every formula is verified by a named check of Revision/theory/reports/wolfram-field-theory.json. Wolfram InputForm; g[xa] = gamma^(xa) of Revision/algebra/gammas.json; a4' = Derivative[1][a4][x4]; z = 6 H x8; Psibar = Psi^dagger C; S = Psibar Psi; V = m + U'(S); both statistics unless stated."], ",\n",
  "  \"producer\": ", jstr["Revision/theory/wolfram/verify_field_theory.wls"], ",\n",
  "  \"formulas\": [\n",
  StringRiffle[fjson /@ formulas, ",\n"],
  "\n  ]\n}\n"];
If[!DirectoryQ[FileNameJoin[{$theoryDir, "reports"}]], CreateDirectory[FileNameJoin[{$theoryDir, "reports"}]]];
writeLF[FileNameJoin[{$theoryDir, "reports", "wolfram-field-theory.json"}], report];
writeLF[FileNameJoin[{$theoryDir, "field-theory.json"}], formulaText];
Print[nPass, "/", nTot, " checks passed; total time ", Round[AbsoluteTime[] - t0, 0.1], " s"];
Exit[If[nPass == nTot, 0, 1]];
