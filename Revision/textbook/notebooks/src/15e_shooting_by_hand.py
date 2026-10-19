#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
"""Builder of Notebook 15e, "The solver's method by hand: shooting, Pruefer count and
Anderson mixing" (textbook "Universes in Pairs", chapter 15).

The notebook Revision/textbook/notebooks/15e_shooting_by_hand.ipynb is BUILT from this
file by Revision/textbook/tools/nbkit.py (never edit the .ipynb by hand):

    python Revision/textbook/tools/nbkit.py build \
        Revision/textbook/notebooks/src/15e_shooting_by_hand.py --date YYYY-MM-DD
    python Revision/textbook/tools/nbkit.py check \
        Revision/textbook/notebooks/src/15e_shooting_by_hand.py

The notebook re-implements in plain Python the numerical method of the Revision Kohn-Sham
solver (Revision/kohn_sham/solver/src/shoot.rs and scf.rs) in the corrected metric of
2026-10-16: RK4 shooting in the hidden coordinate with the hidden scale f, the Pruefer
angle and its integer label, the safeguarded Newton root, the Hermite midpoints and
Simpson normalisation, and the self-consistent loop with Anderson mixing.  It reproduces
the solver's free spectra, the exact fold band eps = kappa k with its slope e^(-a4,0), the
rescaling identity and the interacting N = 8 ground states from the committed Revision
record.  No Rust is needed.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools"))
from nbkit import code, md, run_builder  # noqa: E402

FIGURES = [
    "15e_1_phase_function",
    "15e_2_orbitals",
    "15e_3_rk4_convergence",
    "15e_4_fold_band",
    "15e_5_scf_mixing",
    "15e_6_n8_potentials",
]

FACTS = {
    "id": "15e",
    "name": "15e_shooting_by_hand",
    "title": "The solver's method by hand: shooting, Pruefer count and Anderson mixing",
    "purpose": (
        "It re-implements in plain Python the numerical method of the Rust Kohn-Sham "
        "solver in the corrected metric (fourth-order Runge-Kutta shooting in the hidden "
        "coordinate with the hidden scale f, the Pruefer angle that labels every level, a "
        "safeguarded Newton root, the normalisation of the orbitals, and the "
        "self-consistent loop with Anderson mixing), and uses it to reproduce the "
        "solver's exact free spectra, its convergence order, the exact fold band "
        "eps = kappa k with its slope e^(-a4,0), the rescaling identity between the "
        "slices and the interacting ground states of N = 8 particles from the committed "
        "Revision record."
    ),
    "records": [
        ["Revision/kohn_sham/results/spectrum/free-k0-analytic.csv",
         "the solver's free levels at k = 0 and their exact values, at f = 1 and at "
         "f = e^(-1/2)"],
        ["Revision/kohn_sham/results/ground/summary.csv",
         "energies, HOMO and LUMO of the ground states N = 8"],
        ["Revision/kohn_sham/results/ground/runs.json",
         "the recorded residuals of the self-consistent loop"],
        ["Revision/kohn_sham/results/parameters.json",
         "the couplings lambda_1 and lambda_2 of N = 8 and the history beta = 4/3"],
        ["Revision/kohn_sham/ks-theory.json",
         "the block equation, the boundary conditions and the fold-band slope c"],
        ["Revision/kohn_sham/reports/ks-rust-solver.json",
         "the solver checks that this notebook repeats by hand"],
        ["Revision/kohn_sham/reports/ks-rust-determinism.json",
         "the measured convergence ratio 16 of the solver"],
    ],
    "packages": ["numpy", "matplotlib"],
    "needs_rust": [],
    "expected_seconds": 40,
    "timeout_seconds": 900,
    "files_written": ["Revision/textbook/figures/15e.captions.json"]
    + [f"Revision/textbook/figures/{name}.png" for name in FIGURES],
    "final_lines": [
        "PASS every figure file of this notebook exists",
        "ALL 19 CHECKS PASSED (notebook 15e)",
    ],
    "troubleshooting": [],
}

CELLS = [
    md(r"""
    ## 1. What this notebook computes

    The Rust Kohn-Sham solver of the repository finds the levels and orbitals of the
    Kohn-Sham equations of dirac16complex by **shooting**, labels every level with an
    integer (the **Pruefer label**), and makes the potentials self-consistent with
    **Anderson mixing**. This notebook writes the same method in plain Python, step by
    step, for the corrected metric of the author's primordial field, and reproduces
    numbers of the committed Revision record:

    - the exact levels at $k = 0$ (formulas with the hidden scale $f$) and the solver's
      numerical levels, at the first slice ($f = 1$) and at $a_{4,0} = 1.5$
      ($f = e^{-1/2}$);
    - the order of accuracy of the integration (the error falls 16-fold when the step is
      halved);
    - the exact **fold band** $\varepsilon = \kappa k = k\,e^{-a_{4,0}}$, its slope
      $e^{-a_{4,0}}$ and its redshift along the deflating history, and the rescaling
      identity between the slices;
    - the self-consistent ground states of $N = 8$ particles for the four couplings
      $\pm\lambda_1$, $\pm\lambda_2$: energies, levels and even the residual of each
      iteration of the loop;
    - an exact symmetry of these states: $E_{KS}(-\lambda) = -E_{KS}(+\lambda)$.

    It draws six figures. It needs no Rust: the Python code is short enough to read in
    full, and it is slower than the solver only by a factor of about a hundred.
    """),
    md(r"""
    ## 3. The words used in this notebook

    - **Orbital**: a one-particle wave function; here a pair of real functions $a(y)$,
      $b(y)$ of the hidden coordinate $y$.
    - **Fold** and **tip**: the two ends of the interval of $y$. At the fold $y = 0$
      the two halves of a cell of the hidden direction meet; at the tip $y = -L$ the
      model cuts the hidden direction off.
    - **Hidden scale** $f$: the factor by which the hidden direction has shrunk at a
      slice of the history, $f = e^{-a_4}b_4^{1/2}$, which is $e^{-a_{4,0}/3}$ on the
      record's history; it multiplies the right-hand side of the block equation.
    - **Ordinary differential equation (ODE)**: an equation for functions of one
      variable that contains their derivatives. Given the values at one point (the
      **initial values**) it fixes the functions everywhere.
    - **RK4** (the classical fourth-order Runge-Kutta method): a recipe that advances
      the solution of an ODE by one **step** $h$ using four evaluations of the
      derivatives; its error falls like $h^4$.
    - **Shooting**: guess an energy $\varepsilon$, start the orbital at one end with
      the boundary condition of that end, integrate to the other end, and change
      $\varepsilon$ until the boundary condition there holds too.
    - **Pruefer angle**: the angle $\theta$ of the point $(a, b)$ seen from the origin,
      $a = r\cos\theta$, $b = r\sin\theta$, followed continuously (it may grow beyond
      $2\pi$).
    - **Phase function** $\Phi(\varepsilon)$: $j$ times the Pruefer angle at the fold.
      It increases strictly with $\varepsilon$.
    - **Label** $l$: the whole number that says which crossing of $\Phi$ with the
      targets $l\pi$ (even fold condition) or $\pi/2 + l\pi$ (odd fold condition) a
      level is.
    - **Root**: a value where a function is zero. **Newton's method** improves a guess
      $x$ to $x - F(x)/F'(x)$. A **bracket** is an interval known to contain the root;
      **bisection** halves it.
    - **Normalisation**: multiplying an orbital by a number so that
      $\int_{-L}^{0} (a^2 + b^2)\,dy = 1$.
    - **Simpson's rule**: $\int f\,dy \approx \tfrac{h}{6}[f_0 + 4 f_{1/2} + 2 f_1 +
      4 f_{3/2} + \dots + f_G]$ on the step ends and midpoints of $G$ steps.
    - **Cubic Hermite interpolation**: the value in the middle of a step from the values
      and the derivatives at its two ends.
    - **Fold band**: the lowest level with the even fold condition of the block type
      $j = +1$ at each 3-momentum $k$; its orbital is the zero-mode orbital.
    - **Self-consistency, residual, mixing**: the potentials made from the orbitals must
      equal the potentials that made the orbitals. The residual is the largest change
      in one iteration. **Linear mixing** moves a fraction $\beta$ of the way toward the
      new potential; **Anderson mixing** combines the last few iterations so that their
      residuals cancel as far as possible.
    """),
    md(r"""
    ## 4. The physical and mathematical situation

    The author's corrected metric (version 2 of 2026-10-16) has the hidden space-like
    direction $x_0$, with $z = 6Hx_0$; 3-space $x_1, x_2, x_3$ with the scale factor
    $e^{a_4}$ and no warp; the time $x_4$; and three extra times $x_5, x_6, x_7$ that
    deflate exponentially, with the scale factor $e^{-a_4}b_4^{1/2}(\sin^2 z)^{1/12}$.
    The hidden direction has the scale factor $e^{-a_4}b_4^{1/2}|\cot z|$ and shrinks
    together with the extra times. In the hidden coordinate $y = \ln|\sin z|/(6H)$,
    from the tip $y = -L$ to the fold $y = 0$, the Kohn-Sham equation of dirac16complex
    reduces exactly (Revision record Revision/kohn_sham/ks-theory.json) to eight
    $2 \times 2$ blocks. With the orbital written as $\chi = (a, i\,b)$, $a$ and $b$
    real, a block of type $j = \pm 1$ at the 3-momentum $k$ is the real system

    $$a' = f\,[M a - (\kappa k + j(\varepsilon - v))\,b], \qquad
    b' = f\,[(j(\varepsilon - v) - \kappa k)\,a - M b],$$

    with the momentum weight $\kappa = e^{-a_{4,0}}$ (the same at every $y$), the
    hidden scale $f = e^{-a_{4,0}}b_{4,0}^{1/2}$, which is $e^{-a_{4,0}/3}$ on the
    record's history $b_4 = e^{(4/3)a_4}$, the effective mass $M(y)$ and the potential
    $v(y)$. Boundary conditions: at the tip $b(-L) = 0$ (chosen); at the fold
    $b(0) = 0$ (the even fold condition) and $a(0) = 0$ (the odd fold condition); the
    record solves and fills both (ASSUMED).

    **The Pruefer angle.** Write $a = r\cos\theta$, $b = r\sin\theta$. Then
    $a b' - b a' = r^2 \theta'$. Inserting the system:

    $$a b' - b a' = f\,[j(\varepsilon - v)(a^2 + b^2) - \kappa k (a^2 - b^2)
    - 2 M a b],$$

    because the terms $-M a b$ (from $a b'$) and $-M a b$ (from $-b a'$) add, the terms
    with $\kappa k$ give $-\kappa k a^2 + \kappa k b^2$, and the terms with
    $j(\varepsilon - v)$ give $j(\varepsilon - v)(a^2 + b^2)$, all with the factor $f$.
    Dividing by $r^2$ and using $a^2 - b^2 = r^2\cos 2\theta$ and $2ab = r^2\sin 2\theta$:

    $$\theta' = f\,[j(\varepsilon - v) - \kappa k \cos 2\theta - M \sin 2\theta] .$$

    At the tip $\theta(-L) = 0$ (because $b = 0$ there). Write $\psi = j\theta$.
    Multiplying the angle equation by $j$ and using $j^2 = 1$,
    $\cos(2j\psi) = \cos 2\psi$ and $\sin(2j\psi) = j\sin 2\psi$ gives

    $$\psi' = f\,[\varepsilon + G(y, \psi)], \qquad
    G(y, \psi) = -v - j\kappa k \cos 2\psi - M \sin 2\psi ,$$

    and $G$ does not contain $\varepsilon$. The **phase function**
    $\Phi(\varepsilon) = j\,\theta(0) = \psi(0)$ increases strictly with $\varepsilon$,
    by a comparison of two energies $\varepsilon_1 < \varepsilon_2$: let $\psi_1$,
    $\psi_2$ be their angles (both 0 at the tip) and $D = \psi_2 - \psi_1$. At the tip
    $D = 0$ and $D' = f(\varepsilon_2 - \varepsilon_1) > 0$, so $D > 0$ just after the
    tip. If $D$ came back to 0 at a first point $y_1$, it would arrive there from
    positive values, so $D'(y_1) \le 0$; but at $y_1$ the two angles are equal, the two
    $G$ terms cancel and $D'(y_1) = f(\varepsilon_2 - \varepsilon_1) > 0$. This
    contradiction shows $D(0) > 0$, that is $\Phi(\varepsilon_2) > \Phi(\varepsilon_1)$.
    (The exact derivative $d\Phi/d\varepsilon = f\int r^2 dy / r(0)^2 > 0$, which
    section 6 uses for Newton's method, says the same.) $\Phi$ also runs from
    $-\infty$ to $+\infty$: if $|v|$, $\kappa k$ and $|M|$ are at most $C_0$ on the
    interval, then $|G| \le 3C_0$, and integrating $\psi'$ over the length $L$ gives
    $(\varepsilon - 3C_0)fL \le \Phi(\varepsilon) \le (\varepsilon + 3C_0)fL$, so
    $\Phi(\varepsilon) \approx \varepsilon fL$ for large $|\varepsilon|$. The even fold
    condition, $b(0) = 0$, means $\theta(0)$ is a whole multiple of $\pi$; the odd one,
    $a(0) = 0$, means $\theta(0) = \pi/2 + $ a multiple of $\pi$. Because $\Phi$
    increases strictly, each target $l\pi$ (even) or $\pi/2 + l\pi$ (odd) is reached at
    exactly one energy: **every level has its own whole number $l$, and no level can be
    missed** (the oscillation theorem).

    **Exact levels at $k = 0$** with constant $M = m$ and $v = 0$ (Revision record
    ks-theory.json, boundaryConditions.exactK0Spectra): even fold condition:
    $\varepsilon = 0$ with the zero mode $(a, b) = (e^{fMy}, 0)$, and
    $\varepsilon = \pm\sqrt{M^2 + (n\pi/(fL))^2}$, $n = 1, 2, \dots$; odd fold
    condition: $\varepsilon = \pm\sqrt{M^2 + p^2}$ with $\tan(pfL) = -p/M$.

    **The exact fold band.** For every $k$ the zero-mode orbital $(e^{fMy}, 0)$ also
    solves the block $j = +1$ with $\varepsilon = \kappa k$: with $b = 0$ the first
    equation is $a' = fMa$, and the second needs $j(\varepsilon - v) - \kappa k = 0$,
    that is $\varepsilon = \kappa k$ for $j = +1$, $v = 0$; and $b = 0$ holds at the tip
    and at the fold. This is the fold band (ks-theory.json, boundaryConditions.tip).

    **The self-consistent problem for $N = 8$.** Eight particles fill the eight zero
    modes at $k = 0$ (four orbitals for each $j$). Their proper densities are
    $n = \sum w\,g\,f_o\,P\,(a^2 + b^2)$ and $S = \sum w\,g\,f_o\,P\,j\,2ab$ with
    $P = e^{-3Hy}/\mathrm{Vol}_7$, $w = 1/2$ (each half of the cell holds $N/2$),
    $g = 4$ and the occupation $f_o = 1$; the potentials are
    $M = m + \tfrac{15}{16}\lambda S$ and $v = -\tfrac{1}{16}\lambda n$; the energy is
    $E_{KS} = \sum g f_o \varepsilon - 2\,\mathrm{Vol}_7 \int e^{3Hy} e_{int}\,dy$ with
    $e_{int} = \lambda(\tfrac{15}{32}S^2 - \tfrac{1}{32}n^2)$. Units $H = m = 1$,
    $L = 3$, $\Delta k = 0.25$; $\mathrm{Vol}_7(a_{4,0}) = \ell^3 v_t e^{(5/3)a_{4,0}}$
    with $\ell = 2\pi/\Delta k$ and $v_t = 1$.

    The history $a_4 = A H x_4$, $b_4 = e^{(4/3)AHx_4}$ ($A = 1$) is a PRESCRIBED
    BACKGROUND; the states are instantaneous states at a slice $a_{4,0}$, which enters
    through $\kappa$, $f$ and $\mathrm{Vol}_7$.
    """),
    md(r"""
    ## 5. The grid

    The solver integrates with $G = 900$ RK4 steps of length $h = L/G$ from $y = -L$ to
    $y = 0$. Every RK4 step needs the potentials at its two ends and at its midpoint, so
    the potentials live on the **fine grid** of the $2G + 1$ step ends and midpoints.
    The next cell defines the hidden scale $f$ and the proper volume
    $\mathrm{Vol}_7$ of a slice, and builds the grid exactly as the solver does: the
    coordinates $y_f$, the factors $e^{3Hy}$ (the proper volume) and the Simpson
    weights. The check: Simpson's rule integrates $e^{y}$ from $-3$ to $0$ to
    $1 - e^{-3}$ within $10^{-13}$.
    """),
    code(r'''
    import csv  # reads the tables (CSV files) of the Revision record
    import math  # exp, sqrt, atan2, pi for single numbers

    import numpy as np  # arrays of numbers

    H, MASS, L = 1.0, 1.0, 3.0  # the units H = m = 1 and the tip cutoff L = 3
    DK = 0.25  # the spacing of the 3-momenta
    BETA = 4.0 / 3.0  # the history b4 = e^{beta a4} of the record (beta = 4/3)
    ELL = 2.0 * math.pi / DK  # the side of the coordinate 3-torus
    PALETTE = ["#2a78d6", "#eb6834", "#1baf7a", "#eda100", "#e87ba4", "#008300",
               "#4a3aa7", "#e34948"]  # the colours of the figures, in a fixed order


    def hidden_scale(a4):
        """f = e^{-a4} b4^{1/2} = e^{(beta/2 - 1) a4} on the history (b4(0) = 1)."""
        return math.exp((0.5 * BETA - 1.0) * a4)


    def vol7(a4):
        """Proper 7-volume of the cell per unit e^{3Hy}: ell^3 v_t e^{(2 beta - 1) a4}."""
        return ELL * ELL * ELL * math.exp((2.0 * BETA - 1.0) * a4)


    def make_grid(steps, length=L):
        """The solver's grid for `steps` RK4 steps on [-length, 0] (a dictionary)."""
        points = 2 * steps + 1  # step ends and step midpoints
        y = [-length * ((points - 1 - f) / (points - 1)) for f in range(points)]
        half = 0.5 * length / steps  # the distance between two fine points
        weights = [(4.0 if f % 2 == 1 else 2.0) * half / 3.0 for f in range(points)]
        weights[0] = weights[-1] = half / 3.0  # Simpson: 1, 4, 2, 4, ..., 4, 1 (x h/6)
        return {"steps": steps, "h": length / steps, "points": points, "y": y,
                "e3": [math.exp(3 * H * v) for v in y], "simpson": np.array(weights)}


    GRID = make_grid(900)  # the canonical grid of the solver
    Y = np.array(GRID["y"])
    E3 = np.array(GRID["e3"])
    simpson_test = float(np.sum(GRID["simpson"] * np.exp(Y)))
    say(f"fine grid: {GRID['points']} points, step h = {GRID['h']:.6f}")
    report("hidden scale f at a4,0 = 0, 0.5, 1, 1.5, 2",
           ", ".join(f"{hidden_scale(a):.6f}" for a in (0.0, 0.5, 1.0, 1.5, 2.0)))
    report("Vol_7 at a4,0 = 0 and 2", f"{vol7(0.0):.6f} and {vol7(2.0):.3f}")
    report("Simpson integral of e^y from -3 to 0", f"{simpson_test:.15f}")
    check(abs(simpson_test - (1.0 - math.exp(-3.0))) < 1e-13,
          "Simpson's rule on the fine grid integrates e^y exactly to 1e-13")
    '''),
    md(r"""
    ## 6. Shooting: one integration from the tip to the fold

    The next cell is the heart of the method. `rhs` is the bracket $(a', b')/f$ of the
    block equation for given coefficients; `shoot` multiplies $M$, $\kappa k$ and
    $j(\varepsilon - v)$ by the hidden scale $f$ once at every fine point (exactly as
    the solver does), starts at the tip with $(a, b) = (1, 0)$ (this satisfies
    $b(-L) = 0$), makes $G$ RK4 steps to the fold, and follows the Pruefer angle: after
    each step it computes the angle of the new point with `atan2` and adds the change of
    angle (brought into $(-\pi, \pi]$) to $\theta$, so $\theta$ is followed continuously.
    It also adds up $\int r^2\,dy$ with the trapezoid rule on the step ends,
    $\tfrac{h}{2}(r_i^2 + r_{i+1}^2)$ per step, exactly as the solver does, for the
    derivative $d\Phi/d\varepsilon = f\int r^2 dy / r(0)^2$, which Newton's method
    needs. When asked (`store=True`) it keeps the values at the step ends. The
    potentials `mass` and `pot` are lists of $M$ and $v$ on the fine grid.
    """),
    code(r'''
    def rhs(m_y, kk, je, a, b):
        """(a', b') of the block equation; m_y = f M, kk = f kappa k, je = f j (eps - v)."""
        return m_y * a - (kk + je) * b, (je - kk) * a - m_y * b


    def shoot(eps, k, j, a4, mass, pot, grid=GRID, store=False):
        """Integrate from the tip to the fold.  Returns (Phi, dPhi/deps, node values)."""
        h = grid["h"]
        fh = hidden_scale(a4)  # the hidden scale f of the slice
        kk = k * math.exp(-a4)  # kappa k = k e^{-a4,0}, the same at every y
        coef = [(fh * mass[f], fh * kk, fh * j * (eps - pot[f]))
                for f in range(grid["points"])]
        a, b = 1.0, 0.0  # the tip condition b(-L) = 0
        theta, raw = 0.0, 0.0  # the followed angle and the last angle from atan2
        area, r2_prev = 0.0, 1.0  # integral of r^2 (trapezoid) and r^2 at the last node
        nodes = [(a, b)] if store else None
        for i in range(grid["steps"]):
            c0, c1, c2 = coef[2 * i], coef[2 * i + 1], coef[2 * i + 2]  # end, mid, end
            k1a, k1b = rhs(*c0, a, b)
            k2a, k2b = rhs(*c1, a + 0.5 * h * k1a, b + 0.5 * h * k1b)
            k3a, k3b = rhs(*c1, a + 0.5 * h * k2a, b + 0.5 * h * k2b)
            k4a, k4b = rhs(*c2, a + h * k3a, b + h * k3b)
            a += h / 6.0 * (k1a + 2.0 * k2a + 2.0 * k3a + k4a)
            b += h / 6.0 * (k1b + 2.0 * k2b + 2.0 * k3b + k4b)
            new = math.atan2(b, a)
            change = new - raw
            if change > math.pi:  # bring the change of angle into (-pi, pi]
                change -= 2.0 * math.pi
            elif change <= -math.pi:
                change += 2.0 * math.pi
            theta += change
            raw = new
            r2 = a * a + b * b
            area += 0.5 * h * (r2_prev + r2)  # trapezoid rule over this step
            r2_prev = r2
            if store:
                nodes.append((a, b))
        return j * theta, fh * area / r2_prev, nodes


    FREE_MASS = [MASS] * GRID["points"]  # M = m everywhere (no interaction)
    FREE_POT = [0.0] * GRID["points"]  # v = 0 everywhere
    phi_zero, _, _ = shoot(0.0, 0.0, 1, 0.0, FREE_MASS, FREE_POT)
    report("Phi(0) for k = 0, j = +1 (the zero mode: b stays 0)", phi_zero)
    check(phi_zero == 0.0, "at eps = 0 and k = 0 the Pruefer angle stays exactly 0")
    '''),
    md(r"""
    Why $d\Phi/d\varepsilon = f\int r^2 dy / r(0)^2$, line by line. Call
    $u = \partial\theta/\partial\varepsilon$. (1) Differentiating the angle equation
    $\theta' = f[j(\varepsilon - v) - \kappa k\cos 2\theta - M\sin 2\theta]$ with
    respect to $\varepsilon$ gives $u' = f[j + (2\kappa k\sin 2\theta - 2M\cos
    2\theta)\,u]$ (chain rule), with $u(-L) = 0$ because $\theta(-L) = 0$ for every
    $\varepsilon$. (2) The length $r$ obeys $(\ln r)' = (a a' + b b')/r^2 =
    f[M\cos 2\theta - \kappa k\sin 2\theta]$ (insert the system; the terms with
    $j(\varepsilon - v)$ cancel). (3) So $u' = fj - 2(\ln r)'\,u$, and therefore
    $(r^2 u)' = r^2 u' + 2 r r' u = fj r^2$ (product rule). (4) Integrating from the
    tip to the fold: $r(0)^2 u(0) = fj\int r^2 dy$. (5) Since $\Phi = j\theta(0)$ and
    $j^2 = 1$, $d\Phi/d\varepsilon = j u(0) = f\int r^2 dy / r(0)^2 > 0$. This is the
    strict increase of $\Phi$ in a formula, and the derivative that Newton's method
    uses.
    """),
    md(r"""
    ## 7. The phase function and the levels it labels

    The next cell evaluates $\Phi(\varepsilon)$ at 401 energies from $-4$ to $4$ for
    $k = 0$, $j = +1$, without interaction, at the first slice, and draws $\Phi/\pi$.
    The levels with the even fold condition are where $\Phi/\pi$ crosses a whole number,
    those with the odd fold condition where it crosses a whole number plus one half.
    The check confirms that $\Phi$ increases at every one of the 400 steps.
    """),
    code(r'''
    energies = np.linspace(-4.0, 4.0, 401)  # 401 trial energies
    phase = np.array([shoot(e, 0.0, 1, 0.0, FREE_MASS, FREE_POT)[0] for e in energies])
    fig, ax = plt.subplots(figsize=(7.5, 4.5))
    ax.plot(energies, phase / math.pi, color=PALETTE[0], lw=2.0,
            label="$\\Phi(\\varepsilon)/\\pi$, $k = 0$, $j = +1$")
    for whole in range(-4, 5):
        ax.axhline(whole, color=PALETTE[1], lw=0.8, alpha=0.7)  # even targets l pi
        ax.axhline(whole + 0.5, color=PALETTE[2], lw=0.8, ls="--", alpha=0.7)  # odd
    ax.plot([], [], color=PALETTE[1], lw=0.8, label="even targets $l$")
    ax.plot([], [], color=PALETTE[2], lw=0.8, ls="--", label="odd targets $l + 1/2$")
    ax.set_xlabel("trial energy $\\varepsilon$ (units of $m$)")
    ax.set_ylabel("$\\Phi(\\varepsilon) / \\pi$")
    ax.set_title("The phase function counts the levels")
    ax.set_ylim(-3.2, 3.2)
    ax.legend(fontsize=8, loc="upper left")
    save_figure(fig, "phase_function",
                "The phase function $\\Phi(\\varepsilon)/\\pi$ (vertical axis) of the "
                "free block $j = +1$ at $k = 0$ and $a_{4,0} = 0$ against the trial "
                "energy $\\varepsilon$ (horizontal axis, units of $m$). It rises "
                "steadily; it crosses a solid line (a whole number $l$) at each level "
                "with the even fold condition and a dashed line ($l + 1/2$) at each "
                "level with the odd fold condition. The flat part around "
                "$\\varepsilon = 0$ is the gap of the free field, with the zero mode at "
                "$\\Phi = 0$.")
    check(bool(np.all(np.diff(phase) > 0.0)), "Phi increases strictly at all 400 steps")
    '''),
    md(r"""
    ## 8. Finding a level: Newton's method inside a bracket

    The next cell finds the level with label $l$: the root of $\Phi(\varepsilon) - t_l$
    with the target $t_l = l\pi$ (even) or $\pi/2 + l\pi$ (odd). It is the solver's
    `find_level`, step for step: from a guess it walks with doubling steps (up if
    $\Phi < t_l$, down otherwise) until the sign of $\Phi - t_l$ changes (a bracket),
    then it takes Newton steps $\varepsilon \to \varepsilon - (\Phi - t_l)/\Phi'$ and
    falls back to bisection whenever a Newton step would leave the bracket or the
    previous step did not halve the error. It stops when the bracket is shorter than
    the tolerance ($10^{-13}$ unless another is asked for), or when a Newton step moved
    the energy by at most the tolerance (Newton's method approaches the root from one
    side, so the bracket itself need not shrink).
    """),
    code(r'''
    def target(parity, label):
        """Phi of the level with this label: l pi (even) or pi/2 + l pi (odd)."""
        return label * math.pi + (0.0 if parity == "even" else 0.5 * math.pi)


    def find_level(k, j, parity, label, a4, mass, pot, guess, grid=GRID, tol=1e-13):
        """The energy of the level (k, j, parity, label) in the potentials mass, pot."""
        t = target(parity, label)
        def g(e):  # Phi - target and its derivative at the energy e
            phi, dphi, _ = shoot(e, k, j, a4, mass, pot, grid)
            return phi - t, dphi
        ec = guess
        gc, dc = g(ec)
        if gc == 0.0:
            return ec
        step = min(max(abs(gc / dc) * 1.2, 1e-4), 2.0)  # the first trial step
        if gc < 0.0:  # Phi is too small: walk up until Phi - t >= 0
            lo = ec
            while True:
                e = lo + step
                ge, de = g(e)
                if ge >= 0.0:
                    hi = e  # now [lo, hi] brackets the root
                    if abs(ge) < abs(gc):
                        ec, gc, dc = e, ge, de  # keep the better end for Newton
                    break
                lo, ec, gc, dc = e, e, ge, de
                step *= 2.0  # double the step
        else:  # Phi is too large: walk down until Phi - t <= 0
            hi = ec
            while True:
                e = hi - step
                ge, de = g(e)
                if ge <= 0.0:
                    lo = e
                    if abs(ge) < abs(gc):
                        ec, gc, dc = e, ge, de
                    break
                hi, ec, gc, dc = e, e, ge, de
                step *= 2.0
        if gc == 0.0:
            return ec
        previous = math.inf
        for _ in range(300):
            if hi - lo <= tol:
                break
            new = ec - gc / dc  # the Newton step
            bisect = not lo < new < hi or abs(gc) > 0.5 * previous
            if bisect:
                new = 0.5 * (lo + hi)  # bisection instead
            previous = abs(gc)
            moved = abs(new - ec)  # how far this step moved the energy
            ec = new
            gc, dc = g(ec)
            if gc == 0.0:
                break
            if gc < 0.0:
                lo = ec
            else:
                hi = ec
            if moved <= tol and not bisect:
                break  # a Newton step that moves less than tol: converged
        return ec
    '''),
    md(r"""
    The next cell computes the exact levels at $k = 0$ (the even ones from the formula,
    the odd ones by bisection on $M\sin(pfL) + p\cos(pfL) = 0$, which is
    $\tan(pfL) = -p/M$ multiplied by $M\cos(pfL)$), finds the labels $-3$ to $5$ of both
    fold conditions by shooting at the slices $a_{4,0} = 0$ ($f = 1$) and
    $a_{4,0} = 1.5$ ($f = e^{-1/2}$), and compares. It also compares with the solver's
    own numerical values in the record file `spectrum/free-k0-analytic.csv` (columns
    `m`, `L`, `a4`, `f`, `parity`, `label`, `eps_numeric`, `eps_analytic`,
    `difference`): the same method on the same grid must give the same numbers to the
    root tolerance.
    """),
    code(r'''
    def odd_momentum(n, fh):
        """The n-th root p of M sin(p f L) + p cos(p f L) = 0 (f L the hidden length)."""
        lo, hi = (n - 0.5) * math.pi / (fh * L), n * math.pi / (fh * L)
        g = lambda p: MASS * math.sin(p * fh * L) + p * math.cos(p * fh * L)
        for _ in range(200):
            mid = 0.5 * (lo + hi)
            lo, hi = (mid, hi) if g(lo) * g(mid) > 0.0 else (lo, mid)
        return 0.5 * (lo + hi)


    def exact_level(parity, label, fh=1.0):
        """The exact free level at k = 0 with this label (L = 3, M = 1, hidden scale f)."""
        if parity == "even":
            n = abs(label)
            return math.copysign(math.sqrt(MASS ** 2 + (n * math.pi / (fh * L)) ** 2),
                                 label) if n else 0.0
        n = label + 1 if label >= 0 else -label  # labels 0, 1, ... and -1, -2, ...
        return math.copysign(math.sqrt(MASS ** 2 + odd_momentum(n, fh) ** 2), label + 0.5)


    RECORD_FREE = "Revision/kohn_sham/results/spectrum/free-k0-analytic.csv"
    recorded = {}
    for line in repository_file(RECORD_FREE).read_text(encoding="utf-8").split("\n")[1:]:
        if line:
            m_, l_, a4_, f_, parity, label, eps_num, eps_exact, _ = line.split(",")
            if float(m_) == 1.0 and float(l_) == 3.0:
                recorded[(float(a4_), parity, int(label))] = (float(eps_num),
                                                              float(eps_exact))
    worst_exact, worst_record = 0.0, 0.0
    say("a4,0  parity label   shooting           exact              difference")
    for a4 in (0.0, 1.5):
        fh = hidden_scale(a4)
        for parity in ("even", "odd"):
            for label in range(-3, 6):
                exact = exact_level(parity, label, fh)
                found = find_level(0.0, 1, parity, label, a4, FREE_MASS, FREE_POT,
                                   exact + 0.01)
                say(f"{a4:4.1f}  {parity:5} {label:3d}  {found:17.13f}  {exact:17.13f}"
                    f"  {found - exact:10.2e}")
                if abs(exact) < 4.0:
                    worst_exact = max(worst_exact, abs(found - exact))
                if (a4, parity, label) in recorded:
                    worst_record = max(worst_record,
                                       abs(found - recorded[(a4, parity, label)][0]))
    report("largest |shooting - exact| for |eps| < 4", f"{worst_exact:.2e}")
    report("largest |this notebook - solver record|", f"{worst_record:.2e}")
    check(worst_exact < 5e-9,
          "the shooting levels equal the exact levels within 5e-9 for |eps| < 4",
          record="Revision/kohn_sham/reports/ks-rust-solver.json, check "
                 "free_k0_analytic_spectra")
    check(worst_record < 1e-12, "the levels equal the solver's levels within 1e-12",
          record=f"{RECORD_FREE}, column eps_numeric")
    '''),
    md(r"""
    ## 9. Orbitals: the values in the middle of the steps, and the normalisation

    RK4 gives the orbital at the step ends. The densities (and the potentials) are
    needed on the whole fine grid, so the solver fills in each midpoint by **cubic
    Hermite interpolation**: with the values $u_0, u_1$ and derivatives $u'_0, u'_1$ at
    the two ends of a step of length $h$, the midpoint value is
    $\tfrac12(u_0 + u_1) + \tfrac{h}{8}(u'_0 - u'_1)$ (exact for every cubic polynomial;
    the derivatives come from the equation itself). Then the orbital is normalised with
    Simpson's rule. The next cell defines this and draws three orbitals: the zero mode
    at $a_{4,0} = 0$, the first even bulk level at $k = 0$ and $a_{4,0} = 0$, and the
    fold-band level at $k = 0.5$ (the shell $n_2 = 4$) at the last slice
    $a_{4,0} = 2$. The check compares the zero mode and the fold-band orbital with
    their exact form $a = \sqrt{2fM/(1 - e^{-2fML})}\,e^{fMy}$, $b = 0$, and the
    fold-band level with $\kappa k = 0.5\,e^{-2}$.
    """),
    code(r'''
    def orbital(eps, k, j, a4, mass, pot, grid=GRID):
        """The normalised orbital (a, b) on the fine grid (two numpy arrays)."""
        _, _, nodes = shoot(eps, k, j, a4, mass, pot, grid, store=True)
        h = grid["h"]
        fh = hidden_scale(a4)
        kk = fh * k * math.exp(-a4)  # f kappa k
        a = np.zeros(grid["points"])
        b = np.zeros(grid["points"])
        a[0::2] = [p[0] for p in nodes]  # the step ends
        b[0::2] = [p[1] for p in nodes]
        f = np.arange(0, grid["points"], 2)  # fine indices of the step ends
        m_y = fh * np.array(mass)[f]  # f M at the step ends
        je = fh * j * (eps - np.array(pot)[f])  # f j (eps - v)
        da = m_y * a[f] - (kk + je) * b[f]  # derivatives from the equation
        db = (je - kk) * a[f] - m_y * b[f]
        a[1::2] = 0.5 * (a[f][:-1] + a[f][1:]) + h / 8.0 * (da[:-1] - da[1:])
        b[1::2] = 0.5 * (b[f][:-1] + b[f][1:]) + h / 8.0 * (db[:-1] - db[1:])
        norm = math.sqrt(float(np.sum(grid["simpson"] * (a * a + b * b))))
        return a / norm, b / norm


    def exact_fold_orbital(a4):
        """The normalised orbital (e^{f M y}, 0) of the zero mode and the fold band."""
        fm = hidden_scale(a4) * MASS
        return math.sqrt(2.0 * fm / (1.0 - math.exp(-2.0 * fm * L))) * np.exp(fm * Y)


    zero_a, zero_b = orbital(0.0, 0.0, 1, 0.0, FREE_MASS, FREE_POT)
    bulk_eps = find_level(0.0, 1, "even", 1, 0.0, FREE_MASS, FREE_POT, 1.4)
    bulk_a, bulk_b = orbital(bulk_eps, 0.0, 1, 0.0, FREE_MASS, FREE_POT)
    band_eps = find_level(0.5, 1, "even", 0, 2.0, FREE_MASS, FREE_POT, 0.06)
    band_a, band_b = orbital(band_eps, 0.5, 1, 2.0, FREE_MASS, FREE_POT)
    fig, axes = plt.subplots(1, 3, figsize=(10.5, 3.6), sharey=True,
                             layout="constrained")
    for ax, (a, b, title) in zip(axes, [
            (zero_a, zero_b, "zero mode, $k = 0$, $a_{4,0} = 0$"),
            (bulk_a, bulk_b, f"bulk, $k = 0$, $\\varepsilon = {bulk_eps:.4f}$"),
            (band_a, band_b, f"fold band, $k = 0.5$, $a_{{4,0}} = 2$")]):
        ax.plot(Y, a, color=PALETTE[0], lw=2.0, label="$a(y)$")
        ax.plot(Y, b, color=PALETTE[1], lw=2.0, ls="--", label="$b(y)$")
        ax.set_title(title, fontsize=9)
        ax.set_xlabel("hidden coordinate $y$")
    axes[0].set_ylabel("orbital (normalised)")
    axes[0].legend()
    save_figure(fig, "orbitals",
                "Three normalised orbitals of the free block $j = +1$ (components $a$, "
                "solid, and $b$, dashed; vertical axis, units of $m^{1/2}$) against the "
                "hidden coordinate $y$ (horizontal axis, tip at $-3$, fold at $0$): the "
                "zero mode at $k = 0$ and $a_{4,0} = 0$, which is $e^{y}$ and sits at "
                "the fold; the first even bulk level at $k = 0$, which fills the whole "
                "interval; and the fold-band level at $k = 0.5$ at $a_{4,0} = 2$, which "
                "is again the zero-mode orbital $e^{fy}$, now with the smaller hidden "
                "scale $f = e^{-2/3}$ and therefore spread toward the tip. Each "
                "satisfies $b = 0$ at the tip and at the fold.")
    fold_error = max(float(np.max(np.abs(zero_a - exact_fold_orbital(0.0)))),
                     float(np.max(np.abs(band_a - exact_fold_orbital(2.0)))),
                     float(np.max(np.abs(zero_b))), float(np.max(np.abs(band_b))))
    report("fold-band level at k = 0.5, a4,0 = 2, and kappa k", f"{band_eps:.15f}, "
           f"{0.5 * math.exp(-2.0):.15f}")
    report("largest deviation of the two orbitals from (e^{f M y}, 0)", f"{fold_error:.2e}")
    check(fold_error < 1e-11 and abs(band_eps - 0.5 * math.exp(-2.0)) < 1e-13,
          "the zero mode and the fold band are (e^{f M y}, 0) at eps = kappa k, to 1e-11",
          record="Revision/kohn_sham/reports/ks-rust-solver.json, check "
                 "free_zero_mode_exact")
    '''),
    md(r"""
    ## 10. How accurate is RK4? The order 4

    The error of RK4 falls like $h^4$: halving the step divides it by $2^4 = 16$. The
    next cell finds the even levels with the labels 2 and 3 at $k = 0$ and $a_{4,0} = 0$
    (exact values $\sqrt{1 + (2\pi/3)^2}$ and $\sqrt{1 + \pi^2}$) on grids of 100, 200,
    400 and 800 steps, prints the errors and their ratios, and draws the errors against
    the step on logarithmic axes, where $h^4$ is a straight line of slope 4. The solver
    measured the ratio 16.00 between its canonical and refined runs (Revision record
    ks-rust-determinism.json, check `refined_free_spectra_convergence_order`).
    """),
    code(r'''
    STEPS = [100, 200, 400, 800]
    errors = {2: [], 3: []}
    for steps in STEPS:
        grid = make_grid(steps)
        mass = [MASS] * grid["points"]
        pot = [0.0] * grid["points"]
        for label in errors:
            found = find_level(0.0, 1, "even", label, 0.0, mass, pot,
                               exact_level("even", label), grid=grid)
            errors[label].append(abs(found - exact_level("even", label)))
    ratios = []
    for label, errs in errors.items():
        steps_ratios = [errs[i] / errs[i + 1] for i in range(len(errs) - 1)]
        ratios += steps_ratios
        say(f"label {label}: errors " + ", ".join(f"{e:.2e}" for e in errs)
            + "; ratios " + ", ".join(f"{r:.2f}" for r in steps_ratios))
    steps_h = [L / s for s in STEPS]
    fig, ax = plt.subplots()
    for colour, (label, errs) in zip(PALETTE, errors.items()):
        ax.loglog(steps_h, errs, "o-", color=colour, lw=2.0, ms=7,
                  label=f"even level $l = {label}$")
    ax.loglog(steps_h, [errors[3][0] * (s / steps_h[0]) ** 4 for s in steps_h], "--",
              color="0.4", lw=1.2, label="slope 4: error $\\propto h^4$")
    ax.set_xlabel("step $h$ (units of $1/m$)")
    ax.set_ylabel("|shooting level - exact level| (units of $m$)")
    ax.set_title("RK4: halving the step divides the error by 16")
    ax.legend()
    save_figure(fig, "rk4_convergence",
                "Error of two shooting levels (vertical axis, logarithmic, units of $m$) "
                "against the RK4 step $h = 3/G$ for $G = 100$, $200$, $400$, $800$ steps "
                "(horizontal axis, logarithmic): the points lie on lines of slope 4, the "
                "dashed reference, so halving the step divides the error by 16, the "
                "fourth order of the classical Runge-Kutta method.")
    middle = sorted(ratios)[len(ratios) // 2]
    report("median error ratio for halving the step", f"{middle:.2f}")
    check(15.0 < middle < 17.0, "the error ratio is 16 within 1 (fourth order)",
          record="Revision/kohn_sham/reports/ks-rust-determinism.json, check "
                 "refined_free_spectra_convergence_order")
    '''),
    md(r"""
    ## 11. The fold band and the deflating history

    For every $k$ the lowest even level of $j = +1$ (label 0) is the **fold band**, and
    section 4 showed that it is exactly $\varepsilon = \kappa k = k\,e^{-a_{4,0}}$ with
    the zero-mode orbital: a straight line through the origin with the slope
    $c = e^{-a_{4,0}}$ (Revision/kohn_sham/ks-theory.json, checksNumeric: $c = 1$ at
    $a_{4,0} = 0$, for every $M$, $L$ and $f$; the record keeps the key name
    `braneBandSlope_a0` of an earlier construction). The next cell computes the band by
    shooting at 41 momenta from 0 to 2 at the slices $a_{4,0} = 0$, $1$, $2$ and
    compares every level with $\kappa k$; it measures the slope at $k = 0$ as
    $\varepsilon(k)/k$ at $k = 10^{-4}$ (with the root tolerance $10^{-17}$, so that the
    division by $k$ does not magnify the tolerance); and it computes the first bulk
    level of the same sector (label 1) at 21 momenta, which does not redshift: at small
    $k$ it rises along the history, because the hidden direction shrinks and the bulk
    levels at $k = 0$ are $\sqrt{M^2 + (n\pi/(fL))^2}$. Finally it checks the
    **rescaling identity** of the record without interaction,
    $\varepsilon(k, a_{4,0}; L) = \varepsilon(k\,e^{-a_{4,0}}, 0; f_0 L)$: the level at
    the slice $a_{4,0}$ equals the level at the slice 0 with the redshifted momentum
    $k\,e^{-a_{4,0}}$ on the shorter interval of length $f_0 L$, $f_0 = e^{-a_{4,0}/3}$,
    computed with the same number of RK4 steps. The reason: with $Y = f_0 y$ the block
    equation of the slice becomes the block equation of the slice 0 in $Y$, because
    $f_0\,d/dY = d/dy$ and $\kappa k = (k\,e^{-a_{4,0}}) \cdot 1$.
    """),
    code(r'''
    THEORY = json.loads(repository_file("Revision/kohn_sham/ks-theory.json").read_text(
        encoding="utf-8"))  # the theory file of the solver
    C_RECORD = float(THEORY["checksNumeric"]["braneBandSlope_a0"])  # c at a4,0 = 0


    def band(k, a4, tol=1e-13):
        """The fold-band level (j = +1, even, label 0) at momentum k and slice a4."""
        return find_level(k, 1, "even", 0, a4, FREE_MASS, FREE_POT,
                          0.9 * k * math.exp(-a4), tol=tol)


    def bulk(k, a4):
        """The first bulk level (j = +1, even, label 1) at momentum k and slice a4."""
        guess = math.hypot(exact_level("even", 1, hidden_scale(a4)), k * math.exp(-a4))
        return find_level(k, 1, "even", 1, a4, FREE_MASS, FREE_POT, guess)


    momenta = np.linspace(0.0, 2.0, 41)
    fig, ax = plt.subplots()
    worst_band, slopes = 0.0, []
    for shade, a4 in zip(("#86b6ef", "#2a78d6", "#104281"), (0.0, 1.0, 2.0)):
        curve = [band(k, a4) for k in momenta]
        worst_band = max([worst_band] + [abs(e - k * math.exp(-a4))
                                         for e, k in zip(curve, momenta)])
        ax.plot(momenta, curve, "o", color=shade, ms=4, label=f"$a_{{4,0}} = {a4:.0f}$")
        ax.plot(momenta, momenta * math.exp(-a4), "-", color=shade, lw=1.2)
        ax.plot(momenta[::2], [bulk(k, a4) for k in momenta[::2]], "--", color=shade,
                lw=1.5)
        slopes.append(band(1e-4, a4, tol=1e-17) / 1e-4 * math.exp(a4))  # c e^{a4,0}
    ax.plot([], [], "-", color="0.4", label="$\\kappa k = k\\,e^{-a_{4,0}}$")
    ax.plot([], [], "--", color="0.4", label="first bulk level, same sector")
    ax.set_xlabel("3-momentum $k$ (units of $m$)")
    ax.set_ylabel("level $\\varepsilon$ (units of $m$)")
    ax.set_title("The fold band redshifts, the bulk levels rise")
    ax.legend(fontsize=8)
    save_figure(fig, "fold_band",
                "The fold-band level $\\varepsilon(k)$ (dots, by shooting; vertical axis, "
                "units of $m$) against the 3-momentum $k$ (horizontal axis, units of "
                "$m$) at the slices $a_{4,0} = 0$, $1$, $2$ (light to dark blue), on "
                "the exact lines $\\kappa k = k\\,e^{-a_{4,0}}$: along the deflating "
                "history the band is turned down toward $\\varepsilon = 0$, each line "
                "the previous one with the momentum axis stretched by $e = 2.718$. "
                "Dashed: the first bulk level of the same sector, which at small $k$ "
                "rises along the history, because the hidden direction shrinks.")
    rescale = 0.0
    for a4 in (0.5, 1.0, 2.0):
        partner_grid = make_grid(900, hidden_scale(a4) * L)  # slice 0, length f0 L
        for k in (0.25, 1.0, 2.5):
            for parity, label in (("even", 1), ("odd", 0)):
                guess = math.hypot(exact_level(parity, label, hidden_scale(a4)),
                                   k * math.exp(-a4))
                level = find_level(k, 1, parity, label, a4, FREE_MASS, FREE_POT, guess)
                partner = find_level(k * math.exp(-a4), 1, parity, label, 0.0, FREE_MASS,
                                     FREE_POT, level, grid=partner_grid)
                rescale = max(rescale, abs(level - partner))
    report("largest |fold-band level - kappa k| (123 levels)", f"{worst_band:.1e}")
    report("slope c times e^{a4,0} at a4,0 = 0, 1, 2",
           ", ".join(f"{s:.12f}" for s in slopes))
    report("bulk level at k = 0 for a4,0 = 0, 1, 2",
           ", ".join(f"{bulk(0.0, a4):.6f}" for a4 in (0.0, 1.0, 2.0)))
    report("largest violation of the rescaling identity", f"{rescale:.1e}")
    check(worst_band < 1e-12, "the fold band is eps = kappa k = k e^{-a4,0} within 1e-12",
          record="Revision/kohn_sham/ks-theory.json, boundaryConditions.tip")
    check(max(abs(s - C_RECORD) for s in slopes) < 1e-9 * C_RECORD,
          "the fold-band slope is c e^{-a4,0} with c = 1",
          record="Revision/kohn_sham/reports/ks-rust-solver.json, check "
                 "free_brane_band_slope")
    check(rescale < 1e-12, "eps(k, a4,0; L) = eps(k e^{-a4,0}, 0; f0 L) within 1e-12",
          record="Revision/kohn_sham/reports/ks-rust-solver.json, check "
                 "free_rescaling_relation_and_band_monotone")
    '''),
    md(r"""
    ## 12. The self-consistent loop for N = 8

    Now the interaction. The eight particles of the state $N = 8$ fill the zero modes of
    both block types $j = \pm 1$ at $k = 0$ (four orbitals each). The next cell defines
    one **iteration**: from the current potentials ($M - m$ and $v$ on the fine grid,
    one vector `x` of length $2 \times 1801$) it finds the two occupied levels
    (label 0, even fold condition, $k = 0$, $j = \pm 1$), builds their normalised
    orbitals, the proper densities $n$ and $S$ with $P = e^{-3Hy}/\mathrm{Vol}_7$, the
    output potentials, the residual (largest difference between output and input) and
    the energy $E_{KS}$. It also defines **Anderson mixing** exactly as the solver does:
    it keeps the last six inputs $x_i$ and residuals $r_i$, finds the weights $c_i$ with
    $\sum c_i = 1$ that make $\sum c_i r_i$ as small as possible (a small linear
    system), and takes $\sum c_i (x_i + \beta r_i)$ with $\beta = 0.4$ as the next
    input; its history is cleared when a residual grows tenfold.
    """),
    code(r'''
    POINTS = GRID["points"]


    def iteration(x, lam, a4, guesses):
        """One Kohn-Sham iteration for N = 8; returns (residual, x_out, E, levels)."""
        mass = (MASS + x[:POINTS]).tolist()
        pot = x[POINTS:].tolist()
        p_factor = 1.0 / (E3 * vol7(a4))  # P = e^{-3Hy}/Vol_7 on the fine grid
        n = np.zeros(POINTS)
        s = np.zeros(POINTS)
        levels = {}
        for j in (1, -1):  # the two block types, each level four-fold (g = 4)
            eps = find_level(0.0, j, "even", 0, a4, mass, pot, guesses.get(j, 0.0))
            a, b = orbital(eps, 0.0, j, a4, mass, pot)
            weight = 0.5 * 4.0 * 1.0  # w g f with w = 1/2 (each half holds N/2)
            n += weight * p_factor * (a * a + b * b)
            s += weight * p_factor * j * 2.0 * a * b
            levels[j] = eps
        x_out = np.concatenate([lam * (15.0 / 16.0) * s, lam * (-1.0 / 16.0) * n])
        e_int = lam * (15.0 / 32.0 * s * s - 1.0 / 32.0 * n * n)
        energy = sum(4.0 * e for e in levels.values()) \
            - 2.0 * vol7(a4) * float(np.sum(GRID["simpson"] * E3 * e_int))
        return float(np.max(np.abs(x_out - x))), x_out, energy, levels


    class Anderson:
        """Anderson (Pulay) mixing with the solver's depth 6 and beta 0.4."""

        def __init__(self, depth=6, beta=0.4):
            self.depth, self.beta = depth, beta
            self.xs, self.rs, self.best = [], [], math.inf

        def next(self, x, r):
            size = float(np.max(np.abs(r)))
            if size > 10.0 * self.best and self.xs:
                self.xs, self.rs = [], []  # the residual grew tenfold: start again
            self.best = min(self.best, size)
            self.xs = (self.xs + [x.copy()])[-self.depth:]
            self.rs = (self.rs + [r.copy()])[-self.depth:]
            count = len(self.xs)
            # minimise |sum c_i r_i|^2 with sum c_i = 1 (a Lagrange multiplier):
            system = np.zeros((count + 1, count + 1))
            gram = np.array([[float(np.dot(u, v)) for v in self.rs] for u in self.rs])
            system[:count, :count] = gram + 1e-12 * np.max(np.diag(gram)) * np.eye(count)
            system[:count, count] = 1.0
            system[count, :count] = 1.0
            right = np.zeros(count + 1)
            right[count] = 1.0
            weights = np.linalg.solve(system, right)[:count]
            return sum(c * (xi + self.beta * ri)
                       for c, xi, ri in zip(weights, self.xs, self.rs))


    def solve_n8(lam, a4=0.0, mixing="anderson", tol=1e-11, limit=200):
        """The self-consistent N = 8 state: (E, levels, iteration history, x)."""
        x = np.zeros(2 * POINTS)
        mixer = Anderson()
        guesses, history = {}, []
        for it in range(1, limit + 1):
            residual, x_out, energy, levels = iteration(x, lam, a4, guesses)
            guesses = levels
            history.append((it, residual, energy))
            if residual <= tol:
                return energy, levels, history, x
            r = x_out - x
            x = mixer.next(x, r) if mixing == "anderson" else x + 0.4 * r
        raise RuntimeError("no convergence")
    '''),
    md(r"""
    The next cell reads the coupling $\lambda_1$ of $N = 8$ from the record
    (`parameters.json`), runs the loop with Anderson mixing at the first slice, prints
    the residual and the energy of every iteration, and compares with the record: the
    energy $E_{KS}$ and the occupied level (the HOMO) of the state `N8_lamp1_a00` in
    `ground/summary.csv`, and the residuals of the first six iterations recorded in
    `ground/runs.json` (from the seventh iteration on, the residuals are differences of
    nearly equal numbers and depend on the last digits of the arithmetic, which Python
    and Rust do in a different order, so they are not compared). It checks that both
    block types give the same level, as the exact symmetry
    $\sigma_3 h_j(k)\sigma_3 = h_{-j}(-k)$ of the block Hamiltonian demands at $k = 0$.
    """),
    code(r'''
    params = json.loads(repository_file("Revision/kohn_sham/results/parameters.json")
                        .read_text(encoding="utf-8"))
    calib = {int(c["N"]): c for c in params["couplingCalibration"]["values"]}
    LAM1, LAM2 = calib[8]["lambda1"], calib[8]["lambda2"]
    energy, levels, history, x_final = solve_n8(LAM1)
    say("iteration   residual        E_KS")
    for it, residual, e in history:
        say(f"{it:9d}   {residual:9.3e}   {e:.13e}")
    SUMMARY = "Revision/kohn_sham/results/ground/summary.csv"
    with open(repository_file(SUMMARY), newline="", encoding="utf-8") as handle:
        ground = {row["id"]: row for row in csv.DictReader(handle)}
    runs = {run["id"]: run for run in json.loads(repository_file(
        "Revision/kohn_sham/results/ground/runs.json").read_text(encoding="utf-8"))}
    recorded_history = runs["N8_lamp1_a00"]["scfHistory_iteration_residual_E"]
    early = max(abs(h[1] - r[1]) / r[1] for h, r in zip(history[:6], recorded_history[:6]))
    report("lambda_1 and lambda_2 of N = 8", f"{LAM1} and {LAM2}")
    report("E_KS of N = 8 with lambda_1", f"{energy:.15e}")
    report("iterations (this notebook / record)",
           f"{len(history)} / {len(recorded_history)}")
    report("largest relative difference of the first six residuals", f"{early:.1e}")
    check(abs(energy - float(ground["N8_lamp1_a00"]["E_KS"])) < 1e-14
          and abs(levels[1] - float(ground["N8_lamp1_a00"]["HOMO"])) < 1e-13,
          "E_KS and HOMO of N8_lamp1_a00 reproduced", record=f"{SUMMARY}, row N8_lamp1_a00")
    check(early < 1e-5, "the first six residuals equal the recorded ones within 1e-5",
          record="Revision/kohn_sham/results/ground/runs.json, N8_lamp1_a00")
    check(abs(levels[1] - levels[-1]) < 1e-13, "the levels of j = +1 and j = -1 are equal")
    '''),
    md(r"""
    ## 13. Why Anderson mixing? A comparison with linear mixing

    The next cell solves the same state again with **linear mixing** (the next input is
    $x + 0.4\,r$) and draws both residual histories together with the solver's recorded
    one. Linear mixing reaches the same state but needs several times more iterations;
    the solver's record and this notebook's Anderson run lie on top of each other. The
    two energies agree within $10^{-10}$: each loop stops when the residual is below
    $10^{-11}$, and the energy carries a stopping error of that order.
    """),
    code(r'''
    energy_lin, _, history_lin, _ = solve_n8(LAM1, mixing="linear")
    fig, ax = plt.subplots()
    ax.semilogy([h[0] for h in history_lin], [h[1] for h in history_lin], "s-",
                color=PALETTE[1], ms=4, lw=1.5, label="linear mixing, $\\beta = 0.4$")
    ax.semilogy([h[0] for h in history], [h[1] for h in history], "o-",
                color=PALETTE[0], ms=7, lw=2.0, label="Anderson mixing (this notebook)")
    ax.semilogy([r[0] for r in recorded_history], [r[1] for r in recorded_history], "x",
                color="black", ms=9, label="Anderson mixing (Rust solver, record)")
    ax.axhline(1e-11, color="0.4", ls=":", lw=1.2, label="tolerance $10^{-11}$")
    ax.set_xlabel("iteration")
    ax.set_ylabel("residual (units of $m$)")
    ax.set_title("Self-consistent loop for $N = 8$, $\\lambda = +\\lambda_1$")
    ax.legend(fontsize=8)
    ratio = len(history_lin) / len(history)  # how many times more iterations
    save_figure(fig, "scf_mixing",
                "Residual of the self-consistent loop (vertical axis, logarithmic, units "
                "of $m$) against the iteration (horizontal axis) for $N = 8$ with the "
                "coupling $+\\lambda_1$ at $a_{4,0} = 0$: linear mixing (orange squares) "
                f"needs {ratio:.1f} times as many iterations as Anderson mixing (blue "
                "dots); the crosses are the residuals recorded by the Rust solver, which "
                "agree with this notebook's Anderson run.")
    report("iterations: Anderson / linear", f"{len(history)} / {len(history_lin)}")
    report("|E(linear) - E(Anderson)|", f"{abs(energy_lin - energy):.1e}")
    check(abs(energy_lin - energy) < 1e-10 and len(history_lin) > 2 * len(history),
          "linear mixing reaches the same energy within 1e-10, with more than twice the "
          "iterations")
    '''),
    md(r"""
    ## 14. All four couplings, and an exact symmetry

    The next cell solves $N = 8$ for $+\lambda_1$, $-\lambda_1$, $+\lambda_2$,
    $-\lambda_2$, compares the energies and occupied levels with the record, and computes
    the lowest empty level (the LUMO: the fold band at $k = 0.25$ in the final
    potentials) for $+\lambda_1$. Then it checks an **exact symmetry** of this state:
    changing the sign of $\lambda$ changes the sign of the energy. The reason, line by
    line. (1) At $k = 0$ the real system of block $j$ is $a' = f[M a - j(\varepsilon -
    v)\,b]$, $b' = f[j(\varepsilon - v)\,a - M b]$. (2) Put $\tilde a = a$,
    $\tilde b = -b$, $\tilde\varepsilon = -\varepsilon$, $\tilde v = -v$, the same $M$
    and the same $j$; then $\tilde\varepsilon - \tilde v = -(\varepsilon - v)$, and the
    two equations become $\tilde a' = f[M\tilde a - j(\tilde\varepsilon - \tilde v)\,
    \tilde b]$ and $\tilde b' = f[j(\tilde\varepsilon - \tilde v)\,\tilde a - M\tilde b]$
    (each sign change appears twice and cancels): $(a, -b)$ is an orbital of the problem
    with $(M, -v)$ at the level $-\varepsilon$, with the same boundary conditions
    ($b = 0$ stays $b = 0$) and the same label ($\Phi \to -\Phi$, and the label 0 goes to
    0). (3) Its density $a^2 + b^2$ is the same and its scalar density $2jab$ changes
    sign, so $n \to n$ and $S \to -S$. (4) Under $\lambda \to -\lambda$ the potentials
    of these densities are $M - m = \tfrac{15}{16}(-\lambda)(-S)$, unchanged, and
    $-\tfrac{1}{16}(-\lambda)n = -v$: exactly the potentials assumed in (2), so the
    mapped orbitals form a self-consistent state of $-\lambda$ (the loop started from
    the free state finds exactly this one, as the check shows). (5) Its energy:
    $\sum g f\varepsilon$ changes sign with every level, and
    $e_{int} = \lambda(\tfrac{15}{32}S^2 - \tfrac{1}{32}n^2)$ changes sign with
    $\lambda$ while $S^2$ and $n^2$ stay; so $E_{KS}(-\lambda) = -E_{KS}(\lambda)$.
    """),
    code(r'''
    tags = {"lamp1": LAM1, "lamm1": -LAM1, "lamp2": LAM2, "lamm2": -LAM2}
    results = {}
    worst_e, worst_homo = 0.0, 0.0
    for tag, lam in tags.items():
        e, lv, hist, xf = solve_n8(lam)
        results[tag] = (e, lv[1], xf)
        row = ground[f"N8_{tag}_a00"]
        worst_e = max(worst_e, abs(e - float(row["E_KS"])))
        worst_homo = max(worst_homo, abs(lv[1] - float(row["HOMO"])))
        say(f"{tag}: lambda {lam:+.1f}, E_KS {e:+.12e}, HOMO {lv[1]:+.12e},"
            f" {len(hist)} it.")
    xf = results["lamp1"][2]
    lumo = find_level(0.25, 1, "even", 0, 0.0, (MASS + xf[:POINTS]).tolist(),
                      xf[POINTS:].tolist(), 0.24)
    report("LUMO of N8_lamp1_a00 (fold band at k = 0.25)", f"{lumo:.13f}")
    antisym = max(abs(results["lamp1"][0] + results["lamm1"][0]),
                  abs(results["lamp2"][0] + results["lamm2"][0]))
    report("largest |E(+lambda) + E(-lambda)|", f"{antisym:.1e}")
    check(worst_e < 1e-14 and worst_homo < 1e-13,
          "E_KS and HOMO of all four couplings reproduced", record=f"{SUMMARY}, rows N8")
    check(abs(lumo - float(ground["N8_lamp1_a00"]["LUMO"])) < 1e-12,
          "the LUMO of N8_lamp1_a00 reproduced", record=f"{SUMMARY}, column LUMO")
    check(antisym < 1e-15, "E_KS(-lambda) = -E_KS(+lambda) for N = 8")
    '''),
    md(r"""
    ## 15. The self-consistent potentials of N = 8

    The last figure shows the converged potentials of the four couplings. The potential
    $v = -\lambda n/16$ follows the proper density of the zero modes, which grows toward
    the tip like $e^{2y}e^{-3y} = e^{-y}$ (the free orbital is $e^{fMy} = e^{y}$ at
    $a_{4,0} = 0$, the proper volume $e^{3y}$). The mass shift is smaller: the scalar
    density $S$ of the zero modes vanishes without interaction (there $b = 0$) and is
    created only by the interaction itself; it also vanishes at the tip, where
    $b(-L) = 0$. The check confirms the symmetry of the previous section in the
    potentials: $M - m$ is the same and $v$ changes sign under $\lambda \to -\lambda$.
    """),
    code(r'''
    fig, (left, right) = plt.subplots(1, 2, figsize=(10.0, 4.0), layout="constrained")
    labels = {"lamp1": "$+\\lambda_1$", "lamm1": "$-\\lambda_1$",
              "lamp2": "$+\\lambda_2$", "lamm2": "$-\\lambda_2$"}
    for colour, (tag, label) in zip(PALETTE, labels.items()):
        xf = results[tag][2]
        style = "-" if tag.startswith("lamp") else "--"
        left.plot(Y, xf[:POINTS], style, color=colour, lw=1.8, label=label)
        right.plot(Y, xf[POINTS:], style, color=colour, lw=1.8, label=label)
    left.set_xlabel("hidden coordinate $y$")
    left.set_ylabel("$M(y) - m$ (units of $m$)")
    left.set_title("Mass shift")
    right.set_xlabel("hidden coordinate $y$")
    right.set_ylabel("$v(y)$ (units of $m$)")
    right.set_title("Potential")
    right.legend()
    save_figure(fig, "n8_potentials",
                "The self-consistent mass shift $M(y) - m$ (left) and potential $v(y)$ "
                "(right), vertical axes in units of $m$, of the state $N = 8$ at "
                "$a_{4,0} = 0$ for the couplings $\\pm\\lambda_1$ and $\\pm\\lambda_2$, "
                "against the hidden coordinate $y$. The potential grows toward the tip "
                "roughly like $e^{-y}$ and changes sign with $\\lambda$; the mass shift "
                "is smaller and is the same for $+\\lambda$ and $-\\lambda$ (the dashed "
                "curves lie on the solid ones).")
    plus, minus = results["lamp1"][2], results["lamm1"][2]  # potentials x of +-lambda_1
    mirror = max(float(np.max(np.abs(plus[:POINTS] - minus[:POINTS]))),
                 float(np.max(np.abs(plus[POINTS:] + minus[POINTS:]))))
    report("largest violation of the potential symmetry", f"{mirror:.1e}")
    check(mirror < 1e-12, "M - m is even and v is odd under lambda -> -lambda")
    '''),
    md(r"""
    ## 16. The last check

    The last cell checks that every figure file of this notebook exists and prints the
    number of checks that passed.
    """),
    code(r'''
    NAMES = ["phase_function", "orbitals", "rk4_convergence", "fold_band", "scf_mixing",
             "n8_potentials"]
    missing = [name for number, name in enumerate(NAMES, start=1)
               if not output_file(f"{FIGURE_FOLDER}/15e_{number}_{name}.png").is_file()]
    check(missing == [], "every figure file of this notebook exists")
    all_checks_passed()
    '''),
    md(r"""
    ## 17. What this notebook showed

    - The Pruefer angle turns the search for levels into counting: the phase function
      $\Phi(\varepsilon)$ increases strictly, every level is the crossing with one target
      $l\pi$ or $\pi/2 + l\pi$, and no level can be missed (PROVED by the comparison
      argument of section 4; COMPUTED here for the free spectrum).
    - RK4 shooting on the solver's grid reproduces the exact free levels with the
      hidden scale $f$ (within $5 \times 10^{-9}$ for $|\varepsilon| < 4$, at $f = 1$
      and $f = e^{-1/2}$), the solver's own numbers (within $10^{-12}$) and the fourth
      order of the method (error ratio 16).
    - The fold band is exactly $\varepsilon = \kappa k = k\,e^{-a_{4,0}}$ with the
      zero-mode orbital $(e^{fMy}, 0)$: along the deflating history every 3-momentum is
      redshifted, while the bulk levels at small $k$ rise as the hidden direction
      shrinks; a later slice is the first slice with redshifted momenta on the shorter
      hidden length $f_0 L$ (the rescaling identity).
    - A few dozen lines of Python with Anderson mixing reproduce the interacting $N = 8$
      ground states of the Rust solver: energies, levels and the residuals of the loop.
      Linear mixing converges too, but much more slowly.
    - For $N = 8$ the energy is exactly odd in $\lambda$, a symmetry of the zero-mode
      state found and checked here.
    """),
]

if __name__ == "__main__":
    raise SystemExit(run_builder(__file__))
