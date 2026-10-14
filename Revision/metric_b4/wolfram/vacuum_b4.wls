#!/usr/bin/env wolframscript
(* ::Package:: *)

(* vacuum_b4.wls

   The vacuum Einstein-Lovelock equations of the metric of 2026-10-14 (with b4[x4]) with the author's weights
   w1 = 1, w2 = 1/32, w3 = 1/1152, Lambda = 10 (the author's Out[134]/Out[135] of
   Dirac_Einstein-Lovelock_4+4_Nash.nb): which histories (a4, b4) solve them?

   Reads Revision/metric_b4/results/metric-b4.json (written by verify_metric_b4.wls) and proves, with exact
   algebra (every step is a check):
     V1  E^4_4 (the time-time equation) contains no second derivative: it is a constraint
         C(alpha, beta) = 0 in alpha = a4'/H and beta = b4'/(H b4).
     V2  E^x4_x0 = Cot[6 H x0] b4' Q(alpha, beta) / (2 H^5 b4^3 ...) and E^x0_x4 = -Tan[6 H x0] (the same):
         the off-diagonal equation is beta Q(alpha, beta) = 0.
     V3  the real solutions of {C = 0, Q = 0} are finitely many points (alpha, beta); at each of them some
         diagonal equation fails (checked with the exponential ansatz a4 = alpha H x4, b4 = e^{beta H x4},
         which is forced at such a point because alpha, beta are then constant).
     V4  hence on every interval where b4' != 0 there is no solution: every C^2 vacuum solution has b4' = 0,
         b4 = constant > 0 (a rescaling of x5, x6, x7, i.e. the metric before 2026-10-14), and then
         C(alpha, 0) = -16 (alpha^2 - 1)^2 (alpha^2 + 5)/256 ... = 0 gives a4' = +H or -H: a4 = +-H x4 + const.
     V5  the full set of equations with b4 = const, a4 = +-H x4 is satisfied (the author's solution and its
         time reverse).
   Writes Revision/metric_b4/results/vacuum-b4.json.  Exit 0 if every check passes.
   Coordinates: the author's x0..x7 (x0 = the hidden direction, Wolfram position 1; x4 at position 5).
   Usage (repository root): wolframscript -file Revision/metric_b4/wolfram/vacuum_b4.wls *)

$here = DirectoryName[$InputFileName];
$root = ParentDirectory[$here, 3];
$res = FileNameJoin[{$root, "Revision", "metric_b4", "results"}];
Get[FileNameJoin[{$here, "MetricB4.wl"}]];
If[! ValueQ[MetricB4`MB4Coordinates], Print["ERROR: MetricB4.wl did not load"]; Exit[1]];
src = FileNameJoin[{$res, "metric-b4.json"}];
If[! FileExistsQ[src], Print["ERROR: run verify_metric_b4.wls first"]; Exit[1]];
d = Import[src, "RawJSON"];
toE[s_] := Block[{$Context = "MetricB4`", $ContextPath = {"MetricB4`", "System`"}}, ToExpression[s]];
checks = {};
check[name_, ok_, detail_] := (AppendTo[checks, <|"name" -> name, "verdict" -> If[TrueQ[ok], "PASS", "FAIL"], "detail" -> detail|>];
  Print["check_", name, "=", If[TrueQ[ok], "PASS", "FAIL"]]);

Hs = MetricB4`H; x4s = MetricB4`x4; x0s = MetricB4`x0;
wts = {MetricB4`w1 -> 1, MetricB4`w2 -> 1/32, MetricB4`w3 -> 1/1152, MetricB4`Lambda -> 10};
lab = {"x0", "x1", "x2", "x3", "x4", "x5", "x6", "x7"};
Ek[k_] := Table[With[{v = d["E" <> ToString[k] <> "Mixed"][lab[[h]] <> "," <> lab[[j]]]}, If[MissingQ[v], 0, toE[v]]], {h, 8}, {j, 8}];
vac = -MetricB4`Lambda IdentityMatrix[8] + MetricB4`w1 Ek[1]/Hs^2 + MetricB4`w2 Ek[2]/Hs^4 + MetricB4`w3 Ek[3]/Hs^6;
vacW = vac /. wts;
(* local variables: alpha = a4'/H, beta = b4'/(H b4), and second derivatives p = a4''/H^2, q = b4''/(H^2 b4) *)
loc = {Derivative[2][MetricB4`a4][x4s] -> p Hs^2, Derivative[2][MetricB4`b4][x4s] -> q Hs^2 MetricB4`b4[x4s]};
loc1 = {Derivative[1][MetricB4`a4][x4s] -> al Hs, Derivative[1][MetricB4`b4][x4s] -> be Hs MetricB4`b4[x4s]};
toLoc[e_] := Simplify[(e /. loc) /. loc1, Hs > 0 && MetricB4`b4[x4s] > 0 && 0 < 6 Hs x0s < Pi/2];
E44 = toLoc[vacW[[5, 5]]];  (* x4, x4 *)
check["V1_time_time_is_constraint", FreeQ[E44, p] && FreeQ[E44, q] && FreeQ[E44, x0s] && FreeQ[E44, MetricB4`b4[x4s]],
  "E^x4_x4 = C(alpha, beta) with no second derivative, no x0 and no b4 beyond beta: C = " <> ToString[InputForm[Factor[E44]]]];
E48 = toLoc[vacW[[5, 1]]]; E84 = toLoc[vacW[[1, 5]]];  (* E^x4_x0 and E^x0_x4 (the names E48, E84 are those of the withdrawn labels) *)
Qpoly = Factor[Numerator[Together[E48/(Cot[6 Hs x0s] be)]]];
check["V2_off_diagonal_is_beta_Q", Simplify[E48 - Cot[6 Hs x0s] be Qpoly/Denominator[Together[E48/(Cot[6 Hs x0s] be)]]] === 0 &&
   Simplify[E84 + Tan[6 Hs x0s] be Qpoly/Denominator[Together[E48/(Cot[6 Hs x0s] be)]]] === 0 && FreeQ[Qpoly, x0s],
  "E^x4_x0 = Cot[6 H x0] beta Q/den, E^x0_x4 = -Tan[6 H x0] beta Q/den, Q = " <> ToString[InputForm[Qpoly]]];
Cpoly = Numerator[Together[E44]];
pts = Solve[{Cpoly == 0, Qpoly == 0}, {al, be}, Reals];
check["V3a_constraint_and_Q_isolated_points", ListQ[pts] && Length[pts] < Infinity && AllTrue[pts, NumericQ[al /. #] && NumericQ[be /. #] &],
  "the real solutions of {C = 0, Q = 0} are the points " <> ToString[InputForm[pts]]];
diagExp = Function[{alv, bev}, DeleteDuplicates[Simplify[vacW /. {MetricB4`a4 -> (alv Hs # &), MetricB4`b4 -> (Exp[bev Hs #] &)}, Hs > 0 && 0 < 6 Hs x0s < Pi/2] // Flatten]];
bad = Select[pts, (be /. #) != 0 &];
fails = Table[With[{r = diagExp[al /. pt, be /. pt]}, {pt, DeleteCases[r, 0]}], {pt, bad}];
check["V3b_no_solution_with_beta_nonzero", AllTrue[fails, Length[#[[2]]] > 0 &],
  "at every point with beta != 0 some equation fails (nonzero residuals): " <> ToString[InputForm[N[fails, 6]]]];
C0 = Factor[Cpoly /. be -> 0];
roots0 = Solve[C0 == 0, al, Reals];
check["V4_b4_constant_branch", Union[al /. roots0] === {-1, 1},
  "with b4' = 0 the constraint is " <> ToString[InputForm[C0]] <> " = 0; real roots alpha = " <> ToString[al /. roots0]];
full = Table[Simplify[(vacW /. {MetricB4`a4 -> (sgn Hs # + a0 &), MetricB4`b4 -> (cB &)}), Hs > 0 && cB > 0 && 0 < 6 Hs x0s < Pi/2], {sgn, {1, -1}}];
check["V5_author_solution_and_time_reverse", AllTrue[Flatten[full], # === 0 &],
  "a4 = +-H x4 + a0, b4 = cB > 0 (any constants) solve all 64 equations with w1 = 1, w2 = 1/32, w3 = 1/1152, Lambda = 10"];
out = <|"program" -> "Revision/metric_b4/wolfram/vacuum_b4.wls",
  "weights" -> "w1 = 1, w2 = 1/32, w3 = 1/1152, Lambda = 10 (the author's Out[135])",
  "variables" -> "alpha = a4'/H, beta = b4'/(H b4), p = a4''/H^2, q = b4''/(H^2 b4)",
  "constraintE44" -> ToString[InputForm[Factor[E44]]], "offDiagonalQ" -> ToString[InputForm[Qpoly]],
  "isolatedPoints" -> ToString[InputForm[pts]], "constraintAtBeta0" -> ToString[InputForm[C0]],
  "theorem" -> "Every C^2 solution (a4, b4), b4 > 0, of the author's vacuum Einstein-Lovelock equations (w1 = 1, w2 = 1/32, w3 = 1/1152, Lambda = 10) for the metric with b4 has b4 = constant and a4 = +H x4 + const or -H x4 + const; a constant b4 is the rescaling x5,6,7 -> sqrt(b4) x5,6,7, so the vacuum history is the author's solution (b4 = 1, a4 = H x4) or its time reverse.",
  "checks" -> checks, "checkCount" -> Length[checks], "failedCount" -> Count[checks, c_ /; c["verdict"] =!= "PASS"]|>;
s = ExportString[out, "JSON", "Compact" -> False];
If[Quiet[BinaryWrite[FileNameJoin[{$res, "vacuum-b4.json"}], StringToByteArray[s <> "\n", "UTF-8"]]] === $Failed, Print["ERROR: cannot write vacuum-b4.json"]; Exit[1]];
Close[FileNameJoin[{$res, "vacuum-b4.json"}]];
Print["checks=", Length[checks], " failed=", out["failedCount"]];
Print["vacuum_b4=", If[out["failedCount"] == 0, "OK", "FAILED"]];
Exit[If[out["failedCount"] == 0, 0, 1]];
