#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
"""Builder of Notebook 08d, "The rescaling that removes the term, and the growing modes
fed at the fold" (textbook "Universes in Pairs", chapter 08).

The notebook Revision/textbook/notebooks/08d_rescaling_modes.ipynb is BUILT from this file
by Revision/textbook/tools/nbkit.py (never edit the .ipynb by hand):

    python Revision/textbook/tools/nbkit.py build \
        Revision/textbook/notebooks/src/08d_rescaling_modes.py --date YYYY-MM-DD
    python Revision/textbook/tools/nbkit.py check \
        Revision/textbook/notebooks/src/08d_rescaling_modes.py

For the corrected metric of 2026-10-16 (version 2) it reproduces the checks
rescaling_removes_the_connection_term, rescaled_equation_quadratic_potential,
good_sector_x0_independent_modes_without_boundary_condition and
good_sector_hermiticity_up_to_the_brane_flux of Revision/theory/reports/python-scope.json,
covariant_constancy_D_mu_gamma_nu, gamma_mu_Omega_mu_equals_hidden_block_terms and
exact_solution_family_x4_x0 of Revision/theory/reports/python-field-theory.json, and
solution_matrix_square of Revision/theory/reports/wolfram-field-theory.json.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools"))
from nbkit import code, md, run_builder  # noqa: E402

FIGURES = [
    "08d_1_rescaling_factors",
    "08d_2_family_growth",
    "08d_3_growing_finite_norm",
    "08d_4_good_sector_modes",
    "08d_5_norm_and_flux",
]

FACTS = {
    "id": "08d",
    "name": "08d_rescaling_modes",
    "title": "The rescaling that removes the term, and the growing modes fed at the fold",
    "purpose": (
        "For the corrected metric with the two functions a4(x4) and b4(x4) it takes the "
        "spin connection of the diagonal frame from the Revision record and verifies it, "
        "proves exactly that the rescaling Psi = e^(a4/2) b4^(-1) (sin^2 z)^(-1/8) chi "
        "removes the term cg gamma^(x0) + vg gamma^(x4) from the field equation (for 16 "
        "arbitrary component functions) and turns the quadratic potential into the "
        "coupling lambda e^a4 S/(b4^2 |sin z|^(1/2)), verifies the two exact families "
        "of solutions of the record, finds which members have a finite norm and when "
        "they grow along the deflating history, verifies the growing x0-independent "
        "modes of the good sector, proves that the norm of a half cell changes only "
        "through a boundary term at the fold z = pi/2, follows a growing mode through "
        "its onset, and draws five teaching plots."
    ),
    "records": [
        ["Revision/algebra/gammas.json",
         "the author's 16 x 16 gamma matrices and C (read)"],
        ["Revision/theory/field-theory.json",
         "the formula record Omega_components of the spin connection (read and "
         "verified)"],
        ["Revision/kohn_sham/results/parameters.json",
         "the constant H = 1, the tip cutoff L = 3 and the canonical history a4 = A H x4, "
         "b4 = b4(0) e^(beta A H x4) (A = 1, beta = 4/3, b4(0) = 1, a prescribed "
         "background) of the Kohn-Sham record (read)"],
        ["Revision/theory/reports/python-field-theory.json",
         "checks covariant_constancy_D_mu_gamma_nu, "
         "gamma_mu_Omega_mu_equals_hidden_block_terms and exact_solution_family_x4_x0 "
         "(reproduced)"],
        ["Revision/theory/reports/wolfram-field-theory.json",
         "check solution_matrix_square, the reduction of the field equation for the "
         "families (reproduced)"],
        ["Revision/theory/reports/python-scope.json",
         "checks rescaling_removes_the_connection_term, "
         "rescaled_equation_quadratic_potential, "
         "good_sector_x0_independent_modes_without_boundary_condition and "
         "good_sector_hermiticity_up_to_the_brane_flux (reproduced)"],
    ],
    "packages": ["numpy", "sympy", "matplotlib"],
    "needs_rust": [],
    "expected_seconds": 150,
    "timeout_seconds": 900,
    "files_written": ["Revision/textbook/figures/08d.captions.json"]
    + [f"Revision/textbook/figures/{name}.png" for name in FIGURES],
    "final_lines": [
        "PASS the figure file 08d_5_norm_and_flux.png exists",
        "ALL 27 CHECKS PASSED (notebook 08d)",
    ],
    "troubleshooting": [
        ["A cell of section 6, 7 or 10 runs for more than a minute",
         "sympy simplifies the field equation for sixteen arbitrary functions there; on "
         "a slow computer this can take a few minutes. Wait until the star in the "
         "brackets to the left of the cell turns into a number."],
    ],
}

CELLS = [
    md(r"""
    ## 1. What this notebook computes

    In the diagonal frame the field equation of dirac16complex (and of dirac16complex00)
    in the author's corrected metric, with the two functions $a_4(x_4)$ and $b_4(x_4)$,
    contains the term $G\Psi$ with $G = c_g\gamma^{(0)} + v_g\gamma^{(4)}$, $c_g =
    \frac32He^{a_4}b_4^{-1/2}$ and $v_g = b_4'/b_4 - a_4'/2$. This notebook shows,
    exactly, that a change of the field VARIABLES removes it, and then studies the
    fields that depend only on the time $x_4$ and the hidden direction $x_0$: two exact
    families of solutions, their norms near the *tip* $z \to 0$, their growth along the
    deflating history, and the *fold* $z = \pi/2$, where the two halves of a cell meet.
    It

    - takes the spin connection of the diagonal frame from the Revision record and
      verifies it (the gammas are covariantly constant), and recomputes
      $\gamma^\mu\Omega_\mu = G$;
    - proves that for $\Psi = e^{a_4/2}b_4^{-1}(\sin^2 z)^{-1/8}\chi$ the field equation
      becomes $\gamma^\mu\partial_\mu\chi = (m + U')\chi$ with no spin-connection term,
      for sixteen arbitrary component functions, and that the quadratic potential
      turns into the coupling $\lambda e^{a_4}S[\chi]/(b_4^2|\sin z|^{1/2})$;
    - verifies the two exact families of the record, $\Psi = e^{a_4/2}b_4^{-1}
      (\sin^2 z)^{\alpha/2}(\cosh I + \sinh I\,K)\chi_0$ for $m = 0$ and every
      $\alpha$, and the member $\alpha = -\frac14$ for every $m$, and finds which
      members have a finite norm at the tip ($\alpha > -\frac14$) and when they grow
      along the prescribed history (every member with $\alpha \neq -\frac14$, for
      every mass, after a finite time);
    - verifies the growing $x_0$-independent modes of the good sector and shows that
      every mass falls below the growing coefficient $c_g$ on the history;
    - proves that the norm of a field on one half of a cell changes only through a
      boundary term at the fold $z = \pi/2$, and follows a growing mode through its
      onset, whose norm grows exactly as fast as this boundary term feeds it.

    Every exact statement reproduces a check of a Revision record or is labelled as
    this notebook's own exact computation. Five teaching plots.
    """),
    md(r"""
    ## 3. The words used in this notebook

    - **Coordinates** (the author's names, the hidden direction first): $x_0$ the
      hidden direction, $z = 6Hx_0$ taking every real value; $x_1, x_2, x_3$ ordinary
      space (inflating); $x_4$ the time; $x_5, x_6, x_7$ the three extra times
      (time-like, DEFLATING).
    - **Cell, half, fold, tip**: the metric repeats in $z$ with period $\pi$. A *cell*
      $0 < z < \pi$ has two halves, $0 < z < \pi/2$ and $\pi/2 < z < \pi$, which meet
      at the *fold* $z = \pi/2$ ($x_0 = \pi/(12H)$), where $\cos z = 0$, $g_{00} = 0$ and
      $\sqrt{|g|} = 0$. At the *tips* $z = 0$ and $z = \pi$ the factor $\sin z$ vanishes.
    - **Diagonal frame**, scale factors $f_a$: $f_0 = e^{-a_4}b_4^{1/2}\cot z$ (with the
      sign of $\cot z$), $f_{1,2,3} = e^{a_4}$, $f_4 = 1$, $f_{5,6,7} =
      e^{-a_4}b_4^{1/2}W$ with the warp factor $W = (\sin^2 z)^{1/12} > 0$;
      $\gamma^\mu = \gamma^{(\mu)}/f_\mu$; volume factor $\sqrt{|g|} =
      e^{-a_4}b_4^2|\cot z|(\sin^2 z)^{1/4}$.
    - **Spin connection** $\Omega_\mu$ and **covariant derivative** $D_\mu\Psi =
      \partial_\mu\Psi + \Omega_\mu\Psi$; the gammas are *covariantly constant*:
      $\partial_\mu\gamma^\nu + \sum_\lambda\Gamma^\nu{}_{\mu\lambda}\gamma^\lambda +
      \Omega_\mu\gamma^\nu - \gamma^\nu\Omega_\mu = 0$ ($\Gamma$: Christoffel symbols).
      This property fixes $\Omega_\mu$ and is used to verify it.
    - **Rescaling** (a change of field variables): $\Psi = R\,\chi$ with the function
      $R = e^{a_4/2}b_4^{-1}(\sin^2 z)^{-1/8}$.
    - **Bilinear** $S = \bar\Psi\Psi = \Psi^\dagger C\Psi$ and the quadratic potential
      $U = \frac{\lambda}{2}S^2$, $U' = \lambda S$.
    - **Norm** of a field on one half of a cell: $\int\sqrt{|g|}\,\Psi^\dagger\Psi\,
      dx_0$ from the tip to the fold. It is *finite* when the integral does not diverge
      at the tip.
    - **Hidden coordinate** $y = \ln|\sin z|/(6H)$, $dy = \cot z\,dx_0$; $y = 0$ at the
      fold and $y \to -\infty$ at a tip.
    - **History**: the prescribed background $a_4 = AHx_4$, $b_4 = b_4(0)e^{\beta AHx_4}$
      with $A = 1$, $\beta = 4/3$, $b_4(0) = 1$ of the Kohn-Sham record; on it $c_g =
      \frac32He^{Hx_4/3}$ grows and $v_g = \frac56H$.
    - **Good sector**: fields that do not depend on the extra times $x_5, x_6, x_7$.
    - **Mode operator** $h$: the field equation written as $i\,\partial_4\Psi = h\Psi$;
      for fields that depend only on $x_4$ and $x_0$ (and $U = 0$),
      $h = -im\gamma^{(4)} + i\gamma^{(4)}\gamma^{(0)}e^{a_4}b_4^{-1/2}(\tan z\,
      \partial_0 + \frac32H) - iv_g$.
    - **Hermitian, anti-Hermitian**: $M^\dagger = M$ or $M^\dagger = -M$
      ($M^\dagger$: the conjugate transpose).
    - **Boundary term (flux)**: a total derivative $\partial_0(\dots)$ whose integral is
      the difference of its values at the two ends.
    """),
    md(r"""
    ## 4. The physical and mathematical situation

    For a field that depends only on $x_4$ and $x_0$ the field equation (with $U = 0$)
    is $\gamma^{(4)}\partial_4\Psi + e^{a_4}b_4^{-1/2}\tan z\,\gamma^{(0)}\partial_0\Psi
    + c_g\gamma^{(0)}\Psi + v_g\gamma^{(4)}\Psi = m\Psi$. The rescaling works because,
    line by line,

    1. $\partial_0(\sin^2 z)^{-1/8} = -\frac18(\sin^2 z)^{-1/8}\cdot\frac{2\sin z\cos z
       \cdot 6H}{\sin^2 z} = -\frac32H\cot z\,(\sin^2 z)^{-1/8}$ (the power rule and
       the chain rule, with $dz/dx_0 = 6H$);
    2. so $e^{a_4}b_4^{-1/2}\tan z\,\partial_0(\sin^2 z)^{-1/8} = -c_g(\sin^2 z)^{-1/8}$
       (because $\tan z\cot z = 1$);
    3. and $\partial_4(e^{a_4/2}b_4^{-1}) = (\frac12a_4' - b_4'/b_4)\,e^{a_4/2}b_4^{-1} =
       -v_g\,e^{a_4/2}b_4^{-1}$ (the chain rule and the power rule);
    4. so in $\gamma^\mu D_\mu(R\chi)$ the product rule produces exactly $-GR\chi$, which
       cancels the spin-connection term $GR\chi$.

    The weight moves into the measure: $\sqrt{|g|}\,\Psi^\dagger\Psi\,dx_0 =
    |\cot z|\,\chi^\dagger\chi\,dx_0 = \chi^\dagger\chi\,|dy|$.

    Proper lengths along the hidden direction are $\sqrt{g_{00}}\,dx_0 =
    e^{-a_4}b_4^{1/2}|dy|$. So the fold ($y = 0$) lies at a finite proper distance from
    every point, while a tip ($y \to -\infty$) is infinitely far away. The Revision
    record imposes no boundary condition at the fold (the Kohn-Sham record ASSUMES fold
    conditions there for its own model). Without one, the mode operator is symmetric
    only up to a boundary term at the fold, and the good sector contains growing
    modes: this is the second way (besides the extra-time waves) in which the field
    equation as recorded fails to define a stable evolution.

    Every symbol is exact ($H > 0$, $m$, $\alpha$, $\lambda$ letters; $a_4(x_4)$ and
    $b_4(x_4) > 0$ any functions). The history and the plots use $H = 1$.
    """),
    md(r"""
    ## 5. The spin connection from the record, verified

    The next cell first defines two helpers for the checks that reproduce a Revision
    record. `record_says(report, name, ...)` opens the report (a JSON file with a list
    of checks, each with a name, a verdict and a detail text) and is true when the
    check `name` is there with the verdict pass and its detail text contains every
    further piece of text given (for example a value that this notebook computes).
    `check_record(condition, title, report, name, ...)` is the helper `check` for such
    a result: it passes only if the notebook's own computation (`condition`) is right
    AND the record says the same. Then the cell reads the gammas and the formula
    record `Omega_components` of `Revision/theory/field-theory.json` (written in the
    Wolfram language: `g[xi]` is $\gamma^{(x_i)}$, `a4'[x4]` is $a_4'$, `h4` is the rate
    $h_4 = b_4'/(2b_4) - a_4'$ and `sb` is $e^{-a_4}b_4^{1/2}$), enters the same
    formula in sympy, computes the Christoffel symbols of the corrected metric, and
    checks that the gammas are covariantly constant for all 64 pairs $(\mu, \nu)$ and
    that $\gamma^\mu\Omega_\mu = G = c_g\gamma^{(0)} + v_g\gamma^{(4)}$. The warp factor
    is a sympy function class `W` with one rule of its own: the method `fdiff` tells
    sympy that the derivative of `W(x0)` is `H*cot(6*H*x0)*W(x0)`; the cell first checks
    this rule against the explicit $(\sin^2 z)^{1/12}$, whose derivative sympy computes
    itself. The helper `is_zero` asks sympy to simplify twice (the second time with its
    trigonometric simplifier `fu`).
    """),
    code(r'''
    import numpy as np  # numbers and matrices (for the plots)
    import sympy as sp  # exact algebra with symbols

    REPORTS = {}  # report file -> {check name: (verdict, detail)}, each read once


    def record_says(report_file, check_name, *pieces):
        """True when the Revision report records the check check_name with the verdict
        pass and its detail text contains every given piece of text."""
        if report_file not in REPORTS:  # read the report the first time it is needed
            data = json.loads(repository_file(report_file).read_text(encoding="utf-8"))
            REPORTS[report_file] = {entry["name"]: (entry["verdict"].lower(),
                                                    entry["detail"])
                                    for entry in data["checks"]}
        verdict, detail = REPORTS[report_file][check_name]
        return verdict == "pass" and all(piece in detail for piece in pieces)


    def check_record(condition, title, report_file, check_name, *pieces):
        """check() for a result that reproduces the Revision check check_name: it passes
        only if condition is true AND the report records check_name as passed, with
        every piece of text (values computed here) in its detail."""
        on_record = record_says(report_file, check_name, *pieces)
        check(condition and on_record, title,
              record=f"{report_file}, check {check_name}")


    THEORY = "Revision/theory/reports/python-field-theory.json"  # the sympy records
    SCOPE = "Revision/theory/reports/python-scope.json"
    gammas_record = json.loads(
        repository_file("Revision/algebra/gammas.json").read_text(encoding="utf-8"))
    G = [sp.Matrix(rows) for rows in gammas_record["gamma"]]  # gamma^(x0) ... (x7)
    ETA = gammas_record["eta"]  # [1, 1, 1, 1, -1, -1, -1, -1]
    C = sp.Matrix(gammas_record["C"])  # C = gamma^(x0) gamma^(x1) gamma^(x2) gamma^(x3)
    theory = json.loads(
        repository_file("Revision/theory/field-theory.json").read_text(encoding="utf-8"))
    formulas = {entry["key"]: entry for entry in theory["formulas"]}
    say("record Omega_components: " + formulas["Omega_components"]["wl"])

    x = sp.symbols("x0:8", real=True)  # the coordinates; x[k] is xk
    x0, x4 = x[0], x[4]  # the hidden direction and the time
    H = sp.Symbol("H", positive=True)
    m = sp.Symbol("m", real=True)
    a4 = sp.Function("a4", real=True)(x4)  # any real function of the time x4
    b4 = sp.Function("b4", positive=True)(x4)  # any positive function of x4
    a4_prime, b4_prime = sp.diff(a4, x4), sp.diff(b4, x4)
    z = 6 * H * x0  # every real value


    class W(sp.Function):
        """The warp factor W(x0) = (sin(6 H x0)^2)^(1/12) > 0 of the extra times."""

        def fdiff(self, argindex=1):
            """dW/dx0 = H cot(6 H x0) W, for every real z = 6 H x0 with sin z != 0."""
            return H * sp.cot(6 * H * self.args[0]) * self

        def _eval_is_positive(self):
            return True  # the positive root


    def is_zero(expr):
        """True when sympy shows that expr is exactly zero (two simplifications)."""
        expr = sp.sympify(expr)
        if expr == 0:
            return True
        simpler = sp.simplify(expr)
        return simpler == 0 or sp.simplify(sp.fu(simpler)) == 0


    explicit = (sp.sin(z) ** 2) ** sp.Rational(1, 12)  # the twelfth root, written out
    check(is_zero(sp.diff(explicit, x0) - H * sp.cot(z) * explicit),
          "the derivative of (sin^2 z)^(1/12) is H cot z (sin^2 z)^(1/12): the rule of W")
    s_b = sp.exp(-a4) * sp.sqrt(b4)  # the scale of the hidden block e^(-a4) b4^(1/2)
    f = [s_b * sp.cot(z)] + [sp.exp(a4)] * 3 + [sp.Integer(1)] \
        + [s_b * W(x0)] * 3  # the frame factors f_0, ..., f_7
    g = [ETA[a] * f[a] ** 2 for a in range(8)]  # the diagonal metric
    gamma_up = [G[mu] / f[mu] for mu in range(8)]  # gamma^mu = gamma^(mu) / f_mu
    h4 = b4_prime / (2 * b4) - a4_prime  # the rate of the hidden block
    Omega = [sp.zeros(16, 16) for _ in range(8)]  # Omega_x4 stays zero
    Omega[0] = h4 * s_b * sp.cot(z) * G[0] * G[4] / 2  # the hidden direction x0
    for i in (1, 2, 3):  # x1, x2, x3 (inflating)
        Omega[i] = a4_prime * sp.exp(a4) * G[i] * G[4] / 2
    for t in (5, 6, 7):  # x5, x6, x7 (deflating extra times)
        Omega[t] = W(x0) * (h4 * s_b * G[4] * G[t] + H * G[0] * G[t]) / 2

    Gam = [[[sp.Integer(0)] * 8 for _ in range(8)] for _ in range(8)]
    for lam in range(8):  # Christoffel symbols of the diagonal metric
        for mu in range(8):
            for nu in range(8):
                value = 0
                if lam == nu:
                    value += sp.diff(g[lam], x[mu])
                if lam == mu:
                    value += sp.diff(g[lam], x[nu])
                if mu == nu:
                    value -= sp.diff(g[mu], x[lam])
                if value != 0:
                    Gam[lam][mu][nu] = sp.simplify(value / (2 * g[lam]))
    constant = all(
        all(is_zero(v) for v in sp.diff(gamma_up[nu], x[mu])
            + sum((Gam[nu][mu][lam] * gamma_up[lam] for lam in range(8)), sp.zeros(16, 16))
            + Omega[mu] * gamma_up[nu] - gamma_up[nu] * Omega[mu])
        for mu in range(8) for nu in range(8))
    check_record(constant, "the record's Omega_mu makes every gamma^nu covariantly "
                 "constant (64 pairs)", THEORY, "covariant_constancy_D_mu_gamma_nu",
                 "= 0 for all 64 (mu, nu)")
    c_g = sp.Rational(3, 2) * H * sp.exp(a4) / sp.sqrt(b4)  # (3/2) H e^a4 b4^(-1/2)
    v_g = b4_prime / b4 - a4_prime / 2  # b4'/b4 - a4'/2
    gamma_Omega = sum((gamma_up[mu] * Omega[mu] for mu in range(8)), sp.zeros(16, 16))
    check_record(all(is_zero(v) for v in gamma_Omega - c_g * G[0] - v_g * G[4]),
                 "gamma^mu Omega_mu = c_g gamma^(x0) + v_g gamma^(x4) (diagonal frame)",
                 THEORY, "gamma_mu_Omega_mu_equals_hidden_block_terms",
                 "gamma^mu Omega_mu = (3/2) H e^a4 b4^(-1/2) gamma^(x0) + (b4'/b4 - "
                 "a4'/2) gamma^(x4) exactly")
    '''),
    md(r"""
    ## 6. The rescaling removes the term

    The next cell checks the two one-line identities $(1/f_0)\,\partial_0R = -c_gR$
    and $\partial_4R = -v_gR$ for $R = e^{a_4/2}b_4^{-1}(\sin^2 z)^{-1/8} =
    e^{a_4/2}b_4^{-1}W^{-3/2}$, and then the full statement on sixteen ARBITRARY component
    functions $\chi_A(x_0, \dots, x_7)$ (sympy `Function` objects, about which nothing is
    assumed): $\gamma^\mu D_\mu(R\chi) - R\,\gamma^\mu\partial_\mu\chi = 0$ for all 16
    components. Then it checks the potential: $S[R\chi] = R^2S[\chi] =
    e^{a_4}b_4^{-2}|\sin z|^{-1/2}S[\chi]$ ($R$ is real), so $\lambda S[\Psi]\Psi =
    R\,\frac{\lambda e^{a_4}S[\chi]}{b_4^2|\sin z|^{1/2}}\chi$, and the measure:
    $\sqrt{|g|}\,R^2 = |\cot z| = |dy/dx_0|$. The symbol `sigma` is the sign of
    $\cot z$ ($+1$ on the first half of a cell, $-1$ on the second), so that
    $\sqrt{|g|} = \sigma e^{-a_4}b_4^2\cot z\,W^3$.
    """),
    code(r'''
    R = sp.exp(a4 / 2) / b4 * W(x0) ** sp.Rational(-3, 2)  # the rescaling factor
    check_record(is_zero(sp.diff(R, x0) / f[0] + c_g * R)
                 and is_zero(sp.diff(R, x4) + v_g * R),
                 "(1/f0) d0 R = -c_g R and d4 R = -v_g R for R = e^(a4/2) b4^(-1) "
                 "(sin^2 z)^(-1/8)", SCOPE, "rescaling_removes_the_connection_term",
                 "the x0 terms: e^a4 b4^(-1/2) tan z (-(3/2) H cot z) + cg = 0; "
                 "the x4 terms: a4'/2 - b4'/b4 + vg = 0")
    chi = sp.Matrix([sp.Function(f"chi{A}")(*x) for A in range(1, 17)])  # arbitrary
    Psi = R * chi
    D_Psi = sum((gamma_up[mu] * (sp.diff(Psi, x[mu]) + Omega[mu] * Psi)
                 for mu in range(8)), sp.zeros(16, 1))  # gamma^mu D_mu Psi
    D_chi = sum((gamma_up[mu] * sp.diff(chi, x[mu]) for mu in range(8)),
                sp.zeros(16, 1))  # gamma^mu d_mu chi (no connection)
    check_record(all(is_zero(v) for v in D_Psi - R * D_chi),
                 "gamma^mu D_mu (R chi) = R gamma^mu d_mu chi for 16 arbitrary functions",
                 SCOPE, "rescaling_removes_the_connection_term",
                 "In the variables chi the field equation has no spin-connection term: "
                 "gamma^mu d_mu chi = (m + U'(S)) chi")
    lam, S_chi = sp.symbols("lambda S_chi", real=True)  # S_chi stands for S[chi]
    S_Psi = R**2 * S_chi  # S[R chi] = (R chi)^dagger C (R chi) = R^2 S[chi]
    abs_sin = sp.Abs(sp.sin(z))  # |sin z|
    coupling = sp.exp(a4) * S_chi / (b4**2 * abs_sin ** sp.Rational(1, 2))
    check_record(is_zero((lam * S_Psi).subs(W(x0), abs_sin ** sp.Rational(1, 6))
                         - lam * coupling),
                 "U = (lambda/2) S^2: lambda S[Psi] = lambda e^a4 S[chi]/(b4^2 "
                 "|sin z|^(1/2)) (the new coupling)", SCOPE,
                 "rescaled_equation_quadratic_potential",
                 "S[Psi] = Psi^dagger C Psi = e^a4 b4^(-2) |sin z|^(-1/2) S[chi]",
                 "gamma^mu d_mu chi = (m + lambda e^a4 S[chi]/(b4^2 |sin z|^(1/2))) chi")
    sigma = sp.Symbol("sigma", real=True)  # the sign of cot z (+1 or -1)
    sqrt_g = sigma * sp.exp(-a4) * b4**2 * sp.cot(z) * W(x0) ** 3  # the volume factor
    y_of_x0 = sp.log(sp.sin(z) ** 2) / (12 * H)  # y = ln|sin z|/(6 H)
    check(is_zero(sqrt_g * R**2 - sigma * sp.cot(z)) and
          is_zero(sp.diff(y_of_x0, x0) - sp.cot(z)),
          "sqrt|g| R^2 = |cot z| = |dy/dx0|: the norm of Psi is the y-norm of chi")
    '''),
    md(r"""
    The next cell draws the factor $(\sin^2 z)^{-1/8}$ of the rescaling and the factor
    $|\sin z|^{-1/2}$ of the new coupling across one cell $0 < z < \pi$, in the units
    $e^{a_4/2}b_4^{-1}$ and $e^{a_4}b_4^{-2}$ (their parts that depend on the time), and
    the hidden coordinate $y = \ln|\sin z|/(6H)$, for $H = 1$. It reads $H$ and the tip
    cutoff $L$ of the Kohn-Sham record (that record cuts the hidden direction at
    $y = -L$) and computes where the cutoff lies in $z$: $y = -L$ means $\ln(\sin z) =
    -6HL$, so $\sin z = e^{-6HL}$ and $z_{\rm cut} = \arcsin(e^{-6HL})$. This number is
    tiny, so the right panel uses a logarithmic $z$ axis: on it $y$ is almost a straight
    line, because $\sin z \approx z$ for small $z$ and then $y \approx \ln(z)/(6H)$.
    """),
    code(r'''
    parameters = json.loads(repository_file(
        "Revision/kohn_sham/results/parameters.json").read_text(encoding="utf-8"))
    H_record = parameters["physics"]["H"]  # the author's constant H of the record
    L_tip = parameters["physics"]["L_tipCutoff"]  # the record cuts the tip at y = -L
    z_cut = np.arcsin(np.exp(-6 * H_record * L_tip))  # the z at which y = -L
    report("H and the tip cutoff L of the Kohn-Sham record", f"{H_record}, {L_tip}")
    report("z at the tip cutoff, arcsin(e^(-6 H L))", f"{z_cut:.6e}")
    check(H_record == 1.0 and abs(np.log(np.sin(z_cut)) / (6 * H_record) + L_tip) < 1e-12,
          "the record has H = 1, and y(z_cut) = -L",
          record="Revision/kohn_sham/results/parameters.json, physics.H, "
                 "physics.L_tipCutoff")
    zs = np.linspace(0.01, np.pi - 0.01, 600)  # one cell, tips at 0 and pi
    fig, (left, right) = plt.subplots(1, 2, figsize=(10.0, 4.0))
    left.plot(zs, (np.sin(zs) ** 2) ** (-1 / 8), label="rescaling $(\\sin^2 z)^{-1/8}$")
    left.plot(zs, np.abs(np.sin(zs)) ** -0.5, "--", label="coupling $|\\sin z|^{-1/2}$")
    left.axvline(np.pi / 2, color="gray", linewidth=0.8)  # the fold
    left.set_yscale("log")
    left.set_xlabel("$z = 6Hx_0$ over one cell (fold at $\\pi/2$)")
    left.set_ylabel("factor (units $e^{a_4/2}b_4^{-1}$, $e^{a_4}b_4^{-2}$)")
    left.set_title("$\\Psi = e^{a_4/2}b_4^{-1}(\\sin^2 z)^{-1/8}\\chi$")
    left.legend(loc="upper center")
    mantissa, exponent = f"{z_cut:.1e}".split("e")  # "1.5e-08" -> "1.5" and "-08"
    exponent = int(exponent)  # -8, for the caption
    z_log = np.logspace(-10.0, np.log10(np.pi / 2), 400)  # 10^-10 ... pi/2, log spaced
    right.semilogx(z_log, np.log(np.sin(z_log)) / (6 * H_record), color="tab:green")
    right.axhline(-L_tip, color="gray", linestyle=":", linewidth=0.9)
    right.plot([z_cut], [-L_tip], "o", color="black")  # where y reaches the cutoff
    right.text(2e-8, -L_tip + 0.15, "tip cutoff $y = -L$ of the Kohn-Sham record",
               fontsize=8)
    right.set_xlabel("$z = 6Hx_0$ (logarithmic axis), first half of a cell")
    right.set_ylabel("$y = \\ln|\\sin z|/(6H)$")
    right.set_title("The hidden coordinate $y$, $H = 1$")
    save_figure(fig, "rescaling_factors",
                "Left, on a logarithmic axis, against $z = 6Hx_0$ across one cell from "
                "the tip near 0 through the fold ($\\pi/2$, gray line) to the tip near "
                "$\\pi$, at one time: the factor $(\\sin^2 z)^{-1/8}$ (solid) of the "
                "rescaling $\\Psi = e^{a_4/2}b_4^{-1}(\\sin^2 z)^{-1/8}\\chi$, which "
                "removes the term $c_g\\gamma^{(0)} + v_g\\gamma^{(4)}$, and the factor "
                "$|\\sin z|^{-1/2}$ (dashed) of the new coupling $\\lambda e^{a_4}"
                "S_\\chi/(b_4^2|\\sin z|^{1/2})$; both equal 1 at the fold and diverge at "
                "the tips, the same on both halves. Right: the hidden coordinate $y = "
                "\\ln|\\sin z|/(6H)$ for $H = 1$, in which the norm of $\\Psi$ is "
                "$\\int\\chi^\\dagger\\chi\\,|dy|$, against $z$ on a logarithmic axis; "
                "$y = 0$ at the fold and $y \\to -\\infty$ at the tip. Dotted: the cutoff "
                f"$y = -L = {-L_tip:g}$ of the Kohn-Sham record, reached only at "
                f"$z = \\arcsin(e^{{{-6 * H_record * L_tip:g}}}) \\approx {mantissa} "
                f"\\times 10^{{{exponent}}}$ (black dot).")
    '''),
    md(r"""
    ## 7. Two exact families of solutions

    For $U = 0$ and a field $\Psi = F\,(\sin^2 z)^{\alpha/2}\,\Phi(x_4)$ with $F =
    e^{a_4/2}b_4^{-1}$, a real exponent $\alpha$ and a column $\Phi$ of 16 functions of
    the time, the field equation reduces to an equation in $x_4$ alone. With $K =
    \gamma^{(4)}\gamma^{(0)}$ ($K^2 = 1$, $K\gamma^{(4)} = -\gamma^{(4)}K$) and
    $\mu_A = (4\alpha + 1)c_g = \frac32H(4\alpha + 1)e^{a_4}b_4^{-1/2}$ the record finds
    $\gamma^\mu D_\mu\Psi - m\Psi = F(\sin^2 z)^{\alpha/2}\gamma^{(4)}\big[\Phi' -
    (-m\gamma^{(4)} + \mu_AK)\Phi\big]$, so $\Psi$ solves the field equation exactly when
    $\Phi' = (-m\gamma^{(4)} + \mu_AK)\Phi$. Two cases can be solved in closed form for
    EVERY $a_4$ and $b_4$: (i-a) $m = 0$, every $\alpha$: $\Phi = (\cosh I + \sinh I\,K)
    \chi_0$ with a constant column $\chi_0$ and $I' = \mu_A$ (because $K^2 = 1$, the
    exponential series of $IK$ sorts into cosh and sinh); (i-b) $\alpha = -\frac14$
    ($\mu_A = 0$), every $m$: $\Phi = (\cos(mx_4) - \sin(mx_4)\gamma^{(4)})\chi_0$. The
    next cell checks the matrix facts, the factor rules $F'/F = -v_g$ and $(1/f_0)
    \partial_0(\sin^2 z)^{\alpha/2} = 4\alpha c_g(\sin^2 z)^{\alpha/2}$, the reduction
    for sixteen arbitrary functions $\Phi_A(x_4)$, both families (with all eight
    directions and the spin connection of section 5, for symbolic $\alpha$, $m$, $H$
    and all functions $a_4$ and $b_4$), and that the matrix $M(x_4) = -m\gamma^{(4)} +
    \mu_AK$ of two different times does not commute with itself when $m \neq 0$ and
    $\mu_A$ changes: then the exponential trick fails, which is why the other members
    have no closed form.
    """),
    code(r'''
    K = G[4] * G[0]  # K = gamma^(x4) gamma^(x0)
    F = sp.exp(a4 / 2) / b4  # the scalar factor F = e^(a4/2) b4^(-1)
    alpha = sp.Symbol("alpha", real=True)
    mu_A = (4 * alpha + 1) * c_g  # (3/2) H (4 alpha + 1) e^a4 b4^(-1/2)
    power = W(x0) ** (6 * alpha)  # (sin^2 z)^(alpha/2) = W^(6 alpha)
    K_facts = (K * K == sp.eye(16) and K * G[4] + G[4] * K == sp.zeros(16, 16)
               and K.T * C + C * K == sp.zeros(16, 16))
    factor_rules = (is_zero(sp.diff(F, x4) / F + v_g)
                    and is_zero(sp.diff(power, x0) / f[0] - 4 * alpha * c_g * power))
    Phi = sp.Matrix([sp.Function(f"phi{A}")(x4) for A in range(1, 17)])  # arbitrary
    Psi_red = F * power * Phi
    left_side = sum((gamma_up[mu] * (sp.diff(Psi_red, x[mu]) + Omega[mu] * Psi_red)
                     for mu in range(8)), sp.zeros(16, 1)) - m * Psi_red
    right_side = F * power * G[4] * (sp.diff(Phi, x4) - (-m * G[4] + mu_A * K) * Phi)
    check_record(K_facts and factor_rules
                 and all(is_zero(v) for v in left_side - right_side),
                 "K^2 = 1, {K, g4} = 0, K^T C + C K = 0; Psi = F (sin^2 z)^(alpha/2) Phi "
                 "solves the equation iff Phi' = (-m g4 + mu_A K) Phi",
                 "Revision/theory/reports/wolfram-field-theory.json",
                 "solution_matrix_square",
                 "K = gamma^(x4) gamma^(x0) satisfies K^2 = I16, {K, gamma^(x4)} = 0",
                 "chi' = (-V gamma^(x4) + muA K) chi, muA = (3/2) H (4 al + 1) E^a4 "
                 "b4^(-1/2)")
    I_x4 = sp.Function("I")(x4)  # any function with I' = mu_A
    chi0 = sp.Matrix(sp.symbols("q1:17"))  # 16 arbitrary constants
    family_a = F * power * (sp.cosh(I_x4) * chi0 + sp.sinh(I_x4) * (K * chi0))
    residual_a = sum((gamma_up[mu] * (sp.diff(family_a, x[mu]) + Omega[mu] * family_a)
                      for mu in range(8)), sp.zeros(16, 1))
    residual_a = residual_a.subs(sp.Derivative(I_x4, x4), mu_A)  # I' = mu_A
    check_record(all(is_zero(v) for v in residual_a),
                 "(i-a) m = 0: F (sin^2 z)^(alpha/2) (cosh I + sinh I K) chi0 with I' = "
                 "mu_A solves the equation", THEORY, "exact_solution_family_x4_x0",
                 "(i-a) m = 0, alpha arbitrary: Psi = F (sin^2 z)^(alpha/2) (cosh I + "
                 "sinh I K) chi with I' = (3/2) H (4 alpha + 1) e^a4 b4^(-1/2) solves "
                 "gamma^mu D_mu Psi = 0 exactly")
    family_b = F * W(x0) ** sp.Rational(-3, 2) * (sp.cos(m * x4) * chi0
                                                  - sp.sin(m * x4) * (G[4] * chi0))
    residual_b = sum((gamma_up[mu] * (sp.diff(family_b, x[mu]) + Omega[mu] * family_b)
                      for mu in range(8)), sp.zeros(16, 1)) - m * family_b
    check_record(all(is_zero(v) for v in residual_b),
                 "(i-b) alpha = -1/4: F (sin^2 z)^(-1/8) (cos(m x4) - sin(m x4) g4) chi0 "
                 "solves the equation", THEORY, "exact_solution_family_x4_x0",
                 "(i-b) alpha = -1/4, m arbitrary: Psi = F (sin^2 z)^(-1/8) (cos(m x4) - "
                 "sin(m x4) gamma^(x4)) chi solves gamma^mu D_mu Psi = m Psi exactly")
    mu_1, mu_2 = sp.symbols("mu1 mu2", real=True)  # the values of mu_A at two times
    M_1, M_2 = -m * G[4] + mu_1 * K, -m * G[4] + mu_2 * K
    square_ok = (M_1 * M_1 - (mu_1**2 - m**2) * sp.eye(16)).applyfunc(sp.expand) \
        == sp.zeros(16, 16)
    commutator_ok = (M_1 * M_2 - M_2 * M_1 - 2 * m * (mu_1 - mu_2) * G[4] * K).applyfunc(
        sp.expand) == sp.zeros(16, 16)
    check_record(square_ok and commutator_ok,
                 "M^2 = (mu_A^2 - m^2) I16; [M(1), M(2)] = 2 m (mu1 - mu2) g4 K is not 0",
                 THEORY, "exact_solution_family_x4_x0",
                 "For m != 0 and alpha != -1/4 the reduced system chi' = (-m gamma^(x4) + "
                 "muA K) chi has no closed form for general a4, b4 (muA varies with x4)")
    '''),
    md(r"""
    ## 8. Which members have a finite norm, and when they grow

    The norm of a member on the first half of a cell is a function of $x_4$ times
    $\int_0^{\pi/(12H)}\sqrt{|g|}\,F^2(\sin^2 z)^{\alpha}\,dx_0 = \int_0^{\pi/(12H)}
    \cot z\,\sin^{p}z\,dx_0$ with $p = 2\alpha + \frac12$ (the factors $e^{-a_4}b_4^2$
    of the volume and $e^{a_4}b_4^{-2}$ of $F^2$ cancel; $\sin z > 0$ and $\cot z > 0$
    there). An antiderivative is $\sin^pz/(6Hp)$, so for $p > 0$ the integral is
    $\frac{1}{6Hp} = \frac{1}{3H(4\alpha + 1)}$, and for $p \le 0$ it diverges at the
    tip (for $p = 0$, $\alpha = -\frac14$, the antiderivative is $\ln(\sin z)/(6H)$). So
    the members with a finite norm are exactly those with $\alpha > -\frac14$, and the
    member without $H$, $\alpha = -\frac14$, has an infinite norm. Growth: with frozen
    time the matrix $M$ has $M^2 = (\mu_A^2 - m^2)\,I_{16}$, so the instantaneous growth
    rate is $\sqrt{\mu_A^2 - m^2}$ where $\mu_A^2 > m^2$. On the history $\mu_A =
    \frac32H(4\alpha + 1)e^{Hx_4/3}$ grows without bound for every $\alpha \neq
    -\frac14$, so it overtakes every mass $m > 0$ at the time $x_4 = (3/H)\ln\big(2m/(3H
    |4\alpha + 1|)\big)$; for $m = 0$ the exact family (i-a) grows like $e^{I(x_4)}$
    with $I(x_4) = \int_0^{x_4}\mu_A = \frac92(4\alpha + 1)(e^{Hx_4/3} - 1)$, faster than
    any exponential. The next cell checks these statements (the record states the case
    $\alpha = 0$, with the norm factor $1/(3H)$) and draws them.
    """),
    code(r'''
    p = 2 * alpha + sp.Rational(1, 2)  # the power of sin z in the norm density
    antiderivative = sp.sin(z) ** p / (6 * H * p)
    density = sp.cot(z) * sp.sin(z) ** p  # first half of a cell: sin z > 0, cot z > 0
    log_antiderivative = sp.log(sp.sin(z)) / (6 * H)  # the case p = 0
    eps = sp.Symbol("epsilon", positive=True)
    norm_factor = (antiderivative.subs(x0, sp.pi / (12 * H))
                   - antiderivative.subs(x0, 0)).subs(alpha, 0)  # the case alpha = 0
    say(f"norm factor of the member alpha = 0: {sp.sstr(sp.simplify(norm_factor))}")
    norm_ok = (is_zero(sp.diff(antiderivative, x0) - density)
               and is_zero(sp.diff(log_antiderivative, x0) - sp.cot(z))
               and sp.limit(log_antiderivative.subs(x0, eps), eps, 0, "+") == -sp.oo
               and sp.simplify(norm_factor - 1 / (3 * H)) == 0)
    check_record(norm_ok, "norm factor 1/(3 H (4 alpha + 1)) for alpha > -1/4, 1/(3 H) "
                 "at alpha = 0; infinite at alpha = -1/4", SCOPE,
                 "good_sector_x0_independent_modes_without_boundary_condition",
                 "int_0^(pi/(12 H)) cot(6 H x0) sin(6 H x0)^(1/2) dx0 = "
                 f"{sp.sstr(sp.simplify(norm_factor))}")

    # The record's numbers as exact fractions (nsimplify turns 1.3333333333333333 into 4/3):
    A_record = sp.nsimplify(parameters["physics"]["historyA"])  # a4 = A H x4 ...
    beta_record = sp.nsimplify(parameters["physics"]["historyBeta"])  # b4 = e^(beta ...)
    b4_zero = sp.nsimplify(parameters["physics"]["historyB4AtZero"])  # b4(0) = 1
    history = {a4: A_record * H * x4, b4: b4_zero * sp.exp(beta_record * A_record * H * x4)}
    mu_history = sp.simplify(mu_A.subs(history).doit())
    say(f"mu_A on the history: {mu_history}")
    m_positive = sp.Symbol("m", positive=True)
    onset = 3 * sp.log(2 * m_positive / (3 * H * (4 * alpha + 1))) / H  # mu_A = m there
    s_var = sp.Symbol("s", real=True)
    I_history = sp.integrate(mu_history.subs(x4, s_var), (s_var, 0, x4))
    check(is_zero(mu_history - sp.Rational(3, 2) * H * (4 * alpha + 1) * sp.exp(H * x4 / 3))
          and is_zero(mu_history.subs(x4, onset) - m_positive),
          "on the history mu_A = (3/2) H (4 alpha + 1) e^(H x4/3); it reaches every m > 0 "
          "at x4 = (3/H) ln(2 m/(3 H (4 alpha + 1)))")
    I_expected = sp.Rational(9, 2) * (4 * alpha + 1) * (sp.exp(H * x4 / 3) - 1)
    check(is_zero(I_history - I_expected),
          "m = 0: I(x4) = (9/2)(4 alpha + 1)(e^(H x4/3) - 1), so e^I grows faster than "
          "any exponential")

    times = np.linspace(-3.0, 6.0, 451)
    fig, (left, right) = plt.subplots(1, 2, figsize=(10.0, 4.2))
    for a_value, style in ((0.0, "-"), (0.5, "--"), (1.0, ":")):
        left.semilogy(times, 1.5 * (4 * a_value + 1) * np.exp(times / 3), style,
                      label=f"$\\mu_A$, $\\alpha = {a_value:g}$")
    for mass_value in (1.0, 2.0, 4.0):
        left.axhline(mass_value, color="gray", linewidth=0.8)
        left.text(-2.9, mass_value * 1.08, f"$m = {mass_value:g}$", fontsize=8)
    left.set_xlabel("time $x_4$ (units of $1/H$)")
    left.set_ylabel("$\\mu_A = \\frac{3}{2}H(4\\alpha + 1)e^{Hx_4/3}$ (units of $H$)")
    left.set_title("The coefficient overtakes every mass")
    left.legend(fontsize=8, loc="lower right")
    late = np.linspace(0.0, 15.0, 301)
    for a_value, style in ((0.0, "-"), (0.5, "--"), (1.0, ":")):
        exponent_I = 4.5 * (4 * a_value + 1) * (np.exp(late / 3) - 1)
        right.semilogy(late[1:], exponent_I[1:] / np.log(10.0), style,
                       label=f"$\\alpha = {a_value:g}$")
    right.semilogy(late[1:], late[1:] / np.log(10.0), color="gray", linewidth=0.8,
                   label="$e^{x_4}$ for comparison")
    right.set_xlabel("time $x_4$ (units of $1/H$)")
    right.set_ylabel("$\\log_{10}$ of the growth factor $e^{I}$")
    right.set_title("$m = 0$: the exact members (i-a)")
    right.legend(fontsize=8);
    save_figure(fig, "family_growth",
                "Left: the coefficient $\\mu_A = \\frac32H(4\\alpha + 1)e^{Hx_4/3}$ of "
                "the reduced equation $\\Phi' = (-m\\gamma^{(4)} + \\mu_AK)\\Phi$ along "
                "the history $a_4 = x_4$, $b_4 = e^{4x_4/3}$ ($H = 1$) for the exponents "
                "$\\alpha = 0, 0.5, 1$, against the time $x_4$, on a logarithmic axis; "
                "where it crosses the gray line of a mass $m$, the instantaneous rate "
                "$\\sqrt{\\mu_A^2 - m^2}$ becomes real and the member starts to grow, "
                "so every mass is overtaken after a finite time. Right: the base-10 "
                "logarithm of the growth factor $e^{I}$, $I = \\frac92(4\\alpha + 1)"
                "(e^{x_4/3} - 1)$, of the exact massless members (i-a), on a logarithmic "
                "axis: the curves approach straight lines, so the growth factor is a "
                "double exponential, faster than any exponential (gray: the "
                "exponential $e^{x_4}$, whose curve bends down).")
    '''),
    md(r"""
    The next cell draws the same information in the plane of the mass $m/H$ and the
    exponent $\alpha$: the colour is the time at which $\mu_A^2 = m^2$ on the history,
    $x_4 = (3/H)\ln\big(2m/(3H|4\alpha + 1|)\big)$ (a negative time: the member grows
    already at $x_4 = 0$); the hatched band $\alpha \le -\frac14$ has an infinite norm
    at the tip, and on the line $\alpha = -\frac14$ the member never grows (it
    oscillates with frequency $m$). The red line $\alpha = 0$ is the family of the
    $x_0$-independent modes of section 9.
    """),
    code(r'''
    masses = np.linspace(0.05, 6.0, 240)
    A_grid, M_grid = np.meshgrid(np.linspace(-1.0, 1.5, 251), masses)
    coefficient = 1.5 * np.abs(4 * A_grid + 1)  # |mu_A| at x4 = 0, H = 1
    with np.errstate(divide="ignore"):
        onset_grid = 3 * np.log(M_grid / coefficient)  # the time at which mu_A^2 = m^2
    fig, ax = plt.subplots(figsize=(6.6, 4.8))
    shown = np.clip(onset_grid, -6.0, 9.0)
    image = ax.pcolormesh(M_grid, A_grid, shown, cmap="viridis", shading="auto")
    fig.colorbar(image, ax=ax, label="onset time $x_4$ (units of $1/H$)")
    ax.contour(M_grid, A_grid, onset_grid, levels=[0.0], colors="white", linewidths=1.0)
    ax.axhspan(-1.0, -0.25, facecolor="none", edgecolor="white", hatch="//",
               linewidth=0.0)
    ax.axhline(-0.25, color="black", linewidth=1.2)
    ax.axhline(0.0, color="tab:red", linewidth=1.2)
    ax.text(0.2, -0.6, "infinite norm at the tip", fontsize=9, color="white",
            bbox={"facecolor": "black", "alpha": 0.5, "edgecolor": "none"})
    ax.text(3.2, 0.05, "$\\alpha = 0$", fontsize=8, color="tab:red")
    ax.set_xlabel("mass $m$ (units of $H$)")
    ax.set_ylabel("exponent $\\alpha$")
    ax.set_title("When the members start to grow on the history")
    finite = np.isfinite(onset_grid) | (np.abs(4 * A_grid + 1) < 1e-12)
    early = float(np.mean((onset_grid < 0.0) & (A_grid > -0.25)))
    report("fraction of the rectangle with finite norm that grows already at x4 = 0",
           f"{early:.4f}")
    check(bool(np.all(finite)), "every drawn member with alpha != -1/4 starts to grow "
          "at a finite time")
    save_figure(fig, "growing_finite_norm",
                "The plane of the mass $m$ (horizontal, units of $H$) and the exponent "
                "$\\alpha$ (vertical) of the members $e^{a_4/2}b_4^{-1}(\\sin^2 z)^"
                "{\\alpha/2}\\Phi(x_4)$, coloured by the time at which their "
                "instantaneous growth rate becomes real on the history $a_4 = x_4$, "
                "$b_4 = e^{4x_4/3}$ ($H = 1$), $x_4 = 3\\ln(2m/(3|4\\alpha + 1|))$, "
                "clipped to the range from $-6$ to $9$. Left of the white curve the "
                "member grows already at $x_4 = 0$. Hatched: $\\alpha < -1/4$, infinite "
                "norm at the tip; on the black line $\\alpha = -1/4$ the member never "
                "grows. Red: the $x_0$-independent modes ($\\alpha = 0$). Every member "
                "with a finite norm starts to grow after a finite time, for every mass.")
    '''),
    md(r"""
    ## 9. The $x_0$-independent modes of the good sector

    On fields that depend only on $x_4$ (good sector, $\alpha = 0$) the mode operator
    of section 3 acts as $A - iv_g$ with the matrix $A = -im\gamma^{(4)} +
    ic_g\gamma^{(4)}\gamma^{(0)}$; for $\Psi = F\chi$ the term $-iv_g$ is absorbed by
    the factor (as in section 6), and $i\,\partial_4\chi = A\chi$ is the reduced
    equation of section 7 at $\alpha = 0$, because $A = iM$ with $\mu_A = c_g$. The next
    cell checks this action on sixteen arbitrary functions of $x_4$, that $A$ is not
    Hermitian, that $A^2 = (m^2 - c_g^2)I_{16}$, that on the history $c_g = \frac32
    He^{Hx_4/3}$, and that at $m = H = 1$ and $x_4 = 0$ the eigenvalues are $\pm
    \frac{\sqrt5}{2}\,i$ (eight each; a solution with $e^{-iEx_4}$ and $E =
    \frac{\sqrt5}{2}i$ grows). The finite norm factor $1/(3H)$ of these modes was
    checked in section 8.
    """),
    code(r'''
    def h_of(column):
        """The mode operator h applied to a column of functions of x4 and x0 (U = 0)."""
        return (-sp.I * m * G[4] * column
                + sp.I * G[4] * G[0] * sp.exp(a4) / sp.sqrt(b4)
                * (sp.tan(z) * sp.diff(column, x0) + sp.Rational(3, 2) * H * column)
                - sp.I * v_g * column)


    A_mat = -sp.I * m * G[4] + sp.I * c_g * G[4] * G[0]  # the matrix A(x4)
    chi_t = sp.Matrix([sp.Function(f"c{n}")(x4) for n in range(1, 17)])  # arbitrary
    Psi_t = F * chi_t  # an x0-independent field
    action_ok = all(is_zero(v) for v in h_of(Psi_t) - (A_mat - sp.I * v_g * sp.eye(16))
                    * Psi_t)
    reduced_ok = all(is_zero(v) for v in sp.I * sp.diff(Psi_t, x4) - h_of(Psi_t)
                     - F * (sp.I * sp.diff(chi_t, x4) - A_mat * chi_t))
    check(action_ok and reduced_ok, "h Psi = (A - i v_g) Psi on x0-independent Psi, and "
          "i d4 Psi = h Psi is i d4 chi = A chi for Psi = F chi")
    m_s, cg_s = sp.symbols("m c_g", real=True)  # the mass and c_g as plain real numbers
    A_plain = -sp.I * m_s * G[4] + sp.I * cg_s * G[4] * G[0]
    A_zero = A_plain.subs({m_s: 1, cg_s: sp.Rational(3, 2)})  # m = H = 1 at x4 = 0
    dimension = 16 - (A_zero - sp.sqrt(5) / 2 * sp.I * sp.eye(16)).rank()
    report("dimension of the eigenspace of +sqrt(5)/2 i at m = H = 1, x4 = 0", dimension)
    cg_history = sp.simplify(c_g.subs(history).doit())
    say(f"c_g on the history: {cg_history}")
    all_true = (A_plain != A_plain.H
                and (A_plain * A_plain - (m_s**2 - cg_s**2) * sp.eye(16)).applyfunc(
                    sp.expand) == sp.zeros(16, 16)
                and A_zero * A_zero == -sp.Rational(5, 4) * sp.eye(16) and dimension == 8
                and is_zero(cg_history - sp.Rational(3, 2) * H * sp.exp(H * x4 / 3)))
    check_record(all_true, "A = -i m g4 + i c_g g4 g0 is not Hermitian, A^2 = (m^2 - c_g^2) "
                 "I16; c_g = (3/2) H e^(H x4/3) on the history; +-sqrt(5)/2 i at m = H = 1",
                 SCOPE, "good_sector_x0_independent_modes_without_boundary_condition",
                 "so Psi = e^(a4/2) b4^(-1) chi with i d4 chi = A chi",
                 "A = -i m gamma^(x4) + i cg gamma^(x4) gamma^(x0), which is not "
                 "Hermitian, and A^2 = (m^2 - cg^2) I16 exactly",
                 "cg = (3/2) H e^(H x4/3) grows, so every mass falls below it at late x4")
    '''),
    md(r"""
    The next cell draws, for $H = 1$ and $m = 2$, the eigenvalues $\pm\sqrt{m^2 -
    c_g^2}$ of $A(x_4)$ in the complex plane as the time runs along the history from
    $-2$ to $3$ (left): they move inwards on the real axis, meet at 0 when $c_g = m$, at
    $x_4 = 3\ln(2m/3) = 3\ln(4/3)$, and then leave along the imaginary axis. The right
    panel shows the instantaneous growth rate $\sqrt{c_g^2 - m^2}$ against the time for
    four masses: every mass is overtaken.
    """),
    code(r'''
    g4_number = np.array(G[4], dtype=float)  # gamma^(x4) as numbers
    g4g0_number = np.array(G[4] * G[0], dtype=float)  # gamma^(x4) gamma^(x0), real symmetric


    def cg_of(x4_value):
        """c_g = (3/2) H e^(H x4/3) on the history, H = 1."""
        return 1.5 * np.exp(x4_value / 3)


    def A_number(mass_value, x4_value):
        """The matrix A = -i m gamma^(x4) + i c_g gamma^(x4) gamma^(x0) at time x4."""
        return -1j * mass_value * g4_number + 1j * cg_of(x4_value) * g4g0_number


    path_times = np.linspace(-2.0, 3.0, 51)
    points = np.concatenate([np.linalg.eigvals(A_number(2.0, t)) for t in path_times])
    expected_size = np.repeat(np.sqrt(np.abs(4.0 - cg_of(path_times) ** 2)), 16)
    onset_m2 = 3 * np.log(4.0 / 3.0)  # c_g = m = 2
    report("time at which c_g = m = 2 on the history, 3 ln(4/3)", f"{onset_m2:.6f}")
    check(np.max(np.abs(np.abs(points) - expected_size)) < 1e-9,
          "the eigenvalues of A(x4) are +-sqrt(m^2 - c_g^2) at every time (m = 2)")
    fig, (left, right) = plt.subplots(1, 2, figsize=(10.0, 4.2))
    fig.subplots_adjust(wspace=0.55)  # room for the colour bar and the right label
    dots = left.scatter(points.real, points.imag, c=np.repeat(path_times, 16),
                        cmap="plasma", s=20)
    fig.colorbar(dots, ax=left, label="time $x_4$ (units of $1/H$)")
    left.set_aspect("equal")
    left.set_xlim(-4.0, 4.0)
    left.set_ylim(-4.0, 4.0)
    left.set_xlabel("real part")
    left.set_ylabel("imaginary part")
    left.set_title("Eigenvalues of $A(x_4)$, $m = 2$, $H = 1$")
    fine = np.linspace(-3.0, 6.0, 901)
    for mass_value, style in ((0.5, "-"), (1.0, "--"), (2.0, ":"), (4.0, "-.")):
        rate = np.sqrt(np.maximum(cg_of(fine) ** 2 - mass_value**2, 0.0))
        right.plot(fine, rate, style, label=f"$m = {mass_value:g}$")
    right.set_xlabel("time $x_4$ (units of $1/H$)")
    right.set_ylabel("growth rate $\\sqrt{c_g^2 - m^2}$ (units of $H$)")
    right.set_title("Every mass is overtaken")
    right.legend();
    save_figure(fig, "good_sector_modes",
                "Left: the eigenvalues $\\pm\\sqrt{m^2 - c_g^2}$ of the matrix $A = "
                "-im\\gamma^{(4)} + ic_g\\gamma^{(4)}\\gamma^{(0)}$, which acts on the "
                "$x_0$-independent fields of the good sector, in the complex plane for "
                "$m = 2$, $H = 1$, coloured by the time $x_4$ from $-2$ to $3$ along the "
                "history $a_4 = x_4$, $b_4 = e^{4x_4/3}$, on which $c_g = \\frac32"
                "e^{x_4/3}$. While $c_g < m$ they lie on the real axis (oscillation); "
                "they meet at 0 at $x_4 = 3\\ln(4/3) \\approx 0.863$ and then lie on the "
                "imaginary axis (a mode $e^{-iEx_4}$ grows). Right: the instantaneous "
                "growth rate $\\sqrt{c_g^2 - m^2}$ against $x_4$ for $m = 0.5, 1, 2, 4$; "
                "the light masses grow already at $x_4 = 0$, and every curve leaves zero "
                "after a finite time.")
    '''),
    md(r"""
    ## 10. The boundary term at the fold

    For fields of $x_4$ and $x_0$ the mode operator is $h = A + P\partial_0 - iv_g$ with
    $P = ie^{a_4}b_4^{-1/2}\tan z\,\gamma^{(4)}\gamma^{(0)}$. With $M_0 = i\gamma^{(4)}
    \gamma^{(0)}$ and $\sqrt{|g|} = \sigma e^{-a_4}b_4^2\cot z\,W^3$ the record proves,
    for all columns $u(x_0)$, $v(x_0)$,
    $$\sqrt{|g|}\,\big[u^\dagger(hv) - (hu)^\dagger v\big] = \partial_0\big(\sigma
    b_4^{3/2}(\sin^2 z)^{1/4}u^\dagger M_0 v\big) - i\,(\partial_4\sqrt{|g|})\,
    u^\dagger v .$$
    It follows from four matrix facts: the coefficient $P$ of $\partial_0$ is
    anti-Hermitian; $\sqrt{|g|}\,P = \sigma b_4^{3/2}W^3M_0$; $\sqrt{|g|}\,(A - A^\dagger)
    = \partial_0(\sigma b_4^{3/2}W^3)\,M_0$ for the algebraic part $A$; and the term
    $-iv_g$ is anti-Hermitian, $\sqrt{|g|}\,(-iv_g - (-iv_g)^\ast) = -2iv_g\sqrt{|g|} =
    -i\,\partial_4\sqrt{|g|}$ (because $\partial_4\sqrt{|g|} = 2v_g\sqrt{|g|}$). The last
    term is what keeps the norm constant in time as the 7-volume changes. The next cell
    checks the four facts, the identity itself for two explicit columns of polynomials
    with complex coefficients, and the value at the fold: for $u$ with
    $\gamma^{(4)}\gamma^{(0)}u = u$, $u^\dagger M_0u = i\,u^\dagger u \neq 0$. So the
    norm $\int\sqrt{|g|}\,u^\dagger v\,dx_0$ is conserved only up to
    $[\sigma b_4^{3/2}(\sin^2 z)^{1/4}u^\dagger M_0v]$, which vanishes at a tip
    ($\sin z \to 0$) but not at the fold ($|\sin z| = 1$).
    """),
    code(r'''
    M0 = sp.I * G[4] * G[0]
    P = sp.I * sp.exp(a4) / sp.sqrt(b4) * sp.tan(z) * G[4] * G[0]  # the matrix of d0
    real_rates = {sp.conjugate(a4_prime): a4_prime, sp.conjugate(b4_prime): b4_prime}
    flux_weight = sigma * b4 ** sp.Rational(3, 2) * W(x0) ** 3  # sigma b4^(3/2) W^3
    fact_1 = (P + P.H).applyfunc(sp.simplify) == sp.zeros(16, 16)
    fact_2 = all(is_zero(v) for v in sqrt_g * P - flux_weight * M0)
    fact_3 = all(is_zero(v) for v in sqrt_g * (A_mat - A_mat.H)
                 - sp.diff(flux_weight, x0) * M0)
    fact_4 = is_zero((sqrt_g * (-sp.I * v_g - sp.conjugate(-sp.I * v_g))
                      + sp.I * sp.diff(sqrt_g, x4)).xreplace(real_rates))
    u_col = sp.Matrix([(A_ + 1) + sp.I * (2 * A_ - 3) * x0 + (A_ - 5) * x0**2 / 3
                       for A_ in range(16)])  # a column of polynomials in x0
    v_col = sp.Matrix([(3 - A_) * x0 + sp.I * (A_ + 2) + sp.I * A_ * x0**3 / 7
                       for A_ in range(16)])
    left_flux = (sqrt_g * ((u_col.H * h_of(v_col))[0] - (h_of(u_col).H * v_col)[0])
                 ).xreplace(real_rates)
    right_flux = (sp.diff(flux_weight * (u_col.H * M0 * v_col)[0], x0)
                  - sp.I * sp.diff(sqrt_g, x4) * (u_col.H * v_col)[0])
    u0 = (G[4] * G[0] - sp.eye(16)).nullspace()[0]  # gamma^(4) gamma^(0) u0 = u0
    flux = sp.simplify((u0.H * M0 * u0)[0])
    size_u0 = (u0.H * u0)[0]
    report("u0^dagger M0 u0 and u0^dagger u0", f"{flux}, {size_u0}")
    # The record states the same identity and the same flux (sympy writes i as I):
    check_record(fact_1 and fact_2 and fact_3 and fact_4
                 and is_zero(left_flux - right_flux) and flux == 2 * sp.I and size_u0 == 2,
                 "sqrt|g| (u^dagger h v - (h u)^dagger v) = d0(sigma b4^(3/2) (sin^2 "
                 "z)^(1/4) u^dagger M0 v) - i (d4 sqrt|g|) u^dagger v; at the fold "
                 "u0^dagger M0 u0 = 2 i", SCOPE,
                 "good_sector_hermiticity_up_to_the_brane_flux",
                 "sqrt|g| [u^dagger (h v) - (h u)^dagger v] = d_x0(sgn b4^(3/2) (sin^2 "
                 "z)^(1/4) u^dagger M0 v) - i (d_x4 sqrt|g|) u^dagger v",
                 f"u^dagger M0 u = {sp.sstr(flux)} (|u|^2 = {sp.sstr(size_u0)})")
    '''),
    md(r"""
    ## 11. A growing mode is fed through the fold

    Integrate the identity of section 10 over the first half of a cell ($\sigma = +1$).
    For a solution of $i\,\partial_4\Psi = h\Psi$ the norm $N(x_4) = \int_0^{\pi/(12H)}
    \sqrt{|g|}\,\Psi^\dagger\Psi\,dx_0$ changes, line by line, as
    $\frac{dN}{dx_4} = \int\big[(\partial_4\sqrt{|g|})\Psi^\dagger\Psi +
    \sqrt{|g|}\big((-ih\Psi)^\dagger\Psi + \Psi^\dagger(-ih\Psi)\big)\big]dx_0$ (the
    product rule) $= \int(\partial_4\sqrt{|g|})\Psi^\dagger\Psi\,dx_0 -
    i\int\sqrt{|g|}\,\big[\Psi^\dagger h\Psi - (h\Psi)^\dagger\Psi\big]dx_0 =
    -i\big[b_4^{3/2}(\sin^2 z)^{1/4}\Psi^\dagger M_0\Psi\big]_{\rm tip}^{\rm fold} =
    b_4^{3/2}\,\Psi^\dagger\gamma^{(4)}\gamma^{(0)}\Psi\big|_{z = \pi/2}$ (section 10;
    the two terms with $\partial_4\sqrt{|g|}$ cancel): the norm changes ONLY through
    the fold. For the $x_0$-independent mode $\Psi = F\chi(x_4)$ this reads $N =
    \chi^\dagger\chi/(3H)$ and $dN/dx_4 = e^{a_4}b_4^{-1/2}\chi^\dagger\gamma^{(4)}
    \gamma^{(0)}\chi$. The next cell follows such a mode with $m = 2$, $H = 1$ along
    the history from $x_4 = 0$ to $4$, through its onset at $3\ln(4/3)$, solving
    $d\chi/dx_4 = -iA(x_4)\chi = (-m\gamma^{(4)} + c_g\gamma^{(4)}\gamma^{(0)})\chi$
    (a real equation) with RK4 from a fixed random column, computes $dN/dx_4$ from the
    solution by the five-point difference formula $\big(-N(x_4 + 2s) + 8N(x_4 + s) -
    8N(x_4 - s) + N(x_4 - 2s)\big)/(12s)$ with the step $s$ (its error shrinks like
    $s^4$), compares it with the flux at the fold, and draws both. Interpretation
    (labelled): the growth is fed through the fold; a boundary
    condition at $z = \pi/2$ that stops this flux would change the spectrum, and which
    condition is physical is a question this notebook does not decide.
    """),
    code(r'''
    rng = np.random.default_rng(12345)  # fixed seed: the same column in every run
    chi_start = rng.normal(size=16)  # a real column (the equation is real)
    chi_start = chi_start / np.linalg.norm(chi_start)


    def rate_of(x4_value, column, mass_value=2.0):
        """d chi/dx4 = (-m gamma^(x4) + c_g gamma^(x4) gamma^(x0)) chi on the history."""
        return (-mass_value * g4_number + cg_of(x4_value) * g4g0_number) @ column


    steps = 4000
    step = 4.0 / steps
    times = np.linspace(0.0, 4.0, steps + 1)
    states = [chi_start]
    for n in range(steps):  # the classical RK4 method
        t_n, u = times[n], states[-1]
        s1 = rate_of(t_n, u)
        s2 = rate_of(t_n + step / 2, u + step / 2 * s1)
        s3 = rate_of(t_n + step / 2, u + step / 2 * s2)
        s4 = rate_of(t_n + step, u + step * s3)
        states.append(u + step / 6 * (s1 + 2 * s2 + 2 * s3 + s4))
    states = np.array(states)
    norms = np.einsum("ij,ij->i", states, states) / 3.0  # N = chi^dagger chi/(3 H)
    fluxes = np.exp(times / 3) * np.einsum("ij,jk,ik->i", states, g4g0_number, states)
    # dN/dx4 by the five-point difference formula (its error shrinks like step^4):
    slopes = (-norms[4:] + 8 * norms[3:-1] - 8 * norms[1:-3] + norms[:-4]) / (12 * step)
    inner = fluxes[2:-2]  # the flux at the same times
    agreement = np.max(np.abs(slopes - inner) / np.maximum(np.abs(inner), 1.0))
    report("largest relative difference of dN/dx4 and the flux", f"{agreement:.1e}")
    check(agreement < 1e-8, "dN/dx4 equals the flux through the fold at every x4 (to the "
          "accuracy of the difference formula)")
    report("N(4) / N(0)", f"{norms[-1] / norms[0]:.6e}")
    check(norms[-1] / norms[0] > 1e4, "the norm grows by more than a factor 10^4")

    fig, (left, right) = plt.subplots(1, 2, figsize=(10.0, 4.0))
    left.semilogy(times, norms)
    left.axvline(3 * np.log(4.0 / 3.0), color="gray", linestyle=":", linewidth=0.9)
    left.set_xlabel("time $x_4$ (units of $1/H$)")
    left.set_ylabel("norm $N(x_4)$")
    left.set_title("The $x_0$-independent mode, $m = 2$, $H = 1$")
    right.plot(times[2:-2], slopes, label="$dN/dx_4$ (five-point differences)")
    right.plot(times[::200], fluxes[::200], "o", color="black", markersize=4,
               label="flux at the fold $z = \\pi/2$")
    right.axhline(0.0, color="black", linewidth=0.8)
    right.set_yscale("symlog", linthresh=1.0)  # linear between -1 and 1, log outside
    right.set_ylim(-1.5, 3.0e9)
    right.set_xlabel("time $x_4$ (units of $1/H$)")
    right.set_ylabel("rate (units of $H$)")
    right.set_title("Rate of change of the norm = flux")
    right.legend();
    save_figure(fig, "norm_and_flux",
                "An $x_0$-independent mode of the good sector, $\\Psi = e^{a_4/2}"
                "b_4^{-1}\\chi(x_4)$ with $m = 2$, $H = 1$, along the history $a_4 = "
                "x_4$, $b_4 = e^{4x_4/3}$ from a fixed random start, solved with RK4, "
                "against the time $x_4$ in units of $1/H$. Left, on a logarithmic axis: "
                "its norm $N = \\int\\sqrt{|g|}\\,\\Psi^\\dagger\\Psi\\,dx_0$ over the "
                "first half of a cell, which wavers while $c_g < m$ and grows faster "
                "and faster after the onset at $x_4 = 3\\ln(4/3)$ (dotted). Right, on an "
                "axis that is linear between $-1$ and $1$ and logarithmic outside: the "
                "rate of change $dN/dx_4$ (line) and the flux $b_4^{3/2}\\Psi^\\dagger"
                "\\gamma^{(4)}\\gamma^{(0)}\\Psi$ through the fold $z = \\pi/2$ (dots); "
                "they coincide at every time: the norm changes only through the fold, "
                "where the Revision record imposes no boundary condition.")
    '''),
    md(r"""
    ## 12. The last check

    The last cell checks that the five figure files exist in the folder
    Revision/textbook/figures and prints the number of checks that passed.
    """),
    code(r'''
    for name in ("08d_1_rescaling_factors.png", "08d_2_family_growth.png",
                 "08d_3_growing_finite_norm.png", "08d_4_good_sector_modes.png",
                 "08d_5_norm_and_flux.png"):
        check(output_file(f"{FIGURE_FOLDER}/{name}").is_file(),
              f"the figure file {name} exists")
    all_checks_passed()
    '''),
    md(r"""
    ## 13. What this notebook showed

    - The spin connection of the record makes the gammas covariantly constant, and
      $\gamma^\mu\Omega_\mu = c_g\gamma^{(0)} + v_g\gamma^{(4)}$ in the diagonal frame
      (PROVED).
    - The rescaling $\Psi = e^{a_4/2}b_4^{-1}(\sin^2 z)^{-1/8}\chi$ removes this term
      exactly: $\gamma^\mu D_\mu\Psi = e^{a_4/2}b_4^{-1}(\sin^2 z)^{-1/8}\gamma^\mu
      \partial_\mu\chi$ for every $\chi$, so for $U = 0$ the equation for $\chi$ has no
      spin-connection term, and for $U = \frac{\lambda}{2}S^2$ the term reappears as the
      coupling $\lambda e^{a_4}S[\chi]/(b_4^2|\sin z|^{1/2})$, which depends on $x_0$ and
      on the time (PROVED). The weight moves into the measure: the norm of $\Psi$ is
      $\int\chi^\dagger\chi\,|dy|$. Together with the frame dependence of the term, this
      is the exact scope of the statement "the field equation contains $c_g\gamma^{(0)}
      + v_g\gamma^{(4)}$": it belongs to one frame AND one choice of field variables.
    - The field equation for $\Psi = e^{a_4/2}b_4^{-1}(\sin^2 z)^{\alpha/2}\Phi(x_4)$
      reduces to $\Phi' = (-m\gamma^{(4)} + \mu_AK)\Phi$; the two exact families of the
      record ($m = 0$ with every $\alpha$; $\alpha = -\frac14$ with every $m$) solve the
      field equation for all functions $a_4$ and $b_4$ (PROVED). The members with
      $\alpha > -\frac14$ have a finite norm at the tip, $1/(3H(4\alpha + 1))$ times a
      function of the time; on the history $\mu_A$ grows like $e^{Hx_4/3}$, so every
      member with $\alpha \neq -\frac14$ eventually has a real instantaneous growth
      rate, for every mass (PROVED with frozen time), and the massless members grow
      like $e^{I}$ with $I = \frac92(4\alpha + 1)(e^{Hx_4/3} - 1)$ (PROVED).
    - The $x_0$-independent modes of the good sector have the matrix $A = -im
      \gamma^{(4)} + ic_g\gamma^{(4)}\gamma^{(0)}$ with $A^2 = (m^2 - c_g^2)I_{16}$; on the
      history $c_g = \frac32He^{Hx_4/3}$ overtakes every mass (PROVED; Revision check
      `good_sector_x0_independent_modes_without_boundary_condition`).
    - The mode operator is symmetric only up to the boundary term $[\sigma b_4^{3/2}
      (\sin^2 z)^{1/4}u^\dagger M_0v]$ (its term $-iv_g$ compensates the change of the
      7-volume), which does not vanish at the fold $z = \pi/2$ (PROVED), and the norm
      of a growing mode changes exactly by the flux through the fold (COMPUTED, to the
      accuracy of the method). Without a boundary condition at the fold the
      initial-value problem of the good sector therefore has growing solutions; which
      boundary condition is physical is OPEN here (the Kohn-Sham record ASSUMES fold
      conditions for its own model).
    """),
]

if __name__ == "__main__":
    raise SystemExit(run_builder(__file__))
