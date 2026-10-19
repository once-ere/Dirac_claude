#!/usr/bin/env python3
"""Assemble ANALYSIS.md (version 4) from the source parts: inventory placeholders @@FE-n@@ / @@IN-n@@ are replaced by the
exact LaTeX and keys of universe_model_2/docs_src/equations.json."""
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = Path('/home/claude/dirac_claude')
INV = json.loads((ROOT / 'universe_model_2/docs_src/equations.json').read_text(encoding='utf-8'))
INV = {e['id']: e for e in INV}
parts = ['src_0.md', 'src_A.md', 'src_B.md', 'src_C.md']
text = '\n'.join((HERE / p).read_text(encoding='utf-8').rstrip('\n') for p in parts) + '\n'
used = []


def repl(m):
    tag = m.group(1)
    e = INV[tag]
    used.append(tag)
    latex = e['latex'].strip('\n')
    assert '\\tag{%s}' % tag in latex, tag
    return '$$\n' + latex + '\n$$\n<!-- symbols: ' + ', '.join(e['keys']) + ' -->'


text = re.sub(r'^@@((?:FE|IN)-\d+)@@$', repl, text, flags=re.M)
assert '@@' not in text
(ROOT / 'universe_model_2/ANALYSIS.md').write_text(text, encoding='utf-8')
print('assembled; inventory equations written out: %d (%d distinct): %s' % (len(used), len(set(used)), ', '.join(used)))
