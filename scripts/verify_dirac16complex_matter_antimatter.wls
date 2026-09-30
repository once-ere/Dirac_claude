#!/usr/bin/env wolframscript
(* ::Package:: *)

(* verify_dirac16complex_matter_antimatter.wls

   Exact verifier of the matter-antimatter analysis of dirac16complex (MATTER_ANTIMATTER_SPEC,
   theorems M1-M4 and the implication of M5, both statistics).  Loads
   wolfram/Dirac16ComplexMatterAntimatter.wl (context Dirac16ComplexMatterAntimatter`, which loads
   the Stage-1 geometry package read-only), runs every check, writes

     the JSON report   (default artifacts/dirac16complex/matter-antimatter/wolfram-matter-antimatter-report.json)
     the exact theory  (matter-antimatter-theory.json in the same directory as the report)

   and prints

     check_<name>=true|false          (one line per check)
     measurement_<name>=<value>       (one line per measurement)
     check_count=N
     failed_check_count=K

   and exits with status 1 if any check failed or the number of checks is not the expected
   one (2 on a load/IO error or if the run produced messages).

   Usage (from the repository root; the report path is a plain positional argument):
     wolframscript -file scripts/verify_dirac16complex_matter_antimatter.wls artifacts/dirac16complex/matter-antimatter/wolfram-matter-antimatter-report.json

   Do NOT put "--" before the path: WolframScript 1.14 drops "--" and every argument after it
   when it is combined with -file.  An optional second positional argument overrides the
   theory path; the environment variable DIRAC16_MATTER_ANTIMATTER_REPORT overrides the default
   report path.

   HONESTY: the checks establish M1-M4 and the M5 implication exactly as stated in the report;
   they do NOT establish that the theory solves the matter-antimatter problem (it cannot, see
   the honestyRule in the theory file).

   The JSON text is produced by ExportString[..., "RawJSON"] with "\r\n" -> "\n" and the
   optional JSON escape "\/" -> "/", and written as UTF-8 bytes with a trailing newline.

   License: GPL-3.0-or-later. *)

scriptPath = ExpandFileName[$InputFileName];
scriptDirectory = DirectoryName[scriptPath];
repositoryRoot = ParentDirectory[scriptDirectory];
arguments = Select[Rest[$ScriptCommandLine], # =!= "--" &];
nonEmptyString[value_] := StringQ[value] && value =!= "";
defaultReportPath = FileNameJoin[{repositoryRoot, "artifacts", "dirac16complex", "matter-antimatter", "wolfram-matter-antimatter-report.json"}];
reportPath = ExpandFileName[Which[
  Length[arguments] >= 1, arguments[[1]],
  nonEmptyString[Environment["DIRAC16_MATTER_ANTIMATTER_REPORT"]], Environment["DIRAC16_MATTER_ANTIMATTER_REPORT"],
  True, defaultReportPath
]];
theoryPath = ExpandFileName[If[Length[arguments] >= 2, arguments[[2]], FileNameJoin[{DirectoryName[reportPath], "matter-antimatter-theory.json"}]]];

packagePath = FileNameJoin[{repositoryRoot, "wolfram", "Dirac16ComplexMatterAntimatter.wl"}];
geometryPath = FileNameJoin[{repositoryRoot, "wolfram", "Dirac16ComplexGeometry.wl"}];
fixturePath = FileNameJoin[{repositoryRoot, "artifacts", "dirac16complex", "arbitrary-field", "algebra-fixture.json"}];
If[! FileExistsQ[packagePath], Print["ERROR: missing package ", packagePath]; Exit[2]];
Check[Get[packagePath], Print["ERROR: package load produced messages: ", packagePath]; Exit[2]];

expectedCheckCount = Dirac16ComplexMatterAntimatter`D16MAExpectedCheckCount;

relativePath[path_String] := Module[{rootText = StringReplace[repositoryRoot, "\\" -> "/"], pathText = StringReplace[path, "\\" -> "/"]},
  If[StringStartsQ[pathText, rootText <> "/", IgnoreCase -> True], StringDrop[pathText, StringLength[rootText] + 1], pathText]
];
sha256[path_String] := ToLowerCase[FileHash[path, "SHA256", All, "HexString"]];
jsonString[expr_] := Module[{s = ExportString[expr, "RawJSON"]},
  If[! StringQ[s], Print["ERROR: JSON export failed"]; Exit[2]];
  StringReplace[s, {"\r\n" -> "\n", "\\/" -> "/"}]
];
writeUTF8[path_String, text_String] := Module[{stream},
  If[! DirectoryQ[DirectoryName[path]], CreateDirectory[DirectoryName[path], CreateIntermediateDirectories -> True]];
  stream = OpenWrite[path, BinaryFormat -> True];
  BinaryWrite[stream, ToCharacterCode[text, "UTF-8"]];
  Close[stream];
];
valueText[v_] := Which[StringQ[v], v, v === True, "true", v === False, "false", True, ToString[v, InputForm, PageWidth -> Infinity]];

result = Check[Dirac16ComplexMatterAntimatter`D16MARun[repositoryRoot], $Failed];
If[result === $Failed || ! AssociationQ[result], Print["ERROR: D16MARun failed or produced messages"]; Exit[2]];
checks = result["checks"];
measurements = result["measurements"];

stage5Files = Select[{
    FileNameJoin[{repositoryRoot, "artifacts", "dirac16complex", "pair-creation", "wolfram-pairing-report.json"}],
    FileNameJoin[{repositoryRoot, "artifacts", "dirac16complex", "pair-creation", "pairing-theory.json"}]}, FileExistsQ];
sourceFiles = Join[{packagePath, scriptPath, geometryPath, fixturePath}, stage5Files];
sources = Association[(relativePath[#] -> sha256[#]) & /@ sourceFiles];
producer = "scripts/verify_dirac16complex_matter_antimatter.wls with wolfram/Dirac16ComplexMatterAntimatter.wl (context Dirac16ComplexMatterAntimatter`), Wolfram Language " <>
  First[StringSplit[$Version]];

report = <|
  "schemaVersion" -> 1,
  "producer" -> producer,
  "checks" -> checks,
  "measurements" -> measurements,
  "sourceSha256" -> sources
|>;
reportText = jsonString[report];
If[! StringEndsQ[reportText, "\n"], reportText = reportText <> "\n"];
writeUTF8[reportPath, reportText];

theory = Join[result["theory"], <|"sourceSha256" -> sources|>];
theoryText = jsonString[theory];
If[! StringEndsQ[theoryText, "\n"], theoryText = theoryText <> "\n"];
writeUTF8[theoryPath, theoryText];

failed = Keys[Select[checks, ! TrueQ[#] &]];
If[Length[checks] =!= expectedCheckCount, AppendTo[failed, "expectedCheckCount"]];
Scan[Print["check_" <> #[[1]] <> "=" <> If[TrueQ[#[[2]]], "true", "false"]] &, Normal[checks]];
Scan[Print["measurement_" <> #[[1]] <> "=" <> valueText[#[[2]]]] &, Normal[measurements]];
Print["check_count=", Length[checks]];
Print["failed_check_count=", Length[DeleteDuplicates[failed]]];
Print["report=", relativePath[reportPath]];
Print["theory=", relativePath[theoryPath]];
If[failed =!= {}, Print["failed_checks=", StringRiffle[DeleteDuplicates[failed], ","]]; Exit[1]];
Exit[0];
