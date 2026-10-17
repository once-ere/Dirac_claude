#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
"""Builder of Notebook 02d, "Shooting two first-order equations with the Pruefer angle"
(textbook "Universes in Pairs").

The notebook Revision/textbook/notebooks/02d_pruefer_shooting.ipynb is BUILT from this
file by Revision/textbook/tools/nbkit.py (never edit the .ipynb by hand):

    python Revision/textbook/tools/nbkit.py build \
        Revision/textbook/notebooks/src/02d_pruefer_shooting.py --date YYYY-MM-DD
    python Revision/textbook/tools/nbkit.py check \
        Revision/textbook/notebooks/src/02d_pruefer_shooting.py

Chapter 02, example d: the shooting method of the Revision Kohn-Sham solver
(Revision/kohn_sham/solver/src/shoot.rs and spectrum.rs), taught on its simplest case,
the free k = 0 block a' = f (M a - eps b), b' = f (eps a - M b) on -L <= y <= 0 of the
corrected metric of 2026-10-16 (hidden scale f = e^(-a4) b4^(1/2) = e^(-a4/3) on the
prescribed history), with the regular tip b(-L) = 0 and the fold conditions b(0) = 0
(even, theta = 0) or a(0) = 0 (odd, theta = pi) at the fold cos z = 0 that joins the
two halves of a cell (filling both is the record's ASSUMED convention).  RK4 with
G = 900 L/3 steps, the Pruefer angle and its winding count, the slope
dPhi/deps = f (integral of r^2)/r(0)^2 (derived with the product rule), and the
program's root finder (Newton steps with a bisection safety net) re-implemented line by
line.  It reproduces every row of Revision/kohn_sham/results/spectrum/free-k0-analytic.csv
(72 levels of four cases, numeric and analytic, and the column f; on the build computer
the 72 numeric levels agree in all 16 printed digits), the numbers of the checks
free_k0_analytic_spectra and free_zero_mode_exact of
Revision/kohn_sham/reports/ks-rust-solver.json (7.23e-10, 5.05e-08 and 1.35e-12),
measures the fourth-order convergence of the levels, and draws the free levels along
the deflating history.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools"))
from nbkit import code, md, run_builder  # noqa: E402

FIGURES = [
    "02d_1_pruefer_staircase",
    "02d_2_staircase_slope",
    "02d_3_angle_along_y",
    "02d_4_odd_level_equation",
    "02d_5_newton_vs_bisection",
    "02d_6_orbitals",
    "02d_7_level_convergence",
    "02d_8_record_differences",
    "02d_9_levels_along_history",
]

FACTS = {
    "id": "02d",
    "name": "02d_pruefer_shooting",
    "title": "Shooting two first-order equations with the Pruefer angle",
    "purpose": (
        "It solves the simplest Kohn-Sham equations of the book, two first-order "
        "equations for the components a and b of an orbital in the hidden coordinate "
        "of the corrected metric (constant mass, no momentum, no interaction, the "
        "hidden scale f), as an eigenvalue problem: it derives the exact levels, "
        "introduces the Pruefer angle, proves with the product rule that its end "
        "value increases with the energy, shoots with RK4 exactly as the Revision Rust "
        "solver does (900 steps on the interval of length 3, the winding count of the "
        "angle, the Newton root finder with a bisection safety net, tolerance 1e-13), "
        "reproduces all 72 levels of the Revision record of the free spectrum, numeric "
        "and exact, for four cases (one of them at a4 = 1.5 on the prescribed history, "
        "f = e^(-1/2)), and the numbers of the solver checks of that spectrum and of "
        "the zero mode, measures the fourth-order convergence of the levels, and draws "
        "the free levels along the deflating history."
    ),
    "records": [
        ["Revision/kohn_sham/ks-theory.json",
         "the block equations in real form with the hidden scale f, the tip and fold "
         "conditions with their status, the history exponent historyBeta and the exact "
         "k = 0 spectra (read)"],
        ["Revision/kohn_sham/results/parameters.json",
         "the solver settings: 900 RK4 steps, root tolerance 1e-13, m = H = 1, L = 3, "
         "the hidden-scale rule (read and used)"],
        ["Revision/kohn_sham/results/spectrum/free-k0-analytic.csv",
         "the 72 free k = 0 levels of the Rust solver for four cases, their hidden "
         "scales f, exact values and differences (reproduced)"],
        ["Revision/kohn_sham/reports/ks-rust-solver.json",
         "the checks free_k0_analytic_spectra and free_zero_mode_exact (their numbers "
         "reproduced)"],
    ],
    "packages": ["numpy", "sympy", "mpmath", "matplotlib"],
    "needs_rust": [],
    "expected_seconds": 20,
    "timeout_seconds": 400,
    "files_written": ["Revision/textbook/figures/02d.captions.json"]
    + [f"Revision/textbook/figures/{name}.png" for name in FIGURES],
    "final_lines": [
        "PASS all 9 figure files of notebook 02d exist",
        "ALL 21 CHECKS PASSED (notebook 02d)",
    ],
    "troubleshooting": [
    ],
}

CELLS = [
    md(r"""
    ## 1. What this notebook computes

    The Kohn-Sham equations of this book (its density-functional model of the field
    dirac16complex in the author's primordial universe) are solved by a Rust program
    of the Revision record, Revision/kohn_sham/solver, with the shooting method. This
    notebook teaches that method on the simplest case of those equations and
    REPRODUCES the program's results for it. It

    - takes from the Revision record Revision/kohn_sham/ks-theory.json the two
      first-order equations for the two real components $a(y)$ and $b(y)$ of an
      orbital in the hidden coordinate $y$ of the corrected metric (version 2 of
      2026-10-16), in the free case (constant mass $M$, no 3-space momentum, no
      interaction), with the hidden scale $f$ and their boundary conditions;
    - derives their exact levels: $\varepsilon = 0$ and
      $\pm\sqrt{M^2 + (n\pi/(fL))^2}$ for the even orbitals, $\pm\sqrt{M^2 + p^2}$
      with $\tan(p f L) = -p/M$ for the odd ones;
    - introduces the **Pruefer angle** $\theta = \mathrm{atan2}(b, a)$ and proves,
      with nothing more than the product rule, that its end value $\Phi$ grows with
      the energy, at the rate $d\Phi/d\varepsilon = f \int r^2\,dy / r(0)^2$; so
      every level is found exactly once and carries a whole-number label;
    - shoots with RK4 exactly as the Rust program does (900 steps on an interval of
      length 3) and finds every level with the program's own root finder (Newton's
      method with a bisection safety net, tolerance $10^{-13}$), re-written here line
      by line;
    - reproduces all 72 levels of the record
      Revision/kohn_sham/results/spectrum/free-k0-analytic.csv (four cases, one of
      them on the deflating history with $f = e^{-1/2}$; on the computer that made
      the record, in all 16 printed digits), the exact column of the record, and the
      numbers that the program's checks of this spectrum and of the zero mode quote;
    - draws the staircase of the Pruefer angle and its slope, the winding of the
      angle along $y$, Newton against bisection, the orbitals, the fourth-order
      convergence of the levels, and the free levels along the deflating history.

    It draws 9 figures and prints a PASS line for every check.
    """),
    md(r"""
    ## 3. The words used in this notebook

    - **Orbital**: a single-particle state of the Kohn-Sham model. Here it is
      described by two real functions $a(y)$ and $b(y)$, its *components*.
    - **Hidden coordinate** $y$: the book's coordinate along the hidden direction
      $x_0$, $y = \ln|\sin z|/(6H)$ with $z = 6 H x_0$ (so $y \le 0$); $y = 0$ is
      the *fold* $\cos z = 0$ ($z = \pi/2$), where the two halves of a cell meet,
      and the interval is cut off at $y = -L$ (the *tip*, towards $\sin z = 0$).
    - **Hidden scale** $f = e^{-a_4} b_4^{1/2}$: the factor that turns a step $dy$
      into a true length $f\,dy$; it shrinks with the deflating extra times. Along
      the prescribed history of the record ($a_4 = H x_4$,
      $b_4 = e^{(4/3) H x_4}$) it is $f = e^{-a_4/3}$: $f = 1$ at $a_4 = 0$ and
      $f = e^{-1/2} = 0.6065$ at $a_4 = 1.5$.
    - **Energy level** $\varepsilon$: a value of the energy for which the equations
      have a solution with all boundary conditions; an eigenvalue. Unit: the mass
      $m$ (in units with $m = H = 1$).
    - **Mass** $M$: the constant mass of the free case; here $M = m$.
    - **Boundary conditions**: at the tip $b(-L) = 0$ (the *regular tip*, a choice
      of the model); at the fold $b(0) = 0$ (*even* orbitals, the fold parameter
      $\theta = 0$) or $a(0) = 0$ (*odd* orbitals, $\theta = \pi$). The record
      derives these two conditions from the joining of the two halves at the fold
      and labels the filling of both together ASSUMED (its convention).
    - **Pruefer angle** $\theta(y)$: the angle of the point $(a, b)$ seen from the
      origin, $a = r \cos\theta$, $b = r \sin\theta$ with $r > 0$; we count every
      full turn, so $\theta$ can grow beyond $2\pi$ (*winding*). $r$ is the
      distance of the point from the origin, $r^2 = a^2 + b^2$.
    - **atan2(b, a)**: the angle of the point $(a, b)$ between $-\pi$ and $\pi$.
    - **End angle** $\Phi(\varepsilon) = \theta(0)$: the angle reached at the fold
      when we shoot with the energy $\varepsilon$.
    - **Label** $l$: the whole number that names a level through its target angle,
      $\theta(0) = l\pi$ (even) or $\pi/2 + l\pi$ (odd).
    - **Monotone (increasing)**: a function that grows whenever its argument grows.
    - **RK4 step count** $G$: the number of RK4 steps on $-L \le y \le 0$; the step
      is $h = L/G$.
    - **Trapezoid rule**: the integral over one step approximated by the step length
      times the average of the two end values.
    - **Bracket**: two energies at which $\Phi$ minus the target has opposite signs;
      the level lies between them.
    - **Newton's method**: replace a function by its tangent line at the current
      guess and take the zero of that line as the next guess.
    - **Transcendental equation**: an equation such as $\tan(pL) = -p/M$ that has no
      solution formula and is solved numerically.
    """),
    md(r"""
    ## 4. The physical and mathematical situation

    **The equations.** The record gives the Kohn-Sham equation of one 2-component
    block in the real form (key `blockEquation.realForm`)
    $a' = f\,[M a - (\kappa k + j(\varepsilon - v)) b]$,
    $b' = f\,[(j(\varepsilon - v) - \kappa k) a - M b]$, where the prime is $d/dy$
    and $f = e^{-a_4} b_4^{1/2}$ is the hidden scale. In the free case with no
    3-space momentum ($k = 0$), no potential ($v = 0$), constant mass $M$ and the
    block type $j = +1$ they are

    $$a' = f\,(M a - \varepsilon b), \qquad b' = f\,(\varepsilon a - M b), \qquad
    -L \le y \le 0,$$

    with $b(-L) = 0$ at the tip and $b(0) = 0$ (even) or $a(0) = 0$ (odd) at the
    fold. The record's values are $M = m = 1$, $H = 1$, $L = 3$ and $f = 1$
    ($a_4 = 0$); the program also checks $L = 2$, $M = 2$, and $L = 3$ at
    $a_4 = 1.5$ on the history, where $f = e^{-1/2}$. In this notebook we take the
    equations as given; the physics chapters derive them.

    **Only the proper length $fL$ matters.** Put $s = f y$, the true (proper)
    distance from the fold. Then $d/dy = f\, d/ds$, the factor $f$ cancels, and the
    equations become $da/ds = M a - \varepsilon b$, $db/ds = \varepsilon a - M b$ on
    $-fL \le s \le 0$: the case $f = 1$ on an interval of length $\ell = fL$. So we
    derive everything for $f = 1$ and length $\ell$, and then put $\ell = fL$.

    **The exact levels.** Step 1: from the first equation,
    $b = (M a - a')/\varepsilon$ (for $\varepsilon \ne 0$; here the prime is
    $d/ds$). Step 2: differentiate: $b' = (M a' - a'')/\varepsilon$. Step 3: put both
    into the second equation: $(M a' - a'')/\varepsilon = \varepsilon a - M (M a -
    a')/\varepsilon$. Step 4: multiply by $\varepsilon$: $M a' - a'' =
    \varepsilon^2 a - M^2 a + M a'$. Step 5: cancel $M a'$:

    $$a'' = (M^2 - \varepsilon^2)\, a .$$

    For $|\varepsilon| > M$ put $p = \sqrt{\varepsilon^2 - M^2}$; then $a'' = -p^2 a$
    and $a = \cos(p s + \varphi)$ with a constant $\varphi$. The conditions on $b$
    become conditions on $a$: $b = 0$ means $M a - a' = 0$.

    - Even: $M a - a' = 0$ at BOTH ends. $M\cos(ps + \varphi) + p \sin(ps +
      \varphi) = R \cos(ps + \varphi - \delta)$ with $\tan\delta = p/M$ vanishes at
      $s = 0$ and at $s = -\ell$ only if the two phases differ by a multiple of
      $\pi$: $p\ell = n\pi$. So $\varepsilon = \pm\sqrt{M^2 + (n\pi/\ell)^2}$,
      $n = 1, 2, \dots$
    - Odd: $a(0) = 0$ gives $a = \sin(ps)$; the tip condition $M \sin(-p\ell) -
      p\cos(-p\ell) = 0$ gives $\tan(p\ell) = -p/M$.
    - $\varepsilon = 0$: the equations become $a' = M a$, $b' = -M b$; with
      $b(-\ell) = 0$ we get $b = 0$ everywhere and $a = e^{M s} = e^{f M y}$: the
      *zero mode*, an even orbital ($b(0) = 0$) with energy exactly 0.

    With $\ell = fL$: the even levels are $\pm\sqrt{M^2 + (n\pi/(fL))^2}$ and the odd
    ones solve $\tan(p f L) = -p/M$, as the record states (key
    `boundaryConditions.exactK0Spectra`). A smaller $f$ (a shorter proper interval)
    raises every level except the zero mode.

    **The Pruefer angle.** Write $a = r\cos\theta$, $b = r\sin\theta$. Then
    $\theta' = (a b' - b a')/r^2$ (the derivative of the angle of a moving point;
    the prime is $d/dy$ again). Insert the equations: $a b' - b a' =
    f\,[a(\varepsilon a - M b) - b(M a - \varepsilon b)] = f\,[\varepsilon (a^2 +
    b^2) - 2 M a b]$. Divide by $r^2 = a^2 + b^2$ and use $2ab/r^2 = 2\sin\theta
    \cos\theta = \sin 2\theta$:

    $$\theta' = f\,(\varepsilon - M \sin 2\theta), \qquad \theta(-L) = 0 .$$

    The fold conditions say $b(0) = 0$, that is $\theta(0) = l\pi$ (even), or
    $a(0) = 0$, that is $\theta(0) = \pi/2 + l\pi$ (odd), for a whole number $l$.

    **How fast the end angle grows.** First the distance $r$: from $r^2 = a^2 + b^2$,
    $r r' = a a' + b b' = f\,[a(M a - \varepsilon b) + b(\varepsilon a - M b)] =
    f M(a^2 - b^2)$, and $(a^2 - b^2)/r^2 = \cos^2\theta - \sin^2\theta =
    \cos 2\theta$, so $r'/r = f M\cos 2\theta$. Now let $u(y) =
    \partial\theta(y)/\partial\varepsilon$, the change of the angle at $y$ per unit
    change of the energy. Differentiate $\theta' = f(\varepsilon - M\sin 2\theta)$
    with respect to $\varepsilon$ (the order of the two derivatives does not
    matter): $u' = f - 2fM\cos(2\theta)\, u = f - 2 (r'/r)\, u$. Multiply by $r^2$:
    $r^2 u' + 2 r r' u = f r^2$. By the product rule the left side is $(r^2 u)'$.
    Integrate from $-L$ to $0$; at the tip $u(-L) = 0$, because $\theta(-L) = 0$ for
    every energy:

    $$\frac{d\Phi}{d\varepsilon} = u(0) = \frac{f}{r(0)^2}\int_{-L}^{0} r^2\,dy > 0 .$$

    So $\Phi(\varepsilon)$ increases strictly, and each target $l\pi$ or
    $\pi/2 + l\pi$ is reached for exactly one $\varepsilon$: every level has its own
    label $l$ and none can be missed. This is how the Rust program finds and names
    its levels, and the formula gives its root finder the slope it needs.
    """),
    md(r"""
    ## 5. The records and the settings

    The next cell reads the three Revision records this notebook uses: the theory
    (the equations, the boundary conditions with their status, the exact spectra,
    the exponent $\beta = 4/3$ of the history $b_4 = e^{\beta a_4}$), the solver's
    parameters (900 RK4 steps, root tolerance $10^{-13}$, the hidden-scale rule
    $f = e^{(\beta/2 - 1) a_4}$) and the table of the free spectrum. It prints the
    statements it relies on and defines the function `hidden_scale`, which computes
    $f$ from $a_4$ with the same arithmetic as the Rust program.
    """),
    code(r'''
    import csv  # reads the table of levels (comma-separated values)
    import math  # sqrt, atan2, pi for single numbers
    import re  # finds numbers inside a text

    import mpmath  # numbers with as many digits as we ask for
    import numpy as np  # arrays of numbers
    import sympy as sp  # exact algebra with symbols

    BLUE, ORANGE, AQUA, VIOLET = "#2a78d6", "#eb6834", "#1baf7a", "#4a3aa7"
    GREY, BLACK = "#8a8986", "#000000"

    THEORY = "Revision/kohn_sham/ks-theory.json"
    PARAMETERS = "Revision/kohn_sham/results/parameters.json"
    TABLE = "Revision/kohn_sham/results/spectrum/free-k0-analytic.csv"
    SOLVER_REPORT = "Revision/kohn_sham/reports/ks-rust-solver.json"
    theory = json.loads(repository_file(THEORY).read_text(encoding="utf-8"))
    parameters = json.loads(repository_file(PARAMETERS).read_text(encoding="utf-8"))
    with open(repository_file(TABLE), encoding="utf-8", newline="") as table:
        ROWS = list(csv.DictReader(table))  # one dictionary per level
    say("realForm: " + theory["blockEquation"]["realForm"])
    FOLD_STATUS = theory["boundaryConditions"]["fold"]["status"]
    say("fold status: " + FOLD_STATUS)
    say("tip status: " + theory["boundaryConditions"]["tip"]["status"])
    say("exact k = 0 spectra: " + theory["boundaryConditions"]["exactK0Spectra"])
    G_CANONICAL = parameters["numerics"]["rk4Steps"]  # RK4 steps for L = 3
    ROOT_TOLERANCE = parameters["numerics"]["rootTolerance"]
    M_RECORD, L_RECORD = parameters["physics"]["m"], parameters["physics"]["L_tipCutoff"]
    top, bottom = theory["adiabaticity"]["historyBeta"].split("/")  # the text "4/3"
    BETA = float(top) / float(bottom)  # beta = 4/3, as the Rust program reads it


    def hidden_scale(a4):
        """f = e^((beta/2 - 1) a4), the record's hidden-scale rule (b4(0) = 1)."""
        return math.exp((0.5 * BETA - 1.0) * a4)


    say("hidden-scale rule: " + parameters["physics"]["hiddenScaleRule"])
    report("RK4 steps, root tolerance, m, L of the record",
           f"{G_CANONICAL}, {ROOT_TOLERANCE}, {M_RECORD}, {L_RECORD}")
    TABLE_CASES = sorted({(float(r["m"]), float(r["L"]), float(r["a4"])) for r in ROWS})
    report("levels in the table; the cases (m, L, a4)", f"{len(ROWS)}; " + ", ".join(
        f"({m:g}, {L:g}, {a4:g})" for m, L, a4 in TABLE_CASES))
    report("hidden scale f at a4 = 0 and at a4 = 1.5",
           f"{hidden_scale(0.0)}, {hidden_scale(1.5):.16f}")
    check("ASSUMED" in FOLD_STATUS and "realForm" in theory["blockEquation"]
          and "f [M_eff a" in theory["blockEquation"]["realForm"]
          and G_CANONICAL == 900 and ROOT_TOLERANCE == 1e-13 and len(ROWS) == 72,
          "records read: equations with f, filling both fold conditions ASSUMED, "
          "900 RK4 steps, tolerance 1e-13, 72 levels")
    '''),
    md(r"""
    ## 6. Shooting with RK4 and counting the turns of the angle

    The function `shoot` follows the Rust program (file
    Revision/kohn_sham/solver/src/shoot.rs) line by line: it starts at the tip
    with $(a, b) = (1, 0)$, so $\theta = 0$; makes $G$ RK4 steps of the two
    equations; after every step it takes the new angle `atan2(b, a)`, adds the
    change of angle since the last step (brought into the range from $-\pi$ to
    $\pi$, so that a full turn is never lost: one step turns the point by much less
    than $\pi$) and so counts every turn. Along the way it adds up
    $\int r^2\,dy$ with the trapezoid rule. It returns $\Phi = \theta(0)$, the slope
    $d\Phi/d\varepsilon = f \int r^2\,dy / r(0)^2$ of section 4, the largest turn of
    a single step (the program refuses a shot in which one step turns by 2 or
    more), and, when asked, the whole path. Like the program, it first multiplies
    the mass and the energy by the hidden scale, $fM$ and $f\varepsilon$, and then
    uses only these products; for $f = 1$ (the default) they are $M$ and
    $\varepsilon$ themselves. (The program also shrinks $(a, b)$ when they become
    astronomically large, above $10^{125}$; that never happens here.)

    The second function integrates the single angle equation
    $\theta' = f(\varepsilon - M \sin 2\theta)$ with RK4 instead; the two different
    computations must agree up to the small RK4 errors. A third test confirms
    section 4: shooting with the hidden scale $f = e^{-1/2}$ on $-3 \le y \le 0$
    gives the same end angle as shooting with $f = 1$ on the proper length
    $\ell = fL = 3 e^{-1/2}$.
    """),
    code(r'''
    def shoot(eps, M, L, G, f=1.0, keep=False):
        """RK4 from y = -L, (a, b) = (1, 0), to y = 0 in G steps, hidden scale f.
        Returns Phi = theta(0), the slope dPhi/deps = f (integral of r^2) / r(0)^2
        and the largest turn of one step; with keep=True also the arrays y, a, b,
        theta of the path."""
        h = L / G  # the step
        fM, fe = f * M, f * eps  # f M and f eps, as the program multiplies them
        a, b = 1.0, 0.0  # the tip: b(-L) = 0, so theta(-L) = 0
        theta, raw = 0.0, 0.0  # the counted angle and the last atan2 value
        integral, r2_before = 0.0, 1.0  # running integral of r^2; r^2 at the last node
        largest = 0.0  # the largest turn of one step so far
        path = [(-L, a, b, theta)]
        for i in range(G):
            p1a, p1b = fM * a - fe * b, fe * a - fM * b  # the slopes (a', b') at start
            a2, b2 = a + h / 2 * p1a, b + h / 2 * p1b  # half a step with them
            p2a, p2b = fM * a2 - fe * b2, fe * a2 - fM * b2  # the slopes there
            a3, b3 = a + h / 2 * p2a, b + h / 2 * p2b  # half a step with these
            p3a, p3b = fM * a3 - fe * b3, fe * a3 - fM * b3  # the slopes there
            a4, b4 = a + h * p3a, b + h * p3b  # a whole step with the third slopes
            p4a, p4b = fM * a4 - fe * b4, fe * a4 - fM * b4  # the slopes at the end
            a += h / 6 * (p1a + 2 * p2a + 2 * p3a + p4a)  # weights 1 : 2 : 2 : 1
            b += h / 6 * (p1b + 2 * p2b + 2 * p3b + p4b)
            new = math.atan2(b, a)  # the angle of (a, b), between -pi and pi
            change = new - raw
            if change > math.pi:  # crossed from just below pi to just above -pi
                change -= 2 * math.pi
            elif change <= -math.pi:  # crossed the other way
                change += 2 * math.pi
            largest = max(largest, abs(change))
            theta += change
            raw = new
            r2 = a * a + b * b  # r^2 at the new node
            integral += h / 2 * (r2_before + r2)  # the trapezoid rule for this step
            r2_before = r2
            if keep:
                path.append((-L + (i + 1) * h, a, b, theta))
        if keep:
            return theta, f * integral / r2_before, largest, np.array(path).T
        return theta, f * integral / r2_before, largest


    def angle_equation(eps, M, L, G, f=1.0):
        """RK4 for the single equation theta' = f (eps - M sin(2 theta)),
        theta(-L) = 0."""
        h = L / G
        theta = 0.0

        def slope(t):
            return f * (eps - M * math.sin(2 * t))
        for _ in range(G):
            k1 = slope(theta)
            k2 = slope(theta + h / 2 * k1)
            k3 = slope(theta + h / 2 * k2)
            k4 = slope(theta + h * k3)
            theta += h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        return theta


    M1, L3 = 1.0, 3.0  # the canonical case of the record
    for eps in (-2.0, 0.0, 1.0, 2.5):
        Phi = shoot(eps, M1, L3, 900)[0]  # element 0 of the result: Phi
        say(f"eps = {eps:+.1f}: Phi by (a, b) = {Phi:+.12f},  "
            f"by the angle equation = {angle_equation(eps, M1, L3, 900):+.12f}")
    differences = [abs(shoot(e, M1, L3, 900)[0] - angle_equation(e, M1, L3, 900))
                   for e in np.linspace(-5.0, 5.0, 21)]
    check(max(differences) < 1e-8 and shoot(0.0, M1, L3, 900)[0] == 0.0,
          "both ways of computing Phi agree within 1e-8; Phi(0) is exactly 0")
    F15 = hidden_scale(1.5)  # f = e^(-1/2) at a4 = 1.5 on the history
    proper = [abs(shoot(e, M1, L3, 900, f=F15)[0] - shoot(e, M1, F15 * L3, 900)[0])
              for e in np.linspace(-5.0, 5.0, 21)]
    report("largest |Phi(f = e^(-1/2), L = 3) - Phi(f = 1, L = 3 e^(-1/2))|",
           f"{max(proper):.1e}")
    check(max(proper) < 1e-12,
          "with the hidden scale f only the proper length f L matters")
    '''),
    md(r"""
    ## 7. The staircase of the Pruefer angle

    The next cell computes $\Phi(\varepsilon)$ for 651 energies from $-6$ to $7$
    ($M = 1$, $L = 3$, $f = 1$, 900 steps) and checks that it increases. The figure
    shows it with the target lines $l\pi$ (even) and $\pi/2 + l\pi$ (odd): the
    levels are the crossings, every target is crossed once, and the levels
    alternate between even and odd. Away from the levels the curve rises with slope
    about $fL = 3$, because $\theta' = f(\varepsilon - M\sin 2\theta)$ is
    $f\varepsilon$ on average.

    Inside the *mass gap* $|\varepsilon| \le M$ the equation
    $a'' = (M^2 - \varepsilon^2)\, a$ has no oscillating solutions, and the only
    level there is the zero mode. The cell checks this for the four cases
    $(M, L, a_4)$ of the table: $\Phi(-M)$ and $\Phi(+M)$ both lie between $-\pi/2$
    and $\pi/2$, so the increasing staircase crosses no target except $0$ while
    $|\varepsilon| \le M$.
    """),
    code(r'''
    eps_grid = np.linspace(-6.0, 7.0, 651)
    shots = [shoot(e, M1, L3, 900) for e in eps_grid]  # (Phi, slope, largest turn)
    Phi_grid = np.array([s[0] for s in shots])
    slope_grid = np.array([s[1] for s in shots])  # dPhi/deps by the formula
    check(np.all(np.diff(Phi_grid) > 0), "Phi(eps) increases on the whole grid")
    gap_ends = []  # Phi at eps = -M and eps = +M for the four cases of the table
    for M, L, a4 in TABLE_CASES:
        G = round(G_CANONICAL * L / 3.0)  # the record's step h = 1/300
        f = hidden_scale(a4)
        gap_ends += [shoot(-M, M, L, G, f=f)[0], shoot(M, M, L, G, f=f)[0]]
    report("largest |Phi(-M)|, |Phi(+M)| in units of pi (four cases)",
           f"{max(abs(p) for p in gap_ends) / math.pi:.4f}")
    check(max(abs(p) for p in gap_ends) < math.pi / 2,
          "for |eps| <= M the staircase crosses no target but 0: only the zero mode")


    def target(parity, label):
        """The target value of Phi for a level of the given parity and label."""
        return label * math.pi if parity == "even" else math.pi / 2 + label * math.pi


    canonical = [r for r in ROWS if float(r["m"]) == 1.0 and float(r["L"]) == 3.0
                 and float(r["a4"]) == 0.0]  # the case M = 1, L = 3, f = 1
    fig, ax = plt.subplots(figsize=(7.0, 5.4))
    ax.plot(eps_grid, Phi_grid / math.pi, color=BLACK, lw=1.4,
            label="$\\Phi(\\varepsilon)/\\pi$ (RK4, 900 steps)")
    for label in range(-4, 7):
        ax.axhline(label, color=BLUE, lw=0.6, alpha=0.6)
        ax.axhline(label + 0.5, color=ORANGE, lw=0.6, ls="--", alpha=0.6)
    for r in canonical:
        is_even = r["parity"] == "even"
        ax.plot(float(r["eps_numeric"]), target(r["parity"], int(r["label"])) / math.pi,
                "o" if is_even else "s", color=BLUE if is_even else ORANGE, ms=6)
    ax.plot([], [], "o", color=BLUE, label="even levels: $\\Phi = l\\pi$")
    ax.plot([], [], "s", color=ORANGE, label="odd levels: $\\Phi = \\pi/2 + l\\pi$")
    ax.set_ylim(-4.2, 6.2)
    ax.set_xlabel("energy $\\varepsilon$ (units $m$)")
    ax.set_ylabel("end angle $\\Phi = \\theta(0)$ in units of $\\pi$")
    ax.set_title("The Pruefer staircase: $M = 1$, $L = 3$, $f = 1$")
    ax.legend(loc="upper left", fontsize=8)
    save_figure(fig, "pruefer_staircase",
                "The end value of the Pruefer angle, $\\Phi(\\varepsilon) = "
                "\\theta(0)$ in units of $\\pi$ (vertical axis), against the energy "
                "$\\varepsilon$ in units of the mass $m$ from $-6$ to $7$ (horizontal "
                "axis), for $M = 1$, $L = 3$, $f = 1$ and 900 RK4 steps. Blue lines: "
                "the even "
                "targets $l\\pi$; dashed orange lines: the odd targets "
                "$\\pi/2 + l\\pi$. Dots and squares: the 18 levels of the Revision "
                "record for this case. $\\Phi$ increases steadily, so it crosses every "
                "target exactly once: each level has its own label $l$, and even and "
                "odd levels alternate. The zero mode sits at $\\varepsilon = 0$, "
                "$\\Phi = 0$.")
    '''),
    md(r"""
    ## 8. The slope of the staircase

    Section 4 proved $d\Phi/d\varepsilon = f \int_{-L}^{0} r^2\,dy / r(0)^2$, which
    is never negative. The next cell tests this formula for $f = 1$ in two ways.
    First, it compares the formula (computed by `shoot` with the trapezoid rule)
    with the *central difference* $(\Phi(\varepsilon + \delta) - \Phi(\varepsilon -
    \delta))/(2\delta)$, $\delta = 10^{-4}$, at seven energies, and with the
    value $(1 - e^{-2ML})/(2M)$ at $\varepsilon = 0$, where the shot is exactly
    $a = e^{M(y + L)}$, $b = 0$ and the integral can be done by hand. Second, it
    draws the formula over the whole grid together with the central differences of
    the grid of section 7 (spacing 0.02). The slope is about $L = 3$ far from the
    mass. Near $\varepsilon = 0$ it is about $1/(2M) = 0.5$: there the shot grows
    like $e^{M(y + L)}$ and is largest at the fold, so $r(0)^2$ is large. Near
    $|\varepsilon| = 1.34$ it is much larger, about 12.5: there the shot ends with a
    small $r(0)$ compared with its size inside the interval, so a small change of
    energy turns the end angle a lot, and the staircase climbs steeply.
    """),
    code(r'''
    DELTA = 1e-4  # the half-width of the central difference
    tested = [-4.0, -1.34, -0.5, 0.0, 0.7, 1.3, 3.0]  # seven energies
    relative = []
    for e in tested:
        formula = shoot(e, M1, L3, 900)[1]  # element 1 of the result: the slope
        central = (shoot(e + DELTA, M1, L3, 900)[0]
                   - shoot(e - DELTA, M1, L3, 900)[0]) / (2 * DELTA)
        relative.append(abs(central / formula - 1))
        say(f"eps = {e:+.2f}: formula {formula:9.5f}, central difference {central:9.5f}")
    report("largest relative difference formula - central difference",
           f"{max(relative):.1e}")
    check(max(relative) < 1e-4 and np.all(slope_grid > 0),
          "dPhi/deps = f (integral of r^2)/r(0)^2 > 0 (agrees with central "
          "differences)")
    # At eps = 0 the shot is exactly a = e^(M(y + L)), b = 0, so the integral can be
    # done by hand: (e^(2ML) - 1)/(2M) divided by r(0)^2 = e^(2ML).
    at_zero = (1 - math.exp(-2 * M1 * L3)) / (2 * M1)
    report("slope at eps = 0: formula, exact (1 - e^(-2ML))/(2M)",
           f"{shoot(0.0, M1, L3, 900)[1]:.6f}, {at_zero:.6f}")
    check(abs(shoot(0.0, M1, L3, 900)[1] - at_zero) < 1e-4,
          "at eps = 0 the slope is (1 - e^(-2ML))/(2M), about 1/(2M)")

    grid_difference = (Phi_grid[2:] - Phi_grid[:-2]) / (eps_grid[2:] - eps_grid[:-2])
    fig, ax = plt.subplots()
    ax.plot(eps_grid, slope_grid, color=BLACK, lw=1.4,
            label="formula $f \\int r^2 dy / r(0)^2$, $f = 1$")
    ax.plot(eps_grid[1:-1][::6], grid_difference[::6], "o", color=AQUA, ms=4,
            label="central differences of the staircase")
    ax.axhline(L3, color=GREY, ls="--", lw=1.0, label="$L = 3$")
    ax.set_ylim(0.0, 17.5)  # room for the legend above the two peaks
    ax.set_xlabel("energy $\\varepsilon$ (units $m$)")
    ax.set_ylabel("$d\\Phi/d\\varepsilon$ (units $1/m$)")
    ax.set_title("The slope of the staircase is never negative")
    ax.legend(loc="upper right", fontsize=8)
    save_figure(fig, "staircase_slope",
                "The slope $d\\Phi/d\\varepsilon$ of the end angle (vertical axis, "
                "units $1/m$) against the energy $\\varepsilon$ in units of $m$ "
                "(horizontal axis), for $M = 1$, $L = 3$, $f = 1$, 900 RK4 steps. "
                "Black line: the formula $f \\int r^2 dy / r(0)^2$ proved with the "
                "product rule; aqua dots: central differences of the staircase of the "
                "previous figure. The slope is positive everywhere, which is why each "
                "level is crossed once. It is about $L = 3$ (dashed) far from the "
                "mass, about $1/(2M) = 0.5$ near $\\varepsilon = 0$, where the shot "
                "grows towards the fold, and large near $|\\varepsilon| = 1.34$, where "
                "the shot ends with a small $r(0)$ and the staircase climbs steeply.")
    '''),
    md(r"""
    ## 9. The angle along the interval

    For five of the levels the next cell keeps the whole path and draws
    $\theta(y)/\pi$ from the tip $y = -3$ to the fold $y = 0$. Each curve starts
    at $0$ and ends exactly on its target; the number of half-turns it makes is the
    label. The zero mode stays at $\theta = 0$ all the way ($b = 0$ everywhere).
    """),
    code(r'''
    chosen = [("even", 0), ("odd", 0), ("even", 1), ("odd", 1), ("even", 3)]
    level_of = {(r["parity"], int(r["label"])): float(r["eps_numeric"]) for r in canonical}
    fig, ax = plt.subplots()
    for (parity, label), color in zip(chosen, [BLACK, ORANGE, BLUE, VIOLET, AQUA]):
        eps = level_of[(parity, label)]
        y_path, a_path, b_path, theta_path = shoot(eps, M1, L3, 900, keep=True)[3]
        ax.plot(y_path, theta_path / math.pi, color=color, lw=1.5,
                ls="-" if parity == "even" else "--",
                label=f"{parity} $l = {label}$, $\\varepsilon = {eps:.4f}$")
        ax.plot([0.0], [target(parity, label) / math.pi], "o", color=color, ms=6)
    ax.set_xlabel("hidden coordinate $y$ (units $1/H$): tip at $-3$, fold at $0$")
    ax.set_ylabel("Pruefer angle $\\theta(y)/\\pi$")
    ax.set_title("The angle winds up to its target at the fold")
    ax.legend(loc="upper left", fontsize=8)
    save_figure(fig, "angle_along_y",
                "The Pruefer angle $\\theta(y)$ in units of $\\pi$ (vertical axis) "
                "along the hidden coordinate $y$ from the tip $y = -3$ to the fold "
                "$y = 0$ (horizontal axis, units $1/H$) for five levels of the case "
                "$M = 1$, $L = 3$, $f = 1$: the zero mode (black, stays at 0), the odd "
                "label 0 "
                "(1.2923, ends at $\\pi/2$), the even label 1 (1.4480, ends at $\\pi$), "
                "the odd label 1 (2.0106, ends at $3\\pi/2$) and the even label 3 "
                "(3.2969, ends at $3\\pi$). Solid lines are even, dashed lines odd "
                "orbitals; every curve starts at 0 and ends on its target (dots).")
    '''),
    md(r"""
    ## 10. The exact levels, computed again

    The odd levels need the roots $p$ of $\tan(p\ell) = -p/M$, with the proper
    length $\ell = fL$, which we write as $M\sin(p\ell) + p\cos(p\ell) = 0$ (no
    infinities). The $n$-th root ($n = 0, 1, 2, \dots$) lies between
    $(n + \frac{1}{2})\pi/\ell$ and $(n + 1)\pi/\ell$, where the left side changes
    sign. The cell solves them with mpmath at 30 digits, forms all 72 exact levels
    of the table (labels $-3$ to $5$ of both parities, for
    $(M, L, a_4) = (1, 3, 0), (1, 2, 0), (2, 3, 0)$ with $f = 1$ and
    $(1, 3, 1.5)$ with $f = e^{-1/2}$; the odd label $l \ge 0$ uses the root $p_l$
    and $l \le -1$ the root $p_{-l-1}$ with the minus sign) and compares them with
    the record's column `eps_analytic`. The figure shows the graphical solution for
    $M = 1$, $\ell = 3$.
    """),
    code(r'''
    mpmath.mp.dps = 30


    def odd_root(M, ell, n):
        """The n-th positive root p of M sin(p ell) + p cos(p ell) = 0 (30 digits)."""
        g = lambda p: M * mpmath.sin(p * ell) + p * mpmath.cos(p * ell)  # noqa: E731
        return mpmath.findroot(g, ((n + 0.5) * mpmath.pi / ell,
                                   (n + 1) * mpmath.pi / ell), solver="anderson")


    def exact_level(M, ell, parity, label):
        """The exact level of the given parity and label for the proper length ell."""
        if parity == "even":
            if label == 0:
                return 0.0  # the zero mode
            return math.copysign(
                float(mpmath.sqrt(M ** 2 + (label * mpmath.pi / ell) ** 2)), label)
        n = label if label >= 0 else -label - 1
        value = float(mpmath.sqrt(M ** 2 + odd_root(M, ell, n) ** 2))
        return value if label >= 0 else -value


    analytic_ours = [exact_level(float(r["m"]),
                                 hidden_scale(float(r["a4"])) * float(r["L"]),
                                 r["parity"], int(r["label"])) for r in ROWS]
    analytic_record = [float(r["eps_analytic"]) for r in ROWS]
    worst_analytic = max(abs(a - b) for a, b in zip(analytic_ours, analytic_record))
    report("largest |exact level (here) - eps_analytic (record)|", f"{worst_analytic:.1e}")
    check(worst_analytic < 1e-14, "all 72 exact levels equal the column eps_analytic",
          record=f"{TABLE}, column eps_analytic")

    p_axis = np.linspace(0.01, 3.3, 3000)
    tangent = np.tan(p_axis * L3)
    tangent[np.abs(tangent) > 8] = np.nan  # do not draw the jumps at the poles
    fig, ax = plt.subplots()
    ax.plot(p_axis, tangent, color=BLUE, lw=1.4,
            label="$\\tan(p\\ell)$, $\\ell = fL = 3$")
    ax.plot(p_axis, -p_axis / M1, color=ORANGE, lw=1.4, ls="--", label="$-p/M$, $M = 1$")
    for n in range(3):
        p_n = float(odd_root(M1, L3, n))
        ax.plot([p_n], [-p_n], "o", color=BLACK, ms=6)
        ax.annotate(f"$p_{n} = {p_n:.4f}$", (p_n, -p_n), textcoords="offset points",
                    xytext=(6, -14), fontsize=8)
    ax.axhline(0.0, color=BLACK, lw=0.6)
    ax.set_ylim(-6.0, 6.0)
    ax.set_xlabel("$p$ (units $m$)")
    ax.set_ylabel("value of each side")
    ax.set_title("Odd levels: $\\tan(p\\ell) = -p/M$, then "
                 "$\\varepsilon = \\sqrt{M^2 + p^2}$")
    ax.legend(loc="upper right", fontsize=8)
    save_figure(fig, "odd_level_equation",
                "The equation of the odd levels for $M = 1$ and the proper length "
                "$\\ell = fL = 3$ ($f = 1$, $L = 3$): the branches of $\\tan(p\\ell)$ "
                "(solid blue) and the line $-p/M$ (dashed orange) against $p$ in "
                "units of $m$ (horizontal axis; the vertical axis is the value of each "
                "side, a pure number). Each crossing, one on every branch between "
                "$(n + 1/2)\\pi/\\ell$ and $(n + 1)\\pi/\\ell$, is a root $p_n$ and "
                "gives the two odd levels $\\pm\\sqrt{M^2 + p_n^2}$; the first three "
                "give 1.2923, 2.0106 and 2.9119.")
    '''),
    md(r"""
    ## 11. Newton's method with a safety net: the program's root finder

    To find a level we must solve $F(\varepsilon) = \Phi(\varepsilon) - t = 0$ for
    its target $t$. **Newton's method** replaces $F$ by its tangent line at the
    current guess $\varepsilon_c$, $F(\varepsilon) \approx F(\varepsilon_c) +
    F'(\varepsilon_c)(\varepsilon - \varepsilon_c)$, and takes the zero of that line
    as the next guess:

    $$\varepsilon_{\rm new} = \varepsilon_c - \frac{F(\varepsilon_c)}
    {F'(\varepsilon_c)}, \qquad F'(\varepsilon) = \frac{d\Phi}{d\varepsilon} =
    \frac{f}{r(0)^2}\int_{-L}^{0} r^2\,dy .$$

    Close to the root the number of correct digits roughly doubles at every step.
    Far from it the tangent can point anywhere, so the Rust program (function
    `find_level` in Revision/kohn_sham/solver/src/shoot.rs) adds a safety net:

    1. Shoot at the starting guess $\varepsilon = 0$; if $F(0) = 0$ exactly (the zero
       mode), stop.
    2. Make a bracket: walk upwards (if $F < 0$) or downwards (if $F > 0$) with a
       first step of 1.2 times Newton's estimate (at least $10^{-4}$, at most 2),
       doubling the step until $F$ changes sign.
    3. Newton steps inside the bracket; whenever Newton's point falls outside the
       bracket, or the mismatch $|F|$ has not at least halved since the last step,
       bisect instead. After each shot the bracket shrinks to the side that keeps
       the sign change.
    4. Stop when the bracket is narrower than the tolerance $10^{-13}$, or when a
       Newton step is smaller than it.

    The next cell writes this down in Python, step for step as in the Rust code,
    and compares it with plain bisection (bracket $-12$ to $12$, halved until it is
    narrower than $10^{-13}$) on the even level with label 3 of the case $M = 1$,
    $L = 3$, $f = 1$: the figure shows the error of every energy that is shot.
    """),
    code(r'''
    def find_level(M, L, G, goal, f=1.0, tolerance=ROOT_TOLERANCE, log=None):
        """The energy with Phi(eps) = goal (hidden scale f), found as the Rust program
        finds it.  If log is a list, every energy that is shot is appended to it."""
        def mismatch(eps):
            Phi, slope, largest = shoot(eps, M, L, G, f=f)
            if largest >= 2.0:  # the program refuses such a shot
                raise ValueError(f"one step turns the angle by {largest:.2f}")
            if log is not None:
                log.append(eps)
            return Phi - goal, slope  # F(eps) and F'(eps)

        e_c = 0.0  # step 1: the starting guess
        F_c, dF_c = mismatch(e_c)
        if F_c == 0.0:
            return e_c
        if F_c < 0.0:  # step 2, upwards: the level lies above
            low = e_c
            step = min(max(1.2 * (-F_c / dF_c), 1e-4), 2.0)
            while True:
                e = low + step
                F, dF = mismatch(e)
                if F >= 0.0:  # the sign changed: the bracket is (low, e)
                    high = e
                    if abs(F) < abs(F_c):  # keep the better of the two guesses
                        e_c, F_c, dF_c = e, F, dF
                    break
                low, e_c, F_c, dF_c = e, e, F, dF  # still below: move on
                step *= 2.0
        else:  # step 2, downwards: the level lies below
            high = e_c
            step = min(max(1.2 * (F_c / dF_c), 1e-4), 2.0)
            while True:
                e = high - step
                F, dF = mismatch(e)
                if F <= 0.0:  # the sign changed: the bracket is (e, high)
                    low = e
                    if abs(F) < abs(F_c):
                        e_c, F_c, dF_c = e, F, dF
                    break
                high, e_c, F_c, dF_c = e, e, F, dF
                step *= 2.0
        if F_c == 0.0:
            return e_c
        previous = math.inf  # |F| at the previous step
        for _ in range(300):  # step 3
            if high - low <= tolerance:  # step 4: the bracket is narrow enough
                break
            e_new = e_c - F_c / dF_c  # Newton's point
            bisect = not (low < e_new < high) or abs(F_c) > 0.5 * previous
            if bisect:
                e_new = 0.5 * (low + high)  # the safety net
            previous = abs(F_c)
            F, dF = mismatch(e_new)
            moved = abs(e_new - e_c)
            e_c, F_c, dF_c = e_new, F, dF
            if F == 0.0:
                break
            if F < 0.0:  # keep the half of the bracket with the sign change
                low = e_new
            else:
                high = e_new
            if moved <= tolerance and not bisect:  # step 4: a tiny Newton step
                break
        return e_c


    def find_level_by_bisection(M, L, G, goal, tolerance=ROOT_TOLERANCE, log=None):
        """The same level by plain bisection on the bracket (-12, 12)."""
        low, high = -12.0, 12.0
        while high - low > tolerance:
            middle = 0.5 * (low + high)
            if log is not None:
                log.append(middle)
            if shoot(middle, M, L, G)[0] < goal:
                low = middle
            else:
                high = middle
        return 0.5 * (low + high)


    newton_log, bisection_log = [], []
    by_newton = find_level(M1, L3, 900, target("even", 3), log=newton_log)
    by_bisection = find_level_by_bisection(M1, L3, 900, target("even", 3),
                                           log=bisection_log)
    report("even label 3 by Newton", f"{by_newton:.15f} ({len(newton_log)} shots)")
    report("even label 3 by bisection",
           f"{by_bisection:.15f} ({len(bisection_log)} shots)")
    for k, e in enumerate(newton_log, 1):
        say(f"Newton shot {k}: eps = {e:.15f}, error {abs(e - by_newton):.1e}")
    fig, ax = plt.subplots()
    ax.semilogy(range(1, len(bisection_log) + 1),
                np.maximum(np.abs(np.array(bisection_log) - by_newton), 1e-17), "s-",
                color=ORANGE, ms=4, lw=1.2, label="bisection on $(-12, 12)$")
    ax.semilogy(range(1, len(newton_log) + 1),
                np.maximum(np.abs(np.array(newton_log) - by_newton), 1e-17), "o-",
                color=BLUE, ms=5, lw=1.2, label="the program's Newton with safety net")
    ax.set_ylim(1e-17, 30.0)
    ax.set_xlabel("number of the shot")
    ax.set_ylabel("$|\\varepsilon - \\varepsilon_3|$ (units $m$)")
    ax.set_title("Finding the even level $l = 3$ ($M = 1$, $L = 3$)")
    ax.legend(loc="upper right", fontsize=8)
    save_figure(fig, "newton_vs_bisection",
                "The distance $|\\varepsilon - \\varepsilon_3|$ (units of $m$, "
                "logarithmic vertical axis) of every energy that is shot from the "
                "even level with label 3, $\\varepsilon_3 = 3.2969$, of the case "
                "$M = 1$, $L = 3$, against the number of the shot (horizontal axis). "
                "Squares: bisection, which halves the bracket $(-12, 12)$ at every "
                "shot and needs 48 shots to reach the tolerance $10^{-13}$. Circles: "
                "the Rust program's root finder, which first walks up from 0 to make "
                "a bracket and then takes Newton steps; once close, each step about "
                "doubles the number of correct digits, and it stops after 9 shots. "
                "Distances of exactly zero are drawn at $10^{-17}$.")
    check(abs(by_newton - level_of[("even", 3)]) < 1e-12
          and abs(by_bisection - by_newton) < 1e-13
          and len(newton_log) < 15 < 45 < len(bisection_log),
          "Newton (fewer than 15 shots) gives the record's level; bisection agrees",
          record=f"{TABLE}, column eps_numeric")
    '''),
    md(r"""
    ## 12. All 72 levels, against the Rust program

    Now the whole table. For each row the cell computes the hidden scale $f$ from
    the row's $a_4$ with `hidden_scale` and compares it, written as the program
    writes numbers (16 significant digits, exponents like `e0`), with the
    record's column `f`. Then it takes the target of the row's parity and label and
    finds the energy with `find_level`, with the program's number of RK4 steps
    $G = 900 L/3$ (900 for $L = 3$, 600 for $L = 2$: the same step $h = 1/300$)
    and the row's $f$. It writes every level in the program's format and compares
    the text with the record's column `eps_numeric`. On the computer that made the
    record all 72 are identical; on another computer the function atan2 or exp of
    the system's mathematics library may round differently in the last binary
    place, and a last digit may differ, so the check asks for agreement within
    $10^{-12}$ (ten times the root tolerance). The record keeps 16 digits, so even
    an identical level differs from the number read back from the record by up to
    about $10^{-15}$.

    Then it recomputes the two numbers that the program's check
    `free_k0_analytic_spectra` quotes: the largest $|\varepsilon_{\rm numeric} -
    \varepsilon_{\rm exact}|$ for $|\varepsilon| < 4m$ and for $|\varepsilon| \ge
    4m$ (the Rust code, file Revision/kohn_sham/solver/src/spectrum.rs, puts every
    level with $|\varepsilon| \ge 4m$ into the second band; the table goes up to
    $9.61m$).
    """),
    code(r'''
    def rust_text(x):
        """x written as the Rust program writes numbers: 16 digits, exponent like e0."""
        mantissa, exponent = f"{x:.15e}".split("e")  # Python writes e+00, Rust e0
        return f"{mantissa}e{int(exponent)}"


    scales = [hidden_scale(float(r["a4"])) for r in ROWS]  # f of every row
    f_identical = sum(rust_text(f) == r["f"] for f, r in zip(scales, ROWS))
    report("rows whose f (here) equals the column f in all 16 digits", f"{f_identical}"
           f" of {len(ROWS)}")
    numeric_ours, shots_per_level = [], []
    for r, f in zip(ROWS, scales):
        M, L = float(r["m"]), float(r["L"])
        G = round(G_CANONICAL * L / 3.0)  # 900 steps for L = 3, 600 for L = 2
        log = []
        numeric_ours.append(find_level(M, L, G, target(r["parity"], int(r["label"])),
                                       f=f, log=log))
        shots_per_level.append(len(log))
    numeric_record = [float(r["eps_numeric"]) for r in ROWS]
    identical = sum(rust_text(x) == r["eps_numeric"] for x, r in zip(numeric_ours, ROWS))
    worst_numeric = max(abs(a - b) for a, b in zip(numeric_ours, numeric_record))
    report("levels whose 16 digits equal the column eps_numeric", f"{identical} of 72")
    report("largest |level (here) - eps_numeric (Rust program)|", f"{worst_numeric:.1e}")
    report("shots per level (fewest, most, all 72 together)",
           f"{min(shots_per_level)}, {max(shots_per_level)}, {sum(shots_per_level)}")
    check(max(abs(f - float(r["f"])) for f, r in zip(scales, ROWS)) < 1e-15
          and worst_numeric < 1e-12 and max(shots_per_level) <= 20,
          "the hidden scales and all 72 shooting levels equal the columns f and "
          "eps_numeric (at most 20 shots each)",
          record=f"{TABLE}, columns f and eps_numeric")
    zero_rows = [i for i, r in enumerate(ROWS) if r["parity"] == "even"
                 and int(r["label"]) == 0]
    check(all(numeric_ours[i] == 0.0 == numeric_record[i] for i in zero_rows),
          "the zero mode has the energy exactly 0 in all four cases",
          record=f"{SOLVER_REPORT}, check free_zero_mode_exact")

    differences_ours = [n - a for n, a in zip(numeric_ours, analytic_ours)]
    pairs = list(zip(differences_ours, analytic_ours))
    low_band = max(abs(d) for d, a in pairs if abs(a) < 4)  # all levels below 4 m
    high_band = max(abs(d) for d, a in pairs if abs(a) >= 4)  # all levels from 4 m on
    top = max(abs(a) for _, a in pairs)  # the highest level of the table
    report("the highest level of the table (units m)", f"{top:.4f}")
    solver_report = json.loads(repository_file(SOLVER_REPORT).read_text(encoding="utf-8"))
    detail = [c["detail"] for c in solver_report["checks"]
              if c["name"] == "free_k0_analytic_spectra"][0]
    quoted = float(re.findall(r"max \|difference\| ([0-9.]+e-[0-9]+) for \|eps\| < 4 m",
                              detail)[0])
    quoted_high = float(re.findall(r"([0-9.]+e-[0-9]+) for \|eps\| >= 4 m",
                                   detail)[0])
    report("largest |numeric - exact| for |eps| < 4 m (here, record)",
           f"{low_band:.2e}, {quoted:.2e}")
    report("largest |numeric - exact| for |eps| >= 4 m (here, record)",
           f"{high_band:.2e}, {quoted_high:.2e}")
    check(abs(low_band / quoted - 1) < 0.005 and abs(high_band / quoted_high - 1) < 0.005,
          "the two largest differences quoted by the solver check are reproduced",
          record=f"{SOLVER_REPORT}, check free_k0_analytic_spectra")
    '''),
    md(r"""
    ## 13. The orbitals

    The next cell builds the normalised orbitals of four levels of the canonical
    case as the Rust program builds them (function `profile` in shoot.rs): the
    values at the $G + 1$ step ends (*nodes*) come from the RK4 shot; the values in
    the middle of every step from *cubic interpolation*: the cubic polynomial that
    has the values $f_0, f_1$ and the slopes $f_0', f_1'$ at the two ends of a step
    of length $h$ takes in the middle the value $(f_0 + f_1)/2 + h(f_0' - f_1')/8$
    (check it on $f = y^2$ and $f = y^3$ on the step from 0 to $h$); the slopes
    come from the equations themselves. On this fine grid of $2G + 1$ points the
    norm $\int_{-L}^{0} (a^2 + b^2)\, dy$ is computed with Simpson's rule (weights
    $1, 4, 2, 4, \dots, 4, 1$ times one third of the spacing $h/2$), and the orbital
    is divided by its square root. The cell draws $a(y)$ and $b(y)$ for $f = 1$,
    checks the fold condition of each ($b(0) = 0$ even, $a(0) = 0$ odd), and
    measures how far the computed zero mode is from its exact form
    $a = \sqrt{2fM/(1 - e^{-2fML})}\, e^{f M y}$, $b = 0$ (the normalised
    $e^{fMy}$), as the program's check `free_zero_mode_exact` does: at $a_4 = 0$
    ($f = 1$) and at $a_4 = 2$ on the history ($f = e^{-2/3}$); the check quotes
    the larger of the two distances.
    """),
    code(r'''
    def orbital(eps, M, L, G, f=1.0):
        """The normalised orbital on the fine grid of 2G + 1 points, made as the Rust
        program makes it.  Returns the arrays y, a, b."""
        h = L / G
        nf = 2 * G + 1  # nodes and step midpoints
        y = -L * ((nf - 1 - np.arange(nf)) / (nf - 1))  # the fine grid, as in the program
        _, a_nodes, b_nodes, _ = shoot(eps, M, L, G, f=f, keep=True)[3]
        fM, fe = f * M, f * eps
        da = fM * a_nodes - fe * b_nodes  # the slopes a' at the nodes (the equations)
        db = fe * a_nodes - fM * b_nodes  # the slopes b'
        a, b = np.zeros(nf), np.zeros(nf)
        a[0::2], b[0::2] = a_nodes, b_nodes  # the nodes take the even places
        a[1::2] = 0.5 * (a_nodes[:-1] + a_nodes[1:]) + h / 8.0 * (da[:-1] - da[1:])
        b[1::2] = 0.5 * (b_nodes[:-1] + b_nodes[1:]) + h / 8.0 * (db[:-1] - db[1:])
        half = 0.5 * h  # the spacing of the fine grid
        weights = np.full(nf, 2.0 * half / 3.0)  # Simpson: 2 at the even inner places
        weights[1::2] = 4.0 * half / 3.0  # 4 at the odd places (the midpoints)
        weights[0] = weights[-1] = half / 3.0  # 1 at the two ends
        scale = 1.0 / math.sqrt(np.sum(weights * (a * a + b * b)))
        return y, a * scale, b * scale


    fig, axes = plt.subplots(2, 2, figsize=(9.0, 6.4), sharex=True)
    residuals = []
    for ax, (parity, label) in zip(axes.flat, [("even", 0), ("odd", 0), ("even", 1),
                                              ("odd", 2)]):
        eps = level_of[(parity, label)]
        y_fine, a_fine, b_fine = orbital(eps, M1, L3, 900)
        end = b_fine[-1] if parity == "even" else a_fine[-1]  # must vanish at y = 0
        residuals.append(abs(end))
        ax.plot(y_fine, a_fine, color=BLUE, lw=1.5, label="$a(y)$")
        ax.plot(y_fine, b_fine, color=ORANGE, lw=1.5, ls="--", label="$b(y)$")
        ax.axhline(0.0, color=BLACK, lw=0.6)
        ax.set_title(f"{parity}, $l = {label}$, $\\varepsilon = {eps:.4f}$", fontsize=10)
        ax.legend(fontsize=8, loc="upper left")
    for ax in axes[1]:
        ax.set_xlabel("hidden coordinate $y$ (units $1/H$)")
    for ax in axes[:, 0]:
        ax.set_ylabel("component (units $H^{1/2}$)")
    save_figure(fig, "orbitals",
                "The normalised orbitals of four levels of the case $M = 1$, $L = 3$, "
                "$f = 1$: the components $a(y)$ (solid blue) and $b(y)$ (dashed orange) "
                "against the hidden coordinate $y$ from the tip $-3$ to the fold $0$ "
                "(horizontal axes, units $1/H$; vertical axes in units of $H^{1/2}$, so "
                "that $\\int (a^2 + b^2) dy = 1$). Top left: the zero mode "
                "$a \\propto e^{y}$, $b = 0$, concentrated at the fold. Top right: odd "
                "label 0. Bottom: even label 1 and odd label 2. Every orbital has "
                "$b = 0$ at the tip; at the fold the even ones have $b = 0$ and the "
                "odd ones $a = 0$.")
    report("largest fold residual |b(0)| or |a(0)|", f"{max(residuals):.1e}")
    zero_distance, zero_b = [], []  # at a4 = 0 (f = 1) and a4 = 2 (f = e^(-2/3))
    for a4 in (0.0, 2.0):
        f = hidden_scale(a4)
        eps0 = find_level(M1, L3, 900, target("even", 0), f=f)  # the zero mode
        y_fine, a_fine, b_fine = orbital(eps0, M1, L3, 900, f=f)
        fM = f * M1
        exact_a = math.sqrt(2.0 * fM / (1.0 - math.exp(-2.0 * fM * L3))) * np.exp(
            fM * y_fine)  # the exact normalised zero mode
        zero_distance.append(np.max(np.abs(a_fine - exact_a)))
        zero_b.append(np.max(np.abs(b_fine)) + abs(eps0))
    zero_detail = [c["detail"] for c in solver_report["checks"]
                   if c["name"] == "free_zero_mode_exact"][0]
    zero_quoted = float(re.findall(r"e\^\(fMy\) to ([0-9.]+e-[0-9]+)", zero_detail)[0])
    report("zero mode: distance from the exact form at a4 = 0, at a4 = 2 (here); record",
           f"{zero_distance[0]:.2e}, {zero_distance[1]:.2e}; {zero_quoted:.2e}")
    check(max(residuals) < 1e-10, "every orbital meets its fold condition within 1e-10")
    check(max(zero_b) == 0.0 and abs(max(zero_distance) / zero_quoted - 1) < 0.01,
          "the zero mode: eps = 0 and b = 0 exactly, distance 1.35e-12 from "
          "sqrt(2fM/(1 - e^(-2fML))) e^(fMy)",
          record=f"{SOLVER_REPORT}, check free_zero_mode_exact")
    '''),
    md(r"""
    ## 14. How the error depends on the step

    The levels inherit the RK4 error. The next cell repeats the search for three
    levels of the canonical case with $G = 25, 50, 100, 200, 400, 800$ steps and
    draws the error against the step $h = L/G$ (log-log; the slope is the order).
    """),
    code(r'''
    G_LIST = [25, 50, 100, 200, 400, 800]
    tracked = [("even", 1), ("odd", 2), ("even", 5)]
    fig, ax = plt.subplots()
    orders = []
    for (parity, label), color, marker in zip(tracked, [BLUE, ORANGE, AQUA],
                                              ["o", "s", "^"]):
        exact = exact_level(M1, L3, parity, label)
        errors = np.array([abs(find_level(M1, L3, G, target(parity, label)) - exact)
                           for G in G_LIST])
        h_list = L3 / np.array(G_LIST, dtype=float)
        fit = errors > 1e-11  # leave out points limited by the root tolerance
        orders.append(np.polyfit(np.log10(h_list[fit]), np.log10(errors[fit]), 1)[0])
        ax.loglog(h_list, errors, marker=marker, color=color, ms=5, lw=1.2,
                  label=f"{parity} $l = {label}$ ($\\varepsilon = {exact:.4f}$)")
    h_guide = L3 / np.array(G_LIST, dtype=float)
    ax.loglog(h_guide, 2e-3 * (h_guide / h_guide[0]) ** 4, "--", color=GREY,
              label="slope 4")
    ax.axvline(L3 / 900, color=BLACK, ls=":", lw=1.0)
    ax.text(L3 / 900 * 1.08, 1e-4, "the record's\nstep 1/300", fontsize=8)
    ax.set_xlabel("RK4 step $h = L/G$ (units $1/H$)")
    ax.set_ylabel("error of the level (units $m$)")
    ax.set_title("The levels converge like $h^4$")
    ax.legend(loc="lower right", fontsize=8)
    save_figure(fig, "level_convergence",
                "The error of three levels of the case $M = 1$, $L = 3$ found by "
                "shooting, against the RK4 step $h = L/G$ for $G = 25$ to 800 steps "
                "(logarithmic axes; the error in units of $m$, the step in units of "
                "$1/H$): even label 1 (circles), odd label 2 (squares), even label 5 "
                "(triangles). The points follow lines of slope 4 (dashed guide): the "
                "levels have the order of RK4, and higher levels have larger errors. "
                "The dotted line marks the record's step $1/300$.")
    report("measured orders", ", ".join(f"{q:.2f}" for q in orders))
    check(all(3.8 < q < 4.2 for q in orders), "the level errors fall like h^4")
    '''),
    md(r"""
    **Why the error grows with the level.** Far from the mass, $\theta' \approx
    f\varepsilon$: the point $(a, b)$ turns at the rate $f\varepsilon$ (forwards
    for $\varepsilon > 0$, backwards for $\varepsilon < 0$). One RK4 step
    multiplies a turning point by $R(i\omega)$ with $\omega = f\varepsilon h$ (the
    amplification factor of the test equation $y' = i f\varepsilon y$), whose
    angle is a little SMALLER IN SIZE than the exact $\omega$. The next cell lets
    sympy expand the angle of $R(i\omega)$: it is $\omega - \omega^5/120 + \dots$
    (for $\omega < 0$ too, because the angle of $R(-i|\omega|)$ is minus that of
    $R(i|\omega|)$). After $G = L/h$ steps the computed end angle differs by about
    $-L\, f^5 \varepsilon^5 h^4/120$ from the exact one: it is too small for
    $\varepsilon > 0$ and too large for $\varepsilon < 0$. Since $\Phi$ grows by
    about $fL$ per unit of energy, the computed level must move AWAY FROM ZERO by

    $$\delta\varepsilon \approx \frac{f^4 \varepsilon^5 h^4}{120}, \qquad
    \frac{\delta\varepsilon}{\varepsilon} \approx \frac{(f h\varepsilon)^4}{120}$$

    to make up for it ($\varepsilon^5$ has the sign of $\varepsilon$): positive
    levels come out too high, negative levels too low, both too large in size.
    The cell checks this sign in the record's column `difference`. The figure draws
    the relative error $|\delta\varepsilon/\varepsilon|$ of all 68 nonzero levels
    of the record against $f h|\varepsilon|$ with $h = 1/300$, with our own
    differences on top, and this prediction as a line. Close to the mass the point
    does not turn uniformly ($\theta' = f(\varepsilon - M \sin 2\theta)$), and the
    error is smaller than the prediction; far from it the points approach the line.
    """),
    code(r'''
    w = sp.symbols("omega", positive=True)  # the angle turned in one step, eps h
    R_rk4 = 1 + sp.I * w - w ** 2 / 2 - sp.I * w ** 3 / 6 + w ** 4 / 24  # R(i omega)
    turned = sp.atan(sp.im(R_rk4) / sp.re(R_rk4))  # the angle of R(i omega)
    lag = sp.series(turned - w, w, 0, 7).removeO()
    say(f"angle of R(i omega) - omega = {lag} + ...")
    check(sp.simplify(lag + w ** 5 / 120) == 0,
          "one RK4 step turns by omega - omega^5/120: the phase lags")

    nonzero = [i for i, a in enumerate(analytic_record) if a != 0.0]
    eps_abs = np.array([abs(analytic_record[i]) for i in nonzero])
    f_rows = np.array([scales[i] for i in nonzero])  # the hidden scale of each level
    x_values = f_rows * eps_abs / 300.0  # f h |eps| with h = 1/300
    record_diff = np.array([abs(float(ROWS[i]["difference"])) for i in nonzero])
    our_diff = np.array([abs(differences_ours[i]) for i in nonzero])
    masses = np.array([float(ROWS[i]["m"]) for i in nonzero])
    GROUPS = [((f_rows == 1.0) & (masses == 1.0), BLUE, "record, $M = 1$, $f = 1$"),
              (masses == 2.0, ORANGE, "record, $M = 2$, $f = 1$"),
              (f_rows < 1.0, AQUA, "record, $M = 1$, $f = e^{-1/2}$")]
    fig, ax = plt.subplots()
    for pick, color, name in GROUPS:
        ax.loglog(x_values[pick], record_diff[pick] / eps_abs[pick], "o", color=color,
                  ms=6, label=name)
    ax.loglog(x_values, our_diff / eps_abs, "x", color=BLACK, ms=5,
              label="this notebook")
    x_guide = np.linspace(x_values.min(), x_values.max(), 50)
    ax.loglog(x_guide, x_guide ** 4 / 120, "--", color=GREY,
              label="prediction $(f h\\varepsilon)^4/120$")
    ax.set_xlabel("$f h |\\varepsilon|$ with $h = 1/300$ (pure number)")
    ax.set_ylabel("relative error $\\delta\\varepsilon / |\\varepsilon|$")
    ax.set_title("The RK4 error of all 68 nonzero levels of the record")
    ax.legend(loc="upper left", fontsize=8)
    save_figure(fig, "record_differences",
                "The relative error $\\delta\\varepsilon/|\\varepsilon|$ of the "
                "shooting levels for all 68 nonzero levels of the Revision record of "
                "the free spectrum (vertical axis, a pure number), against "
                "$f h|\\varepsilon|$ with the record's step $h = 1/300$ and the "
                "hidden scale $f$ of the level (horizontal axis, a pure number), on "
                "logarithmic axes. Dots: the record's column difference divided by "
                "the level, for $M = 1$, $f = 1$ (blue; $L = 3$ and $L = 2$), "
                "$M = 2$ (orange) and $M = 1$, $f = e^{-1/2}$ (aqua); crosses: this "
                "notebook's shooting, which falls on the record's points. Dashed: "
                "the prediction $(f h\\varepsilon)^4/120$ from the phase lag of one "
                "RK4 step; the levels far from the mass approach it, those near the "
                "mass lie below it.")
    ratio = (record_diff / eps_abs) / (x_values ** 4 / 120)
    far = eps_abs > 7  # the levels far from the mass M = 1
    report("error / prediction for the levels above 7 m",
           ", ".join(f"{q:.3f}" for q in ratio[far]))
    check(np.all(ratio < 1) and np.all(ratio[far] > 0.9),
          "every level error lies below the prediction, within 10 % above 7 m")
    report("largest |difference (here) - difference (record)|",
           f"{np.max(np.abs(record_diff - our_diff)):.1e}")
    check(np.max(np.abs(record_diff - our_diff)) < 1e-12,
          "our differences equal the record's column difference within 1e-12",
          record=f"{TABLE}, column difference")
    signed = np.array([float(ROWS[i]["difference"]) for i in nonzero])  # with sign
    levels = np.array([analytic_record[i] for i in nonzero])
    report("computed too high (levels > 0), too low (levels < 0)",
           f"{np.sum((levels > 0) & (signed > 0))} of {np.sum(levels > 0)}, "
           f"{np.sum((levels < 0) & (signed < 0))} of {np.sum(levels < 0)}")
    check(np.all(np.sign(signed) == np.sign(levels)),
          "every computed level lies farther from 0 than the exact one (sign of eps^5)",
          record=f"{TABLE}, columns difference and eps_analytic")
    '''),
    md(r"""
    ## 15. The free levels along the deflating history

    Along the prescribed history of the record ($a_4 = H x_4$,
    $b_4 = e^{(4/3) H x_4}$) the hidden scale is $f = e^{-a_4/3}$: as $a_4$ grows,
    the hidden direction deflates together with the extra times, and the proper
    length $fL$ of the interval shrinks. Section 4 showed that the levels depend on
    $f$ and $L$ only through $fL$, like the levels of a box of length $fL$. The
    next cell computes the exact positive levels of the case $M = 1$, $L = 3$ for
    41 values of $a_4$ from 0 to 2, draws them, marks the record's shooting levels
    at $a_4 = 0$ and $a_4 = 1.5$, and checks that every nonzero level rises along
    the history while the zero mode stays at $\varepsilon = 0$.
    """),
    code(r'''
    a4_axis = np.linspace(0.0, 2.0, 41)
    curves = {("even", 0): [0.0] * len(a4_axis)}  # the zero mode stays at 0
    for label in (0, 1, 2):
        curves[("odd", label)] = [exact_level(M1, hidden_scale(a) * L3, "odd", label)
                                  for a in a4_axis]
    for label in (1, 2, 3):
        curves[("even", label)] = [exact_level(M1, hidden_scale(a) * L3, "even", label)
                                   for a in a4_axis]
    fig, ax = plt.subplots(figsize=(7.0, 5.0))
    for (parity, label), values in sorted(curves.items()):
        is_even = parity == "even"
        ax.plot(a4_axis, values, color=BLUE if is_even else ORANGE, lw=1.5,
                ls="-" if is_even else "--")
        ax.text(2.03, values[-1], f"{parity} {label}", fontsize=7, va="center")
    for r in ROWS:  # the record's shooting levels of the two slices with M = 1, L = 3
        key = (r["parity"], int(r["label"]))
        if float(r["m"]) == 1.0 and float(r["L"]) == 3.0 and key in curves:
            is_even = r["parity"] == "even"
            ax.plot(float(r["a4"]), float(r["eps_numeric"]), "o" if is_even else "s",
                    color=BLUE if is_even else ORANGE, ms=6, mec=BLACK)
    ax.plot([], [], "-", color=BLUE, label="even levels (exact)")
    ax.plot([], [], "--", color=ORANGE, label="odd levels (exact)")
    ax.plot([], [], "o", color=GREY, mec=BLACK, label="record, shooting")
    ax.set_xlim(0.0, 2.35)  # room for the labels on the right
    ax.set_ylim(-0.2, 6.6)
    ax.set_xlabel("$a_4$ along the history ($f = e^{-a_4/3}$)")
    ax.set_ylabel("level $\\varepsilon$ (units $m$)")
    ax.set_title("Free levels at $k = 0$ along the deflating history "
                 "($M = 1$, $L = 3$)")
    ax.legend(loc="upper left", fontsize=8)
    save_figure(fig, "levels_along_history",
                "The positive free levels at $k = 0$ of the case $M = 1$, $L = 3$ "
                "(vertical axis, units of $m$) against $a_4$ from 0 to 2 along the "
                "prescribed history $a_4 = H x_4$, $b_4 = e^{(4/3) H x_4}$ of the "
                "Revision record, on which the hidden scale is $f = e^{-a_4/3}$ "
                "(horizontal axis, a pure number). Solid blue: the even levels "
                "$\\sqrt{M^2 + (n\\pi/(fL))^2}$, $n = 1, 2, 3$, and the zero mode at "
                "0; dashed orange: the odd levels with $\\tan(p f L) = -p/M$; markers: "
                "the record's shooting levels at $a_4 = 0$ and $a_4 = 1.5$. As the "
                "hidden direction deflates, the proper length $fL$ shrinks and every "
                "level except the zero mode rises.")
    rising = all(np.all(np.diff(values) > 0) for key, values in curves.items()
                 if key != ("even", 0))
    first_even = curves[("even", 1)]  # the even level with label 1
    report("even label 1 at a4 = 0 and at a4 = 2 (exact)",
           f"{first_even[0]:.4f}, {first_even[-1]:.4f}")
    zero_on_history = [float(r["eps_numeric"]) for r in ROWS if float(r["a4"]) > 0
                       and r["parity"] == "even" and int(r["label"]) == 0]
    check(rising and zero_on_history == [0.0],
          "along the history every nonzero free level rises; the zero mode stays at 0",
          record=f"{TABLE}, rows with a4 = 1.5")
    '''),
    md(r"""
    ## 16. The last check

    The last cell checks that all 9 figure files exist in the folder
    Revision/textbook/figures and prints the number of checks that passed.
    """),
    code(r'''
    names = ["pruefer_staircase", "staircase_slope", "angle_along_y",
             "odd_level_equation", "newton_vs_bisection", "orbitals",
             "level_convergence", "record_differences", "levels_along_history"]
    present = [output_file(f"{FIGURE_FOLDER}/02d_{k}_{name}.png").is_file()
               for k, name in enumerate(names, 1)]
    check(all(present), f"all {len(names)} figure files of notebook 02d exist")
    all_checks_passed()
    '''),
    md(r"""
    ## 17. What this notebook showed

    - The free Kohn-Sham block of the book in the corrected metric,
      $a' = f(M a - \varepsilon b)$, $b' = f(\varepsilon a - M b)$ with
      $b(-L) = 0$ and $b(0) = 0$ or $a(0) = 0$ at the fold, depends on the hidden
      scale $f$ and the length $L$ only through the proper length $fL$. It has the
      exact levels $0$ (the zero mode $a \propto e^{fMy}$, $b = 0$),
      $\pm\sqrt{M^2 + (n\pi/(fL))^2}$ (even) and $\pm\sqrt{M^2 + p^2}$ with
      $\tan(pfL) = -p/M$ (odd).
    - The Pruefer angle obeys $\theta' = f(\varepsilon - M\sin 2\theta)$, and the
      product rule gives $d\Phi/d\varepsilon = f\int r^2\,dy / r(0)^2 > 0$: the end
      value increases with $\varepsilon$, so each level is the unique crossing of a
      target $l\pi$ or $\pi/2 + l\pi$; no level can be missed and each has a label.
    - The Rust program finds a level with Newton's method (slope from the same
      formula) and a bisection safety net: 9 shots for the even level $l = 3$,
      where plain bisection needs 48.
    - Re-written line by line in Python, the program's shooting (900 RK4 steps for
      $L = 3$) and root finder reproduce all 72 levels of the record
      Revision/kohn_sham/results/spectrum/free-k0-analytic.csv (four cases, one at
      $a_4 = 1.5$ with $f = e^{-1/2}$; on the computer that made the record,
      identical in all 16 printed digits), its columns f and eps_analytic, the zero
      mode exactly, the distance $1.35 \times 10^{-12}$ of the computed zero mode
      from its exact form, and the numbers $7.23 \times 10^{-10}$ (levels below
      $4m$) and $5.05 \times 10^{-8}$ (all levels from $4m$ up) quoted by the
      program's check free_k0_analytic_spectra.
    - The level errors fall like $h^4$; for levels far from the mass the relative
      error is close to $(fh\varepsilon)^4/120$, the phase lag of RK4, and every
      computed level lies farther from zero than the exact one (too high above
      zero, too low below it). The canonical step $h = 1/300$ gives errors below
      $10^{-9}$ for $|\varepsilon| < 4m$.
    - Inside the mass gap $|\varepsilon| \le M$ the only level is the zero mode.
    - Along the deflating history ($f = e^{-a_4/3}$) every nonzero free level at
      $k = 0$ rises, because the proper length $fL$ shrinks; the zero mode stays at
      0.
    - What this notebook does not show: the physics of these equations (where they
      come from, the meaning of the levels, the interacting case); the record
      derives the two fold conditions from the joining of the two halves of a cell
      at the fold and labels the filling of both together ASSUMED, and the tip
      condition is a choice of the model, as the record states; the history along
      which $f$ shrinks is a PRESCRIBED BACKGROUND.
    """),
]

if __name__ == "__main__":
    raise SystemExit(run_builder(__file__))
