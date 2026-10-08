"""Write the restart continuation scripts into Revision/workflows/restart/ (run from the repository root).

Every script reads finished results from the repository (Revision/workflows/state_restart/state_<family>.json), not
from a session scratchpad, and carries the placeholder SP guard: set SP to the new session's scratchpad before launch.
"""
import json
import os
import re

ROOT = "D:/Developer/github/Dirac_claude"
STATE_DIR = ROOT + "/Revision/workflows/state_restart"
OUT = "Revision/workflows/restart"
PLACE = "<SCRATCHPAD OF THE RUNNING SESSION>"
BS = "\\"
os.makedirs(OUT, exist_ok=True)


def set_sp(s):
    s = re.sub(r"const SP = '[^']*'", f"const SP = '{PLACE}'", s, count=1)
    guard = "if (SP.startsWith('<')) throw new Error('set SP to the scratchpad directory of the running session')\n"
    if guard not in s:
        i = s.index("\n", s.index("const SP = ")) + 1
        s = s[:i] + guard + s[i:]
    return s


def load(fam):
    return json.load(open(f"Revision/workflows/state_restart/state_{fam}.json", encoding="utf-8"))


restart_note = ("RESTART NOTE (2026-10-07 20:30): the work was PAUSED before a session limit; every agent was stopped in the middle "
                "of its task and its partial edits are committed (b89b8b1 and earlier). Finished results of all earlier runs are in "
                f"{STATE_DIR}/state_<family>.json. Inspect, verify and finish partial files; never trust them unchecked.")

# ---------------- textbook ----------------
s = open("Revision/workflows/textbook_universes_in_pairs_cont.js", encoding="utf-8").read()
st = load("textbook")
s = s.replace("CONTINUATION NOTE (2026-10-07 20:10): the previous run (wf_bf3a3e31-ec0) was cut by a session limit; its finished results are in ",
              restart_note + " Textbook results: ", 1)
s = re.sub(r"[A-Za-z]:/Users/[^\s`'\"]*?/scratchpad/state_wf_bf3a3e31-ec0\.json", STATE_DIR + "/state_textbook.json", s)
s = re.sub(r"const NB_DONE = \[[^\]]*\]", "const NB_DONE = " + json.dumps(sorted(k[3:] for k in st if k.startswith("nb:"))), s, count=1)
s = re.sub(r"const WRITE_DONE = \[[^\]]*\]", "const WRITE_DONE = " + json.dumps(sorted(k[6:] for k in st if k.startswith("write:"))), s, count=1)
s = s.replace("name: 'textbook-universes-in-pairs-cont',", "name: 'textbook-universes-in-pairs-restart',", 1)
open(f"{OUT}/textbook_restart.js", "w", encoding="utf-8", newline="\n").write(set_sp(s))

# ---------------- execution provenance ----------------
s = open("Revision/workflows/execution_provenance_cont.js", encoding="utf-8").read()
st = load("execution_provenance")
s = s.replace("CONTINUATION NOTE (2026-10-07 20:10): the previous run (wf_f856ecb5-265) was cut by a session limit; its finished results are in ",
              restart_note + " Execution-provenance results: ", 1)
s = re.sub(r"[A-Za-z]:/Users/[^\s`'\"]*?/scratchpad/state_wf_f856ecb5-265\.json", STATE_DIR + "/state_execution_provenance.json", s)
s = re.sub(r"const RUN_DONE = \[[^\]]*\]", "const RUN_DONE = " + json.dumps(sorted(k[4:] for k in st if k.startswith("run:"))), s, count=1)
s = re.sub(r"const VERIFY_DONE = \{[^}]*\}", "const VERIFY_DONE = " + json.dumps({k[7:]: len(st[k].get("findings", [])) for k in sorted(st) if k.startswith("verify:")}), s, count=1)
s = re.sub(r"const FIX_DONE = \[[^\]]*\]", "const FIX_DONE = " + json.dumps(sorted(k[4:] for k in st if k.startswith("fix:"))), s, count=1)
s = s.replace("name: 'execution-provenance-cont',", "name: 'execution-provenance-restart',", 1)
open(f"{OUT}/execution_provenance_restart.js", "w", encoding="utf-8", newline="\n").write(set_sp(s))

# ---------------- dirac audit fix ----------------
s = open("Revision/workflows/dirac_matrices_audit_fix.js", encoding="utf-8").read()
s = s.replace("${SP}/audit_confirmed.json", STATE_DIR + "/audit_confirmed.json")
s = s.replace("IMPORTANT: an earlier fixer was interrupted by a session limit in the middle of this task;",
              "IMPORTANT: two earlier fixers were interrupted (a session limit, then a pause) in the middle of this task;", 1)
s = s.replace("name: 'dirac-matrices-audit-fix',", "name: 'dirac-matrices-audit-fix-restart',", 1)
open(f"{OUT}/dirac_matrices_audit_fix_restart.js", "w", encoding="utf-8", newline="\n").write(set_sp(s))

# ---------------- wave 1b (continuation) then wave 2 ----------------
s = open("Revision/workflows/revision_wave_1b.js", encoding="utf-8").read()
st = load("wave_1b_2")
s = s.replace("name: 'revision-wave-1b',", "name: 'revision-wave-1b-restart',", 1)
key = "const COMMON = `\n"
i = s.index(key) + len(key)
s = s[:i] + restart_note + " Wave 1b results: " + STATE_DIR + "/state_wave_1b_2.json." + BS + "n" + s[i:]
a = s.index("() => run('ks-mermin-fix'")
b = s.index("\n", s.index("() => run('theory-reconcile'"))
c = s.index("() => agent(`${COMMON}" + BS + "nTASK (wave-1 fix verifier")
d = s.index("\n", c)
ks = st.get("ks-mermin-fix")
w1 = st.get("wave1-fix-verifier")
ks_stub = ("() => ({ files_changed: [], commands_run: [], all_checks_pass: false, failing: ['the pair-creation document still quotes 57 KS-theory checks (now 58): fix in the Fix phase'], "
           "key_results: ['ks-mermin-fix FINISHED in an earlier run: solver 42/42, determinism 14/14, Mermin roots 5/5, KS theory python 58/58, wolfram 46/46, cross-check 29/29; full report under key ks-mermin-fix in "
           + STATE_DIR + "/state_wave_1b_2.json'], open_items: [], summary: 'Mermin mu repaired and verified (see the state file)' }),")
w1_stub = ("() => (" + json.dumps(w1) + "),") if w1 is not None else s[c:d]
s = s[:a] + ks_stub + s[a + len(s[a:b]) - len(s[a:b]):]  # placeholder, replaced below
# rebuild cleanly: replace the ks-mermin-fix line and the verifier line by their stubs
lines = open("Revision/workflows/revision_wave_1b.js", encoding="utf-8").read()
lines = lines.replace("name: 'revision-wave-1b',", "name: 'revision-wave-1b-restart',", 1)
i = lines.index(key) + len(key)
lines = lines[:i] + restart_note + " Wave 1b results: " + STATE_DIR + "/state_wave_1b_2.json." + BS + "n" + lines[i:]
ka = lines.index("  () => run('ks-mermin-fix'")
kb = lines.index("\n", ka)
lines = lines[:ka] + "  " + ks_stub + lines[kb:]
va = lines.index("  () => agent(`${COMMON}" + BS + "nTASK (wave-1 fix verifier")
vb = lines.index("\n", va)
lines = lines[:va] + "  " + w1_stub + lines[vb:]
open(f"{OUT}/revision_wave_1b_restart.js", "w", encoding="utf-8", newline="\n").write(set_sp(lines))

s2 = open("Revision/workflows/revision_wave_2.js", encoding="utf-8").read()
open(f"{OUT}/revision_wave_2.js", "w", encoding="utf-8", newline="\n").write(set_sp(s2))
chain = """export const meta = {
  name: 'revision-wave-1b-restart-then-2',
  description: 'Revision wave 1b continuation (theory reconcile, full KS cross-check, reproduction gate, review, fix) followed automatically by Revision wave 2',
  phases: [
    { title: 'Wave 1b', detail: 'restart/revision_wave_1b_restart.js' },
    { title: 'Wave 2', detail: 'restart/revision_wave_2.js after wave 1b' },
  ],
}
const SP = '<SCRATCHPAD OF THE RUNNING SESSION>'
if (SP.startsWith('<')) throw new Error('set SP to the scratchpad directory of the running session')
phase('Wave 1b')
let w1b = null
try { w1b = await workflow({ scriptPath: SP + '/revision_wave_1b_restart.js' }) } catch (e) { log('wave 1b raised: ' + String(e).slice(0, 500)); w1b = { error: String(e).slice(0, 2000) } }
log('wave 1b finished; starting wave 2')
phase('Wave 2')
let w2 = null
try { w2 = await workflow({ scriptPath: SP + '/revision_wave_2.js' }) } catch (e) { log('wave 2 raised: ' + String(e).slice(0, 500)); w2 = { error: String(e).slice(0, 2000) } }
return { wave1b: w1b, wave2: w2 }
"""
open(f"{OUT}/revision_wave_1b_restart_then_2.js", "w", encoding="utf-8", newline="\n").write(chain)

a4 = open("Revision/workflows/a4_author_gammas_prep.js", encoding="utf-8").read()
open(f"{OUT}/a4_author_gammas_prep.js", "w", encoding="utf-8", newline="\n").write(set_sp(a4))
print(sorted(os.listdir(OUT)))
