#!/usr/bin/env wolframscript
(* ::Package:: *)

(* verify_dirac16complex_algebra.wls

   Exact verifier for the dirac16complex algebra (Stage 1, arbitrary field).
   Loads wolfram/Dirac16ComplexAlgebra.wl (context Dirac16Complex`Algebra`), runs every
   check, compares with the independent Python fixture when it exists, writes the JSON
   report and prints

     check_<name>=true|false          (one line per check)
     measurement_<name>=<value>       (one line per measurement, compact JSON)
     check_count=N
     failed_check_count=K

   and exits with status 1 if any check failed (2 on a load/IO error).

   Usage (from the repository root):
     wolframscript -file scripts/verify_dirac16complex_algebra.wls -- artifacts/dirac16complex/arbitrary-field/wolfram-algebra-report.json

   WolframScript 1.14 drops every argument that follows "--" when it is combined with
   -file, so the report path defaults to the canonical path above.  Positional arguments
   given without "--" (report path, then fixture path) or the environment variables
   DIRAC16_ALGEBRA_REPORT / DIRAC16_ALGEBRA_FIXTURE override the defaults.

   License: GPL-3.0-or-later. *)

scriptDirectory = DirectoryName[ExpandFileName[$InputFileName]];
repositoryRoot = ParentDirectory[scriptDirectory];
arguments = Select[Rest[$ScriptCommandLine], # =!= "--" &];

nonEmptyString[value_] := StringQ[value] && value =!= "";
defaultReportPath = FileNameJoin[{repositoryRoot, "artifacts", "dirac16complex", "arbitrary-field", "wolfram-algebra-report.json"}];
defaultFixturePath = FileNameJoin[{repositoryRoot, "artifacts", "dirac16complex", "arbitrary-field", "algebra-fixture.json"}];
reportPath = ExpandFileName[Which[
  Length[arguments] >= 1, arguments[[1]],
  nonEmptyString[Environment["DIRAC16_ALGEBRA_REPORT"]], Environment["DIRAC16_ALGEBRA_REPORT"],
  True, defaultReportPath
]];
fixturePath = ExpandFileName[Which[
  Length[arguments] >= 2, arguments[[2]],
  nonEmptyString[Environment["DIRAC16_ALGEBRA_FIXTURE"]], Environment["DIRAC16_ALGEBRA_FIXTURE"],
  True, defaultFixturePath
]];

packagePath = FileNameJoin[{repositoryRoot, "wolfram", "Dirac16ComplexAlgebra.wl"}];
If[!FileExistsQ[packagePath], Print["ERROR: missing package ", packagePath]; Exit[2]];
Check[Get[packagePath], Print["ERROR: package load produced messages: ", packagePath]; Exit[2]];

(* repository-relative path with forward slashes (used as sourceSha256 keys) *)
relativePath[path_String] := Module[{rootText = StringReplace[repositoryRoot, "\\" -> "/"], pathText = StringReplace[path, "\\" -> "/"]},
  If[StringStartsQ[pathText, rootText <> "/", IgnoreCase -> True], StringDrop[pathText, StringLength[rootText] + 1], pathText]
];
sha256[path_String] := ToLowerCase[FileHash[path, "SHA256", All, "HexString"]];

jsonString[expr_, compact_] := Module[{s},
  s = If[compact, ExportString[expr, "RawJSON", "Compact" -> True], ExportString[expr, "RawJSON"]];
  If[!StringQ[s], Print["ERROR: JSON export failed"]; Exit[2]];
  s = StringReplace[s, {"\r\n" -> "\n", "\\/" -> "/"}];
  s
];

writeUTF8[path_String, text_String] := Module[{stream},
  If[!DirectoryQ[DirectoryName[path]], CreateDirectory[DirectoryName[path], CreateIntermediateDirectories -> True]];
  stream = OpenWrite[path, BinaryFormat -> True];
  BinaryWrite[stream, ToCharacterCode[text, "UTF-8"]];
  Close[stream];
];

startTime = AbsoluteTime[];
result = Dirac16Complex`Algebra`D16AlgebraVerification[repositoryRoot];
checks = result["checks"];
measurements = result["measurements"];

sourceFiles = {
  packagePath,
  ExpandFileName[$InputFileName],
  FileNameJoin[{repositoryRoot, "dirac-main", "artifacts", "exact", "cl44-seed.json"}],
  FileNameJoin[{repositoryRoot, "dirac-main", "artifacts", "exact", "split-octonion.json"}],
  FileNameJoin[{repositoryRoot, "dirac-main", "artifacts", "exact", "triality44.json"}]
};

If[FileExistsQ[fixturePath],
  Module[{fixture, cmp},
    fixture = Quiet[Check[Import[fixturePath, "RawJSON"], $Failed]];
    If[fixture === $Failed,
      checks = Append[checks, "ALG_fixtureAgreement" -> False];
      measurements = Join[measurements, <|"fixtureAgreement" -> "run",
        "fixtureAgreement.path" -> relativePath[fixturePath],
        "fixtureAgreement.error" -> "fixture is not valid JSON"|>],
      cmp = Dirac16Complex`Algebra`D16CompareFixture[fixture];
      checks = Append[checks, "ALG_fixtureAgreement" -> TrueQ[cmp["agree"]]];
      measurements = Join[measurements, <|"fixtureAgreement" -> "run",
        "fixtureAgreement.path" -> relativePath[fixturePath],
        "fixtureAgreement.summary" -> KeyDrop[cmp, "details"],
        "fixtureAgreement.details" -> cmp["details"]|>]
    ];
    AppendTo[sourceFiles, fixturePath]
  ],
  measurements = Append[measurements, "fixtureAgreement" -> "not-run"]
];

(* dirac-main is a separately published, git-ignored reference tree: its fixtures are hashed and
   cross-checked only when present (the corresponding measurements then read "not-run") *)
measurements = Append[measurements, "referenceFilesPresent" ->
  Association[(relativePath[#] -> FileExistsQ[#]) & /@ Rest[Rest[sourceFiles]]]];
sourceHashes = Association[(relativePath[#] -> sha256[#]) & /@ Select[sourceFiles, FileExistsQ]];

report = <|
  "schemaVersion" -> 1,
  "producer" -> "scripts/verify_dirac16complex_algebra.wls with wolfram/Dirac16ComplexAlgebra.wl (context Dirac16Complex`Algebra`), Wolfram Language " <>
    First[StringSplit[$Version]],
  "checks" -> checks,
  "measurements" -> Dirac16Complex`Algebra`D16JSONValue[measurements],
  "sourceSha256" -> sourceHashes
|>;

reportText = jsonString[report, False];
If[!StringEndsQ[reportText, "\n"], reportText = reportText <> "\n"];
writeUTF8[reportPath, reportText];

Scan[Print["check_" <> #[[1]] <> "=" <> If[TrueQ[#[[2]]], "true", "false"]] &, Normal[checks]];
Scan[
  Function[rule, Module[{v = Dirac16Complex`Algebra`D16JSONValue[rule[[2]]]},
    Print["measurement_" <> rule[[1]] <> "=" <> If[StringQ[v], v, jsonString[v, True]]]]],
  Normal[report["measurements"]]
];
failed = Count[Values[checks], x_ /; !TrueQ[x]];
Print["report_path=" <> relativePath[reportPath]];
Print["elapsed_seconds=" <> ToString[Round[AbsoluteTime[] - startTime]]];
Print["check_count=" <> ToString[Length[checks]]];
Print["failed_check_count=" <> ToString[failed]];
Exit[If[failed > 0, 1, 0]];
