"""Fill D00.draft.md and write Revision/docs/DIRAC16COMPLEX00_FIELD_THEORY.md."""
import json
import re
import sys
from pathlib import Path

SP = Path(__file__).resolve().parent
sys.path.insert(0, str(SP))
import gen_d00_blocks as G  # noqa: E402

REV = Path(r"D:\Developer\github\Dirac_claude\Revision")
REPORTS = [
    "algebra/reports/wolfram-algebra.json",
    "algebra/reports/python-algebra.json",
    "theory/reports/wolfram-field-theory.json",
    "theory/reports/python-field-theory.json",
    "field_equations_a4/reports/wolfram-a4-report.json",
    "field_equations_a4/reports/python-a4-report.json",
    "pairing/reports/wolfram-pairing.json",
    "pairing/reports/python-pairing.json",
    "theory/reports/wolfram-scope.json",
    "theory/reports/python-scope.json",
    "dark_sector/dirac16complex00/reports/python-derive-eos.json",
    "dark_sector/dirac16complex00/reports/python-independent-numerics.json",
]
A4 = G.A4


def aligned(rows):
    return "$$\n\\begin{aligned}\n" + " \\\\\n".join(rows) + "\n\\end{aligned}\n$$"


def einstein_block():
    e = A4["einstein"]
    return aligned([
        "& " + e["constraint_x4"]["tex"] + ",",
        "& " + e["space_x1"]["tex"] + ",",
        "& " + e["hidden_x0"]["tex"] + " \\quad (x_0 = x_5 = x_6 = x_7),",
        "& " + e["nullEnergy_x0"]["tex"] + ",",
        "& " + e["nullEnergy_x1"]["tex"] + ".",
    ])


def exp_einstein_block():
    e = A4["exponentialHistory"]["einstein"]
    return aligned([
        "\\rho &= " + e["rho"]["tex"] + ",",
        "p_3 &= " + e["p3"]["tex"] + ",",
        "p_0 = p_t &= " + e["p0"]["tex"] + ".",
    ])


def history_block(key, end):
    h = A4["exponentialHistory"]["authorWeights"][key]
    assert h["p0"]["tex"] == h["pt"]["tex"]
    return aligned([
        "-\\kappa\\rho - \\Lambda &= " + h["minus_rho"]["tex"] + ",",
        "\\kappa p_3 - \\Lambda &= " + h["p3"]["tex"] + ",",
        "\\kappa p_0 - \\Lambda = \\kappa p_t - \\Lambda &= " + h["p0"]["tex"] + end,
    ])


def index_rows(text):
    checks = {}
    for rel in REPORTS:
        data = json.loads((REV / rel).read_text(encoding="utf-8"))
        checks[rel] = {c["name"]: c["verdict"] for c in data["checks"]}
    body = text.split("## 14. Check index", 1)[0] + text.split("## 15. What is not claimed", 1)[1]
    cited = []
    for token in re.findall(r"`([^`\s]+)`", body):
        if token not in cited:
            cited.append(token)
    rows, used = [], set()
    for rel in REPORTS:
        names = [t for t in cited if t in checks[rel]]
        for n in names:
            assert checks[rel][n] in ("PASS", "pass"), (rel, n)
            used.add(n)
        for k in range(0, len(names), 6):
            rows.append(f"| `Revision/{rel}` | " + ", ".join(f"`{n}`" for n in names[k:k + 6]) + " |")
    return rows, used, cited


def main():
    text = (SP / "D00.draft.md").read_text(encoding="utf-8")
    blocks = {
        "@@COMPONENTS@@": G.component_blocks(),
        "@@LOVELOCK@@": G.lovelock_blocks(),
        "@@OFFDIAG@@": G.offdiagonal_table(),
        "@@EINSTEIN@@": einstein_block(),
        "@@EXP_EINSTEIN@@": exp_einstein_block(),
        "@@HISTORY@@": history_block("historySource_kappaT_minus_Lam", ","),
        "@@EINSTEIN_HISTORY@@": history_block("einsteinHistorySource_kappaT_minus_Lam", ":"),
    }
    for key, value in blocks.items():
        assert text.count(key) == 1, key
        text = text.replace(key, value)
    rows, used, cited = index_rows(text)
    assert text.count("@@INDEX@@") == 1
    text = text.replace("@@INDEX@@", "\n".join(rows))
    assert "@@" not in text
    out = REV / "docs" / "DIRAC16COMPLEX00_FIELD_THEORY.md"
    out.write_text(text, encoding="utf-8", newline="\n")
    print("written", len(text), "index rows", len(rows), "cited checks", len(used))
    candidates = [t for t in cited if re.fullmatch(r"[A-Za-z][A-Za-z0-9_.]*_[A-Za-z0-9_.]*", t) and "/" not in t]
    print("tokens not in any report:", [t for t in candidates if t not in used])


if __name__ == "__main__":
    main()
