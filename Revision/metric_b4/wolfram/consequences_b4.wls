#!/usr/bin/env wolframscript
(* ::Package:: *)

(* consequences_b4.wls

   The pairing theorems and the dark-sector volume factor in the user's metric of 2026-10-14 (b4[x4] in the extra-time
   components).  Uses the Revision field-theory package (Revision/theory/wolfram/RevisionFieldTheory.wl) and the author's
   T16 (Revision/algebra/gammas.json).  Exact checks:
     P1  T1 (chirality pairing, Revision/pairing/pairing-theory.json: "any gravitational field"): for the metric with b4,
         {Gamma, gamma^mu} = 0 and [Gamma, Omega_mu] = 0 for every mu, so gamma^mu D_mu (Gamma Psi) = -Gamma gamma^mu D_mu Psi
         for every Psi: Gamma maps a solution with (m, U') to one with (-m, -U'); the theorem holds unchanged.
     P2  T2 (mirror pairing) uses the isometry phi: x0 -> pi/(6H) - x0 (z -> pi - z) of the primordial field; the metric
         with b4 is invariant under phi (b4 depends on x4 only), so the Z2 mirror construction holds unchanged.
     P3  T3 (Kohn-Sham level) is a statement about the good-sector Kohn-Sham problem, which does not depend on b4
         (Revision/kohn_sham/reports/ks-b4-wolfram.json, check K2): unchanged.
     P4  dark sector: the proper volume element of the 7 dimensions other than x4 is sqrt|g| = b4^(3/2) cos z (constant in
         x4 iff b4 is); a 3-space observer's effective 4-dimensional density carries the proper extra-time volume factor
         c^3 with c = e^(-a4) b4^(1/2) (instead of e^(-a4)); on the background of the record (b4 = 1) every recorded
         equation of state is unchanged.
   Coordinates: the author's x0..x7 (x0 = the hidden direction, Wolfram position 1; x4 = position 5; x5 = position 6).
   Writes Revision/metric_b4/results/consequences-b4.json; exit 0 iff all pass.
   Usage (repository root): wolframscript -file Revision/metric_b4/wolfram/consequences_b4.wls *)

$here = DirectoryName[$InputFileName];
$revDir = ExpandFileName[FileNameJoin[{$here, "..", ".."}]];
If[Get[FileNameJoin[{$revDir, "theory", "wolfram", "RevisionFieldTheory.wl"}]] === $Failed, Print["ERROR  RevisionFieldTheory.wl: Get failed"]; Exit[1]];
rftLoadFixture[FileNameJoin[{$revDir, "algebra", "gammas.json"}]];
checks = {};
addCheck[name_String, ok_, detail_String] := (AppendTo[checks, <|"name" -> name, "verdict" -> If[TrueQ[ok], "PASS", "FAIL"], "detail" -> detail|>];
  Print[If[TrueQ[ok], "PASS  ", "FAIL  "], name]);
g = rftGam; Gch = rftChir; X = rftX;
fB = {Cot[rftZ], E^a4[x4] Sin[rftZ]^(1/6), E^a4[x4] Sin[rftZ]^(1/6), E^a4[x4] Sin[rftZ]^(1/6), 1,
   E^(-a4[x4]) Sqrt[b4[x4]] Sin[rftZ]^(1/6), E^(-a4[x4]) Sqrt[b4[x4]] Sin[rftZ]^(1/6), E^(-a4[x4]) Sqrt[b4[x4]] Sin[rftZ]^(1/6)};
e0 = DiagonalMatrix[fB]; ei = DiagonalMatrix[1/fB];
g0 = Transpose[e0] . rftEta . e0; gi = Inverse[g0];
Gm = rftChristoffel[g0, gi]; Om = rftSpinorConnection[rftLower[rftOmegaMixed[e0, ei, Gm]]]; gup = rftGammaUp[ei];
geo = <|"sqrtg" -> b4[x4]^(3/2) Cos[rftZ], "gup" -> gup, "Om" -> Om|>;
Xf = Table[ph[A] @@ X, {A, 16}];
addCheck["P1_T1_chirality_pairing_with_b4",
  And @@ Table[rftZeroQ[Gch . gup[[mu]] + gup[[mu]] . Gch] && rftZeroQ[Gch . Om[[mu]] - Om[[mu]] . Gch], {mu, 8}] &&
   rftZeroQ[rftDirac["C", geo, Gch . Xf] + Gch . rftDirac["C", geo, Xf]],
  "metric with b4: {Gamma, gamma^mu} = 0, [Gamma, Omega_mu] = 0 for every mu and gamma^mu D_mu (Gamma Psi) = -Gamma gamma^mu D_mu Psi for a general 16-component Psi: T1 holds unchanged (its hypothesis 'any gravitational field' covers the metric with b4)"];
gB = DiagonalMatrix[{Cot[6 H x0]^2, E^(2 a4[x4]) Sin[6 H x0]^(1/3), E^(2 a4[x4]) Sin[6 H x0]^(1/3), E^(2 a4[x4]) Sin[6 H x0]^(1/3), -1,
   -E^(-2 a4[x4]) b4[x4] Sin[6 H x0]^(1/3), -E^(-2 a4[x4]) b4[x4] Sin[6 H x0]^(1/3), -E^(-2 a4[x4]) b4[x4] Sin[6 H x0]^(1/3)}];
jac = DiagonalMatrix[{-1, 1, 1, 1, 1, 1, 1, 1}];   (* d phi: x0 -> pi/(6H) - x0 reverses the x0 direction *)
gPull = jac . (gB /. x0 -> Pi/(6 H) - x0) . jac;
addCheck["P2_T2_mirror_isometry_with_b4",
  And @@ (Simplify[#] === 0 & /@ Flatten[gPull - gB]),
  "the map phi: x0 -> pi/(6H) - x0 (z -> pi - z) pulls the metric with b4 back to itself (Sin and Cot^2 are symmetric under z -> pi - z, b4 depends on x4 only): the Z2 mirror of T2 is an isometry for every b4"];
ksb4 = Import[FileNameJoin[{$revDir, "kohn_sham", "reports", "ks-b4-wolfram.json"}], "RawJSON"];
addCheck["P3_T3_kohn_sham_level",
  AssociationQ[ksb4] && ksb4["verdict"] === "PASS" && MemberQ[#["name"] & /@ ksb4["checks"], "K2_good_sector_independent_of_b4"],
  "T3 concerns the good-sector Kohn-Sham problem, whose levels and orbitals are independent of b4 (Revision/kohn_sham/reports/ks-b4-wolfram.json, K2 PASS): T3 holds unchanged"];
vol7 = Simplify[Sqrt[Abs[Det[gB]]], {H > 0, 0 < 6 H x0 < Pi/2, b4[x4] > 0}];
extraScale = Simplify[Sqrt[-gB[[6, 6]]]/Sin[6 H x0]^(1/6), {b4[x4] > 0, 0 < 6 H x0 < Pi/2, Element[a4[x4], Reals]}];   (* x5 *)
addCheck["P4_dark_sector_volume_factor",
  Simplify[vol7 - b4[x4]^(3/2) Cos[6 H x0], {H > 0, 0 < 6 H x0 < Pi/2, b4[x4] > 0}] === 0 &&
   Simplify[extraScale - E^(-a4[x4]) Sqrt[b4[x4]], {b4[x4] > 0, Element[a4[x4], Reals]}] === 0,
  "sqrt|det g| = b4^(3/2) cos z and the extra-time scale factor (without the warp) is c = e^(-a4) b4^(1/2): the effective 4-dimensional density of a 3-space observer carries c^3 = e^(-3 a4) b4^(3/2); at b4 = 1 (the background of the record) it is e^(-3 a4) as recorded"];
failed = Count[checks, c_ /; c["verdict"] =!= "PASS"];
out = FileNameJoin[{$revDir, "metric_b4", "results", "consequences-b4.json"}];
s = ExportString[<|"producer" -> "Revision/metric_b4/wolfram/consequences_b4.wls", "checkCount" -> Length[checks], "failedCount" -> failed,
   "verdict" -> If[failed == 0, "PASS", "FAIL"], "checks" -> checks|>, "JSON", "Compact" -> False];
If[Quiet[BinaryWrite[out, StringToByteArray[s <> "\n", "UTF-8"]]] === $Failed, Print["ERROR  cannot write ", out]; Exit[1]];
Close[out];
Print[Length[checks] - failed, "/", Length[checks], " checks passed"];
Exit[If[failed == 0, 0, 1]];
