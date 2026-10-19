#!/usr/bin/env python3
"""Build MODEL.md from the parts.

* A line '@@FE-12@@' (or '@@IN-5@@') is replaced by the inventory display: '$$', the exact LaTeX of equations.json, '$$',
  and the marker with the inventory keys.
* A marker '<!-- symbols: AUTO -->' (or 'AUTO + key1, key2') after an untagged display is replaced by the keys that own the
  atoms of the display (in order of appearance), plus the listed extra keys.
* Missing atoms (owned by no registry file) are reported with the part file and line.

usage: fill.py OUT.md PART.md [PART.md ...]
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path('/home/claude/dirac_claude/universe_model_2')
sys.path.insert(0, str(ROOT / 'tools'))
import symbols_tool as st  # noqa: E402

reg, owner, rprob = st.load_registry()
for p in rprob:
    print('REGISTRY PROBLEM:', p)
inv = {e['id']: e for e in json.loads((ROOT / 'docs_src' / 'equations.json').read_text())}

PH = re.compile(r'^@@((?:FE|IN)-\d+)@@\s*$')
AUTO = re.compile(r'^<!-- symbols: AUTO(?:\s*\+\s*(.*?))? -->\s*$')

out = []
missing_total = 0
used = {}
for part in sys.argv[2:]:
    lines = Path(part).read_text(encoding='utf-8').split('\n')
    # first pass: placeholders
    exp = []
    for ln, line in enumerate(lines):
        m = PH.match(line.strip())
        if m:
            e = inv[m.group(1)]
            used[m.group(1)] = used.get(m.group(1), 0) + 1
            exp += ['$$', e['latex'], '$$', '<!-- symbols: %s -->' % ', '.join(e['keys'])]
        else:
            exp.append(line)
    # second pass: AUTO markers
    disp = {end: (start, latex) for start, end, latex in st.displays(exp)}
    res = []
    i = 0
    while i < len(exp):
        line = exp[i]
        m = AUTO.match(line.strip())
        if m:
            # find the display that ends just before (allow one blank line)
            j = len(res) - 1
            while j >= 0 and res[j].strip() == '':
                j -= 1
            # locate display end index in exp coordinates: search backwards in exp
            k = i - 1
            while k >= 0 and exp[k].strip() == '':
                k -= 1
            if k not in disp:
                print('%s:%d AUTO marker without a display' % (part, i + 1))
                res.append(line)
                i += 1
                continue
            latex = disp[k][1]
            keys = []
            miss = []
            for a in st.atoms_of(latex, frozenset(owner)):
                if a in owner:
                    if owner[a] not in keys:
                        keys.append(owner[a])
                elif a not in miss:
                    miss.append(a)
            extra = [x.strip() for x in (m.group(1) or '').split(',') if x.strip()]
            for x in extra:
                if x not in keys:
                    keys.append(x)
            if miss:
                missing_total += len(miss)
                print('%s:%d MISSING atoms: %s   in: %s' % (Path(part).name, disp[k][0] + 1, ', '.join(miss),
                                                           latex.strip().replace('\n', ' ')[:110]))
            res.append('<!-- symbols: %s -->' % ', '.join(keys))
        else:
            res.append(line)
        i += 1
    out += res
Path(sys.argv[1]).write_text('\n'.join(out), encoding='utf-8')
print('written %s: %d lines; inventory displays used: %d distinct (%d in all); missing atoms: %d'
      % (sys.argv[1], len(out), len(used), sum(used.values()), missing_total))
fe = sorted(int(k[3:]) for k in used if k.startswith('FE'))
inn = sorted(int(k[3:]) for k in used if k.startswith('IN'))
print('FE used:', fe)
print('FE not used:', [n for n in range(1, 137) if n not in fe])
print('IN used:', inn, ' IN not used:', [n for n in range(1, 19) if n not in inn])
