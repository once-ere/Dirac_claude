"""12a builder: the author's coordinates x0..x7 (positions 0..7 = x0..x7); the a4 record is
read with the same names; e88 -> e00 (the hidden-direction equation)."""
import re
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from relabel_common import REPO, strict_replace  # noqa: E402

p = REPO / "Revision/textbook/notebooks/src/12a_a4_field_equations.py"
s = p.read_text(encoding="utf-8")
pairs = [
    ('''    g = ([sp.exp(2 * a4) * warp] * 3  # g11 = g22 = g33: 3-space, factor e^(2 a4)
         + [sp.Integer(-1)]  # g44 = -1: the time x4
         + [-sp.exp(-2 * a4) * warp] * 3  # g55 = g66 = g77: extra times, e^(-2 a4)
         + [sp.cot(z) ** 2])  # g88 = cot(z)^2: the hidden direction''',
     '''    g = ([sp.cot(z) ** 2]  # g00 = cot(z)^2: the hidden direction
         + [sp.exp(2 * a4) * warp] * 3  # g11 = g22 = g33: 3-space, factor e^(2 a4)
         + [sp.Integer(-1)]  # g44 = -1: the time x4
         + [-sp.exp(-2 * a4) * warp] * 3)  # g55 = g66 = g77: extra times, e^(-2 a4)'''),
    ('''        mu (0..7 for x0..x7); d/dx8 = 6 H d/dz by the chain rule."""
        if mu == 3:
            return sp.diff(expr, x4)
        if mu == 7:
            return 6 * H * sp.diff(expr, z)''',
     '''        mu (0..7 for x0..x7); d/dx0 = 6 H d/dz by the chain rule."""
        if mu == 4:
            return sp.diff(expr, x4)
        if mu == 0:
            return 6 * H * sp.diff(expr, z)'''),
    ('''    reproduces(G[0][0] == G[1][1] == G[2][2] and G[4][4] == G[5][5] == G[6][6],''',
     '''    reproduces(G[1][1] == G[2][2] == G[3][3] and G[5][5] == G[6][6] == G[7][7],'''),
    ('''                     and Ek[0][0] == Ek[1][1] == Ek[2][2]
                     and Ek[4][4] == Ek[5][5] == Ek[6][6]''',
     '''                     and Ek[1][1] == Ek[2][2] == Ek[3][3]
                     and Ek[5][5] == Ek[6][6] == Ek[7][7]'''),
    ('''    reproduces(sp.expand(lanczos[3][3].subs(LINEAR)''',
     '''    reproduces(sp.expand(lanczos[4][4].subs(LINEAR)'''),
    ('''    reproduces(sp.expand(lanczos[0][0].subs(LINEAR)''',
     '''    reproduces(sp.expand(lanczos[1][1].subs(LINEAR)'''),
    ('''    for i, value in enumerate([p3, p3, p3, -rho, pt, pt, pt, p0]):
        T[i][i] = value  # the diagonal of the source
    T[3][7], T[7][3] = q40, q04  # the two mixed components x4-x0 and x0-x4''',
     '''    for i, value in enumerate([p0, p3, p3, p3, -rho, pt, pt, pt]):
        T[i][i] = value  # the diagonal of the source, in the order x0..x7
    T[4][0], T[0][4] = q40, q04  # the two mixed components x4-x0 and x0-x4'''),
    ('''    groups_equal = (LHS[0][0] == LHS[1][1] == LHS[2][2]
                    and LHS[4][4] == LHS[5][5] == LHS[6][6])''',
     '''    groups_equal = (LHS[1][1] == LHS[2][2] == LHS[3][3]
                    and LHS[5][5] == LHS[6][6] == LHS[7][7])'''),
    ('''    e11, e44, e55, e88 = (sp.expand(LHS[i][i] - Lam) for i in (0, 3, 4, 7))''',
     '''    e11, e44, e55, e88 = (sp.expand(LHS[i][i] - Lam) for i in (1, 4, 5, 0))'''),
    ('''    for i, name in enumerate(["p3", "p3", "p3", "rho", "pt", "pt", "pt", "p0"]):
        Tgeneral[i][i] = source[name]
    Tgeneral[3][3] = -source["rho"]  # T^x4_x4 = -rho
    Tgeneral[3][7], Tgeneral[7][3] = source["q40"], source["q04"]''',
     '''    for i, name in enumerate(["p0", "p3", "p3", "p3", "rho", "pt", "pt", "pt"]):
        Tgeneral[i][i] = source[name]
    Tgeneral[4][4] = -source["rho"]  # T^x4_x4 = -rho
    Tgeneral[4][0], Tgeneral[0][4] = source["q40"], source["q04"]'''),
    ('''    expect_x4 = (-d(source["rho"], 3) - 3 * a4p * (source["p3"] - source["pt"])
                 + d(source["q04"], 7) - 6 * H * sp.tan(z) * source["q04"])
    expect_x0 = (d(source["p0"], 7) + d(source["q40"], 3)''',
     '''    expect_x4 = (-d(source["rho"], 4) - 3 * a4p * (source["p3"] - source["pt"])
                 + d(source["q04"], 0) - 6 * H * sp.tan(z) * source["q04"])
    expect_x0 = (d(source["p0"], 0) + d(source["q40"], 4)'''),
    ('''    reproduces(clean(divT[3] - expect_x4) == 0, "nabla_mu T^mu_x4 as in the record",''',
     '''    reproduces(clean(divT[4] - expect_x4) == 0, "nabla_mu T^mu_x4 as in the record",'''),
    ('''    reproduces(clean(divT[7] - expect_x0) == 0, "nabla_mu T^mu_x0 as in the record",''',
     '''    reproduces(clean(divT[0] - expect_x0) == 0, "nabla_mu T^mu_x0 as in the record",'''),
    ('''    reproduces(all(divT[n] == 0 for n in (0, 1, 2, 4, 5, 6)),''',
     '''    reproduces(all(divT[n] == 0 for n in (1, 2, 3, 5, 6, 7)),'''),
    ('''    vacuum = [LHS[i][i].subs(EINSTEIN) for i in (0, 3, 4, 7)]  # T = 0''',
     '''    vacuum = [LHS[i][i].subs(EINSTEIN) for i in (1, 4, 5, 0)]  # T = 0'''),
]
s = strict_replace(s, pairs, "12a")
s = re.sub(r"(?<![A-Za-z0-9_])e88(?![A-Za-z0-9_])", "e00", s)
s = s.replace("p_8", "p_0")
p.write_bytes(s.encode("utf-8"))
print("ok", [l.strip() for l in s.splitlines() if re.search(r"\[3\]|\[7\]|x8|e88|p8\b", l)][:8])
