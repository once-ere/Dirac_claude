#!/usr/bin/env wolframscript
(* verify_dirac16complex00.wls

   Stage 5 exact verifier: the classical theory of dirac16complex00 (16 COMMUTING complex
   components forming a Pin(4,4) spinor) side by side with the Grassmann field
   dirac16complex (wolfram/Dirac16Complex00.wl, STAGE5_SPEC sections 1-3).
   Usage (from the repository root):
     wolframscript -file scripts/verify_dirac16complex00.wls artifacts/dirac16complex/pair-creation/wolfram-dirac16complex00-report.json
   Pass the report path positionally, NOT after "--": WolframScript 1.14 drops "--" and
   everything after it from $ScriptCommandLine.  A "--" that does arrive is filtered out.
   Writes the report and, next to it, dirac16complex00-theory.json (formulas and exact data
   for the downstream Stage-5 agents; exact rationals as strings, complex entries as
   [re, im] pairs of rational strings).
   Prints check_<name>=true|false, measurement_<name>=..., check_count, failed_check_count;
   exits nonzero if any check fails or the number of checks is not the expected one.

   License: GPL-3.0-or-later. *)

scriptDir = DirectoryName[ExpandFileName[$InputFileName]];
repoRoot = ParentDirectory[scriptDir];
args = DeleteCases[Rest[$ScriptCommandLine], "--"];
reportRel = If[Length[args] >= 1, First[args], "artifacts/dirac16complex/pair-creation/wolfram-dirac16complex00-report.json"];
reportPath = If[StringStartsQ[reportRel, "/"] || StringMatchQ[reportRel, RegularExpression["^[A-Za-z]:.*"]], reportRel,
   FileNameJoin[{repoRoot, reportRel}]];
theoryPath = FileNameJoin[{DirectoryName[reportPath], "dirac16complex00-theory.json"}];
If[! DirectoryQ[DirectoryName[reportPath]], CreateDirectory[DirectoryName[reportPath], CreateIntermediateDirectories -> True]];

expectedCheckCount = 45;

modulePath = FileNameJoin[{repoRoot, "wolfram", "Dirac16Complex00.wl"}];
loadResult = Check[Get[modulePath], $Failed];
If[loadResult === $Failed, Print["FATAL: module failed to load (or produced messages): ", modulePath]; Print["check_count=0"]; Print["failed_check_count=1"]; Exit[2]];

t0 = AbsoluteTime[];
result = Dirac16Complex00`D16C00Run[repoRoot];
elapsed = Round[AbsoluteTime[] - t0];
If[! AssociationQ[result] || ! AssociationQ[result["checks"]] || ! AssociationQ[result["measurements"]] || ! AssociationQ[result["theory"]],
  Print["FATAL: D16C00Run did not return an Association with checks/measurements/theory"]; Print["check_count=0"]; Print["failed_check_count=1"]; Exit[2]];

relFiles = {"wolfram/Dirac16Complex00.wl", "scripts/verify_dirac16complex00.wls",
   "wolfram/Dirac16ComplexGeometry.wl", "wolfram/Dirac16ComplexPrimordial.wl", "wolfram/Dirac16ComplexKohnSham.wl",
   "artifacts/dirac16complex/arbitrary-field/algebra-fixture.json", "artifacts/dirac16complex/kohn-sham/kohn-sham-theory.json",
   "artifacts/dirac16complex/arbitrary-field/wolfram-geometry-report.json", "artifacts/dirac16complex/arbitrary-field/wolfram-algebra-report.json",
   "artifacts/dirac16complex/primordial-field/wolfram-primordial-report.json", "artifacts/dirac16complex/kohn-sham/wolfram-kohn-sham-report.json"};
sha = Association[Table[f -> ToLowerCase[FileHash[FileNameJoin[Prepend[FileNameSplit[f], repoRoot]], "SHA256", All, "HexString"]], {f, relFiles}]];

cleanContexts[s_String] := StringReplace[s, {"Dirac16Complex00`Private`" -> "", "Dirac16ComplexKohnSham`Private`" -> "", "Dirac16ComplexPrimordial`Private`" -> "",
    "Dirac16Complex`Geometry`Private`" -> "", "Global`" -> ""}];
ratS[x_Integer] := ToString[x];
ratS[x_Rational] := ToString[Numerator[x]] <> "/" <> ToString[Denominator[x]];
jsonValue[x_Association] := Association[KeyValueMap[(If[StringQ[#1], #1, cleanContexts[ToString[#1, InputForm]]]) -> jsonValue[#2] &, x]];
jsonValue[x_List] := jsonValue /@ x;
jsonValue[x_String] := cleanContexts[x];
jsonValue[True] := True; jsonValue[False] := False;
jsonValue[x_Integer] := x;
jsonValue[x_Rational] := ratS[x];
jsonValue[Complex[a_, b_]] /; (IntegerQ[a] || Head[a] === Rational) && (IntegerQ[b] || Head[b] === Rational) := {ratS[a], ratS[b]};
jsonValue[x_Missing] := "missing";
jsonValue[x_] := cleanContexts[ToString[x, InputForm, PageWidth -> Infinity]];

writeJSON[path_, data_] := Module[{str, bytes},
  str = ExportString[jsonValue[data], "RawJSON", "Compact" -> False];
  If[! StringQ[str], Print["FATAL: JSON export failed for ", path]; Exit[2]];
  str = StringReplace[str, {"\r\n" -> "\n", "\\/" -> "/"}];
  If[! StringEndsQ[str, "\n"], str = str <> "\n"];
  bytes = ToCharacterCode[str, "UTF-8"];
  With[{s = OpenWrite[path, BinaryFormat -> True]}, BinaryWrite[s, bytes]; Close[s]];];

(* the expected number of module checks guards against a silently skipped check; it is itself a check of the report *)
checks = KeySort[Append[result["checks"], "C00_verifier_expectedCheckCount" -> (Length[result["checks"]] === expectedCheckCount)]];
meas = KeySort[result["measurements"]];
producer = "scripts/verify_dirac16complex00.wls (wolfram/Dirac16Complex00.wl), Wolfram Language " <> First[StringSplit[$Version]];
report = <|"schemaVersion" -> 1, "producer" -> producer, "checks" -> checks, "measurements" -> meas, "sourceSha256" -> sha|>;
theory = Join[<|"schemaVersion" -> 1, "producer" -> producer,
    "description" -> "Exact Stage-5 theory of dirac16complex00 (commuting components) side by side with dirac16complex (Grassmann components): the Lagrangian (L1) with the explicit mass term, the real restriction, the coupling to the spin connection and gravity, the field equations, the energy-momentum tensor from the vielbein variation, current, energy splits and equations of state in an arbitrary field, the indefinite charge and unbounded energy of the commuting field, the primordial field (Stage-2 chart) and the static warped form with the Stage-4 2x2 blocks.",
    "sourceSha256" -> sha|>, result["theory"]];
writeJSON[reportPath, report];
writeJSON[theoryPath, theory];

Scan[Print["check_", #, "=", If[TrueQ[checks[#]], "true", "false"]] &, Keys[checks]];
Scan[Print["measurement_", #, "=", With[{v = jsonValue[meas[#]]}, If[StringQ[v], v, ExportString[v, "RawJSON", "Compact" -> True]]]] &, Keys[meas]];
failed = Count[Values[checks], False];
Print["module_check_count=", Length[result["checks"]], " (expected ", expectedCheckCount, ")"];
Print["check_count=", Length[checks]];
Print["failed_check_count=", failed];
Print["elapsed_seconds=", elapsed];
Print["report=", reportPath];
Print["theory=", theoryPath];
Exit[If[failed == 0 && Length[checks] > 0, 0, 1]];
