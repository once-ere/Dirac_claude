#!/usr/bin/env wolframscript
(* ::Package:: *)

(* extract_author_b4_outputs.wls

   Reads the AUTHOR's notebook Dirac_Einstein-Lovelock_4+4_Nash.nb (repository root; read only, never
   modified, never evaluated) and writes the author's STORED results for the primordial metric of
   2026-10-14 into Revision/metric_b4/results/author-b4-outputs.json:

     the input cell In[97] that builds the metric (beta1 = Sin[6 H x0]^(1/3), beta2 = Cot[6 H x0]^2,
     beta3 = Exp[2 a4[x4]], DiagonalMatrix[...] with b4[x4]) and the stored metric Out[101];
     Ricci R_ab (Out[123]), Ricci R_a^b (Out[124]), Ricci scalar (Out[119]), Einstein G_a^b (Out[120]),
     the Lovelock tensors allLovelock1, allLovelock2, allLovelock3 (Out[126], Out[127], Out[128]),
     the vacuum Einstein-Lovelock equations (Out[129]), their distinct nonzero entries (Out[132]) and the
     author's solution (Out[134], Out[135]).

   Every stored output is converted from its boxes to an expression WITHOUT evaluation (ToExpression with
   head HoldComplete; a cell of several lines gives a list of held lines), written in InputForm, and the author's symbols are mapped to plain names: x0[] -> X0, x1[]..x7[]
   -> X1..X7, a4, b4, H, w1, w2, w3, Lambda.  The notebook's coordinate order is (x0, x1, ..., x7) with x0
   the hidden direction; the Revision order (x1, ..., x8) puts the hidden direction last (x8 = x0).  This
   script does NOT reorder: it records the author's arrays as stored; the comparison script reorders.

   Output: UTF-8, LF, no time stamps; the notebook's sha256 is recorded (key notebookSha256).
   Usage (repository root): wolframscript -file Revision/metric_b4/wolfram/extract_author_b4_outputs.wls *)

$root = ParentDirectory[DirectoryName[$InputFileName], 3];
$nbFile = FileNameJoin[{$root, "Dirac_Einstein-Lovelock_4+4_Nash.nb"}];
If[! FileExistsQ[$nbFile], Print["ERROR: author notebook not found: ", $nbFile]; Exit[1]];
$out = FileNameJoin[{$root, "Revision", "metric_b4", "results", "author-b4-outputs.json"}];
nb = Import[$nbFile, "Notebook"];
cells = Cases[nb, Cell[_, "Input" | "Output", ___], Infinity];
label[c_] := Replace[Cases[c, (CellLabel -> l_String) :> l], {{l_, ___} :> StringTrim[l], {} -> ""}];
byLabel[l_String] := Module[{m = Select[cells, StringStartsQ[label[#], l] &]},
  If[Length[m] != 1, Print["ERROR: expected exactly one cell labelled ", l, ", found ", Length[m]]; Exit[1]]; First[m]];
toText[c_] := Module[{b = c[[1]], held},
  If[! MatchQ[b, _BoxData], Print["ERROR: not BoxData: ", label[c]]; Exit[1]];
  held = Quiet[ToExpression[b[[1]], StandardForm, HoldComplete]];
  If[! MatchQ[held, _HoldComplete | {__HoldComplete}], Print["ERROR: boxes do not parse: ", label[c]]; Exit[1]];
  StringReplace[ToString[held, InputForm, PageWidth -> Infinity], {
    "$CellContext`" -> "", "xAct`xCoba`" -> "", "xAct`xTensor`" -> "",
    "x0[]" -> "X0", "x1[]" -> "X1", "x2[]" -> "X2", "x3[]" -> "X3", "x4[]" -> "X4", "x5[]" -> "X5",
    "x6[]" -> "X6", "x7[]" -> "X7", "\[CapitalLambda]" -> "Lambda", "\[CapitalLambda]" -> "Lambda"}]];
want = {"In[97]", "Out[101]", "Out[119]", "Out[120]", "Out[123]", "Out[124]", "Out[126]", "Out[127]", "Out[128]",
  "Out[129]", "Out[132]", "Out[134]", "Out[135]"};
data = Association[(# -> toText[byLabel[#]]) & /@ want];
json = ExportString[<|"notebook" -> "Dirac_Einstein-Lovelock_4+4_Nash.nb",
   "notebookSha256" -> IntegerString[FileHash[$nbFile, "SHA256"], 16, 64],
   "wolframVersion" -> ToString[$VersionNumber] <> "." <> ToString[$ReleaseNumber],
   "symbolMap" -> "x0[] -> X0 (hidden direction), x1[]..x7[] -> X1..X7; held InputForm of the stored boxes, unevaluated (HoldComplete[...])",
   "cells" -> data|>, "JSON", "Compact" -> False];
BinaryWrite[$out, StringToByteArray[json <> "\n", "UTF-8"]]; Close[$out];
Print["author_b4_outputs=OK cells=", Length[data], " file=", $out];
