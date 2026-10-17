#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
"""Builder of Notebook 03a, "The corrected metric of the primordial field" (textbook
"Universes in Pairs").

The notebook Revision/textbook/notebooks/03a_authors_metric.ipynb is BUILT from this
file by Revision/textbook/tools/nbkit.py (never edit the .ipynb by hand):

    python Revision/textbook/tools/nbkit.py build \
        Revision/textbook/notebooks/src/03a_authors_metric.py --date YYYY-MM-DD
    python Revision/textbook/tools/nbkit.py check \
        Revision/textbook/notebooks/src/03a_authors_metric.py

Physics source: Revision/SPEC.md section 1 (the corrected metric, version 2 of
2026-10-16, in the author's coordinates x0..x7; z = 6 H x0 takes every real value; the
hidden direction x0 and the three extra times x5, x6, x7 DEFLATE exponentially together)
and the Revision records named in FACTS["records"].  Every number the notebook compares
with a record is checked by an assertion that names the record file and its check.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools"))
from nbkit import code, md, run_builder  # noqa: E402

FIG = "Revision/textbook/figures/03a"

FACTS = {
    "id": "03a",
    "name": "03a_authors_metric",
    "title": "The corrected metric of the primordial field: signature, scale factors, "
             "the fold and proper volumes",
    "purpose": (
        "It reads the corrected metric of the primordial gravitational field (version 2 "
        "of 2026-10-16, in the author's coordinates x0 to x7, with the two metric "
        "functions a4 and b4) exactly as the Revision record of the curvature "
        "computation stores it, turns the text into an exact sympy matrix, and checks "
        "its diagonal entries, its determinant, its signature (4,4) for every real "
        "z = 6 H x0 away from the points where sin z cos z = 0, its symmetry under "
        "z to pi - z and z to z + pi, and its diagonal vielbein against the Revision "
        "records. It then computes the expansion rate of every direction, the proper "
        "volumes and the hidden coordinate y, and draws the metric as a heat map, its "
        "entries versus z, the scale factor of 3-space (inflating) and the common scale "
        "factor of the hidden direction and the three extra times (deflating "
        "exponentially) along the deflating history a4 = A H x4, b4 = b4(0) "
        "e^(beta A H x4) with beta = 4/3 of the Revision Kohn-Sham work, the functions of "
        "z, the proper volumes and the coordinate y."
    ),
    "records": [
        ["Revision/gkd_lovelock/results/curvature.json",
         "the corrected metric as the record stores it (metricAsGiven), its diagonal "
         "entries (metricDiagonal) and the square root of the absolute value of its "
         "determinant (sqrtAbsDetG), written by the Rust program lovelock_gkd"],
        ["Revision/gkd_lovelock/results/python-lovelock-report.json",
         "the independent sympy verification of that program; its check sqrt_abs_det_g"],
        ["Revision/metric_warped/results/warped-metric.json",
         "the record of the corrected metric: its diagonal vielbein (vielbein_corrected) "
         "and the square root of the absolute value of its determinant "
         "(sqrt_det_g_corrected)"],
        ["Revision/lead_checks/reports/emt-divergence-and-spin-connection.json",
         "the checks vielbein_reproduces_metric and ks_coordinate_jacobian"],
        ["Revision/kohn_sham/results/parameters.json",
         "the deflating history a4 = A H x4, b4 = b4(0) e^(beta A H x4) with A = 1, H = 1, "
         "b4(0) = 1 and beta = 4/3, its five slices of a4 and the tip cut-off L of the "
         "Revision Kohn-Sham solver"],
        ["Revision/kohn_sham/ks-theory.json",
         "the definition of the hidden coordinate y, the fold and the tip, the line "
         "element in y with the hidden scale f = e^(-a4) b4^(1/2) and the warp factor "
         "W = e^(H y) of the extra times, the volume factor e^(-a4) b4^2 e^(3 H y), and "
         "the status of the history (a prescribed background, not solved for)"],
    ],
    "packages": ["numpy", "sympy", "matplotlib"],
    "needs_rust": [],
    "expected_seconds": 15,
    "timeout_seconds": 300,
    "files_written": [
        "Revision/textbook/figures/03a.captions.json",
        f"{FIG}_1_metric_heat_map.png",
        f"{FIG}_2_diagonal_entries.png",
        f"{FIG}_3_history_scale_factors.png",
        f"{FIG}_4_hidden_direction.png",
        f"{FIG}_5_scale_factor_maps.png",
        f"{FIG}_6_proper_volumes.png",
        f"{FIG}_7_hidden_coordinate_y.png",
    ],
    "final_lines": [
        "PASS all seven figure files exist",
        "ALL 30 CHECKS PASSED (notebook 03a)",
    ],
    "troubleshooting": [
        ["\"FileNotFoundError\" for curvature.json, python-lovelock-report.json, "
         "warped-metric.json, emt-divergence-and-spin-connection.json, parameters.json "
         "or ks-theory.json",
         "the notebook reads these six Revision records of the repository, so the "
         "folder Revision of your copy is incomplete. Restore it with the following "
         "command in the repository folder (or clone the repository again) and run the "
         "notebook again:",
         ["git checkout -- Revision"]],
        ["\"AssertionError: record check failed\"",
         "a Revision report no longer lists a check that the notebook relies on as "
         "passed, so your copy of the folder Revision differs from the one the book was "
         "built with. Restore it with the same command and run the notebook again:",
         ["git checkout -- Revision"]],
    ],
}

CELLS = [
    md(r"""
    ## 1. What this notebook computes

    This notebook studies the **metric of the primordial gravitational field**, the
    $8 \times 8$ matrix on which every later computation of the book is built: the
    **corrected metric** (version 2 of 2026-10-16), written in the author's coordinates
    $x_0, \dots, x_7$. It

    - reads the metric **exactly as the Revision record stores it** (the text is in the
      record `Revision/gkd_lovelock/results/curvature.json`) and turns the text into an
      exact sympy matrix, step by step;
    - checks the eight diagonal entries, the determinant
      $\det g = e^{-2a_4} b_4^4 \cot^2 z\, |\sin z|$ and
      $\sqrt{|\det g|} = e^{-a_4} b_4^2\, |\cot z|\, (\sin^2 z)^{1/4}$ against the
      Revision records;
    - checks the **signature** (4,4) for every real $z = 6Hx_0$ away from the points
      where $\sin z \cos z = 0$: four space-like directions $x_0, x_1, x_2, x_3$ and
      four time-like directions $x_4, x_5, x_6, x_7$;
    - checks that the metric repeats with the period $\pi$ in $z$ and is symmetric
      under $z \to \pi - z$ (the reflection across the **fold** $z = \pi/2$);
    - builds the diagonal **vielbein** (the scale factors) and checks that it
      reproduces the metric;
    - computes the **expansion rate** of every direction: 3-space expands with the rate
      $a_4'$, the hidden direction and the three extra times shrink (deflate) together
      with the rate $-a_4' + b_4'/(2b_4)$;
    - draws the scale factors along the **deflating history** $a_4 = A H x_4$,
      $b_4 = b_4(0)\,e^{\beta A H x_4}$ that the Revision Kohn-Sham work uses as a
      prescribed background ($A = 1$, $H = 1$, $b_4(0) = 1$, $\beta = 4/3$);
    - computes the **proper volumes** (3-space grows like $e^{3 a_4}$, the extra times
      shrink like $b_4^{3/2} e^{-3 a_4}$, the 7-volume density
      $e^{-a_4} b_4^2 |\cot z| (\sin^2 z)^{1/4}$ grows on the history like
      $e^{5a_4/3}$) and the **hidden coordinate** $y = \ln|\sin z|/(6H)$, in which the
      hidden direction and the extra times form one block with the common scale factor
      $f = e^{-a_4} b_4^{1/2}$;
    - draws 7 figures and prints a PASS line for every check.
    """),
    md(r"""
    ## 3. The words used in this notebook

    - **Coordinates** $x_0, \dots, x_7$: eight numbers that name a point of the
      8-dimensional spacetime. The author's names and roles: $x_0$ the **hidden** space
      direction; $x_1, x_2, x_3$ ordinary 3-space; $x_4$ the time; $x_5, x_6, x_7$ the
      three **extra times**. (In Python lists they are counted 0 to 7 as well: $x_k$ is
      entry $k$.)
    - **Metric** $g_{\mu\nu}$: the table of numbers (a symmetric matrix) that turns a
      small coordinate step $dx^\mu$ into a squared length,
      $ds^2 = \sum_{\mu,\nu} g_{\mu\nu}\, dx^\mu dx^\nu$. The entries may depend on the
      point.
    - **Diagonal metric**: $g_{\mu\nu} = 0$ whenever $\mu \ne \nu$; then
      $ds^2 = \sum_\mu g_{\mu\mu} (dx^\mu)^2$.
    - **Line element**: the formula for $ds^2$.
    - **Space-like, time-like**: a step along a direction with $g_{\mu\mu} > 0$ has a
      positive squared length (space-like); with $g_{\mu\mu} < 0$ a negative one
      (time-like: it measures a time, not a distance).
    - **Signature** $(p, q)$: the number $p$ of positive and $q$ of negative eigenvalues
      of the metric matrix. For a diagonal matrix the eigenvalues are the diagonal
      entries. The corrected metric has signature (4,4).
    - $\eta$: the flat metric with the same signs, $\eta = \mathrm{diag}(+1, +1, +1,
      +1, -1, -1, -1, -1)$ in the order $x_0, \dots, x_7$.
    - **Determinant** $\det g$: for a diagonal matrix the product of its diagonal
      entries. $\sqrt{|\det g|}\, d^8x$ is the proper (true) volume of a small
      coordinate box.
    - **Scale factor** of a direction: the number $h_\mu = \sqrt{|g_{\mu\mu}|}$ that
      turns a coordinate interval $\Delta x^\mu$ into a proper length
      $h_\mu \Delta x^\mu$.
    - **Vielbein** $e^a{}_\mu$: a matrix with $g_{\mu\nu} = \sum_{a,b} e^a{}_\mu
      \eta_{ab} e^b{}_\nu$; for a diagonal metric the diagonal matrix of the scale
      factors (the Revision record keeps the sign of $\cot z$ in the hidden entry).
    - **Expansion rate** (Hubble rate) of a direction: $\partial_{x_4} \ln h_\mu$, the
      fraction by which its lengths grow per unit of time $x_4$.
    - **Inflate, deflate**: grow, shrink exponentially. 3-space inflates; the hidden
      direction and the extra times deflate.
    - $z = 6 H x_0$: the hidden coordinate in angle form; it takes **every real value**.
    - $(\sin^2 z)^{1/6}$: the positive sixth root of $\sin^2 z$, that is $|\sin z|^{1/3}$
      (the author's reading of $\sin^{1/3} z$, the positive branch).
    - **Degenerate points**: the values of $z$ with $\sin z \cos z = 0$, where an entry
      of the metric vanishes or grows without bound; nothing is computed there.
    - **Fold**: the points $\cos z = 0$ ($z = \pi/2$ and its copies), where $g_{00}$ and
      $\sqrt{|\det g|}$ vanish; the fold joins the two **halves** $0 < z < \pi/2$ and
      $\pi/2 < z < \pi$ of a **cell** $0 < z < \pi$. **Tip**: the points $\sin z = 0$
      ($z = 0$, $z = \pi$, ...), the ends of a cell.
    - **Hidden coordinate** $y = \ln|\sin z|/(6H)$: a second coordinate for the hidden
      direction; $y = 0$ at the fold and $y \to -\infty$ at the tip (section 13).
    - **Hidden scale** $f = e^{-a_4} b_4^{1/2}$: the factor that the hidden direction
      and the three extra times share. **Warp factor** $W = (\sin^2 z)^{1/12} = e^{Hy}$:
      the factor of the extra times only.
    - **Prescribed background**: a metric that is given and not solved for from field
      equations.
    - **Lead checks**: short independent Python programs of the Revision record (folder
      `Revision/lead_checks`), written from scratch by the coordinator of the Revision
      work (the "lead") without importing any other Revision code; each writes a report
      with a list of named checks and their verdicts.
    - **sympy**: the Python package for exact algebra with symbols; **numpy**: arrays of
      numbers; **matplotlib**: plots.
    """),
    md(r"""
    ## 4. The physical and mathematical situation

    The corrected metric of the primordial gravitational field is diagonal. In the order
    $x_0, \dots, x_7$ its diagonal entries are

    $$g = \mathrm{diag}\bigl(e^{-2a_4} b_4 \cot^2 z,\ e^{2a_4},\ e^{2a_4},\ e^{2a_4},\
    -1,\ -e^{-2a_4} b_4 (\sin^2 z)^{1/6},\ -e^{-2a_4} b_4 (\sin^2 z)^{1/6},\
    -e^{-2a_4} b_4 (\sin^2 z)^{1/6}\bigr),\qquad z = 6 H x_0 .$$

    Here $H > 0$ is a constant of the author (a number with the unit 1/length), and
    $a_4 = a_4(x_4)$ and $b_4 = b_4(x_4) > 0$ are functions of the time $x_4$ only, the
    **metric functions** ($b_4$ is never 1). A prime means the derivative with respect
    to $x_4$: $a_4' = d a_4 / d x_4$, $b_4' = d b_4 / d x_4$. The angle $z$ takes every
    real value.

    The line element is therefore

    $$ds^2 = e^{-2a_4} b_4 \cot^2 z\, dx_0^2 + e^{2a_4}(dx_1^2 + dx_2^2 + dx_3^2) - dx_4^2
    - e^{-2a_4} b_4 (\sin^2 z)^{1/6}\,(dx_5^2 + dx_6^2 + dx_7^2) .$$

    Read it term by term. A step $dx_1$ in 3-space has the proper length
    $e^{a_4}\, dx_1$: when $a_4$ grows, 3-space **inflates**, at every $z$ alike. A step
    $dx_5$ along an extra time has the proper duration
    $e^{-a_4} b_4^{1/2} (\sin^2 z)^{1/12}\, dx_5$ and a step $dx_0$ the proper length
    $e^{-a_4} b_4^{1/2} |\cot z|\, dx_0$: both carry the common factor
    $f = e^{-a_4} b_4^{1/2}$, which shrinks at the rate $a_4' - b_4'/(2b_4)$, and along
    the history used below (where $b_4'/b_4 = \tfrac43 a_4'$) at the rate $a_4'/3$: the
    hidden direction and the extra times **deflate exponentially** together. The time
    $x_4$ has the coefficient $-1$, so a step $dx_4$ is a proper time interval of
    exactly $dx_4$: the clock of an observer at rest shows $x_4$.

    This metric replaces two earlier versions, which are WITHDRAWN and appear here only
    as dated history: the metric of 2026-10-14 (with $\cot^2 z$ in the hidden entry and
    the factor $\sin^{1/3} z$ also in 3-space), whose Einstein tensor has an
    off-diagonal component that no diagonal source can match, and version 1 of
    2026-10-16 (with $g_{44} = -\sin^{1/3} z$), whose time lapse oscillates in $x_0$.
    The corrected metric keeps $g_{44} = -1$ and the warp of the extra times, and gives
    the hidden direction the scale factor of the extra times (`Revision/SPEC.md`,
    section 1).

    The metric alone does not fix the functions $a_4(x_4)$ and $b_4(x_4)$; the field
    equations of $a_4$ and $b_4$, derived later in the book, relate them to the energy
    and the pressures of the matter that fills the spacetime. For the plots this
    notebook uses the history of the Revision Kohn-Sham work, $a_4 = A H x_4$ and
    $b_4 = b_4(0)\,e^{\beta A H x_4}$ with $A = 1$, $\beta = 4/3$, $b_4(0) = 1$ and the
    unit of length chosen so that $H = 1$ (`Revision/SPEC.md`, section 1). This history
    is a **prescribed background** (it is assumed, not solved for). With $A > 0$ the
    function $a_4$ increases, so the extra times deflate, as the author requires.
    """),
    md(r"""
    ## 5. Reading the metric exactly as the record stores it

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
    The Rust program `lovelock_gkd`, which computed the curvature of this metric for
    the Revision record, stored the text of the metric in its output file
    `Revision/gkd_lovelock/results/curvature.json` under the name `metricAsGiven`. The
    next cell reads that file and prints the text, one row of the matrix per line (it
    only starts a new line after each `},` and changes nothing else). It is written in
    the language of Mathematica: `{...}` is a list (the whole matrix is a list of eight
    rows, each row a list of eight entries), `E^(...)` means $e$ to the power
    $(...)$, `Sin[...]` and `Cot[...]` are the sine and the cotangent, `a4[x4]` and
    `b4[x4]` are the values of the functions $a_4$ and $b_4$ at $x_4$, and a blank between
    two factors means times. After the matrix the record adds, in brackets, where the
    text comes from.

    The cell also defines the function `record_check(report_file, check_name,
    detail_part)`. Some PASS lines below say that a result reproduces a named check of
    a Revision report (a JSON file with a list or a dictionary `checks`, each check with
    its name, its verdict and a detail text). `record_check` opens the report, finds the
    check with that name and stops the notebook with an error unless the check is there
    and passed (and, if `detail_part` is given, its detail contains that text). Every
    PASS line that names a check of a Revision report calls it first, so that a renamed,
    missing or failing check in the record is caught.
    """),
    code(r'''
    import numpy as np  # arrays of numbers
    import sympy as sp  # exact algebra with symbols
    from sympy.parsing.sympy_parser import (implicit_multiplication, parse_expr,
                                            standard_transformations)


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


    CURVATURE_RECORD = "Revision/gkd_lovelock/results/curvature.json"
    record = json.loads(repository_file(CURVATURE_RECORD).read_text(encoding="utf-8"))
    # the metric exactly as the record stores it, then a note in brackets
    author_text, note = record["metricAsGiven"].split("}} ", 1)
    author_text += "}}"  # the two closing brackets that split removed
    say(f"The metric as the record stores it ({len(author_text)} characters):")
    for line in author_text.replace("},", "},\n").split("\n"):  # one row per line
        print(line)
    say("The note of the record: " + note)
    '''),
    md(r"""
    The next cell makes the **symbols** of the computation: the eight coordinates, the
    constant $H$ (declared positive), the metric functions $a_4(x_4)$ and $b_4(x_4)$
    (unknown functions of $x_4$, so that sympy can differentiate them; $b_4$ declared
    positive), and five plain symbols that we use for printing: `a4p` and `b4p` stand for
    $a_4'$ and $b_4'$, `a4v` and `b4v` for the values of $a_4$ and $b_4$, and `z` for
    $6 H x_0$ (declared real, not positive: $z$ takes every real value).
    """),
    code(r'''
    x0, x1, x2, x3, x4, x5, x6, x7 = sp.symbols("x0:8", real=True)  # 8 coordinates
    COORDS = [x0, x1, x2, x3, x4, x5, x6, x7]
    H = sp.symbols("H", positive=True)  # the constant of the author, H > 0
    a4 = sp.Function("a4")(x4)  # the metric function a4: an unknown function of x4
    b4 = sp.Function("b4", positive=True)(x4)  # the metric function b4 > 0 of x4
    a4p, a4v = sp.symbols("a4p a4v", real=True)  # a4p = a4 prime, a4v = value of a4
    b4p = sp.symbols("b4p", real=True)  # b4p = b4 prime
    b4v = sp.symbols("b4v", positive=True)  # b4v = value of b4
    z = sp.symbols("z", real=True)  # z = 6 H x0, any real number, for printing


    def plain(expression):
        """Write the derivatives of a4 and b4 as a4p and b4p, their values as a4v and
        b4v, and 6 H x0 as z."""
        expression = expression.subs(sp.Derivative(a4, x4), a4p).subs(a4, a4v)
        expression = expression.subs(sp.Derivative(b4, x4), b4p).subs(b4, b4v)
        return expression.subs(x0, z / (6 * H))  # then 6*H*x0 becomes z


    say("Symbols: x0 ... x7, H > 0, the functions a4(x4) and b4(x4), and a4p, a4v, b4p, "
        "b4v, z for printing.")
    '''),
    md(r"""
    The next cell turns the text into Python, one rule at a time, and lets sympy read
    the result. Each `replace` changes one piece of Mathematica notation into the Python
    notation that sympy understands: `exp^` (which an older text of the author used)
    becomes `E^` (sympy's `E` is the number $e = 2.718\ldots$), the square brackets of
    `Sin[6 H x0]` and `Cot[6 H x0]` become round brackets, `a4[x4]` and `b4[x4]` become
    `a4` and `b4` (which the dictionary `names` connects to the functions $a_4(x_4)$ and
    $b_4(x_4)$), the curly brackets of the lists become square brackets, and the power
    sign `^` becomes `**`. The option `implicit_multiplication` reads a blank between
    two factors as a multiplication, as Mathematica does: `6 H x0` means
    $6 \cdot H \cdot x_0$. Because $x_0$ is declared real, sympy writes the positive
    sixth root $(\sin^2 z)^{1/6}$ at once as `Abs(sin(6*H*x0))**(1/3)`, that is
    $|\sin z|^{1/3}$: the positive branch, for every real $z$.
    """),
    code(r'''
    text = author_text
    text = text.replace("exp^", "E^")  # e to the power ...
    text = text.replace("Sin[6 H x0]", "sin(6 H x0)")  # Mathematica [ ] -> Python ( )
    text = text.replace("Cot[6 H x0]", "cot(6 H x0)")
    text = text.replace("a4[x4]", "a4")  # the value of the function a4 at x4
    text = text.replace("b4[x4]", "b4")  # the value of the function b4 at x4
    text = text.replace("{", "[").replace("}", "]")  # Mathematica lists -> Python lists
    text = text.replace("^", "**")  # Mathematica power ^ -> Python power **
    names = {"E": sp.E, "a4": a4, "b4": b4, "H": H, "x0": x0, "sin": sp.sin,
             "cot": sp.cot, "sign": sp.sign}
    rows = parse_expr(text, local_dict=names,
                      transformations=standard_transformations + (implicit_multiplication,))
    g = sp.Matrix(rows)  # the corrected metric as an exact 8 x 8 sympy matrix
    say(f"The matrix has {g.rows} rows and {g.cols} columns. Its diagonal entries:")
    for k in range(8):
        say(f"  g[x{k}, x{k}] = {g[k, k]}")
    off_diagonal = [g[i, j] for i in range(8) for j in range(8) if i != j]
    check(all(entry == 0 for entry in off_diagonal),
          "the 56 entries off the diagonal are zero: the metric is diagonal")
    '''),
    md(r"""
    Two independent checks of this reading follow. First, the next cell types the
    metric a second time by hand, from the formula of section 4 of this notebook, and
    checks that the two matrices agree entry by entry (the difference of every entry
    simplifies to $0$). Second, it compares each diagonal entry with the entry that the
    Rust program `lovelock_gkd` wrote into the record (`metricDiagonal`, in Mathematica
    notation with explicit `*` signs). The small function `from_mathematica` translates
    such a record entry into sympy with the same rules as above, and also `Sign[...]`
    (the sign, $+1$ or $-1$) into `sign(...)`; the check that no square bracket is left
    proves that every piece of notation was translated.
    """),
    code(r'''
    f_hidden = sp.exp(-a4) * sp.sqrt(b4)  # f = e^(-a4) b4^(1/2), the hidden scale
    warp_sq = (sp.sin(6 * H * x0) ** 2) ** sp.Rational(1, 6)  # (sin^2 z)^(1/6) > 0
    typed = sp.diag(f_hidden ** 2 * sp.cot(6 * H * x0) ** 2,  # the order x0, x1, ..., x7
                    sp.exp(2 * a4), sp.exp(2 * a4), sp.exp(2 * a4),
                    -1,
                    -f_hidden ** 2 * warp_sq, -f_hidden ** 2 * warp_sq,
                    -f_hidden ** 2 * warp_sq)
    difference = (g - typed).applyfunc(sp.simplify)  # simplify every entry
    check(difference == sp.zeros(8, 8),
          "the text of the record equals the metric typed by hand from the formula")


    def from_mathematica(entry_text):
        """A record entry in Mathematica notation, as a sympy expression."""
        t = entry_text.replace("Sin[6*H*x0]", "sin(6*H*x0)")
        t = t.replace("Cot[6*H*x0]", "cot(6*H*x0)")
        t = t.replace("Sign[cot(6*H*x0)]", "sign(cot(6*H*x0))")  # the sign of cot z
        t = t.replace("a4[x4]", "a4").replace("b4[x4]", "b4").replace("^", "**")
        if "[" in t or "]" in t:  # a piece of notation that was not translated
            raise ValueError(f"cannot translate {entry_text}")
        return parse_expr(t, local_dict=names)


    agree = [sp.simplify(g[k, k] - from_mathematica(entry)) == 0
             for k, entry in enumerate(record["metricDiagonal"])]
    check(len(agree) == 8 and all(agree),
          "the 8 diagonal entries equal those of the Rust program lovelock_gkd",
          record=f"{CURVATURE_RECORD}, metricDiagonal")
    '''),
    md(r"""
    ## 6. The determinant and the volume factor

    The determinant of a diagonal matrix is the product of its diagonal entries:

    $$\det g = e^{-2a_4} b_4 \cot^2 z \cdot \bigl(e^{2a_4}\bigr)^3 \cdot (-1) \cdot
    \bigl(-e^{-2a_4} b_4 (\sin^2 z)^{1/6}\bigr)^3 .$$

    Line by line: $\bigl(e^{2a_4}\bigr)^3 = e^{6a_4}$ (a power of a power multiplies
    the exponents); $\bigl(-e^{-2a_4} b_4 (\sin^2 z)^{1/6}\bigr)^3 =
    -e^{-6a_4} b_4^3 (\sin^2 z)^{1/2} = -e^{-6a_4} b_4^3 |\sin z|$ (an odd power keeps
    the minus sign, and the positive square root of $\sin^2 z$ is $|\sin z|$); the two
    minus signs multiply to $+1$ and $e^{-2a_4} e^{6a_4} e^{-6a_4} = e^{-2a_4}$, so
    $\det g = e^{-2a_4} b_4^4 \cot^2 z\, |\sin z|$. Its absolute value has the positive
    square root $\sqrt{|\det g|} = e^{-a_4} b_4^2\, |\cot z|\, (\sin^2 z)^{1/4}$ (the root
    of a product is the product of the roots, $\sqrt{\cot^2 z} = |\cot z|$ and
    $\sqrt{|\sin z|} = (\sin^2 z)^{1/4}$). It vanishes at the fold $\cos z = 0$. The
    record writes $|\cot z|$ as `Cot[6*H*x0]*Sign[Cot[6*H*x0]]`, the cotangent times its
    sign. The function $a_4$ does not drop out: the factor $e^{-a_4}$ is left over from
    the hidden direction, which shrinks with the extra times. The next cell lets sympy
    do the same and compares with the records; then it compares numbers at eight points,
    two in each quarter of the period $0 < z < 2\pi$, with $a_4 = 0.3$ and $b_4 = 2$
    (any values would do).
    """),
    code(r'''
    det_g = g.det()  # the product of the diagonal entries
    say(f"det g = {plain(det_g)}")
    record_check("Revision/gkd_lovelock/results/python-lovelock-report.json",
                 "sqrt_abs_det_g",
                 "det g = e^(-2 a4) b4^4 cot^2(6 H x0) |sin(6 H x0)| exactly")  # or stop
    check(sp.simplify(det_g - sp.exp(-2 * a4) * b4 ** 4 * sp.cot(6 * H * x0) ** 2
                      * sp.Abs(sp.sin(6 * H * x0))) == 0,
          "det g = e^(-2 a4) b4^4 cot(z)^2 |sin z|",
          record="Revision/gkd_lovelock/results/python-lovelock-report.json, "
                 "check sqrt_abs_det_g")
    # sqrt|det g| for every real z: |cot z| written as cot z times its sign
    abs_cot = sp.cot(6 * H * x0) * sp.sign(sp.cot(6 * H * x0))
    volume_factor = (sp.exp(-a4) * b4 ** 2 * abs_cot
                     * (sp.sin(6 * H * x0) ** 2) ** sp.Rational(1, 4))
    check(sp.simplify(from_mathematica(record["sqrtAbsDetG"]) - volume_factor) == 0,
          "sqrt|det g| = e^(-a4) b4^2 |cot z| (sin^2 z)^(1/4), as the record writes it",
          record=f"{CURVATURE_RECORD}, sqrtAbsDetG")
    WARPED_RECORD = "Revision/metric_warped/results/warped-metric.json"
    warped = json.loads(repository_file(WARPED_RECORD).read_text(encoding="utf-8"))
    say("record of the corrected metric, sqrt_det_g_corrected: "
        + warped["sqrt_det_g_corrected"])
    # numbers: sqrt(|det g|) at 8 points, two in each quarter, a4 = 0.3, b4 = 2
    z_points = np.array([0.3, 1.2, 1.9, 2.8, 3.5, 4.4, 5.1, 6.0])
    det_numbers = np.array([float(det_g.subs({a4: 0.3, b4: 2}).subs({H: 1, x0: zp / 6}))
                            for zp in z_points])
    formula = (np.exp(-0.3) * 4.0 * np.abs(1 / np.tan(z_points))
               * np.abs(np.sin(z_points)) ** 0.5)
    check(np.max(np.abs(np.sqrt(np.abs(det_numbers)) - formula)) < 1e-13
          and warped["sqrt_det_g_corrected"].startswith("E^(-a4) b4^2 |Cot[6 H x0]|"),
          "sqrt|det g| equals the formula at 8 points in all four quarters",
          record=f"{WARPED_RECORD}, sqrt_det_g_corrected")
    '''),
    md(r"""
    ## 7. The signature (4,4), and the same metric in every half cell

    For a diagonal matrix the eigenvalues are the diagonal entries, so the signature is
    read off the signs of the eight entries. The next cell turns the eight entries into
    fast numerical functions of $z$ and of the values of $a_4$ and $b_4$
    (`sp.lambdify`), evaluates them on a grid of 800 values of $z$ across the whole
    period $-\pi < z < \pi$ (the midpoints of 800 equal steps, so that no point is a
    degenerate point $\sin z \cos z = 0$), 13 values of $a_4$ from $-3$ to $3$ and the
    three values $b_4 = 0.5$, 2 and 4, and checks that the sign pattern is always that of
    $\eta = (+,+,+,+,-,-,-,-)$: four positive and four negative entries. It also checks
    two vectors: a step along $x_1$ has a positive squared length (space-like), a step
    along $x_5$ a negative one (time-like). Where a single point is needed, this notebook
    takes the point of the deflating history of section 10 at $a_4 = 0.5$: there
    $b_4 = b_4(0)\,e^{(4/3)a_4} = e^{2/3}\,b_4(0) = 1.948$ with $b_4(0) = 1$.

    Then it checks two exact symmetries of every entry: the metric does not change when
    $z$ is replaced by $z + \pi$ ($\cot^2$ and $\sin^2$ repeat with the period $\pi$), and
    it does not change when $z$ is replaced by $\pi - z$ (the reflection across the fold
    $z = \pi/2$: $\cot(\pi - z) = -\cot z$ and $\sin(\pi - z) = \sin z$, and only squares
    enter). So every half cell, $0 < z < \pi/2$, $\pi/2 < z < \pi$ and their copies,
    carries the same geometry: the record works on the cell $0 < z < \pi$, whose two
    halves the fold joins.
    """),
    code(r'''
    ETA = np.array([1, 1, 1, 1, -1, -1, -1, -1])  # the flat metric diag(+,+,+,+,-,-,-,-)
    B4_POINT = float(np.exp(2.0 / 3.0))  # b4 on the history at a4 = 0.5, b4(0) = 1
    # the entries as functions of z, a4v and b4v
    diagonal_z = [plain(g[k, k]) for k in range(8)]
    functions = [sp.lambdify((z, a4v, b4v), entry, "numpy") for entry in diagonal_z]


    def diagonal_values(z_values, a4_value, b4_value=B4_POINT):
        """The 8 diagonal entries at the points z_values (one row per entry)."""
        return np.array([np.broadcast_to(f(z_values, a4_value, b4_value), z_values.shape)
                         for f in functions], dtype=float)


    z_grid = -np.pi + (np.arange(800) + 0.5) * (2 * np.pi / 800)  # 800 midpoints
    patterns = set()
    for b4_value in (0.5, 2.0, 4.0):
        for a4_value in np.linspace(-3.0, 3.0, 13):
            # +1 or -1 for each entry
            signs = np.sign(diagonal_values(z_grid, a4_value, b4_value))
            patterns.update(tuple(int(s) for s in column) for column in signs.T)
    say(f"sign patterns found on the grid: {sorted(patterns)}")
    check(patterns == {tuple(int(s) for s in ETA)},
          "on the whole grid -pi < z < pi the signs are (+,+,+,+,-,-,-,-): signature (4,4)")
    step_x1 = diagonal_values(np.array([0.7]), 0.5)[1, 0]  # g11: step along x1
    step_x5 = diagonal_values(np.array([0.7]), 0.5)[5, 0]  # g55: step along x5
    say(f"at z = 0.7, a4 = 0.5, b4 = e^(2/3): g11 = {step_x1:.6f} (space-like), "
        f"g55 = {step_x5:.6f} (time-like)")
    check(step_x1 > 0 > step_x5, "a step along x1 is space-like, along x5 time-like")
    shift = {x0: x0 + sp.pi / (6 * H)}  # z -> z + pi
    mirror = {x0: sp.pi / (6 * H) - x0}  # z -> pi - z, the reflection across the fold
    check(all(sp.simplify(g[k, k].subs(shift) - g[k, k]) == 0
              and sp.simplify(g[k, k].subs(mirror) - g[k, k]) == 0 for k in range(8)),
          "every entry repeats with the period pi and is symmetric under z -> pi - z")
    '''),
    md(r"""
    The next cell sets the colours of all figures of this notebook (a palette chosen so
    that the curves can be told apart also by readers with a colour-vision deficiency;
    every figure also uses line styles and labels, so that it can be read in black and
    white) and then draws the metric at one point, $z = \pi/4$, $a_4 = 0.5$ and
    $b_4 = e^{2/3}$, as a **heat map**: each of the $8 \times 8$ entries is a coloured
    square, red for positive, blue for negative, grey for zero, and its value is written
    in it.
    """),
    code(r'''
    from matplotlib.colors import LinearSegmentedColormap

    BLUE, ORANGE, AQUA, YELLOW = "#2a78d6", "#eb6834", "#1baf7a", "#eda100"
    MAGENTA, GREEN, VIOLET, RED = "#e87ba4", "#008300", "#4a3aa7", "#e34948"
    GREY = "#f0efec"  # the neutral middle of the two-sided colour scale
    DIVERGING = LinearSegmentedColormap.from_list("blue_grey_red", [BLUE, GREY, RED])
    LABELS = [f"$x_{k}$" for k in range(8)]

    z_point, a4_point = np.pi / 4, 0.5
    values = np.zeros((8, 8))
    values[np.diag_indices(8)] = diagonal_values(np.array([z_point]), a4_point)[:, 0]
    fig, ax = plt.subplots(figsize=(6.4, 5.4))
    image = ax.imshow(values, cmap=DIVERGING, vmin=-3.0, vmax=3.0)
    for i in range(8):
        for j in range(8):
            ax.text(j, i, f"{values[i, j]:.3f}" if i == j else "0", ha="center",
                    va="center", fontsize=8)
    ax.set_xticks(range(8), LABELS)
    ax.set_yticks(range(8), LABELS)
    ax.grid(False)  # no grid lines across the squares
    ax.set_title("The metric $g_{\\mu\\nu}$ at $z = \\pi/4$, $a_4 = 0.5$, $b_4 = e^{2/3}$")
    fig.colorbar(image, ax=ax, label="value of the entry (no unit)")
    save_figure(fig, "metric_heat_map",
                "The corrected metric $g_{\\mu\\nu}$ at the point $z = 6Hx_0 = \\pi/4$ "
                "with $a_4 = 0.5$ and $b_4 = e^{2/3}$ (the deflating history at "
                "$a_4 = 0.5$, $b_4(0) = 1$), drawn as a heat map: row $\\mu$ and "
                "column $\\nu$ run "
                "over the coordinates $x_0$ to $x_7$, red squares are positive entries, "
                "blue squares negative ones, grey squares zero; the number in each "
                "square is the entry. Only the diagonal is non-zero; the hidden entry is "
                "$e^{-1}e^{2/3}\\cot^2(\\pi/4) = e^{-1/3} = 0.717$, the three 3-space "
                "entries are equal, $e^{1} = 2.718$, the three extra-time entries are "
                "equal, $-e^{-1/3}(\\sin^2 \\pi/4)^{1/6} = -0.638$, and the time entry "
                "is $-1$: four positive and four negative entries, the signature (4,4).")
    check(abs(values[0, 0] - np.exp(-1.0 / 3.0)) < 1e-12
          and abs(values[1, 1] - np.e) < 1e-12
          and abs(values[5, 5] + np.exp(-1.0 / 3.0) * 0.5 ** (1 / 6)) < 1e-12,
          "at z = pi/4, a4 = 0.5, b4 = e^(2/3): g00 = e^(-1/3), g11 = e and "
          "g55 = -e^(-1/3) (1/2)^(1/6)")
    '''),
    md(r"""
    The next cell draws the eight diagonal entries as functions of $z$ across two cells,
    $-\pi < z < \pi$, for $a_4 = 0.5$ and $b_4 = e^{2/3}$, together with the determinant
    divided by its factor $e^{-2a_4} b_4^4$, $\cot^2 z\,|\sin z| = \cos^2 z/|\sin z|$.
    Entries that are equal are drawn as one curve. The hidden entry
    $e^{-2a_4} b_4 \cot^2 z$ grows without bound towards each tip ($z \to 0$, $\pm\pi$)
    and vanishes at each fold ($z = \pm\pi/2$), where the determinant vanishes too;
    there the coordinate $x_0$ stops being a good coordinate. The 3-space entries do not
    depend on $z$ at all.
    """),
    code(r'''
    cells = [np.linspace(-np.pi + 0.02, -0.02, 600), np.linspace(0.02, np.pi - 0.02, 600)]
    fig, ax = plt.subplots()
    for n, z_cell in enumerate(cells):  # one cell after the other: no line across a tip
        entries = diagonal_values(z_cell, 0.5)  # b4 = e^(2/3), the history at a4 = 0.5
        first = n == 0  # only the first cell gets the labels of the legend
        ax.plot(z_cell, entries[0], color=AQUA, lw=1.8,
                label="$g_{00} = e^{-2a_4}b_4\\cot^2 z$" if first else None)
        ax.plot(z_cell, entries[1], color=RED, lw=1.8,
                label="$g_{11} = g_{22} = g_{33} = e^{2a_4}$" if first else None)
        ax.plot(z_cell, entries[4], color=VIOLET, lw=1.8, ls="-.",
                label="$g_{44} = -1$" if first else None)
        ax.plot(z_cell, entries[5], color=BLUE, lw=1.8, ls="--",
                label="$g_{55} = g_{66} = g_{77} = -e^{-2a_4}b_4(\\sin^2 z)^{1/6}$"
                if first else None)
        ax.plot(z_cell, np.cos(z_cell) ** 2 / np.abs(np.sin(z_cell)), color="black",
                lw=1.2, ls=":",
                label="$\\det g/(e^{-2a_4}b_4^4) = \\cos^2 z/|\\sin z|$" if first else None)
    ax.axhline(0.0, color="black", lw=0.8)
    for fold in (-np.pi / 2, np.pi / 2):
        ax.axvline(fold, color="grey", lw=0.8, ls=":")
        ax.text(fold + 0.05, 3.3, "fold", fontsize=9)
    ax.set_ylim(-3.4, 3.6)  # room below the curves for the legend
    ax.set_xlabel("$z = 6 H x_0$ (radians)")
    ax.set_ylabel("entry of the metric (no unit)")
    ax.set_title("The diagonal entries across two cells ($a_4 = 0.5$, $b_4 = e^{2/3}$)")
    ax.legend(fontsize=7, loc="lower center", ncol=2)
    save_figure(fig, "diagonal_entries",
                "The diagonal entries of the corrected metric as functions of "
                "$z = 6Hx_0$ from $-\\pi$ to $\\pi$ (two cells, each made of two halves "
                "joined at a fold), for $a_4 = 0.5$ and $b_4 = e^{2/3}$ (the deflating "
                "history at $a_4 = 0.5$); horizontal axis $z$ in radians, vertical axis "
                "the value of the entry (pure numbers). The three 3-space entries "
                "(solid red) are $e = 2.718$ at every $z$, the three extra-time entries "
                "(dashed blue) and the time entry (dash-dotted) stay negative "
                "everywhere, so the signature is (4,4) at every point with "
                "$\\sin z\\cos z \\neq 0$; the hidden entry (aqua) grows without "
                "bound towards the tips $z = 0, \\pm\\pi$ and reaches $0$ at the folds "
                "$z = \\pm\\pi/2$ (grey vertical lines), where the determinant, drawn as "
                "$\\cos^2 z/|\\sin z|$ (dotted black), also vanishes.")
    values_all = np.concatenate([diagonal_values(c, 0.5) for c in cells], axis=1)
    check(np.all(values_all[0] > 0) and np.all(values_all[1] == np.e)
          and np.cos(np.pi / 2) ** 2 < 1e-30,
          "g00 > 0 away from the folds, g11 = e at every z, det g = 0 at the fold")
    '''),
    md(r"""
    ## 8. The vielbein: the scale factor of each direction

    Write each diagonal entry as a sign times a square: $g_{\mu\mu} = \eta_{\mu\mu}
    h_\mu^2$. With $f = e^{-a_4} b_4^{1/2}$ the scale factors are

    $$h = \bigl(f\cot z,\ e^{a_4},\ e^{a_4},\ e^{a_4},\ 1,\ f(\sin^2 z)^{1/12},\
    f(\sin^2 z)^{1/12},\ f(\sin^2 z)^{1/12}\bigr).$$

    The hidden entry keeps the sign of $\cot z$, as in the record (only its square
    enters the metric; its size $f|\cot z|$ is the scale factor proper). The diagonal
    matrix of these numbers is the **vielbein** $e^a{}_\mu$ used for the spinors later
    in the book. The next cell checks $\eta_{\mu\mu} h_\mu^2 = g_{\mu\mu}$ for all eight
    directions; the lead's independent check of the Revision record did the same, and
    the record of the corrected metric states the same vielbein.
    """),
    code(r'''
    twelfth = (sp.sin(6 * H * x0) ** 2) ** sp.Rational(1, 12)  # (sin^2 z)^(1/12) > 0
    # the author's order x0, x1, ..., x7
    h = [f_hidden * sp.cot(6 * H * x0)] + [sp.exp(a4)] * 3 + [sp.Integer(1)] \
        + [f_hidden * twelfth] * 3
    for k in range(8):
        say(f"  h[x{k}] = {plain(h[k])}")
    say("record of the corrected metric, vielbein_corrected: "
        + warped["vielbein_corrected"])
    LEAD_EMT = "Revision/lead_checks/reports/emt-divergence-and-spin-connection.json"
    record_check(LEAD_EMT, "vielbein_reproduces_metric")  # stops if not passed
    check(all(sp.simplify(int(ETA[k]) * h[k] ** 2 - g[k, k]) == 0 for k in range(8))
          and warped["vielbein_corrected"].startswith(
              "f0 = E^(-a4) b4^(1/2) Cot[6 H x0] (signed"),
          "eta times h squared reproduces every diagonal entry of the metric",
          record=f"{LEAD_EMT}, check vielbein_reproduces_metric")
    '''),
    md(r"""
    ## 9. The expansion rate of each direction

    The proper length of a coordinate interval $\Delta x_\mu$ is $|h_\mu| \Delta x_\mu$.
    Its relative growth per unit time is $\partial_{x_4} \ln |h_\mu|$. For 3-space,
    $\ln h_1 = a_4$, so the rate is $a_4'$; for an extra time
    $\ln h_5 = \tfrac12 \ln b_4 - a_4 + \tfrac1{12} \ln \sin^2 z$ and the rate is
    $-a_4' + b_4'/(2b_4)$; for the hidden direction
    $\ln |h_0| = \tfrac12 \ln b_4 - a_4 + \ln|\cot z|$ and the rate is the same,
    $-a_4' + b_4'/(2b_4)$; $h_4 = 1$ does not change. The next cell lets sympy
    differentiate (it differentiates $\ln h_\mu^2/2$, which needs no absolute value). It
    also checks that the four scale factors of the hidden direction and the extra
    times are $f$ times functions of $z$ alone, and that the scale factor of 3-space does
    not depend on $z$: 3-space has no warp.
    """),
    code(r'''
    rates = [sp.simplify(sp.diff(sp.log(h[k] ** 2) / 2, x4)) for k in range(8)]
    for k in range(8):
        say(f"  expansion rate of x{k}: {plain(rates[k])}")
    a4_prime, b4_prime = sp.Derivative(a4, x4), sp.Derivative(b4, x4)
    shrink = -a4_prime + b4_prime / (2 * b4)  # the common rate of x0, x5, x6, x7
    expected = [shrink] + [a4_prime] * 3 + [0] + [shrink] * 3  # the order x0, ..., x7
    check([sp.simplify(r - e) == 0 for r, e in zip(rates, expected)] == [True] * 8,
          "3-space expands with rate a4p; x0 and the extra times change with rate "
          "-a4p + b4p/(2 b4)")
    check(all(sp.diff(sp.simplify(h[k] / f_hidden), x4) == 0 for k in (0, 5, 6, 7))
          and all(not h[k].has(x0) for k in (1, 2, 3)),
          "x0 and the extra times share the factor f; 3-space has no z dependence")
    '''),
    md(r"""
    ## 10. The deflating history of the Revision Kohn-Sham work

    The next cell reads the parameters of the Revision Kohn-Sham solver
    (`Revision/kohn_sham/results/parameters.json`): the constant $H$, the slope $A$ of
    the history $a_4 = A H x_4$, the exponent $\beta$ and the starting value $b_4(0)$ of
    the second metric function $b_4 = b_4(0)\,e^{\beta A H x_4}$, the five values of
    $a_4$ (the **slices**) at which that solver computes its states, the rule for the
    hidden scale $f$, and the tip cut-off $L$ (used in section 13 of this notebook). It
    also reads the theory record of that work (`Revision/kohn_sham/ks-theory.json`) and
    prints the first and the last sentence of its statement about the **status of the
    history** (key `historyStatus`). The sentences in between, not printed, say why:
    with the author's Lovelock weights the field equations of $a_4$ and $b_4$ allow this
    history only with a source whose hidden and extra-time pressures are equal and that
    grows with $x_4$, and the Kohn-Sham states computed along it are not shown to supply
    it. So the history is assumed, not derived; this notebook uses it only to draw the
    time dependence of the metric.
    """),
    code(r'''
    PARAMETERS = "Revision/kohn_sham/results/parameters.json"
    parameters = json.loads(repository_file(PARAMETERS).read_text(encoding="utf-8"))
    physics = parameters["physics"]
    H_value, A_value = physics["H"], physics["historyA"]
    beta = physics["historyBeta"]  # b4 = b4(0) e^(beta A H x4)
    b4_start = physics["historyB4AtZero"]  # b4(0)
    slices = physics["slicesA4"]  # the values of a4 at which the solver works
    L_tip = physics["L_tipCutoff"]  # the tip cut-off, in units of 1/H
    say(f"H = {H_value}, A = {A_value}, beta = {beta:.6f}, b4(0) = {b4_start}, "
        f"slices a4 = {slices}, tip cut-off L = {L_tip}")
    say("record, hiddenScaleRule: " + physics["hiddenScaleRule"])
    check(H_value == 1.0 and A_value == 1.0 and abs(beta - 4.0 / 3.0) < 1e-15
          and b4_start == 1.0 and slices == [0.0, 0.5, 1.0, 1.5, 2.0],
          "the history of the record is a4 = x4, b4 = e^(4 x4/3) (A = 1, H = 1, "
          "beta = 4/3, b4(0) = 1) with slices 0 to 2")
    KS_THEORY = "Revision/kohn_sham/ks-theory.json"
    ks_theory = json.loads(repository_file(KS_THEORY).read_text(encoding="utf-8"))
    status = ks_theory["adiabaticity"]["historyStatus"]  # the record's own statement
    sentences = status.split(". ")  # the statement, cut into its sentences
    say("status of the history (record): " + sentences[0] + ".")
    say(sentences[-1])  # the last sentence already ends with a full stop
    check(status.startswith("PRESCRIBED BACKGROUND") and "not solved for" in status,
          "the record states that the history is a prescribed background",
          record=f"{KS_THEORY}, adiabaticity.historyStatus")
    '''),
    md(r"""
    Along this history $a_4 = A H x_4$ and $b_4 = b_4(0)\,e^{\beta A H x_4}$, so
    $a_4 = 0, 0.5, \dots, 2$ at $x_4 = 0, 0.5, \dots, 2$ (in units of $1/H$). The scale
    factor of 3-space is $e^{a_4}$, and the common factor of the hidden direction and of
    the extra times is
    $f = e^{-a_4}b_4^{1/2} = b_4(0)^{1/2}\,e^{-(1 - \beta/2)a_4} = e^{-a_4/3}$: they
    deflate exponentially, at one third of the rate at which 3-space inflates, and the
    product of the two factors grows like $e^{(\beta/2)a_4} = e^{2a_4/3}$. The next cell
    draws both, and their product, against $x_4$ twice: on an ordinary vertical axis
    (left) and on a logarithmic one (right), on which an exponential is a straight line
    whose slope is its rate ($+AH$ and $-AH/3$). The dots mark the five slices.
    """),
    code(r'''
    x4_line = np.linspace(0.0, 2.5, 251)
    a4_line = A_value * H_value * x4_line  # the history a4 = A H x4
    slice_x4 = np.array(slices) / (A_value * H_value)  # the times of the slices
    rate_t = 1.0 - beta / 2.0  # f = e^(-a4) b4^(1/2) scales like e^(-(1 - beta/2) a4)
    fig, axes = plt.subplots(1, 2, figsize=(10.0, 4.2))
    for ax, scale in zip(axes, ["linear", "log"]):
        ax.plot(x4_line, np.exp(a4_line), color=RED, lw=1.8,
                label="3-space: $e^{a_4}$ (inflates)")
        ax.plot(x4_line, np.exp(-rate_t * a4_line), color=BLUE, lw=1.8, ls="--",
                label="$x_0$ and extra times: $f = e^{-a_4}b_4^{1/2} = e^{-a_4/3}$")
        ax.plot(x4_line, np.exp(a4_line) * np.exp(-rate_t * a4_line), color="black",
                lw=1.2, ls=":", label="product $= e^{2a_4/3}$")
        ax.plot(slice_x4, np.exp(slices), "o", color=RED, ms=6)
        ax.plot(slice_x4, np.exp(-rate_t * np.array(slices)), "s", color=BLUE, ms=6)
        ax.set_yscale(scale)
        ax.set_xlabel("time $x_4$ (unit $1/H$)")
        ax.set_ylabel("scale factor relative to $x_4 = 0$")
    axes[0].set_title("Ordinary vertical axis")
    axes[1].set_title("Logarithmic vertical axis: straight lines")
    axes[0].legend(fontsize=8)
    save_figure(fig, "history_scale_factors",
                "The time dependence of the scale factors along the deflating history "
                "$a_4 = A H x_4$, $b_4 = b_4(0)\\,e^{\\beta A H x_4}$ with $A = 1$, "
                "$H = 1$, $b_4(0) = 1$, $\\beta = 4/3$ of the Revision Kohn-Sham work: "
                "3-space $e^{a_4}$ (solid red), the common factor "
                "$f = e^{-a_4}b_4^{1/2} = e^{-a_4/3}$ of the hidden direction and the "
                "three extra times (dashed blue) and their "
                "product $e^{2a_4/3}$ (dotted black), on an ordinary (left) and a "
                "logarithmic (right) vertical axis; horizontal axis the time $x_4$ in "
                "units of $1/H$, vertical axis the factor by which lengths have grown "
                "since $x_4 = 0$ (a pure number). Dots and squares mark the five slices "
                "$a_4 = 0, 0.5, 1, 1.5, 2$. 3-space grows by $e^2 = 7.39$ and the hidden "
                "direction and the extra times shrink to $e^{-2/3} = 0.513$; on the "
                "logarithmic axis both are straight lines with slopes $+1$ and $-1/3$, "
                "the product grows by $e^{4/3} = 3.79$.")
    report("3-space growth factor at the last slice a4 = 2", f"{np.exp(2.0):.6f}")
    report("shrink factor f of x0 and the extra times at the last slice a4 = 2",
           f"{np.exp(-2.0 / 3.0):.6f}")
    product_last = np.exp(slices[-1]) * np.exp(-rate_t * slices[-1])
    check(abs(product_last - np.exp(2.0 * slices[-1] / 3.0)) < 1e-14 and rate_t > 0,
          "x0 and the extra times deflate (rate 1/3 of a4'), the product grows like "
          "e^(2 a4/3)")
    '''),
    md(r"""
    ## 11. The hidden direction: the functions of $z$

    The scale factors of the hidden direction and of the extra times also depend on
    $z$. The extra times share the warp factor $W = (\sin^2 z)^{1/12}$ (their metric
    entries share its square $W^2 = (\sin^2 z)^{1/6}$), and the hidden direction itself
    has the factor $|\cot z|$ (its metric entry has $\cot^2 z$). The next cell draws
    these four functions across two cells, $-\pi < z < \pi$: the first two on an
    ordinary axis (they lie between 0 and 1, reach 1 at each fold and vanish at each
    tip), the last two on a logarithmic axis (they grow without bound at each tip and
    vanish at each fold).
    """),
    code(r'''
    z_line = -np.pi + (np.arange(1200) + 0.5) * (2 * np.pi / 1200)  # no degenerate point
    fig, axes = plt.subplots(1, 2, figsize=(10.0, 4.2))
    axes[0].plot(z_line, np.abs(np.sin(z_line)) ** (1 / 6), color=RED, lw=1.8,
                 label="warp factor $W = (\\sin^2 z)^{1/12}$")
    axes[0].plot(z_line, np.abs(np.sin(z_line)) ** (1 / 3), color=ORANGE, lw=1.8,
                 ls="--", label="$W^2 = (\\sin^2 z)^{1/6}$ (in $g_{55}$)")
    axes[0].set_ylim(0.0, 1.25)
    axes[0].set_title("The warp of the three extra times")
    axes[1].plot(z_line, np.abs(1 / np.tan(z_line)), color=AQUA, lw=1.8,
                 label="$|\\cot z|$ (in the scale factor of $x_0$)")
    axes[1].plot(z_line, 1 / np.tan(z_line) ** 2, color=VIOLET, lw=1.8, ls="--",
                 label="$\\cot^2 z$ (in $g_{00}$)")
    axes[1].set_yscale("log")
    axes[1].set_title("The hidden direction (logarithmic axis)")
    for ax in axes:
        ax.set_xlabel("$z = 6 H x_0$ (radians)")
        ax.set_ylabel("value (no unit)")
        ax.legend(fontsize=8, loc="upper center")
    save_figure(fig, "hidden_direction",
                "The functions of the hidden coordinate $z = 6Hx_0$ in the corrected "
                "metric, across two cells $-\\pi < z < \\pi$; horizontal axes $z$ in "
                "radians, vertical axes pure numbers. Left: the warp factor "
                "$W = (\\sin^2 z)^{1/12}$ of the three extra times (solid) "
                "and its square $W^2 = (\\sin^2 z)^{1/6}$, which stands in the three "
                "extra-time metric entries (dashed), rise from $0$ at each tip to $1$ at "
                "each fold $z = \\pm\\pi/2$. Right, on a logarithmic axis: the factor "
                "$|\\cot z|$ of the hidden direction (solid) and its square "
                "$\\cot^2 z$ of $g_{00}$ (dashed) "
                "grow without bound towards each tip and fall to $0$ at each fold. All "
                "four repeat with the period $\\pi$ and are symmetric about each fold.")
    check(abs(np.abs(np.sin(np.pi / 2)) ** (1 / 6) - 1.0) < 1e-15
          and abs(np.abs(np.sin(-np.pi / 2)) ** (1 / 6) - 1.0) < 1e-15,
          "the warp factor equals 1 at the folds z = pi/2 and z = -pi/2")
    '''),
    md(r"""
    The next cell shows how the two effects combine. It draws, over the plane of the
    time $x_4$ (along the history $a_4 = x_4$, $b_4 = e^{4x_4/3}$) and the hidden
    coordinate $z$ across one cell $0 < z < \pi$, the logarithm to base 10 of the scale
    factor of the hidden direction, $\log_{10}(e^{-a_4}b_4^{1/2}|\cot z|) =
    \log_{10}(e^{-a_4/3}|\cot z|)$ (left), and of an extra time,
    $\log_{10}(e^{-a_4}b_4^{1/2}(\sin^2 z)^{1/12}) = \log_{10}(e^{-a_4/3}
    (\sin^2 z)^{1/12})$ (right). The value $0$ (grey) means the factor $1$; red means
    larger, blue smaller. (The scale factor $e^{a_4}$ of 3-space is the same at every $z$
    and needs no map: its logarithm grows from $0$ to $1.09$ along the time axis.)
    """),
    code(r'''
    x4_grid, z_grid2 = np.meshgrid(np.linspace(0.0, 2.5, 251),
                                   np.linspace(0.01, np.pi - 0.01, 300))
    a4_grid = A_value * H_value * x4_grid
    hidden_map = np.log10(np.exp(-rate_t * a4_grid) * np.abs(1 / np.tan(z_grid2)))
    extra_map = np.log10(np.exp(-rate_t * a4_grid) * np.abs(np.sin(z_grid2)) ** (1 / 6))
    fig, axes = plt.subplots(1, 2, figsize=(10.0, 4.2), sharey=True)
    for ax, data, title in zip(axes, [hidden_map, extra_map],
                               ["hidden: $e^{-a_4}b_4^{1/2}|\\cot z|$",
                                "extra time: $e^{-a_4}b_4^{1/2}(\\sin^2 z)^{1/12}$"]):
        mesh = ax.pcolormesh(x4_grid, z_grid2, data, cmap=DIVERGING, vmin=-1.5,
                             vmax=1.5, shading="auto")
        ax.contour(x4_grid, z_grid2, data, levels=[0.0], colors="black",
                   linewidths=1.0)
        ax.axhline(np.pi / 2, color="black", lw=0.8, ls=":")  # the fold
        ax.set_title(title)
        ax.set_xlabel("time $x_4$ (unit $1/H$)")
        ax.grid(False)
    axes[0].set_ylabel("$z = 6 H x_0$ (radians)")
    fig.colorbar(mesh, ax=axes, label="$\\log_{10}$ of the scale factor")
    save_figure(fig, "scale_factor_maps",
                "Maps of the logarithm to base 10 of the scale factor of the hidden "
                "direction $e^{-a_4}b_4^{1/2}|\\cot z| = e^{-a_4/3}|\\cot z|$ (left) and "
                "of an extra time $e^{-a_4}b_4^{1/2}(\\sin^2 z)^{1/12} = "
                "e^{-a_4/3}(\\sin^2 z)^{1/12}$ (right) along the deflating history "
                "$a_4 = x_4$, $b_4 = e^{4x_4/3}$; "
                "horizontal axes the time $x_4$ in units of $1/H$, vertical axes "
                "$z = 6Hx_0$ in radians across one cell $0 < z < \\pi$ (the dotted line "
                "is the fold $z = \\pi/2$), colour the value (red above $0$: lengths "
                "larger than the coordinate interval, blue below $0$: smaller, grey and "
                "the black line: factor $1$). As time goes on both shrink at every $z$ "
                "(the black lines move towards the tips), the hidden factor vanishes at "
                "the fold, and both maps are symmetric about the fold.")
    check(np.all(np.diff(hidden_map, axis=1) < 0) and np.all(np.diff(extra_map, axis=1) < 0),
          "along the history x0 and the extra times shrink at every z")
    '''),
    md(r"""
    ## 12. Proper volumes: 3-space inflates, the block of $x_0$ and the extra times deflates

    Take a box with coordinate edges $\Delta x_1 = \Delta x_2 = \Delta x_3 = 1$. Its
    proper 3-volume is the product of the three scale factors,
    $V_3 = (e^{a_4})^3 = e^{3a_4}$. The same box in the three extra times has the proper
    3-volume $V_t = f^3 (\sin^2 z)^{1/4} = b_4^{3/2} e^{-3a_4} (\sin^2 z)^{1/4}$. The
    slice $x_4 = \mathrm{const}$ is 7-dimensional ($x_0, x_1, x_2, x_3, x_5, x_6, x_7$);
    its volume factor is the product of the sizes of the seven scale factors other than
    $h_4 = 1$, which is $\sqrt{|\det g|} = e^{-a_4} b_4^2 |\cot z| (\sin^2 z)^{1/4}$:
    the factors $e^{3a_4}$ of 3-space and $f^4 = e^{-4a_4}b_4^2$ of the four deflating
    directions leave $e^{-a_4}b_4^2$. The next cell computes these products and, by an
    integral over one half cell $0 < z < \pi/2$, the proper 7-volume of the half cell per
    unit coordinate volume of the six directions $x_1, x_2, x_3, x_5, x_6, x_7$. On the
    half cell $\cot z > 0$ and $\sin z > 0$; with $s = \sin z$, $ds = \cos z\, dz$ and
    $dx_0 = dz/(6H)$:

    $$\int_0^{\pi/(12H)} \cot z\, \sin^{1/2} z\; dx_0 = \frac{1}{6H}\int_0^{\pi/2}
    \frac{\cos z}{\sin^{1/2} z}\, dz = \frac{1}{6H}\int_0^1 s^{-1/2}\, ds
    = \frac{1}{6H}\bigl[2 s^{1/2}\bigr]_0^1 = \frac{1}{3H},$$

    so the half cell has the proper 7-volume $e^{-a_4}b_4^2/(3H)$ (by the symmetries of
    section 7, every other half cell has the same).
    """),
    code(r'''
    V3 = sp.simplify(h[1] * h[2] * h[3])  # proper 3-volume of a unit coordinate box
    Vt = sp.simplify(h[5] * h[6] * h[7])  # the same in the three extra times
    # the 7-volume: the sizes of every scale factor except h[4] = 1 of the time x4
    V7 = f_hidden * abs_cot * V3 * Vt  # the size of h[0] is f |cot z|
    say(f"V3 = {plain(V3)},  Vt = {plain(Vt)}")
    check(sp.simplify(V7 - volume_factor) == 0
          and sp.simplify(sp.diff(sp.log(V7), x4) - (-a4_prime + 2 * b4_prime / b4)) == 0,
          "the 7-volume density is sqrt|det g| and changes with the rate -a4p + 2 b4p/b4")
    s = sp.symbols("s", positive=True)  # s = sin z on the half cell
    half_cell = sp.integrate(s ** sp.Rational(-1, 2), (s, 0, 1)) / (6 * H)
    say(f"proper 7-volume of a half cell per unit transverse coordinate volume = "
        f"e^(-a4) b4^2 times {half_cell}")
    check(half_cell == 1 / (3 * H),
          "a half cell has the proper 7-volume e^(-a4) b4^2/(3H) per unit coordinate "
          "volume")
    '''),
    md(r"""
    The next cell draws these volumes along the history at the fixed point
    $z = \pi/3$ (where $(\sin^2 z)^{1/4} = 0.9306$ and $|\cot z| = 0.5774$), on a
    logarithmic axis. On the history $f^3 = e^{-a_4}$, so $V_3$ grows like $e^{3x_4}$,
    $V_t$ shrinks like $e^{-x_4}$, their product like $e^{2x_4}$, and the 7-volume
    density, which also contains the hidden factor $f|\cot z|$, grows like
    $e^{2x_4}e^{-x_4/3} = e^{5x_4/3}$: the inflation of 3-space wins over the
    deflation of the four directions of the block.
    """),
    code(r'''
    z_fixed = np.pi / 3
    f_line = np.exp(-rate_t * a4_line)  # f = e^(-a4/3) on the history
    v3 = np.exp(3 * a4_line)
    vt = f_line ** 3 * np.abs(np.sin(z_fixed)) ** 0.5
    v7 = v3 * vt * f_line * np.abs(1 / np.tan(z_fixed))
    fig, ax = plt.subplots()
    ax.plot(x4_line, v3, color=RED, lw=1.8, label="$V_3 = e^{3a_4}$")
    ax.plot(x4_line, vt, color=BLUE, lw=1.8, ls="--",
            label="$V_t = f^3(\\sin^2 z)^{1/4}$")
    ax.plot(x4_line, v3 * vt, color=ORANGE, lw=1.8, ls="-.",
            label="$V_3 V_t = e^{3a_4}f^3(\\sin^2 z)^{1/4}$")
    ax.plot(x4_line, v7, color="black", lw=1.2, ls=":",
            label="7-volume density $e^{-a_4}b_4^2|\\cot z|(\\sin^2 z)^{1/4}$")
    ax.set_yscale("log")
    ax.set_xlabel("time $x_4$ (unit $1/H$), history $a_4 = x_4$, "
                  "$b_4 = e^{4x_4/3}$")
    ax.set_ylabel("proper volume per unit coordinate volume")
    ax.set_title("Proper volumes at $z = \\pi/3$")
    ax.legend(fontsize=8)
    save_figure(fig, "proper_volumes",
                "Proper volumes per unit coordinate volume at the fixed hidden position "
                "$z = \\pi/3$ along the history $a_4 = x_4$, $b_4 = e^{4x_4/3}$ "
                "($f = e^{-a_4/3}$), on a logarithmic vertical "
                "axis; horizontal axis the time $x_4$ in units of $1/H$. The proper "
                "3-volume of 3-space $V_3$ (solid red) grows like $e^{3x_4}$, the proper "
                "3-volume of the three extra times $V_t$ (dashed blue) shrinks like "
                "$e^{-x_4}$, their product (dash-dotted, $0.931$ at $x_4 = 0$) grows "
                "like $e^{2x_4}$, and the density of the proper 7-volume (dotted, "
                "$0.537$ at $x_4 = 0$), which also contains the shrinking hidden "
                "factor, grows like $e^{5x_4/3}$.")
    at_start = 0.75 ** 0.25 / 3 ** 0.5  # (sin^2 z)^(1/4) |cot z| at z = pi/3
    check(np.max(np.abs(v7 / (at_start * np.exp(5.0 * a4_line / 3.0)) - 1.0)) < 1e-12,
          "the 7-volume density at z = pi/3 grows like e^(5 a4/3) along the history")
    '''),
    md(r"""
    ## 13. The hidden coordinate $y$: one block of the hidden direction and the extra times

    The entry $e^{-2a_4} b_4 \cot^2 z$ makes the hidden direction awkward. The Revision
    Kohn-Sham work uses the coordinate $y = \ln|\sin z|/(6H) = \ln(\sin^2 z)/(12H)$. Line
    by line: the chain rule gives
    $dy/dx_0 = \frac{1}{12H}\,\frac{2\sin z\cos z}{\sin^2 z}\, 6H = \cot z$, so
    $dy^2 = \cot^2 z\, dx_0^2$ and $g_{00}\, dx_0^2 = f^2 dy^2$: a step $dy$ has the
    proper length $f\,dy$. Next, $12Hy = \ln \sin^2 z$ gives $\sin^2 z = e^{12Hy}$
    ($e$ to the power of both sides), so the warp factor of the extra times is
    $W = (\sin^2 z)^{1/12} = e^{Hy}$ and its square is $W^2 = e^{2Hy}$. Hence

    $$ds^2 = e^{2a_4}(dx_1^2 + dx_2^2 + dx_3^2) - dx_4^2
    + f^2\bigl[dy^2 - e^{2Hy}(dx_5^2 + dx_6^2 + dx_7^2)\bigr], \qquad
    f = e^{-a_4} b_4^{1/2} :$$

    the hidden direction and the three extra times form one **block** with the common
    factor $f^2$. On every half cell $y$ runs from $-\infty$ (the tip) to $0$ (the fold).
    In the coordinates $(y, x_1, \dots, x_7)$ the volume factor is
    $f \cdot e^{3a_4} \cdot f^3 e^{3Hy} = e^{-a_4} b_4^2 e^{3Hy}$. The Kohn-Sham record
    writes its line element and its volume factor in exactly this form.

    The next cell prints four statements of the record
    `Revision/kohn_sham/ks-theory.json` (read in section 10): the definition of $y$, the
    line element, the warp factor and the volume factor. Then it checks them with sympy;
    the checks also require that the record still writes them in these words. To write
    the metric in the coordinate $y$ it uses, on each of the four quarters of the period,
    the inverse relation: $z = \arcsin(e^{6Hy})$, $\pi - \arcsin(e^{6Hy})$,
    $\pi + \arcsin(e^{6Hy})$ and $-\arcsin(e^{6Hy})$; the hidden entry becomes
    $g_{00}\,(dx_0/dy)^2$ (because $dx_0 = (dx_0/dy)\,dy$), and the seven entries
    $g_{11}, \dots, g_{77}$ only need $|\sin z| = e^{6Hy}$ put in. The cell checks the
    form on all four quarters, for every $a_4$ and $b_4$.
    """),
    code(r'''
    geometry = ks_theory["geometry"]  # the statements of the record about the geometry
    for key in ("hiddenCoordinate", "lineElement", "warp", "sqrtDetG"):
        say(f"record, {key}: {geometry[key]}")
    y_of_x0 = sp.log(sp.sin(6 * H * x0) ** 2) / (12 * H)  # y = ln|sin z|/(6H)
    dy_dx0 = sp.diff(y_of_x0, x0)  # the chain rule, done by sympy
    say(f"dy/dx0 = {plain(dy_dx0)}")
    record_check(LEAD_EMT, "ks_coordinate_jacobian")  # stops if not passed
    check(sp.simplify(dy_dx0 - sp.cot(6 * H * x0)) == 0,
          "dy/dx0 = cot z",
          record=f"{LEAD_EMT}, check ks_coordinate_jacobian")
    check(sp.simplify(f_hidden ** 2 * dy_dx0 ** 2 - g[0, 0]) == 0,
          "g00 dx0^2 = f^2 dy^2: a step dy has the proper length f dy")
    check(sp.simplify(sp.exp(H * y_of_x0) - twelfth) == 0,
          "the warp factor W = (sin^2 z)^(1/12) equals e^(H y)")
    y = sp.symbols("y", negative=True)  # the hidden coordinate, y < 0 off the fold
    arcsine = sp.asin(sp.exp(6 * H * y))
    W = sp.exp(H * y)  # the warp factor in the coordinate y
    block = sp.diag(*([f_hidden ** 2] + [sp.exp(2 * a4)] * 3 + [-1]
                      + [-f_hidden ** 2 * W ** 2] * 3))  # the form of the record
    same_form = []
    for z_of_y in (arcsine, sp.pi - arcsine, sp.pi + arcsine, -arcsine):
        x0_of_y = z_of_y / (6 * H)  # the inverse on one quarter
        dx0_dy = sp.diff(x0_of_y, y)  # dx0/dy
        g_y = sp.diag(g[0, 0].subs(x0, x0_of_y) * dx0_dy ** 2,
                      *[g[k, k].subs(x0, x0_of_y) for k in range(1, 8)])
        same_form.append((g_y - block).applyfunc(sp.simplify) == sp.zeros(8, 8))
    for k in (0, 1, 4, 5):
        say(f"  in the coordinate y: g[{k}, {k}] = {plain(block[k, k])}")
    check(all(same_form) and len(same_form) == 4
          and geometry["warp"].startswith("W(y) = e^{Hy} on the extra times only")
          and "f(x4)^2 [dy^2 - e^{2Hy} (dx5^2+dx6^2+dx7^2)]" in geometry["lineElement"],
          "on all four quarters the metric in y is the block form of the record, with "
          "f = e^(-a4) b4^(1/2) and W = e^(H y)",
          record="Revision/kohn_sham/ks-theory.json, geometry.lineElement and "
                 "geometry.warp")
    root = sp.exp(-a4) * b4 ** 2 * sp.exp(3 * H * y)  # positive: compare the squares
    check(sp.simplify(block.det() - root ** 2) == 0
          and geometry["sqrtDetG"].startswith("e^{-a4} b4^2 e^{3Hy}"),
          "in the coordinate y, sqrt|det g| is e^(-a4) b4^2 e^(3 H y), as the record "
          "states",
          record="Revision/kohn_sham/ks-theory.json, geometry.sqrtDetG")
    # the proper distance from the fold is f (0 - y); -y grows without bound at the tip
    check(sp.limit(-y_of_x0, x0, 0, "+") == sp.oo,
          "the tip z -> 0 lies at y -> minus infinity: infinitely far from the fold")
    '''),
    md(r"""
    The Revision Kohn-Sham solver keeps only the part $-L \le y \le 0$ of each half cell,
    with the tip cut-off $L = 3/H$ read in section 10; its proper hidden length is $fL$
    (record key `geometry.hiddenScale`). How much of the 7-volume does the cut-off
    remove? In $y$ the 7-volume density is $e^{-a_4} b_4^2 e^{3Hy}$, and the factor
    $e^{-a_4} b_4^2$ cancels in a fraction, so the fraction of the 7-volume beyond the
    cut-off is
    $\int_{-\infty}^{-L} e^{3Hy} dy \big/ \int_{-\infty}^{0} e^{3Hy} dy = e^{-3HL}$,
    which is $e^{-9} \approx 1.2 \times 10^{-4}$ for $L = 3/H$. The cut-off lies at the
    tiny angle $z = \arcsin e^{-18} \approx 1.5 \times 10^{-8}$. The next cell computes
    the fraction with sympy and draws $y$ as a function of $z$ on the first half cell
    (left; the $z$ axis is logarithmic, so that the region near the tip is visible:
    there $y \approx \ln(z)/(6H)$ is a straight line) and the warp factor
    $W = e^{Hy}$, its square $W^2 = e^{2Hy}$ and the volume density $e^{3Hy}$ (in the
    unit $e^{-a_4}b_4^2$, which does not depend on $y$) as functions of $y$ (right).
    """),
    code(r'''
    L_exact = sp.nsimplify(L_tip)  # the number 3.0 of the record as the exact integer 3
    y_any = sp.symbols("y_any", real=True)  # y as a real variable of integration
    fraction = sp.integrate(sp.exp(3 * H * y_any), (y_any, -sp.oo, -L_exact / H)) \
        / sp.integrate(sp.exp(3 * H * y_any), (y_any, -sp.oo, 0))
    fraction = sp.simplify(fraction.subs(H, 1))
    report("fraction of the 7-volume beyond the tip cut-off y = -3", sp.sstr(fraction),
           f"= {float(fraction):.4e}")
    z_cut = float(sp.asin(sp.exp(-18)))  # the angle z of the cut-off, sin z = e^(-18)
    report("angle z of the tip cut-off", f"{z_cut:.4e}", "radians")
    say("record, hiddenScale: " + geometry["hiddenScale"])
    z_line = np.logspace(-10, np.log10(np.pi / 2), 800)  # 1e-10 ... pi/2, evenly in log
    y_line = np.log(np.sin(z_line)) / 6.0  # with H = 1
    fig, axes = plt.subplots(1, 2, figsize=(10.0, 4.2))
    axes[0].plot(z_line, y_line, color=VIOLET, lw=1.8, label="$y(z)$")
    axes[0].axhline(-L_tip, color="black", lw=1.0, ls="--",
                    label=f"tip cut-off $y = -L = -{L_tip:g}$")
    axes[0].plot([z_cut], [-L_tip], "o", color="black", ms=6)
    axes[0].set_xscale("log")
    axes[0].set_xlabel("$z = 6 H x_0$ (radians, logarithmic axis)")
    axes[0].set_ylabel("$y = \\ln|\\sin z|/(6H)$ (unit $1/H$)")
    axes[0].set_title("The hidden coordinate $y$ on a half cell")
    axes[0].legend(fontsize=8)
    y_axis = np.linspace(-4.0, 0.0, 400)
    axes[1].plot(y_axis, np.exp(y_axis), color=RED, lw=1.8,
                 label="warp factor $W = e^{Hy} = (\\sin^2 z)^{1/12}$")
    axes[1].plot(y_axis, np.exp(2 * y_axis), color=ORANGE, lw=1.8, ls="-.",
                 label="$W^2 = e^{2Hy} = (\\sin^2 z)^{1/6}$")
    axes[1].plot(y_axis, np.exp(3 * y_axis), color=AQUA, lw=1.8, ls="--",
                 label="7-volume density per $e^{-a_4}b_4^2$: $e^{3Hy}$")
    axes[1].axvspan(-4.0, -L_tip, color="grey", alpha=0.25,
                    label="removed by the tip cut-off")
    axes[1].set_xlabel("$y$ (unit $1/H$)")
    axes[1].set_ylabel("value (no unit)")
    axes[1].set_title("Warp and volume density in $y$")
    axes[1].legend(fontsize=8, loc="upper left")
    save_figure(fig, "hidden_coordinate_y",
                "The hidden coordinate $y = \\ln|\\sin z|/(6H)$ with $H = 1$. Left: $y$ "
                "versus $z = 6Hx_0$ in radians on a logarithmic axis from $10^{-10}$ to "
                "$\\pi/2$ (the half cell next to the tip $z = 0$); $y$ is $0$ at the "
                "fold $z = \\pi/2$ and falls without bound towards the tip $z \\to 0$, "
                "along the straight line "
                "$y \\approx \\ln(z)/6$; the dashed line and the dot mark the tip cut-off "
                "$y = -3$ of the Revision Kohn-Sham solver, at $z = 1.5 \\times "
                "10^{-8}$. Right: the warp factor $W = e^{Hy}$ of the extra times "
                "(solid), its square $W^2 = e^{2Hy}$ (dash-dotted) and the density "
                "$e^{3Hy}$ of the proper 7-volume in the unit $e^{-a_4}b_4^2$ (dashed) "
                "versus $y$ in units of $1/H$; the grey band beyond the cut-off holds "
                "only the fraction $e^{-9} = 1.2 \\times 10^{-4}$ of the 7-volume of the "
                "half cell.")
    check(fraction == sp.exp(-9), "the cut-off removes exactly the fraction e^(-9)")
    '''),
    md(r"""
    ## 14. The last check

    The last cell checks that the seven figure files exist in the folder
    Revision/textbook/figures and prints the number of checks that passed.
    """),
    code(r'''
    figure_names = ["metric_heat_map", "diagonal_entries", "history_scale_factors",
                    "hidden_direction", "scale_factor_maps", "proper_volumes",
                    "hidden_coordinate_y"]
    files = [output_file(f"{FIGURE_FOLDER}/03a_{k}_{n}.png")
             for k, n in enumerate(figure_names, 1)]
    check(all(path.is_file() for path in files), "all seven figure files exist")
    all_checks_passed()
    '''),
    md(r"""
    ## 15. What this notebook showed

    - The corrected metric was read **exactly as the Revision record stores it**, and
      the text agrees with the formula and with the record of the Rust program
      `lovelock_gkd` (all 8 diagonal entries; the 56 other entries are zero).
    - $\det g = e^{-2a_4} b_4^4 \cot^2 z\,|\sin z|$ and
      $\sqrt{|\det g|} = e^{-a_4} b_4^2 |\cot z| (\sin^2 z)^{1/4}$: PROVED here by exact
      algebra (and in the Revision record); it vanishes at the fold $\cos z = 0$.
    - The signature is (4,4) at every real $z$ with $\sin z \cos z \neq 0$: $x_0, x_1,
      x_2, x_3$ are space-like, $x_4, x_5, x_6, x_7$ time-like. The metric repeats with
      the period $\pi$ in $z$ and is symmetric under $z \to \pi - z$, the reflection
      across the fold that joins the two halves of a cell.
    - The diagonal vielbein $h = (f\cot z, e^{a_4}\ (\times 3), 1,
      f(\sin^2 z)^{1/12}\ (\times 3))$, $f = e^{-a_4}b_4^{1/2}$, reproduces the metric.
    - 3-space expands with the rate $a_4'$; the hidden direction and the three extra
      times **deflate** together with the rate $-a_4' + b_4'/(2b_4)$; along the
      prescribed history $a_4 = x_4$, $b_4 = e^{4x_4/3}$ ($A = 1$, $H = 1$,
      $b_4(0) = 1$, $\beta = 4/3$) 3-space lengths grow by $e^2 = 7.39$ and the factor
      $f$ of the block shrinks to $e^{-2/3} = 0.513$ between the first and the last
      slice.
    - The proper 3-volume of 3-space grows like $e^{3a_4}$, that of the extra times
      shrinks like $b_4^{3/2} e^{-3a_4}$, and the 7-volume density
      $e^{-a_4}b_4^2|\cot z|(\sin^2 z)^{1/4}$ changes with the rate
      $-a_4' + 2b_4'/b_4$ (on the history like $e^{5a_4/3}$); a half cell has the
      7-volume $e^{-a_4}b_4^2/(3H)$ per unit transverse coordinate volume.
    - In the hidden coordinate $y = \ln|\sin z|/(6H)$ the hidden direction and the extra
      times form one block $f^2[dy^2 - e^{2Hy}(dx_5^2 + dx_6^2 + dx_7^2)]$, as in the
      Revision record, on all four quarters of the period; the volume factor is
      $e^{-a_4}b_4^2e^{3Hy}$; the tip is at infinite proper distance, and the tip
      cut-off $y = -3/H$ of the Kohn-Sham solver removes only the fraction $e^{-9}$ of
      the 7-volume of a half cell.
    - ASSUMED: the history $a_4 = A H x_4$, $b_4 = b_4(0)\,e^{\beta A H x_4}$ is a
      prescribed background (the Revision record says so in its own words), used here
      only to draw the time dependence; the field equations of $a_4$ and $b_4$ come
      later. Nothing is computed at the degenerate points $\sin z \cos z = 0$.
    """),
]

if __name__ == "__main__":
    raise SystemExit(run_builder(__file__))
