#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
"""Builder of Notebook 08c, "The spin-connection term depends on the frame"
(textbook "Universes in Pairs", chapter 08).

The notebook Revision/textbook/notebooks/08c_frame_dependence.ipynb is BUILT from this
file by Revision/textbook/tools/nbkit.py (never edit the .ipynb by hand):

    python Revision/textbook/tools/nbkit.py build \
        Revision/textbook/notebooks/src/08c_frame_dependence.py --date YYYY-MM-DD
    python Revision/textbook/tools/nbkit.py check \
        Revision/textbook/notebooks/src/08c_frame_dependence.py

It recomputes exactly (sympy), from the corrected metric of 2026-10-16 (version 2) and the
Revision gammas, the canonical spin connection of the diagonal frame and of the frame
boosted in the (x4, x0) plane with a rapidity b(x4), and reproduces the checks of
Revision/theory/reports/python-scope.json (boosted_frame_*,
gammaOmega_sees_the_hidden_block, connection_free_lagrangian_same_equations,
spin_connection_in_the_energy_momentum_tensor), of
Revision/theory/reports/python-field-theory.json (among them
nontriviality_Omega_zero_iff_flat and curvature_and_flat_member) and of
wolfram-field-theory.json. Every such check also requires the record to hold the check
with the verdict pass and the values computed here.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools"))
from nbkit import code, md, run_builder  # noqa: E402

FIGURES = [
    "08c_1_cancel_and_survive",
    "08c_2_pieces_along_history",
    "08c_3_boost_size",
    "08c_4_heat_maps",
    "08c_5_curvature_maps",
]

FACTS = {
    "id": "08c",
    "name": "08c_frame_dependence",
    "title": "The spin-connection term depends on the frame",
    "purpose": (
        "From the corrected metric and the author's gamma matrices it computes exactly "
        "(sympy) the Christoffel symbols, the canonical spin connection of the diagonal "
        "frame and of a frame boosted in the (x4, x0) plane with a rapidity b(x4), and "
        "the term gamma^mu Omega_mu of the field equation, for the metric with the two "
        "functions a4(x4) and b4(x4); it shows that the connection vanishes only in the "
        "formal limit a4' = b4' = 0, H = 0, which pieces cancel and which survive (cg "
        "gamma^(x0) + vg gamma^(x4) in the diagonal frame, with cg = (3/2) H e^a4 "
        "b4^(-1/2) and vg = b4'/b4 - a4'/2), that the term sees the deflating hidden "
        "block, that the metric is flat for a4 = 0, b4 = H^2 x4^2 and curved on the "
        "history, that a boost with rapidity rate b' = 2 cg removes the cg part while "
        "no boost removes the vg part, that the spin connection itself vanishes in no "
        "frame where the metric is curved (its curvature is the Riemann tensor), and "
        "that it enters the energy-momentum tensor; it draws five teaching plots."
    ),
    "records": [
        ["Revision/algebra/gammas.json",
         "the author's 16 x 16 gamma matrices and C (read)"],
        ["Revision/kohn_sham/results/parameters.json",
         "the canonical history a4 = A H x4, b4 = b4(0) e^(beta A H x4) with A = H = 1, "
         "beta = 4/3, b4(0) = 1, used for the checks on the history and the plots "
         "(read)"],
        ["Revision/theory/reports/python-field-theory.json",
         "checks metric_from_vielbein_equals_SPEC, sqrt_det_g, "
         "christoffel_symmetric_metric_compatible, vielbein_postulate, "
         "spin_connection_antisymmetric, per_direction_terms, "
         "gamma_mu_Omega_mu_equals_hidden_block_terms, gravity_term_square, "
         "divergence_of_sqrtg_gamma, curvature_and_flat_member, "
         "spinor_curvature_equals_riemann and nontriviality_Omega_zero_iff_flat "
         "(reproduced)"],
        ["Revision/theory/reports/wolfram-field-theory.json",
         "checks christoffel_count, omega_components, "
         "Omega_vanishes_iff_a4prime_b4prime_and_H_vanish, ricci_mixed_components and "
         "flat_member_and_curvature (reproduced)"],
        ["Revision/theory/reports/python-scope.json",
         "checks boosted_frame_reproduces_metric, boosted_frame_canonical_connection, "
         "boosted_frame_gammaOmega_formula, boosted_frame_removes_only_the_H_term, "
         "boosted_frame_curvature_nonzero, gammaOmega_sees_the_hidden_block, "
         "connection_free_lagrangian_same_equations and "
         "spin_connection_in_the_energy_momentum_tensor (reproduced)"],
    ],
    "packages": ["numpy", "sympy", "matplotlib"],
    "needs_rust": [],
    "expected_seconds": 240,
    "timeout_seconds": 1200,
    "files_written": ["Revision/textbook/figures/08c.captions.json"]
    + [f"Revision/textbook/figures/{name}.png" for name in FIGURES],
    "final_lines": [
        "PASS the figure file 08c_5_curvature_maps.png exists",
        "ALL 37 CHECKS PASSED (notebook 08c)",
    ],
    "troubleshooting": [
        ["A cell of sections 7, 10, 11 or 12 runs for more than a minute",
         "these cells simplify hundreds of exact expressions with sympy; on a slow "
         "computer each can take a few minutes. Wait until the star in the brackets "
         "to the left of the cell turns into a number."],
    ],
}

CELLS = [
    md(r"""
    ## 1. What this notebook computes

    The field equation of dirac16complex (and of dirac16complex00) contains the term
    $\gamma^\mu\Omega_\mu\Psi$, where $\Omega_\mu$ is the canonical spin connection. In
    the diagonal frame of the author's corrected metric this term is $G\Psi$ with $G =
    c_g\gamma^{(0)} + v_g\gamma^{(4)}$, $c_g = \frac32He^{a_4}b_4^{-1/2}$ and $v_g =
    b_4'/b_4 - a_4'/2$; on the history of the Revision record $c_g = \frac32He^{Hx_4/3}$
    and $v_g = \frac56H$. This notebook computes everything from the definitions,
    exactly, with sympy, for the metric with the two functions $a_4(x_4)$ and
    $b_4(x_4)$, and shows what that value means and what it does not mean. It

    - builds the corrected metric from the diagonal vielbein, its Christoffel symbols
      (21 independent nonzero ones) and the canonical spin connection (10 independent
      nonzero components), and checks the vielbein postulate for all 512 components;
    - shows that the connection vanishes only in the formal limit $a_4' = 0$,
      $b_4' = 0$, $H = 0$ (the core of non-triviality) and that the term $G\Psi$ is
      not zero for any field $\Psi \neq 0$ wherever $c_g^2 \neq v_g^2$;
    - shows, direction by direction, which pieces of $\gamma^\mu\Omega_\mu$ cancel
      (the $a_4'$ pieces of 3-space and of the extra times) and which survive (the
      rate $h_4 = b_4'/(2b_4) - a_4'$ shared by the hidden direction and the three
      extra times, and the pieces $\frac12He^{a_4}b_4^{-1/2}$ of the extra times);
    - shows that the term sees the deflation of the hidden block, that the metric is
      flat for the special history $a_4 = 0$, $b_4 = H^2x_4^2$ (there the term is a pure
      frame effect) and curved on the history of the record;
    - repeats everything in a second, equally valid frame, boosted in the
      $(x_4, x_0)$ plane with a rapidity $b(x_4)$, finds $\gamma'^\mu\Omega'_\mu =
      (c_g - \frac{b'}{2})(\cosh b\,\gamma^{(0)} - \sinh b\,\gamma^{(4)}) +
      v_g(\cosh b\,\gamma^{(4)} - \sinh b\,\gamma^{(0)})$: a frame in which the part
      $c_g\gamma^{(0)}$ is gone, while no boost removes the part $v_g$;
    - shows that the spin connection itself is not zero in that frame (nor in any
      other where the metric is curved): its curvature is the Riemann tensor;
    - shows that the spin connection enters the energy-momentum tensor.

    Every exact statement reproduces a check of a Revision record. Five teaching plots.
    """),
    md(r"""
    ## 3. The words used in this notebook

    - **Coordinates** (the author's names, the hidden direction first): $x_0$ the
      hidden direction, $z = 6Hx_0$ taking every real value; $x_1, x_2, x_3$ ordinary
      space (inflating, scale factor $e^{a_4}$); $x_4$ the time; $x_5, x_6, x_7$ the
      three extra times (time-like, DEFLATING: their scale factor is $e^{-a_4}b_4^{1/2}
      (\sin^2 z)^{1/12}$). $a_4(x_4)$ and $b_4(x_4) > 0$ are any functions of the time.
    - **Metric** $g_{\mu\nu}$: the table of numbers that turns coordinate steps into
      lengths, $ds^2 = \sum g_{\mu\nu}dx_\mu dx_\nu$. The corrected metric is diagonal:
      $g = \mathrm{diag}(e^{-2a_4}b_4\cot^2 z, e^{2a_4}\ (3\times), -1,
      -e^{-2a_4}b_4(\sin^2 z)^{1/6}\ (3\times))$. It degenerates where $\sin z\cos z =
      0$: at the *fold* $\cos z = 0$, where the two halves of a cell $0 < z < \pi$ meet,
      and at the *tips* $\sin z = 0$.
    - **Warp factor** $W = (\sin^2 z)^{1/12} > 0$: in the code a sympy function class
      `W` whose derivative rule is $dW/dx_0 = H\cot z\,W$ (valid for every real $z$ with
      $\sin z \neq 0$).
    - **Frame (vielbein)** $e^a{}_\mu$: eight vectors, one per direction $a$, that are
      orthonormal for the metric: $\sum_{a} \eta_{aa}e^a{}_\mu e^a{}_\nu = g_{\mu\nu}$
      with $\eta = \mathrm{diag}(+,+,+,+,-,-,-,-)$. The *diagonal frame* has
      $e^a{}_\mu = f_a\delta^a_\mu$ with $f_0 = e^{-a_4}b_4^{1/2}\cot z$ (it keeps the
      sign of $\cot z$), $f_{1,2,3} = e^{a_4}$, $f_4 = 1$, $f_{5,6,7} =
      e^{-a_4}b_4^{1/2}W$. Its inverse is $E_a{}^\mu$ (written `E[mu, a]` in the code).
    - **Christoffel symbols** $\Gamma^\lambda{}_{\mu\nu}$: the numbers that say how the
      coordinate directions turn from point to point; for a diagonal metric
      $\Gamma^\lambda{}_{\mu\nu} = \frac{1}{2g_{\lambda\lambda}}(\partial_\mu
      g_{\lambda\nu} + \partial_\nu g_{\lambda\mu} - \partial_\lambda g_{\mu\nu})$.
    - **Canonical spin connection** $\omega_\mu{}^a{}_b = e^a{}_\nu(\partial_\mu
      E_b{}^\nu + \Gamma^\nu{}_{\mu\lambda}E_b{}^\lambda)$: how the frame vectors turn;
      it obeys the *vielbein postulate* $\partial_\mu e^a{}_\nu -
      \Gamma^\lambda{}_{\mu\nu}e^a{}_\lambda + \omega_\mu{}^a{}_b e^b{}_\nu = 0$, and
      $\omega_{\mu ab} = \eta_{aa}\omega_\mu{}^a{}_b$ is antisymmetric in $a, b$.
    - **Spinor connection** $\Omega_\mu = \frac12\sum_{a,b}\omega_{\mu ab}S^{ab}$ with
      $S^{ab} = \frac14[\gamma^{(a)}, \gamma^{(b)}]$; $D_\mu\Psi = \partial_\mu\Psi +
      \Omega_\mu\Psi$ and $\gamma^\mu = \sum_a E_a{}^\mu\gamma^{(a)}$.
    - **Rates**: $a_4'$ (3-space), $h_4 = b_4'/(2b_4) - a_4'$ (the hidden direction and
      the extra times, whose common factor $e^{-a_4}b_4^{1/2}$ changes at this rate);
      the code writes `A1` for $a_4'$ and `B1` for $b_4'/b_4$, as the Revision record
      does.
    - **Boost**: a change of frame that mixes a time-like and a space-like frame vector
      with $\cosh b$ and $\sinh b$ ($b$ is the *rapidity*, here any function $b(x_4)$
      of the time); because $\cosh^2 b - \sinh^2 b = 1$ the new vectors are again
      orthonormal, so the new frame describes the SAME metric.
    - **Riemann tensor** $R^\rho{}_{\sigma\mu\nu}$ (curvature) and its traces: the Ricci
      tensor $R_{\sigma\nu} = \sum_\rho R^\rho{}_{\sigma\rho\nu}$, its mixed form
      $R^\mu{}_\nu = g^{\mu\mu}R_{\mu\nu}$ and the Ricci scalar $R = \sum_a R^a{}_a$. A
      space is flat exactly when the Riemann tensor vanishes.
    - **Spinor curvature** $F_{\mu\nu} = \partial_\mu\Omega_\nu - \partial_\nu\Omega_\mu
      + [\Omega_\mu, \Omega_\nu]$, where $[A, B] = AB - BA$ (the *commutator*); the
      record proves $F_{\mu\nu} = \frac14\sum R_{\rho\sigma\mu\nu}\gamma^\rho
      \gamma^\sigma$.
    - **Anticommutator** $\{A, B\} = AB + BA$; **trace** of a matrix: the sum of its
      diagonal.
    """),
    md(r"""
    ## 4. The physical and mathematical situation

    Coupling a spinor field to gravity needs a frame, because the gamma matrices
    $\gamma^{(a)}$ belong to the orthonormal frame directions, not to the coordinates.
    The frame is not unique: at every point one may turn (rotate or boost) the eight
    frame vectors among themselves, and the metric stays the same. The spin connection
    changes under such a turn, and so may $\gamma^\mu\Omega_\mu$. A statement is a
    property of the field equation only if it holds in every frame (together with the
    matching change of the field, $\Psi' = S\Psi$ with a constant-or-varying $16
    \times 16$ matrix $S$).

    The plan: compute $\gamma^\mu\Omega_\mu$ in the diagonal frame (result $G = c_g
    \gamma^{(0)} + v_g\gamma^{(4)}$, sections 7 to 10), then in the boosted frame
    $e'^{(4)} = \cosh b\,e^{(4)} + \sinh b\,e^{(0)}$, $e'^{(0)} = \sinh b\,e^{(4)} +
    \cosh b\,e^{(0)}$, other $e'^{(a)} = e^{(a)}$, with a rapidity $b(x_4)$ (section 11),
    and finally the curvature (section 12), which no frame can remove.

    Every symbol is exact: $H > 0$ is a letter, and $a_4(x_4)$, $b_4(x_4) > 0$ and
    $b(x_4)$ are unspecified functions; so every check holds for EVERY history. Only the
    checks on the history and the plots put numbers in: $H = 1$, $z = \pi/4$, and the
    canonical history of the Kohn-Sham record, $a_4 = AHx_4$ and $b_4 =
    b_4(0)\,e^{\beta_4AHx_4}$ with $A = 1$, $\beta_4 = 4/3$ and $b_4(0) = 1$ (the
    exponent is called $\beta_4$ here, because $\beta$ is the rate of a boost). It is
    a prescribed background, not a solution of the field equations of the metric.
    """),
    md(r"""
    ## 5. The metric from the diagonal frame

    The next cell first defines two helpers for the checks that reproduce a Revision
    record. `record_says(report, name, ...)` opens the report (a JSON file with a list
    of checks, each with a name, a verdict and a detail text) and is true when the
    check `name` is there with the verdict pass and its detail text contains every
    further piece of text given (for example a formula that this notebook computes).
    `check_record(condition, title, report, names, ...)` is the helper `check` for such
    a result (`names` is one check name or a list of names): it passes only if the
    notebook's own computation (`condition`) is right AND the record says the same.
    Then the cell reads the gamma matrices, defines the symbols and the warp factor
    class `W` (its derivative rule is checked against the explicit $(\sin^2
    z)^{1/12}$, whose derivative sympy computes itself), builds the scale factors $f_a$
    and the metric $g_{aa} = \eta_{aa}f_a^2$, and checks that this is the corrected
    metric entry by entry (the record prints the same eight entries, with $W$ written
    as $|\sin z|^{1/6}$) and that $f_0f_1\cdots f_7 = e^{-a_4}b_4^2\cot z\,W^3$, whose
    size is $\sqrt{|g|} = e^{-a_4}b_4^2|\cot z|(\sin^2 z)^{1/4}$, with $\partial_4
    \sqrt{|g|} = (2b_4'/b_4 - a_4')\sqrt{|g|}$. The helper `is_zero` asks sympy to
    simplify an expression twice (the second time with its trigonometric simplifier
    `fu`) and says whether it is exactly zero.
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


    def check_record(condition, title, report_file, check_names, *pieces):
        """check() for a result that reproduces Revision checks (one name or a list of
        names): it passes only if condition is true AND the report records every one
        of them as passed, with every piece of text in the detail of the first one."""
        names = [check_names] if isinstance(check_names, str) else list(check_names)
        on_record = record_says(report_file, names[0], *pieces) and all(
            record_says(report_file, name) for name in names[1:])
        word = "check" if len(names) == 1 else "checks"
        check(condition and on_record, title,
              record=f"{report_file}, {word} " + " and ".join(names))


    gammas_record = json.loads(
        repository_file("Revision/algebra/gammas.json").read_text(encoding="utf-8"))
    G = [sp.Matrix(rows) for rows in gammas_record["gamma"]]  # gamma^(x0) ... (x7)
    ETA = gammas_record["eta"]  # [1, 1, 1, 1, -1, -1, -1, -1]
    C = sp.Matrix(gammas_record["C"])  # C = gamma^(x0) gamma^(x1) gamma^(x2) gamma^(x3)
    THEORY = "Revision/theory/reports/python-field-theory.json"  # the sympy record
    WOLFRAM = "Revision/theory/reports/wolfram-field-theory.json"  # the Wolfram record

    x = sp.symbols("x0:8", real=True)  # the coordinates; x[k] is xk
    x0, x4 = x[0], x[4]  # the hidden direction and the time
    H = sp.Symbol("H", positive=True)
    a4 = sp.Function("a4")(x4)  # the first metric function: ANY function of x4
    b4 = sp.Function("b4", positive=True)(x4)  # the second one: ANY positive function
    a4p, b4p = sp.diff(a4, x4), sp.diff(b4, x4)  # a4' and b4'
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


    explicit_W = sp.Abs(sp.sin(z)) ** sp.Rational(1, 6)  # (sin^2 z)^(1/12) = |sin z|^(1/6)
    check(is_zero(sp.diff(explicit_W, x0) - H * sp.cot(z) * explicit_W),
          "the derivative of (sin^2 z)^(1/12) is H cot z (sin^2 z)^(1/12): the rule of W")
    s_b = sp.exp(-a4) * sp.sqrt(b4)  # the scale of the hidden block e^(-a4) b4^(1/2)
    f = [s_b * sp.cot(z)] + [sp.exp(a4)] * 3 + [sp.Integer(1)] \
        + [s_b * W(x0)] * 3  # the scale factors f_0, ..., f_7
    g = [ETA[a] * f[a] ** 2 for a in range(8)]  # the diagonal entries g_aa
    sixth = (sp.sin(z) ** 2) ** sp.Rational(1, 6)  # (sin^2 z)^(1/6), sympy: |sin z|^(1/3)
    authors_metric = [b4 * sp.exp(-2 * a4) * sp.cot(z) ** 2] + [sp.exp(2 * a4)] * 3 \
        + [-1] + [-b4 * sp.exp(-2 * a4) * sixth] * 3  # the corrected metric, typed in
    # The record prints each entry as sympy writes it, e.g. "g_x4x4 = -1".
    metric_texts = [f"g_x{a}x{a} = {sp.sstr(authors_metric[a])}" for a in range(8)]
    say(metric_texts[0])
    say(metric_texts[5])
    check_record(all(is_zero(g[a].subs(W(x0), explicit_W) - authors_metric[a])
                     for a in range(8)),
                 "eta_aa f_a^2 is the corrected metric (all 8 diagonal entries)",
                 THEORY, "metric_from_vielbein_equals_SPEC", *metric_texts)
    volume = sp.prod(f)  # f_0 f_1 ... f_7: it has the sign of cot z
    check_record(is_zero(volume - sp.exp(-a4) * b4**2 * sp.cot(z) * W(x0) ** 3)
                 and is_zero(volume**2 - sp.prod(g))
                 and is_zero(sp.diff(volume, x4) - (2 * b4p / b4 - a4p) * volume),
                 "f0 ... f7 = e^(-a4) b4^2 cot z W^3, so sqrt|g| = e^(-a4) b4^2 |cot z| "
                 "(sin^2 z)^(1/4), d4 sqrt|g| = (2 b4'/b4 - a4') sqrt|g|",
                 THEORY, "sqrt_det_g", "e^-a4 b4^2 |cot z| (sin^2 z)^(1/4)",
                 "d_x4 sqrt|g| = (2 b4'/b4 - a4') sqrt|g|")
    '''),
    md(r"""
    ## 6. The Christoffel symbols

    The next cell computes all $8 \times 8 \times 8$ symbols
    $\Gamma^\lambda{}_{\mu\nu}$ (stored as `Gam[lam][mu][nu]`) with the formula for a
    diagonal metric, counts the independent nonzero ones (those with $\mu \le \nu$,
    because $\Gamma^\lambda{}_{\mu\nu} = \Gamma^\lambda{}_{\nu\mu}$), and prints six of
    them. sympy writes $a_4'$ as `Derivative(a4(x4), x4)`.
    """),
    code(r'''
    Gam = [[[sp.Integer(0)] * 8 for _ in range(8)] for _ in range(8)]
    for lam in range(8):
        for mu in range(8):
            for nu in range(8):
                value = 0  # the bracket of the formula; g is diagonal, so only these
                if lam == nu:  # three cases contribute
                    value += sp.diff(g[lam], x[mu])
                if lam == mu:
                    value += sp.diff(g[lam], x[nu])
                if mu == nu:
                    value -= sp.diff(g[mu], x[lam])
                if value != 0:
                    Gam[lam][mu][nu] = sp.simplify(value / (2 * g[lam]))
    independent = sum(1 for lam in range(8) for mu in range(8) for nu in range(mu, 8)
                      if Gam[lam][mu][nu] != 0)
    report("independent nonzero Christoffel symbols", independent)
    for lam, mu, nu in ((0, 0, 0), (0, 0, 4), (0, 5, 5), (5, 0, 5), (1, 1, 4), (5, 4, 5)):
        say(f"Gamma^x{lam}_x{mu} x{nu} = {Gam[lam][mu][nu]}")
    check_record(independent == 21, "21 independent nonzero Christoffel symbols",
                 THEORY, "christoffel_symmetric_metric_compatible",
                 f"{independent} independent nonzero symbols")
    check_record(independent == 21, "the same count in the independent Wolfram verifier",
                 WOLFRAM, "christoffel_count",
                 f"the Levi-Civita connection has {independent} independent nonzero "
                 "symbols")
    '''),
    md(r"""
    ## 7. The canonical spin connection of the diagonal frame

    The function `frame(b)` below builds the frame boosted by the rapidity $b$ (for
    $b = 0$ the diagonal frame), its inverse, the mixed connection
    $\omega_\mu{}^a{}_c$ (stored as `omega[mu, a, c]`), the spinor connections
    $\Omega_\mu$ and the matrices $\gamma^\mu$. `postulate_failures` counts the
    components of the vielbein postulate that are NOT zero. The next cell applies them
    to the diagonal frame, checks the postulate (512 components) and the antisymmetry,
    and prints the 10 independent nonzero components $\omega_{\mu ab}$ ($a < b$).
    """),
    code(r'''
    S_AB = [[(G[a] * G[c] - G[c] * G[a]) / 4 for c in range(8)] for a in range(8)]


    def boost(b):
        """The boost by the rapidity b in the frame plane (x4, x0), and its inverse."""
        L, L_inverse = sp.eye(8), sp.eye(8)
        L[4, 4] = L[0, 0] = L_inverse[4, 4] = L_inverse[0, 0] = sp.cosh(b)
        L[4, 0] = L[0, 4] = sp.sinh(b)
        L_inverse[4, 0] = L_inverse[0, 4] = -sp.sinh(b)
        return L, L_inverse


    def frame(b):
        """Vielbein e[a, mu], inverse E[mu, a], connection omega[mu, a, c] (mixed),
        Omega_mu and gamma^mu of the diagonal frame boosted by the rapidity b."""
        L, L_inverse = boost(b)
        e = L * sp.diag(*f)
        E = sp.diag(*[1 / value for value in f]) * L_inverse
        omega = {}
        for mu in range(8):
            for a in range(8):
                for c in range(8):
                    value = 0  # e^a_nu (d_mu E_c^nu + Gamma^nu_mu,lam E_c^lam)
                    for nu in range(8):
                        if e[a, nu] == 0:
                            continue  # skip the terms that are zero anyway
                        term = sp.diff(E[nu, c], x[mu])
                        for lam in range(8):
                            if Gam[nu][mu][lam] != 0 and E[lam, c] != 0:
                                term += Gam[nu][mu][lam] * E[lam, c]
                        value += e[a, nu] * term
                    omega[mu, a, c] = sp.simplify(value)
        Omega = []
        for mu in range(8):
            matrix = sp.zeros(16, 16)
            for a in range(8):
                for c in range(a + 1, 8):  # (1/2) sum over all a, c = sum over a < c
                    matrix += ETA[a] * omega[mu, a, c] * S_AB[a][c]
            Omega.append(matrix)
        gamma_up = [sum((E[mu, a] * G[a] for a in range(8)), sp.zeros(16, 16))
                    for mu in range(8)]
        return {"e": e, "E": E, "omega": omega, "Omega": Omega, "gamma": gamma_up}


    def postulate_failures(fr):
        """How many of the 512 components of the vielbein postulate are not zero."""
        failures = 0
        for a in range(8):
            for mu in range(8):
                for nu in range(8):
                    value = sp.diff(fr["e"][a, nu], x[mu]) \
                        - sum(Gam[lam][mu][nu] * fr["e"][a, lam] for lam in range(8)) \
                        + sum(fr["omega"][mu, a, c] * fr["e"][c, nu] for c in range(8))
                    failures += 0 if is_zero(value) else 1
        return failures


    def antisymmetric(fr):
        """omega_mu,ac = eta_aa omega_mu^a_c is antisymmetric in a, c for every mu."""
        return all(is_zero(ETA[a] * fr["omega"][mu, a, c] + ETA[c] * fr["omega"][mu, c, a])
                   for mu in range(8) for a in range(8) for c in range(8))


    diagonal = frame(sp.Integer(0))
    check_record(postulate_failures(diagonal) == 0 and antisymmetric(diagonal),
                 "diagonal frame: vielbein postulate (512 components), omega antisymmetric",
                 THEORY, ["vielbein_postulate", "spin_connection_antisymmetric"],
                 "(512 components)")
    nonzero = [(mu, a, c) for mu in range(8) for a in range(8) for c in range(a + 1, 8)
               if not is_zero(diagonal["omega"][mu, a, c])]
    omega_diagonal = diagonal["omega"]
    for mu, a, c in nonzero:
        say(f"omega_x{mu},(x{a})(x{c}) = "
            f"{sp.simplify(ETA[a] * omega_diagonal[mu, a, c])}")
    check_record(len(nonzero) == 10, "10 independent nonzero components omega_mu,ab (a < b)",
                 WOLFRAM, "omega_components",
                 f"exactly {len(nonzero)} independent nonzero omega_mu,ab "
                 "(a < b in the order x0..x7)")
    '''),
    md(r"""
    ## 8. The connection vanishes only in the formal flat limit: non-triviality

    Every one of the 10 components printed above is $a_4'$ times, or $h_4 = b_4'/(2b_4)
    - a_4'$ times, or $H$ times, one of the factors $\pm e^{a_4}$, $\pm
    e^{-a_4}b_4^{1/2}\cot z$, $\pm e^{-a_4}b_4^{1/2}W$ and $\pm W$, and these factors
    are never zero between the degenerate points (an exponential is never zero,
    $b_4 > 0$, $W > 0$, and $\cot z \neq 0$ away from the folds). The 28 matrices
    $S^{ab}$ ($a < b$) are linearly independent: written as rows of $16 \times 16 =
    256$ numbers they have rank 28 (rank: the number of independent rows). So $\Omega_\mu
    = \frac12\sum\omega_{\mu ab}S^{ab}$ is zero exactly when all its coefficients are.
    The next cell finds, for each of the 10 components, which of the three shapes it
    has (it writes `A1` for $a_4'$ and `h4` for $h_4$), counts three, four and three,
    computes the rank of the $S^{ab}$, and so checks, line by line:

    1. each component is $a_4'\cdot(\text{factor})$ (three of them: 3-space),
       $h_4\cdot(\text{factor})$ (four: the hidden direction and the three extra
       times) or $H\cdot(\text{factor})$ (three: the extra times), with a factor that
       is never zero;
    2. if $a_4' \neq 0$, the three components of the first kind are not zero; if
       $h_4 \neq 0$, the four of the second kind; if $H \neq 0$, the three of the third;
    3. so $\Omega_\mu = 0$ for every $\mu$ if and only if $a_4' = 0$, $h_4 = 0$ (that
       is, $b_4' = 0$ as well) AND $H = 0$, the formal limit. $H = 0$ is not a member
       of the author's family (the metric degenerates there), so for the author's
       metric the connection never vanishes in this frame.

    This is the core of the non-triviality statements [1] and [2] of the Revision
    record; whether a different frame can remove it is the question of sections 10 to
    12 (it can, exactly where the metric is flat).
    """),
    code(r'''
    A1 = sp.Symbol("A1", real=True)  # a letter that stands for a4'
    h4 = sp.Symbol("h4", real=True)  # a letter for h4 = b4'/(2 b4) - a4'
    allowed = [sign * factor for sign in (1, -1)
               for factor in (sp.exp(a4), s_b * sp.cot(z), s_b * W(x0), W(x0))]
    kinds = []  # for each component: "A1", "h4" or "H" (that rate times a factor)
    for mu, a, c in nonzero:
        value = sp.simplify(ETA[a] * omega_diagonal[mu, a, c])
        value = value.subs(b4p, 2 * (h4 + a4p) * b4).subs(a4p, A1)
        found = [str(coupling) for coupling in (A1, h4, H) for factor in allowed
                 if is_zero(value - coupling * factor)]  # which shape fits
        kinds.append(found[0] if len(found) == 1 else "no shape")
    n_A1, n_h4, n_H = kinds.count("A1"), kinds.count("h4"), kinds.count("H")
    report("components of the form a4' x factor, h4 x factor and H x factor",
           f"{n_A1}, {n_h4}, {n_H}")
    S_rows = np.array([[float(v) for v in S_AB[a][c]] for a in range(8)
                       for c in range(a + 1, 8)])  # 28 rows of 256 numbers
    rank_S = int(np.linalg.matrix_rank(S_rows))
    report("rank of the 28 matrices S^ab written as rows of 256 numbers", rank_S)
    # a4' != 0 makes the three "A1" components nonzero, h4 != 0 the four "h4" ones and
    # H != 0 the three "H" ones; with independent S^ab, Omega vanishes for every mu only
    # when a4' = 0, h4 = 0 (so b4' = 0) and H = 0.
    shapes_ok = n_A1 == 3 and n_h4 == 4 and n_H == 3 and rank_S == 28
    check_record(shapes_ok, "Omega_mu = 0 for every mu iff a4' = 0, b4' = 0 and H = 0 "
                 "(formal limit)", THEORY, "nontriviality_Omega_zero_iff_flat",
                 "the S^ab are linearly independent",
                 "every Omega_mu vanishes iff a4' = 0, a4' - b4'/(2 b4) = 0 (i.e. b4' = 0) "
                 "AND H = 0")
    check_record(shapes_ok, "the same in the independent Wolfram verifier", WOLFRAM,
                 "Omega_vanishes_iff_a4prime_b4prime_and_H_vanish",
                 "so all x4-parts vanish iff a4 and b4 are both constant, and for H > 0 "
                 "the spin connection never vanishes")
    '''),
    md(r"""
    ## 9. What cancels and what survives

    For each direction $\mu$ separately (no sum) the product $\gamma^{x_\mu}
    \Omega_{x_\mu}$ turns out to be a combination of $\gamma^{(4)}$ and $\gamma^{(0)}$
    only. The coefficient of $\gamma^{(0)}$ in a matrix $M$ is $\mathrm{tr}(\gamma^{(0)}
    M)/16$ and that of $\gamma^{(4)}$ is $-\mathrm{tr}(\gamma^{(4)}M)/16$ (because
    $(\gamma^{(0)})^2 = 1$, $(\gamma^{(4)})^2 = -1$, and the trace of a product of two
    different gammas is 0). The next cell computes both coefficients for every
    direction, checks that nothing else is left and that they are the record's
    $\frac12h_4$ (hidden direction), $\frac12a_4'$ (each 3-space direction), $0$ (time)
    and $\frac12h_4\gamma^{(4)} + \frac12He^{a_4}b_4^{-1/2}\gamma^{(0)}$ (each extra
    time); checks the sum $\gamma^\mu\Omega_\mu = G = c_g\gamma^{(0)} + v_g\gamma^{(4)}$;
    checks $GG = (c_g^2 - v_g^2)\,I_{16}$ (the cross terms cancel because
    $\gamma^{(0)}$ and $\gamma^{(4)}$ anticommute), which is $H^2(\frac94e^{2Hx_4/3} -
    \frac{25}{36})\,I_{16}$ on the history: where this number is not zero, $G$ can be
    undone (multiply by $G$ again and divide by the number), so $G\Psi = 0$ only when
    $\Psi = 0$, while where $c_g = \pm v_g$ the matrix $G = c_g(\gamma^{(0)} \pm
    \gamma^{(4)})$ has rank 8; checks the *divergence form* $\frac{1}{2\sqrt{|g|}}
    \sum_\mu\partial_\mu(\sqrt{|g|}\gamma^\mu) = G$ (the sign of $\cot z$ in $\sqrt{|g|}$
    cancels); checks $\{\gamma^\mu, \Omega_\mu\} = 0$ for each $\mu$ (which makes the
    connection drop out of the symmetrised Lagrangian); and draws the coefficients. It
    prints the partial sums in the record's notation (`A1` for $a_4'$, `B1` for
    $b_4'/b_4$).
    """),
    code(r'''
    per_direction = [(diagonal["gamma"][mu] * diagonal["Omega"][mu]).applyfunc(sp.simplify)
                     for mu in range(8)]
    coefficient_4 = [sp.simplify(-(G[4] * M).trace() / 16) for M in per_direction]
    coefficient_0 = [sp.simplify((G[0] * M).trace() / 16) for M in per_direction]
    nothing_else = all(
        all(is_zero(entry) for entry in
            per_direction[mu] - coefficient_4[mu] * G[4] - coefficient_0[mu] * G[0])
        for mu in range(8))
    for mu in range(8):
        say(f"gamma^x{mu} Omega_x{mu} = ({coefficient_4[mu]}) gamma^(x4) "
            f"+ ({coefficient_0[mu]}) gamma^(x0)")
    check(nothing_else, "each gamma^mu Omega_mu (no sum) is a combination of gamma^(x4) "
          "and gamma^(x0)")
    rate_h4 = b4p / (2 * b4) - a4p  # h4, the rate of the hidden block
    B1 = sp.Symbol("B1", real=True)  # the record's letter for b4'/b4


    def in_record_notation(expr):
        return sp.simplify(expr.subs(b4p, B1 * b4).subs(a4p, A1))


    hidden_sum = in_record_notation(coefficient_4[0] + sum(coefficient_4[5:8]))  # 2 h4
    space_sum = in_record_notation(sum(coefficient_4[1:4]))  # 3*A1/2
    extra_sum_0 = sp.simplify(sum(coefficient_0))  # 3 H e^a4 b4^(-1/2) / 2
    say(f"sums: hidden block (x0, x5, x6, x7) {hidden_sum}, 3-space {space_sum}, "
        f"gamma^(x0) part {extra_sum_0}")
    expected_4 = [rate_h4 / 2] + [a4p / 2] * 3 + [0] + [rate_h4 / 2] * 3
    expected_0 = [0] * 5 + [H * sp.exp(a4) / (2 * sp.sqrt(b4))] * 3
    check_record(all(is_zero(coefficient_4[mu] - expected_4[mu])
                     and is_zero(coefficient_0[mu] - expected_0[mu]) for mu in range(8)),
                 "per direction: h4/2, a4'/2 (x3), 0, and h4/2 with H e^a4 b4^(-1/2)/2 "
                 "(x3)", THEORY, "per_direction_terms",
                 "gamma^(x0) Omega_(x0) = (h4/2) gamma^(x4)",
                 "gamma^(xi) Omega_(xi) = (a4'/2) gamma^(x4) (i = 1,2,3)",
                 "gamma^(xt) Omega_(xt) = (h4/2) gamma^(x4) + (H/2) e^a4 b4^(-1/2) "
                 "gamma^(x0) (t = 5,6,7)", "gamma^(x4) Omega_(x4) = 0")
    total = sum(per_direction, sp.zeros(16, 16))
    c_g = sp.Rational(3, 2) * H * sp.exp(a4) / sp.sqrt(b4)  # (3/2) H e^a4 b4^(-1/2)
    v_g = b4p / b4 - a4p / 2  # b4'/b4 - a4'/2
    G_term = c_g * G[0] + v_g * G[4]  # the gravitational term of the diagonal frame
    check_record(all(is_zero(entry) for entry in total - G_term),
                 "gamma^mu Omega_mu = c_g gamma^(x0) + v_g gamma^(x4) in the diagonal "
                 "frame", THEORY, "gamma_mu_Omega_mu_equals_hidden_block_terms",
                 "gamma^mu Omega_mu = (3/2) H e^a4 b4^(-1/2) gamma^(x0) + (b4'/b4 - "
                 "a4'/2) gamma^(x4) exactly")
    parameters = json.loads(repository_file(
        "Revision/kohn_sham/results/parameters.json").read_text(encoding="utf-8"))
    A_history = sp.nsimplify(parameters["physics"]["historyA"])  # a4 = A H x4
    beta_4 = sp.nsimplify(parameters["physics"]["historyBeta"])  # b4 = e^(beta_4 A H x4)
    b4_zero = sp.nsimplify(parameters["physics"]["historyB4AtZero"])  # b4(0)
    history = {a4: A_history * H * x4, b4: b4_zero * sp.exp(beta_4 * A_history * H * x4)}
    square_history = sp.simplify((c_g**2 - v_g**2).subs(history).doit())
    say(f"c_g^2 - v_g^2 on the history: {square_history}")
    ranks = [(G[0] + sign * G[4]).rank() for sign in (1, -1)]  # c_g = +-v_g: G ~ these
    check_record(all(is_zero(entry) for entry in G_term * G_term
                     - (c_g**2 - v_g**2) * sp.eye(16))
                 and is_zero(square_history - H**2 * (sp.Rational(9, 4)
                                                      * sp.exp(2 * H * x4 / 3)
                                                      - sp.Rational(25, 36)))
                 and ranks == [8, 8],
                 "G G = (c_g^2 - v_g^2) 1, H^2 ((9/4) e^(2 H x4/3) - 25/36) on the "
                 "history; rank 8 where c_g = +-v_g", THEORY, "gravity_term_square",
                 "M M = (cg^2 - vg^2) I16 exactly",
                 "M M = H^2 ((9/4) e^(2 H x4/3) - 25/36) I16 > 0", "(ranks [8, 8])")
    sign_cot = sp.Symbol("sigma", real=True)  # the sign of cot z: sqrt|g| = sigma f0...f7
    sqrt_g = sign_cot * volume
    divergence = sum((sp.diff(sqrt_g * diagonal["gamma"][mu], x[mu]) for mu in range(8)),
                     sp.zeros(16, 16)) / (2 * sqrt_g)
    check_record(all(is_zero(entry) for entry in divergence - G_term),
                 "(1/(2 sqrt|g|)) d_mu(sqrt|g| gamma^mu) = c_g gamma^(x0) + v_g "
                 "gamma^(x4) (divergence form)", THEORY, "divergence_of_sqrtg_gamma",
                 "(1/2)(1/sqrt|g|) d_mu(sqrt|g| gamma^mu) = (3/2) H e^a4 b4^(-1/2) "
                 "gamma^(x0) + (b4'/b4 - a4'/2) gamma^(x4) = gamma^mu Omega_mu")
    check_record(all(all(is_zero(entry) for entry in
                         diagonal["gamma"][mu] * diagonal["Omega"][mu]
                         + diagonal["Omega"][mu] * diagonal["gamma"][mu])
                     for mu in range(8)),
                 "{gamma^mu, Omega_mu} = 0 for each mu: Omega drops out of the Lagrangian",
                 "Revision/theory/reports/python-scope.json",
                 "connection_free_lagrangian_same_equations",
                 "{gamma^mu, Omega_mu} = 0 for each mu separately")

    names = [f"$x_{mu}$" for mu in range(8)] + ["sum"]
    a4_parts = [float(sp.simplify(c4.subs(b4p, 0) / a4p)) for c4 in coefficient_4]
    b4_parts = [float(sp.simplify(c4.subs(a4p, 0) / (b4p / b4))) for c4 in coefficient_4]
    values_0 = [float(sp.simplify(c0 / (H * sp.exp(a4) / sp.sqrt(b4))))
                for c0 in coefficient_0]  # in units of H e^a4 b4^(-1/2)
    for values in (a4_parts, b4_parts, values_0):
        values.append(sum(values))
    positions = np.arange(9)
    colours = ["tab:green"] + ["tab:blue"] * 3 + ["gray"] + ["tab:red"] * 3 + ["black"]
    fig, (left, right) = plt.subplots(1, 2, figsize=(10.0, 4.0))
    left.bar(positions - 0.2, a4_parts, width=0.38, color="tab:purple",
             label="part with $a_4'$ (units of $a_4'$)")
    left.bar(positions + 0.2, b4_parts, width=0.38, color="tab:orange",
             label="part with $b_4'/b_4$ (units of $b_4'/b_4$)")
    left.set_title("coefficient of $\\gamma^{(4)}$")
    left.set_ylabel("coefficient")
    left.legend(fontsize=8, loc="lower left")
    right.bar(positions, values_0, color=colours)
    right.set_title("coefficient of $\\gamma^{(0)}$, units of $He^{a_4}b_4^{-1/2}$")
    for panel in (left, right):
        panel.axhline(0.0, color="black", linewidth=0.8)
        panel.set_xticks(positions)
        panel.set_xticklabels(names)
        panel.set_xlabel("direction $\\mu$ of $\\gamma^{\\mu}\\Omega_{\\mu}$")
    save_figure(fig, "cancel_and_survive",
                "The term $\\gamma^\\mu\\Omega_\\mu$ of the field equation in the "
                "diagonal frame of the corrected metric, direction by direction (no "
                "sum) and summed. Left: the coefficient of $\\gamma^{(4)}$, split into "
                "its part with $a_4'$ (purple, in units of $a_4'$) and its part with "
                "$b_4'/b_4$ (orange, in units of $b_4'/b_4$): the three 3-space "
                "directions give $+\\frac12$ each and the three extra times "
                "$-\\frac12$ each, which cancel, but the hidden direction $x_0$ adds "
                "$-\\frac12$; the four directions of the hidden block give "
                "$\\frac14b_4'/b_4$ each; the sums are $-\\frac12$ and $1$, so $v_g = "
                "b_4'/b_4 - a_4'/2$. Right: the coefficient of $\\gamma^{(0)}$ in units "
                "of $He^{a_4}b_4^{-1/2}$; only the three extra times (red) contribute, "
                "$\\frac12$ each, and the sum is $\\frac32$: $c_g = \\frac32He^{a_4}"
                "b_4^{-1/2}$. Exact values from sympy, for all functions $a_4$, $b_4$.")
    '''),
    md(r"""
    ## 10. The term sees the deflating hidden block; the curvature and the flat member

    The term $G = c_g\gamma^{(0)} + v_g\gamma^{(4)}$ contains $a_4$: its
    $\gamma^{(0)}$ coefficient is $\frac32H$ times the inverse scale factor
    $e^{a_4}b_4^{-1/2}$ of the hidden block, which grows as the block deflates (in the
    withdrawn metric of 2026-10-14 the term contained no $a_4$). The next cell computes
    the Riemann tensor from the Christoffel symbols,
    $R^\rho{}_{\sigma\mu\nu} = \partial_\mu\Gamma^\rho{}_{\nu\sigma} -
    \partial_\nu\Gamma^\rho{}_{\mu\sigma} + \sum_\lambda(\Gamma^\rho{}_{\mu\lambda}
    \Gamma^\lambda{}_{\nu\sigma} - \Gamma^\rho{}_{\nu\lambda}\Gamma^\lambda{}_{\mu\sigma})$,
    and from it all 64 components of the mixed Ricci tensor $R^\mu{}_\nu$; it checks
    that the 56 components off the diagonal vanish and that the diagonal ones are the
    record's ($k = e^{2a_4}/b_4$, $u = b_4'/b_4$): $R^{x_0}{}_{x_0} = R^{x_t}{}_{x_t} =
    -3H^2k + (a_4')^2 - a_4'' - \frac52a_4'u + \frac12b_4''/b_4 + \frac12u^2$ (the hidden
    direction and the extra times form one block), $R^{x_i}{}_{x_i} = -(a_4')^2 +
    a_4'' + 2a_4'u$, $R^{x_4}{}_{x_4} = 7(a_4')^2 - a_4'' - 4a_4'u + 2b_4''/b_4 - u^2$,
    and the Ricci scalar $R = -12H^2k + 8(a_4')^2 - 2a_4'' - 8a_4'u + 4b_4''/b_4 +
    u^2$. Then it checks that ALL Riemann components vanish for the special history
    $a_4 = 0$, $b_4 = H^2x_4^2$ (the corrected metric is flat there; computing the 1792
    components with $\mu < \nu$ suffices, because $R^\rho{}_{\sigma\nu\mu} =
    -R^\rho{}_{\sigma\mu\nu}$), prints $G$ for that flat member (it is not zero: there
    the term is a pure frame effect), and checks that on the history of the record
    $R^{x_i}{}_{x_i} = \frac53H^2 \neq 0$ at every time. Last, it draws, along the
    history at $z = \pi/4$ and $H = 1$, four pieces of the connection and the parts of
    the term.
    """),
    code(r'''
    def riemann(rho, sigma, mu, nu, symbols=None):
        """R^rho_sigma,mu,nu from the Christoffel symbols (not simplified)."""
        Gs = Gam if symbols is None else symbols
        value = sp.diff(Gs[rho][nu][sigma], x[mu]) - sp.diff(Gs[rho][mu][sigma], x[nu])
        for lam in range(8):
            value += Gs[rho][mu][lam] * Gs[lam][nu][sigma] \
                - Gs[rho][nu][lam] * Gs[lam][mu][sigma]
        return value


    ricci_low = [[sum(riemann(rho, s, rho, n) for rho in range(8)) for n in range(8)]
                 for s in range(8)]  # R_sn = R^rho_s,rho,n
    ricci = [[ricci_low[mu][nu] / g[mu] for nu in range(8)] for mu in range(8)]  # R^mu_nu
    off_diagonal_zero = all(is_zero(ricci[mu][nu]) for mu in range(8) for nu in range(8)
                            if mu != nu)
    a4pp, u, v = sp.diff(a4, x4, 2), b4p / b4, sp.diff(b4, x4, 2) / b4
    k_ratio = sp.exp(2 * a4) / b4  # k = e^(2 a4)/b4
    block = (-3 * H**2 * k_ratio + a4p**2 - a4pp - sp.Rational(5, 2) * a4p * u + v / 2
             + u**2 / 2)  # R^x0_x0 = R^xt_xt
    expected = ([block] + [-a4p**2 + a4pp + 2 * a4p * u] * 3
                + [7 * a4p**2 - a4pp - 4 * a4p * u + 2 * v - u**2] + [block] * 3)
    check_record(off_diagonal_zero and all(is_zero(ricci[a][a] - expected[a])
                                           for a in range(8)),
                 "R^mu_nu is diagonal and its eight entries equal the record",
                 WOLFRAM, "ricci_mixed_components", "R^mu_nu is DIAGONAL",
                 "R^x0_x0 = R^xt_xt = -3 Cb + a4'^2 - a4'' - (5/2) a4' b4'/b4 + (1/2) "
                 "b4''/b4 + (1/2)(b4'/b4)^2 (t = 5, 6, 7",
                 "R^xi_xi = -a4'^2 + a4'' + 2 a4' b4'/b4 (i = 1, 2, 3)",
                 "R^x4_x4 = 7 a4'^2 - a4'' - 4 a4' b4'/b4 + 2 b4''/b4 - (b4'/b4)^2")
    ricci_scalar = sum(ricci[a][a] for a in range(8))
    check_record(is_zero(ricci_scalar - (-12 * H**2 * k_ratio + 8 * a4p**2 - 2 * a4pp
                                         - 8 * a4p * u + 4 * v + u**2)),
                 "Ricci scalar R = -12 H^2 e^(2 a4)/b4 + 8 a4'^2 - 2 a4'' - 8 a4' "
                 "b4'/b4 + 4 b4''/b4 + (b4'/b4)^2", THEORY, "curvature_and_flat_member",
                 "= -12 H^2 e^(2 a4)/b4 + 8 a4'^2 - 2 a4'' - 8 a4' b4'/b4 + 4 b4''/b4 + "
                 "(b4'/b4)^2")
    flat = {a4: 0, b4: H**2 * x4**2}  # the special history of the flat member
    Gam_flat = [[[sp.simplify(Gam[l][m][n].subs(flat).doit()) for n in range(8)]
                 for m in range(8)] for l in range(8)]
    flat_ok = all(is_zero(riemann(rho, s, mu, nu, Gam_flat)) for rho in range(8)
                  for s in range(8) for mu in range(8) for nu in range(mu + 1, 8))
    G_flat = sp.simplify((c_g * G[0] + v_g * G[4]).subs(flat).doit())
    say(f"G on the flat member: ({sp.simplify(c_g.subs(flat).doit())}) gamma^(x0) + "
        f"({sp.simplify(v_g.subs(flat).doit())}) gamma^(x4)")
    space_history = sp.simplify(ricci[1][1].subs(history).doit())
    say(f"R^x1_x1 on the history: {space_history}")
    check_record(flat_ok and G_flat != sp.zeros(16, 16)
                 and is_zero(space_history - sp.Rational(5, 3) * H**2),
                 "flat for a4 = 0, b4 = H^2 x4^2 (all Riemann components vanish, G != 0 "
                 "there); curved on the history (R^x1_x1 = 5 H^2/3)",
                 WOLFRAM, "flat_member_and_curvature",
                 "the corrected metric is FLAT for a4 = 0, b4 = H^2 x4^2 (all 4096 "
                 "R^r_smn vanish", "R != 0 (curved)")
    check_record(total.has(a4) and not is_zero(ricci[4][4]),
                 "gamma^mu Omega_mu contains a4 (e^a4 and a4'), and R^x4_x4 is not zero",
                 "Revision/theory/reports/python-scope.json",
                 "gammaOmega_sees_the_hidden_block", "contains a4 (e^a4 and a4')",
                 "R^x4_x4 = 7 a4'^2 - a4'' - 4 a4' b4'/b4 + 2 b4''/b4 - (b4'/b4)^2")
    check(A_history == 1 and beta_4 == sp.Rational(4, 3) and b4_zero == 1,
          "the history of the record: A = 1, beta_4 = 4/3, b4(0) = 1",
          record="Revision/kohn_sham/results/parameters.json, physics.historyA, "
                 "physics.historyBeta and physics.historyB4AtZero")


    def along_history(expr):
        """A numpy function of x4 for expr with H = 1, the history, z = pi/4."""
        concrete = sp.sympify(expr).subs(W(x0), explicit_W).subs(history).doit()
        concrete = concrete.subs({H: 1, x0: sp.pi / 24})  # z = 6 x0 = pi/4
        return sp.lambdify(x4, concrete, "numpy")


    times = np.linspace(0.0, 4.0, 201)
    pieces = {"3-space: $\\omega_{x_1,(1)(4)} = a_4'e^{a_4}$": omega_diagonal[1, 1, 4],
              "hidden: $|\\omega_{x_0,(0)(4)}| = |h_4|e^{-a_4}b_4^{1/2}\\cot z$":
                  omega_diagonal[0, 0, 4],
              "extra time: $|\\omega_{x_5,(4)(5)}| = |h_4|e^{-a_4}b_4^{1/2}W$":
                  -ETA[4] * omega_diagonal[5, 4, 5],
              "extra time: $\\omega_{x_5,(0)(5)} = HW$": omega_diagonal[5, 0, 5]}
    fig, (left, right) = plt.subplots(1, 2, figsize=(10.0, 4.2))
    for (label, expr), style in zip(pieces.items(), ("-", "--", "-.", ":")):
        left.plot(times, np.abs(along_history(expr)(times)) * np.ones_like(times),
                  style, label=label)
    left.set_yscale("log")
    left.set_xlabel("time $x_4$")
    left.set_ylabel("size of the component")
    left.set_title("Pieces of the connection")
    left.legend(fontsize=7)
    c_g_path = along_history(c_g)(times) * np.ones_like(times)
    space_part = along_history(sum(coefficient_4[1:4]))(times) * np.ones_like(times)
    block_part = along_history(coefficient_4[0] + sum(coefficient_4[5:8]))(times) \
        * np.ones_like(times)
    right.plot(times, c_g_path, color="tab:red", label="$c_g = \\frac32He^{a_4}b_4^{-1/2}$")
    right.plot(times, space_part, color="tab:blue", label="3-space: $\\frac32a_4'$")
    right.plot(times, block_part, color="tab:green", label="hidden block: $2h_4$")
    right.plot(times, space_part + block_part, color="black",
               label="$v_g = \\frac32a_4' + 2h_4 = \\frac56H$")
    right.axhline(0.0, color="black", linewidth=0.6)
    right.set_xlabel("time $x_4$")
    right.set_ylabel("coefficient")
    right.set_title("The parts of the term")
    right.legend(fontsize=8);
    save_figure(fig, "pieces_along_history",
                "Along the canonical history $a_4 = x_4$, $b_4 = e^{4x_4/3}$ of the "
                "Kohn-Sham record ($A = H = 1$, a prescribed background) at $z = "
                "\\pi/4$, against the time $x_4$. Left, logarithmic axis: four "
                "components of the spin connection of the diagonal frame; that of the "
                "inflating direction $x_1$ grows like $e^{a_4}$, those with the rate "
                "$h_4 = b_4'/(2b_4) - a_4' = -\\frac13$ of the hidden direction and of "
                "the extra time $x_5$ shrink like $e^{-a_4}b_4^{1/2} = e^{-x_4/3}$, and "
                "$HW$ stays constant. Right: the parts of the term: the coefficient "
                "$c_g$ of $\\gamma^{(0)}$ grows like $e^{x_4/3}$ as the hidden block "
                "deflates, while the coefficient of $\\gamma^{(4)}$, the sum of the "
                "3-space part $\\frac32a_4' = \\frac32$ and of the hidden-block part "
                "$2h_4 = -\\frac23$, stays at $v_g = \\frac56$.")
    '''),
    md(r"""
    ## 11. The boosted frame: the term depends on the frame

    The next cell builds the frame boosted by a rapidity $b(x_4)$, any function of the
    time (a sympy `Function`). It checks that the new frame gives the SAME metric
    ($\sum_a\eta_{aa}e'^a{}_\mu e'^a{}_\nu = g_{\mu\nu}$ for all 64 pairs) and that its
    canonical connection obeys the vielbein postulate, and then that
    $\gamma'^\mu\Omega'_\mu = (c_g - \frac{b'}{2})(\cosh b\,\gamma^{(0)} -
    \sinh b\,\gamma^{(4)}) + v_g(\cosh b\,\gamma^{(4)} - \sinh b\,\gamma^{(0)})$ exactly
    (for a rapidity $b = \beta x_4 + b_0$ of constant rate $\beta$ this is the formula
    of the record, with $c_g - \beta/2$). Its coefficients $c_0$ of $\gamma^{(0)}$ and
    $c_4$ of $\gamma^{(4)}$ obey $\cosh b\,c_4 + \sinh b\,c_0 = v_g$ for every rapidity
    (multiply out; $\cosh^2b - \sinh^2b = 1$), so no such boost makes the term vanish
    unless $v_g = 0$, that is $b_4'/b_4 = a_4'/2$. For a rapidity of rate $b' = 2c_g$
    the part with $c_g$ is gone for every $H$, $a_4$ and $b_4$, and only $v_g(\cosh b\,
    \gamma^{(4)} - \sinh b\,\gamma^{(0)})$ is left, although the spinor connections
    $\Omega'_\mu$ themselves are not zero (for every $\mu$). The 28 matrices $S^{ab}$
    ($a < b$) are linearly independent (rank 28, checked in section 8), so $\Omega'_\mu$
    is zero exactly when all its coefficients $\omega'_{\mu ab}$ are. Every check also
    compares with the text of the Revision record.
    """),
    code(r'''
    rapidity = sp.Function("b")(x4)  # any rapidity b(x4)
    rate_b = sp.diff(rapidity, x4)  # b'
    boosted = frame(rapidity)
    e_b = boosted["e"]
    same_metric = all(
        is_zero(sum(ETA[a] * e_b[a, mu] * e_b[a, nu] for a in range(8))
                - (g[mu] if mu == nu else 0)) for mu in range(8) for nu in range(8))
    SCOPE = "Revision/theory/reports/python-scope.json"  # the record of these checks
    check_record(same_metric and all(is_zero(v) for v in e_b * boosted["E"] - sp.eye(8)),
                 "the boosted frame gives the same metric (64 entries); e' E' = 1",
                 SCOPE, "boosted_frame_reproduces_metric",
                 "equals the corrected metric for all 64 (mu, nu)")
    failures = postulate_failures(boosted)  # the number of nonzero components
    check_record(failures == 0 and antisymmetric(boosted),
                 "boosted frame: vielbein postulate (512 components), omega' antisymmetric",
                 SCOPE, "boosted_frame_canonical_connection",
                 f"holds for all 512 (a, mu, nu) ({failures} failures)")
    total_boosted = sum((boosted["gamma"][mu] * boosted["Omega"][mu] for mu in range(8)),
                        sp.zeros(16, 16))
    v_boost = sp.cosh(rapidity) * G[0] - sp.sinh(rapidity) * G[4]
    w_boost = sp.cosh(rapidity) * G[4] - sp.sinh(rapidity) * G[0]
    formula = (c_g - rate_b / 2) * v_boost + v_g * w_boost
    c0 = (c_g - rate_b / 2) * sp.cosh(rapidity) - v_g * sp.sinh(rapidity)
    c4 = -(c_g - rate_b / 2) * sp.sinh(rapidity) + v_g * sp.cosh(rapidity)
    beta, b0 = sp.symbols("beta b0", real=True)  # a rapidity beta x4 + b0
    linear = {rapidity: beta * x4 + b0}
    formula_linear = (c_g - beta / 2) * v_boost.subs(linear) + v_g * w_boost.subs(linear)
    check_record(all(is_zero(entry) for entry in total_boosted - formula)
                 and all(is_zero(entry) for entry in formula - c0 * G[0] - c4 * G[4])
                 and is_zero(sp.cosh(rapidity) * c4 + sp.sinh(rapidity) * c0 - v_g)
                 and all(is_zero(entry) for entry in formula.subs(linear).doit()
                         - formula_linear),
                 "gamma'^mu Omega'_mu = (c_g - b'/2) v + v_g w; cosh b c4 + sinh b c0 = "
                 "v_g", SCOPE, "boosted_frame_gammaOmega_formula",
                 "gamma'^mu Omega'_mu = (cg - beta/2) (cosh b gamma^(x0) - sinh b "
                 "gamma^(x4)) + vg (cosh b gamma^(x4) - sinh b gamma^(x0))",
                 "cosh b c4 + sinh b c0 = vg for every beta")
    removing = {rate_b: 2 * c_g}  # the rapidity rate b' = 2 c_g
    nonzero_Omega = [mu for mu in range(8) if not all(
        is_zero(boosted["omega"][mu, a, c].subs(removing))
        for a in range(8) for c in range(a + 1, 8))]
    nonzero_text = ", ".join(f"x{mu}" for mu in nonzero_Omega)  # "x0, x1, ..."
    say("b' = 2 c_g: Omega'_mu is nonzero for mu = " + nonzero_text)
    check_record(all(is_zero(entry) for entry in total_boosted.subs(removing)
                     - v_g * w_boost)
                 and nonzero_Omega == list(range(8)),
                 "b' = 2 c_g: gamma'^mu Omega'_mu = v_g w, only the v_g part; Omega'_mu != "
                 "0 for every mu", SCOPE, "boosted_frame_removes_only_the_H_term",
                 "with a rapidity b(x4) of rate b' = 2 cg = 3 H e^a4 b4^(-1/2)",
                 "is vg (cosh b gamma^(x4) - sinh b gamma^(x0))",
                 f"Omega'_mu itself is nonzero for mu = {nonzero_text}")
    '''),
    md(r"""
    The next cell draws the size of the term, $\lVert M\rVert = \sqrt{\mathrm{tr}
    (M^TM)/16}$ (for $M = \gamma^{(0)}$ and for $M = \gamma^{(4)}$ this is 1, and for
    $M = c_0\gamma^{(0)} + c_4\gamma^{(4)}$ it is $\sqrt{c_0^2 + c_4^2}$), on the history
    of the record ($c_g = \frac32e^{x_4/3}$, $v_g = \frac56$ for $H = 1$). On the left
    against the rapidity rate $\beta$ at $x_4 = 0$ for a rapidity with $b(0) = 0$, where
    it is $\sqrt{(c_g - \beta/2)^2 + v_g^2}$: $\sqrt{106}/6$ in the diagonal frame
    ($\beta = 0$) and smallest, $v_g = \frac56$, at $\beta = 2c_g = 3$. On the right
    against $x_4$ for four frames: the diagonal frame, the constant rate $b = 3x_4$
    (which removes the $c_g$ part only at $x_4 = 0$), the removing rapidity $b =
    9(e^{x_4/3} - 1)$ with $b' = 2c_g$ at every time, and half of it. The cell evaluates
    the formula, which the previous cell showed to be equal, entry by entry, to the
    computed matrix $\gamma'^\mu\Omega'_\mu$.
    """),
    code(r'''
    def term_on_history(rapidity_expr):
        """A numpy function of x4: the 16 x 16 matrix gamma'^mu Omega'_mu for the given
        rapidity b(x4), on the history with H = 1."""
        concrete = formula.subs(rapidity, rapidity_expr).doit()
        concrete = concrete.subs(history).doit().subs(H, 1)
        return sp.lambdify(x4, concrete, "numpy")


    def size(matrix):
        """sqrt(tr(M^T M)/16): the size of a 16 x 16 matrix, 1 for gamma^(x0)."""
        matrix = np.array(matrix, dtype=float)
        return np.sqrt(np.trace(matrix.T @ matrix) / 16)


    frames = {"diagonal frame, $b = 0$": sp.Integer(0),
              "constant rate, $b = 3x_4$": 3 * x4,
              "half: $b = \\frac92(e^{x_4/3} - 1)$":
                  sp.Rational(9, 2) * (sp.exp(x4 / 3) - 1),
              "removing: $b = 9(e^{x_4/3} - 1)$": 9 * (sp.exp(x4 / 3) - 1)}
    terms = {label: term_on_history(expr) for label, expr in frames.items()}
    beta_values = np.linspace(0.0, 8.0, 161)
    linear_term = term_on_history(beta * x4)  # rate beta, b(0) = 0; still has beta
    sizes_beta = [size(sp.Matrix(linear_term(0.0)).subs(beta, bv)) for bv in beta_values]
    diagonal_size = size(terms["diagonal frame, $b = 0$"](0.0))
    removing_size = size(terms["removing: $b = 9(e^{x_4/3} - 1)$"](0.0))
    report("size at x4 = 0: diagonal frame, removing frame",
           f"{diagonal_size:.6f}, {removing_size:.6f}")
    check(abs(diagonal_size - np.sqrt(106.0) / 6) < 1e-12
          and abs(removing_size - 5.0 / 6.0) < 1e-12
          and min(sizes_beta) >= 5.0 / 6.0 - 1e-12,
          "on the history at x4 = 0: size sqrt(106)/6 in the diagonal frame, at least "
          "v_g = 5/6 for every rate beta, and 5/6 for b' = 2 c_g")
    fig, (left, right) = plt.subplots(1, 2, figsize=(10.0, 4.0))
    left.plot(beta_values, sizes_beta)
    left.plot([0.0, 3.0], [diagonal_size, removing_size], "o", color="black")
    left.annotate("diagonal frame: $c_g\\gamma^{(0)} + v_g\\gamma^{(4)}$",
                  (0.0, diagonal_size), (0.4, 2.6))
    left.annotate("$\\beta = 2c_g$: only $v_g\\gamma^{(4)}$", (3.0, removing_size),
                  (3.4, 0.3))
    left.set_xlabel("rapidity rate $\\beta = b'(0)$ (units of $H$)")
    left.set_ylabel("size of $\\gamma'^\\mu\\Omega'_\\mu$ (units of $H$)")
    left.set_title("At $x_4 = 0$, $b(0) = 0$")
    left.set_ylim(0.0, 3.2)
    times = np.linspace(0.0, 1.0, 101)
    for label, function in terms.items():
        right.plot(times, [size(function(t)) for t in times], label=label)
    right.set_yscale("log")
    right.set_xlabel("time $x_4$ (units of $1/H$)")
    right.set_ylabel("size (units of $H$)")
    right.set_title("Against time, on the history")
    right.legend(fontsize=8);
    save_figure(fig, "boost_size",
                "The size $\\sqrt{\\mathrm{tr}(M^TM)/16}$ of the term $M = "
                "\\gamma'^\\mu\\Omega'_\\mu$ of the field equation in frames boosted in "
                "the $(x_4, x_0)$ plane, on the history of the Revision record ($c_g = "
                "\\frac32e^{x_4/3}$, $v_g = \\frac56$ for $H = 1$); sizes in units of "
                "$H$. Left: against the rapidity rate $\\beta = b'(0)$ at $x_4 = 0$ with "
                "$b(0) = 0$; the diagonal frame gives $\\sqrt{106}/6 \\approx 1.716$, and "
                "the size $\\sqrt{(c_g - \\beta/2)^2 + v_g^2}$ is smallest, $v_g = "
                "\\frac56$, at $\\beta = 2c_g = 3$. Right: against the time $x_4$ "
                "(logarithmic axis) for the diagonal frame, a constant rate $b = 3x_4$, "
                "the removing rapidity $b = 9(e^{x_4/3} - 1)$, whose rate is $2c_g$ at "
                "every time and whose term $v_g(\\cosh b\\,\\gamma^{(4)} - \\sinh b\\,"
                "\\gamma^{(0)})$ has the size $v_g\\sqrt{\\cosh 2b}$, never zero, and "
                "half of it. The metric is the same in every one of these frames.")
    '''),
    md(r"""
    The next cell draws the $16 \times 16$ matrices themselves as colour maps (red
    positive, blue negative, white zero): $\gamma^\mu\Omega_\mu$ of the diagonal frame,
    $\gamma'^\mu\Omega'_\mu$ for the constant rate $b = 3x_4$ and for the removing
    rapidity $b = 9(e^{x_4/3} - 1)$, at $x_4 = 0.3$ on the history of the record, with
    $H = 1$.
    """),
    code(r'''
    maps = [("diagonal frame", terms["diagonal frame, $b = 0$"](0.3)),
            ("boosted, $b = 3x_4$", terms["constant rate, $b = 3x_4$"](0.3)),
            ("boosted, $b' = 2c_g$", terms["removing: $b = 9(e^{x_4/3} - 1)$"](0.3))]
    fig, panels = plt.subplots(1, 3, figsize=(11.0, 3.9))
    for panel, (title, matrix) in zip(panels, maps):
        image = panel.imshow(np.array(matrix, dtype=float), cmap="RdBu_r", vmin=-2.0,
                             vmax=2.0)
        panel.set_title(title, fontsize=10)
        panel.set_xticks([0, 5, 10, 15])
        panel.set_yticks([0, 5, 10, 15])
        panel.set_xlabel("column")
        panel.grid(False)  # no grid lines over the coloured squares
    panels[0].set_ylabel("row")
    fig.colorbar(image, ax=list(panels), shrink=0.8, label="entry (units of $H$)")
    save_figure(fig, "heat_maps",
                "The $16 \\times 16$ matrix $\\gamma^\\mu\\Omega_\\mu$ of the field "
                "equation as a colour map (rows and columns numbered from 0; red "
                "positive, blue negative, white zero; entries in units of $H$, $H = 1$, "
                "time $x_4 = 0.3$, on the history of the Revision record, where $c_g = "
                "\\frac32e^{0.1} = 1.658$ and $v_g = \\frac56$). Left: diagonal frame, "
                "$c_g\\gamma^{(0)} + v_g\\gamma^{(4)}$, sixteen entries $c_g$ and "
                "sixteen entries $\\pm v_g$. Middle: frame boosted with the constant "
                "rate $b = 3x_4$ ($b = 0.9$). Right: frame boosted with the removing "
                "rapidity $b = 9(e^{x_4/3} - 1)$ ($b = 0.946$), only $v_g(\\cosh b\\,"
                "\\gamma^{(4)} - \\sinh b\\,\\gamma^{(0)})$: the part $c_g\\gamma^{(0)}$ is "
                "gone, the part $v_g$ is not. Same metric, same field equation, "
                "different frames.")
    '''),
    md(r"""
    ## 12. The connection itself vanishes in no frame: the curvature

    If $\Omega'_\mu$ were zero in some frame, the spinor curvature $F_{\mu\nu} =
    \partial_\mu\Omega_\nu - \partial_\nu\Omega_\mu + [\Omega_\mu, \Omega_\nu]$ would
    be zero there. The next cell computes $F_{x_5x_0}$ (the component that the record
    uses) in the diagonal frame and in the frame boosted with $b' = 2c_g$ (where the
    part $c_g\gamma^{(0)}$ of $\gamma'^\mu\Omega'_\mu$ is gone) and checks:

    1. in both frames $F_{x_5x_0} = \frac14\sum_{\rho,\sigma}R_{\rho\sigma x_5x_0}
       \gamma^\rho\gamma^\sigma$ with $R_{\rho\sigma\mu\nu} =
       g_{\rho\rho}R^\rho{}_{\sigma\mu\nu}$: the curvature of the connection is the
       Riemann tensor of the metric;
    2. in both frames $F_{x_5x_0} = c_{05}\,\gamma^{(0)}\gamma^{(5)} +
       c_{45}\,\gamma^{(4)}\gamma^{(5)}$ with two numbers $c_{05}, c_{45}$ (found as
       traces, like the coefficients of section 9, and printed); in the diagonal frame
       $c_{45} = 0$ and $c_{05} = \frac12\cot z\,W(h_4^2e^{-2a_4}b_4 - H^2)$;
    3. hence $F_{x_5x_0}^2 = (c_{05}^2 - c_{45}^2)\,I_{16}$, because
       $(\gamma^{(0)}\gamma^{(5)})^2 = +1$, $(\gamma^{(4)}\gamma^{(5)})^2 = -1$ and the
       two products anticommute; and $c_{05}^2 - c_{45}^2$ is the SAME in both frames.
       It must be: the matrices $\gamma^\rho$ and $\gamma'^\rho$ of the two frames obey
       the same relations $\{\gamma^\rho, \gamma^\sigma\} = 2g^{\rho\sigma}$, so
       (because the 16-dimensional representation is irreducible) there is an
       invertible $16 \times 16$ matrix $S$ with $\gamma'^\rho = S\gamma^\rho S^{-1}$,
       and then $F' = SFS^{-1}$ and $F'^2 = SF^2S^{-1} = F^2$;
    4. $c_{05}$ vanishes on the flat member ($a_4 = 0$, $b_4 = H^2x_4^2$, where $h_4
       e^{-a_4}b_4^{1/2} = H$), and $F'_{x_5x_0}$ is not zero for general $a_4$, $b_4$.

    Since the Riemann tensor does not depend on the frame, no frame can remove
    $\Omega_\mu$ wherever the metric is curved.
    """),
    code(r'''
    def spinor_curvature(fr):
        """F_x5x0 = d_5 Omega_0 - d_0 Omega_5 + [Omega_5, Omega_0]."""
        O5, O0 = fr["Omega"][5], fr["Omega"][0]
        return sp.diff(O0, x[5]) - sp.diff(O5, x[0]) + O5 * O0 - O0 * O5


    def riemann_side(fr):
        """(1/4) sum R_rho,sigma,x5,x0 gamma^rho gamma^sigma in the frame fr."""
        result = sp.zeros(16, 16)
        for rho in range(8):
            for sigma in range(8):
                value = g[rho] * riemann(rho, sigma, 5, 0)  # lower the first index
                if not is_zero(value):
                    result += value * fr["gamma"][rho] * fr["gamma"][sigma] / 4
        return result


    P05, P45 = G[0] * G[5], G[4] * G[5]  # gamma^(0) gamma^(5) and gamma^(4) gamma^(5)


    def two_coefficients(F):
        """c05, c45 with F = c05 P05 + c45 P45 (P05^2 = 1, P45^2 = -1), and whether
        nothing else is left."""
        c05 = sp.simplify((P05 * F).trace() / 16)
        c45 = sp.simplify(-(P45 * F).trace() / 16)
        return c05, c45, all(is_zero(v) for v in F - c05 * P05 - c45 * P45)


    frame_removing = {"Omega": [M.subs(removing) for M in boosted["Omega"]],
                      "gamma": boosted["gamma"]}  # the frame with b' = 2 c_g
    F_diagonal = spinor_curvature(diagonal)
    F_boosted = spinor_curvature(frame_removing)
    check_record(all(is_zero(v) for v in F_diagonal - riemann_side(diagonal)),
                 "diagonal frame: F_x5x0 = (1/4) R_rho,sigma,x5,x0 gamma^rho gamma^sigma",
                 THEORY, "spinor_curvature_equals_riemann",
                 "= (1/4) R_{rho sigma mu nu} gamma^rho gamma^sigma")
    check(all(is_zero(v) for v in F_boosted - riemann_side(frame_removing)),
          "boosted frame (b' = 2 c_g): F'_x5x0 = (1/4) R gamma'^rho gamma'^sigma")
    c05, c45, only_two = two_coefficients(F_diagonal)
    c05_b, c45_b, only_two_b = two_coefficients(F_boosted)
    say(f"diagonal frame: c05 = {c05}")
    say(f"diagonal frame: c45 = {c45}")
    say(f"boosted frame:  c05 = {c05_b}")
    say(f"boosted frame:  c45 = {c45_b}")
    expected_c05 = sp.cot(z) * W(x0) * (rate_h4**2 * sp.exp(-2 * a4) * b4 - H**2) / 2
    check(only_two and only_two_b and is_zero(c45) and is_zero(c05 - expected_c05),
          "in both frames F_x5x0 = c05 g0 g5 + c45 g4 g5; diagonal: c45 = 0, c05 = "
          "(1/2) cot z W (h4^2 e^(-2 a4) b4 - H^2)")
    check(is_zero(c05_b**2 - c45_b**2 - c05**2)
          and is_zero(expected_c05.subs(flat).doit()),
          "F^2 = F'^2 = c05^2 I16 in both frames; c05 = 0 on the flat member")
    entries_nonzero = sum(1 for v in F_boosted if not is_zero(v))
    report("nonzero entries of F'_x5x0 in the frame boosted with b' = 2 c_g",
           entries_nonzero)
    check_record(entries_nonzero > 0, "b' = 2 c_g: the spinor curvature F'_x5x0 is not "
                 "zero", SCOPE, "boosted_frame_curvature_nonzero",
                 "the spinor curvature F'_x5x0 = d_x5 Omega'_x0 - d_x0 Omega'_x5 + "
                 "[Omega'_x5, Omega'_x0] is nonzero for general a4, b4")
    '''),
    md(r"""
    The next cell draws $F_{x_5x_0}$ in both frames as colour maps, at $H = 1$,
    $z = \pi/4$, $x_4 = 0.5$, along the canonical history of the record, with the
    removing rapidity $b = 9(e^{x_4/3} - 1)$ ($b = 1.632$ there). There $c_{05} =
    \frac12\cdot1\cdot2^{-1/12}(\frac19e^{-1/3} - 1) = -0.434$, and $F'_{x_5x_0} =
    c_{05}(\cosh b\,\gamma^{(0)}\gamma^{(5)} - \sinh b\,\gamma^{(4)}\gamma^{(5)})$. The
    cell checks that both matrices have rank 16 (their squares are the same nonzero
    multiple $c_{05}^2$ of the unit matrix) and that the boosted one has this form;
    each map has its own colour scale.
    """),
    code(r'''
    point = {H: 1, x0: sp.pi / 24, x4: sp.Rational(1, 2)}  # z = pi/4, x4 = 0.5


    def at_point(matrix):
        """The numbers of a symbolic matrix at H = 1 on the history, z = pi/4, x4 = 0.5,
        for the removing rapidity b = 9 (e^(x4/3) - 1)."""
        concrete = matrix.subs(rapidity, 9 * (sp.exp(x4 / 3) - 1)).doit()
        concrete = concrete.subs(W(x0), explicit_W).subs(history).doit()
        return np.array(concrete.subs(point).evalf(), dtype=float)


    F_numbers = [("diagonal frame: $F_{x_5x_0}$", at_point(F_diagonal)),
                 ("boosted, $b' = 2c_g$: $F'_{x_5x_0}$", at_point(F_boosted))]
    c05_number = float(expected_c05.subs(W(x0), explicit_W).subs(history).doit()
                       .subs(point))
    b_number = 9 * (np.exp(0.5 / 3) - 1)  # the rapidity at x4 = 0.5
    P05_number, P45_number = (np.array(P, dtype=float) for P in (P05, P45))
    report("c05 at the point and the rapidity there", f"{c05_number:.6f}, {b_number:.6f}")
    ranks = [int(np.linalg.matrix_rank(matrix)) for _, matrix in F_numbers]
    report("rank of F_x5x0 at the point (diagonal, boosted)", ranks)
    squares_ok = all(np.allclose(matrix @ matrix, c05_number**2 * np.eye(16), atol=1e-12)
                     for _, matrix in F_numbers)
    form_ok = np.allclose(F_numbers[1][1], c05_number * (np.cosh(b_number) * P05_number
                                                         - np.sinh(b_number) * P45_number),
                          atol=1e-12)
    check(ranks == [16, 16] and squares_ok and form_ok,
          "on the history: F and F' have rank 16, F^2 = F'^2 = c05^2 1, F' = c05 (cosh b "
          "g0 g5 - sinh b g4 g5)")
    fig, panels = plt.subplots(1, 2, figsize=(10.0, 4.2))
    for panel, (title, matrix) in zip(panels, F_numbers):
        largest = np.abs(matrix).max()  # each panel has its own colour scale
        image = panel.imshow(matrix, cmap="RdBu_r", vmin=-largest, vmax=largest)
        fig.colorbar(image, ax=panel, shrink=0.85, label="entry (units of $H^2$)")
        panel.set_title(title, fontsize=10)
        panel.set_xticks([0, 5, 10, 15])
        panel.set_yticks([0, 5, 10, 15])
        panel.set_xlabel("column")
        panel.grid(False)  # no grid lines over the coloured squares
    panels[0].set_ylabel("row")
    save_figure(fig, "curvature_maps",
                "The spinor curvature $F_{x_5x_0} = \\partial_5\\Omega_0 - "
                "\\partial_0\\Omega_5 + \\Omega_5\\Omega_0 - \\Omega_0\\Omega_5$ as a "
                "$16 \\times 16$ colour map (red positive, blue negative, white zero; "
                "units of $H^2$) at $H = 1$, $z = \\pi/4$, $x_4 = 0.5$ along the history "
                "of the Revision record; each panel has its own colour scale. Left: "
                "diagonal frame, $c_{05}\\gamma^{(0)}\\gamma^{(5)}$ with $c_{05} = "
                "-0.434$. Right: the frame boosted with the removing rapidity $b = "
                "9(e^{x_4/3} - 1) = 1.632$, in which the part $c_g\\gamma^{(0)}$ of the "
                "term $\\gamma'^\\mu\\Omega'_\\mu$ is gone; there the curvature is "
                "$c_{05}(\\cosh b\\,\\gamma^{(0)}\\gamma^{(5)} - \\sinh b\\,\\gamma^{(4)}"
                "\\gamma^{(5)})$. Neither is zero: the curvature is one quarter of the "
                "Riemann tensor contracted with two gammas, so no choice of frame can "
                "make the spin connection vanish. Both matrices have rank 16.")
    '''),
    md(r"""
    ## 13. The spin connection in the energy-momentum tensor

    Although the connection drops out of the symmetrised Lagrangian (section 9), it
    appears in the energy-momentum tensor. For a field that depends only on $x_4$,
    the derivative parts of $K^{x_4}{}_{x_1} = \frac12(\bar\Phi\gamma^{x_4}D_{x_1}\Phi -
    (D_{x_1}\bar\Phi)\gamma^{x_4}\Phi)$ and of $K^{x_4}{}_{x_5}$ vanish and the
    connection parts are $\frac12\bar\Phi\{\gamma^{x_4}, \Omega_{x_1}\}\Phi$ and
    $\frac12\bar\Phi\{\gamma^{x_4}, \Omega_{x_5}\}\Phi$. The next cell checks
    $\frac12\{\gamma^{x_4}, \Omega_{x_1}\} = 0$ (3-space does not depend on $x_0$, so
    $\Omega_{x_1}$ has no part with $H$), $\frac12\{\gamma^{x_4}, \Omega_{x_5}\} =
    \frac12HW\gamma^{(4)}\gamma^{(0)}\gamma^{(5)}$ (the part with $h_4$ cancels) and
    that the bilinear matrix $C\gamma^{(4)}\gamma^{(0)}\gamma^{(5)}$ is not zero.
    """),
    code(r'''
    g4_up = diagonal["gamma"][4]  # gamma^x4 = gamma^(x4), because f_4 = 1
    part_1 = (g4_up * diagonal["Omega"][1] + diagonal["Omega"][1] * g4_up) / 2
    part_5 = (g4_up * diagonal["Omega"][5] + diagonal["Omega"][5] * g4_up) / 2
    target = H * W(x0) * G[4] * G[0] * G[5] / 2
    check_record(all(is_zero(v) for v in part_1)
                 and all(is_zero(v) for v in part_5 - target)
                 and C * G[4] * G[0] * G[5] != sp.zeros(16, 16),
                 "(1/2){gamma^x4, Omega_x1} = 0, (1/2){gamma^x4, Omega_x5} = (1/2) H W "
                 "g4 g0 g5, and C g4 g0 g5 != 0",
                 SCOPE, "spin_connection_in_the_energy_momentum_tensor",
                 "is (1/2) Phibar {gamma^x4, Omega_x1} Phi = 0 (3-space does not depend "
                 "on x0)", "(1/2) H (sin^2 z)^(1/12) Phibar gamma^(x4) gamma^(x0) "
                 "gamma^(x5) Phi (the a4', b4' part cancels exactly)",
                 "C gamma^(x4) gamma^(x0) gamma^(x5) != 0")
    '''),
    md(r"""
    ## 14. The last check

    The last cell checks that the five figure files exist in the folder
    Revision/textbook/figures and prints the number of checks that passed.
    """),
    code(r'''
    for name in ("08c_1_cancel_and_survive.png", "08c_2_pieces_along_history.png",
                 "08c_3_boost_size.png", "08c_4_heat_maps.png", "08c_5_curvature_maps.png"):
        check(output_file(f"{FIGURE_FOLDER}/{name}").is_file(),
              f"the figure file {name} exists")
    all_checks_passed()
    '''),
    md(r"""
    ## 15. What this notebook showed

    - The canonical spin connection of the diagonal frame of the corrected metric has
      10 independent nonzero components, each $a_4'$, $h_4 = b_4'/(2b_4) - a_4'$ or $H$
      times a factor that never vanishes between the degenerate points, so $\Omega_\mu =
      0$ for every $\mu$ only in the formal limit $a_4' = b_4' = 0$, $H = 0$, which is
      not a member of the author's family (PROVED; Revision check
      `nontriviality_Omega_zero_iff_flat`).
    - In the diagonal frame the term of the field equation is $\gamma^\mu\Omega_\mu =
      G = c_g\gamma^{(0)} + v_g\gamma^{(4)}$ with $c_g = \frac32He^{a_4}b_4^{-1/2}$ and
      $v_g = b_4'/b_4 - a_4'/2$, for all functions $a_4$ and $b_4$ (PROVED, exact): the
      pieces $\pm\frac12a_4'$ of 3-space and of the extra times cancel, the hidden
      direction and the three extra times share the rate $h_4$ ($4\cdot\frac12h_4 +
      3\cdot\frac12a_4' = v_g$), and only the three extra times give $\gamma^{(0)}$
      pieces, $\frac12He^{a_4}b_4^{-1/2}$ each; equivalently it is the half-density term
      $\frac{1}{2\sqrt{|g|}}\partial_\mu(\sqrt{|g|}\gamma^\mu)$, and $\{\gamma^\mu,
      \Omega_\mu\} = 0$ for each $\mu$, so the connection drops out of the symmetrised
      Lagrangian. Because $GG = (c_g^2 - v_g^2)I_{16}$, $H^2(\frac94e^{2Hx_4/3} -
      \frac{25}{36})I_{16}$ on the history, the term $G\Psi$ is not zero for any field
      $\Psi \neq 0$ wherever $c_g^2 \neq v_g^2$ (PROVED).
    - The term sees the deflating hidden block (its $\gamma^{(0)}$ coefficient is
      $\frac32H$ times the inverse scale factor $e^{a_4}b_4^{-1/2}$ of the block). The
      metric is flat for $a_4 = 0$, $b_4 = H^2x_4^2$, where the term is still nonzero in
      the diagonal frame (a pure frame effect), and curved on the history of the record
      ($R^{x_1}{}_{x_1} = \frac53H^2$) (PROVED).
    - The value $G$ belongs to the diagonal frame: in the frame boosted in the
      $(x_4, x_0)$ plane with a rapidity $b(x_4)$ the term is $(c_g - \frac{b'}{2})
      (\cosh b\,\gamma^{(0)} - \sinh b\,\gamma^{(4)}) + v_g(\cosh b\,\gamma^{(4)} -
      \sinh b\,\gamma^{(0)})$; for $b' = 2c_g$ its part $c_g\gamma^{(0)}$ is gone, and no
      boost removes its part $v_g$ (PROVED). So "the field equation contains the
      gravitational term $c_g\gamma^{(0)}$" is a statement about one frame and one
      choice of field variables, not about the field equation as such.
    - What no frame removes where the metric is curved: the spin connection itself. Its
      curvature equals $\frac14 R_{\rho\sigma\mu\nu}\gamma^\rho\gamma^\sigma$ (checked in
      two frames for $(\mu, \nu) = (x_5, x_0)$, where $F^2 = F'^2 =
      \frac14\cot^2 z\,W^2(h_4^2e^{-2a_4}b_4 - H^2)^2I_{16}$), and the Riemann tensor is
      not zero on the history (PROVED). Together with the frame factors in every
      derivative term, this is the frame-independent content of the non-triviality
      statements [1] and [2].
    - The connection also enters the energy-momentum tensor (PROVED for the component
      $K^{x_4}{}_{x_5}$ of a field that depends only on $x_4$; the component
      $K^{x_4}{}_{x_1}$ gets no connection part).
    """),
]

if __name__ == "__main__":
    raise SystemExit(run_builder(__file__))
