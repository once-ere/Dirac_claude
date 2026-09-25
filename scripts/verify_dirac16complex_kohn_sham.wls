#!/usr/bin/env wolframscript
(* verify_dirac16complex_kohn_sham.wls

   Stage 4 exact verifier: the Kohn-Sham theory of dirac16complex in the static
   primordial gravitational field (wolfram/Dirac16ComplexKohnSham.wl).
   Usage (from the repository root):
     wolframscript -file scripts/verify_dirac16complex_kohn_sham.wls artifacts/dirac16complex/kohn-sham/wolfram-kohn-sham-report.json
   Pass the report path positionally, NOT after "--": WolframScript 1.14 drops
   "--" and everything after it from $ScriptCommandLine.  A "--" that does
   arrive is filtered out below.
   Writes the report and, next to it, kohn-sham-theory.json (every explicit
   matrix as exact Gaussian rationals, read by the Rust and Python solvers).
   Prints check_<name>=true|false, measurement_<name>=..., check_count,
   failed_check_count; exits nonzero if any check fails. *)

scriptDir = DirectoryName[ExpandFileName[$InputFileName]];
repoRoot = ParentDirectory[scriptDir];
args = DeleteCases[Rest[$ScriptCommandLine], "--"];
reportRel = If[Length[args] >= 1, First[args], "artifacts/dirac16complex/kohn-sham/wolfram-kohn-sham-report.json"];
reportPath = If[StringStartsQ[reportRel, "/"] || StringMatchQ[reportRel, RegularExpression["^[A-Za-z]:.*"]], reportRel,
   FileNameJoin[{repoRoot, reportRel}]];
theoryPath = FileNameJoin[{DirectoryName[reportPath], "kohn-sham-theory.json"}];
If[! DirectoryQ[DirectoryName[reportPath]], CreateDirectory[DirectoryName[reportPath], CreateIntermediateDirectories -> True]];

modulePath = FileNameJoin[{repoRoot, "wolfram", "Dirac16ComplexKohnSham.wl"}];
loadResult = Get[modulePath];
If[loadResult === $Failed, Print["FATAL: module failed to load: ", modulePath]; Print["check_count=0"]; Print["failed_check_count=1"]; Exit[1]];

t0 = AbsoluteTime[];
result = Dirac16ComplexKohnSham`D16KSRun[repoRoot];
elapsed = Round[AbsoluteTime[] - t0];
If[! AssociationQ[result] || ! AssociationQ[result["checks"]] || ! AssociationQ[result["measurements"]] || ! AssociationQ[result["theory"]],
  Print["FATAL: D16KSRun did not return an Association with checks/measurements/theory"]; Print["check_count=0"]; Print["failed_check_count=1"]; Exit[1]];

relFiles = {"wolfram/Dirac16ComplexKohnSham.wl", "scripts/verify_dirac16complex_kohn_sham.wls",
   "artifacts/dirac16complex/arbitrary-field/algebra-fixture.json"};
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
producer = "scripts/verify_dirac16complex_kohn_sham.wls (wolfram/Dirac16ComplexKohnSham.wl)";
report = <|"schemaVersion" -> 1, "producer" -> producer, "checks" -> checks, "measurements" -> meas, "sourceSha256" -> sha|>;
theory = Join[<|"schemaVersion" -> 1, "producer" -> producer,
    "description" -> "Exact Stage-4 Kohn-Sham theory data for dirac16complex in the static primordial field: geometry, reduction to eight 2x2 blocks (explicit basis and matrices), boundary conditions, exchange, functional, energy-momentum reduction. All numbers are exact rational strings; complex entries are [re, im] pairs.",
    "sourceSha256" -> sha|>, result["theory"]];
writeJSON[reportPath, report];
writeJSON[theoryPath, theory];

Scan[Print["check_", #, "=", If[TrueQ[checks[#]], "true", "false"]] &, Keys[checks]];
Scan[Print["measurement_", #, "=", jsonValue[meas[#]] /. {l_List :> ExportString[l, "RawJSON", "Compact" -> True]}] &, Keys[meas]];
failed = Count[Values[checks], False];
Print["check_count=", Length[checks]];
Print["failed_check_count=", failed];
Print["elapsed_seconds=", elapsed];
Print["report=", reportPath];
Print["theory=", theoryPath];
Exit[If[failed == 0 && Length[checks] > 0, 0, 1]];
