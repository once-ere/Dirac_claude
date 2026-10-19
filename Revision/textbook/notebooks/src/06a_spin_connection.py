#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
"""Builder of Notebook 06a, "The vielbein, the spin connection and gamma^mu Omega_mu"
(textbook "Universes in Pairs", chapter 06).

The notebook Revision/textbook/notebooks/06a_spin_connection.ipynb is BUILT from this
file by Revision/textbook/tools/nbkit.py (never edit the .ipynb by hand):

    python Revision/textbook/tools/nbkit.py build \
        Revision/textbook/notebooks/src/06a_spin_connection.py --date YYYY-MM-DD
    python Revision/textbook/tools/nbkit.py check \
        Revision/textbook/notebooks/src/06a_spin_connection.py

Physics source (the Revision record): the corrected metric of 2026-10-16 (version 2,
Revision/SPEC.md section 1); Revision/theory (field-theory.json and its reports),
Revision/kohn_sham/results/parameters.json (the history) and Revision/lead_checks
(emt-divergence-and-spin-connection.json).  The author's coordinates x0..x7: x0 the
hidden, space-like direction (z = 6 H x0 takes every real value), x1, x2, x3 3-space
(inflating), x4 the time, x5, x6, x7 the three extra times (deflating exponentially).
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools"))
from nbkit import code, md, run_builder  # noqa: E402

FIGURES = [
    "polar_frame_and_spin_rotation",
    "vielbein_factors",
    "christoffel_pattern",
    "omega_heat_maps",
    "spinor_connection_heat_maps",
    "gamma_omega_per_direction",
    "gamma_omega_sum",
    "divergence_form",
    "derivative_coefficients",
    "negative_control",
]

FACTS = {
    "id": "06a",
    "name": "06a_spin_connection",
    "title": "Vielbein, spin connection and the term gamma^mu Omega_mu of the field equation",
    "purpose": (
        "Starting from the corrected metric of the author's primordial field (version 2 "
        "of 2026-10-16) with the functions a4(x4) and b4(x4), for every real z = 6 H x0, "
        "and from the author's real 16 x 16 gamma matrices, it computes exactly, with "
        "sympy, the diagonal vielbein, the Christoffel symbols, the canonical spin "
        "connection, the spinor connection Omega_mu, the covariant derivative of a "
        "spinor and the term gamma^mu Omega_mu = (3/2) H e^(a4) b4^(-1/2) gamma^(x0) + "
        "(b4'/b4 - a4'/2) gamma^(x4) of the field equation; it shows which directions "
        "make each part (the hidden direction and the three extra times share one rate, "
        "3-space has another, and only the three extra times feel the hidden "
        "coordinate), checks the results against the Revision records, repeats the "
        "computation for a negative control whose hidden block grows instead of "
        "deflating, works a two-dimensional warm-up (the polar plane), and draws ten "
        "teaching plots."
    ),
    "records": [
        ["Revision/algebra/gammas.json",
         "the author's eight real 16 x 16 gamma matrices in the order x0 to x7 (input)"],
        ["Revision/theory/field-theory.json",
         "the exact formulas of the field theory for the corrected metric: metric, "
         "vielbein, volume factor, Christoffel symbols, spin connection, gamma^mu "
         "Omega_mu per direction and in total, the 16 component field equations "
         "(reproduced)"],
        ["Revision/kohn_sham/results/parameters.json",
         "the history of the Revision record: the slope A, the exponent beta of b4 and "
         "b4(0) (physics.historyA, physics.historyBeta, physics.historyB4AtZero)"],
        ["Revision/theory/reports/python-field-theory.json",
         "the sympy checks of the geometry, of the spin connection, of gamma^mu Omega_mu "
         "and of the square of the gravity term in the corrected metric"],
        ["Revision/theory/reports/wolfram-field-theory.json",
         "the WolframScript checks of the geometry, the spin connection and the Dirac "
         "operator in the corrected metric"],
        ["Revision/lead_checks/reports/emt-divergence-and-spin-connection.json",
         "the lead's independent checks of the vielbein, of gamma^mu Omega_mu, of its "
         "divergence form and of the negative control with a growing hidden block "
         "(reproduced)"],
    ],
    "packages": ["numpy", "sympy", "matplotlib"],
    "needs_rust": [],
    "expected_seconds": 60,
    "timeout_seconds": 900,
    "files_written": (
        ["Revision/textbook/figures/06a.captions.json"]
        + [f"Revision/textbook/figures/06a_{k}_{name}.png"
           for k, name in enumerate(FIGURES, 1)]
    ),
    "final_lines": [
        "PASS all ten figure files exist",
        "ALL 40 CHECKS PASSED (notebook 06a)",
    ],
    "troubleshooting": [
        ["\"FileNotFoundError\" for Revision/algebra/gammas.json or for a report",
         "the notebook reads Revision records from the repository; open it inside the "
         "folder Revision/textbook/notebooks of a complete copy of the repository "
         "Dirac_claude (a single downloaded notebook file is not enough)."],
        ["a cell runs for many minutes",
         "the exact algebra of sympy is slow on old computers; the whole notebook needs "
         "about a minute on a 2024 laptop, and up to about two minutes while other "
         "programs use the processor. Wait, or close the other programs."],
    ],
}

CELLS = [
    md(r"""
    ## 1. What this notebook computes

    A spinor field (a column of 16 numbers at every point, such as the author's fields
    dirac16complex and dirac16complex00) does not see the metric directly. It sees it
    through a **vielbein** (a set of eight perpendicular unit directions at every point)
    and through the **spin connection** (the rate at which these directions turn from
    point to point). This notebook computes both, exactly, for the corrected metric of
    the author's primordial field (version 2 of 2026-10-16) with its two functions
    $a_4(x_4)$ and $b_4(x_4)$, and the one combination that enters the field equation,

    $$\gamma^\mu \Omega_\mu = c_g\,\gamma^{(x0)} + v_g\,\gamma^{(x4)}, \qquad
    c_g = \tfrac32 H e^{a_4} b_4^{-1/2}, \qquad v_g = \frac{b_4'}{b_4} -
    \frac{a_4'}{2},$$

    which is $\frac32 H e^{Hx_4/3}\gamma^{(x0)} + \frac56 H\gamma^{(x4)}$ on the history
    of the Revision record ($a_4 = Hx_4$, $b_4 = e^{4Hx_4/3}$). It

    - starts with a warm-up in two dimensions (the flat plane in polar coordinates),
      where every step can be followed by hand;
    - builds the diagonal vielbein of the corrected metric, for every real value of
      the hidden coordinate $z = 6Hx_0$, and checks that it gives the metric back;
    - computes the 21 independent nonzero Christoffel symbols, the canonical spin
      connection $\omega_{\mu ab}$ (10 independent nonzero components) and the spinor
      connection $\Omega_\mu$ (16 x 16 matrices built from the author's gammas);
    - checks the vielbein postulate (512 equations), the antisymmetry of $\omega$ and
      the covariant constancy of the gammas (64 matrix equations);
    - computes $\gamma^\mu\Omega_\mu$ direction by direction: the hidden direction
      $x0$ and the three extra times $x5, x6, x7$ share one rate $h_4 = b_4'/(2b_4)
      - a_4'$, 3-space has the rate $a_4'$, and these do NOT cancel: four shrinking
      directions against three growing ones leave $v_g$; the three extra times, whose
      lengths depend on $x_0$, add up to the term $c_g\gamma^{(x0)}$;
    - explains both terms with the divergence form: $v_g$ is half the rate at which
      the 7-volume of a slice changes, $c_g$ comes from the warp of the extra times;
    - writes the covariant derivative and the Dirac operator out in full and compares
      all 16 component equations with the Revision record;
    - shows when the term vanishes for a nonzero field: only where $c_g = \pm v_g$
      (on the history at one single time);
    - repeats the computation for a NEGATIVE CONTROL, a metric whose hidden block
      grows like 3-space instead of shrinking: the coefficient of $a_4'$ changes from
      $-\frac12$ to $+\frac72$;
    - draws ten teaching plots.

    Every result that the Revision record also contains is compared with the record,
    and the check prints the record file and the name of its check.
    """),
    md(r"""
    ## 3. The words used in this notebook

    - **Coordinates** $x0, \dots, x7$: the eight numbers that name a point, with the
      author's names: $x0$ the **hidden direction** (space-like); $x1, x2, x3$
      ordinary 3-space; $x4$ the time; $x5, x6, x7$ the three **extra times**. In
      Python lists they have the positions 0 to 7 (Python counts from 0) in the same
      order, so `x[0]` is $x0$ and `x[4]` is $x4$.
    - $z = 6Hx_0$: the hidden coordinate in angle form; it takes every real value.
      **Degenerate points**: the values with $\sin z \cos z = 0$, where an entry of
      the metric vanishes or grows without bound; nothing is computed there. **Fold**:
      the points $\cos z = 0$ ($z = \pi/2$ and its copies), where the two **halves**
      $0 < z < \pi/2$ and $\pi/2 < z < \pi$ of a **cell** $0 < z < \pi$ meet.
    - **Warp factor** $W = (\sin^2 z)^{1/12}$: the positive twelfth root of
      $\sin^2 z$; the extra-time lengths carry it.
    - **Metric** $g_{\mu\nu}$: the rule that turns small coordinate steps into squared
      lengths, $ds^2 = \sum_\mu g_{\mu\mu} (dx^\mu)^2$ for the author's (diagonal)
      metric. A positive $g_{\mu\mu}$ makes direction $\mu$ **space-like**, a negative
      one **time-like**.
    - **Signature (4,4)**: four space-like directions ($x0, x1, x2, x3$) and four
      time-like ones ($x4, x5, x6, x7$).
    - **Frame metric** $\eta_{ab}$: the constant diagonal matrix
      $\mathrm{diag}(+1,+1,+1,+1,-1,-1,-1,-1)$ in the order $x0, \dots, x7$.
    - **Vielbein** $e^a{}_\mu$ (German "many legs"): at every point eight directions
      that are perpendicular and of unit length, so that
      $g_{\mu\nu} = \sum_{a} \eta_{aa} e^a{}_\mu e^a{}_\nu$. The index $a$ (a
      **frame index**) numbers the eight directions; $\mu$ (a **coordinate index**)
      numbers the coordinates. Its **inverse** $e_a{}^\mu$ satisfies
      $\sum_\mu e^a{}_\mu e_b{}^\mu = \delta^a_b$ (1 if $a = b$, else 0).
    - **Hidden scale** $s_b = e^{-a_4} b_4^{1/2}$: the factor that the hidden
      direction and the three extra times share; its rate is $h_4 = \partial_{x4}
      \ln s_b = b_4'/(2b_4) - a_4'$.
    - **Christoffel symbols** $\Gamma^\lambda{}_{\mu\nu}$: the numbers that say how the
      coordinate directions change from point to point; computed from the first
      derivatives of the metric.
    - **Spin connection** $\omega_\mu{}^a{}_b$: the numbers that say how the vielbein
      turns when one moves along $x^\mu$. The **canonical** one is fixed by the
      **vielbein postulate** (below). Lowering the first frame index with $\eta$ gives
      $\omega_{\mu ab} = \eta_{aa}\,\omega_\mu{}^a{}_b$, which is **antisymmetric**:
      $\omega_{\mu ab} = -\omega_{\mu ba}$.
    - **Gamma matrices** $\gamma^a$: the author's eight real 16 x 16 matrices with
      $\gamma^a\gamma^b + \gamma^b\gamma^a = 2\eta^{ab}\,1$ (the **Clifford
      relation**; $1$ is the 16 x 16 identity matrix). **Curved gammas**:
      $\gamma^\mu = \sum_a e_a{}^\mu \gamma^a$.
    - **Commutator** $[A, B] = AB - BA$; **anticommutator** $\{A, B\} = AB + BA$.
    - $S^{ab} = \frac14[\gamma^a, \gamma^b]$: the 28 matrices (one for each pair
      $a < b$) that turn spinors when the frame is turned.
    - **Spinor connection** $\Omega_\mu = \frac12 \sum_{a,b}\omega_{\mu ab} S^{ab}$: a
      16 x 16 matrix for every $\mu$.
    - **Covariant derivative** of a spinor: $D_\mu \Psi = \partial_\mu \Psi +
      \Omega_\mu \Psi$ ($\partial_\mu$ is the partial derivative with respect to
      $x^\mu$). **Dirac operator**: $\gamma^\mu D_\mu = \sum_\mu \gamma^\mu D_\mu$.
    - **Trace** $\mathrm{tr}\,M$: the sum of the diagonal entries of a square matrix.
    - **Exact** computation: with symbols and fractions (sympy), not with rounded
      decimal numbers; an exact check that an expression is zero proves it for ALL
      values of the symbols.
    - **Negative control**: a deliberately changed case in which the effect must NOT
      occur (or must occur differently); it shows that a check can fail and that the
      result depends on the feature that was changed.
    - **Heat map**: a picture of a matrix in which every entry is a small coloured
      square; here red is positive, blue is negative and white is zero.
    """),
    md(r"""
    ## 4. The physical and mathematical situation

    **The corrected metric.** With $z = 6 H x_0$ (every real value), a positive
    constant $H$ and two functions of the time, $a_4(x_4)$ and $b_4(x_4) > 0$,

    $$g = \mathrm{diag}\big(e^{-2a_4}b_4\cot^2 z,\ e^{2a_4},\ e^{2a_4},\ e^{2a_4},\ -1,\
    -e^{-2a_4}b_4 W^2,\ -e^{-2a_4}b_4 W^2,\ -e^{-2a_4}b_4 W^2\big)$$

    in the order $x0, \dots, x7$, with the warp factor $W = (\sin^2 z)^{1/12}$, so that
    $W^2 = (\sin^2 z)^{1/6}$. When $a_4$ grows, lengths along $x1, x2, x3$ grow like
    $e^{a_4}$ (3-space **inflates**, with no dependence on $x_0$); lengths along the
    extra times $x5, x6, x7$ and along the hidden direction $x0$ change together with
    the hidden scale $s_b = e^{-a_4}b_4^{1/2}$ (they **deflate exponentially** while
    $a_4$ grows faster than $\ln b_4^{1/2}$). On the history of the Revision record,
    $a_4 = AHx_4$ and $b_4 = b_4(0)\,e^{\beta AHx_4}$ with $A = 1$, $\beta = 4/3$ and
    $b_4(0) = 1$, the hidden scale is $s_b = e^{-a_4/3}$ (a prescribed background, not a
    solution of field equations); every result below holds for every $a_4$ and $b_4$.

    **The diagonal vielbein.** Because $g$ is diagonal, the vielbein can be chosen
    diagonal: $e^a{}_\mu = f_a\,\delta^a_\mu$ with $\eta_{aa} f_a^2 = g_{aa}$:

    $$f = \big(s_b\cot z,\ e^{a_4},\ e^{a_4},\ e^{a_4},\ 1,\ s_b W,\ s_b W,\ s_b W\big),
    \qquad s_b = e^{-a_4} b_4^{1/2} .$$

    The hidden factor keeps the sign of $\cot z$ (it is negative on the second half of
    a cell), as in the Revision record; $f_0^2$ is all the metric needs.

    **Every real $z$ at once.** The only property of $W$ that the computation needs is
    its derivative, $\partial_{x0} W = H\cot z\,W$ wherever $\sin z \neq 0$ (the
    logarithm $\ln W = \frac{1}{12}\ln\sin^2 z$ has the derivative $\frac{1}{12}
    \cdot\frac{2\sin z\cos z}{\sin^2 z}\cdot 6H = H\cot z$). The notebook teaches sympy
    this one rule, so that every result holds for every real $z$ with
    $\sin z\cos z \neq 0$, with no case for the sign of $\sin z$.

    **The formulas used** (the standard ones of general relativity with spinors):

    $$\Gamma^\lambda{}_{\mu\nu} = \tfrac12 \sum_\rho g^{\lambda\rho}\big(\partial_\mu
    g_{\rho\nu} + \partial_\nu g_{\rho\mu} - \partial_\rho g_{\mu\nu}\big),$$

    $$\omega_\mu{}^a{}_b = \sum_\nu e^a{}_\nu \Big(\partial_\mu e_b{}^\nu +
    \sum_\lambda \Gamma^\nu{}_{\mu\lambda} e_b{}^\lambda\Big), \qquad
    \omega_{\mu ab} = \eta_{aa}\,\omega_\mu{}^a{}_b ,$$

    $$\Omega_\mu = \tfrac12 \sum_{a,b} \omega_{\mu ab} S^{ab}, \qquad D_\mu\Psi =
    \partial_\mu\Psi + \Omega_\mu\Psi, \qquad \gamma^\mu = \sum_a e_a{}^\mu\gamma^a .$$

    The formula for $\omega$ is the unique solution of the **vielbein postulate**
    $\partial_\mu e^a{}_\nu - \sum_\lambda \Gamma^\lambda{}_{\mu\nu} e^a{}_\lambda +
    \sum_b \omega_\mu{}^a{}_b e^b{}_\nu = 0$: the vielbein is constant for the full
    covariant derivative. The notebook checks this equation in all 512 components.

    **What is PROVED here (exact, sympy) and what it means.** In the diagonal vielbein,
    $\gamma^\mu\Omega_\mu = c_g\gamma^{(x0)} + v_g\gamma^{(x4)}$ for every $H > 0$,
    all functions $a_4(x_4)$ and $b_4(x_4) > 0$ and every real $z$ away from the
    degenerate points. This term appears in the field equation $\gamma^\mu D_\mu\Psi =
    (m + U'(S))\Psi$ of both fields. Its value belongs to the diagonal vielbein and to
    the field variable: the next notebook of this chapter (06b) shows that in a boosted
    vielbein its $c_g$ part vanishes while its $v_g$ part stays, and that a rescaling
    of the field removes all of it. What no choice can remove is the curvature of the
    metric, wherever the metric is curved (the corrected metric is curved on the
    history of the record and flat for the special member $a_4 = 0$,
    $b_4 = H^2x_4^2$).
    """),
    md(r"""
    ## 5. The tools: sympy and the author's gamma matrices

    The next cell imports numpy (numbers for the plots) and sympy (exact algebra),
    reads the author's eight gamma matrices from the Revision record
    `Revision/algebra/gammas.json`, and checks two of their properties: the 64
    Clifford relations, and that there are eight of them, each a 16 x 16 matrix whose
    entries are all real numbers. It then builds the 28 matrices $S^{ab} =
    \frac14[\gamma^a, \gamma^b]$.

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
    import numpy as np  # arrays of decimal numbers (only for the plots)
    import sympy as sp  # exact algebra and calculus with symbols

    GAMMA_FILE = "Revision/algebra/gammas.json"  # a Revision record (read only)
    fixture = json.loads(repository_file(GAMMA_FILE).read_text(encoding="utf-8"))
    NAMES = fixture["coordinates"]  # ["x0", ..., "x7"], the names of the directions
    ETA = fixture["eta"]  # the frame metric: +1 space-like, -1 time-like
    # Each gamma is stored as 16 rows of 16 whole numbers; sp.Matrix makes it an exact
    # sympy matrix.  gamma[a] is the gamma of the direction NAMES[a].
    gamma = [sp.Matrix(rows) for rows in fixture["gamma"]]
    I16 = sp.eye(16)  # the 16 x 16 identity matrix
    Z16 = sp.zeros(16, 16)  # the 16 x 16 zero matrix
    say(f"directions: {NAMES}")
    say(f"eta (frame metric): {ETA}")
    # The Clifford relation for all 8 x 8 = 64 pairs (a, b): the anticommutator is
    # 2 eta_aa times the identity when a = b and the zero matrix when a and b differ.
    clifford = all(gamma[a] * gamma[b] + gamma[b] * gamma[a]
                   == (2 * ETA[a] if a == b else 0) * I16
                   for a in range(8) for b in range(8))
    check(clifford, "the 64 Clifford relations of the author's gammas",
          record="Revision/theory/reports/python-field-theory.json, "
                 "check clifford_relations")
    # eight matrices, each with 16 rows and 16 columns, and every entry a real number
    check(len(gamma) == 8 and all(matrix.shape == (16, 16) for matrix in gamma)
          and all(entry.is_real for matrix in gamma for entry in matrix),
          "the eight gammas are 16 x 16 matrices with real entries",
          record="Revision/theory/reports/python-field-theory.json, check gammas_real")
    # S[a][b] = (1/4)(gamma^a gamma^b - gamma^b gamma^a), for all 64 pairs (a, b).
    S = [[(gamma[a] * gamma[b] - gamma[b] * gamma[a]) / 4 for b in range(8)]
         for a in range(8)]
    '''),
    md(r"""
    The next cell defines four small helpers that the rest of the notebook uses.

    - `is_zero(expr)` decides EXACTLY whether a sympy expression is zero for all values
      of its symbols. It first tries a fast route (write every sine and cosine through
      exponential functions, multiply out, cancel common factors) and then sympy's
      general `simplify`. It never says "zero" for an expression that is not zero; at
      worst it fails to recognise a zero, and then a check fails visibly.
    - `matrix_is_zero(M)` applies `is_zero` to every entry of a matrix.
    - `record_passed(path, name)` opens a Revision report (a JSON file) and returns
      True when the report records the check `name` as passed.
    - `record_formula(key, names)` reads a formula of a record, written in the notation
      of the Wolfram Language, and turns it into a sympy expression with sympy's reader
      `parse_mathematica`. The record read is `Revision/theory/field-theory.json`,
      written for the corrected metric. The record writes the roots of $\sin^2 z$ as
      `(Sin[6*H*x0]^2)^(1/12)` and in two other ways; the reader turns each of them
      into a power of one name, `warp`, which stands for $W$, and stops with an error
      if any other root is left, so that nothing is read wrongly in silence.
    """),
    code(r'''
    from sympy.parsing.mathematica import parse_mathematica  # reads Wolfram notation


    def is_zero(expr):
        """True when expr is exactly zero for all values of its symbols."""
        expr = sp.sympify(expr)
        if expr == 0:
            return True
        # Fast route: sin, cos, tan, ... written through exp, multiplied out, cancelled.
        if sp.cancel(sp.expand(expr.rewrite(sp.exp))) == 0:
            return True
        return sp.simplify(expr) == 0  # the slower general route


    def matrix_is_zero(matrix):
        """True when every entry of the matrix is exactly zero."""
        return all(is_zero(entry) for entry in matrix)


    def record_passed(path, name):
        """True when the Revision report at path records the check name as passed."""
        data = json.loads(repository_file(path).read_text(encoding="utf-8"))
        for entry in data["checks"]:
            if entry["name"] == name:
                return entry["verdict"].upper() == "PASS"  # "PASS" or "pass"
        raise KeyError(f"{path} has no check {name}")


    def read_formulas(path):
        """The formulas of a record as a dictionary key -> text (or list of texts)."""
        data = json.loads(repository_file(path).read_text(encoding="utf-8"))
        return {item["key"]: item["wl"] for item in data["formulas"]}


    THEORY_FILE = "Revision/theory/field-theory.json"  # the record, corrected metric
    FORMULAS = read_formulas(THEORY_FILE)
    # The roots of sin^2 z as the record writes them, and the same root as a power of
    # warp = W = (sin^2 z)^(1/12):  |sin z|^(1/3) = (sin^2 z)^(1/6) = W^2.
    ROOTS = (("(Sin[6*H*x0]^2)^(1/12)", "warp"), ("(Sin[6*H*x0]^2)^(1/6)", "warp^2"),
             ("(Sin[6*H*x0]^2)^(1/4)", "warp^3"), ("Abs[Sin[6*H*x0]]^(1/3)", "warp^2"))


    def wolfram_to_sympy(text, names):
        """A text in Wolfram notation as a sympy expression.  names maps the record's
        symbol names (texts) to the symbols and functions of this notebook."""
        # The roots first, then a4', a4'', a4(x4) and the same for b4, which the record
        # writes as Derivative[1][a4][x4], Derivative[2][a4][x4], a4[x4], ...
        for long_form, short_form in ROOTS + (("Derivative[1][a4][x4]", "a4p"),
                                              ("Derivative[2][a4][x4]", "a4pp"),
                                              ("Derivative[1][b4][x4]", "b4p"),
                                              ("Derivative[2][b4][x4]", "b4pp"),
                                              ("a4[x4]", "a4"), ("b4[x4]", "b4")):
            text = text.replace(long_form, short_form)
        if "Sin[6*H*x0]^2" in text or "Abs[" in text:  # a root that was not translated
            raise ValueError(f"cannot translate {text}")
        expr = parse_mathematica(text)
        return expr.subs({sp.Symbol(name): value for name, value in names.items()},
                         simultaneous=True)


    def record_formula(key, names):
        """The formula key of the record field-theory.json as a sympy expression."""
        return wolfram_to_sympy(FORMULAS[key], names)


    REPORT_PY = "Revision/theory/reports/python-field-theory.json"
    REPORT_WL = "Revision/theory/reports/wolfram-field-theory.json"
    REPORT_LEAD = "Revision/lead_checks/reports/emt-divergence-and-spin-connection.json"
    PARAMETERS = "Revision/kohn_sham/results/parameters.json"
    physics = json.loads(repository_file(PARAMETERS).read_text(encoding="utf-8"))["physics"]
    A_value, beta = physics["historyA"], physics["historyBeta"]  # the record's history
    b4_zero = physics["historyB4AtZero"]  # the value b4(0)
    A_EXACT, BETA = sp.nsimplify(A_value), sp.nsimplify(beta)  # 1 and 4/3 as fractions
    B4_ZERO = sp.nsimplify(b4_zero)  # b4(0) = 1 as an exact number
    say(f"{len(FORMULAS)} formulas read from {THEORY_FILE}")
    say(f"history of the record: slope A = {A_value}, beta = {beta:.6f}, b4(0) = "
        f"{b4_zero} (a4 = A H x4, b4 = b4(0) e^(beta A H x4))")
    check(A_EXACT == 1 and BETA == sp.Rational(4, 3) and B4_ZERO == 1,
          "the history of the record has A = 1, beta = 4/3 and b4(0) = 1",
          record=f"{PARAMETERS}, physics.historyA, historyBeta and historyB4AtZero")
    '''),
    md(r"""
    ## 6. Four general formulas as Python functions

    The next cell turns the formulas of Section 4 into four Python functions. They work
    in ANY number of dimensions and for ANY vielbein, so the same functions serve the
    two-dimensional warm-up and the author's eight-dimensional metric.

    - `christoffel(g, coords)`: the Christoffel symbols of the metric matrix `g`;
      `Gam[l][m][n]` is $\Gamma^l{}_{mn}$. Because $\Gamma^l{}_{mn} = \Gamma^l{}_{nm}$,
      each pair $(m, n)$ is computed once.
    - `spin_connection(e, Gam, coords, eta)`: the canonical spin connection with the
      first frame index lowered, `omega[mu][a][b]` $= \omega_{\mu ab}$. The vielbein is
      the matrix `e` with `e[a, mu]` $= e^a{}_\mu$ (row = frame index, column =
      coordinate index); its inverse matrix `E = e.inv()` has `E[mu, a]` $=
      e_a{}^\mu$, because $\sum_\mu e^a{}_\mu e_b{}^\mu = \delta^a_b$ says exactly
      `e * E = 1`.
    - `spinor_connection(omega, S)`: $\Omega_\mu = \frac12\sum_{a,b}\omega_{\mu ab}
      S^{ab}$. Since both $\omega_{\mu ab}$ and $S^{ab}$ change sign when $a$ and $b$
      are exchanged, the terms $(a, b)$ and $(b, a)$ are equal, and the factor
      $\frac12$ is used up by summing over $a < b$ only.
    - `curved_gammas(e, gammas)`: $\gamma^\mu = \sum_a e_a{}^\mu \gamma^a$.

    Every nonzero result is simplified with sympy's `simplify`, so that it prints in a
    short form.
    """),
    code(r'''
    def christoffel(g, coords):
        """Gam[l][m][n] = (1/2) sum_r g^lr (d_m g_rn + d_n g_rm - d_r g_mn)."""
        n = len(coords)
        g_inv = g.inv()  # the inverse metric g^lr
        Gam = [[[sp.Integer(0)] * n for _ in range(n)] for _ in range(n)]
        for l in range(n):
            for m in range(n):
                for k in range(m, n):  # Gamma^l_mk = Gamma^l_km: compute it once
                    value = sum(g_inv[l, r] * (sp.diff(g[r, k], coords[m])
                                               + sp.diff(g[r, m], coords[k])
                                               - sp.diff(g[m, k], coords[r]))
                                for r in range(n) if g_inv[l, r] != 0) / 2
                    value = sp.simplify(value)
                    Gam[l][m][k] = value
                    Gam[l][k][m] = value
        return Gam


    def spin_connection(e, Gam, coords, eta):
        """omega[mu][a][b] = omega_{mu ab} = eta_aa omega_mu^a_b, where
        omega_mu^a_b = sum_nu e^a_nu (d_mu e_b^nu + sum_lam Gam^nu_{mu lam} e_b^lam)."""
        n = len(coords)
        E = e.inv()  # E[nu, b] = e_b^nu, the inverse vielbein
        omega = [[[sp.Integer(0)] * n for _ in range(n)] for _ in range(n)]
        for mu in range(n):
            for a in range(n):
                for b in range(n):
                    mixed = 0  # will become omega_mu^a_b
                    for nu in range(n):
                        if e[a, nu] == 0:
                            continue  # this term is zero
                        inner = sp.diff(E[nu, b], coords[mu]) + sum(
                            Gam[nu][mu][lam] * E[lam, b] for lam in range(n))
                        mixed += e[a, nu] * inner
                    omega[mu][a][b] = sp.simplify(eta[a] * mixed)  # lower the index a
        return omega


    def spinor_connection(omega, S):
        """Omega[mu] = (1/2) sum_{a,b} omega_{mu ab} S^ab = sum_{a<b} omega_{mu ab} S^ab."""
        n = len(omega)
        size = S[0][0].shape[0]  # 16 for the author's gammas, 2 in two dimensions
        Omega = []
        for mu in range(n):
            total = sp.zeros(size, size)
            for a in range(n):
                for b in range(a + 1, n):
                    if omega[mu][a][b] != 0:
                        total += omega[mu][a][b] * S[a][b]
            Omega.append(total)
        return Omega


    def curved_gammas(e, gammas):
        """gamma^mu = sum_a e_a^mu gamma^a for every coordinate mu."""
        E = e.inv()
        n = len(gammas)
        return [sum((E[mu, a] * gammas[a] for a in range(n)),
                    sp.zeros(*gammas[0].shape)) for mu in range(n)]


    say("defined: christoffel, spin_connection, spinor_connection, curved_gammas")
    '''),
    md(r"""
    ## 7. A warm-up in two dimensions: the flat plane in polar coordinates

    Before eight dimensions, two. A point of the flat plane has the polar coordinates
    $r$ (distance from the centre) and $\varphi$ (angle). The metric is
    $ds^2 = dr^2 + r^2 d\varphi^2$, so $g = \mathrm{diag}(1, r^2)$ and $\eta =
    \mathrm{diag}(1, 1)$. The unit directions are the radial direction (frame index 0)
    and the angular direction (frame index 1); a step $d\varphi$ has the length
    $r\,d\varphi$, so the vielbein is $e = \mathrm{diag}(1, r)$. Two 2 x 2 matrices with
    the Clifford relation of the plane are the Pauli matrices $\sigma_1$ and
    $\sigma_2$, so $\gamma^0 = \sigma_1$ and $\gamma^1 = \sigma_2$.

    The next cell computes everything with the general functions and checks the
    results that can be worked by hand:
    $\Gamma^r{}_{\varphi\varphi} = -r$, $\Gamma^\varphi{}_{r\varphi} = 1/r$;
    $\omega_{\varphi 01} = -1$ (the frame turns by one radian per radian of
    $\varphi$); $\Omega_\varphi = -\frac{i}{2}\sigma_3$; and
    $\gamma^\mu\Omega_\mu = \sigma_1/(2r)$, so that the Dirac operator of the plane in
    polar coordinates is $\sigma_1(\partial_r + \frac{1}{2r}) + \frac{\sigma_2}{r}
    \partial_\varphi$. The plane is flat, so the curvature of the spinor connection,
    $F_{r\varphi} = \partial_r\Omega_\varphi - \partial_\varphi\Omega_r +
    [\Omega_r, \Omega_\varphi]$, must vanish; the cell checks that too. A change of
    frame by a spin transformation $R(\varphi)$ changes the spinor connection into
    $R\,\Omega_\varphi R^{-1} - (\partial_\varphi R)R^{-1}$. The Cartesian frame has
    no connection, and the cell checks that $\Omega_\varphi = -(\partial_\varphi
    U)U^{-1}$ for the spinor rotation $U(\varphi) = \cos\frac{\varphi}{2} +
    i\sin\frac{\varphi}{2}\,\sigma_3$: this is the rule with $R = U$ applied to the
    connection 0 of the Cartesian frame, so $U$ carries the Cartesian frame into the
    polar frame. Finally it checks that the inverse rotation $U^{-1}$ removes the
    connection: the rule with $R = U^{-1}$ gives $U^{-1}\Omega_\varphi U -
    (\partial_\varphi U^{-1})U = 0$. In a flat space the spin connection is only the
    turning of the chosen frame.
    """),
    code(r'''
    r, phi = sp.symbols("r phi", positive=True)  # polar coordinates, r > 0
    sigma1 = sp.Matrix([[0, 1], [1, 0]])  # the three Pauli matrices
    sigma2 = sp.Matrix([[0, -sp.I], [sp.I, 0]])
    sigma3 = sp.Matrix([[1, 0], [0, -1]])
    plane_gammas = [sigma1, sigma2]  # gamma^0 (radial), gamma^1 (angular)
    plane_eta = [1, 1]
    plane_S = [[(plane_gammas[a] * plane_gammas[b] - plane_gammas[b] * plane_gammas[a])
                / 4 for b in range(2)] for a in range(2)]
    plane_g = sp.diag(1, r**2)  # ds^2 = dr^2 + r^2 dphi^2
    plane_e = sp.diag(1, r)  # e^a_mu: unit radial and unit angular direction

    plane_Gam = christoffel(plane_g, [r, phi])
    plane_omega = spin_connection(plane_e, plane_Gam, [r, phi], plane_eta)
    plane_Omega = spinor_connection(plane_omega, plane_S)
    plane_gup = curved_gammas(plane_e, plane_gammas)
    plane_slash = sp.simplify(plane_gup[0] * plane_Omega[0] + plane_gup[1] * plane_Omega[1])
    say(f"Gamma^r_phiphi = {plane_Gam[0][1][1]},  Gamma^phi_rphi = {plane_Gam[1][0][1]}")
    say(f"omega_phi01 = {plane_omega[1][0][1]},  omega_phi10 = {plane_omega[1][1][0]}")
    say(f"Omega_phi = {plane_Omega[1].tolist()}")
    say(f"gamma^mu Omega_mu = {plane_slash.tolist()}")
    check(plane_Gam[0][1][1] == -r and plane_Gam[1][0][1] == 1 / r,
          "polar plane: Gamma^r_phiphi = -r and Gamma^phi_rphi = 1/r")
    check(plane_omega[1][0][1] == -1 and plane_omega[1][1][0] == 1
          and plane_omega[0][0][1] == 0, "polar plane: omega_phi01 = -1, omega_r = 0")
    check(plane_Omega[1] == -sp.I / 2 * sigma3 and plane_Omega[0] == sp.zeros(2, 2),
          "polar plane: Omega_phi = -(i/2) sigma3 and Omega_r = 0")
    check(plane_slash == sigma1 / (2 * r), "polar plane: gamma^mu Omega_mu = sigma1/(2 r)")
    F_rphi = (plane_Omega[1].diff(r) - plane_Omega[0].diff(phi)
              + plane_Omega[0] * plane_Omega[1] - plane_Omega[1] * plane_Omega[0])
    U = sp.cos(phi / 2) * sp.eye(2) + sp.I * sp.sin(phi / 2) * sigma3  # spinor rotation
    pure_gauge = -U.diff(phi) * U.inv() - plane_Omega[1]  # must be the zero matrix
    removed = U.inv() * plane_Omega[1] * U - U.inv().diff(phi) * U  # frame change U^-1
    check(F_rphi == sp.zeros(2, 2) and matrix_is_zero(pure_gauge)
          and matrix_is_zero(removed),
          "polar plane: flat (F_rphi = 0), Omega_phi = -(dU/dphi) U^-1, U^-1 removes it")
    '''),
    md(r"""
    The next cell draws two pictures of the warm-up. On the left, the unit radial
    direction (black arrows) and the unit angular direction (orange arrows) at twelve
    angles on two circles: the frame turns as one goes around, by exactly the angle
    $\varphi$, which is why $\omega_{\varphi 01} = -1$ (one radian of frame rotation per
    radian of $\varphi$; the sign records the sense of rotation). On the right, the
    real part and the imaginary part of the entry $U_{11} = \cos\frac\varphi2 +
    i\sin\frac\varphi2$ of the spinor rotation $U(\varphi)$ that carries the Cartesian
    frame into the polar frame (its inverse $U^{-1}$ removes the connection), for
    $\varphi$ from $0$ to $4\pi$: after one full turn ($\varphi = 2\pi$) $U = -1$, and
    only after two full turns is $U = +1$ again. A spinor turns by half the angle of the
    frame; this is the "double cover" of rotations by spinor transformations.
    """),
    code(r'''
    fig, (ax_left, ax_right) = plt.subplots(1, 2, figsize=(10.0, 4.6))
    angles = np.arange(12) * np.pi / 6  # 12 angles, 30 degrees apart
    for radius in (1.0, 2.0):
        px, py = radius * np.cos(angles), radius * np.sin(angles)  # the points
        ax_left.quiver(px, py, np.cos(angles), np.sin(angles), color="black",
                       angles="xy", scale_units="xy", scale=3.0, width=0.006)
        ax_left.quiver(px, py, -np.sin(angles), np.cos(angles), color="tab:orange",
                       angles="xy", scale_units="xy", scale=3.0, width=0.006)
        circle = np.linspace(0.0, 2.0 * np.pi, 200)
        ax_left.plot(radius * np.cos(circle), radius * np.sin(circle), ":",
                     color="gray", linewidth=1.0)
    ax_left.plot([], [], color="black", label="unit radial direction $e_{(0)}$")
    ax_left.plot([], [], color="tab:orange", label="unit angular direction $e_{(1)}$")
    ax_left.set_aspect("equal")
    ax_left.set_xlim(-2.8, 2.8)
    ax_left.set_ylim(-2.8, 3.6)  # room for the legend above the circles
    ax_left.set_xlabel("Cartesian $x = r\\cos\\varphi$")
    ax_left.set_ylabel("Cartesian $y = r\\sin\\varphi$")
    ax_left.set_title("The polar frame turns with the angle")
    ax_left.legend(loc="upper left", fontsize=8)
    turn = np.linspace(0.0, 4.0 * np.pi, 400)  # phi from 0 to 4 pi
    ax_right.plot(turn / np.pi, np.cos(turn / 2), label="$\\cos(\\varphi/2)$, real part")
    ax_right.plot(turn / np.pi, np.sin(turn / 2), "--",
                  label="$\\sin(\\varphi/2)$, imaginary part")
    ax_right.set_xlabel("$\\varphi / \\pi$")
    ax_right.set_ylabel("entry $U_{11}$ of the spinor rotation")
    ax_right.set_ylim(-1.45, 1.2)  # room for the legend below the curves
    ax_right.set_title("A spinor turns by half the angle")
    ax_right.legend(loc="lower center", ncol=2, fontsize=8)
    save_figure(fig, "polar_frame_and_spin_rotation",
                "Warm-up in the flat plane. Left: the unit radial direction (black) and "
                "the unit angular direction (orange) of the polar frame at twelve angles "
                "on the circles $r = 1$ and $r = 2$, drawn in Cartesian coordinates $x$, "
                "$y$ (pure numbers); the frame turns by the angle $\\varphi$ as one goes "
                "around, and the spin connection $\\omega_{\\varphi 01} = -1$ records "
                "this rate. Right: the entry $U_{11} = \\cos(\\varphi/2) + "
                "i\\sin(\\varphi/2)$ of the spinor rotation $U$ that carries the "
                "Cartesian frame into the polar frame (its inverse $U^{-1}$ removes the "
                "connection), real part (solid) and imaginary part (dashed), for "
                "$\\varphi$ from $0$ to $4\\pi$; at $\\varphi = 2\\pi$ the spinor "
                "rotation is $-1$, and only at $4\\pi$ is it $+1$ again.")
    '''),
    md(r"""
    ## 8. The corrected metric and its diagonal vielbein

    The next cell makes the symbols of the metric: the coordinates $x0, \dots, x7$
    (real), the constant $H > 0$, the two functions $a_4(x_4)$ and $b_4(x_4) > 0$
    (unknown functions: every result below holds for EVERY $a_4$ and $b_4$), and
    $z = 6Hx_0$. The warp factor is a sympy **function class** `W` with one rule of its
    own: the method `fdiff` tells sympy that the derivative of `W(x0)` is
    `H*cot(6*H*x0)*W(x0)`, and the method `_eval_is_positive` that $W > 0$. The symbol
    `G` is the sign of $\cot z$ ($+1$ on the first half of a cell, $-1$ on the second);
    it appears only in $\sqrt{|\det g|} = G f_0 f_1\cdots f_7$. The cell first checks
    the rule of `W` against the explicit function $(\sin^2 z)^{1/12}$, whose derivative
    sympy computes itself. Then it writes the eight factors $f_a$ of the diagonal
    vielbein and checks three things: that $\eta_{aa} f_a^2 = g_{aa}$ reproduces the
    corrected metric as recorded in `Revision/theory/field-theory.json` (formula
    `metric`); that the factors are the record's `vielbein_diagonal`; and that
    $\sqrt{|\det g|} = G f_0 f_1\cdots f_7 = e^{-a_4}b_4^2|\cot z|(\sin^2 z)^{1/4}$
    (formula `sqrt_det_g`). The last fact has a meaning: 3-space gives $e^{3a_4}$, the
    four directions of the hidden block give $e^{-4a_4}b_4^2$, so the 7-volume of a
    slice changes with the time like $e^{-a_4}b_4^2$ (on the history of the record like
    $e^{5a_4/3}$).
    """),
    code(r'''
    x = sp.symbols("x0:8", real=True)  # x[0] = x0, ..., x[4] = x4, ..., x[7] = x7
    x0, x4 = x[0], x[4]  # the hidden direction and the time
    H = sp.Symbol("H", positive=True)  # the author's constant H > 0
    a4 = sp.Function("a4")(x4)  # the metric function a4(x4): any function of the time
    b4 = sp.Function("b4", positive=True)(x4)  # the metric function b4(x4) > 0
    z = 6 * H * x0  # the hidden coordinate z = 6 H x0, every real value


    class W(sp.Function):
        """The warp factor W(x0) = (sin(6 H x0)^2)^(1/12) > 0 of the extra times."""

        def fdiff(self, argindex=1):
            """dW/dx0 = H cot(6 H x0) W, for every real z = 6 H x0 with sin z != 0."""
            return H * sp.cot(6 * H * self.args[0]) * self

        def _eval_is_positive(self):
            return True  # the positive root


    G = sp.Symbol("G", real=True)  # the sign of cot z (+1 or -1): |cot z| = G cot z
    explicit = (sp.sin(z) ** 2) ** sp.Rational(1, 12)  # the twelfth root, written out
    check(is_zero(sp.diff(explicit, x0) - H * sp.cot(z) * explicit),
          "the derivative of (sin^2 z)^(1/12) is H cot z (sin^2 z)^(1/12): the rule of W")
    s_b = sp.exp(-a4) * sp.sqrt(b4)  # the hidden scale e^(-a4) b4^(1/2)
    f = ([s_b * sp.cot(z)] + [sp.exp(a4)] * 3 + [sp.Integer(1)]
         + [s_b * W(x0)] * 3)  # f_0, ..., f_7
    g = sp.diag(*[ETA[a] * f[a] ** 2 for a in range(8)])  # g_aa = eta_aa f_a^2
    e = sp.diag(*f)  # the diagonal vielbein e^a_mu = f_a delta^a_mu
    # The names under which the records write symbols, and our symbols for them:
    RECORD_NAMES = {"H": H, "x4": x4, "x0": x0, "a4": a4, "b4": b4, "warp": W(x0),
                    "rftSig": G, "a4p": sp.Derivative(a4, x4),
                    "a4pp": sp.Derivative(a4, (x4, 2)), "b4p": sp.Derivative(b4, x4),
                    "b4pp": sp.Derivative(b4, (x4, 2))}
    metric_record = sp.Matrix([list(row) for row in record_formula("metric", RECORD_NAMES)])
    check(matrix_is_zero(g - metric_record)
          and record_passed(REPORT_WL, "metric_is_the_corrected_metric")
          and record_passed(REPORT_PY, "metric_from_vielbein_equals_SPEC"),
          "eta_aa f_a^2 is the corrected metric (all 64 entries)",
          record=f"{THEORY_FILE}, formula metric")
    f_record = record_formula("vielbein_diagonal", RECORD_NAMES)
    check(all(is_zero(f[a] - f_record[a]) for a in range(8))
          and record_passed(REPORT_LEAD, "vielbein_reproduces_metric"),
          "the eight vielbein factors of the record",
          record=f"{THEORY_FILE}, formula vielbein_diagonal")
    volume = sp.simplify(sp.prod(f))  # f_0 f_1 ... f_7, with the sign of cot z
    say(f"f_0 f_1 ... f_7 = {volume}")
    volume_record = record_formula("sqrt_det_g", RECORD_NAMES)
    check(is_zero(G * volume - volume_record) and is_zero(volume**2 - g.det())
          and record_passed(REPORT_WL, "sqrt_det_g")
          and record_passed(REPORT_PY, "sqrt_det_g"),
          "sqrt|det g| = G f_0 f_1 ... f_7 = e^(-a4) b4^2 |cot z| (sin^2 z)^(1/4)",
          record=f"{THEORY_FILE}, formula sqrt_det_g")
    '''),
    md(r"""
    The next cell draws the vielbein factors. The left panel shows how they depend on
    the time $x4$ at the fixed hidden angle $z = \pi/4$, on the history of the record,
    $a_4 = x_4$ and $b_4 = e^{\beta x_4}$ with $\beta = 4/3$ in units in which $H = 1$
    (an illustration only: the results of this notebook hold for every $a_4$ and
    $b_4$). On a logarithmic vertical axis the exponential factors are straight lines:
    the 3-space factor $e^{a_4}$ rises; the hidden factor $s_b\cot z = e^{-x_4/3}$ and
    the extra-time factor $s_b W = e^{-x_4/3}W$ fall at one third of that rate, side by
    side; and the volume factor $\sqrt{|\det g|} = e^{-a_4}b_4^2|\cot z|W^3$ rises like
    $e^{5x_4/3}$. To draw a function numerically the cell replaces `W(x0)` by the
    explicit $|\sin z|^{1/6}$ (the same number). The right panel shows the dependence
    on $z$ across one cell $0 < z < \pi$: the warp factor $W$, the hidden factor
    $|\cot z|$ (divided by $s_b$) and the volume factor divided by $e^{-a_4}b_4^2$, both
    of which vanish at the fold $z = \pi/2$.
    """),
    code(r'''
    X4_SYMBOL = sp.Symbol("t", real=True)  # the time x4 as a plain symbol for numbers
    history = {a4: A_EXACT * X4_SYMBOL,  # the record's history with H = 1, b4(0) = 1
               b4: B4_ZERO * sp.exp(BETA * A_EXACT * X4_SYMBOL)}


    def explicit_warp(expr):
        """expr with W(x0) replaced by the explicit |sin z|^(1/6) (for numbers)."""
        return sp.sympify(expr).subs(W(x0), sp.Abs(sp.sin(z)) ** sp.Rational(1, 6))


    # the eight factors and the volume factor (positive at z = pi/4) at z = 6 x0 = pi/4
    f_of_time = sp.lambdify(X4_SYMBOL, [explicit_warp(fa.subs(history)).subs(
        {H: 1, x0: sp.pi / 24}) for fa in f + [volume]])
    times = np.linspace(-2.0, 2.0, 201)
    values = [np.broadcast_to(v, times.shape) for v in f_of_time(times)]
    fig, (ax_left, ax_right) = plt.subplots(1, 2, figsize=(10.0, 4.4))
    ax_left.semilogy(times, values[1], label="$f_1 = f_2 = f_3 = e^{a_4}$ (3-space)")
    ax_left.semilogy(times, values[0], "--", label="$f_0 = s_b\\cot z$ (hidden)")
    ax_left.semilogy(times, values[5], "-.",
                     label="$f_5 = f_6 = f_7 = s_bW$ (extra times)")
    ax_left.semilogy(times, values[4], ":", color="black", label="$f_4 = 1$ (time)")
    ax_left.semilogy(times, values[8], color="gray", linewidth=2.5, alpha=0.6,
                     label="$\\sqrt{|\\det g|}$ (7-volume factor)")
    ax_left.set_xlabel("time $x_4$ (units $1/H$), history $a_4 = x_4$, "
                       "$b_4 = e^{4x_4/3}$")
    ax_left.set_ylabel("factor at $z = \\pi/4$ (logarithmic axis)")
    ax_left.set_title("Inflating 3-space, deflating hidden block")
    ax_left.legend(fontsize=7)
    zz = np.linspace(0.02, np.pi - 0.02, 400)  # z inside one cell (0, pi)
    ax_right.plot(zz, np.abs(np.sin(zz)) ** (1 / 6), label="$W = (\\sin^2 z)^{1/12}$")
    ax_right.plot(zz, np.abs(1 / np.tan(zz)), "--", label="$|f_0|/s_b = |\\cot z|$")
    ax_right.plot(zz, np.abs(1 / np.tan(zz)) * np.abs(np.sin(zz)) ** 0.5, ":",
                  color="black", label="$\\sqrt{|\\det g|}/(e^{-a_4}b_4^2)$")
    ax_right.axvline(np.pi / 2, color="gray", linewidth=0.8)  # the fold
    ax_right.set_ylim(0.0, 3.0)
    ax_right.set_xlabel("hidden angle $z = 6 H x_0$ (radians), fold at $\\pi/2$")
    ax_right.set_ylabel("factor (pure number)")
    ax_right.set_title("Dependence on the hidden direction")
    ax_right.legend(fontsize=8, loc="upper center")
    save_figure(fig, "vielbein_factors",
                "The factors $f_a$ of the diagonal vielbein of the corrected metric. "
                "Left: versus the time $x_4$ in units $1/H$ at $z = \\pi/4$, on the "
                "history of the Revision record $a_4 = x_4$, $b_4 = e^{4x_4/3}$, on a "
                "logarithmic axis; the 3-space factor $e^{a_4}$ grows, the hidden factor "
                "$s_b\\cot z = e^{-x_4/3}$ and the extra-time factor $s_bW$ shrink side "
                "by side at one third of that exponential rate, the time factor is "
                "$1$, and the 7-volume factor $e^{-a_4}b_4^2|\\cot z|W^3$ grows like "
                "$e^{5x_4/3}$. Right: versus the hidden angle $z = 6Hx_0$ in radians "
                "across one cell; the warp factor $W = (\\sin^2 z)^{1/12}$, the hidden "
                "factor $|\\cot z|$ and the volume factor divided by $e^{-a_4}b_4^2$, "
                "which both vanish at the fold $z = \\pi/2$ (vertical line).")
    '''),
    md(r"""
    ## 9. The Christoffel symbols of the corrected metric

    The next cell computes all Christoffel symbols with the general function, counts
    the independent nonzero ones (those with $m \le n$; the record counts 21) and
    compares each of them with the list `christoffel_nonzero` of the record. In this
    list an entry $\{l, m, n, \text{value}\}$ means $\Gamma^{l}{}_{mn} = $ value, with
    the directions numbered from 1 in the order $x0, \dots, x7$ (the number 1 is $x0$,
    5 is $x4$); Python counts from 0, so 1 is subtracted. The cell prints seven
    symbols. Three of them show the rates: $\Gamma^{x1}{}_{x1\,x4} = a_4'$ (moving
    forward in time a 3-space direction grows at the rate $a_4'$), and
    $\Gamma^{x5}{}_{x4\,x5} = \Gamma^{x0}{}_{x0\,x4} = -a_4' + b_4'/(2b_4) = h_4$ (an
    extra time and the hidden direction change at the same rate $h_4$; on the history
    of the record $h_4 = -a_4'/3$). One shows the warp: $\Gamma^{x5}{}_{x0\,x5} =
    H\cot z$.
    """),
    code(r'''
    Gam = christoffel(g, x)
    independent = {(l, m, n): Gam[l][m][n] for l in range(8) for m in range(8)
                   for n in range(m, 8) if Gam[l][m][n] != 0}
    report("number of independent nonzero Christoffel symbols", len(independent))


    def as_dictionary(entries):
        """{l, m, n, value} entries of a record (numbered from 1) -> {(l, m, n): value}
        with Python's numbers 0 to 7."""
        return {(int(l) - 1, int(m) - 1, int(n) - 1): value for l, m, n, value in entries}


    record_gamma = as_dictionary(record_formula("christoffel_nonzero", RECORD_NAMES))
    same = set(record_gamma) == set(independent) and all(
        is_zero(independent[key] - record_gamma[key]) for key in independent)
    for key in [(1, 1, 4), (5, 4, 5), (0, 0, 4), (5, 0, 5), (4, 5, 5), (0, 5, 5),
                (0, 0, 0)]:
        l, m, n = key
        say(f"Gamma^{NAMES[l]}_{NAMES[m]}{NAMES[n]} = {independent[key]}")
    check(len(independent) == 21 and same and record_passed(REPORT_WL, "christoffel_count"),
          "the 21 independent nonzero Christoffel symbols equal the record",
          record=f"{THEORY_FILE}, formula christoffel_nonzero")
    '''),
    md(r"""
    The next cell draws where the nonzero Christoffel symbols sit. There is one small
    8 x 8 grid for each upper index $l = x0, \dots, x7$; the square in row $m$ and
    column $n$ is coloured by the sign of $\Gamma^l{}_{mn}$ at the sample point
    $H = 1$, $z = \pi/4$, $a_4 = 1/2$, $a_4' = 1$, $b_4 = e^{2/3}$, $b_4'/b_4 = 4/3$
    (the point $a_4 = 1/2$ of the history of the record; red positive, blue negative,
    white zero). The pattern shows the structure of the metric: only the hidden
    direction $x0$ and the time $x4$ appear as the "derivative" index, because the
    metric depends on $x_0$ and $x_4$ only; and the 3-space directions never pair with
    $x0$, because 3-space has no warp.
    """),
    code(r'''
    SAMPLE = {H: 1, x0: sp.pi / 24}  # H = 1 and z = 6 H x0 = pi/4
    B4_SAMPLE = sp.exp(sp.Rational(2, 3))  # b4 at a4 = 1/2 on the history, b4(0) = 1


    def at_sample(expr):
        """The decimal value of expr at the sample point H = 1, z = pi/4 on the history
        of the record: a4 = 1/2, a4' = 1, a4'' = 0, b4 = e^(2/3), b4' = (4/3) b4,
        b4'' = (16/9) b4 (derivatives are replaced first, then the functions)."""
        expr = sp.sympify(expr)
        rate = sp.Rational(4, 3)  # b4'/b4 = beta a4'
        for function, second, first in ((a4, 0, 1),
                                         (b4, rate**2 * B4_SAMPLE, rate * B4_SAMPLE)):
            expr = expr.subs(sp.Derivative(function, (x4, 2)), second)
            expr = expr.subs(sp.Derivative(function, x4), first)
        expr = explicit_warp(expr.subs({a4: sp.Rational(1, 2), b4: B4_SAMPLE}))
        return complex(sp.N(expr.subs(SAMPLE)))


    fig, axes = plt.subplots(2, 4, figsize=(10.0, 5.6))
    for l, ax in enumerate(axes.flat):
        signs = np.array([[np.sign(at_sample(Gam[l][m][n]).real) for n in range(8)]
                          for m in range(8)])
        ax.imshow(signs, cmap="RdBu_r", vmin=-1.5, vmax=1.5)
        ax.set_title(f"$\\Gamma^{{x{l}}}{{}}_{{mn}}$", fontsize=9)
        ax.set_xticks(range(8), [f"{k}" for k in range(8)], fontsize=7)
        ax.set_yticks(range(8), [f"{k}" for k in range(8)], fontsize=7)
        ax.set_xlabel("$n$ (x-number)", fontsize=7)
        ax.set_ylabel("$m$ (x-number)", fontsize=7)
        ax.grid(False)
    fig.suptitle("Signs of the Christoffel symbols at a sample point "
                 "(red +, blue -, white 0)", fontsize=10)
    fig.tight_layout()
    save_figure(fig, "christoffel_pattern",
                "Where the Christoffel symbols $\\Gamma^l{}_{mn}$ of the corrected metric "
                "are nonzero: one 8 x 8 grid per upper index $l = x0, \\dots, x7$, rows "
                "$m$ and columns $n$ numbered 0 to 7 for $x0$ to $x7$, each square "
                "coloured by the sign of the symbol at the sample point $H = 1$, $z = "
                "\\pi/4$, $a_4 = 1/2$, $a_4' = 1$, $b_4 = e^{2/3}$, $b_4'/b_4 = 4/3$ "
                "(on the history of the Revision record; red "
                "positive, blue negative, white zero). Every nonzero symbol has an index "
                "equal to 0 or 4: the metric depends only on the hidden coordinate $x_0$ "
                "and on the time $x_4$; the 3-space directions 1, 2, 3 meet only the "
                "time. The grids are symmetric because "
                "$\\Gamma^l{}_{mn} = \\Gamma^l{}_{nm}$.")
    '''),
    md(r"""
    ## 10. The canonical spin connection

    The next cell computes $\omega_{\mu ab}$ with the general function and checks:

    1. the vielbein postulate $\partial_\mu e^a{}_\nu - \sum_\lambda
       \Gamma^\lambda{}_{\mu\nu}e^a{}_\lambda + \sum_b \omega_\mu{}^a{}_b e^b{}_\nu = 0$
       in all $8 \cdot 8 \cdot 8 = 512$ components (here $\omega_\mu{}^a{}_b =
       \eta_{aa}\omega_{\mu ab}$, because $\eta_{aa}^2 = 1$);
    2. the antisymmetry $\omega_{\mu ab} = -\omega_{\mu ba}$ (all 512 triples);
    3. that exactly 10 components with $a < b$ are nonzero and equal the list
       `omega_nonzero` (entries $\{\mu, a, b, \text{value}\}$, numbered from 1 as for
       the Christoffel symbols) of the record;
    4. that every nonzero component is a rate times a factor that never vanishes
       between the degenerate points: the rate is $a_4'$ (3-space), $h_4 =
       b_4'/(2b_4) - a_4'$ (the hidden direction and the extra times) or $H$ (the warp
       of the extra times), and the factor is $e^{a_4}$, $s_b\cot z$, $s_bW$ or $W$.
       So the part of the spin connection made by the time dependence vanishes only if
       $a_4$ and $b_4$ are constant, and the part made by the hidden coordinate never
       vanishes for $H > 0$.
    """),
    code(r'''
    omega = spin_connection(e, Gam, x, ETA)
    postulate = [sp.diff(e[a, nu], x[mu])
                 - sum(Gam[lam][mu][nu] * e[a, lam] for lam in range(8))
                 + sum(ETA[a] * omega[mu][a][b] * e[b, nu] for b in range(8))
                 for mu in range(8) for a in range(8) for nu in range(8)]
    check(len(postulate) == 512 and all(is_zero(v) for v in postulate),
          "the vielbein postulate holds in all 512 components",
          record=f"{REPORT_PY}, check vielbein_postulate")
    check(all(is_zero(omega[mu][a][b] + omega[mu][b][a])
              for mu in range(8) for a in range(8) for b in range(8)),
          "omega_mu ab = -omega_mu ba for all mu, a, b",
          record=f"{REPORT_PY}, check spin_connection_antisymmetric")
    omega_nonzero = {(mu, a, b): omega[mu][a][b] for mu in range(8) for a in range(8)
                     for b in range(a + 1, 8) if omega[mu][a][b] != 0}
    for (mu, a, b), value in omega_nonzero.items():
        say(f"omega_{NAMES[mu]},{NAMES[a]}{NAMES[b]} = {value}")
    omega_record = as_dictionary(record_formula("omega_nonzero", RECORD_NAMES))
    check(len(omega_nonzero) == 10 and set(omega_record) == set(omega_nonzero)
          and all(is_zero(omega_nonzero[k] - omega_record[k]) for k in omega_nonzero),
          "the 10 independent nonzero omega_mu ab equal the record",
          record=f"{THEORY_FILE}, formula omega_nonzero")
    a4p, b4p = sp.Derivative(a4, x4), sp.Derivative(b4, x4)
    h4 = b4p / (2 * b4) - a4p  # the rate of the hidden scale s_b
    rates = (a4p, h4, H)  # 3-space, the hidden block, the warp
    factors = [sign * phys for sign in (1, -1)
               for phys in (sp.exp(a4), s_b * sp.cot(z), s_b * W(x0), W(x0))]
    # value / (rate * factor) must simplify to exactly 1 for one choice of each.
    shape_ok = all(any(sp.simplify(value / (rate * phys)) == 1 for rate in rates
                       for phys in factors) for value in omega_nonzero.values())
    check(shape_ok and record_passed(REPORT_WL, "omega_components")
          and record_passed(REPORT_WL, "Omega_vanishes_iff_a4prime_b4prime_and_H_vanish"),
          "every nonzero omega is a4', h4 or H times +-e^(a4), s_b cot z, s_b W or W",
          record=f"{REPORT_WL}, checks omega_components and "
                 "Omega_vanishes_iff_a4prime_b4prime_and_H_vanish")
    '''),
    md(r"""
    The next cell draws three of the eight 8 x 8 arrays $\omega_{\mu ab}$ at the sample
    point: for $\mu = x0$ (the hidden direction), $\mu = x1$ (an inflating 3-space
    direction) and $\mu = x5$ (a deflating extra time). Each array is antisymmetric: the
    square $(a, b)$ has the opposite colour of the square $(b, a)$, and the diagonal is
    white. For $\mu = x0$ the hidden frame direction turns towards the time (rate
    $h_4 s_b\cot z$, negative at the sample point, where $h_4 = 2/3 - 1 = -1/3$); for
    $\mu = x1$ the frame direction $x1$ turns towards the time $x4$ (rate
    $a_4'e^{a_4}$) and towards nothing else; for $\mu = x5$ the extra time turns towards
    the time (rate $h_4 s_bW$) and towards the hidden direction (rate $HW$).
    """),
    code(r'''
    fig, axes = plt.subplots(1, 3, figsize=(12.0, 4.0))
    for ax, mu in zip(axes, (0, 1, 5)):  # the directions x0, x1 and x5
        table = np.array([[at_sample(omega[mu][a][b]).real for b in range(8)]
                          for a in range(8)])
        limit = np.abs(table).max()
        image = ax.imshow(table, cmap="RdBu_r", vmin=-limit, vmax=limit)
        for a in range(8):
            for b in range(8):
                if table[a, b] != 0:  # white digits on the dark squares
                    dark = abs(table[a, b]) > 0.6 * limit
                    ax.text(b, a, f"{table[a, b]:.2f}", ha="center", va="center",
                            fontsize=6, color="white" if dark else "black")
        ax.set_xticks(range(8), NAMES, fontsize=7)
        ax.set_yticks(range(8), NAMES, fontsize=7)
        ax.set_xlabel("frame index $b$")
        ax.set_ylabel("frame index $a$")
        ax.set_title(f"$\\omega_{{x{mu}\\,ab}}$ at the sample point")
        ax.grid(False)
        fig.colorbar(image, ax=ax, shrink=0.75)
    fig.tight_layout()
    save_figure(fig, "omega_heat_maps",
                "The canonical spin connection $\\omega_{\\mu ab}$ of the diagonal "
                "vielbein as three heat maps, for $\\mu = x0$ (left, the hidden "
                "direction), $\\mu = x1$ (middle, an inflating 3-space direction) and "
                "$\\mu = x5$ (right, a deflating extra time), at the sample point "
                "$H = 1$, $z = \\pi/4$, $a_4 = 1/2$, $a_4' = 1$, $b_4 = e^{2/3}$, "
                "$b_4'/b_4 = 4/3$ (on the history); rows $a$ and columns $b$ are the "
                "frame directions $x0$ to $x7$, the colour and the printed number give "
                "the value (red positive, blue negative, white zero). Each array is "
                "antisymmetric, and only the pairs with $x4$ or $x0$ are nonzero; the "
                "hidden direction and the extra time turn towards the time with the "
                "same negative rate $h_4 = -1/3$, the 3-space direction with the "
                "positive rate $a_4' = 1$.")
    '''),
    md(r"""
    ## 11. The spinor connection $\Omega_\mu$ and the covariant constancy of the gammas

    The next cell builds the eight 16 x 16 matrices $\Omega_\mu$ and the curved gammas
    $\gamma^\mu = \gamma^a/f_a$ (no sum) and checks:

    1. $\Omega_{x4} = 0$ (no frame direction turns when one moves along the time) and
       $\Omega_{x0} \neq 0$ (moving along the hidden direction, the hidden frame
       direction turns towards the time, because its length $s_b\cot z$ changes with
       the time);
    2. the closed forms of the record's formula `Omega_components`:
       $\Omega_{x0} = \frac12 h_4 s_b\cot z\,\gamma^{(x0)}\gamma^{(x4)}$,
       $\Omega_{xi} = \frac12 a_4' e^{a_4}\gamma^{(xi)}\gamma^{(x4)}$ ($i = 1, 2, 3$)
       and $\Omega_{xt} = \frac12 W\big(h_4 s_b\gamma^{(x4)}\gamma^{(xt)} +
       H\gamma^{(x0)}\gamma^{(xt)}\big)$ ($t = 5, 6, 7$);
    3. the defining property of the spinor connection, $[\Omega_\mu, \gamma^a] =
       -\sum_b \omega_\mu{}^a{}_b \gamma^b$ for all 64 pairs $(\mu, a)$: commuting
       with $\Omega_\mu$ turns the gammas exactly as $\omega_\mu$ turns the frame;
    4. the covariant constancy of the curved gammas, $D_\mu\gamma^\nu = \partial_\mu
       \gamma^\nu + \sum_\lambda\Gamma^\nu{}_{\mu\lambda}\gamma^\lambda + [\Omega_\mu,
       \gamma^\nu] = 0$ for all 64 pairs $(\mu, \nu)$, which is the vielbein postulate
       written with gammas.
    """),
    code(r'''
    Omega = spinor_connection(omega, S)  # eight 16 x 16 matrices
    gup = curved_gammas(e, gamma)  # gamma^mu = gamma^a / f_a for mu = a
    check(Omega[4] == Z16 and not matrix_is_zero(Omega[0]),
          "Omega_x4 = 0 and Omega_x0 is not zero",
          record=f"{REPORT_PY}, check Omega_x4_vanishes_Omega_x0_does_not")
    closed = ([h4 * s_b * sp.cot(z) * gamma[0] * gamma[4] / 2]
              + [a4p * sp.exp(a4) * gamma[i] * gamma[4] / 2 for i in (1, 2, 3)] + [Z16]
              + [W(x0) * (h4 * s_b * gamma[4] * gamma[t] + H * gamma[0] * gamma[t]) / 2
                 for t in (5, 6, 7)])  # the record's Omega_components, typed in
    check(all(matrix_is_zero(Omega[mu] - closed[mu]) for mu in range(8))
          and record_passed(REPORT_WL, "Omega_components"),
          "the eight Omega_mu are the closed forms of the record",
          record=f"{THEORY_FILE}, formula Omega_components")
    rotation_ok = all(matrix_is_zero(
        Omega[mu] * gamma[a] - gamma[a] * Omega[mu]
        + sum((ETA[a] * omega[mu][a][b] * gamma[b] for b in range(8)), Z16))
        for mu in range(8) for a in range(8))
    check(rotation_ok, "[Omega_mu, gamma^a] = -omega_mu^a_b gamma^b for all 64 pairs",
          record=f"{REPORT_WL}, check S_rotates_gamma_with_omega")
    constancy_ok = all(matrix_is_zero(
        gup[nu].diff(x[mu]) + sum((Gam[nu][mu][lam] * gup[lam] for lam in range(8)), Z16)
        + Omega[mu] * gup[nu] - gup[nu] * Omega[mu])
        for mu in range(8) for nu in range(8))
    check(constancy_ok and record_passed(REPORT_WL, "gamma_covariantly_constant")
          and record_passed(REPORT_PY, "covariant_constancy_D_mu_gamma_nu"),
          "D_mu gamma^nu = 0 for all 64 pairs (mu, nu)",
          record=f"{REPORT_WL}, check gamma_covariantly_constant")
    say(f"Omega_x5 has {sum(1 for v in Omega[5] if v != 0)} nonzero entries of 256")
    '''),
    md(r"""
    The author's gammas are real, the four space-like ones are symmetric matrices and
    the four time-like ones are antisymmetric. Because of this, $S^{ab} =
    \frac12\gamma^a\gamma^b$ ($a \ne b$) is a SYMMETRIC matrix when one of $a, b$ is
    space-like and the other time-like (a **boost**, 16 pairs), and an ANTISYMMETRIC
    matrix when both are of the same kind (a **rotation**, 12 pairs). The next cell
    checks this for all 28 pairs and then draws $\Omega_{x0}$, $\Omega_{x1}$ and
    $\Omega_{x5}$ as 16 x 16 heat maps at the sample point. $\Omega_{x0}$ is a pure
    boost ($x0$ with the time $x4$) and so is $\Omega_{x1}$ ($x1$ with $x4$): both are
    symmetric. $\Omega_{x5}$ is a rotation ($x4$ with $x5$, two time-like directions)
    plus a boost ($x0$ with $x5$).
    """),
    code(r'''
    pattern_ok = True
    for a in range(8):
        for b in range(a + 1, 8):
            boost = ETA[a] * ETA[b] == -1  # one space-like, one time-like direction
            want = S[a][b] if boost else -S[a][b]  # S^T = S (boost) or -S (rotation)
            pattern_ok = pattern_ok and S[a][b].T == want
    check(pattern_ok, "S^ab is symmetric for the 16 boosts, antisymmetric for the 12 "
          "rotations")
    fig, axes = plt.subplots(1, 3, figsize=(12.0, 3.9))
    for ax, mu in zip(axes, (0, 1, 5)):  # the directions x0, x1 and x5
        table = np.array([[at_sample(v).real for v in row] for row in Omega[mu].tolist()])
        limit = np.abs(table).max()
        image = ax.imshow(table, cmap="RdBu_r", vmin=-limit, vmax=limit)
        ax.set_xticks(range(0, 16, 3), [str(k + 1) for k in range(0, 16, 3)])
        ax.set_yticks(range(0, 16, 3), [str(k + 1) for k in range(0, 16, 3)])
        ax.set_xlabel("column (spinor component 1 to 16)")
        ax.set_ylabel("row (spinor component)")
        ax.set_title(f"$\\Omega_{{x{mu}}}$ at the sample point")
        ax.grid(False)
        fig.colorbar(image, ax=ax, shrink=0.75)
    fig.tight_layout()
    save_figure(fig, "spinor_connection_heat_maps",
                "The spinor connection $\\Omega_{x0}$ (left), $\\Omega_{x1}$ (middle) "
                "and $\\Omega_{x5}$ (right) as 16 x 16 heat maps at the sample point "
                "$H = 1$, $z = \\pi/4$, $a_4 = 1/2$, $a_4' = 1$, $b_4 = e^{2/3}$, "
                "$b_4'/b_4 = 4/3$; rows and columns are the 16 spinor components, red "
                "is positive, blue negative, white zero, each panel with its own colour "
                "scale. $\\Omega_{x0}$ and $\\Omega_{x1}$ are boosts (a space-like "
                "direction with the time), symmetric matrices (entries $(i, j)$ and "
                "$(j, i)$ of the same colour); $\\Omega_{x5}$ is a rotation of two "
                "time-like directions, antisymmetric, plus a boost. All three map the "
                "first eight components to the first eight and the last eight to the "
                "last eight.")
    '''),
    md(r"""
    ## 12. The contraction $\gamma^\mu\Omega_\mu$, direction by direction

    The field equation contains $\gamma^\mu D_\mu\Psi = \gamma^\mu\partial_\mu\Psi +
    \gamma^\mu\Omega_\mu\Psi$, so the spin connection enters it only through the
    16 x 16 matrix $\gamma^\mu\Omega_\mu$ (summed over $\mu$). The next cell computes
    each term $\gamma^\mu\Omega_\mu$ (no sum) separately and writes it as
    $\alpha_\mu\gamma^{(x4)} + \beta_\mu\gamma^{(x0)}$. The numbers $\alpha_\mu$ and
    $\beta_\mu$ are found with traces: for two different gammas
    $\mathrm{tr}(\gamma^a\gamma^b) = 0$, while $\mathrm{tr}(\gamma^{(x4)}
    \gamma^{(x4)}) = -16$ and $\mathrm{tr}(\gamma^{(x0)}\gamma^{(x0)}) = +16$, so
    $\alpha_\mu = -\mathrm{tr}(M\gamma^{(x4)})/16$ and $\beta_\mu =
    \mathrm{tr}(M\gamma^{(x0)})/16$ for $M = \gamma^\mu\Omega_\mu$; the cell then
    checks that $M - \alpha_\mu\gamma^{(x4)} - \beta_\mu\gamma^{(x0)}$ is the zero
    matrix. It compares the table with the predicted values ($\alpha = h_4/2$ for $x0$
    and for $x5, x6, x7$, $\alpha = a_4'/2$ for $x1, x2, x3$, $\beta =
    \frac12He^{a_4}b_4^{-1/2}$ for $x5, x6, x7$, and zero otherwise), with the record's
    table `gammaOmega_per_direction`, and the sum with the record's
    `gammaOmega_total`. Finally it evaluates the sum on the history of the record,
    where $e^{a_4}b_4^{-1/2} = e^{Hx_4/3}$, $h_4 = -H/3$ and $v_g = \frac56H$.
    """),
    code(r'''
    per_direction = []  # (alpha_mu, beta_mu) for mu = x0 ... x7
    decomposed = True
    for mu in range(8):
        M = (gup[mu] * Omega[mu]).applyfunc(sp.simplify)
        alpha = sp.simplify(-(M * gamma[4]).trace() / 16)  # coefficient of gamma^(x4)
        beta = sp.simplify((M * gamma[0]).trace() / 16)  # coefficient of gamma^(x0)
        decomposed = decomposed and matrix_is_zero(M - alpha * gamma[4] - beta * gamma[0])
        per_direction.append((alpha, beta))
        say(f"gamma^{NAMES[mu]} Omega_{NAMES[mu]} = ({alpha}) gamma^(x4) "
            f"+ ({beta}) gamma^(x0)")
    c_g = sp.Rational(3, 2) * H * sp.exp(a4) / sp.sqrt(b4)  # coefficient of gamma^(x0)
    v_g = b4p / b4 - a4p / 2  # coefficient of gamma^(x4)
    warp_term = H * sp.exp(a4) / (2 * sp.sqrt(b4))  # beta of an extra time
    predicted = ([(h4 / 2, 0)] + [(a4p / 2, 0)] * 3 + [(0, 0)]
                 + [(h4 / 2, warp_term)] * 3)  # x0, x1..x3, x4, x5..x7
    check(decomposed and all(is_zero(per_direction[k][0] - predicted[k][0])
                             and is_zero(per_direction[k][1] - predicted[k][1])
                             for k in range(8))
          and record_passed(REPORT_PY, "per_direction_terms")
          and record_passed(REPORT_WL, "gammaOmega_per_direction"),
          "the eight terms gamma^mu Omega_mu (no sum)",
          record=f"{REPORT_WL}, check gammaOmega_per_direction")
    table_record = record_formula("gammaOmega_per_direction", RECORD_NAMES)
    check(all(is_zero(per_direction[k][0] - table_record[k][1])
              and is_zero(per_direction[k][1] - table_record[k][2]) for k in range(8)),
          "the eight terms equal the record's table",
          record=f"{THEORY_FILE}, formula gammaOmega_per_direction")
    space_part = sp.simplify(sum(per_direction[k][0] for k in (1, 2, 3)))
    block_part = sp.simplify(sum(per_direction[k][0] for k in (0, 5, 6, 7)))
    hidden = sp.simplify(sum(beta for _, beta in per_direction))
    report("x4 part from the inflating x1, x2, x3", space_part)
    report("x4 part from the hidden block x0, x5, x6, x7", block_part)
    report("x0 part from all directions", hidden)
    check(is_zero(space_part - 3 * a4p / 2) and is_zero(block_part - 2 * h4)
          and is_zero(space_part + block_part - v_g) and is_zero(hidden - c_g),
          "x4 parts: 3-space (3/2) a4', hidden block 2 h4, together v_g; x0 part c_g",
          record=f"{REPORT_PY}, check per_direction_terms")
    slash = sum((gup[mu] * Omega[mu] for mu in range(8)), Z16)
    gravity_term = c_g * gamma[0] + v_g * gamma[4]
    total_text = FORMULAS["gammaOmega_total"].replace(chr(34), "")  # gamma[x0], gamma[x4]
    total_record = wolfram_to_sympy(total_text.replace("gamma[x0]", "G0")
                                    .replace("gamma[x4]", "G4"), RECORD_NAMES)
    G0, G4 = sp.Symbol("G0"), sp.Symbol("G4")  # the record's gamma[x0], gamma[x4]
    record_matrix = (total_record.coeff(G0) * gamma[0]
                     + total_record.coeff(G4) * gamma[4])
    check(matrix_is_zero(slash - gravity_term) and matrix_is_zero(slash - record_matrix)
          and record_passed(REPORT_WL, "gammaOmega_total")
          and record_passed(REPORT_PY, "gamma_mu_Omega_mu_equals_hidden_block_terms")
          and record_passed(REPORT_LEAD, "gamma_Omega_equals_hidden_block_terms"),
          "gamma^mu Omega_mu = (3/2) H e^(a4) b4^(-1/2) gamma^(x0) + (b4'/b4 - a4'/2) "
          "gamma^(x4) exactly",
          record=f"{THEORY_FILE}, formula gammaOmega_total; {REPORT_LEAD}, check "
                 "gamma_Omega_equals_hidden_block_terms")
    on_history = {b4p: BETA * A_EXACT * H * b4, a4p: A_EXACT * H}  # the derivatives
    history_values = {a4: A_EXACT * H * x4, b4: B4_ZERO * sp.exp(BETA * A_EXACT * H * x4)}
    slash_history = slash.subs(on_history).subs(history_values)
    check(matrix_is_zero(slash_history - sp.Rational(3, 2) * H * sp.exp(H * x4 / 3)
                         * gamma[0] - sp.Rational(5, 6) * H * gamma[4]),
          "on the history of the record: gamma^mu Omega_mu = (3/2) H e^(H x4/3) "
          "gamma^(x0) + (5/6) H gamma^(x4)")
    '''),
    md(r"""
    The next cell draws the table of the previous cell as three bar charts, one bar for
    each direction $\mu$. The coefficient $\alpha_\mu$ of $\gamma^{(x4)}$ is the sum of
    a part proportional to $a_4'$ and a part proportional to $b_4'/b_4$; the left chart
    shows the first in units of $a_4'$, the middle chart the second in units of
    $b_4'/b_4$, and the right chart the coefficient $\beta_\mu$ of $\gamma^{(x0)}$ in
    units of $He^{a_4}b_4^{-1/2}$. On the left, three bars $+\frac12$ (3-space) and four
    bars $-\frac12$ (the hidden block): total $-\frac12$; in the middle, four bars
    $\frac14$ (the hidden block): total $1$; on the right, three bars $\frac12$ (the
    extra times): total $\frac32$.
    """),
    code(r'''
    a4_part = [float(sp.simplify(alpha.subs(b4p, 0) / a4p))  # the part with a4'
               for alpha, _ in per_direction]
    b4_part = [float(sp.simplify(alpha.subs(a4p, 0) / (b4p / b4)))
               for alpha, _ in per_direction]  # the part with b4'/b4
    beta_units = [float(sp.simplify(beta / (H * sp.exp(a4) / sp.sqrt(b4))))
                  for _, beta in per_direction]  # beta / (H e^a4 b4^(-1/2))
    positions = np.arange(8)
    fig, axes = plt.subplots(1, 3, figsize=(12.0, 4.2), sharey=True)
    colors = ["tab:blue"] + ["tab:red"] * 3 + ["gray"] + ["tab:blue"] * 3
    panels = [(a4_part, "$\\gamma^{(x4)}$, part / $a_4'$"),
              (b4_part, "$\\gamma^{(x4)}$, part / $(b_4'/b_4)$"),
              (beta_units, "$\\gamma^{(x0)}$ / $(He^{a_4}b_4^{-1/2})$")]
    for ax, (heights, title) in zip(axes, panels):
        ax.bar(positions, heights, color=colors, width=0.6)
        ax.set_title(f"{title}: total {sum(heights):g}", fontsize=10)
        ax.axhline(0.0, color="black", linewidth=0.8)
        ax.set_xticks(positions, NAMES)
        ax.set_xlabel("direction $\\mu$")
    axes[0].set_ylabel("coefficient (in the unit named in the title)")
    save_figure(fig, "gamma_omega_per_direction",
                "The eight terms $\\gamma^\\mu\\Omega_\\mu$ (no sum) of the diagonal "
                "vielbein, each equal to $\\alpha_\\mu\\gamma^{(x4)} + "
                "\\beta_\\mu\\gamma^{(x0)}$; horizontal axis the direction $\\mu$ (red: "
                "inflating 3-space, blue: the hidden block of $x0$ and the three extra "
                "times, gray: time). Left: the part of $\\alpha_\\mu$ proportional to "
                "$a_4'$, in units of $a_4'$: $+1/2$ for $x1, x2, x3$ and $-1/2$ for "
                "$x0, x5, x6, x7$, total $-1/2$. Middle: the part proportional to "
                "$b_4'/b_4$, in units of $b_4'/b_4$: $1/4$ for each direction of the "
                "hidden block, total $1$. Right: $\\beta_\\mu$ in units of "
                "$He^{a_4}b_4^{-1/2}$: three times $1/2$, total $3/2$. So "
                "$\\gamma^\\mu\\Omega_\\mu = \\frac32He^{a_4}b_4^{-1/2}\\gamma^{(x0)} + "
                "(b_4'/b_4 - a_4'/2)\\gamma^{(x4)}$.")
    '''),
    md(r"""
    The next cell shows the same sum as pictures of the 16 x 16 matrices at the sample
    point on the history ($H = 1$, $a_4 = 1/2$, $a_4' = 1$, $b_4 = e^{2/3}$, $b_4'/b_4 =
    4/3$): the sum of the three 3-space terms, $\frac32a_4'\gamma^{(x4)}$ (entries
    $\pm1.5$); the sum of the four terms of the hidden block, $2h_4\gamma^{(x4)} +
    c_g\gamma^{(x0)}$ (entries $\mp0.67$ in the pattern of $\gamma^{(x4)}$ and $c_g =
    \frac32e^{1/6} = 1.77$ in the pattern of $\gamma^{(x0)}$); the total; and the
    predicted $c_g\gamma^{(x0)} + v_g\gamma^{(x4)}$ with $v_g = \frac56$. The author's
    $\gamma^{(x0)}$ has the 8 x 8 identity matrix in its upper-right and lower-left
    blocks and zeros elsewhere: it maps the first eight spinor components onto the last
    eight and back, so $c_g\gamma^{(x0)}$ shows the value $c_g$ on two diagonal lines.
    The cell first checks the block form of all eight gammas against the record's list
    `field_equation_blocks`: each entry $\{xa, \bar t, t\}$ says that $\gamma^{(xa)}$
    has the 8 x 8 block $\bar t$ in its upper-right corner, the block $t$ in its
    lower-left corner and zeros in the two diagonal blocks. The record is written with
    curly brackets; replacing them by square brackets turns each entry into JSON, which
    `json.loads` reads.
    """),
    code(r'''
    I8, Z8 = sp.eye(8), sp.zeros(8, 8)  # 8 x 8 identity and zero matrices
    blocks_ok = True
    for entry in FORMULAS["field_equation_blocks"]:  # eight texts {"xa", tb, t}
        name, tb, t = json.loads(entry.replace("{", "[").replace("}", "]"))
        a = NAMES.index(name)  # the position of the direction xa (0 ... 7)
        # gamma^(xa) must be the block matrix with the zero blocks on the diagonal
        blocks_ok = blocks_ok and gamma[a] == sp.BlockMatrix(
            [[Z8, sp.Matrix(tb)], [sp.Matrix(t), Z8]]).as_explicit()
    check(blocks_ok and len(FORMULAS["field_equation_blocks"]) == 8
          and record_passed(REPORT_WL, "block_form"),
          "the eight gammas have the block form of the record",
          record=f"{THEORY_FILE}, formula field_equation_blocks")
    check(gamma[0] == sp.BlockMatrix([[Z8, I8], [I8, Z8]]).as_explicit(),
          "gamma^(x0) has the 8 x 8 identity in its two off-diagonal blocks")
    panels = [
        ("sum over $x1, x2, x3$", sum((gup[k] * Omega[k] for k in (1, 2, 3)), Z16)),
        ("sum over $x0, x5, x6, x7$", sum((gup[k] * Omega[k] for k in (0, 5, 6, 7)), Z16)),
        ("total $\\gamma^\\mu\\Omega_\\mu$", slash),
        ("$c_g\\gamma^{(x0)} + v_g\\gamma^{(x4)}$", gravity_term),
    ]
    fig, axes = plt.subplots(2, 2, figsize=(8.0, 7.6))
    for ax, (title, matrix) in zip(axes.flat, panels):
        table = np.array([[at_sample(v).real for v in row] for row in matrix.tolist()])
        image = ax.imshow(table, cmap="RdBu_r", vmin=-2.0, vmax=2.0)
        ax.set_title(title, fontsize=10)
        ax.set_xticks([])
        ax.set_yticks([])
        ax.grid(False)
    fig.colorbar(image, ax=axes, shrink=0.7, label="entry value")
    save_figure(fig, "gamma_omega_sum",
                "The sum as pictures of 16 x 16 matrices at the sample point "
                "$H = 1$, $z = \\pi/4$, $a_4 = 1/2$, $a_4' = 1$, $b_4 = e^{2/3}$, "
                "$b_4'/b_4 = 4/3$ (on the history of the Revision record) "
                "(red positive, blue negative, white zero; colour scale from $-2$ to "
                "$2$). Top left: the sum of the three 3-space terms, "
                "$\\frac32 a_4'\\gamma^{(x4)}$ with entries $\\pm 1.5$; top right: the "
                "sum of the four terms of the hidden block $x0, x5, x6, x7$, "
                "$2h_4\\gamma^{(x4)} + c_g\\gamma^{(x0)}$ with $2h_4 = -2/3$ and $c_g = "
                "1.77$ on two diagonal lines; their $\\gamma^{(x4)}$ parts have opposite "
                "signs and do not cancel. Bottom left: the total over all eight "
                "directions; bottom right: $c_g\\gamma^{(x0)} + v_g\\gamma^{(x4)}$ with "
                "$v_g = 5/6$. The two bottom pictures are identical.")
    '''),
    md(r"""
    ## 13. Where the two terms come from: the divergence form

    Two facts explain the result without computing all of $\Omega_\mu$.

    **Fact 1.** For each $\mu$ separately, $\gamma^\mu\Omega_\mu + \Omega_\mu\gamma^\mu
    = 0$ (no sum). Now sum the covariant constancy $D_\mu\gamma^\nu = 0$ over
    $\mu = \nu$: $\sum_\mu\partial_\mu\gamma^\mu + \sum_{\mu,\lambda}
    \Gamma^\mu{}_{\mu\lambda}\gamma^\lambda + \sum_\mu(\Omega_\mu\gamma^\mu -
    \gamma^\mu\Omega_\mu) = 0$. The standard contraction $\sum_\mu
    \Gamma^\mu{}_{\mu\lambda} = \partial_\lambda \ln\sqrt{|g|}$ turns the first two sums
    into $\frac{1}{\sqrt{|g|}}\sum_\mu\partial_\mu(\sqrt{|g|}\,\gamma^\mu)$ (product
    rule), and Fact 1 turns the last sum into $-2\sum_\mu\gamma^\mu\Omega_\mu$. Solving
    for the contraction gives

    $$\gamma^\mu\Omega_\mu = \frac{1}{2\sqrt{|g|}}\sum_\mu \partial_\mu\big(\sqrt{|g|}\,
    \gamma^\mu\big) .$$

    The constant sign $G$ of $\cot z$ in $\sqrt{|g|} = G f_0\cdots f_7$ cancels between
    the numerator and the denominator, so the signed product $f_0\cdots f_7$ can be
    used.

    **Fact 2.** For the diagonal vielbein, $\sqrt{|g|}\gamma^\mu = \pm\big(\prod_{c \ne
    \mu} f_c\big)\gamma^{(\mu)}$, because $\gamma^\mu = \gamma^{(\mu)}/f_\mu$. Now
    $\prod_{c \ne x4} f_c = e^{-a_4}b_4^2\cot z\,W^3$, the whole volume factor, so the
    time direction contributes $\frac12\partial_{x4}\ln(e^{-a_4}b_4^2) = b_4'/b_4 -
    a_4'/2 = v_g$: half the rate at which the 7-volume changes. And $\prod_{c \ne x0}
    f_c = b_4^{3/2}W^3$ (3-space and the extra times; $e^{3a_4}$ and $e^{-3a_4}$
    cancel) gives $\frac{1}{2e^{-a_4}b_4^2\cot z\,W^3}\,\partial_{x0}(b_4^{3/2}W^3) =
    \frac{3H\cot z\,b_4^{3/2}W^3}{2e^{-a_4}b_4^2\cot z\,W^3} = \frac32He^{a_4}b_4^{-1/2}
    = c_g$: the warp of the three extra times along $x0$. The other six products do not
    depend on their own coordinate.

    The next cell checks Fact 1 for every $\mu$, the divergence form, and the eight
    products of Fact 2.
    """),
    code(r'''
    anticommutes = all(matrix_is_zero(gup[mu] * Omega[mu] + Omega[mu] * gup[mu])
                       for mu in range(8))
    check(anticommutes, "{gamma^mu, Omega_mu} = 0 for each mu separately",
          record=f"{REPORT_PY}, check anticommutator_gamma_Omega_vanishes")
    sqrt_g = volume  # f_0 ... f_7; the sign G of cot z cancels in the formula
    divergence = sum(((sqrt_g * gup[mu]).diff(x[mu]) for mu in range(8)), Z16) / (2 * sqrt_g)
    check(matrix_is_zero(divergence - gravity_term)
          and record_passed(REPORT_WL, "gammaOmega_divergence_form")
          and record_passed(REPORT_PY, "divergence_of_sqrtg_gamma")
          and record_passed(REPORT_LEAD, "gamma_Omega_divergence_formula"),
          "(1/(2 sqrt|g|)) d_mu (sqrt|g| gamma^mu) = c_g gamma^(x0) + v_g gamma^(x4)",
          record=f"{REPORT_WL}, check gammaOmega_divergence_form")
    products = [sp.simplify(sp.prod([f[c] for c in range(8) if c != b])) for b in range(8)]
    for b in (0, 4):
        say(f"product of the f_c with c != {NAMES[b]}: {products[b]}")
    own_coordinate = [sp.simplify(sp.diff(products[b], x[b]) / (2 * sqrt_g))
                      for b in range(8)]
    say("(1/(2 sqrt|g|)) d_b (product without b), b = x0 ... x7: "
        f"{own_coordinate}")
    expected_own = [c_g, 0, 0, 0, v_g, 0, 0, 0]
    check(all(is_zero(own_coordinate[b] - expected_own[b]) for b in range(8)),
          "only the hidden direction (c_g) and the time (v_g) contribute")
    '''),
    md(r"""
    The next cell checks Fact 2 with numbers instead of symbols, as a student would with
    a calculator. For the hidden direction it computes the derivative of
    $(\sin^2 z)^{1/4} = W^3$ with respect to $x_0$ by a **central difference**,
    $\big(F(x_0 + h) - F(x_0 - h)\big)/(2h)$ with the small step $h = 10^{-5}$, divides
    by $2\cot z\,(\sin^2 z)^{1/4}$ and plots the result across one whole cell with
    $H = 1$ (the factors $b_4^{3/2}$ and $e^{-a_4}b_4^2$ do not depend on $x_0$ and
    leave the factor $e^{a_4}b_4^{-1/2}$, by which the coefficient is divided; the
    points within $0.06$ of the fold and of the ends of the cell are left out, where
    numerator and denominator both approach zero or infinity). For the time direction
    it takes the history $a_4 = x_4$ with one illustrative function, $b_4(x_4) =
    e^{4x_4/3}(1 + \frac12\sin x_4)$ (positive; the exponential of the history of the
    record with an added wobble, an illustration only), computes the derivative of
    $e^{-a_4}b_4^2$ with respect to $x_4$ in the same way, divides by
    $2e^{-a_4}b_4^2$ and compares with the exact $v_g = b_4'/b_4 - a_4'/2$; on the
    history of the record itself, $b_4 = e^{4x_4/3}$, the coefficient is exactly
    $\frac56$, drawn as a line for comparison. The differences from the exact values
    are of the size $h^2$ times third derivatives, far below the check limit
    $10^{-6}$.
    """),
    code(r'''
    H_value = 1.0
    z_values = np.concatenate([np.linspace(0.06, np.pi / 2 - 0.06, 200),
                               np.linspace(np.pi / 2 + 0.06, np.pi - 0.06, 200)])
    x0_values = z_values / (6 * H_value)  # both halves of the cell 0 < z < pi
    step = 1e-5  # the step h of the central difference


    def hidden_density(x0_value):
        return np.abs(np.sin(6 * H_value * x0_value)) ** 0.5  # (sin^2 z)^(1/4) = W^3


    derivative = (hidden_density(x0_values + step)
                  - hidden_density(x0_values - step)) / (2 * step)
    ratio = derivative / (2 * hidden_density(x0_values) / np.tan(z_values))  # 3H/2
    x4_values = np.linspace(-6.0, 6.0, 300)


    def b4_history(x4_value):  # an illustrative b4(x4) > 0: the history with a wobble
        return np.exp(4.0 * x4_value / 3.0) * (1.0 + 0.5 * np.sin(x4_value))


    def time_density(x4_value):
        return np.exp(-x4_value) * b4_history(x4_value) ** 2  # e^(-a4) b4^2, a4 = x4


    time_derivative = (time_density(x4_values + step)
                       - time_density(x4_values - step)) / (2 * step)
    time_ratio = time_derivative / (2 * time_density(x4_values))  # d ln(e^-a4 b4^2) / 2
    # v_g = b4'/b4 - a4'/2 = 4/3 + (1/2) cos x4 / (1 + (1/2) sin x4) - 1/2
    exact_time = (4.0 / 3.0 + 0.5 * np.cos(x4_values) / (1.0 + 0.5 * np.sin(x4_values))
                  - 0.5)
    report("largest |central difference - 3H/2| over the cell",
           f"{np.max(np.abs(ratio - 1.5)):.0e}")
    report("largest |central difference - v_g| over the grid",
           f"{np.max(np.abs(time_ratio - exact_time)):.0e}")
    check(np.max(np.abs(ratio - 1.5)) < 1e-6
          and np.max(np.abs(time_ratio - exact_time)) < 1e-6,
          "the numerical derivatives give c_g / (e^a4 b4^(-1/2)) = 3H/2 and v_g")
    fig, (ax_left, ax_right) = plt.subplots(1, 2, figsize=(10.0, 4.2))
    for half in (slice(0, 200), slice(200, 400)):  # the two halves, drawn separately
        ax_left.plot(z_values[half], ratio[half], color="tab:blue")
    ax_left.plot([], [], color="tab:blue",
                 label="$\\partial_{x0}(\\sin^2 z)^{1/4}/(2\\cot z\\,(\\sin^2 z)^{1/4})$")
    ax_left.axvline(np.pi / 2, color="gray", linewidth=0.8)  # the fold
    ax_left.set_ylim(0.0, 2.4)
    ax_left.set_xlabel("hidden angle $z = 6Hx_0$ (radians), fold at $\\pi/2$")
    ax_left.set_ylabel("$c_g/(e^{a_4}b_4^{-1/2})$ (units of $H$)")
    ax_left.set_title("Hidden direction: the constant $3H/2$")
    ax_left.legend(fontsize=8, loc="lower center")
    ax_right.plot(x4_values, time_ratio, label="central difference, "
                  "$b_4 = e^{4x_4/3}(1 + \\frac{1}{2}\\sin x_4)$")
    ax_right.plot(x4_values, exact_time, ":", color="black", linewidth=2.5,
                  label="exact $b_4'/b_4 - a_4'/2$")
    ax_right.plot(x4_values, np.full_like(x4_values, 5.0 / 6.0), "--", color="gray",
                  label="history $b_4 = e^{4x_4/3}$: exactly $5/6$")
    ax_right.set_ylim(-0.6, 1.9)  # room for the legend below the curves
    ax_right.set_xlabel("time $x_4$ (units $1/H$), $a_4 = x_4$")
    ax_right.set_ylabel("coefficient $v_g$ of $\\gamma^{(x4)}$")
    ax_right.set_title("Time direction: $v_g = b_4'/b_4 - a_4'/2$")
    ax_right.legend(fontsize=8, loc="lower center")
    save_figure(fig, "divergence_form",
                "The divergence form of $\\gamma^\\mu\\Omega_\\mu$, with $H = 1$, checked "
                "by central differences with step $10^{-5}$. Left: the coefficient "
                "$c_g$ of $\\gamma^{(x0)}$ divided by $e^{a_4}b_4^{-1/2}$, "
                "$\\partial_{x0}(\\sin^2 z)^{1/4}/(2\\cot z\\,(\\sin^2 z)^{1/4})$, versus "
                "the hidden angle $z$ in radians across both halves of a cell (the "
                "vertical line is the fold): the constant $3/2$ for every $z$. Right: "
                "the coefficient of $\\gamma^{(x4)}$, $\\partial_{x4}(e^{-a_4}b_4^2)/"
                "(2e^{-a_4}b_4^2)$, versus the time $x_4$ for $a_4 = x_4$ and the "
                "illustrative function $b_4 = e^{4x_4/3}(1 + \\frac12\\sin x_4)$ "
                "(solid), on the exact $b_4'/b_4 - a_4'/2$ (dotted), and $5/6$ for the "
                "history $b_4 = e^{4x_4/3}$ of the Revision record (dashed): the time "
                "term is half the rate of the 7-volume $e^{-a_4}b_4^2$.")
    '''),
    md(r"""
    ## 14. The covariant derivative of a spinor and the Dirac operator written out

    The next cell takes a completely general spinor field: 16 unknown functions
    $\psi_1, \dots, \psi_{16}$ of all eight coordinates. It computes the covariant
    derivatives $D_\mu\Psi = \partial_\mu\Psi + \Omega_\mu\Psi$ and the Dirac operator
    $\gamma^\mu D_\mu\Psi$, and checks that

    $$\gamma^\mu D_\mu\Psi = \sum_a \frac{1}{f_a}\gamma^{(a)}\partial_a\Psi +
    c_g\gamma^{(x0)}\Psi + v_g\gamma^{(x4)}\Psi ,$$

    that is, with the factors written out, $e^{a_4}b_4^{-1/2}\tan z\,
    \gamma^{(x0)}\partial_0\Psi + e^{-a_4}(\gamma^{(x1)}\partial_1 +
    \gamma^{(x2)}\partial_2 + \gamma^{(x3)}\partial_3)\Psi + \gamma^{(x4)}\partial_4\Psi
    + e^{a_4}b_4^{-1/2}W^{-1}(\gamma^{(x5)}\partial_5 + \gamma^{(x6)}\partial_6 +
    \gamma^{(x7)}\partial_7)\Psi + c_g\gamma^{(x0)}\Psi + v_g\gamma^{(x4)}\Psi$. It
    then compares all 16 components with the 16 component equations of the record
    (`field_equation_components`; their right-hand side $V\Psi_A$, $V = m + U'(S)$, is
    not needed here).

    Finally it checks when the term $M\Psi$, $M = c_g\gamma^{(x0)} +
    v_g\gamma^{(x4)}$, can vanish for a field that is not zero. Since
    $(\gamma^{(x0)})^2 = 1$, $(\gamma^{(x4)})^2 = -1$ and the two anticommute,
    $MM = (c_g^2 - v_g^2)\,1$. When the number in front of $1$ is not zero, $M\Psi = 0$
    gives $\Psi = 0$ (multiply by $M$ and divide by that number); the WolframScript
    report `wolfram-field-theory.json` records the statement for both fields (checks
    `nontriviality_1_dirac16complex` and `nontriviality_2_dirac16complex00`). Where
    $c_g = \pm v_g$, however, $MM = 0$: the cell computes that $\gamma^{(x0)} \pm
    \gamma^{(x4)}$ has rank 8, so there $M$ sends an 8-dimensional set of nonzero fields
    to zero (the sympy report checks the same, check `gravity_term_square`). On the
    history of the record $MM = H^2\big(\frac94e^{2Hx_4/3} - \frac{25}{36}\big)\,1$,
    which vanishes at exactly one time, $x_4 = 3\ln(5/9)/H$; the cell computes this
    time.
    """),
    code(r'''
    import re  # text patterns, to rename the record's symbols

    psi = sp.Matrix([sp.Function(f"psi{A}")(*x) for A in range(1, 17)])  # 16 functions
    D = [psi.diff(x[mu]) + Omega[mu] * psi for mu in range(8)]  # D_mu Psi
    dirac = sum((gup[mu] * D[mu] for mu in range(8)), sp.zeros(16, 1))
    written_out = sum((gamma[a] * psi.diff(x[a]) / f[a] for a in range(8)),
                      sp.zeros(16, 1)) + gravity_term * psi
    check(all(is_zero(v) for v in dirac - written_out)
          and record_passed(REPORT_WL, "Dirac_operator_explicit_C")
          and record_passed(REPORT_WL, "Dirac_operator_explicit_G"),
          "gamma^mu D_mu Psi = sum_a (1/f_a) gamma^a d_a Psi + c_g gamma^(x0) Psi + "
          "v_g gamma^(x4) Psi",
          record=f"{REPORT_WL}, checks Dirac_operator_explicit_C and _G")
    # Rename the derivatives d psi_B / d x_k and then the functions psi_B as plain
    # symbols dPsi<B>x<k> and Psi<B> (derivatives first: renaming psi_B first would
    # turn its derivatives into derivatives of a constant symbol, which are zero).
    rename_derivatives = {sp.Derivative(psi[B], x[k]): sp.Symbol(f"dPsi{B + 1}x{k}")
                          for B in range(16) for k in range(8)}
    rename_functions = {psi[B]: sp.Symbol(f"Psi{B + 1}") for B in range(16)}


    def same_components(equations):
        """True when the 16 left sides of the record equal ours."""
        same = True
        for A, equation in enumerate(equations):
            left = equation.split("==")[0]  # the record: left side == V*Psi[A]
            left = left.replace(chr(34), "")  # chr(34) is the double-quote character
            # dd[x4, Psi[14]] (the derivative of Psi_14 by x4) becomes dPsi14x4:
            left = re.sub(r"dd\[x(\d), Psi\[(\d+)\]\]", r"dPsi\2x\1", left)
            left = re.sub(r"Psi\[(\d+)\]", r"Psi\1", left)
            record_left = wolfram_to_sympy(left, RECORD_NAMES)
            mine = dirac[A].subs(rename_derivatives).subs(rename_functions)
            same = same and is_zero(mine - record_left)
        return same


    check(same_components(FORMULAS["field_equation_components"]),
          "all 16 components of the Dirac operator equal the record",
          record=f"{THEORY_FILE}, formula field_equation_components")
    square = (gravity_term * gravity_term - (c_g**2 - v_g**2) * I16)
    ranks = [(gamma[0] + sign * gamma[4]).rank() for sign in (1, -1)]
    report("ranks of gamma^(x0) + gamma^(x4) and gamma^(x0) - gamma^(x4)", ranks)
    both_fields = all(record_passed(REPORT_WL, name) for name in [
        "nontriviality_1_dirac16complex", "nontriviality_2_dirac16complex00"])
    check(matrix_is_zero(square) and gamma[0] * gamma[0] == I16 and ranks == [8, 8]
          and both_fields and record_passed(REPORT_PY, "gravity_term_square"),
          "M M = (c_g^2 - v_g^2) 1: M Psi = 0 only for Psi = 0 unless c_g = +-v_g, "
          "and there M has rank 8",
          record=f"{REPORT_PY}, check gravity_term_square; {REPORT_WL}, checks "
                 "nontriviality_1_dirac16complex and nontriviality_2_dirac16complex00")
    square_history = sp.simplify((c_g**2 - v_g**2).subs(on_history).subs(history_values))
    zero_time = sp.solve(sp.Eq(sp.Rational(3, 2) * sp.exp(H * x4 / 3),
                               sp.Rational(5, 6)), x4)  # c_g = v_g on the history
    say(f"on the history c_g^2 - v_g^2 = {sp.expand(square_history)}")
    report("the one time of the history with c_g = v_g, x4 H",
           f"{float(zero_time[0].subs(H, 1)):.4f}")
    check(is_zero(square_history - H**2 * (sp.Rational(9, 4) * sp.exp(2 * H * x4 / 3)
                                          - sp.Rational(25, 36)))
          and len(zero_time) == 1 and is_zero(zero_time[0] - 3 * sp.log(
              sp.Rational(5, 9)) / H),
          "on the history c_g^2 - v_g^2 = H^2 ((9/4) e^(2 H x4/3) - 25/36), zero only "
          "at x4 = 3 ln(5/9)/H")
    '''),
    md(r"""
    The term $\gamma^\mu\Omega_\mu$ is not the only place where the metric enters the
    Dirac operator: the factors $1/f_a$ in front of the derivatives carry it too. The
    next cell draws these factors. On the left, versus the time on the history of the
    record, $a_4 = x_4$, $b_4 = e^{4x_4/3}$ (with $H = 1$, $z = \pi/4$): as 3-space
    inflates, the 3-space derivatives are weighted less and less ($e^{-a_4}$), and as
    the hidden block deflates, the hidden and the extra-time derivatives are weighted
    more and more ($e^{a_4}b_4^{-1/2} = e^{x_4/3}$ times $\tan z$ or $1/W$). On the
    right, versus $z$ across one cell at $x_4 = 0$: the hidden factor $|\tan z|$, which
    grows without bound at the fold, and the factor $1/W = (\sin^2 z)^{-1/12}$ of the
    extra times, which grows slowly towards the ends of the cell.
    """),
    code(r'''
    fig, (ax_left, ax_right) = plt.subplots(1, 2, figsize=(10.0, 4.2))
    coefficient = [sp.lambdify(X4_SYMBOL, explicit_warp((1 / fa).subs(history)).subs(
        {H: 1, x0: sp.pi / 24})) for fa in f]
    ax_left.semilogy(times, coefficient[1](times),
                     label="$1/f_1 = e^{-a_4}$ (3-space derivatives)")
    ax_left.semilogy(times, coefficient[0](times), "--",
                     label="$1/f_0 = e^{a_4}b_4^{-1/2}\\tan z$ (hidden derivative)")
    ax_left.semilogy(times, coefficient[5](times), "-.",
                     label="$1/f_5 = e^{a_4}b_4^{-1/2}/W$ (extra-time derivatives)")
    ax_left.semilogy(times, np.ones_like(times), ":", color="black",
                     label="$1/f_4 = 1$ (time derivative)")
    ax_left.set_xlabel("time $x_4$ (units $1/H$), history $a_4 = x_4$, "
                       "$b_4 = e^{4x_4/3}$")
    ax_left.set_ylabel("factor in front of the derivative (log axis)")
    ax_left.set_title("Where the deflation enters the field equation")
    ax_left.legend(fontsize=7)
    zz = np.linspace(0.03, np.pi - 0.03, 600)  # one cell
    ax_right.semilogy(zz, np.abs(np.tan(zz)), label="$|1/f_0| = |\\tan z|$ (hidden)")
    ax_right.semilogy(zz, np.abs(np.sin(zz)) ** (-1 / 6), "--",
                      label="$1/W = (\\sin^2 z)^{-1/12}$ (extra times)")
    ax_right.axvline(np.pi / 2, color="gray", linewidth=0.8)  # the fold
    ax_right.set_xlabel("hidden angle $z = 6Hx_0$ (radians), fold at $\\pi/2$")
    ax_right.set_ylabel("factor at $x_4 = 0$ (log axis)")
    ax_right.set_title("Dependence on the hidden direction")
    ax_right.legend(fontsize=8, loc="upper left")
    save_figure(fig, "derivative_coefficients",
                "The factors $1/f_a$ in front of the derivatives in the Dirac operator "
                "$\\gamma^\\mu D_\\mu = \\sum_a f_a^{-1}\\gamma^{(a)}\\partial_a + "
                "c_g\\gamma^{(x0)} + v_g\\gamma^{(x4)}$. Left: versus the time $x_4$ in "
                "units $1/H$ at $z = \\pi/4$ on the history of the Revision record "
                "$a_4 = x_4$, $b_4 = e^{4x_4/3}$, on a logarithmic axis: the 3-space "
                "factor $e^{-a_4}$ falls, while the hidden factor $e^{a_4}b_4^{-1/2}"
                "\\tan z$ and the extra-time factor $e^{a_4}b_4^{-1/2}/W$ rise like "
                "$e^{x_4/3}$; this is how the deflation of the hidden block enters the "
                "field equation. Right: versus the hidden angle $z$ in radians at "
                "$x_4 = 0$ across one cell: the hidden factor $|\\tan z|$, unbounded at "
                "the fold (vertical line), and the factor $(\\sin^2 z)^{-1/12}$ of the "
                "extra times.")
    '''),
    md(r"""
    ## 15. The negative control: a hidden block that GROWS

    Does the result really see the direction in which the hidden block changes? The
    control answers this. The next cell repeats the whole computation (Christoffel
    symbols, spin connection, spinor connection, curved gammas) for a changed metric in
    which the hidden direction and the extra times grow with $e^{+a_4}$, like 3-space:
    $g_{00} = e^{+2a_4}b_4\cot^2 z$ and $g_{tt} = -e^{+2a_4}b_4W^2$ for $t = x5, x6, x7$,
    with vielbein factors $e^{+a_4}b_4^{1/2}\cot z$ and $e^{+a_4}b_4^{1/2}W$ (as in the
    lead's record: only the sign of $a_4$ in the hidden block is changed). Then the four
    directions of the hidden block have the rate $b_4'/(2b_4) + a_4'$, and the
    coefficient of $\gamma^{(x4)}$ should be $4\cdot\frac12\big(\frac{b_4'}{2b_4} +
    a_4'\big) + 3\cdot\frac12a_4' = \frac{b_4'}{b_4} + \frac72a_4'$, while the
    coefficient of $\gamma^{(x0)}$ should follow the new scale factor,
    $\frac32He^{-a_4}b_4^{-1/2}$. The record of the lead's independent check finds
    exactly these; the cell checks that it gets the same.
    """),
    code(r'''
    f_control = ([sp.exp(a4) * sp.sqrt(b4) * sp.cot(z)] + [sp.exp(a4)] * 3
                 + [sp.Integer(1)] + [sp.exp(a4) * sp.sqrt(b4) * W(x0)] * 3)  # GROWING
    g_control = sp.diag(*[ETA[a] * f_control[a] ** 2 for a in range(8)])
    e_control = sp.diag(*f_control)
    Gam_control = christoffel(g_control, x)
    omega_control = spin_connection(e_control, Gam_control, x, ETA)
    Omega_control = spinor_connection(omega_control, S)
    gup_control = curved_gammas(e_control, gamma)
    slash_control = sum((gup_control[mu] * Omega_control[mu] for mu in range(8)), Z16)
    alpha_control = sp.simplify(-(slash_control * gamma[4]).trace() / 16)
    beta_control = sp.simplify((slash_control * gamma[0]).trace() / 16)
    report("control: coefficient of gamma^(x4)", alpha_control)
    report("control: coefficient of gamma^(x0)", beta_control)
    lead = json.loads(repository_file(REPORT_LEAD).read_text(encoding="utf-8"))
    detail = [c["detail"] for c in lead["checks"]
              if c["name"] == "negative_control_growing_block"][0]
    check(matrix_is_zero(slash_control - alpha_control * gamma[4] - beta_control * gamma[0])
          and is_zero(alpha_control - b4p / b4 - sp.Rational(7, 2) * a4p)
          and is_zero(beta_control - sp.Rational(3, 2) * H * sp.exp(-a4) / sp.sqrt(b4))
          and "+7/2 instead of -1/2" in detail
          and record_passed(REPORT_LEAD, "negative_control_growing_block"),
          "control with a growing hidden block: (b4'/b4 + (7/2) a4') gamma^(x4) + "
          "(3/2) H e^(-a4) b4^(-1/2) gamma^(x0)",
          record=f"{REPORT_LEAD}, check negative_control_growing_block")
    '''),
    md(r"""
    The next cell draws the result of the control next to the author's case. On the
    left, the part of the coefficient of $\gamma^{(x4)}$ that is proportional to $a_4'$
    as a function of the rate $a_4'$ (the part $b_4'/b_4$ is the same in both cases):
    $-\frac12a_4'$ for the author's deflating block, $+\frac72a_4'$ for the growing
    control, two straight lines through the origin. On the right, the coefficient of
    $\gamma^{(x0)}$ versus the time on the history of the record ($H = 1$): it follows
    the inverse scale factor of the hidden block, $\frac32e^{x_4/3}$ for the author's
    metric (the block shrinks like $e^{-x_4/3}$) and $\frac32e^{-5x_4/3}$ for the
    control (the block grows like $e^{5x_4/3}$).
    """),
    code(r'''
    rates = np.linspace(-2.0, 2.0, 81)  # values of a4'
    rate_symbol = sp.Symbol("rate")
    author_alpha = sp.lambdify(rate_symbol, sp.simplify(v_g.subs(b4p, 0)).subs(
        a4p, rate_symbol))  # the part with a4'
    control_alpha = sp.lambdify(rate_symbol, sp.simplify(alpha_control.subs(
        b4p, 0)).subs(a4p, rate_symbol))
    fig, (ax_left, ax_right) = plt.subplots(1, 2, figsize=(10.0, 4.2))
    ax_left.plot(rates, np.broadcast_to(author_alpha(rates), rates.shape),
                 label="author: deflating hidden block ($-a_4'/2$)")
    ax_left.plot(rates, np.broadcast_to(control_alpha(rates), rates.shape), "--",
                 label="control: growing hidden block ($+7a_4'/2$)")
    ax_left.set_xlabel("rate $a_4'$ (units of $H$)")
    ax_left.set_ylabel("$a_4'$ part of the $\\gamma^{(x4)}$ coefficient (units of $H$)")
    ax_left.set_title("The time-direction term")
    ax_left.legend(fontsize=8)
    history_numbers = {H: 1, x4: X4_SYMBOL}
    author_beta = sp.lambdify(X4_SYMBOL, c_g.subs(history_values).subs(history_numbers))
    control_beta = sp.lambdify(X4_SYMBOL, beta_control.subs(history_values).subs(
        history_numbers))
    ax_right.semilogy(times, author_beta(times), label="author: $\\frac{3}{2} e^{x_4/3}$")
    ax_right.semilogy(times, control_beta(times), "--",
                      label="control: $\\frac{3}{2} e^{-5x_4/3}$")
    ax_right.set_xlabel("time $x_4$ (units $1/H$), history $a_4 = x_4$, "
                        "$b_4 = e^{4x_4/3}$")
    ax_right.set_ylabel("coefficient of $\\gamma^{(x0)}$ (units of $H$, log axis)")
    ax_right.set_title("The hidden-direction term")
    ax_right.legend(fontsize=8)
    save_figure(fig, "negative_control",
                "The negative control. Left: the part proportional to $a_4'$ of the "
                "coefficient of $\\gamma^{(x4)}$ in $\\gamma^\\mu\\Omega_\\mu$ versus the "
                "rate $a_4'$, both in units of $H = 1$, for the corrected metric, whose "
                "hidden block deflates (solid, the line $-a_4'/2$), and for a control "
                "metric whose hidden block grows like 3-space (dashed, the line "
                "$+7a_4'/2$); the part $b_4'/b_4$ is the same in both. Right: the "
                "coefficient of $\\gamma^{(x0)}$ versus the time $x_4$ on the history "
                "$a_4 = x_4$, $b_4 = e^{4x_4/3}$ on a logarithmic axis: "
                "$\\frac32e^{x_4/3}$ for the author's metric and "
                "$\\frac32e^{-5x_4/3}$ for the control, in both cases $\\frac32H$ "
                "divided by the scale factor of the hidden block. The term sees in "
                "which direction the hidden block changes.")
    '''),
    md(r"""
    ## 16. The last checks

    Most results of this notebook are recorded several times in the Revision record, by
    verifiers that share no code: the sympy checker (report `python-field-theory.json`),
    the WolframScript checker (`wolfram-field-theory.json`) and the lead's independent
    check (`emt-divergence-and-spin-connection.json`), all three for the corrected
    metric. Each PASS line above names one of them. The last cell lists every check of
    these three reports that states a result reproduced here and checks that each is
    recorded as passed (so the record this notebook reproduces is itself a passing
    record). Then it checks that all ten figure files exist in the folder
    Revision/textbook/figures, and prints the number of checks that passed.
    """),
    code(r'''
    cited = {
        REPORT_PY: ["clifford_relations", "gammas_real", "metric_from_vielbein_equals_SPEC",
                    "sqrt_det_g", "christoffel_symmetric_metric_compatible",
                    "vielbein_postulate", "spin_connection_antisymmetric",
                    "spinor_connection_real", "nontriviality_Omega_zero_iff_flat",
                    "Omega_x4_vanishes_Omega_x0_does_not",
                    "covariant_constancy_D_mu_gamma_nu",
                    "gamma_mu_Omega_mu_equals_hidden_block_terms", "per_direction_terms",
                    "gravity_term_square", "anticommutator_gamma_Omega_vanishes",
                    "divergence_of_sqrtg_gamma"],
        REPORT_WL: ["metric_is_the_corrected_metric", "vielbein_inverse", "sqrt_det_g",
                    "christoffel_count", "vielbein_postulate", "omega_antisymmetric",
                    "omega_components", "Omega_components", "S_rotates_gamma_with_omega",
                    "gamma_covariantly_constant", "gammaOmega_total",
                    "gammaOmega_per_direction", "gammaOmega_divergence_form",
                    "Dirac_operator_explicit_C", "Dirac_operator_explicit_G",
                    "nontriviality_1_dirac16complex", "nontriviality_2_dirac16complex00",
                    "Omega_vanishes_iff_a4prime_b4prime_and_H_vanish", "block_form"],
        REPORT_LEAD: ["fixture_clifford", "vielbein_reproduces_metric",
                      "gamma_Omega_equals_hidden_block_terms",
                      "gamma_Omega_divergence_formula", "negative_control_growing_block"],
    }
    count = sum(len(names) for names in cited.values())
    check(all(record_passed(path, name) for path, names in cited.items()
              for name in names),
          f"the {count} cited record checks are recorded as passed")
    expected = [f"06a_{k}_{name}.png" for k, name in enumerate([
        "polar_frame_and_spin_rotation", "vielbein_factors", "christoffel_pattern",
        "omega_heat_maps", "spinor_connection_heat_maps", "gamma_omega_per_direction",
        "gamma_omega_sum", "divergence_form", "derivative_coefficients",
        "negative_control"], 1)]
    check(all(output_file(f"{FIGURE_FOLDER}/{name}").is_file() for name in expected),
          "all ten figure files exist")
    all_checks_passed()
    '''),
    md(r"""
    ## 17. What this notebook showed

    - In the flat plane in polar coordinates the spin connection is not zero
      ($\omega_{\varphi 01} = -1$, $\gamma^\mu\Omega_\mu = \sigma_1/(2r)$), but its
      curvature is zero and a spinor rotation removes it: in flat space the spin
      connection only records how the chosen frame turns.
    - For the corrected metric the diagonal vielbein $f = (s_b\cot z,\ e^{a_4}\
      (\times 3),\ 1,\ s_bW\ (\times 3))$, $s_b = e^{-a_4}b_4^{1/2}$, $W =
      (\sin^2 z)^{1/12}$, gives the metric back for every real $z$ away from the
      degenerate points, and $\sqrt{|\det g|} = e^{-a_4}b_4^2|\cot z|(\sin^2 z)^{1/4}$
      (PROVED, exact; reproduces the record).
    - The metric has 21 independent nonzero Christoffel symbols, and the canonical spin
      connection has 10 independent nonzero components $\omega_{\mu ab}$, each equal to
      a rate ($a_4'$, $h_4 = b_4'/(2b_4) - a_4'$ or $H$) times a factor that never
      vanishes between the degenerate points; the vielbein postulate (512 equations),
      the antisymmetry and the covariant constancy of the gammas (64 matrix equations)
      hold exactly (PROVED; reproduces the records).
    - $\gamma^\mu\Omega_\mu = \frac32He^{a_4}b_4^{-1/2}\gamma^{(x0)} + (b_4'/b_4 -
      a_4'/2)\gamma^{(x4)}$ exactly, for every $H > 0$, all functions $a_4(x_4)$,
      $b_4(x_4) > 0$ and every real $z$ (PROVED; reproduces the Python, Wolfram and
      lead records): the time-direction terms $+\frac12a_4'$ of the three 3-space
      directions and $\frac12h_4$ of the four directions of the hidden block add to
      $v_g$, half the rate of the 7-volume $e^{-a_4}b_4^2$; the three extra times,
      warped along $x0$, add $\frac12He^{a_4}b_4^{-1/2}$ each. On the history of the
      record it is $\frac32He^{Hx_4/3}\gamma^{(x0)} + \frac56H\gamma^{(x4)}$: its hidden
      part grows as the hidden block deflates.
    - The Dirac operator is $\sum_a f_a^{-1}\gamma^{(a)}\partial_a + c_g\gamma^{(x0)} +
      v_g\gamma^{(x4)}$; all 16 component equations equal the records. The deflation
      also enters through the factors $e^{\mp a_4}$ and $e^{a_4}b_4^{-1/2}$ in front of
      the derivatives.
    - The term vanishes for a nonzero field only where $c_g = \pm v_g$, because its
      square is $(c_g^2 - v_g^2)\,1$; on the history this happens at the single time
      $x_4 = 3\ln(5/9)/H$, where $M$ has rank 8.
    - NEGATIVE CONTROL: with a growing hidden block the coefficient of $a_4'$ in the
      time term is $+\frac72$ instead of $-\frac12$ and the hidden term is
      $\frac32He^{-a_4}b_4^{-1/2}$ (reproduces the lead's record): the term sees the
      direction in which the hidden block changes.
    - Scope (stated by the record and shown in Notebook 06b): the value of
      $\gamma^\mu\Omega_\mu$ belongs to the diagonal vielbein and the variable $\Psi$;
      a boosted vielbein removes its $c_g$ part, a rescaling of the field removes all
      of it, while the curvature of the metric, where it is not zero, can be removed by
      nothing.
    """),
]

if __name__ == "__main__":
    raise SystemExit(run_builder(__file__))
