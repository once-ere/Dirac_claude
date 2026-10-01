(* ::Package:: *)

(* LovelockGKDCheck.wl

   An independent Wolfram Language check of GKD (the pure-Rust generalized Kronecker delta of
   studies/lovelock_gkd/src/gkd.rs) and of the Lovelock tensors of Lovelock's equation (4.38)
   for the author's 8 x 8 test metric.  Context LovelockGKDCheck`.  Driven by
   scripts/verify_lovelock_gkd.wls, which writes artifacts/lovelock-gkd/wolfram-gkd-report.json.

   What is in here, for a student who has never seen it:

   1. The author's definition of the generalized Kronecker delta, re-typed verbatim:

        k\[Delta][lower_, upper_] /; Length[lower] == Length[upper] := Det[Outer[delta, lower, upper]]

      (k\[Delta] is how the symbol "k delta" is spelled in plain ASCII: it is the same
      symbol as k followed by the Greek letter delta, U+03B4).  delta is the ordinary
      Kronecker delta of two coordinate labels: delta[a, b] = 1 if a = b and 0 otherwise.
      For index lists lower = {l1, ..., lp} and upper = {u1, ..., up},
      Outer[delta, lower, upper] is the p x p matrix with entries delta[l_i, u_j], and its
      determinant is the generalized Kronecker delta delta^{u1 ... up}_{l1 ... lp}.
      This file never replaces it by a "faster" formula.

   2. The metric (exactly as the author gave it; coordinates x1..x8, labels 1..8 here):

        g = diag( E^(2 a4[x4]) Sin[6 H x8]^(1/3)   (x1, x2, x3),
                  -1                               (x4),
                  -E^(-2 a4[x4]) Sin[6 H x8]^(1/3) (x5, x6, x7),
                  Cot[6 H x8]^2                    (x8) )

      and its curvature, computed here from scratch with Mathematica's own D, Inverse and
      Simplify (no file of the Rust program is read for this):

        Christoffel  Gamma^a_{bc} = (1/2) g^{ad} (d_b g_dc + d_c g_db - d_d g_bc)
        Riemann      R^a_{bcd} = d_c Gamma^a_{db} - d_d Gamma^a_{cb}
                                 + Gamma^a_{ce} Gamma^e_{db} - Gamma^a_{de} Gamma^e_{cb}
        mixed        R^{ab}_{cd} = g^{be} R^a_{ecd},   Ricci R^a_b = R^{ac}_{bc},  R = R^a_a.

      (Misner-Thorne-Wheeler sign convention, the same as studies/lovelock_gkd/src/geometry.rs.)

   3. The Lovelock sums of (4.38), with the verbatim k\[Delta] as the weight:

        P_(k)^h_j = sum k\[Delta][{j, j1, ..., j2k}, {h, h1, ..., h2k}]
                        R^{j1 j2}_{h1 h2} ... R^{j(2k-1) j2k}_{h(2k-1) h2k}
        A_(k)^{lh} = sqrt(g) g^{jl} P_(k)^h_j     (n = 8, m = n/2 = 4, k = 1, 2, 3).

      A vanishing factor R gives a vanishing term, so the sum runs over the k-tuples of the
      NONZERO entries R^{ab}_{cd} (156 of the 4096).  Two ways are provided:

      * LGKDLovelockUnpruned: every k-tuple of nonzero entries, k\[Delta] called on each one
        (no shortcut at all); used for k = 1 and k = 2 (all 64 components) and, because it
        costs 156^3 = 3,796,416 calls of k\[Delta] per component, for selected k = 3 components.
      * LGKDLovelockPruned: the same sum, but an entry whose upper (lower) pair repeats an index
        already present in the lower (upper) row of k\[Delta] is skipped: the matrix
        Outer[delta, lower, upper] then has two equal rows (columns), so its determinant is 0
        and the term vanishes.  k\[Delta] (verbatim) is still called on every index list that
        is left.  Used for k = 3, all 64 components.

      Products of R entries commute, so the terms are collected by the SORTED tuple of entries
      with their integer k\[Delta] coefficients and multiplied out once per distinct tuple
      (LGKDCombine); this is exact algebra, not an approximation.

   4. LGKDFromMonomials rebuilds an expression from the exact monomial lists of
      artifacts/lovelock-gkd/lovelock-tensors.json:
        [[num, den, [e_H, e_a4', e_a4'', e_a4''', e_a4'''', e_E, e_S, e_C]], ...]
      with E = e^{a4[x4]}, S = Sin[6 H x8]^(1/3), C = Cot[6 H x8].

   Encoding: this file is pure ASCII on purpose (WolframScript on Windows reads source files as
   ISO8859-1, so a literal UTF-8 delta would become a different symbol); k\[Delta] is the
   standard ASCII spelling of the same symbol.

   License: GPL-3.0-or-later. *)

BeginPackage["LovelockGKDCheck`"];

k\[Delta]::usage = "k\[Delta][lower, upper] is the author's generalized Kronecker delta, re-typed verbatim: Det[Outer[delta, lower, upper]] for index lists of equal length (unevaluated otherwise).";
delta::usage = "delta[a, b] is the Kronecker delta of two integer coordinate labels (KroneckerDelta[a, b]); it stays unevaluated for anything that is not an integer.";
H::usage = "H is the constant of the test metric (Sin[6 H x8], Cot[6 H x8]).";
a4::usage = "a4 is the arbitrary function a4[x4] of the test metric.";
x1::usage = "x1 .. x8 are the coordinates of the test metric.";
x2::usage = x1::usage; x3::usage = x1::usage; x4::usage = x1::usage;
x5::usage = x1::usage; x6::usage = x1::usage; x7::usage = x1::usage; x8::usage = x1::usage;

LGKDCoordinates::usage = "LGKDCoordinates is {x1, x2, x3, x4, x5, x6, x7, x8}.";
LGKDMetric::usage = "LGKDMetric[] is the author's 8 x 8 test metric (diagonal).";
LGKDDomainAssumption::usage = "LGKDDomainAssumption is 0 < 6 H x8 < Pi/2, where sqrt(det g) = Cos[6 H x8] = Sin[6 H x8] Cot[6 H x8].";
LGKDCurvature::usage = "LGKDCurvature[] computes the inverse metric, sqrt(det g), the Christoffel symbols, the Riemann tensor R^a_bcd, the mixed Riemann tensor R^ab_cd, the mixed Ricci tensor, the Ricci scalar, the mixed Einstein tensor and the list of nonzero R^ab_cd, all simplified, and returns them in an Association.";
LGKDDefinitionText::usage = "LGKDDefinitionText[] is the definition of k\[Delta] held by the kernel, printed in InputForm with the Greek letter written as a Unicode character.";
LGKDLovelockUnpruned::usage = "LGKDLovelockUnpruned[k, nonzeroEntries, {h, j}] sums over every k-tuple of nonzero R^ab_cd entries, calling k\[Delta] on each; returns <|terms, kDeltaCalls, nonzeroCalls, nonIntegerCalls|>.";
LGKDLovelockPruned::usage = "LGKDLovelockPruned[k, nonzeroEntries, {h, j}] is the same sum with index lists that repeat an index in a row skipped (k\[Delta] = 0 there); k\[Delta] is called on every remaining list; returns <|terms, kDeltaCalls, nonzeroCalls, nonIntegerCalls|>.";
LGKDCombine::usage = "LGKDCombine[terms, values] multiplies out the collected terms {sortedTuple, coefficient}: Sum coefficient * Times @@ values[[sortedTuple]].";
LGKDFromMonomials::usage = "LGKDFromMonomials[list] rebuilds an expression from the exact monomial list [[num, den, [e_H, e_a4', e_a4'', e_a4''', e_a4'''', e_E, e_S, e_C]], ...] of lovelock-tensors.json.";

Begin["`Private`"];

(* ------------------------------------------------------------------------------------------ *)
(* 1. The author's definition, verbatim.                                                      *)
(* ------------------------------------------------------------------------------------------ *)

delta[a_Integer, b_Integer] := KroneckerDelta[a, b];

Clear[k\[Delta]]; k\[Delta][lower_, upper_] /; Length[lower] == Length[upper] := Det[Outer[delta, lower, upper]]

LGKDDefinitionText[] := Block[
  {$ContextPath = {"LovelockGKDCheck`Private`", "LovelockGKDCheck`", "System`"}, $Context = "LovelockGKDCheck`Private`"},
  StringReplace[ToString[Definition[k\[Delta]], InputForm], "\\[Delta]" -> FromCharacterCode[948]]
];

(* ------------------------------------------------------------------------------------------ *)
(* 2. The metric and its curvature.                                                           *)
(* ------------------------------------------------------------------------------------------ *)

LGKDCoordinates = {x1, x2, x3, x4, x5, x6, x7, x8};
LGKDDomainAssumption = 0 < 6 H x8 < Pi/2;

LGKDMetric[] := DiagonalMatrix[{
  E^(2 a4[x4]) Sin[6 H x8]^(1/3), E^(2 a4[x4]) Sin[6 H x8]^(1/3), E^(2 a4[x4]) Sin[6 H x8]^(1/3),
  -1,
  -E^(-2 a4[x4]) Sin[6 H x8]^(1/3), -E^(-2 a4[x4]) Sin[6 H x8]^(1/3), -E^(-2 a4[x4]) Sin[6 H x8]^(1/3),
  Cot[6 H x8]^2}];

LGKDCurvature[] := Module[{n = 8, xs = LGKDCoordinates, g, gi, sqrtg, chr, riem, mixed, ricci, scalar, einstein, nonzero},
  g = LGKDMetric[];
  gi = Simplify[Inverse[g]];
  sqrtg = Simplify[Sqrt[Det[g]], LGKDDomainAssumption];
  (* Gamma^a_{bc} = 1/2 g^{ad} (d_b g_dc + d_c g_db - d_d g_bc) *)
  chr = Table[Simplify[1/2 Sum[gi[[a, d]] (D[g[[d, c]], xs[[b]]] + D[g[[d, b]], xs[[c]]] - D[g[[b, c]], xs[[d]]]), {d, n}]],
    {a, n}, {b, n}, {c, n}];
  (* R^a_{bcd} = d_c Gamma^a_{db} - d_d Gamma^a_{cb} + Gamma^a_{ce} Gamma^e_{db} - Gamma^a_{de} Gamma^e_{cb} *)
  riem = Table[Simplify[D[chr[[a, d, b]], xs[[c]]] - D[chr[[a, c, b]], xs[[d]]]
      + Sum[chr[[a, c, e]] chr[[e, d, b]] - chr[[a, d, e]] chr[[e, c, b]], {e, n}]],
    {a, n}, {b, n}, {c, n}, {d, n}];
  (* R^{ab}_{cd} = g^{be} R^a_{ecd} *)
  mixed = Table[Simplify[Sum[gi[[b, e]] riem[[a, e, c, d]], {e, n}]], {a, n}, {b, n}, {c, n}, {d, n}];
  ricci = Table[Simplify[Sum[mixed[[a, c, b, c]], {c, n}]], {a, n}, {b, n}];
  scalar = Simplify[Sum[ricci[[a, a]], {a, n}]];
  einstein = Table[Simplify[ricci[[a, b]] - 1/2 KroneckerDelta[a, b] scalar], {a, n}, {b, n}];
  (* the nonzero R^{ab}_{cd}, in lexicographic order of (a, b, c, d) *)
  nonzero = Flatten[Table[If[mixed[[a, b, c, d]] =!= 0, {{{a, b, c, d}, mixed[[a, b, c, d]]}}, {}],
    {a, n}, {b, n}, {c, n}, {d, n}], 4];
  <|"metric" -> g, "inverseMetric" -> gi, "sqrtDetG" -> sqrtg, "christoffel" -> chr, "riemann" -> riem,
    "riemannMixed" -> mixed, "ricciMixed" -> ricci, "ricciScalar" -> scalar, "einsteinMixed" -> einstein,
    "nonzeroMixed" -> nonzero|>
];

(* ------------------------------------------------------------------------------------------ *)
(* 3. The Lovelock sums with the verbatim k\[Delta].                                          *)
(*    entries = {{{a, b, c, d}, R^{ab}_{cd}}, ...}; a, b (the upper pair of R) join the lower  *)
(*    row of k\[Delta] (they are contracted with the lower indices j1 j2 ...), c, d join the   *)
(*    upper row.                                                                              *)
(* ------------------------------------------------------------------------------------------ *)

LGKDLovelockUnpruned[k_Integer?Positive, entries_List, {h_Integer, j_Integer}] := Module[
  {idx = entries[[All, 1]], low, up, calls = 0, nonzeroCalls = 0, nonInteger = 0, sown},
  low = idx[[All, {1, 2}]];
  up = idx[[All, {3, 4}]];
  sown = Reap[
    Do[
      calls++;
      With[{s = k\[Delta][Join[{j}, Flatten[low[[t]]]], Join[{h}, Flatten[up[[t]]]]]},
        If[! IntegerQ[s], nonInteger++];
        If[s =!= 0, nonzeroCalls++; Sow[{Sort[t], s}]]
      ],
      {t, Tuples[Range[Length[idx]], k]}
    ]
  ][[2]];
  <|"terms" -> If[sown === {}, {}, First[sown]], "kDeltaCalls" -> calls, "nonzeroCalls" -> nonzeroCalls,
    "nonIntegerCalls" -> nonInteger|>
];

LGKDLovelockPruned[k_Integer?Positive, entries_List, {h_Integer, j_Integer}] := Module[
  {idx = entries[[All, 1]], low, up, lowMask, upMask, range, calls = 0, nonzeroCalls = 0, nonInteger = 0, rec, sown},
  low = idx[[All, {1, 2}]];
  up = idx[[All, {3, 4}]];
  (* bit masks of the labels 1..8 in each pair *)
  lowMask = BitOr[2^(low[[All, 1]] - 1), 2^(low[[All, 2]] - 1)];
  upMask = BitOr[2^(up[[All, 1]] - 1), 2^(up[[All, 2]] - 1)];
  range = Range[Length[idx]];
  rec[depth_, lm_, um_, chosen_] := If[depth == k,
    calls++;
    With[{s = k\[Delta][Join[{j}, Flatten[low[[chosen]]]], Join[{h}, Flatten[up[[chosen]]]]]},
      If[! IntegerQ[s], nonInteger++];
      If[s =!= 0, nonzeroCalls++; Sow[{Sort[chosen], s}]]
    ],
    (* skip an entry that repeats a label already in the lower or the upper row *)
    Scan[rec[depth + 1, BitOr[lm, lowMask[[#]]], BitOr[um, upMask[[#]]], Append[chosen, #]] &,
      Pick[range, BitAnd[lowMask, lm] + BitAnd[upMask, um], 0]]
  ];
  sown = Reap[rec[0, 2^(j - 1), 2^(h - 1), {}]][[2]];
  <|"terms" -> If[sown === {}, {}, First[sown]], "kDeltaCalls" -> calls, "nonzeroCalls" -> nonzeroCalls,
    "nonIntegerCalls" -> nonInteger|>
];

LGKDCombine[terms_List, values_List] := Module[{grouped},
  If[terms === {}, Return[0, Module]];
  grouped = Select[GroupBy[terms, First -> Last, Total], # =!= 0 &];
  Total[KeyValueMap[#2 (Times @@ values[[#1]]) &, grouped]]
];

(* ------------------------------------------------------------------------------------------ *)
(* 4. Rebuild an expression from the exact monomials of lovelock-tensors.json.                *)
(* ------------------------------------------------------------------------------------------ *)

LGKDFromMonomials[monomials_List] := Total[Map[
  Function[term, Module[{c = term[[1]]/term[[2]], e = term[[3]]},
    c H^e[[1]] Derivative[1][a4][x4]^e[[2]] Derivative[2][a4][x4]^e[[3]] Derivative[3][a4][x4]^e[[4]]
      Derivative[4][a4][x4]^e[[5]] E^(e[[6]] a4[x4]) Sin[6 H x8]^(e[[7]]/3) Cot[6 H x8]^e[[8]]
  ]],
  monomials]];

End[];

EndPackage[];
