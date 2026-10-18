#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
"""Builder of Notebook 09c, "The full energy-momentum tensor of a condensate"
(textbook "Universes in Pairs", chapter 09).

The notebook Revision/textbook/notebooks/09c_condensate_tensor.ipynb is BUILT from this
file by Revision/textbook/tools/nbkit.py (never edit the .ipynb by hand):

    python Revision/textbook/tools/nbkit.py build \
        Revision/textbook/notebooks/src/09c_condensate_tensor.py --date YYYY-MM-DD
    python Revision/textbook/tools/nbkit.py check \
        Revision/textbook/notebooks/src/09c_condensate_tensor.py

The metric is the corrected metric of 2026-10-16 (version 2; Revision/SPEC.md section 1).
It computes the complete 8 x 8 energy-momentum tensor of the condensates of
dirac16complex00 (off-diagonal entries included), reproduces the field-equations record's
statements about them (36 nonzero off-diagonal entries, combinations of 24 three-gamma
bilinears with the listed coefficients; the exact witnesses with a diagonal tensor on the
histories with constant e^(2 a4)/b4), and tests the conservation of the full tensor
numerically with finite differences, with a negative control.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools"))
from nbkit import code, md, run_builder  # noqa: E402

FIGURES = [
    "Revision/textbook/figures/09c_1_generic_condensate.png",
    "Revision/textbook/figures/09c_2_offdiagonal_entries.png",
    "Revision/textbook/figures/09c_3_witness_condensate.png",
    "Revision/textbook/figures/09c_4_conservation_convergence.png",
    "Revision/textbook/figures/09c_5_divergence_components.png",
]

FACTS = {
    "id": "09c",
    "name": "09c_condensate_tensor",
    "title": "The full energy-momentum tensor of a condensate",
    "purpose": (
        "It computes all 64 entries of the energy-momentum tensor of condensates "
        "Phi = e^(a4/2) b4^(-1) chi of the commuting field dirac16complex00 in the "
        "corrected metric of 2026-10-16, including the off-diagonal entries that the "
        "spin connection and the gravitational term of the field equation produce, "
        "finds the 36 nonzero off-diagonal entries of a generic condensate and checks "
        "that each is a fixed combination of one or two of 24 three-gamma bilinears "
        "with exactly the coefficients that the record lists, builds the exact "
        "condensates whose tensor is diagonal on the histories with constant "
        "e^(2 a4)/b4 and reproduces their frequencies omega and their S from the record "
        "(S up to one common factor), and tests the conservation of the full tensor "
        "along a curved history of a4 and b4 with finite differences of shrinking step, "
        "with a negative control that leaves out the gravitational term of the "
        "condensate equation; five teaching plots."
    ),
    "records": [
        ["Revision/algebra/gammas.json",
         "the author's gamma matrices and the matrix C (the fixture)"],
        ["Revision/theory/field-theory.json",
         "the formulas of the spin connection, of the tensor and of the exact solutions"],
        ["Revision/theory/reports/wolfram-field-theory.json",
         "the exact nonlinear homogeneous solution conserves its tensor; conservation "
         "on shell"],
        ["Revision/field_equations_a4/a4-equations.json",
         "the 36 off-diagonal entries of the condensate tensor: bilinears and "
         "coefficients of each"],
        ["Revision/field_equations_a4/reports/wolfram-a4-report.json",
         "the condensate tensor: diagonal kinetic part, 36 off-diagonal entries, the "
         "diagonal witnesses on the histories with constant e^(2 a4)/b4"],
        ["Revision/field_equations_a4/reports/python-a4-report.json",
         "the same statements, verified independently with sympy"],
    ],
    "packages": ["numpy", "sympy", "matplotlib"],
    "needs_rust": [],
    "expected_seconds": 20,
    "timeout_seconds": 300,
    "files_written": ["Revision/textbook/figures/09c.captions.json"] + FIGURES,
    "final_lines": [
        "PASS the five figures of this notebook are saved and captioned",
        "ALL 25 CHECKS PASSED (notebook 09c)",
    ],
    "troubleshooting": [
        ["\"KeyError\" with the words \"has no check\"",
         "the notebook asks a Revision report for the verdict of one of its checks, and "
         "the report in your copy of the repository does not contain that check: your "
         "copy is older or newer than the notebook. Run `git pull` in the repository "
         "folder, then run the notebook again."],
    ],
}

CELLS = [
    md(r"""
    ## 1. What this notebook computes

    A condensate (a field that depends on the time $x_4$ only) has the same energy
    density and pressure in every direction. That does not yet make it a *perfect
    fluid*: a perfect fluid at rest has a diagonal energy-momentum tensor, and the
    spin connection and the gravitational term of the field equation put entries off
    the diagonal. This notebook computes all 64 entries of the tensor of condensates
    $\Phi = e^{a_4/2}b_4^{-1}\chi$ of dirac16complex00 in the corrected metric of
    2026-10-16, with the two functions $a_4(x_4)$ and $b_4(x_4)$, and

    - shows the tensor of a generic condensate as a heat map and counts its nonzero
      off-diagonal entries: 36, at every point of every history; 30 at a moment with
      $4a_4' = b_4'/b_4$, when the six entries between the hidden direction and
      3-space vanish;
    - shows how four of these entries depend on the rate $a_4'$ (at a fixed
      $b_4'/b_4$);
    - checks that each of the 36 entries is a fixed combination of one or two of 24
      *three-gamma bilinears* $\bar\Phi\gamma^{(a)}\gamma^{(b)}\gamma^{(c)}\Phi$, with
      exactly the coefficients that the Revision record lists for it;
    - builds the exact condensates of the Revision record for which all 24
      bilinears vanish, on the histories along which $e^{2a_4}/b_4$ stays constant,
      and checks that their tensor is diagonal at 36 points with different $a_4$,
      $a_4'$ and $z$ (the record states it for all of them);
    - shows why $S$ of these condensates is never negative, and reproduces the
      record's numbers for them: their frequencies $\omega = 4, 3, 4$ exactly, and
      its three values of $S$ up to one common factor (the record's columns are not
      of length 1);
    - tests the conservation $\nabla_\mu T^\mu{}_\nu = 0$ of the full tensor of a
      condensate along a curved (non-linear) history of $a_4$ and $b_4$ with finite
      differences whose step shrinks, and contrasts it with a configuration that
      leaves out the gravitational part $c_g\gamma^{(4)}\gamma^{(0)}$ of the
      condensate equation (a negative control);
    - draws five teaching plots.
    """),
    md(r"""
    ## 3. The words used in this notebook

    - **Condensate**: a configuration that depends only on the time $x_4$.
    - **Diagonal / off-diagonal entry**: the entry $T^\nu{}_\mu$ with $\nu = \mu$ /
      with $\nu \neq \mu$. Off-diagonal entries describe flows of energy and momentum
      (for example $T^{x_4}{}_{x_1}$ is a flow of momentum along $x_1$) and stresses
      that shear.
    - **Perfect fluid (at rest)**: matter whose energy-momentum tensor is diagonal,
      with the energy density and the pressures on the diagonal.
    - **Three-gamma bilinear**: the number $\bar\Phi\gamma^{(a)}\gamma^{(b)}
      \gamma^{(c)}\Phi$ for three different directions $a$, $b$, $c$; we write it
      $B(a\,b\,c)$.
    - **Least squares**: the method that finds the numbers $c_1, c_2$ for which
      $c_1 u + c_2 v$ comes closest to a given column $w$; when $w$ is exactly such a
      combination, the remaining difference (the residual) is zero.
    - **Eigenvector, joint eigenvector**: a column $v$ with $Mv = \mu v$ for a
      number $\mu$ (the eigenvalue); a joint eigenvector of several matrices is an
      eigenvector of each of them.
    - **Witness**: an explicit example that proves that something exists.
    - **Trace** of a square matrix: the sum of its diagonal entries.
    - **Rank** of a matrix: the number of its independent columns.
    - **Projector**: a matrix $\Pi$ with $\Pi^2 = \Pi$; it keeps some columns
      unchanged and sends others to zero, and its trace is the dimension of the
      space it keeps.
    - **Sector**: the columns $v$ of one eigenvalue space of $A$ with fixed signs
      $P_1v = \pm v$, $P_2v = \pm v$, $P_3v = \pm v$ (the matrices $P_k$ are defined
      in section 8).
    - **Frequency** $\omega$ (the Greek letter omega): the number in the factor
      $e^{-i\omega x_4} = \cos(\omega x_4) - i\sin(\omega x_4)$; a field with this
      factor repeats itself after the time $2\pi/\omega$. It has nothing to do with
      the equation of state $w = p/\rho$ of the other examples of this chapter.
    - **Finite difference**: the derivative approximated by
      $\frac{F(x + h) - F(x - h)}{2h}$; its error falls like $h^2$ when the step $h$
      shrinks, until rounding errors take over.
    - **Covariant divergence**: $\nabla_\mu T^\mu{}_\nu = \partial_\mu T^\mu{}_\nu
      + \Gamma^\mu{}_{\mu\lambda}T^\lambda{}_\nu - \Gamma^\lambda{}_{\mu\nu}
      T^\mu{}_\lambda$, with the Christoffel symbols $\Gamma$.
    - **Negative control**: a test case built so that the check must FAIL; it shows
      that the check can detect an error.
    """),
    md(r"""
    ## 4. The physical and mathematical situation

    **The condensates.** For a field that depends on $x_4$ only, write
    $\Phi = F\chi$ with $F = e^{a_4/2}b_4^{-1}$. The field equation of
    dirac16complex00 in the corrected metric reduces to $\partial_4\chi = A\chi$ with
    $A = -V\gamma^{(4)} + c_g\gamma^{(4)}\gamma^{(0)}$, the effective mass
    $V = m + \lambda S$ and the gravitational coefficient
    $c_g = \frac32He^{a_4}b_4^{-1/2}$, where $S = \bar\Phi\Phi =
    e^{a_4}b_4^{-2}\chi^\dagger C\chi$ and $\chi^\dagger C\chi$ is constant. In general
    $V$ and $c_g$ change in time, and the linear system has no closed form
    (Notebook 09b). At one point the jet of a condensate is $\Phi$ = a column and
    $\partial_4\Phi = (A - v_g)\Phi$ with $v_g = b_4'/b_4 - a_4'/2$ (the product
    rule: $F'/F = -v_g$).

    **The tensor.** $T^\nu{}_\mu = \delta^\nu_\mu L_0 - \frac14(\bar\Phi\gamma^\nu
    D_\mu\Phi - D_\mu\bar\Phi \gamma^\nu\Phi + \bar\Phi\gamma_\mu D^\nu\Phi
    - D^\nu\bar\Phi \gamma_\mu\Phi)$ with $D_\mu\Phi = \partial_\mu\Phi
    + \Omega_\mu\Phi$. For a condensate $\partial_\mu\Phi = 0$ for $\mu \neq x_4$,
    but $D_\mu\Phi = \Omega_\mu\Phi$ is not zero along the hidden direction, 3-space
    and the extra times, and $\partial_4\Phi$ contains the term $c_g\gamma^{(4)}
    \gamma^{(0)}$ of $A$. These fill the off-diagonal entries.

    **The record** (`Revision/field_equations_a4/reports/wolfram-a4-report.json` and
    the independent `python-a4-report.json`): for a condensate the diagonal is
    $T^{x_4}{}_{x_4} = -VS + L_0$ and $T^\mu{}_\mu = L_0$ otherwise, and
    $T^{x_4}{}_{x_0} = T^{x_0}{}_{x_4} = 0$; 36 ordered pairs $(\nu, \mu)$ carry
    nonzero off-diagonal entries (the pairs $x_0$-$x_i$, $x_i$-$x_4$, $x_i$-$x_t$ and
    $x_4$-$x_t$, with $i$ in 3-space and $t$ an extra time), each a combination of
    the 24 bilinears with $\{a, b, c\} = \{x_0, i, x_4\}$ (3), $\{x_0, i, t\}$ (9),
    $\{i, x_4, t\}$ (9) or $\{x_0, x_4, t\}$ (3), with coefficients that depend on $H$,
    $a_4$, $a_4'$, $b_4$, $b_4'/b_4$ and $z$; and exact witnesses for which all 24
    vanish exist on the histories with a constant $k = e^{2a_4}/b_4$ (for other
    histories the record does not decide). All of this holds for all functions $a_4$
    and $b_4$ and every real $z$. The field equations for $a_4$ and $b_4$ require,
    among other conditions, that every off-diagonal entry of the source vanishes (for
    a coupling $\kappa \neq 0$; record `Revision/field_equations_a4/a4-equations.json`,
    entries `generalSource.offDiagonal` and
    `fields.dirac16complex00.offDiagonalConditions`): a condensate meets this
    condition only if all 24 bilinears vanish, as for the witnesses.

    **Conservation.** The record proves $\nabla_\mu T^\mu{}_\nu = 0$ for every
    solution (the Noether identity of coordinate invariance) and checks it exactly
    on the condensate (`exact_solution_nonlinear_homogeneous_C`). This notebook tests
    it numerically, for all eight components and with the off-diagonal entries
    included, along the non-linear history $a_4 = 0.3x_4 + 0.05x_4^2$,
    $b_4 = e^{0.4x_4 - 0.02x_4^2}$ (a choice of this notebook).
    """),
    md(r"""
    ## 5. The gammas, the geometry and the tensor at a point

    The next cell reads the Revision gammas and $C$ from the fixture
    `Revision/algebra/gammas.json` and defines two helpers for the Revision
    reports: `record_entry(path, name)` returns the whole entry of one check (its
    name, its verdict and its detail text), and `recorded(path, name)` returns only
    its verdict (PASS or FAIL).
    """),
    code(r'''
    import numpy as np  # arrays of numbers, matrices, linear algebra

    fixture = json.loads(
        repository_file("Revision/algebra/gammas.json").read_text(encoding="utf-8"))
    gamma = [np.array(rows, dtype=float) for rows in fixture["gamma"]]  # x0, ..., x7
    eta = np.array(fixture["eta"], dtype=float)  # (+1, +1, +1, +1, -1, -1, -1, -1)
    C = np.array(fixture["C"], dtype=float)  # gamma^(x0) gamma^(x1) gamma^(x2) gamma^(x3)
    I16 = np.eye(16)  # the 16 x 16 unit matrix
    g4, g0 = gamma[4], gamma[0]  # gamma^(x4) and gamma^(x0)
    NAMES = ["x0", "x1", "x2", "x3", "x4", "x5", "x6", "x7"]  # the author's coordinates


    def record_entry(path, name):
        """The entry (name, verdict, detail) of the check name in the report path."""
        report_data = json.loads(repository_file(path).read_text(encoding="utf-8"))
        for item in report_data["checks"]:
            if item["name"] == name:
                return item
        raise KeyError(f"{path} has no check {name}")


    def recorded(path, name):
        """The verdict (PASS or FAIL) of the check name in the Revision report path."""
        return record_entry(path, name)["verdict"].upper()  # some reports write "pass"


    say("The gammas, C and the two report helpers are ready.")
    '''),
    md(r"""
    The next cell defines the geometry at one point, the same functions as in the
    first example of this chapter: `frame_factors(a4, b4, z)` returns the eight
    vielbein factors $f_a$ in the order $x_0, \dots, x_7$
    ($e^{-a_4}b_4^{1/2}\cot z$, $e^{a_4}$ three times, $1$,
    $e^{-a_4}b_4^{1/2}(\sin^2 z)^{1/12}$ three times), and
    `spin_connection(a4, a4p, b4, u, z, H)`, with $u = b_4'/b_4$, returns the eight
    $16 \times 16$ matrices $\Omega_\mu$ of the record's formula `Omega_components`:
    $\Omega_{x_0} = \frac12h_4s_b\cot z\,\gamma^{(0)}\gamma^{(4)}$,
    $\Omega_{x_i} = \frac12a_4'e^{a_4}\gamma^{(i)}\gamma^{(4)}$,
    $\Omega_{x_t} = \frac12(\sin^2 z)^{1/12}(h_4s_b\gamma^{(4)}\gamma^{(t)}
    + H\gamma^{(0)}\gamma^{(t)})$ and $\Omega_{x_4} = 0$, with
    $s_b = e^{-a_4}b_4^{1/2}$ and $h_4 = u/2 - a_4'$.
    """),
    code(r'''
    def frame_factors(a4, b4, z):
        """The eight factors f_a of the diagonal vielbein, in the order x0, ..., x7."""
        block = np.exp(-a4) * np.sqrt(b4)  # e^(-a4) b4^(1/2)
        extra = block * np.abs(np.sin(z)) ** (1 / 6)  # times (sin^2 z)^(1/12)
        return np.array([block / np.tan(z)] + [np.exp(a4)] * 3 + [1.0] + [extra] * 3)


    def spin_connection(a4, a4p, b4, u, z, H):
        """The eight matrices Omega_mu (record formula Omega_components), u = b4'/b4."""
        s_b = np.exp(-a4) * np.sqrt(b4)  # e^(-a4) b4^(1/2)
        h4 = u / 2 - a4p  # the rate of the block of x0 and the extra times
        root = np.abs(np.sin(z)) ** (1 / 6)  # (sin^2 z)^(1/12)
        omega = [np.zeros((16, 16)) for _ in range(8)]  # Omega_x4 stays 0
        omega[0] = 0.5 * h4 * s_b / np.tan(z) * g0 @ g4
        for i in range(1, 4):  # the three 3-space directions x1, x2, x3
            omega[i] = 0.5 * a4p * np.exp(a4) * gamma[i] @ g4
        for t in range(5, 8):  # the three extra times x5, x6, x7
            omega[t] = 0.5 * root * (h4 * s_b * g4 @ gamma[t] + H * g0 @ gamma[t])
        return omega


    say("frame_factors and spin_connection are defined.")
    '''),
    md(r"""
    The next cell defines `bar(vector)`, the Dirac adjoint $\bar\Phi = \Phi^\dagger C$,
    and `energy_momentum(phi, dphi, m, lam, a4, a4p, b4, u, z, H)`, which returns the
    64 entries $T^\nu{}_\mu$ (row $\nu$, column $\mu$) of the record's tensor
    $T^\nu{}_\mu = \delta^\nu_\mu L_0 - \frac14(\bar\Phi\gamma^\nu D_\mu\Phi
    - D_\mu\bar\Phi \gamma^\nu\Phi + \bar\Phi\gamma_\mu D^\nu\Phi
    - D^\nu\bar\Phi \gamma_\mu\Phi)$ from the jet of the field at one point (the 16
    values of $\Phi$ and the eight columns $\partial_\mu\Phi$). The tensor of a
    configuration of the commuting field is real; the function stops with an error
    if the imaginary parts are larger than rounding noise.
    """),
    code(r'''
    def bar(vector):
        """The Dirac adjoint vector^dagger C."""
        return vector.conj() @ C


    def energy_momentum(phi, dphi, m, lam, a4, a4p, b4, u, z, H):
        """The 64 entries T[nu, mu] = T^nu_mu at one point (real parts)."""
        f = frame_factors(a4, b4, z)
        g_values = eta * f ** 2  # g_mumu
        omega = spin_connection(a4, a4p, b4, u, z, H)
        gup = [gamma[mu] / f[mu] for mu in range(8)]  # gamma^mu
        S = (bar(phi) @ phi).real
        D = [dphi[mu] + omega[mu] @ phi for mu in range(8)]  # D_mu Phi
        Dbar = [bar(dphi[mu]) - bar(phi) @ omega[mu] for mu in range(8)]  # D_mu Phibar
        L0 = 0.5 * sum(bar(phi) @ gup[mu] @ D[mu] - Dbar[mu] @ gup[mu] @ phi
                       for mu in range(8)) - m * S - lam / 2 * S ** 2
        T = np.zeros((8, 8), dtype=complex)
        for nu in range(8):
            for mu in range(8):
                bracket = (bar(phi) @ gup[nu] @ D[mu] - Dbar[mu] @ gup[nu] @ phi
                           + g_values[mu] / g_values[nu]  # gamma_mu D^nu
                           * (bar(phi) @ gup[mu] @ D[nu] - Dbar[nu] @ gup[mu] @ phi))
                T[nu, mu] = (nu == mu) * L0 - bracket / 4
        if np.abs(T.imag).max() > 1e-9 * max(1.0, np.abs(T).max()):
            raise ValueError("the tensor is not real")  # it must be real
        return T.real


    say("bar and energy_momentum are defined.")
    '''),
    md(r"""
    ## 6. The tensor of a generic condensate

    The next cell takes the effective mass $V = 5$ ($m = 5$, $\lambda = 0$), the
    constant $H = 1$, a random column of length 1 (fixed seed), and the point
    $a_4 = 0.5$, $a_4' = 0.25$, $b_4 = e^{2/3}$, $b_4'/b_4 = \frac13$, $z = \pi/4$ of
    the record's history ($a_4 = AHx_4$ and $b_4 = e^{(4/3)AHx_4}$ in the unit
    $b_4(0)$, with $A = 0.25$, at $x_4 = 2$). The condensate's jet at the point is
    $\Phi$ = the column and $\partial_4\Phi = (A - v_g)\Phi$ (any other column with
    the same $S$ belongs to the same condensate at another time). The cell computes
    the 64 entries, checks the record's diagonal ($T^{x_4}{}_{x_4} = -VS$ and the
    other diagonal entries $0$, because $\lambda = 0$ makes $L_0 = 0$ on shell) and
    $T^{x_4}{}_{x_0} = T^{x_0}{}_{x_4} = 0$, counts the nonzero off-diagonal entries
    (36, in the four groups of the record, also at $z = 2.0$ beyond the fold), and
    counts them again at a moment with $4a_4' = b_4'/b_4$ and at a moment with
    $a_4' = b_4' = 0$ (30 each: the six entries between the hidden direction and
    3-space vanish).
    """),
    code(r'''
    V, H = 5.0, 1.0  # effective mass (m = 5, lambda = 0) and the author's constant
    POINT = {"a4": 0.5, "a4p": 0.25, "b4": np.exp(2 / 3), "u": 1 / 3,
             "z": np.pi / 4}  # a point of the deflating history (u = b4'/b4)
    rng = np.random.default_rng(11)  # a fixed seed
    chi = rng.normal(size=16) + 1j * rng.normal(size=16)
    chi /= np.linalg.norm(chi)  # length 1


    def condensate_tensor(column, a4, a4p, b4, u, z, V_value=V, H_value=H):
        """T of the condensate (lambda = 0, m = V_value) whose jet at the point is
        Phi = column, d4 Phi = (A - v_g) column, A = -V gamma^(x4) + c_g g^(x4) g^(x0)."""
        c_g = 1.5 * H_value * np.exp(a4) / np.sqrt(b4)  # (3/2) H e^a4 b4^(-1/2)
        v_g = u - a4p / 2  # b4'/b4 - a4'/2
        A_value = -V_value * g4 + c_g * g4 @ g0
        dphi = np.zeros((8, 16), dtype=complex)
        dphi[4] = A_value @ column - v_g * column  # the only nonzero derivative
        return energy_momentum(column, dphi, V_value, 0.0, a4, a4p, b4, u, z, H_value)


    def off_diagonal_pairs(T):
        """The ordered pairs (nu, mu), nu != mu, whose entry is not zero."""
        tolerance = 1e-10 * max(1.0, np.abs(T).max())
        return [(nu, mu) for nu in range(8) for mu in range(8)
                if nu != mu and abs(T[nu, mu]) > tolerance]


    T_generic = condensate_tensor(chi, **POINT)
    S_chi = (bar(chi) @ chi).real
    expected_diagonal = np.zeros(8)
    expected_diagonal[4] = -V * S_chi
    A4_WL = "Revision/field_equations_a4/reports/wolfram-a4-report.json"
    A4_PY = "Revision/field_equations_a4/reports/python-a4-report.json"
    check(np.abs(np.diag(T_generic) - expected_diagonal).max() < 1e-12
          and abs(T_generic[4, 0]) < 1e-12 and abs(T_generic[0, 4]) < 1e-12
          and recorded(A4_WL, "condensate_kinetic_tensor_diagonal") == "PASS"
          and recorded(A4_PY, "authorT16_condensate_kinetic_diagonal") == "PASS",
          "diagonal (0, 0, 0, 0, -V S, 0, 0, 0) and T^x4_x0 = T^x0_x4 = 0",
          record=f"{A4_WL}, check condensate_kinetic_tensor_diagonal; {A4_PY}, check "
                 "authorT16_condensate_kinetic_diagonal")
    pairs = off_diagonal_pairs(T_generic)
    SPACE, EXTRA = (1, 2, 3), (5, 6, 7)  # x1, x2, x3 and x5, x6, x7
    groups_of_record = ([(0, i) for i in SPACE] + [(i, 4) for i in SPACE]
                        + [(i, t) for i in SPACE for t in EXTRA] + [(4, t) for t in EXTRA])
    expected_pairs = sorted(groups_of_record + [(b, a) for a, b in groups_of_record])
    beyond_fold = off_diagonal_pairs(condensate_tensor(chi, **dict(POINT, z=2.0)))
    check(sorted(pairs) == expected_pairs and sorted(beyond_fold) == expected_pairs,
          "36 nonzero off-diagonal entries: x0-xi, xi-x4, xi-xt, x4-xt (also at z = 2)")
    hidden_space = sorted([(0, i) for i in SPACE] + [(i, 0) for i in SPACE])
    pairs_equal_rates = off_diagonal_pairs(condensate_tensor(
        chi, POINT["a4"], POINT["u"] / 4, POINT["b4"], POINT["u"], POINT["z"]))
    pairs_still = off_diagonal_pairs(condensate_tensor(
        chi, POINT["a4"], 0.0, POINT["b4"], 0.0, POINT["z"]))
    check(sorted(set(pairs) - set(pairs_equal_rates)) == hidden_space
          and sorted(pairs_still) == sorted(pairs_equal_rates)
          and len(pairs_equal_rates) == 30,
          "with 4 a4' = b4'/b4, or with a4' = b4' = 0, the six x0-xi entries vanish")
    report("S of the random column", f"{S_chi:.6f}")
    report("T^x4_x4 = -V S", f"{T_generic[4, 4]:.6f}")
    report("largest off-diagonal entry in size", f"{np.abs(T_generic).max():.6f}")
    '''),
    md(r"""
    The next cell draws the 64 entries of this generic condensate as a heat map.
    """),
    code(r'''
    def heat_map(ax, T, title, largest):
        """Draw T as coloured squares with the value printed in each."""
        picture = ax.imshow(T, cmap="RdBu_r", vmin=-largest, vmax=largest)
        for nu in range(8):
            for mu in range(8):
                text = f"{T[nu, mu]:.2f}"
                if text == "-0.00":  # a tiny negative number: print it as 0.00
                    text = "0.00"
                # white digits on dark squares, black digits on light ones
                colour = "white" if abs(T[nu, mu]) > 0.6 * largest else "black"
                ax.text(mu, nu, text, ha="center", va="center", fontsize=6,
                        color=colour)
        ticks = [f"${n[0]}_{n[1]}$" for n in NAMES]
        ax.set_xticks(range(8), ticks)
        ax.set_yticks(range(8), ticks)
        ax.set_xlabel("lower index $\\mu$ (column)")
        ax.set_ylabel("upper index $\\nu$ (row)")
        ax.set_title(title)
        ax.grid(False)
        return picture


    SCALE = 2.0  # the colour scale runs from -2 to 2 in both heat maps of this notebook
    fig, ax = plt.subplots(figsize=(6.6, 5.6))
    picture = heat_map(ax, T_generic, "Generic condensate: $T^\\nu{}_\\mu$", SCALE)
    fig.colorbar(picture, ax=ax, label="value (energy per unit volume)", extend="both")
    save_figure(fig, "generic_condensate",
                "Heat map of the 64 entries $T^\\nu{}_\\mu$ (row $\\nu$, column $\\mu$, "
                "both running over $x_0, \\dots, x_7$) of a generic exact condensate of "
                "dirac16complex00 with effective mass $V = 5$, $\\lambda = 0$, $H = 1$, "
                "a random unit column, at the point $a_4 = 0.5$, $a_4' = 0.25$, "
                "$b_4 = e^{2/3}$, $b_4'/b_4 = 1/3$, $z = \\pi/4$ of the history in the "
                "corrected metric; colour scale from $-2$ to $2$ (entries beyond it "
                "are shown in the darkest colour and printed), in units of energy per "
                "unit volume. The diagonal holds only $-VS$ at $x_4$; 36 off-diagonal "
                "squares are nonzero, in the rows and columns pairing 3-space with "
                "$x_0$, with $x_4$ and with the extra times, and $x_4$ with the extra "
                "times. The squares $(x_4, x_0)$ and $(x_0, x_4)$ and those inside "
                "3-space and inside the extra times are zero.")
    '''),
    md(r"""
    ## 7. How the off-diagonal entries depend on the rate $a_4'$

    The next cell computes four off-diagonal entries of the same condensate at the
    same point for 41 values of $a_4'$ from $-1$ to $1$, with $b_4'/b_4 = \frac13$
    kept fixed: the momentum flows $T^{x_4}{}_{x_1}$ and $T^{x_4}{}_{x_7}$, the
    hidden/3-space stress $T^{x_1}{}_{x_0}$ and the 3-space/extra-time stress
    $T^{x_1}{}_{x_7}$ (the extra time $x_7$ is taken because its bilinears are
    larger for this random column; $x_5$ and $x_6$ behave in the same way). The
    two flows do not depend on $a_4'$ (they come from $H$:
    from $c_g$ and from the part $H\gamma^{(0)}\gamma^{(t)}$ of $\Omega_{x_t}$); the
    hidden/3-space entry is proportional to $4a_4' - b_4'/b_4$ (the record's
    coefficient), so it vanishes at $a_4' = \frac14 b_4'/b_4 = \frac{1}{12}$; and
    $T^{x_1}{}_{x_7}$ is the sum of a part from $H$ and a part proportional to
    $4a_4' - b_4'/b_4$, so it is a straight line in $a_4'$ that does not pass
    through zero at $a_4' = \frac{1}{12}$. The cell checks the three statements.
    """),
    code(r'''
    rates = np.linspace(-1.0, 1.0, 41)  # values of a4p
    zero_rate = POINT["u"] / 4  # 4 a4p - u vanishes here: 1/12
    entries = np.array([[T[4, 1], T[4, 7], T[1, 0], T[1, 7]] for T in (
        condensate_tensor(chi, POINT["a4"], rate, POINT["b4"], POINT["u"], POINT["z"])
        for rate in rates)])
    middle = 20  # rates[20] = 0
    check(np.abs(entries[:, :2] - entries[middle, :2]).max() < 1e-12
          and np.abs(entries[middle, :2]).min() > 0.01,
          "T^x4_x1 and T^x4_x7 do not depend on a4p and are not zero")
    slope_hidden = entries[-1, 2] / (rates[-1] - zero_rate)
    slope_extra = (entries[-1, 3] - entries[0, 3]) / (rates[-1] - rates[0])
    at_zero_rate = entries[0, 3] + slope_extra * (zero_rate - rates[0])  # the H part
    check(np.abs(entries[:, 2] - slope_hidden * (rates - zero_rate)).max() < 1e-12
          and np.abs(entries[:, 3] - at_zero_rate
                     - slope_extra * (rates - zero_rate)).max() < 1e-12
          and min(abs(slope_hidden), abs(slope_extra), abs(at_zero_rate)) > 1e-3,
          "T^x1_x0 is proportional to 4 a4p - b4'/b4, T^x1_x7 is linear in a4p")
    report("T^x4_x1 and T^x4_x7", f"{entries[middle, 0]:.6f} and {entries[middle, 1]:.6f}")
    report("slope of T^x1_x0, slope of T^x1_x7, T^x1_x7 at a4p = 1/12",
           f"{slope_hidden:.6f}, {slope_extra:.6f}, {at_zero_rate:.6f}")
    fig, (left, right) = plt.subplots(1, 2, figsize=(9.6, 3.9))
    fig.subplots_adjust(wspace=0.35)
    left.plot(rates, entries[:, 0], label="$T^{x_4}{}_{x_1}$ (momentum flow)")
    left.plot(rates, entries[:, 1], "--", label="$T^{x_4}{}_{x_7}$ (momentum flow)")
    left.axhline(0.0, color="black", linewidth=0.8)
    left.set_xlabel("rate $a_4'$ (with $b_4'/b_4 = 1/3$)")
    left.set_ylabel("entry (energy per unit volume)")
    left.set_title("Come from $H$: independent of $a_4'$")
    left.legend(fontsize=8)
    right.plot(rates, entries[:, 2], label="$T^{x_1}{}_{x_0}$")
    right.plot(rates, entries[:, 3], "--", label="$T^{x_1}{}_{x_7}$")
    right.axhline(0.0, color="black", linewidth=0.8)
    right.axvline(zero_rate, color="gray", linestyle=":", linewidth=0.9)
    right.set_xlabel("rate $a_4'$ (with $b_4'/b_4 = 1/3$)")
    right.set_title("Contain $4a_4' - b_4'/b_4$")
    right.legend(fontsize=8)
    save_figure(fig, "offdiagonal_entries",
                "Four off-diagonal entries of the generic condensate of the previous "
                "figure ($V = 5$, $H = 1$, $a_4 = 0.5$, $b_4 = e^{2/3}$, "
                "$b_4'/b_4 = 1/3$, $z = \\pi/4$) against the rate $a_4'$ from $-1$ to "
                "$1$, in units of energy per unit volume. Left: the momentum flows "
                "$T^{x_4}{}_{x_1}$ and $T^{x_4}{}_{x_7}$ come from $H$ and do not depend "
                "on $a_4'$. Right: $T^{x_1}{}_{x_0}$ (solid) is proportional to "
                "$4a_4' - b_4'/b_4$ and vanishes at $a_4' = 1/12$ (dotted line), where "
                "3-space and the block change at the same rate; $T^{x_1}{}_{x_7}$ "
                "(dashed) is a part from $H$ plus a part proportional to "
                "$4a_4' - b_4'/b_4$, a straight line that keeps its $H$ part at "
                "$a_4' = 1/12$.")
    '''),
    md(r"""
    ## 8. The 24 three-gamma bilinears and the condensates with a diagonal tensor

    **Each entry is a combination of bilinears.** The record says that each of the
    36 nonzero off-diagonal entries is a fixed combination of one or two bilinears
    $B(a\,b\,c) = \bar\Phi\gamma^{(a)}\gamma^{(b)}\gamma^{(c)}\Phi$: for the pairs
    $x_0$-$x_i$ and $x_i$-$x_4$ the one bilinear $B(x_0\,x_i\,x_4)$, for the pairs
    $x_4$-$x_t$ the one bilinear $B(x_0\,x_4\,x_t)$, and for the pairs $x_i$-$x_t$
    the two bilinears $B(x_0\,x_i\,x_t)$ and $B(x_i\,x_4\,x_t)$. The next cell checks
    this with four random columns: for each entry it finds by least squares the
    numbers that multiply its bilinears, and the residual must be zero (the numbers
    depend on the point and on $V$ and $H$, not on the column). It also checks that
    exactly 24 bilinears occur, and prints them.

    **The witnesses.** The record builds condensates for which all 24 bilinears
    vanish. The three matrices $P_1 = \gamma^{(1)}\gamma^{(5)}$,
    $P_2 = \gamma^{(2)}\gamma^{(6)}$, $P_3 = \gamma^{(3)}\gamma^{(7)}$ square to 1 and
    commute with each other and with $A$. On a history along which
    $k = e^{2a_4}/b_4$ keeps a constant value $k_0$ (that is $b_4 = e^{2a_4}/k_0$, with
    any function $a_4$), $c_g = \frac32H\sqrt{k_0}$ is a constant, and for a constant
    effective mass $V$ (here $\lambda = 0$) so is $A$. Let
    $\omega = \sqrt{V^2 - c_g^2}$ (a real number when $V^2 > c_g^2$); then
    $A^2 = (c_g^2 - V^2) \cdot 1 = -\omega^2 \cdot 1$, and $A$ has the eigenvalue
    $-i\omega$ on an 8-dimensional space: every column $u$ is the sum of
    $\frac12(u + \frac{i}{\omega}Au)$, with eigenvalue $-i\omega$, and
    $\frac12(u - \frac{i}{\omega}Au)$, with eigenvalue $+i\omega$, and because $A$ is
    real, complex conjugation carries the one space onto the other, so both have
    dimension $16/2 = 8$. The three $P_k$ split that space into eight sectors (one
    for each choice of the signs of $P_1$, $P_2$, $P_3$). The matrix that keeps one
    sector, $\frac12(1 + \frac{i}{\omega}A) \cdot \frac12(1 \pm P_1) \cdot
    \frac12(1 \pm P_2) \cdot \frac12(1 \pm P_3)$, has trace 1, because every product
    of different gammas has trace 0; so every sector has dimension 1. In the sector
    $P_1 = P_2 = P_3 = -1$ take a unit vector $v_1$ and in the sector
    $P_1 = P_2 = P_3 = +1$ a unit vector $v_2$ (each unique up to a factor of size 1,
    which does not change the bilinears), put $c = \overline{v_1^\dagger Cv_2}$ (the
    bar means the complex conjugate number) and $\Phi_0 = v_1 + cv_2$. The
    condensate is $\Phi = e^{a_4/2}b_4^{-1}e^{-i\omega x_4}\Phi_0$: it oscillates with
    the frequency $\omega$ and is diluted by the 7-volume. The record gives three such
    witnesses, $(V, H, k_0) = (5, 1, 4)$, $(5, 4/3, 4)$, $(-5, 1, 4)$, with
    $c_g = 3, 4, 3$ and $\omega = 4$, $3$, $4$ (the record writes the effective mass
    $V$ as $M$ and the frequency $\omega$ as w).
    """),
    code(r'''
    def bilinear_sets(nu, mu):
        """The direction triples (a, b, c) of the bilinears that carry T^nu_mu."""
        low, high = sorted((nu, mu))
        if low == 0:  # x0-xi
            return [(0, high, 4)]
        if high == 4:  # xi-x4
            return [(0, low, 4)]
        if low == 4:  # x4-xt
            return [(0, 4, high)]
        return [(0, low, high), (low, 4, high)]  # xi-xt: two bilinears


    def bilinear(column, directions):
        """B(a b c) = Phibar gamma^(a) gamma^(b) gamma^(c) Phi."""
        a, b, c = directions
        return bar(column) @ gamma[a] @ gamma[b] @ gamma[c] @ column


    columns = [rng.normal(size=16) + 1j * rng.normal(size=16) for _ in range(4)]
    tensors = [condensate_tensor(column, **POINT) for column in columns]
    worst_residual, used = 0.0, set()
    for nu, mu in pairs:
        sets = bilinear_sets(nu, mu)
        used.update(sets)
        # one row per column: the bilinears of the entry, and the entry itself
        matrix = np.array([[bilinear(column, d) for d in sets] for column in columns])
        values = np.array([T[nu, mu] for T in tensors])
        numbers = np.linalg.lstsq(matrix, values, rcond=None)[0]  # least squares
        residual = np.abs(matrix @ numbers - values).max() / np.abs(values).max()
        worst_residual = max(worst_residual, residual)
    check(worst_residual < 1e-9 and len(used) == 24
          and recorded(A4_WL, "condensate_offdiagonal_are_three_gamma_bilinears") == "PASS"
          and recorded(A4_PY, "authorT16_condensate_offdiagonal_three_gamma") == "PASS",
          "each of the 36 entries is a fixed combination of its bilinears (24 in all)",
          record=f"{A4_WL}, check condensate_offdiagonal_are_three_gamma_bilinears; "
                 f"{A4_PY}, check authorT16_condensate_offdiagonal_three_gamma")
    for directions in sorted(used):
        say("bilinear B(" + " ".join(NAMES[d] for d in directions) + ")")
    '''),
    md(r"""
    **The coefficients of the record.** The record
    `Revision/field_equations_a4/a4-equations.json` lists, for each of the 36
    entries, its bilinears and their coefficients as formulas in the Wolfram
    Language, in the names `a4v` $= a_4$, `ad1` $= a_4'$, `bb` $= b_4$,
    `uu` $= b_4'/b_4$, `H`, `sv` $= \sin z$, `cv` $= \cos z$ and
    `ww` $= (\sin^2 z)^{1/12}$, for the symmetrised kinetic tensor
    $K^{(\nu}{}_{\mu)}$, the average of
    $K^\nu{}_\mu = \frac12(\bar\Phi\gamma^\nu D_\mu\Phi - D_\mu\bar\Phi\gamma^\nu\Phi)$
    and of $g^{\nu\nu}g_{\mu\mu}K^\mu{}_\nu$ (the same with the two indices
    exchanged, then moved back to their places with the metric). Off the diagonal the
    tensor is $T^\nu{}_\mu = -K^{(\nu}{}_{\mu)}$, so every entry must equal minus the
    sum of its coefficients times its bilinears. The next cell translates each formula
    into sympy (`E^x` becomes `E**x`, `^` becomes `**`, `Sqrt[bb]` becomes
    `sqrt(bb)`), evaluates it at the point $a_4 = 0.5$, $a_4' = 0.25$,
    $b_4 = e^{2/3}$, $b_4'/b_4 = \frac13$, $z = \pi/4$, $H = 1$, and compares, for the
    generic condensate and for the four random columns, all 36 entries. The
    coefficients contain $V$ nowhere: they are the same for every effective mass.
    The cell prints one term of each of the ten groups of equal coefficients.
    """),
    code(r'''
    import re  # regular expressions: patterns that find pieces of a text

    import sympy as sp  # exact algebra with symbols

    A4_RECORD = "Revision/field_equations_a4/a4-equations.json"
    record_entries = json.loads(repository_file(A4_RECORD).read_text(encoding="utf-8"))[
        "fields"]["dirac16complex00"]["offDiagonalKinetic"]
    a4v, ad1, uu, H_symbol, sv, cv, ww = sp.symbols("a4v ad1 uu H sv cv ww", real=True)
    bb = sp.Symbol("bb", positive=True)  # b4
    AT_POINT = {a4v: POINT["a4"], ad1: POINT["a4p"], bb: POINT["b4"], uu: POINT["u"],
                H_symbol: H, sv: np.sin(POINT["z"]), cv: np.cos(POINT["z"]),
                ww: np.abs(np.sin(POINT["z"])) ** (1 / 6)}
    NAMES_RECORD = {"E": sp.E, "a4v": a4v, "ad1": ad1, "bb": bb, "uu": uu, "H": H_symbol,
                    "sv": sv, "cv": cv, "ww": ww, "sqrt": sp.sqrt}
    worst_coefficient, groups, record_pairs = 0.0, {}, []
    for item in record_entries:
        # "K^x1_x4 (symmetrised)": upper index x1 (row nu), lower index x4 (column mu)
        nu, mu = [int(digit) for digit in re.findall(r"x(\d)", item["component"])]
        record_pairs.append((nu, mu))
        predicted = np.zeros(5, dtype=complex)  # for the generic and the four columns
        for term in item["terms"]:  # one or two terms
            directions = tuple(int(d) for d in re.findall(r"x(\d)", term["bilinear"]))
            formula = term["coefficient"]["input"]  # the Wolfram Language text
            text = formula.replace("E^", "E**").replace("^", "**")
            text = text.replace("Sqrt[", "sqrt(").replace("]", ")")  # Sqrt[bb] -> sqrt(bb)
            coefficient = float(sp.sympify(text, locals=NAMES_RECORD).subs(AT_POINT))
            predicted -= coefficient * np.array([bilinear(column, directions)
                                                 for column in [chi] + columns])
            groups.setdefault(formula, (nu, mu, directions, coefficient))
        for n, T in enumerate([T_generic] + tensors):
            worst_coefficient = max(worst_coefficient, abs(T[nu, mu] - predicted[n]))
    check(len(record_entries) == 36 and sorted(record_pairs) == sorted(pairs)
          and len(groups) == 10 and worst_coefficient < 1e-12
          and recorded(A4_PY, "json_offdiagonal_coefficients") == "PASS"
          and recorded(A4_PY, "offdiagonal_coefficients_representation_independent")
          == "PASS",
          "all 36 entries are -(record coefficients) x bilinears, for 5 columns",
          record=f"{A4_RECORD}, offDiagonalKinetic; {A4_PY}, checks "
                 "json_offdiagonal_coefficients and "
                 "offdiagonal_coefficients_representation_independent")
    for nu, mu, directions, coefficient in groups.values():
        say(f"K^{NAMES[nu]}_{NAMES[mu]}: coefficient {coefficient:+.6f} of B("
            + " ".join(NAMES[d] for d in directions) + ")")
    '''),
    md(r"""
    The next cell defines the function `witness(V_w, H_w, k0)`. It computes
    $c_g = \frac32H_w\sqrt{k_0}$, $A = -V_w\gamma^{(4)} + c_g\gamma^{(4)}\gamma^{(0)}$
    and $\omega = \sqrt{V_w^2 - c_g^2}$, finds the 8-dimensional space of $A$ for the
    eigenvalue $-i\omega$ (as the null space of $A + i\omega$, from a singular value
    decomposition), then inside it the joint eigenvectors $v_1$, $v_2$ (with the
    projector $\frac18(1 \pm P_1)(1 \pm P_2)(1 \pm P_3)$, which keeps exactly the
    vectors with $P_1 = P_2 = P_3 = \pm1$), each of length 1, and returns $\omega$,
    $A$, $v_1$, $v_2$ and $\Phi_0 = v_1 + cv_2$ (in the code the frequency $\omega$ is
    called `freq`). The cell builds the three witnesses and prints their frequencies.
    It then checks the two dimensions of the construction with numbers: each of the
    $2^8 - 1 = 255$ products of 1 to 8 different gammas has trace 0; for each witness
    the space of $A$ for $-i\omega$ has dimension 8 (the rank of $A + i\omega$ is
    $16 - 8$); and the matrix that keeps one sector has trace 1 for all eight choices
    of the three signs.
    """),
    code(r'''
    import itertools  # all combinations and all sign choices of a list

    P = [gamma[i] @ gamma[i + 4] for i in range(1, 4)]  # gamma^(x1) gamma^(x5), ...


    def witness(V_w, H_w, k0):
        """The frequency omega (here freq), A, the unit vectors v1, v2 and the column
        Phi0 of the record's diagonal witness for (V_w, H_w) on a history with k = k0."""
        c_w = 1.5 * H_w * np.sqrt(k0)  # c_g = (3/2) H sqrt(k0), a constant
        A_w = -V_w * g4 + c_w * g4 @ g0  # d4 chi = A chi
        freq = np.sqrt(V_w ** 2 - c_w ** 2)  # the frequency omega
        # The null space of A + i omega: the rows of the third SVD factor whose
        # singular value is zero, complex conjugated and written as columns.
        _, singular, rows = np.linalg.svd(A_w + 1j * freq * I16)
        space = rows[singular < 1e-9].conj().T  # 16 x 8: the eigenspace for -i omega
        found = []
        for sign in (-1, 1):
            projector = (I16 + sign * P[0]) @ (I16 + sign * P[1]) @ (I16 + sign * P[2]) / 8
            left_vectors, values, _ = np.linalg.svd(projector @ space)
            if np.sum(values > 1e-9) != 1:
                raise ValueError("the joint eigenvector is not unique")
            found.append(left_vectors[:, 0])  # a unit vector
        v1, v2 = found
        c = np.conj(bar(v1) @ v2)  # c = conj(v1^dagger C v2)
        return freq, A_w, v1, v2, v1 + c * v2


    WITNESSES = [(5.0, 1.0, 4.0), (5.0, 4 / 3, 4.0), (-5.0, 1.0, 4.0)]  # (V, H, k0)
    witnesses = {triple: witness(*triple) for triple in WITNESSES}  # (V, H, k0) -> five
    for (V_w, H_w, k0), found in witnesses.items():
        say(f"witness (V, H, k0) = ({V_w:g}, {H_w:.4g}, {k0:g}): frequency omega = "
            f"{found[0]:.6f}")


    def product_of(indices):
        """The product gamma^(a) gamma^(b) ... of the frame gammas with these indices."""
        result = I16
        for index in indices:
            result = result @ gamma[index]
        return result


    subsets = [chosen for size in range(1, 9)
               for chosen in itertools.combinations(range(8), size)]  # 255 index sets
    traceless = all(abs(np.trace(product_of(chosen))) < 1e-12 for chosen in subsets)
    dimensions_hold = True
    for (V_w, H_w, k0), (freq, A_w, v1, v2, phi0) in witnesses.items():
        # the dimension of the space of -i omega: 16 minus the rank of A + i omega
        dimension = 16 - np.linalg.matrix_rank(A_w + 1j * freq * I16, tol=1e-9)
        for signs in itertools.product((-1, 1), repeat=3):  # the eight sectors
            keeper = (I16 + 1j / freq * A_w) / 2  # keeps the space of -i omega
            for sign, P_k in zip(signs, P):
                keeper = keeper @ (I16 + sign * P_k) / 2  # keeps P_k = sign
            dimensions_hold = dimensions_hold and abs(np.trace(keeper) - 1) < 1e-12
        dimensions_hold = dimensions_hold and dimension == 8
    check(len(subsets) == 255 and traceless and dimensions_hold,
          "255 gamma products have trace 0; space of -i omega: dim 8; each sector: dim 1")
    '''),
    md(r"""
    The next cell checks each witness: that $A\Phi_0 = -i\omega\Phi_0$ (so
    $\Phi = e^{a_4/2}b_4^{-1}e^{-i\omega x_4}\Phi_0$ is an exact condensate on every
    history with $e^{2a_4}/b_4 = k_0$), that all 24 bilinears vanish, that $S \neq 0$,
    and that the tensor is diagonal at 36 points of such histories: every combination
    of $a_4 \in \{-1, 0, 0.5\}$ (with $b_4 = e^{2a_4}/k_0$), of
    $a_4' \in \{-0.5, 0, 0.25, 1\}$ (with $b_4'/b_4 = 2a_4'$, so that $k$ stays
    constant), and of $z \in \{0.3, 1.3, 2.4\}$ (the last beyond the fold). At each
    point the jet is the column $\Phi_0$ and $\partial_4\Phi = (-i\omega - v_g)\Phi_0$.
    It prints $S$ of $\Phi_0$ for each witness (with $v_1$ and $v_2$ of length 1).
    """),
    code(r'''
    grid = [(a4, a4p, z) for a4 in (-1.0, 0.0, 0.5) for a4p in (-0.5, 0.0, 0.25, 1.0)
            for z in (0.3, 1.3, 2.4)]  # 3 x 4 x 3 = 36 points
    witness_columns = {}  # (V, H, k0) -> Phi0
    unit_S = {}  # (V, H, k0) -> S of Phi0 built from v1 and v2 of length 1
    for (V_w, H_w, k0), (freq, A_w, v1, v2, phi0) in witnesses.items():
        S_w = (bar(phi0) @ phi0).real
        largest_bilinear = max(abs(bilinear(phi0, d)) for d in used)
        worst_off = 0.0  # the largest off-diagonal entry at the 36 points
        for a4, a4p, z in grid:  # b4 = e^(2 a4)/k0 and b4'/b4 = 2 a4': k stays k0
            T = condensate_tensor(phi0, a4, a4p, np.exp(2 * a4) / k0, 2 * a4p, z,
                                  V_w, H_w)
            worst_off = max(worst_off, np.abs(T - np.diag(np.diag(T))).max())
        check(np.abs(A_w @ phi0 + 1j * freq * phi0).max() < 1e-12
              and largest_bilinear < 1e-12 and abs(S_w) > 0.1 and worst_off < 1e-12,
              f"witness ({V_w:g}, {H_w:.4g}, {k0:g}): omega = {freq:g}, the 24 "
              "bilinears vanish, S != 0, T diagonal at 36 points")
        witness_columns[(V_w, H_w, k0)] = phi0
        unit_S[(V_w, H_w, k0)] = S_w
        report(f"witness ({V_w:g}, {H_w:.4g}, {k0:g}): omega, and S for unit v1, v2",
               f"{freq:g} and {S_w:.6f}")
    '''),
    md(r"""
    **Why $S$ of a witness is never negative.** $C$ anticommutes with each $P_k$ (it
    contains $\gamma^{(x_k)}$ but not $\gamma^{(x_{k+4})}$), and each $P_k$ is real
    and symmetric, so $P_k^\dagger = P_k$. Take $P_1v_1 = -v_1$. Then, line by line:
    $v_1^\dagger Cv_1 = -v_1^\dagger CP_1v_1$ (replace $v_1$ by $-P_1v_1$)
    $= v_1^\dagger P_1Cv_1$ ($CP_1 = -P_1C$) $= (P_1v_1)^\dagger Cv_1$
    ($P_1^\dagger = P_1$) $= -v_1^\dagger Cv_1$ ($P_1v_1 = -v_1$). A number equal to
    minus itself is zero: $v_1^\dagger Cv_1 = 0$, and in the same way
    $v_2^\dagger Cv_2 = 0$. Write $s = v_1^\dagger Cv_2$; then
    $v_2^\dagger Cv_1 = \bar s$ ($C$ is real and symmetric) and $c = \bar s$, so
    $S = \Phi_0^\dagger C\Phi_0 = v_1^\dagger Cv_1 + c\,s + \bar c\,\bar s
    + |c|^2 v_2^\dagger Cv_2 = 0 + |s|^2 + |s|^2 + 0 = 2|s|^2 \geq 0$. The next cell
    checks each step numerically for the three witnesses. It also checks an
    observation (COMPUTED for these three witnesses, not proved here): with $v_1$,
    $v_2$ of length 1, $|s| = |\omega/V|$, so $S = 2\omega^2/V^2$; this gives
    $2 \cdot 16/25 = 1.28$ and $2 \cdot 9/25 = 0.72$.
    """),
    code(r'''
    anticommute = all(np.abs(C @ P_k + P_k @ C).max() < 1e-12 for P_k in P)
    symmetric = all(np.array_equal(P_k, P_k.T) for P_k in P)  # real: P^dagger = P^T
    steps_hold, observation = True, True
    for (V_w, H_w, k0), (freq, A_w, v1, v2, phi0) in witnesses.items():
        s = bar(v1) @ v2  # s = v1^dagger C v2
        S_unit = unit_S[(V_w, H_w, k0)]  # S of Phi0 with unit v1, v2 (previous cell)
        steps_hold = (steps_hold and abs(bar(v1) @ v1) < 1e-12
                      and abs(bar(v2) @ v2) < 1e-12
                      and abs(S_unit - 2 * abs(s) ** 2) < 1e-12)
        observation = observation and abs(S_unit - 2 * freq ** 2 / V_w ** 2) < 1e-12
    check(anticommute and symmetric and steps_hold,
          "C P_k = -P_k C, P_k symmetric, v^dagger C v = 0, so S = 2 |v1^dagger C v2|^2")
    check(observation,
          "observed: S = 2 omega^2 / V^2 for the three witnesses (unit v1, v2)")
    '''),
    md(r"""
    **The numbers of the record.** The Wolfram report of the record lists, in the
    detail text of its check `condensate_witness_constant_k_exact`, the frequencies
    $\omega$ (written w there) and the values of $e^{-a_4}b_4^2S$ of the three
    witnesses, that is of $S$ of their columns $\Phi_0$. The record's verifier builds
    the witnesses with exact columns $v_1$, $v_2$ that are not of length 1; since
    $S = 2|v_1^\dagger Cv_2|^2$ grows with the lengths of $v_1$ and $v_2$, its values
    cannot equal ours, while $\omega = \sqrt{V^2 - \frac94H^2k_0}$ must agree exactly.
    The next cell reads the numbers out of the detail text (with a regular
    expression, a pattern that finds text), prints them, checks $\omega$, and divides
    each $S$ of the record by our $S$: the three quotients must be one and the same
    number, so that the record's three values are reproduced up to one common factor,
    which the cell prints. That factor is the product of the squared lengths of the
    record's columns, a choice of its verifier, not a physical number.
    """),
    code(r'''
    detail = record_entry(A4_WL, "condensate_witness_constant_k_exact")["detail"]
    # the frequencies, which the record writes "w = sqrt(M^2 - (9/4) H^2 k0) = {4, 3, 4}"
    freq_text = re.search(r"k0\) = \{([^}]*)\}", detail).group(1)  # "4, 3, 4"
    S_text = re.search(r"S = \{([^}]*)\}", detail).group(1)  # the three S values
    record_freq = np.array([float(value) for value in freq_text.split(",")])
    record_S = np.array([float(value) for value in S_text.split(",")])
    our_freq = np.array([witnesses[triple][0] for triple in WITNESSES])
    our_S = np.array([unit_S[triple] for triple in WITNESSES])
    check(np.abs(our_freq - record_freq).max() < 1e-12
          and recorded(A4_WL, "condensate_witness_constant_k_exact") == "PASS"
          and recorded(A4_PY, "authorT16_condensate_witness") == "PASS",
          f"omega = {freq_text} for the three witnesses, as in the record",
          record=f"{A4_WL}, check condensate_witness_constant_k_exact; {A4_PY}, check "
                 "authorT16_condensate_witness")
    quotients = record_S / our_S  # S of the record divided by S of unit v1, v2
    check(np.abs(quotients / quotients[0] - 1).max() < 1e-9 and np.all(record_S > 0),
          f"S = {S_text} of the record are one common multiple of ours",
          record=f"{A4_WL}, check condensate_witness_constant_k_exact")
    report("S of the record divided by S of unit v1, v2 (all three)",
           f"{quotients[0]:.1f}")
    '''),
    md(r"""
    The next cell draws the tensor of the witness $(V, H, k_0) = (5, 1, 4)$ with the
    same colour scale as the generic condensate, at a point of a history with
    $k = 4$: $a_4 = 0.5$, $a_4' = 0.25$, $b_4 = e^{2a_4}/4 = e/4$,
    $b_4'/b_4 = 2a_4' = 0.5$, $z = \pi/4$. Only one square is coloured. (The value of
    $S$, and hence of $-VS$, depends on the lengths of $v_1$ and $v_2$; here both have
    length 1, and the jet at the point is $\Phi_0$, so $S = 1.28$ and $-VS = -6.4$.)
    """),
    code(r'''
    WITNESS_POINT = {"a4": 0.5, "a4p": 0.25, "b4": np.exp(1.0) / 4, "u": 0.5,
                     "z": np.pi / 4}  # a point of a history with k = e^(2 a4)/b4 = 4
    T_witness = condensate_tensor(witness_columns[(5.0, 1.0, 4.0)], **WITNESS_POINT)
    fig, ax = plt.subplots(figsize=(6.6, 5.6))
    picture = heat_map(ax, T_witness, "Witness condensate: $T^\\nu{}_\\mu$", SCALE)
    fig.colorbar(picture, ax=ax, label="value (energy per unit volume)", extend="both")
    save_figure(fig, "witness_condensate",
                "Heat map of the 64 entries $T^\\nu{}_\\mu$ of the exact witness "
                "condensate $\\Phi = e^{a_4/2}b_4^{-1}e^{-4ix_4}\\Phi_0$ of the Revision "
                "record with $V = 5$, $H = 1$, $\\lambda = 0$, on a history with "
                "$k = e^{2a_4}/b_4 = 4$, at the point $a_4 = 0.5$, $a_4' = 0.25$, "
                "$b_4 = e/4$, $b_4'/b_4 = 0.5$, $z = \\pi/4$ (jet $\\Phi_0$), with the "
                "same colour scale as the generic condensate, in units of energy per "
                "unit volume. All 24 three-gamma bilinears of $\\Phi_0$ vanish, so every "
                "off-diagonal entry is zero (by the record, at every point of every "
                "history with constant $k$): this condensate is a perfect fluid at rest, "
                "with $T^{x_4}{}_{x_4} = -VS$ and zero pressure.")
    check(len(off_diagonal_pairs(T_witness)) == 0 and abs(T_witness[4, 4]) > 0.1,
          "the drawn witness tensor is diagonal with T^x4_x4 = -V S != 0")
    '''),
    md(r"""
    ## 9. Conservation of the full tensor, tested with finite differences

    The full tensor of a condensate, off-diagonal entries included, must satisfy
    $\nabla_\mu T^\mu{}_\nu = 0$. Because the condensate solves the field equation on
    every history, the test uses a non-linear one, $a_4 = 0.3x_4 + 0.05x_4^2$
    ($a_4' = 0.3 + 0.1x_4$) and $b_4 = e^{0.4x_4 - 0.02x_4^2}$
    ($b_4'/b_4 = 0.4 - 0.04x_4$), with $m = 1$, $\lambda = 0.5$, $H = 0.25$. The
    tensor depends on $x_4$ (through $\Phi$, $a_4$, $a_4'$, $b_4$ and $b_4'/b_4$) and
    on $x_0$ (through $z$); the derivatives $\partial_4 T$ and $\partial_0 T$ are
    taken by central finite differences with step $h$.

    The next cell computes the 21 Christoffel symbols of the metric with sympy
    (the formula $\Gamma^\lambda{}_{\mu\nu} = \frac{1}{2g_{\lambda\lambda}}
    (\partial_\mu g_{\lambda\nu} + \partial_\nu g_{\lambda\mu}
    - \partial_\lambda g_{\mu\nu})$ of a diagonal metric, with the functions $a_4$
    and $b_4$), for $\sin z > 0$, where $(\sin^2 z)^{1/6} = \sin^{1/3}z$ (the test
    points lie at $0 < z < \pi$, on both sides of the fold $z = \pi/2$), puts the
    history into them and turns each into a fast numpy function of $(x_4, x_0, H)$
    with `sp.lambdify`.
    """),
    code(r'''
    x = sp.symbols("x0:8", real=True)  # sympy was imported in section 8
    Hs = sp.symbols("H", positive=True)
    a4_function = sp.Function("a4")(x[4])
    b4_function = sp.Function("b4", positive=True)(x[4])
    zs = 6 * Hs * x[0]
    block = sp.exp(-2 * a4_function) * b4_function  # e^(-2 a4) b4
    g = sp.diag(*([block * sp.cot(zs) ** 2] + [sp.exp(2 * a4_function)] * 3 + [-1]
                  + [-block * sp.sin(zs) ** sp.Rational(1, 3)] * 3))  # sin z > 0
    history = {  # a4(x4) and b4(x4) of the test
        a4_function: sp.Rational(3, 10) * x[4] + sp.Rational(1, 20) * x[4] ** 2,
        b4_function: sp.exp(sp.Rational(2, 5) * x[4] - sp.Rational(1, 50) * x[4] ** 2)}
    christoffel = {}  # (l, i, j) with i <= j -> a numpy function of (x4, x0, H)
    for l in range(8):
        for i in range(8):
            for j in range(i, 8):
                value = sp.simplify((sp.diff(g[l, j], x[i]) + sp.diff(g[l, i], x[j])
                                     - sp.diff(g[i, j], x[l])) / (2 * g[l, l]))
                if value != 0:  # put the history in, then make a numpy function
                    christoffel[(l, i, j)] = sp.lambdify(
                        (x[4], x[0], Hs), value.subs(history).doit(), "numpy")
    check(len(christoffel) == 21, "21 nonzero Christoffel symbols (i <= j)")
    '''),
    md(r"""
    The next cell builds the two condensates of the test and the divergence. With
    $\lambda \neq 0$ and a changing $a_4$ and $b_4$ the effective mass
    $V(x_4) = m + \lambda S_0e^{a_4}b_4^{-2}$ and the coefficient
    $c_g(x_4) = \frac32He^{a_4}b_4^{-1/2}$ change in time, and the condensate has no
    closed form. So the notebook fixes the column $\chi$ at the time of each test
    point (a random unit column, with $S_0 = \chi^\dagger C\chi$) and computes it at
    the neighbouring times $x_4 \pm h$ by RK4 with 50 steps (`flow`); the error of
    RK4 over the distance $h$ is of the order $h^5/50^4$, far below the error $h^2$ of
    the finite differences. The true condensate uses
    $A = -V\gamma^{(4)} + c_g\gamma^{(4)}\gamma^{(0)}$; the negative control uses
    $A = -V\gamma^{(4)}$, the condensate of an equation without the gravitational
    part $c_g\gamma^{(4)}\gamma^{(0)}$. Its $S$ is also $e^{a_4}b_4^{-2}S_0$, but it
    does not solve the field equation of the corrected metric, so its tensor must not
    be conserved. The function `condensate(kind, x4_base)` returns a function
    `field(x4)` with $\Phi(x_4) = F\chi(x_4)$ and
    $\partial_4\Phi = F(A\chi - v_g\chi)$, `tensor_at(field, x4, x0)` the 64 entries of
    the tensor at a point of the history, and `divergence(field, x4, x0, h)` the
    eight components of $\nabla_\mu T^\mu{}_\nu$, with the derivatives $\partial_4 T$
    and $\partial_0 T$ replaced by central finite differences of step $h$ (the tensor
    of a condensate depends on $x_4$ and $x_0$ only). The cell only defines; it
    prints the effective mass $V$ and the coefficient $c_g$ of the test at $x_4 = 1$.
    """),
    code(r'''
    m9, lam9, H9 = 1.0, 0.5, 0.25  # the parameters of this section
    chi9 = rng.normal(size=16) + 1j * rng.normal(size=16)
    chi9 /= np.linalg.norm(chi9)  # the column chi at the time of a test point
    S9 = (bar(chi9) @ chi9).real  # S0 = chi^dagger C chi, constant along chi


    def a4_of(x4):
        return 0.3 * x4 + 0.05 * x4 ** 2


    def a4p_of(x4):
        return 0.3 + 0.1 * x4


    def b4_of(x4):
        return np.exp(0.4 * x4 - 0.02 * x4 ** 2)


    def u_of(x4):
        return 0.4 - 0.04 * x4  # b4'/b4


    def A_of(kind, x4):
        """A(x4) of the true condensate or of the control (no c_g g^(x4) g^(x0))."""
        V_now = m9 + lam9 * S9 * np.exp(a4_of(x4)) / b4_of(x4) ** 2  # m + lambda S
        A_now = -V_now * g4
        c_now = 1.5 * H9 * np.exp(a4_of(x4)) / np.sqrt(b4_of(x4))  # c_g at x4
        return A_now + c_now * g4 @ g0 if kind == "true" else A_now


    def flow(kind, column, x_from, x_to, count=50):
        """RK4 for chi' = A(x4) chi from x_from to x_to with count steps."""
        step = (x_to - x_from) / count
        x4, column = x_from, column.astype(complex)
        for _ in range(count):
            s1 = A_of(kind, x4) @ column
            s2 = A_of(kind, x4 + step / 2) @ (column + step / 2 * s1)
            s3 = A_of(kind, x4 + step / 2) @ (column + step / 2 * s2)
            s4 = A_of(kind, x4 + step) @ (column + step * s3)
            column = column + step / 6 * (s1 + 2 * s2 + 2 * s3 + s4)
            x4 += step
        return column


    def condensate(kind, x4_base):
        """field(x4) -> (Phi, dPhi/dx4) of the condensate with chi(x4_base) = chi9."""
        def field(x4):
            column = chi9 if x4 == x4_base else flow(kind, chi9, x4_base, x4)
            factor = np.exp(a4_of(x4) / 2) / b4_of(x4)  # F = e^(a4/2) b4^(-1)
            v_g = u_of(x4) - a4p_of(x4) / 2  # b4'/b4 - a4'/2
            return factor * column, factor * (A_of(kind, x4) @ column - v_g * column)
        return field


    def tensor_at(field, x4, x0):
        phi, d4 = field(x4)
        dphi = np.zeros((8, 16), dtype=complex)
        dphi[4] = d4
        return energy_momentum(phi, dphi, m9, lam9, a4_of(x4), a4p_of(x4),
                               b4_of(x4), u_of(x4), 6 * H9 * x0, H9)


    def divergence(field, x4, x0, h):
        """The eight components of nabla_mu T^mu_nu, with central differences of step h,
        and the size of the tensor (its largest entry)."""
        T = tensor_at(field, x4, x0)
        d4T = (tensor_at(field, x4 + h, x0) - tensor_at(field, x4 - h, x0)) / (2 * h)
        d0T = (tensor_at(field, x4, x0 + h) - tensor_at(field, x4, x0 - h)) / (2 * h)
        G = np.zeros((8, 8, 8))  # G[l, i, j] = Gamma^l_ij
        for (l, i, j), function in christoffel.items():
            G[l, i, j] = G[l, j, i] = function(x4, x0, H9)
        result = np.zeros(8)
        for nu in range(8):
            result[nu] = (d4T[4, nu] + d0T[0, nu]  # d_mu T^mu_nu (only x4 and x0)
                          + np.einsum("mml,l->", G, T[:, nu])  # Gamma^mu_mu l T^l_nu
                          - np.einsum("lm,ml->", G[:, :, nu], T))  # Gamma^l_mu nu T^mu_l
        return result, np.abs(T).max()


    report("effective mass V = m + lambda S at x4 = 1",
           f"{m9 + lam9 * S9 * np.exp(a4_of(1.0)) / b4_of(1.0) ** 2:.6f}")
    report("c_g at x4 = 1", f"{1.5 * H9 * np.exp(a4_of(1.0)) / np.sqrt(b4_of(1.0)):.6f}")
    '''),
    md(r"""
    The next cell computes the largest of the eight components of the divergence for
    eleven steps $h$ from $0.2$ down to $0.0002$ at the point $x_4 = 1$, $z = 0.5$,
    for the true condensate and for the control. For the true condensate the result
    must fall like $h^2$ (each halving of $h$ divides it by about 4): the exact
    divergence is zero and only the error of the finite differences is left. For the
    control it must approach a nonzero value. The cell also checks the true
    condensate at two more points (each with the column $\chi$ fixed at its own
    time), one of them at $z = 2.2$ beyond the fold, with $h = 0.001$ and
    $h = 0.0001$: the divergence must shrink about a hundredfold and end below
    $10^{-5}$ of the size of the tensor.
    """),
    code(r'''
    steps = 0.2 / 2.0 ** np.arange(11)  # 0.2, 0.1, ..., about 0.0002
    X4_TEST, X0_TEST = 1.0, 0.5 / (6 * H9)  # x4 = 1 and z = 0.5
    TRUE, CONTROL = condensate("true", X4_TEST), condensate("control", X4_TEST)
    true_sizes, control_sizes = [], []
    for h in steps:
        div_true, size_true = divergence(TRUE, X4_TEST, X0_TEST, h)
        div_control, _ = divergence(CONTROL, X4_TEST, X0_TEST, h)
        true_sizes.append(np.abs(div_true).max())
        control_sizes.append(np.abs(div_control).max())
    true_sizes, control_sizes = np.array(true_sizes), np.array(control_sizes)
    ratios = true_sizes[:6] / true_sizes[1:7]  # halving h from 0.2 to 0.003125
    check(np.all((ratios > 3.6) & (ratios < 4.4)),
          "true condensate: halving h divides the divergence by about 4 (error h^2)")
    check(true_sizes[8] < 1e-6 * size_true,
          "true condensate: the divergence falls below 1e-6 of the tensor's size")
    check(abs(control_sizes[-1] / control_sizes[-2] - 1) < 1e-3
          and control_sizes[-1] > 1e-2 * size_true,
          "control: the divergence tends to a nonzero value (it is not conserved)")
    for x4_point, z_point in ((2.0, 1.0), (0.5, 2.2)):
        x0_point = z_point / (6 * H9)
        other = condensate("true", x4_point)  # chi9 at the time x4_point
        coarse, size_other = divergence(other, x4_point, x0_point, 1e-3)
        fine, _ = divergence(other, x4_point, x0_point, 1e-4)
        shrink = np.abs(coarse).max() / np.abs(fine).max()  # about 10^2 for an h^2 error
        check(90 < shrink < 110 and np.abs(fine).max() < 1e-5 * size_other,
              f"true condensate conserved at x4 = {x4_point}, z = {z_point} "
              "(h = 0.001 and 0.0001)")
    WL = "Revision/theory/reports/wolfram-field-theory.json"
    check(recorded(WL, "exact_solution_nonlinear_homogeneous_C") == "PASS"
          and recorded(WL, "conservation_on_shell_general") == "PASS",
          "the record proves the conservation that these numbers confirm",
          record=f"{WL}, checks exact_solution_nonlinear_homogeneous_C and "
                 "conservation_on_shell_general")
    for h, t_size, c_size in zip(steps[::2], true_sizes[::2], control_sizes[::2]):
        say(f"h = {h:.5f}:  true condensate {t_size:.2e},  control {c_size:.4f}")
    '''),
    md(r"""
    The next cell draws the two series on logarithmic axes, with a line proportional
    to $h^2$ for comparison.
    """),
    code(r'''
    fig, ax = plt.subplots()
    ax.loglog(steps, true_sizes, "o-", label="true condensate")
    ax.loglog(steps, control_sizes, "s-",
              label="control (no $c_g\\gamma^{(4)}\\gamma^{(0)}$ part)")
    ax.loglog(steps, true_sizes[0] * (steps / steps[0]) ** 2, "k:",
              label="proportional to $h^2$")
    ax.set_xlabel("finite-difference step $h$")
    ax.set_ylabel("largest $|\\nabla_\\mu T^\\mu{}_\\nu|$")
    ax.set_title("Conservation of the full tensor of a condensate")
    ax.legend()
    save_figure(fig, "conservation_convergence",
                "The largest of the eight components of the covariant divergence "
                "$\\nabla_\\mu T^\\mu{}_\\nu$ of the full tensor of a condensate "
                "($m = 1$, $\\lambda = 0.5$, $H = 0.25$, history "
                "$a_4 = 0.3x_4 + 0.05x_4^2$, $b_4 = e^{0.4x_4 - 0.02x_4^2}$, point "
                "$x_4 = 1$, $z = 0.5$, corrected metric), computed with central finite "
                "differences of step $h$, against $h$ from $0.2$ to $0.0002$; both axes "
                "logarithmic, the divergence in units of energy per unit volume per "
                "unit length. For the true condensate (circles) it falls like $h^2$ "
                "(dotted line): the exact divergence is zero. For the control "
                "(squares), which leaves out the gravitational part "
                "$c_g\\gamma^{(4)}\\gamma^{(0)}$ of the condensate equation, it stays "
                "near $0.044$: its tensor is not conserved.")
    '''),
    md(r"""
    The next cell draws the eight components separately at the step $h = 0.001$, for
    the true condensate and for the control, as bars on a logarithmic axis, and
    checks what the picture shows: the control fails in the three momentum
    components along 3-space, while its energy component $\nu = x_4$, its hidden
    component $\nu = x_0$ and its three extra-time components vanish up to the error
    of the finite differences, as those of the true condensate do. The control's
    energy density and pressures are the same as those of the true condensate (its
    $S$ is also $e^{a_4}b_4^{-2}S_0$ and $p_3 = p_t = p_0$), so its energy balance
    holds. Its momentum flow along 3-space, however, is zero: in the corrected metric
    the flow $T^{x_4}{}_{x_i}$ of a condensate comes only from the part
    $c_g\gamma^{(4)}\gamma^{(0)}$ of its time derivative (the 3-space connection
    $\Omega_{x_i}$ anticommutes with $\gamma^{(4)}$), while the stresses between
    3-space and the hidden direction and the extra times remain; the momentum
    balance along 3-space then fails.
    """),
    code(r'''
    div_true, size_true = divergence(TRUE, X4_TEST, X0_TEST, 1e-3)
    div_control, _ = divergence(CONTROL, X4_TEST, X0_TEST, 1e-3)
    positions = np.arange(8)
    fig, ax = plt.subplots()
    floor = 1e-16  # zero components are drawn at this height on the logarithmic axis
    ax.bar(positions - 0.2, np.abs(div_true) + floor, width=0.4, label="true condensate")
    ax.bar(positions + 0.2, np.abs(div_control) + floor, width=0.4,
           label="control (no $c_g\\gamma^{(4)}\\gamma^{(0)}$ part)")
    ax.set_yscale("log")
    ax.set_ylim(1e-16, 10.0)
    ax.set_xticks(positions, [f"$\\nu = {n[0]}_{n[1]}$" for n in NAMES], fontsize=8)
    ax.set_ylabel("$|\\nabla_\\mu T^\\mu{}_\\nu|$ (with $h = 0.001$)")
    ax.set_title("The eight components of the divergence")
    ax.legend(fontsize=8)
    save_figure(fig, "divergence_components",
                "The eight components $|\\nabla_\\mu T^\\mu{}_\\nu|$, $\\nu = x_0, \\dots, "
                "x_7$, of the divergence of the full tensor of the condensate of the "
                "previous figure, with finite differences of step $h = 0.001$, on a "
                "logarithmic axis (components that vanish exactly are drawn at "
                "$10^{-16}$). The true condensate (left bars) has every component at the "
                "level of the finite-difference error, below $10^{-6}$. The control "
                "(right bars) has its three momentum components along 3-space, "
                "$\\nu = x_1, x_2, x_3$, between about $0.019$ and $0.044$, while its "
                "components $\\nu = x_0$, $x_4$ and $x_5, x_6, x_7$ stay at the error "
                "level of the true condensate: the control keeps the energy balance, "
                "the hidden balance and the extra-time balances but breaks the momentum "
                "balance along 3-space.")
    space_components = [1, 2, 3]  # nu = x1, x2, x3
    others = [0, 4, 5, 6, 7]  # nu = x0, x4, x5, x6, x7
    check(np.abs(div_control).max() > 1e3 * np.abs(div_true).max()
          and np.abs(div_control[space_components]).min() > 1e-3
          and np.abs(div_control[others]).max() < 1e-6 * size_true,
          "control: its three 3-space momentum components are nonzero (over 1000 times "
          "the true condensate's), its x0, x4, x5, x6, x7 components vanish up to the "
          "h^2 error")
    '''),
    md(r"""
    ## 10. The last check

    The last cell checks that the five figures are saved with their captions and
    prints the number of checks that passed.
    """),
    code(r'''
    captions = json.loads(output_file(CAPTION_FILE).read_text(encoding="utf-8"))
    expected_files = ["09c_1_generic_condensate.png", "09c_2_offdiagonal_entries.png",
                      "09c_3_witness_condensate.png",
                      "09c_4_conservation_convergence.png",
                      "09c_5_divergence_components.png"]
    check(sorted(captions) == expected_files and all(
        output_file(f"{FIGURE_FOLDER}/{name}").is_file() for name in expected_files),
        "the five figures of this notebook are saved and captioned")
    all_checks_passed()
    '''),
    md(r"""
    ## 11. What this notebook showed

    - A generic condensate $\Phi = e^{a_4/2}b_4^{-1}\chi$ of dirac16complex00 in the
      corrected metric has the diagonal of a perfect fluid ($-VS$ at $x_4$, the same
      pressure elsewhere, zero for $\lambda = 0$) but 36 nonzero off-diagonal
      entries: the 12 momentum flows $T^{x_4}{}_{x_i}$, $T^{x_i}{}_{x_4}$,
      $T^{x_4}{}_{x_t}$, $T^{x_t}{}_{x_4}$, which come from $H$, the 18 stresses
      between 3-space and the extra times, which have a part from $H$ and a part
      proportional to $4a_4' - b_4'/b_4$, and the 6 stresses between 3-space and the
      hidden direction, proportional to $4a_4' - b_4'/b_4$ (they vanish when 3-space
      and the block change at the same rate, and 30 remain). Its $x_4$-$x_0$ entries
      vanish.
    - Each off-diagonal entry is a fixed combination of one or two of 24 three-gamma
      bilinears (the record's statement, confirmed with four random columns), and
      the combination is exactly minus the one that the record lists for the entry
      (all 36 entries, ten groups of equal coefficients, five columns).
    - The record's witnesses, on the histories with constant $e^{2a_4}/b_4$, built
      from joint eigenvectors of $\gamma^{(1)}\gamma^{(5)}$,
      $\gamma^{(2)}\gamma^{(6)}$, $\gamma^{(3)}\gamma^{(7)}$, make all 24 bilinears
      vanish: their tensor is diagonal (the record shows it at every point of every
      such history; this notebook checked 36 points). The space of the eigenvalue
      $-i\omega$ has dimension 8 and each of its eight sectors dimension 1, so $v_1$
      and $v_2$ are unique up to a factor of size 1. Their $S = 2|v_1^\dagger Cv_2|^2$
      is never negative; the record's frequencies $\omega = 4, 3, 4$ are reproduced
      exactly and its three values of $S$ up to one common factor (the factor printed
      above; the record's columns are not of length 1). Only condensates whose 24
      bilinears all vanish, such as these, meet the condition of the field equations
      for $a_4$ and $b_4$ that the off-diagonal entries of the source vanish (one
      condition among several).
    - The full tensor of a condensate is conserved, $\nabla_\mu T^\mu{}_\nu = 0$,
      along a curved history of $a_4$ and $b_4$: the finite-difference divergence
      falls like $h^2$. A configuration that leaves out the gravitational part
      $c_g\gamma^{(4)}\gamma^{(0)}$ of the condensate equation keeps the energy, the
      hidden and the extra-time balances but breaks the three momentum balances along
      3-space: the term is needed for the conservation of the tensor.
    - Status: the statements are PROVED in the Revision record (exact, Wolfram and
      sympy); this notebook confirms them numerically (COMPUTED). The formula
      $S = 2\omega^2/V^2$ for unit $v_1$, $v_2$ is an observation for the three
      witnesses (COMPUTED, not proved). The parameter values are choices of this
      notebook.
    """),
]

if __name__ == "__main__":
    raise SystemExit(run_builder(__file__))
