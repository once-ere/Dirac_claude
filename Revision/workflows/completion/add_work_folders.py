"""Declare FACTS["work_folders"] (tools_patch.py fix 2) in the builders that keep raw program output in a git-ignored Rust
target folder, so that the provenance files' 'exactly these files and no other file' stays true.

The folder of each builder is found in its own source (the literal 'Revision/.../target/textbook_<id>' it writes into); the key
is inserted as the last entry of the FACTS dict.  Builders that already declare it are left unchanged.

Usage (repository root, AFTER tools_patch.py):  python Revision/workflows/completion/add_work_folders.py [--dry-run]
"""
import ast
import glob
import re
import sys

dry = "--dry-run" in sys.argv
for path in sorted(glob.glob("Revision/textbook/notebooks/src/[0-9][0-9][a-z]_*.py")):
    src = open(path, encoding="utf-8").read()
    folders = sorted(set(re.findall(r"Revision/[A-Za-z0-9_/]*/target/textbook_[0-9a-z]+", src)))
    if not folders:
        continue
    tree = ast.parse(src)
    facts = next(n.value for n in ast.walk(tree) if isinstance(n, ast.Assign)
                 and any(isinstance(t, ast.Name) and t.id == "FACTS" for t in n.targets) and isinstance(n.value, ast.Dict))
    if any(isinstance(k, ast.Constant) and k.value == "work_folders" for k in facts.keys):
        print(f"{path}: already declares work_folders")
        continue
    lines = src.splitlines(keepends=True)
    close = facts.end_lineno - 1          # the line holding the closing brace of FACTS
    assert lines[close].strip().startswith("}"), (path, lines[close])
    entry = "    \"work_folders\": [" + ", ".join(f"\"{f}\"" for f in folders) + "],\n"
    new = "".join(lines[:close]) + entry + "".join(lines[close:])
    ast.parse(new)
    print(f"{path}: work_folders = {folders}")
    if not dry:
        open(path, "w", encoding="utf-8", newline="\n").write(new)
