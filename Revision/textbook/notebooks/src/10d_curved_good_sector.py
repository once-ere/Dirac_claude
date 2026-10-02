#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
"""Builder of Notebook 10d, "The curved good sector and the boundary at z = pi/2"
(textbook "Universes in Pairs", chapter 10: canonical quantisation in 4+4, the Krein
space and the good sector).

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
    "title": "The curved good sector and the boundary at z = pi/2",
    "purpose": (
        "In the author's metric it writes the good-sector mode operator along the hidden "
        "direction, proves exactly with sympy that it is symmetric, and that the Krein "
        "form is conserved, only up to a boundary term that vanishes at the tip z = 0 "
        "but not at the patch end z = pi/2, shows that without the spin-connection "
        "term 3 H a remainder survives, shows that the waves independent of x8 (finite "
        "norm) have the frequencies squared m^2 - 9 H^2 and therefore grow for m below "
        "3 H, checks an exact growing solution and that its Krein charge changes by "
        "exactly the flux through z = pi/2, reproduces the recorded numbers, and draws "
        "five teaching figures."
    ),
    "records": [
        ["Revision/algebra/gammas.json", "the author's gamma matrices (read)"],
        ["Revision/theory/reports/wolfram-field-theory.json",
         "checks good_sector_hermiticity_curved and Krein_form_conserved_curved "
         "(reproduced)"],
        ["Revision/theory/reports/python-scope.json",
         "checks good_sector_hermiticity_up_to_the_brane_flux and "
         "good_sector_x8_independent_modes_without_boundary_condition (reproduced)"],
        ["Revision/theory/reports/python-field-theory.json",
         "check exact_solution_family_x4_x8 (reproduced in its case alpha = 0)"],
    ],
    "packages": ["numpy", "sympy", "matplotlib"],
    "needs_rust": [],
    "expected_seconds": 20,
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
        "ALL 16 CHECKS PASSED (notebook 10d)",
    ],
    "troubleshooting": [
        ["\"FileNotFoundError\" for gammas.json",
         "the notebook reads one file of the repository; it must be opened inside the "
         "folder Revision/textbook/notebooks of a complete copy of the repository. Clone "
         "the repository again and open the notebook there."],
    ],
}

CELLS = [
    md(r"""
    ## 1. What this notebook computes

    The previous notebooks of this chapter worked with plane waves in flat 4+4 space (or
    with the coefficients frozen at one point). This notebook goes back to the author's
    curved metric and looks at the good sector (no dependence on the extra times
    $x_5, x_6, x_7$) along the hidden direction $x_8$, with $z = 6Hx_8$ running from
    the tip $z = 0$ to the patch end $z = \pi/2$. It

    - writes the mode operator $h$ of the field equation for waves that depend only on
      $x_4$ and $x_8$: $i\,\partial_4\Psi = h\Psi$;
    - proves exactly (sympy) that $h$ is symmetric for the volume $\cos z\,dx_8$ only up
      to a boundary term $\partial_8(\sin z\,u^\dagger M_8v)$, and that the Krein form is
      conserved only up to a similar term; the term vanishes at the tip but NOT at
      $z = \pi/2$;
    - shows that the spin-connection term $3H\gamma^{(x_8)}$ of the field equation is
      exactly what makes the hidden-direction operator symmetric up to that boundary
      term (without it a remainder $-6H\cos z\,u^\dagger M_8v$ survives);
    - shows that the waves that do not depend on $x_8$ (they have a finite norm) see the
      matrix $A = -im\gamma^{(x_4)} + 3iH\gamma^{(x_4)}\gamma^{(x_8)}$, with $A^2 = (m^2 -
      9H^2)I_{16}$: for $m < 3H$ their frequencies are imaginary and they grow;
    - checks an exact growing solution, and that its Krein charge changes in time by
      exactly the flux through $z = \pi/2$;
    - reproduces the recorded numbers and draws five teaching figures.

    The message for the chapter: the positive Fock space of the previous notebook is a
    construction for flat space (frozen coefficients). In the curved good sector the
    evolution is Hermitian, and the Krein charge conserved, only if a boundary condition
    is imposed at $z = \pi/2$, and the Revision record imposes none.
    """),
    md(r"""
    ## 3. The words used in this notebook

    - **Hidden direction, $z$, tip, patch end**: $x_8$ is the hidden space direction;
      $z = 6Hx_8$ runs over $0 < z < \pi/2$. The *tip* is $z \to 0$, the *patch end* is
      $z = \pi/2$, where the author's metric component $g_{88} = \cot^2 z$ and the volume
      factor $\sqrt{|g|} = \cos z$ vanish.
    - **Volume element**: $\sqrt{|g|} = \cos z$; an integral over the hidden direction
      is $\int \cos z\,(\ldots)\,dx_8$.
    - **Symmetric operator (formally Hermitian)**: an operator $h$ with
      $\int\cos z\,u^\dagger(hv)\,dx_8 = \int\cos z\,(hu)^\dagger v\,dx_8$ for all
      wave functions $u, v$. A *boundary term* is a part of the integrand that is a
      derivative, $\partial_8(\ldots)$; its integral is the difference of the bracket at
      the two ends, so the operator is symmetric when that difference vanishes.
    - **Krein form, Krein charge**: $\int\cos z\,u^\dagger Bv\,dx_8$; for $u = v = \Psi$
      it is the charge of the wave.
    - **Flux**: the value of the bracket at an end; a nonzero flux at $z = \pi/2$ means
      that something flows through the patch end (in or out).
    - **Boundary condition**: a rule imposed on the wave functions at an end (for
      example that a flux vanishes there); it is an assumption added to the equations.
    - **$M_8$**: the matrix $i\gamma^{(x_4)}\gamma^{(x_8)}$.
    - **Exponential of a matrix**: $e^{Mx_4} = \sum_n (Mx_4)^n/n!$; if $M^2 = k^2 I$ the
      series collapses to $\cosh(kx_4)I + \frac{\sinh(kx_4)}{k}M$ (even and odd powers).
    """),
    md(r"""
    ## 4. The physical and mathematical situation

    **The field equation for waves in $x_4$ and $x_8$ only.** The field equation of
    dirac16complex in the author's metric (Revision theory record, $U = 0$) is

    $$e^{-a_4}\sin^{-1/6}z\sum_{i=1}^3\gamma^{(x_i)}\partial_i\Psi + \gamma^{(x_4)}
    \partial_4\Psi + e^{a_4}\sin^{-1/6}z\sum_{t=5}^7\gamma^{(x_t)}\partial_t\Psi +
    \tan z\,\gamma^{(x_8)}\partial_8\Psi + 3H\gamma^{(x_8)}\Psi = m\Psi .$$

    For a wave that depends only on $x_4$ and $x_8$ the first and third groups vanish:

    $$\gamma^{(x_4)}\partial_4\Psi + \tan z\,\gamma^{(x_8)}\partial_8\Psi +
    3H\gamma^{(x_8)}\Psi = m\Psi .$$

    Multiply from the left by $\gamma^{(x_4)}$, use $(\gamma^{(x_4)})^2 = -1$ and solve
    for $\partial_4\Psi$:

    $$\partial_4\Psi = -m\gamma^{(x_4)}\Psi + \tan z\,\gamma^{(x_4)}\gamma^{(x_8)}
    \partial_8\Psi + 3H\gamma^{(x_4)}\gamma^{(x_8)}\Psi .$$

    Multiply by $i$:

    $$i\,\partial_4\Psi = h\Psi,\qquad h = A + D\,\partial_8,\qquad
    A = -im\gamma^{(x_4)} + 3iH\gamma^{(x_4)}\gamma^{(x_8)},\qquad D = \tan z\,M_8,
    \qquad M_8 = i\gamma^{(x_4)}\gamma^{(x_8)} .$$

    **Symmetry up to a boundary term, line by line.** Write $u'$ for $\partial_8u$. Then

    $$u^\dagger(hv) - (hu)^\dagger v = u^\dagger(A - A^\dagger)v + u^\dagger Dv' -
    u'^\dagger D^\dagger v .$$

    The notebook checks that $M_8$ is anti-Hermitian, so $D^\dagger = -D$ ($\tan z$ is
    real), and the last two terms are $u^\dagger Dv' + u'^\dagger Dv =
    (u^\dagger Dv)' - u^\dagger D'v$ (product rule). Multiply by $\cos z$. The notebook
    checks the two matrix identities $\cos z\,D = \sin z\,M_8$ and
    $\cos z\,(A - A^\dagger) = (\sin z)'M_8$; with them (and the product rule
    $(\cos z\,D)' = (\cos z)'D + \cos z\,D'$) everything collects into one derivative:

    $$\cos z\,\big[u^\dagger(hv) - (hu)^\dagger v\big] = \partial_8\big(\sin z\;
    u^\dagger M_8 v\big).$$

    Integrated over $0 < z < \pi/2$ this is $[\sin z\,u^\dagger M_8v]$ at $z = \pi/2$
    minus its value at $z = 0$. At the tip $\sin z = 0$; at the patch end $\sin z = 1$,
    so the flux $u^\dagger M_8v$ there does not vanish in general. The term
    $3iH\gamma^{(x_4)}\gamma^{(x_8)}$ of $A$ (the spin-connection term $3H\gamma^{(x_8)}$
    of the field equation) supplies exactly $A - A^\dagger = 6HM_8$, which is needed
    because $(\sin z)' = 6H\cos z$.

    **Waves that do not depend on $x_8$.** For them $\partial_8\Psi = 0$ and $h$ acts as
    the constant matrix $A$. Their norm $\int_0^{\pi/(12H)}\cos(6Hx_8)\,dx_8 = 1/(6H)$ is
    finite (the patch $0 < z < \pi/2$ is $0 < x_8 < \pi/(12H)$), so they are honest
    members of the good sector. The notebook proves $A^2 = (m^2 - 9H^2)I_{16}$: for
    $m < 3H$ the frequencies are imaginary and these waves grow.
    """),
    md(r"""
    ## 5. The matrices of the hidden direction

    The next cell reads the gammas, builds $C$ and $B$ with numpy and as exact sympy
    matrices, defines the symbols $m$, $H$ (positive) and $x_8$, the expression
    $z = 6Hx_8$, and the matrices $M_8$, $A$ and $D$ of Section 4. It also defines
    `check_record` (the PASS line and the line of the reproduced Revision record are
    printed in one piece, so that the stored output is the same in every run) and the
    colours. Then it checks the matrix facts of Section 4 exactly:
    $M_8^\dagger = -M_8$, $\cos z\,D = \sin z\,M_8$ and $\cos z\,(A - A^\dagger) =
    \partial_8(\sin z)\,M_8$, and in addition that $B$ commutes with $\gamma^{(x_4)}$ and
    $\gamma^{(x_8)}$. The last fact gives the Krein version: $B$ then commutes with $A$,
    $A^\dagger$, $D$ and $M_8$, so the same steps with $u^\dagger B$ in place of
    $u^\dagger$ give $\cos z\,[u^\dagger B(hv) - (hu)^\dagger Bv] = \partial_8(\sin z\,
    u^\dagger BM_8v)$.
    """),
    code(r'''
    import contextlib  # lets a block of code print into a text buffer
    import io  # the text buffer
    import sys  # the screen output, sys.stdout

    import numpy as np  # numbers, arrays and matrices
    import sympy as sp  # exact algebra with symbols


    def check_record(condition, name, record):
        """check(condition, name, record=record), printed in one piece."""
        buffer = io.StringIO()
        with contextlib.redirect_stdout(buffer):  # what check prints goes to buffer
            check(condition, name, record=record)
        sys.stdout.write(buffer.getvalue())  # one single piece of output


    BLUE, ORANGE, GREEN, GREY = "#2a78d6", "#eb6834", "#1baf7a", "#52514e"
    fixture = json.loads(repository_file("Revision/algebra/gammas.json").read_text(
        encoding="utf-8"))
    gamma = {a: np.array(fixture["gamma"][a - 1], dtype=float) for a in range(1, 9)}
    C = gamma[8] @ gamma[1] @ gamma[2] @ gamma[3]
    B = -1j * (C @ gamma[4])  # B = -i C gamma^(x4)
    g = {a: sp.Matrix(fixture["gamma"][a - 1]) for a in range(1, 9)}  # exact gammas
    B_exact = -sp.I * g[8] * g[1] * g[2] * g[3] * g[4]

    m = sp.Symbol("m", real=True)  # the mass
    H = sp.Symbol("H", positive=True)  # the author's constant H > 0
    x8 = sp.Symbol("x8", real=True)  # the hidden coordinate
    z = 6 * H * x8  # z = 6 H x8
    M8 = sp.I * g[4] * g[8]  # M_8 = i gamma^(x4) gamma^(x8)
    A = -sp.I * m * g[4] + 3 * sp.I * H * g[4] * g[8]  # the part without derivative
    A_no_connection = -sp.I * m * g[4]  # the same without the term 3 H
    D = sp.tan(z) * M8  # the coefficient of the derivative d/dx8
    zero = sp.zeros(16, 16)
    anti_hermitian = M8.H == -M8
    identity_D = (sp.cos(z) * D - sp.sin(z) * M8).applyfunc(sp.simplify) == zero
    identity_A = (sp.cos(z) * (A - A.H) - sp.diff(sp.sin(z), x8) * M8).applyfunc(
        sp.simplify) == zero
    B_commutes = (B_exact * g[4] == g[4] * B_exact) and (B_exact * g[8] == g[8] * B_exact)
    say(f"M8 anti-Hermitian: {anti_hermitian}; cos z D = sin z M8: {identity_D}; "
        f"cos z (A - A^dagger) = d8(sin z) M8: {identity_A}; B commutes with "
        f"gamma^(x4) and gamma^(x8): {B_commutes}")
    check(anti_hermitian and identity_D and identity_A and B_commutes,
          "exact: the four matrix identities of the hidden direction")
    '''),
    md(r"""
    ## 6. Symmetric up to a boundary term, checked on wave functions

    The matrix identities prove the statement of Section 4 for all wave functions. The
    next cell also checks it directly on two concrete wave functions $u(x_8)$ and
    $v(x_8)$: each of their 16 entries is a combination $a + b\sin z + c\cos z$ with
    small whole numbers $a, b, c$ (real and imaginary parts chosen at random with a
    fixed seed). It computes, exactly,

    - the defect $\cos z\,[u^\dagger(hv) - (hu)^\dagger v] - \partial_8(\sin z\,u^\dagger
      M_8v)$, which must be 0;
    - the same with the operator WITHOUT the spin-connection term, which must equal
      $-6H\cos z\,u^\dagger M_8v$ instead;
    - the Krein version $\cos z\,[u^\dagger B(hv) - (hu)^\dagger Bv] - \partial_8(\sin z
      \,u^\dagger BM_8v)$, which must be 0.

    To let sympy recognise the zeros, $x_8$ is replaced by $z/(6H)$ and the
    trigonometric functions are expanded before simplifying.
    """),
    code(r'''
    rng = np.random.default_rng(12345)


    def test_function():
        """16 entries a + b sin z + c cos z with small random whole numbers."""
        def number():
            return int(rng.integers(-3, 4)) + sp.I * int(rng.integers(-3, 4))
        return sp.Matrix([number() + number() * sp.sin(z) + number() * sp.cos(z)
                          for _ in range(16)])


    def apply_h(matrix_A, w):
        """h w = A w + D dw/dx8 for a column w of functions of x8."""
        return matrix_A * w + D * w.diff(x8)


    def is_zero(expression):
        """Exact zero test: write x8 = z / (6 H), expand the trigonometric functions."""
        zz = sp.Symbol("zz")
        rewritten = sp.expand_trig(sp.expand(expression.subs(x8, zz / (6 * H))))
        return sp.simplify(rewritten) == 0


    u, v = test_function(), test_function()
    hv, hu = apply_h(A, v), apply_h(A, u)
    defect = (sp.cos(z) * ((u.H * hv)[0] - (hu.H * v)[0])
              - sp.diff(sp.sin(z) * (u.H * M8 * v)[0], x8))
    hv0, hu0 = apply_h(A_no_connection, v), apply_h(A_no_connection, u)
    defect_without = (sp.cos(z) * ((u.H * hv0)[0] - (hu0.H * v)[0])
                      - sp.diff(sp.sin(z) * (u.H * M8 * v)[0], x8))
    remainder_ok = is_zero(defect_without + 6 * H * sp.cos(z) * (u.H * M8 * v)[0])
    krein_defect = (sp.cos(z) * ((u.H * B_exact * hv)[0] - (hu.H * B_exact * v)[0])
                    - sp.diff(sp.sin(z) * (u.H * B_exact * M8 * v)[0], x8))
    check_record(is_zero(defect),
                 "exact: cos z (u^dagger h v - (h u)^dagger v) = d8(sin z u^dagger M8 v)",
                 record="Revision/theory/reports/python-scope.json, check "
                        "good_sector_hermiticity_up_to_the_brane_flux")
    check_record(remainder_ok,
                 "exact: without the term 3 H the remainder -6 H cos z u^dagger M8 v stays",
                 record="Revision/theory/reports/wolfram-field-theory.json, check "
                        "good_sector_hermiticity_curved")
    check_record(is_zero(krein_defect),
                 "exact: the Krein form is conserved up to d8(sin z u^dagger B M8 v)",
                 record="Revision/theory/reports/wolfram-field-theory.json, check "
                        "Krein_form_conserved_curved")
    '''),
    md(r"""
    ## 7. The flux at the two ends

    The bracket $\sin z\,u^\dagger M_8v$ vanishes at the tip ($\sin 0 = 0$) for wave
    functions that stay finite there, but at the patch end $z = \pi/2$ it is
    $u^\dagger M_8v$. The Revision record gives an example: the matrix
    $\gamma^{(x_4)}\gamma^{(x_8)}$ is real, symmetric and squares to $I$, so it has the
    eigenvalue $+1$; for a column with $\gamma^{(x_4)}\gamma^{(x_8)}u = u$ and
    $u^\dagger u = 2$ the flux is $u^\dagger M_8u = i\,u^\dagger u = 2i$, not 0. The next
    cell builds such a column ($u = e_A + \gamma^{(x_4)}\gamma^{(x_8)}e_A$ for the first
    unit column $e_A$) and draws the volume factor $\cos z$ and the flux factor
    $\sin z$ along the hidden direction.
    """),
    code(r'''
    G48 = gamma[4] @ gamma[8]  # gamma^(x4) gamma^(x8), real
    symmetric_square = np.array_equal(G48, G48.T) and np.array_equal(G48 @ G48,
                                                                      np.eye(16))
    e_first = np.eye(16)[:, 0]
    u_flux = e_first + G48 @ e_first  # an eigenvector of G48 with eigenvalue +1
    M8_numbers = 1j * G48
    flux_value = u_flux.conj() @ M8_numbers @ u_flux
    report("u^dagger u for the column u = e_1 + gamma4 gamma8 e_1", f"{u_flux @ u_flux:.1f}")
    report("flux u^dagger M8 u at z = pi/2",
           f"{flux_value.imag:.1f} i (real part {abs(flux_value.real):.1f})")
    check_record(symmetric_square and np.allclose(G48 @ u_flux, u_flux)
                 and abs(flux_value - 2j) < 1e-14,
                 "the flux at z = pi/2 is u^dagger M8 u = 2 i for gamma4 gamma8 u = u",
                 record="Revision/theory/reports/python-scope.json, check "
                        "good_sector_hermiticity_up_to_the_brane_flux")

    z_values = np.linspace(0.0, np.pi / 2, 400)
    fig, ax = plt.subplots()
    ax.plot(z_values, np.cos(z_values), color=BLUE, linewidth=2,
            label="volume factor $\\sqrt{|g|} = \\cos z$")
    ax.plot(z_values, np.sin(z_values), color=ORANGE, linewidth=2,
            label="flux factor $\\sin z$ of the bracket")
    ax.plot([0.0], [0.0], "o", color=ORANGE, markersize=8)
    ax.plot([np.pi / 2], [1.0], "o", color=ORANGE, markersize=8)
    ax.annotate("tip: the flux vanishes", (0.0, 0.0), xytext=(0.15, 0.25),
                arrowprops={"arrowstyle": "->", "color": GREY})
    ax.annotate("patch end: the flux remains", (np.pi / 2, 1.0), xytext=(0.55, 1.08),
                arrowprops={"arrowstyle": "->", "color": GREY})
    ax.set_xlabel("$z = 6 H x_8$ (from the tip $z = 0$ to the patch end $z = \\pi/2$)")
    ax.set_ylabel("value")
    ax.set_ylim(-0.05, 1.25)
    ax.set_title("The hidden direction: volume and boundary flux")
    ax.legend(loc="center left")
    save_figure(fig, "volume_and_flux",
                "Along the hidden direction, $z = 6Hx_8$ from the tip $z = 0$ to the "
                "patch end $z = \\pi/2$ (horizontal axis): the volume factor $\\sqrt{|g|}"
                " = \\cos z$ of the author's metric (blue) and the factor $\\sin z$ of "
                "the boundary bracket $\\sin z\\,u^\\dagger M_8 v$ (orange); vertical "
                "axis: pure numbers. The volume vanishes at the patch end, but the "
                "bracket there is $u^\\dagger M_8 v$, for example $2i$ for the recorded "
                "column: the mode operator is symmetric, and the Krein charge "
                "conserved, only if a boundary condition removes this flux at $z = "
                "\\pi/2$.")
    '''),
    md(r"""
    The next cell makes the role of the spin-connection term visible for one pair of
    wave functions, here $u = v$ (the test function $u$ of Section 6) at $m = H = 1$:
    it evaluates along $0 < z < \pi/2$ the left-hand side $\cos z\,[u^\dagger(hu) -
    (hu)^\dagger u]$, the right-hand side $\partial_8(\sin z\,u^\dagger M_8u)$, and the
    left-hand side computed WITHOUT the term $3H$. For $u = v$ all three are purely
    imaginary (a number minus its complex conjugate), so their imaginary parts are
    plotted. The exact expressions are turned into fast numerical functions with
    `sp.lambdify`.
    """),
    code(r'''
    numbers = {m: 1, H: 1}  # m = H = 1, so z = 6 x8
    hu_full, hu_bare = apply_h(A, u), apply_h(A_no_connection, u)
    left = sp.cos(z) * ((u.H * hu_full)[0] - (hu_full.H * u)[0])
    right = sp.diff(sp.sin(z) * (u.H * M8 * u)[0], x8)
    left_bare = sp.cos(z) * ((u.H * hu_bare)[0] - (hu_bare.H * u)[0])
    x8_values = np.linspace(0.002, np.pi / 12 - 0.002, 300)  # inside 0 < z < pi/2
    curves = [np.imag(sp.lambdify(x8, e.subs(numbers), "numpy")(x8_values))
              for e in (left, right, left_bare)]
    difference = np.max(np.abs(curves[0] - curves[1]))
    report("largest |left - right| on the grid", f"{difference:.1e}")
    check(difference < 1e-9, "numerical: the two sides agree along the hidden direction")

    fig, ax = plt.subplots()
    ax.plot(6 * x8_values, curves[0], color=BLUE, linewidth=3,
            label="left side, with the term $3H$")
    ax.plot(6 * x8_values, curves[1], "--", color=GREEN, linewidth=2,
            label="right side $\\partial_8(\\sin z\\,u^\\dagger M_8 u)$")
    ax.plot(6 * x8_values, curves[2], color=ORANGE, linewidth=2,
            label="left side WITHOUT the term $3H$")
    ax.set_xlabel("$z = 6 H x_8$ ($m = H = 1$)")
    ax.set_ylabel("imaginary part")
    ax.set_title("The spin-connection term makes the defect a pure boundary term")
    ax.legend(fontsize=8)
    save_figure(fig, "symmetry_defect",
                "For one concrete wave function $u(x_8)$ (16 entries of the form $a + "
                "b\\sin z + c\\cos z$) and $m = H = 1$: the imaginary parts of the "
                "symmetry defect $\\cos z\\,(u^\\dagger(hu) - (hu)^\\dagger u)$ of the "
                "curved good-sector mode operator (blue), of the derivative "
                "$\\partial_8(\\sin z\\,u^\\dagger M_8u)$ (green dashed, on top of the "
                "blue curve), and of the defect of the operator without the "
                "spin-connection term $3H$ (orange), against $z$ (horizontal axis). "
                "With the term the defect is exactly a derivative, whose integral "
                "is the flux at the ends; without it a remainder $-6H\\cos z\\,"
                "u^\\dagger M_8u$ survives.")
    '''),
    md(r"""
    ## 8. Waves that do not depend on $x_8$: growth for $m < 3H$

    For a wave that depends on $x_4$ only, $h$ acts as the constant matrix $A$. The next
    cell checks exactly: the norm integral $\int_0^{\pi/(12H)}\cos(6Hx_8)\,dx_8 =
    1/(6H)$ is finite; $A$ is not Hermitian; $A^2 = (m^2 - 9H^2)I_{16}$ (the same
    cancellation of mixed terms as for the mode Hamiltonian of flat space, because
    $\gamma^{(x_4)}$ and $\gamma^{(x_4)}\gamma^{(x_8)}$ anticommute); and at $m = H = 1$
    the eigenvalues are $\pm 2\sqrt2\,i$, eight of each (the trace of $A$ is 0).
    """),
    code(r'''
    norm_integral = sp.integrate(sp.cos(6 * H * x8), (x8, 0, sp.pi / (12 * H)))
    say(f"integral of cos(6 H x8) over the patch: {norm_integral}")
    A_square_ok = (A * A - (m ** 2 - 9 * H ** 2) * sp.eye(16)).applyfunc(
        sp.expand) == zero
    A_not_hermitian = (A - A.H).applyfunc(sp.expand) != zero
    G48_numbers = gamma[4] @ gamma[8]  # gamma^(x4) gamma^(x8) as numbers


    def A_numbers_of(mass, H_value=1.0):
        """The matrix A as numbers: -i m gamma^(x4) + 3 i H gamma^(x4) gamma^(x8)."""
        return -1j * mass * gamma[4] + 3j * H_value * G48_numbers


    A_numbers = A_numbers_of(1.0)
    eigenvalues = np.linalg.eigvals(A_numbers)
    upper = int(np.sum(np.abs(eigenvalues - 2j * np.sqrt(2)) < 1e-9))
    lower = int(np.sum(np.abs(eigenvalues + 2j * np.sqrt(2)) < 1e-9))
    report("eigenvalues 2 sqrt(2) i and -2 sqrt(2) i at m = H = 1, how many",
           f"{upper} and {lower}")
    check_record(norm_integral == 1 / (6 * H) and A_square_ok and A_not_hermitian
                 and (upper, lower) == (8, 8),
                 "x8-independent waves: A^2 = (m^2 - 9 H^2) I, at m = H = 1: +-2 sqrt(2) i",
                 record="Revision/theory/reports/python-scope.json, check "
                        "good_sector_x8_independent_modes_without_boundary_condition")
    '''),
    md(r"""
    The next cell draws two figures. The first follows the 16 eigenvalues of $A$ (with
    $H = 1$) in the complex plane as $m$ grows from 0 to 5: they are $\pm\sqrt{m^2 -
    9H^2}$, on the imaginary axis for $m < 3H$ (growth) and on the real axis for
    $m > 3H$ (oscillation). The second shows the growth rate
    $\kappa = \sqrt{9H^2 - m^2}$ (zero for $m \geq 3H$) against $m/H$, with the recorded
    point $m = H = 1$, $\kappa = 2\sqrt2$.
    """),
    code(r'''
    mass_values = np.linspace(0.0, 5.0, 101)
    paths = []
    for mass in mass_values:
        paths.append(np.linalg.eigvals(A_numbers_of(mass)))
    paths = np.array(paths)
    worst = np.max(np.abs(np.sort(np.abs(paths), axis=1)
                          - np.sqrt(np.abs(mass_values ** 2 - 9))[:, None]))
    report("largest deviation of |eigenvalue| from sqrt|m^2 - 9|", f"{worst:.1e}")
    check(worst < 1e-6, "the eigenvalues of A follow +-sqrt(m^2 - 9 H^2)")

    fig, ax = plt.subplots(figsize=(6.0, 5.0))
    growing = mass_values < 3.0
    for column in range(16):
        ax.plot(paths[growing, column].real, paths[growing, column].imag, ".",
                color=ORANGE, markersize=4)
        ax.plot(paths[~growing, column].real, paths[~growing, column].imag, ".",
                color=BLUE, markersize=4)
    ax.plot([], [], ".", color=ORANGE, label="$m < 3H$: imaginary, the waves grow")
    ax.plot([], [], ".", color=BLUE, label="$m > 3H$: real, the waves oscillate")
    ax.plot([0, 0], [2 * np.sqrt(2), -2 * np.sqrt(2)], "o", color=GREEN, markersize=9,
            fillstyle="none", label="recorded: $m = H = 1$, $\\pm 2\\sqrt{2}\\,i$")
    ax.set_xlabel("real part of the eigenvalue of $A$ (units of $H$)")
    ax.set_ylabel("imaginary part (units of $H$)")
    ax.set_aspect("equal")
    ax.set_title("Frequencies of the $x_8$-independent waves, $m$ from 0 to 5")
    ax.legend(loc="lower right", fontsize=8)
    save_figure(fig, "frequency_paths",
                "The 16 eigenvalues of the matrix $A = -im\\gamma^{(x_4)} + "
                "3iH\\gamma^{(x_4)}\\gamma^{(x_8)}$, which governs the good-sector waves "
                "that do not depend on $x_8$, in the complex plane (horizontal axis: "
                "real part, vertical axis: imaginary part, units of $H$) for $H = 1$ "
                "and the mass $m$ from 0 to 5. For $m < 3H$ (orange) they are "
                "$\\pm i\\sqrt{9H^2 - m^2}$ on the imaginary axis: these finite-norm "
                "waves grow. For $m > 3H$ (blue) they are real. Green circles: the "
                "recorded values $\\pm 2\\sqrt{2}\\,i$ at $m = H = 1$.")

    rate = np.sqrt(np.maximum(9.0 - mass_values ** 2, 0.0))
    fig, ax = plt.subplots()
    ax.plot(mass_values, rate, color=ORANGE, linewidth=2,
            label="growth rate $\\kappa = \\sqrt{9H^2 - m^2}$")
    ax.plot([1.0], [2 * np.sqrt(2)], "o", color=GREEN, markersize=9,
            label="recorded: $m = H = 1$, $\\kappa = 2\\sqrt{2}$")
    ax.axvline(3.0, color=GREY, linestyle=":", linewidth=1)
    ax.set_xlabel("mass $m$ in units of $H$")
    ax.set_ylabel("growth rate $\\kappa$ (units of $H$)")
    ax.set_title("Without a boundary condition: growth for $m < 3H$")
    ax.legend()
    save_figure(fig, "growth_rate",
                "The growth rate $\\kappa = \\sqrt{9H^2 - m^2}$ (vertical axis, units of "
                "$H$) of the good-sector waves that do not depend on $x_8$ in the "
                "author's metric, against the mass $m$ (horizontal axis, units of $H$). "
                "It is positive for $m < 3H$ (left of the dotted line) and zero for "
                "$m \\geq 3H$; the green dot is the recorded value $2\\sqrt{2}$ at "
                "$m = H = 1$. These waves have a finite norm, so without a boundary "
                "condition at $z = \\pi/2$ the curved good sector contains growing "
                "waves.")
    '''),
    md(r"""
    ## 9. An exact growing solution, and where its Krein charge goes

    For a wave of $x_4$ alone the equation $i\partial_4\Psi = A\Psi$ reads
    $\partial_4\Psi = M\Psi$ with $M = -iA = -m\gamma^{(x_4)} + 3H\gamma^{(x_4)}
    \gamma^{(x_8)}$, and $M^2 = (9H^2 - m^2)I = k^2I$. Its solution is $\Psi(x_4) =
    e^{Mx_4}\chi = \big(\cosh(kx_4)I + \frac{\sinh(kx_4)}{k}M\big)\chi$ for any constant
    column $\chi$: the case $\alpha = 0$ of the exact family of the Revision theory
    record. The next cell checks exactly that it solves the full field equation of
    Section 4 (with $\partial_8\Psi = 0$).

    Then it follows, for $m = H = 1$ ($k = 2\sqrt2$) and a column $\chi$ with
    $B\chi = \chi$, the ordinary length $\Psi^\dagger\Psi$ and the Krein charge
    $Q(x_4) = \int\cos z\,\Psi^\dagger B\Psi\,dx_8 = \Psi^\dagger B\Psi/(6H)$. By
    Section 6 (with $u = v = \Psi$ and $\partial_8\Psi = 0$) the charge changes at the
    rate of the flux through the patch end:
    $dQ/dx_4 = -i\,[\sin z\,\Psi^\dagger BM_8\Psi]_{z = \pi/2} =
    \Psi^\dagger B\gamma^{(x_4)}\gamma^{(x_8)}\Psi$. The cell checks that $Q(x_4) - Q(0)$
    equals the flux added up over time (trapezoidal sums on a fine grid).
    """),
    code(r'''
    x4, k = sp.symbols("x4 k", positive=True)
    M_exact = -m * g[4] + 3 * H * g[4] * g[8]
    chi = sp.Matrix(sp.symbols("q1:17"))  # any constant column
    Psi = (sp.cosh(k * x4) * sp.eye(16) + sp.sinh(k * x4) / k * M_exact) * chi
    field_equation = g[4] * Psi.diff(x4) + 3 * H * g[8] * Psi - m * Psi  # d8 Psi = 0
    # multiply by k, then replace k^2 by 9 H^2 - m^2 (the definition of k)
    residual = field_equation.applyfunc(
        lambda e: sp.expand(sp.expand(k * e).subs(k ** 2, 9 * H ** 2 - m ** 2)))
    square_ok = (M_exact * M_exact - (9 * H ** 2 - m ** 2) * sp.eye(16)).applyfunc(
        sp.expand) == zero
    check_record(square_ok and residual == sp.zeros(16, 1),
                 "exact: Psi = (cosh kx4 + sinh(kx4)/k M) chi solves the field equation",
                 record="Revision/theory/reports/python-field-theory.json, check "
                        "exact_solution_family_x4_x8")

    M_numbers = -1.0 * gamma[4] + 3.0 * G48  # m = H = 1
    k_number = np.sqrt(8.0)  # k = sqrt(9 - 1) = 2 sqrt(2)
    plus_columns = (np.eye(16) + B) / 2  # columns with B chi = chi (after scaling)
    chi_number = plus_columns[:, 0] / np.linalg.norm(plus_columns[:, 0])
    x4_values = np.linspace(0.0, 1.5, 3001)
    lengths, charges, fluxes = [], [], []
    for t in x4_values:
        Psi_t = (np.cosh(k_number * t) * np.eye(16)
                 + np.sinh(k_number * t) / k_number * M_numbers) @ chi_number
        lengths.append((Psi_t.conj() @ Psi_t).real)
        charges.append((Psi_t.conj() @ B @ Psi_t).real / 6.0)  # 6 H = 6
        fluxes.append((Psi_t.conj() @ B @ G48 @ Psi_t).real)
    lengths, charges, fluxes = map(np.array, (lengths, charges, fluxes))
    step = x4_values[1] - x4_values[0]
    added_flux = np.concatenate([[0.0], np.cumsum((fluxes[1:] + fluxes[:-1]) / 2) * step])
    relative = np.max(np.abs(charges - charges[0] - added_flux)) / np.max(np.abs(charges))
    report("Krein charge Q at x4 = 0 and at x4 = 1.5", f"{charges[0]:.6f} and "
           f"{charges[-1]:.3f}")
    report("largest relative mismatch of Q(x4) - Q(0) and the added flux",
           f"{relative:.1e}")
    check(relative < 1e-5, "the Krein charge changes by the flux through z = pi/2")
    growth = np.polyfit(x4_values[1500:], np.log(lengths[1500:]), 1)[0]
    report("late slope of ln(Psi^dagger Psi)", f"{growth:.4f} (2 k = {2 * k_number:.4f})")
    check(abs(growth - 2 * k_number) < 0.05, "the ordinary length grows like exp(2 k x4)")
    '''),
    md(r"""
    The next cell draws the result: the logarithm of the ordinary length (left) and the
    Krein charge together with the flux added up over time (right).
    """),
    code(r'''
    fig, axes = plt.subplots(1, 2, figsize=(11.0, 4.2))
    axes[0].plot(x4_values, np.log(lengths), color=BLUE, linewidth=2,
                 label="$\\ln(\\Psi^\\dagger\\Psi)$")
    axes[0].plot(x4_values, 2 * k_number * x4_values + np.log(lengths[-1])
                 - 2 * k_number * x4_values[-1], "--", color=GREY, linewidth=1,
                 label="slope $2k = 4\\sqrt{2}$")
    axes[0].set_xlabel("time $x_4$ (units of $1/H$)")
    axes[0].set_ylabel("$\\ln$ of the ordinary length")
    axes[0].set_title("the wave grows")
    axes[0].legend()
    axes[1].plot(x4_values, charges, color=ORANGE, linewidth=3,
                 label="Krein charge $Q(x_4)$")
    axes[1].plot(x4_values, charges[0] + added_flux, "--", color=GREEN, linewidth=2,
                 label="$Q(0)$ + flux through $z = \\pi/2$")
    axes[1].set_xlabel("time $x_4$ (units of $1/H$)")
    axes[1].set_ylabel("Krein charge (units of $1/H$)")
    axes[1].set_title("not conserved: it changes by the flux")
    axes[1].legend()
    save_figure(fig, "krein_leak",
                "The exact good-sector solution $\\Psi(x_4) = (\\cosh kx_4 + \\sinh(kx_4)"
                "/k\\,M)\\chi$, independent of $x_8$, for $m = H = 1$ ($k = 2\\sqrt{2}$) "
                "and a column $\\chi$ with $B\\chi = \\chi$; horizontal axes: the time "
                "$x_4$ in units of $1/H$. Left: the logarithm of its ordinary length "
                "grows with the slope $2k$ (grey dashed line). Right: its Krein charge "
                "$Q = \\int\\cos z\\,\\Psi^\\dagger B\\Psi\\,dx_8$ (orange) is not "
                "constant; it equals its starting value plus the flux through the "
                "patch end $z = \\pi/2$ added up over time (green dashed). Without a "
                "boundary condition at $z = \\pi/2$ the Krein charge is not conserved: "
                "it changes by exactly what passes through the patch end.")
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

    - PROVED (exactly): in the author's metric the good-sector mode operator along the
      hidden direction, $h = -im\gamma^{(x_4)} + 3iH\gamma^{(x_4)}\gamma^{(x_8)} +
      i\tan z\,\gamma^{(x_4)}\gamma^{(x_8)}\partial_8$, satisfies $\cos z\,[u^\dagger(hv)
      - (hu)^\dagger v] = \partial_8(\sin z\,u^\dagger M_8v)$: it is symmetric for the
      volume $\cos z\,dx_8$ only up to a boundary term, which vanishes at the tip but
      not at the patch end $z = \pi/2$ (flux $2i$ for the recorded column). The Krein
      form is conserved up to the analogous term.
    - PROVED: the spin-connection term $3H\gamma^{(x_8)}$ is what makes the defect a pure
      boundary term in these variables and this volume; without it the remainder
      $-6H\cos z\,u^\dagger M_8v$ survives. (In other variables, $\Psi = \sin^{-1/2}z\,
      \chi$ with the volume $dy$, no such term is needed: this role of $3H$ depends on
      the variables, as the Revision record states.)
    - PROVED: the good-sector waves that do not depend on $x_8$ have a finite norm and
      the frequencies $\pm\sqrt{m^2 - 9H^2}$; for $m < 3H$ they grow (at $m = H = 1$ the
      eigenvalues are $\pm 2\sqrt2\,i$). The exact solution of the record with
      $\alpha = 0$ is such a wave.
    - COMPUTED: for that solution the Krein charge is not conserved; it changes by
      exactly the flux through $z = \pi/2$.
    - CONSEQUENCE (the scope of the quantisation in the Revision record): Hermiticity of
      the curved good-sector evolution and conservation of the Krein charge need a
      boundary condition at $z = \pi/2$ (for example the ASSUMED brane condition of the
      Kohn-Sham record); the Revision quantisation imposes none. The positive Fock space
      of the previous notebook is built for single good-sector momenta with frozen
      coefficients; a positive Hilbert space for the whole field is not constructed.
    """),
]

if __name__ == "__main__":
    raise SystemExit(run_builder(__file__))
