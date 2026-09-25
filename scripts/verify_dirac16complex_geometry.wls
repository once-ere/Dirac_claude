#!/usr/bin/env wolframscript
(* ::Package:: *)

(* verify_dirac16complex_geometry.wls

   Exact verifier for the curved-space geometry, Lagrangian, energy-momentum tensor and
   canonical structure of dirac16complex (Stage 1, arbitrary gravitational field).
   Loads wolfram/Dirac16ComplexGeometry.wl (context Dirac16Complex`Geometry`), runs every
   check on the test geometries G1 (general non-diagonal vielbein), G2 (primordial field
   with arbitrary a4) and G3 (homogeneous Bianchi-I minisuperspace), writes the JSON report
   and prints

     check_<name>=true|false          (one line per check)
     measurement_<name>=<value>       (one line per measurement)
     check_count=N
     failed_check_count=K

   and exits with status 1 if any check failed or the number of checks is not the
   expected one (2 on a load/IO error).

   Usage (from the repository root; the report path is a plain positional argument):
     wolframscript -file scripts/verify_dirac16complex_geometry.wls artifacts/dirac16complex/arbitrary-field/wolfram-geometry-report.json

   Do NOT put "--" before the path: WolframScript 1.14 drops "--" and every argument
   after it when it is combined with -file ($ScriptCommandLine is then {script} only),
   and the report would silently go to the default path above.  A positional argument
   or the environment variable DIRAC16_GEOMETRY_REPORT overrides the default.

   The JSON text is produced by ExportString[..., "RawJSON"] with "\r\n" -> "\n" and the
   optional JSON escape "\/" -> "/", and written as UTF-8 bytes with a trailing newline.

   License: GPL-3.0-or-later. *)

scriptPath = ExpandFileName[$InputFileName];
scriptDirectory = DirectoryName[scriptPath];
repositoryRoot = ParentDirectory[scriptDirectory];
arguments = Select[Rest[$ScriptCommandLine], # =!= "--" &];
nonEmptyString[value_] := StringQ[value] && value =!= "";
defaultReportPath = FileNameJoin[{repositoryRoot, "artifacts", "dirac16complex", "arbitrary-field", "wolfram-geometry-report.json"}];
reportPath = ExpandFileName[Which[
  Length[arguments] >= 1, arguments[[1]],
  nonEmptyString[Environment["DIRAC16_GEOMETRY_REPORT"]], Environment["DIRAC16_GEOMETRY_REPORT"],
  True, defaultReportPath
]];

packagePath = FileNameJoin[{repositoryRoot, "wolfram", "Dirac16ComplexGeometry.wl"}];
If[! FileExistsQ[packagePath], Print["ERROR: missing package ", packagePath]; Exit[2]];
Check[Get[packagePath], Print["ERROR: package load produced messages: ", packagePath]; Exit[2]];

expectedCheckCount = 43;

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
valueText[v_] := Which[StringQ[v], v, v === True, "true", v === False, "false", True, ToString[v, InputForm]];

result = Check[Dirac16Complex`Geometry`D16GeoReport[], $Failed];
If[result === $Failed || ! AssociationQ[result], Print["ERROR: D16GeoReport failed or produced messages"]; Exit[2]];
checks = result["checks"];
measurements = result["measurements"];

sourceFiles = {packagePath, scriptPath};
report = <|
  "schemaVersion" -> 1,
  "producer" -> "scripts/verify_dirac16complex_geometry.wls with wolfram/Dirac16ComplexGeometry.wl (context Dirac16Complex`Geometry`), Wolfram Language " <>
    First[StringSplit[$Version]],
  "checks" -> checks,
  "measurements" -> measurements,
  "sourceSha256" -> Association[(relativePath[#] -> sha256[#]) & /@ sourceFiles]
|>;
reportText = jsonString[report];
If[! StringEndsQ[reportText, "\n"], reportText = reportText <> "\n"];
writeUTF8[reportPath, reportText];

failed = Keys[Select[checks, ! TrueQ[#] &]];
If[Length[checks] =!= expectedCheckCount, AppendTo[failed, "expectedCheckCount"]];
Scan[Print["check_" <> #[[1]] <> "=" <> If[TrueQ[#[[2]]], "true", "false"]] &, Normal[checks]];
Scan[Print["measurement_" <> #[[1]] <> "=" <> valueText[#[[2]]]] &, Normal[measurements]];
Print["check_count=", Length[checks]];
Print["failed_check_count=", Length[DeleteDuplicates[failed]]];
Print["report=", relativePath[reportPath]];
If[failed =!= {}, Print["failed_checks=", StringRiffle[DeleteDuplicates[failed], ","]]; Exit[1]];
Exit[0];
