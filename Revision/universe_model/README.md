# Revision/universe_model — UM-1, a 4+4 model of the Universe (order of 2026-10-17)

| file | content |
| --- | --- |
| `MODEL.md`, `MODEL.pdf` | the model (version 1.1): fields, action, the power-series metric, the $x_0$ mass mechanism, the portal interactions, assumptions |
| `PROVENANCE.md`, `PROVENANCE.pdf` | the origin of every ingredient (record, standard physics, new) |
| `FIELD_EQUATIONS.md`, `FIELD_EQUATIONS.pdf` | the coupled field equations, derived by `field_equations/derive_field_equations.py` (13/13 checks) |
| `SOLUTION.md`, `SOLUTION.pdf` | an accurate approximate solution, Kohn-Sham for dirac16complex coupled to all fields (21/21 checks) |
| `solution/vacua.py` | the Einstein-Lovelock vacuum, the effective Newton factor, the block-mode theorem, the slow deflation |
| `solution/masses.py` | the $x_0$ mass spectrum (W, Z, photon, gluon, graviton, e, u, d, $\nu$) and its fit |
| `solution/ks_coupled.py` | the Kohn-Sham solution of dirac16complex with the portal mean fields and the block feedback (record solver, unchanged) |
| `solution/cosmology.py` | CMB ($\theta_*$, $\ell_A$, $\ell_1$), BAO (eBOSS DR16), CNB, $N_{eff}$ |
| `solution/solve_model.py` | assembles the solution, the checks (`solution/reports/`), the figures (`solution/figures/`) and the tables of `SOLUTION.md` |
| `tools/md2tex.py`, `tools/build_pdfs.py` | Markdown → LaTeX → PDF (the .md files are the sources; deterministic output) |

Reproduce the solution (from `Revision/universe_model/solution`, every calculation under `timeout -k 5 423`): the eight
`python ks_coupled.py JOB` runs listed in `SOLUTION.md` section 8, then `python solve_model.py`.
Build the PDFs from the repository root: `python Revision/universe_model/tools/build_pdfs.py`. Gate steps: um1-* in `Revision/verify_revision.{sh,ps1}`.
