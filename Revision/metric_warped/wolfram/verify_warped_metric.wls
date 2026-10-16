#!/usr/bin/env wolframscript
(* ::Package:: *)

(* verify_warped_metric.wls  (version 2, 2026-10-16)

   The independent Wolfram check of the self-consistency study of the primordial metric and of the CORRECTED metric
       g = diag(E^(-2 a4) b4 Cot[z]^2, E^(2 a4), E^(2 a4), E^(2 a4), -1, -E^(-2 a4) b4 S, -E^(-2 a4) b4 S, -E^(-2 a4) b4 S),
       z = 6 H x0 real, S = (Sin[z]^2)^(1/6)  (the author's Sin[z]^(1/3), positive branch),
   for every real z (the user's rules of 2026-10-16: x0 space-like, x4 the time, -Infinity < z < Infinity, g44 cannot
   oscillate, Sin^(1/3) = (Sin^2)^(1/6)).  With the package MetricWarped.wl (the Wolfram record's Christoffel, Riemann
   and k-delta contraction, and an exact normal form valid for every real z) it recomputes:
     1. the corrected metric: vielbein and volume; no mixed Riemann component; no off-diagonal component of E_(1),
        E_(2), E_(3); diagonal components independent of x0; the block (x0, x5, x6, x7) has constant curvature -H^2;
     2. the family with g44 = -1 and its conditions; the condition of Einstein gravity alone;
     3. the metric of 2026-10-14: its off-diagonal pair = the record's generalSource.offDiagonal_x4x0 (frozen in
        Revision/metric_warped/reference_2026_10_14/a4-offdiagonal-x4x0.json);
     4. version 1 (g44 = -Sin[z]^(1/3)) oscillates in z (withdrawn);
     5. the Ricci tensor and scalar, the source of the history and the gravity term of the Dirac operator equal the
        sympy record Revision/metric_warped/results/warped-metric.json; the divergence of a diagonal tensor;
     6. the alternatives K (g00 = E^(2 a4) Cot[z]^2) and g00 = b4^(1/2) Cot[z]^2.
   Writes Revision/metric_warped/reports/wolfram-warped-metric-report.json (UTF-8, LF, no time stamps).  Exit code 0
   if every check passes.  Usage (repository root), after derive_warped_metric.py:
     wolframscript -file Revision/metric_warped/wolfram/verify_warped_metric.wls *)

$t0 = AbsoluteTime[];
$here = DirectoryName[$InputFileName];
$root = ParentDirectory[$here, 3];
Get[FileNameJoin[{$here, "MetricWarped.wl"}]];
If[! ValueQ[MetricWarped`MWCoordinates], Print["ERROR: MetricWarped.wl did not load"]; Exit[1]];
lap[name_] := Print["time_", name, "=", Round[AbsoluteTime[] - $t0, 0.1]];
checks = {};
check[name_String, ok_, detail_String] := (AppendTo[checks, <|"name" -> name, "verdict" -> If[TrueQ[ok], "PASS", "FAIL"],
     "detail" -> detail|>]; Print["check_", name, "=", If[TrueQ[ok], "PASS", "FAIL"]]);

Begin["MetricWarped`"];
xs = MWCoordinates; n = 8;
z = 6 H x0; S = (Sin[z]^2)^(1/6);
metric[g00_, gs_, g44_, gt_] := {g00, gs, gs, gs, g44, gt, gt, gt};
offPairs = Select[Tuples[Range[n], 2], #[[1]] != #[[2]] &];
diagPairs = Table[{h, h}, {h, n}];
mixedOf[curv_] := Select[curv["nonzeroMixed"], Sort[#[[1, 1 ;; 2]]] =!= Sort[#[[1, 3 ;; 4]]] &];
a4p = Derivative[1][a4][x4]; b4p = Derivative[1][b4][x4]; u = b4p/b4[x4];
(* v and core are linear in a4', b4'; propQ: v = (nonzero factor free of a4', b4') core *)
propQ[v_, core_] := Module[{vv = v /. {a4p -> A1, b4p -> B1}, cc = core /. {a4p -> A1, b4p -> B1}},
  Simplify[vv - A1 D[vv, A1] - B1 D[vv, B1]] === 0 && Simplify[D[vv, A1] D[cc, B1] - D[vv, B1] D[cc, A1]] === 0 &&
  Simplify[D[vv, A1] D[cc, A1] + D[vv, B1] D[cc, B1]] =!= 0];

(* ---- 1. the corrected metric ---- *)
gC = metric[E^(-2 a4[x4]) b4[x4] Cot[z]^2, E^(2 a4[x4]), -1, -E^(-2 a4[x4]) b4[x4] S];
fC = Join[{E^(-a4[x4]) Sqrt[b4[x4]] Cot[z]}, ConstantArray[E^a4[x4], 3], {1},
   ConstantArray[E^(-a4[x4]) Sqrt[b4[x4]] (Sin[z]^2)^(1/12), 3]];
etaD = {1, 1, 1, 1, -1, -1, -1, -1};
check["corrected_metric_entries",
  MWZeroQ[etaD fC^2 - gC] && MWZeroQ[Times @@ fC - E^(-a4[x4]) b4[x4]^2 Cot[z] (Sin[z]^2)^(1/4)] &&
  MWNormal[gC[[6]] + E^(-2 a4[x4]) b4[x4] w^2] === 0,
  "every real z: the vielbein f0 = E^(-a4) b4^(1/2) Cot[z], f_i = E^a4, f4 = 1, f_t = E^(-a4) b4^(1/2) (Sin[z]^2)^(1/12) " <>
  "reproduces g; f0 ... f7 = E^(-a4) b4^2 Cot[z] (Sin[z]^2)^(1/4), so sqrt|det g| = E^(-a4) b4^2 |Cot[z]| (Sin[z]^2)^(1/4); " <>
  "g_tt = -E^(-2 a4) b4 w^2 < 0 with w = (Sin[z]^2)^(1/12) > 0; g44 = -1"];
curvC = MWCurvature[gC, xs];
lap["curvature_corrected"];
check["corrected_mixed_riemann_vanish", mixedOf[curvC] === {},
  "corrected metric, every real z: every nonzero R^{ab}_{cd} has {a, b} = {c, d} (" <>
  ToString[Length[curvC["nonzeroMixed"]]] <> " nonzero entries with ordered pairs)"];
offC = Table[MWLovelock[k, curvC, offPairs], {k, 3}];
diagC = Table[MWLovelock[k, curvC, diagPairs], {k, 3}];
lap["lovelock_corrected"];
check["corrected_offdiagonal_all_orders",
  AllTrue[Flatten[offC], # === 0 &] && AllTrue[Flatten[diagC], FreeQ[#, sv | cv | w | x0] &],
  "corrected metric: the 56 off-diagonal components of E_(1), E_(2), E_(3) are identically 0 for all a4[x4], " <>
  "b4[x4] > 0 and every real z, and all diagonal components are independent of x0"];
curvB = MWCurvature[{Cot[z]^2, -S, -S, -S}, {x0, x5, x6, x7}];
blockOK = Sort[curvB["nonzeroMixed"][[All, 1]]] ===
    Sort[Flatten[Table[{{a, b, a, b}, {a, b, b, a}, {b, a, a, b}, {b, a, b, a}}, {a, 4}, {b, a + 1, 4}], 2]] &&
  AllTrue[Select[curvB["nonzeroMixed"], #[[1, 1]] < #[[1, 2]] && #[[1, 1]] == #[[1, 3]] &], MWZeroQ[#[[2]] + H^2] &];
check["hidden_block_constant_curvature", blockOK,
  "the block Cot[z]^2 dx0^2 - (Sin[z]^2)^(1/6) (dx5^2 + dx6^2 + dx7^2): R^{ab}_{ab} = -H^2 for the six pairs a < b " <>
  "and no other independent component: constant curvature -H^2 for every real z (in the corrected metric the block " <>
  "carries the factor E^(-2 a4) b4)"];
lap["block"];

(* ---- 2. the family with g44 = -1 ---- *)
gF = metric[b4[x4]^(2 p) E^(2 q a4[x4]) Cot[z]^2, E^(2 a4[x4]) (Sin[z]^2)^(3 al), -1,
   -E^(-2 a4[x4]) b4[x4] (Sin[z]^2)^(3 be)];
chrF = Module[{g = DiagonalMatrix[gF], gi = DiagonalMatrix[1/gF]},
  Table[1/2 Sum[gi[[a, d]] (D[g[[d, c]], xs[[b]]] + D[g[[d, b]], xs[[c]]] - D[g[[b, c]], xs[[d]]]), {d, n}],
   {a, n}, {b, n}, {c, n}]];
(* R^{ab}_{cd} = g^{bb} R^a_{bcd} (diagonal metric) *)
riemF[a_, b_, c_, d_] := (1/gF[[b]]) (D[chrF[[a, d, b]], xs[[c]]] - D[chrF[[a, c, b]], xs[[d]]] +
     Sum[chrF[[a, c, f]] chrF[[f, d, b]] - chrF[[a, d, f]] chrF[[f, c, b]], {f, n}]);
coreS = al ((q - 1) a4p + p u); coreT = be ((q + 1) a4p + (p - 1/2) u);
famFactor = 18 H Tan[z] E^(-2 q a4[x4]) b4[x4]^(-2 p);
famOK = AllTrue[Range[2, 4], propQ[riemF[1, #, 5, #], coreS] && Simplify[riemF[1, #, 5, #] - famFactor coreS] === 0 &] &&
  AllTrue[Range[6, 8], propQ[riemF[1, #, 5, #], coreT] && Simplify[riemF[1, #, 5, #] - famFactor coreT] === 0 &];
check["family_g44_fixed_conditions", famOK,
  "family g00 = b4^(2p) E^(2 q a4) Cot[z]^2, g_ii = E^(2 a4) (Sin[z]^2)^(3 al), g44 = -1, " <>
  "g_tt = -E^(-2 a4) b4 (Sin[z]^2)^(3 be): R^{x0 xi}_{x4 xi} = 18 H Tan[z] E^(-2 q a4) b4^(-2 p) al ((q - 1) a4' + p b4'/b4) " <>
  "and R^{x0 xt}_{x4 xt} = 18 H Tan[z] E^(-2 q a4) b4^(-2 p) be ((q + 1) a4' + (p - 1/2) b4'/b4) for every real z: " <>
  "both vanish for all a4, b4 iff [al = 0 or (q, p) = (1, 0)] and [be = 0 or (q, p) = (-1, 1/2)]"];
curvF1 = MWCurvature[gF /. {al -> 1/6, be -> 1/6}, xs];
eF1 = First[MWLovelock[1, curvF1, {{5, 1}}]];
check["family_einstein_condition", propQ[eF1, 2 q a4p + (2 p - 1/2) u],
  "with both of the author's warps (al = be = 1/6) E_(1)^x4_x0 is (nonzero factor) (2 q a4' + (2 p - 1/2) b4'/b4): " <>
  "zero for all a4, b4 iff q = 0, p = 1/4 (g00 = b4^(1/2) Cot[z]^2)"];
lap["family"];

(* ---- 3. the metric of 2026-10-14 ---- *)
gR = metric[Cot[z]^2, E^(2 a4[x4]) S, -1, -E^(-2 a4[x4]) b4[x4] S];
curvR = MWCurvature[gR, xs];
eR = Table[First[MWLovelock[k, curvR, {{5, 1}}]], {k, 3}];
offR1 = MWLovelock[1, curvR, offPairs];
ref = Import[FileNameJoin[{$root, "Revision", "metric_warped", "reference_2026_10_14", "a4-offdiagonal-x4x0.json"}], "RawJSON"];
recLHS = ToExpression[First[StringSplit[ref["generalSource.offDiagonal_x4x0"]["input"], "=="]]] /.
   {cc -> Cot[z], uu -> u, ad1 -> a4p};
check["record_metric_offdiagonal_reproduced",
  MWZeroQ[alpha1 eR[[1]] + alpha2 eR[[2]] + alpha3 eR[[3]] - recLHS] && Count[offR1, Except[0]] == 2 &&
  NoneTrue[eR, MWZeroQ],
  "metric of 2026-10-14 (every real z): E_(1) has exactly 2 nonzero off-diagonal components ((x4, x0), (x0, x4)); " <>
  "E_(k)^x4_x0 != 0 for k = 1, 2, 3; sum_k alpha_k E_(k)^x4_x0 = the record's generalSource.offDiagonal_x4x0 (cot z u Q)"];
lap["record_metric"];

(* ---- 4. version 1 ---- *)
g44v1 = -(Sin[z]^2)^(1/6);
check["version_1_g44_oscillates",
  Simplify[(g44v1 /. x0 -> x0 + Pi/(6 H)) - g44v1] === 0 && (g44v1 /. x0 -> 0) === 0 && (g44v1 /. x0 -> Pi/(12 H)) === -1,
  "version 1 (withdrawn): g44 = -(Sin[z]^2)^(1/6) has period Pi in z, is -1 at z = Pi/2 and 0 at z = 0: " <>
  "the lapse of the time x4 oscillates and vanishes for real z"];

(* ---- 5. comparisons with the sympy record ---- *)
py = Import[FileNameJoin[{$root, "Revision", "metric_warped", "results", "warped-metric.json"}], "RawJSON"];
ricC = Table[MWNormal[Total[Select[curvC["nonzeroMixed"],
       #[[1, 1]] == a && #[[1, 3]] == a && #[[1, 2]] == #[[1, 4]] &][[All, 2]]]], {a, n}];
ricPy = Table[ReleaseHold[ToExpression[py["ricci_mixed_diagonal_mathematica"]["x" <> ToString[a - 1]]]], {a, n}];
check["ricci_tensor",
  MWZeroQ[ricC - ricPy] && MWZeroQ[Total[ricC] - ReleaseHold[ToExpression[py["ricci_scalar_mathematica"]]]] &&
  AllTrue[ricC, FreeQ[#, sv | cv | w] &],
  "the Ricci tensor R^a_a = sum_b R^{ab}_{ab} and the Ricci scalar of the corrected metric equal the sympy record " <>
  "(ricci_mixed_diagonal_mathematica, ricci_scalar_mathematica); both are independent of x0"];
histSub = {a4 -> Function[t, H t], b4 -> Function[t, E^(4 H t/3)]};
idx = <|"p0" -> 1, "p3" -> 2, "-rho" -> 5, "p_t" -> 6|>;
srcOK = AllTrue[Keys[idx], Function[key,
    MWZeroQ[(diagC[[1, idx[key]]] /. histSub) - ToExpression[py["history_source"]["einstein_A1_beta43_mathematica"][key]]] &&
    MWZeroQ[((diagC[[1, idx[key]]]/H^2 + diagC[[2, idx[key]]]/(32 H^4) + diagC[[3, idx[key]]]/(1152 H^6)) /. histSub) -
       ToExpression[py["history_source"]["author_weights_A1_beta43_mathematica"][key]]]]];
check["history_source_equals_sympy", srcOK,
  "on the history a4 = H x4, b4 = E^(4 H x4/3): E_(1)^mu_mu and the author-weight sum " <>
  "E_(1)/H^2 + E_(2)/(32 H^4) + E_(3)/(1152 H^6) equal the sympy values (history_source) for -rho, p3, p_t, p0"];
Module[{T, gm, div, h, exp4, exp0},
  gm = curvC["christoffel"];
  T = DiagonalMatrix[{p0[x0, x4], p3[x0, x4], p3[x0, x4], p3[x0, x4], -rho[x0, x4], pt[x0, x4], pt[x0, x4], pt[x0, x4]}];
  div = Table[Sum[D[T[[m, nu]], xs[[m]]], {m, n}] + Sum[gm[[m, m, l]] T[[l, nu]], {m, n}, {l, n}] -
      Sum[gm[[l, m, nu]] T[[m, l]], {m, n}, {l, n}], {nu, n}];
  h = u/2 - a4p;
  exp4 = -D[rho[x0, x4], x4] - 3 a4p (rho[x0, x4] + p3[x0, x4]) - 3 h (rho[x0, x4] + pt[x0, x4]) -
    h (rho[x0, x4] + p0[x0, x4]);
  exp0 = D[p0[x0, x4], x0] + 3 H Cot[z] (p0[x0, x4] - pt[x0, x4]);
  check["divergence_of_diagonal_tensor",
    MWZeroQ[div[[5]] - exp4] && MWZeroQ[div[[1]] - exp0] && MWZeroQ[div[[{2, 3, 4, 6, 7, 8}]]],
    "corrected metric, T = diag(p0, p3, p3, p3, -rho, p_t, p_t, p_t) depending on x0, x4: nabla_mu T^mu_x4 = " <>
    "-d4 rho - 3 a4' (rho + p3) - 3 h (rho + p_t) - h (rho + p0), h = b4'/(2 b4) - a4'; nabla_mu T^mu_x0 = " <>
    "d0 p0 + 3 H Cot[z] (p0 - p_t); the six other components vanish (every real z)"]];
volC = Times @@ fC;
coefs = Table[MWNormal[1/2 D[volC/fC[[a]], xs[[a]]]/volC], {a, n}];
check["dirac_gravity_term",
  MWZeroQ[coefs[[1]] - 3/2 H E^a4[x4]/Sqrt[b4[x4]]] && MWZeroQ[coefs[[5]] - (u - a4p/2)] &&
  AllTrue[coefs[[{2, 3, 4, 6, 7, 8}]], # === 0 &],
  "gamma^mu Omega_mu = sum_a gamma^(a) (1/(2 V)) d_a (V/f_a), V = f0 ... f7: " <>
  "(3/2) H E^a4 b4^(-1/2) gamma^(x0) + (b4'/b4 - a4'/2) gamma^(x4) for every real z (= the sympy record: " <>
  py["dirac_gravity_term"] <> ")"];
lap["comparisons"];

(* ---- 6. alternatives ---- *)
gK = metric[E^(2 a4[x4]) Cot[z]^2, E^(2 a4[x4]) S, -1, -E^(-2 a4[x4]) b4[x4]];
curvK = MWCurvature[gK, xs];
okK = mixedOf[curvK] === {} && AllTrue[Flatten[Table[MWLovelock[k, curvK, offPairs], {k, 3}]], # === 0 &];
gEin = metric[Sqrt[b4[x4]] Cot[z]^2, E^(2 a4[x4]) S, -1, -E^(-2 a4[x4]) b4[x4] S];
curvE = MWCurvature[gEin, xs];
e2Ein = First[MWLovelock[2, curvE, {{5, 1}}]];
okE = AllTrue[MWLovelock[1, curvE, offPairs], # === 0 &] &&
  MWZeroQ[e2Ein + 3/2 H Cot[z] b4p (4 a4p b4[x4] - b4p)^2/b4[x4]^3];
check["alternatives", okK && okE,
  "alternative K (g00 = E^(2 a4) Cot[z]^2, 3-space E^(2 a4) S, extra times without the warp S): no mixed Riemann component and no " <>
  "off-diagonal component at any order; g00 = b4^(1/2) Cot[z]^2 (both warps): E_(1) diagonal, but " <>
  "E_(2)^x4_x0 = -(3/2) H Cot[z] b4' (4 a4' b4 - b4')^2/b4^3 != 0"];
lap["alternatives"];
End[];

report = <|"program" -> "Revision/metric_warped/wolfram/verify_warped_metric.wls", "version" -> 2, "checks" -> checks|>;
outFile = FileNameJoin[{$root, "Revision", "metric_warped", "reports", "wolfram-warped-metric-report.json"}];
Module[{s = ExportString[report, "RawJSON", "Compact" -> False]},
  If[! StringQ[s], Print["ERROR: JSON export failed"]; Exit[1]];
  s = StringReplace[s, "\r\n" -> "\n"];
  If[Quiet[BinaryWrite[outFile, StringToByteArray[s <> "\n", "UTF-8"]]] === $Failed, Print["ERROR: cannot write ", outFile];
    Exit[1]];
  Close[outFile]];
npass = Count[checks, c_ /; c["verdict"] == "PASS"];
Print["wolfram_warped_metric=", If[npass == Length[checks], "OK", "FAIL"], " (", npass, " of ", Length[checks],
  ") seconds=", Round[AbsoluteTime[] - $t0, 0.1]];
Exit[If[npass == Length[checks], 0, 1]];
