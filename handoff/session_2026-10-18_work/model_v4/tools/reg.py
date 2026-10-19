#!/usr/bin/env python3
"""Helpers for writing MODEL.md v4 against the symbol registry.

  reg.py inv [FE|IN|ID...]        print inventory entries (id, title, latex, keys)
  reg.py atoms "LATEX"            atoms of a formula with the registry key that owns each (or MISSING)
  reg.py keys "LATEX"             a suggested marker line (keys owning the atoms)
  reg.py find WORD                registry entries whose key/tex/atoms/meaning contain WORD
  reg.py key KEY [KEY...]         print the full registry entries
  reg.py owner ATOM               which key owns an atom
"""
import json
import sys
from pathlib import Path

ROOT = Path('/home/claude/dirac_claude/universe_model_2')
sys.path.insert(0, str(ROOT / 'tools'))
import symbols_tool as st  # noqa: E402


def registry():
    reg, owner, problems = st.load_registry()
    return reg, owner, problems


def inv(args):
    inv = json.loads((ROOT / 'docs_src' / 'equations.json').read_text())
    items = inv if isinstance(inv, list) else inv.get('equations', inv.get('items', []))
    if isinstance(inv, dict) and not items:
        # maybe dict id -> entry
        items = [dict(id=k, **v) for k, v in inv.items() if isinstance(v, dict)]
    for e in items:
        eid = e.get('id', '')
        if args and not any(eid == a or eid.startswith(a + '-') for a in args):
            continue
        print('=' * 100)
        print(eid, '|', e.get('title', ''), '|', e.get('status', ''))
        print('fields:', e.get('fields', ''), '| solved_in:', e.get('solved_in', ''))
        print('LATEX:', e.get('latex', ''))
        print('KEYS:', ', '.join(e.get('keys', [])))
        for k in e:
            if k not in ('id', 'title', 'status', 'fields', 'solved_in', 'latex', 'keys'):
                print('%s: %s' % (k, e[k]))


def atoms(latex):
    reg, owner, _ = registry()
    out = []
    for a in st.atoms_of(latex, frozenset(owner)):
        out.append((a, owner.get(a, 'MISSING')))
    return out


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return
    cmd = sys.argv[1]
    if cmd == 'inv':
        inv(sys.argv[2:])
    elif cmd == 'atoms':
        seen = set()
        for a, k in atoms(' '.join(sys.argv[2:])):
            if a in seen:
                continue
            seen.add(a)
            print('%-28s %s' % (a, k))
    elif cmd == 'keys':
        keys = []
        miss = []
        for a, k in atoms(' '.join(sys.argv[2:])):
            if k == 'MISSING':
                if a not in miss:
                    miss.append(a)
            elif k not in keys:
                keys.append(k)
        print('<!-- symbols: %s -->' % ', '.join(keys))
        if miss:
            print('MISSING atoms:', ', '.join(miss))
    elif cmd == 'find':
        reg, owner, _ = registry()
        w = ' '.join(sys.argv[2:]).lower()
        for k, e in reg.items():
            blob = (k + ' ' + e.get('tex', '') + ' ' + ' '.join(e.get('atoms', [])) + ' ' + e.get('meaning', '')).lower()
            if w in blob:
                print('%-26s %-26s atoms=%s :: %s' % (k, e.get('tex', ''), e.get('atoms', []), e.get('meaning', '')[:150]))
    elif cmd == 'key':
        reg, owner, _ = registry()
        for k in sys.argv[2:]:
            print(k, json.dumps(reg.get(k), indent=1, ensure_ascii=False))
    elif cmd == 'owner':
        reg, owner, _ = registry()
        for a in sys.argv[2:]:
            print(a, owner.get(a, 'MISSING'))
    else:
        print(__doc__)


if __name__ == '__main__':
    main()
