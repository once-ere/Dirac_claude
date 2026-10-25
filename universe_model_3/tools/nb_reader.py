#!/usr/bin/env python3
"""nb_reader.py - read a Wolfram (Mathematica) notebook file (.nb) without Mathematica.

A .nb file is a plain-text Wolfram Language expression Notebook[{Cell[...], ...}, options].
This module parses that expression (strings, numbers, symbols, Head[args], {lists}, Rule ->,
RuleDelayed :>), walks the cell tree (CellGroupData keeps the Section/Subsection grouping) and
converts the box structures of input cells (RowBox, SuperscriptBox, FractionBox, GridBox, ...)
into linear Wolfram Language input text, so that the cells can be read, quoted and evaluated
by an independent emulator.

Nothing is evaluated here and nothing in the notebook is modified.

Usage:
    python nb_reader.py NOTEBOOK.nb --dump OUT.txt      # every cell, in order, as text
    python nb_reader.py NOTEBOOK.nb --json OUT.json     # every cell as a JSON record
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from dataclasses import dataclass, field
from typing import Any

# ----------------------------------------------------------------------------------------------
# 1. Tokenizer and parser of the notebook expression
# ----------------------------------------------------------------------------------------------


@dataclass
class Sym:
    name: str

    def __repr__(self) -> str:  # pragma: no cover - debugging aid
        return self.name


@dataclass
class Str:
    raw: str  # the characters between the quotes, escapes kept as in the file

    def __repr__(self) -> str:  # pragma: no cover
        return '"' + self.raw[:40] + '"'


@dataclass
class Num:
    text: str

    def __repr__(self) -> str:  # pragma: no cover
        return self.text


@dataclass
class Expr:
    head: Any
    args: list = field(default_factory=list)

    def hname(self) -> str:
        return self.head.name if isinstance(self.head, Sym) else ""

    def __repr__(self) -> str:  # pragma: no cover
        return f"{self.head!r}[{len(self.args)} args]"


class ParseError(Exception):
    pass


_SYM_START = re.compile(r"[A-Za-z$`]")
_SYM_CHARS = re.compile(r"[A-Za-z0-9$`]*")
_NUM = re.compile(r"(\d+\.?\d*|\.\d+)(`[\d.]*)?(\*\^-?\d+)?")


class Parser:
    def __init__(self, text: str):
        self.s = text
        self.i = 0
        self.n = len(text)

    # -- lexical helpers ------------------------------------------------------------------------
    def _skip_ws(self) -> None:
        s, n = self.s, self.n
        while self.i < n:
            c = s[self.i]
            if c in " \t\r\n":
                self.i += 1
            elif c == "\\" and self.i + 1 < n and s[self.i + 1] in "\r\n":
                self.i += 2  # line continuation between tokens
            elif c == "(" and self.i + 1 < n and s[self.i + 1] == "*":
                depth = 0
                while self.i < n:
                    if s.startswith("(*", self.i):
                        depth += 1
                        self.i += 2
                    elif s.startswith("*)", self.i):
                        depth -= 1
                        self.i += 2
                        if depth == 0:
                            break
                    else:
                        self.i += 1
            else:
                break

    def _peek(self) -> str:
        self._skip_ws()
        return self.s[self.i] if self.i < self.n else ""

    def _string(self) -> Str:
        assert self.s[self.i] == '"'
        self.i += 1
        start = self.i
        s, n = self.s, self.n
        while self.i < n:
            c = s[self.i]
            if c == "\\":
                self.i += 2
            elif c == '"':
                raw = s[start:self.i]
                self.i += 1
                return Str(raw)
            else:
                self.i += 1
        raise ParseError("unterminated string")

    # -- grammar --------------------------------------------------------------------------------
    def parse(self) -> Any:
        e = self.expr()
        return e

    def expr(self) -> Any:
        left = self.postfix()
        c = self._peek()
        if self.s.startswith("->", self.i):
            self.i += 2
            right = self.expr()
            return Expr(Sym("Rule"), [left, right])
        if self.s.startswith(":>", self.i):
            self.i += 2
            right = self.expr()
            return Expr(Sym("RuleDelayed"), [left, right])
        if c == "&":
            self.i += 1
            return Expr(Sym("Function"), [left])
        return left

    def postfix(self) -> Any:
        a = self.atom()
        while self._peek() == "[":
            self.i += 1
            args = self.seq("]")
            a = Expr(a, args)
        return a

    def seq(self, close: str) -> list:
        args: list = []
        if self._peek() == close:
            self.i += 1
            return args
        while True:
            args.append(self.expr())
            c = self._peek()
            if c == ",":
                self.i += 1
                continue
            if c == close:
                self.i += 1
                return args
            raise ParseError(f"expected , or {close} at {self.i}: {self.s[self.i:self.i+60]!r}")

    def atom(self) -> Any:
        c = self._peek()
        if c == '"':
            return self._string()
        if c == "{":
            self.i += 1
            return Expr(Sym("List"), self.seq("}"))
        if c == "-" and not self.s.startswith("->", self.i):
            self.i += 1
            a = self.atom()
            if isinstance(a, Num):
                return Num("-" + a.text)
            return Expr(Sym("Times"), [Num("-1"), a])
        if c == "#":
            self.i += 1
            m = re.compile(r"\d*").match(self.s, self.i)
            self.i = m.end()
            return Sym("#" + m.group(0))
        if c.isdigit() or (c == "." and self.i + 1 < self.n and self.s[self.i + 1].isdigit()):
            m = _NUM.match(self.s, self.i)
            self.i = m.end()
            return Num(m.group(0))
        if _SYM_START.match(c or " "):
            m = _SYM_CHARS.match(self.s, self.i)
            self.i = m.end()
            return Sym(m.group(0))
        raise ParseError(f"unexpected {c!r} at {self.i}: {self.s[self.i:self.i+80]!r}")


def parse_notebook(path: str) -> Expr:
    text = open(path, encoding="utf-8", errors="strict").read()
    k = text.find("Notebook[")
    if k < 0:
        raise ParseError("no Notebook[ in file")
    p = Parser(text)
    p.i = k
    return p.parse()


# ----------------------------------------------------------------------------------------------
# 2. Strings: notebook escapes
# ----------------------------------------------------------------------------------------------

_NAMED = {
    # the named characters that occur in the author's notebooks; others are kept as \[Name]
    "IndentingNewLine": "\n", "NewLine": "\n", "LineSeparator": "\n",
    "InvisibleSpace": "", "InvisibleTimes": " ", "InvisibleApplication": "",
    "NonBreakingSpace": " ", "VeryThinSpace": " ", "ThinSpace": " ", "MediumSpace": " ",
    "ThickSpace": " ", "Times": "*", "Cross": "\\[Cross]", "Rule": "->", "RuleDelayed": ":>",
    "Equal": "==", "LongEqual": "==", "NotEqual": "!=", "LessEqual": "<=", "GreaterEqual": ">=",
    "DifferentialD": "d", "PartialD": "\\[PartialD]", "ImaginaryI": "I", "ExponentialE": "E",
    "Function": "&", "Element": "\\[Element]",
}


def unescape(raw: str, keep_named: bool = True) -> str:
    """Characters of a notebook string, with \\< \\> removed and \\" \\\\ \\n resolved."""
    out = []
    i, n = 0, len(raw)
    while i < n:
        c = raw[i]
        if c == "\\" and i + 1 < n:
            d = raw[i + 1]
            if d in "<>":
                i += 2
                continue
            if d == "\n":  # line continuation
                i += 2
                continue
            if d == "\r" and i + 2 < n and raw[i + 2] == "\n":
                i += 3
                continue
            if d == '"':
                out.append('"'); i += 2; continue
            if d == "\\":
                out.append("\\"); i += 2; continue
            if d == "n":
                out.append("\n"); i += 2; continue
            if d == "t":
                out.append("\t"); i += 2; continue
            if d == "[":
                j = raw.find("]", i)
                name = raw[i + 2:j]
                if name in _NAMED and not (keep_named and name in ("PartialD", "Element", "Cross")):
                    out.append(_NAMED[name])
                else:
                    out.append("\\[" + name + "]")
                i = j + 1
                continue
            if d == ":":
                out.append(chr(int(raw[i + 2:i + 6], 16))); i += 6; continue
            if d == ".":
                out.append(chr(int(raw[i + 2:i + 4], 16))); i += 4; continue
            if d == "|":
                out.append(chr(int(raw[i + 2:i + 8], 16))); i += 8; continue
            out.append(d); i += 2; continue
        out.append(c)
        i += 1
    return "".join(out)


# ----------------------------------------------------------------------------------------------
# 3. Boxes -> linear input text
# ----------------------------------------------------------------------------------------------

_INFIX_TIGHT = {"^", "_"}


def _paren(t: str) -> str:
    t = t.strip()
    if re.fullmatch(r"[A-Za-z0-9$`\\\[\]#.]+", t) or (t.startswith("(") and t.endswith(")") and _balanced(t[1:-1])):
        return t
    return "(" + t + ")"


def _balanced(t: str) -> bool:
    d = 0
    for ch in t:
        if ch in "([{":
            d += 1
        elif ch in ")]}":
            d -= 1
            if d < 0:
                return False
    return d == 0


def boxes_to_text(b: Any) -> str:
    """Linear Wolfram Language text of a box expression (input-form reading)."""
    if isinstance(b, Str):
        return unescape(b.raw)
    if isinstance(b, Num):
        return b.text
    if isinstance(b, Sym):
        return b.name
    if not isinstance(b, Expr):
        return str(b)
    h = b.hname()
    a = b.args
    if h == "List":
        return "".join(boxes_to_text(x) for x in a)
    if h == "RowBox":
        return "".join(boxes_to_text(x) for x in a[0].args) if a and isinstance(a[0], Expr) else ""
    if h == "BoxData":
        if a and isinstance(a[0], Expr) and a[0].hname() == "List":
            return "\n".join(boxes_to_text(x) for x in a[0].args)
        return boxes_to_text(a[0]) if a else ""
    if h == "SuperscriptBox":
        base, sup = boxes_to_text(a[0]), boxes_to_text(a[1])
        if sup.strip() in ("\\[Prime]", "′"):
            return base + "'"
        if sup.strip() in ("\\[Prime]\\[Prime]", "′′"):
            return base + "''"
        if sup.strip() in ("\\[Dagger]", "†"):
            return "SuperDagger[" + base + "]"
        if sup.strip() == "T":
            return "Transpose[" + base + "]"
        return _paren(base) + "^" + _paren(sup)
    if h == "SubscriptBox":
        return "Subscript[" + boxes_to_text(a[0]) + ", " + boxes_to_text(a[1]) + "]"
    if h == "SubsuperscriptBox":
        return ("Subsuperscript[" + boxes_to_text(a[0]) + ", " + boxes_to_text(a[1]) + ", "
                + boxes_to_text(a[2]) + "]")
    if h == "FractionBox":
        return _paren(boxes_to_text(a[0])) + "/" + _paren(boxes_to_text(a[1]))
    if h == "SqrtBox":
        return "Sqrt[" + boxes_to_text(a[0]) + "]"
    if h == "RadicalBox":
        return _paren(boxes_to_text(a[0])) + "^(1/" + _paren(boxes_to_text(a[1])) + ")"
    if h == "OverscriptBox":
        return "Overscript[" + boxes_to_text(a[0]) + ", " + boxes_to_text(a[1]) + "]"
    if h == "UnderscriptBox":
        return "Underscript[" + boxes_to_text(a[0]) + ", " + boxes_to_text(a[1]) + "]"
    if h == "UnderoverscriptBox":
        return ("Underoverscript[" + boxes_to_text(a[0]) + ", " + boxes_to_text(a[1]) + ", "
                + boxes_to_text(a[2]) + "]")
    if h in ("StyleBox", "FormBox", "AdjustmentBox", "ItemBox", "PaneBox", "FrameBox",
             "PanelBox", "ButtonBox", "TooltipBox", "Cell", "TextData", "PaneSelectorBox"):
        return boxes_to_text(a[0]) if a else ""
    if h == "TagBox":
        inner = a[0] if a else Str("")
        return boxes_to_text(inner)
    if h == "InterpretationBox":
        return boxes_to_text(a[0]) if a else ""
    if h == "TemplateBox":
        args = a[0].args if a and isinstance(a[0], Expr) and a[0].hname() == "List" else []
        name = unescape(a[1].raw) if len(a) > 1 and isinstance(a[1], Str) else ""
        if name == "NotationTemplateTag" and args:
            return boxes_to_text(args[0])
        if name in ("Superscript",) and len(args) == 2:
            return _paren(boxes_to_text(args[0])) + "^" + _paren(boxes_to_text(args[1]))
        if name in ("Subscript",) and len(args) == 2:
            return "Subscript[" + boxes_to_text(args[0]) + ", " + boxes_to_text(args[1]) + "]"
        if name in ("RowDefault", "RowWithSeparators", "RowWithSeparator") :
            return "".join(boxes_to_text(x) for x in args)
        if name == "Conjugate" and args:
            return "Conjugate[" + boxes_to_text(args[0]) + "]"
        if name == "Abs" and args:
            return "Abs[" + boxes_to_text(args[0]) + "]"
        return name + "[" + ", ".join(boxes_to_text(x) for x in args) + "]"
    if h == "GridBox":
        rows = a[0].args if a and isinstance(a[0], Expr) else []
        out = []
        for r in rows:
            if isinstance(r, Expr) and r.hname() == "List":
                out.append("{" + ", ".join(boxes_to_text(x) for x in r.args) + "}")
            else:
                out.append(boxes_to_text(r))
        return "{" + ", ".join(out) + "}"
    if h == "DynamicBox":
        return "<Dynamic>"
    if h in ("GraphicsBox", "Graphics3DBox"):
        return "<Graphics>"
    if h == "DynamicModuleBox":
        return "<DynamicModule>"
    # unknown box: show its head and arguments
    return (b.hname() or "?") + "[" + ", ".join(boxes_to_text(x) for x in a) + "]"


def textdata_to_text(td: Any) -> str:
    if isinstance(td, Str):
        return unescape(td.raw)
    if isinstance(td, Expr):
        h = td.hname()
        if h == "List":
            return "".join(textdata_to_text(x) for x in td.args)
        if h == "TextData":
            return textdata_to_text(td.args[0]) if td.args else ""
        if h == "StyleBox":
            return textdata_to_text(td.args[0]) if td.args else ""
        if h == "Cell":  # inline cell
            return "$" + boxes_to_text(td.args[0]) + "$" if td.args else ""
        if h == "ButtonBox":
            return textdata_to_text(td.args[0]) if td.args else ""
        return boxes_to_text(td)
    return str(td)


# ----------------------------------------------------------------------------------------------
# 4. The cell walk
# ----------------------------------------------------------------------------------------------

@dataclass
class CellRec:
    index: int            # running number of the cell in the file (0-based)
    style: str            # "Input", "Output", "Text", "Section", ...
    label: str            # CellLabel ("In[12]:=") or ""
    path: list            # titles of the enclosing Title/Section/Subsection/... cells
    text: str             # linear text of the content
    raw_kind: str         # "BoxData", "TextData", "String", ...
    content: Any = None   # the parsed content expression (not serialised)

    def as_json(self) -> dict:
        return {"index": self.index, "style": self.style, "label": self.label,
                "path": self.path, "kind": self.raw_kind, "text": self.text}


_HEADING_LEVEL = {"Title": 0, "Subtitle": 1, "Chapter": 1, "Section": 2, "Subsection": 3,
                  "Subsubsection": 4, "Subsubsubsection": 5}


def _opt(cell: Expr, name: str) -> Any:
    for x in cell.args[1:]:
        if isinstance(x, Expr) and x.hname() in ("Rule", "RuleDelayed") and isinstance(x.args[0], Sym) \
                and x.args[0].name == name:
            return x.args[1]
    return None


def walk_cells(nb: Expr) -> list[CellRec]:
    out: list[CellRec] = []
    stack: list[tuple[int, str]] = []

    def visit(cell: Any) -> None:
        if not (isinstance(cell, Expr) and cell.hname() == "Cell"):
            return
        first = cell.args[0] if cell.args else None
        if isinstance(first, Expr) and first.hname() == "CellGroupData":
            group = first.args[0].args if first.args and isinstance(first.args[0], Expr) else []
            depth = len(stack)
            for c in group:
                visit(c)
            del stack[depth:]
            return
        style = ""
        if len(cell.args) > 1 and isinstance(cell.args[1], Str):
            style = unescape(cell.args[1].raw)
        lab = _opt(cell, "CellLabel")
        label = unescape(lab.raw) if isinstance(lab, Str) else ""
        if isinstance(first, Str):
            text, kind = unescape(first.raw), "String"
        elif isinstance(first, Expr) and first.hname() == "BoxData":
            text, kind = boxes_to_text(first), "BoxData"
        elif isinstance(first, Expr) and first.hname() == "TextData":
            text, kind = textdata_to_text(first), "TextData"
        else:
            text, kind = boxes_to_text(first), (first.hname() if isinstance(first, Expr) else "other")
        if style in _HEADING_LEVEL:
            lvl = _HEADING_LEVEL[style]
            while stack and stack[-1][0] >= lvl:
                stack.pop()
            path = [t for _, t in stack]
            out.append(CellRec(len(out), style, label, path, text, kind, first))
            stack.append((lvl, " ".join(text.split())))
        else:
            out.append(CellRec(len(out), style, label, [t for _, t in stack], text, kind, first))

    top = nb.args[0].args if nb.args and isinstance(nb.args[0], Expr) else []
    for c in top:
        visit(c)
    return out


def sha256(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("notebook")
    ap.add_argument("--dump", help="write every cell as text to this file")
    ap.add_argument("--json", help="write every cell as JSON to this file")
    ap.add_argument("--max-output", type=int, default=600,
                    help="truncate Output cells to this many characters in --dump (0 = no limit)")
    args = ap.parse_args(argv)
    nb = parse_notebook(args.notebook)
    cells = walk_cells(nb)
    digest = sha256(args.notebook)
    if args.json:
        with open(args.json, "w", encoding="utf-8") as f:
            json.dump({"notebook": args.notebook.replace("\\", "/").split("/")[-1], "sha256": digest,
                       "cells": [c.as_json() for c in cells]}, f, indent=1, ensure_ascii=False)
    if args.dump:
        with open(args.dump, "w", encoding="utf-8") as f:
            f.write(f"# {args.notebook}  sha256 {digest}  cells {len(cells)}\n")
            for c in cells:
                t = c.text
                if c.style == "Output" and args.max_output and len(t) > args.max_output:
                    t = t[:args.max_output] + f" ...[{len(c.text)} chars]"
                where = " / ".join(c.path)
                f.write(f"\n=== [{c.index}] {c.style} {c.label}  <{where}>\n{t}\n")
    print(f"cells={len(cells)} sha256={digest}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
