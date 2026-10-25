# The author's inputs of the revision UM-3 (read only)

| file | what it is | sha256 |
| --- | --- | --- |
| `4+4.nb` | Patrick L. Nash's Mathematica notebook "eight, real-valued, 16 by 16, Dirac Matrices" (Wolfram 15.0), received on 2026-10-24 from `D:\Developer\github\Dirac_claude\4+4.nb`; copied unchanged, never modified | `7ec1709a0028bce0b443f116cf27b5d3e670de7aa195659a9c3274527270429d` |
| `4+4.nb.cells.txt` | every one of its 806 cells, in order, as linear Wolfram Language text (input, text and heading cells complete; output cells truncated after 2000 characters), written by `../tools/nb_reader.py` without Mathematica | `3a7c295c6d4843ee6b2faa0c1f8f7e90b938de3bee173122ddf114b3015bd526` |

The coordinates of the model are the author's `X = {x0[], x1[], x2[], x3[], x4[], x5[], x6[], x7[]}` of the notebook
`Dirac_Einstein-Lovelock_4+4_Nash.nb` (repository root, Section DEFCHART; `4+4.nb` uses the same list
`X = {x0, x1, x2, x3, x4, x5, x6, x7}`, cell 9: "hidden space", "3-space", "time", "superluminal deflating time").

To regenerate the cell listing:

```text
python universe_model_3/tools/nb_reader.py "universe_model_3/author_inputs/4+4.nb" --dump "universe_model_3/author_inputs/4+4.nb.cells.txt" --max-output 2000
```
