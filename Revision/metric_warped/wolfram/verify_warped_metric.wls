#!/usr/bin/env wolframscript
(* ::Package:: *)

(* verify_warped_metric.wls

   The independent Wolfram check of the self-consistency study of the primordial metric (the user's order of
   2026-10-16) and of the warped metric
       g = diag(Cot[z]^2, E^(2 a4) S, E^(2 a4) S, E^(2 a4) S, -S, -E^(-2 a4) b4 S, -E^(-2 a4) b4 S, -E^(-2 a4) b4 S),
       z = 6 H x0, S = Sin[z]^(1/3),
   which differs from the metric of 2026-10-14 only in g44 (-1 -> -Sin[z]^(1/3)).  It recomputes, with the package
   MetricWarped.wl (the Wolfram record's Christoffel, Riemann and k-delta contraction):
     1. the warped metric: every off-diagonal component of E_(1), E_(2), E_(3) vanishes;
     2. the metric of 2026-10-14: the off-diagonal pair (x4, x0) and its author-weight sum = the record's
        generalSource.offDiagonal_x4x0 (Revision/field_equations_a4/a4-equations.json of commit 04fa2e7, frozen in
        Revision/metric_warped/reference_2026_10_14/a4-offdiagonal-x4x0.json);
     3. the family g00 = b4^(2p) E^(2 q a4) Cot[z]^2, g44 = -Sin[z]^(2 gamma): the Einstein condition q = 0,
        6 gamma + 4 p = 1, and on that line the Gauss-Bonnet component (6 gamma - 1) b4' (4 a4' b4 - b4')^2;
     4. the rejected alternative g00 = b4^(1/2) Cot[z]^2;
     5. the layers E_(k) = sum_j c_kj H^(2(k-j)) Sin[z]^(-j/3) Ehat_(j) with the 7-dimensional fiber computed separately;
     6. the Kasner vacuum of Einstein gravity with Lambda = -21 H^2;
     7. the source of the history a4 = H x4, b4 = E^(4 H x4/3) (Einstein and the author's weights) = the sympy result
        Revision/metric_warped/results/warped-metric.json;
     8. sqrt|det g| and the gravity term gamma^mu Omega_mu of the Dirac operator.
   Writes Revision/metric_warped/reports/wolfram-warped-metric-report.json (UTF-8, LF, no time stamps).  Exit code 0
   if every check passes.  Usage (repository root):
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
z = 6 H x0; S = Sin[z]^(1/3);
metric[g00f_, g44_] := {g00f Cot[z]^2, E^(2 a4[x4]) S, E^(2 a4[x4]) S, E^(2 a4[x4]) S, g44,
   -E^(-2 a4[x4]) b4[x4] S, -E^(-2 a4[x4]) b4[x4] S, -E^(-2 a4[x4]) b4[x4] S};
zeroQ[e_, extra_: True] := TrueQ[MWSimplify[e, extra] === 0];
offPairs = Select[Tuples[Range[n], 2], #[[1]] != #[[2]] &];

(* ---- 1. the warped metric ---- *)
gW = metric[1, -S];
curvW = MWCurvature[gW, xs];
lap["curvature_warped"];
mixedW = Select[curvW["nonzeroMixed"], Sort[#[[1, 1 ;; 2]]] =!= Sort[#[[1, 3 ;; 4]]] &];
check["warped_mixed_riemann_vanish", mixedW === {},
  "warped metric: every nonzero R^{ab}_{cd} has {a, b} = {c, d} (" <> ToString[Length[curvW["nonzeroMixed"]]] <> " nonzero entries with ordered pairs)"];
offW = Table[MWLovelock[k, curvW, n, offPairs], {k, 3}];
lap["lovelock_offdiagonal_warped"];
check["warped_offdiagonal_all_orders", AllTrue[Flatten[offW], # === 0 &],
  "warped metric: the 56 off-diagonal components of E_(1), E_(2), E_(3) are identically 0 for all a4[x4], b4[x4] > 0"];
diagW = Table[MWLovelock[k, curvW, n, Table[{h, h}, {h, n}]], {k, 3}];
lap["lovelock_diagonal_warped"];

(* ---- 2. the metric of 2026-10-14 ---- *)
gR = metric[1, -1];
curvR = MWCurvature[gR, xs];
eR = Table[First[MWLovelock[k, curvR, n, {{5, 1}}]], {k, 3}];
offR1 = MWLovelock[1, curvR, n, offPairs];
a4eq = Import[FileNameJoin[{$root, "Revision", "metric_warped", "reference_2026_10_14", "a4-offdiagonal-x4x0.json"}], "RawJSON"];
recText = First[StringSplit[a4eq["generalSource.offDiagonal_x4x0"]["input"], "=="]];
recLHS = ToExpression[recText] /. {cc -> Cot[z], uu -> Derivative[1][b4][x4]/b4[x4], ad1 -> Derivative[1][a4][x4]};
ourLHS = alpha1 eR[[1]] + alpha2 eR[[2]] + alpha3 eR[[3]];
check["record_metric_offdiagonal_reproduced",
  zeroQ[ourLHS - recLHS] && Count[offR1, Except[0]] == 2 && AllTrue[eR, ! zeroQ[#] &],
  "metric of 2026-10-14: E_(1) has exactly 2 nonzero off-diagonal components ((x4, x0), (x0, x4)); E_(k)^x4_x0 != 0 for k = 1, 2, 3; sum_k alpha_k E_(k)^x4_x0 = the record's generalSource.offDiagonal_x4x0 (cot z u Q); E_(1)^x4_x0 = " <> ToString[InputForm[MWSimplify[eR[[1]]]]]];
lap["record_metric"];

(* ---- 3. the family ---- *)
famAss = Element[gam, Reals] && Element[p, Reals] && Element[q, Reals];
gF = metric[b4[x4]^(2 p) E^(2 q a4[x4]), -Sin[z]^(2 gam)];
curvF = MWCurvature[gF, xs, famAss];
eF1 = First[MWLovelock[1, curvF, n, {{5, 1}}, famAss]];
expF1 = -3 H Cot[z] Sin[z]^(-2 gam) (4 q Derivative[1][a4][x4] b4[x4] + (6 gam + 4 p - 1) Derivative[1][b4][x4])/(2 b4[x4]);
offF1 = MWLovelock[1, curvF, n, offPairs, famAss];
check["family_einstein_condition", zeroQ[eF1 - expF1, famAss] && Count[offF1, Except[0]] == 2,
  "g00 = b4^(2p) E^(2 q a4) Cot[z]^2, g44 = -Sin[z]^(2 gamma): E_(1)^x4_x0 = -(3 H Cot[z] Sin[z]^(-2 gamma)/(2 b4)) (4 q a4' b4 + (6 gamma + 4 p - 1) b4'), the only off-diagonal pair; zero for all a4, b4 iff q = 0 and 6 gamma + 4 p = 1"];
lap["family_einstein"];
gLn = metric[b4[x4]^((1 - 6 gam)/2), -Sin[z]^(2 gam)];
curvLn = MWCurvature[gLn, xs, Element[gam, Reals]];
eLn2 = First[MWLovelock[2, curvLn, n, {{5, 1}}, Element[gam, Reals]]];
expLn2 = 3/2 H Cot[z] Sin[z]^(-4 gam) (6 gam - 1) Derivative[1][b4][x4] (4 Derivative[1][a4][x4] b4[x4] - Derivative[1][b4][x4])^2/b4[x4]^3;
check["family_gauss_bonnet_condition", zeroQ[eLn2 - expLn2, Element[gam, Reals]],
  "on the line q = 0, p = (1 - 6 gamma)/4: E_(2)^x4_x0 = (3/2) H Cot[z] Sin[z]^(-4 gamma) (6 gamma - 1) b4' (4 a4' b4 - b4')^2/b4^3: zero for all a4, b4 iff gamma = 1/6 (the warped metric)"];
lap["family_gauss_bonnet"];

(* ---- 4. the rejected alternative ---- *)
gHid = metric[Sqrt[b4[x4]], -1];
curvHid = MWCurvature[gHid, xs];
offHid1 = MWLovelock[1, curvHid, n, offPairs];
eHid2 = First[MWLovelock[2, curvHid, n, {{5, 1}}]];
eHid3 = First[MWLovelock[3, curvHid, n, {{5, 1}}]];
check["alternative_hidden_breathing_einstein_only",
  AllTrue[offHid1, # === 0 &] && zeroQ[eHid2 + 3/2 H Cot[z] Derivative[1][b4][x4] (4 Derivative[1][a4][x4] b4[x4] - Derivative[1][b4][x4])^2/b4[x4]^3] && ! zeroQ[eHid3],
  "g00 = b4^(1/2) Cot[z]^2 (g44 = -1): E_(1) diagonal; E_(2)^x4_x0 = -(3/2) H Cot[z] b4' (4 a4' b4 - b4')^2/b4^3 != 0; E_(3)^x4_x0 != 0"];
lap["alternative"];

(* ---- 5. layers ---- *)
xf = {x1, x2, x3, x4, x5, x6, x7};
gFib = {E^(2 a4[x4]), E^(2 a4[x4]), E^(2 a4[x4]), -1, -E^(-2 a4[x4]) b4[x4], -E^(-2 a4[x4]) b4[x4], -E^(-2 a4[x4]) b4[x4]};
curvFib = MWCurvature[gFib, xf];
fibT = Table[MWLovelock[j, curvFib, 7, Table[{h, h}, {h, 7}]], {j, 3}];
fibS = Table[MWLovelockScalar[j, curvFib, 7], {j, 3}];
cc0 = <|{1, 0} -> 21, {1, 1} -> 1, {2, 0} -> -420, {2, 1} -> -40, {2, 2} -> 1, {3, 0} -> 2520, {3, 1} -> 360,
   {3, 2} -> -18, {3, 3} -> 1|>;
layerOK = And @@ Flatten[Table[
     Module[{fib},
      fib[j_] := If[j == 0, 1, If[mu == 1, fibS[[j]], fibT[[j, mu - 1]]]];
      zeroQ[diagW[[k, mu]] - Sum[cc0[{k, j}] H^(2 (k - j)) Sin[z]^(-j/3) fib[j], {j, 0, k}]]],
     {k, 3}, {mu, n}]];
check["warped_layer_decomposition", layerOK,
  "E_(k)^mu_mu = sum_{j=0..k} c_kj H^(2(k-j)) Sin[z]^(-j/3) Ehat_(j) (mu = x1..x7: the fiber tensor Ehat_(j)^mu_mu; mu = x0: the fiber scalar Ehat_(j)^(0)); c_10..c_33 = 21, 1; -420, -40, 1; 2520, 360, -18, 1"];
lap["layers"];

(* ---- 6. Kasner vacuum of Einstein gravity ---- *)
kasOK = And @@ Flatten[Table[
     Module[{ps = (1 + sg Sqrt[5])/6, sub},
      sub = {a4 -> Function[t, ps Log[t]], b4 -> Function[t, t^(2/3)]};
      Table[TrueQ[Simplify[(diagW[[1, mu]] /. sub) - 21 H^2, x4 > 0 && H > 0 && 0 < z < Pi/2] === 0], {mu, n}]],
     {sg, {1, -1}}]];
check["einstein_vacuum_kasner", kasOK,
  "Einstein gravity, Lambda = -21 H^2: a4 = ps Log[x4], b4 = x4^(2/3), ps = (1 +- Sqrt[5])/6 solve all 64 components at every x0 (the off-diagonal ones vanish identically)"];
lap["kasner"];

(* ---- 7. the source of the history ---- *)
py = Import[FileNameJoin[{$root, "Revision", "metric_warped", "results", "warped-metric.json"}], "RawJSON"];
toW[s_String] := ToExpression[StringReplace[s, {"**" -> "^", "sqrt(" -> "Sqrt[", ")" -> ")"}]] /. {W -> Sin[z]^(-1/3)};
histSub = {a4 -> Function[t, H t], b4 -> Function[t, E^(4 H t/3)]};
idx = <|"p0" -> 1, "p3" -> 2, "-rho" -> 5, "p_t" -> 6|>;
srcOK = And @@ Table[
    zeroQ[(diagW[[1, idx[key]]] /. histSub) - toW[py["history_source"]["einstein_A1_beta43"][key]]] &&
    zeroQ[((diagW[[1, idx[key]]]/H^2 + (1/32) diagW[[2, idx[key]]]/H^4 + (1/1152) diagW[[3, idx[key]]]/H^6) /. histSub) -
       toW[py["history_source"]["author_weights_A1_beta43"][key]]],
    {key, Keys[idx]}];
check["history_source_equals_sympy", srcOK,
  "on a4 = H x4, b4 = E^(4 H x4/3): E_(1)^mu_mu and the author-weight sum E_(1)/H^2 + E_(2)/(32 H^4) + E_(3)/(1152 H^6) equal the sympy values of warped-metric.json (history_source) for rho, p3, p_t, p0"];
lap["history"];

(* ---- 8. sqrt|det g| and the gravity term of the Dirac operator ---- *)
check["sqrt_det_g", zeroQ[Sqrt[Abs[Times @@ gW]] - b4[x4]^(3/2) Cos[z] Sin[z]^(1/6)],
  "sqrt|det g| = b4^(3/2) Cos[z] Sin[z]^(1/6)"];
fSpace = E^a4[x4] Sin[z]^(1/6);
fExtra = E^(-a4[x4]) Sqrt[b4[x4]] Sin[z]^(1/6);
fW = Join[{Cot[z]}, ConstantArray[fSpace, 3], {Sin[z]^(1/6)}, ConstantArray[fExtra, 3]];
vol = Times @@ fW;
coefs = Table[MWSimplify[1/2 D[vol/fW[[a]], xs[[a]]]/vol], {a, n}];
check["dirac_gravity_term",
  zeroQ[coefs[[1]] - 7/2 H] && zeroQ[coefs[[5]] - 3/4 Derivative[1][b4][x4]/b4[x4] Sin[z]^(-1/6)] && AllTrue[coefs[[{2, 3, 4, 6, 7, 8}]], zeroQ],
  "gamma^mu Omega_mu = (1/2) sum_a gamma^(a) (1/sqrt g) d_a (sqrt g/f_a) = (7/2) H gamma^(x0) + (3/4) (b4'/b4) Sin[z]^(-1/6) gamma^(x4)"];
End[];

report = <|"program" -> "Revision/metric_warped/wolfram/verify_warped_metric.wls", "checks" -> checks|>;
outFile = FileNameJoin[{$root, "Revision", "metric_warped", "reports", "wolfram-warped-metric-report.json"}];
Export[outFile, StringReplace[ExportString[report, "RawJSON", "Compact" -> False], "\r\n" -> "\n"] <> "\n", "Text",
  CharacterEncoding -> "UTF-8"];
npass = Count[checks, c_ /; c["verdict"] == "PASS"];
Print["wolfram_warped_metric=", If[npass == Length[checks], "OK", "FAIL"], " (", npass, " of ", Length[checks], ") seconds=",
  Round[AbsoluteTime[] - $t0, 0.1]];
Exit[If[npass == Length[checks], 0, 1]];
