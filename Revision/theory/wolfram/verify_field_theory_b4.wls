#!/usr/bin/env wolframscript
(* ::Package:: *)

(* verify_field_theory_b4.wls

   The metric-dependent part of the field theory (Revision/SPEC.md sections 1-4) for the user's metric of 2026-10-14,
   g55 = g66 = g77 = -E^(-2 a4[x4]) b4[x4] Sin[6 H x8]^(1/3) (b4 > 0; b4 = 1 is the metric before 2026-10-14).

   Why a supplement.  RevisionFieldTheory.wl is written for an arbitrary diagonal vielbein; everything that does
   not depend on the metric (the Clifford fixture, the Grassmann algebra, the Lagrangian's form, the variational
   identities) is unchanged.  verify_field_theory.wls checks those AND the metric-dependent statements for the
   vielbein of the metric before 2026-10-14 (b4 = 1) in about 30 to 45 minutes; its outputs field-theory.json and
   reports/wolfram-field-theory.json remain the record of the case b4 = 1.  This script loads the SAME package,
   replaces the vielbein by the one of the metric with b4 (f(x5..x7) = E^-a4 b4^(1/2) Sin[z]^(1/6)), rebuilds the
   geometry with the package's own functions and re-checks every metric-dependent statement for general b4:
   metric, vielbein, sqrt|det g|, Christoffel symbols, Ricci tensor (compared with Revision/metric_b4), the spin
   connection and its curvature, gamma^mu Omega_mu (per direction and in total), the explicit Dirac operator and
   field equation for both statistics, the block form and the evolution form.
   Writes Revision/theory/field-theory-b4.json (formulas) and Revision/theory/reports/wolfram-field-theory-b4.json
   (checks); LF, no time stamps.  Exit code 0 iff every check passes.
   Usage (repository root): wolframscript -file Revision/theory/wolfram/verify_field_theory_b4.wls *)

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
rftF = {E^a4[x4] Sin[rftZ]^(1/6), E^a4[x4] Sin[rftZ]^(1/6), E^a4[x4] Sin[rftZ]^(1/6), 1,
        E^(-a4[x4]) Sqrt[b4[x4]] Sin[rftZ]^(1/6), E^(-a4[x4]) Sqrt[b4[x4]] Sin[rftZ]^(1/6), E^(-a4[x4]) Sqrt[b4[x4]] Sin[rftZ]^(1/6), Cot[rftZ]};
rftMetricAuthor = {{E^(2 a4[x4]) Sin[6 H x8]^(1/3),0,0,0,0,0,0,0},{0,E^(2 a4[x4]) Sin[6 H x8]^(1/3),0,0,0,0,0,0},
  {0,0,E^(2 a4[x4]) Sin[6 H x8]^(1/3),0,0,0,0,0},{0,0,0,-1,0,0,0,0},
  {0,0,0,0,-E^(-2 a4[x4]) b4[x4] Sin[6 H x8]^(1/3),0,0,0},{0,0,0,0,0,-E^(-2 a4[x4]) b4[x4] Sin[6 H x8]^(1/3),0,0},
  {0,0,0,0,0,0,-E^(-2 a4[x4]) b4[x4] Sin[6 H x8]^(1/3),0},{0,0,0,0,0,0,0,Cot[6 H x8]^2}};
rftAssumptions = {H > 0, 0 < 6 H x8 < Pi/2, Element[a4[x4], Reals], Element[x4, Reals], b4[x4] > 0};
rftE0 = DiagonalMatrix[rftF]; rftEinv0 = DiagonalMatrix[1/rftF];
rftG0 = Transpose[rftE0] . rftEta . rftE0; rftGinv0 = Inverse[rftG0];
rftSqrtG0 = b4[x4]^(3/2) Cos[rftZ];
g = rftGam; eta = rftEta; id16 = rftI16; z16 = rftZ16; Cm = rftC;
X = rftX; f = rftF; sg = rftSqrtG0;
a4p = Derivative[1][a4][x4]; u = Derivative[1][b4][x4]/b4[x4];
b1 = {b4 -> (1 &)};

section["geometry"];
rftBuildGeometry[];
Gm = rftGamma0;
addCheck["metric_is_the_authors_b4",
  rftZeroQ[rftG0 - rftMetricAuthor] && rftZeroQ[Transpose[rftE0] . eta . rftE0 - rftMetricAuthor],
  "g = e^T eta e with the diagonal vielbein f(x1,x2,x3) = E^a4 Sin[z]^(1/6), f(x4) = 1, f(x5,x6,x7) = E^-a4 b4^(1/2) Sin[z]^(1/6), f(x8) = Cot[z] reproduces the metric of SPEC section 1 (2026-10-14) entry by entry"];
addCheck["vielbein_inverse",
  rftZeroQ[rftE0 . rftEinv0 - IdentityMatrix[8]] &&
  rftZeroQ[Table[Sum[rftEinv0[[mu, a]] rftEinv0[[nu, a]] eta[[a, a]], {a, 8}] - rftGinv0[[mu, nu]], {mu, 8}, {nu, 8}]],
  "e^a_mu e_a^nu = delta and e_a^mu e_b^nu eta^ab = g^munu"];
addCheck["sqrt_det_g",
  rftZeroQ[Det[rftG0] - b4[x4]^3 Cos[rftZ]^2] && rftZeroQ[Times @@ f - b4[x4]^(3/2) Cos[rftZ]],
  "det g = b4^3 Cos[z]^2, sqrt|det g| = f1...f8 = b4^(3/2) Cos[z] (constant in x4 only when b4 is)"];
gamNZ = DeleteCases[Flatten[Table[{l, mm, n, rftSimp[Gm[[l, mm, n]]]}, {l, 8}, {mm, 8}, {n, mm, 8}], 2], {_, _, _, 0}];
addFormula["christoffel_nonzero", "nonzero Christoffel symbols {l, m, n, Gamma^l_mn} (m <= n), indices 1..8 = x1..x8, metric with b4", gamNZ];
addCheck["christoffel_count",
  Length[gamNZ] == 25,
  "the Levi-Civita connection has " <> ToString[Length[gamNZ]] <> " independent nonzero symbols Gamma^l_mn (m <= n), as for b4 = 1; the extra-time ones now contain b4'/b4 (field-theory-b4.json christoffel_nonzero)"];
Rm = rftRiemann[Gm];
Ric = Table[Sum[Rm[[r, s, r, n]], {r, 8}], {s, 8}, {n, 8}];
RicMixed = Table[Sum[rftGinv0[[mu, s]] Ric[[s, nu]], {s, 8}], {mu, 8}, {nu, 8}];
Rs = Sum[RicMixed[[mu, mu]], {mu, 8}];
mb = Import[FileNameJoin[{$revDir, "metric_b4", "results", "metric-b4.json"}], "RawJSON"];
lab = {"x1", "x2", "x3", "x4", "x5", "x6", "x7", "x8"};
mbRic = Table[ToExpression[Lookup[mb["ricciMixed"], lab[[h]] <> "," <> lab[[j]], "0"]], {h, 8}, {j, 8}];
addCheck["ricci_equals_metric_b4_set",
  rftZeroQ[RicMixed - mbRic] && rftZeroQ[Rs - ToExpression[mb["ricciScalar"]]],
  "R^mu_nu and R computed here (package convention) equal Revision/metric_b4/results/metric-b4.json (compared there with the author's stored outputs Out[119], Out[124] of Dirac_Einstein-Lovelock_4+4_Nash.nb); R^4_8 and R^8_4 are proportional to b4'"];
addFormula["ricci_scalar", "Ricci scalar R (metric with b4)", rftSimp[Rs]];
addCheck["ricci_reduces_at_b4_1",
  rftZeroQ[(Rs /. b1) - 6 (a4p^2 - 7 H^2)],
  "at b4 = 1: R = 6 (a4'^2 - 7 H^2), the value of field-theory.json (b4 = 1)"];

section["spin connection"];
omMix = rftOmegaMix0; omLow = rftOmegaLow0; Om = rftOm0; gup = rftGup0;
addCheck["vielbein_postulate",
  rftZeroQ[Table[D[rftE0[[a, nu]], X[[mu]]] - Sum[Gm[[l, mu, nu]] rftE0[[a, l]], {l, 8}] + Sum[omMix[[mu, a, b]] rftE0[[b, nu]], {b, 8}], {mu, 8}, {a, 8}, {nu, 8}]],
  "d_mu e^a_nu - Gamma^l_mu,nu e^a_l + omega_mu^a_b e^b_nu = 0 for all 512 components"];
addCheck["omega_antisymmetric", rftZeroQ[Table[omLow[[mu, a, b]] + omLow[[mu, b, a]], {mu, 8}, {a, 8}, {b, 8}]], "omega_mu,ab = -omega_mu,ba"];
omExpected = Join[
  Flatten[Table[{{i, i, 4, E^a4[x4] Sin[rftZ]^(1/6) a4p}, {i, i, 8, H E^a4[x4] Sin[rftZ]^(1/6)}}, {i, 1, 3}], 1],
  Flatten[Table[{{t, 4, t, -E^(-a4[x4]) Sqrt[b4[x4]] Sin[rftZ]^(1/6) (a4p - u/2)}, {t, t, 8, -H E^(-a4[x4]) Sqrt[b4[x4]] Sin[rftZ]^(1/6)}}, {t, 5, 7}], 1]];
omNZ = DeleteCases[Flatten[Table[{mu, a, b, rftSimp[omLow[[mu, a, b]]]}, {mu, 8}, {a, 8}, {b, a + 1, 8}], 2], {_, _, _, 0}];
addCheck["omega_components",
  Length[omNZ] == 12 && Sort[omNZ[[All, 1 ;; 3]]] == Sort[omExpected[[All, 1 ;; 3]]] &&
  And @@ Table[rftZeroQ[omLow[[Sequence @@ e[[1 ;; 3]]]] - e[[4]]], {e, omExpected}],
  "12 independent nonzero omega_mu,ab (a < b): i = x1..x3: omega_i,(i)(x4) = a4' E^a4 Sin[z]^(1/6), omega_i,(i)(x8) = H E^a4 Sin[z]^(1/6); t = x5..x7: omega_t,(x4)(t) = -(a4' - b4'/(2 b4)) E^-a4 b4^(1/2) Sin[z]^(1/6), omega_t,(t)(x8) = -H E^-a4 b4^(1/2) Sin[z]^(1/6); omega_x4 = omega_x8 = 0"];
addFormula["omega_nonzero", "nonzero omega_mu,ab as {mu, a, b, value} with a < b (metric with b4)", omExpected];
covConst = Table[D[gup[[n]], X[[mu]]] + Sum[Gm[[n, mu, l]] gup[[l]], {l, 8}] + Om[[mu]] . gup[[n]] - gup[[n]] . Om[[mu]], {mu, 8}, {n, 8}];
addCheck["gamma_covariantly_constant", rftZeroQ[covConst], "D_mu gamma^nu = 0 for all 64 (mu, nu)"];
Fsp[mu_, nu_] := D[Om[[nu]], X[[mu]]] - D[Om[[mu]], X[[nu]]] + Om[[mu]] . Om[[nu]] - Om[[nu]] . Om[[mu]];
Rframe[a_, b_, mu_, nu_] := Sum[eta[[a, a]] rftE0[[a, r]] Rm[[r, s, mu, nu]] rftEinv0[[s, b]], {r, 8}, {s, 8}];
addCheck["spin_curvature_equals_Riemann",
  rftZeroQ[Table[Fsp[mu, nu] - (1/2) Sum[Rframe[a, b, mu, nu] rftS[[a, b]], {a, 8}, {b, 8}], {mu, 8}, {nu, mu + 1, 8}]],
  "[D_mu, D_nu] = (1/2) R_ab,mu,nu S^ab, all 28 pairs"];

section["gamma^mu Omega_mu"];
gO = Sum[gup[[mu]] . Om[[mu]], {mu, 8}];
perDir = Table[gup[[mu]] . Om[[mu]], {mu, 8}];
addCheck["gammaOmega_total",
  rftZeroQ[gO - (3 H g[[8]] + (3/4) u g[[4]])],
  "gamma^mu Omega_mu = 3 H gamma^(x8) + (3/4)(b4'/b4) gamma^(x4) (b4 = 1: 3 H gamma^(x8), field-theory.json)"];
addCheck["gammaOmega_per_direction",
  And @@ Table[rftZeroQ[perDir[[mu]] - (a4p/2 g[[4]] + H/2 g[[8]])], {mu, 1, 3}] &&
  And @@ Table[rftZeroQ[perDir[[mu]] - ((-a4p/2 + u/4) g[[4]] + H/2 g[[8]])], {mu, 5, 7}] &&
  rftZeroQ[perDir[[4]]] && rftZeroQ[perDir[[8]]],
  "per direction (no sum): gamma^(xi) Omega_xi = (a4'/2) gamma^(x4) + (H/2) gamma^(x8) (i = 1, 2, 3); gamma^(xt) Omega_xt = (-a4'/2 + b4'/(4 b4)) gamma^(x4) + (H/2) gamma^(x8) (t = 5, 6, 7); the x4 terms no longer cancel: their sum is (3/4) b4'/b4"];
addCheck["gammaOmega_divergence_form",
  rftZeroQ[gO - 1/(2 sg) Sum[D[sg gup[[mu]], X[[mu]]], {mu, 8}]] && rftZeroQ[Table[gup[[mu]] . Om[[mu]] + Om[[mu]] . gup[[mu]], {mu, 8}]],
  "{gamma^mu, Omega_mu} = 0 for each mu, hence gamma^mu Omega_mu = (1/(2 sqrt g)) d_mu (sqrt g gamma^mu); with sqrt g = b4^(3/2) Cos z the x4 term is (3/4)(b4'/b4) gamma^(x4)"];
addFormula["gammaOmega_total", "gamma^mu Omega_mu (sum over mu), metric with b4; gamma[xa] = gamma^(xa)", 3 H gamma["x8"] + (3/4) (Derivative[1][b4][x4]/b4[x4]) gamma["x4"]];

section["field equations"];
Do[With[{P = rftField[st]},
  Module[{lhs, rhs},
    lhs = rftDirac[st, rftGeo0, P];
    rhs = vAdd[st, Fold[vAdd[st, #1, #2] &, Table[matVec[st, g[[a]]/f[[a]], vD[st, P, X[[a]]]], {a, 8}]],
      matVec[st, 3 H g[[8]] + (3/4) u g[[4]], P]];
    addCheck["Dirac_operator_explicit_" <> st, And @@ Table[sZeroQ[st, sAdd[st, {lhs[[A]], sScal[st, -1, rhs[[A]]]}]], {A, 16}],
      "gamma^mu D_mu Psi = E^-a4 Sin[z]^(-1/6) (gamma^(x1) d1 + gamma^(x2) d2 + gamma^(x3) d3) Psi + gamma^(x4) d4 Psi + E^a4 b4^(-1/2) Sin[z]^(-1/6) (gamma^(x5) d5 + gamma^(x6) d6 + gamma^(x7) d7) Psi + Tan[z] gamma^(x8) d8 Psi + 3 H gamma^(x8) Psi + (3/4)(b4'/b4) gamma^(x4) Psi, for " <> statName[st]]]], {st, stats}];
addFormulaText["field_equation",
  "the Euler-Lagrange equation (both statistics) in the metric with b4, z = 6 H x8, V = m + U'(S); its derivation from the Lagrangian is metric-independent (field-theory.json)",
  "E^-a4[x4] Sin[z]^(-1/6) (g[x1] d1 + g[x2] d2 + g[x3] d3) Psi + g[x4] d4 Psi + E^a4[x4] b4[x4]^(-1/2) Sin[z]^(-1/6) (g[x5] d5 + g[x6] d6 + g[x7] d7) Psi + Tan[z] g[x8] d8 Psi + 3 H g[x8] Psi + (3/4) (b4'[x4]/b4[x4]) g[x4] Psi = (m + U'(S)) Psi"];
compStr = Table[Module[{terms = {}},
   Do[If[g[[a, A, B]] =!= 0, AppendTo[terms, g[[a, A, B]]/f[[a]] dd[rftCoordNames[[a]], Psi[B]]]], {a, 8}, {B, 16}];
   Do[If[g[[8, A, B]] =!= 0, AppendTo[terms, 3 H g[[8, A, B]] Psi[B]]], {B, 16}];
   Do[If[g[[4, A, B]] =!= 0, AppendTo[terms, (3/4) (Derivative[1][b4][x4]/b4[x4]) g[[4, A, B]] Psi[B]]], {B, 16}];
   wl[Total[terms] == V Psi[A]]], {A, 16}];
AppendTo[formulas, <|"key" -> "field_equation_components", "description" -> "the 16 component equations (gamma^mu D_mu Psi)_A = V Psi_A in the metric with b4, A = 1..16 (rows of the fixture gammas); dd[xa, Psi[B]] = d Psi_B / d xa", "wl" -> compStr|>];
Do[With[{P = rftField[st]},
  Module[{rest, d4, Sx, Ev},
    Sx = rftSbil[st, P, rftFieldC[st]];
    rest = vAdd[st, Fold[vAdd[st, #1, #2] &, Table[If[a == 4, Table[sZero[st], {16}], matVec[st, g[[a]]/f[[a]], vD[st, P, X[[a]]]]], {a, 8}]],
      matVec[st, 3 H g[[8]], P]];
    d4 = vAdd[st, matVec[st, -g[[4]], vAdd[st, rftVPsi[st, Sx, P], vScal[st, -1, rest]]], vScal[st, -(3/4) u, P]];
    Ev = vAdd[st, rftDirac[st, rftGeo0, P], vScal[st, -1, rftVPsi[st, Sx, P]]];
    addCheck["evolution_form_" <> st,
      g[[4]] . g[[4]] == -id16 &&
      And @@ Table[sZeroQ[st, sAdd[st, {matVec[st, g[[4]], vAdd[st, vD[st, P, x4], vScal[st, -1, d4]]][[A]], sScal[st, -1, Ev[[A]]]}]], {A, 16}],
      "the field equation is equivalent to d4 Psi = -gamma^(x4) [(m + U'(S)) Psi - sum_(a != 4) (1/f_a) gamma^(a) d_a Psi - 3 H gamma^(x8) Psi] - (3/4)(b4'/b4) Psi (exact; the extra term is the factor b4^(-3/4)), " <> statName[st]]]], {st, stats}];
addFormulaText["evolution_form", "first-order evolution form in the metric with b4",
  "d4 Psi = -g[x4] ((m + U'(S)) Psi - sum_(a != 4) (1/f_a) g[xa] d_a Psi - 3 H g[x8] Psi) - (3/4) (b4'[x4]/b4[x4]) Psi"];

section["energy exchange"];
Module[{Tdiag, divAll, expected, d4rho, d8p8},
  Tdiag = DiagonalMatrix[{p3[x4, x8], p3[x4, x8], p3[x4, x8], -rho[x4, x8], pt[x4, x8], pt[x4, x8], pt[x4, x8], p8[x4, x8]}];
  divAll = Table[Sum[D[sg Tdiag[[mu, nu]], X[[mu]]], {mu, 8}]/sg - Sum[Gm[[r, mu, nu]] Tdiag[[mu, r]], {mu, 8}, {r, 8}], {nu, 8}];
  d4rho = Derivative[1, 0][rho][x4, x8]; d8p8 = Derivative[0, 1][p8][x4, x8];
  expected = {0, 0, 0, -d4rho - 3 a4p (p3[x4, x8] - pt[x4, x8]) - (3/2) u (rho[x4, x8] + pt[x4, x8]), 0, 0, 0,
    d8p8 + 3 H Cot[6 H x8] (2 p8[x4, x8] - p3[x4, x8] - pt[x4, x8])};
  addCheck["energy_exchange_equation_b4",
    rftZeroQ[divAll - expected] && !rftZeroQ[divAll[[4]] - (-d4rho - 3 a4p (p3[x4, x8] - pt[x4, x8]))],
    "for a diagonal T = diag(p3, p3, p3, -rho, p_t, p_t, p_t, p8) (functions of x4 and x8) in the metric with b4: nabla_mu T^mu_x4 = -d rho/d x4 - 3 a4' (p3 - p_t) - (3/2)(b4'/b4)(rho + p_t), nabla_mu T^mu_x8 = d p8/d x8 + 3 H Cot[z] (2 p8 - p3 - p_t), the other components 0; control: the b = 1 formula (without the b4 term) is detected as wrong for general b4"];
  AppendTo[formulas, <|"key" -> "energy_exchange", "description" -> "{nabla_mu T^mu_nu, nu = x1..x8} for the diagonal T above, metric with b4",
    "wl" -> wl[expected]|>]];

section["done"];
failed = Count[checks, c_ /; c["verdict"] =!= "PASS"];
jsonEsc[s_String] := StringReplace[s, {"\\" -> "\\\\", "\"" -> "\\\"", "\n" -> "\\n", "\t" -> "\\t"}];
toJSON[s_String, _] := "\"" <> jsonEsc[s] <> "\"";
toJSON[True, _] := "true"; toJSON[False, _] := "false"; toJSON[n_Integer, _] := ToString[n];
toJSON[l_List, ind_] := If[l === {}, "[]", "[\n" <> StringRiffle[(StringRepeat[" ", ind + 2] <> toJSON[#, ind + 2]) & /@ l, ",\n"] <> "\n" <> StringRepeat[" ", ind] <> "]"];
toJSON[a_Association, ind_] := If[Length[a] == 0, "{}", "{\n" <> StringRiffle[KeyValueMap[(StringRepeat[" ", ind + 2] <> toJSON[#1, 0] <> ": " <> toJSON[#2, ind + 2]) &, a], ",\n"] <> "\n" <> StringRepeat[" ", ind] <> "}"];
writeJSON[path_, data_] := Module[{s = Quiet[OpenWrite[path, BinaryFormat -> True]]},
  If[Head[s] =!= OutputStream, Print["ERROR  cannot write ", path]; Exit[1]];
  BinaryWrite[s, ToCharacterCode[toJSON[data, 0] <> "\n", "UTF-8"]]; Close[s]];
writeJSON[FileNameJoin[{$theoryDir, "field-theory-b4.json"}],
  <|"title" -> "Field theory: the metric-dependent formulas for the metric of 2026-10-14 with b4[x4] (supplement to field-theory.json, which is the case b4 = 1)",
    "producer" -> "Revision/theory/wolfram/verify_field_theory_b4.wls (with RevisionFieldTheory.wl)", "formulas" -> formulas|>];
writeJSON[FileNameJoin[{$theoryDir, "reports", "wolfram-field-theory-b4.json"}],
  <|"producer" -> "Revision/theory/wolfram/verify_field_theory_b4.wls", "checkCount" -> Length[checks], "failedCount" -> failed,
    "verdict" -> If[failed == 0, "PASS", "FAIL"], "checks" -> checks|>];
Print[Length[checks] - failed, "/", Length[checks], " checks passed; total time ", Round[AbsoluteTime[] - t0, 0.1], " s"];
Exit[If[failed == 0, 0, 1]];
