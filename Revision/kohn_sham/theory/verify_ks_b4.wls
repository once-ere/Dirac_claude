#!/usr/bin/env wolframscript
(* ::Package:: *)

(* verify_ks_b4.wls

   The Kohn-Sham record (Revision/kohn_sham, ks-theory.json) in the user's metric of 2026-10-14 with b4[x4] in the
   extra-time components.  Question: which Kohn-Sham quantities change with b4?

   Exact statements checked here (with the vielbein of the metric with b4 and the package
   Revision/theory/wolfram/RevisionFieldTheory.wl; commuting components, the Dirac operator is linear and the same
   for both statistics):
     K1  for every 16-component X(x0..x7):  D_b4[ b4^(-3/4) X ] = b4^(-3/4) ( D_1[X] + (b4^(-1/2) - 1) E^a4 Sin[z]^(-1/6)
         sum_(t = x5, x6, x7) gamma^(t) d_t X ),  where D_b4 = gamma^mu D_mu in the metric with b4 and D_1 the operator of
         the metric before 2026-10-14 (b4 = 1).  So b4 enters the field equation only through the factor b4^(-3/4) and
         through the extra-time derivatives (scaled by b4^(-1/2)).
     K2  the good sector of ks-theory.json (no dependence on x5, x6, x7: extra-time momenta zero): for X independent of
         x5..x7, D_b4[b4^(-3/4) X] = b4^(-3/4) D_1[X] exactly, so the ansatz Psi = e^{i k.x} W^{-3} b4^{-3/4} chi(y, x4)
         gives the SAME chi-equation as at b4 = 1: every level, orbital and slice of the Kohn-Sham record is independent of
         b4 (the slice Hamiltonian h(a4,0) does not contain b4).
     K3  normalisation: sqrt|det g| = b4^(3/2) Cos z, so int sqrt|g| |b4^(-3/4) X|^2 = int Cos z |X|^2: the factor
         b4^(-3/4) keeps the norm; the proper extra-time volume is v_t e^{-3 a4} b4^{3/2} (times the warp), so the
         rescaling identity of ks-theory.json becomes KS(a4,0, b4,0; Delta k, v_t) = KS(0, 1; Delta k e^{-a4,0},
         v_t e^{-3 a4,0} b4,0^{3/2}) (levels and orbitals unchanged; proper densities per proper 7-volume).
     K4  on the background of the record (b4 = 1, the vacuum history of Revision/metric_b4) nothing changes.
   Writes Revision/kohn_sham/reports/ks-b4-wolfram.json; exit 0 iff all pass.
   Usage (repository root): wolframscript -file Revision/kohn_sham/theory/verify_ks_b4.wls *)

$here = DirectoryName[$InputFileName];
$revDir = ExpandFileName[FileNameJoin[{$here, "..", ".."}]];
If[Get[FileNameJoin[{$revDir, "theory", "wolfram", "RevisionFieldTheory.wl"}]] === $Failed, Print["ERROR  RevisionFieldTheory.wl: Get failed"]; Exit[1]];
rftLoadFixture[FileNameJoin[{$revDir, "algebra", "gammas.json"}]];
t0 = AbsoluteTime[];
checks = {};
addCheck[name_String, ok_, detail_String] := (AppendTo[checks, <|"name" -> name, "verdict" -> If[TrueQ[ok], "PASS", "FAIL"], "detail" -> detail|>];
  Print[If[TrueQ[ok], "PASS  ", "FAIL  "], name]);
g = rftGam; X = rftX;
build[fl_] := Module[{e0 = DiagonalMatrix[fl], ei = DiagonalMatrix[1/fl], g0, gi, Gm, om, oml, Om, gup},
  g0 = Transpose[e0] . rftEta . e0; gi = Inverse[g0];
  Gm = rftChristoffel[g0, gi]; om = rftOmegaMixed[e0, ei, Gm]; oml = rftLower[om];
  Om = rftSpinorConnection[oml]; gup = rftGammaUp[ei];
  <|"sqrtg" -> Times @@ Abs[fl] /. Abs[e_] :> e, "gup" -> gup, "Om" -> Om|>];
(* the vielbein diagonal in the author's order x0, x1, ..., x7 *)
fB = {Cot[rftZ], E^a4[x4] Sin[rftZ]^(1/6), E^a4[x4] Sin[rftZ]^(1/6), E^a4[x4] Sin[rftZ]^(1/6), 1,
   E^(-a4[x4]) Sqrt[b4[x4]] Sin[rftZ]^(1/6), E^(-a4[x4]) Sqrt[b4[x4]] Sin[rftZ]^(1/6), E^(-a4[x4]) Sqrt[b4[x4]] Sin[rftZ]^(1/6)};
f1 = fB /. b4 -> (1 &);
geoB = build[fB]; geo1 = build[f1];
Xf = Table[ph[A] @@ X, {A, 16}];
lhs = rftDirac["C", geoB, b4[x4]^(-3/4) Xf];
extra = Sum[g[[t]] . D[Xf, X[[t]]], {t, 6, 8}];  (* t = x5, x6, x7 at positions 6, 7, 8 *)
rhs = b4[x4]^(-3/4) (rftDirac["C", geo1, Xf] + (b4[x4]^(-1/2) - 1) E^a4[x4] Sin[rftZ]^(-1/6) extra);
addCheck["K1_dirac_operator_b4_factorisation", rftZeroQ[lhs - rhs],
  "for every 16-component X(x0..x7): gamma^mu D_mu (b4^(-3/4) X) [metric with b4] = b4^(-3/4) (gamma^mu D_mu X [b4 = 1] + (b4^(-1/2) - 1) E^a4 Sin[z]^(-1/6) sum_(t = x5, x6, x7) gamma^(t) d_t X)"];
lhsG = Module[{P = Table[ph[A][x0, x1, x2, x3, x4], {A, 16}]},
   Fold[Plus, Table[geoB["gup"][[mu]] . (D[b4[x4]^(-3/4) P, X[[mu]]] + geoB["Om"][[mu]] . (b4[x4]^(-3/4) P)), {mu, 8}]]];
rhsG = b4[x4]^(-3/4) Module[{P = Table[ph[A][x0, x1, x2, x3, x4], {A, 16}]},
   Fold[Plus, Table[geo1["gup"][[mu]] . (D[P, X[[mu]]] + geo1["Om"][[mu]] . P), {mu, 8}]]];
addCheck["K2_good_sector_independent_of_b4",
  And @@ (Simplify[PowerExpand[#], {H > 0, 0 < 6 H x0 < Pi/2, b4[x4] > 0}] === 0 & /@ (lhsG - rhsG)),
  "for X independent of x5, x6, x7 (the good sector of ks-theory.json): gamma^mu D_mu (b4^(-3/4) X) = b4^(-3/4) gamma^mu D_mu X [b4 = 1] exactly; the chi-equation, the slice Hamiltonian h(a4,0), every level and orbital of the Kohn-Sham record are independent of b4"];
addCheck["K3_norm_and_volume",
  Simplify[(geoB["sqrtg"] (b4[x4]^(-3/4))^2) - (geo1["sqrtg"]), {H > 0, 0 < 6 H x0 < Pi/2, b4[x4] > 0}] === 0 &&
   Simplify[geoB["sqrtg"] - b4[x4]^(3/2) Cos[rftZ], {H > 0, 0 < 6 H x0 < Pi/2, b4[x4] > 0}] === 0,
  "sqrt|det g| = b4^(3/2) Cos z and sqrt|g| (b4^(-3/4))^2 = Cos z: the factor b4^(-3/4) keeps every normalisation integral; the proper extra-time volume carries b4^(3/2), so the rescaling identity reads KS(a4,0, b4,0; Delta k, v_t) = KS(0, 1; Delta k e^{-a4,0}, v_t e^{-3 a4,0} b4,0^{3/2})"];
gOB = Sum[geoB["gup"][[mu]] . geoB["Om"][[mu]], {mu, 8}];
addCheck["K4_background_b4_1",
  rftZeroQ[gOB - (3 H g[[1]] + (3/4) (Derivative[1][b4][x4]/b4[x4]) g[[5]])] && rftZeroQ[(gOB /. b4 -> (1 &)) - 3 H g[[1]]],
  "gamma^mu Omega_mu = 3 H gamma^(x0) + (3/4)(b4'/b4) gamma^(x4) in the metric with b4 and = 3 H gamma^(x0) at b4 = 1, the value ks-theory.json (geometry.spinConnection) uses: on the background of the record (b4 = 1, the vacuum history of Revision/metric_b4/results/vacuum-b4.json) no recorded number changes"];
failed = Count[checks, c_ /; c["verdict"] =!= "PASS"];
out = FileNameJoin[{$revDir, "kohn_sham", "reports", "ks-b4-wolfram.json"}];
s = ExportString[<|"producer" -> "Revision/kohn_sham/theory/verify_ks_b4.wls", "checkCount" -> Length[checks], "failedCount" -> failed,
   "verdict" -> If[failed == 0, "PASS", "FAIL"], "checks" -> checks|>, "JSON", "Compact" -> False];
If[Quiet[BinaryWrite[out, StringToByteArray[s <> "\n", "UTF-8"]]] === $Failed, Print["ERROR  cannot write ", out]; Exit[1]];
Close[out];
Print[Length[checks] - failed, "/", Length[checks], " checks passed; ", Round[AbsoluteTime[] - t0, 0.1], " s"];
Exit[If[failed == 0, 0, 1]];
