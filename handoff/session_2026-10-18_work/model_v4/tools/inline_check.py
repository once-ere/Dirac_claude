#!/usr/bin/env python3
"""List atoms of inline math ($...$) in the given Markdown files that no registry key owns.
usage: inline_check.py FILE.md...   (prints atom, count, first contexts)"""
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path('/home/claude/dirac_claude/universe_model_2')
sys.path.insert(0, str(ROOT / 'tools'))
import symbols_tool as st  # noqa: E402

reg, owner, _ = st.load_registry()
known = frozenset(owner)
miss = defaultdict(list)
for fn in sys.argv[1:]:
    text = Path(fn).read_text()
    # drop display blocks
    text = re.sub(r'\$\$.*?\$\$', ' ', text, flags=re.S)
    # drop generated symbol lists if present
    text = re.sub(r'<!-- begin generated symbol list -->.*?<!-- end generated symbol list -->', ' ', text, flags=re.S)
    for m in re.finditer(r'(?<!\\)\$(.+?)(?<!\\)\$', text, flags=re.S):
        tex = m.group(1)
        try:
            ats = st.atoms_of(tex, known)
        except Exception as exc:  # noqa: BLE001
            miss['PARSE-ERROR ' + str(exc)[:40]].append((fn, tex))
            continue
        for a in ats:
            if a not in owner:
                miss[a].append((Path(fn).name, tex))
for a, lst in sorted(miss.items(), key=lambda x: -len(x[1])):
    ctx = '; '.join(sorted(set(t for _, t in lst)))[:160]
    files = ','.join(sorted(set(f[:3] for f, _ in lst)))
    print('%-34s %3d  [%s]  %s' % (a, len(lst), files, ctx))
