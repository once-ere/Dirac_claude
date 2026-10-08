# Revision/notebooks — executed Jupyter notebooks of the Revision record

This folder holds the Jupyter notebooks of the Revision (SPEC section 10, deliverable `notebooks/`).
Each notebook runs Revision code (a Rust program or a Revision verifier), shows what it computes, and
checks what it prints and writes against the committed Revision record. Nothing from the old stages
(`artifacts/`, `provenance/`, `scripts/`, `wolfram/`, the root `notebooks/`) is used.

| notebook | what it computes | provenance |
| --- | --- | --- |
| [`lovelock_gkd.ipynb`](lovelock_gkd.ipynb) | the Lovelock tensors of order k = 1, 2, 3 of the author's metric with the generalized Kronecker delta: builds and runs `Revision/gkd_lovelock/code`, reproduces its four result files byte for byte, re-checks the GKD and three identities exactly in Python, quotes the check counts of the five committed records, three figures | [`lovelock_gkd.PROVENANCE.md`](lovelock_gkd.PROVENANCE.md) |
| [`kohn_sham_states.ipynb`](kohn_sham_states.ipynb) | the Kohn-Sham states of dirac16complex in the deflating field: builds `Revision/kohn_sham/solver` and solves nine canonical states (N = 8, 136, 688 at a4,0 = 0, 1, 2) and one thermal state with `single`; levels, energies, EMT integrals and profiles equal to the committed record, 84 rows of the cross-check against the independent reference reproduced, the check counts of the seven committed Kohn-Sham reports, four figures | [`kohn_sham_states.PROVENANCE.md`](kohn_sham_states.PROVENANCE.md) |

## Layout

* `<name>.ipynb` — the executed, committed notebook (normalised: fixed cell ids, no timing metadata,
  sorted keys, LF line ends; two executions on the same computer are byte-identical).
* `<name>.PROVENANCE.md` — what the notebook computes, the files it reads and writes with sha256,
  complete run instructions, expected output, measured run time, side effects, verification record.
* `src/<name>.py` — the deterministic BUILDER: it defines `NAME`, `TITLE` and `cells()` (the markdown and
  code cells as fixed strings). The notebook is never edited by hand; edit the builder and rebuild.
* `tools/build_notebooks.py` — build, check and audit tool shared by every Revision notebook.
* `requirements.txt` — the pinned Python packages (Python 3.12 or newer; built with 3.14.5).

## Commands (from the repository root, with the Python of a private environment, see section 2 of each notebook)

`<name>` is the name of a notebook of the table above without `.ipynb`, for example `lovelock_gkd`.

```text
python Revision/notebooks/tools/build_notebooks.py list
python Revision/notebooks/tools/build_notebooks.py build <name> [--out DIR]
python Revision/notebooks/tools/build_notebooks.py check <name> [--out DIR]
python Revision/notebooks/tools/build_notebooks.py audit <name>
python -m unittest Revision/tests/test_revision_notebooks.py -v
```

* `build` executes the notebook with nbclient (kernel `python3`, working folder `Revision/notebooks`)
  with every output file in DIR (default: a new folder under `build/revision_notebooks/`, which git
  ignores), normalises it and writes `Revision/notebooks/<name>.ipynb`; then it audits the result.
* `check` executes it again in a fresh folder, writes the executed notebook there and compares it byte
  for byte with the committed one (exit status 0 only when identical).
* `audit` checks the structure rules without executing: normalised form, LF only, the sections
  1 (what it computes), 2 (how to run it, for Windows 11, macOS on Apple silicon and Linux), 3 (the
  words used), 4 (the physical and mathematical situation) and a final "what this notebook showed"
  section, a markdown lead-in of at least 80 characters before every code cell, every code cell
  executed without error and without stderr, no `-m jupyter` command (it fails where the jupyter
  executables are not on PATH; the notebooks use `-m jupyterlab` and `-m nbconvert`), no
  machine-specific path.
* The tool never deletes: the output folder must not exist or be empty. The kernel receives
  `REVISION_NB_OUT=DIR` and `PYTHONHASHSEED=0`; `REVISION_NB_LONG` is removed, so the committed notebook
  is always the normal run.
* `Revision/tests/test_revision_notebooks.py` runs the static checks always and re-executes every
  notebook (the `check` command, in a temporary folder) when `REVISION_NOTEBOOKS_FULL=1`.

## Adding a notebook

Write `src/<name>.py` with `NAME`, `TITLE` and `cells()`, keeping the four numbered opening sections
and the final "what this notebook showed / did not show" section; let the notebook find the repository
by searching upwards for `Revision/SPEC.md`, write only into `REVISION_NB_OUT` (or a default under
`build/`), print no path of the computer and no run time (mask them); assert every overlap with a
committed Revision record, naming the record file and check; then `build` twice, `check`, write
`<name>.PROVENANCE.md` and add a row to the table above.
