#!/usr/bin/env wolframscript
(* ::Package:: *)

(* extract_from_author_notebook.wls

   Reads the AUTHOR's notebook (read only, never modified)
     Pair_Creation_of_Universes_WaveFunctionOfUniverse-4+4-Einstein-Lovelock-Nash.nb
   and evaluates, in a fresh kernel, exactly the author's own input cells that define the eight real
   16 x 16 Dirac matrices T16A[0..7], their products sigma16 and T16A[8], the projectors P_L, P_R and
   the scaled commutators SAB.  Nothing is re-typed: the cell boxes are taken from the notebook and
   evaluated with ToExpression, in the author's evaluation order (increasing CellLabel In[n]).

   The author's notebook environment and how it is reproduced here.
   The author loads the Notation package (input cell 51, In[55]: Needs["Notation`"]) and Symbolizes
   three boxes: OverBar[tau] (input cell 54, In[58]), T16^A (input cell 55, In[59]) and T16^alpha
   (input cell 56, In[60]).  After Symbolize each box is ONE atomic symbol: the notebook records the
   name of the T16^A symbol, T16\[UnderBracket]Superscript\[UnderBracket]A (input cell 477, In[583]),
   and the author's own Head check of taubar (input cell 248, In[326]) prints Symbol.  The Notation
   package needs a front end, which wolframscript does not have, so Symbolize is EMULATED: before
   evaluation the box SuperscriptBox["T16","A"] is replaced by the atomic symbol
   T16\[UnderBracket]Superscript\[UnderBracket]A (the author's own name) and the box
   OverscriptBox["\[Tau]","_"] by the atomic symbol \[Tau]\[UnderBracket]Overscript\[UnderBracket]Bar
   (a stand-in name: the name Notation creates for this box is not recorded in the notebook; only its
   atomicity matters).  Without the emulation T16^A[A1] = ... would parse as Power (Protected) and
   taubar would be stored as SubValues of System`OverBar.  These two box replacements are the only
   changes; T16^alpha is not evaluated here.  Below, "T16A" and "taubar" name these two symbols.

   Evaluation order.  The author evaluated input cell 285 (In[370], sigma16 = T16A[0].T16A[1].
   T16A[2].T16A[3]) BEFORE input cell 286 (In[371], the definition of T16A[0..7]); his stored output
   Out[370] is the unevaluated product.  So in the author's kernel sigma16 holds the symbolic product
   and takes its matrix value when T16A is defined.  This script uses the same order (the run stops
   if the In[n] labels of the plan are not strictly increasing) and records that sigma16 is still the
   symbolic product right after cell 285.

   Every cell is located by its index among the notebook's Input cells AND guarded by the text it
   must contain, so a changed notebook stops the run with an ERROR line instead of silently using a
   different cell.  The script also reads the author's STORED outputs of the display cells (so the
   Python builder can compare them with the evaluated values entry by entry) and scans all input
   cells for where the matrices are assigned and used (the chain to the Lagrangians).

   Output (deterministic, the same bytes on every operating system: UTF-8, LF line endings, no time
   stamps): provenance/dirac_matrices/author_notebook_T16.json.  The JSON text is made with ExportString
   (which gives UTF-8 bytes with LF line endings) and written byte for byte with BinaryWrite, because
   Export[file, ...] on Windows writes CR LF.  The JSON records $Version (key "wolfram_version"), so a
   difference caused by another Wolfram version can be recognised.
   Usage (from the repository root):
     wolframscript -file provenance/dirac_matrices/extract_from_author_notebook.wls
*)

$xRoot = FileNameJoin[{DirectoryName[$InputFileName], "..", ".."}];
$xNbFile = FileNameJoin[{$xRoot, "Pair_Creation_of_Universes_WaveFunctionOfUniverse-4+4-Einstein-Lovelock-Nash.nb"}];
If[!FileExistsQ[$xNbFile], Print["ERROR: author notebook not found: ", $xNbFile]; Exit[1]];
$xNb = Import[$xNbFile, "Notebook"];
$xAll = Cases[$xNb, Cell[_, "Input" | "Output", ___], Infinity];
$xInPos = Flatten[Position[$xAll, Cell[_, "Input", ___], {1}]];
$xRaw = $xAll[[#, 1]] & /@ $xInPos;
Print["author notebook: ", Length[$xRaw], " input cells"];

$xLabel[i_] := First[Cases[$xAll[[$xInPos[[i]]]], (CellLabel -> s_String) :> StringTrim[StringReplace[s, ":=" -> ""]], {1}], "none"];
$xLabelNumber[i_] := First[StringCases[$xLabel[i], "In[" ~~ n : DigitCharacter .. ~~ "]" :> ToExpression[n]], Missing[]];
(* the Output cells that directly follow input cell i *)
$xOutputs[i_] := Module[{p = $xInPos[[i]] + 1, r = {}},
  While[p <= Length[$xAll] && MatchQ[$xAll[[p]], Cell[_, "Output", ___]], AppendTo[r, $xAll[[p]]]; p++]; r];
$xOutLabel[c_] := First[Cases[c, (CellLabel -> s_String) :> StringTrim[StringTrim[s], "="], {1}], "none"];

(* readable text of boxes, only for guards and records (never evaluated) *)
$xReadable[b_] := ToString[ToExpression[b /. {SuperscriptBox["T16", "A"] -> "T16A",
     SuperscriptBox["T16", "\[Alpha]"] -> "T16alpha", OverscriptBox["\[Tau]", "_"] -> "taubar"},
     StandardForm, HoldForm], InputForm];
$xText[i_] := $xReadable[$xRaw[[i]]];

(* Symbolize emulation (see the header) *)
$xT16Name = "T16\[UnderBracket]Superscript\[UnderBracket]A";
$xTauBarName = "\[Tau]\[UnderBracket]Overscript\[UnderBracket]Bar";
$xEmulate[b_] := b /. {SuperscriptBox["T16", "A"] -> $xT16Name, OverscriptBox["\[Tau]", "_"] -> $xTauBarName};

(* the author's Notation environment: guard the cells that the header cites *)
$xEnv = {
  {51, "Needs[\"Notation`\"]", "Needs[\"Notation`\"]: loads the Notation package"},
  {54, "Symbolize[NotationTemplateTag[taubar]]", "Symbolize taubar (OverBar[tau])"},
  {55, "Symbolize[NotationTemplateTag[T16A]]", "Symbolize T16^A"},
  {56, "Symbolize[NotationTemplateTag[T16alpha]]", "Symbolize T16^alpha"},
  {477, Null, "the name of the symbolized T16^A: T16\[UnderBracket]Superscript\[UnderBracket]A"}
};
Do[
  If[If[e[[2]] === Null, $xRaw[[e[[1]]]] =!= BoxData[$xT16Name], !StringContainsQ[$xText[e[[1]]], e[[2]]]],
    Print["ERROR: notebook input cell ", e[[1]], " is not the expected Notation cell: ", e[[3]]]; Exit[1]],
  {e, $xEnv}];

(* {input-cell index, text the cell must contain, what it defines}, in the author's order *)
$xPlan = {
  {41,  "\[Eta]4488 = ArrayFlatten",              "eta4488 = diag(I4, -I4)"},
  {42,  "\[Sigma] = ArrayFlatten",                "sigma = {{0, I4}, {I4, 0}}"},
  {109, "ID8 = IdentityMatrix[8]",               "ID4, ID8"},
  {114, "ID16 = IdentityMatrix[16]",             "ID16, ZERO16"},
  {223, "Qa[h_, p_, q_] := Signature",           "Qa, Qb, SelfDualAntiSymmetric, AntiSelfDualAntiSymmetric"},
  {226, "s4by4[h] = Table",                      "s4by4[1..3]"},
  {227, "t4by4[h] = Table",                      "t4by4[1..3]"},
  {257, "\[Tau][7 - h] = ArrayFlatten",           "tau[0..7]"},
  {267, "taubar[A] = FullSimplify",              "taubar[0..7]"},
  {285, "\[Sigma]16 = T16A[0] . T16A[1] . T16A[2] . T16A[3]", "sigma16 = T16A[0].T16A[1].T16A[2].T16A[3] (T16A not yet defined)"},
  {286, "T16A[A1] = ArrayFlatten[{{0, taubar[A1]}, {\[Tau][A1], 0}}]", "T16A[0..7] = {{0, taubar}, {tau, 0}}"},
  {287, "T16A[8] = T16A[0] . T16A[1]",            "T16A[8] = T16A[0]...T16A[7]"},
  {323, "Subscript[P, L] = (1/2)*(ID16 - T16A[8])", "P_L = (ID16 - T16A[8])/2"},
  {324, "Subscript[P, R] = (1/2)*(ID16 + T16A[8])", "P_R = (ID16 + T16A[8])/2"},
  {326, "SAB = Table[(1/4)*(T16A[A1] . T16A[B1] - T16A[B1] . T16A[A1])", "SAB = (1/4)[T16A[A1], T16A[B1]], A1, B1 = 0..7"}
};
$xLabels = $xLabelNumber[#[[1]]] & /@ $xPlan;
If[!(VectorQ[$xLabels, IntegerQ] && Less @@ $xLabels),
  Print["ERROR: the In[n] labels of the plan are not strictly increasing: ", $xLabels]; Exit[1]];

$xSigmaAfter285 = Missing[];
Do[
  {$xI, $xMust, $xWhat} = $xStep;
  If[$xI > Length[$xRaw] || !StringContainsQ[$xText[$xI], $xMust],
    Print["ERROR: notebook input cell ", $xI, " does not contain \"", $xMust, "\""]; Exit[1]];
  ToExpression[$xEmulate[$xRaw[[$xI]]], StandardForm];
  If[$xI == 285,
    $xSigmaAfter285 = With[{t = Symbol[$xT16Name]},
      Cases[OwnValues[\[Sigma]16], HoldPattern[_ :> r_] :> Hold[r]] === {Hold[Dot[t[0], t[1], t[2], t[3]]]}]];
  Print["evaluated author input cell ", $xI, " (", $xLabel[$xI], "): ", $xWhat],
  {$xStep, $xPlan}];

$xT16 = Symbol[$xT16Name];
$xTauBar = Symbol[$xTauBarName];
$xT = Table[$xT16[k], {k, 0, 8}];
$xPL = Subscript[P, L]; $xPR = Subscript[P, R];
$xOk = AllTrue[Flatten[{$xT, \[Sigma]16, 2 $xPL, 2 $xPR, 4 SAB}], IntegerQ] && Dimensions[$xT] == {9, 16, 16} &&
  Dimensions[SAB] == {8, 8, 16, 16} && Head[$xTauBar] === Symbol && Length[DownValues[Evaluate[$xTauBar]]] == 8 &&
  SubValues[OverBar] === {};
If[!$xOk, Print["ERROR: the evaluated matrices are not 16 x 16 integer matrices (or the Symbolize emulation failed): ",
  {AllTrue[Flatten[{$xT, \[Sigma]16, 2 $xPL, 2 $xPR, 4 SAB}], IntegerQ], Dimensions[$xT], Dimensions[SAB],
   Head[$xTauBar], Length[DownValues[Evaluate[$xTauBar]]], Length[SubValues[OverBar]]}]; Exit[1]];

(* ---- the author's stored outputs of the display cells *)
$xMatrixOut[i_] := Module[{o = $xOutputs[i]},
  If[Length[o] != 1, Print["ERROR: expected one output cell after input cell ", i]; Exit[1]];
  ReleaseHold[ToExpression[o[[1, 1]], StandardForm, HoldForm]] /. MatrixForm[m_] :> m];
$xStored = {
  {257, "tau[7]", $xMatrixOut[257]},
  {287, "T16A[8]", $xMatrixOut[287]},
  {288, "sigma16", $xMatrixOut[288]},
  {298, "sigma16", $xMatrixOut[298]},
  {323, "P_L", $xMatrixOut[323]},
  {324, "P_R", $xMatrixOut[324]}
};
Do[If[!(MatrixQ[s[[3]], IntegerQ] || MatrixQ[s[[3]], IntegerQ[2 #] &]),
    Print["ERROR: stored output after input cell ", s[[1]], " is not a matrix"]; Exit[1]], {s, $xStored}];
If[!StringContainsQ[$xText[288], "MatrixForm[\[Sigma]16]"] || !StringContainsQ[$xText[298], "MatrixForm[\[Sigma]16]"],
  Print["ERROR: input cells 288 / 298 are not MatrixForm[sigma16]"]; Exit[1]];
$xOut370 = $xReadable[$xOutputs[285][[1, 1]]];
$xOut406 = $xReadable[$xOutputs[325][[1, 1]]];
$xOut393 = $xOutputs[314];
If[Length[$xOut393] != 1 || !StringContainsQ[$xText[314], "(1/2)*(T16A[A1] . T16A[B1] + T16A[B1] . T16A[A1])"],
  Print["ERROR: input cell 314 is not the author's anticommutator check"]; Exit[1]];
$xClifTrue = Count[$xOut393[[1, 1]], "True", Infinity];
$xClifFalse = Count[$xOut393[[1, 1]], "False", Infinity];

(* ---- scan of all input cells: where the matrices are assigned and used (commented-out code (* ... *) is removed first) *)
$xUncomment[b_] := b //. RowBox[{pre___, "(*", Shortest[___], "*)", post___}] :> RowBox[{pre, post}];
$xCode = $xUncomment /@ $xRaw;
$xNames = {
  {"sigma16", "\[Sigma]16"}, {"T16A", SuperscriptBox["T16", "A"]}, {"T16alpha", SuperscriptBox["T16", "\[Alpha]"]},
  {"SAB", "SAB"}, {"useT16", "useT16"}, {"base16", "base16"}, {"Psi16", "\[CapitalPsi]16"},
  {"Lg", "Lg"}, {"La", "La"}, {"Lj", "Lj"}, {"eL", "eL"}, {"eLa", "eLa"},
  {"P_L", SubscriptBox["P", "L"]}, {"P_R", SubscriptBox["P", "R"]}};
$xWs = _String?(StringMatchQ[#, Whitespace] &);
$xHead[RowBox[{h_, "[", ___}]] := $xHead[h];
$xHead[x_] := x;
$xAssigned[b_] := $xHead /@ Cases[b, RowBox[{lhs_, $xWs ..., "=" | ":=", ___}] :> lhs, Infinity];
$xAssignTable = $xAssigned /@ $xCode;
$xAssignedIn = Association[Table[n[[1]] -> Flatten[Position[$xAssignTable, l_ /; MemberQ[l, n[[2]]], {1}, Heads -> False]], {n, $xNames}]];
$xRefIn[pat_] := Flatten[Position[$xCode, b_ /; !FreeQ[b, pat], {1}, Heads -> False]];
$xT16A8 = RowBox[{SuperscriptBox["T16", "A"], "[", "8", "]"}];
$xReferencedIn = <|"P_L" -> $xRefIn[SubscriptBox["P", "L"]], "P_R" -> $xRefIn[SubscriptBox["P", "R"]],
  "T16A[8]" -> $xRefIn[$xT16A8]|>;
$xChainCells = {43, 285, 286, 314, 325, 326, 361, 362, 367, 451, 453, 479, 821, 822, 828, 830, 836, 839, 841};
$xChain = Table[<|"input_cell" -> c, "label" -> $xLabel[c],
    "assigns" -> Select[$xNames, MemberQ[$xAssignTable[[c]], #[[2]]] &][[All, 1]],
    "refs" -> Select[$xNames, !FreeQ[$xCode[[c]], #[[2]]] &][[All, 1]],
    "text" -> StringTake[$xText[c], UpTo[160]]|>, {c, $xChainCells}];
$xCited = Union[$xChainCells, Flatten[Values[$xAssignedIn]], Flatten[Values[$xReferencedIn]],
  $xEnv[[All, 1]], $xPlan[[All, 1]], {248, 288, 298}];

(* the same bytes on every operating system: UTF-8 JSON with LF line endings, written byte for byte *)
$xWriteJSON[file_String, data_Association] := Module[{s = ExportString[data, "JSON", "Compact" -> 1], st},
  If[!StringQ[s] || Max[ToCharacterCode[s]] > 255 || MemberQ[ToCharacterCode[s], 13],
    Print["ERROR: ExportString did not return UTF-8 bytes with LF line endings"]; Exit[1]];
  st = OpenWrite[file, BinaryFormat -> True];
  BinaryWrite[st, Append[ToCharacterCode[s], 10]];
  Close[st]];

$xOut = FileNameJoin[{DirectoryName[$InputFileName], "author_notebook_T16.json"}];
$xWriteJSON[$xOut, <|
  "source" -> "Pair_Creation_of_Universes_WaveFunctionOfUniverse-4+4-Einstein-Lovelock-Nash.nb (author notebook, read only)",
  "producer" -> "provenance/dirac_matrices/extract_from_author_notebook.wls",
  "wolfram_version" -> $Version,
  "notation" -> <|
    "cells" -> (<|"input_cell" -> #[[1]], "label" -> $xLabel[#[[1]]], "what" -> #[[3]]|> & /@ $xEnv),
    "taubar_head_check" -> <|"input_cell" -> 248, "label" -> $xLabel[248],
      "stored_outputs" -> ($xReadable[#[[1]]] & /@ $xOutputs[248])|>,
    "emulated_names" -> <|"T16A" -> $xT16Name, "taubar" -> $xTauBarName|>,
    "taubar_atomic" -> (Head[$xTauBar] === Symbol), "OverBar_SubValues_empty" -> (SubValues[OverBar] === {})|>,
  "cells" -> (<|"input_cell" -> #[[1]], "label" -> $xLabel[#[[1]]], "defines" -> #[[3]]|> & /@ $xPlan),
  "sigma16_symbolic_after_cell_285" -> $xSigmaAfter285,
  "eta4488" -> \[Eta]4488,
  "sigma8" -> \[Sigma],
  "tau" -> Table[\[Tau][k], {k, 0, 7}],
  "taubar" -> Table[$xTauBar[k], {k, 0, 7}],
  "T16A" -> $xT[[1 ;; 8]],
  "T16A_8" -> $xT[[9]],
  "sigma16" -> \[Sigma]16,
  "twice_PL" -> 2 $xPL,
  "twice_PR" -> 2 $xPR,
  "four_SAB" -> 4 SAB,
  "stored_outputs" -> (<|"input_cell" -> #[[1]], "in_label" -> $xLabel[#[[1]]],
      "out_label" -> $xOutLabel[$xOutputs[#[[1]]][[1]]], "what" -> #[[2]], "twice_matrix" -> 2 #[[3]]|> & /@ $xStored),
  "stored_Out370" -> <|"input_cell" -> 285, "out_label" -> $xOutLabel[$xOutputs[285][[1]]], "text" -> $xOut370|>,
  "stored_Out406" -> <|"input_cell" -> 325, "out_label" -> $xOutLabel[$xOutputs[325][[1]]], "text" -> $xOut406|>,
  "stored_Out393" -> <|"input_cell" -> 314, "out_label" -> $xOutLabel[$xOut393[[1]]], "true" -> $xClifTrue, "false" -> $xClifFalse|>,
  "scan" -> <|"assigned_in" -> $xAssignedIn, "referenced_in" -> $xReferencedIn, "chain" -> $xChain|>,
  "labels" -> Association[ToString[#] -> $xLabel[#] & /@ $xCited]
|>];
Print["wrote ", $xOut];
