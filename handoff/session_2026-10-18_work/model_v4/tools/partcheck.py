#!/usr/bin/env python3
"""Check one part file (or several) without touching MODEL.md: every display must have a marker; every atom of every
display must be defined by the listed keys; every key must exist.  Prints the problems with line numbers.

usage: partcheck.py PART.md [PART.md ...]
"""
import sys
from pathlib import Path

sys.path.insert(0, '/home/claude/dirac_claude/universe_model_2/tools')
import symbols_tool as st  # noqa: E402

reg, owner, rprob = st.load_registry()
for p in rprob:
    print('REGISTRY:', p)
total = 0
nprob = 0
for name in sys.argv[1:]:
    lines = Path(name).read_text(encoding='utf-8').split('\n')
    for start, end, latex in st.displays(lines):
        total += 1
        j, keys = st.find_marker(lines, end)
        where = '%s:%d' % (Path(name).name, start + 1)
        if keys is None:
            print(where, 'NO MARKER:', latex.strip()[:100])
            nprob += 1
            continue
        unknown = [k for k in keys if k not in reg]
        if unknown:
            print(where, 'UNKNOWN KEYS:', unknown)
            nprob += 1
        covered = set()
        for k in keys:
            if k in reg:
                covered.update(reg[k]['atoms'])
        need = []
        for a in st.atoms_of(latex, frozenset(owner)):
            if a not in covered and a not in need:
                need.append(a)
        if need:
            print(where, 'MISSING ATOMS:', ', '.join('%s (%s)' % (a, owner.get(a, '-')) for a in need))
            nprob += 1
        # unused keys (listed but no atom of theirs appears): informative only
        present = set(st.atoms_of(latex, frozenset(owner)))
        unused = [k for k in keys if k in reg and not (set(reg[k]['atoms']) & present)]
        if unused:
            print(where, 'unused keys (info):', unused)
print('displays: %d, problems: %d' % (total, nprob))
