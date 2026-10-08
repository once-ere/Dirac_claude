#!/usr/bin/env wolframscript
(* ::Package:: *)

(* extract_author_curvature_outputs.wls  (Revision/gkd_lovelock/comparison)

   READ-ONLY extraction of the author's OWN stored curvature outputs from the notebook
   Pair_Creation_of_Universes_WaveFunctionOfUniverse-4+4-Einstein-Lovelock-Nash.nb, for the comparison
   with the Revision results (compare_with_author.py).

   How the notebook is read:
   * Get[] of the notebook FILE returns the inert Notebook[...] expression (no front end, no
     NotebookOpen, nothing is saved, the file is never written).
   * Cells are enumerated as Cases[nb, Cell[_, _String, ___], Infinity] (the same enumeration as the
     survey recorded in the README); "cellIndex" is the 1-based position in that list.
   * Stored OUTPUT boxes are converted to expressions with ToExpression[boxes, StandardForm, HoldComplete]
     (MakeExpression inside HoldComplete): the parsed expression is never evaluated, and NONE of the
     notebook's definitions is evaluated (no input cell is run).  The exact InputForm of the held
     expression is written.
   * The defining INPUT cells (the metric, the curvature routine rt[], the calls) are converted the
     same way (held, never evaluated) and written as InputForm text, so the conventions can be read.
   * A keyword scan of the box strings of EVERY cell of both notebooks (this one and
     'Generalized _Kronecker_Delta_4+4.nb') re-checks whether any cell mentions Lovelock tensors.

   Output: author-curvature-outputs.json next to this script (or the path in the environment variable
   AUTHOR_CURVATURE_OUTPUTS).  Deterministic (no dates, no timings in the file), LF line endings, ASCII. *)

$HistoryLength = 0;

here = DirectoryName[$InputFileName];
root = FileNameJoin[{here, "..", "..", ".."}];
nbName = "Pair_Creation_of_Universes_WaveFunctionOfUniverse-4+4-Einstein-Lovelock-Nash.nb";
gkdName = "Generalized _Kronecker_Delta_4+4.nb";
nbPath = FileNameJoin[{root, nbName}];
gkdPath = FileNameJoin[{root, gkdName}];
outPath = With[{e = Environment["AUTHOR_CURVATURE_OUTPUTS"]},
  If[StringQ[e] && e =!= "", e, FileNameJoin[{here, "author-curvature-outputs.json"}]]];

If[! FileExistsQ[nbPath], Print["ERROR: notebook not found: ", nbPath]; Exit[1]];
If[! FileExistsQ[gkdPath], Print["ERROR: notebook not found: ", gkdPath]; Exit[1]];

sha256[p_] := ToLowerCase[IntegerString[FileHash[p, "SHA256"], 16, 64]];

(* ---------- reading (inert expressions only) ---------- *)
readNotebook[p_] := Module[{nb = Get[p]},
  If[Head[nb] =!= Notebook, Print["ERROR: not a Notebook expression: ", p]; Exit[1]];
  nb];

cellList[nb_] := Cases[nb, Cell[b_, style_String, opts___] :> {style,
     Replace[CellLabel /. Cases[{opts}, _Rule | _RuleDelayed], CellLabel -> ""], b}, Infinity];

(* parse boxes WITHOUT evaluation, in a private context so that no parsed symbol can collide with the
   symbols of this script; names print without context *)
heldParse[b_] := Block[{$Context = "AuthorNB`", $ContextPath = {"System`"}},
  Quiet[Check[ToExpression[b, StandardForm, HoldComplete], $Failed]]];

heldInputForm[h_HoldComplete] := Block[{$Context = "AuthorNB`", $ContextPath = {"System`", "AuthorNB`"}},
  StringReplace[
   ToString[HoldForm @@ h, InputForm, CharacterEncoding -> "ASCII", PageWidth -> Infinity],
   "\r\n" -> "\n"]];
heldInputForm[_] := "UNPARSED";

(* ---------- the target cells (labels as stored in the file) ---------- *)
nb = readNotebook[nbPath];
cells = cellList[nb];
Print["cells: ", Length[cells]];

findCell[style_, label_] := Module[{pos = Flatten[Position[cells, {style, label, _}, {1}]]},
  If[Length[pos] =!= 1, Print["ERROR: cell ", style, " ", label, " found ", Length[pos], " times"]; Exit[1]];
  First[pos]];

(* input cells read for the conventions and the provenance of the outputs *)
inputLabels = {"In[79]:=", "In[82]:=", "In[214]:=", "In[235]:=", "In[238]:=", "In[245]:=", "In[535]:=", "In[536]:="};
(* the stored outputs compared *)
outputLabels = {
  {"Out[235]=", "gtry (= MatrixMetric44), the metric to which rt[] was applied by In[238]"},
  {"Out[245]=", "MatrixMetric44 printed again (control: must equal Out[235])"},
  {"Out[535]=", "RS, the Ricci scalar returned by rt[gtry] (In[238])"},
  {"Out[536]=", "EinsteinG, the Einstein tensor returned by rt[gtry] (In[238])"}};

inputRecords = Table[Module[{i = findCell["Input", lab], h},
    h = heldParse[cells[[i, 3]]];
    <|"label" -> lab, "cellIndex" -> i, "parsed" -> (Head[h] === HoldComplete),
      "inputForm" -> heldInputForm[h]|>], {lab, inputLabels}];

outputRecords = Table[Module[{lab = ol[[1]], i, h, dims},
    i = findCell["Output", lab];
    h = heldParse[cells[[i, 3]]];
    dims = Replace[h, {HoldComplete[e_List] :> Dimensions[Unevaluated[e]], _ -> {}}];
    <|"label" -> lab, "cellIndex" -> i, "meaning" -> ol[[2]],
      "parsed" -> (Head[h] === HoldComplete),
      "dimensions" -> dims,
      "inputForm" -> heldInputForm[h]|>], {ol, outputLabels}];

(* ---------- which input cells assign or mention RS / EinsteinG (held, never evaluated) ---------- *)
rsSyms = {"AuthorNB`RS", "AuthorNB`EinsteinG"};
symNames[h_] := Union[Cases[h, s_Symbol :> Context[Unevaluated[s]] <> SymbolName[Unevaluated[s]], {0, Infinity}, Heads -> True]];
assignedNames[h_] := Union[Flatten[Cases[h, (Set | SetDelayed)[lhs_, _] :>
     Cases[HoldComplete[lhs], s_Symbol :> Context[Unevaluated[s]] <> SymbolName[Unevaluated[s]], {0, Infinity}, Heads -> True],
     {0, Infinity}, Heads -> True]]];
rsCells = Select[Table[Module[{h = heldParse[cells[[i, 3]]]},
     If[Head[h] =!= HoldComplete, Nothing,
      <|"cellIndex" -> i, "label" -> cells[[i, 2]],
        "mentions" -> StringDelete[Intersection[symNames[h], rsSyms], "AuthorNB`"],
        "assigns" -> StringDelete[Intersection[assignedNames[h], rsSyms], "AuthorNB`"]|>]],
    {i, Flatten[Position[cells[[All, 1]], "Input"]]}], Length[#["mentions"]] > 0 &];

(* ---------- keyword scan (re-check: is there any Lovelock P2/P3 output?) ---------- *)
atoms[b_] := Cases[b, s_String, {0, Infinity}];
scanNotebook[p_, cl_] := Module[{lov, pk, styles},
  lov = Select[Range[Length[cl]], AnyTrue[atoms[cl[[#, 3]]], StringContainsQ[#, "lovelock", IgnoreCase -> True] &] &];
  pk = Select[Range[Length[cl]], AnyTrue[atoms[cl[[#, 3]]], MemberQ[{"P2", "P3", "P4", "LovelockP", "kd", "k\[Delta]"}, #] &] &];
  styles = SortBy[Tally[cl[[All, 1]]], First];
  <|"file" -> FileNameTake[p], "sha256" -> sha256[p], "cells" -> Length[cl],
    "styleCounts" -> Association[Rule @@@ styles],
    "cellsContainingLovelock" -> Table[<|"cellIndex" -> i, "style" -> cl[[i, 1]], "label" -> cl[[i, 2]],
        "outputIsOnlyStrings" -> If[cl[[i, 1]] === "Output",
          MatchQ[heldParse[cl[[i, 3]]], HoldComplete[_String | {__String}]], Null]|>, {i, lov}],
    "outputCellsContainingLovelock" -> Count[cl[[lov, 1]], "Output"],
    "cellsWithTokenP2P3P4kdelta" -> Table[<|"cellIndex" -> i, "style" -> cl[[i, 1]], "label" -> cl[[i, 2]]|>, {i, pk}]|>];

scanMain = scanNotebook[nbPath, cells];
gkdCells = cellList[readNotebook[gkdPath]];
scanGkd = scanNotebook[gkdPath, gkdCells];

result = <|
  "program" -> "Revision/gkd_lovelock/comparison/extract_author_curvature_outputs.wls",
  "purpose" -> "read-only extraction of the author's stored curvature outputs (no notebook definition evaluated)",
  "notebook" -> nbName,
  "notebookSha256" -> sha256[nbPath],
  "wolframVersion" -> $Version,
  "wolframVersionNumber" -> StringRiffle[ToString /@ {Floor[$VersionNumber], Round[10 FractionalPart[$VersionNumber]], $ReleaseNumber}, "."],
  "cellEnumeration" -> "Cases[Get[file], Cell[_, _String, ___], Infinity], 1-based",
  "conversion" -> "ToExpression[boxes, StandardForm, HoldComplete], then InputForm of the held expression (never evaluated)",
  "inputCells" -> inputRecords,
  "outputCells" -> outputRecords,
  "inputCellsMentioningRSorEinsteinG" -> rsCells,
  "keywordScan" -> {scanMain, scanGkd}
  |>;

(* ---------- deterministic ASCII JSON, LF ---------- *)
json = ExportString[result, "RawJSON", "Compact" -> False];
json = StringReplace[json, "\r\n" -> "\n"];
If[! StringEndsQ[json, "\n"], json = json <> "\n"];
If[! AllTrue[ToCharacterCode[json], # < 128 &], Print["ERROR: non-ASCII character in the JSON"]; Exit[1]];
strm = Quiet[OpenWrite[outPath, BinaryFormat -> True]];
If[Head[strm] =!= OutputStream, Print["ERROR: cannot write ", outPath]; Exit[1]];
BinaryWrite[strm, ToCharacterCode[json]];
Close[strm];

Print["inputs parsed: ", Count[inputRecords, _?(#["parsed"] &)], "/", Length[inputRecords]];
Print["outputs parsed: ", Count[outputRecords, _?(#["parsed"] &)], "/", Length[outputRecords]];
Print["output dimensions: ", #["label"] -> #["dimensions"] & /@ outputRecords];
Print["Lovelock mentions (main, gkd): ", Length[scanMain["cellsContainingLovelock"]], ", ", Length[scanGkd["cellsContainingLovelock"]],
  "; of them Output cells: ", scanMain["outputCellsContainingLovelock"], ", ", scanGkd["outputCellsContainingLovelock"]];
Print["input cells mentioning RS or EinsteinG: ", {#["label"], #["assigns"]} & /@ rsCells];
Print["wrote ", outPath];
