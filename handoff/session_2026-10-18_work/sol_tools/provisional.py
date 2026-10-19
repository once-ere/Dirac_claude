#!/usr/bin/env python3
"""Check the atoms of the display equations of the SOLUTION draft parts against a provisional registry built in memory from
the inventory writer's reg_*.py modules (nothing is written to the repository).  Usage: python3 provisional.py PART.md ..."""
import importlib
import sys
from pathlib import Path

UM = Path('/tmp/claude-0/-home-claude/b01d490e-90a5-59ef-9e41-d6c1af230b6f/scratchpad/um2v4')
REPO = Path('/home/claude/dirac_claude/universe_model_2')
sys.path.insert(0, str(UM))
sys.path.insert(0, str(REPO / 'tools'))
import symbols_tool as st  # noqa: E402
import build_lib  # noqa: E402

for p in sorted(UM.glob('reg_*.py')):
    importlib.import_module(p.stem)
import build as umbuild  # noqa: E402  (the inventory writer's canonicalisation of atoms)
REG = build_lib.REG
for e in REG.values():
    e['atoms'] = [umbuild.canon(a) for a in e['atoms']]
owner = {}
for k, e in REG.items():
    for a in e['atoms']:
        owner.setdefault(a, k)
names = frozenset(owner)
print('provisional registry entries:', len(REG))
for f in sys.argv[1:]:
    lines = Path(f).read_text(encoding='utf-8').split('\n')
    for start, end, latex in st.displays(lines):
        ats = st.atoms_of(latex, names)
        unk = [a for a in dict.fromkeys(ats) if a not in owner]
        own = [(a, owner[a]) for a in dict.fromkeys(ats) if a in owner]
        print('%s:%d  UNOWNED: %s' % (Path(f).name, start + 1, ', '.join(unk) or '-'))
        if '-v' in sys.argv[0:1]:
            print('    owned:', own)
