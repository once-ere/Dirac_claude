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
(Revision/kohn_sham/solver/src/shoot.rs), taught on its simplest case, the free k = 0
block a' = M a - eps b, b' = eps a - M b on -L <= y <= 0 with the regular tip b(-L) = 0
and the ASSUMED Z2 brane conditions b(0) = 0 (even) or a(0) = 0 (odd).  RK4 with
G = 900 L/3 steps, the Pruefer angle and its winding count, bisection to 1e-13.  It
reproduces every row of Revision/kohn_sham/results/spectrum/free-k0-analytic.csv (54
levels, numeric and analytic) and the numbers of the checks free_k0_analytic_spectra
and free_zero_mode_exact of Revision/kohn_sham/reports/ks-rust-solver.json.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools"))
from nbkit import code, md, run_builder  # noqa: E402

FIGURES = [
    "02d_1_pruefer_staircase",
    "02d_2_angle_along_y",
    "02d_3_odd_level_equation",
    "02d_4_orbitals",
    "02d_5_level_convergence",
    "02d_6_record_differences",
]

FACTS = {
    "id": "02d",
    "name": "02d_pruefer_shooting",
    "title": "Shooting two first-order equations with the Pruefer angle",
    "purpose": (
        "It solves the simplest Kohn-Sham equations of the book, two first-order "
        "equations for the components a and b of an orbital in the hidden coordinate "
        "(constant mass, no momentum, no interaction), as an eigenvalue problem: it "
        "derives the exact levels, shoots with RK4 exactly as the Revision Rust solver "
        "does (900 steps on the interval of length 3, the Pruefer angle and its "
        "winding count, levels to 1e-13), reproduces all 54 levels of the Revision "
        "record of the free spectrum, numeric and exact, and the numbers of the "
        "solver checks of that spectrum and of the zero mode, and measures the "
        "fourth-order convergence of the levels."
    ),
    "records": [
        ["Revision/kohn_sham/ks-theory.json",
         "the block equations in real form, the tip and brane conditions with their "
         "status, and the exact k = 0 spectra (read)"],
        ["Revision/kohn_sham/results/parameters.json",
         "the solver settings: 900 RK4 steps, root tolerance 1e-13, m = H = 1, L = 3 "
         "(read and used)"],
        ["Revision/kohn_sham/results/spectrum/free-k0-analytic.csv",
         "the 54 free k = 0 levels of the Rust solver and their exact values "
         "(reproduced)"],
        ["Revision/kohn_sham/reports/ks-rust-solver.json",
         "the checks free_k0_analytic_spectra and free_zero_mode_exact (reproduced)"],
    ],
    "packages": ["numpy", "sympy", "mpmath", "matplotlib"],
    "needs_rust": [],
    "expected_seconds": 10,
    "timeout_seconds": 400,
    "files_written": ["Revision/textbook/figures/02d.captions.json"]
    + [f"Revision/textbook/figures/{name}.png" for name in FIGURES],
    "final_lines": [
        "PASS all 6 figure files of notebook 02d exist",
        "ALL 15 CHECKS PASSED (notebook 02d)",
    ],
    "troubleshooting": [],
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
      orbital in the hidden coordinate $y$, in the free case (constant mass $M$, no
      3-space momentum, no interaction), with their boundary conditions;
    - derives their exact levels: $\varepsilon = 0$ and $\pm\sqrt{M^2 + (n\pi/L)^2}$
      for the even orbitals, $\pm\sqrt{M^2 + p^2}$ with $\tan(pL) = -p/M$ for the odd
      ones;
    - introduces the **Pruefer angle** $\theta = \mathrm{atan2}(b, a)$, shows that its
      end value grows steadily with the energy, so that every level is found exactly
      once by a whole-number label;
    - shoots with RK4 exactly as the Rust program does (900 steps on an interval of
      length 3) and finds all 54 levels of the record
      Revision/kohn_sham/results/spectrum/free-k0-analytic.csv by bisection to
      $10^{-13}$; it reproduces the program's numbers and the exact numbers of every
      row, and the numbers quoted by the program's checks of this spectrum;
    - draws the staircase of the Pruefer angle, the winding of the angle along $y$,
      the orbitals, and the fourth-order convergence of the levels.

    It draws 6 figures and prints a PASS line for every check.
    """),
    md(r"""
    ## 3. The words used in this notebook

    - **Orbital**: a single-particle state of the Kohn-Sham model. Here it is
      described by two real functions $a(y)$ and $b(y)$, its *components*.
    - **Hidden coordinate** $y$: the book's coordinate along the hidden direction
      $x_8$, $y = \ln(\sin z)/(6H)$ with $z = 6 H x_8$; $y = 0$ is the end of the
      patch $z = \pi/2$ (the *brane*), and the interval is cut off at $y = -L$ (the
      *tip*).
    - **Energy level** $\varepsilon$: a value of the energy for which the equations
      have a solution with all boundary conditions; an eigenvalue. Unit: the mass
      $m$ (in units with $m = H = 1$).
    - **Mass** $M$: the constant mass of the free case; here $M = m$.
    - **Boundary conditions**: at the tip $b(-L) = 0$ (the *regular tip*, a choice
      of the model); at the brane $b(0) = 0$ (*even* orbitals) or $a(0) = 0$
      (*odd* orbitals), which follow from the ASSUMED mirror symmetry of the model
      (the record labels it ASSUMED).
    - **Pruefer angle** $\theta(y)$: the angle of the point $(a, b)$ seen from the
      origin, $a = r \cos\theta$, $b = r \sin\theta$ with $r > 0$; we count every
      full turn, so $\theta$ can grow beyond $2\pi$ (*winding*).
    - **atan2(b, a)**: the angle of the point $(a, b)$ between $-\pi$ and $\pi$.
    - **Label** $l$: the whole number that names a level through its target angle,
      $\theta(0) = l\pi$ (even) or $\pi/2 + l\pi$ (odd).
    - **Monotone (increasing)**: a function that grows whenever its argument grows.
    - **RK4 step count** $G$: the number of RK4 steps on $-L \le y \le 0$; the step
      is $h = L/G$.
    - **Transcendental equation**: an equation such as $\tan(pL) = -p/M$ that has no
      solution formula and is solved numerically.
    """),
    md(r"""
    ## 4. The physical and mathematical situation

    **The equations.** The record gives the Kohn-Sham equation of one 2-component
    block in the real form (key `blockEquation.realForm`)
    $a' = M a - (\kappa k + j(\varepsilon - v)) b$,
    $b' = (j(\varepsilon - v) - \kappa k) a - M b$, where the prime is $d/dy$. In the
    free case with no 3-space momentum ($k = 0$), no potential ($v = 0$), constant
    mass $M$ and the block type $j = +1$ they are

    $$a' = M a - \varepsilon b, \qquad b' = \varepsilon a - M b, \qquad
    -L \le y \le 0,$$

    with $b(-L) = 0$ at the tip and $b(0) = 0$ (even) or $a(0) = 0$ (odd) at the
    brane. The record's values are $M = m = 1$, $H = 1$, $L = 3$; the program also
    checks $L = 2$ and $M = 2$. In this notebook we take the equations as given; the
    physics chapters derive them.

    **The exact levels.** Step 1: from the first equation, $b = (M a - a')/\varepsilon$
    (for $\varepsilon \ne 0$). Step 2: differentiate: $b' = (M a' - a'')/\varepsilon$.
    Step 3: put both into the second equation: $(M a' - a'')/\varepsilon =
    \varepsilon a - M (M a - a')/\varepsilon$. Step 4: multiply by $\varepsilon$:
    $M a' - a'' = \varepsilon^2 a - M^2 a + M a'$. Step 5: cancel $M a'$:

    $$a'' = (M^2 - \varepsilon^2)\, a .$$

    For $|\varepsilon| > M$ put $p = \sqrt{\varepsilon^2 - M^2}$; then $a'' = -p^2 a$
    and $a = \cos(p y + \varphi)$ with a constant $\varphi$. The conditions on $b$
    become conditions on $a$: $b = 0$ means $M a - a' = 0$.

    - Even: $M a - a' = 0$ at BOTH ends. $M\cos(py + \varphi) + p \sin(py +
      \varphi) = R \cos(py + \varphi - \delta)$ with $\tan\delta = p/M$ vanishes at
      $y = 0$ and at $y = -L$ only if the two phases differ by a multiple of $\pi$:
      $pL = n\pi$. So $\varepsilon = \pm\sqrt{M^2 + (n\pi/L)^2}$, $n = 1, 2, \dots$
    - Odd: $a(0) = 0$ gives $a = \sin(py)$; the tip condition $M \sin(-pL) -
      p\cos(-pL) = 0$ gives $\tan(pL) = -p/M$.
    - $\varepsilon = 0$: the equations become $a' = M a$, $b' = -M b$; with
      $b(-L) = 0$ we get $b = 0$ everywhere and $a = e^{M y}$: the *zero mode*, an
      even orbital ($b(0) = 0$) with energy exactly 0.

    **The Pruefer angle.** Write $a = r\cos\theta$, $b = r\sin\theta$. Then
    $\theta' = (a b' - b a')/r^2$ (the derivative of the angle of a moving point).
    Insert the equations: $a b' - b a' = a(\varepsilon a - M b) - b(M a -
    \varepsilon b) = \varepsilon (a^2 + b^2) - 2 M a b$. Divide by $r^2 = a^2 + b^2$
    and use $2ab/r^2 = 2\sin\theta\cos\theta = \sin 2\theta$:

    $$\theta' = \varepsilon - M \sin 2\theta, \qquad \theta(-L) = 0 .$$

    This is ONE first-order equation. Its right-hand side grows with $\varepsilon$,
    so two solutions with $\varepsilon_1 < \varepsilon_2$ that start together at
    $\theta = 0$ can never cross: where they would meet, the one with
    $\varepsilon_2$ climbs faster. Hence the end value $\Phi(\varepsilon) =
    \theta(0)$ increases with $\varepsilon$. The brane conditions say $b(0) = 0$, that
    is $\theta(0) = l\pi$ (even), or $a(0) = 0$, that is $\theta(0) = \pi/2 + l\pi$
    (odd), for a whole number $l$. Each target is reached for exactly one
    $\varepsilon$: every level has its own label $l$ and none can be missed. This
    is how the Rust program finds and names its levels.
    """),
    md(r"""
    ## 5. The records and the settings

    The next cell reads the three Revision records this notebook uses: the theory
    (the equations, the boundary conditions with their status, the exact spectra),
    the solver's parameters (900 RK4 steps, root tolerance $10^{-13}$) and the
    table of the free spectrum. It prints the statements it relies on.
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
    say("brane status: " + theory["boundaryConditions"]["brane"]["status"])
    say("tip status: " + theory["boundaryConditions"]["tip"]["status"])
    say("exact k = 0 spectra: " + theory["boundaryConditions"]["exactK0Spectra"])
    G_CANONICAL = parameters["numerics"]["rk4Steps"]  # RK4 steps for L = 3
    ROOT_TOLERANCE = parameters["numerics"]["rootTolerance"]
    M_RECORD, L_RECORD = parameters["physics"]["m"], parameters["physics"]["L_tipCutoff"]
    report("RK4 steps, root tolerance, m, L of the record",
           f"{G_CANONICAL}, {ROOT_TOLERANCE}, {M_RECORD}, {L_RECORD}")
    report("levels in the table", len(ROWS))
    check(theory["boundaryConditions"]["brane"]["status"] == "ASSUMED"
          and G_CANONICAL == 900 and ROOT_TOLERANCE == 1e-13 and len(ROWS) == 54,
          "records read: brane ASSUMED, 900 RK4 steps, tolerance 1e-13, 54 levels")
    '''),
    md(r"""
    ## 6. Shooting with RK4 and counting the turns of the angle

    The function `shoot` follows the Rust program line by line: it starts at the tip
    with $(a, b) = (1, 0)$, so $\theta = 0$; makes $G$ RK4 steps of the two
    equations; after every step it takes the new angle `atan2(b, a)`, adds the
    change of angle since the last step (brought into the range from $-\pi$ to
    $\pi$, so that a full turn is never lost: one step turns the point by much less
    than $\pi$) and so counts every turn. It returns $\Phi = \theta(0)$ and, when
    asked, the whole path. The second function integrates the single angle equation
    $\theta' = \varepsilon - M \sin 2\theta$ with RK4 instead; the two different
    computations must agree up to the small RK4 errors.
    """),
    code(r'''
    def shoot(eps, M, L, G, keep=False):
        """RK4 from y = -L, (a, b) = (1, 0), to y = 0 in G steps.  Returns
        Phi = theta(0) and, if keep, the arrays y, a, b, theta of the path."""
        h = L / G
        a, b = 1.0, 0.0
        theta, raw = 0.0, 0.0  # the counted angle and the last atan2 value
        path = [(-L, a, b, theta)]
        for i in range(G):
            p1a, p1b = M * a - eps * b, eps * a - M * b  # the slopes (a', b') at the start
            a2, b2 = a + h / 2 * p1a, b + h / 2 * p1b
            p2a, p2b = M * a2 - eps * b2, eps * a2 - M * b2
            a3, b3 = a + h / 2 * p2a, b + h / 2 * p2b
            p3a, p3b = M * a3 - eps * b3, eps * a3 - M * b3
            a4, b4 = a + h * p3a, b + h * p3b
            p4a, p4b = M * a4 - eps * b4, eps * a4 - M * b4
            a += h / 6 * (p1a + 2 * p2a + 2 * p3a + p4a)
            b += h / 6 * (p1b + 2 * p2b + 2 * p3b + p4b)
            new = math.atan2(b, a)  # the angle of (a, b), between -pi and pi
            change = new - raw
            if change > math.pi:  # crossed from just below pi to just above -pi
                change -= 2 * math.pi
            elif change <= -math.pi:  # crossed the other way
                change += 2 * math.pi
            theta += change
            raw = new
            if keep:
                path.append((-L + (i + 1) * h, a, b, theta))
        if keep:
            return theta, np.array(path).T
        return theta


    def angle_equation(eps, M, L, G):
        """RK4 for the single equation theta' = eps - M sin(2 theta), theta(-L) = 0."""
        h = L / G
        theta = 0.0

        def slope(t):
            return eps - M * math.sin(2 * t)
        for _ in range(G):
            k1 = slope(theta)
            k2 = slope(theta + h / 2 * k1)
            k3 = slope(theta + h / 2 * k2)
            k4 = slope(theta + h * k3)
            theta += h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        return theta


    M1, L3 = 1.0, 3.0  # the canonical case of the record
    for eps in (-2.0, 0.0, 1.0, 2.5):
        say(f"eps = {eps:+.1f}: Phi by (a, b) = {shoot(eps, M1, L3, 900):+.12f},  "
            f"by the angle equation = {angle_equation(eps, M1, L3, 900):+.12f}")
    differences = [abs(shoot(e, M1, L3, 900) - angle_equation(e, M1, L3, 900))
                   for e in np.linspace(-5.0, 5.0, 21)]
    check(max(differences) < 1e-8 and shoot(0.0, M1, L3, 900) == 0.0,
          "both ways of computing Phi agree within 1e-8; Phi(0) is exactly 0")
    '''),
    md(r"""
    ## 7. The staircase of the Pruefer angle

    The next cell computes $\Phi(\varepsilon)$ for 651 energies from $-6$ to $7$
    ($M = 1$, $L = 3$, 900 steps) and checks that it increases. The figure shows
    it with the target lines $l\pi$ (even) and $\pi/2 + l\pi$ (odd): the levels are
    the crossings, every target is crossed once, and the levels alternate between
    even and odd. Away from the levels the curve rises with slope about $L = 3$,
    because $\theta' = \varepsilon - M\sin 2\theta$ is $\varepsilon$ on average.
    """),
    code(r'''
    eps_grid = np.linspace(-6.0, 7.0, 651)
    Phi_grid = np.array([shoot(e, M1, L3, 900) for e in eps_grid])
    check(np.all(np.diff(Phi_grid) > 0), "Phi(eps) increases on the whole grid")


    def target(parity, label):
        """The target value of Phi for a level of the given parity and label."""
        return label * math.pi if parity == "even" else math.pi / 2 + label * math.pi


    canonical = [r for r in ROWS if float(r["m"]) == 1.0 and float(r["L"]) == 3.0]
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
    ax.set_title("The Pruefer staircase: $M = 1$, $L = 3$")
    ax.legend(loc="upper left", fontsize=8)
    save_figure(fig, "pruefer_staircase",
                "The end value of the Pruefer angle, $\\Phi(\\varepsilon) = "
                "\\theta(0)$ in units of $\\pi$ (vertical axis), against the energy "
                "$\\varepsilon$ in units of the mass $m$ from $-6$ to $7$ (horizontal "
                "axis), for $M = 1$, $L = 3$ and 900 RK4 steps. Blue lines: the even "
                "targets $l\\pi$; dashed orange lines: the odd targets "
                "$\\pi/2 + l\\pi$. Dots and squares: the 18 levels of the Revision "
                "record for this case. $\\Phi$ increases steadily, so it crosses every "
                "target exactly once: each level has its own label $l$, and even and "
                "odd levels alternate. The zero mode sits at $\\varepsilon = 0$, "
                "$\\Phi = 0$.")
    '''),
    md(r"""
    ## 8. The angle along the interval

    For five of the levels the next cell keeps the whole path and draws
    $\theta(y)/\pi$ from the tip $y = -3$ to the brane $y = 0$. Each curve starts
    at $0$ and ends exactly on its target; the number of half-turns it makes is the
    label. The zero mode stays at $\theta = 0$ all the way ($b = 0$ everywhere).
    """),
    code(r'''
    chosen = [("even", 0), ("odd", 0), ("even", 1), ("odd", 1), ("even", 3)]
    level_of = {(r["parity"], int(r["label"])): float(r["eps_numeric"]) for r in canonical}
    fig, ax = plt.subplots()
    for (parity, label), color in zip(chosen, [BLACK, ORANGE, BLUE, VIOLET, AQUA]):
        eps = level_of[(parity, label)]
        _, (y_path, a_path, b_path, theta_path) = shoot(eps, M1, L3, 900, keep=True)
        ax.plot(y_path, theta_path / math.pi, color=color, lw=1.5,
                ls="-" if parity == "even" else "--",
                label=f"{parity} $l = {label}$, $\\varepsilon = {eps:.4f}$")
        ax.plot([0.0], [target(parity, label) / math.pi], "o", color=color, ms=6)
    ax.set_xlabel("hidden coordinate $y$ (units $1/H$): tip at $-3$, brane at $0$")
    ax.set_ylabel("Pruefer angle $\\theta(y)/\\pi$")
    ax.set_title("The angle winds up to its target at the brane")
    ax.legend(loc="upper left", fontsize=8)
    save_figure(fig, "angle_along_y",
                "The Pruefer angle $\\theta(y)$ in units of $\\pi$ (vertical axis) "
                "along the hidden coordinate $y$ from the tip $y = -3$ to the brane "
                "$y = 0$ (horizontal axis, units $1/H$) for five levels of the case "
                "$M = 1$, $L = 3$: the zero mode (black, stays at 0), the odd label 0 "
                "(1.2923, ends at $\\pi/2$), the even label 1 (1.4480, ends at $\\pi$), "
                "the odd label 1 (2.0106, ends at $3\\pi/2$) and the even label 3 "
                "(3.2969, ends at $3\\pi$). Solid lines are even, dashed lines odd "
                "orbitals; every curve starts at 0 and ends on its target (dots).")
    '''),
    md(r"""
    ## 9. The exact levels, computed again

    The odd levels need the roots $p$ of $\tan(pL) = -p/M$, which we write as
    $M\sin(pL) + p\cos(pL) = 0$ (no infinities). The $n$-th root ($n = 0, 1, 2,
    \dots$) lies between $(n + \frac{1}{2})\pi/L$ and $(n + 1)\pi/L$, where the
    left side changes sign. The cell solves them with mpmath at 30 digits, forms
    all 54 exact levels of the table (labels $-3$ to $5$ of both parities, for
    $(M, L) = (1, 3), (1, 2), (2, 3)$; the odd label $l \ge 0$ uses the root
    $p_l$ and $l \le -1$ the root $p_{-l-1}$ with the minus sign) and compares them
    with the record's column `eps_analytic`. The figure shows the graphical
    solution for $M = 1$, $L = 3$.
    """),
    code(r'''
    mpmath.mp.dps = 30


    def odd_root(M, L, n):
        """The n-th positive root p of M sin(pL) + p cos(pL) = 0 (30 digits)."""
        g = lambda p: M * mpmath.sin(p * L) + p * mpmath.cos(p * L)  # noqa: E731
        return mpmath.findroot(g, ((n + 0.5) * mpmath.pi / L, (n + 1) * mpmath.pi / L),
                               solver="anderson")


    def exact_level(M, L, parity, label):
        """The exact level of the given parity and label."""
        if parity == "even":
            if label == 0:
                return 0.0  # the zero mode
            return math.copysign(float(mpmath.sqrt(M ** 2 + (label * mpmath.pi / L) ** 2)),
                                 label)
        n = label if label >= 0 else -label - 1
        value = float(mpmath.sqrt(M ** 2 + odd_root(M, L, n) ** 2))
        return value if label >= 0 else -value


    analytic_ours = [exact_level(float(r["m"]), float(r["L"]), r["parity"],
                                 int(r["label"])) for r in ROWS]
    analytic_record = [float(r["eps_analytic"]) for r in ROWS]
    worst_analytic = max(abs(a - b) for a, b in zip(analytic_ours, analytic_record))
    report("largest |exact level (here) - eps_analytic (record)|", f"{worst_analytic:.1e}")
    check(worst_analytic < 1e-14, "all 54 exact levels equal the column eps_analytic",
          record=f"{TABLE}, column eps_analytic")

    p_axis = np.linspace(0.01, 3.3, 3000)
    tangent = np.tan(p_axis * L3)
    tangent[np.abs(tangent) > 8] = np.nan  # do not draw the jumps at the poles
    fig, ax = plt.subplots()
    ax.plot(p_axis, tangent, color=BLUE, lw=1.4, label="$\\tan(pL)$, $L = 3$")
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
    ax.set_title("Odd levels: $\\tan(pL) = -p/M$, then $\\varepsilon = \\sqrt{M^2 + p^2}$")
    ax.legend(loc="upper right", fontsize=8)
    save_figure(fig, "odd_level_equation",
                "The equation of the odd levels for $M = 1$ and $L = 3$: the branches "
                "of $\\tan(pL)$ (solid blue) and the line $-p/M$ (dashed orange) "
                "against $p$ in units of $m$ (horizontal axis; the vertical axis is "
                "the value of each side, a pure number). Each crossing, one on every "
                "branch between $(n + 1/2)\\pi/L$ and $(n + 1)\\pi/L$, is a root "
                "$p_n$ and gives the two odd levels $\\pm\\sqrt{M^2 + p_n^2}$; the "
                "first three give 1.2923, 2.0106 and 2.9119.")
    '''),
    md(r"""
    ## 10. All 54 levels by shooting, against the Rust program

    Now the search itself. For each row of the table the cell takes the target of
    its parity and label and finds the energy with $\Phi(\varepsilon)$ = target by
    bisection, starting from the bracket $-12 < \varepsilon < 12$ (the cell checks
    that $\Phi(-12)$ lies below and $\Phi(12)$ above every target) and stopping when
    the bracket is narrower than the record's tolerance $10^{-13}$. Like the Rust
    program it first tries $\varepsilon = 0$, which hits the zero mode's target
    exactly. The number of RK4 steps is the program's: $G = 900 L/3$ (900 for
    $L = 3$, 600 for $L = 2$, the same step $h = 1/300$). Then it compares with the
    record's column `eps_numeric`, and recomputes the two numbers that the
    program's check `free_k0_analytic_spectra` quotes: the largest
    $|\varepsilon_{\rm numeric} - \varepsilon_{\rm exact}|$ for $|\varepsilon| <
    4m$ and for $|\varepsilon| \ge 4m$. (The check's text calls the second band
    "$4m \le |\varepsilon| < 7m$", but the Rust code, file
    Revision/kohn_sham/solver/src/spectrum.rs, puts every level with
    $|\varepsilon| \ge 4m$ into it, and the table goes up to $8.75m$; the cell
    prints both numbers.)
    """),
    code(r'''
    def find_level(M, L, G, parity, label, tolerance=ROOT_TOLERANCE):
        """The level of the given parity and label: bisection on Phi - target."""
        goal = target(parity, label)
        if shoot(0.0, M, L, G) == goal:  # the zero mode: exactly 0
            return 0.0
        low, high = -12.0, 12.0  # Phi(low) < goal <= Phi(high), checked below
        while high - low > tolerance:
            middle = 0.5 * (low + high)
            if shoot(middle, M, L, G) < goal:
                low = middle
            else:
                high = middle
        return 0.5 * (low + high)


    CASES = [(1.0, 3.0), (1.0, 2.0), (2.0, 3.0)]
    brackets_ok = all(shoot(-12.0, M, L, round(900 * L / 3)) < target("odd", -4)
                      and shoot(12.0, M, L, round(900 * L / 3)) > target("odd", 5)
                      for M, L in CASES)
    numeric_ours = [find_level(float(r["m"]), float(r["L"]),
                               round(G_CANONICAL * float(r["L"]) / 3.0), r["parity"],
                               int(r["label"])) for r in ROWS]
    numeric_record = [float(r["eps_numeric"]) for r in ROWS]
    worst_numeric = max(abs(a - b) for a, b in zip(numeric_ours, numeric_record))
    report("largest |level (here) - eps_numeric (Rust program)|", f"{worst_numeric:.1e}")
    check(brackets_ok, "Phi(-12) < every target < Phi(12) in the three cases")
    check(worst_numeric < 1e-11, "all 54 shooting levels equal the column eps_numeric",
          record=f"{TABLE}, column eps_numeric")
    zero_rows = [i for i, r in enumerate(ROWS) if r["parity"] == "even"
                 and int(r["label"]) == 0]
    check(all(numeric_ours[i] == 0.0 == numeric_record[i] for i in zero_rows),
          "the zero mode has the energy exactly 0 in all three cases",
          record=f"{SOLVER_REPORT}, check free_zero_mode_exact")

    differences_ours = [n - a for n, a in zip(numeric_ours, analytic_ours)]
    pairs = list(zip(differences_ours, analytic_ours))
    low_band = max(abs(d) for d, a in pairs if abs(a) < 4)  # all levels below 4 m
    high_band = max(abs(d) for d, a in pairs if abs(a) >= 4)  # all levels from 4 m on
    below_7 = max(abs(d) for d, a in pairs if 4 <= abs(a) < 7)
    top = max(abs(a) for _, a in pairs)  # the highest level of the table
    solver_report = json.loads(repository_file(SOLVER_REPORT).read_text(encoding="utf-8"))
    detail = [c["detail"] for c in solver_report["checks"]
              if c["name"] == "free_k0_analytic_spectra"][0]
    quoted = float(re.findall(r"max \|difference\| ([0-9.]+e-[0-9]+) for \|eps\| < 4 m",
                              detail)[0])
    quoted_high = float(re.findall(r"([0-9.]+e-[0-9]+) for 4 m <= \|eps\| < 7 m",
                                   detail)[0])
    report("largest |numeric - exact| for |eps| < 4 m (here, record)",
           f"{low_band:.2e}, {quoted:.2e}")
    report("largest |numeric - exact| for |eps| >= 4 m (here, record)",
           f"{high_band:.2e}, {quoted_high:.2e}")
    say(f"Note: the record's check text names its second band 4 m <= |eps| < 7 m, but "
        f"the solver puts every level with |eps| >= 4 m into it, and the table's "
        f"levels reach {top:.4f} m; the quoted number belongs to that level. For "
        f"4 m <= |eps| < 7 m alone the largest difference is {below_7:.2e}.")
    check(abs(low_band / quoted - 1) < 0.005 and abs(high_band / quoted_high - 1) < 0.005,
          "the two largest differences quoted by the solver check are reproduced",
          record=f"{SOLVER_REPORT}, check free_k0_analytic_spectra")
    '''),
    md(r"""
    ## 11. The orbitals

    The next cell keeps the paths of four levels of the canonical case, normalises
    each orbital so that $\int_{-L}^{0} (a^2 + b^2)\, dy = 1$ (Simpson's rule on the
    900 steps), and draws $a(y)$ and $b(y)$. It checks the brane condition of each
    ($b(0) = 0$ even, $a(0) = 0$ odd) and compares the zero mode with its exact form
    $a = \sqrt{2M/(1 - e^{-2ML})}\, e^{M y}$, $b = 0$ (the normalised $e^{My}$),
    which the Rust program's check `free_zero_mode_exact` also tests.
    """),
    code(r'''
    def simpson(values, h):
        """Simpson's rule for equally spaced values (an even number of intervals)."""
        return h / 3 * (values[0] + values[-1] + 4 * values[1:-1:2].sum()
                        + 2 * values[2:-1:2].sum())


    fig, axes = plt.subplots(2, 2, figsize=(9.0, 6.4), sharex=True)
    residuals = []
    for ax, (parity, label) in zip(axes.flat, [("even", 0), ("odd", 0), ("even", 1),
                                              ("odd", 2)]):
        eps = level_of[(parity, label)]
        _, (y_path, a_path, b_path, _) = shoot(eps, M1, L3, 900, keep=True)
        norm = math.sqrt(simpson(a_path ** 2 + b_path ** 2, L3 / 900))
        a_path, b_path = a_path / norm, b_path / norm
        end = b_path[-1] if parity == "even" else a_path[-1]  # must vanish at y = 0
        residuals.append(abs(end))
        ax.plot(y_path, a_path, color=BLUE, lw=1.5, label="$a(y)$")
        ax.plot(y_path, b_path, color=ORANGE, lw=1.5, ls="--", label="$b(y)$")
        ax.axhline(0.0, color=BLACK, lw=0.6)
        ax.set_title(f"{parity}, $l = {label}$, $\\varepsilon = {eps:.4f}$", fontsize=10)
        ax.legend(fontsize=8, loc="upper left")
        if parity == "even" and label == 0:
            exact_a = math.sqrt(2 * M1 / (1 - math.exp(-2 * M1 * L3))) * np.exp(M1 * y_path)
            zero_mode_error = max(np.max(np.abs(a_path - exact_a)), np.max(np.abs(b_path)))
    for ax in axes[1]:
        ax.set_xlabel("hidden coordinate $y$ (units $1/H$)")
    for ax in axes[:, 0]:
        ax.set_ylabel("component (units $H^{1/2}$)")
    save_figure(fig, "orbitals",
                "The normalised orbitals of four levels of the case $M = 1$, $L = 3$: "
                "the components $a(y)$ (solid blue) and $b(y)$ (dashed orange) against "
                "the hidden coordinate $y$ from the tip $-3$ to the brane $0$ "
                "(horizontal axes, units $1/H$; vertical axes in units of $H^{1/2}$, so "
                "that $\\int (a^2 + b^2) dy = 1$). Top left: the zero mode "
                "$a \\propto e^{y}$, $b = 0$, concentrated at the brane. Top right: odd "
                "label 0. Bottom: even label 1 and odd label 2. Every orbital has "
                "$b = 0$ at the tip; at the brane the even ones have $b = 0$ and the "
                "odd ones $a = 0$.")
    report("largest brane residual |b(0)| or |a(0)|", f"{max(residuals):.1e}")
    zero_detail = [c["detail"] for c in solver_report["checks"]
                   if c["name"] == "free_zero_mode_exact"][0]
    zero_quoted = re.findall(r"e\^\(My\) to ([0-9.]+e-[0-9]+)", zero_detail)[0]
    report("zero mode: largest distance from the exact normalised form (here, record)",
           f"{zero_mode_error:.1e}, {zero_quoted}")
    say("The record's program integrates the norm with Simpson's rule on a grid twice "
        "as fine (step midpoints added by cubic interpolation); our Simpson's rule on "
        "the 900 steps alone is slightly less accurate, still far below 1e-10.")
    check(max(residuals) < 1e-10, "every orbital meets its brane condition within 1e-10")
    check(zero_mode_error < 1e-10,
          "the zero mode is sqrt(2M/(1 - e^(-2ML))) e^(My), b = 0, within 1e-10",
          record=f"{SOLVER_REPORT}, check free_zero_mode_exact")
    '''),
    md(r"""
    ## 12. How the error depends on the step

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
        errors = np.array([abs(find_level(M1, L3, G, parity, label) - exact)
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
    **Why the error grows with the level.** Far above the mass, $\theta' \approx
    \varepsilon$: the point $(a, b)$ turns at the rate $\varepsilon$. One RK4 step
    multiplies a turning point by $R(i\omega)$ with $\omega = \varepsilon h$ (the
    amplification factor of the test equation $y' = i\varepsilon y$), whose angle
    is a little SMALLER than the exact $\omega$. The next cell lets sympy expand the
    angle of $R(i\omega)$: it is $\omega - \omega^5/120 + \dots$ After $G = L/h$
    steps the end angle lags by about $L\, \varepsilon^5 h^4/120$; since $\Phi$
    grows by about $L$ per unit of energy, the computed level comes out too high by

    $$\delta\varepsilon \approx \frac{\varepsilon^5 h^4}{120}, \qquad
    \frac{\delta\varepsilon}{\varepsilon} \approx \frac{(h\varepsilon)^4}{120} .$$

    The figure draws the relative error $\delta\varepsilon/\varepsilon$ of all 51
    nonzero levels of the record (the record's column `difference`) against
    $h|\varepsilon|$ with $h = 1/300$, with our own differences on top, and this
    prediction as a line. Close to the mass the point does not turn uniformly
    ($\theta' = \varepsilon - M \sin 2\theta$), and the error is smaller than the
    prediction; far above it the points approach the line.
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
    x_values = eps_abs / 300.0  # h |eps| with h = 1/300
    record_diff = np.array([abs(float(ROWS[i]["difference"])) for i in nonzero])
    our_diff = np.array([abs(differences_ours[i]) for i in nonzero])
    masses = np.array([float(ROWS[i]["m"]) for i in nonzero])
    fig, ax = plt.subplots()
    for mass, color in ((1.0, BLUE), (2.0, ORANGE)):
        pick = masses == mass
        ax.loglog(x_values[pick], record_diff[pick] / eps_abs[pick], "o", color=color,
                  ms=6, label=f"record, $M = {mass:.0f}$")
    ax.loglog(x_values, our_diff / eps_abs, "x", color=BLACK, ms=5,
              label="this notebook")
    x_guide = np.linspace(x_values.min(), x_values.max(), 50)
    ax.loglog(x_guide, x_guide ** 4 / 120, "--", color=GREY,
              label="prediction $(h\\varepsilon)^4/120$")
    ax.set_xlabel("$h |\\varepsilon|$ with $h = 1/300$ (pure number)")
    ax.set_ylabel("relative error $\\delta\\varepsilon / |\\varepsilon|$")
    ax.set_title("The RK4 error of all 51 nonzero levels of the record")
    ax.legend(loc="upper left", fontsize=8)
    save_figure(fig, "record_differences",
                "The relative error $\\delta\\varepsilon/|\\varepsilon|$ of the "
                "shooting levels for all 51 nonzero levels of the Revision record of "
                "the free spectrum (vertical axis, a pure number), against "
                "$h|\\varepsilon|$ with the record's step $h = 1/300$ (horizontal "
                "axis, a pure number), on logarithmic axes. Dots: the record's column "
                "difference divided by the level, for $M = 1$ (blue; $L = 3$ and "
                "$L = 2$) and $M = 2$ (orange); crosses: this notebook's shooting, "
                "which falls on the record's points. Dashed: the prediction "
                "$(h\\varepsilon)^4/120$ from the phase lag of one RK4 step; the "
                "levels far above the mass approach it, those near the mass lie "
                "below it.")
    ratio = (record_diff / eps_abs) / (x_values ** 4 / 120)
    report("error / prediction for the levels above 7 m",
           ", ".join(f"{q:.3f}" for q in ratio[eps_abs > 7]))
    check(np.all(ratio < 1) and np.all(ratio[eps_abs > 7] > 0.9),
          "every level error lies below the prediction, within 10 % above 7 m")
    check(np.max(np.abs(record_diff - our_diff)) < 1e-11,
          "our differences equal the record's column difference within 1e-11",
          record=f"{TABLE}, column difference")
    '''),
    md(r"""
    ## 13. The last check

    The last cell checks that all 6 figure files exist in the folder
    Revision/textbook/figures and prints the number of checks that passed.
    """),
    code(r'''
    names = ["pruefer_staircase", "angle_along_y", "odd_level_equation", "orbitals",
             "level_convergence", "record_differences"]
    present = [output_file(f"{FIGURE_FOLDER}/02d_{k}_{name}.png").is_file()
               for k, name in enumerate(names, 1)]
    check(all(present), f"all {len(names)} figure files of notebook 02d exist")
    all_checks_passed()
    '''),
    md(r"""
    ## 14. What this notebook showed

    - The free Kohn-Sham block of the book, $a' = M a - \varepsilon b$,
      $b' = \varepsilon a - M b$ with $b(-L) = 0$ and $b(0) = 0$ or $a(0) = 0$, has
      the exact levels $0$ (the zero mode $a \propto e^{My}$, $b = 0$),
      $\pm\sqrt{M^2 + (n\pi/L)^2}$ (even) and $\pm\sqrt{M^2 + p^2}$ with
      $\tan(pL) = -p/M$ (odd).
    - The Pruefer angle obeys $\theta' = \varepsilon - M\sin 2\theta$; its end value
      increases with $\varepsilon$, so each level is the unique crossing of a target
      $l\pi$ or $\pi/2 + l\pi$: no level can be missed and each has a label.
    - Shooting with RK4 exactly as the Revision Rust program does (900 steps for
      $L = 3$, bisection to $10^{-13}$) reproduces all 54 levels of the record
      Revision/kohn_sham/results/spectrum/free-k0-analytic.csv within
      $10^{-11}$ (in fact about $10^{-13}$), the exact column, the zero mode exactly,
      and the numbers $7.23 \times 10^{-10}$ (levels below $4m$) and
      $5.05 \times 10^{-8}$ (all levels from $4m$ up to $8.75m$; the check's text
      says "below $7m$") quoted by the program's check free_k0_analytic_spectra.
    - The level errors fall like $h^4$; for levels far above the mass the relative
      error is close to $(h\varepsilon)^4/120$, the phase lag of RK4. The canonical
      step $h = 1/300$ gives errors below $10^{-9}$ for $|\varepsilon| < 4m$.
    - What this notebook does not show: the physics of these equations (where they
      come from, the meaning of the levels, the interacting case); the brane
      conditions rest on the ASSUMED mirror symmetry and the tip condition is a
      choice of the model, as the record states.
    """),
]

if __name__ == "__main__":
    raise SystemExit(run_builder(__file__))
