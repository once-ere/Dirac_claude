#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
"""Builder of Notebook 03a, "The author's metric" (textbook "Universes in Pairs").

The notebook Revision/textbook/notebooks/03a_authors_metric.ipynb is BUILT from this
file by Revision/textbook/tools/nbkit.py (never edit the .ipynb by hand):

    python Revision/textbook/tools/nbkit.py build \
        Revision/textbook/notebooks/src/03a_authors_metric.py --date YYYY-MM-DD
    python Revision/textbook/tools/nbkit.py check \
        Revision/textbook/notebooks/src/03a_authors_metric.py

Physics source: Revision/SPEC.md section 1 (the metric of the author, coordinates x0..x7,
the three extra times x5, x6, x7 DEFLATE exponentially) and the Revision records named in
FACTS["records"].  Every number the notebook compares with a record is checked by an
assertion that names the record file and its check.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools"))
from nbkit import code, md, run_builder  # noqa: E402

FIG = "Revision/textbook/figures/03a"

FACTS = {
    "id": "03a",
    "name": "03a_authors_metric",
    "title": "The author's metric: signature, scale factors, warp and proper volumes",
    "purpose": (
        "It reads the metric of the primordial gravitational field exactly as the author "
        "typed it, with the two metric functions a4 and b4 (from the Revision record of the "
        "curvature computation), turns the text into an exact sympy matrix, and checks its "
        "diagonal entries, its determinant, its signature (4,4) and its diagonal vielbein "
        "against the Revision records. It then computes the expansion rate of every "
        "direction, the proper volumes and the hidden coordinate y, and draws the metric as "
        "a heat map, its entries versus z, the scale factors of 3-space (inflating) and of "
        "the three extra times (deflating exponentially) along the deflating history "
        "a4 = A H x4, b4 = b4(0) e^(beta A H x4) with beta = 4/3 of the Revision Kohn-Sham "
        "work, the warp factor and the proper volumes."
    ),
    "records": [
        ["Revision/gkd_lovelock/results/curvature.json",
         "the metric with b4 as the author wrote it (metricAsGiven), its diagonal entries "
         "(metricDiagonal) and the square root of the absolute value of its determinant "
         "(sqrtAbsDetG), written by the Rust program lovelock_gkd"],
        ["Revision/gkd_lovelock/results/python-lovelock-report.json",
         "the independent sympy verification of that program; its check sqrt_abs_det_g"],
        ["Revision/lead_checks/reports/emt-divergence-and-spin-connection.json",
         "the checks vielbein_reproduces_metric and ks_coordinate_jacobian"],
        ["Revision/kohn_sham/results/parameters.json",
         "the deflating history a4 = A H x4, b4 = b4(0) e^(beta A H x4) with A = 1, H = 1 "
         "and beta = 4/3, its five slices of a4 and the tip cut-off L of the Revision "
         "Kohn-Sham solver"],
        ["Revision/kohn_sham/ks-theory.json",
         "the definition of the hidden coordinate y, the patch end and the tip, the line "
         "element in y with the warp factor W = e^(H y) and the volume factor "
         "b4^(3/2) e^(6 H y), and the status of the history (a prescribed background, not "
         "solved for)"],
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
        "ALL 29 CHECKS PASSED (notebook 03a)",
    ],
    "troubleshooting": [
        ["\"FileNotFoundError\" for curvature.json, python-lovelock-report.json, "
         "emt-divergence-and-spin-connection.json, parameters.json or ks-theory.json",
         "the notebook reads these five Revision records of the repository, so the "
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
    $8 \times 8$ matrix that the author wrote down and on which every later computation
    of the book is built. It

    - reads the metric **exactly as the author typed it** (the text is stored in the
      Revision record `Revision/gkd_lovelock/results/curvature.json`) and turns the text
      into an exact sympy matrix, step by step;
    - checks the eight diagonal entries, the determinant $\det g = b_4^3 \cos^2 z$ and
      $\sqrt{|\det g|} = b_4^{3/2} \cos z$ against the Revision records;
    - checks the **signature** (4,4): four space-like directions $x_0, x_1, x_2, x_3$ and
      four time-like directions $x_4, x_5, x_6, x_7$;
    - builds the diagonal **vielbein** (the scale factors) and checks that it reproduces
      the metric;
    - computes the **expansion rate** of every direction: 3-space expands with the rate
      $a_4'$, the three extra times shrink (deflate) with the rate $-a_4' + b_4'/(2b_4)$;
    - draws the scale factors along the **deflating history** $a_4 = A H x_4$,
      $b_4 = b_4(0)\,e^{\beta A H x_4}$ that the Revision Kohn-Sham work uses as a
      prescribed background ($A = 1$, $H = 1$, $\beta = 4/3$);
    - computes the **proper volumes** (3-space grows like $e^{3 a_4}$, the extra times
      shrink like $b_4^{3/2} e^{-3 a_4}$, the 7-volume density $b_4^{3/2}\cos z$ follows
      $b_4$) and
      the **hidden coordinate** $y = \ln(\sin z)/(6H)$ in which the metric takes its
      warped form;
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
      entries. The author's metric has signature (4,4).
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
      factors.
    - **Expansion rate** (Hubble rate) of a direction: $\partial_{x_4} \ln h_\mu$, the
      fraction by which its lengths grow per unit of time $x_4$.
    - **Inflate, deflate**: grow, shrink exponentially. 3-space inflates; the extra
      times deflate.
    - $z = 6 H x_0$: the hidden coordinate in angle form, between $0$ and $\pi/2$.
    - **Patch**: the range $0 < z < \pi/2$ on which the metric is used. Its end
      $z = \pi/2$ is the **patch end**; the end $z \to 0$ is the **tip**.
    - **Warp factor** $W = \sin^{1/6} z$: the factor that the scale factors of the six
      **transverse** directions $x_1, x_2, x_3, x_5, x_6, x_7$ share; the six transverse
      entries $g_{11}, g_{22}, g_{33}, g_{55}, g_{66}, g_{77}$ of the metric contain its
      square $W^2 = \sin^{1/3} z$.
    - **Hidden coordinate** $y = \ln(\sin z)/(6H)$: a second coordinate for the hidden
      direction, in which the warp factor is $W = e^{Hy}$ (section 13).
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

    The author's metric of the primordial gravitational field is diagonal. In the order
    $x_0, \dots, x_7$ its diagonal entries are

    $$g = \mathrm{diag}\bigl(\cot^2 z,\ e^{2a_4}\sin^{1/3}z,\ e^{2a_4}\sin^{1/3}z,\
    e^{2a_4}\sin^{1/3}z,\ -1,\ -b_4 e^{-2a_4}\sin^{1/3}z,\ -b_4 e^{-2a_4}\sin^{1/3}z,\
    -b_4 e^{-2a_4}\sin^{1/3}z\bigr),\qquad z = 6 H x_0 .$$

    Here $H > 0$ is a constant of the author (a number with the unit 1/length), and
    $a_4 = a_4(x_4)$ and $b_4 = b_4(x_4) > 0$ are functions of the time $x_4$ only, the
    **metric functions**; $b_4$ is the author's change of 2026-10-14 (the metric used
    before, with $b_4 = 1$, is withdrawn: $b_4$ is never 1). A prime means the derivative
    with respect to $x_4$:
    $a_4' = d a_4 / d x_4$, $b_4' = d b_4 / d x_4$.

    The line element is therefore

    $$ds^2 = \cot^2 z\, dx_0^2 + e^{2a_4}\sin^{1/3}z\,(dx_1^2 + dx_2^2 + dx_3^2) - dx_4^2
    - b_4 e^{-2a_4}\sin^{1/3}z\,(dx_5^2 + dx_6^2 + dx_7^2) .$$

    Read it term by term. A step $dx_1$ in 3-space has the proper length
    $e^{a_4}\sin^{1/6} z\, dx_1$: when $a_4$ grows, 3-space **inflates**. A step $dx_5$
    along an extra time has the proper duration $b_4^{1/2} e^{-a_4}\sin^{1/6} z\, dx_5$:
    it shrinks at the rate $a_4' - b_4'/(2b_4)$, and along the history used below (where
    $b_4'/b_4 = \tfrac43 a_4'$) at the rate $a_4'/3$: the extra times **deflate
    exponentially**. The time $x_4$ has the coefficient
    $-1$, so a step $dx_4$ is a proper time interval of exactly $dx_4$: the clock of an
    observer at rest shows $x_4$. The hidden direction has the coefficient $\cot^2 z$,
    which depends on $x_0$ only.

    The metric alone does not fix the functions $a_4(x_4)$ and $b_4(x_4)$; the field
    equations of $a_4$ and $b_4$, derived later in the book, relate them to the energy
    and the pressures of the matter that fills the spacetime (with the author's Lovelock
    weights every vacuum solution has a constant $b_4$, which is excluded). For the plots
    this notebook uses the history of the Revision Kohn-Sham work,
    $a_4 = A H x_4$ and $b_4 = b_4(0)\,e^{\beta A H x_4}$ with $A = 1$, $\beta = 4/3$
    and the unit of length chosen so that $H = 1$ (`Revision/SPEC.md`, section 1). This
    history is a **prescribed background** (it is assumed, not solved for). With
    $A > 0$ the function $a_4$ increases, so the extra times deflate, as the author
    requires.
    """),
    md(r"""
    ## 5. Reading the metric exactly as the author wrote it

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
    the Revision record, stored the author's text of the metric in its output file
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
    # the metric exactly as the author typed it, then a note in brackets
    author_text, note = record["metricAsGiven"].split("}} ", 1)
    author_text += "}}"  # the two closing brackets that split removed
    say(f"The metric as the author wrote it ({len(author_text)} characters):")
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
    $6 H x_0$.
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
    z = sp.symbols("z", positive=True)  # z = 6 H x0, for printing


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
    The next cell turns the author's text into Python, one rule at a time, and lets
    sympy read the result. Each `replace` changes one piece of Mathematica notation into
    the Python notation that sympy understands: `exp^` (which an older text of the
    author used) becomes `E^` (sympy's `E` is the number $e = 2.718\ldots$), the square
    brackets of `Sin[6 H x0]` and `Cot[6 H x0]` become round brackets, `a4[x4]` and
    `b4[x4]` become `a4` and `b4` (which the dictionary `names` connects to the functions
    $a_4(x_4)$ and $b_4(x_4)$), the curly brackets of the lists become square brackets,
    and the power sign `^` becomes `**`. The option `implicit_multiplication` reads a
    blank between two factors as a multiplication, as Mathematica does: `6 H x0` means
    $6 \cdot H \cdot x_0$.
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
             "cot": sp.cot}
    rows = parse_expr(text, local_dict=names,
                      transformations=standard_transformations + (implicit_multiplication,))
    g = sp.Matrix(rows)  # the metric of the author as an exact 8 x 8 sympy matrix
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
    such a record entry into sympy with the same rules as above; the check that no
    square bracket is left proves that every piece of notation was translated.
    """),
    code(r'''
    warp = sp.sin(6 * H * x0) ** sp.Rational(1, 3)  # sin(z)^(1/3), Rational: exact 1/3
    typed = sp.diag(sp.cot(6 * H * x0) ** 2,  # the author's order x0, x1, ..., x7
                    sp.exp(2 * a4) * warp, sp.exp(2 * a4) * warp, sp.exp(2 * a4) * warp,
                    -1,
                    -b4 * sp.exp(-2 * a4) * warp, -b4 * sp.exp(-2 * a4) * warp,
                    -b4 * sp.exp(-2 * a4) * warp)
    difference = (g - typed).applyfunc(sp.simplify)  # simplify every entry
    check(difference == sp.zeros(8, 8),
          "the text of the author equals the metric typed by hand from the formula")


    def from_mathematica(entry_text):
        """A record entry in Mathematica notation, as a sympy expression."""
        t = entry_text.replace("Sin[6*H*x0]", "sin(6*H*x0)")
        t = t.replace("Cot[6*H*x0]", "cot(6*H*x0)")
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

    $$\det g = \cot^2 z \cdot \bigl(e^{2a_4}\sin^{1/3}z\bigr)^3 \cdot (-1) \cdot
    \bigl(-b_4 e^{-2a_4}\sin^{1/3}z\bigr)^3 .$$

    Line by line: $\bigl(e^{2a_4}\sin^{1/3}z\bigr)^3 = e^{6a_4}\sin z$ (a power of a
    product is the product of the powers); $\bigl(-b_4 e^{-2a_4}\sin^{1/3}z\bigr)^3 =
    -b_4^3 e^{-6a_4}\sin z$ (an odd power keeps the minus sign); the two minus signs
    multiply to $+1$ and $e^{6a_4} e^{-6a_4} = 1$, so $\det g = b_4^3 \sin^2 z \cot^2 z$;
    and $\cot z = \cos z / \sin z$ gives $\det g = b_4^3 \cos^2 z$. On the patch
    $0 < z < \pi/2$ the cosine is positive, so $\sqrt{|\det g|} = b_4^{3/2} \cos z$.
    The function $a_4$ has dropped out: the volume factor changes with time only through
    $b_4$, and not at all when $b_4$ is constant. The next cell lets sympy do the same and
    compares with the record (`sqrtAbsDetG`, written there as
    `Sin[6*H*x0]*Cot[6*H*x0]*b4[x4]^(3/2)`); then it compares numbers at seven points with
    $b_4 = 2$ (any positive value would do).
    """),
    code(r'''
    det_g = g.det()  # the product of the diagonal entries; sympy cancels exp(6 a4)
    say(f"det g = {plain(det_g)}")
    record_check("Revision/gkd_lovelock/results/python-lovelock-report.json",
                 "sqrt_abs_det_g", "det g = b4^3 cos^2(6 H x0) exactly")  # stops if not
    check(sp.simplify(det_g - b4 ** 3 * sp.cos(6 * H * x0) ** 2) == 0,
          "det g = b4^3 cos(z)^2: the function a4 drops out",
          record="Revision/gkd_lovelock/results/python-lovelock-report.json, "
                 "check sqrt_abs_det_g")
    # sqrt|det g| on the patch, where cos z > 0 and b4 > 0
    volume_factor = b4 ** sp.Rational(3, 2) * sp.cos(6 * H * x0)
    check(sp.simplify(from_mathematica(record["sqrtAbsDetG"]) - volume_factor) == 0,
          "sqrt|det g| = b4^(3/2) sin(z) cot(z) = b4^(3/2) cos(z)",
          record=f"{CURVATURE_RECORD}, sqrtAbsDetG")
    # numbers: sqrt(|det g|) at 7 points of the patch with b4 = 2, against 2^(3/2) cos z
    z_points = np.linspace(0.1, 1.5, 7)
    det_numbers = np.array([float(det_g.subs(b4, 2).subs({H: 1, x0: zp / 6}))
                            for zp in z_points])
    check(np.max(np.abs(np.sqrt(np.abs(det_numbers)) - 2 ** 1.5 * np.cos(z_points))) < 1e-13,
          "at b4 = 2, sqrt|det g| equals 2^(3/2) cos z at 7 points of the patch")
    '''),
    md(r"""
    ## 7. The signature (4,4)

    For a diagonal matrix the eigenvalues are the diagonal entries, so the signature is
    read off the signs of the eight entries. The next cell turns the eight entries into
    fast numerical functions of $z$ and of the values of $a_4$ and $b_4$
    (`sp.lambdify`), evaluates them on a grid of 400 values of $z$ strictly inside the
    patch, 13 values of $a_4$ from $-3$ to $3$ and the three values $b_4 = 0.5$, 2 and 4,
    and checks that the sign pattern is always that of $\eta = (+,+,+,+,-,-,-,-)$: four
    positive and four negative entries. It also checks two vectors: a step along $x_1$ has
    a positive squared length (space-like), a step along $x_5$ a negative one
    (time-like). Where a single point is needed, this notebook takes the point of the
    deflating history of section 10 at $a_4 = 0.5$: there $b_4 = b_4(0)\,e^{(4/3)a_4}
    = e^{2/3}\,b_4(0) = 1.948\,b_4(0)$, with $b_4(0)$ as the unit of $b_4$ (a constant
    factor of $b_4$ only rescales $x_5, x_6, x_7$).
    """),
    code(r'''
    ETA = np.array([1, 1, 1, 1, -1, -1, -1, -1])  # the flat metric diag(+,+,+,+,-,-,-,-)
    B4_POINT = float(np.exp(2.0 / 3.0))  # b4 on the history at a4 = 0.5, unit b4(0)
    # the entries as functions of z, a4v and b4v
    diagonal_z = [plain(g[k, k]) for k in range(8)]
    functions = [sp.lambdify((z, a4v, b4v), entry, "numpy") for entry in diagonal_z]


    def diagonal_values(z_values, a4_value, b4_value=B4_POINT):
        """The 8 diagonal entries at the points z_values (one row per entry)."""
        return np.array([np.broadcast_to(f(z_values, a4_value, b4_value), z_values.shape)
                         for f in functions], dtype=float)


    z_grid = np.linspace(0.0, np.pi / 2, 402)[1:-1]  # 400 points strictly inside
    patterns = set()
    for b4_value in (0.5, 2.0, 4.0):
        for a4_value in np.linspace(-3.0, 3.0, 13):
            # +1 or -1 for each entry
            signs = np.sign(diagonal_values(z_grid, a4_value, b4_value))
            patterns.update(tuple(int(s) for s in column) for column in signs.T)
    say(f"sign patterns found on the grid: {sorted(patterns)}")
    check(patterns == {tuple(int(s) for s in ETA)},
          "on the whole grid the signs are (+,+,+,+,-,-,-,-): signature (4,4)")
    step_x1 = diagonal_values(np.array([0.7]), 0.5)[1, 0]  # g11: step along x1
    step_x5 = diagonal_values(np.array([0.7]), 0.5)[5, 0]  # g55: step along x5
    say(f"at z = 0.7, a4 = 0.5, b4 = e^(2/3): g11 = {step_x1:.6f} (space-like), "
        f"g55 = {step_x5:.6f} (time-like)")
    check(step_x1 > 0 > step_x5, "a step along x1 is space-like, along x5 time-like")
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
                "The author's metric $g_{\\mu\\nu}$ at the point $z = 6Hx_0 = \\pi/4$ "
                "with $a_4 = 0.5$ and $b_4 = e^{2/3}$ (the deflating history at "
                "$a_4 = 0.5$, unit $b_4(0)$), drawn as a heat map: row $\\mu$ and "
                "column $\\nu$ run "
                "over the coordinates $x_0$ to $x_7$, red squares are positive entries, "
                "blue squares negative ones, grey squares zero; the number in each "
                "square is the entry. Only the diagonal is non-zero; the hidden entry is "
                "$\\cot^2(\\pi/4) = 1$, the three 3-space "
                "entries are equal, $e^{1}\\,(\\sin \\pi/4)^{1/3} = 2.422$, the three "
                "extra-time entries are equal, $-e^{2/3}e^{-1}(\\sin \\pi/4)^{1/3} = "
                "-0.638$, and the time entry is $-1$: "
                "four positive and four negative entries, the signature (4,4).")
    check(abs(values[1, 1] - np.e * np.sin(np.pi / 4) ** (1 / 3)) < 1e-12
          and abs(values[5, 5] + np.exp(-1.0 / 3.0) * np.sin(np.pi / 4) ** (1 / 3)) < 1e-12,
          "at z = pi/4, a4 = 0.5, b4 = e^(2/3): g11 = e (sin pi/4)^(1/3) and "
          "g55 = -e^(-1/3) (sin pi/4)^(1/3)")
    '''),
    md(r"""
    The next cell draws the eight diagonal entries as functions of $z$ across the whole
    patch, for $a_4 = 0.5$ and $b_4 = e^{2/3}$, together with the determinant divided by
    its constant factor $b_4^3$, $\det g/b_4^3 = \cos^2 z$.
    Entries that are equal are drawn as one curve. The hidden entry $\cot^2 z$ grows
    without bound towards the tip $z \to 0$ and vanishes at the patch end $z = \pi/2$,
    where the determinant vanishes too: there the coordinate $x_0$ stops being a good
    coordinate.
    """),
    code(r'''
    z_line = np.linspace(0.02, np.pi / 2, 600)
    entries = diagonal_values(z_line, 0.5)  # at b4 = e^(2/3), the history at a4 = 0.5
    fig, ax = plt.subplots()
    ax.plot(z_line, entries[0], color=AQUA, lw=1.8, label="$g_{00} = \\cot^2 z$")
    ax.plot(z_line, entries[1], color=RED, lw=1.8,
            label="$g_{11} = g_{22} = g_{33} = e^{2a_4}\\sin^{1/3}z$")
    ax.plot(z_line, entries[4], color=VIOLET, lw=1.8, ls="-.", label="$g_{44} = -1$")
    ax.plot(z_line, entries[5], color=BLUE, lw=1.8, ls="--",
            label="$g_{55} = g_{66} = g_{77} = -b_4 e^{-2a_4}\\sin^{1/3}z$")
    ax.plot(z_line, np.cos(z_line) ** 2, color="black", lw=1.2, ls=":",
            label="$\\det g / b_4^3 = \\cos^2 z$")
    ax.axhline(0.0, color="black", lw=0.8)
    ax.axvline(np.pi / 2, color="grey", lw=0.8, ls=":")
    ax.text(np.pi / 2 - 0.02, 3.3, "patch end", ha="right", fontsize=9)
    ax.text(0.05, 3.3, "towards the tip", fontsize=9)
    ax.set_ylim(-3.4, 3.6)  # room below the curves for the legend
    ax.set_xlabel("$z = 6 H x_0$ (radians)")
    ax.set_ylabel("entry of the metric (no unit)")
    ax.set_title("The diagonal entries across the patch ($a_4 = 0.5$, $b_4 = e^{2/3}$)")
    ax.legend(fontsize=8, loc="lower center", ncol=2)
    save_figure(fig, "diagonal_entries",
                "The diagonal entries of the author's metric as functions of "
                "$z = 6Hx_0$ from the tip side to the patch end $z = \\pi/2$, for "
                "$a_4 = 0.5$ and $b_4 = e^{2/3}$ (the deflating history at $a_4 = 0.5$); "
                "horizontal axis $z$ in radians, vertical axis the value of "
                "the entry (pure numbers). The three 3-space entries (solid red) stay "
                "positive and the three extra-time entries (dashed blue) and the time "
                "entry (dash-dotted) stay negative everywhere, so the signature is (4,4) "
                "at every point; the hidden entry $\\cot^2 z$ (aqua) grows without bound "
                "towards the tip and reaches $0$ at the patch end, where the determinant, "
                "drawn as $\\det g/b_4^3 = \\cos^2 z$ (dotted), also vanishes.")
    check(np.all(entries[0] > 0) and np.cos(np.pi / 2) ** 2 < 1e-30,
          "g00 > 0 inside the patch and det g = 0 at the patch end")
    '''),
    md(r"""
    ## 8. The vielbein: the scale factor of each direction

    Write each diagonal entry as a sign times a square: $g_{\mu\mu} = \eta_{\mu\mu}
    h_\mu^2$ with a positive **scale factor** $h_\mu$. On the patch all the factors below
    are positive (and $\cot z > 0$), so

    $$h = \bigl(\cot z,\ e^{a_4}\sin^{1/6}z,\ e^{a_4}\sin^{1/6}z,\ e^{a_4}\sin^{1/6}z,\
    1,\ b_4^{1/2}e^{-a_4}\sin^{1/6}z,\ b_4^{1/2}e^{-a_4}\sin^{1/6}z,\
    b_4^{1/2}e^{-a_4}\sin^{1/6}z\bigr).$$

    The diagonal matrix of these numbers is the **vielbein** $e^a{}_\mu$ used for the
    spinors later in the book. The next cell checks $\eta_{\mu\mu} h_\mu^2 = g_{\mu\mu}$
    for all eight directions; the lead's independent check of the Revision record did
    the same.
    """),
    code(r'''
    sixth = sp.sin(6 * H * x0) ** sp.Rational(1, 6)  # sin(z)^(1/6)
    # the author's order x0, x1, ..., x7
    h = [sp.cot(6 * H * x0)] + [sp.exp(a4) * sixth] * 3 + [sp.Integer(1)] \
        + [sp.sqrt(b4) * sp.exp(-a4) * sixth] * 3
    for k in range(8):
        say(f"  h[x{k}] = {plain(h[k])}")
    LEAD_EMT = "Revision/lead_checks/reports/emt-divergence-and-spin-connection.json"
    record_check(LEAD_EMT, "vielbein_reproduces_metric")  # stops if not passed
    check(all(sp.simplify(int(ETA[k]) * h[k] ** 2 - g[k, k]) == 0 for k in range(8)),
          "eta times h squared reproduces every diagonal entry of the metric",
          record=f"{LEAD_EMT}, check vielbein_reproduces_metric")
    '''),
    md(r"""
    ## 9. The expansion rate of each direction

    The proper length of a coordinate interval $\Delta x_\mu$ is $h_\mu \Delta x_\mu$.
    Its relative growth per unit time is $\partial_{x_4} \ln h_\mu$. For 3-space,
    $\ln h_1 = a_4 + \tfrac16 \ln \sin z$, and only $a_4$ depends on $x_4$, so the rate
    is $a_4'$; for an extra time $\ln h_5 = \tfrac12 \ln b_4 - a_4 + \tfrac16 \ln \sin z$
    and the rate is $-a_4' + b_4'/(2b_4)$; $h_0$ and $h_4$ do not depend on $x_4$, so their
    rates are $0$. The next cell lets sympy differentiate. It also checks that the six
    transverse scale factors multiply to $b_4^{3/2} \sin z$, without $a_4$: what 3-space
    gains, the extra times lose.
    """),
    code(r'''
    rates = [sp.simplify(sp.diff(sp.log(h[k]), x4)) for k in range(8)]
    for k in range(8):
        say(f"  expansion rate of x{k}: {plain(rates[k])}")
    a4_prime, b4_prime = sp.Derivative(a4, x4), sp.Derivative(b4, x4)
    expected = ([0] + [a4_prime] * 3 + [0]
                + [-a4_prime + b4_prime / (2 * b4)] * 3)  # the order x0, x1, ..., x7
    check([sp.simplify(r - e) == 0 for r, e in zip(rates, expected)] == [True] * 8,
          "3-space expands with rate a4p, the extra times shrink with rate "
          "-a4p + b4p/(2 b4)")
    transverse = sp.simplify(h[1] * h[2] * h[3] * h[5] * h[6] * h[7])
    say(f"product of the six transverse scale factors = {plain(transverse)}")
    check(sp.simplify(transverse - b4 ** sp.Rational(3, 2) * sp.sin(6 * H * x0)) == 0,
          "the six transverse scale factors multiply to b4^(3/2) sin z, without a4")
    '''),
    md(r"""
    ## 10. The deflating history of the Revision Kohn-Sham work

    The next cell reads the parameters of the Revision Kohn-Sham solver
    (`Revision/kohn_sham/results/parameters.json`): the constant $H$, the slope $A$ of
    the history $a_4 = A H x_4$, the exponent $\beta$ of the second metric function
    $b_4 = b_4(0)\,e^{\beta A H x_4}$, the five values of $a_4$ (the **slices**) at which
    that solver computes its states, and the tip cut-off $L$ (used in section 13 of this
    notebook). It also reads the theory record of that work
    (`Revision/kohn_sham/ks-theory.json`) and prints the first and the last sentence of
    its statement about the **status of the history** (key `historyStatus`). The
    sentence in between, not printed, says why: with the author's Lovelock weights the
    field equations of $a_4$ and $b_4$ allow this history only with a constant source
    of negative energy density, and the Kohn-Sham states computed along it do not supply
    it. So the history is assumed, not derived; this notebook uses it only to draw the
    time dependence of the metric. The exponent $\beta = 4/3$ is the one value that the
    author's weights allow on $a_4 = H x_4$ for a source without an $x_4$-$x_0$
    component, apart from the excluded constant $b_4$ (`Revision/SPEC.md`, section 1).
    """),
    code(r'''
    PARAMETERS = "Revision/kohn_sham/results/parameters.json"
    parameters = json.loads(repository_file(PARAMETERS).read_text(encoding="utf-8"))
    physics = parameters["physics"]
    H_value, A_value = physics["H"], physics["historyA"]
    beta = physics["historyBeta"]  # b4 = b4(0) e^(beta A H x4)
    slices = physics["slicesA4"]  # the values of a4 at which the solver works
    L_tip = physics["L_tipCutoff"]  # the tip cut-off, in units of 1/H
    say(f"H = {H_value}, A = {A_value}, beta = {beta:.6f}, slices a4 = {slices}, "
        f"tip cut-off L = {L_tip}")
    check(H_value == 1.0 and A_value == 1.0 and abs(beta - 4.0 / 3.0) < 1e-15
          and slices == [0.0, 0.5, 1.0, 1.5, 2.0],
          "the history of the record is a4 = x4, b4 = b4(0) e^(4 x4/3) (A = 1, H = 1, "
          "beta = 4/3) with slices 0 to 2")
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
    factor of 3-space is proportional to $e^{a_4}$ and that of the extra times to
    $e^{-a_4}b_4^{1/2} = b_4(0)^{1/2}\,e^{-(1 - \beta/2)a_4} = b_4(0)^{1/2}\,e^{-a_4/3}$:
    the extra times deflate exponentially, at one third of the rate at which 3-space
    inflates, and the product of the two factors grows like $e^{(\beta/2)a_4} =
    e^{2a_4/3}$. The next cell draws both, and their product, against $x_4$ twice: on an
    ordinary vertical axis (left) and on a logarithmic one (right), on which an
    exponential is a straight line whose slope is its rate ($+AH$ and $-AH/3$). The dots
    mark the five slices.
    """),
    code(r'''
    x4_line = np.linspace(0.0, 2.5, 251)
    a4_line = A_value * H_value * x4_line  # the history a4 = A H x4
    slice_x4 = np.array(slices) / (A_value * H_value)  # the times of the slices
    rate_t = 1.0 - beta / 2.0  # the extra times scale like e^(-(1 - beta/2) a4)
    fig, axes = plt.subplots(1, 2, figsize=(10.0, 4.2))
    for ax, scale in zip(axes, ["linear", "log"]):
        ax.plot(x4_line, np.exp(a4_line), color=RED, lw=1.8,
                label="3-space: $e^{a_4}$ (inflates)")
        ax.plot(x4_line, np.exp(-rate_t * a4_line), color=BLUE, lw=1.8, ls="--",
                label="extra times: $e^{-a_4}(b_4/b_4(0))^{1/2} = e^{-a_4/3}$ (deflate)")
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
                "$H = 1$, $\\beta = 4/3$ of the Revision Kohn-Sham work: "
                "3-space $e^{a_4}$ (solid red), the three extra times "
                "$e^{-a_4}(b_4/b_4(0))^{1/2} = e^{-a_4/3}$ (dashed blue) and their "
                "product $e^{2a_4/3}$ (dotted black), on an ordinary (left) and a "
                "logarithmic (right) vertical axis; horizontal axis the time $x_4$ in "
                "units of $1/H$, vertical axis the factor by which lengths have grown "
                "since $x_4 = 0$ (a pure number). Dots and squares mark the five slices "
                "$a_4 = 0, 0.5, 1, 1.5, 2$. 3-space grows by $e^2 = 7.39$ and the extra "
                "times shrink to $e^{-2/3} = 0.513$; on the logarithmic axis both are "
                "straight lines with slopes $+1$ and $-1/3$, the product grows by "
                "$e^{4/3} = 3.79$.")
    report("3-space growth factor at the last slice a4 = 2", f"{np.exp(2.0):.6f}")
    report("extra-time shrink factor at the last slice a4 = 2", f"{np.exp(-2.0 / 3.0):.6f}")
    product_last = np.exp(slices[-1]) * np.exp(-rate_t * slices[-1])
    check(abs(product_last - np.exp(2.0 * slices[-1] / 3.0)) < 1e-14 and rate_t > 0,
          "the extra times deflate (rate 1/3 of a4') and the product grows like e^(2 a4/3)")
    '''),
    md(r"""
    ## 11. The hidden direction: the functions of $z$

    The scale factors also depend on the hidden direction through $z$. The six
    transverse directions share the warp factor $W = \sin^{1/6} z$ (their metric
    entries share its square $W^2 = \sin^{1/3} z$), and the hidden direction itself
    has the scale factor $\cot z$ (its metric entry is $\cot^2 z$). The next cell draws
    these four functions across the patch: the first two on an ordinary axis (they lie
    between 0 and 1 and reach 1 at the patch end), the last two on a logarithmic axis
    (they grow without bound at the tip and vanish at the patch end).
    """),
    code(r'''
    z_line = np.linspace(0.005, np.pi / 2 - 0.005, 600)
    fig, axes = plt.subplots(1, 2, figsize=(10.0, 4.2))
    axes[0].plot(z_line, np.sin(z_line) ** (1 / 6), color=RED, lw=1.8,
                 label="warp factor $W = \\sin^{1/6} z$")
    axes[0].plot(z_line, np.sin(z_line) ** (1 / 3), color=ORANGE, lw=1.8, ls="--",
                 label="$W^2 = \\sin^{1/3} z$ (in the entries of $g$)")
    axes[0].set_ylim(0.0, 1.05)
    axes[0].set_title("The warp of the six transverse directions")
    axes[1].plot(z_line, 1 / np.tan(z_line), color=AQUA, lw=1.8,
                 label="$\\cot z$ (scale factor of $x_0$)")
    axes[1].plot(z_line, 1 / np.tan(z_line) ** 2, color=VIOLET, lw=1.8, ls="--",
                 label="$\\cot^2 z$ (entry $g_{00}$)")
    axes[1].set_yscale("log")
    axes[1].set_title("The hidden direction (logarithmic axis)")
    for ax in axes:
        ax.set_xlabel("$z = 6 H x_0$ (radians)")
        ax.set_ylabel("value (no unit)")
        ax.legend(fontsize=8)
    save_figure(fig, "hidden_direction",
                "The functions of the hidden coordinate $z = 6Hx_0$ in the author's "
                "metric, across the patch $0 < z < \\pi/2$; horizontal axes $z$ in "
                "radians, vertical axes pure numbers. Left: the warp factor "
                "$W = \\sin^{1/6} z$ shared by the six transverse scale factors (solid) "
                "and its square $W^2 = \\sin^{1/3} z$, which stands in the six "
                "transverse metric entries (dashed), rise from $0$ at the tip to $1$ at "
                "the patch end. Right, on a logarithmic axis: the scale factor "
                "$\\cot z$ of the hidden direction (solid) and its square "
                "$g_{00} = \\cot^2 z$ (dashed) "
                "grow without bound towards the tip and fall to $0$ at the patch end.")
    check(abs(np.sin(np.pi / 2) ** (1 / 6) - 1.0) < 1e-15,
          "the warp factor equals 1 at the patch end z = pi/2")
    '''),
    md(r"""
    The next cell shows how the two effects combine. It draws, over the plane of the
    time $x_4$ (along the history $a_4 = x_4$, $b_4 = b_4(0)\,e^{4x_4/3}$, unit $b_4(0)$)
    and the hidden coordinate $z$, the logarithm to base 10 of the scale factor of
    3-space, $\log_{10}(e^{a_4}\sin^{1/6}z)$ (left), and of an extra time,
    $\log_{10}(e^{-a_4}b_4^{1/2}\sin^{1/6}z) = \log_{10}(e^{-a_4/3}\sin^{1/6}z)$ (right).
    The value $0$ (grey) means the factor $1$; red means larger, blue smaller.
    """),
    code(r'''
    x4_grid, z_grid2 = np.meshgrid(np.linspace(0.0, 2.5, 251),
                                   np.linspace(0.01, np.pi / 2, 200))
    a4_grid = A_value * H_value * x4_grid
    space_map = np.log10(np.exp(a4_grid) * np.sin(z_grid2) ** (1 / 6))
    extra_map = np.log10(np.exp(-rate_t * a4_grid) * np.sin(z_grid2) ** (1 / 6))
    fig, axes = plt.subplots(1, 2, figsize=(10.0, 4.2), sharey=True)
    for ax, data, title in zip(axes, [space_map, extra_map],
                               ["3-space: $e^{a_4}\\sin^{1/6}z$",
                                "extra time: $e^{-a_4}b_4^{1/2}\\sin^{1/6}z$"]):
        mesh = ax.pcolormesh(x4_grid, z_grid2, data, cmap=DIVERGING, vmin=-1.3,
                             vmax=1.3, shading="auto")
        ax.contour(x4_grid, z_grid2, data, levels=[0.0], colors="black",
                   linewidths=1.0)
        ax.set_title(title)
        ax.set_xlabel("time $x_4$ (unit $1/H$)")
        ax.grid(False)
    axes[0].set_ylabel("$z = 6 H x_0$ (radians)")
    fig.colorbar(mesh, ax=axes, label="$\\log_{10}$ of the scale factor")
    save_figure(fig, "scale_factor_maps",
                "Maps of the logarithm to base 10 of the scale factor of 3-space "
                "$e^{a_4}\\sin^{1/6}z$ (left) and of an extra time "
                "$e^{-a_4}b_4^{1/2}\\sin^{1/6}z = e^{-a_4/3}\\sin^{1/6}z$ (right, unit "
                "$b_4(0)$) along the deflating history $a_4 = x_4$, "
                "$b_4 = b_4(0)\\,e^{4x_4/3}$; "
                "horizontal axes the time $x_4$ in units of $1/H$, vertical axes "
                "$z = 6Hx_0$ in radians, colour the value (red above $0$: lengths larger "
                "than the coordinate interval, blue below $0$: smaller, grey and the "
                "black line: factor $1$). As time goes on, 3-space grows everywhere "
                "(left, red spreads), the extra times shrink everywhere (right, blue "
                "deepens), and near the tip $z \\to 0$ both factors are small.")
    check(np.all(np.diff(space_map, axis=1) > 0) and np.all(np.diff(extra_map, axis=1) < 0),
          "along the history 3-space grows and the extra times shrink at every z")
    '''),
    md(r"""
    ## 12. Proper volumes: 3-space inflates, the extra times deflate, the 7-volume grows

    Take a box with coordinate edges $\Delta x_1 = \Delta x_2 = \Delta x_3 = 1$. Its
    proper 3-volume is the product of the three scale factors,
    $V_3 = (e^{a_4}\sin^{1/6}z)^3 = e^{3a_4}\sin^{1/2}z$. The same box in the three extra
    times has the proper 3-volume $V_t = b_4^{3/2} e^{-3a_4}\sin^{1/2}z$, and
    $V_3 V_t = b_4^{3/2} \sin z$. The slice $x_4 = \mathrm{const}$ is 7-dimensional
    ($x_0, x_1, x_2, x_3, x_5, x_6, x_7$); its volume factor is the product of the seven
    scale factors other than $h_4 = 1$, which is $b_4^{3/2} \sin z \cot z =
    b_4^{3/2} \cos z$: the factors $e^{\pm 3a_4}$ cancel, so it changes with $x_4$ only
    through $b_4$. The next cell computes these products and, by an integral over the
    whole patch $0 < x_0 < \pi/(12H)$, the proper 7-volume of the patch per unit
    coordinate volume of the six transverse directions:
    $\int_0^{\pi/(12H)} b_4^{3/2}\cos(6Hx_0)\, dx_0
    = b_4^{3/2}\bigl[\sin(6Hx_0)/(6H)\bigr]_0^{\pi/(12H)} = b_4^{3/2}/(6H)$.
    """),
    code(r'''
    V3 = sp.simplify(h[1] * h[2] * h[3])  # proper 3-volume of a unit coordinate box
    Vt = sp.simplify(h[5] * h[6] * h[7])  # the same in the three extra times
    # the 7-volume: every scale factor except h[4] = 1 of the time x4
    V7 = sp.simplify(h[0] * h[1] * h[2] * h[3] * h[5] * h[6] * h[7])
    say(f"V3 = {plain(V3)},  Vt = {plain(Vt)},  V7 density = {plain(V7)}")
    check(sp.simplify(V7 - b4 ** sp.Rational(3, 2) * sp.cos(6 * H * x0)) == 0
          and sp.simplify(sp.diff(V7 / b4 ** sp.Rational(3, 2), x4)) == 0,
          "the 7-volume density is b4^(3/2) cos z and changes with x4 only through b4")
    patch_volume = sp.integrate(b4 ** sp.Rational(3, 2) * sp.cos(6 * H * x0),
                                (x0, 0, sp.pi / (12 * H)))
    say(f"proper 7-volume of the patch per unit transverse coordinate volume = "
        f"{patch_volume}")
    check(sp.simplify(patch_volume - b4 ** sp.Rational(3, 2) / (6 * H)) == 0,
          "the whole patch has the proper 7-volume b4^(3/2)/(6H) per unit coordinate "
          "volume")
    '''),
    md(r"""
    The next cell draws these volumes along the history at the fixed point
    $z = \pi/3$ (where $\sin z = 0.866$ and $\cos z = 0.5$), in the unit $b_4(0)^{3/2}$,
    on a logarithmic axis. On the history $b_4^{3/2} = b_4(0)^{3/2}\,e^{(3\beta/2)a_4}
    = b_4(0)^{3/2}\,e^{2a_4}$, so $V_3$ grows like $e^{3x_4}$, $V_t$ shrinks like
    $e^{-3x_4}e^{2x_4} = e^{-x_4}$, and their product $b_4^{3/2}\sin z$ and the 7-volume
    density $b_4^{3/2}\cos z$ both grow like $e^{2x_4}$: the inflation of 3-space is
    compensated by the factor $e^{-3a_4}$ of the extra times, but not the growth of
    $b_4$.
    """),
    code(r'''
    z_fixed = np.pi / 3
    b4_line = np.exp(beta * a4_line)  # b4 on the history, unit b4(0)
    v3 = np.exp(3 * a4_line) * np.sin(z_fixed) ** 0.5
    vt = b4_line ** 1.5 * np.exp(-3 * a4_line) * np.sin(z_fixed) ** 0.5
    fig, ax = plt.subplots()
    ax.plot(x4_line, v3, color=RED, lw=1.8, label="$V_3 = e^{3a_4}\\sin^{1/2}z$")
    ax.plot(x4_line, vt, color=BLUE, lw=1.8, ls="--",
            label="$V_t = b_4^{3/2}e^{-3a_4}\\sin^{1/2}z$")
    ax.plot(x4_line, v3 * vt, color=ORANGE, lw=1.8, ls="-.",
            label="$V_3 V_t = b_4^{3/2}\\sin z$")
    ax.plot(x4_line, b4_line ** 1.5 * np.cos(z_fixed), color="black", lw=1.2,
            ls=":", label="7-volume density $b_4^{3/2}\\cos z$")
    ax.set_yscale("log")
    ax.set_xlabel("time $x_4$ (unit $1/H$), history $a_4 = x_4$, "
                  "$b_4 = b_4(0)e^{4x_4/3}$")
    ax.set_ylabel("proper volume per unit coordinate volume")
    ax.set_title("Proper volumes at $z = \\pi/3$ (unit $b_4(0)^{3/2}$)")
    ax.legend(fontsize=8)
    save_figure(fig, "proper_volumes",
                "Proper volumes per unit coordinate volume at the fixed hidden position "
                "$z = \\pi/3$ along the history $a_4 = x_4$, $b_4 = b_4(0)\\,e^{4x_4/3}$ "
                "(unit $b_4(0)^{3/2}$), on a logarithmic vertical "
                "axis; horizontal axis the time $x_4$ in units of $1/H$. The proper "
                "3-volume of 3-space $V_3$ (solid red) grows like $e^{3x_4}$, the proper "
                "3-volume of the three extra times $V_t$ (dashed blue) shrinks like "
                "$e^{-x_4}$, and both their product $b_4^{3/2}\\sin z$ (dash-dotted, "
                "$0.866$ at $x_4 = 0$) and the density $b_4^{3/2}\\cos z$ of the proper "
                "7-volume (dotted, $0.5$ at $x_4 = 0$) grow like $e^{2x_4}$: the "
                "factors $e^{\\pm 3a_4}$ compensate, the growth of $b_4$ does not.")
    check(np.max(np.abs(v3 * vt / (np.exp(2.0 * a4_line) * np.sin(z_fixed)) - 1.0)) < 1e-12,
          "V3 times Vt equals b4^(3/2) sin z = e^(2 a4) sin z along the history "
          "(unit b4(0)^(3/2))")
    '''),
    md(r"""
    ## 13. The hidden coordinate $y$ and the warped form of the metric

    The entry $\cot^2 z$ makes the hidden direction awkward. The Revision Kohn-Sham work
    uses the coordinate $y = \ln(\sin z)/(6H)$, which measures proper distance along
    $x_0$. Line by line: the chain rule gives
    $dy/dx_0 = \frac{1}{6H}\,\frac{\cos z}{\sin z}\, 6H = \cot z$, so
    $dy^2 = \cot^2 z\, dx_0^2 = g_{00}\, dx_0^2$. Next, $6Hy = \ln \sin z$ gives
    $\sin z = e^{6Hy}$ ($e$ to the power of both sides), so the warp factor is
    $W = \sin^{1/6} z = e^{Hy}$ and its square is $W^2 = \sin^{1/3} z = e^{2Hy}$. Hence
    the **warped form**

    $$ds^2 = dy^2 - dx_4^2 + W^2\bigl[e^{2a_4}(dx_1^2 + dx_2^2 + dx_3^2)
    - b_4 e^{-2a_4}(dx_5^2 + dx_6^2 + dx_7^2)\bigr], \qquad W = e^{Hy}.$$

    As $z$ runs from $0$ to $\pi/2$, $y$ runs from $-\infty$ (the tip) to $0$ (the patch
    end). In the coordinates $(y, x_1, \dots, x_7)$ the scale factor of the hidden
    direction is $1$, so the volume factor is the product of the six transverse scale
    factors, $b_4^{3/2} W^6 = b_4^{3/2} e^{6Hy} = b_4^{3/2} \sin z$. The Kohn-Sham record
    writes its volume factor in exactly this form, $b_4^{3/2} e^{6Hy}$.

    The next cell prints four statements of the record
    `Revision/kohn_sham/ks-theory.json` (read in section 10): the definition of $y$, the
    line element, the warp factor and the volume factor. Then it checks them with sympy;
    the checks of the warp factor and of the volume factor also require that the record
    still writes them as `W(y) = e^{Hy}` and as a text that starts with
    `b4^{3/2} e^{6Hy} (= b4^{3/2} cos z`, and the line element of the record must carry
    $b_4$ in its extra-time part.
    To write the metric in the coordinate $y$ it uses the inverse relation
    $x_0 = \arcsin(e^{6Hy})/(6H)$: the hidden entry becomes $g_{00}\,(dx_0/dy)^2$
    (because $dx_0 = (dx_0/dy)\,dy$), and the seven entries $g_{11}, \dots, g_{77}$ only
    need $\sin z = e^{6Hy}$ put in. The cell checks the warped form for every $b_4$.
    """),
    code(r'''
    geometry = ks_theory["geometry"]  # the statements of the record about the geometry
    for key in ("hiddenCoordinate", "lineElement", "warp", "sqrtDetG"):
        say(f"record, {key}: {geometry[key]}")
    y_of_x0 = sp.log(sp.sin(6 * H * x0)) / (6 * H)  # y = ln(sin z)/(6H)
    dy_dx0 = sp.diff(y_of_x0, x0)  # the chain rule, done by sympy
    say(f"dy/dx0 = {plain(dy_dx0)}")
    record_check(LEAD_EMT, "ks_coordinate_jacobian")  # stops if not passed
    check(sp.simplify(dy_dx0 - sp.cot(6 * H * x0)) == 0,
          "dy/dx0 = cot z",
          record=f"{LEAD_EMT}, check ks_coordinate_jacobian")
    check(sp.simplify(dy_dx0 ** 2 - g[0, 0]) == 0,
          "dy^2 = g00 dx0^2: y measures proper distance along x0")
    check(sp.simplify(sp.exp(H * y_of_x0) - sixth) == 0,
          "the warp factor W = sin(z)^(1/6) equals e^(H y)")
    y = sp.symbols("y", real=True)  # the hidden coordinate as a symbol of its own
    x0_of_y = sp.asin(sp.exp(6 * H * y)) / (6 * H)  # the inverse: sin z = e^(6 H y)
    dx0_dy = sp.diff(x0_of_y, y)  # dx0/dy
    # the metric in y, x1, ..., x7: the hidden entry first, as in the author's order
    g_y = sp.diag(g[0, 0].subs(x0, x0_of_y) * dx0_dy ** 2,
                  *[g[k, k].subs(x0, x0_of_y) for k in range(1, 8)])
    W = sp.exp(H * y)  # the warp factor in the coordinate y
    warped = sp.diag(*([1] + [W ** 2 * sp.exp(2 * a4)] * 3 + [-1]
                       + [-W ** 2 * b4 * sp.exp(-2 * a4)] * 3))  # the warped form
    for k in (0, 1, 4, 5):
        say(f"  in the coordinate y: g[{k}, {k}] = {plain(g_y[k, k])}")
    check((g_y - warped).applyfunc(sp.simplify) == sp.zeros(8, 8)
          and geometry["warp"] == "W(y) = e^{Hy}"
          and "b4(x4) (dx5^2+dx6^2+dx7^2)" in geometry["lineElement"],
          "in the coordinate y the metric is the warped form with W = e^(H y), with b4 in "
          "the extra-time part as in the record",
          record="Revision/kohn_sham/ks-theory.json, geometry.lineElement and "
                 "geometry.warp")
    check(sp.simplify(g_y.det() - b4 ** 3 * sp.exp(12 * H * y)) == 0
          and geometry["sqrtDetG"].startswith("b4^{3/2} e^{6Hy} (= b4^{3/2} cos z"),
          "in the coordinate y, sqrt|det g| is b4^(3/2) e^(6 H y) = b4^(3/2) sin z, as the "
          "record states",
          record="Revision/kohn_sham/ks-theory.json, geometry.sqrtDetG")
    distance_to_end = -y_of_x0  # proper distance from the point to the patch end
    check(sp.limit(distance_to_end, x0, 0, "+") == sp.oo,
          "the tip z -> 0 lies at an infinite proper distance (y -> minus infinity)")
    '''),
    md(r"""
    The Revision Kohn-Sham solver keeps only the part $-L \le y \le 0$ of the hidden
    direction, with the tip cut-off $L = 3/H$ read in section 10. How much of the
    7-volume does the cut-off remove? In $y$ the 7-volume density is $b_4^{3/2} e^{6Hy}$,
    and the constant factor $b_4^{3/2}$ cancels in a fraction, so the
    fraction of the 7-volume beyond the cut-off is
    $\int_{-\infty}^{-L} e^{6Hy} dy \big/ \int_{-\infty}^{0} e^{6Hy} dy = e^{-6HL}$,
    which is $e^{-18} \approx 1.5 \times 10^{-8}$ for $L = 3/H$. The cut-off lies at the
    tiny angle $z = \arcsin e^{-18} \approx 1.5 \times 10^{-8}$. The next cell computes
    the fraction with sympy and draws $y$ as a function of $z$ (left; the $z$ axis is
    logarithmic, so that the region near the tip is visible: there
    $y \approx \ln(z)/(6H)$ is a straight line) and the warp factor $W = e^{Hy}$, its
    square $W^2 = e^{2Hy}$ and the volume density $W^6 = e^{6Hy}$ (in the unit
    $b_4^{3/2}$, which does not depend on $y$) as functions of $y$ (right).
    """),
    code(r'''
    L_exact = sp.nsimplify(L_tip)  # the number 3.0 of the record as the exact integer 3
    fraction = sp.integrate(sp.exp(6 * H * y), (y, -sp.oo, -L_exact / H)) \
        / sp.integrate(sp.exp(6 * H * y), (y, -sp.oo, 0))  # y: the symbol made above
    fraction = sp.simplify(fraction.subs(H, 1))
    report("fraction of the 7-volume beyond the tip cut-off y = -3", sp.sstr(fraction),
           f"= {float(fraction):.4e}")
    z_cut = float(sp.asin(sp.exp(-18)))  # the angle z of the cut-off, sin z = e^(-18)
    report("angle z of the tip cut-off", f"{z_cut:.4e}", "radians")
    z_line = np.logspace(-10, np.log10(np.pi / 2), 800)  # 1e-10 ... pi/2, evenly in log
    y_line = np.log(np.sin(z_line)) / 6.0  # with H = 1
    fig, axes = plt.subplots(1, 2, figsize=(10.0, 4.2))
    axes[0].plot(z_line, y_line, color=VIOLET, lw=1.8, label="$y(z)$")
    axes[0].axhline(-L_tip, color="black", lw=1.0, ls="--",
                    label=f"tip cut-off $y = -L = -{L_tip:g}$")
    axes[0].plot([z_cut], [-L_tip], "o", color="black", ms=6)
    axes[0].set_xscale("log")
    axes[0].set_xlabel("$z = 6 H x_0$ (radians, logarithmic axis)")
    axes[0].set_ylabel("$y = \\ln(\\sin z)/(6H)$ (unit $1/H$)")
    axes[0].set_title("The hidden coordinate $y$")
    axes[0].legend(fontsize=8)
    y_axis = np.linspace(-4.0, 0.0, 400)
    axes[1].plot(y_axis, np.exp(y_axis), color=RED, lw=1.8,
                 label="warp factor $W = e^{Hy} = \\sin^{1/6} z$")
    axes[1].plot(y_axis, np.exp(2 * y_axis), color=ORANGE, lw=1.8, ls="-.",
                 label="$W^2 = e^{2Hy} = \\sin^{1/3} z$")
    axes[1].plot(y_axis, np.exp(6 * y_axis), color=AQUA, lw=1.8, ls="--",
                 label="7-volume density per $b_4^{3/2}$: $W^6 = e^{6Hy} = \\sin z$")
    axes[1].axvspan(-4.0, -L_tip, color="grey", alpha=0.25,
                    label="removed by the tip cut-off")
    axes[1].set_xlabel("$y$ (unit $1/H$)")
    axes[1].set_ylabel("value (no unit)")
    axes[1].set_title("Warp and volume density in $y$")
    axes[1].legend(fontsize=8, loc="upper left")
    save_figure(fig, "hidden_coordinate_y",
                "The hidden coordinate $y = \\ln(\\sin z)/(6H)$ with $H = 1$. Left: $y$ "
                "versus $z = 6Hx_0$ in radians on a logarithmic axis from $10^{-10}$ to "
                "$\\pi/2$; $y$ is $0$ at the patch end $z = \\pi/2$ and falls without "
                "bound towards the tip $z \\to 0$, along the straight line "
                "$y \\approx \\ln(z)/6$; the dashed line and the dot mark the tip cut-off "
                "$y = -3$ of the Revision Kohn-Sham solver, at $z = 1.5 \\times "
                "10^{-8}$. Right: the warp factor $W = e^{Hy}$ (solid), its square "
                "$W^2 = e^{2Hy}$ (dash-dotted) and the density $W^6 = e^{6Hy}$ of the "
                "proper 7-volume in the unit $b_4^{3/2}$ (dashed) versus $y$ in units of "
                "$1/H$; the grey band beyond "
                "the cut-off holds only the fraction $e^{-18} = 1.5 \\times 10^{-8}$ of "
                "the 7-volume of the patch.")
    check(fraction == sp.exp(-18), "the cut-off removes exactly the fraction e^(-18)")
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

    - The metric was read **exactly as the author typed it**, and the text agrees with
      the formula and with the Revision record of the Rust program `lovelock_gkd`
      (all 8 diagonal entries; the 56 other entries are zero).
    - $\det g = b_4^3 \cos^2 z$ and $\sqrt{|\det g|} = b_4^{3/2} \cos z$, without $a_4$:
      PROVED here by exact algebra (and in the Revision record).
    - The signature is (4,4) at every point of the patch: $x_0, x_1, x_2, x_3$ are
      space-like, $x_4, x_5, x_6, x_7$ time-like.
    - The diagonal vielbein $h = (\cot z, e^{a_4}\sin^{1/6}z\ (\times 3), 1,
      b_4^{1/2} e^{-a_4}\sin^{1/6}z\ (\times 3))$ reproduces the metric.
    - 3-space expands with the rate $a_4'$ and the three extra times **deflate** with the
      rate $-a_4' + b_4'/(2b_4)$; along the prescribed history $a_4 = x_4$,
      $b_4 = b_4(0)\,e^{4x_4/3}$ ($A = 1$, $H = 1$, $\beta = 4/3$) 3-space
      lengths grow by $e^2 = 7.39$ and extra-time durations shrink to $e^{-2/3} = 0.513$
      between the first and the last slice.
    - The proper 3-volume of 3-space grows like $e^{3a_4}$, that of the extra times
      shrinks like $b_4^{3/2} e^{-3a_4}$, and the 7-volume density $b_4^{3/2} \cos z$
      changes only through $b_4$ (on the history like $e^{2a_4}$); the whole patch has the
      7-volume $b_4^{3/2}/(6H)$ per unit transverse coordinate volume.
    - In the hidden coordinate $y = \ln(\sin z)/(6H)$ the metric has the warped form
      of the Revision record, with the warp factor $W = e^{Hy}$ and the volume factor
      $b_4^{3/2}W^6 = b_4^{3/2}e^{6Hy}$; the tip is at infinite proper distance, and the
      tip cut-off $y = -3/H$ of the Kohn-Sham solver removes only the fraction $e^{-18}$
      of the 7-volume.
    - ASSUMED: the history $a_4 = A H x_4$, $b_4 = b_4(0)\,e^{\beta A H x_4}$ is a
      prescribed background (the Revision record says so in its own words), used here
      only to draw the time dependence; the field equations of $a_4$ and $b_4$ come
      later.
    """),
]

if __name__ == "__main__":
    raise SystemExit(run_builder(__file__))
