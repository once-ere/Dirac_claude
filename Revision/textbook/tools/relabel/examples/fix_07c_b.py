"""07c builder: the b4 symbols get names that no loop variable uses (b4, b4p, b4pp, b4ppp)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from relabel_common import REPO, strict_replace  # noqa: E402

p = REPO / "Revision/textbook/notebooks/src/07c_real_fields.py"
s = p.read_text(encoding="utf-8")
pairs = [
    (r'''    ring, the diagonal frame $f = (c/s^6, Es, Es, Es, 1, s\sqrt b/E, s\sqrt b/E,
    s\sqrt b/E)$ of the metric with $b_4$ (in the order $x_0, \dots, x_7$; $b$ stands
    for $b_4(x_4)$ and `b1`, `b2`, `b3` for its derivatives), the Christoffel symbols of''',
     r'''    ring, the diagonal frame $f = (c/s^6, Es, Es, Es, 1, s\sqrt{b_4}/E, s\sqrt{b_4}/E,
    s\sqrt{b_4}/E)$ of the metric with $b_4$ (in the order $x_0, \dots, x_7$; the
    symbol `b4` stands for $b_4(x_4)$ and `b4p`, `b4pp`, `b4ppp` for its first three
    derivatives), the Christoffel symbols of'''),
    ('''    b = sp.Symbol("b", positive=True)  # b4(x4) > 0
    b1, b2, b3 = sp.symbols("b1 b2 b3", real=True)  # derivatives of b4 (1st to 3rd)
''',
     '''    b4 = sp.Symbol("b4", positive=True)  # b4(x4) > 0
    b4p, b4pp, b4ppp = sp.symbols("b4p b4pp b4ppp", real=True)  # its 1st to 3rd derivative
'''),
    ('''                    + sp.diff(expression, A2) * A3 + sp.diff(expression, b) * b1
                    + sp.diff(expression, b1) * b2 + sp.diff(expression, b2) * b3)''',
     '''                    + sp.diff(expression, A2) * A3 + sp.diff(expression, b4) * b4p
                    + sp.diff(expression, b4p) * b4pp + sp.diff(expression, b4pp) * b4ppp)'''),
    ("    f = [c / s**6] + [E * s] * 3 + [sp.Integer(1)] + [s * sp.sqrt(b) / E] * 3  # frame\n",
     "    f = [c / s**6] + [E * s] * 3 + [sp.Integer(1)] + [s * sp.sqrt(b4) / E] * 3  # frame\n"),
    ("    sqrt_g = sp.prod(f)  # = b^(3/2) c = b4^(3/2) cos z\n",
     "    sqrt_g = sp.prod(f)  # = b4^(3/2) c = b4^(3/2) cos z\n"),
    ('''    at_b4_1 = {b: 1, b1: 0, b2: 0, b3: 0}  # the background b4 = 1
    check(all(is_zero(v) for v in (total - 3 * H * G[X0] - 3 * b1 / (4 * b) * G[X4]))''',
     '''    at_b4_1 = {b4: 1, b4p: 0, b4pp: 0, b4ppp: 0}  # the background b4 = 1
    check(all(is_zero(v) for v in (total - 3 * H * G[X0] - 3 * b4p / (4 * b4) * G[X4]))'''),
]
s = strict_replace(s, pairs, "07c_b")
p.write_bytes(s.encode("utf-8"))
print("ok")
