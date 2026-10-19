#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
"""Builder of Notebook 12c, "Integrating the field equations for a4 and b4".

Textbook "Universes in Pairs", chapter 12 (the field equations for a4 and b4: Einstein and
Einstein-Lovelock).  The notebook Revision/textbook/notebooks/12c_a4_evolution.ipynb is
BUILT from this file by Revision/textbook/tools/nbkit.py (never edit the .ipynb by hand):

    python Revision/textbook/tools/nbkit.py build \
        Revision/textbook/notebooks/src/12c_a4_evolution.py --date YYYY-MM-DD
    python Revision/textbook/tools/nbkit.py check \
        Revision/textbook/notebooks/src/12c_a4_evolution.py

It takes the Lovelock components of the corrected metric from the Revision record
Revision/field_equations_a4/a4-equations.json, integrates the two equations of second
order for a4 and b4 with a fourth-order Runge-Kutta method for PRESCRIBED sources (test
inputs, not sources derived from a field), compares with exact solutions, checks the
constraint along the solutions, and recomputes the record's numbers on the Kohn-Sham
states.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools"))
from nbkit import code, md, run_builder  # noqa: E402

FACTS = {
    "id": "12c",
    "name": "12c_a4_evolution",
    "title": "Integrating the field equations for a4 and b4 for prescribed sources",
    "purpose": (
        "It integrates the two equations of second order for a4 and b4 of the corrected "
        "metric, which determine the second derivatives of a4 and of ln b4 from the "
        "3-space pressure and the hidden pressure, with the fourth-order Runge-Kutta "
        "method for prescribed "
        "sources: no source (the flat vacuum), the source of the record history (in "
        "Einstein gravity and with the author's weights), the same source from other "
        "starting rates, the source of a history whose rate rises in a pulse, and a gas "
        "of massless particles in 3-space with the author's weights, where the system "
        "becomes singular. It compares every history with its exact solution, measures "
        "the convergence order, checks that the energy density integrated from the "
        "conservation law equals the one the constraint gives, and draws seven teaching "
        "plots. At the end it reads the record on the Kohn-Sham states and recomputes "
        "its numbers from the table of their integrated energy-momentum tensors."
    ),
    "records": [
        ["Revision/field_equations_a4/a4-equations.json",
         "the Lovelock components and the source of the record history"],
        ["Revision/field_equations_a4/reports/python-a4-report.json",
         "the sympy checks of the a4 and b4 record that the notebook reproduces"],
        ["Revision/field_equations_a4/reports/wolfram-a4-report.json",
         "the Wolfram checks of the a4 and b4 record that the notebook reproduces"],
        ["Revision/field_equations_a4/ks_source/reports/ks-source-a4.json",
         "the record of the gas of massless particles as a source, whose singular point "
         "the notebook reproduces"],
        ["Revision/field_equations_a4/reports/ks-source-conditions.json",
         "the record that no Kohn-Sham state of the repository is an admissible source"],
        ["Revision/kohn_sham/results/ground/emt-integrals.csv",
         "the integrals over the hidden direction of the energy density and the pressures "
         "of every recorded Kohn-Sham ground state, from which the notebook recomputes "
         "the numbers of the record ks-source-conditions.json"],
    ],
    "packages": ["numpy", "sympy", "matplotlib"],
    "needs_rust": [],
    "expected_seconds": 20,
    "timeout_seconds": 600,
    "files_written": [
        "Revision/textbook/figures/12c.captions.json",
        "Revision/textbook/figures/12c_1_flat_member.png",
        "Revision/textbook/figures/12c_2_record_history.png",
        "Revision/textbook/figures/12c_3_starting_rate.png",
        "Revision/textbook/figures/12c_4_pulse_history.png",
        "Revision/textbook/figures/12c_5_pulse_source.png",
        "Revision/textbook/figures/12c_6_rk4_convergence.png",
        "Revision/textbook/figures/12c_7_gas_breakdown.png",
    ],
    "final_lines": [
        "PASS all seven figure files exist",
        "ALL 21 CHECKS PASSED (notebook 12c)",
    ],
    "troubleshooting": [
        ["\"FileNotFoundError\" naming a4-equations.json",
         "the notebook reads the Revision record of the repository. Run it inside the "
         "folder Revision/textbook/notebooks of a complete copy of the repository made "
         "with git clone, not on a copy of the notebook file alone."],
        ["\"RuntimeWarning: overflow\" or \"invalid value\" below a cell after you changed "
         "a number",
         "a changed source or step drove the solution to the point where the Jacobian of "
         "the two equations of second order vanishes, or the step was too large for a "
         "steep part; the notebook as distributed stops every integration before that. "
         "Undo the change or make the step smaller."],
    ],
}

CELLS = [
    md(r"""
    ## 1. What this notebook computes

    The field equations for $a_4(x_4)$ and $b_4(x_4)$ consist of a constraint (the time
    component) and two equations of second order (the 3-space component and the
    common component of the hidden direction and the extra times). The two are linear
    in $a_4''$ and $v = u'$, $u = b_4'/b_4$:

    $$J\begin{pmatrix}a_4''\\ v\end{pmatrix} = \begin{pmatrix}\kappa p_3 - \Lambda
    - R_1(a_4', u, k)\\ \kappa p_0 - \Lambda - R_0(a_4', u, k)\end{pmatrix},$$

    where $J$ is the Jacobian and $R_1$, $R_0$ are the parts of the two left-hand sides
    without $a_4''$ and $v$, and $k = e^{2a_4}/b_4$. If the pressures $p_3$ and
    $p_0 = p_t$ are given (as functions of the time or of the state), this is a system
    of ordinary differential equations for $a_4$ and $b_4$, and we can solve it step by
    step on the computer. This notebook

    - takes the Lovelock components from the Revision record;
    - writes a fourth-order Runge-Kutta solver (RK4) and tests it;
    - integrates the system for **prescribed** sources: no source (the flat vacuum),
      the source of the record history $a_4 = Hx_4$, $b_4 = e^{(4/3)Hx_4}$ in Einstein
      gravity and with the author's weights, the same source from other starting
      rates, the source of a history whose rate $a_4'$ rises in a pulse from $H$ to
      $2H$, and a gas of massless particles in 3-space with the author's weights;
    - compares each numerical history with its exact solution and measures the
      convergence order of RK4;
    - checks that the energy density integrated from the conservation law equals the
      one that the constraint gives;
    - finds where the system becomes singular for the gas;
    - reads the record on the Kohn-Sham states and recomputes its numbers;
    - draws seven plots.
    """),
    md(r"""
    ## 3. The words used in this notebook

    - **Ordinary differential equation (ODE)**: an equation for unknown functions of
      one variable (here $a_4(x_4)$ and $b_4(x_4)$) that contains their derivatives.
    - **Initial value problem**: an ODE together with the starting values, here
      $a_4(0)$, $a_4'(0)$, $b_4(0)$ and $u(0)$.
    - **State**: the list $y = (a_4, a_4', \ln b_4, u, \kappa\rho)$ that the solver
      advances; $\ln b_4$ is used instead of $b_4$ because $b_4 > 0$ grows
      exponentially.
    - **RK4** (Runge-Kutta of fourth order): a rule that advances the solution by one
      step $h$ using four evaluations of the right-hand side; its error shrinks like
      $h^4$.
    - **Convergence order**: the power $q$ in "error $\approx$ constant $\times h^q$";
      halving $h$ divides the error by $2^q$.
    - **Jacobian** $J$: the 2 by 2 table of the coefficients of $a_4''$ and $v$ in the
      two equations of second order; where $\det J = 0$ they cannot be solved for
      $a_4''$ and $v$ (a **breakdown** or singular point).
    - **Prescribed source**: a source that we choose by hand to see what the equations
      do (status ASSUMED); it is not derived from any field of the theory.
    - **Constraint**: the time component of the field equations, which fixes the
      energy density from $a_4'$, $u$ and $k$; **conservation**:
      $\partial_4\rho = -3a_4'(\rho + p_3) - 4h_4(\rho + p_0)$ with
      $h_4 = \tfrac12u - a_4'$.
    - **Scale factors**: $e^{a_4}$ for 3-space and $e^{-a_4}b_4^{1/2}$ for the hidden
      direction and the extra times (times factors of $z$ that do not change in time).
    - **Record history**: $a_4 = Hx_4$, $b_4 = e^{(4/3)Hx_4}$, the prescribed background
      of the Revision record (ASSUMED); on it the block shrinks like $e^{-Hx_4/3}$.
    - **Author's weights**: $\alpha_k = w_k/H^{2k}$ with $w = (1, \tfrac1{32},
      \tfrac1{1152})$ and $\Lambda = -10$.
    - **Units**: $H = 1$ and $\kappa = 1$: the time $x_4$ is measured in units of
      $1/H$, $a_4'$ and $u$ in units of $H$, $\kappa\rho$ and the pressures in units of
      $H^2$.
    """),
    md(r"""
    ## 4. The physical and mathematical situation

    For a source that does not depend on $x_0$ and has no mixed component, the field
    equations of the corrected metric are (Revision record `a4-equations.json`)

    $$e_{44}(a_4', u, k) + \Lambda = -\kappa\rho,\qquad
    e_{11} + \Lambda = \kappa p_3,\qquad e_{00} + \Lambda = \kappa p_0 = \kappa p_t,$$

    with $e_{hh} = \sum_k\alpha_kE_{(k)}{}^h{}_h$. We choose (prescribe) the pressures
    $p_3$ and $p_0$ and the starting values. The two equations of second order then
    determine $a_4''$ and $v$, so the solver follows $a_4$ and $b_4$; the constraint
    gives the energy density at the start, and the conservation law carries it along.
    The record proves that the derivative of the constraint is a combination of the
    other two equations (the Bianchi identity); so along a solution the energy density
    from conservation must equal the one the constraint gives, which this notebook
    checks numerically.

    **Honesty.** Every source used here is a mathematical test input (ASSUMED). The
    Revision record constructs no state of either field that produces it, and it shows
    that the Kohn-Sham states of the repository are not admissible sources (section 14
    of this notebook reads that record). The histories below show what the equations
    do, not what the universe did.
    """),
    md(r"""
    ## 5. The Revision records and the Lovelock components

    The next cell defines the helpers that read the Revision records (as in every
    notebook of this chapter; `reproduces` prints its PASS and reproduces lines with
    one call, through a text buffer, so that they stay together) and turns the record's
    components into fast numpy functions of $(a_4', u, k)$ and the couplings
    $(\alpha_1, \alpha_2, \alpha_3)$, with $H = 1$: `e44` (the constraint), `rest1` and
    `rest0` (the 3-space and the hidden components at $a_4'' = v = 0$), and the four
    entries `J11`, `J12`, `J21`, `J22` of the Jacobian. The equations are linear in
    $(a_4'', v)$, so these seven functions give the whole system. `sp.lambdify` turns a
    sympy formula into a numpy function.
    """),
    code(r'''
    import contextlib  # redirect_stdout: send printed lines into a buffer
    import io  # StringIO: a text buffer in memory
    import math  # the error function erf, for an exact solution

    import matplotlib.ticker  # control of the tick labels of an axis
    import numpy as np  # arrays of numbers
    import sympy as sp  # exact algebra, used here only to read the record formulas

    PY = "Revision/field_equations_a4/reports/python-a4-report.json"  # sympy record
    WL = "Revision/field_equations_a4/reports/wolfram-a4-report.json"  # Wolfram record
    EQUATIONS = "Revision/field_equations_a4/a4-equations.json"  # the equations
    KS_A4 = "Revision/field_equations_a4/ks_source/reports/ks-source-a4.json"
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
        """A check that also requires the record check record_name to be PASS.  Its
        printed lines (PASS and reproduces) are collected in a text buffer and printed
        by one print call, so that they always stay together in the cell's output."""
        found = record_verdict(report_file, record_name) == "PASS"
        lines = io.StringIO()  # a text buffer
        with contextlib.redirect_stdout(lines):  # print() now writes into the buffer
            check(condition and found, name, record=f"{report_file}, check {record_name}")
        print(lines.getvalue(), end="")  # all lines at once


    record = read_json(EQUATIONS)
    H, ad1, ad2, uu, vv, kk = sp.symbols("H ad1 ad2 uu vv kk", real=True)
    a1, a2, a3 = sp.symbols("alpha1 alpha2 alpha3", real=True)
    LOCALS = {"H": H, "ad1": ad1, "ad2": ad2, "uu": uu, "vv": vv, "kk": kk}


    def from_record(text):
        """A Wolfram InputForm text of the record as a sympy expression with H = 1."""
        return sp.sympify(text.replace("^", "**"), locals=LOCALS).subs(H, 1)


    lovelock = record["lovelockTensors"]
    weights = {1: a1, 2: a2, 3: a3}
    side = {key: sp.expand(sum(weights[k] * from_record(lovelock[f"E{k}"][key]["input"])
                               for k in (1, 2, 3)))
            for key in ("x4x4", "x1x1", "x0x0")}  # sum_k alpha_k E_(k), H = 1
    ARGS = (ad1, uu, kk, a1, a2, a3)
    zero_second = {ad2: 0, vv: 0}
    e44 = sp.lambdify(ARGS, side["x4x4"], "numpy")  # the constraint, no a4'' or v
    rest1 = sp.lambdify(ARGS, side["x1x1"].subs(zero_second), "numpy")
    rest0 = sp.lambdify(ARGS, side["x0x0"].subs(zero_second), "numpy")
    J11 = sp.lambdify(ARGS, sp.diff(side["x1x1"], ad2), "numpy")
    J12 = sp.lambdify(ARGS, sp.diff(side["x1x1"], vv), "numpy")
    J21 = sp.lambdify(ARGS, sp.diff(side["x0x0"], ad2), "numpy")
    J22 = sp.lambdify(ARGS, sp.diff(side["x0x0"], vv), "numpy")
    linear = all(sp.diff(side[key], x, y) == 0 for key in ("x1x1", "x0x0")
                 for x in (ad2, vv) for y in (ad2, vv))
    say(f"the 3-space and hidden components are linear in (a4'', v): {linear}")
    EINSTEIN = (1.0, 0.0, 0.0)  # alpha1, alpha2, alpha3 of Einstein gravity
    AUTHOR = (1.0, 1.0 / 32.0, 1.0 / 1152.0)  # the author's weights, H = 1
    '''),
    md(r"""
    The next cell checks that for Einstein gravity these functions are what the record
    says, at five sample points $(a_4', u, k)$: $J = \begin{pmatrix}2 & -2\\ 0 &
    -3/2\end{pmatrix}$, $e_{44} = 3(a_4')^2 + 6k - \tfrac32u^2$,
    $R_1 = -5(a_4')^2 + 6a_4'u + 6k - \tfrac52u^2$ and
    $R_0 = -3(a_4')^2 + \tfrac32a_4'u + 3k - \tfrac32u^2$ (with $H = 1$).
    """),
    code(r'''
    points = np.array([[-2.0, 0.5, 1.0], [-0.5, 1.0, 0.3], [0.0, 2.0, 2.0],
                       [1.0, 4.0 / 3.0, 1.0], [3.0, -1.0, 5.0]])  # (a4', u, k)
    a_p, u_p, k_p = points.T
    ok = (np.allclose(J11(a_p, u_p, k_p, *EINSTEIN), 2.0)
          and np.allclose(J12(a_p, u_p, k_p, *EINSTEIN), -2.0)
          and np.allclose(J21(a_p, u_p, k_p, *EINSTEIN), 0.0)
          and np.allclose(J22(a_p, u_p, k_p, *EINSTEIN), -1.5)
          and np.allclose(e44(a_p, u_p, k_p, *EINSTEIN), 3 * a_p ** 2 + 6 * k_p
                          - 1.5 * u_p ** 2)
          and np.allclose(rest1(a_p, u_p, k_p, *EINSTEIN), -5 * a_p ** 2 + 6 * a_p * u_p
                          + 6 * k_p - 2.5 * u_p ** 2)
          and np.allclose(rest0(a_p, u_p, k_p, *EINSTEIN), -3 * a_p ** 2 + 1.5 * a_p * u_p
                          + 3 * k_p - 1.5 * u_p ** 2))
    reproduces(ok, "Einstein: J = {{2, -2}, {0, -3/2}} and the three components (H = 1)",
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
    function of the old and the new state; when it returns True the integration ends
    before the new state is accepted (used in section 13 to stop where $\det J$ changes
    sign). The test integrates $y' = -y$, $y(0) = 1$, from 0 to 1 with 20 steps; the
    exact value is $y(1) = e^{-1}$, and the RK4 error must be tiny (below $10^{-7}$).
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
            new = y + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
            if stop is not None and stop(y, new):
                break
            xs.append((n + 1) * h)  # (n + 1) h avoids adding up rounding errors
            ys.append(new)
        return np.array(xs), np.array(ys)


    x_test, y_test = rk4(lambda x, y: -y, [1.0], 0.05, 20)
    error_test = abs(y_test[-1, 0] - math.exp(-1.0))
    say(f"y' = -y: RK4 with h = 0.05 gives y(1) = {y_test[-1, 0]:.10f}; "
        f"exact {math.exp(-1.0):.10f}")
    check(error_test < 1e-7, "RK4 solves y' = -y to better than 1e-7 with 20 steps")
    '''),
    md(r"""
    ## 7. The system for a4 and b4

    The state is $y = (a_4, a_4', \ln b_4, u, \kappa\rho)$ and the right-hand side is

    $$\frac{d}{dx_4}a_4 = a_4',\quad \frac{d}{dx_4}\ln b_4 = u,\quad
    \begin{pmatrix}a_4''\\ v\end{pmatrix} = J^{-1}\begin{pmatrix}\kappa p_3 - \Lambda
    - R_1\\ \kappa p_0 - \Lambda - R_0\end{pmatrix},\quad
    \frac{d}{dx_4}(\kappa\rho) = -3a_4'\kappa(\rho + p_3) - 4h_4\kappa(\rho + p_0),$$

    with $k = e^{2a_4 - \ln b_4}$ and $h_4 = \tfrac12u - a_4'$. The last line is the
    conservation law; we integrate it alongside so that we can compare the energy
    density it gives with the one the constraint gives. The helper `history` builds
    the right-hand side for two pressure functions `p3(x, y)` and `p0(x, y)` (they may
    depend on the time and on the state) and the couplings, starts with $\kappa\rho$
    from the constraint, and integrates; `np.linalg.solve` solves the 2 by 2 system.
    The helper `constraint_gap` measures, along a solution, the difference between the
    integrated $\kappa\rho$ and $-(e_{44} + \Lambda)$.
    """),
    code(r'''
    def history(p3, p0, start, h, steps, couplings=EINSTEIN, Lam=0.0, stop=None):
        """Integrate (a4, a4', ln b4, u, kappa rho) for the prescribed pressures
        kappa p3(x, y), kappa p0(x, y), from start = (a4, a4', ln b4, u)."""
        def rhs(x, y):
            a4, rate, log_b4, u, kappa_rho = y
            k = math.exp(2.0 * a4 - log_b4)  # k = e^(2 a4)/b4
            jacobian = np.array([
                [J11(rate, u, k, *couplings), J12(rate, u, k, *couplings)],
                [J21(rate, u, k, *couplings), J22(rate, u, k, *couplings)]])
            pressure3, pressure0 = p3(x, y), p0(x, y)
            right = np.array([pressure3 - Lam - rest1(rate, u, k, *couplings),
                              pressure0 - Lam - rest0(rate, u, k, *couplings)])
            second, v = np.linalg.solve(jacobian, right)  # a4'' and v = u'
            h4 = u / 2.0 - rate
            change = (-3.0 * rate * (kappa_rho + pressure3)
                      - 4.0 * h4 * (kappa_rho + pressure0))  # the conservation law
            return np.array([rate, second, u, v, change])

        a4, rate, log_b4, u = start
        kappa_rho0 = -(e44(rate, u, math.exp(2.0 * a4 - log_b4), *couplings) + Lam)
        return rk4(rhs, [a4, rate, log_b4, u, kappa_rho0], h, steps, stop)


    def constraint_gap(ys, couplings=EINSTEIN, Lam=0.0):
        """The largest |kappa rho integrated + e44 + Lambda| along a solution."""
        k = np.exp(2.0 * ys[:, 0] - ys[:, 2])
        return float(np.max(np.abs(ys[:, 4] + e44(ys[:, 1], ys[:, 3], k, *couplings) + Lam)))


    def no_pressure(x, y):
        return 0.0  # a vacuum: p3 = p0 = 0
    '''),
    md(r"""
    ## 8. No source: the flat vacuum

    The record proves that the **flat member** $a_4 = 0$, $b_4 = H^2(x_4 - c)^2$ solves
    the vacuum equations of Einstein gravity with $\Lambda = 0$ (every curvature
    component vanishes). With $c = -1/H$ it starts at $a_4 = 0$, $a_4' = 0$,
    $b_4 = 1$, $u = 2H$; then $\kappa\rho(0) = -(3\cdot0 - \tfrac32\cdot4 + 6) = 0$, as a
    vacuum needs. The next cell integrates the vacuum equations from these starting
    values up to $x_4 = 3$ with $h = 0.01$ and compares with the exact
    $\ln b_4 = 2\ln(1 + x_4)$ and $u = 2/(1 + x_4)$.
    """),
    code(r'''
    x_flat, y_flat = history(no_pressure, no_pressure, (0.0, 0.0, 0.0, 2.0), 0.01, 300)
    error_log_b4 = np.max(np.abs(y_flat[:, 2] - 2.0 * np.log(1.0 + x_flat)))
    error_u = np.max(np.abs(y_flat[:, 3] - 2.0 / (1.0 + x_flat)))
    say(f"largest error: ln b4 {error_log_b4:.0e}, u {error_u:.0e}, a4 "
        f"{np.max(np.abs(y_flat[:, 0])):.0e}")
    reproduces(error_log_b4 < 1e-8 and error_u < 1e-8
               and np.max(np.abs(y_flat[:, 0])) < 1e-8 and np.max(np.abs(y_flat[:, 4])) == 0,
               "the flat member a4 = 0, b4 = (1 + x4)^2 solves the vacuum equations",
               PY, "einstein_flat_vacuum")
    check(constraint_gap(y_flat) < 1e-8, "flat member: the constraint holds along x4")
    '''),
    md(r"""
    The next cell draws the flat member: the numerical $b_4^{1/2}$ against the exact
    $1 + x_4$, and the rate $u$ against $2/(1 + x_4)$. The scale factor of the hidden
    direction and the extra times, $e^{-a_4}b_4^{1/2} = 1 + x_4$, grows linearly while
    3-space stays still ($a_4 = 0$): 8-dimensional flat space in Milne form, not a
    deflating history.
    """),
    code(r'''
    fig, (left, right) = plt.subplots(1, 2, figsize=(11.0, 4.2))
    every = slice(0, None, 20)  # every 20th point for the numerical markers
    left.plot(x_flat, 1.0 + x_flat, color="black", label="exact $1 + x_4$")
    left.plot(x_flat[every], np.exp(y_flat[every, 2] / 2.0), "o", markersize=4,
              label="RK4: $b_4^{1/2}$")
    left.plot(x_flat, np.exp(y_flat[:, 0]), "--", label="3-space $e^{a_4} = 1$")
    left.set_xlabel("time $x_4$ (units $1/H$)")
    left.set_ylabel("scale factor")
    left.set_title("the block grows linearly, 3-space is still")
    left.legend(fontsize=8)
    right.plot(x_flat, 2.0 / (1.0 + x_flat), color="black", label="exact $2/(1 + x_4)$")
    right.plot(x_flat[every], y_flat[every, 3], "o", markersize=4, label="RK4: $u$")
    right.set_xlabel("time $x_4$ (units $1/H$)")
    right.set_ylabel("$u = b_4'/b_4$ (units $H$)")
    right.set_title("the rate $u$")
    right.legend(fontsize=8)
    save_figure(fig, "flat_member",
                "Einstein gravity without a source: the flat member $a_4 = 0$, "
                "$b_4 = H^2(x_4 + 1/H)^2$, integrated from $a_4 = a_4' = 0$, $b_4 = 1$, "
                "$u = 2H$ with RK4 (step $h = 0.01/H$, dots) and the exact solution "
                "(black lines), against the time $x_4$ in units of $1/H$. Left: the "
                "scale factor $e^{-a_4}b_4^{1/2} = 1 + Hx_4$ of the hidden direction and "
                "the extra times grows linearly while the 3-space factor $e^{a_4}$ stays "
                "1 (dashed): 8-dimensional flat space in Milne form. Right: the rate "
                "$u = b_4'/b_4 = 2/(1 + Hx_4)$ in units of $H$.")
    '''),
    md(r"""
    ## 9. The record history with its own source

    The record history $a_4 = x_4$, $b_4 = e^{(4/3)x_4}$ needs the source of the record
    (`exponentialHistory`): in Einstein gravity with $\Lambda = 0$,
    $\kappa p_3 = 6k - \tfrac{13}9$ and $\kappa p_0 = 3k - \tfrac{11}3$, and with the
    author's weights $\kappa p_3 - \Lambda = -\tfrac9{16}k^2 + \tfrac{1601}{216}k -
    \tfrac{5359}{3888}$ and $\kappa p_0 - \Lambda = \tfrac{79}{16}k - \tfrac{497}{144}$
    with $\Lambda = -10$, where $k = e^{2x_4/3}$ on the history. The next cell
    prescribes these pressures as functions of the time, starts on the history
    ($a_4 = 0$, $a_4' = 1$, $b_4 = 1$, $u = 4/3$) and integrates to $x_4 = 3$: the
    solver must reproduce the history, and the energy density from the conservation
    law must equal the one the constraint gives (the Bianchi identity).
    """),
    code(r'''
    def einstein_p3(x, y):
        return 6.0 * math.exp(2.0 * x / 3.0) - 13.0 / 9.0  # kappa p3, Lambda = 0


    def einstein_p0(x, y):
        return 3.0 * math.exp(2.0 * x / 3.0) - 11.0 / 3.0  # kappa p0 = kappa p_t


    AUTHOR_LAMBDA = -10.0  # the record's Lambda for the author's weights


    def author_p3(x, y):
        k = math.exp(2.0 * x / 3.0)
        return -9.0 / 16.0 * k ** 2 + 1601.0 / 216.0 * k - 5359.0 / 3888.0 + AUTHOR_LAMBDA


    def author_p0(x, y):
        k = math.exp(2.0 * x / 3.0)
        return 79.0 / 16.0 * k - 497.0 / 144.0 + AUTHOR_LAMBDA


    START = (0.0, 1.0, 0.0, 4.0 / 3.0)  # a4, a4', ln b4, u of the record history
    record_runs = {"Einstein": history(einstein_p3, einstein_p0, START, 0.01, 300),
                   "author's weights": history(author_p3, author_p0, START, 0.01, 300,
                                               AUTHOR, AUTHOR_LAMBDA)}
    gaps = []
    for name, (xs, ys) in record_runs.items():
        couplings, Lam = (EINSTEIN, 0.0) if name == "Einstein" else (AUTHOR, AUTHOR_LAMBDA)
        error_a4 = np.max(np.abs(ys[:, 0] - xs))  # exact a4 = x4
        error_log_b4 = np.max(np.abs(ys[:, 2] - 4.0 * xs / 3.0))  # exact ln b4 = 4 x4/3
        gaps.append(constraint_gap(ys, couplings, Lam))
        say(f"{name}: largest error a4 {error_a4:.0e}, ln b4 {error_log_b4:.0e}; "
            f"constraint gap {gaps[-1]:.0e}")
        check(error_a4 < 1e-9 and error_log_b4 < 1e-9,
              f"{name}: the solver reproduces the record history")
    reproduces(max(gaps) < 1e-8,
               "the energy density from conservation equals the constraint along x4",
               WL, "constraint_propagation_bianchi")
    '''),
    md(r"""
    The next cell draws the two integrations against the exact history: $a_4$ and
    $\ln b_4$ (left; numerical dots on the exact lines), and on a logarithmic axis the
    scale factor $e^{a_4} = e^{x_4}$ of 3-space and $e^{-a_4}b_4^{1/2} = e^{-x_4/3}$ of
    the hidden direction and the extra times (right): 3-space inflates while the block
    deflates exponentially.
    """),
    code(r'''
    fig, (left, right) = plt.subplots(1, 2, figsize=(11.0, 4.2))
    xs = record_runs["Einstein"][0]
    left.plot(xs, xs, color="black", label="exact $a_4 = x_4$")
    left.plot(xs, 4.0 * xs / 3.0, color="grey", label="exact $\\ln b_4 = 4x_4/3$")
    for (name, (x_run, y_run)), marker in zip(record_runs.items(), ("o", "s")):
        left.plot(x_run[every], y_run[every, 0], marker, markersize=4, fillstyle="none",
                  label=f"$a_4$, {name}")
        left.plot(x_run[every], y_run[every, 2], marker, markersize=4,
                  label=f"$\\ln b_4$, {name}")
    left.set_xlabel("time $x_4$ (units $1/H$)")
    left.set_ylabel("$a_4$ and $\\ln b_4$")
    left.set_title("RK4 reproduces the record history")
    left.legend(fontsize=7)
    x_run, y_run = record_runs["author's weights"]
    right.semilogy(x_run, np.exp(y_run[:, 0]), label="3-space $e^{a_4}$ (inflates)")
    right.semilogy(x_run, np.exp(-y_run[:, 0] + y_run[:, 2] / 2.0), "--",
                   label="block $e^{-a_4}b_4^{1/2}$ (deflates)")
    right.set_xlabel("time $x_4$ (units $1/H$)")
    right.set_ylabel("scale factor")
    right.set_title("the scale factors (author's weights)")
    right.legend(fontsize=8)
    save_figure(fig, "record_history",
                "The record history $a_4 = Hx_4$, $b_4 = e^{(4/3)Hx_4}$ integrated with "
                "RK4 (step $h = 0.01/H$) from its own prescribed source, in Einstein "
                "gravity ($\\Lambda = 0$, circles) and with the author's weights "
                "($\\Lambda = -10$, squares), against the time $x_4$ in units of $1/H$. "
                "Left: $a_4$ (open markers) and $\\ln b_4$ (filled markers) on the exact "
                "lines $x_4$ and $4x_4/3$. Right, on a logarithmic axis: the scale factor "
                "$e^{a_4}$ of 3-space inflates as $e^{Hx_4}$ and the factor "
                "$e^{-a_4}b_4^{1/2}$ of the hidden direction and the extra times "
                "deflates as $e^{-Hx_4/3}$.")
    '''),
    md(r"""
    ## 10. The same source, other starting rates

    The source of the record history does not force the record history. With the same
    prescribed pressures, the next cell starts with $a_4'(0) = 1.05$ and $0.95$
    (and $u(0) = 4/3$, $b_4(0) = 1$; the constraint gives a different $\kappa\rho(0)$),
    integrates to $x_4 = 3$ in both theories, and follows the differences
    $a_4' - 1$ and $u - \tfrac43$ from the record history. The constraint still holds
    along every one of these solutions; they are other histories with the same
    pressures, and the differences do not die out.
    """),
    code(r'''
    perturbed = {}  # (theory, starting rate) -> (x4, solution)
    for name, (p3, p0, couplings, Lam) in {
            "Einstein": (einstein_p3, einstein_p0, EINSTEIN, 0.0),
            "author's weights": (author_p3, author_p0, AUTHOR, AUTHOR_LAMBDA)}.items():
        for rate0 in (1.05, 0.95):
            xs, ys = history(p3, p0, (0.0, rate0, 0.0, 4.0 / 3.0), 0.01, 300, couplings, Lam)
            perturbed[(name, rate0)] = (xs, ys)
            check(constraint_gap(ys, couplings, Lam) < 1e-7,
                  f"{name}, a4'(0) = {rate0}: the constraint holds along the solution")
            say(f"{name}, a4'(0) = {rate0}: at x4 = 3, a4' - 1 = {ys[-1, 1] - 1:+.4f}, "
                f"u - 4/3 = {ys[-1, 3] - 4 / 3:+.4f}")
    '''),
    md(r"""
    The next cell draws the differences $a_4' - 1$ (solid) and $u - \tfrac43$ (dashed)
    for the four solutions, Einstein gravity on the left and the author's weights on
    the right.
    """),
    code(r'''
    fig, (left, right) = plt.subplots(1, 2, figsize=(11.0, 4.2))
    for ax, name in ((left, "Einstein"), (right, "author's weights")):
        for rate0, colour in ((1.05, "tab:blue"), (0.95, "tab:orange")):
            xs, ys = perturbed[(name, rate0)]
            ax.plot(xs, ys[:, 1] - 1.0, color=colour,
                    label=f"$a_4' - 1$, $a_4'(0) = {rate0}$")
            ax.plot(xs, ys[:, 3] - 4.0 / 3.0, "--", color=colour,
                    label=f"$u - 4/3$, $a_4'(0) = {rate0}$")
        ax.axhline(0.0, color="black", linewidth=0.8)
        ax.set_xlabel("time $x_4$ (units $1/H$)")
        ax.set_ylabel("difference from the record history (units $H$)")
        ax.set_title(name)
        ax.legend(fontsize=7)
    save_figure(fig, "starting_rate",
                "The source of the record history used with other starting rates: the "
                "differences $a_4' - H$ (solid) and $u - 4H/3$ (dashed) from the record "
                "history for the starting rates $a_4'(0) = 1.05H$ (blue) and $0.95H$ "
                "(orange), with $u(0) = 4H/3$ and $b_4(0) = 1$, against the time $x_4$ "
                "in units of $1/H$; left Einstein gravity, right the author's weights. "
                "The differences do not die out: the prescribed source does not select "
                "the record history, the starting values do.")
    '''),
    md(r"""
    ## 11. A pulse in the rate: from the history to the source and back

    The equations can also be used the other way round: choose a history, compute the
    source it needs, then integrate that source and get the history back. We choose a
    history whose rate rises in a pulse around $x_c = 3$ with width $w = 0.5$:

    $$a_4' = 1 + \tfrac12\Big(\operatorname{erf}\frac{x_4 - x_c}{w}
    + \operatorname{erf}\frac{x_c}{w}\Big),\qquad b_4 = e^{(4/3)a_4},$$

    so $u = \tfrac43a_4'$, $v = \tfrac43a_4''$ and $k = e^{(2/3)a_4}$ (erf is the
    *error function*; it rises from $-1$ to $1$). The rate rises from 1 to almost
    exactly 2: before the pulse the history is the record history, after it the
    exponential history with $A = 2$, $\beta = 4/3$, and the block deflates at every
    time, faster after the pulse. With
    $\int\operatorname{erf}(s)\,ds = s\operatorname{erf}(s) + e^{-s^2}/\sqrt\pi$ the
    function $a_4$ itself is known exactly. The next cell computes the Einstein source
    of this history ($\Lambda = 0$) from the record's components, prescribes it as a
    function of the time, integrates from the starting values of the history up to
    $x_4 = 8$ with $h = 0.01$, and compares.
    """),
    code(r'''
    X_C, WIDTH = 3.0, 0.5  # the centre and the width of the pulse
    einstein_side = {key: sp.lambdify((ad1, ad2, uu, vv, kk),
                                      side[key].subs({a1: 1, a2: 0, a3: 0}), "numpy")
                     for key in ("x4x4", "x1x1", "x0x0")}


    def pulse_history(x):
        """The exact a4, a4' and a4'' of the pulse history (a4(0) = 0, a4'(0) = 1)."""
        t, t0 = (x - X_C) / WIDTH, -X_C / WIDTH  # the argument now and at x4 = 0

        def antiderivative(s):  # an antiderivative of erf
            return s * math.erf(s) + math.exp(-s * s) / math.sqrt(math.pi)

        rate = 1.0 + 0.5 * (math.erf(t) + math.erf(X_C / WIDTH))
        second = math.exp(-t * t) / (WIDTH * math.sqrt(math.pi))  # the derivative
        a4 = x + 0.5 * (WIDTH * (antiderivative(t) - antiderivative(t0))
                        + x * math.erf(X_C / WIDTH))
        return a4, rate, second


    def pulse_source(x):
        """kappa rho, kappa p3 and kappa p0 that the pulse history needs (Einstein)."""
        a4, rate, second = pulse_history(x)
        values = (rate, second, 4.0 * rate / 3.0, 4.0 * second / 3.0,
                  math.exp(2.0 * a4 / 3.0))
        return (-einstein_side["x4x4"](*values), einstein_side["x1x1"](*values),
                einstein_side["x0x0"](*values))


    x_pulse, y_pulse = history(lambda x, y: pulse_source(x)[1],
                               lambda x, y: pulse_source(x)[2],
                               (0.0, 1.0, 0.0, 4.0 / 3.0), 0.01, 800)
    exact = np.array([pulse_history(x) for x in x_pulse])  # columns: a4, a4', a4''
    needed_rho = np.array([pulse_source(x)[0] for x in x_pulse])
    error_a4 = np.max(np.abs(y_pulse[:, 0] - exact[:, 0]))
    error_rate = np.max(np.abs(y_pulse[:, 1] - exact[:, 1]))
    error_rho = np.max(np.abs(y_pulse[:, 4] - needed_rho) / np.abs(needed_rho))
    say(f"largest error: a4 {error_a4:.0e}, a4' {error_rate:.0e}, ln b4 "
        f"{np.max(np.abs(y_pulse[:, 2] - 4.0 * exact[:, 0] / 3.0)):.0e}; relative error "
        f"of kappa rho {error_rho:.0e}")
    check(error_a4 < 1e-8 and error_rate < 1e-6 and error_rho < 1e-8,
          "pulse: RK4 (h = 0.01) gets the history back from its source")
    report("rate a4'/H after the pulse (x4 = 8)", f"{y_pulse[-1, 1]:.8f}")
    check(abs(y_pulse[-1, 1] - 2.0) < 1e-6 and np.min(y_pulse[:, 1]) > 1.0 - 1e-6,
          "after the pulse a4' = 2 H; the rate never falls below H")
    '''),
    md(r"""
    The next cell draws the pulse history: the rates $a_4'$ and $u = \tfrac43a_4'$
    (numerical lines and exact points) and, on a logarithmic axis, the scale factors
    $e^{a_4}$ of 3-space and $e^{-a_4}b_4^{1/2} = e^{-a_4/3}$ of the block.
    """),
    code(r'''
    fig, (left, right) = plt.subplots(1, 2, figsize=(11.0, 4.2))
    marks = slice(0, None, 40)  # every 40th point for the exact markers
    left.plot(x_pulse, y_pulse[:, 1], label="RK4: $a_4'$")
    left.plot(x_pulse, y_pulse[:, 3], label="RK4: $u$")
    left.plot(x_pulse[marks], exact[marks, 1], "o", color="black", markersize=3,
              label="exact")
    left.plot(x_pulse[marks], 4.0 * exact[marks, 1] / 3.0, "o", color="black",
              markersize=3)
    left.set_xlabel("time $x_4$ (units $1/H$)")
    left.set_ylabel("rate (units $H$)")
    left.set_title("the rates rise in the pulse")
    left.legend(fontsize=8)
    right.semilogy(x_pulse, np.exp(y_pulse[:, 0]), label="3-space $e^{a_4}$")
    right.semilogy(x_pulse, np.exp(-y_pulse[:, 0] + y_pulse[:, 2] / 2.0), "--",
                   label="block $e^{-a_4}b_4^{1/2}$")
    right.set_xlabel("time $x_4$ (units $1/H$)")
    right.set_ylabel("scale factor")
    right.set_title("the scale factors")
    right.legend(fontsize=8)
    save_figure(fig, "pulse_history",
                "A history whose rate rises in a pulse, recovered by RK4 (step "
                "$h = 0.01/H$) from the Einstein source it needs ($\\Lambda = 0$). Left: "
                "the rates $a_4'$ and $u = 4a_4'/3$ in units of $H$, numerical lines and "
                "exact points, rising from $H$ and $4H/3$ to $2H$ and $8H/3$ around "
                "$x_4 = 3/H$. Right, on a logarithmic axis: the scale factor $e^{a_4}$ of "
                "3-space inflates and the factor $e^{-a_4}b_4^{1/2} = e^{-a_4/3}$ of the "
                "hidden direction and the extra times deflates at every time, twice as "
                "fast after the pulse. Horizontal axes: the time $x_4$ in units of "
                "$1/H$.")
    '''),
    md(r"""
    The next cell draws the source that the pulse history needs, divided by
    $k = e^{(2/3)a_4}$ (the source grows like $k$, which hides the pulse). Before the
    pulse it is the source of the record history,
    $\kappa(\rho, p_3, p_0) = (-6k - \tfrac13,\ 6k - \tfrac{13}9,\ 3k - \tfrac{11}3)$;
    after it that of the exponential history with $A = 2$, $\beta = \tfrac43$, whose
    constant terms are four times larger,
    $(-6k - \tfrac43,\ 6k - \tfrac{52}9,\ 3k - \tfrac{44}3)$ (the Einstein source of
    section 7 of Notebook 12b with $A^2 = 4$). The cell checks both ends against these
    formulas. Divided by $k$, all three approach $-6$, $6$ and $3$ as $k$ grows; during
    the pulse the 3-space and the block pressures move apart.
    """),
    code(r'''
    sources = np.array([pulse_source(x) for x in x_pulse])  # kappa rho, p3, p0
    k_pulse = np.exp(2.0 * exact[:, 0] / 3.0)
    scaled = sources / k_pulse[:, None]
    say("kappa (rho, p3, p0)/k at x4 = 0: " + ", ".join(f"{v:.4f}" for v in scaled[0])
        + "; at x4 = 8: " + ", ".join(f"{v:.4f}" for v in scaled[-1]))
    k0, k8 = k_pulse[0], k_pulse[-1]
    before = np.array([-6 * k0 - 1 / 3, 6 * k0 - 13 / 9, 3 * k0 - 11 / 3])  # A = 1
    after = np.array([-6 * k8 - 4 / 3, 6 * k8 - 52 / 9, 3 * k8 - 44 / 3])  # A = 2
    check(np.allclose(sources[0], before, rtol=1e-12, atol=1e-12)
          and np.allclose(sources[-1], after, rtol=1e-9, atol=0.0),
          "before the pulse the source of A = 1, after it the source of A = 2")
    fig, ax = plt.subplots()
    for column, style, label in ((0, "-", "$\\kappa\\rho/k$"), (1, "--", "$\\kappa p_3/k$"),
                                 (2, ":", "$\\kappa p_0/k = \\kappa p_t/k$")):
        ax.plot(x_pulse, scaled[:, column], style, label=label)
    ax.axhline(0.0, color="black", linewidth=0.8)
    ax.set_xlabel("time $x_4$ (units $1/H$)")
    ax.set_ylabel("required source divided by $k$ (units $H^2$)")
    ax.set_title("The Einstein source of the pulse history")
    ax.legend(fontsize=8)
    save_figure(fig, "pulse_source",
                "The source that the pulse history needs in Einstein gravity with "
                "$\\Lambda = 0$, divided by $k = e^{2a_4}/b_4 = e^{(2/3)a_4}$ (the source "
                "grows like $k$): the energy density $\\kappa\\rho/k$ (solid), the 3-space "
                "pressure $\\kappa p_3/k$ (dashed) and the common pressure "
                "$\\kappa p_0/k = \\kappa p_t/k$ (dotted), in units of $H^2$, against the "
                "time $x_4$ in units of $1/H$. Before the pulse it is the source of the "
                "record history, after it that of the exponential history with $A = 2$; "
                "as $k$ grows all three approach $-6$, $6$ and $3$. During the pulse the "
                "rates change and the pressures move apart: the source that makes the "
                "block deflate faster.")
    '''),
    md(r"""
    ## 12. How fast does RK4 converge?

    The flat member is a good test: its right-hand side depends on the state itself
    (the hidden equation gives $v = -\tfrac23(3k - \tfrac32u^2)$ with $k = 1/b_4$), so
    it is a genuine nonlinear system, and the exact solution is known. The next cell
    integrates it up to $x_4 = 3$ with the step sizes $h = 0.2, 0.1, 0.05, 0.025,
    0.0125$ and measures the error of $\ln b_4(3)$ against the exact value
    $2\ln 4$. If the error behaves like $Ch^4$, halving $h$ divides it by $2^4 = 16$,
    and the measured order $\log_2(e_h / e_{h/2})$ is close to 4. The table prints
    each step, its error and the order; the plot shows the errors on logarithmic axes,
    where $Ch^4$ is a straight line of slope 4.
    """),
    code(r'''
    steps_list = [15, 30, 60, 120, 240]  # h = 3/steps = 0.2, 0.1, 0.05, 0.025, 0.0125
    sizes, errors = [], []
    for steps in steps_list:
        xs, ys = history(no_pressure, no_pressure, (0.0, 0.0, 0.0, 2.0), 3.0 / steps, steps)
        sizes.append(3.0 / steps)
        errors.append(abs(ys[-1, 2] - 2.0 * math.log(4.0)))
    orders = [math.log2(errors[i] / errors[i + 1]) for i in range(len(errors) - 1)]
    for i, (size, error) in enumerate(zip(sizes, errors)):
        order = f"{orders[i - 1]:.2f}" if i > 0 else "-"
        say(f"h = {size:<7} error of ln b4(3) = {error:.2e}   measured order {order}")
    check(all(3.7 < q < 4.5 for q in orders),
          "RK4 converges with order 4 (measured orders between 3.7 and 4.5)")
    fig, ax = plt.subplots()
    ax.loglog(sizes, errors, "o-", label="error of $\\ln b_4(3)$")
    reference = errors[-1] * (np.array(sizes) / sizes[-1]) ** 4
    ax.loglog(sizes, reference, "--", color="black", label="slope 4: $C h^4$")
    ax.set_xticks(sizes)  # one tick at each step size used
    ax.set_xticklabels([f"{size:g}" for size in sizes])
    ax.xaxis.set_minor_formatter(matplotlib.ticker.NullFormatter())  # no extra labels
    ax.set_xlabel("step size $h$ (units $1/H$)")
    ax.set_ylabel("absolute error")
    ax.set_title("RK4 on the flat member: fourth-order convergence")
    ax.legend(fontsize=8)
    save_figure(fig, "rk4_convergence",
                "The error of the RK4 value of $\\ln b_4$ at $x_4 = 3/H$ for the flat "
                "member (exact value $2\\ln 4$), for the step sizes $h = 0.2$, $0.1$, "
                "$0.05$, $0.025$ and $0.0125$ (units $1/H$), on logarithmic axes. The "
                "points follow the dashed reference line $Ch^4$ of slope 4: halving the "
                "step divides the error by about 16, the fourth-order convergence of the "
                "Runge-Kutta method.")
    '''),
    md(r"""
    ## 13. A gas of massless particles with the author's weights: the system breaks down

    Now a source that depends on the state: a gas of massless particles that move in
    3-space only, with $p_3 = \rho/3$ and $p_0 = p_t = 0$. Its conservation law reads
    $\partial_4\rho = -3a_4'\cdot\tfrac43\rho - 4(\tfrac12u - a_4')\rho = -2u\rho$, so
    $\rho = \sigma_0b_4^{-2}$ for every history: it conserves energy automatically. It
    is the source that the record calls the $x_0$-averaged free fold-band gas of the
    Kohn-Sham states (Chapter 17 explains where it comes from). With the author's
    weights ($\Lambda = -10$) and the starting values of the record history, the
    constraint fixes $\kappa\sigma_0 = -(e_{44}(1, \tfrac43, 1) + \Lambda)$. The next
    cell integrates with the small step $h = 2\times10^{-5}$ and stops where $\det J$
    changes sign: there $a_4''$ and $v$ grow without bound and the system has no
    smooth continuation. The record finds this point at $x_4 = 0.428813$; the cell
    compares $x_4$, $a_4$ and $b_4$ there with the record (the rates change fast near
    the point, so they are printed but compared only loosely).
    """),
    code(r'''
    import re  # regular expressions: find numbers in a text


    def determinant(rate, u, k, couplings):
        """det J of the two equations of second order."""
        return (J11(rate, u, k, *couplings) * J22(rate, u, k, *couplings)
                - J12(rate, u, k, *couplings) * J21(rate, u, k, *couplings))


    sigma0 = -(e44(1.0, 4.0 / 3.0, 1.0, *AUTHOR) + AUTHOR_LAMBDA)  # kappa rho(0)
    report("kappa sigma0 from the constraint", f"{sigma0:.6g}")


    def gas_p3(x, y):
        return sigma0 * math.exp(-2.0 * y[2]) / 3.0  # kappa p3 = kappa rho/3


    def sign_change(old, new):
        """True where det J changes sign between two states (the breakdown)."""
        dets = [determinant(s[1], s[3], math.exp(2.0 * s[0] - s[2]), AUTHOR)
                for s in (old, new)]
        return dets[0] * dets[1] <= 0.0


    x_gas, y_gas = history(gas_p3, no_pressure, START, 2e-5, 30000, AUTHOR, AUTHOR_LAMBDA,
                           stop=sign_change)
    end = y_gas[-1]
    say(f"det J changes sign after x4 = {x_gas[-1]:.6f}: a4 = {end[0]:.6f}, "
        f"b4 = {math.exp(end[2]):.6f}, a4' = {end[1]:.4f}, u = {end[3]:.4f}")
    check(np.max(np.abs(y_gas[:, 4] - sigma0 * np.exp(-2.0 * y_gas[:, 2]))
                 / (sigma0 * np.exp(-2.0 * y_gas[:, 2]))) < 1e-10,
          "the gas conserves its energy: kappa rho = kappa sigma0 b4^(-2) along x4")
    text = [entry["detail"] for entry in read_json(KS_A4)["checks"]
            if entry["name"] == "D2_author_weights_from_the_record_history"][0]
    numbers = re.search(r"singular_second_order_system at x4 = (\S+) \(a4 = (\S+?), "
                        r"b4 = (\S+?), a4'/H = (\S+?), u/H = (\S+?)\)", text)
    recorded = [float(value) for value in numbers.groups()]
    say("record: x4 = {}, a4 = {}, b4 = {}, a4' = {}, u = {}".format(*numbers.groups()))
    reproduces(f"{sigma0:.6g}" in text and abs(x_gas[-1] - recorded[0]) < 1e-3
               and abs(end[0] - recorded[1]) < 1e-3
               and abs(math.exp(end[2]) - recorded[2]) < 1e-3
               and abs(end[1] - recorded[3]) < 0.05 and abs(end[3] - recorded[4]) < 0.05,
               "the system becomes singular where the record finds it",
               KS_A4, "D2_author_weights_from_the_record_history")
    '''),
    md(r"""
    The next cell draws the solution with the gas up to the breakdown: the rates
    $a_4'$ and $u$ (left), which leave the values $1$ and $\tfrac43$ of the record
    history, and $\det J$ (right), which approaches zero.
    """),
    code(r'''
    fig, (left, right) = plt.subplots(1, 2, figsize=(11.0, 4.2))
    left.plot(x_gas, y_gas[:, 1], label="$a_4'$ with the gas")
    left.plot(x_gas, y_gas[:, 3], "--", label="$u$ with the gas")
    left.axhline(1.0, color="black", linestyle=":", linewidth=0.8,
                 label="record history: $a_4' = 1$, $u = 4/3$")
    left.axhline(4.0 / 3.0, color="black", linestyle=":", linewidth=0.8)
    left.set_xlabel("time $x_4$ (units $1/H$)")
    left.set_ylabel("rate (units $H$)")
    left.set_title("the rates leave the record history")
    left.legend(fontsize=8)
    k_gas = np.exp(2.0 * y_gas[:, 0] - y_gas[:, 2])
    right.plot(x_gas, determinant(y_gas[:, 1], y_gas[:, 3], k_gas, AUTHOR))
    right.axhline(0.0, color="black", linewidth=0.8)
    right.axvline(x_gas[-1], color="grey", linestyle="--", linewidth=0.8)
    right.set_xlabel("time $x_4$ (units $1/H$)")
    right.set_ylabel("$\\det J$")
    right.set_title("the Jacobian reaches zero")
    save_figure(fig, "gas_breakdown",
                "The author's weights ($\\Lambda = -10$) with a gas of massless particles "
                "in 3-space as the prescribed source ($p_3 = \\rho/3$, $p_0 = p_t = 0$, "
                "$\\kappa\\rho = 3.57407\\,b_4^{-2}$), started on the record history "
                "($a_4' = H$, $u = 4H/3$, $b_4 = 1$) and integrated with RK4 (step "
                "$2\\times10^{-5}/H$). Left: the rates $a_4'$ (solid) and $u$ (dashed) "
                "leave the record values (dotted); $u$ turns negative. Right: the "
                "determinant of the Jacobian of the two equations of second order falls "
                "to zero at $x_4 = 0.4288/H$ (dashed line), where the system has no "
                "smooth continuation, as the record found.")
    '''),
    md(r"""
    ## 14. Which sources are real? The record on the Kohn-Sham states

    The sources above were chosen by hand. The Revision record asks the opposite
    question for the only many-particle states it has computed, the Kohn-Sham states
    of dirac16complex: can they be the source of the corrected metric? Its answer is
    no: every nonzero state depends on $x_0$, the interacting states also violate
    $p_0 = p_t$, and no constant $\kappa$ makes them the source of the record history.
    The next cell reads the record, checks that every one of its checks passed, and
    recomputes three of its numbers from the table `emt-integrals.csv` of the
    Kohn-Sham record, which holds one row per recorded ground state: its name (for
    example `N592_lam0_a10`: $N = 592$ particles, coupling $\lambda = 0$, slice
    $a_{4,0} = 1$) and the integrals over the hidden direction of the energy density
    and of the three pressures (columns `int_rho`, `int_p3`, `int_p_t`, `int_p0`).

    - The number of states and of those whose four integrals are not all zero.
    - The ratios $p_3/\rho$, $p_0/\rho$, $p_t/\rho$ of each state, averaged over $x_0$
      per proper volume: the ratios of the integrals.
    - The ratios that the record history needs with the author's weights at the slice
      of the state ($k = e^{2a_{4,0}/3}$, $\Lambda = -10$; they do not depend on the
      unknown $\kappa$), and the smallest distance between the two sets of ratios.
    """),
    code(r'''
    import csv  # reads tables of comma-separated values

    ks = read_json(KS)
    detail = {entry["name"]: entry["detail"] for entry in ks["checks"]}
    verdicts = [entry["verdict"] for entry in ks["checks"]]
    say(f"{KS}: {verdicts.count('PASS')} of {len(verdicts)} checks PASS")
    check(len(verdicts) > 0 and verdicts.count("PASS") == len(verdicts)
          == ks["summary"]["checks"],
          "record: no Kohn-Sham state is an admissible source (every check PASS)")
    TABLE = "Revision/kohn_sham/results/ground/emt-integrals.csv"
    with repository_file(TABLE).open(encoding="utf-8", newline="") as handle:
        table = {row["id"]: row for row in csv.DictReader(handle)}
    INTEGRALS = ("int_rho", "int_p3", "int_p_t", "int_p0")
    zero = sorted(name for name, row in table.items()
                  if all(float(row[column]) == 0.0 for column in INTEGRALS))
    nonzero = [name for name in table if name not in zero]
    report("Kohn-Sham states in the table, with a nonzero tensor",
           f"{len(table)}, {len(nonzero)}")
    counted = re.search(r"(\d+) ground-state profiles .*?\((\d+) with a nonzero",
                        detail["ks_profiles_depend_on_x0"])
    listed = re.search(r"\(zero source\): (.*?) \(the",
                       detail["ks_zero_source_states_listed"]).group(1)
    reproduces(counted is not None and counted.groups() == (str(len(table)),
                                                            str(len(nonzero)))
               and sorted(listed.split(", ")) == zero,
               f"{len(nonzero)} of the {len(table)} states have a nonzero tensor",
               KS, "ks_zero_source_states_listed")
    kq = sp.symbols("kq", positive=True)
    shifted = record["exponentialHistory"]["authorWeights"]["historySource_kappaT_minus_Lam"]
    need = {key: sp.sympify(shifted[key]["input"].replace("^", "**"), locals={"kk": kq})
            for key in ("minus_rho", "p3", "p0", "pt")}
    kappa_rho = -(need["minus_rho"] + AUTHOR_LAMBDA)
    distance = {}
    for name in nonzero:
        row = table[name]
        if float(row["int_rho"]) == 0.0:
            continue
        k_value = math.exp(2.0 * float(row["a4"]) / 3.0)
        needed = [float(((need[key] + AUTHOR_LAMBDA) / kappa_rho).subs(kq, k_value))
                  for key in ("p3", "p0", "pt")]
        mine = [float(row[column]) / float(row["int_rho"])
                for column in ("int_p3", "int_p0", "int_p_t")]
        distance[name] = max(abs(a - b) for a, b in zip(mine, needed))
    closest = min(distance, key=distance.get)
    report("smallest distance of the ratios, and its state",
           f"{distance[closest]:.6g}, {closest}")
    reproduces(f"by at least {distance[closest]:.6g} (closest: {closest})"
               in detail["ks_history_is_a_prescribed_background"],
               "the ratios of every state differ from the needed ones, as recorded",
               KS, "ks_history_is_a_prescribed_background")
    '''),
    md(r"""
    ## 15. The last check

    The last cell checks that the seven figure files exist in the folder
    Revision/textbook/figures and prints the number of checks that passed.
    """),
    code(r'''
    figure_names = ["flat_member", "record_history", "starting_rate", "pulse_history",
                    "pulse_source", "rk4_convergence", "gas_breakdown"]
    paths = [output_file(f"{FIGURE_FOLDER}/12c_{k}_{name}.png")
             for k, name in enumerate(figure_names, 1)]
    check(all(path.is_file() for path in paths), "all seven figure files exist")
    all_checks_passed()
    '''),
    md(r"""
    ## 16. What this notebook showed

    - With prescribed pressures $p_3$ and $p_0 = p_t$ the two equations of second
      order are a system of ordinary differential equations for $a_4$ and $b_4$, which
      RK4 solves with fourth-order accuracy (COMPUTED, compared with exact solutions).
    - No source gives back the flat member $a_4 = 0$, $b_4 = (1 + Hx_4)^2$, and the
      source of the record history gives back the record history, in Einstein gravity
      and with the author's weights; the energy density from the conservation law
      equals the one the constraint gives along every solution (COMPUTED, as the
      record's Bianchi identity requires).
    - The same source with other starting rates gives other histories: the source
      does not select the history, the starting values do (COMPUTED).
    - From a chosen history (a pulse in the rate) the equations give its source, and
      integrating that source gives the history back (COMPUTED for an ASSUMED
      history).
    - A gas of massless particles in 3-space, started on the record history with the
      author's weights, drives the solution to a point where $\det J = 0$ at
      $x_4 = 0.4288/H$, where the system breaks down (COMPUTED, as in the record).
    - None of these sources is known to come from a field of the theory; the record
      shows that the Kohn-Sham states of the repository are not admissible sources,
      and the notebook recomputes the record's numbers from the Kohn-Sham table
      (COMPUTED from the record's table; equal to the record).
    """),
]

if __name__ == "__main__":
    raise SystemExit(run_builder(__file__))
