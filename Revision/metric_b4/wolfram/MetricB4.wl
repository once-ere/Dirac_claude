(* ::Package:: *)

(* MetricB4.wl

   The primordial metric of the user's order of 2026-10-14 (from the author's notebook
   Dirac_Einstein-Lovelock_4+4_Nash.nb, input cell In[97] and stored output Out[101]) and everything
   that follows from it exactly: inverse metric, sqrt|det g|, Christoffel symbols, Riemann tensor,
   Ricci tensor, Ricci scalar, Einstein tensor, the Lovelock tensors k = 1, 2, 3 and the vacuum
   Einstein-Lovelock equations.  Context MetricB4`.  Driven by verify_metric_b4.wls.

   The metric in the author's coordinates x0, x1, ..., x7 (his order, as in the notebook: x0 the hidden
   direction, listed first; x1, x2, x3 space; x4 time; x5, x6, x7 the exponentially deflating extra times):

     g = diag( Cot[6 H x0]^2                              (x0),
               E^(2 a4[x4]) Sin[6 H x0]^(1/3)             (x1, x2, x3),
               -1                                         (x4),
               -E^(-2 a4[x4]) b4[x4] Sin[6 H x0]^(1/3)    (x5, x6, x7) )

   (Until 2026-10-14 this package used the withdrawn labels x1..x8 with the hidden direction x8 listed last.)

   The only difference from the metric of Revision/SPEC.md section 1 before 2026-10-14 is the new
   metric function b4[x4] in the three extra-time components; b4 = 1 gives the earlier metric.

   Conventions (the same as Revision/gkd_lovelock/verification/LovelockGKDCheck.wl, so that b4 = 1 can
   be compared entry by entry):
     Christoffel  Gamma^a_{bc} = (1/2) g^{ad} (d_b g_dc + d_c g_db - d_d g_bc)
     Riemann      R^a_{bcd} = d_c Gamma^a_{db} - d_d Gamma^a_{cb} + Gamma^a_{ce} Gamma^e_{db} - Gamma^a_{de} Gamma^e_{cb}
     mixed        R^{ab}_{cd} = g^{be} R^a_{ecd},  Ricci R^a_b = R^{ac}_{bc},  R = R^a_a,  G^a_b = R^a_b - R delta^a_b / 2
     Lovelock     P_(k)^h_j = kdelta[{j, j1..j2k}, {h, h1..h2k}] R^{j1 j2}_{h1 h2} ... (the author's
                  generalized Kronecker delta, verbatim, from LovelockGKDCheck.wl), E_(k) = -P_(k)/2^(k+1),
                  E_(1) = G.
   Arrays M of mixed tensors are stored with the UPPER index first: M[[h, j]] = T^h_j.
   The domain: 0 < 6 H x0 < Pi/2, H > 0, b4[x4] > 0 (the extra-time components are time-like only for b4 > 0).

   License: GPL-3.0-or-later.  Pure ASCII on purpose (WolframScript on Windows reads sources as ISO8859-1). *)

BeginPackage["MetricB4`"];

H::usage = "H > 0, the author's constant.";
a4::usage = "a4[x4], the metric function of the 3-space and extra-time scale factors.";
b4::usage = "b4[x4] > 0, the metric function of the three extra-time components (new on 2026-10-14).";
x0::usage = "the author's coordinates x0 .. x7 (his order; x0 is the hidden direction).";
x1::usage = x0::usage; x2::usage = x0::usage; x3::usage = x0::usage; x4::usage = x0::usage;
x5::usage = x0::usage; x6::usage = x0::usage; x7::usage = x0::usage;
w1::usage = "Lovelock weight of k = 1."; w2::usage = "Lovelock weight of k = 2."; w3::usage = "Lovelock weight of k = 3.";
Lambda::usage = "the cosmological constant of the author's vacuum equations (the author's Greek capital Lambda).";

MB4Coordinates::usage = "MB4Coordinates = {x0, x1, ..., x7} (the author's order).";
MB4Metric::usage = "MB4Metric[] is the 8 x 8 diagonal metric with b4.";
MB4Assumptions::usage = "MB4Assumptions: H > 0, 0 < 6 H x0 < Pi/2, b4[x4] > 0, a4[x4] real.";
MB4Curvature::usage = "MB4Curvature[] gives an Association of the metric, inverse, sqrt|det g|, Christoffel, Riemann, mixed Riemann, mixed Ricci, Ricci scalar, mixed Einstein and the nonzero mixed Riemann entries.";
MB4Lovelock::usage = "MB4Lovelock[k, curvature] gives the mixed array E_(k)^h_j = -P_(k)^h_j / 2^(k+1) (upper index first) and the k-delta call counts.";
MB4Simplify::usage = "MB4Simplify[expr] simplifies under MB4Assumptions.";
MB4AuthorToRevision::usage = "MB4AuthorToRevision[array] maps an author array A[[a, b]] = T_a^b (lower index first) to the Revision array M[[h, j]] = T^h_j (upper index first); both are in the author's order x0, ..., x7, so M = Transpose[A].";

Begin["`Private`"];

(* the author's k-delta and the pruned Lovelock sum, verbatim, from the GKD record (only its metric-independent
   functions LGKDLovelockPruned and LGKDCombine are used; they are called with full context names) *)
Block[{$ContextPath = $ContextPath},
  Quiet[Get[FileNameJoin[{ParentDirectory[DirectoryName[$InputFileName], 2], "gkd_lovelock", "verification", "LovelockGKDCheck.wl"}]], General::shdw]];

MB4Coordinates = {x0, x1, x2, x3, x4, x5, x6, x7};
MB4Assumptions = H > 0 && 0 < 6 H x0 < Pi/2 && b4[x4] > 0 && Element[a4[x4], Reals] &&
  Element[Derivative[1][a4][x4], Reals] && Element[Derivative[1][b4][x4], Reals] &&
  Element[Derivative[2][a4][x4], Reals] && Element[Derivative[2][b4][x4], Reals];
MB4Simplify[e_] := Simplify[e, MB4Assumptions];

MB4Metric[] := DiagonalMatrix[{
  Cot[6 H x0]^2,
  E^(2 a4[x4]) Sin[6 H x0]^(1/3), E^(2 a4[x4]) Sin[6 H x0]^(1/3), E^(2 a4[x4]) Sin[6 H x0]^(1/3),
  -1,
  -E^(-2 a4[x4]) b4[x4] Sin[6 H x0]^(1/3), -E^(-2 a4[x4]) b4[x4] Sin[6 H x0]^(1/3), -E^(-2 a4[x4]) b4[x4] Sin[6 H x0]^(1/3)}];

MB4Curvature[] := Module[{n = 8, xs = MB4Coordinates, g, gi, sqrtg, chr, riem, mixed, ricci, scalar, einstein, nonzero},
  g = MB4Metric[];
  gi = MB4Simplify[Inverse[g]];
  sqrtg = MB4Simplify[Sqrt[Abs[Det[g]]]];
  chr = Table[MB4Simplify[1/2 Sum[gi[[a, d]] (D[g[[d, c]], xs[[b]]] + D[g[[d, b]], xs[[c]]] - D[g[[b, c]], xs[[d]]]), {d, n}]],
    {a, n}, {b, n}, {c, n}];
  riem = Table[MB4Simplify[D[chr[[a, d, b]], xs[[c]]] - D[chr[[a, c, b]], xs[[d]]]
      + Sum[chr[[a, c, e]] chr[[e, d, b]] - chr[[a, d, e]] chr[[e, c, b]], {e, n}]],
    {a, n}, {b, n}, {c, n}, {d, n}];
  mixed = Table[MB4Simplify[Sum[gi[[b, e]] riem[[a, e, c, d]], {e, n}]], {a, n}, {b, n}, {c, n}, {d, n}];
  ricci = Table[MB4Simplify[Sum[mixed[[a, c, b, c]], {c, n}]], {a, n}, {b, n}];
  scalar = MB4Simplify[Sum[ricci[[a, a]], {a, n}]];
  einstein = Table[MB4Simplify[ricci[[a, b]] - 1/2 KroneckerDelta[a, b] scalar], {a, n}, {b, n}];
  nonzero = Flatten[Table[If[mixed[[a, b, c, d]] =!= 0, {{{a, b, c, d}, mixed[[a, b, c, d]]}}, {}],
    {a, n}, {b, n}, {c, n}, {d, n}], 4];
  <|"metric" -> g, "inverseMetric" -> gi, "sqrtAbsDetG" -> sqrtg, "christoffel" -> chr, "riemann" -> riem,
    "riemannMixed" -> mixed, "ricciMixed" -> ricci, "ricciScalar" -> scalar, "einsteinMixed" -> einstein,
    "nonzeroMixed" -> nonzero|>
];

(* E_(k)^h_j for all 64 (h, j); the pruned k-delta sum of LovelockGKDCheck (exact; k-delta called verbatim
   on every index list whose rows have no repeated label) *)
MB4Lovelock[k_Integer?Positive, curv_Association] := Module[{entries = curv["nonzeroMixed"], values, calls = 0, arr},
  values = entries[[All, 2]];
  arr = Table[
    With[{r = LovelockGKDCheck`LGKDLovelockPruned[k, entries, {h, j}]},
      calls += r["kDeltaCalls"];
      MB4Simplify[-LovelockGKDCheck`LGKDCombine[r["terms"], values]/2^(k + 1)]],
    {h, 8}, {j, 8}];
  <|"E" -> arr, "kDeltaCalls" -> calls|>
];

(* the author's array A[[p, q]] = T_{a(p)}^{a(q)} (lower index first) and the Revision array M[[h, j]] = T^h_j
   (upper index first) are both in the author's order x0..x7 (Wolfram position p = a + 1): M[[q, p]] = A[[p, q]] *)
MB4AuthorToRevision[A_] := Module[{M = ConstantArray[0, {8, 8}]},
  Do[M[[q, p]] = A[[p, q]], {p, 8}, {q, 8}];
  M
];

End[];
EndPackage[];
