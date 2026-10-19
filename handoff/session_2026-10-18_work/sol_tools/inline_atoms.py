#!/usr/bin/env python3
"""List the atoms of the inline formulas of a Markdown source that no registry entry owns (with where they occur)."""
import re, sys
from pathlib import Path
REPO = Path('/home/claude/dirac_claude/universe_model_2')
sys.path.insert(0, str(REPO / 'tools'))
import symbols_tool as st
reg, owner, problems = st.load_registry()
names = frozenset(owner)
text = Path(sys.argv[1]).read_text(encoding='utf-8')
# drop display blocks and HTML comments
text = re.sub(r'\$\$.*?\$\$', ' ', text, flags=re.S)
text = re.sub(r'<!--.*?-->', ' ', text, flags=re.S)
text = re.sub(r'`[^`]*`', ' ', text)
unknown = {}
if True:
    for m in re.finditer(r'(?<!\\)\$([^$]+?)(?<!\\)\$', text, flags=re.S):
        latex = m.group(1).replace('\n', ' ')
        i = text.count('\n', 0, m.start())
        try:
            ats = st.atoms_of(latex, names)
        except Exception as exc:
            unknown.setdefault('PARSE-ERROR ' + latex[:40], []).append(i + 1)
            continue
        for a in ats:
            if a not in owner:
                unknown.setdefault(a, []).append((i + 1, latex[:70]))
for a, where in sorted(unknown.items(), key=lambda x: -len(x[1])):
    print('%-28s %3d  %s' % (a, len(where), where[:3]))
