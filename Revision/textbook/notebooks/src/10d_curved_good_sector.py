#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
"""Builder of Notebook 10d, "The curved good sector and the fold z = pi/2" (textbook
"Universes in Pairs", chapter 10: canonical quantisation in 4+4, the Krein space and the
good sector).

The notebook Revision/textbook/notebooks/10d_curved_good_sector.ipynb is BUILT from this
file by Revision/textbook/tools/nbkit.py (never edit the .ipynb by hand):

    python Revision/textbook/tools/nbkit.py build \
        Revision/textbook/notebooks/src/10d_curved_good_sector.py --date YYYY-MM-DD
    python Revision/textbook/tools/nbkit.py check \
        Revision/textbook/notebooks/src/10d_curved_good_sector.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools"))
from nbkit import code, md, run_builder  # noqa: E402

FACTS = {
    "id": "10d",
    "name": "10d_curved_good_sector",
    "title": "The curved good sector and the fold z = pi/2",
    "purpose": (
        "In the corrected metric of the author (version 2 of 2026-10-16) it writes the "
        "good-sector mode operator along the hidden direction, proves exactly with sympy "
        "that it is symmetric, and that the Krein form is conserved, only up to a "
        "boundary term that vanishes where sin z = 0 but not at the fold z = pi/2 "
        "between the two halves of a cell, with the anti-Hermitian part of the operator "
        "compensating the time dependence of the volume factor; it shows that without "
        "the spin-connection term c_g a remainder survives, that the waves independent "
        "of x0 (finite norm) evolve with a matrix A whose square is m^2 - c_g^2, so that "
        "they grow wherever the mass is below c_g, which grows along the prescribed "
        "history, checks the exact growing solution of mass 0 and that its Krein charge "
        "changes by exactly the flux through the fold, reproduces the recorded "
        "statements, and draws five teaching figures."
    ),
    "records": [
        ["Revision/algebra/gammas.json", "the author's gamma matrices (read)"],
        ["Revision/theory/field-theory.json",
         "formulas sqrt_det_g and gammaOmega_total, the volume factor and the "
         "spin-connection term of the corrected metric (read and reproduced)"],
        ["Revision/kohn_sham/results/parameters.json",
         "the prescribed history a4 = A H x4, b4 = b4(0) e to the beta a4 (A = 1, "
         "beta = 4/3, b4(0) = 1, H = m = 1) and the five slices a4,0 of the Kohn-Sham "
         "record (read)"],
        ["Revision/theory/reports/wolfram-field-theory.json",
         "checks good_sector_hermiticity_curved and Krein_form_conserved_curved "
         "(reproduced)"],
        ["Revision/theory/reports/python-scope.json",
         "checks good_sector_hermiticity_up_to_the_brane_flux and "
         "good_sector_x0_independent_modes_without_boundary_condition (reproduced; the "
         "first keeps its name from the withdrawn metric of 2026-10-14, its detail "
         "concerns the folds of the corrected metric)"],
        ["Revision/theory/reports/python-field-theory.json",
         "checks sqrt_det_g and exact_solution_family_x4_x0 (reproduced; the second in "
         "its case alpha = 0, m = 0)"],
    ],
    "packages": ["numpy", "sympy", "matplotlib"],
    "needs_rust": [],
    "expected_seconds": 25,
    "timeout_seconds": 300,
    "files_written": [
        "Revision/textbook/figures/10d.captions.json",
        "Revision/textbook/figures/10d_1_volume_and_flux.png",
        "Revision/textbook/figures/10d_2_symmetry_defect.png",
        "Revision/textbook/figures/10d_3_frequency_paths.png",
        "Revision/textbook/figures/10d_4_growth_rate.png",
        "Revision/textbook/figures/10d_5_krein_leak.png",
    ],
    "final_lines": [
        "PASS the figure file 10d_5_krein_leak.png exists",
        "ALL 19 CHECKS PASSED (notebook 10d)",
    ],
    "troubleshooting": [
        ["\"FileNotFoundError\" for a file below the folder Revision",
         "the notebook reads files of the Revision record: the data it starts from and "
         "the report files whose checks it reproduces (each cited check must still "
         "exist there with the verdict PASS). It must be opened inside the folder "
         "Revision/textbook/notebooks of a complete copy of the repository (a notebook "
         "copied alone to another folder cannot find them). Clone the repository again "
         "and open the notebook there."],
        ["\"AssertionError: the cited record check is missing or not PASS\"",
         "a report file of the Revision record no longer holds the check that the "
         "notebook names, or holds it with another verdict: the copy of the repository "
         "is incomplete or was changed. Clone the repository again and open the "
         "notebook there."],
    ],
}

CELLS = [
    md(r"""
    ## 1. What this notebook computes

    The previous notebooks of this chapter worked with plane waves in flat 4+4 space (or
    with the coefficients frozen at one point). This notebook goes back to the author's
    curved metric, the corrected metric of 2026-10-16, and looks at the good sector (no
    dependence on the extra times $x_5, x_6, x_7$) along the hidden direction $x_0$,
    with $z = 6Hx_0$. A cell of the hidden direction has two halves, $0 < z < \pi/2$
    and $\pi/2 < z < \pi$, which meet at the fold $z = \pi/2$, where $g_{00}$ and the
    volume factor $\sqrt{|g|}$ vanish; the notebook works on the half $0 < z < \pi/2$
    (the other half is its image under the reflection $z \to \pi - z$). It

    - writes the mode operator $h$ of the field equation for waves that depend only on
      $x_4$ and $x_0$: $i\,\partial_4\Psi = h\Psi$;
    - proves exactly (sympy) that $h$ is symmetric for the volume $\sqrt{|g|}\,dx_0$
      only up to a boundary term $\partial_0(b_4^{3/2}\sin^{1/2}z\,u^\dagger M_0v)$ and
      a term of the time-dependent volume, which the part $-iv_g$ of $h$ compensates;
      the Krein form is conserved only up to a similar boundary term; the boundary term
      vanishes where $\sin z = 0$ but NOT at the fold $z = \pi/2$;
    - shows that the spin-connection term $c_g\gamma^{(x_0)}$ of the field equation,
      $c_g = \frac32He^{a_4}b_4^{-1/2}$, is exactly what makes the hidden-direction
      operator symmetric up to that boundary term (without it a remainder
      $-2c_g\sqrt{|g|}\,u^\dagger M_0v$ survives);
    - shows that the waves that do not depend on $x_0$ (they have a finite norm) evolve
      with the matrix $A = -im\gamma^{(x_4)} + ic_g\gamma^{(x_4)}\gamma^{(x_0)}$, with
      $A^2 = (m^2 - c_g^2)I_{16}$: wherever $m^2 < c_g^2$ their frequencies are
      imaginary and they grow, and along the prescribed history of the Revision record
      $c_g$ grows, so every mass falls below it at late times;
    - checks an exact growing solution (mass 0), and that its Krein charge changes in
      time by exactly the flux through the fold $z = \pi/2$;
    - reproduces the recorded statements and draws five teaching figures.

    The message for the chapter: the positive Fock space of the previous notebook is a
    construction for flat space (frozen coefficients). In the curved good sector the
    evolution is Hermitian, and the Krein charge conserved, only if a boundary condition
    is imposed at the folds $z = \pi/2 + n\pi$, and the Revision quantisation imposes
    none (the Kohn-Sham record ASSUMES fold conditions for its own states).
    """),
    md(r"""
    ## 3. The words used in this notebook

    - **Hidden direction, $z$, cell, fold**: $x_0$ is the hidden space direction and
      $z = 6Hx_0$ takes every real value. The metric component $g_{00} =
      e^{-2a_4}b_4\cot^2 z$ vanishes at $z = \pi/2 + n\pi$, the *folds*, where the two
      halves $z < \pi/2$ and $z > \pi/2$ of a *cell* $0 < z < \pi$ meet; at $z = n\pi$
      ($\sin z = 0$) the extra-time components of the metric vanish. Both kinds of
      points are *degenerate points* of the metric. This notebook works on the half
      $0 < z < \pi/2$, that is $0 < x_0 < \pi/(12H)$.
    - **$a_4$, $b_4$, the history**: the two metric functions of the time $x_4$. The
      Revision record uses the prescribed history $a_4 = AHx_4$, $b_4 =
      b_4(0)e^{\beta AHx_4}$ with $A = 1$, $\beta = 4/3$, $b_4(0) = 1$ and $H = 1$, a
      PRESCRIBED BACKGROUND (not a solution of the field equations for $a_4$ and
      $b_4$).
    - **Volume element**: $\sqrt{|g|} = e^{-a_4}b_4^2|\cot z|(\sin^2 z)^{1/4}$; on the
      half $0 < z < \pi/2$ it is $e^{-a_4}b_4^2\cot z\,\sin^{1/2}z$. An integral over
      the hidden direction is $\int\sqrt{|g|}\,(\ldots)\,dx_0$.
    - **$c_g$ and $v_g$**: the two coefficients of the spin-connection term
      $\gamma^\mu\Omega_\mu = c_g\gamma^{(x_0)} + v_g\gamma^{(x_4)}$ of the field
      equation, $c_g = \frac32He^{a_4}b_4^{-1/2}$ and $v_g = b_4'/b_4 - a_4'/2$ (a prime
      is the derivative in $x_4$). On the history $c_g = \frac32He^{AHx_4/3}$ grows and
      $v_g = \frac56AH$ is constant.
    - **Symmetric operator (formally Hermitian)**: an operator $h$ with
      $\int\sqrt{|g|}\,u^\dagger(hv)\,dx_0 = \int\sqrt{|g|}\,(hu)^\dagger v\,dx_0$ for
      all wave functions $u, v$. A *boundary term* is a part of the integrand that is a
      derivative, $\partial_0(\ldots)$; its integral is the difference of the bracket at
      the two ends, so the operator is symmetric when that difference vanishes.
    - **Krein form, Krein charge**: $\int\sqrt{|g|}\,u^\dagger Bv\,dx_0$; for $u = v =
      \Psi$ it is the charge of the wave.
    - **Flux**: the value of the bracket at an end; a nonzero flux at the fold means
      that something flows through the fold (in or out).
    - **Boundary condition**: a rule imposed on the wave functions at an end (for
      example that a flux vanishes there); it is an assumption added to the equations.
    - **$K$ and $M_0$**: the matrices $K = \gamma^{(x_4)}\gamma^{(x_0)}$ and $M_0 =
      iK = i\gamma^{(x_4)}\gamma^{(x_0)}$.
    - **Exponential of a matrix**: $e^{\theta K} = \sum_n (\theta K)^n/n!$; since
      $K^2 = I_{16}$ the series collapses to $\cosh(\theta)\,I_{16} + \sinh(\theta)\,K$
      (even and odd powers).
    """),
    md(r"""
    ## 4. The physical and mathematical situation

    **The field equation for waves in $x_4$ and $x_0$ only.** The field equation of
    dirac16complex in the author's metric (Revision theory record, formula
    `field_equation`, $U = 0$) is

    $$e^{a_4}b_4^{-1/2}\tan z\,\gamma^{(x_0)}\partial_0\Psi + e^{-a_4}\sum_{i=1}^3
    \gamma^{(x_i)}\partial_i\Psi + \gamma^{(x_4)}\partial_4\Psi +
    \frac{e^{a_4}}{b_4^{1/2}(\sin^2 z)^{1/12}}\sum_{t=5}^7\gamma^{(x_t)}\partial_t\Psi
    + c_g\gamma^{(x_0)}\Psi + v_g\gamma^{(x_4)}\Psi = m\Psi .$$

    For a wave that depends only on $x_4$ and $x_0$ the second and fourth groups vanish:

    $$\gamma^{(x_4)}\partial_4\Psi + e^{a_4}b_4^{-1/2}\tan z\,\gamma^{(x_0)}
    \partial_0\Psi + c_g\gamma^{(x_0)}\Psi + v_g\gamma^{(x_4)}\Psi = m\Psi .$$

    Multiply from the left by $\gamma^{(x_4)}$, use $(\gamma^{(x_4)})^2 = -1$ and solve
    for $\partial_4\Psi$:

    $$\partial_4\Psi = -m\gamma^{(x_4)}\Psi + e^{a_4}b_4^{-1/2}\tan z\,\gamma^{(x_4)}
    \gamma^{(x_0)}\partial_0\Psi + c_g\gamma^{(x_4)}\gamma^{(x_0)}\Psi - v_g\Psi .$$

    Multiply by $i$:

    $$i\,\partial_4\Psi = h\Psi,\qquad h = A + D\,\partial_0 - iv_g,\qquad
    A = -im\gamma^{(x_4)} + ic_g\gamma^{(x_4)}\gamma^{(x_0)},\qquad
    D = e^{a_4}b_4^{-1/2}\tan z\,M_0 .$$

    **Symmetry up to a boundary term, line by line.** Write $u'$ for $\partial_0u$.
    Then

    $$u^\dagger(hv) - (hu)^\dagger v = u^\dagger(A - A^\dagger)v + u^\dagger Dv' -
    u'^\dagger D^\dagger v - 2iv_g\,u^\dagger v .$$

    (The last term: $-iv_g$ is a number times $I_{16}$, and its conjugate transpose is
    $+iv_g$.) The notebook checks that $M_0$ is anti-Hermitian, so $D^\dagger = -D$,
    and the two derivative terms are $u^\dagger Dv' + u'^\dagger Dv$. Multiply by
    $\sqrt{|g|}$. The notebook checks two matrix identities on the half $0 < z < \pi/2$:
    $\sqrt{|g|}\,D = wM_0$ and $\sqrt{|g|}\,(A - A^\dagger) = w'M_0$, with the bracket
    factor $w = b_4^{3/2}\sin^{1/2}z$ (the factors $\cot z$ and $\tan z$ cancel). With
    them and the product rule $(w\,u^\dagger M_0v)' = w'u^\dagger M_0v +
    w\,(u^\dagger M_0v' + u'^\dagger M_0v)$ the $x_0$ terms collect into one derivative:

    $$\sqrt{|g|}\,\big[u^\dagger(hv) - (hu)^\dagger v\big] = \partial_0\big(w\,
    u^\dagger M_0 v\big) - 2iv_g\sqrt{|g|}\,u^\dagger v .$$

    **The time-dependent volume.** The volume factor depends on the time:
    $\partial_4\sqrt{|g|} = 2v_g\sqrt{|g|}$ (the notebook checks it). For two solutions
    $u, v$ the product rule and $\partial_4u = -ihu$ give

    $$\frac{d}{dx_4}\int\sqrt{|g|}\,u^\dagger v\,dx_0 = \int\Big[(\partial_4\sqrt{|g|})
    \,u^\dagger v - i\sqrt{|g|}\big(u^\dagger(hv) - (hu)^\dagger v\big)\Big]dx_0 =
    -i\,\big[w\,u^\dagger M_0v\big]_{\rm ends} ,$$

    because the term $-2iv_g\sqrt{|g|}\,u^\dagger v$, times $-i$, is
    $-2v_g\sqrt{|g|}\,u^\dagger v$ and cancels $(\partial_4\sqrt{|g|})\,u^\dagger v$. So
    the anti-Hermitian part $-iv_g$ of $h$ is exactly what the time dependence of the
    volume needs, and the inner product changes only through the bracket at the ends.
    At $z = 0$ the bracket vanishes ($\sin 0 = 0$); at the fold $z = \pi/2$ it is
    $b_4^{3/2}u^\dagger M_0v$, which does not vanish in general. The term
    $ic_g\gamma^{(x_4)}\gamma^{(x_0)}$ of $A$ (the spin-connection term
    $c_g\gamma^{(x_0)}$ of the field equation) supplies exactly $A - A^\dagger =
    2c_gM_0$, which is needed because $w' = 2c_g\sqrt{|g|}$.

    **Waves that do not depend on $x_0$.** For them $\partial_0\Psi = 0$ and $h$ acts as
    $A - iv_g$. Writing $\Psi = e^{a_4/2}b_4^{-1}\chi$ removes $-iv_g$ (the factor
    changes at the rate $-v_g$), so $i\,\partial_4\chi = A\chi$. Their norm
    $\int\sqrt{|g|}\,\Psi^\dagger\Psi\,dx_0$ over the half is $\chi^\dagger\chi$ times
    $\int_0^{\pi/(12H)}\cot z\,\sin^{1/2}z\,dx_0 = 1/(3H)$ (the factor $e^{-a_4}b_4^2$
    of the volume and the factor $e^{a_4}b_4^{-2}$ of $\Psi^\dagger\Psi$ cancel): it is
    finite, so they are honest members of the good sector. The notebook proves
    $A^2 = (m^2 - c_g^2)I_{16}$: wherever $m^2 < c_g^2$ the frequencies of the instant
    are imaginary and these waves grow. On the history $c_g = \frac32He^{AHx_4/3}$ grows
    without bound: every mass falls below it at late times.
    """),
    md(r"""
    ## 5. The matrices of the hidden direction

    The next cell reads the gammas, builds $C$ and $B$ with numpy and as exact sympy
    matrices, and defines the helper `check_record` (the PASS line and the line of the
    reproduced Revision record are printed in one piece, so that the stored output is
    the same in every run; before that it confirms with the helper `record_says_pass`
    that the cited report check still exists with the verdict PASS) and the colours. It
    reads the prescribed history from the Revision Kohn-Sham record, and from the
    Revision theory record the formulas `sqrt_det_g` and `gammaOmega_total`, written in
    the notation of the Wolfram Language; it translates them into sympy and checks that
    they are the volume factor and the coefficients $c_g$ and $v_g$ of Section 4.

    To keep every check exact AND fast, the cell writes the functions of the hidden
    direction with two letters, $s = \sin^{1/2}z$ and $c = \cos z$, both positive on
    the half $0 < z < \pi/2$. Then $\sin z = s^2$, $\tan z = s^2/c$, $\cot z = c/s^2$,
    and every expression is a fraction of polynomials. The derivative along $x_0$
    follows from the chain rule: $d(\sin z)/dx_0 = 6H\cos z$ gives $2s\,ds/dx_0 = 6Hc$,
    so $ds/dx_0 = 3Hc/s$, and $dc/dx_0 = -6H\sin z = -6Hs^2$; the function `d0` applies
    these two rules. The letters $a$ and $b$ stand for the values of $a_4$ and $b_4$
    at the instant, and $v_g$ for the value of $b_4'/b_4 - a_4'/2$. The cell checks
    exactly that $\partial_4(e^{-a_4}b_4^2) = 2v_g\,e^{-a_4}b_4^2$ for arbitrary
    functions $a_4(x_4)$ and $b_4(x_4)$, and the matrix facts of Section 4:
    $M_0^\dagger = -M_0$, $\sqrt{|g|}\,D = wM_0$ and $\sqrt{|g|}\,(A - A^\dagger) =
    \partial_0(w)\,M_0$, and in addition that $B$ commutes with $\gamma^{(x_4)}$ and
    $\gamma^{(x_0)}$. The last fact gives the Krein version: $B$ then commutes with $A$,
    $A^\dagger$, $D$ and $M_0$, so the same steps with $u^\dagger B$ in place of
    $u^\dagger$ give $\sqrt{|g|}\,[u^\dagger B(hv) - (hu)^\dagger Bv] =
    \partial_0(w\,u^\dagger BM_0v) - 2iv_g\sqrt{|g|}\,u^\dagger Bv$.
    """),
    code(r'''
    import contextlib  # lets a block of code print into a text buffer
    import io  # the text buffer
    import sys  # the screen output, sys.stdout

    import numpy as np  # numbers, arrays and matrices
    import sympy as sp  # exact algebra with symbols


    REPORT_CHECKS = {}  # report file -> {check name: verdict}; each file is read once


    def record_says_pass(record):
        """True if the cited report check exists today with the verdict PASS."""
        path, separator, check_name = record.partition(", check ")
        if not separator:  # a data entry of a record file that the notebook reads itself
            return True
        if path not in REPORT_CHECKS:
            checks = json.loads(repository_file(path).read_text(encoding="utf-8"))["checks"]
            REPORT_CHECKS[path] = {c["name"]: c["verdict"].upper() for c in checks}
        return REPORT_CHECKS[path].get(check_name) == "PASS"


    def check_record(condition, name, record):
        """check(condition, name, record=record), printed in one piece."""
        if not record_says_pass(record):  # the cited check must exist and say PASS
            raise AssertionError("the cited record check is missing or not PASS: " + record)
        buffer = io.StringIO()
        with contextlib.redirect_stdout(buffer):  # what check prints goes to buffer
            check(condition, name, record=record)
        sys.stdout.write(buffer.getvalue())  # one single piece of output


    BLUE, ORANGE, GREEN, GREY = "#2a78d6", "#eb6834", "#1baf7a", "#52514e"
    fixture = json.loads(repository_file("Revision/algebra/gammas.json").read_text(
        encoding="utf-8"))
    gamma = {a: np.array(fixture["gamma"][a], dtype=float) for a in range(8)}
    C = gamma[0] @ gamma[1] @ gamma[2] @ gamma[3]
    B = -1j * (C @ gamma[4])  # B = -i C gamma^(x4)
    g = {a: sp.Matrix(fixture["gamma"][a]) for a in range(8)}  # exact gammas
    B_exact = -sp.I * g[0] * g[1] * g[2] * g[3] * g[4]

    parameters = json.loads(repository_file(
        "Revision/kohn_sham/results/parameters.json").read_text(encoding="utf-8"))
    physics = parameters["physics"]
    A_history, beta = physics["historyA"], physics["historyBeta"]  # a4 = A H x4
    b4_start, H_value, m_value = physics["historyB4AtZero"], physics["H"], physics["m"]
    slices = physics["slicesA4"]  # the five slices a4,0 of the Kohn-Sham record
    say(f"history: A = {A_history}, beta = {beta:.6f}, b4(0) = {b4_start}, "
        f"H = {H_value}, m = {m_value}; slices a4,0 = {slices}")

    m = sp.Symbol("m", real=True)  # the mass
    H = sp.Symbol("H", positive=True)  # the author's constant H > 0
    a, b = sp.symbols("a b", positive=True)  # the values of a4 and b4 at the instant
    v_g = sp.Symbol("v_g", real=True)  # the value of b4'/b4 - a4'/2 at the instant
    s, c = sp.symbols("s c", positive=True)  # s = sin(z)^(1/2), c = cos z, z < pi/2


    def d0(expression):
        """d/dx0 by the chain rule: ds/dx0 = 3 H c / s and dc/dx0 = -6 H s^2."""
        return (sp.diff(expression, s) * 3 * H * c / s
                + sp.diff(expression, c) * (-6 * H * s ** 2))


    sqrt_g = sp.exp(-a) * b ** 2 * (c / s ** 2) * s  # e^-a4 b4^2 cot z sin(z)^(1/2)
    c_g = sp.Rational(3, 2) * H * sp.exp(a) / sp.sqrt(b)  # (3/2) H e^a4 b4^(-1/2)
    w = b ** sp.Rational(3, 2) * s  # the bracket factor b4^(3/2) sin(z)^(1/2)
    M0 = sp.I * g[4] * g[0]  # M_0 = i gamma^(x4) gamma^(x0)
    A = -sp.I * m * g[4] + sp.I * c_g * g[4] * g[0]  # the part without derivative
    A_no_connection = -sp.I * m * g[4]  # the same without the term c_g
    D = sp.exp(a) / sp.sqrt(b) * (s ** 2 / c) * M0  # e^a4 b4^(-1/2) tan z M_0

    formulas = {f["key"]: f["wl"] for f in json.loads(repository_file(
        "Revision/theory/field-theory.json").read_text(encoding="utf-8"))["formulas"]}
    z_letter = sp.Symbol("z", positive=True)  # z = 6 H x0
    volume_text = (formulas["sqrt_det_g"].replace("rftSig*", "")  # sign of cot z: +1
                   .replace("b4[x4]", "b").replace("Cot[6*H*x0]", "cot(z)")
                   .replace("Sin[6*H*x0]", "sin(z)").replace("E^a4[x4]", "exp(a)")
                   .replace("^", "**"))
    volume_record = sp.sympify(volume_text, locals={"a": a, "b": b, "z": z_letter})
    volume_record = volume_record.subs({sp.sin(z_letter): s ** 2,
                                        sp.cot(z_letter): c / s ** 2})
    term_text = (formulas["gammaOmega_total"].replace('gamma["x0"]', "G0")
                 .replace('gamma["x4"]', "G4").replace("Derivative[1][a4][x4]", "da")
                 .replace("Derivative[1][b4][x4]", "db").replace("Sqrt[b4[x4]]", "sqrt(b)")
                 .replace("b4[x4]", "b").replace("E^a4[x4]", "exp(a)").replace("^", "**"))
    G0, G4, da, db = sp.symbols("G0 G4 da db")  # stand-ins: the two gammas, a4', b4'
    term_record = sp.expand(sp.sympify(term_text, locals={
        "a": a, "b": b, "H": H, "G0": G0, "G4": G4, "da": da, "db": db}))
    say("record sqrt_det_g: " + formulas["sqrt_det_g"])
    say("record gammaOmega_total: " + formulas["gammaOmega_total"])
    check_record(sp.simplify(volume_record - sqrt_g) == 0
                 and sp.simplify(term_record.coeff(G0) - c_g) == 0
                 and sp.simplify(term_record.coeff(G4) - (db / b - da / 2)) == 0,
                 "the volume factor, c_g and v_g of the theory record",
                 record="Revision/theory/field-theory.json, formulas sqrt_det_g and "
                        "gammaOmega_total")

    x4 = sp.Symbol("x4", real=True)  # the time
    a4, b4 = sp.Function("a4")(x4), sp.Function("b4")(x4)  # any functions of x4
    volume_in_time = sp.exp(-a4) * b4 ** 2  # the x4-dependent factor of sqrt|g|
    v_g_function = sp.diff(b4, x4) / b4 - sp.diff(a4, x4) / 2
    measure = sp.simplify(sp.diff(volume_in_time, x4) - 2 * v_g_function * volume_in_time)
    check_record(measure == 0,
                 "exact: d/dx4 (e^-a4 b4^2) = 2 v_g e^-a4 b4^2 for all a4(x4), b4(x4)",
                 record="Revision/theory/reports/python-field-theory.json, check "
                        "sqrt_det_g")

    zero = sp.zeros(16, 16)
    anti_hermitian = M0.H == -M0
    identity_D = (sqrt_g * D - w * M0).applyfunc(sp.simplify) == zero
    identity_A = (sqrt_g * (A - A.H) - d0(w) * M0).applyfunc(sp.simplify) == zero
    B_commutes = (B_exact * g[4] == g[4] * B_exact) and (B_exact * g[0] == g[0] * B_exact)
    say(f"M0 anti-Hermitian: {anti_hermitian}; sqrt|g| D = w M0: {identity_D}; "
        f"sqrt|g| (A - A^dagger) = d0(w) M0: {identity_A}; B commutes with "
        f"gamma^(x4) and gamma^(x0): {B_commutes}")
    check(anti_hermitian and identity_D and identity_A and B_commutes,
          "exact: the four matrix identities of the hidden direction")
    '''),
    md(r"""
    ## 6. Symmetric up to a boundary term, checked on wave functions

    The matrix identities prove the statement of Section 4 for all wave functions. The
    next cell also checks it directly on two concrete wave functions $u(x_0)$ and
    $v(x_0)$: each of their 16 entries is a combination $\alpha + \beta\sin z +
    \delta\cos z = \alpha + \beta s^2 + \delta c$ with small whole numbers $\alpha,
    \beta, \delta$ (real and imaginary parts chosen at random with a fixed seed). It
    computes, exactly,

    - the defect $\sqrt{|g|}\,[u^\dagger(hv) - (hu)^\dagger v] -
      \partial_0(w\,u^\dagger M_0v) + 2iv_g\sqrt{|g|}\,u^\dagger v$, which must be 0;
    - the same with the operator WITHOUT the spin-connection term $c_g$, which must
      equal $-2c_g\sqrt{|g|}\,u^\dagger M_0v$ instead;
    - the Krein version $\sqrt{|g|}\,[u^\dagger B(hv) - (hu)^\dagger Bv] -
      \partial_0(w\,u^\dagger BM_0v) + 2iv_g\sqrt{|g|}\,u^\dagger Bv$, which must be 0.

    An expression is zero exactly when the numerator of its fraction, multiplied out,
    is zero; the function `is_zero` tests this. (The first record check below keeps the
    name `good_sector_hermiticity_up_to_the_brane_flux` from the withdrawn metric of
    2026-10-14; the corrected metric has no brane, and the detail of the check concerns
    the degenerate points $z = \pi/2 + n\pi$, the folds.)
    """),
    code(r'''
    rng = np.random.default_rng(12345)


    def test_function():
        """16 entries alpha + beta s^2 + delta c with small random whole numbers."""
        def number():
            return int(rng.integers(-3, 4)) + sp.I * int(rng.integers(-3, 4))
        return sp.Matrix([number() + number() * s ** 2 + number() * c
                          for _ in range(16)])


    def apply_h(matrix_A, f):
        """h f = A f + D df/dx0 - i v_g f for a column f of functions of x0."""
        return matrix_A * f + D * f.applyfunc(d0) - sp.I * v_g * f


    def is_zero(expression):
        """Exact zero test: the multiplied-out numerator of the fraction is 0."""
        return sp.expand(sp.numer(sp.together(sp.expand(expression)))) == 0


    u, v = test_function(), test_function()
    hv, hu = apply_h(A, v), apply_h(A, u)
    volume_term = 2 * sp.I * v_g * sqrt_g  # the term of the time-dependent volume
    defect = (sqrt_g * ((u.H * hv)[0] - (hu.H * v)[0]) - d0(w * (u.H * M0 * v)[0])
              + volume_term * (u.H * v)[0])
    hv0, hu0 = apply_h(A_no_connection, v), apply_h(A_no_connection, u)
    defect_without = (sqrt_g * ((u.H * hv0)[0] - (hu0.H * v)[0])
                      - d0(w * (u.H * M0 * v)[0]) + volume_term * (u.H * v)[0])
    remainder_ok = is_zero(defect_without + 2 * c_g * sqrt_g * (u.H * M0 * v)[0])
    krein_defect = (sqrt_g * ((u.H * B_exact * hv)[0] - (hu.H * B_exact * v)[0])
                    - d0(w * (u.H * B_exact * M0 * v)[0])
                    + volume_term * (u.H * B_exact * v)[0])
    check_record(is_zero(defect),
                 "exact: h is symmetric up to d0(w u^dagger M0 v) and the volume term",
                 record="Revision/theory/reports/python-scope.json, check "
                        "good_sector_hermiticity_up_to_the_brane_flux")
    check_record(remainder_ok and not is_zero(defect_without),
                 "exact: without c_g the remainder -2 c_g sqrt|g| u^dagger M0 v stays",
                 record="Revision/theory/reports/wolfram-field-theory.json, check "
                        "good_sector_hermiticity_curved")
    check_record(is_zero(krein_defect),
                 "exact: the Krein form is conserved up to d0(w u^dagger B M0 v)",
                 record="Revision/theory/reports/wolfram-field-theory.json, check "
                        "Krein_form_conserved_curved")
    '''),
    md(r"""
    ## 7. The flux at the two ends

    The bracket $w\,u^\dagger M_0v = b_4^{3/2}\sin^{1/2}z\,u^\dagger M_0v$ vanishes at
    $z = 0$ ($\sin 0 = 0$) for wave functions that stay finite there, but at the fold
    $z = \pi/2$ it is $b_4^{3/2}u^\dagger M_0v$. The Revision record gives an example:
    the matrix $K = \gamma^{(x_4)}\gamma^{(x_0)}$ is real, symmetric and squares to
    $I$, so it has the eigenvalue $+1$; for a column with $Ku = u$ and $u^\dagger u = 2$
    the flux factor is $u^\dagger M_0u = i\,u^\dagger Ku = i\,u^\dagger u = 2i$, not 0.
    The next cell builds such a column ($u = e_1 + Ke_1$ for the first unit column
    $e_1$) and draws, along one whole cell $0 < z < \pi$, the $z$-dependent part
    $|\cot z|(\sin^2 z)^{1/4}$ of the volume factor and the $z$-dependent part
    $(\sin^2 z)^{1/4}$ of the bracket.
    """),
    code(r'''
    K_numbers = gamma[4] @ gamma[0]  # K = gamma^(x4) gamma^(x0), real
    symmetric_square = (np.array_equal(K_numbers, K_numbers.T)
                        and np.array_equal(K_numbers @ K_numbers, np.eye(16)))
    e_first = np.eye(16)[:, 0]
    u_flux = e_first + K_numbers @ e_first  # an eigenvector of K with eigenvalue +1
    M0_numbers = 1j * K_numbers
    flux_value = u_flux.conj() @ M0_numbers @ u_flux
    report("u^dagger u for the column u = e_1 + K e_1", f"{u_flux @ u_flux:.1f}")
    report("flux factor u^dagger M0 u at the fold z = pi/2",
           f"{flux_value.imag:.1f} i (real part {abs(flux_value.real):.1f})")
    check_record(symmetric_square and np.allclose(K_numbers @ u_flux, u_flux)
                 and abs(flux_value - 2j) < 1e-14,
                 "the bracket at the fold is b4^(3/2) u^dagger M0 u = 2 i b4^(3/2)",
                 record="Revision/theory/reports/python-scope.json, check "
                        "good_sector_hermiticity_up_to_the_brane_flux")

    z_values = np.linspace(0.005, np.pi - 0.005, 600)  # one cell, without its two ends
    root = np.sqrt(np.abs(np.sin(z_values)))  # (sin^2 z)^(1/4)
    volume_factor = np.abs(np.cos(z_values) / np.sin(z_values)) * root
    fig, ax = plt.subplots()
    ax.plot(z_values, volume_factor, color=BLUE, linewidth=2,
            label="volume factor: $|\\cot z|(\\sin^2 z)^{1/4}$")
    ax.plot(z_values, root, color=ORANGE, linewidth=2,
            label="bracket factor: $(\\sin^2 z)^{1/4}$")
    ax.plot([0.0, np.pi], [0.0, 0.0], "o", color=ORANGE, markersize=8)
    ax.plot([np.pi / 2], [1.0], "o", color=ORANGE, markersize=8)
    ax.axvline(np.pi / 2, color=GREY, linestyle=":", linewidth=1)
    ax.annotate("fold: the volume\nvanishes, the\nbracket does not", (np.pi / 2, 1.0),
                xytext=(0.8, 1.35), arrowprops={"arrowstyle": "->", "color": GREY})
    ax.annotate("$\\sin z = 0$: the\nbracket vanishes", (0.0, 0.0), xytext=(0.12, 0.35),
                arrowprops={"arrowstyle": "->", "color": GREY})
    ax.set_xlabel("$z = 6 H x_0$ (one cell: two halves joined at the fold $z = \\pi/2$)")
    ax.set_ylabel("value")
    ax.set_ylim(-0.05, 2.0)
    ax.set_title("The hidden direction: volume and boundary bracket")
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.17), ncol=2, fontsize=8)
    save_figure(fig, "volume_and_flux",
                "Along one cell of the hidden direction, $z = 6Hx_0$ from 0 to $\\pi$ "
                "(horizontal axis): the $z$-dependent part $|\\cot z|(\\sin^2 z)^{1/4}$ "
                "of the volume factor $\\sqrt{|g|} = e^{-a_4}b_4^2|\\cot z|(\\sin^2 "
                "z)^{1/4}$ of the corrected metric (blue) and the $z$-dependent part "
                "$(\\sin^2 z)^{1/4}$ of the boundary bracket $b_4^{3/2}(\\sin^2 "
                "z)^{1/4}u^\\dagger M_0v$ (orange); vertical axis: pure numbers. The "
                "volume vanishes at the fold $z = \\pi/2$ (dotted line), where the two "
                "halves of the cell meet, and grows (integrably) towards $z = 0$ and "
                "$z = \\pi$; the bracket vanishes at $z = 0$ and $z = \\pi$ but is 1 "
                "at the fold, where it carries $b_4^{3/2}u^\\dagger M_0v$, for example "
                "$2ib_4^{3/2}$ for the recorded column. The mode operator is symmetric, "
                "and the Krein charge conserved, only if a boundary condition removes "
                "this flux at the fold.")
    '''),
    md(r"""
    The next cell makes the role of the spin-connection term visible for one pair of
    wave functions, here $u = v$ (the test function $u$ of Section 6), at the instant
    $x_4 = 0$ of the history ($a_4 = 0$, $b_4 = 1$) and $m = H = 1$, so that $c_g =
    3/2$. It takes the hidden-direction part $h_0 = A + D\,\partial_0$ of the operator
    (the part $-iv_g$ only adds the volume term $-2iv_g\sqrt{|g|}\,u^\dagger u$, which
    the time dependence of the volume cancels) and evaluates along $0 < z < \pi/2$ the
    left-hand side $\sqrt{|g|}\,[u^\dagger(h_0u) - (h_0u)^\dagger u]$, the right-hand
    side $\partial_0(w\,u^\dagger M_0u)$, and the left-hand side computed WITHOUT the
    term $c_g$. For $u = v$ all three are purely imaginary (a number minus its complex
    conjugate), so their imaginary parts are plotted. The exact expressions are turned
    into fast numerical functions of $s$ and $c$ with `sp.lambdify`, and $s =
    \sin^{1/2}z$, $c = \cos z$ are computed on a grid of $z$.
    """),
    code(r'''
    instant = {m: m_value, H: H_value, a: 0, b: b4_start}  # x4 = 0: a4 = 0, b4 = b4(0)
    h0u = A * u + D * u.applyfunc(d0)  # the hidden-direction part of h u
    h0u_bare = A_no_connection * u + D * u.applyfunc(d0)  # the same without c_g
    left = sqrt_g * ((u.H * h0u)[0] - (h0u.H * u)[0])
    right = d0(w * (u.H * M0 * u)[0])
    left_bare = sqrt_g * ((u.H * h0u_bare)[0] - (h0u_bare.H * u)[0])
    z_grid = np.linspace(0.02, np.pi / 2 - 0.02, 300)  # inside 0 < z < pi/2
    s_grid, c_grid = np.sqrt(np.sin(z_grid)), np.cos(z_grid)
    curves = [np.imag(sp.lambdify((s, c), e.subs(instant), "numpy")(s_grid, c_grid))
              for e in (left, right, left_bare)]
    difference = np.max(np.abs(curves[0] - curves[1]))
    report("largest |left - right| on the grid", f"{difference:.1e}")
    check(difference < 1e-9, "numerical: the two sides agree along the hidden direction")

    fig, ax = plt.subplots()
    ax.plot(z_grid, curves[0], color=BLUE, linewidth=3,
            label="left side, with the term $c_g$")
    ax.plot(z_grid, curves[1], "--", color=GREEN, linewidth=2,
            label="right side $\\partial_0(w\\,u^\\dagger M_0 u)$")
    ax.plot(z_grid, curves[2], color=ORANGE, linewidth=2,
            label="left side WITHOUT the term $c_g$")
    ax.set_xlabel("$z = 6 H x_0$ ($x_4 = 0$: $a_4 = 0$, $b_4 = 1$; $m = H = 1$)")
    ax.set_ylabel("imaginary part")
    ax.set_title("The spin-connection term makes the defect a pure boundary term")
    ax.legend(fontsize=8)
    save_figure(fig, "symmetry_defect",
                "For one concrete wave function $u(x_0)$ (16 entries of the form "
                "$\\alpha + \\beta\\sin z + \\delta\\cos z$) at the instant $x_4 = 0$ of "
                "the history ($a_4 = 0$, $b_4 = 1$, so $c_g = 3/2$) and $m = H = 1$: the "
                "imaginary parts of the symmetry defect $\\sqrt{|g|}\\,(u^\\dagger(h_0u) "
                "- (h_0u)^\\dagger u)$ of the hidden-direction part $h_0 = A + "
                "D\\partial_0$ of the curved good-sector mode operator (blue), of the "
                "derivative $\\partial_0(w\\,u^\\dagger M_0u)$ (green dashed, on top of "
                "the blue curve), and of the defect of the operator without the "
                "spin-connection term $c_g$ (orange), against $z$ from 0 to the fold "
                "$\\pi/2$ (horizontal axis). With the term the defect is exactly a "
                "derivative, whose integral is the flux at the ends; without it a "
                "remainder $-2c_g\\sqrt{|g|}\\,u^\\dagger M_0u$ survives.")
    '''),
    md(r"""
    ## 8. Waves that do not depend on $x_0$: growth wherever $m < c_g$

    For a wave that depends on $x_4$ only, $h$ acts as $A - iv_g$, and $\chi =
    e^{-a_4/2}b_4\Psi$ obeys $i\,\partial_4\chi = A\chi$. The next cell checks exactly:
    the norm integral $\int_0^{\pi/(12H)}\cot z\,\sin^{1/2}z\,dx_0 = 1/(3H)$ (by the
    substitution $q = \sin z$: the integrand is $c/s$, and $dq/dx_0 = 6H\cos z = 6Hc$,
    so the integrand is $\frac{1}{6H\sqrt q}\,dq/dx_0$ and the integral is
    $\int_0^1\frac{dq}{6H\sqrt q} = \frac{2}{6H}$); $A$ is not Hermitian; $A^2 = (m^2 -
    c_g^2)I_{16}$ (the same cancellation of mixed terms as for the mode Hamiltonian of
    flat space, because $\gamma^{(x_4)}$ and $\gamma^{(x_4)}\gamma^{(x_0)}$
    anticommute); and at the instant $x_4 = 0$ of the history with $m = H = 1$, where
    $c_g = 3/2$, the eigenvalues are $\pm i\sqrt{9/4 - 1} = \pm i\sqrt5/2$, eight of
    each (the trace of $A$ is 0).
    """),
    code(r'''
    q = sp.Symbol("q", positive=True)  # q = sin z, from 0 (z = 0) to 1 (the fold)
    integrand = sqrt_g / (sp.exp(-a) * b ** 2)  # cot z sin(z)^(1/2) = c / s
    substitution_ok = sp.simplify(integrand - d0(s ** 2) / (6 * H * s)) == 0
    norm_integral = sp.integrate(1 / (6 * H * sp.sqrt(q)), (q, 0, 1))
    say(f"integral of cot z sin(z)^(1/2) over the half 0 < x0 < pi/(12 H): "
        f"{norm_integral}")
    A_square_ok = (A * A - (m ** 2 - c_g ** 2) * sp.eye(16)).applyfunc(
        sp.expand) == zero
    A_not_hermitian = (A - A.H).applyfunc(sp.expand) != zero


    def A_numbers_of(mass, cg):
        """The matrix A as numbers: -i m gamma^(x4) + i c_g gamma^(x4) gamma^(x0)."""
        return -1j * mass * gamma[4] + 1j * cg * K_numbers


    c_g_now = 1.5 * H_value / np.sqrt(b4_start)  # c_g at x4 = 0, where a4 = 0
    rate_now = np.sqrt(c_g_now ** 2 - m_value ** 2)  # sqrt(9/4 - 1) = sqrt(5)/2
    eigenvalues = np.linalg.eigvals(A_numbers_of(m_value, c_g_now))
    upper = int(np.sum(np.abs(eigenvalues - 1j * rate_now) < 1e-9))
    lower = int(np.sum(np.abs(eigenvalues + 1j * rate_now) < 1e-9))
    report("c_g at x4 = 0 and the growth rate sqrt(c_g^2 - m^2)",
           f"{c_g_now:.4f} and {rate_now:.6f}")
    report("eigenvalues +i sqrt(5)/2 and -i sqrt(5)/2 (m = H = 1, x4 = 0), how many",
           f"{upper} and {lower}")
    check_record(substitution_ok and norm_integral == 1 / (3 * H) and A_square_ok
                 and A_not_hermitian and (upper, lower) == (8, 8)
                 and abs(rate_now - np.sqrt(5) / 2) < 1e-15,
                 "x0-independent waves: norm 1/(3 H), A^2 = (m^2 - c_g^2) I, "
                 "+-i sqrt(5)/2 at x4 = 0",
                 record="Revision/theory/reports/python-scope.json, check "
                        "good_sector_x0_independent_modes_without_boundary_condition")
    '''),
    md(r"""
    The next cell draws two figures. The first follows the 16 eigenvalues of $A$ at the
    instant $x_4 = 0$ ($c_g = 3/2$, $H = 1$) in the complex plane as $m$ grows from 0
    to 5: they are $\pm\sqrt{m^2 - c_g^2}$, on the imaginary axis for $m < c_g$ (growth)
    and on the real axis for $m > c_g$ (oscillation). The second follows the growth
    rate $\kappa(x_4) = \sqrt{c_g(x_4)^2 - m^2}$ (zero while $m \geq c_g$) along the
    history, $c_g(x_4) = \frac32He^{a_4}b_4^{-1/2} =
    \frac32Hb_4(0)^{-1/2}e^{AH(1 - \beta/2)x_4} = \frac32e^{x_4/3}$, for the masses
    $m = 0.5, 1, 2, 4$. The rate of a mass becomes positive at the time where
    $c_g(x_4) = m$, that is $x_4 = 3\ln(2m/3)$ for the record's values; the cell checks
    these times and that $c_g$ passes every mass.
    """),
    code(r'''
    mass_values = np.linspace(0.0, 5.0, 101)
    paths = np.array([np.linalg.eigvals(A_numbers_of(mass, c_g_now))
                      for mass in mass_values])
    worst = np.max(np.abs(np.sort(np.abs(paths), axis=1)
                          - np.sqrt(np.abs(mass_values ** 2 - c_g_now ** 2))[:, None]))
    report("largest deviation of |eigenvalue| from sqrt|m^2 - c_g^2|", f"{worst:.1e}")
    check(worst < 1e-6, "the eigenvalues of A follow +-sqrt(m^2 - c_g^2)")

    fig, ax = plt.subplots(figsize=(6.0, 5.0))
    growing = mass_values < c_g_now
    for column in range(16):
        ax.plot(paths[growing, column].real, paths[growing, column].imag, ".",
                color=ORANGE, markersize=4)
        ax.plot(paths[~growing, column].real, paths[~growing, column].imag, ".",
                color=BLUE, markersize=4)
    ax.plot([], [], ".", color=ORANGE, label="$m < c_g$: imaginary, the waves grow")
    ax.plot([], [], ".", color=BLUE, label="$m > c_g$: real, the waves oscillate")
    ax.plot([0, 0], [rate_now, -rate_now], "o", color=GREEN, markersize=9,
            fillstyle="none", label="$m = 1$: $\\pm i\\sqrt{5}/2$")
    ax.set_xlabel("real part of the eigenvalue of $A$ (units of $H$)")
    ax.set_ylabel("imaginary part (units of $H$)")
    ax.set_title("Frequencies of the $x_0$-independent waves at $x_4 = 0$")
    ax.legend(loc="upper left", bbox_to_anchor=(1.02, 1.0), fontsize=8)  # outside
    save_figure(fig, "frequency_paths",
                "The 16 eigenvalues of the matrix $A = -im\\gamma^{(x_4)} + "
                "ic_g\\gamma^{(x_4)}\\gamma^{(x_0)}$, which governs the good-sector "
                "waves that do not depend on $x_0$, in the complex plane (horizontal "
                "axis: real part, vertical axis: imaginary part, units of $H$) at the "
                "instant $x_4 = 0$ of the history ($a_4 = 0$, $b_4 = 1$, so $c_g = "
                "3/2$; $H = 1$) for the mass $m$ from 0 to 5. For $m < c_g$ (orange) "
                "they are $\\pm i\\sqrt{c_g^2 - m^2}$ on the imaginary axis: these "
                "finite-norm waves grow. For $m > c_g$ (blue) they are real. Green "
                "circles: $\\pm i\\sqrt{5}/2$ at $m = H = 1$.")

    rate_exponent = A_history * H_value * (1 - beta / 2)  # c_g ~ e^(x4/3) on the history


    def c_g_history(x4_value):
        """c_g = (3/2) H e^a4 b4^(-1/2) along a4 = A H x4, b4 = b4(0) e^(beta a4)."""
        return 1.5 * H_value * np.exp(rate_exponent * x4_value) / np.sqrt(b4_start)


    masses_shown = (0.5, 1.0, 2.0, 4.0)
    onsets = [np.log(2 * mass * np.sqrt(b4_start) / (3 * H_value)) / rate_exponent
              for mass in masses_shown]  # the times at which c_g(x4) = m
    report("the times x4 at which c_g reaches m = 0.5, 1, 2, 4",
           ", ".join(f"{t:.4f}" for t in onsets))
    onset_ok = all(abs(c_g_history(t) - mass) < 1e-12
                   and abs(t - 3 * np.log(2 * mass / 3)) < 1e-12
                   for mass, t in zip(masses_shown, onsets))
    slice_times = np.array(slices) / (A_history * H_value)  # the times of the slices
    check_record(abs(rate_exponent - 1 / 3) < 1e-12 and onset_ok
                 and c_g_history(slice_times).min() > m_value,
                 "history: c_g = (3/2) e^(x4/3) reaches every m at x4 = 3 ln(2 m/3)",
                 record="Revision/theory/reports/python-scope.json, check "
                        "good_sector_x0_independent_modes_without_boundary_condition")

    times = np.linspace(-4.0, 4.0, 401)
    fig, ax = plt.subplots()
    for mass, onset, colour in zip(masses_shown, onsets, (GREEN, ORANGE, BLUE, GREY)):
        kappa = np.sqrt(np.maximum(c_g_history(times) ** 2 - mass ** 2, 0.0))
        ax.plot(times, kappa, color=colour, linewidth=2, label=f"$m = {mass}$")
        ax.plot([onset], [0.0], "o", color=colour, markersize=7)
    for a4_slice in slices:
        ax.axvline(a4_slice / (A_history * H_value), color=GREEN, linestyle="--",
                   linewidth=1)
    ax.plot([], [], "--", color=GREEN, label="slices $a_{4,0}$ of the Kohn-Sham record")
    ax.set_xlabel("time $x_4$ (units of $1/H$; history $a_4 = x_4$, $b_4 = e^{4x_4/3}$)")
    ax.set_ylabel("growth rate $\\kappa$ (units of $H$)")
    ax.set_title("Without a boundary condition: every mass falls below $c_g$")
    ax.legend(loc="upper left", fontsize=8)
    save_figure(fig, "growth_rate",
                "The growth rate $\\kappa = \\sqrt{c_g^2 - m^2}$ of the instant "
                "(vertical axis, units of $H$; zero while $m \\geq c_g$) of the "
                "good-sector waves that do not depend on $x_0$, along the prescribed "
                "history $a_4 = x_4$, $b_4 = e^{4x_4/3}$ of the Revision record ($H = "
                "1$), against the time $x_4$ (horizontal axis, units of $1/H$), for "
                "$m = 0.5$, 1, 2, 4. On this history $c_g = \\frac{3}{2}e^{x_4/3}$ "
                "grows, so each curve leaves zero at the time $3\\ln(2m/3)$ (dots) and "
                "then rises like $e^{x_4/3}$: every mass falls below $c_g$. The green "
                "dashed lines mark the five slices $a_{4,0} = 0$, 0.5, 1, 1.5, 2 of the "
                "Kohn-Sham record, where $c_g \\geq 3/2 > 1$: without a boundary "
                "condition at the folds these waves grow at every slice for $m = 1$.")
    '''),
    md(r"""
    ## 9. An exact growing solution of mass 0, and where its Krein charge goes

    For $m = 0$ the equation $i\,\partial_4\chi = A\chi$ reads $\partial_4\chi =
    c_gK\chi$, and since $K^2 = I_{16}$ its solution is $\chi = e^{\theta K}\chi_0 =
    (\cosh\theta\,I_{16} + \sinh\theta\,K)\chi_0$ with $\theta(x_4)' = c_g$ and a
    constant column $\chi_0$. So $\Psi = e^{a_4/2}b_4^{-1}(\cosh\theta + \sinh\theta\,
    K)\chi_0$: the case $\alpha = 0$, $m = 0$ of the exact family of the Revision theory
    record. The next cell checks exactly that it solves the field equation of Section 4
    (with $\partial_0\Psi = 0$) for ARBITRARY functions $a_4(x_4)$ and $b_4(x_4)$.

    Then it follows it along the history from $x_4 = 0$ to $x_4 = 2$ (the range of the
    slices of the Kohn-Sham record), with $\theta(x_4) = \int_0^{x_4}c_g =
    \frac{3H}{2b_4(0)^{1/2}}\,\frac{e^{rx_4} - 1}{r}$, $r = AH(1 - \beta/2) = 1/3$,
    and a column $\chi_0$ with $B\chi_0 = \chi_0$, $\chi_0^\dagger\chi_0 = 1$ and
    $\chi_0^\dagger K\chi_0 = 0$ (the cell checks the last one). It computes the
    ordinary squared length $\Psi^\dagger\Psi = e^{a_4}b_4^{-2}\cosh 2\theta$ and the
    Krein charge $Q(x_4) = \int\sqrt{|g|}\,\Psi^\dagger B\Psi\,dx_0 =
    e^{-a_4}b_4^2\,\Psi^\dagger B\Psi/(3H)$ over the half. By Section 4 the charge
    changes at the rate of the flux through the fold: $dQ/dx_4 = -i\,[w\,\Psi^\dagger
    BM_0\Psi]_{z = \pi/2} = b_4^{3/2}\,\Psi^\dagger BK\Psi$. The cell checks that
    $Q(x_4) - Q(0)$ equals the flux added up over time (trapezoidal sums on a fine
    grid), and that the logarithm of the squared length grows at the rate
    $2c_g\tanh 2\theta - (2\beta - 1)AH$, which itself grows: faster than any
    exponential.
    """),
    code(r'''
    theta = sp.Function("theta")(x4)  # theta(x4), with theta' = c_g
    c_g_function = sp.Rational(3, 2) * H * sp.exp(a4) / sp.sqrt(b4)
    F_scale = sp.exp(a4 / 2) / b4  # e^(a4/2) b4^(-1), changing at the rate -v_g
    K_exact = g[4] * g[0]
    chi = sp.Matrix(sp.symbols("chi1:17"))  # any constant column
    Psi = F_scale * (sp.cosh(theta) * sp.eye(16) + sp.sinh(theta) * K_exact) * chi
    field_equation = (g[4] * Psi.diff(x4) + c_g_function * g[0] * Psi
                      + v_g_function * g[4] * Psi)  # m = 0 and d0 Psi = 0
    residual = field_equation.subs(sp.Derivative(theta, x4), c_g_function)
    check_record(K_exact * K_exact == sp.eye(16)
                 and residual.applyfunc(sp.simplify) == sp.zeros(16, 1),
                 "exact: e^(a4/2) b4^(-1) (cosh theta + sinh theta K) chi solves the "
                 "field equation for m = 0",
                 record="Revision/theory/reports/python-field-theory.json, check "
                        "exact_solution_family_x4_x0")


    def theta_history(x4_value):
        """theta(x4) = the integral of c_g from 0 to x4 along the history."""
        return (1.5 * H_value / np.sqrt(b4_start)
                * (np.exp(rate_exponent * x4_value) - 1) / rate_exponent)


    plus_columns = (np.eye(16) + B) / 2  # columns with B chi = chi (after scaling)
    chi_number = plus_columns[:, 0] / np.linalg.norm(plus_columns[:, 0])
    overlap = (chi_number.conj() @ K_numbers @ chi_number).real  # chi0^dagger K chi0
    x4_values = np.linspace(0.0, 2.0, 2001)
    lengths, charges, fluxes = [], [], []
    for t in x4_values:
        a4_t = A_history * H_value * t  # a4 and b4 of the history at the time t
        b4_t = b4_start * np.exp(beta * a4_t)
        th = theta_history(t)
        Psi_t = (np.exp(a4_t / 2) / b4_t
                 * (np.cosh(th) * np.eye(16) + np.sinh(th) * K_numbers) @ chi_number)
        lengths.append((Psi_t.conj() @ Psi_t).real)
        charges.append(np.exp(-a4_t) * b4_t ** 2 * (Psi_t.conj() @ B @ Psi_t).real
                       / (3 * H_value))  # Q = integral of sqrt|g| Psi^dag B Psi
        fluxes.append(b4_t ** 1.5 * (Psi_t.conj() @ B @ K_numbers @ Psi_t).real)
    lengths, charges, fluxes = map(np.array, (lengths, charges, fluxes))
    step = x4_values[1] - x4_values[0]
    added_flux = np.concatenate([[0.0], np.cumsum((fluxes[1:] + fluxes[:-1]) / 2) * step])
    relative = np.max(np.abs(charges - charges[0] - added_flux)) / np.max(np.abs(charges))
    report("chi0^dagger K chi0", f"{abs(overlap):.1f}")
    report("Krein charge Q at x4 = 0 and at x4 = 2", f"{charges[0]:.6f} and "
           f"{charges[-1]:.3f}")
    report("largest relative mismatch of Q(x4) - Q(0) and the added flux",
           f"{relative:.1e}")
    check(abs(overlap) < 1e-15 and relative < 1e-5,
          "the Krein charge changes by exactly the flux through the fold z = pi/2")
    slope = np.gradient(np.log(lengths), x4_values)  # d ln(Psi^dagger Psi) / dx4
    predicted = (2 * c_g_history(x4_values) * np.tanh(2 * theta_history(x4_values))
                 - (2 * beta - 1) * A_history * H_value)
    worst_slope = np.max(np.abs(slope[5:-5] - predicted[5:-5]))  # inner points
    report("growth rate of ln(Psi^dagger Psi) at x4 = 0.5 and at x4 = 2",
           f"{predicted[500]:.4f} and {predicted[-1]:.4f}")
    report("largest difference between the measured and the predicted rate",
           f"{worst_slope:.1e}")
    check(worst_slope < 1e-4,
          "the rate of ln(Psi^dag Psi) is 2 c_g tanh(2 theta) - 5/3, and it grows")
    '''),
    md(r"""
    The next cell draws the result: the logarithm of the ordinary squared length with
    the formula $\ln(e^{a_4}b_4^{-2}\cosh 2\theta)$ (left), and the Krein charge
    together with the flux added up over time (right).
    """),
    code(r'''
    a4_values = A_history * H_value * x4_values
    b4_values = b4_start * np.exp(beta * a4_values)
    formula = np.log(np.exp(a4_values) / b4_values ** 2
                     * np.cosh(2 * theta_history(x4_values)))
    fig, axes = plt.subplots(1, 2, figsize=(11.0, 4.2))
    axes[0].plot(x4_values, np.log(lengths), color=BLUE, linewidth=3,
                 label="$\\ln(\\Psi^\\dagger\\Psi)$ computed")
    axes[0].plot(x4_values, formula, "--", color=GREY, linewidth=1.5,
                 label="$\\ln(e^{a_4}b_4^{-2}\\cosh 2\\theta)$")
    axes[0].set_xlabel("time $x_4$ (units of $1/H$)")
    axes[0].set_ylabel("$\\ln$ of the squared length $\\Psi^\\dagger\\Psi$")
    axes[0].set_title("the wave grows faster and faster")
    axes[0].legend()
    axes[1].plot(x4_values, charges, color=ORANGE, linewidth=3,
                 label="Krein charge $Q(x_4)$")
    axes[1].plot(x4_values, charges[0] + added_flux, "--", color=GREEN, linewidth=2,
                 label="$Q(0)$ + flux through the fold")
    axes[1].set_xlabel("time $x_4$ (units of $1/H$)")
    axes[1].set_ylabel("Krein charge (units of $1/H$)")
    axes[1].set_title("not conserved: it changes by the flux")
    axes[1].legend()
    save_figure(fig, "krein_leak",
                "The exact good-sector solution $\\Psi = e^{a_4/2}b_4^{-1}(\\cosh\\theta "
                "+ \\sinh\\theta\\,K)\\chi_0$ of mass 0, independent of $x_0$, with "
                "$\\theta' = c_g$, along the history $a_4 = x_4$, $b_4 = e^{4x_4/3}$ "
                "($H = 1$) from $x_4 = 0$ to 2, for a column $\\chi_0$ with $B\\chi_0 = "
                "\\chi_0$; horizontal axes: the time $x_4$ in units of $1/H$. Left: the "
                "logarithm of its squared length (blue) lies on the formula "
                "$\\ln(e^{a_4}b_4^{-2}\\cosh 2\\theta)$ (grey dashed); its slope keeps "
                "increasing because $c_g$ grows. Right: its Krein charge $Q = "
                "\\int\\sqrt{|g|}\\,\\Psi^\\dagger B\\Psi\\,dx_0$ over the half $0 < z < "
                "\\pi/2$ (orange) grows from $1/3$ to about 844; it equals its starting "
                "value plus the flux through the fold $z = \\pi/2$ added up over time "
                "(green dashed). Without a boundary condition at the fold the Krein "
                "charge is not conserved.")
    '''),
    md(r"""
    ## 10. The last check

    The last cell checks that all five figure files exist in the folder
    Revision/textbook/figures and prints the number of checks that passed.
    """),
    code(r'''
    for name in ("10d_1_volume_and_flux.png", "10d_2_symmetry_defect.png",
                 "10d_3_frequency_paths.png", "10d_4_growth_rate.png",
                 "10d_5_krein_leak.png"):
        check(output_file(f"{FIGURE_FOLDER}/{name}").is_file(),
              f"the figure file {name} exists")
    all_checks_passed()
    '''),
    md(r"""
    ## 11. What this notebook showed

    - REPRODUCED: the volume factor $\sqrt{|g|} = e^{-a_4}b_4^2|\cot z|(\sin^2 z)^{1/4}$
      and the spin-connection term $c_g\gamma^{(x_0)} + v_g\gamma^{(x_4)}$ of the
      corrected metric, read from the Revision theory record; PROVED (exactly):
      $\partial_4\sqrt{|g|} = 2v_g\sqrt{|g|}$.
    - PROVED (exactly): the good-sector mode operator along the hidden direction,
      $h = -im\gamma^{(x_4)} + ic_g\gamma^{(x_4)}\gamma^{(x_0)} +
      ie^{a_4}b_4^{-1/2}\tan z\,\gamma^{(x_4)}\gamma^{(x_0)}\partial_0 - iv_g$, satisfies
      $\sqrt{|g|}\,[u^\dagger(hv) - (hu)^\dagger v] = \partial_0(w\,u^\dagger M_0v) -
      2iv_g\sqrt{|g|}\,u^\dagger v$ with $w = b_4^{3/2}\sin^{1/2}z$; the part $-iv_g$
      compensates the time dependence of the volume, so the inner product of two
      solutions changes only by the bracket at the ends, which vanishes where
      $\sin z = 0$ but not at the fold $z = \pi/2$ (flux factor $2i$ for the recorded
      column). The Krein form is conserved up to the analogous term.
    - PROVED: the spin-connection term $c_g\gamma^{(x_0)}$ is what makes the defect a
      pure boundary term in these variables and this volume; without it the remainder
      $-2c_g\sqrt{|g|}\,u^\dagger M_0v$ survives. (In the variables $\chi$ with $\Psi =
      e^{a_4/2}b_4^{-1}(\sin^2 z)^{-1/8}\chi$ no such term is needed: this role of the
      spin connection depends on the variables, as the Revision record states.)
    - PROVED: the good-sector waves that do not depend on $x_0$ have a finite norm and
      evolve with $A$, $A^2 = (m^2 - c_g^2)I_{16}$; wherever $m^2 < c_g^2$ they grow (at
      $x_4 = 0$ of the history with $m = H = 1$ the eigenvalues are $\pm i\sqrt5/2$).
      COMPUTED: along the prescribed history $c_g = \frac32e^{x_4/3}$ reaches every mass,
      at $x_4 = 3\ln(2m/3)$; for $m = 1$ these waves grow at all five slices of the
      Kohn-Sham record.
    - PROVED (exactly) and COMPUTED: the exact solution of mass 0 of the record's family
      grows faster than any exponential, and its Krein charge is not conserved: it
      changes by exactly the flux through the fold (from $1/3$ at $x_4 = 0$ to 843.742
      at $x_4 = 2$).
    - CONSEQUENCE (the scope of the quantisation in the Revision record): Hermiticity of
      the curved good-sector evolution and conservation of the Krein charge need a
      boundary condition at the folds $z = \pi/2 + n\pi$ (the Kohn-Sham record ASSUMES
      fold conditions for its states); the Revision quantisation imposes none. The
      positive Fock space of the previous notebook is built for single good-sector
      momenta with frozen coefficients; a positive Hilbert space for the whole field is
      not constructed. ASSUMED: the history $a_4 = AHx_4$, $b_4 = b_4(0)e^{\beta AHx_4}$
      is a prescribed background.
    """),
]

if __name__ == "__main__":
    raise SystemExit(run_builder(__file__))
