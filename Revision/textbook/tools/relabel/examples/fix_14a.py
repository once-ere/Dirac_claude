"""14a builder: the author's coordinates x0..x7. gammas.json is in that order, so the unpacked
names are g0, ..., g7 (g0 = gamma^(x0)); the coordinate list is (y, x1, ..., x7) with the
hidden coordinate y (for x0) first."""
import re
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from relabel_common import REPO, strict_replace  # noqa: E402

p = REPO / "Revision/textbook/notebooks/src/14a_block_reduction.py"
s = p.read_text(encoding="utf-8")
pairs = [
    ("    g1, g2, g3, g4, g5, g6, g7, g8 = g  # gN is gamma^(xN)\n",
     "    g0, g1, g2, g3, g4, g5, g6, g7 = g  # gN is gamma^(xN)\n"),
    ('''    X = sp.symbols("x1:8", real=True) + (sp.Symbol("y", real=True),)  # x1..x7 and y
    Y, x4 = X[7], X[3]  # the hidden coordinate and the time''',
     '''    X = (sp.Symbol("y", real=True),) + sp.symbols("x1:8", real=True)  # y, x1..x7
    Y, x4 = X[0], X[4]  # the hidden coordinate and the time'''),
    ('''    vb = [sp.exp(a4) * W] * 3 + [sp.Integer(1)] + [sp.exp(-a4) * W] * 3 + [sp.Integer(1)]''',
     '''    vb = [sp.Integer(1)] + [sp.exp(a4) * W] * 3 + [sp.Integer(1)] + [sp.exp(-a4) * W] * 3'''),
    ('''    names = ["x1", "x2", "x3", "x4", "x5", "x6", "x7", "x0 (y)"]''',
     '''    names = ["x0 (y)", "x1", "x2", "x3", "x4", "x5", "x6", "x7"]'''),
    ('''    inflating = sp.simplify(sum(c4_list[0:3]))  # x1, x2, x3
    deflating = sp.simplify(sum(c4_list[4:7]))  # x5, x6, x7''',
     '''    inflating = sp.simplify(sum(c4_list[1:4]))  # x1, x2, x3
    deflating = sp.simplify(sum(c4_list[5:8]))  # x5, x6, x7'''),
    ('''          and Omega[3].is_zero_matrix and Omega[7].is_zero_matrix''',
     '''          and Omega[4].is_zero_matrix and Omega[0].is_zero_matrix'''),
    ('''    ax.set_xticklabels(["$x_1$", "$x_2$", "$x_3$", "$x_4$", "$x_5$", "$x_6$", "$x_7$",
                        "$x_0$"])''',
     '''    ax.set_xticklabels(["$x_0$", "$x_1$", "$x_2$", "$x_3$", "$x_4$", "$x_5$", "$x_6$",
                        "$x_7$"])'''),
    ('''    phase = sp.exp(sp.I * (k1 * X[0] + k2 * X[1] + k3 * X[2]))  # the plane wave''',
     '''    phase = sp.exp(sp.I * (k1 * X[1] + k2 * X[2] + k3 * X[3]))  # the plane wave'''),
]
s = strict_replace(s, pairs, "14a")
for old, new in (("g8", "g0"), ("c8", "c0"), ("c8_list", "c0_list"), ("c8_numbers", "c0_numbers")):
    s = re.sub(r"(?<![A-Za-z0-9_])" + re.escape(old) + r"(?![A-Za-z0-9_])", new, s)
s = s.replace("in the code `g1`, ..., `g8`.", "in the code `g0`, ..., `g7`.")
s = s.replace("c_4\\gamma^{(x_4)} + c_8\\gamma^{(x_0)}", "c_4\\gamma^{(x_4)} + c_0\\gamma^{(x_0)}")
s = s.replace("$c_8 =", "$c_0 =").replace("c_8\\\\gamma^{(x_0)}", "c_0\\\\gamma^{(x_0)}")
p.write_bytes(s.encode("utf-8"))
print("ok", [l.strip() for l in s.splitlines() if re.search(r"\bg8\b|c_8|X\[7\]|X\[3\]", l)][:5])
