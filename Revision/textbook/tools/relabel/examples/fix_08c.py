"""08c builder: positions of the author's coordinates x0..x7 (gammas.json and the records are
in that order); the notebook stays on the background b4 = 1 of the record's scope reports and
says so (Notebook 06b treats the frame dependence for a general b4)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from relabel_common import REPO, strict_replace  # noqa: E402

p = REPO / "Revision/textbook/notebooks/src/08c_frame_dependence.py"
s = p.read_text(encoding="utf-8")
pairs = [
    # markdown
    (r'''    $e'^{(4)} = \cosh b\,e^{(4)} + \sinh b\,e^{(0)}$, $e'^{(8)} = \sinh b\,e^{(4)} +''',
     r'''    $e'^{(4)} = \cosh b\,e^{(4)} + \sinh b\,e^{(0)}$, $e'^{(0)} = \sinh b\,e^{(4)} +'''),
    (r'''    Every symbol is exact: $H > 0$, $\beta$, $b_0$ are letters, and $a_4(x_4)$ is an
    unspecified function; so every check holds for EVERY history $a_4$.''',
     r'''    Every symbol is exact: $H > 0$, $\beta$, $b_0$ are letters, and $a_4(x_4)$ is an
    unspecified function; so every check holds for EVERY history $a_4$. The second
    function $b_4(x_4)$ of the author's metric is put equal to 1 here, the background
    of the Revision record's scope reports with which this notebook compares; Notebook
    06b (Chapter 6) repeats the frame dependence for a general $b_4$, where the
    diagonal frame gives $3H\gamma^{(0)} + \frac34(b_4'/b_4)\gamma^{(4)}$.'''),
    (r'''       c_{18}\,\gamma^{(1)}\gamma^{(0)}$ with two numbers $c_{14}, c_{18}$ (found as''',
     r'''       c_{10}\,\gamma^{(1)}\gamma^{(0)}$ with two numbers $c_{14}, c_{10}$ (found as'''),
    (r'''    3. hence $F_{x_1x_0}^2 = (c_{14}^2 - c_{18}^2)\,I_{16}$, because''',
     r'''    3. hence $F_{x_1x_0}^2 = (c_{14}^2 - c_{10}^2)\,I_{16}$, because'''),
    (r'''       two products anticommute; and $c_{14}^2 - c_{18}^2$ is the SAME in both frames,''',
     r'''       two products anticommute; and $c_{14}^2 - c_{10}^2$ is the SAME in both frames,'''),
    (r'''    this history $a_4' = AH = H$, so $c_{14}^2 - c_{18}^2 = 0$: the matrix $F_{x_1x_0}$''',
     r'''    this history $a_4' = AH = H$, so $c_{14}^2 - c_{10}^2 = 0$: the matrix $F_{x_1x_0}$'''),
    # code: coordinates and metric
    ('''    x = sp.symbols("x0:8", real=True)  # the coordinates; x[0] is x1, x[7] is x0''',
     '''    x = sp.symbols("x0:8", real=True)  # the coordinates; x[k] is xk'''),
    ('''    a4 = sp.Function("a4")(x[3])  # the metric function: ANY function of x4
    z = 6 * H * x[7]''',
     '''    a4 = sp.Function("a4")(x[4])  # the metric function: ANY function of x4
    z = 6 * H * x[0]'''),
    ('''    f = [sp.exp(a4) * sixth] * 3 + [sp.Integer(1)] + [sp.exp(-a4) * sixth] * 3 \\
        + [sp.cot(z)]  # the scale factors f_0, ..., f_7''',
     '''    f = [sp.cot(z)] + [sp.exp(a4) * sixth] * 3 + [sp.Integer(1)] \\
        + [sp.exp(-a4) * sixth] * 3  # the scale factors f_0, ..., f_7 (b4 = 1)'''),
    ('''    authors_metric = [sp.exp(2 * a4) * third] * 3 + [-1] \\
        + [-sp.exp(-2 * a4) * third] * 3 + [sp.cot(z) ** 2]''',
     '''    authors_metric = [sp.cot(z) ** 2] + [sp.exp(2 * a4) * third] * 3 + [-1] \\
        + [-sp.exp(-2 * a4) * third] * 3  # the author's metric at b4 = 1'''),
    ('''    metric_texts = [f"g_x{a + 1}x{a + 1} = {sp.sstr(authors_metric[a])}" for a in range(8)]''',
     '''    metric_texts = [f"g_x{a}x{a} = {sp.sstr(authors_metric[a])}" for a in range(8)]'''),
    ('''    for lam, mu, nu in ((0, 0, 3), (4, 3, 4), (0, 0, 7), (7, 7, 7)):
        say(f"Gamma^x{lam + 1}_x{mu + 1} x{nu + 1} = {Gam[lam][mu][nu]}")''',
     '''    for lam, mu, nu in ((1, 1, 4), (5, 4, 5), (1, 0, 1), (0, 0, 0)):
        say(f"Gamma^x{lam}_x{mu} x{nu} = {Gam[lam][mu][nu]}")'''),
    ('''        """The boost by the rapidity b in the frame plane (x4, x0), and its inverse."""
        L, L_inverse = sp.eye(8), sp.eye(8)
        L[3, 3] = L[7, 7] = L_inverse[3, 3] = L_inverse[7, 7] = sp.cosh(b)
        L[3, 7] = L[7, 3] = sp.sinh(b)
        L_inverse[3, 7] = L_inverse[7, 3] = -sp.sinh(b)''',
     '''        """The boost by the rapidity b in the frame plane (x4, x0), and its inverse."""
        L, L_inverse = sp.eye(8), sp.eye(8)
        L[4, 4] = L[0, 0] = L_inverse[4, 4] = L_inverse[0, 0] = sp.cosh(b)
        L[4, 0] = L[0, 4] = sp.sinh(b)
        L_inverse[4, 0] = L_inverse[0, 4] = -sp.sinh(b)'''),
    ('''        say(f"omega_x{mu + 1},(x{a + 1})(x{c + 1}) = "''',
     '''        say(f"omega_x{mu},(x{a})(x{c}) = "'''),
    ("    a4_prime = sp.diff(a4, x[3])  # a4' = d a4 / d x4\n",
     "    a4_prime = sp.diff(a4, x[4])  # a4' = d a4 / d x4\n"),
    # per direction
    ('''    coefficient_4 = [sp.simplify(-(G[3] * M).trace() / 16) for M in per_direction]
    coefficient_8 = [sp.simplify((G[7] * M).trace() / 16) for M in per_direction]''',
     '''    coefficient_4 = [sp.simplify(-(G[4] * M).trace() / 16) for M in per_direction]
    coefficient_8 = [sp.simplify((G[0] * M).trace() / 16) for M in per_direction]'''),
    ('''            per_direction[mu] - coefficient_4[mu] * G[3] - coefficient_8[mu] * G[7])''',
     '''            per_direction[mu] - coefficient_4[mu] * G[4] - coefficient_8[mu] * G[0])'''),
    ('''        say(f"gamma^x{mu + 1} Omega_x{mu + 1} = ({coefficient_4[mu]}) gamma^(x4) "''',
     '''        say(f"gamma^x{mu} Omega_x{mu} = ({coefficient_4[mu]}) gamma^(x4) "'''),
    ('''    inflating_sum = sp.simplify(sum(coefficient_4[:3])).subs(a4_prime, A1)  # 3*A1/2
    deflating_sum = sp.simplify(sum(coefficient_4[4:7])).subs(a4_prime, A1)  # -3*A1/2''',
     '''    inflating_sum = sp.simplify(sum(coefficient_4[1:4])).subs(a4_prime, A1)  # 3*A1/2
    deflating_sum = sp.simplify(sum(coefficient_4[5:8])).subs(a4_prime, A1)  # -3*A1/2'''),
    ('''                 == [sp.Rational(1, 2)] * 3 + [0] + [-sp.Rational(1, 2)] * 3 + [0]
                 and [sp.simplify(c8 / H) for c8 in coefficient_8]
                 == [sp.Rational(1, 2)] * 3 + [0] + [sp.Rational(1, 2)] * 3 + [0],''',
     '''                 == [0] + [sp.Rational(1, 2)] * 3 + [0] + [-sp.Rational(1, 2)] * 3
                 and [sp.simplify(c8 / H) for c8 in coefficient_8]
                 == [0] + [sp.Rational(1, 2)] * 3 + [0] + [sp.Rational(1, 2)] * 3,'''),
    ('''    check_record(all(is_zero(entry) for entry in total - 3 * H * G[7]),''',
     '''    check_record(all(is_zero(entry) for entry in total - 3 * H * G[0]),'''),
    ('''    check_record(G[7] * G[7] == sp.eye(16),''',
     '''    check_record(G[0] * G[0] == sp.eye(16),'''),
    ('''    sqrt_g = sp.cos(z)''',
     '''    sqrt_g = sp.cos(z)  # sqrt|g| = b4^(3/2) cos z, at b4 = 1'''),
    ('''    check_record(all(is_zero(entry) for entry in divergence - 3 * H * G[7]),''',
     '''    check_record(all(is_zero(entry) for entry in divergence - 3 * H * G[0]),'''),
    ('''    names = [f"$x_{mu + 1}$" for mu in range(8)] + ["sum"]''',
     '''    names = [f"$x_{mu}$" for mu in range(8)] + ["sum"]'''),
    ('''    colours = ["tab:blue"] * 3 + ["gray"] + ["tab:red"] * 3 + ["gray", "black"]''',
     '''    colours = ["gray"] + ["tab:blue"] * 3 + ["gray"] + ["tab:red"] * 3 + ["black"]'''),
    ('''                "$\\\\gamma^{(0)}$ in units of $H$; the same six directions give $+1/2$ "
                "each and the sum is $3$. Exact values from sympy, valid for every "
                "history $a_4$ and every $H > 0$.")''',
     '''                "$\\\\gamma^{(0)}$ in units of $H$; the same six directions give $+1/2$ "
                "each and the sum is $3$. Exact values from sympy, valid for every "
                "history $a_4$ and every $H > 0$, on the background $b_4 = 1$.")'''),
    # Ricci
    ("    a4_second = sp.diff(a4, x[3], 2)\n", "    a4_second = sp.diff(a4, x[4], 2)\n"),
    ('''    expected = [a4_second - 6 * H**2] * 3 + [6 * a4_prime**2] \\
        + [-a4_second - 6 * H**2] * 3 + [-6 * H**2]''',
     '''    expected = [-6 * H**2] + [a4_second - 6 * H**2] * 3 + [6 * a4_prime**2] \\
        + [-a4_second - 6 * H**2] * 3'''),
    ('''                 "ricci_mixed_components", "R^1_1 = R^2_2 = R^3_3 = a4'' - 6 H^2",
                 "R^4_4 = 6 a4'^2", "R^5_5 = R^6_6 = R^7_7 = -a4'' - 6 H^2",
                 "R^8_8 = -6 H^2")''',
     '''                 "ricci_mixed_components", "R^x0_x0 = -6 H^2",
                 "R^x1_x1 = R^x2_x2 = R^x3_x3 = a4'' - 6 H^2", "R^x4_x4 = 6 a4'^2",
                 "R^x5_x5 = R^x6_x6 = R^x7_x7 = -a4'' - 6 H^2")'''),
    ('''    check_record(not total.applyfunc(sp.simplify).has(a4) and not is_zero(ricci[3]),''',
     '''    check_record(not total.applyfunc(sp.simplify).has(a4) and not is_zero(ricci[4]),'''),
    ('''    history = sp.Lambda(x[3], A_history * x[3])  # with H = 1: a4 = x4''',
     '''    history = sp.Lambda(x[4], A_history * x[4])  # with H = 1: a4 = x4'''),
    ('''        concrete = concrete.subs({H: 1, x[7]: sp.pi / 24})  # z = 6 x0 = pi/4
        return sp.lambdify(x[3], concrete, "numpy")''',
     '''        concrete = concrete.subs({H: 1, x[0]: sp.pi / 24})  # z = 6 x0 = pi/4
        return sp.lambdify(x[4], concrete, "numpy")'''),
    ('''    pieces = {"$\\\\omega_{x_1,(1)(4)} = a_4'e^{a_4}\\\\sin^{1/6}z$": diagonal["omega"][0, 0, 3],
              "$\\\\omega_{x_1,(1)(8)} = He^{a_4}\\\\sin^{1/6}z$": diagonal["omega"][0, 0, 7],
              "$|\\\\omega_{x_5,(4)(5)}| = a_4'e^{-a_4}\\\\sin^{1/6}z$":
                  -ETA[3] * diagonal["omega"][4, 3, 4],
              "$|\\\\omega_{x_5,(5)(8)}| = He^{-a_4}\\\\sin^{1/6}z$":
                  ETA[4] * diagonal["omega"][4, 4, 7]}''',
     '''    pieces = {"$\\\\omega_{x_1,(1)(4)} = a_4'e^{a_4}\\\\sin^{1/6}z$": diagonal["omega"][1, 1, 4],
              "$\\\\omega_{x_1,(1)(0)} = He^{a_4}\\\\sin^{1/6}z$": diagonal["omega"][1, 1, 0],
              "$|\\\\omega_{x_5,(4)(5)}| = a_4'e^{-a_4}\\\\sin^{1/6}z$":
                  -ETA[4] * diagonal["omega"][5, 4, 5],
              "$|\\\\omega_{x_5,(5)(0)}| = He^{-a_4}\\\\sin^{1/6}z$":
                  ETA[5] * diagonal["omega"][5, 5, 0]}'''),
    ('''    inflating = along_history(sum(coefficient_4[:3]))(times) * np.ones_like(times)
    deflating = along_history(sum(coefficient_4[4:7]))(times) * np.ones_like(times)''',
     '''    inflating = along_history(sum(coefficient_4[1:4]))(times) * np.ones_like(times)
    deflating = along_history(sum(coefficient_4[5:8]))(times) * np.ones_like(times)'''),
    # boosted frame
    ("    rapidity = beta * x[3] + b0\n", "    rapidity = beta * x[4] + b0\n"),
    ('''    formula = (6 * H - beta) / 2 * (sp.cosh(rapidity) * G[7] - sp.sinh(rapidity) * G[3])''',
     '''    formula = (6 * H - beta) / 2 * (sp.cosh(rapidity) * G[0] - sp.sinh(rapidity) * G[4])'''),
    ('''    nonzero_text = ", ".join(f"x{mu + 1}" for mu in nonzero_Omega)  # "x1, x2, ..."''',
     '''    nonzero_text = ", ".join(f"x{mu}" for mu in nonzero_Omega)  # "x1, x2, ..."'''),
    ('''                 and nonzero_Omega == [0, 1, 2, 3, 4, 5, 6],''',
     '''                 and nonzero_Omega == [1, 2, 3, 4, 5, 6, 7],'''),
    ('''    term = sp.lambdify((beta, x[3], b0), formula.subs(H, 1), "numpy")''',
     '''    term = sp.lambdify((beta, x[4], b0), formula.subs(H, 1), "numpy")'''),
    # curvature
    ('''        """F_x1x0 = d_1 Omega_8 - d_8 Omega_1 + [Omega_1, Omega_8]."""
        O1, O8 = fr["Omega"][0], fr["Omega"][7]
        return sp.diff(O8, x[0]) - sp.diff(O1, x[7]) + O1 * O8 - O8 * O1''',
     '''        """F_x1x0 = d_1 Omega_0 - d_0 Omega_1 + [Omega_1, Omega_0]."""
        O1, O0 = fr["Omega"][1], fr["Omega"][0]
        return sp.diff(O0, x[1]) - sp.diff(O1, x[0]) + O1 * O0 - O0 * O1'''),
    ('''                value = g[rho] * riemann(rho, sigma, 0, 7)  # lower the first index''',
     '''                value = g[rho] * riemann(rho, sigma, 1, 0)  # lower the first index'''),
    ('''    P14, P18 = G[0] * G[3], G[0] * G[7]  # gamma^(1) gamma^(4) and gamma^(1) gamma^(8)''',
     '''    P14, P10 = G[1] * G[4], G[1] * G[0]  # gamma^(1) gamma^(4) and gamma^(1) gamma^(0)'''),
    ('''        """c14, c18 with F = c14 P14 + c18 P18 (P14^2 = 1, P18^2 = -1), and whether''',
     '''        """c14, c10 with F = c14 P14 + c10 P10 (P14^2 = 1, P10^2 = -1), and whether'''),
    ('''        c18 = sp.simplify(-(P18 * F).trace() / 16)
        return c14, c18, all(is_zero(v) for v in F - c14 * P14 - c18 * P18)''',
     '''        c10 = sp.simplify(-(P10 * F).trace() / 16)
        return c14, c10, all(is_zero(v) for v in F - c14 * P14 - c10 * P10)'''),
    ('''    c14, c18, only_two = two_coefficients(F_diagonal)
    c14_b, c18_b, only_two_b = two_coefficients(F_zero)
    say(f"diagonal frame: c14 = {c14}")
    say(f"diagonal frame: c18 = {c18}")
    say(f"boosted frame:  c14 = {c14_b}")
    say(f"boosted frame:  c18 = {c18_b}")
    check(only_two and only_two_b,
          "in both frames F_x1x0 = c14 gamma^(1) gamma^(4) + c18 gamma^(1) gamma^(8)")''',
     '''    c14, c10, only_two = two_coefficients(F_diagonal)
    c14_b, c10_b, only_two_b = two_coefficients(F_zero)
    say(f"diagonal frame: c14 = {c14}")
    say(f"diagonal frame: c10 = {c10}")
    say(f"boosted frame:  c14 = {c14_b}")
    say(f"boosted frame:  c10 = {c10_b}")
    check(only_two and only_two_b,
          "in both frames F_x1x0 = c14 gamma^(1) gamma^(4) + c10 gamma^(1) gamma^(0)")'''),
    ('''    check(is_zero(c14**2 - c18**2 - kappa_F) and is_zero(c14_b**2 - c18_b**2 - kappa_F),''',
     '''    check(is_zero(c14**2 - c10**2 - kappa_F) and is_zero(c14_b**2 - c10_b**2 - kappa_F),'''),
    ('''        concrete = concrete.subs({H: 1, x[7]: sp.pi / 24, x[3]: sp.Rational(1, 2), b0: 0})''',
     '''        concrete = concrete.subs({H: 1, x[0]: sp.pi / 24, x[4]: sp.Rational(1, 2), b0: 0})'''),
    ('''                "The spinor curvature $F_{x_1x_0} = \\\\partial_1\\\\Omega_8 - "
                "\\\\partial_0\\\\Omega_1 + \\\\Omega_1\\\\Omega_8 - \\\\Omega_8\\\\Omega_1$ as a "''',
     '''                "The spinor curvature $F_{x_1x_0} = \\\\partial_1\\\\Omega_0 - "
                "\\\\partial_0\\\\Omega_1 + \\\\Omega_1\\\\Omega_0 - \\\\Omega_0\\\\Omega_1$ as a "'''),
    # energy-momentum tensor
    ('''    g4_up, Omega_1 = diagonal["gamma"][3], diagonal["Omega"][0]''',
     '''    g4_up, Omega_1 = diagonal["gamma"][4], diagonal["Omega"][1]'''),
    ('''    target = sp.exp(a4) * sixth * H * G[3] * G[0] * G[7] / 2''',
     '''    target = sp.exp(a4) * sixth * H * G[4] * G[1] * G[0] / 2'''),
    ('''                 and C * G[3] * G[0] * G[7] != sp.zeros(16, 16),''',
     '''                 and C * G[4] * G[1] * G[0] != sp.zeros(16, 16),'''),
    ('''                 "gamma^(1) gamma^(8), and C gamma^(4) gamma^(1) gamma^(8) != 0",''',
     '''                 "gamma^(1) gamma^(0), and C gamma^(4) gamma^(1) gamma^(0) != 0",'''),
    # summary
    (r'''    - The canonical spin connection of the diagonal frame has 12 independent nonzero
      components, each $a_4'$ or $H$ times a factor that never vanishes,''',
     r'''    - On the background $b_4 = 1$: the canonical spin connection of the diagonal frame
      has 12 independent nonzero components, each $a_4'$ or $H$ times a factor that
      never vanishes,'''),
    (r'''      deflation of the extra times enters the field equation only through the frame
      factors $e^{\mp a_4}\sin^{-1/6}z$ of the derivative terms (PROVED).''',
     r'''      deflation of the extra times enters the field equation only through the frame
      factors $e^{\mp a_4}\sin^{-1/6}z$ of the derivative terms (PROVED). For a general
      $b_4$ the term is $3H\gamma^{(0)} + \frac34(b_4'/b_4)\gamma^{(4)}$ and the
      extra-time factor $e^{a_4}b_4^{-1/2}\sin^{-1/6}z$ (Chapter 6, Notebook 06a).'''),
]
s = strict_replace(s, pairs, "08c")
p.write_bytes(s.encode("utf-8"))
print("ok")
