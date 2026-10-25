#!/usr/bin/env python3
"""Write the equation inventory docs_src/equations.json from the master document FIELD_EQUATIONS.md: every display
tagged FE-n or IN-n with its LaTeX, the keys of its symbol list, the heading under which it stands, the status stated
in the paragraph that follows it, and the fields it involves (from the headings).  The other UM-3 documents copy these
equations with `symbols_tool.py sync`, so every tagged equation is written identically in every document.

Usage: python universe_model_3/tools/make_inventory.py
"""
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
DOCS = HERE.parent
sys.path.insert(0, str(HERE))
import symbols_tool as ST  # noqa: E402


def main():
    lines = (DOCS / 'FIELD_EQUATIONS.md').read_text(encoding='utf-8').split('\n')
    inv = []
    heading = ''
    heads = {}
    for i, l in enumerate(lines):
        if l.startswith('#'):
            heading = l.lstrip('#').strip()
        heads[i] = heading
    for start, end, latex in ST.displays(lines):
        tag = ST.tag_of(latex)
        if not (tag and re.fullmatch(r'(FE|IN)-\d+', tag)):
            continue
        j, keys = ST.find_marker(lines, end)
        # status: the first 'Status:' of the text after the display (not inside its generated symbol list), before the next
        # display
        status = ''
        k = end + 1
        in_list = False
        while k < len(lines) and not lines[k].strip().startswith('$$'):
            t = lines[k].strip()
            if t == ST.BEGIN:
                in_list = True
            elif t == ST.END:
                in_list = False
            elif not in_list:
                m = re.search(r'Status:\s*([A-Z]+)', lines[k])
                if m:
                    status = m.group(1)
                    break
            k += 1
        inv.append({'id': tag, 'title': heads[start], 'latex': latex.strip('\n'), 'keys': keys or [], 'status': status})
    ids = [e['id'] for e in inv]
    dup = sorted(set(x for x in ids if ids.count(x) > 1))
    if dup:
        raise SystemExit('duplicate tags: %s' % dup)
    (DOCS / 'docs_src' / 'equations.json').write_text(json.dumps(inv, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
    print('%d tagged equations written to docs_src/equations.json' % len(inv))


if __name__ == '__main__':
    main()
