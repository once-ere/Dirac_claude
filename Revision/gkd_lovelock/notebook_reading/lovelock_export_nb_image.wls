(* Render the image held by the input cell In[101] of the author's notebook (the author's In[68], Lovelock's
   equation (4.38)) to Revision/gkd_lovelock/results/notebook-in68-image.png.  Run from the repository root:
     wolframscript -file Revision/gkd_lovelock/notebook_reading/lovelock_export_nb_image.wls
   Only that input cell is read; no output cell is read or evaluated.
   Deterministic: Export writes PNG text chunks (tEXt "Creation Time" and the like) that change from run to run;
   they are removed below (tEXt, zTXt, iTXt and tIME chunks; every other chunk, including IDAT, is kept byte for
   byte, and the CRC of each kept chunk is unchanged), so two runs give byte-identical files. *)
nb = Get[FileNameJoin[{Directory[], "Generalized _Kronecker_Delta_4+4.nb"}]];
cells = Cases[nb, Cell[b_, "Input", opts___] /; MemberQ[{opts}, CellLabel -> "In[101]:="] :> b, Infinity];
img = First[Cases[ToExpression[First[cells], StandardForm, HoldComplete], _Image, Infinity]];
Print[ImageDimensions[img]];
out = FileNameJoin[{Directory[], "Revision", "gkd_lovelock", "results", "notebook-in68-image.png"}];
bytes = ExportByteArray[img, "PNG"];
stripPNG[ba_ByteArray] := Module[{b = Normal[ba], pos = 9, keep = {}, len, type},
  If[Take[b, 8] =!= {137, 80, 78, 71, 13, 10, 26, 10}, Print["ERROR: not a PNG"]; Exit[2]];
  keep = Take[b, 8];
  While[pos <= Length[b],
    len = FromDigits[b[[pos ;; pos + 3]], 256];
    type = FromCharacterCode[b[[pos + 4 ;; pos + 7]]];
    If[! MemberQ[{"tEXt", "zTXt", "iTXt", "tIME"}, type], keep = Join[keep, b[[pos ;; pos + 11 + len]]]];
    pos = pos + 12 + len];
  ByteArray[keep]];
clean = stripPNG[bytes];
strm = OpenWrite[out, BinaryFormat -> True];
BinaryWrite[strm, Normal[clean]];
Close[strm];
Print["wrote ", out, ": ", Length[clean], " bytes (", Length[bytes] - Length[clean], " bytes of text/time chunks removed)"];
