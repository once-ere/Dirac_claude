#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
"""Builder of Notebook 03d, "Free fall in the corrected metric" (textbook "Universes in
Pairs").

The notebook Revision/textbook/notebooks/03d_free_fall.ipynb is BUILT from this file by
Revision/textbook/tools/nbkit.py (never edit the .ipynb by hand):

    python Revision/textbook/tools/nbkit.py build \
        Revision/textbook/notebooks/src/03d_free_fall.py --date YYYY-MM-DD
    python Revision/textbook/tools/nbkit.py check \
        Revision/textbook/notebooks/src/03d_free_fall.py

What a freely falling test particle does in the corrected metric (Revision/SPEC.md
section 1, version 2 of 2026-10-16, with the functions a4 and b4, in the author's
coordinates x0..x7) along the deflating history a4 = A H x4, b4 = b4(0) e^(beta A H x4)
(beta = 4/3, b4(0) = 1) of the Revision Kohn-Sham work: the geodesic equations are
integrated with exactly the Christoffel symbols of the Revision record
Revision/gkd_lovelock/results/curvature.json; the conservation laws, the redshift of the
3-space motion, the blueshift of the extra-time motion, the push of the extra-time
motion along the hidden direction and the law of the x4 velocity are proved exactly
with sympy and confirmed on the computed paths.  The momentum weight of the Revision
Kohn-Sham record and the quadratic form of the plane-wave check of the Revision scope
report are reproduced.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools"))
from nbkit import code, md, run_builder  # noqa: E402

FIG = "Revision/textbook/figures/03d"
CURV = "Revision/gkd_lovelock/results/curvature.json"
PARS = "Revision/kohn_sham/results/parameters.json"
KST = "Revision/kohn_sham/ks-theory.json"
SCOPE = "Revision/theory/reports/python-scope.json"

FACTS = {
    "id": "03d",
    "name": "03d_free_fall",
    "title": "Free fall in the corrected metric: conserved momenta, redshift, blueshift "
             "and the fall towards the tip",
    "purpose": (
        "It integrates the geodesic equations of free fall in the corrected metric with "
        "the Christoffel symbols of the Revision record, along the deflating history "
        "a4 = A H x4, b4 = b4(0) e^(beta A H x4) with A = 1, H = 1, b4(0) = 1 and "
        "beta = 4/3, by the Runge-Kutta method RK4. With sympy it proves exactly, for "
        "general a4(x4) and b4(x4) and every real z, that the six momenta along x1, x2, "
        "x3, x5, x6, x7 and the squared length of the velocity are conserved, that the "
        "frame velocity in 3-space falls like e^(-a4) at every height (redshift) while "
        "the frame velocity along an extra time grows like e^(a4) b4^(-1/2) (blueshift), "
        "that only motion along the extra times pushes a particle along the hidden "
        "coordinate y (towards the tip), and the law of the x4 velocity; it reproduces "
        "the momentum weight of the Revision Kohn-Sham record and the quadratic form of "
        "the plane-wave check of the Revision scope report. It checks all of this on the "
        "computed paths, follows a particle that moves along an extra time until it "
        "reaches the tip cut-off of the Kohn-Sham solver, compares its x4 velocity with "
        "the exact solution of its law, measures the order 4 of RK4, and draws 5 figures."
    ),
    "records": [
        [CURV, "the 21 non-zero Christoffel symbols with b <= c "
               "(christoffelNonzero_b_le_c), written by the Rust program lovelock_gkd; "
               "the notebook integrates the geodesic equations with exactly these symbols"],
        [PARS, "H = 1, the slope A = 1, the exponent beta = 4/3 and b4(0) = 1 of the "
               "deflating history a4 = A H x4, b4 = b4(0) e^(beta A H x4) of the Revision "
               "Kohn-Sham work, and its tip cut-off L (physics.H, physics.historyA, "
               "physics.historyBeta, physics.historyB4AtZero, physics.L_tipCutoff)"],
        [KST, "the momentum weight kappa(x4) = e^(-a4), which does not depend on y "
              "(geometry.kappa), the good sector without extra-time momenta "
              "(sectorAndAnsatz.sector) and the status of the history (a prescribed "
              "background, not solved for)"],
        [SCOPE, "the check extra_time_growth_rates_unbounded: for plane waves in flat 4+4 "
                "space the squared frequency is m^2 + k0^2 + k1^2 + k2^2 + k3^2 - k5^2 - "
                "k6^2 - k7^2, the same quadratic form as the squared x4 velocity of a free "
                "particle"],
    ],
    "packages": ["numpy", "sympy", "matplotlib"],
    "needs_rust": [],
    "expected_seconds": 50,
    "timeout_seconds": 300,
    "files_written": [
        "Revision/textbook/figures/03d.captions.json",
        f"{FIG}_1_frame_velocities.png",
        f"{FIG}_2_x4_velocity.png",
        f"{FIG}_3_hidden_push.png",
        f"{FIG}_4_quadratic_form.png",
        f"{FIG}_5_accuracy.png",
    ],
    "final_lines": [
        "PASS all five figure files exist",
        "ALL 23 CHECKS PASSED (notebook 03d)",
    ],
    "troubleshooting": [
        ["\"FileNotFoundError\" for curvature.json, parameters.json, ks-theory.json or "
         "python-scope.json",
         "the notebook reads these four Revision records of the repository, so the folder "
         "Revision of your copy is incomplete. Restore it with the following command in "
         "the repository folder (or clone the repository again) and run the notebook "
         "again:",
         ["git checkout -- Revision"]],
    ],
}

CELLS = [
    md(r"""
    ## 1. What this notebook computes

    Notebooks 03a and 03b described the corrected metric and its curvature. This
    notebook asks what the metric DOES: how does a small body move when no force acts on
    it, only the geometry? Such a body is in **free fall**, and its path is a
    **geodesic**. The notebook

    - reads the 21 non-zero Christoffel symbols of the Revision record
      `Revision/gkd_lovelock/results/curvature.json` and builds from them the geodesic
      equations, 16 first-order equations for the 8 coordinates and the 8 velocities;
    - proves exactly, with sympy, what stays constant during free fall: the six
      **momenta** along $x_1, x_2, x_3$ and $x_5, x_6, x_7$ and the squared length of the
      velocity;
    - proves that the velocity of a body moving in 3-space, measured with rulers and
      clocks at its place, falls like $e^{-a_4}$ at every height in the hidden direction
      (**redshift**: 3-space inflates), while its velocity along an extra time grows like
      $e^{a_4} b_4^{-1/2}$ (**blueshift**: the extra times deflate), and reproduces the
      **momentum weight** $\kappa = e^{-a_4}$ of the Revision Kohn-Sham record;
    - proves that only motion along an extra time pushes the body along the hidden
      coordinate $y$ (towards the tip; 3-space has no warp and pushes nothing), and finds
      the law of the velocity along the time $x_4$;
    - shows that the squared $x_4$ velocity of the body is the same quadratic form as the
      squared frequency of a plane wave in the Revision record's check
      `extra_time_growth_rates_unbounded`;
    - integrates the geodesic equations numerically (RK4) for a body at rest, three
      bodies moving in 3-space and one body moving along an extra time, along the
      deflating history $a_4 = AHx_4$, $b_4 = b_4(0)\,e^{\beta AHx_4}$ ($A = 1$, $H = 1$,
      $b_4(0) = 1$, $\beta = 4/3$), checks every exact law on the computed paths, follows
      the last body until it reaches the tip cut-off of the Kohn-Sham solver, and
      measures the accuracy of RK4;
    - draws 5 figures and prints a PASS line for every check.
    """),
    md(r"""
    ## 3. The words used in this notebook

    - **Coordinates** $x_0, \dots, x_7$ (the author's names): $x_0$ the **hidden**
      direction, $x_1, x_2, x_3$ ordinary 3-space, $x_4$ the time, $x_5, x_6, x_7$ the
      three **extra times**; $z = 6Hx_0$, any real number. In Python lists they are
      counted 0 to 7 as well: $x_k$ is entry $k$, its velocity $u^k$ too.
    - **Hidden coordinate** $y = \ln|\sin z|/(6H)$: $y = 0$ at the **fold**
      $\cos z = 0$ and $y \to -\infty$ at the **tip** $\sin z \to 0$. A step $dy$ has
      the proper length $f\,dy$, with the **hidden scale** $f = e^{-a_4}b_4^{1/2}$.
    - **Free fall**: motion under no force other than the geometry. **Test particle**: a
      body so small that it does not change the metric.
    - **Proper time** $\tau$: the time shown by a clock carried by the body.
    - **Velocity** $u^a = dx^a/d\tau$: how fast each coordinate changes per unit of
      proper time.
    - **Geodesic equation**: $du^a/d\tau = -\sum_{b,c} \Gamma^a{}_{bc}\, u^b u^c$, with
      the Christoffel symbols $\Gamma^a{}_{bc}$ of the metric; its solutions are the
      paths of free fall.
    - **Squared length of the velocity**: $g(u, u) = \sum_a g_{aa} (u^a)^2$ (the metric
      is diagonal). For a body with mass it equals $-1$ when $\tau$ is its proper time.
    - **Scale factor** $h_a = \sqrt{|g_{aa}|}$ and **frame velocity**
      $\hat u^a = h_a u^a$: the proper length (along an extra time: the proper
      duration) that the body covers along $x_a$ per unit of its own proper time,
      measured with the rulers and clocks of an observer at rest at its place; divided
      by $u^4$ it is the velocity that this observer measures.
    - **Momentum** $p_a = g_{aa} u^a$ (no sum) of a direction $x_a$. **Conserved**: the
      same number at every point of the path.
    - **Redshift, blueshift**: the decrease, increase of a frame velocity (or momentum)
      caused by the expansion, contraction of the space it points along.
    - **History** $a_4 = AHx_4$, $b_4 = b_4(0)\,e^{\beta AHx_4}$: the time dependence of
      the metric used for the numbers, the one of the Revision Kohn-Sham work ($A = 1$,
      $H = 1$, $\beta = 4/3$, $b_4(0) = 1$); with $A > 0$ the hidden direction and the
      extra times deflate, like $f = e^{-a_4/3}$. It is a **prescribed background**:
      assumed, not solved for.
    - **RK4**: the classical Runge-Kutta method of order 4; halving its step makes its
      error about $2^4 = 16$ times smaller.
    - **Turning point**: an instant at which the $x_4$ velocity $u^4$ passes through
      zero, so that $x_4$ stops growing.
    """),
    md(r"""
    ## 4. The physical and mathematical situation

    The corrected metric is diagonal,
    $g = \mathrm{diag}(h_0^2, h_1^2, h_2^2, h_3^2, -1, -h_5^2, -h_6^2, -h_7^2)$ with
    the scale factors $h_0 = f|\cot z|$ (the hidden direction), $h_1 = h_2 = h_3 =
    e^{a_4}$ (3-space, inflating, the same at every $z$) and $h_5 = h_6 = h_7 = fW$ (the
    extra times), where $f = e^{-a_4}b_4^{1/2}$ deflates at the rate
    $a_4' - b_4'/(2b_4)$ and $W = (\sin^2 z)^{1/12} = e^{Hy}$ is the warp factor of the
    extra times. A test particle with mass falls freely along a solution of the
    **geodesic equations**

    $$\frac{dx^a}{d\tau} = u^a, \qquad \frac{du^a}{d\tau} = -\sum_{b,c}
    \Gamma^a{}_{bc}\, u^b u^c \qquad (a = 0, \dots, 7),$$

    sixteen first-order equations. The Christoffel symbols are those of the Revision
    record (Notebook 03b checked them component by component). The metric depends only
    on $x_4$ and $x_0$; for each of the other six directions this makes a momentum
    $p_a = g_{aa} u^a$ conserved (section 6). The squared length $g(u, u)$ of the
    velocity is conserved too, and we choose it equal to $-1$: then $\tau$ is the
    proper time of the particle and the path is time-like.

    For the numbers the notebook uses the deflating history $a_4 = AHx_4$,
    $b_4 = b_4(0)\,e^{\beta AHx_4}$ of the Revision Kohn-Sham work with $A = 1$, $H = 1$,
    $b_4(0) = 1$ and $\beta = 4/3$ (so $a_4' = 1$, $b_4'/b_4 = 4/3$, and the hidden
    direction and the extra times deflate at the rate $a_4' - b_4'/(2b_4) = 1/3$). It
    is a prescribed background, and the particles are test particles: they move in the
    given metric and do not change it. Everything in sections 6 to 9 holds for general
    functions $a_4(x_4)$ and $b_4(x_4)$ and every real $z$; only the numerical paths of
    sections 10 to 13 use the history, and all of them stay inside the first half cell
    $0 < z < \pi/2$, where $\cot z > 0$ and $\sin z > 0$.
    """),
    md(r"""
    ## 5. The Christoffel symbols, read from the record

    First a technical step. While a cell runs, Jupyter sends what the cell prints to the
    notebook in pieces, about one piece every 0.2 seconds, so where one piece ends and
    the next begins depends on the speed of the computer. The tools that build this
    book read the PASS line of a check together with the line under it that names the
    Revision record, and they read the two correctly only when both arrive in the same
    piece. The next cell therefore defines the function `in_one_piece(helper)`: it
    returns a new function that does exactly what `helper` does, but lets `helper`
    print into a text buffer in memory (an `io.StringIO`, with
    `contextlib.redirect_stdout`) and then writes the whole buffer with one call of
    `sys.stdout.write`, which arrives as one piece. (The stars in `*arguments` and
    `**options` pass on all the values the new function is given, whatever they are.)
    The cell then replaces the helpers `check` and `report` of the set-up cell by such
    functions. Nothing else changes: the same checks, the same PASS lines, the same
    numbers.
    """),
    code(r'''
    import contextlib  # redirect_stdout: send printed text into a buffer
    import io  # StringIO: a text buffer in memory
    import sys  # sys.stdout: the place where printed text goes


    def in_one_piece(helper):
        """A function that does what helper does, with all the lines that helper prints
        written in one piece."""
        def helper_in_one_piece(*arguments, **options):
            collected = io.StringIO()  # an empty text buffer
            with contextlib.redirect_stdout(collected):  # print() writes into it
                helper(*arguments, **options)  # a failing check stops here, as before
            sys.stdout.write(collected.getvalue())  # all the lines with one write
        return helper_in_one_piece


    check = in_one_piece(check)  # a PASS line and its record line stay together
    report = in_one_piece(report)  # a long RESULT line and its second line, too
    say("From now on check and report print each of their results in one piece.")
    '''),
    md(r"""
    The next cell imports the packages, makes the symbols (the eight coordinates, the
    constant $H > 0$, the functions $a_4(x_4)$ and $b_4(x_4)$, the warp factor `W`, and
    the printing names `a4p` for $a_4'$, `a4v` for the value of $a_4$, `b4p` and `b4v`
    the same for $b_4$), and reads the list `christoffelNonzero_b_le_c` of the record.
    The warp factor is the same sympy function class as in Notebook 03b: `W(x0)` stands
    for $(\sin^2 z)^{1/12}$, and its method `fdiff` gives sympy its derivative
    $H\cot z\, W$. Each entry of the record gives the three indices `a`, `b`, `c` of
    $\Gamma^a{}_{bc}$ (with $b \le c$) and its value in Mathematica notation, which the
    function `from_mathematica` translates into sympy (the same translation as in
    Notebook 03b: `(Sin[6*H*x0]^2)^(1/6)` becomes `W(x0)^2`, `Derivative[1][a4][x4]`
    becomes `a4p`, `a4[x4]` becomes `a4v`, the same for $b_4$, square brackets of
    functions become round ones, `^` becomes `**`). Because
    $\Gamma^a{}_{bc} = \Gamma^a{}_{cb}$, every entry with $b < c$ is stored twice, once
    for each order of the lower indices: the 21 entries give 31 symbols. The cell prints
    four of them.
    """),
    code(r'''
    import numpy as np  # arrays of numbers
    import sympy as sp  # exact algebra with symbols
    from sympy.parsing.sympy_parser import parse_expr  # text -> sympy expression

    CURVATURE_RECORD = "Revision/gkd_lovelock/results/curvature.json"
    record = json.loads(repository_file(CURVATURE_RECORD).read_text(encoding="utf-8"))
    NAMES = ["x0", "x1", "x2", "x3", "x4", "x5", "x6", "x7"]
    X = sp.symbols("x0:8", real=True)  # the coordinates x0 ... x7 (X[0] ... X[7])
    x4, x0 = X[4], X[0]
    H = sp.symbols("H", positive=True)  # the constant of the author
    a4 = sp.Function("a4")(x4)  # the metric function a4, any function of x4
    b4 = sp.Function("b4", positive=True)(x4)  # the metric function b4 > 0


    class W(sp.Function):
        """The warp factor W(x0) = (sin(6 H x0)^2)^(1/12) > 0 of the extra times."""

        def fdiff(self, argindex=1):
            """dW/dx0 = H cot(6 H x0) W, for every real z = 6 H x0 with sin z != 0."""
            return H * sp.cot(6 * H * self.args[0]) * self


    a4p, a4v, b4p = sp.symbols("a4p a4v b4p", real=True)  # printing names
    b4v = sp.symbols("b4v", positive=True)  # printing name of the value of b4
    record_names = {"a4p": a4p, "a4v": a4v, "b4p": b4p, "b4v": b4v, "H": H, "x0": x0,
                    "E": sp.E, "sin": sp.sin, "cot": sp.cot, "W": W}


    def from_mathematica(entry_text):
        """A value of the record (Mathematica notation) as a sympy expression."""
        t = entry_text.replace("(Sin[6*H*x0]^2)^(1/6)", "W(x0)^2")  # the warp squared
        t = t.replace("Derivative[1][a4][x4]", "a4p").replace("a4[x4]", "a4v")
        t = t.replace("Derivative[1][b4][x4]", "b4p").replace("b4[x4]", "b4v")
        t = t.replace("Sin[6*H*x0]", "sin(6*H*x0)").replace("Cot[6*H*x0]", "cot(6*H*x0)")
        t = t.replace("^", "**")
        if "[" in t or "]" in t:  # a piece of notation that was not translated
            raise ValueError(f"cannot translate {entry_text}")
        return parse_expr(t, local_dict=record_names)


    Gamma = {}  # (a, b, c) -> the value of Gamma^a_bc, with a4p, a4v, b4p, b4v
    for entry in record["christoffelNonzero_b_le_c"]:
        a, b, c = (NAMES.index(entry[key]) for key in ("a", "b", "c"))
        Gamma[(a, b, c)] = from_mathematica(entry["value"])
        Gamma[(a, c, b)] = Gamma[(a, b, c)]  # the same symbol with b and c exchanged
    for key in [(1, 1, 4), (4, 5, 5), (0, 5, 5), (0, 0, 4)]:
        a, b, c = key
        say(f"  Gamma^{NAMES[a]}_({NAMES[b]} {NAMES[c]}) = {Gamma[key]}")
    report("entries of the record (b <= c)", len(record["christoffelNonzero_b_le_c"]))
    check(len(record["christoffelNonzero_b_le_c"]) == 21 and len(Gamma) == 31,
          "the 21 entries of the record give 31 non-zero Christoffel symbols",
          record=f"{CURVATURE_RECORD}, christoffelNonzero_b_le_c")
    '''),
    md(r"""
    ## 6. What stays constant during free fall (exact)

    A quantity $f$ that depends on the position $x$ and the velocity $u$ changes along a
    path at the rate given by the chain rule,

    $$\frac{df}{d\tau} = \sum_a \frac{\partial f}{\partial x^a}\, u^a
    + \sum_a \frac{\partial f}{\partial u^a}\, \frac{du^a}{d\tau},$$

    and on a path of free fall $du^a/d\tau$ is given by the geodesic equation. The next
    cell defines this rate as the function `along_path(f)`, with the record's
    Christoffel symbols for general functions $a_4(x_4)$ and $b_4(x_4)$ (`a4p` becomes
    the derivative of $a_4$, `a4v` the value $a_4(x_4)$, and the same for $b_4$).

    By hand, for the momentum $p_5 = g_{55} u^5$ of the extra time $x_5$. Line 1, the
    chain rule (only $x_4$ and $x_0$ appear in $g_{55}$):
    $dp_5/d\tau = (\partial_4 g_{55}\, u^4 + \partial_0 g_{55}\, u^0)\, u^5
    + g_{55}\, du^5/d\tau$. Line 2, the geodesic equation for $u^5$ has the four terms
    with $\Gamma^{x_5}{}_{x_5x_4} = \Gamma^{x_5}{}_{x_4x_5} = \alpha_t$ (the rate
    $\alpha_t = -a_4' + b_4'/(2b_4)$ of the extra times) and
    $\Gamma^{x_5}{}_{x_5x_0} = \Gamma^{x_5}{}_{x_0x_5} = H\cot z$:
    $du^5/d\tau = -2\alpha_t u^5 u^4 - 2H\cot z\, u^5 u^0$. Line 3, from
    $g_{55} = -f^2 W^2$: $\partial_4 g_{55} = 2\alpha_t g_{55}$ (because
    $\partial_4 \ln f = \alpha_t$) and $\partial_0 g_{55} = 2H\cot z\, g_{55}$
    (because $\partial_0 \ln W = H\cot z$). Line 4, inserting lines 2 and 3 into line 1:
    $dp_5/d\tau = 2\alpha_t g_{55} u^4 u^5 + 2H\cot z\, g_{55} u^0 u^5
    - 2\alpha_t g_{55} u^5 u^4 - 2H\cot z\, g_{55} u^5 u^0 = 0$. The momentum is
    conserved because the metric does not depend on $x_5$. For 3-space it is shorter:
    $g_{11} = e^{2a_4}$ and the only symbols are $\Gamma^{x_1}{}_{x_1x_4} = a_4'$, so
    $dp_1/d\tau = 2a_4' g_{11} u^4 u^1 - 2a_4' g_{11} u^1 u^4 = 0$. The cell lets sympy
    do the same for all six momenta of $x_1, x_2, x_3, x_5, x_6, x_7$, and for the
    squared length $g(u, u) = \sum_a g_{aa} (u^a)^2$.
    """),
    code(r'''
    u = sp.symbols("u0:8", real=True)  # the velocity components u^0 ... u^7
    # back to the functions a4(x4) and b4(x4)
    to_function = {a4p: sp.Derivative(a4, x4), a4v: a4, b4p: sp.Derivative(b4, x4),
                   b4v: b4}
    acceleration = [sp.S(0)] * 8  # du^a/dtau from the geodesic equation
    for (a, b, c), value in Gamma.items():
        acceleration[a] -= value.subs(to_function) * u[b] * u[c]


    def along_path(f):
        """The rate of change df/dtau of f(x, u) along a path of free fall."""
        return sum(sp.diff(f, X[k]) * u[k] + sp.diff(f, u[k]) * acceleration[k]
                   for k in range(8))


    f_hidden = sp.exp(-a4) * sp.sqrt(b4)  # f = e^(-a4) b4^(1/2), the hidden scale
    # the eight scale factors h_a in the author's order x0, x1, ..., x7 (x0 with the
    # sign of cot z, as in the record)
    h = [f_hidden * sp.cot(6 * H * x0)] + [sp.exp(a4)] * 3 + [sp.Integer(1)] \
        + [f_hidden * W(x0)] * 3
    ETA = [1, 1, 1, 1, -1, -1, -1, -1]  # the signs of the metric entries
    g = [ETA[k] * h[k] ** 2 for k in range(8)]  # the diagonal of the metric
    say(f"du5/dtau = {sp.factor(acceleration[5]).subs(sp.Derivative(a4, x4), a4p)}")
    momenta = {k: g[k] * u[k] for k in (1, 2, 3, 5, 6, 7)}  # p_a = g_aa u^a
    rates = [sp.simplify(along_path(p)) for p in momenta.values()]
    check(rates == [0] * 6,
          "the six momenta of x1, x2, x3, x5, x6, x7 are conserved in free fall")
    squared_length = sum(g[k] * u[k] ** 2 for k in range(8))  # g(u, u)
    check(sp.simplify(along_path(squared_length)) == 0,
          "the squared length g(u, u) of the velocity is conserved in free fall")
    '''),
    md(r"""
    ## 7. Redshift in 3-space, blueshift along the extra times (exact)

    The frame velocity is $\hat u^a = h_a u^a$. Since $p_a = g_{aa} u^a = \pm h_a^2 u^a$
    (plus for 3-space, minus for the extra times),

    $$\hat u^1 = \frac{p_1}{h_1} = p_1\, e^{-a_4}, \qquad
    \hat u^5 = -\frac{p_5}{h_5} = -p_5\, b_4^{-1/2} e^{a_4} W^{-1} .$$

    With $p_1$ and $p_5$ constant, the frame velocity in 3-space falls like $e^{-a_4}$
    when $a_4$ grows (redshift), at every height in the hidden direction alike, and the
    frame velocity along an extra time grows like $e^{a_4} b_4^{-1/2} = 1/f$, on the
    history of this notebook like $e^{a_4/3}$ (blueshift). $1/h_1 = e^{-a_4}$ is exactly
    the **momentum weight** $\kappa(x_4) = e^{-a_4(x_4)}$ that the Revision Kohn-Sham
    record uses to turn a conserved 3-space momentum into the momentum seen at time
    $x_4$, and the record states that it does not depend on $y$. In the hidden
    coordinate $W = e^{Hy}$, so $1/h_5 = b_4^{-1/2} e^{a_4 - Hy}$: an extra-time motion
    is blueshifted more where $y$ is lower. The next cell reads that statement of the
    record and checks both.
    """),
    code(r'''
    KS_THEORY = "Revision/kohn_sham/ks-theory.json"
    ks_theory = json.loads(repository_file(KS_THEORY).read_text(encoding="utf-8"))
    say("record, geometry.kappa: " + ks_theory["geometry"]["kappa"])
    y_of_x0 = sp.log(sp.sin(6 * H * x0) ** 2) / (12 * H)  # y = ln|sin z|/(6H)
    kappa = sp.exp(-a4)  # the record's e^{-a4(x4)}
    check(sp.simplify(1 / h[1] - kappa) == 0 and not (1 / h[1]).has(x0)
          and "it does not depend on y" in ks_theory["geometry"]["kappa"],
          "1/h1 = e^(-a4) at every y: the frame velocity in 3-space is p1 times kappa",
          record=f"{KS_THEORY}, geometry.kappa")
    W_in_y = (sp.sin(6 * H * x0) ** 2) ** sp.Rational(1, 12)  # W written out
    check(sp.simplify(sp.exp(H * y_of_x0) - W_in_y) == 0
          and sp.simplify(1 / h[5] - sp.exp(a4) / sp.sqrt(b4) / W(x0)) == 0,
          "W = e^(H y) and 1/h5 = b4^(-1/2) e^(a4 - H y): the frame velocity along an "
          "extra time grows with a4")
    '''),
    md(r"""
    ## 8. The push along the hidden direction and the law of $x_4$ (exact)

    Two more exact laws follow from the record's symbols. First the hidden direction.
    The frame velocity along $x_0$ is $\hat u^0 = h_0 u^0 = f\cot z\, u^0 = f\,dy/d\tau$
    (because $dy/dx_0 = \cot z$). The geodesic equation for $u^0$ has the terms with
    $\Gamma^{x_0}{}_{x_0x_0} = -6H(\tan z + \cot z)$,
    $\Gamma^{x_0}{}_{x_0x_4} = \alpha_t$ and $\Gamma^{x_0}{}_{x_jx_j} = H W^2 \tan z$
    (extra times, $j = 5, 6, 7$); there is no symbol $\Gamma^{x_0}{}_{x_ix_i}$ for
    3-space, which has no warp. Working out $d(f\hat u^0)/d\tau$ with the product rule,
    the terms with $(u^0)^2$ and with $u^0 u^4$ cancel (as for the momenta of section 6),
    and what is left is

    $$\frac{d}{d\tau}\bigl(f\,\hat u^0\bigr) = \frac{d}{d\tau}\Bigl(f^2\,\frac{dy}{d\tau}
    \Bigr) = -H \sum_{j=5}^{7} (\hat u^j)^2 .$$

    Motion along an extra time pushes the particle towards the tip ($y$ falls); motion
    in 3-space does not push at all, and without extra-time motion $f\hat u^0$ is
    conserved: a motion along $x_0$ is blueshifted like $1/f$, as along an extra time.
    Second, the time $x_4$: the only symbols with upper index $x_4$ are
    $\Gamma^{x_4}{}_{x_0x_0} = \alpha_t h_0^2$, $\Gamma^{x_4}{}_{x_ix_i} = a_4' h_i^2$ and
    $\Gamma^{x_4}{}_{x_jx_j} = -\alpha_t h_j^2$, so

    $$\frac{du^4}{d\tau} = -a_4' \sum_{i=1}^{3} (\hat u^i)^2
    - \alpha_t\Bigl((\hat u^0)^2 - \sum_{j=5}^{7} (\hat u^j)^2\Bigr) .$$

    On a deflating history ($a_4' > 0$, $\alpha_t < 0$) motion in 3-space and along the
    extra times slows the $x_4$ velocity down, motion along $x_0$ speeds it up. Third, in
    frame velocities the squared length reads
    $g(u, u) = (\hat u^0)^2 + \sum_i (\hat u^i)^2 - (u^4)^2 - \sum_j (\hat u^j)^2$, so
    with $g(u, u) = -1$:

    $$(u^4)^2 = 1 + (\hat u^0)^2 + \sum_{i=1}^{3} (\hat u^i)^2
    - \sum_{j=5}^{7} (\hat u^j)^2 .$$

    The next cell checks all three with sympy for general $a_4(x_4)$ and $b_4(x_4)$.
    """),
    code(r'''
    frame = [h[k] * u[k] for k in range(8)]  # the frame velocities u-hat^a = h_a u^a
    space_squared = sum(frame[k] ** 2 for k in (1, 2, 3))  # 3-space part
    extra_squared = sum(frame[k] ** 2 for k in (5, 6, 7))  # extra-time part
    push = along_path(f_hidden * frame[0]) + H * extra_squared
    check(sp.simplify(push) == 0,
          "d(f u0 hat)/dtau = -H (extra-time frame velocities squared): only the extra "
          "times push along y")
    alpha_t = -sp.diff(a4, x4) + sp.diff(b4, x4) / (2 * b4)  # the rate of x0, x5..x7
    law_x4 = (along_path(u[4]) + sp.diff(a4, x4) * space_squared
              + alpha_t * (frame[0] ** 2 - extra_squared))
    check(sp.simplify(law_x4) == 0,
          "du4/dtau = -a4' (3-space frame velocities squared) - alpha_t (u0 hat^2 - "
          "extra-time ones squared)")
    in_frame = frame[0] ** 2 + space_squared - u[4] ** 2 - extra_squared
    check(sp.simplify(squared_length - in_frame) == 0,
          "g(u, u) written with the frame velocities")
    '''),
    md(r"""
    ## 9. The same quadratic form as the plane waves of the Revision record

    Multiply the last formula by $m^2$, the squared mass of the particle, and call
    $k_a = m\,\hat u^a$ its frame momenta and $E = m\,u^4$ its energy: then
    $E^2 = m^2 + k_0^2 + k_1^2 + k_2^2 + k_3^2 - k_5^2 - k_6^2 - k_7^2$. The Revision
    scope report `Revision/theory/reports/python-scope.json` has, in its check
    `extra_time_growth_rates_unbounded`, exactly this expression for plane waves of the
    fields in flat 4+4 space (or with the coefficients of the equation frozen at one
    instant): a wave $e^{i(k \cdot x - E x_4)}$ has $E^2$ equal to it, and when the
    extra-time momentum is so large that $E^2 < 0$, $E$ is imaginary and the wave grows
    exponentially in $x_4$ instead of oscillating. The next cell cuts the expression out
    of the record's text, turns it into sympy and compares it with $m^2 (u^4)^2$ of the
    particle. For the particle $(u^4)^2$ can never be negative; where a plane wave would
    start to grow, the particle instead would reach $u^4 = 0$, a **turning point** in
    $x_4$ (section 11). (That a wave packet of the fields follows such a path in the
    curved metric is not computed here.)
    """),
    code(r'''
    SCOPE = "Revision/theory/reports/python-scope.json"
    scope = json.loads(repository_file(SCOPE).read_text(encoding="utf-8"))
    growth = next(entry for entry in scope["checks"]
                  if entry["name"] == "extra_time_growth_rates_unbounded")
    form_text = growth["detail"].split("h_k^2 = (")[1].split(") I16")[0]  # the formula
    say(f"record ({growth['verdict']}): E^2 = {form_text}")
    k = sp.symbols("k0:8", real=True)  # frame momenta k0 ... k7 (k4 is not used)
    m = sp.symbols("m", positive=True)  # the mass
    form = parse_expr(form_text, local_dict={**{f"k{n}": k[n] for n in range(8)},
                                             "m": m})
    U = sp.symbols("U0:8", real=True)  # the frame velocities as plain symbols
    particle = m ** 2 * (1 + U[0] ** 2 + U[1] ** 2 + U[2] ** 2 + U[3] ** 2 - U[5] ** 2
                         - U[6] ** 2 - U[7] ** 2)  # m^2 (u^4)^2 from section 8
    same_form = sp.expand(form.subs({k[n]: m * U[n] for n in range(8)}) - particle)
    check(growth["verdict"] == "PASS" and same_form == 0,
          "m^2 (u4)^2 of the particle is the plane-wave E^2 of the record",
          record=f"{SCOPE}, check extra_time_growth_rates_unbounded")
    '''),
    md(r"""
    ## 10. Free fall computed step by step (RK4)

    Now the numbers. The next cell reads the history of the Revision Kohn-Sham record
    ($H = 1$, slope $A = 1$, so $a_4 = x_4$ and $a_4' = 1$; $\beta = 4/3$ and
    $b_4(0) = 1$, so $b_4 = e^{4x_4/3}$ and $b_4' = \tfrac43 b_4$) and its statement that
    this history is a prescribed background, and builds the tools of the computation:

    - `gamma_numbers`: the 31 symbols as fast numerical functions of $a_4$, $a_4'$,
      $x_0$, $H$, $b_4$ and $b_4'$ (`sp.lambdify` with the module `math`), with the warp
      factor written as $|\sin z|^{1/6}$;
    - `free_fall(state)`: the right-hand side of the 16 equations for the state
      $(x^0, \dots, x^7, u^0, \dots, u^7)$ on the history, with
      $b_4 = e^{\beta a_4}$ and $b_4' = \beta a_4' b_4$
      (entry $k$ of the state is $x^k$ and entry $8 + k$ is $u^k$);
    - `rk4_path(state0, tau_end, steps)`: the RK4 method, the same as in chapter 2,
      from $\tau = 0$ to `tau_end` in `steps` equal steps;
    - `start(y0, frame_velocity)`: the state at $\tau = 0$ at the point
      $x_4 = 0$, $y = y_0$ in the first half cell (all other coordinates 0) with the
      given frame velocities; $u^4$ is chosen so that $g(u, u) = -1$, by the last
      formula of section 8;
    - `describe(states)`: for every computed state the frame velocities, $y$,
      $g(u, u)$ and the scale factors.

    All particles start at $y_0 = -1$ (that is $z_0 = \arcsin e^{-6} = 0.0025$), on the
    slice $x_4 = 0$ where $a_4 = 0$.
    """),
    code(r'''
    import math  # sin, tan, exp, ... for single numbers (faster than numpy here)

    PARAMETERS = "Revision/kohn_sham/results/parameters.json"
    physics = json.loads(repository_file(PARAMETERS).read_text(encoding="utf-8"))
    H_value, A_value = physics["physics"]["H"], physics["physics"]["historyA"]
    beta = physics["physics"]["historyBeta"]  # b4 = b4(0) e^(beta A H x4)
    status = ks_theory["adiabaticity"]["historyStatus"]
    say(f"H = {H_value}, A = {A_value}, beta = {beta:.6f}, b4(0) = "
        f"{physics['physics']['historyB4AtZero']}; record: "
        + status.split(". ")[0] + ".")
    check(H_value == 1.0 and A_value == 1.0 and abs(beta - 4.0 / 3.0) < 1e-15
          and physics["physics"]["historyB4AtZero"] == 1.0
          and status.startswith("PRESCRIBED BACKGROUND"),
          "the history of the record: a4 = A H x4, b4 = b4(0) e^(beta A H x4) with A = 1, "
          "H = 1, beta = 4/3, b4(0) = 1, prescribed",
          record=f"{PARAMETERS}, physics.H, physics.historyA, physics.historyBeta and "
                 f"physics.historyB4AtZero; {KS_THEORY}, adiabaticity.historyStatus")
    ARGUMENTS = (a4v, a4p, x0, H, b4v, b4p)
    warp_numbers = {W(x0): sp.Abs(sp.sin(6 * H * x0)) ** sp.Rational(1, 6)}  # W = ...
    gamma_numbers = [(a, b, c, sp.lambdify(ARGUMENTS, value.subs(warp_numbers), "math"))
                     for (a, b, c), value in sorted(Gamma.items())]
    ETA_N = np.array(ETA, dtype=float)  # the signs as numbers


    def free_fall(state):
        """d state/d tau for state = (x0..x7, u0..u7) on the history a4 = A H x4,
        b4 = e^(beta a4) (b4(0) = 1)."""
        x, v = state[:8], state[8:]
        a4_now, rate = A_value * H_value * x[4], A_value * H_value  # a4 and a4'
        b4_now = math.exp(beta * a4_now)  # b4 on the history
        b4_rate = beta * rate * b4_now  # b4' = beta a4' b4
        change = np.zeros(8)
        for a, b, c, f in gamma_numbers:  # du^a/dtau = - sum Gamma^a_bc u^b u^c
            change[a] -= f(a4_now, rate, x[0], H_value, b4_now, b4_rate) * v[b] * v[c]
        return np.concatenate([v, change])


    def rk4_path(state0, tau_end, steps):
        """RK4 from tau = 0 to tau_end; returns the times and the states (rows)."""
        dt = tau_end / steps
        states = np.zeros((steps + 1, 16))
        states[0] = state0
        for n in range(steps):
            s = states[n]
            k1 = free_fall(s)
            k2 = free_fall(s + dt / 2 * k1)
            k3 = free_fall(s + dt / 2 * k2)
            k4 = free_fall(s + dt * k3)
            states[n + 1] = s + dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        return np.linspace(0.0, tau_end, steps + 1), states


    def scale_numbers(x):
        """The eight scale factors h_a at the point x on the history (numbers)."""
        a4_now, z_now = A_value * H_value * x[4], 6 * H_value * x[0]
        f_now = math.exp(-a4_now) * math.sqrt(math.exp(beta * a4_now))  # f
        w = abs(math.sin(z_now)) ** (1 / 6)  # the warp factor W
        return np.array([f_now / math.tan(z_now)] + [math.exp(a4_now)] * 3 + [1.0]
                        + [f_now * w] * 3)


    def start(y0, frame_velocity):
        """The state at tau = 0: x4 = 0, y = y0, frame velocities as given (the entry
        for x4 is replaced by the value that makes g(u, u) = -1)."""
        x = np.zeros(8)
        x[0] = math.asin(math.exp(6 * H_value * y0)) / (6 * H_value)  # sin z = e^(6Hy)
        w = np.array(frame_velocity, dtype=float)
        w[4] = 0.0
        w[4] = math.sqrt(1.0 + np.sum(ETA_N * w ** 2))  # (u^4)^2 = 1 + sum eta w^2
        return np.concatenate([x, w / scale_numbers(x)])  # u^a = u-hat^a / h_a


    def describe(states):
        """Frame velocities (rows), the coordinate y, g(u, u) and the scale factors."""
        h_rows = np.array([scale_numbers(s[:8]) for s in states])
        frame_rows = h_rows * states[:, 8:]
        y_values = np.log(np.abs(np.sin(6 * H_value * states[:, 0]))) / (6 * H_value)
        lengths = np.sum(ETA_N * frame_rows ** 2, axis=1)  # g(u, u)
        return frame_rows, y_values, lengths, h_rows


    Y0 = -1.0  # the starting height of every particle
    say(f"start: y0 = {Y0}, z0 = {math.asin(math.exp(6 * Y0)):.6f}")
    '''),
    md(r"""
    **The particle at rest.** The first particle starts at rest: all frame velocities
    are $0$ except $u^4 = 1$. Notebook 03b showed that $\Gamma^a{}_{x_4x_4} = 0$ for
    every $a$, so it must stay at rest, with $x_4 = \tau$: its clock shows the time
    $x_4$. The next cell integrates its path from $\tau = 0$ to $\tau = 3$ in 3000
    steps and checks this.
    """),
    code(r'''
    tau, rest = rk4_path(start(Y0, [0.0] * 8), 3.0, 3000)
    others = [0, 1, 2, 3, 5, 6, 7]  # every coordinate except x4
    moved = np.max(np.abs(rest[:, others] - rest[0, others]))
    check(moved == 0.0 and np.max(np.abs(rest[:, 4] - tau)) < 1e-12
          and np.max(np.abs(rest[:, 12] - 1.0)) < 1e-12,
          "the particle at rest stays at rest and x4 equals its proper time")
    '''),
    md(r"""
    **Three particles moving in 3-space.** The next three particles start with the
    frame velocities $\hat u^1 = 0.25$, $0.5$ and $1$ along $x_1$, so
    $u^4 = \sqrt{1 + (\hat u^1)^2}$. (The velocity that an
    observer at rest at the particle's place measures is $\hat u^1/u^4$; for
    $\hat u^1 = 1$ it is $1/\sqrt 2 = 0.71$ times the velocity of light, which is $1$
    in these units.) The next cell integrates each from $\tau = 0$ to $3$ in 3000
    steps and checks on every computed state: the momentum $p_1 = g_{11} u^1$ stays
    constant (relative change below $10^{-9}$); $g(u, u)$ stays $-1$; the frame velocity
    equals $p_1 \kappa = p_1 e^{-a_4}$ (section 7); $u^4$ decreases at every step
    (section 8); and the particle does not move along the hidden direction at all: its
    $x_0$, and so its $y$, stays exactly where it started (section 8: 3-space motion
    pushes nothing). It reports the final values for the fastest particle.
    """),
    code(r'''
    SPEEDS = (0.25, 0.5, 1.0)  # starting frame velocities along x1
    space_paths = {}
    for speed in SPEEDS:
        tau, states = rk4_path(start(Y0, [0, speed, 0, 0, 0, 0, 0, 0]), 3.0, 3000)
        frame_rows, y_values, lengths, h_rows = describe(states)
        p1 = h_rows[:, 1] ** 2 * states[:, 9]  # p_1 = g_11 u^1 = h_1^2 u^1
        weight = np.exp(-A_value * H_value * states[:, 4])  # kappa = e^(-a4)
        space_paths[speed] = (states, frame_rows, y_values, lengths, p1)
        check(np.max(np.abs(p1 / p1[0] - 1)) < 1e-9
              and np.max(np.abs(lengths + 1)) < 1e-9
              and np.max(np.abs(frame_rows[:, 1] - p1[0] * weight)) < 1e-9
              and np.all(np.diff(states[:, 12]) < 0)
              and np.all(states[:, 0] == states[0, 0]),
              f"3-space speed {speed}: p1 and g(u, u) conserved, frame velocity "
              "p1 kappa, u4 falls, x0 fixed")
    states, frame_rows, y_values, lengths, p1 = space_paths[1.0]
    report("fastest particle at tau = 3: x4", f"{states[-1, 4]:.4f}")
    report("fastest particle at tau = 3: frame velocity along x1",
           f"{frame_rows[-1, 1]:.6f}")
    report("fastest particle at tau = 3: u4", f"{states[-1, 12]:.6f}")
    report("fastest particle at tau = 3: height y", f"{y_values[-1]:.4f}")
    '''),
    md(r"""
    ## 11. A particle moving along an extra time: the fall towards the tip

    The last particle starts with the frame velocity $\hat u^5 = 0.2$ along the extra
    time $x_5$, so $u^4 = \sqrt{1 - 0.04} = 0.980$ (rounded). Along the deflating
    history its frame velocity $-p_5\, b_4^{-1/2} e^{a_4 - Hy}$ (on this history
    proportional to $e^{a_4/3 - Hy}$) grows, and by section 8 the extra-time motion
    pushes it towards the tip, where $e^{-Hy}$ is larger: it falls faster and faster.
    For this particle (no 3-space motion) the law of section 8 together with
    $(u^4)^2 = 1 + (\hat u^0)^2 - (\hat u^5)^2$ closes on $u^4$ alone:
    $du^4/d\tau = -\alpha_t\bigl((u^4)^2 - 1\bigr)$, and on the history
    $\alpha_t = -AH/3$. With $q = (1 - u^4)/(1 + u^4)$ this is $dq/d\tau = (2AH/3)\,q$
    (the quotient rule), so

    $$q(\tau) = q(0)\,e^{2AH\tau/3}, \qquad u^4(\tau) = \frac{1 - q(\tau)}{1 + q(\tau)} :$$

    $u^4$ falls, and would reach $0$ (a turning point) at
    $\tau = \frac{3}{2AH}\ln\frac{1}{q(0)}$. The next cell integrates the path in steps
    of $0.001$ until the particle passes the tip cut-off $y = -L = -3$ of the Revision
    Kohn-Sham solver, checks the conservation laws, checks that $u^4$ follows the exact
    formula on every step, and reports where the particle is when it passes the
    cut-off, and the instant of the turning point that the formula predicts.

    The cell also prints the definition of the **good sector** of the Revision
    Kohn-Sham work: its states have no dependence on $x_5, x_6, x_7$, that is no
    extra-time momenta (the reason, from the quantum theory, comes in a later chapter).
    For a classical particle without extra-time momentum, $(u^4)^2 = 1 + (\hat u^0)^2 +
    \sum_i (\hat u^i)^2 \ge 1$: such a particle never has a turning point, and nothing
    pushes it towards the tip.
    """),
    code(r'''
    L_tip = physics["physics"]["L_tipCutoff"]  # the tip cut-off of the record, 3/H
    DT = 0.001  # the step of RK4
    path = [start(Y0, [0, 0, 0, 0, 0, 0.2, 0, 0])]
    while math.log(abs(math.sin(6 * H_value * path[-1][0]))) / (6 * H_value) > -L_tip:
        s = path[-1]  # one RK4 step, as in rk4_path
        k1 = free_fall(s)
        k2 = free_fall(s + DT / 2 * k1)
        k3 = free_fall(s + DT / 2 * k2)
        k4 = free_fall(s + DT * k3)
        path.append(s + DT / 6 * (k1 + 2 * k2 + 2 * k3 + k4))
    extra = np.array(path)  # the states, until the first one beyond the cut-off
    tau_t = DT * np.arange(len(extra))  # their proper times
    frame_t, y_t, lengths_t, h_t = describe(extra)
    p5 = -h_t[:, 5] ** 2 * extra[:, 13]  # p_5 = g_55 u^5 = -h_5^2 u^5
    q0 = (1 - extra[0, 12]) / (1 + extra[0, 12])  # q(0) of the exact law
    q_line = q0 * np.exp(2 * A_value * H_value * tau_t / 3)
    exact_u4 = (1 - q_line) / (1 + q_line)  # the exact solution for u4
    check(np.max(np.abs(p5 / p5[0] - 1)) < 1e-8 and np.max(np.abs(lengths_t + 1)) < 1e-8
          and np.all(np.diff(extra[:, 12]) < 0) and np.all(np.diff(y_t) < 0),
          "extra-time particle: p5 and g(u, u) conserved, u4 decreases, y falls")
    check(np.max(np.abs(extra[:, 12] - exact_u4)) < 1e-9,
          "u4 follows the exact law (1 - q0 e^(2 tau/3))/(1 + q0 e^(2 tau/3)) on every step")
    tau_turn = 3 / (2 * A_value * H_value) * math.log(1 / q0)  # where u4 would be 0
    report("tip cut-off y = -3 passed at the proper time tau", f"{tau_t[-1]:.3f}")
    report("time x4 there", f"{extra[-1, 4]:.4f}")
    report("frame velocity along x5 there", f"{frame_t[-1, 5]:.4f}")
    report("frame velocity along y there", f"{frame_t[-1, 0]:.4f}")
    report("u4 there", f"{extra[-1, 12]:.6f}")
    report("turning point predicted by the exact law at tau", f"{tau_turn:.3f}")
    say("record, sectorAndAnsatz.sector: " + ks_theory["sectorAndAnsatz"]["sector"])
    check("extra-time momenta zero" in ks_theory["sectorAndAnsatz"]["sector"]
          and tau_t[-1] < tau_turn,
          "the good sector of the Kohn-Sham record has no extra-time momenta; the "
          "extra-time particle reaches the tip cut-off before any turning point",
          record=f"{KS_THEORY}, sectorAndAnsatz.sector")
    '''),
    md(r"""
    ## 12. Pictures of free fall

    The next cell draws the frame velocities. Left: the three particles that move in
    3-space, their frame velocity $\hat u^1$ against the time $x_4$ on a logarithmic
    axis, computed by RK4 (solid lines), together with the pure redshift
    $\hat u^1(0)\, e^{-a_4}$ (dotted lines; on a logarithmic axis straight lines of
    slope $-1$): the two agree on every step, because 3-space has no warp and the
    particles stay at their height. Right: the particle moving along the extra time
    $x_5$, its frame velocities $\hat u^5$ and $|\hat u^0|$ against $x_4$ until it passes
    the tip cut-off, together with the pure blueshift
    $0.2\, b_4^{-1/2} e^{a_4} = 0.2\, e^{a_4/3}$ (dotted); $\hat u^5$ grows faster than
    $e^{a_4/3}$ because the particle sinks towards the tip, where $e^{-Hy}$ is larger,
    and the speed $|\hat u^0|$ of its fall grows with it.
    """),
    code(r'''
    BLUE, ORANGE, AQUA, YELLOW = "#2a78d6", "#eb6834", "#1baf7a", "#eda100"
    MAGENTA, GREEN, VIOLET, RED = "#e87ba4", "#008300", "#4a3aa7", "#e34948"
    COLOURS = {0.25: AQUA, 0.5: ORANGE, 1.0: RED}  # one colour per 3-space particle
    fig, axes = plt.subplots(1, 2, figsize=(10.5, 4.3))
    fig.subplots_adjust(wspace=0.3)  # room for the label of the right vertical axis
    for speed in SPEEDS:
        states, frame_rows = space_paths[speed][0], space_paths[speed][1]
        axes[0].plot(states[:, 4], frame_rows[:, 1], color=COLOURS[speed], lw=1.8,
                     label=f"RK4, start {speed:g}")
        axes[0].plot(states[:, 4], speed * np.exp(-A_value * H_value * states[:, 4]),
                     ":", color="black", lw=1.2)
    axes[0].plot([], [], ":", color="black", label="pure redshift $e^{-a_4}$")
    axes[0].set_yscale("log")
    axes[0].set_xlabel("time $x_4$ (unit $1/H$), history $a_4 = x_4$, "
                       "$b_4 = e^{4x_4/3}$")
    axes[0].set_ylabel("frame velocity $\\hat u^1$ along $x_1$")
    axes[0].set_title("3-space: redshift")
    axes[0].legend(fontsize=8)
    axes[1].plot(extra[:, 4], frame_t[:, 5], color=VIOLET, lw=1.8,
                 label="RK4: $\\hat u^5$, start 0.2")
    axes[1].plot(extra[1:, 4], np.abs(frame_t[1:, 0]), color=AQUA, lw=1.8, ls="--",
                 label="RK4: $|\\hat u^0|$, speed of the fall")
    blue_rate = (1 - beta / 2) * A_value * H_value  # b4^(-1/2) e^(a4) = e^(a4/3)
    axes[1].plot(extra[:, 4], 0.2 * np.exp(blue_rate * extra[:, 4]),
                 ":", color="black", lw=1.4, label="pure blueshift $0.2\\,e^{a_4/3}$")
    axes[1].axvline(extra[-1, 4], color="grey", lw=1.0, ls="-.",
                    label="tip cut-off $y = -3$ reached")
    axes[1].set_yscale("log")
    axes[1].set_xlabel("time $x_4$ (unit $1/H$), history $a_4 = x_4$, "
                       "$b_4 = e^{4x_4/3}$")
    axes[1].set_ylabel("frame velocity")
    axes[1].set_title("Extra time: blueshift and fall")
    axes[1].legend(fontsize=8, loc="upper left")
    save_figure(fig, "frame_velocities",
                "Frame velocities of freely falling test particles in the corrected "
                "metric along the deflating history $a_4 = x_4$, $b_4 = e^{4x_4/3}$ "
                "($A = 1$, $H = 1$, $\\beta = 4/3$), all started "
                "at $x_4 = 0$, $y = -1$, computed with RK4 from the Christoffel symbols "
                "of the Revision record; horizontal axes the time $x_4$ in units of "
                "$1/H$, vertical axes the frame velocity (proper length per proper "
                "time, a pure number) on logarithmic scales. Left: three particles "
                "started along $x_1$ with $0.25$, $0.5$ and $1$; their frame velocity "
                "falls exactly like the pure redshift $e^{-a_4}$ (dotted), because "
                "3-space has no warp. Right: a particle started along the extra time "
                "$x_5$ with $0.2$; its frame velocity $\\hat u^5$ (solid) grows faster "
                "than the pure blueshift $0.2\\,e^{a_4/3}$ (dotted), and the speed "
                "$|\\hat u^0|$ of its fall along the hidden direction (dashed) grows "
                "with it, until it passes the tip cut-off of the Kohn-Sham solver at "
                f"$x_4 = {extra[-1, 4]:.3f}$ (dash-dotted).")
    check(np.all(frame_t[1:, 5] > 0.2 * np.exp(blue_rate * extra[1:, 4])),
          "the extra-time frame velocity grows faster than the pure blueshift")
    '''),
    md(r"""
    The next cell draws the $x_4$ velocity $u^4$ (left) and the time $x_4$ itself
    (right) against the proper time $\tau$ for all five particles. The particle at rest
    keeps $u^4 = 1$. The particles in 3-space start with $u^4 = \sqrt{1 + (\hat u^1)^2}$
    and slow down towards $1$ as their frame velocity is redshifted away. The particle
    on the extra time starts with $u^4 = 0.98$ and slows down exactly as the formula of
    section 11 says (the dots are the formula); it passes the tip cut-off long before
    the turning point that the formula predicts, which lies outside the plot.
    """),
    code(r'''
    fig, axes = plt.subplots(1, 2, figsize=(10.5, 4.3))
    fig.subplots_adjust(wspace=0.3)
    axes[0].plot(tau, rest[:, 12], color="black", lw=1.4, ls="--", label="at rest")
    axes[1].plot(tau, rest[:, 4], color="black", lw=1.4, ls="--", label="at rest")
    for speed in SPEEDS:
        states = space_paths[speed][0]
        axes[0].plot(tau, states[:, 12], color=COLOURS[speed], lw=1.8,
                     label=f"3-space, start {speed:g}")
        axes[1].plot(tau, states[:, 4], color=COLOURS[speed], lw=1.8,
                     label=f"3-space, start {speed:g}")
    axes[0].plot(tau_t, extra[:, 12], color=VIOLET, lw=1.8, ls="-.",
                 label="extra time, start 0.2")
    axes[0].plot(tau_t[::200], exact_u4[::200], "o", color=VIOLET, ms=5,
                 label="exact law of section 11")
    axes[1].plot(tau_t, extra[:, 4], color=VIOLET, lw=1.8, ls="-.",
                 label="extra time, start 0.2")
    axes[0].set_ylabel("$x_4$ velocity $u^4 = dx_4/d\\tau$")
    axes[1].set_ylabel("time $x_4$ (unit $1/H$)")
    axes[0].set_title("The $x_4$ velocity")
    axes[1].set_title("The time $x_4$ along each path")
    for ax, place in zip(axes, ("upper right", "upper left")):  # legends off the lines
        ax.set_xlabel("proper time $\\tau$ of the particle (unit $1/H$)")
        ax.legend(fontsize=8, loc=place)
    save_figure(fig, "x4_velocity",
                "The $x_4$ velocity $u^4 = dx_4/d\\tau$ (left) and the time $x_4$ "
                "(right) of five freely falling test particles against their own proper "
                "time $\\tau$ in units of $1/H$, along the deflating history $a_4 = x_4$, "
                "$b_4 = e^{4x_4/3}$, computed with RK4: a particle at rest (dashed, "
                "$u^4 = 1$ and $x_4 = \\tau$), three particles moving in 3-space (solid, "
                "started with frame velocities $0.25$, $0.5$, $1$), whose $u^4$ falls "
                "towards $1$ as their motion is redshifted, and a particle moving along "
                "an extra time (dash-dotted, started with $0.2$), whose $u^4$ falls "
                "exactly as the law $u^4 = (1 - q)/(1 + q)$, $q = q(0)e^{2\\tau/3}$, "
                f"says (dots) until it passes the tip cut-off at $\\tau = {tau_t[-1]:.2f}$; "
                f"the formula puts its turning point at $\\tau = {tau_turn:.2f}$.")
    check(np.all(np.diff(space_paths[1.0][0][:, 4]) > 0)
          and np.all(np.diff(extra[:, 4]) > 0),
          "every particle keeps advancing in x4 along the computed paths")
    '''),
    md(r"""
    The next cell shows the push along the hidden direction. Left: the height $y$ of
    every particle against $\tau$; the particle at rest and the particles in 3-space
    stay at $y = -1$ (no push), the particle on the extra time sinks towards the tip,
    until it passes the tip cut-off $y = -3$ of the Revision Kohn-Sham solver (dotted
    line). Right: the rate $d(f\hat u^0)/d\tau$ computed from the RK4 states by a
    numerical derivative (`np.gradient`, central differences) as dots, and the exact law
    $-H\sum_j (\hat u^j)^2$ of section 8 as a line, for the extra-time particle. The cell
    checks the agreement relative to the size of the law along the path (the particle
    speeds up sharply near the cut-off, and the error of the central differences, of
    order $\Delta\tau^2$ times the third derivative, grows with it).
    """),
    code(r'''
    fig, axes = plt.subplots(1, 2, figsize=(10.5, 4.3))
    fig.subplots_adjust(wspace=0.3)
    axes[0].plot(tau, np.full_like(tau, Y0), color="black", lw=1.4, ls="--",
                 label="at rest and 3-space (all at $y = -1$)")
    axes[0].plot(tau_t, y_t, color=VIOLET, lw=1.8, ls="-.", label="extra time, start 0.2")
    axes[0].axhline(0.0, color="grey", lw=1.0, label="fold $y = 0$")
    axes[0].axhline(-L_tip, color="grey", lw=1.0, ls=":", label="tip cut-off $y = -3$")
    axes[0].set_xlabel("proper time $\\tau$ (unit $1/H$)")
    axes[0].set_ylabel("height $y$ in the hidden direction (unit $1/H$)")
    axes[0].set_title("Only the extra-time motion pushes along $y$")
    axes[0].set_ylim(-3.6, 0.4)
    axes[0].legend(fontsize=7, loc="lower left")
    f_numbers = np.exp(-(1 - beta / 2) * A_value * H_value * extra[:, 4])  # f on path
    law = -H_value * np.sum(frame_t[:, 5:8] ** 2, axis=1)  # -H sum of squares
    numeric = np.gradient(f_numbers * frame_t[:, 0], tau_t)  # d(f u0 hat)/dtau
    largest_gap = float(np.max(np.abs(numeric - law)[1:-1]) / np.max(np.abs(law)))
    space_push = max(float(np.max(np.abs(space_paths[s][2] - Y0))) for s in SPEEDS)
    axes[1].plot(tau_t, law, color=VIOLET, lw=1.8, label="law $-H\\sum_j(\\hat u^j)^2$")
    axes[1].plot(tau_t[::100], numeric[::100], "o", color=VIOLET, ms=5,
                 label="from RK4, numerical derivative")
    axes[1].axhline(0.0, color="grey", lw=0.8)
    axes[1].set_xlabel("proper time $\\tau$ (unit $1/H$)")
    axes[1].set_ylabel("$d(f\\hat u^0)/d\\tau$ (unit $H$)")
    axes[1].set_title("The push: $-H$ times the extra-time squares")
    axes[1].legend(fontsize=7, loc="lower left")
    report("largest difference between the numerical rate and the law, relative to the "
           "largest value of the law", f"{largest_gap:.1e}")
    save_figure(fig, "hidden_push",
                "The push along the hidden direction on freely falling test particles in "
                "the corrected metric along the deflating history $a_4 = x_4$, "
                "$b_4 = e^{4x_4/3}$, computed with RK4; horizontal axes the proper time "
                "$\\tau$ in units of $1/H$. Left: the height $y$ (unit $1/H$) of the "
                "particle at rest and of the three particles moving in 3-space (dashed, "
                "all stay at $y = -1$: 3-space motion does not push) and of a particle "
                "moving along an extra time (dash-dotted), which sinks ever faster "
                "towards the tip until it passes the tip cut-off $y = -3$ of the "
                "Revision Kohn-Sham solver (dotted). Right: the rate "
                "$d(f\\hat u^0)/d\\tau$ (unit $H$) of the extra-time particle obtained "
                "from the computed states by a numerical derivative (dots) agrees with "
                "the exact law $-H$ times the squared extra-time frame velocity (line).")
    check(largest_gap < 1e-4 and space_push == 0.0,
          "the computed rate agrees with the exact push law; 3-space motion does not "
          "change y")
    '''),
    md(r"""
    The next cell draws the quadratic form of section 9 as a map. For a particle that
    moves only along $x_5$ and $y$, $(u^4)^2 = 1 + (\hat u^0)^2 - (\hat u^5)^2$. The map
    shows this number over the plane of $\hat u^5$ (horizontal) and $\hat u^0$
    (vertical): white where it is positive, grey where it is negative. On the grey side a
    plane wave with these frame momenta (times $m$) would grow instead of oscillating,
    according to the record's check `extra_time_growth_rates_unbounded`; a particle can
    never be there, because $(u^4)^2 \ge 0$. The curve $(\hat u^5)^2 = 1 + (\hat u^0)^2$
    separates the two regions. The path of the extra-time particle (violet) starts at
    $(0.2, 0)$ and moves right (blueshift) and down (it falls towards the tip), along a
    line that keeps its distance from the curve: by the exact law,
    $(\hat u^5)^2 - (\hat u^0)^2 = 1 - (u^4)^2$ grows only slowly.
    """),
    code(r'''
    top5 = float(np.ceil(frame_t[:, 5].max())) + 0.5  # the plotted range of u5 hat
    low0 = float(np.floor(frame_t[:, 0].min())) - 0.5  # the plotted range of u0 hat
    grid5, grid0 = np.meshgrid(np.linspace(0.0, top5, 451), np.linspace(low0, 0.5, 501))
    squared_u4 = 1 + grid0 ** 2 - grid5 ** 2  # (u^4)^2 over the plane
    fig, ax = plt.subplots(figsize=(6.4, 5.2))
    ax.contourf(grid5, grid0, squared_u4, levels=[-1000.0, 0.0], colors=["#d9d9d9"])
    ax.contour(grid5, grid0, squared_u4, levels=[0.0], colors="black", linewidths=1.2)
    ax.plot(frame_t[:, 5], frame_t[:, 0], color=VIOLET, lw=2.0,
            label="path of the extra-time particle")
    ax.plot([frame_t[0, 5]], [frame_t[0, 0]], "s", color=VIOLET, ms=7, label="start")
    ax.plot([frame_t[-1, 5]], [frame_t[-1, 0]], "o", color=VIOLET, ms=8,
            label="tip cut-off $y = -3$ passed")
    ax.text(0.62 * top5, 0.35 * low0, "$(u^4)^2 < 0$:\nno particle;\nplane waves grow",
            fontsize=8)
    ax.text(0.08 * top5, 0.75 * low0, "$(u^4)^2 > 0$", fontsize=9)
    ax.set_xlabel("frame velocity $\\hat u^5$ along the extra time $x_5$")
    ax.set_ylabel("frame velocity $\\hat u^0 = f\\,dy/d\\tau$")
    ax.set_title("The quadratic form $(u^4)^2 = 1 + (\\hat u^0)^2 - (\\hat u^5)^2$")
    ax.grid(False)
    ax.legend(fontsize=8, loc="lower left")
    save_figure(fig, "quadratic_form",
                "The squared $x_4$ velocity $(u^4)^2 = 1 + (\\hat u^0)^2 - (\\hat u^5)^2$ "
                "of a free particle that moves along the extra time $x_5$ and the "
                "hidden coordinate $y$, as a map over its frame velocities $\\hat u^5$ "
                "(horizontal) and $\\hat u^0$ (vertical), both pure numbers: white where "
                "it is positive, grey where it is negative, the black curve "
                "$(\\hat u^5)^2 = 1 + (\\hat u^0)^2$ between them. Multiplied by $m^2$ it "
                "is the squared frequency of a plane wave in the Revision record "
                "(check extra_time_growth_rates_unbounded), which grows instead of "
                "oscillating in the grey region. The violet path of the extra-time "
                "particle of this notebook (RK4, history $a_4 = x_4$, "
                "$b_4 = e^{4x_4/3}$) starts at $(0.2, 0)$ (square) and runs right and "
                "down, at a distance from the curve, until it passes the tip cut-off "
                "(dot).")
    check(np.all(1 + frame_t[:, 0] ** 2 - frame_t[:, 5] ** 2 > 0.03),
          "the path stays in the region where (u4)^2 > 0, away from the curve")
    '''),
    md(r"""
    ## 13. How accurate is the computation?

    Two tests. First, the conserved quantities: the next cell draws, against $\tau$, how
    far the computed $p_1$ (fastest 3-space particle), $p_5$ (extra-time particle) and
    $g(u, u)$ (both) drift from their starting values, on a logarithmic axis. Second,
    the order of RK4: it integrates both particles from $\tau = 0$ to $2$ with
    $50, 100, 200, 400, 800, 1600$ steps and measures the largest difference of the end
    states of two successive step sizes; for a method of order 4 each halving of the
    step divides this difference by about $2^4 = 16$, so on logarithmic axes the points
    lie on a line of slope 4.
    """),
    code(r'''
    from matplotlib.ticker import NullFormatter  # an empty label for minor ticks

    p1_fast = space_paths[1.0][4]  # p_1 along the fastest 3-space path
    drift = {"$p_1$, 3-space particle": (tau, np.abs(p1_fast / p1_fast[0] - 1)),
             "$g(u,u) + 1$, 3-space particle": (tau, np.abs(space_paths[1.0][3] + 1)),
             "$p_5$, extra-time particle": (tau_t, np.abs(p5 / p5[0] - 1)),
             "$g(u,u) + 1$, extra-time particle": (tau_t, np.abs(lengths_t + 1))}
    STEPS = (50, 100, 200, 400, 800, 1600)
    differences = {}
    for label, state0 in (("3-space, start 1", start(Y0, [0, 1, 0, 0, 0, 0, 0, 0])),
                          ("extra time, start 0.2", start(Y0, [0, 0, 0, 0, 0, 0.2, 0, 0]))):
        ends = [rk4_path(state0, 2.0, n)[1][-1] for n in STEPS]
        differences[label] = np.array([np.max(np.abs(ends[i] - ends[i + 1]))
                                       for i in range(len(STEPS) - 1)])
        ratios = differences[label][:-1] / differences[label][1:]
        say(f"  {label}: ratios of successive differences "
            + ", ".join(f"{r:.1f}" for r in ratios))
    fig, axes = plt.subplots(1, 2, figsize=(10.5, 4.3))
    fig.subplots_adjust(wspace=0.3)
    for (label, (t_values, values)), colour, style in zip(
            drift.items(), (RED, ORANGE, VIOLET, AQUA), ("-", "--", "-.", ":")):
        axes[0].semilogy(t_values[1:], np.maximum(values[1:], 1e-17), color=colour,
                         ls=style, lw=1.6, label=label)
    axes[0].set_xlabel("proper time $\\tau$ (unit $1/H$)")
    axes[0].set_ylabel("relative drift from the start")
    axes[0].set_title("Conserved quantities, RK4 with step $0.001$")
    axes[0].legend(fontsize=7, loc="lower right")
    dts = 2.0 / np.array(STEPS[:-1])  # the larger step of each pair
    for (label, values), colour in zip(differences.items(), (RED, VIOLET)):
        axes[1].loglog(dts, values, "o-", color=colour, lw=1.6, label=label)
    axes[1].loglog(dts, differences["extra time, start 0.2"][0] * (dts / dts[0]) ** 4,
                   "--", color="black", lw=1.0, label="slope 4")
    axes[1].set_xticks(dts, [f"{dt:g}" for dt in dts])  # the five steps as labels
    axes[1].xaxis.set_minor_formatter(NullFormatter())  # no labels between them
    axes[1].set_xlabel("step $\\Delta\\tau$ of RK4")
    axes[1].set_ylabel("difference of end states (step and half step)")
    axes[1].set_title("RK4 is of order 4")
    axes[1].legend(fontsize=8)
    drift_largest = max(float(np.max(values)) for _, values in drift.values())
    save_figure(fig, "accuracy",
                "The accuracy of the RK4 computation of free fall in the corrected "
                "metric along the deflating history $a_4 = x_4$, $b_4 = e^{4x_4/3}$. "
                "Left: the relative drift of "
                "the conserved momentum $p_1$ and of $g(u, u) + 1$ for the 3-space "
                "particle started with frame velocity $1$, and of $p_5$ and "
                "$g(u, u) + 1$ for the extra-time particle started with $0.2$, against "
                "the proper time $\\tau$ in units of $1/H$, logarithmic vertical axis; "
                "all stay below $10^{-8}$ (the extra-time particle drifts more "
                "because its velocities grow). Right: the largest difference between "
                "the end states at $\\tau = 2$ computed with the step $\\Delta\\tau$ and "
                "with half of it, against $\\Delta\\tau$ on logarithmic axes, for the "
                "same two particles; the points follow the dashed line of slope 4: "
                "halving the step makes the error 16 times smaller.")
    all_ratios = np.concatenate([d[1:-1] / d[2:] for d in differences.values()])
    check(np.all((all_ratios > 14) & (all_ratios < 18)) and drift_largest < 1e-8,
          "halving the RK4 step divides the error by 14 to 18: order 4; drifts below 1e-8")
    '''),
    md(r"""
    ## 14. The last check

    The last cell checks that the five figure files exist in the folder
    Revision/textbook/figures and prints the number of checks that passed.
    """),
    code(r'''
    figure_names = ["frame_velocities", "x4_velocity", "hidden_push", "quadratic_form",
                    "accuracy"]
    files = [output_file(f"{FIGURE_FOLDER}/03d_{n}_{name}.png")
             for n, name in enumerate(figure_names, 1)]
    check(all(path.is_file() for path in files), "all five figure files exist")
    all_checks_passed()
    '''),
    md(r"""
    ## 15. What this notebook showed

    - PROVED (exact, sympy, for all functions $a_4(x_4)$ and $b_4(x_4)$ and every real
      $z$, with the Christoffel symbols of the Revision record): in free fall the six
      momenta $p_a = g_{aa} u^a$ of $x_1, x_2, x_3, x_5, x_6, x_7$ and the squared
      length $g(u, u)$ are conserved; the frame velocity in 3-space is $p_1 e^{-a_4}$
      at every height (the momentum weight $\kappa = e^{-a_4}$ of the Revision
      Kohn-Sham record) and along an extra time $-p_5 b_4^{-1/2} e^{a_4 - Hy}$;
      $d(f\hat u^0)/d\tau = -H\sum_j (\hat u^j)^2$;
      $du^4/d\tau = -a_4'\sum_i (\hat u^i)^2 - \alpha_t((\hat u^0)^2 - \sum_j
      (\hat u^j)^2)$ with $\alpha_t = -a_4' + b_4'/(2b_4)$; and
      $(u^4)^2 = 1 + (\hat u^0)^2 + \sum_i (\hat u^i)^2 - \sum_j (\hat u^j)^2$, which,
      times $m^2$, is the quadratic form of the plane-wave check of the Revision scope
      report.
    - So along a deflating history ($a_4' > 0$ and $\alpha_t < 0$) motion in 3-space
      is redshifted like $e^{-a_4}$ and motion along an extra time (and along $x_0$) is
      blueshifted like $b_4^{-1/2} e^{a_4}$, on the history of this notebook like
      $e^{a_4/3}$; only extra-time motion pushes a particle along $y$, towards the tip;
      3-space motion pushes nothing. For a particle without 3-space motion the $x_4$
      velocity obeys $du^4/d\tau = -\alpha_t((u^4)^2 - 1)$, solved exactly on the history.
    - COMPUTED (RK4 with the step $0.001$, along the prescribed history $a_4 = x_4$,
      $b_4 = e^{4x_4/3}$, $H = 1$, from $y = -1$): a particle at rest stays at rest with
      $x_4 = \tau$; three particles moving in 3-space slow down exactly like the
      redshift and stay at their height; a particle started along the extra time $x_5$
      with frame velocity $0.2$ falls ever faster towards the tip and passes the tip
      cut-off $y = -3$ of the Kohn-Sham solver (the RESULT lines above) long before the
      turning point that its exact law predicts; every exact law holds on the computed
      paths, and RK4 shows its order 4.
    - A particle without extra-time momentum has $(u^4)^2 \ge 1$, never turns and is
      never pushed towards the tip (PROVED); the Revision Kohn-Sham work keeps only
      states without extra-time momenta (its good sector).
    - ASSUMED: the history $a_4 = AHx_4$, $b_4 = b_4(0)\,e^{\beta AHx_4}$ with
      $\beta = 4/3$, $b_4(0) = 1$ (a prescribed background); test particles that do not
      change the metric. NOT computed here: whether the waves of the fields follow
      these paths in the curved metric, and what happens to a path at the tip
      $\sin z = 0$, where this chart of the metric ends.
    """),
]

if __name__ == "__main__":
    raise SystemExit(run_builder(__file__))
