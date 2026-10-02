(* Extract ONLY the input cells of the author's notebook as InputForm text, without evaluating them.
   Output cells are never read or printed.
   Run from the repository root (the notebook 'Generalized _Kronecker_Delta_4+4.nb' sits there):
     wolframscript -file Revision/gkd_lovelock/notebook_reading/lovelock_extract_nb_inputs.wls
   The full text goes to $LOVELOCK_NB_INPUTS if that is set, otherwise to <repository root>/build/lovelock_nb_inputs.txt
   (outside Revision/, not committed: it holds the full InputForm of every input cell, about 9.9 MB).
   The committed digest Revision/gkd_lovelock/results/notebook-input-cells.txt (label, size, first 160 characters of
   each cell) is written from that file by lovelock_digest_nb_inputs.py in this folder. *)
nbPath = FileNameJoin[{Directory[], "Generalized _Kronecker_Delta_4+4.nb"}];
nb = Get[nbPath];
cells = Cases[nb, Cell[b_, "Input", opts___] :> {Quiet[CellLabel /. {opts} /. CellLabel -> "(no label)"], b}, Infinity];
outPath = If[StringQ[Environment["LOVELOCK_NB_INPUTS"]] && Environment["LOVELOCK_NB_INPUTS"] =!= "",
  Environment["LOVELOCK_NB_INPUTS"], FileNameJoin[{Directory[], "build", "lovelock_nb_inputs.txt"}]];
If[! DirectoryQ[DirectoryName[outPath]], CreateDirectory[DirectoryName[outPath]]];
out = OpenWrite[outPath, CharacterEncoding -> "UTF-8"];
Do[
  {lbl, b} = c;
  txt = Quiet@Check[ToString[ToExpression[b, StandardForm, HoldForm], InputForm], "UNPARSED: " <> ToString[b, InputForm]];
  WriteString[out, "=== ", lbl, "\n", txt, "\n\n"],
  {c, cells}];
Close[out];
Print["input cells written: ", Length[cells], " -> ", outPath];
