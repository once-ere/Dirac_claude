"""Generated formula blocks of DIRAC16COMPLEX00_FIELD_THEORY.md (corrected metric, version 2).

Every block is made from the Revision records; the publication test re-generates the same lines.
"""
import json
import re
from pathlib import Path

REV = Path(r"D:\Developer\github\Dirac_claude\Revision")
FT = json.loads((REV / "theory/field-theory.json").read_text(encoding="utf-8"))
A4 = json.loads((REV / "field_equations_a4/a4-equations.json").read_text(encoding="utf-8"))


def formula(key):
    for entry in FT["formulas"]:
        if entry["key"] == key:
            return entry["wl"]
    raise KeyError(key)


GRAVITY = r"\(-1/2\*Derivative\[1\]\[a4\]\[x4\] \+ Derivative\[1\]\[b4\]\[x4\]/b4\[x4\]\)"
TERM_PATTERNS = (
    ("x4", re.compile(r'^dd\["x4", Psi\[(\d+)\]\]$')),
    ("mass", re.compile(r"^\(3\*E\^a4\[x4\]\*H\*Psi\[(\d+)\]\)/\(2\*Sqrt\[b4\[x4\]\]\)$")),
    ("space", re.compile(r'^dd\["x([123])", Psi\[(\d+)\]\]/E\^a4\[x4\]$')),
    ("time", re.compile(
        r'^\(E\^a4\[x4\]\*dd\["x([567])", Psi\[(\d+)\]\]\)/\(Sqrt\[b4\[x4\]\]\*\(Sin\[6\*H\*x0\]\^2\)\^\(1/12\)\)$')),
    ("hidden", re.compile(r'^\(E\^a4\[x4\]\*dd\["x0", Psi\[(\d+)\]\]\*Tan\[6\*H\*x0\]\)/Sqrt\[b4\[x4\]\]$')),
    ("b4", re.compile(r"^Psi\[(\d+)\]\*" + GRAVITY + "$")),
)


def top_level_terms(text):
    """Split a Wolfram InputForm sum at the separators ' + ' and ' - ' outside brackets."""
    pieces, depth, start, i = [], 0, 0, 0
    while i < len(text):
        ch = text[i]
        if ch in "([":
            depth += 1
        elif ch in ")]":
            depth -= 1
        elif depth == 0 and text.startswith((" + ", " - "), i):
            pieces.append(text[start:i])
            start = i + 1
            i += 2
            continue
        i += 1
    pieces.append(text[start:])
    return pieces


def parse_component_equation(text):
    lhs, rhs = text.split(" == ")
    target = re.fullmatch(r"V\*Psi\[(\d+)\]", rhs)
    if target is None:
        raise ValueError(rhs)
    pieces = top_level_terms(lhs.strip())
    terms = {"space": {}, "time": {}}
    for piece in pieces:
        sign = 1
        piece = piece.strip()
        if piece.startswith("+ "):
            piece = piece[2:]
        elif piece.startswith("- "):
            sign, piece = -1, piece[2:]
        elif piece.startswith("-"):
            sign, piece = -1, piece[1:]
        if piece.startswith("(") and piece.endswith(")") and piece.count("(") == 1 + piece[1:-1].count("("):
            inner = piece[1:-1]
            if re.fullmatch(r'dd\["x[123]", Psi\[\d+\]\]/E\^a4\[x4\]', inner):
                piece = inner
        for kind, pattern in TERM_PATTERNS:
            match = pattern.fullmatch(piece)
            if match is None:
                continue
            if kind in ("space", "time"):
                terms[kind][int(match.group(1))] = (sign, int(match.group(2)))
            else:
                terms[kind] = (sign, int(match.group(1)))
            break
        else:
            raise ValueError(f"unrecognised term {piece!r}")
    terms["target"] = int(target.group(1))
    return terms


def signed(sign, body, first):
    if first:
        return ("-" if sign < 0 else "") + body
    return (" - " if sign < 0 else " + ") + body


def component_lines():
    lines = []
    for text in formula("field_equation_components"):
        t = parse_component_equation(text)
        assert t["mass"] == (1, t["hidden"][1]) and t["hidden"][0] == 1, t
        assert t["b4"] == t["x4"], t
        s4, i4 = t["x4"]
        space = "".join(signed(t["space"][d][0], rf"\partial_{d}\Phi_{{{t['space'][d][1]}}}", d == 1) for d in (1, 2, 3))
        time = "".join(signed(t["time"][d][0], rf"\partial_{d}\Phi_{{{t['time'][d][1]}}}", d == 5) for d in (5, 6, 7))
        first = (rf"({t['target']})\;\; & " + signed(s4, rf"\hat\partial_4\Phi_{{{i4}}}", True)
                 + rf" + \epsilon_s\,({space}) \\")
        second = (rf"& + \epsilon_t\,({time}) + \epsilon_0\,(t\,\partial_0 + \tfrac32H)\,\Phi_{{{t['hidden'][1]}}}"
                  + rf" = V\,\Phi_{{{t['target']}}}")
        lines.append((first, second))
    return lines


def component_blocks():
    rows = component_lines()
    assert len(rows) == 16
    blocks = []
    for start in range(0, 16, 4):
        body = []
        for k, (first, second) in enumerate(rows[start:start + 4]):
            body.append(first)
            body.append(second + (r" \\" if k < 3 else ""))
        blocks.append("$$\n\\begin{aligned}\n" + "\n".join(body) + "\n\\end{aligned}\n$$")
    return "\n\n".join(blocks)


def split_terms(tex):
    """Split a tex sum at top-level + and - signs (not inside braces or parentheses)."""
    terms, depth, current = [], 0, ""
    for i, ch in enumerate(tex):
        if ch in "{(":
            depth += 1
        elif ch in "})":
            depth -= 1
        if ch in "+-" and depth == 0 and current.strip() and not current.rstrip().endswith(("^", "_")):
            terms.append(current)
            current = ch
        else:
            current += ch
    terms.append(current)
    return terms


def wrapped(label, tex, per_row, end):
    terms = split_terms(tex)
    rows = []
    for k in range(0, len(terms), per_row):
        rows.append("".join(terms[k:k + per_row]))
    out = [f"{label} &= {rows[0]}"]
    for row in rows[1:]:
        out.append(f"&\\quad {row}")
    return " \\\\\n".join(out) + end


def lovelock_blocks():
    t = A4["lovelockTensors"]
    blocks = []
    for k, per_row in (("E1", 6), ("E2", 4), ("E3", 4)):
        n = k[1]
        assert t[k]["x5x5"]["tex"] == t[k]["x0x0"]["tex"], k
        parts = []
        for c, idx in (("x0x0", "x_0"), ("x1x1", "x_1"), ("x4x4", "x_4")):
            label = f"E_{{({n})}}{{}}^{{{idx}}}{{}}_{{{idx}}}"
            parts.append(wrapped(label, t[k][c]["tex"], per_row, "," if c != "x4x4" else "."))
        blocks.append("$$\n\\begin{aligned}\n" + " \\\\\n".join(parts) + "\n\\end{aligned}\n$$")
    return "\n\n".join(blocks)


SPACE = ("x1", "x2", "x3")
EXTRA_TIMES = ("x5", "x6", "x7")


def index_class(index):
    if index in SPACE:
        return "x_i"
    if index in EXTRA_TIMES:
        return "x_t"
    return "x_" + index[1:]


def notation(tex):
    return (tex.replace(r"\cot z^2", r"\cot^2 z").replace(r"\left(\sin z^2-1\right)", r"\left(\sin^2 z-1\right)")
            .replace(r"+1} H", r"+1}\, H"))


def offdiagonal_rows():
    entries = A4["fields"]["dirac16complex00"]["offDiagonalKinetic"]
    groups, sizes = {}, {}
    for entry in entries:
        upper, lower = re.fullmatch(r"K\^(x\d)_(x\d) \(symmetrised\)", entry["component"]).groups()
        value = []
        for term in entry["terms"]:
            pattern = term["bilinear"]
            for index in (upper, lower):
                if index in SPACE + EXTRA_TIMES:
                    pattern = pattern.replace(f"gamma^{index} ", f"gamma^{index_class(index)} ")
            assert not re.search(r"gamma\^x[1235-7] ", pattern), (entry, pattern)
            value.append((pattern, notation(term["coefficient"]["tex"])))
        key = (index_class(upper), index_class(lower))
        assert groups.setdefault(key, value) == value, key
        sizes[key] = sizes.get(key, 0) + 1
    assert sum(sizes.values()) == 36, sizes
    rows = []
    for (upper, lower), value in groups.items():
        for pattern, coefficient in value:
            latex = (pattern.replace("Phibar ", r"\bar\Phi ").replace(" Phi", r" \Phi")
                     .replace("gamma^x_i", r"\gamma^{x_i}").replace("gamma^x_t", r"\gamma^{x_t}")
                     .replace("gamma^x4", r"\gamma^{x_4}").replace("gamma^x0", r"\gamma^{x_0}"))
            rows.append((rf"$K^{{{upper}}}{{}}_{{{lower}}}$", f"${latex}$", f"${coefficient}$"))
    return rows


def offdiagonal_table():
    lines = ["| component: bilinear | coefficient |", "| --- | --- |"]
    lines += [f"| {a}: {b} | {c} |" for a, b, c in offdiagonal_rows()]
    return "\n".join(lines)


if __name__ == "__main__":
    out = Path(__file__).resolve().parent / "d00_blocks.json"
    blocks = {"@@COMPONENTS@@": component_blocks(), "@@LOVELOCK@@": lovelock_blocks(),
              "@@OFFDIAG@@": offdiagonal_table()}
    out.write_text(json.dumps(blocks, indent=1), encoding="utf-8")
    for k, v in blocks.items():
        print(k, len(v))
    print(blocks["@@OFFDIAG@@"])
    print(blocks["@@COMPONENTS@@"][:900])
