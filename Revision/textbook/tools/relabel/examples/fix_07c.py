"""07c builder: the author's coordinates x0..x7 (gammas.json is in that order) and the metric with b4."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from relabel_common import REPO, strict_replace  # noqa: E402

p = REPO / "Revision/textbook/notebooks/src/07c_real_fields.py"
s = p.read_text(encoding="utf-8")
pairs = [
    ("    GAMMA = G[7] * G[0] * G[1] * G[2] * G[3] * G[4] * G[5] * G[6]  # chirality\n",
     "    GAMMA = G[0] * G[1] * G[2] * G[3] * G[4] * G[5] * G[6] * G[7]  # chirality\n"),
    ("    X4, X8 = 3, 7  # list positions of x4 and x0\n",
     "    X0, X4 = 0, 4  # list positions of x0 and x4\n"),
    ('''    LEAD = "Revision/lead_checks/reports/charge-conjugation-and-u1.json"
''',
     '''    LEAD = "Revision/lead_checks/reports/charge-conjugation-and-u1.json"
    PYREP_B4 = "Revision/theory/reports/python-field-theory-b4.json"  # the metric with b4
'''),
    (r'''    The next cell rebuilds, exactly as Notebook 07b does step by step, the coefficient
    ring, the diagonal frame $f = (Es, Es, Es, 1, s/E, s/E, s/E, c/s^6)$, the
    Christoffel symbols of the diagonal metric, the canonical spin connection
    $\omega_{\mu ab}$, the spinor connection $\Omega_\mu = \sum_{a<b}\omega_{\mu ab}
    S^{ab}$ and the coordinate gammas $\gamma^\mu = \gamma^{(\mu)}/f_\mu$. It then
    checks two things. First, every entry of every $\Omega_\mu$ and $\gamma^\mu$ is real
    (real gammas times the real functions $e^{\pm a_4}$, $\sin^{1/6}z$, $\cot z$, $a_4'$
    and $H$; no imaginary unit $i$ anywhere): the operator $\gamma^\mu D_\mu$ is REAL,
    so the complex conjugate of a solution is again a solution, and real fields are a
    consistent restriction. Second, as a consistency check, $\gamma^\mu\Omega_\mu =
    3H\gamma^{(x_0)}$, the value of the Revision record.''',
     r'''    The next cell rebuilds, exactly as Notebook 07b does step by step, the coefficient
    ring, the diagonal frame $f = (c/s^6, Es, Es, Es, 1, s\sqrt b/E, s\sqrt b/E,
    s\sqrt b/E)$ of the metric with $b_4$ (in the order $x_0, \dots, x_7$; $b$ stands
    for $b_4(x_4)$ and `b1`, `b2`, `b3` for its derivatives), the Christoffel symbols of
    the diagonal metric, the canonical spin connection $\omega_{\mu ab}$, the spinor
    connection $\Omega_\mu = \sum_{a<b}\omega_{\mu ab}S^{ab}$ and the coordinate gammas
    $\gamma^\mu = \gamma^{(\mu)}/f_\mu$. It then checks two things, for arbitrary
    functions $a_4$ and $b_4 > 0$. First, every entry of every $\Omega_\mu$ and
    $\gamma^\mu$ is real (real gammas times the real functions $e^{\pm a_4}$,
    $\sin^{1/6}z$, $\cot z$, $b_4^{1/2}$, $a_4'$, $b_4'$ and $H$; no imaginary unit $i$
    anywhere): the operator $\gamma^\mu D_\mu$ is REAL, so the complex conjugate of a
    solution is again a solution, and real fields are a consistent restriction. Second,
    as a consistency check, $\gamma^\mu\Omega_\mu = 3H\gamma^{(x_0)} +
    \frac34(b_4'/b_4)\gamma^{(x_4)}$, the value of the Revision record with $b_4$, which
    is $3H\gamma^{(x_0)}$ at $b_4 = 1$.'''),
    ('''    A1, A2, A3 = sp.symbols("A1 A2 A3", real=True)  # derivatives of a4 (1st to 3rd)
''',
     '''    A1, A2, A3 = sp.symbols("A1 A2 A3", real=True)  # derivatives of a4 (1st to 3rd)
    b = sp.Symbol("b", positive=True)  # b4(x4) > 0
    b1, b2, b3 = sp.symbols("b1 b2 b3", real=True)  # derivatives of b4 (1st to 3rd)
'''),
    ('''        if mu == X4:
            return (sp.diff(expression, E) * E * A1 + sp.diff(expression, A1) * A2
                    + sp.diff(expression, A2) * A3)
        if mu == X8:''',
     '''        if mu == X4:
            return (sp.diff(expression, E) * E * A1 + sp.diff(expression, A1) * A2
                    + sp.diff(expression, A2) * A3 + sp.diff(expression, b) * b1
                    + sp.diff(expression, b1) * b2 + sp.diff(expression, b2) * b3)
        if mu == X0:'''),
    ("    f = [E * s] * 3 + [sp.Integer(1)] + [s / E] * 3 + [c / s**6]  # the frame\n",
     "    f = [c / s**6] + [E * s] * 3 + [sp.Integer(1)] + [s * sp.sqrt(b) / E] * 3  # frame\n"),
    ("    sqrt_g = sp.prod(f)  # = c = cos z\n",
     "    sqrt_g = sp.prod(f)  # = b^(3/2) c = b4^(3/2) cos z\n"),
    ('''    check(real_entries, "every entry of every Omega_mu and gamma^mu is real: gamma^mu "
          "D_mu is a real operator", record=reproduces(LEAD, "spinor_connection_real"))
    total = sum((gam[mu] * Om[mu] for mu in range(8)), Z16)
    check(all(is_zero(v) for v in (total - 3 * H * G[X8])),
          "gamma^mu Omega_mu = 3 H gamma^(x0), the value of the Revision record",
          record=reproduces(PYREP, "gamma_mu_Omega_mu_equals_3H_gamma_x0"))''',
     '''    check(real_entries, "every entry of every Omega_mu and gamma^mu is real, for every "
          "b4: gamma^mu D_mu is a real operator",
          record=reproduces(PYREP_B4, "spinor_connection_real_b4") + "; at b4 = 1 "
          + reproduces(LEAD, "spinor_connection_real"))
    total = sum((gam[mu] * Om[mu] for mu in range(8)), Z16)
    at_b4_1 = {b: 1, b1: 0, b2: 0, b3: 0}  # the background b4 = 1
    check(all(is_zero(v) for v in (total - 3 * H * G[X0] - 3 * b1 / (4 * b) * G[X4]))
          and all(is_zero(v) for v in (total.subs(at_b4_1) - 3 * H * G[X0])),
          "gamma^mu Omega_mu = 3 H gamma^(x0) + (3/4)(b4'/b4) gamma^(x4), and "
          "3 H gamma^(x0) at b4 = 1: the values of the Revision records",
          record=reproduces(PYREP_B4, "gammaOmega_total") + "; at b4 = 1 "
          + reproduces(PYREP, "gamma_mu_Omega_mu_equals_3H_gamma_x0"))'''),
    (r'''    **A real solution and its image.** Notebook 07b verified the exact family $\Psi =
    \sin^\alpha z\,(\cosh kx_4 + \sinh(kx_4)/k\,M)\chi_0$ with $M = -m\gamma^{(x_4)} +
    3H(2\alpha + 1)\gamma^{(x_4)}\gamma^{(x_0)}$.''',
     r'''    **A real solution and its image.** Notebook 07b verified the exact family $\Psi =
    \sin^\alpha z\,(\cosh kx_4 + \sinh(kx_4)/k\,M)\chi_0$ with $M = -m\gamma^{(x_4)} +
    3H(2\alpha + 1)\gamma^{(x_4)}\gamma^{(x_0)}$ on the background $b_4 = 1$ (for a
    changing $b_4$ the extra term $\frac34(b_4'/b_4)\gamma^{(x_4)}$ of the field equation
    changes the family; this cell stays at $b_4 = 1$).'''),
    ("        return -mass * G[X4] + 3 * H * G[X4] * G[X8]  # alpha = 0\n",
     "        return -mass * G[X4] + 3 * H * G[X4] * G[X0]  # alpha = 0, b4 = 1\n"),
    ("    Mf = -2.0 * Gf[X4] + 3.0 * Gf[X4] @ Gf[X8]  # m = 2, H = 1\n",
     "    Mf = -2.0 * Gf[X4] + 3.0 * Gf[X4] @ Gf[X0]  # m = 2, H = 1, b4 = 1\n"),
    ('''        """The largest component of gamma4 d4 Psi + 3 gamma8 Psi - mass Psi."""
        return np.array([np.abs(Gf[X4] @ d + 3.0 * Gf[X8] @ v - mass * v).max()''',
     '''        """The largest component of gamma4 d4 Psi + 3 gamma0 Psi - mass Psi."""
        return np.array([np.abs(Gf[X4] @ d + 3.0 * Gf[X0] @ v - mass * v).max()'''),
    (r'''    The product of all eight gammas in the order $x_0, \dots, x_7$ is $\pm\Gamma$ (the
    sign depends only on the order of the factors), so the second space is spanned by
    $\Gamma$.''',
     r'''    The product of all eight gammas in the order $x_0, \dots, x_7$ is $\Gamma$ (in
    another order of the factors it may be $-\Gamma$), so the second space is spanned by
    $\Gamma$.'''),
]
s = strict_replace(s, pairs, "07c")
assert "X8" not in s, [l for l in s.splitlines() if "X8" in l]
p.write_bytes(s.encode("utf-8"))
print("ok")
