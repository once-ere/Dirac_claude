#!/usr/bin/env wolframscript
(* ::Package:: *)

(* verify_dark_sector.wls

   Independent Wolfram verification of the dark-sector record (Revision/dark_sector) for the corrected primordial metric
   of 2026-10-16 (version 2; Revision/SPEC.md section 1):
     DiagonalMatrix[{E^(-2 a4[x4]) b4[x4] Cot[6 H x0]^2, E^(2 a4[x4]) (x3), -1, -E^(-2 a4[x4]) b4[x4] (Sin[6 H x0]^2)^(1/6) (x3)}]
   in the author's coordinates {x0, ..., x7}, every real z = 6 H x0 (the exact normal form of
   Revision/metric_warped/wolfram/MetricWarped.wl: Sin -> sv, Cos -> cv signed, (Sin^2)^k -> w^(12 k)).  Nothing of the
   Python scripts is used: the Christoffel symbols are those of MetricWarped`MWCurvature, the gammas the author's T16 of
   Revision/algebra/gammas.json (RevisionFieldTheory.wl loader), the record's history source that of
   Revision/field_equations_a4/a4-equations.json.

   Checks:
     D1  |det g| = (E^(-a4) b4^2 Cot[z] |Sin[z]|^(1/2))^2: sqrt|g| = E^(-a4) b4^2 |Cot z| |Sin z|^(1/2); proper extra-time
         volume element E^(-3 a4) b4^(3/2) |Sin z|^(1/2).
     D2  the conservation identities of a diagonal T(x4, x0) from the metric's Christoffel symbols:
         nabla_mu T^mu_x4 = -d4 rho - 3 a4' (rho + p3) - h4 (rho + p0) - 3 h4 (rho + p_t), h4 = b4'/(2 b4) - a4';
         nabla_mu T^mu_x0 = d0 p0 + 3 H Cot[z] (p0 - p_t) (no a4, b4); the others vanish.
     D3  w_eff = -1 - (1/3) d ln rho_4/d ln a for rho_4 ~ E E^(-3 A) (E^(-4 A) B^2)^(-s) with
         dE/dA = -3 P3 - (B'/(2 B) - 1)(P0 + 3 Pt): w_eff = P3/E + (beta/2 - 1)(P0 + 3 Pt)/(3 E) - s (4 - 2 beta)/3.
     D4  the condensate with the author's T16: A = -M gamma^(x4) + c gamma^(x4) gamma^(x0) - (u - a4'/2) I16 gives
         C A + A^T C = -2 (u - a4'/2) C (S ~ E^(a4) b4^(-2)) and (C g4 A - A^T C g4)/2 = M C, for every c.
     D5  the kinetic gas of free modes (omega^2 = M^2 + k^2 E^(-2A) + l^2 E^(2A)/B - q^2 E^(2A)/B, density E^A B^(-2))
         satisfies the x4 identity.
     D6  the record's history source (a4-equations.json exponentialHistory.authorWeights.historySource_kappaT_minus_Lam) is
         anisotropic (p3 != p0 as polynomials in kk), so no homogeneous condensate (p3 = p0 = p_t) sources it; it equals the
         record of dirac16complex00 (eos-theory.json condensate.historyRequiredSource).
     D7  on the history S ~ E^(-(5/3) a4): u = lambda S/m = u0 E^(-(5/3) a4), the ratio u/(2 + u) has wa = (10/3) u/(2 + u)^2.
   Writes Revision/dark_sector/reports/wolfram-dark-sector.json (UTF-8, LF, no time stamps), or the file given as the first
   argument.  Exit 0 iff all pass.
   Usage (repository root): wolframscript -file Revision/dark_sector/wolfram/verify_dark_sector.wls [OUT] *)

$here = DirectoryName[$InputFileName];
$rev = If[StringQ[Environment["REVISION_DIR"]], Environment["REVISION_DIR"], ExpandFileName[FileNameJoin[{$here, "..", ".."}]]];
$out = If[Length[$ScriptCommandLine] >= 2, $ScriptCommandLine[[2]], FileNameJoin[{$rev, "dark_sector", "reports", "wolfram-dark-sector.json"}]];
If[Get[FileNameJoin[{$rev, "metric_warped", "wolfram", "MetricWarped.wl"}]] === $Failed, Print["ERROR  MetricWarped.wl: Get failed"]; Exit[1]];
If[Get[FileNameJoin[{$rev, "theory", "wolfram", "RevisionFieldTheory.wl"}]] === $Failed, Print["ERROR  RevisionFieldTheory.wl"]; Exit[1]];
rftLoadFixture[FileNameJoin[{$rev, "algebra", "gammas.json"}]];
a4eq = Import[FileNameJoin[{$rev, "field_equations_a4", "a4-equations.json"}], "RawJSON"];
If[! AssociationQ[a4eq], Print["ERROR  a4-equations.json not readable"]; Exit[1]];
eos00 = Import[If[StringQ[Environment["EOS00_JSON"]], Environment["EOS00_JSON"], FileNameJoin[{$rev, "dark_sector", "dirac16complex00", "eos-theory.json"}]], "RawJSON"];
If[! AssociationQ[eos00], Print["ERROR  eos-theory.json not readable"]; Exit[1]];
checks = {};
check[name_, ok_, detail_] := (AppendTo[checks, <|"name" -> name, "verdict" -> If[TrueQ[ok], "PASS", "FAIL"], "detail" -> detail|>];
  Print[If[TrueQ[ok], "PASS  ", "FAIL  "], name]);

Hs = MetricWarped`H; x4s = MetricWarped`x4; x0s = MetricWarped`x0; a4f = MetricWarped`a4; b4f = MetricWarped`b4;
X = MetricWarped`MWCoordinates; z = 6 Hs x0s;
diag = Join[{E^(-2 a4f[x4s]) b4f[x4s] Cot[z]^2}, ConstantArray[E^(2 a4f[x4s]), 3], {-1},
   ConstantArray[-E^(-2 a4f[x4s]) b4f[x4s] (Sin[z]^2)^(1/6), 3]];
nz = MetricWarped`MWZeroQ;

(* D1 *)
detg = Times @@ diag;
check["D1_volume", nz[detg - (E^(-a4f[x4s]) b4f[x4s]^2 Cot[z])^2 (Sin[z]^2)^(1/2)] &&
   nz[(-diag[[6]]) (-diag[[7]]) (-diag[[8]]) - (E^(-3 a4f[x4s]) b4f[x4s]^(3/2))^2 (Sin[z]^2)^(1/2)],
  "|det g| = (E^(-a4) b4^2 Cot z)^2 (Sin^2 z)^(1/2) (det g > 0 for every real z): sqrt|g| = E^(-a4) b4^2 |Cot z| |Sin z|^(1/2); the " <>
  "proper extra-time volume element is E^(-3 a4) b4^(3/2) |Sin z|^(1/2)"];

(* D2 *)
curv = MetricWarped`MWCurvature[diag, X];
Gm = curv["christoffel"];
T = DiagonalMatrix[{p0[x4s, x0s], p3[x4s, x0s], p3[x4s, x0s], p3[x4s, x0s], -rho[x4s, x0s], pt[x4s, x0s], pt[x4s, x0s], pt[x4s, x0s]}];
div = Table[Sum[D[T[[m, nu]], X[[m]]], {m, 8}] + Sum[Gm[[m, m, l]] T[[l, nu]], {m, 8}, {l, 8}] - Sum[Gm[[l, m, nu]] T[[m, l]], {m, 8}, {l, 8}], {nu, 8}];
h4 = b4f'[x4s]/(2 b4f[x4s]) - a4f'[x4s];
exp4 = -D[rho[x4s, x0s], x4s] - 3 a4f'[x4s] (rho[x4s, x0s] + p3[x4s, x0s]) - h4 (rho[x4s, x0s] + p0[x4s, x0s]) - 3 h4 (rho[x4s, x0s] + pt[x4s, x0s]);
exp0 = D[p0[x4s, x0s], x0s] + 3 Hs Cot[z] (p0[x4s, x0s] - pt[x4s, x0s]);
check["D2_conservation", nz[div[[5]] - exp4] && nz[div[[1]] - exp0] && FreeQ[div[[1]], a4f | b4f] && nz[div[[{2, 3, 4, 6, 7, 8}]]],
  "nabla_mu T^mu_x4 = -d4 rho - 3 a4' (rho + p3) - h4 (rho + p0) - 3 h4 (rho + p_t), h4 = b4'/(2 b4) - a4'; nabla_mu T^mu_x0 = d0 p0 + " <>
  "3 H Cot[z] (p0 - p_t) (no a4, b4); the other components vanish; every real z"];

(* D3 *)
Clear[Ef, Bf];
rho4 = Ef[A] E^(-3 A) (E^(-4 A) Bf[A]^2)^(-s);
wq = -1 - (1/3) D[Log[rho4], A] /. Ef'[A] -> -3 P3s - (Bf'[A]/(2 Bf[A]) - 1) (P0s + 3 Pts);
wq = Simplify[wq /. Bf'[A] -> beta Bf[A] /. Ef[A] -> Es, Bf[A] > 0 && Es > 0];
check["D3_w_eff_general", Simplify[wq - (P3s/Es + (beta/2 - 1) (P0s + 3 Pts)/(3 Es) - s (4 - 2 beta)/3)] === 0,
  "w_eff = " <> ToString[InputForm[wq]] <> " = P3/E + (beta/2 - 1)(P0 + 3 Pt)/(3E) - s (4 - 2 beta)/3: A, B (s = 0), C (s = 1)"];

(* D4: the author's T16 in the order x0..x7 (positions 1..8) *)
gm = rftGam; C4 = gm[[1]] . gm[[2]] . gm[[3]] . gm[[4]]; I16 = IdentityMatrix[16];
Am = -Mm gm[[5]] + cg gm[[5]] . gm[[1]] - (uu - ad/2) I16;
lhsS = Expand[C4 . Am + Transpose[Am] . C4 + 2 (uu - ad/2) C4];
K4 = Expand[(C4 . gm[[5]] . Am - Transpose[Am] . C4 . gm[[5]])/2 - Mm C4];
hc = a4eq["fields"]["dirac16complex00"]["homogeneousCondensate"];
check["D4_condensate_T16", AllTrue[Flatten[lhsS], # === 0 &] && AllTrue[Flatten[K4], # === 0 &] &&
   StringContainsQ[hc, "S = e^{a4} b4^{-2} S0 (exact)"],
  "A = -M gamma^(x4) + c gamma^(x4) gamma^(x0) - (b4'/b4 - a4'/2) I16 with the author's T16 (c = (3/2) H E^a4 b4^(-1/2), any value): " <>
  "C A + A^T C = -2 (b4'/b4 - a4'/2) C, so S ~ E^(a4) b4^(-2); (C g4 A - A^T C g4)/2 = M C (K_x4 = M S); as a4-equations.json states"];

(* D5 *)
om = Sqrt[Mm^2 + k^2 E^(-2 A) + l^2 E^(2 A)/Bf[A] - q^2 E^(2 A)/Bf[A]]; nn = E^A Bf[A]^(-2);
rg = nn om; p3g = nn k^2 E^(-2 A)/(3 om); p0g = nn l^2 E^(2 A)/(Bf[A] om); ptg = -nn q^2 E^(2 A)/(Bf[A] 3 om);
hb = Bf'[A]/(2 Bf[A]) - 1;
check["D5_kinetic_gas", Simplify[D[rg, A] + 3 (rg + p3g) + hb (rg + p0g) + 3 hb (rg + ptg), Bf[A] > 0] === 0,
  "free modes, omega^2 = M^2 + k^2 E^(-2 a4) + l^2 E^(2 a4)/b4 - q^2 E^(2 a4)/b4 (l hidden, q extra-time momentum), density E^(a4) b4^(-2): " <>
  "d rho/d a4 = -3 (rho + p3) - (b4'/(2 b4 a4') - 1)(rho + p0) - 3 (b4'/(2 b4 a4') - 1)(rho + p_t) exactly"];

(* D6 *)
src = a4eq["exponentialHistory"]["authorWeights"]["historySource_kappaT_minus_Lam"];
toE[s_] := ToExpression[StringReplace[s, {"**" -> "^", "kk" -> "kkv"}]];
srcE = AssociationMap[toE[src[#]["input"]] &, {"minus_rho", "p3", "p0", "pt"}];
aniso = Expand[srcE["p3"] - srcE["p0"]];
rec00 = eos00["condensate"]["historyRequiredSource"];
same00 = AllTrue[{"minus_rho", "p3", "p0", "pt"}, Expand[toE[rec00[#]] - srcE[#]] === 0 &];
check["D6_history_source_anisotropic", aniso =!= 0 && PolynomialQ[aniso, kkv] && srcE["p0"] === srcE["pt"] && same00,
  "the record's history a4 = H x4, b4 = E^((4/3) H x4) with the author's weights needs kappa T - Lambda delta = " <>
  "(minus_rho, p3, p0 = pt) = " <> ToString[InputForm[{srcE["minus_rho"], srcE["p3"], srcE["p0"]}]] <>
  " (kkv = E^((2/3) H x4)); kappa (p3 - p0) = " <> ToString[InputForm[aniso]] <> " != 0, while every homogeneous condensate has p3 = p0 = p_t: " <>
  "no condensate sources the history; the record of dirac16complex00 states the same source: " <> ToString[same00]];

(* D7 *)
uq = u0 E^(-(5/3) A);
wr = uq/(2 + uq);
check["D7_condensate_drift", Simplify[(E^A (E^((4/3) A))^(-2)) - E^(-(5/3) A)] === 0 && Simplify[-D[wr, A] - (10/3) uq/(2 + uq)^2] === 0,
  "S ~ E^(a4) b4^(-2) = E^(-(5/3) a4) on the history, so u = lambda S/m = u0 E^(-(5/3) a4) and the ratio u/(2 + u) has wa = -d/da4 = (10/3) u/(2 + u)^2"];

failed = Count[checks, c_ /; c["verdict"] =!= "PASS"];
out = <|"producer" -> "Revision/dark_sector/wolfram/verify_dark_sector.wls",
   "metric" -> "the corrected primordial metric of 2026-10-16 (version 2; Revision/SPEC.md section 1), every real z",
   "history" -> "a4 = H x4, b4 = E^((4/3) H x4) (the record's history, a prescribed background)",
   "checks" -> checks, "checkCount" -> Length[checks], "failedCount" -> failed|>;
s = ExportString[out, "JSON", "Compact" -> False];
If[! DirectoryQ[DirectoryName[$out]], CreateDirectory[DirectoryName[$out]]];
If[Quiet[BinaryWrite[$out, ByteArray[ToCharacterCode[StringReplace[s, "\r\n" -> "\n"] <> "\n"]]]] === $Failed, Print["ERROR  cannot write ", $out]; Exit[1]];
Close[$out];
Print[Length[checks] - failed, "/", Length[checks], " checks passed"];
Exit[If[failed == 0, 0, 1]];
