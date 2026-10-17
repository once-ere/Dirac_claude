#!/usr/bin/env python3
"""Revision/universe_model/tools/md2tex.py - convert the restricted Markdown of the universe-model documents to LaTeX
(the .md file is the source; the .tex and the .pdf follow from it, so the two say the same thing).

Supported: '#', '##', '###' headings; paragraphs; '* ' bullets (with indented continuation lines); '1. ' numbered
items; pipe tables (header, separator, rows); fenced code blocks; display math '$$ ... $$' (one line or several);
inline math '$...$' (passed through); '**bold**'; '`code`'.  Everything outside math and code is escaped.

Usage: python md2tex.py IN.md OUT.tex ["Title"]   (the first '# ' heading is the title if none is given)
Deterministic output (no dates); compile with pdflatex twice (table of contents)."""
import os
import re
import sys
from pathlib import Path

PREAMBLE = r"""\documentclass[11pt]{article}
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage{lmodern}
\usepackage[margin=1in]{geometry}
\usepackage{amsmath,amssymb,mathtools}
\usepackage{booktabs,longtable,array}
\usepackage{fancyvrb}
\usepackage[hidelinks]{hyperref}
\usepackage{microtype}
\usepackage{graphicx}
\usepackage{adjustbox}
\pdfinfoomitdate=1
\pdftrailerid{}
\pdfsuppressptexinfo=15
\setlength{\parindent}{0pt}
\setlength{\parskip}{0.6em}
\setlength{\emergencystretch}{3em}
\renewcommand{\arraystretch}{1.25}
\setlength{\tabcolsep}{4pt}
\sloppy
"""

SPECIAL = {"\\": r"\textbackslash{}", "&": r"\&", "%": r"\%", "#": r"\#", "_": r"\_", "{": r"\{", "}": r"\}",
           "~": r"\textasciitilde{}", "^": r"\textasciicircum{}", "<": r"\textless{}", ">": r"\textgreater{}",
           "|": r"\textbar{}"}


def esc(s):
    return "".join(SPECIAL.get(c, c) for c in s)


def inline(s):
    """escape a line of text, keeping $...$ math and turning `code` and **bold** into LaTeX"""
    out = []
    i = 0
    while i < len(s):
        if s[i] == "$":
            j = s.find("$", i + 1)
            if j < 0:
                out.append(esc(s[i:]))
                break
            out.append(s[i:j + 1])
            i = j + 1
        elif s[i] == "`":
            j = s.find("`", i + 1)
            if j < 0:
                out.append(esc(s[i:]))
                break
            code = s[i + 1:j]
            tt = esc(code).replace("-", r"-{}\allowbreak{}").replace("/", r"/\allowbreak{}").replace(r"\_", r"\_\allowbreak{}").replace(".", r".\allowbreak{}")
            out.append(r"\texttt{" + tt + "}")
            i = j + 1
        elif s.startswith("**", i):
            j = s.find("**", i + 2)
            if j < 0:
                out.append(esc(s[i:]))
                break
            out.append(r"\textbf{" + inline(s[i + 2:j]) + "}")
            i = j + 2
        else:
            j = i
            while j < len(s) and s[j] not in "$`" and not s.startswith("**", j):
                j += 1
            out.append(esc(s[i:j]))
            i = j
    return "".join(out)


def split_row(r):
    """split a pipe-table row at '|' outside $...$ math and `code`"""
    r = r.strip()
    if r.startswith("|"):
        r = r[1:]
    if r.endswith("|"):
        r = r[:-1]
    cells, cur, in_math, in_code = [], [], False, False
    for ch in r:
        if ch == "$" and not in_code:
            in_math = not in_math
        elif ch == "`" and not in_math:
            in_code = not in_code
        if ch == "|" and not in_math and not in_code:
            cells.append("".join(cur).strip())
            cur = []
        else:
            cur.append(ch)
    cells.append("".join(cur).strip())
    return cells


def visible_len(c):
    """the rendered width of a cell in characters, roughly: a TeX command counts as one character, the math and
    grouping characters as none, and a bold header as 1.1"""
    v = re.sub(r"\\[a-zA-Z]+", "x", c)
    v = re.sub(r"[${}^_`*]", "", v)
    return len(v)


def longest_token(c):
    """the visible length of the longest piece of a cell that cannot be broken across lines (split at spaces)"""
    pieces = []
    for t in re.split(r"\s+", c.strip()):
        # code may break after '/', '.', '_' and '-' (inline() adds the break points)
        pieces += re.split(r"(?<=[/._-])", t) if "`" in t else [t]
    return max((visible_len(t) for t in pieces if t), default=0)


def table(rows):
    cells = [split_row(r) for r in rows]
    head, body = cells[0], cells[2:]
    n = len(head)
    allrows = [head] + body

    def col(c):
        return [r[c] if c < len(r) else "" for r in allrows]
    # every column at least as wide as its longest unbreakable piece (bold header pieces 1.15 x wider); the rest of
    # the line (0.92, less the column separation 2 x 4pt = 0.0171 of the line per column) in proportion to the
    # widest cell of each column (clipped)
    cw = 0.0112 if n >= 7 else 0.0122
    mins = [cw * (1.0 + max([1.15 * longest_token(head[c]) if c < len(head) else 0] + [longest_token(x) for x in col(c)[1:]]))
            for c in range(n)]
    wts = [min(70, max(6, max(1.1 * visible_len(head[c]) if c < len(head) else 0, max(visible_len(x) for x in col(c)[1:]) if body else 0)))
           for c in range(n)]
    avail = 0.92 - 0.0171 * n
    extra = avail - sum(mins)
    widths = [m + max(extra, 0.0) * w / sum(wts) for m, w in zip(mins, wts)]
    spec = "".join(r">{\raggedright\arraybackslash}p{%.3f\linewidth}" % w for w in widths)
    lines = [r"\begin{longtable}{" + spec + "}", r"\toprule",
             " & ".join(r"\textbf{" + inline(c) + "}" for c in head) + r" \\", r"\midrule"]
    for r in body:
        r = (r + [""] * n)[:n]
        row = " & ".join(inline(c) for c in r)
        if row[:1] in "([":
            # booktabs' rules look ahead for '(' (cmidrule trim) and '[' (width): protect a row that starts with one
            row = "{}" + row
        lines.append(row + r" \\")
    lines += [r"\bottomrule", r"\end{longtable}"]
    if n >= 7:
        # wide tables in a smaller font
        lines = [r"\begingroup\small"] + lines + [r"\endgroup"]
    return "\n".join(lines)


def heading(kind, text):
    """a heading whose text carries its own number ('3.', '4.1') is set unnumbered and added to the contents"""
    m = re.match(r"^(\d+(\.\d+)*\.?)\s+(.*)$", text)
    if m:
        return (r"\%s*{%s}" % (kind, inline(text))) + "\n" + (r"\addcontentsline{toc}{%s}{%s}" % (kind, inline(text)))
    return r"\%s{%s}" % (kind, inline(text))


def convert(md, title=None, graphics_dir=None):
    lines = md.split("\n")
    body = []
    i = 0
    if title is None:
        for k, l in enumerate(lines):
            if l.startswith("# "):
                title = l[2:].strip()
                lines = lines[:k] + lines[k + 1:]
                break
    in_list = None

    def close_list():
        nonlocal in_list
        if in_list:
            body.append(r"\end{" + in_list + "}")
            in_list = None

    while i < len(lines):
        l = lines[i]
        if l.strip().startswith("<!--"):
            # an HTML comment line (the GENERATED markers): not part of the document
            i += 1
            continue
        mimg = re.match(r"^!\[(.*)\]\((.+)\)\s*$", l.strip())
        if mimg:
            close_list()
            body.append(r"\begin{figure}[htbp]" + "\n" + r"\centering" + "\n" +
                        r"\includegraphics[width=0.85\linewidth]{" + mimg.group(2) + "}" + "\n" +
                        r"\caption{" + inline(mimg.group(1)) + "}" + "\n" + r"\end{figure}")
            i += 1
            continue
        if l.startswith("```"):
            close_list()
            j = i + 1
            code = []
            while j < len(lines) and not lines[j].startswith("```"):
                code.append(lines[j])
                j += 1
            body.append(r"\begin{Verbatim}[fontsize=\small]")
            body.extend(code)
            body.append(r"\end{Verbatim}")
            i = j + 1
            continue
        if l.strip().startswith("$$"):
            close_list()
            buf = l.strip()
            j = i
            while not (buf.endswith("$$") and len(buf) > 2):
                j += 1
                buf += " " + lines[j].strip()
            eq = buf[2:-2].strip()
            if len(eq) > 100:
                body.append(r"\[\adjustbox{max width=\linewidth}{$\displaystyle " + eq + r"$}\]")
            else:
                body.append(r"\[" + eq + r"\]")
            i = j + 1
            continue
        if l.startswith("### "):
            close_list()
            body.append(heading("subsection", l[4:].strip()))
            i += 1
            continue
        if l.startswith("## "):
            close_list()
            body.append(heading("section", l[3:].strip()))
            i += 1
            continue
        if l.startswith("# "):
            close_list()
            body.append(r"\section*{" + inline(l[2:].strip()) + "}")
            i += 1
            continue
        if l.strip().startswith("|") and i + 1 < len(lines) and re.match(r"^\s*\|[\s\-|:]+\|\s*$", lines[i + 1]):
            close_list()
            j = i
            rows = []
            while j < len(lines) and lines[j].strip().startswith("|"):
                rows.append(lines[j])
                j += 1
            body.append(table(rows))
            i = j
            continue
        m = re.match(r"^(\* |\d+\. )(.*)$", l)
        if m:
            kind = "itemize" if m.group(1) == "* " else "enumerate"
            if in_list != kind:
                close_list()
                body.append(r"\begin{" + kind + "}")
                in_list = kind
            item = [m.group(2)]
            subs = []                    # nested '- ' bullets (indented), with their continuation lines
            j = i + 1
            while j < len(lines) and lines[j].startswith("  ") and lines[j].strip() and not lines[j].strip().startswith("$$"):
                sm = re.match(r"^\s+- (.*)$", lines[j])
                if sm:
                    subs.append([sm.group(1)])
                elif subs:
                    subs[-1].append(lines[j].strip())
                else:
                    item.append(lines[j].strip())
                j += 1
            text = r"\item " + inline(" ".join(item))
            if subs:
                text += "\n" + r"\begin{itemize}" + "\n" + "\n".join(r"\item " + inline(" ".join(s)) for s in subs) + "\n" + r"\end{itemize}"
            body.append(text)
            i = j
            continue
        if not l.strip():
            if in_list and i + 1 < len(lines) and re.match(r"^(\* |\d+\. |  )", lines[i + 1]):
                i += 1
                continue
            close_list()
            body.append("")
            i += 1
            continue
        if in_list and l.startswith("  "):
            body.append(inline(l.strip()))
            i += 1
            continue
        close_list()
        para = [l.strip()]
        j = i + 1
        while j < len(lines) and lines[j].strip() and not re.match(r"^(#|\* |\d+\. |\||```|\$\$|<!--|!\[)", lines[j].strip()):
            para.append(lines[j].strip())
            j += 1
        body.append(inline(" ".join(para)))
        i = j
    close_list()
    head = PREAMBLE
    if graphics_dir is not None:
        # image paths of the Markdown are relative to its folder; pdflatex runs from the repository root
        head += r"\graphicspath{{" + graphics_dir + "/}}\n"
    head += r"\title{" + inline(title or "") + "}\n" + r"\author{dirac16complex project (with Claude Opus 5.5)}" + "\n" + r"\date{}" + "\n"
    return head + "\\begin{document}\n\\maketitle\n\\tableofcontents\n\\newpage\n" + "\n".join(body) + "\n\\end{document}\n"


if __name__ == "__main__":
    src, dst = Path(sys.argv[1]), Path(sys.argv[2])
    title = sys.argv[3] if len(sys.argv) > 3 else None
    gdir = Path(os.path.relpath(src.resolve().parent)).as_posix()
    dst.write_text(convert(src.read_text(encoding="utf-8"), title, gdir), encoding="utf-8", newline="\n")
    print("wrote", dst)
