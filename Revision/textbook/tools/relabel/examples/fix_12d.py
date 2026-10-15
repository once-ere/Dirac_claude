"""12d builder: positions of the author's coordinates x0..x7 (gammas.json is in that order)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from relabel_common import REPO, strict_replace  # noqa: E402

p = REPO / "Revision/textbook/notebooks/src/12d_condensate_solution.py"
s = p.read_text(encoding="utf-8")
pairs = [
    ("# gamma[a] = gamma^(x_(a+1))", "# gamma[a] = gamma^(xa)"),
    ("    C = gamma[7] * gamma[0] * gamma[1] * gamma[2]  # C = g^(x0) g^(x1) g^(x2) g^(x3)\n",
     "    C = gamma[0] * gamma[1] * gamma[2] * gamma[3]  # C = g^(x0) g^(x1) g^(x2) g^(x3)\n"),
    ("    E = [sp.exp(a4) * s6] * 3 + [sp.Integer(1)] + [sp.exp(-a4) * s6] * 3 + [sp.cot(z)]\n",
     "    E = [sp.cot(z)] + [sp.exp(a4) * s6] * 3 + [sp.Integer(1)] + [sp.exp(-a4) * s6] * 3\n"),
    ('''        if mu == 3:
            return sp.diff(expr, x4)
        if mu == 7:
            return 6 * H * sp.diff(expr, z)  # d/dx8 = (dz/dx8) d/dz = 6 H d/dz''',
     '''        if mu == 4:
            return sp.diff(expr, x4)
        if mu == 0:
            return 6 * H * sp.diff(expr, z)  # d/dx0 = (dz/dx0) d/dz = 6 H d/dz'''),
    ('''    reproduces(Omega[3] == Z16 and Omega[7] == Z16, "Omega_x4 = Omega_x0 = 0",''',
     '''    reproduces(Omega[4] == Z16 and Omega[0] == Z16, "Omega_x4 = Omega_x0 = 0",'''),
    ('''    reproduces(gravity_term == 3 * H * gamma[7], "gamma^mu Omega_mu = 3 H gamma^(x0)",''',
     '''    reproduces(gravity_term == 3 * H * gamma[0], "gamma^mu Omega_mu = 3 H gamma^(x0)",'''),
    ('''    reproduces(gravity_term == 3 * H * gamma[7], "the same, the lead's independent check",''',
     '''    reproduces(gravity_term == 3 * H * gamma[0], "the same, the lead's independent check",'''),
    ('''        return -gamma[3] * (M_value * I16 - 3 * H_value * gamma[7])''',
     '''        return -gamma[4] * (M_value * I16 - 3 * H_value * gamma[0])'''),
    ('''    reduced = (gamma[3] * A_sym + gravity_term - MM * I16).applyfunc(sp.expand)''',
     '''    reduced = (gamma[4] * A_sym + gravity_term - MM * I16).applyfunc(sp.expand)'''),
    ('''    NEEDED = sorted({tuple(sorted((i, 3, 7))) for i in (0, 1, 2, 4, 5, 6)}
                    | {tuple(sorted((i, j, 3))) for i in (0, 1, 2) for j in (4, 5, 6)})''',
     '''    NEEDED = sorted({tuple(sorted((i, 4, 0))) for i in (1, 2, 3, 5, 6, 7)}
                    | {tuple(sorted((i, j, 4))) for i in (1, 2, 3) for j in (5, 6, 7)})'''),
    ('''                                     gamma[0] * gamma[4] - sign * I16,
                                     gamma[1] * gamma[5] - sign * I16,
                                     gamma[2] * gamma[6] - sign * I16)''',
     '''                                     gamma[1] * gamma[5] - sign * I16,
                                     gamma[2] * gamma[6] - sign * I16,
                                     gamma[3] * gamma[7] - sign * I16)'''),
    ('''    check(all(3 not in triple and 7 not in triple for triple in nonzero),''',
     '''    check(all(4 not in triple and 0 not in triple for triple in nonzero),'''),
    ('''        return (A_witness if nu == 3 else Z16) + Omega_1[nu]''',
     '''        return (A_witness if nu == 4 else Z16) + Omega_1[nu]'''),
    ('''        return (A_witness.T * C if nu == 3 else Z16) - C * Omega_1[nu]''',
     '''        return (A_witness.T * C if nu == 4 else Z16) - C * Omega_1[nu]'''),
    ('''    reproduces(all(diagonal[mu] == 0 for mu in range(8) if mu != 3)
               and sp.expand(diagonal[3] - (-5) * S_t) == 0,''',
     '''    reproduces(all(diagonal[mu] == 0 for mu in range(8) if mu != 4)
               and sp.expand(diagonal[4] - (-5) * S_t) == 0,'''),
    ('''    rho_family = sp.expand(-T_family[3][3].subs(on_shell))
    pressures = [sp.expand(T_family[mu][mu].subs(on_shell)) for mu in (0, 4, 7)]''',
     '''    rho_family = sp.expand(-T_family[4][4].subs(on_shell))
    pressures = [sp.expand(T_family[mu][mu].subs(on_shell)) for mu in (1, 5, 0)]'''),
    ('''            G_diag = [G_space] * 3 + [G_time] + [G_extra] * 3 + [G_hidden]''',
     '''            G_diag = [G_hidden] + [G_space] * 3 + [G_time] + [G_extra] * 3'''),
    ('''        rho_e, p_e = -T_e[3][3], T_e[0][0]''',
     '''        rho_e, p_e = -T_e[4][4], T_e[1][1]'''),
    ('''        residual = (gamma[3] * sp.diff(phi, x4) + gravity_term.subs(UNIT_H) * phi''',
     '''        residual = (gamma[4] * sp.diff(phi, x4) + gravity_term.subs(UNIT_H) * phi'''),
]
s = strict_replace(s, pairs, "12d")
p.write_bytes(s.encode("utf-8"))
import re  # noqa: E402
print("ok", [l.strip() for l in s.splitlines() if re.search(r"gamma\[(3|7)\]|\[3\]\[3\]|== 3\b|== 7\b", l)][:8])
