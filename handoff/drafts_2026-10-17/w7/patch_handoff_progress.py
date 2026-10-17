"""HANDOFF 0.11: the progress of 2026-10-17 midday (W7 documents and the drafts kept in the session scratch)."""
from pathlib import Path

p = Path(r"D:\Developer\github\Dirac_claude\HANDOFF.md")
s = p.read_text(encoding="utf-8")
old = """  then W7 (documents/PDFs; LOVELOCK_GKD DONE 2026-10-17: rewritten for the corrected metric, 29 pages, registered,
  its publication test 34/34 with the verify-mode rebuild; the comparison report regenerated for the SPEC sha only)
  and W8 (textbook), each committed and pushed.
"""
new = """  then W7 (documents/PDFs; LOVELOCK_GKD DONE 2026-10-17: rewritten for the corrected metric, 29 pages, registered,
  its publication test 34/34 with the verify-mode rebuild; the comparison report regenerated for the SPEC sha only;
  DIRAC16COMPLEX00_FIELD_THEORY DONE 2026-10-17 (f305563): rewritten, 42 pages, registered, test 20/20)
  and W8 (textbook), each committed and pushed.
- Restart material for W6/W7 (2026-10-17 midday; drafts in the session scratch `scratchpad/w7/`, copied to
  `handoff/drafts_2026-10-17/w7/` at each commit): `D16.draft.md` + `fill_d16.py` (DIRAC16COMPLEX_FIELD_THEORY; the
  new test `Revision/tests/test_dirac16complex_field_theory_publication.py` with renderers for the corrected metric,
  its record-only tests pass; still needed: the Kohn-Sham-source paragraph of section 13, the dark-sector verdict of
  section 15 and QUOTED_NUMBERS from the regenerated records), `PAIR.draft.md` + `fill_pair.py` (PAIR_CREATION_PROOFS;
  the test patched for the fold/no-orbifold statements, C1 and the self-test numbers; still needed: the T3
  demonstrations, the Kohn-Sham source paragraph, the run log). The T3 reference demo is placed in the repository
  (N_mid from parameters.json, 1/f, kappa = e^-a4); `verify_t3_completion.wls` and `t3-completion.json` now describe
  T3 as S1-S4 with 9 + 12 checks (the report is byte-identical).
"""
assert s.count(old) == 1
p.write_text(s.replace(old, new), encoding="utf-8", newline="\n")
print("ok")
