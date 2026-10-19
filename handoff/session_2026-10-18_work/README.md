# Work products of the cloud session of 2026-10-18 (copied from the session scratch folder on 2026-10-18 19:05)

Pushed at the author's order of 19:03 ("pause everything NOW, and push all objects to the repo; verify the repo; then resume
everything"). These are the working sources from which the committed results were made; the committed results themselves
are authoritative (`universe_model_2/*.md` are complete sources: `universe_model_2/tools/symbols_tool.py sync|expand|check`
works on them directly).

- `um2v4/`: the generator of the UM-2 version-4 inventory and registry (`build.py` with `eq_*.py`, `reg_*.py`; `python3 build.py --pdf`
  regenerates `docs_src/equations.json`, `docs_src/symbols/core.json`, the test document and its PDF), `fedoc/` (the generator of
  FIELD_EQUATIONS version 4: `gen.py --build`, sources `src/*.md`), `changed_numbers.md`, `common_prompt.txt`.
- `sol_parts/`, `sol_tools/`: the parts and the assembler of SOLUTION version 4 (`sol_tools/assemble.sh build`).
- `model_v4/`: the parts and the assembler of MODEL version 4 (`tools/assemble.sh`).
- `prov/`: the parts and the assembler of PROVENANCE version 4 (`assemble.py`).
- `ana/` and `fillkeys.py`: the parts and the assembler of ANALYSIS version 4 (`assemble.py`, then `fillkeys.py fill`).
- `sgdoc/`: the draft (`student_guide_v0.md`, with its section parts) of the old Stage-4 student guide (`provenance/DIRAC16COMPLEX_STUDENT_GUIDE`, old static-metric frame).
- `w8/`: the textbook (W8) tools of the lead: `stale_walk.py` (walk-throughs against the stored notebooks), `check_all.sh`
  (nbkit check of every notebook), `check_all.txt` and `check_reasons.txt` (the global check of 2026-10-18 before the rewrites),
  `open_items.md`.
- `verify/`: `run_verify_v4.sh` (the fresh-clone verification of UM-2 version 4), `record_r.py` (records a verification in README,
  PROVENANCE and MANUAL_TASKS; written for version 3).
- `stage4/`: the run scripts of the old Stage-4 jobs (reference rerun of m1_L3_N1016_lamm2_T0, canonical repeat, refined runs;
  killed by the container restart of 16:52; to be restarted).
