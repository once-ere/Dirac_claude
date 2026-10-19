#!/usr/bin/env python3
"""The registry file docs_src/symbols/field_equations.json: the symbols that only the derivations of FIELD_EQUATIONS
(version 4) need (keys fe_*).  Writes the file; the atoms must not collide with any other registry file."""
import json
import re
import sys
from pathlib import Path

REPO = Path('/home/claude/dirac_claude/universe_model_2')
sys.path.insert(0, str(REPO / 'tools'))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import symbols_tool as st  # noqa: E402
from build_lib import fmt_units  # noqa: E402
from build import canon  # noqa: E402

REG = {}


def R(key, tex, atoms, meaning, units='', value=None, status=None):
    assert key.startswith('fe_') and key not in REG, key
    e = {'tex': tex, 'atoms': [canon(a) for a in atoms], 'meaning': ' '.join(meaning.split()), 'units': fmt_units(units)}
    if value:
        e['value'] = value
    if status:
        e['status'] = status
    REG[key] = e


# ------------------------------------------------------------------ entries
exec(open(Path(__file__).resolve().parent / 'reg_fe_entries.py').read())


def main():
    others = {}
    for f in sorted((REPO / 'docs_src' / 'symbols').glob('*.json')):
        if f.name == 'field_equations.json':
            continue
        for k, e in json.loads(f.read_text(encoding='utf-8')).items():
            for a in e['atoms']:
                others[a] = (f.name, k)
    bad = 0
    for k, e in REG.items():
        for a in e['atoms']:
            if a in others:
                print('COLLISION: %s (%s) already defined by %s %s' % (a, k, *others[a]))
                bad += 1
    (REPO / 'docs_src' / 'symbols' / 'field_equations.json').write_text(json.dumps(REG, indent=1, ensure_ascii=False) + '\n',
                                                                         encoding='utf-8')
    print('field_equations.json: %d entries, %d collisions' % (len(REG), bad))


if __name__ == '__main__':
    main()
