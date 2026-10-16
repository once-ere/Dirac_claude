#!/usr/bin/env wolframscript
(* ::Package:: *)

(* verify_field_theory.wls

   Driver for Revision/theory/wolfram/RevisionFieldTheory.wl (Revision/SPEC.md, sections 1-4 and 6) for THE WARPED
   METRIC of 2026-10-16 (the user's order: "find the simplest modification for the current metric of the primordial
   gravitational field that is probably self-consistent with the Einstein field equations"; Revision/metric_warped/):
     g = diag(Cot[z]^2, E^(2 a4) Sin[z]^(1/3) (x3), -Sin[z]^(1/3), -E^(-2 a4) b4 Sin[z]^(1/3) (x3)),  z = 6 H x0,
   in the author's coordinates x0..x7 (x0 = the hidden direction, Wolfram position 1; x4 = the time, position 5).
   Every statement is proved for GENERAL functions a4(x4) and b4(x4) > 0.  Until 2026-10-16 this script proved the
   statements for the metric of 2026-10-14 (g44 = -1, withdrawn), until 2026-10-15 for b4 = 1 (withdrawn).

   The script runs in PARTS, each one a separate wolframscript call that stays well below the limit of 7 min 3 s
   for one calculation (the user's order); the parts write their results to the git-ignored folder
   build/theory-wolfram/ and the part "merge" assembles the two committed outputs:
     Revision/theory/reports/wolfram-field-theory.json   every check with name, verdict, detail
     Revision/theory/field-theory.json                   the exact formulas for the documents
   (LF line endings, no time stamps).  Usage, from the repository root, in this order:
     wolframscript -file Revision/theory/wolfram/verify_field_theory.wls base
     wolframscript -file Revision/theory/wolfram/verify_field_theory.wls emt-G
     wolframscript -file Revision/theory/wolfram/verify_field_theory.wls emt-C
     wolframscript -file Revision/theory/wolfram/verify_field_theory.wls solutions
     wolframscript -file Revision/theory/wolfram/verify_field_theory.wls solutions-G
     wolframscript -file Revision/theory/wolfram/verify_field_theory.wls quantisation
     wolframscript -file Revision/theory/wolfram/verify_field_theory.wls merge
   Every part file records the sha256 of this script, the package, the fixture and warped-metric.json; "merge" refuses
   (exit code 1) a part file written by a different version of any of them, and a missing part.
   Every check is exact symbolic algebra (no floating point).  Both statistics are treated:
   "G" = dirac16complex (explicit Grassmann algebra, N = 2 generators theta_1, theta_2 and their
   conjugates), "C" = dirac16complex00 (commuting complex components).  Exit code 0 if every check
   of the part passes, 1 otherwise; 2 for a wrong argument or an output that cannot be written.
*)

$here = DirectoryName[$InputFileName];
$theoryDir = ExpandFileName[FileNameJoin[{$here, ".."}]];
$revDir = ExpandFileName[FileNameJoin[{$theoryDir, ".."}]];
$repoDir = ExpandFileName[FileNameJoin[{$revDir, ".."}]];
$partDir = FileNameJoin[{$repoDir, "build", "theory-wolfram"}];
$parts = {"base", "emt-G", "emt-C", "solutions", "solutions-G", "quantisation"};
part = If[Length[$ScriptCommandLine] > 1, $ScriptCommandLine[[2]], ""];
If[!MemberQ[Append[$parts, "merge"], part],
  Print["usage: wolframscript -file Revision/theory/wolfram/verify_field_theory.wls <part>, part = ", StringRiffle[Append[$parts, "merge"], " | "]]; Exit[2]];
pkgFile = FileNameJoin[{$here, "RevisionFieldTheory.wl"}];
fixFile = FileNameJoin[{$revDir, "algebra", "gammas.json"}];
mwFile = FileNameJoin[{$revDir, "metric_warped", "results", "warped-metric.json"}];
sha[file_] := FileHash[file, "SHA256", All, "HexString"];
inputHashes = <|"script" -> sha[$InputFileName], "package" -> sha[pkgFile], "fixture" -> sha[fixFile], "metric_warped" -> sha[mwFile]|>;

jstr[s_String] := "\"" <> StringReplace[s, {"\\" -> "\\\\", "\"" -> "\\\"", "\n" -> "\\n"}] <> "\"";
writeLF[path_, text_String] := Module[{s = Quiet[OpenWrite[path, BinaryFormat -> True, CharacterEncoding -> "UTF-8"]]},
  If[Head[s] =!= OutputStream, Print["cannot write ", path]; Exit[2]]; BinaryWrite[s, ToCharacterCode[text, "UTF-8"]]; Close[s]];
checkLine[c_] := "    {\"name\": " <> jstr[c["name"]] <> ", \"verdict\": " <> jstr[c["verdict"]] <> ", \"detail\": " <> jstr[c["detail"]] <> "}";
fjson[fm_] := Module[{w = fm["wl"]},
  "    {\"key\": " <> jstr[fm["key"]] <> ", \"description\": " <> jstr[fm["description"]] <> ", \"wl\": " <>
  If[ListQ[w], "[\n" <> StringRiffle[("      " <> jstr[#]) & /@ w, ",\n"] <> "\n    ]", jstr[w]] <> "}"];

(* ================================================================== merge *)
If[part === "merge",
  Module[{data, bad = {}, checks, formulas, cons, nPass, nTot, report, formulaText, pick},
    data = Association[Table[p -> Module[{f = FileNameJoin[{$partDir, p <> ".json"}]},
       If[FileExistsQ[f], Import[f, "RawJSON"], Missing[]]], {p, $parts}]];
    Do[Which[MissingQ[data[p]], AppendTo[bad, p <> ": missing (run the part first)"],
        data[p]["inputs"] =!= inputHashes, AppendTo[bad, p <> ": written by a different version of the script, package, fixture or warped-metric.json; run it again"]], {p, $parts}];
    If[bad =!= {}, Print["ERROR  ", #] & /@ bad; Exit[1]];
    checks = Join @@ Table[data[p]["checks"], {p, $parts}];
    pick[n_] := Lookup[First[Select[checks, #["name"] == n &], <|"verdict" -> "FAIL"|>], "verdict"];
    cons = <|"name" -> "conservation_on_shell_general",
      "verdict" -> If[And @@ Table[pick[n] == "PASS", {n, Flatten[Table[{"Noether_identity_diffeomorphisms_" <> st, "Noether_identity_local_Lorentz_" <> st, "T_symmetric_part_Belinfante_" <> st}, {st, {"G", "C"}}]]}], "PASS", "FAIL"],
      "detail" -> ("consequence for both statistics (from the six checks Noether_identity_diffeomorphisms_*, Noether_identity_local_Lorentz_*, T_symmetric_part_Belinfante_*, for general a4 and b4): " <>
        "on shell (all EL_phi = 0) T^mu_nu = T_sym^mu_nu is symmetric and d_mu(sqrt g T^mu_lambda) - sqrt g T^mu_a d_lambda e^a_mu = 0, " <>
        "which for symmetric T is sqrt g nabla_mu T^mu_lambda = 0 (Gamma^r_mu,lambda T^mu_r = (1/2) d_lambda g_mu,r T^mu r = T^mu_a d_lambda e^a_mu): exact conservation for general solutions")|>;
    checks = Join[data["base"]["checks"], data["emt-G"]["checks"], data["emt-C"]["checks"], {cons}, data["solutions"]["checks"],
      data["solutions-G"]["checks"], data["quantisation"]["checks"]];
    formulas = Join @@ Table[data[p]["formulas"], {p, $parts}];
    nPass = Count[checks, c_ /; c["verdict"] == "PASS"]; nTot = Length[checks];
    report = StringJoin[
      "{\n",
      "  \"report\": ", jstr["Revision field theory (SPEC sections 1-4, 6) for the warped metric of 2026-10-16 (general a4 and b4): vielbein, canonical spin connection, Lagrangian, Euler-Lagrange equations, non-triviality [1] and [2], current, energy-momentum tensor, exact solutions, canonical quantisation; both statistics, verified exactly in WolframScript"], ",\n",
      "  \"producer\": ", jstr["Revision/theory/wolfram/verify_field_theory.wls (parts base, emt-G, emt-C, solutions, solutions-G, quantisation; merge)"], ",\n",
      "  \"package\": ", jstr["Revision/theory/wolfram/RevisionFieldTheory.wl"], ",\n",
      "  \"fixture\": ", jstr["Revision/algebra/gammas.json"], ",\n",
      "  \"metric\": ", jstr["g = diag(Cot[z]^2, E^(2 a4[x4]) Sin[z]^(1/3) (3 times), -Sin[z]^(1/3), -E^(-2 a4[x4]) b4[x4] Sin[z]^(1/3) (3 times)), z = 6 H x0, b4[x4] > 0 and a4[x4] general functions of x4 (Revision/SPEC.md section 1; the warped metric of 2026-10-16)"], ",\n",
      "  \"statistics\": ", jstr["G = dirac16complex: 16 complex anticommuting components, explicit Grassmann algebra with generators theta_1, theta_2 and their conjugates; C = dirac16complex00: 16 complex commuting components"], ",\n",
      "  \"coordinates\": ", jstr["the author's coordinates x0..x7: x0 = the hidden direction; x1, x2, x3 = 3-space; x4 = time; x5, x6, x7 = the exponentially deflating extra times; z = 6 H x0 in (0, Pi/2), H > 0"], ",\n",
      "  \"summary\": {\"passed\": ", ToString[nPass], ", \"failed\": ", ToString[nTot - nPass], ", \"total\": ", ToString[nTot], "},\n",
      "  \"checks\": [\n", StringRiffle[checkLine /@ checks, ",\n"], "\n  ]\n}\n"];
    formulaText = StringJoin[
      "{\n",
      "  \"description\": ", jstr["Exact formulas of the Revision field theory (SPEC sections 1-4, 6) for the warped primordial metric of 2026-10-16 (general a4 and b4), for the documents. Every formula is verified by a named check of Revision/theory/reports/wolfram-field-theory.json. Wolfram InputForm; g[xa] = gamma^(xa) of Revision/algebra/gammas.json; a4' = Derivative[1][a4][x4]; b4' = Derivative[1][b4][x4]; z = 6 H x0; Psibar = Psi^dagger C; S = Psibar Psi; V = m + U'(S); both statistics unless stated."], ",\n",
      "  \"producer\": ", jstr["Revision/theory/wolfram/verify_field_theory.wls"], ",\n",
      "  \"formulas\": [\n", StringRiffle[fjson /@ formulas, ",\n"], "\n  ]\n}\n"];
    If[!DirectoryQ[FileNameJoin[{$theoryDir, "reports"}]], CreateDirectory[FileNameJoin[{$theoryDir, "reports"}]]];
    writeLF[FileNameJoin[{$theoryDir, "reports", "wolfram-field-theory.json"}], report];
    writeLF[FileNameJoin[{$theoryDir, "field-theory.json"}], formulaText];
    Print["merge: ", nPass, "/", nTot, " checks passed"];
    Exit[If[nPass == nTot, 0, 1]]]];

(* ================================================================== the parts: common set-up *)
Get[pkgFile];
rftLoadFixture[fixFile];
(* Parallel evaluation (2026-10-14) in the parts emt-G, emt-C, solutions and solutions-G: every test expression is built on the main
   kernel, and only the zero test itself (rftZeroQ / gZeroQ / zeroQK, the same functions) runs on a subkernel.  Every
   subkernel loads the same package and fixture; nothing is distributed implicitly ($DistributedContexts = None): the
   data of a test travels inside the test expression.  The environment variable RFT_KERNELS sets the number of
   subkernels (0 = everything serial on the main kernel). *)
$rftNK = If[MemberQ[{"emt-G", "emt-C", "solutions", "solutions-G"}, part],
  With[{e = Environment["RFT_KERNELS"]}, If[StringQ[e] && StringMatchQ[e, DigitCharacter ..], ToExpression[e], Min[16, Max[0, $ProcessorCount - 4]]]], 0];
$DistributedContexts = None;
If[$rftNK > 0,
  If[Length[LaunchKernels[$rftNK]] =!= $rftNK, Print["ERROR  could not launch ", $rftNK, " subkernels (set RFT_KERNELS=0 to run serially)"]; Exit[1]];
  With[{pkg = pkgFile, fx = fixFile}, ParallelEvaluate[Block[{Print}, Get[pkg]]; rftLoadFixture[fx]; Null]]];
Print["part ", part, "; subkernels: ", $rftNK];
pZeroQ[test_, l_List] := If[$rftNK > 0, ParallelMap[test, l, Method -> "FinestGrained"], test /@ l];
pS[st_String, l_List] := pZeroQ[With[{s = st}, sZeroQ[s, #] &], l];

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
stats = Switch[part, "emt-G", {"G"}, "emt-C", {"C"}, _, {"G", "C"}];
g = rftGam; eta = rftEta; id16 = rftI16; z16 = rftZ16; Cm = rftC; Bm = rftB;
X = rftX; f = rftF; sg = rftSqrtG0;
a4p = Derivative[1][a4][x4];
bu = Derivative[1][b4][x4]/b4[x4];      (* b4'/b4 *)
bpp = Derivative[2][b4][x4]/b4[x4];     (* b4''/b4 *)
(* Wolfram positions of the author's coordinates x0..x7: position k + 1 holds xk, so x0 (hidden) = 1, x4 (time) = 5,
   3-space x1, x2, x3 = 2, 3, 4 and the extra times x5, x6, x7 = 6, 7, 8 *)
section["geometry (package functions)"];
rftBuildGeometry[];
Gm = rftGamma0; omMix = rftOmegaMix0; omLow = rftOmegaLow0; Om = rftOm0; gup = rftGup0;
fld = Association[Table[st -> <|"Psi" -> rftField[st], "Psic" -> rftFieldC[st]|>, {st, stats}]];
lagData[sts_] := Association[Table[st -> Module[{P = fld[st]["Psi"], Pc = fld[st]["Psic"]},
  <|"L0" -> rftL0[st, rftGeo0, P, Pc], "L" -> rftLag[st, rftGeo0, P, Pc], "Lu" -> rftLagUnsym[st, rftGeo0, P, Pc],
    "E" -> rftE[st, rftGeo0, P, Pc], "Ebar" -> rftEbar[st, rftGeo0, P, Pc], "S" -> rftSbil[st, P, Pc]|>], {st, sts}]];
(* the Euler-Lagrange expressions of every component function (needed by the parts base, emt-G and emt-C) *)
ELc = <||>; ELp = <||>;
computeEL[st_] := Module[{L = Ldata[st]["L"]},
  If[st === "C",
    Do[ELc[{st, A}] = rftVarDer[st, L, phc[A]]; ELp[{st, A}] = rftVarDer[st, L, ph[A]], {A, 16}],
    Do[ELc[{st, A, k}] = rftVarDer[st, L, phc[A, k]]; ELp[{st, A, k}] = rftVarDer[st, L, ph[A, k]], {A, 16}, {k, rftGN}]]];
bilM[st_, Pc_, M_, P_] := sDot[st, Pc, matVec[st, Cm . M, P]];
(* the gravitational (spin-connection) term of the Dirac operator: gamma^mu Omega_mu = (7/2) H gamma^(x0) + (3/4)(b4'/b4) Sin[z]^(-1/6) gamma^(x4) *)
wf = Sin[rftZ]^(1/6);                   (* the warp factor of every direction x1..x7, f4 = wf *)
gOm = (7/2) H g[[1]] + (3/4) bu wf^-1 g[[5]];

(* ================================================================== PART base *)
If[part === "base",
(* ------------------------------------------------------------------ the exact zero test *)
addCheck["zero_test_sanity",
  rftZeroQ[ph[1] @@ X (Sin[6 H x0]^2 + Cos[6 H x0]^2 - 1)] && !rftZeroQ[ph[1] @@ X] && !rftZeroQ[pf[x0]] &&
  rftZeroQ[U'[ph[1] @@ X phc[1] @@ X] ph[2] @@ X - ph[2] @@ X U'[phc[1] @@ X ph[1] @@ X]] && rftZeroQ[E^a4[x4] E^-a4[x4] - 1] &&
  rftZeroQ[cA[1] H - cA[1] H Cot[6 H x0] Tan[6 H x0]] && !rftZeroQ[D[ph[1] @@ X, x1] - D[ph[1] @@ X, x2]] && !rftZeroQ[H Sin[6 H x0]^(1/6) - H] &&
  !rftZeroQ[ph[1] @@ X (Sin[6 H x0]^2 + Cos[6 H x0]^2)] &&
  rftZeroQ[ph[1] @@ X (Sqrt[b4[x4]]^2 - b4[x4])] && rftZeroQ[ph[1] @@ X (b4[x4]^(3/2)/Sqrt[b4[x4]] - b4[x4])] &&
  !rftZeroQ[ph[1] @@ X (b4[x4] - 1)] && !rftZeroQ[ph[1] @@ X Derivative[1][b4][x4]],
  "the exact zero test (field functions, their derivatives and U-expressions as independent polynomial variables; coefficients reduced with Sin z = w^6, w > 0, Cos^2 = 1 - Sin^2) " <>
  "returns True on identities and False on nonzero expressions in a set of control cases; b4[x4] and its derivatives are free symbols: Sqrt[b4]^2 - b4 and b4^(3/2)/b4^(1/2) - b4 are zero, b4 - 1 and b4' are not (the test never sets b4 = 1)"];

(* ------------------------------------------------------------------ 0. fixture *)
section["fixture"];
addCheck["fixture_Clifford_relation",
  And @@ Flatten[Table[g[[a]] . g[[b]] + g[[b]] . g[[a]] == 2 eta[[a, b]] id16, {a, 8}, {b, 8}]] && rftEtaFixture == Diagonal[eta],
  "the gammas read from Revision/algebra/gammas.json satisfy {gamma^a, gamma^b} = 2 eta^ab I16 with eta = diag(1,1,1,1,-1,-1,-1,-1) (order x0..x7), as recorded in the fixture"];
addCheck["fixture_C_B_S_consistent",
  Cm == g[[1]] . g[[2]] . g[[3]] . g[[4]] && Bm == -I Cm . g[[5]] && rftChir == Dot @@ g[[{1, 2, 3, 4, 5, 6, 7, 8}]] &&
  And @@ Flatten[Table[rftS[[a, b]] == (1/4) (g[[a]] . g[[b]] - g[[b]] . g[[a]]), {a, 8}, {b, 8}]] &&
  Transpose[Cm] == Cm && Cm . Cm == id16 && And @@ Table[Transpose[Cm . g[[a]]] == -Cm . g[[a]], {a, 8}],
  "C = gamma^(x0) gamma^(x1) gamma^(x2) gamma^(x3) (real symmetric, C^2 = 1, C gamma^a antisymmetric), B = -i C gamma^(x4), Gamma = gamma^(x0) gamma^(x1)...gamma^(x7), S^ab = (1/4)[gamma^a, gamma^b], all as decoded from the fixture"];

(* ------------------------------------------------------------------ 1. geometry *)
section["geometry"];
addCheck["metric_is_the_authors",
  rftZeroQ[rftG0 - rftMetricAuthor] && rftZeroQ[Transpose[rftE0] . eta . rftE0 - rftMetricAuthor],
  "g = e^T eta e with the diagonal vielbein e^a_mu = f_a delta^a_mu, f(x0) = Cot[z], f(x1,x2,x3) = E^a4 Sin[z]^(1/6), f(x4) = Sin[z]^(1/6), f(x5,x6,x7) = E^-a4 b4^(1/2) Sin[z]^(1/6), z = 6 H x0, " <>
  "reproduces the warped metric of SPEC section 1 (g44 = -Sin[z]^(1/3), g55 = g66 = g77 = -E^(-2 a4) b4 Sin[z]^(1/3); the user's order of 2026-10-16) entry by entry, for general functions a4(x4) and b4(x4) > 0"];
addCheck["vielbein_inverse",
  rftZeroQ[rftE0 . rftEinv0 - IdentityMatrix[8]] &&
  rftZeroQ[Table[Sum[rftEinv0[[mu, a]] rftEinv0[[nu, a]] eta[[a, a]], {a, 8}] - rftGinv0[[mu, nu]], {mu, 8}, {nu, 8}]],
  "e^a_mu e_a^nu = delta and e_a^mu e_b^nu eta^ab = g^munu (inverse vielbein e_a^mu = delta_a^mu / f_a)"];
addCheck["sqrt_det_g",
  rftZeroQ[Det[rftG0] - b4[x4]^3 Cos[rftZ]^2 Sin[rftZ]^(1/3)] && Simplify[b4[x4]^(3/2) Cos[rftZ] Sin[rftZ]^(1/6) > 0, rftAssumptions] &&
  rftZeroQ[Times @@ f - b4[x4]^(3/2) Cos[rftZ] Sin[rftZ]^(1/6)] && rftZeroQ[sg - b4[x4]^(3/2) Cos[rftZ] Sin[rftZ]^(1/6)] &&
  rftZeroQ[D[sg, x4] - (3/2) bu sg] && rftZeroQ[sg/f[[5]] - b4[x4]^(3/2) Cos[rftZ]],
  "det g = b4^3 Cos[z]^2 Sin[z]^(1/3) (four negative entries), so sqrt|det g| = f0...f7 = b4^(3/2) Cos[z] Sin[z]^(1/6) > 0 on 0 < z < Pi/2; the 3-space inflation e^(3 a4) and the extra-time deflation e^(-3 a4) compensate in the volume, " <>
  "d_x4 sqrt|g| = (3/2)(b4'/b4) sqrt|g| (the volume depends on x4 through b4 alone), and the measure of a slice x4 = const divided by the lapse is sqrt|g|/f4 = b4^(3/2) Cos[z]"];
addCheck["degenerate_at_H_0",
  Limit[Sin[6 H x0]^(1/3), H -> 0] === 0 && Limit[Cot[6 H x0]^2, H -> 0, Direction -> "FromAbove", Assumptions -> x0 > 0] === Infinity,
  "at fixed x0 and H -> 0+ the entries g11 = g22 = g33 -> 0, g44 -> 0, g55 = g66 = g77 -> 0 (for every b4 > 0) and g00 -> infinity: H = 0 is not a metric of the family (a degenerate limit); every statement below assumes H > 0 and 0 < z < Pi/2"];
gamNZ = DeleteCases[Flatten[Table[{l, mm, n, rftSimp[Gm[[l, mm, n]]]}, {l, 8}, {mm, 8}, {n, mm, 8}], 2], {_, _, _, 0}];
addFormula["christoffel_nonzero", "nonzero Christoffel symbols {l, m, n, Gamma^l_mn} (m <= n; Gamma^l_nm = Gamma^l_mn), Wolfram positions 1..8 = x0..x7", gamNZ];
addCheck["christoffel_count",
  Length[gamNZ] == 27 && !FreeQ[gamNZ, Derivative[1][b4]] && rftZeroQ[Gm[[5, 1, 5]] - H Cot[rftZ]] && rftZeroQ[Gm[[1, 5, 5]] - H Sec[rftZ] Sin[rftZ]^(4/3)],
  "the Levi-Civita connection has " <> ToString[Length[gamNZ]] <> " independent nonzero symbols Gamma^l_mn (m <= n), the extra-time ones containing b4'/b4; the two symbols of the warped time direction are Gamma^x4_(x0 x4) = H Cot[z] and Gamma^x0_(x4 x4) = H Sec[z] Sin[z]^(4/3): listed in field-theory.json (christoffel_nonzero)"];
Rm = rftRiemann[Gm];
Ric = Table[Sum[Rm[[r, s, r, n]], {r, 8}], {s, 8}, {n, 8}];
RicMixed = Table[Sum[rftGinv0[[mu, s]] Ric[[s, nu]], {s, 8}], {mu, 8}, {nu, 8}];
Rs = Sum[RicMixed[[mu, mu]], {mu, 8}];
wW = Sin[rftZ]^(-1/3);                 (* W = Sin[z]^(-1/3) = 1/(the square of the warp factor) *)
RsExpected = -56 H^2 + wW (6 a4p^2 - 3 a4p bu + 3 bpp);
addCheck["ricci_scalar",
  rftZeroQ[Rs - RsExpected],
  "Ricci scalar R = g^sn R^r_srn = -56 H^2 + Sin[z]^(-1/3) (6 a4'^2 - 3 a4' b4'/b4 + 3 b4''/b4) (convention R^r_smn = d_m Gamma^r_ns - d_n Gamma^r_ms + Gamma^r_ml Gamma^l_ns - Gamma^r_nl Gamma^l_ms)"];
ricExpected = ConstantArray[0, {8, 8}];
ricExpected[[1, 1]] = -7 H^2;
Do[ricExpected[[i, i]] = -7 H^2 + wW (a4''[x4] + (3/2) a4p bu), {i, 2, 4}];
ricExpected[[5, 5]] = -7 H^2 + wW (6 a4p^2 - (3/4) bu^2 - 3 a4p bu + (3/2) bpp);
Do[ricExpected[[t, t]] = -7 H^2 + wW (-a4''[x4] + (1/4) bu^2 - (3/2) a4p bu + (1/2) bpp), {t, 6, 8}];
mw = Import[mwFile, "RawJSON"];
mwRic = DiagonalMatrix[Table[ReleaseHold[ToExpression[mw["ricci_mixed_diagonal_mathematica"][rftCoordNames[[h]]]]], {h, 8}]];
addCheck["ricci_mixed_components",
  rftZeroQ[RicMixed - ricExpected] && rftZeroQ[RicMixed - mwRic] && rftZeroQ[Rs - ReleaseHold[ToExpression[mw["ricci_scalar_mathematica"]]]],
  "R^mu_nu is diagonal (no off-diagonal component: the warped metric): R^x0_x0 = -7 H^2, R^xi_xi = -7 H^2 + Sin[z]^(-1/3) (a4'' + (3/2) a4' b4'/b4) (i = 1, 2, 3), " <>
  "R^x4_x4 = -7 H^2 + Sin[z]^(-1/3) (6 a4'^2 - (3/4)(b4'/b4)^2 - 3 a4' b4'/b4 + (3/2) b4''/b4), R^xt_xt = -7 H^2 + Sin[z]^(-1/3) (-a4'' + (1/4)(b4'/b4)^2 - (3/2) a4' b4'/b4 + (1/2) b4''/b4) (t = 5, 6, 7); " <>
  "R^mu_nu and R equal the independent sympy record Revision/metric_warped/results/warped-metric.json (ricci_mixed_diagonal_mathematica, ricci_scalar_mathematica)"];
addFormula["ricci_mixed_nonzero", "nonzero R^mu_nu as {mu, nu, value}, Wolfram positions 1..8 = x0..x7",
  DeleteCases[Flatten[Table[{mu, nu, ricExpected[[mu, nu]]}, {mu, 8}, {nu, 8}], 1], {_, _, 0}]];
addFormula["ricci_scalar", "Ricci scalar R", RsExpected];
addCheck["never_flat_for_H_positive",
  rftZeroQ[RicMixed[[1, 1]] + 7 H^2] && Simplify[-7 H^2 < 0, H > 0],
  "R^(x0)_(x0) = -7 H^2 < 0 for every H > 0 and all functions a4, b4: the metric is curved for every admissible H, whatever a4 and b4 are"];

(* ------------------------------------------------------------------ 2. spin connection *)
section["spin connection"];
addCheck["vielbein_postulate",
  rftZeroQ[Table[D[rftE0[[a, nu]], X[[mu]]] - Sum[Gm[[l, mu, nu]] rftE0[[a, l]], {l, 8}] + Sum[omMix[[mu, a, b]] rftE0[[b, nu]], {b, 8}], {mu, 8}, {a, 8}, {nu, 8}]],
  "d_mu e^a_nu - Gamma^l_mu,nu e^a_l + omega_mu^a_b e^b_nu = 0 for all 512 components, with omega_mu^a_b = e^a_nu (d_mu e_b^nu + Gamma^nu_mu,l e_b^l)"];
addCheck["omega_antisymmetric",
  rftZeroQ[Table[omLow[[mu, a, b]] + omLow[[mu, b, a]], {mu, 8}, {a, 8}, {b, 8}]],
  "omega_mu,ab = eta_ac omega_mu^c_b = -omega_mu,ba (metric compatibility)"];
omNZ = DeleteCases[Flatten[Table[{mu, a, b, rftSimp[omLow[[mu, a, b]]]}, {mu, 8}, {a, 8}, {b, a + 1, 8}], 2], {_, _, _, 0}];
(* {mu, a, b, omega_mu,ab} with a < b in Wolfram positions (x0 = 1, x4 = 5): omega_xi,(x0)(xi) = -omega_xi,(xi)(x0) *)
omExpected = Join[
  Flatten[Table[{{i, i, 5, E^a4[x4] a4p}, {i, 1, i, -H E^a4[x4] Sin[rftZ]^(1/6)}}, {i, 2, 4}], 1],
  {{5, 1, 5, H Sin[rftZ]^(1/6)}},
  Flatten[Table[{{t, 5, t, -E^(-a4[x4]) Sqrt[b4[x4]] (a4p - bu/2)}, {t, 1, t, H E^(-a4[x4]) Sqrt[b4[x4]] Sin[rftZ]^(1/6)}}, {t, 6, 8}], 1]];
addCheck["omega_components",
  Length[omNZ] == 13 && Sort[omNZ[[All, 1 ;; 3]]] == Sort[omExpected[[All, 1 ;; 3]]] &&
  And @@ Table[rftZeroQ[omLow[[Sequence @@ e[[1 ;; 3]]]] - e[[4]]], {e, omExpected}],
  "exactly 13 independent nonzero omega_mu,ab (a < b in the order x0..x7): for i = x1, x2, x3: omega_i,(i)(x4) = a4' E^a4, omega_i,(x0)(i) = -H E^a4 Sin[z]^(1/6) (i.e. omega_i,(i)(x0) = H E^a4 Sin[z]^(1/6)); " <>
  "for the time x4: omega_x4,(x0)(x4) = H Sin[z]^(1/6) (new in the warped metric: the lapse Sin[z]^(1/6) depends on x0); " <>
  "for t = x5, x6, x7: omega_t,(x4)(t) = -(a4' - b4'/(2 b4)) E^-a4 b4^(1/2), omega_t,(x0)(t) = H E^-a4 b4^(1/2) Sin[z]^(1/6) (i.e. omega_t,(t)(x0) = -H E^-a4 b4^(1/2) Sin[z]^(1/6)); omega_x0 = 0. " <>
  "Every component is a4', a4' - b4'/(2 b4) = -(d/dx4) ln(E^-a4 b4^(1/2)) or H times a nonvanishing factor"];
addFormula["omega_nonzero", "nonzero omega_mu,ab = eta_ac omega_mu^c_b as {mu, a, b, value} with a < b (omega_mu,ba = -omega_mu,ab); Wolfram positions mu, a, b = 1..8 = x0..x7", omExpected];
addCheck["Omega_components",
  rftZeroQ[Om - Table[Sum[If[e[[1]] == mu, e[[4]] (1/2) g[[e[[2]]]] . g[[e[[3]]]], 0], {e, omExpected}], {mu, 8}]] &&
  rftZeroQ[Om[[1]]] && rftZeroQ[Om[[5]] - (1/2) H wf g[[1]] . g[[5]]],
  "Omega_mu = (1/2) omega_mu,ab S^ab = sum_(a<b) omega_mu,ab (1/2) gamma^a gamma^b: Omega_xi = (1/2) E^a4 (a4' gamma^(xi) gamma^(x4) + H Sin[z]^(1/6) gamma^(xi) gamma^(x0)) for i = 1, 2, 3; " <>
  "Omega_x4 = (1/2) H Sin[z]^(1/6) gamma^(x0) gamma^(x4); Omega_xt = -(1/2) E^-a4 b4^(1/2) ((a4' - b4'/(2 b4)) gamma^(x4) gamma^(xt) + H Sin[z]^(1/6) gamma^(xt) gamma^(x0)) for t = 5, 6, 7; Omega_x0 = 0"];
addFormulaText["Omega_components",
  "the spinor connection Omega_mu = (1/2) omega_mu,ab S^ab",
  "Omega_xi = (1/2) E^a4[x4] (a4'[x4] g[xi].g[x4] + H Sin[6 H x0]^(1/6) g[xi].g[x0]) (i = 1, 2, 3); Omega_x4 = (1/2) H Sin[6 H x0]^(1/6) g[x0].g[x4]; Omega_xt = -(1/2) E^-a4[x4] b4[x4]^(1/2) ((a4'[x4] - b4'[x4]/(2 b4[x4])) g[x4].g[xt] + H Sin[6 H x0]^(1/6) g[xt].g[x0]) (t = 5, 6, 7); Omega_x0 = 0; g[xa] = gamma^(xa) (frame gammas of the fixture)"];
covConst = Table[D[gup[[n]], X[[mu]]] + Sum[Gm[[n, mu, l]] gup[[l]], {l, 8}] + Om[[mu]] . gup[[n]] - gup[[n]] . Om[[mu]], {mu, 8}, {n, 8}];
addCheck["gamma_covariantly_constant",
  rftZeroQ[covConst],
  "D_mu gamma^nu = d_mu gamma^nu + Gamma^nu_mu,l gamma^l + [Omega_mu, gamma^nu] = 0 for all 64 (mu, nu), gamma^nu = e_a^nu gamma^a (the canonical connection is the one that makes the gammas covariantly constant)"];
addCheck["S_rotates_gamma_with_omega",
  rftZeroQ[Table[Om[[mu]] . g[[c]] - g[[c]] . Om[[mu]] + Sum[omMix[[mu, c, b]] g[[b]], {b, 8}], {mu, 8}, {c, 8}]],
  "[Omega_mu, gamma^c] = -omega_mu^c_b gamma^b (the frame form of covariant constancy)"];
Fsp[mu_, nu_] := D[Om[[nu]], X[[mu]]] - D[Om[[mu]], X[[nu]]] + Om[[mu]] . Om[[nu]] - Om[[nu]] . Om[[mu]];
Rframe[a_, b_, mu_, nu_] := Sum[eta[[a, a]] rftE0[[a, r]] Rm[[r, s, mu, nu]] rftEinv0[[s, b]], {r, 8}, {s, 8}];
addCheck["spin_curvature_equals_Riemann",
  rftZeroQ[Table[Fsp[mu, nu] - (1/2) Sum[Rframe[a, b, mu, nu] rftS[[a, b]], {a, 8}, {b, 8}], {mu, 8}, {nu, mu + 1, 8}]],
  "[D_mu, D_nu] Psi = (d_mu Omega_nu - d_nu Omega_mu + [Omega_mu, Omega_nu]) Psi = (1/2) R_ab,mu,nu S^ab Psi with R_ab,mu,nu = eta_aa e^a_r R^r_s,mu,nu e_b^s, all 28 pairs: " <>
  "the integrability (compatibility) condition of the spinor connection; it also shows that Omega cannot vanish in any frame unless the Riemann tensor vanishes (flat space)"];

(* gamma^mu Omega_mu *)
section["gamma^mu Omega_mu"];
gO = Sum[gup[[mu]] . Om[[mu]], {mu, 8}];
perDir = Table[gup[[mu]] . Om[[mu]], {mu, 8}];
coefDir = Table[Simplify[Tr[g[[a]] . perDir[[mu]]]/(16 eta[[a, a]])], {mu, 8}, {a, 8}];
addCheck["gammaOmega_total",
  rftZeroQ[gO - gOm],
  "gamma^mu Omega_mu = (7/2) H gamma^(x0) + (3/4)(b4'/b4) Sin[z]^(-1/6) gamma^(x4) exactly (independent of a4)"];
addCheck["gammaOmega_per_direction",
  And @@ Table[rftZeroQ[perDir[[mu]] - (a4p/(2 wf) g[[5]] + H/2 g[[1]])], {mu, 2, 4}] &&
  And @@ Table[rftZeroQ[perDir[[mu]] - ((-a4p/2 + bu/4)/wf g[[5]] + H/2 g[[1]])], {mu, 6, 8}] &&
  rftZeroQ[perDir[[5]] - H/2 g[[1]]] && rftZeroQ[perDir[[1]]],
  "per direction (no sum): gamma^(xi) Omega_xi = (a4'/2) Sin[z]^(-1/6) gamma^(x4) + (H/2) gamma^(x0) for each inflating 3-space direction i = 1, 2, 3, " <>
  "gamma^(x4) Omega_x4 = (H/2) gamma^(x0) for the warped time, and gamma^(xt) Omega_xt = (-a4'/2 + b4'/(4 b4)) Sin[z]^(-1/6) gamma^(x4) + (H/2) gamma^(x0) for each deflating extra time t = 5, 6, 7; gamma^(x0) Omega_x0 = 0. " <>
  "The a4' terms of the time direction cancel between the 3 inflating and the 3 deflating directions (+3 a4'/2 - 3 a4'/2), the b4' terms of the 3 extra times add to (3/4) b4'/b4; the hidden-direction terms of all seven warped directions add: 7 x H/2 = 7 H/2"];
addFormula["gammaOmega_per_direction", "the matrices gamma^mu Omega_mu (no sum) for mu = x0..x7 as coefficients of gamma^(x4) and gamma^(x0): {mu (Wolfram position 1..8 = x0..x7), coefficient of gamma^(x4), coefficient of gamma^(x0)}",
  Table[{mu, coefDir[[mu, 5]], coefDir[[mu, 1]]}, {mu, 8}]];
addFormula["gammaOmega_total", "gamma^mu Omega_mu (sum over mu); gamma[xa] = gamma^(xa)", (7/2) H gamma["x0"] + (3/4) (Derivative[1][b4][x4]/b4[x4]) Sin[6 H x0]^(-1/6) gamma["x4"]];
addCheck["gammaOmega_divergence_form",
  rftZeroQ[gO - 1/(2 sg) Sum[D[sg gup[[mu]], X[[mu]]], {mu, 8}]] &&
  rftZeroQ[Table[gup[[mu]] . Om[[mu]] + Om[[mu]] . gup[[mu]], {mu, 8}]],
  "{gamma^mu, Omega_mu} = 0 for each mu separately (Omega_mu contains only S^(mu b)), hence gamma^mu Omega_mu = (1/(2 sqrt g)) d_mu (sqrt g gamma^mu); " <>
  "for this metric (1/(2 sqrt g)) d_x0(sqrt g e_0^x0) gamma^(x0) = (1/(2 Cos z Sin^(1/6) z)) d_x0 (Sin^(7/6) z) gamma^(x0) = (7/2) H gamma^(x0), and (1/(2 sqrt g)) d_x4 (sqrt g/f4) gamma^(x4) = (3/4)(b4'/b4) Sin^(-1/6) z gamma^(x4) with sqrt g = b4^(3/2) Cos z Sin^(1/6) z"];

(* ------------------------------------------------------------------ 3. fields and Lagrangian *)
section["Lagrangian, both statistics"];
Ldata = lagData[stats];
grassKeysOK = Sort[Keys[Ldata["G"]["L"]]] == Sort[{{1, 3}, {1, 4}, {2, 3}, {2, 4}, {1, 2, 3, 4}}];
addCheck["grassmann_algebra_structure",
  gMul[gTheta[1], gTheta[2]] == <|{1, 2} -> 1|> && gMul[gTheta[2], gTheta[1]] == <|{1, 2} -> -1|> && gMul[gTheta[1], gTheta[1]] == <||> &&
  gConj[gMul[gTheta[1], gTheta[2]]] == gMul[gThetaBar[2], gThetaBar[1]] && gConj[gConj[<|{1, 4} -> c1 + I c2|>]] == <|{1, 4} -> c1 + I c2|> &&
  grassKeysOK && !gZeroQ[gMul[Ldata["G"]["S"], Ldata["G"]["S"]]] && gMul[gMul[Ldata["G"]["S"], Ldata["G"]["S"]], Ldata["G"]["S"]] == <||>,
  "explicit Grassmann algebra on theta_1, theta_2, thetabar_1, thetabar_2: theta_i theta_j = -theta_j theta_i, theta_i^2 = 0, conj(theta_1 theta_2) = thetabar_2 thetabar_1, conj conj = id; " <>
  "Psi_A = sum_k ph[A,k](x) theta_k; L has components only on thetabar_k theta_l (bilinear) and theta_1 theta_2 thetabar_1 thetabar_2 (quartic); S = Psibar Psi is even with S^2 != 0 and S^3 = 0, so U = u1 S + (lam/2) S^2 is the most general potential"];
Do[With[{L = Ldata[st]["L"]},
  addCheck["L_real_" <> st, sZeroQ[st, If[st === "G", gAdd[{gConj[L], gScal[-1, L]}], sConj[st, L] - L]],
    "L* = L exactly for " <> statName[st] <> If[st === "G",
      " (the involution reverses the order of Grassmann factors; U = u1 S + (lam/2) S^2 with real u1, lam)",
      " (ph <-> phc, i -> -i; U a real function)"] <>
    ": C real symmetric, C gamma^a real antisymmetric and S^T C + C S = 0 make the symmetrised kinetic term and Psibar Psi real without a factor i"]], {st, stats}];
Do[With[{P = fld[st]["Psi"], Pc = fld[st]["Psic"]},
  Module[{div, lhs},
    div = sAdd[st, Table[sD[st, sScal[st, sg, sDot[st, Pc, matVec[st, Cm . gup[[mu]], P]]], X[[mu]]], {mu, 8}]];
    lhs = sAdd[st, {Ldata[st]["L"], sScal[st, -1, Ldata[st]["Lu"]], sScal[st, 1/2, div]}];
    addCheck["L_total_divergence_to_unsymmetrised_" <> st, sZeroQ[st, lhs],
      "L = sqrt g [Psibar gamma^mu D_mu Psi - m S - U] - (1/2) d_mu (sqrt g Psibar gamma^mu Psi) exactly, for " <> statName[st] <>
      ": the two forms differ by a total divergence and give the same field equations"]]], {st, stats}];
Do[With[{P = fld[st]["Psi"], Pc = fld[st]["Psic"]},
  Module[{Lflat, geoFlat},
    geoFlat = <|"sqrtg" -> sg, "gup" -> gup, "Om" -> Table[z16, {8}]|>;
    Lflat = rftLag[st, geoFlat, P, Pc];
    addCheck["L_spin_connection_drops_out_" <> st, sZeroQ[st, sAdd[st, {Ldata[st]["L"], sScal[st, -1, Lflat]}]],
      "for this diagonal metric Psibar {gamma^mu, Omega_mu} Psi = 0 term by term, so L = sqrt g [(1/2)(Psibar gamma^mu d_mu Psi - d_mu Psibar gamma^mu Psi) - m S - U] exactly (" <>
      statName[st] <> "); the canonical spin connection reaches the field equations through d_mu(sqrt g gamma^mu) = 2 sqrt g gamma^mu Omega_mu (variation of the derivative terms), " <>
      "and the unsymmetrised form contains it explicitly"]]], {st, stats}];
addFormulaText["Lagrangian",
  "Lagrangian density for both statistics (SPEC section 3), Psibar = Psi^dagger C, S = Psibar Psi, sqrt g = b4^(3/2) Cos[z] Sin[z]^(1/6)",
  "L = b4[x4]^(3/2) Cos[z] Sin[z]^(1/6) [ (1/2) sum_mu (Psibar gamma^mu D_mu Psi - (D_mu Psibar) gamma^mu Psi) - m S - U(S) ] = b4[x4]^(3/2) Cos[z] Sin[z]^(1/6) [ (1/2) sum_a (1/f_a) (Psibar gamma^(a) d_a Psi - d_a Psibar gamma^(a) Psi) - m S - U(S) ]; f_0 = Cot[z], f_(1,2,3) = E^a4 Sin[z]^(1/6), f_4 = Sin[z]^(1/6), f_(5,6,7) = E^-a4 b4^(1/2) Sin[z]^(1/6)"];

(* ------------------------------------------------------------------ 4. Euler-Lagrange equations *)
section["Euler-Lagrange equations"];
Do[computeEL[st]; Module[{E1 = Ldata[st]["E"], Eb = Ldata[st]["Ebar"], CE, okc = True, okp = True},
  CE = matVec[st, Cm, E1];
  If[st === "C",
    Do[okc = okc && rftZeroQ[ELc[{st, A}] - sg CE[[A]]];
      okp = okp && rftZeroQ[ELp[{st, A}] + sg Eb[[A]]], {A, 16}],
    Do[okc = okc && gZeroQ[gAdd[{ELc[{st, A, k}], gScal[-sg, gMul[gThetaBar[k], CE[[A]]]]}]];
      okp = okp && gZeroQ[gAdd[{ELp[{st, A, k}], gScal[-sg, gMul[gTheta[k], Eb[[A]]]]}]], {A, 16}, {k, rftGN}]];
  addCheck["EL_Psibar_" <> st, okc,
    If[st === "G",
      "for every A = 1..16 and k = 1, 2: dL/dphc[A,k] - d_mu dL/d(d_mu phc[A,k]) = thetabar_k sqrt g (C E)_A with E = gamma^mu D_mu Psi - (m + U'(S)) Psi, U'(S) = u1 + lam S (explicit Grassmann algebra): the field equation is gamma^mu D_mu Psi = (m + U'(S)) Psi",
      "for every A = 1..16: dL/dPhi*_A - d_mu dL/d(d_mu Phi*_A) = sqrt g (C E)_A with E = gamma^mu D_mu Phi - (m + U'(S)) Phi (general U): the field equation is gamma^mu D_mu Phi = (m + U'(S)) Phi"]];
  addCheck["EL_Psi_" <> st, okp,
    If[st === "G",
      "for every A, k: dL/dph[A,k] - d_mu dL/d(d_mu ph[A,k]) = theta_k sqrt g Ebar_A with Ebar = (D_mu Psibar) gamma^mu + (m + U'(S)) Psibar (sign from moving theta_k to the left): the adjoint equation (D_mu Psibar) gamma^mu = -(m + U'(S)) Psibar",
      "for every A: dL/dPhi_A - d_mu dL/d(d_mu Phi_A) = -sqrt g Ebar_A with Ebar = (D_mu Phibar) gamma^mu + (m + U'(S)) Phibar: the adjoint equation (D_mu Phibar) gamma^mu = -(m + U'(S)) Phibar"]]], {st, stats}];
Do[Module[{E1 = Ldata[st]["E"], Eb = Ldata[st]["Ebar"], conjE},
  conjE = vecMat[st, sConj[st, #] & /@ E1, Cm];
  addCheck["adjoint_equation_is_Dirac_conjugate_" <> st,
    And @@ Table[sZeroQ[st, sAdd[st, {conjE[[A]], Eb[[A]]}]], {A, 16}],
    "E^dagger C = -Ebar exactly for " <> statName[st] <> " (uses C gamma^a C = -(gamma^a)^T, Omega^T C = -C Omega, U' real): the adjoint equation is the Dirac conjugate of the field equation"]], {st, stats}];

(* explicit Dirac operator *)
Do[With[{P = fld[st]["Psi"]},
  Module[{lhs, rhs},
    lhs = rftDirac[st, rftGeo0, P];
    rhs = vAdd[st, Fold[vAdd[st, #1, #2] &, Table[matVec[st, g[[a]]/f[[a]], vD[st, P, X[[a]]]], {a, 8}]], matVec[st, gOm, P]];
    addCheck["Dirac_operator_explicit_" <> st, And @@ Table[sZeroQ[st, sAdd[st, {lhs[[A]], sScal[st, -1, rhs[[A]]]}]], {A, 16}],
      "gamma^mu D_mu Psi = Tan[z] gamma^(x0) d0 Psi + E^-a4 Sin[z]^(-1/6) (gamma^(x1) d1 + gamma^(x2) d2 + gamma^(x3) d3) Psi + Sin[z]^(-1/6) gamma^(x4) d4 Psi + E^a4 b4^(-1/2) Sin[z]^(-1/6) (gamma^(x5) d5 + gamma^(x6) d6 + gamma^(x7) d7) Psi " <>
      "+ (7/2) H gamma^(x0) Psi + (3/4)(b4'/b4) Sin[z]^(-1/6) gamma^(x4) Psi, for " <> statName[st]]]], {st, stats}];
addFormulaText["field_equation",
  "the Euler-Lagrange equation (both statistics), z = 6 H x0, V = m + U'(S)",
  "Tan[z] g[x0] d0 Psi + E^-a4[x4] Sin[z]^(-1/6) (g[x1] d1 + g[x2] d2 + g[x3] d3) Psi + Sin[z]^(-1/6) g[x4] d4 Psi + E^a4[x4] b4[x4]^(-1/2) Sin[z]^(-1/6) (g[x5] d5 + g[x6] d6 + g[x7] d7) Psi + (7/2) H g[x0] Psi + (3/4) (b4'[x4]/b4[x4]) Sin[z]^(-1/6) g[x4] Psi = (m + U'(S)) Psi"];
addFormulaText["adjoint_equation",
  "the adjoint equation (both statistics); for this metric D_mu Psibar = d_mu Psibar - Psibar Omega_mu",
  "Tan[z] d0 Psibar g[x0] + E^-a4 Sin[z]^(-1/6) (d1 Psibar g[x1] + d2 Psibar g[x2] + d3 Psibar g[x3]) + Sin[z]^(-1/6) d4 Psibar g[x4] + E^a4 b4^(-1/2) Sin[z]^(-1/6) (d5 Psibar g[x5] + d6 Psibar g[x6] + d7 Psibar g[x7]) + (7/2) H Psibar g[x0] + (3/4) (b4'/b4) Sin[z]^(-1/6) Psibar g[x4] = -(m + U'(S)) Psibar"];
(* 16 explicit components with inert symbols *)
compStr = Table[Module[{terms = {}},
   Do[If[g[[a, A, B]] =!= 0, AppendTo[terms, g[[a, A, B]]/f[[a]] dd[rftCoordNames[[a]], Psi[B]]]], {a, 8}, {B, 16}];
   Do[If[g[[1, A, B]] =!= 0, AppendTo[terms, (7/2) H g[[1, A, B]] Psi[B]]], {B, 16}];
   Do[If[g[[5, A, B]] =!= 0, AppendTo[terms, (3/4) bu wf^-1 g[[5, A, B]] Psi[B]]], {B, 16}];
   wl[Total[terms] == V Psi[A]]], {A, 16}];
AppendTo[formulas, <|"key" -> "field_equation_components", "description" -> "the 16 component equations (gamma^mu D_mu Psi)_A = V Psi_A, A = 1..16 (rows of the fixture gammas), V = m + U'(S); dd[xa, Psi[B]] = d Psi_B / d xa", "wl" -> compStr|>];
blk[a_] := {g[[a]][[1 ;; 8, 9 ;; 16]], g[[a]][[9 ;; 16, 1 ;; 8]]};
addCheck["block_form",
  And @@ Table[g[[a]][[1 ;; 8, 1 ;; 8]] == ConstantArray[0, {8, 8}] && g[[a]][[9 ;; 16, 9 ;; 16]] == ConstantArray[0, {8, 8}], {a, 8}] &&
  rftChir == ArrayFlatten[{{-IdentityMatrix[8], 0}, {0, IdentityMatrix[8]}}],
  "every gamma^a = {{0, tb_a}, {t_a, 0}} is block off-diagonal in the chiral split Psi = (psi_-, psi_+) (Gamma = diag(-1, 1)): the field equation is the pair " <>
  "sum_a (1/f_a) tb_a d_a psi_+ + (7/2) H tb_0 psi_+ + (3/4)(b4'/b4) Sin[z]^(-1/6) tb_4 psi_+ = V psi_- and sum_a (1/f_a) t_a d_a psi_- + (7/2) H t_0 psi_- + (3/4)(b4'/b4) Sin[z]^(-1/6) t_4 psi_- = V psi_+ (blocks in field-theory.json)"];
AppendTo[formulas, <|"key" -> "field_equation_blocks",
  "description" -> "block form: Psi = (psi_minus (rows 1..8, Gamma = -1), psi_plus (rows 9..16, Gamma = +1)); gamma^(xa) = {{0, tb[xa]}, {t[xa], 0}}; equations sum_a (1/f_a) tb[xa] d_a psi_plus + (7/2) H tb[x0] psi_plus + (3/4)(b4'/b4) Sin[z]^(-1/6) tb[x4] psi_plus = V psi_minus and sum_a (1/f_a) t[xa] d_a psi_minus + (7/2) H t[x0] psi_minus + (3/4)(b4'/b4) Sin[z]^(-1/6) t[x4] psi_minus = V psi_plus; listed {xa, tb, t}",
  "wl" -> Table[wl[{rftCoordNames[[a]], blk[a][[1]], blk[a][[2]]}], {a, 8}]|>];
(* evolution form *)
Do[With[{P = fld[st]["Psi"]},
  Module[{S = Ldata[st]["S"], rest, d4},
    rest = vAdd[st, Fold[vAdd[st, #1, #2] &, Table[If[a == 5, Table[sZero[st], {16}], matVec[st, g[[a]]/f[[a]], vD[st, P, X[[a]]]]], {a, 8}]], matVec[st, (7/2) H g[[1]], P]];
    d4 = vAdd[st, matVec[st, -wf g[[5]], vAdd[st, rftVPsi[st, S, P], vScal[st, -1, rest]]], vScal[st, -(3/4) bu, P]];
    addCheck["evolution_form_" <> st,
      g[[5]] . g[[5]] == -id16 && rftZeroQ[f[[5]] - wf] &&
      And @@ Table[sZeroQ[st, sAdd[st, {matVec[st, g[[5]]/wf, vAdd[st, vD[st, P, x4], vScal[st, -1, d4]]][[A]], sScal[st, -1, Ldata[st]["E"][[A]]]}]], {A, 16}],
      "(gamma^(x4))^2 = -1, so the field equation is equivalent to the first-order evolution equation d4 Psi = -Sin[z]^(1/6) gamma^(x4) [(m + U'(S)) Psi - sum_(a != x4) (1/f_a) gamma^(a) d_a Psi - (7/2) H gamma^(x0) Psi] - (3/4)(b4'/b4) Psi " <>
      "(exact: Sin[z]^(-1/6) gamma^(x4) (d4 Psi - RHS) = E; the lapse Sin[z]^(1/6) of the warped time multiplies the bracket; the last term is the factor b4^(-3/4) of the solutions): the slices x4 = const are non-characteristic (g^44 = -Sin[z]^(-1/3) != 0), " <> statName[st]]]], {st, stats}];
addFormulaText["evolution_form", "first-order evolution form (both statistics)",
  "d4 Psi = -Sin[z]^(1/6) g[x4] ((m + U'(S)) Psi - sum_(a != x4) (1/f_a) g[xa] d_a Psi - (7/2) H g[x0] Psi) - (3/4) (b4'[x4]/b4[x4]) Psi"];

(* ------------------------------------------------------------------ 5. non-triviality *)
section["non-triviality"];
Do[With[{P = fld[st]["Psi"], Pc = fld[st]["Psic"]},
  Module[{geoNoOm, Enoom, diff},
    geoNoOm = <|"sqrtg" -> sg, "gup" -> gup, "Om" -> Table[z16, {8}]|>;
    Enoom = rftE[st, geoNoOm, P, Pc];
    diff = vAdd[st, Ldata[st]["E"], vScal[st, -1, Enoom], vScal[st, -1, matVec[st, gOm, P]]];
    addCheck["nontriviality_" <> If[st === "G", "1_dirac16complex", "2_dirac16complex00"],
      (And @@ Table[sZeroQ[st, diff[[A]]], {A, 16}]) && !(And @@ Table[sZeroQ[st, matVec[st, gOm, P][[A]]], {A, 16}]) &&
      rftZeroQ[gOm . gOm - ((49/4) H^2 - (9/16) bu^2 wW) id16] &&
      !rftZeroQ[1/f[[2]] - 1] && !rftZeroQ[1/f[[6]] - 1] && !rftZeroQ[1/f[[1]] - 1] && !rftZeroQ[1/f[[5]] - 1],
      "NON-TRIVIALITY [" <> If[st === "G", "1", "2"] <> "] for " <> statName[st] <> ": the spin-connection part of the Euler-Lagrange equation is exactly " <>
      "(gamma^mu D_mu - gamma^mu d_mu) Psi = gamma^mu Omega_mu Psi = G Psi with G = (7/2) H gamma^(x0) + (3/4)(b4'/b4) Sin[z]^(-1/6) gamma^(x4), nonzero for every H > 0 and all functions a4, b4 (its gamma^(x0) coefficient is 7 H/2); " <>
      "G^2 = ((49/4) H^2 - (9/16)(b4'/b4)^2 Sin[z]^(-1/3)) I16, so G Psi != 0 for every Psi != 0 wherever (b4'/b4)^2 Sin[z]^(-1/3) != (196/9) H^2; " <>
      "in addition the vielbein enters every derivative term, gamma^mu d_mu = Tan[z] gamma^(x0) d0 + E^-a4 Sin[z]^(-1/6) gamma^(xi) d_i + Sin[z]^(-1/6) gamma^(x4) d4 + E^a4 b4^(-1/2) Sin[z]^(-1/6) gamma^(xt) d_t " <>
      "(none of the factors is identically 1). The a4'-terms of the spin connection cancel between the 3 inflating and the 3 deflating directions, the b4'-terms of the extra times remain (check gammaOmega_per_direction). " <>
      "All gravitational terms vanish together only if Omega_mu = 0 for all mu, " <>
      "which by spin_curvature_equals_Riemann requires a flat metric; R^(x0)_(x0) = -7 H^2 shows the metric is never flat for H > 0 (H = 0 itself is a degenerate limit, check degenerate_at_H_0)"]]], {st, stats}];
addCheck["Omega_vanishes_iff_a4prime_b4prime_and_H_vanish",
  And @@ Table[Module[{v = e[[4]], c, fac},
     c = Which[!FreeQ[v, Derivative[1][b4]], a4p - bu/2, !FreeQ[v, a4p], a4p, True, H];
     fac = Cancel[Together[v/c]];
     FreeQ[fac, a4p] && FreeQ[fac, Derivative[1][b4]] && FreeQ[fac /. rftZ -> zz, H] &&
       (rftZeroQ[fac^12 - E^(12 a4[x4]) Sin[rftZ]^2] || rftZeroQ[fac^12 - E^(-12 a4[x4]) b4[x4]^6 Sin[rftZ]^2] ||
        rftZeroQ[fac^12 - E^(12 a4[x4])] || rftZeroQ[fac^12 - E^(-12 a4[x4]) b4[x4]^6] || rftZeroQ[fac^12 - Sin[rftZ]^2])], {e, omExpected}],
  "each of the 13 nonzero omega_mu,ab is a4', a4' - b4'/(2 b4) or H times a factor +-E^(+-a4), +-E^-a4 b4^(1/2), +-E^(+-a4) Sin[z]^(1/6), +-E^-a4 b4^(1/2) Sin[z]^(1/6) or Sin[z]^(1/6) that never vanishes on 0 < z < Pi/2: " <>
  "the x4-part of Omega_xi (3-space) vanishes iff a4 is constant, the x4-part of Omega_xt (extra times) iff E^-a4 b4^(1/2) is constant, and the H-part iff H = 0; " <>
  "so all x4-parts vanish iff a4 and b4 are both constant, and for H > 0 the spin connection never vanishes"];

(* ------------------------------------------------------------------ 6. self-consistency: current, integrability *)
section["current and integrability"];
Do[With[{P = fld[st]["Psi"], Pc = fld[st]["Psic"]},
  Module[{J, divJ, rhs, Eb = Ldata[st]["Ebar"], E1 = Ldata[st]["E"]},
    J = Table[sScal[st, -I, sDot[st, Pc, matVec[st, Cm . gup[[mu]], P]]], {mu, 8}];
    divJ = sAdd[st, Table[sD[st, sScal[st, sg, J[[mu]]], X[[mu]]], {mu, 8}]];
    rhs = sScal[st, -I sg, sAdd[st, {sDot[st, Eb, P], sDot[st, rftPsibar[st, Pc], E1]}]];
    addCheck["current_real_" <> st, And @@ Table[sZeroQ[st, If[st === "G", gAdd[{gConj[J[[mu]]], gScal[-1, J[[mu]]]}], sConj[st, J[[mu]]] - J[[mu]]]], {mu, 8}],
      "J^mu = -i Psibar gamma^mu Psi is real (Hermitian) for " <> statName[st] <> " (-i C gamma^a is Hermitian)"];
    addCheck["current_conservation_identity_" <> st, sZeroQ[st, sAdd[st, {divJ, sScal[st, -1, rhs]}]],
      "d_mu (sqrt g J^mu) = -i sqrt g (Ebar Psi + Psibar E) exactly (off shell), so nabla_mu J^mu = 0 on shell, for " <> statName[st]];
    addCheck["charge_density_is_Krein_form_" <> st, sZeroQ[st, sAdd[st, {J[[5]], sScal[st, -1/wf, sDot[st, Pc, matVec[st, Bm, P]]]}]],
      "J^(x4) = Sin[z]^(-1/6) Psi^dagger B Psi with B = -i C gamma^(x4) (Hermitian, signature (8,8)): the charge Q = integral of sqrt g J^x4 = b4^(3/2) Cos[z] Psi^dagger B Psi d^7x over a slice x4 = const (the lapse cancels: sqrt g/f4 = b4^(3/2) Cos[z]) is an indefinite form, " <> statName[st] <>
      " (only the local law d_mu (b4^(3/2) Cos[z] J^mu) = 0 on shell is proved; Q is constant in x4 only if no charge flows through the boundary of the slice, which at the brane z = Pi/2 is an ASSUMED no-flux condition that this record does not impose)"]]], {st, stats}];
addFormulaText["current", "conserved current and its identity (both statistics)",
  "J^mu = -i Psibar gamma^mu Psi; d_mu (b4[x4]^(3/2) Cos[z] Sin[z]^(1/6) J^mu) = -i b4[x4]^(3/2) Cos[z] Sin[z]^(1/6) (Ebar Psi + Psibar E); J^x4 = Sin[z]^(-1/6) Psi^dagger B Psi; Q = Integral b4[x4]^(3/2) Cos[z] Psi^dagger B Psi dx0 dx1 dx2 dx3 dx5 dx6 dx7"];
(* Lichnerowicz *)
Do[With[{P = fld[st]["Psi"]},
  Module[{Dop, DD, box, lhs, res},
    Dop[w_] := Fold[vAdd[st, #1, #2] &, Table[matVec[st, gup[[mu]], vAdd[st, vD[st, w, X[[mu]]], matVec[st, Om[[mu]], w]]], {mu, 8}]];
    DD = Table[vAdd[st, vD[st, P, X[[nu]]], matVec[st, Om[[nu]], P]], {nu, 8}];
    box = Fold[vAdd[st, #1, #2] &, Table[vScal[st, rftGinv0[[mu, mu]],
       vAdd[st, vD[st, DD[[mu]], X[[mu]]], matVec[st, Om[[mu]], DD[[mu]]], vScal[st, -1, Fold[vAdd[st, #1, #2] &, Table[vScal[st, Gm[[l, mu, mu]], DD[[l]]], {l, 8}]]]]], {mu, 8}]];
    lhs = Dop[Dop[P]];
    res = vAdd[st, lhs, vScal[st, -1, box], vScal[st, 1/4 RsExpected, P]];
    addCheck["Lichnerowicz_identity_" <> st, And @@ Table[sZeroQ[st, res[[A]]], {A, 16}],
      "(gamma^mu D_mu)^2 Psi = g^mu,nu (D_mu D_nu Psi - Gamma^l_mu,nu D_l Psi) - (R/4) Psi with R = -56 H^2 + Sin[z]^(-1/3) (6 a4'^2 - 3 a4' b4'/b4 + 3 b4''/b4), for a general " <> statName[st] <>
      " (exact): the second-order consequence of the field equations is consistent with the curvature (integrability)"]]], {st, stats}];
addFormulaText["Lichnerowicz", "second-order identity (both statistics)",
  "(gamma^mu D_mu)^2 Psi = g^mu,nu (D_mu D_nu - Gamma^l_mu,nu D_l) Psi - (R/4) Psi, R = -56 H^2 + Sin[z]^(-1/3) (6 a4'[x4]^2 - 3 a4'[x4] b4'[x4]/b4[x4] + 3 b4''[x4]/b4[x4])"];

(* ------------------------------------------------------------------ 7. negative control: Majorana-type Lg *)
section["Majorana-type Lg"];
Module[{PsiR, Lg, cur, divc, okEL = True, PhiR, LgC, okC = True, ELC, mass},
  PsiR = Table[gAdd[Table[<|{k} -> phr[A, k] @@ X|>, {k, rftGN}]], {A, 16}];
  Lg = gScal[sg, gAdd[Table[sDot["G", PsiR, matVec["G", Cm . gup[[mu]], vAdd["G", vD["G", PsiR, X[[mu]]], matVec["G", Om[[mu]], PsiR]]]], {mu, 8}]]];
  cur = Table[gScal[sg/2, sDot["G", PsiR, matVec["G", Cm . gup[[mu]], PsiR]]], {mu, 8}];
  divc = gAdd[Table[gD[cur[[mu]], X[[mu]]], {mu, 8}]];
  Do[okEL = okEL && gZeroQ[rftVarDer["G", Lg, phr[A, k]]], {A, 16}, {k, rftGN}];
  mass = sDot["G", PsiR, matVec["G", Cm, PsiR]];
  addCheck["Majorana_Lg_total_derivative_grassmann",
    gZeroQ[gAdd[{Lg, gScal[-1, divc]}]] && !gZeroQ[Lg] && okEL && mass == <||>,
    "for REAL anticommuting components Psi_A = sum_k phr[A,k](x) theta_k (explicit Grassmann algebra, N = 2): sqrt g Psi^T C gamma^mu D_mu Psi = d_mu ((1/2) sqrt g Psi^T C gamma^mu Psi) exactly; " <>
    "it is not zero, but it is a total derivative: all 32 Euler-Lagrange expressions vanish identically (no field equation). Also Psi^T C Psi = 0 (C symmetric). " <>
    "This is why the notebook's Majorana-type Lg[] cannot serve and the Dirac-type L with Psibar = Psi^dagger C is used"];
  PhiR = Table[phr[A] @@ X, {A, 16}];
  LgC = sg Sum[PhiR . Cm . gup[[mu]] . (D[PhiR, X[[mu]]] + Om[[mu]] . PhiR), {mu, 8}];
  Do[ELC = rftVarDerExpr[LgC, phr[A]];
     okC = okC && rftZeroQ[ELC - 2 sg (Cm . Sum[gup[[mu]] . (D[PhiR, X[[mu]]] + Om[[mu]] . PhiR), {mu, 8}])[[A]]], {A, 16}];
  addCheck["Majorana_Lg_commuting_control",
    okC && rftZeroQ[Table[PhiR . Cm . gup[[mu]] . PhiR, {mu, 8}]],
    "control: for REAL COMMUTING components the same Lg gives the nontrivial Euler-Lagrange expression 2 sqrt g (C gamma^mu D_mu Phi)_A (a massless equation) while Phi^T C gamma^mu Phi = 0 identically: " <>
    "Lg is a total derivative exactly for anticommuting real components"]];

(* ------------------------------------------------------------------ energy exchange *)
(* ALL EIGHT components nabla_mu T^mu_nu for a diagonal T whose entries rho, p3, pt, p0 are functions of x4 AND x0
   (homogeneous in x1, x2, x3, x5, x6, x7).  The global symbols rho, p3, pt, p0 are used only here; they appear by name
   in field-theory.json (formula energy_exchange).  p0 is the pressure along the hidden direction x0. *)
section["energy exchange"];
Module[{Tdiag, divAll, expected, d4rho, d0p0, eqs, okDiv, okEqs, okFree, ctrl, T0, div0, rho0, p30, pt0, p00},
  Tdiag = DiagonalMatrix[{p0[x4, x0], p3[x4, x0], p3[x4, x0], p3[x4, x0], -rho[x4, x0], pt[x4, x0], pt[x4, x0], pt[x4, x0]}];
  (* nabla_mu T^mu_nu = (1/sqrt g) d_mu (sqrt g T^mu_nu) - Gamma^r_(mu nu) T^mu_r *)
  divAll = Table[Sum[D[sg Tdiag[[mu, nu]], X[[mu]]], {mu, 8}]/sg - Sum[Gm[[r, mu, nu]] Tdiag[[mu, r]], {mu, 8}, {r, 8}], {nu, 8}];
  d4rho = Derivative[1, 0][rho][x4, x0]; d0p0 = Derivative[0, 1][p0][x4, x0];
  expected = {d0p0 + H Cot[6 H x0] (7 p0[x4, x0] - 3 p3[x4, x0] - 3 pt[x4, x0] + rho[x4, x0]), 0, 0, 0,
    -d4rho - 3 a4p (p3[x4, x0] - pt[x4, x0]) - (3/2) bu (rho[x4, x0] + pt[x4, x0]), 0, 0, 0};
  okDiv = rftZeroQ[divAll - expected];
  eqs = {d4rho == -3 a4p (p3[x4, x0] - pt[x4, x0]) - (3/2) bu (rho[x4, x0] + pt[x4, x0]), d0p0 == -H Cot[6 H x0] (7 p0[x4, x0] - 3 p3[x4, x0] - 3 pt[x4, x0] + rho[x4, x0])};
  okEqs = Coefficient[expected[[5]], d4rho] === -1 && Coefficient[expected[[1]], d0p0] === 1 &&
    rftZeroQ[expected[[5]] /. d4rho -> eqs[[1, 2]]] && rftZeroQ[expected[[1]] /. d0p0 -> eqs[[2, 2]]];
  (* x0-independent entries: the x0 component is H Cot[z] (7 p0 - 3 p3 - 3 p_t + rho) with Cot[z] > 0, so 7 p0 = 3 p3 + 3 p_t - rho *)
  T0 = DiagonalMatrix[{p00[x4], p30[x4], p30[x4], p30[x4], -rho0[x4], pt0[x4], pt0[x4], pt0[x4]}];
  div0 = Table[Sum[D[sg T0[[mu, nu]], X[[mu]]], {mu, 8}]/sg - Sum[Gm[[r, mu, nu]] T0[[mu, r]], {mu, 8}, {r, 8}], {nu, 8}];
  okFree = rftZeroQ[div0 - (expected /. {rho -> (rho0[#1] &), p3 -> (p30[#1] &), pt -> (pt0[#1] &), p0 -> (p00[#1] &)})] &&
    rftZeroQ[div0[[1]] /. p00[x4] -> (3 p30[x4] + 3 pt0[x4] - rho0[x4])/7] && Simplify[Cot[6 H x0] > 0, rftAssumptions];
  (* controls: the formula without the b4 term, a wrong sign of the a4' term, and the x0 balance of the metric of 2026-10-14
     (3 H Cot[z] (2 p0 - p3 - p_t), without the lapse) are detected *)
  ctrl = !rftZeroQ[divAll[[5]] - (-d4rho - 3 a4p (p3[x4, x0] - pt[x4, x0]))] &&
    !rftZeroQ[divAll[[5]] - (-d4rho + 3 a4p (p3[x4, x0] - pt[x4, x0]) - (3/2) bu (rho[x4, x0] + pt[x4, x0]))] &&
    !rftZeroQ[divAll[[1]] - (d0p0 + 3 H Cot[6 H x0] (2 p0[x4, x0] - p3[x4, x0] - pt[x4, x0]))];
  addCheck["energy_exchange_equation", okDiv && okEqs && okFree && ctrl,
    "for a diagonal T^mu_nu = diag(p0, p3, p3, p3, -rho, p_t, p_t, p_t) (order x0..x7) whose entries are functions of x4 and x0, all eight components: " <>
    "nabla_mu T^mu_x4 = -d rho/d x4 - 3 a4' (p3 - p_t) - (3/2)(b4'/b4)(rho + p_t), " <>
    "nabla_mu T^mu_x0 = d p0/d x0 + H Cot[z] (7 p0 - 3 p3 - 3 p_t + rho), and nabla_mu T^mu_nu = 0 identically for nu = x1, x2, x3, x5, x6, x7. Conservation is therefore exactly " <>
    "d rho/d x4 = -3 a4' (p3 - p_t) - (3/2)(b4'/b4)(rho + p_t) (energy flows between 3-space and the extra times unless p3 = p_t, and the extra-time volume factor b4^(3/2) dilutes rho + p_t; the lapse Sin[z]^(1/6) does not enter) " <>
    "and d p0/d x0 = -H Cot[z] (7 p0 - 3 p3 - 3 p_t + rho) (hidden-direction balance; the warped time adds H Cot[z] (p0 + rho)); the two components are independent " <>
    "(the x4 component contains no x0 derivative and no H, the x0 component no x4 derivative, no a4' and no b4'). For x0-independent entries the x0 component is H Cot[z] (7 p0 - 3 p3 - 3 p_t + rho) with Cot[z] > 0 on 0 < z < Pi/2, " <>
    "so conservation needs 7 p0 = 3 p3 + 3 p_t - rho. " <>
    "Controls: the formula without the b4' term, a wrong sign of the a4' term and the x0 balance of the metric of 2026-10-14 (3 H Cot[z] (2 p0 - p3 - p_t)) are detected"];
  AppendTo[formulas, <|"key" -> "energy_exchange",
    "description" -> "conservation of a diagonal T = diag(p0, p3, p3, p3, -rho, pt, pt, pt) (order x0..x7) whose entries are functions of x4 and x0 (check energy_exchange_equation); " <>
      "entry 1: {nabla_mu T^mu_nu, nu = x0..x7} (complete identity); entry 2: the equations equivalent to nabla_mu T^mu_nu = 0; entry 3: the same for x0-independent entries (rho, p3, pt, p0 functions of x4 only)",
    "wl" -> {wl[expected], wl[eqs],
      wl[{Derivative[1][rho][x4] == -3 a4p (p3[x4] - pt[x4]) - (3/2) bu (rho[x4] + pt[x4]), 7 p0[x4] == 3 p3[x4] + 3 pt[x4] - rho[x4]}]}|>]];

(* ------------------------------------------------------------------ formulas: statements and geometry *)
addFormulaText["nontriviality",
  "NON-TRIVIALITY [1] (dirac16complex) and [2] (dirac16complex00): exact content of checks nontriviality_1_dirac16complex, nontriviality_2_dirac16complex00, gammaOmega_per_direction, Omega_vanishes_iff_a4prime_b4prime_and_H_vanish, never_flat_for_H_positive, spin_curvature_equals_Riemann",
  "gamma^mu D_mu Psi - gamma^mu d_mu Psi = gamma^mu Omega_mu Psi = ((7/2) H gamma^(x0) + (3/4)(b4'/b4) Sin[z]^(-1/6) gamma^(x4)) Psi (nonzero for every H > 0, all a4 and b4; its square is (49/4) H^2 - (9/16)(b4'/b4)^2 Sin[z]^(-1/3)); " <>
  "per direction gamma^(xi) Omega_xi = (a4'/2) Sin[z]^(-1/6) gamma^(x4) + (H/2) gamma^(x0) (i = 1, 2, 3, inflating), gamma^(x4) Omega_x4 = (H/2) gamma^(x0) (the warped time) and gamma^(xt) Omega_xt = (-a4'/2 + b4'/(4 b4)) Sin[z]^(-1/6) gamma^(x4) + (H/2) gamma^(x0) (t = 5, 6, 7, deflating): the a4' terms of the time direction cancel, the b4' terms add to (3/4) b4'/b4, the hidden-direction terms add (7 H/2); " <>
  "Omega_mu = 0 for all mu iff a4' = 0, b4' = 0 and H = 0 (H = 0 is a degenerate limit of the metric); [D_mu, D_nu] = (1/2) R_ab,mu,nu S^ab, and R^x0_x0 = -7 H^2 != 0: no frame removes Omega, the metric is never flat for H > 0"];
addFormulaText["majorana_negative_control",
  "the notebook's Majorana-type Lagrangian with real components (checks Majorana_Lg_total_derivative_grassmann, Majorana_Lg_commuting_control)",
  "anticommuting real Psi: sqrt g Psi^T C gamma^mu D_mu Psi = d_mu ((1/2) sqrt g Psi^T C gamma^mu Psi) (a total derivative; no field equation; Psi^T C Psi = 0); commuting real Phi: Euler-Lagrange expression 2 sqrt g C gamma^mu D_mu Phi and Phi^T C gamma^mu Phi = 0"];
addFormulaText["equation_of_state_definitions", "pressures and equations of state from the diagonal components (SPEC section 4)",
  "rho = -T^x4_x4, p3 = T^x1_x1, p_t = T^x5_x5, p0 = T^x0_x0; w3 = p3/rho, w_t = p_t/rho, w0 = p0/rho; homogeneous on shell: w3 = w_t = w0 = (S U' - U)/(m S + U)"];
addFormulaText["hidden_direction_hermiticity", "role of the spin-connection term in the quantum theory (check good_sector_hermiticity_curved)",
  "Cos[z] Sin[z]^(1/6) [p (Tan[z] d0 + 7 H/2) q + ((Tan[z] d0 + 7 H/2) p) q] = d0 (Sin[z]^(7/6) p q): the operator Sin[z]^(1/6) (Tan[z] d0 + 7 H/2) is antisymmetric for the measure Cos[z] dx0 up to the boundary term Sin[z]^(7/6) p q, which does not vanish at z = Pi/2; without 7 H/2 the mode operator is not formally Hermitian for this measure and these variables"];
addFormula["metric", "the warped metric (SPEC section 1; the user's order of 2026-10-16), coordinates x0..x7", rftMetricAuthor];
addFormula["vielbein_diagonal", "f_a in e^a_mu = f_a delta^a_mu, a = x0..x7", f];
addFormula["sqrt_det_g", "sqrt|det g|", b4[x4]^(3/2) Cos[6 H x0] Sin[6 H x0]^(1/6)];
addFormula["eta", "frame metric eta_ab, order x0..x7", Diagonal[eta]];
];

(* ================================================================== PART emt-G / emt-C *)
If[StringStartsQ[part, "emt-"],
st = stats[[1]];
section["Lagrangian and Euler-Lagrange expressions, statistics " <> st];
Ldata = lagData[stats];
computeEL[st];
section["energy-momentum tensor by vielbein variation, statistics " <> st];
Tdata = <||>;
Module[{P = fld[st]["Psi"], Pc = fld[st]["Psic"], L0 = Ldata[st]["L0"], pb, Bmat, canon, Sig, Aten, divA, Tvar, Tsym, okF, okSym, tt},
  tt = AbsoluteTime[];
  pb = rftPsibar[st, Pc];
  Bmat = Table[sAdd[st, {sDot[st, vecMat[st, pb, gup[[r]]], rftDPsi[st, rftGeo0, P, s]], sScal[st, -1, sDot[st, vecMat[st, rftDPsibar[st, rftGeo0, Pc, s], gup[[r]]], P]]}], {r, 8}, {s, 8}];
  Sig[n_, r_] := (1/4) (gup[[n]] . gup[[r]] - gup[[r]] . gup[[n]]);
  Aten = Table[If[Length[Union[{l, n, r}]] < 3, sZero[st], bilM[st, Pc, gup[[l]] . Sig[n, r] + Sig[n, r] . gup[[l]], P]], {l, 8}, {n, 8}, {r, 8}];
  divA = Table[sScal[st, 1/sg, sAdd[st, Table[sD[st, sScal[st, sg, Aten[[l, n, r]]], X[[l]]], {l, 8}]]], {n, 8}, {r, 8}];
  canon[n_, mu_] := sAdd[st, {If[n == mu, L0, sZero[st]], sScal[st, -1/2, Bmat[[n, mu]]]}];
  (* closed-form variation result: canon - (1/4) g_mu,rho nabla_l A^(l n rho) (diagonal metric: rho = mu) *)
  Tvar = Table[sScal[st, f[[mu]], rftTvar[st, mu, n, P, Pc, L0]], {n, 8}, {mu, 8}];   (* T^n_mu = T^n_b e^b_mu, b = mu *)
  Print["   ", st, " vielbein variations: ", Round[AbsoluteTime[] - tt, 0.1], " s"];
  (* the 64 test expressions are built here; their zero tests run on the subkernels (pS) *)
  okF = And @@ pS[st, Flatten[Table[sAdd[st, {Tvar[[n, mu]], sScal[st, -1, canon[n, mu]], sScal[st, rftG0[[mu, mu]]/4, divA[[n, mu]]]}], {n, 8}, {mu, 8}], 1]];
  Tsym = Table[sAdd[st, {If[n == mu, L0, sZero[st]], sScal[st, -1/4, Bmat[[n, mu]]], sScal[st, -1/4 rftG0[[mu, mu]] rftGinv0[[n, n]], Bmat[[mu, n]]]}], {n, 8}, {mu, 8}];
  (* symmetric part of T_var (indices up: T^(n r) = T^n_mu g^(mu r)) equals T_sym *)
  okSym = And @@ pS[st, Flatten[Table[sAdd[st, {sScal[st, rftGinv0[[r, r]], Tvar[[n, r]]], sScal[st, rftGinv0[[n, n]], Tvar[[r, n]]], sScal[st, -2 rftGinv0[[r, r]], Tsym[[n, r]]]}], {n, 8}, {r, n, 8}], 1]];
  Tdata[st] = <|"Tvar" -> Tvar, "Tsym" -> Tsym, "Bmat" -> Bmat, "divA" -> divA|>;
  addCheck["T_vielbein_variation_closed_form_" <> st, okF,
    "for all 64 components (" <> statName[st] <> ", metric with general a4 and b4), T^nu_mu := e^b_mu (1/sqrt g) delta S / delta e^b_nu (exact first-order variation of sqrt g, gamma^mu and the spin connection, functional derivative in h(x)) equals " <>
    "delta^nu_mu L0 - (1/2)(Psibar gamma^nu D_mu Psi - D_mu Psibar gamma^nu Psi) - (1/4) g_mu,rho nabla_l (Psibar {gamma^l, Sigma^(nu rho)} Psi), Sigma^(nu rho) = (1/4)[gamma^nu, gamma^rho], L0 = L/sqrt g; " <>
    "the last term (totally antisymmetric spin density) comes from the variation of the spin connection"];
  addCheck["T_symmetric_part_Belinfante_" <> st, okSym,
    "the symmetric part of the variation tensor, (T^(nu rho) + T^(rho nu))/2, equals T_sym^(nu rho) = g^(nu rho) L0 - (1/4)(Psibar gamma^nu D^rho Psi + Psibar gamma^rho D^nu Psi - D^rho Psibar gamma^nu Psi - D^nu Psibar gamma^rho Psi) for all 36 pairs (" <> statName[st] <> ")"]];

section["Noether identities, statistics " <> st];
Module[{P = fld[st]["Psi"], Pc = fld[st]["Psic"], Tvar = Tdata[st]["Tvar"], ELterm, okD, okL, Tb},
  (* Tb[nu, b] = T^nu_b = T^nu_mu e_b^mu (b = mu) *)
  Tb[n_, b_] := sScal[st, 1/f[[b]], Tvar[[n, b]]];
  If[st === "C",
    ELterm[lamb_] := sAdd[st, Join[Table[ELp[{st, A}] D[ph[A] @@ X, X[[lamb]]], {A, 16}], Table[ELc[{st, A}] D[phc[A] @@ X, X[[lamb]]], {A, 16}]]],
    ELterm[lamb_] := gAdd[Flatten[Table[{gScal[D[ph[A, k] @@ X, X[[lamb]]], ELp[{st, A, k}]], gScal[D[phc[A, k] @@ X, X[[lamb]]], ELc[{st, A, k}]]}, {A, 16}, {k, rftGN}]]]];
  (* the 8 test expressions are built here; their zero tests run on the subkernels (pS) *)
  okD = And @@ pS[st, Table[sAdd[st, {
      sAdd[st, Table[sD[st, sScal[st, sg, Tvar[[mu, lamb]]], X[[mu]]], {mu, 8}]],
      sScal[st, -sg, sAdd[st, Table[sScal[st, D[f[[mu]], X[[lamb]]], Tb[mu, mu]], {mu, 8}]]],
      sScal[st, -1, ELterm[lamb]]}], {lamb, 8}]];
  addCheck["Noether_identity_diffeomorphisms_" <> st, okD,
    "for each lambda = x0..x7 (" <> statName[st] <> ", general fields, off shell, metric with general a4 and b4): d_mu (sqrt g T^mu_lambda) - sqrt g T^mu_a d_lambda e^a_mu = sum over all component functions phi of EL_phi d_lambda phi " <>
    "(EL_phi = the Euler-Lagrange expression of phi); this is the identity of the invariance of the action under coordinate changes"];
  (* local Lorentz: lambda_ab = 1 = -lambda_ba; the 28 test expressions are built here, their zero tests run on the subkernels (pS) *)
  okL = And @@ pS[st, Flatten[Table[Module[{dP, dPc, t1, elL},
      dP = rftS[[a, b]]; dPc = rftS[[a, b]];
      t1 = sScal[st, sg, sAdd[st, {sScal[st, eta[[a, a]] f[[b]], Tb[b, a]], sScal[st, -eta[[b, b]] f[[a]], Tb[a, b]]}]];
      elL = If[st === "C",
        Total[Table[ELp[{st, A}] (dP . (ph[#] @@ X & /@ Range[16]))[[A]] + ELc[{st, A}] (dPc . (phc[#] @@ X & /@ Range[16]))[[A]], {A, 16}]],
        gAdd[Flatten[Table[{gScal[(dP . Table[ph[B, k] @@ X, {B, 16}])[[A]], ELp[{st, A, k}]], gScal[(dPc . Table[phc[B, k] @@ X, {B, 16}])[[A]], ELc[{st, A, k}]]}, {A, 16}, {k, rftGN}]]]];
      sAdd[st, {t1, elL}]], {a, 8}, {b, a + 1, 8}], 1]];
  addCheck["Noether_identity_local_Lorentz_" <> st, okL,
    "for all 28 frame rotations lambda_ab = -lambda_ba (" <> statName[st] <> ", off shell): sqrt g T^mu_a lambda^a_c e^c_mu + sum_phi EL_phi delta phi = 0 with delta e^a_mu = lambda^a_c e^c_mu, delta Psi = +(1/2) lambda_ab S^ab Psi, delta Psibar = -(1/2) lambda_ab Psibar S^ab (the spinor rotation that keeps Psibar gamma^mu Psi invariant): " <>
    "the antisymmetric part T^[ab] is a combination of the Euler-Lagrange expressions, so T^mu_nu is symmetric on shell and equals T_sym"]];

section["EMT components, statistics " <> st];
Module[{P = fld[st]["Psi"], Pc = fld[st]["Psic"], L0 = Ldata[st]["L0"], Tsym = Tdata[st]["Tsym"], K, okDiag, S = Ldata[st]["S"], E1 = Ldata[st]["E"], Eb = Ldata[st]["Ebar"], okK, B40, B04, ok},
  K[mu_] := sScal[st, 1/(2 f[[mu]]), sAdd[st, {bilM[st, Pc, g[[mu]], vD[st, P, X[[mu]]]], sScal[st, -1, sDot[st, vecMat[st, vD[st, rftPsibar[st, Pc], X[[mu]]], g[[mu]]], P]]}]];
  okDiag = And @@ pS[st, Flatten[Table[{sAdd[st, {Tsym[[mu, mu]], sScal[st, -1, L0], K[mu]}], sAdd[st, {Tdata[st]["Tvar"][[mu, mu]], sScal[st, -1, Tsym[[mu, mu]]]}]}, {mu, 8}], 1]];
  addCheck["T_diagonal_components_" <> st, okDiag,
    "T^mu_mu (no sum) = L0 - K_mu with K_mu = (1/(2 f_mu)) (Psibar gamma^(mu) d_mu Psi - d_mu Psibar gamma^(mu) Psi) (f_4 = Sin[z]^(1/6), f_5..7 = E^-a4 b4^(1/2) Sin[z]^(1/6)): no spin-connection term survives in the diagonal components " <>
    "(Psibar {gamma^mu, Omega_mu} Psi = 0); the variation tensor and T_sym agree on the diagonal (" <> statName[st] <> ")"];
  okK = sZeroQ[st, sAdd[st, {L0, sScal[st, -1, sAdd[st, Table[K[mu], {mu, 8}]]], sScal[st, m, S], rftPot[st, S]}]] &&
    sZeroQ[st, sAdd[st, {sAdd[st, Table[K[mu], {mu, 8}]], sScal[st, -1/2, sDot[st, rftPsibar[st, Pc], E1]], sScal[st, 1/2, sDot[st, Eb, P]],
      sScal[st, -1, If[st === "C", (m + U'[S]) S, gMul[sAdd[st, {gScalar[m + u1], gScal[lam, S]}], S]]]}]];
  addCheck["EMT_trace_" <> st,
    sZeroQ[st, sAdd[st, {sAdd[st, Table[Tsym[[mu, mu]], {mu, 8}]], sScal[st, -7, sAdd[st, Table[K[mu], {mu, 8}]]], sScal[st, 8 m, S], sScal[st, 8, rftPot[st, S]]}]],
    "trace T^mu_mu (sum) = 7 sum_mu K_mu - 8 (m S + U(S)) exactly (" <> statName[st] <> "); with kinetic_sum_on_shell it is -m S + 7 S U' - 8 U on shell"];
  addCheck["kinetic_sum_on_shell_" <> st, okK,
    "L0 = sum_mu K_mu - m S - U(S) and sum_mu K_mu = (m + U'(S)) S + (1/2)(Psibar E - Ebar Psi) exactly (" <> statName[st] <> "): on shell the total kinetic term is (m + U'(S)) S and L0 = S U'(S) - U(S)"];
  (* Wolfram positions: x4 = 5, x0 = 1 *)
  B40 = sAdd[st, {bilM[st, Pc, g[[5]], vD[st, P, x0]], sScal[st, -1, sDot[st, vecMat[st, vD[st, rftPsibar[st, Pc], x0], g[[5]]], P]]}];
  B04 = sAdd[st, {bilM[st, Pc, g[[1]], vD[st, P, x4]], sScal[st, -1, sDot[st, vecMat[st, vD[st, rftPsibar[st, Pc], x4], g[[1]]], P]]}];
  ok = sZeroQ[st, sAdd[st, {Tsym[[5, 1]], sScal[st, 1/(4 wf), B40], sScal[st, -Cot[rftZ]/(4 wf^2), B04]}]] &&
       sZeroQ[st, sAdd[st, {Tsym[[1, 5]], sScal[st, wf^2 Tan[rftZ]^2, Tsym[[5, 1]]]}]];
  addCheck["T_x4_x0_component_" <> st, ok,
    "T^x4_x0 = -(1/4) Sin[z]^(-1/6) (B40 - Cot[z] Sin[z]^(-1/6) B04), B40 = Psibar gamma^(x4) d0 Psi - d0 Psibar gamma^(x4) Psi, B04 = Psibar gamma^(x0) d4 Psi - d4 Psibar gamma^(x0) Psi " <>
    "(the spin connection Omega_x4 = (1/2) H Sin[z]^(1/6) gamma^(x0) gamma^(x4) of the warped time drops out: {gamma^(x0), gamma^(x0) gamma^(x4)} = 0), and T^x0_x4 = g^00 g_44 T^x4_x0 = -Sin[z]^(1/3) Tan[z]^2 T^x4_x0 (" <> statName[st] <> ")"]];
If[st === "C",
  addFormulaText["T_variation", "energy-momentum tensor from the vielbein variation (both statistics), T^nu_mu = e^b_mu (1/sqrt g) dS/de^b_nu, L0 = L/sqrt g",
    "T^nu_mu = delta^nu_mu L0 - (1/2) (Psibar gamma^nu D_mu Psi - D_mu Psibar gamma^nu Psi) - (1/4) g_mu,rho nabla_l (Psibar {gamma^l, Sigma^(nu rho)} Psi), Sigma^(nu rho) = (1/4) [gamma^nu, gamma^rho]"];
  addFormulaText["T_symmetric", "symmetric (Belinfante) energy-momentum tensor = symmetric part of the variation tensor = the variation tensor on shell",
    "T^nu_mu = delta^nu_mu L0 - (1/4) (Psibar gamma^nu D_mu Psi - D_mu Psibar gamma^nu Psi + Psibar gamma_mu D^nu Psi - D^nu Psibar gamma_mu Psi)"];
  addFormulaText["EMT_diagonal", "diagonal components (no sum), both statistics; K_mu = kinetic term of direction mu",
    "K_mu = (1/(2 f_mu)) (Psibar gamma^(mu) d_mu Psi - d_mu Psibar gamma^(mu) Psi); L0 = sum_mu K_mu - m S - U(S); T^mu_mu = L0 - K_mu; rho = -T^x4_x4 = -sum_(mu != x4) K_mu + m S + U; p3 = T^x1_x1 (= T^x2_x2 = T^x3_x3 for isotropic states) = sum_(mu != x1) K_mu - m S - U; p_t = T^x5_x5 = sum_(mu != x5) K_mu - m S - U; p0 = T^x0_x0 = sum_(mu != x0) K_mu - m S - U"];
  addFormulaText["EMT_kinetic_potential", "split into kinetic (derivative) and potential parts",
    "T^nu_mu = T_kin^nu_mu + T_pot^nu_mu, T_pot^nu_mu = -delta^nu_mu (m S + U(S)), T_kin^nu_mu = delta^nu_mu sum_l K_l - (1/4)(Psibar gamma^nu D_mu Psi - D_mu Psibar gamma^nu Psi + Psibar gamma_mu D^nu Psi - D^nu Psibar gamma_mu Psi); potential energy density rho_pot = m S + U, potential pressure p_pot = -(m S + U) in every direction"];
  addFormulaText["EMT_trace", "trace",
    "T^mu_mu (sum) = 8 L0 - sum_mu K_mu = 7 sum_mu K_mu - 8 (m S + U); on shell = 7 (m + U') S - 8 (m S + U) = -m S + 7 S U' - 8 U"];
  addFormulaText["EMT_homogeneous_on_shell", "configurations that depend on x4 only (in the warped metric they exist only with lam S = 0 and m = +-7 H/2, check homogeneous_configurations_warped): K_mu = 0 for mu != x4 and K_x4 = (m + U') S on shell",
    "rho = m S + U(S); p3 = p_t = p0 = S U'(S) - U(S) (the kinetic-sum identity); at the x4-only solutions of the warped metric S = 0, so rho = p = 0 and the whole diagonal vanishes"];
  addFormulaText["EMT_offdiagonal_x4_x0", "the x4-x0 component of the symmetric tensor (Omega_x0 = 0; Omega_x4 drops out)",
    "T^x4_x0 = -(1/4) Sin[z]^(-1/6) (B40 - Cot[z] Sin[z]^(-1/6) B04), B40 = Psibar gamma^(x4) d0 Psi - d0 Psibar gamma^(x4) Psi, B04 = Psibar gamma^(x0) d4 Psi - d4 Psibar gamma^(x0) Psi; T^x0_x4 = -Sin[z]^(1/3) Tan[z]^2 T^x4_x0 (T_x4x0 = T_x0x4)"]];
];

(* ================================================================== PART solutions *)
(* The exact solutions used as test points in the warped metric (2026-10-16).  With y = Log[Sin z]/(6 H) and the conformal
   coordinate zeta = Sin[z]^(-1/6)/H of the hidden direction, Psi = b4^(-3/4) Sin[z]^(-7/12) PsiT turns the field equation with
   U = 0 into gamma^(x0) d_zeta PsiT + (m/(H zeta)) PsiT = gamma^(x4) d4 PsiT.  Two families follow in closed form:
     static (d4 PsiT = 0), any m:  PsiT = (zeta^(-m/H) P+ + zeta^(m/H) P-) chi, i.e.
       Psi = b4^(-3/4) Sin[z]^(-7/12) (Sin[z]^(m/(6H)) P+ + Sin[z]^(-m/(6H)) P-) chi,   P+- = (1 +- gamma^(x0))/2;
     travelling, m = 0:  PsiT = (f(x4 + zeta) Q+ + g(x4 - zeta) Q-) chi with arbitrary profiles f, g,   Q+- = (1 +- gamma^(x0) gamma^(x4))/2.
   With chi in the range of P+ (static) or of Q+ (travelling) the scalar S vanishes identically (P+^T C P+ = Q+^T C Q+ = 0), so
   these are also exact solutions for every potential U with U'(0) = 0, in particular U = (lam/2) S^2. *)
If[MemberQ[{"solutions", "solutions-G"}, part],
section["exact solutions: definitions"];
Pp = (id16 + g[[1]])/2; Pmn = (id16 - g[[1]])/2; Nm = g[[1]] . g[[5]]; Qp = (id16 + Nm)/2; Qmn = (id16 - Nm)/2;
zeta = Sin[rftZ]^(-1/6)/H;
staticProf[mm_] := b4[x4]^(-3/4) Sin[rftZ]^(-7/12) (Sin[rftZ]^(mm/(6 H)) Pp + Sin[rftZ]^(-mm/(6 H)) Pmn);
travProf[f1_, f2_] := b4[x4]^(-3/4) Sin[rftZ]^(-7/12) (f1[x4 + zeta] Qp + f2[x4 - zeta] Qmn);
If[part === "solutions", addCheck["solution_projectors",
  Pp . Pp == Pp && Pmn . Pmn == Pmn && Pp + Pmn == id16 && Qp . Qp == Qp && Qmn . Qmn == Qmn && Qp + Qmn == id16 &&
  Nm . Nm == id16 && Transpose[g[[1]]] == g[[1]] && Transpose[Nm] == Nm &&
  Transpose[Pp] . Cm . Pp == z16 && Transpose[Pmn] . Cm . Pmn == z16 && Transpose[Qp] . Cm . Qp == z16 && Transpose[Qmn] . Cm . Qmn == z16 &&
  Cm . Pp == Pmn . Cm && Cm . Qp == Qmn . Cm && g[[1]] . Pp == Pp && Nm . Qp == Qp,
  "P+- = (1 +- gamma^(x0))/2 and Q+- = (1 +- gamma^(x0) gamma^(x4))/2 are complementary projectors (gamma^(x0) and N = gamma^(x0) gamma^(x4) are real symmetric with square 1); " <>
  "C anticommutes with gamma^(x0) and with N, so C P+- = P-+ C, C Q+- = Q-+ C and P+-^T C P+- = Q+-^T C Q+- = 0: a column in the range of one projector has chi^T C chi' = 0 for all chi, chi' in that range"]];
(* T_sym, divergence for a given explicit field *)
TsymOf[st_, P_, Pc_] := Module[{pb = rftPsibar[st, Pc], L0, Bm2},
  L0 = rftL0[st, rftGeo0, P, Pc];
  Bm2 = Table[sAdd[st, {sDot[st, vecMat[st, pb, gup[[r]]], rftDPsi[st, rftGeo0, P, s]], sScal[st, -1, sDot[st, vecMat[st, rftDPsibar[st, rftGeo0, Pc, s], gup[[r]]], P]]}], {r, 8}, {s, 8}];
  Table[sAdd[st, {If[n == mu, L0, sZero[st]], sScal[st, -1/4, Bm2[[n, mu]]], sScal[st, -1/4 rftG0[[mu, mu]] rftGinv0[[n, n]], Bm2[[mu, n]]]}], {n, 8}, {mu, 8}]];
divT[st_, T_] := Table[sAdd[st, {
    sScal[st, 1/sg, sAdd[st, Table[sD[st, sScal[st, sg, T[[mu, nu]]], X[[mu]]], {mu, 8}]]],
    sScal[st, -1, sAdd[st, Flatten[Table[If[Gm[[r, mu, nu]] === 0, sZero[st], sScal[st, Gm[[r, mu, nu]], T[[mu, r]]]], {mu, 8}, {r, 8}]]]]}], {nu, 8}];
(* the field of a statistics for a 16 x 16 profile matrix pr (commuting: constants cA; Grassmann: cA[.., k] per generator) *)
fieldOf["C", pr_] := pr . Table[cA[A], {A, 16}];
fieldCOf["C", pr_] := pr . Table[cAc[A], {A, 16}];
fieldOf["G", pr_] := Table[gAdd[Table[<|{k} -> (pr . Table[cA[B, k], {B, 16}])[[A]]|>, {k, rftGN}]], {A, 16}];
fieldCOf["G", pr_] := Table[gAdd[Table[<|{k + rftGN} -> (pr . Table[cAc[B, k], {B, 16}])[[A]]|>, {k, rftGN}]], {A, 16}];
(* the scalar S of a column field pr chi expected from the profile: B[Y] = sum_kl thetabar_k theta_l c_k^dagger Y c_l (Grassmann) *)
bilOf["C", Y_] := Table[cAc[A], {A, 16}] . Y . Table[cA[A], {A, 16}];
bilOf["G", Y_] := gAdd[Flatten[Table[gMul[<|{k1 + rftGN} -> 1|>, <|{k2} -> Table[cAc[B, k1], {B, 16}] . Y . Table[cA[B, k2], {B, 16}]|>], {k1, rftGN}, {k2, rftGN}]]];
(* field equation, conservation of T_sym, conservation of the current and S at an explicit field: the zero tests run on the subkernels *)
solutionTests[st_, Psol_, Pcsol_, Sexp_] := Module[{Eres, T, dv, J, divJ, Sx},
  Eres = rftE[st, rftGeo0, Psol, Pcsol];
  T = TsymOf[st, Psol, Pcsol];
  dv = divT[st, T];
  J = Table[sScal[st, -I, bilM[st, Pcsol, gup[[mu]], Psol]], {mu, 8}];
  divJ = sAdd[st, Table[sD[st, sScal[st, sg, J[[mu]]], X[[mu]]], {mu, 8}]];
  Sx = rftSbil[st, Psol, Pcsol];
  {pS[st, Join[Eres, dv, {divJ, sAdd[st, {Sx, sScal[st, -1, Sexp]}]}]], T}];
];

If[part === "solutions",
section["exact solutions (i): static, any m, U = 0"];
Block[{U = Function[s, lam s^2/2], u1 = 0},
  Do[Module[{prof = staticProf[mm], Psol, Pcsol, res, zr, T, offd},
    Block[{lam = 0, m = mm},
      Psol = fieldOf[st, prof]; Pcsol = fieldCOf[st, prof];
      res = solutionTests[st, Psol, Pcsol, sScal[st, b4[x4]^(-3/2) Sin[rftZ]^(-7/6), bilOf[st, Cm]]];
      zr = res[[1]]; T = res[[2]];
      offd = Count[Flatten[Table[If[n != mu, sZeroQ[st, T[[n, mu]]], True], {n, 8}, {mu, 8}]], False]];
    addCheck["exact_solution_static_" <> st, And @@ zr && offd > 0,
      "exact solution (" <> statName[st] <> ", U = 0, any mass m, general a4 and b4): Psi = b4^(-3/4) Sin[z]^(-7/12) (Sin[z]^(m/(6 H)) P+ + Sin[z]^(-m/(6 H)) P-) chi with constant chi " <>
      "(16 free complex constants" <> If[st === "G", " per Grassmann generator", ""] <> "), P+- = (1 +- gamma^(x0))/2: it satisfies the field equation for all functions a4 and b4 " <>
      "(a test of Tan[z] gamma^(x0) d0, (7/2) H gamma^(x0) and (3/4)(b4'/b4) Sin[z]^(-1/6) gamma^(x4), the latter compensated by b4^(-3/4)), nabla_mu T_sym^mu_nu = 0 for all 8 nu and d_mu(sqrt g J^mu) = 0 hold exactly at it, " <>
      "and S = b4^(-3/2) Sin[z]^(-7/6) chi^dagger C chi. Honest scope: its energy-momentum tensor has " <> ToString[offd] <> " nonzero off-diagonal components (spin-connection bilinears), so it is NOT a diagonal source"]],
    {st, stats}];
  section["exact solutions (ii): travelling, m = 0, U = 0"];
  Do[Module[{prof = travProf[pf, qf], profc = travProf[pfc, qfc], Psol, Pcsol, res, zr},
    Block[{lam = 0, m = 0},
      Psol = fieldOf[st, prof]; Pcsol = fieldCOf[st, profc];
      res = solutionTests[st, Psol, Pcsol, sScal[st, b4[x4]^(-3/2) Sin[rftZ]^(-7/6),
        bilOf[st, (pfc[x4 + zeta] Transpose[Qp] + qfc[x4 - zeta] Transpose[Qmn]) . Cm . (pf[x4 + zeta] Qp + qf[x4 - zeta] Qmn)]]];
      zr = res[[1]]];
    addCheck["exact_solution_travelling_" <> st, And @@ zr,
      "exact solution (" <> statName[st] <> ", U = 0, m = 0, general a4 and b4): Psi = b4^(-3/4) Sin[z]^(-7/12) (f(x4 + zeta) Q+ + g(x4 - zeta) Q-) chi, zeta = Sin[z]^(-1/6)/H, Q+- = (1 +- gamma^(x0) gamma^(x4))/2, " <>
      "with ARBITRARY profiles f, g (and conjugate profiles treated as independent functions): the field equation, nabla_mu T_sym^mu_nu = 0 for all 8 nu, d_mu(sqrt g J^mu) = 0 and the value of S hold exactly: " <>
      "waves that travel along x4 in the conformal coordinate zeta of the hidden direction (the warped time makes x4 and zeta a flat pair)"]],
    {st, stats}];
  section["exact solutions (iii): nonlinear, S = 0, commuting"];
  Module[{prS = staticProf[mm] . Pp, prT = travProf[pf, qf] . Qp, prTc = travProf[pfc, qfc] . Qp, okS, okT, resS, resT},
    Block[{m = mm}, resS = solutionTests["C", fieldOf["C", prS], fieldCOf["C", prS], 0]];
    Block[{m = 0}, resT = solutionTests["C", fieldOf["C", prT], fieldCOf["C", prTc], 0]];
    okS = And @@ resS[[1]]; okT = And @@ resT[[1]];
    addCheck["exact_solution_nonlinear_S0_C", okS && okT,
      "nonlinear solutions of dirac16complex00 with U = (lam/2) S^2 (any lam), general a4 and b4: the static solution with chi = P+ chi (any m) and the travelling solution with chi = Q+ chi (m = 0) have S = Psibar Psi = 0 identically " <>
      "(P+^T C P+ = Q+^T C Q+ = 0), hence U'(S) = 0 and they solve the nonlinear field equation exactly; nabla_mu T^mu_nu = 0 and d_mu(sqrt g J^mu) = 0 hold at them. " <>
      "Solutions with S != 0 and lam != 0 are not in closed form: for S != 0 the effective mass m + lam S depends on x0 and x4"]];
  section["configurations that depend on x4 only"];
  Module[{Phi = Table[ph[A][x4], {A, 16}], Phic = Table[phc[A][x4], {A, 16}], Eg, idt, solP, solPc, Eh, Sh, Th, offd, diag0},
    Eg = rftE["C", rftGeo0, Phi, Phic];
    idt = wf Eg - (g[[5]] . (D[Phi, x4] + (3/4) bu Phi) - wf ((m + U'[Phic . Cm . Phi]) Phi - (7/2) H g[[1]] . Phi));
    solP = b4[x4]^(-3/4) Pp . Table[cA[A], {A, 16}]; solPc = b4[x4]^(-3/4) Pp . Table[cAc[A], {A, 16}];
    Block[{m = 7 H/2}, Eh = rftE["C", rftGeo0, solP, solPc]; Th = TsymOf["C", solP, solPc]];
    Sh = rftSbil["C", solP, solPc];
    diag0 = And @@ Table[rftZeroQ[Th[[mu, mu]]], {mu, 8}];
    offd = Select[Flatten[Table[{n, mu}, {n, 8}, {mu, 8}], 1], #[[1]] != #[[2]] && !rftZeroQ[Th[[#[[1]], #[[2]]]]] &];
    addCheck["homogeneous_configurations_warped",
      rftZeroQ[idt] && rftZeroQ[Eh] && rftZeroQ[Sh] && diag0 && Length[offd] == 18 &&
      Sort[Union[Sort /@ offd]] == Sort[Flatten[Table[{i, t}, {i, 2, 4}, {t, 6, 8}], 1]],
      "for a field Phi(x4) that depends on x4 only, Sin[z]^(1/6) E = gamma^(x4) (d4 + (3/4) b4'/b4) Phi - Sin[z]^(1/6) (V - (7/2) H gamma^(x0)) Phi exactly (V = m + U'(S)): " <>
      "both brackets are independent of x0 and Sin[z]^(1/6) is not constant, so the field equation needs (d4 + (3/4) b4'/b4) Phi = 0 and (V - (7/2) H gamma^(x0)) Phi = 0, i.e. Phi = b4^(-3/4) chi with constant chi, gamma^(x0) chi = +-chi and V = +-7 H/2 constant; " <>
      "since then S = b4^(-3/2) chi^T C chi = 0 (P+-^T C P+- = 0), U'(0) = 0 and the mass must be m = +-7 H/2. The explicit case m = 7 H/2, chi = P+ chi: field equation exact, S = 0, all 8 diagonal components of T vanish (rho = p = 0), " <>
      "and 18 off-diagonal components remain, exactly the pairs (xi, xt) of a 3-space direction and an extra time (spin-connection bilinears): in the warped metric no x4-only configuration carries energy density or pressure"]];
];
addFormulaText["exact_solutions",
  "exact solutions used as test points (checks exact_solution_*), general a4 and b4, warped metric; zeta = Sin[z]^(-1/6)/H, P+- = (1 +- g[x0])/2, Q+- = (1 +- g[x0].g[x4])/2",
  "(i) U = 0, any m: Psi = b4^(-3/4) Sin[z]^(-7/12) (Sin[z]^(m/(6 H)) P+ + Sin[z]^(-m/(6 H)) P-) chi; " <>
  "(ii) U = 0, m = 0: Psi = b4^(-3/4) Sin[z]^(-7/12) (f(x4 + zeta) Q+ + g(x4 - zeta) Q-) chi, f, g arbitrary; " <>
  "(iii) U = (lam/2) S^2, any lam: (i) with chi = P+ chi and (ii) with chi = Q+ chi have S = 0 and solve the nonlinear equation (both statistics); " <>
  "x4-only configurations exist only for V = +-7 H/2 with S = 0 (m = +-7 H/2): Psi = b4^(-3/4) chi, g[x0] chi = +-chi; their diagonal energy-momentum tensor vanishes"];
];

(* ================================================================== PART solutions-G *)
If[part === "solutions-G",
section["exact solutions (iii): nonlinear, S = 0, Grassmann"];
Block[{U = Function[s, lam s^2/2], u1 = 0},
  Module[{prS = staticProf[mm] . Pp, prT = travProf[pf, qf] . Qp, prTc = travProf[pfc, qfc] . Qp, resS, resT, okS, okT, bilChk},
    Block[{m = mm}, resS = solutionTests["G", fieldOf["G", prS], fieldCOf["G", prS], <||>]];
    Block[{m = 0}, resT = solutionTests["G", fieldOf["G", prT], fieldCOf["G", prTc], <||>]];
    okS = And @@ resS[[1]]; okT = And @@ resT[[1]];
    bilChk = !gZeroQ[rftSbil["G", fieldOf["G", staticProf[mm]], fieldCOf["G", staticProf[mm]]]];
    addCheck["exact_solution_nonlinear_S0_G", okS && okT && bilChk,
      "nonlinear solutions of dirac16complex (explicit Grassmann algebra, N = 2) with U = (lam/2) S^2 (any lam), general a4 and b4: Psi = sum_k Prof c_k theta_k with the static profile restricted to P+ (any m) " <>
      "or the travelling profile restricted to Q+ (m = 0) has S = Psibar Psi = 0 as a Grassmann element (P+^T C P+ = Q+^T C Q+ = 0), so it solves the nonlinear field equation exactly; nabla_mu T^mu_nu = 0 (all 8 nu) " <>
      "and d_mu(sqrt g J^mu) = 0 hold at it. Control: with the unrestricted static profile S != 0"]]];
];

(* ================================================================== PART quantisation *)
If[part === "quantisation",
section["canonical quantisation"];
Ldata = lagData[{"G"}];
Module[{LG = Ldata["G"]["L"], okPi = True, K, piRow},
  (* Wolfram position 5 = x4, the time *)
  piRow = vScal["G", sg/(2 wf), vecMat["G", fld["G"]["Psic"], Cm . g[[5]]]];
  Do[okPi = okPi && gZeroQ[gAdd[{rftPartialD["G", LG, ph[A, k], 5], gScal[-1, gMul[piRow[[A]], gTheta[k]]]}]], {A, 16}, {k, rftGN}];
  addCheck["canonical_momentum",
    okPi && Cm . g[[5]] == I Bm && rftZeroQ[sg/wf - b4[x4]^(3/2) Cos[rftZ]],
    "dL/d(d4 ph[A,k]) = pi_A theta_k with pi_A = (1/2) (sqrt g/f4) (Psi^dagger C gamma^(x4))_A = (i/2) b4^(3/2) Cos[z] (Psi^dagger B)_A (the momentum conjugate to Psi_A as a right derivative; C gamma^(x4) = i B; the lapse f4 = Sin[z]^(1/6) cancels the warp of sqrt g): " <>
    "pi depends on Psi^dagger only, a second-class constraint as for Dirac's field"];
  K = (sg/wf) Cm . g[[5]];
  addCheck["first_order_form_and_anticommutator",
    ConjugateTranspose[Cm . g[[5]]] == -Cm . g[[5]] && I Inverse[Cm . g[[5]]] == Bm && Bm . Bm == id16 && rftZeroQ[K - I b4[x4]^(3/2) Cos[rftZ] Bm],
    "up to a total divergence L = Psi^dagger K d4 Psi - (terms without d4), K = (sqrt g/f4) C gamma^(x4) = i b4^(3/2) Cos[z] B (C gamma^(x4) anti-Hermitian with i (C gamma^(x4))^-1 = B; invertible since g^44 != 0); " <>
    "the canonical (Dirac-bracket) anticommutator is {Psi_A(x), Psi^dagger_C(y)} = i (K^-1)_AC delta^7(x - y) = B_AC delta^7(x - y)/(b4^(3/2) Cos[z]) on a slice x4 = const (exact: i K^-1 = B/(b4^(3/2) Cos[z]); the measure of the slice divided by the lapse)"]];
(* Heisenberg equation reproduces the field equation *)
Module[{Phi = rftField["C"], Phic = rftFieldC["C"], Hd, flow, d4sol, ok, S},
  S = Phic . Cm . Phi;
  Hd = sg (Phic . (m Cm) . Phi - Sum[If[a == 5, 0, Phic . Cm . gup[[a]] . (D[Phi, X[[a]]] + Om[[a]] . Phi)], {a, 8}] - Phic . Cm . gup[[5]] . Om[[5]] . Phi + U[S]);
  flow = Table[-I Sum[Bm[[A, Cc]] rftVarDerExpr[Hd, phc[Cc]] wf/sg, {Cc, 16}], {A, 16}];
  d4sol = -wf g[[5]] . ((m + U'[S]) Phi - Sum[If[a == 5, 0, gup[[a]] . (D[Phi, X[[a]]] + Om[[a]] . Phi)], {a, 8}] - gup[[5]] . Om[[5]] . Phi);
  ok = rftZeroQ[flow - d4sol] && rftZeroQ[Simplify[rftLagUnsym["C", rftGeo0, Phi, Phic] - (Phic . ((sg/wf) Cm . g[[5]]) . D[Phi, x4] - Hd)]] &&
    rftZeroQ[g[[5]] . Sum[If[a == 5, 0, gup[[a]] . Om[[a]]], {a, 8}] - (3 H g[[5]] . g[[1]] - (3/4) bu wf^-1 id16)] &&
    rftZeroQ[gup[[5]] . Om[[5]] - (H/2) g[[1]]];
  addCheck["Heisenberg_equation_reproduces_field_equation", ok,
    "with the Hamiltonian density Hd = sqrt g [Psi^dagger (m C - sum_(a != x4) C gamma^a D_a - C gamma^(x4) Omega_x4) Psi + U(S)], sqrt g = b4^(3/2) Cos[z] Sin[z]^(1/6) (so that the unsymmetrised L = Psi^dagger K d4 Psi - Hd exactly; " <>
    "the spin connection Omega_x4 of the warped time has no time derivative and belongs to Hd) and {Psi, Psi^dagger} = B delta^7 f4/sqrt g, " <>
    "the Heisenberg equation d4 Psi = i[H, Psi] = -i B (f4/sqrt g) dHd/dPsi^dagger equals -Sin[z]^(1/6) gamma^(x4) [(m + U'(S)) Psi - sum_(a != x4) gamma^a D_a Psi - gamma^(x4) Omega_x4 Psi], the field equation solved for d4 Psi (exact, general U; " <>
    "the operator ordering of U'(S) Psi is that of the classical expression); the spin connection of the six warped slice directions contributes gamma^(x4) sum_(a != x4) gamma^a Omega_a = 3 H gamma^(x4) gamma^(x0) - (3/4)(b4'/b4) Sin[z]^(-1/6) " <>
    "and the warped time gamma^(x4) Omega_x4 = (H/2) gamma^(x0): the term -(3/4)(b4'/b4) Psi of the evolution form comes from the extra-time spin connection"]];
Module[{ev = Eigenvalues[Bm], um, vneg},
  vneg = First[Select[NullSpace[Bm + id16], True &]];
  um = vneg/Sqrt[Conjugate[vneg] . vneg];
  addCheck["no_positive_inner_product",
    ConjugateTranspose[Bm] == Bm && Count[ev, 1] == 8 && Count[ev, -1] == 8 && Simplify[Conjugate[um] . Bm . um] == -1,
    "B is Hermitian with eigenvalues +1 (8 times) and -1 (8 times); for the exact unit vector u = " <> wl[um] <> " (B u = -u) the smeared operator X = sum_A u_A^* Psi_A(f) has {X, X^dagger} = (u^dagger B u) ||f||^2 = -||f||^2. " <>
    "If Psi^dagger were the adjoint in a space with positive inner product, {X, X^dagger} = X X^dagger + X^dagger X would be a positive operator (<phi|{X,X^dagger}|phi> = ||X^dagger phi||^2 + ||X phi||^2 >= 0): contradiction. " <>
    "Hence the canonical anticommutator in signature (4,4) forces an indefinite (Krein) inner product; the positive representation uses the Hilbert adjoint chi = Psi^dagger B with {Psi_A, chi_C} = (B B)_AC = delta_AC"]];
(* good sector, flat frozen coefficients *)
(* Wolfram positions: x0 = 1, x1, x2, x3 = 2, 3, 4, x4 = 5, x5, x6, x7 = 6, 7, 8; kv[p] is the momentum along the coordinate of position p *)
Module[{beta = -I g[[5]], al, hk, okH},
  al[a_] := -g[[5]] . g[[a]];
  hk = mm beta + Sum[kv[a] al[a], {a, {1, 2, 3, 4, 6, 7, 8}}];
  okH = ConjugateTranspose[beta] == beta && And @@ Table[ConjugateTranspose[al[a]] == al[a], {a, {1, 2, 3, 4}}] &&
    And @@ Table[ConjugateTranspose[al[a]] == -al[a], {a, {6, 7, 8}}] &&
    And @@ Flatten[Table[al[a] . al[b] + al[b] . al[a] == 2 KroneckerDelta[a, b] (-eta[[5, 5]] eta[[a, a]]) id16, {a, {1, 2, 3, 4, 6, 7, 8}}, {b, {1, 2, 3, 4, 6, 7, 8}}]] &&
    And @@ Table[beta . al[a] + al[a] . beta == z16, {a, {1, 2, 3, 4, 6, 7, 8}}] && beta . beta == id16;
  addCheck["mode_hamiltonian_good_sector",
    okH && Expand[hk . hk - (mm^2 + kv[1]^2 + kv[2]^2 + kv[3]^2 + kv[4]^2 - kv[6]^2 - kv[7]^2 - kv[8]^2) id16] == z16 && Tr[hk] == 0,
    "frozen-coefficient (flat-frame) plane waves Psi = u exp(i k.x - i E x4): E u = h_k u with h_k = m beta + sum_a k_a alpha^a, beta = -i gamma^(x4), alpha^a = -gamma^(x4) gamma^a (k_a the momenta in the orthonormal frame); " <>
    "beta and alpha^(x0,x1,x2,x3) are Hermitian, alpha^(x5,x6,x7) anti-Hermitian, {alpha^a, alpha^b} = 2 delta^ab (-eta^44 eta^aa), {alpha, beta} = 0, beta^2 = 1; h_k^2 = (m^2 + k0^2 + k1^2 + k2^2 + k3^2 - k5^2 - k6^2 - k7^2) I, Tr h_k = 0. " <>
    "In the GOOD SECTOR (k5 = k6 = k7 = 0, nothing depends on the extra times) h_k is Hermitian with real eigenvalues +-E (8 each); with extra-time momentum E^2 = m^2 + k_s^2 - k_t^2 is negative for k_t^2 > m^2 + k_s^2: those modes grow exponentially in x4"];
  addCheck["mode_hamiltonian_Krein_selfadjoint",
    Expand[Bm . hk - (ConjugateTranspose[hk] /. Conjugate[q_] :> q) . Bm] == z16 &&
    Bm . (mm Cm) == mm beta && And @@ Table[Bm . (-I Cm . g[[a]]) == al[a], {a, {1, 2, 3, 4, 6, 7, 8}}],
    "B h_k = h_k^dagger B for all real m, k (h_k^dagger taken with m, k real; the Krein norm u^dagger B u is conserved by every mode, also those that grow); the mode Hamiltonian density is Psi^dagger (m C - i C k_a gamma^a) Psi = chi h_k Psi with chi = Psi^dagger B (B m C = m beta, B (-i C gamma^a) = alpha^a)"]];
(* curved good sector: weighted Hermiticity, the role of 3 H gamma^(x0) and of the b4 term; Wolfram positions x0 = 1, x4 = 5.
   h is the operator of i d4 Psi = h Psi (U = 0) read off the evolution form, including the term -i (3/4)(b4'/b4). *)
Module[{u = Table[ph[A] @@ X, {A, 16}], uc = Table[phc[A] @@ X, {A, 16}], v = Table[qv[A] @@ X, {A, 16}], hOp, hOpC, Mm, lhs, divs, rest, lhsNoH, lhsB, divsB, dsg, msr},
  Mm[a_] := I g[[5]] . g[[a]];
  (* i d4 Psi = h Psi read off the evolution form of the warped metric (lapse wf = f4); mu = sqrt g/f4 = b4^(3/2) Cos[z] is the measure of the inner product *)
  hOp[w_, withH_] := wf (mm (-I g[[5]]) . w + Sum[If[a == 5, 0, (1/f[[a]]) Mm[a] . D[w, X[[a]]]], {a, 8}] + withH (7/2) H Mm[1] . w) - I (3/4) bu w;
  hOpC[w_, withH_] := wf (mm (I g[[5]]) . w + Sum[If[a == 5, 0, (1/f[[a]]) Conjugate[Mm[a]] . D[w, X[[a]]]], {a, 8}] + withH (7/2) H Conjugate[Mm[1]] . w) + I (3/4) bu w;
  msr = sg/wf;
  dsg = D[msr, x4];
  lhs = msr (uc . hOp[v, 1] - hOpC[uc, 1] . v);
  divs = Sum[D[msr wf/f[[a]] uc . Mm[a] . v, X[[a]]], {a, {1, 2, 3, 4}}];
  rest = Sum[msr wf/f[[a]] (uc . Mm[a] . D[v, X[[a]]] - D[uc, X[[a]]] . Mm[a] . v), {a, {6, 7, 8}}];
  lhsNoH = msr (uc . hOp[v, 0] - hOpC[uc, 0] . v);
  addCheck["good_sector_hermiticity_curved",
    rftZeroQ[lhs - divs - rest + I dsg uc . v] && rftZeroQ[lhsNoH - divs - rest + I dsg uc . v + 7 H msr wf uc . Mm[1] . v] && rftZeroQ[dsg - (3/2) bu msr] &&
    rftZeroQ[msr - b4[x4]^(3/2) Cos[rftZ]] &&
    rftZeroQ[Cos[rftZ] wf (pf[x0] (Tan[rftZ] D[qf[x0], x0] + (7/2) H qf[x0]) + (Tan[rftZ] D[pf[x0], x0] + (7/2) H pf[x0]) qf[x0]) - D[Sin[rftZ]^(7/6) pf[x0] qf[x0], x0]],
    "the curved mode operator of the warped metric h = Sin[z]^(1/6) [m (-i gamma^(x4)) + sum_(a != x4) (1/f_a) i gamma^(x4) gamma^(a) d_a + (7/2) i H gamma^(x4) gamma^(x0)] - i (3/4)(b4'/b4) (i d4 Psi = h Psi for U = 0; the last term is anti-Hermitian) satisfies, for general u, v and the measure mu = sqrt g/f4 = b4^(3/2) Cos[z], " <>
    "mu (u^dagger h v - (h u)^dagger v) = sum_(a = x0,x1,x2,x3) d_a (mu Sin[z]^(1/6)/f_a u^dagger M_a v) + sum_(t = x5,x6,x7) (mu Sin[z]^(1/6)/f_t)(u^dagger M_t d_t v - d_t u^dagger M_t v) - i (d_x4 mu) u^dagger v, M_a = i gamma^(x4) gamma^(a), d_x4 mu = (3/2)(b4'/b4) mu: " <>
    "the anti-Hermitian term exactly compensates the x4 dependence of the measure, so in the GOOD SECTOR (no extra-time dependence) d/dx4 integral b4^(3/2) Cos[z] u^dagger v d^7x = boundary terms for solutions u, v " <>
    "(the same measure as the charge density; the x0 boundary term Sin[z]^(7/6) u^dagger M_0 v does not vanish at the patch end z = Pi/2, so Hermiticity needs a boundary condition there, see Revision/theory/reports/wolfram-scope.json); without the spin-connection term (7/2) H gamma^(x0) a remainder -7 H mu Sin[z]^(1/6) u^dagger M_0 v survives " <>
    "(Cos[z] Sin[z]^(1/6) [p (Tan z d0 + 7H/2) q + ((Tan z d0 + 7H/2) p) q] = d0 (Sin[z]^(7/6) p q)): the gravitational term makes the warped hidden-direction operator formally antisymmetric for this measure"];
  lhsB = msr (uc . Bm . hOp[v, 1] - hOpC[uc, 1] . Bm . v);
  divsB = Sum[If[a == 5, 0, D[msr wf/f[[a]] uc . Bm . Mm[a] . v, X[[a]]]], {a, 8}];
  addCheck["Krein_form_conserved_curved",
    rftZeroQ[lhsB - divsB + I dsg uc . Bm . v],
    "mu (u^dagger B h v - (h u)^dagger B v) = sum_(a != 4) d_a (mu Sin[z]^(1/6)/f_a u^dagger B M_a v) - i (d_x4 mu) u^dagger B v for general u, v (all seven slice directions; mu = b4^(3/2) Cos[z]): " <>
    "for solutions d/dx4 integral b4^(3/2) Cos[z] u^dagger B v d^7x = boundary terms, i.e. the Krein form is conserved in the whole theory up to these boundary terms (they need boundary conditions, in particular at the patch end z = Pi/2)"]];
(* explicit Fock space in the good sector: m = 3, k1 = 4, E = 5 *)
Module[{beta = -I g[[5]], al1, h, E0 = 5, up, vn, gs, U16, W, expect, vac, st1, std, okC, eH, Ms, okRule, okQ},
  al1 = -g[[5]] . g[[2]];   (* alpha^(x1): positions x4 = 5, x1 = 2 *)
  h = 3 beta + 4 al1;
  gs[vs_] := Module[{out = {}, w}, Do[w = v - Sum[(Conjugate[o] . v) o, {o, out}]; w = Simplify[w/Sqrt[Simplify[Conjugate[w] . w]]]; AppendTo[out, w], {v, vs}]; out];
  up = gs[NullSpace[h - E0 id16]]; vn = gs[NullSpace[h + E0 id16]];
  U16 = Transpose[Join[up, vn]];   (* columns u_0..u_7, v_0..v_7 *)
  okC = Simplify[U16 . ConjugateTranspose[U16]] == id16 && Length[up] == 8 && Length[vn] == 8;
  (* fermionic Fock space of 16 modes: mode p < 8 = b_p, mode 8 + s = d_s; a_p = b_p (p < 8), a_(8+s) = d_s^* *)
  annih[p_][state_Association] := Merge[KeyValueMap[Function[{s, c}, If[BitGet[s, p] == 1, <|s - 2^p -> (-1)^DigitCount[BitAnd[s, 2^p - 1], 2, 1] c|>, <||>]], state], Total];
  creat[p_][state_Association] := Merge[KeyValueMap[Function[{s, c}, If[BitGet[s, p] == 0, <|s + 2^p -> (-1)^DigitCount[BitAnd[s, 2^p - 1], 2, 1] c|>, <||>]], state], Total];
  aOp[p_] := If[p < 8, annih[p], creat[p]];
  aDag[p_] := If[p < 8, creat[p], annih[p]];
  inner[s1_Association, s2_Association] := Total[KeyValueMap[Function[{s, c}, Conjugate[c] Lookup[s2, s, 0]], s1]];
  expect[Wm_, state_] := Simplify[Sum[If[Wm[[p + 1, q + 1]] === 0, 0, Wm[[p + 1, q + 1]] inner[state, aDag[p][aOp[q][state]]]], {p, 0, 15}, {q, 0, 15}]];
  vac = <|0 -> 1|>; st1 = creat[0][vac]; std = creat[8][vac];
  W[M_] := Simplify[ConjugateTranspose[U16] . (Bm . M) . U16];   (* chi B M Psi = a^dagger (U^dagger B M U) a *)
  eH = W[Bm . h];   (* chi h Psi, i.e. M = B h *)
  Ms = {Cm, -I Cm . g[[5]], -I Cm . g[[2]], Cm . g[[3]] . g[[4]], Table[If[A <= Bv, Mod[3 A + 5 Bv, 7] - 3, Mod[3 Bv + 5 A, 7] - 3], {A, 16}, {Bv, 16}]};
  okRule = And @@ Table[Simplify[expect[W[M], st1] - expect[W[M], vac] - Conjugate[up[[1]]] . Bm . M . up[[1]]] == 0 &&
      Simplify[expect[W[M], std] - expect[W[M], vac] + Conjugate[vn[[1]]] . Bm . M . vn[[1]]] == 0, {M, Ms}];
  okQ = Simplify[expect[W[Bm], st1] - expect[W[Bm], vac]] == 1 && Simplify[expect[W[Bm], std] - expect[W[Bm], vac]] == -1;
  addCheck["Fock_space_good_sector_example",
    okC && Simplify[expect[eH, st1] - expect[eH, vac]] == E0 && Simplify[expect[eH, std] - expect[eH, vac]] == E0 && Simplify[expect[eH, vac]] == -8 E0 && okQ && okRule &&
    Simplify[inner[st1, st1]] == 1 && Simplify[inner[std, std]] == 1,
    "explicit fermionic Fock space (2^16 occupation states, positive inner product) for one good-sector momentum, m = 3, k = (4, 0, 0, 0) along x1, E = 5: " <>
    "Psi = sum_s (b_s u_s + d_s^* v_s) with exact orthonormal eigenvectors of h_k (completeness U U^dagger = I, so {Psi_A, chi_C} = delta_AC); " <>
    "the Hamiltonian chi h_k Psi has vacuum value -8 E (the filled sea), normal-ordered energy +E for the particle b_0^*|0> AND for the antiparticle d_0^*|0>; charge Psi^dagger B Psi = chi Psi gives +1 and -1; " <>
    "the expectation-value rule <u|:Psi^dagger M Psi:|u> = u^dagger B M u (particle) and -v^dagger B M v (antiparticle) holds exactly for M = C, -i C gamma^(x4), -i C gamma^(x1), C gamma^(x2) gamma^(x3) and a dense integer matrix"]];
addFormulaText["quantisation",
  "canonical quantisation of dirac16complex (SPEC section 6), x4 the evolution time, sqrt g = b4^(3/2) Cos[z] Sin[z]^(1/6), lapse f4 = Sin[z]^(1/6)",
  "pi_A = (i/2) b4^(3/2) Cos[z] (Psi^dagger B)_A; K = (sqrt g/f4) C gamma^(x4) = i b4^(3/2) Cos[z] B; {Psi_A(x), Psi^dagger_C(y)}_(x4 = y4) = B_AC delta^7(x - y)/(b4^(3/2) Cos[z]); B = -i C gamma^(x4), B^dagger = B, B^2 = 1, signature (8,8); " <>
  "no positive inner product with Psi^dagger the adjoint (Krein space, fundamental symmetry B); positive representation chi = Psi^dagger B, {Psi_A, chi_C} = delta_AC; " <>
  "Heisenberg: d4 Psi = -i B (f4/sqrt g) dHd/dPsi^dagger = -Sin[z]^(1/6) gamma^(x4) [(m + U') Psi - sum_(a != x4) gamma^a D_a Psi - gamma^(x4) Omega_x4 Psi]; mode operator h = Sin[z]^(1/6) [m (-i g[x4]) + sum_(a != x4) (1/f_a) i g[x4].g[xa] d_a + (7/2) i H g[x4].g[x0]] - i (3/4)(b4'/b4); " <>
  "good sector (no x5, x6, x7 dependence): integral b4^(3/2) Cos[z] u^dagger v d^7x conserved up to boundary terms, positive Fock space for frozen-coefficient plane waves, " <>
  "normal-ordered H = sum E (b^* b + d^* d) >= 0 per momentum; expectation-value rule <Psi^dagger M Psi> = u^dagger B M u (u^dagger u = 1, positive-energy good-sector u); EMT operator T^mu_nu = :T^mu_nu[Psi, Psi^dagger = chi B]: (normal ordered), <T> by the same rule; " <>
  "extra-time modes: E^2 = m^2 + k_s^2 - k_t^2 < 0 for k_t^2 > m^2 + k_s^2, growing as exp(|E| x4)"];
];

(* ================================================================== write the part *)
section["writing the part file"];
If[!DirectoryQ[$partDir], CreateDirectory[$partDir, CreateIntermediateDirectories -> True]];
nPass = Count[checks, c_ /; c["verdict"] == "PASS"]; nTot = Length[checks];
writeLF[FileNameJoin[{$partDir, part <> ".json"}], StringJoin[
  "{\n",
  "  \"part\": ", jstr[part], ",\n",
  "  \"inputs\": {", StringRiffle[KeyValueMap[jstr[#1] <> ": " <> jstr[#2] &, inputHashes], ", "], "},\n",
  "  \"checks\": [\n", StringRiffle[checkLine /@ checks, ",\n"], "\n  ],\n",
  "  \"formulas\": [\n", StringRiffle[fjson /@ formulas, ",\n"], "\n  ]\n}\n"]];
Print["part ", part, ": ", nPass, "/", nTot, " checks passed; total time ", Round[AbsoluteTime[] - t0, 0.1], " s"];
Exit[If[nPass == nTot, 0, 1]];
