#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
"""Builder of Notebook 02b, "The shooting method for a quantum well" (textbook
"Universes in Pairs").

The notebook Revision/textbook/notebooks/02b_shooting_quantum_well.ipynb is BUILT from
this file by Revision/textbook/tools/nbkit.py (never edit the .ipynb by hand):

    python Revision/textbook/tools/nbkit.py build \
        Revision/textbook/notebooks/src/02b_shooting_quantum_well.py --date YYYY-MM-DD
    python Revision/textbook/tools/nbkit.py check \
        Revision/textbook/notebooks/src/02b_shooting_quantum_well.py

Chapter 02, example b: eigenvalues of boundary-value problems by shooting.  Part A: the
string (infinite well) u'' = -lambda u, u(0) = u(1) = 0, with bisection and the secant
rule.  Part B: the finite square well of quantum mechanics, its four bound states by
shooting with RK4 and parity conditions at the centre, compared with the exact
transcendental equations solved with mpmath at 30 digits; trial solutions, shooting
functions, eigenfunctions, node counts, orthogonality and the order-4 convergence of
the eigenvalues.  No Revision record is reproduced: every number is computed here.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools"))
from nbkit import code, md, run_builder  # noqa: E402

FIGURES = [
    "02b_1_trial_solutions_string",
    "02b_2_shooting_function_string",
    "02b_3_bisection_vs_secant",
    "02b_4_graphical_solution",
    "02b_5_shooting_functions_well",
    "02b_6_trial_solutions_well",
    "02b_7_eigenfunctions",
    "02b_8_eigenvalue_convergence",
]

FACTS = {
    "id": "02b",
    "name": "02b_shooting_quantum_well",
    "title": "The shooting method: a vibrating string and a quantum well",
    "purpose": (
        "It finds the eigenvalues of two boundary-value problems by shooting: the "
        "string fixed at both ends, whose eigenvalues are n squared times pi squared, "
        "with bisection and the secant rule, and the finite square well of quantum "
        "mechanics (depth 15, half-width 1, in units with hbar = m = 1), whose four "
        "bound states it computes with RK4 and the even and odd conditions at the "
        "centre; it compares every energy with the exact transcendental equations "
        "solved with mpmath to 30 digits, counts the nodes of the eigenfunctions, "
        "checks their orthogonality, and measures the order 4 of the eigenvalue "
        "error."
    ),
    "records": [],
    "packages": ["numpy", "mpmath", "matplotlib"],
    "needs_rust": [],
    "expected_seconds": 10,
    "timeout_seconds": 300,
    "files_written": ["Revision/textbook/figures/02b.captions.json"]
    + [f"Revision/textbook/figures/{name}.png" for name in FIGURES],
    "final_lines": [
        "PASS all 8 figure files of notebook 02b exist",
        "ALL 16 CHECKS PASSED (notebook 02b)",
    ],
    "troubleshooting": [
        ["\"Jupyter command `jupyter-nbconvert` not found\" after typing `python -m "
         "jupyter nbconvert` (the folder that holds the Jupyter programs is not on the "
         "search path of the computer)",
         "start the two programs as Python modules instead. With the environment "
         "active, in the folder Revision/textbook/notebooks, type the first line "
         "below to run the notebook headless, or the second line to open it in "
         "JupyterLab",
         ["python -m nbconvert --execute --inplace 02b_shooting_quantum_well.ipynb",
          "python -m jupyterlab 02b_shooting_quantum_well.ipynb"]],
    ],
}

CELLS = [
    md(r"""
    ## 1. What this notebook computes

    Some differential equations have conditions at BOTH ends of an interval, and they
    have solutions only for special values of a number in the equation, the
    *eigenvalues*. The **shooting method** finds them: guess the number, solve the
    equation from one end as an initial-value problem, see how badly the condition
    at the other end fails, and correct the guess. This notebook

    - Part A: shoots the equation of a string fixed at both ends,
      $u'' = -\lambda u$ with $u(0) = u(1) = 0$, whose eigenvalues are exactly
      $\lambda_n = n^2 \pi^2$; it finds $\lambda_1 = \pi^2$ by bisection and by the
      secant rule and compares how fast the two converge;
    - Part B: shoots the Schroedinger equation of a particle in a finite square
      well (depth $V_0 = 15$, half-width $a = 1$), finds its four bound states with
      RK4 and the even and odd conditions at the centre, and compares every energy
      with the exact solution of the well's transcendental equations, computed with
      mpmath to 30 digits;
    - draws the trial solutions that miss and the ones that hit, the shooting
      functions, the bound-state wave functions in the well, and the convergence of
      the computed energies (order 4, as for RK4 itself);
    - checks the number of nodes and the orthogonality of the wave functions.

    It draws 8 figures and prints a PASS line for every check.
    """),
    md(r"""
    ## 3. The words used in this notebook

    - **Boundary-value problem**: a differential equation with conditions at two
      different points (here at both ends of an interval), instead of all conditions
      at the start.
    - **Eigenvalue, eigenfunction**: a value of the number $\lambda$ (or the energy
      $E$) for which the boundary-value problem has a solution that is not zero
      everywhere; that solution is an eigenfunction.
    - **Shooting**: solve from one end with the conditions there and a guessed
      eigenvalue (like aiming a cannon), measure the *mismatch* at the other end
      (where the shot lands), and change the guess until the mismatch is zero.
    - **Shooting function** $F$: the mismatch as a function of the guess; the
      eigenvalues are its zeros.
    - **Bracket**: two guesses at which $F$ has opposite signs; a continuous $F$ has
      a zero between them.
    - **Bisection**: replace the bracket by the half in which the sign changes; the
      bracket halves at every step.
    - **Secant rule**: draw the straight line through the last two points
      $(\lambda, F(\lambda))$ and take its zero as the next guess.
    - **Schroedinger equation**: the equation of quantum mechanics that gives the
      allowed energies $E$ of a particle in a potential $V(x)$; here, for one
      dimension and in units with $\hbar = m = 1$ ($\hbar$ is Planck's constant
      divided by $2\pi$, $m$ the mass), $-\frac{1}{2} u''(x) + V(x) u(x) = E u(x)$.
      We take it as given.
    - **Potential well, bound state**: a region where $V$ is lower than outside; a
      bound state is a solution with $E$ below the outside value of $V$ that decays
      to zero far away. Its energy is an eigenvalue.
    - **Wave function** $u(x)$: the eigenfunction of the Schroedinger equation;
      $u(x)^2$ is the probability density of finding the particle at $x$, so we
      *normalise* it: $\int u^2\,dx = 1$.
    - **Even, odd (parity)**: $u$ is even if $u(-x) = u(x)$, odd if $u(-x) = -u(x)$.
      An even smooth function has $u'(0) = 0$, an odd one $u(0) = 0$.
    - **Node**: a point where the eigenfunction changes sign.
    - **Orthogonal**: two functions with $\int u_m u_n\,dx = 0$.
    """),
    md(r"""
    ## 4. The physical and mathematical situation

    **Part A: the string.** $u'' = -\lambda u$ on $0 \le x \le 1$ with $u(0) = 0$ and
    $u(1) = 0$. For $\lambda > 0$ the solutions of the equation are
    $A \sin(\sqrt{\lambda}\, x) + B \cos(\sqrt{\lambda}\, x)$ (differentiate twice:
    each term comes back multiplied by $-\lambda$). The condition $u(0) = 0$ gives
    $B = 0$. We may choose $A$ freely (a multiple of a solution is a solution), so
    we start with $u(0) = 0$ and slope $u'(0) = 1$, which gives
    $A = 1/\sqrt{\lambda}$:

    $$u(x; \lambda) = \frac{\sin(\sqrt{\lambda}\, x)}{\sqrt{\lambda}}, \qquad
    F(\lambda) = u(1; \lambda) = \frac{\sin\sqrt{\lambda}}{\sqrt{\lambda}}.$$

    $F(\lambda) = 0$ when $\sqrt{\lambda} = n\pi$, that is $\lambda_n = n^2\pi^2$
    for $n = 1, 2, 3, \dots$ The same equation describes a particle in a box with
    infinitely high walls, with the energy $E = \lambda/2$ (units $\hbar = m = 1$).
    The computer does not know the formula: it computes $F(\lambda)$ by solving the
    initial-value problem with RK4, and we use the formula only to check it.

    **Part B: the finite square well.** The potential is $V(x) = -V_0$ for
    $|x| < a$ and $V(x) = 0$ for $|x| > a$, with $V_0 = 15$ and $a = 1$. The
    Schroedinger equation $-\frac{1}{2} u'' + V u = E u$ multiplied by $-2$ reads

    $$u'' = 2\,(V(x) - E)\, u .$$

    A bound state has $-V_0 < E < 0$. Write $k = \sqrt{2(E + V_0)}$ and
    $\kappa = \sqrt{-2E}$ (both positive).

    - Outside the well ($V = 0$): $u'' = \kappa^2 u$, solved by $e^{\kappa x}$ and
      $e^{-\kappa x}$. For $x < -a$ only $e^{\kappa x}$ goes to zero as
      $x \to -\infty$. So we know exactly how to start: at $x = -a$ take $u = 1$
      and $u' = \kappa$ (the values of $e^{\kappa (x + a)}$ there).
    - Inside ($V = -V_0$): $u'' = -k^2 u$, solved by $\cos$ and $\sin$ of $k x$.
    - The well is symmetric, so every bound state is even or odd. An even state has
      $u'(0) = 0$, an odd state $u(0) = 0$. These are the conditions at the far end
      of the shot: we integrate from $x = -a$ to $x = 0$ and use the shooting
      functions $F_{\rm even}(E) = u'(0)$ and $F_{\rm odd}(E) = u(0)$.

    **The exact answer.** Inside, the solution that starts with $u(-a) = 1$,
    $u'(-a) = \kappa$ is $u = \cos(k(x + a)) + (\kappa/k) \sin(k(x + a))$ (check
    the two start values by putting $x = -a$). At $x = 0$:
    $F_{\rm even} = -k \sin(ka) + \kappa \cos(ka)$, which vanishes when
    $k \tan(ka) = \kappa$, and $F_{\rm odd} = \cos(ka) + (\kappa/k) \sin(ka)$, which
    vanishes when $-k \cot(ka) = \kappa$. With $z = ka$ and
    $z_0 = a\sqrt{2V_0} = \sqrt{30}$ we have $\kappa a = \sqrt{z_0^2 - z^2}$, so

    $$\text{even: } \tan z = \frac{\sqrt{z_0^2 - z^2}}{z}, \qquad
    \text{odd: } -\cot z = \frac{\sqrt{z_0^2 - z^2}}{z}, \qquad
    E = \frac{z^2}{2a^2} - V_0 .$$

    These equations have no formula for $z$, but mpmath solves them to any number
    of digits. The well has one bound state for each interval of length $\pi/2$
    that begins below $z_0$. The intervals begin at $0$, $\pi/2 = 1.571$,
    $\pi = 3.142$, $3\pi/2 = 4.712$, $2\pi = 6.283$, ...; with $z_0 = 5.477$
    (so $z_0/(\pi/2) = 3.49$) the first four begin below $z_0$ and the fifth does
    not, so the well has 4 bound states.

    **The connection to this book.** The Kohn-Sham equations of the book are solved
    in the same way: two first-order equations in the hidden coordinate are shot
    from the tip of the interval to the brane, where (with the ASSUMED mirror
    symmetry) an even or an odd condition must hold, exactly like $u'(0) = 0$ or
    $u(0) = 0$ here.
    """),
    md(r"""
    ## 5. The tools: RK4 for a system, bisection and the secant rule

    The next cell defines one RK4 step for a system $Y' = f(x, Y)$ (the same rule
    as for one equation, applied to the vector $Y = (u, u')$), the bisection and
    the secant rule. Both root finders print nothing; they return the list of all
    the guesses they made, so that we can study how fast they approach the root.
    """),
    code(r'''
    import math  # sqrt, sin, pi for single numbers

    import mpmath  # numbers with as many digits as we ask for
    import numpy as np  # arrays (vectors) of numbers

    # Colours that colour-blind readers can tell apart; curves also differ by style.
    BLUE, ORANGE, AQUA, VIOLET = "#2a78d6", "#eb6834", "#1baf7a", "#4a3aa7"
    GREY, BLACK = "#8a8986", "#000000"
    LEVEL_COLORS = [BLUE, ORANGE, AQUA, VIOLET]  # one colour per bound state


    def rk4_step(f, x, Y, h):
        """One classical RK4 step for the system Y' = f(x, Y)."""
        k1 = f(x, Y)
        k2 = f(x + h / 2, Y + (h / 2) * k1)
        k3 = f(x + h / 2, Y + (h / 2) * k2)
        k4 = f(x + h, Y + h * k3)
        return Y + (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4)


    def bisection(F, lo, hi, steps):
        """steps bisection steps on the bracket (lo, hi); the list of midpoints."""
        f_lo = F(lo)
        guesses = []
        for _ in range(steps):
            mid = 0.5 * (lo + hi)
            f_mid = F(mid)
            guesses.append(mid)
            if (f_mid > 0) == (f_lo > 0):  # same sign as at lo: the root is right
                lo, f_lo = mid, f_mid
            else:  # opposite sign: the root lies between lo and mid
                hi = mid
        return guesses


    def secant(F, x0, x1, steps):
        """steps secant steps from the guesses x0, x1; the list of new guesses."""
        f0, f1 = F(x0), F(x1)
        guesses = []
        for _ in range(steps):
            if f1 == f0:  # the line is flat: no new information (converged)
                break
            x2 = x1 - f1 * (x1 - x0) / (f1 - f0)  # the zero of the line
            x0, f0, x1, f1 = x1, f1, x2, F(x2)
            guesses.append(x2)
        return guesses


    say("RK4 for systems, bisection and the secant rule are defined.")
    '''),
    md(r"""
    ## 6. Part A: shooting the string

    The function `shoot_string(lam, n)` solves $u'' = -\lambda u$ as the system
    $u' = v$, $v' = -\lambda u$ from $x = 0$ with $u = 0$, $v = 1$, in $n$ RK4 steps,
    and returns all the points. The first cell draws three shots: with
    $\lambda = 5$ the string comes down too late, with $\lambda = 15$ too early, and
    with $\lambda = \pi^2$ it lands exactly at $u(1) = 0$.
    """),
    code(r'''
    def shoot_string(lam, n):
        """RK4 solution of u'' = -lam u, u(0) = 0, u'(0) = 1 on 0 <= x <= 1 in n
        steps.  Returns the n + 1 positions and the n + 1 values of u."""
        def f(x, Y):
            return np.array([Y[1], -lam * Y[0]])  # (u', v') = (v, -lam u)
        h = 1.0 / n
        Y = np.array([0.0, 1.0])  # u(0) = 0, u'(0) = 1
        xs, us = [0.0], [0.0]
        for i in range(n):
            Y = rk4_step(f, i * h, Y, h)
            xs.append((i + 1) * h)
            us.append(Y[0])
        return np.array(xs), np.array(us)


    def F_string(lam, n=200):
        """The shooting function: where the shot lands, u(1)."""
        return shoot_string(lam, n)[1][-1]


    fig, ax = plt.subplots()
    for lam, color, style in ((5.0, ORANGE, "--"), (math.pi ** 2, BLUE, "-"),
                              (15.0, AQUA, "-.")):
        xs, us = shoot_string(lam, 200)
        ax.plot(xs, us, style, color=color, lw=1.6,
                label=f"$\\lambda = {lam:.4f}$: $u(1) = {us[-1]:+.4f}$")
        ax.plot([1.0], [us[-1]], "o", color=color, ms=6)
    ax.axhline(0.0, color=BLACK, lw=0.8)
    ax.plot([0.0, 1.0], [0.0, 0.0], "s", color=BLACK, ms=7, label="the two fixed ends")
    ax.set_xlabel("position $x$ along the string")
    ax.set_ylabel("displacement $u(x)$")
    ax.set_title("Three shots for $u'' = -\\lambda u$, $u(0) = 0$, $u'(0) = 1$")
    ax.legend(fontsize=8)
    save_figure(fig, "trial_solutions_string",
                "Three shots for the string equation $d^2u/dx^2 = -\\lambda u$ started at "
                "$x = 0$ with $u = 0$ and slope 1, computed with RK4 (200 steps). "
                "Horizontal axis the position $x$ from 0 to 1, vertical axis the "
                "displacement $u$ (arbitrary units). The target is $u(1) = 0$ (black "
                "squares: the fixed ends). With $\\lambda = 5$ the shot lands above "
                "the target, with $\\lambda = 15$ below it, and with "
                "$\\lambda = \\pi^2 = 9.8696$ exactly on it: $\\pi^2$ is an "
                "eigenvalue.")
    check(F_string(5.0) > 0 > F_string(15.0) and abs(F_string(math.pi ** 2)) < 1e-9,
          "u(1) > 0 for lambda = 5, < 0 for lambda = 15, = 0 for lambda = pi^2")
    '''),
    md(r"""
    The next cell draws the whole shooting function $F(\lambda) = u(1; \lambda)$ for
    $\lambda$ from 0.5 to 100: the RK4 values (points) and the exact
    $\sin\sqrt{\lambda}/\sqrt{\lambda}$ (line). Its zeros are the eigenvalues
    $\pi^2$, $4\pi^2$ and $9\pi^2$.
    """),
    code(r'''
    lam_points = np.linspace(0.5, 100.0, 60)  # 60 guesses for RK4
    lam_fine = np.linspace(0.5, 100.0, 800)  # many points for the exact curve
    F_points = np.array([F_string(lam) for lam in lam_points])
    F_exact = np.sin(np.sqrt(lam_fine)) / np.sqrt(lam_fine)
    fig, ax = plt.subplots()
    ax.plot(lam_fine, F_exact, color=BLACK, lw=1.0,
            label="exact $\\sin\\sqrt{\\lambda}/\\sqrt{\\lambda}$")
    ax.plot(lam_points, F_points, "o", color=BLUE, ms=4, label="RK4 shots, 200 steps")
    for n in (1, 2, 3):
        ax.axvline(n ** 2 * math.pi ** 2, ls=":", color=GREY, lw=1.0)
        ax.text(n ** 2 * math.pi ** 2, 0.62, f"${n * n}\\pi^2$", ha="center",
                fontsize=9)
    ax.axhline(0.0, color=BLACK, lw=0.8)
    ax.set_xlabel("guessed eigenvalue $\\lambda$")
    ax.set_ylabel("$F(\\lambda) = u(1; \\lambda)$")
    ax.set_ylim(-0.3, 0.7)
    ax.set_title("The shooting function of the string")
    ax.legend()
    save_figure(fig, "shooting_function_string",
                "The shooting function $F(\\lambda) = u(1; \\lambda)$ of the string, "
                "for $\\lambda$ from 0.5 to 100 (both axes pure numbers): the "
                "values computed by RK4 with 200 steps (blue points) and the exact "
                "$\\sin\\sqrt{\\lambda}/\\sqrt{\\lambda}$ (black line). The zeros, "
                "marked by dotted lines, are the eigenvalues $\\pi^2 = 9.87$, "
                "$4\\pi^2 = 39.48$ and $9\\pi^2 = 88.83$; between two zeros $F$ "
                "keeps its sign, so every pair of guesses with opposite signs of $F$ "
                "brackets an eigenvalue.")
    worst = np.max(np.abs(F_points - np.sin(np.sqrt(lam_points)) /
                          np.sqrt(lam_points)))
    report("largest difference RK4 - exact shooting function", f"{worst:.2e}")
    check(worst < 1e-7, "the RK4 shooting function equals sin(sqrt(lam))/sqrt(lam)")
    '''),
    md(r"""
    ## 7. Bisection against the secant rule

    Both start from the bracket $5 < \lambda < 15$ (where $F(5) > 0 > F(15)$). The
    next cell prints the first six bisection steps (each one gains one binary digit)
    and the first six secant steps (each one roughly multiplies the number of
    correct digits by 1.6), then runs both further and draws the error
    $|\lambda_k - \pi^2|$ after each step on a logarithmic axis.
    """),
    code(r'''
    PI2 = math.pi ** 2  # the exact eigenvalue
    bis = bisection(F_string, 5.0, 15.0, 45)
    sec = secant(F_string, 5.0, 15.0, 12)
    say("step   bisection midpoint   F(midpoint)    secant guess")
    for k in range(6):
        say(f"{k + 1:4d}   {bis[k]:18.6f}   {F_string(bis[k]):+11.5f}   {sec[k]:13.7f}")
    lam_rk4 = sec[-1]  # the converged secant value: the RK4 eigenvalue (200 steps)
    report("eigenvalue by RK4 shooting (200 steps)", f"{lam_rk4:.12f}")
    report("pi^2", f"{PI2:.12f}")
    errors_bis = np.abs(np.array(bis) - lam_rk4)
    errors_sec = np.abs(np.array(sec) - lam_rk4)
    fig, ax = plt.subplots()
    ax.semilogy(range(1, len(bis) + 1), np.maximum(errors_bis, 1e-17), "s-",
                color=ORANGE, ms=4, lw=1.2, label="bisection")
    ax.semilogy(range(1, len(sec) + 1), np.maximum(errors_sec, 1e-17), "o-",
                color=BLUE, ms=5, lw=1.2, label="secant rule")
    k_values = np.arange(1, len(bis) + 1)
    ax.semilogy(k_values, 10.0 / 2.0 ** k_values, ":", color=GREY,
                label="bracket width $10/2^k$")
    ax.set_xlabel("step $k$")
    ax.set_ylabel("error $|\\lambda_k - \\lambda_1|$")
    ax.set_ylim(1e-17, 10.0)
    ax.set_title("How fast the two root finders approach the eigenvalue $\\lambda_1$")
    ax.legend()
    save_figure(fig, "bisection_vs_secant",
                "The error of the guess after $k$ steps, $|\\lambda_k - \\lambda_1|$, "
                "where $\\lambda_1$ is the zero of the RK4 shooting function (200 "
                "steps), which differs from $\\pi^2$ by $1.0 \\times 10^{-8}$, "
                "for bisection (squares) and the secant rule (circles), both started "
                "from 5 and 15, on a logarithmic vertical axis (pure numbers); errors "
                "of exactly zero are drawn at $10^{-17}$. Bisection follows the "
                "dotted line of the halving bracket, one binary digit per step, and "
                "after 45 steps it is still about $10^{-13}$ away (the bracket is "
                "$10/2^{45} = 2.8 \\times 10^{-13}$ wide); the secant rule reaches the "
                "rounding level in about 9 steps, its error falling faster and faster.")
    check(bis[:6] == [10.0, 7.5, 8.75, 9.375, 9.6875, 9.84375],
          "the bisection midpoints 10, 7.5, 8.75, 9.375, 9.6875, 9.84375")
    check(abs(sec[5] - PI2) < 1e-6 and abs(bis[5] - PI2) > 0.02,
          "after 6 steps: secant within 1e-6 of pi^2, bisection still 0.02 away")
    check(abs(lam_rk4 - PI2) < 2e-8 and abs(bis[-1] - lam_rk4) < 1e-11,
          "RK4 eigenvalue = pi^2 within 2e-8; 45 bisections agree within 1e-11")
    '''),
    md(r"""
    ## 8. Part B: the finite square well, solved exactly with mpmath

    The next cell solves the even and odd equations of section 4 with mpmath at 30
    significant digits. To avoid the infinities of $\tan$ and $\cot$ it multiplies
    them out: even $g(z) = z \sin z - \sqrt{z_0^2 - z^2}\cos z = 0$, odd
    $g(z) = z \cos z + \sqrt{z_0^2 - z^2}\sin z = 0$. Even roots lie between $n\pi$
    and $n\pi + \pi/2$, odd ones between $n\pi + \pi/2$ and $(n + 1)\pi$ (but never
    beyond $z_0$); mpmath's `findroot` with the method "anderson" refines each
    bracket. The figure shows the classic graphical solution: the curves $\tan z$
    and $-\cot z$ cross the curve $\sqrt{z_0^2 - z^2}/z$ at the solutions.
    """),
    code(r'''
    V0, A = 15.0, 1.0  # the depth and the half-width of the well
    mpmath.mp.dps = 30  # work with 30 significant digits
    Z0 = mpmath.sqrt(2 * mpmath.mpf(V0)) * A  # z0 = a sqrt(2 V0) = sqrt(30)


    def g_even(z):
        return z * mpmath.sin(z) - mpmath.sqrt(Z0 ** 2 - z ** 2) * mpmath.cos(z)


    def g_odd(z):
        return z * mpmath.cos(z) + mpmath.sqrt(Z0 ** 2 - z ** 2) * mpmath.sin(z)


    EXACT = []  # (energy, parity) of the bound states, lowest first
    for j in range(8):  # the intervals of length pi/2 between 0 and z0
        lo = j * mpmath.pi / 2
        hi = min((j + 1) * mpmath.pi / 2, Z0)
        if lo >= Z0:
            break
        g, parity = (g_even, "even") if j % 2 == 0 else (g_odd, "odd")
        # the root inside the interval (lo, hi), searched a hair away from its ends
        z = mpmath.findroot(g, (lo + mpmath.mpf("1e-20"), hi - mpmath.mpf("1e-20")),
                            solver="anderson")
        EXACT.append((z ** 2 / (2 * A ** 2) - V0, parity, z))
    for n, (energy, parity, z) in enumerate(EXACT):
        say(f"state {n} ({parity:4}): z = {mpmath.nstr(z, 20)}, "
            f"E = {mpmath.nstr(energy, 20)}")
    check(len(EXACT) == 4 and [p for _, p, _ in EXACT] == ["even", "odd", "even", "odd"],
          "the well has 4 bound states: even, odd, even, odd")

    z_axis = np.linspace(0.01, float(Z0), 2000)
    rhs = np.sqrt(float(Z0) ** 2 - z_axis ** 2) / z_axis
    tan_z = np.tan(z_axis)
    cot_z = -1.0 / np.tan(z_axis)
    tan_z[np.abs(tan_z) > 12] = np.nan  # do not draw the jumps at the poles
    cot_z[np.abs(cot_z) > 12] = np.nan
    fig, ax = plt.subplots()
    ax.plot(z_axis, rhs, color=BLACK, lw=1.5, label="$\\sqrt{z_0^2 - z^2}/z$")
    ax.plot(z_axis, tan_z, color=BLUE, lw=1.2, label="$\\tan z$ (even states)")
    ax.plot(z_axis, cot_z, "--", color=ORANGE, lw=1.2, label="$-\\cot z$ (odd states)")
    for n, (energy, parity, z) in enumerate(EXACT):
        zf = float(z)
        ax.plot([zf], [math.sqrt(float(Z0) ** 2 - zf ** 2) / zf], "o",
                color=LEVEL_COLORS[n], ms=7, zorder=5)
        ax.annotate(f"$n = {n}$", (zf, math.sqrt(float(Z0) ** 2 - zf ** 2) / zf),
                    textcoords="offset points", xytext=(5, 8), fontsize=9)
    ax.axvline(float(Z0), color=GREY, ls=":", lw=1.0)
    ax.text(float(Z0), 7.3, "$z_0 = \\sqrt{30}$", ha="right", fontsize=9)
    ax.set_ylim(0.0, 8.0)
    ax.set_xlabel("$z = k a$")
    ax.set_ylabel("value of each side of the equation")
    ax.set_title("Graphical solution of the finite-well equations, $z_0 = 5.477$")
    ax.legend(loc="upper center", fontsize=8)
    save_figure(fig, "graphical_solution",
                "The graphical solution of the finite-well equations for "
                "$z_0 = a\\sqrt{2V_0} = \\sqrt{30} = 5.477$: horizontal axis "
                "$z = ka$ (a pure number), vertical axis the value of each side. The "
                "black curve is $\\sqrt{z_0^2 - z^2}/z$, the blue branches $\\tan z$ "
                "(even states), the dashed orange branches $-\\cot z$ (odd states). "
                "Each crossing, marked by a dot, is one bound state; there are four, "
                "alternately even and odd, and none beyond $z_0$, where the black "
                "curve reaches zero.")
    '''),
    md(r"""
    ## 9. Part B by shooting with RK4

    The function `shoot_well(E, n)` starts at $x = -a$ with $u = 1$, $u' = \kappa$
    and makes $n$ RK4 steps to $x = 0$ with the inside equation $u'' = -2(V_0 + E)
    u$. It works for one energy or for a whole array of energies at once (numpy
    computes elementwise), which makes the scan of the shooting functions fast. The
    next cell draws $F_{\rm even}(E) = u'(0)$ and $F_{\rm odd}(E) = u(0)$ for 400
    energies between $-V_0$ and 0 and marks the exact energies.
    """),
    code(r'''
    def shoot_well(E, n):
        """RK4 from x = -a (u = 1, u' = kappa) to x = 0 inside the well; E may be an
        array.  Returns (u(0), u'(0))."""
        E = np.asarray(E, dtype=float)
        kappa = np.sqrt(-2.0 * E)  # the decay rate outside the well

        def f(x, Y):
            return np.array([Y[1], 2.0 * (-V0 - E) * Y[0]])  # (u', 2 (V - E) u)
        h = A / n
        Y = np.array([np.ones_like(E), kappa])
        for i in range(n):
            Y = rk4_step(f, -A + i * h, Y, h)
        return Y[0], Y[1]


    def F_even(E, n=200):
        return shoot_well(E, n)[1]  # u'(0): zero for an even state


    def F_odd(E, n=200):
        return shoot_well(E, n)[0]  # u(0): zero for an odd state


    E_scan = np.linspace(-V0 + 1e-3, -1e-3, 400)  # 400 guesses inside (-V0, 0)
    fe, fo = F_even(E_scan), F_odd(E_scan)
    fig, ax = plt.subplots()
    ax.plot(E_scan, fe, color=BLUE, lw=1.4, label="$F_{\\rm even}(E) = u'(0)$")
    ax.plot(E_scan, fo, "--", color=ORANGE, lw=1.4, label="$F_{\\rm odd}(E) = u(0)$")
    for n, (energy, parity, _) in enumerate(EXACT):
        ax.axvline(float(energy), ls=":", color=GREY, lw=1.0)
        ax.plot([float(energy)], [0.0], "o", color=LEVEL_COLORS[n], ms=7, zorder=5)
        ax.text(float(energy), 4.6, f"$E_{n}$", ha="center", fontsize=9)
    ax.axhline(0.0, color=BLACK, lw=0.8)
    ax.set_ylim(-5.5, 5.5)
    ax.set_xlabel("guessed energy $E$ (units $\\hbar^2/(m a^2)$)")
    ax.set_ylabel("mismatch at $x = 0$")
    ax.set_title("Shooting functions of the finite well ($V_0 = 15$, $a = 1$)")
    ax.legend(loc="lower left")
    save_figure(fig, "shooting_functions_well",
                "The shooting functions of the finite well: $F_{\\rm even}(E) = "
                "u'(0)$ (solid blue) and $F_{\\rm odd}(E) = u(0)$ (dashed orange) for "
                "400 guessed energies between $-V_0 = -15$ and $0$ (horizontal axis, "
                "units $\\hbar^2/(m a^2)$; vertical axis the mismatch, arbitrary "
                "units), each computed by shooting with RK4 from $x = -a$, where "
                "$u = 1$ and $u' = \\kappa$. The dots on the axis are the exact "
                "energies from the transcendental equations: the zeros of "
                "$F_{\\rm even}$ give the even states $E_0, E_2$, those of "
                "$F_{\\rm odd}$ the odd states $E_1, E_3$.")
    even_changes = int(np.sum(np.sign(fe[:-1]) != np.sign(fe[1:])))
    odd_changes = int(np.sum(np.sign(fo[:-1]) != np.sign(fo[1:])))
    report("sign changes of F_even and F_odd in the scan", f"{even_changes}, {odd_changes}")
    check(even_changes == 2 and odd_changes == 2,
          "the scan finds 2 even and 2 odd sign changes, one per bound state")
    '''),
    md(r"""
    The next cell turns every sign change of a scan (made with the same number of
    RK4 steps as the refinement) into a bracket and refines all four brackets AT
    ONCE by bisection (each step evaluates both shooting functions
    for the four midpoints as one numpy array), until the brackets are narrower
    than $10^{-13}$. Then it compares the four energies with the 30-digit exact
    values.
    """),
    code(r'''
    def well_levels(n, tolerance=1e-13):
        """The four energies with n RK4 steps: scan, then bisection on the brackets."""
        lo, hi, even = [], [], []
        for values, is_even in ((F_even(E_scan, n), True), (F_odd(E_scan, n), False)):
            # the places i where the sign of the mismatch differs from that at i + 1
            for i in np.nonzero(np.sign(values[:-1]) != np.sign(values[1:]))[0]:
                lo.append(E_scan[i])
                hi.append(E_scan[i + 1])
                even.append(is_even)
        order = np.argsort(lo)  # lowest energy first
        lo, hi = np.array(lo)[order], np.array(hi)[order]
        even = np.array(even)[order]

        def mismatch(E):
            u0, du0 = shoot_well(E, n)
            return np.where(even, du0, u0)  # u'(0) for even, u(0) for odd states
        f_lo = mismatch(lo)
        while np.max(hi - lo) > tolerance:
            mid = 0.5 * (lo + hi)
            f_mid = mismatch(mid)
            same = np.sign(f_mid) == np.sign(f_lo)  # the root is above mid
            lo, f_lo = np.where(same, mid, lo), np.where(same, f_mid, f_lo)
            hi = np.where(same, hi, mid)
        return 0.5 * (lo + hi), even


    LEVELS, EVEN = well_levels(200)
    exact = np.array([float(energy) for energy, _, _ in EXACT])
    for n, (E_n, E_x) in enumerate(zip(LEVELS, exact)):
        say(f"E_{n}: RK4 (200 steps) {E_n:.12f}, exact {E_x:.12f}, "
            f"difference {E_n - E_x:+.1e}")
    check(np.max(np.abs(LEVELS - exact)) < 1e-7,
          "the four shooting energies agree with the exact ones within 1e-7")
    check(list(EVEN) == [True, False, True, False],
          "the levels alternate: even, odd, even, odd")
    '''),
    md(r"""
    ## 10. What a shot looks like when it misses

    For the ground state $E_0$, the next cell shoots across the WHOLE line from
    $x = -3$ to $x = +3$ (600 RK4 steps of $h = 0.01$, so that the walls $x = \pm 1$
    are grid points and the potential is constant inside every step). It starts
    with the exactly decaying solution $u = e^{\kappa(x + a)}$, $u' = \kappa u$ at
    $x = -3$. Only at the eigenvalue does the shot come down to zero on the right;
    a little below or above $E_0$, the growing solution $e^{\kappa x}$ takes over
    and the shot flies off to $+\infty$ or $-\infty$. That is the reason why only
    special energies are allowed.
    """),
    code(r'''
    def shoot_line(E, x_start=-3.0, x_end=3.0, n=600):
        """RK4 across the whole line; the potential is taken at the middle of every
        step (constant inside a step, because the walls are grid points)."""
        kappa = math.sqrt(-2.0 * E)
        h = (x_end - x_start) / n
        Y = np.array([1.0, kappa]) * math.exp(kappa * (x_start + A))  # exact tail
        xs, us = [x_start], [Y[0]]
        for i in range(n):
            x = x_start + i * h
            V = -V0 if abs(x + h / 2) < A else 0.0  # the potential of this step

            def f(x_value, Y_value, V=V):  # V=V freezes this step's potential in f
                return np.array([Y_value[1], 2.0 * (V - E) * Y_value[0]])
            Y = rk4_step(f, x, Y, h)
            xs.append(x + h)
            us.append(Y[0])
        return np.array(xs), np.array(us)


    E0 = float(EXACT[0][0])
    fig, ax = plt.subplots()
    for shift, color, style in ((-0.05, ORANGE, "--"), (0.0, BLUE, "-"),
                                (0.05, AQUA, "-.")):
        xs, us = shoot_line(E0 + shift)
        ax.plot(xs, us / np.max(np.abs(us[xs <= 0])), style, color=color, lw=1.6,
                label=f"$E = E_0 {shift:+.2f}$")
    ax.axvspan(-A, A, color=GREY, alpha=0.15, label="inside the well")
    ax.axhline(0.0, color=BLACK, lw=0.8)
    ax.set_ylim(-2.0, 2.0)
    ax.set_xlabel("position $x$ (units $a$)")
    ax.set_ylabel("$u(x)$ (scaled to 1 at the left peak)")
    ax.set_title("Shots across the well near the ground state $E_0 = %.4f$" % E0)
    ax.legend(loc="lower left", fontsize=8)
    save_figure(fig, "trial_solutions_well",
                "Shots across the whole line from $x = -3$ to $x = 3$ (horizontal "
                "axis, units of the half-width $a$; the shaded band is the well) for "
                f"the ground-state energy $E_0 = {E0:.4f}$ and for $E_0 \\pm 0.05$; "
                "vertical axis the solution $u$, scaled to 1 at its largest value "
                "left of the centre (arbitrary units). Every shot starts as the "
                "decaying solution on the left. At $E_0$ (solid blue) it decays on the "
                "right as well: a bound state. Slightly below (dashed orange) or above "
                "(dash-dotted aqua), the growing exponential takes over and the shot "
                "flies off to plus or minus infinity.")
    tail = {shift: shoot_line(E0 + shift)[1][-1] for shift in (-0.05, 0.05)}
    check(tail[-0.05] * tail[0.05] < 0 and min(abs(tail[-0.05]), abs(tail[0.05])) > 10,
          "slightly below and above E0 the shots fly off to opposite infinities")
    '''),
    md(r"""
    ## 11. The four wave functions

    The next cell builds each normalised wave function on $-3 \le x \le 3$: inside
    the left half of the well from the RK4 shot (200 steps), on the right half by
    the symmetry $u(-x) = u(x)$ (even) or $u(-x) = -u(x)$ (odd), and outside from
    the exact tails $u(-a) e^{\kappa(x + a)}$. The normalisation integral uses
    Simpson's rule inside (an integration rule with error $\propto h^4$) and the
    exact tail integral $\int_{-\infty}^{-a} e^{2\kappa(x + a)} dx = 1/(2\kappa)$.
    It draws each wave function lifted to the height of its energy, inside the
    drawing of the potential, counts the nodes, and checks the normalisation and
    the orthogonality. For an even and an odd state the product $u_m u_n$ is odd
    (it changes sign when $x$ is replaced by $-x$), so the contributions of the
    left and the right half cancel and its integral is exactly zero; for two states
    of the same parity the cell computes the integral (twice the left half: Simpson
    inside, the exact tail $u_m(-a) u_n(-a)/(\kappa_m + \kappa_n)$ outside).
    Finally the cell tests the cancellation for the four pairs of different parity
    numerically: it integrates $u_m u_n$ with Simpson's rule over the whole drawn
    range $-3 \le x \le 3$, and over the left half $-3 \le x \le 0$ alone. The
    whole integral must vanish, although the half does not.
    """),
    code(r'''
    def simpson(values, h):
        """Simpson's rule for equally spaced values (an even number of intervals)."""
        return h / 3 * (values[0] + values[-1] + 4 * values[1:-1:2].sum()
                        + 2 * values[2:-1:2].sum())


    def wave_function(E, is_even, n=200):
        """Normalised u on a grid of -3 <= x <= 3 (step a/n), built as described."""
        kappa = math.sqrt(-2.0 * E)
        h = A / n

        def f(x, Y):
            return np.array([Y[1], 2.0 * (-V0 - E) * Y[0]])
        Y = np.array([1.0, kappa])
        inside = [1.0]
        for i in range(n):
            Y = rk4_step(f, -A + i * h, Y, h)
            inside.append(Y[0])
        inside = np.array(inside)  # u on -a <= x <= 0
        norm = 2.0 * (simpson(inside ** 2, h) + 1.0 / (2.0 * kappa))  # both halves
        x_left = np.arange(-3.0 * n, -n) * h  # -3 <= x < -a
        left = np.concatenate([np.exp(kappa * (x_left + A)), inside])
        x_half = np.concatenate([x_left, -A + np.arange(n + 1) * h])  # up to x = 0
        sign = 1.0 if is_even else -1.0
        x_all = np.concatenate([x_half, -x_half[-2::-1]])  # mirror x -> -x
        u_all = np.concatenate([left, sign * left[-2::-1]])
        return x_all, u_all / math.sqrt(norm), kappa, inside / math.sqrt(norm), h


    STATES = [wave_function(E_n, bool(e)) for E_n, e in zip(LEVELS, EVEN)]
    fig, ax = plt.subplots(figsize=(7.0, 5.6))
    x_pot = np.array([-3.0, -A, -A, A, A, 3.0])
    ax.plot(x_pot, [0.0, 0.0, -V0, -V0, 0.0, 0.0], color=BLACK, lw=1.5,
            label="potential $V(x)$")
    nodes = []
    for n, (x_all, u_all, kappa, inside, h) in enumerate(STATES):
        E_n = LEVELS[n]
        ax.axhline(E_n, ls=":", color=GREY, lw=0.8)
        parity = "even" if EVEN[n] else "odd"
        ax.plot(x_all, E_n + 1.8 * u_all, color=LEVEL_COLORS[n], lw=1.6,
                label=f"$E_{n} = {E_n:.4f}$ ({parity})")
        big = u_all[np.abs(u_all) > 1e-8 * np.max(np.abs(u_all))]  # drop tiny values
        nodes.append(int(np.sum(np.sign(big[:-1]) != np.sign(big[1:]))))
    ax.set_xlabel("position $x$ (units $a$)")
    ax.set_ylabel("energy (units $\\hbar^2/(m a^2)$) and $E_n + 1.8\\, u_n(x)$")
    ax.set_ylim(-16.0, 5.0)  # room for the legend above the well
    ax.set_title("The four bound states of the finite square well")
    ax.legend(loc="upper center", ncol=2, fontsize=8)
    save_figure(fig, "eigenfunctions",
                "The four bound states of the finite square well of depth 15 and "
                "half-width 1 (black: the potential $V(x)$). Horizontal axis the "
                "position $x$ in units of $a$; vertical axis the energy in units of "
                "$\\hbar^2/(m a^2)$. Each normalised wave function $u_n$ is drawn "
                "as $E_n + 1.8\\, u_n(x)$, so that it sits on its energy level "
                "(dotted line). The state $n$ has $n$ nodes; even and odd states "
                "alternate; the higher the energy, the further the wave function "
                "leaks out of the well, where it decays like $e^{-\\kappa |x|}$.")
    report("nodes of the states 0 to 3", nodes)
    check(nodes == [0, 1, 2, 3], "the state n has exactly n nodes")


    def overlap(m, n):
        """The integral of u_m u_n over the whole line: Simpson inside, exact tails."""
        _, _, k_m, in_m, h = STATES[m]
        _, _, k_n, in_n, _ = STATES[n]
        half = simpson(in_m * in_n, h) + in_m[0] * in_n[0] / (k_m + k_n)
        same = (EVEN[m] == EVEN[n])  # different parity: the halves cancel exactly
        return 2.0 * half if same else 0.0


    gram = np.array([[overlap(m, n) for n in range(4)] for m in range(4)])
    report("largest |integral u_m u_n - (1 if m = n else 0)|",
           f"{np.max(np.abs(gram - np.eye(4))):.1e}")
    check(np.max(np.abs(gram - np.eye(4))) < 1e-8,
          "the wave functions are normalised and orthogonal within 1e-8")

    middle = len(STATES[0][0]) // 2  # the position of x = 0 in the grid -3 ... 3
    whole_line, left_half = [], []
    for m, n in [(0, 1), (0, 3), (1, 2), (2, 3)]:  # the pairs of different parity
        product = STATES[m][1] * STATES[n][1]  # u_m u_n on the grid
        h_grid = STATES[m][4]  # the grid spacing a/200
        whole_line.append(abs(simpson(product, h_grid)))  # from x = -3 to x = 3
        left_half.append(abs(simpson(product[:middle + 1], h_grid)))  # -3 to 0
    report("different parity: largest |whole integral|, smallest |left half|",
           f"{max(whole_line):.1e}, {min(left_half):.2f}")
    check(max(whole_line) < 1e-12 < 0.01 < min(left_half),
          "different parity: the two halves cancel, the whole integral is 0")
    '''),
    md(r"""
    ## 12. The order of the computed energies

    The shooting energy inherits the error of the integrator. The next cell repeats
    the whole level search with $n = 4, 8, \dots, 1024$ RK4 steps on $-a \le x \le 0$
    and draws $|E_n(\text{RK4}) - E_n(\text{exact})|$ against the step size
    $h = a/n$ on a log-log plot. The points lie on lines of slope 4: the energies
    converge with the order of RK4. The higher states have larger errors, because
    their wave functions oscillate faster (the error grows like $(k h)^4$).
    """),
    code(r'''
    N_STEPS = [4, 8, 16, 32, 64, 128, 256, 512, 1024]
    level_errors = np.array([np.abs(well_levels(n)[0] - exact) for n in N_STEPS])
    h_values = A / np.array(N_STEPS, dtype=float)
    fig, ax = plt.subplots()
    slopes = []
    for n in range(4):
        ax.loglog(h_values, level_errors[:, n], "o-", color=LEVEL_COLORS[n], ms=5,
                  lw=1.2, label=f"$E_{n}$")
        fit = level_errors[:, n] > 1e-12  # leave out the rounding-limited points
        slope, _ = np.polyfit(np.log10(h_values[fit]), np.log10(level_errors[fit, n]), 1)
        slopes.append(slope)
    guide = level_errors[0, 3] * (h_values / h_values[0]) ** 4
    ax.loglog(h_values, guide, "--", color=GREY, lw=1.0, label="slope 4")
    ax.set_xlabel("RK4 step size $h = a/n$ (units $a$)")
    ax.set_ylabel("error of the energy (units $\\hbar^2/(m a^2)$)")
    ax.set_title("Shooting energies converge like $h^4$")
    ax.legend()
    save_figure(fig, "eigenvalue_convergence",
                "The error of the four shooting energies of the finite well, "
                "$|E_n(\\mathrm{RK4}) - E_n(\\mathrm{exact})|$ in units of "
                "$\\hbar^2/(m a^2)$, against the RK4 step size $h = a/n$ for "
                "$n = 4$ to $1024$ steps, on logarithmic axes. The points follow lines "
                "of slope 4 (dashed guide): halving the step divides the error of "
                "an eigenvalue by 16, the order of RK4. Higher states (faster "
                "oscillation) have larger errors at the same step.")
    report("measured orders of E_0 ... E_3", ", ".join(f"{s:.2f}" for s in slopes))
    check(all(3.8 < s < 4.3 for s in slopes),
          "the energy errors fall with the order 4 (slopes between 3.8 and 4.3)")
    check(np.all(level_errors[-1] < 1e-9), "with 1024 steps every energy is within 1e-9")
    '''),
    md(r"""
    ## 13. The last check

    The last cell checks that all 8 figure files exist in the folder
    Revision/textbook/figures and prints the number of checks that passed.
    """),
    code(r'''
    names = ["trial_solutions_string", "shooting_function_string",
             "bisection_vs_secant", "graphical_solution", "shooting_functions_well",
             "trial_solutions_well", "eigenfunctions", "eigenvalue_convergence"]
    present = [output_file(f"{FIGURE_FOLDER}/02b_{k}_{name}.png").is_file()
               for k, name in enumerate(names, 1)]
    check(all(present), f"all {len(names)} figure files of notebook 02b exist")
    all_checks_passed()
    '''),
    md(r"""
    ## 14. What this notebook showed

    - A boundary-value problem with an unknown number in it becomes a sequence of
      initial-value problems: shoot from one end, measure the mismatch at the other
      end, and find the zeros of the shooting function.
    - For the string $u'' = -\lambda u$, $u(0) = u(1) = 0$, the RK4 shooting function
      equals $\sin\sqrt{\lambda}/\sqrt{\lambda}$ and its zeros are
      $\lambda_n = n^2\pi^2$. Bisection gains one binary digit per step (after 45
      steps the bracket is still $2.8 \times 10^{-13}$ wide); the secant rule
      reaches the rounding level in about 9 steps.
    - The finite square well of depth 15 and half-width 1 has exactly four bound
      states, alternately even and odd, with $n$ nodes in the state $n$; shooting
      with RK4 and the parity conditions $u'(0) = 0$ or $u(0) = 0$ at the centre
      reproduces the exact energies of the transcendental equations (within
      $10^{-7}$ with 200 steps, $10^{-9}$ with 1024 steps), and the energy errors
      fall like $h^4$.
    - Away from an eigenvalue the shot flies off to $\pm\infty$: only special
      energies give a solution that decays on both sides.
    - The wave functions of different energies are orthogonal.
    """),
]

if __name__ == "__main__":
    raise SystemExit(run_builder(__file__))
