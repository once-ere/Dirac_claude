"""17b builder: the author's coordinates x0..x7 (positions, the x0 and y charts with the hidden
coordinate first) and the names with the old label 8 (p_8, b_8, dy_dx8, ...)."""
import re
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from relabel_common import REPO, strict_replace  # noqa: E402

p = REPO / "Revision/textbook/notebooks/src/17b_conserved_sources.py"
s = p.read_text(encoding="utf-8")
pairs = [
    ('''    x4, x0 = coords[3], coords[7]''', '''    x4, x0 = coords[4], coords[0]'''),
    ('''    metric_x0 = sp.diag(*([sp.exp(2 * a4) * wz] * 3 + [-1]
                          + [-sp.exp(-2 * a4) * wz] * 3 + [sp.cot(zz) ** 2]))''',
     '''    metric_x0 = sp.diag(*([sp.cot(zz) ** 2] + [sp.exp(2 * a4) * wz] * 3 + [-1]
                          + [-sp.exp(-2 * a4) * wz] * 3))  # x0, ..., x7 (b4 = 1)'''),
    ('''    T_x0 = sp.diag(p3, p3, p3, -rho, pt, pt, pt, p0)  # the diagonal part
    T_x0[3, 7] = q40  # T^x4_x0
    T_x0[7, 3] = q04  # T^x0_x4''',
     '''    T_x0 = sp.diag(p0, p3, p3, p3, -rho, pt, pt, pt)  # the diagonal part
    T_x0[4, 0] = q40  # T^x4_x0
    T_x0[0, 4] = q04  # T^x0_x4'''),
    ('''    for key, nu in (("conservation_x4", 3), ("conservation_x0", 7)):''',
     '''    for key, nu in (("conservation_x4", 4), ("conservation_x0", 0)):'''),
    ('''    zero_components = all(div_x0[nu] == 0 for nu in (0, 1, 2, 4, 5, 6))''',
     '''    zero_components = all(div_x0[nu] == 0 for nu in (1, 2, 3, 5, 6, 7))'''),
    ('''    chart_y = list(coords[:7]) + [yc]  # x1, ..., x7, y''',
     '''    chart_y = [yc] + list(coords[1:])  # y (for x0), x1, ..., x7'''),
    ('''    metric_y = sp.diag(*([sp.exp(2 * a4) * wy] * 3 + [-1]
                         + [-sp.exp(-2 * a4) * wy] * 3 + [1]))''',
     '''    metric_y = sp.diag(*([1] + [sp.exp(2 * a4) * wy] * 3 + [-1]
                         + [-sp.exp(-2 * a4) * wy] * 3))'''),
    ('''    T_y = sp.diag(P3, P3, P3, -RHO, PT, PT, PT, P0)  # a diagonal source T(x4, y)''',
     '''    T_y = sp.diag(P0, P3, P3, P3, -RHO, PT, PT, PT)  # a diagonal source T(x4, y)'''),
    ('''    say(f"nabla_mu T^mu_x4 = {short(div_y[3])}")
    say(f"nabla_mu T^mu_y = {short(div_y[7])}")
    others_zero = all(div_y[nu] == 0 for nu in (0, 1, 2, 4, 5, 6))''',
     '''    say(f"nabla_mu T^mu_x4 = {short(div_y[4])}")
    say(f"nabla_mu T^mu_y = {short(div_y[0])}")
    others_zero = all(div_y[nu] == 0 for nu in (1, 2, 3, 5, 6, 7))'''),
    ('''    reproduces(sp.simplify(div_y[3] - law_x4) == 0 and sp.simplify(div_y[7] - law_y) == 0''',
     '''    reproduces(sp.simplify(div_y[4] - law_x4) == 0 and sp.simplify(div_y[0] - law_y) == 0'''),
]
s = strict_replace(s, pairs, "17b")
for old, new in (("b_8", "b_0"), ("mean_p8", "mean_p0"), ("dp8", "dp0"), ("dy_dx8", "dy_dx0"),
                 ("b8", "b0"), ("dyp8", "dyp0"), ("dx8", "dx0"), ("X8", "X0"), ("g88", "g00"),
                 ("d8p8", "d0p0")):
    s = re.sub(r"(?<![A-Za-z0-9_])" + re.escape(old) + r"(?![A-Za-z0-9_])", new, s)
s = re.sub(r"p_8(?![0-9])", "p_0", s)
s = s.replace("dy/dx8", "dy/dx0")
p.write_bytes(s.encode("utf-8"))
print("ok", [l.strip() for l in s.splitlines() if re.search(r"\b[A-Za-z_]+8\b|coords\[(3|7)\]|div_[a-z0-9]+\[(3|7)\]", l)][:6])
