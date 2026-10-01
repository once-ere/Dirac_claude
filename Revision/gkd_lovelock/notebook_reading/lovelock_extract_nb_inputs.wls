(* Extract ONLY the input cells of the author's notebook as InputForm text, without evaluating them.
   Output cells are never read or printed. *)
nbPath = FileNameJoin[{Directory[], "Generalized _Kronecker_Delta_4+4.nb"}];
nb = Get[nbPath];
cells = Cases[nb, Cell[b_, "Input", opts___] :> {Quiet[CellLabel /. {opts} /. CellLabel -> "(no label)"], b}, Infinity];
out = OpenWrite[FileNameJoin[{Directory[], "build", "lovelock_nb_inputs.txt"}], CharacterEncoding -> "UTF-8"];
Do[
  {lbl, b} = c;
  txt = Quiet@Check[ToString[ToExpression[b, StandardForm, HoldForm], InputForm], "UNPARSED: " <> ToString[b, InputForm]];
  WriteString[out, "=== ", lbl, "\n", txt, "\n\n"],
  {c, cells}];
Close[out];
Print["input cells written: ", Length[cells]];
