#!/usr/bin/env python3
"""Build the UM-3 documents: NAME.md -> NAME.tex (pandoc, standalone, fixed preamble) -> NAME.pdf (pdflatex, run until
the table of contents and the cross references are stable).

Deterministic: no dates in the .tex, the PDF creation date and trailer id suppressed, SOURCE_DATE_EPOCH fixed, every
run from a clean build directory.  Names may contain spaces ("dirac matrices"): the build directory uses a name with
underscores and the results are copied back under the document's own name.

Usage (from anywhere):  python universe_model_3/tools/build_docs.py [NAME ...]   (default: every document listed below)
Exit code 0 iff every requested document was built.  Overfull boxes are reported.
"""
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
DOCS = HERE.parent
BUILD = DOCS.parent / 'build' / 'universe_model_3'
NAMES = ['dirac matrices', 'MODEL', 'FIELD_EQUATIONS', 'SOLUTION', 'ANALYSIS', 'PROVENANCE']

HEADER = r"""
\usepackage{amsmath,amssymb}
\usepackage{graphicx}
\usepackage{longtable,booktabs,array}
\usepackage{xcolor}
\usepackage[margin=2.0cm]{geometry}
\usepackage{microtype}
\setlength{\emergencystretch}{3em}
\setcounter{MaxMatrixCols}{20}
\pdfinfoomitdate=1
\pdftrailerid{}
\pdfsuppressptexinfo=-1
\renewcommand{\arraystretch}{1.12}
\usepackage{fvextra}
\RecustomVerbatimEnvironment{verbatim}{Verbatim}{breaklines,breakanywhere,fontsize=\small}
\fvset{breaklines,breakanywhere}
\allowdisplaybreaks
\sloppy
"""


def build(name):
    md = DOCS / (name + '.md')
    safe = name.replace(' ', '_')
    BUILD.mkdir(parents=True, exist_ok=True)
    hdr = BUILD / 'header.tex'
    hdr.write_text(HEADER, encoding='utf-8')
    tex_build = BUILD / (safe + '.tex')
    env = dict(os.environ, SOURCE_DATE_EPOCH='1792800000', FORCE_SOURCE_DATE='1', TZ='UTC')
    cmd = ['pandoc', str(md), '-f', 'markdown+tex_math_dollars+pipe_tables+raw_tex+implicit_figures', '-t', 'latex', '-s',
           '--toc', '--number-sections', '-V', 'documentclass=article', '-V', 'fontsize=10pt', '-V', 'colorlinks=true',
           '-V', 'linkcolor=blue', '-V', 'urlcolor=blue', '-V', 'date=', '--include-in-header', str(hdr),
           '-o', str(tex_build)]
    r = subprocess.run(cmd, cwd=DOCS, capture_output=True, text=True, env=env, timeout=300)
    if r.returncode != 0:
        print('pandoc FAILED for %s: %s' % (name, r.stderr[:3000]))
        return False
    for ext in ('.aux', '.toc', '.out', '.log', '.pdf'):
        p = BUILD / (safe + ext)
        if p.exists():
            p.unlink()
    prev = None
    for run in range(6):
        r = subprocess.run(['pdflatex', '-interaction=nonstopmode', '-halt-on-error', '-output-directory=' + str(BUILD),
                            str(tex_build)], cwd=DOCS, capture_output=True, text=True, encoding='latin-1', env=env, timeout=900)
        if r.returncode != 0:
            log = (BUILD / (safe + '.log')).read_text(encoding='latin-1')
            idx = log.find('\n!')
            print('pdflatex FAILED for %s:\n%s' % (name, log[idx:idx + 2500]))
            return False
        state = tuple((BUILD / (safe + e)).read_bytes() if (BUILD / (safe + e)).exists() else b'' for e in ('.aux', '.toc', '.out'))
        if run >= 1 and state == prev:
            break
        prev = state
    shutil.copyfile(tex_build, DOCS / (name + '.tex'))
    shutil.copyfile(BUILD / (safe + '.pdf'), DOCS / (name + '.pdf'))
    log = (BUILD / (safe + '.log')).read_text(encoding='latin-1')
    m = re.search(r'Output written on [^(]*\((\d+) pages?', log.replace('\n', ''))
    print('%s.pdf: %s pages, overfull boxes: %d' % (name, m.group(1) if m else '?', log.count('Overfull')))
    return True


def main():
    names = sys.argv[1:] or [n for n in NAMES if (DOCS / (n + '.md')).exists()]
    ok = all([build(n) for n in names])
    sys.exit(0 if ok else 1)


if __name__ == '__main__':
    main()
