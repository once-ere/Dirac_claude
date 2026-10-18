#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
"""Builder of Notebook 12a, "The field equations for a4 and b4 derived with sympy".

Textbook "Universes in Pairs", chapter 12 (the field equations for a4 and b4: Einstein and
Einstein-Lovelock).  The notebook Revision/textbook/notebooks/12a_a4_field_equations.ipynb
is BUILT from this file by Revision/textbook/tools/nbkit.py (never edit the .ipynb by
hand):

    python Revision/textbook/tools/nbkit.py build \
        Revision/textbook/notebooks/src/12a_a4_field_equations.py --date YYYY-MM-DD
    python Revision/textbook/tools/nbkit.py check \
        Revision/textbook/notebooks/src/12a_a4_field_equations.py

The notebook derives everything from the corrected metric of Revision/SPEC.md section 1
(version 2 of 2026-10-16, two functions a4(x4) and b4(x4), every real z = 6 H x0) and
compares every result with the Revision records of Revision/field_equations_a4,
Revision/metric_warped, Revision/gkd_lovelock, Revision/theory and Revision/lead_checks.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools"))
from nbkit import code, md, run_builder  # noqa: E402

FACTS = {
    "id": "12a",
    "name": "12a_a4_field_equations",
    "title": "The field equations for a4 and b4 derived with sympy",
    "purpose": (
        "It derives with sympy, from the corrected metric of the author with its two "
        "functions a4(x4) and b4(x4), for every real value of the hidden angle, the "
        "Christoffel symbols, the Riemann, Ricci and Einstein tensors and the three "
        "Lovelock tensors (with the generalized Kronecker delta), writes the "
        "Einstein-Lovelock field equations, reduces them to a constraint, two equations "
        "of second order and the conditions on the source, checks the Bianchi identity "
        "and the conservation law of a general source, specialises to Einstein gravity "
        "(a flat vacuum, no exponential vacuum, the null energy combinations) and to the "
        "exponential histories with the source of the record history, compares every "
        "result with the Revision records, and draws five teaching plots."
    ),
    "records": [
        ["Revision/field_equations_a4/a4-equations.json",
         "the field equations for a4 and b4 written by the Wolfram verifier; every "
         "equation of the notebook is compared with it"],
        ["Revision/gkd_lovelock/results/lovelock-tensors.json",
         "the three Lovelock tensors computed by the Rust program lovelock_gkd; all 64 "
         "components of each are compared"],
        ["Revision/field_equations_a4/reports/python-a4-report.json",
         "the sympy checks of the a4 and b4 record that the notebook reproduces"],
        ["Revision/field_equations_a4/reports/wolfram-a4-report.json",
         "the Wolfram checks of the a4 and b4 record that the notebook reproduces"],
        ["Revision/metric_warped/reports/python-warped-metric-report.json",
         "the checks of the corrected metric that the notebook reproduces"],
        ["Revision/metric_warped/results/warped-metric.json",
         "the Einstein tensor and the source of the record history, compared with the "
         "notebook"],
        ["Revision/theory/reports/wolfram-field-theory.json",
         "the field-theory checks of the Christoffel symbols, the volume factor and the "
         "Ricci tensor that the notebook reproduces"],
        ["Revision/lead_checks/reports/einstein-gauss-bonnet-a4.json",
         "the independent checks of the Einstein and Gauss-Bonnet tensors that the "
         "notebook reproduces"],
        ["Revision/lead_checks/reports/emt-divergence-and-spin-connection.json",
         "the independent check of the conservation law that the notebook reproduces"],
    ],
    "packages": ["numpy", "sympy", "matplotlib"],
    "needs_rust": [],
    "expected_seconds": 30,
    "timeout_seconds": 900,
    "files_written": [
        "Revision/textbook/figures/12a.captions.json",
        "Revision/textbook/figures/12a_1_pair_curvatures.png",
        "Revision/textbook/figures/12a_2_einstein_components.png",
        "Revision/textbook/figures/12a_3_lovelock_heat_maps.png",
        "Revision/textbook/figures/12a_4_jacobian_determinant.png",
        "Revision/textbook/figures/12a_5_exponential_vacuum.png",
    ],
    "final_lines": [
        "PASS all five figure files exist",
        "ALL 72 CHECKS PASSED (notebook 12a)",
    ],
    "troubleshooting": [
        ["The cell of section 10, which computes the three Lovelock tensors, runs for a "
         "minute or more",
         "it multiplies about three thousand products of curvature components in pure "
         "Python, which takes about ten seconds on a fast computer and can take a few "
         "minutes on a slow one. The cell is not stuck: wait until its output appears."],
        ["\"FileNotFoundError\" naming a file below the folder Revision",
         "the notebook reads the Revision records of the repository. Run it inside the "
         "folder Revision/textbook/notebooks of a complete copy of the repository made "
         "with git clone, not on a copy of the notebook file alone."],
    ],
}

CELLS = [
    md(r"""
    ## 1. What this notebook computes

    This notebook derives, step by step and with exact algebra (no rounding anywhere),
    the field equations of gravity for the two unknown functions $a_4(x_4)$ and
    $b_4(x_4)$ of the author's corrected metric. Starting from nothing but the metric,
    it

    - writes the corrected metric in the computer-algebra package sympy, for every real
      value of the hidden angle $z = 6Hx_0$, and checks its signature and determinant;
    - computes the Christoffel symbols, the Riemann curvature tensor, the Ricci tensor,
      the Ricci scalar and the Einstein tensor, and finds that the curvature has no
      mixed component at all;
    - computes the three Lovelock tensors $E_{(1)}, E_{(2)}, E_{(3)}$ with the
      generalized Kronecker delta (the first one is the Einstein tensor, the second one
      the Gauss-Bonnet tensor), and checks the second one against the classical
      Gauss-Bonnet formula;
    - writes the Einstein-Lovelock field equations and reduces them to a constraint,
      two equations of second order and the conditions every source must satisfy;
    - checks the Bianchi identity and the conservation law of a general source;
    - specialises to Einstein gravity: a flat vacuum exists, no exponential history is
      a vacuum, and the null energy combinations;
    - specialises to the exponential histories and to the source that the record
      history $a_4 = Hx_4$, $b_4 = e^{(4/3)Hx_4}$ needs;
    - compares every result with the Revision records and draws five teaching plots.
    """),
    md(r"""
    ## 3. The words used in this notebook

    - **Coordinates** $x_0, \dots, x_7$ (the author's names): $x_0$ is the **hidden**
      space-like direction; $x_1, x_2, x_3$ are ordinary 3-space; $x_4$ is the time;
      $x_5, x_6, x_7$ are the three **extra times** (time-like directions). In the code
      the positions 0 to 7 of a list stand for $x_0$ to $x_7$.
    - **Hidden angle** $z = 6Hx_0$: it takes every real value. The code writes the
      metric with $t = \tan z$ and $w = (\sin^2 z)^{1/12} > 0$, which are fine at every
      $z$ with $\sin z\cos z \ne 0$.
    - **Metric** $g_{\mu\nu}$: the table of numbers that turns small coordinate steps
      into squared lengths. Here it is **diagonal**: only $g_{00}, \dots, g_{77}$ are
      not zero.
    - **Scale factor**: the factor by which a length along a direction grows. 3-space
      has $e^{a_4}$; the hidden direction and the extra times share
      $e^{-a_4}b_4^{1/2}$ (times factors that depend on $z$ only).
    - **Deflating**: shrinking. On the record history the extra times and the hidden
      direction shrink like $e^{-a_4/3}$ while 3-space grows like $e^{a_4}$.
    - **Jet variables**: the symbols `ad1`, `ad2`, `ad3` stand for $a_4'$, $a_4''$,
      $a_4'''$ and `bd1`, `bd2`, `bd3` for $b_4'$, $b_4''$, $b_4'''$; `ea` is
      $e^{a_4}$ and `bb` is $b_4$. The record writes its results with $u = b_4'/b_4$,
      $v = u'$ and $k = e^{2a_4}/b_4$ (`uu`, `vv`, `kk` in the code).
    - **Christoffel symbol** $\Gamma^a{}_{bc}$: the combination of first derivatives
      of the metric that tells how the coordinate directions turn from point to point.
    - **Riemann tensor** $R^{ab}{}_{cd}$: the curvature. A component is **sectional**
      when $\{c, d\} = \{a, b\}$: the curvature of one plane. **Ricci tensor**
      $R^h{}_j = R^{ah}{}_{aj}$ (sum over $a$), **Ricci scalar** $R = R^h{}_h$,
      **Einstein tensor** $G^h{}_j = R^h{}_j - \tfrac12 \delta^h_j R$.
    - **Generalized Kronecker delta** (GKD) $\delta^{h_1 \dots h_n}_{j_1 \dots j_n}$:
      $+1$ when the lower list is an even rearrangement of the upper list, $-1$ when it
      is an odd rearrangement, $0$ otherwise (also when an index repeats).
    - **Lovelock tensor** $E_{(k)}$: a tensor built from $k$ factors of the Riemann
      tensor with the GKD; $E_{(1)}$ is the Einstein tensor, $E_{(2)}$ the
      Gauss-Bonnet tensor. In 8 dimensions only $k = 1, 2, 3$ exist.
    - **Source**, **energy-momentum tensor** $T^\mu{}_\nu$: the matter that bends the
      metric. Its parts: the energy density $\rho = -T^{x_4}{}_{x_4}$, the pressures
      $p_0$ (hidden direction), $p_3$ (3-space), $p_t$ (extra times), and the mixed
      components $q_{40} = T^{x_4}{}_{x_0}$, $q_{04} = T^{x_0}{}_{x_4}$.
    - **Couplings**: $\alpha_1, \alpha_2, \alpha_3$ (the weights of the three Lovelock
      tensors), $\Lambda$ (the cosmological constant), $\kappa$ (the strength of
      gravity). **Einstein gravity** is $\alpha_1 = 1$, $\alpha_2 = \alpha_3 = 0$. The
      **author's weights** are $\alpha_k = w_k/H^{2k}$ with $w = (1, 1/32, 1/1152)$ and
      $\Lambda = -10$ in the record's convention.
    - **Constraint**: an equation without second derivatives. **Jacobian** $J$: the
      2 by 2 table of the coefficients with which $a_4''$ and $v$ enter the two
      equations of second order.
    - **Bianchi identity**: the left-hand side of the field equations has zero
      divergence for every metric; **conservation**: the source must then have zero
      divergence too.
    - **Vacuum**: no source, $T = 0$. **Exponential history**: $a_4 = AHx_4 + a_0$,
      $b_4 = b_4(0)e^{\beta AHx_4}$; the **record history** is $A = 1$, $\beta = 4/3$,
      $b_4(0) = 1$.
    - **PASS line**: a printed line that says a check passed; "reproduces" names the
      Revision record (report file and check name) that found the same result.
    """),
    md(r"""
    ## 4. The physical and mathematical situation

    The author's corrected metric (the primordial gravitational field, version 2 of
    2026-10-16) is diagonal:

    $$g = \mathrm{diag}\big(e^{-2a_4}b_4\cot^2 z,\ e^{2a_4},\ e^{2a_4},\ e^{2a_4},\ -1,
    \ -e^{-2a_4}b_4 s,\ -e^{-2a_4}b_4 s,\ -e^{-2a_4}b_4 s\big),$$

    with $s = (\sin^2 z)^{1/6}$ (the positive root) and $z = 6Hx_0$ real, in the order
    $x_0, \dots, x_7$, two functions $a_4(x_4)$ and $b_4(x_4) > 0$ of the time and a
    constant $H > 0$. Its signs are $(+,+,+,+,-,-,-,-)$ wherever
    $\sin z\cos z \ne 0$: the signature (4,4).

    The field equations of Einstein-Lovelock gravity are

    $$\sum_{k=1}^{3} \alpha_k E_{(k)}{}^\mu{}_\nu + \Lambda \delta^\mu_\nu
    = \kappa T^\mu{}_\nu,\qquad E_{(k)}{}^h{}_j = -\frac{P_{(k)}{}^h{}_j}{2^{k+1}},$$

    $$P_{(k)}{}^h{}_j = \delta^{h h_1 \dots h_{2k}}_{j j_1 \dots j_{2k}}
    R^{j_1 j_2}{}_{h_1 h_2} \cdots R^{j_{2k-1} j_{2k}}{}_{h_{2k-1} h_{2k}}$$

    (a sum over every repeated index), with the source

    $$T^\mu{}_\nu = \mathrm{diag}(p_0, p_3, p_3, p_3, -\rho, p_t, p_t, p_t)
    + q_{40}\ (\mu = x_4, \nu = x_0) + q_{04}\ (\mu = x_0, \nu = x_4).$$

    Every statement this notebook checks is an exact algebraic identity (status
    PROVED): sympy computes with symbols, not with rounded numbers. The plots
    evaluate the exact formulas at chosen numbers, in units in which $H = 1$.
    """),
    md(r"""
    ## 5. The Revision records this notebook reproduces

    The Revision record contains two independent derivations of these equations (one
    in the Wolfram Language, one in sympy), the record of the corrected metric, the
    field-theory record and two independent checks by the lead. Each writes a report
    file: a list of checks with a name and a verdict. The next cell defines a helper
    that looks up a check by its name, and the helper `reproduces`: a check that
    passes only when this notebook's own result holds AND the record lists the named
    check with the verdict PASS. `reproduces` collects its two printed lines (PASS and
    reproduces) in a text buffer and prints them with one call, so that they always
    stay together in the output. Finally the cell prints, for each of the six reports,
    how many of its checks passed, and checks that every one did: a record with a
    failed check stops the notebook here. The numbers of checks are printed, not fixed
    in advance, because a record may gain checks when it is extended.
    """),
    code(r'''
    import contextlib  # redirect_stdout: send printed lines into a buffer
    import io  # StringIO: a text buffer in memory

    PY = "Revision/field_equations_a4/reports/python-a4-report.json"  # sympy record
    WL = "Revision/field_equations_a4/reports/wolfram-a4-report.json"  # Wolfram record
    WARPED = "Revision/metric_warped/reports/python-warped-metric-report.json"
    FIELD = "Revision/theory/reports/wolfram-field-theory.json"  # field theory
    LEAD = "Revision/lead_checks/reports/einstein-gauss-bonnet-a4.json"  # lead check
    EMT = "Revision/lead_checks/reports/emt-divergence-and-spin-connection.json"
    EQUATIONS = "Revision/field_equations_a4/a4-equations.json"  # the equations
    LOVELOCK = "Revision/gkd_lovelock/results/lovelock-tensors.json"  # Rust GKD output
    METRIC_RESULTS = "Revision/metric_warped/results/warped-metric.json"


    def read_json(relative):
        """Read a JSON file of the repository (a Revision record)."""
        return json.loads(repository_file(relative).read_text(encoding="utf-8"))


    def record_verdict(report_file, name):
        """The verdict ("PASS" or "FAIL") of the check name in a report, None if absent."""
        for entry in read_json(report_file)["checks"]:
            if entry["name"] == name:
                return entry["verdict"]
        return None


    def reproduces(condition, name, report_file, record_name):
        """A check that also requires the record check record_name to be PASS.  Its
        printed lines (PASS and reproduces) are collected in a text buffer and printed
        by one print call, so that they always stay together in the cell's output."""
        found = record_verdict(report_file, record_name) == "PASS"
        lines = io.StringIO()  # a text buffer
        with contextlib.redirect_stdout(lines):  # print() now writes into the buffer
            check(condition and found, name, record=f"{report_file}, check {record_name}")
        print(lines.getvalue(), end="")  # all lines at once


    for report_file in (PY, WL, WARPED, FIELD, LEAD, EMT):
        verdicts = [entry["verdict"] for entry in read_json(report_file)["checks"]]
        passed = verdicts.count("PASS")  # how many checks of the record passed
        say(f"{report_file}: {passed} of {len(verdicts)} checks PASS")
        check(len(verdicts) > 0 and passed == len(verdicts),
              f"every check of the record {Path(report_file).name} passed")
    '''),
    md(r"""
    ## 6. The corrected metric in sympy

    The next cell makes the symbols. $H$ is positive. The hidden angle enters through
    two symbols: `t` $= \tan z$ (real and not zero) and `w` $= (\sin^2 z)^{1/12}$
    (positive). They describe every real $z$ with $\sin z\cos z \ne 0$, with no
    assumption on the signs of $\sin z$ and $\cos z$: $\cot^2 z = 1/t^2$ and
    $(\sin^2 z)^{1/6} = w^2$. The functions of the time enter through the **jet
    variables** `ea` $= e^{a_4}$, `bb` $= b_4$ (both positive) and the symbols of
    their derivatives. The cell writes the eight diagonal entries of the metric as a
    Python list `g` (position 0 is $g_{00}$, position 7 is $g_{77}$) and prints them.
    """),
    code(r'''
    import itertools  # loops over all combinations of indices

    import numpy as np  # arrays of numbers, used for the plots
    import sympy as sp  # exact algebra with symbols

    H = sp.symbols("H", positive=True)  # the constant H of the metric, H > 0
    t = sp.symbols("t", real=True, nonzero=True)  # t = tan z, z = 6 H x0 real
    w = sp.symbols("w", positive=True)  # w = (sin(z)^2)^(1/12) > 0
    ea, bb = sp.symbols("ea bb", positive=True)  # ea = e^(a4), bb = b4 > 0
    ad1, ad2, ad3 = sp.symbols("ad1 ad2 ad3", real=True)  # derivatives 1, 2, 3 of a4
    bd1, bd2, bd3 = sp.symbols("bd1 bd2 bd3", real=True)  # derivatives 1, 2, 3 of b4
    NAMES = ["x0", "x1", "x2", "x3", "x4", "x5", "x6", "x7"]  # positions 0..7
    N = 8  # the number of dimensions
    g = ([bb / (ea ** 2 * t ** 2)]  # g00 = e^(-2 a4) b4 cot(z)^2: the hidden direction
         + [ea ** 2] * 3  # g11 = g22 = g33 = e^(2 a4): 3-space, no warp
         + [sp.Integer(-1)]  # g44 = -1: the time x4
         + [-bb * w ** 2 / ea ** 2] * 3)  # g55 = g66 = g77: the extra times
    for name, entry in zip(NAMES, g):
        say(f"g[{name},{name}] = {entry}")
    '''),
    md(r"""
    The next cell checks four facts. (1) The signs of the diagonal entries, at any
    point (here $t = w = e^{a_4} = b_4 = 1$), are $(+,+,+,+,-,-,-,-)$. (2) The
    determinant of a diagonal matrix is the product of its diagonal entries:
    $\det g = \frac{b_4}{e^{2a_4}t^2}\,(e^{2a_4})^3\,(-1)\,
    \big(-\frac{b_4w^2}{e^{2a_4}}\big)^3 = \frac{b_4^4w^6}{e^{2a_4}t^2}$, that is
    $e^{-2a_4}b_4^4\cot^2 z\,(\sin^2 z)^{1/2}$, so
    $\sqrt{|\det g|} = e^{-a_4}b_4^2\,|\cot z|\,(\sin^2 z)^{1/4}$. (3) Its rate of
    change in time is $\partial_4\ln\sqrt{|g|} = 2u - a_4'$: unlike in the withdrawn
    metric of 2026-10-14, the volume of the seven directions other than the time
    changes. (4) The record of the corrected metric states the same entries.
    """),
    code(r'''
    point = {t: 1, w: 1, ea: 1, bb: 1}  # any point gives the same signs
    signs = [int(sp.sign(entry.subs(point))) for entry in g]
    say(f"signs of the diagonal entries: {signs}")
    check(signs == [1, 1, 1, 1, -1, -1, -1, -1],
          "the signature is (4,4): eta = diag(+,+,+,+,-,-,-,-) in the order x0..x7")
    det_g = sp.Mul(*g)  # the product of the eight diagonal entries
    say(f"det g = {sp.simplify(det_g)}")
    reproduces(sp.simplify(det_g - bb ** 4 * w ** 6 / (ea ** 2 * t ** 2)) == 0,
               "det g = e^(-2 a4) b4^4 cot(z)^2 (sin(z)^2)^(1/2) for every real z",
               WL, "sqrt_abs_det_g")
    log_rate = sp.cancel(ad1 * ea * sp.diff(sp.log(bb ** 2 * w ** 3 / ea), ea)
                         + bd1 * sp.diff(sp.log(bb ** 2 * w ** 3 / ea), bb))
    reproduces(sp.cancel(log_rate - (2 * bd1 / bb - ad1)) == 0,
               "sqrt|g| = e^(-a4) b4^2 |cot z| (sin^2 z)^(1/4) changes at the rate "
               "2 u - a4'", FIELD, "sqrt_det_g")
    reproduces(g[0] == bb / (ea ** 2 * t ** 2) and g[1] == ea ** 2
               and g[5] == -bb * w ** 2 / ea ** 2,
               "the entries are those of the corrected metric", WARPED,
               "corrected_metric_entries")
    '''),
    md(r"""
    ## 7. Derivatives and the Christoffel symbols

    The metric depends on $x_4$ and on $x_0$ only. The function `d(expr, mu)` below
    takes the partial derivative with respect to the coordinate at position `mu`.
    Along $x_4$ it uses the chain rule on the jet variables: $\partial_4 e^{a_4} =
    a_4'e^{a_4}$, $\partial_4 b_4 = b_4'$, $\partial_4 a_4' = a_4''$ and so on (the
    dictionary `RATE`). Along $x_0$ it uses $\partial_0 = 6H\,\partial_z$ with
    $\partial_z t = 1 + t^2$ (the derivative of $\tan z$) and
    $\partial_z\ln w = \tfrac16\cot z$, so $\partial_0 t = 6H(1 + t^2)$ and
    $\partial_0 w = Hw/t$. Two more symbols, `X4` and `Z`, stand for an explicit
    dependence on the time and on the hidden angle; only the source of section 12
    uses them, and nothing else depends on them.

    For a diagonal metric the Christoffel symbols
    $\Gamma^a{}_{bc} = \tfrac12 g^{ad}(\partial_b g_{dc} + \partial_c g_{db}
    - \partial_d g_{bc})$ reduce (only $d = a$ survives, and $g^{aa} = 1/g_{aa}$) to

    $$\Gamma^a{}_{bc} = \frac{1}{2g_{aa}}\big(\delta_{ac}\,\partial_b g_{aa}
    + \delta_{ab}\,\partial_c g_{aa} - \delta_{bc}\,\partial_a g_{bb}\big)$$

    (no sum over $a$ or $b$). The cell computes all $8^3 = 512$ of them, counts those
    that are not zero (31: the 21 distinct ones printed by the cell after it, 10 of
    which appear twice because $\Gamma^a{}_{bc} = \Gamma^a{}_{cb}$ with $b \ne c$) and
    checks that symmetry.
    """),
    code(r'''
    X4, Z = sp.symbols("X4 Z", real=True)  # explicit dependence (the source only)
    RATE = {ea: ea * ad1, bb: bd1, ad1: ad2, ad2: ad3, bd1: bd2, bd2: bd3}


    def d(expr, mu):
        """The partial derivative of expr with respect to the coordinate at position
        mu (0..7 for x0..x7), by the chain rule on the symbols."""
        if mu == 4:
            return (sum(sp.diff(expr, symbol) * rate for symbol, rate in RATE.items())
                    + sp.diff(expr, X4))
        if mu == 0:
            return (6 * H * (1 + t ** 2) * sp.diff(expr, t) + H * w / t * sp.diff(expr, w)
                    + 6 * H * sp.diff(expr, Z))
        return sp.Integer(0)  # nothing depends on x1, x2, x3, x5, x6, x7


    Gamma = [[[sp.Integer(0)] * N for _ in range(N)] for _ in range(N)]  # 512 zeros
    for a, b, c in itertools.product(range(N), repeat=3):  # every index triple
        value = 0
        if a == c:
            value += d(g[a], b)
        if a == b:
            value += d(g[a], c)
        if b == c:
            value -= d(g[b], a)
        Gamma[a][b][c] = sp.cancel(value / (2 * g[a]))  # Gamma^a_bc, diagonal metric
    nonzero = [(a, b, c) for a, b, c in itertools.product(range(N), repeat=3)
               if Gamma[a][b][c] != 0]
    distinct = [(a, b, c) for a, b, c in nonzero if b <= c]
    say(f"{len(nonzero)} of the 512 Christoffel symbols are not zero, "
        f"{len(distinct)} of them distinct")
    check(len(nonzero) == 31, "31 nonzero Christoffel symbols (10 of them twice)")
    check(all(Gamma[a][b][c] == Gamma[a][c][b] for a, b, c in nonzero),
          "Gamma^a_bc = Gamma^a_cb (symmetric in the two lower indices)")
    reproduces(len(distinct) == 21, "21 distinct nonzero Christoffel symbols",
               FIELD, "christoffel_count")
    '''),
    md(r"""
    The next cell prints the 21 distinct Christoffel symbols, each pair
    $\Gamma^a{}_{bc} = \Gamma^a{}_{cb}$ once, with $b_4'$ written as $u\,b_4$ (the
    symbol `uu` is $u = b_4'/b_4$). For example
    $\Gamma^{x_1}{}_{x_1 x_4} = \tfrac12 g^{11}\partial_4 g_{11} = a_4'$ and
    $\Gamma^{x_5}{}_{x_4 x_5} = \Gamma^{x_0}{}_{x_0 x_4} = u/2 - a_4'$: the hidden
    direction and the extra times change at the same rate.
    """),
    code(r'''
    uu, vv, vd = sp.symbols("uu vv vd", real=True)  # u = b4'/b4, v = u', vd = v'
    kk = sp.symbols("kk", real=True)  # k = e^(2 a4)/b4
    for a, b, c in distinct:
        readable = sp.factor(sp.cancel(Gamma[a][b][c].subs(bd1, uu * bb)))
        say(f"Gamma^{NAMES[a]}_{NAMES[b]}{NAMES[c]} = {readable}")
    '''),
    md(r"""
    ## 8. The Riemann tensor

    The Riemann tensor in the sign convention of Misner, Thorne and Wheeler (MTW) is

    $$R^a{}_{bmn} = \partial_m \Gamma^a{}_{bn} - \partial_n \Gamma^a{}_{bm}
    + \Gamma^a{}_{me}\Gamma^e{}_{bn} - \Gamma^a{}_{ne}\Gamma^e{}_{bm}$$

    (sum over $e$), and with the second index raised,
    $R^{ab}{}_{mn} = g^{bb} R^a{}_{bmn}$. It is antisymmetric in $(a, b)$ and in
    $(m, n)$, so only $a \ne b$, $m \ne n$ can be nonzero. `sp.cancel` brings every
    component to one canonical fraction. The helper `record_form` then writes it in
    the record's variables: $b_4' = u\,b_4$, $b_4'' = (v + u^2)\,b_4$ (because
    $v = u' = b_4''/b_4 - u^2$) and $e^{2a_4} = k\,b_4$.
    """),
    code(r'''
    kp = sp.symbols("kp", positive=True)  # k as a positive symbol, used for the root
    TO_RECORD = {bd2: (vv + uu ** 2) * bb, bd1: uu * bb}  # b4'' and b4' through u, v


    def record_form(expr):
        """expr in the record's variables a4', a4'', u, v, k (b4 must drop out)."""
        expr = sp.cancel(expr.subs(TO_RECORD))
        expr = sp.cancel(expr.subs(ea, sp.sqrt(kp * bb)))  # e^(a4) = (k b4)^(1/2)
        return sp.expand(expr).subs(kp, kk)


    R = {}  # R[(a, b, m, n)] = R^{ab}_{mn}; only the components that are not zero
    for a, b, m, n in itertools.product(range(N), repeat=4):
        if a == b or m == n:
            continue  # antisymmetry: zero when the two indices of a pair are equal
        value = (d(Gamma[a][b][n], m) - d(Gamma[a][b][m], n)
                 + sum(Gamma[a][m][e] * Gamma[e][b][n] - Gamma[a][n][e] * Gamma[e][b][m]
                       for e in range(N)))  # R^a_bmn in the MTW convention
        if value != 0:
            value = sp.cancel(value / g[b])  # raise the index b: multiply by g^bb
            if value != 0:
                R[(a, b, m, n)] = record_form(value)
    ordered = {key: value for key, value in R.items()
               if key[0] < key[1] and key[2] < key[3]}  # a < b and m < n
    report("nonzero components R^ab_mn of the 4096", len(R))
    report("nonzero components with a < b and m < n", len(ordered))
    '''),
    md(r"""
    The next cell checks five facts that the Revision record found. (1) There are 112
    nonzero components, 28 of them with $a < b$, $m < n$. (2) Not one contains $t$ or
    $w$: the curvature does not depend on $x_0$, at every real $z$. (3) Every nonzero
    component is **sectional**: $\{m, n\} = \{a, b\}$, one number per plane, and there
    is no mixed component such as $R^{x_5x_0}{}_{x_5x_4}$. (4) Every component is a
    polynomial in $H, a_4', a_4'', u, v, k$. (5) The pair antisymmetry
    $R^{ab}{}_{mn} = -R^{ba}{}_{mn} = -R^{ab}{}_{nm}$.
    """),
    code(r'''
    free = all(not value.has(t) and not value.has(w) and not value.has(bb)
               for value in R.values())
    reproduces(len(R) == 112 and free,
               "112 nonzero components R^ab_mn of the 4096, all free of x0",
               PY, "mixed_riemann_free_of_x0")
    reproduces(len(ordered) == 28 and free,
               "28 nonzero components with a < b and m < n, all free of x0",
               WL, "mixed_riemann_free_of_x0")
    sectional = all(set(key[:2]) == set(key[2:]) for key in R)
    reproduces(sectional, "every nonzero R^ab_mn is sectional: no mixed component",
               PY, "mixed_riemann_only_sectional")
    reproduces(sectional and len(ordered) == 28,
               "the 28 nonzero components are all of the form R^ab_ab",
               WARPED, "corrected_mixed_riemann_vanish")
    polynomial = all(value.is_polynomial(H, ad1, ad2, uu, vv, kk) for value in R.values())
    reproduces(polynomial, "every R^ab_mn is a polynomial in H, a4', a4'', u, v, k",
               PY, "riemann_entries_polynomial")
    antisymmetric = all(R.get((b, a, m, n)) == -v and R.get((a, b, n, m)) == -v
                        for (a, b, m, n), v in R.items())
    reproduces(antisymmetric, "R^ab_mn = -R^ba_mn = -R^ab_nm",
               PY, "riemann_pair_antisymmetry")
    '''),
    md(r"""
    The next cell prints the 28 sectional curvatures $K_{ab} = R^{ab}{}_{ab}$ grouped by
    their value; each member is written `x1x2` for the plane of $x_1$ and $x_2$. Read
    the five groups as follows: two 3-space directions have $(a_4')^2$; a 3-space
    direction with the time has $(a_4')^2 + a_4''$; a 3-space direction with the hidden
    direction or an extra time has $-a_4'(a_4' - u/2)$; the time with the hidden
    direction or an extra time has $(a_4' - u/2)^2 - a_4'' + v/2$; and two directions
    of the block $(x_0, x_5, x_6, x_7)$ have $(a_4' - u/2)^2 - H^2k$, the curvature of
    a space of constant curvature $-H^2$ scaled by the block factor, plus the
    expansion term.
    """),
    code(r'''
    groups = {}  # printed value -> the planes that have it
    for (a, b, m, n), value in ordered.items():
        groups.setdefault(str(sp.factor(value)), []).append(NAMES[a] + NAMES[b])
    for value, members in groups.items():
        say(f"{value} ({len(members)}): " + " ".join(members))
    '''),
    md(r"""
    The next cell draws the curvature at the sample point $H = 1$, $a_4' = 0.6$,
    $a_4'' = 0.3$, $u = 0.8$, $v = 0.1$, $k = 1.5$ in two panels. Left: the 8 by 8
    table of the sectional curvatures $K_{ab}$ (symmetric, zero on the diagonal).
    Right: the 28 by 28 table of all components $R^{ab}{}_{mn}$ with $a < b$ and
    $m < n$; it has entries only on its diagonal, because the curvature has no mixed
    component. Red is positive, blue negative, white zero.
    """),
    code(r'''
    SAMPLE = {H: 1, ad1: sp.Rational(3, 5), ad2: sp.Rational(3, 10), uu: sp.Rational(4, 5),
              vv: sp.Rational(1, 10), kk: sp.Rational(3, 2)}  # the sample point
    pairs = np.zeros((N, N))  # the sectional curvatures K_ab
    for (a, b, m, n), value in ordered.items():
        pairs[a, b] = pairs[b, a] = float(value.subs(SAMPLE))
    PAIRS28 = [(a, b) for a in range(N) for b in range(a + 1, N)]  # the 28 planes
    table = np.zeros((28, 28))
    for i, (a, b) in enumerate(PAIRS28):
        for j, (m, n) in enumerate(PAIRS28):
            if (a, b, m, n) in R:
                table[i, j] = float(R[(a, b, m, n)].subs(SAMPLE))
    limit = np.abs(table).max()  # one colour scale for both panels
    fig, (left, right) = plt.subplots(1, 2, figsize=(12.0, 5.6))
    left.imshow(pairs, cmap="RdBu_r", vmin=-limit, vmax=limit)
    for a in range(N):
        for b in range(N):
            if a != b:  # the value in each cell off the diagonal
                ink = "white" if abs(pairs[a, b]) > 0.6 * limit else "black"
                left.text(b, a, f"{pairs[a, b]:.2f}", ha="center", va="center",
                          fontsize=6, color=ink)
    left.set_xticks(range(N))
    left.set_xticklabels(NAMES, fontsize=7)
    left.set_yticks(range(N))
    left.set_yticklabels(NAMES, fontsize=7)
    left.grid(False)
    left.set_title("sectional curvatures $K_{ab} = R^{ab}{}_{ab}$", fontsize=10)
    image = right.imshow(table, cmap="RdBu_r", vmin=-limit, vmax=limit)
    labels = [NAMES[a] + NAMES[b] for a, b in PAIRS28]
    right.set_xticks(range(28))
    right.set_xticklabels(labels, rotation=90, fontsize=5)
    right.set_yticks(range(28))
    right.set_yticklabels(labels, fontsize=5)
    right.grid(False)
    right.set_title("all $R^{ab}{}_{mn}$, $a<b$, $m<n$", fontsize=10)
    fig.colorbar(image, ax=right, shrink=0.8, label="value (units of $H^2$)")
    save_figure(fig, "pair_curvatures",
                "The curvature of the corrected metric at the sample point $H = 1$, "
                "$a_4' = 0.6$, $a_4^{\\prime\\prime} = 0.3$, $u = 0.8$, $v = 0.1$, "
                "$k = 1.5$, in units of $H^2$. Left: the 8 by 8 table of the sectional "
                "curvatures $K_{ab}$ of the planes of $x_a$ and $x_b$, with the value "
                "in each cell; the five groups of values are visible as blocks. Right: "
                "the 28 by 28 table of all components $R^{ab}{}_{mn}$ with $a < b$, "
                "$m < n$ (rows the upper pairs, columns the lower pairs); only the "
                "diagonal is coloured, because the corrected metric has no mixed "
                "curvature component. Red positive, blue negative, white zero.")
    '''),
    md(r"""
    ## 9. The Ricci tensor, the Ricci scalar and the Einstein tensor

    The Ricci tensor with one index up is $R^h{}_j = \sum_a R^{ah}{}_{aj}$, the Ricci
    scalar $R = \sum_h R^h{}_h$, and the Einstein tensor
    $G^h{}_j = R^h{}_j - \tfrac12\delta^h_j R$. The next cell computes all 64
    components of each and prints $R$ and the diagonal of $G$.
    """),
    code(r'''
    Ricci = [[sp.expand(sum(R.get((a, h, a, j), 0) for a in range(N)))
              for j in range(N)] for h in range(N)]  # R^h_j
    ricci_scalar = sp.expand(sum(Ricci[h][h] for h in range(N)))
    G = [[sp.expand(Ricci[h][j] - (ricci_scalar / 2 if h == j else 0))
          for j in range(N)] for h in range(N)]  # G^h_j
    report("Ricci scalar R", ricci_scalar)
    for h in range(N):
        say(f"G^{NAMES[h]}_{NAMES[h]} = {G[h][h]}")
    '''),
    md(r"""
    The next cell checks the structure of $G$ and compares it with the records: every
    off-diagonal component is zero; the three 3-space components are equal, and the
    hidden component equals the three extra-time components; nothing depends on
    $x_0$; the three distinct components are

    $$G^{x_4}{}_{x_4} = 3(a_4')^2 + 6H^2k - \tfrac32u^2,\qquad
    G^{x_1}{}_{x_1} = -5(a_4')^2 + 6a_4'u + 2a_4'' - \tfrac52u^2 - 2v + 6H^2k,$$
    $$G^{x_0}{}_{x_0} = G^{x_5}{}_{x_5} = -3(a_4')^2 + \tfrac32a_4'u - \tfrac32u^2
    - \tfrac32v + 3H^2k;$$

    they equal the independent record of the corrected metric, whose file
    `warped-metric.json` writes them with `EA` $= e^{a_4}$, `bb` $= b_4$, `bd1`,
    `bd2` for $b_4'$, $b_4''$; and the Ricci scalar and the diagonal Ricci tensor
    equal the field-theory record.
    """),
    code(r'''
    reproduces(all(G[h][j] == 0 for h in range(N) for j in range(N) if h != j),
               "G^h_j is diagonal: every off-diagonal component vanishes",
               LEAD, "einstein_off_diagonal_vanish")
    reproduces(G[1][1] == G[2][2] == G[3][3] and G[0][0] == G[5][5] == G[6][6] == G[7][7],
               "G^x1_x1 = G^x2_x2 = G^x3_x3 and G^x0_x0 = G^x5_x5 = G^x6_x6 = G^x7_x7",
               LEAD, "einstein_isotropy")
    reproduces(all(G[h][h].is_polynomial(H, ad1, ad2, uu, vv, kk) for h in range(N)),
               "every component of G is free of x0, a polynomial in a4', a4'', u, v, k",
               LEAD, "einstein_diagonal_x0_independent")
    expected = {4: 3 * ad1 ** 2 + 6 * H ** 2 * kk - sp.Rational(3, 2) * uu ** 2,
                1: (-5 * ad1 ** 2 + 6 * ad1 * uu + 2 * ad2 - sp.Rational(5, 2) * uu ** 2
                    - 2 * vv + 6 * H ** 2 * kk),
                0: (-3 * ad1 ** 2 + sp.Rational(3, 2) * (ad1 * uu - uu ** 2 - vv)
                    + 3 * H ** 2 * kk)}
    reproduces(all(sp.expand(G[i][i] - v) == 0 for i, v in expected.items()),
               "the three Einstein components agree with the record",
               PY, "einstein_components")
    EA, bd1_r, bd2_r = sp.symbols("EA bd1 bd2", real=True)  # the names of the file
    metric_record = read_json(METRIC_RESULTS)["einstein_diagonal"]
    same = True
    for key, position in (("x0", 0), ("x1", 1), ("x4", 4), ("x5", 5)):
        text = metric_record[key]
        mine = sp.sympify(text, locals={"EA": EA, "H": H, "ad1": ad1, "ad2": ad2,
                                        "bb": bb, "bd1": bd1_r, "bd2": bd2_r})
        mine = mine.subs({bd2_r: (vv + uu ** 2) * bb, bd1_r: uu * bb, EA: sp.sqrt(kp * bb)})
        same = same and sp.expand(sp.cancel(mine).subs(kp, kk) - G[position][position]) == 0
    reproduces(same, "G equals the record of the corrected metric (einstein_diagonal)",
               PY, "einstein_equals_metric_warped_record")
    scalar = (-12 * H ** 2 * kk + 8 * ad1 ** 2 - 2 * ad2 - 8 * ad1 * uu
              + 4 * (vv + uu ** 2) + uu ** 2)  # the record: 4 b4''/b4 + u^2
    reproduces(sp.expand(ricci_scalar - scalar) == 0 and Ricci[0][0] == Ricci[5][5]
               and all(Ricci[h][j] == 0 for h in range(N) for j in range(N) if h != j),
               "R = -12 H^2 k + 8 a4'^2 - 2 a4'' - 8 a4' u + 4 b4''/b4 + u^2; Ricci "
               "diagonal", FIELD, "ricci_scalar")
    '''),
    md(r"""
    The next cell draws the three distinct components of the Einstein tensor along
    the record history $a_4 = Hx_4$, $b_4 = e^{(4/3)Hx_4}$, where $a_4' = H$,
    $u = \tfrac43H$, $a_4'' = v = 0$ and $k = e^{2a_4}/b_4 = e^{(2/3)Hx_4}$, for
    $0 \le x_4 \le 3$ in units $H = 1$. Inserting these values gives
    $G^{x_4}{}_{x_4} = \tfrac13(18k + 1)$, $G^{x_1}{}_{x_1} = \tfrac19(54k - 13)$ and
    $G^{x_0}{}_{x_0} = \tfrac13(9k - 11)$: the curvature of the shrinking block grows
    along the history.
    """),
    code(r'''
    HISTORY = {ad1: H, ad2: 0, uu: sp.Rational(4, 3) * H, vv: 0}  # the record history
    g_history = {i: sp.expand(G[i][i].subs(HISTORY).subs(H, 1)) for i in (4, 1, 0)}
    for i, value in g_history.items():
        say(f"on the record history: G^{NAMES[i]}_{NAMES[i]} = {sp.factor(value)}")
    x_axis = np.linspace(0.0, 3.0, 301)  # the time x4 in units 1/H
    k_axis = np.exp(2.0 * x_axis / 3.0)  # k = e^(2 x4/3)
    fig, ax = plt.subplots()
    styles = {4: ("-", "$G^{x_4}{}_{x_4}$ (constraint)"),
              1: ("--", "$G^{x_1}{}_{x_1}$ (3-space)"),
              0: (":", "$G^{x_0}{}_{x_0} = G^{x_5}{}_{x_5}$ (block)")}
    for i, (style, label) in styles.items():
        function = sp.lambdify(kk, g_history[i], "numpy")
        ax.plot(x_axis, function(k_axis) * np.ones_like(x_axis), style, label=label)
    ax.axhline(0.0, color="black", linewidth=0.8)
    ax.set_xlabel("time $x_4$ (units $1/H$)")
    ax.set_ylabel("component of $G^\\mu{}_\\nu$ (units of $H^2$)")
    ax.set_title("The Einstein tensor along the record history")
    ax.legend(fontsize=8)
    save_figure(fig, "einstein_components",
                "The three distinct components of the Einstein tensor of the corrected "
                "metric along the record history $a_4 = Hx_4$, $b_4 = e^{(4/3)Hx_4}$, "
                "as functions of the time $x_4$ (units $1/H$), in units of $H^2$: the "
                "time component $G^{x_4}{}_{x_4} = (18k + 1)/3$ (solid), the 3-space "
                "component $G^{x_1}{}_{x_1} = (54k - 13)/9$ (dashed) and the common "
                "component of the hidden direction and the extra times "
                "$G^{x_0}{}_{x_0} = (9k - 11)/3$ (dotted), with "
                "$k = e^{2a_4}/b_4 = e^{(2/3)Hx_4}$. All three grow with $k$, the "
                "curvature of the shrinking block; the 3-space and block components "
                "differ, so a source of this history cannot have equal pressures.")
    '''),
    md(r"""
    ## 10. The three Lovelock tensors with the generalized Kronecker delta

    The GKD $\delta^{h_1 \dots h_n}_{j_1 \dots j_n}$ is the determinant of the
    $n \times n$ matrix of ordinary Kronecker deltas $\delta^{h_r}_{j_s}$. That
    determinant is $0$ when two upper (or two lower) indices are equal (two equal
    rows), and otherwise the sign of the permutation that turns the upper list into
    the lower list (or $0$ when the two lists hold different indices). The next cell
    implements it by counting *inversions*: pairs of positions that appear in the
    wrong order. It prints three small examples and checks that 9 indices in 8
    dimensions always give 0 (two of them must be equal): so there is no fourth
    Lovelock tensor in 8 dimensions.
    """),
    code(r'''
    def gkd(upper, lower):
        """The generalized Kronecker delta: +1 (-1) if lower is an even (odd)
        rearrangement of upper without a repeated index, otherwise 0."""
        if len(set(upper)) != len(upper) or sorted(upper) != sorted(lower):
            return 0
        position = [upper.index(index) for index in lower]  # where each one sits
        inversions = sum(1 for i in range(len(position))
                         for j in range(i + 1, len(position))
                         if position[i] > position[j])
        return -1 if inversions % 2 else 1


    say(f"gkd([1, 2], [1, 2]) = {gkd([1, 2], [1, 2])}, gkd([1, 2], [2, 1]) = "
        f"{gkd([1, 2], [2, 1])}, gkd([1, 1], [1, 1]) = {gkd([1, 1], [1, 1])}")
    nine = list(range(8)) + [0]  # nine indices from eight values: one repeats
    reproduces(gkd(nine, nine) == 0 and gkd(list(range(8)), list(range(8))) == 1,
               "a GKD of 9 indices in 8 dimensions is 0: P_(4) = 0",
               WL, "P4_vanishes_pigeonhole")
    '''),
    md(r"""
    In $P_{(k)}{}^h{}_j$ every curvature factor $R^{j_1 j_2}{}_{h_1 h_2}$ appears with
    its index pairs in both orders. Exchanging $j_1, j_2$ changes the sign of $R$ and
    of the GKD (one more inversion), so both orders give the same term; the same holds
    for $h_1, h_2$. Hence the full sum is $4^k$ times the sum over the 28 components
    with $j_1 < j_2$ and $h_1 < h_2$. The next cell does this sum for $k = 1, 2, 3$,
    together with the Lovelock scalar $L_{(k)}$ (the same sum without $h$ and $j$).
    To multiply fast, each component is stored as a sympy polynomial in
    $H, a_4', a_4'', u, v, k$.
    """),
    code(r'''
    GENERATORS = (H, ad1, ad2, uu, vv, kk)
    FACTORS = [(key, sp.Poly(value, *GENERATORS)) for key, value in ordered.items()]


    def lovelock(k):
        """P_(k)^h_j (8 x 8 list of expressions), L_(k) and the number of terms."""
        zero = sp.Poly(0, *GENERATORS)
        P = [[zero] * N for _ in range(N)]
        L = zero
        terms = 0
        for factors in itertools.product(FACTORS, repeat=k):
            lower = [i for key, _ in factors for i in key[0:2]]  # upper indices of R
            upper = [i for key, _ in factors for i in key[2:4]]  # lower indices of R
            if len(set(lower)) < 2 * k or len(set(upper)) < 2 * k:
                continue  # a repeated index: the GKD is zero
            terms += 1
            product = sp.Poly(4 ** k, *GENERATORS)  # the factor 4^k
            for _, poly in factors:
                product = product * poly
            L = L + gkd(upper, lower) * product
            for h, j in itertools.product(range(N), repeat=2):
                sign = gkd([h] + upper, [j] + lower)
                if sign:
                    P[h][j] = P[h][j] + sign * product
        P = [[sp.expand(P[h][j].as_expr()) for j in range(N)] for h in range(N)]
        return P, sp.expand(L.as_expr()), terms


    P, Lscalar, E = {}, {}, {}
    for k in (1, 2, 3):
        P[k], Lscalar[k], terms = lovelock(k)
        E[k] = [[sp.expand(-P[k][h][j] / 2 ** (k + 1)) for j in range(N)]
                for h in range(N)]  # E_(k) = -P_(k)/2^(k+1)
        say(f"k = {k}: {terms} lists of index pairs contribute; L_({k}) has "
            f"{len(Lscalar[k].args)} terms")
    say(f"L_(1) = {Lscalar[1]}")
    '''),
    md(r"""
    The next cell checks what the Revision record found about these tensors:
    $E_{(1)} = G$ in all 64 components ($P_{(1)} = -4G$); each $E_{(k)}$ is diagonal,
    a polynomial in $H, a_4', a_4'', u, v, k$, equal in the three 3-space directions,
    and equal in the hidden direction and the three extra times; the trace identity
    $\sum_h P_{(k)}{}^h{}_h = (8 - 2k) L_{(k)}$; and the scalars $L_{(k)}$ agree with
    the Rust program of the GKD record. The Rust record writes $L_{(k)}$ as a text in
    the Wolfram Language with `b4[x4]`, its derivatives and `E^(2*a4[x4])`; the helper
    `from_mathematica` replaces them by $b_4$, $u\,b_4$, $(v + u^2)\,b_4$ and
    $k\,b_4$. Because every nonzero Riemann component is sectional, the sum of the GKD
    collapses: a set of $k$ disjoint planes that do not contain $x_h$ enters with
    $k!\,2^k$ orders of the upper indices and $2^k$ orders of the lower ones, each with
    the product of the $k$ sectional curvatures, so that
    $E_{(k)}{}^h{}_h = -k!\,2^{k-1}\sum\prod K$ over these sets. The last lines of the
    cell check this formula in the eight diagonal components for $k = 1, 2, 3$.
    """),
    code(r'''
    reproduces(all(sp.expand(E[1][h][j] - G[h][j]) == 0
                   for h in range(N) for j in range(N)),
               "E_(1) = G in all 64 components (P_(1) = -4 G)",
               PY, "P1_equals_minus_4_Einstein")
    lovelock_json = read_json(LOVELOCK)


    def from_mathematica(text):
        """A Wolfram text of the Rust record as a sympy expression in u, v, k."""
        for old, new in (("Derivative[2][b4][x4]", "((vv + uu**2)*bb)"),
                         ("Derivative[1][b4][x4]", "(uu*bb)"),
                         ("Derivative[2][a4][x4]", "ad2"),
                         ("Derivative[1][a4][x4]", "ad1"),
                         ("E^(4*a4[x4])", "(kk*bb)**2"), ("E^(2*a4[x4])", "(kk*bb)"),
                         ("b4[x4]", "bb"), ("^", "**")):
            text = text.replace(old, new)
        names = {"H": H, "ad1": ad1, "ad2": ad2, "uu": uu, "vv": vv, "kk": kk, "bb": bb}
        return sp.expand(sp.sympify(text, locals=names))


    for k in (1, 2, 3):
        Ek = E[k]
        structure = (all(Ek[h][j] == 0 for h in range(N) for j in range(N) if h != j)
                     and Ek[1][1] == Ek[2][2] == Ek[3][3]
                     and Ek[0][0] == Ek[5][5] == Ek[6][6] == Ek[7][7]
                     and all(Ek[h][h].is_polynomial(*GENERATORS) for h in range(N)))
        reproduces(structure, f"E_({k}) diagonal, x1 = x2 = x3, x0 = x5 = x6 = x7",
                   PY, f"P{k}_structure")
        trace = sp.expand(sum(P[k][h][h] for h in range(N)) - (8 - 2 * k) * Lscalar[k])
        reproduces(trace == 0, f"trace identity sum_h P_({k})^h_h = (8 - {2 * k}) L_({k})",
                   PY, f"P{k}_trace_identity")
        rust = from_mathematica(lovelock_json[f"L{k}"])
        reproduces(sp.expand(rust - Lscalar[k]) == 0,
                   f"L_({k}) equals the Rust GKD program", PY, f"L{k}_equals_gkd_branch")
    K_plane = {(a, b): value for (a, b, m, n), value in ordered.items()}  # K_ab, a < b
    counting = True
    for k, h in itertools.product((1, 2, 3), range(N)):
        planes = [plane for plane in K_plane if h not in plane]  # the planes without h
        total = sum((sp.Mul(*[K_plane[plane] for plane in chosen])
                     for chosen in itertools.combinations(planes, k)
                     if len({i for plane in chosen for i in plane}) == 2 * k), 0)
        counting = counting and sp.expand(-sp.factorial(k) * 2 ** (k - 1) * total
                                          - E[k][h][h]) == 0
    check(counting, "E_(k)^h_h = -k! 2^(k-1) x the sum over k disjoint planes without h "
          "of the products of their K (k = 1, 2, 3)")
    '''),
    md(r"""
    The Rust program `lovelock_gkd` of the GKD record stored every component of
    $P_{(k)}{}^h{}_j$ as a list of monomials: a fraction and the 14 exponents of $H$,
    $a_4', a_4'', a_4''', a_4''''$, $E = e^{a_4}$, $W = (\sin^2 z)^{1/12}$,
    $C = \cot z$, $Q = b_4^{1/2}$, $b_4', b_4'', b_4''', b_4''''$ and
    $\mathrm{sgn}(\cot z)$. The helper `from_monomials` turns such a list into a sympy
    expression in the record's variables ($E = k^{1/2}Q$, $b_4' = uQ^2$,
    $b_4'' = (v + u^2)Q^2$) and requires the exponents of $W$, $C$, the sign and the
    third and fourth derivatives to be zero. The next cell rebuilds all $3 \times 64$
    components and compares them with ours; it also compares the four stored
    components of each $E_{(k)}$ with the Wolfram record `a4-equations.json`.
    """),
    code(r'''
    Q = sp.symbols("Q", positive=True)  # Q = b4^(1/2)


    def from_monomials(monomials):
        """A component of the Rust record as a sympy expression in u, v, k."""
        total = sp.Integer(0)
        for numerator, denominator, exponents in monomials:
            if any(exponents[i] for i in (3, 4, 6, 7, 11, 12, 13)):
                raise ValueError(f"unexpected exponents {exponents}")
            term = sp.Rational(numerator, denominator)
            term *= H ** exponents[0] * ad1 ** exponents[1] * ad2 ** exponents[2]
            term *= (sp.sqrt(kp) * Q) ** exponents[5] * Q ** exponents[8]
            term *= (uu * Q ** 2) ** exponents[9]  # b4' = u b4
            term *= ((vv + uu ** 2) * Q ** 2) ** exponents[10]  # b4'' = (v + u^2) b4
            total += term
        return sp.expand(total).subs(kp, kk)


    for k in (1, 2, 3):
        block = lovelock_json[f"P{k}_mixed_up_h_down_j"]
        same = all(sp.expand(from_monomials(block[f"{NAMES[h]},{NAMES[j]}"]["monomials"])
                             - P[k][h][j]) == 0 for h in range(N) for j in range(N))
        reproduces(same, f"all 64 components of P_({k}) equal the Rust GKD record",
                   PY, f"P{k}_equals_gkd_branch_monomials")
    equations_json = read_json(EQUATIONS)
    LOCALS = {"ad1": ad1, "ad2": ad2, "uu": uu, "vv": vv, "kk": kk, "H": H}


    def parse(text, names=None):
        """A Wolfram InputForm text of the record as a sympy expression."""
        return sp.sympify(text.replace("^", "**"), locals=names or LOCALS)


    POSITIONS = {"x0x0": 0, "x1x1": 1, "x4x4": 4, "x5x5": 5}
    same = all(sp.expand(parse(equations_json["lovelockTensors"][f"E{k}"][key]["input"])
                         - E[k][i][i]) == 0
               for k in (1, 2, 3) for key, i in POSITIONS.items())
    reproduces(same, "E_(1), E_(2), E_(3) equal the Wolfram record a4-equations.json",
               PY, "json_lovelock_components")
    '''),
    md(r"""
    **An independent route to $E_{(2)}$.** The Gauss-Bonnet tensor has a classical
    formula (Lanczos), written here with one index up:

    $$H^\mu{}_\nu = 2\big(R\,R^\mu{}_\nu - 2R^\mu{}_a R^a{}_\nu
    - 2R^{\mu a}{}_{\nu b} R^b{}_a + R^{\mu a}{}_{bc} R^{bc}{}_{\nu a}\big)
    - \tfrac12\delta^\mu_\nu\big(R^2 - 4R^a{}_b R^b{}_a
    + R^{ab}{}_{cd} R^{cd}{}_{ab}\big).$$

    It uses no GKD. The next cell computes it from our Riemann tensor for general
    $a_4$ and $b_4$ and checks that it equals $E_{(2)}$ in all 64 components. On the
    exponential histories ($a_4' = AH$, $u = \beta AH$, $a_4'' = v = 0$) it then
    reproduces the lead's formula for $H^{x_4}{}_{x_4}$ and the record's statement
    that the $\alpha_2$ parts of the required source are $-H^{x_4}{}_{x_4}$,
    $H^{x_1}{}_{x_1}$ and $H^{x_0}{}_{x_0}$.
    """),
    code(r'''
    def contract(mu, nu):
        """The four products in the bracket of the Lanczos formula."""
        term_a = ricci_scalar * Ricci[mu][nu]
        term_b = sum(Ricci[mu][a] * Ricci[a][nu] for a in range(N))
        term_c = sum(R.get((mu, a, nu, b), 0) * Ricci[b][a]
                     for a in range(N) for b in range(N))
        term_d = sum(R.get((mu, a, b, c), 0) * R.get((b, c, nu, a), 0)
                     for a in range(N) for b in range(N) for c in range(N))
        return 2 * (term_a - 2 * term_b - 2 * term_c + term_d)


    gauss_bonnet_scalar = (ricci_scalar ** 2
                           - 4 * sum(Ricci[a][b] * Ricci[b][a]
                                     for a in range(N) for b in range(N))
                           + sum(v * R.get((m, n, a, b), 0)
                                 for (a, b, m, n), v in R.items()))
    lanczos = [[sp.expand(contract(mu, nu)
                          - (gauss_bonnet_scalar / 2 if mu == nu else 0))
                for nu in range(N)] for mu in range(N)]
    check(all(sp.expand(lanczos[h][j] - E[2][h][j]) == 0
              for h in range(N) for j in range(N)),
          "E_(2) (GKD) equals the classical Gauss-Bonnet tensor for every a4 and b4")
    A, beta = sp.symbols("A beta", real=True)  # the exponential history
    EXPONENTIAL = {ad1: A * H, ad2: 0, uu: beta * A * H, vv: 0}
    lead_formula = (-3 * H ** 4 * (A ** 4 * beta ** 4 + 16 * A ** 4 * beta ** 3
                                   - 48 * A ** 4 * beta ** 2 + 48 * A ** 4
                                   - 8 * A ** 2 * beta ** 2 * kk - 64 * A ** 2 * beta * kk
                                   + 64 * A ** 2 * kk + 16 * kk ** 2) / 4)
    reproduces(sp.expand(lanczos[4][4].subs(EXPONENTIAL) - lead_formula) == 0,
               "exponential history: H^x4_x4 equals the lead's formula",
               LEAD, "gauss_bonnet_diagonal")
    alpha2 = sp.symbols("alpha2", real=True)
    required = equations_json["exponentialHistory"]["requiredSource"]
    names_exp = {"AA": A, "be": beta, "H": H, "kk": kk, "alpha2": alpha2}
    parts = {key: sp.diff(sp.sympify(required[key]["input"].replace("^", "**"),
                                     locals=dict(names_exp, kappa=sp.Integer(1))), alpha2)
             for key in ("rho", "p3", "p0", "pt")}
    signs = {"rho": (4, -1), "p3": (1, 1), "p0": (0, 1), "pt": (5, 1)}
    reproduces(all(sp.expand(parts[key] - sign * lanczos[i][i].subs(EXPONENTIAL)) == 0
                   for key, (i, sign) in signs.items()),
               "the alpha2 parts of the required source are -H^x4_x4, H^x1_x1, H^x0_x0",
               LEAD, "gauss_bonnet_source_alpha2")
    '''),
    md(r"""
    **The Bianchi identity.** Lovelock's theorem says that each $E_{(k)}$ has zero
    divergence for every metric. The next cell checks this directly. For a diagonal
    tensor whose entries depend on $x_4$ only, the covariant divergence
    $\nabla_\mu T^\mu{}_\nu = \partial_\mu T^\mu{}_\nu + \Gamma^\mu{}_{\mu l}T^l{}_\nu
    - \Gamma^l{}_{\mu\nu}T^\mu{}_l$ becomes
    $\partial_\nu T^\nu{}_\nu + \sum_\mu\Gamma^\mu{}_{\mu\nu}
    \big(T^\nu{}_\nu - T^\mu{}_\mu\big)$ (no sum over $\nu$). The time derivative of
    an expression in the record's variables uses $a_4''$, $a_4'''$ (`ad3`), $u' = v$,
    $v'$ (`vd`) and $k' = k(2a_4' - u)$ (the dictionary `RATE_RECORD`).
    """),
    code(r'''
    RATE_RECORD = {ad1: ad2, ad2: ad3, uu: vv, vv: vd, kk: kk * (2 * ad1 - uu)}


    def d4_record(expr):
        """The x4 derivative of an expression in a4', a4'', u, v, k."""
        return sp.expand(sum(sp.diff(expr, s) * r for s, r in RATE_RECORD.items()))


    trace_gamma = [record_form(sum(Gamma[m][m][nu] for m in range(N))) for nu in range(N)]
    say(f"sum_mu Gamma^mu_mu x4 = {trace_gamma[4]}, sum_mu Gamma^mu_mu x0 = "
        f"{trace_gamma[0]}")


    def divergence_diagonal(T):
        """nabla_mu T^mu_nu of a diagonal tensor that depends on x4 only."""
        values = []
        for nu in range(N):
            value = d4_record(T[4][4]) if nu == 4 else 0
            value += sum(record_form(Gamma[m][m][nu]) * (T[nu][nu] - T[m][m])
                         for m in range(N))
            values.append(sp.expand(value))
        return values


    for k in (1, 2, 3):
        reproduces(all(value == 0 for value in divergence_diagonal(E[k])),
                   f"nabla_mu E_({k})^mu_nu = 0 for nu = x0..x7",
                   PY, f"E{k}_divergence_free")
    '''),
    md(r"""
    The next cell draws the diagonal of $E_{(1)}, E_{(2)}, E_{(3)}$ at the sample point
    of section 8 as three 8 by 8 heat maps, with the value written in each diagonal
    cell. Each panel has its own colour scale. All three tensors have the same
    pattern: diagonal, one value for $x_1 = x_2 = x_3$, one for $x_4$, and one for the
    block $x_0 = x_5 = x_6 = x_7$.
    """),
    code(r'''
    fig, axes = plt.subplots(1, 3, figsize=(12.0, 4.4))
    for ax, k in zip(axes, (1, 2, 3)):
        values = np.array([[float(E[k][h][j].subs(SAMPLE)) for j in range(N)]
                           for h in range(N)])
        scale = np.abs(values).max()
        ax.imshow(values, cmap="RdBu_r", vmin=-scale, vmax=scale)
        for h in range(N):  # write each diagonal value into its cell
            value = values[h, h]
            ink = "white" if abs(value) > 0.6 * scale else "black"  # readable on dark
            ax.text(h, h, f"{value:.2f}", ha="center", va="center", fontsize=6.5,
                    color=ink)
        ax.set_xticks(range(N))
        ax.set_xticklabels(NAMES, fontsize=7)
        ax.set_yticks(range(N))
        ax.set_yticklabels(NAMES, fontsize=7)
        ax.grid(False)
        ax.set_title(f"$E_{{({k})}}{{}}^h{{}}_j$")
    fig.suptitle("The three Lovelock tensors at the sample point (row $h$, column $j$)")
    save_figure(fig, "lovelock_heat_maps",
                "The three Lovelock tensors $E_{(1)}$ (the Einstein tensor), $E_{(2)}$ "
                "(the Gauss-Bonnet tensor) and $E_{(3)}$ of the corrected metric as 8 by "
                "8 tables, row $h$ and column $j$ running over $x_0$ to $x_7$, evaluated "
                "at $H = 1$, $a_4' = 0.6$, $a_4^{\\prime\\prime} = 0.3$, $u = 0.8$, "
                "$v = 0.1$, $k = 1.5$; the colour is the value (each panel with its own "
                "scale, red positive, blue negative, white zero) and the number in each "
                "diagonal cell is the value. All off-diagonal entries are zero, and "
                "each tensor has only three different diagonal values: one for "
                "3-space, one for the time, and one for the hidden direction and the "
                "three extra times together.")
    '''),
    md(r"""
    ## 11. The field equations and their independent components

    The next cell writes the left-hand side
    $\sum_k \alpha_k E_{(k)}{}^h{}_j + \Lambda\delta^h_j$ and checks that every
    off-diagonal left-hand side is zero (so the field equations there read
    $0 = \kappa T^h{}_j$: the source must have no mixed component at all), that the
    three 3-space components are equal, and that the hidden component equals the
    three extra-time components (so the source must have $p_0 = p_t$). Three
    independent components remain. The cell names them `e44` (time), `e11` (3-space)
    and `e00` (hidden direction and extra times), each without the $\Lambda$.
    """),
    code(r'''
    alpha1, alpha3 = sp.symbols("alpha1 alpha3", real=True)  # alpha2 is defined above
    Lam, kappa = sp.symbols("Lam kappa", real=True)  # Lambda and kappa
    rho, p3, pt, p0 = sp.symbols("rho p3 pt p0", real=True)  # the source
    ALPHA = {1: alpha1, 2: alpha2, 3: alpha3}
    LHS = [[sp.expand(sum(ALPHA[k] * E[k][h][j] for k in (1, 2, 3))
                      + (Lam if h == j else 0)) for j in range(N)] for h in range(N)]
    off_diagonal_zero = all(LHS[h][j] == 0 for h in range(N) for j in range(N)
                            if h != j)
    groups_equal = (LHS[1][1] == LHS[2][2] == LHS[3][3]
                    and LHS[0][0] == LHS[5][5] == LHS[6][6] == LHS[7][7])
    reproduces(off_diagonal_zero and groups_equal,
               "every off-diagonal left-hand side is 0; three independent components",
               WL, "independent_components")
    e44, e11, e00 = (sp.expand(LHS[i][i] - Lam) for i in (4, 1, 0))
    reproduces(LHS[0][0] == LHS[5][5],
               "hidden and extra-time components are one expression: p0 = p_t",
               PY, "independent_components")
    say(f"Einstein part of the constraint: {e44.coeff(alpha1)}")
    '''),
    md(r"""
    **The constraint and the system of second order.** The time component contains
    $a_4'$, $u$ and $k$ but neither $a_4''$ nor $v$: it is a constraint on the first
    derivatives. The 3-space and the hidden components are linear in $(a_4'', v)$:

    $$J\begin{pmatrix}a_4''\\ v\end{pmatrix} = \begin{pmatrix}\kappa p_3 - \Lambda
    - e_{11}|_{a_4'' = v = 0}\\ \kappa p_0 - \Lambda - e_{00}|_{a_4'' = v = 0}
    \end{pmatrix},\qquad J = \begin{pmatrix}\partial e_{11}/\partial a_4'' &
    \partial e_{11}/\partial v\\ \partial e_{00}/\partial a_4'' &
    \partial e_{00}/\partial v\end{pmatrix}.$$

    Where $\det J \ne 0$ they determine $a_4''$ and $v$. The next cell checks this,
    prints $\det J$ for Einstein gravity ($-3$), checks the Einstein Jacobian with
    respect to $(a_4'', b_4'')$ (because $v = b_4''/b_4 - u^2$, a column of $J$ is
    divided by $b_4$), and compares the three equations, $J$ and $\det J$ with the
    record.
    """),
    code(r'''
    reproduces(not e44.has(ad2) and not e44.has(vv),
               "the x4 component contains a4', u and k but no a4'' and no v",
               PY, "constraint_first_order")
    J = sp.Matrix([[sp.diff(e11, ad2), sp.diff(e11, vv)],
                   [sp.diff(e00, ad2), sp.diff(e00, vv)]])
    linear = all(sp.diff(e, x, y) == 0 for e in (e11, e00)
                 for x in (ad2, vv) for y in (ad2, vv))
    det_J = sp.expand(J.det())
    EINSTEIN = {alpha1: 1, alpha2: 0, alpha3: 0}
    report("det J in Einstein gravity", det_J.subs(EINSTEIN))
    reproduces(linear and det_J.subs(EINSTEIN) == -3,
               "x1 and x0 components linear in (a4'', v), Einstein det J = -3",
               WL, "second_order_system_a4pp_vv")
    J_b = sp.Matrix([[J[0, 0], J[0, 1] / bb], [J[1, 0], J[1, 1] / bb]]).subs(EINSTEIN)
    reproduces(J_b == sp.Matrix([[2, -2 / bb], [0, -sp.Rational(3, 2) / bb]]),
               "Einstein: Jacobian with respect to (a4'', b4'') is {{2, -2/b4}, "
               "{0, -3/(2 b4)}}", WL, "einstein_second_order_system")
    general = equations_json["generalSource"]
    NAMES_RECORD = {"ad1": ad1, "ad2": ad2, "uu": uu, "vv": vv, "kk": kk, "H": H,
                    "alpha1": alpha1, "alpha2": alpha2, "alpha3": alpha3, "Lam": Lam,
                    "kappa": kappa, "rho": rho, "p3": p3, "pt": pt, "p0": p0}


    def parse_equation(text):
        """An equation "left == right" of the record as left - right."""
        left, right = text.split(" == ")
        return sp.expand(parse(left, NAMES_RECORD) - parse(right, NAMES_RECORD))


    mine = {"constraint_x4": e44 + Lam + kappa * rho,
            "space_x1_eq_x2_eq_x3": e11 + Lam - kappa * p3,
            "hidden_and_extraTimes_x0_eq_x5_eq_x6_eq_x7": e00 + Lam - kappa * p0}
    same = all(sp.expand(parse_equation(general[key]["input"]) - value) == 0
               for key, value in mine.items())
    J_text = general["secondOrderJacobian"]["input"].replace("{", "[").replace("}", "]")
    same = (same and sp.expand(sp.Matrix(parse(J_text, NAMES_RECORD)) - J)
            == sp.zeros(2, 2)
            and sp.expand(parse(general["secondOrderJacobianDet"]["input"], NAMES_RECORD)
                          - det_J) == 0)
    reproduces(same, "the three equations, J and det J equal the record",
               PY, "json_general_source_equations")
    '''),
    md(r"""
    **The constraint propagates (Bianchi identity).** The time component depends on
    $x_4$ only through $a_4'$, $u$ and $k$. The next cell checks the identity

    $$\frac{d}{dx_4}e_{44} = 3a_4'\,(e_{11} - e_{44}) + 4h_4\,(e_{00} - e_{44}),
    \qquad h_4 = \tfrac12u - a_4',$$

    for every coupling. With the conservation law of section 12 it says: if the
    constraint holds at one time and the two equations of second order hold at every
    time, the constraint holds at every time.
    """),
    code(r'''
    h4 = uu / 2 - ad1  # the rate of the block (x0, x5, x6, x7)
    reproduces(sp.expand(d4_record(e44) - 3 * ad1 * (e11 - e44) - 4 * h4 * (e00 - e44))
               == 0, "d/dx4 e44 = 3 a4' (e11 - e44) + 4 h4 (e00 - e44)",
               PY, "bianchi_x4")
    '''),
    md(r"""
    The next cell draws $\det J$ along the record history ($a_4' = H$,
    $u = \tfrac43H$, $k = e^{(2/3)Hx_4}$, units $H = 1$) for Einstein gravity
    ($-3$), for Einstein-Gauss-Bonnet gravity with $\alpha_2H^2 = 0.01$ and $1/32$, and
    for the author's weights. Where $\det J = 0$ the two equations of second order
    could not be solved for $a_4''$ and $v$. Along this history it stays negative in
    all four cases. For Einstein-Gauss-Bonnet gravity this holds for every $\alpha_2$:
    on the history $\det J$ is $-1/9$ times a quadratic polynomial in $\alpha_2$ whose
    discriminant $256 - 2016k - 1863k^2$ (times a positive factor) is negative for
    $k \ge 1$, so it has no real root.
    """),
    code(r'''
    on_history = {ad1: 1, uu: sp.Rational(4, 3), H: 1}  # the record history, H = 1
    AUTHOR = {alpha1: 1, alpha2: sp.Rational(1, 32), alpha3: sp.Rational(1, 1152)}
    cases = [("Einstein", EINSTEIN, "-"),
             ("Gauss-Bonnet $\\alpha_2H^2 = 0.01$",
              {alpha1: 1, alpha2: sp.Rational(1, 100), alpha3: 0}, "--"),
             ("Gauss-Bonnet $\\alpha_2H^2 = 1/32$",
              {alpha1: 1, alpha2: sp.Rational(1, 32), alpha3: 0}, "-."),
             ("author's weights", AUTHOR, ":")]
    fig, ax = plt.subplots()
    negative = True
    for label, couplings, style in cases:
        value = sp.expand(det_J.subs(couplings).subs(on_history))
        function = sp.lambdify(kk, value, "numpy")
        curve = function(k_axis) * np.ones_like(k_axis)
        negative = negative and bool(np.all(curve < 0))
        ax.plot(x_axis, curve, style, label=label)
    check(negative, "det J < 0 along the record history for the four couplings")
    gauss_bonnet = sp.expand(det_J.subs({alpha1: 1, alpha3: 0}).subs(on_history))
    polynomial_a2 = sp.Poly(sp.expand(-9 * gauss_bonnet), alpha2)
    c2, c1, c0 = polynomial_a2.all_coeffs()  # in alpha2: c2 a2^2 + c1 a2 + c0
    discriminant = sp.Poly(sp.expand((c1 ** 2 - 4 * c2 * c0) / 144), kk)
    leading, middle, constant = discriminant.all_coeffs()  # 256 - 2016 k - 1863 k^2
    say(f"Gauss-Bonnet on the history: det J = -(1/9) ({polynomial_a2.as_expr()})")
    say(f"its discriminant in alpha2 is 144 ({discriminant.as_expr()})")
    check(discriminant.eval(1) < 0 and leading < 0 and middle < 0,
          "Gauss-Bonnet: det J has no real zero in alpha2 for k >= 1 (no breakdown)")
    ax.axhline(0.0, color="black", linewidth=0.8)
    ax.set_xlabel("time $x_4$ (units $1/H$)")
    ax.set_ylabel("$\\det J$")
    ax.set_title("The Jacobian of the second-order system along the record history")
    ax.legend(fontsize=8)
    save_figure(fig, "jacobian_determinant",
                "The determinant of the Jacobian $J$ with which $a_4^{\\prime\\prime}$ "
                "and $v = (b_4'/b_4)'$ enter the 3-space and hidden equations, along "
                "the record history $a_4 = Hx_4$, $b_4 = e^{(4/3)Hx_4}$, as a function "
                "of the time $x_4$ (units $1/H$, $H = 1$): Einstein gravity ($-3$, "
                "solid), Einstein-Gauss-Bonnet gravity with $\\alpha_2H^2 = 0.01$ "
                "(dashed) and $1/32$ (dash-dotted), and the author's weights (dotted). "
                "All four stay below zero, so along this history the two equations of "
                "second order can always be solved for $a_4^{\\prime\\prime}$ and $v$; "
                "where $\\det J$ vanished they could not.")
    '''),
    md(r"""
    ## 12. The conservation law of the source

    The Bianchi identity makes the divergence of the left-hand side zero, so the field
    equations can hold only if the source has zero divergence too. The next cell
    computes $\nabla_\mu T^\mu{}_\nu$ for a general source whose six parts
    $\rho, p_3, p_t, p_0, q_{40}, q_{04}$ are arbitrary functions of the time and of
    the hidden angle (sympy functions of `X4` and `Z`), and compares it with the
    record. With $h_4 = \tfrac12u - a_4'$ the record's result is

    $$\nabla_\mu T^\mu{}_{x_4} = -\partial_4\rho - 3a_4'(\rho + p_3)
    - 3h_4(\rho + p_t) - h_4(\rho + p_0) + \partial_0 q_{04}
    - 3H(\cot z + 2\tan z)\,q_{04},$$
    $$\nabla_\mu T^\mu{}_{x_0} = \partial_0 p_0 + 3H\cot z\,(p_0 - p_t)
    + \partial_4 q_{40} + \tfrac32u\,q_{40} - h_4\cot^2 z\,q_{04}/k,$$

    and zero for the six other $\nu$. The record writes $\partial_0 q_{04}$ as `d0q04`,
    $\cot z$ as `cc` and $\tan z$ as `tt`; the dictionary `MAP` gives them their
    meaning. Without mixed components the two lines are the lead's formulas.
    """),
    code(r'''
    source = {name: sp.Function(name)(X4, Z)
              for name in ("rho", "p3", "pt", "p0", "q40", "q04")}  # f(x4, z)
    T = [[sp.Integer(0)] * N for _ in range(N)]
    for i, name in enumerate(["p0", "p3", "p3", "p3", "rho", "pt", "pt", "pt"]):
        T[i][i] = source[name]
    T[4][4] = -source["rho"]  # T^x4_x4 = -rho
    T[4][0], T[0][4] = source["q40"], source["q04"]


    def divergence(T):
        """nabla_mu T^mu_nu of a mixed tensor T (8 x 8 list), for nu = x0..x7."""
        return [record_form(sp.cancel(
                    sum(d(T[m][n], m) for m in range(N))
                    + sum(Gamma[m][m][l] * T[l][n] for m in range(N) for l in range(N))
                    - sum(Gamma[l][m][n] * T[m][l] for m in range(N) for l in range(N))))
                for n in range(N)]


    divT = divergence(T)
    MAP = {"d0q04": 6 * H * sp.diff(source["q04"], Z), "d4rho": sp.diff(source["rho"], X4),
           "d0p0": 6 * H * sp.diff(source["p0"], Z), "d4q40": sp.diff(source["q40"], X4),
           "cc": 1 / t, "tt": t, "ad1": ad1, "uu": uu, "kk": kk, "H": H}
    MAP.update(source)
    record_x4, record_x0 = (sp.sympify(general[key]["input"].split(" == ")[0]
                                       .replace("^", "**"), locals=MAP)
                            for key in ("conservation_x4", "conservation_x0"))
    reproduces(sp.simplify(divT[4] - record_x4) == 0
               and sp.simplify(divT[0] - record_x0) == 0,
               "nabla_mu T^mu_x4 and nabla_mu T^mu_x0 as in the record",
               PY, "json_conservation")
    no_mixed = {source["q40"]: 0, source["q04"]: 0}
    lead_x4 = (-sp.diff(source["rho"], X4) - 3 * ad1 * (source["rho"] + source["p3"])
               - 3 * h4 * (source["rho"] + source["pt"]) - h4 * (source["rho"]
                                                               + source["p0"]))
    lead_x0 = 6 * H * sp.diff(source["p0"], Z) + 3 * H / t * (source["p0"] - source["pt"])
    reproduces(sp.simplify(divT[4].subs(no_mixed).doit() - lead_x4) == 0,
               "diagonal source: nabla_mu T^mu_x4 as in the lead's record",
               EMT, "divergence_x4_component")
    reproduces(sp.simplify(divT[0].subs(no_mixed).doit() - lead_x0) == 0,
               "diagonal source: nabla_mu T^mu_x0 = d0 p0 + 3 H cot z (p0 - p_t)",
               EMT, "divergence_x0_component")
    reproduces(all(divT[n] == 0 for n in (1, 2, 3, 5, 6, 7)),
               "nabla_mu T^mu_nu = 0 identically for the six other nu",
               EMT, "divergence_other_components_zero")
    '''),
    md(r"""
    ## 13. Einstein gravity: a flat vacuum, no exponential vacuum, the null combinations

    In Einstein gravity ($\alpha_1 = 1$, $\alpha_2 = \alpha_3 = 0$) the next cell
    checks four facts. (1) The **flat member** $a_4 = 0$, $b_4 = H^2(x_4 - c)^2$
    ($u = 2/(x_4 - c)$, $v = -2/(x_4 - c)^2$, $k = 1/(H^2(x_4 - c)^2)$) makes every
    curvature component vanish, so it solves the vacuum equations with $\Lambda = 0$:
    8-dimensional flat space in Milne form. (2) On an **exponential history**
    ($a_4' = AH$, $u = \beta AH$, $a_4'' = v = 0$) the vacuum equations give
    $e_{44} - e_{11} = A^2H^2(\beta - 2)(\beta - 4) = 0$ and, from
    $e_{44} = e_{00}$, $k = A^2(\beta - 4)/2$; the first allows $\beta = 2$, $\beta = 4$
    or $A = 0$, and then $k = -A^2$ or $k = 0$: never $k > 0$. So no exponential
    history is a vacuum, for any $\Lambda$. (3) The **null combinations**
    $\kappa(\rho + p_0) = e_{00} - e_{44}$ and $\kappa(\rho + p_3) = e_{11} - e_{44}$
    (the constraint subtracted from the other two equations; $\Lambda$ cancels). (4) On
    the record history $\kappa(\rho + p_0) = -3k - 4 < 0$ (units $H = 1$): its source
    violates the null energy condition along $x_4 + x_0$ (for $\kappa > 0$).
    """),
    code(r'''
    c, x4 = sp.symbols("c x4", real=True)
    FLAT = {ad1: 0, ad2: 0, uu: 2 / (x4 - c), vv: -2 / (x4 - c) ** 2,
            kk: 1 / (H ** 2 * (x4 - c) ** 2)}
    flat_riemann = all(sp.simplify(value.subs(FLAT)) == 0 for value in R.values())
    reproduces(flat_riemann, "flat member: every R^ab_mn vanishes",
               WL, "flat_member")
    reproduces(all(sp.simplify(G[i][i].subs(FLAT)) == 0 for i in range(N)),
               "Einstein: the flat member is a vacuum with Lambda = 0",
               PY, "einstein_flat_vacuum")
    difference_x1 = sp.factor(sp.expand((e44 - e11).subs(EINSTEIN).subs(EXPONENTIAL)))
    k_vacuum = sp.solve(sp.expand((e44 - e00).subs(EINSTEIN).subs(EXPONENTIAL)), kk)
    say(f"exponential vacuum: e44 - e11 = {difference_x1}, e44 = e00 needs k = {k_vacuum}")
    roots = sp.solve(difference_x1 / (A ** 2 * H ** 2), beta)  # beta = 2 or 4
    k_values = [sp.factor(k_vacuum[0].subs(beta, root)) for root in roots]
    reproduces(sorted(roots) == [2, 4] and k_values == [-A ** 2, 0]
               and sp.factor(k_vacuum[0].subs(A, 0)) == 0,
               "Einstein: no exponential history is a vacuum (k would be -A^2 or 0)",
               PY, "einstein_no_exponential_vacuum")
    null_x0 = sp.factor((e00 - e44).subs(EINSTEIN))  # kappa (rho + p0)
    null_x1 = sp.expand((e11 - e44).subs(EINSTEIN))  # kappa (rho + p3)
    report("Einstein: kappa (rho + p0)", null_x0)
    report("Einstein: kappa (rho + p3)", null_x1)
    reproduces(sp.expand(null_x0 + sp.Rational(3, 2) * (2 * H ** 2 * kk + 4 * ad1 ** 2
                                                         - ad1 * uu + vv)) == 0
               and sp.expand(null_x1 - (2 * ad2 - 8 * ad1 ** 2 + 6 * ad1 * uu - uu ** 2
                                        - 2 * vv)) == 0,
               "Einstein: the two null combinations as in the record",
               PY, "einstein_null_combinations")
    null_history = sp.expand(null_x0.subs(HISTORY).subs(H, 1))
    report("record history: kappa (rho + p0)", null_history)
    check(null_history == -3 * kk - 4, "record history: kappa (rho + p0) = -3 k - 4 < 0")
    einstein_record = equations_json["einstein"]
    mine_einstein = {"constraint_x4": (e44 + Lam).subs(EINSTEIN) + kappa * rho,
                     "space_x1": (e11 + Lam).subs(EINSTEIN) - kappa * p3,
                     "hidden_x0": (e00 + Lam).subs(EINSTEIN) - kappa * p0}
    same = all(sp.expand(parse_equation(einstein_record[key]["input"]) - value) == 0
               for key, value in mine_einstein.items())
    reproduces(same, "the Einstein equations equal the record", PY, "json_einstein")
    '''),
    md(r"""
    The next cell draws why no exponential history is an Einstein vacuum, in the plane
    of $\beta$ (horizontal) and $k/A^2$ (vertical). The 3-space equation minus the time
    equation allows only the two vertical lines $\beta = 2$ and $\beta = 4$; the hidden
    equation minus the time equation allows only the slanted line
    $k/A^2 = (\beta - 4)/2$. They meet at $(2, -1)$ and $(4, 0)$, both in the shaded
    region $k \le 0$, where no history lies ($k = e^{2a_4}/b_4 > 0$). The record history
    has $\beta = 4/3$ (dotted line); along it $k$ grows from 1.
    """),
    code(r'''
    beta_axis = np.linspace(0.0, 6.0, 301)
    fig, ax = plt.subplots()
    ax.axhspan(-3.0, 0.0, color="grey", alpha=0.25, label="$k \\leq 0$: no history")
    ax.plot(beta_axis, (beta_axis - 4.0) / 2.0, color="tab:blue",
            label="hidden equation: $k/A^2 = (\\beta - 4)/2$")
    for position in (2.0, 4.0):
        ax.axvline(position, color="tab:red", linestyle="--")
    ax.plot([], [], color="tab:red", linestyle="--",
            label="3-space equation: $\\beta = 2$ or $\\beta = 4$")
    ax.plot([2.0, 4.0], [-1.0, 0.0], "o", color="black", label="where both hold")
    ax.axvline(4.0 / 3.0, color="black", linestyle=":", label="record history "
               "$\\beta = 4/3$")
    ax.set_xlim(0.0, 6.0)
    ax.set_ylim(-3.0, 3.0)
    ax.set_xlabel("$\\beta = (b_4'/b_4)/a_4'$")
    ax.set_ylabel("$k/A^2$")
    ax.set_title("Einstein gravity: the vacuum conditions on exponential histories")
    ax.legend(fontsize=7.5, loc="upper left")
    save_figure(fig, "exponential_vacuum",
                "Why no exponential history $a_4 = AHx_4 + a_0$, $b_4 = b_4(0)"
                "e^{\\beta AHx_4}$ solves the vacuum equations of Einstein gravity: in "
                "the plane of $\\beta$ (horizontal) and $k/A^2$ (vertical, "
                "$k = e^{2a_4}/b_4$), the 3-space equation minus the time equation holds "
                "only on the dashed lines $\\beta = 2$ and $\\beta = 4$, the hidden "
                "equation minus the time equation only on the solid line "
                "$k/A^2 = (\\beta - 4)/2$. The two meet at the black points $(2, -1)$ "
                "and $(4, 0)$, both in the grey region $k \\leq 0$, where no history "
                "lies. The dotted line is the record history $\\beta = 4/3$.")
    '''),
    md(r"""
    ## 14. Exponential histories and the source of the record history

    On an exponential history the left-hand sides depend on the time only through
    $k = k_0e^{(2 - \beta)AHx_4}$. The next cell checks that the required $\kappa\rho$,
    $\kappa p_3$ and $\kappa p_0 = \kappa p_t$ are polynomials of degree at most 2 in
    $k$, so the source is constant only for $\beta = 2$ or $A = 0$ (where $k$ is
    constant); that they equal the record; and that, written as functions of $k$, they
    contain $A$ only through $A^2$: the sign of $A$ (whether 3-space inflates or
    deflates) is a choice, not selected by the equations.
    """),
    code(r'''
    required_mine = {"rho": sp.expand(-(e44 + Lam).subs(EXPONENTIAL) / kappa),
                     "p3": sp.expand((e11 + Lam).subs(EXPONENTIAL) / kappa),
                     "p0": sp.expand((e00 + Lam).subs(EXPONENTIAL) / kappa)}
    degrees = [sp.Poly(kappa * value, kk).degree() for value in required_mine.values()]
    say(f"degrees in k of kappa rho, kappa p3, kappa p0: {degrees}")
    reproduces(max(degrees) <= 2 and required_mine["p0"].has(kk),
               "exponential history: rho, p3, p0 = p_t polynomials of degree <= 2 in k",
               PY, "exponential_history_required_source")
    names_all = dict(names_exp, alpha1=alpha1, alpha2=alpha2, alpha3=alpha3, Lam=Lam,
                     kappa=kappa)
    same = all(sp.expand(sp.sympify(required[key]["input"].replace("^", "**"),
                                    locals=names_all) - required_mine[name]) == 0
               for key, name in (("rho", "rho"), ("p3", "p3"), ("p0", "p0"),
                                 ("pt", "p0")))
    reproduces(same, "the required source equals the record (exponentialHistory)",
               PY, "json_exponential_history")
    check(all(sp.expand(value.subs(A, -A) - value) == 0
              for value in required_mine.values()),
          "as functions of k the required source contains A only through A^2")
    '''),
    md(r"""
    **The record history.** With the author's weights ($\alpha_k = w_k/H^{2k}$,
    $w = (1, \tfrac1{32}, \tfrac1{1152})$) on the record history ($A = 1$,
    $\beta = \tfrac43$, $H = 1$, $k = e^{(2/3)x_4}$) the next cell computes the source
    $\kappa T - \Lambda\delta$ that the history needs, prints it, and compares it with
    the record `a4-equations.json` and with the record of the corrected metric, which
    writes it with `exp(2*H*x4/3)` for $k$. Then it checks, on the history, the
    energy exchange $\partial_4\rho + 3a_4'(\rho + p_3) + 4h_4(\rho + p_0) = 0$ (the
    conservation law of section 12 for this source): the required source is conserved.
    """),
    code(r'''
    HISTORY_EXP = {A: 1, beta: sp.Rational(4, 3), H: 1}  # A = 1, beta = 4/3, H = 1
    AUTHOR_H = {alpha1: 1, alpha2: sp.Rational(1, 32) / H ** 2,
                alpha3: sp.Rational(1, 1152) / H ** 4}  # alpha_k = w_k/H^(2k)
    needed = {name: sp.expand(value.subs(AUTHOR_H).subs(EXPONENTIAL).subs(HISTORY_EXP))
              for name, value in (("minus_rho", e44), ("p3", e11), ("p0", e00))}
    for name, value in needed.items():
        say(f"author's weights, record history: kappa T - Lambda ({name}) = {value}")
    stored = equations_json["exponentialHistory"]["authorWeights"]
    stored = stored["historySource_kappaT_minus_Lam"]
    same = all(sp.expand(parse(stored[key]["input"]) - needed[name]) == 0
               for key, name in (("minus_rho", "minus_rho"), ("p3", "p3"),
                                 ("p0", "p0"), ("pt", "p0")))
    reproduces(same, "the author's weights: the source of the record history",
               PY, "author_weights_history_source")
    x4s = sp.symbols("x4", real=True)
    metric_history = read_json(METRIC_RESULTS)["history_source"]
    exp_names = {"H": sp.Integer(1), "x4": x4s, "exp": sp.exp}
    as_k = sp.Rational(3, 2) * sp.log(kp)  # x4 = (3/2) ln k, so e^(2 x4/3) = k
    einstein_needed = {name: sp.expand(value.subs(EINSTEIN).subs(EXPONENTIAL)
                                       .subs(HISTORY_EXP))
                       for name, value in (("-rho", e44), ("p3", e11), ("p0", e00),
                                           ("p_t", e00))}
    same = True
    for block, values in (("author_weights_A1_beta43",
                           {"-rho": needed["minus_rho"], "p3": needed["p3"],
                            "p0": needed["p0"], "p_t": needed["p0"]}),
                          ("einstein_A1_beta43", einstein_needed)):
        for key, value in values.items():
            text = sp.sympify(metric_history[block][key], locals=exp_names)
            in_k = sp.expand(sp.expand(text.subs(x4s, as_k)).subs(kp, kk))
            same = same and sp.expand(in_k - value) == 0
    conserved = sp.expand((d4_record(-e44) + 3 * ad1 * (-e44 + e11)
                           + 4 * h4 * (-e44 + e00)).subs(AUTHOR_H).subs(HISTORY)
                          .subs(H, 1))
    reproduces(same and conserved == 0,
               "the history source of the corrected-metric record, conserved",
               WARPED, "history_source_conserved")
    '''),
    md(r"""
    ## 15. The last check

    The last cell checks that the five figure files exist in the folder
    Revision/textbook/figures and prints the number of checks that passed.
    """),
    code(r'''
    figure_names = ["12a_1_pair_curvatures.png", "12a_2_einstein_components.png",
                    "12a_3_lovelock_heat_maps.png", "12a_4_jacobian_determinant.png",
                    "12a_5_exponential_vacuum.png"]
    check(all(output_file(f"{FIGURE_FOLDER}/{name}").is_file() for name in figure_names),
          "all five figure files exist")
    all_checks_passed()
    '''),
    md(r"""
    ## 16. What this notebook showed

    - From the corrected metric alone, at every real $z$, sympy finds 31 nonzero
      Christoffel symbols (21 distinct) and 112 nonzero curvature components
      $R^{ab}{}_{mn}$ (28 with $a < b$, $m < n$), every one of them sectional (no
      mixed component) and free of $x_0$ (PROVED, as in the Revision record).
    - The Einstein tensor is diagonal with three distinct components (time, 3-space,
      and the block of the hidden direction and the extra times); the three Lovelock
      tensors built with the generalized Kronecker delta agree, in all 64 components,
      with the Rust program and the Wolfram record; $E_{(2)}$ equals the classical
      Gauss-Bonnet tensor; each $E_{(k)}$ has zero divergence (PROVED).
    - The field equations reduce to a constraint ($x_4$), two equations of second
      order (3-space and block) that are linear in $(a_4'', v)$ with Einstein
      $\det J = -3$, and conditions on the source: no mixed component, $p_0 = p_t$,
      no dependence on $x_0$ (PROVED).
    - The constraint propagates by the Bianchi identity, and the source must obey
      $\partial_4\rho + 3a_4'(\rho + p_3) + 4h_4(\rho + p_0) = 0$ and
      $\partial_0 p_0 + 3H\cot z(p_0 - p_t) = 0$ (PROVED).
    - Einstein gravity: the flat member $a_4 = 0$, $b_4 = H^2(x_4 - c)^2$ is a vacuum,
      no exponential history is one, and the source of the record history violates
      the null energy condition along $x_4 + x_0$ (PROVED).
    - On exponential histories the required source is a polynomial of degree at most
      2 in $k$ that contains $A$ only through $A^2$; the record history needs, with
      the author's weights, the diagonal conserved source of the record (PROVED).
    """),
]

if __name__ == "__main__":
    raise SystemExit(run_builder(__file__))
