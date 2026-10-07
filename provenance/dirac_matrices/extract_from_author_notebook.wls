#!/usr/bin/env wolframscript
(* ::Package:: *)

(* extract_from_author_notebook.wls

   Reads the AUTHOR's notebook (read only, never modified)
     Pair_Creation_of_Universes_WaveFunctionOfUniverse-4+4-Einstein-Lovelock-Nash.nb
   and evaluates, in a fresh kernel, exactly the author's own input cells that define the eight real
   16 x 16 Dirac matrices T16A[0..7], their products sigma16 and T16A[8], and the projectors P_L, P_R.
   Nothing is re-typed: the cell boxes are taken from the notebook and evaluated with ToExpression.
   The only change is the box SuperscriptBox["T16","A"] -> the symbol T16A (in the front end the
   notebook writes T16^A; as plain kernel input that would parse as Power, which is Protected).

   Every cell is located by its index among the notebook's Input cells AND guarded by the text it
   must contain, so a changed notebook stops the run with an ERROR line instead of silently using a
   different cell.

   Output (deterministic): provenance/dirac_matrices/author_notebook_T16.json
   Usage (from the repository root):
     wolframscript -file provenance/dirac_matrices/extract_from_author_notebook.wls
*)

$root = FileNameJoin[{DirectoryName[$InputFileName], "..", ".."}];
nbFile = FileNameJoin[{$root, "Pair_Creation_of_Universes_WaveFunctionOfUniverse-4+4-Einstein-Lovelock-Nash.nb"}];
If[!FileExistsQ[nbFile], Print["ERROR: author notebook not found: ", nbFile]; Exit[1]];
nb = Import[nbFile, "Notebook"];
cells = Cases[nb, Cell[b_, "Input", ___] :> b, Infinity] /. SuperscriptBox["T16", "A"] -> "T16A";
Print["author notebook: ", Length[cells], " input cells"];

(* {input-cell index, text the cell must contain, what it defines} in evaluation order *)
plan = {
  {41,  "\[Eta]4488 = ArrayFlatten",            "eta4488 = diag(I4, -I4)"},
  {42,  "\[Sigma] = ArrayFlatten",              "sigma = {{0, I4}, {I4, 0}}"},
  {109, "ID8 = IdentityMatrix[8]",             "ID4, ID8"},
  {114, "ID16 = IdentityMatrix[16]",           "ID16, ZERO16"},
  {223, "Qa[h_, p_, q_] := Signature",         "Qa, Qb, SelfDualAntiSymmetric, AntiSelfDualAntiSymmetric"},
  {226, "s4by4[h] = Table",                    "s4by4[1..3]"},
  {227, "t4by4[h] = Table",                    "t4by4[1..3]"},
  {257, "\[Tau][7 - h] = ArrayFlatten",         "tau[0..7]"},
  {267, "OverBar[\[Tau]][A] = FullSimplify",    "taubar[0..7]"},
  {286, "T16A[A1] = ArrayFlatten",             "T16A[0..7] = {{0, taubar}, {tau, 0}}"},
  {285, "\[Sigma]16 = T16A[0] . T16A[1]",       "sigma16 = T16A[0].T16A[1].T16A[2].T16A[3]"},
  {287, "T16A[8] = T16A[0] . T16A[1]",          "T16A[8] = T16A[0]...T16A[7]"},
  {323, "Subscript[P, L] = (1/2)*(ID16 - T16A[8])", "P_L = (ID16 - T16A[8])/2"},
  {324, "Subscript[P, R] = (1/2)*(ID16 + T16A[8])", "P_R = (ID16 + T16A[8])/2"}
};

text[i_] := ToString[ToExpression[cells[[i]], StandardForm, HoldForm], InputForm];
Do[
  {i, must, what} = step;
  If[i > Length[cells] || !StringContainsQ[text[i], must],
    Print["ERROR: notebook input cell ", i, " does not contain \"", must, "\""]; Exit[1]];
  ToExpression[cells[[i]], StandardForm];
  Print["evaluated author input cell ", i, ": ", what],
  {step, plan}];

T = Table[T16A[k], {k, 0, 8}];
PL = Subscript[P, L]; PR = Subscript[P, R];
ok = AllTrue[Flatten[{T, \[Sigma]16, 2 PL, 2 PR}], IntegerQ] && Dimensions[T] == {9, 16, 16};
If[!ok, Print["ERROR: the evaluated matrices are not 16 x 16 integer matrices"]; Exit[1]];

out = FileNameJoin[{DirectoryName[$InputFileName], "author_notebook_T16.json"}];
Export[out, <|
  "source" -> "Pair_Creation_of_Universes_WaveFunctionOfUniverse-4+4-Einstein-Lovelock-Nash.nb (author notebook, read only)",
  "cells" -> (<|"input_cell" -> #[[1]], "defines" -> #[[3]]|> & /@ plan),
  "eta4488" -> \[Eta]4488,
  "T16A" -> T[[1 ;; 8]],
  "T16A_8" -> T[[9]],
  "sigma16" -> \[Sigma]16,
  "twice_PL" -> 2 PL,
  "twice_PR" -> 2 PR
|>, "JSON", "Compact" -> 1];
Print["wrote ", out];
