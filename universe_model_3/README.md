# universe_model_3 — UM-3, the revision of 2026-10-24

The author's order of 2026-10-24 ("This is a major new revision of this project") stopped every earlier stage
permanently (repository `HANDOFF.md`, section 0.14) and asked for a new folder holding all files of the revision. This
folder is that revision. Nothing in it refers to, or depends on, the earlier records (`Revision/`, `universe_model_2/`,
`provenance/`); its documents are self-contained.

## The author's specification (2026-10-24)

* **Coordinates** (author, `Dirac_Einstein-Lovelock_4+4_Nash.nb`, Section DEFCHART):
  `X = {x0[], x1[], x2[], x3[], x4[], x5[], x6[], x7[]}` — `x0` the hidden space-like direction, `x1, x2, x3` ordinary
  space, `x4` the time, `x5, x6, x7` the three extra (deflating) time-like directions. Never relabelled.
* **Dirac matrices** (author, `author_inputs/4+4.nb`): eight real 16 x 16 matrices `T16^A[0..7]` with
  `{T16^A[a], T16^A[b]} = 2 eta_ab I16`, `eta = diag(+1,+1,+1,+1,-1,-1,-1,-1)`; chirality `T16^A[8]`, projectors
  `P_L = (I16 - T16^A[8])/2`, `P_R = (I16 + T16^A[8])/2`. Provenance: `dirac matrices.md` (also `.tex`, `.pdf`).
* **Metric of the primordial gravitational field** (author, new: `b4[x4] -> b4[x4]^2`; `b4` is a function of `x4`,
  never identically 1):

  ```text
  {{Cot[6 H x0]^2, 0, 0, 0, 0, 0, 0, 0},
   {0, E^(2 a4[x4]) Sin[6 H x0]^(1/3), 0, 0, 0, 0, 0, 0},
   {0, 0, E^(2 a4[x4]) Sin[6 H x0]^(1/3), 0, 0, 0, 0, 0},
   {0, 0, 0, E^(2 a4[x4]) Sin[6 H x0]^(1/3), 0, 0, 0, 0},
   {0, 0, 0, 0, -1, 0, 0, 0},
   {0, 0, 0, 0, 0, -E^(-2 a4[x4]) b4[x4]^2 Sin[6 H x0]^(1/3), 0, 0},
   {0, 0, 0, 0, 0, 0, -E^(-2 a4[x4]) b4[x4]^2 Sin[6 H x0]^(1/3), 0},
   {0, 0, 0, 0, 0, 0, 0, -E^(-2 a4[x4]) b4[x4]^2 Sin[6 H x0]^(1/3)}}
  ```

  with `Sin[6 H x0]^(1/3) = (Sin[6 H x0]^2)^(1/6)`, the positive branch (the author's rule of 2026-10-16).
* **Fields**: Einstein-Lovelock gravity (couples to all fields); the Higgs doublet `Phi` with
  `V = mu^2 Phi^dagger Phi + lambda (Phi^dagger Phi)^2`, `lambda > 0`, `mu^2 < 0`, expanded about the ad hoc vacuum
  `Phi = (almightyAdHoc, v + h)/sqrt 2`, `almightyAdHoc = Exp[-2 a40 x4]`, `a40 > 0`, `x4 >= 0`; the three
  left-handed lepton doublets and the right-handed electron, muon and tau; the gauge fields `W1, W2, W3` of `SU(2)_L` and
  `B` of `U(1)_Y`; the three generations of quark doublets; the gluons of `SU(3)_C`; the dirac16complex quantised spinor
  field, coupled to gravity through the canonical spin connection (never identically zero) and, with its left-handed
  and its right-handed part separately, to every Standard-Model field with a unique coupling parameter each (only the
  left-handed part couples to the Higgs field); new phenomenological interactions consistent with QCD and the
  electroweak model.
* **Tasks**: the complete coupled field equations; an accurate approximate solution with Kohn-Sham theory for
  dirac16complex; CMB, CNB, BAO (the metric as a power series of terms of decreasing magnitude); the `x0` mass mechanism
  (period `pi/(6H)`, the uncertainty relation) and the association of dark matter and dark energy with dirac16complex
  analysed; every equation written out and every symbol defined in every document; Markdown + LaTeX + PDF always.

## Status (newest last)

| part | files | state |
| --- | --- | --- |
| author inputs | `author_inputs/` | DONE: `4+4.nb` (read only, sha256 in `author_inputs/README.md`) and its cell listing |
| notebook reader | `tools/nb_reader.py` | DONE: reads every cell of a `.nb` file without Mathematica |
| Dirac matrices provenance | `dirac matrices.md/.tex/.pdf` | in progress |
| gravity sector of the new metric | `code/` | open |
| coupled field equations | `FIELD_EQUATIONS`, `MODEL` | open |
| Kohn-Sham approximate solution | `SOLUTION` | open |
| analysis and provenance | `ANALYSIS`, `PROVENANCE` | open |
| verification from a fresh clone | | open |
