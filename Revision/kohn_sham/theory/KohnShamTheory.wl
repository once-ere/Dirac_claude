(* ::Package:: *)

(* KohnShamTheory.wl

   Revision Kohn-Sham theory for dirac16complex in the author's primordial field (Revision/SPEC.md,
   sections 1 and 7).  Revision code only: it loads nothing from the old stages.  Its only input is
   the Revision algebra fixture Revision/algebra/gammas.json (the author's T16, x1..x8 order).

   Coordinates as the author names them: x1, x2, x3 = 3-space; x4 = time; x5, x6, x7 = the three
   exponentially DEFLATING extra times (scale factor e^{-a4} sin^{1/6} z); x8 = the hidden direction,
   z = 6 H x8.  Arrays index x1..x8 as 1..8.  The proper hidden coordinate y = Log[Sin[z]]/(6H) <= 0
   replaces x8 (dy = Cot[z] dx8, Sin[z]^(1/3) = E^(2 H y)).

   Public symbols (prefix KS):
     KSLoadGammas[path]       -> {gamma (list of 8), eta}
     KSGeometryY[a4]          -> <|"coords","h","g","ginv"|> in the y chart, a4 = a4[x4]
     KSGeometryX8[a40]        -> the same in the author's x8 chart (a4 constant)
     KSChristoffel[g, coords]
     KSSpinConnection[gamma, eta, h, chr, coords] -> list of Omega_mu
     KSBlockBasis[gamma]      -> <|"labels","seeds","U"|>, V = U/(2 Sqrt[2])
     KSBlock[V, X]            -> list of the 8 diagonal 2x2 blocks of V^dagger X V
     KSPauli                  -> {s1, s2, s3}
*)

BeginPackage["KohnShamTheory`"];

KSLoadGammas::usage = "KSLoadGammas[path] reads the Revision fixture and returns {gamma, eta}.";
KSGeometryY::usage = "KSGeometryY[a4] metric data in the chart (x1..x7, y) with a4 an expression in x4.";
KSGeometryX8::usage = "KSGeometryX8[a40] metric data in the author's chart (x1..x8) with constant a4 = a40.";
KSChristoffel::usage = "KSChristoffel[g, coords] Christoffel symbols chr[[n, m, k]] = Gamma^n_{mk}.";
KSSpinConnection::usage = "KSSpinConnection[gamma, eta, h, chr, coords] canonical Omega_mu for the diagonal vielbein h.";
KSBlockBasis::usage = "KSBlockBasis[gamma] the joint eigenbasis of J, K1, K2 (unnormalised U = 2 Sqrt[2] V).";
KSBlock::usage = "KSBlock[V, X] the eight 2x2 diagonal blocks of ConjugateTranspose[V].X.V.";
KSPauli::usage = "KSPauli = {s1, s2, s3}.";
x1::usage = ""; x2::usage = ""; x3::usage = ""; x4::usage = ""; x5::usage = ""; x6::usage = "";
x7::usage = ""; x8::usage = ""; y::usage = ""; H::usage = "";

Begin["`Private`"];

KSPauli = {{{0, 1}, {1, 0}}, {{0, -I}, {I, 0}}, {{1, 0}, {0, -1}}};

KSLoadGammas[path_String] := Module[{j = Import[path, "RawJSON"]},
  {j["gamma"], DiagonalMatrix[j["eta"]]}];

KSGeometryY[a4_] := Module[{W = Exp[H y], h, eta},
  eta = {1, 1, 1, -1, -1, -1, -1, 1};
  h = {Exp[a4] W, Exp[a4] W, Exp[a4] W, 1, Exp[-a4] W, Exp[-a4] W, Exp[-a4] W, 1};
  <|"coords" -> {x1, x2, x3, x4, x5, x6, x7, y}, "h" -> h,
    "g" -> DiagonalMatrix[eta h^2], "ginv" -> DiagonalMatrix[1/(eta h^2)]|>];

KSGeometryX8[a40_] := Module[{z = 6 H x8, h, eta},
  eta = {1, 1, 1, -1, -1, -1, -1, 1};
  h = {Exp[a40] Sin[z]^(1/6), Exp[a40] Sin[z]^(1/6), Exp[a40] Sin[z]^(1/6), 1,
       Exp[-a40] Sin[z]^(1/6), Exp[-a40] Sin[z]^(1/6), Exp[-a40] Sin[z]^(1/6), Cot[z]};
  <|"coords" -> {x1, x2, x3, x4, x5, x6, x7, x8}, "h" -> h,
    "g" -> DiagonalMatrix[eta h^2], "ginv" -> DiagonalMatrix[1/(eta h^2)]|>];

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
  J = g[[8]].g[[1]].g[[4]]; K1 = g[[2]].g[[3]]; K2 = g[[5]].g[[6]];
  labels = Flatten[Table[{j, s2, s3}, {j, {1, -1}}, {s2, {1, -1}}, {s3, {1, -1}}], 2];
  Do[
    P = ((id + lab[[1]] J)/2) . ((id - I lab[[2]] K1)/2) . ((id - I lab[[3]] K2)/2);
    Pp = P . ((id + g[[8]])/2);
    c = SelectFirst[Range[16], Pp[[All, #]] =!= ConstantArray[0, 16] &];
    v = 8 Pp[[All, c]];
    AppendTo[seeds, c - 1];
    cols = Join[cols, {v, g[[8]].g[[1]].v}], {lab, labels}];
  <|"labels" -> labels, "seeds" -> seeds, "U" -> Transpose[cols]|>];

KSBlock[V_, X_] := Module[{Y = Simplify[ConjugateTranspose[V].X.V]},
  Table[Y[[2 b - 1 ;; 2 b, 2 b - 1 ;; 2 b]], {b, 8}]];

End[];
EndPackage[];
