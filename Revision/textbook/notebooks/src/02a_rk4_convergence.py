#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
"""Builder of Notebook 02a, "Euler, midpoint and RK4" (textbook "Universes in Pairs").

The notebook Revision/textbook/notebooks/02a_rk4_convergence.ipynb is BUILT from this
file by Revision/textbook/tools/nbkit.py (never edit the .ipynb by hand):

    python Revision/textbook/tools/nbkit.py build \
        Revision/textbook/notebooks/src/02a_rk4_convergence.py --date YYYY-MM-DD
    python Revision/textbook/tools/nbkit.py check \
        Revision/textbook/notebooks/src/02a_rk4_convergence.py

Chapter 02, example a: the three one-step methods (Euler, midpoint, classical
fourth-order Runge-Kutta), their exact amplification factors, their convergence orders
1, 2, 4 measured as slopes on log-log plots, the rounding floor, the energy of an
oscillator, and Richardson's error estimate.  No Revision record is reproduced here:
every number is computed by the notebook itself and checked against exact formulas.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools"))
from nbkit import code, md, run_builder  # noqa: E402

FIGURES = [
    "02a_1_scale_factors",
    "02a_2_scale_factor_product",
    "02a_3_convergence_loglog",
    "02a_4_error_ratios",
    "02a_5_rounding_floor",
    "02a_6_phase_portrait",
    "02a_7_energy_drift",
    "02a_8_richardson",
]

FACTS = {
    "id": "02a",
    "name": "02a_rk4_convergence",
    "title": "Euler, midpoint and RK4: the order of a method on a log-log plot",
    "purpose": (
        "It solves two differential equations whose exact solutions are known, the "
        "decay equation (the deflation of an extra-time scale factor along a linear "
        "history) and the oscillator equation, with the Euler method, the midpoint "
        "method and the classical fourth-order Runge-Kutta method (RK4); it derives "
        "the exact amplification factor of each method with sympy, measures how the "
        "error at a fixed end time shrinks when the step is halved, finds the orders 1, "
        "2 and 4 as slopes on log-log plots, shows where rounding errors stop the "
        "improvement, predicts the energy drift of the oscillator exactly, and tests "
        "the Richardson estimate of the error."
    ),
    "records": [],
    "packages": ["numpy", "sympy", "matplotlib"],
    "needs_rust": [],
    "expected_seconds": 10,
    "timeout_seconds": 300,
    "files_written": ["Revision/textbook/figures/02a.captions.json"]
    + [f"Revision/textbook/figures/{name}.png" for name in FIGURES],
    "final_lines": [
        "PASS all 8 figure files of notebook 02a exist",
        "ALL 25 CHECKS PASSED (notebook 02a)",
    ],
    "troubleshooting": [],
}

CELLS = [
    md(r"""
    ## 1. What this notebook computes

    A differential equation says how fast a quantity changes. A computer solves it by
    taking many small *steps*. This notebook compares three ways of making one step,
    the **Euler method**, the **midpoint method** and the **classical fourth-order
    Runge-Kutta method (RK4)**, on two equations whose exact solutions we know, so
    that every error can be measured exactly. It

    - makes one step of each method by hand, with exact fractions;
    - derives with sympy the exact *amplification factor* of each method, the number
      by which one step multiplies the solution of $y' = \lambda y$;
    - solves the growth of the 3-space scale factor and the deflation of an
      extra-time scale factor of the author's metric along a linear history, and
      shows that Euler's method spoils their exact product $1$;
    - measures the error at a fixed end time for step sizes from $1/2$ down to
      $1/262144$, finds the *orders* $1$, $2$ and $4$ of the three methods as the
      slopes of straight lines on log-log plots, and shows where rounding errors stop
      the improvement;
    - solves the oscillator $d^2x/dt^2 = -x$, draws its phase portrait, and predicts the
      drift of its energy exactly from the amplification factors;
    - tests Richardson's rule, which estimates the error of a computation without
      knowing the exact answer.

    It draws 8 figures and prints a PASS line for every check.
    """),
    md(r"""
    ## 3. The words used in this notebook

    - **Derivative**: $y'(t) = dy/dt$ is the rate of change of $y$ at time $t$, the
      slope of the graph of $y$.
    - **Ordinary differential equation (ODE)**: an equation $y' = f(t, y)$ that gives
      the rate of change of an unknown function $y(t)$ from $t$ and $y$ itself. Here
      $f$ is a known rule, the *right-hand side*.
    - **Initial-value problem**: an ODE together with the starting value $y(0)$.
      Exactly one solution belongs to it (for the smooth $f$ of this notebook).
    - **System of ODEs**: several unknown functions changing together, for example
      a position $x$ and a velocity $v$; $y$ is then a list (a *vector*) of numbers.
    - **Step size** $h$: the time between two computed points; $N$ steps of size
      $h = T/N$ go from $t = 0$ to $t = T$.
    - **Euler, midpoint, RK4**: three rules that compute the value after one step
      from the value before it (the formulas are in section 4).
    - **Error**: the computed value minus the exact value (we print its size, the
      *absolute value*).
    - **Order** $p$: a method has order $p$ when its error at a fixed end time is
      close to $C h^p$ for small $h$, with a number $C$ that does not depend on $h$.
      Halving $h$ then divides the error by $2^p$.
    - **Logarithm, log-log plot**: $\log_{10} x$ is the power to which 10 must be
      raised to give $x$ ($\log_{10} 1000 = 3$). A log-log plot has both axes marked
      in powers of ten, so that $e = C h^p$ becomes the straight line
      $\log e = \log C + p \log h$ whose *slope* is $p$.
    - **Rounding error, machine epsilon**: a computer stores about 16 significant
      digits of a number; every operation rounds its result. The spacing of the
      stored numbers near 1 is the machine epsilon $2^{-52} \approx 2.2 \times
      10^{-16}$.
    - **Amplification factor** $R(z)$: for the test equation $y' = \lambda y$, one
      step of a method multiplies $y$ by a number $R(z)$ that depends only on
      $z = \lambda h$.
    - **Phase portrait**: the curve traced by the point $(x, v)$ (position,
      velocity) as time goes on.
    - **Richardson's rule**: an estimate of the error made from two computations with
      the step sizes $h$ and $h/2$.
    """),
    md(r"""
    ## 4. The physical and mathematical situation

    **The equations.** We solve two initial-value problems.

    *Problem A (decay and growth).* $y' = -y$ with $y(0) = 1$. The exact solution is
    $y(t) = e^{-t}$, because the derivative of $e^{-t}$ is $-e^{-t}$ and $e^{0} = 1$.
    This equation describes the extra times of the author's metric. Lengths along the
    three extra times $x_5, x_6, x_7$ carry the scale factor $e^{-a_4}\sin^{1/6}z$
    and lengths along 3-space $x_1, x_2, x_3$ the factor $e^{a_4}\sin^{1/6}z$, where
    $a_4(x_4)$ depends on the time $x_4$ and $z = 6 H x_8$ on the hidden coordinate.
    Along the linear history $a_4 = A H x_4$, which the book uses as a prescribed
    background (here $A = 1$ and $H = 1$, and $z$ is held fixed), the extra-time
    factor $b = e^{-x_4}$ obeys $db/dx_4 = -b$ (problem A with $t = x_4$: the extra
    times DEFLATE) and the 3-space factor $a = e^{x_4}$ obeys $da/dx_4 = +a$ (3-space
    inflates). Their product $a b = e^{x_4} e^{-x_4} = 1$ never changes.

    *Problem B (oscillation).* $d^2x/dt^2 = -x$ with $x(0) = 1$, $x'(0) = 0$. With the
    velocity $v = x'$ it becomes a system of two first-order equations, $x' = v$ and
    $v' = -x$. The exact solution is $x = \cos t$, $v = -\sin t$, and the energy
    $E = (x^2 + v^2)/2$ stays exactly $1/2$, because $\cos^2 t + \sin^2 t = 1$.

    **The three methods.** Write $y_n$ for the computed value at $t_n = n h$.

    - Euler: $y_{n+1} = y_n + h f(t_n, y_n)$. It follows the slope at the start of
      the step for the whole step.
    - Midpoint: $k_1 = f(t_n, y_n)$, $k_2 = f(t_n + h/2, y_n + (h/2) k_1)$,
      $y_{n+1} = y_n + h k_2$. It uses the slope at an estimated midpoint.
    - RK4: $k_1 = f(t_n, y_n)$, $k_2 = f(t_n + h/2, y_n + (h/2) k_1)$,
      $k_3 = f(t_n + h/2, y_n + (h/2) k_2)$, $k_4 = f(t_n + h, y_n + h k_3)$,
      $y_{n+1} = y_n + (h/6)(k_1 + 2 k_2 + 2 k_3 + k_4)$. It averages four slopes
      with the weights $1 : 2 : 2 : 1$.

    **Why Euler has order 1.** Taylor's theorem gives $y(t + h) = y(t) + h y'(t) +
    \frac{1}{2} h^2 y''(s)$ for some $s$ between $t$ and $t + h$. Euler keeps the
    first two terms, so one step makes an error of size about $\frac{1}{2} h^2
    |y''|$. To reach the end time $T$ we need $N = T/h$ steps; $N$ errors of size
    $h^2$ add up to about $N h^2 = T h$, proportional to $h^1$. The midpoint method
    has order 2 and RK4 order 4; the amplification factors below show why.

    **The amplification factor.** For $y' = \lambda y$ the exact solution after one
    step is $e^{\lambda h} y_n = e^{z} y_n$, and $e^{z} = 1 + z + z^2/2 + z^3/6 +
    z^4/24 + z^5/120 + \dots$ (the Taylor series of the exponential). We shall find
    that Euler keeps the first 2 terms of this series, the midpoint method the first
    3 and RK4 the first 5. The first term a method misses decides its order.
    """),
    md(r"""
    ## 5. The colours, the three step rules and the solver

    The next cell imports the packages, fixes the colours of the plots, and defines
    the three step rules exactly as written in section 4. The rules use only
    `+`, `-`, `*` and `/`, so the same function works with ordinary numbers, with
    exact fractions, with sympy symbols and with numpy vectors. The function `solve`
    makes $n$ equal steps from $t = 0$ to $t = T$.
    """),
    code(r'''
    import math  # exp, log10 and other functions of one number
    from fractions import Fraction  # exact fractions such as 233/384

    import numpy as np  # arrays (vectors) of numbers
    import sympy as sp  # exact algebra with symbols

    # One colour per method (a set that colour-blind readers can tell apart); every
    # method also has its own line style and marker, so the plots read in grey too.
    COLORS = {"euler": "#eb6834", "midpoint": "#1baf7a", "rk4": "#2a78d6",
              "exact": "#000000", "guide": "#8a8986"}
    MARKERS = {"euler": "s", "midpoint": "^", "rk4": "o"}
    LABELS = {"euler": "Euler", "midpoint": "midpoint", "rk4": "RK4"}


    def euler_step(f, t, y, h):
        """One Euler step: follow the slope at the start for the whole step."""
        return y + h * f(t, y)


    def midpoint_step(f, t, y, h):
        """One midpoint step: use the slope at the estimated middle of the step."""
        k1 = f(t, y)  # the slope at the start
        k2 = f(t + h / 2, y + (h / 2) * k1)  # the slope at the estimated midpoint
        return y + h * k2


    def rk4_step(f, t, y, h):
        """One step of the classical fourth-order Runge-Kutta method (RK4)."""
        k1 = f(t, y)  # the slope at the start
        k2 = f(t + h / 2, y + (h / 2) * k1)  # at the midpoint, reached with k1
        k3 = f(t + h / 2, y + (h / 2) * k2)  # at the midpoint again, reached with k2
        k4 = f(t + h, y + h * k3)  # at the end, reached with k3
        return y + (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4)  # weights 1 : 2 : 2 : 1


    METHODS = {"euler": euler_step, "midpoint": midpoint_step, "rk4": rk4_step}


    def solve(step, f, y0, t_end, n):
        """n equal steps of the rule step from t = 0 to t = t_end.  Returns the list
        of the n + 1 times and the list of the n + 1 computed values."""
        h = t_end / n  # the step size
        times, values = [0 * h], [y0]
        y = y0
        for i in range(n):
            y = step(f, i * h, y, h)  # t_i = i h (no rounding drift of the time)
            times.append((i + 1) * h)
            values.append(y)
        return times, values


    def decay(t, y):
        """Problem A: y' = -y (an extra-time scale factor along the linear history)."""
        return -y


    def growth(t, y):
        """y' = +y (the 3-space scale factor along the same history)."""
        return y


    say("Three step rules and the solver are defined.")
    '''),
    md(r"""
    ## 6. One step by hand, with exact fractions

    We make ONE step of size $h = 1/2$ from $y(0) = 1$ for problem A ($y' = -y$).
    With exact fractions the results are: Euler $1 - 1/2 = 1/2$; midpoint
    $k_1 = -1$, $k_2 = -(1 - 1/4) = -3/4$, so $1 - 3/8 = 5/8$; RK4
    $1 - 1/2 + 1/8 - 1/48 + 1/384 = 233/384$. The exact value is
    $e^{-1/2} = 0.6065306597\dots$. The cell lets Python's `Fraction` do the same
    arithmetic exactly and checks the three fractions.
    """),
    code(r'''
    h = Fraction(1, 2)  # the step size 1/2 as an exact fraction
    one_step = {name: step(decay, 0, Fraction(1), h) for name, step in METHODS.items()}
    for name, value in one_step.items():
        say(f"{LABELS[name]:9} after one step: {str(value):8} = {float(value):.10f}")
    say(f"exact     e^(-1/2)              = {math.exp(-0.5):.10f}")
    check(one_step["euler"] == Fraction(1, 2), "one Euler step of y' = -y gives 1/2")
    check(one_step["midpoint"] == Fraction(5, 8), "one midpoint step gives 5/8")
    check(one_step["rk4"] == Fraction(233, 384), "one RK4 step gives 233/384")
    '''),
    md(r"""
    ## 7. The exact amplification factors

    The next cell applies one step of each method to the test equation $y' = z y$
    with the step $h = 1$, starting from $y = 1$, where $z$ is a sympy symbol. The
    result is the amplification factor $R(z)$ as a polynomial in $z$. The checks
    compare it with the first terms of the Taylor series of $e^{z}$, which sympy
    computes with `sp.series`.

    The oscillator (problem B) is the same test equation in disguise. Put
    $w = x + i v$ with $i^2 = -1$. Then $w' = x' + i v' = v - i x = -i(x + i v) =
    -i w$: the test equation with $\lambda = -i$, so one step multiplies $w$ by
    $R(-ih)$. The energy is $E = (x^2 + v^2)/2 = |w|^2/2$, so one step multiplies
    it by $|R(-ih)|^2 = R(-ih) R(ih)$ (the second factor is the complex conjugate of
    the first, because the coefficients of $R$ are real numbers). The cell computes
    these three polynomials in $h$ as well; we use them in section 12.
    """),
    code(r'''
    z = sp.symbols("z")  # z = lambda h
    hs = sp.symbols("h", positive=True)  # a positive step size, as a symbol


    def linear(t, y):
        """The test equation y' = z y."""
        return z * y


    one = sp.Integer(1)  # sympy's exact 1 (so that 1/2 stays the exact fraction 1/2)
    R = {name: sp.expand(step(linear, 0, one, one)) for name, step in METHODS.items()}
    taylor = sp.series(sp.exp(z), z, 0, 6).removeO()  # 1 + z + ... + z^5/120
    terms = sp.Poly(taylor, z).all_coeffs()[::-1]  # the coefficients 1, 1, 1/2, ...
    for name, keep in (("euler", 2), ("midpoint", 3), ("rk4", 5)):
        partial = sum(terms[k] * z ** k for k in range(keep))  # the first keep terms
        say(f"R_{name}(z) = {sp.expand(R[name])}")
        check(sp.expand(R[name] - partial) == 0,
              f"R_{name}(z) equals the first {keep} terms of the series of e^z")

    # The energy factor of one oscillator step, R(i h) R(-i h), as a polynomial in h.
    ENERGY_FACTOR = {name: sp.expand(R[name].subs(z, sp.I * hs) *
                                     R[name].subs(z, -sp.I * hs))
                     for name in METHODS}
    for name, factor in ENERGY_FACTOR.items():
        say(f"energy factor per step, {LABELS[name]:8}: {factor}")
    check(ENERGY_FACTOR["euler"] == 1 + hs ** 2
          and ENERGY_FACTOR["midpoint"] == 1 + hs ** 4 / 4
          and ENERGY_FACTOR["rk4"] == 1 - hs ** 6 / 72 + hs ** 8 / 576,
          "energy factors 1 + h^2, 1 + h^4/4, 1 - h^6/72 + h^8/576")
    '''),
    md(r"""
    ## 8. The inflating and the deflating scale factor

    The next cell solves $da/dt = a$ (the 3-space factor $a = e^{t}$) and
    $db/dt = -b$ (the extra-time factor $b = e^{-t}$) from $t = 0$ to $t = 2$ with
    the coarse step $h = 0.25$ (8 steps), by Euler and by RK4, and draws them with
    the exact curves. Euler multiplies by $1 + h = 1.25$ and by $1 - h = 0.75$ per
    step, so after 8 steps it gives $1.25^8$ and $0.75^8$; the checks confirm this.
    """),
    code(r'''
    H_COARSE, STEPS = 0.25, 8  # step size and number of steps: t from 0 to 2
    curves = {}
    for name in ("euler", "rk4"):
        t_list, a_list = solve(METHODS[name], growth, 1.0, 2.0, STEPS)
        _, b_list = solve(METHODS[name], decay, 1.0, 2.0, STEPS)
        curves[name] = (np.array(t_list), np.array(a_list), np.array(b_list))
    t_fine = np.linspace(0.0, 2.0, 201)  # many points for the exact curves

    fig, (left, right) = plt.subplots(1, 2, figsize=(9.0, 3.8))
    left.plot(t_fine, np.exp(t_fine), color=COLORS["exact"], lw=1.0,
              label="exact $e^{t}$")
    right.plot(t_fine, np.exp(-t_fine), color=COLORS["exact"], lw=1.0,
               label="exact $e^{-t}$")
    for name in ("euler", "rk4"):
        t_n, a_n, b_n = curves[name]
        style = dict(color=COLORS[name], marker=MARKERS[name], ms=5, lw=1.2)
        left.plot(t_n, a_n, **style, label=f"{LABELS[name]}, $h = 0.25$")
        right.plot(t_n, b_n, **style, label=f"{LABELS[name]}, $h = 0.25$")
    left.set_title("3-space factor $a$: $da/dx_4 = +a$ (inflates)")
    right.set_title("extra-time factor $b$: $db/dx_4 = -b$ (deflates)")
    for ax in (left, right):
        ax.set_xlabel("time $x_4$ (units $1/H$, $A = 1$)")
        ax.legend(fontsize=8)
    left.set_ylabel("scale factor (pure number)")
    save_figure(fig, "scale_factors",
                "Left: the 3-space scale factor $a = e^{x_4}$, which obeys "
                "$da/dx_4 = a$; right: the extra-time scale factor $b = e^{-x_4}$, "
                "which obeys $db/dx_4 = -b$, along the linear history $a_4 = A H x_4$ "
                "with $A = H = 1$ at a fixed hidden position. Horizontal axis the time "
                "$x_4$ in units of $1/H$, vertical axis the scale factor (a pure "
                "number). Black: the exact curves; squares: Euler with the step "
                "$h = 0.25$; circles: RK4 with the same step. Euler falls behind the "
                "growing curve and decays too fast; RK4 lies on both exact curves.")
    a_euler, b_euler = curves["euler"][1][-1], curves["euler"][2][-1]
    a_rk4, b_rk4 = curves["rk4"][1][-1], curves["rk4"][2][-1]
    report("a(2): exact, Euler, RK4", f"{math.exp(2):.6f}, {a_euler:.6f}, {a_rk4:.6f}")
    report("b(2): exact, Euler, RK4", f"{math.exp(-2):.6f}, {b_euler:.6f}, {b_rk4:.6f}")
    check(abs(a_euler - 1.25 ** 8) < 1e-12 and abs(b_euler - 0.75 ** 8) < 1e-15,
          "Euler gives exactly 1.25^8 and 0.75^8 after 8 steps")
    check(abs(a_rk4 / math.exp(2) - 1) < 1e-3 and abs(b_rk4 / math.exp(-2) - 1) < 1e-3,
          "RK4 with h = 0.25 is within 0.1 percent of e^2 and e^(-2)")
    '''),
    md(r"""
    The exact product $a b = e^{t} e^{-t}$ is $1$ at every time: the inflation of a
    3-space direction is compensated exactly by the deflation of an extra-time
    direction. A numerical method multiplies $a$ by $R(h)$ and $b$ by $R(-h)$ per
    step, so it multiplies the product by $R(h) R(-h)$. For Euler that is
    $(1 + h)(1 - h) = 1 - h^2$: the product shrinks by the factor $1 - h^2$ at every
    step, however long we compute. For RK4 the cell lets sympy multiply out
    $R(h) R(-h)$: the terms with $h$, $h^2$, $h^3$, $h^4$ and $h^5$ all cancel and
    $1 + h^6/72 + h^8/576$ remains, which is much closer to $1$. The left panel of
    the figure shows the product itself, the right panel its distance from $1$ on a
    logarithmic scale, where both methods can be seen.
    """),
    code(r'''
    PRODUCT_FACTOR = {name: sp.expand(R[name].subs(z, hs) * R[name].subs(z, -hs))
                      for name in ("euler", "rk4")}
    for name, factor in PRODUCT_FACTOR.items():
        say(f"factor of a b per step, {LABELS[name]:5}: {factor}")
    check(PRODUCT_FACTOR["euler"] == 1 - hs ** 2
          and PRODUCT_FACTOR["rk4"] == 1 + hs ** 6 / 72 + hs ** 8 / 576,
          "R(h) R(-h) is 1 - h^2 (Euler) and 1 + h^6/72 + h^8/576 (RK4)")

    fig, (left, right) = plt.subplots(1, 2, figsize=(9.0, 3.8))
    left.axhline(1.0, color=COLORS["exact"], lw=1.0, label="exact $a b = 1$")
    products = {}
    for name in ("euler", "rk4"):
        t_n, a_n, b_n = curves[name]
        products[name] = a_n * b_n  # the computed product at every step
        factor = float(PRODUCT_FACTOR[name].subs(hs, sp.Rational(1, 4)))  # h = 1/4
        style = dict(color=COLORS[name], marker=MARKERS[name], ms=5, lw=1.2)
        left.plot(t_n, products[name], **style, label=f"{LABELS[name]}, $h = 0.25$")
        right.semilogy(t_n[1:], np.abs(products[name][1:] - 1.0), **style,
                       label=f"{LABELS[name]}: measured")
        predicted = np.abs(factor ** np.arange(1, STEPS + 1) - 1.0)
        right.semilogy(t_n[1:], predicted, ":", color=COLORS["exact"], lw=1.0)
    right.plot([], [], ":", color=COLORS["exact"], label="predicted $|R(h)^n R(-h)^n - 1|$")
    left.set_ylabel("product $a b$ (pure number)")
    right.set_ylabel("$|a b - 1|$ (pure number)")
    left.set_title("the product $a b$")
    right.set_title("its distance from 1 (logarithmic axis)")
    for ax in (left, right):
        ax.set_xlabel("time $x_4$ (units $1/H$)")
        ax.legend(fontsize=8)
    save_figure(fig, "scale_factor_product",
                "Left: the product $a b$ of the 3-space factor and the extra-time "
                "factor of the previous figure, computed with the step $h = 0.25$; "
                "right: its distance $|a b - 1|$ from the exact value on a logarithmic "
                "axis. Horizontal axes the time $x_4$ in units of $1/H$; the product is "
                "a pure number. Exactly $a b = e^{x_4} e^{-x_4} = 1$ (black line). Euler "
                "(squares) multiplies the product by $1 - h^2 = 0.9375$ at every step "
                "and ends at $0.9375^8 = 0.597$; RK4 (circles) multiplies it by "
                "$1 + h^6/72 + h^8/576$ and ends within $3 \\times 10^{-5}$ of 1. The "
                "dotted lines are these predictions; the measured points lie on them.")
    check(abs(products["euler"][-1] - (1 - H_COARSE ** 2) ** 8) < 1e-14,
          "Euler multiplies the product a b by 1 - h^2 per step")
    rk4_factor = 1 + H_COARSE ** 6 / 72 + H_COARSE ** 8 / 576
    check(abs(products["rk4"][-1] - rk4_factor ** 8) < 1e-14
          and abs(products["rk4"][-1] - 1) < 3e-5,
          "RK4 multiplies a b by 1 + h^6/72 + h^8/576 per step (within 3e-5 of 1)")
    '''),
    md(r"""
    ## 9. The convergence study: errors on a log-log plot

    Now the main experiment. For each method we solve problem A from $t = 0$ to
    $t = 1$ with $N = 2, 4, 8, \dots, 4096$ steps ($h = 1/N$) and record the error
    $|y_N - e^{-1}|$ at the end time. The cell prints the table and fits a straight
    line $\log e = \log C + p \log h$ through the points where the error is still
    much larger than the rounding errors, with numpy's `polyfit` (a least-squares
    fit: the line with the smallest sum of squared vertical distances). The slope
    $p$ is the measured order. The table also reproduces the classic numbers of
    Euler's method, $(1 - h)^N$ = 0.250000, 0.316406, 0.343609, 0.356074 for
    $h = 1/2, 1/4, 1/8, 1/16$.
    """),
    code(r'''
    EXACT_A = math.exp(-1.0)  # the exact value y(1) = e^(-1)
    N_LIST = [2 ** k for k in range(1, 13)]  # 2, 4, ..., 4096 steps
    ends = {name: [solve(step, decay, 1.0, 1.0, n)[1][-1] for n in N_LIST]
            for name, step in METHODS.items()}
    errors = {name: np.abs(np.array(values) - EXACT_A) for name, values in ends.items()}
    say("     N        h     Euler y_N   error Euler  error midpoint     error RK4")
    for i, n in enumerate(N_LIST):
        say(f"{n:6d} {1 / n:8.6f}  {ends['euler'][i]:12.6f}  {errors['euler'][i]:11.3e}"
            f"  {errors['midpoint'][i]:14.3e}  {errors['rk4'][i]:12.3e}")

    h_array = 1.0 / np.array(N_LIST, dtype=float)
    FIT = {"euler": slice(5, 12), "midpoint": slice(5, 12), "rk4": slice(1, 8)}
    slopes = {}
    for name, part in FIT.items():
        # polyfit(x, y, 1) returns (slope, intercept) of the best straight line.
        slope, _ = np.polyfit(np.log10(h_array[part]), np.log10(errors[name][part]), 1)
        slopes[name] = slope
        report(f"measured order of {LABELS[name]} (slope)", f"{slope:.4f}")
    check([round(v, 6) for v in ends["euler"][:4]]
          == [0.25, 0.316406, 0.343609, 0.356074],
          "Euler values (1 - h)^N for h = 1/2, 1/4, 1/8, 1/16")
    check(abs(slopes["euler"] - 1) < 0.02 and abs(slopes["midpoint"] - 2) < 0.02
          and abs(slopes["rk4"] - 4) < 0.1,
          "the measured orders are 1, 2 and 4")
    '''),
    md(r"""
    The next cell draws the table as a log-log plot. The grey dashed guide lines have
    the slopes 1, 2 and 4 exactly; each passes through the last fitted point of its
    method. The measured points must lie on lines parallel to them.
    """),
    code(r'''
    fig, ax = plt.subplots(figsize=(7.0, 5.0))
    for name in METHODS:
        ax.loglog(h_array, errors[name], color=COLORS[name], marker=MARKERS[name],
                  ms=5, lw=1.2, label=f"{LABELS[name]} (measured slope "
                  f"{slopes[name]:.2f})")
        order = {"euler": 1, "midpoint": 2, "rk4": 4}[name]
        anchor = FIT[name].stop - 1  # the last fitted point
        guide = errors[name][anchor] * (h_array / h_array[anchor]) ** order
        ax.loglog(h_array, guide, "--", color=COLORS["guide"], lw=0.9)
        ax.text(h_array[0] * 1.15, guide[0], f"slope {order}", fontsize=8,
                color=COLORS["guide"], va="center")
    ax.set_xlim(h_array[-1] / 1.5, h_array[0] * 3.0)
    ax.set_ylim(1e-17, 1.0)
    ax.set_xlabel("step size $h$ (time units)")
    ax.set_ylabel("error $|y_N - e^{-1}|$ at $t = 1$")
    ax.set_title("Problem A: error at the end time against the step size")
    ax.legend(loc="lower right")
    save_figure(fig, "convergence_loglog",
                "The error at the end time $t = 1$ of problem A, $y' = -y$, for the "
                "Euler method (squares), the midpoint method (triangles) and RK4 "
                "(circles), against the step size $h$ from $1/2$ down to $1/4096$, on "
                "logarithmic axes (each tick a power of ten; time in arbitrary units, "
                "the error a pure number). The dashed grey lines have the slopes 1, 2 "
                "and 4. The points lie on straight lines parallel to them: the error is "
                "$C h^p$ with the orders $p = 1, 2, 4$. The RK4 points bend away at the "
                "bottom left, where rounding errors take over.")
    check(errors["rk4"][7] < 1e-11 < errors["midpoint"][7] < errors["euler"][7],
          "at N = 256: RK4 error < 1e-11 < midpoint error < Euler error")
    '''),
    md(r"""
    ## 10. What halving the step does

    If the error is $C h^p$, then halving $h$ divides it by exactly $2^p$: by 2 for
    Euler, 4 for the midpoint method and 16 for RK4. The next cell computes the
    ratios $e(h)/e(h/2)$ for successive rows of the table, draws them, and checks the
    ratios where the error is not yet limited by rounding.
    """),
    code(r'''
    ratios = {name: errors[name][:-1] / errors[name][1:] for name in METHODS}
    fig, ax = plt.subplots()
    for name in METHODS:
        shown = slice(0, 8) if name == "rk4" else slice(0, 11)  # RK4: before rounding
        ax.semilogx(N_LIST[1:][shown], ratios[name][shown], color=COLORS[name],
                    marker=MARKERS[name], ms=5, lw=1.2, label=LABELS[name])
    for target in (2, 4, 16):
        # a dashed line from N = 3 to just beyond the data, its label to the right
        ax.hlines(target, 3.0, N_LIST[-1] * 1.4, ls="--", color=COLORS["guide"], lw=0.9)
        ax.text(N_LIST[-1] * 1.6, target, f"$2^{{{int(math.log2(target))}}}$ = "
                f"{target}", va="center", ha="left", fontsize=8, color=COLORS["guide"])
    ax.set_xlim(3.0, N_LIST[-1] * 8.0)  # room on the right for the labels
    ax.set_xlabel("number of steps $N$ of the finer run ($h = 1/N$)")
    ax.set_ylabel("error ratio $e(2h)/e(h)$")
    ax.set_title("Halving the step divides the error by $2^p$")
    ax.legend(loc="center left")
    save_figure(fig, "error_ratios",
                "The factor by which the error of problem A at $t = 1$ shrinks when the "
                "step is halved, against the number of steps $N$ of the finer run "
                "(logarithmic horizontal axis; the ratio is a pure number). The ratios "
                "approach 2 for Euler (squares), 4 for the midpoint method "
                "(triangles) and 16 for RK4 (circles), the values $2^p$ for the "
                "orders $p = 1, 2, 4$ (dashed grey lines). RK4 is drawn only up to "
                "$N = 512$; beyond, its error is rounding noise.")
    report("ratio Euler at N = 4096", f"{ratios['euler'][-1]:.5f}")
    report("ratio midpoint at N = 4096", f"{ratios['midpoint'][-1]:.5f}")
    report("ratio RK4 at N = 128", f"{ratios['rk4'][5]:.4f}")
    check(abs(ratios["euler"][-1] - 2) < 0.001
          and abs(ratios["midpoint"][-1] - 4) < 0.001
          and abs(ratios["rk4"][5] - 16) < 0.2,
          "halving h divides the errors by 2, 4 and 16")
    '''),
    md(r"""
    ## 11. Where rounding takes over

    A smaller step is not always better. Every arithmetic operation rounds its result
    to about 16 significant digits, and with $N$ steps about $N$ such rounding errors
    add up. The truncation error of RK4 falls like $h^4$, but the rounding error
    grows with the number of steps $N = 1/h$. The next cell runs RK4 for problem A
    with up to $2^{18} = 262144$ steps (this takes about a second) and draws both
    effects: the error falls along the slope-4 line until it reaches about
    $10^{-16}$, then rises again.
    """),
    code(r'''
    N_LONG = [2 ** k for k in range(1, 19)]  # 2 ... 262144 steps
    rk4_long = np.array([abs(solve(rk4_step, decay, 1.0, 1.0, n)[1][-1] - EXACT_A)
                         for n in N_LONG])
    h_long = 1.0 / np.array(N_LONG, dtype=float)
    best = int(np.argmin(rk4_long))  # the position of the smallest error
    EPS = 2.0 ** -52  # the machine epsilon
    fig, ax = plt.subplots()
    shown = rk4_long > 0  # an error of exactly 0 cannot be drawn on a log axis
    ax.loglog(h_long[shown], rk4_long[shown], color=COLORS["rk4"], marker="o", ms=5,
              lw=1.2, label="RK4: measured error")
    ax.loglog(h_long, errors["rk4"][3] * (h_long / h_array[3]) ** 4, "--",
              color=COLORS["guide"], lw=0.9, label="truncation $C h^4$")
    ax.loglog(h_long, EPS * EXACT_A / h_long, ":", color=COLORS["exact"], lw=1.0,
              label="rounding scale $N \\epsilon\\, e^{-1}$")
    ax.set_ylim(1e-18, 1e-2)
    ax.set_xlabel("step size $h = 1/N$ (time units)")
    ax.set_ylabel("error $|y_N - e^{-1}|$")
    ax.set_title("RK4: truncation error against rounding error")
    ax.legend(loc="upper center")
    save_figure(fig, "rounding_floor",
                "The error of RK4 for problem A at $t = 1$ against the step size $h$ "
                "from $1/2$ to $1/262144$, on logarithmic axes (time in arbitrary "
                "units, the error a pure number). Circles: measured. Dashed grey: the "
                "truncation error $C h^4$. Dotted black: the size $N \\epsilon\\, "
                "e^{-1}$ that $N$ rounding errors of relative size $\\epsilon = "
                "2^{-52}$ can reach. Coming from the right, the error falls with "
                "slope 4 down to about $10^{-16}$; smaller steps only add rounding "
                "errors and the error grows again.")
    report("smallest RK4 error", f"{rk4_long[best]:.3e} at N = {N_LONG[best]}")
    report("RK4 error at N = 262144", f"{rk4_long[-1]:.3e}")
    check(rk4_long[best] < 1e-15 and 256 <= N_LONG[best] <= 16384,
          "the smallest RK4 error is below 1e-15, reached at N between 256 and 16384")
    check(rk4_long[-1] > 10 * max(rk4_long[best], EPS * EXACT_A)
          and rk4_long[-1] < 1e-11,
          "with 262144 steps rounding has made the error grow again")
    '''),
    md(r"""
    ## 12. The oscillator: phase portrait and energy

    Problem B as a system: the state is the vector $Y = (x, v)$ and the right-hand
    side is $f(t, Y) = (v, -x)$. The exact solution goes round the circle
    $x^2 + v^2 = 1$ in the $(x, v)$ plane, once every $2\pi$ time units. The next cell
    solves it with the step $h = 0.2$ up to $t = 10$ (50 steps) with each method and
    draws the three phase portraits. Section 7 predicts what happens to the energy
    $E = (x^2 + v^2)/2$: each step multiplies it by $1 + h^2 = 1.04$ (Euler: the
    point spirals outwards), by $1 + h^4/4 = 1.0004$ (midpoint) and by
    $1 - h^6/72 + h^8/576 = 0.99999911$ (RK4).
    """),
    code(r'''
    def oscillator(t, Y):
        """Problem B: x' = v, v' = -x for the state Y = (x, v)."""
        return np.array([Y[1], -Y[0]])


    Y0 = np.array([1.0, 0.0])  # x(0) = 1, v(0) = 0
    H_OSC = 0.2  # the step size
    portraits = {name: np.array(solve(step, oscillator, Y0, 10.0, 50)[1])
                 for name, step in METHODS.items()}
    angle = np.linspace(0.0, 2 * np.pi, 400)
    fig, ax = plt.subplots(figsize=(5.6, 5.6))
    ax.plot(np.cos(angle), -np.sin(angle), color=COLORS["exact"], lw=1.0,
            label="exact circle $x^2 + v^2 = 1$")
    for name in METHODS:
        x_n, v_n = portraits[name][:, 0], portraits[name][:, 1]
        ax.plot(x_n, v_n, color=COLORS[name], marker=MARKERS[name], ms=3, lw=0.9,
                label=f"{LABELS[name]}, $h = 0.2$, 50 steps")
    ax.plot([1.0], [0.0], "o", color=COLORS["exact"], ms=6)  # the starting point
    ax.set_aspect("equal")
    ax.set_xlabel("position $x$")
    ax.set_ylabel("velocity $v$")
    ax.set_title("Phase portrait of $d^2x/dt^2 = -x$ up to $t = 10$")
    ax.legend(loc="lower left", fontsize=8)
    save_figure(fig, "phase_portrait",
                "Phase portrait of the oscillator $d^2x/dt^2 = -x$ started at $x = 1$, "
                "$v = 0$ (black dot): the velocity $v$ against the position $x$ "
                "(arbitrary units), computed with the step $h = 0.2$ up to $t = 10$. "
                "The exact solution runs clockwise round the black unit circle. Euler "
                "(squares) spirals outwards, because every step multiplies the energy "
                "by $1 + h^2$; the midpoint method (triangles) drifts slowly outwards; "
                "RK4 (circles) stays on the circle.")
    for name in METHODS:
        energy = 0.5 * (portraits[name][:, 0] ** 2 + portraits[name][:, 1] ** 2)
        factor = float(ENERGY_FACTOR[name].subs(hs, sp.Rational(1, 5)))  # at h = 0.2
        predicted = 0.5 * factor ** np.arange(51)  # E_0 times the factor n times
        report(f"energy after 50 steps, {LABELS[name]}", f"{energy[-1]:.10f}")
        check(np.max(np.abs(energy / predicted - 1)) < 1e-13,
              f"{LABELS[name]}: E_n = E_0 times the exact factor to the power n")
    '''),
    md(r"""
    The next cell follows the energy much longer, up to $t = 100$ (500 steps of
    $h = 0.2$), and draws the relative energy error $|E_n/E_0 - 1|$ on a logarithmic
    scale. A straight rising line on this plot means growth like a power of $n$ or
    exponential growth; the three methods differ by many powers of ten.
    """),
    code(r'''
    long_runs = {name: np.array(solve(step, oscillator, Y0, 100.0, 500)[1])
                 for name, step in METHODS.items()}
    fig, ax = plt.subplots()
    t_long = np.linspace(0.0, 100.0, 501)
    drift = {}
    for name in METHODS:
        energy = 0.5 * (long_runs[name][:, 0] ** 2 + long_runs[name][:, 1] ** 2)
        drift[name] = np.abs(energy / 0.5 - 1.0)
        ax.semilogy(t_long[1:], drift[name][1:], color=COLORS[name], lw=1.4,
                    label=LABELS[name])
    ax.set_xlabel("time $t$ (arbitrary units)")
    ax.set_ylabel("relative energy error $|E_n/E_0 - 1|$")
    ax.set_title("Energy drift of the oscillator, step $h = 0.2$")
    ax.legend()
    save_figure(fig, "energy_drift",
                "The relative error of the oscillator energy, $|E_n/E_0 - 1|$, on a "
                "logarithmic vertical axis, against the time $t$ from 0 to 100 "
                "(arbitrary units), for the step $h = 0.2$ (500 steps). Euler: the "
                "energy grows by the factor $1.04$ per step and is $3 \\times 10^{8}$ "
                "times too large at the end. Midpoint: it grows by $1.0004$ per step "
                "(20 percent after 500 steps). RK4: it shrinks by $8.9 \\times "
                "10^{-7}$ per step, a relative error below $5 \\times 10^{-4}$ at "
                "the end.")
    report("energy errors at t = 100 (Euler, midpoint, RK4)",
           f"{drift['euler'][-1]:.3e}, {drift['midpoint'][-1]:.3e}, "
           f"{drift['rk4'][-1]:.3e}")
    check(drift["euler"][-1] > 1e8 and 0.1 < drift["midpoint"][-1] < 0.3
          and drift["rk4"][-1] < 5e-4,
          "after 500 steps: Euler energy off by > 1e8, midpoint by 10-30 %, RK4 < 5e-4")
    '''),
    md(r"""
    ## 13. Richardson's rule: an error estimate without the exact answer

    In real problems the exact answer is unknown. Suppose a method of order $p$ gives
    $Y_h = Y + C h^p$ and $Y_{h/2} = Y + C h^p / 2^p$, where $Y$ is the exact value.
    Subtracting the second from the first, $Y_h - Y_{h/2} = C h^p (1 - 2^{-p}) =
    (C h^p / 2^p)(2^p - 1)$, so the error of the finer result is

    $$Y_{h/2} - Y = \frac{C h^p}{2^p} = \frac{Y_h - Y_{h/2}}{2^p - 1},$$

    which for RK4 ($p = 4$) is $(Y_h - Y_{h/2})/15$. Removing this estimated error
    gives the *extrapolated* value $Y_{h/2} - (Y_h - Y_{h/2})/15 = (16 Y_{h/2} -
    Y_h)/15$. The next cell tests both statements on problem A for $N = 2$ to 128
    (finer run $2N$ steps). The rule assumes that the error is already close to
    $C h^p$; the test shows from which $N$ on this is true.
    """),
    code(r'''
    N_R = [2 ** k for k in range(1, 8)]  # the coarse runs: 2 ... 128 steps
    coarse = np.array([solve(rk4_step, decay, 1.0, 1.0, n)[1][-1] for n in N_R])
    fine = np.array([solve(rk4_step, decay, 1.0, 1.0, 2 * n)[1][-1] for n in N_R])
    estimated = (coarse - fine) / 15.0  # Richardson's estimate of the error of fine
    actual = fine - EXACT_A  # the true error of fine (we know the exact answer here)
    extrapolated = (16.0 * fine - coarse) / 15.0
    for n, e_est, e_act, e_ext in zip(N_R, estimated, actual, extrapolated - EXACT_A):
        say(f"N = {n:3d} -> {2 * n:3d}: estimated {e_est: .3e}, actual {e_act: .3e}, "
            f"extrapolated error {e_ext: .2e}")
    fig, ax = plt.subplots(figsize=(6.0, 5.4))
    ax.loglog(np.abs(actual), np.abs(estimated), "o", color=COLORS["rk4"], ms=6,
              label="RK4 runs with $2N = 4$ to $256$ steps")
    for n, x_value, y_value in zip(N_R, np.abs(actual), np.abs(estimated)):
        ax.annotate(f"$N = {n}$", (x_value, y_value), textcoords="offset points",
                    xytext=(6, -10), fontsize=7)
    diagonal = np.array([1e-14, 1e-4])
    ax.loglog(diagonal, diagonal, "--", color=COLORS["guide"], lw=0.9,
              label="estimate = actual")
    ax.set_xlabel("actual error of the finer run")
    ax.set_ylabel("Richardson estimate $(Y_h - Y_{h/2})/15$")
    ax.set_title("Richardson's estimate against the true error")
    ax.legend(loc="upper left")
    save_figure(fig, "richardson",
                "Richardson's error estimate $(Y_h - Y_{h/2})/15$ of RK4 for problem A "
                "at $t = 1$ (vertical axis) against the true error of the finer run "
                "(horizontal axis), both pure numbers on logarithmic axes; each point "
                "is labelled with the number of steps $N$ of the coarse run, the finer "
                "run has $2N$. The points lie on the dashed diagonal: the estimate, "
                "made without knowing the exact answer, is the error itself to within "
                "10 percent once the coarse run has $N \\geq 8$ steps.")
    ratio = estimated[2:] / actual[2:]
    check(np.all((ratio > 0.9) & (ratio < 1.1)),
          "Richardson's estimate is within 10 % of the actual error for N >= 8")
    check(np.all(np.abs(extrapolated[2:6] - EXACT_A) < np.abs(actual[2:6]) / 10),
          "the extrapolated value is more than 10 times more accurate (N = 8 to 64)")
    '''),
    md(r"""
    ## 14. The last check

    The last cell checks that all 8 figure files exist in the folder
    Revision/textbook/figures and prints the number of checks that passed.
    """),
    code(r'''
    names = ["scale_factors", "scale_factor_product", "convergence_loglog",
             "error_ratios", "rounding_floor", "phase_portrait", "energy_drift",
             "richardson"]
    present = [output_file(f"{FIGURE_FOLDER}/02a_{k}_{name}.png").is_file()
               for k, name in enumerate(names, 1)]
    check(all(present), f"all {len(names)} figure files of notebook 02a exist")
    all_checks_passed()
    '''),
    md(r"""
    ## 15. What this notebook showed

    - One step of size $h$ multiplies the solution of $y' = \lambda y$ by an
      amplification factor $R(\lambda h)$: $1 + z$ (Euler), $1 + z + z^2/2$
      (midpoint) and $1 + z + z^2/2 + z^3/6 + z^4/24$ (RK4), the first 2, 3 and 5
      terms of the series of $e^{z}$.
    - Measured on a log-log plot, the error at a fixed end time is $C h^p$ with the
      orders $p = 1, 2, 4$; halving the step divides the error by 2, 4 and 16.
    - RK4 reaches an error of about $10^{-16}$ with a few thousand steps; smaller
      steps make the result worse, because rounding errors add up.
    - The product of the inflating 3-space factor $e^{x_4}$ and the deflating
      extra-time factor $e^{-x_4}$ is exactly 1; Euler's method destroys this
      compensation (factor $1 - h^2$ per step), RK4 keeps it to $3 \times 10^{-5}$
      even with the coarse step $h = 0.25$ (factor $1 + h^6/72 + h^8/576$).
    - For the oscillator the energy factors per step are exactly $1 + h^2$,
      $1 + h^4/4$ and $1 - h^6/72 + h^8/576$; the computed energies follow these
      predictions to 13 digits.
    - Richardson's rule $(Y_{h/2} - Y_h)/(2^p - 1)$ estimates the error without the
      exact answer, and $(16 Y_{h/2} - Y_h)/15$ is a better value than either run.
    """),
]

if __name__ == "__main__":
    raise SystemExit(run_builder(__file__))
