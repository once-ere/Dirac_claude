#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
"""Builder of Notebook 14c, "The brane band: free levels at nonzero 3-momentum along
the deflating history" (textbook "Universes in Pairs", chapter 14).

The notebook Revision/textbook/notebooks/14c_brane_band.ipynb is BUILT from this file
by Revision/textbook/tools/nbkit.py (never edit the .ipynb by hand):

    python Revision/textbook/tools/nbkit.py build \
        Revision/textbook/notebooks/src/14c_brane_band.py --date YYYY-MM-DD
    python Revision/textbook/tools/nbkit.py check \
        Revision/textbook/notebooks/src/14c_brane_band.py

The shooting method is that of the Revision Rust solver (solver/src/shoot.rs), written
with numpy; the notebook reproduces the solver's records spectrum/brane-band.csv,
brane-band-slope.csv, tip-angle.csv and closed-shells.csv (slices 0 and 0.5) and the
particle numbers and bulk edge of results/parameters.json.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools"))
from nbkit import code, md, run_builder  # noqa: E402

FACTS = {
    "id": "14c",
    "name": "14c_brane_band",
    "title": "The brane band: free Kohn-Sham levels at nonzero 3-momentum along the "
             "deflating history",
    "purpose": (
        "With the fourth-order Runge-Kutta shooting method of the Revision Rust "
        "solver it computes the free Kohn-Sham levels of dirac16complex at nonzero "
        "3-momentum k: the brane band that grows out of the zero modes, its slope c "
        "at k = 0 from the Hellmann-Feynman rule and its exact formula, the redshift "
        "of the band along the prescribed deflating history and the exact rescaling "
        "identity eps(k, a4) = eps(k e^(-a4), 0), the mirror symmetries of the two "
        "block types, the insensitivity of the band to the tip condition, the "
        "particle branch, the lattice degeneracies 4 r3(n2) and the closed shells of "
        "the free aufbau with the particle numbers 8, 136 and 688; it reproduces the "
        "Revision Rust solver's records of all of these and draws six teaching "
        "figures."
    ),
    "records": [
        ["Revision/kohn_sham/ks-theory.json",
         "the brane-band slope formula and its value checksNumeric "
         "braneBandSlope_M1_H1_L3_a0 (reproduced)"],
        ["Revision/kohn_sham/reports/ks-theory-python.json",
         "the sympy check brane_band_slope (reproduced)"],
        ["Revision/kohn_sham/reports/ks-rust-solver.json",
         "the Rust solver's free-field checks of the band, the symmetries, the tip "
         "and the particle branch (reproduced)"],
        ["Revision/kohn_sham/results/spectrum/brane-band.csv",
         "the band and three other levels for k from 0 to 4 (reproduced)"],
        ["Revision/kohn_sham/results/spectrum/brane-band-slope.csv",
         "the slope c at the five slices (reproduced)"],
        ["Revision/kohn_sham/results/spectrum/tip-angle.csv",
         "the band level for three tip angles (reproduced)"],
        ["Revision/kohn_sham/results/spectrum/closed-shells.csv",
         "the closed shells of the free aufbau (slices 0 and 0.5 reproduced)"],
        ["Revision/kohn_sham/results/parameters.json",
         "the bulk edge and the particle numbers 8, 136, 688 (reproduced)"],
    ],
    "packages": ["numpy", "sympy", "matplotlib"],
    "needs_rust": [],
    "expected_seconds": 90,
    "timeout_seconds": 600,
    "files_written": [
        "Revision/textbook/figures/14c.captions.json",
        "Revision/textbook/figures/14c_1_band_structure.png",
        "Revision/textbook/figures/14c_2_band_slope.png",
        "Revision/textbook/figures/14c_3_band_redshift.png",
        "Revision/textbook/figures/14c_4_block_type_mirror.png",
        "Revision/textbook/figures/14c_5_tip_insensitivity.png",
        "Revision/textbook/figures/14c_6_closed_shells.png",
    ],
    "final_lines": [
        "PASS all six figure files of this notebook exist",
        "ALL 15 CHECKS PASSED (notebook 14c)",
    ],
    "troubleshooting": [
        ["the cells of sections 8 and 11 run for 10 to 20 seconds each",
         "they integrate the equation for hundreds of energies at once, 72 times "
         "over; wait until the PASS lines appear."],
    ],
}

CELLS = [
    md(r"""
    ## 1. What this notebook computes

    At zero 3-momentum the free Kohn-Sham spectrum of dirac16complex contains eight
    zero modes ($\varepsilon = 0$) sitting at the brane. This notebook follows what
    happens when the 3-momentum $k$ is switched on, at the five slices
    $a_{4,0} = 0, 0.5, 1, 1.5, 2$ of the PRESCRIBED deflating history. It

    - computes the BRANE BAND (the level that grows out of the zero modes) and three
      other low levels for $k$ from 0 to 4 and reproduces the Rust solver's record
      (figure 1);
    - derives the slope $c = d\varepsilon/dk$ at $k = 0$ with the Hellmann-Feynman
      rule, $c = e^{-a_{4,0}}\,\frac{2M}{2M - H}\,\frac{1 - e^{-(2M-H)L}}
      {1 - e^{-2ML}}$, and checks it numerically at every slice (figure 2);
    - checks the exact rescaling identity $\varepsilon(k, a_{4,0}) =
      \varepsilon(k\,e^{-a_{4,0}}, 0)$: along the history the band is redshifted
      (figure 3);
    - checks the mirror symmetries of the two block types $j = \pm1$ (figure 4);
    - shows that the band does not feel the tip condition (figure 5);
    - finds the particle branch, the degeneracies $4r_3(n^2)$ of the torus lattice
      and the closed shells of the free aufbau, with the particle numbers
      $N = 8, 136, 688$ of the Revision runs (figure 6).

    It prints a PASS line for every check (15 in all) and saves six figures.
    """),
    md(r"""
    ## 3. The words used in this notebook

    - **Level, orbital, label**: an energy $\varepsilon$ of the block equation
      $h_j\chi = \varepsilon\chi$, its solution, and the integer that counts its
      Pruefer half-turns (even parity: $\Phi = l\pi$, odd: $\Phi = \pi/2 + l\pi$).
    - **3-momentum $k$**: the momentum along ordinary 3-space; on the coordinate
      torus of size $\ell$ the allowed vectors are $\Delta k\,(n_1, n_2, n_3)$ with
      integers $n_i$ and $\Delta k = 2\pi/\ell = 0.25$ (in units of $H$).
    - **Shell**: all lattice vectors with the same $n^2 = n_1^2 + n_2^2 + n_3^2$;
      $r_3(n^2)$ is their number (for example $r_3(1) = 6$).
    - **Brane band**: the even-parity level of label 0 in the blocks $j = +1$, which
      is the zero mode at $k = 0$ and rises with $k$.
    - **Slope $c$**: $d\varepsilon/dk$ of the brane band at $k = 0$.
    - **Hellmann-Feynman rule**: for a normalised eigenvector, the derivative of
      the level is the expectation value of the derivative of the Hamiltonian:
      $d\varepsilon/dk = \langle\chi|\,\partial h/\partial k\,|\chi\rangle$.
    - **Slice, history**: the slice $a_{4,0}$ is the value of $a_4$ at one instant;
      the history $a_4 = AHx_4$ is a PRESCRIBED BACKGROUND (given, not solved for).
    - **Redshift**: a 3-momentum $k$ acts like $k\,e^{-a_{4,0}}$ at the slice
      $a_{4,0}$: momenta shrink as 3-space inflates.
    - **Tip condition**: the condition $(1 - Q(\theta))\chi(-L) = 0$ at the cutoff
      $y = -L$; $\theta = 0$ ($b(-L) = 0$) is the canonical choice.
    - **Particle branch, sea**: by a CONVENTION of the Revision theory, the levels
      that are positive in the free problem (and the $k = 0$ zero modes) are
      particle levels; the negative branch is the filled, normal-ordered sea.
    - **Aufbau, closed shell**: fill the $N$ lowest particle states; $N$ is a closed
      shell when the filling ends exactly at the end of a degenerate group of levels.
    - **Bulk edge**: the lowest level that is not on the brane band (here a $k = 0$
      level of the odd parity).
    - **Richardson extrapolation**: combining two finite-difference estimates so that
      their leading errors cancel.
    """),
    md(r"""
    ## 4. The physical and mathematical situation

    In each $2\times2$ block of type $j$ the free Kohn-Sham equation is
    $h_j\chi = \varepsilon\chi$ with $h_j = j[-i\sigma_1\,d/dy + M\sigma_2 +
    \kappa(y)k\,\sigma_3]$, the momentum weight $\kappa(y) = e^{-Hy - a_{4,0}}$, the
    ASSUMED Z2 mirror brane at $y = 0$ (even: $b(0) = 0$, odd: $a(0) = 0$) and the
    regular tip $b(-L) = 0$ at the cutoff $y = -L$; in real form $\chi = (a, ib)$:
    $a' = Ma - (\kappa k + j\varepsilon)b$, $b' = (j\varepsilon - \kappa k)a - Mb$.

    The momentum term $\kappa k\sigma_3$ pushes the orbitals toward the brane
    ($\kappa$ grows toward the tip) and lifts the zero modes into a band. Every level
    holds $4r_3(n^2)$ states for each block type (four blocks times the number of
    lattice directions of the shell). The canonical parameters of the Revision
    solver are $H = m = 1$, $L = 3$, $\Delta k = 0.25$, the slices $a_{4,0} = 0,
    0.5, 1, 1.5, 2$, and RK4 with $G = 900$ steps.

    Status: the slope formula and the rescaling identity are PROVED (exact); the
    numerical levels are COMPUTED (they reproduce the Rust solver's records); the
    brane condition is ASSUMED; the tip condition is a chosen cutoff condition; the
    history is a PRESCRIBED BACKGROUND; the counting of the zero modes as particles
    is a CONVENTION whose justification is OPEN.
    """),
    md(r"""
    ## 5. The shooting tools

    The next cell defines the numerical tools, exactly the method of the Revision
    Rust solver: `shoot` integrates the real form from the tip ($(a, b) =
    (\cos\frac\theta2, \sin\frac\theta2)$, canonical $\theta = 0$) to the brane with
    classical RK4 ($G$ steps; the coefficients at the nodes and step midpoints of a
    fine grid of $2G + 1$ points) and follows the Pruefer angle $\mathrm{atan2}(b, a)$
    step by step; it returns $\Phi = j\,\theta(0)$, which grows strictly with
    $\varepsilon$. `levels` finds the energy with $\Phi = $ target (even $l\pi$, odd
    $\pi/2 + l\pi$) by 72 bisections of $[-20, 20]$. `orbital` returns a normalised
    orbital on the fine grid (cubic Hermite values at the midpoints, Simpson's rule
    for the norm). All three accept arrays (numpy), so that hundreds of levels are
    found at once. It also reads the Rust solver's records with a small CSV reader
    and defines `record_check`, which reads the verdict of a named check.
    """),
    code(r'''
    import math  # exp, cos, sin of single numbers

    import numpy as np  # floating-point arrays
    import sympy as sp  # exact algebra with symbols

    RUST_REPORT = "Revision/kohn_sham/reports/ks-rust-solver.json"
    SPECTRUM = "Revision/kohn_sham/results/spectrum"  # the folder of the records


    def record_check(name, report=RUST_REPORT):
        """The check called name is PASS in the Revision report."""
        data = json.loads(repository_file(report).read_text(encoding="utf-8"))
        return [c["verdict"] for c in data["checks"] if c["name"] == name] == ["PASS"]


    def read_csv(relative):
        """The rows of a CSV record as a list of dictionaries (column -> text)."""
        lines = repository_file(relative).read_text(encoding="utf-8").splitlines()
        header = lines[0].split(",")
        return [dict(zip(header, line.split(","))) for line in lines[1:]]


    def shoot(eps, k=0.0, j=1.0, a4=0.0, M=1.0, L=3.0, G=900, H=1.0, tip=0.0,
              keep=False):
        """Phi = j theta(0) for the energies eps (arrays allowed for eps, k, j, a4);
        with keep=True also theta, a, b at the G + 1 nodes."""
        eps, k, j, a4 = np.broadcast_arrays(*(np.asarray(x, dtype=float)
                                              for x in (eps, k, j, a4)))
        nf = 2 * G + 1  # nodes and step midpoints
        y_fine = -L * ((nf - 1 - np.arange(nf)) / (nf - 1))
        e_minus_Hy = np.exp(-H * y_fine)
        kk = k * np.exp(-a4)  # kappa k = kk e^(-Hy)
        h = L / G
        a_ = np.full(eps.shape, math.cos(0.5 * tip))
        b_ = np.full(eps.shape, math.sin(0.5 * tip))
        theta = np.full(eps.shape, 0.5 * tip)
        raw = np.arctan2(b_, a_)
        je = j * eps
        path = [(theta, a_, b_)]
        for i in range(G):
            K0, K1, K2 = (kk * e_minus_Hy[2 * i], kk * e_minus_Hy[2 * i + 1],
                          kk * e_minus_Hy[2 * i + 2])
            p1a, p1b = M * a_ - (K0 + je) * b_, (je - K0) * a_ - M * b_
            a2, b2 = a_ + 0.5 * h * p1a, b_ + 0.5 * h * p1b
            p2a, p2b = M * a2 - (K1 + je) * b2, (je - K1) * a2 - M * b2
            a3, b3 = a_ + 0.5 * h * p2a, b_ + 0.5 * h * p2b
            p3a, p3b = M * a3 - (K1 + je) * b3, (je - K1) * a3 - M * b3
            a4_, b4_ = a_ + h * p3a, b_ + h * p3b
            p4a, p4b = M * a4_ - (K2 + je) * b4_, (je - K2) * a4_ - M * b4_
            a_ = a_ + h / 6.0 * (p1a + 2.0 * p2a + 2.0 * p3a + p4a)
            b_ = b_ + h / 6.0 * (p1b + 2.0 * p2b + 2.0 * p3b + p4b)
            new = np.arctan2(b_, a_)
            step = new - raw  # brought into (-pi, pi]
            step = np.where(step > np.pi, step - 2 * np.pi,
                            np.where(step <= -np.pi, step + 2 * np.pi, step))
            theta = theta + step
            raw = new
            if keep:
                path.append((theta, a_, b_))
        if keep:
            return j * theta, [np.array(q) for q in zip(*path)]
        return j * theta


    def target(parity, label):
        offset = np.where(np.asarray(parity) == "even", 0.0, 0.5 * np.pi)
        return offset + np.asarray(label, dtype=float) * np.pi


    def levels(k, j, parity, label, a4=0.0, iterations=72, **options):
        """The levels with these labels (arrays allowed), by bisection."""
        k, j, parity, label, a4 = np.broadcast_arrays(
            np.asarray(k, dtype=float), np.asarray(j, dtype=float), np.asarray(parity),
            np.asarray(label), np.asarray(a4, dtype=float))
        goal = target(parity, label)
        lo, hi = np.full(k.shape, -20.0), np.full(k.shape, 20.0)
        for _ in range(iterations):
            mid = 0.5 * (lo + hi)
            g = shoot(mid, k, j, a4, **options) - goal
            lo = np.where(g <= 0.0, mid, lo)
            hi = np.where(g >= 0.0, mid, hi)
        return 0.5 * (lo + hi)


    def orbital(eps, k=0.0, j=1.0, a4=0.0, M=1.0, L=3.0, G=900, H=1.0):
        """The normalised orbital (y, a, b) and the Simpson weights on the fine grid."""
        _, (_, a_n, b_n) = shoot(eps, k, j, a4, M=M, L=L, G=G, H=H, keep=True)
        nf, h = 2 * G + 1, L / G
        y_fine = -L * ((nf - 1 - np.arange(nf)) / (nf - 1))
        K_fine = k * math.exp(-a4) * np.exp(-H * y_fine)
        a_f, b_f = np.zeros(nf), np.zeros(nf)
        a_f[0::2], b_f[0::2] = a_n, b_n
        da = M * a_f - (K_fine + j * eps) * b_f
        db = (j * eps - K_fine) * a_f - M * b_f
        for f in range(1, nf, 2):  # cubic Hermite values at the midpoints
            a_f[f] = 0.5 * (a_f[f - 1] + a_f[f + 1]) + h / 8.0 * (da[f - 1] - da[f + 1])
            b_f[f] = 0.5 * (b_f[f - 1] + b_f[f + 1]) + h / 8.0 * (db[f - 1] - db[f + 1])
        weights = np.full(nf, 2.0)  # Simpson weights 1, 4, 2, ..., 4, 1 times (h/2)/3
        weights[1::2] = 4.0
        weights[0] = weights[-1] = 1.0
        weights *= 0.5 * h / 3.0
        norm = math.sqrt(float(np.sum(weights * (a_f ** 2 + b_f ** 2))))
        return y_fine, a_f / norm, b_f / norm, weights


    SLICES = [0.0, 0.5, 1.0, 1.5, 2.0]  # the slices of the Revision solver
    say("defined: shoot, levels, orbital, read_csv, record_check")
    '''),
    md(r"""
    ## 6. The brane band and three other levels for k from 0 to 4

    The Rust solver's record `brane-band.csv` lists, for $k = 0, 0.05, 0.10, \dots,
    4$ at the slice $a_{4,0} = 0$, the brane band (block type $j = +1$, even, label
    0), the next even level of $j = +1$ (label 1), the lowest odd level of $j = +1$
    (label 0), and the even level of label 1 in the blocks $j = -1$. The next cell
    computes these $4\times81$ levels in one call (and, for the figure, the brane
    band of the blocks $j = -1$, label 0), and checks that they equal the record to
    $10^{-11}$. The $k$ values are made exactly as in the Rust program, by adding
    0.05 again and again (so that the last digits agree). It also checks that the
    band rises strictly with $k$.
    """),
    code(r'''
    k_list, kk = [], 0.0
    while kk <= 4.0 + 1e-12:  # 0, 0.05, 0.10, ... as the Rust program makes them
        k_list.append(kk)
        kk += 0.05
    k_band = np.array(k_list)
    sectors = [(1.0, "even", 0), (1.0, "even", 1), (1.0, "odd", 0), (-1.0, "even", 1),
               (-1.0, "even", 0)]  # (j, parity, label); the last one for the figure
    K_all = np.concatenate([k_band] * len(sectors))
    J_all = np.concatenate([[j_] * len(k_band) for j_, _, _ in sectors])
    P_all = np.concatenate([[p_] * len(k_band) for _, p_, _ in sectors])
    L_all = np.concatenate([[l_] * len(k_band) for _, _, l_ in sectors])
    found = levels(K_all, J_all, P_all, L_all).reshape(len(sectors), len(k_band))
    band, bulk_even, odd0, minus_even1, minus_band = found
    rows = read_csv(f"{SPECTRUM}/brane-band.csv")
    record = np.array([[float(r[c]) for r in rows] for c in
                       ("eps_band_a0", "eps_band_bulk_even_l1", "eps_odd_l0",
                        "eps_jm1_even_l1")])
    k_record = np.array([float(r["k"]) for r in rows])
    say(f"k = 0.25: brane band {band[5]:.10f}, odd level {odd0[5]:.10f} (units of m)")
    check(len(rows) == 81 and np.max(np.abs(k_record - k_band)) < 1e-15
          and np.max(np.abs(found[:4] - record)) < 1e-11,
          "the 324 levels equal the record brane-band.csv",
          record=f"{SPECTRUM}/brane-band.csv")
    check(bool(np.all(np.diff(band) > 0.0)) and np.max(np.abs(minus_band + band)) < 1e-12,
          "the band rises strictly with k; the j = -1 band is its mirror image -eps")
    '''),
    md(r"""
    The next cell draws the band structure: the five levels against $k$, with the
    straight line $c\,k$ of the first-order slope (section 7) and the bulk edge
    $1.2923\,m$ (the lowest odd level at $k = 0$, the lowest level not on the band).
    """),
    code(r'''
    c_theory = 2.0 / (1.0 + math.exp(-3.0))  # the slope for M = H = 1, L = 3, a4,0 = 0
    fig, ax = plt.subplots(figsize=(9.5, 4.8))
    ax.plot(k_band, band, color="C0", linewidth=2, label="brane band ($j = +1$, even, 0)")
    ax.plot(k_band, bulk_even, color="C1", label="$j = +1$, even, label 1")
    ax.plot(k_band, odd0, color="C2", label="$j = +1$, odd, label 0")
    ax.plot(k_band, minus_even1, color="C4", label="$j = -1$, even, label 1")
    ax.plot(k_band, minus_band, "--", color="C0",
            label="$j = -1$, even, label 0 (sea)")
    ax.plot(k_band[:13], c_theory * k_band[:13], ":", color="black",
            label="first order: $c\\,k$, $c = 1.9051$")
    ax.axhline(odd0[0], color="gray", linewidth=0.8, linestyle="-.")
    ax.annotate("bulk edge 1.2923", (2.6, odd0[0] - 0.55), fontsize=8,
                color="gray")  # just below the dash-dotted line
    ax.set_xlabel("3-momentum $k$ (units of $H$), slice $a_{4,0} = 0$")
    ax.set_ylabel("level $\\varepsilon$ (units of $m$)")
    ax.set_title("the free levels at nonzero 3-momentum ($m = 1$, $L = 3$)")
    ax.legend(fontsize=7, loc="center left", bbox_to_anchor=(1.01, 0.5))
    save_figure(fig, "band_structure",
                "The free Kohn-Sham levels against the 3-momentum $k$ (units of "
                "$H$) at the slice $a_{4,0} = 0$ for $m = 1$, $L = 3$; vertical axis "
                "the level in units of $m$. The brane band (thick) starts at the zero "
                "mode and rises with the slope $c = 1.9051$ (dotted line) and then "
                "more slowly; the other levels start at or above the bulk edge "
                "$1.2923\\,m$ (dash-dotted); the dashed curve is the brane band of "
                "the blocks $j = -1$, the mirror image $-\\varepsilon$, which belongs "
                "to the sea.")
    '''),
    md(r"""
    ## 7. The slope of the band at k = 0: the Hellmann-Feynman rule

    Line by line:

    1. If $h(k)\chi = \varepsilon(k)\chi$ with $\int\chi^\dagger\chi\,dy = 1$ and
       boundary conditions that do not depend on $k$, then $\varepsilon =
       \int\chi^\dagger h\chi\,dy$, and differentiating, the terms with
       $d\chi/dk$ add up to $\varepsilon\,\frac{d}{dk}\int\chi^\dagger\chi\,dy = 0$
       ($h$ is self-adjoint): $d\varepsilon/dk = \int\chi^\dagger(\partial_k h)\chi
       \,dy$.
    2. Here $\partial_k h_j = j\kappa(y)\sigma_3$ and, at $k = 0$, $\chi$ is the zero
       mode $(a, 0)$ with $a^2 \propto e^{2My}$, so $\chi^\dagger\sigma_3\chi = a^2$.
    3. Hence $d\varepsilon/dk = jc$ with
       $c = \int_{-L}^0 e^{-Hy - a_{4,0}}e^{2My}\,dy\,/\int_{-L}^0 e^{2My}\,dy$.
    4. Doing the two integrals: $c = e^{-a_{4,0}}\,\frac{2M}{2M - H}\,
       \frac{1 - e^{-(2M - H)L}}{1 - e^{-2ML}}$; for $M = H = 1$:
       $c = e^{-a_{4,0}}\,\frac{2(1 - e^{-L})}{1 - e^{-2L}} = \frac{2e^{-a_{4,0}}}
       {1 + e^{-L}}$, which is $1.9051482536$ for $L = 3$, $a_{4,0} = 0$.

    The next cell does step 4 with sympy, compares the value with the Revision
    record (`checksNumeric.braneBandSlope_M1_H1_L3_a0` of ks-theory.json), computes
    the integral of step 3 numerically from the zero-mode orbital (Simpson), and
    measures the slope numerically at the five slices as the Rust solver did:
    levels at $k = 10^{-4}$ and $2\times10^{-4}$, and the Richardson combination
    $c = (4\varepsilon_1/10^{-4} - \varepsilon_2/(2\times10^{-4}))/3$, which removes
    the $k^2$ error of $\varepsilon/k$. These must equal the record
    `brane-band-slope.csv`. Finally it measures the slope for $L = 2$ and $L = 4$.
    """),
    code(r'''
    Ms, Hs, Ls = sp.symbols("M H L", positive=True)
    ys, a4s = sp.symbols("y a", real=True)
    ratio = (sp.integrate(sp.exp(-Hs * ys - a4s) * sp.exp(2 * Ms * ys), (ys, -Ls, 0))
             / sp.integrate(sp.exp(2 * Ms * ys), (ys, -Ls, 0)))  # step 3
    formula = (sp.exp(-a4s) * 2 * Ms / (2 * Ms - Hs) * (1 - sp.exp(-(2 * Ms - Hs) * Ls))
               / (1 - sp.exp(-2 * Ms * Ls)))  # step 4
    same = sp.simplify((ratio - formula).subs({Ms: 1, Hs: 1, Ls: 3})) == 0 and \
        sp.simplify((ratio - formula).subs({Ms: 2, Hs: 1, Ls: 3})) == 0
    c_exact = float(formula.subs({Ms: 1, Hs: 1, Ls: 3, a4s: 0}))
    theory = json.loads(repository_file("Revision/kohn_sham/ks-theory.json")
                        .read_text(encoding="utf-8"))
    c_record = float(theory["checksNumeric"]["braneBandSlope_M1_H1_L3_a0"])
    report("slope c for M = H = 1, L = 3, a4,0 = 0", f"{c_exact:.13f}", "m/H")
    check(same and abs(c_exact - c_record) < 1e-15 and abs(c_exact - c_theory) < 1e-15
          and record_check("brane_band_slope",
                           "Revision/kohn_sham/reports/ks-theory-python.json"),
          "c = e^(-a4,0) (2M/(2M - H)) (1 - e^(-(2M-H)L))/(1 - e^(-2ML)) = 1.9051482536",
          record="Revision/kohn_sham/ks-theory.json, checksNumeric "
                 "braneBandSlope_M1_H1_L3_a0")
    y_f, a_zero, b_zero, simpson = orbital(0.0)  # the zero mode at k = 0
    c_integral = float(np.sum(simpson * np.exp(-y_f) * a_zero ** 2))  # step 3
    check(abs(c_integral - c_exact) < 1e-9,
          "the integral of kappa a^2 over the numerical zero mode gives c")
    tiny = np.array([1e-4, 2e-4] * 5)  # two small momenta at each slice
    slice_of = np.repeat(SLICES, 2)
    small = levels(tiny, 1.0, "even", 0, a4=slice_of).reshape(5, 2)
    c_numeric = (4.0 * small[:, 0] / 1e-4 - small[:, 1] / 2e-4) / 3.0
    rows = read_csv(f"{SPECTRUM}/brane-band-slope.csv")
    c_rows = np.array([float(r["c_numeric"]) for r in rows])
    for a_, c_ in zip(SLICES, c_numeric):
        say(f"slice a4,0 = {a_}: c numerical {c_:.12f}, "
            f"c e^(-a4,0) exact {c_exact * math.exp(-a_):.12f}")
    check(np.max(np.abs(c_numeric / c_rows - 1.0)) < 1e-11
          and np.max(np.abs(c_numeric / (c_exact * np.exp(-np.array(SLICES))) - 1.0))
          < 1e-9 and record_check("free_brane_band_slope"),
          "the numerical slope equals c e^(-a4,0) at all five slices",
          record=f"{SPECTRUM}/brane-band-slope.csv and {RUST_REPORT}, check "
                 "free_brane_band_slope")
    c_by_L = {}
    for L_ in (2.0, 4.0):  # the slope for two other cutoffs
        pair = levels(np.array([1e-4, 2e-4]), 1.0, "even", 0, L=L_, G=round(300 * L_))
        c_by_L[L_] = (4.0 * pair[0] / 1e-4 - pair[1] / 2e-4) / 3.0
    c_by_L[3.0] = float(c_numeric[0])
    exact_by_L = {L_: 2.0 / (1.0 + math.exp(-L_)) for L_ in (2.0, 3.0, 4.0)}
    say("c for L = 2, 3, 4: " + ", ".join(f"{c_by_L[L_]:.6f}" for L_ in (2.0, 3.0, 4.0))
        + " (exact " + ", ".join(f"{exact_by_L[L_]:.6f}" for L_ in (2.0, 3.0, 4.0)) + ")")
    check(all(abs(c_by_L[L_] - exact_by_L[L_]) < 1e-9 for L_ in (2.0, 4.0)),
          "the slope formula holds for L = 2 and L = 4 too")
    '''),
    md(r"""
    The next cell draws the slope. Left: $c$ at the five slices (numerical points)
    on the exact curve $c\,e^{-a_{4,0}}$, logarithmic vertical axis. Right: $c$ as a
    function of the cutoff $L$ for $a_{4,0} = 0$, with the numerical values for
    $L = 2, 3, 4$; for a long hidden interval it approaches $2M/(2M - H) = 2$.
    """),
    code(r'''
    fig, (left, right) = plt.subplots(1, 2, figsize=(10.0, 4.0))
    a_grid = np.linspace(0.0, 2.0, 201)
    left.semilogy(a_grid, c_exact * np.exp(-a_grid), color="C0",
                  label="exact $c\\,e^{-a_{4,0}}$")
    left.semilogy(SLICES, c_numeric, "o", color="C3", label="numerical (Richardson)")
    left.set_xlabel("slice $a_{4,0}$")
    left.set_ylabel("slope $c$ (units of $m/H$, logarithmic)")
    left.set_title("the slope along the history")
    left.legend(fontsize=8)
    L_grid = np.linspace(0.5, 6.0, 221)
    right.plot(L_grid, 2.0 / (1.0 + np.exp(-L_grid)), color="C0",
               label="exact $2/(1 + e^{-L})$")
    right.plot(list(c_by_L), list(c_by_L.values()), "o", color="C3", label="numerical")
    right.axhline(2.0, color="gray", linestyle=":", label="limit $2M/(2M - H) = 2$")
    right.set_xlabel("cutoff $L$ (units of $1/H$)")
    right.set_ylabel("slope $c$ at $a_{4,0} = 0$")
    right.set_title("the slope against the cutoff ($M = H = 1$)")
    right.legend(fontsize=8)
    save_figure(fig, "band_slope",
                "The slope $c = d\\varepsilon/dk$ of the brane band at $k = 0$ "
                "($M = H = 1$). Left: against the slice $a_{4,0}$ from 0 to 2, "
                "logarithmic vertical axis; the numerical Richardson values (dots) lie "
                "on the exact line $c\\,e^{-a_{4,0}}$ with $c = 1.9051$ for $L = 3$: "
                "the band is redshifted along the history. Right: against the "
                "cutoff $L$ (units of $1/H$) at $a_{4,0} = 0$; exact curve "
                "$2/(1 + e^{-L})$ and numerical values for $L = 2, 3, 4$; for a long "
                "hidden interval the slope tends to $2M/(2M - H) = 2$.")
    '''),
    md(r"""
    ## 8. The deflating history: redshift and the exact rescaling identity

    The slice enters the block equation only through $\kappa k = e^{-Hy}(k\,
    e^{-a_{4,0}})$, so EXACTLY $\varepsilon(k, a_{4,0}) = \varepsilon(k\,e^{-a_{4,0}},
    0)$ for every level. The next cell checks this as the Rust solver did (check
    `free_rescaling_relation_and_band_monotone`): for $k = 0.25, 1, 2.5$, the five
    slices and three sectors, the level at the slice and the level at slice 0 with
    the rescaled momentum agree to $10^{-12}$. It then computes the brane band at
    the five slices for the figure, and the gap of the free $N = 8$ state at every
    slice: the eight zero modes are filled and the next level is the band at the
    first lattice shell $k = \Delta k = 0.25$; this gap must equal the record
    `closed-shells.csv` (rows $N = 8$). Along the history the gap shrinks like
    $e^{-a_{4,0}}$ for small momenta: $0.4307$, ..., $0.0642\,m$.
    """),
    code(r'''
    test_k = [0.25, 1.0, 2.5]
    test_sectors = [(1.0, "even", 0), (1.0, "odd", 0), (-1.0, "even", 1)]
    combos = [(a_, k_, s_) for a_ in SLICES for k_ in test_k for s_ in test_sectors]
    at_slice = levels(np.array([k_ for a_, k_, s_ in combos]),
                      np.array([s_[0] for a_, k_, s_ in combos]),
                      np.array([s_[1] for a_, k_, s_ in combos]),
                      np.array([s_[2] for a_, k_, s_ in combos]),
                      a4=np.array([a_ for a_, k_, s_ in combos]))
    at_zero = levels(np.array([k_ * math.exp(-a_) for a_, k_, s_ in combos]),
                     np.array([s_[0] for a_, k_, s_ in combos]),
                     np.array([s_[1] for a_, k_, s_ in combos]),
                     np.array([s_[2] for a_, k_, s_ in combos]))
    check(np.max(np.abs(at_slice - at_zero)) < 1e-12
          and record_check("free_rescaling_relation_and_band_monotone"),
          "eps(k, a4,0) = eps(k e^(-a4,0), 0) for 45 levels at the five slices",
          record=f"{RUST_REPORT}, check free_rescaling_relation_and_band_monotone")
    k_fig = np.linspace(0.0, 4.0, 41)
    band_slices = levels(np.tile(k_fig, 5), 1.0, "even", 0,
                         a4=np.repeat(SLICES, len(k_fig))).reshape(5, len(k_fig))
    gaps = levels(np.full(5, 0.25), 1.0, "even", 0, a4=np.array(SLICES))
    shells_record = read_csv(f"{SPECTRUM}/closed-shells.csv")
    gap_record = [float(r["gap"]) for r in shells_record if r["N_closed"] == "8"]
    for a_, g_ in zip(SLICES, gaps):
        say(f"slice a4,0 = {a_}: gap of the free N = 8 state {g_:.10f} m")
    check(len(gap_record) == 5 and np.max(np.abs(gaps - np.array(gap_record))) < 1e-11,
          "the N = 8 gaps at the five slices equal the record",
          record=f"{SPECTRUM}/closed-shells.csv, rows N_closed = 8")
    '''),
    md(r"""
    The next cell draws the redshift. Left: the brane band against $k$ at the five
    slices; later slices lie lower. Right: the same curves against the redshifted
    momentum $k\,e^{-a_{4,0}}$: they fall onto one curve, the slice-0 band, which is
    the rescaling identity.
    """),
    code(r'''
    fig, (left, right) = plt.subplots(1, 2, figsize=(10.0, 4.0), sharey=True)
    for index, a_ in enumerate(SLICES):
        left.plot(k_fig, band_slices[index], label=f"$a_{{4,0}} = {a_}$")
        right.plot(k_fig * math.exp(-a_), band_slices[index], "o", markersize=3,
                   label=f"$a_{{4,0}} = {a_}$")
    right.plot(k_fig, band_slices[0], color="black", linewidth=0.8,
               label="slice 0 band")
    left.set_xlabel("3-momentum $k$ (units of $H$)")
    left.set_ylabel("brane band $\\varepsilon$ (units of $m$)")
    left.set_title("the band at five slices")
    left.legend(fontsize=8)
    right.set_xlabel("redshifted momentum $k\\,e^{-a_{4,0}}$ (units of $H$)")
    right.set_title("all slices on one curve")
    right.legend(fontsize=7)
    save_figure(fig, "band_redshift",
                "The brane band along the prescribed deflating history. Left: the "
                "band $\\varepsilon(k)$ (units of $m$) against the 3-momentum $k$ "
                "(units of $H$) at the five slices $a_{4,0} = 0$ to $2$; later slices "
                "lie lower. Right: the same levels against the redshifted momentum "
                "$k\\,e^{-a_{4,0}}$; all points fall on the band of the slice 0 "
                "(black line), the exact rescaling identity "
                "$\\varepsilon(k, a_{4,0}) = \\varepsilon(k e^{-a_{4,0}}, 0)$.")
    '''),
    md(r"""
    ## 9. The mirror symmetries of the two block types

    Two exact relations of the block Hamiltonian (for $v = 0$): $h_{-1} = -h_{+1}$,
    so the levels of $j = -1$ are the negatives of those of $j = +1$, with the
    labels $l \to -l$ (even) and $l \to -l - 1$ (odd); and $\sigma_3h_j(k)\sigma_3 =
    h_{-j}(-k)$, so the level of $(j = -1, -k)$ with label $l$ equals the level of
    $(j = +1, k)$ with the same label. The next cell checks both for the shells
    $n^2 = 0, 1, 2, 5, 9$ ($k = 0.25\sqrt{n^2}$) and the labels $-3$ to $3$ of both
    parities (the Rust check `free_block_type_symmetries`), and computes the even
    levels of both block types for $k$ from 0 to 2 for the figure.
    """),
    code(r'''
    sym_k = [0.25 * math.sqrt(n2) for n2 in (0, 1, 2, 5, 9)]
    sym_l = list(range(-3, 4))
    grid = [(k_, l_) for k_ in sym_k for l_ in sym_l]
    K_s = np.array([k_ for k_, l_ in grid])
    L_s = np.array([l_ for k_, l_ in grid])
    plus_even = levels(K_s, 1.0, "even", L_s)
    minus_even = levels(K_s, -1.0, "even", -L_s)
    plus_odd = levels(K_s, 1.0, "odd", L_s)
    minus_odd = levels(K_s, -1.0, "odd", -L_s - 1)
    flipped_even = levels(-K_s, -1.0, "even", L_s)
    flipped_odd = levels(-K_s, -1.0, "odd", L_s)
    mirror = max(np.max(np.abs(plus_even + minus_even)),
                 np.max(np.abs(plus_odd + minus_odd)))
    flip = max(np.max(np.abs(flipped_even - plus_even)),
               np.max(np.abs(flipped_odd - plus_odd)))
    check(mirror < 1e-12 and flip < 1e-12 and record_check("free_block_type_symmetries"),
          "spec h_(-1) = -spec h_(+1) and eps_(-1)(-k) = eps_(+1)(k), label by label",
          record=f"{RUST_REPORT}, check free_block_type_symmetries")
    k_mirror = np.linspace(0.0, 2.0, 41)
    fig_labels = list(range(-2, 3))
    plus_curves = levels(np.tile(k_mirror, 5), 1.0, "even",
                         np.repeat(fig_labels, len(k_mirror))).reshape(5, -1)
    minus_curves = levels(np.tile(k_mirror, 5), -1.0, "even",
                          np.repeat(fig_labels, len(k_mirror))).reshape(5, -1)
    say("even levels at k = 2, labels -2 ... 2:")
    say("  j = +1: " + ", ".join(f"{x:.4f}" for x in plus_curves[:, -1]))
    say("  j = -1: " + ", ".join(f"{x:.4f}" for x in minus_curves[:, -1]))
    '''),
    md(r"""
    The next cell draws the even levels of the two block types against $k$: the
    picture of $j = -1$ is the picture of $j = +1$ turned upside down.
    """),
    code(r'''
    fig, (left, right) = plt.subplots(1, 2, figsize=(10.0, 4.2), sharey=True)
    for row, label in enumerate(fig_labels):
        left.plot(k_mirror, plus_curves[row], label=f"label {label}")
        right.plot(k_mirror, minus_curves[row], label=f"label {label}")
    for ax, title in ((left, "block type $j = +1$"), (right, "block type $j = -1$")):
        ax.axhline(0.0, color="black", linewidth=0.6)
        ax.set_xlabel("3-momentum $k$ (units of $H$)")
        ax.set_title(title + ", even parity")
        ax.legend(fontsize=7, loc="upper left")
    left.set_ylabel("level $\\varepsilon$ (units of $m$)")
    save_figure(fig, "block_type_mirror",
                "The even-parity levels with labels $-2$ to $2$ against the "
                "3-momentum $k$ (units of $H$), slice 0, $m = 1$, $L = 3$; vertical "
                "axis the level in units of $m$. Left the blocks $j = +1$, right the "
                "blocks $j = -1$: each picture is the other one reflected in the line "
                "$\\varepsilon = 0$ (label $l$ goes to $-l$), the exact relation "
                "$h_{-1} = -h_{+1}$; the rising curve of the label 0 on the left is the "
                "brane band, the falling one on the right its sea partner.")
    '''),
    md(r"""
    ## 10. The tip condition does not matter for the band

    For $k \ne 0$ an orbital is suppressed toward the tip like
    $\exp(-k(\kappa(-L) - \kappa(y))/H)$ (the Revision record,
    `boundaryConditions.tip`): the term $\kappa k\sigma_3$ grows toward the tip and
    pushes the orbital away. So the level cannot depend much on the condition
    imposed there. The next cell computes the brane band with the tip angles
    $\theta = 0, 0.5, 1$ for $k = 0.25, 0.5, 1$ (the record `tip-angle.csv`) and
    checks that the shift from $\theta = 0$ is below the suppression factor
    $\exp(-k(e^{HL} - 1)/H)$ (the Rust check `free_tip_angle_insensitivity`); then
    it computes the shifts for ten momenta from 0.1 to 1 for the figure.
    """),
    code(r'''
    tip_rows = read_csv(f"{SPECTRUM}/tip-angle.csv")
    tip_k = np.array([0.25, 0.5, 1.0])
    tip_levels = {th: levels(tip_k, 1.0, "even", 0, tip=th) for th in (0.0, 0.5, 1.0)}
    suppression = np.exp(-tip_k * (math.exp(3.0) - 1.0))  # H = 1, L = 3
    worst_tip, below = 0.0, True
    for r in tip_rows:
        i_k = list(tip_k).index(float(r["k"]))
        mine = tip_levels[float(r["theta_tip"])][i_k]
        worst_tip = max(worst_tip, abs(mine - float(r["eps"])))
        shift = mine - tip_levels[0.0][i_k]
        below &= abs(shift) <= max(suppression[i_k], 1e-12)
    check(len(tip_rows) == 9 and worst_tip < 1e-11 and below
          and record_check("free_tip_angle_insensitivity"),
          "the band levels equal tip-angle.csv; the shifts are below the suppression",
          record=f"{SPECTRUM}/tip-angle.csv and {RUST_REPORT}, check "
                 "free_tip_angle_insensitivity")
    k_tip = np.linspace(0.1, 1.0, 10)
    shifts = {th: np.abs(levels(k_tip, 1.0, "even", 0, tip=th)
                         - levels(k_tip, 1.0, "even", 0, tip=0.0)) for th in (0.5, 1.0)}
    def shown(x):
        """A shift as text; below 1e-14 it is rounding noise and differs between
        computers."""
        return f"{x:.1e}" if x >= 1e-14 else "below 1e-14 (rounding)"


    for k_, s5, s10 in zip(k_tip, shifts[0.5], shifts[1.0]):
        say(f"k = {k_:.1f}: shift for theta = 0.5: {shown(s5)}, for theta = 1: "
            f"{shown(s10)}")
    '''),
    md(r"""
    The next cell draws the shifts against $k$ on a logarithmic axis, together with
    the suppression factor. Shifts below about $10^{-15}$ are rounding noise of the
    floating-point numbers (their exact values differ from computer to computer); a
    shift below $10^{-16}$ (or exactly 0) is drawn at $10^{-16}$, so that it fits on
    the logarithmic axis. The printed list above shows the size of the drop: each
    step of $0.1$ in $k$ makes the shift 12 to 34 times smaller (the suppression
    factor itself only about $e^{0.1(e^3 - 1)} = 6.7$ times), until it reaches the
    rounding level at $k = 0.9$.
    """),
    code(r'''
    fig, ax = plt.subplots(figsize=(7.5, 4.4))
    k_line = np.linspace(0.1, 1.0, 91)
    ax.semilogy(k_line, np.exp(-k_line * (math.exp(3.0) - 1.0)), color="black",
                label="suppression $\\exp(-k(e^{HL} - 1)/H)$")
    for th, marker in ((0.5, "o"), (1.0, "s")):
        ax.semilogy(k_tip, np.maximum(shifts[th], 1e-16), marker, markersize=5,
                    label=f"$|\\varepsilon(\\theta = {th}) - \\varepsilon(\\theta = 0)|$")
    ax.axhline(1e-15, color="gray", linestyle=":", linewidth=0.8)
    ax.annotate("rounding level", (0.75, 2e-15), fontsize=8, color="gray")
    ax.set_xlabel("3-momentum $k$ (units of $H$)")
    ax.set_ylabel("shift of the band level (units of $m$, logarithmic)")
    ax.set_title("the band does not feel the tip condition ($L = 3$)")
    ax.legend(fontsize=8)
    save_figure(fig, "tip_insensitivity",
                "The change of the brane-band level when the tip condition "
                "$(1 - Q(\\theta))\\chi(-L) = 0$ is changed from $\\theta = 0$ to "
                "$\\theta = 0.5$ (circles) and $\\theta = 1$ (squares), against the "
                "3-momentum $k$ (units of $H$), for $m = 1$, $L = 3$, logarithmic "
                "vertical axis in units of $m$; every shift lies below the "
                "suppression factor $\\exp(-k(e^{HL} - 1)/H)$ (line), falls by a "
                "factor of 12 to 34 for each step of $0.1$ in $k$, and from "
                "$k = 0.9$ on it is at the rounding level of the computer (dotted "
                "line): the band lives at the brane and does not see the cutoff.")
    '''),
    md(r"""
    ## 11. Particles, degeneracies and closed shells

    **Shells.** The lattice vectors $(n_1, n_2, n_3)$ with the same
    $n^2 = n_1^2 + n_2^2 + n_3^2$ have the same $|k| = 0.25\sqrt{n^2}$; $r_3(n^2)$
    counts them (the first values, checked against the Rust unit test, are
    $r_3 = 1, 6, 12, 8, 6, 24, 24, 12, 30$ for $n^2 = 0, 1, 2, 3, 4, 5, 6, 8, 9$; no
    vector has $n^2 = 7$). Each level of a block type then holds $4r_3(n^2)$ states.

    **Particles (CONVENTION).** In each sector (shell, $j$, parity) the particle
    levels are those with $\varepsilon > 0$ in the free problem, plus the $k = 0$
    zero modes; the negative ones form the sea. Because $\Phi$ grows with
    $\varepsilon$, the particle levels are exactly the labels $l \ge l_{\min}$, where
    $l_{\min}$ is the first label whose target lies above $\Phi(0)$. The Rust check
    `free_particle_branch_labels` verified this for all shells $n^2 \le 30$ and
    found the level closest to zero (away from the zero modes) at $0.4307\,m$.

    **Closed shells.** Filling the particle states from the bottom (the aufbau),
    $N$ is a closed shell when it ends exactly at the end of a group of degenerate
    levels (equal within $10^{-9}$). The Rust solver listed them up to
    $\varepsilon = 1.6\,m$ at every slice (`closed-shells.csv`), and chose its
    particle numbers by a rule: $N = 8$ (the zero modes), $N_{\rm large}$ = the
    largest closed shell below the BULK EDGE (the lowest level not on the brane
    band, the smaller of the odd label 0 and the even label 1 at $k = 0$), and
    $N_{\rm mid}$ = the closed shell nearest to $N_{\rm large}/4$
    (`parameters.json`). The next cell computes all of this for the slices 0 and
    0.5. It takes about 20 seconds.
    """),
    code(r'''
    def shells(n2_max):
        """[(n2, r3)] for n2 = 0 ... n2_max with r3(n2) > 0 (counting lattice points)."""
        r = math.isqrt(n2_max) + 1
        count = [0] * (n2_max + 1)
        for x in range(-r, r + 1):
            for y_ in range(-r, r + 1):
                for z_ in range(-r, r + 1):
                    s = x * x + y_ * y_ + z_ * z_
                    if s <= n2_max:
                        count[s] += 1
        return [(n2, c) for n2, c in enumerate(count) if c > 0]


    check(shells(9) == [(0, 1), (1, 6), (2, 12), (3, 8), (4, 6), (5, 24), (6, 24),
                        (8, 12), (9, 30)],
          "r3(n2) = 1, 6, 12, 8, 6, 24, 24, 12, 30 for n2 = 0, 1, 2, 3, 4, 5, 6, 8, 9")
    SECTORS = [(1, "even"), (1, "odd"), (-1, "even"), (-1, "odd")]
    SIGN = {1: "+1", -1: "-1"}


    def lowest_particle_labels(pairs, a4):
        """l_min of each (n2, r3, j, parity) and Phi(0)."""
        k_ = np.array([0.25 * math.sqrt(n2) for n2, _, _, _ in pairs])
        j_ = np.array([float(j) for _, _, j, _ in pairs])
        par = np.array([p for _, _, _, p in pairs])
        phi0 = shoot(0.0, k_, j_, a4)
        offset = np.where(par == "even", 0.0, 0.5 * np.pi)
        l_min = np.floor((phi0 - offset) / np.pi).astype(int) + 1
        nearest = np.round((phi0 - offset) / np.pi).astype(int)
        zero_mode = (k_ == 0.0) & (np.abs(phi0 - offset - nearest * np.pi) < 1e-12)
        return np.where(zero_mode, nearest, l_min), phi0, offset, k_, j_, par


    pairs30 = [(n2, r3, j, p) for n2, r3 in shells(30) for j, p in SECTORS]
    l_min, phi0, offset, k30, j30, p30 = lowest_particle_labels(pairs30, 0.0)
    e_first = levels(k30, j30, p30, l_min)
    e_below = levels(k30, j30, p30, l_min - 1)
    zero_k = k30 == 0.0
    branch_ok = (np.all(e_below < 0.0)
                 and np.all(e_first[zero_k & (p30 == "even")] == 0.0)
                 and np.all(e_first[~(zero_k & (p30 == "even"))] > 0.0))
    closest = float(min(np.min(e_first[~(zero_k & (p30 == "even"))]),
                        np.min(-e_below)))
    report("level closest to zero away from the zero modes (n2 <= 30)",
           f"{closest:.4f}", "m")
    check(branch_ok and f"{closest:.4f}" == "0.4307"
          and record_check("free_particle_branch_labels"),
          "particles are the labels l >= l_min in every sector (n2 <= 30)",
          record=f"{RUST_REPORT}, check free_particle_branch_labels")
    '''),
    md(r"""
    The next cell builds the closed shells at the slices 0 and 0.5 as the Rust
    solver does: for every shell (in the order of $n^2$) and sector it finds the
    particle levels $l_{\min}, l_{\min} + 1, \dots$ up to $1.6\,m$; it stops at the
    first shell $n^2 > 0$ that has no level below $1.6\,m$; it sorts all levels by
    energy (and by name), groups levels that agree within $10^{-9}$, and adds up the
    degeneracies $4r_3(n^2)$. Each level is named `n2:j:parity:label`. The table
    must equal the record row by row (the numbers $N$, the names of the last group,
    the energies to $10^{-11}$). Then it finds the bulk edge and the particle numbers
    and compares them with `parameters.json`.
    """),
    code(r'''
    def closed_shells(a4, n2_max, e_max=1.6):
        """[(N, eps_last, eps_next, names)] of the free aufbau at the slice a4."""
        pairs = [(n2, r3, j, p) for n2, r3 in shells(n2_max) for j, p in SECTORS]
        l_next, _, _, k_, j_, par = lowest_particle_labels(pairs, a4)
        found_levels = []  # (energy, degeneracy, name, n2)
        active = np.arange(len(pairs))
        while len(active) > 0:  # one more label in every sector that is still open
            e_ = levels(k_[active], j_[active], par[active], l_next[active], a4=a4)
            keep = e_ <= e_max
            for index, energy in zip(active[keep], e_[keep]):
                n2, r3, j, p = pairs[index]
                found_levels.append((float(energy), 4.0 * r3,
                                     f"{n2}:{SIGN[j]}:{p}:{l_next[index]}", n2))
            active = active[keep]
            l_next[active] += 1
        with_levels = {n2 for _, _, _, n2 in found_levels}
        stop = next(n2 for n2, _ in shells(n2_max) if n2 > 0 and n2 not in with_levels)
        found_levels = [lev for lev in found_levels if lev[3] < stop]
        found_levels.sort(key=lambda lev: (lev[0], lev[2]))
        table, total, i = [], 0.0, 0
        while i < len(found_levels):  # group the degenerate levels
            e0, group, names = found_levels[i][0], 0.0, []
            while i < len(found_levels) and found_levels[i][0] - e0 <= 1e-9:
                group += found_levels[i][1]
                names.append(found_levels[i][2])
                i += 1
            total += group
            following = found_levels[i][0] if i < len(found_levels) else float("nan")
            table.append((int(total), e0, following, ";".join(names)))
        return table, stop


    agree = True
    tables = {}
    for a_, n2_max in ((0.0, 40), (0.5, 80)):
        table, stop = closed_shells(a_, n2_max)
        tables[a_] = table
        mine_rows = [r for r in shells_record if float(r["a4"]) == a_]
        same = len(table) == len(mine_rows) and all(
            int(r["N_closed"]) == t[0] and r["levels_of_the_last_group"] == t[3]
            and abs(float(r["eps_last_filled"]) - t[1]) < 1e-11
            for r, t in zip(mine_rows, table))
        agree &= same and stop < n2_max
        say(f"slice {a_}: {len(table)} closed shells up to 1.6 m, the first shell "
            f"without a level below 1.6 m is n2 = {stop}; equal to the record: {same}")
    check(agree, "the closed shells of the slices 0 and 0.5 equal the record row by row",
          record=f"{SPECTRUM}/closed-shells.csv, rows a4 = 0 and 0.5")
    say("slice 0: N = " + ", ".join(str(t[0]) for t in tables[0.0]))
    bulk_edge = float(min(levels(0.0, 1.0, "odd", 0), levels(0.0, 1.0, "even", 1)))
    below_edge = [t for t in tables[0.0] if t[1] < bulk_edge and t[2] - t[1] > 1e-6]
    N_large = below_edge[-1][0]
    N_mid = min((t[0] for t in below_edge if t[0] >= 8),
                key=lambda n: abs(n - N_large / 4))
    parameters = json.loads(repository_file("Revision/kohn_sham/results/parameters.json")
                            .read_text(encoding="utf-8"))
    numbers = parameters["particleNumbers"]
    report("bulk edge", f"{bulk_edge:.12f}", "m")
    report("particle numbers N", f"8, {N_mid}, {N_large}")
    check(abs(bulk_edge - numbers["bulkEdge"]) < 1e-12 and N_large == 688
          and N_mid == 136 and numbers["values"] == [8.0, 136.0, 688.0],
          "the bulk edge 1.2922928281 and the particle numbers 8, 136, 688",
          record="Revision/kohn_sham/results/parameters.json, particleNumbers")
    '''),
    md(r"""
    The next cell draws the aufbau as a staircase: the number $N$ of filled
    particle states against the energy of the last filled level, at the slices 0 and
    0.5, with the bulk edge and the three particle numbers of the Revision runs
    marked. At the later slice the redshifted band holds many more states below the
    same energy.
    """),
    code(r'''
    fig, ax = plt.subplots(figsize=(8.0, 4.6))
    for a_, style in ((0.0, "-"), (0.5, "--")):
        energies = [t[1] for t in tables[a_]]
        counts = [t[0] for t in tables[a_]]
        ax.step(energies, counts, style, where="post",
                label=f"slice $a_{{4,0}} = {a_}$")
    ax.axvline(bulk_edge, color="gray", linestyle="-.", linewidth=0.8)
    ax.annotate("bulk edge", (bulk_edge + 0.015, 15), fontsize=8, color="gray")
    last_filled = {t[0]: t[1] for t in tables[0.0]}  # N -> its last filled level
    for n_ in (8, N_mid, N_large):
        t_ = last_filled[n_]
        ax.plot([t_], [n_], "o", color="C3")
        ax.annotate(f"N = {n_}", (t_ + 0.02, n_ * 0.75), fontsize=8, color="C3")
    ax.set_yscale("log")
    ax.set_xlabel("energy of the last filled level (units of $m$)")
    ax.set_ylabel("closed-shell particle number $N$ (logarithmic)")
    ax.set_title("the free aufbau: closed shells up to $1.6\\,m$")
    ax.legend(fontsize=8, loc="upper left")
    save_figure(fig, "closed_shells",
                "The closed shells of the free aufbau: the particle number $N$ "
                "(logarithmic axis) against the energy of the last filled level "
                "(units of $m$), at the slices $a_{4,0} = 0$ (solid) and $0.5$ "
                "(dashed), for $m = 1$, $L = 3$, $\\Delta k = 0.25$. Each step is one "
                "group of degenerate levels; the red dots mark the particle numbers "
                "$N = 8$ (the zero modes), $136$ and $688$ of the Revision runs; $688$ "
                "is the last closed shell below the bulk edge $1.2923\\,m$ "
                "(dash-dotted line); at the later slice the redshifted brane band "
                "holds many more particles below the same energy.")
    '''),
    md(r"""
    ## 12. The last check

    The last cell checks that the six figure files exist and prints the number of
    checks that passed.
    """),
    code(r'''
    figure_names = ["14c_1_band_structure.png", "14c_2_band_slope.png",
                    "14c_3_band_redshift.png", "14c_4_block_type_mirror.png",
                    "14c_5_tip_insensitivity.png", "14c_6_closed_shells.png"]
    check(all(output_file(f"{FIGURE_FOLDER}/{name}").is_file() for name in figure_names),
          "all six figure files of this notebook exist")
    all_checks_passed()
    '''),
    md(r"""
    ## 13. What this notebook showed

    - The eight zero modes become the brane band when the 3-momentum is switched
      on; its slope at $k = 0$ is $c = e^{-a_{4,0}}\frac{2M}{2M - H}\frac{1 -
      e^{-(2M-H)L}}{1 - e^{-2ML}}$, $1.9051482536$ for $M = H = 1$, $L = 3$ (PROVED
      by the Hellmann-Feynman rule; COMPUTED numerically at all five slices; the
      values reproduce the Rust solver's records).
    - Along the PRESCRIBED deflating history every level obeys the exact rescaling
      identity $\varepsilon(k, a_{4,0}) = \varepsilon(k e^{-a_{4,0}}, 0)$: the band
      is redshifted, and the gap of the free $N = 8$ state falls from $0.4307\,m$ at
      $a_{4,0} = 0$ to $0.0642\,m$ at $a_{4,0} = 2$.
    - The two block types have mirrored spectra, $\mathrm{spec}\,h_{-1} =
      -\mathrm{spec}\,h_{+1}$, and $\sigma_3$ maps $(j, k)$ to $(-j, -k)$.
    - The band lives at the brane: changing the tip condition shifts it by less than
      $\exp(-k(e^{HL} - 1)/H)$.
    - With the CONVENTION that the positive free levels and the zero modes are
      particle levels (its justification is OPEN), the free aufbau has the closed
      shells $8, 32, 80, 112, 136, \dots, 688$ below the bulk edge $1.2923\,m$; the
      Revision runs use $N = 8, 136, 688$ (reproduced from the rule).
    - ASSUMED: the Z2 mirror brane. CHOSEN: the regular tip at $L = 3$.
    """),
]

if __name__ == "__main__":
    raise SystemExit(run_builder(__file__))
