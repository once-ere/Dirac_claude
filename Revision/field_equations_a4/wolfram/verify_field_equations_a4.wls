#!/usr/bin/env wolframscript
(* ::Package:: *)

(* verify_field_equations_a4.wls

   Driver for Revision/field_equations_a4/wolfram/FieldEquationsA4.wl (Revision/SPEC.md section 5).
   Writes, deterministically (LF line endings, no time stamps):
     Revision/field_equations_a4/a4-equations.json                 the equations (exact, InputForm + TeX)
     Revision/field_equations_a4/reports/wolfram-a4-report.json    every check with name, verdict, detail
   Input: Revision/algebra/gammas.json (the author's T16, order x0..x7), the primary representation of every
   spinor statement; FieldEquationsA4.wl reads it strictly on loading.  A missing or malformed gammas.json stops
   the run at once with a line "ERROR  ..." and exit code 1 (no output is written).  So does a missing or
   unreadable FieldEquationsA4.wl, and an output file that cannot be opened for writing gives a line
   "ERROR  cannot write ..." and exit code 1.
   Usage (from the repository root):
     wolframscript -file Revision/field_equations_a4/wolfram/verify_field_equations_a4.wls
   All checks are exact symbolic identities (no floating point).  Exit code 0 iff every check passes.
   Since 2026-10-15 (the user's orders "b4 is a function of x4; b4 is NEVER 1" and "move everything to b4(x4); b4 is
   never 1") every section is derived for GENERAL functions a4(x4) and b4(x4) > 0 of the author's metric with b4;
   until then sections 3 to 6 restricted the tensors to b4 = 1 (the withdrawn earlier metric).
*)

$here = DirectoryName[$InputFileName];
$fieldDir = ExpandFileName[FileNameJoin[{$here, ".."}]]; (* NORMALISED: a ".." left in a path can push it past the Windows limit of 260 characters (MAX_PATH) *)
$revDir = ExpandFileName[FileNameJoin[{$fieldDir, ".."}]];
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
fnRules = {Derivative[1, 0][f_][x4, x0] :> Symbol["d4" <> SymbolName[f]],
   Derivative[0, 1][f_][x4, x0] :> Symbol["d0" <> SymbolName[f]], f_Symbol[x4, x0] :> f, a4[x4] -> a4v};
inp[e_] := ToString[e /. fnRules, InputForm, PageWidth -> Infinity];
bs = FromCharacterCode[92];   (* the backslash *)
texRules = Map[(bs <> "text{" <> #[[1]] <> "}") -> StringReplace[#[[2]], "@" -> bs] &, {
    {"ad1", "(a_4')"}, {"ad2", "a_4''"}, {"bb", "b_4"}, {"bd1", "b_4'"}, {"bd2", "b_4''"}, {"uu", "u"}, {"vv", "v"}, {"be", "@beta"}, {"alpha1", "@alpha_1"}, {"alpha2", "@alpha_2"}, {"alpha3", "@alpha_3"},
    {"Lam", "@Lambda"}, {"AA", "A"}, {"cc", "@cot z"}, {"a4v", "a_4"}, {"pt", "p_t"}, {"p3", "p_3"}, {"p0", "p_0"},
    {"q40", "q_{40}"}, {"q04", "q_{04}"}, {"sigmaT", "@sigma_T"},
    {"d4rho", "@partial_4 @rho"}, {"d0rho", "@partial_0 @rho"}, {"d4p3", "@partial_4 p_3"}, {"d0p3", "@partial_0 p_3"},
    {"d4pt", "@partial_4 p_t"}, {"d0pt", "@partial_0 p_t"}, {"d4p0", "@partial_4 p_0"}, {"d0p0", "@partial_0 p_0"},
    {"d4q40", "@partial_4 q_{40}"}, {"d0q40", "@partial_0 q_{40}"}, {"d4q04", "@partial_4 q_{04}"}, {"d0q04", "@partial_0 q_{04}"}}];
tex[e_] := StringReplace[ToString[TeXForm[e /. fnRules]], texRules];
expr[e_] := <|"input" -> inp[e], "tex" -> tex[e]|>;
eqn[l_, r_] := <|"input" -> inp[l] <> " == " <> inp[r], "tex" -> tex[l] <> " = " <> tex[r]|>;
zero16 = ConstantArray[0, {16, 16}];
coordName[i_] := ToString[FECoords[[i]]];
(* Wolfram positions of the author's coordinates x0..x7: position k + 1 holds xk, so x0 (hidden) = 1, x1, x2, x3 = 2, 3, 4,
   x4 (time) = 5, x5, x6, x7 = 6, 7, 8 *)

(* ======================================================================
   1. Geometry
   ====================================================================== *)
addCheck["metric_is_SPEC_section_1",
  FEMetricDiag === {Cot[6 H x0]^2, E^(2 a4[x4]) Sin[6 H x0]^(1/3), E^(2 a4[x4]) Sin[6 H x0]^(1/3), E^(2 a4[x4]) Sin[6 H x0]^(1/3), -1,
     -E^(-2 a4[x4]) b4[x4] Sin[6 H x0]^(1/3), -E^(-2 a4[x4]) b4[x4] Sin[6 H x0]^(1/3), -E^(-2 a4[x4]) b4[x4] Sin[6 H x0]^(1/3)},
  "g = diag(cot^2 z, e^{2a4} s, e^{2a4} s, e^{2a4} s, -1, -e^{-2a4} b4 s, -e^{-2a4} b4 s, -e^{-2a4} b4 s), s = sin^{1/3} z, z = 6 H x0 (the author's x0..x7): the metric of SPEC section 1 since 2026-10-14 (b4 a function of x4; b4 = 1 was the withdrawn earlier metric)"];
addCheck["sqrt_abs_det_g_is_cos_z",
  Together[FENormal[Times @@ FEMetricDiag] - bb^3 cc^2/(1 + cc^2)] === 0,
  "sqrt|det g| = b4^{3/2} sin z cot z = b4^{3/2} cos z on 0 < z < pi/2 (independent of a4: the 7-volume factor e^{3a4} e^{-3a4} b4^{3/2} = b4^{3/2}, constant in x4 exactly when b4 is)"];

riemannSthirdFree = FreeQ[FERiemannUU, Sin] && FreeQ[FERiemannUU, a4] && FreeQ[FERiemannUU, a0];
addCheck["mixed_riemann_free_of_warp_and_a4",
  riemannSthirdFree,
  "every R^{ab}_{cd} (MTW, computed here from the Christoffel symbols) is a function of H, a4', a4'', b4'/b4, b4''/b4, cot z only (a Laurent polynomial in cot z): the warp sin^{1/3} z and e^{a4} cancel; " <>
   ToString[Length[FERiemannPairs]] <> " nonzero components with a < b, c < d"];
addCheck["riemann_pair_antisymmetry",
  And @@ Flatten[Table[Together[FERiemannUU[[a, b, c, d]] + FERiemannUU[[b, a, c, d]]] === 0 && Together[FERiemannUU[[a, b, c, d]] + FERiemannUU[[a, b, d, c]]] === 0,
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
   FreeQ[Diagonal[Pdirect[[k]]], cc] && And @@ Flatten[Table[If[h != j && !MemberQ[{{5, 1}, {1, 5}}, {h, j}], Pdirect[[k, h, j]] === 0, True], {h, 8}, {j, 8}]] &&
    Together[Pdirect[[k, 5, 1]] /. bd1 -> 0] === 0 && Together[Pdirect[[k, 1, 5]] /. bd1 -> 0] === 0 &&
    Pdirect[[k, 2, 2]] === Pdirect[[k, 3, 3]] === Pdirect[[k, 4, 4]] && Pdirect[[k, 6, 6]] === Pdirect[[k, 7, 7]] === Pdirect[[k, 8, 8]],
   "P_(" <> ToString[k] <> ")^h_j: the diagonal is free of x0 with x1 = x2 = x3 and x5 = x6 = x7; the only nonzero off-diagonal components are x4-x0 and x0-x4, each proportional to b4' (the metric with b4(x4))"],
  {k, 3}];
addCheck["P4_vanishes_pigeonhole",
  FEGKD[{1, 2, 3, 4, 5, 6, 7, 8, 1}, {1, 2, 3, 4, 5, 6, 7, 8, 2}] === 0 && FEGKD[Range[8], Range[8]] === 1,
  "P_(4) would need GKD of 9 indices over 8 values: two equal upper indices give two equal rows of the delta matrix, determinant 0; so k = 1, 2, 3 is the full Lovelock series in 8 dimensions"];

Ek = Table[-Pdirect[[k]]/2^(k + 1), {k, 3}];
EkD = Map[# /. FESymToDeriv &, Ek, {3}];
Do[
  addCheck["E" <> ToString[k] <> "_divergence_free",
   And @@ (FEZeroQ /@ FEDivergence[EkD[[k]]]),
   "nabla_mu E_(" <> ToString[k] <> ")^mu_nu = 0 for nu = x0..x7 (exact; Christoffel symbols of this file; general a4 and b4)"],
  {k, 3}];
(* Since 2026-10-15 (the user's orders "b4 is a function of x4; b4 is NEVER 1" and "move everything to b4(x4)") every
   section below is derived for GENERAL functions a4(x4) and b4(x4) > 0; until then sections 3 to 6 restricted the
   tensors to b4 = 1.  Notation: uu = b4'/b4, vv = (b4'/b4)' (so b4''/b4 = vv + uu^2).  EkG = the general tensors. *)
EkG = Ek;
uvRules = {bd1 -> uu bb, bd2 -> (vv + uu^2) bb};
uv[e_] := Together[Expand[Together[e /. uvRules]]];

(* ======================================================================
   3. The field equations with a general source (general b4)
   ====================================================================== *)
alphas = {alpha1, alpha2, alpha3};
LHSG = Sum[alphas[[k]] EkG[[k]], {k, 3}] + Lam IdentityMatrix[8];
Tsrc = DiagonalMatrix[{p0, p3, p3, p3, -rho, pt, pt, pt}]; Tsrc[[5, 1]] = q40; Tsrc[[1, 5]] = q04;   (* T^x4_x0, T^x0_x4 *)
FEqG = Map[Together, LHSG - kappa Tsrc, {2}];   (* FEqG = 0 are the field equations *)
g11 = Together[LHSG[[2, 2]] - Lam]; g44 = Together[LHSG[[5, 5]] - Lam]; g55 = Together[LHSG[[6, 6]] - Lam];
g00 = Together[LHSG[[1, 1]] - Lam]; g40 = Together[LHSG[[5, 1]]]; g04 = Together[LHSG[[1, 5]]];   (* E^x4_x0, E^x0_x4 *)
{u11, u44, u55, u00} = Expand /@ (uv /@ {g11, g44, g55, g00});
einst = {alpha1 -> 1, alpha2 -> 0, alpha3 -> 0};

addCheck["independent_components",
  And @@ Flatten[Table[If[h != j && !MemberQ[{{5, 1}, {1, 5}}, {h, j}], FEqG[[h, j]] === 0, True], {h, 8}, {j, 8}]] &&
   FEqG[[2, 2]] === FEqG[[3, 3]] === FEqG[[4, 4]] && FEqG[[6, 6]] === FEqG[[7, 7]] === FEqG[[8, 8]],
  "general a4 and b4: the left-hand sides of the 64 components reduce to x0, x1 (= x2 = x3), x4, x5 (= x6 = x7) and the x4-x0 pair; every other off-diagonal left-hand side is 0, so those components read 0 = kappa T^mu_nu"];
addCheck["lovelock_depends_on_b4_through_u_and_v",
  And @@ Flatten[Table[FreeQ[uv[EkG[[k, h, j]]], bb], {k, 3}, {h, 8}, {j, 8}]],
  "every component of E_(1), E_(2), E_(3) depends on b4 only through u = b4'/b4 and v = (b4'/b4)' (with b4''/b4 = v + u^2): a constant factor of b4 is a rescaling of x5, x6, x7"];
addCheck["constraint_first_order",
  FreeQ[u44, ad2] && FreeQ[u44, vv] && FreeQ[u44, cc],
  "the x4 component (constraint) contains only a4' and u = b4'/b4 (no second derivative, no x0): Einstein: " <> inp[Expand[u44 /. einst]]];
jacG = Together[D[{u11 - u55, u00}, {{ad2, vv}}]];
detG = Factor[Together[Det[jacG]]];
addCheck["second_order_system_a4pp_vv",
  And @@ (FreeQ[#, ad2] && FreeQ[#, vv] & /@ Flatten[jacG]) &&
   Together[(u11 - u55) - (jacG[[1, 1]] ad2 + jacG[[1, 2]] vv) - ((u11 - u55) /. {ad2 -> 0, vv -> 0})] === 0 &&
   Together[u00 - (jacG[[2, 1]] ad2 + jacG[[2, 2]] vv) - (u00 /. {ad2 -> 0, vv -> 0})] === 0 &&
   Together[detG /. einst] =!= 0 && Together[(jacG /. einst) - {{2, -1/2}, {0, -3/2}}] === {{0, 0}, {0, 0}},
  "the x1 - x5 and x0 components are linear in (a4'', v) (v = (b4'/b4)') with the Jacobian J (coefficients depending on a4', u, H, alpha_k), det J = " <> inp[detG] <>
   ", not identically zero (Einstein: J = {{2, -1/2}, {0, -3/2}}, det J = -3): where det J != 0 these two components determine a4'' and (b4'/b4)' from the sources; the x4 component is the constraint"];
idG = Together[g11 + g55 - 2 g00];
idGuv = Expand[uv[idG]];
addCheck["algebraic_identity_x1_plus_x5_minus_2x0",
  Expand[idGuv /. {uu -> 0, vv -> 0}] === 0 && Expand[(idGuv /. einst) - (3 uu^2/4 + vv/2)] === 0,
  "sum_k alpha_k (E^x1_x1 + E^x5_x5 - 2 E^x0_x0) = I(a4', a4'', u, v) with I = 0 when u = v = 0; Einstein: I = (3/4) u^2 + v/2 = (b4'/b4)^2/4 + b4''/(2 b4): the field equations give kappa (p3 + p_t - 2 p0) = I (for constant b4 this was the condition p3 + p_t = 2 p0 of the withdrawn metric)"];
Q40 = Together[g40 bb/(cc bd1)];
Q40u = Together[Q40 /. bd1 -> uu bb];
addCheck["offdiagonal_factorises",
  FreeQ[Q40, cc] && FreeQ[Q40u, bb] && Together[g04 + bd1 Q40/(cc bb)] === 0 && Together[g40 /. bd1 -> 0] === 0 &&
   FreeQ[Together[Diagonal[LHSG]], cc],
  "sum_k alpha_k E_(k)^x4_x0 = cot z u Q and sum_k alpha_k E_(k)^x0_x4 = -tan z u Q, u = b4'/b4, Q = " <> inp[Expand[Q40u]] <>
   "; the diagonal components are free of x0: so the source must have q40 = cot z u Q/kappa and q04 = -tan z u Q/kappa (an x0-dependent off-diagonal pair) unless u Q = 0"];
D4[e_] := (D[e /. FESymToDeriv, x4] /. FEDerivToSym);
bianchiG = Together[D4[g44] - 3 ad1 (g11 - g55) - (3/2) (bd1/bb) (g55 - g44) - 6 H (bd1/bb) Q40];
addCheck["constraint_propagation_bianchi",
  bianchiG === 0,
  "d/dx4 [sum_k alpha_k E_(k)^x4_x4] = 3 a4' (E^x1_x1 - E^x5_x5) + (3/2) u (E^x5_x5 - E^x4_x4) + 6 H u Q identically (sums over k with alpha_k; the x4 component of the Bianchi identity with the off-diagonal pair E^x0_x4 = -tan z u Q): " <>
   "with the conservation law below, the derivative of the constraint follows from the other components"];
(* conservation of a general source T(x4, x0) *)
Tgen = DiagonalMatrix[{p0[x4, x0], p3[x4, x0], p3[x4, x0], p3[x4, x0], -rho[x4, x0], pt[x4, x0], pt[x4, x0], pt[x4, x0]}];
Tgen[[5, 1]] = q40[x4, x0]; Tgen[[1, 5]] = q04[x4, x0];
divTG = FENormal /@ FEDivergence[Tgen];
consGX4 = Expand[divTG[[5]]]; consGX0 = Expand[divTG[[1]]];
addCheck["conservation_components",
  And @@ (# === 0 & /@ divTG[[{2, 3, 4, 6, 7, 8}]]) &&
   Together[divTG[[5]] - (-D[rho[x4, x0], x4] - 3 ad1 (p3[x4, x0] - pt[x4, x0]) - (3/2) (bd1/bb) (rho[x4, x0] + pt[x4, x0]) + D[q04[x4, x0], x0] - 6 H q04[x4, x0]/cc)] === 0 &&
   Together[divTG[[1]] - (D[p0[x4, x0], x0] + 3 H cc (2 p0[x4, x0] - p3[x4, x0] - pt[x4, x0]) + D[q40[x4, x0], x4] + (3/2) (bd1/bb) q40[x4, x0])] === 0,
  "nabla_mu T^mu_x4 = -d4 rho - 3 a4' (p3 - p_t) - (3/2)(b4'/b4)(rho + p_t) + d0 q04 - 6 H tan(z) q04 and nabla_mu T^mu_x0 = d0 p0 + 3 H cot(z) (2 p0 - p3 - p_t) + d4 q40 + (3/2)(b4'/b4) q40 (the other components vanish identically)"];
b4setFile = FileNameJoin[{$revDir, "metric_b4", "results", "metric-b4.json"}];
If[!FileExistsQ[b4setFile], Print["ERROR  ", b4setFile, ": not found (run Revision/metric_b4/wolfram/verify_metric_b4.wls)"]; Exit[1]];
b4set = Import[b4setFile, "RawJSON"];
mbE[k_] := Table[FENormal[ToExpression[Lookup[b4set["E" <> ToString[k] <> "Mixed"], coordName[h] <> "," <> coordName[j], "0"]]], {h, 8}, {j, 8}];
addCheck["lovelock_equals_metric_b4_set",
  And @@ Flatten[Table[Together[EkG[[k, h, j]] - mbE[k][[h, j]]] === 0, {k, 3}, {h, 8}, {j, 8}]],
  "all 64 components of E_(1), E_(2), E_(3) for general b4, computed in this file (GKD as Det of the delta matrix over the nonzero R^{ab}_{cd}), equal those of Revision/metric_b4/results/metric-b4.json (MetricB4.wl, compared there with the author's stored outputs of Dirac_Einstein-Lovelock_4+4_Nash.nb)"];
(* Einstein *)
ein44 = Expand[u44 /. einst]; ein11 = Expand[u11 /. einst]; ein55 = Expand[u55 /. einst]; ein00 = Expand[u00 /. einst];
addCheck["einstein_components",
  ein44 === Expand[3 ad1^2 + 21 H^2 - (3/2) ad1 uu - (3/4) uu^2] && ein11 === Expand[ad2 - 3 ad1^2 + 15 H^2 + 3 ad1 uu - (3/2) uu^2 - (3/2) vv] &&
   ein55 === Expand[-ad2 - 3 ad1^2 + 15 H^2 - (3/4) uu^2 - vv] && ein00 === Expand[-3 ad1^2 + 15 H^2 + (3/2) ad1 uu - (3/2) uu^2 - (3/2) vv] &&
   Together[(Q40 /. einst) - 3 H/2] === 0,
  "Einstein (alpha1 = 1, alpha2 = alpha3 = 0), u = b4'/b4, v = u': G^x4_x4 = 3 a4'^2 + 21 H^2 - (3/2) a4' u - (3/4) u^2, G^x1_x1 = a4'' - 3 a4'^2 + 15 H^2 + 3 a4' u - (3/2) u^2 - (3/2) v, " <>
   "G^x5_x5 = -a4'' - 3 a4'^2 + 15 H^2 - (3/4) u^2 - v, G^x0_x0 = -3 a4'^2 + 15 H^2 + (3/2) a4' u - (3/2) u^2 - (3/2) v, G^x4_x0 = (3/2) H cot z u (Q = 3 H/2)"];
nec0 = Expand[u00 - u44];
addCheck["einstein_null_energy_x0",
  Expand[(nec0 /. einst) - (-6 H^2 - 3 ad1^2 - (3/4) (uu - 2 ad1)^2 - (3/2) vv)] === 0,
  "Einstein: kappa (rho + p0) = -6 H^2 - 3 a4'^2 - (3/4)(u - 2 a4')^2 - (3/2) v: negative wherever (b4'/b4)' >= 0 (in particular on every exponential history, v = 0): the source violates the null energy condition along x4 + x0 there"];
addCheck["einstein_offdiagonal_forces_b4_constant",
  Together[(Q40 /. einst) - 3 H/2] === 0 &&
   Reduce[(3/2) H cc uu == kappa q40 && q40 == 0 && uu != 0 && H > 0 && cc > 0 && kappa != 0, {uu, q40}, Reals] === False,
  "Einstein: Q = 3 H/2 != 0, so the x4-x0 equation kappa q40 = (3/2) H cot z b4'/b4 forces b4' = 0 for every source with T^x4_x0 = 0: with b4 not constant (the metric of SPEC section 1) Einstein gravity needs an x0-dependent off-diagonal source q40 = (3/2) H cot z (b4'/b4)/kappa"];
addCheck["einstein_no_vacuum_solution",
  Reduce[ein44 + Lam == 0 && ein11 + Lam == 0 && ein55 + Lam == 0 && ein00 + Lam == 0 && (3/2) H uu == 0 && H > 0, {ad1, ad2, uu, vv, Lam}, Reals] === False,
  "with T = 0 the Einstein equations (any Lambda) have no real solution for H > 0: the x4-x0 component forces u = 0, and then the x4 and x0 components give 36 H^2 + 2 Lambda = 0 and 6 a4'^2 + 6 H^2 = 0"];
jacE = Together[D[{g11 - g55, g00} /. einst, {{ad2, bd2}}]];
addCheck["einstein_second_order_system",
  Together[Det[jacE] bb] =!= 0 && FreeQ[jacE, ad1] && FreeQ[Together[(g11 - g55) /. einst], cc],
  "Einstein: the x1 - x5 and x0 components are linear in (a4'', b4'') with Jacobian " <> inp[jacE] <> " (nonsingular): they determine a4'' and b4''/b4 from the sources; the x4 component is the constraint"];

(* ======================================================================
   4. Exponential histories a4 = A H x4 + a0, b4 = b4(0) e^{beta A H x4} (u = beta A H, v = 0)
   ====================================================================== *)
hist = {ad1 -> AA H, ad2 -> 0, uu -> be AA H, vv -> 0};
{h11, h44, h55, h00} = Factor /@ ({u11, u44, u55, u00} /. hist);
hQ = Factor[Together[Q40u /. hist]];
srcRho = -(h44 + Lam)/kappa; srcP3 = (h11 + Lam)/kappa; srcPt = (h55 + Lam)/kappa; srcP0 = (h00 + Lam)/kappa;
srcQ40 = cc be AA H hQ/kappa;
addCheck["exponential_history_required_source",
  And @@ (FreeQ[#, cc] && FreeQ[#, x4] && FreeQ[#, x0] & /@ {h11, h44, h55, h00, hQ}),
  "on a4 = A H x4 + a0, b4 = b4(0) e^(beta A H x4) the field equations require constant rho, p3, p_t, p0 (formulas in a4-equations.json, key exponentialHistory) and the off-diagonal pair kappa q40 = cot z beta A H Q(A, beta), " <>
   "kappa q04 = -tan z beta A H Q(A, beta), Q(A, beta) = " <> inp[hQ] <> " (any alpha_k, Lambda); the pressures are not equal in general"];
addCheck["einstein_exponential_history_offdiagonal_source",
  Together[(hQ /. einst) - 3 H/2] === 0,
  "Einstein: on every exponential history with beta A != 0 (b4 not constant) the source needs kappa q40 = (3/2) beta A H^2 cot z != 0"];
authW = {alpha1 -> 1/H^2, alpha2 -> (1/32)/H^4, alpha3 -> (1/1152)/H^6, Lam -> -10};
hQauth = Factor[Together[hQ /. authW]];
addCheck["author_weights_branch",
  Together[(hQauth /. AA -> 1) - 3 be (3 be - 4)/(64 H)] === 0,
  "the author's weights of Dirac_Einstein-Lovelock_4+4_Nash.nb (w1 = 1, w2 = 1/32, w3 = 1/1152, Lambda_author = 10, i.e. alpha_k = w_k/H^(2k), Lam = -10): Q(A, beta) = " <> inp[hQauth] <>
   "; at A = 1 (a4 = H x4) Q = 3 beta (3 beta - 4)/(64 H), so q40 = 0 exactly for beta = 0 (b4 constant, excluded) and beta = 4/3: the history a4 = H x4, b4 = b4(0) e^((4/3) H x4) of SPEC section 1"];
histSrc = Together[{-(h44 + Lam), h11 + Lam, h55 + Lam, h00 + Lam} /. authW /. {AA -> 1, be -> 4/3}];
addCheck["author_weights_history_source",
  histSrc === {-2/27, -2/9, -22/27, -14/27},
  "on the history a4 = H x4, b4 = b4(0) e^((4/3) H x4) with the author's weights the field equations require the constant source kappa (rho, p3, p_t, p0) = (-2/27, -2/9, -22/27, -14/27) and q40 = q04 = 0: it is NOT a vacuum solution (and the pressures differ); the record uses it as a PRESCRIBED background (SPEC section 1)"];
numer[e_] := Numerator[Together[e]];
vacAuth = numer /@ ({h44 + Lam, h11 + Lam, h55 + Lam, h00 + Lam, be hQ} /. authW);
addCheck["author_weights_no_vacuum_with_b4_not_constant",
  Reduce[(And @@ Thread[vacAuth == 0]) && H > 0, {AA, be}, Reals] === (H > 0 && ((AA == -1 && be == 0) || (AA == 1 && be == 0))),
  "the author's weights: an exponential history is a vacuum solution exactly for beta = 0 (b4 constant: the withdrawn metric) with A = +-1 (the author's solution a4 = +-H x4); no exponential history with b4 not constant is a vacuum solution (the general theorem: Revision/metric_b4/results/vacuum-b4.json)"];
egb = {alpha1 -> 1, alpha3 -> 0};
vacEGB = numer /@ ({h44 + Lam, h11 + Lam, h55 + Lam, h00 + Lam, hQ} /. egb);
brEGB = (be == 4 && alpha2 == 1/(40 H^2 (1 - AA^2))) || (be == 2 (1 + AA^2)/AA^2 && alpha2 == -AA^2/(4 H^2 (AA^2 - 1)^2));
lamEGB = Together[Lam /. First[Solve[vacEGB[[1]] == 0, Lam]]];
egbSys = (And @@ Thread[vacEGB == 0]) && AA != 0 && be != 0 && H > 0;
addCheck["egb_exponential_vacuum_branches",
  Reduce[egbSys && !brEGB, {AA, be, Lam, alpha2}, Reals] === False &&
   Reduce[brEGB && AA != 0 && AA^2 != 1 && H > 0 && Lam == lamEGB && !(And @@ Thread[vacEGB == 0]), {AA, be, Lam, alpha2}, Reals] === False,
  "Einstein-Gauss-Bonnet (alpha1 = 1, alpha3 = 0): the vacuum exponential histories with b4 not constant (A beta != 0) are exactly beta = 4 with alpha2 = 1/(40 H^2 (1 - A^2)) and beta = 2 (1 + A^2)/A^2 with alpha2 = -A^2/(4 H^2 (A^2 - 1)^2) < 0 (A^2 != 1), " <>
   "Lambda = -E^x4_x4 at the history: a vacuum with b4(x4) exists only for these tuned couplings"];

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
   am = -gc[[5]] . (MM IdentityMatrix[16] - gdir);     (* d4 Phi = A Phi, since (gamma^x4)^-1 = -gamma^x4; x4 = position 5 *)
   dP[nu_] := If[nu == 5, am, zero16] + om[[nu]];
   dPb[nu_] := If[nu == 5, Transpose[am] . Cm, zero16] - Cm . om[[nu]];
   nm = Table[Map[FENormal, (1/2) (Cm . gc[[mu]] . dP[nu] - dPb[nu] . gc[[mu]]), {2}], {mu, 8}, {nu, 8}];
   ns = Table[Map[FENormal, (1/2) (nm[[mu, nu]] + (gd[[nu]]/gd[[mu]]) nm[[nu, mu]]), {2}], {mu, 8}, {nu, 8}];
   <|"gC" -> gc, "Om" -> om, "Gdirac" -> gdir, "Amat" -> am, "Nmat" -> nm, "NmatSym" -> ns|>];
subsets = Subsets[Range[8]];
basisMatIn[g_List, Cm_, s_List] := Cm . If[s === {}, IdentityMatrix[16], Dot @@ (g[[#]] & /@ s)];
offDiagonalDecomposition[g_List, Cm_, ns_] := Module[{binv, dec, pairs},
   binv = Association[(# -> Inverse[basisMatIn[g, Cm, #]]) & /@ subsets];
   dec[N_] := Select[Association[(# -> Together[Tr[binv[#] . N]/16]) & /@ subsets], # =!= 0 &];
   pairs = Select[Flatten[Table[{mu, nu}, {mu, 8}, {nu, 8}], 1], #[[1]] != #[[2]] && ns[[#[[1]], #[[2]]]] =!= zero16 &];
   Association[(# -> dec[ns[[#[[1]], #[[2]]]]]) & /@ pairs]];

primG = condensateKinetic[FEGammaFrame, FEC];
gF = FEGammaFrame; gC = primG["gC"]; Om = primG["Om"];
addCheck["fixture_author_T16_read",
  fx["coordinates"] === {"x0", "x1", "x2", "x3", "x4", "x5", "x6", "x7"} && fx["notebookFrameIndex"] === {0, 1, 2, 3, 4, 5, 6, 7} &&
   fx["eta"] === Diagonal[FEEta] && Length[gF] == 8 && And @@ (MatrixQ[#, IntegerQ[#] || Head[#] === Rational &] && Dimensions[#] == {16, 16} & /@ gF) &&
   fx["S"] === FESab && fx["Gamma"] === Dot @@ gF[[{1, 2, 3, 4, 5, 6, 7, 8}]] && fx["B"] === -I fx["C"] . gF[[5]],
  "Revision/algebra/gammas.json (sha256 " <> fx["sha256"] <> ") read with strict parsing (every entry a JSON integer or a string \"p/q\" in lowest terms; a missing or malformed file stops the run with an ERROR line and exit code 1): coordinates x0..x7 (the author's), notebook frame index {0, 1, 2, 3, 4, 5, 6, 7} (gamma^(xk) = T16[k]), eta = diag(1,1,1,1,-1,-1,-1,-1), 8 real exact 16 x 16 matrices; the fixture's S, Gamma and B equal (1/4)[gamma^a, gamma^b], gamma^x0 gamma^x1 ... gamma^x7 and -i C gamma^x4 of these gammas: the primary representation of every spinor statement below"];
addCheck["clifford_relations_author_T16",
  And @@ Flatten[Table[gF[[a]] . gF[[b]] + gF[[b]] . gF[[a]] == 2 FEEta[[a, b]] IdentityMatrix[16], {a, 8}, {b, 8}]],
  "the author's T16 (primary representation, Revision/algebra/gammas.json) satisfies {gamma^a, gamma^b} = 2 eta^ab, eta = diag(1,1,1,1,-1,-1,-1,-1)"];
addCheck["C_properties_author_T16",
  FEC === fx["C"] && FEC === Transpose[FEC] && FEC . FEC === IdentityMatrix[16] && And @@ Table[Transpose[FEC . gF[[a]]] === -FEC . gF[[a]], {a, 8}],
  "C = gamma^x0 gamma^x1 gamma^x2 gamma^x3 of the author's T16 equals the fixture's C (the notebook's sigma16, order x0..x7) and is real symmetric, C^2 = 1, C gamma^a antisymmetric (SPEC section 2); every bilinear below uses this C"];
addCheck["clifford_relations_own_rep",
  And @@ Flatten[Table[gR[[a]] . gR[[b]] + gR[[b]] . gR[[a]] == 2 FEEta[[a, b]] IdentityMatrix[16], {a, 8}, {b, 8}]],
  "comparison representation only (not used for any result): the representation built in FieldEquationsA4.wl (Cl(1,1) tensor-graded four times; real 16 x 16) satisfies {gamma^a, gamma^b} = 2 eta^ab, eta = diag(1,1,1,1,-1,-1,-1,-1)"];
addCheck["C_properties_own_rep",
  CR === Transpose[CR] && CR . CR === IdentityMatrix[16] && And @@ Table[Transpose[CR . gR[[a]]] === -CR . gR[[a]], {a, 8}],
  "comparison representation only: C = gamma^x0 gamma^x1 gamma^x2 gamma^x3 is real symmetric, C^2 = 1, C gamma^a antisymmetric (the properties SPEC section 2 requires)"];
kBasis = FEIntertwinerBasis[gR, gF];   (* K . gamma_R^a == gamma_T16^a . K *)
kMat = If[Length[kBasis] == 1, First[kBasis], zero16];
kc = (Transpose[kMat] . kMat)[[1, 1]];
addCheck["representations_equivalent_author_T16_own_rep",
  Length[kBasis] == 1 && kc > 0 && Transpose[kMat] . kMat === kc IdentityMatrix[16] &&
   And @@ Table[kMat . gR[[a]] === gF[[a]] . kMat, {a, 8}] && kMat . CR === FEC . kMat,
  "exact (NullSpace over the rationals): the intertwiners K with K gamma_R^a = gamma_T16^a K for a = x0..x7 (gamma_R the comparison representation) form a space of dimension " <>
   ToString[Length[kBasis]] <> ", and K^T K = " <> ToString[kc, InputForm] <> " I16 (K is " <> ToString[Sqrt[kc], InputForm] <>
   " times an orthogonal matrix) with K C_R = C_T16 K: the two representations are equivalent, so every trace of a product of gammas (in particular every coefficient in the Clifford basis C gamma^I) is the same in both"];
spinAnti = And @@ Flatten[Table[FENormal[FESpinConnLow[[mu, a, b]] + FESpinConnLow[[mu, b, a]]] === 0, {mu, 8}, {a, 8}, {b, 8}]];
addCheck["spin_connection_antisymmetric", spinAnti, "omega_mu ab = -omega_mu ba for the canonical spin connection of this metric (vielbein postulate; general a4 and b4)"];
addCheck["Omega_x0_Omega_x4_vanish",
  Om[[5]] === zero16 && Om[[1]] === zero16,
  "Omega_x0 = Omega_x4 = 0 (the diagonal vielbein has no x4 component that varies, and e^x0 depends on x0 only; general b4)"];
anticommOm = Table[Map[FENormal, gC[[mu]] . Om[[mu]] + Om[[mu]] . gC[[mu]], {2}], {mu, 8}];
addCheck["gamma_mu_anticommutes_with_Omega_mu_no_sum",
  And @@ (# === zero16 & /@ anticommOm),
  "{gamma^mu, Omega_mu} = 0 for each mu separately (no sum; general b4): the spin connection drops out of every diagonal kinetic component K^mu_mu = (1/2)(Psibar gamma^mu d_mu Psi - d_mu Psibar gamma^mu Psi)"];
Gdirac = primG["Gdirac"];
addCheck["gravity_term_gamma_mu_Omega_mu",
  Map[Together, Gdirac - (3 H gF[[1]] + (3/4) (bd1/bb) gF[[5]]), {2}] === zero16,
  "gamma^mu Omega_mu = 3 H gamma^x0 + (3/4)(b4'/b4) gamma^x4 exactly (frame gammas; the a4' terms of the 3 inflating and 3 deflating directions cancel, the b4' terms of the extra times add; independent of a4 and x0)"];
(* the homogeneous condensate: Phi(x4) independent of x0..x3, x5..x7, on shell gamma^mu D_mu Phi = M Phi, M = m + U'(S) real *)
g4 = gC[[5]];   (* gamma^x4 *)
Amat = primG["Amat"];      (* -g4 . (MM I16 - Gdirac): d4 Phi = Amat Phi *)
A0mat = -gF[[5]] . (MM IdentityMatrix[16] - 3 H gF[[1]]);   (* the b4-free part *)
addCheck["condensate_equation_x0_consistent",
  FreeQ[Amat, x0] && FreeQ[Amat, cc] && Map[Together, g4 . Amat + Gdirac - MM IdentityMatrix[16], {2}] === zero16 &&
   Map[Together, Amat - (A0mat - (3/4) (bd1/bb) IdentityMatrix[16]), {2}] === zero16,
  "for Phi = Phi(x4) the equation is d4 Phi = A Phi with A = A0 - (3/4)(b4'/b4) I16, A0 = -gamma^x4 (M - 3 H gamma^x0), free of x0: Phi = b4^(-3/4) chi with d4 chi = A0 chi, an x0-independent solution exists"];
addCheck["condensate_S_b4_three_halves_constant",
  Map[Together, FEC . Amat + Transpose[Amat] . FEC + (3/2) (bd1/bb) FEC, {2}] === zero16 && Expand[FEC . A0mat + Transpose[A0mat] . FEC] === zero16,
  "C A + A^T C = -(3/2)(b4'/b4) C (M real), so d4 S = -(3/2)(b4'/b4) S: b4^(3/2) S = S sqrt|det g|/cos z is constant along x4 (exact, for every initial Phi); S = b4^(-3/2) S0"];
addCheck["condensate_adjoint_equation",
  Map[Together, Transpose[Amat] . FEC . g4 - FEC . Sum[Om[[mu]] . gC[[mu]], {mu, 8}] + MM FEC, {2}] === zero16,
  "(D_mu Phibar) gamma^mu = -M Phibar holds for the condensate (the adjoint of the field equation; general b4)"];
Nmat = primG["Nmat"];
NmatSym = primG["NmatSym"];
addCheck["condensate_kinetic_tensor_diagonal",
  Map[Together, NmatSym[[5, 5]] - MM FEC, {2}] === zero16 && And @@ Table[Map[Together, NmatSym[[mu, mu]], {2}] === zero16, {mu, {1, 2, 3, 4, 6, 7, 8}}] &&
   Map[Together, NmatSym[[5, 1]], {2}] === zero16 && Map[Together, NmatSym[[1, 5]], {2}] === zero16,
  "for the condensate the symmetrised kinetic tensor has K^x4_x4 = M S, K^mu_mu = 0 for mu = x0..x3, x5..x7, and K^x4_x0 = K^x0_x4 = 0, exactly, for every Phi (general b4; the b4' terms of Phi and Phibar cancel)"];
basisMat[s_List] := basisMatIn[gF, FEC, s];
offDecomp = offDiagonalDecomposition[gF, FEC, Map[Together, NmatSym, {4}]];
offPairs = Keys[offDecomp];
recon = And @@ Table[Map[Together, Total[KeyValueMap[#2 basisMat[#1] &, offDecomp[pq]]] - NmatSym[[pq[[1]], pq[[2]]]], {2}] === zero16, {pq, offPairs}];
triples = Union[Flatten[Keys /@ Values[offDecomp], 1]];
addCheck["condensate_offdiagonal_are_three_gamma_bilinears",
  recon && And @@ (Length[#] == 3 & /@ triples) &&
   Sort[triples] === Sort[Join[Table[Sort[{i, 5, 1}], {i, {2, 3, 4, 6, 7, 8}}], Flatten[Table[Sort[{i, j, 5}], {i, 2, 4}, {j, 6, 8}], 1]]],
  "the nonzero off-diagonal kinetic components of the condensate are exactly multiples of the 15 bilinears B_abc = Phibar gamma^a gamma^b gamma^c Phi with {a,b,c} = {i, x4, x0} (i = x1..x3, x5..x7) and {i, j, x4} (i = x1..x3, j = x5..x7), with coefficients depending on H, a4' and b4'/b4; " <>
   ToString[Length[offPairs]] <> " ordered pairs (mu, nu) are nonzero"];
cmpRG = condensateKinetic[gR, CR];
offDecompR = offDiagonalDecomposition[gR, CR, Map[Together, cmpRG["NmatSym"], {4}]];
addCheck["offdiagonal_coefficients_representation_independent",
  Map[Together, cmpRG["Gdirac"] - (3 H gR[[1]] + (3/4) (bd1/bb) gR[[5]]), {2}] === zero16 && Keys[offDecompR] === offPairs &&
   And @@ Table[Keys[offDecompR[pq]] === Keys[offDecomp[pq]] &&
      And @@ (Together[#] === 0 & /@ (Values[offDecompR[pq]] - Values[offDecomp[pq]])), {pq, offPairs}],
  "the comparison representation (Cl(1,1)^(x)4, built in FieldEquationsA4.wl), run through the same condensate pipeline, gives gamma^mu Omega_mu = 3 H gamma^x0 + (3/4)(b4'/b4) gamma^x4, the same " <>
   ToString[Length[offPairs]] <> " nonzero ordered pairs (mu, nu), the same three-gamma bilinears and exactly the same coefficients (general b4) as the author's T16 (primary): the off-diagonal coefficients in a4-equations.json are representation independent"];
(* exact witnesses: Phi = b4^(-3/4) Exp[-I w x4] Phi0, Phi0 = v1 + c v2 in the A0-eigenspace with all 15 bilinears zero and S != 0 *)
witness[mval_, hval_] := Module[{w, Am, ex, v1, v2, sv, ph, ok, sval, conds, cv, phiF, resid},
   w = Sqrt[mval^2 - 9 hval^2];
   Am = A0mat /. {MM -> mval, H -> hval};
   (* gamma^x1 gamma^x5, gamma^x2 gamma^x6, gamma^x3 gamma^x7: positions (2, 6), (3, 7), (4, 8) *)
   ex[e_] := NullSpace[Join[Am + I w IdentityMatrix[16], gF[[2]] . gF[[6]] - e IdentityMatrix[16],
       gF[[3]] . gF[[7]] - e IdentityMatrix[16], gF[[4]] . gF[[8]] - e IdentityMatrix[16]]];
   v1 = First[ex[-1]]; v2 = First[ex[1]];
   sv = Conjugate[v1] . FEC . v2; cv = Conjugate[sv];
   ph = v1 + cv v2;
   sval = Simplify[Conjugate[ph] . FEC . ph];
   conds = Table[FullSimplify[Conjugate[ph] . (basisMat[t]) . ph], {t, triples}];
   (* the full field Phi(x4) = b4^(-3/4) e^(-i w x4) Phi0 solves d4 Phi = A Phi for every b4 *)
   phiF = b4[x4]^(-3/4) Exp[-I w x4] ph;
   resid = Together[(D[phiF, x4] - ((Amat /. {MM -> mval, H -> hval}) /. FESymToDeriv) . phiF)];
   ok = Length[ex[-1]] == 1 && Length[ex[1]] == 1 && Expand[Am . ph + I w ph] === ConstantArray[0, 16] && resid === ConstantArray[0, 16] &&
     And @@ (# === 0 & /@ conds) && sval =!= 0 && Element[sval, Reals] &&
     And @@ Table[Simplify[Conjugate[ph] . (NmatSym[[pq[[1]], pq[[2]]]] /. {MM -> mval, H -> hval}) . ph] === 0, {pq, offPairs}];
   {ok, w, sval}];
wit = {witness[5, 1], witness[5, 4/3], witness[-5, 1]};
addCheck["condensate_diagonal_witness_exact",
  And @@ (#[[1]] & /@ wit),
  "exact Gaussian-rational witnesses (M, H) = (5, 1), (5, 4/3), (-5, 1): Phi = b4^(-3/4) e^{-i w x4} Phi0 with w = sqrt(M^2 - 9 H^2) = " <> inp[#[[2]] & /@ wit] <>
   ", Phi0 = v1 + c v2 (v1, v2 the A0-eigenvectors with gamma^x1 gamma^x5 = gamma^x2 gamma^x6 = gamma^x3 gamma^x7 = -1 and +1, c = conj(v1^dagger C v2)), solves the condensate equation for every b4; all 15 three-gamma bilinears and every off-diagonal kinetic component vanish for every a4, a4', b4; " <>
   "b4^(3/2) S = " <> inp[#[[3]] & /@ wit] <> " != 0"];
(* the condensate as a source: rho = sigmaT (m S + U), p3 = p_t = p0 = sigmaT (S U' - U), q40 = q04 = 0 *)
condAuth = numer /@ ({be hQ, h11 - h55, h11 - h00} /. authW);
condEGB = numer /@ ({hQ, h11 - h55, h11 - h00} /. egb);
brEGBc = (be == 4 && alpha2 == 1/(40 H^2 (1 - AA^2))) || (be == 2 (1 + AA^2)/AA^2 && alpha2 == -AA^2/(4 H^2 (AA^2 - 1)^2));
addCheck["condensate_source_with_b4_not_constant",
  Together[(Q40 /. einst) - 3 H/2] === 0 &&
   Reduce[(And @@ Thread[condAuth == 0]) && be != 0 && H > 0, {AA, be}, Reals] === False &&
   Reduce[(And @@ Thread[condEGB == 0]) && AA != 0 && be != 0 && H > 0 && !brEGBc, {AA, be, alpha2}, Reals] === False,
  "a source with q40 = q04 = 0 and p3 = p_t = p0, such as the homogeneous condensate (K^x4_x0 = 0, K^mu_mu = 0 for mu != x4), with b4 NOT constant: Einstein: impossible (the x4-x0 equation forces b4' = 0); " <>
   "the author's weights: no exponential history a4 = A H x4 + a0, b4 ~ e^(beta A H x4) with beta != 0 (Q = 0 and equal pressures have no common real solution); Einstein-Gauss-Bonnet: only on the two tuned vacuum branches of egb_exponential_vacuum_branches. " <>
   "Histories that are not exponential are not decided here"];

(* ======================================================================
   6. a4-equations.json
   ====================================================================== *)
offJSON = Table[<|"component" -> "K^" <> coordName[pq[[1]]] <> "_" <> coordName[pq[[2]]] <> " (symmetrised)",
     "terms" -> KeyValueMap[<|"bilinear" -> "Phibar " <> StringRiffle[("gamma^" <> coordName[#]) & /@ #1, " "] <> " Phi", "coefficient" -> expr[uv[#2]]|> &, offDecomp[pq]]|>,
   {pq, offPairs}];
compEuv[k_] := <|"x0x0" -> expr[Expand[uv[EkG[[k, 1, 1]]]]], "x1x1" -> expr[Expand[uv[EkG[[k, 2, 2]]]]], "x4x4" -> expr[Expand[uv[EkG[[k, 5, 5]]]]],
   "x5x5" -> expr[Expand[uv[EkG[[k, 6, 6]]]]], "x4x0" -> expr[uv[EkG[[k, 5, 1]]]], "x0x4" -> expr[uv[EkG[[k, 1, 5]]]]|>;
compEG[k_] := <|"x0x0" -> expr[Expand[EkG[[k, 1, 1]]]], "x1x1" -> expr[Expand[EkG[[k, 2, 2]]]], "x4x4" -> expr[Expand[EkG[[k, 5, 5]]]],
   "x5x5" -> expr[Expand[EkG[[k, 6, 6]]]], "x4x0" -> expr[EkG[[k, 5, 1]]], "x0x4" -> expr[EkG[[k, 1, 5]]]|>;
data = <|
  "title" -> "Einstein-Lovelock field equations for a4[x4] and b4[x4] in the primordial metric with b4 (Revision/SPEC.md section 5), for GENERAL functions a4 and b4 > 0 (since 2026-10-15; b4 is never set to 1); the key b4 holds the formulas of 2026-10-14 in the raw variables b4, b4', b4'' for the readers that use them",
  "producer" -> "Revision/field_equations_a4/wolfram/verify_field_equations_a4.wls (with FieldEquationsA4.wl)",
  "conventions" -> <|
    "coordinates" -> "the author's coordinates x0..x7: x0 = hidden direction, z = 6 H x0 in (0, pi/2); x1, x2, x3 = 3-space (scale factor e^{a4} sin^{1/6} z); x4 = time; x5, x6, x7 = extra times, time-like, deflating (scale factor e^{-a4} b4^{1/2} sin^{1/6} z)",
    "symbols" -> "ad1 = a4'(x4), ad2 = a4''(x4), uu = b4'/b4, vv = (b4'/b4)' (b4''/b4 = vv + uu^2), H > 0, alpha1..alpha3 = Lovelock couplings, Lam = Lambda, kappa = gravitational coupling, cc = cot z; AA, be = the parameters of an exponential history; d4f, d0f = partial derivatives of f with respect to x4, x0",
    "curvature" -> "MTW: R^a_{bcd} = d_c Gamma^a_{bd} - d_d Gamma^a_{bc} + Gamma^a_{ce} Gamma^e_{bd} - Gamma^a_{de} Gamma^e_{bc}",
    "lovelock" -> "P_(k)^h_j = GKD[{h,h1..h2k},{j,j1..j2k}] R^{j1j2}_{h1h2} ... R^{j(2k-1)j2k}_{h(2k-1)h2k}; E_(k) = -P_(k)/2^(k+1); E_(1) = G",
    "fieldEquations" -> "sum_{k=1}^{3} alpha_k E_(k)^mu_nu + Lam delta^mu_nu = kappa T^mu_nu",
    "source" -> "T^mu_nu = diag(p0, p3, p3, p3, -rho, p_t, p_t, p_t) (order x0..x7) + q40 (mu = x4, nu = x0) + q04 (mu = x0, nu = x4); rho = -T^x4_x4, p_mu = T^mu_mu (no sum)"|>,
  "lovelockTensors" -> <|"E1" -> compEuv[1], "E2" -> compEuv[2], "E3" -> compEuv[3],
    "allOtherComponents" -> "x2x2 = x3x3 = x1x1, x6x6 = x7x7 = x5x5; the only nonzero off-diagonal components are x4x0 and x0x4 (proportional to b4'); every component depends on b4 only through uu = b4'/b4 and vv = (b4'/b4)' (exact, all 64 components checked)"|>,
  "generalSource" -> <|
    "constraint_x4" -> eqn[u44 + Lam, -kappa rho],
    "space_x1_eq_x2_eq_x3" -> eqn[u11 + Lam, kappa p3],
    "extraTime_x5_eq_x6_eq_x7" -> eqn[u55 + Lam, kappa pt],
    "hidden_x0" -> eqn[u00 + Lam, kappa p0],
    "offDiagonal_x4x0" -> eqn[cc uu Q40u, kappa q40],
    "offDiagonal_x0x4" -> eqn[-uu Q40u/cc, kappa q04],
    "offDiagonalFactor_Q" -> expr[Expand[Q40u]],
    "offDiagonal_other" -> "0 = kappa T^mu_nu for every other mu != nu (the left-hand sides vanish identically)",
    "secondOrderSystem" -> "the x1 - x5 and x0 components are linear in (ad2, vv) with Jacobian J; det J below; where det J != 0 they determine a4'' and (b4'/b4)' from the sources, and the x4 component is the constraint",
    "secondOrderJacobian" -> expr[jacG],
    "secondOrderJacobianDet" -> expr[detG],
    "identity_x1_plus_x5_minus_2x0" -> eqn[idGuv, kappa (p3 + pt - 2 p0)],
    "x0_dependence" -> "the diagonal left-hand sides are free of x0 (and of a4 itself), so the diagonal source must satisfy d0 rho = d0 p3 = d0 p_t = d0 p0 = 0; the off-diagonal pair must be kappa q40 = cot z uu Q, kappa q04 = -tan z uu Q: unless uu Q = 0 the source has an x0-dependent off-diagonal pair",
    "conservation_x4" -> eqn[consGX4, 0],
    "conservation_x0" -> eqn[consGX0, 0],
    "constraint_propagation" -> "d/dx4 [sum_k alpha_k E^x4_x4] = 3 ad1 (E^x1_x1 - E^x5_x5) + (3/2) uu (E^x5_x5 - E^x4_x4) + 6 H uu Q identically (the x4 component of the Bianchi identity)",
    "sourceRequiredByGivenHistory" -> <|"rho" -> expr[-(u44 + Lam)/kappa], "p3" -> expr[(u11 + Lam)/kappa], "pt" -> expr[(u55 + Lam)/kappa], "p0" -> expr[(u00 + Lam)/kappa],
      "q40" -> expr[cc uu Q40u/kappa], "q04" -> expr[-uu Q40u/(cc kappa)]|>,
    "nullCombinations" -> <|"kappa(rho+p0)" -> expr[Expand[u00 - u44]], "kappa(rho+p3)" -> expr[Expand[u11 - u44]], "kappa(rho+pt)" -> expr[Expand[u55 - u44]]|>|>,
  "einstein" -> <|
    "couplings" -> "alpha1 = 1, alpha2 = alpha3 = 0",
    "constraint_x4" -> eqn[ein44 + Lam, -kappa rho],
    "space_x1" -> eqn[ein11 + Lam, kappa p3],
    "extraTime_x5" -> eqn[ein55 + Lam, kappa pt],
    "hidden_x0" -> eqn[ein00 + Lam, kappa p0],
    "offDiagonal_x4x0" -> eqn[(3/2) H cc uu, kappa q40],
    "nullEnergy" -> eqn[kappa (rho + p0), -6 H^2 - 3 ad1^2 - (3/4) (uu - 2 ad1)^2 - (3/2) vv],
    "offDiagonalStatement" -> "Q = 3 H/2: a source with q40 = 0 forces b4' = 0; with b4 not constant Einstein gravity needs kappa q40 = (3/2) H cot z b4'/b4",
    "noVacuum" -> "T = 0 has no solution for H > 0 and any Lambda (the x4-x0 component forces uu = 0, then the x4 and x0 components give 36 H^2 + 2 Lambda = 0 and 6 a4'^2 + 6 H^2 = 0)",
    "secondOrderJacobian" -> expr[jacE]|>,
  "exponentialHistory" -> <|
    "history" -> "a4 = AA H x4 + a0, b4 = b4(0) e^(be AA H x4): ad1 = AA H, ad2 = 0, uu = be AA H, vv = 0 (3-space scale factor e^{AA H x4}, extra-time scale factor e^{-(1 - be/2) AA H x4})",
    "requiredSource" -> <|"rho" -> expr[srcRho], "p3" -> expr[srcP3], "pt" -> expr[srcPt], "p0" -> expr[srcP0], "q40" -> expr[srcQ40], "Q" -> expr[hQ]|>,
    "einstein" -> "Q = 3 H/2: kappa q40 = (3/2) be AA H^2 cot z != 0 for be AA != 0",
    "authorWeights" -> <|
      "weights" -> "alpha_k = w_k/H^(2k), w = (1, 1/32, 1/1152), Lam = -10 (Dirac_Einstein-Lovelock_4+4_Nash.nb, Out[134]/Out[135])",
      "Q" -> expr[hQauth],
      "branch" -> "at AA = 1: Q = 3 be (3 be - 4)/(64 H), so q40 = 0 exactly for be = 0 (b4 constant, excluded) and be = 4/3",
      "historySource" -> "AA = 1, be = 4/3: kappa (rho, p3, p_t, p0) = (-2/27, -2/9, -22/27, -14/27), q40 = q04 = 0 (not a vacuum; a prescribed background, SPEC section 1)",
      "vacuum" -> "an exponential history is a vacuum solution exactly for be = 0 (b4 constant) and AA = +-1; none with b4 not constant"|>,
    "einsteinGaussBonnetVacuum" -> "alpha1 = 1, alpha3 = 0: vacuum exponential histories with b4 not constant exactly for be = 4, alpha2 = 1/(40 H^2 (1 - AA^2)) and for be = 2 (1 + AA^2)/AA^2, alpha2 = -AA^2/(4 H^2 (AA^2 - 1)^2) < 0 (AA^2 != 1), Lambda = -E^x4_x4"|>,
  "fields" -> <|
    "lemmas" -> <|
      "gravityTerm" -> "gamma^mu Omega_mu = 3 H gamma^x0 + (3/4)(b4'/b4) gamma^x4 (canonical spin connection; Omega_x4 = Omega_x0 = 0)",
      "diagonalKinetic" -> "{gamma^mu, Omega_mu} = 0 for each mu (no sum), so K^mu_mu = (1/2)(Psibar gamma^mu d_mu Psi - d_mu Psibar gamma^mu Psi) contains no spin connection; for a configuration independent of x_mu, K^mu_mu = 0",
      "traceOnShell" -> "sum_mu K^mu_mu = (m + U'(S)) S on shell (both statistics), so the on-shell Lagrangian is L = S U'(S) - U(S)"|>,
    "emtConvention" -> "T^mu_nu = sigmaT ( -K^(mu_nu) + delta^mu_nu L ), K^mu_nu = (1/2)(Psibar gamma^mu D_nu Psi - D_nu Psibar gamma^mu Psi), symmetrised; sigmaT = +1 is the convention of SPEC section 4 (homogeneous on-shell states: rho = m S + U, p = S U' - U)",
    "generalFormulas" -> <|
      "rho" -> "sigmaT ( k4 - L )", "p3" -> "sigmaT ( L - k1 )", "pt" -> "sigmaT ( L - k5 )", "p0" -> "sigmaT ( L - k0 )",
      "q40" -> "-sigmaT K^(x4_x0)",
      "kmu" -> "k_mu = K^mu_mu (no sum) = (1/2)(Psibar gamma^mu d_mu Psi - d_mu Psibar gamma^mu Psi); L = k0+k1+k2+k3+k4+k5+k6+k7 - m S - U(S) (on shell S U'(S) - U(S))",
      "offDiagonal" -> "T^mu_nu = -sigmaT K^(mu_nu) for mu != nu, not x4-x0, must vanish (0 = kappa T^mu_nu); the x4-x0 pair must equal cot z uu Q/kappa and -tan z uu Q/kappa"|>,
    "dirac16complex00" -> <|
      "statement" -> "classical commuting Phi; k_mu, S, U are classical bilinears",
      "homogeneousCondensate" -> "Phi = Phi(x4) on shell, independent of x0..x3, x5..x7 (d4 Phi = A Phi, A = A0 - (3/4)(b4'/b4) I16, A0 = -gamma^x4 (M - 3 H gamma^x0), M = m + U'(S)): Phi = b4^(-3/4) chi with d4 chi = A0 chi; b4^(3/2) S is constant (exact), S = b4^(-3/2) S0; the diagonal kinetic components are K^x4_x4 = M S and 0 for every other direction, and K^x4_x0 = 0; hence rho = sigmaT (m S + U(S)), p3 = p_t = p0 = sigmaT (S U'(S) - U(S)), q40 = q04 = 0",
      "offDiagonalKinetic" -> offJSON,
      "offDiagonalConditions" -> "the off-diagonal field equations 0 = kappa T^mu_nu (mu != nu, not x4-x0) require the 15 bilinears B_abc = Phibar gamma^a gamma^b gamma^c Phi (frame gammas) to vanish",
      "offDiagonalWitness" -> "exact solutions with all 15 bilinears zero and S != 0 exist for every b4: Phi = b4^(-3/4) e^{-i w x4} Phi0, w = sqrt(M^2 - 9 H^2) (M^2 > 9 H^2), Phi0 = v1 + c v2 from the two A0-eigenvectors with gamma^x1 gamma^x5 = gamma^x2 gamma^x6 = gamma^x3 gamma^x7 = -1 and +1, c = conj(v1^dagger C v2); checked exactly at (M, H) = (5, 1), (5, 4/3), (-5, 1) (wolfram report, condensate_diagonal_witness_exact)",
      "asSource" -> "the condensate source has q40 = q04 = 0 and p3 = p_t = p0: with b4 not constant it is impossible in Einstein gravity (b4' = 0 is forced), it sources no exponential history with be != 0 for the author's weights, and in Einstein-Gauss-Bonnet only the two tuned branches of exponentialHistory.einsteinGaussBonnetVacuum; histories that are not exponential are not decided (wolfram report, condensate_source_with_b4_not_constant)"|>,
    "dirac16complex" -> <|
      "statement" -> "quantised Psi (SPEC section 6): every bilinear is replaced by the expectation value of the normal-ordered operator in the state, <:k_mu:>, <:S:>, <:U(S):> (note <U(S)> != U(<S>) in general); the trace identity sum_mu <:k_mu:> = <:(m + U'(S)) S:> for the normal-ordered operators of the field on a whole slice is ASSUMED here, not proved. It is decided only in a finite model, by Revision/theory/fock_quartic (reports/fock-quartic.json: one good-sector plane-wave mode set with frozen coefficients, flat frame, volume 1, 16 modes, 2^16 states, U = (lambda/2) S^2 with symbolic lambda). Nothing is proved for the field on a whole slice (many momenta), for the curved x0 dependence with its boundary term at z = pi/2, or for the extra-time sector",
      "rho" -> "sigmaT ( <:k4:> - <:L:> )", "p3" -> "sigmaT ( <:L:> - <:k1:> )", "pt" -> "sigmaT ( <:L:> - <:k5:> )", "p0" -> "sigmaT ( <:L:> - <:k0:> )",
      "offDiagonal" -> "every off-diagonal expectation value <:T^mu_nu:> (mu != nu, not x4-x0) must vanish, and the x4-x0 pair must equal cot z uu Q/kappa, -tan z uu Q/kappa",
      "kohnSham" -> "Kohn-Sham source (Revision/kohn_sham): rho_KS(x4), p3_KS(x4), p_t_KS(x4), p0_KS(x4) from the occupied Kohn-Sham orbitals; with this source the equations of generalSource apply with these entries; the source conditions (every diagonal entry independent of x0, the x4-x0 pair as above) are evaluated in Revision/field_equations_a4/reports/ks-source-conditions.json"|>|>,
  "b4" -> <|
    "metric" -> "the user's metric of 2026-10-14 (SPEC section 1): g55 = g66 = g77 = -E^(-2 a4[x4]) b4[x4] Sin[6 H x0]^(1/3), b4 > 0; symbols bb = b4, bd1 = b4', bd2 = b4'', uu = b4'/b4",
    "lovelockTensors" -> <|"E1" -> compEG[1], "E2" -> compEG[2], "E3" -> compEG[3],
      "allOtherComponents" -> "x2x2 = x3x3 = x1x1, x6x6 = x7x7 = x5x5; the only nonzero off-diagonal components are x4x0 and x0x4 (proportional to b4'); equal to Revision/metric_b4/results/metric-b4.json"|>,
    "generalSource" -> <|
      "constraint_x4" -> eqn[g44 + Lam, -kappa rho],
      "space_x1_eq_x2_eq_x3" -> eqn[g11 + Lam, kappa p3],
      "extraTime_x5_eq_x6_eq_x7" -> eqn[g55 + Lam, kappa pt],
      "hidden_x0" -> eqn[g00 + Lam, kappa p0],
      "offDiagonal_x4x0" -> eqn[g40, kappa q40],
      "offDiagonal_x0x4" -> eqn[g04, kappa q04],
      "offDiagonalFactor_Q" -> expr[Expand[Q40u]],
      "offDiagonalStatement" -> "kappa q40 = cot z (b4'/b4) Q and kappa q04 = -tan z (b4'/b4) Q: a source with q40 = q04 = 0 (in particular every source that is x0-independent and has no T^x4_x0) forces b4' Q = 0; for Einstein gravity Q = 3 H/2, so b4' = 0",
      "identity_x1_plus_x5_minus_2x0" -> expr[idG],
      "identity_einstein" -> "kappa (p3 + p_t - 2 p0) = (b4'/b4)^2/4 + b4''/(2 b4) (Einstein); with b4' = b4'' = 0 the earlier condition p3 + p_t = 2 p0",
      "conservation_x4" -> eqn[consGX4, 0],
      "conservation_x0" -> eqn[consGX0, 0],
      "secondOrderEinstein" -> "the x1 - x5 and x0 components are linear in (a4'', b4'') with a nonsingular Jacobian: they determine a4'' and b4'' from the sources; the x4 component is the constraint"|>,
    "fields" -> <|
      "gravityTerm" -> "gamma^mu Omega_mu = 3 H gamma^x0 + (3/4)(b4'/b4) gamma^x4",
      "condensate" -> "d4 Phi = (A - (3/4)(b4'/b4) I16) Phi: Phi = b4^(-3/4) Phi_1 (Phi_1 a b4 = 1 solution); b4^(3/2) S is constant; K^x4_x4 = M S, K^mu_mu = 0 (mu != x4), K^x4_x0 = 0; the same 15 off-diagonal three-gamma bilinears with b4-dependent coefficients"|>,
    "background" -> "with the author's weights (w1 = 1, w2 = 1/32, w3 = 1/1152, Lambda = 10) every vacuum solution has b4 constant and a4 = +-H x4 + const (Revision/metric_b4/results/vacuum-b4.json); the record uses the prescribed history a4 = H x4, b4 = b4(0) e^((4/3) H x4) (key exponentialHistory.authorWeights; SPEC section 1)"|>,
  "checksSummary" -> "see reports/wolfram-a4-report.json"|>;

writeJSON[FileNameJoin[{$fieldDir, "a4-equations.json"}], data];

failed = Count[checks, c_ /; c["verdict"] =!= "PASS"];
report = <|"producer" -> "Revision/field_equations_a4/wolfram/verify_field_equations_a4.wls", "spec" -> "Revision/SPEC.md section 5",
   "checkCount" -> Length[checks], "failedCount" -> failed, "verdict" -> If[failed == 0, "PASS", "FAIL"], "checks" -> checks|>;
writeJSON[FileNameJoin[{$fieldDir, "reports", "wolfram-a4-report.json"}], report];
Print["checks: ", Length[checks], ", failed: ", failed];
Scan[If[#["verdict"] =!= "PASS", Print["FAIL ", #["name"], ": ", #["detail"]]] &, checks];
Exit[If[failed == 0, 0, 1]];
