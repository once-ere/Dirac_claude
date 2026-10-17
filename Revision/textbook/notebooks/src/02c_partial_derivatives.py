#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
"""Builder of Notebook 02c, "Partial derivatives" (textbook "Universes in Pairs").

The notebook Revision/textbook/notebooks/02c_partial_derivatives.ipynb is BUILT from
this file by Revision/textbook/tools/nbkit.py (never edit the .ipynb by hand):

    python Revision/textbook/tools/nbkit.py build \
        Revision/textbook/notebooks/src/02c_partial_derivatives.py --date YYYY-MM-DD
    python Revision/textbook/tools/nbkit.py check \
        Revision/textbook/notebooks/src/02c_partial_derivatives.py

Chapter 02, example c: functions of several variables.  Partial derivatives with sympy
and by finite differences (orders 1 and 2, the rounding limit), level curves and the
gradient, Schwarz's theorem, the chain rule for z = 6 H x0, and the partial derivatives
of the author's corrected metric (version 2 of 2026-10-16) read from the Revision record
Revision/gkd_lovelock/results/curvature.json: the logarithmic rates of the eight scale
factors (along the record's prescribed history a4 = H x4, b4 = e^((4/3) H x4) of
Revision/kohn_sham/results/parameters.json), their mirror property under z -> pi - z,
the volume factor sqrt|det g| = e^(-a4) b4^2 |cot z| (sin^2 z)^(1/4) (also the Wolfram
check sqrt_abs_det_g of Revision/field_equations_a4/reports/wolfram-a4-report.json),
Jacobi's formula, and all 21 nonzero Christoffel entries of the record.  Every exact
comparison is made on the four quarters of the period of z separately.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools"))
from nbkit import code, md, run_builder  # noqa: E402

FIGURES = [
    "02c_1_level_curves_gradient",
    "02c_2_slices_and_slopes",
    "02c_3_finite_differences",
    "02c_4_chain_rule",
    "02c_5_rates_along_x4",
    "02c_6_rates_along_x0",
]

FACTS = {
    "id": "02c",
    "name": "02c_partial_derivatives",
    "title": "Partial derivatives, finite differences and the chain rule",
    "purpose": (
        "It computes partial derivatives of a function of two variables with sympy "
        "and by finite differences (forward and central differences, their orders 1 "
        "and 2 and the limit set by rounding), draws level curves with the gradient "
        "and slices with their tangent lines, checks that mixed partial derivatives "
        "do not depend on the order, checks the chain rule for the author's variable "
        "z = 6 H x0, and then reads the author's corrected metric (version 2 of "
        "2026-10-16) from a Revision record and computes its partial derivatives: the "
        "growth and deflation rates of the eight scale factors, evaluated along the "
        "prescribed history of the Revision record (a4 = H x4, b4 = e^((4/3) H x4)), "
        "their change of sign under z -> pi - z, the volume factor sqrt of the "
        "absolute determinant, equal to e^(-a4) b4^2 |cot z| (sin^2 z)^(1/4), which "
        "grows with the time, Jacobi's formula, and all 21 nonzero Christoffel entries "
        "listed in the record. Every exact comparison is made on each of the four "
        "quarters of the period of z."
    ),
    "records": [
        ["Revision/gkd_lovelock/results/curvature.json",
         "the author's corrected metric (key metricDiagonal), its volume factor (key "
         "sqrtAbsDetG) and its nonzero Christoffel symbols (key "
         "christoffelNonzero_b_le_c), read and reproduced"],
        ["Revision/field_equations_a4/reports/wolfram-a4-report.json",
         "the Wolfram check sqrt_abs_det_g, reproduced"],
        ["Revision/kohn_sham/results/parameters.json",
         "the prescribed history of the record (keys historyA, historyBeta, "
         "historyB4AtZero and H) and its growth rule of the proper 7-volume (key "
         "Vol7Rule), read and reproduced"],
    ],
    "packages": ["numpy", "sympy", "matplotlib"],
    "needs_rust": [],
    "expected_seconds": 15,
    "timeout_seconds": 300,
    "files_written": ["Revision/textbook/figures/02c.captions.json"]
    + [f"Revision/textbook/figures/{name}.png" for name in FIGURES],
    "final_lines": [
        "PASS all 6 figure files of notebook 02c exist",
        "ALL 20 CHECKS PASSED (notebook 02c)",
    ],
    "troubleshooting": [
    ],
}

CELLS = [
    md(r"""
    ## 1. What this notebook computes

    The quantities of this book depend on several variables at once: the author's
    metric depends on the time $x_4$ and on the hidden coordinate $x_0$. This
    notebook teaches how to differentiate such functions and checks every step. It

    - computes the partial derivatives of $f(x, y) = x^2 \sin y$ with sympy, checks
      that the two mixed second derivatives agree, and draws the level curves of $f$
      with its gradient arrows and two slices with their tangent lines;
    - approximates partial derivatives by finite differences and measures their
      orders (1 for the forward difference, 2 for the central one) and the limit
      that rounding errors set;
    - checks the chain rule for the author's variable $z = 6 H x_0$;
    - reads the author's corrected metric (version 2 of 2026-10-16) from the
      Revision record Revision/gkd_lovelock/results/curvature.json and computes its
      partial derivatives: the growth rates of the eight scale factors along $x_4$
      (evaluated along the prescribed history of the Revision record,
      $a_4 = H x_4$, $b_4 = e^{(4/3) H x_4}$) and along $x_0$, the volume factor
      $\sqrt{|\det g|} = e^{-a_4} b_4^2 |\cot z| (\sin^2 z)^{1/4}$ (which GROWS
      with $x_4$ along that history), Jacobi's formula for the derivative of a
      determinant, and all 21 nonzero *Christoffel symbols* listed in the record
      (combinations of first partial derivatives of the metric that the geometry of
      the book uses).

    It draws 6 figures and prints a PASS line for every check.
    """),
    md(r"""
    ## 3. The words used in this notebook

    - **Function of several variables**: a rule $f(x, y)$ that gives a number for
      every pair of numbers $(x, y)$ (or for every list $x_0, \dots, x_7$).
    - **Partial derivative** $\partial f/\partial x$: the ordinary derivative with
      respect to $x$ while all the other variables are held fixed. We also write
      $\partial_x f$, and for the author's coordinates $\partial_4 = \partial/\partial
      x_4$ and $\partial_0 = \partial/\partial x_0$.
    - **Slice**: the function of ONE variable obtained by holding the others fixed;
      the partial derivative is the slope of its graph.
    - **Level curve (contour)**: the set of points where $f$ has one fixed value.
    - **Gradient**: the arrow $(\partial f/\partial x, \partial f/\partial y)$. It
      points in the direction in which $f$ grows fastest and is perpendicular to the
      level curve through its point.
    - **Mixed partial derivative**: $\partial^2 f/\partial x \partial y$, first with
      respect to $y$, then $x$ (or the other way round). Schwarz's theorem: for a
      function with continuous second derivatives the order does not matter.
    - **Chain rule**: if $f$ depends on $z$ and $z$ on $x_0$, then
      $\partial f/\partial x_0 = (df/dz)(\partial z/\partial x_0)$.
    - **Finite difference**: an approximation of a derivative from values of the
      function at nearby points, with a small spacing $h$.
    - **Metric, diagonal entries** $g_{aa}$: the eight numbers (functions of $x_4$ and
      $x_0$) that turn coordinate distances into true distances in the author's
      8-dimensional world; positive for the space directions $x_0, x_1, x_2, x_3$ and
      negative for the time directions $x_4, x_5, x_6, x_7$.
    - **Scale factor** $s_a = \sqrt{|g_{aa}|}$: the factor by which a coordinate
      length along $x_a$ is multiplied to give a true length.
    - **Positive branch** $(\sin^2 z)^{1/6}$: the positive sixth root of the
      positive number $\sin^2 z$; it equals $|\sin z|^{1/3}$.
    - **Quarter of the period**: $z$ takes every real value; the metric repeats
      when $z$ grows by $\pi$, and each interval between neighbouring points with
      $\sin z \cos z = 0$ is a quarter of the period $2\pi$ of $\sin z$; on it
      $\sin z$ and $\cos z$ keep their signs.
    - **Logarithmic derivative** $\partial \ln s/\partial x = (\partial s/\partial
      x)/s$: the rate of growth of $s$ per unit of $x$, as a fraction of $s$
      itself.
    - **Determinant of a diagonal matrix**: the product of its diagonal entries.
    - **Christoffel symbols** $\Gamma^a{}_{bc}$: numbers built from first partial
      derivatives of the metric; the geometry of the book explains their meaning.
      Here they are only an exercise in partial derivatives.
    """),
    md(r"""
    ## 4. The physical and mathematical situation

    **Definition.** For a function $f(x, y)$,

    $$\frac{\partial f}{\partial x}(x, y) = \lim_{h \to 0}
    \frac{f(x + h, y) - f(x, y)}{h},$$

    the derivative of the slice $x \mapsto f(x, y)$ with $y$ held fixed; likewise for
    $y$. All the rules of one-variable calculus hold for each partial derivative.

    **The first example.** $f(x, y) = x^2 \sin y$. Holding $y$ fixed, $\sin y$ is a
    constant factor and $\partial f/\partial x = 2x \sin y$. Holding $x$ fixed,
    $x^2$ is a constant factor and $\partial f/\partial y = x^2 \cos y$. Then
    $\partial/\partial y$ of $2x \sin y$ is $2x \cos y$ and $\partial/\partial x$ of
    $x^2 \cos y$ is also $2x \cos y$: the mixed derivatives agree, as Schwarz's
    theorem says.

    **Finite differences.** Taylor's theorem in one variable gives
    $f(x + h) = f(x) + h f'(x) + \frac{h^2}{2} f''(x) + \frac{h^3}{6} f'''(x) +
    \dots$ Therefore the *forward difference* $(f(x + h) - f(x))/h = f'(x) +
    \frac{h}{2} f''(x) + \dots$ has an error proportional to $h$ (order 1), and the
    *central difference* $(f(x + h) - f(x - h))/(2h) = f'(x) + \frac{h^2}{6}
    f'''(x) + \dots$ has an error proportional to $h^2$ (order 2), because the
    terms with $h^2 f''$ cancel in the difference. Rounding adds an error of about
    $\epsilon |f| / h$ ($\epsilon = 2.2 \times 10^{-16}$), which GROWS as $h$
    shrinks; the best $h$ balances the two.

    **The author's metric** (the corrected metric, version 2 of 2026-10-16;
    coordinates $x_0, \dots, x_7$; $z = 6 H x_0$ takes every real value;
    $a_4(x_4)$ and $b_4(x_4) > 0$ are functions of the time, and $b_4$ is never the
    constant 1):

    $$g_{00} = e^{-2 a_4} b_4 \cot^2 z, \quad g_{11} = g_{22} = g_{33} = e^{2 a_4},
    \quad g_{44} = -1, \quad g_{55} = g_{66} = g_{77} = -e^{-2 a_4} b_4
    (\sin^2 z)^{1/6} .$$

    It is used where $\sin z \cos z \neq 0$: at $\cos z = 0$ (the *fold*
    $z = \pi/2$, which joins the two halves of a cell) $g_{00}$ vanishes. The scale
    factors are $s_0 = e^{-a_4} b_4^{1/2} |\cot z|$ for the hidden direction $x_0$,
    $s_{1,2,3} = e^{a_4}$ for 3-space ($x_1, x_2, x_3$; no factor of $z$),
    $s_4 = 1$ for the time $x_4$ and $s_{5,6,7} = e^{-a_4} b_4^{1/2}
    (\sin^2 z)^{1/12}$ for the three extra times $x_5, x_6, x_7$. The hidden
    direction and the extra times share the factor $e^{-a_4} b_4^{1/2}$: they
    shrink together. By the chain rule, $\partial_0 = (dz/dx_0)\, d/dz = 6H\, d/dz$
    on a function of $z$. The logarithms are $\ln s_{1,2,3} = a_4$,
    $\ln s_{5,6,7} = -a_4 + \frac{1}{2} \ln b_4 + \frac{1}{12} \ln \sin^2 z$ and
    $\ln s_0 = -a_4 + \frac{1}{2} \ln b_4 + \ln |\cot z|$, so

    $$\partial_4 \ln s_{1,2,3} = a_4', \quad
    \partial_4 \ln s_{0} = \partial_4 \ln s_{5,6,7} = -a_4' + \frac{b_4'}{2 b_4},
    \quad \partial_0 \ln s_{5,6,7} = \tfrac{1}{12} \cdot 6H \cdot 2 \cot z
    = H \cot z,$$

    $\partial_0 \ln s_{1,2,3} = 0$, and $\partial_0 \ln |\cot z| = 6H \cdot
    \frac{-1/\sin^2 z}{\cot z} = -\frac{6H}{\sin z \cos z}$ (the derivative of
    $\ln |u|$ is $u'/u$ for either sign of $u$). The determinant of the diagonal
    metric is the product of the entries; four of them are negative, so it is
    positive: $\det g = e^{-2 a_4} b_4 \cot^2 z\, (e^{2a_4})^3 (e^{-2a_4} b_4)^3
    ((\sin^2 z)^{1/6})^3 = e^{-2 a_4} b_4^4 \cot^2 z\, (\sin^2 z)^{1/2}$ and
    $\sqrt{|\det g|} = e^{-a_4} b_4^2 |\cot z| (\sin^2 z)^{1/4}$. The factors
    $e^{6 a_4}$ of 3-space and $e^{-6 a_4}$ of the extra times cancel, but the
    hidden factor $e^{-2a_4} b_4$ and the factor $b_4^3$ of the extra times remain:
    $\partial_4 \ln \sqrt{|\det g|} = -a_4' + 2 b_4'/b_4$, and the volume factor
    changes with $x_4$. Along the prescribed history of the Revision record,
    $a_4 = A H x_4$ and $b_4 = e^{(4/3) A H x_4}$ with $A = H = 1$, this rate is
    $-1 + 8/3 = 5/3$: the volume grows.

    **Christoffel symbols of a diagonal metric.** We take the formula
    $\Gamma^a{}_{bc} = \frac{1}{2 g_{aa}} (\partial_b g_{ac} + \partial_c g_{ab} -
    \partial_a g_{bc})$ (no sum over $a$) as given; the geometry of the book
    derives it. For a diagonal metric only two kinds of entry can be nonzero:
    $\Gamma^a{}_{ac} = \partial_c g_{aa}/(2 g_{aa}) = \partial_c \ln s_a$, the
    logarithmic rates above, and $\Gamma^c{}_{aa} = -\partial_c g_{aa}/(2 g_{cc})$
    for $c \neq a$.
    """),
    md(r"""
    ## 5. The set-up of this notebook

    The next cell imports the packages, chooses the colours of the plots and
    defines the sympy symbols $x$, $y$ of the first example.
    """),
    code(r'''
    import math  # functions of single numbers

    import numpy as np  # arrays of numbers
    import sympy as sp  # exact algebra and calculus with symbols

    BLUE, ORANGE, AQUA, VIOLET = "#2a78d6", "#eb6834", "#1baf7a", "#4a3aa7"
    GREY, BLACK = "#8a8986", "#000000"
    x, y = sp.symbols("x y", real=True)  # the two variables of the first example
    say("Packages imported; symbols x and y defined.")
    '''),
    md(r"""
    ## 6. Partial derivatives with sympy

    `sp.diff(f, x)` differentiates with respect to $x$ and treats every other
    symbol as a constant: exactly the definition of a partial derivative. The cell
    prints the two first derivatives and the two mixed second derivatives of
    $f = x^2 \sin y$, checks them against the hand calculation of section 4, and
    evaluates everything at the point $(x_0, y_0) = (1.2, 0.7)$.
    """),
    code(r'''
    f = x ** 2 * sp.sin(y)
    f_x = sp.diff(f, x)  # hold y fixed
    f_y = sp.diff(f, y)  # hold x fixed
    f_xy = sp.diff(f, x, y)  # first x, then y
    f_yx = sp.diff(f, y, x)  # first y, then x
    say(f"df/dx = {f_x},  df/dy = {f_y}")
    say(f"d2f/dxdy = {f_xy},  d2f/dydx = {f_yx}")
    check(sp.simplify(f_x - 2 * x * sp.sin(y)) == 0
          and sp.simplify(f_y - x ** 2 * sp.cos(y)) == 0,
          "df/dx = 2 x sin y and df/dy = x^2 cos y")
    check(sp.simplify(f_xy - f_yx) == 0 and sp.simplify(f_xy - 2 * x * sp.cos(y)) == 0,
          "the mixed derivatives agree (Schwarz): both are 2 x cos y")
    X0, Y0 = 1.2, 0.7  # the point at which we evaluate
    at_point = {x: X0, y: Y0}
    for label, expression in (("f", f), ("df/dx", f_x), ("df/dy", f_y),
                              ("d2f/dxdy", f_xy)):
        report(f"{label} at (1.2, 0.7)", f"{float(expression.subs(at_point)):.12f}")
    '''),
    md(r"""
    ## 7. Pictures of a function of two variables

    The first figure is a map of $f$: coloured bands between level curves, and at
    the points of a coarse grid the gradient arrow $(\partial f/\partial x,
    \partial f/\partial y)$. `sp.lambdify` turns a sympy expression into a fast
    numpy function. The check confirms at one point that the gradient is
    perpendicular to the level curve: the direction along the level curve,
    $(-\partial f/\partial y, \partial f/\partial x)$, has zero dot product with the
    gradient, and moving a small step along it changes $f$ only in second order.
    A second check confirms that the gradient points uphill: a small step of length
    $10^{-4}$ along the unit arrow $\nabla f/|\nabla f|$, where
    $|\nabla f| = \sqrt{(\partial f/\partial x)^2 + (\partial f/\partial y)^2}$ is
    the length of the gradient, raises $f$ by about $10^{-4}\,|\nabla f|$ (the
    steepest slope), and such a step raises $f$ at every one of the 120 arrows of
    the figure.
    """),
    code(r'''
    F = sp.lambdify((x, y), f, "numpy")  # f as a numpy function
    FX = sp.lambdify((x, y), f_x, "numpy")
    FY = sp.lambdify((x, y), f_y, "numpy")
    xs = np.linspace(-2.0, 2.0, 201)
    ys = np.linspace(0.0, 2.0 * np.pi, 201)
    XX, YY = np.meshgrid(xs, ys)  # all grid points as two 2-dimensional arrays
    fig, ax = plt.subplots(figsize=(7.0, 5.2))
    bands = ax.contourf(XX, YY, F(XX, YY), levels=17, cmap="RdBu_r")  # coloured bands
    ax.contour(XX, YY, F(XX, YY), levels=17, colors=BLACK, linewidths=0.4)
    fig.colorbar(bands, ax=ax, label="$f(x, y) = x^2 \\sin y$")
    xq, yq = np.meshgrid(np.linspace(-1.8, 1.8, 10), np.linspace(0.3, 6.0, 12))  # coarse
    # an arrow (df/dx, df/dy) at every coarse grid point; scale=40 shortens all arrows
    ax.quiver(xq, yq, FX(xq, yq), FY(xq, yq), color=BLACK, scale=40, width=0.004)
    ax.set_xlabel("$x$")
    ax.set_ylabel("$y$")
    ax.set_title("Level curves of $f = x^2 \\sin y$ and its gradient arrows")
    save_figure(fig, "level_curves_gradient",
                "A map of the function $f(x, y) = x^2 \\sin y$ for $x$ from $-2$ to $2$ "
                "(horizontal axis) and $y$ from $0$ to $2\\pi$ (vertical axis); all "
                "quantities are pure numbers. The colour shows the value of $f$ (red "
                "positive, blue negative), the thin black lines are level curves, and "
                "the arrows are the gradient $(\\partial f/\\partial x, \\partial "
                "f/\\partial y)$ at a grid of points. Every arrow points uphill and "
                "crosses the level curves at a right angle; long arrows mean a steep "
                "slope.")
    gx, gy = float(f_x.subs(at_point)), float(f_y.subs(at_point))
    tangent = np.array([-gy, gx]) / math.hypot(gx, gy)  # along the level curve
    step = 1e-4
    change = F(X0 + step * tangent[0], Y0 + step * tangent[1]) - F(X0, Y0)
    report("change of f along the level curve for a step of 1e-4", f"{change:.2e}")
    check(abs(gx * tangent[0] + gy * tangent[1]) < 1e-15 and abs(change) < 1e-7,
          "the gradient is perpendicular to the level curve")

    length = math.hypot(gx, gy)  # the length |grad f| of the gradient arrow
    rise = F(X0 + step * gx / length, Y0 + step * gy / length) - F(X0, Y0)
    report("rise of f per unit length along the gradient, |grad f|",
           f"{rise / step:.6f}, {length:.6f}")
    gxq, gyq = FX(xq, yq), FY(xq, yq)  # the arrows of the figure
    lengths = np.hypot(gxq, gyq)
    rises = F(xq + step * gxq / lengths, yq + step * gyq / lengths) - F(xq, yq)
    check(abs(rise / step / length - 1) < 1e-3 and np.all(rises > 0),
          "the gradient points uphill: f rises at the rate |grad f| along it")
    '''),
    md(r"""
    The second figure shows what a partial derivative IS: the slope of a slice. On
    the left, $y = y_0 = 0.7$ is held fixed and $f$ is drawn as a function of $x$; on
    the right, $x = x_0 = 1.2$ is held fixed and $f$ is drawn as a function of $y$.
    The dashed lines through the point have the slopes $\partial f/\partial x$ and
    $\partial f/\partial y$ at $(x_0, y_0)$: they are the tangent lines of the
    slices.
    """),
    code(r'''
    fig, (left, right) = plt.subplots(1, 2, figsize=(9.0, 3.8))
    fig.subplots_adjust(wspace=0.3)  # room between the two panels
    f0 = F(X0, Y0)
    x_line = np.linspace(-0.5, 2.5, 200)
    left.plot(x_line, F(x_line, Y0), color=BLUE, lw=1.6,
              label="slice $f(x, 0.7)$")
    left.plot(x_line, f0 + gx * (x_line - X0), "--", color=ORANGE, lw=1.2,
              label=f"slope $\\partial f/\\partial x = {gx:.4f}$")
    left.set_xlabel("$x$ (with $y = 0.7$ fixed)")
    y_line = np.linspace(-0.6, 2.4, 200)
    right.plot(y_line, F(X0, y_line), color=BLUE, lw=1.6, label="slice $f(1.2, y)$")
    right.plot(y_line, f0 + gy * (y_line - Y0), "--", color=ORANGE, lw=1.2,
               label=f"slope $\\partial f/\\partial y = {gy:.4f}$")
    right.set_xlabel("$y$ (with $x = 1.2$ fixed)")
    for ax in (left, right):
        ax.plot([X0 if ax is left else Y0], [f0], "o", color=BLACK, ms=6)
        ax.set_ylabel("$f$")
        ax.legend(fontsize=8)
    save_figure(fig, "slices_and_slopes",
                "Two slices of $f(x, y) = x^2 \\sin y$ through the point "
                "$(x_0, y_0) = (1.2, 0.7)$ (black dot); all quantities are pure "
                "numbers. Left: $f$ as a function of $x$ with $y = 0.7$ held fixed, "
                "and its tangent line (dashed) of slope $\\partial f/\\partial x = "
                "2 x_0 \\sin y_0 = 1.5461$. Right: $f$ as a function of $y$ with "
                "$x = 1.2$ held fixed, and its tangent line of slope $\\partial "
                "f/\\partial y = x_0^2 \\cos y_0 = 1.1014$. A partial derivative is "
                "the slope of a slice.")
    check(abs(gx - 2 * X0 * math.sin(Y0)) < 1e-15 and abs(gy - X0 ** 2 * math.cos(Y0))
          < 1e-15, "the slopes of the slices are 2 x0 sin y0 and x0^2 cos y0")
    '''),
    md(r"""
    ## 8. Finite differences: order and rounding

    The next cell approximates three derivatives at $(1.2, 0.7)$ for 49 spacings
    $h$ from $10^{-12}$ to $1$ (equally spaced in $\log h$):

    - forward difference for $\partial f/\partial y$: $(f(x_0, y_0 + h) -
      f(x_0, y_0))/h$;
    - central difference for $\partial f/\partial y$: $(f(x_0, y_0 + h) -
      f(x_0, y_0 - h))/(2h)$;
    - central difference for the mixed derivative $\partial^2 f/\partial x \partial
      y$: $[f(x_0{+}h, y_0{+}h) - f(x_0{+}h, y_0{-}h) - f(x_0{-}h, y_0{+}h) +
      f(x_0{-}h, y_0{-}h)]/(4h^2)$.

    It fits the slopes on the log-log plot where truncation dominates, and finds the
    best $h$ of each formula, where truncation and rounding balance.
    """),
    code(r'''
    exact_y = X0 ** 2 * math.cos(Y0)  # df/dy at the point
    exact_xy = 2 * X0 * math.cos(Y0)  # d2f/dxdy at the point
    h_values = np.logspace(-12, 0, 49)  # 1e-12 ... 1
    forward = np.array([(F(X0, Y0 + h) - F(X0, Y0)) / h for h in h_values])
    central = np.array([(F(X0, Y0 + h) - F(X0, Y0 - h)) / (2 * h) for h in h_values])
    mixed = np.array([(F(X0 + h, Y0 + h) - F(X0 + h, Y0 - h) - F(X0 - h, Y0 + h)
                       + F(X0 - h, Y0 - h)) / (4 * h * h) for h in h_values])
    err = {"forward": np.abs(forward - exact_y), "central": np.abs(central - exact_y),
           "mixed": np.abs(mixed - exact_xy)}
    RANGES = {"forward": (1e-5, 1e-2), "central": (1e-3, 1e-1), "mixed": (1e-2, 1e-1)}
    slope_of = {}
    for name, (low, high) in RANGES.items():
        part = (h_values >= low) & (h_values <= high)
        slope_of[name], _ = np.polyfit(np.log10(h_values[part]),
                                       np.log10(err[name][part]), 1)
        best = int(np.argmin(err[name]))
        report(f"{name}: slope {slope_of[name]:.3f}, best h", f"{h_values[best]:.1e} "
               f"(error {err[name][best]:.1e})")
    fig, ax = plt.subplots(figsize=(7.0, 5.0))
    styles = {"forward": (ORANGE, "s", "forward difference, $\\partial f/\\partial y$"),
              "central": (BLUE, "o", "central difference, $\\partial f/\\partial y$"),
              "mixed": (AQUA, "^", "central mixed, $\\partial^2 f/\\partial x "
                                   "\\partial y$")}
    for name, (color, marker, label) in styles.items():
        shown = err[name] > 0  # an exact zero cannot be drawn on a log axis
        ax.loglog(h_values[shown], err[name][shown], marker=marker, color=color, ms=4,
                  lw=1.0, label=label)
    ax.loglog(h_values, 2.2e-16 / h_values, ":", color=BLACK, lw=1.0,
              label="rounding scale $\\epsilon / h$")
    ax.loglog(h_values, 2.2e-16 / h_values ** 2, "-.", color=GREY, lw=1.0,
              label="rounding scale $\\epsilon / h^2$ (mixed)")
    ax.set_ylim(1e-14, 10.0)
    ax.set_xlabel("spacing $h$")
    ax.set_ylabel("error of the approximation")
    ax.set_title("Finite differences at $(1.2, 0.7)$: truncation against rounding")
    ax.legend(loc="lower left", fontsize=8)
    save_figure(fig, "finite_differences",
                "The error of three finite-difference approximations at the point "
                "$(1.2, 0.7)$ against the spacing $h$ from $10^{-12}$ to $1$, on "
                "logarithmic axes (pure numbers): forward difference for "
                "$\\partial f/\\partial y$ (squares), central difference for "
                "$\\partial f/\\partial y$ (circles) and the central formula for the "
                "mixed derivative (triangles), for $f = x^2 \\sin y$. Coming from the "
                "right, the errors fall with slope 1 (forward) and slope 2 (central, "
                "mixed). Coming from the left, rounding errors, of the size "
                "$\\epsilon / h$ (dotted) or $\\epsilon / h^2$ (dash-dotted) for the "
                "mixed formula, "
                "dominate. The best spacings are near $10^{-8}$, $10^{-6}$ and "
                "$10^{-4}$.")
    check(abs(slope_of["forward"] - 1) < 0.05 and abs(slope_of["central"] - 2) < 0.05
          and abs(slope_of["mixed"] - 2) < 0.05,
          "measured orders: forward 1, central 2, mixed central 2")
    check(err["central"].min() < 1e-10 < err["forward"].min() < 1e-7,
          "best central error < 1e-10 < best forward error < 1e-7")
    '''),
    md(r"""
    ## 9. The chain rule with $z = 6 H x_0$

    The author writes the hidden direction with $z = 6 H x_0$. A function of $z$,
    such as the factor $\cot^2 z$ of $g_{00} = e^{-2 a_4} b_4 \cot^2 z$, depends on
    $x_0$ through $z$, and the chain rule says $\partial_0 \cot^2(6 H x_0) = 6H
    \cdot \frac{d}{dz} \cot^2 z$. The cell checks it with sympy, and the figure
    shows it with $H = 1$: the same curve drawn against $z$ and against
    $x_0 = z/6$ is squeezed sideways by the factor 6, so every slope is 6 times
    steeper.
    """),
    code(r'''
    x4, x0 = sp.symbols("x4 x0", real=True)  # the time and the hidden coordinate
    H = sp.symbols("H", positive=True)  # the author's constant H > 0
    zs = sp.symbols("z", positive=True)  # z = 6 H x0 as a symbol of its own
    through_x0 = sp.diff(sp.cot(6 * H * x0) ** 2, x0)  # differentiate in x0 directly
    through_z = 6 * H * sp.diff(sp.cot(zs) ** 2, zs).subs(zs, 6 * H * x0)  # chain rule
    say(f"d/dx0 cot(6 H x0)^2 = {sp.simplify(through_x0)}")
    check(sp.simplify(through_x0 - through_z) == 0,
          "chain rule: d/dx0 of cot(6 H x0)^2 = 6 H times d/dz of cot(z)^2")

    z0 = 0.6  # the point z0 and the matching x0 = z0/6 (H = 1)
    slope_z = -2.0 * math.cos(z0) / math.sin(z0) ** 3  # d/dz cot^2 z = -2 cot z / sin^2 z
    fig, (left, right) = plt.subplots(1, 2, figsize=(9.0, 3.8))
    z_line = np.linspace(0.35, 1.5, 300)
    left.plot(z_line, 1 / np.tan(z_line) ** 2, color=BLUE, lw=1.6,
              label="$\\cot^2 z$")
    left.plot(z_line, 1 / math.tan(z0) ** 2 + slope_z * (z_line - z0), "--",
              color=ORANGE, label=f"tangent, slope {slope_z:.3f}")
    left.set_xlabel("$z$")
    x0_line = z_line / 6.0
    right.plot(x0_line, 1 / np.tan(6 * x0_line) ** 2, color=BLUE, lw=1.6,
               label="$\\cot^2(6 H x_0)$, $H = 1$")
    right.plot(x0_line, 1 / math.tan(z0) ** 2 + 6 * slope_z * (x0_line - z0 / 6), "--",
               color=ORANGE, label=f"tangent, slope $6 \\times$ {slope_z:.3f}")
    right.set_xlabel("$x_0$ (units $1/H$)")
    for ax, where in ((left, z0), (right, z0 / 6)):
        ax.plot([where], [1 / math.tan(z0) ** 2], "o", color=BLACK, ms=6)
        ax.set_ylim(0.0, 6.0)
        ax.set_ylabel("$\\cot^2 z$ (pure number)")
        ax.legend(fontsize=8)
    save_figure(fig, "chain_rule",
                "The chain rule for the author's hidden coordinate. Left: the factor "
                "$\\cot^2 z$ of $g_{00} = e^{-2 a_4} b_4 \\cot^2 z$ against $z$ from "
                "0.35 to 1.5, with its tangent line at $z = 0.6$. Right: the same "
                "function against $x_0 = z/(6H)$ with $H = 1$ ($x_0$ in units of "
                "$1/H$), with its tangent line at $x_0 = 0.1$. Both vertical axes show "
                "$\\cot^2 z$, a pure number. The right curve is the left one squeezed "
                "sideways by the factor 6, so its slope is 6 times steeper: "
                "$\\partial_0 = 6H\\, d/dz$.")
    '''),
    md(r"""
    ## 10. The author's metric, read from the Revision record

    The Rust program of the Revision record that computed the curvature of the
    author's corrected metric stored the metric's diagonal in the file
    Revision/gkd_lovelock/results/curvature.json, written in the notation of the
    Wolfram Language (`E^(...)` is $e^{\dots}$, `Sin[...]` is $\sin(\dots)$,
    `Sign[...]` is the sign, $+1$ or $-1$, `Derivative[1][a4][x4]` is $a_4'$). The
    function `from_record` translates such a text into a sympy expression: square
    brackets become round ones and `^` becomes `**`. sympy writes the positive
    branch $(\sin^2 z)^{1/6}$ as `Abs(sin(6*H*x0))**(1/3)`.

    sympy cannot always simplify expressions with absolute values. The function
    `same` therefore compares two expressions on each of the four quarters of the
    period of $z$ separately: on a quarter, $\sin z = \sigma S$ and
    $\cos z = \tau C$ with the positive numbers $S = |\sin z|$, $C = |\cos z|$ and
    fixed signs $\sigma, \tau = \pm 1$ (first quarter $+, +$; second $+, -$; third
    $-, -$; fourth $-, +$). It writes both expressions with $z$, turns $\cot$ and
    $\tan$ into quotients, expands $\sin 2z$ and $\cos 2z$ (sympy likes to write
    $2 \sin z \cos z$ as $\sin 2z$), puts in $\sigma S$ and $\tau C$ (now sympy
    knows $|\sigma S| = S$), simplifies, and if needed uses $S^2 + C^2 = 1$. Every
    real $z$ with $\sin z \cos z \neq 0$ lies inside one quarter, so a difference
    that vanishes on all four vanishes wherever the metric is defined. The cell
    compares the eight entries of the record with the formulas of section 4,
    typed in by hand.
    """),
    code(r'''
    CURVATURE = "Revision/gkd_lovelock/results/curvature.json"
    record = json.loads(repository_file(CURVATURE).read_text(encoding="utf-8"))
    a4 = sp.Function("a4")  # the unknown function a4(x4) of the metric
    b4 = sp.Function("b4", positive=True)  # the unknown function b4(x4) > 0
    NAMES = {"a4": a4, "b4": b4, "x4": x4, "x0": x0, "H": H, "Sin": sp.sin,
             "Cos": sp.cos, "Cot": sp.cot, "Tan": sp.tan, "Sign": sp.sign}


    def from_record(text):
        """A Wolfram-Language text of the record as a sympy expression."""
        for f in ("a4", "b4"):  # Derivative[n][f][x4] is the n-th derivative of f
            for n in (1, 2):
                text = text.replace(f"Derivative[{n}][{f}][x4]",
                                    f"Derivative({f}(x4), (x4, {n}))")
        text = text.replace("[", "(").replace("]", ")").replace("^", "**")
        return sp.parse_expr(text, local_dict=NAMES)


    def plain(expression):
        """Drop sympy's extra branch for sin z = 0 (a point outside the metric's
        domain): keep the last (general) branch of every Piecewise."""
        return expression.replace(sp.Piecewise, lambda *branches: branches[-1][0])


    ZS = sp.Symbol("Z", real=True)  # z itself as a symbol
    S, C = sp.symbols("S C", positive=True)  # |sin z| and |cos z| on a quarter
    QUARTERS = [(1, 1), (1, -1), (-1, -1), (-1, 1)]  # the signs of (sin z, cos z)


    def on_quarter(expression, sigma, tau):
        """The expression on the quarter where sin z = sigma S, cos z = tau C."""
        e = expression.subs(x0, ZS / (6 * H))  # write it with z = 6 H x0
        e = e.replace(sp.cot, lambda u: sp.cos(u) / sp.sin(u))
        e = e.replace(sp.tan, lambda u: sp.sin(u) / sp.cos(u))
        e = sp.expand_trig(e)  # sin 2z = 2 sin z cos z and cos 2z likewise
        return e.subs({sp.sin(ZS): sigma * S, sp.cos(ZS): tau * C})


    def same(first, second):
        """True when first - second simplifies to zero on all four quarters."""
        for sigma, tau in QUARTERS:
            difference = sp.simplify(on_quarter(first - second, sigma, tau))
            if difference != 0:  # use S^2 + C^2 = 1
                difference = sp.simplify(difference.subs(C, sp.sqrt(1 - S ** 2)))
            if difference != 0:
                return False
        return True


    COORDS = ["x0", "x1", "x2", "x3", "x4", "x5", "x6", "x7"]
    X = [sp.Symbol(name, real=True) for name in COORDS]
    X[4], X[0] = x4, x0  # the metric depends on these two only
    z = 6 * H * x0
    W = (sp.sin(z) ** 2) ** sp.Rational(1, 6)  # the positive branch (sin^2 z)^(1/6)
    # the author's order x0, x1, ..., x7
    BY_HAND = ([sp.exp(-2 * a4(x4)) * b4(x4) * sp.cot(z) ** 2]
               + [sp.exp(2 * a4(x4))] * 3 + [sp.Integer(-1)]
               + [-sp.exp(-2 * a4(x4)) * b4(x4) * W] * 3)
    G_RECORD = [from_record(text) for text in record["metricDiagonal"]]
    for name, entry in zip(COORDS, G_RECORD):
        say(f"g_{name[1]}{name[1]} = {entry}")
    check(record["coordinates"] == COORDS and len(G_RECORD) == 8
          and all(same(a, b) for a, b in zip(G_RECORD, BY_HAND)),
          "the record's metric equals the author's corrected metric typed in by hand",
          record=f"{CURVATURE}, key metricDiagonal")
    G = sp.diag(*G_RECORD)  # the metric as an 8 x 8 diagonal sympy matrix
    '''),
    md(r"""
    ## 11. How fast the scale factors change: rates along $x_4$ and $x_0$

    The next cell computes the logarithmic rates $\partial_c \ln s_a =
    \partial_c g_{aa}/(2 g_{aa})$ of the eight scale factors with respect to $x_4$
    and $x_0$ and checks the formulas of section 4. Their sum along $x_4$ is
    $-a_4' + 2 b_4'/b_4$. It then reads the prescribed history of the Revision
    record from Revision/kohn_sham/results/parameters.json, $a_4 = A H x_4$ and
    $b_4 = b_4(0)\, e^{\beta A H x_4}$ with $A = 1$, $H = 1$, $\beta = 4/3$ and
    $b_4(0) = 1$ (so $a_4' = 1$ and $b_4'/b_4 = 4/3$), the background along which
    the book computes its Kohn-Sham states, and evaluates the rates there: the bar
    chart shows $0$ for the time $x_4$, $+1$ for the three 3-space directions
    (inflation) and $-1 + 2/3 = -1/3$ for the hidden direction and the three extra
    times (deflation). Their sum is $3 - 4/3 = 5/3$, the rate at which the volume
    factor grows; the record's rule for its proper 7-volume,
    $e^{(2\beta - 1) a_4}$, has the same exponent $2\beta - 1 = 5/3$.
    sympy prints $H \cot z$ as `H/tan(6*H*x0)` and $-6H/(\sin z \cos z)$ as
    `-12*H/sin(12*H*x0)`; these are the same, because $\sin 2z = 2 \sin z \cos z$.
    """),
    code(r'''
    rate4 = [sp.simplify(sp.diff(G[a, a], x4) / (2 * G[a, a])) for a in range(8)]
    rate0 = [plain(sp.simplify(sp.diff(G[a, a], x0) / (2 * G[a, a]))) for a in range(8)]
    da4 = sp.diff(a4(x4), x4)  # a4', the derivative of a4
    db4 = sp.diff(b4(x4), x4)  # b4', the derivative of b4
    shrink = -da4 + db4 / (2 * b4(x4))  # the rate of the factor e^(-a4) b4^(1/2)
    # the author's order x0, x1, ..., x7
    expected4 = [shrink] + [da4] * 3 + [0] + [shrink] * 3
    expected0 = ([-6 * H / (sp.sin(z) * sp.cos(z))] + [0] * 3 + [0]
                 + [H * sp.cot(z)] * 3)
    for a, name in enumerate(COORDS):
        say(f"{name}: d4 ln s = {rate4[a]},  d0 ln s = {rate0[a]}")
    check(all(same(r, e) for r, e in zip(rate4, expected4))
          and all(same(r, e) for r, e in zip(rate0, expected0)),
          "the rates a4', -a4' + b4'/(2 b4), 0, H cot z and -6H/(sin z cos z)")
    check(same(sum(rate4), -da4 + 2 * db4 / b4(x4)),
          "the eight rates along x4 add up to -a4' + 2 b4'/b4")

    PARAMETERS = "Revision/kohn_sham/results/parameters.json"
    physics = json.loads(repository_file(PARAMETERS).read_text(
        encoding="utf-8"))["physics"]
    A_REC, H_REC = physics["historyA"], physics["H"]  # a4 = A H x4
    BETA, B40 = physics["historyBeta"], physics["historyB4AtZero"]  # b4 = b4(0) e^...
    report("history of the record: A, H, beta, b4(0)", f"{A_REC}, {H_REC}, "
           f"{BETA:.15f}, {B40}")
    check(A_REC == 1.0 and H_REC == 1.0 and abs(BETA - 4 / 3) < 1e-14 and B40 == 1.0,
          "the prescribed history: a4 = H x4, b4 = e^((4/3) H x4) (A = H = 1)",
          record=f"{PARAMETERS}, keys historyA, H, historyBeta, historyB4AtZero")
    on_history = {da4: sp.Integer(1), db4: sp.Rational(4, 3) * b4(x4)}  # a4', b4'
    rates_now = [sp.simplify(r.subs(on_history)) for r in rate4]
    report("the eight rates on the history (x0 ... x7)",
           ", ".join(str(r) for r in rates_now))
    check(sum(rates_now) == sp.Rational(5, 3) == 2 * sp.Rational(4, 3) - 1
          and "(2 beta - 1) a4,0" in physics["Vol7Rule"],
          "on the history the rates add up to 5/3 = 2 beta - 1: the volume grows",
          record=f"{PARAMETERS}, key Vol7Rule")

    values_now = [float(r) for r in rates_now]
    fig, ax = plt.subplots()
    colors = [VIOLET] + [BLUE] * 3 + [GREY] + [ORANGE] * 3
    ax.bar(range(8), values_now, color=colors, width=0.6)
    ax.axhline(0.0, color=BLACK, lw=0.8)
    ax.set_xticks(range(8), [f"$x_{k}$" for k in range(8)])
    for k, value in enumerate(values_now):
        ax.text(k, value + (0.06 if value >= 0 else -0.14), f"{value:+.2f}",
                ha="center", fontsize=9)
    ax.set_ylim(-0.8, 1.4)
    ax.set_xlabel("direction")
    ax.set_ylabel("$\\partial_4 \\ln s_a$ (units $H$)")
    ax.set_title("Growth rate of each scale factor along the time $x_4$ "
                 "($a_4 = H x_4$, $b_4 = e^{4 H x_4/3}$)")
    save_figure(fig, "rates_along_x4",
                "The rate $\\partial_4 \\ln s_a$ at which the scale factor $s_a$ of "
                "each direction changes with the time $x_4$ (vertical axis, units of "
                "$H$), along the prescribed history of the Revision record, "
                "$a_4 = H x_4$ and $b_4 = e^{(4/3) H x_4}$ ($H = 1$). The three "
                "3-space directions $x_1, x_2, x_3$ (blue) grow at the rate "
                "$+a_4' = +1$: 3-space inflates. The three extra times "
                "$x_5, x_6, x_7$ (orange) and the hidden direction $x_0$ (violet) "
                "shrink at the rate $-a_4' + b_4'/(2 b_4) = -1/3$: they deflate "
                "exponentially. The time $x_4$ (grey) does not change. The eight "
                "rates add up to $5/3$: the volume factor grows.")
    '''),
    md(r"""
    The rates along the hidden coordinate depend on $z$. The next cell draws them
    with $H = 1$ on one cell $0 < z < \pi$, made of two halves joined at the fold
    $z = \pi/2$ (each half drawn up to $0.05$ from its ends, where some rates grow
    without bound): $H \cot z$ for the extra-time factors, $0$ for 3-space,
    $-6H/(\sin z \cos z)$ for the hidden
    factor $s_0$, and their sum over all eight directions, which must be the
    logarithmic rate of the volume factor, $\partial_0 \ln (|\cot z|
    (\sin^2 z)^{1/4}) = -6H/(\sin z \cos z) + 3H \cot z = -3H (\cot z + 2 \tan z)$.
    The first check confirms the sum exactly with sympy. The second check confirms
    the mirror property seen in the figure: the metric does not change when $z$ is
    replaced by $\pi - z$ ($\cot^2$ and $\sin^2$ are unchanged), which reverses the
    direction of $x_0$, so every rate along $x_0$ changes its sign.
    """),
    code(r'''
    check(same(sum(rate0), -3 * H * (sp.cot(z) + 2 * sp.tan(z))),
          "the eight rates along x0 add up to -3 H (cot z + 2 tan z)")
    mirrored = [r.subs(x0, (sp.pi - z) / (6 * H)) for r in rate0]  # z -> pi - z
    check(all(same(m, -r) for m, r in zip(mirrored, rate0)),
          "under z -> pi - z every rate along x0 changes its sign")
    fig, ax = plt.subplots()
    halves = [np.linspace(0.05, np.pi / 2 - 0.05, 300),
              np.linspace(np.pi / 2 + 0.05, np.pi - 0.05, 300)]
    for k, z_line in enumerate(halves):
        first = k == 0  # label the curves only once
        ax.plot(z_line, 1 / np.tan(z_line), color=ORANGE, lw=1.6,
                label="$H \\cot z$: directions $x_5, x_6, x_7$" if first else None)
        ax.plot(z_line, 0 * z_line, color=BLUE, lw=1.6,
                label="$0$: directions $x_1, x_2, x_3$ and $x_4$" if first else None)
        ax.plot(z_line, -6 / (np.sin(z_line) * np.cos(z_line)), "--", color=VIOLET,
                lw=1.6, label="$-6H/(\\sin z \\cos z)$: direction $x_0$" if first
                else None)
        ax.plot(z_line, -3 * (1 / np.tan(z_line) + 2 * np.tan(z_line)), "-.",
                color=BLACK, lw=1.4, label="sum of all eight $= -3H(\\cot z + 2\\tan z)$"
                if first else None)
    ax.axvline(np.pi / 2, color=GREY, ls=":", lw=1.2)
    ax.text(np.pi / 2 + 0.04, -56.0, "fold $z = \\pi/2$", fontsize=8, color=GREY)
    ax.set_ylim(-60.0, 60.0)
    ax.set_xlabel("$z = 6 H x_0$")
    ax.set_ylabel("$\\partial_0 \\ln s_a$ (units $H$)")
    ax.set_title("Rates of the scale factors along the hidden coordinate ($H = 1$)")
    ax.legend(loc="lower left", fontsize=7)
    save_figure(fig, "rates_along_x0",
                "The rates $\\partial_0 \\ln s_a$ at which the scale factors change "
                "along the hidden coordinate $x_0$ (vertical axis, units of $H$, "
                "$H = 1$), against $z = 6 H x_0$ over one cell from 0.05 to "
                "$\\pi - 0.05$, whose two halves meet at the fold $z = \\pi/2$ "
                "(dotted). Solid orange: $H \\cot z$ for the three extra times. Solid "
                "blue: 0 for 3-space and the time. Dashed violet: "
                "$-6H/(\\sin z \\cos z)$ for the hidden direction, whose scale factor "
                "is $e^{-a_4} b_4^{1/2} |\\cot z|$. Dash-dotted black: the sum of all "
                "eight rates, the rate $-3H(\\cot z + 2 \\tan z)$ of the volume factor. "
                "Every curve at $\\pi - z$ is minus the curve at $z$.")
    '''),
    md(r"""
    ## 12. The volume factor and Jacobi's formula

    The determinant of the diagonal metric is the product of its entries. The cell
    computes it from the record's metric, compares $\sqrt{|\det g|}$ with the
    record's own entry `sqrtAbsDetG` (written there as $e^{-a_4} b_4^2
    (\sin^2 z)^{1/4} \cot z\, \mathrm{sign}(\cot z)$, and $\cot z\,
    \mathrm{sign}(\cot z) = |\cot z|$) and with $e^{-a_4} b_4^2 |\cot z|
    (\sin^2 z)^{1/4}$ (the Wolfram check `sqrt_abs_det_g` of the Revision record
    Revision/field_equations_a4/reports/wolfram-a4-report.json), and checks that
    its partial derivative with respect to $x_4$ is $(-a_4' + 2 b_4'/b_4)
    \sqrt{|\det g|}$: the volume factor changes with time unless $b_4^2 =
    \text{const} \cdot e^{a_4}$. Finally it checks Jacobi's formula
    $\partial_c \sqrt{|\det g|} = \frac{1}{2} \sqrt{|\det g|}\,
    \mathrm{tr}(g^{-1} \partial_c g)$ for $c = x_4$ and $c = x_0$ (tr, the trace,
    is the sum of the diagonal entries of a matrix).
    """),
    code(r'''
    det_g = sp.simplify(G.det())  # the product of the eight entries
    say(f"det g = {det_g}")
    sqrt_record = from_record(record["sqrtAbsDetG"])
    say(f"sqrtAbsDetG of the record = {sqrt_record}")
    volume = sp.exp(-a4(x4)) * b4(x4) ** 2 * sp.Abs(sp.cot(z)) * (sp.sin(z) ** 2) ** (
        sp.Rational(1, 4))  # e^(-a4) b4^2 |cot z| (sin^2 z)^(1/4)
    check(same(det_g, sp.exp(-2 * a4(x4)) * b4(x4) ** 4 * sp.cot(z) ** 2
               * (sp.sin(z) ** 2) ** sp.Rational(1, 2))
          and same(sqrt_record, volume) and same(sqrt_record ** 2, det_g),
          "det g = e^(-2a4) b4^4 cot^2 z (sin^2 z)^(1/2); the record's sqrt|det g| = "
          "e^(-a4) b4^2 |cot z| (sin^2 z)^(1/4)",
          record=f"{CURVATURE}, key sqrtAbsDetG")
    A4REPORT = "Revision/field_equations_a4/reports/wolfram-a4-report.json"
    a4_report = json.loads(repository_file(A4REPORT).read_text(encoding="utf-8"))
    verdict = [c["verdict"] for c in a4_report["checks"]
               if c["name"] == "sqrt_abs_det_g"]
    check(verdict == ["PASS"]
          and same(sp.diff(sqrt_record, x4),
                   (-da4 + 2 * db4 / b4(x4)) * sqrt_record),
          "d4 sqrt|det g| = (-a4' + 2 b4'/b4) sqrt|det g|: the volume factor depends "
          "on x4", record=f"{A4REPORT}, check sqrt_abs_det_g")
    jacobi = [same(sp.diff(sqrt_record, c),
                   sp.Rational(1, 2) * sqrt_record * (G.inv() * G.diff(c)).trace())
              for c in (x4, x0)]
    check(all(jacobi), "Jacobi's formula for the derivative of sqrt|det g| (x4 and x0)")
    '''),
    md(r"""
    ## 13. All 21 Christoffel entries of the record

    The record lists every nonzero $\Gamma^a{}_{bc}$ with $b$ not after $c$ in the
    order $x_0, \dots, x_7$ (the symbol is symmetric in $b$ and $c$). The next cell
    computes all $8 \times 36 = 288$ such entries from the formula of section 4,
    keeps the nonzero ones, and compares them one by one with the record. Only
    first partial derivatives of the metric entries are needed.
    """),
    code(r'''
    computed = {}
    for a in range(8):
        for b in range(8):
            for c in range(b, 8):
                value = (sp.diff(G[a, c], X[b]) + sp.diff(G[a, b], X[c])
                         - sp.diff(G[b, c], X[a])) / (2 * G[a, a])
                value = plain(sp.simplify(value))
                if value != 0:
                    computed[(COORDS[a], COORDS[b], COORDS[c])] = value
    listed = {(e["a"], e["b"], e["c"]): from_record(e["value"])
              for e in record["christoffelNonzero_b_le_c"]}
    for key in [("x0", "x0", "x0"), ("x0", "x0", "x4"), ("x4", "x0", "x0"),
                ("x5", "x0", "x5")]:
        say(f"Gamma^{key[0]}_({key[1]} {key[2]}) = {computed[key]}")
    report("nonzero entries computed / listed in the record",
           f"{len(computed)} / {len(listed)}")
    check(sorted(computed) == sorted(listed)
          and all(same(computed[k], listed[k]) for k in listed),
          "all 21 nonzero Christoffel entries equal those of the record",
          record=f"{CURVATURE}, key christoffelNonzero_b_le_c")
    '''),
    md(r"""
    ## 14. The last check

    The last cell checks that all 6 figure files exist in the folder
    Revision/textbook/figures and prints the number of checks that passed.
    """),
    code(r'''
    names = ["level_curves_gradient", "slices_and_slopes", "finite_differences",
             "chain_rule", "rates_along_x4", "rates_along_x0"]
    present = [output_file(f"{FIGURE_FOLDER}/02c_{k}_{name}.png").is_file()
               for k, name in enumerate(names, 1)]
    check(all(present), f"all {len(names)} figure files of notebook 02c exist")
    all_checks_passed()
    '''),
    md(r"""
    ## 15. What this notebook showed

    - A partial derivative is an ordinary derivative with the other variables held
      fixed: the slope of a slice. The gradient points uphill, perpendicular to the
      level curves. The two mixed derivatives of $x^2 \sin y$ agree (Schwarz).
    - Forward differences have order 1, central differences order 2; rounding
      errors grow like $\epsilon/h$, so the best spacing is about $10^{-8}$
      (forward) or $10^{-6}$ (central), not the smallest one.
    - The chain rule for $z = 6 H x_0$: $\partial_0 = 6H\, d/dz$.
    - The author's corrected metric, read from the Revision record, has the
      scale-factor rates $+a_4'$ (3-space, inflating), $-a_4' + b_4'/(2 b_4)$ (the
      hidden direction and the three extra times, deflating together) and $0$ (the
      time $x_4$) along $x_4$, and $-6H/(\sin z \cos z)$ (hidden), $0$ (3-space,
      time) and $H \cot z$ (extra times) along $x_0$; every rate along $x_0$ changes
      sign under $z \to \pi - z$. Along the prescribed history of the record
      ($a_4 = H x_4$, $b_4 = e^{(4/3) H x_4}$) the rates are $+1$ and $-1/3$ (units
      $H$), and they add up to $5/3$.
    - $\sqrt{|\det g|} = e^{-a_4} b_4^2 |\cot z| (\sin^2 z)^{1/4}$ for every
      $a_4(x_4)$, $b_4(x_4)$ and every real $z$ with $\sin z \cos z \neq 0$
      (reproduces the record's sqrtAbsDetG and the Wolfram check sqrt_abs_det_g).
      The inflation of 3-space and the deflation of the extra times do not
      compensate: the volume factor changes with $x_4$ at the rate
      $-a_4' + 2 b_4'/b_4$, which is $5/3$ along the history, the exponent of the
      record's proper 7-volume $e^{(2\beta - 1) a_4}$. Jacobi's formula holds.
    - All 21 nonzero Christoffel entries of the record follow from first partial
      derivatives of the metric.
    """),
]

if __name__ == "__main__":
    raise SystemExit(run_builder(__file__))
