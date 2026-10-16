#!/usr/bin/env wolframscript
(* ::Package:: *)

(* verify_dark_sector_b4.wls

   Independent Wolfram verification of the dark-sector record (Revision/dark_sector) for the author's metric of
   2026-10-14 WITH b4[x4] (Dirac_Einstein-Lovelock_4+4_Nash.nb, In[48]: X = {x0[], ..., x7[]}; In[97]-In[102]:
   DiagonalMatrix[{Cot[6 H x0]^2, beta1 {beta3, beta3, beta3}, -1, -beta1 b4[x4] {1/beta3, 1/beta3, 1/beta3}}],
   beta1 = Sin[6 H x0]^(1/3), beta3 = E^(2 a4[x4])).  b4 is a function of x4 (never 1).  Nothing of the Python
   scripts is used: the metric is MetricB4`MB4Metric[], the Lovelock tensors E_(1..3) are those of
   Revision/metric_b4/results/metric-b4.json (equal to the author's stored outputs, verify_metric_b4.wls), the
   gammas are the author's T16 of Revision/algebra/gammas.json (RevisionFieldTheory.wl loader).

   Checks:
     D1  sqrt|det g| = b4^(3/2) Cos[z]; proper extra-time volume E^(-3 a4) b4^(3/2) Sin[z]^(1/2).
     D2  the conservation identities of a diagonal T(x4, x0) from the metric's own Christoffel symbols:
         nabla_mu T^mu_x4 = -d4 rho - 3 a4' (p3 - pt) - (3/2)(b4'/b4)(rho + pt); nabla_mu T^mu_x0 has no b4.
     D3  w_eff = -1 - (1/3) d ln rho_4/d ln a for rho_4 ~ E E^(-3 A) (E^(-3 A) B^(3/2))^(-s) with
         dE/dA = -3 X - (3/2)(B'/B) Pt: w_eff = X/E - s + (beta/2)(Pt/E + s).
     D4  the condensate with the author's T16: A = -gamma^(x4) (M - 3 H gamma^(x0)) - (3/4) u I16 gives
         C A + A^T C = -(3/2) u C (b4^(3/2) S constant) and (C g4 A - A^T C g4)/2 = M C.
     D5  the kinetic gas of free modes (omega^2 = M^2 + k^2 E^(-2A) - q^2 E^(2A)/B, density ~ B^(-3/2)) satisfies the
         b4 conservation identity.
     D6  the author's weights (w1 = 1, w2 = 1/32, w3 = 1/1152, Lambda = 10): on a4 = H x4 + a0 with b4 = c E^(be H x4)
         the (x4, x0) component of -Lambda delta + sum_k w_k E_(k)/H^(2k) vanishes exactly for be = 0 and be = 4/3.
     D7  on a4 = H x4, b4 = c E^((4/3) H x4) that left-hand side (= kappa T^mu_nu) is diagonal and constant:
         kappa (rho, p3, p_t, p0) = (-2/27, -2/9, -22/27, -14/27), as Revision/dark_sector/dirac16complex00/eos-theory.json
         (condensate.branchRequiredSource) records from the record of the a4 equations.
     D8  on that history the condensate's lambda S/m falls like E^(-2 a4) and its ratio has wa = 4 u/(2 + u)^2.
   Writes Revision/dark_sector/reports/wolfram-dark-sector-b4.json (UTF-8, LF, no time stamps).  Exit 0 iff all pass.
   Usage (repository root): wolframscript -file Revision/dark_sector/wolfram/verify_dark_sector_b4.wls *)

$here = DirectoryName[$InputFileName];
$rev = ExpandFileName[FileNameJoin[{$here, "..", ".."}]];
$out = FileNameJoin[{$rev, "dark_sector", "reports", "wolfram-dark-sector-b4.json"}];
Get[FileNameJoin[{$rev, "metric_b4", "wolfram", "MetricB4.wl"}]];
If[! ValueQ[MetricB4`MB4Coordinates], Print["ERROR  MetricB4.wl did not load"]; Exit[1]];
If[Get[FileNameJoin[{$rev, "theory", "wolfram", "RevisionFieldTheory.wl"}]] === $Failed, Print["ERROR  RevisionFieldTheory.wl"]; Exit[1]];
rftLoadFixture[FileNameJoin[{$rev, "algebra", "gammas.json"}]];
mb = Import[FileNameJoin[{$rev, "metric_b4", "results", "metric-b4.json"}], "RawJSON"];
If[! AssociationQ[mb], Print["ERROR  metric-b4.json not readable"]; Exit[1]];
eos00 = Import[FileNameJoin[{$rev, "dark_sector", "dirac16complex00", "eos-theory.json"}], "RawJSON"];
checks = {};
check[name_, ok_, detail_] := (AppendTo[checks, <|"name" -> name, "verdict" -> If[TrueQ[ok], "PASS", "FAIL"], "detail" -> detail|>];
  Print[If[TrueQ[ok], "PASS  ", "FAIL  "], name]);

Hs = MetricB4`H; x4s = MetricB4`x4; x0s = MetricB4`x0; a4f = MetricB4`a4; b4f = MetricB4`b4;
X = MetricB4`MB4Coordinates; z = 6 Hs x0s;
asm = Hs > 0 && 0 < z < Pi/2 && b4f[x4s] > 0 && Element[a4f[x4s], Reals];
g = MetricB4`MB4Metric[];
gi = Inverse[g];

(* D1 *)
sqrtg = Simplify[Sqrt[Abs[Det[g]]], asm];
volt = Simplify[Sqrt[Abs[g[[6, 6]] g[[7, 7]] g[[8, 8]]]], asm];
check["D1_volume_b4", Simplify[sqrtg - b4f[x4s]^(3/2) Cos[z], asm] === 0 &&
   Simplify[volt - E^(-3 a4f[x4s]) b4f[x4s]^(3/2) Sin[z]^(1/2), asm] === 0,
  "sqrt|det g| = " <> ToString[InputForm[sqrtg]] <> "; proper extra-time volume element " <> ToString[InputForm[volt]]];

(* D2 *)
Gm = Table[(1/2) Sum[gi[[l, r]] (D[g[[r, n]], X[[m]]] + D[g[[r, m]], X[[n]]] - D[g[[m, n]], X[[r]]]), {r, 8}], {l, 8}, {m, 8}, {n, 8}];
T = DiagonalMatrix[{p0[x4s, x0s], p3[x4s, x0s], p3[x4s, x0s], p3[x4s, x0s], -rho[x4s, x0s], pt[x4s, x0s], pt[x4s, x0s], pt[x4s, x0s]}];
div = Table[Sum[D[T[[m, nu]], X[[m]]], {m, 8}] + Sum[Gm[[m, m, l]] T[[l, nu]], {m, 8}, {l, 8}] - Sum[Gm[[l, m, nu]] T[[m, l]], {m, 8}, {l, 8}], {nu, 8}];
exp4 = -D[rho[x4s, x0s], x4s] - 3 a4f'[x4s] (p3[x4s, x0s] - pt[x4s, x0s]) - (3/2) (b4f'[x4s]/b4f[x4s]) (rho[x4s, x0s] + pt[x4s, x0s]);
exp0 = D[p0[x4s, x0s], x0s] + 3 Hs Cot[z] (2 p0[x4s, x0s] - p3[x4s, x0s] - pt[x4s, x0s]);
check["D2_conservation_b4", Simplify[div[[5]] - exp4, asm] === 0 && Simplify[div[[1]] - exp0, asm] === 0 &&
   FreeQ[div[[1]], b4f] && AllTrue[div[[{2, 3, 4, 6, 7, 8}]], Simplify[#, asm] === 0 &],
  "nabla_mu T^mu_x4 = -d4 rho - 3 a4' (p3 - p_t) - (3/2)(b4'/b4)(rho + p_t); nabla_mu T^mu_x0 = d0 p0 + 3 H Cot[z] (2 p0 - p3 - p_t) (no b4); the other components vanish"];

(* D3 *)
Clear[Ef, Bf];
rho4 = Ef[A] E^(-3 A) (E^(-3 A) Bf[A]^(3/2))^(-s);
wq = -1 - (1/3) D[Log[rho4], A] /. Ef'[A] -> -3 Xs - (3/2) (Bf'[A]/Bf[A]) Pts;
wq = Simplify[wq /. Bf'[A] -> beta Bf[A] /. Ef[A] -> Es, Bf[A] > 0 && Es > 0];
check["D3_w_eff_general_b4", Simplify[wq - (Xs/Es - s + (beta/2) (Pts/Es + s))] === 0,
  "w_eff = " <> ToString[InputForm[wq]] <> " = X/E - s + (beta/2)(Pt/E + s): A, B (s = 0), C (s = 1)"];

(* D4: the author's T16 in the order x0..x7 (positions 1..8) *)
gm = rftGam; C4 = gm[[1]] . gm[[2]] . gm[[3]] . gm[[4]]; I16 = IdentityMatrix[16];
Am = -gm[[5]] . (Mm I16 - 3 Hs gm[[1]]) - (3/4) u I16;
lhsS = Expand[C4 . Am + Transpose[Am] . C4 + (3/2) u C4];
K4 = Expand[(C4 . gm[[5]] . Am - Transpose[Am] . C4 . gm[[5]])/2 - Mm C4];
check["D4_condensate_b4_T16", AllTrue[Flatten[lhsS], # === 0 &] && AllTrue[Flatten[K4], # === 0 &],
  "A = -gamma^(x4) (M - 3 H gamma^(x0)) - (3/4)(b4'/b4) I16 with the author's T16: C A + A^T C = -(3/2)(b4'/b4) C, so b4^(3/2) S is constant; (C g4 A - A^T C g4)/2 = M C (K_x4 = M S)"];

(* D5 *)
om = Sqrt[Mm^2 + k^2 E^(-2 A) - q^2 E^(2 A)/Bf[A]]; nn = Bf[A]^(-3/2);
rg = nn om; p3g = nn k^2 E^(-2 A)/(3 om); ptg = -nn q^2 E^(2 A)/(Bf[A] 3 om);
check["D5_kinetic_gas_b4", Simplify[D[rg, A] + 3 (p3g - ptg) + (3/2) (Bf'[A]/Bf[A]) (rg + ptg), Bf[A] > 0] === 0,
  "free modes, omega^2 = M^2 + k^2 E^(-2 a4) - q^2 E^(2 a4)/b4, density ~ b4^(-3/2): d rho/d a4 = -3 (p3 - p_t) - (3/2)(d ln b4/d a4)(rho + p_t) exactly"];

(* the author's left-hand side -Lambda delta + sum_k w_k E_(k)/H^(2k) (= kappa T^mu_nu) from metric-b4.json *)
toE[s_] := Block[{$Context = "MetricB4`", $ContextPath = {"MetricB4`", "System`"}}, ToExpression[s]];
lab = {"x0", "x1", "x2", "x3", "x4", "x5", "x6", "x7"};
Ek[kk_] := Table[With[{v = mb["E" <> ToString[kk] <> "Mixed"][lab[[h]] <> "," <> lab[[j]]]}, If[MissingQ[v], 0, toE[v]]], {h, 8}, {j, 8}];
lhsA = -10 IdentityMatrix[8] + Ek[1]/Hs^2 + (1/32) Ek[2]/Hs^4 + (1/1152) Ek[3]/Hs^6;

(* D6 *)
mixed = Simplify[lhsA[[5, 1]] /. {a4f -> (Hs # + a0 &), b4f -> (cB Exp[be Hs #] &)}, Hs > 0 && cB > 0 && 0 < z < Pi/2];
roots = Sort[be /. Solve[mixed == 0, be, Reals]];
check["D6_author_weights_branch", roots === {0, 4/3},
  "the (x4, x0) component of the author's left-hand side on a4 = H x4 + a0, b4 = c E^(be H x4) is " <> ToString[InputForm[Factor[mixed]]] <>
  "; it vanishes for be in " <> ToString[roots] <> ": a source without T^x4_x0 allows a constant b4 or d ln b4/d a4 = 4/3"];

(* D7 *)
onBr = Simplify[lhsA /. {a4f -> (Hs # &), b4f -> (cB Exp[(4/3) Hs #] &)}, Hs > 0 && cB > 0 && 0 < z < Pi/2];
offd = DeleteCases[Flatten[Table[If[h != j, onBr[[h, j]], 0], {h, 8}, {j, 8}]], 0];
vals = {-onBr[[5, 5]], onBr[[2, 2]], onBr[[6, 6]], onBr[[1, 1]]};
rec = eos00["condensate"]["branchRequiredSource"];
recv = ToExpression /@ {rec["kappa_rho"], rec["kappa_p3"], rec["kappa_pt"], rec["kappa_p0"]};
check["D7_branch_required_source", offd === {} && vals === {-2/27, -2/9, -22/27, -14/27} && vals === recv &&
   onBr[[3, 3]] === onBr[[2, 2]] && onBr[[7, 7]] === onBr[[6, 6]],
  "on a4 = H x4, b4 = c E^((4/3) H x4) the author's left-hand side kappa T^mu_nu is diagonal and constant: kappa (rho, p3, p_t, p0) = " <>
  ToString[InputForm[vals]] <> ", equal to dirac16complex00/eos-theory.json (condensate.branchRequiredSource) " <> ToString[InputForm[recv]]];

(* D8 *)
uu = u0 E^(-2 A);
wr = uu/(2 + uu);
check["D8_condensate_drift", Simplify[(cB E^((4/3) A))^(-3/2) - cB^(-3/2) E^(-2 A), cB > 0 && Element[A, Reals]] === 0 &&
   Simplify[-D[wr, A] - 4 uu/(2 + uu)^2] === 0,
  "S ~ b4^(-3/2) = b4(0)^(-3/2) E^(-2 a4) on the history, so u = lambda S/m = u0 E^(-2 a4) and the ratio u/(2 + u) has wa = -d/da4 = 4 u/(2 + u)^2"];

failed = Count[checks, c_ /; c["verdict"] =!= "PASS"];
out = <|"producer" -> "Revision/dark_sector/wolfram/verify_dark_sector_b4.wls",
   "metric" -> "the author's metric with b4[x4] (In[97]-In[102] of Dirac_Einstein-Lovelock_4+4_Nash.nb); b4 is a function of x4",
   "history" -> "a4 = H x4, b4 = b4(0) E^((4/3) H x4) (the branch of the author's weights for a source without T^x4_x0)",
   "checks" -> checks, "checkCount" -> Length[checks], "failedCount" -> failed|>;
s = ExportString[out, "JSON", "Compact" -> False];
If[! DirectoryQ[DirectoryName[$out]], CreateDirectory[DirectoryName[$out]]];
(* ExportString returns the UTF-8 bytes as characters: write them as they are *)
If[Quiet[BinaryWrite[$out, ByteArray[ToCharacterCode[StringReplace[s, "\r\n" -> "\n"] <> "\n"]]]] === $Failed, Print["ERROR  cannot write ", $out]; Exit[1]];
Close[$out];
Print[Length[checks] - failed, "/", Length[checks], " checks passed"];
Exit[If[failed == 0, 0, 1]];
