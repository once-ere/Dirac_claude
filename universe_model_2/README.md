# universe_model_2 — UM-2, a new 4+4 model of the Universe

Order of the author, 2026-10-17 (evening): a new model of the Universe with Einstein-Lovelock gravity, the
dirac16complex quantized spinor field (the dark-matter hypothesis) coupled to gravity through the canonical spin
connection, photons, neutrinos, electrons, up and down quarks, the W and Z bosons, no Higgs particle; every mass from
wave-function dependence on the hidden space coordinate x0 (period pi/(6H)); a metric general enough for the CMB, the
CNB and BAO; the coupled field equations; an approximate solution with Kohn-Sham theory for dirac16complex coupled to
all fields; the analysis of the x0 mass mechanism and of the dark-matter and dark-energy associations.

Coordinates are the author's, X = {x0, x1, ..., x7}: x0 the hidden space direction, x1, x2, x3 space, x4 the time,
x5, x6, x7 the extra times.

Status (pushed as each verified result is obtained):

| step | content | status |
| --- | --- | --- |
| algebra | the author's Cl(4,4) gamma matrices rebuilt from the author's formulas; Pin(4,4)/Spin(4,4) content; the Kohn-Sham block basis | `code/um2_algebra.py`, 31/31 checks (`reports/algebra-checks.json`) |
| geometry | curvature of the corrected primordial metric, the Lovelock tensors E_(1), E_(2), E_(3) by four independent routes, the background equations with the author's weights, the canonical spin connection | `code/um2_geometry.py`, 25/25 checks (`reports/geometry-checks.json`) |
| model, field equations, solution, analysis | documents MODEL, PROVENANCE, FIELD_EQUATIONS, SOLUTION, ANALYSIS (.md, .tex, .pdf) | in progress |

Reproduce (from this folder; every calculation finishes well inside 423 s):

```
cd code
python um2_algebra.py      # about 50 s
python um2_geometry.py     # about 75 s (needs outputs/algebra.json from the previous line)
```
