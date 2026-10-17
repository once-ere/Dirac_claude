#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
"""Builder of Notebook 03b, "The curvature of the corrected metric" (textbook
"Universes in Pairs").

The notebook Revision/textbook/notebooks/03b_curvature.ipynb is BUILT from this file by
Revision/textbook/tools/nbkit.py (never edit the .ipynb by hand):

    python Revision/textbook/tools/nbkit.py build \
        Revision/textbook/notebooks/src/03b_curvature.py --date YYYY-MM-DD
    python Revision/textbook/tools/nbkit.py check \
        Revision/textbook/notebooks/src/03b_curvature.py

Physics source: Revision/SPEC.md section 1 (the corrected metric, version 2 of
2026-10-16, with the functions a4 and b4, in the author's coordinates x0..x7, every real
z = 6 H x0) and the curvature record of the Rust program lovelock_gkd
(Revision/gkd_lovelock/results/curvature.json), its independent sympy verification
(python-lovelock-report.json), its own checks (lovelock-report.json), the lead's
independent checks of the Einstein tensor
(Revision/lead_checks/reports/einstein-gauss-bonnet-a4.json), the record of the field
equations of a4 and b4 (Revision/field_equations_a4/a4-equations.json,
exponentialHistory.requiredSource, and its sympy verification
reports/python-a4-report.json) and the record of the corrected metric
(Revision/metric_warped/results/warped-metric.json and its sympy report).  The notebook
computes everything again with sympy and asserts agreement with every record component.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools"))
from nbkit import code, md, run_builder  # noqa: E402

FIG = "Revision/textbook/figures/03b"
CURV = "Revision/gkd_lovelock/results/curvature.json"
PYREP = "Revision/gkd_lovelock/results/python-lovelock-report.json"
RUSTREP = "Revision/gkd_lovelock/results/lovelock-report.json"
LEAD = "Revision/lead_checks/reports/einstein-gauss-bonnet-a4.json"
A4EQ = "Revision/field_equations_a4/a4-equations.json"
A4REP = "Revision/field_equations_a4/reports/python-a4-report.json"
WARP = "Revision/metric_warped/results/warped-metric.json"
WARPREP = "Revision/metric_warped/reports/python-warped-metric-report.json"

FACTS = {
    "id": "03b",
    "name": "03b_curvature",
    "title": "The curvature of the corrected metric: Christoffel, Riemann, Ricci, "
             "Einstein, Kretschmann",
    "purpose": (
        "It computes with sympy, from the corrected metric exactly as the Revision "
        "record stores it and with general functions a4(x4) and b4(x4), for every real "
        "z = 6 H x0, all 512 Christoffel symbols, the Riemann tensor, the Ricci tensor, "
        "the Ricci scalar, the Einstein tensor and the Kretschmann scalar; it compares "
        "every component with the Revision record of the Rust program lovelock_gkd "
        "(exactly, and numerically at the five test points of the independent Revision "
        "verification, one in each quarter of the period), checks the symmetries of the "
        "Riemann tensor, the first and the contracted Bianchi identities, the "
        "Christoffel symbols by finite differences, the flat member of the family, and "
        "a negative control with the withdrawn metric of 2026-10-14; and it draws the "
        "Christoffel symbols, the curvature of every coordinate plane, the components and "
        "the curvature scalars versus z and versus the slope of the history, and the "
        "Einstein tensor; along the deflating history a4 = A H x4, b4 = b4(0) "
        "e^(beta A H x4) (beta = 4/3, b4(0) = 1) it reproduces the source that the "
        "Einstein equations require in the Revision record of the field equations of a4 "
        "and b4. It shows that every Riemann component is the curvature of a coordinate "
        "plane and does not depend on z, that the Einstein tensor is diagonal with equal "
        "hidden and extra-time components, and that for the planes that contain the time "
        "x4 the plane curvature is the relative acceleration of neighbouring observers at "
        "rest. Every check of a Revision report that a PASS line names is opened and "
        "asserted to exist and to have passed."
    ),
    "records": [
        [CURV, "every non-zero Christoffel symbol, Riemann component, Ricci and Einstein "
               "component and the Ricci scalar of the corrected metric, written by the "
               "Rust program lovelock_gkd"],
        [PYREP, "the independent sympy verification of those components (checks "
                "rust_christoffels_agree, rust_riemann_agrees, "
                "rust_ricci_einstein_scalar_agree, riemann_antisymmetry_and_pair_"
                "symmetry, mixed_riemann_free_of_x0, mixed_riemann_only_sectional, "
                "L1_equals_2R, k1_offdiagonal_vanishes, k1_hidden_equals_extra_times) and "
                "its five random test points"],
        [RUSTREP, "the checks riemann_antisymmetry (with its count of 112 nonzero "
                  "entries), riemann_first_bianchi, mixed_riemann_free_of_x0, "
                  "mixed_riemann_only_sectional, k1_equals_minus_4_einstein, "
                  "k1_divergence_free and the numerical test point of "
                  "k1_brute_force_numeric"],
        [LEAD, "the lead checks einstein_off_diagonal_vanish, "
               "einstein_diagonal_x0_independent, einstein_isotropy, "
               "einstein_null_energy, einstein_flat_vacuum and "
               "einstein_exponential_source_alpha1 (for general b4)"],
        [WARP, "the record of the corrected metric: the source of the canonical history "
               "with the Einstein couplings (history_source.einstein_A1_beta43) and, as "
               "dated history, the off-diagonal Einstein component of the withdrawn "
               "metric of 2026-10-14 (metric_of_2026_10_14_offdiagonal)"],
        [WARPREP, "its checks corrected_offdiagonal_all_orders, milne_flat_check and "
                  "record_metric_offdiagonal_reproduced"],
        [A4EQ, "the record of the field equations of a4 and b4: for the exponential "
               "history a4 = A H x4, b4 = b4(0) e^(beta A H x4) the energy density and the "
               "three pressures that the field equations require "
               "(exponentialHistory.requiredSource: rho, p3, p0, pt), here with the "
               "Einstein couplings"],
        [A4REP, "its sympy verification: the checks L1_equals_gkd_branch (the first "
                "Lovelock scalar, twice the Ricci scalar, in u = b4'/b4, v = u' and "
                "k = e^(2 a4)/b4), flat_member and json_exponential_history"],
    ],
    "packages": ["numpy", "sympy", "mpmath", "matplotlib"],
    "needs_rust": [],
    "expected_seconds": 60,
    "timeout_seconds": 600,
    "files_written": [
        "Revision/textbook/figures/03b.captions.json",
        f"{FIG}_1_christoffel_heat_maps.png",
        f"{FIG}_2_christoffel_versus_z.png",
        f"{FIG}_3_finite_differences.png",
        f"{FIG}_4_plane_curvatures.png",
        f"{FIG}_5_riemann_and_kretschmann_z.png",
        f"{FIG}_6_scalars_versus_a.png",
        f"{FIG}_7_einstein_tensor.png",
    ],
    "final_lines": [
        "PASS all seven figure files exist",
        "ALL 43 CHECKS PASSED (notebook 03b)",
    ],
    "troubleshooting": [
        ["The cells with the Riemann tensor and the negative control run for up to half a "
         "minute each, and their label shows a star meanwhile",
         "this is normal: sympy simplifies several thousand expressions exactly; wait "
         "until the label shows a number."],
    ],
}

CELLS = [
    md(r"""
    ## 1. What this notebook computes

    This notebook computes the **curvature** of the corrected metric of the primordial
    gravitational field (version 2 of 2026-10-16), exactly, with sympy, for general
    metric functions $a_4(x_4)$ and $b_4(x_4)$ and for every real $z = 6Hx_0$ away from
    the degenerate points $\sin z \cos z = 0$. It

    - reads the metric exactly as the Revision record stores it (from the record
      `Revision/gkd_lovelock/results/curvature.json`);
    - computes all $8^3 = 512$ **Christoffel symbols** $\Gamma^a{}_{bc}$, finds the 31
      that are not zero, checks them against the record of the Rust program
      `lovelock_gkd`, draws them as heat maps and as functions of $z$, and checks them a
      second, independent way by **finite differences** (a numerical derivative);
    - shows that the lines along the time $x_4$ are **geodesics** (free fall) with
      proper time $x_4$;
    - computes the **Riemann tensor** $R^a{}_{bcd}$ and its form $R^{ab}{}_{cd}$ with two
      upper indices, finds its 112 non-zero components, checks its symmetries and the
      first Bianchi identity, shows that every component is the curvature of a
      coordinate plane and does not depend on $z$, and compares all 112 with the record;
    - computes the curvature $\sigma(a, b)$ of each of the 28 coordinate planes and
      shows that for the planes with the time $x_4$ it is the relative acceleration of
      two neighbouring observers at rest;
    - computes the **Ricci tensor**, the **Ricci scalar** and the **Einstein tensor**,
      compares them with the record and the lead checks, shows that the Einstein tensor
      is **diagonal** (all 56 off-diagonal components vanish) with equal hidden and
      extra-time components, checks the contracted Bianchi identity
      $\sum_\mu \nabla_\mu G^\mu{}_\nu = 0$, and finds the flat member of the family;
    - computes the **Kretschmann scalar** $K = R^{ab}{}_{cd} R^{cd}{}_{ab}$ and shows
      that it does not depend on $z$, although the Christoffel symbols do;
    - evaluates everything along the **deflating history** $a_4 = A H x_4$ ($A > 0$),
      $b_4 = b_4(0)\,e^{\beta A H x_4}$ with $\beta = 4/3$ and $b_4(0) = 1$, and checks
      that the components of the Einstein tensor are exactly the energy density and the
      pressures that the Revision record of the field equations of $a_4$ and $b_4$ lists
      for this history (with the Einstein couplings);
    - repeats the curvature for a **negative control**, the withdrawn metric of
      2026-10-14, and finds the off-diagonal Einstein component that the corrected
      metric removes;
    - opens every Revision report whose check a PASS line names, and stops unless that
      check is listed there as passed;
    - draws 7 figures and prints a PASS line for every check.
    """),
    md(r"""
    ## 3. The words used in this notebook

    - **Metric** $g_{\mu\nu}$, **inverse metric** $g^{\mu\nu}$ (the inverse matrix:
      $\sum_\lambda g^{\mu\lambda} g_{\lambda\nu} = \delta^\mu{}_\nu$, which is $1$ when
      $\mu = \nu$ and $0$ otherwise). For a diagonal metric $g^{\mu\mu} = 1/g_{\mu\mu}$.
    - **Index notation**: $a, b, c, \dots$ each run over the eight coordinates
      $x_0, \dots, x_7$; an upper and a lower index are positions in a table of numbers;
      $\partial_c$ means the partial derivative $\partial/\partial x_c$.
    - **Christoffel symbols** $\Gamma^a{}_{bc} = \tfrac12 \sum_d g^{ad}(\partial_b g_{dc}
      + \partial_c g_{db} - \partial_d g_{bc})$: the correction terms that make
      derivatives of vectors independent of the coordinates. They are symmetric in $b$
      and $c$.
    - **Geodesic**: a curve $x^a(\tau)$ with $d^2x^a/d\tau^2 + \sum_{b,c}
      \Gamma^a{}_{bc}\,(dx^b/d\tau)(dx^c/d\tau) = 0$, the path of free fall, the
      straightest possible curve.
    - **Riemann tensor** $R^a{}_{bcd} = \partial_c \Gamma^a{}_{bd} - \partial_d
      \Gamma^a{}_{bc} + \sum_e (\Gamma^a{}_{ce}\Gamma^e{}_{bd} - \Gamma^a{}_{de}
      \Gamma^e{}_{bc})$ (the convention of the textbook of Misner, Thorne and Wheeler,
      MTW, used by every Revision record): it measures how much a vector turns when it
      is carried around a small closed loop. It is zero everywhere exactly when the space
      is flat.
    - $R^{ab}{}_{cd} = \sum_e g^{be} R^a{}_{ecd}$: the same tensor with the second index
      raised. For the coordinate plane of $x_a$ and $x_b$, $\sigma(a, b) =
      R^{ab}{}_{ab}$ (no sum) is the **curvature of that plane** (the sectional
      curvature). Only for a plane of two space-like directions does its sign describe
      a shape: positive curved like a sphere, negative like a saddle. For a plane with
      a time-like direction the sign is read from free fall: two neighbouring
      free-fall paths that move along the time-like direction $x_b$, a small proper
      distance $\xi$ apart along $x_a$, accelerate apart as $d^2\xi/d\tau^2 =
      +\sigma(a, b)\,\xi$, while on a sphere $d^2\xi/ds^2 = -\sigma\,\xi$: the same sign
      of $\sigma$ has the opposite effect.
    - **Warp factor** $W = (\sin^2 z)^{1/12} = |\sin z|^{1/6}$ of the extra times, with
      $dW/dx_0 = H\cot z\, W$; **hidden scale** $f = e^{-a_4}b_4^{1/2}$, shared by the
      hidden direction and the extra times; $k = e^{2a_4}/b_4 = 1/f^2$.
    - **Lead checks**: short independent Python programs of the Revision record (folder
      `Revision/lead_checks`), written from scratch by the coordinator of the Revision
      work (the "lead") without importing any other Revision code.
    - **Ricci tensor** $R^a{}_b = \sum_c R^{ac}{}_{bc}$, **Ricci scalar**
      $R = \sum_a R^a{}_a$, **Einstein tensor** $G^a{}_b = R^a{}_b - \tfrac12
      \delta^a{}_b R$: the averages of the curvature that enter Einstein's field
      equations.
    - **Kretschmann scalar** $K = \sum_{a,b,c,d} R^{ab}{}_{cd} R^{cd}{}_{ab}$: one number
      per point, the same in every coordinate system (an **invariant**).
    - **Einstein's field equations** $G^\mu{}_\nu + \Lambda\,\delta^\mu{}_\nu =
      \kappa\, T^\mu{}_\nu$: the Einstein tensor plus a constant $\Lambda$ (the
      **cosmological constant**) times $\delta^\mu{}_\nu$ equals a positive constant
      $\kappa$ times the **energy-momentum tensor** $T^\mu{}_\nu$ of the matter. For the
      sources of this book its diagonal is $T = \mathrm{diag}(p_0, p_3, p_3, p_3, -\rho,
      p_t, p_t, p_t)$ in the order $x_0, \dots, x_7$: the **energy density** $\rho$
      (energy per unit volume) and the
      **pressures** $p_3$ of 3-space, $p_t$ of the extra times and $p_0$ of the hidden
      direction. A later chapter derives these equations; this notebook only reads
      them in a Revision record.
    - **Bianchi identities**: $R^a{}_{bcd} + R^a{}_{cdb} + R^a{}_{dbc} = 0$ (first) and
      $\sum_\mu \nabla_\mu G^\mu{}_\nu = 0$ (contracted): identities that every metric
      satisfies; checking them checks the computation.
    - **Lovelock scalars and tensors**: curvature quantities built from products of one,
      two or three Riemann tensors with the generalized Kronecker delta; the first
      Lovelock scalar is $L_{(1)} = 2R$ and the first Lovelock tensor is
      $P_{(1)} = -4G$. A later chapter treats them in full.
    - **Finite difference**: the numerical derivative $f'(x) \approx (f(x+h) -
      f(x-h))/(2h)$; its error shrinks like $h^2$.
    - `a4p`, `a4pp`, `a4v`: the names the notebook prints for $a_4'$, $a_4''$ and the
      value of $a_4$; `b4p`, `b4pp`, `b4v` the same for $b_4$; `z` stands for $6 H x_0$
      and `w` for the warp factor $W$.
    """),
    md(r"""
    ## 4. The physical and mathematical situation

    The corrected metric is diagonal,

    $$g = \mathrm{diag}\bigl(f^2 \cot^2 z,\ e^{2a_4}\ (\times 3),\ -1,\
    -f^2 W^2\ (\times 3)\bigr), \qquad f = e^{-a_4} b_4^{1/2},\quad
    W = (\sin^2 z)^{1/12},\quad z = 6 H x_0,$$

    in the order $x_0, \dots, x_7$, with the constant $H > 0$ and the metric functions
    $a_4(x_4)$ and $b_4(x_4) > 0$ ($b_4$ is never 1). It depends on two coordinates
    only, $x_4$ (through $a_4$ and $b_4$) and $x_0$ (through $z$). Every derivative along
    $x_1, x_2, x_3, x_5, x_6, x_7$ is therefore zero, which is why most of the $512$
    Christoffel symbols and most of the $4096$ Riemann components vanish.

    The warp factor $W$ is the positive twelfth root of $\sin^2 z$; it is defined for
    every real $z$, and its derivative is $dW/dx_0 = H \cot z\, W$ wherever
    $\sin z \neq 0$ (the logarithm $\ln W = \tfrac1{12}\ln \sin^2 z$ has the derivative
    $\tfrac1{12} \cdot \tfrac{2\sin z \cos z}{\sin^2 z} \cdot 6H = H\cot z$). The
    notebook teaches sympy this one rule, so that every computation holds for every
    real $z$ at once, with no case for the sign of $\sin z$.

    Curvature is computed in three steps, each from the previous one: the Christoffel
    symbols need the first derivatives of the metric; the Riemann tensor needs the
    first derivatives of the Christoffel symbols and their products (so the second
    derivatives of the metric, and $a_4''$ and $b_4''$ appear); the Ricci tensor, the
    Ricci scalar and the Einstein tensor are sums of Riemann components. The Revision
    record computed all of this with an exact Rust program (`lovelock_gkd`); an
    independent sympy program checked every component, and the lead checks recomputed
    the Einstein tensor with their own sympy code. This notebook does it once more, in
    small steps, and compares every single component.

    Nothing here involves the matter fields yet: these are exact properties of the given
    metric. The field equations, which connect the Einstein tensor to the energy and the
    pressures of the fields, are the subject of a later chapter. For the plots the
    notebook uses $H = 1$ and the deflating history $a_4 = A H x_4$,
    $b_4 = b_4(0)\,e^{\beta A H x_4}$ of the Revision Kohn-Sham work, with
    $\beta = 4/3$ and $b_4(0) = 1$ (so $a_4' = A H$, $a_4'' = 0$, $b_4'/b_4 = \beta A H$,
    $b_4''/b_4 = (\beta A H)^2$ and $k = e^{2a_4}/b_4 = e^{(2 - \beta)a_4}
    = e^{2a_4/3}$; $A = 1$ is the canonical value): a PRESCRIBED BACKGROUND, assumed
    here and not obtained by solving the field equations. Every formula with general
    $a_4(x_4)$ and $b_4(x_4)$ is exact; on the history the curvature depends on the
    slope $A$ and, through $k$, on the slice $a_4$.
    """),
    md(r"""
    ## 5. The metric, read from the record

    First a technical step. While a cell runs, Jupyter sends what the cell prints to the
    notebook in pieces, about one piece every 0.2 seconds, so where one piece ends and
    the next begins depends on the speed of the computer. The tools that build this
    book read the PASS line of a check together with the line under it that names the
    Revision record, and they read the two correctly only when both arrive in the same
    piece. The next cell therefore defines the function `in_one_piece(helper)`: it
    returns a new function that does exactly what `helper` does, but lets `helper`
    print into a text buffer in memory (an `io.StringIO`, with
    `contextlib.redirect_stdout`) and then writes the whole buffer with one call of
    `sys.stdout.write`, which arrives as one piece. (The stars in `*arguments` and
    `**options` pass on all the values the new function is given, whatever they are.)
    The cell then replaces the helpers `check` and `report` of the set-up cell by such
    functions. Nothing else changes: the same checks, the same PASS lines, the same
    numbers.
    """),
    code(r'''
    import contextlib  # redirect_stdout: send printed text into a buffer
    import io  # StringIO: a text buffer in memory
    import sys  # sys.stdout: the place where printed text goes


    def in_one_piece(helper):
        """A function that does what helper does, with all the lines that helper prints
        written in one piece."""
        def helper_in_one_piece(*arguments, **options):
            collected = io.StringIO()  # an empty text buffer
            with contextlib.redirect_stdout(collected):  # print() writes into it
                helper(*arguments, **options)  # a failing check stops here, as before
            sys.stdout.write(collected.getvalue())  # all the lines with one write
        return helper_in_one_piece


    check = in_one_piece(check)  # a PASS line and its record line stay together
    report = in_one_piece(report)  # a long RESULT line and its second line, too
    say("From now on check and report print each of their results in one piece.")
    '''),
    md(r"""
    The next cell imports the packages, reads the record, and makes the symbols: the
    eight coordinates, $H > 0$, the unknown functions $a_4(x_4)$ and $b_4(x_4)$ ($b_4$
    positive), the warp factor `W`, the sign `G` of $\cot z$, and the printing names
    `a4p`, `a4pp`, `a4v`, `b4p`, `b4pp`, `b4v`, `w` and `z`. The warp factor is a sympy
    **function class** `W` with one rule of its own: the method `fdiff` tells sympy
    that the derivative of `W(x0)` is `H*cot(6*H*x0)*W(x0)` (section 4 of this
    notebook). The sign `G` of $\cot z$ is $+1$ or $-1$ and constant on each quarter of
    the period; it appears only in $|\cot z| = G \cot z$. The function `plain` rewrites
    an expression with the printing names; the function `symbolic` does the same but
    keeps $x_0$ and `W(x0)` (the record writes its components with $x_0$). It also
    names the two reports of the Revision curvature computation and defines the function
    `record_check(report_file, check_name, detail_part)`, the same as in Notebook 03a:
    it opens a Revision report, finds the check with that name, and stops the notebook
    with an error unless the check is there and passed (and, if `detail_part` is given,
    its detail contains that text). Every PASS line below that names a check of a
    Revision report calls it first, so that a renamed, missing or failing check in the
    record is caught.
    """),
    code(r'''
    import itertools  # loops over all index combinations

    import mpmath  # numbers with many digits
    import numpy as np  # arrays of numbers
    import sympy as sp  # exact algebra with symbols
    from sympy.parsing.sympy_parser import (implicit_multiplication, parse_expr,
                                            standard_transformations)

    CURVATURE_RECORD = "Revision/gkd_lovelock/results/curvature.json"
    record = json.loads(repository_file(CURVATURE_RECORD).read_text(encoding="utf-8"))
    PYTHON_REPORT = "Revision/gkd_lovelock/results/python-lovelock-report.json"  # sympy
    RUST_REPORT = "Revision/gkd_lovelock/results/lovelock-report.json"  # the Rust checks


    def record_check(report_file, check_name, detail_part=""):
        """Return True when the Revision report report_file lists the check check_name
        as passed (and its detail contains detail_part); otherwise stop the notebook."""
        checks = json.loads(repository_file(report_file).read_text(encoding="utf-8"))
        checks = checks["checks"]  # a dictionary or a list, depending on the report
        if isinstance(checks, dict):  # {name: {"passed": true, "detail": ...}}
            entry = checks.get(check_name, {})
            passed = entry.get("passed") is True
        else:  # [{"name": ..., "verdict": "PASS", "detail": ...}, ...]
            entry = next((e for e in checks if e.get("name") == check_name), {})
            passed = entry.get("verdict") == "PASS"
        if not passed or detail_part not in entry.get("detail", ""):
            raise AssertionError(f"record check failed: {report_file} does not list "
                                 f"{check_name} as passed")
        return True


    x0, x1, x2, x3, x4, x5, x6, x7 = sp.symbols("x0:8", real=True)
    X = [x0, x1, x2, x3, x4, x5, x6, x7]  # the coordinates, counted 0 to 7 in Python
    NAMES = ["x0", "x1", "x2", "x3", "x4", "x5", "x6", "x7"]
    H = sp.symbols("H", positive=True)  # the constant of the author
    a4 = sp.Function("a4")(x4)  # the metric function a4, unknown
    b4 = sp.Function("b4", positive=True)(x4)  # the metric function b4 > 0, unknown


    class W(sp.Function):
        """The warp factor W(x0) = (sin(6 H x0)^2)^(1/12) > 0 of the extra times."""

        def fdiff(self, argindex=1):
            """dW/dx0 = H cot(6 H x0) W, for every real z = 6 H x0 with sin z != 0."""
            return H * sp.cot(6 * H * self.args[0]) * self


    G = sp.symbols("G", real=True)  # the sign of cot z: +1 or -1, |cot z| = G cot z
    a4p, a4pp, a4v = sp.symbols("a4p a4pp a4v", real=True)  # a4 prime, a4 two primes, a4
    b4p, b4pp = sp.symbols("b4p b4pp", real=True)  # b4 prime, b4 two primes
    b4v, w = sp.symbols("b4v w", positive=True)  # the value of b4, the warp factor
    z = sp.symbols("z", real=True)  # z = 6 H x0, every real value, for printing


    def symbolic(expression):
        """Write the derivatives of a4 and b4 as a4p, a4pp, b4p, b4pp and the values
        a4(x4), b4(x4) as a4v, b4v."""
        expression = expression.subs(sp.Derivative(a4, (x4, 2)), a4pp)  # second first
        expression = expression.subs(sp.Derivative(b4, (x4, 2)), b4pp)
        expression = expression.subs(sp.Derivative(a4, x4), a4p).subs(a4, a4v)
        return expression.subs(sp.Derivative(b4, x4), b4p).subs(b4, b4v)


    def plain(expression):
        """As symbolic, with W(x0) written as w and 6 H x0 written as z."""
        return symbolic(expression).subs(W(x0), w).subs(x0, z / (6 * H))


    say("Record read; symbols x0 ... x7, H, a4(x4), b4(x4), W(x0), G, a4p, a4pp, a4v, "
        "b4p, b4pp, b4v, w and z defined.")
    '''),
    md(r"""
    The next cell turns the text of the metric into a sympy matrix, with the same
    translation rules as Notebook 03a (the note in brackets after the matrix is cut
    off; square brackets of functions become round brackets, `a4[x4]` and `b4[x4]`
    become `a4` and `b4`, curly brackets of lists become square brackets, `^` becomes
    `**`, and a blank between factors means times) and one more rule, applied first:
    the positive root `(Sin[6 H x0]^2)^(1/6)` becomes `W(x0)^2`, the square of the warp
    factor. It prints the diagonal.
    """),
    code(r'''
    # the metric exactly as the record stores it, without the note in brackets after it
    text = record["metricAsGiven"].split("}} ", 1)[0] + "}}"
    text = text.replace("(Sin[6 H x0]^2)^(1/6)", "W(x0)^2")  # the warp factor squared
    text = text.replace("exp^", "E^").replace("a4[x4]", "a4").replace("b4[x4]", "b4")
    text = text.replace("Sin[6 H x0]", "sin(6 H x0)").replace("Cot[6 H x0]", "cot(6 H x0)")
    text = text.replace("{", "[").replace("}", "]").replace("^", "**")
    metric_names = {"E": sp.E, "a4": a4, "b4": b4, "H": H, "x0": x0, "sin": sp.sin,
                    "cot": sp.cot, "W": W}
    g = sp.Matrix(parse_expr(text, local_dict=metric_names, transformations=(
        standard_transformations + (implicit_multiplication,))))
    for k in range(8):
        say(f"  g[{NAMES[k]}, {NAMES[k]}] = {plain(g[k, k])}")
    check(all(g[i, j] == 0 for i in range(8) for j in range(8) if i != j)
          and not any(g[k, k].has(sp.sin) for k in range(8)),
          "the metric read from the text of the record is diagonal, with the warp W")
    '''),
    md(r"""
    The record writes its components in Mathematica notation, for example
    `-(1/2)*E^(-2*a4[x4])*(Sin[6*H*x0]^2)^(1/6)*Derivative[1][b4][x4] + ...`. The next
    cell defines the function `from_mathematica` that translates such a text into
    sympy: the powers of `(Sin[6*H*x0]^2)` become powers of the warp factor
    (`^(1/12)` is `W(x0)`, `^(1/6)` is `W(x0)**2`, `^(1/4)` is `W(x0)**3`),
    `Sign[Cot[6*H*x0]]` becomes `G`, `Derivative[1][a4][x4]` ($a_4'$) becomes `a4p`,
    `Derivative[2][a4][x4]` becomes `a4pp`, `a4[x4]` becomes `a4v`, the same for $b_4$
    (`b4p`, `b4pp`, `b4v`), the sine and the cotangent get round brackets, and `^`
    becomes `**`. If any square bracket is left, the translation is incomplete and the
    function stops with an error, so a silent mistranslation is impossible.

    The cell also defines three helpers. `tidy(expression)` simplifies an expression:
    it writes $6Hx_0$ as $z$, simplifies it once as it is and once after writing
    $\sin 2z$ as $2\sin z\cos z$ (`expand_trig`), and keeps the shorter of the two
    results (sympy sometimes reaches the simplest form only one way: it writes, for
    example, $-6H/(\sin z\cos z)$ as $-12H/\sin(2z)$, the same number because
    $\sin 2z = 2\sin z\cos z$, and a sum such as $6H\cot z - 12H/\sin 2z + 6H\tan z$ is
    recognised as $0$ only after the rewriting). `vanishes(expression)` is true when
    `tidy` gives $0$, and `same(mine, theirs)` is true when the difference of our
    expression and the record's vanishes.
    """),
    code(r'''
    record_names = {"a4p": a4p, "a4pp": a4pp, "a4v": a4v, "b4p": b4p, "b4pp": b4pp,
                    "b4v": b4v, "H": H, "x0": x0, "E": sp.E, "sin": sp.sin, "cot": sp.cot,
                    "W": W, "G": G}
    ROOTS = {"(Sin[6*H*x0]^2)^(1/12)": "W(x0)", "(Sin[6*H*x0]^2)^(1/6)": "W(x0)^2",
             "(Sin[6*H*x0]^2)^(1/4)": "W(x0)^3", "Sign[Cot[6*H*x0]]": "G"}


    def from_mathematica(entry_text):
        """A component of the record (Mathematica notation) as a sympy expression."""
        t = entry_text
        for root, replacement in ROOTS.items():  # the roots of sin^2 and the sign first
            t = t.replace(root, replacement)
        t = t.replace("Derivative[1][a4][x4]", "a4p")
        t = t.replace("Derivative[2][a4][x4]", "a4pp").replace("a4[x4]", "a4v")
        t = t.replace("Derivative[1][b4][x4]", "b4p")
        t = t.replace("Derivative[2][b4][x4]", "b4pp").replace("b4[x4]", "b4v")
        t = t.replace("Sin[6*H*x0]", "sin(6*H*x0)").replace("Cot[6*H*x0]", "cot(6*H*x0)")
        t = t.replace("^", "**")
        if "[" in t or "]" in t:
            raise ValueError(f"cannot translate {entry_text}")
        return parse_expr(t, local_dict=record_names)


    def tidy(expression):
        """Simplify an expression.  It writes 6 H x0 as z (so that 12 H x0 becomes 2z),
        simplifies it twice, once as it is and once after writing sin(2z) as
        2 sin(z) cos(z) (expand_trig), keeps the shorter result (count_ops counts the
        operations), and writes z as 6 H x0 again."""
        expression = sp.sympify(expression).subs(x0, z / (6 * H))
        first = sp.simplify(expression)
        second = sp.simplify(sp.expand_trig(expression))
        best = second if sp.count_ops(second) < sp.count_ops(first) else first
        return best.subs(z, 6 * H * x0)


    def vanishes(expression):
        """True when the expression simplifies to zero."""
        return tidy(expression) == 0


    def same(mine, theirs):
        """True when mine (with the function a4) equals theirs (record symbols)."""
        return vanishes(symbolic(mine) - theirs)


    example = next(e["value"] for e in record["christoffelNonzero_b_le_c"]
                   if (e["a"], e["b"], e["c"]) == ("x4", "x5", "x5"))  # Gamma^x4_(x5 x5)
    say(f"example of a record entry: {example}")
    say(f"translated: {from_mathematica(example)}")
    '''),
    md(r"""
    ## 6. The Christoffel symbols

    The Christoffel symbols of the metric are

    $$\Gamma^a{}_{bc} = \tfrac12 \sum_{d} g^{ad}\bigl(\partial_b g_{dc} +
    \partial_c g_{db} - \partial_d g_{bc}\bigr).$$

    The next cell defines the function `christoffel(metric, coordinates)`, which applies
    this formula literally to every one of the $8 \times 8 \times 8 = 512$ index
    combinations (it does not use the symmetry in $b$ and $c$, so that the symmetry can
    be checked afterwards), simplifies each result, and returns the table
    `Gamma[a][b][c]`. Then it computes the symbols of the corrected metric and counts
    the non-zero ones.
    """),
    code(r'''
    def christoffel(metric, coordinates):
        """All Christoffel symbols Gamma[a][b][c] of a metric, by the formula above."""
        n = len(coordinates)
        inverse = metric.inv()  # the inverse metric g^(ad)
        d_metric = [metric.diff(c) for c in coordinates]  # d_metric[c][i, j] = d_c g_ij
        table = [[[0] * n for _ in range(n)] for _ in range(n)]
        for a, b, c in itertools.product(range(n), repeat=3):
            value = sum(inverse[a, d] * (d_metric[b][d, c] + d_metric[c][d, b]
                                         - d_metric[d][b, c]) for d in range(n)) / 2
            table[a][b][c] = tidy(value)
        return table


    Gamma = christoffel(g, X)
    nonzero = [(a, b, c) for a, b, c in itertools.product(range(8), repeat=3)
               if Gamma[a][b][c] != 0]
    upper_half = [(a, b, c) for a, b, c in nonzero if b <= c]
    report("non-zero Christoffel symbols (all orders of b, c)", len(nonzero))
    report("non-zero Christoffel symbols with b <= c", len(upper_half))
    check(all(Gamma[a][b][c] == Gamma[a][c][b]
              for a, b, c in itertools.product(range(8), repeat=3)),
          "the Christoffel symbols are symmetric in their two lower indices")
    '''),
    md(r"""
    The next cell prints the 21 non-zero symbols with $b \le c$ (the others follow by the
    symmetry) and compares them with the list `christoffelNonzero_b_le_c` of the record:
    first that the two lists name the same 21 index combinations, then that each value
    agrees exactly. In the record the keys `a`, `b`, `c` are the indices of
    $\Gamma^a{}_{bc}$, and the list runs in the author's order $x_0, \dots, x_7$.
    sympy chooses its own way of writing some symbols: $H\cot z$ appears as
    `H/tan(z)`, $H W^2 \tan z$ as `H*w**2*tan(z)`, and
    $\Gamma^{x_0}{}_{x_0x_0} = -6H/(\sin z\cos z)$ as `-12*H/sin(2*z)`. The symbols
    with the index $x_4$ contain the two rates: $\Gamma^{x_1}{}_{x_1x_4} = a_4'$ and
    $\Gamma^{x_5}{}_{x_4x_5} = \Gamma^{x_0}{}_{x_0x_4} = -a_4' + b_4'/(2b_4)$: the hidden
    direction changes at the rate of the extra times.
    """),
    code(r'''
    for a, b, c in upper_half:
        say(f"  Gamma^{NAMES[a]}_({NAMES[b]} {NAMES[c]}) = {plain(Gamma[a][b][c])}")
    record_gamma = {(NAMES.index(e["a"]), NAMES.index(e["b"]), NAMES.index(e["c"])):
                    from_mathematica(e["value"])
                    for e in record["christoffelNonzero_b_le_c"]}
    check(sorted(record_gamma) == upper_half and len(upper_half) == 21,
          "the same 21 non-zero Christoffel symbols as the record")
    record_check(PYTHON_REPORT, "rust_christoffels_agree")  # stops if not passed
    check(all(same(Gamma[a][b][c], value) for (a, b, c), value in record_gamma.items()),
          "every Christoffel symbol equals the record exactly",
          record=f"{CURVATURE_RECORD}, christoffelNonzero_b_le_c (and "
                 "python-lovelock-report.json, check rust_christoffels_agree)")
    '''),
    md(r"""
    The next cell sets the colours of the figures (a palette whose colours can also be
    told apart with a colour-vision deficiency; the figures also use line styles and
    labels) and turns every Christoffel symbol into a fast numerical function of $z$,
    $a_4$, $a_4'$, $H$, $b_4$ and $b_4'$ (`sp.lambdify`), with the warp factor written
    as $|\sin z|^{1/6}$. It then draws the eight $8 \times 8$ tables
    $\Gamma^{x_k}{}_{bc}$ at the point $z = \pi/4$ with $H = 1$ on the slice
    $a_4 = 0.5$ of the history ($a_4' = 1$, $b_4 = e^{2/3}$, $b_4' = \tfrac43 e^{2/3}$) as
    heat maps. The colour scale is **symmetric-logarithmic**: above $0.1$ in size, equal
    steps of colour stand for equal factors of size (below $0.1$ the scale is
    ordinary), so that small and large symbols are both visible; grey is zero, red
    positive, blue negative.
    """),
    code(r'''
    from matplotlib.colors import LinearSegmentedColormap, SymLogNorm

    BLUE, ORANGE, AQUA, YELLOW = "#2a78d6", "#eb6834", "#1baf7a", "#eda100"
    MAGENTA, GREEN, VIOLET, RED = "#e87ba4", "#008300", "#4a3aa7", "#e34948"
    DIVERGING = LinearSegmentedColormap.from_list("blue_grey_red", [BLUE, "#f0efec", RED])
    LABELS = [f"$x_{k}$" for k in range(8)]
    ARGS = (z, a4v, a4p, H, b4v, b4p)  # the arguments of the numerical functions


    def numeric(expression):
        """A numerical function f(z, a4v, a4p, H, b4v, b4p) of an expression, with the
        warp factor w = |sin z|^(1/6)."""
        value = plain(expression).subs(w, sp.Abs(sp.sin(z)) ** sp.Rational(1, 6))
        return sp.lambdify(ARGS, value, "numpy")


    gamma_functions = {(a, b, c): numeric(Gamma[a][b][c]) for a, b, c in nonzero}
    # z, a4, a4p, H, b4, b4p: the slice a4 = 0.5 of the history, b4 = e^(2/3),
    # b4' = (4/3) b4 (beta = 4/3, A = 1, H = 1, b4(0) = 1)
    B4_SLICE = float(np.exp(2.0 / 3.0))
    POINT = (np.pi / 4, 0.5, 1.0, 1.0, B4_SLICE, 4.0 / 3.0 * B4_SLICE)
    tables = np.zeros((8, 8, 8))
    for (a, b, c), f in gamma_functions.items():
        tables[a, b, c] = f(*POINT)
    fig, axes = plt.subplots(2, 4, figsize=(11.0, 5.4))
    norm = SymLogNorm(linthresh=0.1, vmin=-15.0, vmax=15.0, base=10)
    for a, ax in enumerate(axes.flat):
        image = ax.imshow(tables[a], cmap=DIVERGING, norm=norm)
        for b, c in itertools.product(range(8), repeat=2):
            if tables[a, b, c] != 0:
                ax.text(c, b, f"{tables[a, b, c]:.2f}", ha="center", va="center",
                        fontsize=6.0)
        ax.set_title(f"$\\Gamma^{{x_{a}}}{{}}_{{bc}}$", fontsize=10)
        ax.set_xticks(range(8), [str(k) for k in range(8)], fontsize=7)
        ax.set_yticks(range(8), [str(k) for k in range(8)], fontsize=7)
        ax.grid(False)
    fig.colorbar(image, ax=axes, shrink=0.8, label="value (unit $H$)")
    fig.suptitle("Christoffel symbols at $z = \\pi/4$, $a_4 = 0.5$, "
                 "$a_4^{\\prime} = 1$, $b_4 = e^{2/3}$, $b_4^{\\prime}/b_4 = 4/3$, "
                 "$H = 1$ (row $b$, column $c$)")
    save_figure(fig, "christoffel_heat_maps",
                "The 512 Christoffel symbols $\\Gamma^{a}{}_{bc}$ of the corrected metric "
                "at the point $z = \\pi/4$ on the slice $a_4 = 0.5$ of the history "
                "$a_4 = x_4$, $b_4 = e^{4x_4/3}$ ($a_4^{\\prime} = 1$, "
                "$b_4 = e^{2/3}$ and $b_4^{\\prime}/b_4 = 4/3$, $H = 1$), as eight heat "
                "maps, one "
                "for each upper index $a = x_0, \\dots, x_7$; in each map the row is $b$ "
                "and the column is $c$ (numbers $0$ to $7$ for $x_0$ to $x_7$), the "
                "colour is the value on a symmetric logarithmic scale (grey zero, red "
                "positive, blue negative) and every non-zero value is printed. Only 31 "
                "of the 512 squares are coloured, each map is symmetric about its "
                "diagonal, and every non-zero symbol has at least one index equal to "
                "$x_4$ or $x_0$, the two coordinates on which the metric depends; the "
                "3-space maps have no entry with $x_0$, because 3-space has no warp.")
    check(np.allclose(tables, tables.transpose(0, 2, 1))
          and all(4 in key or 0 in key for key in nonzero)
          and not any(Gamma[k][k][0] != 0 for k in (1, 2, 3)),
          "the tables are symmetric in b, c; every non-zero symbol has an index x4 or x0; "
          "Gamma^xi_(xi x0) = 0 for 3-space")
    '''),
    md(r"""
    The symbols with an index $x_0$ depend on $z$. The next cell draws the size of five
    typical symbols across one cell $0 < z < \pi$ on a logarithmic axis (at the same
    point of the history, $a_4 = 0.5$, $a_4' = 1$, $b_4 = e^{2/3}$, $b_4'/b_4 = 4/3$,
    $H = 1$): $\Gamma^{x_5}{}_{x_5 x_0} = H\cot z$ grows without bound at the tips
    $z \to 0$ and $z \to \pi$ and vanishes at the fold $z = \pi/2$;
    $\Gamma^{x_0}{}_{x_0 x_0}$ is large at the tips and at the fold;
    $\Gamma^{x_0}{}_{x_5 x_5} = HW^2\tan z$ grows without bound at the fold;
    $\Gamma^{x_4}{}_{x_0 x_0}$ grows at the tips and vanishes at the fold;
    $\Gamma^{x_1}{}_{x_1 x_4} = a_4'$ does not depend on $z$. Large Christoffel symbols
    are a property of the coordinates; whether the geometry itself is extreme is decided
    by the Riemann tensor and by invariants such as the Kretschmann scalar of section 12.
    """),
    code(r'''
    z_line = np.linspace(0.01, np.pi - 0.01, 600)
    z_line = z_line[np.abs(z_line - np.pi / 2) > 0.004]  # leave out the fold itself
    chosen = [((5, 5, 0), RED, "-", "$\\Gamma^{x_5}{}_{x_5 x_0}$"),
              ((0, 0, 0), VIOLET, "--", "$\\Gamma^{x_0}{}_{x_0 x_0}$"),
              ((0, 5, 5), ORANGE, "-.", "$\\Gamma^{x_0}{}_{x_5 x_5}$"),
              ((4, 0, 0), BLUE, ":", "$\\Gamma^{x_4}{}_{x_0 x_0}$"),
              ((1, 1, 4), AQUA, "-", "$\\Gamma^{x_1}{}_{x_1 x_4}$")]
    fig, ax = plt.subplots()
    for index, colour, style, label in chosen:
        values = np.broadcast_to(gamma_functions[index](z_line, *POINT[1:]),
                                 z_line.shape)
        ax.plot(z_line, np.abs(values), color=colour, ls=style, lw=1.8, label=label)
    ax.axvline(np.pi / 2, color="grey", lw=0.8, ls=":")
    ax.text(np.pi / 2 + 0.04, 1.5e-5, "fold", fontsize=9)
    ax.set_yscale("log")
    ax.set_xlabel("$z = 6 H x_0$ (radians)")
    ax.set_ylabel("absolute value of the symbol (unit $H$)")
    ax.set_title("Christoffel symbols across a cell "
                 "($a_4 = 0.5$, $a_4^{\\prime} = 1$, $b_4 = e^{2/3}$, $H = 1$)")
    ax.set_ylim(1e-5, 3e3)  # room below the curves for the legend
    ax.legend(fontsize=8, loc="lower center", ncol=3)
    save_figure(fig, "christoffel_versus_z",
                "The absolute values of five Christoffel symbols of the corrected metric "
                "across one cell $0 < z < \\pi$ (two halves joined at the fold "
                "$z = \\pi/2$, dotted), for $a_4 = 0.5$, $a_4^{\\prime} = 1$, "
                "$b_4 = e^{2/3}$, $b_4^{\\prime}/b_4 = 4/3$ (the history at $a_4 = 0.5$), "
                "$H = 1$, on a logarithmic vertical axis; horizontal axis "
                "$z = 6Hx_0$ in radians, vertical axis the absolute value in units of "
                "$H$. $\\Gamma^{x_5}{}_{x_5x_0} = H\\cot z$ is large at the tips and "
                "vanishes at the fold, $\\Gamma^{x_0}{}_{x_0x_0}$ is large at the tips "
                "and at the fold, $\\Gamma^{x_0}{}_{x_5x_5}$ grows towards the fold, "
                "$\\Gamma^{x_4}{}_{x_0x_0}$ grows towards the tips, and "
                "$\\Gamma^{x_1}{}_{x_1x_4} = a_4^{\\prime} = 1$ is the same everywhere; "
                "every curve is symmetric about the fold.")
    check(abs(gamma_functions[(5, 5, 0)](*POINT) - 1.0) < 1e-14
          and abs(gamma_functions[(5, 4, 5)](*POINT) - (-1.0 / 3.0)) < 1e-14
          and abs(gamma_functions[(0, 0, 4)](*POINT) - (-1.0 / 3.0)) < 1e-14,
          "at z = pi/4, H = 1: Gamma^x5_(x5 x0) = H cot z = 1, and on the history "
          "Gamma^x5_(x4 x5) = Gamma^x0_(x0 x4) = -a4' + b4'/(2 b4) = -1/3")
    '''),
    md(r"""
    ## 7. A second, independent check: finite differences

    The exact symbols can be checked without any algebra. Take concrete functions
    $a_4(x_4) = 0.17 + 0.61\,x_4 - 0.185\,x_4^2$ and
    $b_4(x_4) = 1.37 + 0.31\,x_4 - 0.115\,x_4^2$ (so that at $x_4 = 0$:
    $a_4 = 0.17$, $a_4' = 0.61$, $a_4'' = -0.37$, $b_4 = 1.37$, $b_4' = 0.31$,
    $b_4'' = -0.23$), $H = 0.23$ and the point $x_0 = 0.41$: the test point at which the
    Rust program checked its Lovelock tensors by brute force (record
    `lovelock-report.json`, check `k1_brute_force_numeric`).
    The next cell first confirms these numbers in the record. Then it computes the
    metric as a plain table of numbers at points $x \pm h\,e_c$ (one coordinate moved by
    $\pm h$), the derivative of the metric by the central difference
    $\partial_c g \approx (g(x + h e_c) - g(x - h e_c))/(2h)$, and from it all 512
    Christoffel symbols with the same formula; it compares them with the exact symbols
    for eight step sizes $h$ from $10^{-1}$ to $10^{-8}$.
    """),
    code(r'''
    prime = chr(39)  # the apostrophe (character number 39): the record writes a4 prime so
    point_text = (f"H = 0.23, a4 = 0.17, a4{prime} = 0.61, a4{prime}{prime} = -0.37, "
                  f"b4 = 1.37, b4{prime} = 0.31, b4{prime}{prime} = -0.23, "
                  "x0 = 0.41")  # the test point as the record writes it
    check(record_check(RUST_REPORT, "k1_brute_force_numeric", point_text),
          "the test point is the one of the brute-force check of the Rust program")
    H_n, a0, a1, a2, x0_n = 0.23, 0.17, 0.61, -0.37, 0.41  # the test point
    b0, b1, b2 = 1.37, 0.31, -0.23  # b4, b4' and b4'' at x4 = 0


    def metric_numbers(x):
        """The metric as an 8 x 8 numpy table at the point x (8 coordinates)."""
        a = a0 + a1 * x[4] + 0.5 * a2 * x[4] ** 2  # a4(x4) with a4(0) = 0.17, ...
        b = b0 + b1 * x[4] + 0.5 * b2 * x[4] ** 2  # b4(x4) with b4(0) = 1.37, ...
        f_squared = np.exp(-2 * a) * b  # f^2 = e^(-2 a4) b4
        warp_squared = np.abs(np.sin(6 * H_n * x[0])) ** (1 / 3)  # W^2 = |sin z|^(1/3)
        # the author's order x0, x1, ..., x7
        return np.diag([f_squared / np.tan(6 * H_n * x[0]) ** 2] + [np.exp(2 * a)] * 3
                       + [-1.0] + [-f_squared * warp_squared] * 3)


    def christoffel_numbers(x, h):
        """All 512 Christoffel symbols at x from central differences with step h."""
        d_metric = np.zeros((8, 8, 8))  # d_metric[c] = derivative of g along x_c
        for c in range(8):
            step = np.zeros(8)
            step[c] = h
            d_metric[c] = (metric_numbers(x + step) - metric_numbers(x - step)) / (2 * h)
        inverse = np.linalg.inv(metric_numbers(x))
        table = np.zeros((8, 8, 8))
        for a, b, c in itertools.product(range(8), repeat=3):
            table[a, b, c] = 0.5 * sum(inverse[a, d] * (d_metric[b][d, c]
                                       + d_metric[c][d, b] - d_metric[d][b, c])
                                       for d in range(8))
        return table


    x_point = np.array([x0_n, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])  # x0 = 0.41, x4 = 0
    exact = np.zeros((8, 8, 8))
    for (a, b, c), f in gamma_functions.items():
        exact[a, b, c] = f(6 * H_n * x0_n, a0, a1, H_n, b0, b1)
    steps = 10.0 ** -np.arange(1, 9)  # h = 0.1, 0.01, ..., 1e-8
    errors = np.array([np.max(np.abs(christoffel_numbers(x_point, h) - exact))
                       for h in steps])
    for h, e in zip(steps, errors):
        say(f"  h = {h:.0e}: largest error of the 512 symbols = {e:.2e}")
    order = np.log10(errors[0] / errors[1])  # the slope between h = 0.1 and h = 0.01
    report("measured order of the error between h = 0.1 and h = 0.01", f"{order:.3f}")
    check(1.9 < order < 2.1 and errors.min() < 1e-8,
          "finite differences reproduce all 512 symbols; the error falls like h^2")
    '''),
    md(r"""
    The next cell draws the largest error against the step $h$ on logarithmic axes.
    For large $h$ the error of the central difference is about $C h^2$, a straight line
    of slope 2 (the dashed reference line); for very small $h$ the rounding errors of
    the computer (about $10^{-16}$ relative) are divided by $h$ and the error grows
    again. The best step is where the two meet.
    """),
    code(r'''
    fig, ax = plt.subplots()
    ax.loglog(steps, errors, "o-", color=BLUE, lw=1.8, ms=7,
              label="largest error of the 512 symbols")
    ax.loglog(steps, errors[0] * (steps / steps[0]) ** 2, "--", color="black", lw=1.2,
              label="slope 2: error proportional to $h^2$")
    ax.set_xlabel("step $h$ of the central difference")
    ax.set_ylabel("largest absolute error (unit $H$)")
    ax.set_title("Christoffel symbols by finite differences")
    ax.legend(fontsize=8)
    best = int(np.argmin(errors))  # the position of the smallest error in the list
    report("best step and its error", f"h = {steps[best]:.0e}, error {errors[best]:.1e}")
    mantissa, exponent = f"{errors[best]:.1e}".split("e")  # e.g. "3.2" and "-10"
    best_error = f"{mantissa} \\times 10^{{{int(exponent)}}}"  # 3.2 x 10^-10 in LaTeX
    best_step = f"10^{{{round(np.log10(steps[best]))}}}"  # the step as a power of 10
    save_figure(fig, "finite_differences",
                "The largest difference between the 512 Christoffel symbols computed "
                "numerically by central differences of the metric and the exact "
                "symbols, at the test point $H = 0.23$, $a_4 = 0.17$, "
                "$a_4^{\\prime} = 0.61$, $a_4^{\\prime\\prime} = -0.37$, $b_4 = 1.37$, "
                "$b_4^{\\prime} = 0.31$, $b_4^{\\prime\\prime} = -0.23$, $x_0 = 0.41$ of "
                "the Revision record, against the step $h$, on logarithmic axes; "
                "horizontal axis $h$, vertical axis the error in units of $H$. For "
                "large steps the error follows the dashed line of slope 2 (error "
                "proportional to $h^2$); the smallest error, "
                f"${best_error}$, is reached at $h = {best_step}$; for "
                "smaller steps the rounding errors of the computer, which grow like "
                "$1/h$, take over.")
    check(errors[0] > errors[1] > errors[2] > errors[3],
          "the error shrinks as the step shrinks from 0.1 to 0.0001")
    '''),
    md(r"""
    ## 8. Free fall along the time $x_4$

    Consider an observer who stays at fixed $x_1, x_2, x_3, x_5, x_6, x_7, x_0$ while
    $x_4 = \tau$ runs. Then $dx^a/d\tau$ is $1$ for $a = x_4$ and $0$ otherwise, and
    $d^2x^a/d\tau^2 = 0$, so the geodesic equation reduces to
    $\Gamma^a{}_{x_4 x_4} = 0$ for every $a$. Since $g_{44} = -1$, the proper time of
    the observer is $\sqrt{-g_{44}}\, d\tau = d\tau$: $x_4$ is the time shown by the
    observer's clock. The next cell checks that the eight symbols $\Gamma^a{}_{x_4x_4}$
    are zero. It also checks the useful identity $\sum_a \Gamma^a{}_{ab} =
    \partial_b \ln\sqrt{|\det g|}$, with
    $\sqrt{|\det g|} = e^{-a_4} b_4^2 |\cot z| W^3 = e^{-a_4} b_4^2\, G \cot z\, W^3$ (the
    constant sign $G$ drops out of the logarithmic derivative).
    """),
    code(r'''
    check(all(Gamma[a][4][4] == 0 for a in range(8)),
          "Gamma^a_(x4 x4) = 0: observers at rest fall freely, x4 is their proper time")
    volume = sp.exp(-a4) * b4 ** 2 * G * sp.cot(6 * H * x0) * W(x0) ** 3  # sqrt|det g|
    contracted = [vanishes(sum(Gamma[a][a][b] for a in range(8))
                           - sp.diff(sp.log(volume), X[b]))
                  for b in range(8)]
    check(all(contracted),
          "sum over a of Gamma^a_(a b) equals the derivative of ln sqrt|det g|")
    '''),
    md(r"""
    ## 9. The Riemann tensor

    The Riemann tensor in the convention of all Revision records (MTW) is

    $$R^a{}_{bcd} = \partial_c \Gamma^a{}_{bd} - \partial_d \Gamma^a{}_{bc}
    + \sum_e \bigl(\Gamma^a{}_{ce}\Gamma^e{}_{bd} - \Gamma^a{}_{de}\Gamma^e{}_{bc}\bigr).$$

    It is antisymmetric in its last two indices $c, d$ (exchanging $c$ and $d$ turns the
    formula into its negative: the first two terms exchange places and signs, and so do
    the two products), so the next cell computes it for $c < d$ and fills $c > d$ with
    the opposite sign; the components with $c = d$ are zero. It keeps only the
    non-zero components in a dictionary. Then it raises the second index,
    $R^{ab}{}_{cd} = \sum_e g^{be} R^a{}_{ecd}$, the form in which the record stores
    the tensor. This cell takes a few seconds.
    """),
    code(r'''
    def riemann(table, coordinates):
        """The non-zero R^a_bcd (MTW) as a dictionary {(a, b, c, d): value}."""
        n = len(coordinates)
        result = {}
        for a, b in itertools.product(range(n), repeat=2):
            for c, d in itertools.combinations(range(n), 2):  # all pairs c < d
                value = (sp.diff(table[a][b][d], coordinates[c])
                         - sp.diff(table[a][b][c], coordinates[d])
                         + sum(table[a][c][e] * table[e][b][d]
                               - table[a][d][e] * table[e][b][c] for e in range(n)))
                value = tidy(value)
                if value != 0:
                    result[(a, b, c, d)] = value
                    result[(a, b, d, c)] = -value  # antisymmetric in c and d
        return result


    def raise_second(riemann_table, metric):
        """R^ab_cd = sum over e of g^(be) R^a_ecd, the non-zero ones."""
        inverse = metric.inv()
        result = {}
        for (a, e, c, d), value in riemann_table.items():
            for b in range(metric.rows):
                if inverse[b, e] != 0:
                    result[(a, b, c, d)] = result.get((a, b, c, d), 0) \
                        + inverse[b, e] * value
        result = {k: tidy(v) for k, v in result.items()}
        return {k: v for k, v in result.items() if v != 0}


    R_down = riemann(Gamma, X)  # R^a_bcd
    R_mixed = raise_second(R_down, g)  # R^ab_cd
    report("non-zero components R^a_bcd", len(R_down))
    report("non-zero components R^ab_cd", len(R_mixed))
    record_check(RUST_REPORT, "riemann_antisymmetry", "112 nonzero entries")
    check(len(R_mixed) == 112, "R^ab_cd has 112 non-zero components, as in the record",
          record="Revision/gkd_lovelock/results/lovelock-report.json, check "
                 "riemann_antisymmetry (112 nonzero entries)")
    '''),
    md(r"""
    The next cell checks the symmetries that every Riemann tensor has, as a test of the
    computation: (1) $R^{ab}{}_{cd} = -R^{ba}{}_{cd} = -R^{ab}{}_{dc}$; (2) with all
    indices lowered, $R_{abcd} = g_{aa} g_{bb} R^{ab}{}_{cd}$ (diagonal metric), the
    pair symmetry $R_{abcd} = R_{cdab}$; (3) the first Bianchi identity
    $R^a{}_{bcd} + R^a{}_{cdb} + R^a{}_{dbc} = 0$ for all $8^4 = 4096$ index lists.
    Then two properties that are special to the corrected metric: no component
    $R^{ab}{}_{cd}$ depends on $x_0$ (neither the warp factor $W$ nor any function of
    $z$ is left in it), and every non-zero component is the curvature of a coordinate
    plane: its two lower indices are its two upper indices, $\{c, d\} = \{a, b\}$.
    """),
    code(r'''
    def get(table, key):
        return table.get(key, 0)


    antisymmetric = all(vanishes(v + get(R_mixed, (b, a, c, d)))
                        and vanishes(v + get(R_mixed, (a, b, d, c)))
                        for (a, b, c, d), v in R_mixed.items())
    lowered = {(a, b, c, d): g[a, a] * g[b, b] * v
               for (a, b, c, d), v in R_mixed.items()}
    pair_symmetric = all(vanishes(v - get(lowered, (c, d, a, b)))
                         for (a, b, c, d), v in lowered.items())
    record_check(PYTHON_REPORT, "riemann_antisymmetry_and_pair_symmetry")
    check(antisymmetric and pair_symmetric,
          "R^ab_cd is antisymmetric in a, b and in c, d; R_abcd = R_cdab",
          record="Revision/gkd_lovelock/results/python-lovelock-report.json, check "
                 "riemann_antisymmetry_and_pair_symmetry")
    bianchi = [vanishes(get(R_down, (a, b, c, d)) + get(R_down, (a, c, d, b))
                        + get(R_down, (a, d, b, c)))
               for a, b, c, d in itertools.product(range(8), repeat=4)]
    record_check(RUST_REPORT, "riemann_first_bianchi")
    check(all(bianchi) and len(bianchi) == 4096,
          "the first Bianchi identity holds for all 4096 index lists",
          record="Revision/gkd_lovelock/results/lovelock-report.json, check "
                 "riemann_first_bianchi")
    x0_free = all(not symbolic(v).has(x0) for v in R_mixed.values())
    record_check(RUST_REPORT, "mixed_riemann_free_of_x0")
    record_check(PYTHON_REPORT, "mixed_riemann_free_of_x0")
    check(x0_free, "no R^ab_cd depends on x0: neither W nor any function of z is left",
          record="Revision/gkd_lovelock/results/lovelock-report.json and "
                 "python-lovelock-report.json, check mixed_riemann_free_of_x0")
    sectional = all({c, d} == {a, b} for a, b, c, d in R_mixed)
    record_check(RUST_REPORT, "mixed_riemann_only_sectional")
    record_check(PYTHON_REPORT, "mixed_riemann_only_sectional")
    check(sectional, "every non-zero R^ab_cd has {c, d} = {a, b}: only plane curvatures",
          record="Revision/gkd_lovelock/results/lovelock-report.json and "
                 "python-lovelock-report.json, check mixed_riemann_only_sectional")
    '''),
    md(r"""
    The next cell compares all 112 components with the list `riemannMixedNonzero` of the
    record, in which `up` holds $a, b$ and `down` holds $c, d$ of $R^{ab}{}_{cd}$: first
    that the same 112 index lists occur, then that each value agrees exactly. It then
    groups the 112 components by their value and prints the different values (10 for
    general $a_4$ and $b_4$), how often each occurs and one example of where. Each value
    is first multiplied out (`sp.expand`), so that one value that sympy happens to write
    in two ways is counted once.
    """),
    code(r'''
    record_riemann = {}
    for entry in record["riemannMixedNonzero"]:
        key = tuple(NAMES.index(n) for n in entry["up"] + entry["down"])
        record_riemann[key] = from_mathematica(entry["value"])
    check(sorted(record_riemann) == sorted(R_mixed),
          "the same 112 non-zero components R^ab_cd as the record")
    record_check(PYTHON_REPORT, "rust_riemann_agrees")
    check(all(same(R_mixed[k], v) for k, v in record_riemann.items()),
          "every component R^ab_cd equals the record exactly",
          record=f"{CURVATURE_RECORD}, riemannMixedNonzero (and "
                 "python-lovelock-report.json, check rust_riemann_agrees)")
    groups = {}
    for key in sorted(R_mixed):
        # the value multiplied out: one value written in two ways counts once
        groups.setdefault(sp.sstr(sp.expand(plain(R_mixed[key]))), []).append(key)
    for value_text in sorted(groups):
        a, b, c, d = groups[value_text][0]
        say(f"  {len(groups[value_text]):2d} x  {value_text}  e.g. "
            f"R^({NAMES[a]} {NAMES[b]})_({NAMES[c]} {NAMES[d]})")
    report("different values among the 112 components", len(groups))
    '''),
    md(r"""
    ## 10. The curvature of every coordinate plane

    For two different coordinates $x_a$ and $x_b$ the number $\sigma(a, b) =
    R^{ab}{}_{ab}$ (no sum) is the curvature of the coordinate plane spanned by them.
    The next cell computes all 28 of them as formulas, prints one plane of each kind,
    and checks eight formulas. Write $\alpha = a_4'$ for the expansion rate of 3-space,
    $\alpha_t = -a_4' + b_4'/(2b_4)$ for the common rate of the hidden direction and the
    extra times (Notebook 03a), and $k = e^{2a_4}/b_4$. Then: 3-space with 3-space
    $\alpha^2$; 3-space with the time $x_4$ $\alpha^2 + \alpha'$; 3-space with an extra
    time or with the hidden $x_0$ $\alpha\alpha_t$; the time with an extra time or with
    $x_0$ $\alpha_t^2 + \alpha_t'$; two directions of the block (two extra times, or an
    extra time and $x_0$) $\alpha_t^2 - H^2 k$. None depends on $z$. The hidden
    direction behaves in every plane exactly like an extra time: together they form one
    block, of constant curvature $-H^2$ before the factor $f^2$ is put in.

    What does the sign mean? Only 6 of the 28 planes are spanned by two space-like
    directions (two of $x_1, x_2, x_3$, or one of them with $x_0$); only for these does
    a positive value mean curved like a sphere and a negative one like a saddle. The
    other 22 planes contain a time-like direction, and there the sign is read from
    free fall. The clearest case: two observers at rest (they fall freely, section 8),
    a small coordinate distance $\Delta x_a$ apart along a direction $x_a$, are a proper
    distance $\xi = h_a\,\Delta x_a$ apart, where $h_a$ is the scale factor; the proper
    time of both is $\tau = x_4$. The cell computes $(d^2\xi/d\tau^2)/\xi =
    (\partial_4^2 h_a)/h_a$ for $x_a = x_1$ ($h_1 = e^{a_4}$), $x_a = x_5$
    ($h_5 = fW$) and $x_a = x_0$ ($h_0 = f\cot z$) and checks that it is exactly
    $\sigma(a, x_4)$: $d^2\xi/d\tau^2 = +\sigma(a, x_4)\,\xi$. Along the history
    $a_4 = AHx_4$, $b_4 = e^{\beta AHx_4}$ ($\beta = 4/3$, so $\alpha_t = -AH/3$) they are
    $A^2H^2 > 0$ and $A^2H^2/9 > 0$: positive curvatures, and yet the 3-space distance
    grows like $e^{AH\tau}$ (the hidden and extra-time distances shrink like
    $e^{-AH\tau/3}$, also with a positive second derivative); on a sphere a positive
    curvature pulls neighbouring paths together, $d^2\xi/ds^2 = -\sigma\,\xi$.

    Then the cell draws the 28 plane curvatures as $8 \times 8$ heat maps on the first
    slice of the history, $a_4 = 0$, $b_4 = b_4(0) = 1$ (so $k = 1$), with $a_4' = AH$,
    $a_4'' = 0$, $b_4'/b_4 = \beta AH$, $H = 1$, for the three slopes $A = 0.5$, $1$ (the
    canonical value of the Revision record) and $2$, all positive, so that in all three
    the extra times deflate; the diagonal is left empty.
    """),
    code(r'''
    plane = {(a, b): plain(sp.S(get(R_mixed, (a, b, a, b))))  # sp.S: 0 as a sympy 0
             for a, b in itertools.product(range(8), repeat=2) if a != b}
    alpha_t = -a4p + b4p / (2 * b4v)  # the common rate of x0 and the extra times
    alpha_t_prime = -a4pp + b4pp / (2 * b4v) - b4p ** 2 / (2 * b4v ** 2)  # its derivative
    k_value = sp.exp(2 * a4v) / b4v  # k = e^(2 a4)/b4 = 1/f^2
    # the planes (row, column) in the author's order x0, x1, ..., x7
    expected = {(1, 2): a4p ** 2, (1, 4): a4p ** 2 + a4pp,
                (1, 5): a4p * alpha_t, (1, 0): a4p * alpha_t,
                (4, 5): alpha_t ** 2 + alpha_t_prime, (4, 0): alpha_t ** 2 + alpha_t_prime,
                (5, 6): alpha_t ** 2 - H ** 2 * k_value,
                (5, 0): alpha_t ** 2 - H ** 2 * k_value}
    for (a, b), formula in expected.items():
        say(f"  plane ({NAMES[a]}, {NAMES[b]}): R^ab_ab = {plane[(a, b)]}")
    check(all(sp.simplify(plane[key] - formula) == 0 for key, formula in expected.items())
          and all(not v.has(z) for v in plane.values()),
          "the plane curvatures have the eight formulas and do not depend on z")
    apart = {1: sp.exp(a4), 5: sp.exp(-a4) * sp.sqrt(b4) * W(x0),
             0: sp.exp(-a4) * sp.sqrt(b4) * sp.cot(6 * H * x0)}  # h1, h5, h0
    growth = {}  # (d^2 xi/d tau^2)/xi for observers at rest apart along x1, x5 or x0
    for a, h_a in apart.items():  # xi = h_a times a fixed coordinate distance, tau = x4
        growth[a] = sp.expand(plain(sp.simplify(sp.diff(h_a, x4, 2) / h_a)))
        say(f"  at rest, apart along {NAMES[a]}: (d^2 xi/d tau^2)/xi = {growth[a]}")
    check(sp.simplify(apart[1] ** 2 - g[1, 1]) == 0
          and sp.simplify(apart[5] ** 2 + g[5, 5]) == 0
          and sp.simplify(apart[0] ** 2 - g[0, 0]) == 0
          and all(sp.simplify(growth[a] - plane[(a, 4)]) == 0 for a in apart),
          "observers at rest: d^2 xi/d tau^2 = +R^ab_ab xi in the planes (x1, x4), "
          "(x5, x4) and (x0, x4)")
    SLOPES = (0.5, 1.0, 2.0)  # three deflating histories, A > 0
    BETA = sp.Rational(4, 3)  # b4 = b4(0) e^(beta A H x4) on the history


    def history_values(slope, slice_a4=0):
        """a4p, a4pp, b4p, b4pp, a4v, b4v on the history with the slope A (H = 1,
        b4(0) = 1) at the slice a4 = slice_a4, where b4 = e^(beta a4)."""
        b4_slice = sp.exp(BETA * slice_a4)
        return {a4p: slope, a4pp: 0, H: 1, b4p: BETA * slope * b4_slice,
                b4pp: (BETA * slope) ** 2 * b4_slice, a4v: slice_a4, b4v: b4_slice}


    fig, axes = plt.subplots(1, 3, figsize=(15.0, 4.8))  # wide: room for 0.0278
    for ax, slope in zip(axes, SLOPES):
        curv = np.full((8, 8), np.nan)  # NaN: an empty square on the diagonal
        for (a, b), value in plane.items():
            curv[a, b] = float(sp.simplify(value.subs(history_values(slope))))
        image = ax.imshow(curv, cmap=DIVERGING, vmin=-5.0, vmax=5.0)
        for a, b in plane:
            ax.text(b, a, f"{curv[a, b]:.3g}", ha="center", va="center", fontsize=6.0)
        ax.set_xticks(range(8), LABELS, fontsize=8)
        ax.set_yticks(range(8), LABELS, fontsize=8)
        ax.grid(False)
        ax.set_title(f"$A = {slope:g}$")
    fig.colorbar(image, ax=axes, shrink=0.85, label="curvature (unit $H^2$)")
    save_figure(fig, "plane_curvatures",
                "The curvature $\\sigma(a, b) = R^{ab}{}_{ab}$ (no sum) of the plane of "
                "$x_a$ (row) and $x_b$ (column), unit $H^2$, on the first slice "
                "$a_4 = 0$, $b_4 = 1$ ($k = 1$) of the history "
                "$a_4 = AHx_4$, $b_4 = e^{4AHx_4/3}$ "
                "($a_4^{\\prime\\prime} = 0$, $H = 1$) for $A = 0.5$, "
                "$1$ (canonical) and $2$ (left to right); red positive, blue negative "
                "(sphere-like and saddle-like only for two space-like "
                "directions; with $x_4$ a positive value means "
                "$d^2\\xi/d\\tau^2 = +\\sigma\\xi$). "
                "Inside 3-space and 3-space with $x_4$ $a_4^{\\prime 2}$ ($0.25$, $1$, "
                "$4$); 3-space with $x_0$ or an extra time $-a_4^{\\prime 2}/3$ "
                "($-0.0833$, $-0.333$, $-1.33$); $x_4$ with $x_0$ or an extra time "
                "$a_4^{\\prime 2}/9$ ($0.0278$, $0.111$, $0.444$); inside the block of "
                "$x_0$ and the extra times $a_4^{\\prime 2}/9 - H^2 k$ ($-0.972$, "
                "$-0.889$, $-0.556$). The rows and columns of $x_0$ repeat those of "
                "the extra times.")
    check([float(plane[(1, 2)].subs(history_values(s))) for s in SLOPES]
          == [0.25, 1.0, 4.0]
          and [sp.simplify(plane[(5, 6)].subs(history_values(s))) for s in (1, 2)]
          == [sp.Rational(-8, 9), sp.Rational(-5, 9)],
          "on the slice a4 = 0 the planes inside 3-space are 0.25, 1, 4 and inside the "
          "block -8/9, -5/9 (A = 1, 2)")
    '''),
    md(r"""
    ## 11. Ricci tensor, Ricci scalar, Einstein tensor

    The next cell contracts the Riemann tensor: $R^a{}_b = \sum_c R^{ac}{}_{bc}$, then
    $R = \sum_a R^a{}_a$ and $G^a{}_b = R^a{}_b - \tfrac12 \delta^a{}_b R$. It prints the
    diagonal and compares all 64 components of each tensor and the scalar with the
    record (`ricciMixed`, `ricciScalar`, `einsteinMixed`), after confirming with
    `record_check` that the independent verification of the record passed its check
    `rust_ricci_einstein_scalar_agree`.
    """),
    code(r'''
    def ricci(mixed_table, n):
        """R^a_b = sum over c of R^ac_bc, as an n x n sympy matrix."""
        result = sp.zeros(n, n)
        for (a, c, b, d), value in mixed_table.items():
            if c == d:
                result[a, b] += value
        return result.applyfunc(tidy)


    Ric = ricci(R_mixed, 8)
    R_scalar = tidy(Ric.trace())
    G_mixed = (Ric - R_scalar / 2 * sp.eye(8)).applyfunc(tidy)
    for k in range(8):
        say(f"  {NAMES[k]}: R^a_a = {plain(Ric[k, k])}")
        say(f"      G^a_a = {plain(G_mixed[k, k])}")
    say(f"Ricci scalar R = {plain(R_scalar)}")
    ricci_ok = all(same(Ric[i, j], from_mathematica(
        record["ricciMixed"][f"{NAMES[i]},{NAMES[j]}"]["mathematica"]))
        for i in range(8) for j in range(8))
    einstein_ok = all(same(G_mixed[i, j], from_mathematica(
        record["einsteinMixed"][f"{NAMES[i]},{NAMES[j]}"]["mathematica"]))
        for i in range(8) for j in range(8))
    scalar_ok = same(R_scalar, from_mathematica(record["ricciScalar"]))
    record_check(PYTHON_REPORT, "rust_ricci_einstein_scalar_agree")  # stops if not
    check(ricci_ok and einstein_ok and scalar_ok,
          "all 64 Ricci, all 64 Einstein components and R equal the record",
          record=f"{CURVATURE_RECORD}, ricciMixed, einsteinMixed, ricciScalar (and "
                 "python-lovelock-report.json, check rust_ricci_einstein_scalar_agree)")
    '''),
    md(r"""
    The Ricci scalar appears in one more Revision record, in a different form. The
    record of the field equations of $a_4$ builds them from three **Lovelock
    scalars** $L_{(1)}, L_{(2)}, L_{(3)}$ (the subject of a later chapter), and the
    first of them is exactly twice the Ricci scalar, $L_{(1)} = 2R$ (this identity is
    the check `L1_equals_2R` of the record
    `Revision/gkd_lovelock/results/python-lovelock-report.json`). The sympy
    verification of the record of the field equations,
    `Revision/field_equations_a4/reports/python-a4-report.json`, prints $L_{(1)}$ in its
    check `L1_equals_gkd_branch`, with the names `ad1` for $a_4'$, `ad2` for $a_4''$,
    `uu` for $u = b_4'/b_4$, `vv` for $v = u' = b_4''/b_4 - u^2$ and `kk` for
    $k = e^{2a_4}/b_4$. The next cell reads this text, checks that the record marks the
    check as passed, turns the text after the equals sign into a sympy expression,
    confirms with `record_check` that the check `L1_equals_2R` passed, writes our $R$ in
    $u$, $v$ and $k$ ($b_4' = u\,b_4$, $b_4'' = (v + u^2)\,b_4$, $e^{2a_4} = k\,b_4$) and
    checks $L_{(1)} = 2R$.
    """),
    code(r'''
    A4_REPORT = "Revision/field_equations_a4/reports/python-a4-report.json"
    a4_report = json.loads(repository_file(A4_REPORT).read_text(encoding="utf-8"))
    # the report's checks form a list of dictionaries; take the one with this name
    L1_entry = next(entry for entry in a4_report["checks"]
                    if entry["name"] == "L1_equals_gkd_branch")
    L1_detail, L1_verdict = L1_entry["detail"], L1_entry["verdict"]
    say(f"record: {L1_detail} ({L1_verdict})")
    u_sym, v_sym, k_sym = sp.symbols("u v k", real=True)  # u = b4'/b4, v = u', k
    L1_text = L1_detail.split("=")[1]  # the text after the equals sign
    L1_record = parse_expr(L1_text, local_dict={"H": H, "ad1": a4p, "ad2": a4pp,
                                                "uu": u_sym, "vv": v_sym, "kk": k_sym})
    record_check(PYTHON_REPORT, "L1_equals_2R", "L_(1) = 2 R exactly")  # stops if not
    IN_UVK = {b4p: u_sym * b4v, b4pp: (v_sym + u_sym ** 2) * b4v}  # b4' and b4''
    TO_K = {a4v: sp.log(k_sym * b4v) / 2}  # a4 = ln(k b4)/2, that is e^(2 a4) = k b4
    R_in_uv = sp.expand(sp.simplify(plain(R_scalar).subs(IN_UVK).subs(
        TO_K)))  # b4v and a4v drop out
    say(f"our R in u, v and k: {R_in_uv}")
    check(L1_verdict == "PASS" and not R_in_uv.has(b4v) and not R_in_uv.has(a4v)
          and sp.expand(L1_record - 2 * R_in_uv) == 0,
          "the first Lovelock scalar of the record is twice our Ricci scalar (in u, v, k)",
          record=f"{A4_REPORT}, check L1_equals_gkd_branch (with "
                 "python-lovelock-report.json, check L1_equals_2R)")
    '''),
    md(r"""
    Exact agreement was decided by sympy's simplification. A second, independent test
    uses numbers only: the independent Revision verification
    (`Revision/gkd_lovelock/results/python-lovelock-report.json`, list `randomPoints`)
    chose five test points, each a set of exact fractions for $H$, $x_0$, $a_4$, $a_4'$,
    $a_4''$, $b_4$, $b_4'$ and $b_4''$, with $z = 6Hx_0$ in each quarter of the period
    (one point at $z = -2.2$). The next cell evaluates every component of the record
    (21 Christoffel symbols, 112 Riemann components, 64 Ricci and 64 Einstein
    components and the Ricci scalar) and our component with the same indices at these
    five points, with **30 significant digits** (the package mpmath;
    `sp.lambdify(..., "mpmath")` turns an expression into an mpmath function), after
    writing the warp factor as $|\sin z|^{1/6}$ and $G$ as the sign of $\cot z$, and
    reports the largest relative difference
    $|{\rm ours} - {\rm record}| / \max(1, |{\rm record}|)$. Before it reports, it
    confirms with `record_check` that the three exact comparisons of that verification
    (`rust_christoffels_agree`, `rust_riemann_agrees`,
    `rust_ricci_einstein_scalar_agree`) passed.
    """),
    code(r'''
    python_report = json.loads(repository_file(PYTHON_REPORT).read_text(encoding="utf-8"))
    mpmath.mp.dps = 30  # mpmath works with 30 significant digits from now on


    def exact(text):
        """A fraction such as 46/75 of the record as an mpmath number."""
        fraction = sp.Rational(text)
        return mpmath.mpf(fraction.p) / fraction.q  # numerator / denominator


    def as_numbers(expression):
        """The expression with W(x0) = |sin z|^(1/6) and G = the sign of cot z."""
        return sp.S(expression).subs(W(x0), sp.Abs(sp.sin(6 * H * x0)) ** sp.Rational(
            1, 6)).subs(G, sp.sign(sp.cot(6 * H * x0)))


    test_points = [[exact(p["H"]), exact(p["x0"]), exact(p["a4"]),
                    exact(p["a4" + prime]), exact(p["a4" + prime + prime]),
                    exact(p["b4"]), exact(p["b4" + prime]), exact(p["b4" + prime + prime])]
                   for p in python_report["randomPoints"]]
    say("z = 6 H x0 at the five test points: "
        + ", ".join(mpmath.nstr(6 * p[0] * p[1], 4) for p in test_points))
    pairs = [(Gamma[a][b][c], v) for (a, b, c), v in record_gamma.items()]
    pairs += [(R_mixed[key], v) for key, v in record_riemann.items()]
    pairs += [(Ric[i, j], from_mathematica(record["ricciMixed"][f"{NAMES[i]},{NAMES[j]}"]
                                           ["mathematica"]))
              for i in range(8) for j in range(8)]
    pairs += [(G_mixed[i, j], from_mathematica(
        record["einsteinMixed"][f"{NAMES[i]},{NAMES[j]}"]["mathematica"]))
        for i in range(8) for j in range(8)]
    pairs += [(R_scalar, from_mathematica(record["ricciScalar"]))]
    # the order of the eight numbers of a test point
    ARGS30 = (H, x0, a4v, a4p, a4pp, b4v, b4p, b4pp)
    largest, evaluations = mpmath.mpf(0), 0
    for mine, theirs in pairs:
        f_mine = sp.lambdify(ARGS30, as_numbers(symbolic(sp.S(mine))), "mpmath")
        f_record = sp.lambdify(ARGS30, as_numbers(theirs), "mpmath")
        for point in test_points:
            ours, recorded = f_mine(*point), f_record(*point)
            largest = max(largest, abs(ours - recorded) / max(1, abs(recorded)))
            evaluations += 1
    for name in ("rust_christoffels_agree", "rust_riemann_agrees",
                 "rust_ricci_einstein_scalar_agree"):
        record_check(PYTHON_REPORT, name)  # stops unless the check passed
    report("components compared numerically", len(pairs))
    report("evaluations at the five test points", evaluations)
    report("largest relative difference (30 digits)", mpmath.nstr(largest, 3))
    check(len(test_points) == 5 and largest < mpmath.mpf(10) ** -25,
          "at the five test points every component agrees to more than 25 digits",
          record="Revision/gkd_lovelock/results/python-lovelock-report.json, "
                 "randomPoints, checks rust_christoffels_agree, rust_riemann_agrees, "
                 "rust_ricci_einstein_scalar_agree")
    '''),
    md(r"""
    The lead's independent check of the field equations
    (`Revision/lead_checks/reports/einstein-gauss-bonnet-a4.json`) states several
    properties of the Einstein tensor of the corrected metric with general $b_4$. The
    next cell first confirms with `record_check` that the lead's report lists them as
    passed, then checks them on our result. (1) Every one of the 56 off-diagonal
    components of the Einstein tensor vanishes, for all $a_4(x_4)$, $b_4(x_4)$ and every
    real $z$: the reason why the metric was corrected (the record of the corrected
    metric checks the same for all three Lovelock tensors,
    `Revision/metric_warped/reports/python-warped-metric-report.json`, check
    `corrected_offdiagonal_all_orders`). (2) No diagonal component depends on $x_0$.
    (3) The three 3-space components are equal, and the hidden component equals the
    three extra-time components: $G^{x_0}{}_{x_0} = G^{x_5}{}_{x_5}$, so a source must
    have equal hidden and extra-time pressures, $p_0 = p_t$. (4) With $u = b_4'/b_4$,
    $v = u'$ and $k = e^{2a_4}/b_4$,
    $G^{x_0}{}_{x_0} - G^{x_4}{}_{x_4} = -\tfrac32(2H^2k + 4a_4'^2 - a_4'u + v)$, the
    combination that the field equations turn into $\kappa(\rho + p_0)$. (5) The member
    $a_4 = 0$, $b_4 = H^2(x_4 - c)^2$ of the family is flat: every Riemann component
    vanishes there, so it is a solution of the vacuum equations (with $\Lambda = 0$).
    """),
    code(r'''
    LEAD = "Revision/lead_checks/reports/einstein-gauss-bonnet-a4.json"
    for name in ("einstein_off_diagonal_vanish", "einstein_diagonal_x0_independent",
                 "einstein_isotropy", "einstein_null_energy", "einstein_flat_vacuum"):
        record_check(LEAD, name)  # stops unless the lead check passed
    WARPED_REPORT = "Revision/metric_warped/reports/python-warped-metric-report.json"
    for name in ("corrected_offdiagonal_all_orders", "milne_flat_check"):
        record_check(WARPED_REPORT, name)  # stops unless the check passed
    record_check(PYTHON_REPORT, "k1_offdiagonal_vanishes")
    record_check(PYTHON_REPORT, "k1_hidden_equals_extra_times")
    off_diagonal = [(i, j) for i in range(8) for j in range(8)
                    if i != j and (G_mixed[i, j] != 0 or Ric[i, j] != 0)]
    check(off_diagonal == [],
          "all 56 off-diagonal components of the Einstein and Ricci tensors vanish",
          record=f"{LEAD}, check einstein_off_diagonal_vanish, and "
                 "python-warped-metric-report.json, check corrected_offdiagonal_all_orders")
    check(all(not symbolic(G_mixed[k, k]).has(x0) for k in range(8)),
          "no diagonal component of the Einstein tensor depends on x0",
          record=f"{LEAD}, check einstein_diagonal_x0_independent")
    check(G_mixed[1, 1] == G_mixed[2, 2] == G_mixed[3, 3]
          and G_mixed[0, 0] == G_mixed[5, 5] == G_mixed[6, 6] == G_mixed[7, 7],
          "3-space components equal; the hidden component equals the extra-time ones",
          record=f"{LEAD}, check einstein_isotropy (and python-lovelock-report.json, "
                 "check k1_hidden_equals_extra_times)")
    gap = sp.simplify(plain(G_mixed[0, 0] - G_mixed[4, 4]).subs(IN_UVK).subs(TO_K))
    say(f"G^x0_x0 - G^x4_x4 = {sp.expand(gap)}")
    check(sp.expand(gap + sp.Rational(3, 2) * (2 * H ** 2 * k_sym + 4 * a4p ** 2
                                                - a4p * u_sym + v_sym)) == 0,
          "G^x0_x0 - G^x4_x4 = -(3/2)(2 H^2 k + 4 a4p^2 - a4p u + v)",
          record=f"{LEAD}, check einstein_null_energy")
    c_shift = sp.symbols("c", real=True)  # the constant c of the flat member
    flat = {sp.Derivative(a4, (x4, 2)): 0, sp.Derivative(a4, x4): 0, a4: 0,
            sp.Derivative(b4, (x4, 2)): 2 * H ** 2, sp.Derivative(b4, x4):
            2 * H ** 2 * (x4 - c_shift), b4: H ** 2 * (x4 - c_shift) ** 2}
    check(all(sp.simplify(v.subs(flat)) == 0 for v in R_mixed.values()),
          "the member a4 = 0, b4 = H^2 (x4 - c)^2 is flat: all 112 components vanish",
          record=f"{LEAD}, check einstein_flat_vacuum, and "
                 "python-warped-metric-report.json, check milne_flat_check")
    '''),
    md(r"""
    Every Einstein tensor satisfies the **contracted Bianchi identity**
    $\sum_\mu \nabla_\mu G^\mu{}_\nu = 0$, where for a tensor with one upper and one
    lower index $\sum_\mu \nabla_\mu G^\mu{}_\nu = \sum_\mu \partial_\mu G^\mu{}_\nu +
    \sum_{\mu,\lambda} \Gamma^\mu{}_{\mu\lambda} G^\lambda{}_\nu - \sum_{\mu,\lambda}
    \Gamma^\lambda{}_{\mu\nu} G^\mu{}_\lambda$. Within Einstein's equations it makes the
    energy and momentum of the matter that sources the metric conserved. The next cell
    computes the eight components with the function $a_4(x_4)$ (so that sympy can
    differentiate $a_4''$ and produce $a_4'''$) and checks that each simplifies to zero.
    The Rust program checked the same for its tensor $P_{(1)} = -4G$ (its checks
    `k1_equals_minus_4_einstein` and `k1_divergence_free`, which the cell confirms with
    `record_check`).
    """),
    code(r'''
    divergence = []
    for nu in range(8):
        value = sum(sp.diff(G_mixed[mu, nu], X[mu]) for mu in range(8)) \
            + sum(Gamma[mu][mu][lam] * G_mixed[lam, nu]
                  for mu in range(8) for lam in range(8)) \
            - sum(Gamma[lam][mu][nu] * G_mixed[mu, lam]
                  for mu in range(8) for lam in range(8))
        divergence.append(vanishes(value))
    record_check(RUST_REPORT, "k1_equals_minus_4_einstein")  # stops if not passed
    record_check(RUST_REPORT, "k1_divergence_free")
    check(all(divergence),
          "the contracted Bianchi identity: the divergence of G vanishes",
          record="Revision/gkd_lovelock/results/lovelock-report.json, checks "
                 "k1_equals_minus_4_einstein and k1_divergence_free")
    '''),
    md(r"""
    ## 12. The Kretschmann scalar: an invariant that does not see $z$

    The next cell computes $K = \sum R^{ab}{}_{cd} R^{cd}{}_{ab}$ and
    $\sum_{a,b} R^a{}_b R^b{}_a$ from our components, and computes $K$ a second time
    from the 112 components of the record alone. Every component is a plane curvature
    $\pm\sigma(a, b)$, and each of the 28 planes contributes four components, so
    $K = 4\sum_{\rm planes}\sigma^2$: with the five kinds of planes of section 10,

    $$K = 4\bigl[3\alpha^4 + 3(\alpha^2 + \alpha')^2 + 12\alpha^2\alpha_t^2
    + 4(\alpha_t^2 + \alpha_t')^2 + 6(\alpha_t^2 - H^2 k)^2\bigr] .$$

    It does not depend on $z$, and on $a_4$ and $b_4$ only through $a_4'$, $a_4''$,
    $u$, $v$ and $k$. A sum of squares vanishes only when every square does, so $K = 0$
    exactly when all 28 plane curvatures vanish: on the flat member of the previous
    section. The cell checks all of this.
    """),
    code(r'''
    K = sp.factor(sp.expand(symbolic(sum(v * get(R_mixed, (c, d, a, b))
                                         for (a, b, c, d), v in R_mixed.items()))))
    K_record = sp.factor(sp.expand(sum(v * record_riemann.get((c, d, a, b), 0)
                                       for (a, b, c, d), v in record_riemann.items())))
    ricci_square = sp.factor(sp.expand(symbolic(sum(Ric[i, j] * Ric[j, i]
                                                    for i in range(8)
                                                    for j in range(8)))))
    say(f"Kretschmann scalar K = {K}")
    say(f"sum of R^a_b R^b_a  = {ricci_square}")
    check(sp.simplify(K - K_record) == 0,
          "K from our components equals K from the 112 components of the record")
    sum_of_squares = 4 * (3 * a4p ** 4 + 3 * (a4p ** 2 + a4pp) ** 2
                          + 12 * a4p ** 2 * alpha_t ** 2
                          + 4 * (alpha_t ** 2 + alpha_t_prime) ** 2
                          + 6 * (alpha_t ** 2 - H ** 2 * k_value) ** 2)
    K_in_uvk = sp.expand(sp.simplify(K.subs(IN_UVK).subs(TO_K)))
    check(not K.has(x0) and sp.simplify(K - sum_of_squares) == 0
          and not K_in_uvk.has(a4v) and not K_in_uvk.has(b4v),
          "K = 4 times the sum of the 28 squared plane curvatures; no z, and a4, b4 "
          "only through a4p, a4pp, u, v, k")
    check(sp.simplify(sp.factor(symbolic(sum(
        v * get(R_mixed, (c, d, a, b)) for (a, b, c, d), v in R_mixed.items())).subs(
        {a4pp: 0, a4p: 0, a4v: 0, b4pp: 2 * H ** 2, b4p: 2 * H ** 2 * (x4 - c_shift),
         b4v: H ** 2 * (x4 - c_shift) ** 2}))) == 0,
          "K = 0 on the flat member a4 = 0, b4 = H^2 (x4 - c)^2")
    '''),
    md(r"""
    The next cell shows in pictures that the geometry does not see $z$, on the history
    ($a_4'' = 0$, $b_4'/b_4 = \tfrac43 a_4'$, $b_4''/b_4 = (b_4'/b_4)^2$) at the slice
    $a_4 = 0.5$, $b_4 = e^{2/3}$, with $H = 1$. Left: across one cell, the sizes of two
    Christoffel symbols, $\Gamma^{x_0}{}_{x_0x_0}$ and $\Gamma^{x_5}{}_{x_5x_0} =
    H\cot z$, which grow without bound at the tips (and the first also at the fold),
    and of two Riemann components, $\sigma(x_5, x_6) = R^{x_5x_6}{}_{x_5x_6}$ and
    $\sigma(x_1, x_0) = R^{x_1x_0}{}_{x_1x_0}$, which are the same at every $z$, for
    $a_4' = 1.5$. Right: $K$ computed at 300 values of $z$ across one cell by summing
    all 112 products numerically, for four expansion rates $a_4' = A H$ of deflating
    histories, $A = 0.5, 1, 1.5, 2$: four flat lines.
    """),
    code(r'''
    # numerical functions of the 112 components on the history: a4pp = 0 and
    # b4'' = b4'^2/b4 (v = (b4'/b4)' = 0); the second derivatives are replaced first
    riemann_functions = {k: numeric(v.subs({sp.Derivative(a4, (x4, 2)): 0,
                                            sp.Derivative(b4, (x4, 2)):
                                            sp.Derivative(b4, x4) ** 2 / b4}))
                         for k, v in R_mixed.items()}


    def on_history(rate):
        """a4, a4p, H, b4, b4p at the slice a4 = 0.5 for the rate a4p = rate (H = 1):
        b4 = e^(2/3) and b4'/b4 = (4/3) a4p."""
        return (0.5, rate, 1.0, B4_SLICE, 4.0 / 3.0 * rate * B4_SLICE)


    def kretschmann_numbers(z_values, rate):
        """K at the points z_values, summed from the 112 numerical components."""
        total = np.zeros_like(z_values)
        for (a, b, c, d), f in riemann_functions.items():
            partner = riemann_functions.get((c, d, a, b))
            if partner is not None:
                total += (f(z_values, *on_history(rate))
                          * partner(z_values, *on_history(rate)))
        return total


    z_line = np.linspace(0.02, np.pi - 0.02, 300)
    z_line = z_line[np.abs(z_line - np.pi / 2) > 0.01]  # leave out the fold itself
    fig, axes = plt.subplots(1, 2, figsize=(10.5, 4.2))
    fig.subplots_adjust(wspace=0.32)  # room for the label of the right vertical axis
    for index, colour, style, label in (
            ((0, 0, 0), VIOLET, "--", "$\\Gamma^{x_0}{}_{x_0x_0}$ (coordinates)"),
            ((5, 5, 0), RED, "-", "$\\Gamma^{x_5}{}_{x_5x_0}$ (coordinates)")):
        values = gamma_functions[index](z_line, *on_history(1.5))
        axes[0].plot(z_line, np.abs(values), color=colour, ls=style, lw=1.8, label=label)
    for key, colour, style, label in (
            ((5, 6, 5, 6), BLUE, "-.", "$\\sigma(x_5, x_6)$ (geometry)"),
            ((1, 0, 1, 0), AQUA, ":", "$\\sigma(x_1, x_0)$ (geometry)")):
        values = np.broadcast_to(riemann_functions[key](z_line, *on_history(1.5)),
                                 z_line.shape)
        axes[0].plot(z_line, np.abs(values), color=colour, ls=style, lw=2.0, label=label)
    axes[0].set_yscale("log")
    axes[0].set_xlabel("$z = 6 H x_0$ (radians)")
    axes[0].set_ylabel("absolute value (unit $H$ or $H^2$)")
    axes[0].set_title("Symbols and curvatures, $a_4^{\\prime} = 1.5$")
    axes[0].legend(fontsize=7, loc="upper center")
    rates = (0.5, 1.0, 1.5, 2.0)  # four expansion rates a4p = A H (A > 0), unit H
    for rate, colour, style in zip(rates, (VIOLET, AQUA, RED, ORANGE),
                                   ("-", "--", "-.", ":")):
        axes[1].plot(z_line, kretschmann_numbers(z_line, rate), color=colour, ls=style,
                     lw=1.8, label=f"$a_4^{{\\prime}} = {rate:g}\\,H$")
    axes[1].set_yscale("log")
    axes[1].set_xlabel("$z = 6 H x_0$ (radians)")
    axes[1].set_ylabel("$K$ (unit $H^4$)")
    axes[1].set_title("Kretschmann scalar summed from 112 components")
    axes[1].legend(fontsize=8)
    # the values of the formula for K at the four rates on the history, for the caption
    # and the check
    K_values = [float(sp.simplify(K.subs({a4p: r, a4pp: 0, H: 1, a4v: 0.5,
                                          b4v: B4_SLICE,
                                          b4p: sp.Rational(4, 3) * r * B4_SLICE,
                                          b4pp: (sp.Rational(4, 3) * r) ** 2 * B4_SLICE})))
                for r in rates]
    K_text = ", ".join(f"${k:.4g}$" for k in K_values)
    save_figure(fig, "riemann_and_kretschmann_z",
                "Left: across one cell $0 < z < \\pi$, the absolute values of the "
                "Christoffel symbols $\\Gamma^{x_0}{}_{x_0x_0}$ (dashed) and "
                "$\\Gamma^{x_5}{}_{x_5x_0} = H\\cot z$ (solid), which depend on the "
                "coordinate $x_0$ and grow without bound at the tips, and of the plane "
                "curvatures $\\sigma(x_5, x_6)$ (dash-dotted) and $\\sigma(x_1, x_0)$ "
                "(dotted), which are the same at every $z$, for $a_4^{\\prime} = 1.5$ on "
                "the history at the slice $a_4 = 0.5$, $b_4 = e^{2/3}$, "
                "$H = 1$; horizontal axis $z = 6Hx_0$ in "
                "radians, vertical axis logarithmic, units $H$ and $H^2$. "
                "Right: the Kretschmann scalar $K$ summed numerically from all 112 "
                "components at 300 values of $z$ for $a_4^{\\prime} = 0.5, 1, 1.5, 2$ "
                "(in units of $H$) at the same slice, "
                "vertical axis $K$ in units of $H^4$, logarithmic. "
                f"$K$ is the same at every $z$: {K_text}.")
    numbers = [kretschmann_numbers(z_line, r) for r in rates]
    check(all(np.max(np.abs(n - k)) < 1e-9 * k for n, k in zip(numbers, K_values)),
          "summed numerically, K is the same at all values of z and equals the formula")
    '''),
    md(r"""
    ## 13. The curvature along the deflating history

    Along the history $a_4 = A H x_4$, $b_4 = b_4(0)\,e^{\beta A H x_4}$ with
    $\beta = 4/3$ and $b_4(0) = 1$ we have $a_4' = A H$, $a_4'' = 0$,
    $b_4'/b_4 = \beta A H$, $b_4''/b_4 = (\beta A H)^2$ and
    $k = e^{2a_4}/b_4 = e^{(2 - \beta)a_4} = e^{2a_4/3}$: every curvature scalar is a
    polynomial in the slope $A$ and in $k$, and $k$ grows along the history, from $1$ at
    the slice $a_4 = 0$ to $e^{4/3} = 3.79$ at the slice $a_4 = 2$. (The value
    $b_4(0) = 1$ is the choice of the Revision record; unlike the withdrawn metric of
    2026-10-14, the corrected metric does not let a rescaling of the extra times remove
    it, because $b_4$ also stands in the hidden entry.) The author's extra times deflate
    when $a_4$ increases, that is for $A > 0$; the Revision record uses $A = 1$. The next
    cell evaluates the Ricci scalar $R = (\tfrac{56}{9} A^2 - 12k)H^2$, the sum
    $\sum R^a{}_b R^b{}_a$ and $K$ as formulas in $A$ and $k$, checks that they are
    **even** in $A$ at fixed $k$ (they do not change when $A$ is replaced by $-A$; so
    these three scalars cannot tell which of the two families of directions deflates,
    the metric and the components of the curvature tensors can), and draws them for
    $0.1 \le A \le 3$ at the three slices $a_4 = 0$, $1$, $2$ ($k = 1$, $e^{2/3}$,
    $e^{4/3}$): $R$ on an ordinary axis, $K$ and $\sum R^a{}_b R^b{}_a$ on a logarithmic
    axis.
    """),
    code(r'''
    A = sp.symbols("A", real=True)  # the slope of the history a4 = A H x4
    on_history = {a4p: A * H, a4pp: 0, b4p: BETA * A * H * b4v,
                  b4pp: (BETA * A * H) ** 2 * b4v}


    def along_history(expression):
        """An expression on the history, written with A, k and H."""
        value = sp.simplify(symbolic(expression).subs(on_history).subs(TO_K))
        return sp.factor(sp.expand(value))


    R_A, K_A, RR_A = (along_history(e) for e in (R_scalar, K, ricci_square))
    say(f"on the history: R = {R_A}")
    say(f"  K = {sp.expand(K_A)}")
    say(f"  R^a_b R^b_a = {sp.expand(RR_A)}")
    check(all(sp.expand(f.subs(A, -A) - f) == 0 and not f.has(b4v) and not f.has(a4v)
              for f in (R_A, K_A, RR_A)),
          "on the history the curvature scalars are even in A and depend on A and k only")
    A_line = np.linspace(0.1, 3.0, 291)  # slopes 0.1, 0.11, ..., 3; A_line[90] = 1
    SLICE_K = [(0, 1.0), (1, np.exp(2.0 / 3.0)), (2, np.exp(4.0 / 3.0))]  # (a4, k)
    fig, axes = plt.subplots(1, 2, figsize=(10.0, 4.2))
    for (slice_a4, k_number), style in zip(SLICE_K, ("-", "--", ":")):
        on_slice = {H: 1, k_sym: k_number}
        R_numbers = sp.lambdify(A, R_A.subs(on_slice))(A_line)
        K_numbers = sp.lambdify(A, K_A.subs(on_slice))(A_line)
        RR_numbers = sp.lambdify(A, RR_A.subs(on_slice))(A_line)
        axes[0].plot(A_line, R_numbers, color=VIOLET, ls=style, lw=1.8,
                     label=f"$R$, slice $a_4 = {slice_a4}$")
        axes[1].plot(A_line, K_numbers, color=RED, ls=style, lw=1.8,
                     label=f"$K$, slice $a_4 = {slice_a4}$")
        axes[1].plot(A_line, RR_numbers, color=BLUE, ls=style, lw=1.2,
                     label=f"$\\sum R^a{{}}_b R^b{{}}_a$, slice $a_4 = {slice_a4}$")
    axes[0].axhline(0.0, color="black", lw=0.8)
    axes[0].set_ylabel("Ricci scalar $R$ (unit $H^2$)")
    axes[0].set_title("Ricci scalar $R = (56A^2/9 - 12k)H^2$")
    axes[1].set_yscale("log")
    axes[1].set_ylabel("value (unit $H^4$)")
    axes[1].set_title("Squares of the curvature")
    for ax in axes:
        ax.axvline(1.0, color="grey", lw=1.0, ls=":")  # the canonical slope A = 1
        ax.set_xlabel("slope $A$ of the deflating history $a_4 = A H x_4$")
        ax.legend(fontsize=7, loc="upper left")
    R_canonical = [float(R_A.subs({A: 1, H: 1, k_sym: k_number}))
                   for _, k_number in SLICE_K]
    K_canonical = float(K_A.subs({A: 1, H: 1, k_sym: 1}))
    save_figure(fig, "scalars_versus_a",
                "The curvature scalars of the corrected metric along the deflating "
                "history $a_4 = AHx_4$, $b_4 = e^{4AHx_4/3}$ "
                "($a_4^{\\prime} = AH$, $a_4^{\\prime\\prime} = 0$, "
                "$b_4^{\\prime}/b_4 = \\tfrac43 AH$) as functions of the slope $A$ from "
                "$0.1$ to $3$, with $H = 1$, at the three slices $a_4 = 0$ (solid), $1$ "
                "(dashed) and $2$ (dotted), where $k = e^{2a_4/3} = 1$, $1.95$ and "
                "$3.79$; horizontal axes $A$ (a pure number), the "
                "dotted vertical line marks the canonical $A = 1$ of the Revision "
                "record. Left: the Ricci scalar $R = (56A^2/9 - 12k)H^2$ in units "
                f"of $H^2$ ($R = {R_canonical[0]:.4g}$, ${R_canonical[1]:.4g}$, "
                f"${R_canonical[2]:.4g}$ at $A = 1$). Right, on a logarithmic axis in "
                "units of $H^4$: the Kretschmann scalar $K$ (red) and "
                "$\\sum R^a{}_b R^b{}_a$ (blue), both positive for every $A$; as $k$ "
                "grows along the history, the curvature of the shrinking block of the "
                f"hidden direction and the extra times grows ($K = {K_canonical:.4g}$ "
                "at $A = 1$, $a_4 = 0$).")
    check(sp.expand(R_A - (sp.Rational(56, 9) * A ** 2 - 12 * k_sym) * H ** 2) == 0
          and abs(R_canonical[0] - (-52.0 / 9.0)) < 1e-12,
          "on the history R = (56 A^2/9 - 12 k) H^2; at A = 1, a4 = 0: R = -52/9 H^2")
    '''),
    md(r"""
    The next cell draws the Einstein tensor along the deflating history. It has no
    off-diagonal component (section 11). Its diagonal, in units of $H^2$, is
    $G^{x_4}{}_{x_4} = 6k + \tfrac13 A^2$, $G^{x_1}{}_{x_1} = 6k - \tfrac{13}{9}A^2$ and
    $G^{x_0}{}_{x_0} = G^{x_5}{}_{x_5} = 3k - \tfrac{11}{3}A^2$; the cell prints and
    checks these formulas. Left: the eight diagonal components as bars, for the
    canonical slope $A = 1$ of the Revision record, at the first slice $a_4 = 0$
    ($k = 1$) and at the last slice $a_4 = 2$ ($k = e^{4/3}$). Right: the diagonal along
    the canonical history as functions of the time $x_4$, where $k = e^{2x_4/3}$; the
    gap between the time and the hidden component,
    $G^{x_4}{}_{x_4} - G^{x_0}{}_{x_0} = (3k + 4A^2)H^2$, is never zero, and every
    component grows with $k$.
    """),
    code(r'''
    G_A = [along_history(G_mixed[k, k]) for k in range(8)]
    for k in (0, 1, 4, 5):
        say(f"  on the history: G^{NAMES[k]}_{NAMES[k]} = {sp.expand(G_A[k])}")
    check(sp.expand(G_A[4] - (6 * k_sym + A ** 2 / 3) * H ** 2) == 0
          and sp.expand(G_A[1] - (6 * k_sym - sp.Rational(13, 9) * A ** 2) * H ** 2) == 0
          and sp.expand(G_A[0] - (3 * k_sym - sp.Rational(11, 3) * A ** 2) * H ** 2) == 0
          and G_A[0] == G_A[5],
          "on the history G^x4_x4 = 6k + A^2/3, G^x1_x1 = 6k - 13 A^2/9, "
          "G^x0_x0 = G^x5_x5 = 3k - 11 A^2/3 (unit H^2)")
    bars = {slice_a4: [G_A[k].subs({A: 1, H: 1, k_sym: k_number}) for k in range(8)]
            for slice_a4, k_number in ((0, 1), (2, sp.exp(sp.Rational(4, 3))))}
    fig, axes = plt.subplots(1, 2, figsize=(10.0, 4.2))
    positions = np.arange(8)
    axes[0].bar(positions - 0.2, [float(v) for v in bars[0]], width=0.38, color=RED,
                hatch="//", label="slice $a_4 = 0$ ($k = 1$)")
    axes[0].bar(positions + 0.2, [float(v) for v in bars[2]], width=0.38, color=BLUE,
                label="slice $a_4 = 2$ ($k = e^{4/3}$)")
    axes[0].axhline(0.0, color="black", lw=0.8)
    axes[0].set_xticks(positions, [f"$G^{{x_{k}}}{{}}_{{x_{k}}}$" for k in range(8)],
                       fontsize=8)
    axes[0].set_ylabel("component (unit $H^2$)")
    axes[0].set_title("Diagonal of the Einstein tensor, $A = 1$")
    axes[0].set_ylim(-2.0, 29.0)  # room above the bars for the legend
    axes[0].legend(fontsize=8, loc="upper left")
    x4_line = np.linspace(0.0, 2.5, 251)
    k_line = np.exp(2.0 * x4_line / 3.0)  # k = e^(2 a4/3) on the canonical history
    component = {k: sp.lambdify(k_sym, G_A[k].subs({A: 1, H: 1}))(k_line)
                 for k in (0, 1, 4)}
    axes[1].plot(x4_line, component[1], color=RED, lw=1.8, label="$G^{x_1}{}_{x_1}$")
    axes[1].plot(x4_line, component[0], color=AQUA, lw=1.8, ls=":",
                 label="$G^{x_0}{}_{x_0} = G^{x_5}{}_{x_5}$")
    axes[1].plot(x4_line, component[4], color=VIOLET, lw=1.8, ls="--",
                 label="$G^{x_4}{}_{x_4}$")
    axes[1].fill_between(x4_line, component[0], component[4], color="grey", alpha=0.2,
                         label="gap $(3k + 4)H^2 > 0$")
    axes[1].axhline(0.0, color="black", lw=0.8)
    axes[1].set_xlabel("time $x_4$ (unit $1/H$), history $a_4 = x_4$, "
                       "$b_4 = e^{4x_4/3}$")
    axes[1].set_ylabel("component (unit $H^2$)")
    axes[1].set_title("Einstein tensor along the history ($A = 1$)")
    axes[1].legend(fontsize=8, loc="upper left")
    save_figure(fig, "einstein_tensor",
                "The Einstein tensor $G^{\\mu}{}_{\\nu}$ of the corrected metric along "
                "the deflating history $a_4 = AHx_4$, $b_4 = e^{4AHx_4/3}$ with "
                "$H = 1$, in units of $H^2$; it has no off-diagonal component. "
                "Left: the eight diagonal components for the canonical slope $A = 1$ of "
                "the Revision record at the first slice $a_4 = 0$ (hatched bars: "
                "$-2/3$, $41/9$ three times, $19/3$, $-2/3$ three times) and at the last "
                "slice $a_4 = 2$ (plain bars: $3e^{4/3} - 11/3 = 7.72$, "
                "$6e^{4/3} - 13/9 = 21.3$ three times, $6e^{4/3} + 1/3 = 23.1$, "
                "$7.72$ three times); the hidden component equals the extra-time ones. "
                "Right: the 3-space (solid), hidden and extra-time (dotted) and time "
                "(dashed) components versus the time $x_4$ along the canonical history, "
                "where $k = e^{2x_4/3}$; the shaded gap $(3k + 4)H^2$ between the time "
                "and the hidden component never closes.")
    check(bars[0] == [sp.Rational(-2, 3)] + [sp.Rational(41, 9)] * 3 + [sp.Rational(19, 3)]
          + [sp.Rational(-2, 3)] * 3,
          "diagonal of G at A = 1, slice a4 = 0: (-2/3, 41/9 x3, 19/3, -2/3 x3), unit H^2")
    '''),
    md(r"""
    What do these numbers mean for matter? Einstein's field equations (section 3 of
    this notebook) set $G^\mu{}_\nu + \Lambda\,\delta^\mu{}_\nu = \kappa\, T^\mu{}_\nu$
    with $T = \mathrm{diag}(p_0, p_3, p_3, p_3, -\rho, p_t, p_t, p_t)$. Their $x_4$
    component reads $G^{x_4}{}_{x_4} + \Lambda = -\kappa\rho$, so
    $\kappa\rho = -G^{x_4}{}_{x_4} - \Lambda$; their $x_1$, $x_5$ and $x_0$ components
    read $G^{x_1}{}_{x_1} + \Lambda = \kappa p_3$, $G^{x_5}{}_{x_5} + \Lambda = \kappa
    p_t$ and $G^{x_0}{}_{x_0} + \Lambda = \kappa p_0$; every off-diagonal component of
    the source must vanish, because the left-hand side has none. Along the history the
    hidden and the extra-time components on the left are equal (previous cell), so the
    source must have $p_0 = p_t$, and all of $\rho$, $p_3$, $p_0$ grow with $k$. The
    Revision record of the field equations of $a_4$ and $b_4$
    (`Revision/field_equations_a4/a4-equations.json`, entry `exponentialHistory`, key
    `requiredSource`) lists this required source for the exponential history
    $a_4 = AHx_4 + a_0$, $b_4 = b_4(0)\,e^{\beta AHx_4}$ and for any Lovelock couplings
    $\alpha_1, \alpha_2, \alpha_3$, in its texts `rho`, `p3`, `p0` and `pt`, written with
    `AA` for $A$, `be` for $\beta$, `kk` for $k$ and `Lam` for $\Lambda$. The next cell
    reads the four texts, puts in the Einstein couplings ($\alpha_1 = 1$,
    $\alpha_2 = \alpha_3 = 0$) and $\beta = 4/3$, confirms with `record_check` that the
    sympy verification of that record (`python-a4-report.json`, check
    `json_exponential_history`) and the lead (check `einstein_exponential_source_alpha1`)
    passed, and checks the texts against our Einstein tensor. It also compares with the
    record of the corrected metric, which lists the same source on the canonical history
    $A = 1$ as functions of $x_4$ (`Revision/metric_warped/results/warped-metric.json`,
    key `history_source.einstein_A1_beta43`). The sum
    $\kappa(\rho + p_0) = -(3k + 4A^2)H^2$ is negative for every $A$. Ordinary matter
    (dust, radiation, a gas) has $\rho + p \ge 0$ in every direction (the **null energy
    condition**), so within Einstein's equations the source that this history requires
    is not ordinary matter; a later chapter discusses this, also for the field equations
    with the additional Lovelock terms. Here we only check that the records and our
    curvature agree.
    """),
    code(r'''
    A4_EQUATIONS = "Revision/field_equations_a4/a4-equations.json"
    a4_equations = json.loads(repository_file(A4_EQUATIONS).read_text(encoding="utf-8"))
    required = a4_equations["exponentialHistory"]["requiredSource"]  # any couplings
    kappa = sp.symbols("kappa", positive=True)  # the constant of Einstein's equations
    Lam = sp.symbols("Lam", real=True)  # the cosmological constant Lambda
    alpha1, alpha2, alpha3, be = sp.symbols("alpha1 alpha2 alpha3 be", real=True)
    source_names = {"AA": A, "H": H, "kappa": kappa, "Lam": Lam, "kk": k_sym, "be": be,
                    "alpha1": alpha1, "alpha2": alpha2, "alpha3": alpha3}
    EINSTEIN = {alpha1: 1, alpha2: 0, alpha3: 0, be: BETA}  # Einstein, beta = 4/3


    def source(key):
        """The record's text required[key] (Mathematica notation) as sympy, with the
        Einstein couplings and beta = 4/3 put in."""
        text = required[key]["input"].replace("^", "**")
        return sp.expand(parse_expr(text, local_dict=source_names).subs(EINSTEIN))


    rho_record, p0_record = source("rho"), source("p0")
    p3_record, pt_record = source("p3"), source("pt")
    say(f"record: kappa rho = {sp.expand(kappa * rho_record)}")
    say(f"record: kappa (p3, p_t, p0) = ({sp.expand(kappa * p3_record)}, "
        f"{sp.expand(kappa * pt_record)}, {sp.expand(kappa * p0_record)})")
    record_check(A4_REPORT, "json_exponential_history")  # stops if not passed
    record_check(LEAD, "einstein_exponential_source_alpha1")
    check(sp.expand(kappa * rho_record - (-G_A[4] - Lam)) == 0,
          "kappa rho of the record equals -G^x4_x4 - Lambda",
          record=f"{A4_EQUATIONS}, exponentialHistory.requiredSource.rho (and "
                 "python-a4-report.json, check json_exponential_history)")
    check(all(sp.expand(kappa * p - (G_A[k] + Lam)) == 0
              for p, k in ((p3_record, 1), (pt_record, 5), (p0_record, 0)))
          and sp.expand(pt_record - p0_record) == 0,
          "kappa p3, kappa p_t, kappa p0 of the record equal G^x1_x1, G^x5_x5, G^x0_x0 "
          "plus Lambda, and p_t = p0",
          record=f"{A4_EQUATIONS}, exponentialHistory.requiredSource.p3, pt, p0")
    history_source = json.loads(repository_file(
        "Revision/metric_warped/results/warped-metric.json").read_text(
        encoding="utf-8"))["history_source"]["einstein_A1_beta43"]
    on_canonical = {A: 1, k_sym: sp.exp(2 * H * x4 / 3)}  # k = e^(2 H x4/3) for A = 1
    canonical_ok = all(sp.simplify(parse_expr(history_source[key], local_dict={
        "H": H, "x4": x4, "exp": sp.exp}) - G_A[k].subs(on_canonical)) == 0
        for key, k in (("-rho", 4), ("p3", 1), ("p0", 0), ("p_t", 5)))
    check(canonical_ok
          and sp.expand(kappa * (rho_record + p0_record)
                        + (3 * k_sym + 4 * A ** 2) * H ** 2) == 0,
          "the record of the corrected metric gives the same source for A = 1, and "
          "kappa (rho + p0) = -(3k + 4 A^2) H^2 < 0",
          record="Revision/metric_warped/results/warped-metric.json, "
                 "history_source.einstein_A1_beta43")
    '''),
    md(r"""
    ## 14. A negative control: the withdrawn metric of 2026-10-14

    A check that cannot fail teaches nothing. Section 11 found that every off-diagonal
    component of the Einstein tensor of the corrected metric vanishes. To see that the
    same code does find off-diagonal components where they exist, the next cell
    computes the curvature of the metric of 2026-10-14, which the corrected metric
    replaced and which is WITHDRAWN (it is used here only as this dated control): the
    hidden entry $\cot^2 z$ without the factor $f^2$, and the factor $\sin^{1/3} z$ in
    the three 3-space entries as well as in the three extra-time entries,
    $g = \mathrm{diag}(\cot^2 z, e^{2a_4}\sin^{1/3}z\ (\times 3), -1,
    -b_4 e^{-2a_4}\sin^{1/3}z\ (\times 3))$, on the half cell $0 < z < \pi/2$ on which it
    was used (there $\sin z > 0$ and $\sin^{1/3} z$ is the ordinary cube root). The cell
    prints the off-diagonal Einstein components that appear and checks that they are
    exactly the pair $G^{x_4}{}_{x_0} = \tfrac32 H\cot z\, b_4'/b_4$ and
    $G^{x_0}{}_{x_4}$, as the record of the corrected metric states
    (`Revision/metric_warped/results/warped-metric.json`, key
    `metric_of_2026_10_14_offdiagonal`, written with `bd1` for $b_4'$, `bb` for $b_4$,
    `cv` for $\cos z$ and `sv` for $\sin z$; check `record_metric_offdiagonal_reproduced`
    of its sympy report). A source that is diagonal, as every source of this book is,
    cannot match such a component unless $b_4' = 0$; this is why the metric was
    corrected.
    """),
    code(r'''
    cube_root = sp.sin(6 * H * x0) ** sp.Rational(1, 3)  # sin(z)^(1/3), sin z > 0 here
    g_withdrawn = sp.diag(sp.cot(6 * H * x0) ** 2,
                          *[sp.exp(2 * a4) * cube_root] * 3, -1,
                          *[-b4 * sp.exp(-2 * a4) * cube_root] * 3)
    Gamma_old = christoffel(g_withdrawn, X)
    R_old = raise_second(riemann(Gamma_old, X), g_withdrawn)
    Ric_old = ricci(R_old, 8)
    G_old = (Ric_old - Ric_old.trace() / 2 * sp.eye(8)).applyfunc(tidy)
    off = {(i, j): plain(G_old[i, j]) for i in range(8) for j in range(8)
           if i != j and G_old[i, j] != 0}
    for (i, j), value in sorted(off.items()):
        say(f"  withdrawn metric: G^{NAMES[i]}_{NAMES[j]} = {value}")
    WARPED = "Revision/metric_warped/results/warped-metric.json"
    old_record = json.loads(repository_file(WARPED).read_text(encoding="utf-8"))
    old_text = old_record["metric_of_2026_10_14_offdiagonal"]["E1^x4_x0"]
    say(f"record (metric of 2026-10-14): E1^x4_x0 = {old_text}")
    old_value = parse_expr(old_text, local_dict={
        "H": H, "bd1": b4p, "bb": b4v, "cv": sp.cos(6 * H * x0), "sv": sp.sin(6 * H * x0)})
    record_check(WARPED_REPORT, "record_metric_offdiagonal_reproduced")
    check(sorted(off) == [(0, 4), (4, 0)]
          and vanishes(symbolic(G_old[4, 0]) - old_value)
          and vanishes(symbolic(G_old[4, 0]) - sp.Rational(3, 2) * H
                       * sp.cot(6 * H * x0) * b4p / b4v),
          "negative control: the withdrawn metric has G^x4_x0 = (3/2) H cot z b4'/b4 "
          "and G^x0_x4 off the diagonal",
          record=f"{WARPED}, metric_of_2026_10_14_offdiagonal (and "
                 "python-warped-metric-report.json, check "
                 "record_metric_offdiagonal_reproduced)")
    '''),
    md(r"""
    ## 15. The last check

    The last cell checks that the seven figure files exist in the folder
    Revision/textbook/figures and prints the number of checks that passed.
    """),
    code(r'''
    figure_names = ["christoffel_heat_maps", "christoffel_versus_z",
                    "finite_differences", "plane_curvatures",
                    "riemann_and_kretschmann_z", "scalars_versus_a", "einstein_tensor"]
    files = [output_file(f"{FIGURE_FOLDER}/03b_{k}_{n}.png")
             for k, n in enumerate(figure_names, 1)]
    check(all(path.is_file() for path in files), "all seven figure files exist")
    all_checks_passed()
    '''),
    md(r"""
    ## 16. What this notebook showed

    - From the corrected metric exactly as the Revision record stores it, with general
      $a_4(x_4)$ and $b_4(x_4)$ and for every real $z$, sympy computed 31 non-zero
      Christoffel symbols (21 with $b \le c$), 112 non-zero Riemann components
      $R^{ab}{}_{cd}$ with 10 different values, the Ricci tensor, the Ricci scalar
      ($R = 8a_4'^2 - 2a_4'' - 8a_4'u + 5u^2 + 4v - 12H^2k$ with $u = b_4'/b_4$,
      $v = u'$, $k = e^{2a_4}/b_4$) and the Einstein tensor; every component agrees
      exactly with the Revision record of the Rust program `lovelock_gkd` (PROVED by
      exact algebra, here and in the record); at the five test points of the
      independent Revision verification, one in each quarter of the period, all 262
      recorded components agree with ours to more than 25 significant digits. Twice our
      Ricci scalar equals the first Lovelock scalar $L_{(1)}$ of the record of the field
      equations of $a_4$ and $b_4$.
    - The Christoffel symbols were confirmed a second way, by finite differences, with
      an error that falls like $h^2$.
    - The lines along $x_4$ are geodesics: observers at rest fall freely and $x_4$ is
      their proper time.
    - The Riemann tensor has all the symmetries of a Riemann tensor and satisfies the
      first Bianchi identity; every non-zero component is the curvature of one of the 28
      coordinate planes, and none depends on $z$: 3-space with 3-space $a_4'^2$,
      3-space with $x_4$ $a_4'^2 + a_4''$, 3-space with the block $a_4'\alpha_t$, the
      block with $x_4$ $\alpha_t^2 + \alpha_t'$, inside the block $\alpha_t^2 - H^2k$
      ($\alpha_t = -a_4' + b_4'/(2b_4)$); the hidden direction behaves exactly like an
      extra time. For the planes with $x_4$ the curvature is the relative acceleration
      of neighbouring observers at rest.
    - The Einstein tensor is diagonal (all 56 off-diagonal components vanish), satisfies
      the contracted Bianchi identity, has no $x_0$ dependence, equal 3-space components
      and $G^{x_0}{}_{x_0} = G^{x_5}{}_{x_5}$; the member $a_4 = 0$,
      $b_4 = H^2(x_4 - c)^2$ is flat.
    - The Kretschmann scalar is $4\sum_{\rm planes}\sigma^2$; it does not depend on $z$,
      although the Christoffel symbols do, and vanishes only on the flat member.
    - Along the deflating history $a_4 = AHx_4$, $b_4 = e^{4AHx_4/3}$ the curvature
      scalars are polynomials in $A$ and $k = e^{2a_4/3}$, even in $A$, for example
      $R = (56A^2/9 - 12k)H^2$; for the canonical history of the Revision record
      ($A = 1$, $H = 1$) at the first slice: $R = -52/9$ and the diagonal of $G$ is
      $(-2/3, 41/9, 41/9, 41/9, 19/3, -2/3, -2/3, -2/3)$ (units $H^2$); along the history
      every component grows with $k$.
    - Through Einstein's equations this Einstein tensor is exactly the source that the
      Revision records list for the exponential history: $\kappa\rho = -(6k + A^2/3)H^2
      - \Lambda$, $p_0 = p_t$, no off-diagonal component, and
      $\kappa(\rho + p_0) = -(3k + 4A^2)H^2 < 0$.
    - Negative control: the withdrawn metric of 2026-10-14 has the off-diagonal pair
      $G^{x_4}{}_{x_0} = \tfrac32 H\cot z\, b_4'/b_4$ and $G^{x_0}{}_{x_4}$, as the record
      of the corrected metric states; the corrected metric has none.
    - ASSUMED for the plots and the evaluation along the history only: the history
      $a_4 = AHx_4$ with $A > 0$ and $b_4 = b_4(0)\,e^{4AHx_4/3}$ with $b_4(0) = 1$ (a
      prescribed background, not solved for); every formula with general $a_4(x_4)$ and
      $b_4(x_4)$ is exact. Nothing is computed at the degenerate points
      $\sin z \cos z = 0$.
    """),
]

if __name__ == "__main__":
    raise SystemExit(run_builder(__file__))
