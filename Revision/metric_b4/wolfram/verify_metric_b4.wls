#!/usr/bin/env wolframscript
(* ::Package:: *)

(* verify_metric_b4.wls

   Computes the curvature, the Lovelock tensors k = 1, 2, 3 and the vacuum Einstein-Lovelock equations of the
   primordial metric of 2026-10-14 (with b4[x4]; package MetricB4.wl) and checks them against
     (A) the author's STORED outputs of Dirac_Einstein-Lovelock_4+4_Nash.nb (results/author-b4-outputs.json,
         written by extract_author_b4_outputs.wls; nothing of the notebook is evaluated),
     (B) the earlier Revision record at b4 = 1 (the files curvature.json and lovelock-tensors.json of
         Revision/gkd_lovelock/results computed before 2026-10-14 for the metric without b4, frozen in
         Revision/metric_b4/reference_b4_1/ from commit e3e35fe),
     (C) exact identities (the divergence of every Lovelock tensor vanishes; constant b4 drops out of every
         curvature quantity; sqrt|det g| = b4^(3/2) Cos[6 H x0]; the only off-diagonal entries are (x0, x4)
         and (x4, x0), each proportional to b4'[x4]).
   Coordinates: the author's x0, x1, ..., x7 in the author's order (x0 = the hidden direction, Wolfram position 1; xk at
   position k + 1).  The frozen b4 = 1 record of (B) is in the withdrawn labels x1..x8 (hidden x8 last); it is read
   through the map x8 -> x0, xk -> xk.
   Writes Revision/metric_b4/results/metric-b4.json (the components) and wolfram-metric-b4-report.json (the
   checks).  UTF-8, LF, no time stamps in the outputs (times are printed only).  Exit code 0 if every check
   passes, 1 otherwise (or on any ERROR).
   Usage (repository root): wolframscript -file Revision/metric_b4/wolfram/verify_metric_b4.wls *)

$t0 = AbsoluteTime[];
$here = DirectoryName[$InputFileName];
$root = ParentDirectory[$here, 3];
$res = FileNameJoin[{$root, "Revision", "metric_b4", "results"}];
If[! FileExistsQ[FileNameJoin[{$here, "MetricB4.wl"}]], Print["ERROR: MetricB4.wl not found"]; Exit[1]];
Get[FileNameJoin[{$here, "MetricB4.wl"}]];
If[! ValueQ[MetricB4`MB4Coordinates], Print["ERROR: MetricB4.wl did not load"]; Exit[1]];
lap[name_] := Print["time_", name, "=", Round[AbsoluteTime[] - $t0, 0.1]];

checks = {};
check[name_String, ok_, detail_String] := (AppendTo[checks, <|"name" -> name, "verdict" -> If[TrueQ[ok], "PASS", "FAIL"], "detail" -> detail|>];
  Print["check_", name, "=", If[TrueQ[ok], "PASS", "FAIL"]]);
zeroQ[e_] := TrueQ[MetricB4`MB4Simplify[e] === 0];
sameQ[a_, b_] := And @@ Flatten[MapThread[zeroQ[#1 - #2] &, {a, b}, ArrayDepth[a]]];

(* ---- curvature and Lovelock tensors ---- *)
curv = MetricB4`MB4Curvature[]; lap["curvature"];
lov = Association[Table[k -> MetricB4`MB4Lovelock[k, curv], {k, 3}]]; lap["lovelock"];
E1 = lov[1]["E"]; E2 = lov[2]["E"]; E3 = lov[3]["E"];
g = curv["metric"];

(* ---- (A) the author's stored outputs ---- *)
authorFile = FileNameJoin[{$res, "author-b4-outputs.json"}];
If[! FileExistsQ[authorFile], Print["ERROR: run extract_author_b4_outputs.wls first"]; Exit[1]];
author = Import[authorFile, "RawJSON"];
toExpr[s_String] := Block[{$Context = "MetricB4`", $ContextPath = {"MetricB4`", "System`"}},
  ReleaseHold[ToExpression[StringReplace[s, {"X0" -> "x0", "X1" -> "x1", "X2" -> "x2", "X3" -> "x3", "X4" -> "x4",
     "X5" -> "x5", "X6" -> "x6", "X7" -> "x7"}]]]];
cell[l_] := toExpr[author["cells"][l]];
authorMetric = cell["Out[101]"];
check["metric_equals_author_Out101",
  sameQ[Diagonal[g], Diagonal[authorMetric]] && Count[Flatten[authorMetric - DiagonalMatrix[Diagonal[authorMetric]]], Except[0]] == 0,
  "the metric of MetricB4.wl equals the author's stored MatrixMetric44 (Out[101]) component by component, in the author's coordinates x0..x7"];
check["ricci_scalar_equals_author_Out119", zeroQ[curv["ricciScalar"] - cell["Out[119]"]], "R = the author's RicciScalarCD (Out[119])"];
check["einstein_equals_author_Out120", sameQ[curv["einsteinMixed"], MetricB4`MB4AuthorToRevision[cell["Out[120]"]]],
  "G^h_j = the author's EinsteinCD[-a, b] (Out[120]), all 64 components (the author's coordinates; only the index placement is converted)"];
check["ricci_mixed_equals_author_Out124", sameQ[curv["ricciMixed"], MetricB4`MB4AuthorToRevision[cell["Out[124]"]]],
  "R^h_j = the author's RicciCD[-a, b] (Out[124])"];
With[{rcov = Table[MetricB4`MB4Simplify[Sum[g[[a, c]] curv["ricciMixed"][[c, b]], {c, 8}]], {a, 8}, {b, 8}], A = cell["Out[123]"]},
  check["ricci_covariant_equals_author_Out123", sameQ[rcov, A],
    "R_hj = the author's RicciCD[-a, -b] (Out[123])"]];
check["lovelock1_equals_author_Out126", sameQ[E1, MetricB4`MB4AuthorToRevision[cell["Out[126]"]]], "E_(1) = the author's allLovelock1 (Out[126])"];
check["lovelock2_equals_author_Out127", sameQ[E2, MetricB4`MB4AuthorToRevision[cell["Out[127]"]]], "E_(2) = the author's allLovelock2 (Out[127])"];
check["lovelock3_equals_author_Out128", sameQ[E3, MetricB4`MB4AuthorToRevision[cell["Out[128]"]]], "E_(3) = the author's allLovelock3 (Out[128])"];
lap["author_A"];
vac = -MetricB4`Lambda IdentityMatrix[8] + MetricB4`w1 E1/MetricB4`H^2 + MetricB4`w2 E2/MetricB4`H^4 + MetricB4`w3 E3/MetricB4`H^6;
check["vacuum_equations_equal_author_Out129", sameQ[vac, MetricB4`MB4AuthorToRevision[cell["Out[129]"]]],
  "-Lambda delta + w1 E_(1)/H^2 + w2 E_(2)/H^4 + w3 E_(3)/H^6 = the author's EinsteinLovelockVacuumFieldEquations (Out[129])"];
distinct = DeleteCases[DeleteDuplicates[MetricB4`MB4Simplify /@ Flatten[vac], zeroQ[#1 - #2] &], 0];
authorDistinct = cell["Out[132]"];
check["distinct_equations_equal_author_Out132",
  Length[distinct] == Length[authorDistinct] && And @@ (Function[e, Or @@ (zeroQ[e - #] & /@ distinct)] /@ authorDistinct),
  "the distinct nonzero entries of the vacuum equations = the author's eqsELei00 (Out[132]): " <> ToString[Length[distinct]] <> " entries"];
sol = distinct /. {MetricB4`b4 -> (1 &), MetricB4`a4 -> (MetricB4`H # &), MetricB4`w1 -> 1, MetricB4`w2 -> 1/32};
sol = DeleteDuplicates[MetricB4`MB4Simplify /@ sol];
authorSol = cell["Out[134]"];
check["author_solution_equations_Out134", Sort[DeleteCases[sol, 0]] === Sort[DeleteDuplicates[DeleteCases[authorSol, 0]]],
  "with b4 = 1, a4 = H x4, w1 = 1, w2 = 1/32 the equations reduce to the author's Out[134]: " <> ToString[DeleteCases[sol, 0], InputForm]];
solved = Solve[Thread[DeleteCases[sol, 0] == 0], {MetricB4`w3, MetricB4`Lambda}];
check["author_solution_Out135", solved === cell["Out[135]"],
  "Solve gives " <> ToString[solved, InputForm] <> " = the author's Out[135] (w3 = 1/1152, Lambda = 10)"];
lap["author_B"];

(* ---- (B) b4 = 1 reproduces the earlier Revision record ---- *)
one = {MetricB4`b4 -> (1 &)};
(* the record BEFORE 2026-10-14 (metric without b4), frozen from commit e3e35fe in Revision/metric_b4/reference_b4_1/ (the
   files of Revision/gkd_lovelock/results now carry b4); their sha256 are the pins of that record.  That record is in the
   withdrawn labels x1..x8 (hidden x8 last): it is read through the map x8 -> x0, xk -> xk (old name of position p below) *)
refDir = FileNameJoin[{$root, "Revision", "metric_b4", "reference_b4_1"}];
refShaOK = IntegerString[FileHash[FileNameJoin[{refDir, "curvature.json"}], "SHA256"], 16, 64] === "d5beb73a32244ea938ca61eac3573f72061c0e329b78f7506dd983881638763e" &&
   IntegerString[FileHash[FileNameJoin[{refDir, "lovelock-tensors.json"}], "SHA256"], 16, 64] === "9278a0bf0da9ac7b2b22be5bb39e44073e821efb741514f42a43fa9cbc978567";
check["reference_b4_1_files_are_the_earlier_record", refShaOK,
  "Revision/metric_b4/reference_b4_1/curvature.json (sha256 d5beb73a...) and lovelock-tensors.json (9278a0bf...) are the files of Revision/gkd_lovelock/results at commit e3e35fe, before the metric change (the sha256 pinned by Revision/tests/test_gkd_lovelock.py then)"];
recCurv = Import[FileNameJoin[{refDir, "curvature.json"}], "RawJSON"];
recLov = Import[FileNameJoin[{refDir, "lovelock-tensors.json"}], "RawJSON"];
recExpr[s_String] := Block[{$Context = "MetricB4`", $ContextPath = {"MetricB4`", "System`"}},
  ToExpression[StringReplace[s, RegularExpression["x8(?![0-9])"] -> "x0"]]];
lab = {"x0", "x1", "x2", "x3", "x4", "x5", "x6", "x7"};
oldLab = {"x8", "x1", "x2", "x3", "x4", "x5", "x6", "x7"};  (* the withdrawn name of the author's x0, x1, ..., x7 *)
recMixed[key_] := Table[With[{v = recCurv[key][oldLab[[h]] <> "," <> oldLab[[j]]]}, If[v === Missing["KeyAbsent", oldLab[[h]] <> "," <> oldLab[[j]]], 0, recExpr[If[StringQ[v], v, v["mathematica"]]]]], {h, 8}, {j, 8}];
recP[k_] := Table[recExpr[recLov["P" <> ToString[k] <> "_mixed_up_h_down_j"][oldLab[[h]] <> "," <> oldLab[[j]]]["mathematica"]], {h, 8}, {j, 8}];
check["b4_one_ricci_scalar_equals_record", zeroQ[(curv["ricciScalar"] /. one) - recExpr[recCurv["ricciScalar"]]],
  "R at b4 = 1 = curvature.json ricciScalar (the record before 2026-10-14)"];
check["b4_one_einstein_equals_record", sameQ[curv["einsteinMixed"] /. one, recMixed["einsteinMixed"]], "G^h_j at b4 = 1 = curvature.json einsteinMixed"];
check["b4_one_ricci_equals_record", sameQ[curv["ricciMixed"] /. one, recMixed["ricciMixed"]], "R^h_j at b4 = 1 = curvature.json ricciMixed"];
Do[check["b4_one_lovelock" <> ToString[k] <> "_equals_record", sameQ[(lov[k]["E"] /. one), -recP[k]/2^(k + 1)],
  "E_(" <> ToString[k] <> ") at b4 = 1 = -P_(" <> ToString[k] <> ")/2^" <> ToString[k + 1] <> " of lovelock-tensors.json"], {k, 3}];
lap["record"];

(* ---- (C) exact identities ---- *)
xs = MetricB4`MB4Coordinates; chr = curv["christoffel"];
div[E_] := Table[MetricB4`MB4Simplify[Sum[D[E[[h, j]], xs[[h]]], {h, 8}] + Sum[chr[[h, h, l]] E[[l, j]], {h, 8}, {l, 8}] - Sum[chr[[l, h, j]] E[[h, l]], {h, 8}, {l, 8}]], {j, 8}];
Do[check["lovelock" <> ToString[k] <> "_divergence_free", And @@ (zeroQ /@ div[lov[k]["E"]]), "nabla_h E_(" <> ToString[k] <> ")^h_j = 0 for every j, general a4 and b4"], {k, 3}];
check["sqrt_det_g", zeroQ[curv["sqrtAbsDetG"] - MetricB4`b4[MetricB4`x4]^(3/2) Cos[6 MetricB4`H MetricB4`x0]],
  "sqrt|det g| = b4[x4]^(3/2) Cos[6 H x0] (b4 = 1: Cos[6 H x0] as before; the 7-volume element is no longer constant in x4 unless b4 is)"];
constB = {MetricB4`b4 -> (cB &)};
check["constant_b4_drops_out",
  And @@ (zeroQ /@ Flatten[{D[curv["ricciScalar"] /. constB, cB], D[curv["einsteinMixed"] /. constB, cB], D[E2 /. constB, cB], D[E3 /. constB, cB]}]),
  "a constant b4 = cB > 0 drops out of R, G and E_(2), E_(3) (it is the rescaling x5,6,7 -> sqrt(cB) x5,6,7)"];
offd = Flatten[Table[If[h != j && ! zeroQ[E1[[h, j]] E1[[h, j]] + E2[[h, j]]^2 + E3[[h, j]]^2], {h, j}, Nothing], {h, 8}, {j, 8}], 1];
(* Wolfram positions: 1 = x0, 5 = x4 *)
check["off_diagonal_entries_x0_x4_only", Sort[offd] === {{1, 5}, {5, 1}}, "the only nonzero off-diagonal entries of E_(1), E_(2), E_(3) are (h, j) = " <> StringRiffle[(lab[[#[[1]]]] <> "," <> lab[[#[[2]]]]) & /@ Sort[offd], "; "]];
noB1 = {Derivative[1][MetricB4`b4][MetricB4`x4] -> 0, Derivative[2][MetricB4`b4][MetricB4`x4] -> 0};
check["off_diagonal_proportional_to_b4prime",
  And @@ (zeroQ /@ Flatten[(Function[{h, j}, {E1[[h, j]], E2[[h, j]], E3[[h, j]]}] @@@ {{1, 5}, {5, 1}}) /. Derivative[1][MetricB4`b4][MetricB4`x4] -> 0]),
  "E_(k)^x0_x4 and E_(k)^x4_x0 vanish when b4' = 0 (k = 1, 2, 3)"];
check["e1_equals_einstein", sameQ[E1, curv["einsteinMixed"]], "E_(1) = -P_(1)/4 = G"];
lap["identities"];

(* ---- outputs ---- *)
str[e_] := ToString[e, InputForm, PageWidth -> Infinity];
mixedAssoc[M_] := Association[Flatten[Table[If[M[[h, j]] === 0, Nothing, (lab[[h]] <> "," <> lab[[j]]) -> str[M[[h, j]]]], {h, 8}, {j, 8}]]];
out = <|
  "program" -> "Revision/metric_b4/wolfram/verify_metric_b4.wls",
  "metricAsGiven" -> "{{Cot[6 H x0[]]^2,0,0,0,0,0,0,0},{0,E^(2 a4[x4[]]) Sin[6 H x0[]]^(1/3),0,0,0,0,0,0},{0,0,E^(2 a4[x4[]]) Sin[6 H x0[]]^(1/3),0,0,0,0,0},{0,0,0,E^(2 a4[x4[]]) Sin[6 H x0[]]^(1/3),0,0,0,0},{0,0,0,0,-1,0,0,0},{0,0,0,0,0,-E^(-2 a4[x4[]]) b4[x4[]] Sin[6 H x0[]]^(1/3),0,0},{0,0,0,0,0,0,-E^(-2 a4[x4[]]) b4[x4[]] Sin[6 H x0[]]^(1/3),0},{0,0,0,0,0,0,0,-E^(-2 a4[x4[]]) b4[x4[]] Sin[6 H x0[]]^(1/3)}}",
  "coordinates" -> lab, "coordinateMap" -> "the author's coordinates x0..x7 of the notebook, in the author's order (identity; x0 = the hidden direction)",
  "metricDiagonal" -> (str /@ Diagonal[g]), "sqrtAbsDetG" -> str[curv["sqrtAbsDetG"]],
  "christoffelNonzero" -> Flatten[Table[If[chr[[a, b, c]] === 0 || b > c, Nothing, <|"a" -> lab[[a]], "b" -> lab[[b]], "c" -> lab[[c]], "value" -> str[chr[[a, b, c]]]|>], {a, 8}, {b, 8}, {c, 8}]],
  "riemannMixedNonzeroCount" -> Length[curv["nonzeroMixed"]],
  "riemannMixedNonzero" -> (<|"index" -> lab[[#[[1]]]], "value" -> str[#[[2]]]|> & /@ curv["nonzeroMixed"]),
  "ricciMixed" -> mixedAssoc[curv["ricciMixed"]], "ricciScalar" -> str[curv["ricciScalar"]],
  "einsteinMixed" -> mixedAssoc[curv["einsteinMixed"]],
  "lovelockNormalisation" -> "E_(k)^h_j = -P_(k)^h_j / 2^(k+1), P_(k)^h_j = kdelta[{j,j1..j2k},{h,h1..h2k}] R^{j1j2}_{h1h2} ...; E_(1) = G",
  "E1Mixed" -> mixedAssoc[E1], "E2Mixed" -> mixedAssoc[E2], "E3Mixed" -> mixedAssoc[E3],
  "kDeltaCalls" -> <|"k1" -> lov[1]["kDeltaCalls"], "k2" -> lov[2]["kDeltaCalls"], "k3" -> lov[3]["kDeltaCalls"]|>,
  "vacuumEquations" -> "-Lambda delta^h_j + w1 E_(1)^h_j/H^2 + w2 E_(2)^h_j/H^4 + w3 E_(3)^h_j/H^6 = 0 (the author's Out[129])",
  "vacuumDistinctEntries" -> (str /@ distinct),
  "authorSolution" -> <|"substitution" -> "b4 = 1, a4 = H x4, w1 = 1, w2 = 1/32", "reduced" -> (str /@ DeleteCases[sol, 0]), "solve" -> str[solved]|>
|>;
report = <|"program" -> "Revision/metric_b4/wolfram/verify_metric_b4.wls", "checks" -> checks,
  "checkCount" -> Length[checks], "failedCount" -> Count[checks, c_ /; c["verdict"] =!= "PASS"],
  "authorNotebookSha256" -> author["notebookSha256"],
  "wolframVersion" -> ToString[$VersionNumber] <> "." <> ToString[$ReleaseNumber]|>;
writeJSON[file_, data_] := Module[{s = ExportString[data, "JSON", "Compact" -> False]},
  If[! StringQ[s], Print["ERROR: JSON export failed for ", file]; Exit[1]];
  If[Quiet[BinaryWrite[file, StringToByteArray[s <> "\n", "UTF-8"]]] === $Failed, Print["ERROR: cannot write ", file]; Exit[1]]; Close[file]];
writeJSON[FileNameJoin[{$res, "metric-b4.json"}], out];
writeJSON[FileNameJoin[{$res, "wolfram-metric-b4-report.json"}], report];
lap["total"];
Print["checks=", Length[checks], " failed=", report["failedCount"]];
Print["metric_b4_wolfram=", If[report["failedCount"] == 0, "OK", "FAILED"]];
Exit[If[report["failedCount"] == 0, 0, 1]];
