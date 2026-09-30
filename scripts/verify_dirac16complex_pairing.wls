#!/usr/bin/env wolframscript
(* verify_dirac16complex_pairing.wls

   Stage 5 exact verifier: the {+M, -M} pairing theorems T1, T2, T3 of STAGE5_SPEC
   section 5 and the statistics sign of section 4, for dirac16complex (anticommuting)
   and dirac16complex00 (commuting) (wolfram/Dirac16ComplexPairing.wl).
   Usage (from the repository root):
     wolframscript -file scripts/verify_dirac16complex_pairing.wls artifacts/dirac16complex/pair-creation/wolfram-pairing-report.json
   Pass the report path positionally, NOT after "--": WolframScript 1.14 drops
   "--" and everything after it from $ScriptCommandLine.  A "--" that does
   arrive is filtered out below.
   Writes the report and, next to it, pairing-theory.json (every map and formula,
   exact; read by the Stage-5 checkers, solvers and documents).
   Prints check_<name>=true|false, measurement_<name>=..., check_count,
   failed_check_count; exits nonzero if any check fails.  The JSON files contain no
   timing and are byte-deterministic (LF, trailing newline). *)

scriptDir = DirectoryName[ExpandFileName[$InputFileName]];
repoRoot = ParentDirectory[scriptDir];
args = DeleteCases[Rest[$ScriptCommandLine], "--"];
reportRel = If[Length[args] >= 1, First[args], "artifacts/dirac16complex/pair-creation/wolfram-pairing-report.json"];
reportPath = If[StringStartsQ[reportRel, "/"] || StringMatchQ[reportRel, RegularExpression["^[A-Za-z]:.*"]], reportRel,
   FileNameJoin[{repoRoot, reportRel}]];
theoryPath = FileNameJoin[{DirectoryName[reportPath], "pairing-theory.json"}];
If[! DirectoryQ[DirectoryName[reportPath]], CreateDirectory[DirectoryName[reportPath], CreateIntermediateDirectories -> True]];

modulePath = FileNameJoin[{repoRoot, "wolfram", "Dirac16ComplexPairing.wl"}];
loadResult = Get[modulePath];
If[loadResult === $Failed, Print["FATAL: module failed to load: ", modulePath]; Print["check_count=0"]; Print["failed_check_count=1"]; Exit[1]];

t0 = AbsoluteTime[];
result = Dirac16ComplexPairing`D16PairRun[repoRoot];
elapsed = Round[AbsoluteTime[] - t0];
If[! AssociationQ[result] || ! AssociationQ[result["checks"]] || ! AssociationQ[result["measurements"]] || ! AssociationQ[result["theory"]],
  Print["FATAL: D16PairRun did not return an Association with checks/measurements/theory"]; Print["check_count=0"]; Print["failed_check_count=1"]; Exit[1]];

relFiles = {"wolfram/Dirac16ComplexPairing.wl", "scripts/verify_dirac16complex_pairing.wls",
   "wolfram/Dirac16ComplexGeometry.wl",
   "artifacts/dirac16complex/arbitrary-field/algebra-fixture.json",
   "artifacts/dirac16complex/kohn-sham/kohn-sham-theory.json"};
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
producer = "scripts/verify_dirac16complex_pairing.wls (wolfram/Dirac16ComplexPairing.wl)";
report = <|"schemaVersion" -> 1, "producer" -> producer, "checks" -> checks, "measurements" -> meas, "sourceSha256" -> sha|>;
theory = Join[<|"schemaVersion" -> 1, "producer" -> producer,
    "description" -> "Exact Stage-5 pairing theory of dirac16complex (anticommuting) and dirac16complex00 (commuting): the chirality map T1 (field level, arbitrary gravitational field, Krein metric), the mirror map T2 (Pin(4,4) reflections of character -1, Z2 coordinate action), the Kohn-Sham level T3 (exact 2x2 block maps, boundary conditions, densities, potentials, functional, EMT, untransformed-BC control), the statistics sign of the exchange energy, the pair totals and the prescription for the numerics. Complex entries are [re, im] pairs of exact rational strings.",
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
