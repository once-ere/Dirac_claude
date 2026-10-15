#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
"""Builder of Notebook 06b, "What depends on the frame and what does not"
(textbook "Universes in Pairs", chapter 06).

The notebook Revision/textbook/notebooks/06b_frame_dependence.ipynb is BUILT from this
file by Revision/textbook/tools/nbkit.py (never edit the .ipynb by hand):

    python Revision/textbook/tools/nbkit.py build \
        Revision/textbook/notebooks/src/06b_frame_dependence.py --date YYYY-MM-DD
    python Revision/textbook/tools/nbkit.py check \
        Revision/textbook/notebooks/src/06b_frame_dependence.py

Physics source (the Revision record): Revision/theory/reports/python-scope.json and
wolfram-scope.json (frame dependence, rescaling, blindness to the deflation; the metric
at b4 = 1), Revision/theory/field-theory.json (Ricci tensor at b4 = 1),
Revision/metric_b4/results/metric-b4.json (Ricci tensor with b4) and the field-theory
reports (spinor curvature).  The author's coordinates x0..x7: x0 the hidden direction
(z = 6 H x0), x1, x2, x3 3-space (inflating), x4 the time, x5, x6, x7 the three extra
times (deflating exponentially).
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools"))
from nbkit import code, md, run_builder  # noqa: E402

FIGURES = [
    "boost_hyperbolas",
    "boosted_contraction",
    "boosted_connection_heat_maps",
    "ricci_components",
    "spinor_curvature_norms",
    "rescaling",
]

FACTS = {
    "id": "06b",
    "name": "06b_frame_dependence",
    "title": "What depends on the frame: boosts, spin covariance, curvature, rescaling",
    "purpose": (
        "For the author's metric with the functions a4(x4) and b4(x4) it boosts the "
        "diagonal vielbein in the (x4, x0) plane with a time-dependent rapidity and "
        "computes exactly, with sympy, the new spin connection and the new contraction "
        "gamma^mu Omega_mu = ((6 H - beta)/2)(cosh b gamma^(x0) - sinh b gamma^(x4)) + "
        "(3/4)(b4'/b4)(cosh b gamma^(x4) - sinh b gamma^(x0)), which vanishes "
        "identically for the rapidity rate beta = 6 H when b4 is constant; it verifies "
        "the local spin covariance of the connection with an explicit spinor boost, "
        "computes the Riemann and Ricci tensors and the curvature of the spinor "
        "connection, which no frame can remove, shows that the rescaling "
        "Psi = sin^(-1/2)(z) b4^(-3/4) chi removes the whole term gamma^mu Omega_mu, "
        "checks every result against the Revision records and draws six teaching plots."
    ),
    "records": [
        ["Revision/algebra/gammas.json",
         "the author's eight real 16 x 16 gamma matrices and the matrix C (input)"],
        ["Revision/theory/field-theory.json",
         "the exact formulas at b4 = 1: the Ricci tensor and the Ricci scalar "
         "(reproduced at b4 = 1)"],
        ["Revision/metric_b4/results/metric-b4.json",
         "the mixed Ricci tensor and the Ricci scalar of the metric with b4 "
         "(reproduced)"],
        ["Revision/theory/reports/python-scope.json",
         "the sympy checks of the scope statements at b4 = 1: boosted frame, rescaling, "
         "blindness to the deflation (reproduced at b4 = 1)"],
        ["Revision/theory/reports/wolfram-scope.json",
         "the WolframScript checks of the same scope statements (reproduced at b4 = 1)"],
        ["Revision/theory/reports/python-field-theory.json",
         "the sympy checks of the curvature and of the spinor curvature at b4 = 1"],
        ["Revision/theory/reports/wolfram-field-theory.json",
         "the WolframScript checks of the curvature at b4 = 1"],
        ["Revision/theory/reports/wolfram-field-theory-b4.json",
         "the WolframScript checks of the curvature and of the spinor curvature with b4 "
         "(reproduced)"],
    ],
    "packages": ["numpy", "sympy", "matplotlib"],
    "needs_rust": [],
    "expected_seconds": 120,
    "timeout_seconds": 900,
    "files_written": (
        ["Revision/textbook/figures/06b.captions.json"]
        + [f"Revision/textbook/figures/06b_{k}_{name}.png"
           for k, name in enumerate(FIGURES, 1)]
    ),
    "final_lines": [
        "PASS all six figure files exist",
        "ALL 26 CHECKS PASSED (notebook 06b)",
    ],
    "troubleshooting": [
        ["\"FileNotFoundError\" for Revision/algebra/gammas.json or for a report",
         "the notebook reads Revision records from the repository; open it inside the "
         "folder Revision/textbook/notebooks of a complete copy of the repository "
         "Dirac_claude (a single downloaded notebook file is not enough)."],
        ["a cell runs for several minutes",
         "the exact algebra of sympy with hyperbolic functions and two unknown functions "
         "is slow on old computers; the whole notebook needs about two minutes on a 2024 "
         "laptop, and up to about four minutes while other programs use the processor. "
         "Wait, or close the other programs."],
    ],
}

CELLS = [
    md(r"""
    ## 1. What this notebook computes

    The previous notebook of this chapter (06a) found $\gamma^\mu\Omega_\mu =
    3H\gamma^{(x0)} + \frac34(b_4'/b_4)\gamma^{(x4)}$ for the author's metric in the
    DIAGONAL vielbein ($3H\gamma^{(x0)}$ when $b_4$ is constant). A vielbein is a
    choice: at every point any other set of eight perpendicular unit directions
    describes the same metric. This notebook asks which results depend on that choice
    and which do not. It

    - builds a second vielbein of the same metric, the diagonal one **boosted** in the
      plane of the time $x4$ and the hidden direction $x0$ by a rapidity
      $b = \beta x_4 + b_0$ that grows with the time;
    - computes its canonical spin connection and finds exactly
      $\gamma'^\mu\Omega'_\mu = \frac{6H - \beta}{2}\big(\cosh b\,\gamma^{(x0)} -
      \sinh b\,\gamma^{(x4)}\big) + \frac34\frac{b_4'}{b_4}\big(\cosh b\,
      \gamma^{(x4)} - \sinh b\,\gamma^{(x0)}\big)$, which VANISHES for $\beta = 6H$
      when $b_4$ is constant, although $\Omega'_\mu$ itself does not vanish;
    - explains the formula with the **local spin covariance** of the connection,
      using the explicit spinor boost $R = \cosh\frac{b}{2} -
      \sinh\frac{b}{2}\,\gamma^{(x4)}\gamma^{(x0)}$;
    - computes the Riemann and Ricci tensors and the curvature
      $F_{\mu\nu}$ of the spinor connection, checks $F_{\mu\nu} =
      \frac12 R_{ab\mu\nu}S^{ab}$ in all 28 coordinate planes, and shows that this
      curvature, which no choice of frame can remove, is nonzero for every $H > 0$;
    - shows that the rescaled field $\chi = \sin^{1/2}(z)\,b_4^{3/4}\,\Psi$ obeys an
      equation without the term $\gamma^\mu\Omega_\mu$;
    - checks every result against the Revision records (with $b_4$ where the record has
      it, and at $b_4 = 1$) and draws six teaching plots.
    """),
    md(r"""
    ## 3. The words used in this notebook

    - **Vielbein** $e^a{}_\mu$: eight perpendicular unit directions at every point
      (frame index $a$, coordinate index $\mu$), with $g_{\mu\nu} = \sum_a \eta_{aa}
      e^a{}_\mu e^a{}_\nu$; $\eta = \mathrm{diag}(+1,+1,+1,+1,-1,-1,-1,-1)$ in the
      order $x0, \dots, x7$. In Python lists the directions have the positions 0 to 7
      in the same order, so `x[0]` is $x0$ and `x[4]` is $x4$.
    - **Frame rotation** (local Lorentz transformation): a new vielbein
      $e'^a{}_\mu = \sum_b \Lambda^a{}_b(x)\,e^b{}_\mu$ with a matrix $\Lambda(x)$
      that keeps $\eta$: $\Lambda^T\eta\Lambda = \eta$. It describes the same metric.
    - **Boost**: a frame rotation that mixes one space-like and one time-like
      direction. In the plane of the time $x4$ (time-like) and the hidden direction
      $x0$ (space-like) it is $e'^{(x4)} = \cosh b\, e^{(x4)} + \sinh b\, e^{(x0)}$,
      $e'^{(x0)} = \sinh b\, e^{(x4)} + \cosh b\, e^{(x0)}$.
    - **Rapidity** $b$: the "angle" of a boost. **Hyperbolic functions**:
      $\cosh b = (e^b + e^{-b})/2$ and $\sinh b = (e^b - e^{-b})/2$; they satisfy
      $\cosh^2 b - \sinh^2 b = 1$, just as $\cos^2 + \sin^2 = 1$ for rotations.
    - **Spin connection** $\omega_{\mu ab}$, **spinor connection** $\Omega_\mu =
      \frac12\sum_{a,b}\omega_{\mu ab}S^{ab}$ with $S^{ab} = \frac14[\gamma^a,
      \gamma^b]$, **curved gammas** $\gamma^\mu = \sum_a e_a{}^\mu\gamma^a$,
      **covariant derivative** $D_\mu = \partial_\mu + \Omega_\mu$: as in Notebook
      06a. A prime marks the quantities of the boosted vielbein.
    - **Spinor boost** $R(x)$: a 16 x 16 matrix that turns spinors when the frame is
      boosted; it **covers** $\Lambda$ when $R^{-1}\gamma^a R = \sum_b \Lambda^a{}_b
      \gamma^b$ for every $a$.
    - **Riemann tensor** $R^\rho{}_{\sigma\mu\nu}$: the measure of curvature, built
      from the Christoffel symbols and their derivatives; it is zero everywhere only
      for a flat space. **Ricci tensor** $R_{\sigma\nu} = \sum_\rho
      R^\rho{}_{\sigma\rho\nu}$, mixed form $R^\mu{}_\nu = \sum_\sigma g^{\mu\sigma}
      R_{\sigma\nu}$, **Ricci scalar** $R = \sum_\mu R^\mu{}_\mu$.
    - **Curvature of the spinor connection** $F_{\mu\nu} = \partial_\mu\Omega_\nu -
      \partial_\nu\Omega_\mu + [\Omega_\mu, \Omega_\nu]$: the 16 x 16 matrix with
      $D_\mu D_\nu\Psi - D_\nu D_\mu\Psi = F_{\mu\nu}\Psi$.
    - **Frame-dependent**: a quantity whose value changes when the vielbein is
      changed (such as $\gamma^\mu\Omega_\mu$). **Frame-independent**: a statement
      that holds in every vielbein (such as "$F_{\mu\nu}$ is not zero").
    - **Rescaling**: writing the field as a known function times a new field,
      $\Psi = w(x)\,\chi$, and deriving the equation that $\chi$ obeys.
    - **Exact** check: sympy proves that an expression is zero for ALL values of its
      symbols. **Heat map**: a picture of a matrix, red positive, blue negative,
      white zero.
    """),
    md(r"""
    ## 4. The physical and mathematical situation

    The metric is the author's, with $z = 6Hx_0$ in $(0, \pi/2)$, $H > 0$ and two
    arbitrary functions $a_4(x_4)$ and $b_4(x_4) > 0$:

    $$g = \mathrm{diag}\big(\cot^2 z,\ e^{2a_4}\sin^{1/3}z\ (\times 3),\ -1,\
    -e^{-2a_4}b_4\sin^{1/3}z\ (\times 3)\big).$$

    The diagonal vielbein has the factors $f = (\cot z,\ e^{a_4}s\ (\times 3),\ 1,\
    e^{-a_4}b_4^{1/2}s\ (\times 3))$, $s = \sin^{1/6}z$. On the backgrounds of this
    book $b_4 = 1$. The canonical spin connection of ANY vielbein $e$ is
    $\omega_\mu{}^a{}_b = \sum_\nu e^a{}_\nu (\partial_\mu e_b{}^\nu +
    \sum_\lambda\Gamma^\nu{}_{\mu\lambda}e_b{}^\lambda)$.

    **The theorem behind this notebook (local spin covariance).** If $e' = \Lambda e$
    and the spinor matrix $R(x)$ covers $\Lambda(x)$, then

    $$\Omega'_\mu = R\,\Omega_\mu R^{-1} - (\partial_\mu R)R^{-1}, \qquad
    \gamma'^\mu = R\,\gamma^\mu R^{-1}, \qquad F'_{\mu\nu} = R\,F_{\mu\nu}R^{-1}.$$

    Multiplying the first two and summing over $\mu$ gives

    $$\gamma'^\mu\Omega'_\mu = R\,(\gamma^\mu\Omega_\mu)\,R^{-1} -
    \sum_\mu\gamma'^\mu(\partial_\mu R)R^{-1}.$$

    The second term can cancel the first: the contraction $\gamma^\mu\Omega_\mu$ is
    frame-dependent. The curvature only gets turned by $R$, so if $F_{\mu\nu} \ne 0$
    in one frame, it is nonzero in every frame: no frame removes the spinor
    connection itself.

    **Status.** Every statement checked below is PROVED exactly (sympy, symbolic $H$,
    $a_4$, $b_4$, $\beta$, $b_0$). The scope records (`python-scope.json`,
    `wolfram-scope.json`) state these results for the metric at $b_4 = 1$; the notebook
    reproduces them there and computes the general case itself. This is the record's
    own correction of the non-triviality statement: the value of
    $\gamma^\mu\Omega_\mu$ belongs to the diagonal vielbein; what is
    frame-independent is the curvature.
    """),
    md(r"""
    ## 5. The tools: sympy, the author's gammas and the general formulas

    This notebook repeats the tools of Notebook 06a, so that it runs on its own. The
    next cell reads the author's gammas and the matrix $C$ from
    `Revision/algebra/gammas.json`, checks the 64 Clifford relations, builds the 28
    matrices $S^{ab}$, and defines the exact zero test `is_zero` (first a fast route
    through exponential functions, then sympy's `simplify`; it never calls a nonzero
    expression zero) and `record_passed`, which reads a Revision report and tells
    whether a check is recorded as passed.

    The first lines of the next cell change one setting of Jupyter: printed text is
    sent to the screen when a cell has finished (or just before a figure is shown),
    not every 0.2 seconds. This changes no result; it makes the printed text arrive in
    the same pieces in every run, which the book's checking tool needs.
    """),
    code(r'''
    import sys  # the Python system module (here: the stream of printed text)

    # Jupyter sends printed text to the screen in pieces, about every 0.2 seconds.  The
    # book's checking tool reads each PASS line together with its "reproduces" line, so
    # the pieces must be the same in every run: send the printed text of a cell in one
    # piece when the cell ends (or just before a figure), at the latest after 600 s.
    if hasattr(sys.stdout, "flush_interval"):  # true inside Jupyter only
        sys.stdout.flush_interval = 600.0
    import numpy as np  # decimal numbers for the plots
    import sympy as sp  # exact algebra and calculus with symbols
    from sympy.parsing.mathematica import parse_mathematica  # reads Wolfram notation

    fixture = json.loads(repository_file("Revision/algebra/gammas.json").read_text(
        encoding="utf-8"))
    NAMES = fixture["coordinates"]  # ["x0", ..., "x7"]
    ETA = fixture["eta"]  # +1 space-like, -1 time-like
    gamma = [sp.Matrix(rows) for rows in fixture["gamma"]]  # gamma[a] = gamma^(xa)
    C = sp.Matrix(fixture["C"])  # the author's C (Dirac adjoint Psibar = Psi^dagger C)
    I16, Z16 = sp.eye(16), sp.zeros(16, 16)
    check(all(gamma[a] * gamma[b] + gamma[b] * gamma[a]
              == (2 * ETA[a] if a == b else 0) * I16
              for a in range(8) for b in range(8)),
          "the 64 Clifford relations of the author's gammas")
    S = [[(gamma[a] * gamma[b] - gamma[b] * gamma[a]) / 4 for b in range(8)]
         for a in range(8)]


    def is_zero(expr):
        """True when expr is exactly zero for all values of its symbols."""
        expr = sp.sympify(expr)
        if expr == 0:
            return True
        if sp.cancel(sp.expand(expr.rewrite(sp.exp))) == 0:  # the fast route
            return True
        return sp.simplify(expr) == 0  # the slower general route


    def matrix_is_zero(matrix):
        return all(is_zero(entry) for entry in matrix)


    def record_passed(path, name):
        """True when the Revision report at path records the check name as passed."""
        data = json.loads(repository_file(path).read_text(encoding="utf-8"))
        for entry in data["checks"]:
            if entry["name"] == name:
                return entry["verdict"].upper() == "PASS"
        raise KeyError(f"{path} has no check {name}")


    SCOPE_PY = "Revision/theory/reports/python-scope.json"
    SCOPE_WL = "Revision/theory/reports/wolfram-scope.json"
    REPORT_PY = "Revision/theory/reports/python-field-theory.json"
    REPORT_WL = "Revision/theory/reports/wolfram-field-theory.json"
    REPORT_WL_B4 = "Revision/theory/reports/wolfram-field-theory-b4.json"
    THEORY_FILE = "Revision/theory/field-theory.json"
    METRIC_B4_FILE = "Revision/metric_b4/results/metric-b4.json"
    '''),
    md(r"""
    The next cell defines the four general formulas as Python functions, exactly as
    in Notebook 06a: `christoffel(g, coords)` gives $\Gamma^l{}_{mn}$;
    `spin_connection(e, Gam, coords, eta)` gives $\omega_{\mu ab}$ for any vielbein
    matrix `e` (row = frame index, column = coordinate; its inverse `E = e.inv()` has
    `E[nu, b]` $= e_b{}^\nu$); `spinor_connection(omega, S)` gives $\Omega_\mu =
    \sum_{a<b}\omega_{\mu ab}S^{ab}$; `curved_gammas(e, gammas)` gives $\gamma^\mu =
    \sum_a e_a{}^\mu\gamma^a$. For the boosted vielbein the entries contain
    $\cosh$ and $\sinh$; `spin_connection` simplifies every entry, which is the
    slowest step of the notebook.
    """),
    code(r'''
    def christoffel(g, coords):
        """Gam[l][m][n] = (1/2) sum_r g^lr (d_m g_rn + d_n g_rm - d_r g_mn)."""
        n = len(coords)
        g_inv = g.inv()
        Gam = [[[sp.Integer(0)] * n for _ in range(n)] for _ in range(n)]
        for l in range(n):
            for m in range(n):
                for k in range(m, n):
                    value = sum(g_inv[l, r] * (sp.diff(g[r, k], coords[m])
                                               + sp.diff(g[r, m], coords[k])
                                               - sp.diff(g[m, k], coords[r]))
                                for r in range(n) if g_inv[l, r] != 0) / 2
                    Gam[l][m][k] = Gam[l][k][m] = sp.simplify(value)
        return Gam


    def spin_connection(e, Gam, coords, eta):
        """omega[mu][a][b] = eta_aa sum_nu e^a_nu (d_mu e_b^nu + Gam^nu_mu,lam e_b^lam)."""
        n = len(coords)
        E = e.inv()  # E[nu, b] = e_b^nu
        omega = [[[sp.Integer(0)] * n for _ in range(n)] for _ in range(n)]
        for mu in range(n):
            for a in range(n):
                for b in range(n):
                    mixed = 0
                    for nu in range(n):
                        if e[a, nu] == 0:
                            continue
                        mixed += e[a, nu] * (sp.diff(E[nu, b], coords[mu]) + sum(
                            Gam[nu][mu][lam] * E[lam, b] for lam in range(n)))
                    omega[mu][a][b] = sp.simplify(eta[a] * mixed)
        return omega


    def spinor_connection(omega, S):
        """Omega[mu] = sum_{a<b} omega_{mu ab} S^ab."""
        n = len(omega)
        size = S[0][0].shape[0]
        return [sum((omega[mu][a][b] * S[a][b] for a in range(n)
                     for b in range(a + 1, n) if omega[mu][a][b] != 0),
                    sp.zeros(size, size)) for mu in range(n)]


    def curved_gammas(e, gammas):
        """gamma^mu = sum_a e_a^mu gamma^a."""
        E = e.inv()
        return [sum((E[mu, a] * gammas[a] for a in range(len(gammas))),
                    sp.zeros(*gammas[0].shape)) for mu in range(len(gammas))]


    say("defined: christoffel, spin_connection, spinor_connection, curved_gammas")
    '''),
    md(r"""
    ## 6. The diagonal vielbein again (the control)

    The next cell makes the symbols of the metric ($x0, \dots, x7$, $H > 0$, the
    functions $a_4(x_4)$ and $b_4(x_4) > 0$, $z = 6Hx_0$), the diagonal vielbein, the
    Christoffel symbols, the spin connection, $\Omega_\mu$ and the curved gammas, and
    checks the result of Notebook 06a, $\gamma^\mu\Omega_\mu = 3H\gamma^{(x0)} +
    \frac34(b_4'/b_4)\gamma^{(x4)}$, which at $b_4 = 1$ is the record's
    $3H\gamma^{(x0)}$. This is the CONTROL of the boosted computation: the same code,
    with no boost, must give the known value. The helper `at_b4_1` puts $b_4 = 1$
    into an expression and evaluates the derivatives of the constant 1 to 0.
    """),
    code(r'''
    x = sp.symbols("x0:8", real=True)  # x[0] = x0, ..., x[4] = x4, ..., x[7] = x7
    x0, x4 = x[0], x[4]
    H = sp.Symbol("H", positive=True)
    a4 = sp.Function("a4")(x4)  # any function of the time
    b4 = sp.Function("b4", positive=True)(x4)  # any positive function of the time
    a4p, b4p = sp.Derivative(a4, x4), sp.Derivative(b4, x4)
    z = 6 * H * x0
    s = sp.sin(z) ** sp.Rational(1, 6)
    f = ([sp.cot(z)] + [sp.exp(a4) * s] * 3 + [sp.Integer(1)]
         + [sp.exp(-a4) * sp.sqrt(b4) * s] * 3)  # f_0, ..., f_7
    g = sp.diag(*[ETA[a] * f[a] ** 2 for a in range(8)])  # the author's metric
    e = sp.diag(*f)  # the diagonal vielbein


    def at_b4_1(expr):
        """expr at b4 = 1; doit() evaluates the derivatives of the constant 1 to 0."""
        return sp.sympify(expr).subs({b4: 1}).doit()


    Gam = christoffel(g, x)
    omega = spin_connection(e, Gam, x, ETA)
    Omega = spinor_connection(omega, S)
    gup = curved_gammas(e, gamma)
    slash = sum((gup[mu] * Omega[mu] for mu in range(8)), Z16)
    c_b4 = sp.Rational(3, 4) * b4p / b4  # the coefficient (3/4) b4'/b4
    check(matrix_is_zero(slash - 3 * H * gamma[0] - c_b4 * gamma[4])
          and matrix_is_zero(at_b4_1(slash) - 3 * H * gamma[0]),
          "control: the diagonal vielbein gives gamma^mu Omega_mu = 3 H gamma^(x0) + "
          "(3/4)(b4'/b4) gamma^(x4), 3 H gamma^(x0) at b4 = 1",
          record=f"{SCOPE_PY}, check rescaling_removes_the_connection_term (b4 = 1)")
    '''),
    md(r"""
    ## 7. A boost of the frame in the plane of $x4$ and $x0$

    The next cell writes the boost matrix $\Lambda(b)$: the identity, except in the
    rows and columns of $x0$ (position 0) and $x4$ (position 4), where it is
    $\begin{pmatrix}\cosh b & \sinh b\\ \sinh b & \cosh b\end{pmatrix}$. It checks
    that $\Lambda^T\eta\Lambda = \eta$ for EVERY rapidity $b$; in the $(x0, x4)$
    block this is $\cosh^2 b - \sinh^2 b = +1$, $-\cosh^2 b + \sinh^2 b = -1$ and
    $\cosh b\sinh b - \sinh b\cosh b = 0$. It also checks that the inverse boost is
    the boost with $-b$.
    """),
    code(r'''
    def boost(b):
        """The 8 x 8 boost matrix Lambda(b) in the plane of x0 (index 0) and x4 (4)."""
        L = sp.eye(8)
        L[0, 0], L[0, 4], L[4, 0], L[4, 4] = sp.cosh(b), sp.sinh(b), sp.sinh(b), sp.cosh(b)
        return L


    b_symbol = sp.Symbol("b", real=True)  # a rapidity
    eta_matrix = sp.diag(*ETA)
    L_test = boost(b_symbol)
    check(matrix_is_zero(L_test.T * eta_matrix * L_test - eta_matrix),
          "Lambda(b)^T eta Lambda(b) = eta for every rapidity b")
    check(matrix_is_zero(L_test * boost(-b_symbol) - sp.eye(8)),
          "the inverse of the boost with rapidity b is the boost with -b")
    '''),
    md(r"""
    The next cell draws what a boost does to the two frame directions $e^{(x4)}$ and
    $e^{(x0)}$, drawn with their $x4$ component horizontally and their $x0$ component
    vertically, for the rapidities $b = 0, 0.5, 1$. A rotation would move them along
    a circle; a boost moves them along the two **unit hyperbolas** $t^2 - y^2 = 1$
    (where every vector has $\eta$-length $-1$, like the time direction) and
    $y^2 - t^2 = 1$ ($\eta$-length $+1$, like the hidden direction). Both arrows tilt
    towards the diagonal line $t = y$ (the "light line"), and they stay perpendicular
    in the sense of $\eta$.
    """),
    code(r'''
    fig, ax = plt.subplots(figsize=(6.4, 6.0))
    rapidity = np.linspace(-1.4, 1.4, 200)
    ax.plot(np.cosh(rapidity), np.sinh(rapidity), color="tab:blue", linewidth=1.0,
            label="unit hyperbola of the time direction: $t^2 - y^2 = 1$")
    ax.plot(np.sinh(rapidity), np.cosh(rapidity), color="tab:orange", linewidth=1.0,
            label="unit hyperbola of the hidden direction: $y^2 - t^2 = 1$")
    ax.plot([0, 2.2], [0, 2.2], ":", color="gray", label="light line $t = y$")
    for b_value, alpha in ((0.0, 1.0), (0.5, 0.7), (1.0, 0.45)):
        c_b, s_b = np.cosh(b_value), np.sinh(b_value)
        ax.annotate("", xy=(c_b, s_b), xytext=(0, 0), arrowprops=dict(
            arrowstyle="-|>", color="tab:blue", alpha=alpha, linewidth=1.6))
        ax.annotate("", xy=(s_b, c_b), xytext=(0, 0), arrowprops=dict(
            arrowstyle="-|>", color="tab:orange", alpha=alpha, linewidth=1.6))
        ax.text(c_b + 0.04, s_b - 0.12, f"$b = {b_value:g}$", fontsize=8,
                color="tab:blue")
        ax.text(s_b - 0.30, c_b + 0.06, f"$b = {b_value:g}$", fontsize=8,
                color="tab:orange")
    ax.set_xlim(-0.4, 2.3)
    ax.set_ylim(-0.25, 2.3)
    ax.set_aspect("equal")
    ax.set_xlabel("component along $e^{(x4)}$ (time), $t$")
    ax.set_ylabel("component along $e^{(x0)}$ (hidden direction), $y$")
    ax.set_title("A boost moves the frame along hyperbolas")
    ax.legend(fontsize=8, loc="upper left")
    save_figure(fig, "boost_hyperbolas",
                "A boost of the frame in the plane of the time $x4$ and the hidden "
                "direction $x0$. The boosted frame directions $e'^{(x4)} = \\cosh b\\, "
                "e^{(x4)} + \\sinh b\\, e^{(x0)}$ (blue arrows) and $e'^{(x0)} = "
                "\\sinh b\\, e^{(x4)} + \\cosh b\\, e^{(x0)}$ (orange arrows) for the "
                "rapidities $b = "
                "0, 0.5, 1$ (fainter for larger $b$), drawn with their $x4$ component $t$ "
                "horizontally and their $x0$ component $y$ vertically (pure numbers). "
                "They move along the unit hyperbolas $t^2 - y^2 = 1$ and $y^2 - t^2 = 1$ "
                "and tilt symmetrically towards the light line $t = y$ (dotted).")
    '''),
    md(r"""
    ## 8. The boosted vielbein and its canonical spin connection

    Now the rapidity depends on the time: $b = \beta x_4 + b_0$ with two constants
    $\beta$ (the rate) and $b_0$ (the starting value). The boosted vielbein is the
    matrix product $e' = \Lambda(b)\,e$. The next cell checks that it describes the
    author's metric (all 64 entries of $e'^T\eta e'$), computes its canonical spin
    connection, and checks the vielbein postulate (512 equations) and the
    antisymmetry $\omega'_{\mu ab} = -\omega'_{\mu ba}$, for every $b_4$. At $b_4 = 1$
    these are the record's checks `boosted_frame_reproduces_metric` and
    `boosted_frame_canonical_connection`.
    """),
    code(r'''
    beta, b0 = sp.symbols("beta b0", real=True)  # the rate and the start of the rapidity
    b = beta * x4 + b0  # the rapidity grows with the time
    L = boost(b)
    e_boosted = L * e  # e'^a_mu = sum_c Lambda^a_c e^c_mu
    check(matrix_is_zero(e_boosted.T * eta_matrix * e_boosted - g),
          "the boosted vielbein gives the author's metric (64 entries)",
          record=f"{SCOPE_PY}, check boosted_frame_reproduces_metric (b4 = 1)")
    omega_b = spin_connection(e_boosted, Gam, x, ETA)  # omega'_{mu ab}
    postulate = [sp.diff(e_boosted[a, nu], x[mu])
                 - sum(Gam[lam][mu][nu] * e_boosted[a, lam] for lam in range(8))
                 + sum(ETA[a] * omega_b[mu][a][c] * e_boosted[c, nu] for c in range(8))
                 for mu in range(8) for a in range(8) for nu in range(8)]
    antisymmetric = all(is_zero(omega_b[mu][a][c] + omega_b[mu][c][a])
                        for mu in range(8) for a in range(8) for c in range(8))
    check(all(is_zero(v) for v in postulate) and antisymmetric,
          "boosted vielbein: vielbein postulate (512) and antisymmetry of omega'",
          record=f"{SCOPE_PY}, check boosted_frame_canonical_connection (b4 = 1)")
    Omega_b = spinor_connection(omega_b, S)  # Omega'_mu
    gup_b = curved_gammas(e_boosted, gamma)  # gamma'^mu
    count_b = sum(1 for mu in range(8) for a in range(8) for c in range(a + 1, 8)
                  if omega_b[mu][a][c] != 0)
    say(f"nonzero components omega'_mu ab with a < b: {count_b}")
    '''),
    md(r"""
    ## 9. The contraction in the boosted vielbein

    The next cell computes $\gamma'^\mu\Omega'_\mu$ (summed over $\mu$) and compares it,
    exactly, for symbolic $a_4$, $b_4$, $H$, $\beta$ and $b_0$, with

    $$\gamma'^\mu\Omega'_\mu = \frac{6H - \beta}{2}\,v + \frac34\,\frac{b_4'}{b_4}\,
    w, \qquad v = \cosh b\,\gamma^{(x0)} - \sinh b\,\gamma^{(x4)},\quad
    w = \cosh b\,\gamma^{(x4)} - \sinh b\,\gamma^{(x0)} .$$

    At $b_4 = 1$ the second term is absent, and the formula is the record's. At $b = 0$
    (no boost) it gives back $3H\gamma^{(x0)} + \frac34(b_4'/b_4)\gamma^{(x4)}$. The
    coefficient $(6H - \beta)/2$ already shows the surprise: for the rate
    $\beta = 6H$ the first term is zero.
    """),
    code(r'''
    slash_b = sum((gup_b[mu] * Omega_b[mu] for mu in range(8)), Z16)
    v = sp.cosh(b) * gamma[0] - sp.sinh(b) * gamma[4]  # R gamma^(x0) R^-1 (Section 11)
    w = sp.cosh(b) * gamma[4] - sp.sinh(b) * gamma[0]  # R gamma^(x4) R^-1
    formula = (6 * H - beta) / 2 * v + c_b4 * w
    check(matrix_is_zero(slash_b - formula),
          "gamma'^mu Omega'_mu = ((6H - beta)/2) v + (3/4)(b4'/b4) w",
          record=f"{SCOPE_PY}, check boosted_frame_gammaOmega_formula (b4 = 1)")
    check(matrix_is_zero(formula.subs({beta: 0, b0: 0}) - 3 * H * gamma[0]
                         - c_b4 * gamma[4])
          and matrix_is_zero(at_b4_1(formula) - (6 * H - beta) / 2 * v),
          "with no boost the formula is 3 H gamma^(x0) + (3/4)(b4'/b4) gamma^(x4); at "
          "b4 = 1 it is ((6H - beta)/2) v")
    '''),
    md(r"""
    The next cell draws the two coefficients of the formula at $b_4 = 1$ (the
    background of this book), the coefficient of $\gamma^{(x0)}$,
    $\frac{6H-\beta}{2}\cosh b$, and the coefficient of $\gamma^{(x4)}$,
    $-\frac{6H-\beta}{2}\sinh b$, as functions of the time $x_4$, for $b_0 = 0$,
    $H = 1$ and the four rates $\beta = 0, 3, 6, 9$. The curves are made from the
    formula that the previous cell proved. For $\beta = 0$ they are the constants $3$
    and $0$ of the diagonal vielbein; for $\beta = 6$ both are zero at every time; for
    $\beta = 9$ they change sign.
    """),
    code(r'''
    times = np.linspace(-0.25, 0.25, 101)
    t_symbol = sp.Symbol("t", real=True)
    coefficient_x0 = (6 * H - beta) / 2 * sp.cosh(b)  # the coefficient of gamma^(x0)
    coefficient_x4 = -(6 * H - beta) / 2 * sp.sinh(b)  # the coefficient of gamma^(x4)
    fig, (ax_left, ax_right) = plt.subplots(1, 2, figsize=(10.0, 4.2), sharey=True)
    for rate, style in ((0, "-"), (3, "--"), (6, "-."), (9, ":")):
        values = {H: 1, beta: rate, b0: 0, x4: t_symbol}
        c0 = sp.lambdify(t_symbol, coefficient_x0.subs(values))
        c4 = sp.lambdify(t_symbol, coefficient_x4.subs(values))
        ax_left.plot(times, np.broadcast_to(c0(times), times.shape), style,
                     label=f"$\\beta = {rate}H$" if rate else "no boost")
        ax_right.plot(times, np.broadcast_to(c4(times), times.shape), style,
                      label=f"$\\beta = {rate}H$" if rate else "no boost")
    ax_left.set_title("coefficient of $\\gamma^{(x0)}$")
    ax_right.set_title("coefficient of $\\gamma^{(x4)}$")
    for ax in (ax_left, ax_right):
        ax.set_xlabel("time $x_4$ (units $1/H$), with $b = \\beta x_4$")
        ax.legend(fontsize=8)
    ax_left.set_ylabel("coefficient in $\\gamma'^\\mu\\Omega'_\\mu$ (units of $H$)")
    save_figure(fig, "boosted_contraction",
                "The contraction $\\gamma'^\\mu\\Omega'_\\mu$ in the boosted vielbein with "
                "rapidity $b = \\beta x_4$, $H = 1$ and $b_4 = 1$: the coefficient of "
                "$\\gamma^{(x0)}$ (left) and of $\\gamma^{(x4)}$ (right) versus the time "
                "$x_4$ in units $1/H$, for the rates $\\beta = 0, 3H, 6H, 9H$. For "
                "$\\beta = 0$ (no boost) the coefficients are $3$ and $0$, the diagonal "
                "value $3H\\gamma^{(x0)}$ (on the right the zero lines of $\\beta = 0$ "
                "and $\\beta = 6H$ lie on top of each other); for $\\beta = 6H$ both "
                "coefficients vanish at every time; "
                "the same metric, a different frame, a different value. A changing "
                "$b_4$ would add $\\frac34(b_4'/b_4)(\\cosh b\\,\\gamma^{(x4)} - "
                "\\sinh b\\,\\gamma^{(x0)})$.")
    '''),
    md(r"""
    ## 10. The rate $\beta = 6H$: the contraction vanishes for constant $b_4$

    The next cell puts $\beta = 6H$ into the boosted spin connection (substituting
    after the computation is allowed, because the computation was done for every
    $\beta$). It checks that $\gamma'^\mu\Omega'_\mu = \frac34(b_4'/b_4)\,w$ is all that
    remains, so that the contraction is zero identically, for every $H > 0$ and every
    $a_4$, exactly when $b_4$ is constant (the record's statement at $b_4 = 1$); and
    that $\Omega'_\mu$ is nonzero for $\mu = x1, \dots, x7$ and zero only for
    $\mu = x0$. So for a constant $b_4$ the field equation $\gamma'^\mu D'_\mu\Psi' =
    (m + U')\Psi'$ in this vielbein has no term $\gamma'^\mu\Omega'_\mu\Psi'$ at all,
    although the spinor connection is everywhere. (The matrices $v$ and $w$ are
    independent, so no rate $\beta$ removes the term $\frac34(b_4'/b_4)w$ of a changing
    $b_4$; the rescaling of Section 14 removes the whole term.)
    """),
    code(r'''
    six_H = {beta: 6 * H}
    slash_6H = slash_b.subs(six_H)
    Omega_6H = [M.subs(six_H) for M in Omega_b]
    nonzero = [NAMES[mu] for mu in range(8) if not matrix_is_zero(Omega_6H[mu])]
    say(f"Omega'_mu is nonzero for mu = {nonzero}")
    check(matrix_is_zero(slash_6H - c_b4 * w.subs(six_H))
          and matrix_is_zero(at_b4_1(slash_6H))
          and nonzero == NAMES[1:],
          "beta = 6H: gamma'^mu Omega'_mu = (3/4)(b4'/b4) w (zero for constant b4), "
          "Omega'_mu nonzero for x1 ... x7",
          record=f"{SCOPE_PY}, check boosted_frame_gammaOmega_vanishes (b4 = 1)")
    '''),
    md(r"""
    The next cell draws three 16 x 16 matrices of the boosted vielbein with
    $\beta = 6H$ at the sample point $H = 1$, $b_0 = 0$, $x_4 = 1/6$ (so $b = 1$),
    $z = \pi/4$, $a_4 = 1/2$, $a_4' = 1/2$ on the background $b_4 = 1$: the spinor
    connection $\Omega'_{x4}$ (in the diagonal vielbein $\Omega_{x4} = 0$; here it is
    not, because the frame turns with time), $\Omega'_{x1}$, and the total contraction
    $\gamma'^\mu\Omega'_\mu$, which is the zero matrix (white).
    """),
    code(r'''
    def at_sample(expr):
        """The decimal value of expr at H = 1, b0 = 0, x4 = 1/6, z = pi/4, a4 = 1/2,
        a4' = 1/2, a4'' = 0, b4 = 1 (derivatives replaced first, then a4 and b4, then
        x4)."""
        expr = at_b4_1(expr).subs(sp.Derivative(a4, (x4, 2)), 0)
        expr = expr.subs(sp.Derivative(a4, x4), sp.Rational(1, 2))
        expr = expr.subs(a4, sp.Rational(1, 2))
        expr = expr.subs({H: 1, b0: 0, x4: sp.Rational(1, 6), x0: sp.pi / 24})
        return float(sp.N(expr))


    def sample_table(matrix):
        return np.array([[at_sample(v) for v in row] for row in matrix.tolist()])


    panels = [("$\\Omega'_{x4}$", Omega_6H[4]), ("$\\Omega'_{x1}$", Omega_6H[1]),
              ("$\\gamma'^\\mu\\Omega'_\\mu$ (all zero)", slash_6H)]
    tables = [sample_table(M) for _, M in panels]
    fig, axes = plt.subplots(1, 3, figsize=(11.0, 3.6))
    for ax, (title, _), table in zip(axes, panels, tables):
        limit = max(np.abs(table).max(), 1.0)  # each panel its own colour scale
        image = ax.imshow(table, cmap="RdBu_r", vmin=-limit, vmax=limit)
        ax.set_title(title)
        ax.set_xticks([])
        ax.set_yticks([])
        ax.grid(False)
        fig.colorbar(image, ax=ax, shrink=0.8)
    save_figure(fig, "boosted_connection_heat_maps",
                "The boosted vielbein with the rate $\\beta = 6H$ at the sample point "
                "$H = 1$, $b_0 = 0$, $x_4 = 1/6$ (rapidity $b = 1$), $z = \\pi/4$, $a_4 = "
                "1/2$, $a_4' = 1/2$, $b_4 = 1$, as 16 x 16 heat maps (red positive, blue "
                "negative, white zero; rows and columns are the spinor components; each "
                "panel has its own colour scale). Left: "
                "$\\Omega'_{x4}$, nonzero because the frame turns with time; middle: "
                "$\\Omega'_{x1}$; right: the contraction $\\gamma'^\\mu\\Omega'_\\mu$, the "
                "zero matrix. The spinor connection is present, its contraction is not.")
    check(np.abs(tables[2]).max() < 1e-12 and np.abs(tables[0]).max() > 0.1,
          "at the sample point Omega'_x4 is nonzero and the contraction is zero")
    '''),
    md(r"""
    ## 11. Why: the local spin covariance, with an explicit spinor boost

    The next cell takes the 16 x 16 matrix $X = \gamma^{(x4)}\gamma^{(x0)}$. Since
    $X^2 = -\gamma^{(x4)}\gamma^{(x4)}\gamma^{(x0)}\gamma^{(x0)} = -(-1)(+1) = 1$,
    the spinor boost $R = \cosh\frac b2 - \sinh\frac b2\,X$ has the inverse
    $R^{-1} = \cosh\frac b2 + \sinh\frac b2\,X$ (multiply them: $\cosh^2 -
    \sinh^2 X^2 = 1$). The cell checks, exactly:

    1. $R^{-1}\gamma^a R = \sum_c\Lambda^a{}_c\gamma^c$ for all eight $a$: $R$
       covers the boost $\Lambda(b)$;
    2. $\gamma'^\mu = R\,\gamma^\mu R^{-1}$ and $\Omega'_\mu = R\,\Omega_\mu R^{-1} -
       (\partial_\mu R)R^{-1}$ for all eight $\mu$ (the covariance theorem);
    3. the two pieces of the formula of Section 9: $R\,\gamma^{(x0)}R^{-1} = v$ and
       $R\,\gamma^{(x4)}R^{-1} = w$, so that the turned contraction is
       $R(3H\gamma^{(x0)} + \frac34\frac{b_4'}{b_4}\gamma^{(x4)})R^{-1} = 3Hv +
       \frac34\frac{b_4'}{b_4}w$, and the extra term $\sum_\mu\gamma'^\mu(\partial_\mu
       R)R^{-1} = \frac{\beta}{2}\,v$ (only $\mu = x4$ contributes, because $R$ depends
       on $x_4$ only). Their difference is the formula of Section 9.
    """),
    code(r'''
    X = gamma[4] * gamma[0]  # gamma^(x4) gamma^(x0)
    check(X * X == I16, "X = gamma^(x4) gamma^(x0) squares to the identity")
    R = sp.cosh(b / 2) * I16 - sp.sinh(b / 2) * X  # the spinor boost
    R_inv = sp.cosh(b / 2) * I16 + sp.sinh(b / 2) * X
    check(matrix_is_zero(R * R_inv - I16), "R R^-1 = 1")
    covers = all(matrix_is_zero(R_inv * gamma[a] * R
                                - sum((L[a, c] * gamma[c] for c in range(8)), Z16))
                 for a in range(8))
    check(covers, "R^-1 gamma^a R = Lambda^a_c gamma^c: R covers the boost")
    gammas_turn = all(matrix_is_zero(gup_b[mu] - R * gup[mu] * R_inv) for mu in range(8))
    connection_rule = all(matrix_is_zero(Omega_b[mu] - (R * Omega[mu] * R_inv
                                                       - R.diff(x[mu]) * R_inv))
                          for mu in range(8))
    check(gammas_turn and connection_rule,
          "gamma'^mu = R gamma^mu R^-1 and Omega'_mu = R Omega_mu R^-1 - (d_mu R) R^-1")
    turned = R * slash * R_inv
    extra = sum((gup_b[mu] * R.diff(x[mu]) * R_inv for mu in range(8)), Z16)
    check(matrix_is_zero(R * gamma[0] * R_inv - v)
          and matrix_is_zero(R * gamma[4] * R_inv - w)
          and matrix_is_zero(turned - 3 * H * v - c_b4 * w)
          and matrix_is_zero(extra - beta / 2 * v),
          "R g0 R^-1 = v, R g4 R^-1 = w; turned term 3H v + (3/4)(b4'/b4) w; extra term "
          "(beta/2) v")
    '''),
    md(r"""
    ## 12. The curvature: the Riemann and Ricci tensors

    The next cell computes the Riemann tensor of the author's metric from the
    Christoffel symbols with the convention $R^\rho{}_{\sigma\mu\nu} =
    \partial_\mu\Gamma^\rho{}_{\nu\sigma} - \partial_\nu\Gamma^\rho{}_{\mu\sigma} +
    \sum_\lambda(\Gamma^\rho{}_{\mu\lambda}\Gamma^\lambda{}_{\nu\sigma} -
    \Gamma^\rho{}_{\nu\lambda}\Gamma^\lambda{}_{\mu\sigma})$ (it keeps the components
    with $\mu < \nu$; the others follow from the antisymmetry in $\mu, \nu$), then the
    mixed Ricci components $R^\mu{}_\nu$ and the Ricci scalar. It compares them with
    the record of the metric with $b_4$ (`ricciMixed` and `ricciScalar` of
    `Revision/metric_b4/results/metric-b4.json`, which also lists the two components
    off the diagonal, $R^{x4}{}_{x0}$ and $R^{x0}{}_{x4}$, proportional to $b_4'$) and,
    at $b_4 = 1$, with the record `field-theory.json` (`ricci_mixed_diagonal`,
    `ricci_scalar`), whose values are

    $$R^{x0}{}_{x0} = -6H^2,\quad R^{x1}{}_{x1} = R^{x2}{}_{x2} = R^{x3}{}_{x3} =
    a_4'' - 6H^2,\quad R^{x4}{}_{x4} = 6a_4'^2,\quad R^{x5}{}_{x5} = R^{x6}{}_{x6} =
    R^{x7}{}_{x7} = -a_4'' - 6H^2,$$

    and $R = 6(a_4'^2 - 7H^2)$. The component $R^{x0}{}_{x0} = -6H^2$ holds for every
    $b_4$ and is negative for every $H > 0$ and every $a_4$: the metric is never flat.
    At $b_4 = 1$ the component $R^{x4}{}_{x4} = 6a_4'^2$ shows that the deflation makes
    curvature, although $\gamma^\mu\Omega_\mu$ does not contain $a_4$ at all.
    """),
    code(r'''
    def riemann_component(r, sg, mu, nu):
        value = sp.diff(Gam[r][nu][sg], x[mu]) - sp.diff(Gam[r][mu][sg], x[nu])
        for lam in range(8):
            value += Gam[r][mu][lam] * Gam[lam][nu][sg] - Gam[r][nu][lam] * Gam[lam][mu][sg]
        return value


    def is_nonzero(expr):
        """True when expr is not identically zero.  A value clearly different from zero
        at the sample point proves it (fast); otherwise the exact test decides."""
        if abs(at_sample(expr)) > 1e-9:
            return True
        return not is_zero(expr)


    riemann = {}  # (r, sigma, mu, nu) -> R^r_sigma mu nu, only the nonzero ones
    for r in range(8):
        for sg in range(8):
            for mu in range(8):
                for nu in range(mu + 1, 8):
                    value = riemann_component(r, sg, mu, nu)
                    if value != 0 and is_nonzero(value):
                        riemann[(r, sg, mu, nu)] = value
                        riemann[(r, sg, nu, mu)] = -value
    report("nonzero components R^r_sigma mu nu with mu < nu", len(riemann) // 2)
    ricci_lower = sp.Matrix(8, 8, lambda sg, nu: sum(
        riemann.get((r, sg, r, nu), 0) for r in range(8)))  # R_sigma nu
    ricci_mixed = g.inv() * ricci_lower  # R^mu_nu = g^mu sigma R_sigma nu
    names = {"H": H, "x0": x0, "x4": x4, "a4": a4, "b4": b4, "a4p": a4p, "b4p": b4p,
             "a4pp": sp.Derivative(a4, (x4, 2)), "b4pp": sp.Derivative(b4, (x4, 2))}


    def wolfram_to_sympy(text):
        """A text of a record in Wolfram notation as a sympy expression."""
        for long_form, short_form in (("Derivative[1][a4][x4]", "a4p"),
                                      ("Derivative[2][a4][x4]", "a4pp"),
                                      ("Derivative[1][b4][x4]", "b4p"),
                                      ("Derivative[2][b4][x4]", "b4pp"),
                                      ("a4[x4]", "a4"), ("b4[x4]", "b4")):
            text = text.replace(long_form, short_form)
        return parse_mathematica(text).subs(
            {sp.Symbol(k): value for k, value in names.items()}, simultaneous=True)


    metric_b4 = json.loads(repository_file(METRIC_B4_FILE).read_text(encoding="utf-8"))
    ricci_b4 = {tuple(NAMES.index(n) for n in key.split(",")): wolfram_to_sympy(text)
                for key, text in metric_b4["ricciMixed"].items()}
    nonzero_mixed = {(m, n) for m in range(8) for n in range(8)
                     if not is_zero(ricci_mixed[m, n])}
    check(nonzero_mixed == set(ricci_b4)
          and all(is_zero(ricci_mixed[k] - ricci_b4[k]) for k in ricci_b4)
          and is_zero(sum(ricci_mixed[a, a] for a in range(8))
                      - wolfram_to_sympy(metric_b4["ricciScalar"])),
          "the mixed Ricci tensor (10 nonzero components, 2 off the diagonal) and R equal "
          "the record with b4",
          record=f"{METRIC_B4_FILE}, keys ricciMixed and ricciScalar")
    for key in sorted(ricci_b4):
        say(f"R^{NAMES[key[0]]}_{NAMES[key[1]]} = {ricci_b4[key]}")
    FORMULAS = {item["key"]: item["wl"] for item in json.loads(
        repository_file(THEORY_FILE).read_text(encoding="utf-8"))["formulas"]}
    ricci_record = wolfram_to_sympy(FORMULAS["ricci_mixed_diagonal"])
    ricci_scalar = sum(ricci_mixed[a, a] for a in range(8))
    check(all(is_zero(at_b4_1(ricci_mixed[a, a]) - ricci_record[a]) for a in range(8))
          and is_zero(at_b4_1(ricci_scalar) - wolfram_to_sympy(FORMULAS["ricci_scalar"])),
          "at b4 = 1: the eight Ricci components and R = 6 (a4'^2 - 7 H^2) equal the record",
          record=f"{THEORY_FILE}, formulas ricci_mixed_diagonal and ricci_scalar")
    # multiplied out, the entries of gamma^mu Omega_mu contain neither a4 nor its derivatives
    a4_free = all(not sp.expand(entry).has(a4) for entry in slash)
    check(a4_free and is_zero(ricci_mixed[0, 0] + 6 * H**2)
          and is_zero(at_b4_1(ricci_mixed[4, 4]) - 6 * a4p ** 2),
          "gamma^mu Omega_mu contains no a4, but R^x4_x4 = 6 a4'^2 at b4 = 1; "
          "R^x0_x0 = -6 H^2 for every b4",
          record=f"{SCOPE_PY}, check gammaOmega_blind_to_the_deflation (b4 = 1)")
    '''),
    md(r"""
    The next cell draws the Ricci components on the background $b_4 = 1$. On the
    left, the eight values $R^\mu{}_\mu$ at the sample values $H = 1$, $a_4' = 1/2$,
    $a_4'' = 0$ (in units of $H^2$). On the right, three of them as functions of the
    rate $a_4'$ (with $a_4'' = 0$): the hidden component $-6H^2$ does not depend on the
    history, the time component $6a_4'^2$ is made entirely by the expansion and
    deflation, and the 3-space component $a_4'' - 6H^2$ stays $-6H^2$ for a steady
    rate ($a_4'' = 0$).
    """),
    code(r'''
    rate_symbol, accel_symbol = sp.symbols("rate accel", real=True)
    numeric = [sp.lambdify((rate_symbol, accel_symbol), ricci_record[a].subs(
        {H: 1, sp.Derivative(a4, (x4, 2)): accel_symbol,
         sp.Derivative(a4, x4): rate_symbol})) for a in range(8)]
    fig, (ax_left, ax_right) = plt.subplots(1, 2, figsize=(10.0, 4.2))
    values = [float(numeric[a](0.5, 0.0)) for a in range(8)]
    colors = ["black"] + ["tab:red"] * 3 + ["gray"] + ["tab:blue"] * 3
    ax_left.bar(range(8), values, color=colors, width=0.6)
    ax_left.axhline(0.0, color="black", linewidth=0.8)
    ax_left.set_xticks(range(8), [f"$R^{{{n}}}{{}}_{{{n}}}$" for n in NAMES], fontsize=8)
    ax_left.set_ylabel("value (units of $H^2$)")
    ax_left.set_title("Ricci components at $a_4' = 1/2$, $a_4'' = 0$, $b_4 = 1$")
    rates = np.linspace(-3.0, 3.0, 121)
    for a, label, style in ((0, "$R^{x0}{}_{x0} = -6H^2$", "-"),
                            (4, "$R^{x4}{}_{x4} = 6a_4'^2$", "--"),
                            (1, "$R^{x1}{}_{x1} = a_4'' - 6H^2$", ":")):
        ax_right.plot(rates, np.broadcast_to(numeric[a](rates, 0.0), rates.shape),
                      style, label=label)
    ax_right.axhline(0.0, color="black", linewidth=0.8)
    ax_right.set_xlabel("rate $a_4'$ (units of $H$), with $a_4'' = 0$, $b_4 = 1$")
    ax_right.set_ylabel("value (units of $H^2$)")
    ax_right.set_title("Never flat: $R^{x0}{}_{x0} = -6H^2$")
    ax_right.legend(fontsize=8)
    save_figure(fig, "ricci_components",
                "The mixed Ricci components $R^\\mu{}_\\mu$ of the author's metric on the "
                "background $b_4 = 1$, in units of $H^2$. Left: all eight at $H = 1$, "
                "$a_4' = 1/2$, $a_4^{\\prime\\prime} = 0$ (black: hidden direction, red: "
                "3-space, gray: time, blue: extra times). Right: $R^{x0}{}_{x0} = -6H^2$ "
                "(solid), $R^{x4}{}_{x4} = 6a_4'^2$ (dashed) and $R^{x1}{}_{x1} = "
                "a_4^{\\prime\\prime} - 6H^2$ (dotted) versus the rate $a_4'$ in units of "
                "$H$ with $a_4^{\\prime\\prime} = 0$. The hidden component "
                "is negative for every history (and every $b_4$), so the metric is never "
                "flat, and the time component is curvature made by the expansion and "
                "deflation (the dotted line lies on the solid one because "
                "$a_4^{\\prime\\prime} = 0$).")
    '''),
    md(r"""
    ## 13. The curvature of the spinor connection

    The next cell computes, in the diagonal vielbein, the 28 matrices $F_{\mu\nu}$
    ($\mu < \nu$) and checks the theorem $F_{\mu\nu} = \frac12\sum_{a,b}
    R_{ab\mu\nu}S^{ab}$, where $R_{ab\mu\nu} = \eta_{aa}\,f_a\,R^a{}_{b\mu\nu}/f_b$
    is the Riemann tensor with two frame indices (for the diagonal vielbein), for every
    $b_4$. Then it computes $F'_{x0\,x1}$ in the boosted vielbein with $\beta = 6H$
    (where the contraction vanished for a constant $b_4$) and checks that it is
    $R\,F_{x0\,x1}R^{-1}$ and is not zero: the spinor connection is still there and
    curved.
    """),
    code(r'''
    def spinor_curvature(Om, mu, nu):
        return (Om[nu].diff(x[mu]) - Om[mu].diff(x[nu])
                + Om[mu] * Om[nu] - Om[nu] * Om[mu])


    F = {}
    theorem_ok = True
    for mu in range(8):
        for nu in range(mu + 1, 8):
            F[(mu, nu)] = spinor_curvature(Omega, mu, nu)
            from_riemann = sum((ETA[a] * f[a] * riemann[(a, c, mu, nu)] / f[c] * S[a][c] / 2
                                for a in range(8) for c in range(8)
                                if (a, c, mu, nu) in riemann), Z16)
            theorem_ok = theorem_ok and matrix_is_zero(F[(mu, nu)] - from_riemann)
    check(theorem_ok and record_passed(REPORT_WL_B4, "spin_curvature_equals_Riemann"),
          "F_mu nu = (1/2) R_ab mu nu S^ab in all 28 coordinate planes",
          record=f"{REPORT_WL_B4}, check spin_curvature_equals_Riemann")
    F01_boosted = spinor_curvature(Omega_6H, 0, 1)
    R_6H, R_inv_6H = R.subs(six_H), R_inv.subs(six_H)
    check(matrix_is_zero(F01_boosted - R_6H * F[(0, 1)] * R_inv_6H)
          and np.abs(sample_table(F01_boosted)).max() > 0.1,
          "boosted (beta = 6H): F'_x0x1 = R F_x0x1 R^-1, nonzero",
          record=f"{SCOPE_PY}, check boosted_frame_curvature_nonzero (b4 = 1)")
    '''),
    md(r"""
    The next cell draws the size of the spinor curvature in each coordinate plane: for
    every pair $(\mu, \nu)$ the number $\|F_{\mu\nu}\| = \sqrt{\sum_{i,j}
    (F_{\mu\nu})_{ij}^2}$ (the square root of the sum of the squares of the 256
    entries) at the sample point $H = 1$, $z = \pi/4$, $a_4 = 1/2$, $a_4' = 1/2$,
    $a_4^{\prime\prime} = 0$, $b_4 = 1$ (diagonal vielbein). In another frame
    $F'_{\mu\nu} = R\,F_{\mu\nu}R^{-1}$ with an invertible matrix $R$, so a change of
    frame can change the sizes, but it can never turn a coloured square white or a
    white square coloured.
    """),
    code(r'''
    norms = np.zeros((8, 8))
    for (mu, nu), matrix in F.items():
        norms[mu, nu] = norms[nu, mu] = np.sqrt((sample_table(matrix) ** 2).sum())
    fig, ax = plt.subplots(figsize=(6.4, 5.4))
    image = ax.imshow(norms, cmap="Purples")
    for mu in range(8):
        for nu in range(8):
            if norms[mu, nu] > 0:
                # white digits on the dark squares (the largest sizes), black elsewhere
                dark = norms[mu, nu] > 0.6 * norms.max()
                ax.text(nu, mu, f"{norms[mu, nu]:.1f}", ha="center", va="center",
                        fontsize=7, color="white" if dark else "black")
    ax.set_xticks(range(8), NAMES)
    ax.set_yticks(range(8), NAMES)
    ax.set_xlabel("coordinate $\\nu$")
    ax.set_ylabel("coordinate $\\mu$")
    ax.set_title("Size of the spinor curvature $\\|F_{\\mu\\nu}\\|$")
    ax.grid(False)
    fig.colorbar(image, ax=ax, shrink=0.8, label="$\\|F_{\\mu\\nu}\\|$ (units of $H^2$)")
    save_figure(fig, "spinor_curvature_norms",
                "The size $\\|F_{\\mu\\nu}\\|$, the square root of the sum of the squares "
                "of the 256 entries of the spinor curvature, for every pair of "
                "coordinates $(\\mu, \\nu)$ in the diagonal vielbein at the sample point "
                "$H = 1$, $z = \\pi/4$, $a_4 = 1/2$, $a_4' = 1/2$, "
                "$a_4^{\\prime\\prime} = 0$, $b_4 = 1$, in units "
                "of $H^2$ (darker is larger, white is zero). All 28 coordinate planes "
                "except the plane of the hidden direction $x0$ and the time $x4$ are "
                "curved at this point, and $F_{x0\\,x4} = 0$ exactly; $F_{\\mu\\nu} = "
                "\\frac12 R_{ab\\mu\\nu}S^{ab}$ is the Riemann curvature, which no "
                "change of frame removes.")
    report("largest |F_mu nu| at the sample point (units of H^2)", f"{norms.max():.3f}")
    curved = [pair for pair in F if norms[pair] > 1e-9]  # the curved planes
    check(matrix_is_zero(F[(0, 4)]) and len(curved) == 27,
          "F_x0x4 = 0 exactly (every b4); the other 27 planes are curved at the sample "
          "point")
    '''),
    md(r"""
    ## 14. The rescaling $\Psi = \sin^{-1/2}(z)\,b_4^{-3/4}\,\chi$ removes the term

    A frame change is one way to remove $\gamma^\mu\Omega_\mu$; a change of the field
    variable is another. Write $\Psi = w_r\,\chi$ with $w_r = \sin^{-1/2}(z)\,
    b_4^{-3/4}$. Then $\gamma^\mu D_\mu\Psi = w_r\,\gamma^\mu\partial_\mu\chi +
    \big(\gamma^\mu\partial_\mu w_r + w_r\,\gamma^\mu\Omega_\mu\big)\chi$. The weight
    depends on $x_0$ and $x_4$, with $\gamma^{x0} = \tan z\,\gamma^{(x0)}$ and
    $\gamma^{x4} = \gamma^{(x4)}$, so the bracket is $\big(\tan z\,\partial_{x0}w_r +
    3Hw_r\big)\gamma^{(x0)} + \big(\partial_{x4}w_r + \frac34\frac{b_4'}{b_4}w_r\big)
    \gamma^{(x4)}$. Now $\partial_{x0}\sin^{-1/2}z = -\frac12\sin^{-3/2}z\cdot 6H\cos z$
    gives $\tan z\,\partial_{x0}w_r = -3Hw_r$, and $\partial_{x4}b_4^{-3/4} =
    -\frac34 b_4^{-7/4}b_4'$ gives $\partial_{x4}w_r = -\frac34\frac{b_4'}{b_4}w_r$:
    the bracket is zero. At $b_4 = 1$ the weight is the record's $\sin^{-1/2}z$. The
    next cell checks this as a matrix identity and, for safety, on 16 completely
    general functions $\chi_1, \dots, \chi_{16}$ of all eight coordinates. It also
    checks the record's remark about the potential $U = \frac{\lambda}{2}S^2$: since
    $w_r$ is real, $S[\Psi] = \Psi^\dagger C\Psi = w_r^2\,S[\chi] =
    S[\chi]/(b_4^{3/2}\sin z)$, so the rescaled equation is $\gamma^\mu
    \partial_\mu\chi = \big(m + \lambda S[\chi]/(b_4^{3/2}\sin z)\big)\,\chi$: for
    $U = 0$ the term is removed completely; for $U \ne 0$ it becomes a coupling that
    depends on $x_0$ (and on $x_4$ through $b_4$).
    """),
    code(r'''
    w_r = sp.sin(z) ** sp.Rational(-1, 2) * b4 ** sp.Rational(-3, 4)  # the weight
    bracket = sum((gup[mu] * sp.diff(w_r, x[mu]) for mu in range(8)), Z16) + w_r * slash
    chi = sp.Matrix([sp.Function(f"chi{A}")(*x) for A in range(1, 17)])
    psi = w_r * chi
    dirac_psi = sum((gup[mu] * (psi.diff(x[mu]) + Omega[mu] * psi) for mu in range(8)),
                    sp.zeros(16, 1))
    dirac_chi = sum((gup[mu] * chi.diff(x[mu]) for mu in range(8)), sp.zeros(16, 1))
    check(matrix_is_zero(bracket) and all(is_zero(v) for v in dirac_psi - w_r * dirac_chi),
          "gamma^mu D_mu (w chi) = w gamma^mu d_mu chi for w = sin^(-1/2) z b4^(-3/4)",
          record=f"{SCOPE_PY}, check rescaling_removes_the_connection_term (b4 = 1)")
    chi_conj = sp.Matrix([sp.conjugate(v) for v in chi])  # complex conjugates
    S_psi = (w_r * chi_conj).T * C * (w_r * chi)  # Psi^dagger C Psi (w is real)
    S_chi = chi_conj.T * C * chi
    check(is_zero(S_psi[0, 0] - S_chi[0, 0] / (b4 ** sp.Rational(3, 2) * sp.sin(z))),
          "S[w chi] = S[chi] / (b4^(3/2) sin z), S[chi] / sin z at b4 = 1",
          record=f"{SCOPE_PY}, check rescaled_equation_quadratic_potential (b4 = 1)")
    '''),
    md(r"""
    The next cell draws the rescaling for $H = 1$ on the background $b_4 = 1$, where
    $w_r = \sin^{-1/2}z$: on the left the weight (large near the tip $z \to 0$, equal
    to 1 at $z = \pi/2$); on the right the two terms of the coefficient of
    $\gamma^{(x0)}$, $\tan z\,\partial_{x0}w_r$ and $3Hw_r$, computed from their sympy
    formulas, and their sum, which is zero at every $z$.
    """),
    code(r'''
    z_values = np.linspace(0.05, np.pi / 2 - 0.02, 300)
    x0_symbol = sp.Symbol("u", positive=True)
    w_1 = at_b4_1(w_r)  # the weight at b4 = 1: sin^(-1/2) z
    term_derivative = sp.lambdify(x0_symbol, (sp.tan(z) * sp.diff(w_1, x0)).subs(
        {H: 1}).subs(x0, x0_symbol))
    term_connection = sp.lambdify(x0_symbol, (3 * H * w_1).subs({H: 1}).subs(x0, x0_symbol))
    weight = sp.lambdify(x0_symbol, w_1.subs({H: 1}).subs(x0, x0_symbol))
    u_values = z_values / 6.0  # x0 = z / (6 H) with H = 1
    first, second = term_derivative(u_values), term_connection(u_values)
    fig, (ax_left, ax_right) = plt.subplots(1, 2, figsize=(10.0, 4.2))
    ax_left.plot(z_values, weight(u_values), label="$w_r = \\sin^{-1/2} z$ ($b_4 = 1$)")
    ax_left.set_xlabel("hidden angle $z = 6Hx_0$ (radians)")
    ax_left.set_ylabel("weight (pure number)")
    ax_left.set_title("The rescaling weight")
    ax_left.legend(fontsize=8)
    ax_right.plot(z_values, first, label="$\\tan z\\,\\partial_{x0} w_r$")
    ax_right.plot(z_values, second, "--",
                  label="$3H w_r$ (from $\\gamma^\\mu\\Omega_\\mu$)")
    ax_right.plot(z_values, first + second, ":", color="black", label="sum")
    ax_right.set_xlabel("hidden angle $z = 6Hx_0$ (radians)")
    ax_right.set_ylabel("coefficient of $\\gamma^{(x0)}\\chi$ (units of $H$)")
    ax_right.set_title("The two terms cancel")
    ax_right.legend(fontsize=8)
    save_figure(fig, "rescaling",
                "The rescaling $\\Psi = w_r\\chi$ with $w_r = \\sin^{-1/2}(z)\\,"
                "b_4^{-3/4}$, drawn for $H = 1$ on the background $b_4 = 1$. Left: the "
                "weight $w_r$ versus the hidden angle $z$ in radians. Right: the two "
                "terms of the coefficient of $\\gamma^{(x0)}\\chi$ in the field "
                "equation of $\\chi$, the derivative term $\\tan z\\,\\partial_{x0}w_r = "
                "-3Hw_r$ (solid) and the spin-connection term $3Hw_r$ (dashed), in units "
                "of $H$, and their sum (dotted), which is zero at every $z$: in the "
                "variable $\\chi$ the equation has no term $3H\\gamma^{(x0)}$ (and, by "
                "the factor $b_4^{-3/4}$, no term $\\frac34(b_4'/b_4)\\gamma^{(x4)}$).")
    check(np.max(np.abs(first + second)) < 1e-12, "the two terms cancel at all 300 points")
    '''),
    md(r"""
    ## 15. The last checks

    The last cell checks that every check of the Revision reports that states a result
    reproduced in this notebook is recorded there as passed (the sympy scope checker
    `python-scope.json`, the WolframScript scope checker `wolfram-scope.json`, which
    shares no code with it, and the curvature checks of the field-theory reports, with
    $b_4$ and at $b_4 = 1$), that all six figure files exist in the folder
    Revision/textbook/figures, and prints the number of checks that passed.
    """),
    code(r'''
    scope_names = ["boosted_frame_reproduces_metric", "boosted_frame_canonical_connection",
                   "boosted_frame_gammaOmega_formula", "boosted_frame_gammaOmega_vanishes",
                   "boosted_frame_curvature_nonzero",
                   "rescaling_removes_the_connection_term",
                   "rescaled_equation_quadratic_potential",
                   "gammaOmega_blind_to_the_deflation"]
    cited = {SCOPE_PY: scope_names, SCOPE_WL: scope_names,
             REPORT_PY: ["spinor_curvature_equals_riemann",
                         "curvature_nonzero_flat_only_formally"],
             REPORT_WL: ["ricci_scalar", "ricci_mixed_components",
                         "never_flat_for_H_positive", "spin_curvature_equals_Riemann"],
             REPORT_WL_B4: ["ricci_equals_metric_b4_set", "ricci_reduces_at_b4_1",
                            "spin_curvature_equals_Riemann"]}
    count = sum(len(v) for v in cited.values())
    check(all(record_passed(path, name) for path, names in cited.items()
              for name in names), f"the {count} cited record checks are recorded as passed")
    expected = [f"06b_{k}_{name}.png" for k, name in enumerate([
        "boost_hyperbolas", "boosted_contraction", "boosted_connection_heat_maps",
        "ricci_components", "spinor_curvature_norms", "rescaling"], 1)]
    check(all(output_file(f"{FIGURE_FOLDER}/{name}").is_file() for name in expected),
          "all six figure files exist")
    all_checks_passed()
    '''),
    md(r"""
    ## 16. What this notebook showed

    - A boost of the frame in the $(x4, x0)$ plane with rapidity $b = \beta x_4 + b_0$
      describes the same metric, and its canonical spin connection obeys the vielbein
      postulate. In it $\gamma'^\mu\Omega'_\mu = \frac{6H-\beta}{2}(\cosh b\,
      \gamma^{(x0)} - \sinh b\,\gamma^{(x4)}) + \frac34\frac{b_4'}{b_4}(\cosh b\,
      \gamma^{(x4)} - \sinh b\,\gamma^{(x0)})$ exactly (PROVED; at $b_4 = 1$ it
      reproduces the record). For $\beta = 6H$ and a constant $b_4$ the contraction
      vanishes identically, while $\Omega'_\mu$ is nonzero for $\mu = x1, \dots, x7$.
    - The reason is the local spin covariance: with the spinor boost
      $R = \cosh\frac b2 - \sinh\frac b2\,\gamma^{(x4)}\gamma^{(x0)}$, $\Omega'_\mu =
      R\Omega_\mu R^{-1} - (\partial_\mu R)R^{-1}$, and the second term contributes
      $-\frac{\beta}{2}(\cosh b\,\gamma^{(x0)} - \sinh b\,\gamma^{(x4)})$ (PROVED
      here).
    - So the value of $\gamma^\mu\Omega_\mu$ in the diagonal vielbein is
      FRAME-DEPENDENT. What is frame-independent: the metric is curved for every
      $H > 0$ and every $b_4$ ($R^{x0}{}_{x0} = -6H^2$, PROVED; reproduces the
      records), the spinor curvature is $F_{\mu\nu} = \frac12 R_{ab\mu\nu}S^{ab}$ in
      all 28 planes (PROVED; reproduces the record), and it is nonzero in every frame
      because $F' = RFR^{-1}$; therefore no frame makes $\Omega_\mu$ vanish.
    - The deflation makes curvature ($R^{x4}{}_{x4} = 6a_4'^2$ at $b_4 = 1$) that the
      contraction $\gamma^\mu\Omega_\mu$ does not see (PROVED; reproduces the record).
    - The rescaling $\Psi = \sin^{-1/2}(z)\,b_4^{-3/4}\,\chi$ removes the term
      $\gamma^\mu\Omega_\mu$ from the field equation exactly; with
      $U = \frac\lambda2 S^2$ it becomes the coupling
      $\lambda S[\chi]/(b_4^{3/2}\sin z)$ (PROVED; at $b_4 = 1$ it reproduces the
      record).
    - In short, the non-triviality of the field equations holds in the qualified sense
      of the record: the gravitational field enters through the vielbein factors of
      every derivative term and through a spin connection whose curvature cannot be
      removed, but the particular term $\gamma^\mu\Omega_\mu$ is a property of the
      chosen frame and field variables.
    """),
]

if __name__ == "__main__":
    raise SystemExit(run_builder(__file__))
