"""Remove the per-notebook troubleshooting entries that worked around the shared run-instruction text
'(or type `python -m jupyter` instead of `jupyter`)' (fixers of chapters 00, 02, 06, 10, 12, 2026-10-08).

After tools_patch.py fix 1 the SHARED troubleshooting step gives the working commands (`python -m jupyterlab NB`,
`python -m nbconvert --execute --inplace NB`) for every notebook, so the local copies are duplicates.  An entry is removed
when it is an element of FACTS["troubleshooting"] whose command list contains a `python -m jupyterlab` or
`python -m nbconvert` command; nothing else is touched.  The element's exact source span is found with ast.

Usage (repository root):  python Revision/workflows/completion/remove_local_jupyter_workarounds.py [--dry-run] BUILDER...
"""
import ast
import sys

dry = "--dry-run" in sys.argv
builders = [a for a in sys.argv[1:] if a != "--dry-run"]


def offset(lines, lineno, col):
    return sum(len(l) for l in lines[:lineno - 1]) + col


for path in builders:
    src = open(path, encoding="utf-8").read()
    lines = src.splitlines(keepends=True)
    tree = ast.parse(src)
    spans = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign) and any(isinstance(t, ast.Name) and t.id == "FACTS" for t in node.targets) \
                and isinstance(node.value, ast.Dict):
            for k, v in zip(node.value.keys, node.value.values):
                if isinstance(k, ast.Constant) and k.value == "troubleshooting" and isinstance(v, ast.List):
                    for elt in v.elts:
                        seg = ast.get_source_segment(src, elt) or ""
                        try:
                            value = ast.literal_eval(elt)
                        except ValueError:
                            value = None
                        cmds = value[2] if isinstance(value, list) and len(value) == 3 else []
                        if any(c.startswith(("python -m jupyterlab", "python -m nbconvert")) for c in cmds):
                            spans.append((offset(lines, elt.lineno, elt.col_offset),
                                          offset(lines, elt.end_lineno, elt.end_col_offset), seg))
    if not spans:
        print(f"{path}: no local workaround entry")
        continue
    new = src
    for start, end, seg in sorted(spans, reverse=True):
        # extend over the comma that follows the element and the whitespace up to the next element / bracket
        j = end
        while j < len(new) and new[j] in " \t":
            j += 1
        if j < len(new) and new[j] == ",":
            j += 1
        # remove the whole lines when the element starts a line
        i = start
        while i > 0 and new[i - 1] in " \t":
            i -= 1
        if i > 0 and new[i - 1] == "\n" and j < len(new) and new[j] == "\n":
            j += 1
        new = new[:i] + new[j:]
    ast.parse(new)  # still valid Python
    print(f"{path}: removed {len(spans)} entr{'y' if len(spans) == 1 else 'ies'}")
    if not dry:
        open(path, "w", encoding="utf-8", newline="\n").write(new)
