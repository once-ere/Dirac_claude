#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
"""Builder of Notebook 14a, "The reduction of the Kohn-Sham equation to eight 2x2
blocks and the rescaling identity" (textbook "Universes in Pairs", chapter 14).

The notebook Revision/textbook/notebooks/14a_block_reduction.ipynb is BUILT from this
file by Revision/textbook/tools/nbkit.py (never edit the .ipynb by hand):

    python Revision/textbook/tools/nbkit.py build \
        Revision/textbook/notebooks/src/14a_block_reduction.py --date YYYY-MM-DD
    python Revision/textbook/tools/nbkit.py check \
        Revision/textbook/notebooks/src/14a_block_reduction.py

The notebook works in the corrected metric of 2026-10-16 (version 2, Revision/SPEC.md
section 1).  Every exact statement reproduces a check of the Revision records
Revision/kohn_sham/reports/ks-theory-python.json (sympy) and ks-theory-wolfram.json
(WolframScript), written for that metric on 2026-10-16/17; the block basis is
compared entry by entry with Revision/kohn_sham/ks-theory.json and the partner
parameters of the rescaling identity with results/rescaling/rescaling.csv.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools"))
from nbkit import code, md, run_builder  # noqa: E402

FACTS = {
    "id": "14a",
    "name": "14a_block_reduction",
    "title": "The reduction of the Kohn-Sham equation to eight 2x2 blocks and the "
             "rescaling identity",
    "purpose": (
        "It rebuilds from the author's real 16 x 16 gamma matrices every exact step "
        "that turns the 16-component Kohn-Sham equation of dirac16complex in the "
        "deflating primordial field (the corrected metric of 2026-10-16) into eight "
        "independent 2 x 2 equations in the hidden coordinate y: the hidden "
        "coordinate on the two halves of a cell and the metric in it, with the hidden "
        "scale f = exp(-a4) b4^(1/2) and the momentum weight kappa = exp(-a4); the "
        "spin-connection term (3/2)(H/f) gamma^(x0) + (b4'/b4 - a4'/2) gamma^(x4) and "
        "the contribution of every direction to it; the factor "
        "exp(-3Hy/2) exp(a4/2)/b4 that removes it; the three commuting labels J, K1, "
        "K2 and the block basis V; the block forms of every matrix of the equation; "
        "the chirality matrix Gamma, which pairs the blocks of opposite type and "
        "reverses the mass; and the exact rescaling identity between the slices of "
        "the prescribed deflating history. It checks every step against the "
        "Revision records and draws five teaching figures."
    ),
    "records": [
        ["Revision/algebra/gammas.json",
         "the author's 16 x 16 gamma matrices in the order x0 to x7 (read)"],
        ["Revision/kohn_sham/ks-theory.json",
         "the exact Kohn-Sham theory of dirac16complex in the corrected metric: the "
         "block basis, the block forms and the rescaling identity (read and "
         "reproduced)"],
        ["Revision/kohn_sham/reports/ks-theory-python.json",
         "the sympy checks of the theory; this notebook reproduces 26 of them"],
        ["Revision/kohn_sham/reports/ks-theory-wolfram.json",
         "the same checks made independently in WolframScript (their verdicts are "
         "read)"],
        ["Revision/kohn_sham/results/rescaling/rescaling.csv",
         "the partner lattice spacings, extra-time volumes, constants H and cutoffs L "
         "of the rescaling identity used by the Rust solver (reproduced)"],
    ],
    "packages": ["numpy", "sympy", "matplotlib"],
    "needs_rust": [],
    "expected_seconds": 75,
    "timeout_seconds": 900,
    "files_written": [
        "Revision/textbook/figures/14a.captions.json",
        "Revision/textbook/figures/14a_1_hidden_coordinate.png",
        "Revision/textbook/figures/14a_2_inflation_deflation.png",
        "Revision/textbook/figures/14a_3_spin_connection_terms.png",
        "Revision/textbook/figures/14a_4_block_structure.png",
        "Revision/textbook/figures/14a_5_rescaling.png",
    ],
    "final_lines": [
        "PASS all five figure files of this notebook exist",
        "ALL 31 CHECKS PASSED (notebook 14a)",
    ],
    "troubleshooting": [
        ["the cells of sections 7 and 8 seem to hang",
         "they do exact algebra with 16 x 16 matrices of symbols and two unknown "
         "functions of the time; they take 15 to 40 seconds each on a laptop; wait "
         "until the PASS lines appear."],
    ],
}

CELLS = [
    md(r"""
    ## 1. What this notebook computes

    The Kohn-Sham equation of dirac16complex in the author's primordial field is an
    equation for 16 complex functions of the eight coordinates $x_0, \dots, x_7$. This
    notebook turns it, step by exact step, into eight independent equations for TWO
    functions of ONE coordinate, the hidden coordinate $y$. It uses the corrected
    metric of 2026-10-16 (version 2), the current metric of the Revision record.
    Every step is computed here with exact algebra (sympy) from the author's gamma
    matrices and compared with the Revision record, which made the same computation
    twice (in sympy and in WolframScript). The steps are:

    - the hidden coordinate $y = \ln|\sin z|/(6H)$ on the two halves of a cell, and
      the metric in it: the hidden direction carries the HIDDEN SCALE
      $f = e^{-a_4}b_4^{1/2}$ and shrinks together with the deflating extra times
      (figures 1 and 2);
    - the spin connection: the term that survives in the Dirac operator is
      $\frac32(H/f)\gamma^{(x_0)} + (b_4'/b_4 - \frac12 a_4')\gamma^{(x_4)}$; the
      notebook shows what every direction contributes (figure 3);
    - the factor $e^{-(3/2)Hy}e^{a_4/2}b_4^{-1}$ in the orbital removes this term
      exactly, for every history $a_4(x_4)$, $b_4(x_4)$;
    - the equation becomes $i\,\partial_{x_4}\chi = h\,\chi$ with a Hermitian $h$;
    - three matrices $J, K_1, K_2$ commute with $h$ and split the 16 components into
      eight blocks of two; the block basis $V$ is built and compared entry by entry
      with the Revision record (figure 4);
    - in every block the equation is $h_j = j[-(i/f)\sigma_1\,d/dy + M\sigma_2 +
      \kappa k\sigma_3] + v$ with $\kappa = e^{-a_4}$, and only two types of blocks
      exist ($j = \pm 1$);
    - the chirality MATRIX $\Gamma$ maps a block of type $j$ with mass $M$ onto a
      block of type $-j$ with mass $-M$;
    - a slice of the deflating history is exactly the first slice with a rescaled
      constant $H$, cutoff $L$, lattice spacing and extra-time volume: the exact
      rescaling identity (figure 5).

    The notebook prints a line starting with PASS for every check (31 in all) and
    saves five figures.
    """),
    md(r"""
    ## 3. The words used in this notebook

    - **Coordinates $x_0, \dots, x_7$**: the author's names, in this order. $x_0$ is
      the hidden SPACE-LIKE direction, listed first, with $z = 6Hx_0$ taking every
      real value; $x_1, x_2, x_3$ are ordinary 3-space; $x_4$ is the time;
      $x_5, x_6, x_7$ are the three EXTRA TIMES. In Python lists they have the
      positions 0 to 7.
    - **Metric, scale factor**: the metric says how long a small step $dx_\mu$ is.
      A scale factor multiplies a coordinate step: along $x_1$ a step $dx_1$ has the
      length $e^{a_4}dx_1$.
    - **The two metric functions** $a_4(x_4)$ and $b_4(x_4) > 0$ of the time
      ($b_4$ is never 1); $a_4'$ and $b_4'$ are their derivatives.
    - **Inflating, deflating**: along the history $a_4$ grows; 3-space (scale
      factor $e^{a_4}$) inflates, the extra times (scale factor
      $e^{-a_4}b_4^{1/2}(\sin^2 z)^{1/12}$) deflate exponentially.
    - **Slice**: one instant $x_4$ of the history; $a_{4,0}$ and $b_{4,0}$ are the
      values of $a_4$ and $b_4$ there. The history $a_4 = AHx_4$,
      $b_4 = b_4(0)e^{(4/3)AHx_4}$ ($A = 1$, $b_4(0) = 1$) is a PRESCRIBED
      BACKGROUND (it is given, not solved for, and the Kohn-Sham gas does not act
      back on it).
    - **Cell, halves, fold**: one period $0 < z < \pi$ of the hidden direction is a
      cell; the fold $\cos z = 0$ ($z = \pi/2$) joins its two halves $z < \pi/2$
      and $z > \pi/2$. The TIP is where $\sin z \to 0$.
    - **Hidden coordinate $y$**: $y = \ln|\sin z|/(6H)$; it is 0 at the fold and
      runs to $-\infty$ at the tips, on each half.
    - **Hidden scale $f$**: $f = e^{-a_4}b_4^{1/2}$; a step $dy$ along the hidden
      direction has the proper length $f\,dy$.
    - **Momentum weight $\kappa$**: $\kappa = e^{-a_4}$; a 3-momentum $k$ enters
      the equation as $\kappa k$.
    - **Warp factor**: $e^{Hy}$; only the scale factors of the extra times contain
      it.
    - **Gamma matrices $\gamma^{(x_0)}, \dots, \gamma^{(x_7)}$**: the author's real
      $16 \times 16$ matrices with $\gamma^a\gamma^b + \gamma^b\gamma^a =
      2\eta^{ab}$ (the Clifford relation); in the code `g0`, ..., `g7`.
    - **Spin connection $\Omega_\mu$**: the matrices that the curvature of space adds
      to the derivative of a spinor: $D_\mu = \partial_\mu + \Omega_\mu$.
    - **Hermitian matrix**: equal to its conjugate transpose, $X^\dagger = X$; its
      eigenvalues are real. **Unitary**: $V^\dagger V = 1$ (a change of basis that
      keeps lengths).
    - **Commute, anticommute**: $XY = YX$, or $XY = -YX$.
    - **Projector**: a matrix with $P^2 = P$; its rank is the dimension of the space
      it projects onto.
    - **Block**: a $2 \times 2$ piece on the diagonal of a matrix that has no other
      nonzero entries in its rows and columns.
    - **Pauli matrices** $\sigma_1 = [[0,1],[1,0]]$, $\sigma_2 = [[0,-i],[i,0]]$,
      $\sigma_3 = [[1,0],[0,-1]]$ (written row by row).
    - **Chirality matrix $\Gamma$** $= \gamma^{(x_0)}\gamma^{(x_1)}\cdots
      \gamma^{(x_7)}$: a MATRIX (not a complex conjugation); here it equals
      diag$(-1, \dots, -1, 1, \dots, 1)$.
    - **sympy**: computes exactly with symbols and fractions; a check made with
      sympy is an exact identity, not a numerical approximation.
    - **Revision record**: the files under `Revision/` that hold the verified
      computations; a PASS line ending with "reproduces ..." names the record file
      and the check that this notebook computed again.
    """),
    md(r"""
    ## 4. The physical and mathematical situation

    The author's metric of 2026-10-16 (the corrected metric, version 2) is
    diagonal. In the order $x_0, \dots, x_7$ its entries are
    $e^{-2a_4}b_4\cot^2 z$, $e^{2a_4}$ (three times), $-1$ and
    $-e^{-2a_4}b_4(\sin^2 z)^{1/6}$ (three times), with $z = 6Hx_0$ taking every
    real value, $H > 0$, and two functions $a_4(x_4)$, $b_4(x_4) > 0$ of the time;
    $(\sin^2 z)^{1/6}$ is the positive root. The signs
    $\eta = (+,+,+,+,-,-,-,-)$ say which directions are space-like ($+$) and which
    are time-like ($-$). 3-space has no warp; the hidden direction shrinks together
    with the extra times.

    In the Kohn-Sham model (the mean-field description of many quanta) every quantum
    obeys the equation

    $$\gamma^\mu D_\mu \Psi = (M_{\rm eff} - i v_v \gamma^{(x_4)})\Psi ,$$

    where $M_{\rm eff}(y)$ is the effective mass and $v_v(y)$ the vector potential
    made by all the other quanta (their formulas are not needed here). We use the
    GOOD SECTOR: $\Psi$ does not depend on the extra times $x_5, x_6, x_7$. This is
    an ASSUMPTION of the Revision theory: modes with enough momentum along the extra
    times grow without bound, and a space of states with a positive norm has been
    built only without extra-time momentum. We look for orbitals of the form

    $$\Psi = e^{i \mathbf{k}\cdot\mathbf{x}}\, e^{-(3/2)Hy}\, e^{a_4/2}\, b_4^{-1}\,
    \chi(y, x_4),$$

    a plane wave with 3-momentum $\mathbf k$ along 3-space, the factor
    $e^{-(3/2)Hy}e^{a_4/2}b_4^{-1}$, and a column $\chi$ of 16 functions of $y$ and
    the time. The notebook shows that $\chi$ obeys $i\,\partial_{x_4}\chi = h\chi$
    and that $h$ splits into eight $2\times2$ blocks. At one instant (one slice) the
    stationary orbitals solve $h\chi = \varepsilon\chi$: the stationary-slice
    (adiabatic) ansatz of the Revision theory.

    Status of the statements: every identity of this notebook is PROVED (exact, and
    verified twice in the Revision record); the good sector is ASSUMED; the history
    is a PRESCRIBED BACKGROUND.
    """),
    md(r"""
    ## 5. The author's gamma matrices

    The Revision record `Revision/algebra/gammas.json` stores the eight matrices
    $\gamma^{(x_0)}, \dots, \gamma^{(x_7)}$ as lists of rows; `gamma[a]` is
    $\gamma^{(x_a)}$. The next cell reads them, turns them into exact sympy
    matrices and checks the Clifford relation $\gamma^a\gamma^b + \gamma^b\gamma^a =
    2\eta^{ab}\,1$ for all 64 pairs $(a, b)$. It also defines the helper
    `record_check`, which reads the verdict of a named check from a Revision report;
    every check below that repeats a Revision check also requires that the record
    says PASS.
    """),
    code(r'''
    import numpy as np  # floating-point arrays and matrices
    import sympy as sp  # exact algebra with symbols

    PY_REPORT = "Revision/kohn_sham/reports/ks-theory-python.json"
    WL_REPORT = "Revision/kohn_sham/reports/ks-theory-wolfram.json"


    def record_check(name):
        """True when the check called name is PASS in the sympy record and, if the
        WolframScript record has a check of that name, PASS there too."""
        verdicts = {}
        for report in (PY_REPORT, WL_REPORT):
            data = json.loads(repository_file(report).read_text(encoding="utf-8"))
            found = [c["verdict"] for c in data["checks"] if c["name"] == name]
            verdicts[report] = found[0] if found else "absent"
        return (verdicts[PY_REPORT] == "PASS"
                and verdicts[WL_REPORT] in ("PASS", "absent"))


    fixture = json.loads(repository_file("Revision/algebra/gammas.json")
                         .read_text(encoding="utf-8"))
    g = [sp.Matrix(m) for m in fixture["gamma"]]  # g[0] = gamma^(x0) ... g[7] = gamma^(x7)
    eta = [int(v) for v in fixture["eta"]]  # +1 space-like, -1 time-like
    g0, g1, g2, g3, g4, g5, g6, g7 = g  # gN is gamma^(xN)
    I16, Z16 = sp.eye(16), sp.zeros(16)  # the 16 x 16 unit and zero matrices
    say(f"eta in the order x0 ... x7: {eta}")
    entries = sorted({int(e) for m in g for e in m})  # the different entries
    say(f"the entries of the eight gamma matrices are the integers {entries}")
    clifford = all(g[a] * g[b] + g[b] * g[a] == (2 * eta[a] if a == b else 0) * I16
                   for a in range(8) for b in range(8))
    check(clifford and eta == [1, 1, 1, 1, -1, -1, -1, -1]
          and record_check("clifford_relation"),
          "the Clifford relation gamma^a gamma^b + gamma^b gamma^a = 2 eta^ab",
          record=f"{PY_REPORT}, check clifford_relation")
    '''),
    md(r"""
    The next cell builds three products that the theory uses again and again:

    - $C = \gamma^{(x_0)}\gamma^{(x_1)}\gamma^{(x_2)}\gamma^{(x_3)}$, the product of
      the four space-like gammas; the Dirac adjoint is $\bar\Psi = \Psi^\dagger C$.
    - $B = -i\,C\,\gamma^{(x_4)}$, the matrix of the positive inner product of the
      good sector ($\langle\Psi^\dagger X \Psi\rangle = u^\dagger B X u$ for one
      quantum in the mode $u$).
    - $\Gamma = \gamma^{(x_0)}\gamma^{(x_1)}\cdots\gamma^{(x_7)}$, the chirality
      matrix.

    It checks that $C$ is real and symmetric with $C^2 = 1$, that $B$ is Hermitian
    with $B^2 = 1$, that $\Gamma$ is diagonal with eight entries $-1$ followed by
    eight entries $+1$, and three product rules used later: $BC = -i\gamma^{(x_4)}$,
    $C\gamma^{(x_4)} = iB$ and $CBC = B$. (`X.H` is the conjugate transpose
    $X^\dagger$ in sympy and `X.T` the transpose.)
    """),
    code(r'''
    C = g0 * g1 * g2 * g3  # the matrix of the Dirac adjoint
    B = -sp.I * C * g4  # the matrix of the positive inner product
    Gamma = g0 * g1 * g2 * g3 * g4 * g5 * g6 * g7  # the chirality matrix
    check(C.T == C and C * C == I16 and B.H == B and B * B == I16
          and Gamma == sp.diag(*([-1] * 8 + [1] * 8)) and record_check("C_B_Gamma"),
          "C real symmetric with C^2 = 1, B Hermitian with B^2 = 1, Gamma = diag(-1, 1)",
          record=f"{PY_REPORT}, check C_B_Gamma")
    check(B * C == -sp.I * g4 and C * g4 == sp.I * B and C * B * C == B
          and record_check("BC_and_Cg4"),
          "BC = -i gamma^(x4), C gamma^(x4) = i B and C B C = B",
          record=f"{PY_REPORT}, check BC_and_Cg4")
    '''),
    md(r"""
    ## 6. The hidden coordinate y and the metric in it

    Along $x_0$ the metric has the entry $g_{00} = e^{-2a_4}b_4\cot^2 z$ with
    $z = 6Hx_0$. We replace $x_0$ by

    $$y = \frac{\ln|\sin z|}{6H} = \frac{\ln(\sin^2 z)}{12H}.$$

    Line by line:

    1. Differentiate the second form with the chain rule: $dy/dx_0 =
       \frac{1}{12H}\cdot\frac{2\sin z\cos z}{\sin^2 z}\cdot 6H = \cot z$, for every
       real $z$ with $\sin z \ne 0$.
    2. Square: $dy^2 = \cot^2 z\,dx_0^2$, so $g_{00}\,dx_0^2 = e^{-2a_4}b_4\,dy^2 =
       f^2dy^2$ with the hidden scale $f = e^{-a_4}b_4^{1/2}$.
    3. Exponentiate the definition: $|\sin z| = e^{6Hy}$, hence
       $(\sin^2 z)^{1/6} = e^{2Hy}$: the extra-time entries become
       $-f^2e^{2Hy}$.
    4. Range: on each half of a cell, $y = 0$ at the fold $z = \pi/2$ (where
       $|\sin z| = 1$) and $y \to -\infty$ at the tip ($\sin z \to 0$). The
       reflection $z \to \pi - z$ keeps $|\sin z|$, so the same $y$ describes both
       halves.

    The metric becomes

    $$ds^2 = e^{2a_4}(dx_1^2 + dx_2^2 + dx_3^2) - dx_4^2 + f^2\left[dy^2 -
    e^{2Hy}(dx_5^2 + dx_6^2 + dx_7^2)\right] .$$

    Its scale factors (the vielbein entries) in the order $(y, x_1, \dots, x_7)$ are
    $(f, e^{a_4}, e^{a_4}, e^{a_4}, 1, fe^{Hy}, fe^{Hy}, fe^{Hy})$. The square root
    of the absolute value of the determinant is their product:
    $f\,e^{3a_4}\,f^3e^{3Hy} = e^{3a_4}f^4e^{3Hy} = e^{-a_4}b_4^2e^{3Hy}$. In the
    author's $x_0$ chart it is $e^{-a_4}b_4^2|\cot z|(\sin^2 z)^{1/4}$; the two differ
    by the factor $|dy/dx_0| = |\cot z|$ of step 1.

    The next cell verifies steps 1 to 3, the metric in the $y$ chart and the two
    determinants with sympy (with $a_0$ and $b_0$ for the values of $a_4$ and
    $b_4$ at one instant).
    """),
    code(r'''
    H = sp.symbols("H", positive=True)  # the author's constant H > 0
    y_neg = sp.symbols("y", negative=True)  # the hidden coordinate away from the fold
    x0 = sp.symbols("x0", real=True)  # the author's hidden coordinate (every real value)
    z_of_y = sp.asin(sp.exp(6 * H * y_neg))  # z(y) on the first quarter 0 < z < pi/2
    dx0_dy = sp.diff(z_of_y / (6 * H), y_neg)  # x0 = z/(6H) differentiated in y
    ok_line = sp.simplify(sp.cot(z_of_y) ** 2 * dx0_dy ** 2 - 1) == 0  # cot^2 z dx0^2 = dy^2
    ok_warp = sp.simplify((sp.sin(z_of_y) ** 2) ** sp.Rational(1, 6)
                          - sp.exp(2 * H * y_neg)) == 0  # (sin^2 z)^(1/6) = e^(2Hy)
    ok_dy = sp.simplify(sp.diff(sp.log(sp.sin(6 * H * x0) ** 2) / (12 * H), x0)
                        - sp.cot(6 * H * x0)) == 0  # dy/dx0 = cot z for every real z
    check(ok_line and ok_warp and ok_dy and record_check("geometry_hidden_coordinate"),
          "y = ln|sin z|/(6H): dy = cot z dx0 and (sin^2 z)^(1/6) = e^(2Hy)",
          record=f"{PY_REPORT}, check geometry_hidden_coordinate")
    a0 = sp.symbols("a0", real=True)  # the value of a4 at one instant
    b0 = sp.symbols("b0", positive=True)  # the value of b4 at that instant
    f0 = sp.exp(-a0) * sp.sqrt(b0)  # the hidden scale f = e^(-a4) b4^(1/2)
    z = 6 * H * x0
    metric_x0 = ([sp.exp(-2 * a0) * b0 * sp.cot(z) ** 2] + [sp.exp(2 * a0)] * 3 + [-1]
                 + [-sp.exp(-2 * a0) * b0 * (sp.sin(z) ** 2) ** sp.Rational(1, 6)] * 3)
    det_x0 = sp.simplify(sp.prod(metric_x0))  # det g in the author's x0 chart
    say(f"det g in the x0 chart of the author = {det_x0}")
    vielbein_y = [f0] + [sp.exp(a0)] * 3 + [1] + [f0 * sp.exp(H * y_neg)] * 3
    sqrt_g_y = sp.simplify(sp.prod(vielbein_y))  # sqrt|g| in the y chart
    say(f"sqrt|g| in the y chart = {sqrt_g_y}")
    ok_x0 = sp.simplify(det_x0 - sp.exp(-2 * a0) * b0 ** 4 * sp.cot(z) ** 2
                        * sp.Abs(sp.sin(z))) == 0
    ok_y = sp.simplify(sqrt_g_y - sp.exp(-a0) * b0 ** 2 * sp.exp(3 * H * y_neg)) == 0
    check(ok_x0 and ok_y and record_check("geometry_sqrt_det"),
          "det g = e^(-2a4) b4^4 cot^2 z |sin z|; sqrt|g| = e^(-a4) b4^2 e^(3Hy) in y",
          record=f"{PY_REPORT}, check geometry_sqrt_det")
    ok_g00 = sp.simplify(f0 ** 2 / dx0_dy ** 2
                         - sp.exp(-2 * a0) * b0 * sp.cot(z_of_y) ** 2) == 0
    ok_gtt = sp.simplify(f0 ** 2 * sp.exp(2 * H * y_neg) - sp.exp(-2 * a0) * b0
                         * (sp.sin(z_of_y) ** 2) ** sp.Rational(1, 6)) == 0
    check(ok_g00 and ok_gtt and record_check("geometry_line_element"),
          "f^2 dy^2 and -f^2 e^(2Hy) dx_t^2 are the hidden and extra-time entries",
          record=f"{PY_REPORT}, check geometry_line_element")
    '''),
    md(r"""
    The next cell draws the change of coordinate (with $H = 1$). Left: $y$ as a
    function of $z$ over one whole cell $0 < z < \pi$; the curve is symmetric about
    the fold $z = \pi/2$, where $y = 0$, and falls to $-\infty$ at both tips. Right:
    three factors along $y$ from $-3$ to $0$ (the Rust solver cuts the hidden
    direction at $y = -L = -3$): the warp $e^{Hy}$ of the extra-time scale factors,
    the factor $(\sin^2 z)^{1/6} = e^{2Hy}$ of the extra-time entries, and the factor
    $e^{3Hy}$ of the volume $\sqrt{|g|} = e^{-a_4}b_4^2e^{3Hy}$. The vertical axis is
    logarithmic, so each exponential is a straight line with slope 1, 2 or 3.
    """),
    code(r'''
    z_cell = np.linspace(1e-3, np.pi - 1e-3, 1201)  # one cell 0 < z < pi
    y_of_z = np.log(np.abs(np.sin(z_cell))) / 6.0  # y = ln|sin z|/(6H) with H = 1
    y_values = np.linspace(-3.0, 0.0, 301)  # the hidden coordinate from -L to 0

    fig, (left, right) = plt.subplots(1, 2, figsize=(10.0, 4.0))
    left.axvspan(0.0, np.pi / 2, color="C0", alpha=0.08)  # the first half
    left.axvspan(np.pi / 2, np.pi, color="C1", alpha=0.08)  # the second half
    left.plot(z_cell, y_of_z, color="C0")
    left.axvline(np.pi / 2, color="gray", linestyle="--", linewidth=0.8)
    left.set_xlabel("$z = 6 H x_0$ (radians), one cell $0 < z < \\pi$")
    left.set_ylabel("$y = \\ln|\\sin z|/(6H)$")
    left.set_title("the hidden coordinate on the two halves ($H = 1$)")
    left.annotate("tip", (0.05, -1.05), fontsize=9)
    left.annotate("tip", (2.85, -1.05), fontsize=9)
    left.annotate("fold: $y = 0$", (1.62, -0.12), fontsize=9)
    left.annotate("half $z < \\pi/2$", (0.35, -0.55), fontsize=8)
    left.annotate("half $z > \\pi/2$", (1.85, -0.55), fontsize=8)
    right.semilogy(y_values, np.exp(y_values), label="warp of the extra times $e^{Hy}$")
    right.semilogy(y_values, np.exp(2 * y_values), "--",
                   label="$(\\sin^2 z)^{1/6} = e^{2Hy}$")
    right.semilogy(y_values, np.exp(3 * y_values), ":",
                   label="volume factor $e^{3Hy}$ of $\\sqrt{|g|}$")
    right.set_xlabel("$y$ (units of $1/H$)")
    right.set_ylabel("factor (logarithmic scale)")
    right.set_title("the factors of the metric in the $y$ chart")
    right.legend(fontsize=8)
    save_figure(fig, "hidden_coordinate",
                "Left: the hidden coordinate $y = \\ln|\\sin z|/(6H)$ against "
                "$z = 6Hx_0$ (radians) over one cell $0 < z < \\pi$ for $H = 1$; the "
                "two shaded halves meet at the fold $z = \\pi/2$ (dashed line), where "
                "$y = 0$, and on each half $y$ falls to minus infinity at the tip "
                "($\\sin z \\to 0$); the reflection $z \\to \\pi - z$ maps one half "
                "onto the other and keeps $y$. Right: the warp $e^{Hy}$ of the "
                "extra-time scale factors (solid), the factor "
                "$(\\sin^2 z)^{1/6} = e^{2Hy}$ of the extra-time entries (dashed) and "
                "the volume factor $e^{3Hy}$ of $\\sqrt{|g|} = e^{-a_4}b_4^2e^{3Hy}$ "
                "(dotted) against $y$ from $-3$ to $0$ in units of $1/H$, on a "
                "logarithmic vertical axis; the straight lines have the slopes 1, 2 "
                "and 3, and the proper volume near the tip is smaller than at the "
                "fold by the factor $e^{-9}$.")
    '''),
    md(r"""
    The next cell draws what the deflating history does. Left: along the PRESCRIBED
    history $a_4 = AHx_4$, $b_4 = b_4(0)e^{(4/3)AHx_4}$ with $A = H = 1$ and
    $b_4(0) = 1$ (so $a_4 = x_4$), the 3-space scale factor $e^{a_4}$ grows; the
    extra-time scale factor at the fold and the hidden scale, both
    $f = e^{-a_4}b_4^{1/2} = e^{-a_4/3}$, shrink together; the momentum weight
    $\kappa = e^{-a_4}$ shrinks faster; and the proper 7-volume of a coordinate cell,
    the factor $e^{3a_4}f^4 = e^{-a_4}b_4^2 = e^{(5/3)a_4}$, grows. Right: at the
    five slices $a_{4,0} = 0, 0.5, 1, 1.5, 2$ of the Revision Rust solver, the
    extra-time scale factor $f\,e^{Hy}$ against $y$ (it contains the warp) and the
    momentum weight $\kappa$ (it does not depend on $y$; section 8 shows that a
    3-momentum $k$ enters the equation only as $\kappa k$).
    """),
    code(r'''
    a4_values = np.linspace(0.0, 2.0, 201)  # a4 along the history (= x4 for A = H = 1)
    b4_values = np.exp(4.0 * a4_values / 3.0)  # b4 = b4(0) e^((4/3) a4) with b4(0) = 1
    slices = [0.0, 0.5, 1.0, 1.5, 2.0]  # the five slices of the Revision solver

    fig, (left, right) = plt.subplots(1, 2, figsize=(10.0, 4.2))
    left.semilogy(a4_values, np.exp(a4_values), label="3-space: $e^{a_4}$ (inflates)")
    left.semilogy(a4_values, np.exp(-a4_values) * np.sqrt(b4_values), "--",
                  label="extra times at the fold and hidden scale $f$")
    left.semilogy(a4_values, np.exp(-a4_values), "-.",
                  label="momentum weight $\\kappa = e^{-a_4}$")
    left.semilogy(a4_values, np.exp(-a4_values) * b4_values ** 2, ":", color="black",
                  label="cell 7-volume $e^{-a_4} b_4^2$")
    left.set_xlabel("$a_4 = A H x_4$ (with $A = H = 1$: the time $x_4$)")
    left.set_ylabel("factor (logarithmic scale)")
    left.set_title("inflation and deflation along the history")
    left.legend(fontsize=7)
    for index, a in enumerate(slices):  # one colour per slice
        f_a = np.exp(-a / 3.0)  # the hidden scale on the history
        right.semilogy(y_values, f_a * np.exp(y_values), color=f"C{index}",
                       label=f"$a_{{4,0}} = {a}$")
        right.semilogy(y_values, np.full_like(y_values, np.exp(-a)), ":",
                       color=f"C{index}")
    right.set_xlabel("$y$ (units of $1/H$)")
    right.set_ylabel("factor (logarithmic scale)")
    right.set_title("$f e^{Hy}$ (solid) and $\\kappa$ (dotted) at five slices")
    right.legend(fontsize=7)
    save_figure(fig, "inflation_deflation",
                "Left: along the prescribed history $a_4 = A H x_4$, "
                "$b_4 = b_4(0)e^{(4/3)AHx_4}$ with $A = H = 1$, $b_4(0) = 1$, against "
                "$a_4$: the 3-space scale factor $e^{a_4}$ (solid) grows, the "
                "extra-time scale factor at the fold and the hidden scale "
                "$f = e^{-a_4}b_4^{1/2} = e^{-a_4/3}$ (dashed) shrink together, the "
                "momentum weight $\\kappa = e^{-a_4}$ (dash-dotted) shrinks faster, "
                "and the proper 7-volume of a coordinate cell $e^{-a_4}b_4^2 = "
                "e^{(5/3)a_4}$ (dotted) grows; logarithmic vertical axis. Right: at "
                "the five slices $a_{4,0} = 0$ to $2$, the extra-time scale factor "
                "$fe^{Hy}$ (solid lines, slope 1 in $y$) and the momentum weight "
                "$\\kappa = e^{-a_{4,0}}$ (dotted horizontal lines, the same at every "
                "$y$) against $y$ in units of $1/H$: only the extra times carry the "
                "warp, and every later slice lies lower.")
    '''),
    md(r"""
    ## 7. The spin connection

    A spinor needs the covariant derivative $D_\mu\Psi = \partial_\mu\Psi +
    \Omega_\mu\Psi$. For the diagonal vielbein $h_a$ of section 6 the canonical spin
    connection (the one fixed by the vielbein postulate) is computed in three steps:

    1. The Christoffel symbols $\Gamma^n_{mk} = \frac12 g^{nl}(\partial_m g_{lk} +
       \partial_k g_{lm} - \partial_l g_{mk})$. For a diagonal metric only the terms
       with two equal indices survive: $\Gamma^n_{mk} = [\delta_{mn}\partial_k g_{nn}
       + \delta_{kn}\partial_m g_{nn} - \delta_{mk}\partial_n g_{mm}]/(2g_{nn})$.
    2. The connection coefficients $\omega_\mu{}^A{}_B = h_A\,\partial_\mu(1/h_B)\,
       \delta^A_B + h_A\,\Gamma^A_{\mu B}/h_B$ (no sum over $A$, $B$).
    3. $\Omega_\mu = \frac12\sum_{A,B}\eta_{AA}\,\omega_\mu{}^A{}_B\,S^{AB}$ with
       $S^{AB} = \frac14(\gamma^A\gamma^B - \gamma^B\gamma^A)$.

    The next cell does these three steps with $a_4$ and $b_4$ arbitrary functions of
    $x_4$ (so it holds along any history), checks that the curved gammas
    $\gamma^\mu = \gamma^{(\mu)}/h_\mu$ are covariantly constant
    ($\nabla_\mu\gamma^\nu = 0$: 64 matrix equations, the proof that the connection
    is the right one), and computes the only combination that enters the Dirac
    operator, $\gamma^\mu\Omega_\mu = \sum_\mu (\gamma^{(\mu)}/h_\mu)\,\Omega_\mu$.
    The Revision record finds

    $$\gamma^\mu\Omega_\mu = \tfrac32\frac{H}{f}\gamma^{(x_0)} + \Big(\frac{b_4'}{b_4}
    - \frac{a_4'}{2}\Big)\gamma^{(x_4)} .$$

    The cell takes about 15 seconds.
    """),
    code(r'''
    X = (sp.Symbol("y", real=True),) + sp.symbols("x1:8", real=True)  # y, x1..x7
    Y, x4 = X[0], X[4]  # the hidden coordinate and the time
    a4 = sp.Function("a4", real=True)(x4)  # a4 is any function of the time x4
    b4 = sp.Function("b4", positive=True)(x4)  # b4 > 0 is any function of x4
    a4p, b4p = sp.diff(a4, x4), sp.diff(b4, x4)  # their derivatives a4' and b4'
    f = sp.exp(-a4) * sp.sqrt(b4)  # the hidden scale
    W = sp.exp(H * Y)  # the warp of the extra times
    vb = [f] + [sp.exp(a4)] * 3 + [sp.Integer(1)] + [f * W] * 3  # the scale factors
    gdiag = [eta[i] * vb[i] ** 2 for i in range(8)]  # the diagonal metric entries


    def christoffel(n, m, k):
        """Gamma^n_mk of the diagonal metric gdiag (step 1)."""
        total = 0
        if m == n:
            total += sp.diff(gdiag[n], X[k])
        if k == n:
            total += sp.diff(gdiag[n], X[m])
        if m == k:
            total -= sp.diff(gdiag[m], X[n])
        return sp.simplify(total / (2 * gdiag[n]))


    Chr = [[[christoffel(n, m, k) for k in range(8)] for m in range(8)]
           for n in range(8)]
    S = [[(g[a] * g[b] - g[b] * g[a]) / 4 for b in range(8)] for a in range(8)]
    Omega = []  # Omega[mu] is the 16 x 16 matrix Omega_mu
    for mu in range(8):
        total = sp.zeros(16)
        for A in range(8):
            for Bi in range(8):
                w = (vb[A] * sp.diff(1 / vb[Bi], X[mu]) if A == Bi else 0) \
                    + vb[A] * Chr[A][mu][Bi] / vb[Bi]  # omega_mu^A_B (step 2)
                w = sp.simplify(w)
                if w != 0:
                    total += sp.Rational(1, 2) * eta[A] * w * S[A][Bi]  # step 3
        Omega.append(sp.simplify(total))
    compatible = all(
        (sp.diff(g[n] / vb[n], X[m])
         + sum((Chr[n][m][l] * g[l] / vb[l] for l in range(8)), Z16)
         + Omega[m] * g[n] / vb[n] - g[n] / vb[n] * Omega[m]).applyfunc(sp.simplify)
        .is_zero_matrix for m in range(8) for n in range(8))
    check(compatible and record_check("spin_connection_compatibility"),
          "the curved gammas are covariantly constant (64 matrix equations)",
          record=f"{PY_REPORT}, check spin_connection_compatibility")
    slash = sp.simplify(sum((g[m] / vb[m] * Omega[m] for m in range(8)), Z16))
    c_x0 = sp.Rational(3, 2) * H / f  # the coefficient of gamma^(x0)
    c_x4 = b4p / b4 - a4p / 2  # the coefficient of gamma^(x4)
    check((slash - c_x0 * g0 - c_x4 * g4).applyfunc(sp.simplify).is_zero_matrix
          and record_check("spin_connection_slash"),
          "gamma^mu Omega_mu = (3/2)(H/f) gamma^(x0) + (b4'/b4 - a4'/2) gamma^(x4)",
          record=f"{PY_REPORT}, check spin_connection_slash")
    '''),
    md(r"""
    Where does each piece come from? The next cell splits $\gamma^\mu\Omega_\mu$
    into the contributions of the eight directions. Each contribution
    $(\gamma^{(\mu)}/h_\mu)\Omega_\mu$ turns out to be a combination
    $c_4\gamma^{(x_4)} + c_0\gamma^{(x_0)}$. Because $\gamma^{(x_4)}\gamma^{(x_4)} =
    -1$, $\gamma^{(x_0)}\gamma^{(x_0)} = +1$ and the trace of
    $\gamma^{(x_4)}\gamma^{(x_0)}$ is 0, the coefficients are found with traces:
    $c_4 = -\mathrm{Tr}(X\gamma^{(x_4)})/16$ and $c_0 = \mathrm{Tr}(X\gamma^{(x_0)})/16$.
    The cell checks that each contribution is exactly $c_4\gamma^{(x_4)} +
    c_0\gamma^{(x_0)}$, prints the coefficients (`a4p` and `b4p` stand for $a_4'$ and
    $b_4'$), and checks the facts of the Revision record, with
    $h_4 = b_4'/(2b_4) - a_4'$ the rate at which the hidden scale changes
    ($f'/f = h_4$): the hidden direction gives $\frac12h_4\gamma^{(x_4)}$; the three
    3-space directions give $\frac32a_4'\gamma^{(x_4)}$; the three extra times give
    $\frac32h_4\gamma^{(x_4)} + \frac32(H/f)\gamma^{(x_0)}$; the time gives nothing,
    $\Omega_{x_4} = 0$; and $\Omega_y$ is not zero, because $f$ depends on the time.
    """),
    code(r'''
    names = ["x0 (y)", "x1", "x2", "x3", "x4", "x5", "x6", "x7"]
    A4P, B4P = sp.symbols("a4p b4p")  # names for a4' and b4' in the printout
    c4_list, c0_list = [], []  # the coefficients of gamma^(x4) and gamma^(x0)
    split_ok = True
    for m in range(8):
        part = sp.simplify(g[m] / vb[m] * Omega[m])  # the contribution of direction m
        c4 = sp.simplify(-(part * g4).trace() / 16)
        c0 = sp.simplify((part * g0).trace() / 16)
        split_ok &= (part - c4 * g4 - c0 * g0).applyfunc(sp.simplify).is_zero_matrix
        c4_list.append(c4)
        c0_list.append(c0)
        shown_c4 = str(c4.subs({a4p: A4P, b4p: B4P}))  # write a4p, b4p for a4', b4'
        say(f"direction {names[m]:7}: c4 = {shown_c4:24} c0 = {c0}")
    check(split_ok, "every contribution is c4 gamma^(x4) + c0 gamma^(x0)")
    h4 = b4p / (2 * b4) - a4p  # the rate of the hidden scale, f'/f
    terms_ok = (sp.simplify(c4_list[0] - h4 / 2) == 0 and c0_list[0] == 0
                and sp.simplify(sum(c4_list[1:4]) - sp.Rational(3, 2) * a4p) == 0
                and sp.simplify(sum(c4_list[5:8]) - sp.Rational(3, 2) * h4) == 0
                and sp.simplify(sum(c0_list[5:8]) - c_x0) == 0
                and Omega[4].is_zero_matrix and not Omega[0].is_zero_matrix)
    check(terms_ok and record_check("spin_connection_time_terms"),
          "hidden h4/2, 3-space 3a4'/2, extra times 3h4/2 and (3/2)H/f; Omega_x4 = 0",
          record=f"{PY_REPORT}, check spin_connection_time_terms")
    '''),
    md(r"""
    The next cell draws these coefficients as a bar chart on the history at the
    first slice: $a_4' = AH = 1$, $b_4'/b_4 = \frac43AH = \frac43$, $H = 1$ and
    $a_4 = 0$, $b_4 = 1$ (so $f = 1$ and $h_4 = \frac23 - 1 = -\frac13$). For each
    direction one bar shows the coefficient of $\gamma^{(x_4)}$ and one bar the
    coefficient of $\gamma^{(x_0)}$.
    """),
    code(r'''
    on_history = {a4p: 1, b4p: sp.Rational(4, 3) * b4}  # a4' = 1, b4'/b4 = 4/3
    at_first_slice = {a4: 0, b4: 1, H: 1}  # a4 = 0, b4 = 1, H = 1: f = 1
    c4_numbers = [float(c.subs(on_history).subs(at_first_slice)) for c in c4_list]
    c0_numbers = [float(c.subs(on_history).subs(at_first_slice)) for c in c0_list]
    say("c4 on the history at the first slice: "
        + ", ".join(f"{c:+.4f}" for c in c4_numbers))
    say("c0 on the history at the first slice: "
        + ", ".join(f"{c:+.4f}" for c in c0_numbers))
    positions = np.arange(8)  # one group of two bars per direction

    fig, ax = plt.subplots(figsize=(8.0, 4.0))
    ax.bar(positions - 0.2, c4_numbers, width=0.38,
           label="coefficient of $\\gamma^{(x_4)}$")
    ax.bar(positions + 0.2, c0_numbers, width=0.38,
           label="coefficient of $\\gamma^{(x_0)}$")
    ax.axhline(0.0, color="black", linewidth=0.8)
    ax.set_xticks(positions)
    ax.set_xticklabels(["$x_0$", "$x_1$", "$x_2$", "$x_3$", "$x_4$", "$x_5$", "$x_6$",
                        "$x_7$"])
    ax.set_xlabel("direction $\\mu$ of the term $(\\gamma^{(\\mu)}/h_\\mu)\\,"
                  "\\Omega_\\mu$")
    ax.set_ylabel("coefficient (units of $H$)")
    ax.set_title("$\\gamma^\\mu\\Omega_\\mu$ on the history at the first slice: "
                 "$\\frac{3}{2}\\gamma^{(x_0)} + \\frac{5}{6}\\gamma^{(x_4)}$")
    ax.legend(fontsize=8)
    save_figure(fig, "spin_connection_terms",
                "The contribution of each direction $\\mu$ to "
                "$\\gamma^\\mu\\Omega_\\mu$, written as "
                "$c_4\\gamma^{(x_4)} + c_0\\gamma^{(x_0)}$, on the prescribed history "
                "($a_4' = 1$, $b_4'/b_4 = 4/3$, $H = 1$) at the first slice "
                "($a_4 = 0$, $b_4 = 1$, so $f = 1$): left bar of each pair $c_4$, right "
                "bar $c_0$, in units of $H$. The hidden direction $x_0$ gives "
                "$h_4/2 = -1/6$ with $h_4 = b_4'/(2b_4) - a_4'$; each 3-space "
                "direction gives $a_4'/2 = 1/2$; each extra time gives $h_4/2 = -1/6$ "
                "and $H/(2f) = 1/2$; the time $x_4$ gives nothing. In total "
                "$\\gamma^\\mu\\Omega_\\mu = (3/2)(H/f)\\gamma^{(x_0)} + "
                "(b_4'/b_4 - a_4'/2)\\gamma^{(x_4)} = (3/2)\\gamma^{(x_0)} + "
                "(5/6)\\gamma^{(x_4)}$.")
    '''),
    md(r"""
    ## 8. The factor exp(-3Hy/2) exp(a4/2)/b4 removes the spin connection

    Insert $\Psi = e^{i\mathbf k\cdot\mathbf x}e^{-(3/2)Hy}e^{a_4/2}b_4^{-1}
    \chi(y, x_4)$ into $\gamma^\mu D_\mu\Psi = \sum_\mu\gamma^\mu\partial_\mu\Psi +
    \gamma^\mu\Omega_\mu\Psi$ (section 7). Term by term:

    1. $y$: the curved gamma is $\gamma^{(x_0)}/f$, and $\partial_y e^{-(3/2)Hy} =
       -\frac32He^{-(3/2)Hy}$; the term $-\frac32(H/f)\gamma^{(x_0)}\chi$ cancels the
       $+\frac32(H/f)\gamma^{(x_0)}\chi$ of the spin connection.
    2. Time: $\partial_{x_4}(e^{a_4/2}b_4^{-1}\chi) = e^{a_4/2}b_4^{-1}
       (\partial_{x_4}\chi + (\frac12a_4' - b_4'/b_4)\chi)$; with $\gamma^{x_4} =
       \gamma^{(x_4)}$ the term $(\frac12a_4' - b_4'/b_4)\gamma^{(x_4)}\chi$ cancels
       the $(b_4'/b_4 - \frac12a_4')\gamma^{(x_4)}\chi$ of the spin connection.
    3. 3-space: $\partial_j e^{i\mathbf k\cdot\mathbf x} = ik_j e^{i\mathbf k\cdot
       \mathbf x}$ and $\gamma^{x_j} = \gamma^{(x_j)}e^{-a_4}$, so the term is
       $i\kappa k_j\gamma^{(x_j)}$ with the momentum weight $\kappa = e^{-a_4}$,
       which does not depend on $y$.
    4. Extra times: nothing depends on $x_5, x_6, x_7$ (good sector).

    So, dividing by the common factor $e^{i\mathbf k\cdot\mathbf x}e^{-(3/2)Hy}
    e^{a_4/2}b_4^{-1}$:

    $$\gamma^\mu D_\mu\Psi \to \frac1f\gamma^{(x_0)}\partial_y\chi + \gamma^{(x_4)}
    \partial_{x_4}\chi + i\kappa\,k_j\gamma^{(x_j)}\chi .$$

    The factor is the half-density of $\sqrt{|g|} = e^{-a_4}b_4^2e^{3Hy}$: its square
    times $\sqrt{|g|}$ is 1, so $\int\sqrt{|g|}\,\Psi^\dagger\Psi$ over the hidden
    direction is $\int\chi^\dagger\chi\,dy$ for every $a_4$ and $b_4$.

    The next cell verifies all this with sympy for a column of 16 arbitrary functions
    $\chi_A(y, x_4)$ and arbitrary $a_4(x_4)$, $b_4(x_4)$, and verifies that WITHOUT
    the factor $e^{-(3/2)Hy}$ the term $\frac32(H/f)\gamma^{(x_0)}\chi$ survives, and
    WITHOUT the factor $e^{a_4/2}b_4^{-1}$ the term $(b_4'/b_4 - \frac12a_4')
    \gamma^{(x_4)}\chi$ survives. It takes about 40 seconds.
    """),
    code(r'''
    k1, k2, k3 = sp.symbols("k1 k2 k3", real=True)  # the 3-momentum
    chi = sp.Matrix([sp.Function(f"chi{i}")(Y, x4) for i in range(16)])
    phase = sp.exp(sp.I * (k1 * X[1] + k2 * X[2] + k3 * X[3]))  # the plane wave
    kappa = sp.exp(-a4)  # the momentum weight (no y in it)
    factor_y = sp.exp(-sp.Rational(3, 2) * H * Y)  # removes (3/2)(H/f) gamma^(x0)
    factor_t = sp.exp(a4 / 2) / b4  # removes (b4'/b4 - a4'/2) gamma^(x4)


    def dirac(Psi):
        """gamma^mu D_mu Psi with the spin connection of section 7."""
        result = sp.zeros(16, 1)
        for m in range(8):
            result += g[m] / vb[m] * (sp.diff(Psi, X[m]) + Omega[m] * Psi)
        return result


    reduced = (g0 * sp.diff(chi, Y) / f + g4 * sp.diff(chi, x4)
               + sp.I * kappa * (k1 * g1 + k2 * g2 + k3 * g3) * chi)
    both = sp.simplify(dirac(phase * factor_y * factor_t * chi)
                       / (phase * factor_y * factor_t))
    check((both - reduced).applyfunc(sp.simplify).is_zero_matrix
          and record_check("ansatz_removes_spin_connection"),
          "with both factors: (1/f) g0 d_y + g4 d_x4 + i kappa k.g, exactly",
          record=f"{PY_REPORT}, check ansatz_removes_spin_connection")
    no_y = sp.simplify(dirac(phase * factor_t * chi) / (phase * factor_t))
    check((no_y - reduced - c_x0 * g0 * chi).applyfunc(sp.simplify).is_zero_matrix
          and record_check("ansatz_without_y_factor_term_survives"),
          "without exp(-3Hy/2) the term (3/2)(H/f) gamma^(x0) chi survives",
          record=f"{PY_REPORT}, check ansatz_without_y_factor_term_survives")
    no_t = sp.simplify(dirac(phase * factor_y * chi) / (phase * factor_y))
    check((no_t - reduced - c_x4 * g4 * chi).applyfunc(sp.simplify).is_zero_matrix
          and record_check("ansatz_without_x4_factor_term_survives"),
          "without exp(a4/2)/b4 the term (b4'/b4 - a4'/2) gamma^(x4) chi survives",
          record=f"{PY_REPORT}, check ansatz_without_x4_factor_term_survives")
    sqrt_g = sp.exp(-a4) * b4 ** 2 * sp.exp(3 * H * Y)  # sqrt|g| in the y chart
    check(sp.simplify(sqrt_g * (factor_y * factor_t) ** 2 - 1) == 0
          and record_check("ansatz_norm"),
          "sqrt|g| times the square of the factor is 1: the norm is int chi^dag chi dy",
          record=f"{PY_REPORT}, check ansatz_norm")
    '''),
    md(r"""
    ## 9. The equation i d_x4 chi = h chi and its Hermitian pieces

    With the reduced operator of section 8 the Kohn-Sham equation reads

    $$\frac1f\gamma^{(x_0)}\partial_y\chi + \gamma^{(x_4)}\partial_{x_4}\chi +
    i\kappa k_j\gamma^{(x_j)}\chi = (M - iv\gamma^{(x_4)})\chi$$

    ($M$ the effective mass, $v$ the vector potential). Solve for the time
    derivative, line by line:

    1. Move everything except the time term to the right: $\gamma^{(x_4)}
       \partial_{x_4}\chi = (M - iv\gamma^{(x_4)})\chi - \frac1f\gamma^{(x_0)}
       \partial_y\chi - i\kappa k_j\gamma^{(x_j)}\chi$.
    2. Multiply from the left by $-\gamma^{(x_4)}$; since $\gamma^{(x_4)}
       \gamma^{(x_4)} = -1$, the left side becomes $\partial_{x_4}\chi$.
    3. Multiply by $i$: $i\partial_{x_4}\chi = h\chi$ with
       $h = \frac{i}{f}\gamma^{(x_4)}\gamma^{(x_0)}\partial_y - \kappa k_j\gamma^{(x_4)}
       \gamma^{(x_j)} + M(-i\gamma^{(x_4)}) + v$.

    $h$ is Hermitian (so the levels are real and the norm $\int\chi^\dagger\chi\,dy$
    is conserved) because: $\gamma^{(x_4)}\gamma^{(x_0)}$ is real and symmetric, so
    $i\gamma^{(x_4)}\gamma^{(x_0)}$ is anti-Hermitian, and $\partial_y$ is
    anti-Hermitian too (integration by parts when the boundary terms vanish), so their
    product is Hermitian, and the positive number $1/f$ does not change that;
    $\gamma^{(x_4)}\gamma^{(x_j)}$ and $-i\gamma^{(x_4)}$ are Hermitian matrices.
    The next cell checks the three lines with 16-component columns of symbols for
    $\partial_y\chi$ and $\chi$ and a symbol $f$, and the Hermitian pieces.
    """),
    code(r'''
    M, v = sp.symbols("M v", real=True)  # effective mass and vector potential
    fs, kap = sp.symbols("f kappa", positive=True)  # the hidden scale, kappa at a point
    chi_s = sp.Matrix(sp.symbols("c0:16"))  # chi at one point (16 symbols)
    dchi_s = sp.Matrix(sp.symbols("d0:16"))  # d chi/dy at that point
    kg = kap * (k1 * g1 + k2 * g2 + k3 * g3)  # kappa k.gamma
    # lines 1 and 2: d chi/dx4 = -g4 [(M - i v g4) chi - g0 chi'/f - i kappa k.g chi]
    dt_chi = -g4 * ((M * I16 - sp.I * v * g4) * chi_s - g0 * dchi_s / fs
                    - sp.I * kg * chi_s)
    # line 3: h chi with the four pieces of h
    h_chi = (sp.I / fs * g4 * g0 * dchi_s - kap * g4 * (k1 * g1 + k2 * g2 + k3 * g3)
             * chi_s + M * (-sp.I * g4) * chi_s + v * chi_s)
    check((sp.I * dt_chi - h_chi).expand().is_zero_matrix,
          "i d_x4 chi = h chi, h = (i/f) g4 g0 d_y - kappa k_j g4 g_j + M(-i g4) + v")
    hermitian = ((g4 * g0).T == g4 * g0 and all((-g4 * gj).H == -g4 * gj
                                                for gj in (g1, g2, g3))
                 and (-sp.I * g4).H == -sp.I * g4 and (-sp.I * g4) ** 2 == I16)
    check(hermitian and record_check("hamiltonian_16_hermitian"),
          "g4 g0 real symmetric; g4 g_j and -i g4 Hermitian; (-i g4)^2 = 1",
          record=f"{PY_REPORT}, check hamiltonian_16_hermitian")
    '''),
    md(r"""
    ## 10. Three matrices that commute with everything: J, K1, K2

    Rotations of 3-space do not change the levels (section 14), so we may take
    $\mathbf k = (k, 0, 0)$ along $x_1$. Then $h$ is built from the three gammas
    $\gamma^{(x_0)}$, $\gamma^{(x_1)}$, $\gamma^{(x_4)}$ only; the first-order form
    $\chi' = fN_{16}\chi$ of the equation (section 12) uses the three products
    $A_0 = \gamma^{(x_0)}$, $A_1 = \gamma^{(x_0)}\gamma^{(x_1)}$,
    $A_4 = \gamma^{(x_0)}\gamma^{(x_4)}$, and the densities contain $B$ and $C$.

    A rule for products of different gammas: moving $\gamma^c$ through a product of
    $p$ different gammas gives the sign $(-1)^{p-1}$ if $\gamma^c$ is one of the
    factors and $(-1)^p$ if it is not. With it one finds three matrices that commute
    with $A_0, A_1, A_4, B, C$ and with each other:

    $$J = \gamma^{(x_0)}\gamma^{(x_1)}\gamma^{(x_4)},\quad K_1 = \gamma^{(x_2)}
    \gamma^{(x_3)},\quad K_2 = \gamma^{(x_5)}\gamma^{(x_6)} .$$

    Their squares: $J^2 = (-1)^3(\gamma^{(x_0)})^2(\gamma^{(x_1)})^2(\gamma^{(x_4)})^2
    = (-1)(1)(1)(-1) = +1$ (reversing three factors needs three swaps), $K_1^2 =
    -(\gamma^{(x_2)})^2(\gamma^{(x_3)})^2 = -1$, $K_2^2 = -(-1)(-1) = -1$. So $J$
    has the eigenvalues $j = \pm1$ and $K_1, K_2$ the eigenvalues $is_2, is_3$ with
    $s_2, s_3 = \pm1$. The joint eigenspace with the labels $(j, s_2, s_3)$ is the
    range of the projector

    $$P(j, s_2, s_3) = \frac{1 + jJ}{2}\cdot\frac{1 - is_2K_1}{2}\cdot
    \frac{1 - is_3K_2}{2} .$$

    The next cell checks the commutation relations and the squares, builds the
    eight projectors and checks that each has rank 2, that $P^2 = P$, and that the
    eight add up to the unit matrix: the 16 components split into 8 blocks of 2.
    """),
    code(r'''
    A0, A1, A4 = g0, g0 * g1, g0 * g4  # the matrices of the equation (k along x1)
    J, K1, K2 = g0 * g1 * g4, g2 * g3, g5 * g6
    commute = all((P * Q - Q * P).is_zero_matrix for P in (J, K1, K2)
                  for Q in (A0, A1, A4, B, C, J, K1, K2))
    check(commute and J * J == I16 and K1 * K1 == -I16 and K2 * K2 == -I16
          and record_check("blocks_commuting_set"),
          "J, K1, K2 commute with A0, A1, A4, B, C and each other; J^2 = 1, K^2 = -1",
          record=f"{PY_REPORT}, check blocks_commuting_set")
    labels = [(j, s2, s3) for j in (1, -1) for s2 in (1, -1) for s3 in (1, -1)]
    projectors = [(I16 + j * J) / 2 * (I16 - sp.I * s2 * K1) / 2
                  * (I16 - sp.I * s3 * K2) / 2 for (j, s2, s3) in labels]
    check(all(P.rank() == 2 and (P * P - P).is_zero_matrix for P in projectors)
          and sum(projectors, Z16) == I16 and record_check("blocks_projectors"),
          "eight projectors P(j, s2, s3) of rank 2 that add up to 1",
          record=f"{PY_REPORT}, check blocks_projectors")
    '''),
    md(r"""
    ## 11. The block basis V

    In each eigenspace we choose two basis vectors adapted to the equation. Since
    $A_0 = \gamma^{(x_0)}$ squares to 1, $\frac12(1 + \gamma^{(x_0)})$ projects on its
    eigenvalue $+1$. Take the first unit column $e_c$ (counting $c$ from 0) for which
    $v_+ = 8\,P(j, s_2, s_3)\,\frac12(1 + \gamma^{(x_0)})\,e_c$ is not zero; then
    $\gamma^{(x_0)}v_+ = v_+$. Put $v_- = A_1v_+$. Because $A_1$ anticommutes with
    $A_0$, $\gamma^{(x_0)}v_- = -v_-$. The 16 columns $v_+, v_-$ of the eight blocks,
    in the label order $(1,1,1), (1,1,-1), \dots, (-1,-1,-1)$, form the matrix $U$,
    and $V = U/(2\sqrt2)$.

    The next cell builds $U$ and $V$, prints the seed columns $c$, checks that $V$
    is unitary and that every entry of $U$ is $0$, $\pm1$ or $\pm i$, and compares $U$
    entry by entry with the basis stored in the Revision record
    `Revision/kohn_sham/ks-theory.json` (which the Rust solver uses).
    """),
    code(r'''
    columns, seeds = [], []
    for P in projectors:
        P_plus = P * (I16 + g0) / 2  # project on gamma^(x0) = +1 inside the block
        c = next(c for c in range(16) if not P_plus[:, c].is_zero_matrix)
        seeds.append(c)
        v_plus = 8 * P_plus[:, c]
        columns += [v_plus, A1 * v_plus]  # v+ and v- = A1 v+
    U = sp.Matrix.hstack(*columns)  # 16 x 16, entries 0, +-1, +-i
    V = U / (2 * sp.sqrt(2))  # the unitary block basis
    say(f"seed columns c of the eight blocks: {seeds}")
    theory = json.loads(repository_file("Revision/kohn_sham/ks-theory.json")
                        .read_text(encoding="utf-8"))
    as_number = {"0": 0, "1": 1, "-1": -1, "I": sp.I, "-I": -sp.I}
    U_record = sp.Matrix([[as_number[e] for e in row] for row in
                          theory["blockBasis"]["unnormalisedColumns2Sqrt2V"]])
    check(sp.simplify(V.H * V) == I16 and set(U) <= {0, 1, -1, sp.I, -sp.I}
          and seeds == theory["blockBasis"]["seedColumns0Based"]
          and record_check("blocks_basis_unitary"),
          "V = U/(2 sqrt 2) is unitary, U has entries 0, +-1, +-i",
          record=f"{PY_REPORT}, check blocks_basis_unitary")
    check(U == U_record,
          "U equals the basis of the Revision record entry by entry",
          record="Revision/kohn_sham/ks-theory.json, blockBasis.unnormalisedColumns2Sqrt2V")
    '''),
    md(r"""
    ## 12. Every matrix of the equation in the block basis

    The next cell computes $V^\dagger XV$ for the eleven matrices $X$ that occur in
    the equation and in the densities, checks that each is block diagonal (zero
    outside the eight $2\times2$ diagonal blocks), and checks the form of each
    block against the table of the Revision record. In the block with the labels
    $(j, s_2, s_3)$ the forms are printed below. A number such as $js_2$ means that
    number times the $2\times2$ unit matrix. It also checks that NOT every matrix is
    block diagonal: $\gamma^{(x_2)}$, $\gamma^{(x_5)}$ and
    $\gamma^{(x_0)}\gamma^{(x_2)}$ anticommute with $J$ and connect different blocks
    (that is why $\mathbf k$ was put along $x_1$), while $\gamma^{(x_1)}$ is block
    diagonal.
    """),
    code(r'''
    s1 = sp.Matrix([[0, 1], [1, 0]])  # the Pauli matrices
    s2m = sp.Matrix([[0, -sp.I], [sp.I, 0]])
    s3 = sp.Matrix([[1, 0], [0, -1]])
    I2 = sp.eye(2)


    def blocks_of(Xm):
        """The 8 diagonal 2 x 2 blocks of V^dagger X V and whether nothing else is."""
        Yb = sp.simplify(V.H * Xm * V)
        diagonal = [Yb[2 * b:2 * b + 2, 2 * b:2 * b + 2] for b in range(8)]
        rebuilt = sp.zeros(16)
        for b in range(8):
            rebuilt[2 * b:2 * b + 2, 2 * b:2 * b + 2] = diagonal[b]
        return diagonal, rebuilt == Yb


    expected = [  # (name, matrix, the block form as a function of (j, s2, s3))
        ("gamma^(x0)", g0, lambda j, a, b: s3, "sigma3"),
        ("gamma^(x0) gamma^(x1)", A1, lambda j, a, b: -sp.I * s2m, "-i sigma2"),
        ("gamma^(x0) gamma^(x4)", A4, lambda j, a, b: j * s1, "j sigma1"),
        ("B", B, lambda j, a, b: j * a * I2, "j s2"),
        ("C", C, lambda j, a, b: a * s2m, "s2 sigma2"),
        ("BC = -i gamma^(x4)", B * C, lambda j, a, b: j * s2m, "j sigma2"),
        ("gamma^(x4) gamma^(x1)", g4 * g1, lambda j, a, b: -j * s3, "-j sigma3"),
        ("B gamma^(x0)", B * g0, lambda j, a, b: j * a * s3, "j s2 sigma3"),
        ("J", J, lambda j, a, b: j * I2, "j"),
        ("K1", K1, lambda j, a, b: sp.I * a * I2, "i s2"),
        ("K2", K2, lambda j, a, b: sp.I * b * I2, "i s3"),
    ]
    all_forms = True
    for name, Xm, form, text in expected:
        diagonal, only_diagonal = blocks_of(Xm)
        ok = only_diagonal and all(diagonal[i] == form(*labels[i]) for i in range(8))
        all_forms &= ok
        say(f"{name:24} -> {text:12} in block (j, s2, s3): {ok}")
    check(all_forms and record_check("blocks_forms"),
          "all eleven matrices are block diagonal with the forms of the record",
          record=f"{PY_REPORT}, check blocks_forms")
    not_diagonal = (not blocks_of(g2)[1] and not blocks_of(g5)[1]
                    and not blocks_of(g0 * g2)[1] and blocks_of(g1)[1])
    check(not_diagonal and record_check("blocks_not_everything_block_diagonal"),
          "gamma^(x2), gamma^(x5), gamma^(x0)gamma^(x2) connect blocks; gamma^(x1) not",
          record=f"{PY_REPORT}, check blocks_not_everything_block_diagonal")
    '''),
    md(r"""
    The next cell draws the block structure. To have one matrix of the equation
    without derivatives, it uses the matrix $N_{16}$ of the first-order form
    $\chi' = fN_{16}\chi$ of the stationary equation at one point: from section 9 with
    $\partial_{x_4}\chi = -i\varepsilon\chi$ and $\mathbf k = (k,0,0)$ one gets
    $N_{16} = M\gamma^{(x_0)} + i(\varepsilon - v)\gamma^{(x_0)}\gamma^{(x_4)}
    - i\kappa k\,\gamma^{(x_0)}\gamma^{(x_1)}$. The cell takes the sample values
    $M = 1$, $\varepsilon = 0.5$, $v = 0$, $\kappa k = 0.7$ and shows the absolute
    values of the entries of $N_{16}$ in the original basis (left), of
    $V^\dagger N_{16}V$ in the block basis (middle; the thin lines mark the eight
    $2\times2$ blocks), and of $V^\dagger\Gamma V$ (right): the chirality matrix is
    NOT block diagonal, it connects each block to the block with the opposite $j$
    (section 13).
    """),
    code(r'''
    N16 = (1 * g0 + sp.I * sp.Rational(1, 2) * g0 * g4
           - sp.I * sp.Rational(7, 10) * g0 * g1)  # M = 1, eps = 1/2, v = 0, kappa k = 7/10
    pictures = [
        (np.abs(np.array(N16.evalf(), dtype=complex)), "$|N_{16}|$, original basis"),
        (np.abs(np.array(sp.simplify(V.H * N16 * V).evalf(), dtype=complex)),
         "$|V^\\dagger N_{16} V|$, block basis"),
        (np.abs(np.array(sp.simplify(V.H * Gamma * V).evalf(), dtype=complex)),
         "$|V^\\dagger \\Gamma V|$: pairs of blocks"),
    ]
    fig, axes = plt.subplots(1, 3, figsize=(11.5, 3.9))
    fig.subplots_adjust(wspace=0.45)  # room between the panels for the colour bars
    for ax, (values, title) in zip(axes, pictures):
        image = ax.imshow(values, cmap="Blues", vmin=0.0, interpolation="nearest")
        ax.set_title(title, fontsize=9)
        ax.set_xticks([0, 5, 10, 15])
        ax.set_yticks([0, 5, 10, 15])
        ax.set_xlabel("column")
        ax.set_ylabel("row")
        ax.grid(False)  # no grid lines over the matrix
        fig.colorbar(image, ax=ax, shrink=0.75)
    for ax in axes[1:]:  # mark the 2 x 2 blocks in the block basis
        for edge in np.arange(1.5, 15.0, 2.0):
            ax.axhline(edge, color="gray", linewidth=0.4)
            ax.axvline(edge, color="gray", linewidth=0.4)
    save_figure(fig, "block_structure",
                "Absolute values of the matrix entries (row and column 0 to 15, "
                "darker is larger) of the first-order matrix $N_{16}$ of the "
                "stationary equation $\\chi' = fN_{16}\\chi$ at $M = 1$, "
                "$\\varepsilon = 0.5$, $v = 0$, $\\kappa k = 0.7$: left in the original "
                "spinor basis, where the entries are spread over the matrix; middle "
                "in the block basis $V$, where only the eight $2\\times2$ blocks on "
                "the diagonal are nonzero (thin lines mark the blocks); right the "
                "chirality matrix $\\Gamma$ in the block basis, which connects each "
                "block $(j, s_2, s_3)$ with the block $(-j, s_2, s_3)$ four positions "
                "away.")
    '''),
    md(r"""
    ## 13. The 2x2 block Hamiltonian, its two types and the matrix Gamma

    With the forms of section 12 the Hamiltonian of section 9 becomes, in every
    block of type $j$ ($\mathbf k = (k, 0, 0)$; the number $1/f$ simply multiplies
    the derivative term):

    $$h_j = j\left[-\frac{i}{f}\sigma_1\frac{d}{dy} + M\sigma_2 + \kappa k\,\sigma_3
    \right] + v .$$

    It depends on $j$ only, not on $s_2, s_3$: there are only TWO types of block,
    four blocks of each. The eigenvalue equation $h_j\chi = \varepsilon\chi$ is the
    same as the first-order system $\chi' = fN\chi$ with
    $N = M\sigma_3 - \kappa k\sigma_2 + ij(\varepsilon - v)\sigma_1$ (multiply
    $-(ij/f)\sigma_1\chi' = (\varepsilon - v)\chi - j(M\sigma_2 + \kappa k\sigma_3)
    \chi$ from the left by $ijf\sigma_1$). Two exact relations follow:

    - $h_{-1} - v = -(h_{+1} - v)$: the two types have mirrored spectra (for $v = 0$
      the levels of $j = -1$ are the negatives of those of $j = +1$); and
      $\sigma_3 h_j(k)\sigma_3 = h_{-j}(-k)$: the orbital $\sigma_3\chi$ of
      $(-j, -k)$ has the same level as the orbital $\chi$ of $(j, k)$.
    - $\sigma_2 h_j(M, k)\sigma_2 = h_{-j}(-M, k)$. This is the block form of the
      chirality MATRIX $\Gamma$: $\Gamma$ maps the block $(j, s_2, s_3)$ onto
      $(-j, s_2, s_3)$ with the $2\times2$ entry $s_2\sigma_2$, so it maps a solution
      with mass $M$ in a block of type $j$ onto a solution with mass $-M$ in a block
      of type $-j$, at the same $k$ and the same level. It also exchanges the two
      fold conditions $\chi_2(0) = 0$ and $\chi_1(0) = 0$ of Notebook 14b. This is the
      mass-reversing matrix map of the pairing theorem T1. (The gammas are real; for a
      real field plain complex conjugation does nothing and is not a charge
      conjugation. The maps of the theory are MATRICES such as $\Gamma$.)

    The next cell checks the block Hamiltonian in all eight blocks, the equivalence
    with $\chi' = fN\chi$, the two type relations and the block form of $\Gamma$.
    """),
    code(r'''
    ok_h = True
    for i, (j, a, b) in enumerate(labels):  # the three pieces of h in block i
        Vb = V[:, 2 * i:2 * i + 2]
        ok_h &= sp.simplify(Vb.H * (sp.I * g4 * g0) * Vb + sp.I * j * s1).is_zero_matrix
        ok_h &= sp.simplify(Vb.H * (-g4 * g1) * Vb - j * s3).is_zero_matrix
        ok_h &= sp.simplify(Vb.H * (-sp.I * g4) * Vb - j * s2m).is_zero_matrix
    check(ok_h and record_check("block_hamiltonian"),
          "h_j = j[-(i/f) sigma1 d/dy + M sigma2 + kappa k sigma3] + v in all 8 blocks",
          record=f"{PY_REPORT}, check block_hamiltonian")
    eps = sp.symbols("epsilon", real=True)  # the level


    def h_algebraic(j, M_, k_, kap_):
        """The part of h_j - v without the derivative."""
        return j * (M_ * s2m + kap_ * k_ * s3)


    def N_matrix(j, M_, k_, eps_, v_, kap_):
        """N of d chi/dy = f N chi."""
        return M_ * s3 - kap_ * k_ * s2m + sp.I * j * (eps_ - v_) * s1


    kk = sp.symbols("k", real=True)
    # h chi = eps chi  <=>  -(i j/f) sigma1 chi' = (eps - v - j(M s2 + kappa k s3)) chi
    ok_ode = all(sp.simplify(-sp.I * j / fs * s1 * (fs * N_matrix(j, M, kk, eps, v, kap))
                             - ((eps - v) * I2 - h_algebraic(j, M, kk, kap)))
                 .is_zero_matrix for j in (1, -1))
    check(ok_ode and record_check("block_ode_equivalent"),
          "h_j chi = eps chi is the same as d chi/dy = f N chi",
          record=f"{PY_REPORT}, check block_ode_equivalent")
    d_term = -sp.I / fs * s1  # the matrix in front of d/dy (times j)
    ok_types = ((h_algebraic(1, M, kk, kap) + h_algebraic(-1, M, kk, kap))
                .is_zero_matrix
                and (s3 * h_algebraic(1, M, kk, kap) * s3
                     - h_algebraic(-1, M, -kk, kap)).is_zero_matrix
                and (s3 * d_term * s3 + d_term).is_zero_matrix)
    check(ok_types and record_check("block_type_relation"),
          "h_(-1) - v = -(h_(+1) - v) and sigma3 h_j(k) sigma3 = h_(-j)(-k)",
          record=f"{PY_REPORT}, check block_type_relation")
    YG = sp.simplify(V.H * Gamma * V)
    pairs = [(a, b) for a in range(8) for b in range(8)
             if not YG[2 * a:2 * a + 2, 2 * b:2 * b + 2].is_zero_matrix]
    say(f"Gamma connects the blocks (from, to): {pairs}")
    ok_pairs = (pairs == [(0, 4), (1, 5), (2, 6), (3, 7), (4, 0), (5, 1), (6, 2), (7, 3)]
                and all(YG[2 * a:2 * a + 2, 2 * b:2 * b + 2] == labels[a][1] * s2m
                        for (a, b) in pairs)
                and (Gamma * J + J * Gamma).is_zero_matrix
                and (Gamma * K1 - K1 * Gamma).is_zero_matrix
                and (Gamma * K2 - K2 * Gamma).is_zero_matrix)
    check(ok_pairs and record_check("blocks_relation_to_Gamma"),
          "Gamma maps block (j, s2, s3) onto (-j, s2, s3) with the entry s2 sigma2",
          record=f"{PY_REPORT}, check blocks_relation_to_Gamma")
    ok_map = ((s2m * h_algebraic(1, M, kk, kap) * s2m
               - h_algebraic(-1, -M, kk, kap)).is_zero_matrix
              and (s2m * d_term * s2m + d_term).is_zero_matrix)
    check(ok_map and record_check("block_Gamma_map"),
          "sigma2 h_j(M, k) sigma2 = h_(-j)(-M, k): Gamma reverses the mass",
          record=f"{PY_REPORT}, check block_Gamma_map")
    '''),
    md(r"""
    ## 14. Rotations of 3-space: only |k| matters

    A rotation by the angle $\theta$ in the $(x_1, x_2)$ plane acts on spinors with
    the matrix $R = \cos(\theta/2) + \sin(\theta/2)\gamma^{(x_1)}\gamma^{(x_2)}$. Its
    inverse is $\cos(\theta/2) - \sin(\theta/2)\gamma^{(x_1)}\gamma^{(x_2)}$: with
    $G = \gamma^{(x_1)}\gamma^{(x_2)}$, $c = \cos(\theta/2)$, $s = \sin(\theta/2)$
    and $G^2 = -1$ one gets $(c + sG)(c - sG) = c^2 - s^2G^2 = c^2 + s^2 = 1$.
    The next cell checks this, and that $R$ commutes with $\gamma^{(x_0)}$,
    $\gamma^{(x_4)}$, $B$ and $C$ (so it does not change the rest of $h$) and that it
    turns $k\gamma^{(x_1)}$ into
    $k(\cos\theta\,\gamma^{(x_1)} - \sin\theta\,\gamma^{(x_2)})$, the same momentum
    in a rotated direction. So the levels depend on $|\mathbf k|$ only, and
    $\mathbf k = (k, 0, 0)$ is no loss of generality.
    """),
    code(r'''
    theta = sp.symbols("theta", real=True)
    R = sp.cos(theta / 2) * I16 + sp.sin(theta / 2) * g1 * g2  # the spinor rotation
    R_inverse = sp.cos(theta / 2) * I16 - sp.sin(theta / 2) * g1 * g2  # its inverse
    rotated = sp.simplify(R * (kk * g1) * R_inverse)
    ok_rotation = (sp.simplify(R * R_inverse) == I16
                   and sp.simplify(rotated - kk * (sp.cos(theta) * g1
                                                   - sp.sin(theta) * g2)).is_zero_matrix
                   and all((R * Xm - Xm * R).is_zero_matrix for Xm in (g0, g4, B, C)))
    check(ok_rotation and record_check("rotation_invariance"),
          "a 3-space rotation commutes with g0, g4, B, C and rotates k: only |k| counts",
          record=f"{PY_REPORT}, check rotation_invariance")
    '''),
    md(r"""
    ## 15. The exact rescaling identity between slices

    At a slice the constants $f_0 = e^{-a_{4,0}}b_{4,0}^{1/2}$ and
    $\kappa_0 = e^{-a_{4,0}}$ are the only places where $a_{4,0}$ and $b_{4,0}$ enter
    the block Hamiltonian. Line by line:

    1. Use the PROPER hidden coordinate $Y = f_0y$. Then $\frac{1}{f_0}\frac{d}{dy} =
       \frac{d}{dY}$, so $h_j = j[-i\sigma_1\,d/dY + M\sigma_2 + (k e^{-a_{4,0}})
       \sigma_3] + v$: the block Hamiltonian of the first slice ($a_4 = 0$,
       $b_4 = 1$, $f = 1$, $\kappa = 1$) with the momentum $k e^{-a_{4,0}}$.
    2. The interval $-L \le y \le 0$ becomes $-f_0L \le Y \le 0$, the warp
       $e^{Hy} = e^{(H/f_0)Y}$, and the normalised orbital $\chi_Y = \chi/\sqrt{f_0}$.
    3. The 3-space directions form a coordinate torus of size $\ell$; the allowed
       momenta are $\mathbf k = \Delta k\,(n_1, n_2, n_3)$ with integers $n_i$ and
       $\Delta k = 2\pi/\ell$ (the Revision solver uses $\Delta k = 0.25$). The
       momenta $k e^{-a_{4,0}}$ belong to the lattice spacing $\Delta k\,e^{-a_{4,0}}$
       and the box $\ell e^{a_{4,0}}$.
    4. Densities carry the proper factor $P = e^{-3Hy}e^{a_{4,0}}/(\ell^3v_tb_{4,0}^2)$
       ($v_t$ the coordinate volume of the extra times; $1/P$ is the proper 7-volume
       of the cell per unit $e^{3Hy}$). The partner at the first slice with $H/f_0$,
       the box $\ell e^{a_{4,0}}$ and the extra-time volume $v_te^{-3a_{4,0}}
       b_{4,0}^{3/2}$ has the factor $P'(Y)$ with $P = P'(Y)/f_0$: with
       $\chi_Y^\dagger\chi_Y = \chi^\dagger\chi/f_0$ the proper densities agree.

    Hence, exactly (for the free gas, with the interaction, at every temperature):
    $\mathrm{KS}(a_{4,0}, b_{4,0}; H, L, \Delta k, v_t, \lambda) = \mathrm{KS}(0, 1;
    H/f_0, f_0L, \Delta k\,e^{-a_{4,0}}, v_te^{-3a_{4,0}}b_{4,0}^{3/2}, \lambda)$. On
    the history $b_{4,0} = e^{(4/3)a_{4,0}}$: $f_0 = e^{-a_{4,0}/3}$ and the partner
    extra-time volume is $v_te^{-a_{4,0}}$. The next cell verifies 1 to 4 with sympy
    and then computes the partner parameters of the four later slices, which the
    Rust solver used to solve every partner problem independently; they must equal
    the columns `partner_dk`, `partner_v_t`, `partner_H` and `partner_L` of the
    Revision record `rescaling.csv`.
    """),
    code(r'''
    a_sym, y_sym, Y_p = sp.symbols("a y Y", real=True)
    b_sym, ell, v_t = sp.symbols("b ell v_t", positive=True)
    f_slice = sp.exp(-a_sym) * sp.sqrt(b_sym)  # f0 at the slice
    w_a, w_b = sp.Function("w_a"), sp.Function("w_b")  # any column (w_a, w_b)
    ok_h_slice = True
    for j in (1, -1):  # line 1: h_j in y at the slice = h_j in Y at the first slice
        w_y = sp.Matrix([w_a(y_sym), w_b(y_sym)])
        h_y = j * (-sp.I * s1 * sp.diff(w_y, y_sym) / f_slice + M * s2m * w_y
                   + sp.exp(-a_sym) * kk * s3 * w_y)
        w_Y = sp.Matrix([w_a(Y_p / f_slice), w_b(Y_p / f_slice)])
        h_Y = j * (-sp.I * s1 * sp.diff(w_Y, Y_p) + M * s2m * w_Y
                   + (kk * sp.exp(-a_sym)) * s3 * w_Y)
        ok_h_slice &= sp.simplify(h_y.subs(y_sym, Y_p / f_slice) - h_Y).is_zero_matrix


    def proper_factor(a_, b_, H_, ell_, v_t_, y_):
        """P = e^(-3Hy) e^(a4,0)/(ell^3 v_t b4,0^2), the proper-density factor."""
        return sp.exp(-3 * H_ * y_) * sp.exp(a_) / (ell_ ** 3 * v_t_ * b_ ** 2)


    ok_box = sp.simplify(proper_factor(a_sym, b_sym, H, ell, v_t, y_sym)
                         - proper_factor(0, 1, H / f_slice, ell * sp.exp(a_sym),
                                         v_t * sp.exp(-3 * a_sym)
                                         * b_sym ** sp.Rational(3, 2),
                                         f_slice * y_sym) / f_slice) == 0
    on_hist = {b_sym: sp.exp(sp.Rational(4, 3) * a_sym)}  # b4,0 = e^((4/3) a4,0)
    ok_hist = (sp.simplify(f_slice.subs(on_hist) - sp.exp(-a_sym / 3)) == 0
               and sp.simplify((sp.exp(-3 * a_sym) * b_sym ** sp.Rational(3, 2))
                               .subs(on_hist) - sp.exp(-a_sym)) == 0)
    check(ok_h_slice and ok_box and ok_hist and record_check("rescaling_identity"),
          "KS(a4,0, b4,0) = KS(0, 1; H/f0, f0 L, dk e^(-a4,0), v_t e^(-3a4,0) b4,0^(3/2))",
          record=f"{PY_REPORT}, check rescaling_identity")
    rows = repository_file("Revision/kohn_sham/results/rescaling/rescaling.csv") \
        .read_text(encoding="utf-8").splitlines()
    header = rows[0].split(",")
    table = [dict(zip(header, row.split(","))) for row in rows[1:]]
    partner = {}  # slice -> (dk, v_t, H, L) of the partner problem
    worst = 0.0
    for a in slices[1:]:
        partner[a] = (0.25 * np.exp(-a), 1.0 * np.exp(-a), 1.0 * np.exp(a / 3.0),
                      3.0 * np.exp(-a / 3.0))  # dk e^-a, v_t e^-a, H e^(a/3), L e^(-a/3)
        say(f"slice a4,0 = {a}: partner dk = {partner[a][0]:.10f}, v_t = "
            f"{partner[a][1]:.10f}, H = {partner[a][2]:.10f}, L = {partner[a][3]:.10f}")
        for row in table:
            if float(row["a4"]) == a:
                mine = zip(partner[a], ("partner_dk", "partner_v_t", "partner_H",
                                        "partner_L"))
                worst = max([worst] + [abs(float(row[c]) / x - 1) for x, c in mine])
    check(len(table) == 60 and worst < 1e-14,
          "the partner dk, v_t, H and L equal those of all 60 rows of the record",
          record="Revision/kohn_sham/results/rescaling/rescaling.csv, columns "
                 "partner_dk, partner_v_t, partner_H and partner_L")
    '''),
    md(r"""
    The next cell draws the rescaling. Left: the coordinate momenta of the first
    shells of the torus lattice, $|\mathbf k| = \Delta k\sqrt{n_1^2 + n_2^2 + n_3^2}$,
    enter the equation as $|\mathbf k|\,e^{-a_{4,0}}$; on a logarithmic axis these are
    parallel straight lines falling with slope $-1$ along the history: all
    3-momenta are redshifted by the same factor. Right: the four parameters of the
    partner problem at the first slice against $a_{4,0}$ (lines: the formulas;
    dots: the values in the Revision record): the constant $He^{a_{4,0}/3}$ grows
    (the hidden direction is more strongly warped per unit proper length), the
    proper cutoff $Le^{-a_{4,0}/3}$ shrinks with the hidden direction, the lattice
    spacing $\Delta k\,e^{-a_{4,0}}$ and the extra-time volume $v_te^{-a_{4,0}}$
    shrink.
    """),
    code(r'''
    fig, (left, right) = plt.subplots(1, 2, figsize=(10.0, 4.0))
    for n2 in (1, 2, 3, 4, 5, 6):  # the first shells n1^2 + n2^2 + n3^2
        left.semilogy(a4_values, 0.25 * np.sqrt(n2) * np.exp(-a4_values),
                      label=f"$n^2 = {n2}$")
    left.set_xlabel("slice $a_{4,0}$")
    left.set_ylabel("$|\\mathbf{k}|\\,e^{-a_{4,0}}$ (units of $H$, logarithmic)")
    left.set_title("redshift of the lattice momenta")
    left.legend(fontsize=8, ncol=2)
    curves = [(np.exp(a4_values / 3.0), "$H e^{a_{4,0}/3}$", 2),
              (3.0 * np.exp(-a4_values / 3.0), "$L e^{-a_{4,0}/3}$", 3),
              (0.25 * np.exp(-a4_values), "$\\Delta k\\, e^{-a_{4,0}}$", 0),
              (np.exp(-a4_values), "$v_t e^{-a_{4,0}}$", 1)]
    for values, text, column in curves:
        line, = right.semilogy(a4_values, values, label=text)
        right.semilogy(slices[1:], [partner[a][column] for a in slices[1:]], "o",
                       color=line.get_color(), markersize=4)
    right.set_xlabel("slice $a_{4,0}$")
    right.set_ylabel("partner parameter (logarithmic)")
    right.set_title("the partner problem at the first slice")
    right.legend(fontsize=8)
    save_figure(fig, "rescaling",
                "The exact rescaling identity. Left: the momenta of the first six "
                "lattice shells, $|\\mathbf{k}| e^{-a_{4,0}}$ with "
                "$|\\mathbf{k}| = 0.25\\sqrt{n^2}$ (units of $H$), against the slice "
                "$a_{4,0}$ from 0 to 2 on a logarithmic vertical axis: parallel "
                "straight lines, every 3-momentum is redshifted by the same factor "
                "$e^{-a_{4,0}}$. Right: the parameters of the partner problem at the "
                "first slice ($H = 1$, $L = 3$, $\\Delta k = 0.25$, $v_t = 1$ on the "
                "history $b_4 = e^{(4/3)a_4}$): $He^{a_{4,0}/3}$, $Le^{-a_{4,0}/3}$, "
                "$\\Delta k\\,e^{-a_{4,0}}$ and $v_te^{-a_{4,0}}$ (lines) with the "
                "values of the Revision record rescaling.csv at the slices 0.5 to 2 "
                "(dots); logarithmic vertical axis.")
    '''),
    md(r"""
    ## 16. The last check

    The last cell checks that the five figure files exist and prints the number of
    checks that passed.
    """),
    code(r'''
    figure_names = ["14a_1_hidden_coordinate.png", "14a_2_inflation_deflation.png",
                    "14a_3_spin_connection_terms.png", "14a_4_block_structure.png",
                    "14a_5_rescaling.png"]
    check(all(output_file(f"{FIGURE_FOLDER}/{name}").is_file() for name in figure_names),
          "all five figure files of this notebook exist")
    all_checks_passed()
    '''),
    md(r"""
    ## 17. What this notebook showed

    - The hidden coordinate $y = \ln|\sin z|/(6H)$ describes both halves of a cell
      (they meet at the fold $y = 0$) and turns the corrected metric into
      $e^{2a_4}d\mathbf x^2 - dx_4^2 + f^2[dy^2 - e^{2Hy}d\mathbf x_t^2]$ with the
      hidden scale $f = e^{-a_4}b_4^{1/2}$; $\sqrt{|g|} = e^{-a_4}b_4^2e^{3Hy}$
      (PROVED; reproduces the Revision checks).
    - In the Dirac operator the spin connection contributes
      $\frac32(H/f)\gamma^{(x_0)} + (b_4'/b_4 - \frac12a_4')\gamma^{(x_4)}$ for every
      history: the hidden direction gives $\frac12h_4\gamma^{(x_4)}$, 3-space
      $\frac32a_4'\gamma^{(x_4)}$, the extra times $\frac32h_4\gamma^{(x_4)} +
      \frac32(H/f)\gamma^{(x_0)}$ (PROVED).
    - The factor $e^{-(3/2)Hy}e^{a_4/2}b_4^{-1}$, the half-density of $\sqrt{|g|}$,
      removes both terms; without either factor its term survives; the equation
      becomes $i\partial_{x_4}\chi = h\chi$ with a Hermitian $h$ and the norm
      $\int\chi^\dagger\chi\,dy$ (PROVED).
    - $J, K_1, K_2$ split the 16 components into eight blocks of two; the block
      basis equals the one in `Revision/kohn_sham/ks-theory.json` entry by entry; in
      each block $h_j = j[-(i/f)\sigma_1 d/dy + M\sigma_2 + \kappa k\sigma_3] + v$
      with $\kappa = e^{-a_4}$ and only two types $j = \pm1$ (PROVED).
    - The chirality matrix $\Gamma$ pairs the block types and maps mass $M$ to $-M$:
      a matrix map, the one of the pairing theorem T1 (PROVED here at the level of the
      block equation).
    - A slice of the prescribed deflating history is the first slice with $H/f_0$,
      $f_0L$, $\Delta k\,e^{-a_{4,0}}$ and $v_te^{-3a_{4,0}}b_{4,0}^{3/2}$ (the exact
      rescaling identity, PROVED; the partner numbers equal those of the Rust
      solver's record).
    - ASSUMED: the good sector (no dependence on the extra times). PRESCRIBED
      BACKGROUND: the history $a_4 = AHx_4$, $b_4 = b_4(0)e^{(4/3)AHx_4}$.
    """),
]

if __name__ == "__main__":
    raise SystemExit(run_builder(__file__))
