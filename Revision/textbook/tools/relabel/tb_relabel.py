"""Mechanical part of the relabel of the textbook (builders and chapters) to the author's coordinates x0..x7.

1. Enumerations of the directions from 1 to 8 (a token with index 1, an ellipsis, '..', 'to' or 'through', the same
   kind of token with index 8) are shifted: every index of a direction in the span goes down by one, so
   "x_1, x_2, \\dots, x_8" -> "x_0, x_1, \\dots, x_7", "(x_1, x_1), \\dots, (x_8, x_8)" -> "(x_0, x_0), \\dots, (x_7, x_7)",
   "x1->x2, ..., x8->x1" -> "x0->x1, ..., x7->x0", "g_{11} dx_1^2 + \\dots + g_{88} dx_8^2" -> "g_{00} dx_0^2 + ...".
2. Fixed lists in the old order -> the author's order (space-like sets, signs, code lists of names and symbols).
3. Every remaining label of the hidden direction 8 -> 0 (x8, x_8, g_88, gamma^(8), d_8, f_8, p8, P8, q48, q84, ...).
NOT done here: code that indexes arrays by position; such lines are listed for a manual review.
Usage: tb_relabel.py FILE... [--dry]"""
import re
import sys
from pathlib import Path

DRY = "--dry" in sys.argv
FILES = [Path(a) for a in sys.argv[1:] if a != "--dry"]

ELLIPSIS = "\\\\dots|\\\\ldots|\\\\cdots|\\.\\.\\.?|…|\\bto\\b|\\bthrough\\b"
# a token of a direction inside an enumeration: x_1, x_{1}, x1, dx_1
TOK = r"(?<![A-Za-z0-9])d?x_?\{?([1-8])\}?(?![0-9])"
# other indexed symbols of the eight directions: f_1, k_1, h_1, g_{11}, \gamma^{(1)}
OTHER = r"(?<![A-Za-z0-9])(?:f_|k_|h_)\{?[1-8]\}?(?![0-9])|g_\{[1-8][1-8]\}|\\gamma\^\{\([1-8]\)\}"
FIRST = r"(?:(?<![A-Za-z0-9])d?x_?\{?1\}?(?![0-9])|(?<![A-Za-z0-9])(?:f_|k_)\{?1\}?(?![0-9])|g_\{11\}|\\gamma\^\{\(1\)\})"
LAST = r"(?:(?<![A-Za-z0-9])d?x_?\{?8\}?(?![0-9])|(?<![A-Za-z0-9])(?:f_|k_)\{?8\}?(?![0-9])|g_\{88\} ?dx_8|\\gamma\^\{\(8\)\})"
ENUM = re.compile(FIRST + r"(?:[^.;:]{0,45}?)(?:" + ELLIPSIS + r")(?:[^.;:]{0,30}?)" + LAST
                  + r"(?:,\s*x_?\{?8\}?(?![0-9]))?" + r"(?:[^\s,.;]{0,12})")


def shift_span(span):
    """Lower every index of a direction in an enumeration span by one."""
    span = re.sub(TOK, lambda m: m.group(0).replace(m.group(1), str(int(m.group(1)) - 1), 1), span)
    return re.sub(OTHER, lambda m: re.sub(r"[1-8]", lambda d: str(int(d.group(0)) - 1), m.group(0)), span)


def shift_enumerations(text):
    out, pos, n = [], 0, 0
    for m in ENUM.finditer(text):
        span = m.group(0)
        # an enumeration has no further list of direction tokens after the ellipsis: "x1 to x3, 1 for x4, ..., for x8"
        parts = re.split(ELLIPSIS, span, maxsplit=1)
        if len(parts) == 2 and len(re.findall(TOK, parts[1])) > 2:
            continue
        out.append(text[pos:m.start()])
        out.append(shift_span(span))
        pos = m.end()
        n += 1
    out.append(text[pos:])
    return "".join(out), n


ORDERED = [
    (r"x_1, x_2, x_3, x_8", r"x_0, x_1, x_2, x_3"),
    (r"x_1,x_2,x_3,x_8", r"x_0,x_1,x_2,x_3"),
    (r"$x_1$, $x_2$, $x_3$, $x_8$", r"$x_0$, $x_1$, $x_2$, $x_3$"),
    (r"$x_1$, $x_2$, $x_3$ and $x_8$", r"$x_0$, $x_1$, $x_2$ and $x_3$"),
    (r"x_1, x_2, x_3 and x_8", r"x_0, x_1, x_2 and x_3"),
    (r"x1, x2, x3, x8", r"x0, x1, x2, x3"),
    (r"x1, x2, x3 and x8", r"x0, x1, x2 and x3"),
    (r"(+,+,+,-,-,-,-,+)", r"(+,+,+,+,-,-,-,-)"),
    (r"(+, +, +, -, -, -, -, +)", r"(+, +, +, +, -, -, -, -)"),
    (r"(+1,+1,+1,-1,-1,-1,-1,+1)", r"(+1,+1,+1,+1,-1,-1,-1,-1)"),
    (r"(+1, +1, +1, -1, -1, -1, -1, +1)", r"(+1, +1, +1, +1, -1, -1, -1, -1)"),
    (r"[1, 1, 1, -1, -1, -1, -1, 1]", r"[1, 1, 1, 1, -1, -1, -1, -1]"),
    (r"(1, 1, 1, -1, -1, -1, -1, 1)", r"(1, 1, 1, 1, -1, -1, -1, -1)"),
    (r"[1, 1, 1, -1, -1, -1, -1, +1]", r"[1, 1, 1, 1, -1, -1, -1, -1]"),
    ('sp.symbols("x1:9"', 'sp.symbols("x0:8"'),
    ('symbols("x1:9"', 'symbols("x0:8"'),
    ("x1, x2, x3, x4, x5, x6, x7, x8 = ", "x0, x1, x2, x3, x4, x5, x6, x7 = "),
    ("[x1, x2, x3, x4, x5, x6, x7, x8]", "[x0, x1, x2, x3, x4, x5, x6, x7]"),
    ("(x1, x2, x3, x4, x5, x6, x7, x8)", "(x0, x1, x2, x3, x4, x5, x6, x7)"),
    ('["x1", "x2", "x3", "x4", "x5", "x6", "x7", "x8"]', '["x0", "x1", "x2", "x3", "x4", "x5", "x6", "x7"]'),
    ('("x1", "x2", "x3", "x4", "x5", "x6", "x7", "x8")', '("x0", "x1", "x2", "x3", "x4", "x5", "x6", "x7")'),
    ('[f"x{k}" for k in range(1, 9)]', '[f"x{k}" for k in range(8)]'),
    ('[f"x{i}" for i in range(1, 9)]', '[f"x{i}" for i in range(8)]'),
    ('[f"$x_{k}$" for k in range(1, 9)]', '[f"$x_{k}$" for k in range(8)]'),
    ('[f"$x_{{{k}}}$" for k in range(1, 9)]', '[f"$x_{{{k}}}$" for k in range(8)]'),
]
TOKENS = [
    ("\\gamma^{(8)}", "\\gamma^{(0)}"), ("\\gamma^8", "\\gamma^0"),
    ("e^{(8)}", "e^{(0)}"), ("(i)(8)", "(i)(0)"), ("(t)(8)", "(t)(0)"),
    ("\\partial_8", "\\partial_0"), ("g_{88}", "g_{00}"), ("g^{88}", "g^{00}"), ("\\tau_8", "\\tau_0"),
    ("q_{48}", "q_{40}"), ("q_{84}", "q_{04}"), ("B_{48}", "B_{40}"), ("B_{84}", "B_{04}"),
]
REGEX = [
    (r"(?<![A-Za-z0-9])int_p8(?![0-9])", "int_p0"),
    (r"(?<![A-Za-z0-9])p8_", "p0_"),
    (r"(?<![A-Za-z0-9_])p8(?![0-9])", "p0"),
    (r"(?<![A-Za-z0-9_])P8(?![0-9])", "P0"),
    (r"(?<![A-Za-z0-9])q48(?![0-9])", "q40"),
    (r"(?<![A-Za-z0-9])q84(?![0-9])", "q04"),
    (r"(?<![A-Za-z0-9\\])p_8(?![0-9])", "p_0"),
    (r"(?<![A-Za-z0-9\\])P_8(?![0-9])", "P_0"),
    (r"(?<![A-Za-z0-9\\])f_8(?![0-9])", "f_0"),
    (r"(?<![A-Za-z0-9\\])k_8(?![0-9])", "k_0"),
    (r"(?<![A-Za-z0-9\\])q_8(?![0-9])", "q_0"),
    (r"(?<![A-Za-z0-9_])q8(?![0-9])", "q0"),
    (r"\\eta_\{88\}", r"\\eta_{00}"),
    (r"\\eta\^\{88\}", r"\\eta^{00}"),
    (r"(?<=\\partial_[0-9])f_8(?![0-9])", "f_0"),
    # compound plane labels written without a separator: x1x8, x_ix8, x4x8, S^{x_tx8}
    (r"(?<=x[0-9])x8(?![0-9])", "x0"),
    (r"(?<=x_[a-z])x8(?![0-9])", "x0"),
    (r"x_8(?![0-9])", "x_0"),
    (r"x_\{8\}", "x_{0}"),
    (r"x8x8", "x0x0"),
    (r"(?<![A-Za-z0-9])x8(?![0-9])", "x0"),
]
NAME_MAP = {
    "Omega_x4_Omega_x8_vanish": "Omega_x0_Omega_x4_vanish",
    "Omega_x4_and_Omega_x8_vanish": "Omega_x0_and_Omega_x4_vanish",
    "ownrep_Omega_x4_x8_zero": "ownrep_Omega_x0_x4_zero",
    "authorT16_Omega_x4_x8_zero": "authorT16_Omega_x0_x4_zero",
    "off_diagonal_entries_x4_x8_only": "off_diagonal_entries_x0_x4_only",
    "gamma_Omega_equals_3H_gamma8": "gamma_Omega_equals_3H_gamma0",
}
REVIEW = re.compile(r"sp\.diag\(|np\.diag\(|\[7\]|range\(1, ?9\)|\bk \+ 1\b|\bk - 1\b|eta\[|ETA\[|"
                    r"\[1:8\]|\[0:7\]|\[:7\]|\.index\(|\[3\]|\bcot\b.*\*\* ?2\)\s*$|COORD|ROLE|x_0 to x_1\b|x0 to x1\b")


DIAG_HEAD = re.compile(r"diag\}?\s*(?:\\bigl?|\\left)?\(")
LAST_COT = re.compile(r"^\s*(?:\\cot\^\{?2\}?\s*\(?z\)?|\\cot\^2\s*\(6\s*H\s*x_?\{?[08]\}?\)|sp\.cot\([^()]*\)\s*\*\*\s*2"
                      r"|cot\^2 ?z|cot\(z\)\^2)\s*$")


def cot_first(text):
    """In every diag(...) of eight entries whose last entry is cot^2 z, move that entry to the front."""
    out, pos, n = [], 0, 0
    for m in DIAG_HEAD.finditer(text):
        if m.start() < pos:
            continue
        start, depth, i = m.end(), 1, m.end()
        while i < len(text) and depth:
            if text[i] == "(":
                depth += 1
            elif text[i] == ")":
                depth -= 1
            i += 1
        if depth:
            continue
        close = i - 1
        for suffix in ("\\bigr", "\\big", "\\right"):
            if text[close - len(suffix):close] == suffix:
                close -= len(suffix)
                break
        inner = text[start:close]
        items, d, cur = [], 0, ""
        for ch in inner:
            if ch in "({[":
                d += 1
            elif ch in ")}]":
                d -= 1
            if ch == "," and d == 0:
                items.append(cur)
                cur = ""
            else:
                cur += ch
        items.append(cur)
        if len(items) != 8 or not LAST_COT.match(items[-1]):
            continue
        body = inner.rstrip()
        trail = inner[len(body):]
        last = items[-1].strip()
        lead = re.match(r"\s*", items[0]).group(0)
        rest = body[:body.rstrip().rfind(",")]  # everything before the last comma
        rest_core = rest[len(lead):]
        new_inner = lead + last + ", " + rest_core + trail
        out.append(text[pos:start])
        out.append(new_inner)
        pos = close
        n += 1
    out.append(text[pos:])
    return "".join(out), n


def relabel(text):
    for old, new in NAME_MAP.items():
        text = text.replace(old, new)
    text, n = shift_enumerations(text)
    text, n_diag = cot_first(text)
    n += n_diag
    for a, b in ORDERED:
        text = text.replace(a, b)
    for a, b in TOKENS:
        text = text.replace(a, b)
    for a, b in REGEX:
        text = re.sub(a, b, text)
    return text, n


if __name__ == "__main__":
    for f in FILES:
        old = f.read_text(encoding="utf-8")
        new, n_enum = relabel(old)
        review = [(i + 1, b.strip()[:150]) for i, (a, b) in enumerate(zip(old.split("\n"), new.split("\n")))
                  if REVIEW.search(b)]
        n_changed = sum(1 for a, b in zip(old.split("\n"), new.split("\n")) if a != b)
        print(f"{f.name}: {n_changed} lines changed, {n_enum} enumerations shifted; {len(review)} lines to review")
        for i, l in review:
            print(f"   REVIEW {i}: {l}")
        if not DRY and new != old:
            f.write_bytes(new.encode("utf-8"))
