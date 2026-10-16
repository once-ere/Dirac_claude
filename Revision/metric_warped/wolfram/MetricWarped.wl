(* ::Package:: *)

(* MetricWarped.wl

   Curvature and Lovelock tensors of a DIAGONAL metric given as a list of its diagonal entries, for the
   self-consistency study of the primordial metric (Revision/metric_warped/, the user's order of 2026-10-16).
   Context MetricWarped`.  Driven by verify_warped_metric.wls.  Independent of the sympy program
   Revision/metric_warped/python/derive_warped_metric.py: here the Christoffel symbols, the Riemann tensor and the
   generalized Kronecker delta contraction are those of the Wolfram record (the GKD record's metric-independent
   functions LGKDLovelockPruned and LGKDCombine, with the author's k-delta), the sympy program contracts by the sign of
   the permutation.

   Conventions (the Revision record's, as in Revision/metric_b4/wolfram/MetricB4.wl):
     Christoffel  Gamma^a_{bc} = (1/2) g^{ad} (d_b g_dc + d_c g_db - d_d g_bc)
     Riemann      R^a_{bcd} = d_c Gamma^a_{db} - d_d Gamma^a_{cb} + Gamma^a_{ce} Gamma^e_{db} - Gamma^a_{de} Gamma^e_{cb}
     mixed        R^{ab}_{cd} = g^{be} R^a_{ecd}
     Lovelock     P_(k)^h_j = kdelta[{j, j1..j2k}, {h, h1..h2k}] R^{j1 j2}_{h1 h2} ..., E_(k) = -P_(k)/2^(k+1),
                  E_(1) = Einstein; the scalar E_(k)^(0) = -(1/2^(k+1)) kdelta[{j1..j2k},{h1..h2k}] R...R
   Arrays of mixed tensors: M[[h, j]] = T^h_j (upper index first).  The coordinates are the author's x0..x7 (x0 the
   hidden direction first, x4 the time).
   License: GPL-3.0-or-later.  Pure ASCII on purpose (WolframScript on Windows reads sources as ISO8859-1). *)

BeginPackage["MetricWarped`"];

H::usage = "H > 0, the author's constant.";
a4::usage = "a4[x4], the metric function of the 3-space and extra-time scale factors.";
b4::usage = "b4[x4] > 0, the metric function of the three extra-time components.";
x0::usage = "the author's coordinates x0 .. x7 (x0 is the hidden direction).";
x1::usage = x0::usage; x2::usage = x0::usage; x3::usage = x0::usage; x4::usage = x0::usage;
x5::usage = x0::usage; x6::usage = x0::usage; x7::usage = x0::usage;

MWCoordinates::usage = "MWCoordinates = {x0, x1, ..., x7}.";
MWAssumptions::usage = "MWAssumptions: H > 0, 0 < 6 H x0 < Pi/2, b4[x4] > 0, real derivatives.";
MWSimplify::usage = "MWSimplify[expr] simplifies under MWAssumptions (plus extra assumptions given as a second argument).";
MWCurvature::usage = "MWCurvature[diag, coords, assumptions] gives <|christoffel, riemannMixed, nonzeroMixed|> of the diagonal metric DiagonalMatrix[diag].";
MWLovelock::usage = "MWLovelock[k, curv, n, pairs, assumptions] gives the list of E_(k)^h_j for the index pairs {h, j} (Wolfram positions 1..n).";
MWLovelockScalar::usage = "MWLovelockScalar[k, curv, n, assumptions] gives E_(k)^(0) = Sum_h E_(k)^h_h / (n - 2 k).";

Begin["`Private`"];

Block[{$ContextPath = $ContextPath},
  Quiet[Get[FileNameJoin[{ParentDirectory[DirectoryName[$InputFileName], 2], "gkd_lovelock", "verification", "LovelockGKDCheck.wl"}]], General::shdw]];

MWCoordinates = {x0, x1, x2, x3, x4, x5, x6, x7};
MWAssumptions = H > 0 && 0 < 6 H x0 < Pi/2 && b4[x4] > 0 && Element[a4[x4], Reals] &&
  Element[Derivative[1][a4][x4], Reals] && Element[Derivative[1][b4][x4], Reals] &&
  Element[Derivative[2][a4][x4], Reals] && Element[Derivative[2][b4][x4], Reals];
MWSimplify[e_] := Simplify[e, MWAssumptions];
MWSimplify[e_, extra_] := Simplify[e, MWAssumptions && extra];

MWCurvature[diag_List, xs_List, extra_: True] := Module[{n = Length[xs], g, gi, chr, riem, mixed, nonzero, simp},
  simp = Simplify[#, MWAssumptions && extra] &;
  g = DiagonalMatrix[diag];
  gi = DiagonalMatrix[1/diag];
  chr = Table[simp[1/2 Sum[gi[[a, d]] (D[g[[d, c]], xs[[b]]] + D[g[[d, b]], xs[[c]]] - D[g[[b, c]], xs[[d]]]), {d, n}]],
    {a, n}, {b, n}, {c, n}];
  riem = Table[D[chr[[a, d, b]], xs[[c]]] - D[chr[[a, c, b]], xs[[d]]]
      + Sum[chr[[a, c, e]] chr[[e, d, b]] - chr[[a, d, e]] chr[[e, c, b]], {e, n}],
    {a, n}, {b, n}, {c, n}, {d, n}];
  mixed = Table[simp[Sum[gi[[b, e]] riem[[a, e, c, d]], {e, n}]], {a, n}, {b, n}, {c, n}, {d, n}];
  nonzero = Flatten[Table[If[mixed[[a, b, c, d]] =!= 0, {{{a, b, c, d}, mixed[[a, b, c, d]]}}, {}],
    {a, n}, {b, n}, {c, n}, {d, n}], 4];
  <|"christoffel" -> chr, "riemannMixed" -> mixed, "nonzeroMixed" -> nonzero|>
];

MWLovelock[k_Integer?Positive, curv_Association, n_Integer, pairs_List, extra_: True] := Module[
  {entries = curv["nonzeroMixed"], values},
  values = entries[[All, 2]];
  Table[
    With[{r = LovelockGKDCheck`LGKDLovelockPruned[k, entries, pr]},
      Simplify[-LovelockGKDCheck`LGKDCombine[r["terms"], values]/2^(k + 1), MWAssumptions && extra]],
    {pr, pairs}]
];

MWLovelockScalar[k_Integer?Positive, curv_Association, n_Integer, extra_: True] := Module[{diag},
  diag = MWLovelock[k, curv, n, Table[{h, h}, {h, n}], extra];
  Simplify[Total[diag]/(n - 2 k), MWAssumptions && extra]
];

End[];
EndPackage[];
