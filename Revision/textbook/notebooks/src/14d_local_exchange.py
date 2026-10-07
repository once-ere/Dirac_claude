#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
"""Builder of Notebook 14d, "The exact local exchange of the contact interaction and
the Kohn-Sham potentials" (textbook "Universes in Pairs", chapter 14).

The notebook Revision/textbook/notebooks/14d_local_exchange.ipynb is BUILT from this
file by Revision/textbook/tools/nbkit.py (never edit the .ipynb by hand):

    python Revision/textbook/tools/nbkit.py build \
        Revision/textbook/notebooks/src/14d_local_exchange.py --date YYYY-MM-DD
    python Revision/textbook/tools/nbkit.py check \
        Revision/textbook/notebooks/src/14d_local_exchange.py

Every exact statement reproduces a check of Revision/kohn_sham/reports/
ks-theory-python.json (section E of check_ks_theory.py); the zero-mode densities
reproduce the calibration of the coupling in Revision/kohn_sham/results/
parameters.json and the free density maximum of ground/summary.csv.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools"))
from nbkit import code, md, run_builder  # noqa: E402

FACTS = {
    "id": "14d",
    "name": "14d_local_exchange",
    "title": "The exact local exchange of the contact interaction and the Kohn-Sham "
             "potentials",
    "purpose": (
        "It derives with exact algebra on the author's gamma matrices the "
        "Hartree-Fock energy of the contact interaction U = (lambda/2) S^2 of "
        "dirac16complex in Kohn-Sham states: the positive-energy projector of the "
        "flat good-sector plane waves, the cancellation between the momenta p and -p "
        "that makes the one-body matrix of every symmetric occupation equal to "
        "(nB + SC)/16, the bookkeeping of Wick's rule checked term by term, the exact "
        "local exchange -(lambda/32)(n^2 + S^2), the filled-shell ratio -1/8, the "
        "Kohn-Sham potentials M_eff = m + (15/16) lambda S and v_v = -lambda n/16, "
        "and the exact Fock exchange of the closed-shell slab, which differs by "
        "+(lambda/32) Q^2; it then computes the densities of the eight brane zero "
        "modes and reproduces the Revision calibration of the coupling for N = 8 and "
        "the vanishing exact-Fock energy of that state, with four teaching figures."
    ),
    "records": [
        ["Revision/algebra/gammas.json",
         "the author's 16 x 16 gamma matrices in the order x1 to x8 (read)"],
        ["Revision/kohn_sham/ks-theory.json",
         "the block basis and the exchange coefficients (read and reproduced)"],
        ["Revision/kohn_sham/reports/ks-theory-python.json",
         "the sympy checks of the exchange that this notebook reproduces"],
        ["Revision/kohn_sham/reports/ks-theory-wolfram.json",
         "the same checks in WolframScript (their verdicts are read)"],
        ["Revision/kohn_sham/results/parameters.json",
         "the coefficients used by the Rust solver and the calibration of the "
         "coupling for N = 8 (reproduced)"],
        ["Revision/kohn_sham/results/ground/summary.csv",
         "the largest proper density of the free N = 8 state (reproduced)"],
        ["Revision/kohn_sham/results/exx/exact-fock-variant.csv",
         "the self-consistent exact-Fock energies of the N = 8 states (compared)"],
    ],
    "packages": ["numpy", "sympy", "matplotlib"],
    "needs_rust": [],
    "expected_seconds": 30,
    "timeout_seconds": 300,
    "files_written": [
        "Revision/textbook/figures/14d.captions.json",
        "Revision/textbook/figures/14d_1_pair_average.png",
        "Revision/textbook/figures/14d_2_energy_densities.png",
        "Revision/textbook/figures/14d_3_exact_fock_ratio.png",
        "Revision/textbook/figures/14d_4_zero_mode_state.png",
    ],
    "final_lines": [
        "PASS all four figure files of this notebook exist",
        "ALL 16 CHECKS PASSED (notebook 14d)",
    ],
    "troubleshooting": [],
}

CELLS = [
    md(r"""
    ## 1. What this notebook computes

    The quanta of dirac16complex interact through the contact term
    $U = \frac\lambda2 S^2$ of the Lagrangian, $S = \bar\Psi\Psi$. The Kohn-Sham
    model needs the energy of this interaction in a Kohn-Sham state (a Slater
    determinant or a thermal mixture of orbitals) as a function of the densities.
    This notebook derives it exactly, with the author's gamma matrices:

    - the plane waves of the good sector in flat space, their energies $\pm E$ and
      the projector on the positive ones;
    - why every occupation that is symmetric under $\mathbf p \to -\mathbf p$ has
      the one-body matrix $\rho = (nB + SC)/16$ (figure 1);
    - the Hartree-Fock energy: Hartree $\frac\lambda2S^2$ plus the EXACT LOCAL
      EXCHANGE $-\frac{\lambda}{32}(n^2 + S^2)$, and the ratio $-1/8$ of a filled
      level at rest (figure 2);
    - the Kohn-Sham potentials $M_{\rm eff} = m + \frac{15}{16}\lambda S$ and
      $v_v = -\frac{\lambda}{16}n$;
    - the exact Fock exchange of a closed-shell slab state, $-\frac{\lambda}{32}
      (n^2 + S^2 - Q^2)$, which the uniform-gas formula misses by
      $+\frac{\lambda}{32}Q^2$ (figure 3);
    - the densities and potentials of the eight brane zero modes (the state
      $N = 8$), which reproduce the Revision calibration of the coupling, and why the
      exact Fock exchange of that state is exactly zero (figure 4).

    It prints a PASS line for every check (16 in all) and saves four figures.
    """),
    md(r"""
    ## 3. The words used in this notebook

    - **Contact interaction**: the term $U(S) = \frac\lambda2S^2$ of the
      Lagrangian; $\lambda > 0$ is repulsive. $\lambda$ has the dimension
      mass$^{-6}$.
    - **Density**: an expectation value per unit volume. Number density
      $n = \langle\Psi^\dagger B\Psi\rangle$; scalar density
      $S = \langle\bar\Psi\Psi\rangle = \langle\Psi^\dagger C\Psi\rangle$; the
      density $Q = \langle\Psi^\dagger B\gamma^{(x_8)}\Psi\rangle$. PROPER densities
      are per proper 7-volume.
    - **Expectation-value rule**: for one quantum in the mode $u$,
      $\langle\Psi^\dagger X\Psi\rangle = u^\dagger BXu$; for many,
      $\langle\Psi^\dagger X\Psi\rangle = \mathrm{Tr}(X\rho)$ with the one-body
      matrix $\rho = \sum_{\rm occupied} f\,uu^\dagger B$ ($f$ the occupation).
    - **Trace** $\mathrm{Tr}\,X$: the sum of the diagonal entries; $\mathrm{Tr}(XY)
      = \mathrm{Tr}(YX)$.
    - **Normal ordering** $:\;:$: the operators of the free sea are reordered so
      that the vacuum has zero energy; it removes the infinite sea contributions.
    - **Quasi-free state, Wick's rule**: a Slater determinant or a thermal state of
      independent quanta; the expectation of four field operators is a sum of
      products of two-operator expectations (a "direct" and an "exchange" term).
    - **Hartree term, exchange term**: the direct and the exchange part of the
      interaction energy. **Hartree-Fock**: keeping both, for a quasi-free state.
    - **Kohn-Sham potential**: the derivative of the interaction energy density with
      respect to a density; it enters the one-quantum equation.
    - **Uniform gas**: quanta in flat space, the same in every place.
    - **Closed-shell slab**: the Kohn-Sham states of the model, uniform along 3-space
      but not along the hidden coordinate $y$, with complete lattice shells filled.
    - **Commutant**: all matrices that commute with a given set of matrices.
    - **Zero modes, $N = 8$**: the eight brane-bound orbitals at zero 3-momentum,
      $\chi = (a, 0)$ with $a \propto e^{My}$; filling them gives the state $N = 8$.
    """),
    md(r"""
    ## 4. The physical and mathematical situation

    The Revision theory (`Revision/kohn_sham/ks-theory.json`, section `exchange`)
    builds the Kohn-Sham functional of dirac16complex from the Hartree-Fock energy of
    the uniform good-sector gas, which turns out to be LOCAL (a function of the
    densities at one point) at every temperature. The steps, each exact:

    1. In flat space a plane wave $e^{-i\varepsilon x_4 + i\mathbf p\cdot\mathbf x}$
       of the good sector solves $h_{\mathbf p}u = \varepsilon u$ with
       $h_{\mathbf p} = M(-i\gamma^{(x_4)}) - p_a\gamma^{(x_4)}\gamma^{(a)}$, the sum
       over the four space-like directions $x_1, x_2, x_3, x_8$.
    2. $h_{\mathbf p}^2 = (M^2 + p^2)\,1$: the energies are $\pm E$,
       $E = \sqrt{M^2 + p^2}$, each 8 times.
    3. The interaction energy needs $\langle{:}S^2{:}\rangle$, which Wick's rule
       turns into $(\mathrm{Tr}\,C\rho)^2 - \mathrm{Tr}(C\rho C\rho)$.
    4. For symmetric occupations $\rho = (nB + SC)/16$, and the second trace is
       $(n^2 + S^2)/16$.

    Status: every formula here is PROVED (exact; verified twice in the Revision
    record). The use of the uniform-gas exchange for the slab states of the model is
    the canonical functional of the Revision theory (an approximation: no
    correlation energy); the exact Fock exchange of the slab is a DIAGNOSTIC.
    """),
    md(r"""
    ## 5. The gamma matrices, B and C

    The next cell reads the author's gamma matrices from the Revision record
    `Revision/algebra/gammas.json` (`g1` is $\gamma^{(x_1)}$, ..., `g8` is
    $\gamma^{(x_8)}$), builds $C = \gamma^{(x_8)}\gamma^{(x_1)}\gamma^{(x_2)}
    \gamma^{(x_3)}$ and $B = -iC\gamma^{(x_4)}$, and checks the facts used below:
    $B$ and $C$ square to 1, $\mathrm{Tr}\,B^2 = \mathrm{Tr}\,C^2 = 16$,
    $\mathrm{Tr}\,BC = 0$, $CBC = B$, and $(-i\gamma^{(x_4)})B = C$. It also defines
    `record_check`, which reads the verdict of a named check from the two Revision
    theory reports.
    """),
    code(r'''
    import math  # exp, sqrt, log10 of single numbers

    import numpy as np  # floating-point arrays
    import sympy as sp  # exact algebra with symbols

    PY_REPORT = "Revision/kohn_sham/reports/ks-theory-python.json"
    WL_REPORT = "Revision/kohn_sham/reports/ks-theory-wolfram.json"


    def record_check(name):
        """PASS in the sympy record and, if the WolframScript record has a check of
        that name, PASS there too."""
        verdicts = []
        for report_file in (PY_REPORT, WL_REPORT):
            data = json.loads(repository_file(report_file).read_text(encoding="utf-8"))
            found = [c["verdict"] for c in data["checks"] if c["name"] == name]
            verdicts.append(found[0] if found else "absent")
        return verdicts[0] == "PASS" and verdicts[1] in ("PASS", "absent")


    fixture = json.loads(repository_file("Revision/algebra/gammas.json")
                         .read_text(encoding="utf-8"))
    g = [sp.Matrix(m) for m in fixture["gamma"]]
    g1, g2, g3, g4, g5, g6, g7, g8 = g
    I16, Z16 = sp.eye(16), sp.zeros(16)
    C = g8 * g1 * g2 * g3
    B = -sp.I * C * g4
    facts_ok = (B * B == I16 and C * C == I16 and (B * B).trace() == 16
                and (C * C).trace() == 16 and (B * C).trace() == 0 and C * B * C == B
                and (-sp.I * g4) * B == C)
    check(facts_ok, "B^2 = C^2 = 1, Tr B^2 = Tr C^2 = 16, Tr BC = 0, CBC = B, (-i g4) B = C")
    '''),
    md(r"""
    ## 6. The plane waves of the good sector and their projector

    The four space-like directions are $x_1, x_2, x_3, x_8$; their gammas square to
    $+1$, and $\gamma^{(x_4)}$ squares to $-1$. Line by line:

    1. $h_{\mathbf p} = M(-i\gamma^{(x_4)}) - \sum_a p_a\gamma^{(x_4)}\gamma^{(a)}$.
    2. Squaring: $(-i\gamma^{(x_4)})^2 = -(\gamma^{(x_4)})^2 = 1$;
       $(\gamma^{(x_4)}\gamma^{(a)})^2 = -(\gamma^{(x_4)})^2(\gamma^{(a)})^2 = 1$;
       all mixed products anticommute and cancel in pairs. So
       $h_{\mathbf p}^2 = (M^2 + p_1^2 + p_2^2 + p_3^2 + p_8^2)\,1 = E^2\,1$.
    3. Hence $G_{\mathbf p} = \frac12(1 + h_{\mathbf p}/E)$ satisfies
       $G_{\mathbf p}^2 = G_{\mathbf p}$: it projects on the energy $+E$; its trace
       is 8 because $h_{\mathbf p}$ is traceless: eight positive-energy modes.

    The next cell checks the three lines with sympy.
    """),
    code(r'''
    M = sp.symbols("M", positive=True)  # the mass
    p1, p2, p3, p8 = sp.symbols("p1 p2 p3 p8", real=True)  # the momentum
    E = sp.symbols("E", positive=True)  # stands for sqrt(M^2 + p^2)
    h_p = M * (-sp.I * g4) - (p1 * g4 * g1 + p2 * g4 * g2 + p3 * g4 * g3 + p8 * g4 * g8)
    E_squared = M ** 2 + p1 ** 2 + p2 ** 2 + p3 ** 2 + p8 ** 2
    square_ok = (h_p * h_p - E_squared * I16).applyfunc(sp.expand).is_zero_matrix
    G_p = (I16 + h_p / E) / 2  # the projector on the positive energy
    projector_ok = ((G_p * G_p - G_p).subs(E, sp.sqrt(E_squared))
                    .applyfunc(sp.simplify).is_zero_matrix
                    and G_p.H == G_p and sp.simplify(G_p.trace()) == 8)
    check(square_ok and projector_ok and record_check("gas_mode_projector"),
          "h_p^2 = (M^2 + p^2) 1 and G_p = (1 + h_p/E)/2 is a projector of rank 8",
          record=f"{PY_REPORT}, check gas_mode_projector")
    '''),
    md(r"""
    ## 7. Why every symmetric occupation gives rho = (nB + SC)/16

    The one-body matrix of the eight positive-energy modes at momentum $\mathbf p$
    is $G_{\mathbf p}B$. Split it into a part that does not depend on the direction
    of $\mathbf p$ and a part that is linear in $\mathbf p$:

    $$G_{\mathbf p}B = \frac12\left(B + \frac ME(-i\gamma^{(x_4)})B\right) -
    \frac1{2E}\sum_a p_a\gamma^{(x_4)}\gamma^{(a)}B .$$

    The linear part changes sign under $\mathbf p \to -\mathbf p$. So if the
    occupation is the same for $\mathbf p$ and $-\mathbf p$ (true for every closed
    shell and for the thermal states), the linear parts cancel in pairs, and with
    $(-i\gamma^{(x_4)})B = C$ what is left is $\frac12(B + \frac ME C)$. The same
    holds for an average over all directions (the average of each component of a
    direction over the sphere is 0). For the negative-energy modes,
    $\frac12(1 - h_{\mathbf p}/E)B$, the result is $\frac12(B - \frac ME C)$. Adding
    up any such occupation therefore gives a combination of $B$ and $C$ only,
    $\rho = \alpha B + \beta C$; and since $\mathrm{Tr}(B\rho) = 16\alpha = n$ and
    $\mathrm{Tr}(C\rho) = 16\beta = S$,

    $$\rho = \frac{nB + SC}{16}.$$

    The next cell checks the pair cancellation, the sphere averages of the three
    components (exact integrals), both mode types and the trace formulas.
    """),
    code(r'''
    p_flip = {p1: -p1, p2: -p2, p3: -p3, p8: -p8}
    pair_average = ((G_p * B + (G_p * B).subs(p_flip)) / 2).applyfunc(sp.simplify)
    pair_ok = (pair_average - (B + M / E * C) / 2).applyfunc(sp.simplify).is_zero_matrix
    th, ph = sp.symbols("vartheta varphi", real=True)  # angles on the sphere
    components = [sp.sin(th) * sp.cos(ph), sp.sin(th) * sp.sin(ph), sp.cos(th)]
    sphere = [sp.integrate(sp.integrate(c * sp.sin(th), (ph, 0, 2 * sp.pi)), (th, 0, sp.pi))
              / (4 * sp.pi) for c in components]  # the averages of the components
    say(f"sphere averages of the three direction components: {sphere}")
    check(pair_ok and sphere == [0, 0, 0] and record_check("gas_angular_average"),
          "the average over p and -p (or over all directions) is (B + (M/E) C)/2",
          record=f"{PY_REPORT}, check gas_angular_average")
    h_0 = M * (-sp.I * g4)  # the p-independent part of h_p
    negative_ok = (((I16 - h_0 / E) / 2) * B - (B - M / E * C) / 2).is_zero_matrix
    check(negative_ok and record_check("gas_negative_energy_modes"),
          "negative-energy modes give (B - (M/E) C)/2: only B and C ever appear",
          record=f"{PY_REPORT}, check gas_negative_energy_modes")
    n, S, lam = sp.symbols("n S lambda", real=True)
    rho = (n * B + S * C) / 16  # the one-body matrix of a symmetric occupation
    check(sp.expand((B * rho).trace()) == n and sp.expand((C * rho).trace()) == S
          and record_check("gas_densities"),
          "rho = (nB + SC)/16 has Tr(B rho) = n and Tr(C rho) = S",
          record=f"{PY_REPORT}, check gas_densities")
    '''),
    md(r"""
    The next cell draws the cancellation for $M = 1$, $\mathbf p = (1, 0, 0, 0)$
    (so $E = \sqrt2$): the absolute values of the entries of the one-body matrix
    $G_{\mathbf p}B$ of one momentum (left), of its average with $-\mathbf p$
    (middle), which is exactly $\frac12(B + C/\sqrt2)$, and of the part linear in
    $\mathbf p$ (right), which cancels between $\mathbf p$ and $-\mathbf p$.
    """),
    code(r'''
    values = {M: 1, E: sp.sqrt(2), p1: 1, p2: 0, p3: 0, p8: 0}
    one_mode = np.abs(np.array((G_p * B).subs(values).evalf(), dtype=complex))
    averaged = np.abs(np.array(pair_average.subs(values).evalf(), dtype=complex))
    odd_part = np.abs(np.array((G_p * B - pair_average).subs(values).evalf(),
                               dtype=complex))
    fig, axes = plt.subplots(1, 3, figsize=(11.5, 3.9))
    fig.subplots_adjust(wspace=0.45)
    titles = ["$|G_{\\mathbf{p}}B|$: one momentum",
              "$|(G_{\\mathbf{p}} + G_{-\\mathbf{p}})B/2|$",
              "$|$part linear in $\\mathbf{p}|$"]
    for ax, data, title in zip(axes, (one_mode, averaged, odd_part), titles):
        image = ax.imshow(data, cmap="Blues", vmin=0.0, vmax=0.6,
                          interpolation="nearest")
        ax.set_title(title, fontsize=9)
        ax.set_xticks([0, 5, 10, 15])
        ax.set_yticks([0, 5, 10, 15])
        ax.set_xlabel("column")
        ax.set_ylabel("row")
        ax.grid(False)
        fig.colorbar(image, ax=ax, shrink=0.75)
    save_figure(fig, "pair_average",
                "Absolute values of the entries (rows and columns 0 to 15, darker is "
                "larger) of the one-body matrix of the eight positive-energy plane "
                "waves for $M = 1$ and the momentum $\\mathbf{p} = (1, 0, 0, 0)$, "
                "$E = \\sqrt{2}$: left for one momentum, middle averaged with "
                "$-\\mathbf{p}$, which leaves exactly $(B + C/\\sqrt{2})/2$, a "
                "combination of $B$ and $C$ only; right the part linear in "
                "$\\mathbf{p}$, which cancels between $\\mathbf{p}$ and $-\\mathbf{p}$. "
                "Every occupation that is symmetric under $\\mathbf{p} \\to "
                "-\\mathbf{p}$ therefore has the one-body matrix $(nB + SC)/16$.")
    '''),
    md(r"""
    ## 8. Wick's rule for the contact term

    For a quasi-free state with the two-operator expectations
    $f_{AB} = \langle\Psi_A^\dagger\Psi_B\rangle = \rho_{BA}$ (the expectation-value
    rule), Wick's rule gives for the normal-ordered square of
    $S = \Psi^\dagger C\Psi = \sum_{AB}\Psi_A^\dagger C_{AB}\Psi_B$

    $$\langle{:}S^2{:}\rangle = \sum_{ABCD}C_{AB}C_{CD}\,(f_{AB}f_{CD} -
    f_{AD}f_{CB}) .$$

    The first product is the DIRECT (Hartree) term, the second, with the minus sign
    of the anticommuting fields, the EXCHANGE (Fock) term. In matrix language the
    first sum is $(\mathrm{Tr}\,C\rho)^2$ and the second is $\mathrm{Tr}(C\rho C
    \rho)$. The next cell checks this bookkeeping term by term, as the Revision
    record did, for the explicit two-mode state with the mode vectors $u_1, u_2$ of
    the record, and for a second two-mode state $v_1, v_2$ with less symmetry: it
    adds up the $16^4$ terms of the sum (only those with nonzero $C$ entries are
    kept, 256 of them) and compares with the two traces.
    """),
    code(r'''
    half, i_half = sp.Rational(1, 2), sp.I / 2
    u1 = sp.Matrix([half, i_half, 0, 0, 0, 0, 0, 0, half, 0, 0, 0, 0, 0, -i_half, 0])
    u2 = sp.Matrix([0, 0, half, 0, -half, 0, 0, 0, 0, 0, i_half, 0, 0, 0, 0, i_half])
    v1 = sp.Matrix([1, 2, 0, -1, sp.I, 0, 3, 1, 0, 1, -2, sp.I, 0, 1, 1, 0]) / 4
    v2 = sp.Matrix([0, 1, sp.I, 2, 1, -1, 0, 0, 1, 0, sp.I, 1, 2, 0, -1, 1]) / 4
    nonzero = [(A_, B_) for A_ in range(16) for B_ in range(16) if C[A_, B_] != 0]
    wick_ok = True
    for name, modes in (("u1, u2 (record)", (u1, u2)), ("v1, v2", (v1, v2))):
        rho_2 = (modes[0] * modes[0].H + modes[1] * modes[1].H) * B  # one-body matrix
        f = rho_2.T  # f_AB = rho_BA
        brute = sp.simplify(sum(
            C[A_, B_] * C[C_, D_] * (f[A_, B_] * f[C_, D_] - f[A_, D_] * f[C_, B_])
            for A_, B_ in nonzero for C_, D_ in nonzero))
        direct = sp.simplify((C * rho_2).trace() ** 2)
        exchange = sp.simplify((C * rho_2 * C * rho_2).trace())
        say(f"state {name}: (Tr C rho)^2 = {direct}, Tr(C rho C rho) = {exchange}, "
            f"term-by-term sum = {brute}")
        wick_ok &= sp.simplify(brute - (direct - exchange)) == 0
    check(len(nonzero) == 16 and wick_ok and record_check("hf_wick_contraction"),
          "<:S^2:> = (Tr C rho)^2 - Tr(C rho C rho), checked term by term",
          record=f"{PY_REPORT}, check hf_wick_contraction")
    '''),
    md(r"""
    ## 9. The exact local exchange and the filled-shell ratio

    With $\rho = (nB + SC)/16$ (line by line, using $CBC = B$, $C^2 = 1$,
    $\mathrm{Tr}\,B^2 = \mathrm{Tr}\,C^2 = 16$, $\mathrm{Tr}\,BC = 0$):

    1. $C\rho = (nCB + S)/16$.
    2. $(C\rho)^2 = (n^2CBCB + nS\,CB + nS\,CB + S^2)/256 = (n^2 + 2nS\,CB +
       S^2)/256$, because $CBCB = BB = 1$.
    3. $\mathrm{Tr}(C\rho C\rho) = (16n^2 + 0 + 16S^2)/256 = (n^2 + S^2)/16$.
    4. The energy density is $\frac\lambda2\langle{:}S^2{:}\rangle = e_H + e_x$ with
       the Hartree term $e_H = \frac\lambda2S^2$ and the EXCHANGE
       $e_x = -\frac\lambda2\mathrm{Tr}(C\rho C\rho) = -\frac{\lambda}{32}(n^2 + S^2)$.

    This is exact, at every temperature, for every symmetric occupation: the exchange
    of the contact interaction is LOCAL. For one filled 8-fold level at rest
    ($n = S = 8$ per unit volume): $e_x/e_H = -\frac{1}{32}\cdot128/(\frac12\cdot64)
    = -\frac18$. The next cell checks 1 to 4 and the ratio.
    """),
    code(r'''
    e_x = sp.factor(-lam / 2 * (C * rho * C * rho).trace())  # the exchange energy density
    say(f"e_x = -(lambda/2) Tr(C rho C rho) = {e_x}")
    check(sp.simplify(e_x + lam / 32 * (n ** 2 + S ** 2)) == 0
          and record_check("exchange_uniform_gas"),
          "the exact local exchange e_x = -(lambda/32)(n^2 + S^2)",
          record=f"{PY_REPORT}, check exchange_uniform_gas")
    e_H = lam / 2 * S ** 2  # the Hartree energy density
    ratio = sp.simplify((e_x / e_H).subs({n: 8, S: 8}))
    say(f"one filled level at rest (n = S = 8): e_x/e_H = {ratio}")
    check(ratio == sp.Rational(-1, 8) and record_check("filled_shell_ratio"),
          "a filled 8-fold level at rest has e_x/e_H = -1/8",
          record=f"{PY_REPORT}, check filled_shell_ratio")
    '''),
    md(r"""
    ## 10. The Kohn-Sham potentials

    The interaction energy density is $e_{\rm int}(n, S) = e_H + e_x =
    \frac{15}{32}\lambda S^2 - \frac{1}{32}\lambda n^2$. The Kohn-Sham potentials are
    its derivatives: $M_{\rm eff} = m + \partial e_{\rm int}/\partial S = m +
    \frac{15}{16}\lambda S$ (it shifts the mass) and $v_v = \partial e_{\rm int}/
    \partial n = -\frac{1}{16}\lambda n$ (it enters $h$ as $v_v$ times the unit
    matrix). Because $e_{\rm int}$ is homogeneous of degree 2,
    $S\,\partial_S e + n\,\partial_n e = 2e$, so on shell
    $\langle L\rangle/\sqrt{|g|} = M_{\rm eff}S + v_vn - mS - e_{\rm int} =
    e_{\rm int}$. The next cell checks this and compares the coefficients with the
    Revision record (ks-theory.json) and with the numbers the Rust solver read
    (parameters.json: 0.9375, -0.0625, -0.03125, -0.03125).
    """),
    code(r'''
    m = sp.symbols("m", real=True)
    e_int = sp.expand(e_H + e_x)
    M_eff = m + sp.diff(e_int, S)  # the effective mass
    v_v = sp.diff(e_int, n)  # the vector potential
    say(f"e_int = {e_int}")
    say(f"M_eff = {M_eff},  v_v = {v_v}")
    check(sp.simplify(M_eff - m - sp.Rational(15, 16) * lam * S) == 0
          and sp.simplify(v_v + lam * n / 16) == 0 and record_check("ks_potentials"),
          "M_eff = m + (15/16) lambda S and v_v = -lambda n/16",
          record=f"{PY_REPORT}, check ks_potentials")
    on_shell = sp.simplify(M_eff * S + v_v * n - m * S - e_int - e_int)
    check(on_shell == 0 and record_check("ks_onshell_lagrangian"),
          "on shell <L>/sqrt|g| = M_eff S + v_v n - m S - e_int = e_int",
          record=f"{PY_REPORT}, check ks_onshell_lagrangian")
    theory = json.loads(repository_file("Revision/kohn_sham/ks-theory.json")
                        .read_text(encoding="utf-8"))
    potentials = theory["exchange"]["kohnShamPotentials"]
    gas = theory["exchange"]["uniformGas"]
    inputs = json.loads(repository_file("Revision/kohn_sham/results/parameters.json")
                        .read_text(encoding="utf-8"))["theoryInputs"]
    same = (sp.Rational(potentials["Meff_coefficient_of_lambda_S"]) == sp.Rational(15, 16)
            and sp.Rational(potentials["vv_coefficient_of_lambda_n"]) == sp.Rational(-1, 16)
            and sp.Rational(gas["coefficient_n2"]) == sp.Rational(-1, 32)
            and sp.Rational(gas["coefficient_S2"]) == sp.Rational(-1, 32)
            and inputs["MeffCoefficientOfLambdaS"] == 0.9375
            and inputs["vvCoefficientOfLambdaN"] == -0.0625
            and inputs["exchangeCoefficientN2"] == -0.03125
            and inputs["exchangeCoefficientS2"] == -0.03125)
    check(same and record_check("ks_theory_json_exchange"),
          "the coefficients 15/16, -1/16, -1/32, -1/32 equal the records",
          record="Revision/kohn_sham/ks-theory.json and results/parameters.json")
    '''),
    md(r"""
    The next cell draws the three energy densities per unit $\lambda n^2$ against
    the ratio $S/n$ (between $-1$ and $1$, where the physical states lie): the
    Hartree term $\frac12(S/n)^2$, the exchange $-\frac1{32}(1 + (S/n)^2)$ and their
    sum $e_{\rm int}$. The exchange is small and negative; at $S = n$ (a filled level
    at rest) it is $-1/8$ of the Hartree term; near $S = 0$ only the exchange is
    left.
    """),
    code(r'''
    s_over_n = np.linspace(-1.0, 1.0, 401)
    hartree = 0.5 * s_over_n ** 2
    exchange_curve = -(1.0 + s_over_n ** 2) / 32.0
    fig, ax = plt.subplots(figsize=(7.5, 4.4))
    ax.plot(s_over_n, hartree, label="Hartree $e_H/(\\lambda n^2) = (S/n)^2/2$")
    ax.plot(s_over_n, exchange_curve, "--",
            label="exchange $e_x/(\\lambda n^2) = -(1 + (S/n)^2)/32$")
    ax.plot(s_over_n, hartree + exchange_curve, ":", color="black",
            label="$e_{\\rm int} = e_H + e_x$")
    ax.plot([1.0], [-1.0 / 16.0], "o", color="C3")
    ax.annotate("$S = n$: $e_x = -e_H/8$", xy=(1.0, -1.0 / 16.0), xytext=(-0.05, 0.3),
                fontsize=8, color="C3", arrowprops={"arrowstyle": "->", "color": "C3"})
    ax.axhline(0.0, color="gray", linewidth=0.6)
    ax.set_xlabel("ratio of the scalar to the number density $S/n$")
    ax.set_ylabel("energy density per $\\lambda n^2$")
    ax.set_title("the Hartree-Fock energy of the contact interaction")
    ax.legend(fontsize=8, loc="upper center")
    save_figure(fig, "energy_densities",
                "The interaction energy densities of the contact term per unit "
                "$\\lambda n^2$ against the ratio $S/n$ of the scalar and the number "
                "density: the Hartree term $(S/n)^2/2$ (solid), the exact local "
                "exchange $-(1 + (S/n)^2)/32$ (dashed) and their sum $e_{\\rm int}$ "
                "(dotted). For $\\lambda > 0$ the exchange lowers the energy a little; "
                "at $S = n$ (a filled level at rest, red dot) it is $-1/8$ of the "
                "Hartree term, and near $S = 0$ it is all that is left.")
    '''),
    md(r"""
    ## 11. The exact Fock exchange of the closed-shell slab

    The states of the model are not uniform along $y$, and in each block the
    orbital is a $2\times2$ object. The Revision record computes the EXACT Fock
    exchange of such a closed-shell state: take one level with the $2\times2$ block
    density $D = \frac12(d_0 + d_1\sigma_1 + d_2\sigma_2 + d_3\sigma_3)$ in each of
    the four blocks of type $j = +1$ and $\sigma_3D\sigma_3$ in each of the four of
    type $-1$ (the degenerate partners), and average it over a closed shell of
    3-space directions; the average is the projection onto the commutant of the
    3-space rotations (the 64-dimensional space of matrices that commute with
    $\gamma^{(x_1)}\gamma^{(x_2)}$, $\gamma^{(x_1)}\gamma^{(x_3)}$,
    $\gamma^{(x_2)}\gamma^{(x_3)}$). The result: $n = 8d_0$, $S = 8d_2$,
    $Q = \langle\Psi^\dagger B\gamma^{(x_8)}\Psi\rangle = 8d_3$, the $y$-current
    $Y = 8d_1$, and

    $$e_x^{\rm exact} = -\frac{\lambda}{32}(n^2 + S^2 - Q^2 - Y^2).$$

    For eigen-orbitals $Y = 0$; so the uniform-gas exchange omits $+\frac{\lambda}{32}
    Q^2$. The canonical functional of the Revision theory is the uniform-gas one; the
    exact Fock exchange is a DIAGNOSTIC that the Rust solver reports and also solves
    as a variant. The next cell repeats the computation: it reads the block basis
    from the Revision record (and checks that it is unitary), builds the averaged
    one-body matrix with sympy's linear solver and checks the four densities and the
    exchange.
    """),
    code(r'''
    as_number = {"0": 0, "1": 1, "-1": -1, "I": sp.I, "-I": -sp.I}
    U = sp.Matrix([[as_number[e] for e in row] for row in
                   theory["blockBasis"]["unnormalisedColumns2Sqrt2V"]])
    V = U / (2 * sp.sqrt(2))  # the block basis of the record
    labels = [(j, s2, s3) for j in (1, -1) for s2 in (1, -1) for s3 in (1, -1)]
    s1 = sp.Matrix([[0, 1], [1, 0]])
    s2m = sp.Matrix([[0, -sp.I], [sp.I, 0]])
    s3 = sp.Matrix([[1, 0], [0, -1]])
    d0, d1, d2, d3 = sp.symbols("d0 d1 d2 d3", real=True)
    D = (d0 * sp.eye(2) + d1 * s1 + d2 * s2m + d3 * s3) / 2  # the block density
    G_slab = Z16
    for b, (j, _, _) in enumerate(labels):
        Vb = V[:, 2 * b:2 * b + 2]
        G_slab = G_slab + Vb * (D if j == 1 else s3 * D * s3) * Vb.H
    unknowns = sp.Matrix(16, 16, sp.symbols("x0:256"))  # a general 16 x 16 matrix
    equations = []
    for rotation in (g1 * g2, g1 * g3, g2 * g3):  # commute with the 3-space rotations
        equations += list(rotation * unknowns - unknowns * rotation)
    solution = sp.Matrix(16, 16, list(list(sp.linsolve(equations, list(unknowns)))[0]))
    free = sorted(solution.free_symbols, key=lambda s_: int(str(s_)[1:]))
    basis = [solution.subs({x: (1 if x == y else 0) for x in free}) for y in free]
    gram = sp.Matrix(len(basis), len(basis),
                     lambda i, k: (basis[i].H * basis[k]).trace())
    coefficients = gram.LUsolve(sp.Matrix([(b_.H * G_slab).trace() for b_ in basis]))
    G_avg = sp.simplify(sum((c_ * b_ for c_, b_ in zip(coefficients, basis)), Z16))
    rho_slab = G_avg * B
    n_s, S_s = sp.simplify((B * rho_slab).trace()), sp.simplify((C * rho_slab).trace())
    Q_s = sp.simplify((B * g8 * rho_slab).trace())
    e_x_slab = sp.expand(-lam / 2 * (C * rho_slab * C * rho_slab).trace())
    say(f"commutant dimension {len(basis)}; n = {n_s}, S = {S_s}, Q = {Q_s}")
    say(f"V unitary: {sp.simplify(V.H * V) == I16}")
    check(len(basis) == 64 and n_s == 8 * d0 and S_s == 8 * d2 and Q_s == 8 * d3
          and sp.simplify(e_x_slab + lam / 32 * (n_s ** 2 + S_s ** 2 - Q_s ** 2
                                                 - (8 * d1) ** 2)) == 0
          and record_check("exchange_slab_exact_fock"),
          "exact Fock exchange of the slab: -(lambda/32)(n^2 + S^2 - Q^2 - Y^2)",
          record=f"{PY_REPORT}, check exchange_slab_exact_fock")
    '''),
    md(r"""
    For one orbital $\chi = (a, ib)$ the three densities are proportional to
    $a^2 + b^2$ ($n$), $2ab$ ($S$, up to the sign $j$) and $a^2 - b^2$ ($Q$), so
    $S^2 + Q^2 = n^2$; for a mixture $S^2 + Q^2 \le n^2$: the physical states fill
    the disk $(S/n)^2 + (Q/n)^2 \le 1$. The next cell draws, over this disk, the
    ratio $e_x^{\rm exact}/e_x^{\rm gas} = (n^2 + S^2 - Q^2)/(n^2 + S^2)$ of the exact
    Fock exchange to the uniform-gas exchange ($Y = 0$). On the line $Q = 0$ the two
    agree; at the point $S = 0$, $Q = n$, which is the state of the zero modes
    (section 12), the exact exchange vanishes.
    """),
    code(r'''
    grid = np.linspace(-1.0, 1.0, 401)
    S_grid, Q_grid = np.meshgrid(grid, grid)  # S/n horizontally, Q/n vertically
    inside = S_grid ** 2 + Q_grid ** 2 <= 1.0
    ratio_grid = np.where(inside, (1.0 + S_grid ** 2 - Q_grid ** 2) / (1.0 + S_grid ** 2),
                          np.nan)
    fig, ax = plt.subplots(figsize=(6.4, 5.2))
    filled = ax.contourf(S_grid, Q_grid, ratio_grid, levels=np.linspace(0.0, 1.0, 11),
                         cmap="Blues")
    ax.contour(S_grid, Q_grid, ratio_grid, levels=[0.5], colors="gray", linewidths=0.8)
    fig.colorbar(filled, ax=ax, label="$e_x^{\\rm exact} / e_x^{\\rm gas}$")
    ax.plot([0.0, 0.0], [1.0, -1.0], "o", color="C3")  # S = 0, Q = +n and -n
    ax.annotate("zero modes ($N = 8$): ratio 0", (0.05, 0.9), fontsize=8, color="C3")
    ax.annotate("$Q = 0$: ratio 1", (-0.95, 0.04), fontsize=8,
                color="white")  # white text on the dark band
    ax.set_xlabel("$S/n$")
    ax.set_ylabel("$Q/n$")
    ax.set_aspect("equal")
    ax.grid(False)
    ax.set_title("exact Fock exchange / uniform-gas exchange")
    save_figure(fig, "exact_fock_ratio",
                "The ratio of the exact Fock exchange of a closed-shell slab state, "
                "$-(\\lambda/32)(n^2 + S^2 - Q^2)$, to the uniform-gas exchange "
                "$-(\\lambda/32)(n^2 + S^2)$, over the disk of possible density "
                "ratios $(S/n)^2 + (Q/n)^2 \\le 1$ (horizontal $S/n$, vertical "
                "$Q/n$, darker is larger, gray line the ratio 1/2). On the line "
                "$Q = 0$ the two exchanges agree; toward the top and bottom of the "
                "disk the uniform-gas formula overestimates the exchange, and at "
                "$S = 0$, $Q = \\pm n$ (red dots; the top one is the state of the "
                "eight zero modes) the exact exchange vanishes.")
    '''),
    md(r"""
    ## 12. The state of the eight zero modes (N = 8)

    The simplest Kohn-Sham state of the model fills the eight brane zero modes at
    $k = 0$ (both block types, even parity). Each orbital is $\chi = (a, 0)$ with
    $a = \sqrt{2M/(1 - e^{-2ML})}\,e^{My}$ (normalised on the patch). The densities,
    line by line (Revision record, `densities`):

    1. One orbital: $n_o = P\,(a^2 + b^2) = Pa^2$, $s_o = P\,j\,2ab = 0$,
       $q_o = P\,(a^2 - b^2) = Pa^2$, with $P = e^{-6Hy}/(\ell^3v_t)$ (the factor
       that makes the densities proper).
    2. The state: $n = \sum w\,g\,f\,n_o$ with the weight $w = \frac12$ of the
       ASSUMED Z2 doubled system, the degeneracy $g = 4$ per block type and $f = 1$:
       $n = \frac12(4 + 4)Pa^2 = 4Pa^2$; $S = 0$; $Q = n$.
    3. The potentials to first order in $\lambda$ (free orbitals):
       $M_{\rm eff} - m = \frac{15}{16}\lambda S = 0$, $v_v = -\frac{\lambda}{16}n$.
    4. The Revision solver calibrates its couplings by the largest first-order
       potential per unit $\lambda$, max over $y$ of $\max(\frac{15}{16}|S|,
       |n|/16)$, here $n_{\max}/16$; $\lambda_1$ and $\lambda_2$ are $0.1$ and $0.3$
       divided by it, rounded to 4 significant digits.
    5. Exact Fock exchange: with $S = 0$ and $Q = n$, $e_x^{\rm exact} =
       -\frac{\lambda}{32}(n^2 - Q^2) = 0$. In the exact-Fock functional the
       potential is $v_v + w_Q\sigma_3$ with $w_Q = \frac{\lambda}{16}Q$, which on
       $(a, 0)$ acts as $\frac{\lambda}{16}(Q - n) = 0$: the zero modes stay exact
       solutions with $\varepsilon = 0$ and the energy of the state is exactly 0.

    With $H = m = 1$, $L = 3$, $\ell = 2\pi/0.25$, $v_t = 1$, the next cell computes
    $n(y)$ and its maximum (at the tip $y = -3$, where $e^{-6Hy}a^2 \propto
    e^{(2M - 6H)y}$ is largest) and compares with the records: the largest proper
    density of the free state $N = 8$ (`ground/summary.csv`, column `n_max`), the
    strength per $\lambda$, $\lambda_{1,2}$ and the first-order potentials
    (`parameters.json`), and the self-consistent exact-Fock energies of all twenty
    $N = 8$ states (`exx/exact-fock-variant.csv`), which must be zero to rounding.
    """),
    code(r'''
    H_val, m_val, L_val = 1.0, 1.0, 3.0
    ell = 2.0 * math.pi / 0.25  # the coordinate size of the 3-torus
    vol7 = ell ** 3 * 1.0  # the coordinate 7-volume ell^3 v_t
    y = np.linspace(-L_val, 0.0, 1801)  # the hidden coordinate
    a_sq = 2.0 * m_val / (1.0 - math.exp(-2.0 * m_val * L_val)) * np.exp(2.0 * m_val * y)
    P = np.exp(-6.0 * H_val * y) / vol7  # proper-density factor
    n_y = 4.0 * P * a_sq  # line 2
    n_max = float(np.max(n_y))
    summary = repository_file("Revision/kohn_sham/results/ground/summary.csv") \
        .read_text(encoding="utf-8").splitlines()
    header = summary[0].split(",")
    free8 = dict(zip(header, [r for r in summary if r.startswith("N8_lam0_a00,")][0]
                     .split(",")))
    report("largest proper density of the free N = 8 state", f"{n_max:.10f}",
           "per unit proper 7-volume")
    check(abs(n_max / float(free8["n_max"]) - 1.0) < 1e-9 and float(y[np.argmax(n_y)])
          == -3.0,
          "n_max = 4 P a^2 at the tip y = -3 equals the record",
          record="Revision/kohn_sham/results/ground/summary.csv, N8_lam0_a00, n_max")


    def round_significant(x, digits):
        """x rounded to digits significant digits (halves away from zero)."""
        exponent = math.floor(math.log10(abs(x))) - (digits - 1)
        scale = 10.0 ** (-exponent)
        return math.copysign(math.floor(abs(x) * scale + 0.5), x) / scale


    strength = n_max / 16.0  # line 4: the largest first-order potential per lambda
    lambda_1 = round_significant(0.1 / strength, 4)
    lambda_2 = round_significant(0.3 / strength, 4)
    parameters = json.loads(repository_file("Revision/kohn_sham/results/parameters.json")
                            .read_text(encoding="utf-8"))
    calibration = [c for c in parameters["couplingCalibration"]["values"]
                   if c["N"] == 8.0][0]
    report("strength per lambda", f"{strength:.9f}")
    report("lambda_1, lambda_2", f"{lambda_1}, {lambda_2}")
    report("first-order potentials", f"{lambda_1 * strength:.10f}, "
           f"{lambda_2 * strength:.10f}", "m")
    check(abs(strength / calibration["strengthPerLambda"] - 1.0) < 1e-9
          and lambda_1 == calibration["lambda1"] and lambda_2 == calibration["lambda2"]
          and abs(lambda_1 * strength - calibration["firstOrderPotential1"]) < 1e-9
          and len(set(calibration["strengthPerLambdaAtSlices"])) == 1,
          "strength 5.1388, lambda_1 = 0.01946, lambda_2 = 0.05838 (the same at all "
          "slices)", record="Revision/kohn_sham/results/parameters.json, "
          "couplingCalibration N = 8")
    exx = repository_file("Revision/kohn_sham/results/exx/exact-fock-variant.csv") \
        .read_text(encoding="utf-8").splitlines()
    exx_header = exx[0].split(",")
    rows8 = [dict(zip(exx_header, r.split(","))) for r in exx[1:] if r.startswith("N8_")]
    largest = max(abs(float(r["E_exact_fock_scf"])) for r in rows8)
    check(len(rows8) == 20 and largest < 1e-12,
          "the self-consistent exact-Fock energy of all 20 N = 8 states is 0",
          record="Revision/kohn_sham/results/exx/exact-fock-variant.csv, "
                 "E_exact_fock_scf")
    '''),
    md(r"""
    The next cell draws the state. Left: the proper density $n(y)$ and the
    coordinate density $e^{6Hy}n(y)$ (particles per unit $y$ and per unit coordinate
    volume) on a logarithmic axis: the zero modes sit at the brane in the coordinate
    density, but because the proper 7-volume $e^{6Hy}$ shrinks toward the tip, the
    PROPER density, which the interaction feels, is largest at the tip. Right: the
    first-order vector potential $v_v = -\lambda n/16$ of the uniform-gas
    functional for $\lambda_1$ and $\lambda_2$ (its largest size is $0.1$ and
    $0.3\,m$, by the calibration) and the exact-Fock combination
    $v_v + w_Q = \frac{\lambda}{16}(Q - n) = 0$.
    """),
    code(r'''
    fig, (left, right) = plt.subplots(1, 2, figsize=(10.5, 4.0))
    fig.subplots_adjust(wspace=0.32)  # room for the label of the right panel
    left.semilogy(y, n_y, label="proper density $n(y) = 4Pa^2$")
    left.semilogy(y, np.exp(6.0 * y) * n_y, "--",
                  label="coordinate density $e^{6Hy} n(y)$")
    left.set_xlabel("$y$ (units of $1/H$; tip at $-3$, brane at $0$)")
    left.set_ylabel("density (logarithmic)")
    left.set_title("the eight zero modes ($N = 8$, $\\lambda = 0$)")
    left.legend(fontsize=8)
    right.plot(y, -lambda_1 * n_y / 16.0, label=f"$v_v$, $\\lambda_1 = {lambda_1}$")
    right.plot(y, -lambda_2 * n_y / 16.0, label=f"$v_v$, $\\lambda_2 = {lambda_2}$")
    right.plot(y, np.zeros_like(y), ":", color="black",
               label="exact Fock: $v_v + w_Q = 0$")
    right.set_xlabel("$y$ (units of $1/H$)")
    right.set_ylabel("first-order potential (units of $m$)")
    right.set_title("the Kohn-Sham potential of the zero modes")
    right.legend(fontsize=8, loc="lower right")
    save_figure(fig, "zero_mode_state",
                "The state of the eight brane zero modes ($N = 8$, $m = H = 1$, "
                "$L = 3$, $\\Delta k = 0.25$, $v_t = 1$). Left, logarithmic axis: the "
                "proper density $n(y) = 4Pa^2$ (solid) and the coordinate density "
                "$e^{6Hy}n(y)$ (dashed) against $y$ (units of $1/H$); the orbitals "
                "sit at the brane, but the proper density is largest at the tip, "
                "$n_{\\max} = 82.22$ at $y = -3$. Right: the first-order vector "
                "potential $v_v = -\\lambda n/16$ of the uniform-gas functional for "
                "$\\lambda_1 = 0.01946$ and $\\lambda_2 = 0.05838$ (lowest values "
                "$-0.1$ and $-0.3$ in units of $m$, the calibration of the Revision "
                "runs) and the exact-Fock potential, which is zero for this state.")
    '''),
    md(r"""
    ## 13. The last check

    The last cell checks that the four figure files exist and prints the number of
    checks that passed.
    """),
    code(r'''
    figure_names = ["14d_1_pair_average.png", "14d_2_energy_densities.png",
                    "14d_3_exact_fock_ratio.png", "14d_4_zero_mode_state.png"]
    check(all(output_file(f"{FIGURE_FOLDER}/{name}").is_file() for name in figure_names),
          "all four figure files of this notebook exist")
    all_checks_passed()
    '''),
    md(r"""
    ## 14. What this notebook showed

    - The flat good-sector plane waves have the energies $\pm\sqrt{M^2 + p^2}$, each
      8 times; every occupation symmetric under $\mathbf p \to -\mathbf p$ has the
      one-body matrix $\rho = (nB + SC)/16$ (PROVED).
    - Wick's rule gives $\langle{:}S^2{:}\rangle = (\mathrm{Tr}\,C\rho)^2 -
      \mathrm{Tr}(C\rho C\rho)$, and the exchange of the contact interaction is
      exactly local: $e_x = -\frac{\lambda}{32}(n^2 + S^2)$ at every temperature;
      a filled level at rest has $e_x/e_H = -1/8$ (PROVED).
    - The Kohn-Sham potentials are $M_{\rm eff} = m + \frac{15}{16}\lambda S$ and
      $v_v = -\frac{\lambda}{16}n$; on shell $\langle L\rangle/\sqrt{|g|} =
      e_{\rm int}$ (PROVED; the coefficients equal those the Rust solver used).
    - For the closed-shell slab states the exact Fock exchange is
      $-\frac{\lambda}{32}(n^2 + S^2 - Q^2 - Y^2)$; the canonical (uniform-gas)
      functional omits $+\frac{\lambda}{32}Q^2$ (PROVED; a DIAGNOSTIC of the
      functional; there is no correlation energy in either).
    - The eight zero modes have $S = 0$ and $Q = n$; their proper density is largest
      at the tip ($n_{\max} = 82.22$); this fixes the Revision couplings
      $\lambda_1 = 0.01946$, $\lambda_2 = 0.05838$ for $N = 8$; and their exact Fock
      exchange vanishes, so their exact-Fock energy is exactly zero (the record's
      self-consistent values are zero to rounding).
    - ASSUMED: the Z2 doubled system (the weight $w = \frac12$) and the good sector.
    """),
]

if __name__ == "__main__":
    raise SystemExit(run_builder(__file__))
