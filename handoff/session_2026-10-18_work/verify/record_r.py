r"""Record the fresh-clone verification of 815db9e in README, PROVENANCE and MANUAL_TASKS of universe_model_2 (and the root
README).  Reads verify4/times.txt and checks.txt; fails loudly if an expected text is not found exactly once."""
import re
import sys
from pathlib import Path

V = Path("/tmp/claude-0/-home-claude/b01d490e-90a5-59ef-9e41-d6c1af230b6f/scratchpad/verify4")
R = Path("/home/claude/dirac_claude")
U = R / "universe_model_2"
COMMIT = "815db9e"

times = {}
total = None
for line in (V / "times.txt").read_text().splitlines():
    m = re.match(r"(\S+(?: \w+)?) exit=(\d+) ([\d.]+) s$", line)
    if m:
        assert m.group(2) == "0", line
        key = m.group(1).replace("universe_model_2/", "")
        times[key] = float(m.group(3))
    m = re.match(r"TOTAL (\d+) s$", line)
    if m:
        total = int(m.group(1))
assert total is not None and len(times) == 22, (total, len(times))
checks_last = (V / "checks.txt").read_text().splitlines()[-1]
m = re.match(r"TOTAL (\d+) checks, (\d+) failed$", checks_last)
assert m and m.group(1) == "235" and m.group(2) == "0", checks_last
cmp = (V / "compare.txt").read_text()
assert "result: REPRODUCED" in cmp and "compare exit 0" in cmp, cmp[-500:]


def fmt(t):
    if t < 1.5:
        return f"{t:.1f}".rstrip("0").rstrip(".") if t >= 1 else f"{t:.1f}"
    return f"{round(t):d}"


def tt(k):
    return fmt(times[k])


def replace_once(path, old, new):
    text = path.read_text(encoding="utf-8")
    n = text.count(old)
    if n != 1:
        sys.exit(f"{path.name}: expected 1 occurrence, found {n}: {old[:80]!r}")
    path.write_text(text.replace(old, new), encoding="utf-8")


def sub_once(path, pattern, repl):
    text = path.read_text(encoding="utf-8")
    new, n = re.subn(pattern, repl, text, count=0, flags=re.M)
    if n != 1:
        sys.exit(f"{path.name}: pattern matched {n} times: {pattern[:80]!r}")
    path.write_text(new, encoding="utf-8")


rows = {
    "code/um2_algebra.py": "31/31", "code/um2_geometry.py": "25/25", "code/um2_background.py": "22/22",
    "code/um2_fields.py": "16/16", "code/um2_spectra.py": "14/14", "code/um2_flavour.py": "7/7",
    "code/um2_neutrino.py": "16/16", "code/um2_electroweak.py": "19/19", "code/um2_primordial.py": "5/5",
    "code/um2_cosmology.py": "8/8", "code/um2_analysis.py": "23/23", "code/um2_thermal.py": "7/7",
    "code/um2_coupled.py": "16/16", "code/um2_series.py": "4/4",
}
readme = U / "README.md"
for script, chk in rows.items():
    sub_once(readme, r"^\| `" + re.escape(script) + r"` \| " + re.escape(chk) + r" \| [\d.]+ \|$",
             f"| `{script}` | {chk} | {tt(script)} |")
ks = ["validate", "spectrum", "ground8", "ground592", "darkmatter", "portals", "feedback"]
sub_once(readme, r"^(\| `code/um2_ks_jobs\.py validate, spectrum, ground8, ground592, darkmatter, portals, feedback` \| "
         r"2/2, 3/3, 3/3, 4/4, 3/3, 5/5, 2/2 \| )[^|]+\|$",
         r"\g<1>" + ", ".join(tt(f"code/um2_ks_jobs.py {k}") for k in ks) + " |")
sub_once(readme, r"^\| `tools/build_docs\.py` \(all six PDFs\) \| \| [\d.]+ \|$",
         f"| `tools/build_docs.py` (all six PDFs) | | {tt('tools/build_docs.py')} |")
replace_once(readme,
             "Times are those of the verification run of version 3 from a fresh clone of the repository (2026-10-18, commit `726997f`,\n"
             "every computation run as a separate step, 1100 s in all): all 233 checks passed,",
             "Times are those of the verification run of version 3 from a fresh clone of the repository (2026-10-18, commit "
             f"`{COMMIT}`,\nafter the fixes of the independent review; every computation run as a separate step, {total} s in all): "
             "all 235 checks passed,")

prov = U / "PROVENANCE.md"
replace_once(prov,
             "1027 s in all) and version 3 on 2026-10-18 at commit `726997f` (every computation as a separate step, 1100 s in all, the longest\n"
             "the primordial integration with 269 s): every check passed (205 of 205 for version 2, 233 of 233 for version 3) and every stored",
             "1027 s in all) and version 3 on 2026-10-18 at commit `726997f` (every computation as a separate step, 1100 s in all, the longest\n"
             f"the primordial integration with 269 s) and again, after the fixes of its independent review, at commit `{COMMIT}` ({total} s in "
             f"all, the primordial integration {tt('code/um2_primordial.py')} s): every check passed (205 of 205 for version 2, 233 of 233 "
             "for version 3 at `726997f`, 235 of 235 at\n"
             f"`{COMMIT}`) and every stored")
replace_once(prov,
             "of the independent review of version 3 with the record of the fresh-clone verification of `726997f` (item 24; the commit that carries this text).",
             "of the independent review of version 3 with the record of the fresh-clone verification of `726997f` (item 24; `815db9e`), and the "
             f"record of the fresh-clone verification of `{COMMIT}` (the commit that carries this text).")

mt = U / "MANUAL_TASKS.md"
replace_once(mt,
             "* **Task 1, the fresh-clone verification**: all 21 computations of version 3 and the document build took 1100 s\n"
             "  (about 18 minutes) on 2026-10-18 at commit `726997f`, although every individual computation takes at most about\n"
             "  4.5 minutes (the primordial integration, 269 s).",
             f"* **Task 1, the fresh-clone verification**: all 21 computations of version 3 and the document build took {total} s\n"
             f"  (about {round(total / 60)} minutes) on 2026-10-18 at commit `{COMMIT}`, although every individual computation takes at most about\n"
             f"  4.5 minutes (the primordial integration, {tt('code/um2_primordial.py')} s).")
replace_once(mt, "before it; the expected durations are those of the run of 2026-10-18 at commit `726997f`).",
             f"before it; the expected durations are those of the run of 2026-10-18 at commit `{COMMIT}`).")
blocks = [
    ("1", "`run code/um2_algebra.py`", tt("code/um2_algebra.py") + " s", "31"),
    ("2", "`run code/um2_geometry.py`", tt("code/um2_geometry.py") + " s", "25"),
    ("3", "`run code/um2_background.py`", tt("code/um2_background.py") + " s", "22"),
    ("4", "`run code/um2_fields.py`", tt("code/um2_fields.py") + " s", "16"),
    ("5", "`run code/um2_spectra.py`", tt("code/um2_spectra.py") + " s", "14"),
    ("6", "`run code/um2_flavour.py` and `run code/um2_neutrino.py`",
     f"{tt('code/um2_flavour.py')} s, {tt('code/um2_neutrino.py')} s", "7, 16"),
    ("7", "`run code/um2_ks_jobs.py validate` and `run code/um2_ks_jobs.py spectrum`",
     f"{tt('code/um2_ks_jobs.py validate')} s, {tt('code/um2_ks_jobs.py spectrum')} s", "2, 3"),
    ("8", "`run code/um2_ks_jobs.py ground8`", tt("code/um2_ks_jobs.py ground8") + " s", "3"),
    ("9", "`run code/um2_ks_jobs.py ground592`", tt("code/um2_ks_jobs.py ground592") + " s", "4"),
    ("10", "`run code/um2_ks_jobs.py darkmatter`, `run code/um2_ks_jobs.py portals`, `run code/um2_ks_jobs.py feedback`",
     f"{tt('code/um2_ks_jobs.py darkmatter')} s, {tt('code/um2_ks_jobs.py portals')} s, "
     f"{tt('code/um2_ks_jobs.py feedback')} s", "3, 5, 2"),
    ("11", "`run code/um2_electroweak.py`", tt("code/um2_electroweak.py") + " s", "19"),
    ("12", "`run code/um2_primordial.py`", tt("code/um2_primordial.py") + " s", "5"),
    ("13", "`run code/um2_cosmology.py` and `run code/um2_analysis.py`",
     f"{tt('code/um2_cosmology.py')} s, {tt('code/um2_analysis.py')} s", "8, 23"),
    ("14", "`run code/um2_thermal.py`, `run code/um2_coupled.py` and `run code/um2_series.py`",
     f"{tt('code/um2_thermal.py')} s, {tt('code/um2_coupled.py')} s, {tt('code/um2_series.py')} s", "7, 16, 4"),
    ("15", "`run tools/build_docs.py`", tt("tools/build_docs.py") + " s", ""),
]
for b, cmd, t, c in blocks:
    sub_once(mt, r"^\| " + b + r" \| " + re.escape(cmd) + r" \| [^|]+ \| [^|]*\|$", f"| {b} | {cmd} | {t} | {c} |"
             if c else f"| {b} | {cmd} | {t} | |")
replace_once(mt, "Expected result: `result: REPRODUCED`. In the run of 2026-10-18 at commit `726997f` (as in the run of version 2 at `4a6421d`)",
             f"Expected result: `result: REPRODUCED`. In the runs of 2026-10-18 at commits `726997f` and `{COMMIT}` (as in the run of version 2 "
             "at `4a6421d`)")
print("recorded:", COMMIT, total, "s;", checks_last)
for k in sorted(times):
    print(f"  {k}: {times[k]}")
