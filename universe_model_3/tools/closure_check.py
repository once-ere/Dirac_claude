#!/usr/bin/env python3
"""closure_check.py - the closure of the symbol lists of the UM-3 documents: every symbol that the meaning, the value or the
unit of a listed entry writes in mathematics must itself be defined by an entry listed in the same document (or by the
entry itself).  Group names such as SU(3) and unit names such as \\mathrm{GeV} are typography.  The same test is part of
`symbols_tool.py check`; this module reports the undefined symbols with their owning entries, and `symbols_close.py` uses it
to add those entries to the lists.

Usage (repository root):  python universe_model_3/tools/closure_check.py [NAME ...] [--index]
"""
import re
import sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import symbols_tool as st

MATH = re.compile(r'(?<!\\)\$(.+?)(?<!\\)\$')
GROUP = re.compile(r'(?:\\mathrm\{)?(?:SU|SO|Sp|U|O)(?:\})?\(\d+\)(?:_\{?(?:\\mathrm\{)?[A-Za-z]+\}?\}?)?|E_8')
UNITS = re.compile(r'(?<![_{])\\mathrm\{(?:GeV|MeV|keV|eV|meV|TeV|PeV|cm|km|Mpc|Gpc|kpc|pc|yr|Gyr)\}')
LABELS = re.compile(r'\\in\s*\\\{.*?\\\}')   # in the entry of an index: the values of the label, defined by the entry


def base(a):
    return re.sub(r'_\{.*\}$|_.$', '', a)


def satisfied(a, atoms):
    # a numbered copy of a Latin index letter (M_1, N_2) is the index itself
    numbered = re.fullmatch(r'[A-Za-z]_\{?\d+\}?', a) is not None
    return a in atoms or ('index:' + a) in atoms or (numbered and ('index:' + base(a)) in atoms)


def closure(name, reg, owner, with_index=False):
    lines = st.doc_path(name).read_text(encoding='utf-8').split('\n')
    listed = []
    for line in lines:
        m = st.MARK.match(line.strip()) or st.FURTHER.match(line.strip())
        if m:
            for k in m.group(1).split(','):
                k = k.strip()
                if k in reg and k not in listed:
                    listed.append(k)
    defined = set()
    for k in listed:
        defined.update(reg[k]['atoms'])
    missing = {}
    for k in listed:
        own = set(reg[k]['atoms'])
        is_index = all(x.startswith('index:') for x in reg[k]['atoms'][:1])
        for field in ('meaning', 'value', 'units'):
            for seg in MATH.findall(reg[k].get(field, '') or ''):
                seg = UNITS.sub(' ', GROUP.sub(' ', seg))
                if is_index:
                    seg = LABELS.sub(' ', seg)
                for a in st.atoms_of(seg, frozenset(owner)):
                    if a.startswith('index:'):
                        if not with_index:
                            continue
                        a2 = a[6:]
                        if satisfied(a2, own) or satisfied(a2, defined) or a in defined:
                            continue
                        missing.setdefault(a, set()).add(k)
                        continue
                    if satisfied(a, own) or satisfied(a, defined):
                        continue
                    missing.setdefault(a, set()).add(k)
    return listed, missing


def main():
    args = sys.argv[1:]
    with_index = '--index' in args
    names = [a for a in args if not a.startswith('--')] or st.NAMES
    reg, owner, _ = st.load_registry()
    total = 0
    for n in names:
        listed, missing = closure(n, reg, owner, with_index)
        total += len(missing)
        print('== %s: %d keys listed, %d undefined symbols in the meanings' % (n, len(listed), len(missing)))
        for a, ks in sorted(missing.items()):
            print('   %-30s owner=%-12s used by %s' % (a, owner.get(a, owner.get('index:' + a, '-')), ', '.join(sorted(ks))))
    print('closure=%s (%d)' % ('OK' if total == 0 else 'FAILED', total))
    return 1 if total else 0


if __name__ == '__main__':
    sys.exit(main())
