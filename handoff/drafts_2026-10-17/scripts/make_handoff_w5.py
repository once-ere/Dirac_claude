"""W5: replace the W5 IN PROGRESS entry of HANDOFF.md (0.10) by the W5 DONE entry (scratchpad/handoff_w5_done.md filled
from this session's reports) and keep the W6 preparation as the W6 restart kit; also writes the filled commit message
scratchpad/w5_commit_msg_filled.txt."""
import json
from pathlib import Path

S = Path(__file__).resolve().parent
ROOT = Path(r"D:\Developer\github\Dirac_claude")
H = ROOT / "HANDOFF.md"


def load(p):
    return json.loads((ROOT / p).read_text(encoding="utf-8"))


ref = load("Revision/kohn_sham/reports/ks-reference.json")
cc = load("Revision/kohn_sham/reports/ks-crosscheck.json")
tip = load("Revision/kohn_sham/tip_convergence/tip-convergence.json")
hist = load("Revision/dark_sector/dirac16complex/reports/ks-history-run.json")
kss = load("Revision/field_equations_a4/ks_source/reports/ks-source-a4.json")


def counts(rep):
    s = rep["summary"]
    if "passed" in s:
        return s["passed"], s["total"]
    return s.get("pass", s.get("passed")), s.get("checks", s.get("total"))


for nm, rep in (("ref", ref), ("cc", cc), ("tip", tip), ("hist", hist), ("kss", kss)):
    p, t = counts(rep)
    assert p == t, (nm, p, t)
REF = "%d/%d (stages 1 and 2 in six parts each with the job cache, assembly 4.5 s; H12: the a4 neighbours at NB_TOL = 1e-14)" % counts(ref)
CC = ("%d/%d (the repeat of the reference computed beforehand in two stages of six parts into its own cache, then "
      "byte-identical to the record)" % counts(cc))
TIP = ("%d/%d (scan 6 parts, recal 3 parts, final; 1085 s): the free states are exact fold-band gases independent of L "
       "(except N = 2352 at a4,0 = 0, where k = 0 bulk levels become occupied from L = 3.5); the interacting zero modes "
       "depend on L the more the later the slice (N = 8 at a4,0 = 2: the recorded E_KS is 0.215 of the large-L value); "
       "the calibration rule has no non-trivial limit" % counts(tip))
HIST = "%d/%d (615 runs: 15 series x 41 slices; three parts of 23 s and an assembly of 0.7 s)" % counts(hist)
KSS = ("%d/%d (H13: part D integrates with step-doubling substeps and detects det J -> 0 at 1e-6 of det J(0); the unit "
       "test pins the 19 check names)" % counts(kss))
GATE = ("both twins; patch 1: the Rust matrix, repeat and refined run, the reference and the cross-check's repeat in "
        "parts; patch 2: the tip study (scan 6, recal 3, final) and the dense history (3 parts and the assembly), "
        "budgets from the measured times; `Revision/tests/test_revision_gate.py` 16 tests OK, 1 skipped (the full gate)")

t = (S / "handoff_w5_done.md").read_text(encoding="utf-8")
for a, b in (("@@REF@@", REF), ("@@CC@@", CC), ("@@TIP@@", TIP), ("@@HIST@@", HIST), ("@@KSS@@", KSS), ("@@GATE@@", GATE),
             ("determinism 14/14; the matrix, its repeat and the refined run in parts",
              "determinism 14/14 (the refined run at the SCF tolerance 1e-14 since H15); the matrix, its repeat and the refined\n  run in parts"),
             ("`claude_failures.md` H2-H12 (H11: a part's wall time included a 9-hour system sleep;\n  H12: the reference's a4 neighbours needed the SCF tolerance 1e-14)",
              "`claude_failures.md` H2-H15 (H11: a part's wall time included a 9-hour system sleep;\n  H12: the reference's a4 neighbours needed the SCF tolerance 1e-14; H13: the fixed-step integration of ks_source\n  part D did not resolve the solutions before their events; H14: the cross-check read a changed text of the\n  determinism report; H15: the cross-check failed 3 checks: the SCF stopping error was in neither uncertainty (the\n  Rust refined run now stops at 1e-14, the reference solves every state to 1e-14) and the reference's sea-hole list\n  was shorter than the Rust thermal label sets)")):
    assert t.count(a) == 1, a[:60]
    t = t.replace(a, b)
assert "@@" not in t

doc = H.read_text(encoding="utf-8")
start = doc.index("- W5 IN PROGRESS 2026-10-16 (restart kit; replace by the DONE entry).")
w6 = doc.index("  (9) commit and push W5.  W6 preparation (not durable, session scratch, on disk at", start)
end = doc.index("\n### 0.9 ORDER 2026-10-15 evening", w6)
w6_text = doc[w6 + len("  (9) commit and push W5.  "):end].rstrip("\n")
assert w6_text.startswith("W6 preparation (not durable")
new = (t.rstrip("\n") + "\n- W6 NEXT (restart kit): the dark sector, pairing (T1/T2/Q, T3 and its demos), the notebooks, in the corrected\n"
       "  metric.  " + w6_text + "\n"
       "  (e) Drafts of 2026-10-17 in the scratch folder (patch scripts `w6/patch_*.py`, patched copies; NOT yet run unless\n"
       "  stated): pairing T1/T2/Q (`w6/pairing/python/check_pairing.py`, `w6/pairing/wolfram/verify_pairing.wls` and\n"
       "  `RevisionPairing.wl`: the corrected vielbein, sqrt|g| = e^{-a4} b4^2 cot z sin^{1/2} z, the fold instead of the Z2\n"
       "  brane, the not-established tokens 'across the fold' and 'degenerate' in both lists); `Revision/SPEC.md` section 9\n"
       "  (`w6/spec9_draft.md`); the T3 demos (`w6/t3demo/`: key e3Hy, Vol_7 e^{(5/3) a4}, N_mid read from parameters.json);\n"
       "  check_t3_completion with the zero mode (e^{f M y}, 0); the dirac16complex00 tests (`w6/d00/tests/`); compute_eos\n"
       "  13/13 and independent_free_gas 10/10 on the new dense history (the latter after a fix: the collocation leaves a\n"
       "  spurious partner of the fold-band mode in a degenerate eigenspace).  RUN-TIME RISK: the gate row t3-rust-demo\n"
       "  (3 members x 210 states of the new matrix) will exceed 423 s and must be split into parts before it is run.\n")
doc = doc[:start] + new + doc[end:]
H.write_bytes(doc.encode("utf-8"))

m = (S / "w5_commit_msg.txt").read_text(encoding="utf-8")
for a, b in (("@@REF@@", REF), ("@@CC@@", CC), ("@@TIP@@", TIP), ("@@HIST@@", HIST), ("@@KSS@@", KSS),
             ("@@GT@@", "16 tests OK (1 skipped: the full gate)"),
             ("claude_failures.md H2-H12;", "claude_failures.md H2-H15;")):
    assert m.count(a) == 1, a
    m = m.replace(a, b)
assert "@@" not in m
(S / "w5_commit_msg_filled.txt").write_text(m, encoding="utf-8", newline="\n")
print("ok")
