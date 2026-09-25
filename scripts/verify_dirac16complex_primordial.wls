#!/usr/bin/env wolframscript
(* verify_dirac16complex_primordial.wls

   Stage 2 exact verifier: dirac16complex in the notebook's primordial field.
   Usage (from the repository root):
     wolframscript -file scripts/verify_dirac16complex_primordial.wls artifacts/dirac16complex/primordial-field/wolfram-primordial-report.json
   Pass the report path positionally, NOT after "--": with WolframScript 1.14.0,
   "-file s.wls -- r.json" gives $ScriptCommandLine = {"s.wls"} (the "--" and
   everything after it are dropped), so the path would silently fall back to the
   default.  A "--" that does arrive is filtered out below, so both forms read
   the same path when it is passed through.
   Writes the report and, next to it, primordial-components.json (read by
   scripts/check_dirac16complex_primordial.py for P_EL_agreesWithWolfram).
   Prints check_<name>=true|false, measurement_<name>=..., check_count, failed_check_count;
   exits nonzero if any check fails. *)

scriptDir = DirectoryName[ExpandFileName[$InputFileName]];
repoRoot = ParentDirectory[scriptDir];
args = DeleteCases[Rest[$ScriptCommandLine], "--"];
reportRel = If[Length[args] >= 1, First[args], "artifacts/dirac16complex/primordial-field/wolfram-primordial-report.json"];
reportPath = If[StringStartsQ[reportRel, "/"] || StringMatchQ[reportRel, RegularExpression["^[A-Za-z]:.*"]], reportRel,
   FileNameJoin[{repoRoot, reportRel}]];
componentsPath = FileNameJoin[{DirectoryName[reportPath], "primordial-components.json"}];
If[! DirectoryQ[DirectoryName[reportPath]], CreateDirectory[DirectoryName[reportPath], CreateIntermediateDirectories -> True]];

modulePath = FileNameJoin[{repoRoot, "wolfram", "Dirac16ComplexPrimordial.wl"}];
Get[modulePath];

t0 = AbsoluteTime[];
result = Dirac16ComplexPrimordial`D16PRun[repoRoot];
elapsed = Round[AbsoluteTime[] - t0];

relFiles = {"wolfram/Dirac16ComplexPrimordial.wl", "scripts/verify_dirac16complex_primordial.wls",
   "artifacts/dirac16complex/arbitrary-field/algebra-fixture.json",
   "Pair_Creation_of_Universes_WaveFunctionOfUniverse-4+4-Einstein-Lovelock-Nash.nb"};
sha = Association[Table[f -> ToLowerCase[FileHash[FileNameJoin[Prepend[FileNameSplit[f], repoRoot]], "SHA256", All, "HexString"]], {f, relFiles}]];

jsonValue[x_Association] := Association[KeyValueMap[#1 -> jsonValue[#2] &, x]];
jsonValue[x_List] := jsonValue /@ x;
jsonValue[x_String] := x;
jsonValue[True] := True; jsonValue[False] := False;
jsonValue[x_Integer] := x;
jsonValue[x_Rational] := ToString[Numerator[x]] <> "/" <> ToString[Denominator[x]];
jsonValue[x_] := ToString[x, InputForm, PageWidth -> Infinity];

writeJSON[path_, data_] := Module[{str, bytes},
  str = ExportString[jsonValue[data], "RawJSON", "Compact" -> False];
  str = StringReplace[str, "\r\n" -> "\n"];
  If[! StringEndsQ[str, "\n"], str = str <> "\n"];
  bytes = ToCharacterCode[str, "UTF-8"];
  With[{s = OpenWrite[path, BinaryFormat -> True]}, BinaryWrite[s, bytes]; Close[s]];];

checks = result["checks"];
meas = result["measurements"];
report = <|"schemaVersion" -> 1,
   "producer" -> "scripts/verify_dirac16complex_primordial.wls (wolfram/Dirac16ComplexPrimordial.wl)",
   "checks" -> checks,
   "measurements" -> meas,
   "sourceSha256" -> sha|>;
components = Join[<|"schemaVersion" -> 1,
    "producer" -> "scripts/verify_dirac16complex_primordial.wls (wolfram/Dirac16ComplexPrimordial.wl)",
    "notation" -> <|"coordinates" -> "x0..x7 (zero-based); z = 6 H x0 in (0, pi/2); t = H x4; s = sin z; a_4 = a_4(t); a_4' = da_4/dt",
      "frame" -> "eta = diag(+1,+1,+1,+1,-1,-1,-1,-1); gamma^a = [[0, taubar_a],[tau_a, 0]]; C = sigma16 = gamma^0 gamma^1 gamma^2 gamma^3; Psibar = Psi^dagger C",
      "spinor" -> "Psi_0..Psi_15 (notebook f16[k] = Z[k]); upper 8 chirality -1, lower 8 chirality +1",
      "texSymbols" -> "s = \\sin z; m = mass parameter of CONTRACT section 5 (notebook: m = -H M); S = \\bar\\Psi\\Psi; U = (\\lambda/2) S^2",
      "pyStrings" -> "sympy-parsable: z, H, a4, a4p (= a4'), a4pp, a4ppp, m, lam, S, K, M, Q1, kappa, Meff"|>,
    "field" -> <|"metric" -> "g=\\mathrm{diag}\\bigl(\\cot^2z,\\ s^{1/3}e^{2a_4}(\\times3),\\ -1,\\ -s^{1/3}e^{-2a_4}(\\times3)\\bigr)",
      "vielbein" -> "e_\\mu{}^a=\\mathrm{diag}(h_\\mu),\\ h=\\bigl(\\cot z,\\ s^{1/6}e^{a_4}(\\times3),\\ 1,\\ s^{1/6}e^{-a_4}(\\times3)\\bigr)",
      "detG" -> "\\det g=+\\cos^2 z,\\quad \\sqrt{|g|}=\\cos z", "signature" -> "(4,4)"|>|>,
   result["components"]];
writeJSON[reportPath, report];
writeJSON[componentsPath, components];

Scan[Print["check_", #, "=", If[TrueQ[checks[#]], "true", "false"]] &, Keys[checks]];
Scan[Print["measurement_", #, "=", jsonValue[meas[#]] /. {l_List :> ExportString[l, "RawJSON", "Compact" -> True]}] &, Keys[meas]];
failed = Count[Values[checks], False];
Print["check_count=", Length[checks]];
Print["failed_check_count=", failed];
Print["elapsed_seconds=", elapsed];
Print["report=", reportPath];
Print["components=", componentsPath];
Exit[If[failed == 0 && Length[checks] > 0, 0, 1]];
