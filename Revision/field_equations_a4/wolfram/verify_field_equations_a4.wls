#!/usr/bin/env wolframscript
(* ::Package:: *)

(* verify_field_equations_a4.wls

   Driver for Revision/field_equations_a4/wolfram/FieldEquationsA4.wl (Revision/SPEC.md section 5).
   Writes, deterministically (LF line endings, no time stamps):
     Revision/field_equations_a4/a4-equations.json                 the equations (exact, InputForm + TeX)
     Revision/field_equations_a4/reports/wolfram-a4-report.json    every check with name, verdict, detail
   Input: Revision/algebra/gammas.json (the author's T16, order x1..x8), the primary representation of every
   spinor statement; FieldEquationsA4.wl reads it strictly on loading.  A missing or malformed gammas.json stops
   the run at once with a line "ERROR  ..." and exit code 1 (no output is written).  So does a missing or
   unreadable FieldEquationsA4.wl, and an output file that cannot be opened for writing gives a line
   "ERROR  cannot write ..." and exit code 1.
   Usage (from the repository root):
     wolframscript -file Revision/field_equations_a4/wolfram/verify_field_equations_a4.wls
   All checks are exact symbolic identities (no floating point).  Exit code 0 iff every check passes.
*)

$here = DirectoryName[$InputFileName];
$fieldDir = FileNameJoin[{$here, ".."}];
$revDir = FileNameJoin[{$fieldDir, ".."}];
$package = FileNameJoin[{$here, "FieldEquationsA4.wl"}];
If[!FileExistsQ[$package], Print["ERROR  ", $package, ": package not found"]; Exit[1]];
If[Get[$package] === $Failed, Print["ERROR  ", $package, ": Get failed"]; Exit[1]];

checks = {};
addCheck[name_String, ok_, detail_String] :=
  AppendTo[checks, <|"name" -> name, "verdict" -> If[TrueQ[ok], "PASS", "FAIL"], "detail" -> detail|>];

(* ---------- deterministic JSON writer ---------- *)
jsonEsc[s_String] := StringReplace[s, {"\\" -> "\\\\", "\"" -> "\\\"", "\n" -> "\\n", "\t" -> "\\t"}];
toJSON[s_String, _] := "\"" <> jsonEsc[s] <> "\"";
toJSON[True, _] := "true"; toJSON[False, _] := "false";
toJSON[n_Integer, _] := ToString[n];
toJSON[l_List, ind_] := If[l === {}, "[]",
   "[\n" <> StringRiffle[(StringRepeat[" ", ind + 2] <> toJSON[#, ind + 2]) & /@ l, ",\n"] <> "\n" <> StringRepeat[" ", ind] <> "]"];
toJSON[a_Association, ind_] := If[Length[a] == 0, "{}",
   "{\n" <> StringRiffle[KeyValueMap[(StringRepeat[" ", ind + 2] <> toJSON[#1, 0] <> ": " <> toJSON[#2, ind + 2]) &, a], ",\n"] <>
    "\n" <> StringRepeat[" ", ind] <> "}"];
writeJSON[path_, data_] := Module[{s = Quiet[OpenWrite[path, BinaryFormat -> True]]},
   If[Head[s] =!= OutputStream, Print["ERROR  cannot write ", path]; Exit[1]];
   If[BinaryWrite[s, ToCharacterCode[toJSON[data, 0] <> "\n", "UTF-8"]] === $Failed,
    Close[s]; Print["ERROR  cannot write ", path]; Exit[1]];
   Close[s]];

(* expressions as strings: InputForm (parsable by sympy once the caret is replaced) and TeX *)
fnRules = {Derivative[1, 0][f_][x4, x8] :> Symbol["d4" <> SymbolName[f]],
   Derivative[0, 1][f_][x4, x8] :> Symbol["d8" <> SymbolName[f]], f_Symbol[x4, x8] :> f, a4[x4] -> a4v};
inp[e_] := ToString[e /. fnRules, InputForm, PageWidth -> Infinity];
bs = FromCharacterCode[92];   (* the backslash *)
texRules = Map[(bs <> "text{" <> #[[1]] <> "}") -> StringReplace[#[[2]], "@" -> bs] &, {
    {"ad1", "(a_4')"}, {"ad2", "a_4''"}, {"alpha1", "@alpha_1"}, {"alpha2", "@alpha_2"}, {"alpha3", "@alpha_3"},
    {"Lam", "@Lambda"}, {"AA", "A"}, {"cc", "@cot z"}, {"a4v", "a_4"}, {"pt", "p_t"}, {"p3", "p_3"}, {"p8", "p_8"},
    {"q48", "q_{48}"}, {"q84", "q_{84}"}, {"sigmaT", "@sigma_T"},
    {"d4rho", "@partial_4 @rho"}, {"d8rho", "@partial_8 @rho"}, {"d4p3", "@partial_4 p_3"}, {"d8p3", "@partial_8 p_3"},
    {"d4pt", "@partial_4 p_t"}, {"d8pt", "@partial_8 p_t"}, {"d4p8", "@partial_4 p_8"}, {"d8p8", "@partial_8 p_8"},
    {"d4q48", "@partial_4 q_{48}"}, {"d8q48", "@partial_8 q_{48}"}, {"d4q84", "@partial_4 q_{84}"}, {"d8q84", "@partial_8 q_{84}"}}];
tex[e_] := StringReplace[ToString[TeXForm[e /. fnRules]], texRules];
expr[e_] := <|"input" -> inp[e], "tex" -> tex[e]|>;
eqn[l_, r_] := <|"input" -> inp[l] <> " == " <> inp[r], "tex" -> tex[l] <> " = " <> tex[r]|>;
zero16 = ConstantArray[0, {16, 16}];
coordName[i_] := ToString[FECoords[[i]]];

(* ======================================================================
   1. Geometry
   ====================================================================== *)
addCheck["metric_is_SPEC_section_1",
  FEMetricDiag === {E^(2 a4[x4]) Sin[6 H x8]^(1/3), E^(2 a4[x4]) Sin[6 H x8]^(1/3), E^(2 a4[x4]) Sin[6 H x8]^(1/3), -1,
     -E^(-2 a4[x4]) Sin[6 H x8]^(1/3), -E^(-2 a4[x4]) Sin[6 H x8]^(1/3), -E^(-2 a4[x4]) Sin[6 H x8]^(1/3), Cot[6 H x8]^2},
  "g = diag(e^{2a4} s, e^{2a4} s, e^{2a4} s, -1, -e^{-2a4} s, -e^{-2a4} s, -e^{-2a4} s, cot^2 z), s = sin^{1/3} z, z = 6 H x8 (x1..x8)"];
addCheck["sqrt_abs_det_g_is_cos_z",
  Together[FENormal[Times @@ FEMetricDiag] - cc^2/(1 + cc^2)] === 0,
  "sqrt|det g| = sin z cot z = cos z on 0 < z < pi/2 (independent of a4: the 7-volume factor e^{3a4} e^{-3a4} = 1)"];

riemannSthirdFree = FreeQ[FERiemannUU, Sin] && FreeQ[FERiemannUU, a4] && FreeQ[FERiemannUU, a0];
addCheck["mixed_riemann_free_of_warp_and_a4",
  riemannSthirdFree,
  "every R^{ab}_{cd} (MTW, computed here from the Christoffel symbols) is a function of H, a4', a4'', cot z only (a Laurent polynomial in cot z): the warp sin^{1/3} z and e^{a4} cancel; " <>
   ToString[Length[FERiemannPairs]] <> " nonzero components with a < b, c < d"];
addCheck["riemann_pair_antisymmetry",
  And @@ Flatten[Table[FERiemannUU[[a, b, c, d]] === -FERiemannUU[[b, a, c, d]] && FERiemannUU[[a, b, c, d]] === -FERiemannUU[[a, b, d, c]],
     {a, 8}, {b, 8}, {c, 8}, {d, 8}]],
  "R^{ab}_{cd} = -R^{ba}_{cd} = -R^{ab}_{dc} for all 4096 index lists"];

(* ======================================================================
   2. Lovelock tensors: direct GKD computation here, and the GKD branch's monomial lists
   ====================================================================== *)
lovelockJSON = Import[FileNameJoin[{$revDir, "gkd_lovelock", "results", "lovelock-tensors.json"}], "RawJSON"];
Pdirect = Table[FELovelockDirect[k], {k, 3}];
Ldirect = Table[FELovelockScalarDirect[k], {k, 3}];
Prebuilt = Table[FERebuildMixed[lovelockJSON, "P" <> ToString[k] <> "_mixed_up_h_down_j"], {k, 3}];
Lrebuilt = Table[FERebuildScalar[lovelockJSON, "L" <> ToString[k]], {k, 3}];

addCheck["P1_direct_equals_minus_4_Einstein",
  And @@ Flatten[Table[FENormal[Pdirect[[1, h, j]] + 4 FEEinsteinMixed[[h, j]]] === 0, {h, 8}, {j, 8}]],
  "P_(1)^h_j = GKD[{h,h1,h2},{j,j1,j2}] R^{j1j2}_{h1h2} equals -4 G^h_j, G from the Ricci tensor (two routes, both in this file)"];
Do[
  addCheck["P" <> ToString[k] <> "_direct_equals_gkd_branch_monomials",
   And @@ Flatten[Table[FENormal[Pdirect[[k, h, j]] - Prebuilt[[k, h, j]]] === 0, {h, 8}, {j, 8}]],
   "all 64 components of P_(" <> ToString[k] <> ")^h_j computed here (GKD as Det of the delta matrix, sum over the nonzero R^{ab}_{cd}) equal the exact monomial lists of Revision/gkd_lovelock/results/lovelock-tensors.json"];
  addCheck["L" <> ToString[k] <> "_direct_equals_gkd_branch",
   FENormal[Ldirect[[k]] - Lrebuilt[[k]]] === 0,
   "L_(" <> ToString[k] <> ") = " <> inp[Expand[Ldirect[[k]]]]];
  addCheck["P" <> ToString[k] <> "_trace_identity",
   FENormal[Tr[Pdirect[[k]]] - (8 - 2 k) Ldirect[[k]]] === 0,
   "sum_h P_(" <> ToString[k] <> ")^h_h = (8 - " <> ToString[2 k] <> ") L_(" <> ToString[k] <> ")"];
  addCheck["P" <> ToString[k] <> "_structure",
   FreeQ[Pdirect[[k]], cc] && And @@ Flatten[Table[If[h != j, Pdirect[[k, h, j]] === 0, True], {h, 8}, {j, 8}]] &&
    Pdirect[[k, 1, 1]] === Pdirect[[k, 2, 2]] === Pdirect[[k, 3, 3]] && Pdirect[[k, 5, 5]] === Pdirect[[k, 6, 6]] === Pdirect[[k, 7, 7]],
   "P_(" <> ToString[k] <> ")^h_j is diagonal (in particular the x4-x8 components vanish), free of x8, with x1 = x2 = x3 and x5 = x6 = x7"],
  {k, 3}];
addCheck["P4_vanishes_pigeonhole",
  FEGKD[{1, 2, 3, 4, 5, 6, 7, 8, 1}, {1, 2, 3, 4, 5, 6, 7, 8, 2}] === 0 && FEGKD[Range[8], Range[8]] === 1,
  "P_(4) would need GKD of 9 indices over 8 values: two equal upper indices give two equal rows of the delta matrix, determinant 0; so k = 1, 2, 3 is the full Lovelock series in 8 dimensions"];

Ek = Table[-Pdirect[[k]]/2^(k + 1), {k, 3}];
EkD = Map[# /. FESymToDeriv &, Ek, {3}];
Do[
  addCheck["E" <> ToString[k] <> "_divergence_free",
   And @@ (FEZeroQ /@ FEDivergence[EkD[[k]]]),
   "nabla_mu E_(" <> ToString[k] <> ")^mu_nu = 0 for nu = x1..x8 (exact; Christoffel symbols of this file)"],
  {k, 3}];

(* ======================================================================
   3. The field equations with a general homogeneous source
   ====================================================================== *)
alphas = {alpha1, alpha2, alpha3};
LHS = Sum[alphas[[k]] Ek[[k]], {k, 3}] + Lam IdentityMatrix[8];
Tsrc = DiagonalMatrix[{p3, p3, p3, -rho, pt, pt, pt, p8}]; Tsrc[[4, 8]] = q48; Tsrc[[8, 4]] = q84;
FEq = Expand[LHS - kappa Tsrc];   (* FEq = 0 are the field equations *)
e11 = Expand[LHS[[1, 1]] - Lam]; e44 = Expand[LHS[[4, 4]] - Lam]; e55 = Expand[LHS[[5, 5]] - Lam]; e88 = Expand[LHS[[8, 8]] - Lam];
eD = Factor[Expand[e11 - e55]];
fEvo = Expand[Simplify[(e11 - e55)/ad2]];

addCheck["independent_components",
  And @@ Flatten[Table[If[h != j && !MemberQ[{{4, 8}, {8, 4}}, {h, j}], FEq[[h, j]] === 0, True], {h, 8}, {j, 8}]] &&
   FEq[[1, 1]] === FEq[[2, 2]] === FEq[[3, 3]] && FEq[[5, 5]] === FEq[[6, 6]] === FEq[[7, 7]],
  "the left-hand sides of the 64 components reduce to x1 (= x2 = x3), x4, x5 (= x6 = x7), x8 and the x4-x8 pair; every other off-diagonal left-hand side is 0, so those components read 0 = kappa T^mu_nu"];
addCheck["evolution_factorises_a4pp_times_F",
  FreeQ[fEvo, ad2] && Expand[fEvo ad2 - (e11 - e55)] === 0,
  "sum_k alpha_k (E_(k)^x1_x1 - E_(k)^x5_x5) = a4'' F(a4'), F = " <> inp[fEvo]];
addCheck["evolution_F_not_identically_zero",
  Module[{cl = CoefficientList[fEvo, ad1]}, Reduce[And @@ Thread[Flatten[CoefficientList[fEvo, {ad1, H}]] == 0], {alpha1, alpha2, alpha3}] === (alpha1 == 0 && alpha2 == 0 && alpha3 == 0)],
  "F(a4') vanishes identically as a polynomial in (a4', H) only for alpha1 = alpha2 = alpha3 = 0"];
addCheck["algebraic_identity_x1_plus_x5_minus_2x8",
  Expand[e11 + e55 - 2 e88] === 0,
  "sum_k alpha_k (E^x1_x1 + E^x5_x5 - 2 E^x8_x8) = 0 identically (each k separately), so the field equations imply p3 + p_t = 2 p8"];
addCheck["x8_component_contains_no_a4pp",
  FreeQ[e88, ad2] && FreeQ[e44, ad2],
  "the x4 (constraint) and x8 components contain a4' only (first order)"];
bianchi44 = Expand[(D[e44 /. FESymToDeriv, x4] /. FEDerivToSym) - 3 ad1 (e11 - e55)];
addCheck["constraint_propagation_bianchi",
  bianchi44 === 0,
  "d/dx4 [sum_k alpha_k E_(k)^x4_x4] = 3 a4' sum_k alpha_k (E^x1_x1 - E^x5_x5) identically (the x4 component of the Bianchi identity): the derivative of the constraint equals 3 a4' times the evolution equation once rho' = -3 a4' (p3 - p_t)"];

(* conservation of a general source T(x4, x8) *)
Tgen = DiagonalMatrix[{p3[x4, x8], p3[x4, x8], p3[x4, x8], -rho[x4, x8], pt[x4, x8], pt[x4, x8], pt[x4, x8], p8[x4, x8]}];
Tgen[[4, 8]] = q48[x4, x8]; Tgen[[8, 4]] = q84[x4, x8];
divT = FENormal /@ FEDivergence[Tgen];
consX4 = Collect[Expand[divT[[4]]], {cc}];
consX8 = Collect[Expand[divT[[8]]], {cc}];
addCheck["conservation_components",
  And @@ (# === 0 & /@ divT[[{1, 2, 3, 5, 6, 7}]]) &&
   Expand[divT[[4]] - (-D[rho[x4, x8], x4] - 3 ad1 (p3[x4, x8] - pt[x4, x8]) + D[q84[x4, x8], x8] - 6 H q84[x4, x8]/cc)] === 0 &&
   Expand[divT[[8]] - (D[p8[x4, x8], x8] + 3 H cc (2 p8[x4, x8] - p3[x4, x8] - pt[x4, x8]) + D[q48[x4, x8], x4])] === 0,
  "nabla_mu T^mu_x4 = -d4 rho - 3 a4' (p3 - p_t) + d8 q84 - 6 H tan(z) q84 and nabla_mu T^mu_x8 = d8 p8 + 3 H cot(z) (2 p8 - p3 - p_t) + d4 q48 (the other components vanish identically)"];

(* source required by a given a4 *)
srcRho = Expand[-(e44 + Lam)/kappa]; srcP3 = Expand[(e11 + Lam)/kappa]; srcPt = Expand[(e55 + Lam)/kappa]; srcP8 = Expand[(e88 + Lam)/kappa];
nec8 = Expand[e88 - e44]; nec3 = Expand[e11 - e44]; nect = Expand[e55 - e44];
einst = {alpha1 -> 1, alpha2 -> 0, alpha3 -> 0};
addCheck["einstein_components",
  Expand[e44 /. einst] === 3 ad1^2 + 21 H^2 && Expand[e11 /. einst] === ad2 - 3 ad1^2 + 15 H^2 &&
   Expand[e55 /. einst] === -ad2 - 3 ad1^2 + 15 H^2 && Expand[e88 /. einst] === -3 ad1^2 + 15 H^2,
  "Einstein (alpha1 = 1, alpha2 = alpha3 = 0): G^x4_x4 = 3 a4'^2 + 21 H^2, G^x1_x1 = a4'' - 3 a4'^2 + 15 H^2, G^x5_x5 = -a4'' - 3 a4'^2 + 15 H^2, G^x8_x8 = -3 a4'^2 + 15 H^2"];
addCheck["einstein_null_energy_x8",
  Expand[nec8 /. einst] === -6 ad1^2 - 6 H^2,
  "Einstein: kappa (rho + p8) = -6 (a4'^2 + H^2) < 0 for every a4 and every Lambda (H > 0): the source violates the null energy condition along the null direction x4 + x8"];
addCheck["einstein_no_vacuum_solution",
  Reduce[(e44 /. einst) + Lam == 0 && (e11 /. einst) + Lam == 0 && (e55 /. einst) + Lam == 0 && (e88 /. einst) + Lam == 0 && H > 0, {ad1, ad2, Lam}, Reals] === False,
  "with T = 0 the Einstein equations (any Lambda) have no real solution a4 for H > 0: the x4 and x8 components give 36 H^2 + 2 Lambda = 0 and 6 a4'^2 + 6 H^2 = 0"];

(* ======================================================================
   4. The linear member a4 = A H x4 + a0 (3-space inflates as e^{A H x4}, the extra times deflate as e^{-A H x4})
   ====================================================================== *)
lin = {ad1 -> AA H, ad2 -> 0};
rhoLin = Expand[srcRho /. lin]; pLin = Expand[srcP8 /. lin];
addCheck["linear_member_equal_pressures",
  Expand[(srcP3 - srcP8) /. lin] === 0 && Expand[(srcPt - srcP8) /. lin] === 0,
  "for a4 = A H x4 + a0 (a4'' = 0) the field equations require p3 = p_t = p8 =: p, all constant, rho constant (any alpha_k, Lambda)"];
vacPoly = Factor[Expand[((e44 - e88) /. lin)/H^2]];
vacReduced = Expand[Simplify[vacPoly/(6 (AA^2 + 1))]];
addCheck["linear_member_vacuum_factor",
  Expand[vacReduced 6 (AA^2 + 1) - ((e44 - e88) /. lin)/H^2] === 0 && PolynomialQ[vacReduced, AA],
  "sum_k alpha_k (E^x4_x4 - E^x8_x8) at a4' = A H equals 6 (A^2 + 1) H^2 V, V = " <> inp[vacReduced] <> "; vacuum (rho = p = 0) needs V = 0"];
addCheck["einstein_gauss_bonnet_vacuum_linear",
  Expand[(vacReduced /. {alpha3 -> 0, alpha1 -> 1} /. AA -> Sqrt[(1 - 40 alpha2 H^2)/(8 alpha2 H^2)]) ] === 0 &&
   Expand[(vacReduced /. {alpha3 -> 0, alpha1 -> 1}) - (1 - 8 alpha2 H^2 (AA^2 + 5))] === 0,
  "Einstein-Gauss-Bonnet (alpha1 = 1, alpha3 = 0): V = 1 - 8 alpha2 H^2 (A^2 + 5), so V = 0 gives A^2 = (1 - 40 alpha2 H^2)/(8 alpha2 H^2)" <>
   " (real A iff 0 < alpha2 H^2 <= 1/40), with Lambda = -sum_k alpha_k E^x4_x4"];

(* ======================================================================
   5. Field-specific sources: the spinor bilinears in the author's T16 (the PRIMARY representation, SPEC
      section 2: Revision/algebra/gammas.json, read strictly by FieldEquationsA4.wl).  The representation
      Cl(1,1)^(x)4 built in FieldEquationsA4.wl is used ONLY for comparison: its Clifford relations and C, its
      exact equivalence with T16, and the representation independence of the off-diagonal coefficients.
   ====================================================================== *)
fx = FEFixture; gR = FEGammaFrameComparison; CR = FECComparison;
(* the kinetic matrices of the homogeneous condensate in a representation g with charge matrix Cm:
   Phi = Phi(x4) on shell, d4 Phi = A Phi with A = -gamma^x4 (M - gamma^mu Omega_mu); N^mu_nu with
   K^mu_nu = Phi^dagger N^mu_nu Phi, K^mu_nu = (1/2)(Phibar gamma^mu D_nu Phi - (D_nu Phibar) gamma^mu Phi) *)
gd = FEMetricDiag;
condensateKinetic[g_List, Cm_] := Module[{gc, om, gdir, am, dP, dPb, nm, ns},
   gc = Map[FENormal, FEGammaCoordOf[g], {3}]; om = Map[FENormal, FEOmegaOf[g], {3}];
   gdir = Map[FENormal, Sum[gc[[mu]] . om[[mu]], {mu, 8}], {2}];
   am = -gc[[4]] . (MM IdentityMatrix[16] - gdir);     (* d4 Phi = A Phi, since (gamma^x4)^-1 = -gamma^x4 *)
   dP[nu_] := If[nu == 4, am, zero16] + om[[nu]];
   dPb[nu_] := If[nu == 4, Transpose[am] . Cm, zero16] - Cm . om[[nu]];
   nm = Table[Map[FENormal, (1/2) (Cm . gc[[mu]] . dP[nu] - dPb[nu] . gc[[mu]]), {2}], {mu, 8}, {nu, 8}];
   ns = Table[Map[FENormal, (1/2) (nm[[mu, nu]] + (gd[[nu]]/gd[[mu]]) nm[[nu, mu]]), {2}], {mu, 8}, {nu, 8}];
   <|"gC" -> gc, "Om" -> om, "Gdirac" -> gdir, "Amat" -> am, "Nmat" -> nm, "NmatSym" -> ns|>];
(* the decomposition of the nonzero off-diagonal N^mu_nu in the Clifford basis C gamma^I of a representation *)
subsets = Subsets[Range[8]];
basisMatIn[g_List, Cm_, s_List] := Cm . If[s === {}, IdentityMatrix[16], Dot @@ (g[[#]] & /@ s)];
offDiagonalDecomposition[g_List, Cm_, ns_] := Module[{binv, dec, pairs},
   binv = Association[(# -> Inverse[basisMatIn[g, Cm, #]]) & /@ subsets];
   dec[N_] := Select[Association[(# -> Together[Tr[binv[#] . N]/16]) & /@ subsets], # =!= 0 &];
   pairs = Select[Flatten[Table[{mu, nu}, {mu, 8}, {nu, 8}], 1], #[[1]] != #[[2]] && ns[[#[[1]], #[[2]]]] =!= zero16 &];
   Association[(# -> dec[ns[[#[[1]], #[[2]]]]]) & /@ pairs]];

prim = condensateKinetic[FEGammaFrame, FEC];
gF = FEGammaFrame; gC = prim["gC"]; Om = prim["Om"];
addCheck["fixture_author_T16_read",
  fx["coordinates"] === {"x1", "x2", "x3", "x4", "x5", "x6", "x7", "x8"} && fx["notebookFrameIndex"] === {1, 2, 3, 4, 5, 6, 7, 0} &&
   fx["eta"] === Diagonal[FEEta] && Length[gF] == 8 && And @@ (MatrixQ[#, IntegerQ[#] || Head[#] === Rational &] && Dimensions[#] == {16, 16} & /@ gF) &&
   fx["S"] === FESab && fx["Gamma"] === Dot @@ gF[[{8, 1, 2, 3, 4, 5, 6, 7}]] && fx["B"] === -I fx["C"] . gF[[4]],
  "Revision/algebra/gammas.json (sha256 " <> fx["sha256"] <> ") read with strict parsing (every entry a JSON integer or a string \"p/q\" in lowest terms; a missing or malformed file stops the run with an ERROR line and exit code 1): coordinates x1..x8, notebook frame index {1, 2, 3, 4, 5, 6, 7, 0} (gamma^(x1..x7) = T16[1..7], gamma^(x8) = T16[0]), eta = diag(1,1,1,-1,-1,-1,-1,1), 8 real exact 16 x 16 matrices; the fixture's S, Gamma and B equal (1/4)[gamma^a, gamma^b], gamma^x8 gamma^x1 ... gamma^x7 and -i C gamma^x4 of these gammas: the primary representation of every spinor statement below"];
addCheck["clifford_relations_author_T16",
  And @@ Flatten[Table[gF[[a]] . gF[[b]] + gF[[b]] . gF[[a]] == 2 FEEta[[a, b]] IdentityMatrix[16], {a, 8}, {b, 8}]],
  "the author's T16 (primary representation, Revision/algebra/gammas.json) satisfies {gamma^a, gamma^b} = 2 eta^ab, eta = diag(1,1,1,-1,-1,-1,-1,1)"];
addCheck["C_properties_author_T16",
  FEC === fx["C"] && FEC === Transpose[FEC] && FEC . FEC === IdentityMatrix[16] && And @@ Table[Transpose[FEC . gF[[a]]] === -FEC . gF[[a]], {a, 8}],
  "C = gamma^x8 gamma^x1 gamma^x2 gamma^x3 of the author's T16 equals the fixture's C (the notebook's sigma16 in the order x1..x8) and is real symmetric, C^2 = 1, C gamma^a antisymmetric (SPEC section 2); every bilinear below uses this C"];
addCheck["clifford_relations_own_rep",
  And @@ Flatten[Table[gR[[a]] . gR[[b]] + gR[[b]] . gR[[a]] == 2 FEEta[[a, b]] IdentityMatrix[16], {a, 8}, {b, 8}]],
  "comparison representation only (not used for any result): the representation built in FieldEquationsA4.wl (Cl(1,1) tensor-graded four times; real 16 x 16) satisfies {gamma^a, gamma^b} = 2 eta^ab, eta = diag(1,1,1,-1,-1,-1,-1,1)"];
addCheck["C_properties_own_rep",
  CR === Transpose[CR] && CR . CR === IdentityMatrix[16] && And @@ Table[Transpose[CR . gR[[a]]] === -CR . gR[[a]], {a, 8}],
  "comparison representation only: C = gamma^x8 gamma^x1 gamma^x2 gamma^x3 is real symmetric, C^2 = 1, C gamma^a antisymmetric (the properties SPEC section 2 requires)"];
kBasis = FEIntertwinerBasis[gR, gF];   (* K . gamma_R^a == gamma_T16^a . K *)
kMat = If[Length[kBasis] == 1, First[kBasis], zero16];
kc = (Transpose[kMat] . kMat)[[1, 1]];
addCheck["representations_equivalent_author_T16_own_rep",
  Length[kBasis] == 1 && kc > 0 && Transpose[kMat] . kMat === kc IdentityMatrix[16] &&
   And @@ Table[kMat . gR[[a]] === gF[[a]] . kMat, {a, 8}] && kMat . CR === FEC . kMat,
  "exact (NullSpace over the rationals): the intertwiners K with K gamma_R^a = gamma_T16^a K for a = x1..x8 (gamma_R the comparison representation) form a space of dimension " <>
   ToString[Length[kBasis]] <> ", and K^T K = " <> ToString[kc, InputForm] <> " I16 (K is " <> ToString[Sqrt[kc], InputForm] <>
   " times an orthogonal matrix) with K C_R = C_T16 K: the two representations are equivalent, so every trace of a product of gammas (in particular every coefficient in the Clifford basis C gamma^I) is the same in both"];
spinAnti = And @@ Flatten[Table[FENormal[FESpinConnLow[[mu, a, b]] + FESpinConnLow[[mu, b, a]]] === 0, {mu, 8}, {a, 8}, {b, 8}]];
addCheck["spin_connection_antisymmetric", spinAnti, "omega_mu ab = -omega_mu ba for the canonical spin connection of this metric (vielbein postulate)"];
addCheck["Omega_x4_Omega_x8_vanish",
  Om[[4]] === zero16 && Om[[8]] === zero16,
  "Omega_x4 = Omega_x8 = 0 (the diagonal vielbein has no x4 component that varies, and e^x8 depends on x8 only)"];
anticommOm = Table[Map[FENormal, gC[[mu]] . Om[[mu]] + Om[[mu]] . gC[[mu]], {2}], {mu, 8}];
addCheck["gamma_mu_anticommutes_with_Omega_mu_no_sum",
  And @@ (# === zero16 & /@ anticommOm),
  "{gamma^mu, Omega_mu} = 0 for each mu separately (no sum): the spin connection drops out of every diagonal kinetic component K^mu_mu = (1/2)(Psibar gamma^mu d_mu Psi - d_mu Psibar gamma^mu Psi)"];
Gdirac = prim["Gdirac"];   (* Map[FENormal, Sum[gC[[mu]] . Om[[mu]], {mu, 8}], {2}] *)
addCheck["gravity_term_gamma_mu_Omega_mu",
  Gdirac === 3 H gF[[8]],
  "gamma^mu Omega_mu = 3 H gamma^x8 exactly (the x4 terms of the 3 inflating and 3 deflating directions cancel; the hidden-direction term survives; independent of a4 and x8)"];

(* the homogeneous condensate: Phi(x4) independent of x1..x3, x5..x8, on shell gamma^mu D_mu Phi = M Phi, M = m + U'(S) real *)
g4 = gC[[4]];
Amat = prim["Amat"];     (* -g4 . (MM I16 - Gdirac): d4 Phi = Amat Phi, since (gamma^x4)^-1 = -gamma^x4 *)
addCheck["condensate_equation_x8_consistent",
  FreeQ[Amat, x8] && FreeQ[Amat, cc] && Expand[g4 . Amat + Gdirac - MM IdentityMatrix[16]] === zero16,
  "for Phi = Phi(x4) the equation is d4 Phi = A Phi with A = -gamma^x4 (M - 3 H gamma^x8), free of x8: an x8-independent solution exists"];
addCheck["condensate_S_constant",
  Expand[FEC . Amat + Transpose[Amat] . FEC] === zero16,
  "C A + A^T C = 0 (M real), so d4 S = d4 (Phi^dagger C Phi) = 0: S is constant along x4 (exact, for every initial Phi)"];
addCheck["condensate_adjoint_equation",
  Expand[Transpose[Amat] . FEC . g4 - FEC . Sum[Om[[mu]] . gC[[mu]], {mu, 8}] + MM FEC] === zero16,
  "(D_mu Phibar) gamma^mu = -M Phibar holds for the condensate (the adjoint of the field equation)"];
(* kinetic matrices N^mu_nu with K^mu_nu = Phi^dagger N^mu_nu Phi, K^mu_nu = (1/2)(Phibar gamma^mu D_nu Phi - (D_nu Phibar) gamma^mu Phi),
   and their symmetrisation (computed by condensateKinetic above) *)
Nmat = prim["Nmat"];
NmatSym = prim["NmatSym"];
addCheck["condensate_kinetic_tensor_diagonal",
  NmatSym[[4, 8]] === zero16 && NmatSym[[8, 4]] === zero16 && And @@ Table[NmatSym[[mu, mu]] === zero16, {mu, {1, 2, 3, 5, 6, 7, 8}}] &&
   Expand[NmatSym[[4, 4]] - MM FEC] === zero16,
  "for the condensate the symmetrised kinetic tensor has K^x4_x4 = M S, K^mu_mu = 0 for mu = x1..x3, x5..x8, and K^x4_x8 = K^x8_x4 = 0, exactly, for every Phi"];

(* the remaining off-diagonal components: decomposition in the Clifford basis C gamma^I (offDiagonalDecomposition above) *)
basisMat[s_List] := basisMatIn[gF, FEC, s];
offDecomp = offDiagonalDecomposition[gF, FEC, NmatSym];
offPairs = Keys[offDecomp];
recon = And @@ Table[Expand[Total[KeyValueMap[#2 basisMat[#1] &, offDecomp[pq]]] - NmatSym[[pq[[1]], pq[[2]]]]] === zero16, {pq, offPairs}];
triples = Union[Flatten[Keys /@ Values[offDecomp], 1]];
addCheck["condensate_offdiagonal_are_three_gamma_bilinears",
  recon && And @@ (Length[#] == 3 & /@ triples) &&
   Sort[triples] === Sort[Join[Table[Sort[{i, 4, 8}], {i, {1, 2, 3, 5, 6, 7}}], Flatten[Table[Sort[{i, j, 4}], {i, 3}, {j, 5, 7}], 1]]],
  "the nonzero off-diagonal kinetic components of the condensate are exactly multiples of the 15 bilinears B_abc = Phibar gamma^a gamma^b gamma^c Phi with {a,b,c} = {i, x4, x8} (i = x1..x3, x5..x7; coefficients proportional to H or a4') and {i, j, x4} (i = x1..x3, j = x5..x7; coefficients proportional to a4'); " <>
   ToString[Length[offPairs]] <> " ordered pairs (mu, nu) are nonzero"];
(* the same pipeline in the comparison representation: the coefficients written to a4-equations.json do not depend on it *)
cmpR = condensateKinetic[gR, CR];
offDecompR = offDiagonalDecomposition[gR, CR, cmpR["NmatSym"]];
addCheck["offdiagonal_coefficients_representation_independent",
  cmpR["Gdirac"] === 3 H gR[[8]] && Keys[offDecompR] === offPairs &&
   And @@ Table[Keys[offDecompR[pq]] === Keys[offDecomp[pq]] &&
      And @@ (FENormal[#] === 0 & /@ (Values[offDecompR[pq]] - Values[offDecomp[pq]])), {pq, offPairs}],
  "the comparison representation (Cl(1,1)^(x)4, built in FieldEquationsA4.wl), run through the same condensate pipeline, gives gamma^mu Omega_mu = 3 H gamma^x8, the same " <>
   ToString[Length[offPairs]] <> " nonzero ordered pairs (mu, nu), the same three-gamma bilinears and exactly the same coefficients as the author's T16 (primary): the off-diagonal coefficients in a4-equations.json are representation independent"];

(* exact witnesses: Phi = Exp[-I w x4] Phi0, Phi0 = v1 + c v2 in the A-eigenspace with all 15 bilinears zero and S != 0 *)
witness[mval_, hval_] := Module[{w, Am, ex, v1, v2, sv, ph, ok, sval, conds, cv},
   w = Sqrt[mval^2 - 9 hval^2];
   Am = Amat /. {MM -> mval, H -> hval};
   ex[e_] := NullSpace[Join[Am + I w IdentityMatrix[16], gF[[1]] . gF[[5]] - e IdentityMatrix[16],
       gF[[2]] . gF[[6]] - e IdentityMatrix[16], gF[[3]] . gF[[7]] - e IdentityMatrix[16]]];
   v1 = First[ex[-1]]; v2 = First[ex[1]];
   sv = Conjugate[v1] . FEC . v2; cv = Conjugate[sv];
   ph = v1 + cv v2;
   sval = Simplify[Conjugate[ph] . FEC . ph];
   conds = Table[FullSimplify[Conjugate[ph] . (basisMat[t]) . ph], {t, triples}];
   ok = Length[ex[-1]] == 1 && Length[ex[1]] == 1 && Expand[Am . ph + I w ph] === ConstantArray[0, 16] &&
     And @@ (# === 0 & /@ conds) && sval =!= 0 && Element[sval, Reals] &&
     And @@ Table[Simplify[Conjugate[ph] . (NmatSym[[pq[[1]], pq[[2]]]] /. {MM -> mval, H -> hval}) . ph] === 0, {pq, offPairs}];
   {ok, w, sval}];
wit = {witness[5, 1], witness[5, 4/3], witness[-5, 1]};
(* Einstein conditions for the condensate with U = (lambda/2) S^2 on the linear member *)
condC = Expand[((e44 /. einst) /. lin) + Lam + kappa sigmaT (m S + lam S^2/2)];
condX = Expand[((e88 /. einst) /. lin) + Lam - kappa sigmaT (S (lam S) - lam S^2/2)];
addCheck["condensate_einstein_quadratic_U",
  Expand[condC + condX - (36 H^2 + 2 Lam + kappa sigmaT m S)] === 0 &&
   Expand[condC - condX - (6 (AA^2 + 1) H^2 + kappa sigmaT S (m + lam S))] === 0,
  "Einstein, a4 = A H x4 + a0, U = (lambda/2) S^2 (rho = sigmaT (m S + lambda S^2/2), p = sigmaT lambda S^2/2): the x4 and x8 equations are equivalent to kappa sigmaT m S = -(36 H^2 + 2 Lambda) and 6 (A^2 + 1) H^2 = -kappa sigmaT S (m + lambda S)"];

addCheck["condensate_diagonal_witness_exact",
  And @@ (#[[1]] & /@ wit),
  "exact Gaussian-rational witnesses (M, H) = (5, 1), (5, 4/3), (-5, 1): Phi = e^{-i w x4} Phi0 with w = sqrt(M^2 - 9 H^2) = " <> inp[#[[2]] & /@ wit] <>
   ", Phi0 = v1 + c v2 (v1, v2 the A-eigenvectors with gamma^x1 gamma^x5 = gamma^x2 gamma^x6 = gamma^x3 gamma^x7 = -1 and +1, c = conj(v1^dagger C v2)), solves the condensate equation; all 15 three-gamma bilinears and every off-diagonal kinetic component vanish for every a4, a4'; S = " <> inp[#[[3]] & /@ wit] <> " != 0"];

(* ======================================================================
   6. a4-equations.json
   ====================================================================== *)
offJSON = Table[<|"component" -> "K^" <> coordName[pq[[1]]] <> "_" <> coordName[pq[[2]]] <> " (symmetrised)",
     "terms" -> KeyValueMap[<|"bilinear" -> "Phibar " <> StringRiffle[("gamma^" <> coordName[#]) & /@ #1, " "] <> " Phi", "coefficient" -> expr[#2]|> &, offDecomp[pq]]|>,
   {pq, offPairs}];
compE[k_] := <|"x1x1" -> expr[Expand[Ek[[k, 1, 1]]]], "x4x4" -> expr[Expand[Ek[[k, 4, 4]]]], "x5x5" -> expr[Expand[Ek[[k, 5, 5]]]],
   "x8x8" -> expr[Expand[Ek[[k, 8, 8]]]], "x4x8" -> expr[Ek[[k, 4, 8]]], "x8x4" -> expr[Ek[[k, 8, 4]]]|>;
Fein = fEvo /. einst;

data = <|
  "title" -> "Einstein-Lovelock field equations for a4[x4] in the primordial metric (Revision/SPEC.md section 5)",
  "producer" -> "Revision/field_equations_a4/wolfram/verify_field_equations_a4.wls (with FieldEquationsA4.wl)",
  "conventions" -> <|
    "coordinates" -> "x1, x2, x3 = 3-space (scale factor e^{a4} sin^{1/6} z); x4 = time; x5, x6, x7 = extra times, time-like, deflating (scale factor e^{-a4} sin^{1/6} z); x8 = hidden direction, z = 6 H x8 in (0, pi/2)",
    "symbols" -> "ad1 = a4'(x4), ad2 = a4''(x4), H > 0, alpha1..alpha3 = Lovelock couplings, Lam = Lambda, kappa = gravitational coupling, cc = cot z; d4f, d8f = partial derivatives of f with respect to x4, x8",
    "curvature" -> "MTW: R^a_{bcd} = d_c Gamma^a_{bd} - d_d Gamma^a_{bc} + Gamma^a_{ce} Gamma^e_{bd} - Gamma^a_{de} Gamma^e_{bc}",
    "lovelock" -> "P_(k)^h_j = GKD[{h,h1..h2k},{j,j1..j2k}] R^{j1j2}_{h1h2} ... R^{j(2k-1)j2k}_{h(2k-1)h2k}; E_(k) = -P_(k)/2^(k+1); E_(1) = G",
    "fieldEquations" -> "sum_{k=1}^{3} alpha_k E_(k)^mu_nu + Lam delta^mu_nu = kappa T^mu_nu",
    "source" -> "T^mu_nu = diag(p3, p3, p3, -rho, p_t, p_t, p_t, p8) + q48 (mu = x4, nu = x8) + q84 (mu = x8, nu = x4); rho = -T^x4_x4, p_mu = T^mu_mu (no sum)"|>,
  "lovelockTensors" -> <|"E1" -> compE[1], "E2" -> compE[2], "E3" -> compE[3],
    "allOtherComponents" -> "x2x2 = x3x3 = x1x1, x6x6 = x7x7 = x5x5, every other off-diagonal component 0 (exact, all 64 components checked)"|>,
  "generalSource" -> <|
    "constraint_x4" -> eqn[e44 + Lam, -kappa rho],
    "space_x1_eq_x2_eq_x3" -> eqn[e11 + Lam, kappa p3],
    "extraTime_x5_eq_x6_eq_x7" -> eqn[e55 + Lam, kappa pt],
    "hidden_x8" -> eqn[e88 + Lam, kappa p8],
    "offDiagonal_x4x8" -> eqn[0, kappa q48],
    "offDiagonal_x8x4" -> eqn[0, kappa q84],
    "offDiagonal_other" -> "0 = kappa T^mu_nu for every other mu != nu (the left-hand sides vanish identically)",
    "evolution_x1_minus_x5" -> eqn[ad2 fEvo, kappa (p3 - pt)],
    "evolution_F" -> expr[fEvo],
    "algebraic_condition" -> eqn[p3 + pt, 2 p8],
    "x8_dependence" -> "the left-hand sides are free of x8 (and of a4 itself), so the source must satisfy d8 rho = d8 p3 = d8 p_t = d8 p8 = 0 and q48 = q84 = 0: every mixed component of T is a function of x4 alone; an x8-dependent source is not compatible with the metric of SPEC section 1",
    "conservation_x4" -> eqn[consX4, 0],
    "conservation_x8" -> eqn[consX8, 0],
    "conservation_reduced" -> "with an x8-independent source and q48 = q84 = 0: rho' = -3 a4' (p3 - p_t) (x4 component) and p3 + p_t = 2 p8 (x8 component), both implied by the field equations (Bianchi identity)",
    "constraint_propagation" -> "d/dx4 (constraint) = 3 a4' (evolution) once rho' = -3 a4' (p3 - p_t) is used (constraint: sum_k alpha_k E^x4_x4 + Lam + kappa rho = 0; evolution: a4'' F - kappa (p3 - p_t) = 0); so for a4' != 0 the evolution equation follows from the constraint and rho' = -3 a4' (p3 - p_t); the x8 equation is an independent first-order relation",
    "sourceRequiredByGivenA4" -> <|"rho" -> expr[srcRho], "p3" -> expr[srcP3], "pt" -> expr[srcPt], "p8" -> expr[srcP8]|>,
    "nullCombinations" -> <|"kappa(rho+p8)" -> expr[nec8], "kappa(rho+p3)" -> expr[nec3], "kappa(rho+pt)" -> expr[nect]|>|>,
  "einstein" -> <|
    "couplings" -> "alpha1 = 1, alpha2 = alpha3 = 0",
    "constraint_x4" -> eqn[(e44 /. einst) + Lam, -kappa rho],
    "space_x1" -> eqn[(e11 /. einst) + Lam, kappa p3],
    "extraTime_x5" -> eqn[(e55 /. einst) + Lam, kappa pt],
    "hidden_x8" -> eqn[(e88 /. einst) + Lam, kappa p8],
    "evolution" -> eqn[ad2 Fein, kappa (p3 - pt)],
    "x4_plus_x8" -> eqn[Expand[(e44 + e88) /. einst] + 2 Lam, kappa (p8 - rho)],
    "nullEnergy" -> eqn[kappa (rho + p8), Expand[nec8 /. einst]],
    "noVacuum" -> "T = 0 has no solution for H > 0 and any Lambda (x4 + x8 components: 36 H^2 + 2 Lambda = 0; x4 - x8: 6 a4'^2 + 6 H^2 = 0)",
    "allowedA4" -> "every C^2 function a4(x4) is allowed, with the source fixed by sourceRequiredByGivenA4 (alpha1 = 1, alpha2 = alpha3 = 0); kappa rho > 0 needs Lambda < -(3 a4'^2 + 21 H^2), and kappa (rho + p8) = -6 (a4'^2 + H^2) < 0 always"|>,
  "linearMember" -> <|
    "a4" -> "a4 = A H x4 + a0 (ad1 = A H, ad2 = 0): 3-space scale factor e^{A H x4}, extra-time scale factor e^{-A H x4} (exponential deflation for A > 0)",
    "requiredSource" -> "rho, p3 = p_t = p8 = p constants (any alpha_k); A is any real number, the source being fixed by A through rho and p below",
    "rho" -> expr[rhoLin], "p" -> expr[pLin],
    "rhoEinstein" -> expr[Expand[rhoLin /. einst]], "pEinstein" -> expr[Expand[pLin /. einst]],
    "rhoPlusPEinstein" -> expr[Factor[Expand[(rhoLin + pLin) /. einst]]],
    "vacuumCondition" -> eqn[6 (AA^2 + 1) H^2 vacReduced, 0],
    "vacuumFactor" -> expr[vacReduced],
    "einsteinGaussBonnetVacuum" -> "alpha3 = 0, alpha1 = 1: A^2 = (1 - 40 alpha2 H^2)/(8 alpha2 H^2), real A iff 0 < alpha2 H^2 <= 1/40; Lambda = -sum_k alpha_k E_(k)^x4_x4 at a4' = A H"|>,
  "fields" -> <|
    "lemmas" -> <|
      "gravityTerm" -> "gamma^mu Omega_mu = 3 H gamma^x8 (canonical spin connection; Omega_x4 = Omega_x8 = 0)",
      "diagonalKinetic" -> "{gamma^mu, Omega_mu} = 0 for each mu (no sum), so K^mu_mu = (1/2)(Psibar gamma^mu d_mu Psi - d_mu Psibar gamma^mu Psi) contains no spin connection; for a configuration independent of x_mu, K^mu_mu = 0",
      "traceOnShell" -> "sum_mu K^mu_mu = (m + U'(S)) S on shell (both statistics), so the on-shell Lagrangian is L = S U'(S) - U(S)"|>,
    "emtConvention" -> "T^mu_nu = sigmaT ( -K^(mu_nu) + delta^mu_nu L ), K^mu_nu = (1/2)(Psibar gamma^mu D_nu Psi - D_nu Psibar gamma^mu Psi), symmetrised; sigmaT = +1 is the convention of SPEC section 4 (homogeneous on-shell states: rho = m S + U, p = S U' - U); if the vielbein variation of the theory branch fixes the opposite overall sign, set sigmaT = -1 everywhere",
    "generalFormulas" -> <|
      "rho" -> "sigmaT ( k4 - L )", "p3" -> "sigmaT ( L - k1 )", "pt" -> "sigmaT ( L - k5 )", "p8" -> "sigmaT ( L - k8 )",
      "q48" -> "-sigmaT K^(x4_x8)",
      "kmu" -> "k_mu = K^mu_mu (no sum) = (1/2)(Psibar gamma^mu d_mu Psi - d_mu Psibar gamma^mu Psi); L = k1+k2+k3+k4+k5+k6+k7+k8 - m S - U(S) (on shell S U'(S) - U(S))",
      "evolution" -> "a4'' F(a4') = kappa sigmaT ( k5 - k1 )",
      "offDiagonal" -> "T^mu_nu = -sigmaT K^(mu_nu) for mu != nu must vanish (0 = kappa T^mu_nu); for the homogeneous condensate these are the 15 three-gamma bilinears listed under dirac16complex00.offDiagonalKinetic",
      "algebraic" -> "2 k8 = k1 + k5 (from p3 + p_t = 2 p8)"|>,
    "dirac16complex00" -> <|
      "statement" -> "classical commuting Phi; k_mu, S, U are classical bilinears",
      "homogeneousCondensate" -> "Phi = Phi(x4) on shell, independent of x1..x3, x5..x8 (d4 Phi = A Phi, A = -gamma^x4 (M - 3 H gamma^x8), M = m + U'(S)): S = Phibar Phi is constant (exact); the diagonal kinetic components are K^x4_x4 = M S and 0 for every other direction, and K^x4_x8 = 0; hence rho = sigmaT (m S + U(S)), p3 = p_t = p8 = sigmaT (S U'(S) - U(S)), q48 = q84 = 0",
      "offDiagonalKinetic" -> offJSON,
      "offDiagonalConditions" -> "the off-diagonal field equations 0 = kappa T^mu_nu (mu != nu, not x4-x8) require the 15 bilinears B_abc = Phibar gamma^a gamma^b gamma^c Phi (frame gammas) to vanish: B_{i x4 x8} = 0 for i = x1..x3, x5..x7 (coefficients proportional to H and to a4'), and, when a4' != 0, B_{i j x4} = 0 for i = x1..x3, j = x5..x7",
      "offDiagonalWitness" -> "exact solutions with all 15 bilinears zero and S != 0 exist: Phi = e^{-i w x4} Phi0, w = sqrt(M^2 - 9 H^2) (M^2 > 9 H^2), Phi0 = v1 + c v2 from the two A-eigenvectors with gamma^x1 gamma^x5 = gamma^x2 gamma^x6 = gamma^x3 gamma^x7 = -1 and +1, c = conj(v1^dagger C v2); checked exactly at (M, H) = (5, 1), (5, 4/3), (-5, 1) (wolfram report, condensate_diagonal_witness_exact)",
      "theoremLinear" -> "Hypotheses: Phi a homogeneous on-shell condensate as above (classical, commuting), satisfying the off-diagonal conditions, a4 in C^2, (alpha1, alpha2, alpha3) != (0,0,0). Then p3 = p_t, so a4'' F(a4') = 0; F is a nonzero polynomial with finitely many roots, a4' is continuous, so a4'' = 0 on every interval: a4 = A H x4 + a0 (linear) with real A. The equations contain A only through A^2 (invariant under A -> -A): the extra times deflate for A > 0, which is a choice of sign (an initial condition), not selected by the equations; A < 0 (inflating extra times) is allowed on the same footing and A = 0 is the static case",
      "einsteinConditions" -> "kappa sigmaT (m S + U) = -(3 A^2 + 21) H^2 - Lambda and kappa sigmaT (S U' - U) = (15 - 3 A^2) H^2 + Lambda",
      "einsteinQuadraticU" -> "U = (lambda/2) S^2, m != 0: kappa sigmaT m S = -(36 H^2 + 2 Lambda) and A^2 = -kappa sigmaT S (m + lambda S)/(6 H^2) - 1 (real A needs kappa sigmaT S (m + lambda S) <= -6 H^2)",
      "lovelockConditions" -> "kappa sigmaT (m S + U) = -(Lam + sum_k alpha_k E_(k)^x4_x4) and kappa sigmaT (S U' - U) = Lam + sum_k alpha_k E_(k)^x8_x8, both at a4' = A H (linearMember.rho, linearMember.p)"|>,
    "dirac16complex" -> <|
      "statement" -> "quantised Psi (SPEC section 6): every bilinear is replaced by the expectation value of the normal-ordered operator in the state, <:k_mu:>, <:S:>, <:U(S):> (note <U(S)> != U(<S>) in general); the trace identity sum_mu <:k_mu:> = <:(m + U'(S)) S:> is assumed to hold for the normal-ordered operators (to be confirmed by the theory branch)",
      "rho" -> "sigmaT ( <:k4:> - <:L:> )", "p3" -> "sigmaT ( <:L:> - <:k1:> )", "pt" -> "sigmaT ( <:L:> - <:k5:> )", "p8" -> "sigmaT ( <:L:> - <:k8:> )",
      "evolution" -> "a4'' F(a4') = kappa sigmaT ( <:k5:> - <:k1:> ): a state with <:k1:> != <:k5:> would drive a4'' if it also met the remaining conditions (p3 + p_t = 2 p8, every expectation value independent of x8, off-diagonal components zero); no such state is constructed in Revision",
      "kohnSham" -> "to be filled by Revision/kohn_sham: rho_KS(x4), p3_KS(x4), p_t_KS(x4), p8_KS(x4) from the occupied Kohn-Sham orbitals (with the Hartree and exchange terms); then constraint: sum_k alpha_k E_(k)^x4_x4 + Lam = -kappa rho_KS; evolution: a4'' F(a4') = kappa (p3_KS - p_t_KS); x8: sum_k alpha_k E_(k)^x8_x8 + Lam = kappa p8_KS; conditions: p3_KS + p_t_KS = 2 p8_KS, the x4-x8 component zero, and every component independent of x8 (a Kohn-Sham source with an x8 profile satisfies the equations only if these hold; otherwise the metric of SPEC section 1 is not an exact solution with that source). Evaluated on the recorded Kohn-Sham states (Revision/field_equations_a4/reports/ks-source-conditions.json): every nonzero ground state depends on x8 and violates p3 + p_t = 2 p8 pointwise and after integration over x8, so none is an admissible source; the Kohn-Sham history a4 = A H x4 is a PRESCRIBED test-field background without back-reaction (the linear member needs p3 = p_t = p8 and constant rho, which the Kohn-Sham gas does not have)",
      "offDiagonal" -> "every off-diagonal expectation value <:T^mu_nu:> (mu != nu) must vanish, in particular the expectation values of the 15 three-gamma bilinears for a homogeneous state",
      "homogeneousSingleMode" -> "if a state has <:k1:> = <:k5:> (e.g. all quanta at zero 3- and extra-time momentum), for every x4 (and the off-diagonal conditions hold), then a4'' F(a4') = 0 and the argument of the dirac16complex00 theorem gives a4 = A H x4 + a0 with real A (A -> -A is a symmetry of the equations; the sign of A is not selected)"|>|>,
  "checksSummary" -> "see reports/wolfram-a4-report.json"|>;

writeJSON[FileNameJoin[{$fieldDir, "a4-equations.json"}], data];

failed = Count[checks, c_ /; c["verdict"] =!= "PASS"];
report = <|"producer" -> "Revision/field_equations_a4/wolfram/verify_field_equations_a4.wls", "spec" -> "Revision/SPEC.md section 5",
   "checkCount" -> Length[checks], "failedCount" -> failed, "verdict" -> If[failed == 0, "PASS", "FAIL"], "checks" -> checks|>;
writeJSON[FileNameJoin[{$fieldDir, "reports", "wolfram-a4-report.json"}], report];
Print["checks: ", Length[checks], ", failed: ", failed];
Scan[If[#["verdict"] =!= "PASS", Print["FAIL ", #["name"], ": ", #["detail"]]] &, checks];
Exit[If[failed == 0, 0, 1]];
