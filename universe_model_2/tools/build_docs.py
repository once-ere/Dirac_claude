#!/usr/bin/env python3
"""Build the UM-2 documents: NAME.md -> NAME.tex (pandoc, standalone, fixed preamble) -> NAME.pdf (pdflatex, run until the
table of contents and the references are stable).  Deterministic: no dates in the .tex, PDF dates and trailer id suppressed,
SOURCE_DATE_EPOCH fixed, every run from a clean build directory.

Usage (from anywhere): python universe_model_2/tools/build_docs.py [NAME ...]   (default: every document of the folder)
Exit code 0 iff every document was built; overfull boxes are reported.
"""
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
DOCS = HERE.parent
BUILD = DOCS.parent / 'build' / 'universe_model_2'
NAMES = ['MODEL', 'PROVENANCE', 'FIELD_EQUATIONS', 'SOLUTION', 'ANALYSIS']

HEADER = r"""
\usepackage{amsmath,amssymb}
\usepackage{graphicx}
\usepackage{longtable,booktabs,array}
\usepackage{xcolor}
\usepackage[margin=2.1cm]{geometry}
\usepackage{microtype}
\setlength{\emergencystretch}{3em}
\pdfinfoomitdate=1
\pdftrailerid{}
\pdfsuppressptexinfo=-1
\renewcommand{\arraystretch}{1.15}
\allowdisplaybreaks
"""


def build(name):
    md = DOCS / (name + '.md')
    tex = DOCS / (name + '.tex')
    hdr = BUILD / 'header.tex'
    BUILD.mkdir(parents=True, exist_ok=True)
    hdr.write_text(HEADER, encoding='utf-8')
    env = dict(os.environ, SOURCE_DATE_EPOCH='1792195200', FORCE_SOURCE_DATE='1', TZ='UTC')
    cmd = ['pandoc', str(md), '-f', 'markdown+tex_math_dollars+pipe_tables+raw_tex+implicit_figures', '-t', 'latex', '-s',
           '--toc', '--number-sections', '-V', 'documentclass=article', '-V', 'fontsize=10pt', '-V', 'colorlinks=true',
           '-V', 'linkcolor=blue', '-V', 'urlcolor=blue', '-V', 'date=', '--include-in-header', str(hdr), '-o', str(tex)]
    r = subprocess.run(cmd, cwd=DOCS, capture_output=True, text=True, env=env, timeout=120)
    if r.returncode != 0:
        print('pandoc FAILED for %s: %s' % (name, r.stderr[:2000]))
        return False
    # graphics are referenced relative to the document folder (pdflatex runs with cwd = the document folder)
    for ext in ('.aux', '.toc', '.out', '.log'):
        p = BUILD / (name + ext)
        if p.exists():
            p.unlink()
    prev = None
    for run in range(6):
        r = subprocess.run(['pdflatex', '-interaction=nonstopmode', '-halt-on-error', '-output-directory=' + str(BUILD), str(tex)],
                           cwd=DOCS, capture_output=True, text=True, encoding='latin-1', env=env, timeout=180)
        if r.returncode != 0:
            log = (BUILD / (name + '.log')).read_text(encoding='latin-1')
            err = [l for l in log.splitlines() if l.startswith('!')]
            idx = log.find('\n!')
            print('pdflatex FAILED for %s: %s\n%s' % (name, err[:3], log[idx:idx + 1500]))
            return False
        state = tuple((BUILD / (name + e)).read_bytes() if (BUILD / (name + e)).exists() else b'' for e in ('.aux', '.toc', '.out'))
        if run >= 1 and state == prev:
            break
        prev = state
    shutil.copyfile(BUILD / (name + '.pdf'), DOCS / (name + '.pdf'))
    log = (BUILD / (name + '.log')).read_text(encoding='latin-1')
    m = re.search(r'Output written on [^(]*\((\d+) pages?', log.replace('\n', ''))
    print('%s.pdf: %s pages, overfull boxes: %d' % (name, m.group(1) if m else '?', log.count('Overfull')))
    return True


def main():
    names = sys.argv[1:] or [n for n in NAMES if (DOCS / (n + '.md')).exists()]
    ok = all([build(n) for n in names])
    sys.exit(0 if ok else 1)


if __name__ == '__main__':
    main()
