#!/usr/bin/env python3
"""Search the UM-2 registry.  Usage:
    python3 regfind.py atom 'x_0'          # which entry owns this atom
    python3 regfind.py grep 'Hubble'       # entries whose key/tex/meaning match the regex (case-insensitive)
    python3 regfind.py latex 'LATEX'       # atoms of a formula with their owners
    python3 regfind.py key KEY [KEY...]    # show entries
"""
import re
import sys
from pathlib import Path

REPO = Path('/home/claude/dirac_claude/universe_model_2')
sys.path.insert(0, str(REPO / 'tools'))
import symbols_tool as st  # noqa: E402

reg, owner, problems = st.load_registry()
src = {}
for f in sorted((REPO / 'docs_src' / 'symbols').glob('*.json')):
    import json
    for k in json.loads(f.read_text(encoding='utf-8')):
        src[k] = f.name
mode = sys.argv[1]
if mode == 'atom':
    for a in sys.argv[2:]:
        k = owner.get(a)
        print(a, '->', k, '(%s)' % src.get(k), reg[k]['meaning'][:200] if k else '')
elif mode == 'grep':
    pat = re.compile(sys.argv[2], re.I)
    for k, e in reg.items():
        if pat.search(k) or pat.search(e['tex']) or pat.search(e['meaning']):
            print('%-28s %-22s %-14s atoms=%s | %s' % (k, src[k], e['tex'], e['atoms'], e['meaning'][:150]))
elif mode == 'latex':
    for a in st.atoms_of(' '.join(sys.argv[2:]), frozenset(owner)):
        k = owner.get(a)
        print('%-30s %-28s %s' % (a, k, (reg[k]['meaning'][:110] if k else 'UNOWNED')))
elif mode == 'key':
    for k in sys.argv[2:]:
        e = reg.get(k)
        print(k, '(%s)' % src.get(k), e)
for p in problems:
    print('REGISTRY PROBLEM:', p)
