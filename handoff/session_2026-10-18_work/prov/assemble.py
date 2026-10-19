#!/usr/bin/env python3
"""Assemble universe_model_2/PROVENANCE.md from the parts: fill @@FE-n@@ / @@IN-n@@ with the inventory's display (LaTeX,
tag and keys, exactly as in docs_src/equations.json) and @@CATALOGUE@@ with the numbered check names of the reports."""
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = '/home/claude/dirac_claude/universe_model_2'
INV = json.load(open(os.path.join(ROOT, 'docs_src', 'equations.json')))
BYID = {e['id']: e for e in INV}

REPORTS = [
    ('alg', 'um2_algebra.py', 'algebra-checks.json'),
    ('geo', 'um2_geometry.py', 'geometry-checks.json'),
    ('bg', 'um2_background.py', 'background-checks.json'),
    ('fld', 'um2_fields.py', 'fields-checks.json'),
    ('mass', 'um2_spectra.py', 'masses-checks.json'),
    ('flav', 'um2_flavour.py', 'flavour-checks.json'),
    ('nu', 'um2_neutrino.py', 'neutrino-checks.json'),
    ('ksv', 'um2_ks_jobs.py validate', 'ks-checks-validate.json'),
    ('kss', 'um2_ks_jobs.py spectrum', 'ks-checks-spectrum.json'),
    ('ks8', 'um2_ks_jobs.py ground8', 'ks-checks-ground8.json'),
    ('ks592', 'um2_ks_jobs.py ground592', 'ks-checks-ground592.json'),
    ('ksdm', 'um2_ks_jobs.py darkmatter', 'ks-checks-darkmatter.json'),
    ('ksp', 'um2_ks_jobs.py portals', 'ks-checks-portals.json'),
    ('ksfb', 'um2_ks_jobs.py feedback', 'ks-checks-feedback.json'),
    ('ew', 'um2_electroweak.py', 'electroweak-checks.json'),
    ('prim', 'um2_primordial.py', 'primordial-checks.json'),
    ('cos', 'um2_cosmology.py', 'cosmology-checks.json'),
    ('ana', 'um2_analysis.py', 'analysis-checks.json'),
    ('th', 'um2_thermal.py', 'thermal-checks.json'),
    ('cpl', 'um2_coupled.py', 'coupled-checks.json'),
    ('ser', 'um2_series.py', 'series-checks.json'),
    ('res', 'um2_residuals.py', 'residuals-checks.json'),
]


def display(eid):
    e = BYID[eid]
    return '$$\n%s\n$$\n\n<!-- symbols: %s -->' % (e['latex'].strip(), ', '.join(e['keys']))


def catalogue():
    out = []
    total = 0
    for ab, script, rep in REPORTS:
        d = json.load(open(os.path.join(ROOT, 'reports', rep)))
        assert d['failed_check_count'] == 0
        names = [c['name'] for c in d['checks']]
        assert all('`' not in n for n in names)
        total += len(names)
        items = '; '.join('%d `%s`' % (i, n) for i, n in enumerate(names, 1))
        out.append('**%s** (`%s`, %d checks, all passed): %s.' % (ab, script, len(names), items))
        out.append('')
    assert total == 287, total
    return '\n'.join(out).rstrip()


def main():
    parts = ['part%d.md' % i for i in range(1, 9)]
    text = '\n'.join(open(os.path.join(HERE, p)).read().rstrip('\n') + '\n' for p in parts)
    text = text.replace('@@CATALOGUE@@', catalogue())
    used = []

    def rep(m):
        used.append(m.group(1))
        return display(m.group(1))
    text = re.sub(r'@@((?:FE|IN)-\d+)@@', rep, text)
    assert '@@' not in text
    open(os.path.join(ROOT, 'PROVENANCE.md'), 'w').write(text)
    print('written; inventory displays:', len(used), sorted(set(used), key=lambda s: (s[:2], int(s[3:]))))


if __name__ == '__main__':
    main()
