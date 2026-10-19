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

Physics source (the Revision record): the corrected metric of 2026-10-16 (version 2,
Revision/SPEC.md section 1); Revision/theory/reports/python-scope.json and
wolfram-scope.json (frame dependence, rescaling, the hidden block in the term),
Revision/theory/field-theory.json (the diagonal Ricci tensor), the field-theory reports
(spinor curvature, flat member), Revision/gkd_lovelock/results/curvature.json (the 112
nonzero components R^ab_cd and the Einstein tensor) with its sympy report, and
Revision/kohn_sham/results/parameters.json (the history).  The author's coordinates
x0..x7: x0 the hidden, space-like direction (z = 6 H x0 takes every real value), x1, x2,
x3 3-space (inflating), x4 the time, x5, x6, x7 the three extra times (deflating).
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
        "For the corrected metric of the author's primordial field with the functions "
        "a4(x4) and b4(x4) it boosts the diagonal vielbein in the (x4, x0) plane with a "
        "rapidity b(x4) that may be any function of the time and computes exactly, with "
        "sympy, the new spin connection and the new contraction gamma^mu Omega_mu = "
        "(c_g - b'/2)(cosh b gamma^(x0) - sinh b gamma^(x4)) + v_g (cosh b gamma^(x4) - "
        "sinh b gamma^(x0)), whose first term vanishes for the rapidity with b' = 2 c_g "
        "while the second remains for every rapidity; it verifies the local spin "
        "covariance of the connection with an explicit spinor boost, computes the "
        "Riemann tensor (only the 28 plane components are nonzero), the diagonal Ricci "
        "and Einstein tensors and the curvature of the spinor connection, which no "
        "frame can remove where the metric is curved, shows that the rescaling Psi = "
        "e^(a4/2) b4^(-1) (sin^2 z)^(-1/8) chi removes the whole term gamma^mu "
        "Omega_mu, checks every result against the Revision records and draws six "
        "teaching plots."
    ),
    "records": [
        ["Revision/algebra/gammas.json",
         "the author's eight real 16 x 16 gamma matrices and the matrix C (input)"],
        ["Revision/theory/field-theory.json",
         "the exact formulas for the corrected metric: the eight nonzero (diagonal) "
         "components of the mixed Ricci tensor and the Ricci scalar (reproduced)"],
        ["Revision/gkd_lovelock/results/curvature.json",
         "the 112 nonzero components R^ab_cd of the Riemann tensor and the 64 components "
         "of the mixed Einstein tensor of the corrected metric (reproduced)"],
        ["Revision/gkd_lovelock/results/python-lovelock-report.json",
         "the sympy checks of the curvature record: only plane components, agreement of "
         "the Riemann, Ricci and Einstein components"],
        ["Revision/kohn_sham/results/parameters.json",
         "the history of the Revision record: the slope A, the exponent beta of b4 and "
         "b4(0) (physics.historyA, physics.historyBeta, physics.historyB4AtZero)"],
        ["Revision/theory/reports/python-scope.json",
         "the sympy checks of the scope statements for the corrected metric: boosted "
         "frame, rescaling, the hidden block in the term (reproduced)"],
        ["Revision/theory/reports/wolfram-scope.json",
         "the WolframScript checks of the same scope statements (reproduced)"],
        ["Revision/theory/reports/python-field-theory.json",
         "the sympy checks of the curvature, of the flat member and of the spinor "
         "curvature"],
        ["Revision/theory/reports/wolfram-field-theory.json",
         "the WolframScript checks of the Ricci tensor, of the flat member and of the "
         "spinor curvature (reproduced)"],
    ],
    "packages": ["numpy", "sympy", "matplotlib"],
    "needs_rust": [],
    "expected_seconds": 360,
    "timeout_seconds": 900,
    "files_written": (
        ["Revision/textbook/figures/06b.captions.json"]
        + [f"Revision/textbook/figures/06b_{k}_{name}.png"
           for k, name in enumerate(FIGURES, 1)]
    ),
    "final_lines": [
        "PASS all six figure files exist",
        "ALL 29 CHECKS PASSED (notebook 06b)",
    ],
    "troubleshooting": [
        ["\"FileNotFoundError\" for Revision/algebra/gammas.json or for a report",
         "the notebook reads Revision records from the repository; open it inside the "
         "folder Revision/textbook/notebooks of a complete copy of the repository "
         "Dirac_claude (a single downloaded notebook file is not enough)."],
        ["a cell runs for several minutes",
         "the exact algebra of sympy with hyperbolic functions and three unknown "
         "functions is slow on old computers; the whole notebook needs about six "
         "minutes on a 2024 laptop, and up to about twelve minutes while other "
         "programs use the processor. Wait, or close the other programs."],
    ],
}

CELLS = [
    md(r"""
    ## 1. What this notebook computes

    The previous notebook of this chapter (06a) found, for the corrected metric of the
    author's primordial field in the DIAGONAL vielbein,
    $\gamma^\mu\Omega_\mu = c_g\gamma^{(x0)} + v_g\gamma^{(x4)}$ with
    $c_g = \frac32He^{a_4}b_4^{-1/2}$ and $v_g = b_4'/b_4 - a_4'/2$ (on the history of
    the Revision record $\frac32He^{Hx_4/3}\gamma^{(x0)} + \frac56H\gamma^{(x4)}$). A
    vielbein is a choice: at every point any other set of eight perpendicular unit
    directions describes the same metric. This notebook asks which results depend on
    that choice and which do not. It

    - builds a second vielbein of the same metric, the diagonal one **boosted** in the
      plane of the time $x4$ and the hidden direction $x0$ by a rapidity $b(x_4)$ that
      may be any function of the time;
    - computes its canonical spin connection and finds exactly
      $\gamma'^\mu\Omega'_\mu = (c_g - \frac{b'}{2})\big(\cosh b\,\gamma^{(x0)} -
      \sinh b\,\gamma^{(x4)}\big) + v_g\big(\cosh b\,\gamma^{(x4)} - \sinh b\,
      \gamma^{(x0)}\big)$: the first term VANISHES for the rapidity with $b' = 2c_g$,
      although $\Omega'_\mu$ itself does not vanish, while the second remains for every
      rapidity;
    - explains the formula with the **local spin covariance** of the connection,
      using the explicit spinor boost $R = \cosh\frac{b}{2} -
      \sinh\frac{b}{2}\,\gamma^{(x4)}\gamma^{(x0)}$;
    - computes the Riemann tensor, finds that only the 28 components that describe a
      coordinate plane are nonzero (112 entries $R^{ab}{}_{cd}$), so that the Ricci and
      Einstein tensors are diagonal, and computes the curvature $F_{\mu\nu}$ of the
      spinor connection, checks $F_{\mu\nu} = \frac12 R_{ab\mu\nu}S^{ab}$ in all 28
      coordinate planes, and shows that this curvature, which no choice of frame can
      remove, is nonzero on the history of the record and zero for the flat member
      $a_4 = 0$, $b_4 = H^2x_4^2$ of the family;
    - shows that the rescaled field $\chi = e^{-a_4/2}b_4(\sin^2 z)^{1/8}\,\Psi$ obeys
      an equation without the term $\gamma^\mu\Omega_\mu$;
    - checks every result against the Revision records and draws six teaching plots.
    """),
    md(r"""
    ## 3. The words used in this notebook

    - **Vielbein** $e^a{}_\mu$: eight perpendicular unit directions at every point
      (frame index $a$, coordinate index $\mu$), with $g_{\mu\nu} = \sum_a \eta_{aa}
      e^a{}_\mu e^a{}_\nu$; $\eta = \mathrm{diag}(+1,+1,+1,+1,-1,-1,-1,-1)$ in the
      order $x0, \dots, x7$. In Python lists the directions have the positions 0 to 7
      in the same order, so `x[0]` is $x0$ and `x[4]` is $x4$.
    - $z = 6Hx_0$, every real value; **warp factor** $W = (\sin^2 z)^{1/12}$; **hidden
      scale** $s_b = e^{-a_4}b_4^{1/2}$; **fold** $\cos z = 0$, where the two halves of
      a cell $0 < z < \pi$ meet; **degenerate points** $\sin z\cos z = 0$.
    - $c_g = \frac32He^{a_4}b_4^{-1/2}$ and $v_g = b_4'/b_4 - a_4'/2$: the coefficients
      of $\gamma^{(x0)}$ and $\gamma^{(x4)}$ in $\gamma^\mu\Omega_\mu$ in the diagonal
      vielbein (Notebook 06a).
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
      for a flat space. With the second index raised, $R^{ab}{}_{cd}$; for $\{c, d\} =
      \{a, b\}$ it describes the coordinate **plane** of $a$ and $b$, and
      $K(a, b) = R^{ab}{}_{ab}$ is called the curvature of that plane. **Ricci tensor**
      $R_{\sigma\nu} = \sum_\rho R^\rho{}_{\sigma\rho\nu}$, mixed form $R^\mu{}_\nu =
      \sum_\sigma g^{\mu\sigma}R_{\sigma\nu}$, **Ricci scalar** $R = \sum_\mu
      R^\mu{}_\mu$, **Einstein tensor** $G^\mu{}_\nu = R^\mu{}_\nu - \frac12
      \delta^\mu_\nu R$.
    - **Curvature of the spinor connection** $F_{\mu\nu} = \partial_\mu\Omega_\nu -
      \partial_\nu\Omega_\mu + [\Omega_\mu, \Omega_\nu]$: the 16 x 16 matrix with
      $D_\mu D_\nu\Psi - D_\nu D_\mu\Psi = F_{\mu\nu}\Psi$.
    - **Flat member**: the choice $a_4 = 0$, $b_4 = H^2x_4^2$ ($x_4 > 0$) of the two
      functions, for which the corrected metric is flat (8-dimensional flat space in
      unusual coordinates).
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

    The metric is the corrected metric of the author's primordial field (version 2 of
    2026-10-16), with $z = 6Hx_0$ (every real value), $H > 0$ and two arbitrary
    functions $a_4(x_4)$ and $b_4(x_4) > 0$:

    $$g = \mathrm{diag}\big(e^{-2a_4}b_4\cot^2 z,\ e^{2a_4}\ (\times 3),\ -1,\
    -e^{-2a_4}b_4W^2\ (\times 3)\big), \qquad W = (\sin^2 z)^{1/12}.$$

    The diagonal vielbein has the factors $f = (s_b\cot z,\ e^{a_4}\ (\times 3),\ 1,\
    s_bW\ (\times 3))$, $s_b = e^{-a_4}b_4^{1/2}$; as in Notebook 06a, the warp factor
    is a sympy function with the one rule $\partial_{x0}W = H\cot z\,W$, so that every
    result holds for every real $z$ away from the degenerate points. On the history of
    the Revision record, $a_4 = AHx_4$ and $b_4 = b_4(0)\,e^{\beta AHx_4}$ with $A = 1$,
    $\beta = 4/3$ and $b_4(0) = 1$ (a prescribed background), $c_g =
    \frac32He^{Hx_4/3}$ and $v_g = \frac56H$. The canonical spin connection of ANY
    vielbein $e$ is $\omega_\mu{}^a{}_b = \sum_\nu e^a{}_\nu (\partial_\mu e_b{}^\nu +
    \sum_\lambda\Gamma^\nu{}_{\mu\lambda}e_b{}^\lambda)$.

    **The theorem behind this notebook (local spin covariance).** If $e' = \Lambda e$
    and the spinor matrix $R(x)$ covers $\Lambda(x)$, then

    $$\Omega'_\mu = R\,\Omega_\mu R^{-1} - (\partial_\mu R)R^{-1}, \qquad
    \gamma'^\mu = R\,\gamma^\mu R^{-1}, \qquad F'_{\mu\nu} = R\,F_{\mu\nu}R^{-1}.$$

    Multiplying the first two and summing over $\mu$ gives

    $$\gamma'^\mu\Omega'_\mu = R\,(\gamma^\mu\Omega_\mu)\,R^{-1} -
    \sum_\mu\gamma'^\mu(\partial_\mu R)R^{-1}.$$

    The second term can cancel part of the first: the contraction
    $\gamma^\mu\Omega_\mu$ is frame-dependent. The curvature only gets turned by $R$,
    so if $F_{\mu\nu} \ne 0$ in one frame, it is nonzero in every frame: where the
    metric is curved, no frame removes the spinor connection itself.

    **Status.** Every statement checked below is PROVED exactly (sympy, symbolic $H$,
    $a_4$, $b_4$ and rapidity $b(x_4)$). The scope records (`python-scope.json`,
    `wolfram-scope.json`) state these results for the corrected metric; the notebook
    reproduces them. This is the record's own statement of the scope of the
    non-triviality: the value of $\gamma^\mu\Omega_\mu$ belongs to the diagonal
    vielbein and to the field variable; what is frame-independent is the curvature.
    """),
    md(r"""
    ## 5. The tools: sympy, the author's gammas and the general formulas

    This notebook repeats the tools of Notebook 06a, so that it runs on its own. The
    next cell reads the author's gammas and the matrix $C$ from
    `Revision/algebra/gammas.json`, checks the 64 Clifford relations, builds the 28
    matrices $S^{ab}$, and defines the exact zero test `is_zero` (first a fast route
    through exponential functions, then sympy's `simplify`; it never calls a nonzero
    expression zero) and `record_passed`, which reads a Revision report and tells
    whether a check is recorded as passed. It reads the history of the record.

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
    THEORY_FILE = "Revision/theory/field-theory.json"
    CURVATURE = "Revision/gkd_lovelock/results/curvature.json"
    CURVATURE_PY = "Revision/gkd_lovelock/results/python-lovelock-report.json"
    PARAMETERS = "Revision/kohn_sham/results/parameters.json"
    physics = json.loads(repository_file(PARAMETERS).read_text(encoding="utf-8"))["physics"]
    A_EXACT = sp.nsimplify(physics["historyA"])  # the slope A of the history, 1
    BETA_B4 = sp.nsimplify(physics["historyBeta"])  # the exponent of b4, 4/3
    B4_ZERO = sp.nsimplify(physics["historyB4AtZero"])  # b4(0) = 1
    check(A_EXACT == 1 and BETA_B4 == sp.Rational(4, 3) and B4_ZERO == 1,
          "the history of the record: a4 = A H x4, b4 = b4(0) e^(4 A H x4/3), A = 1, "
          "b4(0) = 1",
          record=f"{PARAMETERS}, physics.historyA, historyBeta and historyB4AtZero")
    '''),
    md(r"""
    The next cell defines the four general formulas as Python functions, exactly as
    in Notebook 06a: `christoffel(g, coords)` gives $\Gamma^l{}_{mn}$;
    `spin_connection(e, Gam, coords, eta)` gives $\omega_{\mu ab}$ for any vielbein
    matrix `e` (row = frame index, column = coordinate; its inverse `E = e.inv()` has
    `E[nu, b]` $= e_b{}^\nu$); `spinor_connection(omega, S)` gives $\Omega_\mu =
    \sum_{a<b}\omega_{\mu ab}S^{ab}$; `curved_gammas(e, gammas)` gives $\gamma^\mu =
    \sum_a e_a{}^\mu\gamma^a$. For the boosted vielbein the entries contain
    $\cosh b$ and $\sinh b$; `spin_connection` simplifies every entry, which is one of
    the slowest steps of the notebook.
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
    functions $a_4(x_4)$ and $b_4(x_4) > 0$, $z = 6Hx_0$, the warp factor `W` with its
    derivative rule), the diagonal vielbein, the Christoffel symbols, the spin
    connection, $\Omega_\mu$ and the curved gammas, and checks the result of Notebook
    06a, $\gamma^\mu\Omega_\mu = c_g\gamma^{(x0)} + v_g\gamma^{(x4)}$, the record's
    value. This is the CONTROL of the boosted computation: the same code, with no
    boost, must give the known value. The dictionaries `on_history` and
    `history_values` put in the history of the record ($a_4' = AH$, $b_4' =
    \frac43AH\,b_4$, then $a_4 = AHx_4$, $b_4 = e^{4AHx_4/3}$ with $A = 1$), where the
    value is $\frac32He^{Hx_4/3}\gamma^{(x0)} + \frac56H\gamma^{(x4)}$.
    """),
    code(r'''
    x = sp.symbols("x0:8", real=True)  # x[0] = x0, ..., x[4] = x4, ..., x[7] = x7
    x0, x4 = x[0], x[4]
    H = sp.Symbol("H", positive=True)
    a4 = sp.Function("a4")(x4)  # any function of the time
    b4 = sp.Function("b4", positive=True)(x4)  # any positive function of the time
    a4p, b4p = sp.Derivative(a4, x4), sp.Derivative(b4, x4)
    z = 6 * H * x0


    class W(sp.Function):
        """The warp factor W(x0) = (sin(6 H x0)^2)^(1/12) > 0 of the extra times."""

        def fdiff(self, argindex=1):
            """dW/dx0 = H cot(6 H x0) W, for every real z = 6 H x0 with sin z != 0."""
            return H * sp.cot(6 * H * self.args[0]) * self

        def _eval_is_positive(self):
            return True  # the positive root


    s_b = sp.exp(-a4) * sp.sqrt(b4)  # the hidden scale
    f = ([s_b * sp.cot(z)] + [sp.exp(a4)] * 3 + [sp.Integer(1)]
         + [s_b * W(x0)] * 3)  # f_0, ..., f_7
    g = sp.diag(*[ETA[a] * f[a] ** 2 for a in range(8)])  # the corrected metric
    e = sp.diag(*f)  # the diagonal vielbein
    on_history = {b4p: BETA_B4 * A_EXACT * H * b4, a4p: A_EXACT * H}  # the derivatives
    history_values = {a4: A_EXACT * H * x4, b4: B4_ZERO * sp.exp(BETA_B4 * A_EXACT * H * x4)}


    Gam = christoffel(g, x)
    omega = spin_connection(e, Gam, x, ETA)
    Omega = spinor_connection(omega, S)
    gup = curved_gammas(e, gamma)
    slash = sum((gup[mu] * Omega[mu] for mu in range(8)), Z16)
    c_g = sp.Rational(3, 2) * H * sp.exp(a4) / sp.sqrt(b4)  # coefficient of gamma^(x0)
    v_g = b4p / b4 - a4p / 2  # coefficient of gamma^(x4)
    slash_history = slash.subs(on_history).subs(history_values)
    check(matrix_is_zero(slash - c_g * gamma[0] - v_g * gamma[4])
          and matrix_is_zero(slash_history - sp.Rational(3, 2) * H * sp.exp(H * x4 / 3)
                             * gamma[0] - sp.Rational(5, 6) * H * gamma[4]),
          "control: the diagonal vielbein gives gamma^mu Omega_mu = c_g gamma^(x0) + "
          "v_g gamma^(x4), on the history (3/2) H e^(H x4/3) gamma^(x0) + (5/6) H "
          "gamma^(x4)",
          record=f"{SCOPE_PY}, check rescaling_removes_the_connection_term")
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
        c_b, s_b_value = np.cosh(b_value), np.sinh(b_value)
        ax.annotate("", xy=(c_b, s_b_value), xytext=(0, 0), arrowprops=dict(
            arrowstyle="-|>", color="tab:blue", alpha=alpha, linewidth=1.6))
        ax.annotate("", xy=(s_b_value, c_b), xytext=(0, 0), arrowprops=dict(
            arrowstyle="-|>", color="tab:orange", alpha=alpha, linewidth=1.6))
        ax.text(c_b + 0.04, s_b_value - 0.12, f"$b = {b_value:g}$", fontsize=8,
                color="tab:blue")
        ax.text(s_b_value - 0.30, c_b + 0.06, f"$b = {b_value:g}$", fontsize=8,
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

    Now the rapidity depends on the time: $b = b(x_4)$, an unknown function, so that
    every result holds for every rapidity; a constant rate, $b = \beta x_4 + b_0$, is
    the special case $b' = \beta$. The boosted vielbein is the matrix product
    $e' = \Lambda(b)\,e$. The next cell checks that it describes the corrected metric
    (all 64 entries of $e'^T\eta e'$), computes its canonical spin connection, and
    checks the vielbein postulate (512 equations) and the antisymmetry
    $\omega'_{\mu ab} = -\omega'_{\mu ba}$, for every $a_4$, $b_4$ and $b$: the record's
    checks `boosted_frame_reproduces_metric` and `boosted_frame_canonical_connection`.
    """),
    code(r'''
    b = sp.Function("b", real=True)(x4)  # the rapidity: any function of the time
    bp = sp.Derivative(b, x4)  # its rate b'
    L = boost(b)
    e_boosted = L * e  # e'^a_mu = sum_c Lambda^a_c e^c_mu
    check(matrix_is_zero(e_boosted.T * eta_matrix * e_boosted - g),
          "the boosted vielbein gives the corrected metric (64 entries)",
          record=f"{SCOPE_PY}, check boosted_frame_reproduces_metric")
    omega_b = spin_connection(e_boosted, Gam, x, ETA)  # omega'_{mu ab}
    postulate = [sp.diff(e_boosted[a, nu], x[mu])
                 - sum(Gam[lam][mu][nu] * e_boosted[a, lam] for lam in range(8))
                 + sum(ETA[a] * omega_b[mu][a][c] * e_boosted[c, nu] for c in range(8))
                 for mu in range(8) for a in range(8) for nu in range(8)]
    antisymmetric = all(is_zero(omega_b[mu][a][c] + omega_b[mu][c][a])
                        for mu in range(8) for a in range(8) for c in range(8))
    check(all(is_zero(v) for v in postulate) and antisymmetric,
          "boosted vielbein: vielbein postulate (512) and antisymmetry of omega'",
          record=f"{SCOPE_PY}, check boosted_frame_canonical_connection")
    Omega_b = spinor_connection(omega_b, S)  # Omega'_mu
    gup_b = curved_gammas(e_boosted, gamma)  # gamma'^mu
    count_b = sum(1 for mu in range(8) for a in range(8) for c in range(a + 1, 8)
                  if omega_b[mu][a][c] != 0)
    say(f"nonzero components omega'_mu ab with a < b: {count_b}")
    '''),
    md(r"""
    ## 9. The contraction in the boosted vielbein

    The next cell computes $\gamma'^\mu\Omega'_\mu$ (summed over $\mu$) and compares it,
    exactly, for symbolic $a_4$, $b_4$, $H$ and rapidity $b(x_4)$, with

    $$\gamma'^\mu\Omega'_\mu = \Big(c_g - \frac{b'}{2}\Big)\,v + v_g\,w, \qquad
    v = \cosh b\,\gamma^{(x0)} - \sinh b\,\gamma^{(x4)},\quad
    w = \cosh b\,\gamma^{(x4)} - \sinh b\,\gamma^{(x0)} .$$

    For a constant rate, $b = \beta x_4 + b_0$, this is the record's formula with
    $c_g - \beta/2$. At $b = 0$ (no boost) it gives back $c_g\gamma^{(x0)} +
    v_g\gamma^{(x4)}$. The cell also reads off the two coefficients $c_0$ and $c_4$ of
    $\gamma'^\mu\Omega'_\mu = c_0\gamma^{(x0)} + c_4\gamma^{(x4)}$ and checks that
    $\cosh b\,c_4 + \sinh b\,c_0 = v_g$ for every rapidity: this combination does not
    depend on the boost at all, so no boost in this plane can make
    $\gamma'^\mu\Omega'_\mu$ vanish unless $v_g = 0$, that is $b_4'/b_4 = a_4'/2$.
    """),
    code(r'''
    slash_b = sum((gup_b[mu] * Omega_b[mu] for mu in range(8)), Z16)
    v = sp.cosh(b) * gamma[0] - sp.sinh(b) * gamma[4]  # R gamma^(x0) R^-1 (Section 11)
    w = sp.cosh(b) * gamma[4] - sp.sinh(b) * gamma[0]  # R gamma^(x4) R^-1
    formula = (c_g - bp / 2) * v + v_g * w
    beta, b0 = sp.symbols("beta b0", real=True)  # a constant rate and a start value
    constant_rate = {bp: beta}  # b' = beta for b = beta x4 + b0
    record_form = ((c_g - beta / 2) * v + v_g * w).subs(b, beta * x4 + b0)
    check(matrix_is_zero(slash_b - formula)
          and matrix_is_zero(slash_b.subs(constant_rate).subs(b, beta * x4 + b0)
                             - record_form),
          "gamma'^mu Omega'_mu = (c_g - b'/2) v + v_g w for every rapidity b(x4)",
          record=f"{SCOPE_PY}, check boosted_frame_gammaOmega_formula")
    c0 = sp.simplify((slash_b * gamma[0]).trace() / 16)  # coefficient of gamma^(x0)
    c4 = sp.simplify(-(slash_b * gamma[4]).trace() / 16)  # coefficient of gamma^(x4)
    check(is_zero(sp.cosh(b) * c4 + sp.sinh(b) * c0 - v_g)
          and matrix_is_zero(formula.subs(bp, 0).subs(b, 0) - c_g * gamma[0]
                             - v_g * gamma[4]),
          "cosh b c4 + sinh b c0 = v_g for every rapidity; no boost gives c_g gamma^(x0) "
          "+ v_g gamma^(x4)",
          record=f"{SCOPE_WL}, check boosted_frame_removes_only_the_H_term")
    '''),
    md(r"""
    The next cell draws the two coefficients on the history of the record ($H = 1$,
    $c_g = \frac32e^{x_4/3}$, $v_g = \frac56$) as functions of the time, for three
    frames: no boost ($b = 0$: $c_0 = c_g$, which grows with the time, and
    $c_4 = v_g$); a boost with the constant rate $b = 3x_4$, which removes
    the term $c_g$ only at the time $x_4 = 0$, where $c_g = \frac32 = b'/2$; and the
    rapidity $b = 9(e^{x_4/3} - 1)$, whose rate $b' = 3e^{x_4/3} = 2c_g$ removes the
    term $c_g$ at every time, so that only $v_g w$ is left: $c_0 = -\frac56\sinh b$,
    $c_4 = \frac56\cosh b$. The curves are made from the formula that the previous cell
    proved.
    """),
    code(r'''
    times = np.linspace(-0.5, 0.5, 101)
    t_symbol = sp.Symbol("t", real=True)
    c_g_history = c_g.subs(history_values)  # (3/2) H e^(H x4/3)
    v_g_history = v_g.subs(on_history).subs(history_values)  # (5/6) H
    frames = [("no boost, $b = 0$", sp.Integer(0), "-"),
              ("constant rate, $b = 3x_4$", 3 * H * x4, "--"),
              ("$b = 9(e^{x_4/3} - 1)$, $b' = 2c_g$", 9 * (sp.exp(H * x4 / 3) - 1), "-.")]
    fig, (ax_left, ax_right) = plt.subplots(1, 2, figsize=(10.0, 4.2), sharey=True)
    for label, rapidity_function, style in frames:
        rate = sp.diff(rapidity_function, x4)
        coefficient_x0 = ((c_g_history - rate / 2) * sp.cosh(rapidity_function)
                          - v_g_history * sp.sinh(rapidity_function))
        coefficient_x4 = (-(c_g_history - rate / 2) * sp.sinh(rapidity_function)
                          + v_g_history * sp.cosh(rapidity_function))
        c0_numbers = sp.lambdify(t_symbol, coefficient_x0.subs({H: 1, x4: t_symbol}))
        c4_numbers = sp.lambdify(t_symbol, coefficient_x4.subs({H: 1, x4: t_symbol}))
        ax_left.plot(times, np.broadcast_to(c0_numbers(times), times.shape), style,
                     label=label)
        ax_right.plot(times, np.broadcast_to(c4_numbers(times), times.shape), style,
                      label=label)
    ax_left.set_title("coefficient $c_0$ of $\\gamma^{(x0)}$")
    ax_right.set_title("coefficient $c_4$ of $\\gamma^{(x4)}$")
    for ax in (ax_left, ax_right):
        ax.axhline(0.0, color="black", linewidth=0.6)
        ax.set_xlabel("time $x_4$ (units $1/H$), history $a_4 = x_4$")
        ax.legend(fontsize=8)
    ax_left.set_ylabel("coefficient in $\\gamma'^\\mu\\Omega'_\\mu$ (units of $H$)")
    save_figure(fig, "boosted_contraction",
                "The contraction $\\gamma'^\\mu\\Omega'_\\mu = c_0\\gamma^{(x0)} + "
                "c_4\\gamma^{(x4)}$ in three frames of the same metric, on the history "
                "of the Revision record with $H = 1$ ($c_g = \\frac32e^{x_4/3}$, "
                "$v_g = \\frac56$): the coefficient $c_0$ (left) and $c_4$ (right) "
                "versus the time $x_4$ in units $1/H$. Solid: no boost, $c_0 = c_g$ and "
                "$c_4 = v_g$. Dashed: the constant rapidity rate $b = 3x_4$, which "
                "removes the $c_g$ term only at $x_4 = 0$. Dash-dotted: the rapidity "
                "$b = 9(e^{x_4/3} - 1)$ with $b' = 2c_g$, which removes it at every "
                "time and leaves $v_g(\\cosh b\\,\\gamma^{(x4)} - \\sinh b\\,"
                "\\gamma^{(x0)})$: the same metric, a different frame, a different "
                "value.")
    '''),
    md(r"""
    ## 10. The rate $b' = 2c_g$ removes the $c_g$ term, not the $v_g$ term

    The next cell puts $b' = 2c_g$ into the boosted spin connection (substituting
    after the computation is allowed, because the computation was done for every
    rapidity). It checks that $\gamma'^\mu\Omega'_\mu = v_g\,w$ is all that remains,
    for every $H > 0$, $a_4$ and $b_4$ (the record's check
    `boosted_frame_removes_only_the_H_term`), and that $\Omega'_\mu$ is nonzero for all
    eight $\mu$: a matrix is not the zero matrix as soon as one of its entries is
    clearly nonzero at one point, so the cell evaluates the entries at the sample point
    of the history used below. The contraction would vanish only where $v_g = 0$; on
    the history of the record it is $\frac56H\,w \ne 0$. The rescaling of Section 14
    removes the whole term.
    """),
    code(r'''
    B4_SAMPLE = sp.exp(sp.Rational(2, 3))  # b4 at a4 = 1/2 on the history, b4(0) = 1
    B_SAMPLE = 9 * (sp.exp(sp.Rational(1, 6)) - 1)  # the rapidity 9 (e^(x4/3) - 1)


    def at_sample(expr):
        """The decimal value of expr at H = 1, z = pi/4, x4 = 1/2 on the history of the
        record (a4 = 1/2, a4' = 1, a4'' = 0, b4 = e^(2/3), b4' = (4/3) b4, b4'' =
        (16/9) b4) with the rapidity b = 9 (e^(x4/3) - 1): b = 9 (e^(1/6) - 1),
        b' = 3 e^(1/6), b'' = e^(1/6) (derivatives first, then the functions)."""
        rate = sp.Rational(4, 3)  # b4'/b4
        expr = sp.sympify(expr).subs(sp.Derivative(b, (x4, 2)), sp.exp(sp.Rational(1, 6)))
        expr = expr.subs(bp, 3 * sp.exp(sp.Rational(1, 6))).subs(b, B_SAMPLE)
        expr = expr.subs(sp.Derivative(a4, (x4, 2)), 0)
        expr = expr.subs(sp.Derivative(b4, (x4, 2)), rate**2 * B4_SAMPLE)
        expr = expr.subs({a4p: 1, b4p: rate * B4_SAMPLE})
        expr = expr.subs({a4: sp.Rational(1, 2), b4: B4_SAMPLE})
        expr = expr.subs(W(x0), sp.Abs(sp.sin(z)) ** sp.Rational(1, 6))  # explicit W
        expr = expr.subs({H: 1, x4: sp.Rational(1, 2), x0: sp.pi / 24})
        return float(sp.N(expr))


    def sample_table(matrix):
        return np.array([[at_sample(v) for v in row] for row in matrix.tolist()])


    removing = {bp: 2 * c_g}  # the rate b' = 2 c_g = 3 H e^(a4) b4^(-1/2)
    slash_removed = slash_b.subs(removing)
    Omega_removed = [M.subs(removing) for M in Omega_b]
    nonzero = [NAMES[mu] for mu in range(8)
               if np.abs(sample_table(Omega_removed[mu])).max() > 1e-9]
    say(f"Omega'_mu is nonzero for mu = {nonzero}")
    check(matrix_is_zero(slash_removed - v_g * w) and nonzero == NAMES,
          "b' = 2 c_g: gamma'^mu Omega'_mu = v_g w, only the v_g term remains; "
          "Omega'_mu nonzero for all eight mu",
          record=f"{SCOPE_PY}, check boosted_frame_removes_only_the_H_term")
    '''),
    md(r"""
    The next cell draws three 16 x 16 matrices of the boosted vielbein with $b' = 2c_g$
    at the sample point $H = 1$, $x_4 = 1/2$, $z = \pi/4$, with the values $a_4 = 1/2$,
    $a_4' = 1$, $b_4 = e^{2/3}$, $b_4'/b_4 = 4/3$ of the history of the record and the
    rapidity $b = 9(e^{1/6} - 1) = 1.632$: the spinor connection $\Omega'_{x4}$ (in the
    diagonal vielbein $\Omega_{x4} = 0$; here it is not, because the frame turns with
    time), $\Omega'_{x0}$, and the total contraction $\gamma'^\mu\Omega'_\mu$, which is
    only the term $v_g w$.
    """),
    code(r'''
    panels = [("$\\Omega'_{x4}$", Omega_removed[4]), ("$\\Omega'_{x0}$", Omega_removed[0]),
              ("$\\gamma'^\\mu\\Omega'_\\mu$ (only the $v_g$ term)", slash_removed)]
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
                "The boosted vielbein with the rapidity rate $b' = 2c_g$ at the sample "
                "point $H = 1$, $x_4 = 1/2$, $z = \\pi/4$, $a_4 = 1/2$, $a_4' = 1$, "
                "$b_4 = e^{2/3}$, $b_4'/b_4 = 4/3$ (the history of the Revision record "
                "at $a_4 = 1/2$) with the rapidity $b = 9(e^{1/6} - 1) = 1.632$, as "
                "16 x 16 heat maps (red positive, blue negative, white zero; rows and "
                "columns are the spinor components; each panel has its own colour "
                "scale). Left: $\\Omega'_{x4}$, nonzero because the frame turns with "
                "time; middle: $\\Omega'_{x0}$; right: the contraction "
                "$\\gamma'^\\mu\\Omega'_\\mu$, which is only the term "
                "$v_g(\\cosh b\\,\\gamma^{(x4)} - \\sinh b\\,\\gamma^{(x0)})$: the boost "
                "removed the term $c_g\\gamma^{(x0)}$.")
    check(np.abs(tables[2] - sample_table(v_g * w)).max() < 1e-12
          and np.abs(tables[2]).max() > 0.1 and np.abs(tables[0]).max() > 0.1,
          "at the sample point Omega'_x4 is nonzero and the contraction is the v_g term")
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
       $R(c_g\gamma^{(x0)} + v_g\gamma^{(x4)})R^{-1} = c_gv + v_gw$, and the extra
       term $\sum_\mu\gamma'^\mu(\partial_\mu R)R^{-1} = \frac{b'}{2}\,v$ (only
       $\mu = x4$ contributes, because $R$ depends on $x_4$ only). Their difference is
       the formula of Section 9.
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
          and matrix_is_zero(turned - c_g * v - v_g * w)
          and matrix_is_zero(extra - bp / 2 * v),
          "R g0 R^-1 = v, R g4 R^-1 = w; turned term c_g v + v_g w; extra term "
          "(b'/2) v")
    '''),
    md(r"""
    ## 12. The curvature: the Riemann tensor has only plane components

    The next cell computes the Riemann tensor of the corrected metric from the
    Christoffel symbols with the convention $R^\rho{}_{\sigma\mu\nu} =
    \partial_\mu\Gamma^\rho{}_{\nu\sigma} - \partial_\nu\Gamma^\rho{}_{\mu\sigma} +
    \sum_\lambda(\Gamma^\rho{}_{\mu\lambda}\Gamma^\lambda{}_{\nu\sigma} -
    \Gamma^\rho{}_{\nu\lambda}\Gamma^\lambda{}_{\mu\sigma})$ (it keeps the components
    with $\mu < \nu$; the others follow from the antisymmetry in $\mu, \nu$). A
    component is kept as nonzero when its value at the sample point is clearly
    different from zero (which proves it is not identically zero) or, failing that,
    when the exact test says it is not zero. Then it raises the second index,
    $R^{ab}{}_{cd} = R^a{}_{bcd}/g_{bb}$ (the metric is diagonal), and checks the
    statement of the Revision curvature record `curvature.json`: every nonzero
    $R^{ab}{}_{cd}$ has $\{c, d\} = \{a, b\}$, so the tensor consists of the 28
    curvatures $K(a, b) = R^{ab}{}_{ab}$ of the coordinate planes, each appearing in
    four entries (112 in all), and every one of them is independent of $x_0$. It
    compares all 112 entries with the record (`riemannMixedNonzero`) and prints the
    eight different plane curvatures.
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
    raised = {key: value / g[key[1], key[1]] for key, value in riemann.items()}  # R^ab_cd
    record = json.loads(repository_file(CURVATURE).read_text(encoding="utf-8"))


    def from_record(text):
        """A component of the curvature record (Wolfram notation) as a sympy expression."""
        for long_form, short_form in (("Derivative[1][a4][x4]", "a4p"),
                                      ("Derivative[2][a4][x4]", "a4pp"),
                                      ("Derivative[1][b4][x4]", "b4p"),
                                      ("Derivative[2][b4][x4]", "b4pp"),
                                      ("a4[x4]", "a4"), ("b4[x4]", "b4")):
            text = text.replace(long_form, short_form)
        names = {"H": H, "a4": a4, "b4": b4, "a4p": a4p, "b4p": b4p,
                 "a4pp": sp.Derivative(a4, (x4, 2)), "b4pp": sp.Derivative(b4, (x4, 2))}
        return parse_mathematica(text).subs({sp.Symbol(k): v for k, v in names.items()},
                                            simultaneous=True)


    record_riemann = {(NAMES.index(item["up"][0]), NAMES.index(item["up"][1]),
                       NAMES.index(item["down"][0]), NAMES.index(item["down"][1])):
                      from_record(item["value"]) for item in record["riemannMixedNonzero"]}
    planes_only = all({c, d} == {a, bb} for (a, bb, c, d) in raised)
    check(planes_only and len(raised) == 112 and set(raised) == set(record_riemann)
          and all(is_zero(raised[k] - record_riemann[k]) for k in raised)
          and all(is_zero(sp.diff(value, x0)) for value in record_riemann.values())
          and record_passed(CURVATURE_PY, "mixed_riemann_only_sectional")
          and record_passed(CURVATURE_PY, "rust_riemann_agrees"),
          "only the 28 plane curvatures K(a, b) are nonzero (112 entries R^ab_cd), free "
          "of x0, equal to the record",
          record=f"{CURVATURE}, riemannMixedNonzero; {CURVATURE_PY}, check "
                 "mixed_riemann_only_sectional")
    K = {(a, bb): record_riemann[(a, bb, a, bb)] for a in range(8) for bb in range(a + 1, 8)}
    for a, bb in [(0, 1), (0, 4), (0, 5), (1, 2), (1, 4), (1, 5), (4, 5), (5, 6)]:
        say(f"K({NAMES[a]}, {NAMES[bb]}) = {K[(a, bb)]}")
    '''),
    md(r"""
    The next cell contracts the Riemann tensor to the mixed Ricci tensor $R^\mu{}_\nu$,
    the Ricci scalar and the Einstein tensor $G^\mu{}_\nu = R^\mu{}_\nu -
    \frac12\delta^\mu_\nu R$, and checks four things. First, $R^\mu{}_\nu$ is DIAGONAL:
    all 56 components off the diagonal vanish (because only plane components exist), and
    the eight diagonal ones and $R$ equal the record `field-theory.json`
    (`ricci_mixed_nonzero`, `ricci_scalar`); the Einstein tensor, all 64 components,
    equals `einsteinMixed` of `curvature.json`, so it has no component off the diagonal
    either. Second, for the flat member $a_4 = 0$, $b_4 = H^2x_4^2$ all 28 plane
    curvatures vanish: the metric is flat there (8-dimensional flat space in unusual
    coordinates), as the record states. Third, on the history of the record the metric
    is curved: $K(x1, x2) = a_4'^2 = H^2$ and the Ricci scalar is $R = H^2\big(
    \frac{56}{9} - 12e^{2Hx_4/3}\big)$. Fourth, the record's scope check
    `gammaOmega_sees_the_hidden_block`: $\gamma^\mu\Omega_\mu$ contains the function
    $a_4$ (through $e^{a_4}$ and $a_4'$), unlike the term of the withdrawn metric of
    2026-10-14.
    """),
    code(r'''
    ricci_lower = sp.Matrix(8, 8, lambda sg, nu: sum(
        riemann.get((r, sg, r, nu), 0) for r in range(8)))  # R_sigma nu
    ricci_mixed = g.inv() * ricci_lower  # R^mu_nu = g^mu sigma R_sigma nu
    ricci_scalar = sum(ricci_mixed[a, a] for a in range(8))
    names = {"H": H, "x0": x0, "x4": x4, "a4": a4, "b4": b4, "a4p": a4p, "b4p": b4p,
             "a4pp": sp.Derivative(a4, (x4, 2)), "b4pp": sp.Derivative(b4, (x4, 2))}
    FORMULAS = {item["key"]: item["wl"] for item in json.loads(
        repository_file(THEORY_FILE).read_text(encoding="utf-8"))["formulas"]}
    # the record's list {mu, nu, value}: R^mu_nu, directions numbered from 1 (x0 is 1)
    ricci_record = {(int(m) - 1, int(n) - 1): value
                    for m, n, value in from_record(FORMULAS["ricci_mixed_nonzero"])}
    off_diagonal = all(is_zero(ricci_mixed[m, n]) for m in range(8) for n in range(8)
                       if m != n)
    einstein = ricci_mixed - sp.eye(8) * ricci_scalar / 2  # G^mu_nu
    einstein_record = {(NAMES.index(k.split(",")[0]), NAMES.index(k.split(",")[1])):
                       from_record(item["mathematica"])
                       for k, item in record["einsteinMixed"].items()}
    check(off_diagonal and set(ricci_record) == {(a, a) for a in range(8)}
          and all(is_zero(ricci_mixed[k] - ricci_record[k]) for k in ricci_record)
          and is_zero(ricci_scalar - from_record(FORMULAS["ricci_scalar"]))
          and len(einstein_record) == 64
          and all(is_zero(einstein[k] - einstein_record[k]) for k in einstein_record)
          and record_passed(REPORT_WL, "ricci_mixed_components")
          and record_passed(CURVATURE_PY, "rust_ricci_einstein_scalar_agree"),
          "the mixed Ricci and Einstein tensors are diagonal (56 components off the "
          "diagonal vanish) and equal the records",
          record=f"{THEORY_FILE}, formulas ricci_mixed_nonzero and ricci_scalar; "
                 f"{CURVATURE}, einsteinMixed")
    for a in (0, 1, 4):
        say(f"R^{NAMES[a]}_{NAMES[a]} = {ricci_record[(a, a)]}")


    def on_member(expr, a4_value, b4_value):
        """expr for the given functions a4 and b4 (derivatives carried out)."""
        return sp.simplify(sp.sympify(expr).subs({a4: a4_value, b4: b4_value}).doit())


    flat = [on_member(K[key], 0, H**2 * x4**2) for key in K]  # the flat member
    on_hist = {key: on_member(K[key], A_EXACT * H * x4,
                              B4_ZERO * sp.exp(BETA_B4 * A_EXACT * H * x4)) for key in K}
    R_history = on_member(from_record(FORMULAS["ricci_scalar"]), A_EXACT * H * x4,
                          B4_ZERO * sp.exp(BETA_B4 * A_EXACT * H * x4))
    say(f"on the history: R = {sp.factor(R_history)}")
    check(all(value == 0 for value in flat) and is_zero(on_hist[(1, 2)] - H**2)
          and is_zero(R_history - H**2 * (sp.Rational(56, 9) - 12 * sp.exp(2 * H * x4 / 3)))
          and record_passed(REPORT_WL, "flat_member_and_curvature")
          and record_passed(REPORT_PY, "curvature_and_flat_member"),
          "flat for a4 = 0, b4 = H^2 x4^2 (all 28 plane curvatures vanish); curved on the "
          "history, R = H^2 (56/9 - 12 e^(2 H x4/3))",
          record=f"{REPORT_WL}, check flat_member_and_curvature")
    check(any(entry.has(a4) for entry in slash)
          and record_passed(SCOPE_PY, "gammaOmega_sees_the_hidden_block")
          and record_passed(SCOPE_WL, "gammaOmega_sees_the_hidden_block"),
          "gamma^mu Omega_mu contains a4: it sees the deflation of the hidden block",
          record=f"{SCOPE_PY}, check gammaOmega_sees_the_hidden_block")
    '''),
    md(r"""
    The next cell draws the curvature on the history of the record ($a_4 = x_4$,
    $b_4 = e^{4x_4/3}$, $H = 1$). On the left, the eight diagonal Ricci components
    $R^\mu{}_\mu$ at the time $x_4 = 1/2$ (in units of $H^2$): the hidden direction
    and the three extra times share one value, the three 3-space directions another.
    On the right, three of them and the Ricci scalar $R$ as functions of the time:
    $R^{x1}{}_{x1} = \frac53H^2$ and $R^{x4}{}_{x4} = \frac{31}{9}H^2$ are constant,
    while $R^{x0}{}_{x0} = -(3e^{2x_4/3} + \frac59)H^2$ and $R$ change with the time;
    for the flat member every component is zero (the black line at zero).
    """),
    code(r'''
    t_values = np.linspace(-2.0, 2.0, 161)
    history_numbers = {H: 1, x4: t_symbol}
    ricci_history = [sp.lambdify(t_symbol, on_member(ricci_record[(a, a)], x4,
                                                     sp.exp(sp.Rational(4, 3) * x4))
                                 .subs(history_numbers)) for a in range(8)]
    R_numbers = sp.lambdify(t_symbol, R_history.subs(history_numbers))
    fig, (ax_left, ax_right) = plt.subplots(1, 2, figsize=(10.0, 4.2))
    values = [float(np.broadcast_to(ricci_history[a](0.5), ())) for a in range(8)]
    colors = ["tab:blue"] + ["tab:red"] * 3 + ["gray"] + ["tab:blue"] * 3
    ax_left.bar(range(8), values, color=colors, width=0.6)
    ax_left.axhline(0.0, color="black", linewidth=0.8)
    ax_left.set_xticks(range(8), [f"$R^{{{n}}}{{}}_{{{n}}}$" for n in NAMES], fontsize=8)
    ax_left.set_ylabel("value (units of $H^2$)")
    ax_left.set_title("Ricci components on the history at $x_4 = 1/2$")
    for a, label, style in ((0, "$R^{x0}{}_{x0} = R^{x5}{}_{x5}$", "-"),
                            (1, "$R^{x1}{}_{x1}$", "--"),
                            (4, "$R^{x4}{}_{x4}$", ":")):
        ax_right.plot(t_values, np.broadcast_to(ricci_history[a](t_values),
                                                t_values.shape), style, label=label)
    ax_right.plot(t_values, R_numbers(t_values), "-.", color="gray",
                  label="Ricci scalar $R$")
    ax_right.axhline(0.0, color="black", linewidth=1.2, label="flat member: all zero")
    ax_right.set_ylim(-20.0, 8.0)
    ax_right.set_xlabel("time $x_4$ (units $1/H$), history $a_4 = x_4$, "
                        "$b_4 = e^{4x_4/3}$")
    ax_right.set_ylabel("value (units of $H^2$)")
    ax_right.set_title("Curved on the history")
    ax_right.legend(fontsize=7, loc="lower left")
    save_figure(fig, "ricci_components",
                "The mixed Ricci tensor of the corrected metric, which is diagonal, on "
                "the history of the Revision record ($a_4 = x_4$, $b_4 = e^{4x_4/3}$, "
                "$H = 1$), in units of $H^2$. Left: the eight components "
                "$R^\\mu{}_\\mu$ at $x_4 = 1/2$ (blue: the hidden direction and the "
                "three extra times, which share one value; red: 3-space; gray: time). "
                "Right: $R^{x0}{}_{x0} = R^{x5}{}_{x5}$ (solid), $R^{x1}{}_{x1}$ "
                "(dashed), $R^{x4}{}_{x4}$ (dotted) and the Ricci scalar $R$ (gray "
                "dash-dotted) versus the time $x_4$ in units $1/H$; for the flat member "
                "$a_4 = 0$, $b_4 = H^2x_4^2$ of the family every curvature component is "
                "zero (black line). The metric is curved on the history.")
    '''),
    md(r"""
    ## 13. The curvature of the spinor connection

    The next cell computes, in the diagonal vielbein, the 28 matrices $F_{\mu\nu}$
    ($\mu < \nu$) and checks the theorem $F_{\mu\nu} = \frac12\sum_{a,b}
    R_{ab\mu\nu}S^{ab}$, where $R_{ab\mu\nu} = \eta_{aa}\,f_a\,R^a{}_{b\mu\nu}/f_b$
    is the Riemann tensor with two frame indices (for the diagonal vielbein). Because
    only plane components exist, each $F_{\mu\nu}$ is a multiple of the single
    generator $S^{\mu\nu}$ of its own plane: $F_{\mu\nu} = \eta_{\mu\mu}\eta_{\nu\nu}
    f_\mu f_\nu K(\mu, \nu)\,S^{\mu\nu}$; the cell checks this too. Then it computes
    $F'_{x0\,x5}$ in the boosted vielbein with $b' = 2c_g$ (where the $c_g$ term of the
    contraction vanished) and checks that it is $R\,F_{x0\,x5}R^{-1}$ and is not zero:
    the spinor connection is still there and curved.
    """),
    code(r'''
    def spinor_curvature(Om, mu, nu):
        return (Om[nu].diff(x[mu]) - Om[mu].diff(x[nu])
                + Om[mu] * Om[nu] - Om[nu] * Om[mu])


    F = {}
    theorem_ok, plane_ok = True, True
    for mu in range(8):
        for nu in range(mu + 1, 8):
            F[(mu, nu)] = spinor_curvature(Omega, mu, nu)
            from_riemann = sum((ETA[a] * f[a] * riemann[(a, c, mu, nu)] / f[c] * S[a][c] / 2
                                for a in range(8) for c in range(8)
                                if (a, c, mu, nu) in riemann), Z16)
            theorem_ok = theorem_ok and matrix_is_zero(F[(mu, nu)] - from_riemann)
            plane = ETA[mu] * ETA[nu] * f[mu] * f[nu] * K[(mu, nu)] * S[mu][nu]
            plane_ok = plane_ok and matrix_is_zero(from_riemann - plane)
    check(theorem_ok and record_passed(REPORT_WL, "spin_curvature_equals_Riemann")
          and record_passed(REPORT_PY, "spinor_curvature_equals_riemann"),
          "F_mu nu = (1/2) R_ab mu nu S^ab in all 28 coordinate planes",
          record=f"{REPORT_WL}, check spin_curvature_equals_Riemann")
    check(plane_ok, "F_mu nu = eta_mumu eta_nunu f_mu f_nu K(mu, nu) S^mu nu: one "
          "generator per plane")
    F05_boosted = spinor_curvature(Omega_removed, 0, 5)
    R_removed, R_inv_removed = R.subs(removing), R_inv.subs(removing)
    check(matrix_is_zero(F05_boosted - R_removed * F[(0, 5)] * R_inv_removed)
          and np.abs(sample_table(F05_boosted)).max() > 0.1,
          "boosted (b' = 2 c_g): F'_x0x5 = R F_x0x5 R^-1, nonzero",
          record=f"{SCOPE_PY}, check boosted_frame_curvature_nonzero")
    '''),
    md(r"""
    The next cell draws the size of the spinor curvature in each coordinate plane: for
    every pair $(\mu, \nu)$ the number $\|F_{\mu\nu}\| = \sqrt{\sum_{i,j}
    (F_{\mu\nu})_{ij}^2}$ (the square root of the sum of the squares of the 256
    entries) at the sample point $H = 1$, $z = \pi/4$ with the values of the history at
    $a_4 = 1/2$ ($a_4' = 1$, $a_4^{\prime\prime} = 0$, $b_4 = e^{2/3}$,
    $b_4'/b_4 = 4/3$; diagonal vielbein). By the formula of the previous cell it is
    $2f_\mu f_\nu|K(\mu, \nu)|$, because $S^{\mu\nu}$ has 16 entries $\pm\frac12$. All
    28 planes are curved at this point. In another frame $F'_{\mu\nu} = R\,F_{\mu\nu}
    R^{-1}$ with an invertible matrix $R$, so a change of frame can change the sizes,
    but it can never turn a coloured square white or a white square coloured; for the
    flat member every square would be white.
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
                ax.text(nu, mu, f"{norms[mu, nu]:.2f}", ha="center", va="center",
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
                "$H = 1$, $z = \\pi/4$ with the values $a_4 = 1/2$, $a_4' = 1$, "
                "$a_4^{\\prime\\prime} = 0$, $b_4 = e^{2/3}$, $b_4'/b_4 = 4/3$ of the "
                "history of the Revision record, in units of $H^2$ (darker is larger, "
                "white is zero). It equals $2f_\\mu f_\\nu|K(\\mu, \\nu)|$; all 28 planes "
                "are curved, the three planes inside 3-space most strongly, the three "
                "planes of the time with an extra time most weakly, closely followed by "
                "the plane of the hidden direction and the time. $F_{\\mu\\nu} = "
                "\\frac12 R_{ab\\mu\\nu}S^{ab}$ is the Riemann curvature, which no "
                "change of frame removes.")
    report("largest |F_mu nu| at the sample point (units of H^2)", f"{norms.max():.3f}")
    report("smallest |F_mu nu| at the sample point (units of H^2)",
           f"{norms[norms > 0].min():.3f}")
    curved = [pair for pair in F if norms[pair] > 1e-9]  # the curved planes
    check(len(curved) == 28, "at the sample point all 28 coordinate planes are curved")
    '''),
    md(r"""
    ## 14. The rescaling $\Psi = e^{a_4/2}b_4^{-1}(\sin^2 z)^{-1/8}\,\chi$ removes the term

    A frame change removes part of $\gamma^\mu\Omega_\mu$; a change of the field
    variable removes all of it. Write $\Psi = w_r\,\chi$ with $w_r = e^{a_4/2}b_4^{-1}
    W^{-3/2}$ (so $W^{-3/2} = (\sin^2 z)^{-1/8}$). Then $\gamma^\mu D_\mu\Psi =
    w_r\,\gamma^\mu\partial_\mu\chi + \big(\gamma^\mu\partial_\mu w_r +
    w_r\,\gamma^\mu\Omega_\mu\big)\chi$. The weight depends on $x_0$ and $x_4$, with
    $\gamma^{x0} = \gamma^{(x0)}/f_0$ and $\gamma^{x4} = \gamma^{(x4)}$, so the bracket
    is $\big(\partial_{x0}w_r/f_0 + c_gw_r\big)\gamma^{(x0)} + \big(\partial_{x4}w_r +
    v_gw_r\big)\gamma^{(x4)}$. Now $\partial_{x0}W^{-3/2} = -\frac32H\cot z\,W^{-3/2}$
    and $1/f_0 = e^{a_4}b_4^{-1/2}\tan z$ give $\partial_{x0}w_r/f_0 =
    -\frac32He^{a_4}b_4^{-1/2}w_r = -c_gw_r$, and $\partial_{x4}(e^{a_4/2}b_4^{-1}) =
    (\frac12a_4' - b_4'/b_4)\,e^{a_4/2}b_4^{-1}$ gives $\partial_{x4}w_r = -v_gw_r$:
    the bracket is zero. This is the record's rescaling. The next cell checks this as a
    matrix identity and, for safety, on 16 completely general functions
    $\chi_1, \dots, \chi_{16}$ of all eight coordinates. It also checks the record's
    remark about the potential $U = \frac{\lambda}{2}S^2$: since $w_r$ is real,
    $S[\Psi] = \Psi^\dagger C\Psi = w_r^2\,S[\chi] = e^{a_4}b_4^{-2}W^{-3}S[\chi]$, and
    $W^{-3} = |\sin z|^{-1/2}$, so the rescaled equation is $\gamma^\mu\partial_\mu\chi
    = \big(m + \lambda e^{a_4}S[\chi]/(b_4^2|\sin z|^{1/2})\big)\,\chi$: for $U = 0$
    the term is removed completely; for $U \ne 0$ it becomes a coupling that depends on
    $x_0$ and on $x_4$.
    """),
    code(r'''
    w_r = sp.exp(a4 / 2) / b4 * W(x0) ** sp.Rational(-3, 2)  # the weight
    bracket = sum((gup[mu] * sp.diff(w_r, x[mu]) for mu in range(8)), Z16) + w_r * slash
    chi = sp.Matrix([sp.Function(f"chi{A}")(*x) for A in range(1, 17)])
    psi = w_r * chi
    dirac_psi = sum((gup[mu] * (psi.diff(x[mu]) + Omega[mu] * psi) for mu in range(8)),
                    sp.zeros(16, 1))
    dirac_chi = sum((gup[mu] * chi.diff(x[mu]) for mu in range(8)), sp.zeros(16, 1))
    check(matrix_is_zero(bracket) and all(is_zero(v) for v in dirac_psi - w_r * dirac_chi),
          "gamma^mu D_mu (w chi) = w gamma^mu d_mu chi for w = e^(a4/2) b4^(-1) "
          "(sin^2 z)^(-1/8)",
          record=f"{SCOPE_PY}, check rescaling_removes_the_connection_term")
    chi_conj = sp.Matrix([sp.conjugate(v) for v in chi])  # complex conjugates
    S_psi = (w_r * chi_conj).T * C * (w_r * chi)  # Psi^dagger C Psi (w is real)
    S_chi = chi_conj.T * C * chi
    check(is_zero(S_psi[0, 0] - sp.exp(a4) / b4**2 * W(x0) ** (-3) * S_chi[0, 0]),
          "S[w chi] = e^(a4) b4^(-2) |sin z|^(-1/2) S[chi]",
          record=f"{SCOPE_PY}, check rescaled_equation_quadratic_potential")
    '''),
    md(r"""
    The next cell draws the rescaling for $H = 1$ at the time where $a_4 = 0$ and
    $b_4 = 1$ (the time $x_4 = 0$ of the history; at another time the factor
    $e^{a_4/2}b_4^{-1}$ only changes the unit): on the left the weight
    $W^{-3/2} = (\sin^2 z)^{-1/8}$ across one cell (large near the ends of the cell,
    equal to 1 at the fold $z = \pi/2$); on the right the two terms of the coefficient
    of $\gamma^{(x0)}$, $\partial_{x0}w_r/f_0$ and $c_gw_r$, computed from their sympy
    formulas, and their sum, which is zero at every $z$, on both halves of the cell.
    """),
    code(r'''
    z_values = np.linspace(0.05, np.pi - 0.05, 300)  # one cell, without the ends
    u_symbol = sp.Symbol("u", real=True)  # x0 as a plain symbol for numbers
    at_start = {a4: 0, b4: 1}  # a4 = 0, b4 = 1: the time x4 = 0 of the history


    def numbers(expr):
        """A numerical function of x0 (as u) with H = 1 at a4 = 0, b4 = 1."""
        expr = sp.simplify(expr.subs(at_start).subs(W(x0), sp.Abs(sp.sin(z)) ** sp.Rational(
            1, 6)))
        return sp.lambdify(u_symbol, expr.subs({H: 1}).subs(x0, u_symbol))


    weight = numbers(w_r)
    term_derivative = numbers(sp.diff(w_r, x0) / f[0])
    term_connection = numbers(c_g * w_r)
    u_values = z_values / 6.0  # x0 = z / (6 H) with H = 1
    first, second = term_derivative(u_values), term_connection(u_values)
    fig, (ax_left, ax_right) = plt.subplots(1, 2, figsize=(10.0, 4.2))
    ax_left.plot(z_values, weight(u_values), label="$W^{-3/2} = (\\sin^2 z)^{-1/8}$")
    ax_left.axvline(np.pi / 2, color="gray", linewidth=0.8)  # the fold
    ax_left.set_xlabel("hidden angle $z = 6Hx_0$ (radians), fold at $\\pi/2$")
    ax_left.set_ylabel("weight (pure number)")
    ax_left.set_title("The rescaling weight")
    ax_left.legend(fontsize=8)
    ax_right.plot(z_values, first, label="$\\partial_{x0} w_r/f_0$")
    ax_right.plot(z_values, second, "--",
                  label="$c_g w_r$ (from $\\gamma^\\mu\\Omega_\\mu$)")
    ax_right.plot(z_values, first + second, ":", color="black", label="sum")
    ax_right.axvline(np.pi / 2, color="gray", linewidth=0.8)
    ax_right.set_xlabel("hidden angle $z = 6Hx_0$ (radians), fold at $\\pi/2$")
    ax_right.set_ylabel("coefficient of $\\gamma^{(x0)}\\chi$ (units of $H$)")
    ax_right.set_title("The two terms cancel")
    ax_right.legend(fontsize=8)
    save_figure(fig, "rescaling",
                "The rescaling $\\Psi = w_r\\chi$ with $w_r = e^{a_4/2}b_4^{-1}"
                "(\\sin^2 z)^{-1/8}$, drawn for $H = 1$ at $a_4 = 0$, $b_4 = 1$. Left: "
                "the weight $(\\sin^2 z)^{-1/8}$ versus the hidden angle $z$ in radians "
                "across one cell (vertical line: the fold). Right: the two terms of the "
                "coefficient of $\\gamma^{(x0)}\\chi$ in the field equation of $\\chi$, "
                "the derivative term $\\partial_{x0}w_r/f_0 = -c_gw_r$ (solid) and the "
                "spin-connection term $c_gw_r$ (dashed), in units of $H$, and their sum "
                "(dotted), which is zero at every $z$: in the variable $\\chi$ the "
                "equation has no term $c_g\\gamma^{(x0)}$ (and, by the factor "
                "$e^{a_4/2}b_4^{-1}$, no term $v_g\\gamma^{(x4)}$).")
    check(np.max(np.abs(first + second)) < 1e-12, "the two terms cancel at all 300 points")
    '''),
    md(r"""
    ## 15. The last checks

    The last cell checks that every check of the Revision reports that states a result
    reproduced in this notebook is recorded there as passed (the sympy scope checker
    `python-scope.json`, the WolframScript scope checker `wolfram-scope.json`, which
    shares no code with it, the curvature checks of the field-theory reports and of the
    curvature record, all for the corrected metric), that all six figure files exist in
    the folder Revision/textbook/figures, and prints the number of checks that passed.
    """),
    code(r'''
    scope_names = ["boosted_frame_reproduces_metric", "boosted_frame_canonical_connection",
                   "boosted_frame_gammaOmega_formula",
                   "boosted_frame_removes_only_the_H_term",
                   "boosted_frame_curvature_nonzero",
                   "rescaling_removes_the_connection_term",
                   "rescaled_equation_quadratic_potential",
                   "gammaOmega_sees_the_hidden_block"]
    cited = {SCOPE_PY: scope_names, SCOPE_WL: scope_names,
             REPORT_PY: ["spinor_curvature_equals_riemann", "curvature_and_flat_member"],
             REPORT_WL: ["ricci_scalar", "ricci_mixed_components",
                         "flat_member_and_curvature", "spin_curvature_equals_Riemann"],
             CURVATURE_PY: ["mixed_riemann_only_sectional", "rust_riemann_agrees",
                            "rust_ricci_einstein_scalar_agree", "k1_offdiagonal_vanishes"]}
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

    - A boost of the frame in the $(x4, x0)$ plane with any rapidity $b(x_4)$ describes
      the same metric, and its canonical spin connection obeys the vielbein postulate.
      In it $\gamma'^\mu\Omega'_\mu = (c_g - \frac{b'}{2})(\cosh b\,\gamma^{(x0)} -
      \sinh b\,\gamma^{(x4)}) + v_g(\cosh b\,\gamma^{(x4)} - \sinh b\,\gamma^{(x0)})$
      exactly (PROVED; reproduces the record). For the rapidity with $b' = 2c_g$ the
      term $c_g\gamma^{(x0)}$ is gone at every time and only the term of $v_g$ remains
      ($\frac56H(\cosh b\,\gamma^{(x4)} - \sinh b\,\gamma^{(x0)})$ on the history of
      the record), while $\Omega'_\mu$ is nonzero for all eight $\mu$. For every
      rapidity $\cosh b\,c_4 + \sinh b\,c_0 = v_g$: no boost in this plane removes the
      $v_g$ term.
    - The reason is the local spin covariance: with the spinor boost
      $R = \cosh\frac b2 - \sinh\frac b2\,\gamma^{(x4)}\gamma^{(x0)}$, $\Omega'_\mu =
      R\Omega_\mu R^{-1} - (\partial_\mu R)R^{-1}$, and the second term contributes
      $-\frac{b'}{2}(\cosh b\,\gamma^{(x0)} - \sinh b\,\gamma^{(x4)})$ (PROVED here).
    - So the value of $\gamma^\mu\Omega_\mu$ in the diagonal vielbein is
      FRAME-DEPENDENT. What is frame-independent is the curvature. The Riemann tensor
      of the corrected metric has only the 28 plane components $K(a, b)$, free of $x_0$
      (112 entries $R^{ab}{}_{cd}$), so the Ricci and Einstein tensors are diagonal
      (PROVED; reproduces the records). The metric is curved on the history of the
      record ($K(x1, x2) = H^2$, $R = H^2(\frac{56}{9} - 12e^{2Hx_4/3})$) and flat for
      the member $a_4 = 0$, $b_4 = H^2x_4^2$ (PROVED; reproduces the records).
    - The spinor curvature is $F_{\mu\nu} = \frac12 R_{ab\mu\nu}S^{ab}$ in all 28 planes
      (PROVED; reproduces the record), one generator per plane, and it is nonzero in
      every frame wherever the metric is curved, because $F' = RFR^{-1}$; therefore no
      frame makes $\Omega_\mu$ vanish there. On the flat member the spin connection is
      a pure frame effect.
    - The term sees the deflation of the hidden block: $\gamma^\mu\Omega_\mu$ contains
      $a_4$ (PROVED; reproduces the record).
    - The rescaling $\Psi = e^{a_4/2}b_4^{-1}(\sin^2 z)^{-1/8}\,\chi$ removes the term
      $\gamma^\mu\Omega_\mu$ from the field equation exactly; with $U = \frac\lambda2
      S^2$ it becomes the coupling $\lambda e^{a_4}S[\chi]/(b_4^2|\sin z|^{1/2})$
      (PROVED; reproduces the record).
    - In short, the non-triviality of the field equations holds in the qualified sense
      of the record: the gravitational field enters through the vielbein factors of
      every derivative term and through a spin connection whose curvature cannot be
      removed where the metric is curved, but the particular term
      $\gamma^\mu\Omega_\mu$ is a property of the chosen frame and field variable.
    """),
]

if __name__ == "__main__":
    raise SystemExit(run_builder(__file__))
