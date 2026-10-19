#!/usr/bin/env python3
"""Build core.json and equations.json from the registry/equation modules, write a test document, run the symbols tool
(expand, check) and optionally pandoc + pdflatex.  Usage: python3 build.py [--pdf] [--write]"""
import importlib
import json
import os
import re
import subprocess
import sys
from pathlib import Path

SCR = Path(__file__).resolve().parent
REPO = Path('/home/claude/dirac_claude/universe_model_2')
sys.path.insert(0, str(SCR))
sys.path.insert(0, str(REPO / 'tools'))
import symbols_tool as st  # noqa: E402
from build_lib import REG, EQS  # noqa: E402
from solved_v4 import SOLVED  # noqa: E402

REG_MODULES = sorted(p.stem for p in SCR.glob('reg_*.py'))
EQ_MODULES = sorted(p.stem for p in SCR.glob('eq_*.py'))


def wrap(latex, width=104):
    """Soft-wrap long source lines at a space (a newline is a space in TeX math); never right after a backslash."""
    out = []
    for ln in latex.split('\n'):
        while len(ln) > width + 6:
            cut = -1
            for pos in range(width, 20, -1):
                if ln[pos] == ' ' and ln[pos - 1] != '\\' and ln[pos + 1:pos + 2] not in ('', ' '):
                    cut = pos
                    break
            if cut >= 0:
                out.append(ln[:cut])
                ln = ' ' + ln[cut + 1:]
                continue
            for pos in range(width, 20, -1):   # else break before a control word (harmless in math mode)
                if ln[pos] == '\\' and ln[pos - 1] != '\\' and ln[pos + 1:pos + 2].isalpha():
                    cut = pos
                    break
            if cut < 0:
                break
            out.append(ln[:cut])
            ln = ' ' + ln[cut:]
        out.append(ln)
    return '\n'.join(out)


MARKS = {'prime', 'dagger', 'transpose', 'star'}


def canon(s):
    """The atom the tool forms for a registered name written as LaTeX (base with up to two glued scripts)."""
    if s.startswith('index:') or s in MARKS:
        return s
    toks = st.tokenize(s)
    if toks[0] in st.DECOR or toks[0] in st.NAMEFONTS:
        base, i = st.group(toks, 0)
    else:
        base, i = [toks[0]], 1
    atom = st.normalise(base)
    while i < len(toks) and toks[i] in ('_', '^'):
        kind = toks[i]
        g, i = st.group(toks, i + 1)
        atom = atom + kind + '{' + st.normalise(g) + '}'
    return atom


def main():
    for m in REG_MODULES + EQ_MODULES:
        importlib.import_module(m)
    for e in REG.values():
        e['atoms'] = [canon(a) for a in e['atoms']]
    # atom ownership
    owner = {}
    bad = []
    for k, e in REG.items():
        for a in e['atoms']:
            if a in owner:
                bad.append('atom %s in %s and %s' % (a, owner[a], k))
            owner[a] = k
    names = frozenset(owner)
    counters = {'IN': 0, 'FE': 0}
    ids = {}
    for q in EQS:
        counters[q['kind']] += 1
        if q['name']:
            if q['name'] in ids:
                raise SystemExit('duplicate equation name ' + q['name'])
            ids[q['name']] = '%s-%d' % (q['kind'], counters[q['kind']])
    counters = {'IN': 0, 'FE': 0}

    def refs(text):
        def sub(m):
            if m.group(1) not in ids:
                print('UNRESOLVED reference', m.group(1))
                return m.group(0)
            return ids[m.group(1)]
        return re.sub(r'\[\[([A-Za-z0-9_]+)\]\]', sub, text)
    out = []
    unknown = {}
    used = set()
    longlines = []
    for q in EQS:
        counters[q['kind']] += 1
        eid = '%s-%d' % (q['kind'], counters[q['kind']])
        latex = wrap(q['latex'].rstrip() + ' \\tag{%s}' % eid)
        keys = []
        for a in st.atoms_of(latex, names):
            if a in owner:
                if owner[a] not in keys:
                    keys.append(owner[a])
            else:
                unknown.setdefault(a, []).append(eid)
        used.update(keys)
        for ln in latex.split('\n'):
            if len(ln) > 112:
                longlines.append('%s (%d chars): %s' % (eid, len(ln), ln[:60]))
        out.append({'id': eid, 'title': q['title'], 'latex': latex, 'keys': keys, 'status': q['status'],
                    'fields': q['fields'], 'solved_in': SOLVED.get(eid, refs(q['solved_in']))})
    for b in bad:
        print('DUPLICATE', b)
    for a, ids in sorted(unknown.items()):
        print('UNKNOWN atom %-28s in %s' % (a, ', '.join(ids[:6])))
    for l in longlines:
        print('LONG', l)
    unused = [k for k in REG if k not in used]
    print('registry entries %d, unused %d: %s' % (len(REG), len(unused), ', '.join(unused[:40])))
    print('equations: IN %d, FE %d' % (counters['IN'], counters['FE']))
    # test document
    lines = ['---', 'title: "UM-2 version 4: inventory test"', '---', '']
    for q in out:
        lines += ['**(%s) %s.** Status: %s.' % (q['id'], q['title'], q['status']), '', '$$', q['latex'], '$$', '',
                  '<!-- symbols: %s -->' % ', '.join(q['keys']), '']
    test = SCR / 'test_fe.md'
    test.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    if '--write' in sys.argv or '--pdf' in sys.argv:
        (REPO / 'docs_src' / 'symbols').mkdir(parents=True, exist_ok=True)
        (REPO / 'docs_src' / 'symbols' / 'core.json').write_text(
            json.dumps(REG, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
        (REPO / 'docs_src' / 'equations.json').write_text(
            json.dumps(out, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
        tool = str(REPO / 'tools' / 'symbols_tool.py')
        r = subprocess.run([sys.executable, tool, 'expand', str(test)], capture_output=True, text=True)
        print('expand:', r.returncode, r.stdout[-2000:], r.stderr[-2000:])
        r = subprocess.run([sys.executable, tool, 'check', str(test)], capture_output=True, text=True)
        print('check:', r.stdout[-3000:], r.stderr[-1000:])
    if '--pdf' in sys.argv:
        pdf(test)


HEADER = r"""
\usepackage{amsmath,amssymb}
\usepackage{graphicx}
\usepackage{longtable,booktabs,array}
\usepackage{xcolor}
\usepackage[margin=2.1cm]{geometry}
\usepackage{microtype}
\setlength{\emergencystretch}{3em}
\renewcommand{\arraystretch}{1.15}
\allowdisplaybreaks
"""


def pdf(md):
    bdir = SCR / 'pdfbuild'
    bdir.mkdir(exist_ok=True)
    hdr = bdir / 'header.tex'
    hdr.write_text(HEADER, encoding='utf-8')
    tex = bdir / 'test_fe.tex'
    r = subprocess.run(['pandoc', str(md), '-f', 'markdown+tex_math_dollars+pipe_tables+raw_tex', '-t', 'latex', '-s',
                        '-V', 'documentclass=article', '-V', 'fontsize=10pt', '--include-in-header', str(hdr),
                        '-o', str(tex)], capture_output=True, text=True)
    if r.returncode:
        print('pandoc failed', r.stderr[:2000])
        return
    for _ in range(2):
        r = subprocess.run(['pdflatex', '-interaction=nonstopmode', '-halt-on-error', '-output-directory', str(bdir),
                            str(tex)], capture_output=True, text=True, encoding='latin-1', cwd=bdir)
        if r.returncode:
            log = (bdir / 'test_fe.log').read_text(encoding='latin-1')
            i = log.find('\n!')
            print('pdflatex failed:', log[i:i + 2500])
            return
    log = (bdir / 'test_fe.log').read_text(encoding='latin-1')
    m = re.search(r'Output written on [^(]*\((\d+) pages?', log.replace('\n', ''))
    print('pdf pages', m.group(1) if m else '?', 'overfull', log.count('Overfull'))
    for mm in re.finditer(r'Overfull \\hbox \(([\d.]+)pt too wide\)[^\n]*lines? (\d+)', log):
        print('  overfull %spt at tex line %s' % (mm.group(1), mm.group(2)))


if __name__ == '__main__':
    main()
