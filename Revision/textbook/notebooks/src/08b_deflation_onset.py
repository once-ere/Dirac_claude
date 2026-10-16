#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
"""Builder of Notebook 08b, "The deflating extra times drive every extra-time wave into
growth" (textbook "Universes in Pairs", chapter 08).

The notebook Revision/textbook/notebooks/08b_deflation_onset.ipynb is BUILT from this
file by Revision/textbook/tools/nbkit.py (never edit the .ipynb by hand):

    python Revision/textbook/tools/nbkit.py build \
        Revision/textbook/notebooks/src/08b_deflation_onset.py --date YYYY-MM-DD
    python Revision/textbook/tools/nbkit.py check \
        Revision/textbook/notebooks/src/08b_deflation_onset.py

It uses the canonical deflating history of the Kohn-Sham record
(Revision/kohn_sham/results/parameters.json: a4 = A H x4, b4 = b4(0) e^(beta A H x4) with
A = 1, beta = 4/3, H = m = 1, a PRESCRIBED BACKGROUND) and the local-frame (frozen hidden
position) model of the Revision statement extra_time_modes_grow
(Revision/theory/reports/python-field-theory.json).
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools"))
from nbkit import code, md, run_builder  # noqa: E402

FIGURES = [
    "08b_1_scale_factors",
    "08b_2_frame_momenta",
    "08b_3_onset_times",
    "08b_4_growth_along_history",
    "08b_5_rate_and_krein",
]

FACTS = {
    "id": "08b",
    "name": "08b_deflation_onset",
    "title": "The deflating extra times drive every extra-time wave into growth",
    "purpose": (
        "Along the deflating history a4 = A H x4, b4 = b4(0) e^(4 A H x4/3) of the "
        "Kohn-Sham record (A = 1, H = m = 1, a prescribed background) on which the extra "
        "times shrink like e^(-A H x4/3), it computes the scale factors and the "
        "frame momenta of a wave with fixed wave numbers along x1 and x5, the exact time "
        "at which such a wave turns from oscillation to growth, and shows that every "
        "wave along an extra time reaches this onset; it then follows one wave through "
        "the onset with the local-frame model (RK4, convergence of order 4) and compares "
        "the growth with the WKB formulas, checks the Krein form, and draws five "
        "teaching plots."
    ),
    "records": [
        ["Revision/kohn_sham/results/parameters.json",
         "the canonical deflating history a4 = A H x4, b4 = b4(0) e^(beta A H x4) (A = 1, "
         "beta = 4/3, H = 1, m = 1, prescribed background) and the tip cutoff L (read)"],
        ["Revision/algebra/gammas.json",
         "the author's 16 x 16 gamma matrices, C and B (read)"],
        ["Revision/theory/reports/python-field-theory.json",
         "checks sqrt_det_g_equals_b4_cos_z and extra_time_modes_grow (reproduced)"],
        ["Revision/theory/reports/python-scope.json",
         "check extra_time_growth_rates_unbounded (its frozen-coefficient formula for "
         "E^2, reproduced at every instant of the history)"],
    ],
    "packages": ["numpy", "sympy", "matplotlib"],
    "needs_rust": [],
    "expected_seconds": 30,
    "timeout_seconds": 300,
    "files_written": ["Revision/textbook/figures/08b.captions.json"]
    + [f"Revision/textbook/figures/{name}.png" for name in FIGURES],
    "final_lines": [
        "PASS the figure file 08b_5_rate_and_krein.png exists",
        "ALL 26 CHECKS PASSED (notebook 08b)",
    ],
    "troubleshooting": [
        ["FileNotFoundError naming Revision/kohn_sham/results/parameters.json",
         "the notebook reads this Revision record of the repository. Check that your "
         "copy of the repository contains the folder Revision/kohn_sham/results with "
         "the file parameters.json (clone the repository again if it does not) and "
         "that you opened the notebook from its folder Revision/textbook/notebooks."],
    ],
}

CELLS = [
    md(r"""
    ## 1. What this notebook computes

    In the author's metric the three extra times $x_5, x_6, x_7$ DEFLATE: their lengths
    carry the factor $e^{-a_4}b_4^{1/2}\sin^{1/6}z$ ($b_4(x_4) > 0$ is the second
    function of the metric). This notebook uses the deflating history of the
    Kohn-Sham record, $a_4 = A H x_4$ and $b_4 = b_4(0)\,e^{\beta AHx_4}$ with $A = 1$,
    $\beta = 4/3$ and $H = m = 1$ (a PRESCRIBED background, not a solution of the
    $a_4$ equations); on it $e^{-a_4}b_4^{1/2} = b_4(0)^{1/2}e^{-\delta x_4}$ with the
    deflation rate $\delta = (1 - \beta/2)AH = AH/3$. A wave that wiggles a fixed number
    of times per unit of the coordinate $x_5$ therefore wiggles more and more often per
    unit of PROPER length (length measured with the metric): its frame momentum grows
    like $e^{\delta x_4}$. The notebook

    - draws the scale factors of 3-space (inflating) and of the extra times (deflating)
      and checks exactly that the volume factor is $\sqrt{|g|} = b_4^{3/2}\cos z$, which
      changes in time only through $b_4$;
    - computes the frame momenta of a wave with fixed wave numbers $q_1$ along $x_1$
      and $q_5$ along $x_5$, and the exact time $x_4^\ast$ at which $E^2 = m^2 +
      k_{(1)}^2 - k_{(5)}^2$ turns negative (the *onset*), checked against a numerical
      root search;
    - shows that every wave with $q_5 \neq 0$ reaches the onset at a finite time: every
      wave along an extra time eventually grows (the Revision statement
      `extra_time_modes_grow`);
    - follows one wave through the onset with the local-frame model (explained in
      section 4), solved with RK4 (fourth-order convergence checked), and compares its
      growth with the WKB formulas; the growth is faster than any exponential;
    - checks that the Krein form stays constant while the ordinary size grows by more
      than 40 powers of ten.

    It draws five teaching plots.
    """),
    md(r"""
    ## 3. The words used in this notebook

    - **Coordinates** (the author's names): $x_1, x_2, x_3$ ordinary space; $x_4$ the
      time; $x_5, x_6, x_7$ the three extra times (time-like, deflating); $x_0$ the
      hidden direction, $z = 6Hx_0$ between $0$ and $\pi/2$.
    - **Hidden coordinate** $y = \ln(\sin z)/(6H)$: a second way to label the points of
      the hidden direction. $y = 0$ at $z = \pi/2$ (the *patch end*, where the author's
      coordinate patch ends) and $y \to -\infty$ at the *tip* $z \to 0$; the Kohn-Sham
      record cuts the tip at $y = -L$ with $L = 3$. In this coordinate
      $\sin^{1/6}z = e^{Hy}$.
    - **Scale factor**: the factor by which a coordinate length must be multiplied to
      give the proper length; $e^{a_4}\sin^{1/6}z$ for $x_1, x_2, x_3$ and
      $e^{-a_4}b_4^{1/2}\sin^{1/6}z$ for $x_5, x_6, x_7$. **Inflating** means growing,
      **deflating** shrinking.
    - **History** $a_4(x_4)$, $b_4(x_4)$: how the two functions change with time. Here
      $a_4 = A H x_4$ and $b_4 = b_4(0)\,e^{\beta AHx_4}$ with $A = 1$ and
      $\beta = 4/3$ (the canonical history of the Kohn-Sham record; $b_4(0)$ is the unit
      of $b_4$). It is PRESCRIBED: chosen, not solved for (the record shows that the
      Kohn-Sham states do not supply the source that the $a_4$ equations need for it).
    - **Deflation rate** $\delta = (1 - \beta/2)AH = AH/3$: on the history the extra
      times shrink like $e^{-\delta x_4}$.
    - **Coordinate wave number** $q_a$ and **frame momentum** $k_{(a)} = q_a/f_a$, where
      $f_a$ is the scale factor: the wave $e^{iq_a x_a}$ has $q_a$ radians of phase per
      unit of coordinate length and $k_{(a)}$ radians per unit of proper length.
    - **Mode matrix** $h = -im\gamma^{(4)} - \gamma^{(4)}\sum_a k_{(a)}\gamma^{(a)}$:
      with frozen coefficients a wave $u\,e^{-iEx_4}$ needs $hu = Eu$, and $h^2 = E^2$
      with $E^2 = m^2 + k_{(1)}^2 - k_{(5)}^2$ when only $k_{(1)}$ and $k_{(5)}$ are
      nonzero. **Onset**: the time at which $E^2$ turns negative.
    - **Local-frame model**: the equation $i\,du/dx_4 = h(x_4)u$ in which the frame
      momenta change with $x_4$ as the history prescribes, while the hidden position is
      held fixed (section 4).
    - **WKB approximation** (after Wentzel, Kramers and Brillouin): when the growth rate
      $\kappa$ changes slowly, the size grows like $e^{2W}$ with $W = \int\kappa\,dx_4$.
    - **Krein form** $u^\dagger B u$ with the matrix $B = -iC\gamma^{(4)}$ of the record
      ($B^\dagger = B$, $B^2 = 1$); **Hilbert norm** $u^\dagger u$.
    - **RK4**: the classical fourth-order Runge-Kutta method; *fourth order* means that
      halving the step divides the error by about $2^4 = 16$.
    """),
    md(r"""
    ## 4. The physical and mathematical situation

    In the hidden coordinate $y$ the author's metric reads
    $ds^2 = e^{2Hy}\big(e^{2a_4}(dx_1^2 + dx_2^2 + dx_3^2) - e^{-2a_4}b_4(dx_5^2 + dx_6^2
    + dx_7^2)\big) - dx_4^2 + dy^2$, because $\sin^{1/3}z = e^{2Hy}$ and $dy = \cot z\,
    dx_0$. Its coefficients do not depend on $x_1, x_2, x_3, x_5, x_6, x_7$, so a wave
    $e^{i(q_1x_1 + q_5x_5)}$ keeps its coordinate wave numbers $q_1, q_5$ exactly for
    all times. Its frame momenta are, line by line (on the history, $b_4$ in its unit
    $b_4(0)$):

    1. $k_{(1)} = q_1/f_1 = q_1\,e^{-a_4}e^{-Hy} = q_1\,e^{-AHx_4}e^{-Hy}$ (the factor
       of $x_1$ is $f_1 = e^{a_4}e^{Hy}$);
    2. $k_{(5)} = q_5/f_5 = q_5\,e^{a_4}b_4^{-1/2}e^{-Hy} = q_5\,e^{\delta x_4}e^{-Hy}$
       (the factor of $x_5$ is $f_5 = e^{-a_4}b_4^{1/2}e^{Hy}$, and $a_4 -
       \frac12\ln b_4 = AHx_4 - \frac12\beta AHx_4 = \delta x_4$);
    3. with frozen coefficients $E^2 = m^2 + k_{(1)}^2 - k_{(5)}^2
       = m^2 + q_1^2e^{-2Hy}e^{-2AHx_4} - q_5^2e^{-2Hy}e^{2\delta x_4}$.

    As the time goes on, the last term grows like $e^{2\delta x_4}$ and the middle one
    decays like $e^{-2AHx_4}$: $E^2$ must turn negative. With $X = e^{2\delta x_4}$ and
    $w = e^{-Hy}$, and $e^{-2AHx_4} = X^{-3}$ (because $AH = 3\delta$), the onset
    $E^2 = 0$ is, after multiplication by $X^3$, the equation of fourth degree
    $q_5^2w^2X^4 - m^2X^3 - q_1^2w^2 = 0$. Its coefficients change sign once, so it has
    exactly one positive root $X^\ast$ (Descartes' rule of signs), and the onset time
    is $x_4^\ast = \ln(X^\ast)/(2\delta)$. For $q_1 = 0$ it is $X^\ast =
    m^2/(q_5^2w^2)$ and $x_4^\ast = \big(Hy + \ln(m/q_5)\big)/\delta = 3\big(Hy +
    \ln(m/q_5)\big)/(AH)$: three times later than it would be without the growth of
    $b_4$.

    THE MODEL (labelled). The field also depends on $y$, and the factor $e^{-Hy}$ in
    the frame momenta makes the exact equation couple neighbouring values of $y$. The
    *local-frame model* holds the hidden position fixed (it freezes the coefficients
    in $y$, the WKB statement of the Revision record), works in the variables
    $\chi = \sin^{1/2}z\,\Psi$ (in which the term $3H\gamma^{(0)}$ of the diagonal
    frame is absent exactly), takes no momentum along the hidden direction, and keeps
    the exact time dependence of the frame momenta: $i\,du/dx_4 = h(x_4)u$ with
    $h(x_4) = -im\gamma^{(4)} - \gamma^{(4)}\big(k_{(1)}(x_4)\gamma^{(1)} +
    k_{(5)}(x_4)\gamma^{(5)}\big)$. Its solutions are not exact solutions of the field
    equation; they show how a wave behaves near one hidden position. The position
    enters only through $q_5e^{-Hy}$, so the runs below use $y = 0$.

    Units: $H = m = 1$, as in the Kohn-Sham record; times in units of $1/m$, momenta
    in units of $m$.
    """),
    md(r"""
    ## 5. The deflating history of the Kohn-Sham record

    The next cell first defines two helpers for the checks that reproduce a Revision
    record. `record_says(report, name, ...)` opens the report (a JSON file with a list
    of checks, each with a name, a verdict and a detail text) and is true when the
    check `name` is there with the verdict pass and its detail text contains every
    further piece of text given. `check_record(condition, title, report, name, ...)` is
    the helper `check` for such a result: it passes only if the notebook's own
    computation (`condition`) is right AND the record says the same. Then the cell
    reads the parameters of the Kohn-Sham record, takes from it $H$, $m$, the history
    constants $A$ and $\beta$ and the tip cutoff $L$, prints how the record describes
    the history and its status, and checks the values $A = H = m = 1$, $\beta = 4/3$,
    $L = 3$. It defines the history $a_4(x_4)$, $b_4(x_4)$ (in the unit $b_4(0)$) and
    the deflation rate $\delta = (1 - \beta/2)AH$, and checks $\delta = 1/3$.
    """),
    code(r'''
    import numpy as np  # arrays of numbers, matrices, linear algebra
    import sympy as sp  # exact algebra with symbols

    REPORTS = {}  # report file -> {check name: (verdict, detail)}, each read once


    def record_says(report_file, check_name, *pieces):
        """True when the Revision report records the check check_name with the verdict
        pass and its detail text contains every given piece of text."""
        if report_file not in REPORTS:  # read the report the first time it is needed
            data = json.loads(repository_file(report_file).read_text(encoding="utf-8"))
            REPORTS[report_file] = {entry["name"]: (entry["verdict"].lower(),
                                                    entry["detail"])
                                    for entry in data["checks"]}
        verdict, detail = REPORTS[report_file][check_name]
        return verdict == "pass" and all(piece in detail for piece in pieces)


    def check_record(condition, title, report_file, check_name, *pieces):
        """check() for a result that reproduces the Revision check check_name: it passes
        only if condition is true AND the report records check_name as passed, with
        every piece of text (values computed here) in its detail."""
        on_record = record_says(report_file, check_name, *pieces)
        check(condition and on_record, title,
              record=f"{report_file}, check {check_name}")


    parameters = json.loads(repository_file(
        "Revision/kohn_sham/results/parameters.json").read_text(encoding="utf-8"))
    H = parameters["physics"]["H"]  # the author's constant H
    mass = parameters["physics"]["m"]  # the mass m
    A = parameters["physics"]["historyA"]  # the history a4 = A H x4
    beta = parameters["physics"]["historyBeta"]  # and b4 = b4(0) e^(beta A H x4)
    L_tip = parameters["physics"]["L_tipCutoff"]  # the record cuts the tip at y = -L
    say("history: " + parameters["theoryInputs"]["adiabaticityHistory"])
    say("status: " + parameters["conventions"]["history"].split(". ")[0] + ".")
    check(H == 1.0 and mass == 1.0 and A == 1.0 and sp.nsimplify(beta) == sp.Rational(4, 3)
          and L_tip == 3.0,
          "the canonical history: A = 1, beta = 4/3, H = 1, m = 1, tip cutoff L = 3",
          record="Revision/kohn_sham/results/parameters.json, physics.historyA, "
                 "physics.historyBeta, physics.H, physics.m, physics.L_tipCutoff")


    def a4_of(x4):
        """The prescribed deflating history a4 = A H x4."""
        return A * H * x4


    def b4_of(x4):
        """The prescribed history b4 = b4(0) e^(beta A H x4), in the unit b4(0)."""
        return np.exp(beta * A * H * x4)


    delta = (1 - beta / 2) * A * H  # the deflation rate: e^(-a4) b4^(1/2) = e^(-delta x4)
    report("deflation rate delta = (1 - beta/2) A H", f"{delta:.12f}")
    check(abs(delta - 1 / 3) < 1e-15 and abs(A * H / delta - 3) < 1e-14,
          "the extra times shrink like e^(-x4/3) on the history: delta = A H/3")
    '''),
    md(r"""
    ## 6. The scale factors and the volume

    The next cell first checks three exact statements with sympy: $dy/dx_0 = \cot z$
    for $y = \ln(\sin z)/(6H)$; $e^{Hy} = \sin^{1/6}z$; and the product of the eight
    scale factors, $\cot z \cdot (e^{a_4}\sin^{1/6}z)^3 \cdot 1 \cdot
    (e^{-a_4}b_4^{1/2}\sin^{1/6}z)^3$, equals $b_4^{3/2}\cos z$ for every $a_4$: the
    factors $e^{\pm3a_4}$ of the inflation of 3-space and of the deflation of the extra
    times compensate exactly, and the volume changes in time only through $b_4$. Then
    it draws the scale factors along the history at two hidden positions.
    """),
    code(r'''
    x0, H_symbol = sp.symbols("x0 H", positive=True)
    a4_symbol = sp.Symbol("a4", real=True)
    z = 6 * H_symbol * x0
    y_of_x0 = sp.log(sp.sin(z)) / (6 * H_symbol)  # the hidden coordinate y
    check(sp.simplify(sp.diff(y_of_x0, x0) - sp.cot(z)) == 0, "dy/dx0 = cot z")
    check(sp.simplify(sp.exp(H_symbol * y_of_x0) - sp.sin(z) ** sp.Rational(1, 6)) == 0,
          "e^(H y) = sin(z)^(1/6)")
    space_factor = sp.exp(a4_symbol) * sp.sin(z) ** sp.Rational(1, 6)  # x1, x2, x3
    b4_symbol = sp.Symbol("b4", positive=True)  # the second function of the metric
    extra_factor = (sp.exp(-a4_symbol) * sp.sqrt(b4_symbol)
                    * sp.sin(z) ** sp.Rational(1, 6))  # x5, x6, x7
    volume = sp.cot(z) * space_factor**3 * 1 * extra_factor**3  # x4 has the factor 1
    check_record(sp.simplify(volume - b4_symbol ** sp.Rational(3, 2) * sp.cos(z)) == 0,
                 "sqrt|g| = product of the scale factors = b4^(3/2) cos z, for every a4",
                 "Revision/theory/reports/python-field-theory.json",
                 "sqrt_det_g_equals_b4_cos_z", "b4(x4)^(3/2) cos(6 H x0)")

    times = np.linspace(0.0, 6.0, 601)
    fig, ax = plt.subplots()
    for y, style in ((0.0, "-"), (-1.0, "--")):
        warp = np.exp(H * y)  # sin^(1/6) z = e^(H y)
        ax.plot(times, np.exp(a4_of(times)) * warp, style, color="tab:blue",
                label=f"3-space $e^{{a_4}}e^{{Hy}}$, $y = {y}$")
        ax.plot(times, np.exp(-a4_of(times)) * np.sqrt(b4_of(times)) * warp, style,
                color="tab:red", label=f"extra times $e^{{-a_4}}b_4^{{1/2}}e^{{Hy}}$, "
                f"$y = {y}$")
        ax.plot(times, b4_of(times) ** 1.5 * warp**6, style, color="black",
                linewidth=0.8, label=f"product of the six, $b_4^{{3/2}}e^{{6Hy}}$, "
                f"$y = {y}$")
    ax.set_yscale("log")
    ax.set_xlabel("time $x_4$ (units of $1/m$)")
    ax.set_ylabel("scale factor")
    ax.set_title("Scale factors along the history $a_4 = x_4$, $b_4 = e^{4x_4/3}$")
    ax.legend(fontsize=7, loc="upper left");
    save_figure(fig, "scale_factors",
                "The scale factors of the author's metric along the prescribed "
                "deflating history $a_4 = A H x_4$, $b_4 = b_4(0)\\,e^{4AHx_4/3}$ "
                "($A = H = 1$, $b_4$ in the unit $b_4(0)$) against the time $x_4$ in "
                "units of $1/m$, on a logarithmic vertical axis, at the patch end "
                "$y = 0$ (solid) and at $y = -1$ (dashed). Blue: 3-space, "
                "$e^{a_4}e^{Hy}$, a rising straight line (exponential inflation, "
                "$e^{x_4}$). Red: the extra times, $e^{-a_4}b_4^{1/2}e^{Hy}$, a "
                "falling straight line (exponential deflation, $e^{-x_4/3}$). Black: "
                "the product of the three spatial and the three extra-time factors, "
                "$b_4^{3/2}e^{6Hy} = b_4^{3/2}\\sin z$, which grows only through "
                "$b_4^{3/2} = e^{2x_4}$.")
    '''),
    md(r"""
    ## 7. Frame momenta and the onset of growth

    The next cell defines the frame momenta of section 4, the local $E^2$, and the
    onset time, the positive root of the equation of fourth degree of section 4
    (computed with numpy's root finder for polynomials and polished by two steps of
    Newton's method); it checks the onset time against a numerical root search of
    $E^2$ itself (bisection: halve an interval in which $E^2$ changes sign 200 times)
    for several waves, and checks the simple form $x_4^\ast = 3\ln(m/q_5)$ for
    $q_1 = 0$, $y = 0$.
    """),
    code(r'''
    def frame_momenta(x4, q1, q5, y):
        """(k_(1), k_(5)) of the wave exp(i (q1 x1 + q5 x5)) at time x4 and position y."""
        w = np.exp(-H * y)  # e^(-H y) = sin^(-1/6) z
        return (q1 * np.exp(-a4_of(x4)) * w,
                q5 * np.exp(a4_of(x4)) / np.sqrt(b4_of(x4)) * w)  # q5 e^(delta x4) w


    def local_E2(x4, q1, q5, y):
        """E^2 = m^2 + k_(1)^2 - k_(5)^2 with frozen coefficients."""
        k1, k5 = frame_momenta(x4, q1, q5, y)
        return mass**2 + k1**2 - k5**2


    def onset_time(q1, q5, y):
        """The time at which E^2 = 0: X = e^(2 delta x4) is the positive root of
        q5^2 w^2 X^4 - m^2 X^3 - q1^2 w^2 = 0 (w = e^(-H y))."""
        w = np.exp(-H * y)
        coefficients = [q5**2 * w**2, -mass**2, 0.0, 0.0, -q1**2 * w**2]
        roots = np.roots(coefficients)  # the four roots (complex numbers)
        X = max(r.real for r in roots if abs(r.imag) < 1e-9 * abs(r) and r.real > 0)
        for _ in range(2):  # two Newton steps polish the root
            value = np.polyval(coefficients, X)
            slope = np.polyval(np.polyder(coefficients), X)
            X -= value / slope
        return np.log(X) / (2 * delta)


    def bisection(q1, q5, y, low=-30.0, high=30.0):
        """The time at which E^2 changes sign, by halving [low, high] 200 times."""
        for _ in range(200):
            middle = (low + high) / 2
            if local_E2(middle, q1, q5, y) > 0:  # still oscillating: onset is later
                low = middle
            else:
                high = middle
        return (low + high) / 2


    worst = max(abs(onset_time(q1, q5, y) - bisection(q1, q5, y))
                for q1 in (0.0, 0.5, 1.0, 3.0) for q5 in (0.01, 0.05, 0.1, 0.4)
                for y in (0.0, -1.0, -3.0))
    check(worst < 1e-10, "the onset time from the polynomial equals the bisection "
          "result (48 waves)")
    check(abs(onset_time(0.0, 0.05, 0.0) - 3 * np.log(1 / 0.05)) < 1e-12,
          "q1 = 0, y = 0: onset time = 3 ln(m/q5)")
    for q5 in (0.05, 0.1):
        report(f"onset time for q1 = 0, q5 = {q5}, y = 0", f"{onset_time(0.0, q5, 0.0):.6f}")
    '''),
    md(r"""
    The next cell draws the two frame momenta of a wave with $q_1 = q_5 = 0.1$ (left)
    and the local $E^2$ of several waves (right) along the history, over the times 0 to
    15 (long enough for the onsets); the dots mark the onset times computed above.
    """),
    code(r'''
    times = np.linspace(0.0, 15.0, 1501)  # long enough for the onsets
    fig, (left, right) = plt.subplots(1, 2, figsize=(10.0, 4.2))
    k1_path, k5_path = frame_momenta(times, 0.1, 0.1, 0.0)
    left.plot(times, k5_path, color="tab:red",
              label="extra time: $k_{(5)} = q_5e^{a_4}b_4^{-1/2}$")
    left.plot(times, k1_path, color="tab:blue", label="3-space: $k_{(1)} = q_1e^{-a_4}$")
    left.axhline(mass, color="black", linewidth=0.8, linestyle=":", label="$m$")
    left.set_yscale("log")
    left.set_xlabel("time $x_4$")
    left.set_ylabel("frame momentum (units of $m$)")
    left.set_title("$q_1 = q_5 = 0.1$, $y = 0$")
    left.legend(fontsize=8)
    for q1, q5, style in ((0.0, 0.02, "-"), (0.0, 0.05, "-"), (0.0, 0.1, "-"),
                          (0.0, 0.2, "-"), (1.0, 0.05, "--")):
        right.plot(times, local_E2(times, q1, q5, 0.0), style,
                   label=f"$q_1 = {q1}$, $q_5 = {q5}$")
        t_star = onset_time(q1, q5, 0.0)
        right.plot([t_star], [0.0], "o", color="black", markersize=4)
    right.axhline(0.0, color="black", linewidth=0.8)
    right.set_ylim(-4.0, 2.5)
    right.set_xlabel("time $x_4$")
    right.set_ylabel("$E^2 = m^2 + k_{(1)}^2 - k_{(5)}^2$")
    right.set_title("Local $E^2$ along the history, $y = 0$")
    right.legend(fontsize=8, loc="lower left");
    save_figure(fig, "frame_momenta",
                "Left: the frame momenta of one wave with coordinate wave numbers "
                "$q_1 = q_5 = 0.1$ at $y = 0$ against the time $x_4$, on a logarithmic "
                "axis in units of $m$, along the history $a_4 = x_4$, $b_4 = "
                "e^{4x_4/3}$: the extra-time momentum $k_{(5)} = q_5e^{a_4}b_4^{-1/2} "
                "= q_5e^{x_4/3}$ grows exponentially because the extra times deflate, "
                "the space momentum $k_{(1)} = q_1e^{-a_4}$ shrinks because 3-space "
                "inflates; the dotted line is the mass $m = 1$. Right: the local $E^2$ "
                "of five waves along the history; each curve crosses zero once, at its "
                "onset time (black dot), and stays negative afterwards: the wave stops "
                "oscillating and starts to grow. The dashed wave has also $q_1 = 1$: "
                "its $E^2$ starts higher, but the space term dies away like $e^{-2a_4}$ "
                "and its onset is almost that of the same wave with $q_1 = 0$.")
    '''),
    md(r"""
    ## 8. Every wave along an extra time reaches the onset

    The onset time $x_4^\ast$ is finite for EVERY $q_5 > 0$: the equation of section 4
    always has its one positive root, for $q_1 = 0$ the formula has $q_5$ only in a
    denominator inside a logarithm, so a smaller $q_5$ only delays the onset
    logarithmically, and a deeper position (more negative $y$) or a nonzero $q_1$
    changes it by a bounded amount. The next cell evaluates the onset time on a
    grid of $q_5$ from $10^{-4}$ to $1$, checks that it is finite and decreasing in
    $q_5$, and draws it for three hidden positions and for $q_1 = 1$.
    """),
    code(r'''
    q5_grid = np.logspace(-4.0, 0.0, 200)  # 10^-4 ... 1, equally spaced on a log axis
    fig, ax = plt.subplots()
    all_finite_and_decreasing = True
    for q1, y, style in ((0.0, 0.0, "-"), (0.0, -1.0, "--"), (0.0, -L_tip, ":"),
                         (1.0, 0.0, "-.")):
        onsets = np.array([onset_time(q1, q5, y) for q5 in q5_grid])
        all_finite_and_decreasing &= bool(np.all(np.isfinite(onsets))
                                          and np.all(np.diff(onsets) < 0))
        ax.plot(q5_grid, onsets, style, label=f"$q_1 = {q1}$, $y = {y}$")
    ax.set_xscale("log")
    ax.set_xlabel("coordinate wave number $q_5$ along the extra time $x_5$")
    ax.set_ylabel("onset time $x_4^\\ast$ (units of $1/m$)")
    ax.set_title("Every extra-time wave reaches the onset")
    ax.legend();
    save_figure(fig, "onset_times",
                "The onset time $x_4^\\ast$ at which a wave with coordinate wave number "
                "$q_5$ along the extra time $x_5$ stops oscillating and starts to grow, "
                "against $q_5$ from $10^{-4}$ to $1$ on a logarithmic axis, along the "
                "history $a_4 = x_4$, $b_4 = e^{4x_4/3}$ with $m = H = 1$, at the hidden "
                "positions $y = 0$ (the patch end), $y = -1$ and $y = -3$ (the tip "
                "cutoff of the Kohn-Sham record), and for a wave that also has "
                "$q_1 = 1$. Every curve is finite and rises only like $3\\ln(1/q_5)$: "
                "however small $q_5$ is, "
                "the deflation of the extra times eventually drives the wave into "
                "growth; a negative onset time means that the wave grows already at "
                "$x_4 = 0$.")
    check_record(all_finite_and_decreasing,
                 "the onset time is finite for every q5 > 0 on the grid and decreases "
                 "with q5", "Revision/theory/reports/python-field-theory.json",
                 "extra_time_modes_grow",
                 "every extra-time mode eventually enters the growing regime",
                 "e^{-a4/3}")
    '''),
    md(r"""
    ## 9. Following one wave through the onset: the local-frame model

    The next cell reads the gamma matrices and builds the time-dependent mode matrix
    $h(x_4)$ of the local-frame model. It checks at five instants, for a wave with
    $q_1 = 0.3$ and $q_5 = 0.1$, that $h(x_4)^2 = E^2(x_4)\,I_{16}$, where $E^2$ is the
    formula of the Revision record for frozen coefficients, $E^2 = m^2 + k_1^2 + k_2^2 +
    k_3^2 + k_0^2 - k_5^2 - k_6^2 - k_7^2$, taken at the frame momenta of that instant
    (and checks that the record holds exactly this formula). Then it chooses the
    starting column for $q_1 = 0$.
    With $q_1 = 0$ the matrix $C = \gamma^{(0)}\gamma^{(1)}\gamma^{(2)}\gamma^{(3)}$
    commutes with $h$ ($\gamma^{(4)}$ and $\gamma^{(5)}$ each anticommute with all four
    factors of $C$), so there are columns that are eigenvectors of $h(0)$ for the
    positive frequency $E_0 = \sqrt{m^2 - q_5^2}$ AND of $C$ for $+1$ or $-1$. The
    projectors $\Lambda_+ = (1 + h(0)/E_0)/2$ and $(1 \pm C)/2$ produce them from the
    first unit column. For such a column the Krein form is $u^\dagger B u = \pm E_0/m$:
    $B = -iC\gamma^{(4)} = C(-i\gamma^{(4)})$ gives $u^\dagger B u = \pm u^\dagger
    (-i\gamma^{(4)})u$, and $E_0 = u^\dagger h u = m\,u^\dagger(-i\gamma^{(4)})u -
    q_5\,u^\dagger\gamma^{(4)}\gamma^{(5)}u$, where the first term is real and the
    second imaginary ($\gamma^{(4)}\gamma^{(5)}$ is real and antisymmetric), so the
    second term vanishes. The cell checks all of this.
    """),
    code(r'''
    gammas_record = json.loads(
        repository_file("Revision/algebra/gammas.json").read_text(encoding="utf-8"))
    GAMMA = [np.array(rows, dtype=int) for rows in gammas_record["gamma"]]
    C = np.array(gammas_record["C"], dtype=int)  # C = g^(x0) g^(x1) g^(x2) g^(x3)
    B = np.array(gammas_record["B"]["re"]) + 1j * np.array(gammas_record["B"]["im"])
    g4 = GAMMA[4].astype(complex)  # gamma^(x4)
    g4g1 = (GAMMA[4] @ GAMMA[1]).astype(complex)  # gamma^(x4) gamma^(x1)
    g4g5 = (GAMMA[4] @ GAMMA[5]).astype(complex)  # gamma^(x4) gamma^(x5)
    check(np.array_equal(C @ GAMMA[4], GAMMA[4] @ C) and
          np.array_equal(C @ GAMMA[5], GAMMA[5] @ C),
          "C commutes with gamma^(x4) and gamma^(x5)")


    def h_local(x4, q1, q5, y):
        """The mode matrix of the local-frame model at time x4."""
        k1, k5 = frame_momenta(x4, q1, q5, y)
        return -1j * mass * g4 - k1 * g4g1 - k5 * g4g5


    # At every instant h(x4)^2 = E^2(x4) I16, where E^2 is the frozen-coefficient E^2 of
    # the record with k1 = k_(1)(x4), k5 = k_(5)(x4) and all other momenta 0.
    m_s = sp.Symbol("m", real=True)
    k_s = {a: sp.Symbol(f"k{a}", real=True) for a in (0, 1, 2, 3, 5, 6, 7)}
    E2_record = m_s**2 + sum(k_s[a] ** 2 for a in (0, 1, 2, 3)) \
        - sum(k_s[a] ** 2 for a in (5, 6, 7))
    squares_ok = True
    for x4 in (0.0, 1.0, 2.0, 3.0, 4.0):
        k1_now, k5_now = frame_momenta(x4, 0.3, 0.1, 0.0)  # q1 = 0.3, q5 = 0.1, y = 0
        values = {symbol: 0 for symbol in k_s.values()}  # every momentum 0 ...
        values.update({m_s: mass, k_s[1]: k1_now, k_s[5]: k5_now})  # ... but these
        E2_now = float(E2_record.subs(values))
        h_now = h_local(x4, 0.3, 0.1, 0.0)
        squares_ok &= bool(np.allclose(h_now @ h_now, E2_now * np.eye(16), atol=1e-12)
                           and abs(E2_now - local_E2(x4, 0.3, 0.1, 0.0)) < 1e-12)
    check_record(squares_ok, "x4 = 0, 1, 2, 3, 4: h(x4)^2 = E^2(x4) I16 (q1 = 0.3, "
                 "q5 = 0.1)", "Revision/theory/reports/python-scope.json",
                 "extra_time_growth_rates_unbounded", f"h_k^2 = ({sp.sstr(E2_record)}) I16")


    def starting_column(q5, sign):
        """A unit column with h(0) u = E0 u and C u = sign u (q1 = 0, y = 0)."""
        h0 = h_local(0.0, 0.0, q5, 0.0)
        E0 = np.sqrt(mass**2 - q5**2)
        first = np.zeros(16, dtype=complex)
        first[0] = 1.0  # the first unit column
        u = (np.eye(16) + h0 / E0) @ ((np.eye(16) + sign * C) @ first) / 4
        return u / np.linalg.norm(u), h0, E0


    starts = {}
    for q5, sign in ((0.05, +1), (0.1, -1)):
        u0, h0, E0 = starting_column(q5, sign)
        starts[q5] = u0
        krein0 = np.vdot(u0, B @ u0)  # u^dagger B u
        report(f"q5 = {q5}: E0, Krein form of the start",
               f"{E0:.9f}, {krein0.real:+.9f}")
        sign_text = "+" if sign > 0 else "-"  # the sign as a character
        check(np.linalg.norm(h0 @ u0 - E0 * u0) < 1e-14 and
              np.linalg.norm(C @ u0 - sign * u0) < 1e-14 and
              abs(krein0 - sign * E0 / mass) < 1e-14,
              f"q5 = {q5}: h(0) u = E0 u, C u = {sign_text}u, "
              f"Krein form = {sign_text}E0/m")
    '''),
    md(r"""
    The next cell solves $du/dx_4 = -i\,h(x_4)u$ with RK4 from $x_4 = 0$ to $3/\delta
    = 9$ time units after the onset (in which the frame momentum grows by the factor
    $e^3$), for $q_5 = 0.05$ and $q_5 = 0.1$, with 36000 steps, and records $u^\dagger u$
    and $u^\dagger B u$ after every step. It prints the size
    $u^\dagger u$ at the onset (at the first step after it) and $\ln(u^\dagger u)$ at
    the end. Before the onset the size does not stay exactly 1: with extra-time
    momentum the mode matrix is not Hermitian, so the Hilbert norm is not conserved.
    For $q_5 = 0.05$ it repeats the run with 18000 and 72000 steps: the differences of
    the end values must shrink by a factor close to 16 (fourth order).
    """),
    code(r'''
    def rk4_history(u0, q5, x4_end, steps):
        """RK4 for du/dx4 = -i h(x4) u (q1 = 0, y = 0); returns the times, u^dagger u,
        u^dagger B u after every step, and the final column."""
        step = x4_end / steps
        u = u0.copy()
        times_out = [0.0]
        hilbert = [np.vdot(u, u).real]
        krein = [np.vdot(u, B @ u)]

        def rate(x4, v):  # the right-hand side -i h(x4) v
            return -1j * (h_local(x4, 0.0, q5, 0.0) @ v)

        for n in range(steps):
            x4 = n * step
            s1 = rate(x4, u)
            s2 = rate(x4 + step / 2, u + step / 2 * s1)
            s3 = rate(x4 + step / 2, u + step / 2 * s2)
            s4 = rate(x4 + step, u + step * s3)
            u = u + step / 6 * (s1 + 2 * s2 + 2 * s3 + s4)
            times_out.append((n + 1) * step)
            hilbert.append(np.vdot(u, u).real)
            krein.append(np.vdot(u, B @ u))
        return np.array(times_out), np.array(hilbert), np.array(krein), u


    runs = {}
    for q5 in (0.05, 0.1):
        x4_end = onset_time(0.0, q5, 0.0) + 3.0 / delta  # 9 time units after the onset
        runs[q5] = rk4_history(starts[q5], q5, x4_end, 36000)
        at_onset = np.searchsorted(runs[q5][0], onset_time(0.0, q5, 0.0))  # its index
        report(f"q5 = {q5}: u^dagger u at the onset", f"{runs[q5][1][at_onset]:.2f}")
        final_size = runs[q5][1][-1]  # u^dagger u at the end of the run
        report(f"q5 = {q5}: ln(u^dagger u) at the onset + 9", f"{np.log(final_size):.6f}")
    x4_end = onset_time(0.0, 0.05, 0.0) + 3.0 / delta
    end_18000 = rk4_history(starts[0.05], 0.05, x4_end, 18000)[3]
    end_72000 = rk4_history(starts[0.05], 0.05, x4_end, 72000)[3]
    end_36000 = runs[0.05][3]
    ratio = np.linalg.norm(end_18000 - end_36000) / np.linalg.norm(end_36000 - end_72000)
    relative_error = np.linalg.norm(end_36000 - end_72000) / np.linalg.norm(end_72000)
    report("RK4 error ratio (18000 vs 36000) / (36000 vs 72000) steps", f"{ratio:.2f}")
    check(14.0 < ratio < 18.0, "RK4 converges with order 4 (error ratio near 16)")
    check(relative_error < 1e-8, "the 36000-step run is accurate to 1e-8 (relative)")
    '''),
    md(r"""
    ## 10. The WKB formulas and the comparison

    After the onset, write $Q = k_{(5)} = q_5e^{\delta x_4}$ and
    $\kappa = \sqrt{Q^2 - m^2}$. Line by line:

    1. Leading order: at each instant the growing eigenvalue of $-ih$ is $+\kappa$, so
       $\frac{d}{dx_4}\ln(u^\dagger u) \approx 2\kappa$ and $\ln(u^\dagger u) \approx
       2W + $ const with $W(x_4) = \int\kappa\,dx_4$.
    2. Because $dQ/dx_4 = \delta\,Q$, the substitution $dx_4 = dQ/(\delta Q)$ gives
       $W = \frac{1}{\delta}\int\frac{\sqrt{Q^2 - m^2}}{Q}dQ = \frac{1}{\delta}\Big(
       \sqrt{Q^2 - m^2} - m\arccos\frac{m}{Q}\Big)$ (differentiate the bracket:
       $\frac{Q}{\kappa} - \frac{m^2}{Q\kappa} = \frac{\kappa}{Q}$).
    3. First order: the matrices $A_4 = -i\gamma^{(4)}$ and $M = -i\gamma^{(4)}
       \gamma^{(5)}$ are Hermitian, square to 1 and anticommute, and $h = mA_4 - iQM$.
       In each of 8 planes spanned by a column $w$ with $A_4w = w$ and by $Mw$ the
       equation is $v' = \begin{pmatrix}-im & -Q\\ -Q & im\end{pmatrix}v$.
    4. This symmetric matrix has the eigenvector $r = (Q, -\kappa - im)$ for $+\kappa$.
       Multiplying the equation by $r^T$ and keeping only the growing part $v \approx
       c\,r$ gives $c'/c = \kappa - n'/(2n)$ with $n = r^Tr = 2\kappa(\kappa + im)$.
    5. Hence $|c|^2 \propto e^{2W}/|n| = e^{2W}/(2\kappa Q)$, and $u^\dagger u \approx
       |c|^2\,r^\dagger r = |c|^2\,2Q^2 \propto e^{2W}Q/\kappa$: $\ln(u^\dagger u)
       \approx 2W + \ln(Q/\kappa) + $ const, and the rate is $2\kappa + \frac{d}{dx_4}
       \ln\frac{Q}{\kappa} = 2\kappa - \delta\,m^2/\kappa^2$.

    Both approximations fail at the onset itself ($\kappa \to 0$), so the comparison
    uses increases over a window from $1.5/\delta = 4.5$ to $3/\delta = 9$ time units
    after the onset (the unknown constants drop out of increases). The next cell
    computes them.
    """),
    code(r'''
    def Q_of(x4, q5):
        return q5 * np.exp(delta * x4)  # the frame momentum k_(5) at y = 0


    def kappa_of(x4, q5):
        return np.sqrt(Q_of(x4, q5) ** 2 - mass**2)


    def W_of(x4, q5):
        Q = Q_of(x4, q5)
        return (np.sqrt(Q**2 - mass**2) - mass * np.arccos(mass / Q)) / delta


    comparison = {}
    for q5 in (0.05, 0.1):
        x4s, hilbert, krein, _ = runs[q5]
        start = np.searchsorted(x4s, onset_time(0.0, q5, 0.0) + 1.5 / delta)  # window
        xa, xb = x4s[start], x4s[-1]
        increase = np.log(hilbert[-1]) - np.log(hilbert[start])
        leading = 2 * (W_of(xb, q5) - W_of(xa, q5))
        first = leading + np.log(Q_of(xb, q5) / kappa_of(xb, q5)) \
            - np.log(Q_of(xa, q5) / kappa_of(xa, q5))
        comparison[q5] = (xa, increase, leading, first)
        say(f"q5 = {q5}: window {xa:.4f} to {xb:.4f}; increase of ln(u^dagger u) "
            f"{increase:.4f}, leading WKB {leading:.4f} (relative difference "
            f"{abs(increase - leading) / increase:.2e}), first order {first:.4f} "
            f"(relative difference {abs(increase - first) / increase:.2e})")
        check(abs(increase - leading) / increase < 2e-3,
              f"q5 = {q5}: leading WKB agrees to 2e-3 over the window")
        check(abs(increase - first) < abs(increase - leading) and
              abs(increase - first) / increase < 5e-4,
              f"q5 = {q5}: first-order WKB is better and agrees to 5e-4")
    x4s, hilbert, _, _ = runs[0.05]
    step = x4s[1] - x4s[0]
    late_rate = (np.log(hilbert[-1]) - np.log(hilbert[-3])) / (2 * step)  # centred
    kappa_late = kappa_of(x4s[-2], 0.05)  # kappa at the middle of the centred difference
    predicted = 2 * kappa_late - delta * mass**2 / kappa_late**2
    report("q5 = 0.05: computed late rate, predicted 2 kappa - delta m^2/kappa^2",
           f"{late_rate:.5f}, {predicted:.5f}")
    check(abs(late_rate - predicted) / predicted < 1e-5,
          "the late growth rate equals 2 kappa - delta m^2/kappa^2 to 1e-5")
    '''),
    md(r"""
    The next cell draws $\ln(u^\dagger u)$ of both runs with the leading WKB curve $2W$
    (shifted to agree at the window start), and the onset times.
    """),
    code(r'''
    fig, ax = plt.subplots()
    for q5, colour in ((0.05, "tab:blue"), (0.1, "tab:orange")):
        x4s, hilbert, _, _ = runs[q5]
        xa, _, _, _ = comparison[q5]
        ax.plot(x4s, np.log(hilbert), color=colour, label=f"RK4, $q_5 = {q5}$")
        after = x4s >= onset_time(0.0, q5, 0.0) + 0.05
        shift = np.log(hilbert[np.searchsorted(x4s, xa)]) - 2 * W_of(xa, q5)
        ax.plot(x4s[after], 2 * W_of(x4s[after], q5) + shift, "--", color="black",
                linewidth=0.9)
        ax.axvline(onset_time(0.0, q5, 0.0), color=colour, linestyle=":", linewidth=0.9)
    ax.plot([], [], "--", color="black", linewidth=0.9, label="WKB $2W$ + const")
    ax.set_xlabel("time $x_4$ (units of $1/m$)")
    ax.set_ylabel("$\\ln(u^\\dagger u)$")
    ax.set_title("A wave along an extra time, $a_4 = x_4$, $b_4 = e^{4x_4/3}$, $y = 0$")
    ax.legend();
    save_figure(fig, "growth_along_history",
                "The natural logarithm of the size $u^\\dagger u$ of a wave with "
                "coordinate wave number $q_5 = 0.05$ (blue) and $q_5 = 0.1$ (orange) "
                "along the extra time $x_5$, solved with RK4 in the local-frame model "
                "along the prescribed deflating history $a_4 = x_4$, $b_4 = e^{4x_4/3}$ "
                "($m = H = 1$, $y = 0$), against the time $x_4$ in units of $1/m$. "
                "Before the onset (dotted vertical lines, $x_4^\\ast = 3\\ln 20$ and "
                "$3\\ln 10$) the wave oscillates and its size grows only slowly, to "
                "about 2 at the onset (the mode matrix is not Hermitian); after the "
                "onset it grows faster and faster, by about 48 powers of ten in nine "
                "time units, following the WKB curve $2W$ (black dashed, matched 4.5 "
                "units after the onset).")
    '''),
    md(r"""
    The last figure shows, for $q_5 = 0.05$, the growth RATE $\frac{d}{dx_4}
    \ln(u^\dagger u)$ (computed from the RK4 values by centred differences) together
    with the WKB rates $2\kappa$ and $2\kappa - \delta m^2/\kappa^2$, and the change of the
    Krein form divided by $\max(u^\dagger u, 1)$. The cell checks that this change
    stays below $10^{-9}$.
    """),
    code(r'''
    x4s, hilbert, krein, _ = runs[0.05]
    step = x4s[1] - x4s[0]
    computed_rate = (np.log(hilbert[2:]) - np.log(hilbert[:-2])) / (2 * step)
    middle = x4s[1:-1]
    after = middle > onset_time(0.0, 0.05, 0.0) + 0.02
    drift = np.abs(krein - krein[0]) / np.maximum(hilbert, 1.0)
    check(drift.max() < 1e-9, "the Krein form is conserved (drift below 1e-9)")
    check(hilbert[-1] > 1e40, "the Hilbert norm grows by more than 10^40")

    fig, (left, right) = plt.subplots(1, 2, figsize=(10.0, 4.2))
    fig.subplots_adjust(wspace=0.35)  # room for the label of the right panel
    left.plot(middle, computed_rate, color="tab:blue", label="RK4 (centred differences)")
    left.plot(middle[after], 2 * kappa_of(middle[after], 0.05), "--", color="black",
              label="$2\\kappa$")
    left.plot(middle[after], 2 * kappa_of(middle[after], 0.05)
              - delta * mass**2 / kappa_of(middle[after], 0.05) ** 2, ":", color="tab:red",
              label="$2\\kappa - \\delta m^2/\\kappa^2$")
    left.set_ylim(-5.0, 45.0)
    left.set_xlabel("time $x_4$")
    left.set_ylabel("growth rate $d\\ln(u^\\dagger u)/dx_4$")
    left.set_title("Growth rate, $q_5 = 0.05$")
    left.legend(fontsize=8)
    right.semilogy(x4s[1:], np.maximum(drift[1:], 1e-18), color="tab:green")
    right.set_xlabel("time $x_4$")
    right.set_ylabel("$|\\Delta(u^\\dagger Bu)| / \\max(u^\\dagger u, 1)$")
    right.set_title("Krein form: change (rounding only)")
    save_figure(fig, "rate_and_krein",
                "Left: the growth rate $d\\ln(u^\\dagger u)/dx_4$ of the wave with "
                "$q_5 = 0.05$ against the time $x_4$ (units of $1/m$ and $m$), computed "
                "from the RK4 solution (blue), with the leading WKB rate $2\\kappa$ "
                "(black dashed) and the first-order rate $2\\kappa - \\delta m^2/"
                "\\kappa^2$ with $\\delta = 1/3$ "
                "(red dotted); before the onset the rate stays below 1, after it the "
                "rate itself grows exponentially, so the growth is faster than any "
                "exponential, and far from the onset the first-order rate is accurate. "
                "Right: the change of the Krein form $u^\\dagger Bu$ divided by "
                "$\\max(u^\\dagger u, 1)$, on a logarithmic axis (exact zeros are drawn "
                "at $10^{-18}$); it stays at the level of rounding errors, far below "
                "$10^{-9}$.")
    '''),
    md(r"""
    ## 11. The last check

    The last cell checks that the five figure files exist in the folder
    Revision/textbook/figures and prints the number of checks that passed.
    """),
    code(r'''
    for name in ("08b_1_scale_factors.png", "08b_2_frame_momenta.png",
                 "08b_3_onset_times.png", "08b_4_growth_along_history.png",
                 "08b_5_rate_and_krein.png"):
        check(output_file(f"{FIGURE_FOLDER}/{name}").is_file(),
              f"the figure file {name} exists")
    all_checks_passed()
    '''),
    md(r"""
    ## 12. What this notebook showed

    - Along the prescribed deflating history $a_4 = AHx_4$, $b_4 = b_4(0)\,
      e^{\beta AHx_4}$ of the Kohn-Sham record ($A = H = m = 1$, $\beta = 4/3$) 3-space
      inflates like $e^{a_4}$ and the extra times deflate like $e^{-a_4}b_4^{1/2} =
      e^{-\delta x_4}$ with $\delta = AH/3$, while the volume factor $\sqrt{|g|} =
      b_4^{3/2}\cos z$ changes in time only through $b_4$ (PROVED, exact sympy;
      Revision check `sqrt_det_g_equals_b4_cos_z`).
    - A wave $e^{i(q_1x_1 + q_5x_5)}$ keeps its coordinate wave numbers; its frame
      momentum along the extra time grows like $q_5e^{a_4}b_4^{-1/2}e^{-Hy} =
      q_5e^{\delta x_4}e^{-Hy}$ and along 3-space it shrinks like $q_1e^{-a_4}e^{-Hy}$
      (PROVED).
    - With frozen coefficients its $E^2$ turns negative at the onset time
      $x_4^\ast = \ln(X^\ast)/(2\delta)$, finite for every $q_5 > 0$: every wave along an
      extra time eventually enters the growing regime (PROVED for the frozen
      coefficients; the Revision statement `extra_time_modes_grow` is this local-frame
      statement).
    - In the local-frame model (MODEL: hidden position frozen; not an exact solution of
      the field equation) a wave started with positive frequency oscillates until the
      onset, while its size grows only slowly (to about 2 at the onset, because with
      extra-time momentum the mode matrix is not Hermitian), and then grows faster than
      any exponential, by about $10^{48}$ in nine time units; the growth follows the
      WKB formulas (COMPUTED: leading order to $2.8 \times 10^{-4}$, first order to
      $2 \times 10^{-5}$ over the window, late rate to $10^{-5}$), and the Krein form
      is conserved to rounding.
    - Consequence (with Notebook 08a): in flat 4 + 4 space and with frozen
      coefficients the initial-value problem is not well posed for data that depend on
      the extra times, and the deflation makes every such wave reach the growing
      regime. Only the good sector (no dependence on $x_5, x_6, x_7$) is free of this
      growth; restricting to it is a choice, not a result.
    """),
]

if __name__ == "__main__":
    raise SystemExit(run_builder(__file__))
