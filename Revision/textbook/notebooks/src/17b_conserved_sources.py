#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
"""Builder of Notebook 17b, "Conserved but not admissible: the conservation laws and the
source conditions" (textbook "Universes in Pairs", chapter 17: the a4 equations with the
Kohn-Sham source, a prescribed background).

The notebook Revision/textbook/notebooks/17b_conserved_sources.ipynb is BUILT from this
file by Revision/textbook/tools/nbkit.py (never edit the .ipynb by hand):

    python Revision/textbook/tools/nbkit.py build \
        Revision/textbook/notebooks/src/17b_conserved_sources.py --date YYYY-MM-DD
    python Revision/textbook/tools/nbkit.py check \
        Revision/textbook/notebooks/src/17b_conserved_sources.py

It checks that the Kohn-Sham source rests on the author's eight real 16 x 16 gamma
matrices (Revision/algebra/gammas.json, the file the Rust solver read), derives with sympy
the covariant divergence of a source in the author's metric (x8 chart and hidden
coordinate y) and compares it with the a4 record and the Kohn-Sham theory record, proves
that for a conserved source the violation of C2 is p8'/(3H) and that the time derivative
of the constraint is 3 a4' times the evolution equation, and tests these identities on
the 75 committed Kohn-Sham ground states (pointwise with fourth-order differences and a
convergence study, integrated with the brane and tip values, and along the history with
Simpson's rule).  Five figures.  Every number in a caption is computed by the notebook.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools"))
from nbkit import code, md, run_builder  # noqa: E402

FIGURES = [
    "17b_1_eight_gammas",
    "17b_2_slope_identity",
    "17b_3_difference_order",
    "17b_4_brane_and_mean",
    "17b_5_energy_exchange",
]

FACTS = {
    "id": "17b",
    "name": "17b_conserved_sources",
    "title": "Conserved but not admissible: the conservation laws and the source "
             "conditions",
    "purpose": (
        "It checks that the Kohn-Sham source of chapter 17 rests on the eight real "
        "16 x 16 gamma matrices of the author (the very file the Rust solver read), "
        "derives with sympy the conservation law of a source in the author's metric, "
        "in the coordinate x8 and in the hidden coordinate y, and compares it with the "
        "Revision records. It proves that for a conserved source the violation "
        "p3 + p_t - 2 p8 of condition C2 equals the slope of p8 along y divided by 3H, "
        "and that the time derivative of the constraint is 3 a4' times the evolution "
        "equation, so that the linear member needs p3 = p_t. It then tests these "
        "identities on the 75 recorded Kohn-Sham ground states: point by point with "
        "fourth-order differences and a convergence study, integrated with the brane "
        "and tip values, and along the deflating history with Simpson's rule. The "
        "Kohn-Sham states obey every conservation law and still fail the source "
        "conditions. Five teaching plots."
    ),
    "records": [
        ["Revision/algebra/gammas.json",
         "the author's eight real 16 x 16 gamma matrices"],
        ["Revision/algebra/reports/python-algebra.json",
         "the checks of the gamma matrices: reality and the Clifford relation"],
        ["Revision/field_equations_a4/a4-equations.json",
         "the a4 equations: Lovelock components, conservation law, evolution factor F"],
        ["Revision/field_equations_a4/reports/python-a4-report.json",
         "the sympy checks of the a4 record that the notebook reproduces"],
        ["Revision/field_equations_a4/reports/wolfram-a4-report.json",
         "the Wolfram checks of the a4 record that the notebook reproduces"],
        ["Revision/field_equations_a4/reports/ks-source-conditions.json",
         "the record on the Kohn-Sham source conditions (the integrated ratio of C2)"],
        ["Revision/kohn_sham/ks-theory.json",
         "the Kohn-Sham theory record: the conservation law along y and the energy "
         "change along the history"],
        ["Revision/kohn_sham/reports/ks-theory-python.json",
         "the sympy checks of the Kohn-Sham theory: hidden coordinate, volume, "
         "conservation"],
        ["Revision/kohn_sham/reports/ks-rust-solver.json",
         "the checks of the Rust solver: its gamma input and its conservation checks"],
        ["Revision/kohn_sham/results/parameters.json",
         "the parameters of the Kohn-Sham computations (H, tip cutoff, Vol_7)"],
        ["Revision/kohn_sham/results/ground/profiles",
         "the profiles of the 75 Kohn-Sham ground states along the hidden coordinate"],
        ["Revision/kohn_sham/results/ground/emt-integrals.csv",
         "the integrals, brane values and tip values of every ground state"],
        ["Revision/kohn_sham/results/adiabatic/history.json",
         "the Fermi-level crossings along the history (there are none)"],
    ],
    "packages": ["numpy", "sympy", "matplotlib"],
    "needs_rust": [],
    "expected_seconds": 20,
    "timeout_seconds": 300,
    "files_written": ["Revision/textbook/figures/17b.captions.json"]
    + [f"Revision/textbook/figures/{name}.png" for name in FIGURES],
    "final_lines": [
        "PASS every figure file of this notebook exists",
        "ALL 20 CHECKS PASSED (notebook 17b)",
    ],
    "troubleshooting": [
        ["\"FileNotFoundError\" naming gammas.json, a report or a profile file",
         "the notebook reads the Revision records of the repository. Run it inside the "
         "folder Revision/textbook/notebooks of a complete copy of the repository made "
         "with git clone, not on a copy of the notebook file alone."],
        ["the check of the sha256 fingerprint of gammas.json fails",
         "the file was changed, for example by an editor or a tool that converted its "
         "line endings. Restore it with the command below, run in the repository "
         "folder.",
         ["git checkout HEAD Revision/algebra/gammas.json"]],
    ],
}

CELLS = [
    md(r"""
    ## 1. What this notebook computes

    Notebook 17a showed that no recorded Kohn-Sham state of dirac16complex is an
    admissible source of the author's metric: the states fail the three source
    conditions C1, C2, C3 of the $a_4$ equations. This notebook asks WHY, and the
    answer is the **conservation law** of energy and momentum. Every source of the
    field equations must be conserved; the Kohn-Sham states are conserved; and for a
    conserved source the conditions take a very simple form. The notebook

    - checks that the Kohn-Sham source is built on the author's eight REAL
      $16 \times 16$ gamma matrices (the very file that the Rust solver read);
    - derives with sympy the conservation law of a source in the author's metric, in
      the coordinate $x_8$ and in the hidden coordinate $y$, and compares it with the
      Revision records;
    - PROVES that for a conserved source the violation of C2 is the slope of $p_8$:
      $p_3 + p_t - 2p_8 = p_8'(y)/(3H)$; so C2 holds exactly where $p_8$ is flat;
    - PROVES that the time derivative of the constraint equation is $3a_4'$ times the
      evolution equation, so that the linear member $a_4 = AHx_4$ needs $p_3 = p_t$;
    - tests these identities on the 75 recorded Kohn-Sham ground states: point by
      point (with a convergence study of the differences), integrated over the
      hidden direction, and along the deflating history;
    - draws five teaching plots. It takes about twenty seconds.
    """),
    md(r"""
    ## 3. The words used in this notebook

    - **Coordinates** (the author's names): $x_1, x_2, x_3$ = ordinary 3-space,
      which inflates (scale factor $e^{a_4}\sin^{1/6}z$); $x_4$ = the time;
      $x_5, x_6, x_7$ = the three **extra times**, which **deflate exponentially**
      (scale factor $e^{-a_4}\sin^{1/6}z$, with $a_4$ increasing); $x_8$ = the hidden
      space direction, $z = 6Hx_8$ between $0$ and $\pi/2$.
    - **Hidden coordinate** $y = \ln(\sin z)/(6H)$: another way to number the points
      of the hidden direction; $y = 0$ is the **brane** ($z = \pi/2$), $y = -3$ the
      **tip cutoff** of the computations. A **chart** is a choice of coordinates.
    - **Gamma matrices** $\gamma^{(x_1)}, \dots, \gamma^{(x_8)}$: eight square tables
      of numbers with $\gamma^a\gamma^b + \gamma^b\gamma^a = 2\eta^{ab}\,1$ (the
      **Clifford relation**), $\eta = \mathrm{diag}(+1,+1,+1,-1,-1,-1,-1,+1)$. The
      author's are real $16 \times 16$ **signed permutation matrices**: each row and
      each column holds exactly one nonzero entry, $+1$ or $-1$.
    - **sha256 fingerprint**: a 64-digit code computed from the bytes of a file; two
      files with the same fingerprint are, for all practical purposes, identical.
    - **Energy-momentum tensor** $T^\mu{}_\nu$ (the **source**): here
      $T = \mathrm{diag}(p_3, p_3, p_3, -\rho, p_t, p_t, p_t, p_8)$ in the order
      $x_1, \dots, x_8$, with energy density $\rho$ and pressures $p_3$ (3-space),
      $p_t$ (extra times), $p_8$ (hidden direction); possibly mixed entries $q_{48}$
      (row $x_4$, column $x_8$) and $q_{84}$.
    - **Christoffel symbols** $\Gamma^\lambda{}_{\mu\nu} = \tfrac12 g^{\lambda\kappa}
      (\partial_\mu g_{\kappa\nu} + \partial_\nu g_{\kappa\mu} -
      \partial_\kappa g_{\mu\nu})$: numbers built from the first derivatives of the
      metric that say how the coordinate directions turn from point to point.
    - **Covariant divergence** $\nabla_\mu T^\mu{}_\nu = \partial_\mu T^\mu{}_\nu +
      \Gamma^\mu{}_{\mu\lambda}T^\lambda{}_\nu - \Gamma^\lambda{}_{\mu\nu}
      T^\mu{}_\lambda$ (sum over repeated indices): the curved-space version of "what
      flows out of a small box". The **conservation law** is
      $\nabla_\mu T^\mu{}_\nu = 0$ for every $\nu$.
    - **Bianchi identity**: the left-hand sides of the Einstein-Lovelock equations
      have zero covariant divergence for EVERY metric; hence every source of the
      equations must be conserved.
    - **Source conditions** (from the $a_4$ equations): **C1** no component of the
      source depends on $x_8$ and $q_{48} = q_{84} = 0$; **C2** $p_3 + p_t = 2p_8$;
      **C3** for the linear member $a_4 = AHx_4 + a_0$: $p_3 = p_t = p_8$ and a
      constant $\rho$. **Admissible source**: one that meets them.
    - **Constraint** (the $x_4$ equation, no $a_4''$) and **evolution equation**
      ($a_4''\,F(a_4') = \kappa(p_3 - p_t)$) of the $a_4$ equations.
    - **Finite difference** of fourth order: the slope of a tabulated function from
      five neighbouring values,
      $f'(y) \approx [-f(y+2h) + 8f(y+h) - 8f(y-h) + f(y-2h)]/(12h)$; its error falls
      like $h^4$ when the step $h$ shrinks (**order of accuracy** 4).
    - **Simpson's rule**: the integral of a function over $[a, a+2h]$ is about
      $(h/3)[f(a) + 4f(a+h) + f(a+2h)]$; error like $h^4$.
    - **Weighted mean**: $\int e^{6Hy}p_8\,dy / \int e^{6Hy}dy$, the average of
      $p_8$ over the proper volume.
    - **Kohn-Sham state**, **slice** $a_{4,0}$, **history** $a_4 = AHx_4$ with
      $A = 1$, **prescribed background**, **test field**, **back-reaction**: as in
      Notebook 17a; a state name such as `N136_lamp2_a20` means $N = 136$,
      $\lambda = +\lambda_2$, $a_{4,0} = 2.0$.
    - **Status labels**: PROVED (exact), COMPUTED (numerical, with its measured
      error), ASSUMED, OPEN. Units: $H = 1$, $m = 1$.
    """),
    md(r"""
    ## 4. The physical and mathematical situation

    The field equations of gravity, $\sum_k\alpha_kE_{(k)}{}^\mu{}_\nu +
    \Lambda\delta^\mu_\nu = \kappa T^\mu{}_\nu$, have a left-hand side whose covariant
    divergence vanishes identically (the Bianchi identity; the Revision record checks
    it for all three Lovelock tensors of the author's metric). Taking the divergence
    of both sides gives $\kappa\nabla_\mu T^\mu{}_\nu = 0$: a source must be
    conserved. Conservation is therefore NECESSARY. This notebook shows that it is not
    SUFFICIENT, and that it explains the failure of the Kohn-Sham states.

    The Kohn-Sham states are computed in the prescribed background $a_4 = Hx_4$ (the
    extra times deflate as $e^{-a_4}$, 3-space inflates as $e^{a_4}$). A field that
    solves its own field equation in a given metric always has a conserved
    energy-momentum tensor; the Kohn-Sham theory record proves this for the
    self-consistent states, and the Rust solver checks it numerically. We will see:

    1. in the hidden direction, conservation reads
       $p_8' + 6Hp_8 = 3H(p_3 + p_t)$ (the prime is $d/dy$); hence the violation of
       C2 is $V = p_3 + p_t - 2p_8 = p_8'/(3H)$. For a conserved source, C2 and
       "$p_8$ does not depend on $x_8$" (part of C1) are the SAME condition. The
       Kohn-Sham $p_8$ changes by orders of magnitude along $y$, so C2 must fail;
    2. in the time direction, conservation reads $\rho' = -3a_4'(p_3 - p_t)$ (the
       prime is $d/dx_4$): energy flows between the source and the expanding and
       deflating directions unless $p_3 = p_t$. The Kohn-Sham gas has
       $p_3 > 0 = p_t$ (at $\lambda = 0$), so its energy must change along the
       history, which C3 forbids.
    """),
    md(r"""
    ## 5. The Revision records and the helpers that read them

    The next cell imports the packages and names the Revision records used below. It
    defines three helpers: `read_json` reads a JSON file of the repository,
    `record_entry` finds a check by its name in a Revision report, and `reproduces` is
    a check that passes only when this notebook's own result holds AND the named
    checks of the report have the verdict PASS. Then it counts the checks of the six
    reports and requires that all of them passed.
    """),
    code(r'''
    import csv  # reads tables stored as CSV files (comma-separated values)
    import hashlib  # computes the sha256 fingerprint of a file

    import numpy as np  # arrays of numbers
    import sympy as sp  # exact algebra with symbols

    GAMMAS = "Revision/algebra/gammas.json"  # the eight real 16 x 16 gammas
    ALGEBRA = "Revision/algebra/reports/python-algebra.json"  # their checks
    EQUATIONS = "Revision/field_equations_a4/a4-equations.json"  # the a4 equations
    PY_A4 = "Revision/field_equations_a4/reports/python-a4-report.json"  # sympy
    WL_A4 = "Revision/field_equations_a4/reports/wolfram-a4-report.json"  # Wolfram
    SOURCE_REPORT = "Revision/field_equations_a4/reports/ks-source-conditions.json"
    KS_THEORY = "Revision/kohn_sham/ks-theory.json"  # the Kohn-Sham theory record
    KS_PY = "Revision/kohn_sham/reports/ks-theory-python.json"  # its sympy checks
    KS_RUST = "Revision/kohn_sham/reports/ks-rust-solver.json"  # the solver checks
    GROUND = "Revision/kohn_sham/results/ground"  # the 75 Kohn-Sham ground states


    def read_json(relative):
        """Read a JSON file of the repository (a Revision record)."""
        return json.loads(repository_file(relative).read_text(encoding="utf-8"))


    def record_entry(report_file, name):
        """The entry {name, verdict, detail} of a check of a report, None if absent."""
        for entry in read_json(report_file)["checks"]:
            if entry["name"] == name:
                return entry
        return None


    def reproduces(condition, name, report_file, record_names):
        """A check that also requires the named checks of the report to be PASS."""
        found = all((record_entry(report_file, n) or {}).get("verdict", "").upper()
                    == "PASS" for n in record_names)  # some reports write "pass"
        check(condition and found, name,
              record=f"{report_file}, check {', '.join(record_names)}")


    REPORTS = [ALGEBRA, PY_A4, WL_A4, SOURCE_REPORT, KS_PY, KS_RUST]
    every_pass = True
    for report_file in REPORTS:
        verdicts = [entry["verdict"].upper()
                    for entry in read_json(report_file)["checks"]]
        passed = verdicts.count("PASS")  # how many checks of this report passed
        every_pass = every_pass and passed == len(verdicts)
        report(report_file.split("/")[-1], f"{passed} of {len(verdicts)} checks PASS")
    check(every_pass, "every check of the six Revision reports used here is PASS")
    '''),
    md(r"""
    ## 6. The eight real $16 \times 16$ gamma matrices behind the Kohn-Sham source

    dirac16complex is a 16-component spinor field, and its field equation, its
    Lagrangian and its energy-momentum tensor are written with the author's eight
    real $16 \times 16$ gamma matrices. The Kohn-Sham solver reduces the 16-component
    equation to $2 \times 2$ blocks; the solver's own check `block_reduction_numeric`
    confirms that its blocks are exactly the 16-component Hamiltonian written in
    another basis. The next cell reads the matrices from the Revision record
    `gammas.json` and checks: there are eight; each is $16 \times 16$; every entry is
    a JSON integer (so the matrices are REAL) equal to $-1$, $0$ or $+1$; each is a
    signed permutation matrix.
    """),
    code(r'''
    gamma_record = read_json(GAMMAS)
    entries = [v for matrix in gamma_record["gamma"] for row in matrix for v in row]
    real_integers = all(isinstance(v, int) for v in entries)  # no complex entries
    gamma = [np.array(matrix, dtype=float) for matrix in gamma_record["gamma"]]
    eta = np.array(gamma_record["eta"], dtype=float)  # +1 or -1 for x1, ..., x8
    shapes = sorted({matrix.shape for matrix in gamma})  # should be one shape only
    values = sorted({int(v) for v in entries})  # the entries that occur
    one_per_line = all(np.all(np.count_nonzero(matrix, axis=0) == 1)
                       and np.all(np.count_nonzero(matrix, axis=1) == 1)
                       for matrix in gamma)  # one nonzero entry per row and column
    report("number of gamma matrices", len(gamma))
    report("their shapes", shapes)
    report("the entries that occur", values)
    report("eta in the order x1, ..., x8", [int(v) for v in eta])
    reproduces(len(gamma) == 8 and shapes == [(16, 16)] and real_integers
               and values == [-1, 0, 1] and one_per_line,
               "eight real 16 x 16 signed permutation matrices",
               ALGEBRA, ["reality_signed_permutations"])
    '''),
    md(r"""
    The next cell checks the Clifford relation
    $\gamma^a\gamma^b + \gamma^b\gamma^a = 2\eta^{ab}\,1$ for all $8 \times 8 = 64$
    ordered pairs $(a, b)$ (the products of integer matrices are exact in floating
    point), and it computes the sha256 fingerprint of the file `gammas.json`. The Rust
    solver printed the first 16 digits of the fingerprint of the file it read into
    its check `gamma_fixture_numeric`; equal digits show that the Kohn-Sham states
    were computed with exactly these matrices.
    """),
    code(r'''
    identity16 = np.eye(16)  # the 16 x 16 unit matrix
    deviation = 0.0  # the largest deviation from the Clifford relation
    for a in range(8):
        for b in range(8):
            anticommutator = gamma[a] @ gamma[b] + gamma[b] @ gamma[a]
            target = 2.0 * eta[a] * identity16 if a == b else 0.0 * identity16
            deviation = max(deviation, float(np.max(np.abs(anticommutator - target))))
    report("largest deviation from the Clifford relation, 64 pairs", deviation)
    reproduces(deviation == 0.0, "the Clifford relation holds exactly for all 64 pairs",
               ALGEBRA, ["clifford_relation"])
    fingerprint = hashlib.sha256(repository_file(GAMMAS).read_bytes()).hexdigest()
    report("sha256 of gammas.json, first 16 digits", fingerprint[:16])
    solver_detail = record_entry(KS_RUST, "gamma_fixture_numeric")["detail"]
    reproduces(f"(sha256 {fingerprint[:16]})" in solver_detail,
               "the Rust Kohn-Sham solver read exactly this file of gammas",
               KS_RUST, ["gamma_fixture_numeric", "block_reduction_numeric"])
    '''),
    md(r"""
    The next cell draws the eight matrices as coloured tables (heat maps): red is
    $+1$, blue is $-1$, white is $0$. The title of each panel says which coordinate
    the matrix belongs to and the sign of its square, $(\gamma^a)^2 = \eta^{aa}\,1$.
    """),
    code(r'''
    LABELS = ["x_1", "x_2", "x_3", "x_4", "x_5", "x_6", "x_7", "x_8"]
    fig, axes = plt.subplots(2, 4, figsize=(9.6, 5.4))
    for a, ax in enumerate(axes.flat):
        image = ax.imshow(gamma[a], cmap="RdBu_r", vmin=-1.0, vmax=1.0)
        sign = "+1" if eta[a] > 0 else "-1"  # the square of this gamma matrix
        ax.set_title(f"$\\gamma^{{({LABELS[a]})}}$, square ${sign}$", fontsize=10)
        ax.set_xticks([0, 15], ["1", "16"])  # column numbers 1 and 16
        ax.set_yticks([0, 15], ["1", "16"])  # row numbers 1 and 16
    fig.colorbar(image, ax=axes, shrink=0.75, label="matrix entry")
    nonzero_count = int(sum(np.count_nonzero(matrix) for matrix in gamma))
    save_figure(fig, "eight_gammas",
                "The author's eight real $16 \\times 16$ gamma matrices "
                "$\\gamma^{(x_1)}$ to $\\gamma^{(x_8)}$ as heat maps (rows 1 to 16 down, "
                "columns 1 to 16 across; red $+1$, blue $-1$, white $0$). Each row and "
                "each column holds exactly one nonzero entry, so the eight matrices "
                f"have {nonzero_count} nonzero entries in all; the squares are $+1$ "
                "for the space-like directions $x_1, x_2, x_3, x_8$ and $-1$ for the "
                "time $x_4$ and the deflating extra times $x_5, x_6, x_7$. These are "
                "the matrices with which the Kohn-Sham source of this chapter was "
                "computed.")
    '''),
    md(r"""
    ## 7. The hidden coordinate $y$

    The author's metric has $g_{88} = \cot^2 z$ with $z = 6Hx_8$, and the warp factor
    $\sin^{1/3}z$ in front of the six directions $x_1, x_2, x_3, x_5, x_6, x_7$. The
    Kohn-Sham computations use $y = \ln(\sin z)/(6H)$ instead of $x_8$. The next cell
    derives, step by step with sympy:

    1. $dy/dx_8 = \cot z$ (the chain rule: $d\ln(\sin z)/dz = \cot z$ and
       $dz/dx_8 = 6H$);
    2. $g_{yy} = g_{88}\,(dx_8/dy)^2 = \cot^2 z/\cot^2 z = 1$: $y$ measures proper
       length along the hidden direction;
    3. $\sin z = e^{6Hy}$, so the warp factor is $\sin^{1/3}z = e^{2Hy}$;
    4. $\sqrt{|\det g|} = \cos z$ in the $x_8$ chart and $e^{6Hy}$ in the $y$ chart
       (the factors $e^{\pm 2a_4}$ of 3-space and of the extra times cancel in the
       determinant: the 7-volume does not change while 3-space inflates and the
       extra times deflate).

    To let sympy simplify powers safely, $\sin z$ and $\cos z$ are written as
    positive symbols $s$ and $c$ (both are positive for $0 < z < \pi/2$).
    """),
    code(r'''
    H = sp.symbols("H", positive=True)  # the constant H of the metric
    X8 = sp.symbols("x8", positive=True)  # the author's hidden coordinate
    z = 6 * H * X8  # the angle z = 6 H x8
    y_of_x8 = sp.log(sp.sin(z)) / (6 * H)  # the hidden coordinate y
    dy_dx8 = sp.simplify(sp.diff(y_of_x8, X8))  # chain rule
    g_yy = sp.simplify(sp.cot(z) ** 2 / dy_dx8 ** 2)  # g88 times (dx8/dy)^2
    say(f"dy/dx8 = {dy_dx8},  g_yy = {g_yy}")
    s, c, a4_value = sp.symbols("s c a4", positive=True)  # s = sin z, c = cos z
    y_of_s = sp.log(s) / (6 * H)  # y written with s = sin z
    warp = sp.simplify(sp.exp(2 * H * y_of_s))  # e^{2Hy} in terms of s
    say(f"e^(2Hy) = {warp}  (the warp factor sin^(1/3) z)")
    factors = ([sp.exp(2 * a4_value) * s ** sp.Rational(1, 3)] * 3 + [1]
               + [sp.exp(-2 * a4_value) * s ** sp.Rational(1, 3)] * 3)  # |g_ii|, i < 8
    root_x8 = sp.simplify(sp.sqrt(sp.prod(factors) * (c / s) ** 2))  # g88 = cot^2 z
    root_y = sp.simplify(sp.sqrt(sp.prod(factors) * 1))  # g_yy = 1
    say(f"sqrt|det g| in the x8 chart = {root_x8};  in the y chart = {root_y}")
    reproduces(sp.simplify(dy_dx8 - sp.cot(z)) == 0 and g_yy == 1
               and warp == s ** sp.Rational(1, 3) and root_x8 == c and root_y == s,
               "dy/dx8 = cot z, g_yy = 1, sin^(1/3) z = e^(2Hy), sqrt|g| = cos z or e^(6Hy)",
               KS_PY, ["geometry_hidden_coordinate", "geometry_sqrt_det",
                       "geometry_warped_form"])
    '''),
    md(r"""
    ## 8. The conservation law of a source in the author's metric

    The next cell defines two helpers that work for any diagonal metric:
    `christoffel` computes all $8 \times 8 \times 8 = 512$ Christoffel symbols with
    the formula of section 3, and `divergence` computes the eight components
    $\nabla_\mu T^\mu{}_\nu$, $\nu = 1, \dots, 8$, of the covariant divergence of a
    table $T^\mu{}_\nu$ (stored as `T[mu, nu]`). It then builds the author's metric in
    the $x_8$ chart with a general function $a_4(x_4)$, and the most general source
    the $a_4$ record allows: $\rho, p_3, p_t, p_8, q_{48}, q_{84}$, each a function of
    $x_4$ and $x_8$. Finally it prints the eight components of the divergence, written
    in the record's notation: `ad1` is $a_4'$, `d4rho` is $\partial\rho/\partial x_4$,
    `d8p8` is $\partial p_8/\partial x_8$, and so on.
    """),
    code(r'''
    def christoffel(metric, chart):
        """All Gamma^l_{mn} of a diagonal metric, as a nested list [l][m][n]."""
        inverse = [1 / metric[k, k] for k in range(8)]  # diagonal: g^kk = 1 / g_kk
        return [[[sp.simplify(inverse[l] * (sp.diff(metric[l, m], chart[n])
                                            + sp.diff(metric[l, n], chart[m])
                                            - sp.diff(metric[m, n], chart[l])) / 2)
                  for n in range(8)] for m in range(8)] for l in range(8)]


    def divergence(T, metric, chart):
        """The 8 components nabla_mu T^mu_nu of a table T[mu, nu] = T^mu_nu."""
        G = christoffel(metric, chart)
        result = []
        for nu in range(8):
            total = 0
            for mu in range(8):
                total += sp.diff(T[mu, nu], chart[mu])  # d_mu T^mu_nu
                for lam in range(8):
                    total += G[mu][mu][lam] * T[lam, nu]  # Gamma^mu_{mu lam} T^lam_nu
                    total -= G[lam][mu][nu] * T[mu, lam]  # Gamma^lam_{mu nu} T^mu_lam
            result.append(sp.simplify(total))
        return result


    coords = sp.symbols("x1:9", real=True)  # x1, ..., x8 (the x8 chart)
    x4, x8 = coords[3], coords[7]
    a4 = sp.Function("a4")(x4)  # the free function of the metric
    zz = 6 * H * x8  # z = 6 H x8
    wz = sp.sin(zz) ** sp.Rational(1, 3)  # the warp factor sin^(1/3) z
    metric_x8 = sp.diag(*([sp.exp(2 * a4) * wz] * 3 + [-1]
                          + [-sp.exp(-2 * a4) * wz] * 3 + [sp.cot(zz) ** 2]))
    names = ("rho", "p3", "pt", "p8", "q48", "q84")
    rho, p3, pt, p8, q48, q84 = (sp.Function(n)(x4, x8) for n in names)
    T_x8 = sp.diag(p3, p3, p3, -rho, pt, pt, pt, p8)  # the diagonal part
    T_x8[3, 7] = q48  # T^x4_x8
    T_x8[7, 3] = q84  # T^x8_x4
    div_x8 = divergence(T_x8, metric_x8, coords)
    notation = {sp.Derivative(f, v): sp.Symbol(f"d{v.name[1]}{f.func.__name__}")
                for f in (rho, p3, pt, p8, q48, q84) for v in (x4, x8)}
    notation[sp.Derivative(a4, x4)] = sp.Symbol("ad1")  # a4'


    def in_record_notation(expression):
        """Write derivatives as d4rho, d8p8, ... and functions as plain symbols."""
        expression = expression.subs(notation)
        return expression.subs({f: sp.Symbol(f.func.__name__)
                                for f in (rho, p3, pt, p8, q48, q84)})


    for nu, component in enumerate(div_x8):
        say(f"nabla_mu T^mu_x{nu + 1} = {in_record_notation(component)}")
    '''),
    md(r"""
    Six of the eight components vanish identically. The two others are the
    conservation laws in the time direction $x_4$ and in the hidden direction $x_8$.
    The next cell reads the record's two equations `conservation_x4` and
    `conservation_x8` (Wolfram Language text; `cc` stands for $\cot z$) and checks
    that they equal ours (the difference is rewritten with cosines and simplified to
    zero; one term needs the identity $\tan z + \cot z = 2/\sin 2z$).
    """),
    code(r'''
    equations = read_json(EQUATIONS)
    RECORD_NAMES = {"ad1": sp.Derivative(a4, x4), "H": H, "cc": sp.cot(zz),
                    "rho": rho, "p3": p3, "pt": pt, "p8": p8, "q48": q48, "q84": q84}
    RECORD_NAMES.update({str(symbol): derivative
                         for derivative, symbol in notation.items()})


    def record_equation(text):
        """An equation left == right of the record as the expression left - right."""
        left, right = text.replace("^", "**").split("==")
        return (sp.sympify(left, locals=RECORD_NAMES)
                - sp.sympify(right, locals=RECORD_NAMES))


    same = []
    for key, nu in (("conservation_x4", 3), ("conservation_x8", 7)):
        recorded = record_equation(equations["generalSource"][key]["input"])
        difference = sp.simplify((div_x8[nu] - recorded).rewrite(sp.cos))
        same.append(difference == 0)
        say(f"{key}: ours minus the record = {difference}")
    zero_components = all(div_x8[nu] == 0 for nu in (0, 1, 2, 4, 5, 6))
    reproduces(all(same) and zero_components,
               "our divergence equals the record: x4 and x8 laws, six zero components",
               PY_A4, ["conservation_components", "json_conservation"])
    '''),
    md(r"""
    ## 9. The conservation law in the coordinate $y$, and what it does to C2

    The Kohn-Sham states have $q_{48} = q_{84} = 0$ (their mixed component vanishes
    for every eigen-orbital) and depend on $y$. In the $y$ chart the author's metric
    is, by section 7,
    $e^{2Hy}[e^{2a_4}(dx_1^2 + dx_2^2 + dx_3^2) - e^{-2a_4}(dx_5^2 + dx_6^2 +
    dx_7^2)] - dx_4^2 + dy^2$. The next cell computes the covariant divergence of a
    diagonal source $T(x_4, y)$ in this chart with the same helper and checks the two
    surviving components against the formulas

    $$\nabla_\mu T^\mu{}_{x_4} = -\partial_4\rho - 3a_4'(p_3 - p_t), \qquad
    \nabla_\mu T^\mu{}_y = p_8' + 6Hp_8 - 3H(p_3 + p_t)$$

    of the Kohn-Sham theory record (the prime on $p_8$ is $\partial/\partial y$).
    """),
    code(r'''
    yc = sp.symbols("y", real=True)  # the hidden coordinate y
    chart_y = list(coords[:7]) + [yc]  # x1, ..., x7, y
    wy = sp.exp(2 * H * yc)  # the warp factor e^{2Hy} = sin^(1/3) z
    metric_y = sp.diag(*([sp.exp(2 * a4) * wy] * 3 + [-1]
                         + [-sp.exp(-2 * a4) * wy] * 3 + [1]))
    RHO, P3, PT, P8 = (sp.Function(n)(x4, yc) for n in ("rho", "p3", "pt", "p8"))
    T_y = sp.diag(P3, P3, P3, -RHO, PT, PT, PT, P8)  # a diagonal source T(x4, y)
    div_y = divergence(T_y, metric_y, chart_y)
    law_x4 = -sp.diff(RHO, x4) - 3 * sp.diff(a4, x4) * (P3 - PT)
    law_y = sp.diff(P8, yc) + 6 * H * P8 - 3 * H * (P3 + PT)
    say(f"nabla_mu T^mu_x4 = {div_y[3]}")
    say(f"nabla_mu T^mu_y = {div_y[7]}")
    others_zero = all(div_y[nu] == 0 for nu in (0, 1, 2, 4, 5, 6))
    theory = read_json(KS_THEORY)["emt"]  # the energy-momentum part of the record
    say("ks-theory.json, emt.conservationY: " + theory["conservationY"])
    reproduces(sp.simplify(div_y[3] - law_x4) == 0 and sp.simplify(div_y[7] - law_y) == 0
               and others_zero
               and theory["conservationY"].startswith("p8' + 6H p8 = 3H (p3 + p_t)"),
               "in the y chart: the x4 law and p8' + 6H p8 = 3H (p3 + p_t)",
               KS_PY, ["emt_y_conservation_selfconsistent", "emt_x4_component"])
    '''),
    md(r"""
    Now the key step. Solve the $y$ law for $p_3$:
    $p_3 = (p_8' + 6Hp_8)/(3H) - p_t$. Put this into the violation of C2:

    $$V = p_3 + p_t - 2p_8 = \frac{p_8' + 6Hp_8}{3H} - 2p_8 = \frac{p_8'}{3H}.$$

    The first equality is the definition of $V$; the second replaces $p_3 + p_t$ by
    its value from the conservation law; the third cancels $6Hp_8/(3H) = 2p_8$
    against $-2p_8$. So, for EVERY conserved diagonal source: **C2 holds at a point
    exactly when $p_8$ is flat there.** C2 is not an extra demand on a conserved
    source; it is the $p_8$ part of C1. The next cell repeats the algebra with
    sympy.
    """),
    code(r'''
    p3_from_law = sp.solve(sp.Eq(law_y, 0), P3)[0]  # p3 from the y conservation law
    V = P3 + PT - 2 * P8  # the violation of C2
    V_conserved = sp.simplify(V.subs(P3, p3_from_law))
    say(f"p3 from the conservation law: {p3_from_law}")
    say(f"V = p3 + p_t - 2 p8 for a conserved source: {V_conserved}")
    check(sp.simplify(V_conserved - sp.diff(P8, yc) / (3 * H)) == 0,
          "PROVED: for a conserved source V = p3 + p_t - 2 p8 = p8'(y) / (3H)")
    '''),
    md(r"""
    ## 10. Testing $V = p_8'/(3H)$ on the recorded Kohn-Sham states

    The next cell reads the 75 profile files of the Kohn-Sham record (151 points
    $y = -3, -2.98, \dots, 0$; columns `rho`, `p3`, `p_t`, `p8` among others), the
    table of integrals and the parameters. It defines `slope`, the fourth-order
    difference of section 3 with the step $s \cdot h$ ($h = 0.02$, $s = 1, 2, \dots$),
    evaluated at the inner points (two points at each end have no neighbours on one
    side). For every state with a nonzero tensor it compares $V$ with $p_8'/(3H)$ and
    divides the largest difference by max|T| (the largest absolute value of $\rho$,
    $p_3$, $p_t$, $p_8$ of the state).
    """),
    code(r'''
    COLUMNS = ("rho", "p3", "p_t", "p8")  # the four diagonal components


    def read_profile(path):
        """A profile table as a dictionary: column name -> numpy array (151 values)."""
        data = np.genfromtxt(path, delimiter=",", names=True)
        return {name: data[name] for name in data.dtype.names}


    files = sorted(repository_file(f"{GROUND}/profiles").glob("*.csv"),
                   key=lambda path: path.name)
    profiles = {path.stem: read_profile(path) for path in files}
    with repository_file(f"{GROUND}/emt-integrals.csv").open(
            encoding="utf-8", newline="") as handle:
        integrals = {row["id"]: row for row in csv.DictReader(handle)}
    physics = read_json("Revision/kohn_sham/results/parameters.json")["physics"]
    H_value, L_cut, VOL7 = physics["H"], physics["L_tipCutoff"], physics["Vol7"]
    scale = {sid: float(max(np.max(np.abs(prof[c])) for c in COLUMNS))
             for sid, prof in profiles.items()}  # max|T| of every state
    nonzero = [sid for sid in profiles if scale[sid] > 0.0]
    y = profiles["N136_lam0_a10"]["y"]  # the common grid of y
    h = float(y[1] - y[0])  # the grid step


    def slope(values, s=1):
        """dv/dy at the points i = 2s, ..., 150 - 2s (fourth order, step s h)."""
        v = values
        return (-v[4 * s:] + 8 * v[3 * s:-s] - 8 * v[s:-3 * s] + v[:-4 * s]) / (12 * h * s)


    def violation(prof):
        """V(y) = p3 + p_t - 2 p8 of a profile."""
        return prof["p3"] + prof["p_t"] - 2.0 * prof["p8"]


    residual = {sid: float(np.max(np.abs(slope(profiles[sid]["p8"]) / (3 * H_value)
                                          - violation(profiles[sid])[2:-2])))
                / scale[sid] for sid in nonzero}
    worst = max(residual, key=residual.get)  # the state with the largest difference
    report("states with a nonzero tensor", len(nonzero))
    report("grid step h", f"{h:.2f}")
    report("largest |p8'/(3H) - V| / max|T| over 70 states", f"{residual[worst]:.2e}",
           f"({worst})")
    check(len(nonzero) == 70 and residual[worst] < 1e-3,
          "V = p8'/(3H) on every state to 1e-3 of max|T| (fourth-order differences)")
    '''),
    md(r"""
    The next cell draws the identity for the history $N = 136$, $\lambda = 0$. Left:
    $p_8(y)$ at the five slices (divided by max|T|): for C2, by section 9, these
    curves would have to be horizontal. Right: $V(y)$ (lines) and $p_8'(y)/(3H)$
    (dots, every fifth grid point) of the slice $a_{4,0} = 1$. Both vertical axes are
    symmetric logarithmic (logarithmic for large positive and negative values,
    linear near zero), so that both signs and many orders of magnitude are visible.
    """),
    code(r'''
    SLICES = {"a00": 0.0, "a05": 0.5, "a10": 1.0, "a15": 1.5, "a20": 2.0}  # a4,0
    SHADES = ["#86b6ef", "#5598e7", "#2a78d6", "#1c5cab", "#104281"]  # light to dark
    history136 = [f"N136_lam0_{tag}" for tag in SLICES]
    fig, (left, right) = plt.subplots(1, 2, figsize=(9.6, 4.0))
    for shade, sid, a40 in zip(SHADES, history136, SLICES.values()):
        left.plot(y, profiles[sid]["p8"] / scale[sid], color=shade, lw=1.8,
                  label=f"$a_{{4,0}} = {a40:g}$")
    left.set_yscale("symlog", linthresh=1e-6)
    left.set_xlabel("hidden coordinate $y$ (tip $-3$, brane $0$)")
    left.set_ylabel("$p_8(y)$ / max|T|")
    left.set_title("$N = 136$, $\\lambda = 0$: $p_8$ is far from flat")
    left.legend(fontsize=7, loc="upper right")
    example = profiles["N136_lam0_a10"]
    inner = y[2:-2]  # the points where the slope is known
    right.plot(y, violation(example) / scale["N136_lam0_a10"], color="#2a78d6",
               lw=2.0, label="$V = p_3 + p_t - 2p_8$")
    right.plot(inner[::5], (slope(example["p8"]) / (3 * H_value))[::5]
               / scale["N136_lam0_a10"], "o", color="#eb6834", ms=3.5,
               label="$p_8'(y)/(3H)$")
    right.axhline(0.0, color="#e34948", ls="--", lw=1.0, label="C2: $V = 0$")
    right.set_yscale("symlog", linthresh=1e-6)
    right.set_xlabel("hidden coordinate $y$")
    right.set_ylabel("divided by max|T|")
    right.set_title("$a_{4,0} = 1$: the two sides of the identity")
    right.legend(fontsize=7, loc="upper right")
    fig.tight_layout()
    p8_range = [float(np.max(np.abs(profiles[s]["p8"])) / np.min(np.abs(profiles[s]["p8"])))
                for s in history136]  # how far p8 is from flat, per slice
    save_figure(fig, "slope_identity",
                "Left: the hidden-direction pressure $p_8(y)$ of the Kohn-Sham states "
                "$N = 136$, $\\lambda = 0$ at the five slices $a_{4,0} = 0$ to $2$, "
                "divided by the largest component of each state (horizontal axis: the "
                "hidden coordinate $y$; vertical axis symmetric logarithmic, linear "
                "between $-10^{-6}$ and $10^{-6}$); the largest $|p_8|$ is "
                f"{min(p8_range):.0f} to {max(p8_range):.3g} times the smallest, while "
                "condition C2 of a conserved source demands a flat $p_8$. Right: for "
                "$a_{4,0} = 1$ the violation $V = p_3 + p_t - 2p_8$ (blue line) and the "
                "slope $p_8'(y)/(3H)$ from fourth-order differences (orange dots) lie "
                "on top of each other, as the conservation law demands; the dashed "
                "line is the value $0$ that C2 needs.")
    '''),
    md(r"""
    How do we know that the small differences of the last test are errors of the
    finite differences and not a failure of conservation? By changing the step. The
    next cell evaluates $|p_8'/(3H) - V|/\max|T|$ at the four points
    $y = -2.4, -1.8, -1.2, -0.6$ (grid indices 30, 60, 90, 120) with the steps
    $s \cdot h$, $s = 1, 2, 3, 5, 6$, for five states, and fits a straight line to
    $\log(\text{difference})$ against $\log(\text{step})$. A fourth-order difference
    of an exact identity must give the slope $4$.
    """),
    code(r'''
    STEPS = np.array([1, 2, 3, 5, 6])  # the step is s h
    POINTS = [30, 60, 90, 120]  # grid indices of y = -2.4, -1.8, -1.2, -0.6
    STUDY = ["N8_lamp1_a00", "N136_lam0_a10", "N136_lamp2_a20", "N688_lam0_a10",
             "N688_lamm2_a00"]


    def difference_at_points(sid, s):
        """max over POINTS of |p8'/(3H) - V| / max|T| with the step s h."""
        prof = profiles[sid]
        derivative = slope(prof["p8"], s) / (3 * H_value)  # index i - 2s is point i
        return max(abs(float(derivative[i - 2 * s] - violation(prof)[i]))
                   for i in POINTS) / scale[sid]


    errors = {sid: np.array([difference_at_points(sid, s) for s in STEPS])
              for sid in STUDY}
    orders = {sid: float(np.polyfit(np.log(STEPS * h), np.log(errors[sid]), 1)[0])
              for sid in STUDY}  # the slope of the straight-line fit
    for sid in STUDY:
        say(f"{sid}: differences " + ", ".join(f"{e:.1e}" for e in errors[sid])
            + f";  fitted order {orders[sid]:.2f}")
    check(all(3.8 < order < 4.2 for order in orders.values()),
          "the differences fall like (step)^4: they are errors of the differences")
    fig, ax = plt.subplots(figsize=(6.4, 4.4))
    for sid in STUDY:
        ax.loglog(STEPS * h, errors[sid], "o-", lw=1.4, ms=4,
                  label=f"{sid} (order {orders[sid]:.2f})")
    reference = errors["N136_lam0_a10"][0] * (STEPS / STEPS[0]) ** 4.0
    ax.loglog(STEPS * h, reference, "k--", lw=1.0, label="slope 4 (reference)")
    ax.set_xlabel("step of the difference $s h$ (units of $1/H$)")
    ax.set_ylabel("max $|p_8'/(3H) - V|$ / max|T|")
    ax.legend(fontsize=7)
    save_figure(fig, "difference_order",
                "The difference between $p_8'(y)/(3H)$, computed with fourth-order "
                "differences of step $sh$ ($h = 0.02$, $s = 1, 2, 3, 5, 6$), and the "
                "violation $V = p_3 + p_t - 2p_8$, at the four points $y = -2.4$, "
                "$-1.8$, $-1.2$, $-0.6$, divided by the largest component of the state, "
                "for five recorded Kohn-Sham states (logarithmic axes; the step in units "
                "of $1/H$). The fitted slopes lie between "
                f"{min(orders.values()):.2f} and {max(orders.values()):.2f}, the order "
                "4 of the differences: the small differences are errors of the finite "
                "differences, and the conservation law itself holds.")
    '''),
    md(r"""
    ## 11. The integrated form, and why the integrated ratio of C2 is not 1

    Multiply the $y$ law by $e^{6Hy}$: since $(e^{6Hy}p_8)' = e^{6Hy}(p_8' + 6Hp_8)$
    (product rule), the law becomes $(e^{6Hy}p_8)' = 3He^{6Hy}(p_3 + p_t)$. Integrate
    from the tip $y = -L$ to the brane $y = 0$ (fundamental theorem of calculus) and
    multiply by $2\,\mathrm{Vol}_7$ (the volume factor of the record's integrals):

    $$2\,\mathrm{Vol}_7\left[p_8(0) - e^{-6HL}p_8(-L)\right] =
    3H\left(\textstyle\int p_3 + \int p_t\right),$$

    where $\int X$ means $2\,\mathrm{Vol}_7\int_{-L}^{0}e^{6Hy}X\,dy$, the column
    `int_X` of the record's table. The next cell checks this with the table's brane
    values, tip values and integrals for all 70 nonzero states (relative difference)
    and compares with the solver's check `emt_y_conservation_integrated`.
    """),
    code(r'''
    def number(sid, column):
        """A number of the record's table of integrals."""
        return float(integrals[sid][column])


    tip_weight = float(np.exp(-6.0 * H_value * L_cut))  # e^{-6HL}, about 1.5e-8
    integrated = {}
    for sid in nonzero:
        left_side = 2 * VOL7 * (number(sid, "p8_brane") - tip_weight * number(sid, "p8_tip"))
        right_side = 3 * H_value * (number(sid, "int_p3") + number(sid, "int_p_t"))
        integrated[sid] = abs(left_side - right_side) / abs(right_side)
    worst_integrated = max(integrated, key=integrated.get)
    report("largest relative difference of the integrated law",
           f"{integrated[worst_integrated]:.3e} ({worst_integrated})")
    solver = record_entry(KS_RUST, "emt_y_conservation_integrated")["detail"]
    say("the solver record: " + solver)
    same_as_column = all(abs(integrated[sid] - number(sid, "ycons_integrated_rel"))
                         < 1e-13 for sid in nonzero)  # the table's own column
    reproduces(integrated[worst_integrated] < 1e-7 and same_as_column
               and f"({worst_integrated})" in solver,
               "the integrated conservation law holds for all 70 states",
               KS_RUST, ["emt_y_conservation_integrated"])
    '''),
    md(r"""
    Notebook 17a found that the integrated ratio $R = (\int p_3 + \int p_t)/(2\int
    p_8)$ lies between about $0.1$ and $0.4$ instead of $1$. The integrated law
    explains this number. Divide it by $2\int p_8$ and write $\int p_8 =
    2\,\mathrm{Vol}_7\,\bar p_8\,(1 - e^{-6HL})/(6H)$, where $\bar p_8$ is the
    weighted mean of $p_8$ (because $\int_{-L}^0 e^{6Hy}dy = (1 - e^{-6HL})/(6H)$):

    $$R = \frac{p_8(0) - e^{-6HL}p_8(-L)}{(1 - e^{-6HL})\,\bar p_8}
    \approx \frac{p_8(\text{brane})}{\bar p_8}.$$

    So the averaged C2 asks that $p_8$ at the brane equal its mean: true for a flat
    $p_8$, false for the Kohn-Sham states. The next cell computes $R$ both ways for
    every nonzero state and checks the record's closest value.
    """),
    code(r'''
    mean_p8 = {sid: number(sid, "int_p8") / (2 * VOL7 * (1 - tip_weight) / (6 * H_value))
               for sid in nonzero}  # the weighted mean of p8
    ratio = {sid: (number(sid, "int_p3") + number(sid, "int_p_t"))
             / (2 * number(sid, "int_p8")) for sid in nonzero}  # as in Notebook 17a
    from_brane = {sid: (number(sid, "p8_brane") - tip_weight * number(sid, "p8_tip"))
                  / ((1 - tip_weight) * mean_p8[sid]) for sid in nonzero}
    agreement = max(abs(from_brane[sid] / ratio[sid] - 1.0) for sid in nonzero)
    closest = min(ratio, key=lambda sid: abs(ratio[sid] - 1.0))
    report("largest relative difference of the two forms of R", f"{agreement:.1e}")
    report("R closest to 1", f"{ratio[closest]:.6g} ({closest})")
    detail = record_entry(SOURCE_REPORT, "ks_integrals_violate_algebraic_condition")[
        "detail"]
    reproduces(agreement < 1e-9
               and f"(closest to 1: {ratio[closest]:.6g} at {closest})" in detail,
               "R = p8(brane) / mean of p8 (up to e^(-6HL)) for all 70 states",
               SOURCE_REPORT, ["ks_integrals_violate_algebraic_condition"])
    '''),
    md(r"""
    The next cell draws $|p_8(\text{brane})|$ against $|\bar p_8|$ for all 70
    states (logarithmic axes; filled markers where $p_8$ is positive, open markers
    where it is negative: the $N = 8$ states have negative $p_8$). The averaged C2
    would put every point on the diagonal.
    """),
    code(r'''
    N_COLOURS = {8: "#1baf7a", 136: "#2a78d6", 688: "#eb6834"}
    fig, ax = plt.subplots(figsize=(6.4, 5.0))
    for n, colour in N_COLOURS.items():
        ids = [sid for sid in nonzero if sid.startswith(f"N{n}_")]
        xs = [abs(mean_p8[sid]) for sid in ids]
        ys = [abs(number(sid, "p8_brane")) for sid in ids]
        filled = mean_p8[ids[0]] > 0  # all states of one N have the same sign
        ax.loglog(xs, ys, "o", ms=5, color=colour,
                  mfc=colour if filled else "none",
                  label=f"$N = {n}$" + ("" if filled else " ($p_8 < 0$)"))
    line = np.array([1e-7, 1.0])  # the range of the diagonal
    ax.loglog(line, line, "--", color="#e34948", lw=1.2,
              label="averaged C2: brane value = mean")
    ax.set_xlabel("weighted mean $|\\bar p_8|$ (units of $m^8$)")
    ax.set_ylabel("$|p_8|$ at the brane $y = 0$ (units of $m^8$)")
    ax.legend(fontsize=8, loc="upper left")
    signs_uniform = all(np.sign(mean_p8[sid]) == np.sign(mean_p8[f"{sid[:sid.index('_')]}"
                                                                   "_lam0_a10"])
                        if not sid.startswith("N8_") else mean_p8[sid] < 0
                        for sid in nonzero)
    save_figure(fig, "brane_and_mean",
                "The hidden-direction pressure $p_8$ at the brane against its weighted "
                "mean over the patch, for the 70 recorded Kohn-Sham states with a "
                "nonzero source (logarithmic axes, units of $m^8$; colours: particle "
                "number; open markers: the $N = 8$ states, whose $p_8$ is negative). By "
                "the integrated conservation law the averaged condition C2 holds only "
                "on the dashed diagonal; every state lies below it, with ratios "
                f"between {min(ratio.values()):.3f} and {max(ratio.values()):.3f}: "
                "$p_8$ at the brane is much smaller than its mean.")
    check(signs_uniform and all(ratio[sid] < 1.0 for sid in nonzero),
          "every state lies below the diagonal; p8 < 0 exactly for N = 8")
    '''),
    md(r"""
    ## 12. The time direction: energy exchange and condition C3

    The $x_4$ law of section 9 for a source that does not depend on $x_8$ reads
    $\rho' = -3a_4'(p_3 - p_t)$. In words: when 3-space inflates ($a_4' > 0$) a
    3-space pressure $p_3$ takes energy out of the source, and when the extra times
    deflate an extra-time pressure $p_t$ puts energy in. For the linear member
    $a_4' = AH \neq 0$, so a constant $\rho$ (part of C3) holds exactly when
    $p_3 = p_t$ (another part of C3).

    The $a_4$ equations know this. Write the constraint as
    $\mathcal C = \sum_k\alpha_kE_{(k)}{}^{x_4}{}_{x_4} + \Lambda + \kappa\rho = 0$
    and the evolution equation as $\mathcal E = a_4''F - \kappa(p_3 - p_t) = 0$. The
    left-hand side of $\mathcal C$ depends on $x_4$ only through $a_4'$, so by the
    chain rule $d\mathcal C/dx_4 = (\partial\mathcal C/\partial a_4')\,a_4'' +
    \kappa\rho'$. The next cell inserts the record's Lovelock components and $F$,
    uses $\rho' = -3a_4'(p_3 - p_t)$, and checks
    $d\mathcal C/dx_4 = 3a_4'\,\mathcal E$ for all couplings $\alpha_1, \alpha_2,
    \alpha_3$. Along the linear member ($a_4'' = 0$) this gives
    $d\mathcal C/dx_4 = -3\kappa AH(p_3 - p_t)$: the constraint can hold at all
    times only if $p_3 = p_t$.
    """),
    code(r'''
    ad1, ad2 = sp.symbols("ad1 ad2", real=True)  # a4' and a4''
    alpha = sp.symbols("alpha1:4", real=True)  # the Lovelock couplings
    kappa, Lam, p3s, pts = sp.symbols("kappa Lam p3 pt", real=True)
    LOCALS = {"ad1": ad1, "ad2": ad2, "H": H, "alpha1": alpha[0], "alpha2": alpha[1],
              "alpha3": alpha[2]}


    def parse(text):
        """A formula of the record (Wolfram Language text) as a sympy expression."""
        return sp.sympify(text.replace("^", "**"), locals=LOCALS)


    E44 = sum(alpha[k - 1] * parse(equations["lovelockTensors"][f"E{k}"]["x4x4"]["input"])
              for k in (1, 2, 3))  # sum_k alpha_k E_(k)^x4_x4
    F = parse(equations["generalSource"]["evolution_F"]["input"])
    rho_dot = -3 * ad1 * (p3s - pts)  # the x4 conservation law
    constraint_dot = sp.diff(E44, ad1) * ad2 + kappa * rho_dot  # chain rule
    evolution = ad2 * F - kappa * (p3s - pts)
    say(f"Einstein part: d/da4' of E_(1)^x4_x4 = {sp.diff(parse(equations['lovelockTensors']['E1']['x4x4']['input']), ad1)}")
    reproduces(sp.expand(constraint_dot - 3 * ad1 * evolution) == 0,
               "PROVED: dC/dx4 = 3 a4' times the evolution equation (all couplings)",
               WL_A4, ["constraint_propagation_bianchi"])
    linear = sp.expand(constraint_dot.subs({ad2: 0, ad1: sp.Symbol("A") * H}))
    say(f"along the linear member a4 = A H x4: dC/dx4 = {sp.factor(linear)}")
    '''),
    md(r"""
    For the Kohn-Sham gas the integrated version of the $x_4$ law is recorded:
    $dE/da_{4,0} = -3\left(\int p_3 - \int p_t\right)$ with the total energy
    $E = \int\rho$ (the Rust solver checks it with tiny steps of $a_4$). The recorded
    slices are $0.5$ apart, so we can test it with Simpson's rule over the whole
    history: $E(2) - E(0)$ must equal the integral of $-3(\int p_3 - \int p_t)$ from
    $0$ to $2$. This is fair only if each state is followed continuously from slice
    to slice (no level crosses the Fermi level); the record of the history lists no
    such crossing. The next cell does this for all 15 series (three particle numbers,
    five couplings).
    """),
    code(r'''
    history = read_json("Revision/kohn_sham/results/adiabatic/history.json")
    no_crossing = all(not series["fermiLevelCrossings"] for series in history["series"])
    TAGS = ["lamm2", "lamm1", "lam0", "lamp1", "lamp2"]  # the five couplings
    simpson_error, energies, drives = {}, {}, {}
    for n in (8, 136, 688):
        for tag in TAGS:
            ids = [f"N{n}_{tag}_{s}" for s in SLICES]
            E = np.array([number(sid, "int_rho") for sid in ids])  # E at the slices
            drive = np.array([-3 * (number(sid, "int_p3") - number(sid, "int_p_t"))
                              for sid in ids])  # dE/da4 at the slices
            simpson = 0.5 / 3 * (drive[0] + 4 * drive[1] + 2 * drive[2]
                                 + 4 * drive[3] + drive[4])  # step 0.5, from 0 to 2
            energies[(n, tag)], drives[(n, tag)] = E, drive
            change = E[-1] - E[0]
            simpson_error[(n, tag)] = (abs(simpson - change) / abs(change)
                                       if change != 0.0 else abs(simpson))
    moving = [key for key in simpson_error if key[0] != 8]
    largest = max(simpson_error[key] for key in moving)
    frozen = all(np.all(energies[(8, tag)] == energies[(8, tag)][0])
                 and np.all(drives[(8, tag)] == 0.0) for tag in TAGS)
    for n in (136, 688):
        E = energies[(n, "lam0")]
        say(f"N = {n}, lambda = 0: E(0) = {E[0]:.6g}, E(2) = {E[-1]:.6g}, "
            f"change {E[-1] - E[0]:.6g}, relative Simpson error "
            f"{simpson_error[(n, 'lam0')]:.1e}")
    report("largest relative Simpson error, N = 136 and 688", f"{largest:.1e}")
    reproduces(no_crossing and largest < 1e-3 and frozen,
               "E(2) - E(0) = integral of -3 (int p3 - int p_t) along the history",
               KS_RUST, ["emt_energy_change_dE_da4"])
    '''),
    md(r"""
    The next cell draws the energy along the history for $N = 136$ and $N = 688$
    with $\lambda = 0$, divided by its value at $a_{4,0} = 0$ (left), together with
    the values predicted from $E(0)$ by Simpson's rule (crosses at $a_{4,0} = 1$ and
    $2$) and the constant energy that C3 would need; and the relative Simpson error
    of all ten moving series (right). The $N = 8$ series do not move: their
    pressures obey $p_3 = p_t$ exactly, so their energy is the same at every slice.
    """),
    code(r'''
    fig, (left, right) = plt.subplots(1, 2, figsize=(9.6, 4.0))
    slice_values = np.array(list(SLICES.values()))
    for n, marker in ((136, "o"), (688, "s")):
        E, drive = energies[(n, "lam0")], drives[(n, "lam0")]
        to_one = E[0] + 0.5 / 3 * (drive[0] + 4 * drive[1] + drive[2])  # 0 to 1
        to_two = to_one + 0.5 / 3 * (drive[2] + 4 * drive[3] + drive[4])  # 1 to 2
        left.plot(slice_values, E / E[0], marker=marker, color=N_COLOURS[n], lw=1.6,
                  label=f"$N = {n}$: recorded $E$")
        left.plot([1.0, 2.0], [to_one / E[0], to_two / E[0]], "x", color="black",
                  ms=9, mew=1.6)
    left.plot([], [], "x", color="black", label="from $E(0)$ by Simpson")
    left.axhline(1.0, color="#e34948", ls="--", lw=1.2, label="C3: constant energy")
    left.set_xlabel("slice $a_{4,0}$ (history $a_4 = Hx_4$)")
    left.set_ylabel("$E(a_{4,0}) / E(0)$")
    left.set_ylim(0.0, 1.1)
    left.legend(fontsize=7, loc="lower left")
    keys = [(n, tag) for n in (136, 688) for tag in TAGS]
    labels = [f"{n}, {tag[3:]}" for n, tag in keys]  # N and the coupling tag
    right.bar(range(len(keys)), [simpson_error[key] * 1e4 for key in keys],
              color=[N_COLOURS[n] for n, _ in keys])
    right.set_xticks(range(len(keys)), labels, rotation=60, fontsize=7)
    right.set_xlabel("series ($N$, coupling: m2 $= -\\lambda_2$, ..., p2 $= +\\lambda_2$)")
    right.set_ylabel("relative Simpson error ($10^{-4}$)")
    fig.tight_layout()
    fall = [energies[(n, "lam0")][0] / energies[(n, "lam0")][-1] for n in (136, 688)]
    save_figure(fig, "energy_exchange",
                "Left: the total energy $E = \\int\\rho$ of the Kohn-Sham states with "
                "$\\lambda = 0$ along the history $a_4 = Hx_4$, divided by its value at "
                "$a_{4,0} = 0$ (circles $N = 136$, squares $N = 688$; pure numbers), "
                "the values predicted from $E(0)$ by integrating "
                "$dE/da_4 = -3(\\int p_3 - \\int p_t)$ with Simpson's rule (crosses), "
                "and the constant energy that condition C3 of the linear member needs "
                f"(dashed). The energy falls by factors of {fall[0]:.2f} and "
                f"{fall[1]:.2f}: as 3-space inflates and the extra times deflate, the "
                "gas with $p_3 > p_t = 0$ gives up energy. Right: the relative error of "
                "Simpson's rule for $E(2) - E(0)$ in all ten moving series, in units of "
                f"$10^{{-4}}$ (largest {largest:.1e}): the energy-change law holds to "
                "the accuracy of the five slices.")
    '''),
    md(r"""
    ## 13. The last check

    The last cell checks that the five figure files exist in the folder
    Revision/textbook/figures and prints the number of checks that passed.
    """),
    code(r'''
    figure_names = ["eight_gammas", "slope_identity", "difference_order",
                    "brane_and_mean", "energy_exchange"]
    paths = [output_file(f"{FIGURE_FOLDER}/17b_{k}_{name}.png")
             for k, name in enumerate(figure_names, 1)]
    check(all(path.is_file() for path in paths),
          "every figure file of this notebook exists")
    all_checks_passed()
    '''),
    md(r"""
    ## 14. What this notebook showed

    - COMPUTED and exact: the Kohn-Sham source rests on the author's eight REAL
      $16 \times 16$ gamma matrices (signed permutation matrices with the Clifford
      relation for all 64 pairs); the Rust solver read exactly this file (equal sha256
      digits).
    - PROVED (sympy, equal to the $a_4$ record and to the Kohn-Sham theory record):
      in the author's metric a diagonal source is conserved when
      $\rho' = -3a_4'(p_3 - p_t)$ (time direction) and
      $p_8' + 6Hp_8 = 3H(p_3 + p_t)$ (hidden direction, coordinate $y$).
    - PROVED: for a conserved source the violation of C2 is
      $p_3 + p_t - 2p_8 = p_8'(y)/(3H)$, so C2 is the statement "$p_8$ is flat"; and
      $d\mathcal C/dx_4 = 3a_4'\,\mathcal E$, so the linear member needs $p_3 = p_t$
      and a constant $\rho$.
    - COMPUTED (the 75 recorded states): the Kohn-Sham states obey the conservation
      law point by point (to about $10^{-4}$ of max|T| with fourth-order differences
      of step 0.02, the error falling with the fourth power of the step), integrated
      over the patch (to about $10^{-11}$), and along the history (Simpson's rule, to
      about $2 \times 10^{-4}$).
    - Hence the Kohn-Sham source is CONSERVED but NOT ADMISSIBLE: its $p_8$ is far
      from flat (so C1 and C2 fail together) and its $p_3 > p_t$ makes its energy
      change along the history (so C3 fails). Conservation is necessary for a source
      of the $a_4$ equations, not sufficient. The history $a_4 = Hx_4$ remains a
      PRESCRIBED BACKGROUND (ASSUMED), and the Kohn-Sham gas a test field without
      back-reaction.
    - NOT shown (OPEN): what metric the Kohn-Sham gas would produce with
      back-reaction; whether any state of dirac16complex is an admissible source of
      the author's metric.
    """),
]

if __name__ == "__main__":
    raise SystemExit(run_builder(__file__))
