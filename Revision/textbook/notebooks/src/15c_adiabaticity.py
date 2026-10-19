#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
"""Builder of Notebook 15c, "Adiabaticity along the deflating history" (textbook
"Universes in Pairs", chapter 15).

The notebook Revision/textbook/notebooks/15c_adiabaticity.ipynb is BUILT from this file by
Revision/textbook/tools/nbkit.py (never edit the .ipynb by hand):

    python Revision/textbook/tools/nbkit.py build \
        Revision/textbook/notebooks/src/15c_adiabaticity.py --date YYYY-MM-DD
    python Revision/textbook/tools/nbkit.py check \
        Revision/textbook/notebooks/src/15c_adiabaticity.py

The notebook recomputes in plain Python (the solver's shooting method, corrected metric of
2026-10-16 with the hidden scale f) the adiabaticity measure Q_nm of every allowed
transition of the free Kohn-Sham states N = 8, 592 and 2352 at the five slices of the
history, reproduces Q_max, its pair, its energy difference and its matrix element from
Revision/kohn_sham/results/adiabatic/adiabaticity.csv, checks the Hellmann-Feynman theorem
and the energy derivative dE/da4, and reproduces the Fermi-level crossing demonstration
(N = 2360).  No Rust is needed.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools"))
from nbkit import code, md, run_builder  # noqa: E402

FIGURES = [
    "15c_1_transition_orbitals",
    "15c_2_q_by_pair",
    "15c_3_q_history",
    "15c_4_hellmann_feynman",
    "15c_5_fermi_crossing",
    "15c_6_q_map",
]

FACTS = {
    "id": "15c",
    "name": "15c_adiabaticity",
    "title": "Adiabaticity along the deflating history",
    "purpose": (
        "It explains when the instantaneous Kohn-Sham states of dirac16complex can be "
        "followed along the deflating history (the adiabatic approximation), recomputes "
        "in plain Python, with the hidden scale of the corrected metric, the "
        "adiabaticity measure Q of every allowed transition of the free states N = 8, "
        "592 and 2352 at the five slices, reproduces the largest Q, its pair of levels, "
        "its energy difference and its matrix element from the committed Revision "
        "record, checks the Hellmann-Feynman theorem and the energy derivative along "
        "the history, and reproduces the Fermi-level crossing of the demonstration "
        "state N = 2360."
    ),
    "records": [
        ["Revision/kohn_sham/results/adiabatic/adiabaticity.csv",
         "the largest Q of every ground state, its pair, energy difference and matrix "
         "element, and dE/da4"],
        ["Revision/kohn_sham/results/adiabatic/crossing-demo.csv",
         "the Fermi-level crossing demonstration N = 2360"],
        ["Revision/kohn_sham/results/adiabatic/fermi-level-crossings.csv",
         "the Fermi-level crossings of the canonical matrix (none)"],
        ["Revision/kohn_sham/results/ground/levels",
         "the level sets with labels and occupations of the ground states"],
        ["Revision/kohn_sham/ks-theory.json",
         "the adiabaticity measure, the derivative of the Hamiltonian, the history and "
         "its status"],
        ["Revision/kohn_sham/reports/ks-rust-solver.json",
         "the checks adiabatic_hellmann_feynman and "
         "adiabatic_crossing_flag_demonstration"],
    ],
    "packages": ["numpy", "matplotlib"],
    "needs_rust": [],
    "expected_seconds": 60,
    "timeout_seconds": 900,
    "files_written": ["Revision/textbook/figures/15c.captions.json"]
    + [f"Revision/textbook/figures/{name}.png" for name in FIGURES],
    "final_lines": [
        "PASS every figure file of this notebook exists",
        "ALL 12 CHECKS PASSED (notebook 15c)",
    ],
    "troubleshooting": [],
}

CELLS = [
    md(r"""
    ## 1. What this notebook computes

    The Kohn-Sham states of the Revision record are **instantaneous** states: at each
    slice $a_{4,0}$ of the history the solver finds the ground state of the Hamiltonian
    of that instant. But the history moves on: $a_4 = A H x_4$ grows with the time
    $x_4$, 3-space inflates, and the extra times and the hidden direction shrink. Does
    the gas follow the instantaneous ground state, or does the motion of the background
    kick particles into higher levels? This is the question of **adiabaticity**. This
    notebook

    - explains the measure $Q_{nm}$ of the Revision record and where it comes from;
    - recomputes in plain Python, with the solver's own shooting method, every
      allowed transition of the free states $N = 8$, $592$ and $2352$ at the five
      slices, and reproduces the largest value $Q_{max}$, the pair of levels, their
      energy difference and the matrix element recorded by the Rust solver;
    - checks the Hellmann-Feynman theorem $d\varepsilon_n/da_4 = \langle n|\partial_a
      h|n\rangle$ and the energy derivative $dE/da_4$;
    - reproduces the **Fermi-level crossing** of the demonstration state $N = 2360$,
      where the instantaneous ground state and the adiabatically followed state differ.

    It draws six figures and needs no Rust.
    """),
    md(r"""
    ## 3. The words used in this notebook

    - **Instantaneous (adiabatic) state**: the ground state of the Hamiltonian
      $h(a_{4,0})$ of one instant of the history (one slice $a_{4,0}$); the history
      itself keeps moving, with 3-space inflating and the extra times deflating.
    - **Adiabatic**: a change of the Hamiltonian slow enough that a system in an
      eigenstate stays in the eigenstate that continues it (the adiabatic theorem).
    - **Transition**: a jump of a particle from an occupied level $n$ to an empty level
      $m$; its **amplitude** is a number whose square is the probability of the jump.
    - **Matrix element** $\langle n|X|m\rangle$: for orbitals $\chi_n = (a_n, i b_n)$
      the integral $\int \chi_n^\dagger X \chi_m\,dy$; for $X = \sigma_3$ it is
      $\int (a_n a_m - b_n b_m)\,dy$, for $X = \sigma_2$ it is
      $\int (a_n b_m + b_n a_m)\,dy$.
    - **Sector**: the shell $n_2$, the block type $j$ and the fold condition (even or
      odd). The exact evolution conserves all three, so transitions happen only inside
      a sector.
    - **Hidden scale** $f = e^{-a_{4,0}/3}$: the factor by which the hidden direction
      has shrunk at the slice; the kinetic term of $h$ carries $1/f$.
    - **Adiabaticity measure** $Q_{nm} = A H |\langle n|\partial_a h|m\rangle| /
      (\varepsilon_n - \varepsilon_m)^2$: the first-order amplitude of the jump
      $n \to m$; $Q_{max}$ is the largest over all allowed pairs.
    - **Hellmann-Feynman theorem**: the derivative of a level with respect to a
      parameter equals the matrix element of the derivative of the Hamiltonian.
    - **Aufbau**: filling the lowest levels with the $N$ particles. **Fermi-level
      crossing**: an empty level comes down below an occupied one along the history,
      so the aufbau filling changes. **Adiabatically continued state**: the state
      that keeps the occupations of the first slice.
    - **Open shell**: a degenerate group of levels only partly filled.
    - **Heat map**: a table of numbers drawn as coloured squares.
    """),
    md(r"""
    ## 4. The physical and mathematical situation

    In the author's corrected metric 3-space $x_1, x_2, x_3$ inflates with $e^{a_4}$,
    and the three extra times $x_5, x_6, x_7$ and the hidden direction deflate with the
    hidden scale $f = e^{-a_4}b_4^{1/2}$; the history is $a_4 = A H x_4$,
    $b_4 = e^{(4/3)AHx_4}$ with $A = 1$, so $f = e^{-a_4/3}$, a PRESCRIBED BACKGROUND
    (Revision record ks-theory.json, adiabaticity.historyStatus). In the hidden
    coordinate $y$ the Kohn-Sham orbitals of a sector obey exactly (ks-theory.json,
    adiabaticity.exactEvolution)

    $$i\,\frac{\partial \chi}{\partial x_4} = h(a_4(x_4))\,\chi, \qquad
    h_j = j\left[-\frac{i}{f}\sigma_1 \frac{d}{dy} + M\sigma_2 + \kappa k \sigma_3\right]
    + v, \qquad \kappa = e^{-a_4}.$$

    **Where $Q$ comes from.** Write $\chi = \sum_m c_m(x_4)\,e^{-i\theta_m}\,\phi_m$ with
    the instantaneous orbitals $h\phi_m = \varepsilon_m\phi_m$ and the phases
    $\theta_m = \int \varepsilon_m\,dx_4$. Inserting into the equation and projecting
    on $\phi_m$ gives, line by line: (1) the left side gives
    $i\dot c_m + \varepsilon_m c_m + i\sum_n c_n e^{i(\theta_m - \theta_n)}\langle
    m|\dot\phi_n\rangle$ (product rule; the dot is $d/dx_4$); (2) the right side gives
    $\varepsilon_m c_m$; (3) so $\dot c_m = -\sum_n c_n e^{i(\theta_m-\theta_n)}\langle
    m|\dot\phi_n\rangle$. (4) Differentiating $h\phi_n = \varepsilon_n\phi_n$ and
    projecting on $\phi_m$ ($m \ne n$) gives $\langle m|\dot\phi_n\rangle = \dot a_4
    \langle m|\partial_a h|n\rangle/(\varepsilon_n - \varepsilon_m)$. (5) Starting from
    $c_n = 1$, integrating (3) over a time in which the phase $e^{i(\varepsilon_m -
    \varepsilon_n)x_4}$ turns many times gives an amplitude of size
    $|\langle m|\dot\phi_n\rangle|/|\varepsilon_m - \varepsilon_n|$ (the integral of
    $e^{i\omega t}$ is $e^{i\omega t}/(i\omega)$), that is, with $\dot a_4 = AH$,

    $$Q_{nm} = A H\,\frac{|\langle n|\partial_a h|m\rangle|}{(\varepsilon_n -
    \varepsilon_m)^2}, \qquad \text{transition probability} \approx Q_{nm}^2 .$$

    The evolution is adiabatic when every $Q_{nm} \ll 1$.

    **The derivative of $h$.** Without interaction ($\lambda = 0$) two things in $h$
    depend on $a_4$: the momentum weight, $\partial\kappa/\partial a_4 = -\kappa$, and
    the hidden scale, $\partial(1/f)/\partial a_4 = \tfrac13(1/f)$ (because
    $1/f = e^{a_4/3}$). So (ks-theory.json, adiabaticity.derivative)

    $$\partial_a h_j = -j\kappa k\sigma_3 + \tfrac13\,T_j, \qquad
    T_j = j\left(-\frac{i}{f}\sigma_1\frac{d}{dy}\right),$$

    and the kinetic term needs no derivative of an orbital: the eigen-equation gives
    $T_j\phi_m = (\varepsilon_m - v - jM\sigma_2 - j\kappa k\sigma_3)\phi_m$. For the
    real orbitals $\chi = (a, ib)$, with $s_0 = a_na_m + b_nb_m$,
    $s_2 = a_nb_m + b_na_m$, $s_3 = a_na_m - b_nb_m$:

    $$\langle n|\partial_a h|m\rangle = \int_{-L}^{0}\Big[-j\kappa k\,s_3 + \tfrac13
    \big(\varepsilon_m s_0 - jM s_2 - j\kappa k\,s_3\big)\Big]dy .$$

    The second term, one third of the kinetic term, comes from the shrinking hidden
    direction; it acts even at $k = 0$. (With interaction the self-consistent potentials
    change too; the solver includes their derivatives. This notebook recomputes the free
    states and shows the recorded values of all states.)

    **Hellmann-Feynman.** For $m = n$ the same steps give
    $d\varepsilon_n/da_4 = \langle n|\partial_a h|n\rangle$, and the energy of the free
    gas, $E = \sum g f\varepsilon$, changes by $dE/da_4 = \sum g f\langle n|\partial_a
    h|n\rangle$.

    The non-adiabatic (time-dependent) problem itself is OPEN; $Q$ is a first-order
    estimate. Units $H = m = 1$, $L = 3$, $\Delta k = 0.25$.
    """),
    md(r"""
    ## 5. The solver's shooting method in Python

    The next cell defines the solver's method for the free problem ($M = m$, $v = 0$):
    the grid of $G = 900$ RK4 steps on $[-3, 0]$ with its fine grid of step ends and
    midpoints, `shoot` (integrate the block equation $a' = f[Ma - (\kappa k +
    j\varepsilon)b]$, $b' = f[(j\varepsilon - \kappa k)a - Mb]$ from the tip, where
    $b = 0$, to the fold, and follow the Pruefer angle $\theta = \mathrm{atan2}(b, a)$;
    the phase $\Phi = j\theta(0)$ increases with $\varepsilon$ and equals $l\pi$ (even
    fold condition) or $\pi/2 + l\pi$ (odd fold condition) at the level with label $l$;
    `shoot` also returns the derivative $d\Phi/d\varepsilon = f\int r^2 dy/r(0)^2$,
    $r^2 = a^2 + b^2$, with the integral by the trapezoid rule on the step ends, as in
    the solver), `find_level` (the solver's Newton method inside a bracket for
    $\Phi(\varepsilon) = $ target: walk with doubling steps until the target is
    bracketed, then Newton steps, with bisection whenever a Newton step leaves the
    bracket or the previous step did not halve the error; stop when the bracket or a
    Newton step is below $10^{-13}$), `orbital` (the normalised orbital on the fine
    grid, with cubic Hermite midpoints) and `da_h` (the matrix element of
    $\partial_a h$ of section 4). Because the free coefficients $fM$, $f\kappa k$ and
    $fj\varepsilon$ do not depend on $y$, every RK4 stage uses the same three numbers.
    The comments say what each line does.
    """),
    code(r'''
    import csv  # reads the tables (CSV files) of the Revision record
    import math  # exp, sqrt, atan2, pi for single numbers

    import numpy as np  # arrays of numbers

    L, STEPS = 3.0, 900  # tip cutoff and number of RK4 steps (the solver's values)
    BETA = 4.0 / 3.0  # the history b4 = e^{beta a4} of the record
    CKIN = 1.0 - 0.5 * BETA  # the weight 1/3 of the kinetic term in d_a h
    POINTS = 2 * STEPS + 1  # step ends and midpoints
    STEP = L / STEPS
    Y = np.array([-L * ((POINTS - 1 - f) / (POINTS - 1)) for f in range(POINTS)])
    SIMPSON = np.full(POINTS, 2.0 * STEP / 6.0)  # Simpson weights on the fine grid
    SIMPSON[1::2] = 4.0 * STEP / 6.0
    SIMPSON[0] = SIMPSON[-1] = STEP / 6.0
    PALETTE = ["#2a78d6", "#eb6834", "#1baf7a", "#eda100", "#e87ba4", "#008300",
               "#4a3aa7", "#e34948"]  # the colours of the figures, in a fixed order


    def coefficients(eps, k, j, a4):
        """f M, f kappa k and f j eps of the free block (M = 1, v = 0) at the slice a4."""
        fh = math.exp((0.5 * BETA - 1.0) * a4)  # the hidden scale f = e^{-a4/3}
        return fh * 1.0, fh * (k * math.exp(-a4)), fh * j * eps, fh


    def shoot(eps, k, j, a4, store=False):
        """Free block: integrate tip -> fold; (Phi, dPhi/deps, nodes)."""
        m_y, kk, je, fh = coefficients(eps, k, j, a4)
        a, b, theta, raw, area, r2_prev = 1.0, 0.0, 0.0, 0.0, 0.0, 1.0
        nodes = [(a, b)] if store else None
        for i in range(STEPS):
            p1a, p1b = m_y * a - (kk + je) * b, (je - kk) * a - m_y * b  # (a', b')
            aa, bb = a + 0.5 * STEP * p1a, b + 0.5 * STEP * p1b
            p2a, p2b = m_y * aa - (kk + je) * bb, (je - kk) * aa - m_y * bb
            aa, bb = a + 0.5 * STEP * p2a, b + 0.5 * STEP * p2b
            p3a, p3b = m_y * aa - (kk + je) * bb, (je - kk) * aa - m_y * bb
            aa, bb = a + STEP * p3a, b + STEP * p3b
            p4a, p4b = m_y * aa - (kk + je) * bb, (je - kk) * aa - m_y * bb
            a += STEP / 6.0 * (p1a + 2.0 * p2a + 2.0 * p3a + p4a)
            b += STEP / 6.0 * (p1b + 2.0 * p2b + 2.0 * p3b + p4b)
            new = math.atan2(b, a)  # the Pruefer angle, followed continuously:
            change = new - raw  # bring the change of angle into (-pi, pi]
            if change > math.pi:
                change -= 2.0 * math.pi
            elif change <= -math.pi:
                change += 2.0 * math.pi
            theta, raw = theta + change, new
            r2 = a * a + b * b
            area, r2_prev = area + 0.5 * STEP * (r2_prev + r2), r2  # trapezoid rule
            if store:
                nodes.append((a, b))
        return j * theta, fh * area / r2_prev, nodes  # Phi and f int r^2 / r(0)^2


    def find_level(k, j, parity, label, a4, guess, tol=1e-13):
        """The level with this label: the solver's Newton method inside a bracket."""
        target = label * math.pi + (0.0 if parity == "even" else 0.5 * math.pi)
        e = guess
        g, d = shoot(e, k, j, a4)[:2]
        g -= target
        if g == 0.0:
            return e
        step = min(max(abs(g / d) * 1.2, 1e-4), 2.0)  # the first trial step
        if g < 0:  # Phi too small: walk up with doubling steps until Phi >= target
            lo = e
            while True:
                trial = lo + step
                gt, dt = shoot(trial, k, j, a4)[:2]
                gt -= target
                if gt >= 0:
                    hi = trial  # [lo, hi] brackets the level
                    if abs(gt) < abs(g):
                        e, g, d = trial, gt, dt  # keep the better end for Newton
                    break
                lo, e, g, d = trial, trial, gt, dt
                step *= 2.0
        else:  # Phi too large: walk down until Phi <= target
            hi = e
            while True:
                trial = hi - step
                gt, dt = shoot(trial, k, j, a4)[:2]
                gt -= target
                if gt <= 0:
                    lo = trial
                    if abs(gt) < abs(g):
                        e, g, d = trial, gt, dt
                    break
                hi, e, g, d = trial, trial, gt, dt
                step *= 2.0
        previous = math.inf
        while hi - lo > tol and g != 0.0:
            new = e - g / d  # Newton step, or bisection if it leaves the bracket
            bisect = not lo < new < hi or abs(g) > 0.5 * previous
            if bisect:
                new = 0.5 * (lo + hi)
            previous = abs(g)
            moved = abs(new - e)
            e = new
            g, d = shoot(e, k, j, a4)[:2]
            g -= target
            if g < 0:
                lo = e
            elif g > 0:
                hi = e
            if moved <= tol and not bisect:
                break  # a Newton step that moves less than tol: converged
        return e


    def orbital(eps, k, j, a4):
        """Normalised orbital (a, b) on the fine grid; Hermite midpoints, Simpson norm."""
        nodes = np.array(shoot(eps, k, j, a4, store=True)[2])
        m_y, kk, je, _ = coefficients(eps, k, j, a4)
        a_n, b_n = nodes[:, 0], nodes[:, 1]
        da = m_y * a_n - (kk + je) * b_n  # derivatives at the step ends
        db = (je - kk) * a_n - m_y * b_n
        a = np.zeros(POINTS)
        b = np.zeros(POINTS)
        a[0::2], b[0::2] = a_n, b_n
        a[1::2] = 0.5 * (a_n[:-1] + a_n[1:]) + STEP / 8.0 * (da[:-1] - da[1:])
        b[1::2] = 0.5 * (b_n[:-1] + b_n[1:]) + STEP / 8.0 * (db[:-1] - db[1:])
        norm = math.sqrt(float(np.sum(SIMPSON * (a * a + b * b))))
        return a / norm, b / norm


    def da_h(k, j, a4, first, second, eps_second, parts=False):
        """<first| d_a h |second>: the integral of -j kappa k s3 + (1/3) T_j terms."""
        kk = k * math.exp(-a4)  # kappa k
        s3 = first[0] * second[0] - first[1] * second[1]
        s2 = first[0] * second[1] + first[1] * second[0]
        s0 = first[0] * second[0] + first[1] * second[1]
        momentum = -j * kk * s3  # from d kappa / d a4 = -kappa
        kinetic = CKIN * (eps_second * s0 - j * 1.0 * s2 - j * kk * s3)  # (1/3) T_j
        if parts:
            return momentum, kinetic  # the two integrands on the fine grid
        return float(np.sum(SIMPSON * (momentum + kinetic)))
    '''),
    md(r"""
    ## 6. The levels of the record, solved again

    The next cell reads the level table of a free ground state from the record (for
    example `ground/levels/N592_lam0_a00.csv`: for each level its shell $n_2$, the
    number $r_3$ of momentum vectors in the shell, $k$, $j$, the fold condition (column
    `parity`), the label $l$, the energy and the occupation $f$), keeps the sectors that
    contain an occupied level (only there can a particle jump), and solves every level
    of these sectors again in Python. Each energy must agree with the solver's to
    $10^{-12}$. The sectors are kept in the solver's order (shell, then block type with
    $j = -1$ first, then the fold condition, even first).
    """),
    code(r'''
    LEVELS = "Revision/kohn_sham/results/ground/levels"
    SLICES = [0.0, 0.5, 1.0, 1.5, 2.0]


    def state_id(n, a4, tag="lam0"):
        return f"N{n}_{tag}_a{round(10 * a4):02d}"


    def solve_state(n, a4):
        """{sector: {label: (eps, f, k, r3, orbital)}} for the sectors with particles."""
        rows = list(csv.DictReader(open(repository_file(f"{LEVELS}/{state_id(n, a4)}.csv"),
                                        newline="", encoding="utf-8")))
        sectors = {}
        for row in rows:
            sector = (int(row["n2"]), int(row["j"]), row["parity"])
            sectors.setdefault(sector, []).append(row)
        solved, worst = {}, 0.0
        for sector in sorted(sectors):  # the solver's order: n2, then j, then parity
            members = sectors[sector]
            if all(float(row["f"]) < 0.5 for row in members):
                continue  # no particle in this sector: no transition starts here
            solved[sector] = {}
            for row in members:
                k, eps_rec = float(row["k"]), float(row["eps"])
                eps = find_level(k, sector[1], sector[2], int(row["label"]), a4, eps_rec)
                worst = max(worst, abs(eps - eps_rec))
                solved[sector][int(row["label"])] = (
                    eps, float(row["f"]), k, int(row["r3"]), orbital(eps, k, sector[1], a4))
        return solved, worst


    states = {}
    worst_level = 0.0
    for n in (8, 592, 2352):
        for a4 in SLICES:
            states[(n, a4)], worst = solve_state(n, a4)
            worst_level = max(worst_level, worst)
    count = sum(len(levels) for state in states.values() for levels in state.values())
    report("levels solved again (15 states)", count)
    report("largest |eps(Python) - eps(solver)|", f"{worst_level:.1e}")
    check(worst_level < 1e-12, "every level equals the solver's level within 1e-12",
          record=f"{LEVELS}/N8_lam0_a*.csv, N592_lam0_a*.csv and N2352_lam0_a*.csv, "
                 "column eps")
    '''),
    md(r"""
    ## 7. The pair of levels with the largest Q

    For $N = 592$ at $a_{4,0} = 0$ the record names the pair with the largest $Q$: from
    the fold-band level of the shell $n_2 = 10$ ($k = 0.79$, the highest occupied
    shell, label 0) to the first bulk level of the same sector (label 1). The next cell
    draws the two orbitals and the two parts of the integrand of their matrix element:
    the momentum part $-j\kappa k\,s_3$ and the kinetic part
    $\tfrac13(\varepsilon_m s_0 - j s_2 - j\kappa k\,s_3)$. The fold-band orbital
    $(e^{fMy}, 0)$ is bound to the fold, the bulk orbital oscillates across the
    interval, so their overlap partly cancels, and the energy difference is large.
    """),
    code(r'''
    sector = (10, 1, "even")
    band = states[(592, 0.0)][sector][0]  # (eps, f, k, r3, (a, b)) of label 0
    bulk = states[(592, 0.0)][sector][1]  # label 1
    k = band[2]
    momentum, kinetic = da_h(k, 1, 0.0, band[4], bulk[4], bulk[0], parts=True)
    fig, (left, right) = plt.subplots(1, 2, figsize=(10.0, 4.0), layout="constrained")
    left.plot(Y, band[4][0], color=PALETTE[0], lw=2.0, label="band: $a$")
    left.plot(Y, band[4][1], color=PALETTE[0], lw=1.5, ls="--", label="band: $b$")
    left.plot(Y, bulk[4][0], color=PALETTE[1], lw=2.0, label="bulk: $a$")
    left.plot(Y, bulk[4][1], color=PALETTE[1], lw=1.5, ls="--", label="bulk: $b$")
    left.set_xlabel("hidden coordinate $y$")
    left.set_ylabel("orbital (normalised)")
    left.set_title(f"$n_2 = 10$: band $\\varepsilon = {band[0]:.4f}$, "
                   f"bulk $\\varepsilon = {bulk[0]:.4f}$", fontsize=10)
    left.legend(fontsize=8)
    right.plot(Y, momentum, color=PALETTE[2], lw=1.5, ls="--", label="momentum part")
    right.plot(Y, kinetic, color=PALETTE[3], lw=1.5, ls=":", label="kinetic part")
    right.plot(Y, momentum + kinetic, color=PALETTE[6], lw=2.0, label="sum")
    right.fill_between(Y, momentum + kinetic, color=PALETTE[6], alpha=0.2)
    right.set_xlabel("hidden coordinate $y$")
    right.set_ylabel("integrand (units of $m$)")
    right.set_title("Integrand of the matrix element")
    right.legend(fontsize=8)
    element = abs(da_h(k, 1, 0.0, band[4], bulk[4], bulk[0]))
    save_figure(fig, "transition_orbitals",
                "Left: the orbitals (components $a$ solid, $b$ dashed; vertical axis, "
                "normalised) of the occupied fold-band level (blue) and the empty bulk "
                "level (orange) of the sector $n_2 = 10$, $j = +1$, even fold "
                "condition, of the free state $N = 592$ at $a_{4,0} = 0$, against $y$ "
                "(horizontal axis). Right: the integrand of their matrix element "
                "$\\langle n|\\partial_a h|m\\rangle$ (units of $m$), its momentum part "
                "and its kinetic part from the shrinking hidden direction; the size of "
                f"the area under the sum is ${element:.4f}\\,m$, and with the energy "
                f"difference ${abs(band[0] - bulk[0]):.4f}\\,m$ it gives "
                f"$Q = {element / (band[0] - bulk[0]) ** 2:.4f}$, the largest of this "
                "state.")
    report("|<band| d_a h |bulk>| and Q for N = 592, a4,0 = 0",
           f"{element:.13f}, {element / (band[0] - bulk[0]) ** 2:.13f}")
    '''),
    md(r"""
    ## 8. Q for every allowed pair, and the comparison with the record

    The next cell computes $Q_{nm}$ for every pair (occupied $n$, empty $m$, same sector)
    of the fifteen free states $N = 8, 592, 2352$ at the five slices, finds the largest,
    and compares the value, the pair (written as the record writes it,
    `n2:j:parity:label -> n2:j:parity:label`), the energy difference and the matrix
    element with the columns `Q_max`, `Q_max_pair`, `Q_max_delta_eps` and
    `Q_max_matrix_element` of `adiabatic/adiabaticity.csv`. Two pairs can have the same
    $Q$: at $k = 0$ the sectors $j = +1$ and $j = -1$ have the same levels and orbitals
    up to the sign of $b$ (the block relation $\sigma_3 h_j(k)\sigma_3 = h_{-j}(-k)$ at
    $k = 0$). The solver keeps the first in its order, and so does the cell: a pair
    replaces the best one found so far only if its $Q$ is larger by more than a
    relative $10^{-12}$.
    """),
    code(r'''
    ADIABATIC = "Revision/kohn_sham/results/adiabatic/adiabaticity.csv"
    with open(repository_file(ADIABATIC), newline="", encoding="utf-8") as handle:
        adiabatic = {row["id"]: row for row in csv.DictReader(handle)}


    def key_text(sector, label):
        return f"{sector[0]}:{sector[1]:+d}:{sector[2]}:{label}"


    pairs = {}  # (n, a4) -> list of (Q, n2, label m) for the figure
    worst_q, same_pairs = 0.0, True
    say("   N  a4,0   Q_max    pair                          delta eps   matrix el.")
    for (n, a4), state in states.items():
        best = (0.0, "", 0.0, 0.0)
        pairs[(n, a4)] = []
        for sector, levels in state.items():
            for ln, (en, fn, k, _, on) in levels.items():
                if fn < 0.5:
                    continue
                for lm, (em, fm, _, _, om) in levels.items():
                    if fm > 0.5:
                        continue
                    element = abs(da_h(k, sector[1], a4, on, om, em))
                    q = element / (en - em) ** 2  # A H = 1
                    pairs[(n, a4)].append((q, sector[0], lm))
                    if q > best[0] * (1.0 + 1e-12):
                        best = (q, f"{key_text(sector, ln)} -> {key_text(sector, lm)}",
                                abs(en - em), element)
        row = adiabatic[state_id(n, a4)]
        for value, column in ((best[0], "Q_max"), (best[2], "Q_max_delta_eps"),
                              (best[3], "Q_max_matrix_element")):
            worst_q = max(worst_q, abs(value / float(row[column]) - 1.0))
        same_pairs = same_pairs and best[1] == row["Q_max_pair"]
        say(f"{n:4d}  {a4:4.1f}  {best[0]:.5f}  {best[1]:28}  {best[2]:9.6f}"
            f"  {best[3]:9.6f}")
    report("largest relative difference to the record", f"{worst_q:.1e}")
    check(worst_q < 1e-9, "Q_max, its energy difference and matrix element reproduced",
          record=f"{ADIABATIC}, columns Q_max, Q_max_delta_eps, Q_max_matrix_element")
    check(same_pairs, "the pair with the largest Q is the recorded pair",
          record=f"{ADIABATIC}, column Q_max_pair")
    '''),
    md(r"""
    The next cell draws all pairs of $N = 8$, $592$ and $2352$ at $a_{4,0} = 0$: $Q$
    against the shell $n_2$ of the sector, coloured by the label $m$ of the empty level.
    In every shell the jump to the next bulk level (label 1) dominates, and for the
    fold-band shells it grows with $n_2$: the momentum part of the matrix element is
    proportional to $k$. The largest $Q$ belongs to the highest occupied shell
    ($n_2 = 10$ for $N = 592$, $n_2 = 26$ for $N = 2352$). The zero modes ($n_2 = 0$)
    can jump too: at $k = 0$ the momentum part vanishes, but the kinetic part of the
    shrinking hidden direction couples the zero mode to the bulk levels of its sector.
    """),
    code(r'''
    fig, ax = plt.subplots()
    for marker, n in (("^", 8), ("o", 592), ("s", 2352)):
        for colour, label in zip(PALETTE, (1, 2)):
            points = [(n2, q) for q, n2, lm in pairs[(n, 0.0)] if lm == label]
            ax.plot([p[0] for p in points], [p[1] for p in points], marker,
                    color=colour, ms=8 if n != 2352 else 6,
                    markerfacecolor=colour if n != 2352 else "white",
                    label=f"$N = {n}$, to label {label}")
    ax.set_yscale("log")
    ax.set_xlabel("shell $n_2$ of the sector ($k = 0.25\\sqrt{n_2}$)")
    ax.set_ylabel("$Q_{nm}$ (pure number)")
    ax.set_title("Every allowed transition at $a_{4,0} = 0$, $\\lambda = 0$")
    ax.legend(fontsize=8)
    largest = max(q for values in pairs.values() for q, _, _ in values)
    save_figure(fig, "q_by_pair",
                "The adiabaticity measure $Q_{nm}$ (vertical axis, logarithmic, pure "
                "number) of every allowed transition of the free states $N = 8$ "
                "(triangles), $N = 592$ (circles) and $N = 2352$ (open squares) at "
                "$a_{4,0} = 0$, against the shell $n_2$ of the sector (horizontal "
                "axis); colour: the label of the empty level. The jumps to label 1 "
                "dominate and grow with the momentum; even the zero modes at $k = 0$ "
                "can jump, through the kinetic term of the shrinking hidden direction. "
                f"All values lie below $0.2$ (the largest is ${largest:.4f}$).")
    report("largest Q of all free pairs (15 states)", f"{largest:.5f}")
    check(largest < 0.2, "every Q of the free states is below 0.2")
    '''),
    md(r"""
    ## 9. Q along the history, for every state of the matrix

    The next cell reads $Q_{max}$ of all 75 ground states from the record (with
    interaction the self-consistent potentials contribute too) and draws it against the
    slice, together with the values computed here for $\lambda = 0$ (black crosses).
    $Q_{max}$ falls along the history: the energy differences of the jumps grow (the
    bulk levels rise as the hidden direction shrinks) while the momenta redshift. The
    right panel shows the transition probability $Q_{max}^2$.
    """),
    code(r'''
    fig, (left, right) = plt.subplots(1, 2, figsize=(10.0, 4.0), layout="constrained")
    tags = [("lam0", "$0$"), ("lamp1", "$+\\lambda_1$"), ("lamm1", "$-\\lambda_1$"),
            ("lamp2", "$+\\lambda_2$"), ("lamm2", "$-\\lambda_2$")]
    record_max, record_state = 0.0, ""
    for style, n in ((":", 8), ("-", 592), ("--", 2352)):
        for colour, (tag, label) in zip(PALETTE, tags):
            values = [float(adiabatic[state_id(n, a4, tag)]["Q_max"]) for a4 in SLICES]
            if max(values) > record_max:
                record_max = max(values)
                record_state = state_id(n, SLICES[values.index(record_max)], tag)
            left.plot(SLICES, values, style, color=colour, lw=1.5, marker="o", ms=3,
                      label=f"$N = {n}$, $\\lambda = $ {label}" if n == 592 else None)
            right.plot(SLICES, [v * v for v in values], style, color=colour, lw=1.5,
                       marker="o", ms=3)
        mine = [max(q for q, _, _ in pairs[(n, a4)]) for a4 in SLICES]
        left.plot(SLICES, mine, "x", color="black", ms=10, mew=2)
    left.plot([], [], "x", color="black", ms=10, mew=2, label="this notebook")
    left.set_yscale("log")
    left.set_xlabel("slice $a_{4,0}$")
    left.set_ylabel("$Q_{max}$")
    left.set_title("Largest $Q$ (record)")
    left.legend(fontsize=7, ncol=2)
    right.set_yscale("log")
    right.set_xlabel("slice $a_{4,0}$")
    right.set_ylabel("$Q_{max}^2$")
    right.set_title("Transition probability estimate")
    save_figure(fig, "q_history",
                "Left: the largest adiabaticity measure $Q_{max}$ (vertical axis, "
                "logarithmic) of the 75 ground states, $N = 8$ (dotted), $N = 592$ "
                "(solid) and $N = 2352$ (dashed), for the five couplings (colours; the "
                "legend names them for $N = 592$), against the slice (horizontal axis), "
                "from the record; black crosses: the values recomputed here for "
                "$\\lambda = 0$. Right: the transition probability estimate "
                f"$Q_{{max}}^2$, below ${record_max ** 2:.3f}$ everywhere. Both fall "
                "along the history.")
    report("largest Q_max of the whole matrix (record) and its state",
           f"{record_max:.7f} ({record_state})")
    check(f"{record_max:.7f}" == "0.1982205" and record_state == "N2352_lamm1_a00",
          "Q_max <= 0.1982205 over the matrix, at N2352_lamm1_a00",
          record=f"{ADIABATIC}, column Q_max")
    falling = all(max(q for q, _, _ in pairs[(n, SLICES[i + 1])])
                  < max(q for q, _, _ in pairs[(n, SLICES[i])])
                  for n in (8, 592, 2352) for i in range(4))
    check(falling, "Q_max of the free states falls from slice to slice")
    '''),
    md(r"""
    ## 10. The Hellmann-Feynman theorem and the energy derivative

    The next cell takes the free state $N = 2352$ at $a_{4,0} = 1$: for each occupied
    fold-band level (shells $n_2 = 1$ to $26$) and for the first bulk level of the same
    sector (label 1) it computes the level also at $a_{4,0} \pm \delta$ and
    $\pm 2\delta$ with $\delta = 0.002$ (the solver's step), forms the **Richardson**
    combination of the two central differences, $\tfrac{1}{3}[4 D(\delta) - D(2\delta)]$
    with $D(s) = [\varepsilon(a+s) - \varepsilon(a-s)]/(2s)$ (it removes the error
    proportional to $\delta^2$), and compares with the matrix element
    $\langle n|\partial_a h|n\rangle$. For a fold-band level $\varepsilon = \kappa k$
    both must be $-\kappa k$; the bulk levels rise at small $k$, because the hidden
    direction shrinks. Then it adds up $dE/da_4 = \sum g f \langle n|\partial_a h|n\rangle$
    over all occupied levels, with the degeneracy $g = 4 r_3(n_2)$, and compares with
    the derivative the solver obtained by finite differences of $E$ (column
    `dE_da4_finite_difference`), which for this fold-band gas is $-E_{KS}$.
    """),
    code(r'''
    DELTA = 2e-3
    a0 = 1.0
    state = states[(2352, a0)]
    shells, finite, element, kinds = [], [], [], []
    for sector, levels in state.items():
        if sector[0] == 0:
            continue  # the zero modes stay at 0
        for label in (0, 1):  # the fold-band level and the first bulk level
            eps, f, k, r3, orb = levels[label]
            near = {s: find_level(k, sector[1], sector[2], label, a0 + s, eps)
                    for s in (DELTA, -DELTA, 2 * DELTA, -2 * DELTA)}
            d1 = (near[DELTA] - near[-DELTA]) / (2 * DELTA)
            d2 = (near[2 * DELTA] - near[-2 * DELTA]) / (4 * DELTA)
            shells.append(k)
            kinds.append(label)
            finite.append((4.0 * d1 - d2) / 3.0)
            element.append(da_h(k, sector[1], a0, orb, orb, eps))
    hf_dev = max(abs(a - b) for a, b in zip(finite, element))
    band_dev = max(abs(e + k * math.exp(-a0)) for e, k, kind in zip(element, shells, kinds)
                   if kind == 0)
    de_da = sum(4.0 * levels[l][3] * levels[l][1] * da_h(levels[l][2], sector[1], a0,
                                                           levels[l][4], levels[l][4],
                                                           levels[l][0])
                for sector, levels in state.items() for l in levels)
    recorded = float(adiabatic[state_id(2352, a0)]["dE_da4_finite_difference"])
    fig, ax = plt.subplots()
    for label, colour, text in ((0, PALETTE[0], "fold band"), (1, PALETTE[1],
                                                               "first bulk level")):
        xs = [s for s, kind in zip(shells, kinds) if kind == label]
        ax.plot(xs, [v for v, kind in zip(finite, kinds) if kind == label], "o",
                color=colour, ms=8, label=f"{text}: finite differences")
        ax.plot(xs, [v for v, kind in zip(element, kinds) if kind == label], "x",
                color="black", ms=8, mew=1.5)
    ax.plot([], [], "x", color="black", ms=8, mew=1.5,
            label="$\\langle n|\\partial_a h|n\\rangle$")
    ax.axhline(0.0, color="0.5", lw=0.8)
    ax.set_xlabel("3-momentum $k$ of the shell (units of $m$)")
    ax.set_ylabel("$d\\varepsilon/da_4$ (units of $m$)")
    ax.set_title("Hellmann-Feynman: $N = 2352$, $\\lambda = 0$, $a_{4,0} = 1$")
    ax.legend(fontsize=8)
    save_figure(fig, "hellmann_feynman",
                "The derivative $d\\varepsilon/da_4$ (vertical axis, units of $m$) of "
                "the occupied fold-band levels (blue) and of the first bulk level of "
                "each of their sectors (orange) of the free state $N = 2352$ at "
                "$a_{4,0} = 1$, against the momentum $k$ of the shell (horizontal "
                "axis): circles from Richardson finite differences of the levels, "
                "crosses from the matrix element of $\\partial_a h$. They agree (the "
                "Hellmann-Feynman theorem). The fold band falls like $-\\kappa k$; the "
                "bulk levels rise at small $k$, because the hidden direction shrinks, "
                "and fall at large $k$, where the momentum term wins.")
    report("largest |finite difference - matrix element| (52 levels)", f"{hf_dev:.1e}")
    report("largest |<n| d_a h |n> + kappa k| of the fold band", f"{band_dev:.1e}")
    report("dE/da4 of N2352_lam0_a10: Hellmann-Feynman / record",
           f"{de_da:.10f} / {recorded:.10f}")
    check(hf_dev < 1e-7 and band_dev < 1e-12,
          "d eps/da4 = <n| d_a h |n> within 1e-7, and -kappa k on the fold band",
          record="Revision/kohn_sham/reports/ks-rust-solver.json, check "
                 "adiabatic_hellmann_feynman")
    check(abs(de_da / recorded - 1.0) < 1e-9, "dE/da4 = sum g f <n| d_a h |n>",
          record=f"{ADIABATIC}, N2352_lam0_a10, column dE_da4_finite_difference")
    '''),
    md(r"""
    ## 11. When the Fermi level is crossed

    Adiabatic evolution keeps the occupation of every level. If an empty level comes
    down below an occupied one along the history (a **Fermi-level crossing**), the
    instantaneous ground state fills the new lower level, but the adiabatically
    evolving gas cannot get there: the two levels lie in different sectors, and the
    exact evolution never moves a particle between sectors. The canonical matrix has no
    such crossing (the record file `adiabatic/fermi-level-crossings.csv`). The record's
    demonstration uses $N = 2360 = 2352 + 8$, the smallest closed shell of the
    $a_{4,0} = 0$ aufbau that occupies a level off the fold band: at $a_{4,0} = 0$ the
    eight extra particles sit in the odd bulk level at $k = 0$ ($\varepsilon = 1.2923$,
    four orbitals for each $j$), while the fold band of the shell $n_2 = 27$
    ($k = 0.25\sqrt{27} = 1.299$, 128 orbitals) lies just above it. Along the history
    the band level comes down like $k\,e^{-a_{4,0}}$ and the bulk level goes up (the
    hidden direction shrinks), so they cross almost at once. The next cell computes both
    levels, finds the slice where they cross by bisection, and computes the energy by
    which the adiabatically continued state lies above the instantaneous ground state,
    $8\,(\varepsilon_{odd} - \varepsilon_{27})$ (in the aufbau state the eight particles
    sit in the band level instead), at the five slices.
    """),
    code(r'''
    K27 = 0.25 * math.sqrt(27.0)


    def odd0(a4):
        """The odd bulk level at k = 0 (label 0) at the slice a4."""
        return find_level(0.0, 1, "odd", 0, a4, 1.3)


    def band27(a4):
        """The fold-band level of the shell n2 = 27 at the slice a4."""
        return find_level(K27, 1, "even", 0, a4, 0.9 * K27 * math.exp(-a4))


    lo, hi = 0.0, 0.5  # bisection for band27(a4) = odd0(a4)
    for _ in range(45):
        mid = 0.5 * (lo + hi)
        lo, hi = (mid, hi) if band27(mid) > odd0(mid) else (lo, mid)
    crossing = 0.5 * (lo + hi)
    dense = np.linspace(0.0, 2.0, 21)
    band_curve = [band27(a) for a in dense]
    odd_curve = [odd0(a) for a in dense]
    with open(repository_file("Revision/kohn_sham/results/adiabatic/crossing-demo.csv"),
              newline="", encoding="utf-8") as handle:
        demo = {float(row["a4"]): row for row in csv.DictReader(handle)}
    mine = {a4: max(0.0, 8.0 * (odd0(a4) - band27(a4))) for a4 in SLICES}
    worst_demo = max(abs(mine[a4] - float(demo[a4]["difference"])) for a4 in SLICES)
    fig, (left, right) = plt.subplots(1, 2, figsize=(10.0, 4.0), layout="constrained")
    left.plot(dense, band_curve, color=PALETTE[0], lw=2.0,
              label="fold band $n_2 = 27$ (128 orbitals)")
    left.plot(dense, odd_curve, color=PALETTE[1], lw=2.0,
              label="odd bulk level, $k = 0$ (8)")
    left.axvline(crossing, color="0.4", ls=":", lw=1.2, label="crossing")
    left.set_xlabel("slice $a_{4,0}$")
    left.set_ylabel("level (units of $m$)")
    left.set_title("Two levels near the Fermi level, $N = 2360$")
    left.legend(fontsize=8)
    right.plot(SLICES, [float(demo[a]["difference"]) for a in SLICES], "o", color="black",
               ms=9, label="record")
    right.plot(SLICES, [mine[a] for a in SLICES], "x", color=PALETTE[0], ms=10, mew=2,
               label="$8(\\varepsilon_{odd} - \\varepsilon_{27})$, this notebook")
    right.set_xlabel("slice $a_{4,0}$")
    right.set_ylabel("$E_{continued} - E_{aufbau}$ (units of $m$)")
    right.set_title("Energy above the instantaneous ground state")
    right.legend(fontsize=8)
    save_figure(fig, "fermi_crossing",
                "The Fermi-level crossing of the demonstration state $N = 2360$ without "
                "interaction. Left: the fold-band level of the shell $n_2 = 27$ (blue) "
                "falls along the history and the odd bulk level at $k = 0$ (orange) "
                f"rises; they cross almost at once, at $a_{{4,0}} = {crossing:.4f}$ "
                "(dotted line), because at $a_{4,0} = 0$ the band lies only "
                f"${band_curve[0] - odd_curve[0]:.4f}\\,m$ above the bulk level; "
                "vertical axis in units of $m$. Right: the energy by which the "
                "adiabatically continued state lies above the instantaneous aufbau "
                "state (vertical axis, units of $m$), from the record (dots) and from "
                "the two levels (crosses), at the five slices.")
    report("band level n2 = 27 minus the odd level at a4,0 = 0",
           f"{band_curve[0] - odd_curve[0]:.10f}")
    report("crossing slice a4,0", f"{crossing:.6f}")
    report("largest |8 (eps_odd - eps_27) - recorded difference|", f"{worst_demo:.1e}")
    check(0.0 < crossing < 0.5, "the crossing lies between the slices 0 and 0.5",
          record="Revision/kohn_sham/results/adiabatic/crossing-demo.csv, flags at 0 "
                 "and 0.5")
    check(worst_demo < 1e-9, "the energy differences of the demonstration reproduced",
          record="Revision/kohn_sham/results/adiabatic/crossing-demo.csv, column "
                 "difference")
    '''),
    md(r"""
    ## 12. The whole matrix at a glance

    The last figure is a heat map of $Q_{max}$ from the record: one row per series
    (particle number and coupling), one column per slice, darker for larger values.
    The check reads the record file of Fermi-level crossings and confirms that none of
    its 60 rows (15 series, 4 steps between slices) reports a change of the occupied set.
    """),
    code(r'''
    rows, names = [], []
    for n in (8, 592, 2352):
        for tag, label in tags:
            rows.append([float(adiabatic[state_id(n, a4, tag)]["Q_max"]) for a4 in SLICES])
            names.append(f"N = {n}, {tag}")
    table = np.array(rows)
    fig, ax = plt.subplots(figsize=(6.5, 6.0))
    image = ax.imshow(table, cmap="Blues", aspect="auto", vmin=0.0, vmax=0.2)
    ax.grid(False)  # no grid lines across the coloured squares
    ax.set_xticks(range(5), [f"{a:.1f}" for a in SLICES])
    ax.set_yticks(range(len(names)), names, fontsize=8)
    for i in range(table.shape[0]):
        for jj in range(table.shape[1]):
            ax.text(jj, i, f"{table[i, jj]:.3f}", ha="center", va="center", fontsize=7,
                    color="white" if table[i, jj] > 0.12 else "black")
    ax.set_xlabel("slice $a_{4,0}$")
    ax.set_title("$Q_{max}$ of the 75 ground states (record)")
    fig.colorbar(image, ax=ax, label="$Q_{max}$")
    save_figure(fig, "q_map",
                "Heat map of the largest adiabaticity measure $Q_{max}$ of the 75 ground "
                "states of the canonical matrix (record): rows are the particle numbers "
                "$N = 8$, $592$, $2352$ with the couplings $0$, $\\pm\\lambda_1$, "
                "$\\pm\\lambda_2$ (tags lam0, lamp1, lamm1, lamp2, lamm2), columns the "
                "slices $a_{4,0}$; the printed numbers are the values. Every value is "
                "below $0.2$, the largest at the start of the history and for the "
                "largest particle number.")
    with open(repository_file("Revision/kohn_sham/results/adiabatic/"
                              "fermi-level-crossings.csv"), newline="",
              encoding="utf-8") as handle:
        crossings = list(csv.DictReader(handle))
    changed = sum(row["occupied_set_changed"] == "true" for row in crossings)
    report("rows of the crossing record / rows with a changed occupied set",
           f"{len(crossings)} / {changed}")
    check(len(crossings) == 60 and changed == 0,
          "no Fermi-level crossing in the canonical matrix",
          record="Revision/kohn_sham/results/adiabatic/fermi-level-crossings.csv")
    '''),
    md(r"""
    ## 13. The last check

    The last cell checks that every figure file of this notebook exists and prints the
    number of checks that passed.
    """),
    code(r'''
    NAMES = ["transition_orbitals", "q_by_pair", "q_history", "hellmann_feynman",
             "fermi_crossing", "q_map"]
    missing = [name for number, name in enumerate(NAMES, start=1)
               if not output_file(f"{FIGURE_FOLDER}/15c_{number}_{name}.png").is_file()]
    check(missing == [], "every figure file of this notebook exists")
    all_checks_passed()
    '''),
    md(r"""
    ## 14. What this notebook showed

    - The adiabaticity measure $Q_{nm} = AH|\langle n|\partial_a h|m\rangle|/
      (\varepsilon_n - \varepsilon_m)^2$ is the first-order amplitude of a jump between
      instantaneous levels of one sector; its derivation needs only the product rule and
      the integral of a rotating phase. In the corrected metric $\partial_a h$ has a
      momentum part and one third of the kinetic term, from the shrinking hidden
      direction.
    - Recomputed in plain Python, every level, the largest $Q$, its pair, its energy
      difference and its matrix element of the free states agree with the Rust
      solver's record (COMPUTED).
    - $Q_{max} \le 0.1982205$ over the whole canonical matrix (transition probability
      below $0.04$), the largest for $N = 2352$ at the start of the history, and it
      decreases along the history; even the zero modes of $N = 8$ have $Q_{max}$ up to
      $0.07$. The instantaneous states are followed adiabatically only in the weak
      sense $Q_{max} < 1$.
    - The Hellmann-Feynman theorem holds: the fold band falls like $-\kappa k$, the
      bulk levels at small $k$ rise, and the energy falls along the history at the rate
      $\sum g f\langle n|\partial_a h|n\rangle = -E_{KS}$.
    - When a level crosses the Fermi level (the demonstration $N = 2360$), the
      instantaneous ground state is not the state that the evolution reaches: there the
      instantaneous picture fails, by $4.68$ to $12.48\,m$ in energy. The full
      time-dependent problem is OPEN.
    """),
]

if __name__ == "__main__":
    raise SystemExit(run_builder(__file__))
