#!/usr/bin/env python3
"""Generate universe_model_2/FIELD_EQUATIONS.md (version 4) from the prose sources in src/*.md, the inventory
docs_src/equations.json and the registry docs_src/symbols/*.json; then run the symbols tool (expand, check).

Source syntax (line based):
  @FE-12 / @IN-3        the inventory display of that equation (with its tag) and its symbol marker
  @@                    a line '@@' opens and a line '@@' closes an extra display (derivation step); its symbol marker is
                        computed from the registry (every atom must be registered)
  everything else       copied verbatim
Usage: python3 gen.py [--build]
"""
import json
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = Path('/home/claude/dirac_claude/universe_model_2')
sys.path.insert(0, str(REPO / 'tools'))
import symbols_tool as st  # noqa: E402

FEJSON = REPO / 'docs_src' / 'symbols' / 'field_equations.json'


def load_registry():
    reg = {}
    for f in sorted((REPO / 'docs_src' / 'symbols').glob('*.json')):
        reg.update(json.loads(f.read_text(encoding='utf-8')))
    owner = {}
    for k, e in reg.items():
        for a in e['atoms']:
            owner.setdefault(a, k)
    return reg, owner


def keys_of(latex, owner, where):
    names = frozenset(owner)
    keys, unknown = [], []
    for a in st.atoms_of(latex, names):
        if a in owner:
            if owner[a] not in keys:
                keys.append(owner[a])
        elif a not in unknown:
            unknown.append(a)
    if unknown:
        print('UNKNOWN atoms in %s: %s' % (where, ', '.join(unknown)))
    return keys


def main():
    eqs = {q['id']: q for q in json.loads((REPO / 'docs_src' / 'equations.json').read_text(encoding='utf-8'))}
    reg, owner = load_registry()
    out = []
    used = set()
    nextra = 0
    for src in sorted((HERE / 'src').glob('*.md')):
        lines = src.read_text(encoding='utf-8').split('\n')
        i = 0
        while i < len(lines):
            ln = lines[i]
            m = re.match(r'^@((?:FE|IN)-\d+)\s*$', ln)
            if m:
                q = eqs[m.group(1)]
                if m.group(1) in used:
                    print('NOTE: %s written out again (%s)' % (m.group(1), src.name))
                used.add(m.group(1))
                out += ['$$', q['latex'], '$$', '', '<!-- symbols: %s -->' % ', '.join(q['keys'])]
                i += 1
                continue
            if ln.strip() == '@@':
                j = i + 1
                body = []
                while j < len(lines) and lines[j].strip() != '@@':
                    body.append(lines[j])
                    j += 1
                if j >= len(lines):
                    raise SystemExit('unclosed @@ in %s at line %d' % (src.name, i + 1))
                latex = '\n'.join(body).strip('\n')
                nextra += 1
                for bl in latex.split('\n'):
                    if len(bl) > 112:
                        print('LONG line in extra display (%s line %d): %s' % (src.name, i + 1, bl[:70]))
                keys = keys_of(latex, owner, '%s line %d' % (src.name, i + 1))
                out += ['$$', latex, '$$', '', '<!-- symbols: %s -->' % ', '.join(keys)]
                i = j + 1
                continue
            out.append(ln)
            i += 1
    missing = [k for k in eqs if k not in used]
    if missing:
        print('MISSING inventory equations:', ', '.join(missing))
    text = '\n'.join(out).rstrip('\n') + '\n'
    md = REPO / 'FIELD_EQUATIONS.md'
    md.write_text(text, encoding='utf-8')
    print('written %s: %d inventory displays, %d extra displays, %d lines' % (md.name, len(used), nextra, len(out)))
    tool = str(REPO / 'tools' / 'symbols_tool.py')
    r = subprocess.run([sys.executable, tool, 'expand', 'FIELD_EQUATIONS'], capture_output=True, text=True)
    print('expand:', r.returncode, r.stdout[-1500:], r.stderr[-1500:])
    r = subprocess.run([sys.executable, tool, 'check', 'FIELD_EQUATIONS'], capture_output=True, text=True)
    print(r.stdout[-4000:], r.stderr[-1500:])
    if '--build' in sys.argv:
        r = subprocess.run(['nice', '-n', '5', sys.executable, str(REPO / 'tools' / 'build_docs.py'), 'FIELD_EQUATIONS'],
                           capture_output=True, text=True, cwd=str(REPO.parent))
        print(r.stdout[-3000:], r.stderr[-3000:])


if __name__ == '__main__':
    main()
