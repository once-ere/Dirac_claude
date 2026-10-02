#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
"""Builder of Notebook 12c, "Integrating the evolution equation of a4".

Textbook "Universes in Pairs", chapter 12 (the field equations for a4: Einstein and
Einstein-Lovelock).  The notebook Revision/textbook/notebooks/12c_a4_evolution.ipynb is
BUILT from this file by Revision/textbook/tools/nbkit.py (never edit the .ipynb by hand):

    python Revision/textbook/tools/nbkit.py build \
        Revision/textbook/notebooks/src/12c_a4_evolution.py --date YYYY-MM-DD
    python Revision/textbook/tools/nbkit.py check \
        Revision/textbook/notebooks/src/12c_a4_evolution.py

It takes the Lovelock components from the Revision record
Revision/field_equations_a4/a4-equations.json, integrates the evolution equation
a4'' F(a4') = kappa (p3 - p_t) with a fourth-order Runge-Kutta method for PRESCRIBED
anisotropic stresses (test inputs, not sources derived from a field), compares with
exact solutions, and checks the constraint and the conservation law along the solutions.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools"))
from nbkit import code, md, run_builder  # noqa: E402

FACTS = {
    "id": "12c",
    "name": "12c_a4_evolution",
    "title": "Integrating the evolution equation of a4 for prescribed sources",
    "purpose": (
        "It integrates the evolution equation of the author's metric, in which the "
        "second derivative of a4 times the factor F equals kappa (p3 - p_t), with the "
        "fourth-order Runge-Kutta method for prescribed anisotropic stresses p3 - p_t "
        "(zero, a pulse, a stress proportional to the rate of a4, a constant stress in "
        "Einstein-Gauss-Bonnet gravity), compares every history a4(x4) with its exact "
        "solution, measures the convergence order, computes the energy density and the "
        "pressures that each history requires, checks numerically that the constraint "
        "and the conservation law hold along the solutions, and draws six teaching "
        "plots of a4, its rate and the scale factors of 3-space and of the deflating "
        "extra times."
    ),
    "records": [
        ["Revision/field_equations_a4/a4-equations.json",
         "the Lovelock components and the factor F of the evolution equation"],
        ["Revision/field_equations_a4/reports/python-a4-report.json",
         "the sympy checks of the a4 record that the notebook reproduces"],
        ["Revision/field_equations_a4/reports/wolfram-a4-report.json",
         "the Wolfram checks of the a4 record that the notebook reproduces"],
        ["Revision/field_equations_a4/reports/ks-source-conditions.json",
         "the record that no Kohn-Sham state of the repository is an admissible source"],
    ],
    "packages": ["numpy", "sympy", "matplotlib"],
    "needs_rust": [],
    "expected_seconds": 10,
    "timeout_seconds": 600,
    "files_written": [
        "Revision/textbook/figures/12c.captions.json",
        "Revision/textbook/figures/12c_1_linear_member.png",
        "Revision/textbook/figures/12c_2_stress_pulse.png",
        "Revision/textbook/figures/12c_3_required_source.png",
        "Revision/textbook/figures/12c_4_damped_deflation.png",
        "Revision/textbook/figures/12c_5_rk4_convergence.png",
        "Revision/textbook/figures/12c_6_gauss_bonnet_breakdown.png",
    ],
    "final_lines": [
        "PASS all six figure files exist",
        "ALL 21 CHECKS PASSED (notebook 12c)",
    ],
    "troubleshooting": [
        ["\"FileNotFoundError\" naming a4-equations.json",
         "the notebook reads the Revision record of the repository. Run it inside the "
         "folder Revision/textbook/notebooks of a complete copy of the repository made "
         "with git clone, not on a copy of the notebook file alone."],
        ["\"RuntimeWarning: overflow\" or \"invalid value\" below a cell after you changed "
         "a number",
         "a changed coupling or stress drove a4' past the point where F vanishes; the "
         "notebook as distributed stops every integration before that point. Undo the "
         "change or lower the stress."],
    ],
}

CELLS = [
    md(r"""
    ## 1. What this notebook computes

    The field equations for $a_4(x_4)$ contain one equation with the second derivative
    $a_4''$, the **evolution equation**

    $$a_4''\,F(a_4') = \kappa\,(p_3 - p_t),$$

    where $p_3 - p_t$ is the difference between the pressure along 3-space and the
    pressure along the extra times (the **anisotropic stress**). If $p_3 - p_t$ is
    given as a function of the time $x_4$, this is an ordinary differential equation
    for $a_4$, and we can solve it step by step on the computer. This notebook

    - takes $F$ and the other Lovelock components from the Revision record;
    - writes a fourth-order Runge-Kutta solver (RK4) and tests it;
    - integrates the equation for four **prescribed** stresses: zero (the linear
      member), a short pulse that switches the deflation of the extra times on, a
      stress that brakes the deflation, and a constant stress in Einstein-Gauss-Bonnet
      gravity, where the equation breaks down at a finite time;
    - compares each numerical history with its exact solution and measures the
      convergence order of RK4;
    - computes the energy density and the pressures that each history requires, and
      checks that the constraint and the conservation law hold along the solution;
    - draws six plots of $a_4$, its rate $a_4'$, and the scale factors $e^{a_4}$ of
      3-space and $e^{-a_4}$ of the deflating extra times.
    """),
    md(r"""
    ## 3. The words used in this notebook

    - **Ordinary differential equation (ODE)**: an equation for an unknown function of
      one variable (here $a_4(x_4)$) that contains its derivatives.
    - **Initial value problem**: an ODE together with the starting values, here
      $a_4(0) = 0$ and the starting rate $a_4'(0)$.
    - **First-order system**: the second-order equation written as two first-order
      ones, $\frac{d}{dx_4}a_4 = v$ and $\frac{d}{dx_4}v = \kappa(p_3 - p_t)/F(v)$,
      with $v = a_4'$.
    - **RK4** (Runge-Kutta of fourth order): a rule that advances the solution by one
      step $h$ using four evaluations of the right-hand side; its error shrinks like
      $h^4$.
    - **Convergence order**: the power $q$ in "error $\approx$ constant $\times h^q$";
      halving $h$ divides the error by $2^q$.
    - **Anisotropic stress** $\Delta = p_3 - p_t$: the difference of the pressures along
      3-space and along the extra times.
    - **Prescribed source**: a source that we choose by hand to see what the equations
      do (status ASSUMED); it is not derived from any field of the theory.
    - **Scale factor**: the factor by which lengths along a direction grow:
      $e^{a_4}$ for 3-space and $e^{-a_4}$ for the extra times $x_5, x_6, x_7$ (times
      the common factor $\sin^{1/6} z$, which does not change with $x_4$).
    - **Constraint**: the time component of the field equations, which fixes the
      energy density $\rho$ from $a_4'$; **conservation**: $\rho' = -3a_4'(p_3 - p_t)$.
    - **Breakdown**: a point where $F(a_4') = 0$, so that the evolution equation can no
      longer be solved for $a_4''$.
    - **Units**: $H = 1$ and $\kappa = 1$: the time $x_4$ is measured in units of
      $1/H$, $a_4'$ in units of $H$, $\kappa\rho$ and the pressures in units of $H^2$.
    """),
    md(r"""
    ## 4. The physical and mathematical situation

    For a source that does not depend on $x_8$ and has no mixed components, the
    field equations of the author's metric are (Revision record `a4-equations.json`)

    $$\kappa\rho = -\Big(\sum_k\alpha_k E_{(k)}{}^{x_4}{}_{x_4}(a_4') + \Lambda\Big),
    \qquad \kappa p_8 = \sum_k\alpha_k E_{(k)}{}^{x_8}{}_{x_8}(a_4') + \Lambda,$$
    $$a_4''\,F(a_4') = \kappa(p_3 - p_t),\qquad p_3 + p_t = 2p_8.$$

    We choose (prescribe) the anisotropic stress $\Delta(x_4) = p_3 - p_t$ and the
    starting values $a_4(0)$, $a_4'(0)$. The evolution equation then determines
    $a_4(x_4)$; the first equation gives the energy density, the second the hidden
    pressure, and $p_3 = p_8 + \Delta/2$, $p_t = p_8 - \Delta/2$. The record proves
    that the derivative of the constraint is $3a_4'$ times the evolution equation; so
    along a solution the energy density must obey $\rho' = -3a_4'\Delta$, which this
    notebook checks numerically.

    **Honesty.** Every stress used here is a mathematical test input (ASSUMED). The
    Revision record constructs no state of either field that produces it, and it shows
    that the Kohn-Sham states of the repository are not admissible sources (section 13
    of this notebook reads that record). The histories below show what the equations
    do, not what the universe did.
    """),
    md(r"""
    ## 5. The Revision records and the Lovelock components

    The next cell defines the helpers that read the Revision records (as in every
    notebook of this chapter) and turns three entries of `a4-equations.json` into
    Python functions of the rate $v = a_4'$ and the couplings, with $H = 1$:
    `rho_side(v, a1, a2, a3)` $= \sum_k\alpha_kE_{(k)}{}^{x_4}{}_{x_4}$,
    `p8_side(v, a1, a2, a3)` $= \sum_k\alpha_kE_{(k)}{}^{x_8}{}_{x_8}$ and
    `F_of(v, a1, a2, a3)` $= F$. `sp.lambdify` turns a sympy formula into a fast
    numpy function.
    """),
    code(r'''
    import math  # the error function erf, for an exact solution

    import matplotlib.ticker  # control of the tick labels of an axis
    import numpy as np  # arrays of numbers
    import sympy as sp  # exact algebra, used here only to read the record formulas

    PY = "Revision/field_equations_a4/reports/python-a4-report.json"  # sympy record
    WL = "Revision/field_equations_a4/reports/wolfram-a4-report.json"  # Wolfram record
    EQUATIONS = "Revision/field_equations_a4/a4-equations.json"  # the equations
    KS = "Revision/field_equations_a4/reports/ks-source-conditions.json"


    def read_json(relative):
        """Read a JSON file of the repository (a Revision record)."""
        return json.loads(repository_file(relative).read_text(encoding="utf-8"))


    def record_verdict(report_file, name):
        """The verdict of the check name in a report ("PASS"), None if absent."""
        for entry in read_json(report_file)["checks"]:
            if entry["name"] == name:
                return entry["verdict"]
        return None


    def reproduces(condition, name, report_file, record_name):
        """A check that also requires the record check record_name to be PASS."""
        found = record_verdict(report_file, record_name) == "PASS"
        check(condition and found, name, record=f"{report_file}, check {record_name}")


    record = read_json(EQUATIONS)
    H, ad1, ad2 = sp.symbols("H ad1 ad2", real=True)
    a1, a2, a3 = sp.symbols("alpha1 alpha2 alpha3", real=True)
    LOCALS = {"H": H, "ad1": ad1, "ad2": ad2, "alpha1": a1, "alpha2": a2, "alpha3": a3}


    def from_record(text):
        """A Wolfram InputForm text of the record as a sympy expression with H = 1."""
        return sp.sympify(text.replace("^", "**"), locals=LOCALS).subs(H, 1)


    lovelock = record["lovelockTensors"]
    weights = {1: a1, 2: a2, 3: a3}


    def lovelock_sum(component):
        """sum_k alpha_k E_(k) of one component ("x4x4" or "x8x8") of the record."""
        return sum(weights[k] * from_record(lovelock[f"E{k}"][component]["input"])
                   for k in (1, 2, 3))


    e44 = lovelock_sum("x4x4")  # the time component (constraint)
    e88 = lovelock_sum("x8x8")  # the hidden component
    F_expr = from_record(record["generalSource"]["evolution_F"]["input"])
    rho_side = sp.lambdify((ad1, a1, a2, a3), e44, "numpy")
    p8_side = sp.lambdify((ad1, a1, a2, a3), e88, "numpy")
    F_of = sp.lambdify((ad1, a1, a2, a3), F_expr, "numpy")
    say(f"F(a4') with H = 1: {F_expr}")
    EINSTEIN = (1.0, 0.0, 0.0)  # alpha1, alpha2, alpha3 of Einstein gravity
    '''),
    md(r"""
    The next cell checks that for Einstein gravity these functions are what the record
    says: $F = 2$ (the evolution equation is $2a_4'' = \kappa(p_3 - p_t)$),
    $E^{x_4}{}_{x_4} = 3(a_4')^2 + 21$ and $E^{x_8}{}_{x_8} = 15 - 3(a_4')^2$ (with
    $H = 1$), at five rates $a_4'$.
    """),
    code(r'''
    rates = np.array([-2.0, -0.5, 0.0, 1.0, 3.0])  # a few values of a4'
    ok = (np.allclose(F_of(rates, *EINSTEIN), 2.0)
          and np.allclose(rho_side(rates, *EINSTEIN), 3 * rates ** 2 + 21)
          and np.allclose(p8_side(rates, *EINSTEIN), 15 - 3 * rates ** 2))
    reproduces(ok, "Einstein: F = 2, E44 = 3 a4'^2 + 21, E88 = 15 - 3 a4'^2 (H = 1)",
               PY, "einstein_components")
    '''),
    md(r"""
    ## 6. The Runge-Kutta method of fourth order

    For a system $\frac{dy}{dx} = f(x, y)$ (here $y$ is a list of numbers) one RK4 step
    of size $h$ from $(x, y)$ computes

    $$k_1 = f(x, y),\quad k_2 = f(x + \tfrac h2, y + \tfrac h2 k_1),\quad
    k_3 = f(x + \tfrac h2, y + \tfrac h2 k_2),\quad k_4 = f(x + h, y + hk_3),$$
    $$y_{\text{new}} = y + \tfrac h6(k_1 + 2k_2 + 2k_3 + k_4).$$

    The function `rk4` below repeats this step. Its optional argument `stop` is a
    function of $y$; when it returns True the integration ends (used in section 12 to
    stop before $F$ reaches zero). The test integrates $y' = -y$, $y(0) = 1$, from 0
    to 1 with 20 steps; the exact value is $y(1) = e^{-1}$, and the RK4 error must be
    tiny (below $10^{-7}$).
    """),
    code(r'''
    def rk4(rhs, y0, h, steps, stop=None):
        """Solve dy/dx = rhs(x, y), y(0) = y0, with at most steps RK4 steps of size h.
        Return the arrays x (one value per step) and y (one row per step)."""
        xs = [0.0]
        ys = [np.array(y0, dtype=float)]
        for n in range(steps):
            x, y = xs[-1], ys[-1]
            k1 = rhs(x, y)
            k2 = rhs(x + h / 2, y + h / 2 * k1)
            k3 = rhs(x + h / 2, y + h / 2 * k2)
            k4 = rhs(x + h, y + h * k3)
            xs.append((n + 1) * h)  # (n + 1) h avoids adding up rounding errors
            ys.append(y + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4))
            if stop is not None and stop(ys[-1]):
                break
        return np.array(xs), np.array(ys)


    x_test, y_test = rk4(lambda x, y: -y, [1.0], 0.05, 20)
    error_test = abs(y_test[-1, 0] - math.exp(-1.0))
    say(f"y' = -y: RK4 with h = 0.05 gives y(1) = {y_test[-1, 0]:.10f}; "
        f"exact {math.exp(-1.0):.10f}")
    check(error_test < 1e-7, "RK4 solves y' = -y to better than 1e-7 with 20 steps")
    '''),
    md(r"""
    ## 7. No anisotropic stress: the linear member

    The state is $y = (a_4, a_4', \kappa\rho)$. The right-hand side is

    $$\frac{d}{dx_4}a_4 = a_4',\qquad \frac{d}{dx_4}a_4' = \frac{\kappa\Delta(x_4)}
    {F(a_4')},\qquad \frac{d}{dx_4}(\kappa\rho) = -3a_4'\,\kappa\Delta(x_4).$$

    The third line is the conservation law; we integrate it alongside so that we can
    later compare the energy density it gives with the one the constraint gives. The
    helper `history` builds the right-hand side for a stress function and the
    couplings, starts with $\kappa\rho$ from the constraint, and integrates.

    With $\Delta = 0$ the equation is $a_4'' = 0$, so $a_4 = a_4'(0)\,x_4$: the linear
    member $a_4 = AHx_4$ with $A = a_4'(0)/H$. The next cell integrates it for
    $A = 1, 0, -1$ up to $x_4 = 3$ and compares with the exact straight line.
    """),
    code(r'''
    def history(stress, rate0, h, steps, couplings=EINSTEIN, Lam=0.0, stop=None):
        """Integrate (a4, a4', kappa rho) for the prescribed stress kappa Delta(x4, y),
        starting at a4 = 0, a4' = rate0 and kappa rho from the constraint."""
        def rhs(x, y):
            push = stress(x, y)  # kappa (p3 - pt) at this time
            return np.array([y[1], push / F_of(y[1], *couplings), -3.0 * y[1] * push])

        rho0 = -(rho_side(rate0, *couplings) + Lam)  # kappa rho at x4 = 0
        return rk4(rhs, [0.0, rate0, rho0], h, steps, stop)


    def no_stress(x, y):
        return 0.0  # Delta = 0: an isotropic source


    linear = {}  # slope A -> (x4, solution)
    for slope in (1.0, 0.0, -1.0):
        linear[slope] = history(no_stress, slope, 0.01, 300)
        x4, y = linear[slope]
        error = np.max(np.abs(y[:, 0] - slope * x4))  # compare with a4 = A x4
        check(error < 1e-12, f"Delta = 0, A = {slope:g}: a4 = A H x4 exactly")
    x4, y = linear[1.0]
    report("A = 1, Lambda = 0: kappa rho along the history", f"{y[-1, 2]:.6f}", "H^2")
    product = np.exp(3 * y[:, 0]) * np.exp(-3 * y[:, 0])  # e^(3 a4) e^(-3 a4)
    check(np.max(np.abs(product - 1.0)) < 1e-12,
          "the 7-volume factor e^(3 a4) e^(-3 a4) stays 1")
    '''),
    md(r"""
    The next cell draws the three linear histories and, for $A = 1$, the scale factor
    $e^{a_4}$ of 3-space and $e^{-a_4}$ of the extra times on a logarithmic vertical
    axis (on which an exponential is a straight line). Their cube product
    $e^{3a_4}e^{-3a_4} = 1$, the volume factor of the seven directions
    $x_1, x_2, x_3, x_5, x_6, x_7$, stays constant: 3-space gains exactly what the
    extra times lose.
    """),
    code(r'''
    fig, (left, right) = plt.subplots(1, 2, figsize=(11.0, 4.2))
    for slope, style in ((1.0, "-"), (0.0, ":"), (-1.0, "--")):
        x4, y = linear[slope]
        left.plot(x4, y[:, 0], style, label=f"$A = {slope:g}$")
    left.set_xlabel("time $x_4$ (units $1/H$)")
    left.set_ylabel("$a_4$")
    left.set_title("$\\Delta = 0$: $a_4 = AHx_4$")
    left.legend(fontsize=8)
    x4, y = linear[1.0]
    right.semilogy(x4, np.exp(y[:, 0]), label="3-space $e^{a_4}$ (inflates)")
    right.semilogy(x4, np.exp(-y[:, 0]), "--", label="extra times $e^{-a_4}$ (deflate)")
    right.semilogy(x4, np.exp(3 * y[:, 0]) * np.exp(-3 * y[:, 0]), ":", color="black",
                   label="$e^{3a_4}e^{-3a_4} = 1$")
    right.set_xlabel("time $x_4$ (units $1/H$)")
    right.set_ylabel("scale factor")
    right.set_title("$A = 1$: the scale factors")
    right.legend(fontsize=8)
    save_figure(fig, "linear_member",
                "Without anisotropic stress ($p_3 = p_t$) the evolution equation gives "
                "$a_4^{\\prime\\prime} = 0$. Left: the numerical histories $a_4(x_4)$ "
                "for the starting rates $A = 1$ (solid), $0$ (dotted) and $-1$ "
                "(dashed), straight lines "
                "$a_4 = AHx_4$; horizontal axis the time $x_4$ in units of $1/H$. Right: "
                "for $A = 1$ the scale factor $e^{a_4}$ of 3-space (inflating) and "
                "$e^{-a_4}$ of the extra times (deflating exponentially) on a "
                "logarithmic axis, and the constant product $e^{3a_4}e^{-3a_4} = 1$: "
                "what 3-space gains, the extra times lose.")
    '''),
    md(r"""
    ## 8. A pulse of anisotropic stress switches the deflation on

    Now we start static ($a_4'(0) = 0$) and prescribe a short pulse of stress around
    the time $x_c = 3$ with width $w = 0.5$:

    $$\kappa\Delta(x_4) = \kappa\Delta_0\,e^{-((x_4 - x_c)/w)^2},\qquad
    \kappa\Delta_0 = \frac{2}{w\sqrt\pi}.$$

    In Einstein gravity $a_4'' = \kappa\Delta/2$. Integrating once, with
    $\int e^{-t^2}dt = \tfrac{\sqrt\pi}{2}\operatorname{erf}(t)$ (erf is the *error
    function*; it rises from $-1$ to $1$):

    $$a_4'(x_4) = \frac{\kappa\Delta_0 w\sqrt\pi}{4}\Big(\operatorname{erf}
    \frac{x_4 - x_c}{w} + \operatorname{erf}\frac{x_c}{w}\Big)
    = \frac12\Big(\operatorname{erf}\frac{x_4 - x_c}{w}
    + \operatorname{erf}\frac{x_c}{w}\Big),$$

    which rises from 0 to almost exactly 1: after the pulse the history is the
    deflating linear member with $A = 1$. Integrating again, with
    $\int\operatorname{erf}(t)\,dt = t\operatorname{erf}(t) + e^{-t^2}/\sqrt\pi$, gives
    $a_4(x_4)$ exactly. The next cell integrates numerically up to $x_4 = 8$ with
    $h = 0.01$ and compares both.
    """),
    code(r'''
    X_C, WIDTH = 3.0, 0.5  # the centre and the width of the pulse
    PUSH = 2.0 / (WIDTH * math.sqrt(math.pi))  # kappa Delta_0


    def pulse(x, y):
        return PUSH * math.exp(-((x - X_C) / WIDTH) ** 2)  # kappa Delta(x4)


    def exact_pulse(x):
        """The exact a4 and a4' of the pulse history (Einstein, a4(0) = a4'(0) = 0)."""
        scale = PUSH * WIDTH * math.sqrt(math.pi) / 4  # = 1/2
        t, t0 = (x - X_C) / WIDTH, -X_C / WIDTH  # the argument now and at x4 = 0

        def antiderivative(s):  # an antiderivative of erf
            return s * math.erf(s) + math.exp(-s * s) / math.sqrt(math.pi)

        rate = scale * (math.erf(t) + math.erf(X_C / WIDTH))
        a4 = scale * (WIDTH * (antiderivative(t) - antiderivative(t0))
                      + x * math.erf(X_C / WIDTH))
        return a4, rate


    x4_pulse, y_pulse = history(pulse, 0.0, 0.01, 800)
    exact = np.array([exact_pulse(x) for x in x4_pulse])  # columns: a4, a4'
    error_a4 = np.max(np.abs(y_pulse[:, 0] - exact[:, 0]))
    error_rate = np.max(np.abs(y_pulse[:, 1] - exact[:, 1]))
    say(f"largest error: a4 {error_a4:.0e}, a4' {error_rate:.0e}")
    check(error_a4 < 1e-8 and error_rate < 1e-8,
          "pulse: RK4 (h = 0.01) agrees with the exact solution to 1e-8")
    report("rate a4'/H after the pulse (x4 = 8)", f"{y_pulse[-1, 1]:.10f}")
    check(abs(y_pulse[-1, 1] - 1.0) < 1e-8,
          "after the pulse a4' = H: the linear member A = 1")
    '''),
    md(r"""
    The next cell draws the pulse history in four panels: the prescribed stress; the
    rate $a_4'$ (numerical line and exact points); $a_4$ itself; and the two scale
    factors on a logarithmic axis.
    """),
    code(r'''
    fig, axes = plt.subplots(2, 2, figsize=(10.0, 7.0))
    stress_values = np.array([pulse(x, None) for x in x4_pulse])
    axes[0, 0].plot(x4_pulse, stress_values)
    axes[0, 0].set_ylabel("$\\kappa(p_3 - p_t)$ (units $H^2$)")
    axes[0, 0].set_title("the prescribed stress pulse")
    every = slice(0, None, 40)  # every 40th point for the exact markers
    axes[0, 1].plot(x4_pulse, y_pulse[:, 1], label="RK4")
    axes[0, 1].plot(x4_pulse[every], exact[every, 1], "o", markersize=3, label="exact")
    axes[0, 1].set_ylabel("$a_4'/H$")
    axes[0, 1].set_title("the rate $a_4'$")
    axes[0, 1].legend(fontsize=8)
    axes[1, 0].plot(x4_pulse, y_pulse[:, 0], label="RK4")
    axes[1, 0].plot(x4_pulse[every], exact[every, 0], "o", markersize=3, label="exact")
    axes[1, 0].set_ylabel("$a_4$")
    axes[1, 0].set_title("$a_4$")
    axes[1, 0].legend(fontsize=8)
    axes[1, 1].semilogy(x4_pulse, np.exp(y_pulse[:, 0]), label="3-space $e^{a_4}$")
    axes[1, 1].semilogy(x4_pulse, np.exp(-y_pulse[:, 0]), "--",
                        label="extra times $e^{-a_4}$")
    axes[1, 1].set_ylabel("scale factor")
    axes[1, 1].set_title("the scale factors")
    axes[1, 1].legend(fontsize=8)
    for ax in axes[1]:
        ax.set_xlabel("time $x_4$ (units $1/H$)")
    fig.tight_layout()
    save_figure(fig, "stress_pulse",
                "Einstein gravity, starting static ($a_4 = a_4' = 0$): a prescribed "
                "pulse of anisotropic stress $\\kappa(p_3 - p_t)$ centred at $x_4 = 3$ "
                "(top left, units $H^2$) raises the rate $a_4'$ from 0 to $H$ (top "
                "right); afterwards $a_4$ grows linearly (bottom left) and the history "
                "is the deflating linear member with $A = 1$. Bottom right: the scale "
                "factor $e^{a_4}$ of 3-space starts to inflate and $e^{-a_4}$ of the extra "
                "times to deflate exponentially once the pulse has passed. Lines: RK4 "
                "with step $h = 0.01$; dots: the exact solution with the error "
                "function. Horizontal axes: the time $x_4$ in units of $1/H$.")
    '''),
    md(r"""
    ## 9. The source the pulse history requires, and the constraint

    Along the pulse history the field equations fix the whole source (with
    $\Lambda = 0$):

    $$\kappa\rho = -(3(a_4')^2 + 21),\quad \kappa p_8 = 15 - 3(a_4')^2,\quad
    \kappa p_3 = \kappa p_8 + \tfrac12\kappa\Delta,\quad
    \kappa p_t = \kappa p_8 - \tfrac12\kappa\Delta.$$

    The third component of our state, $\kappa\rho$ integrated from the conservation law
    $\rho' = -3a_4'\Delta$, must agree with the $\kappa\rho$ that the constraint gives
    at every time: this is the numerical form of the record's proof that the
    derivative of the constraint is $3a_4'$ times the evolution equation. The next
    cell checks the agreement, checks that the source ends on the linear member's
    values $\kappa\rho = -24$, $\kappa p = 12$ (for $A = 1$), and draws the four source
    components and the size of the disagreement.
    """),
    code(r'''
    rate = y_pulse[:, 1]
    rho_constraint = -(rho_side(rate, *EINSTEIN) + 0.0)  # kappa rho, Lambda = 0
    p8_values = p8_side(rate, *EINSTEIN) + 0.0  # kappa p8
    p3_values = p8_values + stress_values / 2  # kappa p3
    pt_values = p8_values - stress_values / 2  # kappa pt
    mismatch = np.abs(y_pulse[:, 2] - rho_constraint)  # conservation versus constraint
    say(f"largest difference of the two energy densities: {mismatch.max():.0e}")
    reproduces(mismatch.max() < 1e-8,
               "the energy density from conservation equals the constraint along x4",
               WL, "constraint_propagation_bianchi")
    check(abs(rho_constraint[-1] + 24) < 1e-6 and abs(p8_values[-1] - 12) < 1e-6,
          "after the pulse: kappa rho = -24, kappa p = 12 (the linear member A = 1)")
    fig, (left, right) = plt.subplots(1, 2, figsize=(11.0, 4.2))
    left.plot(x4_pulse, rho_constraint, label="$\\kappa\\rho$")
    left.plot(x4_pulse, p3_values, label="$\\kappa p_3$")
    left.plot(x4_pulse, pt_values, "--", label="$\\kappa p_t$")
    left.plot(x4_pulse, p8_values, ":", color="black", label="$\\kappa p_8$")
    left.set_xlabel("time $x_4$ (units $1/H$)")
    left.set_ylabel("required source (units $H^2$)")
    left.set_title("the source of the pulse history")
    left.legend(fontsize=8)
    right.semilogy(x4_pulse, np.maximum(mismatch, 1e-16))  # exact zeros at 1e-16
    right.set_xlabel("time $x_4$ (units $1/H$)")
    right.set_ylabel("$|\\kappa\\rho$ conserved $-$ $\\kappa\\rho$ constraint$|$")
    right.set_title("conservation agrees with the constraint")
    save_figure(fig, "required_source",
                "Left: the source that the pulse history requires in Einstein gravity "
                "with $\\Lambda = 0$, in units of $H^2$: the energy density $\\kappa\\rho$, "
                "the pressures $\\kappa p_3$ (3-space), $\\kappa p_t$ (extra times, "
                "dashed) and $\\kappa p_8$ (hidden direction, dotted). During the pulse "
                "$p_3$ and $p_t$ split by the prescribed stress; before it the source "
                "is that of the static member ($\\kappa\\rho = -21$, $\\kappa p = 15$), "
                "after it that of the linear member $A = 1$ ($\\kappa\\rho = -24$, "
                "$\\kappa p = 12$). Right: on a logarithmic axis, the difference between "
                "the energy density integrated from the conservation law and the one "
                "given by the constraint (an exact zero is drawn at $10^{-16}$). The two "
                "agree to about $2 \\times 10^{-11}$, the accuracy of the RK4 "
                "integration with the step $h = 0.01$.")
    '''),
    md(r"""
    ## 10. A stress that brakes the deflation

    A stress can also depend on the state. We prescribe
    $\kappa\Delta = -2\eta\,a_4'$ with a constant $\eta > 0$ (a resistance proportional
    to the rate, like friction). In Einstein gravity $a_4'' = -\eta a_4'$, so

    $$a_4' = Ae^{-\eta x_4},\qquad a_4 = \frac{A}{\eta}\big(1 - e^{-\eta x_4}\big).$$

    The deflation slows down and stops: the extra-time scale factor $e^{-a_4}$ falls
    only to the final value $e^{-A/\eta}$. The next cell integrates this for $A = 1$
    and $\eta = 0.25, 0.5, 1$ up to $x_4 = 10$, compares with the exact solution, and
    checks the conservation law, which here reads $\kappa\rho' = 6\eta(a_4')^2 > 0$.
    """),
    code(r'''
    damped = {}  # eta -> (x4, solution)
    for eta in (0.25, 0.5, 1.0):
        def friction(x, y, eta=eta):
            return -2.0 * eta * y[1]  # kappa Delta = -2 eta a4'

        x4, y = history(friction, 1.0, 0.01, 1000)
        damped[eta] = (x4, y)
        exact_a4 = (1.0 / eta) * (1.0 - np.exp(-eta * x4))
        error = np.max(np.abs(y[:, 0] - exact_a4))
        mismatch = np.max(np.abs(y[:, 2] + rho_side(y[:, 1], *EINSTEIN)))
        check(error < 1e-9 and mismatch < 1e-8,
              f"eta = {eta}: a4 = (1 - e^(-eta x4))/eta, conservation holds")
        report(f"eta = {eta}: final extra-time scale factor e^(-a4(10))",
               f"{math.exp(-y[-1, 0]):.6f}")
    '''),
    md(r"""
    The next cell draws the rate $a_4'$ and the extra-time scale factor $e^{-a_4}$ for
    the three values of $\eta$, with the undamped linear member ($\eta = 0$) for
    comparison.
    """),
    code(r'''
    fig, (left, right) = plt.subplots(1, 2, figsize=(11.0, 4.2))
    x4 = damped[0.25][0]
    left.plot(x4, np.ones_like(x4), ":", color="black", label="$\\eta = 0$")
    right.semilogy(x4, np.exp(-x4), ":", color="black", label="$\\eta = 0$: $e^{-x_4}$")
    for eta, (x4, y) in damped.items():
        left.plot(x4, y[:, 1], label=f"$\\eta = {eta}$")
        right.semilogy(x4, np.exp(-y[:, 0]), label=f"$\\eta = {eta}$")
    left.set_xlabel("time $x_4$ (units $1/H$)")
    left.set_ylabel("$a_4'/H$")
    left.set_title("the deflation rate decays")
    left.legend(fontsize=8)
    right.set_xlabel("time $x_4$ (units $1/H$)")
    right.set_ylabel("extra-time scale factor $e^{-a_4}$")
    right.set_title("the extra times stop deflating")
    right.legend(fontsize=8)
    save_figure(fig, "damped_deflation",
                "Einstein gravity with the prescribed braking stress "
                "$\\kappa(p_3 - p_t) = -2\\eta a_4'$, starting from the deflating rate "
                "$a_4' = H$: left, the rate $a_4' = He^{-\\eta x_4}$ for $\\eta = 0.25$, "
                "$0.5$ and $1$ (units $H$), with the undamped case $\\eta = 0$ dotted; "
                "right, the scale factor $e^{-a_4}$ of the extra times on a logarithmic "
                "axis. Without braking the extra times deflate forever "
                "($e^{-x_4}$); with braking they stop at $e^{-1/\\eta}$. Horizontal "
                "axes: the time $x_4$ in units of $1/H$.")
    '''),
    md(r"""
    ## 11. How fast does RK4 converge?

    For the braking history the right-hand side depends on the solution itself, so it
    is a genuine differential equation and a good test of the method. (For the pulse
    the stress depends on $x_4$ alone; RK4 then reduces to Simpson's rule for an
    integrand that vanishes smoothly at both ends, and such integrals converge much
    faster than $h^4$, which would hide the order.) The next cell integrates the
    braking history with $\\eta = 1$ up to $x_4 = 8$ with the step sizes
    $h = 0.4, 0.2, 0.1, 0.05, 0.025$ and measures the error of $a_4(8)$ against the
    exact value $1 - e^{-8}$. If the error behaves like $Ch^4$, halving $h$ divides it
    by $2^4 = 16$, and the measured order $\log_2(e_h / e_{h/2})$ is close to 4. The
    table prints each step, its error and the order; the plot shows the errors on
    logarithmic axes, where $Ch^4$ is a straight line of slope 4.
    """),
    code(r'''
    def braking_unit(x, y):
        return -2.0 * y[1]  # kappa Delta = -2 eta a4' with eta = 1


    exact_end = 1.0 - math.exp(-8.0)  # the exact a4(8) for eta = 1, A = 1
    steps_list = [20, 40, 80, 160, 320]  # h = 8/steps = 0.4, 0.2, 0.1, 0.05, 0.025
    sizes, errors = [], []
    for steps in steps_list:
        x4, y = history(braking_unit, 1.0, 8.0 / steps, steps)
        sizes.append(8.0 / steps)
        errors.append(abs(y[-1, 0] - exact_end))
    orders = [math.log2(errors[i] / errors[i + 1]) for i in range(len(errors) - 1)]
    for i, (size, error) in enumerate(zip(sizes, errors)):
        order = f"{orders[i - 1]:.2f}" if i > 0 else "-"
        say(f"h = {size:<6} error of a4(8) = {error:.2e}   measured order {order}")
    check(all(3.7 < q < 4.3 for q in orders),
          "RK4 converges with order 4 (measured orders between 3.7 and 4.3)")
    fig, ax = plt.subplots()
    ax.loglog(sizes, errors, "o-", label="error of $a_4(8)$")
    reference = errors[-1] * (np.array(sizes) / sizes[-1]) ** 4
    ax.loglog(sizes, reference, "--", color="black", label="slope 4: $C h^4$")
    ax.set_xticks(sizes)  # one tick at each step size used
    ax.set_xticklabels([f"{size:g}" for size in sizes])
    ax.xaxis.set_minor_formatter(matplotlib.ticker.NullFormatter())  # no extra labels
    ax.set_xlabel("step size $h$ (units $1/H$)")
    ax.set_ylabel("absolute error")
    ax.set_title("RK4 on the braking history: fourth-order convergence")
    ax.legend(fontsize=8)
    save_figure(fig, "rk4_convergence",
                "The error of the RK4 value of $a_4$ at $x_4 = 8$ for the braking "
                "history with $\\eta = 1$ (exact value $1 - e^{-8}$), for the step sizes "
                "$h = 0.4$, $0.2$, $0.1$, $0.05$ and $0.025$ (units $1/H$), on "
                "logarithmic axes. The points follow the dashed reference line $Ch^4$ "
                "of slope 4: halving the step divides the error by about 16, the "
                "fourth-order convergence of the Runge-Kutta method.")
    '''),
    md(r"""
    ## 12. Einstein-Gauss-Bonnet gravity: the evolution equation breaks down

    With the Gauss-Bonnet coupling ($\alpha_1 = 1$, $\alpha_3 = 0$, $H = 1$),
    $F(a_4') = 2 - 80\alpha_2 - 48\alpha_2(a_4')^2$ decreases as $|a_4'|$ grows and
    vanishes at $a_4'_c = \sqrt{(2 - 80\alpha_2)/(48\alpha_2)}$. For a constant stress
    $\kappa\Delta$ the equation $F(a_4')\,a_4'' = \kappa\Delta$ can be integrated
    once: with $G(v) = (2 - 80\alpha_2)v - 16\alpha_2v^3$ (so that $dG/dv = F$),

    $$G(a_4'(x_4)) = G(a_4'(0)) + \kappa\Delta\,x_4 .$$

    $G$ has its maximum at $a_4'_c$, so the rate reaches $a_4'_c$ at the finite time
    $x_4^{\star} = (G(a_4'_c) - G(a_4'(0)))/(\kappa\Delta)$, with $a_4'' = \kappa\Delta/F$
    growing without bound; beyond it the equation has no solution with a smooth
    $a_4'$. The next cell integrates with $\kappa\Delta = 0.5$, $a_4'(0) = 0.5$ and
    $\alpha_2 = 0.005, 0.01$ (step $h = 0.001$), stops when $F < 0.05$, and checks the
    integrated relation and the breakdown time.
    """),
    code(r'''
    STRESS, RATE0 = 0.5, 0.5  # kappa Delta and the starting rate a4'(0)


    def constant_stress(x, y):
        return STRESS


    breakdown = {}  # alpha2 -> (x4, solution, predicted breakdown time)
    for alpha2 in (0.005, 0.01):
        couplings = (1.0, alpha2, 0.0)

        def G(v, alpha2=alpha2):
            return (2 - 80 * alpha2) * v - 16 * alpha2 * v ** 3  # dG/dv = F

        critical = math.sqrt((2 - 80 * alpha2) / (48 * alpha2))  # F(critical) = 0
        x_star = (G(critical) - G(RATE0)) / STRESS  # the breakdown time

        def near_zero(y, couplings=couplings):
            return F_of(y[1], *couplings) < 0.05  # stop before F reaches zero

        x4, y = history(constant_stress, RATE0, 0.001, 20000, couplings,
                        stop=near_zero)
        breakdown[alpha2] = (x4, y, x_star)
        residual = np.max(np.abs(G(y[:, 1]) - G(RATE0) - STRESS * x4))
        check(residual < 1e-6, f"alpha2 = {alpha2}: G(a4') = G(a4'(0)) + kappa Delta x4")
        check(abs(x4[-1] - x_star) < 0.01,
              f"alpha2 = {alpha2}: F reaches 0 near the predicted time x4*")
        report(f"alpha2 = {alpha2}: critical rate, breakdown time x4*",
               f"{critical:.4f} H, {x_star:.4f}/H")
    '''),
    md(r"""
    The next cell compares the two Gauss-Bonnet histories with Einstein gravity, where
    $F = 2$ and the rate simply grows linearly, $a_4' = 0.5 + 0.25x_4$, and draws
    $F(a_4'(x_4))$ along each history.
    """),
    code(r'''
    x_einstein, y_einstein = history(constant_stress, RATE0, 0.01, 500)
    check(np.max(np.abs(y_einstein[:, 1] - (RATE0 + STRESS * x_einstein / 2))) < 1e-12,
          "Einstein: a4' = 0.5 + 0.25 x4 for the constant stress")
    fig, (left, right) = plt.subplots(1, 2, figsize=(11.0, 4.2))
    left.plot(x_einstein, y_einstein[:, 1], color="black", label="Einstein")
    right.plot(x_einstein, F_of(y_einstein[:, 1], *EINSTEIN) * np.ones_like(x_einstein),
               color="black", label="Einstein")
    for alpha2, (x4, y, x_star) in breakdown.items():
        line = left.plot(x4, y[:, 1], label=f"$\\alpha_2H^2 = {alpha2}$")[0]
        left.axvline(x_star, linestyle="--", color=line.get_color(), linewidth=0.8)
        right.plot(x4, F_of(y[:, 1], 1.0, alpha2, 0.0), color=line.get_color(),
                   label=f"$\\alpha_2H^2 = {alpha2}$")
    left.set_xlabel("time $x_4$ (units $1/H$)")
    left.set_ylabel("$a_4'/H$")
    left.set_title("the rate under a constant stress")
    left.legend(fontsize=8)
    right.axhline(0.0, color="black", linewidth=0.8)
    right.set_xlabel("time $x_4$ (units $1/H$)")
    right.set_ylabel("$F(a_4')$")
    right.set_title("$F$ along the history")
    right.legend(fontsize=8)
    save_figure(fig, "gauss_bonnet_breakdown",
                "A constant prescribed stress $\\kappa(p_3 - p_t) = 0.5H^2$ starting from "
                "$a_4' = 0.5H$. Left: the rate $a_4'$ in Einstein gravity grows "
                "linearly (black), while in Einstein-Gauss-Bonnet gravity with "
                "$\\alpha_2H^2 = 0.005$ and $0.01$ it bends upward and reaches the "
                "critical rate at the predicted finite time $x_4^{\\star}$ (dashed vertical "
                "lines), where its slope becomes infinite. Right: the factor $F(a_4')$ "
                "of the evolution equation along each history; the integration stops "
                "when $F$ falls below $0.05$, because at $F = 0$ the evolution equation "
                "breaks down. Horizontal axes: the time $x_4$ in units of $1/H$.")
    '''),
    md(r"""
    ## 13. Which sources are real? The record on the Kohn-Sham states

    The stresses above were chosen by hand. The Revision record asks the opposite
    question for the only many-particle states it has computed, the Kohn-Sham states
    of dirac16complex: can they be the source of the author's metric? The next cell
    reads the record's answer and checks that all its checks passed. The answer is no:
    every nonzero Kohn-Sham state depends on $x_8$ and violates $p_3 + p_t = 2p_8$, so
    the Kohn-Sham history $a_4 = AHx_4$ is a prescribed background, not a solution of
    these equations with that source.
    """),
    code(r'''
    ks = read_json(KS)
    say("record: " + ks["conclusion"])
    names = [entry["name"] for entry in ks["checks"]]
    check(ks["summary"]["pass"] == ks["summary"]["checks"] == 5
          and "ks_history_is_a_prescribed_background" in names,
          "record: no Kohn-Sham state is an admissible source (5 of 5 checks PASS)")
    '''),
    md(r"""
    ## 14. The last check

    The last cell checks that the six figure files exist in the folder
    Revision/textbook/figures and prints the number of checks that passed.
    """),
    code(r'''
    figure_names = ["linear_member", "stress_pulse", "required_source",
                    "damped_deflation", "rk4_convergence", "gauss_bonnet_breakdown"]
    paths = [output_file(f"{FIGURE_FOLDER}/12c_{k}_{name}.png")
             for k, name in enumerate(figure_names, 1)]
    check(all(path.is_file() for path in paths), "all six figure files exist")
    all_checks_passed()
    '''),
    md(r"""
    ## 15. What this notebook showed

    - With a prescribed anisotropic stress $p_3 - p_t$ the evolution equation
      $a_4''F(a_4') = \kappa(p_3 - p_t)$ is an ordinary differential equation for
      $a_4(x_4)$, which RK4 solves with fourth-order accuracy (COMPUTED, compared with
      exact solutions).
    - No stress gives the linear member $a_4 = AHx_4$: 3-space inflates as
      $e^{AHx_4}$ and the extra times deflate as $e^{-AHx_4}$, with a constant
      7-volume (PROVED, and reproduced numerically).
    - A pulse of stress can switch the deflation on, and a braking stress can stop it;
      the equations do not prefer either (COMPUTED for ASSUMED stresses).
    - The energy density that the conservation law gives equals the one that the
      constraint gives along every history, as the record's Bianchi identity requires
      (COMPUTED).
    - In Einstein-Gauss-Bonnet gravity a constant stress drives $a_4'$ to the zero of
      $F$ in a finite time, where the evolution equation breaks down (PROVED by the
      integrated relation, COMPUTED numerically).
    - None of these stresses is known to come from a field of the theory; the record
      shows that the Kohn-Sham states of the repository are not admissible sources
      (record ks-source-conditions.json).
    """),
]

if __name__ == "__main__":
    raise SystemExit(run_builder(__file__))
