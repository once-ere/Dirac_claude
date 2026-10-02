#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
"""Builder of Notebook 09b, "Homogeneous condensates: energy, pressure, equation of state
and energy exchange" (textbook "Universes in Pairs", chapter 09).

The notebook Revision/textbook/notebooks/09b_condensates.ipynb is BUILT from this file by
Revision/textbook/tools/nbkit.py (never edit the .ipynb by hand):

    python Revision/textbook/tools/nbkit.py build \
        Revision/textbook/notebooks/src/09b_condensates.py --date YYYY-MM-DD
    python Revision/textbook/tools/nbkit.py check \
        Revision/textbook/notebooks/src/09b_condensates.py

The exact homogeneous solution, its energy density and pressure, the vanishing of its
x4-x8 component and the unbounded energy of the commuting field are statements of the
Revision record; the notebook computes them anew from the Revision gamma matrices and
asserts the agreement, naming the record file and check.  The toy fluids of section 12
are an ILLUSTRATION of the conservation identity, labelled as such.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools"))
from nbkit import code, md, run_builder  # noqa: E402

FIGURES = [
    "Revision/textbook/figures/09b_1_sign_of_s.png",
    "Revision/textbook/figures/09b_2_condensate_solutions.png",
    "Revision/textbook/figures/09b_3_energy_and_pressure.png",
    "Revision/textbook/figures/09b_4_equation_of_state.png",
    "Revision/textbook/figures/09b_5_regime_map.png",
    "Revision/textbook/figures/09b_6_energy_exchange.png",
    "Revision/textbook/figures/09b_7_energy_sign.png",
]

FACTS = {
    "id": "09b",
    "name": "09b_condensates",
    "title": "Homogeneous condensates: energy, pressure, equation of state and energy "
             "exchange",
    "purpose": (
        "It builds the exact homogeneous solutions (condensates) of the commuting field "
        "dirac16complex00 with the potential U = (lambda/2) S^2 in the author's metric "
        "from the Revision gamma matrices, checks that S stays constant and that the "
        "energy density and pressure are rho = m S + U and p = S U' - U in every "
        "direction, measures the equation of state w = p/rho of actual solutions "
        "against lambda S/m, maps where condensates oscillate or grow, shows with "
        "assumed toy fluids how energy is exchanged between 3-space and the extra "
        "times when the two pressures differ (and that a condensate exchanges none), "
        "and shows that the energy of the commuting field has no lower bound, in seven "
        "teaching plots."
    ),
    "records": [
        ["Revision/algebra/gammas.json",
         "the author's gamma matrices, the matrices C and B (the fixture)"],
        ["Revision/algebra/reports/python-algebra.json",
         "C as diag(-sigma, sigma) and the signature of B"],
        ["Revision/algebra/reports/wolfram-algebra.json",
         "sigma squares to one and has trace zero"],
        ["Revision/theory/field-theory.json",
         "the formulas of the exact solutions and of the homogeneous energy density "
         "and pressure"],
        ["Revision/theory/reports/wolfram-field-theory.json",
         "the solution matrix, the exact nonlinear homogeneous solution, the energy "
         "exchange"],
        ["Revision/theory/reports/python-field-theory.json",
         "the same solution, the homogeneous energy density and pressure, the x4-x8 "
         "component, the trace"],
        ["Revision/theory/reports/python-scope.json",
         "the energy of the commuting field is unbounded below"],
        ["Revision/theory/reports/wolfram-scope.json",
         "the same statement, verified with the Wolfram Language"],
        ["Revision/pairing/reports/python-pairing.json",
         "the Krein inertia (4,4) of every real-frequency eigenspace"],
    ],
    "packages": ["numpy", "matplotlib"],
    "needs_rust": [],
    "expected_seconds": 10,
    "timeout_seconds": 300,
    "files_written": ["Revision/textbook/figures/09b.captions.json"] + FIGURES,
    "final_lines": [
        "PASS the seven figures of this notebook are saved and captioned",
        "ALL 32 CHECKS PASSED (notebook 09b)",
    ],
    "troubleshooting": [],
}

CELLS = [
    md(r"""
    ## 1. What this notebook computes

    A *condensate* is a configuration of the field that is the same at every place:
    it depends on the time $x_4$ only. This notebook builds the exact condensates of
    the commuting field dirac16complex00 with the potential
    $U(S) = \frac{\lambda}{2}S^2$ in the author's metric and studies their
    energy-momentum tensor. It

    - shows that the number $S = \bar\Phi\Phi$ can have either sign (a histogram);
    - builds the exact solution
      $\Phi(x_4) = (\cosh(kx_4) + \frac{\sinh(kx_4)}{k}M)\chi$ of the Revision
      record, checks the field equation and that $S$ stays constant, for one
      condensate that oscillates and one that grows;
    - computes from the solution the energy density $\rho$ and the pressure $p$ and
      checks the record's values $\rho = mS + U$ and $p = SU' - U$, the same in all
      seven directions, and the vanishing of the $x_4$-$x_8$ component;
    - measures the equation of state $w = p/\rho$ of actual solutions and compares it
      with $w = \lambda S/(2m + \lambda S)$; finds where $w = -1$;
    - maps where condensates oscillate and where they grow;
    - shows with toy fluids (an ILLUSTRATION, not solutions of the field equations)
      how energy flows between 3-space and the extra times when $p_3 \neq p_t$, and
      that a condensate, with $p_3 = p_t$, exchanges none;
    - shows that the energy of the commuting field has no lower bound;
    - draws seven teaching plots.
    """),
    md(r"""
    ## 3. The words used in this notebook

    - **Condensate (homogeneous configuration)**: a field that depends only on the
      time $x_4$, not on $x_1, x_2, x_3, x_5, x_6, x_7, x_8$.
    - **Effective mass** $V = m + U'(S) = m + \lambda S$: the number that multiplies
      $\Phi$ on the right side of the field equation.
    - **Matrix exponential**: for a square matrix $M$ the matrix
      $e^{Mx_4} = 1 + Mx_4 + \frac{1}{2}M^2x_4^2 + \dots$; the column
      $e^{Mx_4}\chi$ solves $\frac{d}{dx_4}\Phi = M\Phi$ with $\Phi(0) = \chi$. When
      $M^2 = k^2$ times the unit matrix, the series sums to
      $\cosh(kx_4) + \frac{\sinh(kx_4)}{k}M$.
    - **Oscillating / growing**: when $k^2 < 0$ the number $k$ is imaginary,
      $\cosh(kx_4)$ becomes a cosine and the solution oscillates; when $k^2 > 0$ it
      contains $e^{kx_4}$ and grows.
    - **Energy density** $\rho$, **pressure** $p$, **equation of state** $w = p/\rho$.
      Dust has $w = 0$, radiation $w = 1/3$, a cosmological constant $w = -1$; a
      value $w < -1$ is called *phantom*.
    - **Energy exchange**: the change of the energy density in time caused by work
      done by the inflating 3-space and the deflating extra times.
    - **Toy fluid (ILLUSTRATION)**: a source with assumed pressures $p_3 = w_3\rho$
      and $p_t = w_t\rho$, used only to show what the conservation identity does; it
      is not a solution of the field equations of this book.
    - **Runge-Kutta method (RK4)**: a step-by-step method that solves a differential
      equation numerically with four slope evaluations per step.
    - **Histogram**: a bar chart that counts how many numbers fall into each of a
      row of equal intervals.
    - **Krein (indefinite) form**: the form $\Phi^\dagger B\Phi$ built with the
      matrix $B$, which has eight eigenvalues $+1$ and eight eigenvalues $-1$; it can
      be positive or negative.
    """),
    md(r"""
    ## 4. The physical and mathematical situation

    **The field equation of a condensate.** In the author's metric the field
    equation of dirac16complex00 is
    $\sum_a\frac{1}{f_a}\gamma^{(a)}\partial_a\Phi + 3H\gamma^{(8)}\Phi = V\Phi$ with
    $V = m + \lambda S$. For a condensate every derivative except $\partial_4$ is
    zero, and $f_4 = 1$, so the equation is
    $\gamma^{(4)}\partial_4\Phi + 3H\gamma^{(8)}\Phi = V\Phi$. Multiplying by
    $-\gamma^{(4)}$ and using $(\gamma^{(4)})^2 = -1$ gives
    $\partial_4\Phi = M\Phi$ with $M = -V\gamma^{(4)} + 3H\gamma^{(4)}\gamma^{(8)}$.
    Neither $a_4$ nor $x_8$ appears: the same condensate solves the equation on
    every history $a_4(x_4)$, the deflating one included.

    **The exact solution** (Revision record, `Revision/theory/field-theory.json`,
    formula `exact_solutions`): $M^2 = k^2$ with $k^2 = 9H^2 - V^2$, and
    $M^TC + CM = 0$, so $S = \Phi^\dagger C\Phi$ does not change with $x_4$; then $V$
    is a constant and $\Phi = (\cosh(kx_4) + \frac{\sinh(kx_4)}{k}M)\chi$
    with $S = S_0 = \chi^\dagger C\chi$.

    **Its energy-momentum tensor** (formula `EMT_homogeneous_on_shell`): only $K_4$
    is nonzero, $K_4 = VS$ on shell, so $\rho = mS + U$ and
    $p_3 = p_t = p_8 = SU' - U$; for $U = \frac{\lambda}{2}S^2$:
    $\rho = mS + \frac{\lambda}{2}S^2$, $p = \frac{\lambda}{2}S^2$ and
    $w = \lambda S/(2m + \lambda S)$.

    **Energy exchange** (formula `energy_exchange`): conservation gives
    $d\rho/dx_4 = -3a_4'(p_3 - p_t)$. A condensate has $p_3 = p_t$, so its energy
    density is constant along every history.

    **What is not computed here.** The equation of state that an observer living in
    3-space would infer (after integrating over the hidden direction and the extra
    times), its time dependence and any comparison with supernova data are not part
    of the Revision record: they are OPEN. The $w$ of this notebook is the ratio
    $p/\rho$ of the 8-dimensional tensor. The condensate's off-diagonal entries,
    which are not zero in general, are not used here.
    """),
    md(r"""
    ## 5. The matrices C and B, and the sign of S

    The next cell reads the Revision fixture (the gammas $\gamma^{(x_1)}, \dots,
    \gamma^{(x_8)}$, the matrix $C$ and the matrix $B = -iC\gamma^{(4)}$) and defines
    the helper `recorded(path, name)`, which returns the verdict of a check in a
    Revision report. The record says that $C = \mathrm{diag}(-\sigma, \sigma)$ with
    an $8 \times 8$ matrix $\sigma$ that squares to 1 and has trace 0; so $C$ has
    eight eigenvalues $+1$ and eight $-1$, and $S_0 = \chi^\dagger C\chi$ can be
    positive or negative. The cell computes the eigenvalues of $C$ and the values of
    $S_0$ for 20000 random columns $\chi$ of length 1.
    """),
    code(r'''
    import numpy as np  # arrays of numbers, matrices, linear algebra

    fixture = json.loads(
        repository_file("Revision/algebra/gammas.json").read_text(encoding="utf-8"))
    gamma = [np.array(rows, dtype=float) for rows in fixture["gamma"]]  # x1, ..., x8
    C = np.array(fixture["C"], dtype=float)  # gamma^(x8) gamma^(x1) gamma^(x2) gamma^(x3)
    B = (np.array(fixture["B"]["re"], dtype=float)  # B = -i C gamma^(x4), stored as its
         + 1j * np.array(fixture["B"]["im"], dtype=float))  # real and imaginary parts
    I16 = np.eye(16)  # the 16 x 16 unit matrix
    g4, g8 = gamma[3], gamma[7]  # gamma^(x4) and gamma^(x8)


    def recorded(path, name):
        """The verdict (PASS or FAIL) of the check name in the Revision report path."""
        report_data = json.loads(repository_file(path).read_text(encoding="utf-8"))
        for item in report_data["checks"]:
            if item["name"] == name:
                return item["verdict"].upper()  # some reports write "pass"
        raise KeyError(f"{path} has no check {name}")


    ALGEBRA_PY = "Revision/algebra/reports/python-algebra.json"
    ALGEBRA_WL = "Revision/algebra/reports/wolfram-algebra.json"
    eigenvalues_C = np.linalg.eigvalsh(C)  # C is symmetric: eigvalsh, sorted ascending
    check(np.allclose(eigenvalues_C, [-1.0] * 8 + [1.0] * 8, atol=1e-12)
          and recorded(ALGEBRA_PY, "C_equals_notebook_sigma16") == "PASS"
          and recorded(ALGEBRA_WL, "sigma8_involution") == "PASS",
          "C has eight eigenvalues -1 and eight eigenvalues +1",
          record=f"{ALGEBRA_PY}, check C_equals_notebook_sigma16; {ALGEBRA_WL}, check "
                 "sigma8_involution")
    rng = np.random.default_rng(2026)  # a fixed seed: the same numbers in every run
    chis = rng.normal(size=(20000, 16)) + 1j * rng.normal(size=(20000, 16))
    chis /= np.linalg.norm(chis, axis=1)[:, None]  # every row now has length 1
    # S0 = chi^dagger C chi for every row at once (einsum sums over the indices i, j).
    S0_values = np.einsum("ni,ij,nj->n", chis.conj(), C, chis).real
    negative_share = float(np.mean(S0_values < 0))  # the fraction of negative S0
    check(S0_values.min() < 0 < S0_values.max() and np.abs(S0_values).max() <= 1 + 1e-12,
          "S0 = chi^dagger C chi takes both signs and lies between -1 and 1")
    report("fraction of the 20000 random chi with S0 < 0", f"{negative_share:.4f}")
    '''),
    md(r"""
    The next cell draws the histogram of the 20000 values of $S_0$. A condensate
    with $\lambda = 0$ has $\rho = mS_0$, so for $m > 0$ about half of these random
    condensates have a negative energy density.
    """),
    code(r'''
    fig, ax = plt.subplots()
    ax.hist(S0_values, bins=60, range=(-1.0, 1.0), color="tab:blue", edgecolor="white")
    ax.axvline(0.0, color="black", linewidth=1.0)
    ax.set_xlabel("$S_0 = \\chi^\\dagger C \\chi$ for a random $\\chi$ of length 1")
    ax.set_ylabel("number of the 20000 random $\\chi$")
    ax.set_title("The scalar $S = \\bar\\Phi\\Phi$ has no sign")
    save_figure(fig, "sign_of_s",
                "Histogram of $S_0 = \\chi^\\dagger C\\chi$ for 20000 random complex "
                "columns $\\chi$ of length 1 (fixed seed); horizontal axis $S_0$ (a pure "
                "number between $-1$ and $1$, because the eigenvalues of $C$ are $\\pm 1$), "
                "vertical axis the number of $\\chi$ in each of 60 intervals. The values "
                "are spread symmetrically about $0$: about half are negative. For a "
                "condensate with $\\lambda = 0$ the energy density is $\\rho = mS_0$, so "
                "its sign is the sign of $S_0$.")
    '''),
    md(r"""
    ## 6. The matrix M and its square

    The next cell defines the function `condensate_matrix(V, H)`, which returns
    $M = -V\gamma^{(4)} + 3H\gamma^{(4)}\gamma^{(8)}$ and $k^2 = 9H^2 - V^2$, and
    checks for several values of $V$ and $H$ the two facts of the record:
    $M^2 = k^2 \cdot 1$ and $M^TC + CM = 0$. The second fact makes $S$ constant:
    $\frac{d}{dx_4}(\Phi^\dagger C\Phi) = \Phi^\dagger(M^TC + CM)\Phi = 0$ (here $M$ is
    real, so $M^\dagger = M^T$).
    """),
    code(r'''
    def condensate_matrix(V, H):
        """M = -V gamma^(x4) + 3 H gamma^(x4) gamma^(x8) and k^2 = 9 H^2 - V^2."""
        return -V * g4 + 3 * H * g4 @ g8, 9 * H ** 2 - V ** 2


    THEORY_WL = "Revision/theory/reports/wolfram-field-theory.json"
    THEORY_PY = "Revision/theory/reports/python-field-theory.json"
    worst_square, worst_c = 0.0, 0.0  # the largest deviations found
    for V_test in (-2.0, -0.5, 0.0, 0.75, 1.5, 3.0):
        for H_test in (0.1, 0.25, 1.0):
            M_test, k2_test = condensate_matrix(V_test, H_test)
            worst_square = max(worst_square, np.abs(M_test @ M_test - k2_test * I16).max())
            worst_c = max(worst_c, np.abs(M_test.T @ C + C @ M_test).max())
    check(worst_square < 1e-12 and worst_c < 1e-12
          and recorded(THEORY_WL, "solution_matrix_square") == "PASS",
          "M^2 = (9 H^2 - V^2) times 1 and M^T C + C M = 0 for 18 pairs (V, H)",
          record=f"{THEORY_WL}, check solution_matrix_square")
    '''),
    md(r"""
    ## 7. Two exact condensates: one oscillates, one grows

    The next cell fixes $m = 1$ and $H = 0.25$ and a column $\chi$ with
    $S_0 = \chi^\dagger C\chi = 1$ (it draws random columns with a fixed seed until
    $S_0 > 0$ and divides by $\sqrt{S_0}$). With $\lambda = 0.5$ the effective mass is
    $V = 1.5 > 3H = 0.75$, so $k^2 = 9H^2 - V^2 < 0$: the condensate oscillates.
    With $\lambda = -0.5$ it is $V = 0.5 < 0.75$, so $k^2 > 0$: the condensate grows.
    The function `condensate(x4, chi, M, k2)` returns $\Phi(x_4)$ and its derivative
    $\Phi'(x_4) = k\sinh(kx_4)\chi + \cosh(kx_4)M\chi$; numpy computes $\cosh$ and
    $\sinh$ of the imaginary $k$ correctly when $k$ is stored as a complex number.
    At 401 times the cell checks the field equation
    $\gamma^{(4)}\Phi' + 3H\gamma^{(8)}\Phi = (m + \lambda S)\Phi$ and that $S$ stays
    equal to 1.
    """),
    code(r'''
    m, H = 1.0, 0.25  # the mass and the author's constant
    rng = np.random.default_rng(7)
    while True:  # draw until S0 > 0 (the first draw usually succeeds)
        chi = rng.normal(size=16) + 1j * rng.normal(size=16)
        S0 = (chi.conj() @ C @ chi).real
        if S0 > 0:
            break
    chi = chi / np.sqrt(S0)  # now chi^dagger C chi = 1


    def condensate(x4, chi_value, M, k2):
        """Phi(x4) and dPhi/dx4 of the exact condensate with Phi(0) = chi_value."""
        if k2 == 0.0:  # cosh(k x4) -> 1 and sinh(k x4)/k -> x4 when k -> 0
            return chi_value + x4 * M @ chi_value, M @ chi_value
        k = np.sqrt(complex(k2))  # k is imaginary when k2 < 0
        phi = np.cosh(k * x4) * chi_value + np.sinh(k * x4) / k * (M @ chi_value)
        dphi = k * np.sinh(k * x4) * chi_value + np.cosh(k * x4) * (M @ chi_value)
        return phi, dphi


    times = np.linspace(0.0, 12.0, 401)  # the times x4 at which the solution is tested
    EXAMPLES = {"oscillating": 0.5, "growing": -0.5}  # name -> lambda
    solutions = {}  # name -> (Phi at every time, S at every time)
    for name, lam in EXAMPLES.items():
        V = m + lam * 1.0  # S0 = 1
        M, k2 = condensate_matrix(V, H)
        phis, S_values, worst_residual = [], [], 0.0
        for x4 in times:
            phi, dphi = condensate(x4, chi, M, k2)
            S_now = (phi.conj() @ C @ phi).real
            residual = g4 @ dphi + 3 * H * g8 @ phi - (m + lam * S_now) * phi
            # The residual relative to the size of the solution at this time.  Rounding
            # errors grow with the solution (S is a difference of large numbers when
            # Phi grows), so the tolerance below is 1e-9, not 1e-15.
            worst_residual = max(worst_residual,
                                 np.abs(residual).max() / max(1.0, np.abs(phi).max()))
            phis.append(phi)
            S_values.append(S_now)
        solutions[name] = (np.array(phis), np.array(S_values))
        report(f"{name}: lambda = {lam}, V = m + lambda S0", f"{V:.4f}")
        report(f"{name}: k^2 = 9 H^2 - V^2", f"{k2:.4f}")
        check(worst_residual < 1e-9,
              f"{name}: the field equation holds at 401 times")
        check(np.abs(np.array(S_values) - 1.0).max() < 1e-9,
              f"{name}: S stays equal to S0 = 1 at 401 times")
    check(recorded(THEORY_WL, "exact_solution_nonlinear_homogeneous_C") == "PASS"
          and recorded(THEORY_PY, "exact_nonlinear_homogeneous_solution") == "PASS",
          "both condensates are the record's exact nonlinear homogeneous solution",
          record=f"{THEORY_WL}, check exact_solution_nonlinear_homogeneous_C; "
                 f"{THEORY_PY}, check exact_nonlinear_homogeneous_solution")
    '''),
    md(r"""
    The next cell draws the two condensates. Left: the real parts of three of the 16
    components of the oscillating condensate, and $S$. Right: the size
    $\Phi^\dagger\Phi$ of the growing condensate (logarithmic axis) and $S$. In both
    cases $S$ stays exactly 1, even where $\Phi^\dagger\Phi$ grows by a factor of
    more than 100000: the growth happens in directions in which the indefinite form
    $\Phi^\dagger C\Phi$ does not grow.
    """),
    code(r'''
    fig, (left, right) = plt.subplots(1, 2, figsize=(9.6, 3.9))
    phis, S_values = solutions["oscillating"]
    for component in (0, 5, 10):  # three of the 16 components (rows 1, 6 and 11)
        left.plot(times, phis[:, component].real,
                  label=f"Re $\\Phi_{{{component + 1}}}$")
    left.plot(times, S_values, "k--", label="$S = \\bar\\Phi\\Phi$")
    left.set_xlabel("time $x_4$")
    left.set_ylabel("value")
    left.set_ylim(-0.8, 1.35)  # room for the legend above the curves
    left.set_title("Oscillating: $\\lambda = 0.5$, $V = 1.5$")
    left.legend(fontsize=7, loc="upper center", ncol=4)
    phis, S_values = solutions["growing"]
    right.plot(times, np.einsum("ti,ti->t", phis.conj(), phis).real,
               label="$\\Phi^\\dagger\\Phi$")
    right.plot(times, S_values, "k--", label="$S = \\bar\\Phi\\Phi$")
    right.set_yscale("log")
    right.set_xlabel("time $x_4$")
    right.set_title("Growing: $\\lambda = -0.5$, $V = 0.5$")
    right.legend(fontsize=8)
    save_figure(fig, "condensate_solutions",
                "Two exact condensates of dirac16complex00 with $m = 1$, $H = 0.25$ and "
                "$S_0 = 1$, for $x_4$ from $0$ to $12$. Left, $\\lambda = 0.5$, so the "
                "effective mass $V = 1.5$ exceeds $3H = 0.75$: the real parts of the "
                "components 1, 6 and 11 of $\\Phi$ oscillate and $S$ (dashed) stays $1$. "
                "Right, $\\lambda = -0.5$, so $V = 0.5 < 3H$: the size "
                "$\\Phi^\\dagger\\Phi$ grows like $e^{2kx_4}$ with $k = 0.559$ "
                "(logarithmic axis) while $S$ (dashed) stays exactly $1$. All values "
                "are pure numbers.")
    '''),
    md(r"""
    ## 8. Energy density, pressures, kinetic and potential parts of the condensates

    For a condensate every kinetic term except $K_4$ vanishes, because every other
    derivative is zero. The next cell computes, at every tested time,
    $K_4 = \frac12(\bar\Phi\gamma^{(4)}\Phi' - \bar\Phi'\gamma^{(4)}\Phi)$ from the
    solution, the Lagrangian $L_0 = K_4 - mS - U$, the energy density
    $\rho = -T^{x_4}{}_{x_4} = K_4 - L_0$ and the pressures
    $p_\mu = T^\mu{}_\mu = L_0 - K_\mu = L_0$ for $\mu \neq x_4$, which are equal in
    all seven directions. It checks $K_4 = VS$, $\rho = mS + \frac{\lambda}{2}S^2$ and
    $p = \frac{\lambda}{2}S^2$, hence the kinetic and potential parts
    ($\rho_{\rm kin} = 0$, $p_{\rm kin} = K_4 = VS$, $p_{\rm pot} = -(mS + U)$), the trace
    $-\rho + 7p = -mS + 3\lambda S^2$, and that the $x_4$-$x_8$ component vanishes:
    $T^{x_4}{}_{x_8} = -\frac14(B_{48} - \cot z B_{84})$ with
    $B_{48} = 0$ (no $x_8$ derivative) and
    $B_{84} = \bar\Phi\gamma^{(8)}\Phi' - \bar\Phi'\gamma^{(8)}\Phi$, which must be 0.
    """),
    code(r'''
    def homogeneous_tensor(phi, dphi, lam):
        """K4, rho, p and B84 of a condensate at one time."""
        S = (phi.conj() @ C @ phi).real
        U = lam / 2 * S ** 2
        K4 = 0.5 * (phi.conj() @ C @ g4 @ dphi - dphi.conj() @ C @ g4 @ phi)
        L0 = K4.real - m * S - U  # the other seven kinetic terms are zero
        B84 = phi.conj() @ C @ g8 @ dphi - dphi.conj() @ C @ g8 @ phi
        return S, U, K4, K4.real - L0, L0, B84  # rho = K4 - L0, p = L0


    values = {}  # name -> (rho, p) of the condensate
    for name, lam in EXAMPLES.items():
        V = m + lam * 1.0
        M, k2 = condensate_matrix(V, H)
        rhos, ps, worst = [], [], 0.0
        for x4 in times:
            phi, dphi = condensate(x4, chi, M, k2)
            S, U, K4, rho, p, B84 = homogeneous_tensor(phi, dphi, lam)
            size = max(1.0, (phi.conj() @ phi).real)  # for relative tolerances
            worst = max(worst, abs(K4.imag) / size, abs(K4.real - V * S) / size,
                        abs(B84) / size)
            rhos.append(rho)
            ps.append(p)
        rhos, ps = np.array(rhos), np.array(ps)
        values[name] = (rhos.mean(), ps.mean())
        check(worst < 1e-12, f"{name}: K4 is real, K4 = V S, and B84 = 0 (T^x4_x8 = 0)")
        check(np.abs(rhos - (m + lam / 2)).max() < 1e-9
              and np.abs(ps - lam / 2).max() < 1e-9,
              f"{name}: rho = m S + lambda S^2/2 and p = lambda S^2/2 at 401 times")
        check(abs(-values[name][0] + 7 * values[name][1] - (-m + 3 * lam)) < 1e-9,
              f"{name}: trace -rho + 7 p = -m S + 3 lambda S^2")
        report(f"{name}: rho", f"{values[name][0]:.6f}")
        report(f"{name}: p (all seven directions)", f"{values[name][1]:.6f}")
        report(f"{name}: w = p/rho", f"{values[name][1] / values[name][0]:.6f}")
    check(recorded(THEORY_PY, "commuting_homogeneous_on_shell_rho_p") == "PASS"
          and recorded(THEORY_PY, "commuting_T_x4x8_homogeneous") == "PASS"
          and recorded(THEORY_PY, "commuting_trace_on_shell") == "PASS",
          "these are the record's homogeneous values and its vanishing x4-x8 component",
          record=f"{THEORY_PY}, checks commuting_homogeneous_on_shell_rho_p, "
                 "commuting_T_x4x8_homogeneous and commuting_trace_on_shell")
    '''),
    md(r"""
    ## 9. Energy density and pressure against S

    The next cell draws, for $m = 1$ and $\lambda = 0.5$, the energy density
    $\rho = mS + \frac{\lambda}{2}S^2$ and the pressure $p = \frac{\lambda}{2}S^2$ of
    a condensate against $S$, with the two parts of the pressure: the kinetic part
    $p_{\rm kin} = VS = (m + \lambda S)S$ and the potential part
    $p_{\rm pot} = -(mS + U)$. The energy density is zero at $S = 0$ and at
    $S = -2m/\lambda = -4$ and negative between them. The cell also checks that the
    two parts add up to $p$ at every drawn $S$.
    """),
    code(r'''
    lam = 0.5
    S_axis = np.linspace(-6.0, 2.0, 401)
    rho_axis = m * S_axis + lam / 2 * S_axis ** 2  # rho = m S + U
    p_axis = lam / 2 * S_axis ** 2  # p = S U' - U
    p_kin = (m + lam * S_axis) * S_axis  # V S
    p_pot = -(m * S_axis + lam / 2 * S_axis ** 2)  # -(m S + U)
    check(np.abs(p_kin + p_pot - p_axis).max() < 1e-12,
          "p = p_kin + p_pot = V S - (m S + U) at every drawn S")
    fig, ax = plt.subplots()
    ax.plot(S_axis, rho_axis, label="energy density $\\rho = mS + \\lambda S^2/2$")
    ax.plot(S_axis, p_axis, label="pressure $p = \\lambda S^2/2$")
    ax.plot(S_axis, p_kin, "--", label="kinetic part of $p$: $(m + \\lambda S)S$")
    ax.plot(S_axis, p_pot, ":", label="potential part of $p$: $-(mS + U)$")
    ax.plot([0.0, -2 * m / lam], [0.0, 0.0], "ko", label="$\\rho = 0$")
    ax.axhline(0.0, color="black", linewidth=0.8)
    ax.set_xlabel("$S = \\bar\\Phi\\Phi$")
    ax.set_ylabel("energy per unit volume")
    ax.set_title("Condensate: $\\rho$ and $p$ against $S$ ($m = 1$, $\\lambda = 0.5$)")
    ax.legend(fontsize=8)
    save_figure(fig, "energy_and_pressure",
                "Energy density $\\rho = mS + \\lambda S^2/2$ (solid), pressure "
                "$p = \\lambda S^2/2$ (solid) and the two parts of the pressure, the "
                "kinetic part $(m + \\lambda S)S$ (dashed) and the potential part "
                "$-(mS + U)$ (dotted), of a condensate of dirac16complex00 with $m = 1$, "
                "$\\lambda = 0.5$, against $S$ from $-6$ to $2$; vertical axis in units "
                "of energy per unit volume. The energy density vanishes at $S = 0$ and "
                "$S = -2m/\\lambda = -4$ (black dots) and is negative between them; the "
                "pressure is the same in all seven directions.")
    '''),
    md(r"""
    ## 10. The equation of state of actual solutions

    The ratio $w = p/\rho$ depends on $m$, $\lambda$ and $S$ only through
    $x = \lambda S/m$: $w = \frac{\lambda S^2/2}{mS + \lambda S^2/2} = \frac{x}{2 + x}$.
    The next cell does not use this formula to compute $w$. For twelve values of $x$
    it builds the exact condensate with $m = 1$, $S_0 = 1$ and $\lambda = x$, takes
    $\Phi$ and $\Phi'$ at the time $x_4 = 1.3$, computes $\rho$ and $p$ from them as
    in section 8, and only then compares $p/\rho$ with $x/(2 + x)$. It also finds the
    special values: $w = 0$ at $x = 0$ (dust-like), $w = -1$ at $x = -1$, where the
    effective mass $V = m + \lambda S$ is zero, $w < -1$ (phantom) for
    $-2 < x < -1$, and $w \to 1$ as $x$ grows. At $x = -2$ the energy density is zero
    and $w$ is not defined.
    """),
    code(r'''
    x_measured = np.array([-3.5, -3.0, -2.5, -1.5, -1.0, -0.5, 0.0, 0.5, 1.0, 2.0, 3.0,
                           4.0])  # values of x = lambda S/m (here lambda = x)
    w_measured = []
    for x_value in x_measured:
        V = m + x_value * 1.0  # lambda = x_value, S0 = 1
        M, k2 = condensate_matrix(V, H)
        phi, dphi = condensate(1.3, chi, M, k2)
        S, U, K4, rho, p, B84 = homogeneous_tensor(phi, dphi, x_value)
        w_measured.append(p / rho)
    w_measured = np.array(w_measured)
    w_formula = x_measured / (2 + x_measured)
    check(np.abs(w_measured - w_formula).max() < 1e-9,
          "w = p/rho of 12 exact condensates equals x/(2 + x), x = lambda S/m")
    at_minus_one = w_measured[list(x_measured).index(-1.0)]
    check(abs(at_minus_one + 1.0) < 1e-12,
          "w = -1 exactly where the effective mass m + lambda S vanishes (x = -1)")
    for x_value, w_value in zip(x_measured, w_measured):
        say(f"x = lambda S/m = {x_value:5.1f}:  w = p/rho = {w_value: .6f}")
    '''),
    md(r"""
    The next cell draws $w = x/(2 + x)$ as a curve, the twelve measured values as
    points, and marks the special lines.
    """),
    code(r'''
    fig, ax = plt.subplots()
    for piece in (np.linspace(-6.0, -2.05, 300), np.linspace(-1.95, 6.0, 500)):
        ax.plot(piece, piece / (2 + piece), color="tab:blue")  # two branches
    ax.plot(x_measured, w_measured, "o", color="tab:red",
            label="measured on exact condensates")
    ax.axvline(-2.0, color="gray", linestyle=":", label="$\\rho = 0$ ($x = -2$)")
    ax.axhline(-1.0, color="tab:green", linestyle="--", label="$w = -1$")
    ax.axhline(0.0, color="black", linewidth=0.8)
    ax.axhspan(-6.0, -1.0, xmin=0.0, xmax=1.0, color="tab:green", alpha=0.08)
    ax.set_ylim(-6.0, 6.0)
    ax.set_xlabel("$x = \\lambda S / m$")
    ax.set_ylabel("$w = p/\\rho$")
    ax.set_title("Equation of state of a condensate: $w = x/(2 + x)$")
    ax.legend(fontsize=8, loc="upper right")
    save_figure(fig, "equation_of_state",
                "Equation of state $w = p/\\rho$ of a condensate of dirac16complex00 "
                "against $x = \\lambda S/m$ (pure numbers): the curve is "
                "$w = x/(2 + x)$, the red points are $p/\\rho$ computed from twelve exact "
                "solutions ($m = 1$, $H = 0.25$, $S_0 = 1$, $\\lambda = x$) and lie on "
                "it. $w = 0$ at $x = 0$, $w = -1$ (dashed) at $x = -1$, where the "
                "effective mass $m + \\lambda S$ vanishes, $w < -1$ (shaded) for "
                "$-2 < x < -1$, $w$ is undefined at $x = -2$ (dotted) where $\\rho = 0$, "
                "and $w$ approaches $1$ for large $x$. This is the 8-dimensional "
                "ratio, not the equation of state a 3-space observer would infer.")
    '''),
    md(r"""
    ## 11. Where condensates oscillate and where they grow

    A condensate oscillates when $k^2 = 9H^2 - V^2 < 0$, that is when
    $|1 + x| > 3H/|m|$ with $x = \lambda S/m$, and grows when $|1 + x| < 3H/|m|$
    (because $V = m(1 + x)$). The equation of state depends on $x$ alone, so on the
    map of the plane $(x, 3H/|m|)$ every line of constant $w$ is vertical. The next
    cell draws the map, the lines $w = -1$, $0$, $1/3$ and the two condensates of
    section 7, and checks that each of them lies in the region the map gives.
    """),
    code(r'''
    x_grid = np.linspace(-4.0, 3.0, 701)  # x = lambda S/m
    h_grid = np.linspace(0.0, 3.0, 301)  # h = 3 H/|m|
    X, Hgrid = np.meshgrid(x_grid, h_grid)  # every pair (x, h) of the two grids
    growing_region = (np.abs(1 + X) < Hgrid).astype(float)  # 1 where k^2 > 0
    fig, ax = plt.subplots()
    ax.contourf(X, Hgrid, growing_region, levels=[-0.5, 0.5, 1.5],
                colors=["#dbe9f6", "#f6d5d5"])
    for label, x_line in (("$w = -1$", -1.0), ("$w = 0$", 0.0), ("$w = 1/3$", 1.0)):
        ax.axvline(x_line, color="black", linestyle="--", linewidth=0.8)
        ax.text(x_line + 0.05, 2.8, label, fontsize=8)
    for name, lam_value in EXAMPLES.items():
        ax.plot([lam_value * 1.0 / m], [3 * H / abs(m)], "ko")
        ax.text(lam_value / m + 0.08, 3 * H / abs(m) - 0.15, name, fontsize=8)
    ax.text(-3.8, 0.3, "oscillating ($k^2 < 0$)", fontsize=9)
    ax.text(-2.9, 2.3, "growing\n($k^2 > 0$)", fontsize=9)
    ax.set_xlabel("$x = \\lambda S / m$")
    ax.set_ylabel("$3H/|m|$")
    ax.set_title("Condensates: oscillating (blue) or growing (red)")
    ax.grid(False)
    save_figure(fig, "regime_map",
                "Map of the condensates of dirac16complex00 in the plane of "
                "$x = \\lambda S/m$ (horizontal) and $3H/|m|$ (vertical), pure numbers. "
                "In the red wedge $|1 + x| < 3H/|m|$ the number $k^2 = 9H^2 - "
                "(m + \\lambda S)^2$ is positive and the condensate grows; in the blue "
                "region it oscillates. The dashed vertical lines are the equations of "
                "state $w = -1$ ($x = -1$), $w = 0$ and $w = 1/3$ ($x = 1$); $w$ "
                "depends on $x$ only. The black dots are the two condensates of the "
                "second figure ($H = 0.25$, $m = 1$). Every condensate with $w = -1$ "
                "lies in the growing wedge.")
    for name, lam_value in EXAMPLES.items():
        grows = abs(1 + lam_value / m) < 3 * H / abs(m)
        check(grows == (name == "growing"),
              f"the {name} condensate lies in the {name} region of the map")
    '''),
    md(r"""
    ## 12. Energy exchange between 3-space and the extra times

    Conservation says $d\rho/dx_4 = -3a_4'(p_3 - p_t)$. A condensate has $p_3 = p_t$,
    so along every history its energy density stays constant; the next cell confirms
    this on the oscillating condensate along the deflating history $a_4 = AHx_4$
    ($A = 1$): the solution does not depend on $a_4$, and $\rho$ is the same at all
    401 times.

    Then, as an ILLUSTRATION only, it takes toy fluids with assumed pressures
    $p_3 = w_3\rho$ and $p_t = w_t\rho$ (constant $w_3$, $w_t$; these are not
    solutions of the field equations of this book). The identity becomes
    $d\rho/dx_4 = -3AH(w_3 - w_t)\rho$, whose solution is
    $\rho = \rho_0 e^{-3AH(w_3 - w_t)x_4}$. The cell solves it numerically with the
    Runge-Kutta method (RK4, step $0.05$) for five values of $\Delta w = w_3 - w_t$,
    compares with the exact solution (and checks that halving the step divides the
    error by about $2^4 = 16$, as it must for a fourth-order method), and checks that
    reversing the history ($A \to -A$: the extra times inflate, 3-space deflates)
    reverses the flow.
    """),
    code(r'''
    A = 1.0  # the deflating history a4 = A H x4
    M, k2 = condensate_matrix(m + 0.5 * 1.0, H)  # the oscillating condensate, S0 = 1
    # rho at every time; homogeneous_tensor returns (S, U, K4, rho, p, B84): index 3.
    # The condensate does not contain a4, so these are its values on this history too.
    rho_at_times = np.array([homogeneous_tensor(*condensate(x4, chi, M, k2), 0.5)[3]
                             for x4 in times])
    check(np.abs(rho_at_times - rho_at_times[0]).max() < 1e-9,
          "the condensate has p3 = p_t, so its rho is constant along the history")


    def rk4(rate, y0, step, count):
        """Solve dy/dx = rate(y) from y(0) = y0 with count Runge-Kutta steps."""
        y, path = y0, [y0]
        for _ in range(count):
            s1 = rate(y)
            s2 = rate(y + step / 2 * s1)
            s3 = rate(y + step / 2 * s2)
            s4 = rate(y + step * s3)
            y = y + step / 6 * (s1 + 2 * s2 + 2 * s3 + s4)
            path.append(y)
        return np.array(path)


    STEP, COUNT = 0.05, 160  # x4 from 0 to 8
    toy_times = STEP * np.arange(COUNT + 1)
    DELTAS = (-2 / 3, -1 / 3, 0.0, 1 / 3, 2 / 3)  # Delta w = w3 - w_t
    toy = {}  # Delta w -> rho(x4)/rho0 along A = +1
    errors = {STEP: 0.0, STEP / 2: 0.0}  # the largest relative error for two steps
    for delta in DELTAS:
        for step in errors:
            count = round(8.0 / step)  # the number of steps from x4 = 0 to 8
            path = rk4(lambda r, d=delta: -3 * A * H * d * r, 1.0, step, count)
            exact = np.exp(-3 * A * H * delta * step * np.arange(count + 1))
            errors[step] = max(errors[step], np.abs(path / exact - 1).max())
            if step == STEP:
                toy[delta] = path
    check(errors[STEP] < 1e-7,
          "RK4 (step 0.05) reproduces rho0 exp(-3 A H Delta w x4) for 5 toy fluids")
    ratio = errors[STEP] / errors[STEP / 2]  # RK4: half the step, 1/16 of the error
    check(14 < ratio < 18, "halving the RK4 step divides the error by about 2^4 = 16")
    report("largest relative RK4 error, step 0.05", f"{errors[STEP]:.2e}")
    report("error ratio of the steps 0.05 and 0.025", f"{ratio:.2f}")
    reversed_path = rk4(lambda r: -3 * (-A) * H * (1 / 3) * r, 1.0, STEP, COUNT)
    check(np.abs(reversed_path * toy[1 / 3] - 1).max() < 1e-8,
          "A -> -A reverses the energy flow (the product of the two paths is 1)")
    report("toy fluid Delta w = 1/3: rho(8)/rho(0) along A = 1", f"{toy[1 / 3][-1]:.6f}")
    '''),
    md(r"""
    The next cell draws the energy densities of the toy fluids and of the condensate
    (left), and for the toy fluid with $(w_3, w_t) = (1/3, 0)$ the two contributions
    to $d\rho/dx_4$ (right): the work of the inflating 3-space, $-3a_4'p_3$, and the
    work of the deflating extra times, $+3a_4'p_t$. For the condensate the two would
    be equal and opposite at every time.
    """),
    code(r'''
    fig, (left, right) = plt.subplots(1, 2, figsize=(9.6, 3.9))
    fig.subplots_adjust(wspace=0.35)  # more room between the two panels
    for delta in DELTAS:
        left.plot(toy_times, toy[delta], label=f"toy, $\\Delta w = {delta:+.2f}$")
    left.plot(times[times <= 8.0], rho_at_times[times <= 8.0] / rho_at_times[0], "k:",
              linewidth=2.0, label="condensate ($p_3 = p_t$)")
    left.set_yscale("log")
    left.set_xlabel("time $x_4$")
    left.set_ylabel("$\\rho(x_4) / \\rho(0)$")
    left.set_title("Energy density along $a_4 = AHx_4$ ($A = 1$)")
    left.legend(fontsize=7)
    rho_toy = toy[1 / 3]  # w3 = 1/3, w_t = 0
    work_space = -3 * A * H * (1 / 3) * rho_toy  # -3 a4' p3
    work_extra = 3 * A * H * 0.0 * rho_toy  # +3 a4' p_t with p_t = 0
    right.plot(toy_times, work_space, label="3-space: $-3a_4' p_3$")
    right.plot(toy_times, work_extra, "--", label="extra times: $+3a_4' p_t$")
    right.plot(toy_times, np.gradient(rho_toy, toy_times), ":", color="black",
               label="$d\\rho/dx_4$ (finite differences)")
    right.set_xlabel("time $x_4$")
    right.set_ylabel("rate of change of $\\rho$")
    right.set_title("Toy fluid $(w_3, w_t) = (1/3, 0)$")
    right.legend(fontsize=7)
    save_figure(fig, "energy_exchange",
                "Energy exchange along the deflating history $a_4 = AHx_4$, $A = 1$, "
                "$H = 0.25$, for $x_4$ from $0$ to $8$. Left, logarithmic axis: "
                "$\\rho(x_4)/\\rho(0)$ of five toy fluids with assumed pressures "
                "$p_3 = w_3\\rho$, $p_t = w_t\\rho$ and $\\Delta w = w_3 - w_t$ from "
                "$-2/3$ to $2/3$ (an illustration, not solutions of the field "
                "equations), solved with RK4: $\\rho$ falls when $p_3 > p_t$ and rises "
                "when $p_3 < p_t$; the exact condensate (dotted) has $p_3 = p_t$ and "
                "constant $\\rho$. Right: for the toy fluid $(1/3, 0)$ the work term of "
                "3-space $-3a_4'p_3$, the work term of the extra times $+3a_4'p_t$ "
                "(zero here) and $d\\rho/dx_4$, which is their sum.")
    check(np.abs(np.gradient(rho_toy, toy_times) - (work_space + work_extra))[2:-2].max()
          < 1e-3, "d rho/dx4 equals the sum of the two work terms on the drawn path")
    '''),
    md(r"""
    ## 13. The energy of the commuting field has no lower bound

    The record proves that the classical energy of dirac16complex00 is unbounded
    below already for $U = 0$, with an exact example: in flat 4+4 space (all
    $f_a = 1$, no spin connection) with $m = 2$ and the momentum
    $(k_1, k_2, k_3, k_8) = (1, 2, 0, 4)$, the plane waves
    $\Phi = u e^{i(k_1x_1 + k_2x_2 + k_8x_8 - Ex_4)}$ with $E = 5$ solve the field
    equation when $u$ lies in the 8-dimensional eigenspace of the matrix
    $h = m\beta + \sum_a k_a\alpha^a$ ($\beta = -i\gamma^{(4)}$,
    $\alpha^a = -\gamma^{(4)}\gamma^{(a)}$) with eigenvalue 5, and the energy density
    is $\rho = E u^\dagger Bu$. On that eigenspace the form $u^\dagger Bu$ has four
    positive and four negative directions (Krein inertia (4,4)). The next cell
    builds $h$, finds the eigenspace, checks the field equation, computes $\rho$
    from the kinetic terms for the eigenvectors with $Bu = -u$ and $Bu = +u$
    ($\rho = -5$ and $+5$), and computes $\rho$ for 5000 random unit vectors $u$ of
    the eigenspace.
    """),
    code(r'''
    m_flat, E_flat = 2.0, 5.0
    momentum = {0: 1.0, 1: 2.0, 2: 0.0, 7: 4.0}  # k1, k2, k3, k8 (x5, x6, x7: zero)
    beta = -1j * g4
    h = m_flat * beta + sum(k_a * (-g4 @ gamma[a]) for a, k_a in momentum.items())
    check(np.abs(h - h.conj().T).max() < 1e-12 and np.abs(h @ h - 25 * I16).max() < 1e-12
          and np.abs(B @ h - h @ B).max() < 1e-12,
          "h is Hermitian, h^2 = 25, and h commutes with B")
    energies, vectors = np.linalg.eigh(h)  # eigenvalues in ascending order
    U5 = vectors[:, energies > 0]  # the eight columns with eigenvalue +5
    form = U5.conj().T @ B @ U5  # u^dagger B u on the eigenspace, as an 8 x 8 matrix
    inertia, directions = np.linalg.eigh(form)
    PAIRING = "Revision/pairing/reports/python-pairing.json"
    check(np.allclose(energies, [-5.0] * 8 + [5.0] * 8, atol=1e-12)
          and np.allclose(inertia, [-1.0] * 4 + [1.0] * 4, atol=1e-12)
          and recorded(PAIRING, "Q.one_particle_Krein_inertia_proof") == "PASS",
          "E = +-5 (eight each); u^dagger B u has inertia (4,4) on the E = 5 space",
          record=f"{PAIRING}, check Q.one_particle_Krein_inertia_proof (every real "
                 "frequency)")


    def flat_energy_density(u):
        """rho = -sum over a != x4 of K_a + m S for the plane wave u e^(i(k.x - E x4))."""
        S = (u.conj() @ C @ u).real
        kinetic = 0.0
        for a, k_a in momentum.items():  # d_a Phi = i k_a Phi
            d_u = 1j * k_a * u
            kinetic += 0.5 * (u.conj() @ C @ gamma[a] @ d_u - d_u.conj() @ C @ gamma[a] @ u)
        return (-kinetic + m_flat * S).real


    rho_pair = []
    # column 0 of directions has the eigenvalue -1 of the form, column 7 the value +1
    for column, b_value in ((0, -1.0), (7, 1.0)):
        u = U5 @ directions[:, column]  # a unit vector of the eigenspace, B u = b_value u
        d4_u = -1j * E_flat * u  # d4 Phi = -i E Phi
        field = (g4 @ d4_u + sum(gamma[a] @ (1j * k_a * u) for a, k_a in momentum.items())
                 - m_flat * u)  # sum_a gamma^(a) d_a Phi - m Phi
        check(np.abs(field).max() < 1e-12 and np.abs(B @ u - b_value * u).max() < 1e-12,
              f"the plane wave with B u = {b_value:+.0f} u solves the field equation")
        rho_pair.append(flat_energy_density(u))
    SCOPE_PY = "Revision/theory/reports/python-scope.json"
    SCOPE_WL = "Revision/theory/reports/wolfram-scope.json"
    check(abs(rho_pair[0] + 5.0) < 1e-12 and abs(rho_pair[1] - 5.0) < 1e-12
          and recorded(SCOPE_PY, "commuting_field_energy_unbounded_below") == "PASS"
          and recorded(SCOPE_WL, "commuting_field_energy_unbounded_below") == "PASS",
          "rho = -5 for B u = -u and rho = +5 for B u = +u (|u| = 1)",
          record=f"{SCOPE_PY} and {SCOPE_WL}, check commuting_field_energy_unbounded_below")
    samples = rng.normal(size=(5000, 8)) + 1j * rng.normal(size=(5000, 8))
    samples /= np.linalg.norm(samples, axis=1)[:, None]
    us = samples @ U5.T  # 5000 random unit vectors of the eigenspace
    charges = np.einsum("ni,ij,nj->n", us.conj(), B, us).real  # u^dagger B u
    rho_samples = np.array([flat_energy_density(u) for u in us])
    check(np.abs(rho_samples - E_flat * charges).max() < 1e-12
          and rho_samples.min() < 0 < rho_samples.max(),
          "rho = E u^dagger B u for all 5000 random u of the eigenspace; both signs")
    report("smallest and largest rho of the 5000 samples",
           f"{rho_samples.min():.4f} and {rho_samples.max():.4f}")
    '''),
    md(r"""
    The next cell draws the histogram of the 5000 energy densities.
    """),
    code(r'''
    fig, ax = plt.subplots()
    ax.hist(rho_samples, bins=50, range=(-5.0, 5.0), color="tab:purple", edgecolor="white")
    ax.axvline(0.0, color="black", linewidth=1.0)
    ax.set_xlabel("energy density $\\rho = E\\,u^\\dagger B u$ of the plane wave")
    ax.set_ylabel("number of the 5000 random $u$")
    ax.set_title("Waves of positive frequency $E = 5$: $\\rho$ has both signs")
    save_figure(fig, "energy_sign",
                "Histogram of the energy density $\\rho = -\\sum_{a \\neq x_4} K_a + mS$ "
                "of 5000 plane waves $u\\,e^{i(k \\cdot x - Ex_4)}$ of dirac16complex00 "
                "in flat 4+4 space with $m = 2$, $(k_1, k_2, k_3, k_8) = (1, 2, 0, 4)$ "
                "and positive frequency $E = 5$, for random unit vectors $u$ of the "
                "8-dimensional solution space; horizontal axis $\\rho$ in units of "
                "energy per unit volume, vertical axis the count in each of 50 "
                "intervals. Every value equals $E\\,u^\\dagger Bu$ and they fill the "
                "whole interval from $-5$ to $5$: positive frequency does not mean "
                "positive energy for this commuting field.")
    '''),
    md(r"""
    ## 14. The last check

    The last cell checks that the seven figures are saved with their captions and
    prints the number of checks that passed.
    """),
    code(r'''
    captions = json.loads(output_file(CAPTION_FILE).read_text(encoding="utf-8"))
    expected_files = ["09b_1_sign_of_s.png", "09b_2_condensate_solutions.png",
                      "09b_3_energy_and_pressure.png", "09b_4_equation_of_state.png",
                      "09b_5_regime_map.png", "09b_6_energy_exchange.png",
                      "09b_7_energy_sign.png"]
    check(sorted(captions) == expected_files and all(
        output_file(f"{FIGURE_FOLDER}/{name}").is_file() for name in expected_files),
        "the seven figures of this notebook are saved and captioned")
    all_checks_passed()
    '''),
    md(r"""
    ## 15. What this notebook showed

    - The exact condensates of dirac16complex00,
      $\Phi = (\cosh(kx_4) + \frac{\sinh(kx_4)}{k}M)\chi$ with
      $k^2 = 9H^2 - (m + \lambda S_0)^2$, solve the field equation on every history
      $a_4$; $S$ stays equal to $S_0$, whether the condensate oscillates
      ($k^2 < 0$) or grows ($k^2 > 0$).
    - Their energy density and pressure are $\rho = mS + \frac{\lambda}{2}S^2$ and
      $p = \frac{\lambda}{2}S^2$, the same in all seven directions; the kinetic
      energy density is zero, the kinetic pressure is $(m + \lambda S)S$; the
      $x_4$-$x_8$ component vanishes (record values, computed here anew from the
      solutions).
    - The equation of state is $w = x/(2 + x)$ with $x = \lambda S/m$, measured on
      twelve exact solutions; $w = -1$ exactly where the effective mass vanishes, and
      such condensates always grow. These $w$ are constant in time and are
      8-dimensional ratios; what a 3-space observer would infer is OPEN in the
      Revision record.
    - Because $p_3 = p_t$, a condensate exchanges no energy between 3-space and the
      extra times; toy fluids with $p_3 \neq p_t$ (an illustration) show the exchange
      $d\rho/dx_4 = -3a_4'(p_3 - p_t)$ and its reversal under $A \to -A$.
    - $S$ and the energy density of the commuting field have no sign: half of all
      random condensates with $\lambda = 0$ have $\rho < 0$, and positive-frequency
      plane waves have $\rho$ anywhere between $-E$ and $E$ (record:
      `commuting_field_energy_unbounded_below`).
    """),
]

if __name__ == "__main__":
    raise SystemExit(run_builder(__file__))
