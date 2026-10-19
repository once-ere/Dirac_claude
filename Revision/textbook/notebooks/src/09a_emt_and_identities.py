#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
"""Builder of Notebook 09a, "The energy-momentum tensor and its conservation identities"
(textbook "Universes in Pairs", chapter 09).

The notebook Revision/textbook/notebooks/09a_emt_and_identities.ipynb is BUILT from this
file by Revision/textbook/tools/nbkit.py (never edit the .ipynb by hand):

    python Revision/textbook/tools/nbkit.py build \
        Revision/textbook/notebooks/src/09a_emt_and_identities.py --date YYYY-MM-DD
    python Revision/textbook/tools/nbkit.py check \
        Revision/textbook/notebooks/src/09a_emt_and_identities.py

The metric is the corrected metric of 2026-10-16 (version 2; Revision/SPEC.md section 1).
Every formula the notebook uses comes from the Revision record (the gammas fixture, the
field-theory formulas and reports, the scope reports, the field-equations reports, the
lead's checks, the record of the corrected metric); every number it prints is computed by
the notebook itself, and wherever it overlaps a Revision check the notebook asserts the
agreement and names the record file and the check.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools"))
from nbkit import code, md, run_builder  # noqa: E402

FIGURES = [
    "Revision/textbook/figures/09a_1_kinetic_weights.png",
    "Revision/textbook/figures/09a_2_tensor_heat_map.png",
    "Revision/textbook/figures/09a_3_diagonal_parts.png",
    "Revision/textbook/figures/09a_4_volumes_first_law.png",
    "Revision/textbook/figures/09a_5_hidden_balance.png",
]

FACTS = {
    "id": "09a",
    "name": "09a_emt_and_identities",
    "title": "The energy-momentum tensor and its conservation identities",
    "purpose": (
        "It builds the energy-momentum tensor of the commuting field dirac16complex00 at "
        "one point of the corrected metric of 2026-10-16 from the Revision gamma matrices "
        "and spin connection, checks that the tensor is real and symmetric, that its "
        "diagonal entries are the energy density and the pressures with their kinetic "
        "and potential parts, and the trace and on-shell identities; it shows that the "
        "spin connection enters the flow entry along an extra time and not the one "
        "along 3-space; it then derives with sympy, for both signs of sin z, the 21 "
        "Christoffel symbols of the metric and the two conservation identities of a "
        "diagonal tensor for all functions a4 and b4 (the energy balance along x4, in "
        "which 3-space and the block of the hidden direction and the extra times each "
        "dilute the energy density plus their own pressure, and the balance between the "
        "hidden and the extra-time pressures along x0), reads the first one as a first "
        "law for four volumes, checks that the source the record history requires obeys "
        "both identities, and draws five teaching plots."
    ),
    "records": [
        ["Revision/algebra/gammas.json",
         "the author's gamma matrices, the matrix C and the frame metric (the fixture)"],
        ["Revision/algebra/reports/python-algebra.json",
         "the Clifford relation and the properties of C"],
        ["Revision/theory/field-theory.json",
         "the formulas of the Christoffel symbols and of the energy exchange"],
        ["Revision/theory/reports/python-field-theory.json",
         "the metric, the volume factor, the spin-connection term, the symmetric "
         "tensor, the trace on shell, the energy exchange"],
        ["Revision/theory/reports/wolfram-field-theory.json",
         "the diagonal components, the trace, the kinetic sum, the Christoffel count, "
         "the spin-connection term per direction, the energy exchange"],
        ["Revision/theory/reports/python-scope.json",
         "the spin connection in the off-diagonal energy-momentum tensor"],
        ["Revision/theory/reports/wolfram-scope.json",
         "the same statement, verified with the Wolfram Language"],
        ["Revision/field_equations_a4/reports/wolfram-a4-report.json",
         "the anticommutator of each coordinate gamma with its spin connection, the "
         "components of the field equations and the source of the history"],
        ["Revision/field_equations_a4/reports/python-a4-report.json",
         "the source of the history, verified independently with sympy"],
        ["Revision/lead_checks/reports/emt-divergence-and-spin-connection.json",
         "the divergence of a diagonal tensor, the hidden coordinate y and the "
         "spin-connection term"],
        ["Revision/metric_warped/results/warped-metric.json",
         "the source that the record history requires (key history_source)"],
    ],
    "packages": ["numpy", "sympy", "matplotlib"],
    "needs_rust": [],
    "expected_seconds": 40,
    "timeout_seconds": 400,
    "files_written": ["Revision/textbook/figures/09a.captions.json"] + FIGURES,
    "final_lines": [
        "PASS the five figures of this notebook are saved and captioned",
        "ALL 29 CHECKS PASSED (notebook 09a)",
    ],
    "troubleshooting": [
        ["\"KeyError\" with the words \"has no check\"",
         "the notebook asks a Revision report for the verdict of one of its checks, and "
         "the report in your copy of the repository does not contain that check: your "
         "copy is older or newer than the notebook. Run `git pull` in the repository "
         "folder, then run the notebook again."],
        ["The cell of the Christoffel symbols runs for more than a minute",
         "sympy simplifies 288 expressions there for each of the two signs of sin z; on "
         "a slow computer this takes longer; wait until the cell has finished (its "
         "number appears in the margin) before you run the next cell."],
    ],
}

CELLS = [
    md(r"""
    ## 1. What this notebook computes

    This notebook is the first worked example of the chapter on the energy-momentum
    tensor. It works with the commuting field dirac16complex00 (16 complex numbers at
    every point) in the corrected metric of 2026-10-16, with the two functions
    $a_4(x_4)$ and $b_4(x_4)$, and it

    - builds, at one chosen point of the record history, the coordinate gamma
      matrices, the spin connection and the energy-momentum tensor $T^\nu{}_\mu$ (an
      $8 \times 8$ table of numbers) of a field configuration chosen at random;
    - checks that the tensor is real and symmetric, that its diagonal entries are
      $T^\mu{}_\mu = L_0 - K_\mu$, and computes from them the energy density $\rho$,
      the pressures $p_0$ (hidden direction), $p_3$ (3-space) and $p_t$ (extra times)
      with their kinetic and potential parts;
    - checks the trace identity and the kinetic-sum identity, and what they become
      when the configuration satisfies the field equation (on shell);
    - shows where the spin connection does enter the tensor: in the flow entry along
      an extra time, not in the one along 3-space;
    - derives exactly, with sympy, for both signs of $\sin z$, the 21 Christoffel
      symbols of the metric and the covariant divergence of a diagonal tensor: the
      two conservation identities
      $\partial_4\rho = -3a_4'(\rho + p_3) - 3h_4(\rho + p_t) - h_4(\rho + p_0)$, with
      the rate $h_4 = b_4'/(2b_4) - a_4'$ of the block of the hidden direction and the
      extra times, and $\partial_0 p_0 = -3H\cot z\,(p_0 - p_t)$;
    - reads the first identity as a first law of thermodynamics for the volumes of
      3-space, of the extra times and of the hidden direction, and the second one as a
      balance between the hidden and the extra-time pressures;
    - checks that the source which the record history requires obeys both identities;
    - compares every result that the Revision record also contains with that record
      and draws five teaching plots.
    """),
    md(r"""
    ## 3. The words used in this notebook

    - **Coordinates**: $x_0$ is the hidden space direction (listed first);
      $x_1, x_2, x_3$ are ordinary 3-space; $x_4$ is the time; $x_5, x_6, x_7$ are the
      three extra times. In the code, index $k$ means $x_k$: index 0 is $x_0$ and
      index 4 is $x_4$. We write $z = 6Hx_0$; $z$ takes every real value.
    - **Tensor** $T^\nu{}_\mu$: a table of $8 \times 8$ numbers at every point, one
      for each pair of directions $(\nu, \mu)$. The upper index $\nu$ is the row, the
      lower index $\mu$ the column. Lowering the upper index with the metric gives
      $T_{\nu\mu} = g_{\nu\nu} T^\nu{}_\mu$ (the metric here is diagonal).
    - **Energy-momentum tensor**: the tensor that says how much energy and momentum
      the field has and how they flow. Its diagonal entries are the energy density
      and the pressures; its off-diagonal entries are flows of energy and momentum.
    - **Energy density** $\rho = -T^{x_4}{}_{x_4}$: energy per unit (proper) volume.
      **Pressure** in direction $\mu$: $p_\mu = T^\mu{}_\mu$ (no sum).
      **Equation of state**: the ratio $w = p/\rho$.
    - **Kinetic term** $K_\mu$: the part of the Lagrangian that holds the derivative
      along the direction $\mu$; **potential energy**: $mS + U(S)$, the part without
      derivatives.
    - **Trace**: the sum of the diagonal entries, $T^\mu{}_\mu$ summed over $\mu$.
    - **Jet at a point**: the values of the field and of its eight first derivatives
      at one point. The energy-momentum tensor needs nothing else.
    - **On shell / off shell**: a configuration is on shell when it satisfies the
      field equation, off shell when it need not.
    - **Spin connection** $\Omega_\mu$: the $16 \times 16$ matrix that turns the
      ordinary derivative of the spinor into the covariant one,
      $D_\mu\Phi = \partial_\mu\Phi + \Omega_\mu\Phi$.
    - **Christoffel symbols** $\Gamma^\lambda{}_{\mu\nu}$: the numbers that turn
      ordinary derivatives of tensors into covariant ones.
    - **Covariant divergence** $\nabla_\mu T^\mu{}_\nu$: the derivative of the
      tensor summed over its upper index, corrected by the Christoffel symbols.
      **Conservation** means $\nabla_\mu T^\mu{}_\nu = 0$.
    - **Block**: the four directions $x_0, x_5, x_6, x_7$, which share the time
      dependent scale factor $e^{-a_4}b_4^{1/2}$ and its rate
      $h_4 = b_4'/(2b_4) - a_4'$.
    - **Fold**: the places $\cos z = 0$ (for example $z = \pi/2$), where $g_{x_0x_0}$
      and the volume factor vanish and two halves of a cell meet.
    - **Heat map**: a picture of a table of numbers in which each entry is a coloured
      square; the colour scale says which number each colour means.
    """),
    md(r"""
    ## 4. The physical and mathematical situation

    **The metric.** The corrected metric of 2026-10-16 is diagonal,
    $g = \mathrm{diag}(f_0^2, f_1^2, f_2^2, f_3^2, -f_4^2, -f_5^2, -f_6^2, -f_7^2)$
    (in the order $x_0, \dots, x_7$), with the vielbein factors
    $f_0 = e^{-a_4}b_4^{1/2}\cot z$ (the hidden direction; it carries the sign of
    $\cot z$), $f_1 = f_2 = f_3 = e^{a_4}$ (3-space, inflating as $a_4$ grows; no
    dependence on $z$), $f_4 = 1$ (the time) and
    $f_5 = f_6 = f_7 = e^{-a_4}b_4^{1/2}(\sin^2 z)^{1/12}$ (the extra times), where
    $z = 6Hx_0$ takes every real value, $H > 0$ is the author's constant and $a_4$
    and $b_4 > 0$ depend on $x_4$; $(\sin^2 z)^{1/12}$ is the positive root. The
    hidden direction and the extra times form one block with the scale factor
    $e^{-a_4}b_4^{1/2}$, which changes at the rate $h_4 = b_4'/(2b_4) - a_4'$. The
    volume factor is $\sqrt{|g|} = |f_0 f_1 \cdots f_7| =
    e^{-a_4}b_4^2|\cot z|(\sin^2 z)^{1/4}$. The metric is degenerate where
    $\sin z\cos z = 0$: at the folds $\cos z = 0$ two halves of a cell meet. The
    Kohn-Sham part of the book uses the deflating history $a_4 = AHx_4$,
    $b_4 = b_4(0)e^{(4/3)AHx_4}$ as a prescribed background; this notebook takes its
    point on that history (with $b_4(0)$ as the unit of $b_4$), where
    $h_4 = -AH/3 < 0$: the block deflates.

    **The field and its Lagrangian.** dirac16complex00 is a column $\Phi$ of 16
    complex numbers at every point. With $\bar\Phi = \Phi^\dagger C$, $S = \bar\Phi\Phi$
    and $U(S) = \frac{\lambda}{2}S^2$, the Lagrangian per unit volume is
    $L_0 = \frac12\sum_\mu(\bar\Phi\gamma^\mu D_\mu\Phi
    - (D_\mu\bar\Phi)\gamma^\mu\Phi) - mS - U(S)$, with the coordinate gammas
    $\gamma^\mu = \gamma^{(\mu)}/f_\mu$,
    $D_\mu\Phi = \partial_\mu\Phi + \Omega_\mu\Phi$ and
    $D_\mu\bar\Phi = \partial_\mu\bar\Phi - \bar\Phi\Omega_\mu$.

    **The energy-momentum tensor** (Revision record, `Revision/theory/field-theory.json`,
    formula `T_symmetric`):
    $T^\nu{}_\mu = \delta^\nu_\mu L_0 - \frac14(\bar\Phi\gamma^\nu D_\mu\Phi
    - D_\mu\bar\Phi \gamma^\nu\Phi + \bar\Phi\gamma_\mu D^\nu\Phi
    - D^\nu\bar\Phi \gamma_\mu\Phi)$, with $\gamma_\mu = g_{\mu\mu}\gamma^\mu$ and
    $D^\nu = g^{\nu\nu}D_\nu$. The sign convention is $\rho = -T^{x_4}{}_{x_4}$ and
    $p_\mu = T^\mu{}_\mu$ (no sum) for $\mu \neq x_4$. This symmetric (Belinfante)
    tensor is the symmetric part of the tensor that a variation of the vielbein
    gives (record formula `T_variation`, which has an extra spin-density term); the
    two are equal on every solution of the field equation, and for other
    configurations they agree in general only on the diagonal (record check
    `commuting_emt_equals_general_vielbein_variation_on_shell`). This notebook uses
    the symmetric tensor `T_symmetric`; so the lowered table $T_{\nu\mu}$ computed
    below for random values, which do not solve the field equation, is symmetric by
    construction.

    **The diagonal entries.** With the kinetic term of direction $\mu$,
    $K_\mu = \frac{1}{2f_\mu}(\bar\Phi\gamma^{(\mu)}\partial_\mu\Phi
    - \partial_\mu\bar\Phi \gamma^{(\mu)}\Phi)$, the record states
    $L_0 = \sum_\mu K_\mu - mS - U$ and $T^\mu{}_\mu = L_0 - K_\mu$, so
    $\rho = -\sum_{\mu \neq x_4}K_\mu + mS + U$ and
    $p_\mu = \sum_{\nu \neq \mu}K_\nu - mS - U$.

    **Conservation.** On shell $\nabla_\mu T^\mu{}_\nu = 0$ (a theorem of the record,
    proved from the invariance of the action under changes of coordinates). For a
    diagonal tensor $\mathrm{diag}(p_0, p_3, p_3, p_3, -\rho, p_t, p_t, p_t)$ whose
    entries depend on $x_4$ and $x_0$, this notebook derives the two conditions it
    becomes.

    **Both fields.** The same formulas hold for the anticommuting field
    dirac16complex, whose bilinears are even elements of a Grassmann algebra (the
    record verifies them, for example in the checks `T_diagonal_components_G`,
    `EMT_trace_G` and `kinetic_sum_on_shell_G` of
    `Revision/theory/reports/wolfram-field-theory.json`). After quantisation the record
    defines the tensor as a normal-ordered operator; the positive space of quantum
    states this needs is constructed only for single good-sector momenta (waves that
    do not depend on the extra times) with frozen coefficients, and for
    $\lambda \neq 0$ the operator form of the on-shell identity
    $\sum_\mu\langle{:}K_\mu{:}\rangle = \langle{:}(m + U')S{:}\rangle$ is verified
    only in a finite model of one such mode set, and there only when the potential
    and the tensor are Wick (normal) ordered as whole products
    (`Revision/theory/fock_quartic/reports/fock-quartic.json`, 21 of 21 checks); for
    the field on a whole slice it is OPEN. This notebook computes with ordinary
    complex numbers, that is, for dirac16complex00.
    """),
    md(r"""
    ## 5. The gamma matrices and the matrix C

    The next cell reads the Revision fixture `Revision/algebra/gammas.json`, which
    holds the author's real $16 \times 16$ gamma matrices in the order
    $x_0, \dots, x_7$, the frame metric $\eta$ and the matrix
    $C = \gamma^{(x_0)}\gamma^{(x_1)}\gamma^{(x_2)}\gamma^{(x_3)}$. It also defines the
    helper `recorded(path, name)`, which opens a Revision report and returns the
    verdict of one of its checks; every check of this notebook that reproduces a
    Revision check asks the report for that verdict too.
    """),
    code(r'''
    import numpy as np  # arrays of numbers, matrices, linear algebra

    fixture = json.loads(
        repository_file("Revision/algebra/gammas.json").read_text(encoding="utf-8"))
    # gamma[a] is the frame matrix gamma^(xa): gamma[0] = x0, ..., gamma[7] = x7.
    gamma = [np.array(rows, dtype=float) for rows in fixture["gamma"]]
    eta = np.array(fixture["eta"], dtype=float)  # (+1, +1, +1, +1, -1, -1, -1, -1)
    C = np.array(fixture["C"], dtype=float)  # gamma^(x0) gamma^(x1) gamma^(x2) gamma^(x3)
    I16 = np.eye(16)  # the 16 x 16 unit matrix
    NAMES = ["x0", "x1", "x2", "x3", "x4", "x5", "x6", "x7"]  # the author's coordinates


    def recorded(path, name):
        """The verdict (PASS or FAIL) of the check name in the Revision report path."""
        report_data = json.loads(repository_file(path).read_text(encoding="utf-8"))
        for item in report_data["checks"]:
            if item["name"] == name:
                return item["verdict"].upper()  # some reports write "pass"
        raise KeyError(f"{path} has no check {name}")


    ALGEBRA = "Revision/algebra/reports/python-algebra.json"
    # {gamma^a, gamma^b} = gamma^a gamma^b + gamma^b gamma^a must be 2 eta^ab times 1.
    clifford = all(np.array_equal(gamma[a] @ gamma[b] + gamma[b] @ gamma[a],
                                  2 * eta[a] * (a == b) * I16)
                   for a in range(8) for b in range(8))
    check(clifford and recorded(ALGEBRA, "clifford_relation") == "PASS",
          "the 64 Clifford relations {gamma^a, gamma^b} = 2 eta^ab",
          record=f"{ALGEBRA}, check clifford_relation")
    # C is symmetric, C times C is 1, and every C gamma^a is antisymmetric.
    c_ok = np.array_equal(C, C.T) and np.array_equal(C @ C, I16) and all(
        np.array_equal((C @ g).T, -(C @ g)) for g in gamma)
    check(c_ok and recorded(ALGEBRA, "C_real_symmetric_involution") == "PASS"
          and recorded(ALGEBRA, "C_gamma_antisymmetric") == "PASS",
          "C is real symmetric, C^2 = 1, every C gamma^a is antisymmetric",
          record=f"{ALGEBRA}, checks C_real_symmetric_involution and "
                 "C_gamma_antisymmetric")
    '''),
    md(r"""
    ## 6. The corrected metric at one point and the weights of the kinetic terms

    The next cell fixes the point at which the tensor is built. The author's
    constant is $H = 0.25$ (all quantities are pure numbers: lengths in a unit of
    our choice, $H$, $m$ and $\lambda$ in the matching powers of it). The history is
    $a_4 = AHx_4$, $b_4 = e^{\beta AHx_4}$ with $A = 1$ and $\beta = \frac43$, so
    $a_4' = AH = 0.25$, $b_4'/b_4 = \beta AH = \frac13$ and
    $h_4 = b_4'/(2b_4) - a_4' = -\frac{1}{12}$; the point is $x_4 = 2$ (hence
    $a_4 = 0.5$ and $b_4 = e^{2/3}$) and $z = \pi/4$. The function `frame_factors`
    returns the eight factors $f_a$; the cell checks that $\eta_{aa}f_a^2$ is the
    corrected metric and that $|f_0 f_1 \cdots f_7| =
    e^{-a_4}b_4^2|\cot z|(\sin^2 z)^{1/4}$.

    In the energy-momentum tensor every derivative along $x_\mu$ carries the weight
    $1/f_\mu$: $e^{-a_4}$ along 3-space, $1$ along the time,
    $e^{a_4}b_4^{-1/2}(\sin^2 z)^{-1/12}$ along the extra times and
    $e^{a_4}b_4^{-1/2}\tan z$ along the hidden direction. The figure shows the sizes
    of these weights along the history and against $z$.
    """),
    code(r'''
    H = 0.25  # the author's constant H
    A = 1.0  # the history a4 = A H x4; A > 0: 3-space inflates, the block deflates
    m = 1.0  # the mass m of the field
    lam = 0.5  # the strength lambda of the potential U(S) = (lambda/2) S^2
    beta = 4 / 3  # the history b4 = b4(0) e^(beta A H x4), in the unit b4(0)
    X4 = 2.0  # the time x4 of the point
    a4 = A * H * X4  # a4 at the point: 0.5
    a4p = A * H  # its derivative da4/dx4 (written a4p, "a4 prime"): 0.25
    b4 = np.exp(beta * A * H * X4)  # b4 at the point: e^(2/3)
    b4p = beta * A * H * b4  # db4/dx4, so that b4p/b4 = 1/3
    z = np.pi / 4  # z = 6 H x0 at the point


    def frame_factors(a4_value, b4_value, z_value):
        """The eight factors f_a of the diagonal vielbein, in the order x0, ..., x7."""
        block = np.exp(-a4_value) * np.sqrt(b4_value)  # e^(-a4) b4^(1/2)
        hidden = block / np.tan(z_value)  # e^(-a4) b4^(1/2) cot z (signed)
        extra = block * np.abs(np.sin(z_value)) ** (1 / 6)  # times (sin^2 z)^(1/12)
        return np.array([hidden] + [np.exp(a4_value)] * 3 + [1.0] + [extra] * 3)


    f = frame_factors(a4, b4, z)
    g_diag = eta * f ** 2  # the diagonal entries g_mumu = eta_mumu f_mu^2
    # The corrected metric written out: e^(-2 a4) b4 cot^2 z, e^(2 a4), -1,
    # -e^(-2 a4) b4 (sin^2 z)^(1/6).
    authors = np.array([np.exp(-2 * a4) * b4 / np.tan(z) ** 2] + [np.exp(2 * a4)] * 3
                       + [-1.0] + [-np.exp(-2 * a4) * b4 * (np.sin(z) ** 2) ** (1 / 6)] * 3)
    THEORY_PY = "Revision/theory/reports/python-field-theory.json"
    check(np.allclose(g_diag, authors, rtol=1e-14, atol=0)
          and recorded(THEORY_PY, "metric_from_vielbein_equals_SPEC") == "PASS",
          "eta_aa f_a^2 is the corrected metric at the point",
          record=f"{THEORY_PY}, check metric_from_vielbein_equals_SPEC")
    volume = np.exp(-a4) * b4 ** 2 * abs(1 / np.tan(z)) * (np.sin(z) ** 2) ** (1 / 4)
    check(abs(abs(np.prod(f)) - volume) < 1e-14
          and recorded(THEORY_PY, "sqrt_det_g") == "PASS",
          "|f0 f1 ... f7| equals e^(-a4) b4^2 |cot z| (sin^2 z)^(1/4)",
          record=f"{THEORY_PY}, check sqrt_det_g")
    for name, value in zip(NAMES, f):
        report(f"f_{name}", f"{value:.6f}")
    report("sqrt|g| at the point", f"{volume:.6f}")
    '''),
    md(r"""
    The next cell draws the sizes of the weights $|1/f_\mu|$. Left: along the history,
    against $a_4$ from $-2$ to $2$ with $b_4 = e^{4a_4/3}$, at $z = \pi/4$; the 3-space
    weight falls like $e^{-a_4}$, and the extra-time and hidden weights rise like
    $e^{a_4/3}$ (the block deflates), so their derivatives count more and more; these
    two lines differ only by the constant factor $(\sin^2 z)^{-1/12}$. Right: against
    $z$ from $0.02$ to $\pi - 0.02$ at the point ($a_4 = 0.5$, $b_4 = e^{2/3}$); the
    hidden weight $e^{a_4}b_4^{-1/2}|\tan z|$ grows without bound at the fold
    $z = \pi/2$, where the two halves of the cell meet, and the 3-space weight does
    not depend on $z$.
    """),
    code(r'''
    from matplotlib.ticker import NullFormatter  # a tick label that prints nothing

    a4_axis = np.linspace(-2.0, 2.0, 401)  # values of a4 for the left panel
    z_axis = np.linspace(0.02, np.pi - 0.02, 400)  # values of z for the right panel
    fig, (left, right) = plt.subplots(1, 2, figsize=(9.6, 3.9))
    # along the history b4 = e^(beta a4) (since a4 = A H x4 and b4 = e^(beta A H x4))
    weights_a4 = np.abs([1 / frame_factors(value, np.exp(beta * value), z)
                         for value in a4_axis])
    weights_z = np.abs([1 / frame_factors(a4, b4, value) for value in z_axis])
    for panel, axis, weights in ((left, a4_axis, weights_a4), (right, z_axis, weights_z)):
        panel.plot(axis, weights[:, 1], label="3-space $x_1, x_2, x_3$")
        panel.plot(axis, weights[:, 4], "--", label="time $x_4$")
        panel.plot(axis, weights[:, 5], label="extra times $x_5, x_6, x_7$")
        panel.plot(axis, weights[:, 0], ":", label="hidden direction $x_0$")
        panel.set_yscale("log")  # equal factors are equal distances on this axis
        panel.yaxis.set_minor_formatter(NullFormatter())  # no labels on minor ticks
        panel.set_ylabel("size of the weight $|1/f_\\mu|$")
    right.axvline(np.pi / 2, color="gray", linewidth=0.8)  # the fold z = pi/2
    ticks = [0.03, 0.1, 0.2, 0.5, 1, 2, 5, 10, 30]  # plain numbers on the vertical axes
    left.set_yticks(ticks[2:8], [str(t) for t in ticks[2:8]])
    right.set_yticks(ticks, [str(t) for t in ticks])
    right.set_ylim(0.02, 50.0)
    left.set_xlabel("$a_4$ (history: $b_4 = e^{4a_4/3}$; $z = \\pi/4$)")
    right.set_xlabel("$z = 6 H x_0$ (at $a_4 = 0.5$, $b_4 = e^{2/3}$; fold at $\\pi/2$)")
    left.set_title("Weights along the history")
    right.set_title("Weights against $z$")
    left.legend(fontsize=8)
    save_figure(fig, "kinetic_weights",
                "The sizes of the weights $1/f_\\mu$ with which a derivative along each "
                "direction enters the energy-momentum tensor, on a logarithmic vertical "
                "axis (pure numbers). Left: along the history $b_4 = e^{4a_4/3}$ (in the "
                "unit $b_4(0)$), against $a_4$ from $-2$ to $2$ at $z = \\pi/4$; the "
                "3-space weight $e^{-a_4}$ falls, while the extra-time weight "
                "$e^{a_4}b_4^{-1/2}(\\sin^2 z)^{-1/12}$ and the hidden weight "
                "$e^{a_4}b_4^{-1/2}|\\tan z|$ both rise like $e^{a_4/3}$, because the "
                "block of the hidden direction and the extra times deflates; the time "
                "weight is $1$. Right: against $z$ from $0.02$ to $\\pi - 0.02$ at "
                "$a_4 = 0.5$, $b_4 = e^{2/3}$; the hidden weight grows without bound at "
                "the fold $z = \\pi/2$ (gray line), where the two halves of the cell "
                "meet, and the 3-space weight does not depend on $z$.")
    '''),
    md(r"""
    ## 7. The spin connection at the point

    The record gives the spin connection of the diagonal vielbein in closed form
    (`Revision/theory/field-theory.json`, formula `Omega_components`), with
    $s_b = e^{-a_4}b_4^{1/2}$ and $h_4 = b_4'/(2b_4) - a_4'$:
    $\Omega_{x_0} = \frac12 h_4 s_b\cot z\,\gamma^{(0)}\gamma^{(4)}$,
    $\Omega_{x_i} = \frac12 a_4' e^{a_4}\gamma^{(i)}\gamma^{(4)}$ for $i = 1, 2, 3$,
    $\Omega_{x_t} = \frac12(\sin^2 z)^{1/12}(h_4 s_b\gamma^{(4)}\gamma^{(t)}
    + H\gamma^{(0)}\gamma^{(t)})$ for $t = 5, 6, 7$, and $\Omega_{x_4} = 0$. The next
    cell builds these eight matrices and the coordinate gammas
    $\gamma^\mu = \gamma^{(\mu)}/f_\mu$, and confirms three exact facts of the record
    at this point: for each direction separately
    $\gamma^\mu\Omega_\mu + \Omega_\mu\gamma^\mu = 0$ (no sum), which is why no spin
    connection survives in the diagonal entries of the tensor; direction by
    direction $\gamma^{x_0}\Omega_{x_0} = \frac12h_4\gamma^{(4)}$,
    $\gamma^{x_i}\Omega_{x_i} = \frac12a_4'\gamma^{(4)}$ and
    $\gamma^{x_t}\Omega_{x_t} = \frac12h_4\gamma^{(4)} +
    \frac12He^{a_4}b_4^{-1/2}\gamma^{(0)}$; and summed over the directions
    $\gamma^\mu\Omega_\mu = c_g\gamma^{(x_0)} + v_g\gamma^{(x_4)}$ with
    $c_g = \frac32He^{a_4}b_4^{-1/2}$ and $v_g = b_4'/b_4 - a_4'/2$, the term of the
    field equation.
    """),
    code(r'''
    def spin_connection(a4_value, a4p_value, b4_value, b4p_value, z_value):
        """The eight 16 x 16 matrices Omega_mu of the record's formula Omega_components."""
        s_b = np.exp(-a4_value) * np.sqrt(b4_value)  # e^(-a4) b4^(1/2)
        h4 = b4p_value / (2 * b4_value) - a4p_value  # the rate of the block
        root = np.abs(np.sin(z_value)) ** (1 / 6)  # (sin^2 z)^(1/12)
        omega = [np.zeros((16, 16)) for _ in range(8)]  # Omega_x4 stays 0
        omega[0] = 0.5 * h4 * s_b / np.tan(z_value) * gamma[0] @ gamma[4]
        for i in range(1, 4):  # the three 3-space directions x1, x2, x3
            omega[i] = 0.5 * a4p_value * np.exp(a4_value) * gamma[i] @ gamma[4]
        for t in range(5, 8):  # the three extra times x5, x6, x7
            omega[t] = 0.5 * root * (h4 * s_b * gamma[4] @ gamma[t]
                                     + H * gamma[0] @ gamma[t])
        return omega


    Omega = spin_connection(a4, a4p, b4, b4p, z)
    gamma_up = [gamma[mu] / f[mu] for mu in range(8)]  # coordinate gammas gamma^mu
    gamma_down = [g_diag[mu] * gamma_up[mu] for mu in range(8)]  # gamma_mu
    # {gamma^mu, Omega_mu} for each mu separately: the largest entry of all eight.
    anti = max(np.abs(gamma_up[mu] @ Omega[mu] + Omega[mu] @ gamma_up[mu]).max()
               for mu in range(8))
    A4_REPORT = "Revision/field_equations_a4/reports/wolfram-a4-report.json"
    check(anti < 1e-14
          and recorded(A4_REPORT, "gamma_mu_anticommutes_with_Omega_mu_no_sum") == "PASS",
          "{gamma^mu, Omega_mu} = 0 for each direction mu (no sum)",
          record=f"{A4_REPORT}, check gamma_mu_anticommutes_with_Omega_mu_no_sum")
    h4 = b4p / (2 * b4) - a4p  # -1/12 at the point
    c_g = 1.5 * H * np.exp(a4) / np.sqrt(b4)  # the coefficient of gamma^(x0)
    v_g = b4p / b4 - a4p / 2  # the coefficient of gamma^(x4)
    # the record's value of gamma^mu Omega_mu for each direction (no sum)
    per_direction = ([0.5 * h4 * gamma[4]] + [0.5 * a4p * gamma[4]] * 3 + [0 * I16]
                     + [0.5 * h4 * gamma[4] + c_g / 3 * gamma[0]] * 3)
    THEORY_WL = "Revision/theory/reports/wolfram-field-theory.json"
    check(max(np.abs(gamma_up[mu] @ Omega[mu] - per_direction[mu]).max()
              for mu in range(8)) < 1e-14
          and recorded(THEORY_PY, "per_direction_terms") == "PASS"
          and recorded(THEORY_WL, "gammaOmega_per_direction") == "PASS",
          "gamma^mu Omega_mu per direction: h4/2, a4'/2 (x3), 0, h4/2 + c_g/3 (x3)",
          record=f"{THEORY_PY}, check per_direction_terms; {THEORY_WL}, check "
                 "gammaOmega_per_direction")
    total = sum(gamma_up[mu] @ Omega[mu] for mu in range(8))  # gamma^mu Omega_mu, summed
    LEAD = "Revision/lead_checks/reports/emt-divergence-and-spin-connection.json"
    check(np.abs(total - c_g * gamma[0] - v_g * gamma[4]).max() < 1e-14
          and recorded(THEORY_PY, "gamma_mu_Omega_mu_equals_hidden_block_terms") == "PASS"
          and recorded(LEAD, "gamma_Omega_equals_hidden_block_terms") == "PASS",
          "gamma^mu Omega_mu = c_g gamma^(x0) + v_g gamma^(x4) at the point",
          record=f"{THEORY_PY}, check gamma_mu_Omega_mu_equals_hidden_block_terms; "
                 f"{LEAD}, check gamma_Omega_equals_hidden_block_terms")
    report("h4 = b4'/(2 b4) - a4'", f"{h4:.6f}")
    report("c_g = (3/2) H e^a4 b4^(-1/2)", f"{c_g:.6f}")
    report("v_g = b4'/b4 - a4'/2", f"{v_g:.6f}")
    '''),
    md(r"""
    ## 8. A field configuration at the point and its energy-momentum tensor

    The tensor at a point needs only the jet there: the 16 complex values of $\Phi$
    and the $8 \times 16$ complex values of its first derivatives
    $\partial_\mu\Phi$. The next cell defines two functions. `bar` returns the Dirac
    adjoint $\bar\Phi = \Phi^\dagger C$ as a row of 16 numbers. `energy_momentum`
    follows the formula of section 4 literally: from the jet it builds
    $D_\mu\Phi$ and $D_\mu\bar\Phi$, the Lagrangian $L_0$ and the 64 entries
    $T^\nu{}_\mu$ (row $\nu$, column $\mu$), and also the eight kinetic terms
    $K_\mu$ from their own formula (without the spin connection), so that the two
    can be compared later. The cell only defines the functions; it prints nothing.
    """),
    code(r'''
    def bar(vector):
        """The Dirac adjoint: the row vector vector^dagger C."""
        return vector.conj() @ C


    def energy_momentum(phi, dphi, f_values, gup, gdown, omega):
        """S, U, L0, the kinetic terms K_mu and the tensor T (T[nu, mu] = T^nu_mu)."""
        g_values = eta * f_values ** 2  # g_mumu
        S = (bar(phi) @ phi).real  # S = Phibar Phi (a real number)
        U = lam / 2 * S ** 2  # U(S) = (lambda/2) S^2
        D = [dphi[mu] + omega[mu] @ phi for mu in range(8)]  # D_mu Phi
        Dbar = [bar(dphi[mu]) - bar(phi) @ omega[mu] for mu in range(8)]  # D_mu Phibar
        L0 = 0.5 * sum(bar(phi) @ gup[mu] @ D[mu] - Dbar[mu] @ gup[mu] @ phi
                       for mu in range(8)) - m * S - U
        T = np.zeros((8, 8), dtype=complex)
        for nu in range(8):
            for mu in range(8):
                bracket = (bar(phi) @ gup[nu] @ D[mu] - Dbar[mu] @ gup[nu] @ phi
                           # gamma_mu D^nu = gamma_mu D_nu / g_nunu
                           + (bar(phi) @ gdown[mu] @ D[nu]
                              - Dbar[nu] @ gdown[mu] @ phi) / g_values[nu])
                T[nu, mu] = (nu == mu) * L0 - bracket / 4
        # K_mu = (1/(2 f_mu)) (Phibar gamma^(mu) d_mu Phi - d_mu Phibar gamma^(mu) Phi)
        K = np.array([(bar(phi) @ gamma[mu] @ dphi[mu] - bar(dphi[mu]) @ gamma[mu] @ phi)
                      / (2 * f_values[mu]) for mu in range(8)])
        return S, U, L0, K, T
    '''),
    md(r"""
    The next cell draws the jet at random, with a fixed seed so that every run draws
    the same numbers. The jet need not satisfy the field equation: the identities of
    sections 8 to 10 hold off shell. The cell computes the tensor and checks that
    every entry is real (its imaginary part is rounding noise) and that
    $T_{\nu\mu} = g_{\nu\nu}T^\nu{}_\mu$ is symmetric.
    """),
    code(r'''
    rng = np.random.default_rng(12345)  # a fixed seed: the same numbers in every run
    Phi = rng.normal(size=16) + 1j * rng.normal(size=16)  # the 16 values of Phi
    dPhi = rng.normal(size=(8, 16)) + 1j * rng.normal(size=(8, 16))  # d_mu Phi
    # np.roll moves the last row to the front: the eight rows are the derivatives along
    # x0, x1, ..., x7, and the numbers are those of the earlier edition of this notebook.
    dPhi = np.roll(dPhi, 1, axis=0)
    S, U, L0, K, T = energy_momentum(Phi, dPhi, f, gamma_up, gamma_down, Omega)
    largest_imaginary = max(np.abs(T.imag).max(), np.abs(K.imag).max(), abs(L0.imag))
    check(largest_imaginary < 1e-12, "every entry of T, every K_mu and L0 are real")
    T, K, L0 = T.real, K.real, L0.real  # keep the real parts
    T_low = g_diag[:, None] * T  # T_numu = g_nunu T^nu_mu
    check(np.abs(T_low - T_low.T).max() < 1e-12
          and recorded(THEORY_PY, "commuting_emt_symmetric") == "PASS",
          "T_numu is symmetric (64 entries, 28 pairs compared)",
          record=f"{THEORY_PY}, check commuting_emt_symmetric")
    report("S = Phibar Phi", f"{S:.6f}")
    report("L0", f"{L0:.6f}")
    '''),
    md(r"""
    The next cell draws the 64 entries $T^\nu{}_\mu$ as a heat map: row $\nu$,
    column $\mu$, red for positive and blue for negative numbers, with the value
    written in each square. The diagonal holds the energy density (with a minus
    sign, at $x_4$) and the seven pressures; the other squares are flows of energy
    and momentum, which a random configuration has in every direction.
    """),
    code(r'''
    fig, ax = plt.subplots(figsize=(6.6, 5.6))
    largest = np.abs(T).max()  # the colour scale runs from -largest to +largest
    picture = ax.imshow(T, cmap="RdBu_r", vmin=-largest, vmax=largest)
    for nu in range(8):
        for mu in range(8):
            # white digits on dark squares, black digits on light ones
            colour = "white" if abs(T[nu, mu]) > 0.6 * largest else "black"
            ax.text(mu, nu, f"{T[nu, mu]:.1f}", ha="center", va="center", fontsize=7,
                    color=colour)
    ax.set_xticks(range(8), [f"${n[0]}_{n[1]}$" for n in NAMES])
    ax.set_yticks(range(8), [f"${n[0]}_{n[1]}$" for n in NAMES])
    ax.set_xlabel("lower index $\\mu$ (column)")
    ax.set_ylabel("upper index $\\nu$ (row)")
    ax.set_title("$T^\\nu{}_\\mu$ of one random configuration at one point")
    ax.grid(False)  # no grid lines across the squares
    fig.colorbar(picture, ax=ax, label="value of $T^\\nu{}_\\mu$ (energy per volume)")
    save_figure(fig, "tensor_heat_map",
                "Heat map of the energy-momentum tensor $T^\\nu{}_\\mu$ of a random "
                "configuration of dirac16complex00 at the point $a_4 = 0.5$, "
                "$a_4' = 0.25$, $b_4 = e^{2/3}$, $b_4'/b_4 = 1/3$, $z = \\pi/4$ of the "
                "record history in the corrected metric, with $H = 0.25$, "
                "$m = 1$, $\\lambda = 0.5$; row $\\nu$ and column $\\mu$ run over "
                "$x_0, \\dots, x_7$; colour and printed number give the value, in units "
                "of energy per unit volume. The diagonal holds $-\\rho$ at $x_4$ and "
                "the seven pressures; the off-diagonal squares are flows of energy and "
                "momentum. The table is not symmetric as printed, because the upper "
                "index is raised with the metric; $g_{\\nu\\nu}T^\\nu{}_\\mu$ is "
                "symmetric.")
    '''),
    md(r"""
    ## 9. The diagonal entries: energy density, pressures, kinetic and potential parts

    The next cell checks the record's statement $T^\mu{}_\mu = L_0 - K_\mu$ for all
    eight directions and $L_0 = \sum_\mu K_\mu - mS - U$. It then computes the energy
    density and the pressures and splits each into its kinetic part (made of the
    $K_\nu$) and its potential part ($mS + U$):
    $\rho = \rho_{\rm kin} + \rho_{\rm pot}$ with
    $\rho_{\rm kin} = -\sum_{\mu \neq x_4}K_\mu$, $\rho_{\rm pot} = mS + U$, and
    $p_\mu = \sum_{\nu \neq \mu}K_\nu - (mS + U)$. A random configuration is not
    isotropic, so the three 3-space pressures differ, and so do the three extra-time
    pressures. Its energy density may come out negative: the energy of
    dirac16complex00 has no lower bound (Revision record
    `Revision/theory/reports/python-scope.json`, check
    `commuting_field_energy_unbounded_below`), because both $S$ and the kinetic
    terms can have either sign.
    """),
    code(r'''
    check(np.abs(np.diag(T) - (L0 - K)).max() < 1e-12
          and abs(L0 - (K.sum() - m * S - U)) < 1e-12
          and recorded(THEORY_WL, "T_diagonal_components_C") == "PASS",
          "T^mu_mu = L0 - K_mu for all eight mu, and L0 = sum K - m S - U",
          record=f"{THEORY_WL}, check T_diagonal_components_C")
    potential = m * S + U  # the potential energy density m S + U(S)
    # kinetic part of T^mu_mu: the sum of the K_nu with nu different from mu
    kinetic_parts = np.array([K.sum() - K[mu] for mu in range(8)])
    rho = -T[4, 4]  # the energy density
    rho_kin = -(K.sum() - K[4])  # minus the sum of the K_mu with mu different from x4
    check(abs(rho - (rho_kin + potential)) < 1e-12
          and np.abs(np.diag(T) - (kinetic_parts - potential)).max() < 1e-12,
          "rho = rho_kin + rho_pot and p_mu = (sum of the other K) - (m S + U)")
    report("rho = -T^x4_x4", f"{rho:.6f}")
    report("rho_kin", f"{rho_kin:.6f}")
    report("rho_pot = m S + U", f"{potential:.6f}")
    for mu in (0, 1, 2, 3, 5, 6, 7):
        report(f"pressure T^{NAMES[mu]}_{NAMES[mu]}", f"{T[mu, mu]:.6f}")
    '''),
    md(r"""
    The next cell draws, for each direction, the kinetic part, the potential part and
    their sum, the diagonal entry $T^\mu{}_\mu$. The potential part is the same,
    $-(mS + U)$, in every direction; the kinetic parts differ.
    """),
    code(r'''
    positions = np.arange(8)  # one group of bars per direction
    fig, ax = plt.subplots(figsize=(8.0, 4.2))
    ax.bar(positions - 0.27, kinetic_parts, width=0.27, label="kinetic part")
    ax.bar(positions, [-potential] * 8, width=0.27, label="potential part $-(mS + U)$")
    ax.bar(positions + 0.27, np.diag(T), width=0.27, label="total $T^\\mu{}_\\mu$")
    ax.axhline(0.0, color="black", linewidth=0.8)
    ax.set_xticks(positions, [f"${n[0]}_{n[1]}$" for n in NAMES])
    ax.set_xlabel("direction $\\mu$")
    ax.set_ylabel("value (energy per unit volume)")
    ax.set_title("Diagonal entries $T^\\mu{}_\\mu$ and their two parts")
    ax.legend(fontsize=8)
    save_figure(fig, "diagonal_parts",
                "The eight diagonal entries $T^\\mu{}_\\mu$ (right bar of each group) "
                "of the random configuration of the previous figure, each split into "
                "its kinetic part, the sum of the kinetic terms $K_\\nu$ of the other "
                "seven directions (left bar), and its potential part $-(mS + U)$ "
                "(middle bar), in units of energy per unit volume. The potential part "
                "is the same in every direction; the entry at $x_4$ is $-\\rho$, and "
                "the others are the pressures $p_0$, $p_3$ (three of them) and $p_t$ "
                "(three).")
    '''),
    md(r"""
    ## 10. The trace, the kinetic sum, and the configuration put on shell

    Summing $T^\mu{}_\mu = L_0 - K_\mu$ over the eight directions gives
    $8L_0 - \sum_\mu K_\mu = 7\sum_\mu K_\mu - 8(mS + U)$ (the record's trace
    identity). The record also states, for every configuration, the kinetic-sum
    identity $\sum_\mu K_\mu = VS + \frac12(\bar\Phi E - \bar E\Phi)$ with
    $V = m + U'(S) = m + \lambda S$, the field-equation expression
    $E = \gamma^\mu D_\mu\Phi - V\Phi$ and its adjoint
    $\bar E = (D_\mu\bar\Phi)\gamma^\mu + V\bar\Phi$. The next cell checks both.

    Then it puts the configuration on shell at the point: the field equation can be
    solved for the time derivative (its evolution form),
    $\partial_4\Phi = -\gamma^{(4)}\big[V\Phi - \sum_{a \neq 4}\frac{1}{f_a}\gamma^{(a)}
    \partial_a\Phi - c_g\gamma^{(0)}\Phi\big] - v_g\Phi$ (record formula
    `evolution_form`); the cell replaces the random
    $\partial_4\Phi$ by this one, checks that $E = 0$, and checks the on-shell values
    $\sum_\mu K_\mu = VS$, $L_0 = SU' - U$ and
    $T^\mu{}_\mu = -mS + 7SU' - 8U = -mS + 3\lambda S^2$.
    """),
    code(r'''
    V = m + lam * S  # V = m + U'(S), with U'(S) = lambda S
    E = sum(gamma_up[mu] @ (dPhi[mu] + Omega[mu] @ Phi) for mu in range(8)) - V * Phi
    E_bar = sum((bar(dPhi[mu]) - bar(Phi) @ Omega[mu]) @ gamma_up[mu]
                for mu in range(8)) + V * bar(Phi)
    check(abs(np.trace(T) - (7 * K.sum() - 8 * (m * S + U))) < 1e-11
          and recorded(THEORY_WL, "EMT_trace_C") == "PASS",
          "trace: sum of T^mu_mu = 7 sum K - 8 (m S + U), off shell",
          record=f"{THEORY_WL}, check EMT_trace_C")
    kinetic_sum = V * S + 0.5 * (bar(Phi) @ E - E_bar @ Phi)
    check(abs(K.sum() - kinetic_sum) < 1e-11
          and recorded(THEORY_WL, "kinetic_sum_on_shell_C") == "PASS",
          "sum K = V S + (1/2)(Phibar E - Ebar Phi), off shell",
          record=f"{THEORY_WL}, check kinetic_sum_on_shell_C")
    report("|E| of the random configuration (it is off shell)",
           f"{np.linalg.norm(E):.6f}")
    # The evolution form of the field equation gives d4 Phi from the other derivatives.
    rest = sum(gamma[a] @ dPhi[a] / f[a] for a in range(8) if a != 4)
    dPhi_on = dPhi.copy()
    dPhi_on[4] = -gamma[4] @ (V * Phi - rest - c_g * gamma[0] @ Phi) - v_g * Phi
    E_on = sum(gamma_up[mu] @ (dPhi_on[mu] + Omega[mu] @ Phi) for mu in range(8)) - V * Phi
    S_on, U_on, L0_on, K_on, T_on = energy_momentum(Phi, dPhi_on, f, gamma_up, gamma_down,
                                                    Omega)
    check(np.abs(E_on).max() < 1e-12, "with d4 Phi from the evolution form, E = 0")
    check(abs(K_on.real.sum() - V * S) < 1e-11
          and abs(L0_on.real - (S * lam * S - U)) < 1e-11
          and abs(np.trace(T_on.real) - (-m * S + 3 * lam * S ** 2)) < 1e-10
          and recorded(THEORY_PY, "commuting_trace_on_shell") == "PASS",
          "on shell: sum K = V S, L0 = S U' - U, trace = -m S + 3 lambda S^2",
          record=f"{THEORY_PY}, check commuting_trace_on_shell")
    report("trace on shell, -m S + 3 lambda S^2", f"{np.trace(T_on.real):.6f}")
    '''),
    md(r"""
    ## 11. Where the spin connection does enter the tensor

    The spin connection drops out of the Lagrangian and of the diagonal entries.
    It does enter off-diagonal entries, but not all of them. Take a homogeneous
    configuration (it depends on $x_4$ only, so $\partial_\mu\Phi = 0$ for
    $\mu \neq x_4$). In the piece $K^{x_4}{}_{\mu} = \frac12(\bar\Phi\gamma^{x_4}
    D_\mu\Phi - D_\mu\bar\Phi \gamma^{x_4}\Phi)$ of $T^{x_4}{}_{\mu}$ the derivative
    part vanishes and only the connection part
    $\frac12\bar\Phi\{\gamma^{x_4}, \Omega_\mu\}\Phi$ is left. Along 3-space it is
    zero, because $\Omega_{x_1}$ is a multiple of $\gamma^{(1)}\gamma^{(4)}$, which
    anticommutes with $\gamma^{(4)}$ (3-space does not depend on $x_0$). Along an
    extra time the record states $K^{x_4}{}_{x_5} = \frac12H(\sin^2 z)^{1/12}\,
    \bar\Phi\gamma^{(4)}\gamma^{(0)}\gamma^{(5)}\Phi$ (the $h_4$ part cancels). The
    next cell checks both at the point.
    """),
    code(r'''
    dPhi_hom = np.zeros((8, 16), dtype=complex)  # homogeneous: only d4 Phi is nonzero
    dPhi_hom[4] = rng.normal(size=16) + 1j * rng.normal(size=16)


    def flow_piece(mu):
        """K^x4_mu = (1/2)(Phibar gamma^x4 D_mu Phi - D_mu Phibar gamma^x4 Phi)."""
        D_mu = dPhi_hom[mu] + Omega[mu] @ Phi  # D_mu Phi = Omega_mu Phi here
        Dbar_mu = bar(dPhi_hom[mu]) - bar(Phi) @ Omega[mu]  # = -Phibar Omega_mu here
        return 0.5 * (bar(Phi) @ gamma_up[4] @ D_mu - Dbar_mu @ gamma_up[4] @ Phi)


    K_41, K_45 = flow_piece(1), flow_piece(5)
    expected = 0.5 * H * np.abs(np.sin(z)) ** (1 / 6) * (
        bar(Phi) @ gamma[4] @ gamma[0] @ gamma[5] @ Phi)
    SCOPE_PY = "Revision/theory/reports/python-scope.json"
    SCOPE_WL = "Revision/theory/reports/wolfram-scope.json"
    check(abs(K_41) < 1e-12 and abs(K_45 - expected) < 1e-12 and abs(K_45) > 0.01
          and recorded(SCOPE_PY, "spin_connection_in_the_energy_momentum_tensor") == "PASS"
          and recorded(SCOPE_WL, "spin_connection_in_the_energy_momentum_tensor") == "PASS",
          "homogeneous configuration: K^x4_x1 = 0, K^x4_x5 is the nonzero connection term",
          record=f"{SCOPE_PY} and {SCOPE_WL}, check "
                 "spin_connection_in_the_energy_momentum_tensor")
    report("K^x4_x1 (homogeneous configuration)", f"{abs(K_41):.1e}")
    report("K^x4_x5 (homogeneous configuration)", f"{K_45.real:.6f}")
    '''),
    md(r"""
    ## 12. The Christoffel symbols of the corrected metric (exact, with sympy)

    From here on the notebook computes exactly with symbols. For a diagonal metric
    the Christoffel symbols are
    $\Gamma^\lambda{}_{\mu\nu} = \frac{1}{2g_{\lambda\lambda}}(\partial_\mu
    g_{\lambda\nu} + \partial_\nu g_{\lambda\mu} - \partial_\lambda g_{\mu\nu})$
    (no sum over $\lambda$). The metric contains $(\sin^2 z)^{1/6}$, the positive
    root, which equals $|\sin z|^{1/3}$. To avoid the absolute value, the cell
    treats the two signs $s = \pm1$ of $\sin z$ separately: where $s\sin z > 0$ the
    root is $(s\sin z)^{1/3}$, and the two cases together cover every real $z$ with
    $\sin z \neq 0$ (the same method as the lead's independent check). For each sign
    the cell writes the metric with symbols (general functions $a_4(x_4)$ and
    $b_4(x_4) > 0$, the symbol $H$) and computes all the symbols with $\mu \le \nu$
    (the symbol is symmetric in $\mu$ and $\nu$), keeping the nonzero ones in a
    dictionary. It prints how many it found.
    """),
    code(r'''
    import sympy as sp  # exact algebra and calculus with symbols

    x = sp.symbols("x0:8", real=True)  # the coordinates x0, ..., x7 (x[0] ... x[7])
    Hs = sp.symbols("H", positive=True)  # the author's constant, as a symbol
    a4_function = sp.Function("a4")(x[4])  # a general function a4(x4)
    b4_function = sp.Function("b4", positive=True)(x[4])  # a general positive b4(x4)
    zs = 6 * Hs * x[0]  # z = 6 H x0
    SIGNS = (1, -1)  # the sign s of sin z


    def metric_for_sign(s):
        """The corrected metric where s sin z > 0, written without an absolute value."""
        block = sp.exp(-2 * a4_function) * b4_function  # e^(-2 a4) b4
        root = (s * sp.sin(zs)) ** sp.Rational(1, 3)  # (sin^2 z)^(1/6), positive
        return sp.diag(*([block * sp.cot(zs) ** 2] + [sp.exp(2 * a4_function)] * 3
                         + [-1] + [-block * root] * 3))


    christoffel = {}  # s -> {(lambda, mu, nu): Gamma^lambda_mu nu}, the nonzero ones
    for s in SIGNS:
        g = metric_for_sign(s)
        christoffel[s] = {}
        for l in range(8):
            for i in range(8):
                for j in range(i, 8):  # mu <= nu
                    value = sp.simplify((sp.diff(g[l, j], x[i]) + sp.diff(g[l, i], x[j])
                                         - sp.diff(g[i, j], x[l])) / (2 * g[l, l]))
                    if value != 0:
                        christoffel[s][(l, i, j)] = value
        say(f"sign of sin z = {s:+d}: {len(christoffel[s])} nonzero Christoffel symbols "
            "with mu <= nu")
    '''),
    md(r"""
    The record lists exactly 21 such symbols (`Revision/theory/field-theory.json`,
    formula `christoffel_nonzero`, written in the Wolfram Language, with
    $|\sin z|^{1/3}$ written `Abs[Sin[6*H*x0]]^(1/3)`). The next cell translates
    that text into sympy's notation with the function `from_wolfram`, by plain text
    replacements (for example `Abs[Sin[6*H*x0]]` becomes `(s*sin(6*H*x0))`, `Sin[`
    becomes `sin(`, `Derivative[1][a4][x4]` becomes `a4p` and `Derivative[1][b4][x4]`
    becomes `b4p`); the function `plain` writes our own symbols with the same plain
    names `a4`, `a4p`, `b4` and `b4p`. For each sign the cell compares the two lists
    symbol by symbol, and it prints the 21 symbols for $\sin z > 0$.
    """),
    code(r'''
    a4s, a4ps = sp.symbols("a4 a4p", real=True)  # plain symbols for a4 and da4/dx4
    b4s = sp.Symbol("b4", positive=True)  # plain symbol for b4
    b4ps = sp.Symbol("b4p", real=True)  # plain symbol for db4/dx4


    def plain(expression):
        """Replace the derivatives and the functions a4(x4), b4(x4) by plain symbols."""
        expression = expression.subs({sp.Derivative(a4_function, x[4]): a4ps,
                                      sp.Derivative(b4_function, x[4]): b4ps})
        return expression.subs({a4_function: a4s, b4_function: b4s})


    WOLFRAM_TO_SYMPY = [  # (Wolfram text, sympy text), applied in this order
        ("Abs[Sin[6*H*x0]]", "(s*sin(6*H*x0))"),  # |sin z| = s sin z
        ("Derivative[1][a4][x4]", "a4p"), ("Derivative[1][b4][x4]", "b4p"),
        ("Derivative[1, 0][rho][x4, x0]", "rho_4"),
        ("Derivative[0, 1][p0][x4, x0]", "p0_0"), ("[x4, x0]", ""), ("a4[x4]", "a4"),
        ("b4[x4]", "b4"),
        ("Sin[", "sin("), ("Cos[", "cos("), ("Tan[", "tan("), ("Cot[", "cot("),
        ("Csc[", "csc("), ("E^", "E**"), ("^", "**"), ("[", "("), ("]", ")"),
        ("{", "["), ("}", "]")]


    def from_wolfram(text):
        """Translate a formula of the record from the Wolfram Language into sympy."""
        for old, new in WOLFRAM_TO_SYMPY:
            text = text.replace(old, new)
        return text


    FORMULAS = {item["key"]: item["wl"] for item in json.loads(repository_file(
        "Revision/theory/field-theory.json").read_text(encoding="utf-8"))["formulas"]}
    NAMES_SYMPY = {"a4": a4s, "a4p": a4ps, "b4": b4s, "b4p": b4ps, "H": Hs, "x0": x[0],
                   "E": sp.E}
    same = True
    for s in SIGNS:
        record_list = sp.sympify(from_wolfram(FORMULAS["christoffel_nonzero"]),
                                 locals=dict(NAMES_SYMPY, s=s))
        # The record counts the positions 1 ... 8 (x0 ... x7); Python counts 0 ... 7.
        record_symbols = {(int(e[0]) - 1, int(e[1]) - 1, int(e[2]) - 1): e[3]
                          for e in record_list}
        same = same and sorted(record_symbols) == sorted(christoffel[s]) and all(
            sp.simplify(plain(christoffel[s][key]) - record_symbols[key]) == 0
            for key in christoffel[s])
    check(all(len(christoffel[s]) == 21 for s in SIGNS) and same
          and recorded(THEORY_WL, "christoffel_count") == "PASS",
          "21 nonzero Christoffel symbols for each sign, equal to the record's list",
          record=f"{THEORY_WL}, check christoffel_count (formula christoffel_nonzero)")
    for (l, i, j), value in sorted(christoffel[1].items()):
        print(f"Gamma^{NAMES[l]}_({NAMES[i]} {NAMES[j]}) = {plain(value)}")
    '''),
    md(r"""
    ## 13. The covariant divergence of a diagonal tensor: the two identities

    For a tensor $T^\mu{}_\nu$ the covariant divergence is
    $\nabla_\mu T^\mu{}_\nu = \partial_\mu T^\mu{}_\nu + \Gamma^\mu{}_{\mu\lambda}
    T^\lambda{}_\nu - \Gamma^\lambda{}_{\mu\nu}T^\mu{}_\lambda$ (sums over $\mu$ and
    $\lambda$). The next cell takes the diagonal tensor
    $\mathrm{diag}(p_0, p_3, p_3, p_3, -\rho, p_t, p_t, p_t)$ whose four entries are
    arbitrary functions of $x_4$ and $x_0$ and computes the eight components with the
    Christoffel symbols of the previous section, for each sign of $\sin z$. It prints
    which components are not identically zero.
    """),
    code(r'''
    rho_f, p3_f, pt_f, p0_f = [sp.Function(n)(x[4], x[0]) for n in ("rho", "p3", "pt",
                                                                     "p0")]
    T_diag = sp.diag(p0_f, p3_f, p3_f, p3_f, -rho_f, pt_f, pt_f, pt_f)  # T^mu_nu


    def divergence_of(symbols):
        """The eight components nabla_mu T^mu_nu of T_diag for the given symbols."""
        def gamma_symbol(l, i, j):
            """Gamma^l_ij for any order of i and j (zero when it is not stored)."""
            return symbols.get((l, min(i, j), max(i, j)), 0)

        components = []
        for nu in range(8):
            value = sum(sp.diff(T_diag[mu, nu], x[mu]) for mu in range(8))
            value += sum(gamma_symbol(mu, mu, l) * T_diag[l, nu]
                         for mu in range(8) for l in range(8))
            value -= sum(gamma_symbol(l, mu, nu) * T_diag[mu, l]
                         for mu in range(8) for l in range(8))
            components.append(sp.simplify(value))
        return components


    divergence = {s: divergence_of(christoffel[s]) for s in SIGNS}
    for s in SIGNS:
        nonzero = [NAMES[nu] for nu in range(8) if divergence[s][nu] != 0]
        say(f"sign of sin z = {s:+d}: components of the divergence that are not "
            "identically zero: nu = " + ", ".join(nonzero))
    '''),
    md(r"""
    The record (formula `energy_exchange`, and the lead's independent check) says,
    with $h_4 = b_4'/(2b_4) - a_4'$:
    $\nabla_\mu T^\mu{}_{x_4} = -\partial_4\rho - 3a_4'(\rho + p_3)
    - 3h_4(\rho + p_t) - h_4(\rho + p_0)$,
    $\nabla_\mu T^\mu{}_{x_0} = \partial_0 p_0 + 3H\cot z\,(p_0 - p_t)$, and
    the other six components vanish identically. The next cell writes our eight
    components with the record's plain names (`rho_4` for $\partial_4\rho$, `p0_0`
    for $\partial_0 p_0$), translates the record's formula, and checks all eight
    components against it and against these two lines, for both signs.
    """),
    code(r'''
    rho_4, p0_0, p3s, pts, p0s = sp.symbols("rho_4 p0_0 p3 pt p0", real=True)
    rho_s = sp.Symbol("rho", real=True)  # the plain symbol for rho


    def plain_t(expression):
        """Write the derivatives and functions as the plain symbols of the record."""
        expression = expression.subs({sp.Derivative(rho_f, x[4]): rho_4,
                                      sp.Derivative(p0_f, x[0]): p0_0})
        expression = expression.subs({p3_f: p3s, pt_f: pts, p0_f: p0s, rho_f: rho_s})
        return plain(expression)


    NAMES_T = dict(NAMES_SYMPY, rho_4=rho_4, p0_0=p0_0, p3=p3s, pt=pts, p0=p0s, rho=rho_s)
    record_divergence = sp.sympify(from_wolfram(FORMULAS["energy_exchange"][0]),
                                   locals=NAMES_T)
    h4s = b4ps / (2 * b4s) - a4ps  # the rate h4 of the block, with plain symbols
    x4_line = (-rho_4 - 3 * a4ps * (rho_s + p3s) - 3 * h4s * (rho_s + pts)
               - h4s * (rho_s + p0s))
    x0_line = p0_0 + 3 * Hs * sp.cot(zs) * (p0s - pts)
    agree = all(sp.simplify(plain_t(divergence[s][n]) - record_divergence[n]) == 0
                for s in SIGNS for n in range(8))
    check(agree and recorded(THEORY_WL, "energy_exchange_equation") == "PASS"
          and recorded(THEORY_PY, "energy_exchange_equation") == "PASS",
          "the eight components agree with the record formula energy_exchange",
          record=f"{THEORY_WL} and {THEORY_PY}, check energy_exchange_equation")
    check(all(sp.simplify(plain_t(divergence[s][4]) - x4_line) == 0 for s in SIGNS)
          and recorded(LEAD, "divergence_x4_component") == "PASS",
          "nabla_mu T^mu_x4 = -d4 rho - 3 a4' (rho + p3) - 3 h4 (rho + p_t) "
          "- h4 (rho + p0)",
          record=f"{LEAD}, check divergence_x4_component")
    check(all(sp.simplify(plain_t(divergence[s][0]) - x0_line) == 0 for s in SIGNS)
          and recorded(LEAD, "divergence_x0_component") == "PASS",
          "nabla_mu T^mu_x0 = d0 p0 + 3 H cot z (p0 - p_t)",
          record=f"{LEAD}, check divergence_x0_component")
    check(all(divergence[s][n] == 0 for s in SIGNS for n in (1, 2, 3, 5, 6, 7))
          and recorded(LEAD, "divergence_other_components_zero") == "PASS",
          "the components x1, x2, x3, x5, x6, x7 vanish identically",
          record=f"{LEAD}, check divergence_other_components_zero")
    say(f"nabla_mu T^mu_x4 = {x4_line}")  # rho_4 = d rho/d x4, b4p = d b4/d x4
    say(f"nabla_mu T^mu_x0 = {x0_line}")  # p0_0 = d p0/d x0
    '''),
    md(r"""
    ## 14. The x4 identity read as a first law

    Conservation, $\nabla_\mu T^\mu{}_{x_4} = 0$, says
    $\partial_4\rho = -3a_4'(\rho + p_3) - 3h_4(\rho + p_t) - h_4(\rho + p_0)$. Here
    is why. At fixed $x_0$ take a small box of coordinate size 1 in each of the seven
    directions other than $x_4$. Its 3-space volume is $V_3 = f_1 f_2 f_3 =
    e^{3a_4}$, its extra-time volume $V_t = f_5 f_6 f_7 =
    e^{-3a_4}b_4^{3/2}(\sin^2 z)^{1/4}$, its hidden length $V_0 = |f_0| =
    e^{-a_4}b_4^{1/2}|\cot z|$, and its 7-volume $V_7 = V_3 V_t V_0 =
    e^{-a_4}b_4^2|\cot z|(\sin^2 z)^{1/4} = \sqrt{|g|}$. The first law of
    thermodynamics (energy changes by minus pressure times change of volume), applied
    to each family of directions, would say that the energy $\rho V_7$ in the box
    changes as $\frac{d}{dx_4}(\rho V_7) = -p_3\frac{V_7}{V_3}\frac{dV_3}{dx_4}
    - p_t\frac{V_7}{V_t}\frac{dV_t}{dx_4} - p_0\frac{V_7}{V_0}\frac{dV_0}{dx_4}$. The
    next cell checks with sympy, for both signs of $\sin z$ (and with the signed
    $V_0 = f_0$, whose sign cancels), that this is exactly the conservation identity.
    This is a reading of the identity (an interpretation, not an extra result):
    dividing by $V_7$, $d\rho + \rho\,dV_7/V_7 = -p_3\,dV_3/V_3 - p_t\,dV_t/V_t
    - p_0\,dV_0/V_0$, with $dV_3/V_3 = 3a_4'\,dx_4$ and $dV_t/V_t = 3\,dV_0/V_0 =
    3h_4\,dx_4$. While 3-space inflates a positive $p_3$ takes energy out of the box;
    while the block deflates ($h_4 < 0$) positive $p_t$ and $p_0$ put energy in; and
    the change of the 7-volume dilutes the energy density.
    """),
    code(r'''
    first_law_holds = True
    for s in SIGNS:
        block = sp.exp(-a4_function) * sp.sqrt(b4_function)  # e^(-a4) b4^(1/2)
        V3 = sp.exp(3 * a4_function)  # f1 f2 f3 = e^(3 a4)
        Vt = block ** 3 * (s * sp.sin(zs)) ** sp.Rational(1, 2)  # f5 f6 f7
        V0 = block * sp.cot(zs)  # f0, signed (its sign cancels below)
        V7 = V3 * Vt * V0  # sign(cot z) times sqrt|g|
        signed_volume = (sp.exp(-a4_function) * b4_function ** 2 * sp.cot(zs)
                         * (s * sp.sin(zs)) ** sp.Rational(1, 2))
        first_law = (sp.diff(rho_f * V7, x[4]) + p3_f * V7 / V3 * sp.diff(V3, x[4])
                     + pt_f * V7 / Vt * sp.diff(Vt, x[4])
                     + p0_f * V7 / V0 * sp.diff(V0, x[4]))
        # The first law says first_law = 0; it must be -V7 times the x4 divergence.
        first_law_holds = (first_law_holds
                           and sp.simplify(V7 - signed_volume) == 0
                           and sp.simplify(first_law + V7 * divergence[s][4]) == 0)
    check(first_law_holds,
          "V3 Vt V0 = sign(cot z) sqrt|g|, and the first law is the x4 identity")
    '''),
    md(r"""
    The next cell draws the four volumes along the deflating history
    $a_4 = AHx_4$, $b_4 = e^{\beta AHx_4}$ ($A = 1$, $\beta = \frac43$, $H = 0.25$)
    for $x_4$ from $0$ to $8$, each divided by its value at $x_4 = 0$: $V_3$ grows
    like $e^{3AHx_4}$, the block factor $e^{-a_4}b_4^{1/2}$ shrinks like
    $e^{-AHx_4/3}$, so $V_t$ shrinks like $e^{-AHx_4}$ and $V_0$ like
    $e^{-AHx_4/3}$, and $V_7 = e^{-a_4}b_4^2$ (times the constant
    $|\cot z|(\sin^2 z)^{1/4}$) grows like $e^{5AHx_4/3}$.
    """),
    code(r'''
    x4_axis = np.linspace(0.0, 8.0, 401)  # the time x4
    a4_history = A * H * x4_axis  # a4 along the history
    b4_history = np.exp(beta * A * H * x4_axis)  # b4 along the history (unit b4(0))
    V3_ratio = np.exp(3 * a4_history)  # V3(x4)/V3(0) = e^(3 a4)
    block_ratio = np.exp(-a4_history) * np.sqrt(b4_history)  # e^(-a4) b4^(1/2)
    Vt_ratio = block_ratio ** 3  # the three extra times
    V0_ratio = block_ratio  # the hidden direction
    V7_ratio = V3_ratio * Vt_ratio * V0_ratio  # e^(-a4) b4^2
    fig, ax = plt.subplots()
    ax.plot(x4_axis, V3_ratio, label="3-space volume $V_3$ (inflates)")
    ax.plot(x4_axis, Vt_ratio, "--", label="extra-time volume $V_t$ (deflates)")
    ax.plot(x4_axis, V0_ratio, "-.", label="hidden length $V_0$ (deflates)")
    ax.plot(x4_axis, V7_ratio, ":", color="black",
            label="7-volume $V_7 = V_3 V_t V_0 = \\sqrt{|g|}$")
    ax.set_yscale("log")
    ax.set_xlabel("time $x_4$")
    ax.set_ylabel("volume divided by its value at $x_4 = 0$")
    ax.set_title("Volumes along the history ($A = 1$, $\\beta = 4/3$, $H = 0.25$)")
    ax.legend(fontsize=8)
    save_figure(fig, "volumes_first_law",
                "The 3-space volume $V_3 = e^{3a_4}$ (solid), the extra-time volume "
                "$V_t = e^{-3a_4}b_4^{3/2}(\\sin^2 z)^{1/4}$ (dashed), the hidden "
                "length $V_0 = e^{-a_4}b_4^{1/2}|\\cot z|$ (dash-dotted) and the "
                "7-volume $V_7 = \\sqrt{|g|} = e^{-a_4}b_4^2|\\cot z|(\\sin^2 z)^{1/4}$ "
                "(dotted) of a coordinate box at fixed $x_0$, along the deflating "
                "history $a_4 = AHx_4$, $b_4 = e^{4AHx_4/3}$ with $A = 1$, $H = 0.25$, "
                "for $x_4$ from $0$ to $8$, each divided by its value at $x_4 = 0$; "
                "logarithmic vertical axis. $V_3$ grows like $e^{3AHx_4}$, $V_t$ "
                "shrinks like $e^{-AHx_4}$, $V_0$ like $e^{-AHx_4/3}$, and $V_7$ grows "
                "like $e^{5AHx_4/3}$. Read as a first law, the conservation identity "
                "says: while 3-space inflates a positive $p_3$ takes energy out of the "
                "box, while the block deflates positive $p_t$ and $p_0$ put energy in, "
                "and the growing 7-volume dilutes the energy density.")
    '''),
    md(r"""
    ## 15. The x0 identity: the balance along the hidden direction

    Conservation along $x_0$ says $\partial_0 p_0 = -3H\cot z\,(p_0 - p_t)$: the
    hidden pressure balances against the extra-time pressure only (3-space does not
    depend on $x_0$). If the entries do not depend on $x_0$, it forces $p_0 = p_t$
    wherever $\cot z \neq 0$. If $p_t = P$ is a constant, every solution is
    $p_0 = P + c\,(\sin^2 z)^{-1/4}$ with a constant $c$; only $c = 0$ is independent
    of $x_0$. The next cell checks this with sympy for both signs of $\sin z$, then
    the same identity in the hidden coordinate $y = \ln|\sin z|/(6H)$ used by the
    Kohn-Sham solver of the book: $dy/dx_0 = \cot z$, and the $x_0$ component is
    $\cot z\,[p_0'(y) + 3H(p_0 - p_t)]$ (the lead's checks); in $y$ the profiles are
    $p_0 = P + c\,e^{-3Hy}$.
    """),
    code(r'''
    P, c = sp.symbols("P c", real=True)  # P = p_t (a constant) and the constant c
    y = sp.symbols("y", real=True)
    P0, PT = [sp.Function(n)(y) for n in ("P0", "PT")]  # p0 and p_t as functions of y
    profiles_hold, jacobian_holds, y_form_holds = True, True, True
    for s in SIGNS:
        profile = P + c * (s * sp.sin(zs)) ** sp.Rational(-1, 2)  # p0 = P + c |sin z|^(-1/2)
        balance = sp.diff(profile, x[0]) + 3 * Hs * sp.cot(zs) * (profile - P)
        profiles_hold = profiles_hold and sp.simplify(balance) == 0
        y_of_x0 = sp.log(s * sp.sin(zs)) / (6 * Hs)  # y = ln|sin z|/(6 H)
        jacobian_holds = (jacobian_holds
                          and sp.simplify(sp.diff(y_of_x0, x[0]) - sp.cot(zs)) == 0)
        in_x0 = (sp.diff(P0.subs(y, y_of_x0), x[0])
                 + 3 * Hs * sp.cot(zs) * (P0.subs(y, y_of_x0) - PT.subs(y, y_of_x0)))
        in_y = sp.cot(zs) * (sp.diff(P0, y).subs(y, y_of_x0)
                             + 3 * Hs * (P0.subs(y, y_of_x0) - PT.subs(y, y_of_x0)))
        y_form_holds = y_form_holds and sp.simplify(in_x0 - in_y) == 0
    check(profiles_hold, "p0 = P + c (sin^2 z)^(-1/4) solves the x0 identity for every c")
    check(jacobian_holds and recorded(LEAD, "ks_coordinate_jacobian") == "PASS",
          "y = ln|sin z|/(6 H) has dy/dx0 = cot z",
          record=f"{LEAD}, check ks_coordinate_jacobian")
    check(y_form_holds and recorded(LEAD, "ks_coordinate_form") == "PASS",
          "x0 component = cot z [p0'(y) + 3 H (p0 - p_t)]",
          record=f"{LEAD}, check ks_coordinate_form")
    '''),
    md(r"""
    The next cell draws the profiles $p_0 = P + c\,(\sin^2 z)^{-1/4}$ for $P = 1$ and
    five values of $c$, across the fold $z = \pi/2$ into the second half of the cell,
    and checks numerically on the drawn grid (with numpy's `np.gradient`, a
    finite-difference derivative) that each profile satisfies the balance: the left
    side minus the right side is small compared with the terms.
    """),
    code(r'''
    z_grid = np.linspace(0.1, np.pi - 0.1, 2001)  # z across the fold at pi/2
    x0_grid = z_grid / (6 * H)  # the matching x0 = z/(6 H)
    fig, ax = plt.subplots()
    worst = 0.0  # the largest relative residual of the balance on the grid
    for c_value in (-0.4, -0.2, 0.0, 0.2, 0.4):
        p0_values = 1.0 + c_value * (np.sin(z_grid) ** 2) ** (-1 / 4)  # P = 1
        slope = np.gradient(p0_values, x0_grid)  # d p0/d x0, by finite differences
        rhs = -3 * H / np.tan(z_grid) * (p0_values - 1.0)
        # The size of the terms; 1 (the size of P) is added, so that for the flat
        # profile c = 0, whose terms are zero, rounding noise is not divided by zero.
        scale = 1.0 + np.abs(slope).max() + np.abs(rhs).max()
        # [5:-5] leaves out five points at each end, where np.gradient is less exact.
        worst = max(worst, np.abs(slope - rhs)[5:-5].max() / scale)
        style = "-" if c_value == 0.0 else "--"
        ax.plot(z_grid, p0_values, style, label=f"$c = {c_value:g}$")  # g: short form
    check(worst < 1e-4, "the drawn profiles satisfy the x0 balance on the grid")
    ax.axvline(np.pi / 2, color="gray", linewidth=0.8)  # the fold
    ax.set_ylim(-0.5, 2.5)
    ax.set_xlabel("$z = 6 H x_0$ (fold at $\\pi/2$)")
    ax.set_ylabel("$p_0$ (with $p_t = 1$)")
    ax.set_title("Pressure profiles allowed by the balance along $x_0$")
    ax.legend(fontsize=8)
    save_figure(fig, "hidden_balance",
                "The hidden-direction pressure profiles $p_0 = P + c\\,(\\sin^2 z)^{-1/4}$ "
                "that satisfy the conservation identity along $x_0$, "
                "$\\partial_0 p_0 = -3H\\cot z\\,(p_0 - p_t)$, when $p_t = P = 1$ is "
                "constant, for $c = -0.4, -0.2, 0, 0.2, 0.4$; horizontal axis "
                "$z = 6Hx_0$ from $0.1$ to $\\pi - 0.1$, across the fold $z = \\pi/2$ "
                "(gray line) into the second half of the cell, vertical axis $p_0$ in "
                "units of energy per unit volume. Only $c = 0$ (solid line) is "
                "independent of $x_0$, and it has $p_0 = p_t$; every other profile is "
                "flat at the fold, where $\\cot z = 0$, and grows in size like "
                "$|\\sin z|^{-1/2}$ towards $z = 0$ and $z = \\pi$, where the extra "
                "times degenerate.")
    report("largest relative residual of the balance on the grid", f"{worst:.1e}")
    '''),
    md(r"""
    ## 16. The source that the record history needs obeys both identities

    The field equations of gravity (Chapter 12 of the book) determine the source
    that a given history needs. For the record history $a_4 = Hx_4$,
    $b_4 = e^{(4/3)Hx_4}$ (so $a_4' = H$ and $h_4 = -H/3$) the record of the
    corrected metric lists it, as $\kappa T - \Lambda$, for Einstein gravity and for
    the author's Lovelock weights (`Revision/metric_warped/results/warped-metric.json`,
    key `history_source`); the field-equations record finds the same source, with
    $p_0 = p_t$ and no off-diagonal entry. Its entries depend on $x_4$ only. A
    constant $\Lambda$ changes $\rho$ and every pressure by opposite constants and
    leaves both identities unchanged, so the next cell checks directly that each
    listed source obeys the $x_4$ identity and has $p_0 = p_t$ (which, for entries
    free of $x_0$, is the $x_0$ identity). It prints the Einstein source.
    """),
    code(r'''
    WARPED = "Revision/metric_warped/results/warped-metric.json"
    sources = json.loads(repository_file(WARPED).read_text(encoding="utf-8"))[
        "history_source"]
    x4s = sp.Symbol("x4", real=True)  # the time as a plain symbol
    a4p_history, h4_history = Hs, sp.Rational(4, 3) * Hs / 2 - Hs  # H and -H/3
    sources_conserved = True
    for key in ("einstein_A1_beta43", "author_weights_A1_beta43"):
        entry = {name: sp.sympify(text, locals={"H": Hs, "x4": x4s})
                 for name, text in sources[key].items()}
        rho_h, p3_h, pt_h, p0_h = -entry["-rho"], entry["p3"], entry["p_t"], entry["p0"]
        x4_identity = (-sp.diff(rho_h, x4s) - 3 * a4p_history * (rho_h + p3_h)
                       - 3 * h4_history * (rho_h + pt_h) - h4_history * (rho_h + p0_h))
        sources_conserved = (sources_conserved and sp.simplify(x4_identity) == 0
                             and sp.simplify(p0_h - pt_h) == 0)
        if key == "einstein_A1_beta43":
            say(f"Einstein: rho = {rho_h}, p3 = {p3_h}, p_t = p0 = {pt_h}")
    A4_PY = "Revision/field_equations_a4/reports/python-a4-report.json"
    check(sources_conserved
          and recorded(A4_REPORT, "author_weights_history_source") == "PASS"
          and recorded(A4_PY, "author_weights_history_source") == "PASS",
          "the history source (Einstein, author's weights) obeys the x4 identity",
          record=f"{A4_REPORT} and {A4_PY}, check author_weights_history_source")
    check(recorded(A4_REPORT, "independent_components") == "PASS"
          and recorded(A4_PY, "independent_components") == "PASS",
          "the field equations need p0 = p_t and no off-diagonal source",
          record=f"{A4_REPORT} and {A4_PY}, check independent_components")
    '''),
    md(r"""
    ## 17. The last check

    The last cell checks that the five figures are saved with their captions and
    prints the number of checks that passed.
    """),
    code(r'''
    captions = json.loads(output_file(CAPTION_FILE).read_text(encoding="utf-8"))
    expected_files = ["09a_1_kinetic_weights.png", "09a_2_tensor_heat_map.png",
                      "09a_3_diagonal_parts.png", "09a_4_volumes_first_law.png",
                      "09a_5_hidden_balance.png"]
    check(sorted(captions) == expected_files and all(
        output_file(f"{FIGURE_FOLDER}/{name}").is_file() for name in expected_files),
        "the five figures of this notebook are saved and captioned")
    all_checks_passed()
    '''),
    md(r"""
    ## 18. What this notebook showed

    - At a point of the deflating history of the corrected metric the
      energy-momentum tensor of dirac16complex00 is a real $8 \times 8$ table whose
      lowered form is symmetric; its diagonal entries are $T^\mu{}_\mu = L_0 - K_\mu$,
      so the energy density is $\rho = -\sum_{\mu \neq x_4}K_\mu + mS + U$ and each
      pressure is the sum of the other seven kinetic terms minus $mS + U$ (exact
      statements of the record, confirmed here numerically).
    - The trace is $7\sum_\mu K_\mu - 8(mS + U)$ for every configuration; on shell
      $\sum_\mu K_\mu = (m + U')S$, $L_0 = SU' - U$ and the trace is
      $-mS + 3\lambda S^2$.
    - The spin connection drops out of the diagonal entries, because
      $\{\gamma^\mu, \Omega_\mu\} = 0$ for each direction, but it enters off-diagonal
      entries such as $T^{x_4}{}_{x_5}$ (not the flow piece $K^{x_4}{}_{x_1}$ along
      3-space); summed, $\gamma^\mu\Omega_\mu = c_g\gamma^{(x_0)} + v_g\gamma^{(x_4)}$
      with $c_g = \frac32He^{a_4}b_4^{-1/2}$ and $v_g = b_4'/b_4 - a_4'/2$.
    - The corrected metric has 21 nonzero Christoffel symbols, the record's list
      exactly, for both signs of $\sin z$, and conservation of a diagonal tensor is
      exactly two conditions:
      $\partial_4\rho = -3a_4'(\rho + p_3) - 3h_4(\rho + p_t) - h_4(\rho + p_0)$ (each
      family of directions dilutes $\rho$ plus its own pressure: a first law for the
      volumes $V_3$, $V_t$, $V_0$ and the 7-volume $\sqrt{|g|}$) and
      $\partial_0 p_0 = -3H\cot z\,(p_0 - p_t)$ (a balance between the hidden and the
      extra-time pressures, which forces $p_0 = p_t$ for $x_0$-independent entries,
      the same condition that the field equations of gravity impose).
    - The source that the record history needs, for Einstein gravity and for the
      author's weights, obeys both identities.
    - Status: the identities are PROVED in the record (exact, Wolfram and sympy);
      this notebook re-derives the two conservation identities exactly and confirms
      the tensor identities numerically at one point. The parameter values are
      choices of this notebook, not results.
    """),
]

if __name__ == "__main__":
    raise SystemExit(run_builder(__file__))
