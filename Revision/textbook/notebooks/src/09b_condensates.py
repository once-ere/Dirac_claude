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

The metric is the corrected metric of 2026-10-16 (version 2; Revision/SPEC.md section 1).
The exact homogeneous solution, its energy density and pressure, the vanishing of its
x4-x0 component and the unbounded energy of the commuting field are statements of the
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
        "It builds the homogeneous solutions (condensates) Phi = e^(a4/2) b4^(-1) chi of "
        "the commuting field dirac16complex00 with the potential U = (lambda/2) S^2 along "
        "the history a4 = A H x4, b4 = b4(0) e^(beta A H x4) of the corrected metric of "
        "2026-10-16, from the Revision gamma matrices, checks that e^(-a4) b4^2 S stays "
        "constant and that the energy density and pressure are rho = m S + U and "
        "p = S U' - U in every direction, measures the equation of state w = p/rho of "
        "actual solutions against lambda S/m, maps where condensates oscillate or grow "
        "and how the deflating block moves them into the growing region, shows with "
        "assumed toy fluids how 3-space and the block exchange energy and how the "
        "7-volume dilutes it (a condensate is only diluted), and shows that the energy "
        "of the commuting field has no lower bound, in seven teaching plots."
    ),
    "records": [
        ["Revision/algebra/gammas.json",
         "the author's gamma matrices, the matrices C and B (the fixture)"],
        ["Revision/algebra/reports/python-algebra.json",
         "C as diag(-sigma, sigma) and the signature of B"],
        ["Revision/algebra/reports/wolfram-algebra.json",
         "sigma squares to one and has trace zero"],
        ["Revision/theory/field-theory.json",
         "the formulas of the exact solutions, of the homogeneous energy density and "
         "pressure and of the energy exchange"],
        ["Revision/theory/reports/wolfram-field-theory.json",
         "the solution matrix, the exact nonlinear homogeneous solution, the energy "
         "exchange"],
        ["Revision/theory/reports/python-field-theory.json",
         "the same solution, the homogeneous energy density and pressure, the x4-x0 "
         "component, the trace"],
        ["Revision/field_equations_a4/reports/wolfram-a4-report.json",
         "the condensate equation and the square of its matrix"],
        ["Revision/theory/reports/python-scope.json",
         "the energy of the commuting field is unbounded below; the growing "
         "x0-independent modes of the good sector"],
        ["Revision/theory/reports/wolfram-scope.json",
         "the same statements, verified with the Wolfram Language"],
        ["Revision/pairing/reports/python-pairing.json",
         "the Krein inertia (4,4) of every real-frequency eigenspace"],
    ],
    "packages": ["numpy", "matplotlib"],
    "needs_rust": [],
    "expected_seconds": 20,
    "timeout_seconds": 300,
    "files_written": ["Revision/textbook/figures/09b.captions.json"] + FIGURES,
    "final_lines": [
        "PASS the seven figures of this notebook are saved and captioned",
        "ALL 35 CHECKS PASSED (notebook 09b)",
    ],
    "troubleshooting": [
        ["\"KeyError\" with the words \"has no check\"",
         "the notebook asks a Revision report for the verdict of one of its checks, and "
         "the report in your copy of the repository does not contain that check: your "
         "copy is older or newer than the notebook. Run `git pull` in the repository "
         "folder, then run the notebook again."],
    ],
}

CELLS = [
    md(r"""
    ## 1. What this notebook computes

    A *condensate* is a configuration of the field that is the same at every place:
    it depends on the time $x_4$ only. This notebook builds the condensates of the
    commuting field dirac16complex00 with the potential $U(S) = \frac{\lambda}{2}S^2$
    along the history $a_4 = AHx_4$, $b_4 = b_4(0)e^{\beta AHx_4}$ of the corrected
    metric of 2026-10-16 and studies their energy-momentum tensor. It

    - shows that the number $S = \bar\Phi\Phi$ can have either sign (a histogram);
    - builds the condensates $\Phi = e^{a_4/2}b_4^{-1}\chi$ of the Revision record, in
      which the column $\chi$ solves a linear system with the effective mass
      $m + \lambda S$ and the gravitational coefficient
      $c_g = \frac32He^{a_4}b_4^{-1/2}$; checks the field equation and that
      $e^{-a_4}b_4^2S$ stays constant (so $S$ is diluted by the growing 7-volume),
      for one condensate that oscillates first and grows later and one that grows,
      oscillates and grows again;
    - computes from the solution the energy density $\rho$ and the pressure $p$ and
      checks the record's values $\rho = mS + U$ and $p = SU' - U$, the same in all
      seven directions, and the vanishing of the $x_4$-$x_0$ component;
    - measures the equation of state $w = p/\rho$ of actual solutions and compares it
      with $w = \lambda S/(2m + \lambda S)$; finds where $w = -1$;
    - maps where condensates oscillate and where they grow, and how the dilution and
      the deflating block move a condensate on that map until it grows;
    - shows with toy fluids (an ILLUSTRATION, not solutions of the field equations)
      how 3-space and the block of the hidden direction and the extra times exchange
      energy when $p_3 \neq p_t$ and how the growing 7-volume dilutes it, and that a
      condensate, with $p_3 = p_t = p_0$, is only diluted;
    - shows that the energy of the commuting field has no lower bound;
    - draws seven teaching plots.
    """),
    md(r"""
    ## 3. The words used in this notebook

    - **Condensate (homogeneous configuration)**: a field that depends only on the
      time $x_4$, not on $x_0, x_1, x_2, x_3, x_5, x_6, x_7$.
    - **Effective mass** $V = m + U'(S) = m + \lambda S$: the number that multiplies
      $\Phi$ on the right side of the field equation.
    - **Gravitational coefficient** $c_g = \frac32He^{a_4}b_4^{-1/2}$: the
      coefficient of $\gamma^{(x_0)}$ in the spin-connection term of the field
      equation; it grows as the block of the hidden direction and the extra times
      deflates.
    - **Matrix exponential**: for a square matrix $M$ the matrix
      $e^{Mx_4} = 1 + Mx_4 + \frac{1}{2}M^2x_4^2 + \dots$; the column
      $e^{Mx_4}\chi$ solves $\frac{d}{dx_4}\Phi = M\Phi$ with $\Phi(0) = \chi$. When
      $M^2 = k^2$ times the unit matrix, the series sums to
      $\cosh(kx_4) + \frac{\sinh(kx_4)}{k}M$.
    - **Oscillating / growing**: when $k^2 < 0$ the number $k$ is imaginary,
      $\cosh(kx_4)$ becomes a cosine and the solution oscillates; when $k^2 > 0$ it
      contains $e^{kx_4}$ and grows. Here $k^2 = c_g^2 - V^2$ changes in time, and
      the words describe one moment.
    - **Energy density** $\rho$, **pressure** $p$, **equation of state** $w = p/\rho$.
      Dust has $w = 0$, radiation $w = 1/3$, a cosmological constant $w = -1$; a
      value $w < -1$ is called *phantom*.
    - **Energy exchange**: the change of the energy density in time caused by the
      work that the inflating 3-space and the deflating block of the hidden
      direction and the extra times do.
    - **Dilution**: the decrease of a density because the volume it fills grows; here
      the 7-volume grows like $e^{-a_4}b_4^2$.
    - **Toy fluid (ILLUSTRATION)**: a source with assumed pressures $p_3 = w_3\rho$
      and $p_t = p_0 = w_t\rho$, used only to show what the conservation identity
      does; it is not a solution of the field equations of this book.
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

    **The field equation of a condensate.** In the corrected metric the field
    equation of dirac16complex00 is
    $\sum_a\frac{1}{f_a}\gamma^{(a)}\partial_a\Phi + c_g\gamma^{(0)}\Phi +
    v_g\gamma^{(4)}\Phi = V\Phi$ with $V = m + \lambda S$,
    $c_g = \frac32He^{a_4}b_4^{-1/2}$ and $v_g = b_4'/b_4 - a_4'/2$. For a
    condensate every derivative except $\partial_4$ is zero, and $f_4 = 1$, so the
    equation is $\gamma^{(4)}\partial_4\Phi + c_g\gamma^{(0)}\Phi +
    v_g\gamma^{(4)}\Phi = V\Phi$. Write $\Phi = F\chi$ with $F = e^{a_4/2}b_4^{-1}$,
    whose logarithmic derivative is $F'/F = a_4'/2 - b_4'/b_4 = -v_g$: the derivative
    of the factor removes the term with $v_g$, and
    $\gamma^{(4)}\chi' + c_g\gamma^{(0)}\chi = V\chi$. Multiplying by $-\gamma^{(4)}$
    and using $(\gamma^{(4)})^2 = -1$ gives $\chi' = M\chi$ with
    $M = -V\gamma^{(4)} + c_g\gamma^{(4)}\gamma^{(0)}$. The coordinate $x_0$ does not
    appear; $a_4$ and $b_4$ enter through $F$, through $c_g$ and through
    $S = \bar\Phi\Phi = F^2\chi^\dagger C\chi$ in $V$.

    **The solutions** (Revision record, `Revision/theory/field-theory.json`, formula
    `exact_solutions`): $M^TC + CM = 0$, so $S_\chi = \chi^\dagger C\chi$ does not
    change with $x_4$, $S_\chi = S_0$. Then $S = e^{a_4}b_4^{-2}S_0$ and
    $V(x_4) = m + \lambda S_0e^{a_4}b_4^{-2}$ is a known function of the time, and
    $\chi' = M(x_4)\chi$ is a LINEAR system, with $M^2 = (c_g^2 - V^2)$ times the unit
    matrix. Both $V$ and $c_g$ change in time, so there is no closed form, and this
    notebook solves the system with the Runge-Kutta method (RK4).

    **Its energy-momentum tensor** (formula `EMT_homogeneous_on_shell`): only $K_4$
    is nonzero, $K_4 = VS$ on shell (the terms with $v_g$ of $\Phi$ and $\bar\Phi$
    cancel in $K_4$), so $\rho = mS + U$ and $p_3 = p_t = p_0 = SU' - U$; for
    $U = \frac{\lambda}{2}S^2$: $\rho = mS + \frac{\lambda}{2}S^2$,
    $p = \frac{\lambda}{2}S^2$ and $w = \lambda S/(2m + \lambda S)$. With
    $S = e^{a_4}b_4^{-2}S_0$ all three change in time: the condensate is diluted, and
    $w \to 0$ as the 7-volume grows.

    **Energy exchange** (formula `energy_exchange`): conservation gives
    $d\rho/dx_4 = -3a_4'(\rho + p_3) - 3h_4(\rho + p_t) - h_4(\rho + p_0)$ with the
    rate $h_4 = b_4'/(2b_4) - a_4'$ of the block, that is
    $d\rho/dx_4 = -(3a_4' + 4h_4)\rho - 3a_4'p_3 - h_4(3p_t + p_0)$: the dilution
    by the 7-volume $e^{-a_4}b_4^2$ (rate $3a_4' + 4h_4 = 2b_4'/b_4 - a_4'$), the work
    of the inflating 3-space and the work of the deflating block. A condensate has
    $p_3 = p_t = p_0$; it is only diluted: $d\rho/dx_4 = -(3a_4' + 4h_4)(\rho + p)$.

    **The history.** This notebook takes $H = 0.25$, $m = 1$ and the history of the
    record, $a_4 = AHx_4$ and $b_4 = b_4(0)e^{\beta AHx_4}$ with $A = 1$ and
    $\beta = \frac43$, with $b_4(0)$ as the unit of $b_4$; then
    $e^{a_4}b_4^{-2} = e^{-(5/3)AHx_4} = e^{-5x_4/12}$, $F = e^{-5x_4/24}$ and
    $c_g = \frac32He^{AHx_4/3} = 0.375\,e^{x_4/12}$, which grows without bound: at
    late times every condensate grows (the record states the same for the
    $x_0$-independent modes of the good sector, Revision record
    `Revision/theory/reports/python-scope.json`, check
    `good_sector_x0_independent_modes_without_boundary_condition`).

    **What is not computed here.** The equation of state that an observer living in
    3-space would infer (after integrating over the hidden direction and the extra
    times), its time dependence and its comparison with supernova fit values are not
    computed in this notebook. The Revision record computes them in
    `Revision/dark_sector/` under an ASSUMED normalisation of the observer's energy
    density (definitions A, B and C, called N1 and N2 in the record of
    dirac16complex00; `Revision/docs/DARK_SECTOR_HYPOTHESES.md`, taught in Chapter
    22); which normalisation, if any, describes a physical observer, and a fit to
    supernova data, are OPEN. The $w$ of this notebook is the ratio $p/\rho$ of the
    8-dimensional tensor. The condensate's off-diagonal entries, which are not zero
    in general, are not used here.
    """),
    md(r"""
    ## 5. The matrices C and B, and the sign of S

    The next cell reads the Revision fixture (the gammas $\gamma^{(x_0)}, \dots,
    \gamma^{(x_7)}$, the matrix $C$ and the matrix $B = -iC\gamma^{(4)}$) and defines
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
    gamma = [np.array(rows, dtype=float) for rows in fixture["gamma"]]  # x0, ..., x7
    C = np.array(fixture["C"], dtype=float)  # gamma^(x0) gamma^(x1) gamma^(x2) gamma^(x3)
    B = (np.array(fixture["B"]["re"], dtype=float)  # B = -i C gamma^(x4), stored as its
         + 1j * np.array(fixture["B"]["im"], dtype=float))  # real and imaginary parts
    I16 = np.eye(16)  # the 16 x 16 unit matrix
    g4, g0 = gamma[4], gamma[0]  # gamma^(x4) and gamma^(x0)


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
    with $\lambda = 0$ has $\rho = mS = mS_0e^{a_4}b_4^{-2}$, so for $m > 0$ about
    half of these random condensates have a negative energy density.
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
                "condensate with $\\lambda = 0$ the energy density is "
                "$\\rho = mS = mS_0e^{a_4}b_4^{-2}$, so its sign is the sign of $S_0$.")
    '''),
    md(r"""
    ## 6. The matrix M and its square

    The next cell defines the function `condensate_matrix(V, c)`, which returns
    $M = -V\gamma^{(4)} + c\,\gamma^{(4)}\gamma^{(0)}$ and $k^2 = c^2 - V^2$ (with
    $c = c_g$ at the moment considered), and checks for several values of $V$ and $c$
    the two facts of the record: $M^2 = k^2 \cdot 1$ and $M^TC + CM = 0$. The second
    fact makes $S_0$ constant:
    $\frac{d}{dx_4}(\chi^\dagger C\chi) = \chi^\dagger(M^TC + CM)\chi = 0$ (here $M$ is
    real, so $M^\dagger = M^T$).
    """),
    code(r'''
    def condensate_matrix(V, c):
        """M = -V gamma^(x4) + c gamma^(x4) gamma^(x0) and k^2 = c^2 - V^2."""
        return -V * g4 + c * g4 @ g0, c ** 2 - V ** 2


    THEORY_WL = "Revision/theory/reports/wolfram-field-theory.json"
    THEORY_PY = "Revision/theory/reports/python-field-theory.json"
    A4_WL = "Revision/field_equations_a4/reports/wolfram-a4-report.json"
    worst_square, worst_c = 0.0, 0.0  # the largest deviations found
    for V_test in (-2.0, -0.5, 0.0, 0.75, 1.5, 3.0):
        for c_test in (0.1, 0.375, 1.0, 2.5):
            M_test, k2_test = condensate_matrix(V_test, c_test)
            worst_square = max(worst_square, np.abs(M_test @ M_test - k2_test * I16).max())
            worst_c = max(worst_c, np.abs(M_test.T @ C + C @ M_test).max())
    check(worst_square < 1e-12 and worst_c < 1e-12
          and recorded(THEORY_WL, "solution_matrix_square") == "PASS"
          and recorded(A4_WL, "condensate_equation_x0_consistent") == "PASS",
          "M^2 = (c^2 - V^2) times 1 and M^T C + C M = 0 for 24 pairs (V, c)",
          record=f"{THEORY_WL}, check solution_matrix_square; {A4_WL}, check "
                 "condensate_equation_x0_consistent")
    '''),
    md(r"""
    ## 7. Two condensates along the history

    The next cell fixes $m = 1$, $H = 0.25$, the history ($A = 1$, $\beta = \frac43$)
    and a column $\chi$ with $S_0 = \chi^\dagger C\chi = 1$ (it draws random columns
    with a fixed seed until $S_0 > 0$ and divides by $\sqrt{S_0}$). It defines
    `a4_of(x4)` and `b4_of(x4)`, which return $a_4 = AHx_4$ and $b_4 = e^{\beta AHx_4}$
    (in the unit $b_4(0)$), `F_of(x4)` $= e^{a_4/2}b_4^{-1}$, `dilution(x4)`
    $= e^{a_4}b_4^{-2}$ (so that $S = S_0 \cdot$ `dilution`) and `c_g_of(x4)`
    $= \frac32He^{a_4}b_4^{-1/2}$, and the function `condensate(chi0, lam, x4_end,
    steps)`, which solves $\chi' = M(x_4)\chi$ with
    $V(x_4) = m + \lambda S_0e^{a_4}b_4^{-2}$ and $c = c_g(x_4)$ by RK4 (four slopes per
    step, as in Notebook 08a) and returns the times, $\Phi = F\chi$, its derivative
    $\Phi' = F(M\chi - v_g\chi)$ (product rule, with $F' = -v_gF$ and
    $v_g = b_4'/b_4 - a_4'/2$, a constant on this history) and the columns $\chi$.
    It prints the value of $S_0$ after the division, which must be 1.
    """),
    code(r'''
    m, H = 1.0, 0.25  # the mass and the author's constant
    A, beta = 1.0, 4 / 3  # the history a4 = A H x4, b4 = b4(0) e^(beta A H x4)
    a4p, u = A * H, beta * A * H  # a4' = 1/4 and b4'/b4 = 1/3 on the history
    h4 = u / 2 - a4p  # the rate of the block: -1/12 (it deflates)
    v_g = u - a4p / 2  # the coefficient of gamma^(x4) in the field equation: 5/24
    rng = np.random.default_rng(7)
    while True:  # draw until S0 > 0 (the first draw usually succeeds)
        chi = rng.normal(size=16) + 1j * rng.normal(size=16)
        S0 = (chi.conj() @ C @ chi).real
        if S0 > 0:
            break
    chi = chi / np.sqrt(S0)  # now chi^dagger C chi = 1


    def a4_of(x4):
        """a4 = A H x4 on the history."""
        return A * H * x4


    def b4_of(x4):
        """b4 = e^(beta A H x4) on the history, in the unit b4(0)."""
        return np.exp(beta * A * H * x4)


    def F_of(x4):
        """The factor F = e^(a4/2) b4^(-1) of Phi = F chi."""
        return np.exp(a4_of(x4) / 2) / b4_of(x4)


    def dilution(x4):
        """e^(a4) b4^(-2) = F^2, so that S = S0 e^(a4) b4^(-2)."""
        return np.exp(a4_of(x4)) / b4_of(x4) ** 2


    def c_g_of(x4):
        """The gravitational coefficient c_g = (3/2) H e^(a4) b4^(-1/2)."""
        return 1.5 * H * np.exp(a4_of(x4)) / np.sqrt(b4_of(x4))


    def condensate(chi0, lam, x4_end, steps):
        """RK4 for chi' = M(x4) chi with V = m + lam S0 e^a4 b4^-2 and c = c_g(x4);
        returns the times, Phi = F chi, dPhi/dx4 = F (M chi - v_g chi) and chi."""
        S0_value = (chi0.conj() @ C @ chi0).real  # constant along the solution
        step = x4_end / steps

        def rate(x4, column):  # M(x4) chi
            V = m + lam * S0_value * dilution(x4)
            return condensate_matrix(V, c_g_of(x4))[0] @ column

        times_out, columns = [0.0], [chi0.astype(complex)]
        column = columns[0]
        for n in range(steps):
            x4 = n * step
            s1 = rate(x4, column)
            s2 = rate(x4 + step / 2, column + step / 2 * s1)
            s3 = rate(x4 + step / 2, column + step / 2 * s2)
            s4 = rate(x4 + step, column + step * s3)
            column = column + step / 6 * (s1 + 2 * s2 + 2 * s3 + s4)
            times_out.append((n + 1) * step)
            columns.append(column)
        times_out, columns = np.array(times_out), np.array(columns)
        factor = F_of(times_out)  # F at every time
        derivatives = np.array([rate(t, c) - v_g * c for t, c in zip(times_out, columns)])
        return (times_out, factor[:, None] * columns, factor[:, None] * derivatives,
                columns)


    S0_now = (chi.conj() @ C @ chi).real  # 1 up to rounding
    report("S0 = chi^dagger C chi after the division", f"{S0_now:.6f}")
    '''),
    md(r"""
    The next cell builds two condensates from $x_4 = 0$ to $16$ with 1600 steps, and
    finds, by halving an interval (bisection) 60 times, the moments at which
    $k^2 = c_g^2 - V^2$ changes sign. With $\lambda = 0.5$ the effective mass falls
    from $V = 1.5$ towards 1 while $c_g$ rises from $0.375$: the condensate
    oscillates first, and grows once $c_g$ has passed $V$. With $\lambda = -0.8$ the
    effective mass starts at $V = 0.2$, below $c_g = 0.375$: the condensate grows
    first, oscillates once $V$ has passed $c_g$, and grows again when $c_g$ catches
    up with $V$. At every step the cell checks the field equation
    $\gamma^{(4)}\Phi' + c_g\gamma^{(0)}\Phi + v_g\gamma^{(4)}\Phi =
    (m + \lambda S)\Phi$, with $S = \bar\Phi\Phi$ computed from the solution, and that
    $S = e^{a_4}b_4^{-2}S_0$; and it repeats each run with half the number of steps to
    measure the accuracy of RK4.
    """),
    code(r'''
    EXAMPLES = {"oscillating first": 0.5, "growing first": -0.8}  # name -> lambda


    def k_squared(x4, lam):
        """k^2 = c_g^2 - V^2 at the time x4 for a condensate with S0 = 1."""
        return c_g_of(x4) ** 2 - (m + lam * dilution(x4)) ** 2


    def sign_change(lam, low, high):
        """The time between low and high at which k^2 changes sign (bisection)."""
        for _ in range(60):
            middle = (low + high) / 2
            if np.sign(k_squared(middle, lam)) == np.sign(k_squared(low, lam)):
                low = middle  # the sign change lies in the upper half
            else:
                high = middle  # the sign change lies in the lower half
        return (low + high) / 2


    CHANGES = {"oscillating first": [sign_change(0.5, 5.0, 16.0)],
               "growing first": [sign_change(-0.8, 0.0, 3.0),
                                 sign_change(-0.8, 5.0, 16.0)]}
    solutions = {}  # name -> (times, Phi, dPhi/dx4, chi)
    for name, lam in EXAMPLES.items():
        times, phis, dphis, columns = condensate(chi, lam, 16.0, 1600)
        S_values = np.einsum("ti,ij,tj->t", phis.conj(), C, phis).real
        S_expected = dilution(times)  # S0 e^(a4) b4^(-2) with S0 = 1
        worst_residual = 0.0
        for x4, phi, dphi, S_now in zip(times, phis, dphis, S_values):
            residual = (g4 @ dphi + c_g_of(x4) * g0 @ phi + v_g * g4 @ phi
                        - (m + lam * S_now) * phi)
            worst_residual = max(worst_residual,
                                 np.abs(residual).max() / np.abs(phi).max())
        solutions[name] = (times, phis, dphis, columns)
        report(f"{name}: lambda = {lam}, V = m + lambda S at x4 = 0 and 16",
               f"{m + lam:.4f} and {m + lam * S_expected[-1]:.4f}")
        report(f"{name}: k^2 changes sign at x4",
               ", ".join(f"{t:.4f}" for t in CHANGES[name]))
        check(worst_residual < 1e-9,
              f"{name}: the field equation holds at 1601 times")
        check(np.abs(S_values / S_expected - 1).max() < 1e-9,
              f"{name}: S = e^a4 b4^-2 S0 at 1601 times (e^-a4 b4^2 S stays 1)")
        coarse = condensate(chi, lam, 16.0, 800)[1][-1]  # twice the step
        rk4_change = np.abs(coarse - phis[-1]).max() / np.abs(phis[-1]).max()
        report(f"{name}: change of Phi(16) when the RK4 step is halved",
               f"{rk4_change:.1e}")
        check(rk4_change < 1e-7,
              f"{name}: halving the RK4 step changes Phi(16) by less than 1e-7")
    report("c_g at x4 = 0 and 16", f"{c_g_of(0.0):.4f} and {c_g_of(16.0):.4f}")
    check(recorded(THEORY_WL, "exact_solution_nonlinear_homogeneous_C") == "PASS"
          and recorded(THEORY_PY, "exact_nonlinear_homogeneous_solution") == "PASS",
          "both condensates are the record's homogeneous solutions",
          record=f"{THEORY_WL}, check exact_solution_nonlinear_homogeneous_C; "
                 f"{THEORY_PY}, check exact_nonlinear_homogeneous_solution")
    '''),
    md(r"""
    The next cell draws the two condensates. Left: the real parts of three of the 16
    components of the condensate with $\lambda = 0.5$, and $S$; both shrink at first,
    because $\Phi = F\chi$ with $F = e^{-5x_4/24}$ and $S = e^{-5x_4/12}S_0$, and the
    components oscillate; after the dotted line, where $k^2$ changes sign, the
    components grow. Right: for the condensate with $\lambda = -0.8$, the size
    $\chi^\dagger\chi = F^{-2}\Phi^\dagger\Phi$ of the column $\chi$ and the size
    $\Phi^\dagger\Phi$ of the field (logarithmic axis), with dotted lines at the two
    moments at which $k^2$ changes sign.
    """),
    code(r'''
    fig, (left, right) = plt.subplots(1, 2, figsize=(9.6, 3.9))
    times, phis, _, _ = solutions["oscillating first"]
    S_values = np.einsum("ti,ij,tj->t", phis.conj(), C, phis).real
    for component in (0, 5, 10):  # three of the 16 components (rows 1, 6 and 11)
        left.plot(times, phis[:, component].real,
                  label=f"Re $\\Phi_{{{component + 1}}}$")
    left.plot(times, S_values, "k--", label="$S = \\bar\\Phi\\Phi$")
    left.axvline(CHANGES["oscillating first"][0], color="black", linestyle=":",
                 linewidth=0.9)
    left.set_xlabel("time $x_4$")
    left.set_ylabel("value")
    left.set_ylim(-0.8, 1.35)  # room for the legend above the curves
    left.set_title("Oscillating first: $\\lambda = 0.5$")
    left.legend(fontsize=7, loc="upper center", ncol=4)
    times, phis, _, columns = solutions["growing first"]
    right.plot(times, np.einsum("ti,ti->t", columns.conj(), columns).real,
               label="$\\chi^\\dagger\\chi = F^{-2}\\Phi^\\dagger\\Phi$")
    right.plot(times, np.einsum("ti,ti->t", phis.conj(), phis).real, "--",
               label="$\\Phi^\\dagger\\Phi$")
    for moment in CHANGES["growing first"]:
        right.axvline(moment, color="black", linestyle=":", linewidth=0.9)
    right.set_yscale("log")
    right.set_xlabel("time $x_4$")
    right.set_title("Growing first: $\\lambda = -0.8$")
    right.legend(fontsize=8)
    save_figure(fig, "condensate_solutions",
                "Two condensates $\\Phi = e^{a_4/2}b_4^{-1}\\chi$ of dirac16complex00 with "
                "$m = 1$, $H = 0.25$ and $S_0 = 1$ along the history $a_4 = AHx_4$, "
                "$b_4 = e^{4AHx_4/3}$ ($A = 1$), for $x_4$ from $0$ to $16$; the "
                "gravitational coefficient $c_g = 0.375\\,e^{x_4/12}$ grows from 0.375 "
                "to 1.42. Left, $\\lambda = 0.5$: the effective mass $m + \\lambda S$ "
                "falls from 1.5 towards 1; the real parts of the components 1, 6 and 11 "
                "of $\\Phi$ oscillate and shrink, and $S$ (dashed) falls like "
                "$e^{-5x_4/12}$; after $x_4 = 11.81$ (dotted), where $c_g$ passes the "
                "effective mass, the components grow. Right, $\\lambda = -0.8$, "
                "logarithmic axis: the size $\\chi^\\dagger\\chi$ of the column and the "
                "size $\\Phi^\\dagger\\Phi$ of the field (dashed); the condensate grows "
                "until $x_4 = 0.68$, oscillates until $x_4 = 11.70$ (dotted lines) and "
                "grows again. All values are pure numbers.")
    '''),
    md(r"""
    ## 8. Energy density, pressures, kinetic and potential parts of the condensates

    For a condensate every kinetic term except $K_4$ vanishes, because every other
    derivative is zero. The next cell computes, at every step,
    $K_4 = \frac12(\bar\Phi\gamma^{(4)}\Phi' - \bar\Phi'\gamma^{(4)}\Phi)$ from the
    solution, the Lagrangian $L_0 = K_4 - mS - U$, the energy density
    $\rho = -T^{x_4}{}_{x_4} = K_4 - L_0$ and the pressures
    $p_\mu = T^\mu{}_\mu = L_0 - K_\mu = L_0$ for $\mu \neq x_4$, which are equal in
    all seven directions. It checks $K_4 = VS$ (the terms with $v_g$ cancel),
    $\rho = mS + \frac{\lambda}{2}S^2$ and $p = \frac{\lambda}{2}S^2$ with
    $S = e^{a_4}b_4^{-2}S_0$, hence the kinetic and potential parts
    ($\rho_{\rm kin} = 0$, $p_{\rm kin} = K_4 = VS$, $p_{\rm pot} = -(mS + U)$), the trace
    $-\rho + 7p = -mS + 3\lambda S^2$, and that the $x_4$-$x_0$ component vanishes:
    $T^{x_4}{}_{x_0} = -\frac14(B_{40} - e^{-a_4}b_4^{1/2}\cot z\,B_{04})$ with
    $B_{40} = 0$ (no $x_0$ derivative) and
    $B_{04} = \bar\Phi\gamma^{(0)}\Phi' - \bar\Phi'\gamma^{(0)}\Phi$, which must be 0.
    It prints $\rho$, $p$ and $w = p/\rho$ at three times.
    """),
    code(r'''
    def homogeneous_tensor(phi, dphi, lam):
        """S, U, K4, rho, p and B04 of a condensate at one time."""
        S = (phi.conj() @ C @ phi).real
        U = lam / 2 * S ** 2
        K4 = 0.5 * (phi.conj() @ C @ g4 @ dphi - dphi.conj() @ C @ g4 @ phi)
        L0 = K4.real - m * S - U  # the other seven kinetic terms are zero
        B04 = phi.conj() @ C @ g0 @ dphi - dphi.conj() @ C @ g0 @ phi
        return S, U, K4, K4.real - L0, L0, B04  # rho = K4 - L0, p = L0


    for name, lam in EXAMPLES.items():
        times, phis, dphis, _ = solutions[name]
        S_expected = dilution(times)
        rhos, ps, worst = [], [], 0.0
        for phi, dphi in zip(phis, dphis):
            S, U, K4, rho, p, B04 = homogeneous_tensor(phi, dphi, lam)
            size = (phi.conj() @ phi).real  # for relative tolerances
            worst = max(worst, abs(K4.imag) / size,
                        abs(K4.real - (m + lam * S) * S) / size, abs(B04) / size)
            rhos.append(rho)
            ps.append(p)
        rhos, ps = np.array(rhos), np.array(ps)
        check(worst < 1e-12, f"{name}: K4 is real, K4 = V S, and B04 = 0 (T^x4_x0 = 0)")
        check(np.abs(rhos / (m * S_expected + lam / 2 * S_expected ** 2) - 1).max()
              < 1e-9 and np.abs(ps / (lam / 2 * S_expected ** 2) - 1).max() < 1e-9,
              f"{name}: rho = m S + lambda S^2/2, p = lambda S^2/2, S = e^a4 b4^-2 S0")
        trace_error = np.abs(-rhos + 7 * ps - (-m * S_expected + 3 * lam
                                                * S_expected ** 2)).max()
        check(trace_error < 1e-9,
              f"{name}: trace -rho + 7 p = -m S + 3 lambda S^2 at every step")
        for index, label in ((0, "x4 = 0"), (800, "x4 = 8"), (-1, "x4 = 16")):
            report(f"{name}: rho, p, w at {label}",
                   f"{rhos[index]:.6f}, {ps[index]:.3e}, {ps[index] / rhos[index]:.6f}")
    check(recorded(THEORY_PY, "commuting_homogeneous_on_shell_rho_p") == "PASS"
          and recorded(THEORY_PY, "commuting_T_x4x0_homogeneous") == "PASS"
          and recorded(THEORY_PY, "commuting_trace_on_shell") == "PASS",
          "these are the record's homogeneous values and its vanishing x4-x0 component",
          record=f"{THEORY_PY}, checks commuting_homogeneous_on_shell_rho_p, "
                 "commuting_T_x4x0_homogeneous and commuting_trace_on_shell")
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
    Along the history $S = e^{a_4}b_4^{-2}S_0$ shrinks, so $x$ and $w$ of one
    condensate change in time and approach 0. The next cell does not use this formula
    to compute $w$. For twelve values of $x$ it builds the condensate with $m = 1$,
    $S_0 = 1$ and the $\lambda$ for which $\lambda S/m = x$ at the time $x_4 = 1.3$
    (that is $\lambda = x\,e^{0.5417}$, since $S(1.3) = e^{-(5/12)1.3} =
    e^{-0.5417}$), solves it with RK4 up to $x_4 = 1.3$, computes $\rho$ and $p$ there
    as in section 8, and only then compares $p/\rho$ with $x/(2 + x)$. It also finds
    the special values: $w = 0$ at $x = 0$ (dust-like), $w = -1$ at $x = -1$, where
    the effective mass $V = m + \lambda S$ is zero, $w < -1$ (phantom) for
    $-2 < x < -1$, and $w \to 1$ as $x$ grows. At $x = -2$ the energy density is zero
    and $w$ is not defined. For $x < -2$ (with $m > 0$ and $S > 0$) the energy density
    and the pressure are both negative, and $w > 1$.
    """),
    code(r'''
    x_measured = np.array([-3.5, -3.0, -2.5, -1.5, -1.0, -0.5, 0.0, 0.5, 1.0, 2.0, 3.0,
                           4.0])  # values of x = lambda S/m at the time x4 = 1.3
    S_then = dilution(1.3)  # S at x4 = 1.3 for S0 = 1: e^(-0.5417)
    rho_measured, p_measured = [], []  # rho and p of each of the twelve condensates
    for x_value in x_measured:
        lam_x = x_value * m / S_then  # lambda S(1.3) / m = x
        _, phis, dphis, _ = condensate(chi, lam_x, 1.3, 1300)
        S, U, K4, rho, p, B04 = homogeneous_tensor(phis[-1], dphis[-1], lam_x)
        rho_measured.append(rho)
        p_measured.append(p)
    rho_measured, p_measured = np.array(rho_measured), np.array(p_measured)
    w_measured = p_measured / rho_measured  # the equation of state of each condensate
    w_formula = x_measured / (2 + x_measured)
    check(np.abs(w_measured - w_formula).max() < 1e-9,
          "w = p/rho of 12 condensates at x4 = 1.3 equals x/(2 + x), x = lambda S/m")
    at_minus_one = w_measured[list(x_measured).index(-1.0)]
    check(abs(at_minus_one + 1.0) < 1e-9,
          "w = -1 where the effective mass m + lambda S vanishes (x = -1)")
    below = x_measured < -2  # the three condensates with x < -2
    check(np.all(rho_measured[below] < 0) and np.all(p_measured[below] < 0)
          and np.all(w_measured[below] > 1),
          "for x < -2: rho < 0, p < 0 and w > 1")
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
            label="measured on condensates at $x_4 = 1.3$")
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
                "$w = x/(2 + x)$, the red points are $p/\\rho$ computed at $x_4 = 1.3$ "
                "from twelve condensates along the history ($m = 1$, $H = 0.25$, "
                "$S_0 = 1$, $\\lambda = x e^{0.5417}$) and lie on it. $w = 0$ at "
                "$x = 0$, $w = -1$ (dashed) at $x = -1$, where the "
                "effective mass $m + \\lambda S$ vanishes, $w < -1$ (shaded) for "
                "$-2 < x < -1$, $w$ is undefined at $x = -2$ (dotted) where $\\rho = 0$, "
                "$w > 1$ for $x < -2$, where $\\rho$ and $p$ are both negative, "
                "and $w$ approaches $1$ for large $x$. This is the 8-dimensional "
                "ratio, not the equation of state a 3-space observer would infer.")
    '''),
    md(r"""
    ## 11. Where condensates oscillate and where they grow

    A condensate oscillates at a moment when $c_g^2 - V^2 < 0$, that is when
    $|1 + x| > c_g/|m|$ with $x = \lambda S/m$, and grows when $|1 + x| < c_g/|m|$
    (because $V = m(1 + x)$). The equation of state depends on $x$ alone, so on the
    map of the plane $(x, c_g/|m|)$ every line of constant $w$ is vertical. Along the
    history a condensate moves on this map in two ways at once: $x$ shrinks with
    $S = e^{a_4}b_4^{-2}S_0$ (towards $x = 0$), and $c_g/|m|$ grows like
    $e^{AHx_4/3}$ (upwards), because the block deflates. The next cell draws the map,
    the lines $w = -1$, $0$, $1/3$ and the paths of the two condensates of section 7
    from $x_4 = 0$ to $16$. It checks that the condensate with $\lambda = 0.5$ starts
    in the oscillating region and enters the growing wedge at the moment found in
    section 7, and that the one with $\lambda = -0.8$ starts in the wedge, leaves it
    and enters it again at those moments.
    """),
    code(r'''
    x_grid = np.linspace(-3.0, 2.0, 701)  # x = lambda S/m
    h_grid = np.linspace(0.0, 2.0, 301)  # c_g/|m|
    X, Hgrid = np.meshgrid(x_grid, h_grid)  # every pair (x, c_g/|m|) of the two grids
    growing_region = (np.abs(1 + X) < Hgrid).astype(float)  # 1 where c_g^2 > V^2
    fig, ax = plt.subplots()
    ax.contourf(X, Hgrid, growing_region, levels=[-0.5, 0.5, 1.5],
                colors=["#dbe9f6", "#f6d5d5"])
    for label, x_line in (("$w = -1$", -1.0), ("$w = 0$", 0.0), ("$w = 1/3$", 1.0)):
        ax.axvline(x_line, color="black", linestyle="--", linewidth=0.8)
        ax.text(x_line + 0.05, 1.88, label, fontsize=8)
    path_times = np.linspace(0.0, 16.0, 1601)
    paths = {name: (lam_value * dilution(path_times) / m,  # x(x4) with S0 = 1
                    c_g_of(path_times) / abs(m))  # c_g(x4)/|m|
             for name, lam_value in EXAMPLES.items()}
    for name, (path_x, path_h) in paths.items():
        ax.plot(path_x, path_h, color="black", linewidth=1.2)
        ax.annotate("", xy=(path_x[-1], path_h[-1]), xytext=(path_x[-40], path_h[-40]),
                    arrowprops={"arrowstyle": "->", "color": "black"})
        ax.plot([path_x[0]], [path_h[0]], "ko")
        ax.text(path_x[0] - 0.25, path_h[0] - 0.13, name, fontsize=8)
    ax.text(-2.8, 0.3, "oscillating", fontsize=9)
    ax.text(-2.4, 1.6, "growing", fontsize=9)
    ax.set_xlabel("$x = \\lambda S / m$")
    ax.set_ylabel("$c_g/|m|$")
    ax.set_title("Condensates: oscillating (blue) or growing (red)")
    ax.grid(False)
    save_figure(fig, "regime_map",
                "Map of the condensates of dirac16complex00 in the plane of "
                "$x = \\lambda S/m$ (horizontal) and $c_g/|m|$ (vertical), pure numbers, "
                "with $c_g = \\frac{3}{2}He^{a_4}b_4^{-1/2}$. In the red wedge "
                "$|1 + x| < c_g/|m|$ the number $c_g^2 - (m + \\lambda S)^2$ is positive "
                "and the condensate grows at that moment; in the blue region it "
                "oscillates. The dashed vertical lines are the equations of state "
                "$w = -1$, $w = 0$ and $w = 1/3$; $w$ depends on $x$ only. The black "
                "curves are the paths of the two condensates of the second figure "
                "($H = 0.25$, $m = 1$) from $x_4 = 0$ (dots) to $16$ (arrows): $S$ is "
                "diluted, so $x$ moves towards $0$, while $c_g$ grows like "
                "$e^{x_4/12}$ as the block deflates; both paths end in the growing "
                "wedge. Every condensate with $w = -1$ lies in the wedge at that "
                "moment.")
    inside = {name: np.abs(1 + path_x) < path_h for name, (path_x, path_h) in paths.items()}
    entries = {name: path_times[1:][np.diff(inside[name].astype(int)) != 0]
               for name in EXAMPLES}  # the grid times just after each change
    check(not inside["oscillating first"][0] and len(entries["oscillating first"]) == 1
          and abs(entries["oscillating first"][0] - CHANGES["oscillating first"][0])
          < 0.011,
          "lambda = 0.5: starts oscillating, enters the growing wedge once")
    check(bool(inside["growing first"][0]) and len(entries["growing first"]) == 2
          and np.abs(entries["growing first"] - CHANGES["growing first"]).max() < 0.011,
          "lambda = -0.8: starts in the wedge, leaves it and enters it again")
    '''),
    md(r"""
    ## 12. Energy exchange between 3-space and the block

    Conservation says $d\rho/dx_4 = -(3a_4' + 4h_4)\rho - 3a_4'p_3 - h_4(3p_t + p_0)$
    (the dilution by the 7-volume, the work of 3-space and the work of the block). A
    condensate has $p_3 = p_t = p_0 = p$, so along the history it is only diluted,
    $d\rho/dx_4 = -(3a_4' + 4h_4)(\rho + p)$, with $3a_4' + 4h_4 = 2b_4'/b_4 - a_4' =
    \frac{5}{12}$ on this history. The next cell confirms this on the condensate with
    $\lambda = 0.5$: it computes $\rho$ and $p$ at every step and compares the slope of
    $\rho$ (finite differences) with $-(3a_4' + 4h_4)(\rho + p)$.
    """),
    code(r'''
    times, phis, dphis, _ = solutions["oscillating first"]
    rho_and_p = np.array([homogeneous_tensor(phi, dphi, 0.5)[3:5]
                          for phi, dphi in zip(phis, dphis)])
    rho_at_times, p_at_times = rho_and_p[:, 0], rho_and_p[:, 1]
    slope = np.gradient(rho_at_times, times)  # d rho/dx4 by finite differences
    dilution_rate = 3 * a4p + 4 * h4  # 5/12 on this history
    diluted = -dilution_rate * (rho_at_times + p_at_times)  # -(3 a4' + 4 h4)(rho + p)
    # [2:-2] leaves out two points at each end, where np.gradient is less exact.
    check(np.abs(slope - diluted)[2:-2].max() < 1e-4 * np.abs(diluted).max()
          and recorded(THEORY_WL, "energy_exchange_equation") == "PASS"
          and recorded(THEORY_PY, "energy_exchange_equation") == "PASS",
          "condensate (p3 = p_t = p0): d rho/dx4 = -(3 a4' + 4 h4)(rho + p)",
          record=f"{THEORY_WL} and {THEORY_PY}, check energy_exchange_equation")
    report("dilution rate 3 a4' + 4 h4 = 2 b4'/b4 - a4'", f"{dilution_rate:.6f}")
    '''),
    md(r"""
    Then, as an ILLUSTRATION only, the next cell takes toy fluids with assumed
    pressures $p_3 = w_3\rho$ and $p_t = p_0 = w_t\rho$ (constant $w_3$, $w_t$; $p_0 =
    p_t$ is what the $x_0$ identity requires of entries that do not depend on $x_0$;
    these are not solutions of the field equations of this book). Along the history
    the identity becomes $d\rho/dx_4 = -AH\big(3(w_3 - w_t) + (2\beta - 1)(1 + w_t)\big)
    \rho$, whose solution is an exponential. The cell takes five toy fluids with
    $w_t = 0$ and $\Delta w = w_3 - w_t$ from $-\frac59$ to $\frac23$, solves the
    equation numerically with the Runge-Kutta method (RK4, step $0.05$), compares
    with the exact solution (and checks that halving the step divides the error by
    about $2^4 = 16$, as it must for a fourth-order method), and checks that
    reversing the history ($A \to -A$: 3-space deflates, the block inflates and
    $b_4$ shrinks) reverses the flow.
    """),
    code(r'''
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


    def toy_rate(delta, w_t, sign=1.0):
        """The rate of rho of a toy fluid; sign -1 reverses the history (A -> -A)."""
        return -sign * A * H * (3 * delta + (2 * beta - 1) * (1 + w_t))


    STEP, COUNT = 0.05, 160  # x4 from 0 to 8
    toy_times = STEP * np.arange(COUNT + 1)
    DELTAS = (-5 / 9, -1 / 3, 0.0, 1 / 3, 2 / 3)  # Delta w = w3 - w_t, with w_t = 0
    toy = {}  # Delta w -> rho(x4)/rho0 along the history
    errors = {STEP: 0.0, STEP / 2: 0.0}  # the largest relative error for two steps
    for delta in DELTAS:
        for step in errors:
            count = round(8.0 / step)  # the number of steps from x4 = 0 to 8
            path = rk4(lambda r, d=delta: toy_rate(d, 0.0) * r, 1.0, step, count)
            exact = np.exp(toy_rate(delta, 0.0) * step * np.arange(count + 1))
            errors[step] = max(errors[step], np.abs(path / exact - 1).max())
            if step == STEP:
                toy[delta] = path
    check(errors[STEP] < 1e-6,
          "RK4 (step 0.05) reproduces the exponential rho of 5 toy fluids")
    ratio = errors[STEP] / errors[STEP / 2]  # RK4: half the step, 1/16 of the error
    check(14 < ratio < 18, "halving the RK4 step divides the error by about 2^4 = 16")
    report("largest relative RK4 error, step 0.05", f"{errors[STEP]:.2e}")
    report("error ratio of the steps 0.05 and 0.025", f"{ratio:.2f}")
    reversed_path = rk4(lambda r: toy_rate(1 / 3, 0.0, -1.0) * r, 1.0, STEP, COUNT)
    check(np.abs(reversed_path * toy[1 / 3] - 1).max() < 1e-8,
          "A -> -A reverses the energy flow (the product of the two paths is 1)")
    report("toy fluid Delta w = 1/3, w_t = 0: rho(8)/rho(0)", f"{toy[1 / 3][-1]:.6f}")
    '''),
    md(r"""
    The next cell draws the energy densities of the toy fluids and of the condensate
    (left), and for the toy fluid with $(w_3, w_t) = (1/3, 2/3)$, that is
    $\Delta w = -1/3$, the three contributions to $d\rho/dx_4$ (right): the work of
    the inflating 3-space, $-3a_4'p_3$, which takes energy out, the work of the
    deflating block, $-h_4(3p_t + p_0) = -4h_4p_t$, which puts energy in, and the
    dilution $-(3a_4' + 4h_4)\rho$. The cell checks that their sum is the slope
    $d\rho/dx_4$ of the drawn path.
    """),
    code(r'''
    fig, (left, right) = plt.subplots(1, 2, figsize=(9.6, 3.9))
    fig.subplots_adjust(wspace=0.35)  # more room between the two panels
    for delta in DELTAS:
        left.plot(toy_times, toy[delta], label=f"toy, $\\Delta w = {delta:+.2f}$")
    left.plot(times[times <= 8.0], rho_at_times[times <= 8.0] / rho_at_times[0], "k:",
              linewidth=2.0, label="condensate ($p_3 = p_t = p_0$)")
    left.set_yscale("log")
    left.set_xlabel("time $x_4$")
    left.set_ylabel("$\\rho(x_4) / \\rho(0)$")
    left.set_title("Energy density along the history ($w_t = 0$)")
    left.legend(fontsize=7)
    rho_toy = rk4(lambda r: toy_rate(-1 / 3, 2 / 3) * r, 1.0, STEP, COUNT)
    work_space = -3 * a4p * (1 / 3) * rho_toy  # -3 a4' p3 with p3 = rho/3
    work_block = -4 * h4 * (2 / 3) * rho_toy  # -h4 (3 p_t + p0) with p_t = p0 = 2 rho/3
    dilution_toy = -dilution_rate * rho_toy  # -(3 a4' + 4 h4) rho
    right.plot(toy_times, work_space, label="3-space: $-3a_4' p_3$")
    right.plot(toy_times, work_block, "--", label="block: $-h_4(3p_t + p_0)$")
    right.plot(toy_times, dilution_toy, "-.",
               label="dilution: $-(3a_4' + 4h_4)\\rho$")
    right.plot(toy_times, np.gradient(rho_toy, toy_times), ":", color="black",
               label="$d\\rho/dx_4$ (finite differences)")
    right.axhline(0.0, color="black", linewidth=0.8)
    right.set_xlabel("time $x_4$")
    right.set_ylabel("rate of change of $\\rho$")
    right.set_title("Toy fluid $(w_3, w_t) = (1/3, 2/3)$")
    right.legend(fontsize=7)
    save_figure(fig, "energy_exchange",
                "Energy exchange and dilution along the history $a_4 = AHx_4$, "
                "$b_4 = e^{4AHx_4/3}$, $A = 1$, $H = 0.25$, for $x_4$ from $0$ to $8$. "
                "Left, logarithmic axis: $\\rho(x_4)/\\rho(0)$ of five toy fluids with "
                "assumed pressures $p_3 = w_3\\rho$, $p_t = p_0 = 0$, $\\Delta w = w_3$ "
                "from $-5/9$ to $2/3$ (an illustration, not solutions), solved with "
                "RK4: $\\rho$ falls faster when $p_3 > p_t$, and the dilution by the "
                "growing 7-volume makes it fall except at $\\Delta w = -5/9$, where the "
                "two terms balance; the condensate (dotted) has $p_3 = p_t = p_0$ and "
                "is only diluted. Right: for the toy fluid $(w_3, w_t) = (1/3, 2/3)$ "
                "the work of 3-space $-3a_4'p_3$ (negative), the work of the deflating "
                "block $-h_4(3p_t + p_0)$ (positive), the dilution "
                "$-(3a_4' + 4h_4)\\rho$ (dash-dotted) and their sum $d\\rho/dx_4$ "
                "(dotted); units of energy per unit volume per unit time.")
    # [2:-2] leaves out two points at each end, where np.gradient is less exact.
    check(np.abs(np.gradient(rho_toy, toy_times)
                 - (work_space + work_block + dilution_toy))[2:-2].max() < 1e-3,
          "d rho/dx4 equals the sum of the three terms on the drawn path")
    '''),
    md(r"""
    ## 13. The energy of the commuting field has no lower bound

    The record proves that the classical energy of dirac16complex00 is unbounded
    below already for $U = 0$, with an exact example: in flat 4+4 space (all
    $f_a = 1$, no spin connection) with $m = 2$ and the momentum
    $(k_0, k_1, k_2, k_3) = (4, 1, 2, 0)$, the plane waves
    $\Phi = u e^{i(k_1x_1 + k_2x_2 + k_0x_0 - Ex_4)}$ with $E = 5$ solve the field
    equation when $u$ lies in the 8-dimensional eigenspace of the matrix
    $h = m\beta + \sum_a k_a\alpha^a$ ($\beta = -i\gamma^{(4)}$,
    $\alpha^a = -\gamma^{(4)}\gamma^{(a)}$; the code writes $\beta$ as `beta_matrix`,
    because `beta` is the exponent of the history) with eigenvalue 5, and the energy density
    is $\rho = E u^\dagger Bu$. On that eigenspace the form $u^\dagger Bu$ has four
    positive and four negative directions (Krein inertia (4,4)). The next cell
    builds $h$, checks that it is Hermitian, that $h^2 = 25$ and that it commutes
    with $B$, finds its eigenvalues and the eigenspace with eigenvalue 5, and the
    inertia of the form $u^\dagger Bu$ on that eigenspace (the eigenvalues of the
    $8 \times 8$ matrix of the form).
    """),
    code(r'''
    m_flat, E_flat = 2.0, 5.0
    momentum = {0: 4.0, 1: 1.0, 2: 2.0, 3: 0.0}  # k0, k1, k2, k3 (x5, x6, x7: zero)
    beta_matrix = -1j * g4  # Dirac's beta; the name beta is the history's exponent
    h = m_flat * beta_matrix + sum(k_a * (-g4 @ gamma[a]) for a, k_a in momentum.items())
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
    '''),
    md(r"""
    The next cell defines `flat_energy_density(u)`, which computes
    $\rho = -\sum_{a \neq x_4}K_a + mS$ of the plane wave from its kinetic terms
    ($\partial_a\Phi = ik_a\Phi$), takes the two eigenvectors of the form with
    $Bu = -u$ and $Bu = +u$, checks that each plane wave solves the field equation
    $\sum_a\gamma^{(a)}\partial_a\Phi = m\Phi$ of flat space, and checks the record's
    values $\rho = -5$ and $\rho = +5$.
    """),
    code(r'''
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
    '''),
    md(r"""
    The next cell draws 5000 random unit vectors $u$ of the eigenspace (random
    combinations of its eight columns, each divided by its length), computes the
    energy density of each plane wave from its kinetic terms, and checks that it
    equals $E\,u^\dagger Bu$ every time and takes both signs.
    """),
    code(r'''
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
                "in flat 4+4 space with $m = 2$, $(k_0, k_1, k_2, k_3) = (4, 1, 2, 0)$ "
                "and positive frequency $E = 5$, for random unit vectors $u$ of the "
                "8-dimensional solution space; horizontal axis $\\rho$ in units of "
                "energy per unit volume, vertical axis the count in each of 50 "
                "intervals. Every value equals $E\\,u^\\dagger Bu$; about half are "
                "negative. The possible values fill the whole interval from $-5$ "
                "(reached for $Bu = -u$) to $5$ (for $Bu = u$), but random vectors "
                "seldom come near the two ends: positive frequency does not mean "
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

    - The condensates of dirac16complex00 along the history of the corrected metric
      are $\Phi = e^{a_4/2}b_4^{-1}\chi$, where $\chi$ solves the linear system
      $\chi' = M(x_4)\chi$ with the effective mass $m + \lambda S_0e^{a_4}b_4^{-2}$
      and the gravitational coefficient $c_g = \frac32He^{a_4}b_4^{-1/2}$; they solve
      the field equation with the term $c_g\gamma^{(0)} + v_g\gamma^{(4)}$, and
      $e^{-a_4}b_4^2S$ stays equal to $S_0$, so $S$ is diluted by the 7-volume. A
      condensate oscillates while its effective mass exceeds $c_g$ in size and grows
      while it is smaller; because $c_g$ grows as the block deflates and the
      effective mass approaches $m$, every condensate grows at late times.
    - Their energy density and pressure are $\rho = mS + \frac{\lambda}{2}S^2$ and
      $p = \frac{\lambda}{2}S^2$, the same in all seven directions; the kinetic
      energy density is zero, the kinetic pressure is $(m + \lambda S)S$; the
      $x_4$-$x_0$ component vanishes (record values, computed here anew from the
      solutions).
    - The equation of state is $w = x/(2 + x)$ with $x = \lambda S/m$, measured on
      twelve condensates; $w = -1$ exactly where the effective mass vanishes, and
      such condensates grow at that moment. Along the history $x$ shrinks with
      $S = e^{a_4}b_4^{-2}S_0$, so $w$ of a condensate changes in time and approaches
      0. These are 8-dimensional ratios; what a 3-space observer would infer rests on
      an ASSUMED normalisation of its energy density (Chapter 22).
    - Because $p_3 = p_t = p_0$, a condensate is only diluted,
      $d\rho/dx_4 = -(3a_4' + 4h_4)(\rho + p)$. Toy fluids with $p_3 \neq p_t$ (an
      illustration) show the work of 3-space and of the block together with the
      dilution, and their reversal under $A \to -A$.
    - $S$ and the energy density of the commuting field have no sign: half of all
      random condensates with $\lambda = 0$ have $\rho < 0$, and positive-frequency
      plane waves have $\rho$ anywhere between $-E$ and $E$ (record:
      `commuting_field_energy_unbounded_below`).
    - Status: the condensates (as solutions of the linear system for every $a_4$ and
      $b_4$), their $\rho$ and $p$, the vanishing $x_4$-$x_0$ component, the
      energy-exchange identity and the unbounded energy are PROVED in the Revision
      record (exact, Wolfram and sympy); this notebook re-computes them numerically
      along the history (COMPUTED). The toy fluids are an ILLUSTRATION, not solutions.
      The equation of state of a 3-space observer is not computed here; the Revision
      record computes it under the ASSUMED definitions A, B and C (Chapter 22), and
      which definition describes a physical observer is OPEN. The parameter values
      are choices of this notebook.
    """),
]

if __name__ == "__main__":
    raise SystemExit(run_builder(__file__))
