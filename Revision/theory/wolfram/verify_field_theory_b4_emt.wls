#!/usr/bin/env wolframscript
(* ::Package:: *)

(* verify_field_theory_b4_emt.wls

   The metric-dependent part of the field theory (Revision/SPEC.md sections 1-4) for the user's metric of 2026-10-14,
   g55 = g66 = g77 = -E^(-2 a4[x4]) b4[x4] Sin[6 H x0]^(1/3) (b4 > 0; b4 = 1 is the metric before 2026-10-14), in the
   author's coordinates x0..x7 (x0 = the hidden direction, Wolfram position 1; x4 = position 5).

   Why a supplement.  RevisionFieldTheory.wl is written for an arbitrary diagonal vielbein; everything that does
   not depend on the metric (the Clifford fixture, the Grassmann algebra, the Lagrangian's form, the variational
   identities) is unchanged.  verify_field_theory.wls checks those AND the metric-dependent statements for the
   vielbein of the metric before 2026-10-14 (b4 = 1) (about 5 minutes with parallel subkernels); its outputs field-theory.json and
   reports/wolfram-field-theory.json remain the record of the case b4 = 1.  This script loads the SAME package,
   replaces the vielbein by the one of the metric with b4 (f(x5..x7) = E^-a4 b4^(1/2) Sin[z]^(1/6)), rebuilds the
   geometry with the package's own functions and re-checks every metric-dependent statement for general b4:
   metric, vielbein, sqrt|det g|, Christoffel symbols, Ricci tensor (compared with Revision/metric_b4), the spin
   connection and its curvature, gamma^mu Omega_mu (per direction and in total), the explicit Dirac operator and
   field equation for both statistics, the block form and the evolution form.
   THIS FILE: the energy-momentum tensor by vielbein variation in the metric with b4, for one statistics given as
   the argument (C = dirac16complex00, commuting; G = dirac16complex, Grassmann; default C) (the corresponding section of verify_field_theory.wls took 444.5 s for both statistics at b4 = 1).
   Writes Revision/theory/reports/wolfram-field-theory-b4-emt-<C|G>.json.  Usage: wolframscript -file Revision/theory/wolfram/verify_field_theory_b4_emt.wls C   (or G) *)

$here = DirectoryName[$InputFileName];
$theoryDir = ExpandFileName[FileNameJoin[{$here, ".."}]];
$revDir = ExpandFileName[FileNameJoin[{$theoryDir, ".."}]];
If[Get[FileNameJoin[{$here, "RevisionFieldTheory.wl"}]] === $Failed, Print["ERROR  RevisionFieldTheory.wl: Get failed"]; Exit[1]];
rftLoadFixture[FileNameJoin[{$revDir, "algebra", "gammas.json"}]];
t0 = AbsoluteTime[]; tSec = t0;
section[name_] := (Print["[", Round[AbsoluteTime[] - tSec, 0.1], " s] -> ", name]; tSec = AbsoluteTime[]);
checks = {};
addCheck[name_String, ok_, detail_String] := (
  AppendTo[checks, <|"name" -> name, "verdict" -> If[TrueQ[ok], "PASS", "FAIL"], "detail" -> detail|>];
  Print[If[TrueQ[ok], "PASS  ", "FAIL  "], name]);
formulas = {};
wl[e_] := ToString[e, InputForm];
addFormula[key_String, desc_String, e_] := AppendTo[formulas, <|"key" -> key, "description" -> desc, "wl" -> wl[e]|>];
addFormulaText[key_String, desc_String, text_String] := AppendTo[formulas, <|"key" -> key, "description" -> desc, "wl" -> text|>];
statName["G"] = "dirac16complex (Grassmann)"; statName["C"] = "dirac16complex00 (commuting)";
stats = {"G", "C"};

(* ---------------------------------------------------------------- the metric with b4: the package's globals *)
rftF = {Cot[rftZ], E^a4[x4] Sin[rftZ]^(1/6), E^a4[x4] Sin[rftZ]^(1/6), E^a4[x4] Sin[rftZ]^(1/6), 1,
        E^(-a4[x4]) Sqrt[b4[x4]] Sin[rftZ]^(1/6), E^(-a4[x4]) Sqrt[b4[x4]] Sin[rftZ]^(1/6), E^(-a4[x4]) Sqrt[b4[x4]] Sin[rftZ]^(1/6)};
(* the author's coordinates x0..x7 (Wolfram position k + 1 holds xk: x0 = 1, x4 = 5) *)
rftMetricAuthor = {{Cot[6 H x0]^2,0,0,0,0,0,0,0},{0,E^(2 a4[x4]) Sin[6 H x0]^(1/3),0,0,0,0,0,0},
  {0,0,E^(2 a4[x4]) Sin[6 H x0]^(1/3),0,0,0,0,0},{0,0,0,E^(2 a4[x4]) Sin[6 H x0]^(1/3),0,0,0,0},
  {0,0,0,0,-1,0,0,0},{0,0,0,0,0,-E^(-2 a4[x4]) b4[x4] Sin[6 H x0]^(1/3),0,0},
  {0,0,0,0,0,0,-E^(-2 a4[x4]) b4[x4] Sin[6 H x0]^(1/3),0},{0,0,0,0,0,0,0,-E^(-2 a4[x4]) b4[x4] Sin[6 H x0]^(1/3)}};
rftAssumptions = {H > 0, 0 < 6 H x0 < Pi/2, Element[a4[x4], Reals], Element[x4, Reals], b4[x4] > 0};
rftE0 = DiagonalMatrix[rftF]; rftEinv0 = DiagonalMatrix[1/rftF];
rftG0 = Transpose[rftE0] . rftEta . rftE0; rftGinv0 = Inverse[rftG0];
rftSqrtG0 = b4[x4]^(3/2) Cos[rftZ];
g = rftGam; eta = rftEta; id16 = rftI16; z16 = rftZ16; Cm = rftC;
X = rftX; f = rftF; sg = rftSqrtG0;
a4p = Derivative[1][a4][x4]; u = Derivative[1][b4][x4]/b4[x4];
b1 = {b4 -> (1 &)};

section["geometry"];
rftBuildGeometry[];
Gm = rftGamma0; gup = rftGup0;
st = If[Length[$ScriptCommandLine] > 1 && MemberQ[{"C", "G"}, $ScriptCommandLine[[2]]], $ScriptCommandLine[[2]], "C"];
P = rftField[st]; Pc = rftFieldC[st];
L0 = rftL0[st, rftGeo0, P, Pc]; Sx = rftSbil[st, P, Pc];
section["energy-momentum tensor by vielbein variation, statistics " <> st];
bilM[st_, Pc_, M_, P_] := sDot[st, Pc, matVec[st, Cm . M, P]];
pb = rftPsibar[st, Pc];
Bmat = Table[sAdd[st, {sDot[st, vecMat[st, pb, gup[[r]]], rftDPsi[st, rftGeo0, P, s]], sScal[st, -1, sDot[st, vecMat[st, rftDPsibar[st, rftGeo0, Pc, s], gup[[r]]], P]]}], {r, 8}, {s, 8}];
Sig[n_, r_] := (1/4) (gup[[n]] . gup[[r]] - gup[[r]] . gup[[n]]);
Aten = Table[If[Length[Union[{l, n, r}]] < 3, sZero[st], bilM[st, Pc, gup[[l]] . Sig[n, r] + Sig[n, r] . gup[[l]], P]], {l, 8}, {n, 8}, {r, 8}];
divA = Table[sScal[st, 1/sg, sAdd[st, Table[sD[st, sScal[st, sg, Aten[[l, n, r]]], X[[l]]], {l, 8}]]], {n, 8}, {r, 8}];
canon[n_, mu_] := sAdd[st, {If[n == mu, L0, sZero[st]], sScal[st, -1/2, Bmat[[n, mu]]]}];
Tvar = Table[sScal[st, f[[mu]], rftTvar[st, mu, n, P, Pc, L0]], {n, 8}, {mu, 8}];
Print["   ", st, " vielbein variations done"];
okF = And @@ Flatten[Table[sZeroQ[st, sAdd[st, {Tvar[[n, mu]], sScal[st, -1, canon[n, mu]], sScal[st, rftG0[[mu, mu]]/4, divA[[n, mu]]]}]], {n, 8}, {mu, 8}]];
addCheck["T_vielbein_variation_closed_form_" <> st <> "_b4", okF,
  "metric with b4, " <> statName[st] <> ": for all 64 components T^nu_mu := e^b_mu (1/sqrt g) delta S / delta e^b_nu equals delta^nu_mu L0 - (1/2)(Psibar gamma^nu D_mu Psi - D_mu Psibar gamma^nu Psi) - (1/4) g_mu,rho nabla_l (Psibar {gamma^l, Sigma^(nu rho)} Psi), the formula of field-theory.json"];
Tsym = Table[sAdd[st, {If[n == mu, L0, sZero[st]], sScal[st, -1/4, Bmat[[n, mu]]], sScal[st, -1/4 rftG0[[mu, mu]] rftGinv0[[n, n]], Bmat[[mu, n]]]}], {n, 8}, {mu, 8}];
okSym = And @@ Flatten[Table[sZeroQ[st, sAdd[st, {sScal[st, rftGinv0[[r, r]], Tvar[[n, r]]], sScal[st, rftGinv0[[n, n]], Tvar[[r, n]]], sScal[st, -2 rftGinv0[[r, r]], Tsym[[n, r]]]}]], {n, 8}, {r, n, 8}]];
addCheck["T_symmetric_part_Belinfante_" <> st <> "_b4", okSym, "metric with b4, " <> statName[st] <> ": the symmetric part of the variation tensor equals T_sym of field-theory.json"];
K[mu_] := sScal[st, 1/(2 f[[mu]]), sAdd[st, {bilM[st, Pc, g[[mu]], vD[st, P, X[[mu]]]], sScal[st, -1, sDot[st, vecMat[st, vD[st, rftPsibar[st, Pc], X[[mu]]], g[[mu]]], P]]}]];
okDiag = And @@ Table[sZeroQ[st, sAdd[st, {Tsym[[mu, mu]], sScal[st, -1, L0], K[mu]}]], {mu, 8}];
addCheck["T_diagonal_components_" <> st <> "_b4", okDiag, "metric with b4, " <> statName[st] <> ": T^mu_mu (no sum) = L0 - K_mu, K_mu = (1/(2 f_mu))(Psibar gamma^(mu) d_mu Psi - d_mu Psibar gamma^(mu) Psi), f_5..7 = E^-a4 b4^(1/2) Sin[z]^(1/6)"];
(* Wolfram positions: x4 = 5, x0 = 1 *)
B40 = sAdd[st, {bilM[st, Pc, g[[5]], vD[st, P, x0]], sScal[st, -1, sDot[st, vecMat[st, vD[st, rftPsibar[st, Pc], x0], g[[5]]], P]]}];
B04 = sAdd[st, {bilM[st, Pc, g[[1]], vD[st, P, x4]], sScal[st, -1, sDot[st, vecMat[st, vD[st, rftPsibar[st, Pc], x4], g[[1]]], P]]}];
addCheck["T_x4_x0_component_" <> st <> "_b4",
  sZeroQ[st, sAdd[st, {Tsym[[5, 1]], sScal[st, 1/4, B40], sScal[st, -Cot[rftZ]/4, B04]}]] && sZeroQ[st, sAdd[st, {Tsym[[1, 5]], sScal[st, Tan[rftZ]^2, Tsym[[5, 1]]]}]],
  "metric with b4, " <> statName[st] <> ": T^x4_x0 = -(1/4)(B40 - Cot[z] B04) and T^x0_x4 = -Tan[z]^2 T^x4_x0, as in field-theory.json"];
section["done"];
failed = Count[checks, c_ /; c["verdict"] =!= "PASS"];
jsonEsc[s_String] := StringReplace[s, {"\\" -> "\\\\", "\"" -> "\\\"", "\n" -> "\\n", "\t" -> "\\t"}];
toJSON[s_String, _] := "\"" <> jsonEsc[s] <> "\"";
toJSON[n_Integer, _] := ToString[n];
toJSON[l_List, ind_] := If[l === {}, "[]", "[\n" <> StringRiffle[(StringRepeat[" ", ind + 2] <> toJSON[#, ind + 2]) & /@ l, ",\n"] <> "\n" <> StringRepeat[" ", ind] <> "]"];
toJSON[a_Association, ind_] := If[Length[a] == 0, "{}", "{\n" <> StringRiffle[KeyValueMap[(StringRepeat[" ", ind + 2] <> toJSON[#1, 0] <> ": " <> toJSON[#2, ind + 2]) &, a], ",\n"] <> "\n" <> StringRepeat[" ", ind] <> "}"];
outPath = FileNameJoin[{$theoryDir, "reports", "wolfram-field-theory-b4-emt-" <> st <> ".json"}];
outS = Quiet[OpenWrite[outPath, BinaryFormat -> True]];
If[Head[outS] =!= OutputStream, Print["ERROR  cannot write ", outPath]; Exit[1]];
BinaryWrite[outS, ToCharacterCode[toJSON[<|"producer" -> "Revision/theory/wolfram/verify_field_theory_b4_emt.wls " <> st, "checkCount" -> Length[checks], "failedCount" -> failed,
    "verdict" -> If[failed == 0, "PASS", "FAIL"], "checks" -> checks|>, 0] <> "\n", "UTF-8"]];
Close[outS];
Print[Length[checks] - failed, "/", Length[checks], " checks passed; total time ", Round[AbsoluteTime[] - t0, 0.1], " s"];
Exit[If[failed == 0, 0, 1]];
