#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
"""Builder of Notebook 20c, "Allowed is not the same as happens: the threshold of pair
creation" (textbook "Universes in Pairs", chapter 20: Do universes come in pairs? What
the equations prove and what they do not).

The notebook Revision/textbook/notebooks/20c_allowed_not_happens.ipynb is BUILT from
this file by Revision/textbook/tools/nbkit.py (never edit the .ipynb by hand):

    python Revision/textbook/tools/nbkit.py build \
        Revision/textbook/notebooks/src/20c_allowed_not_happens.py --date YYYY-MM-DD
    python Revision/textbook/tools/nbkit.py check \
        Revision/textbook/notebooks/src/20c_allowed_not_happens.py

A lesson from ordinary physics, computed from zero: what conservation laws can and
cannot say about the creation of a pair (an electron and a positron made from light).
It separates the three questions "is it allowed?", "does it happen?" and "how often?"
that the chapter asks about universes, and reads from the Revision record what the
pairing theorems do not establish.  The relativistic energy-momentum relation and the
conservation of energy and momentum are standard physics, ASSUMED here; every number
is computed by the notebook.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools"))
from nbkit import code, md, run_builder  # noqa: E402

FIGURES = [
    "invariant_mass_inequality",
    "nucleus_threshold",
    "allowed_photon_energies",
    "two_photon_regions",
]

FACTS = {
    "id": "20c",
    "name": "20c_allowed_not_happens",
    "title": "Allowed is not the same as happens: the threshold of pair creation",
    "purpose": (
        "It computes, from the relativistic relation between energy, momentum and mass "
        "and the conservation of energy and momentum, when the creation of an electron "
        "and a positron from light is allowed: it proves with sympy that the invariant "
        "mass of two bodies is at least the sum of their masses and tests it on 20000 "
        "random pairs, shows that a single photon can never make a pair, derives the "
        "threshold photon energy 2m(1 + m/M) on a nucleus of mass M with an exact final "
        "state at the threshold, and the allowed region for two photons at any angle. "
        "It then reads from the Revision record what the pairing theorems do not "
        "establish (no creation process, no rate, no amplitude), and draws four "
        "teaching figures."
    ),
    "records": [
        ["Revision/pairing/pairing-theory.json",
         "the list not_established of what the pairing theorems do not establish "
         "(read; three of its items are checked)"],
        ["Revision/lead_checks/reports/charge-conjugation-and-u1.json",
         "check u1_noether_matrix_identity, the local conservation law of the U(1) "
         "charge of one universe (its verdict is read)"],
    ],
    "packages": ["numpy", "sympy", "matplotlib"],
    "needs_rust": [],
    "expected_seconds": 15,
    "timeout_seconds": 300,
    "files_written": ["Revision/textbook/figures/20c.captions.json"] + [
        f"Revision/textbook/figures/20c_{k}_{name}.png"
        for k, name in enumerate(FIGURES, 1)],
    "final_lines": [
        "PASS every figure file of this notebook exists",
        "ALL 12 CHECKS PASSED (notebook 20c)",
    ],
    "troubleshooting": [
        ["\"FileNotFoundError\" naming a file below the folder Revision",
         "the notebook reads two files of the repository; it must be opened inside the "
         "folder Revision/textbook/notebooks of a complete copy of the repository made "
         "with git clone (a notebook copied alone to another folder cannot find them)."],
    ],
}

CELLS = [
    md(r"""
    ## 1. What this notebook computes

    The request behind this chapter speaks of universes "created in pairs". Before we
    can say what the equations of this book do and do not prove about that, we must be
    clear what a proof of creation would contain. This notebook works it out on the
    one example of pair creation that physics understands completely: an electron and
    a positron (its antiparticle) made from light. It separates three questions:

    - **Q1, allowed?** Do the conservation laws (energy, momentum, charge) permit the
      process? This is answered here completely, by algebra and by computation.
    - **Q2, does it happen?** Is there a dynamical law that turns the initial state
      into the final one? For light this is quantum electrodynamics, which this
      notebook does NOT compute.
    - **Q3, how often?** A number: a rate, a probability, a cross section. Again a
      result of the dynamics, not of the conservation laws.

    It computes: the invariant mass and the inequality behind every threshold (proved
    with sympy, tested on 20000 random pairs); why one photon can never make a pair;
    the threshold photon energy on a nucleus, with an exact final state at the
    threshold; and the allowed region for two photons. At the end it reads, from the
    Revision record of the pairing theorems, which of the three questions those
    theorems answer for universes: none of Q2 and Q3.
    """),
    md(r"""
    ## 3. The words used in this notebook

    - **Units**: the speed of light is 1, and energies, momenta and masses are
      measured in units of the electron mass $m$ (so $m = 1$ in the code).
    - **Momentum** $\vec p = (p_1, p_2, p_3)$, a vector; its length is $|\vec p| =
      \sqrt{p_1^2 + p_2^2 + p_3^2}$. **Energy** $E$ of a body of mass $\mu$:
      $E = \sqrt{\mu^2 + |\vec p|^2}$ (the energy-momentum relation of special
      relativity). A **photon** (light) has $\mu = 0$, so $E = |\vec p|$.
    - **Electron, positron**: two particles of the same mass $m$ and opposite
      electric charge $-1$ and $+1$. **Nucleus**: the heavy centre of an atom, mass
      $M$.
    - **Conservation law**: a quantity whose total is the same before and after any
      process (here the total energy, the total momentum and the total charge).
    - **Invariant mass** $\mu$ of a collection of bodies: $\mu^2 = E_{\rm tot}^2 -
      |\vec p_{\rm tot}|^2$, computed from the totals. Because the totals are
      conserved, so is $\mu$. For one body $\mu$ is its mass.
    - **Threshold**: the smallest energy at which a process is allowed.
    - **Allowed** (in this notebook): not forbidden by any conservation law. Allowed
      does not mean that the process happens, nor how often.
    - **Rate, cross section, amplitude**: numbers that say how often a process
      happens; they come from a dynamical theory.
    - **Lemma, proposition**: a proved statement (a lemma is a step towards others).
    """),
    md(r"""
    ## 4. The physical and mathematical situation

    **ASSUMED (standard physics of special relativity):** each body has $E^2 =
    \mu^2 + |\vec p|^2$; the total energy and the total momentum of an isolated system
    do not change; nor does its total electric charge. Everything else is derived and
    computed here.

    **The rule of every threshold.** A process A $\to$ B is forbidden if any conserved
    quantity has different values in A and in B. Since $\mu^2$ is built from conserved
    totals, $\mu_A = \mu_B$ is NECESSARY. The lemma of section 5 says that a final
    state made of bodies with masses $\mu_1, \mu_2, \dots$ always has $\mu_B \geq \mu_1
    + \mu_2 + \cdots$. So the initial state must bring at least that much invariant
    mass:

    $$\mu_A \;\geq\; \text{(sum of the final masses)}.$$

    This is a necessary condition only. Whether the process then happens, and how
    often, is decided by the dynamics.
    """),
    md(r"""
    ## 5. The lemma: two bodies have at least the sum of their masses

    **Lemma.** Two bodies with masses $\mu_1, \mu_2 \geq 0$, momenta $\vec p_1,
    \vec p_2$ and energies $E_i = \sqrt{\mu_i^2 + |\vec p_i|^2}$ have together
    $(E_1 + E_2)^2 - |\vec p_1 + \vec p_2|^2 \geq (\mu_1 + \mu_2)^2$.

    *Proof, line by line.* Write $a = |\vec p_1|$, $b = |\vec p_2|$.

    1. Multiply out the squares: $(E_1 + E_2)^2 - |\vec p_1 + \vec p_2|^2 =
       (E_1^2 - a^2) + (E_2^2 - b^2) + 2(E_1E_2 - \vec p_1\cdot\vec p_2)$.
    2. Use $E_i^2 - |\vec p_i|^2 = \mu_i^2$: this is $\mu_1^2 + \mu_2^2 +
       2(E_1E_2 - \vec p_1\cdot\vec p_2)$.
    3. The dot product is at most the product of the lengths, $\vec p_1\cdot\vec p_2
       \leq ab$, so it suffices to show $E_1E_2 \geq \mu_1\mu_2 + ab$.
    4. Both sides are not negative, so compare their squares:
       $E_1^2E_2^2 - (\mu_1\mu_2 + ab)^2 = (\mu_1^2 + a^2)(\mu_2^2 + b^2) -
       (\mu_1\mu_2 + ab)^2$.
    5. Multiplying out, the terms $\mu_1^2\mu_2^2$ and $a^2b^2$ cancel and what remains
       is $\mu_1^2b^2 + \mu_2^2a^2 - 2\mu_1\mu_2ab = (\mu_1b - \mu_2a)^2 \geq 0$.
    6. Hence $E_1E_2 - \vec p_1\cdot\vec p_2 \geq \mu_1\mu_2$, and line 2 is at least
       $\mu_1^2 + \mu_2^2 + 2\mu_1\mu_2 = (\mu_1 + \mu_2)^2$. QED.

    The next cell checks line 5 with sympy, then tests the lemma on 20000 random
    pairs of bodies (random masses between 0 and 3, random momenta, fixed seed).
    """),
    code(r'''
    import numpy as np  # arrays and random numbers
    import sympy as sp  # exact algebra

    mu1, mu2, a, b = sp.symbols("mu1 mu2 a b", nonnegative=True)
    E1_sq, E2_sq = mu1 ** 2 + a ** 2, mu2 ** 2 + b ** 2  # E_i^2 = mu_i^2 + |p_i|^2
    line5 = sp.expand(E1_sq * E2_sq - (mu1 * mu2 + a * b) ** 2)
    check(sp.expand(line5 - (mu1 * b - mu2 * a) ** 2) == 0,
          "line 5: E1^2 E2^2 - (mu1 mu2 + a b)^2 = (mu1 b - mu2 a)^2")


    def invariant_mass(energies, momenta):
        """mu = sqrt(E_tot^2 - |p_tot|^2) of a collection of bodies."""
        E_total = np.sum(energies, axis=0)
        p_total = np.sum(momenta, axis=0)
        return np.sqrt(np.maximum(E_total ** 2 - np.sum(p_total ** 2, axis=-1), 0.0))


    rng = np.random.default_rng(20261007)  # fixed seed: the same numbers every run
    count = 20000
    masses = rng.uniform(0.0, 3.0, size=(2, count))  # mu1, mu2
    momenta = rng.normal(size=(2, count, 3)) * rng.uniform(0.0, 4.0, size=(2, count, 1))
    energies = np.sqrt(masses ** 2 + np.sum(momenta ** 2, axis=-1))
    mu_total = invariant_mass(energies, momenta)
    margin = mu_total - masses.sum(axis=0)  # must never be negative
    report("smallest margin mu_total - (mu1 + mu2) in 20000 pairs",
           f"{margin.min():.2e}")
    check(margin.min() > -1e-12, "the lemma holds for all 20000 random pairs")
    '''),
    md(r"""
    The next cell draws the 20000 pairs: the invariant mass of the pair against the
    sum of the two masses. Every point lies on or above the diagonal; points on the
    diagonal are pairs whose bodies move together (equal velocities, the equality case
    $\mu_1b = \mu_2a$ of line 5 with parallel momenta).
    """),
    code(r'''
    fig, ax = plt.subplots(figsize=(6.4, 5.0))
    ax.plot(masses.sum(axis=0), mu_total, ".", markersize=1.5, alpha=0.4,
            color="tab:blue", label="20000 random pairs")
    ax.plot([0, 6], [0, 6], color="black", linewidth=1.5,
            label="$\\mu = \\mu_1 + \\mu_2$")
    ax.set_xlabel("sum of the masses $\\mu_1 + \\mu_2$ (units $m$)")
    ax.set_ylabel("invariant mass of the pair $\\mu$ (units $m$)")
    ax.set_xlim(0, 6)
    ax.set_ylim(0, 16)
    ax.set_title("Two bodies have at least the sum of their masses")
    ax.legend(fontsize=8, loc="upper left", markerscale=6)
    save_figure(fig, "invariant_mass_inequality",
                "The invariant mass "
                "$\\mu = \\sqrt{E_{\\rm tot}^2 - |\\vec p_{\\rm tot}|^2}$ of 20000 random "
                "pairs of bodies (vertical) against the sum of their "
                "masses $\\mu_1 + \\mu_2$ (horizontal), both in units of the electron "
                "mass $m$; masses between 0 and 3, random momenta, fixed seed. Every "
                "point lies on or above the black diagonal $\\mu = \\mu_1 + \\mu_2$, as "
                "the lemma proves: a final state of bodies with given masses needs at "
                "least the sum of those masses as invariant mass, which is the origin "
                "of every threshold.")
    '''),
    md(r"""
    ## 6. One photon can never make a pair

    **Proposition.** A single photon in empty space cannot turn into an electron and
    a positron. *Proof.* Before: one photon, $\mu_A^2 = E^2 - |\vec p|^2 = 0$. After:
    two bodies of mass $m$, so by the lemma $\mu_B \geq 2m > 0$. The invariant mass is
    conserved, so $0 \geq 2m$, which is false. QED.

    Charge does not forbid it ($-1 + 1 = 0$, the photon's charge), and energy alone
    does not either (the photon may have any energy): the COMBINATION of energy and
    momentum forbids it. The next cell checks the statement on 5000 random final
    states: none has invariant mass zero; the smallest is $2m$.
    """),
    code(r'''
    pair_momenta = rng.normal(size=(2, 5000, 3)) * 3.0  # electron and positron
    pair_energies = np.sqrt(1.0 + np.sum(pair_momenta ** 2, axis=-1))  # m = 1
    pair_mu = invariant_mass(pair_energies, pair_momenta)
    report("smallest invariant mass of 5000 electron-positron states",
           f"{pair_mu.min():.4f}")
    check(pair_mu.min() >= 2.0 - 1e-12, "every electron-positron state has mu >= 2 m > 0")
    '''),
    md(r"""
    ## 7. A photon on a nucleus: the threshold

    A photon of energy $E_\gamma$ hits a nucleus of mass $M$ at rest; the final state
    is an electron, a positron and the nucleus. Line by line:

    1. Before: total energy $E_\gamma + M$, total momentum of length $E_\gamma$ (the
       photon's), so $\mu_A^2 = (E_\gamma + M)^2 - E_\gamma^2 = M^2 + 2E_\gamma M$.
    2. After: by the lemma (applied twice) $\mu_B \geq m + m + M$.
    3. Conservation, $\mu_A = \mu_B$, therefore needs $M^2 + 2E_\gamma M \geq
       (2m + M)^2 = M^2 + 4mM + 4m^2$.
    4. Subtract $M^2$ and divide by $2M$: $E_\gamma \geq 2m + 2m^2/M =
       2m(1 + m/M)$.

    At exactly the threshold the three final bodies move together with the common
    velocity $v = p_{\rm tot}/E_{\rm tot}$ (the equality case of the lemma). For
    $M = 4m$: $E_\gamma = 5m/2$, $p_{\rm tot} = 5m/2$, $E_{\rm tot} = 13m/2$,
    $\mu = 6m$, and each body carries the share $\mu_i/\mu$ of the momentum: $5m/12$
    for the electron and for the positron, $5m/3$ for the nucleus. The next cell
    solves line 3 with sympy, checks this final state EXACTLY (energies and momenta
    add up to the initial ones), and computes the threshold for three nuclei: $M =
    4m$ (helium-like), $1000m$ and $1836m$ (about a proton).
    """),
    code(r'''
    E_gamma, M_nuc, m_e = sp.symbols("E_gamma M m", positive=True)
    mu_initial_sq = (E_gamma + M_nuc) ** 2 - E_gamma ** 2  # line 1
    threshold = sp.solve(sp.Eq(mu_initial_sq, (2 * m_e + M_nuc) ** 2), E_gamma)[0]
    say(f"threshold photon energy: {sp.factor(threshold)}")
    check(sp.simplify(threshold - 2 * m_e * (1 + m_e / M_nuc)) == 0,
          "E_threshold = 2 m (1 + m/M)")
    M4 = 4  # the nucleus of mass 4 m, with m = 1
    E_th = threshold.subs({m_e: 1, M_nuc: M4})  # 5/2
    p_total, E_total = E_th, E_th + M4  # the initial totals
    mu_final = sp.Integer(2 + M4)  # 6 m
    shares = [1, 1, M4]  # electron, positron, nucleus masses
    p_parts = [sp.Rational(mass) * p_total / mu_final for mass in shares]
    E_parts = [sp.sqrt(mass ** 2 + p ** 2) for mass, p in zip(shares, p_parts)]
    say(f"final state at threshold: momenta {p_parts}, energies {E_parts}")
    check(sum(p_parts) == p_total and sp.simplify(sum(E_parts) - E_total) == 0
          and E_th == sp.Rational(5, 2),
          "M = 4 m: the threshold state conserves energy and momentum exactly")
    for M_value in (4, 1000, 1836):
        value = threshold.subs({m_e: 1, M_nuc: M_value})
        report(f"threshold for M = {M_value} m", f"{sp.nsimplify(value)} = "
               f"{float(value):.6f} m")
    check(threshold.subs({m_e: 1, M_nuc: 1836}) == 2 + sp.Rational(2, 1836),
          "M = 1836 m: the threshold is 2 m + 2 m/1836, just above 2 m")
    '''),
    md(r"""
    The next cell draws the threshold $E_\gamma/m = 2(1 + m/M)$ against the nucleus
    mass $M/m$ on a logarithmic axis: a light nucleus needs much more than the two rest
    energies $2m$, a heavy one takes up the momentum and almost no energy.
    """),
    code(r'''
    M_axis = np.logspace(-0.5, 4, 400)  # M/m from about 0.3 to 10000
    fig, ax = plt.subplots(figsize=(7.0, 4.4))
    ax.semilogx(M_axis, 2 * (1 + 1 / M_axis), color="tab:blue",
                label="threshold $2m(1 + m/M)$")
    ax.axhline(2.0, color="black", linestyle=":", label="the two rest energies $2m$")
    for M_value, marker in ((4, "o"), (1000, "s"), (1836, "^")):
        ax.plot([M_value], [2 * (1 + 1 / M_value)], marker, color="tab:red",
                markersize=7, label=f"$M = {M_value}m$: {2 * (1 + 1 / M_value):.5f}$m$")
    ax.fill_between(M_axis, 2 * (1 + 1 / M_axis), 9.0, color="tab:green", alpha=0.12,
                    label="allowed (not forbidden)")
    ax.set_ylim(1.5, 9.0)
    ax.set_xlabel("mass of the nucleus $M/m$")
    ax.set_ylabel("photon energy $E_\\gamma/m$")
    ax.set_title("Pair creation on a nucleus: the threshold")
    ax.legend(fontsize=8, loc="upper right")
    save_figure(fig, "nucleus_threshold",
                "The smallest photon energy $E_\\gamma$ (vertical, units of the "
                "electron mass $m$) at which energy and momentum conservation allow a "
                "photon hitting a nucleus of mass $M$ (horizontal, logarithmic, units "
                "$m$) to make an electron-positron pair: $E_\\gamma = 2m(1 + m/M)$ "
                "(blue). Above it (green) the process is allowed, below it forbidden. "
                "Red markers: $M = 4m$ ($2.5m$), $1000m$ ($2.002m$) and $1836m$, about "
                "a proton ($2.00109m$). For heavy nuclei the threshold approaches the "
                "two rest energies $2m$ (dotted). The curve says nothing about how "
                "often the process happens above the threshold.")
    '''),
    md(r"""
    The next cell shows the same threshold as a comparison of two curves for $M =
    4m$: the invariant mass the initial state brings, $\mu_A = \sqrt{M^2 +
    2E_\gamma M}$, rises with the photon energy; the invariant mass the final state
    needs at least is the constant $2m + M = 6m$. They cross at $E_\gamma = 5m/2$.
    """),
    code(r'''
    E_axis = np.linspace(0.0, 6.0, 601)
    brought = np.sqrt(M4 ** 2 + 2 * E_axis * M4)  # mu_A for M = 4 m
    crossing = E_axis[np.argmin(np.abs(brought - (2 + M4)))]
    report("crossing of the two curves (M = 4 m)", f"{crossing:.2f} m")
    check(abs(crossing - 2.5) < 0.01, "the curves cross at E_gamma = 2.5 m")
    fig, ax = plt.subplots(figsize=(7.0, 4.4))
    ax.plot(E_axis, brought, color="tab:blue", label="brought: $\\sqrt{M^2 + 2E_\\gamma M}$")
    ax.axhline(2 + M4, color="tab:red", label="needed at least: $2m + M = 6m$")
    ax.axvline(2.5, color="black", linestyle=":", label="threshold $E_\\gamma = 5m/2$")
    ax.fill_between(E_axis, 2 + M4, brought, where=brought >= 2 + M4,
                    color="tab:green", alpha=0.15, label="allowed")
    ax.set_xlabel("photon energy $E_\\gamma/m$")
    ax.set_ylabel("invariant mass (units $m$)")
    ax.set_title("Photon on a nucleus of mass $M = 4m$")
    ax.legend(fontsize=8, loc="lower right")
    save_figure(fig, "allowed_photon_energies",
                "For a photon hitting a nucleus of mass $M = 4m$ at rest: the invariant "
                "mass the initial state brings, $\\sqrt{M^2 + 2E_\\gamma M}$ (blue), "
                "and the smallest invariant mass the final state of electron, positron "
                "and nucleus needs, $2m + M = 6m$ (red), against the photon energy "
                "$E_\\gamma$ (horizontal; all in units of the electron mass $m$). "
                "Conservation of energy and momentum allows the pair only where the "
                "blue curve is at or above the red line (green), from the threshold "
                "$E_\\gamma = 5m/2$ (dotted) on.")
    '''),
    md(r"""
    ## 8. Two photons

    Two photons of energies $E_a$ and $E_b$ meet at the angle $\theta$ between their
    directions. Line by line: $\mu^2 = (E_a + E_b)^2 - |\vec p_a + \vec p_b|^2$;
    multiplying out with $|\vec p_a| = E_a$, $|\vec p_b| = E_b$ and $\vec p_a\cdot\vec
    p_b = E_aE_b\cos\theta$ gives $\mu^2 = 2E_aE_b(1 - \cos\theta)$. The lemma requires
    $\mu \geq 2m$, so the pair is allowed exactly when

    $$E_aE_b \;\geq\; \frac{2m^2}{1 - \cos\theta}.$$

    Head on ($\theta = 180$ degrees, $\cos\theta = -1$) this is $E_aE_b \geq m^2$; for
    photons moving in the same direction ($\theta = 0$) never. The next cell checks
    the formula with sympy and draws the allowed regions for three angles.
    """),
    code(r'''
    Ea, Eb, theta = sp.symbols("E_a E_b theta", positive=True)
    pa = sp.Matrix([Ea, 0, 0])  # photon a along the first axis
    pb = sp.Matrix([Eb * sp.cos(theta), Eb * sp.sin(theta), 0])  # photon b at angle
    mu_sq = sp.simplify((Ea + Eb) ** 2 - (pa + pb).dot(pa + pb))
    check(sp.simplify(mu_sq - 2 * Ea * Eb * (1 - sp.cos(theta))) == 0,
          "two photons: mu^2 = 2 E_a E_b (1 - cos theta)")
    check(sp.simplify(mu_sq.subs(theta, sp.pi) - 4 * Ea * Eb) == 0
          and mu_sq.subs(theta, 0) == 0,
          "head on mu^2 = 4 E_a E_b; same direction mu^2 = 0 (never allowed)")
    grid = np.linspace(0.05, 6.0, 300)
    EA, EB = np.meshgrid(grid, grid)
    fig, ax = plt.subplots(figsize=(6.4, 5.4))
    for degrees, colour in ((180, "tab:blue"), (90, "tab:orange"), (45, "tab:red")):
        bound = 2.0 / (1 - np.cos(np.radians(degrees)))  # E_a E_b >= bound (m = 1)
        ax.contourf(EA, EB, (EA * EB >= bound).astype(float), levels=[0.5, 1.5],
                    colors=[colour], alpha=0.12)
        ax.contour(EA, EB, EA * EB, levels=[bound], colors=[colour])
        ax.plot([], [], color=colour,
                label=f"$\\theta = {degrees}$ deg: $E_aE_b \\geq {bound:.2f}m^2$")
    ax.set_xlabel("energy of photon a, $E_a/m$")
    ax.set_ylabel("energy of photon b, $E_b/m$")
    ax.set_title("Two photons: allowed above each curve")
    ax.legend(fontsize=8, loc="upper right")
    save_figure(fig, "two_photon_regions",
                "Two photons of energies $E_a$ and $E_b$ (horizontal and vertical, "
                "units of the electron mass $m$) meeting at the angle $\\theta$: an "
                "electron-positron pair is allowed above the curve $E_aE_b = "
                "2m^2/(1 - \\cos\\theta)$ (shaded), drawn for head-on photons, "
                "$\\theta = 180$ degrees (blue, $E_aE_b \\geq m^2$), for $90$ degrees "
                "(orange, $2m^2$) and $45$ degrees (red, about $6.83m^2$). The smaller "
                "the angle, the more energy is needed; photons moving in the same "
                "direction can never make a pair.")
    '''),
    md(r"""
    ## 9. What the conservation laws cannot say, and what this means for universes

    Sections 5 to 8 answered Q1 completely for light: below a threshold the process
    is forbidden, above it allowed. They say NOTHING about Q2 and Q3. That pairs are
    really made above the threshold, and how often, was computed from quantum
    electrodynamics, the dynamical theory of electrons and light, by Bethe and Heitler
    (H. Bethe and W. Heitler, Proc. R. Soc. Lond. A 146, 83 (1934)) for a photon on a
    nucleus and by Breit and Wheeler (G. Breit and J. A. Wheeler, Phys. Rev. 46, 1087
    (1934)) for two photons. This notebook quotes these works; it does not compute
    their results.

    For universes of masses $+m$ and $-m$ the theory of this book supplies:

    - **Q1, conserved quantities.** Light: energy, momentum and charge. Universes:
      the U(1) charge of each universe obeys an exact local conservation law (PROVED
      in the record); its total is constant only if no charge flows through the brane
      $z = \pi/2$ (the no-flux condition, ASSUMED: the record does not derive it, and
      on the homogeneous solutions of chapter 18 charge does flow through the brane).
      The momenta along the six directions on which the metric does not depend ($x_1$,
      $x_2$, $x_3$, $x_5$, $x_6$, $x_7$) obey local laws too, separately for each
      universe (derived from the record's on-shell law
      $\nabla_\mu T^\mu{}_\nu = 0$ and the symmetry of $T$; ASSUMED: the boundary
      terms vanish); the energy of a universe is NOT a conserved
      quantity, because the deflating metric depends on the time $x_4$ (for a
      homogeneous source the record's identity is $d\rho/dx_4 = -3a_4'(p_3 - p_t)$).
    - **Q1, interaction.** Light couples to electrons. No term of any Lagrangian of
      the record couples two universes.
    - **Q2, the dynamics of creation.** Light: quantum electrodynamics. Universes:
      none; no creation process is derived.
    - **Q3, rate and amplitude.** Light: computed in 1934. Universes: none; no rate,
      probability or amplitude.

    One consequence can be drawn in two lines from the record's conservation law
    (status: derived here; ASSUMED: the boundary terms vanish, e.g. periodic
    coordinates and no flux through the brane $z = \pi/2$, a condition that the
    record does not derive). Each universe obeys its own field equation and nothing
    couples the two, so under these conditions the charge $Q_+$ of the first
    universe is conserved on its own. If both
    fields were zero at some time, $Q_+$ would be zero at every time. A T1 pair whose
    members carry the charges $Q$ and $-Q$ with $Q \neq 0$ can therefore not evolve
    out of zero fields in the theory as built: the zero TOTAL charge of a T1 pair does
    not make its appearance allowed, because the separate charges are conserved too
    (under the no-flux condition).

    The next cell reads the record's own list of what the pairing theorems do not
    establish and checks that it names the missing answers to Q2 and Q3.
    """),
    code(r'''
    theory = json.loads(repository_file("Revision/pairing/pairing-theory.json")
                        .read_text(encoding="utf-8"))
    missing = theory["not_established"]  # the record's list
    say(f"the record lists {len(missing)} things the pairing theorems do not establish;")
    for item in missing[:3]:
        say("- " + item.split(":")[0] + ": " + item.split(":")[1].split(";")[0].strip())
    starts = [item.split(":")[0] for item in missing]
    check({"No creation process", "No rate and no amplitude",
           "No dynamical necessity"} <= set(starts),
          "the record states: no creation process, no rate or amplitude, no necessity")
    u1 = json.loads(repository_file(
        "Revision/lead_checks/reports/charge-conjugation-and-u1.json")
        .read_text(encoding="utf-8"))
    verdicts = {entry["name"]: entry["verdict"] for entry in u1["checks"]}
    check(verdicts.get("u1_noether_matrix_identity") == "PASS",
          "the record proves the local U(1) conservation law of one universe",
          record="Revision/lead_checks/reports/charge-conjugation-and-u1.json, check "
                 "u1_noether_matrix_identity")
    '''),
    md(r"""
    ## 10. The last check

    The last cell checks that the four figure files exist in the folder
    Revision/textbook/figures and prints the number of checks that passed.
    """),
    code(r'''
    figure_names = ["invariant_mass_inequality", "nucleus_threshold",
                    "allowed_photon_energies", "two_photon_regions"]
    paths = [output_file(f"{FIGURE_FOLDER}/20c_{k}_{name}.png")
             for k, name in enumerate(figure_names, 1)]
    check(all(path.is_file() for path in paths),
          "every figure file of this notebook exists")
    all_checks_passed()
    '''),
    md(r"""
    ## 11. What this notebook showed

    - The invariant mass of two bodies is at least the sum of their masses (PROVED
      with sympy, and true for 20000 random pairs); this is the origin of every
      threshold (figure 1).
    - One photon can never make an electron-positron pair; on a nucleus of mass $M$
      the photon needs at least $2m(1 + m/M)$: $2.5m$ for $M = 4m$, $2.00109m$ for
      $M = 1836m$, with an exact final state at the threshold (figures 2 and 3); two
      photons need $E_aE_b \geq 2m^2/(1 - \cos\theta)$ (figure 4).
    - These are answers to Q1 only (allowed or forbidden). That the process happens,
      and how often, needs a dynamical theory (quantum electrodynamics, quoted, not
      computed).
    - For universes the record has local conservation laws but no interaction
      between universes, no creation process, no rate and no amplitude: Q2 and Q3 are
      not answered, and with separately conserved charges (ASSUMED: no flux through
      the brane) a T1 pair with nonzero charges cannot evolve out of zero fields in
      the theory as built.
    """),
]

if __name__ == "__main__":
    raise SystemExit(run_builder(__file__))
