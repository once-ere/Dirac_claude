(* ::Package:: *)

(* MetricWarped.wl

   Curvature and Lovelock tensors of a DIAGONAL metric given as a list of its diagonal entries, for the
   self-consistency study of the primordial metric (Revision/metric_warped/, the user's order of 2026-10-16).
   Context MetricWarped`.  Driven by verify_warped_metric.wls.  Independent of the sympy program
   Revision/metric_warped/python/derive_warped_metric.py: here the Christoffel symbols, the Riemann tensor and the
   generalized Kronecker delta contraction are those of the Wolfram record (the GKD record's metric-independent
   functions LGKDLovelockPruned and LGKDCombine, with the author's k-delta), the sympy program contracts by the sign of
   the permutation.

   Every real z = 6 H x0 (the user's rule of 2026-10-16: -Infinity < z < Infinity; Sin[6 H x0]^(1/3) means
   (Sin[6 H x0]^2)^(1/6), the positive branch).  No assumption on the sign of Sin or Cos is made: the exact normal form
   MWNormal writes Sin[z] = sv, Cos[z] = cv (signed) and (Sin[z]^2)^k = w^(12 k) with w = (Sin[z]^2)^(1/12) > 0, and
   reduces numerator and denominator modulo cv^2 + sv^2 - 1 and w^12 - sv^2.

   Conventions (the Revision record's, as in Revision/metric_b4/wolfram/MetricB4.wl):
     Christoffel  Gamma^a_{bc} = (1/2) g^{ad} (d_b g_dc + d_c g_db - d_d g_bc)
     Riemann      R^a_{bcd} = d_c Gamma^a_{db} - d_d Gamma^a_{cb} + Gamma^a_{ce} Gamma^e_{db} - Gamma^a_{de} Gamma^e_{cb}
     mixed        R^{ab}_{cd} = g^{be} R^a_{ecd}
     Lovelock     P_(k)^h_j = kdelta[{j, j1..j2k}, {h, h1..h2k}] R^{j1 j2}_{h1 h2} ..., E_(k) = -P_(k)/2^(k+1),
                  E_(1) = Einstein
   Arrays of mixed tensors: M[[h, j]] = T^h_j (upper index first).  The coordinates are the author's x0..x7 (x0 the
   hidden space-like direction first, x4 the time).
   License: GPL-3.0-or-later.  Pure ASCII on purpose (WolframScript on Windows reads sources as ISO8859-1). *)

BeginPackage["MetricWarped`"];

H::usage = "H > 0, the author's constant.";
a4::usage = "a4[x4], the metric function of the 3-space and extra-time scale factors.";
b4::usage = "b4[x4] > 0, the metric function of the three extra-time components.";
x0::usage = "the author's coordinates x0 .. x7 (x0 is the hidden direction).";
x1::usage = x0::usage; x2::usage = x0::usage; x3::usage = x0::usage; x4::usage = x0::usage;
x5::usage = x0::usage; x6::usage = x0::usage; x7::usage = x0::usage;
sv::usage = "Sin[6 H x0] in the normal form (signed)."; cv::usage = "Cos[6 H x0] in the normal form (signed).";
w::usage = "(Sin[6 H x0]^2)^(1/12) > 0 in the normal form.";

MWCoordinates::usage = "MWCoordinates = {x0, x1, ..., x7}.";
MWNormal::usage = "MWNormal[expr] is the exact normal form for every real z (see the header).";
MWZeroQ::usage = "MWZeroQ[expr] is True iff the normal form is 0.";
MWX0FreeQ::usage = "MWX0FreeQ[expr] is True iff the normal form contains neither sv, cv nor w.";
MWCurvature::usage = "MWCurvature[diag, coords] gives <|christoffel, nonzeroMixed|> of the diagonal metric DiagonalMatrix[diag] (the mixed Riemann components in the normal form).";
MWLovelock::usage = "MWLovelock[k, curv, pairs] gives the list of E_(k)^h_j (normal form) for the index pairs {h, j}.";
MWLovelockScalar::usage = "MWLovelockScalar[k, curv, n] gives E_(k)^(0) = Sum_h E_(k)^h_h / (n - 2 k).";

Begin["`Private`"];

Block[{$ContextPath = $ContextPath},
  Quiet[Get[FileNameJoin[{ParentDirectory[DirectoryName[$InputFileName], 2], "gkd_lovelock", "verification", "LovelockGKDCheck.wl"}]], General::shdw]];

MWCoordinates = {x0, x1, x2, x3, x4, x5, x6, x7};
trig = {(Sin[6 H x0]^2)^k_ :> w^(12 k), Sin[6 H x0] -> sv, Cos[6 H x0] -> cv, Cot[6 H x0] -> cv/sv,
   Tan[6 H x0] -> sv/cv, Csc[6 H x0] -> 1/sv, Sec[6 H x0] -> 1/cv, Sin[12 H x0] -> 2 sv cv, Cos[12 H x0] -> cv^2 - sv^2};
rdc[p_] := Module[{q = Expand[p]},
  If[q === 0, 0, Last[PolynomialReduce[q, {cv^2 + sv^2 - 1, w^12 - sv^2}, {cv, w, sv}]]]];
MWNormal[e_] := Module[{t = Together[(e //. trig) /. (w^12)^k_ :> sv^(2 k)]},
  Together[rdc[Numerator[t]]/rdc[Denominator[t]]]];
MWZeroQ[e_] := MWNormal[e] === 0;
MWZeroQ[e_List] := AllTrue[Flatten[e], MWZeroQ];
MWX0FreeQ[e_] := FreeQ[MWNormal[e], sv | cv | w];

MWCurvature[diag_List, xs_List] := Module[{n = Length[xs], g, gi, chr, riem, mixed, nonzero},
  g = DiagonalMatrix[diag];
  gi = DiagonalMatrix[1/diag];
  chr = Table[1/2 Sum[gi[[a, d]] (D[g[[d, c]], xs[[b]]] + D[g[[d, b]], xs[[c]]] - D[g[[b, c]], xs[[d]]]), {d, n}],
    {a, n}, {b, n}, {c, n}];
  riem = Table[D[chr[[a, d, b]], xs[[c]]] - D[chr[[a, c, b]], xs[[d]]]
      + Sum[chr[[a, c, e]] chr[[e, d, b]] - chr[[a, d, e]] chr[[e, c, b]], {e, n}],
    {a, n}, {b, n}, {c, n}, {d, n}];
  mixed = Table[MWNormal[Sum[gi[[b, e]] riem[[a, e, c, d]], {e, n}]], {a, n}, {b, n}, {c, n}, {d, n}];
  nonzero = Flatten[Table[If[mixed[[a, b, c, d]] =!= 0, {{{a, b, c, d}, mixed[[a, b, c, d]]}}, {}],
    {a, n}, {b, n}, {c, n}, {d, n}], 4];
  <|"christoffel" -> chr, "nonzeroMixed" -> nonzero|>
];

MWLovelock[k_Integer?Positive, curv_Association, pairs_List] := Module[
  {entries = curv["nonzeroMixed"], values},
  values = entries[[All, 2]];
  Table[
    With[{r = LovelockGKDCheck`LGKDLovelockPruned[k, entries, pr]},
      MWNormal[-LovelockGKDCheck`LGKDCombine[r["terms"], values]/2^(k + 1)]],
    {pr, pairs}]
];

MWLovelockScalar[k_Integer?Positive, curv_Association, n_Integer] := Module[{diag},
  diag = MWLovelock[k, curv, Table[{h, h}, {h, n}]];
  MWNormal[Total[diag]/(n - 2 k)]
];

End[];
EndPackage[];
