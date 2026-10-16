#!/usr/bin/env wolframscript
(* ::Package:: *)

(* verify_field_theory.wls

   Driver for Revision/theory/wolfram/RevisionFieldTheory.wl (Revision/SPEC.md, sections 1-4 and 6) for the CORRECTED
   metric of 2026-10-16 (version 2; Revision/metric_warped/, Revision/docs/METRIC_SELF_CONSISTENCY.md):
     g = diag(E^(-2 a4) b4 Cot[z]^2, E^(2 a4) (x3), -1, -E^(-2 a4) b4 (Sin[z]^2)^(1/6) (x3)),  z = 6 H x0 REAL,
   in the author's coordinates x0..x7 (x0 = the hidden, space-like direction, Wolfram position 1; x4 = the time,
   position 5).  Every statement is proved for GENERAL functions a4(x4) and b4(x4) > 0 and for EVERY real z (the
   user's rules of 2026-10-16: -Infinity < z < Infinity; Sin[z]^(1/3) = (Sin[z]^2)^(1/6), the positive branch); no
   sign of Sin z or Cos z is assumed.  sqrt|g| = sig f0...f7 with sig = sign(Cot z) = +-1 (a symbol with sig^2 = 1,
   constant between the degenerate points z = n Pi/2).  Until 2026-10-16 this script proved the statements for the
   metric of 2026-10-14 (diag(Cot^2, E^(2 a4) Sin^(1/3) (x3), -1, -E^(-2 a4) b4 Sin^(1/3) (x3)), 0 < z < Pi/2),
   withdrawn because its Lovelock tensors have off-diagonal components that no diagonal source can match.

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
      "  \"report\": ", jstr["Revision field theory (SPEC sections 1-4, 6) for the corrected metric of 2026-10-16 (general a4 and b4; every real z): vielbein, canonical spin connection, Lagrangian, Euler-Lagrange equations, non-triviality [1] and [2], current, energy-momentum tensor, exact solutions, canonical quantisation; both statistics, verified exactly in WolframScript"], ",\n",
      "  \"producer\": ", jstr["Revision/theory/wolfram/verify_field_theory.wls (parts base, emt-G, emt-C, solutions, solutions-G, quantisation; merge)"], ",\n",
      "  \"package\": ", jstr["Revision/theory/wolfram/RevisionFieldTheory.wl"], ",\n",
      "  \"fixture\": ", jstr["Revision/algebra/gammas.json"], ",\n",
      "  \"metric\": ", jstr["g = diag(E^(-2 a4[x4]) b4[x4] Cot[z]^2, E^(2 a4[x4]) (3 times), -1, -E^(-2 a4[x4]) b4[x4] (Sin[z]^2)^(1/6) (3 times)), z = 6 H x0 real, b4[x4] > 0 and a4[x4] general functions of x4 (Revision/SPEC.md section 1; the corrected metric of 2026-10-16, version 2)"], ",\n",
      "  \"statistics\": ", jstr["G = dirac16complex: 16 complex anticommuting components, explicit Grassmann algebra with generators theta_1, theta_2 and their conjugates; C = dirac16complex00: 16 complex commuting components"], ",\n",
      "  \"coordinates\": ", jstr["the author's coordinates x0..x7: x0 = the hidden, space-like direction; x1, x2, x3 = 3-space; x4 = time; x5, x6, x7 = the exponentially deflating extra times; z = 6 H x0 takes every real value (-Infinity < z < Infinity), H > 0; Sin[z]^(1/3) = (Sin[z]^2)^(1/6); sqrt|g| = sig f0...f7, sig = sign(Cot z) = +-1"], ",\n",
      "  \"summary\": {\"passed\": ", ToString[nPass], ", \"failed\": ", ToString[nTot - nPass], ", \"total\": ", ToString[nTot], "},\n",
      "  \"checks\": [\n", StringRiffle[checkLine /@ checks, ",\n"], "\n  ]\n}\n"];
    formulaText = StringJoin[
      "{\n",
      "  \"description\": ", jstr["Exact formulas of the Revision field theory (SPEC sections 1-4, 6) for the corrected primordial metric of 2026-10-16 (general a4 and b4, every real z), for the documents. Every formula is verified by a named check of Revision/theory/reports/wolfram-field-theory.json. Wolfram InputForm; g[xa] = gamma^(xa) of Revision/algebra/gammas.json; a4' = Derivative[1][a4][x4]; b4' = Derivative[1][b4][x4]; z = 6 H x0; rftSig = sign(Cot z); Psibar = Psi^dagger C; S = Psibar Psi; V = m + U'(S); both statistics unless stated."], ",\n",
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
(* the gravitational (spin-connection) term of the Dirac operator for the corrected metric:
   gamma^mu Omega_mu = cg gamma^(x0) + vg gamma^(x4), cg = (3/2) H E^a4 b4^(-1/2), vg = b4'/b4 - a4'/2
   (the independent sympy record Revision/metric_warped/results/warped-metric.json, key dirac_gravity_term) *)
cg = (3/2) H E^a4[x4]/Sqrt[b4[x4]];
vg = bu - a4p/2;
gOm = cg g[[1]] + vg g[[5]];
(* the hidden block: f0 = sb Cot z, f_t = sb (Sin z^2)^(1/12) with sb = E^-a4 b4^(1/2) (its scale factor) *)
sb = E^(-a4[x4]) Sqrt[b4[x4]];
w12 = (Sin[rftZ]^2)^(1/12);
mw = Import[mwFile, "RawJSON"];

(* ================================================================== PART base *)
If[part === "base",
(* ------------------------------------------------------------------ the exact zero test *)
addCheck["zero_test_sanity",
  rftZeroQ[ph[1] @@ X (Sin[6 H x0]^2 + Cos[6 H x0]^2 - 1)] && !rftZeroQ[ph[1] @@ X] && !rftZeroQ[pf[x0]] &&
  rftZeroQ[U'[ph[1] @@ X phc[1] @@ X] ph[2] @@ X - ph[2] @@ X U'[phc[1] @@ X ph[1] @@ X]] && rftZeroQ[E^a4[x4] E^-a4[x4] - 1] &&
  rftZeroQ[cA[1] H - cA[1] H Cot[6 H x0] Tan[6 H x0]] && !rftZeroQ[D[ph[1] @@ X, x1] - D[ph[1] @@ X, x2]] && !rftZeroQ[H (Sin[6 H x0]^2)^(1/12) - H] &&
  !rftZeroQ[ph[1] @@ X (Sin[6 H x0]^2 + Cos[6 H x0]^2)] &&
  rftZeroQ[ph[1] @@ X (Sqrt[b4[x4]]^2 - b4[x4])] && rftZeroQ[ph[1] @@ X (b4[x4]^(3/2)/Sqrt[b4[x4]] - b4[x4])] &&
  !rftZeroQ[ph[1] @@ X (b4[x4] - 1)] && !rftZeroQ[ph[1] @@ X Derivative[1][b4][x4]] &&
  rftZeroQ[ph[1] @@ X (((Sin[6 H x0]^2)^(1/12))^12 - Sin[6 H x0]^2)] && !rftZeroQ[ph[1] @@ X ((Sin[6 H x0]^2)^(1/2) - Sin[6 H x0])] &&
  !rftZeroQ[ph[1] @@ X ((Sin[6 H x0]^2)^(1/2) + Sin[6 H x0])] && rftZeroQ[ph[1] @@ X (rftSig^2 - 1)] && !rftZeroQ[ph[1] @@ X (rftSig - 1)] &&
  rftZeroQ[D[(Sin[6 H x0]^2)^(1/12), x0] - H Cot[6 H x0] (Sin[6 H x0]^2)^(1/12)],
  "the exact zero test (field functions, their derivatives and U-expressions as independent polynomial variables; coefficients in the normal form for EVERY real z: Sin z, Cos z signed, w = (Sin z^2)^(1/12) > 0, " <>
  "reduced modulo Cos^2 + Sin^2 - 1, w^12 - Sin^2 and sig^2 - 1, sig = sign(Cot z)) returns True on identities and False on nonzero expressions in a set of control cases: " <>
  "(Sin z^2)^(1/2) - Sin z and (Sin z^2)^(1/2) + Sin z are NOT zero (no sign of Sin z is assumed), w^12 - Sin^2 and sig^2 - 1 are zero, sig - 1 is not; d0 (Sin z^2)^(1/12) = H Cot z (Sin z^2)^(1/12); " <>
  "b4[x4] and its derivatives are free symbols: Sqrt[b4]^2 - b4 and b4^(3/2)/b4^(1/2) - b4 are zero, b4 - 1 and b4' are not (the test never sets b4 = 1)"];

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
addCheck["metric_is_the_corrected_metric",
  rftZeroQ[rftG0 - rftMetricAuthor] && rftZeroQ[Transpose[rftE0] . eta . rftE0 - rftMetricAuthor] &&
  rftZeroQ[rftMetricAuthor - DiagonalMatrix[ToExpression /@ {"E^(-2 a4[x4]) b4[x4] Cot[6 H x0]^2", "E^(2 a4[x4])", "E^(2 a4[x4])", "E^(2 a4[x4])", "-1",
    "-E^(-2 a4[x4]) b4[x4] (Sin[6 H x0]^2)^(1/6)", "-E^(-2 a4[x4]) b4[x4] (Sin[6 H x0]^2)^(1/6)", "-E^(-2 a4[x4]) b4[x4] (Sin[6 H x0]^2)^(1/6)"}]] &&
  mw["metric_corrected"] === "diag(E^(-2 a4[x4]) b4[x4] Cot[6 H x0]^2, E^(2 a4[x4]), E^(2 a4[x4]), E^(2 a4[x4]), -1, -E^(-2 a4[x4]) b4[x4] (Sin[6 H x0]^2)^(1/6), -E^(-2 a4[x4]) b4[x4] (Sin[6 H x0]^2)^(1/6), -E^(-2 a4[x4]) b4[x4] (Sin[6 H x0]^2)^(1/6))",
  "g = e^T eta e with the diagonal vielbein e^a_mu = f_a delta^a_mu, f(x0) = E^-a4 b4^(1/2) Cot[z] (signed), f(x1,x2,x3) = E^a4, f(x4) = 1, f(x5,x6,x7) = E^-a4 b4^(1/2) (Sin[z]^2)^(1/12), z = 6 H x0, " <>
  "reproduces the corrected metric of SPEC section 1 entry by entry, for general functions a4(x4) and b4(x4) > 0 and every real z, and the record of Revision/metric_warped (key metric_corrected) states the same metric"];
addCheck["vielbein_inverse",
  rftZeroQ[rftE0 . rftEinv0 - IdentityMatrix[8]] &&
  rftZeroQ[Table[Sum[rftEinv0[[mu, a]] rftEinv0[[nu, a]] eta[[a, a]], {a, 8}] - rftGinv0[[mu, nu]], {mu, 8}, {nu, 8}]],
  "e^a_mu e_a^nu = delta and e_a^mu e_b^nu eta^ab = g^munu (inverse vielbein e_a^mu = delta_a^mu / f_a)"];
addCheck["sqrt_det_g",
  rftZeroQ[Det[rftG0] - E^(-2 a4[x4]) b4[x4]^4 Cot[rftZ]^2 (Sin[rftZ]^2)^(1/2)] && rftZeroQ[Times @@ f - E^(-a4[x4]) b4[x4]^2 Cot[rftZ] (Sin[rftZ]^2)^(1/4)] &&
  rftZeroQ[sg - rftSig Times @@ f] && rftZeroQ[sg^2 - Det[rftG0]] && rftZeroQ[D[sg, x4] - (2 bu - a4p) sg] &&
  rftZeroQ[D[sg, x0] + 3 H (2 Tan[rftZ] + Cot[rftZ]) sg],
  "det g = E^(-2 a4) b4^4 Cot[z]^2 (Sin[z]^2)^(1/2) >= 0 (four negative entries), f0...f7 = E^-a4 b4^2 Cot[z] (Sin[z]^2)^(1/4), so sqrt|det g| = sig f0...f7 = E^-a4 b4^2 |Cot z| (Sin z^2)^(1/4) with sig = sign(Cot z) = +-1, " <>
  "constant on every interval n Pi/2 < z < (n + 1) Pi/2 (the metric degenerates at z = n Pi/2: g00 = 0 where Cos z = 0, g_tt = 0 where Sin z = 0); sqrt g^2 = det g; " <>
  "d_x4 sqrt|g| = (2 b4'/b4 - a4') sqrt|g| and d_x0 sqrt|g| = -3 H (2 Tan z + Cot z) sqrt|g|. Every field equation and every T^mu_nu below is independent of sig (they are homogeneous of degree 0 in sqrt g)"];
addCheck["degenerate_at_H_0",
  Limit[(Sin[6 H x0]^2)^(1/6), H -> 0] === 0 && Limit[Cot[6 H x0]^2, H -> 0, Direction -> "FromAbove", Assumptions -> x0 > 0] === Infinity,
  "at fixed x0 != 0 and H -> 0+ the entries g55 = g66 = g77 -> 0 (for every b4 > 0) and g00 -> infinity: H = 0 is not a metric of the family (a degenerate limit); every statement below assumes H > 0"];
gamNZ = DeleteCases[Flatten[Table[{l, mm, n, rftSimp[Gm[[l, mm, n]]]}, {l, 8}, {mm, 8}, {n, mm, 8}], 2], {_, _, _, 0}];
addFormula["christoffel_nonzero", "nonzero Christoffel symbols {l, m, n, Gamma^l_mn} (m <= n; Gamma^l_nm = Gamma^l_mn), Wolfram positions 1..8 = x0..x7", gamNZ];
addCheck["christoffel_count",
  Length[gamNZ] == 21 && !FreeQ[gamNZ, Derivative[1][b4]],
  "the Levi-Civita connection has " <> ToString[Length[gamNZ]] <> " independent nonzero symbols Gamma^l_mn (m <= n): Gamma^x0_(x0 x0), Gamma^x0_(x0 x4), Gamma^x0_(xt xt) (3), Gamma^xi_(xi x4) (3), Gamma^x4_(x0 x0), Gamma^x4_(xi xi) (3), " <>
  "Gamma^x4_(xt xt) (3), Gamma^xt_(xt x0) (3), Gamma^xt_(xt x4) (3); the hidden and extra-time ones contain b4'/b4; listed in field-theory.json (christoffel_nonzero)"];
Rm = rftRiemann[Gm];
Ric = Table[Sum[Rm[[r, s, r, n]], {r, 8}], {s, 8}, {n, 8}];
RicMixed = Table[Sum[rftGinv0[[mu, s]] Ric[[s, nu]], {s, 8}], {mu, 8}, {nu, 8}];
Rs = Sum[RicMixed[[mu, mu]], {mu, 8}];
(* Cb = H^2 E^(2 a4)/b4: the hidden block (x0, x5, x6, x7) has the constant curvature -Cb at each time *)
Cb = H^2 E^(2 a4[x4])/b4[x4];
RsExpected = -12 Cb + 8 a4p^2 - 2 a4''[x4] - 8 a4p bu + 4 bpp + bu^2;
addCheck["ricci_scalar",
  rftZeroQ[Rs - RsExpected],
  "Ricci scalar R = g^sn R^r_srn = -12 Cb + 8 a4'^2 - 2 a4'' - 8 a4' b4'/b4 + 4 b4''/b4 + (b4'/b4)^2, Cb = H^2 E^(2 a4)/b4, independent of x0 " <>
  "(convention R^r_smn = d_m Gamma^r_ns - d_n Gamma^r_ms + Gamma^r_ml Gamma^l_ns - Gamma^r_nl Gamma^l_ms)"];
ricExpected = ConstantArray[0, {8, 8}];
ricExpected[[1, 1]] = -3 Cb + a4p^2 - a4''[x4] - (5/2) a4p bu + (1/2) bpp + (1/2) bu^2;
Do[ricExpected[[i, i]] = -a4p^2 + a4''[x4] + 2 a4p bu, {i, 2, 4}];
ricExpected[[5, 5]] = 7 a4p^2 - a4''[x4] - 4 a4p bu + 2 bpp - bu^2;
Do[ricExpected[[t, t]] = ricExpected[[1, 1]], {t, 6, 8}];
mwRic = Table[ReleaseHold[ToExpression[mw["ricci_mixed_diagonal_mathematica"][rftCoordNames[[h]]]]], {h, 8}];
addCheck["ricci_mixed_components",
  rftZeroQ[RicMixed - ricExpected] && rftZeroQ[Diagonal[RicMixed] - mwRic] && rftZeroQ[Rs - ReleaseHold[ToExpression[mw["ricci_scalar_mathematica"]]]],
  "R^mu_nu is DIAGONAL (no off-diagonal component; the metric of 2026-10-14 had R^x4_x0 = (3/2) H Cot[z] b4'/b4) and independent of x0: " <>
  "R^x0_x0 = R^xt_xt = -3 Cb + a4'^2 - a4'' - (5/2) a4' b4'/b4 + (1/2) b4''/b4 + (1/2)(b4'/b4)^2 (t = 5, 6, 7; the hidden direction and the extra times form one block), " <>
  "R^xi_xi = -a4'^2 + a4'' + 2 a4' b4'/b4 (i = 1, 2, 3), R^x4_x4 = 7 a4'^2 - a4'' - 4 a4' b4'/b4 + 2 b4''/b4 - (b4'/b4)^2, Cb = H^2 E^(2 a4)/b4; " <>
  "R^mu_nu and R equal the independent sympy record Revision/metric_warped/results/warped-metric.json (keys ricci_mixed_diagonal_mathematica, ricci_scalar_mathematica)"];
addFormula["ricci_mixed_nonzero", "nonzero R^mu_nu as {mu, nu, value}, Wolfram positions 1..8 = x0..x7",
  DeleteCases[Flatten[Table[{mu, nu, ricExpected[[mu, nu]]}, {mu, 8}, {nu, 8}], 1], {_, _, 0}]];
addFormula["ricci_scalar", "Ricci scalar R", RsExpected];
(* the corrected metric is flat for a4 = 0, b4 = H^2 x4^2 (8-dimensional flat space in Milne form), so the
   statement "never flat for H > 0" of the metric of 2026-10-14 does not hold for it; the record states instead
   when it is curved *)
Module[{milne = {a4 -> Function[t, 0], b4 -> Function[t, H^2 t^2]}, RmM, flatM, curvedHist},
  RmM = rftRiemann[rftChristoffel[rftG0 /. milne, Inverse[rftG0 /. milne]]];
  flatM = rftZeroQ[RmM];
  curvedHist = !rftZeroQ[(Rs /. {a4 -> Function[t, H t], b4 -> Function[t, E^(4 H t/3)]})];
  addCheck["flat_member_and_curvature",
    flatM && curvedHist && rftZeroQ[(RsExpected /. {a4 -> Function[t, 0], b4 -> Function[t, H^2 t^2]})],
    "the corrected metric is FLAT for a4 = 0, b4 = H^2 x4^2 (all 4096 R^r_smn vanish: 8-dimensional flat space in Milne form, the block of curvature -H^2 scaled by H x4), " <>
    "so unlike the metric of 2026-10-14 (R^x0_x0 = -6 H^2) it is not curved for every a4, b4; on the record's history a4 = H x4, b4 = E^(4 H x4/3) R != 0 (curved). " <>
    "This replaces the check never_flat_for_H_positive of the metric of 2026-10-14"]];

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
(* h4 = b4'/(2 b4) - a4' = (d/dx4) ln(E^-a4 b4^(1/2)), the rate of the hidden block (x0, x5, x6, x7) *)
h4 = bu/2 - a4p;
omExpected = Join[
  {{1, 1, 5, h4 sb Cot[rftZ]}},
  Table[{i, i, 5, a4p E^a4[x4]}, {i, 2, 4}],
  Flatten[Table[{{t, 5, t, h4 sb w12}, {t, 1, t, H w12}}, {t, 6, 8}], 1]];
addCheck["omega_components",
  Length[omNZ] == 10 && Sort[omNZ[[All, 1 ;; 3]]] == Sort[omExpected[[All, 1 ;; 3]]] &&
  And @@ Table[rftZeroQ[omLow[[Sequence @@ e[[1 ;; 3]]]] - e[[4]]], {e, omExpected}],
  "exactly 10 independent nonzero omega_mu,ab (a < b in the order x0..x7), with h4 = b4'/(2 b4) - a4' = (d/dx4) ln(E^-a4 b4^(1/2)) and sb = E^-a4 b4^(1/2): " <>
  "omega_x0,(x0)(x4) = h4 sb Cot[z] (the hidden direction now follows the extra times in x4); for i = x1, x2, x3: omega_i,(i)(x4) = a4' E^a4 (no x0 part: 3-space does not depend on x0); " <>
  "for t = x5, x6, x7: omega_t,(x4)(t) = h4 sb (Sin[z]^2)^(1/12) and omega_t,(x0)(t) = H (Sin[z]^2)^(1/12); omega_x4 = 0. " <>
  "These are omega_c,(c)(b) = eta_cc (d_b f_c)/f_b for the diagonal vielbein; every component is h4, a4' or H times a factor that does not vanish between the degenerate points z = n Pi/2"];
addFormula["omega_nonzero", "nonzero omega_mu,ab = eta_ac omega_mu^c_b as {mu, a, b, value} with a < b (omega_mu,ba = -omega_mu,ab); Wolfram positions mu, a, b = 1..8 = x0..x7", omExpected];
addCheck["Omega_components",
  rftZeroQ[Om - Table[Sum[If[e[[1]] == mu, e[[4]] (1/2) g[[e[[2]]]] . g[[e[[3]]]], 0], {e, omExpected}], {mu, 8}]] &&
  rftZeroQ[Om[[5]]] && !rftZeroQ[Om[[1]]],
  "Omega_mu = (1/2) omega_mu,ab S^ab = sum_(a<b) omega_mu,ab (1/2) gamma^a gamma^b: Omega_x0 = (1/2) h4 sb Cot[z] gamma^(x0) gamma^(x4); Omega_xi = (1/2) a4' E^a4 gamma^(xi) gamma^(x4) for i = 1, 2, 3; " <>
  "Omega_xt = (1/2) (Sin[z]^2)^(1/12) (h4 sb gamma^(x4) gamma^(xt) + H gamma^(x0) gamma^(xt)) for t = 5, 6, 7; Omega_x4 = 0 (f4 = 1); Omega_x0 != 0"];
addFormulaText["Omega_components",
  "the spinor connection Omega_mu = (1/2) omega_mu,ab S^ab; h4 = b4'/(2 b4) - a4', sb = E^-a4 b4^(1/2)",
  "Omega_x0 = (1/2) h4 sb Cot[6 H x0] g[x0].g[x4]; Omega_xi = (1/2) a4'[x4] E^a4[x4] g[xi].g[x4] (i = 1, 2, 3); Omega_xt = (1/2) (Sin[6 H x0]^2)^(1/12) (h4 sb g[x4].g[xt] + H g[x0].g[xt]) (t = 5, 6, 7); Omega_x4 = 0; g[xa] = gamma^(xa) (frame gammas of the fixture)"];
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
  rftZeroQ[gO - gOm] && mw["dirac_gravity_term"] === "(3/2) H E^a4 b4^(-1/2) gamma^(x0) + (b4'/b4 - a4'/2) gamma^(x4)",
  "gamma^mu Omega_mu = (3/2) H E^a4 b4^(-1/2) gamma^(x0) + (b4'/b4 - a4'/2) gamma^(x4) exactly, independent of x0 for every real z and equal to the independent sympy record " <>
  "Revision/metric_warped/results/warped-metric.json (key dirac_gravity_term); in the metric of 2026-10-14 it was 3 H gamma^(x0) + (3/4)(b4'/b4) gamma^(x4)"];
addCheck["gammaOmega_per_direction",
  rftZeroQ[perDir[[1]] - (h4/2) g[[5]]] &&
  And @@ Table[rftZeroQ[perDir[[mu]] - (a4p/2) g[[5]]], {mu, 2, 4}] &&
  And @@ Table[rftZeroQ[perDir[[mu]] - ((h4/2) g[[5]] + (H/(2 sb)) g[[1]])], {mu, 6, 8}] &&
  rftZeroQ[perDir[[5]]],
  "per direction (no sum): gamma^(x0) Omega_x0 = (h4/2) gamma^(x4); gamma^(xi) Omega_xi = (a4'/2) gamma^(x4) for each 3-space direction i = 1, 2, 3; " <>
  "gamma^(xt) Omega_xt = (h4/2) gamma^(x4) + (H/2) E^a4 b4^(-1/2) gamma^(x0) for each extra time t = 5, 6, 7; gamma^(x4) Omega_x4 = 0 (h4 = b4'/(2 b4) - a4'). " <>
  "Sum: gamma^(x4) coefficient 4 (h4/2) + 3 (a4'/2) = b4'/b4 - a4'/2 (the four directions of the hidden block x0, x5, x6, x7 share the rate h4); gamma^(x0) coefficient 3 (H/2) E^a4 b4^(-1/2) from the three extra times"];
addFormula["gammaOmega_per_direction", "the matrices gamma^mu Omega_mu (no sum) for mu = x0..x7 as coefficients of gamma^(x4) and gamma^(x0): {mu (Wolfram position 1..8 = x0..x7), coefficient of gamma^(x4), coefficient of gamma^(x0)}",
  Table[{mu, coefDir[[mu, 5]], coefDir[[mu, 1]]}, {mu, 8}]];
addFormula["gammaOmega_total", "gamma^mu Omega_mu (sum over mu); gamma[xa] = gamma^(xa)", (3/2) H E^a4[x4] b4[x4]^(-1/2) gamma["x0"] + (Derivative[1][b4][x4]/b4[x4] - Derivative[1][a4][x4]/2) gamma["x4"]];
addCheck["gammaOmega_divergence_form",
  rftZeroQ[gO - 1/(2 sg) Sum[D[sg gup[[mu]], X[[mu]]], {mu, 8}]] &&
  rftZeroQ[Table[gup[[mu]] . Om[[mu]] + Om[[mu]] . gup[[mu]], {mu, 8}]],
  "{gamma^mu, Omega_mu} = 0 for each mu separately (Omega_mu contains only S^(mu b)), hence gamma^mu Omega_mu = (1/(2 sqrt g)) d_mu (sqrt g gamma^mu) (sig cancels); " <>
  "for this metric (1/(2 sqrt g)) d_x0 (sqrt g/f0) gamma^(x0) = (1/(2 sqrt g)) d_x0 (sig b4^(3/2) (Sin z^2)^(1/4)) gamma^(x0) = (3/2) H E^a4 b4^(-1/2) gamma^(x0) and (1/(2 sqrt g)) d_x4 (sqrt g) gamma^(x4) = (b4'/b4 - a4'/2) gamma^(x4)"];

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
  "Lagrangian density for both statistics (SPEC section 3), Psibar = Psi^dagger C, S = Psibar Psi, sqrt g = E^-a4 b4^2 |Cot[z]| (Sin[z]^2)^(1/4)",
  "L = sqrt g [ (1/2) sum_mu (Psibar gamma^mu D_mu Psi - (D_mu Psibar) gamma^mu Psi) - m S - U(S) ] = sqrt g [ (1/2) sum_a (1/f_a) (Psibar gamma^(a) d_a Psi - d_a Psibar gamma^(a) Psi) - m S - U(S) ]; sqrt g = E^-a4[x4] b4[x4]^2 |Cot[z]| (Sin[z]^2)^(1/4); f_0 = E^-a4 b4^(1/2) Cot[z], f_(1,2,3) = E^a4, f_4 = 1, f_(5,6,7) = E^-a4 b4^(1/2) (Sin[z]^2)^(1/12)"];

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
      "gamma^mu D_mu Psi = E^a4 b4^(-1/2) Tan[z] gamma^(x0) d0 Psi + E^-a4 (gamma^(x1) d1 + gamma^(x2) d2 + gamma^(x3) d3) Psi + gamma^(x4) d4 Psi + E^a4 b4^(-1/2) (Sin[z]^2)^(-1/12) (gamma^(x5) d5 + gamma^(x6) d6 + gamma^(x7) d7) Psi " <>
      "+ (3/2) H E^a4 b4^(-1/2) gamma^(x0) Psi + (b4'/b4 - a4'/2) gamma^(x4) Psi, for " <> statName[st] <>
      " (the hidden-direction terms E^a4 b4^(-1/2) (Tan[z] d0 + (3/2) H) gamma^(x0) carry the inverse scale factor of the hidden block)"]]], {st, stats}];
addFormulaText["field_equation",
  "the Euler-Lagrange equation (both statistics), z = 6 H x0, V = m + U'(S)",
  "E^a4[x4] b4[x4]^(-1/2) Tan[z] g[x0] d0 Psi + E^-a4[x4] (g[x1] d1 + g[x2] d2 + g[x3] d3) Psi + g[x4] d4 Psi + E^a4[x4] b4[x4]^(-1/2) (Sin[z]^2)^(-1/12) (g[x5] d5 + g[x6] d6 + g[x7] d7) Psi + (3/2) H E^a4[x4] b4[x4]^(-1/2) g[x0] Psi + (b4'[x4]/b4[x4] - a4'[x4]/2) g[x4] Psi = (m + U'(S)) Psi"];
addFormulaText["adjoint_equation",
  "the adjoint equation (both statistics); D_mu Psibar = d_mu Psibar - Psibar Omega_mu",
  "E^a4 b4^(-1/2) Tan[z] d0 Psibar g[x0] + E^-a4 (d1 Psibar g[x1] + d2 Psibar g[x2] + d3 Psibar g[x3]) + d4 Psibar g[x4] + E^a4 b4^(-1/2) (Sin[z]^2)^(-1/12) (d5 Psibar g[x5] + d6 Psibar g[x6] + d7 Psibar g[x7]) + (3/2) H E^a4 b4^(-1/2) Psibar g[x0] + (b4'/b4 - a4'/2) Psibar g[x4] = -(m + U'(S)) Psibar"];
(* 16 explicit components with inert symbols *)
compStr = Table[Module[{terms = {}},
   Do[If[g[[a, A, B]] =!= 0, AppendTo[terms, g[[a, A, B]]/f[[a]] dd[rftCoordNames[[a]], Psi[B]]]], {a, 8}, {B, 16}];
   Do[If[g[[1, A, B]] =!= 0, AppendTo[terms, cg g[[1, A, B]] Psi[B]]], {B, 16}];
   Do[If[g[[5, A, B]] =!= 0, AppendTo[terms, vg g[[5, A, B]] Psi[B]]], {B, 16}];
   wl[Total[terms] == V Psi[A]]], {A, 16}];
AppendTo[formulas, <|"key" -> "field_equation_components", "description" -> "the 16 component equations (gamma^mu D_mu Psi)_A = V Psi_A, A = 1..16 (rows of the fixture gammas), V = m + U'(S); dd[xa, Psi[B]] = d Psi_B / d xa", "wl" -> compStr|>];
blk[a_] := {g[[a]][[1 ;; 8, 9 ;; 16]], g[[a]][[9 ;; 16, 1 ;; 8]]};
addCheck["block_form",
  And @@ Table[g[[a]][[1 ;; 8, 1 ;; 8]] == ConstantArray[0, {8, 8}] && g[[a]][[9 ;; 16, 9 ;; 16]] == ConstantArray[0, {8, 8}], {a, 8}] &&
  rftChir == ArrayFlatten[{{-IdentityMatrix[8], 0}, {0, IdentityMatrix[8]}}],
  "every gamma^a = {{0, tb_a}, {t_a, 0}} is block off-diagonal in the chiral split Psi = (psi_-, psi_+) (Gamma = diag(-1, 1)): the field equation is the pair " <>
  "sum_a (1/f_a) tb_a d_a psi_+ + cg tb_0 psi_+ + vg tb_4 psi_+ = V psi_- and sum_a (1/f_a) t_a d_a psi_- + cg t_0 psi_- + vg t_4 psi_- = V psi_+, cg = (3/2) H E^a4 b4^(-1/2), vg = b4'/b4 - a4'/2 (blocks in field-theory.json)"];
AppendTo[formulas, <|"key" -> "field_equation_blocks",
  "description" -> "block form: Psi = (psi_minus (rows 1..8, Gamma = -1), psi_plus (rows 9..16, Gamma = +1)); gamma^(xa) = {{0, tb[xa]}, {t[xa], 0}}; equations sum_a (1/f_a) tb[xa] d_a psi_plus + cg tb[x0] psi_plus + vg tb[x4] psi_plus = V psi_minus and sum_a (1/f_a) t[xa] d_a psi_minus + cg t[x0] psi_minus + vg t[x4] psi_minus = V psi_plus, cg = (3/2) H E^a4 b4^(-1/2), vg = b4'/b4 - a4'/2; listed {xa, tb, t}",
  "wl" -> Table[wl[{rftCoordNames[[a]], blk[a][[1]], blk[a][[2]]}], {a, 8}]|>];
(* evolution form *)
Do[With[{P = fld[st]["Psi"]},
  Module[{S = Ldata[st]["S"], rest, d4},
    rest = vAdd[st, Fold[vAdd[st, #1, #2] &, Table[If[a == 5, Table[sZero[st], {16}], matVec[st, g[[a]]/f[[a]], vD[st, P, X[[a]]]]], {a, 8}]], matVec[st, cg g[[1]], P]];
    d4 = vAdd[st, matVec[st, -g[[5]], vAdd[st, rftVPsi[st, S, P], vScal[st, -1, rest]]], vScal[st, -vg, P]];
    addCheck["evolution_form_" <> st,
      g[[5]] . g[[5]] == -id16 &&
      And @@ Table[sZeroQ[st, sAdd[st, {matVec[st, g[[5]], vAdd[st, vD[st, P, x4], vScal[st, -1, d4]]][[A]], sScal[st, -1, Ldata[st]["E"][[A]]]}]], {A, 16}],
      "(gamma^(x4))^2 = -1, so the field equation is equivalent to the first-order evolution equation d4 Psi = -gamma^(x4) [(m + U'(S)) Psi - sum_(a != x4) (1/f_a) gamma^(a) d_a Psi - (3/2) H E^a4 b4^(-1/2) gamma^(x0) Psi] - (b4'/b4 - a4'/2) Psi " <>
      "(exact: gamma^(x4) (d4 Psi - RHS) = E; the last term is the factor E^(a4/2) b4^(-1) of the solutions): the slices x4 = const are non-characteristic (g^44 = -1 != 0), " <> statName[st]]]], {st, stats}];
addFormulaText["evolution_form", "first-order evolution form (both statistics)",
  "d4 Psi = -g[x4] ((m + U'(S)) Psi - sum_(a != x4) (1/f_a) g[xa] d_a Psi - (3/2) H E^a4[x4] b4[x4]^(-1/2) g[x0] Psi) - (b4'[x4]/b4[x4] - a4'[x4]/2) Psi"];

(* ------------------------------------------------------------------ 5. non-triviality *)
section["non-triviality"];
Do[With[{P = fld[st]["Psi"], Pc = fld[st]["Psic"]},
  Module[{geoNoOm, Enoom, diff},
    geoNoOm = <|"sqrtg" -> sg, "gup" -> gup, "Om" -> Table[z16, {8}]|>;
    Enoom = rftE[st, geoNoOm, P, Pc];
    diff = vAdd[st, Ldata[st]["E"], vScal[st, -1, Enoom], vScal[st, -1, matVec[st, gOm, P]]];
    addCheck["nontriviality_" <> If[st === "G", "1_dirac16complex", "2_dirac16complex00"],
      (And @@ Table[sZeroQ[st, diff[[A]]], {A, 16}]) && !(And @@ Table[sZeroQ[st, matVec[st, gOm, P][[A]]], {A, 16}]) &&
      rftZeroQ[gOm . gOm - (cg^2 - vg^2) id16] &&
      !rftZeroQ[1/f[[2]] - 1] && !rftZeroQ[1/f[[6]] - 1] && !rftZeroQ[1/f[[1]] - 1],
      "NON-TRIVIALITY [" <> If[st === "G", "1", "2"] <> "] for " <> statName[st] <> ": the spin-connection part of the Euler-Lagrange equation is exactly " <>
      "(gamma^mu D_mu - gamma^mu d_mu) Psi = gamma^mu Omega_mu Psi = G Psi with G = cg gamma^(x0) + vg gamma^(x4), cg = (3/2) H E^a4 b4^(-1/2), vg = b4'/b4 - a4'/2, nonzero for every H > 0 and all functions a4, b4 (cg > 0); " <>
      "G^2 = (cg^2 - vg^2) I16 = ((9/4) H^2 E^(2 a4)/b4 - (b4'/b4 - a4'/2)^2) I16, so G Psi != 0 for every Psi != 0 wherever cg^2 != vg^2 " <>
      "(on the record's history a4 = H x4, b4 = E^(4 H x4/3): cg = (3/2) H E^(H x4/3), vg = (5/6) H, G^2 = H^2 ((9/4) E^(2 H x4/3) - 25/36) > 0); " <>
      "in addition the vielbein enters every derivative term, gamma^mu d_mu = E^a4 b4^(-1/2) Tan[z] gamma^(x0) d0 + E^-a4 gamma^(xi) d_i + gamma^(x4) d4 + E^a4 b4^(-1/2) (Sin[z]^2)^(-1/12) gamma^(xt) d_t " <>
      "(none of the factors is identically 1). All gravitational terms vanish together only if Omega_mu = 0 for all mu (check Omega_vanishes_iff_a4prime_b4prime_and_H_vanish), " <>
      "which by spin_curvature_equals_Riemann requires a flat metric (the corrected metric is flat only for special a4, b4, check flat_member_and_curvature; H = 0 is a degenerate limit, check degenerate_at_H_0)"]]], {st, stats}];
addCheck["Omega_vanishes_iff_a4prime_b4prime_and_H_vanish",
  And @@ Table[Module[{v = e[[4]], c, fac},
     c = Which[!FreeQ[v, Derivative[1][b4]], h4, !FreeQ[v, a4p], a4p, True, H];
     fac = Cancel[Together[v/c]];
     FreeQ[fac, a4p] && FreeQ[fac, Derivative[1][b4]] && FreeQ[fac /. rftZ -> zz, H] &&
       (rftZeroQ[fac - E^a4[x4]] || rftZeroQ[fac - sb Cot[rftZ]] || rftZeroQ[fac - sb w12] || rftZeroQ[fac - w12])], {e, omExpected}],
  "each of the 10 nonzero omega_mu,ab is h4 = b4'/(2 b4) - a4', a4' or H times one of the factors E^a4, E^-a4 b4^(1/2) Cot[z], E^-a4 b4^(1/2) (Sin[z]^2)^(1/12), (Sin[z]^2)^(1/12), " <>
  "none of which vanishes between the degenerate points z = n Pi/2: the x4-part of Omega_xi (3-space) vanishes iff a4 is constant, the x4-parts of Omega_x0 and Omega_xt (the hidden block) iff E^-a4 b4^(1/2) is constant, " <>
  "and the H-part of Omega_xt iff H = 0; so all x4-parts vanish iff a4 and b4 are both constant, and for H > 0 the spin connection never vanishes"];

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
    addCheck["charge_density_is_Krein_form_" <> st, sZeroQ[st, sAdd[st, {J[[5]], sScal[st, -1, sDot[st, Pc, matVec[st, Bm, P]]]}]],
      "J^(x4) = Psi^dagger B Psi with B = -i C gamma^(x4) (Hermitian, signature (8,8)): the charge Q = integral of sqrt g Psi^dagger B Psi d^7x (sqrt g = E^-a4 b4^2 |Cot z| (Sin z^2)^(1/4)) over a slice x4 = const is an indefinite form, " <> statName[st] <>
      " (only the local law d_mu (sqrt g J^mu) = 0 on shell is proved; Q is constant in x4 only if no charge flows through the boundary of the slice, which at the degenerate points z = n Pi/2 is an ASSUMED no-flux condition that this record does not impose)"]]], {st, stats}];
addFormulaText["current", "conserved current and its identity (both statistics)",
  "J^mu = -i Psibar gamma^mu Psi; d_mu (sqrt g J^mu) = -i sqrt g (Ebar Psi + Psibar E), sqrt g = E^-a4[x4] b4[x4]^2 |Cot[z]| (Sin[z]^2)^(1/4); J^x4 = Psi^dagger B Psi; Q = Integral sqrt g Psi^dagger B Psi dx0 dx1 dx2 dx3 dx5 dx6 dx7"];
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
      "(gamma^mu D_mu)^2 Psi = g^mu,nu (D_mu D_nu Psi - Gamma^l_mu,nu D_l Psi) - (R/4) Psi with R = -12 H^2 E^(2 a4)/b4 + 8 a4'^2 - 2 a4'' - 8 a4' b4'/b4 + 4 b4''/b4 + (b4'/b4)^2, for a general " <> statName[st] <>
      " (exact): the second-order consequence of the field equations is consistent with the curvature (integrability)"]]], {st, stats}];
addFormulaText["Lichnerowicz", "second-order identity (both statistics)",
  "(gamma^mu D_mu)^2 Psi = g^mu,nu (D_mu D_nu - Gamma^l_mu,nu D_l) Psi - (R/4) Psi, R = -12 H^2 E^(2 a4[x4])/b4[x4] + 8 a4'[x4]^2 - 2 a4''[x4] - 8 a4'[x4] b4'[x4]/b4[x4] + 4 b4''[x4]/b4[x4] + (b4'[x4]/b4[x4])^2"];

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
  (* h4 = b4'/(2 b4) - a4' is the rate of the hidden block (x0, x5, x6, x7), a4' that of 3-space *)
  expected = {d0p0 + 3 H Cot[6 H x0] (p0[x4, x0] - pt[x4, x0]), 0, 0, 0,
    -d4rho - 3 a4p (rho[x4, x0] + p3[x4, x0]) - 3 h4 (rho[x4, x0] + pt[x4, x0]) - h4 (rho[x4, x0] + p0[x4, x0]), 0, 0, 0};
  okDiv = rftZeroQ[divAll - expected] && mw["divergence_of_diagonal_tensor"] === <|"x0" -> "d0 p0 + 3 H Cot[z] (p0 - p_t)",
    "x4" -> "-d4 rho - 3 a4' (rho + p3) - 3 h (rho + p_t) - h (rho + p0), h = b4'/(2 b4) - a4'"|>;
  eqs = {d4rho == -3 a4p (rho[x4, x0] + p3[x4, x0]) - 3 h4 (rho[x4, x0] + pt[x4, x0]) - h4 (rho[x4, x0] + p0[x4, x0]), d0p0 == -3 H Cot[6 H x0] (p0[x4, x0] - pt[x4, x0])};
  okEqs = Coefficient[expected[[5]], d4rho] === -1 && Coefficient[expected[[1]], d0p0] === 1 &&
    rftZeroQ[expected[[5]] /. d4rho -> eqs[[1, 2]]] && rftZeroQ[expected[[1]] /. d0p0 -> eqs[[2, 2]]];
  (* x0-independent entries: the x0 component is 3 H Cot[z] (p0 - p_t), Cot z != 0 between the degenerate points, so p0 = p_t *)
  T0 = DiagonalMatrix[{p00[x4], p30[x4], p30[x4], p30[x4], -rho0[x4], pt0[x4], pt0[x4], pt0[x4]}];
  div0 = Table[Sum[D[sg T0[[mu, nu]], X[[mu]]], {mu, 8}]/sg - Sum[Gm[[r, mu, nu]] T0[[mu, r]], {mu, 8}, {r, 8}], {nu, 8}];
  okFree = rftZeroQ[div0 - (expected /. {rho -> (rho0[#1] &), p3 -> (p30[#1] &), pt -> (pt0[#1] &), p0 -> (p00[#1] &)})] &&
    rftZeroQ[div0[[1]] /. p00[x4] -> pt0[x4]] && !rftZeroQ[div0[[1]]];
  (* controls: the formula of the metric of 2026-10-14, a missing hidden-direction term and a wrong factor of the Cot[z] term are detected *)
  ctrl = !rftZeroQ[divAll[[5]] - (-d4rho - 3 a4p (p3[x4, x0] - pt[x4, x0]) - (3/2) bu (rho[x4, x0] + pt[x4, x0]))] &&
    !rftZeroQ[divAll[[5]] - (-d4rho - 3 a4p (rho[x4, x0] + p3[x4, x0]) - 3 h4 (rho[x4, x0] + pt[x4, x0]))] &&
    !rftZeroQ[divAll[[1]] - (d0p0 + 2 H Cot[6 H x0] (p0[x4, x0] - pt[x4, x0]))];
  addCheck["energy_exchange_equation", okDiv && okEqs && okFree && ctrl,
    "for a diagonal T^mu_nu = diag(p0, p3, p3, p3, -rho, p_t, p_t, p_t) (order x0..x7) whose entries are functions of x4 and x0, all eight components (every real z, sig cancels): " <>
    "nabla_mu T^mu_x4 = -d rho/d x4 - 3 a4' (rho + p3) - 3 h4 (rho + p_t) - h4 (rho + p0), h4 = b4'/(2 b4) - a4', " <>
    "nabla_mu T^mu_x0 = d p0/d x0 + 3 H Cot[z] (p0 - p_t), and nabla_mu T^mu_nu = 0 identically for nu = x1, x2, x3, x5, x6, x7 (equal to the sympy record, key divergence_of_diagonal_tensor). " <>
    "Each expanding direction dilutes rho plus its own pressure, at the rate a4' for 3-space and h4 for the four directions of the hidden block; the hidden direction balances against the extra times only. " <>
    "For x0-independent entries the x0 component is 3 H Cot[z] (p0 - p_t), so conservation needs p0 = p_t (the hidden direction and the extra times form one block; the Einstein tensor has E^x0_x0 = E^xt_xt). " <>
    "Controls: the formula of the metric of 2026-10-14, the formula without the hidden-direction term and a wrong factor of the Cot[z] term are detected"];
  AppendTo[formulas, <|"key" -> "energy_exchange",
    "description" -> "conservation of a diagonal T = diag(p0, p3, p3, p3, -rho, pt, pt, pt) (order x0..x7) whose entries are functions of x4 and x0 (check energy_exchange_equation); h4 = b4'/(2 b4) - a4'; " <>
      "entry 1: {nabla_mu T^mu_nu, nu = x0..x7} (complete identity); entry 2: the equations equivalent to nabla_mu T^mu_nu = 0; entry 3: the same for x0-independent entries (rho, p3, pt, p0 functions of x4 only)",
    "wl" -> {wl[expected], wl[eqs],
      wl[{Derivative[1][rho][x4] == -3 a4p (rho[x4] + p3[x4]) - 4 h4 (rho[x4] + pt[x4]), p0[x4] == pt[x4]}]}|>]];

(* ------------------------------------------------------------------ formulas: statements and geometry *)
addFormulaText["nontriviality",
  "NON-TRIVIALITY [1] (dirac16complex) and [2] (dirac16complex00): exact content of checks nontriviality_1_dirac16complex, nontriviality_2_dirac16complex00, gammaOmega_per_direction, Omega_vanishes_iff_a4prime_b4prime_and_H_vanish, flat_member_and_curvature, spin_curvature_equals_Riemann",
  "gamma^mu D_mu Psi - gamma^mu d_mu Psi = gamma^mu Omega_mu Psi = ((3/2) H E^a4 b4^(-1/2) gamma^(x0) + (b4'/b4 - a4'/2) gamma^(x4)) Psi (nonzero for every H > 0, all a4 and b4; its square is (9/4) H^2 E^(2 a4)/b4 - (b4'/b4 - a4'/2)^2); " <>
  "per direction gamma^(x0) Omega_x0 = (h4/2) gamma^(x4), gamma^(xi) Omega_xi = (a4'/2) gamma^(x4) (i = 1, 2, 3) and gamma^(xt) Omega_xt = (h4/2) gamma^(x4) + (H/2) E^a4 b4^(-1/2) gamma^(x0) (t = 5, 6, 7), h4 = b4'/(2 b4) - a4'; " <>
  "Omega_mu = 0 for all mu iff a4' = 0, b4' = 0 and H = 0 (H = 0 is a degenerate limit of the metric); [D_mu, D_nu] = (1/2) R_ab,mu,nu S^ab: Omega can be removed by a frame only where the metric is flat " <>
  "(the corrected metric is flat for a4 = 0, b4 = H^2 x4^2 and curved on the record's history)"];
addFormulaText["majorana_negative_control",
  "the notebook's Majorana-type Lagrangian with real components (checks Majorana_Lg_total_derivative_grassmann, Majorana_Lg_commuting_control)",
  "anticommuting real Psi: sqrt g Psi^T C gamma^mu D_mu Psi = d_mu ((1/2) sqrt g Psi^T C gamma^mu Psi) (a total derivative; no field equation; Psi^T C Psi = 0); commuting real Phi: Euler-Lagrange expression 2 sqrt g C gamma^mu D_mu Phi and Phi^T C gamma^mu Phi = 0"];
addFormulaText["equation_of_state_definitions", "pressures and equations of state from the diagonal components (SPEC section 4)",
  "rho = -T^x4_x4, p3 = T^x1_x1, p_t = T^x5_x5, p0 = T^x0_x0; w3 = p3/rho, w_t = p_t/rho, w0 = p0/rho; homogeneous on shell: w3 = w_t = w0 = (S U' - U)/(m S + U)"];
addFormulaText["hidden_direction_hermiticity", "role of the spin-connection term in the quantum theory (check good_sector_hermiticity_curved)",
  "(Sin[z]^2)^(1/4) [p (d0 + (3/2) H Cot[z]) q + ((d0 + (3/2) H Cot[z]) p) q] = d0 ((Sin[z]^2)^(1/4) p q): the hidden-direction operator E^a4 b4^(-1/2) (Tan[z] d0 + (3/2) H) gamma^(x0) is antisymmetric for the measure sqrt g/f0 dx0 = b4^(3/2) (Sin[z]^2)^(1/4) dx0 " <>
  "up to the boundary term (Sin[z]^2)^(1/4) p q, which vanishes where Sin z = 0 and not where Cos z = 0; without the spin-connection term (3/2) H the operator is not formally Hermitian for this measure and these variables"];
addFormula["metric", "the corrected metric of 2026-10-16 (SPEC section 1, version 2), coordinates x0..x7, every real z", rftMetricAuthor];
addFormula["vielbein_diagonal", "f_a in e^a_mu = f_a delta^a_mu, a = x0..x7 (f0 signed)", f];
addFormula["sqrt_det_g", "sqrt|det g| = rftSig f0...f7, rftSig = sign(Cot z) = +-1", rftSig E^(-a4[x4]) b4[x4]^2 Cot[6 H x0] (Sin[6 H x0]^2)^(1/4)];
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
    "T^mu_mu (no sum) = L0 - K_mu with K_mu = (1/(2 f_mu)) (Psibar gamma^(mu) d_mu Psi - d_mu Psibar gamma^(mu) Psi) (f_0 = E^-a4 b4^(1/2) Cot z, f_5..7 = E^-a4 b4^(1/2) (Sin z^2)^(1/12)): no spin-connection term survives in the diagonal components " <>
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
  ok = sZeroQ[st, sAdd[st, {Tsym[[5, 1]], sScal[st, 1/4, B40], sScal[st, -f[[1]]/4, B04]}]] &&
       sZeroQ[st, sAdd[st, {Tsym[[1, 5]], sScal[st, 1/f[[1]]^2, Tsym[[5, 1]]]}]] &&
       !sZeroQ[st, sAdd[st, {Tsym[[5, 1]], sScal[st, 1/4, B40], sScal[st, -Cot[rftZ]/4, B04]}]];
  addCheck["T_x4_x0_component_" <> st, ok,
    "T^x4_x0 = -(1/4)(B40 - f0 B04), f0 = E^-a4 b4^(1/2) Cot[z], B40 = Psibar gamma^(x4) d0 Psi - d0 Psibar gamma^(x4) Psi, B04 = Psibar gamma^(x0) d4 Psi - d4 Psibar gamma^(x0) Psi " <>
    "(Omega_x0 = (1/2) h4 f0 gamma^(x0) gamma^(x4) drops out: {gamma^(x4), gamma^(x0) gamma^(x4)} = 0), and T^x0_x4 = g^00 g_44 T^x4_x0 = -E^(2 a4) b4^(-1) Tan[z]^2 T^x4_x0 (" <> statName[st] <>
    "); control: the formula of the metric of 2026-10-14 (f0 -> Cot[z]) is detected"]];
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
  addFormulaText["EMT_homogeneous_on_shell", "homogeneous states (Psi depends on x4 only): K_mu = 0 for mu != x4 and K_x4 = (m + U') S on shell (the scalar factor E^(a4/2) b4^(-1) of Psi and Psibar cancels in K_x4)",
    "rho = m S + U(S); p3 = p_t = p0 = S U'(S) - U(S); w = (S U' - U)/(m S + U); for U = (lam/2) S^2: rho = m S + lam S^2/2, p = lam S^2/2, w = lam S/(2 m + lam S); S = E^a4 b4^(-2) S_chi with S_chi constant on shell (check exact_solution_nonlinear_homogeneous_C)"];
  addFormulaText["EMT_offdiagonal_x4_x0", "the x4-x0 component of the symmetric tensor (Omega_x4 = 0; Omega_x0 drops out)",
    "T^x4_x0 = -(1/4) (B40 - E^-a4 b4^(1/2) Cot[z] B04), B40 = Psibar gamma^(x4) d0 Psi - d0 Psibar gamma^(x4) Psi, B04 = Psibar gamma^(x0) d4 Psi - d4 Psibar gamma^(x0) Psi; T^x0_x4 = -E^(2 a4) b4^(-1) Tan[z]^2 T^x4_x0 (T_x4x0 = T_x0x4)"]];
];

(* ================================================================== PART solutions *)
If[MemberQ[{"solutions", "solutions-G"}, part],
section["exact solutions: definitions"];
(* Homogeneous reduction for the corrected metric.  For Psi = Fsc (Sin z^2)^(al/2) chi(x4), Fsc = E^(a4/2) b4^(-1)
   (Fsc'/Fsc = -vg removes the term vg gamma^(x4)), the hidden-direction terms give
   E^a4 b4^(-1/2) (Tan z d0 + (3/2) H) (Sin z^2)^(al/2) = muA[al] (Sin z^2)^(al/2), muA[al] = (3/2) H (4 al + 1) E^a4 b4^(-1/2),
   and the field equation becomes chi' = (-V gamma^(x4) + muA[al] K) chi with K = gamma^(x4) gamma^(x0), K^2 = 1,
   {K, gamma^(x4)} = 0.  muA depends on x4 through E^a4 b4^(-1/2), so exp(M x4) is not a solution for m != 0 and
   general a4, b4; closed forms exist for m = 0 (any al) and for al = -1/4 (any m). *)
Kmat = g[[5]] . g[[1]];
Fsc = E^(a4[x4]/2)/b4[x4];
muA[al_] := (3/2) H (4 al + 1) E^a4[x4]/Sqrt[b4[x4]];
If[part === "solutions", addCheck["solution_matrix_square",
  Kmat . Kmat == id16 && Kmat . g[[5]] + g[[5]] . Kmat == z16 && g[[5]] . g[[5]] == -id16 &&
  Transpose[Kmat] . Cm + Cm . Kmat == z16 && Transpose[g[[5]]] . Cm + Cm . g[[5]] == z16 && Transpose[Cm . g[[5]]] == -Cm . g[[5]] &&
  rftZeroQ[D[Fsc, x4]/Fsc + vg] &&
  rftZeroQ[(E^a4[x4]/Sqrt[b4[x4]]) (Tan[rftZ] D[(Sin[rftZ]^2)^(al/2), x0] + (3/2) H (Sin[rftZ]^2)^(al/2)) (Sin[rftZ]^2)^(-al/2) - muA[al]],
  "K = gamma^(x4) gamma^(x0) satisfies K^2 = I16, {K, gamma^(x4)} = 0, (gamma^(x4))^2 = -I16, K^T C + C K = 0 and gamma^(x4)^T C + C gamma^(x4) = 0 (C gamma^(x4) antisymmetric); " <>
  "Fsc = E^(a4/2) b4^(-1) has Fsc'/Fsc = -(b4'/b4 - a4'/2), and E^a4 b4^(-1/2) (Tan z d0 + (3/2) H) (Sin z^2)^(al/2) = (3/2) H (4 al + 1) E^a4 b4^(-1/2) (Sin z^2)^(al/2) for every real z: " <>
  "so Psi = Fsc (Sin z^2)^(al/2) chi(x4) solves the field equation iff chi' = (-V gamma^(x4) + muA K) chi, muA = (3/2) H (4 al + 1) E^a4 b4^(-1/2); every bilinear chi^dagger C Y chi with Y^T C + C Y = 0 generators is conserved"]];
(* exact zero test for the explicit solutions: Cosh[ib[x4]], Sinh[ib[x4]] (Cosh^2 = 1 + Sinh^2) and Cos[mm x4],
   Sin[mm x4] (Cos^2 = 1 - Sin^2) are polynomial variables; coefficient by coefficient of the polynomial in the
   constants cA[..], cAc[..]; the coefficients in the normal form of the package (every real z) *)
zeroQX[e_] := Module[{t, vars, coefs, red},
  t = Expand[(e /. rftTrigRules) /. {Cosh[ib[x4]] -> chv, Sinh[ib[x4]] -> shv, Cos[mm x4] -> cmv, Sin[mm x4] -> smv}];
  If[t === 0, Return[True]];
  vars = Union[Cases[t, (cA | cAc)[__], {0, Infinity}]];
  coefs = If[vars === {}, {t}, Last /@ CoefficientRules[t, vars]];
  red[c_] := Module[{u = Expand[Numerator[Together[c]]]},
    u = Expand[u /. {chv^n_Integer /; n >= 2 :> (1 + shv^2)^Quotient[n, 2] chv^Mod[n, 2],
      cmv^n_Integer /; n >= 2 :> (1 - smv^2)^Quotient[n, 2] cmv^Mod[n, 2]}];
    rftReduceCos[u]];
  And @@ (red[#] === 0 & /@ coefs)];
gZeroQX[a_Association] := And @@ (zeroQX /@ Values[a]);
sZeroQX["C", e_] := zeroQX[e]; sZeroQX["G", e_] := gZeroQX[e];
If[$rftNK > 0, DistributeDefinitions[zeroQX, gZeroQX, sZeroQX]];   (* the zero tests below run on the subkernels *)
(* T_sym, divergence and field equation for a given explicit field *)
TsymOf[st_, P_, Pc_] := Module[{pb = rftPsibar[st, Pc], L0, Bm2},
  L0 = rftL0[st, rftGeo0, P, Pc];
  Bm2 = Table[sAdd[st, {sDot[st, vecMat[st, pb, gup[[r]]], rftDPsi[st, rftGeo0, P, s]], sScal[st, -1, sDot[st, vecMat[st, rftDPsibar[st, rftGeo0, Pc, s], gup[[r]]], P]]}], {r, 8}, {s, 8}];
  Table[sAdd[st, {If[n == mu, L0, sZero[st]], sScal[st, -1/4, Bm2[[n, mu]]], sScal[st, -1/4 rftG0[[mu, mu]] rftGinv0[[n, n]], Bm2[[mu, n]]]}], {n, 8}, {mu, 8}]];
divT[st_, T_] := Table[sAdd[st, {
    sScal[st, 1/sg, sAdd[st, Table[sD[st, sScal[st, sg, T[[mu, nu]]], X[[mu]]], {mu, 8}]]],
    sScal[st, -1, sAdd[st, Flatten[Table[If[Gm[[r, mu, nu]] === 0, sZero[st], sScal[st, Gm[[r, mu, nu]], T[[mu, r]]]], {mu, 8}, {r, 8}]]]]}], {nu, 8}];
];

(* ================================================================== PART solutions *)
If[part === "solutions",
section["exact solutions (i), linear"];
Block[{U = Function[s, lam s^2/2], u1 = 0},
  (* (i-a) m = 0, al general: chi = (Cosh[ib] + Sinh[ib] K) chi0 with ib' = muA[al];
     (i-b) al = -1/4 (muA = 0), m general: chi = (Cos[mm x4] - Sin[mm x4] gamma^(x4)) chi0 *)
  Do[Module[{fam = famSpec[[1]], alv = famSpec[[2]], mmv = famSpec[[3]], Pm, pre, rules, Psol, Pcsol, Eres, T, dv, J, divJ, Sx, Schi, zr, okE, okT, okJ, okR, okS, tag},
    Block[{lam = 0, m = mmv},
      Pm = If[fam === "a", Cosh[ib[x4]] id16 + Sinh[ib[x4]] Kmat, Cos[mm x4] id16 - Sin[mm x4] g[[5]]];
      pre = Fsc (Sin[rftZ]^2)^(alv/2);
      rules = {Derivative[2][ib][x4] -> D[muA[alv], x4], Derivative[1][ib][x4] -> muA[alv]};
      If[st === "C",
        Psol = pre Pm . Table[cA[A], {A, 16}];
        Pcsol = pre Pm . Table[cAc[A], {A, 16}];
        Schi = Table[cAc[A], {A, 16}] . Cm . Table[cA[A], {A, 16}],
        Psol = Table[gAdd[Table[<|{k} -> (pre Pm . Table[cA[B, k], {B, 16}])[[A]]|>, {k, rftGN}]], {A, 16}];
        Pcsol = Table[gAdd[Table[<|{k + rftGN} -> (pre Pm . Table[cAc[B, k], {B, 16}])[[A]]|>, {k, rftGN}]], {A, 16}];
        Schi = gAdd[Flatten[Table[gMul[<|{k1 + rftGN} -> 1|>, <|{k2i} -> Table[cAc[B, k1], {B, 16}] . Cm . Table[cA[B, k2i], {B, 16}]|>], {k1, rftGN}, {k2i, rftGN}]]]];
      Eres = rftE[st, rftGeo0, Psol, Pcsol];
      T = TsymOf[st, Psol, Pcsol];
      dv = divT[st, T];
      J = Table[sScal[st, -I, bilM[st, Pcsol, gup[[mu]], Psol]], {mu, 8}];
      divJ = sAdd[st, Table[sD[st, sScal[st, sg, J[[mu]]], X[[mu]]], {mu, 8}]];
      Sx = rftSbil[st, Psol, Pcsol];
      (* the symbolic exponent al is removed before the zero test: the field equation is divided by (Sin z^2)^(al/2), the
         bilinears by (Sin z^2)^al; the 28 zero tests (16 field equation, 8 divergence, current, rho = m S, S) run on the subkernels *)
      zr = pZeroQ[With[{s = st, q = rules}, sZeroQX[s, sMap[s, (# /. q) &, #]] &],
        Join[sScal[st, (Sin[rftZ]^2)^(-alv/2), #] & /@ Eres, sScal[st, (Sin[rftZ]^2)^(-alv), #] & /@ dv,
          {sScal[st, (Sin[rftZ]^2)^(-alv), divJ], sScal[st, (Sin[rftZ]^2)^(-alv), sAdd[st, {T[[5, 5]], sScal[st, m, Sx]}]],
           sScal[st, (Sin[rftZ]^2)^(-alv), sAdd[st, {Sx, sScal[st, -pre^2, Schi]}]]}]];
      okE = And @@ zr[[1 ;; 16]]; okT = And @@ zr[[17 ;; 24]]; okJ = zr[[25]]; okR = zr[[26]]; okS = zr[[27]];
      tag = If[fam === "a", "m0_", "quarter_"];
      addCheck["exact_solution_x4_x0_" <> tag <> st, okE && okT && okJ && okR && okS && !sZeroQ[st, Schi],
        "exact solution (" <> statName[st] <> ", U = 0, general a4 and b4, every real z): " <>
        If[fam === "a",
          "m = 0, al arbitrary: Psi = E^(a4/2) b4^(-1) (Sin z^2)^(al/2) (Cosh[I] + Sinh[I] K) chi, K = gamma^(x4) gamma^(x0), I(x4) = int muA dx4, muA = (3/2) H (4 al + 1) E^a4 b4^(-1/2) " <>
            "(the symbol I is general, its first and second derivatives are replaced by muA and muA')",
          "al = -1/4 (muA = 0), m arbitrary: Psi = E^(a4/2) b4^(-1) (Sin z^2)^(-1/8) (Cos[m x4] - Sin[m x4] gamma^(x4)) chi"] <>
        ", with constant chi (16 free complex constants" <> If[st === "G", " per Grassmann generator", ""] <> "); " <>
        "it satisfies the field equation (a test of every term: the hidden-direction terms E^a4 b4^(-1/2) (Tan z d0 + (3/2) H) gamma^(x0), the time term (b4'/b4 - a4'/2) gamma^(x4) compensated by the factor E^(a4/2) b4^(-1)), " <>
        "nabla_mu T_sym^mu_nu = 0 for all 8 nu and d_mu (sqrt g J^mu) = 0 hold exactly at it; S = Psibar Psi = E^a4 b4^(-2) (Sin z^2)^(" <> If[fam === "a", "al", "-1/4"] <> ") chi^dagger C chi != 0 and rho = -T^x4_x4 = m S. " <>
        "For m != 0 and al != -1/4 the system chi' = (-m gamma^(x4) + muA K) chi has no closed form for general a4, b4 (muA varies with x4, [M(x), M(y)] != 0); in the metric of 2026-10-14 muA was the constant 3 H (2 al + 1)"]]],
    {famSpec, {{"a", al, 0}, {"b", -1/4, mm}}}, {st, stats}];
  section["exact solutions (ii), nonlinear commuting"];
  (* (ii) nonlinear homogeneous, commuting: Psi = Fsc chi(x4) for EVERY solution chi of the homogeneous system
     chi' = M(S_chi) chi, M(S) = -(m + lam Fsc^2 S) gamma^(x4) + cg K, S_chi = chi^dagger C chi.  The functions chi_A =
     ph[A][x4] and their conjugates phc[A][x4] are general; after the expressions are built, their first and second
     derivatives are replaced by the equation (first the second derivatives by the x4 derivative of the right side, then
     the first derivatives), and the result must vanish identically. *)
  Module[{chi = Table[ph[A][x4], {A, 16}], chic = Table[phc[A][x4], {A, 16}], Sch, Mfull, rhs, rhsc, r1, r2, Psol, Pcsol, Eres, T, dv, Sx, zr, okE, okS, okT, okRP},
    Sch = chic . Cm . chi;
    Mfull = -(m + lam Fsc^2 Sch) g[[5]] + cg Kmat;
    rhs = Mfull . chi; rhsc = Mfull . chic;   (* M is real (real gammas, real S_chi): the conjugate equation *)
    r1 = Join[Table[Derivative[1][ph[A]][x4] -> rhs[[A]], {A, 16}], Table[Derivative[1][phc[A]][x4] -> rhsc[[A]], {A, 16}]];
    r2 = Join[Table[Derivative[2][ph[A]][x4] -> D[rhs[[A]], x4], {A, 16}], Table[Derivative[2][phc[A]][x4] -> D[rhsc[[A]], x4], {A, 16}]];
    Psol = Fsc chi; Pcsol = Fsc chic;
    Sx = rftSbil["C", Psol, Pcsol];
    Eres = rftE["C", rftGeo0, Psol, Pcsol];
    T = TsymOf["C", Psol, Pcsol]; dv = divT["C", T];
    (* the 34 zero tests run on the subkernels: 16 field equation (1-16), S_chi' = 0 (17), S = Fsc^2 S_chi (18),
       8 divergence (19-26), rho and p (27-34) *)
    zr = pZeroQ[With[{q1 = r1, q2 = r2}, rftZeroQ[(# /. q2) /. q1] &],
      Join[Eres, {D[Sch, x4], Sx - Fsc^2 Sch}, dv, {-T[[5, 5]] - (m Sx + lam Sx^2/2)}, Table[T[[mu, mu]] - lam Sx^2/2, {mu, {1, 2, 3, 4, 6, 7, 8}}]]];
    okE = And @@ zr[[1 ;; 16]]; okS = zr[[17]] && zr[[18]]; okT = And @@ zr[[19 ;; 26]]; okRP = And @@ zr[[27 ;; 34]];
    addCheck["exact_solution_nonlinear_homogeneous_C", okE && okS && okT && okRP,
      "nonlinear solutions of dirac16complex00 with U = (lam/2) S^2, general a4 and b4, every real z: for EVERY solution chi(x4) of the homogeneous system chi' = M chi, " <>
      "M = -(m + lam E^a4 b4^(-2) S_chi) gamma^(x4) + (3/2) H E^a4 b4^(-1/2) K, K = gamma^(x4) gamma^(x0), S_chi = chi^dagger C chi " <>
      "(checked by substituting the system for the first and second derivatives of 16 general complex functions chi_A and their conjugates): Psi = E^(a4/2) b4^(-1) chi solves the field equation exactly; " <>
      "S_chi is constant (M^T C + C M = 0), so the system is LINEAR with the effective mass m + lam E^a4 b4^(-2) S0 once S_chi = S0 is fixed by chi(0) (global existence and uniqueness), and S = Psibar Psi = E^a4 b4^(-2) S0; " <>
      "nabla_mu T^mu_nu = 0 for all nu, and the diagonal components are T^x4_x4 = -rho, T^mu_mu = p (mu != x4) with rho = m S + lam S^2/2 = m S + U, p = lam S^2/2 = S U' - U exactly (homogeneous on-shell forms; p0 = p_t as conservation requires). " <>
      "The system has no closed-form solution for general a4, b4 (both the effective mass and the coefficient of K depend on x4)"]];
];
addFormulaText["exact_solutions",
  "exact solutions used as test points (checks exact_solution_*), general a4 and b4, every real z; K = g[x4].g[x0], Fsc = E^(a4/2) b4^(-1), muA = (3/2) H (4 al + 1) E^a4 b4^(-1/2)",
  "(i-a) U = 0, m = 0: Psi = Fsc (Sin[z]^2)^(al/2) (Cosh[I] + Sinh[I] K) chi, I' = muA; (i-b) U = 0, al = -1/4: Psi = Fsc (Sin[z]^2)^(-1/8) (Cos[m x4] - Sin[m x4] g[x4]) chi; " <>
  "(ii) U = (lam/2) S^2, homogeneous, commuting: Psi = Fsc chi for every solution of chi' = (-(m + lam E^a4 b4^(-2) S0) g[x4] + (3/2) H E^a4 b4^(-1/2) K) chi, S0 = chi^dagger C chi constant, S = E^a4 b4^(-2) S0; " <>
  "(iii) Grassmann, m = 0: Psi = Fsc sum_k [P c_k + lam S0 eta_k] theta_k, P = Cosh[I0] + Sinh[I0] K, I0' = (3/2) H E^a4 b4^(-1/2), eta_k = -P g[x4] (Ic + Is K) c_k, Ic' = Fsc^2 Cosh[2 I0], Is' = Fsc^2 Sinh[2 I0], S0 = sum_kl thetabar_k theta_l c_k^dagger C c_l; " <>
  "at (ii) and (iii): rho = m S + lam S^2/2, p3 = p_t = p0 = lam S^2/2"];
];

(* ================================================================== PART solutions-G *)
(* (iii) nonlinear homogeneous Grassmann solution for m = 0: Psi = sum_k [U0 c_k + lam S0 U1 c_k] theta_k with
   U0 = Fsc P, U1 = Fsc W, P = Cosh[I0] + Sinh[I0] K (I0' = cg), W = -P gamma^(x4) (Ic + Is K), Ic' = Fsc^2 Cosh[2 I0],
   Is' = Fsc^2 Sinh[2 I0] (variation of constants for eta' = cg K eta - Fsc^2 gamma^(x4) P c, using
   P^-1 gamma^(x4) P = gamma^(x4) (Cosh[2 I0] + Sinh[2 I0] K)); S0 = sum_kl thetabar_k theta_l c_k^dagger C c_l.  The
   functions ib (= I0), ibc, ibs are general symbols whose first and second derivatives are replaced by the integrands.
   For m != 0 the linear system chi' = (-m gamma^(x4) + cg K) chi has no closed-form fundamental matrix for general a4,
   b4 (cg depends on x4); the nonlinear commuting case (ii) covers every m.
   Method (as for the metric of 2026-10-14, 2026-10-15): every statement is reduced EXACTLY to 16 x 16 matrix
   identities, the reduction being the Grassmann bookkeeping of a homogeneous field whose components are
   U_d0 c_k theta_k + sigma U_d1 c_k theta_k (sigma = lam S0 even, sigma^2 times any bilinear = 0):
     field equation      gamma^mu D_mu Psi - lam S Psi = sum_k theta_k [D U0] c_k + sigma sum_k theta_k [D U1 - Fsc^2 U0] c_k
                         (D = gamma^(x4) d4 + gamma^mu Omega_mu on homogeneous columns; S Psi = Fsc^2 S0 Psi^(1));
     S                   Psibar Psi = B[U0^T C U0] + sigma B[U0^T C U1 + U1^T C U0], B[Y] = sum_kl thetabar_k theta_l c_k^dagger Y c_l;
     kinetic tensor      T_kin = B[Y0] + sigma B[Y1], Y0 = sum U_d1,0^T N U_d2,0, Y1 = sum (U_d1,1^T N U_d2,0 + U_d1,0^T N U_d2,1),
                         N the coefficient matrix of the bilinear T_kin in the jets (Psibar, d4 Psibar) x (Psi, d4 Psi),
                         taken from the package's T_sym of a general homogeneous field;
     potential part      -delta V, V = (lam/2) S^2 = sigma B[(1/2) Fsc^4 C].
   The field equation and S are in addition evaluated directly in the explicit Grassmann algebra with 16 generic complex
   constants per generator (this checks the reduction for them), and the contraction of the kinetic tensor is
   cross-checked against the direct explicit-algebra value of T_kin^x0_x0. *)
If[part === "solutions-G",
section["exact solution (iii), nonlinear Grassmann (m = 0): matrix identities"];
Block[{U = Function[s, lam s^2/2], u1 = 0, m = 0},
Module[{Pm, Wm, integrand, r1, r2, F2, U0, U1, Uj, Dop, idE0, idE1, idS0, idS1, zr, okId,
    Pg, Pcg, Tk, vc, vp, Yof, okBil, Ys, Yt, Vy, divY, rp, zr2, okRP, okCons, ctrlCons, chik, chick, S0g, Psol, Pcsol, Sx, Eres, zr3,
    okEx, okSx, okS02, Bof, Tdirect, okLemma, zt},
  F2 = Fsc^2;
  Pm = Cosh[ib[x4]] id16 + Sinh[ib[x4]] Kmat;
  Wm = -Pm . g[[5]] . (ibc[x4] id16 + ibs[x4] Kmat);
  integrand = {F2 (Cosh[ib[x4]]^2 + Sinh[ib[x4]]^2), F2 2 Sinh[ib[x4]] Cosh[ib[x4]]};
  r1 = Join[{Derivative[1][ib][x4] -> cg}, Thread[{Derivative[1][ibc][x4], Derivative[1][ibs][x4]} -> integrand]];
  r2 = Join[{Derivative[2][ib][x4] -> D[cg, x4]}, Thread[{Derivative[2][ibc][x4], Derivative[2][ibs][x4]} -> D[integrand, x4]]];
  zt = With[{q1 = r1, q2 = r2}, zeroQX[(# /. q2) /. q1] &];
  U0 = Fsc Pm; U1 = Fsc Wm;
  Uj = {{U0, U1}, {D[U0, x4], D[U1, x4]}};        (* jets d = (), (x4): {U_d0, U_d1} *)
  Dop[V_] := g[[5]] . D[V, x4] + gOm . V;         (* gamma^mu D_mu on homogeneous columns *)
  idE0 = Dop[U0]; idE1 = Dop[U1] - F2 U0;
  idS0 = Transpose[U0] . Cm . U0 - F2 Cm; idS1 = Transpose[U0] . Cm . U1 + Transpose[U1] . Cm . U0;
  zr = pZeroQ[zt, Flatten[{idE0, idE1, idS0, idS1}]];
  okId = And @@ zr;
  Print["   matrix identities of the field equation and of S: ", okId];
  section["exact solution (iii): kinetic tensor by contraction"];
  Pg = Table[ph[A][x4], {A, 16}]; Pcg = Table[phc[A][x4], {A, 16}];
  Tk = Block[{U = (0 &)}, TsymOf["C", Pg, Pcg]];   (* T_kin of a general homogeneous field (m = 0): a bilinear in the jets *)
  vc = Join[Pcg, D[Pcg, x4]]; vp = Join[Pg, D[Pg, x4]];
  okBil = True;
  Yof[e_] := Module[{ca = CoefficientArrays[e, Join[vc, vp]], c2, NN, blk},
    c2 = If[Length[ca] >= 3, Normal[ca[[3]]], ConstantArray[0, {64, 64}]];
    NN = c2[[1 ;; 32, 33 ;; 64]] + Transpose[c2[[33 ;; 64, 1 ;; 32]]];
    okBil = okBil && Length[ca] <= 3 && rftZeroQ[e - vc . NN . vp];
    blk[d1_, d2_] := NN[[16 (d1 - 1) + 1 ;; 16 d1, 16 (d2 - 1) + 1 ;; 16 d2]];
    {Sum[Transpose[Uj[[d1, 1]]] . blk[d1, d2] . Uj[[d2, 1]], {d1, 2}, {d2, 2}],
     Sum[Transpose[Uj[[d1, 2]]] . blk[d1, d2] . Uj[[d2, 1]] + Transpose[Uj[[d1, 1]]] . blk[d1, d2] . Uj[[d2, 2]], {d1, 2}, {d2, 2}]}];
  Ys = Table[Yof[Tk[[n, mu]]], {n, 8}, {mu, 8}];
  Vy = {0 Cm, F2^2/2 Cm};
  Yt = Table[Ys[[n, mu]] - If[n == mu, Vy, {0, 0}], {n, 8}, {mu, 8}];
  divY[YY_, nu_, j_] := Sum[D[sg YY[[mu, nu, j]], X[[mu]]], {mu, 8}]/sg - Sum[If[Gm[[r, mu, nu]] === 0, 0, Gm[[r, mu, nu]] YY[[mu, r, j]]], {mu, 8}, {r, 8}];
  (* -T^x4_x4 = -T_kin^x4_x4 + V and T^i_i = T_kin^i_i - V: rho = (lam/2) S^2 and p = (lam/2) S^2 (m = 0) need
     T_kin^x4_x4 = 0 and T_kin^i_i = lam S^2 = sigma B[Fsc^4 C] *)
  rp = Join[{Ys[[5, 5, 1]], Ys[[5, 5, 2]]}, Flatten[Table[{Ys[[i, i, 1]], Ys[[i, i, 2]] - F2^2 Cm}, {i, {1, 2, 3, 4, 6, 7, 8}}], 1]];
  zr2 = pZeroQ[zt, Flatten[Join[rp, Table[divY[Yt, nu, j], {nu, 8}, {j, 2}]]]];
  okRP = And @@ zr2[[1 ;; 16 256]]; okCons = And @@ zr2[[16 256 + 1 ;;]];
  ctrlCons = !(And @@ pZeroQ[zt, Flatten[divY[Ys, 5, 2]]]);   (* the kinetic part alone is not conserved: V depends on x4 *)
  Print["   bilinear extraction: ", okBil, "; rho and p: ", okRP, "; conservation: ", okCons, "; control: ", ctrlCons];
  section["exact solution (iii): explicit Grassmann algebra"];
  chik = Table[Table[cA[B, k], {B, 16}], {k, rftGN}]; chick = Table[Table[cAc[B, k], {B, 16}], {k, rftGN}];
  S0g = gAdd[Flatten[Table[gMul[<|{k1 + rftGN} -> 1|>, <|{k2i} -> chick[[k1]] . Cm . chik[[k2i]]|>], {k1, rftGN}, {k2i, rftGN}]]];
  Psol = Table[gAdd[Flatten[Table[{<|{k} -> (U0 . chik[[k]])[[A]]|>, gScal[lam, gMul[S0g, <|{k} -> (U1 . chik[[k]])[[A]]|>]]}, {k, rftGN}]]], {A, 16}];
  Pcsol = gConj /@ Psol;
  Sx = rftSbil["G", Psol, Pcsol];
  Eres = rftE["G", rftGeo0, Psol, Pcsol];
  Bof[Y_] := gAdd[Flatten[Table[gMul[<|{k1 + rftGN} -> 1|>, <|{k2i} -> chick[[k1]] . Y . chik[[k2i]]|>], {k1, rftGN}, {k2i, rftGN}]]];
  (* T_kin^x0_x0 = K - (1/2) B00 directly in the explicit algebra (K = the kinetic part of L0; T_sym^x0_x0 = L0 - (1/2) B00) *)
  Tdirect = Module[{pb = rftPsibar["G", Pcsol], K0, B00},
    K0 = rftKin["G", rftGeo0, Psol, Pcsol];
    B00 = sAdd["G", {sDot["G", vecMat["G", pb, gup[[1]]], rftDPsi["G", rftGeo0, Psol, 1]], sScal["G", -1, sDot["G", vecMat["G", rftDPsibar["G", rftGeo0, Pcsol, 1], gup[[1]]], Psol]]}];
    sAdd["G", {K0, sScal["G", -1/2, B00]}]];
  zr3 = pZeroQ[With[{q1 = r1, q2 = r2}, gZeroQX[gMapCoeff[(#1 /. q2) /. q1 &, #]] &],
    Join[Eres, {gAdd[{Sx, gScal[-F2, S0g]}], gMul[S0g, S0g], gAdd[{Tdirect, gScal[-1, Bof[Ys[[1, 1, 1]]]], gScal[-lam, gMul[S0g, Bof[Ys[[1, 1, 2]]]]]}]}]];
  okEx = And @@ zr3[[1 ;; 16]]; okSx = zr3[[17]]; okS02 = !zr3[[18]]; okLemma = zr3[[19]];
  Print["   explicit algebra: field equation ", okEx, ", S ", okSx, ", S0^2 != 0 ", okS02, ", contraction = direct T_kin^x0_x0 ", okLemma];
  addCheck["exact_solution_nonlinear_homogeneous_G", okId && okBil && okRP && okCons && ctrlCons && okEx && okSx && okS02 && okLemma,
    "exact nonlinear solution of dirac16complex (explicit Grassmann algebra, N = 2) with U = (lam/2) S^2 and m = 0, general a4 and b4, every real z: " <>
    "Psi = E^(a4/2) b4^(-1) sum_k [P c_k + lam S0 eta_k] theta_k, P = Cosh[I0] + Sinh[I0] K, K = gamma^(x4) gamma^(x0), I0 = int (3/2) H E^a4 b4^(-1/2) dx4, " <>
    "eta_k = -P gamma^(x4) (Ic + Is K) c_k, Ic = int E^a4 b4^(-2) Cosh[2 I0] dx4, Is = int E^a4 b4^(-2) Sinh[2 I0] dx4 (eta_k solves eta_k' = cg K eta_k - E^a4 b4^(-2) gamma^(x4) P c_k), " <>
    "S0 = sum_kl thetabar_k theta_l c_k^dagger C c_l (the expansion terminates because S0^2 Psi = 0). Verified: the 16 x 16 matrix identities D U0 = 0, D U1 = E^a4 b4^(-2) U0, U0^T C U0 = E^a4 b4^(-2) C, U0^T C U1 + U1^T C U0 = 0 " <>
    "(U0 = E^(a4/2) b4^(-1) P, U1 = E^(a4/2) b4^(-1) eta-matrix, D = gamma^(x4) d4 + gamma^mu Omega_mu); in the explicit algebra with 16 generic complex constants per generator: " <>
    "the field equation holds for all 16 components and S = E^a4 b4^(-2) S0 (S0 even, nilpotent, S0^2 != 0); the energy-momentum tensor by the exact contraction T_kin = B[Y0] + lam S0 B[Y1] " <>
    "(the bilinear coefficient matrix taken from the package's T_sym of a general homogeneous field, reproducing it exactly; the contraction equals the direct explicit-algebra value of T_kin^x0_x0): " <>
    "nabla_mu T^mu_nu = 0 for all 8 nu (control: the kinetic part alone is not conserved), rho = p3 = p_t = p0 = (lam/2) S^2 with S = E^a4 b4^(-2) S0 as Grassmann-algebra elements. " <>
    "Scope: m = 0 only; for m != 0 the linear system has no closed-form fundamental matrix for general a4, b4 (the metric of 2026-10-14 had the constant coefficient 3 H and a closed form for every m); " <>
    "for every m the commuting nonlinear case is check exact_solution_nonlinear_homogeneous_C"]]];
];

(* ================================================================== PART quantisation *)
If[part === "quantisation",
section["canonical quantisation"];
Ldata = lagData[{"G"}];
Module[{LG = Ldata["G"]["L"], okPi = True, K, piRow},
  (* Wolfram position 5 = x4, the time *)
  piRow = vScal["G", sg/2, vecMat["G", fld["G"]["Psic"], Cm . g[[5]]]];
  Do[okPi = okPi && gZeroQ[gAdd[{rftPartialD["G", LG, ph[A, k], 5], gScal[-1, gMul[piRow[[A]], gTheta[k]]]}]], {A, 16}, {k, rftGN}];
  addCheck["canonical_momentum",
    okPi && Cm . g[[5]] == I Bm,
    "dL/d(d4 ph[A,k]) = pi_A theta_k with pi_A = (1/2) sqrt g (Psi^dagger C gamma^(x4))_A = (i/2) sqrt g (Psi^dagger B)_A, sqrt g = E^-a4 b4^2 |Cot z| (Sin z^2)^(1/4) (the momentum conjugate to Psi_A as a right derivative; C gamma^(x4) = i B): " <>
    "pi depends on Psi^dagger only, a second-class constraint as for Dirac's field"];
  K = sg Cm . g[[5]];
  addCheck["first_order_form_and_anticommutator",
    ConjugateTranspose[Cm . g[[5]]] == -Cm . g[[5]] && I Inverse[Cm . g[[5]]] == Bm && Bm . Bm == id16 && rftZeroQ[K - I sg Bm],
    "up to a total divergence L = Psi^dagger K d4 Psi - (terms without d4), K = sqrt g C gamma^(x4) = i sqrt g B (C gamma^(x4) anti-Hermitian with i (C gamma^(x4))^-1 = B; invertible since g^44 != 0); " <>
    "the canonical (Dirac-bracket) anticommutator is {Psi_A(x), Psi^dagger_C(y)} = i (K^-1)_AC delta^7(x - y) = B_AC delta^7(x - y)/sqrt|g| on a slice x4 = const (exact: i K^-1 = B/sqrt g, sqrt g = E^-a4 b4^2 |Cot z| (Sin z^2)^(1/4))"]];
(* Heisenberg equation reproduces the field equation *)
Module[{Phi = rftField["C"], Phic = rftFieldC["C"], Hd, flow, d4sol, ok, S},
  S = Phic . Cm . Phi;
  Hd = sg (Phic . (m Cm) . Phi - Sum[If[a == 5, 0, Phic . Cm . gup[[a]] . (D[Phi, X[[a]]] + Om[[a]] . Phi)], {a, 8}] + U[S]);
  flow = Table[-I Sum[Bm[[A, Cc]] rftVarDerExpr[Hd, phc[Cc]]/sg, {Cc, 16}], {A, 16}];
  d4sol = -g[[5]] . ((m + U'[S]) Phi - Sum[If[a == 5, 0, gup[[a]] . (D[Phi, X[[a]]] + Om[[a]] . Phi)], {a, 8}]);
  ok = rftZeroQ[flow - d4sol] && rftZeroQ[Simplify[rftLagUnsym["C", rftGeo0, Phi, Phic] - (Phic . (sg Cm . g[[5]]) . D[Phi, x4] - Hd)]] &&
    rftZeroQ[g[[5]] . Sum[If[a == 5, 0, gup[[a]] . Om[[a]]], {a, 8}] - (cg g[[5]] . g[[1]] - vg id16)];
  addCheck["Heisenberg_equation_reproduces_field_equation", ok,
    "with the Hamiltonian density Hd = sqrt g [Psi^dagger (m C - sum_(a != x4) C gamma^a D_a) Psi + U(S)] (so that the unsymmetrised L = Psi^dagger K d4 Psi - Hd exactly) and {Psi, Psi^dagger} = B delta^7/sqrt g, " <>
    "the Heisenberg equation d4 Psi = i[H, Psi] = -i B (1/sqrt g) dHd/dPsi^dagger equals -gamma^(x4) [(m + U'(S)) Psi - sum_(a != x4) gamma^a D_a Psi], the field equation solved for d4 Psi (exact, general U; " <>
    "the operator ordering of U'(S) Psi is that of the classical expression); the spin connection of the seven slice directions contributes " <>
    "gamma^(x4) sum_(a != x4) gamma^a Omega_a = (3/2) H E^a4 b4^(-1/2) gamma^(x4) gamma^(x0) - (b4'/b4 - a4'/2) (Omega_x4 = 0), " <>
    "i.e. the term -(b4'/b4 - a4'/2) Psi of the evolution form comes from the spin connection of the hidden block and of 3-space"]];
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
(* curved good sector: weighted Hermiticity, the role of the spin-connection term cg gamma^(x0) and of the term vg;
   Wolfram positions x0 = 1, x4 = 5.  h is the operator of i d4 Psi = h Psi (U = 0) read off the evolution form,
   including the term -i vg = -i (b4'/b4 - a4'/2). *)
Module[{u = Table[ph[A] @@ X, {A, 16}], uc = Table[phc[A] @@ X, {A, 16}], v = Table[qv[A] @@ X, {A, 16}], hOp, hOpC, Mm, lhs, divs, rest, lhsNoH, lhsB, divsB, dsg},
  Mm[a_] := I g[[5]] . g[[a]];
  hOp[w_, withH_] := mm (-I g[[5]]) . w + Sum[If[a == 5, 0, (1/f[[a]]) Mm[a] . D[w, X[[a]]]], {a, 8}] + withH cg Mm[1] . w - I vg w;
  hOpC[w_, withH_] := mm (I g[[5]]) . w + Sum[If[a == 5, 0, (1/f[[a]]) Conjugate[Mm[a]] . D[w, X[[a]]]], {a, 8}] + withH cg Conjugate[Mm[1]] . w + I vg w;
  dsg = D[sg, x4];
  lhs = sg (uc . hOp[v, 1] - hOpC[uc, 1] . v);
  divs = Sum[D[sg/f[[a]] uc . Mm[a] . v, X[[a]]], {a, {1, 2, 3, 4}}];
  rest = Sum[sg/f[[a]] (uc . Mm[a] . D[v, X[[a]]] - D[uc, X[[a]]] . Mm[a] . v), {a, {6, 7, 8}}];
  lhsNoH = sg (uc . hOp[v, 0] - hOpC[uc, 0] . v);
  addCheck["good_sector_hermiticity_curved",
    rftZeroQ[lhs - divs - rest + I dsg uc . v] && rftZeroQ[lhsNoH - divs - rest + I dsg uc . v + 2 cg sg uc . Mm[1] . v] && rftZeroQ[dsg - 2 vg sg] &&
    rftZeroQ[(Sin[rftZ]^2)^(1/4) (pf[x0] (D[qf[x0], x0] + (3/2) H Cot[rftZ] qf[x0]) + (D[pf[x0], x0] + (3/2) H Cot[rftZ] pf[x0]) qf[x0]) - D[(Sin[rftZ]^2)^(1/4) pf[x0] qf[x0], x0]] &&
    rftZeroQ[sg/f[[1]] - rftSig b4[x4]^(3/2) (Sin[rftZ]^2)^(1/4)],
    "the curved mode operator h = m (-i gamma^(x4)) + sum_(a != x4) (1/f_a) i gamma^(x4) gamma^(a) d_a + i cg gamma^(x4) gamma^(x0) - i vg, cg = (3/2) H E^a4 b4^(-1/2), vg = b4'/b4 - a4'/2 " <>
    "(i d4 Psi = h Psi for U = 0; the last term is anti-Hermitian) satisfies, for general u, v and every real z, " <>
    "sqrt g (u^dagger h v - (h u)^dagger v) = sum_(a = x0,x1,x2,x3) d_a (sqrt g/f_a u^dagger M_a v) + sum_(t = x5,x6,x7) (sqrt g/f_t)(u^dagger M_t d_t v - d_t u^dagger M_t v) - i (d_x4 sqrt g) u^dagger v, M_a = i gamma^(x4) gamma^(a), " <>
    "d_x4 sqrt g = 2 vg sqrt g: the anti-Hermitian term exactly compensates the x4 dependence of the measure, so in the GOOD SECTOR (no extra-time dependence) d/dx4 integral sqrt g u^dagger v d^7x = boundary terms for solutions u, v. " <>
    "The x0 term carries sqrt g/f0 = sig b4^(3/2) (Sin z^2)^(1/4): its boundary term vanishes where Sin z = 0 and not where Cos z = 0, so Hermiticity needs a boundary condition at the degenerate points z = Pi/2 + n Pi (see Revision/theory/reports/wolfram-scope.json); " <>
    "without the spin-connection term cg gamma^(x0) a remainder -2 cg sqrt g u^dagger M_0 v survives ((Sin z^2)^(1/4) [p (d0 + (3/2) H Cot z) q + ((d0 + (3/2) H Cot z) p) q] = d0 ((Sin z^2)^(1/4) p q)): " <>
    "for this measure and the variables Psi the gravitational term is what makes the hidden-direction operator formally antisymmetric"];
  lhsB = sg (uc . Bm . hOp[v, 1] - hOpC[uc, 1] . Bm . v);
  divsB = Sum[If[a == 5, 0, D[sg/f[[a]] uc . Bm . Mm[a] . v, X[[a]]]], {a, 8}];
  addCheck["Krein_form_conserved_curved",
    rftZeroQ[lhsB - divsB + I dsg uc . Bm . v],
    "sqrt g (u^dagger B h v - (h u)^dagger B v) = sum_(a != 4) d_a (sqrt g/f_a u^dagger B M_a v) - i (d_x4 sqrt g) u^dagger B v for general u, v (all seven slice directions; every real z): " <>
    "for solutions d/dx4 integral sqrt g u^dagger B v d^7x = boundary terms, i.e. the Krein form integral sqrt g u^dagger B v d^7x is conserved in the whole theory up to these boundary terms (they need boundary conditions, in particular at the degenerate points z = n Pi/2)"]];
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
  "canonical quantisation of dirac16complex (SPEC section 6), x4 the evolution time, sqrt g = E^-a4 b4^2 |Cot[z]| (Sin[z]^2)^(1/4)",
  "pi_A = (i/2) sqrt g (Psi^dagger B)_A; K = sqrt g C gamma^(x4) = i sqrt g B; {Psi_A(x), Psi^dagger_C(y)}_(x4 = y4) = B_AC delta^7(x - y)/sqrt g; B = -i C gamma^(x4), B^dagger = B, B^2 = 1, signature (8,8); " <>
  "no positive inner product with Psi^dagger the adjoint (Krein space, fundamental symmetry B); positive representation chi = Psi^dagger B, {Psi_A, chi_C} = delta_AC; " <>
  "Heisenberg: d4 Psi = -i B (1/sqrt g) dHd/dPsi^dagger = -gamma^(x4) [(m + U') Psi - sum_(a != x4) gamma^a D_a Psi]; mode operator h = m (-i g[x4]) + sum_(a != x4) (1/f_a) i g[x4].g[xa] d_a + (3/2) i H E^a4 b4^(-1/2) g[x4].g[x0] - i (b4'/b4 - a4'/2); " <>
  "good sector (no x5, x6, x7 dependence): integral sqrt g u^dagger v d^7x conserved up to boundary terms (the anti-Hermitian term compensates d_x4 sqrt g = (2 b4'/b4 - a4') sqrt g), positive Fock space, " <>
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
