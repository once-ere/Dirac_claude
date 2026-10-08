# Revision/notebooks — executed Jupyter notebooks of the Revision record

This folder holds the Jupyter notebooks of the Revision (SPEC section 10, deliverable `notebooks/`).
Each notebook runs Revision code (a Rust program or a Revision verifier), shows what it computes, and
checks what it prints and writes against the committed Revision record. Nothing from the old stages
(`artifacts/`, `provenance/`, `scripts/`, `wolfram/`, the root `notebooks/`) is used.

| notebook | what it computes | provenance |
| --- | --- | --- |
| [`lovelock_gkd.ipynb`](lovelock_gkd.ipynb) | the Lovelock tensors of order k = 1, 2, 3 of the author's metric with the generalized Kronecker delta: builds and runs `Revision/gkd_lovelock/code`, reproduces its four result files byte for byte, re-checks the GKD and three identities exactly in Python, quotes the check counts of the five committed records, three figures | [`lovelock_gkd.PROVENANCE.md`](lovelock_gkd.PROVENANCE.md) |
| [`kohn_sham_states.ipynb`](kohn_sham_states.ipynb) | the Kohn-Sham states of dirac16complex in the deflating field: builds `Revision/kohn_sham/solver` and solves nine canonical states (N = 8, 136, 688 at a4,0 = 0, 1, 2) and one thermal state with `single`; levels, energies, EMT integrals and profiles equal to the committed record, 84 rows of the cross-check against the independent reference reproduced, the check counts of the seven committed Kohn-Sham reports, four figures | [`kohn_sham_states.PROVENANCE.md`](kohn_sham_states.PROVENANCE.md) |
| [`dark_sector_hypotheses.ipynb`](dark_sector_hypotheses.ipynb) | the two dark-sector hypotheses against the Unite values: builds `Revision/kohn_sham/solver` and solves the Kohn-Sham gas on the dense history (N688_lam0, N136_lam0, N8_lamp1, 41 slices each, 123 runs with the arguments of `run_ks_history.py`), every row equal to `ks-history-dense.csv`; recomputes X = P3 - Pt, w_eff(A) = w_eff(B) = X/E, w_eff(C) = X/E - 1, the ratios and derivatives (`eos-history.csv`), CPL tangents and fits, mixtures and the ratio scan (`eos-summary.json`); the condensate (lambda S/m = -382/441 gives -0.764 exactly) and the closed formulas with exact fractions and dual numbers; Hypothesis00: exact M2-M4 tangents and the M5 crossing of w = -1 (ghost-like component); the check counts of the six committed dark-sector reports, four figures; neither hypothesis is established | [`dark_sector_hypotheses.PROVENANCE.md`](dark_sector_hypotheses.PROVENANCE.md) |

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
* Every notebook compiles its Rust program into a build folder OUTSIDE DIR, `<cargo-target>`: the folder
  named by `REVISION_NB_CARGO_TARGET` if it is set, otherwise `revision-nb-<name>-` followed by the first
  12 hexadecimal digits of the sha256 of the path of DIR, in the system's temporary folder (about 3 MB
  per run; nothing deletes it). It is kept short and outside the repository because on Windows the MSVC
  linker `link.exe` cannot open a file whose path is longer than 259 characters (MAX_PATH): with the
  former build folder `DIR/cargo-target` under `build/revision_notebooks/`, `check` failed with
  `LNK1104` when the repository folder was longer than 148 (`lovelock_gkd`), 153
  (`dark_sector_hypotheses`) or 159 (`kohn_sham_states`) characters (each notebook's provenance file,
  section 7). The printed notebook does not depend on where `<cargo-target>` is (checked for
  `lovelock_gkd` with `REVISION_NB_CARGO_TARGET` set: byte-identical).
* On macOS and Linux the default `<cargo-target>` is created private (mode 0700), and the notebook stops
  with an error if a folder of that name already exists and is a symbolic link, belongs to another user
  or can be written by group or others: the name is predictable, a shared temporary folder such as
  `/tmp` can be written by every user, and the notebook runs the program built there. On Windows the
  temporary folder belongs to the user and the folder is used as it is; a folder named by
  `REVISION_NB_CARGO_TARGET` is used as given. The final list of written files of every notebook leaves
  out `<cargo-target>` and an old `DIR/cargo-target` left in a reused output folder by an earlier
  version.
* `Revision/tests/test_revision_notebooks.py` runs the static checks always and re-executes every
  notebook (the `check` command, in a temporary folder) when `REVISION_NOTEBOOKS_FULL=1`.

## Adding a notebook

Write `src/<name>.py` with `NAME`, `TITLE` and `cells()`, keeping the four numbered opening sections
and the final "what this notebook showed / did not show" section; let the notebook find the repository
by searching upwards for `Revision/SPEC.md`, write only into `REVISION_NB_OUT` (or a default under
`build/`), print no path of the computer and no run time (mask them); assert every overlap with a
committed Revision record, naming the record file and check; then `build` twice, `check`, write
`<name>.PROVENANCE.md` and add a row to the table above.
