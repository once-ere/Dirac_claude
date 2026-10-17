# Drafts and scripts of 2026-10-17 (restart material, not part of the record)

Saved at the author's stop order of 2026-10-17 (~07:52 PDT) so that the work survives the session; see `HANDOFF.md`
section 0.10, the entry "W5 STATE AT THE STOP OF 2026-10-17".

* `scripts/`: the H15 rerun (`run_h15.sh`: every Kohn-Sham step in order under `timeout -k 5 423`, the same commands as
  the gate rows; `same_tree.py`), the README and gate updaters that fill the numbers of that rerun
  (`patch_solver_readme_h15.py`, `patch_ref_readme_h15.py`, `patch_ref_timings_h15.py`, `patch_tip_readme_h15.py`,
  `patch_gate_budgets_h15.py`, `make_checker_readme.py` with `checker_readme_draft.md` and
  `checker_corrected_section.md`), the HANDOFF and commit-message drafts of W5 DONE, and the diagnostics of H15
  (`diag_scf_main.py`, `diag_ref_grids.py`, `diag_ref_thermal.py`, `patch_diag_tols.py`).  The scripts contain the path
  of the session's scratch folder; adjust `S=` before use.  `patch_ref_h15.py` is ALREADY APPLIED (its changes are
  committed).
* `w6/` and `w6_notes.md`: the W6 drafts (dark sector `derive_effective.py` 37/37, `compute_eos.py` 13/13,
  `independent_free_gas.py` 10/10 on the new dense history, `verify_dark_sector.wls` 7/7; dirac16complex00 A 48/48, B
  32/32 and its tests; pairing T1/T2/Q for the corrected vielbein (`pairing/`, not run); T3 (`t3/`, `t3w/`), the T3
  demos (`t3demo/`); the patch scripts `patch_*.py`), with the hand derivations and the findings in `w6_notes.md`.
