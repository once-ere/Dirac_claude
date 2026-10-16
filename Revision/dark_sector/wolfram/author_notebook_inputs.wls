#!/usr/bin/env wolframscript
(* ::Package:: *)

(* author_notebook_inputs.wls

   Reads the author's notebook Dirac_Einstein-Lovelock_4+4_Nash.nb WITHOUT evaluating anything and records its cells:
   every Input cell as InputForm text (each input box converted with ToExpression[box, StandardForm, HoldForm]) and every
   Title/Section/Subsection/Text cell as text.  The record keeps, per cell, its kind, its label (In[n]), the first 400
   characters and the sha256 of the full text (one input cell holds an embedded image of about 12 MB).  Given a second
   notebook (the pinned version of the author's order, commit b13373c), it lists the cells that differ.

   This is the provenance of the dark-sector update to the metric with b4 (2026-10-15): it shows the coordinates
   In[48] X = {x0[], ..., x7[]}, the metric In[97]-In[102] with b4[x4] in the three extra-time components, and the
   vacuum equations and their solution In[129]-In[134].

   Usage (repository root):
     git show b13373c:Dirac_Einstein-Lovelock_4+4_Nash.nb > <scratch>/pinned.nb
     wolframscript -file Revision/dark_sector/wolfram/author_notebook_inputs.wls Dirac_Einstein-Lovelock_4+4_Nash.nb <scratch>/pinned.nb
   Writes Revision/dark_sector/reports/author-notebook-inputs.json (UTF-8, LF). *)

$here = DirectoryName[$InputFileName];
$rev = ExpandFileName[FileNameJoin[{$here, "..", ".."}]];
$out = FileNameJoin[{$rev, "dark_sector", "reports", "author-notebook-inputs.json"}];
args = Rest[$ScriptCommandLine];
If[Length[args] < 1, Print["ERROR  usage: author_notebook_inputs.wls NOTEBOOK [PINNED_NOTEBOOK]"]; Exit[1]];
sha[f_] := IntegerString[FileHash[f, "SHA256"], 16, 64];
strsha[s_String] := IntegerString[Hash[ByteArray[StringToByteArray[s, "UTF-8"]], "SHA256"], 16, 64];
styles = {"Input", "Text", "Section", "Subsection", "Subsubsection", "Title"};
label[opts___] := Module[{l = Cases[{opts}, (CellLabel -> x_) :> x]}, If[l === {}, "", First[l]]];
text[Cell[c_, "Input", opts___]] := Module[{h = Quiet@Check[ToExpression[c, StandardForm, HoldForm], $Failed]},
   If[h === $Failed, "<<unparsed>> " <> ToString[c, InputForm], ToString[h, InputForm]]];
text[Cell[c_String, style_, opts___]] := c;
text[Cell[c_, style_, opts___]] := ToString[c, InputForm];
cellsOf[f_] := Module[{nb = Import[f, "Notebook"]},
   Cases[nb, Cell[c_, style_String, opts___] /; MemberQ[styles, style] :> <|"kind" -> style,
       "label" -> label[opts], "text" -> Quiet@Check[text[Cell[c, style, opts]], "<<error>>"]|>, Infinity]];
cur = cellsOf[args[[1]]];
rec[cells_] := MapIndexed[<|"index" -> First[#2], "kind" -> #1["kind"], "label" -> #1["label"],
     "text" -> StringTake[#1["text"], UpTo[400]], "chars" -> StringLength[#1["text"]], "sha256" -> strsha[#1["text"]]|> &, cells];
out = <|"producer" -> "Revision/dark_sector/wolfram/author_notebook_inputs.wls",
   "notebook" -> FileNameTake[args[[1]]], "notebookSha256" -> sha[args[[1]]], "cellCount" -> Length[cur],
   "inputCellCount" -> Count[cur, c_ /; c["kind"] === "Input"], "cells" -> rec[cur]|>;
If[Length[args] >= 2,
  pin = cellsOf[args[[2]]];
  key[c_] := c["kind"] <> "|" <> c["text"];
  onlyCur = Complement[key /@ cur, key /@ pin]; onlyPin = Complement[key /@ pin, key /@ cur];
  out["pinned"] = <|"notebookSha256" -> sha[args[[2]]], "cellCount" -> Length[pin],
     "cellsOnlyInCurrent" -> (StringTake[#, UpTo[400]] & /@ onlyCur), "cellsOnlyInPinned" -> (StringTake[#, UpTo[400]] & /@ onlyPin)|>];
s = ExportString[out, "JSON", "Compact" -> False];
If[! DirectoryQ[DirectoryName[$out]], CreateDirectory[DirectoryName[$out]]];
(* ExportString returns the UTF-8 bytes as characters: write them as they are *)
If[Quiet[BinaryWrite[$out, ByteArray[ToCharacterCode[StringReplace[s, "\r\n" -> "\n"] <> "\n"]]]] === $Failed, Print["ERROR  cannot write ", $out]; Exit[1]];
Close[$out];
Print["cells=", Length[cur], " inputs=", out["inputCellCount"], If[KeyExistsQ[out, "pinned"],
   " onlyInCurrent=" <> ToString[Length[out["pinned"]["cellsOnlyInCurrent"]]] <> " onlyInPinned=" <> ToString[Length[out["pinned"]["cellsOnlyInPinned"]]], ""]];
Print["author_notebook_inputs=OK"];
