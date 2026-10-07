#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
"""Builder of Notebook 20b, "One universe and its two partners: an exact case study"
(textbook "Universes in Pairs", chapter 20: Do universes come in pairs? What the
equations prove and what they do not).

The notebook Revision/textbook/notebooks/20b_one_universe_partners.ipynb is BUILT from
this file by Revision/textbook/tools/nbkit.py (never edit the .ipynb by hand):

    python Revision/textbook/tools/nbkit.py build \
        Revision/textbook/notebooks/src/20b_one_universe_partners.py --date YYYY-MM-DD
    python Revision/textbook/tools/nbkit.py check \
        Revision/textbook/notebooks/src/20b_one_universe_partners.py

The notebook takes ONE exact solution of the coupled equations of the theory (a
homogeneous condensate of dirac16complex00 that is the complete source of the author's
metric with the deflating history a4 = H x4, Einstein gravity) and examines its T1
partner, the T1 pair and its T2 mirror copy across the Z2 brane.  The theorems it uses
(T1, T2, C1) and the Einstein conditions of a condensate are Revision records; the
solution itself and the statements about its partners are computations of this
notebook, labelled as such.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools"))
from nbkit import code, md, run_builder  # noqa: E402

FIGURES = [
    "einstein_residuals",
    "null_requirement",
    "bookkeeping",
    "partner_in_time",
]

FACTS = {
    "id": "20b",
    "name": "20b_one_universe_partners",
    "title": "One universe and its two partners: an exact case study",
    "purpose": (
        "It builds, with exact arithmetic and the author's gamma matrices, one exact "
        "solution of the coupled equations: a homogeneous condensate of dirac16complex00 "
        "that is by itself the complete source of the author's metric with the "
        "exponentially deflating history a4 = H x4 in Einstein gravity. It then builds "
        "its T1 partner Gamma Phi with mass and coupling reversed, the T1 pair, and its "
        "T2 mirror copy across the Z2 brane, checks the field equation of each exactly "
        "and the Einstein equations of each numerically at many points, and shows: the "
        "universe needs no partner; the T1 partner solves its own field equation but "
        "cannot be the source of any member of the author's family in Einstein gravity; "
        "the T1 pair cannot either (corollary C1); the T2 copy is a solution with equal "
        "energy on the mirror patch. It reproduces the Revision records where they "
        "overlap and draws four teaching figures."
    ),
    "records": [
        ["Revision/algebra/gammas.json",
         "the author's real 16 by 16 gamma matrices (read)"],
        ["Revision/field_equations_a4/a4-equations.json",
         "the Einstein tensor of the author's metric and the null combination (read)"],
        ["Revision/field_equations_a4/reports/python-a4-report.json",
         "checks authorT16_gravity_term, authorT16_condensate_S_constant, "
         "authorT16_condensate_kinetic_diagonal, condensate_einstein_quadratic_U and "
         "einstein_null_energy_x8 (reproduced)"],
        ["Revision/field_equations_a4/reports/wolfram-a4-report.json",
         "checks condensate_equation_x8_consistent and condensate_diagonal_witness_exact "
         "(reproduced)"],
        ["Revision/pairing/reports/python-pairing.json",
         "checks T1.metric.commuting.euler_lagrange_map, T1.metric.commuting.emt, "
         "T1.metric.commuting.current, T2.metric.commuting.euler_lagrange_map, "
         "T2.metric.commuting.emt and Q.T2_image_keeps_B (reproduced)"],
        ["Revision/pairing/reports/wolfram-pairing.json",
         "checks Q_one_particle_maps and Q_Krein_metric_of_images (reproduced)"],
        ["Revision/docs/PAIR_CREATION_PROOFS.md",
         "the list of what the pairing theorems do not establish (read; one sentence is "
         "checked)"],
    ],
    "packages": ["numpy", "sympy", "matplotlib"],
    "needs_rust": [],
    "expected_seconds": 30,
    "timeout_seconds": 600,
    "files_written": ["Revision/textbook/figures/20b.captions.json"] + [
        f"Revision/textbook/figures/20b_{k}_{name}.png"
        for k, name in enumerate(FIGURES, 1)],
    "final_lines": [
        "PASS every figure file of this notebook exists",
        "ALL 25 CHECKS PASSED (notebook 20b)",
    ],
    "troubleshooting": [
        ["\"FileNotFoundError\" naming a file below the folder Revision",
         "the notebook reads seven files of the repository; it must be opened inside the "
         "folder Revision/textbook/notebooks of a complete copy of the repository made "
         "with git clone (a notebook copied alone to another folder cannot find them)."],
    ],
}

CELLS = [
    md(r"""
    ## 1. What this notebook computes

    The pairing theorems are statements about ALL solutions at once. This notebook
    follows them through ONE exact solution, so that every statement becomes a
    number. The solution (the **universe** of this notebook) is a homogeneous
    condensate $\Phi(x_4)$ of the commuting field dirac16complex00 that is the
    COMPLETE source of the author's metric with the exponentially deflating history
    $a_4 = Hx_4$ in Einstein gravity: the field equation (16 components) and the
    Einstein equations (64 components) hold together. Then the notebook builds

    - the **T1 partner** $\Gamma\Phi$ with the mass and the coupling reversed: it
      solves its own field equation, has the same frequency, the opposite energy
      density and charge density, and is NOT a source of the author's metric;
    - the **T1 pair** (universe plus T1 partner) as the only source: its source is
      zero, and the Einstein equations fail (corollary C1);
    - the **T2 mirror copy** $\gamma^{(x_8)}\Phi$ with the mass reversed and the same
      coupling, placed on the mirror patch across the Z2 brane: it solves the coupled
      equations there, with the SAME energy density and charge density.

    It checks every field equation exactly (sympy), every energy-momentum tensor and
    every Einstein equation numerically at many points (rounding $10^{-10}$), and
    draws four teaching figures. The lesson is in section 13: a universe is a complete
    solution without any partner; the theorems pair solutions, they do not create
    them.
    """),
    md(r"""
    ## 3. The words used in this notebook

    - **Coordinates** $x_1, \dots, x_8$ (the author's names): $x_1, x_2, x_3$ ordinary
      3-space (inflating), $x_4$ the time, $x_5, x_6, x_7$ the three EXTRA TIMES
      (deflating exponentially: scale factor $e^{-a_4}\sin^{1/6}z$), $x_8$ the hidden
      direction with $z = 6Hx_8$; the **patch** $0 < z < \pi/2$, the **mirror patch**
      $\pi/2 < z < \pi$, the **brane** $z = \pi/2$ between them (the Z2 construction
      across it is ASSUMED). In the code positions 0 to 7 stand for $x_1$ to $x_8$.
    - **Gamma matrices** $\gamma^{(a)}$, $C = \gamma^{(x_8)}\gamma^{(x_1)}\gamma^{(x_2)}
      \gamma^{(x_3)}$, **chirality** $\Gamma = \gamma^{(x_8)}\gamma^{(x_1)}\cdots
      \gamma^{(x_7)} = \mathrm{diag}(-I_8, I_8)$, $B = -iC\gamma^{(x_4)}$.
    - **Spinor** $\Phi$: 16 complex numbers (here functions of $x_4$);
      $\bar\Phi = \Phi^\dagger C$; **density** $S = \bar\Phi\Phi$; **charge density**
      $J^{x_4} = \Phi^\dagger B\Phi$.
    - **Mass** $m$, **coupling** $\lambda$, potential $U = \tfrac\lambda2S^2$,
      **effective mass** $M = m + \lambda S$.
    - **Condensate**: a solution that depends on the time $x_4$ only.
      **Frequency** $w$: $\Phi \propto e^{-iwx_4}$.
    - **Energy-momentum tensor** $T^\mu{}_\nu$ in the sign convention of the record of
      the field equations ($\sigma_T = +1$): energy density $\rho = -T^{x_4}{}_{x_4}$,
      pressures $p_\mu = T^\mu{}_\mu$ (no sum).
    - **Einstein equations** $G^\mu{}_\nu + \Lambda\delta^\mu_\nu = \kappa T^\mu{}_\nu$;
      the **residual** $R^\mu{}_\nu = G^\mu{}_\nu + \Lambda\delta^\mu_\nu - \kappa
      T^\mu{}_\nu$ is zero exactly when they hold.
    - **Linear member** $a_4 = AHx_4$: $A = 1$ is the author's deflating history.
    - **Null combination** $\rho + p_8$; **units** $H = \kappa = 1$.
    """),
    md(r"""
    ## 4. The physical and mathematical situation

    **The coupled equations.** The field: $\gamma^\mu D_\mu\Phi = (m + \lambda S)\Phi$.
    For a condensate only the $x_4$ derivative survives, and with the spin-connection
    term $\sum_\mu\gamma^\mu\Omega_\mu = 3H\gamma^{(x_8)}$ of the record the equation
    becomes $\Phi' = \mathcal{A}\Phi$ with $\mathcal{A} = -\gamma^{(x_4)}(M -
    3H\gamma^{(x_8)})$ (the record's `condensate_equation_x8_consistent`). Gravity: the
    record gives, for the linear member and a condensate with all 15 three-gamma
    bilinears zero, $\rho = mS + \tfrac\lambda2S^2$, $p_3 = p_t = p_8 = \tfrac\lambda2
    S^2$, and the Einstein equations reduce to two conditions:

    $$\kappa MS = -6(A^2 + 1)H^2,\qquad \kappa mS = -(36H^2 + 2\Lambda).$$

    **The theorems used (PROVED in the Revision record).** T1: $\Gamma\Phi$ solves the
    $(-m, -\lambda)$ field equation, $T \to -T$, $J \to -J$. T2: $\gamma^{(x_8)}\Phi$
    placed at the mirror point solves the $(-m, \lambda)$ field equation on the mirror
    patch, with the pulled-back (equal) $T$ and $J$. C1: a T1 pair as the only source
    is a zero source and has no Einstein solution. The record's null combination:
    in Einstein gravity every source of the author's metric must have
    $\kappa(\rho + p_8) = -6(a_4'^2 + H^2) < 0$.

    **What is new here (COMPUTED in this notebook, not a Revision record).** The
    explicit universe and its partners, and the conclusions of sections 10 to 12.

    **ASSUMED:** Einstein gravity; the sign convention $\sigma_T = +1$; the classical
    commuting field dirac16complex00 (not the quantised dirac16complex); the chosen
    numbers $A = 1$, $\Lambda = -36H^2$, $M = -5H$; the Z2 construction across the
    brane (section 12).
    """),
    md(r"""
    ## 5. The Revision records this notebook reproduces

    The next cell defines the helpers `read_json` (reads a JSON file of the
    repository), `record_verdict` (the verdict of a named check in a report) and
    `reproduces` (a check that passes only when this notebook's own result holds AND
    the named record check is PASS). It then reads one sentence of the record's list of
    what the pairing theorems do NOT establish; section 13 shows it on the example.
    """),
    code(r'''
    import contextlib  # redirect_stdout: send printed lines into a buffer
    import io  # StringIO: a text buffer in memory

    GAMMAS = "Revision/algebra/gammas.json"  # the author's gamma matrices
    A4_RECORD = "Revision/field_equations_a4/a4-equations.json"  # the a4 equations
    A4_PY = "Revision/field_equations_a4/reports/python-a4-report.json"
    A4_WL = "Revision/field_equations_a4/reports/wolfram-a4-report.json"
    PAIR_PY = "Revision/pairing/reports/python-pairing.json"
    PAIR_WL = "Revision/pairing/reports/wolfram-pairing.json"
    PROOFS = "Revision/docs/PAIR_CREATION_PROOFS.md"


    def read_json(relative):
        """Read a JSON file of the repository (a Revision record)."""
        return json.loads(repository_file(relative).read_text(encoding="utf-8"))


    def record_verdict(report_file, name):
        """The verdict ("PASS") of the check called name in a report; None if absent."""
        for entry in read_json(report_file)["checks"]:
            if entry["name"] == name:
                return entry["verdict"]
        return None


    def reproduces(condition, name, report_file, record_name):
        """A check that also requires the record check record_name to be PASS."""
        found = record_verdict(report_file, record_name) == "PASS"
        lines = io.StringIO()  # a text buffer
        with contextlib.redirect_stdout(lines):  # print() now writes into the buffer
            check(condition and found, name,
                  record=f"{report_file}, check {record_name}")
        print(lines.getvalue(), end="")  # both lines with one print call


    NO_NECESSITY = ("a single universe with mass $+m$ is an equally valid solution "
                    "without its partner")
    proofs = repository_file(PROOFS).read_text(encoding="utf-8")
    say(f"{PROOFS} says: \"... a single universe with mass +m is an equally valid "
        "solution without its partner.\"")
    check(NO_NECESSITY in proofs, "the record states that no partner is required")
    '''),
    md(r"""
    ## 6. The gamma matrices and the spin connection on both patches

    The next cell reads the author's gammas (exact whole numbers), builds $C$,
    $\Gamma$, $B$ and $S^{ab}$, and computes the canonical spin connection of the
    author's metric exactly as Notebook 20a does: lengths $E = (e^{a_4}s, e^{a_4}s,
    e^{a_4}s, 1, e^{-a_4}s, e^{-a_4}s, e^{-a_4}s, s_8\cot z)$ with $s = \sin^{1/6}z$,
    $s_8 = +1$ on the patch and $-1$ on the mirror patch, Christoffel symbols of the
    diagonal metric, and $\omega_{\mu ab} = \eta_{aa}(E_a/E_b)\Gamma^a{}_{\mu b}$ for
    $a \neq b$. It checks the record's $\sum_\mu\gamma^\mu\Omega_\mu = 3H\gamma^{(x_8)}$
    on the patch and finds $-3H\gamma^{(x_8)}$ on the mirror patch.
    """),
    code(r'''
    import itertools  # loops over all combinations of indices

    import numpy as np  # floating-point arrays
    import sympy as sp  # exact algebra

    NAMES = ["x1", "x2", "x3", "x4", "x5", "x6", "x7", "x8"]  # positions 0..7
    ETA = [1, 1, 1, -1, -1, -1, -1, 1]  # the frame metric eta, x1..x8
    I16, Z16 = sp.eye(16), sp.zeros(16, 16)
    gamma = [sp.Matrix([[sp.Rational(x) for x in row] for row in matrix])
             for matrix in read_json(GAMMAS)["gamma"]]  # gamma[a] = gamma^(x_(a+1))
    C = gamma[7] * gamma[0] * gamma[1] * gamma[2]  # C = g^(x8) g^(x1) g^(x2) g^(x3)
    chirality = gamma[7]  # Gamma = g^(x8) g^(x1) ... g^(x7), factor by factor
    for a in range(7):
        chirality = chirality * gamma[a]
    B = -sp.I * C * gamma[3]  # the Krein matrix B = -i C gamma^(x4)
    S_exact = [[(gamma[a] * gamma[b] - gamma[b] * gamma[a]) / 4 for b in range(8)]
               for a in range(8)]
    H = sp.symbols("H", positive=True)
    z = sp.symbols("z", real=True)
    x4 = sp.symbols("x4", real=True)
    a4 = sp.Function("a4")(x4)
    a4_value, slope = sp.symbols("a4_value slope", real=True)


    def d(expr, mu):
        """The partial derivative along the coordinate at position mu."""
        if mu == 3:
            return sp.diff(expr, x4)
        if mu == 7:
            return 6 * H * sp.diff(expr, z)  # d/dx8 = 6 H d/dz
        return sp.Integer(0)


    def spin_connection(s8):
        """The lengths E_a and omega[mu][a][b] = omega_mu ab (s8 = +1 patch, -1 mirror)."""
        s = sp.sin(z) ** sp.Rational(1, 6)
        E = [sp.exp(a4) * s] * 3 + [sp.Integer(1)] + [sp.exp(-a4) * s] * 3
        E = E + [s8 * sp.cot(z)]
        g = [ETA[a] * E[a] ** 2 for a in range(8)]
        christoffel = {}
        for a, b, c in itertools.product(range(8), repeat=3):
            value = 0
            if a == c:
                value += d(g[a], b)
            if a == b:
                value += d(g[a], c)
            if b == c:
                value -= d(g[b], a)
            christoffel[a, b, c] = value / (2 * g[a])
        omega = [[[sp.Integer(0)] * 8 for _ in range(8)] for _ in range(8)]
        for mu, a, b in itertools.product(range(8), repeat=3):
            if a != b:
                value = ETA[a] * E[a] * christoffel[a, mu, b] / E[b]
                value = value.subs(sp.Derivative(a4, x4), slope).subs(a4, a4_value)
                omega[mu][a][b] = sp.simplify(value)
        return [length.subs(a4, a4_value) for length in E], omega


    CONNECTION = {s8: spin_connection(s8) for s8 in (1, -1)}
    gravity_term = {}  # s8 -> sum over mu of gamma^mu Omega_mu
    for s8, (E, omega) in CONNECTION.items():
        Omega = [sum((omega[mu][a][b] * S_exact[a][b] / 2 for a in range(8)
                      for b in range(8) if omega[mu][a][b] != 0), Z16)
                 for mu in range(8)]
        gravity_term[s8] = sum((gamma[mu] / E[mu] * Omega[mu] for mu in range(8)),
                               Z16).applyfunc(sp.simplify)
    reproduces(gravity_term[1] == 3 * H * gamma[7],
               "patch: gamma^mu Omega_mu = 3 H gamma^(x8)", A4_PY, "authorT16_gravity_term")
    check(gravity_term[-1] == -3 * H * gamma[7],
          "mirror patch: gamma^mu Omega_mu = -3 H gamma^(x8)")
    '''),
    md(r"""
    ## 7. Choosing the universe: the two Einstein conditions

    We fix the geometry first: $H = \kappa = 1$, the author's deflating history
    $A = 1$ ($a_4 = Hx_4$; the extra times shrink as $e^{-x_4}$), and the cosmological
    constant $\Lambda = -36H^2$, chosen so that the universe has a positive energy
    density. We choose the effective mass $M = m + \lambda S = -5H$ (then the
    condensate oscillates, because $|M| > 3H$, with $w = \sqrt{M^2 - 9H^2} = 4H$). The
    two conditions then fix everything, line by line:

    1. $\kappa MS = -6(A^2 + 1)H^2 = -12$, so $S = -12/M = 12/5$;
    2. $\kappa mS = -(36 + 2\Lambda) = 36$, so $m = 36/S = 15$;
    3. $M = m + \lambda S$, so $\lambda = (M - m)/S = -20/(12/5) = -25/3$;
    4. $\rho = mS + \tfrac\lambda2S^2 = 36 - 24 = 12$ and $p = \tfrac\lambda2S^2 = -24$.

    The next cell checks the two conditions against the record (it rebuilds them from
    the record's Einstein tensor) and solves them with sympy.
    """),
    code(r'''
    record = read_json(A4_RECORD)
    ad1, ad2 = sp.symbols("ad1 ad2", real=True)  # a4' and a4''
    A, Lam, kappa = sp.symbols("A Lambda kappa", real=True)
    m, lam, S_sym = sp.symbols("m lambda S", real=True)


    def einstein(key):
        """The component key of the Einstein tensor E_(1) from the record."""
        text = record["lovelockTensors"]["E1"][key]["input"].replace("^", "**")
        return sp.sympify(text, locals={"ad1": ad1, "ad2": ad2, "H": H})


    G = {key: einstein(key) for key in ("x1x1", "x4x4", "x5x5", "x8x8")}
    LINEAR = {ad1: A * H, ad2: 0}  # the linear member a4 = A H x4
    rho_c, p_c = m * S_sym + lam * S_sym ** 2 / 2, lam * S_sym ** 2 / 2  # condensate
    time_eq = G["x4x4"].subs(LINEAR) + Lam + kappa * rho_c  # = 0
    hidden_eq = G["x8x8"].subs(LINEAR) + Lam - kappa * p_c  # = 0
    first = sp.expand(time_eq - hidden_eq)  # kappa (m + lambda S) S + 6 (A^2 + 1) H^2
    second = sp.expand(time_eq + hidden_eq)  # kappa m S + 36 H^2 + 2 Lambda
    reproduces(sp.expand(first - (kappa * (m + lam * S_sym) * S_sym
                                  + 6 * (A ** 2 + 1) * H ** 2)) == 0
               and sp.expand(second - (kappa * m * S_sym + 36 * H ** 2 + 2 * Lam)) == 0,
               "Einstein: kappa M S = -6 (A^2 + 1) H^2, kappa m S = -(36 H^2 + 2 Lambda)",
               A4_PY, "condensate_einstein_quadratic_U")
    CHOICE = {H: 1, kappa: 1, A: 1, Lam: -36}  # the geometry of this notebook
    M_VALUE = -5  # the effective mass M = m + lambda S
    S_value = sp.solve(first.subs(CHOICE).subs(lam, (M_VALUE - m) / S_sym), S_sym)[0]
    m_value = sp.solve(second.subs(CHOICE).subs(S_sym, S_value), m)[0]
    lam_value = (M_VALUE - m_value) / S_value
    rho_value = rho_c.subs({m: m_value, lam: lam_value, S_sym: S_value})
    p_value = p_c.subs({lam: lam_value, S_sym: S_value})
    for label, value in (("S", S_value), ("m", m_value), ("lambda", lam_value),
                         ("rho", rho_value), ("p", p_value)):
        report(label, value)
    check((S_value, m_value, lam_value, rho_value, p_value)
          == (sp.Rational(12, 5), 15, sp.Rational(-25, 3), 12, -24),
          "the universe: S = 12/5, m = 15, lambda = -25/3, rho = 12, p = -24")
    '''),
    md(r"""
    ## 8. Building the universe: the condensate $\Phi(x_4)$

    The record's recipe for a condensate whose 15 three-gamma bilinears vanish (they
    must, for the off-diagonal Einstein equations), at $M = -5$, $H = 1$, $w = 4$: the
    spinor $v_1$ with $\mathcal{A}v_1 = -iwv_1$ and $\gamma^{(x_1)}\gamma^{(x_5)} =
    \gamma^{(x_2)}\gamma^{(x_6)} = \gamma^{(x_3)}\gamma^{(x_7)} = -1$ on it, the
    spinor $v_2$ with the same frequency and the value $+1$, and $c =
    \overline{v_1^\dagger Cv_2}$; each is the null space of a stacked matrix. The
    family $\Phi_0(t) = v_1 + t\,c\,v_2$ keeps all 15 bilinears zero for every real
    $t$ and has $S(t) = 2t|v_1^\dagger Cv_2|^2$, so $t$ is fixed by $S = 12/5$. The
    universe is $\Phi(x_4) = e^{-iwx_4}\Phi_0$. The next cell builds it, checks the 15
    bilinears and $S$, checks that $S$ is constant ($C\mathcal{A} + \mathcal{A}^TC =
    0$), checks the 16 components of the field equation $\gamma^{(x_4)}\Phi' +
    3H\gamma^{(x_8)}\Phi = (m + \lambda S)\Phi$ EXACTLY at every time $x_4$, and
    computes the charge density $J^{x_4} = \Phi^\dagger B\Phi$.
    """),
    code(r'''
    w = sp.sqrt(M_VALUE ** 2 - 9)  # the frequency, H = 1
    A_matrix = -gamma[3] * (M_VALUE * I16 - 3 * gamma[7])  # Phi' = A Phi
    spaces = []
    for sign in (-1, 1):  # the value of g^(x1)g^(x5) = g^(x2)g^(x6) = g^(x3)g^(x7)
        stack = sp.Matrix.vstack(A_matrix + sp.I * w * I16,
                                 gamma[0] * gamma[4] - sign * I16,
                                 gamma[1] * gamma[5] - sign * I16,
                                 gamma[2] * gamma[6] - sign * I16)
        spaces.append(stack.nullspace())  # every solution of stack * v = 0
    v1, v2 = spaces[0][0], spaces[1][0]
    c = sp.conjugate(sp.expand((v1.H * C * v2)[0]))  # c = conj(v1^dagger C v2)
    t = sp.symbols("t", real=True)
    family = (v1 + t * c * v2).applyfunc(sp.expand)  # Phi_0(t)


    def bilinear(phi, matrix):
        """phibar matrix phi = phi^dagger C matrix phi (exact)."""
        return sp.expand((phi.H * C * matrix * phi)[0])


    t_value = sp.solve(bilinear(family, I16) - S_value, t)[0]
    phi0 = family.subs(t, t_value).applyfunc(sp.expand)  # the universe at x4 = 0
    report("t", t_value)
    NEEDED = sorted({tuple(sorted((i, 3, 7))) for i in (0, 1, 2, 4, 5, 6)}
                    | {tuple(sorted((i, j, 3))) for i in (0, 1, 2) for j in (4, 5, 6)})
    zero_15 = all(bilinear(family, gamma[a] * gamma[b] * gamma[e]) == 0
                  for a, b, e in NEEDED)  # for every real t, so also for t_value
    reproduces([len(space) for space in spaces] == [1, 1] and zero_15
               and bilinear(phi0, I16) == S_value,
               "the universe: 15 three-gamma bilinears 0 and S = 12/5",
               A4_WL, "condensate_diagonal_witness_exact")
    reproduces((C * A_matrix + A_matrix.T * C).applyfunc(sp.expand) == Z16,
               "C A + A^T C = 0: S stays 12/5 at every time", A4_PY,
               "authorT16_condensate_S_constant")
    Phi = phi0 * sp.exp(-sp.I * w * x4)  # the universe Phi(x4)


    def field_residual(field, term, mass, coupling, density):
        """gamma^(x4) field' + term field - (mass + coupling density) field."""
        return (gamma[3] * sp.diff(field, x4) + term * field
                - (mass + coupling * density) * field).applyfunc(sp.simplify)


    universe_ok = field_residual(Phi, gravity_term[1].subs(H, 1), m_value, lam_value,
                                 S_value) == sp.zeros(16, 1)
    reproduces(universe_ok, "the universe solves its field equation (16 components)",
               A4_WL, "condensate_equation_x8_consistent")
    charge_value = sp.simplify((phi0.H * B * phi0)[0])  # J^x4, constant in time
    report("charge density J^x4 of the universe", charge_value)
    '''),
    md(r"""
    ## 9. The universe alone solves the Einstein equations

    The next cell turns the geometry into numpy functions and evaluates the complete
    energy-momentum tensor of a configuration from its first jet, as in Notebook 20a:
    the value $\Phi$ and the derivatives (here only $\partial_4\Phi = -iw\Phi$; the
    condensate does not depend on the other coordinates). From the pairing records'
    tensor $T_{\mu\nu}$ it forms the mixed tensor of this notebook's convention,
    $T^\mu{}_\nu = -g^{\mu\mu}T_{\mu\nu}$ (the two conventions differ by a sign), and
    the Einstein residual $R^\mu{}_\nu = G^\mu{}_\nu + \Lambda\delta^\mu_\nu -
    \kappa T^\mu{}_\nu$ with $G$ from the record at $a_4' = H$. It does this at nine
    points: $z = 0.3, 0.8, 1.3$ on the patch and the times $x_4 = 0, 0.7, 2$ (where
    $a_4 = x_4$). All 64 components of the residual must vanish at every point.
    """),
    code(r'''
    point_symbols = (z, a4_value, slope, H)
    S_num = [[np.array(S_exact[a][b].tolist(), dtype=float) for b in range(8)]
             for a in range(8)]
    gamma_num = [np.array(g.tolist(), dtype=float) for g in gamma]
    C_num = np.array(C.tolist(), dtype=float)
    Gamma_num = np.array(chirality.tolist(), dtype=float)
    B_num = np.array(B.tolist(), dtype=complex)
    NUMERIC = {}
    for s8, (E, omega) in CONNECTION.items():
        pieces = [(mu, a, b, sp.lambdify(point_symbols, omega[mu][a][b], "numpy"))
                  for mu in range(8) for a in range(8) for b in range(8)
                  if omega[mu][a][b] != 0]
        NUMERIC[s8] = (sp.lambdify(point_symbols, E, "numpy"), pieces)


    def geometry_at(s8, z_value, a4_number, slope_number):
        """Metric, Omega_mu and curved gammas at one point (H = 1)."""
        lengths_f, pieces = NUMERIC[s8]
        values = (z_value, a4_number, slope_number, 1.0)
        E = np.array([float(x) for x in lengths_f(*values)])
        Om = [np.zeros((16, 16)) for _ in range(8)]
        for mu, a, b, f in pieces:
            Om[mu] += float(f(*values)) * S_num[a][b] / 2
        return {"g": np.array(ETA) * E ** 2, "Omega": Om,
                "up": [gamma_num[mu] / E[mu] for mu in range(8)],
                "down": [ETA[mu] * E[mu] * gamma_num[mu] for mu in range(8)]}


    def mixed_tensor(at, psi, dpsi, mass, coupling):
        """T^mu_nu (convention sigma_T = +1) and K^mu_mu of a first jet."""
        bar = psi.conj() @ C_num
        dbar = [row.conj() @ C_num for row in dpsi]
        D = [dpsi[mu] + at["Omega"][mu] @ psi for mu in range(8)]
        Dbar = [dbar[mu] - bar @ at["Omega"][mu] for mu in range(8)]
        S = (bar @ psi).real
        kinetic = [0.5 * (bar @ at["up"][mu] @ D[mu] - Dbar[mu] @ at["up"][mu] @ psi)
                   for mu in range(8)]  # K^mu_mu, no sum
        L = sum(kinetic).real - mass * S - coupling * S ** 2 / 2
        T = np.zeros((8, 8))
        for mu, nu in itertools.product(range(8), repeat=2):
            low = 0.25 * (bar @ at["down"][mu] @ D[nu] + bar @ at["down"][nu] @ D[mu]
                          - Dbar[mu] @ at["down"][nu] @ psi
                          - Dbar[nu] @ at["down"][mu] @ psi).real
            if mu == nu:
                low -= at["g"][mu] * L  # the pairing records' T_mu nu
            T[mu, nu] = -low / at["g"][mu]  # T^mu_nu = -g^(mu mu) T_mu nu
        return T, np.array([k.real for k in kinetic])


    G_numeric = np.diag([float(G[k].subs({ad1: 1, ad2: 0, H: 1})) for k in
                         ("x1x1", "x1x1", "x1x1", "x4x4", "x5x5", "x5x5", "x5x5",
                          "x8x8")])  # G^mu_nu at a4' = H, H = 1
    LAMBDA = -36.0
    phi0_num = np.array([complex(entry) for entry in phi0])
    W = float(w)
    POINTS = [(zv, xv) for zv in (0.3, 0.8, 1.3) for xv in (0.0, 0.7, 2.0)]


    def universe_jet(x_value, matrix=None):
        """Value and derivatives of matrix Phi at the time x_value."""
        value = phi0_num * np.exp(-1j * W * x_value)
        if matrix is not None:
            value = matrix @ value
        jet = [np.zeros(16, dtype=complex) for _ in range(8)]
        jet[3] = -1j * W * value  # d Phi / d x4 = -i w Phi
        return value, jet


    worst_residual, worst_kinetic = 0.0, 0.0
    for z_value, x_value in POINTS:
        at = geometry_at(1, z_value, x_value, 1.0)  # a4 = x4, a4' = 1
        T, kinetic = mixed_tensor(at, *universe_jet(x_value), float(m_value),
                                  float(lam_value))
        residual = G_numeric + LAMBDA * np.eye(8) - T  # kappa = 1
        worst_residual = max(worst_residual, np.abs(residual).max())
        wanted = np.zeros(8)
        wanted[3] = M_VALUE * float(S_value)  # K^x4_x4 = M S, all others 0
        worst_kinetic = max(worst_kinetic, np.abs(kinetic - wanted).max())
    T_universe = T  # the tensor at the last point (it is the same at every point)
    report("rho of the universe", f"{-T_universe[3, 3]:.10f}")
    report("p of the universe", f"{T_universe[0, 0]:.10f}")
    reproduces(worst_kinetic < 1e-10, "K^x4_x4 = M S and K^mu_mu = 0 otherwise (9 points)",
               A4_PY, "authorT16_condensate_kinetic_diagonal")
    check(worst_residual < 1e-10,
          "the universe ALONE solves all 64 Einstein equations (9 points)")
    '''),
    md(r"""
    ## 10. The T1 partner $\Gamma\Phi$

    By T1 the partner $\Gamma\Phi$ solves the field equation with $(-m, -\lambda) =
    (-15, 25/3)$. Its density is $S' = S$ (the scalar is unchanged), so its effective
    mass is $M' = -m - \lambda S = -M = 5$. Its matrix $\mathcal{A}' =
    -\gamma^{(x_4)}(M' - 3H\gamma^{(x_8)})$ equals $\Gamma\mathcal{A}\Gamma$, so it
    has the SAME eigenvalues $\pm iw$: the partner oscillates with the same frequency
    (similar matrices have equal spectra; the record proves the same for the
    one-particle Hamiltonians, $\Gamma h_m\Gamma = h_{-m}$). Its tensor is $T' = -T$
    and its charge density is $-J^{x_4}$. The next cell checks all of this exactly
    where possible, and numerically for the tensor.

    Can the partner ALONE be the source of the author's metric? The record's null
    combination says that every source must have $\kappa(\rho + p_8) =
    -6(a_4'^2 + H^2)$, which is at most $-6H^2$. The universe has $\kappa(\rho + p_8)
    = 12 - 24 = -12$, which fits $a_4' = \pm H$. The partner has $\rho' + p_8' =
    -(\rho + p_8) = +12$: positive, so it fits NO rate $a_4'$ and no $\Lambda$, in
    Einstein gravity. (Its tensor does not depend on $a_4$, so this holds for every
    member of the author's family.)
    """),
    code(r'''
    partner = chirality * Phi  # Gamma Phi
    partner_ok = field_residual(partner, gravity_term[1].subs(H, 1), -m_value,
                                -lam_value, S_value) == sp.zeros(16, 1)
    reproduces(partner_ok and bilinear(chirality * phi0, I16) == S_value,
               "Gamma Phi solves the (-m, -lambda) field equation; S' = S",
               PAIR_PY, "T1.metric.commuting.euler_lagrange_map")
    A_partner = -gamma[3] * (-M_VALUE * I16 - 3 * gamma[7])  # M' = -M
    same_spectrum = (chirality * A_matrix * chirality == A_partner
                     and (A_partner * A_partner + w ** 2 * I16) == Z16)
    reproduces(same_spectrum, "A' = Gamma A Gamma: the partner has the same frequency",
               PAIR_WL, "Q_one_particle_maps")
    partner_charge = sp.simplify(((chirality * phi0).H * B * (chirality * phi0))[0])
    reproduces(partner_charge == -charge_value, "the partner's charge density is -J^x4",
               PAIR_PY, "T1.metric.commuting.current")
    worst_sum, worst_partner = 0.0, 0.0
    for z_value, x_value in POINTS:
        at = geometry_at(1, z_value, x_value, 1.0)
        T_one, _ = mixed_tensor(at, *universe_jet(x_value), float(m_value),
                                float(lam_value))
        T_two, _ = mixed_tensor(at, *universe_jet(x_value, Gamma_num),
                                -float(m_value), -float(lam_value))
        worst_sum = max(worst_sum, np.abs(T_one + T_two).max())
        residual = G_numeric + LAMBDA * np.eye(8) - T_two
        worst_partner = max(worst_partner, np.abs(residual - 2 * T_one).max())
    T_partner = T_two
    reproduces(worst_sum < 1e-10, "T' = -T at all 9 points (64 components each)",
               PAIR_PY, "T1.metric.commuting.emt")
    check(worst_partner < 1e-10 and np.abs(2 * T_one).max() > 1.0,
          "partner alone: the Einstein residual is 2 kappa T, not zero")
    null_universe = -T_universe[3, 3] + T_universe[7, 7]  # kappa (rho + p8)
    null_partner = -T_partner[3, 3] + T_partner[7, 7]
    report("kappa (rho + p8) of the universe", f"{null_universe:.10f}")
    report("kappa (rho + p8) of the partner", f"{null_partner:.10f}")
    rate = sp.symbols("rate", real=True)  # a real value of a4'/H
    required = sp.expand(-(einstein("x4x4") - einstein("x8x8")).subs(
        {ad1: rate, ad2: 0, H: 1}))  # the requirement -6 (a4'^2 + 1)
    universe_null = rho_value + p_value  # exact: 12 - 24 = -12
    partner_null = -(rho_value + p_value)  # exact: T' = -T gives +12
    check(abs(null_universe - float(universe_null)) < 1e-10
          and abs(null_partner - float(partner_null)) < 1e-10,
          "kappa (rho + p8): universe -12, partner +12 (numbers = exact values)")
    reproduces(required == -6 * rate ** 2 - 6
               and sorted(sp.solve(required - universe_null, rate)) == [-1, 1]
               and sp.solve(required - partner_null, rate) == [],
               "the universe fits a4' = +-H; the partner fits no real rate",
               A4_PY, "einstein_null_energy_x8")
    '''),
    md(r"""
    ## 11. The T1 pair as the only source (corollary C1)

    With the universe AND its T1 partner as the only source, the source is
    $T + T' = 0$ and the residual is $G^\mu{}_\nu + \Lambda\delta^\mu_\nu$, which is
    not zero for any $\Lambda$ (Notebook 20a). At $a_4' = H$, $\Lambda = -36H^2$ it is
    $\mathrm{diag}(-24, -24, -24, -12, -24, -24, -24, -24)H^2$. The next cell checks
    this at the nine points.
    """),
    code(r'''
    worst_pair = 0.0
    for z_value, x_value in POINTS:
        at = geometry_at(1, z_value, x_value, 1.0)
        T_one, _ = mixed_tensor(at, *universe_jet(x_value), float(m_value),
                                float(lam_value))
        T_two, _ = mixed_tensor(at, *universe_jet(x_value, Gamma_num),
                                -float(m_value), -float(lam_value))
        residual = G_numeric + LAMBDA * np.eye(8) - (T_one + T_two)
        expected = np.diag([-24.0, -24, -24, -12, -24, -24, -24, -24])
        worst_pair = max(worst_pair, np.abs(residual - expected).max())
    check(worst_pair < 1e-10,
          "T1 pair alone: residual = G + Lambda = diag(-24, ..., -12, ...), not zero")
    '''),
    md(r"""
    ## 12. The T2 mirror copy across the brane

    By T2 (with $m \to -m$) the field $\Phi'(\pi - z) = \gamma^{(x_8)}\Phi(z)$ on the
    mirror patch solves the $(-m, \lambda) = (-15, -25/3)$ field equation there. For
    the condensate $\Phi$ does not depend on $z$, so the copy is simply
    $\gamma^{(x_8)}\Phi(x_4)$. Its density is $S' = -S$, so its effective mass is
    $M' = -m + \lambda S' = -M$. On the mirror patch the spin-connection term is
    $-3H\gamma^{(x_8)}$ (section 6). Its tensor is the pulled-back one, $R_8TR_8$,
    which for the diagonal $T$ of the condensate is $T$ itself: the SAME energy
    density $12$ and pressure $-24$. Its charge density is $+J^{x_4}$ (the record:
    $\gamma^{(x_8)}B\gamma^{(x_8)\dagger} = +B$). Because the mirror is an isometry, the
    Einstein tensor is the same on both patches. So the copy is a complete solution
    of the coupled equations on the mirror patch: together with the universe it
    fills the Z2-doubled geometry, with twice the energy, NOT zero. Whether the two
    halves can be joined at the brane (a junction condition, a brane tension) is not
    derived in the record (OPEN); the Z2 construction is ASSUMED.
    """),
    code(r'''
    copy = gamma[7] * Phi  # gamma^(x8) Phi on the mirror patch
    copy_ok = field_residual(copy, gravity_term[-1].subs(H, 1), -m_value, lam_value,
                             -S_value) == sp.zeros(16, 1)
    reproduces(copy_ok and bilinear(gamma[7] * phi0, I16) == -S_value,
               "the mirror copy solves the (-m, lambda) equation there; S' = -S",
               PAIR_PY, "T2.metric.commuting.euler_lagrange_map")
    copy_charge = sp.simplify(((gamma[7] * phi0).H * B * (gamma[7] * phi0))[0])
    reproduces(copy_charge == charge_value, "the copy's charge density is +J^x4",
               PAIR_PY, "Q.T2_image_keeps_B")
    worst_copy, worst_pull = 0.0, 0.0
    R8 = np.diag([1.0, 1, 1, 1, 1, 1, 1, -1])
    for z_value, x_value in POINTS:
        there = geometry_at(-1, np.pi - z_value, x_value, 1.0)  # the mirror point
        T_copy, _ = mixed_tensor(there, *universe_jet(x_value, gamma_num[7]),
                                 -float(m_value), float(lam_value))
        T_one, _ = mixed_tensor(geometry_at(1, z_value, x_value, 1.0),
                                *universe_jet(x_value), float(m_value), float(lam_value))
        worst_pull = max(worst_pull, np.abs(T_copy - R8 @ T_one @ R8).max())
        residual = G_numeric + LAMBDA * np.eye(8) - T_copy
        worst_copy = max(worst_copy, np.abs(residual).max())
    T_mirror = T_copy
    reproduces(worst_pull < 1e-10, "the copy's tensor is R8 T R8 = T at 9 mirror points",
               PAIR_PY, "T2.metric.commuting.emt")
    check(worst_copy < 1e-10,
          "the mirror copy ALONE solves the 64 Einstein equations on the mirror patch")
    '''),
    md(r"""
    The next cell draws the Einstein residual $R^\mu{}_\nu$ (an $8 \times 8$ table)
    for the four situations: the universe alone on the patch, the T1 partner alone,
    the T1 pair, and the T2 mirror copy alone on the mirror patch. A white table means
    that the Einstein equations hold.
    """),
    code(r'''
    tables = [
        ("universe $\\Phi$ alone", G_numeric + LAMBDA * np.eye(8) - T_universe),
        ("T1 partner $\\Gamma\\Phi$ alone", G_numeric + LAMBDA * np.eye(8) - T_partner),
        ("T1 pair (C1)", G_numeric + LAMBDA * np.eye(8) - T_universe - T_partner),
        ("T2 copy alone (mirror patch)", G_numeric + LAMBDA * np.eye(8) - T_mirror),
    ]
    fig, axes = plt.subplots(1, 4, figsize=(14.0, 4.0))
    for ax, (title, values) in zip(axes, tables):
        image = ax.imshow(values, cmap="RdBu_r", vmin=-48, vmax=48)
        for mu in range(8):
            if abs(values[mu, mu]) > 1e-6:
                ink = "white" if abs(values[mu, mu]) > 30 else "black"  # readable
                ax.text(mu, mu, f"{values[mu, mu]:.0f}", ha="center", va="center",
                        fontsize=6.5, color=ink)
        ax.set_xticks(range(8))
        ax.set_xticklabels(NAMES, fontsize=6.5)
        ax.set_yticks(range(8))
        ax.set_yticklabels(NAMES, fontsize=6.5)
        ax.grid(False)
        ax.set_title(title, fontsize=9)
    fig.colorbar(image, ax=list(axes), shrink=0.75, label="residual (units $H^2$)")
    save_figure(fig, "einstein_residuals",
                "The residual $G^\\mu{}_\\nu + \\Lambda\\delta^\\mu_\\nu - \\kappa "
                "T^\\mu{}_\\nu$ of the Einstein equations (rows $\\mu$, columns $\\nu$, "
                "$x_1$ to $x_8$; units $H = \\kappa = 1$; white means zero, the numbers "
                "are the nonzero diagonal entries) for the author's metric with the "
                "deflating history $a_4 = Hx_4$ and $\\Lambda = -36H^2$, with four "
                "different sources: the universe $\\Phi$ (a condensate with "
                "$m = 15$, $\\lambda = -25/3$) alone, which solves all 64 equations; "
                "its T1 partner $\\Gamma\\Phi$ alone, residual $2\\kappa T$; the T1 pair, "
                "residual $G + \\Lambda$ (corollary C1); and the T2 mirror copy "
                "$\\gamma^{(x_8)}\\Phi$ alone on the mirror patch, which solves all 64 "
                "equations there.")
    '''),
    md(r"""
    The next cell draws the null combination: the curve $\kappa(\rho + p_8) =
    -6(a_4'^2 + H^2)$ that Einstein gravity requires of any source, against the rate
    $a_4'/H$, and the values that the universe, the T1 partner, the T1 pair and the
    T2 copy supply (each a constant, a horizontal line).
    """),
    code(r'''
    rates = np.linspace(-2.5, 2.5, 501)
    fig, ax = plt.subplots(figsize=(7.0, 4.6))
    ax.plot(rates, -6 * (rates ** 2 + 1), color="black", linewidth=2.0,
            label="required: $-6(a_4'^2 + H^2)$")
    supplied = (("universe $\\Phi$", null_universe, "tab:blue", "-"),
                ("T1 partner $\\Gamma\\Phi$", null_partner, "tab:red", "-"),
                ("T1 pair", null_universe + null_partner, "tab:purple", "--"),
                ("T2 copy", -T_mirror[3, 3] + T_mirror[7, 7], "tab:green", ":"))
    for label, value, colour, style in supplied:
        ax.axhline(value, color=colour, linestyle=style, linewidth=1.6,
                   label=f"{label} supplies {value:+.0f}")
    ax.plot([-1.0, 1.0], [-12.0, -12.0], "o", color="tab:blue", markersize=8,
            label="solutions: $a_4' = \\pm H$")
    ax.set_xlabel("rate $a_4'/H$ of the metric function")
    ax.set_ylabel("$\\kappa(\\rho + p_8)/H^2$")
    ax.set_ylim(-45, 18)
    ax.set_title("What Einstein gravity requires, and what each source supplies")
    ax.legend(fontsize=7.5, loc="lower center", ncol=2)
    save_figure(fig, "null_requirement",
                "The null combination $\\kappa(\\rho + p_8)$ (energy density plus the "
                "pressure along $x_8$; vertical, units $H^2$) that Einstein gravity "
                "requires of every source of the author's metric, $-6(a_4'^2 + H^2)$ "
                "(black curve), against the rate $a_4'/H$ (horizontal), and the "
                "constant values supplied by the universe ($-12$, blue), its T1 "
                "partner ($+12$, red), the T1 pair (0, purple dashed) and the T2 "
                "mirror copy ($-12$, green dotted, on top of the blue line). Only the "
                "universe and its mirror copy meet the curve, at $a_4' = \\pm H$ (blue "
                "dots; the sign is a choice, $+H$ is the deflating history); the "
                "partner and the pair lie above the curve's maximum $-6$ and meet it "
                "nowhere.")
    '''),
    md(r"""
    ## 13. The bookkeeping, and what this example shows

    The next cell collects, for the universe, the T1 partner, the T1 pair, the T2 copy
    and the T2 pair (universe on the patch plus copy on the mirror patch, each
    counted at its own point), the energy density $\rho$, the pressure $p$, the charge
    density $J^{x_4}$ and the density $S$, and draws them as bars.
    """),
    code(r'''
    rho_u, p_u = -T_universe[3, 3], T_universe[0, 0]
    rho_m, p_m = -T_mirror[3, 3], T_mirror[0, 0]
    J_u = float(charge_value)
    rows = {
        "universe": (rho_u, p_u, J_u, float(S_value)),
        "T1 partner": (-T_partner[3, 3], T_partner[0, 0], float(partner_charge),
                       float(S_value)),
        "T1 pair": (rho_u - T_partner[3, 3], p_u + T_partner[0, 0],
                    J_u + float(partner_charge), 2 * float(S_value)),
        "T2 copy": (rho_m, p_m, float(copy_charge), -float(S_value)),
        "T2 pair": (rho_u + rho_m, p_u + p_m, J_u + float(copy_charge), 0.0),
    }
    for name, (r, p, j, s) in rows.items():
        say(f"{name:11s}: rho = {r:+7.2f}, p = {p:+7.2f}, J^x4 = {j:+6.2f}, "
            f"S = {s:+5.2f}")
    check(abs(rows["T1 pair"][0]) < 1e-10 and abs(rows["T1 pair"][2]) < 1e-12
          and abs(rows["T2 pair"][0] - 24) < 1e-9 and abs(rows["T2 pair"][2] + 6) < 1e-12,
          "T1 pair: rho = 0 and J = 0; T2 pair: rho = 24 and J = -6")
    quantities = ["$\\rho$", "$p$", "$J^{x_4}$", "$S$"]
    fig, ax = plt.subplots(figsize=(9.0, 5.0))
    width = 0.16
    colours = ["tab:blue", "tab:red", "tab:purple", "tab:green", "tab:olive"]
    for k, (name, values) in enumerate(rows.items()):
        positions = np.arange(4) + (k - 2) * width
        ax.bar(positions, values, width=width, color=colours[k], label=name)
        for x_value, value in zip(positions, values):
            if abs(value) < 1e-9:  # a bar of height zero: write 0 so it is seen
                ax.text(x_value, 1.0, "0", ha="center", fontsize=8,
                        color=colours[k], fontweight="bold")
    ax.axhline(0.0, color="black", linewidth=0.8)
    ax.set_xticks(range(4))
    ax.set_xticklabels(quantities)
    ax.set_ylabel("value (units $H = \\kappa = 1$)")
    ax.set_title("The bookkeeping of one universe and its partners")
    ax.legend(fontsize=8, ncol=5, loc="upper center", bbox_to_anchor=(0.5, -0.08))
    ax.set_ylim(-52, 30)
    save_figure(fig, "bookkeeping",
                "Energy density $\\rho$, pressure $p$, charge density $J^{x_4}$ and "
                "density $S$ (groups of bars; units $H = \\kappa = 1$) of the universe "
                "$\\Phi$ (blue), its T1 partner $\\Gamma\\Phi$ (red), the T1 pair "
                "(purple), the T2 mirror copy $\\gamma^{(x_8)}\\Phi$ (green) and the "
                "T2 pair (olive). The T1 partner has $\\rho$, $p$ and $J^{x_4}$ "
                "reversed and the same $S$, so the T1 pair has zero energy, pressure "
                "and charge; the T2 copy has the same $\\rho$, $p$ and $J^{x_4}$ and "
                "the reversed $S$, so the T2 pair has twice the energy and the "
                "charge of the universe.")
    '''),
    md(r"""
    The last picture shows the universe and its T1 partner in time. On the left, the
    real parts of two components of $\Phi(x_4)$ and of $\Gamma\Phi(x_4)$: component 1
    lies in the half where $\Gamma = -1$ (it changes sign), component 9 in the half
    where $\Gamma = +1$ (it does not); both oscillate with the same period
    $2\pi/w$. On the right, the 16 eigenvalues of $\mathcal{A}$ (universe) and
    $\mathcal{A}'$ (partner) in the complex plane: both are $\pm 4i$, each eight
    times. Same frequency, opposite energy density: the opposite sign of the energy
    is not an opposite frequency.
    """),
    code(r'''
    times = np.linspace(0.0, 3.0, 601)
    phi_t = np.outer(np.exp(-1j * W * times), phi0_num)  # rows: times, columns: A
    partner_t = phi_t @ Gamma_num.T  # Gamma Phi at every time
    fig, (left, right) = plt.subplots(1, 2, figsize=(12.0, 4.4))
    for index, colour in ((0, "tab:blue"), (8, "tab:orange")):
        left.plot(times, phi_t[:, index].real, color=colour, linewidth=4.0,
                  alpha=0.35, label=f"universe, component {index + 1}")
        left.plot(times, partner_t[:, index].real, "--", color=colour,
                  label=f"partner, component {index + 1}")  # drawn on top
    left.set_xlabel("time $x_4$ (units $1/H$)")
    left.set_ylabel("real part")
    left.set_title("same oscillation, the first half of the components reversed",
                   fontsize=9)
    left.legend(fontsize=7.5, loc="lower left", ncol=2)
    left.set_ylim(-2.2, 1.7)
    eig_u = np.linalg.eigvals(np.array(A_matrix.tolist(), dtype=float))
    eig_p = np.linalg.eigvals(np.array(A_partner.tolist(), dtype=float))
    right.plot(eig_u.real, eig_u.imag, "o", markersize=11, markerfacecolor="none",
               color="tab:blue", label="universe: eigenvalues of $\\mathcal{A}$")
    right.plot(eig_p.real, eig_p.imag, "x", markersize=9, color="tab:red",
               label="partner: eigenvalues of $\\mathcal{A}'$")
    right.set_xlim(-1.5, 1.5)
    right.set_ylim(-5.5, 5.5)
    right.set_xlabel("real part")
    right.set_ylabel("imaginary part (units $H$)")
    right.set_title("equal spectra: $\\pm 4i$, eight times each", fontsize=9)
    right.legend(fontsize=8, loc="center right")
    check(np.allclose(np.sort(eig_u.imag), np.sort(eig_p.imag), atol=1e-12)
          and np.abs(eig_u.real).max() < 1e-12,
          "both spectra are +-4i, eight times each (numerically)")
    save_figure(fig, "partner_in_time",
                "Left: the real parts of components 1 and 9 of the universe "
                "$\\Phi(x_4)$ (thick pale lines) and of its T1 partner "
                "$\\Gamma\\Phi(x_4)$ (dashed) against the time $x_4$ (units $1/H$). "
                "Component 1 belongs to "
                "the half where $\\Gamma = -1$ and is reversed, component 9 to the half "
                "where $\\Gamma = +1$ and is unchanged; both oscillate with the period "
                "$2\\pi/4$. Right: the 16 eigenvalues of the matrix $\\mathcal{A}$ of "
                "the universe (circles) and of $\\mathcal{A}' = \\Gamma\\mathcal{A}"
                "\\Gamma$ of the partner (crosses) in the complex plane: both are "
                "$\\pm 4i$, each eight times. The partner has the same frequency and "
                "the opposite energy density.")
    '''),
    md(r"""
    **What this example shows (COMPUTED here, exact for the field equations, to
    $10^{-10}$ for the Einstein equations):**

    1. A universe needs no partner. The condensate $\Phi$ with $m = 15$,
       $\lambda = -25/3$ is by itself a complete solution of the coupled equations
       with the deflating history $a_4 = Hx_4$. The record's sentence "a single
       universe with mass $+m$ is an equally valid solution without its partner" is
       here a solution one can write down.
    2. The T1 partner exists as a solution of ITS field equation (mass $-15$,
       coupling $25/3$), with the same frequency and opposite energy and charge. It is
       not a source of the author's metric in Einstein gravity, for any rate and any
       $\Lambda$, because its $\rho + p_8$ is positive.
    3. The T1 pair has zero energy and zero charge, and therefore (C1) it cannot be the
       source of the author's metric in Einstein gravity.
    4. The T2 mirror copy (mass $-15$, coupling $-25/3$) is a solution on the mirror
       patch with the SAME energy density and charge density. The Z2-doubled geometry
       with the universe on one side and its copy on the other solves the bulk
       equations on both patches; the brane itself is ASSUMED and its junction is not
       derived (OPEN).

    **What it does not show:** that the partner or the copy is created, or that it
    must exist; any process, rate or amplitude; anything about the quantised field
    dirac16complex (the condensate is a classical solution of dirac16complex00); the
    stability of the condensate.
    """),
    md(r"""
    ## 14. The last check

    The last cell checks that the four figure files exist in the folder
    Revision/textbook/figures and prints the number of checks that passed.
    """),
    code(r'''
    figure_names = ["einstein_residuals", "null_requirement", "bookkeeping",
                    "partner_in_time"]
    paths = [output_file(f"{FIGURE_FOLDER}/20b_{k}_{name}.png")
             for k, name in enumerate(figure_names, 1)]
    check(all(path.is_file() for path in paths),
          "every figure file of this notebook exists")
    all_checks_passed()
    '''),
    md(r"""
    ## 15. What this notebook showed

    - With $A = 1$, $\Lambda = -36H^2$ and $M = -5H$ the record's two Einstein
      conditions give $S = 12/5$, $m = 15$, $\lambda = -25/3$, $\rho = 12$,
      $p = -24$; the record's recipe gives an exact condensate with these numbers
      and the charge density $J^{x_4} = -3$, which solves its field equation exactly
      and, alone, all 64 Einstein equations (figure 1).
    - Its T1 partner $\Gamma\Phi$ solves the $(-15, 25/3)$ field equation with the
      same frequency $w = 4H$ (figure 4) and has $\rho' = -12$, $p' = 24$,
      $J' = +3$; with $\kappa(\rho' + p_8') = +12 > -6$ it is the source of no member
      of the author's family in Einstein gravity (figure 2).
    - The T1 pair has zero energy, pressure and charge, and its Einstein residual is
      $G + \Lambda \neq 0$: corollary C1 on an example (figures 1 and 3).
    - The T2 mirror copy $\gamma^{(x_8)}\Phi$ with $(-15, -25/3)$ solves the coupled
      equations on the mirror patch with the same $\rho = 12$ and $J^{x_4} = -3$; the
      T2 pair has $\rho = 24$ and $J^{x_4} = -6$ (figure 3).
    - The equations pair solutions; they neither require nor create the partner.
    """),
]

if __name__ == "__main__":
    raise SystemExit(run_builder(__file__))
