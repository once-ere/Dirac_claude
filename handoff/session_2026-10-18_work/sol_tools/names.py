#!/usr/bin/env python3
"""Map the inventory writer's internal equation names to the inventory ids (FE-n / IN-n) by replaying the order of the
E() calls of the modules eq_*.py (sorted by file name, as build.py does).  Prints name, id, title; and checks the titles
against equations.json when it exists.  Importable: names.mapping() -> {name: (id, title)}."""
import importlib
import json
import sys
from pathlib import Path

UM = Path('/tmp/claude-0/-home-claude/b01d490e-90a5-59ef-9e41-d6c1af230b6f/scratchpad/um2v4')
REPO = Path('/home/claude/dirac_claude/universe_model_2')


def mapping():
    sys.path.insert(0, str(UM))
    import build_lib
    build_lib.EQS.clear()
    build_lib.REG.clear()
    for p in sorted(UM.glob('eq_*.py')):
        if p.stem in sys.modules:
            importlib.reload(sys.modules[p.stem])
        else:
            importlib.import_module(p.stem)
    counters = {'IN': 0, 'FE': 0}
    out = {}
    order = []
    for q in build_lib.EQS:
        counters[q['kind']] += 1
        eid = '%s-%d' % (q['kind'], counters[q['kind']])
        order.append((eid, q['title'], q['name']))
        if q['name']:
            out[q['name']] = (eid, q['title'])
    return out, order


if __name__ == '__main__':
    m, order = mapping()
    inv = {}
    f = REPO / 'docs_src' / 'equations.json'
    if f.exists():
        inv = {q['id']: q for q in json.loads(f.read_text(encoding='utf-8'))}
    for eid, title, name in order:
        flag = ''
        if inv:
            if eid not in inv:
                flag = '  [NOT IN equations.json]'
            elif inv[eid]['title'] != title:
                flag = '  [TITLE DIFFERS: %s]' % inv[eid]['title']
        print('%-7s %-18s %s%s' % (eid, name or '-', title, flag))
