#!/usr/bin/env wolframscript
(* ::Package:: *)

(* verify_field_equations_a4.wls

   Driver for Revision/field_equations_a4/wolfram/FieldEquationsA4.wl (Revision/SPEC.md section 5).
   Writes, deterministically (LF line endings, no time stamps):
     Revision/field_equations_a4/a4-equations.json                 the equations (exact, InputForm + TeX)
     Revision/field_equations_a4/reports/wolfram-a4-report.json    every check with name, verdict, detail
   Inputs: Revision/algebra/gammas.json (the author's T16, order x0..x7), the primary representation of every
   spinor statement; FieldEquationsA4.wl reads it strictly on loading.  Revision/gkd_lovelock/results/lovelock-tensors.json
   (the GKD branch) and Revision/metric_warped/results/warped-metric.json (the independent sympy record of the
   corrected metric).  A missing or malformed gammas.json stops the run at once with a line "ERROR  ..." and exit code 1
   (no output is written).  So does a missing or unreadable FieldEquationsA4.wl or input, and an output file that
   cannot be opened for writing gives a line "ERROR  cannot write ..." and exit code 1.
   Usage (from the repository root):
     wolframscript -file Revision/field_equations_a4/wolfram/verify_field_equations_a4.wls
   All checks are exact symbolic identities (no floating point).  Exit code 0 iff every check passes.
   Since 2026-10-16 (the user's order "go ahead with the recomputation using the corrected metric", HANDOFF.md 0.10,
   phase W2) every section is derived for the CORRECTED metric of SPEC section 1 (version 2), general functions
   a4(x4) and b4(x4) > 0 and every real z = 6 H x0; the metric of 2026-10-14 (with its off-diagonal pair E^x4_x0) and
   its formulas (the former key b4 of a4-equations.json) are withdrawn.
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
readJSON[path_String] := Module[{v},
   If[!FileExistsQ[path], Print["ERROR  ", path, ": not found"]; Exit[1]];
   v = Quiet[Import[path, "RawJSON"]];
   If[!AssociationQ[v], Print["ERROR  ", path, ": not a JSON object"]; Exit[1]];
   v];

(* expressions as strings: InputForm (parsable by sympy once the caret is replaced) and TeX *)
fnRules = {Derivative[1, 0][f_][x4, x0] :> Symbol["d4" <> SymbolName[f]],
   Derivative[0, 1][f_][x4, x0] :> Symbol["d0" <> SymbolName[f]], f_Symbol[x4, x0] :> f, a4[x4] -> a4v};
inp[e_] := ToString[e /. fnRules, InputForm, PageWidth -> Infinity];
bs = FromCharacterCode[92];   (* the backslash *)
texRules = Map[(bs <> "text{" <> #[[1]] <> "}") -> StringReplace[#[[2]], "@" -> bs] &, {
    {"ad1", "(a_4')"}, {"ad2", "a_4''"}, {"uu", "u"}, {"vv", "v"}, {"kk", "k"}, {"be", "@beta"}, {"alpha1", "@alpha_1"}, {"alpha2", "@alpha_2"}, {"alpha3", "@alpha_3"},
    {"Lam", "@Lambda"}, {"AA", "A"}, {"cc", "@cot z"}, {"tt", "@tan z"}, {"a4v", "a_4"}, {"pt", "p_t"}, {"p3", "p_3"}, {"p0", "p_0"},
    {"q40", "q_{40}"}, {"q04", "q_{04}"}, {"sigmaT", "@sigma_T"}, {"hh", "h_4"},
    {"sv", "@sin z"}, {"cv", "@cos z"}, {"ww", "(@sin^2 z)^{1/12}"}, {"sgn", "@operatorname{sgn}(@cot z)"}, {"bb", "b_4"},
    {"d4rho", "@partial_4 @rho"}, {"d0rho", "@partial_0 @rho"}, {"d4p3", "@partial_4 p_3"}, {"d0p3", "@partial_0 p_3"},
    {"d4pt", "@partial_4 p_t"}, {"d0pt", "@partial_0 p_t"}, {"d4p0", "@partial_4 p_0"}, {"d0p0", "@partial_0 p_0"},
    {"d4q40", "@partial_4 q_{40}"}, {"d0q40", "@partial_0 q_{40}"}, {"d4q04", "@partial_4 q_{04}"}, {"d0q04", "@partial_0 q_{04}"}}];
tex[e_] := StringReplace[ToString[TeXForm[e /. fnRules]], texRules];
expr[e_] := <|"input" -> inp[e], "tex" -> tex[e]|>;
eqn[l_, r_] := <|"input" -> inp[l] <> " == " <> inp[r], "tex" -> tex[l] <> " = " <> tex[r]|>;
zero16 = ConstantArray[0, {16, 16}];
coordName[i_] := ToString[FECoords[[i]]];
x0FreeQ[e_] := FreeQ[e, sv] && FreeQ[e, cv] && FreeQ[e, ww] && FreeQ[e, sgn];
(* Wolfram positions of the author's coordinates x0..x7: position k + 1 holds xk, so x0 (hidden) = 1, x1, x2, x3 = 2, 3, 4,
   x4 (time) = 5, x5, x6, x7 = 6, 7, 8 *)
(* the derivative with respect to x4 in the variables of the field equations: kk = E^(2 a4)/b4, so kk' = kk (2 a4' - u) *)
d4uvk[e_] := D[e, ad1] ad2 + D[e, ad2] ad3 + D[e, uu] vv + D[e, vv] ww3 + D[e, kk] kk (2 ad1 - uu);

(* ======================================================================
   1. Geometry
   ====================================================================== *)
addCheck["metric_is_SPEC_section_1",
  FEMetricDiag === {E^(-2 a4[x4]) b4[x4] Cot[6 H x0]^2, E^(2 a4[x4]), E^(2 a4[x4]), E^(2 a4[x4]), -1,
     -E^(-2 a4[x4]) b4[x4] (Sin[6 H x0]^2)^(1/6), -E^(-2 a4[x4]) b4[x4] (Sin[6 H x0]^2)^(1/6), -E^(-2 a4[x4]) b4[x4] (Sin[6 H x0]^2)^(1/6)},
  "g = diag(e^{-2a4} b4 cot^2 z, e^{2a4}, e^{2a4}, e^{2a4}, -1, -e^{-2a4} b4 (sin^2 z)^{1/6} (x3)), z = 6 H x0 real (the author's x0..x7): the corrected metric of SPEC section 1 (version 2, 2026-10-16)"];
sqrtg = E^(-a4[x4]) b4[x4]^2 Abs[Cot[6 H x0]] (Sin[6 H x0]^2)^(1/4);
addCheck["sqrt_abs_det_g",
  FEZeroQ[Times @@ FEMetricDiag - E^(-2 a4[x4]) b4[x4]^4 Cot[6 H x0]^2 (Sin[6 H x0]^2)^(1/2)] && FEZeroQ[sqrtg^2 - Times @@ FEMetricDiag],
  "det g = e^{-2a4} b4^4 cot^2 z (sin^2 z)^{1/2} > 0 and sqrt|det g| = e^{-a4} b4^2 |cot z| (sin^2 z)^{1/4}, for every real z with sin z cos z != 0 (exact zero test modulo cos^2 + sin^2 - 1, w^12 - sin^2, sign(cot)^2 - 1)"];
addCheck["mixed_riemann_free_of_x0",
  x0FreeQ[FERiemannUU] && Length[FERiemannPairs] == 28,
  "every R^{ab}_{cd} (MTW, computed here from the Christoffel symbols, brought to the exact normal form for every real z) is free of x0: a rational function of H, a4', a4'', e^{a4}, b4, b4', b4''; " <>
   ToString[Length[FERiemannPairs]] <> " nonzero components with a < b, c < d"];
addCheck["mixed_riemann_only_sectional",
  And @@ (Sort[#[[{1, 2}]]] === Sort[#[[{3, 4}]]] & /@ FERiemannPairs),
  "every nonzero R^{ab}_{cd} has {c, d} = {a, b}: the 28 planes (a, b) each carry one sectional curvature, and there is no mixed component such as R^{x5 x0}_{x5 x4}"];
addCheck["riemann_pair_antisymmetry",
  And @@ Flatten[Table[Together[FERiemannUU[[a, b, c, d]] + FERiemannUU[[b, a, c, d]]] === 0 && Together[FERiemannUU[[a, b, c, d]] + FERiemannUU[[a, b, d, c]]] === 0,
     {a, 8}, {b, 8}, {c, 8}, {d, 8}]],
  "R^{ab}_{cd} = -R^{ba}_{cd} = -R^{ab}_{dc} for all 4096 index lists"];
milne = {ad1 -> 0, ad2 -> 0, bb -> H^2 (x4 - c0)^2, bd1 -> 2 H^2 (x4 - c0), bd2 -> 2 H^2, a4[x4] -> 0};
addCheck["flat_member",
  And @@ (Together[(#[[5]] /. milne)] === 0 & /@ FERiemannPairs),
  "a4 = 0, b4 = H^2 (x4 - c)^2: every R^{ab}_{cd} vanishes (the corrected metric is flat for this member: the block (x0, x4, x5, x6, x7) is Milne-like, the 3-space static)"];

(* ======================================================================
   2. Lovelock tensors: direct GKD computation here, and the GKD branch's monomial lists
   ====================================================================== *)
lovelockJSON = readJSON[FileNameJoin[{$revDir, "gkd_lovelock", "results", "lovelock-tensors.json"}]];
Pdirect = Table[FELovelockDirect[k], {k, 3}];
Ldirect = Table[FELovelockScalarDirect[k], {k, 3}];
Prebuilt = Table[FERebuildMixed[lovelockJSON, "P" <> ToString[k] <> "_mixed_up_h_down_j"], {k, 3}];
Lrebuilt = Table[FERebuildScalar[lovelockJSON, "L" <> ToString[k]], {k, 3}];

addCheck["P1_direct_equals_minus_4_Einstein",
  And @@ Flatten[Table[FEZeroQ[Pdirect[[1, h, j]] + 4 FEEinsteinMixed[[h, j]]], {h, 8}, {j, 8}]],
  "P_(1)^h_j = GKD[{h,h1,h2},{j,j1,j2}] R^{j1j2}_{h1h2} equals -4 G^h_j, G from the Ricci tensor (two routes, both in this file)"];
Do[
  addCheck["P" <> ToString[k] <> "_direct_equals_gkd_branch_monomials",
   And @@ Flatten[Table[FEZeroQ[Pdirect[[k, h, j]] - Prebuilt[[k, h, j]]], {h, 8}, {j, 8}]],
   "all 64 components of P_(" <> ToString[k] <> ")^h_j computed here (GKD as Det of the delta matrix, sum over the nonzero R^{ab}_{cd}) equal the exact monomial lists of Revision/gkd_lovelock/results/lovelock-tensors.json (14 exponents)"];
  addCheck["L" <> ToString[k] <> "_direct_equals_gkd_branch",
   FEZeroQ[Ldirect[[k]] - Lrebuilt[[k]]],
   "L_(" <> ToString[k] <> ") = " <> inp[Expand[FEUVK[Ldirect[[k]]]]] <> " (uu = b4'/b4, vv = (b4'/b4)', kk = e^{2a4}/b4)"];
  addCheck["P" <> ToString[k] <> "_trace_identity",
   FEZeroQ[Tr[Pdirect[[k]]] - (8 - 2 k) Ldirect[[k]]],
   "sum_h P_(" <> ToString[k] <> ")^h_h = (8 - " <> ToString[2 k] <> ") L_(" <> ToString[k] <> ")"];
  addCheck["P" <> ToString[k] <> "_structure",
   x0FreeQ[Pdirect[[k]]] && And @@ Flatten[Table[If[h != j, Pdirect[[k, h, j]] === 0, True], {h, 8}, {j, 8}]] &&
    Pdirect[[k, 2, 2]] === Pdirect[[k, 3, 3]] === Pdirect[[k, 4, 4]] && Pdirect[[k, 1, 1]] === Pdirect[[k, 6, 6]] === Pdirect[[k, 7, 7]] === Pdirect[[k, 8, 8]],
   "P_(" <> ToString[k] <> ")^h_j is diagonal (all 56 off-diagonal components vanish) and free of x0, with x1 = x2 = x3 and x0 = x5 = x6 = x7 (the hidden direction and the three extra times carry the same component)"],
  {k, 3}];
addCheck["P4_vanishes_pigeonhole",
  FEGKD[{1, 2, 3, 4, 5, 6, 7, 8, 1}, {1, 2, 3, 4, 5, 6, 7, 8, 2}] === 0 && FEGKD[Range[8], Range[8]] === 1,
  "P_(4) would need GKD of 9 indices over 8 values: two equal upper indices give two equal rows of the delta matrix, determinant 0; so k = 1, 2, 3 is the full Lovelock series in 8 dimensions"];

Ek = Table[-Pdirect[[k]]/2^(k + 1), {k, 3}];
EkD = Map[# /. FESymToDeriv &, Ek, {3}];
Do[
  addCheck["E" <> ToString[k] <> "_divergence_free",
   And @@ (FEZeroQ /@ FEDivergence[EkD[[k]]]),
   "nabla_mu E_(" <> ToString[k] <> ")^mu_nu = 0 for nu = x0..x7 (exact; Christoffel symbols of this file; general a4 and b4, every real z)"],
  {k, 3}];
(* the variables of the field equations: uu = b4'/b4, vv = (b4'/b4)' (so b4''/b4 = vv + uu^2), kk = e^{2 a4}/b4 *)
EkV = Table[If[h == j, Expand[FEUVK[Ek[[k, h, j]]]], 0], {k, 3}, {h, 8}, {j, 8}];
addCheck["lovelock_variables",
  And @@ Flatten[Table[FreeQ[EkV[[k, h, h]], bb] && FreeQ[EkV[[k, h, h]], a4] && PolynomialQ[EkV[[k, h, h]], {H, ad1, ad2, uu, vv, kk}], {k, 3}, {h, 8}]] &&
   And @@ Flatten[Table[FEZeroQ[Ek[[k, h, h]] - (EkV[[k, h, h]] /. {uu -> bd1/bb, vv -> bd2/bb - bd1^2/bb^2, kk -> E^(2 a4[x4])/bb})], {k, 3}, {h, 8}]],
  "every component of E_(1), E_(2), E_(3) is a polynomial in H, a4', a4'', u = b4'/b4, v = (b4'/b4)' and k = e^{2a4}/b4 (k enters through the curvature -H^2 e^{2a4}/b4 of the block (x0, x5, x6, x7)): a4 and b4 themselves enter only through k"];

(* ======================================================================
   3. The field equations with a general source
   ====================================================================== *)
alphas = {alpha1, alpha2, alpha3};
LHSG = Sum[alphas[[k]] Ek[[k]], {k, 3}] + Lam IdentityMatrix[8];
LHSV = Sum[alphas[[k]] EkV[[k]], {k, 3}];
{u11, u44, u00} = Expand /@ {LHSV[[2, 2]], LHSV[[5, 5]], LHSV[[1, 1]]};
einst = {alpha1 -> 1, alpha2 -> 0, alpha3 -> 0};
hh = uu/2 - ad1;   (* h4 = d/dx4 Log[e^{-a4} b4^{1/2}], the rate of the block (x0, x5, x6, x7) *)

addCheck["independent_components",
  And @@ Flatten[Table[If[h != j, LHSG[[h, j]] === 0, True], {h, 8}, {j, 8}]] &&
   LHSG[[2, 2]] === LHSG[[3, 3]] === LHSG[[4, 4]] && LHSG[[1, 1]] === LHSG[[6, 6]] === LHSG[[7, 7]] === LHSG[[8, 8]],
  "general a4 and b4: every off-diagonal left-hand side vanishes identically, x1 = x2 = x3 and x0 = x5 = x6 = x7: the field equations have three independent components (x4, x1, x0); they require T^mu_nu = 0 for every mu != nu and T^x0_x0 = T^x5_x5 = T^x6_x6 = T^x7_x7 (p0 = p_t)"];
addCheck["constraint_first_order",
  FreeQ[u44, ad2] && FreeQ[u44, vv],
  "the x4 component (constraint) contains a4', u = b4'/b4 and k = e^{2a4}/b4 but no second derivative: Einstein: " <> inp[Expand[u44 /. einst]]];
jacG = Together[D[{u11, u00}, {{ad2, vv}}]];
detG = Factor[Together[Det[jacG]]];
addCheck["second_order_system_a4pp_vv",
  And @@ (FreeQ[#, ad2] && FreeQ[#, vv] & /@ Flatten[jacG]) &&
   Expand[u11 - (jacG[[1, 1]] ad2 + jacG[[1, 2]] vv) - (u11 /. {ad2 -> 0, vv -> 0})] === 0 &&
   Expand[u00 - (jacG[[2, 1]] ad2 + jacG[[2, 2]] vv) - (u00 /. {ad2 -> 0, vv -> 0})] === 0 &&
   Together[detG /. einst] === -3 && (jacG /. einst) === {{2, -2}, {0, -3/2}},
  "the x1 and x0 components are linear in (a4'', v) (v = (b4'/b4)') with the Jacobian J (coefficients depending on a4', u, k, H, alpha_k), det J = " <> inp[detG] <>
   ", not identically zero (Einstein: J = {{2, -2}, {0, -3/2}}, det J = -3): where det J != 0 these two components determine a4'' and (b4'/b4)' from the sources; the x4 component is the constraint"];
bianchiG = Expand[d4uvk[u44] - 3 ad1 (u11 - u44) - 4 hh (u00 - u44)];
addCheck["constraint_propagation_bianchi",
  bianchiG === 0,
  "d/dx4 [sum_k alpha_k E_(k)^x4_x4] = 3 a4' (E^x1_x1 - E^x4_x4) + 4 h4 (E^x0_x0 - E^x4_x4), h4 = b4'/(2 b4) - a4' (k' = k (2 a4' - u)), identically: the x4 component of the Bianchi identity; with the conservation law below the derivative of the constraint follows from the other components"];
(* conservation of a general source T(x4, x0), with an off-diagonal pair q40 = T^x4_x0, q04 = T^x0_x4 *)
Tgen = DiagonalMatrix[{p0[x4, x0], p3[x4, x0], p3[x4, x0], p3[x4, x0], -rho[x4, x0], pt[x4, x0], pt[x4, x0], pt[x4, x0]}];
Tgen[[5, 1]] = q40[x4, x0]; Tgen[[1, 5]] = q04[x4, x0];
divTG = FENormal /@ FEDivergence[Tgen];
consX4 = -D[rho[x4, x0], x4] - 3 ad1 (rho[x4, x0] + p3[x4, x0]) - 3 hh (rho[x4, x0] + pt[x4, x0]) - hh (rho[x4, x0] + p0[x4, x0]) /. uu -> bd1/bb;
consX0 = D[p0[x4, x0], x0] + 3 H (cv/sv) (p0[x4, x0] - pt[x4, x0]);
addCheck["conservation_components",
  And @@ (# === 0 & /@ divTG[[{2, 3, 4, 6, 7, 8}]]) &&
   FENormal[divTG[[5]] - consX4 - (D[q04[x4, x0], x0] - 3 H ((1 + sv^2)/(sv cv)) q04[x4, x0])] === 0 &&
   FENormal[divTG[[1]] - consX0 - (D[q40[x4, x0], x4] + (3/2) (bd1/bb) q40[x4, x0] + (ad1 - bd1/(2 bb)) (bb/E^(2 a4[x4])) (cv/sv)^2 q04[x4, x0])] === 0,
  "nabla_mu T^mu_x4 = -d4 rho - 3 a4' (rho + p3) - 3 h4 (rho + p_t) - h4 (rho + p0) + d0 q04 - 3 H (cot z + 2 tan z) q04 and nabla_mu T^mu_x0 = d0 p0 + 3 H cot z (p0 - p_t) + d4 q40 + (3/2)(b4'/b4) q40 - h4 cot^2 z q04/k (h4 = b4'/(2 b4) - a4', k = e^{2a4}/b4); the other components vanish identically.  With the field equations (q40 = q04 = 0, p0 = p_t) the x0 component is d0 p0 = 0 and the x4 component is the energy exchange"];
mwFile = FileNameJoin[{$revDir, "metric_warped", "results", "warped-metric.json"}];
mw = readJSON[mwFile];
mwParse[s_String] := ToExpression[StringReplace[s, "**" -> "^"]] /. {EA -> Sqrt[kk bb], bd1 -> uu bb, bd2 -> (vv + uu^2) bb};
mwE = Association[KeyValueMap[#1 -> Expand[Together[mwParse[#2]]] &, mw["einstein_diagonal"]]];
addCheck["einstein_equals_metric_warped_record",
  Sort[Keys[mwE]] === {"x0", "x1", "x4", "x5"} && mwE["x0"] === Expand[u00 /. einst] && mwE["x1"] === Expand[u11 /. einst] &&
   mwE["x4"] === Expand[u44 /. einst] && mwE["x5"] === Expand[EkV[[1, 6, 6]]],
  "the Einstein tensor G = E_(1) computed here (GKD over the nonzero R^{ab}_{cd}) equals the independent sympy record Revision/metric_warped/results/warped-metric.json (key einstein_diagonal: x0, x1, x4, x5)"];
(* Einstein *)
ein44 = Expand[u44 /. einst]; ein11 = Expand[u11 /. einst]; ein00 = Expand[u00 /. einst];
addCheck["einstein_components",
  ein44 === Expand[6 H^2 kk + 3 ad1^2 - (3/2) uu^2] && ein11 === Expand[2 ad2 - 5 ad1^2 + 6 H^2 kk + 6 ad1 uu - (5/2) uu^2 - 2 vv] &&
   ein00 === Expand[3 H^2 kk - 3 ad1^2 + (3/2) ad1 uu - (3/2) uu^2 - (3/2) vv],
  "Einstein (alpha1 = 1, alpha2 = alpha3 = 0), u = b4'/b4, v = u', k = e^{2a4}/b4: G^x4_x4 = 6 H^2 k + 3 a4'^2 - (3/2) u^2, G^x1_x1 = 2 a4'' - 5 a4'^2 + 6 H^2 k + 6 a4' u - (5/2) u^2 - 2 v, G^x0_x0 = G^x5_x5 = 3 H^2 k - 3 a4'^2 + (3/2) a4' u - (3/2) u^2 - (3/2) v"];
nec0 = Expand[u00 - u44]; nec3 = Expand[u11 - u44];
addCheck["einstein_null_combinations",
  Expand[(nec0 /. einst) + (3/2) (2 H^2 kk + 4 ad1^2 - ad1 uu + vv)] === 0 && Expand[(nec3 /. einst) - (2 ad2 - 8 ad1^2 + 6 ad1 uu - uu^2 - 2 vv)] === 0,
  "Einstein: kappa (rho + p0) = kappa (rho + p_t) = -(3/2)(2 H^2 k + 4 a4'^2 - a4' u + v) and kappa (rho + p3) = 2 a4'' - 8 a4'^2 + 6 a4' u - u^2 - 2 v"];
milneV = {ad1 -> 0, ad2 -> 0, uu -> 2/(x4 - c0), vv -> -2/(x4 - c0)^2, kk -> 1/(H^2 (x4 - c0)^2)};
addCheck["einstein_flat_vacuum",
  Together[{ein44, ein11, ein00} /. milneV] === {0, 0, 0},
  "Einstein: a4 = 0, b4 = H^2 (x4 - c)^2 (the flat member) solves the vacuum equations with Lambda = 0"];
expoE = {ad1 -> AA H, ad2 -> 0, uu -> be AA H, vv -> 0};
addCheck["einstein_no_exponential_vacuum",
  Reduce[(ein44 + Lam == 0 && ein11 + Lam == 0 && ein00 + Lam == 0 /. expoE) && kk > 0 && H > 0, {AA, be, kk, Lam}, Reals] === False,
  "Einstein: no exponential history a4 = A H x4 + a0, b4 = b4(0) e^(beta A H x4) is a vacuum solution, for any A, beta, Lambda: the vacuum equations have no real solution with k = e^{2a4}/b4 > 0 at any single x4"];
jacE = Together[D[{u11, u00} /. einst /. {uu -> bd1/bb, vv -> bd2/bb - bd1^2/bb^2}, {{ad2, bd2}}]];
addCheck["einstein_second_order_system",
  Together[Det[jacE] bb] === -3 && FreeQ[jacE, ad1],
  "Einstein: the x1 and x0 components are linear in (a4'', b4'') with Jacobian " <> inp[jacE] <> " (det = -3/b4, nonsingular): they determine a4'' and b4'' from the sources; the x4 component is the constraint"];

(* ======================================================================
   4. Exponential histories a4 = A H x4 + a0, b4 = b4(0) e^{beta A H x4}: u = beta A H, v = 0,
      k = e^{2a4}/b4 = k0 e^{(2 - beta) A H x4} (constant exactly when beta = 2 or A = 0)
   ====================================================================== *)
hist = {ad1 -> AA H, ad2 -> 0, uu -> be AA H, vv -> 0};
{h11, h44, h00} = Expand /@ ({u11, u44, u00} /. hist);
srcRho = -(h44 + Lam)/kappa; srcP3 = (h11 + Lam)/kappa; srcP0 = (h00 + Lam)/kappa;
addCheck["exponential_history_required_source",
  And @@ (PolynomialQ[#, kk] && Exponent[#, kk] <= 2 & /@ {h11, h44, h00}) && Expand[Coefficient[h44, kk] /. einst] === 6 H^2,
  "on a4 = A H x4 + a0, b4 = b4(0) e^(beta A H x4) the field equations require a diagonal source with p0 = p_t: rho, p3, p0 are polynomials of degree <= 2 in k = k0 e^{(2 - beta) A H x4} (formulas in a4-equations.json, key exponentialHistory): the source is constant only for beta = 2 or A = 0 (the k-coefficient of the constraint is 6 H^2 alpha1 + ..., Einstein 6 H^2)"];
authW = {alpha1 -> 1/H^2, alpha2 -> (1/32)/H^4, alpha3 -> (1/1152)/H^6, Lam -> -10};
recordHist = {AA -> 1, be -> 4/3};
authHist = Expand /@ ({h44, h11, h00} /. authW /. recordHist);
mwHist = mw["history_source"]["author_weights_A1_beta43_mathematica"];
mwH[s_String] := Expand[ToExpression[s] /. Power[E, e_] :> kk^Together[3 e/(2 H x4)]];   (* k = e^{(2/3) H x4} on the record's history *)
mwEin = mw["history_source"]["einstein_A1_beta43_mathematica"];
einHist = Expand /@ ({h44, h11, h00} /. einst /. recordHist);
addCheck["author_weights_history_source",
  authHist === {mwH[mwHist["-rho"]], mwH[mwHist["p3"]], mwH[mwHist["p0"]]} && mwH[mwHist["p_t"]] === authHist[[3]] &&
   einHist === Expand[{mwH[mwEin["-rho"]], mwH[mwEin["p3"]], mwH[mwEin["p0"]]}],
  "the record's history a4 = H x4, b4 = b4(0) e^((4/3) H x4) (b4(0) = 1, k = e^{(2/3) H x4}) with the author's weights (alpha_k = w_k/H^(2k), w = (1, 1/32, 1/1152), Lambda_author = 10, Lam = -10): kappa T - Lam = diag(p0, p3, p3, p3, -rho, p_t, p_t, p_t) with -kappa rho - Lam = " <> inp[authHist[[1]]] <>
   ", kappa p3 - Lam = " <> inp[authHist[[2]]] <> ", kappa p0 - Lam = kappa p_t - Lam = " <> inp[authHist[[3]]] <>
   " (k = e^{(2/3) H x4}), and with Einstein " <> inp[einHist] <> ": equal to the independent sympy record Revision/metric_warped/results/warped-metric.json (key history_source); a diagonal, x0-independent source with p0 = p_t that grows with x4: the history is a PRESCRIBED background, not a vacuum"];
numer[e_] := Numerator[Together[e]];
vacAuth = numer /@ ({h44 + Lam, h11 + Lam, h00 + Lam} /. authW);
addCheck["author_weights_no_exponential_vacuum",
  Reduce[(And @@ Thread[Flatten[CoefficientList[#, kk] & /@ vacAuth] == 0]) && H > 0, {AA, be}, Reals] === False &&
   Reduce[(And @@ Thread[(vacAuth /. be -> 2) == 0]) && kk > 0 && H > 0, {AA, kk}, Reals] === False &&
   Reduce[(And @@ Thread[(vacAuth /. AA -> 0) == 0]) && kk > 0 && H > 0, {kk}, Reals] === False,
  "the author's weights: no exponential history is a vacuum solution: where k varies (beta != 2, A != 0) every coefficient of k^0, k^1, k^2 would have to vanish (no real solution), and for constant k (beta = 2 or A = 0) the equations have no real solution with k > 0"];
egb = {alpha1 -> 1, alpha3 -> 0};
vacEGB = numer /@ ({h44 + Lam, h11 + Lam, h00 + Lam} /. egb);
egbConst = Reduce[(And @@ Thread[(vacEGB /. be -> 2) == 0]) && kk > 0 && H > 0, {AA, kk, alpha2, Lam}, Reals];
egbBranch = H > 0 && kk > 0 && kk != AA^2 && alpha2 == -1/(4 H^2 (AA^2 - kk)) && Lam == Together[-(h44 /. egb /. be -> 2 /. alpha2 -> -1/(4 H^2 (AA^2 - kk)))];
addCheck["egb_exponential_vacuum_branches",
  Reduce[(And @@ Thread[Flatten[CoefficientList[#, kk] & /@ vacEGB] == 0]) && H > 0, {AA, be, alpha2, Lam}, Reals] === False &&
   Reduce[egbConst && ! egbBranch, {AA, kk, alpha2, Lam}, Reals] === False && Reduce[egbBranch && ! egbConst, {AA, kk, alpha2, Lam}, Reals] === False,
  "Einstein-Gauss-Bonnet (alpha1 = 1, alpha3 = 0): where k varies there is no vacuum exponential history; for constant k = k0 > 0 (beta = 2: b4 = b4(0) e^{2 A H x4}, any A) the vacuum histories are exactly those with k0 != A^2, alpha2 = -1/(4 H^2 (A^2 - k0)) and Lambda = -E^x4_x4 at the history (" <>
   inp[Together[-(h44 /. egb /. be -> 2 /. alpha2 -> -1/(4 H^2 (AA^2 - kk)))]] <> "): a vacuum exists only for these tuned couplings"];

(* ======================================================================
   5. Field-specific sources: the spinor bilinears in the author's T16 (the PRIMARY representation, SPEC
      section 2: Revision/algebra/gammas.json, read strictly by FieldEquationsA4.wl).  The representation
      Cl(1,1)^(x)4 built in FieldEquationsA4.wl is used ONLY for comparison: its Clifford relations and C, its
      exact equivalence with T16, and the representation independence of the off-diagonal coefficients.
   ====================================================================== *)
fx = FEFixture; gR = FEGammaFrameComparison; CR = FECComparison;
cgrav = (3/2) H E^a4[x4] bb^(-1/2); vgrav = bd1/bb - ad1/2;   (* gamma^mu Omega_mu = cgrav gamma^x0 + vgrav gamma^x4 *)
(* the kinetic matrices of the homogeneous condensate in a representation g with charge matrix Cm:
   Phi = Phi(x4) on shell, d4 Phi = A Phi with A = -gamma^x4 (M - gamma^mu Omega_mu); N^mu_nu with
   K^mu_nu = Phi^dagger N^mu_nu Phi, K^mu_nu = (1/2)(Phibar gamma^mu D_nu Phi - (D_nu Phibar) gamma^mu Phi) *)
gd = FEMetricDiag;
condensateKinetic[g_List, Cm_] := Module[{gc, om, gdir, am, dP, dPb, nm, ns},
   gc = Map[FENormal, FEGammaCoordOf[g], {3}]; om = Map[FENormal, FEOmegaOf[g], {3}];
   gdir = Map[FENormal, Sum[gc[[mu]] . om[[mu]], {mu, 8}], {2}];
   am = Map[FENormal, -gc[[5]] . (MM IdentityMatrix[16] - gdir), {2}];     (* d4 Phi = A Phi, since (gamma^x4)^-1 = -gamma^x4; x4 = position 5 *)
   dP[nu_] := If[nu == 5, am, zero16] + om[[nu]];
   dPb[nu_] := If[nu == 5, Transpose[am] . Cm, zero16] - Cm . om[[nu]];
   nm = Table[Map[FENormal, (1/2) (Cm . gc[[mu]] . dP[nu] - dPb[nu] . gc[[mu]]), {2}], {mu, 8}, {nu, 8}];
   ns = Table[Map[FENormal, (1/2) (nm[[mu, nu]] + FENormal[gd[[nu]]/gd[[mu]]] nm[[nu, mu]]), {2}], {mu, 8}, {nu, 8}];
   <|"gC" -> gc, "Om" -> om, "Gdirac" -> gdir, "Amat" -> am, "Nmat" -> nm, "NmatSym" -> ns|>];
subsets = Subsets[Range[8]];
basisMatIn[g_List, Cm_, s_List] := Cm . If[s === {}, IdentityMatrix[16], Dot @@ (g[[#]] & /@ s)];
offDiagonalDecomposition[g_List, Cm_, ns_] := Module[{binv, dec, pairs},
   binv = Association[(# -> Inverse[basisMatIn[g, Cm, #]]) & /@ subsets];
   dec[N_] := Select[Association[(# -> FENormal[Tr[binv[#] . N]/16]) & /@ subsets], # =!= 0 &];
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
spinAnti = And @@ Flatten[Table[FEZeroQ[FESpinConnLow[[mu, a, b]] + FESpinConnLow[[mu, b, a]]], {mu, 8}, {a, 8}, {b, 8}]];
addCheck["spin_connection_antisymmetric", spinAnti, "omega_mu ab = -omega_mu ba for the canonical spin connection of this metric (vielbein postulate; general a4 and b4, every real z)"];
addCheck["Omega_x4_vanishes_Omega_x0_does_not",
  Om[[5]] === zero16 && Om[[1]] =!= zero16 && Map[FENormal, Om[[1]] - (1/2) (cv/sv) E^(-a4[x4]) Sqrt[bb] (bd1/(2 bb) - ad1) gF[[1]] . gF[[5]], {2}] === zero16,
  "Omega_x4 = 0 and Omega_x0 = (1/2) cot z e^{-a4} b4^{1/2} h4 gamma^x0 gamma^x4 != 0 (h4 = b4'/(2 b4) - a4': the hidden vielbein e^{-a4} b4^{1/2} cot z depends on x4)"];
anticommOm = Table[Map[FENormal, gC[[mu]] . Om[[mu]] + Om[[mu]] . gC[[mu]], {2}], {mu, 8}];
addCheck["gamma_mu_anticommutes_with_Omega_mu_no_sum",
  And @@ (# === zero16 & /@ anticommOm),
  "{gamma^mu, Omega_mu} = 0 for each mu separately (no sum; general a4, b4): the spin connection drops out of every diagonal kinetic component K^mu_mu = (1/2)(Psibar gamma^mu d_mu Psi - d_mu Psibar gamma^mu Psi)"];
Gdirac = primG["Gdirac"];
addCheck["gravity_term_gamma_mu_Omega_mu",
  Map[FENormal, Gdirac - (cgrav gF[[1]] + vgrav gF[[5]]), {2}] === zero16 && x0FreeQ[Gdirac],
  "gamma^mu Omega_mu = (3/2) H e^{a4} b4^{-1/2} gamma^x0 + (b4'/b4 - a4'/2) gamma^x4 exactly (frame gammas; free of x0; the same as the field-theory record and Revision/metric_warped/results/warped-metric.json, key dirac_gravity_term)"];
(* the homogeneous condensate: Phi(x4) independent of x0..x3, x5..x7, on shell gamma^mu D_mu Phi = M Phi, M = m + U'(S) real *)
g4 = gC[[5]];   (* gamma^x4 *)
Amat = primG["Amat"];      (* -g4 . (MM I16 - Gdirac): d4 Phi = Amat Phi *)
Kmat = gF[[5]] . gF[[1]];   (* K = gamma^x4 gamma^x0 *)
Bmat[c_] := -MM gF[[5]] + c Kmat;   (* the reduced system chi' = B chi *)
addCheck["condensate_equation_x0_consistent",
  x0FreeQ[Amat] && Map[FENormal, g4 . Amat + Gdirac - MM IdentityMatrix[16], {2}] === zero16 &&
   Map[FENormal, Amat - (Bmat[cgrav] - vgrav IdentityMatrix[16]), {2}] === zero16 &&
   Expand[Bmat[c] . Bmat[c] - (c^2 - MM^2) IdentityMatrix[16]] === zero16,
  "for Phi = Phi(x4) the equation is d4 Phi = A Phi with A = B - (b4'/b4 - a4'/2) I16, B = -M gamma^x4 + c(x4) gamma^x4 gamma^x0, c = (3/2) H e^{a4} b4^{-1/2}, free of x0: Phi = e^{a4/2} b4^{-1} chi with chi' = B chi (B^2 = (c^2 - M^2) I16): an x0-independent solution exists for every a4, b4"];
addCheck["condensate_S_law",
  Map[FENormal, FEC . Amat + Transpose[Amat] . FEC + 2 vgrav FEC, {2}] === zero16 && Expand[FEC . Bmat[c] + Transpose[Bmat[c]] . FEC] === zero16,
  "C A + A^T C = -2 (b4'/b4 - a4'/2) C (M real), so d4 S = (a4' - 2 b4'/b4) S: S = e^{a4} b4^{-2} S0, exact for every initial Phi (C B + B^T C = 0)"];
addCheck["condensate_adjoint_equation",
  Map[FENormal, Transpose[Amat] . FEC . g4 - FEC . Sum[Om[[mu]] . gC[[mu]], {mu, 8}] + MM FEC, {2}] === zero16,
  "(D_mu Phibar) gamma^mu = -M Phibar holds for the condensate (the adjoint of the field equation; general a4, b4)"];
Nmat = primG["Nmat"];
NmatSym = primG["NmatSym"];
addCheck["condensate_kinetic_tensor_diagonal",
  Map[FENormal, NmatSym[[5, 5]] - MM FEC, {2}] === zero16 && And @@ Table[NmatSym[[mu, mu]] === zero16, {mu, {1, 2, 3, 4, 6, 7, 8}}] &&
   NmatSym[[5, 1]] === zero16 && NmatSym[[1, 5]] === zero16,
  "for the condensate the symmetrised kinetic tensor has K^x4_x4 = M S, K^mu_mu = 0 for mu = x0..x3, x5..x7, and K^x4_x0 = K^x0_x4 = 0, exactly, for every Phi (general a4, b4)"];
basisMat[s_List] := basisMatIn[gF, FEC, s];
offDecomp = offDiagonalDecomposition[gF, FEC, NmatSym];
offPairs = Keys[offDecomp];
recon = And @@ Table[Map[FENormal, Total[KeyValueMap[#2 basisMat[#1] &, offDecomp[pq]]] - NmatSym[[pq[[1]], pq[[2]]]], {2}] === zero16, {pq, offPairs}];
triples = Union[Flatten[Keys /@ Values[offDecomp], 1]];
expectedTriples = Sort[Join[Table[{1, i, 5}, {i, 2, 4}], Flatten[Table[{1, i, t}, {i, 2, 4}, {t, 6, 8}], 1],
    Flatten[Table[{i, 5, t}, {i, 2, 4}, {t, 6, 8}], 1], Table[{1, 5, t}, {t, 6, 8}]]];
addCheck["condensate_offdiagonal_are_three_gamma_bilinears",
  recon && And @@ (Length[#] == 3 & /@ triples) && Sort[triples] === expectedTriples,
  "the nonzero off-diagonal kinetic components of the condensate are exactly combinations of the 24 bilinears B_abc = Phibar gamma^a gamma^b gamma^c Phi with {a,b,c} = {x0, i, x4} (3), {x0, i, t} (9), {i, x4, t} (9), {x0, x4, t} (3) (i = x1..x3, t = x5..x7), with coefficients depending on H, a4', b4'/b4, e^{a4}, b4 and x0; " <>
   ToString[Length[offPairs]] <> " ordered pairs (mu, nu) are nonzero (the pairs x0-i, i-x4, i-t, x4-t)"];
cmpRG = condensateKinetic[gR, CR];
offDecompR = offDiagonalDecomposition[gR, CR, cmpRG["NmatSym"]];
addCheck["offdiagonal_coefficients_representation_independent",
  Map[FENormal, cmpRG["Gdirac"] - (cgrav gR[[1]] + vgrav gR[[5]]), {2}] === zero16 && Keys[offDecompR] === offPairs &&
   And @@ Table[Keys[offDecompR[pq]] === Keys[offDecomp[pq]] &&
      And @@ (FEZeroQ /@ (Values[offDecompR[pq]] - Values[offDecomp[pq]])), {pq, offPairs}],
  "the comparison representation (Cl(1,1)^(x)4, built in FieldEquationsA4.wl), run through the same condensate pipeline, gives the same gravity term, the same " <>
   ToString[Length[offPairs]] <> " nonzero ordered pairs (mu, nu), the same three-gamma bilinears and exactly the same coefficients as the author's T16 (primary): the off-diagonal coefficients in a4-equations.json are representation independent"];
(* exact witnesses for histories with constant k = e^{2a4}/b4 = k0 (b4 = b4(0) e^{2 a4}, any a4) and constant M:
   c = (3/2) H sqrt(k0) is constant, chi = e^{B x4} chi0; Phi = e^{a4/2} b4^{-1} e^{-i w x4} Phi0 with B Phi0 = -i w Phi0 *)
witness[mval_, hval_, kval_] := Module[{w, cval, Bm, ex, v1, v2, svl, ph, ok, sval, conds, cvl, phiF, resid, histK},
   cval = (3/2) hval Sqrt[kval]; w = Sqrt[mval^2 - cval^2];
   Bm = Bmat[cval] /. MM -> mval;
   (* gamma^x1 gamma^x5, gamma^x2 gamma^x6, gamma^x3 gamma^x7: positions (2, 6), (3, 7), (4, 8) *)
   ex[e_] := NullSpace[Join[Bm + I w IdentityMatrix[16], gF[[2]] . gF[[6]] - e IdentityMatrix[16],
       gF[[3]] . gF[[7]] - e IdentityMatrix[16], gF[[4]] . gF[[8]] - e IdentityMatrix[16]]];
   v1 = First[ex[-1]]; v2 = First[ex[1]];
   svl = Conjugate[v1] . FEC . v2; cvl = Conjugate[svl];
   ph = v1 + cvl v2;
   sval = Simplify[Conjugate[ph] . FEC . ph];
   conds = Table[FullSimplify[Conjugate[ph] . (basisMat[t]) . ph], {t, triples}];
   (* the full field Phi(x4) = e^{a4/2} b4^{-1} e^{-i w x4} Phi0 on the history b4 = e^{2 a4}/k0 solves d4 Phi = A Phi for every a4 *)
   histK = {b4 -> Function[{y}, E^(2 a4[y])/kval]};
   phiF = E^(a4[x4]/2) b4[x4]^(-1) Exp[-I w x4] ph /. histK;
   resid = Together[D[phiF, x4] - (((Amat /. {MM -> mval, H -> hval}) /. FESymToDeriv) /. histK) . phiF];
   ok = Length[ex[-1]] == 1 && Length[ex[1]] == 1 && Expand[Bm . ph + I w ph] === ConstantArray[0, 16] && Simplify[resid, Element[a4[x4], Reals]] === ConstantArray[0, 16] &&
     And @@ (# === 0 & /@ conds) && sval =!= 0 && Element[sval, Reals];
   {ok, w, sval}];
wit = {witness[5, 1, 4], witness[5, 4/3, 4], witness[-5, 1, 4]};
addCheck["condensate_witness_constant_k_exact",
  And @@ (#[[1]] & /@ wit),
  "exact Gaussian-rational witnesses (M, H, k0) = (5, 1, 4), (5, 4/3, 4), (-5, 1, 4) on the histories with constant k = e^{2a4}/b4 = k0 (b4 = e^{2 a4}/k0, any a4(x4)) and constant M: Phi = e^{a4/2} b4^{-1} e^{-i w x4} Phi0 with w = sqrt(M^2 - (9/4) H^2 k0) = " <> inp[#[[2]] & /@ wit] <>
   ", Phi0 = v1 + c v2 (v1, v2 the eigenvectors of B = -M gamma^x4 + (3/2) H sqrt(k0) gamma^x4 gamma^x0 for -i w with gamma^x1 gamma^x5 = gamma^x2 gamma^x6 = gamma^x3 gamma^x7 = -1 and +1, c = conj(v1^dagger C v2)), solves the condensate equation; all 24 three-gamma bilinears vanish and " <>
   "e^{-a4} b4^2 S = " <> inp[#[[3]] & /@ wit] <> " != 0.  For histories with k not constant (or M not constant) no witness is constructed here (not decided)"];
(* the condensate as a source: rho = sigmaT (m S + U), p3 = p_t = p0 = sigmaT (S U' - U), every off-diagonal component 0 *)
condE = numer[Expand[(u11 - u00) /. hist] /. einst];
condAuth = numer[Expand[(u11 - u00) /. hist] /. authW];
authEqB2 = Reduce[(condAuth /. be -> 2) == 0 && kk > 0 && H > 0, {AA, kk}, Reals];
authEqB2Expected = H > 0 && kk == (16 + 2 AA^2)/(2 + AA^2);
authEqA0 = Reduce[(condAuth /. AA -> 0) == 0 && kk > 0 && H > 0, {kk}, Reals];
addCheck["condensate_source_equal_pressures",
  Reduce[(And @@ Thread[CoefficientList[condE, kk] == 0]) && H > 0, {AA, be}, Reals] === False &&
   Reduce[(condE /. be -> 2) == 0 && kk > 0 && H > 0, {AA, kk}, Reals] === False &&
   Reduce[(condE /. AA -> 0) == 0 && kk > 0 && H > 0, {kk}, Reals] === False &&
   Reduce[(And @@ Thread[CoefficientList[condAuth, kk] == 0]) && H > 0, {AA, be}, Reals] === False &&
   Reduce[authEqB2 && ! authEqB2Expected, {AA, kk}, Reals] === False && Reduce[authEqB2Expected && ! authEqB2, {AA, kk}, Reals] === False &&
   Reduce[authEqA0 && ! (H > 0 && kk == 8), {kk}, Reals] === False && Reduce[(H > 0 && kk == 8) && ! authEqA0, {kk}, Reals] === False,
  "a source with p3 = p_t = p0 (such as the homogeneous condensate: K^mu_mu = 0 for mu != x4, every off-diagonal component zero when the 24 bilinears vanish) needs sum_k alpha_k (E^x1_x1 - E^x0_x0) = 0.  On the exponential histories: Einstein (" <>
   inp[Expand[((u11 - u00) /. hist) /. einst]] <> " = 0): no solution, neither for varying k (every power of k) nor for constant k > 0 (beta = 2 or A = 0).  The author's weights: no solution where k varies; for constant k exactly k0 = (16 + 2 A^2)/(2 + A^2) on beta = 2 (b4 = b4(0) e^{2 A H x4}) and k0 = 8 on the static history A = 0.  " <>
   "On those histories the x4 and x0 equations still need rho = sigmaT (m S + U(S)) and p = sigmaT (S U' - U) with S = e^{a4} b4^{-2} S0 (S ~ e^{-3 A H x4} for A != 0, constant for A = 0) to equal the constant left-hand sides: for A != 0 this requires U(S) = c - m S on the range of S (rho = -p); for A = 0 it fixes S0 and U(S0); not decided further here.  Histories that are not exponential are not decided here"];

(* ======================================================================
   6. a4-equations.json
   ====================================================================== *)
cvsvToCot[e_] := e /. {cv -> cc sv} /. {sv -> 1/Sqrt[1 + cc^2]};   (* display only: cot z = cc *)
offJSON = Table[<|"component" -> "K^" <> coordName[pq[[1]]] <> "_" <> coordName[pq[[2]]] <> " (symmetrised)",
     "terms" -> KeyValueMap[<|"bilinear" -> "Phibar " <> StringRiffle[("gamma^" <> coordName[#]) & /@ #1, " "] <> " Phi",
         "coefficient" -> expr[Together[#2 /. {bd1 -> uu bb}]]|> &, offDecomp[pq]]|>,
   {pq, offPairs}];
compE[k_] := <|"x0x0" -> expr[EkV[[k, 1, 1]]], "x1x1" -> expr[EkV[[k, 2, 2]]], "x4x4" -> expr[EkV[[k, 5, 5]]], "x5x5" -> expr[EkV[[k, 6, 6]]]|>;
data = <|
  "title" -> "Einstein-Lovelock field equations for a4[x4] and b4[x4] in the corrected primordial metric of 2026-10-16 (version 2; Revision/SPEC.md sections 1 and 5), for general functions a4 and b4 > 0 and every real z = 6 H x0",
  "producer" -> "Revision/field_equations_a4/wolfram/verify_field_equations_a4.wls (with FieldEquationsA4.wl)",
  "conventions" -> <|
    "metric" -> "g = diag(E^(-2 a4) b4 Cot[z]^2, E^(2 a4) (x3), -1, -E^(-2 a4) b4 (Sin[z]^2)^(1/6) (x3)), z = 6 H x0 real ((Sin^2)^(1/6) the positive branch); the metric of 2026-10-14 and its formulas are withdrawn",
    "coordinates" -> "the author's coordinates x0..x7: x0 = hidden direction, space-like (scale factor e^{-a4} b4^{1/2} |cot z|); x1, x2, x3 = 3-space (scale factor e^{a4}); x4 = time; x5, x6, x7 = extra times, time-like (scale factor e^{-a4} b4^{1/2} (sin^2 z)^{1/12}); the block (x0, x5, x6, x7) is e^{-2a4} b4 times a space of constant curvature -H^2",
    "symbols" -> "ad1 = a4'(x4), ad2 = a4''(x4), uu = b4'/b4, vv = (b4'/b4)' (b4''/b4 = vv + uu^2), kk = e^{2 a4}/b4 (so kk' = kk (2 ad1 - uu)), hh = uu/2 - ad1 = h4, the rate of the block (x0, x5, x6, x7); H > 0, alpha1..alpha3 = Lovelock couplings, Lam = Lambda, kappa = gravitational coupling, cc = cot z, tt = tan z; AA, be = the parameters of an exponential history; d4f, d0f = partial derivatives of f with respect to x4, x0",
    "curvature" -> "MTW: R^a_{bcd} = d_c Gamma^a_{bd} - d_d Gamma^a_{bc} + Gamma^a_{ce} Gamma^e_{bd} - Gamma^a_{de} Gamma^e_{bc}",
    "lovelock" -> "P_(k)^h_j = GKD[{h,h1..h2k},{j,j1..j2k}] R^{j1j2}_{h1h2} ... R^{j(2k-1)j2k}_{h(2k-1)h2k}; E_(k) = -P_(k)/2^(k+1); E_(1) = G",
    "fieldEquations" -> "sum_{k=1}^{3} alpha_k E_(k)^mu_nu + Lam delta^mu_nu = kappa T^mu_nu",
    "source" -> "T^mu_nu = diag(p0, p3, p3, p3, -rho, p_t, p_t, p_t) (order x0..x7); rho = -T^x4_x4, p_mu = T^mu_mu (no sum); the field equations require every off-diagonal component to vanish and p0 = p_t"|>,
  "lovelockTensors" -> <|"E1" -> compE[1], "E2" -> compE[2], "E3" -> compE[3],
    "allOtherComponents" -> "x2x2 = x3x3 = x1x1, x0x0 = x5x5 = x6x6 = x7x7; every off-diagonal component is 0; every component is a polynomial in H, ad1, ad2, uu, vv, kk (exact, all 64 components checked)"|>,
  "generalSource" -> <|
    "constraint_x4" -> eqn[u44 + Lam, -kappa rho],
    "space_x1_eq_x2_eq_x3" -> eqn[u11 + Lam, kappa p3],
    "hidden_and_extraTimes_x0_eq_x5_eq_x6_eq_x7" -> eqn[u00 + Lam, kappa p0],
    "hiddenEqualsExtraTimes" -> "sum_k alpha_k (E^x0_x0 - E^x5_x5) = 0 identically, so kappa (p0 - p_t) = 0: p0 = p_t",
    "offDiagonal" -> "0 = kappa T^mu_nu for every mu != nu (the left-hand sides vanish identically): no off-diagonal source component, in particular T^x4_x0 = T^x0_x4 = 0",
    "secondOrderSystem" -> "the x1 and x0 components are linear in (ad2, vv) with Jacobian J; det J below; where det J != 0 they determine a4'' and (b4'/b4)' from the sources, and the x4 component is the constraint",
    "secondOrderJacobian" -> expr[jacG],
    "secondOrderJacobianDet" -> expr[detG],
    "x0_dependence" -> "the left-hand sides are free of x0 (and of a4, b4 except through kk), so the source must satisfy d0 rho = d0 p3 = d0 p0 = 0",
    "conservation_x4" -> eqn[-d4rho - 3 ad1 (rho + p3) - 3 hh (rho + pt) - hh (rho + p0) + d0q04 - 3 H (cc + 2 tt) q04, 0],
    "conservation_x0" -> eqn[d0p0 + 3 H cc (p0 - pt) + d4q40 + (3/2) uu q40 - hh cc^2 q04/kk, 0],
    "energyExchange" -> eqn[-d4rho - 3 ad1 (rho + p3) - 4 hh (rho + p0), 0],
    "constraint_propagation" -> "d/dx4 [sum_k alpha_k E^x4_x4] = 3 ad1 (E^x1_x1 - E^x4_x4) + 4 hh (E^x0_x0 - E^x4_x4) identically (the x4 component of the Bianchi identity)",
    "sourceRequiredByGivenHistory" -> <|"rho" -> expr[-(u44 + Lam)/kappa], "p3" -> expr[(u11 + Lam)/kappa], "p0" -> expr[(u00 + Lam)/kappa], "pt" -> expr[(u00 + Lam)/kappa]|>,
    "nullCombinations" -> <|"kappa(rho+p0)" -> expr[nec0], "kappa(rho+p3)" -> expr[nec3]|>|>,
  "einstein" -> <|
    "couplings" -> "alpha1 = 1, alpha2 = alpha3 = 0",
    "constraint_x4" -> eqn[ein44 + Lam, -kappa rho],
    "space_x1" -> eqn[ein11 + Lam, kappa p3],
    "hidden_x0" -> eqn[ein00 + Lam, kappa p0],
    "nullEnergy_x0" -> eqn[kappa (rho + p0), -(3/2) (2 H^2 kk + 4 ad1^2 - ad1 uu + vv)],
    "nullEnergy_x1" -> eqn[kappa (rho + p3), 2 ad2 - 8 ad1^2 + 6 ad1 uu - uu^2 - 2 vv],
    "flatVacuum" -> "a4 = 0, b4 = H^2 (x4 - c)^2 (the flat member of the corrected metric) is a vacuum solution with Lambda = 0",
    "noExponentialVacuum" -> "no exponential history a4 = AA H x4 + a0, b4 = b4(0) e^(be AA H x4) is a vacuum solution, for any Lambda",
    "secondOrderJacobian" -> expr[jacE]|>,
  "exponentialHistory" -> <|
    "history" -> "a4 = AA H x4 + a0, b4 = b4(0) e^(be AA H x4): ad1 = AA H, ad2 = 0, uu = be AA H, vv = 0, kk = (e^{2 a0}/b4(0)) e^{(2 - be) AA H x4} (constant exactly for be = 2 or AA = 0); 3-space scale factor e^{AA H x4}, the block (x0, x5, x6, x7) e^{-(1 - be/2) AA H x4}",
    "requiredSource" -> <|"rho" -> expr[srcRho], "p3" -> expr[srcP3], "p0" -> expr[srcP0], "pt" -> expr[srcP0]|>,
    "einstein" -> <|"rho" -> expr[srcRho /. einst], "p3" -> expr[srcP3 /. einst], "p0" -> expr[srcP0 /. einst]|>,
    "authorWeights" -> <|
      "weights" -> "alpha_k = w_k/H^(2k), w = (1, 1/32, 1/1152), Lam = -10 (Dirac_Einstein-Lovelock_4+4_Nash.nb, Out[134]/Out[135])",
      "recordHistory" -> "AA = 1, be = 4/3, a0 = 0, b4(0) = 1: kk = e^{(2/3) H x4}",
      "historySource_kappaT_minus_Lam" -> <|"minus_rho" -> expr[authHist[[1]]], "p3" -> expr[authHist[[2]]], "p0" -> expr[authHist[[3]]], "pt" -> expr[authHist[[3]]]|>,
      "einsteinHistorySource_kappaT_minus_Lam" -> <|"minus_rho" -> expr[einHist[[1]]], "p3" -> expr[einHist[[2]]], "p0" -> expr[einHist[[3]]], "pt" -> expr[einHist[[3]]]|>,
      "statement" -> "the record's history a4 = H x4, b4 = b4(0) e^((4/3) H x4) needs a diagonal, x0-independent source with p0 = p_t that grows with x4 (powers of kk = e^{(2/3) H x4}); it is not a vacuum solution and is used as a PRESCRIBED background (SPEC section 1)",
      "vacuum" -> "no exponential history is a vacuum solution for the author's weights"|>,
    "einsteinGaussBonnetVacuum" -> "alpha1 = 1, alpha3 = 0: no vacuum exponential history where kk varies; for constant kk = k0 > 0 (be = 2, any AA) exactly k0 != AA^2, alpha2 = -1/(4 H^2 (AA^2 - k0)), Lambda = -E^x4_x4 at the history"|>,
  "fields" -> <|
    "lemmas" -> <|
      "gravityTerm" -> "gamma^mu Omega_mu = (3/2) H e^{a4} b4^{-1/2} gamma^x0 + (b4'/b4 - a4'/2) gamma^x4 (canonical spin connection; Omega_x4 = 0, Omega_x0 = (1/2) cot z e^{-a4} b4^{1/2} hh gamma^x0 gamma^x4)",
      "diagonalKinetic" -> "{gamma^mu, Omega_mu} = 0 for each mu (no sum), so K^mu_mu = (1/2)(Psibar gamma^mu d_mu Psi - d_mu Psibar gamma^mu Psi) contains no spin connection; for a configuration independent of x_mu, K^mu_mu = 0",
      "traceOnShell" -> "sum_mu K^mu_mu = (m + U'(S)) S on shell (both statistics), so the on-shell Lagrangian is L = S U'(S) - U(S)"|>,
    "emtConvention" -> "T^mu_nu = sigmaT ( -K^(mu_nu) + delta^mu_nu L ), K^mu_nu = (1/2)(Psibar gamma^mu D_nu Psi - D_nu Psibar gamma^mu Psi), symmetrised; sigmaT = +1 is the convention of SPEC section 4 (homogeneous on-shell states: rho = m S + U, p = S U' - U)",
    "generalFormulas" -> <|
      "rho" -> "sigmaT ( k4 - L )", "p3" -> "sigmaT ( L - k1 )", "pt" -> "sigmaT ( L - k5 )", "p0" -> "sigmaT ( L - k0 )",
      "kmu" -> "k_mu = K^mu_mu (no sum) = (1/2)(Psibar gamma^mu d_mu Psi - d_mu Psibar gamma^mu Psi); L = k0+k1+k2+k3+k4+k5+k6+k7 - m S - U(S) (on shell S U'(S) - U(S))",
      "offDiagonal" -> "T^mu_nu = -sigmaT K^(mu_nu) for mu != nu must vanish (0 = kappa T^mu_nu), and the field equations need p0 = p_t"|>,
    "dirac16complex00" -> <|
      "statement" -> "classical commuting Phi; k_mu, S, U are classical bilinears",
      "homogeneousCondensate" -> "Phi = Phi(x4) on shell, independent of x0..x3, x5..x7: d4 Phi = A Phi, A = B - (b4'/b4 - a4'/2) I16, B = -M gamma^x4 + (3/2) H e^{a4} b4^{-1/2} gamma^x4 gamma^x0, M = m + U'(S): Phi = e^{a4/2} b4^{-1} chi with chi' = B chi (B^2 = ((9/4) H^2 kk - M^2) I16); S = e^{a4} b4^{-2} S0 (exact); the diagonal kinetic components are K^x4_x4 = M S and 0 for every other direction, and K^x4_x0 = K^x0_x4 = 0; hence rho = sigmaT (m S + U(S)), p3 = p_t = p0 = sigmaT (S U'(S) - U(S))",
      "offDiagonalKinetic" -> offJSON,
      "offDiagonalConditions" -> "the off-diagonal field equations 0 = kappa T^mu_nu require the 24 bilinears B_abc = Phibar gamma^a gamma^b gamma^c Phi (frame gammas) with {a,b,c} = {x0, i, x4}, {x0, i, t}, {i, x4, t}, {x0, x4, t} (i = x1..x3, t = x5..x7) to vanish",
      "offDiagonalWitness" -> "on the histories with constant kk = k0 (b4 = e^{2 a4}/k0, any a4) and constant M: exact solutions with all 24 bilinears zero and S != 0, Phi = e^{a4/2} b4^{-1} e^{-i w x4} Phi0, w = sqrt(M^2 - (9/4) H^2 k0) (M^2 > (9/4) H^2 k0), Phi0 = v1 + c v2 from the two eigenvectors of B for -i w with gamma^x1 gamma^x5 = gamma^x2 gamma^x6 = gamma^x3 gamma^x7 = -1 and +1, c = conj(v1^dagger C v2); checked exactly at (M, H, k0) = (5, 1, 4), (5, 4/3, 4), (-5, 1, 4) (wolfram report, condensate_witness_constant_k_exact); for kk not constant not decided",
      "asSource" -> "the condensate source has p3 = p_t = p0 and no off-diagonal component: it needs sum_k alpha_k (E^x1_x1 - E^x0_x0) = 0; on the exponential histories: no solution in Einstein gravity; for the author's weights only on constant-kk histories, kk = (16 + 2 AA^2)/(2 + AA^2) with be = 2 and kk = 8 with AA = 0 (static), where the x4 and x0 equations further need U(S) = c - m S for AA != 0 (S = e^{a4} b4^{-2} S0 varies) and fix S0 for AA = 0 (wolfram report, condensate_source_equal_pressures); histories that are not exponential are not decided"|>,
    "dirac16complex" -> <|
      "statement" -> "quantised Psi (SPEC section 6): every bilinear is replaced by the expectation value of the normal-ordered operator in the state, <:k_mu:>, <:S:>, <:U(S):> (note <U(S)> != U(<S>) in general); the trace identity sum_mu <:k_mu:> = <:(m + U'(S)) S:> for the normal-ordered operators of the field on a whole slice is ASSUMED here, not proved. It is decided only in a finite model, by Revision/theory/fock_quartic (reports/fock-quartic.json: one good-sector plane-wave mode set with frozen coefficients, flat frame, volume 1, 16 modes, 2^16 states, U = (lambda/2) S^2 with symbolic lambda). Nothing is proved for the field on a whole slice (many momenta), for the curved x0 dependence, or for the extra-time sector",
      "rho" -> "sigmaT ( <:k4:> - <:L:> )", "p3" -> "sigmaT ( <:L:> - <:k1:> )", "pt" -> "sigmaT ( <:L:> - <:k5:> )", "p0" -> "sigmaT ( <:L:> - <:k0:> )",
      "offDiagonal" -> "every off-diagonal expectation value <:T^mu_nu:> (mu != nu) must vanish, and <:p0:> = <:p_t:>",
      "kohnSham" -> "Kohn-Sham source (Revision/kohn_sham): rho_KS(x4), p3_KS(x4), p_t_KS(x4), p0_KS(x4) from the occupied Kohn-Sham orbitals; with this source the equations of generalSource apply with these entries; the source conditions (no off-diagonal component, p0 = p_t, x0-independence) are evaluated in Revision/field_equations_a4/reports/ks-source-conditions.json"|>|>,
  "checksSummary" -> "see reports/wolfram-a4-report.json"|>;

writeJSON[FileNameJoin[{$fieldDir, "a4-equations.json"}], data];

failed = Count[checks, c_ /; c["verdict"] =!= "PASS"];
report = <|"producer" -> "Revision/field_equations_a4/wolfram/verify_field_equations_a4.wls", "spec" -> "Revision/SPEC.md section 5",
   "checkCount" -> Length[checks], "failedCount" -> failed, "verdict" -> If[failed == 0, "PASS", "FAIL"], "checks" -> checks|>;
writeJSON[FileNameJoin[{$fieldDir, "reports", "wolfram-a4-report.json"}], report];
Print["checks: ", Length[checks], ", failed: ", failed];
Scan[If[#["verdict"] =!= "PASS", Print["FAIL ", #["name"], ": ", #["detail"]]] &, checks];
Exit[If[failed == 0, 0, 1]];
