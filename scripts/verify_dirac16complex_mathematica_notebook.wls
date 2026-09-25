#!/usr/bin/env wolframscript
(* ::Package:: *)

(* verify_dirac16complex_mathematica_notebook.wls

   Headless verifier of notebooks/Dirac16ComplexDarkSector.nb (pattern of
   dirac-main/scripts/verify_mathematica_notebook.wls).  It imports the notebook,
   evaluates every Input cell in order with $Dirac16RepositoryRoot set to the
   repository root, and fails (exit code 1) if any cell issues a message or returns
   $Failed, if the number of Input cells or of notebookChecks differs from the
   expected count, or if any entry of notebookChecks is not True.  Evaluating the
   notebook rewrites artifacts/dirac16complex/numerics/mathematica-report.json and the
   PNG files under artifacts/dirac16complex/numerics/figures/mathematica/.

   Usage:  wolframscript -file scripts/verify_dirac16complex_mathematica_notebook.wls [notebook.nb] [--verbose]
           --verbose prints the wall time of every cell.
   The last line printed is dirac16complex_mathematica_notebook=OK or =FAILED.

   License: GPL-3.0-or-later (same as the repository). *)

ClearAll["Global`*"];

Module[
  {scriptDirectory, repositoryRoot, arguments, verbose, notebookPath, notebook, inputBoxes,
   expectedInputCount = 37, expectedCheckCount = 49, messages = {}, results, failedCells = {},
   checks, failedChecks, start = AbsoluteTime[], ok},

  scriptDirectory = DirectoryName[ExpandFileName[$InputFileName]];
  repositoryRoot = ParentDirectory[scriptDirectory];
  arguments = Select[Rest[$ScriptCommandLine], # =!= "--" &];
  verbose = MemberQ[arguments, "--verbose"];
  arguments = DeleteCases[arguments, "--verbose"];
  notebookPath = ExpandFileName[
    If[Length[arguments] >= 1, First[arguments], FileNameJoin[{repositoryRoot, "notebooks", "Dirac16ComplexDarkSector.nb"}]]];

  If[! FileExistsQ[notebookPath],
    Print["ERROR: missing notebook: ", notebookPath];
    Print["dirac16complex_mathematica_notebook=FAILED"];
    Exit[2]
  ];
  notebook = Quiet[Check[Import[notebookPath, "Notebook"], $Failed]];
  If[notebook === $Failed || ! MatchQ[notebook, _Notebook],
    Print["ERROR: notebook import failed"];
    Print["dirac16complex_mathematica_notebook=FAILED"];
    Exit[2]
  ];
  inputBoxes = Cases[notebook, Cell[BoxData[boxes_], "Input", ___] :> boxes, Infinity];
  If[Length[inputBoxes] =!= expectedInputCount,
    Print["ERROR: expected ", expectedInputCount, " input cells, found ", Length[inputBoxes]];
    Print["dirac16complex_mathematica_notebook=FAILED"];
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
        If[value === $Failed, AppendTo[failedCells, index]];
        If[verbose, Print["cell ", index, " time=", Round[AbsoluteTime[] - cellStart, 0.01], " failed=", value === $Failed, " messages=", Length[cellMessages]]];
        value],
      {index, Length[inputBoxes]}]
  ];

  messages = DeleteDuplicates[messages];
  checks = If[AssociationQ[Global`notebookChecks], Global`notebookChecks, <||>];
  failedChecks = Keys[Select[checks, ! TrueQ[#] &]];

  Print["input_cell_count=", Length[inputBoxes]];
  Print["failed_evaluation_count=", Length[failedCells]];
  Print["message_count=", Length[messages]];
  Print["notebook_check_count=", Length[checks]];
  Print["failed_notebook_check_count=", Length[failedChecks]];
  Print["report=", If[StringQ[Global`reportPath] && FileExistsQ[Global`reportPath], Global`reportPath, "missing"]];
  Print["elapsed_seconds=", Round[AbsoluteTime[] - start]];
  If[failedCells =!= {}, Print["failed_cells=", StringRiffle[ToString /@ failedCells, ","]]];
  If[messages =!= {}, Print["messages=", StringRiffle[messages, " | "]]];
  If[failedChecks =!= {}, Print["failed_checks=", StringRiffle[failedChecks, ","]]];

  ok = failedCells === {} && messages === {} && Length[checks] === expectedCheckCount && failedChecks === {};
  If[Length[checks] =!= expectedCheckCount, Print["ERROR: expected ", expectedCheckCount, " notebook checks, found ", Length[checks]]];
  Print["dirac16complex_mathematica_notebook=", If[ok, "OK", "FAILED"]];
  Exit[If[ok, 0, 1]]
];
