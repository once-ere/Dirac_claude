#!/usr/bin/env python3
"""Helper for writing ANALYSIS.md (version 4): fill the symbol markers of display equations from the registry.

Usage (repository root):
  python3 fillkeys.py fill DOC.md      # markers '<!-- symbols: AUTO -->' (optionally 'AUTO, key1, key2') are replaced
                                         # by the owners of all atoms of the display (keys listed first are kept first);
                                         # displays tagged FE-n / IN-n get the inventory keys (and their LaTeX is compared)
  python3 fillkeys.py missing DOC.md   # list atoms without an owner (to be added to analysis.json)
  python3 fillkeys.py tags DOC.md      # compare every tagged display with the inventory
"""
import importlib.util
import json
import re
import sys
from pathlib import Path

ROOT = Path('/home/claude/dirac_claude')
spec = importlib.util.spec_from_file_location('symtool', ROOT / 'universe_model_2/tools/symbols_tool.py')
st = importlib.util.module_from_spec(spec)
spec.loader.exec_module(st)
INV = ROOT / 'universe_model_2/docs_src/equations.json'


def inventory():
    if not INV.exists():
        return {}
    d = json.loads(INV.read_text(encoding='utf-8'))
    if isinstance(d, dict) and 'equations' in d:
        d = d['equations']
    if isinstance(d, dict):
        d = list(d.values())
    return {e['id']: e for e in d}


def norm(s):
    return re.sub(r'\s+', '', s)


def main():
    cmd, doc = sys.argv[1], Path(sys.argv[2])
    reg, owner, probs = st.load_registry()
    inv = inventory()
    lines = doc.read_text(encoding='utf-8').split('\n')
    names = frozenset(owner)
    missing = {}
    changed = 0
    for start, end, latex in list(st.displays(lines)):
        j, keys = st.find_marker(lines, end)
        tag = st.tag_of(latex)
        ats = st.atoms_of(latex, names)
        if cmd == 'tags' and tag:
            e = inv.get(tag)
            if e is None:
                print('line %d: tag %s not in the inventory' % (start + 1, tag))
            elif norm(e['latex']) != norm(latex):
                print('line %d: %s LaTeX differs from the inventory' % (start + 1, tag))
            if e is not None and keys is not None and keys != e['keys']:
                print('line %d: %s keys differ from the inventory' % (start + 1, tag))
        for a in ats:
            if a not in owner:
                missing.setdefault(a, []).append(start + 1)
        if cmd == 'fill' and j is not None and keys and keys[0] == 'AUTO':
            if tag and tag in inv:
                new = list(inv[tag]['keys'])
            else:
                new = [k for k in keys[1:]]
                for a in ats:
                    k = owner.get(a)
                    if k and k not in new:
                        new.append(k)
            lines[j] = '<!-- symbols: %s -->' % ', '.join(new)
            changed += 1
    if cmd == 'fill':
        doc.write_text('\n'.join(lines), encoding='utf-8')
        print('filled %d markers' % changed)
    if cmd in ('missing', 'fill'):
        for a, ls in sorted(missing.items()):
            print('no owner: %-30s lines %s' % (a, ls[:8]))
    for p in probs:
        print('registry problem:', p)


if __name__ == '__main__':
    main()
