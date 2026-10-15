"""11b builder: the author's coordinates x0..x7 (the record's NAMES are in that order)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from relabel_common import REPO, strict_replace  # noqa: E402

p = REPO / "Revision/textbook/notebooks/src/11b_lovelock_tensors.py"
s = p.read_text(encoding="utf-8")
pairs = [
    ('''    a4 = sp.Function("a4")(X[3])  # the unknown function a4(x4)
    z = 6 * H * X[7]  # z = 6 H x0''',
     '''    a4 = sp.Function("a4")(X[4])  # the unknown function a4(x4)
    z = 6 * H * X[0]  # z = 6 H x0'''),
    ('''    METRIC = ([sp.exp(2 * a4) * warp] * 3 + [sp.Integer(-1)]
              + [-sp.exp(-2 * a4) * warp] * 3 + [sp.cot(z) ** 2])  # g_11 ... g_88''',
     '''    METRIC = ([sp.cot(z) ** 2] + [sp.exp(2 * a4) * warp] * 3 + [sp.Integer(-1)]
              + [-sp.exp(-2 * a4) * warp] * 3)  # g_00 ... g_77, at b4 = 1'''),
    ('''    SYMBOLS = {sp.Derivative(a4, (X[3], 2)): A2, sp.Derivative(a4, X[3]): A1}''',
     '''    SYMBOLS = {sp.Derivative(a4, (X[4], 2)): A2, sp.Derivative(a4, X[4]): A1}'''),
    ('''    mixing = [sp.expand(RIEMANN.get((3, c, 7, c), 0)) for c in range(7)]  # c = x1..x7''',
     '''    mixing = [sp.expand(RIEMANN.get((4, c, 0, c), 0)) for c in range(1, 8)]  # c = x1..x7'''),
    ('''    for c, term in enumerate(mixing):
        say(f"R^(x4 {NAMES[c]})_(x0 {NAMES[c]}) = {term}")''',
     '''    for c, term in enumerate(mixing, 1):
        say(f"R^(x4 {NAMES[c]})_(x0 {NAMES[c]}) = {term}")'''),
    ('''    ax.bar(NAMES[:7], heights, color=colours)''',
     '''    ax.bar(NAMES[1:], heights, color=colours)'''),
    ('''        and tables[k][0, 0] == tables[k][1, 1] == tables[k][2, 2]
        and tables[k][4, 4] == tables[k][5, 5] == tables[k][6, 6]
        and tables[k][7, 7] == (tables[k][0, 0] + tables[k][4, 4]) / 2''',
     '''        and tables[k][1, 1] == tables[k][2, 2] == tables[k][3, 3]
        and tables[k][5, 5] == tables[k][6, 6] == tables[k][7, 7]
        and tables[k][0, 0] == (tables[k][1, 1] + tables[k][5, 5]) / 2'''),
    ('''    check(diagonal_ok and list(np.diag(tables[1])) == [4, 4, 4, 33, 2, 2, 2, 3],''',
     '''    check(diagonal_ok and list(np.diag(tables[1])) == [3, 4, 4, 4, 33, 2, 2, 2],'''),
    ('''          "equal, hidden entry their mean; G = diag(4, 4, 4, 33, 2, 2, 2, 3) H^2")''',
     '''          "equal, hidden entry their mean; G = diag(3, 4, 4, 4, 33, 2, 2, 2) H^2")'''),
]
s = strict_replace(s, pairs, "11b")
p.write_bytes(s.encode("utf-8"))
left = [l.strip() for l in s.splitlines() if "X[3]" in l or "X[7]" in l]
print("ok", left)
