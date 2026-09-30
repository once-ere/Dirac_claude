#!/usr/bin/env wolframscript
(* ::Package:: *)

(* verify_dirac16complex_ks_mathematica_notebook.wls

   Headless verifier of notebooks/Dirac16ComplexKohnSham.nb (pattern of the Stage-3
   verifier scripts/verify_dirac16complex_mathematica_notebook.wls).  It imports the
   notebook, evaluates every Input cell in order with $Dirac16RepositoryRoot set to the
   repository root, and fails (exit code 1) if any cell issues a message or returns
   $Failed, if the number of Input cells or of notebookChecks differs from the expected
   count, or if any entry of notebookChecks is not True.  Evaluating the notebook
   rewrites artifacts/dirac16complex/kohn-sham/mathematica-report.json and the PNG files
   under artifacts/dirac16complex/kohn-sham/figures/mathematica/ (deterministic: a
   repeated run on the same machine gives byte-identical files).

   Output contract (repository checkers): one line check_<name>=true|false per notebook
   check, one line measurement_<name>=<value> per entry of the report's "measurements",
   check_count=..., failed_check_count=..., and as the last line
   dirac16complex_ks_mathematica_notebook=OK or =FAILED.

   Usage:  wolframscript -file scripts/verify_dirac16complex_ks_mathematica_notebook.wls [notebook.nb] [--verbose]
           --verbose prints the wall time of every cell.
           (WolframScript 1.14 drops arguments after "--": pass the path positionally.)

   License: GPL-3.0-or-later (same as the repository). *)

ClearAll["Global`*"];

Module[
  {scriptDirectory, repositoryRoot, arguments, verbose, notebookPath, notebook, inputBoxes,
   expectedInputCount = 32, expectedCheckCount = 93, messages = {}, results, failedCells = {},
   checks, failedChecks, measurements, start = AbsoluteTime[], ok, fail},

  fail[text_String] := (Print["ERROR: ", text]; Print["dirac16complex_ks_mathematica_notebook=FAILED"]; Exit[2]);
  scriptDirectory = DirectoryName[ExpandFileName[$InputFileName]];
  repositoryRoot = ParentDirectory[scriptDirectory];
  arguments = Select[Rest[$ScriptCommandLine], # =!= "--" &];
  verbose = MemberQ[arguments, "--verbose"];
  arguments = DeleteCases[arguments, "--verbose"];
  notebookPath = ExpandFileName[
    If[Length[arguments] >= 1, First[arguments], FileNameJoin[{repositoryRoot, "notebooks", "Dirac16ComplexKohnSham.nb"}]]];

  If[! FileExistsQ[notebookPath], fail["missing notebook: " <> notebookPath]];
  notebook = Quiet[Check[Import[notebookPath, "Notebook"], $Failed]];
  If[notebook === $Failed || ! MatchQ[notebook, _Notebook], fail["notebook import failed"]];
  inputBoxes = Cases[notebook, Cell[BoxData[boxes_], "Input", ___] :> boxes, Infinity];
  If[Length[inputBoxes] =!= expectedInputCount,
    Print["ERROR: expected ", expectedInputCount, " input cells, found ", Length[inputBoxes]];
    Print["dirac16complex_ks_mathematica_notebook=FAILED"];
    Exit[1]
  ];

  results = Block[{$Dirac16RepositoryRoot = repositoryRoot},
    Table[
      Module[{cellStart = AbsoluteTime[], value, cellMessages},
        Block[{$MessageList = {}},
          value = Check[ReleaseHold[ToExpression[inputBoxes[[index]], StandardForm, HoldComplete]], $Failed];
          cellMessages = ToString[#, InputForm] & /@ $MessageList;
        ];
        If[cellMessages =!= {}, messages = Join[messages, ("cell " <> ToString[index] <> ": " <> #) & /@ cellMessages]];
        If[value === $Failed || MatchQ[value, _Failure], AppendTo[failedCells, index]];
        If[verbose, Print["cell ", index, " time=", Round[AbsoluteTime[] - cellStart, 0.01], " failed=", value === $Failed || MatchQ[value, _Failure], " messages=", Length[cellMessages]]];
        value],
      {index, Length[inputBoxes]}]
  ];

  messages = DeleteDuplicates[messages];
  checks = If[AssociationQ[Global`notebookChecks], Global`notebookChecks, <||>];
  failedChecks = Keys[Select[checks, ! TrueQ[#] &]];
  measurements = If[AssociationQ[Global`mathematicaReport] && AssociationQ[Global`mathematicaReport["measurements"]], Global`mathematicaReport["measurements"], <||>];

  KeyValueMap[Print["check_", #1, "=", If[TrueQ[#2], "true", "false"]] &, checks];
  KeyValueMap[Print["measurement_", #1, "=", If[NumberQ[#2], ToString[CForm[#2]], ToString[#2, InputForm]]] &, measurements];
  Print["check_count=", Length[checks]];
  Print["failed_check_count=", Length[failedChecks]];
  Print["input_cell_count=", Length[inputBoxes]];
  Print["failed_evaluation_count=", Length[failedCells]];
  Print["message_count=", Length[messages]];
  Print["report=", If[StringQ[Global`reportPath] && FileExistsQ[Global`reportPath], Global`reportPath, "missing"]];
  Print["elapsed_seconds=", Round[AbsoluteTime[] - start]];
  If[failedCells =!= {}, Print["failed_cells=", StringRiffle[ToString /@ failedCells, ","]]];
  If[messages =!= {}, Print["messages=", StringRiffle[messages, " | "]]];
  If[failedChecks =!= {}, Print["failed_checks=", StringRiffle[failedChecks, ","]]];

  ok = failedCells === {} && messages === {} && Length[checks] === expectedCheckCount && failedChecks === {};
  If[Length[checks] =!= expectedCheckCount, Print["ERROR: expected ", expectedCheckCount, " notebook checks, found ", Length[checks]]];
  Print["dirac16complex_ks_mathematica_notebook=", If[ok, "OK", "FAILED"]];
  Exit[If[ok, 0, 1]]
];
