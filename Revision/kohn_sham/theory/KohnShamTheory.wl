(* ::Package:: *)

(* KohnShamTheory.wl

   Revision Kohn-Sham theory for dirac16complex in the author's primordial field (Revision/SPEC.md,
   sections 1 and 7).  Revision code only: it loads nothing from the old stages.  Its only input is
   the Revision algebra fixture Revision/algebra/gammas.json (the author's T16 in the author's order x0..x7,
   gamma^(xk) = T16[k]).

   The author's coordinates {x0, x1, ..., x7}: x0 = the hidden direction (space-like), z = 6 H x0 real; x1, x2, x3 =
   3-space; x4 = time; x5, x6, x7 = the three extra times.  The metric is the corrected primordial metric of 2026-10-16
   (version 2; Revision/SPEC.md section 1, Revision/metric_warped/):
     g = diag(E^(-2 a4) b4 Cot[z]^2, E^(2 a4) (x3), -1, -E^(-2 a4) b4 (Sin[z]^2)^(1/6) (x3)),
   for general a4(x4), b4(x4) > 0 and every real z with Sin z Cos z != 0 ((Sin^2)^(1/6) the positive branch).
   Arrays index x0..x7 as 1..8 (xk at position k+1).  The hidden coordinate y = Log[|Sin[z]|]/(6H) <= 0 replaces x0 at
   position 1 on every quarter of the period of z (dy = Cot[z] dx0, (Sin[z]^2)^(1/6) = E^(2 H y)); with
   f = E^(-a4) b4^(1/2) the line element is E^(2 a4) dx_i^2 - dx4^2 + f^2 (dy^2 - E^(2 H y) dx_t^2).
   (Until 2026-10-16 the package used the metric of 2026-10-14, now withdrawn.)

   Public symbols (prefix KS):
     KSLoadGammas[path]       -> {gamma (list of 8), eta}
     KSGeometryY[a4, b4]      -> <|"coords","h","g","ginv"|> in the y chart (y, x1..x7), a4 = a4[x4], b4 = b4[x4]
     KSGeometryX0[a4, b4]     -> the same in the author's chart (x0..x7)
     KSChristoffel[g, coords]
     KSSpinConnection[gamma, eta, h, chr, coords] -> list of Omega_mu
     KSBlockBasis[gamma]      -> <|"labels","seeds","U"|>, V = U/(2 Sqrt[2])
     KSBlock[V, X]            -> list of the 8 diagonal 2x2 blocks of V^dagger X V
     KSPauli                  -> {s1, s2, s3}
*)

BeginPackage["KohnShamTheory`"];

KSLoadGammas::usage = "KSLoadGammas[path] reads the Revision fixture and returns {gamma, eta}.";
KSGeometryY::usage = "KSGeometryY[a4, b4] metric data in the chart (y, x1..x7) with a4, b4 expressions in x4.";
KSGeometryX0::usage = "KSGeometryX0[a4, b4] metric data in the author's chart (x0..x7) with a4, b4 expressions in x4.";
KSZeroX0Q::usage = "KSZeroX0Q[e] exact zero test for every real z = 6 H x0 with Sin z Cos z != 0 (reduction modulo Cos^2 + Sin^2 - 1, ww^12 - Sin^2, Sign[Cot]^2 - 1).";
KSChristoffel::usage = "KSChristoffel[g, coords] Christoffel symbols chr[[n, m, k]] = Gamma^n_{mk}.";
KSSpinConnection::usage = "KSSpinConnection[gamma, eta, h, chr, coords] canonical Omega_mu for the diagonal vielbein h.";
KSBlockBasis::usage = "KSBlockBasis[gamma] the joint eigenbasis of J, K1, K2 (unnormalised U = 2 Sqrt[2] V).";
KSBlock::usage = "KSBlock[V, X] the eight 2x2 diagonal blocks of ConjugateTranspose[V].X.V.";
KSPauli::usage = "KSPauli = {s1, s2, s3}.";
x0::usage = ""; x1::usage = ""; x2::usage = ""; x3::usage = ""; x4::usage = ""; x5::usage = "";
x6::usage = ""; x7::usage = ""; y::usage = ""; H::usage = "";

Begin["`Private`"];

KSPauli = {{{0, 1}, {1, 0}}, {{0, -I}, {I, 0}}, {{1, 0}, {0, -1}}};

KSLoadGammas[path_String] := Module[{j = Import[path, "RawJSON"]},
  {j["gamma"], DiagonalMatrix[j["eta"]]}];

KSGeometryY[a4_, b4_] := Module[{W = Exp[H y], f = Exp[-a4] Sqrt[b4], h, eta},
  eta = {1, 1, 1, 1, -1, -1, -1, -1};
  h = {f, Exp[a4], Exp[a4], Exp[a4], 1, f W, f W, f W};
  <|"coords" -> {y, x1, x2, x3, x4, x5, x6, x7}, "h" -> h,
    "g" -> DiagonalMatrix[eta h^2], "ginv" -> DiagonalMatrix[1/(eta h^2)]|>];

(* the author's chart: e^x0 = E^(-a4) b4^(1/2) Cot[z] (signed), e^xt = E^(-a4) b4^(1/2) (Sin[z]^2)^(1/12) *)
KSGeometryX0[a4_, b4_] := Module[{z = 6 H x0, f = Exp[-a4] Sqrt[b4], h, eta},
  eta = {1, 1, 1, 1, -1, -1, -1, -1};
  h = {f Cot[z], Exp[a4], Exp[a4], Exp[a4], 1, f (Sin[z]^2)^(1/12), f (Sin[z]^2)^(1/12), f (Sin[z]^2)^(1/12)};
  <|"coords" -> {x0, x1, x2, x3, x4, x5, x6, x7}, "h" -> h,
    "g" -> DiagonalMatrix[eta h^2], "ginv" -> DiagonalMatrix[1/(eta h^2)]|>];

(* exact zero test for every real z = 6 H x0 with Sin z Cos z != 0 (the author's chart): Sin -> sv, Cos -> cv (signed),
   (Sin^2)^k -> ww^(12 k), |Sin|^k -> ww^(6 k), |Cot| -> sgn cv/sv, Sign[Cot] -> sgn; numerator reduced modulo the
   Groebner basis {cv^2 + sv^2 - 1, ww^12 - sv^2, sgn^2 - 1} *)
KSTrigRules = {
   Power[Power[Sin[6 H x0], 2], k_] :> ksww^(12 k), Power[Abs[Sin[6 H x0]], k_] :> ksww^(6 k), Abs[Sin[6 H x0]] -> ksww^6,
   Power[Abs[Cot[6 H x0]], k_] :> (kssgn kscv/kssv)^k, Abs[Cot[6 H x0]] -> kssgn kscv/kssv, Sign[Cot[6 H x0]] -> kssgn,
   Sin[12 H x0] -> 2 kssv kscv, Cos[12 H x0] -> kscv^2 - kssv^2,
   Sin[6 H x0] -> kssv, Cos[6 H x0] -> kscv, Cot[6 H x0] -> kscv/kssv, Tan[6 H x0] -> kssv/kscv,
   Csc[6 H x0] -> 1/kssv, Sec[6 H x0] -> 1/kscv};
KSZeroX0Q[e_] := Module[{r = Together[e /. KSTrigRules]},
  If[Cases[r, (Sin | Cos | Tan | Cot | Csc | Sec | Abs | Sign)[arg_] /; ! FreeQ[arg, x0], {0, Infinity}] =!= {},
   Print["ERROR  KSZeroX0Q cannot map ", InputForm[e]]; Exit[1]];
  r === 0 || Last[PolynomialReduce[Expand[Numerator[r]], {kscv^2 + kssv^2 - 1, ksww^12 - kssv^2, kssgn^2 - 1},
     {kscv, ksww, kssgn, kssv}]] === 0];

KSChristoffel[g_, coords_] := Module[{gi = Inverse[g]},
  Table[Simplify[(1/2) Sum[gi[[n, l]] (D[g[[l, m]], coords[[k]]] + D[g[[l, k]], coords[[m]]] -
       D[g[[m, k]], coords[[l]]]), {l, 8}]], {n, 8}, {m, 8}, {k, 8}]];

KSSpinConnection[gamma_, eta_, h_, chr_, coords_] := Module[{S, w},
  S = Table[(gamma[[a]].gamma[[b]] - gamma[[b]].gamma[[a]])/4, {a, 8}, {b, 8}];
  Table[
    Simplify[ConstantArray[0, {16, 16}] + Sum[
      w = Simplify[If[A == B, h[[A]] D[1/h[[B]], coords[[mu]]], 0] + h[[A]] chr[[A, mu, B]]/h[[B]]];
      If[w === 0, 0, (1/2) eta[[A, A]] w S[[A, B]]], {A, 8}, {B, 8}]],
    {mu, 8}]];

KSBlockBasis[gamma_] := Module[{g = gamma, id = IdentityMatrix[16], J, K1, K2, labels, cols = {}, seeds = {},
    P, Pp, c, v},
  (* g[[k + 1]] = gamma^(xk): J = gamma^(x0) gamma^(x1) gamma^(x4), K1 = gamma^(x2) gamma^(x3), K2 = gamma^(x5) gamma^(x6) *)
  J = g[[1]].g[[2]].g[[5]]; K1 = g[[3]].g[[4]]; K2 = g[[6]].g[[7]];
  labels = Flatten[Table[{j, s2, s3}, {j, {1, -1}}, {s2, {1, -1}}, {s3, {1, -1}}], 2];
  Do[
    P = ((id + lab[[1]] J)/2) . ((id - I lab[[2]] K1)/2) . ((id - I lab[[3]] K2)/2);
    Pp = P . ((id + g[[1]])/2);
    c = SelectFirst[Range[16], Pp[[All, #]] =!= ConstantArray[0, 16] &];
    v = 8 Pp[[All, c]];
    AppendTo[seeds, c - 1];
    cols = Join[cols, {v, g[[1]].g[[2]].v}], {lab, labels}];
  <|"labels" -> labels, "seeds" -> seeds, "U" -> Transpose[cols]|>];

KSBlock[V_, X_] := Module[{Y = Simplify[ConjugateTranspose[V].X.V]},
  Table[Y[[2 b - 1 ;; 2 b, 2 b - 1 ;; 2 b]], {b, 8}]];

End[];
EndPackage[];
