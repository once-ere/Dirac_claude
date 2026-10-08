#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
"""Builder of Notebook 03b, "The curvature of the author's metric" (textbook
"Universes in Pairs").

The notebook Revision/textbook/notebooks/03b_curvature.ipynb is BUILT from this file by
Revision/textbook/tools/nbkit.py (never edit the .ipynb by hand):

    python Revision/textbook/tools/nbkit.py build \
        Revision/textbook/notebooks/src/03b_curvature.py --date YYYY-MM-DD
    python Revision/textbook/tools/nbkit.py check \
        Revision/textbook/notebooks/src/03b_curvature.py

Physics source: Revision/SPEC.md section 1 (the metric) and the curvature record of the
Rust program lovelock_gkd (Revision/gkd_lovelock/results/curvature.json), its
independent sympy verification (python-lovelock-report.json), its own checks
(lovelock-report.json) and the lead's independent checks of the Einstein tensor
(Revision/lead_checks/reports/einstein-gauss-bonnet-a4.json), and the record of the
field equations of a4 (Revision/field_equations_a4/a4-equations.json, linearMember, and
its sympy verification reports/python-a4-report.json).  The notebook computes everything
again with sympy and asserts agreement with every record component.
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

FACTS = {
    "id": "03b",
    "name": "03b_curvature",
    "title": "The curvature of the author's metric: Christoffel, Riemann, Ricci, "
             "Einstein, Kretschmann",
    "purpose": (
        "It computes with sympy, from the metric exactly as the author typed it and with "
        "a general function a4(x4), all 512 Christoffel symbols, the Riemann tensor, the "
        "Ricci tensor, the Ricci scalar, the Einstein tensor and the Kretschmann scalar; "
        "it compares every component with the Revision record of the Rust program "
        "lovelock_gkd (exactly, and numerically at the five test points of the "
        "independent Revision verification), checks the symmetries of the Riemann "
        "tensor, the first and the contracted Bianchi identities, the Christoffel "
        "symbols by finite differences, and a negative control with inflating extra "
        "times; and it draws the Christoffel symbols, the curvature of every coordinate "
        "plane, the components and the curvature scalars versus z and versus the "
        "expansion rate, and the Einstein tensor; along the deflating history "
        "a4 = A H x4 it reproduces the source that the Einstein equations require in "
        "the Revision record of the field equations of a4. It shows that for the "
        "planes that contain the time x4 the plane curvature is the relative "
        "acceleration of neighbouring observers at rest. Every check of a Revision "
        "report that a PASS line names is opened and asserted to exist and to have "
        "passed."
    ),
    "records": [
        [CURV, "every non-zero Christoffel symbol, Riemann component, Ricci and Einstein "
               "component and the Ricci scalar of the metric, written by the Rust program "
               "lovelock_gkd"],
        [PYREP, "the independent sympy verification of those components (checks "
                "rust_christoffels_agree, rust_riemann_agrees, "
                "rust_ricci_einstein_scalar_agree, riemann_antisymmetry_and_pair_"
                "symmetry, mixed_riemann_free_of_warp_and_exponential, L1_equals_2R) "
                "and its five random test points"],
        [RUSTREP, "the checks riemann_antisymmetry (with its count of 156 nonzero "
                  "entries), riemann_first_bianchi, mixed_riemann_free_of_sin_third, "
                  "k1_equals_minus_4_einstein, k1_divergence_free and the numerical test "
                  "point of k1_brute_force_numeric"],
        [LEAD, "the lead checks einstein_x8_independent, einstein_off_diagonal_zero, "
               "einstein_isotropy and no_vacuum_for_H_positive"],
        [A4EQ, "the record of the field equations of a4: for the linear history "
               "a4 = A H x4 the energy density and the pressure that the Einstein "
               "equations require (linearMember: rhoEinstein, pEinstein, "
               "rhoPlusPEinstein)"],
        [A4REP, "its sympy verification: the check L1_equals_gkd_branch (the first "
                "Lovelock scalar, twice the Ricci scalar) and the check json_linear_member"],
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
        "ALL 40 CHECKS PASSED (notebook 03b)",
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

    This notebook computes the **curvature** of the author's metric of the primordial
    gravitational field, exactly, with sympy, for a general metric function $a_4(x_4)$.
    It

    - reads the metric exactly as the author typed it (from the Revision record
      `Revision/gkd_lovelock/results/curvature.json`);
    - computes all $8^3 = 512$ **Christoffel symbols** $\Gamma^a{}_{bc}$, finds the 37
      that are not zero, checks them against the record of the Rust program
      `lovelock_gkd`, draws them as heat maps and as functions of $z$, and checks them a
      second, independent way by **finite differences** (a numerical derivative);
    - shows that the lines along the time $x_4$ are **geodesics** (free fall) with
      proper time $x_4$;
    - computes the **Riemann tensor** $R^a{}_{bcd}$ and its form $R^{ab}{}_{cd}$ with two
      upper indices, finds its 156 non-zero components, checks its symmetries and the
      first Bianchi identity, and compares all 156 with the record;
    - computes the curvature $\sigma(a, b)$ of each of the 28 coordinate planes and
      shows that for the planes with the time $x_4$ it is the relative acceleration of
      two neighbouring observers at rest;
    - computes the **Ricci tensor**, the **Ricci scalar** and the **Einstein tensor**,
      compares them with the record and the lead checks, and checks the contracted
      Bianchi identity $\sum_\mu \nabla_\mu G^\mu{}_\nu = 0$;
    - computes the **Kretschmann scalar** $K = R^{ab}{}_{cd} R^{cd}{}_{ab}$, shows that it
      does not depend on $z$ although single components do, and that it is never zero
      for $H > 0$;
    - evaluates everything along the **deflating history** $a_4 = A H x_4$ ($A > 0$) and
      checks that minus the time component and the space component of the Einstein
      tensor are exactly the energy density and the pressure that the Revision record
      of the field equations of $a_4$ lists for this history;
    - repeats the curvature for a **negative control** in which the extra times inflate
      instead of deflating, and shows what then changes;
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
      $x_1, \dots, x_8$; an upper and a lower index are positions in a table of numbers;
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
      sources of this book its diagonal is $T = \mathrm{diag}(p_3, p_3, p_3, -\rho, p_t,
      p_t, p_t, p_8)$: the **energy density** $\rho$ (energy per unit volume) and the
      **pressures** $p_3$ of 3-space, $p_t$ of the extra times and $p_8$ of the hidden
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
      value of $a_4$; `z` stands for $6 H x_8$.
    """),
    md(r"""
    ## 4. The physical and mathematical situation

    The metric of the author is diagonal,

    $$g = \mathrm{diag}\bigl(e^{2a_4}\sin^{1/3}z\ (\times 3),\ -1,\
    -e^{-2a_4}\sin^{1/3}z\ (\times 3),\ \cot^2 z\bigr), \qquad z = 6 H x_8,$$

    in the order $x_1, \dots, x_8$, with the constant $H > 0$ and the metric function
    $a_4(x_4)$. It depends on two coordinates only, $x_4$ (through $a_4$) and $x_8$
    (through $z$). Every derivative along $x_1, x_2, x_3, x_5, x_6, x_7$ is therefore
    zero, which is why most of the $512$ Christoffel symbols and most of the $4096$
    Riemann components vanish.

    Curvature is computed in three steps, each from the previous one: the Christoffel
    symbols need the first derivatives of the metric; the Riemann tensor needs the
    first derivatives of the Christoffel symbols and their products (so the second
    derivatives of the metric, and $a_4''$ appears); the Ricci tensor, the Ricci scalar
    and the Einstein tensor are sums of Riemann components. The Revision record
    computed all of this with an exact Rust program (`lovelock_gkd`); an independent
    sympy program checked every component, and the lead checks recomputed the Einstein
    tensor with their own sympy code. This notebook does it once more, in small steps, and compares every
    single component.

    Nothing here involves the matter fields yet: these are exact properties of the given
    metric. The field equations, which connect the Einstein tensor to the energy and the
    pressures of the fields, are the subject of a later chapter. For the plots the
    notebook uses $H = 1$ and the deflating history $a_4 = A H x_4$ of the Revision
    Kohn-Sham work (so $a_4' = A H$ and $a_4'' = 0$, with $A = 1$ the canonical value):
    a PRESCRIBED BACKGROUND, assumed here and not obtained by solving the field
    equations.
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
    eight coordinates, $H > 0$, the unknown function $a_4(x_4)$, and the printing names
    `a4p`, `a4pp`, `a4v` and `z`. The function `plain` rewrites an expression with these
    printing names; the function `symbolic` does the same but keeps $x_8$ (the record
    writes its components with $x_8$). It also names the two reports of the Revision
    curvature computation and defines the function `record_check(report_file,
    check_name, detail_part)`, the same as in Notebook 03a: it opens a Revision report,
    finds the check with that name, and stops the notebook with an error unless the
    check is there and passed (and, if `detail_part` is given, its detail contains that
    text). Every PASS line below that names a check of a Revision report calls it
    first, so that a renamed, missing or failing check in the record is caught.
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


    x1, x2, x3, x4, x5, x6, x7, x8 = sp.symbols("x1:9", real=True)
    X = [x1, x2, x3, x4, x5, x6, x7, x8]  # the coordinates, counted 0 to 7 in Python
    NAMES = ["x1", "x2", "x3", "x4", "x5", "x6", "x7", "x8"]
    H = sp.symbols("H", positive=True)  # the constant of the author
    a4 = sp.Function("a4")(x4)  # the metric function, unknown
    a4p, a4pp, a4v = sp.symbols("a4p a4pp a4v", real=True)  # a4 prime, a4 two primes, a4
    z = sp.symbols("z", positive=True)  # z = 6 H x8, for printing


    def symbolic(expression):
        """Write the derivatives of a4 as a4p and a4pp and the value a4(x4) as a4v."""
        expression = expression.subs(sp.Derivative(a4, (x4, 2)), a4pp)  # second first
        return expression.subs(sp.Derivative(a4, x4), a4p).subs(a4, a4v)


    def plain(expression):
        """As symbolic, and 6 H x8 written as z."""
        return symbolic(expression).subs(x8, z / (6 * H))


    say("Record read; symbols x1 ... x8, H, a4(x4), a4p, a4pp, a4v and z defined.")
    '''),
    md(r"""
    The next cell turns the author's text of the metric into a sympy matrix, with the
    same translation rules as Notebook 03a (Mathematica's `exp^` becomes `E^`, square
    brackets of functions become round brackets, curly brackets of lists become square
    brackets, `^` becomes `**`, and a blank between factors means times), and prints
    the diagonal.
    """),
    code(r'''
    text = record["metricAsGiven"]  # the metric exactly as the author typed it
    text = text.replace("exp^", "E^").replace("a4[x4]", "a4")
    text = text.replace("Sin[6 H x8]", "sin(6 H x8)").replace("Cot[6 H x8]", "cot(6 H x8)")
    text = text.replace("{", "[").replace("}", "]").replace("^", "**")
    metric_names = {"E": sp.E, "a4": a4, "H": H, "x8": x8, "sin": sp.sin, "cot": sp.cot}
    g = sp.Matrix(parse_expr(text, local_dict=metric_names, transformations=(
        standard_transformations + (implicit_multiplication,))))
    for k in range(8):
        say(f"  g[{NAMES[k]}, {NAMES[k]}] = {plain(g[k, k])}")
    check(all(g[i, j] == 0 for i in range(8) for j in range(8) if i != j),
          "the metric read from the text of the author is diagonal")
    '''),
    md(r"""
    The record writes its components in Mathematica notation, for example
    `Derivative[1][a4][x4]*E^(2*a4[x4])*Sin[6*H*x8]^(1/3)`. The next cell defines the
    function `from_mathematica` that translates such a text into sympy:
    `Derivative[1][a4][x4]` ($a_4'$) becomes `a4p`, `Derivative[2][a4][x4]` becomes
    `a4pp`, `a4[x4]` becomes `a4v`, the sine and the cotangent get round brackets, and
    `^` becomes `**`. If any square bracket is left, the translation is incomplete and
    the function stops with an error, so a silent mistranslation is impossible.

    The cell also defines three helpers. `tidy(expression)` simplifies an expression:
    it writes $6Hx_8$ as $z$, simplifies it once as it is and once after writing
    $\sin 2z$ as $2\sin z\cos z$ (`expand_trig`), and keeps the shorter of the two
    results (sympy sometimes reaches the simplest form only one way: it writes, for
    example, $-6H/(\sin z\cos z)$ as $-12H/\sin(2z)$, the same number because
    $\sin 2z = 2\sin z\cos z$, and a sum such as $6H\cot z - 12H/\sin 2z + 6H\tan z$ is
    recognised as $0$ only after the rewriting). `vanishes(expression)` is true when
    `tidy` gives $0$, and `same(mine, theirs)` is true when the difference of our
    expression and the record's vanishes.
    """),
    code(r'''
    record_names = {"a4p": a4p, "a4pp": a4pp, "a4v": a4v, "H": H, "x8": x8, "E": sp.E,
                    "sin": sp.sin, "cot": sp.cot}


    def from_mathematica(entry_text):
        """A component of the record (Mathematica notation) as a sympy expression."""
        t = entry_text.replace("Derivative[1][a4][x4]", "a4p")
        t = t.replace("Derivative[2][a4][x4]", "a4pp").replace("a4[x4]", "a4v")
        t = t.replace("Sin[6*H*x8]", "sin(6*H*x8)").replace("Cot[6*H*x8]", "cot(6*H*x8)")
        t = t.replace("^", "**")
        if "[" in t or "]" in t:
            raise ValueError(f"cannot translate {entry_text}")
        return parse_expr(t, local_dict=record_names)


    def tidy(expression):
        """Simplify an expression.  It writes 6 H x8 as z (so that 12 H x8 becomes 2z),
        simplifies it twice, once as it is and once after writing sin(2z) as
        2 sin(z) cos(z) (expand_trig), keeps the shorter result (count_ops counts the
        operations), and writes z as 6 H x8 again."""
        expression = sp.sympify(expression).subs(x8, z / (6 * H))
        first = sp.simplify(expression)
        second = sp.simplify(sp.expand_trig(expression))
        best = second if sp.count_ops(second) < sp.count_ops(first) else first
        return best.subs(z, 6 * H * x8)


    def vanishes(expression):
        """True when the expression simplifies to zero."""
        return tidy(expression) == 0


    def same(mine, theirs):
        """True when mine (with the function a4) equals theirs (record symbols)."""
        return vanishes(symbolic(mine) - theirs)


    example = record["christoffelNonzero_b_le_c"][6]["value"]
    say(f"example of a record entry: {example}")
    say(f"translated: {from_mathematica(example)}")
    '''),
    md(r"""
    ## 6. The Christoffel symbols

    The Christoffel symbols of the metric are

    $$\Gamma^a{}_{bc} = \tfrac12 \sum_{d=1}^{8} g^{ad}\bigl(\partial_b g_{dc} +
    \partial_c g_{db} - \partial_d g_{bc}\bigr).$$

    The next cell defines the function `christoffel(metric, coordinates)`, which applies
    this formula literally to every one of the $8 \times 8 \times 8 = 512$ index
    combinations (it does not use the symmetry in $b$ and $c$, so that the symmetry can
    be checked afterwards), simplifies each result, and returns the table
    `Gamma[a][b][c]`. Then it computes the symbols of the author's metric and counts
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
    The next cell prints the 25 non-zero symbols with $b \le c$ (the others follow by the
    symmetry) and compares them with the list `christoffelNonzero_b_le_c` of the record:
    first that the two lists name the same 25 index combinations, then that each value
    agrees exactly. In the record the keys `a`, `b`, `c` are the indices of
    $\Gamma^a{}_{bc}$. sympy chooses its own way of writing some symbols: $H\cot z$
    appears as `H/tan(z)`, $-He^{2a_4}\sin^{1/3}z\,\tan z$ as
    `-H*exp(2*a4v)*sin(z)**(4/3)/cos(z)` (because $\sin^{1/3}z\,\tan z =
    \sin^{4/3}z/\cos z$), and $\Gamma^{x_8}{}_{x_8x_8} = -6H/(\sin z\cos z)$ as
    `-12*H/sin(2*z)`.
    """),
    code(r'''
    for a, b, c in upper_half:
        say(f"  Gamma^{NAMES[a]}_({NAMES[b]} {NAMES[c]}) = {plain(Gamma[a][b][c])}")
    record_gamma = {(NAMES.index(e["a"]), NAMES.index(e["b"]), NAMES.index(e["c"])):
                    from_mathematica(e["value"])
                    for e in record["christoffelNonzero_b_le_c"]}
    check(sorted(record_gamma) == upper_half and len(upper_half) == 25,
          "the same 25 non-zero Christoffel symbols as the record")
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
    $a_4$, $a_4'$ and $H$ (`sp.lambdify`). It then draws the eight $8 \times 8$ tables
    $\Gamma^{x_k}{}_{bc}$ at the point $z = \pi/4$ with $H = 1$, $a_4 = 0.5$, $a_4' = 1$
    as heat maps. The colour scale is **symmetric-logarithmic**: above $0.1$ in size,
    equal steps of colour stand for equal factors of size (below $0.1$ the scale is
    ordinary), so that small and large symbols are both visible; grey is zero, red
    positive, blue negative.
    """),
    code(r'''
    from matplotlib.colors import LinearSegmentedColormap, SymLogNorm

    BLUE, ORANGE, AQUA, YELLOW = "#2a78d6", "#eb6834", "#1baf7a", "#eda100"
    MAGENTA, GREEN, VIOLET, RED = "#e87ba4", "#008300", "#4a3aa7", "#e34948"
    DIVERGING = LinearSegmentedColormap.from_list("blue_grey_red", [BLUE, "#f0efec", RED])
    LABELS = [f"$x_{k}$" for k in range(1, 9)]
    ARGS = (z, a4v, a4p, H)  # the arguments of the numerical functions


    def numeric(expression):
        """A numerical function f(z, a4v, a4p, H) of an expression."""
        return sp.lambdify(ARGS, plain(expression), "numpy")


    gamma_functions = {(a, b, c): numeric(Gamma[a][b][c]) for a, b, c in nonzero}
    POINT = (np.pi / 4, 0.5, 1.0, 1.0)  # z, a4, a4p, H: the canonical slice a4 = 0.5
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
        ax.set_title(f"$\\Gamma^{{x_{a + 1}}}{{}}_{{bc}}$", fontsize=10)
        ax.set_xticks(range(8), [str(k) for k in range(1, 9)], fontsize=7)
        ax.set_yticks(range(8), [str(k) for k in range(1, 9)], fontsize=7)
        ax.grid(False)
    fig.colorbar(image, ax=axes, shrink=0.8, label="value (unit $H$)")
    fig.suptitle("Christoffel symbols at $z = \\pi/4$, $a_4 = 0.5$, "
                 "$a_4^{\\prime} = 1$, $H = 1$ (row $b$, column $c$)")
    save_figure(fig, "christoffel_heat_maps",
                "The 512 Christoffel symbols $\\Gamma^{a}{}_{bc}$ of the author's metric "
                "at the point $z = \\pi/4$ on the slice $a_4 = 0.5$ of the history "
                "$a_4 = x_4$ ($a_4^{\\prime} = 1$, $H = 1$), as eight heat maps, one "
                "for each upper index $a = x_1, \\dots, x_8$; in each map the row is $b$ "
                "and the column is $c$ (numbers $1$ to $8$ for $x_1$ to $x_8$), the "
                "colour is the value on a symmetric logarithmic scale (grey zero, red "
                "positive, blue negative) and every non-zero value is printed. Only 37 "
                "of the 512 squares are coloured, each map is symmetric about its "
                "diagonal, and every non-zero symbol has at least one index equal to "
                "$x_4$ or $x_8$, the two coordinates on which the metric depends.")
    check(np.allclose(tables, tables.transpose(0, 2, 1))
          and all(3 in key or 7 in key for key in nonzero),
          "the tables are symmetric in b, c; every non-zero symbol has an index x4 or x8")
    '''),
    md(r"""
    The symbols with an index $x_8$ depend on $z$. The next cell draws the size of five
    typical symbols across the patch on a logarithmic axis (for $a_4 = 0.5$,
    $a_4' = 1$, $H = 1$): $\Gamma^{x_1}{}_{x_1 x_8} = H\cot z$ and
    $\Gamma^{x_8}{}_{x_8 x_8}$ grow without bound at the tip $z \to 0$;
    $\Gamma^{x_8}{}_{x_1 x_1}$, $\Gamma^{x_8}{}_{x_8 x_8}$ and
    $\Gamma^{x_8}{}_{x_5 x_5}$ grow without bound at the patch end $z \to \pi/2$;
    $\Gamma^{x_1}{}_{x_1 x_4} = a_4'$ does not depend on $z$. Large Christoffel symbols
    are a property of the coordinates; whether the geometry itself is extreme is decided
    by invariants such as the Kretschmann scalar of section 12.
    """),
    code(r'''
    z_line = np.linspace(0.01, np.pi / 2 - 0.01, 500)
    chosen = [((0, 0, 7), RED, "-", "$\\Gamma^{x_1}{}_{x_1 x_8}$"),
              ((7, 7, 7), VIOLET, "--", "$\\Gamma^{x_8}{}_{x_8 x_8}$"),
              ((7, 0, 0), ORANGE, "-.", "$\\Gamma^{x_8}{}_{x_1 x_1}$"),
              ((7, 4, 4), BLUE, ":", "$\\Gamma^{x_8}{}_{x_5 x_5}$"),
              ((0, 0, 3), AQUA, "-", "$\\Gamma^{x_1}{}_{x_1 x_4}$")]
    fig, ax = plt.subplots()
    for index, colour, style, label in chosen:
        values = np.broadcast_to(gamma_functions[index](z_line, 0.5, 1.0, 1.0),
                                 z_line.shape)
        sign = "+" if values[len(values) // 2] > 0 else "minus"
        ax.plot(z_line, np.abs(values), color=colour, ls=style, lw=1.8,
                label=f"{label} (sign {sign})")
    ax.set_yscale("log")
    ax.set_xlabel("$z = 6 H x_8$ (radians)")
    ax.set_ylabel("absolute value of the symbol (unit $H$)")
    ax.set_title("Christoffel symbols across the patch "
                 "($a_4 = 0.5$, $a_4^{\\prime} = 1$, $H = 1$)")
    ax.set_ylim(1e-5, 3e3)  # room below the curves for the legend
    ax.legend(fontsize=8, loc="lower center", ncol=2)
    save_figure(fig, "christoffel_versus_z",
                "The absolute values of five Christoffel symbols of the author's metric "
                "across the patch $0 < z < \\pi/2$, for $a_4 = 0.5$, $a_4^{\\prime} = 1$, "
                "$H = 1$, on a logarithmic vertical axis; horizontal axis "
                "$z = 6Hx_8$ in radians, vertical axis the absolute value in units of "
                "$H$; the legend gives each sign. $\\Gamma^{x_1}{}_{x_1x_8} = H\\cot z$ "
                "falls from the tip to the patch end, $\\Gamma^{x_8}{}_{x_8x_8}$ is "
                "large at both ends, $\\Gamma^{x_8}{}_{x_1x_1}$ and "
                "$\\Gamma^{x_8}{}_{x_5x_5}$ grow towards the patch end, and "
                "$\\Gamma^{x_1}{}_{x_1x_4} = a_4^{\\prime} = 1$ is the same everywhere.")
    check(abs(gamma_functions[(0, 0, 7)](np.pi / 4, 0.5, 1.0, 1.0) - 1.0) < 1e-14,
          "Gamma^x1_(x1 x8) = H cot z equals 1 at z = pi/4, H = 1")
    '''),
    md(r"""
    ## 7. A second, independent check: finite differences

    The exact symbols can be checked without any algebra. Take a concrete function
    $a_4(x_4) = 0.17 + 0.61\,x_4 - 0.185\,x_4^2$ (so that at $x_4 = 0$:
    $a_4 = 0.17$, $a_4' = 0.61$, $a_4'' = -0.37$), $H = 0.23$ and the point
    $x_8 = 0.41$: the test point at which the Rust program checked its Lovelock tensors
    by brute force (record `lovelock-report.json`, check `k1_brute_force_numeric`).
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
                  "x8 = 0.41")  # the test point as the record writes it
    check(record_check(RUST_REPORT, "k1_brute_force_numeric", point_text),
          "the test point is the one of the brute-force check of the Rust program")
    H_n, a0, a1, a2, x8_n = 0.23, 0.17, 0.61, -0.37, 0.41  # the test point


    def metric_numbers(x):
        """The metric as an 8 x 8 numpy table at the point x (8 coordinates)."""
        a = a0 + a1 * x[3] + 0.5 * a2 * x[3] ** 2  # a4(x4) with a4(0) = 0.17, ...
        warp_n = np.sin(6 * H_n * x[7]) ** (1 / 3)
        return np.diag([np.exp(2 * a) * warp_n] * 3 + [-1.0]
                       + [-np.exp(-2 * a) * warp_n] * 3
                       + [1 / np.tan(6 * H_n * x[7]) ** 2])


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


    x_point = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, x8_n])
    exact = np.zeros((8, 8, 8))
    for (a, b, c), f in gamma_functions.items():
        exact[a, b, c] = f(6 * H_n * x8_n, a0, a1, H_n)
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
                "$a_4^{\\prime} = 0.61$, $a_4^{\\prime\\prime} = -0.37$, $x_8 = 0.41$ of "
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

    Consider an observer who stays at fixed $x_1, x_2, x_3, x_5, x_6, x_7, x_8$ while
    $x_4 = \tau$ runs. Then $dx^a/d\tau$ is $1$ for $a = x_4$ and $0$ otherwise, and
    $d^2x^a/d\tau^2 = 0$, so the geodesic equation reduces to
    $\Gamma^a{}_{x_4 x_4} = 0$ for every $a$. Since $g_{44} = -1$, the proper time of
    the observer is $\sqrt{-g_{44}}\, d\tau = d\tau$: $x_4$ is the time shown by the
    observer's clock. The next cell checks that the eight symbols $\Gamma^a{}_{x_4x_4}$
    are zero. It also checks the useful identity $\sum_a \Gamma^a{}_{ab} =
    \partial_b \ln\sqrt{|\det g|}$, with $\sqrt{|\det g|} = \cos z$.
    """),
    code(r'''
    check(all(Gamma[a][3][3] == 0 for a in range(8)),
          "Gamma^a_(x4 x4) = 0: observers at rest fall freely, x4 is their proper time")
    contracted = [vanishes(sum(Gamma[a][a][b] for a in range(8))
                           - sp.diff(sp.log(sp.cos(6 * H * x8)), X[b]))
                  for b in range(8)]
    check(all(contracted),
          "sum over a of Gamma^a_(a b) equals the derivative of ln cos z")
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
    record_check(RUST_REPORT, "riemann_antisymmetry", "156 nonzero entries")
    check(len(R_mixed) == 156, "R^ab_cd has 156 non-zero components, as in the record",
          record="Revision/gkd_lovelock/results/lovelock-report.json, check "
                 "riemann_antisymmetry (156 nonzero entries)")
    '''),
    md(r"""
    The next cell checks the symmetries that every Riemann tensor has, as a test of the
    computation: (1) $R^{ab}{}_{cd} = -R^{ba}{}_{cd} = -R^{ab}{}_{dc}$; (2) with all
    indices lowered, $R_{abcd} = g_{aa} g_{bb} R^{ab}{}_{cd}$ (diagonal metric), the
    pair symmetry $R_{abcd} = R_{cdab}$; (3) the first Bianchi identity
    $R^a{}_{bcd} + R^a{}_{cdb} + R^a{}_{dbc} = 0$ for all $8^4 = 4096$ index lists.
    It also checks that no component $R^{ab}{}_{cd}$ contains the factor
    $\sin^{1/3} z$ of the transverse metric entries (the square $W^2$ of the warp factor
    $W = \sin^{1/6} z$ of Notebook 03a) or the exponential $e^{a_4}$: they cancel when
    one index is raised.
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
    warp_free = all(not symbolic(v).has(a4v) and not any(
        isinstance(p, sp.Pow) and p.base == sp.sin(6 * H * x8) and not p.exp.is_integer
        for p in sp.preorder_traversal(symbolic(v))) for v in R_mixed.values())
    record_check(RUST_REPORT, "mixed_riemann_free_of_sin_third")
    record_check(PYTHON_REPORT, "mixed_riemann_free_of_warp_and_exponential")
    check(warp_free, "no R^ab_cd contains sin(z)^(1/3) or e^(a4): the warp cancels",
          record="Revision/gkd_lovelock/results/lovelock-report.json, check "
                 "mixed_riemann_free_of_sin_third, and python-lovelock-report.json, "
                 "check mixed_riemann_free_of_warp_and_exponential")
    '''),
    md(r"""
    The next cell compares all 156 components with the list `riemannMixedNonzero` of the
    record, in which `up` holds $a, b$ and `down` holds $c, d$ of $R^{ab}{}_{cd}$: first
    that the same 156 index lists occur, then that each value agrees exactly. It then
    groups the 156 components by their value and prints the 14 different values, how
    often each occurs and one example of where.
    """),
    code(r'''
    record_riemann = {}
    for entry in record["riemannMixedNonzero"]:
        key = tuple(NAMES.index(n) for n in entry["up"] + entry["down"])
        record_riemann[key] = from_mathematica(entry["value"])
    check(sorted(record_riemann) == sorted(R_mixed),
          "the same 156 non-zero components R^ab_cd as the record")
    record_check(PYTHON_REPORT, "rust_riemann_agrees")
    check(all(same(R_mixed[k], v) for k, v in record_riemann.items()),
          "every component R^ab_cd equals the record exactly",
          record=f"{CURVATURE_RECORD}, riemannMixedNonzero (and "
                 "python-lovelock-report.json, check rust_riemann_agrees)")
    groups = {}
    for key in sorted(R_mixed):
        groups.setdefault(sp.sstr(plain(R_mixed[key])), []).append(key)
    for value_text in sorted(groups):
        a, b, c, d = groups[value_text][0]
        say(f"  {len(groups[value_text]):2d} x  {value_text:30s}  e.g. "
            f"R^({NAMES[a]} {NAMES[b]})_({NAMES[c]} {NAMES[d]})")
    report("different values among the 156 components", len(groups))
    '''),
    md(r"""
    ## 10. The curvature of every coordinate plane

    For two different coordinates $x_a$ and $x_b$ the number $\sigma(a, b) =
    R^{ab}{}_{ab}$ (no sum) is the curvature of the coordinate plane spanned by them.
    The next cell computes all 28 of them as formulas, prints one plane of each kind,
    and checks the six formulas: 3-space with 3-space and extra time with extra time
    $a_4'^2 - H^2$; 3-space with an extra time $-(a_4'^2 + H^2)$; 3-space with the time
    $x_4$ $a_4'^2 + a_4''$; the time with an extra time $a_4'^2 - a_4''$; a 3-space or
    extra-time direction with the hidden $x_8$ $-H^2$; the time with the hidden $x_8$
    zero. None depends on $z$ or on the value of $a_4$.

    What does the sign mean? Only 6 of the 28 planes are spanned by two space-like
    directions (two of $x_1, x_2, x_3$, or one of them with $x_8$); only for these does
    a positive value mean curved like a sphere and a negative one like a saddle. The
    other 22 planes contain a time-like direction, and there the sign is read from
    free fall. The clearest case: two observers at rest (they fall freely, section 8),
    a small coordinate distance $\Delta x_a$ apart along a transverse direction $x_a$,
    are a proper distance $\xi = h_a\,\Delta x_a$ apart, where $h_a$ is the scale factor;
    the proper time of both is $\tau = x_4$. The cell computes $(d^2\xi/d\tau^2)/\xi =
    (\partial_4^2 h_a)/h_a$ for $x_a = x_1$ (with $h_1 = e^{a_4}\sin^{1/6}z$) and
    $x_a = x_5$ (with $h_5 = e^{-a_4}\sin^{1/6}z$) and checks that it is exactly
    $\sigma(a, x_4)$: $d^2\xi/d\tau^2 = +\sigma(a, x_4)\,\xi$. Along the history
    $a_4 = AHx_4$ both are $A^2H^2 > 0$: a positive curvature, and yet the 3-space
    distance grows like $e^{AH\tau}$ (the extra-time distance shrinks like
    $e^{-AH\tau}$, also with a positive second derivative); on a sphere a positive
    curvature pulls neighbouring paths together, $d^2\xi/ds^2 = -\sigma\,\xi$.

    Then the cell draws the 28 plane curvatures as $8 \times 8$ heat maps along the
    deflating history $a_4 = AHx_4$ ($a_4' = AH$, $a_4'' = 0$, $H = 1$) for the three
    slopes $A = 0.5$, $1$ (the canonical value of the Revision record) and $2$, all
    positive, so that in all three the extra times deflate; the diagonal is left empty.
    The planes inside 3-space and inside the extra times change sign at $A = 1$:
    $a_4'^2 - H^2 = H^2(A^2 - 1)$ is negative for $A < 1$, zero at $A = 1$ and positive
    for $A > 1$.
    """),
    code(r'''
    plane = {(a, b): plain(sp.S(get(R_mixed, (a, b, a, b))))  # sp.S: 0 as a sympy 0
             for a, b in itertools.product(range(8), repeat=2) if a != b}
    expected = {(0, 1): a4p ** 2 - H ** 2, (4, 5): a4p ** 2 - H ** 2,
                (0, 4): -(a4p ** 2 + H ** 2), (0, 3): a4p ** 2 + a4pp,
                (3, 4): a4p ** 2 - a4pp, (0, 7): -H ** 2, (4, 7): -H ** 2, (3, 7): 0}
    for (a, b), formula in expected.items():
        say(f"  plane ({NAMES[a]}, {NAMES[b]}): R^ab_ab = {plane[(a, b)]}")
    check(all(sp.expand(plane[key] - formula) == 0 for key, formula in expected.items())
          and all(not v.has(z) and not v.has(a4v) for v in plane.values()),
          "the plane curvatures have the six formulas and do not depend on z or a4")
    sixth = sp.sin(6 * H * x8) ** sp.Rational(1, 6)  # sin(z)^(1/6)
    apart = {0: sp.exp(a4) * sixth, 4: sp.exp(-a4) * sixth}  # the scale factors h1, h5
    growth = {}  # (d^2 xi/d tau^2)/xi for observers at rest apart along x1 or x5
    for a, h_a in apart.items():  # xi = h_a times a fixed coordinate distance, tau = x4
        growth[a] = sp.expand(plain(sp.simplify(sp.diff(h_a, x4, 2) / h_a)))
        say(f"  at rest, apart along {NAMES[a]}: (d^2 xi/d tau^2)/xi = {growth[a]}")
    check(sp.simplify(apart[0] ** 2 - g[0, 0]) == 0
          and sp.simplify(apart[4] ** 2 + g[4, 4]) == 0
          and all(sp.expand(growth[a] - plane[(a, 3)]) == 0 for a in apart),
          "observers at rest: d^2 xi/d tau^2 = +R^ab_ab xi in the planes (x1, x4) and "
          "(x5, x4)")
    SLOPES = (0.5, 1.0, 2.0)  # three deflating histories, A > 0
    fig, axes = plt.subplots(1, 3, figsize=(14.0, 4.8))  # wide: room for -1.25
    for ax, slope in zip(axes, SLOPES):
        curv = np.full((8, 8), np.nan)  # NaN: an empty square on the diagonal
        for (a, b), value in plane.items():
            curv[a, b] = float(value.subs({a4p: slope, a4pp: 0, H: 1}))
        image = ax.imshow(curv, cmap=DIVERGING, vmin=-5.0, vmax=5.0)
        for a, b in plane:
            ax.text(b, a, f"{curv[a, b]:g}", ha="center", va="center", fontsize=6.5)
        ax.set_xticks(range(8), LABELS, fontsize=8)
        ax.set_yticks(range(8), LABELS, fontsize=8)
        ax.grid(False)
        ax.set_title(f"$A = {slope:g}$")
    fig.colorbar(image, ax=axes, shrink=0.85, label="curvature (unit $H^2$)")
    save_figure(fig, "plane_curvatures",
                "The curvature $R^{ab}{}_{ab}$ (no sum) of the coordinate plane of "
                "$x_a$ (row) and $x_b$ (column), in units of $H^2$, along the deflating "
                "history $a_4 = AHx_4$ ($a_4^{\\prime} = AH$, "
                "$a_4^{\\prime\\prime} = 0$, $H = 1$) for $A = 0.5$ (left), $A = 1$ "
                "(middle, the canonical history of the Revision record) and $A = 2$ "
                "(right); red positive (curved like a sphere), blue negative (curved "
                "like a saddle), grey zero, diagonal empty. The planes inside 3-space "
                "and inside the extra times have $a_4^{\\prime 2} - H^2$ ($-0.75$, $0$, "
                "$3$: the sign changes at $A = 1$); a 3-space direction with an extra "
                "time $-(a_4^{\\prime 2} + H^2)$ ($-1.25$, $-2$, $-5$); the planes with "
                "the time $x_4$ $a_4^{\\prime 2} \\pm a_4^{\\prime\\prime}$ ($0.25$, "
                "$1$, $4$), except the plane of $x_4$ and $x_8$, which is flat; every "
                "other plane with the hidden $x_8$ has $-H^2 = -1$ for every $A$.")
    check([float(plane[(0, 1)].subs({a4p: s, H: 1})) for s in SLOPES] == [-0.75, 0.0, 3.0],
          "the planes inside 3-space: -0.75, 0 and 3 for A = 0.5, 1 and 2")
    '''),
    md(r"""
    ## 11. Ricci tensor, Ricci scalar, Einstein tensor

    The next cell contracts the Riemann tensor: $R^a{}_b = \sum_c R^{ac}{}_{bc}$, then
    $R = \sum_a R^a{}_a$ and $G^a{}_b = R^a{}_b - \tfrac12 \delta^a{}_b R$. It prints the
    diagonal and compares all 64 components of each tensor and the scalar with the
    record (`ricciMixed`, `ricciScalar`, `einsteinMixed`).
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
    G = (Ric - R_scalar / 2 * sp.eye(8)).applyfunc(tidy)
    for k in range(8):
        say(f"  {NAMES[k]}: R^a_a = {sp.sstr(plain(Ric[k, k])):18s} "
            f"G^a_a = {plain(G[k, k])}")
    say(f"Ricci scalar R = {plain(R_scalar)}")
    ricci_ok = all(same(Ric[i, j], from_mathematica(
        record["ricciMixed"][f"{NAMES[i]},{NAMES[j]}"]["mathematica"]))
        for i in range(8) for j in range(8))
    einstein_ok = all(same(G[i, j], from_mathematica(
        record["einsteinMixed"][f"{NAMES[i]},{NAMES[j]}"]["mathematica"]))
        for i in range(8) for j in range(8))
    scalar_ok = same(R_scalar, from_mathematica(record["ricciScalar"]))
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
    check `L1_equals_gkd_branch`, with the name `ad1` for $a_4'$. The next cell reads
    this text, checks that the record marks the check as passed, turns the text after
    the equals sign into a sympy expression, and checks $L_{(1)} = 2R$ with our $R$.
    """),
    code(r'''
    A4_REPORT = "Revision/field_equations_a4/reports/python-a4-report.json"
    a4_report = json.loads(repository_file(A4_REPORT).read_text(encoding="utf-8"))
    # the report's checks form a list of dictionaries; take the one with this name
    L1_entry = next(entry for entry in a4_report["checks"]
                    if entry["name"] == "L1_equals_gkd_branch")
    L1_detail, L1_verdict = L1_entry["detail"], L1_entry["verdict"]
    say(f"record: {L1_detail} ({L1_verdict})")
    L1_text = L1_detail.split("=")[1]  # the text after the equals sign
    L1_record = parse_expr(L1_text, local_dict={"H": H, "ad1": a4p})
    check(L1_verdict == "PASS" and sp.expand(L1_record - 2 * plain(R_scalar)) == 0,
          "the first Lovelock scalar of the record is twice our Ricci scalar",
          record=f"{A4_REPORT}, check L1_equals_gkd_branch (with "
                 "python-lovelock-report.json, check L1_equals_2R)")
    '''),
    md(r"""
    Exact agreement was decided by sympy's simplification. A second, independent test
    uses numbers only: the independent Revision verification
    (`Revision/gkd_lovelock/results/python-lovelock-report.json`, list `randomPoints`)
    chose five test points, each a set of exact fractions for $H$, $x_8$, $a_4$, $a_4'$
    and $a_4''$. The next cell evaluates every component of the record (25 Christoffel
    symbols, 156 Riemann components, 64 Ricci and 64 Einstein components and the Ricci
    scalar) and our component with the same indices at these five points, with
    **30 significant digits** (the package mpmath; `sp.lambdify(..., "mpmath")` turns an
    expression into an mpmath function), and reports the largest relative difference
    $|{\rm ours} - {\rm record}| / \max(1, |{\rm record}|)$.
    """),
    code(r'''
    PYTHON_REPORT = "Revision/gkd_lovelock/results/python-lovelock-report.json"
    python_report = json.loads(repository_file(PYTHON_REPORT).read_text(encoding="utf-8"))
    mpmath.mp.dps = 30  # mpmath works with 30 significant digits from now on


    def exact(text):
        """A fraction such as 46/75 of the record as an mpmath number."""
        fraction = sp.Rational(text)
        return mpmath.mpf(fraction.p) / fraction.q  # numerator / denominator


    test_points = [[exact(p["H"]), exact(p["x8"]), exact(p["a4"]),
                    exact(p["a4" + prime]), exact(p["a4" + prime + prime])]
                   for p in python_report["randomPoints"]]
    pairs = [(Gamma[a][b][c], v) for (a, b, c), v in record_gamma.items()]
    pairs += [(R_mixed[key], v) for key, v in record_riemann.items()]
    pairs += [(Ric[i, j], from_mathematica(record["ricciMixed"][f"{NAMES[i]},{NAMES[j]}"]
                                           ["mathematica"]))
              for i in range(8) for j in range(8)]
    pairs += [(G[i, j], from_mathematica(record["einsteinMixed"][f"{NAMES[i]},{NAMES[j]}"]
                                         ["mathematica"]))
              for i in range(8) for j in range(8)]
    pairs += [(R_scalar, from_mathematica(record["ricciScalar"]))]
    ARGS30 = (H, x8, a4v, a4p, a4pp)  # the order of the five numbers of a test point
    largest, evaluations = mpmath.mpf(0), 0
    for mine, theirs in pairs:
        f_mine = sp.lambdify(ARGS30, symbolic(sp.S(mine)), "mpmath")
        f_record = sp.lambdify(ARGS30, sp.S(theirs), "mpmath")
        for point in test_points:
            ours, recorded = f_mine(*point), f_record(*point)
            largest = max(largest, abs(ours - recorded) / max(1, abs(recorded)))
            evaluations += 1
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
    (`Revision/lead_checks/reports/einstein-gauss-bonnet-a4.json`) states four
    properties of the Einstein tensor; the next cell checks them on our result: $G$ is
    diagonal (in particular $G^{x_4}{}_{x_8} = 0$), no component depends on $x_8$, the
    three 3-space components are equal and the three extra-time components are equal,
    and $G^{x_4}{}_{x_4} - G^{x_8}{}_{x_8} = 6(a_4'^2 + H^2)$, which is positive for
    $H > 0$ (a later chapter uses this to show that for $H > 0$ no empty spacetime, not
    even one with a cosmological constant, has this metric: some matter is needed).
    """),
    code(r'''
    LEAD = "Revision/lead_checks/reports/einstein-gauss-bonnet-a4.json"
    check(all(G[i, j] == 0 for i in range(8) for j in range(8) if i != j),
          "the Einstein tensor is diagonal",
          record=f"{LEAD}, check einstein_off_diagonal_zero")
    check(all(sp.diff(G[i, i], x8) == 0 for i in range(8)),
          "no component of the Einstein tensor depends on x8",
          record=f"{LEAD}, check einstein_x8_independent")
    check(G[0, 0] == G[1, 1] == G[2, 2] and G[4, 4] == G[5, 5] == G[6, 6],
          "3-space components equal, extra-time components equal",
          record=f"{LEAD}, check einstein_isotropy")
    gap = sp.simplify(symbolic(G[3, 3] - G[7, 7]))
    say(f"G^x4_x4 - G^x8_x8 = {sp.factor(gap)}")
    check(sp.simplify(gap - 6 * (a4p ** 2 + H ** 2)) == 0,
          "G^x4_x4 - G^x8_x8 = 6 (a4p^2 + H^2) > 0",
          record=f"{LEAD}, check no_vacuum_for_H_positive")
    '''),
    md(r"""
    Every Einstein tensor satisfies the **contracted Bianchi identity**
    $\nabla_\mu G^\mu{}_\nu = 0$, where for a tensor with one upper and one lower index
    $\nabla_\mu G^\mu{}_\nu = \sum_\mu \partial_\mu G^\mu{}_\nu + \sum_{\mu,\lambda}
    \Gamma^\mu{}_{\mu\lambda} G^\lambda{}_\nu - \sum_{\mu,\lambda} \Gamma^\lambda{}_{\mu\nu}
    G^\mu{}_\lambda$. It is the reason why the energy of the matter that sources the
    metric must be conserved. The next cell computes the eight components with the
    function $a_4(x_4)$ (so that sympy can differentiate $a_4''$ and produce $a_4'''$)
    and checks that each simplifies to zero. The Rust program checked the same for its
    tensor $P_{(1)} = -4G$.
    """),
    code(r'''
    divergence = []
    for nu in range(8):
        value = sum(sp.diff(G[mu, nu], X[mu]) for mu in range(8)) \
            + sum(Gamma[mu][mu][lam] * G[lam, nu] for mu in range(8) for lam in range(8)) \
            - sum(Gamma[lam][mu][nu] * G[mu, lam] for mu in range(8) for lam in range(8))
        divergence.append(vanishes(value))
    check(all(divergence),
          "the contracted Bianchi identity: the divergence of G vanishes",
          record="Revision/gkd_lovelock/results/lovelock-report.json, checks "
                 "k1_equals_minus_4_einstein and k1_divergence_free")
    '''),
    md(r"""
    ## 12. The Kretschmann scalar: an invariant that does not see $z$

    The next cell computes $K = \sum R^{ab}{}_{cd} R^{cd}{}_{ab}$ and
    $\sum_{a,b} R^a{}_b R^b{}_a$ from our components, and computes $K$ a second time
    from the 156 components of the record alone. Although some components depend on
    $z$ (for example $R^{x_1x_4}{}_{x_1x_8} = H a_4' \cot z$), their products combine so
    that $K$ depends only on $H$, $a_4'$ and $a_4''$. Completing the square,

    $$\frac{K}{12} = 7H^4 - 2H^2 a_4'^2 + 7 a_4'^4 + 2 a_4''^2
    = 7\Bigl(a_4'^2 - \frac{H^2}{7}\Bigr)^2 + \frac{48}{7} H^4 + 2 a_4''^2 ,$$

    (expand the square: $7 a_4'^4 - 2 H^2 a_4'^2 + H^4/7$, and $H^4/7 + 48 H^4/7 =
    7 H^4$), so $K \ge \frac{576}{7} H^4 > 0$ for every history: the metric is curved
    for every $H > 0$. The cell checks all of this.
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
          "K from our components equals K from the 156 components of the record")
    check(not K.has(x8) and not K.has(a4v),
          "K depends only on H, a4p and a4pp, not on z and not on a4")
    square_form = 7 * (a4p ** 2 - H ** 2 / 7) ** 2 + sp.Rational(48, 7) * H ** 4 \
        + 2 * a4pp ** 2
    check(sp.expand(K / 12 - square_form) == 0,
          "K/12 = 7 (a4p^2 - H^2/7)^2 + 48 H^4/7 + 2 a4pp^2, so K > 0 for H > 0")
    report("smallest possible K (at a4p^2 = H^2/7, a4pp = 0)",
           sp.sstr(sp.Rational(576, 7) * H ** 4))
    '''),
    md(r"""
    The next cell shows the cancellation in pictures, for $a_4'' = 0$ and $H = 1$. Left:
    the sizes of two $z$-dependent components, $R^{x_1x_4}{}_{x_1x_8} = H a_4' \cot z$
    and $R^{x_1x_8}{}_{x_1x_4} = -H a_4' \tan z$, of their product $-H^2 a_4'^2$ and of
    the constant component $R^{x_1x_8}{}_{x_1x_8} = -H^2$, for $a_4' = 1.5$ (so that the
    product, $2.25$, and $H^2 = 1$ are different numbers). Right: $K$
    computed at 300 values of $z$ by summing all 156 products numerically, for four
    expansion rates $a_4' = A H$ of deflating histories, $A = 0.5, 1, 1.5, 2$: four
    flat lines.
    """),
    code(r'''
    # numerical functions of the 156 components with a4pp = 0 (true on the history
    # a4 = A H x4); the second derivative of a4 is replaced by 0 before lambdify
    riemann_functions = {k: numeric(v.subs(sp.Derivative(a4, (x4, 2)), 0))
                         for k, v in R_mixed.items()}


    def kretschmann_numbers(z_values, rate):
        """K at the points z_values, summed from the 156 numerical components."""
        total = np.zeros_like(z_values)
        for (a, b, c, d), f in riemann_functions.items():
            partner = riemann_functions.get((c, d, a, b))
            if partner is not None:
                total += f(z_values, 0.5, rate, 1.0) * partner(z_values, 0.5, rate, 1.0)
        return total


    z_line = np.linspace(0.02, np.pi / 2 - 0.02, 300)
    cot_part = riemann_functions[(0, 3, 0, 7)](z_line, 0.5, 1.5, 1.0)  # a4p = 1.5
    tan_part = riemann_functions[(0, 7, 0, 3)](z_line, 0.5, 1.5, 1.0)
    fig, axes = plt.subplots(1, 2, figsize=(10.5, 4.2))
    fig.subplots_adjust(wspace=0.32)  # room for the label of the right vertical axis
    axes[0].plot(z_line, np.abs(cot_part), color=RED, lw=1.8,
                 label="$R^{x_1x_4}{}_{x_1x_8} = Ha_4^{\\prime}\\cot z$")
    axes[0].plot(z_line, np.abs(tan_part), color=BLUE, lw=1.8, ls="--",
                 label="minus $R^{x_1x_8}{}_{x_1x_4} = Ha_4^{\\prime}\\tan z$")
    axes[0].plot(z_line, np.abs(cot_part * tan_part), color="black", lw=1.2, ls=":",
                 label="minus their product $= H^2 a_4^{\\prime 2}$")
    axes[0].plot(z_line, np.abs(np.broadcast_to(
        riemann_functions[(0, 7, 0, 7)](z_line, 0.5, 1.5, 1.0), z_line.shape)),
        color=AQUA, lw=1.8, ls="-.", label="minus $R^{x_1x_8}{}_{x_1x_8} = H^2$")
    axes[0].set_yscale("log")
    axes[0].set_xlabel("$z = 6 H x_8$ (radians)")
    axes[0].set_ylabel("absolute value (unit $H^2$)")
    axes[0].set_title("Riemann components, $a_4^{\\prime} = 1.5$")
    axes[0].legend(fontsize=8)
    rates = (0.5, 1.0, 1.5, 2.0)  # four expansion rates a4p = A H (A > 0), unit H
    for rate, colour, style in zip(rates, (VIOLET, AQUA, RED, ORANGE),
                                   ("-", "--", "-.", ":")):
        axes[1].plot(z_line, kretschmann_numbers(z_line, rate), color=colour, ls=style,
                     lw=1.8, label=f"$a_4^{{\\prime}} = {rate:g}\\,H$")
    axes[1].set_yscale("log")
    axes[1].set_xlabel("$z = 6 H x_8$ (radians)")
    axes[1].set_ylabel("$K$ (unit $H^4$)")
    axes[1].set_title("Kretschmann scalar summed from 156 components")
    axes[1].legend(fontsize=8)
    # the values of the formula for K at the four rates, for the caption and the check
    K_values = [float(K.subs({a4p: r, a4pp: 0, H: 1})) for r in rates]
    K_text = ", ".join(f"${k:g}$" for k in K_values)
    save_figure(fig, "riemann_and_kretschmann_z",
                "Left: the absolute values of the Riemann components "
                "$R^{x_1x_4}{}_{x_1x_8} = Ha_4^{\\prime}\\cot z$ (solid) and "
                "$R^{x_1x_8}{}_{x_1x_4} = -Ha_4^{\\prime}\\tan z$ (dashed), of their "
                "product (dotted) and of $R^{x_1x_8}{}_{x_1x_8} = -H^2$ (dash-dotted) "
                "across the patch, for $a_4^{\\prime} = 1.5$, "
                "$a_4^{\\prime\\prime} = 0$, $H = 1$; horizontal axis $z = 6Hx_8$ in "
                "radians, vertical axis on a logarithmic scale in units of $H^2$. "
                "Right: the Kretschmann scalar $K$ summed numerically from all 156 "
                "components at 300 values of $z$ for $a_4^{\\prime} = 0.5, 1, 1.5, 2$ "
                "(in units of $H$), vertical axis $K$ in units of $H^4$, logarithmic. "
                "Single components grow without bound at the ends of the patch, but $K$ "
                f"is the same at every $z$: {K_text}.")
    numbers = [kretschmann_numbers(z_line, r) for r in rates]
    check(all(np.max(np.abs(n - k)) < 1e-9 * k for n, k in zip(numbers, K_values)),
          "summed numerically, K is the same at all 300 values of z and equals the "
          "formula")
    '''),
    md(r"""
    ## 13. The curvature along the deflating history

    Along the history $a_4 = A H x_4$ we have $a_4' = A H$ and $a_4'' = 0$, so every
    curvature scalar is a polynomial in the slope $A$. The author's extra times deflate
    when $a_4$ increases, that is for $A > 0$; the Revision record uses $A = 1$. The
    next cell evaluates the Ricci scalar $R = 6H^2(A^2 - 7)$, the sum
    $\sum R^a{}_b R^b{}_a$ and $K$ as formulas in $A$, checks that they are **even** in
    $A$ (they do not change when $A$ is replaced by $-A$; so these three scalars cannot
    tell which of the two families of directions deflates, the metric and the
    components of the curvature tensors can), and draws them for $0.1 \le A \le 3$
    (every one of these histories deflates the extra times): $R$ on an ordinary axis
    (it vanishes at $A = \sqrt 7$), the two squares on a logarithmic axis.
    """),
    code(r'''
    A = sp.symbols("A", real=True)  # the slope of the history a4 = A H x4
    on_history = {a4p: A * H, a4pp: 0}
    R_A = sp.factor(symbolic(R_scalar).subs(on_history))
    K_A = sp.factor(K.subs(on_history))
    RR_A = sp.factor(ricci_square.subs(on_history))
    say(f"on the history: R = {R_A},  K = {K_A},  R^a_b R^b_a = {RR_A}")
    check(all(sp.expand(f.subs(A, -A) - f) == 0 for f in (R_A, K_A, RR_A)),
          "the curvature scalars are even in A")
    A_line = np.linspace(0.1, 3.0, 291)  # slopes 0.1, 0.11, ..., 3; A_line[90] = 1
    R_numbers = sp.lambdify(A, R_A.subs(H, 1))(A_line)
    K_numbers = sp.lambdify(A, K_A.subs(H, 1))(A_line)
    RR_numbers = sp.lambdify(A, RR_A.subs(H, 1))(A_line)
    fig, axes = plt.subplots(1, 2, figsize=(10.0, 4.2))
    axes[0].plot(A_line, R_numbers, color=VIOLET, lw=1.8, label="$R = 6H^2(A^2 - 7)$")
    axes[0].axhline(0.0, color="black", lw=0.8)
    axes[0].plot([np.sqrt(7)], [0.0], "o", color=VIOLET, ms=7)  # the zero of R
    axes[0].set_ylabel("Ricci scalar $R$ (unit $H^2$)")
    axes[0].set_title("Ricci scalar")
    axes[1].plot(A_line, K_numbers, color=RED, lw=1.8, label="Kretschmann $K$")
    axes[1].plot(A_line, RR_numbers, color=BLUE, lw=1.8, ls="--",
                 label="$\\sum R^a{}_b R^b{}_a$")
    axes[1].set_yscale("log")
    axes[1].set_ylabel("value (unit $H^4$)")
    axes[1].set_title("Squares of the curvature")
    for ax in axes:
        ax.axvline(1.0, color="grey", lw=1.0, ls=":")  # the canonical slope A = 1
        ax.set_xlabel("slope $A$ of the deflating history $a_4 = A H x_4$")
        ax.legend(fontsize=8, loc="upper left")
    axes[0].text(1.05, -40, "$A = 1$", fontsize=9)
    save_figure(fig, "scalars_versus_a",
                "The curvature scalars of the author's metric along the deflating "
                "history $a_4 = AHx_4$ ($a_4^{\\prime} = AH$, "
                "$a_4^{\\prime\\prime} = 0$) as functions of the slope $A$ from $0.1$ "
                "to $3$, with $H = 1$; horizontal axes $A$ (a pure number), the dotted "
                "vertical line marks the canonical $A = 1$ of the Revision record. "
                "Left: the Ricci scalar $R = 6H^2(A^2 - 7)$ in units of $H^2$, "
                "negative for $A < \\sqrt 7$ and zero at the dot. Right, on a "
                "logarithmic axis in units of $H^4$: the Kretschmann scalar "
                "$K = 12H^4(7A^4 - 2A^2 + 7)$ (solid), smallest at "
                "$A^2 = 1/7$, and $\\sum R^a{}_b R^b{}_a = 36H^4(A^4 + 7)$ (dashed), "
                "both positive for every $A$.")
    check(abs(R_numbers[90] - (-36.0)) < 1e-9 and abs(K_numbers[90] - 144.0) < 1e-9,
          "at A = 1: R = -36 H^2 and K = 144 H^4")
    '''),
    md(r"""
    The next cell draws the Einstein tensor along the deflating history. Left: its
    eight diagonal components as bars, for the canonical slope $A = 1$ of the Revision
    record and for $A = 2$. Right: as functions of $A$; with $a_4'' = 0$ the 3-space,
    extra-time and hidden components coincide,
    $G^{x_1}{}_{x_1} = G^{x_5}{}_{x_5} = G^{x_8}{}_{x_8} = 3H^2(5 - A^2)$, and
    $G^{x_4}{}_{x_4} = 3H^2(7 + A^2)$; the gap between them, $6H^2(A^2 + 1)$, is never
    zero.
    """),
    code(r'''
    G_A = [sp.factor(symbolic(G[k, k]).subs(on_history)) for k in range(8)]
    for k in (0, 3, 4, 7):
        say(f"  on the history: G^{NAMES[k]}_{NAMES[k]} = {G_A[k]}")
    bars = {value: [float(G_A[k].subs({A: value, H: 1})) for k in range(8)]
            for value in (1, 2)}
    fig, axes = plt.subplots(1, 2, figsize=(10.0, 4.2))
    positions = np.arange(8)
    axes[0].bar(positions - 0.2, bars[1], width=0.38, color=RED, hatch="//",
                label="$A = 1$")
    axes[0].bar(positions + 0.2, bars[2], width=0.38, color=BLUE, label="$A = 2$")
    axes[0].set_xticks(positions, [f"$G^{{x_{k}}}{{}}_{{x_{k}}}$" for k in range(1, 9)],
                       fontsize=8)
    axes[0].set_ylabel("component (unit $H^2$)")
    axes[0].set_title("Diagonal of the Einstein tensor")
    axes[0].legend(fontsize=8)
    space_numbers = sp.lambdify(A, G_A[0].subs(H, 1))(A_line)
    time_numbers = sp.lambdify(A, G_A[3].subs(H, 1))(A_line)
    axes[1].plot(A_line, space_numbers, color=RED, lw=1.8,
                 label="$G^{x_1}{}_{x_1} = G^{x_5}{}_{x_5} = G^{x_8}{}_{x_8}$")
    axes[1].plot(A_line, time_numbers, color=VIOLET, lw=1.8, ls="--",
                 label="$G^{x_4}{}_{x_4}$")
    axes[1].fill_between(A_line, space_numbers, time_numbers, color="grey", alpha=0.2,
                         label="gap $6H^2(A^2 + 1) > 0$")
    axes[1].axhline(0.0, color="black", lw=0.8)
    axes[1].axvline(1.0, color="grey", lw=1.0, ls=":")  # the canonical slope A = 1
    axes[1].set_xlabel("slope $A$ of the deflating history $a_4 = A H x_4$")
    axes[1].set_ylabel("component (unit $H^2$)")
    axes[1].set_title("Einstein tensor versus $A$")
    axes[1].legend(fontsize=8, loc="lower left")
    save_figure(fig, "einstein_tensor",
                "The Einstein tensor $G^{\\mu}{}_{\\nu}$ of the author's metric along "
                "the deflating history $a_4 = AHx_4$ with $H = 1$, in units of $H^2$. "
                "Left: the eight diagonal components (the only non-zero ones) for the "
                "canonical slope $A = 1$ of the Revision record (hatched bars: "
                "$12, 12, 12, 24, 12, 12, 12, 12$) and for $A = 2$ (plain bars: "
                "$3, 3, 3, 33, 3, 3, 3, 3$). Right: the 3-space, extra-time and hidden "
                "components $3H^2(5 - A^2)$ (solid) and the time component "
                "$3H^2(7 + A^2)$ (dashed) as functions of the slope $A$ from $0.1$ to "
                "$3$; the shaded gap $6H^2(A^2 + 1)$ between them never closes.")
    check(bars[1] == [12.0, 12.0, 12.0, 24.0, 12.0, 12.0, 12.0, 12.0]
          and bars[2] == [3.0, 3.0, 3.0, 33.0, 3.0, 3.0, 3.0, 3.0],
          "diagonal of G: 12 (24 for x4) at A = 1 and 3 (33 for x4) at A = 2, unit H^2")
    '''),
    md(r"""
    What do these numbers mean for matter? Einstein's field equations (section 3 of
    this notebook) set $G^\mu{}_\nu + \Lambda\,\delta^\mu{}_\nu = \kappa\, T^\mu{}_\nu$
    with $T = \mathrm{diag}(p_3, p_3, p_3, -\rho, p_t, p_t, p_t, p_8)$. Their $x_4$
    component reads $G^{x_4}{}_{x_4} + \Lambda = -\kappa\rho$, so
    $\kappa\rho = -G^{x_4}{}_{x_4} - \Lambda$; their $x_1$, $x_5$ and $x_8$ components
    read $G^{x_1}{}_{x_1} + \Lambda = \kappa p_3$, $G^{x_5}{}_{x_5} + \Lambda = \kappa
    p_t$ and $G^{x_8}{}_{x_8} + \Lambda = \kappa p_8$. Along the history the three
    components on the left are equal (previous cell), so all three pressures must be
    the same number $p$. The Revision record of the field equations of $a_4$
    (`Revision/field_equations_a4/a4-equations.json`, entry `linearMember`) lists this
    required source in its texts `rhoEinstein` ($\rho$), `pEinstein` ($p$) and
    `rhoPlusPEinstein` ($\rho + p$), written with `AA` for $A$ and `Lam` for $\Lambda$.
    The next cell reads the three texts, turns them into sympy expressions and checks
    them against our Einstein tensor. The sum $\kappa(\rho + p) = -6(A^2 + 1)H^2$ is
    negative for every $A$. Ordinary matter (dust, radiation, a gas) has
    $\rho + p \ge 0$ (the **null energy condition**), so within Einstein's equations
    the source that this history requires is not ordinary matter; a later chapter
    discusses this, also for the field equations with the additional Lovelock terms.
    Here we only check that the record and our curvature agree.
    """),
    code(r'''
    A4_EQUATIONS = "Revision/field_equations_a4/a4-equations.json"
    a4_equations = json.loads(repository_file(A4_EQUATIONS).read_text(encoding="utf-8"))
    linear = a4_equations["linearMember"]  # the entry of the linear history
    kappa = sp.symbols("kappa", positive=True)  # the constant of Einstein's equations
    Lam = sp.symbols("Lam", real=True)  # the cosmological constant Lambda
    source_names = {"AA": A, "H": H, "kappa": kappa, "Lam": Lam}


    def source(key):
        """The record's text linear[key] (Mathematica notation) as sympy."""
        return parse_expr(linear[key]["input"].replace("^", "**"),
                          local_dict=source_names)


    rho_record, p_record = source("rhoEinstein"), source("pEinstein")
    sum_record = source("rhoPlusPEinstein")  # rho + p
    say(f"record: kappa rho       = {sp.expand(kappa * rho_record)}")
    say(f"record: kappa p         = {sp.expand(kappa * p_record)}")
    say(f"record: kappa (rho + p) = {sp.factor(kappa * sum_record)}")
    check(sp.expand(kappa * rho_record - (-G_A[3] - Lam)) == 0,
          "kappa rho of the record equals -G^x4_x4 - Lambda",
          record=f"{A4_EQUATIONS}, linearMember.rhoEinstein (and "
                 "python-a4-report.json, check json_linear_member)")
    check(all(sp.expand(kappa * p_record - (G_A[k] + Lam)) == 0 for k in (0, 4, 7)),
          "kappa p of the record equals G^x1_x1, G^x5_x5 and G^x8_x8 plus Lambda",
          record=f"{A4_EQUATIONS}, linearMember.pEinstein")
    check(sp.expand(kappa * sum_record - (G_A[0] - G_A[3])) == 0,
          "kappa (rho + p) of the record equals G^x1_x1 - G^x4_x4 = -6 (A^2 + 1) H^2",
          record=f"{A4_EQUATIONS}, linearMember.rhoPlusPEinstein")
    '''),
    md(r"""
    ## 14. A negative control: what if the extra times inflated?

    A check that cannot fail teaches nothing. So the next cell changes the metric on
    purpose: the extra times now **inflate** like 3-space, $g_{55} = g_{66} = g_{77} =
    -e^{+2a_4}\sin^{1/3} z$ (this is NOT the author's metric), and computes the
    curvature again with the same functions. In the author's metric the
    $x_4$-$x_8$ components cancelled between the three inflating and the three deflating
    directions; here they add up. The cell prints the off-diagonal Einstein components
    that appear and checks that they are not zero and that they depend on $z$.
    """),
    code(r'''
    g_control = g.copy()
    for k in (4, 5, 6):  # the three extra times, now inflating
        g_control[k, k] = -sp.exp(2 * a4) * sp.sin(6 * H * x8) ** sp.Rational(1, 3)
    Gamma_control = christoffel(g_control, X)
    R_control = raise_second(riemann(Gamma_control, X), g_control)
    Ric_control = ricci(R_control, 8)
    G_control = (Ric_control - Ric_control.trace() / 2 * sp.eye(8)).applyfunc(tidy)
    off = {(i, j): plain(G_control[i, j]) for i in range(8) for j in range(8)
           if i != j and G_control[i, j] != 0}
    for (i, j), value in sorted(off.items()):
        say(f"  control: G^{NAMES[i]}_{NAMES[j]} = {value}")
    check(sorted(off) == [(3, 7), (7, 3)] and all(v.has(z) for v in off.values()),
          "negative control: with inflating extra times G^x4_x8 and G^x8_x4 are not "
          "zero and depend on z")
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

    - From the metric exactly as the author typed it, sympy computed 37 non-zero
      Christoffel symbols (25 with $b \le c$), 156 non-zero Riemann components
      $R^{ab}{}_{cd}$ with 14 different values, the Ricci tensor, the Ricci scalar
      $R = 6a_4'^2 - 42H^2$ and the Einstein tensor; every component agrees exactly
      with the Revision record of the Rust program `lovelock_gkd` (PROVED by exact
      algebra, here and in the record); at the five test points of the independent
      Revision verification all 310 recorded components agree with ours to more than 25
      significant digits. Twice our Ricci scalar equals the first Lovelock scalar
      $L_{(1)}$ of the record of the field equations of $a_4$.
    - The Christoffel symbols were confirmed a second way, by finite differences, with
      an error that falls like $h^2$.
    - The lines along $x_4$ are geodesics: observers at rest fall freely and $x_4$ is
      their proper time.
    - The Riemann tensor has all the symmetries of a Riemann tensor and satisfies the
      first Bianchi identity; the Einstein tensor satisfies the contracted Bianchi
      identity, is diagonal, isotropic in 3-space and in the extra times, and does not
      depend on $x_8$; $G^{x_4}{}_{x_4} - G^{x_8}{}_{x_8} = 6(a_4'^2 + H^2) > 0$.
    - The Kretschmann scalar $K = 12(7H^4 - 2H^2a_4'^2 + 7a_4'^4 + 2a_4''^2)$ does not
      depend on $z$ although single components do, and $K \ge 576H^4/7 > 0$: the metric
      is curved for every $H > 0$.
    - Along the deflating history $a_4 = AHx_4$ the curvature scalars are
      $R = 6H^2(A^2 - 7)$, $K = 12H^4(7A^4 - 2A^2 + 7)$ and
      $\sum R^a{}_b R^b{}_a = 36H^4(A^4 + 7)$, all even in $A$. For the canonical
      history of the Revision record ($A = 1$, $H = 1$): $R = -36$, $K = 144$ and
      $G = \mathrm{diag}(12, 12, 12, 24, 12, 12, 12, 12)$ (units $H^2$ and $H^4$); for
      $A = 2$: $G = \mathrm{diag}(3, 3, 3, 33, 3, 3, 3, 3)$.
    - Through Einstein's equations this Einstein tensor is exactly the source that the
      Revision record of the field equations of $a_4$ lists for the linear history:
      $\kappa\rho = -3(7 + A^2)H^2 - \Lambda$, $\kappa p = 3(5 - A^2)H^2 + \Lambda$ for
      all three pressures, and $\kappa(\rho + p) = -6(A^2 + 1)H^2 < 0$.
    - Negative control: if the extra times inflated instead of deflating, the Einstein
      tensor would acquire the off-diagonal components $G^{x_4}{}_{x_8}$ and
      $G^{x_8}{}_{x_4}$: comparing the two metrics, it is the deflation of the extra
      times that makes the Einstein tensor of the author's metric diagonal.
    - ASSUMED for the plots and the evaluation along the history only: the history
      $a_4 = AHx_4$ with $A > 0$ (a prescribed background, not solved for); every
      formula with a general $a_4(x_4)$ is exact.
    """),
]

if __name__ == "__main__":
    raise SystemExit(run_builder(__file__))
