#!/usr/bin/env python3
"""For each section (## or #) list FE/IN tags mentioned in prose that are not written out (@@TAG@@) in that section."""
import re, sys
from pathlib import Path
for fn in sys.argv[1:]:
    sec = None; written = set(); mentioned = {}
    def flush():
        if sec is None: return
        miss = {t: c for t, c in mentioned.items() if t not in written}
        if miss:
            print('%s | %s' % (Path(fn).name[:3], sec[:70]))
            for t, c in sorted(miss.items(), key=lambda x: (x[0].split('-')[0], int(x[0].split('-')[1]))):
                print('     %-7s %s' % (t, c[:150]))
    for line in Path(fn).read_text().splitlines():
        if re.match(r'^#{1,2} ', line):
            flush(); sec = line; written = set(); mentioned = {}
            continue
        m = re.match(r'^@@((?:FE|IN)-\d+)@@\s*$', line)
        if m:
            written.add(m.group(1)); continue
        for t in re.findall(r'\b((?:FE|IN)-\d+)\b', line):
            mentioned.setdefault(t, line.strip())
    flush()
