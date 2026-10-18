#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
"""Builder of Notebook 12d, "A condensate of dirac16complex00 as a source of the corrected
metric".

Textbook "Universes in Pairs", chapter 12 (the field equations for a4 and b4: Einstein and
Einstein-Lovelock).  The notebook Revision/textbook/notebooks/12d_condensate_solution.ipynb
is BUILT from this file by Revision/textbook/tools/nbkit.py (never edit the .ipynb by
hand):

    python Revision/textbook/tools/nbkit.py build \
        Revision/textbook/notebooks/src/12d_condensate_solution.py --date YYYY-MM-DD
    python Revision/textbook/tools/nbkit.py check \
        Revision/textbook/notebooks/src/12d_condensate_solution.py

The Revision record proves, for the corrected metric of 2026-10-16, the condensate
equation of the commuting field dirac16complex00 for general a4 and b4, gives exact
condensates (witnesses) whose 24 three-gamma bilinears vanish on the histories with
constant k = e^(2 a4)/b4, and states that it contains no check that combines a witness
with the field equations for a history.  This notebook rebuilds the record's statements
with exact arithmetic and the author's gamma matrices, computes the complete
energy-momentum tensor of the witnesses, and shows exactly that a witness with nonzero
density is the source of no history of its own family, in Einstein gravity and with the
author's couplings for every Lambda.  The last result is a computation of the textbook; it
is not part of the Revision record.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools"))
from nbkit import code, md, run_builder  # noqa: E402

FACTS = {
    "id": "12d",
    "name": "12d_condensate_solution",
    "title": "A condensate of dirac16complex00 as a source of the corrected metric",
    "purpose": (
        "It rebuilds, with exact arithmetic and the author's gamma matrices, the spin "
        "connection of the corrected metric for general a4 and b4, the condensate "
        "equation of the commuting field dirac16complex00 and its density law, builds "
        "the record's exact condensates whose 24 three-gamma bilinears vanish on the "
        "histories with constant k = e^(2 a4)/b4, computes their complete "
        "energy-momentum tensor, and shows exactly that such a condensate with nonzero "
        "density is the source of no history of its own family, in Einstein gravity and "
        "with the author's couplings for every Lambda. It reproduces the Revision "
        "records where they overlap and draws six teaching plots. The last result is a "
        "computation of this notebook; the "
        "Revision record states that it contains no check that combines a witness "
        "with the field equations for a history."
    ),
    "records": [
        ["Revision/algebra/gammas.json",
         "the author's real 16 by 16 gamma matrices and C"],
        ["Revision/field_equations_a4/a4-equations.json",
         "the Lovelock components of the corrected metric and the statements on the "
         "condensate source"],
        ["Revision/field_equations_a4/reports/python-a4-report.json",
         "the sympy checks with the author's gammas that the notebook reproduces"],
        ["Revision/field_equations_a4/reports/wolfram-a4-report.json",
         "the Wolfram checks of the condensate that the notebook reproduces"],
        ["Revision/lead_checks/reports/emt-divergence-and-spin-connection.json",
         "the independent check of the gravity term of the Dirac operator"],
        ["Revision/docs/DIRAC16COMPLEX00_FIELD_THEORY.md",
         "the document of the record that says that no check combines a witness with "
         "the field equations for a history"],
    ],
    "packages": ["numpy", "sympy", "matplotlib"],
    "needs_rust": [],
    "expected_seconds": 40,
    "timeout_seconds": 900,
    "files_written": [
        "Revision/textbook/figures/12d.captions.json",
        "Revision/textbook/figures/12d_1_oscillation_threshold.png",
        "Revision/textbook/figures/12d_2_three_gamma_bilinears.png",
        "Revision/textbook/figures/12d_3_witness_in_time.png",
        "Revision/textbook/figures/12d_4_tensor_mismatch.png",
        "Revision/textbook/figures/12d_5_witness_versus_required.png",
        "Revision/textbook/figures/12d_6_witness_frequency.png",
    ],
    "final_lines": [
        "PASS all six figure files exist",
        "ALL 31 CHECKS PASSED (notebook 12d)",
    ],
    "troubleshooting": [
        ["\"FileNotFoundError\" naming a file below the folder Revision",
         "the notebook reads the Revision records of the repository. Run it inside the "
         "folder Revision/textbook/notebooks of a complete copy of the repository made "
         "with git clone, not on a copy of the notebook file alone."],
    ],
}

CELLS = [
    md(r"""
    ## 1. What this notebook computes

    The other notebooks of this chapter derive the field equations for $a_4(x_4)$ and
    $b_4(x_4)$ and the source that a given history requires. Here we ask whether a
    field of the theory can BE such a source, exactly. The Revision record proves four
    things about a homogeneous condensate of the commuting field dirac16complex00 (a
    solution $\Phi(x_4)$ that depends on the time only) in the corrected metric:

    1. it obeys $\partial_4\Phi = \mathcal{A}\Phi$ with a 16 by 16 matrix
       $\mathcal{A}$ that contains no $x_0$, and its density obeys
       $S = e^{a_4}b_4^{-2}S_0$;
    2. its energy-momentum tensor has equal pressures, $p_3 = p_t = p_0$, and its
       off-diagonal components vanish exactly when 24 numbers built from it, the
       three-gamma bilinears, vanish;
    3. condensates with all 24 bilinears zero exist on the histories with constant
       $k = e^{2a_4}/b_4$ (exact examples, called witnesses);
    4. a source with equal pressures cannot drive an exponential history in Einstein
       gravity.

    The record states that it contains no check that combines a witness with the
    field equations for a history. This notebook does that combination, with exact
    arithmetic (rational and complex-rational numbers, never rounded) and the author's
    gamma matrices. It

    - rebuilds the spin connection of the corrected metric and the gravity term
      $\gamma^\mu\Omega_\mu = \tfrac32He^{a_4}b_4^{-1/2}\gamma^{(x_0)} + (u -
      \tfrac12a_4')\gamma^{(x_4)}$, $u = b_4'/b_4$;
    - rebuilds the condensate equation and the density law;
    - builds the witnesses (a one-parameter family) and checks the 24 bilinears;
    - computes their complete energy-momentum tensor (all 64 components) for an
      arbitrary $a_4(x_4)$ on their histories $b_4 = e^{2a_4}/4$;
    - shows that such a witness is the source of no history of this family in
      Einstein gravity, and, if its density is not zero, none with the author's
      couplings for any $\Lambda$;
    - states exactly what this shows and what it does not, and draws six plots.
    """),
    md(r"""
    ## 3. The words used in this notebook

    - **Coordinates** $x_0, \dots, x_7$ (the author's names): $x_0$ the hidden
      space-like direction with $z = 6Hx_0$ real, $x_1, x_2, x_3$ ordinary 3-space,
      $x_4$ the time, $x_5, x_6, x_7$ the three extra times. In the code the positions
      0 to 7 of a list stand for $x_0$ to $x_7$.
    - **Gamma matrices** $\gamma^{(x_0)}, \dots, \gamma^{(x_7)}$: the author's eight real
      16 by 16 matrices with $\gamma^{(a)}\gamma^{(b)} + \gamma^{(b)}\gamma^{(a)} =
      2\eta^{ab}$, $\eta = \mathrm{diag}(+,+,+,+,-,-,-,-)$ (the Clifford relation).
    - **Spinor** $\Phi$: a column of 16 complex numbers (here: functions of $x_4$).
      dirac16complex00 is a field of such spinors whose components are ordinary
      (commuting) complex numbers.
    - **Adjoint** $\bar\Phi = \Phi^\dagger C$ with $C = \gamma^{(x_0)}\gamma^{(x_1)}
      \gamma^{(x_2)}\gamma^{(x_3)}$; $\Phi^\dagger$ is the row of complex conjugates.
    - **Density** $S = \bar\Phi\Phi$, a real number. **Bilinear**: a number
      $\bar\Phi X \Phi$ with a 16 by 16 matrix $X$; a **three-gamma bilinear** has
      $X = \gamma^{(a)}\gamma^{(b)}\gamma^{(c)}$ with three different directions.
    - **Mass** $m$, **potential** $U(S)$, **effective mass** $M = m + U'(S)$.
    - **Vielbein** $E_a$: the square roots of $|g_{aa}|$ with the sign of $\cot z$ in
      $E_0$: $E_0 = e^{-a_4}b_4^{1/2}\cot z$, $E_i = e^{a_4}$, $E_4 = 1$,
      $E_t = e^{-a_4}b_4^{1/2}(\sin^2 z)^{1/12}$.
    - **Spin connection** $\Omega_\mu$: the 16 by 16 matrices that make the derivative
      of a spinor covariant, $D_\mu\Phi = \partial_\mu\Phi + \Omega_\mu\Phi$.
    - **Condensate**: a solution that depends on the time $x_4$ only.
    - **Frequency** $w$: in $e^{-iwx_4}$, the number of radians per unit of time.
    - **Energy-momentum tensor** $T^\mu{}_\nu$: the energy density
      $\rho = -T^{x_4}{}_{x_4}$, the pressures $p_\mu = T^\mu{}_\mu$ (no sum), and the
      mixed components; **sign convention** $\sigma_T = +1$ of the Revision record.
    - **Witness**: an explicit example that proves that something exists.
    - **Family of histories with constant $k$**: $b_4 = e^{2a_4}/k_0$ with any
      $a_4(x_4)$; then $u = 2a_4'$, $v = 2a_4''$, and the scale factor
      $e^{-a_4}b_4^{1/2} = k_0^{-1/2}$ of the hidden direction and the extra times is
      constant: these histories do not deflate.
    - **Units**: $H = 1$ and $\kappa = 1$ in the examples.
    """),
    md(r"""
    ## 4. The physical and mathematical situation

    The coupled equations are, for the field (the Euler-Lagrange equation of the
    Revision record, with $\gamma^\mu = \gamma^{(\mu)}/E_\mu$ the gammas of the curved
    metric),

    $$\gamma^\mu D_\mu\Phi = (m + U'(S))\,\Phi,$$

    and for the metric the field equations of Notebook 12a with the source

    $$T^\mu{}_\nu = \sigma_T\big(-K^{(\mu}{}_{\nu)} + \delta^\mu_\nu L\big),\qquad
    K^\mu{}_\nu = \tfrac12\big(\bar\Phi\gamma^\mu D_\nu\Phi
    - (D_\nu\bar\Phi)\gamma^\mu\Phi\big),\qquad
    L = \sum_\mu K^\mu{}_\mu - mS - U(S),$$

    where $K^{(\mu}{}_{\nu)}$ is the symmetrised kinetic tensor and $L$ the Lagrangian
    on shell (the record's formulas; $\sigma_T = +1$).

    **Status.** Every check below is an exact identity verified by computer algebra
    (PROVED for the stated inputs). ASSUMED: the sign convention $\sigma_T = +1$, the
    classical commuting field dirac16complex00 (not the quantised dirac16complex). The
    combination of a witness with the field equations for a history is new in this
    notebook; it is not a Revision record.
    """),
    md(r"""
    ## 5. The Revision records this notebook reproduces

    The next cell defines the helpers that read the Revision records: `read_json`
    reads a JSON file of the repository, `record_verdict` finds a check by its name in
    a report, and `reproduces` is a check that passes only when this notebook's own
    result holds AND the record lists the named check with the verdict PASS (it
    collects its two printed lines in a text buffer and prints them with one call, so
    that they always stay together in the output). It then prints the sentence of the
    record's document that this notebook answers.
    """),
    code(r'''
    import contextlib  # redirect_stdout: send printed lines into a buffer
    import io  # StringIO: a text buffer in memory

    GAMMAS = "Revision/algebra/gammas.json"  # the author's gamma matrices
    EQUATIONS = "Revision/field_equations_a4/a4-equations.json"  # the a4, b4 equations
    PY = "Revision/field_equations_a4/reports/python-a4-report.json"  # sympy record
    WL = "Revision/field_equations_a4/reports/wolfram-a4-report.json"  # Wolfram record
    EMT = "Revision/lead_checks/reports/emt-divergence-and-spin-connection.json"
    DOC = "Revision/docs/DIRAC16COMPLEX00_FIELD_THEORY.md"  # the record's document


    def read_json(relative):
        """Read a JSON file of the repository (a Revision record)."""
        return json.loads(repository_file(relative).read_text(encoding="utf-8"))


    def record_verdict(report_file, name):
        """The verdict of the check name in a report ("PASS"), None if absent."""
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


    OPEN_SENTENCE = ("this record contains no check that combines a witness with the "
                     "field equations for definite")
    document = repository_file(DOC).read_text(encoding="utf-8")
    say(f"{DOC} says: \"... {OPEN_SENTENCE} kappa, Lambda, m, lambda and a history.\"")
    check(OPEN_SENTENCE in document, "the record leaves this combination open")
    '''),
    md(r"""
    ## 6. The author's gamma matrices and the matrix $C$

    The next cell reads the eight gamma matrices from the Revision record
    `gammas.json` (each entry an integer or a fraction written as text, which
    `sp.Rational` turns into an exact number), checks the Clifford relation for all 64
    pairs, builds $C = \gamma^{(x_0)}\gamma^{(x_1)}\gamma^{(x_2)}\gamma^{(x_3)}$,
    compares it with the $C$ stored in the record, and checks the three properties the
    adjoint needs: $C$ is real and symmetric, $C^2 = 1$, and every $C\gamma^{(a)}$ is
    antisymmetric.
    """),
    code(r'''
    import itertools  # loops over all combinations of indices

    import numpy as np  # floating-point arrays, used only for the plots
    import sympy as sp  # exact algebra

    NAMES = ["x0", "x1", "x2", "x3", "x4", "x5", "x6", "x7"]  # positions 0..7
    ETA = [1, 1, 1, 1, -1, -1, -1, -1]  # the frame metric eta, x0..x7
    I16, Z16 = sp.eye(16), sp.zeros(16, 16)  # the 16 by 16 unit and zero matrices
    fixture = read_json(GAMMAS)
    gamma = [sp.Matrix([[sp.Rational(x) for x in row] for row in matrix])
             for matrix in fixture["gamma"]]  # gamma[a] = gamma^(xa)
    clifford = all(gamma[a] * gamma[b] + gamma[b] * gamma[a]
                   == 2 * ETA[a] * (1 if a == b else 0) * I16
                   for a in range(8) for b in range(8))
    reproduces(clifford, "the author's gammas satisfy the Clifford relation",
               PY, "authorT16_clifford")
    C = gamma[0] * gamma[1] * gamma[2] * gamma[3]  # C = g^(x0) g^(x1) g^(x2) g^(x3)
    stored_C = sp.Matrix([[sp.Rational(x) for x in row] for row in fixture["C"]])
    properties = (C == stored_C and C == C.T and C * C == I16
                  and all((C * g).T == -(C * g) for g in gamma))
    reproduces(properties, "C is the record's C, real symmetric, C^2 = 1, C gamma "
               "antisymmetric", PY, "authorT16_C_properties")
    '''),
    md(r"""
    ## 7. The spin connection of the corrected metric

    The vielbein of the diagonal corrected metric is diagonal, $e^a{}_\mu = E_a
    \delta^a_\mu$. The code writes it, for every real $z$, with $t = \tan z$,
    $w_z = (\sin^2 z)^{1/12} > 0$ and the jet variables `ea` $= e^{a_4}$, `q` $= b_4^{1/2}$,
    `ad1` $= a_4'$, `uu` $= u$: $E = (q/(e^{a_4}t),\ e^{a_4},\ e^{a_4},\ e^{a_4},\ 1,\
    qw_z/e^{a_4},\ qw_z/e^{a_4},\ qw_z/e^{a_4})$ ($1/t = \cot z$ keeps its sign). The
    derivatives use the chain rule: $\partial_4e^{a_4} = a_4'e^{a_4}$,
    $\partial_4 q = \tfrac12uq$, $\partial_4a_4' = a_4''$, $\partial_4u = v$, and
    $\partial_0 = 6H\partial_z$ with $\partial_zt = 1 + t^2$, $\partial_0w_z = Hw_z/t$.
    The canonical spin connection is
    $\omega_\mu{}^a{}_b = e^a{}_\nu(\partial_\mu e_b{}^\nu + \Gamma^\nu{}_{\mu\lambda}
    e_b{}^\lambda)$ with the inverse vielbein $e_b{}^\nu = \delta_b^\nu/E_b$. For
    $a = b$ the two terms cancel; for $a \ne b$ only the second survives:

    $$\omega_{\mu\,ab} = \eta_{aa}\,\omega_\mu{}^a{}_b
    = \eta_{aa}\,\frac{E_a}{E_b}\,\Gamma^a{}_{\mu b}\qquad(a \ne b),$$

    and $\Omega_\mu = \tfrac12\sum_{a,b}\omega_{\mu\,ab}S^{ab}$ with
    $S^{ab} = \tfrac14[\gamma^{(a)}, \gamma^{(b)}]$. The next cell computes the
    Christoffel symbols of the diagonal metric, the connection and the eight matrices
    $\Omega_\mu$ for arbitrary $a_4(x_4)$ and $b_4(x_4)$.
    """),
    code(r'''
    H = sp.symbols("H", positive=True)  # the constant H of the metric
    t = sp.symbols("t", real=True, nonzero=True)  # t = tan z, z = 6 H x0 real
    wz = sp.symbols("wz", positive=True)  # wz = (sin(z)^2)^(1/12)
    ea, q = sp.symbols("ea q", positive=True)  # ea = e^(a4), q = b4^(1/2)
    ad1, ad2, uu, vv = sp.symbols("ad1 ad2 uu vv", real=True)  # a4', a4'', u, v
    E = [q / (ea * t)] + [ea] * 3 + [sp.Integer(1)] + [q * wz / ea] * 3  # the vielbein
    g = [ETA[a] * E[a] ** 2 for a in range(8)]  # g_aa = eta_aa E_a^2
    RATE = {ea: ea * ad1, q: q * uu / 2, ad1: ad2, uu: vv}  # d/dx4 of each symbol


    def d(expr, mu):
        """The partial derivative with respect to the coordinate at position mu."""
        if mu == 4:
            return sum(sp.diff(expr, symbol) * rate for symbol, rate in RATE.items())
        if mu == 0:
            return 6 * H * (1 + t ** 2) * sp.diff(expr, t) + H * wz / t * sp.diff(expr, wz)
        return sp.Integer(0)  # nothing depends on x1, x2, x3, x5, x6, x7


    Gamma = [[[sp.Integer(0)] * 8 for _ in range(8)] for _ in range(8)]
    for a, b, c in itertools.product(range(8), repeat=3):  # diagonal-metric formula
        value = 0
        if a == c:
            value += d(g[a], b)
        if a == b:
            value += d(g[a], c)
        if b == c:
            value -= d(g[b], a)
        Gamma[a][b][c] = sp.cancel(value / (2 * g[a]))
    S_ab = [[(gamma[a] * gamma[b] - gamma[b] * gamma[a]) / 4 for b in range(8)]
            for a in range(8)]
    omega = [[[sp.cancel(ETA[a] * E[a] * Gamma[a][mu][b] / E[b]) if a != b else 0
               for b in range(8)] for a in range(8)] for mu in range(8)]
    antisymmetric = all(sp.cancel(omega[mu][a][b] + omega[mu][b][a]) == 0
                        for mu in range(8) for a in range(8) for b in range(8))
    reproduces(antisymmetric, "omega_mu ab = -omega_mu ba (canonical spin connection)",
               WL, "spin_connection_antisymmetric")
    Omega = [sum((omega[mu][a][b] * S_ab[a][b] / 2 for a in range(8) for b in range(8)
                  if omega[mu][a][b] != 0), Z16) for mu in range(8)]
    for mu in range(8):
        terms = sum(1 for a in range(8) for b in range(8) if omega[mu][a][b] != 0)
        say(f"Omega_{NAMES[mu]}: {terms} nonzero entries omega_mu ab")
    '''),
    md(r"""
    The next cell forms the curved-space gammas $\gamma^\mu = \gamma^{(\mu)}/E_\mu$
    (no sum) and checks three facts that the Revision record proved with the author's
    gammas: $\Omega_{x_4} = 0$ and $\Omega_{x_0} = \tfrac12\cot z\,e^{-a_4}b_4^{1/2}
    h_4\,\gamma^{(x_0)}\gamma^{(x_4)}$ with $h_4 = \tfrac12u - a_4'$;
    $\gamma^\mu\Omega_\mu + \Omega_\mu\gamma^\mu = 0$ for each $\mu$ separately; and
    the sum $\sum_\mu\gamma^\mu\Omega_\mu = \tfrac32He^{a_4}b_4^{-1/2}\gamma^{(x_0)} +
    (u - \tfrac12a_4')\gamma^{(x_4)}$, which contains no $z$.
    """),
    code(r'''
    gamma_curved = [gamma[mu] / E[mu] for mu in range(8)]  # gamma^mu = gamma^(mu)/E_mu
    h4 = uu / 2 - ad1  # the rate of the block (x0, x5, x6, x7)
    expected_x0 = (q / (2 * t * ea)) * h4 * gamma[0] * gamma[4]
    reproduces(Omega[4] == Z16
               and (Omega[0] - expected_x0).applyfunc(sp.cancel) == Z16,
               "Omega_x4 = 0, Omega_x0 = (1/2) cot z e^(-a4) b4^(1/2) h4 g^(x0) g^(x4)",
               PY, "authorT16_Omega_x4_zero_Omega_x0")
    anticommute = all((gamma_curved[mu] * Omega[mu] + Omega[mu] * gamma_curved[mu])
                      .applyfunc(sp.cancel) == Z16 for mu in range(8))
    reproduces(anticommute, "{gamma^mu, Omega_mu} = 0 for each mu (no sum)",
               PY, "authorT16_anticommutator_no_sum")
    gravity_term = sum((gamma_curved[mu] * Omega[mu] for mu in range(8)), Z16)
    gravity_term = gravity_term.applyfunc(sp.cancel)
    c_gravity = sp.Rational(3, 2) * H * ea / q  # (3/2) H e^(a4) b4^(-1/2)
    expected = c_gravity * gamma[0] + (uu - ad1 / 2) * gamma[4]
    same = (gravity_term - expected).applyfunc(sp.cancel) == Z16
    reproduces(same, "gamma^mu Omega_mu = (3/2) H e^(a4) b4^(-1/2) g^(x0) + (u - a4'/2) "
               "g^(x4)", PY, "authorT16_gravity_term")
    reproduces(same, "the same, the lead's independent check",
               EMT, "gamma_Omega_equals_hidden_block_terms")
    '''),
    md(r"""
    ## 8. The condensate equation and the density law

    For $\Phi = \Phi(x_4)$ only the $x_4$ derivative survives, and $\gamma^{x_4} =
    \gamma^{(x_4)}$ (because $E_4 = 1$). With the term of section 7 the field equation
    becomes $\gamma^{(x_4)}\Phi' + c\,\gamma^{(x_0)}\Phi + (u - \tfrac12a_4')
    \gamma^{(x_4)}\Phi = M\Phi$ with $c = \tfrac32He^{a_4}b_4^{-1/2}$. Multiplying by
    $-\gamma^{(x_4)}$ and using $(\gamma^{(x_4)})^2 = -1$:

    $$\Phi' = \mathcal{A}\Phi,\qquad \mathcal{A} = \mathcal{B} - (u - \tfrac12a_4')\,1,
    \qquad \mathcal{B} = -M\gamma^{(x_4)} + c\,\gamma^{(x_4)}\gamma^{(x_0)}.$$

    $\mathcal{A}$ contains no $z$. Squaring $\mathcal{B}$, with
    $(\gamma^{(x_4)})^2 = -1$, $(\gamma^{(x_0)})^2 = 1$ and
    $\gamma^{(x_4)}\gamma^{(x_0)} = -\gamma^{(x_0)}\gamma^{(x_4)}$, the mixed terms
    cancel and $\mathcal{B}^2 = (c^2 - M^2)\,1$. The part $-(u - \tfrac12a_4')$ of
    $\mathcal{A}$ is a multiple of the unit matrix: writing
    $\Phi = e^{a_4/2}b_4^{-1}\chi$ removes it, $\chi' = \mathcal{B}\chi$. The next cell
    checks the reduction, the square, and $C\mathcal{A} + \mathcal{A}^TC =
    -2(u - \tfrac12a_4')C$, which gives $S' = (a_4' - 2u)S$, so
    $S = e^{a_4}b_4^{-2}S_0$ for every solution.
    """),
    code(r'''
    MM = sp.symbols("M", real=True)  # the effective mass M = m + U'(S)
    B_sym = -MM * gamma[4] + c_gravity * gamma[4] * gamma[0]
    A_sym = B_sym - (uu - ad1 / 2) * I16
    reduced = (gamma[4] * A_sym + gravity_term - MM * I16).applyfunc(sp.cancel)
    reproduces(reduced == Z16 and not A_sym.has(t) and not A_sym.has(wz),
               "gamma^(x4) A + gamma^mu Omega_mu = M: the equation is Phi' = A Phi",
               PY, "authorT16_condensate_equation")
    check((B_sym * B_sym - (c_gravity ** 2 - MM ** 2) * I16).applyfunc(sp.cancel) == Z16,
          "B^2 = (c^2 - M^2), c = (3/2) H e^(a4) b4^(-1/2)")
    reproduces((C * A_sym + A_sym.T * C + 2 * (uu - ad1 / 2) * C).applyfunc(sp.expand)
               == Z16, "C A + A^T C = -2 (u - a4'/2) C: S = e^(a4) b4^(-2) S0",
               PY, "authorT16_condensate_S_law")
    '''),
    md(r"""
    **Oscillating or growing?** Where $c^2 < M^2$ the matrix $\mathcal{B}$ has the
    eigenvalues $\pm i\sqrt{M^2 - c^2}$ (each eight times) and $\chi$ oscillates
    locally with the frequency $\sqrt{M^2 - c^2}$; where $c^2 > M^2$ the eigenvalues
    are real, $\pm\sqrt{c^2 - M^2}$, and $\chi$ grows or decays. On the record history
    $a_4 = Hx_4$, $b_4 = e^{(4/3)Hx_4}$ the coefficient $c = \tfrac32He^{Hx_4/3}$
    grows, so for every mass the condensate stops oscillating at
    $x_4^{\star} = (3/H)\ln(2|M|/(3H))$. The next cell draws $c$ against the time with
    the values $|M| = 3, 5, 7$ (units $H = 1$), checks the eigenvalues of $\mathcal{B}$
    numerically at six times for $M = 5$, and draws the local frequency.
    """),
    code(r'''
    times = np.linspace(0.0, 6.0, 601)  # x4 in units 1/H
    c_history = 1.5 * np.exp(times / 3.0)  # c on the record history, H = 1
    B_numeric = sp.lambdify((MM, ea, q), B_sym.subs(H, 1), "numpy")
    deviations, counts = [], []
    for x_value in (0.0, 1.0, 2.0, 3.0, 4.0, 5.0):
        matrix = np.array(B_numeric(5.0, np.exp(x_value), np.exp(2.0 * x_value / 3.0)),
                          dtype=float)  # e^(a4) = e^(x4), b4^(1/2) = e^(2 x4/3)
        eigenvalues = np.linalg.eigvals(matrix)
        c_value = 1.5 * np.exp(x_value / 3.0)
        squared = c_value ** 2 - 25.0  # c^2 - M^2: each eigenvalue squared
        deviations.append(np.max(np.abs(eigenvalues ** 2 - squared)))
        counts.append(int(np.sum(eigenvalues.imag > 1e-9) + np.sum(eigenvalues.real > 1e-9)))
    say(f"largest deviation of an eigenvalue squared from c^2 - M^2: {max(deviations):.0e}")
    say(f"eigenvalues on the positive side, at x4 = 0, 1, ..., 5: {counts}")
    check(max(deviations) < 1e-9 and counts == [8] * 6,
          "M = 5: the 16 eigenvalues of B are +-sqrt(c^2 - M^2), eight of each sign")
    fig, (left, right) = plt.subplots(1, 2, figsize=(11.0, 4.2))
    left.plot(times, c_history, color="black", label="$c = \\frac{3}{2}e^{x_4/3}$")
    for mass, style in ((3.0, ":"), (5.0, "--"), (7.0, "-.")):
        left.axhline(mass, linestyle=style, color="tab:blue", label=f"$|M| = {mass:g}$")
        frequency = np.sqrt(np.maximum(mass ** 2 - c_history ** 2, 0.0))
        right.plot(times, frequency, style, label=f"$|M| = {mass:g}$")
    left.set_xlabel("time $x_4$ (units $1/H$)")
    left.set_ylabel("$c$ and $|M|$ (units $H$)")
    left.set_title("the hidden-direction coefficient grows")
    left.legend(fontsize=8)
    right.set_xlabel("time $x_4$ (units $1/H$)")
    right.set_ylabel("local frequency $\\sqrt{M^2 - c^2}$ (units $H$)")
    right.set_title("the condensate stops oscillating")
    right.legend(fontsize=8)
    save_figure(fig, "oscillation_threshold",
                "A homogeneous condensate of dirac16complex00 on the record history "
                "$a_4 = Hx_4$, $b_4 = e^{(4/3)Hx_4}$. Left: the coefficient "
                "$c = \\frac{3}{2}He^{a_4}b_4^{-1/2} = \\frac{3}{2}He^{Hx_4/3}$ of the "
                "hidden-direction term of the field equation (black), against the time "
                "$x_4$ in units of $1/H$, with the effective masses $|M| = 3H$, $5H$, "
                "$7H$ (blue lines). Right: the local frequency $\\sqrt{M^2 - c^2}$ of "
                "the condensate, which falls to zero where $c$ reaches $|M|$, at "
                "$x_4 = (3/H)\\ln(2|M|/(3H))$; after that the condensate grows or "
                "decays instead of oscillating, because the hidden direction shrinks.")
    '''),
    md(r"""
    ## 9. The witnesses: condensates whose 24 three-gamma bilinears vanish

    The record shows that the off-diagonal parts of the kinetic tensor of a condensate
    are combinations of 24 three-gamma bilinears
    $B_{abc} = \bar\Phi\gamma^{(a)}\gamma^{(b)}\gamma^{(c)}\Phi$: those with
    $\{a, b, c\} = \{x_0, i, x_4\}$ (3), $\{x_0, i, t\}$ (9), $\{i, x_4, t\}$ (9) and
    $\{x_0, x_4, t\}$ (3), with $i$ in 3-space and $t$ an extra time. The off-diagonal
    field equations $0 = \kappa T^\mu{}_\nu$ need all 24 to vanish. The record finds
    exact solutions on the histories with constant $k = e^{2a_4}/b_4 = k_0$: there
    $c = \tfrac32H\sqrt{k_0}$ is constant, and for $k_0 = 4$, $H = 1$, $c = 3$, so
    $\mathcal{B}$ is a constant matrix with the frequency $w = \sqrt{M^2 - 9}$; for
    $M = \pm5$, $w = 4$. The recipe: take the spinor $v_1$ with $\mathcal{B}v_1 =
    -iwv_1$ and $\gamma^{(x_1)}\gamma^{(x_5)} = \gamma^{(x_2)}\gamma^{(x_6)} =
    \gamma^{(x_3)}\gamma^{(x_7)} = -1$ on it, the spinor $v_2$ with the same frequency
    and the value $+1$, and $c_{12} = \overline{v_1^\dagger Cv_2}$ (the bar is the
    complex conjugate). Each is found as the null space (the solutions of a set of
    linear equations) of a stacked matrix. When $M$ and $c$ are multiplied by the same
    number, $\mathcal{B}$ and $w$ are multiplied by it too, so $v_1$ and $v_2$ depend
    only on the ratio $M/c$. We extend the recipe to the family

    $$\Phi_0(s) = v_1 + s\,c_{12}\,v_2\qquad(s \text{ any real number}),$$

    and the condensate is $\Phi(x_4) = e^{a_4/2}b_4^{-1}e^{-iwx_4}\Phi_0(s)$ on
    $b_4 = e^{2a_4}/4$. The next cell builds $v_1$, $v_2$ and $c_{12}$ at $M = -5$,
    checks that each null space is one-dimensional, that $\Phi_0(s)$ has the frequency
    $w$, and that the 24 bilinears vanish for EVERY real $s$ (sympy keeps $s$ as a
    symbol).
    """),
    code(r'''
    s = sp.symbols("s", real=True)  # the free real parameter of the family
    TRIPLES = list(itertools.combinations(range(8), 3))  # all 56 sets {a, b, c}
    NEEDED = sorted({tuple(sorted((0, i, 4))) for i in (1, 2, 3)}
                    | {tuple(sorted((0, i, j))) for i in (1, 2, 3) for j in (5, 6, 7)}
                    | {tuple(sorted((i, 4, j))) for i in (1, 2, 3) for j in (5, 6, 7)}
                    | {tuple(sorted((0, 4, j))) for j in (5, 6, 7)})


    def witness_parts(M_value, c_value=3):
        """v1, v2, c12, the frequency w and the matrix B of the record's recipe for the
        mass M_value and the constant c_value (c = 3 is k0 = 4 at H = 1)."""
        w_value = sp.sqrt(M_value ** 2 - c_value ** 2)
        B_value = -M_value * gamma[4] + c_value * gamma[4] * gamma[0]
        spaces = []
        for sign in (-1, 1):  # the value of g^(x1)g^(x5) = g^(x2)g^(x6) = g^(x3)g^(x7)
            stack = sp.Matrix.vstack(B_value + sp.I * w_value * I16,
                                     gamma[1] * gamma[5] - sign * I16,
                                     gamma[2] * gamma[6] - sign * I16,
                                     gamma[3] * gamma[7] - sign * I16)
            spaces.append(stack.nullspace())  # all solutions of stack * v = 0
        v1, v2 = spaces[0][0], spaces[1][0]
        c12 = sp.conjugate(sp.expand((v1.H * C * v2)[0]))  # conj(v1^dagger C v2)
        return spaces, v1, v2, c12, w_value, B_value


    def bilinear(phi, matrix):
        """The bilinear phibar matrix phi = phi^dagger C matrix phi."""
        return sp.expand((phi.H * C * matrix * phi)[0])


    def three_gamma(triple):
        a, b, c = triple
        return gamma[a] * gamma[b] * gamma[c]


    spaces, v1, v2, c12, w_minus, B_minus = witness_parts(-5)
    phi_s = (v1 + s * c12 * v2).applyfunc(sp.expand)  # the family Phi_0(s)
    check([len(space) for space in spaces] == [1, 1],
          "the two null spaces are one-dimensional (v1 and v2 are unique)")
    report("frequency w at M = -5 H, k0 = 4", w_minus, "H")
    check((B_minus * phi_s + sp.I * w_minus * phi_s).applyfunc(sp.expand)
          == sp.zeros(16, 1), "B Phi_0(s) = -i w Phi_0(s) for every s")
    needed_values = [bilinear(phi_s, three_gamma(triple)) for triple in NEEDED]
    check(len(NEEDED) == 24 and all(value == 0 for value in needed_values),
          "the 24 three-gamma bilinears vanish for every real s")
    '''),
    md(r"""
    **The density of the family.** $\Phi_0^\dagger C\Phi_0$ has four parts:
    $v_1^\dagger Cv_1$, $s^2|c_{12}|^2v_2^\dagger Cv_2$ and the two cross terms
    $s\,c_{12}\,v_1^\dagger Cv_2 + s\,\bar c_{12}\,v_2^\dagger Cv_1 =
    2s\,|v_1^\dagger Cv_2|^2$ (because $\bar c_{12} = v_1^\dagger Cv_2$ and
    $v_2^\dagger Cv_1$ is its complex conjugate, $C$ being real symmetric). The next
    cell finds the first two zero, so $\Phi_0^\dagger C\Phi_0 = 2s\,|v_1^\dagger
    Cv_2|^2$: the family contains condensates of every real density, positive for
    $s > 0$ and negative for $s < 0$. It also repeats the construction at $M = +5$,
    where the Revision record ran it with the author's gammas, and checks the record's
    statement there ($s = 1$: the 24 bilinears vanish, $S$ is real and not zero; the
    size of $S$ depends on the arbitrary normalisation of the null vectors).
    """),
    code(r'''
    S0_s = bilinear(phi_s, I16)  # Phi_0(s)^dagger C Phi_0(s)
    cross = sp.expand((v1.H * C * v2)[0])  # v1^dagger C v2
    report("v1^dagger C v2", cross)
    report("Phi_0(s)^dagger C Phi_0(s)", S0_s)
    check(bilinear(v1, I16) == 0 and bilinear(v2, I16) == 0
          and sp.expand(S0_s - 2 * s * cross * sp.conjugate(cross)) == 0,
          "Phi_0(s)^dagger C Phi_0(s) = 2 s |v1^dagger C v2|^2: every real density")
    _, u1, u2, c_plus, w_plus, B_plus = witness_parts(5)  # the record's M = +5
    phi_plus = (u1 + c_plus * u2).applyfunc(sp.expand)  # s = 1
    S_plus = bilinear(phi_plus, I16)
    ok_plus = ((B_plus * phi_plus + sp.I * w_plus * phi_plus).applyfunc(sp.expand)
               == sp.zeros(16, 1)
               and all(bilinear(phi_plus, three_gamma(tr)) == 0 for tr in NEEDED)
               and S_plus != 0 and sp.im(S_plus) == 0)
    report("M = +5: Phi_0^dagger C Phi_0 with this normalisation", S_plus)
    reproduces(ok_plus, "M = +5, k0 = 4: a witness with S real, not 0, 24 bilinears 0",
               PY, "authorT16_condensate_witness")
    reproduces(ok_plus and sp.im(S0_s) == 0 and S0_s.subs(s, 1) != 0,
               "M = -5 and M = +5 at k0 = 4, H = 1 (s = 1): exact witnesses",
               WL, "condensate_witness_constant_k_exact")
    '''),
    md(r"""
    The next cell computes all 56 three-gamma bilinears of $\Phi_0(1)$ (at $M = -5$),
    checks that each is a real number, and draws them: the 24 that the field equations
    need to vanish in red (all zero), the others in blue. The ones that do not vanish
    are built from three directions among $x_1, x_2, x_3, x_5, x_6, x_7$ only, and no
    field equation asks them to vanish.
    """),
    code(r'''
    phi_one = phi_s.subs(s, 1)  # Phi_0(1)
    all_values = [bilinear(phi_one, three_gamma(triple)) for triple in TRIPLES]
    check(all(sp.im(value) == 0 for value in all_values),
          "all 56 three-gamma bilinears of Phi_0(1) are real numbers")
    nonzero = [triple for triple, value in zip(TRIPLES, all_values) if value != 0]
    say("nonzero bilinears: " + ", ".join(
        "".join(NAMES[i][1] for i in triple) for triple in nonzero))
    check(all(4 not in triple and 0 not in triple for triple in nonzero),
          "every nonzero one avoids x4 and x0")
    labels = ["".join(NAMES[i][1] for i in triple) for triple in TRIPLES]
    numbers = np.array([float(value) for value in all_values])
    is_needed = np.array([triple in NEEDED for triple in TRIPLES])
    fig, ax = plt.subplots(figsize=(11.0, 4.2))
    positions = np.arange(len(TRIPLES))
    ax.bar(positions[~is_needed], numbers[~is_needed], color="tab:blue",
           label="other bilinears")
    ax.plot(positions[is_needed], numbers[is_needed], "x", color="tab:red",
            markersize=8, label="the 24 the field equations need to vanish")
    ax.axhline(0.0, color="black", linewidth=0.8)
    ax.set_xticks(positions)
    ax.set_xticklabels(labels, rotation=90, fontsize=6.5)
    ax.set_xlabel("directions $abc$ of $\\bar\\Phi\\gamma^{(a)}\\gamma^{(b)}"
                  "\\gamma^{(c)}\\Phi$ (digit $k$ for $x_k$)")
    ax.set_ylabel("value of the bilinear")
    ax.set_title("The 56 three-gamma bilinears of the witness $\\Phi_0(1)$, $M = -5H$")
    ax.legend(fontsize=8)
    save_figure(fig, "three_gamma_bilinears",
                "The 56 three-gamma bilinears $\\bar\\Phi\\gamma^{(a)}\\gamma^{(b)}"
                "\\gamma^{(c)}\\Phi$ of the witness $\\Phi_0(1) = v_1 + c_{12}v_2$ at "
                "$M = -5H$, $k_0 = 4$, $H = 1$, one for each set of three directions "
                "$a < b < c$ (horizontal axis, labelled by the digits of $x_0$ to $x_7$); "
                "vertical axis the exact value (a real number). Red crosses: the 24 "
                "bilinears whose vanishing the off-diagonal field equations require "
                "(they contain $x_0$ or $x_4$ together with directions of 3-space and "
                "the extra times); all are exactly zero. Blue bars: the other 32; the "
                "nonzero ones are built from 3-space directions and extra times only.")
    '''),
    md(r"""
    ## 10. The complete energy-momentum tensor of a witness

    On the histories $b_4 = e^{2a_4}/4$ (with an arbitrary function $a_4(x_4)$) we have
    $b_4^{1/2} = e^{a_4}/2$ and $u = 2a_4'$, $v = 2a_4''$; the witness is
    $\Phi = e^{a_4/2}b_4^{-1}e^{-iwx_4}\Phi_0 = 4e^{-3a_4/2}e^{-iwx_4}\Phi_0$, and
    every bilinear carries the factor $f^2 = 16e^{-3a_4}$ (the phase cancels). The
    next cell computes the kinetic tensor $K^\mu{}_\nu$ for every pair $(\mu, \nu)$ as
    $f^2\Phi_0^\dagger N^\mu{}_\nu\Phi_0$, with the matrix
    $N^\mu{}_\nu = \tfrac12(C\gamma^\mu\mathcal{D}_\nu - \bar{\mathcal{D}}_\nu
    \gamma^\mu)$, where $\mathcal{D}_\nu = \mathcal{A}\delta_{\nu 4} + \Omega_\nu$ acts
    on $\Phi$ ($\Phi' = \mathcal{A}\Phi$) and $\bar{\mathcal{D}}_\nu =
    \mathcal{A}^TC\delta_{\nu 4} - C\Omega_\nu$ on $\bar\Phi$. It works for the whole
    family (symbol $s$), every $a_4$, $a_4'$ and every $z$, at $H = 1$. Then it
    symmetrises, $K^{(\mu}{}_{\nu)} = \tfrac12\big(K^\mu{}_\nu + (g_{\nu\nu}/g_{\mu\mu})
    K^\nu{}_\mu\big)$, and checks the record's statements: every off-diagonal component
    vanishes; on the diagonal only $K^{x_4}{}_{x_4} = MS$ survives, with
    $S = f^2\Phi_0^\dagger C\Phi_0$. It also counts the record's list of the
    off-diagonal kinetic components of a general condensate: 36 ordered pairs, built
    from the 24 bilinears.
    """),
    code(r'''
    ON_FAMILY = {q: ea / 2, uu: 2 * ad1, vv: 2 * ad2, H: 1}  # b4 = e^(2 a4)/4
    Omega_w = [matrix.subs(ON_FAMILY) for matrix in Omega]
    gamma_w = [matrix.subs(ON_FAMILY) for matrix in gamma_curved]
    g_w = [entry.subs(ON_FAMILY) for entry in g]
    A_w = B_minus - sp.Rational(3, 2) * ad1 * I16  # A = B - (u - a4'/2), u = 2 a4'
    factor = 16 / ea ** 3  # f^2 = (e^(a4/2)/b4)^2 = 16 e^(-3 a4)


    def D_phi(nu):
        """The matrix that gives D_nu Phi from Phi."""
        return (A_w if nu == 4 else Z16) + Omega_w[nu]


    def D_phibar(nu):
        """The matrix that gives D_nu Phibar from Phi^dagger (row times matrix)."""
        return (A_w.T * C if nu == 4 else Z16) - C * Omega_w[nu]


    K = [[factor * (phi_s.H * ((C * gamma_w[mu] * D_phi(nu) - D_phibar(nu) * gamma_w[mu])
                               / 2) * phi_s)[0] for nu in range(8)] for mu in range(8)]
    K_sym = [[sp.cancel(sp.expand((K[mu][nu] + (g_w[nu] / g_w[mu]) * K[nu][mu]) / 2))
              for nu in range(8)] for mu in range(8)]
    S_family = sp.expand(factor * S0_s)  # S = 16 e^(-3 a4) Phi_0^dagger C Phi_0
    off_diagonal = all(K_sym[mu][nu] == 0 for mu in range(8) for nu in range(8)
                       if mu != nu)
    diagonal = [K_sym[mu][mu] for mu in range(8)]
    say(f"diagonal of K: {diagonal}")
    reproduces(off_diagonal and all(diagonal[mu] == 0 for mu in range(8) if mu != 4)
               and sp.expand(diagonal[4] - (-5) * S_family) == 0,
               "witness: K^x4_x4 = M S, every other component of K is 0 (every a4, z)",
               PY, "authorT16_condensate_kinetic_diagonal")
    offdiagonal_record = read_json(EQUATIONS)["fields"]["dirac16complex00"]
    offdiagonal_record = offdiagonal_record["offDiagonalKinetic"]
    bilinear_names = sorted({term["bilinear"] for entry in offdiagonal_record
                             for term in entry["terms"]})
    report("record: off-diagonal kinetic components, distinct bilinears",
           f"{len(offdiagonal_record)}, {len(bilinear_names)}")
    reproduces(len(offdiagonal_record) == 36 and len(bilinear_names) == 24,
               "a general condensate: 36 off-diagonal components, 24 bilinears",
               WL, "condensate_offdiagonal_are_three_gamma_bilinears")
    '''),
    md(r"""
    With $\sigma_T = +1$ the energy-momentum tensor is $T^\mu{}_\nu =
    -K^{(\mu}{}_{\nu)} + \delta^\mu_\nu L$ with $L = \sum_\mu K^\mu{}_\mu - mS - U(S)$.
    The trace of the kinetic tensor is $MS$, and $M = m + U'(S)$, so
    $L = SU'(S) - U(S)$ and

    $$\rho = -T^{x_4}{}_{x_4} = MS - L = mS + U(S),\qquad
    p_3 = p_t = p_0 = L = SU'(S) - U(S),\qquad \rho + p = MS,$$

    the formulas of the Revision record. A witness has a constant $M$. If $a_4$
    changes, $S$ changes, so $U' = M - m$ is constant on the range of $S$ and
    $U = (M - m)S + U_0$: then $p = -U_0$ and $\rho = MS + U_0$, and the constant $U_0$
    acts exactly like a change of $\Lambda$ by $\kappa U_0$. If $a_4$ is constant, $S$
    is constant, and $\rho$ and $p$ are constants with $\rho + p = MS$. In every case a
    witness is, up to a change of $\Lambda$, a pressureless source (like dust) with
    $\rho = MS$ and no mixed component. The next cell builds the tensor with $U = 0$
    (so $m = M = -5$), checks these formulas, and checks that this source is conserved
    on every history of the family: there $h_4 = \tfrac12u - a_4' = 0$, and the
    conservation law of Notebook 12a reduces to $\partial_4\rho + 3a_4'\rho = 0$, which
    $\rho \propto S \propto e^{-3a_4}$ obeys.
    """),
    code(r'''
    m = sp.symbols("m", real=True)  # the mass; with U = 0, m = M = -5 here
    L_witness = sp.expand(sum(diagonal) - m * S_family)  # L = trace K - m S - U, U = 0
    T_witness = [[sp.expand(-K_sym[mu][nu] + (L_witness if mu == nu else 0))
                  for nu in range(8)] for mu in range(8)]
    on_shell = {m: -5}  # M = m for U = 0
    rho_witness = sp.expand(-T_witness[4][4].subs(on_shell))
    pressures = [sp.expand(T_witness[mu][mu].subs(on_shell)) for mu in range(8) if mu != 4]
    check(sp.expand(sum(diagonal) - (-5) * S_family) == 0
          and sp.expand(rho_witness - (-5) * S_family) == 0
          and all(p == 0 for p in pressures),
          "witness: trace K = M S, rho = M S, all seven pressures 0 (pressureless)")
    check(sp.expand(d(rho_witness, 4) + 3 * ad1 * rho_witness) == 0,
          "witness: d4 rho + 3 a4' rho = 0, the source is conserved on the family")
    '''),
    md(r"""
    ## 11. Can a witness be the source of a history of its family?

    On the family $b_4 = e^{2a_4}/k_0$ we have $u = 2a_4'$, $v = 2a_4''$ and $k = k_0$;
    write $e_{\mu\mu}$ for the components of $\sum_k\alpha_kE_{(k)}$ there. With the
    source of a witness ($\rho = MS$, all pressures zero, any $\Lambda$) the field
    equations are

    $$e_{44} + \Lambda = -\kappa MS,\qquad e_{11} + \Lambda = 0,\qquad
    e_{00} + \Lambda = 0 .$$

    **Einstein gravity.** There $e_{11} = -3(a_4')^2 - 2a_4'' + 6H^2k_0$ and
    $e_{00} = -6(a_4')^2 - 3a_4'' + 3H^2k_0$. Three times the 3-space equation minus
    twice the hidden equation removes $a_4''$: $3(a_4')^2 + 12H^2k_0 + \Lambda = 0$.
    So $a_4'$ is constant and $a_4'' = 0$; the 3-space equation then needs
    $\Lambda = -9H^2k_0$, and $(a_4')^2 = -H^2k_0 < 0$: no history of the family has
    zero pressures, and no witness, of any density, fits.

    **The author's couplings** $\alpha_1 = 1$, $\alpha_2 = 1/(32H^2)$,
    $\alpha_3 = 1/(1152H^4)$, with any $\Lambda$. The 3-space and hidden equations are
    linear in $a_4''$. The 3-space equation times the $a_4''$-coefficient of the hidden
    one, minus the hidden equation times the $a_4''$-coefficient of the 3-space one,
    leaves a polynomial $P = c_4(a_4')^4 + c_2(a_4')^2 + c_0$ that vanishes at every
    time. Two cases:

    1. $P$ is not the zero polynomial. Then $a_4'$ takes only finitely many values, so
       (being continuous) it is constant and $a_4'' = 0$: an exponential history with
       $\beta = 2$ or a static one. There the part $(x_1, \dots, x_4)$ of the metric is
       de Sitter space or flat space, $e_{44} = e_{11}$, and the difference of the
       first two equations gives $\kappa MS = 0$.
    2. $P$ is the zero polynomial, $c_4 = c_2 = c_0 = 0$. The cell finds that this
       happens only for $k_0 = 6 \pm 2\sqrt5$ with $\Lambda = -\tfrac32H^2(k_0 + 4)$,
       and that there $e_{44} + \Lambda = 0$ for every $a_4$: again $\kappa MS = 0$.

    In both cases $S = 0$: a witness with nonzero density is the source of no history
    of its family. A by-product of case 2: at those two values the time and 3-space
    equations hold for every $a_4$ and the hidden one is a second-order equation for
    $a_4$, so the family contains vacua that are not exponential (with the author's
    $\Lambda = -10$ they do not occur). The next cell does this algebra with the
    Lovelock components of the Revision record.
    """),
    code(r'''
    record = read_json(EQUATIONS)
    kk, k0, Lam, y = sp.symbols("kk k0 Lam y", real=True)  # y stands for a4'^2
    a1, a2, a3 = sp.symbols("alpha1 alpha2 alpha3", real=True)
    LOCALS = {"H": H, "ad1": ad1, "ad2": ad2, "uu": uu, "vv": vv, "kk": kk}
    lovelock = record["lovelockTensors"]
    weights = {1: a1, 2: a2, 3: a3}
    side = {key: sum(weights[k] * sp.sympify(lovelock[f"E{k}"][key]["input"]
                                             .replace("^", "**"), locals=LOCALS)
                     for k in (1, 2, 3)) for key in ("x4x4", "x1x1", "x0x0")}
    FAMILY = {uu: 2 * ad1, vv: 2 * ad2, kk: k0}  # b4 = e^(2 a4)/k0
    EINSTEIN = {a1: 1, a2: 0, a3: 0}
    AUTHOR = {a1: 1, a2: sp.Rational(1, 32) / H ** 2, a3: sp.Rational(1, 1152) / H ** 4}


    def on_family(key, couplings):
        """The component key of sum_k alpha_k E_(k) on the family b4 = e^(2 a4)/k0."""
        return sp.expand(side[key].subs(FAMILY).subs(couplings))


    def eliminant(couplings):
        """P: the 3-space and hidden equations combined so that a4'' drops out."""
        x1_eq = on_family("x1x1", couplings) + Lam
        x0_eq = on_family("x0x0", couplings) + Lam
        return sp.expand(sp.diff(x0_eq, ad2) * x1_eq - sp.diff(x1_eq, ad2) * x0_eq)


    e44, e11, e00 = (on_family(key, EINSTEIN) for key in ("x4x4", "x1x1", "x0x0"))
    say(f"Einstein on the family: e44 = {e44}, e11 = {e11}, e00 = {e00}")
    P_einstein = eliminant(EINSTEIN)
    y_value = sp.solve(P_einstein.subs(ad1 ** 2, y), y)[0]  # a4'^2: a constant
    Lam_value = sp.solve((e11 + Lam).subs({ad2: 0, ad1 ** 2: y_value}), Lam)[0]
    final = sp.expand(y_value.subs(Lam, Lam_value))
    say(f"Einstein: P = {P_einstein}, so a4'^2 = {y_value} is constant and a4'' = 0; "
        f"the 3-space equation then needs Lambda = {Lam_value}, and a4'^2 = {final}")
    check(not P_einstein.has(ad2) and final == -H ** 2 * k0,
          "Einstein: no history b4 = e^(2 a4)/k0 has zero pressures (a4'^2 = -H^2 k0)")
    P_author = eliminant(AUTHOR)
    c4, c2, c0 = (P_author.coeff(ad1, n) for n in (4, 2, 0))
    shape = (not P_author.has(ad2) and sp.Poly(P_author, ad1).degree() == 4
             and P_author.coeff(ad1, 3) == 0 and P_author.coeff(ad1, 1) == 0)
    say(f"the author's couplings: c4 = {sp.factor(c4)}")
    say(f"c2 = {sp.factor(c2)}")
    say(f"c0 = {sp.factor(c0)}")
    zeros_c4 = sp.solve(c4, k0)
    say(f"c4 = 0 at k0 = {zeros_c4}")
    degenerate = len(zeros_c4) == 3
    for root in zeros_c4:
        c2_root = sp.simplify(c2.subs(k0, root))
        if not c2_root.has(Lam):
            say(f"k0 = {root}: c2 = {c2_root}, so P is not the zero polynomial")
            degenerate = degenerate and c2_root != 0
            continue
        Lam_root = sp.radsimp(sp.solve(c2_root, Lam)[0])  # c2 = 0 fixes Lambda
        c0_root = sp.simplify(sp.expand(c0.subs({k0: root, Lam: Lam_root})))
        time_eq = sp.simplify(sp.expand(on_family("x4x4", AUTHOR).subs(k0, root)
                                        + Lam_root))
        space_eq = sp.simplify(sp.expand(on_family("x1x1", AUTHOR).subs(k0, root)
                                         + Lam_root))
        say(f"k0 = {root}: c2 = 0 needs Lambda = {Lam_root}; there c0 = {c0_root}, "
            f"e44 + Lambda = {time_eq}, e11 + Lambda = {space_eq}")
        degenerate = (degenerate and c0_root == 0 and time_eq == 0 and space_eq == 0
                      and sp.simplify(Lam_root + sp.Rational(3, 2) * H ** 2 * (root + 4))
                      == 0)
    check(shape and degenerate, "the author's couplings: P = 0 identically only at "
          "k0 = 6 +- 2 sqrt 5, Lambda = -(3/2) H^2 (k0 + 4), where e44 + Lambda = 0")
    equal = all(sp.expand((on_family("x4x4", couplings) - on_family("x1x1", couplings))
                          .subs(ad2, 0)) == 0 for couplings in (EINSTEIN, AUTHOR))
    check(equal, "Einstein and the author's couplings: e44 = e11 where a4'' = 0 on the "
          "family (beta = 2 or static), so kappa M S = 0 there")
    '''),
    md(r"""
    The next cell draws a witness in time on the history $a_4 = Hx_4$,
    $b_4 = e^{2Hx_4}/4$ (so the block does not shrink): on the left the real and the
    imaginary part of the largest component of
    $\Phi(x_4) = 4e^{-3x_4/2}e^{-4ix_4}\Phi_0(1)$, which oscillate with the period
    $2\pi/4$ and decay, and the density
    $S = 16e^{-3x_4}\Phi_0^\dagger C\Phi_0$; on the right, on a logarithmic axis, the
    scale factor $e^{a_4}$ of 3-space and the constant $e^{-a_4}b_4^{1/2} = \tfrac12$ of
    the hidden direction and the extra times. It checks $S(x_4)$ numerically from the
    spinor at every plotted time.
    """),
    code(r'''
    phi_numbers = np.array([complex(entry) for entry in phi_one])
    C_numbers = np.array(C.tolist(), dtype=float)
    biggest = int(np.argmax(np.abs(phi_numbers)))  # the largest component (first one)
    times = np.linspace(0.0, 3.0, 601)  # x4 in units 1/H
    S0_one = float(S0_s.subs(s, 1))
    density = []
    for x_value in times:  # S from the numbers, at every time
        phi_x = 4.0 * np.exp(-1.5 * x_value) * np.exp(-4j * x_value) * phi_numbers
        density.append((phi_x.conj() @ C_numbers @ phi_x).real)
    density = np.array(density)
    check(np.allclose(density, 16.0 * np.exp(-3.0 * times) * S0_one, rtol=1e-12,
                      atol=0.0), "witness on a4 = x4: S(x4) = 16 e^(-3 x4) S0 numerically")
    fig, (left, right) = plt.subplots(1, 2, figsize=(11.0, 4.2))
    component = 4.0 * np.exp(-1.5 * times) * np.exp(-4j * times) * phi_numbers[biggest]
    left.plot(times, component.real, label=f"Re $\\Phi_{{{biggest + 1}}}$")
    left.plot(times, component.imag, "--", label=f"Im $\\Phi_{{{biggest + 1}}}$")
    left.plot(times, density / abs(S0_one), color="black", linewidth=2.0,
              label="$S/|\\Phi_0^\\dagger C\\Phi_0|$")
    left.set_xlabel("time $x_4$ (units $1/H$)")
    left.set_ylabel("value")
    left.set_title("the witness oscillates and decays")
    left.legend(fontsize=8)
    right.semilogy(times, np.exp(times), color="tab:orange", label="3-space $e^{a_4}$")
    right.semilogy(times, 0.5 * np.ones_like(times), "--", color="tab:blue",
                   label="block $e^{-a_4}b_4^{1/2} = 1/2$")
    right.set_xlabel("time $x_4$ (units $1/H$)")
    right.set_ylabel("scale factor")
    right.set_title("on its history the block does not shrink")
    right.legend(fontsize=8)
    save_figure(fig, "witness_in_time",
                "A witness of the record on the history $a_4 = Hx_4$, "
                "$b_4 = e^{2Hx_4}/4$ (constant $k = 4$), as a function of the time "
                "$x_4$ in units of $1/H$. Left: the real and the imaginary part of the "
                "largest component of $\\Phi(x_4) = 4e^{-3x_4/2}e^{-4ix_4}\\Phi_0(1)$, "
                "which oscillate with the period $2\\pi/4$ and decay, and the density "
                "$S = 16e^{-3x_4}\\Phi_0^\\dagger C\\Phi_0$ divided by "
                "$|\\Phi_0^\\dagger C\\Phi_0|$ (black). Right, on a logarithmic axis: "
                "the scale factor $e^{a_4}$ of 3-space inflates, while the factor "
                "$e^{-a_4}b_4^{1/2} = 1/2$ of the hidden direction and the extra times "
                "stays constant: the witnesses live on histories that do not deflate.")
    '''),
    md(r"""
    The next cell draws, for the exponential member $a_4 = Hx_4$ of the family
    ($b_4 = e^{2Hx_4}/4$, Einstein gravity, $H = \kappa = 1$), the left-hand side
    $G^\mu{}_\nu + \Lambda\delta^\mu_\nu$ with $\Lambda = -21$ (chosen so that the
    3-space equation holds), the right-hand side $\kappa T^\mu{}_\nu$ of a witness, and
    their difference: the time component would need $\kappa MS = 0$, and the four
    components of the hidden direction and the extra times miss by $-15$.
    """),
    code(r'''
    member = {ad1: 1, ad2: 0, H: 1, k0: 4}  # a4 = x4 on the family with k0 = 4
    G_member = {key: sp.expand(side[key].subs(FAMILY).subs(EINSTEIN).subs(member))
                for key in ("x4x4", "x1x1", "x0x0")}
    LAMBDA_MEMBER = -21  # makes the 3-space equation hold
    G_diag = [G_member["x0x0"]] + [G_member["x1x1"]] * 3 + [G_member["x4x4"]] \
        + [G_member["x0x0"]] * 3
    left_side = np.array([[float(G_diag[mu] + LAMBDA_MEMBER) if mu == nu else 0.0
                           for nu in range(8)] for mu in range(8)])
    right_side = np.zeros((8, 8))  # p3 = p0 = p_t = 0 for a witness
    right_side[4, 4] = -1.0  # -kappa rho with kappa M S = 1 at the moment drawn
    difference = left_side - right_side
    say(f"G + Lambda on the diagonal: {[float(v) for v in np.diag(left_side)]}")
    check(np.allclose(np.diag(difference)[[0, 5, 6, 7]], -15.0)
          and np.allclose(np.diag(difference)[[1, 2, 3]], 0.0),
          "a4 = x4, k0 = 4, Lambda = -21: the block components miss by -15")
    fig, axes = plt.subplots(1, 3, figsize=(12.0, 4.4))
    scale = 22.0
    panels = ((left_side, "$G^\\mu{}_\\nu + \\Lambda\\delta^\\mu_\\nu$"),
              (right_side, "$\\kappa T^\\mu{}_\\nu$ of a witness"),
              (difference, "difference"))
    for ax, (values, title) in zip(axes, panels):
        ax.imshow(values, cmap="RdBu_r", vmin=-scale, vmax=scale)
        for mu in range(8):
            value = values[mu, mu]
            ink = "white" if abs(value) > 0.6 * scale else "black"  # readable on dark
            ax.text(mu, mu, f"{value:.0f}", ha="center", va="center", fontsize=7,
                    color=ink)
        ax.set_xticks(range(8))
        ax.set_xticklabels(NAMES, fontsize=7)
        ax.set_yticks(range(8))
        ax.set_yticklabels(NAMES, fontsize=7)
        ax.grid(False)
        ax.set_title(title, fontsize=9)
    fig.suptitle("Einstein gravity, $a_4 = Hx_4$, $b_4 = e^{2Hx_4}/4$: a witness is not "
                 "the source")
    save_figure(fig, "tensor_mismatch",
                "Einstein gravity on the member $a_4 = Hx_4$, $b_4 = e^{2Hx_4}/4$ of the "
                "witnesses' family (units $H = \\kappa = 1$), with $\\Lambda = -21$ chosen "
                "so that the 3-space equation holds: left, the left-hand side "
                "$G^\\mu{}_\\nu + \\Lambda\\delta^\\mu_\\nu$ (diagonal $-15$, $0$, $0$, "
                "$0$, "
                "$0$, $-15$, $-15$, $-15$ in the order $x_0$ to $x_7$); middle, the "
                "right-hand side $\\kappa T^\\mu{}_\\nu$ of a witness, pressureless, with "
                "$-\\kappa\\rho = -\\kappa MS$ drawn as $-1$; right, their difference. The "
                "hidden direction and the extra times miss by $-15$, and the time "
                "component would need $\\kappa MS = 0$: the field equations fail.")
    '''),
    md(r"""
    The next cell draws the reason in time for the same member: the energy density
    that the history requires, $\kappa\rho = -(e_{44} + \Lambda)$, is constant (here
    with $\Lambda = -21$ it is $0$; for other $\Lambda$ another constant), while a
    witness supplies $\kappa\rho = \kappa MS \propto e^{-3Hx_4}$, which falls; and the
    hidden pressure that the history requires, $\kappa p_0 = e_{00} + \Lambda = -15$,
    against the witness's $p_0 = 0$.
    """),
    code(r'''
    required_rho = float(-(G_member["x4x4"] + LAMBDA_MEMBER))
    required_p0 = float(G_member["x0x0"] + LAMBDA_MEMBER)
    report("member a4 = x4, k0 = 4, Lambda = -21: required kappa rho, kappa p0",
           f"{required_rho:g}, {required_p0:g}")
    fig, ax = plt.subplots()
    ax.plot(times, required_rho * np.ones_like(times), color="black",
            label=f"required $\\kappa\\rho = {required_rho:g}$ (constant)")
    for scale_value, style in ((1.0, "--"), (5.0, ":")):
        ax.plot(times, scale_value * np.exp(-3.0 * times), style, color="tab:blue",
                label=f"witness $\\kappa\\rho = \\kappa MS$, "
                f"$\\kappa MS(0) = {scale_value:g}$")
    ax.plot(times, required_p0 * np.ones_like(times) / 5.0, "-.", color="tab:red",
            label="required $\\kappa p_0/5 = -3$ (witness: $0$)")
    ax.axhline(0.0, color="grey", linewidth=0.8)
    ax.set_xlabel("time $x_4$ (units $1/H$)")
    ax.set_ylabel("units $H^2$")
    ax.set_title("What the history needs and what a witness supplies")
    ax.legend(fontsize=8)
    save_figure(fig, "witness_versus_required",
                "Einstein gravity on the member $a_4 = Hx_4$, $b_4 = e^{2Hx_4}/4$ of the "
                "witnesses' family, $\\Lambda = -21$, units $H = \\kappa = 1$, against the "
                "time $x_4$ in units of $1/H$: the energy density that the history "
                "requires is constant (black, here 0), while a witness supplies "
                "$\\kappa\\rho = \\kappa MS \\propto e^{-3x_4}$ (blue, for two starting "
                "values); the hidden pressure that the history requires is "
                "$\\kappa p_0 = -15$ (red, drawn divided by 5), while a witness has "
                "$p_0 = 0$. A constant requirement and a falling supply can agree at "
                "most at one moment.")
    '''),
    md(r"""
    The last picture shows where witnesses of the record's form exist. On the histories
    with constant $k_0$ the coefficient is $c = \tfrac32H\sqrt{k_0}$ and the frequency
    $w = \sqrt{M^2 - c^2} = \sqrt{M^2 - \tfrac94H^2k_0}$; the recipe needs
    $M^2 > \tfrac94H^2k_0$. The record ran it at $(M, H, k_0) = (\pm5, 1, 4)$ and
    $(5, \tfrac43, 4)$, that is at $M/H = \pm5$ and $3.75$ with $k_0 = 4$ and
    $w/H = 4$ and $2.25$. The next cell runs the recipe at three more pairs
    $(M, c) = (5, 4)$, $(13, 5)$, $(13, 12)$ ($H = 1$; integer frequencies $3$, $12$,
    $5$, so the arithmetic stays exact) and checks that the null spaces are
    one-dimensional, the 24 bilinears vanish and $S \ne 0$ there too. It then draws $w$
    against $k_0$ for $|M| = 3.75H$, $5H$ and $13H$ with the record's points and these
    three.
    """),
    code(r'''
    more = []  # (M, c, k0, w, the witness works)
    for M_value, c_value in ((5, 4), (13, 5), (13, 12)):
        spaces_m, p1, p2, c_m, w_m, B_m = witness_parts(M_value, c_value)
        phi_m = (p1 + c_m * p2).applyfunc(sp.expand)
        works = ([len(space) for space in spaces_m] == [1, 1]
                 and (B_m * phi_m + sp.I * w_m * phi_m).applyfunc(sp.expand)
                 == sp.zeros(16, 1)
                 and all(bilinear(phi_m, three_gamma(tr)) == 0 for tr in NEEDED)
                 and bilinear(phi_m, I16) != 0)
        k0_m = sp.Rational(4, 9) * c_value ** 2  # c = (3/2) sqrt(k0) at H = 1
        more.append((M_value, c_value, k0_m, w_m, works))
        say(f"M = {M_value}, c = {c_value} (k0 = {k0_m}): w = {w_m}, witness: {works}")
    check(all(entry[4] for entry in more),
          "(M, c) = (5, 4), (13, 5), (13, 12): witnesses, 24 bilinears 0, S not 0")
    k_values = np.linspace(0.0, 80.0, 801)
    fig, ax = plt.subplots()
    for mass, style in ((3.75, ":"), (5.0, "-"), (13.0, "--")):
        frequency = np.sqrt(np.maximum(mass ** 2 - 2.25 * k_values, 0.0))
        ax.plot(k_values, frequency, style, label=f"$|M| = {mass:g}H$")
    ax.plot([4.0, 4.0], [4.0, 2.25], "o", color="black", label="the record's witnesses")
    ax.plot([float(entry[2]) for entry in more], [float(entry[3]) for entry in more],
            "s", color="tab:red", label="witnesses of this notebook")
    ax.set_xlabel("$k_0 = e^{2a_4}/b_4$ (constant)")
    ax.set_ylabel("frequency $w$ (units $H$)")
    ax.set_title("Where witnesses of the record's form exist")
    ax.legend(fontsize=8)
    save_figure(fig, "witness_frequency",
                "The frequency $w = \\sqrt{M^2 - \\frac{9}{4}H^2k_0}$ of the condensates "
                "on the histories with constant $k = k_0$, against $k_0$, for the "
                "effective masses $|M| = 3.75H$, $5H$ and $13H$; a witness of the "
                "record's form oscillates only where $M^2 > \\frac{9}{4}H^2k_0$. Black "
                "points: the record's witnesses at $k_0 = 4$ ($M = \\pm 5H$, $w = 4H$; "
                "$M = 3.75H$, $w = 2.25H$). Red squares: the witnesses built in this "
                "notebook at $(M, c) = (5, 4)$, $(13, 5)$ and $(13, 12)$ with $H = 1$. "
                "Every one of these histories keeps the hidden direction and the extra "
                "times at the constant size $k_0^{-1/2}$.")
    '''),
    md(r"""
    ## 12. What this shows, and what it does not

    - **PROVED here (exact; a computation of this notebook, not a Revision record):** a
      witness (a homogeneous condensate of dirac16complex00 with all 24 three-gamma
      bilinears zero, on a history $b_4 = e^{2a_4}/k_0$) has a diagonal
      energy-momentum tensor that is, up to a change of $\Lambda$, pressureless, with
      $\rho = MS$, $S \propto e^{-3a_4}$, and conserved. In Einstein gravity no history
      of the family has zero pressures, so no witness fits; with the author's couplings
      $\alpha_1, \alpha_2, \alpha_3$ and any $\Lambda$, a witness with $S \ne 0$ is the
      source of no history of its family. This answers, for these witnesses and these
      couplings, the combination that the Revision record leaves open.
    - **PROVED here, a by-product:** with the author's couplings, at
      $k_0 = 6 \pm 2\sqrt5$ and $\Lambda = -\tfrac32H^2(k_0 + 4)$, the time and 3-space
      equations hold on every history of the family, so the family contains vacua
      that are not exponential.
    - **PROVED in the record (reproduced):** the gravity term, the condensate equation,
      the density law $S = e^{a_4}b_4^{-2}S_0$, the diagonal kinetic tensor, the 24
      bilinears and the witnesses at $k_0 = 4$; and (Notebook 12b) that a condensate
      has equal pressures, which no exponential history allows in Einstein gravity, and
      that no condensate is the source of the record history.
    - **ASSUMED:** the record's sign convention $\sigma_T = +1$; the classical
      commuting field dirac16complex00, not the quantised dirac16complex; $U = 0$ for
      the witnesses (shown above to cost nothing but a change of $\Lambda$).
    - **OPEN:** condensates on histories whose $k$ is not constant (the record: not
      decided), and so whether any field of the theory drives the deflation of the
      extra times exactly; the condensate sources that the record allows with the
      author's weights on $\beta = 2$ need $M = 0$, where the recipe of the witnesses
      does not apply, and whether their 24 bilinears can vanish is not decided.
    - **History:** the exact solutions of the earlier version of this notebook belonged
      to the metric of 2026-10-14, withdrawn on 2026-10-16; they are not used here.
    - **Not shown:** anything about stability, about how such a condensate could arise,
      about the quantised field, or about the creation of universes.
    """),
    md(r"""
    ## 13. The last check

    The last cell checks that the six figure files exist in the folder
    Revision/textbook/figures and prints the number of checks that passed.
    """),
    code(r'''
    figure_names = ["oscillation_threshold", "three_gamma_bilinears", "witness_in_time",
                    "tensor_mismatch", "witness_versus_required", "witness_frequency"]
    paths = [output_file(f"{FIGURE_FOLDER}/12d_{k}_{name}.png")
             for k, name in enumerate(figure_names, 1)]
    check(all(path.is_file() for path in paths), "all six figure files exist")
    all_checks_passed()
    '''),
    md(r"""
    ## 14. What this notebook showed

    - With the author's gammas, the spin connection of the corrected metric gives
      $\sum_\mu\gamma^\mu\Omega_\mu = \tfrac32He^{a_4}b_4^{-1/2}\gamma^{(x_0)} +
      (u - \tfrac12a_4')\gamma^{(x_4)}$, and a homogeneous condensate obeys
      $\Phi' = \mathcal{A}\Phi$ with $\mathcal{B}^2 = c^2 - M^2$ and
      $S = e^{a_4}b_4^{-2}S_0$ (PROVED, reproducing the Revision record); on the record
      history it stops oscillating when $c = \tfrac32He^{Hx_4/3}$ reaches $|M|$.
    - The family $\Phi_0(s) = v_1 + s\,c_{12}\,v_2$ on $b_4 = e^{2a_4}/4$ has all 24
      three-gamma bilinears zero for every real $s$ and densities of either sign; its
      energy-momentum tensor is diagonal and, up to a change of $\Lambda$,
      pressureless with $\rho = MS$, for every $a_4$ (PROVED).
    - Such a witness is the source of no history $b_4 = e^{2a_4}/k_0$ in Einstein
      gravity ($(a_4')^2 = -H^2k_0$ would be needed), and, if $S \ne 0$, none with
      the author's couplings for any $\Lambda$ (PROVED here; a computation of this
      notebook).
    - Whether any field of the theory drives the deflation of the extra times exactly
      stays OPEN in the corrected metric.
    """),
]

if __name__ == "__main__":
    raise SystemExit(run_builder(__file__))
