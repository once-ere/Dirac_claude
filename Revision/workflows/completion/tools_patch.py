"""Phase 2c tool fixes for the textbook (run from the repo root, AFTER every textbook agent has finished).

1. run_instructions.py: the generic troubleshooting item for "jupyter is not recognized" offered
   `python -m jupyter`, which fails when the jupyter-* programs are not on PATH (measured by the fixers of
   chapters 00, 01, 02, 06, 07, 08, 10).  New item: do Step 4; otherwise start the two programs through
   Python itself (`python -m jupyterlab NB`, `python -m nbconvert --execute --inplace NB`; --inplace sets
   the notebook exporter in nbconvert 7).
2. run_instructions.py + nbkit.py: an optional FACTS key `work_folders` (folders inside a git-ignored Rust
   `target` folder where a notebook keeps the raw output of its program runs), printed in the run
   instructions and in section 4.1 of the provenance file, so that "exactly these files and no other file"
   stays true (finding of the chapter-15 fixer: 15a, 15b, 15d write into Revision/kohn_sham/solver/target/).
3. nbkit.py: the scanner that collects the PASS/RESULT lines (and their indented continuation lines, e.g. "reproduces
   <record> / check <name>") for the provenance file reset its state at the start of every stdout OUTPUT CHUNK.  How the
   kernel splits stdout into chunks depends on timing, so a continuation line that landed in the next chunk was dropped:
   the stored notebook (normalised: chunks merged) compared equal while the regenerated provenance differed from run to
   run (found 2026-10-08 in a fresh clone: 04b, In [12]).  The scanner now reads the normalised outputs, i.e. exactly what
   the stored notebook holds.  Every provenance file must then be regenerated (the bulk rebuild does it).
"""
import re

RI = "Revision/textbook/tools/run_instructions.py"
NK = "Revision/textbook/tools/nbkit.py"


def edit(path, pairs):
    s = open(path, encoding="utf-8").read()
    for a, b in pairs:
        assert s.count(a) == 1, (path, a[:90], s.count(a))
        s = s.replace(a, b)
    open(path, "w", encoding="utf-8", newline="\n").write(s)
    print("edited", path)


edit(RI, [
    ('        ("\\"jupyter is not recognized\\" or \\"command not found: jupyter\\": the "\n'
     '         "environment is not active; do Step 4 (or type `python -m jupyter` instead of "\n'
     '         "`jupyter`).", []),\n',
     '        ("\\"jupyter is not recognized\\" or \\"command not found: jupyter\\": the "\n'
     '         "environment is not active; do Step 4. If the environment is active and the "\n'
     '         "message stays, the programs jupyter-lab and jupyter-nbconvert are not in the "\n'
     '         "folders where the terminal looks for programs (`python -m jupyter` does not "\n'
     '         "help then: it has to find the same programs). Start them through Python "\n'
     '         "itself, in the folder of the notebook: the first command below does what "\n'
     '         "`jupyter lab` does, the second what the headless command does:",\n'
     '         [f"python -m jupyterlab {nb_name}",\n'
     '          f"python -m nbconvert --execute --inplace {nb_name}"]),\n'),
    ('    "network": "optional str: what the notebook downloads while it runs (default: "\n'
     '               "nothing)",\n}',
     '    "network": "optional str: what the notebook downloads while it runs (default: "\n'
     '               "nothing)",\n'
     '    "work_folders": "optional list of repository-relative folders inside a git-ignored "\n'
     '                    "Rust build folder (a path containing /target/) where the notebook "\n'
     '                    "keeps the raw output of its program runs (default: none)",\n}'),
    ('OPTIONAL_KEYS = {"allow_stderr": bool, "network": str}',
     'OPTIONAL_KEYS = {"allow_stderr": bool, "network": str, "work_folders": list}'),
])

s = open(RI, encoding="utf-8").read()
# validation of work_folders, right after the OPTIONAL_KEYS type loop
anchor = ('    for key, kind in OPTIONAL_KEYS.items():\n'
          '        if key in facts and not isinstance(facts[key], kind):\n'
          '            problems.append(f"FACTS[{key!r}] must be of type {kind}")\n')
assert s.count(anchor) == 1
s = s.replace(anchor, anchor +
              '    for folder in facts.get("work_folders", []) if isinstance(facts.get("work_folders"), list) else []:\n'
              '        if not isinstance(folder, str) or "/target/" not in folder or folder.startswith("/"):\n'
              '            problems.append(f"FACTS[\'work_folders\']: {folder!r} must be a repository-relative "\n'
              '                            "folder inside a Rust build folder target (git-ignored)")\n')
# the side-effect sentence of the run instructions
old = ('        "It changes no other file of the repository"\n'
       '        + (" except the Rust build folder `target` next to each `Cargo.toml` it "\n'
       '           "builds" if rust else "")\n')
assert s.count(old) == 1, "side-effect sentence"
s = s.replace(old,
              '        "It changes no other file of the repository"\n'
              '        + (" except the Rust build folder `target` next to each `Cargo.toml` it "\n'
              '           "builds" if rust else "")\n'
              '        + ("" if not facts.get("work_folders") else\n'
              '           " (inside it the notebook keeps the raw output of its program runs in "\n'
              '           + _join([f"`{f}`" for f in facts["work_folders"]]) + ", which git ignores)")\n')
open(RI, "w", encoding="utf-8", newline="\n").write(s)
print("edited", RI, "(validation, side effects)")

edit(NK, [
    ('    add("Running the notebook headless with `--inplace`, or saving it in JupyterLab, "\n',
     '    if facts.get("work_folders"):\n'
     '        add("Besides these files the notebook writes only the raw output of its program runs, "\n'
     '            "below " + ", ".join(f"`{f}`" for f in facts["work_folders"]) + " (inside the Rust "\n'
     '            "build folder `target`, which git ignores; section 4.2).")\n'
     '        add("")\n'
     '    add("Running the notebook headless with `--inplace`, or saving it in JupyterLab, "\n'),
])

edit(NK, [
    ('        for output in cell.get("outputs", []):\n            kind = output["output_type"]\n',
     '        # The normalised outputs (consecutive stream chunks merged) are what the stored notebook holds; scanning\n'
     '        # the raw chunks made the collected PASS continuation lines depend on how the kernel split stdout.\n'
     '        for output in normalise_outputs(cell.get("outputs", [])):\n            kind = output["output_type"]\n'),
])
