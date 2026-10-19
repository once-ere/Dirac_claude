#!/usr/bin/env python3
r"""Helper for writing SOLUTION.md (version 4).

1. Placeholders on a line of their own are replaced by the inventory display
       $$
       <latex of the inventory, with its \tag>
       $$

       <!-- symbols: <the inventory's keys> -->
   Forms:  @@FE-12@@  @@IN-3@@ (ids),  @@name@@ (the inventory writer's internal name, resolved by names.py),
           @@T:title prefix@@ (the unique inventory entry whose title starts with the text).
   Inline references  [[name]]  or  [[T:title prefix]]  anywhere in the text are replaced by the id (FE-n / IN-n).
2. Markers  <!-- symbols: AUTO -->  (after a display) are filled with the registry keys that own the atoms of the display
   (in order of first appearance); extra keys may follow AUTO:  <!-- symbols: AUTO, key1, key2 -->.
3. Report: displays without marker, atoms that no listed key covers (with their owner if any).

Usage: python3 automark.py SRC.md OUT.md
"""
import json
import re
import sys
from pathlib import Path

REPO = Path('/home/claude/dirac_claude/universe_model_2')
sys.path.insert(0, str(REPO / 'tools'))
sys.path.insert(0, str(Path(__file__).resolve().parent))
import symbols_tool as st  # noqa: E402


def main():
    src, out = Path(sys.argv[1]), Path(sys.argv[2])
    reg, owner, problems = st.load_registry()
    for p in problems:
        print('REGISTRY PROBLEM:', p)
    names = frozenset(owner)
    invlist = json.loads((REPO / 'docs_src' / 'equations.json').read_text(encoding='utf-8'))
    inv = {q['id']: q for q in invlist}
    try:
        import names as nm
        nmap, _ = nm.mapping()
    except Exception as exc:  # noqa: BLE001
        print('names.py failed:', exc)
        nmap = {}

    def resolve(tok):
        if re.fullmatch(r'(FE|IN)-\d+', tok):
            return tok
        if tok.startswith('T:'):
            pre = tok[2:]
            ins = [q for q in invlist if q['id'].startswith('IN-')]
            hits = [q['id'] for q in ins if q['title'] == pre] or [q['id'] for q in ins if q['title'].startswith(pre)]
            if len(hits) != 1:
                raise SystemExit('title prefix %r matches %s' % (pre, hits))
            return hits[0]
        if tok in nmap:
            eid, title = nmap[tok]
            if inv[eid]['title'] != title:
                print('WARNING name %s -> %s but titles differ: %r vs %r' % (tok, eid, title, inv[eid]['title']))
            return eid
        raise SystemExit('cannot resolve placeholder %r' % tok)

    text = src.read_text(encoding='utf-8')
    text = re.sub(r'\[\[([^\]]+)\]\]', lambda m: resolve(m.group(1)), text)
    lines = text.split('\n')
    res = []
    used = []
    for ln in lines:
        m = re.fullmatch(r'\s*@@([^@]+)@@\s*', ln)
        if m:
            eid = resolve(m.group(1))
            q = inv[eid]
            used.append(eid)
            res += ['$$', q['latex'], '$$', '', '<!-- symbols: %s -->' % ', '.join(q['keys'])]
            continue
        res.append(ln)
    lines = res
    disp = list(st.displays(lines))
    unknown = {}
    for start, end, latex in disp:
        j, keys = st.find_marker(lines, end)
        if j is None:
            print('NO MARKER line %d: %s' % (start + 1, latex.strip()[:80]))
            continue
        if keys and keys[0] == 'AUTO':
            extra = keys[1:]
            ks = []
            for a in st.atoms_of(latex, names):
                if a in owner:
                    if owner[a] not in ks:
                        ks.append(owner[a])
                else:
                    unknown.setdefault(a, []).append(start + 1)
            for e in extra:
                if e not in ks:
                    ks.append(e)
            lines[j] = '<!-- symbols: %s -->' % ', '.join(ks)
        else:
            covered = set()
            for k in keys:
                if k in reg:
                    covered.update(reg[k]['atoms'])
                else:
                    print('UNKNOWN KEY %s at line %d' % (k, j + 1))
            for a in st.atoms_of(latex, names):
                if a not in covered:
                    unknown.setdefault(a, []).append(start + 1)
    out.write_text('\n'.join(lines), encoding='utf-8')
    for a, where in sorted(unknown.items()):
        print('UNCOVERED atom %-30s owner=%-28s lines %s' % (a, owner.get(a, '-'), where[:8]))
    print('displays: %d; inventory displays: %d (distinct %d)' % (len(disp), len(used), len(set(used))))


if __name__ == '__main__':
    main()
