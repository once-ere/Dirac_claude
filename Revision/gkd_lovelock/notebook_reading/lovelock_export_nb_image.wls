nb = Get[FileNameJoin[{Directory[], "Generalized _Kronecker_Delta_4+4.nb"}]];
cells = Cases[nb, Cell[b_, "Input", opts___] /; MemberQ[{opts}, CellLabel -> "In[101]:="] :> b, Infinity];
img = First[Cases[ToExpression[First[cells], StandardForm, HoldComplete], _Image, Infinity]];
Print[ImageDimensions[img]];
Export[FileNameJoin[{Directory[], "Revision", "gkd_lovelock", "results", "notebook-in68-image.png"}], img];
