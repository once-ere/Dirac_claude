"""09a builder: positions of the author's coordinates x0..x7 (gammas.json and the records are
in that order); the random configuration is reordered so that its numbers are unchanged."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from relabel_common import REPO, strict_replace  # noqa: E402

p = REPO / "Revision/textbook/notebooks/src/09a_emt_and_identities.py"
s = p.read_text(encoding="utf-8")
pairs = [
    ("    # gamma[a] is the frame matrix gamma^(x_(a+1)): gamma[0] = x0, ..., gamma[7] = x7.\n",
     "    # gamma[a] is the frame matrix gamma^(xa): gamma[0] = x0, ..., gamma[7] = x7.\n"),
    ('''        return np.array([space] * 3 + [1.0] + [extra] * 3 + [1 / np.tan(z_value)])''',
     '''        return np.array([1 / np.tan(z_value)] + [space] * 3 + [1.0] + [extra] * 3)'''),
    ('''    authors = np.array([np.exp(2 * a4) * np.sin(z) ** (1 / 3)] * 3 + [-1.0]
                       + [-np.exp(-2 * a4) * np.sin(z) ** (1 / 3)] * 3
                       + [1 / np.tan(z) ** 2])''',
     '''    authors = np.array([1 / np.tan(z) ** 2] + [np.exp(2 * a4) * np.sin(z) ** (1 / 3)] * 3
                       + [-1.0] + [-np.exp(-2 * a4) * np.sin(z) ** (1 / 3)] * 3)'''),
    ('''          "the volume factor f1 f2 ... f8 equals cos z",''',
     '''          "the volume factor f0 f1 ... f7 equals cos z",'''),
    ('''        panel.plot(axis, weights[:, 0], label="3-space $x_1, x_2, x_3$")
        panel.plot(axis, weights[:, 3], "--", label="time $x_4$")
        panel.plot(axis, weights[:, 4], label="extra times $x_5, x_6, x_7$")
        panel.plot(axis, weights[:, 7], ":", label="hidden direction $x_0$")''',
     '''        panel.plot(axis, weights[:, 1], label="3-space $x_1, x_2, x_3$")
        panel.plot(axis, weights[:, 4], "--", label="time $x_4$")
        panel.plot(axis, weights[:, 5], label="extra times $x_5, x_6, x_7$")
        panel.plot(axis, weights[:, 0], ":", label="hidden direction $x_0$")'''),
    ('''        for i in range(3):  # the three 3-space directions x1, x2, x3
            omega[i] = 0.5 * np.exp(a4_value) * s * (
                a4p_value * gamma[i] @ gamma[3] + H * gamma[i] @ gamma[7])
        for t in range(4, 7):  # the three extra times x5, x6, x7
            omega[t] = -0.5 * np.exp(-a4_value) * s * (
                a4p_value * gamma[3] @ gamma[t] + H * gamma[t] @ gamma[7])''',
     '''        for i in range(1, 4):  # the three 3-space directions x1, x2, x3
            omega[i] = 0.5 * np.exp(a4_value) * s * (
                a4p_value * gamma[i] @ gamma[4] + H * gamma[i] @ gamma[0])
        for t in range(5, 8):  # the three extra times x5, x6, x7
            omega[t] = -0.5 * np.exp(-a4_value) * s * (
                a4p_value * gamma[4] @ gamma[t] + H * gamma[t] @ gamma[0])'''),
    ('''    check(np.abs(total - 3 * H * gamma[7]).max() < 1e-14''',
     '''    check(np.abs(total - 3 * H * gamma[0]).max() < 1e-14'''),
    ('''    dPhi = rng.normal(size=(8, 16)) + 1j * rng.normal(size=(8, 16))  # d_mu Phi''',
     '''    dPhi = rng.normal(size=(8, 16)) + 1j * rng.normal(size=(8, 16))  # d_mu Phi
    # np.roll moves the last row to the front: the eight rows are the derivatives along
    # x0, x1, ..., x7, and the numbers are those of the earlier edition of this notebook.
    dPhi = np.roll(dPhi, 1, axis=0)'''),
    ('''    rho = -T[3, 3]  # the energy density
    rho_kin = -(K.sum() - K[3])  # minus the sum of the K_mu with mu different from x4''',
     '''    rho = -T[4, 4]  # the energy density
    rho_kin = -(K.sum() - K[4])  # minus the sum of the K_mu with mu different from x4'''),
    ('''    for mu in (0, 1, 2, 4, 5, 6, 7):
        report(f"pressure T^{NAMES[mu]}_{NAMES[mu]}", f"{T[mu, mu]:.6f}")''',
     '''    for mu in (0, 1, 2, 3, 5, 6, 7):
        report(f"pressure T^{NAMES[mu]}_{NAMES[mu]}", f"{T[mu, mu]:.6f}")'''),
    ('''    rest = sum(gamma[a] @ dPhi[a] / f[a] for a in range(8) if a != 3)
    dPhi_on = dPhi.copy()
    dPhi_on[3] = -gamma[3] @ (V * Phi - rest - 3 * H * gamma[7] @ Phi)''',
     '''    rest = sum(gamma[a] @ dPhi[a] / f[a] for a in range(8) if a != 4)
    dPhi_on = dPhi.copy()
    dPhi_on[4] = -gamma[4] @ (V * Phi - rest - 3 * H * gamma[0] @ Phi)'''),
    ('''    dPhi_hom[3] = rng.normal(size=16) + 1j * rng.normal(size=16)
    D_x1 = dPhi_hom[0] + Omega[0] @ Phi  # D_x1 Phi = Omega_x1 Phi here
    Dbar_x1 = bar(dPhi_hom[0]) - bar(Phi) @ Omega[0]  # D_x1 Phibar = -Phibar Omega_x1
    K_41 = 0.5 * (bar(Phi) @ gamma_up[3] @ D_x1 - Dbar_x1 @ gamma_up[3] @ Phi)
    expected = 0.5 * np.exp(a4) * np.sin(z) ** (1 / 6) * H * (
        bar(Phi) @ gamma[3] @ gamma[0] @ gamma[7] @ Phi)''',
     '''    dPhi_hom[4] = rng.normal(size=16) + 1j * rng.normal(size=16)
    D_x1 = dPhi_hom[1] + Omega[1] @ Phi  # D_x1 Phi = Omega_x1 Phi here
    Dbar_x1 = bar(dPhi_hom[1]) - bar(Phi) @ Omega[1]  # D_x1 Phibar = -Phibar Omega_x1
    K_41 = 0.5 * (bar(Phi) @ gamma_up[4] @ D_x1 - Dbar_x1 @ gamma_up[4] @ Phi)
    expected = 0.5 * np.exp(a4) * np.sin(z) ** (1 / 6) * H * (
        bar(Phi) @ gamma[4] @ gamma[1] @ gamma[0] @ Phi)'''),
    # sympy part
    ('''    a4_function = sp.Function("a4")(x[3])  # a general function a4(x4)
    zs = 6 * Hs * x[7]  # z = 6 H x0''',
     '''    a4_function = sp.Function("a4")(x[4])  # a general function a4(x4)
    zs = 6 * Hs * x[0]  # z = 6 H x0'''),
    ('''    g = sp.diag(*([space_entry] * 3 + [-1] + [extra_entry] * 3 + [sp.cot(zs) ** 2]))''',
     '''    g = sp.diag(*([sp.cot(zs) ** 2] + [space_entry] * 3 + [-1] + [extra_entry] * 3))'''),
    ('''        return expression.subs(sp.Derivative(a4_function, x[3]), a4ps).subs(''',
     '''        return expression.subs(sp.Derivative(a4_function, x[4]), a4ps).subs('''),
    ('''    NAMES_SYMPY = {"a4": a4s, "a4p": a4ps, "H": Hs, "x0": x[7], "E": sp.E}''',
     '''    NAMES_SYMPY = {"a4": a4s, "a4p": a4ps, "H": Hs, "x0": x[0], "E": sp.E}'''),
    ('''    rho_f, p3_f, pt_f, p0_f = [sp.Function(n)(x[3], x[7]) for n in ("rho", "p3", "pt",''',
     '''    rho_f, p3_f, pt_f, p0_f = [sp.Function(n)(x[4], x[0]) for n in ("rho", "p3", "pt",'''),
    ('''    T_diag = sp.diag(p3_f, p3_f, p3_f, -rho_f, pt_f, pt_f, pt_f, p0_f)  # T^mu_nu''',
     '''    T_diag = sp.diag(p0_f, p3_f, p3_f, p3_f, -rho_f, pt_f, pt_f, pt_f)  # T^mu_nu'''),
    ('''        expression = expression.subs({sp.Derivative(rho_f, x[3]): rho_4,
                                      sp.Derivative(p0_f, x[7]): p0_8})''',
     '''        expression = expression.subs({sp.Derivative(rho_f, x[4]): rho_4,
                                      sp.Derivative(p0_f, x[0]): p0_0})'''),
    ('''    check(sp.simplify(plain_t(divergence[3]) - x4_line) == 0''',
     '''    check(sp.simplify(plain_t(divergence[4]) - x4_line) == 0'''),
    ('''    check(sp.simplify(plain_t(divergence[7]) - x0_line) == 0''',
     '''    check(sp.simplify(plain_t(divergence[0]) - x0_line) == 0'''),
    ('''          "nabla_mu T^mu_x0 = d8 p0 + 3 H cot z (2 p0 - p3 - p_t)",''',
     '''          "nabla_mu T^mu_x0 = d0 p0 + 3 H cot z (2 p0 - p3 - p_t)",'''),
    ('''    check(all(divergence[n] == 0 for n in (0, 1, 2, 4, 5, 6))''',
     '''    check(all(divergence[n] == 0 for n in (1, 2, 3, 5, 6, 7))'''),
    ('''    V7 = V3 * Vt * sp.cot(zs)  # times f8 = cot z (and f4 = 1)
    check(sp.simplify(V7 - sp.cos(zs)) == 0, "V3 Vt f8 = cos z, independent of x4")
    first_law = (sp.diff(rho_f * V7, x[3]) + p3_f * V7 / V3 * sp.diff(V3, x[3])
                 + pt_f * V7 / Vt * sp.diff(Vt, x[3]))''',
     '''    V7 = V3 * Vt * sp.cot(zs)  # times f0 = cot z (and f4 = 1)
    check(sp.simplify(V7 - sp.cos(zs)) == 0, "V3 Vt f0 = cos z, independent of x4")
    first_law = (sp.diff(rho_f * V7, x[4]) + p3_f * V7 / V3 * sp.diff(V3, x[4])
                 + pt_f * V7 / Vt * sp.diff(Vt, x[4]))'''),
    ('''    check(sp.simplify(first_law + V7 * divergence[3]) == 0,''',
     '''    check(sp.simplify(first_law + V7 * divergence[4]) == 0,'''),
    ('''    balance = sp.diff(profile, x[7]) + 3 * Hs * sp.cot(zs) * (2 * profile - P)''',
     '''    balance = sp.diff(profile, x[0]) + 3 * Hs * sp.cot(zs) * (2 * profile - P)'''),
    ('''    dy_dx8 = sp.diff(sp.log(sp.sin(zs)) / (6 * Hs), x[7])  # y = ln(sin z)/(6 H)
    check(sp.simplify(dy_dx8 - sp.cot(zs)) == 0''',
     '''    dy_dx0 = sp.diff(sp.log(sp.sin(zs)) / (6 * Hs), x[0])  # y = ln(sin z)/(6 H)
    check(sp.simplify(dy_dx0 - sp.cot(zs)) == 0'''),
    ('''          "y = ln(sin z)/(6 H) has dy/dx8 = cot z",''',
     '''          "y = ln(sin z)/(6 H) has dy/dx0 = cot z",'''),
]
s = strict_replace(s, pairs, "09a")
s = s.replace("p0_8", "p0_0")
left = [l for l in s.splitlines() if any(t in l for t in ("x[3]", "x[7]", "gamma[7]", "gamma[3]", "p0_8"))]
p.write_bytes(s.encode("utf-8"))
print("ok", left)
