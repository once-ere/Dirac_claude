"""Generate the phase-1 completion workflow from the original scripts and the journals (run from the repo root)."""
import json
import os
import re

SP = "C:/Users/nsh/AppData/Local/Temp/claude/D--Developer-github-Dirac-claude/9e0a6725-1ba0-4d61-be26-82d9c70a6ded/scratchpad"
W = "C:/Users/nsh/.claude/projects/D--Developer-github-Dirac-claude/9e0a6725-1ba0-4d61-be26-82d9c70a6ded/subagents/workflows"
ROOT = "D:/Developer/github/Dirac_claude"

w2 = open("Revision/workflows/revision_wave_2.js", encoding="utf-8").read()
w1b = open("Revision/workflows/revision_wave_1b.js", encoding="utf-8").read()
tb = open("Revision/workflows/textbook_universes_in_pairs.js", encoding="utf-8").read()


def template(src, start):
    """The template literal that starts right after `start` in src (backticks; nested ${...} kept as text)."""
    i = src.index(start) + len(start)
    assert src[i] == "`", (start, src[i:i + 20])
    j = i + 1
    depth = 0
    while True:
        c = src[j]
        if c == "\\":
            j += 2
            continue
        if c == "$" and src[j + 1] == "{":
            depth += 1
            j += 2
            continue
        if c == "}" and depth:
            depth -= 1
        elif c == "`" and not depth:
            return src[i + 1:j]
        j += 1


def common(src):
    return template(src, "const COMMON = ")


w2_common = common(w2)
tb_common = common(tb)
tasks = {}
for label in ("dark-sector-dirac16complex", "dark-sector-dirac16complex00", "a4-with-ks-source", "ks-pairing-T3"):
    tasks[label] = template(w2, f"run('{label}', 'Science', ")
xcheck = template(w1b, "run('ks-full-crosscheck', 'Cross-check', ")

# chapter review findings from the journals
res = {}
for wf in os.listdir(W):
    p = os.path.join(W, wf, "journal.jsonl")
    if not os.path.exists(p):
        continue
    labels = {}
    for line in open(p, encoding="utf-8"):
        e = json.loads(line)
        if e.get("type") == "started":
            labels[e["agentId"]] = e.get("label")
        if e.get("type") == "result" and e.get("result") is not None:
            res[labels.get(e["agentId"])] = e["result"]
chapters = ["00", "01", "02", "03", "05", "06", "07", "08", "09", "10", "12", "13"]
findings = {nn: res.get(f"review:{nn}", {}).get("findings", []) for nn in chapters}
os.makedirs(f"{SP}/phase1", exist_ok=True)
for nn in chapters:
    json.dump(findings[nn], open(f"{SP}/phase1/review_{nn}.json", "w", encoding="utf-8"), indent=1)
json.dump(res.get("verify:nb-kohn-sham", {}).get("findings", []), open(f"{SP}/phase1/verify_nb-kohn-sham.json", "w", encoding="utf-8"), indent=1)
json.dump(res.get("verify:rev-a4", {}).get("findings", []), open(f"{SP}/phase1/verify_rev-a4.json", "w", encoding="utf-8"), indent=1)

BOUND = ("BOUNDED TASK (user, 2026-10-08: no hours-long agent jobs): work in small verified steps; after every step append one line to "
         f"{SP}/phase1/<your label>.progress.md (what is done, what is verified, what remains). Aim to finish within about 45 minutes "
         "of work. If the full task cannot be finished in that time, stop at a CONSISTENT, VERIFIED state (every file you leave "
         "must pass its own checks and tests) and list exactly what remains in open_items. Never leave a half-edited file. "
         "Do not commit (the lead commits and pushes). NEVER accept licence terms, source agreements or any other agreement.")
STATE = ("STATE (2026-10-08): the a4 engine now uses the author's T16 from gammas.json (Wolfram 52/52, Python 63/63; a4-equations.json "
         "unchanged; condensate witness S = 51200, 28800, 51200); wave-1b's Mermin repair is done (solver 42/42, determinism 14/14, "
         "KS theory 58/58, cross-check 29/29 on the representative subset); check_field_theory.py reproduces its report (70/70, "
         "comparison agree). Other agents work in parallel on other directories; touch only what you own.")

chapter_titles = dict(re.findall(r"\['(\d\d)', '((?:[^'\\]|\\.)*)', \[", tb))
chapter_titles.update(dict(re.findall(r"\['(\d\d)', \"((?:[^\"\\]|\\.)*)\", \[", tb)))

A4NOTES = {
    "00": "A4 SYNC for this chapter: notebook 00c asserts the Revision/README.md report table against the reports; the a4 counts are now Wolfram 52, sympy 63 (README updated): rebuild 00c and update the chapter-00 totals that quote 00c's sums (around lines 1596 and 3056).",
    "09": "A4 SYNC for this chapter: the a4 record now builds the condensate witnesses in the author's T16: S = 51200, 28800, 51200 (common factor 51200/1.28 = 28800/0.72 = 40000, was 160000); notebook 09c's prose 'its own (equivalent) Clifford representation' is now false. Rebuild 09c and correct chapter 09 (around line 2786).",
    "12": "A4 SYNC for this chapter: the a4 reports now have 52 (Wolfram) and 63 (sympy) checks (chapter 12 around line 757 says 47 and 61); notebooks 12a-12d read the a4 reports: rebuild every one whose stored output changed and correct every quoted count.",
}

js = []
js.append("""export const meta = {
  name: 'completion-phase-1',
  description: 'Completion phase 1: Revision wave-1b full KS cross-check, wave-2 science (dark sector x2, a4 with KS source, T3), the two open provenance records, textbook chapter fixes 00-13 and the review/fix of chapter 11 - small bounded agents',
  phases: [
    { title: 'Revision science', detail: 'KS full cross-check; dark sector dirac16complex and dirac16complex00; a4 with the KS source; T3' },
    { title: 'Provenance', detail: 'rev-a4 record (patched engine); nb-kohn-sham fix' },
    { title: 'Textbook', detail: 'fixers for chapters 00-13; review and fix of chapter 11' },
  ],
}
""")
js.append(f"const ROOT = '{ROOT}'\nconst SP = '{SP}'\nconst R = 'Revision'\nconst T = 'Revision/textbook'\n")
js.append("const W2COMMON = `" + w2_common + "`\n")
js.append("const TBCOMMON = `" + tb_common + "`\n")
js.append("const BOUND = " + json.dumps(BOUND) + "\nconst STATE = " + json.dumps(STATE) + "\n")
js.append("""const RESULT = { type: 'object', properties: { files_changed: { type: 'array', items: { type: 'string' } }, commands_run: { type: 'array', items: { type: 'string' } }, all_checks_pass: { type: 'boolean' }, failing: { type: 'array', items: { type: 'string' } }, key_results: { type: 'array', items: { type: 'string' } }, open_items: { type: 'array', items: { type: 'string' } }, summary: { type: 'string' } }, required: ['files_changed', 'commands_run', 'all_checks_pass', 'failing', 'key_results', 'open_items', 'summary'] }
const FINDINGS = { type: 'object', properties: { findings: { type: 'array', items: { type: 'object', properties: { severity: { type: 'string', enum: ['critical', 'major', 'minor'] }, file: { type: 'string' }, location: { type: 'string' }, problem: { type: 'string' }, evidence: { type: 'string' }, fix: { type: 'string' } }, required: ['severity', 'file', 'location', 'problem', 'evidence', 'fix'] } }, verified_ok: { type: 'array', items: { type: 'string' } } }, required: ['findings', 'verified_ok'] }
const rev = (label, ph, task) => agent(`${W2COMMON}\\n${STATE}\\n${BOUND}\\nTASK (${label}): ${task}`, { label, phase: ph, schema: RESULT })
const tbk = (label, task) => agent(`${TBCOMMON}\\n${STATE}\\n${BOUND}\\nTASK (${label}): ${task}`, { label, phase: 'Textbook', schema: RESULT })
""")
js.append("const XCHECK = `" + xcheck.replace("${JSON.stringify(ksFix).slice(0, 4000)}", "${'the Mermin repair is done and verified: see STATE'}") + "`\n")
for k, v in tasks.items():
    js.append(f"const TASK_{k.replace('-', '_')} = `" + v + "`\n")

chapter_items = []
for nn in chapters:
    title = chapter_titles.get(nn, "")
    note = A4NOTES.get(nn, "")
    chapter_items.append({"nn": nn, "title": title, "note": note, "n": len(findings[nn])})
js.append("const CHAPTERS = " + json.dumps(chapter_items) + "\n")
js.append(r"""
const QUOTES = `QUOTED CODE MUST MATCH THE NOTEBOOKS: run python Revision/textbook/tools/audit/walkthrough_diff.py <chapter.md> <notebook.ipynb> <id> for every notebook of your chapter; it lists quoted blocks that no notebook cell contains (NO MATCH), wrong In [k] headings and unquoted cells. Its section detection can be wrong when the chapter MENTIONS a walk-through before the real heading: check each report by hand. Deliberate conventions that are allowed: captions shortened with a line '...)', docstrings omitted, the generated set-up cell In [1] not quoted. Every other mismatch must be fixed in the chapter (re-quote the notebook's current code and explain every new line).`

const results = await parallel([
  () => rev('ks-full-crosscheck', 'Revision science', XCHECK),
  () => rev('dark-sector-dirac16complex', 'Revision science', TASK_dark_sector_dirac16complex),
  () => rev('dark-sector-dirac16complex00', 'Revision science', TASK_dark_sector_dirac16complex00),
  () => rev('a4-with-ks-source', 'Revision science', TASK_a4_with_ks_source),
  () => rev('ks-pairing-T3', 'Revision science', TASK_ks_pairing_T3),
  () => rev('provenance-rev-a4', 'Provenance', `You own ${R}/field_equations_a4/wolfram/WOLFRAMSCRIPT_PROVENANCE.md, the execution-provenance record of the set rev-a4 (its fix was held until the a4 patch was applied; it now is, commit e377368). Read it fully, the independent verifier's findings in ${SP}/phase1/verify_rev-a4.json, and the patched code. Update the file to the PATCHED set: what it computes (the author's T16 as the primary representation; the comparison basis and the exact intertwiner checks; SPEC section 2 now satisfied), file hashes and line counts, every input incl. gammas.json, outputs with sha256, expected output (checks: 52, failed: 0), the ERROR exits, measured run times and memory, side effects (incl. WolframScript's two tmp_* files in %LOCALAPPDATA%\\Wolfram\\WolframScript\\WolframScriptTemporary and what an interrupted run leaves), complete Windows/macOS/Linux instructions; fix every verifier finding. Any embedded comparison script must use FEGammaFrameComparison (FEGammaFrame is now T16 itself). Verify by following the file LITERALLY in a fresh clone under ${SP}/phase1/reva4/: byte identity of the outputs with the committed files.`),
  () => rev('provenance-nb-kohn-sham', 'Provenance', `You own notebooks/dirac16complex_kohn_sham.PROVENANCE.md (the execution-provenance record of the old Stage-4 Jupyter notebook). Its independent verifier's 9 findings are in ${SP}/phase1/verify_nb-kohn-sham.json: re-verify each in a fresh clone under ${SP}/phase1/nbks/ and fix the confirmed ones in the provenance file (the notebook and its outputs belong to the old Stage 4, which is paused by the user: do NOT change them; record measured truth, incl. the gauntlet's 2 failing checks). One line per finding: FIXED / REJECTED (reason).`),
  ...CHAPTERS.map(c => () => tbk(`fix:${c.nn}`, `You own chapter ${c.nn} (${T}/chapters/${c.nn}-*.md: "${c.title}"), its notebook builders, notebooks, PROVENANCE files and figures (${T}/notebooks/src/${c.nn}*.py, ${T}/notebooks/${c.nn}*, ${T}/figures/${c.nn}*). The chapter's adversarial reviewer found ${c.n} problems; they are in ${SP}/phase1/review_${c.nn}.json (fields severity, file, location, problem, evidence, fix): read ALL of it. Re-verify each finding; fix every confirmed one at the root (rebuild changed notebooks with python ${T}/tools/nbkit.py build <builder> --date 2026-10-08 and check them; keep FACTS (final_lines, files_written) and every count consistent; delete stale figure files); reject unconfirmed ones with evidence. ${c.note} ${QUOTES} Finally test-build the chapter alone with python ${T}/tools/check_chapter.py ${T}/chapters/${c.nn}-*.md until warning-free, and run python ${T}/tools/nbkit.py check on every notebook of the chapter. One line per finding in key_results: FIXED / REJECTED (reason).`)),
  () => agent(`${TBCOMMON}\n${STATE}\n${BOUND}\nTASK (adversarial reviewer of chapter 11; do not edit files): Review chapter ${T}/chapters/11-*.md and its notebooks 11a-11c against TEXTBOOK_SPEC: re-execute each notebook with nbkit check; re-derive the key derivations and check every formula and number against the Revision records it cites; the deep-dive standard (skipped steps, undefined words, unexplained code lines, figures without teaching captions); the run instructions; R2/R3/R5/R6; exercises and answers. ${QUOTES} Report only real problems with concrete evidence.`, { label: 'review:11', phase: 'Textbook', schema: FINDINGS })
    .then(r => (r && r.findings && r.findings.length)
      ? tbk('fix:11', `You own chapter 11 (${T}/chapters/11-*.md), its notebook builders, notebooks and figures. Reviewer findings (JSON): ${JSON.stringify(r.findings).slice(0, 60000)}\nRe-verify each; fix confirmed ones at the root (rebuild notebooks with nbkit and check them; test-build the chapter warning-free with check_chapter.py); reject unconfirmed ones with evidence. One line per finding: FIXED / REJECTED (reason).`)
      : { files_changed: [], commands_run: [], all_checks_pass: true, failing: [], key_results: ['review:11: no findings'], open_items: [], summary: 'chapter 11 reviewed without findings' }),
])
return { results }
""")
open(f"{SP}/phase1/completion_phase_1.js", "w", encoding="utf-8", newline="\n").write("".join(js))
print("written; chapters:", [(c["nn"], c["n"]) for c in chapter_items])
