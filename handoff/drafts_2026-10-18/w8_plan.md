# W8 plan and state: the textbook "Universes in Pairs" for the corrected metric (version 2 of 2026-10-16)

Started in the cloud session of 2026-10-18 (the PC session's notes `w8/notes.md` were in its scratch and are not
available). The binding rules are `Revision/textbook/TEXTBOOK_SPEC.md` (R2 already states the corrected metric; section 5
the chapter plan for it) and `Revision/textbook/tools/README.md` (the notebook and chapter workflow).

## Environment (Linux, byte-identical with the Windows builds)

- Python 3.14.5 (the version of the Windows builds; `uv python install 3.14.5`), a virtual environment with exactly
  `Revision/textbook/requirements.txt` (`uv pip install --python <venv>/bin/python -r Revision/textbook/requirements.txt`).
- The PNG bytes depend on the zlib of Pillow: run every notebook build or check with a zlib-ng build in compat mode on
  `LD_LIBRARY_PATH` (zlib-ng 2.2.5 or 2.3.3, `cmake -DZLIB_COMPAT=ON`); with it `nbkit check` reproduces notebooks built on
  Windows byte for byte (verified on 01b, 2026-10-18).
- Command form: `LD_LIBRARY_PATH=<zlib-ng build> <venv>/bin/python Revision/textbook/tools/nbkit.py check|build <builder> --scratch <dir>`.

## State found on 2026-10-18 (static survey: builder against stored notebook, provenance current)

- 85 of 91 notebooks match their builders and have current provenance files (static); the dates of their verified
  executions: 2026-10-08 (6), 2026-10-14 (28), 2026-10-15 (27), 2026-10-16 (13), 2026-10-17 (17). The 17 of 2026-10-17
  (01a-01c, 01e-01g, 02a-02d, 03a, 03b, 04a-04d, 05e) were rebuilt for the corrected metric on the PC (W8 had started);
  the others were built for the withdrawn metrics (the metric of 2026-10-14 with the Z2 brane, or its b4 form) or are
  metric-independent.
- 6 do not match: 00b and 00c name the retired records `Revision/theory/reports/{wolfram,python}-field-theory-b4.json`;
  03b, 03d, 04b, 05a have builders changed after their last build (WIP snapshots 0cb4916, dc8f01a, 33912a4 of
  2026-10-17).
- A static match does not mean the notebook reproduces against the current Revision records: `nbkit check` (re-execution)
  decides that (records changed in W1-W6, e.g. `Revision/kohn_sham/results/spectrum/brane-band.csv` now holds the fold
  band of the corrected metric under its old file name).
- The chapter texts are older than the notebooks: chapter 03 still teaches the b4 metric of 2026-10-14 (warps
  sin^(1/6) z on 3-space and the extra times, off-diagonal Einstein components), chapters 14-23 the Z2 brane of the
  metric of 2026-10-14 (counts of "brane" per chapter: 14: 115, 15: 68, 16: 86, 17: 87, 18: 47, 19: 102, 20: 65,
  21: 46, 22: 95, 23: 42), chapter 00 its ledger rows (Z2 mirror, cos z J), chapters 01, 02, 04-13 smaller parts.

## Order of work (each chapter verified, committed and pushed)

1. `nbkit check` of all 91 notebooks (re-execution) to list the dynamically stale ones.
2. Chapters 01 to 13 (mostly examples and walk-throughs to bring to the rebuilt notebooks; chapter 03 rewritten for the
   corrected metric: diagonal Lovelock tensors, no off-diagonal component, the fold).
3. Chapters 14 to 17 (Kohn-Sham in the corrected metric; source: `Revision/docs/KOHN_SHAM_DEFLATING_FIELD.md`,
   `Revision/kohn_sham/ks-theory.json`, reports and results of W5).
4. Chapters 18 to 21 (pairing across the fold, T3 without the mirror statement S5; sources:
   `Revision/docs/PAIR_CREATION_PROOFS.md`, `Revision/pairing/`, `Revision/lead_checks/`).
5. Chapters 22, 23, then 00 (its ledger reads every report) and the abstract.
6. Assembly (`tools/assemble_textbook.py`), the PDF (`scripts/build_provenance_pdf.py ... --developer-layout
   --number-sections-from-zero --wide-page-numbers --specifications Revision/pdf-specifications.json --register`),
   `Revision/tests/test_universes_in_pairs_textbook.py`, the gate rows, README and HANDOFF.

Per chapter: (a) builders: corrected metric, current records, checks; `nbkit lint`; (b) `nbkit build` (two executions,
byte for byte); (c) the chapter text: definitions, derivations line by line, the walk-throughs of every code cell, every
number from the new outputs, status labels; (d) `tools/check_chapter.py <chapter> --scratch <dir>` until
`chapter_check=OK`; (e) commit and push.
