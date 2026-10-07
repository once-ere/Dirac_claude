#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
"""Builder of Notebook 10g, "The quantum reading of the pairing: one system or two
universes" (textbook "Universes in Pairs", chapter 10: canonical quantisation in 4+4,
the Krein space and the good sector).

The notebook Revision/textbook/notebooks/10g_quantum_pair_reading.ipynb is BUILT from
this file by Revision/textbook/tools/nbkit.py (never edit the .ipynb by hand):

    python Revision/textbook/tools/nbkit.py build \
        Revision/textbook/notebooks/src/10g_quantum_pair_reading.py --date YYYY-MM-DD
    python Revision/textbook/tools/nbkit.py check \
        Revision/textbook/notebooks/src/10g_quantum_pair_reading.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools"))
from nbkit import code, md, run_builder  # noqa: E402

FACTS = {
    "id": "10g",
    "name": "10g_quantum_pair_reading",
    "title": "The quantum reading of the pairing: one system or two universes",
    "purpose": (
        "It checks, exactly with sympy and on explicit fermionic Fock spaces, the "
        "quantum reading Q of the Revision pairing record: the Lagrangian identity "
        "L_m of Gamma chi equals minus L_-m of chi, the time-derivative kernels of the "
        "three Lagrangians involved (the field, its chirality image, an independent "
        "universe of mass -m), the canonical anticommutators they force (+B, -B, +B), "
        "that the chirality image Gamma Psi carries the Krein metric -B and the mirror "
        "image keeps +B, that the energy and the charge of the field are minus those "
        "that the mass -m theory assigns to its image (one quantum system, T to -T and "
        "J to -J as operator identities), that two independently quantised universes "
        "of masses +m and -m have the anticommutator +B each, anticommute with each "
        "other and cannot be identified with the image, and that their generators add "
        "without cancelling (block eigenvalues +m and -m, 16 each; one good-sector "
        "momentum: every state of the product Fock space has a non-negative total "
        "energy, a pair of zero total charge has energy 2E); five teaching figures."
    ),
    "records": [
        ["Revision/algebra/gammas.json", "the author's gamma matrices (read)"],
        ["Revision/pairing/pairing-theory.json",
         "the theorem entry Q, quantum-level reading, with its hypotheses and its five "
         "statements (read)"],
        ["Revision/pairing/reports/python-pairing.json",
         "checks Q.image_krein_metric, Q.image_own_quantisation, "
         "Q.image_generators_same_dynamics, Q.no_cancellation_independent_universes "
         "and Q.T2_image_keeps_B (reproduced)"],
        ["Revision/pairing/reports/wolfram-pairing.json",
         "checks Q_Krein_metric_of_images, Q_symplectic_kernel_grassmann, "
         "Q_generators_of_the_image_grassmann and "
         "Q_no_identification_of_independent_universes (reproduced)"],
        ["Revision/lead_checks/reports/charge-conjugation-and-u1.json",
         "check quantum_charge_conjugation_unitary_type (reproduced)"],
        ["Revision/theory/reports/python-field-theory.json",
         "check good_sector_positive_fock_realisation (reproduced in both universes)"],
    ],
    "packages": ["numpy", "sympy", "matplotlib"],
    "needs_rust": [],
    "expected_seconds": 15,
    "timeout_seconds": 300,
    "files_written": [
        "Revision/textbook/figures/10g.captions.json",
        "Revision/textbook/figures/10g_1_krein_metrics.png",
        "Revision/textbook/figures/10g_2_one_system.png",
        "Revision/textbook/figures/10g_3_anticommutator_blocks.png",
        "Revision/textbook/figures/10g_4_block_generator.png",
        "Revision/textbook/figures/10g_5_two_universe_states.png",
    ],
    "final_lines": [
        "PASS the figure file 10g_5_two_universe_states.png exists",
        "ALL 25 CHECKS PASSED (notebook 10g)",
    ],
    "troubleshooting": [
        ["\"FileNotFoundError\" for gammas.json or pairing-theory.json",
         "the notebook reads two files of the repository; it must be opened inside the "
         "folder Revision/textbook/notebooks of a complete copy of the repository. Clone "
         "the repository again and open the notebook there."],
    ],
}

CELLS = [
    md(r"""
    ## 1. What this notebook computes

    The pairing theorem T1 of the Revision record says that the chirality matrix
    $\Gamma = \gamma^{(x_8)}\gamma^{(x_1)}\cdots\gamma^{(x_7)}$ turns every solution
    $\Psi$ of the field of mass $m$ (and coupling $\lambda$) into a solution
    $\Gamma\Psi$ of the field of mass $-m$ (and coupling $-\lambda$), with the
    energy-momentum tensor and the current reversed: $T \to -T$, $J \to -J$. What
    does this mean once dirac16complex is QUANTISED? The Revision pairing record
    answers with five statements, the *quantum reading* Q. This notebook checks the
    four of them that concern the canonical anticommutator, exactly with sympy and on
    explicit fermionic Fock spaces (the fifth, about one-particle spectra, is the
    subject of the first notebook of this chapter). It

    - proves the Lagrangian identity $\mathcal{L}_m[\Gamma\chi] = -\mathcal{L}_{-m}[\chi]$
      for symbolic field components, and computes the time-derivative kernels of three
      Lagrangians: that of the field $\Psi$, that of its chirality image $\chi =
      \Gamma\Psi$ (the same system written in new variables) and that of an
      independent universe of mass $-m$; they force the canonical anticommutators
      $+B$, $-B$ and $+B$;
    - checks on a Fock space that the image $\Gamma\Psi$ carries the Krein metric $-B$,
      while the mirror image $\gamma^{(x_8)}\Psi$ of theorem T2 keeps $+B$;
    - checks that the energy and the charge of the field are MINUS the energy and the
      charge that the mass $-m$ theory assigns to the image: $T \to -T$ and $J \to -J$
      hold as identities between operators of ONE quantum system;
    - builds two independently quantised universes of masses $+m$ and $-m$ on one Fock
      space and checks that each has the anticommutator $+B$, that they anticommute
      with each other, and that the image $\Gamma\Psi$ cannot be one of them;
    - shows that their energies ADD and never cancel: the block generator has the
      eigenvalues $+m$ and $-m$ (16 each, none zero), and for one good-sector momentum
      every state of the two universes has a total energy of at least 0, while a pair
      of total charge 0 has the energy $2E$, not 0;
    - reproduces the corresponding checks of the Revision record and draws five
      teaching figures.

    Nothing here describes the CREATION of a universe or of a pair: the statements are
    about how the canonical rule treats a solution, its image and a second universe.
    """),
    md(r"""
    ## 3. The words used in this notebook

    - **Chirality image**: for a field $\Psi$, the field $\chi = \Gamma\Psi$. Because
      $\Gamma^2 = I_{16}$, also $\Psi = \Gamma\chi$: the image carries exactly the
      same information, written in other variables.
    - **Mirror image**: the field $\gamma^{(x_8)}\Psi$ (with the hidden direction
      reflected) of the pairing theorem T2.
    - **Lagrangian $\mathcal{L}_m[\Psi]$**: the Lagrangian density of dirac16complex
      with mass $m$, evaluated on the field $\Psi$. Here (flat 4+4 space, $U = 0$) it is
      $\frac12\sum_a(\Psi^\dagger C\gamma^{(x_a)}\partial_a\Psi -
      \partial_a\Psi^\dagger C\gamma^{(x_a)}\Psi) - m\Psi^\dagger C\Psi$.
    - **Time-derivative kernel** $N$: the matrix in the terms of a Lagrangian that
      contain $\partial_4$, written as $\frac{i}{2}(\Psi^\dagger N\partial_4\Psi -
      \partial_4\Psi^\dagger N\Psi)$. Canonical quantisation turns it into the
      anticommutator $\{\Psi_A, \Psi^\dagger_C\} = (N^{-1})_{AC}$ (at one point; derived
      in the second notebook of this chapter).
    - **Anticommutator matrix**: for two lists of operators $X_1, \dots, X_n$ and
      $Y_1, \dots, Y_n$ whose anticommutators are numbers, the matrix with entries
      $\{X_i, Y_j\}$.
    - **Independent universes**: two quantum fields $\Psi_1, \Psi_2$ on one state
      space with $\{\Psi_{1A}, \Psi_{2C}^\dagger\} = 0$ and $\{\Psi_{1A}, \Psi_{2C}\} = 0$:
      nothing done to one changes the anticommutation rules of the other.
    - **Product Fock space**: the Fock space of the modes of both universes together,
      here $16 + 16 = 32$ fermion modes ($2^{32}$ occupation patterns).
    - **Generator**: the operator (or, for one particle, the matrix) that moves a
      system in time; the energy is the generator of time translations.
    - **Rank** of a matrix: the number of independent columns; a matrix of rank 16 out
      of 16 has no column that is a combination of the others, in particular it is not 0.
    - **Normal-ordered energy**: the energy of a state minus the energy of the vacuum
      (the filled sea), as in the third notebook of this chapter.
    - **Status words**: PROVED (exact, for all values), CHECKED (exact or to rounding,
      for the values shown), REPRODUCED (agrees with a Revision record), NOT
      ESTABLISHED (not shown by these equations).
    """),
    md(r"""
    ## 4. The physical and mathematical situation

    Everything is at one point with frozen coefficients (flat 4+4 space), $U = 0$, and
    with the conventions of the earlier notebooks of this chapter: $C =
    \gamma^{(x_8)}\gamma^{(x_1)}\gamma^{(x_2)}\gamma^{(x_3)}$, $B = -iC\gamma^{(x_4)}$,
    $\Gamma = \gamma^{(x_8)}\gamma^{(x_1)}\cdots\gamma^{(x_7)} = \mathrm{diag}(-I_8,
    I_8)$, real, symmetric, $\Gamma^2 = I_{16}$.

    **Two sign rules.** $\Gamma$ anticommutes with every gamma. Moving $\Gamma$ through
    a product of $n$ gammas therefore costs the sign $(-1)^n$:

    $$\Gamma C\Gamma = C\ (n = 4),\qquad \Gamma C\gamma^{(x_a)}\Gamma = -C\gamma^{(x_a)}\
    (n = 5),\qquad \Gamma B\Gamma = -B\ (n = 5).$$

    The mirror matrix $\gamma^{(x_8)}$ commutes with itself and anticommutes with the
    four other gammas in $B = -i\gamma^{(x_8)}\gamma^{(x_1)}\gamma^{(x_2)}\gamma^{(x_3)}
    \gamma^{(x_4)}$, so $\gamma^{(x_8)}B\gamma^{(x_8)} = (-1)^4B = +B$.

    **The Lagrangian identity, line by line.** Insert $\Psi = \Gamma\chi$ (and
    $\Psi^\dagger = \chi^\dagger\Gamma$, because $\Gamma$ is real and symmetric) into
    $\mathcal{L}_m$:

    $$\mathcal{L}_m[\Gamma\chi] = \tfrac12\sum_a(\chi^\dagger\Gamma C\gamma^{(x_a)}
    \Gamma\partial_a\chi - \partial_a\chi^\dagger\Gamma C\gamma^{(x_a)}\Gamma\chi) -
    m\chi^\dagger\Gamma C\Gamma\chi .$$

    Use the two sign rules:

    $$\mathcal{L}_m[\Gamma\chi] = -\tfrac12\sum_a(\chi^\dagger C\gamma^{(x_a)}
    \partial_a\chi - \partial_a\chi^\dagger C\gamma^{(x_a)}\chi) - m\chi^\dagger C\chi .$$

    Take the sign $-1$ out of both terms; the mass term becomes $+m\chi^\dagger C\chi =
    -(-m)\chi^\dagger C\chi$, so the bracket is the Lagrangian with mass $-m$:

    $$\mathcal{L}_m[\Gamma\chi] = -\mathcal{L}_{-m}[\chi] .$$

    **Three kernels.** In $\mathcal{L}_m[\Psi]$ the $\partial_4$ terms are
    $\frac12(\Psi^\dagger C\gamma^{(x_4)}\partial_4\Psi - \ldots)$, and $C\gamma^{(x_4)} =
    iB$, so $N = B$ and $\{\Psi, \Psi^\dagger\} = B^{-1} = B$. The SAME system written
    in the variable $\chi$ has the Lagrangian $\mathcal{L}_m[\Gamma\chi] =
    -\mathcal{L}_{-m}[\chi]$, whose kernel is $\Gamma B\Gamma = -B$: canonical
    quantisation of the image gives $\{\chi, \chi^\dagger\} = -B$, which agrees with
    the map, $\{\Gamma\Psi, (\Gamma\Psi)^\dagger\} = \Gamma B\Gamma = -B$. An
    INDEPENDENT universe of mass $-m$ has its own Lagrangian $\mathcal{L}_{-m}[\Psi_2]$
    with kernel $+B$ (the mass does not enter the kernel), hence $\{\Psi_2,
    \Psi_2^\dagger\} = +B$. Since $B \neq -B$, the image of universe 1 cannot be such
    a universe.

    **Energy and charge.** For one plane wave with momenta $k_a$ ($a \neq 4$) the energy
    of the field is $H = \Psi^\dagger h'_m\Psi$ with $h'_m = mC - i\sum_a k_aC
    \gamma^{(x_a)}$ (second notebook of this chapter), and its charge is $Q =
    \Psi^\dagger B\Psi$. Written in the image variable:

    $$H = \chi^\dagger\Gamma h'_m\Gamma\chi = \chi^\dagger(mC + i\textstyle\sum_a k_aC
    \gamma^{(x_a)})\chi = -\chi^\dagger h'_{-m}\chi,\qquad Q = \chi^\dagger\Gamma B
    \Gamma\chi = -\chi^\dagger B\chi .$$

    So the energy and the charge of the field are MINUS the energy and the charge that
    the mass $-m$ theory assigns to the image: this is $T \to -T$, $J \to -J$ of T1 as
    an identity between operators of one system. The image is not a second universe
    with negative energy; it is the first universe described in other variables.

    **Two independent universes.** On the product Fock space put $\Psi_1$ (mass $m$,
    anticommutator $+B$) and $\Psi_2$ (mass $-m$, anticommutator $+B$) with
    $\{\Psi_1, \Psi_2^\dagger\} = 0$. The total energy is $H_1 + H_2$, and its
    one-particle generator is the block matrix $\mathrm{diag}(Bh'_m, Bh'_{-m})$. At
    zero momentum $Bh'_{\pm m} = \pm mBC$; since $(BC)^2 = -C\gamma^{(x_4)}CC
    \gamma^{(x_4)}C = I_{16}$ and $\mathrm{tr}(BC) = 0$, the matrix $BC$ has the
    eigenvalues $+1$ and $-1$, eight each, and the block generator has the eigenvalues
    $+m$ and $-m$, sixteen each: none is 0 for $m \neq 0$. After normal ordering each
    universe has quanta of energy $+E > 0$ (third notebook of this chapter), so the
    total energy of every state is at least 0, and equals 0 only in the vacuum. A
    particle in universe 1 (charge $+1$) and an antiparticle in universe 2 (charge
    $-1$) have the total charge 0 but the total energy $2E$.
    """),
    md(r"""
    ## 5. The matrices and the statements of the record

    The next cell reads the author's gamma matrices, builds $C$, $\Gamma$ and $B$ (exact
    whole numbers and the imaginary unit `1j`), checks the sign rules of Section 4, and
    reads the theorem entry Q of the Revision pairing record
    `Revision/pairing/pairing-theory.json`: its hypothesis and its five statements.

    It also defines `check_record(condition, name, record)`: it does what
    `check(condition, name, record=record)` of the set-up cell does, but prints the PASS
    line and the line naming the reproduced Revision record in one piece (Jupyter
    sends printed text to the screen in pieces whose boundaries depend on timing;
    printing them in one piece keeps the stored output the same in every run).
    """),
    code(r'''
    import contextlib  # lets a block of code print into a text buffer
    import io  # the text buffer
    import sys  # the screen output, sys.stdout
    from math import comb  # comb(8, j): the number of ways to choose j of 8 things

    import numpy as np  # numbers, arrays and matrices
    import sympy as sp  # exact algebra with symbols
    from matplotlib.colors import LinearSegmentedColormap  # colour scales


    def check_record(condition, name, record):
        """check(condition, name, record=record), printed in one piece."""
        buffer = io.StringIO()
        with contextlib.redirect_stdout(buffer):  # what check prints goes to buffer
            check(condition, name, record=record)
        sys.stdout.write(buffer.getvalue())  # one single piece of output


    BLUE, ORANGE, GREEN, GREY = "#2a78d6", "#eb6834", "#1baf7a", "#52514e"
    DIVERGING = LinearSegmentedColormap.from_list(
        "blue_grey_red", ["#184f95", "#f0efec", "#e34948"])  # -1 blue, 0 grey, +1 red

    fixture = json.loads(repository_file("Revision/algebra/gammas.json").read_text(
        encoding="utf-8"))
    # gamma[a] is the matrix gamma^(x_a) of the coordinate x_a, a = 1, ..., 8.
    gamma = {a: np.array(fixture["gamma"][a - 1], dtype=int) for a in range(1, 9)}
    C = gamma[8] @ gamma[1] @ gamma[2] @ gamma[3]  # the author's sigma16
    Gamma = (gamma[8] @ gamma[1] @ gamma[2] @ gamma[3] @ gamma[4] @ gamma[5]
             @ gamma[6] @ gamma[7])  # the chirality matrix
    B = -1j * (C @ gamma[4])  # B = -i C gamma^(x4)
    I16 = np.eye(16)
    diagonal = np.array([-1] * 8 + [1] * 8)  # the expected diagonal of Gamma
    sign_rules = (np.array_equal(Gamma, np.diag(diagonal))
                  and np.array_equal(Gamma @ C @ Gamma, C)
                  and all(np.array_equal(Gamma @ C @ gamma[a] @ Gamma, -C @ gamma[a])
                          for a in range(1, 9)))
    check(sign_rules, "Gamma = diag(-I8, I8), Gamma C Gamma = C, Gamma C g^a Gamma = -C g^a")

    pairing = json.loads(repository_file("Revision/pairing/pairing-theory.json")
                         .read_text(encoding="utf-8"))
    theorem_Q = next(t for t in pairing["theorems"] if t["id"] == "Q")
    say(f"record entry Q: {theorem_Q['name']}; {len(theorem_Q['hypotheses'])} "
        f"hypothesis, {len(theorem_Q['statement'])} statements")
    for number, statement in enumerate(theorem_Q["statement"], 1):
        say(f"Q{number}: {statement[:70]} ...")  # the first 70 characters of each
    check(len(theorem_Q["statement"]) == 5, "the record states five quantum statements")
    '''),
    md(r"""
    The next cell computes the Krein metrics carried by the two images,
    $\Gamma B\Gamma^\dagger$ and $\gamma^{(x_8)}B(\gamma^{(x_8)})^\dagger$, compares
    them with $-B$ and $+B$, and draws the three matrices $B$, $\Gamma B\Gamma^\dagger$
    and $\gamma^{(x_8)}B(\gamma^{(x_8)})^\dagger$ as heat maps. All three are purely
    imaginary, so their imaginary parts are drawn (blue $-1$, light grey 0, red $+1$).
    """),
    code(r'''
    image_metric = Gamma @ B @ Gamma.conj().T  # Gamma B Gamma^dagger
    mirror_metric = gamma[8] @ B @ gamma[8].conj().T  # gamma8 B gamma8^dagger
    signature = np.round(np.linalg.eigvalsh(image_metric)).astype(int)
    report("eigenvalues -1 and +1 of Gamma B Gamma^dagger",
           f"{int(np.sum(signature == -1))} and {int(np.sum(signature == 1))}")
    check_record(np.array_equal(image_metric, -B)
                 and sorted(signature.tolist()) == [-1] * 8 + [1] * 8,
                 "the chirality image Gamma Psi carries the Krein metric -B, signature (8,8)",
                 record="Revision/pairing/reports/python-pairing.json, check "
                        "Q.image_krein_metric")
    check_record(np.array_equal(mirror_metric, B),
                 "the mirror image gamma^(x8) Psi keeps the Krein metric +B",
                 record="Revision/pairing/reports/python-pairing.json, check "
                        "Q.T2_image_keeps_B")
    check_record(np.array_equal(image_metric, -B) and np.array_equal(mirror_metric, B),
                 "Krein signs: Gamma gives -1, gamma^(x8) gives +1",
                 record="Revision/pairing/reports/wolfram-pairing.json, check "
                        "Q_Krein_metric_of_images")


    def draw_matrix(ax, matrix, title):
        """Draw a real matrix as a heat map with rows and columns numbered from 1."""
        image = ax.imshow(matrix, cmap=DIVERGING, vmin=-1.0, vmax=1.0)
        size = matrix.shape[0]
        step = 3 if size <= 16 else 4  # label every third (or fourth) row and column
        ticks = list(range(0, size, step))
        ax.set_xticks(ticks, [str(t + 1) for t in ticks])
        ax.set_yticks(ticks, [str(t + 1) for t in ticks])
        ax.grid(False)  # no grid lines on top of the squares
        ax.set_title(title)
        return image


    fig, axes = plt.subplots(1, 3, figsize=(12.0, 4.2))
    draw_matrix(axes[0], B.imag, "field $\\Psi$: $B$")
    draw_matrix(axes[1], image_metric.imag,
                "image $\\Gamma\\Psi$: $\\Gamma B\\Gamma^\\dagger = -B$")
    image = draw_matrix(axes[2], mirror_metric.imag,
                        "mirror $\\gamma^{(x_8)}\\Psi$: $+B$")
    fig.colorbar(image, ax=list(axes), shrink=0.8, label="imaginary part of the entry")
    save_figure(fig, "krein_metrics",
                "The Krein metrics, that is the matrices of the canonical anticommutator, "
                "carried by the field $\\Psi$ (left: $B = -iC\\gamma^{(x_4)}$), by its "
                "chirality image $\\Gamma\\Psi$ (middle: $\\Gamma B\\Gamma^\\dagger$) "
                "and by its mirror image $\\gamma^{(x_8)}\\Psi$ (right: $\\gamma^{(x_8)}"
                "B\\gamma^{(x_8)\\dagger}$), drawn as heat maps of their imaginary parts "
                "(the real parts are zero). Horizontal axis: column number, vertical "
                "axis: row number; red is $+1$, blue is $-1$, light grey is 0. The "
                "middle picture is the left one with every colour exchanged: the "
                "chirality image carries $-B$. The right picture equals the left one: "
                "the mirror image keeps $+B$.")
    '''),
    md(r"""
    ## 6. The Lagrangian identity and the three kernels, exactly

    The next cell writes the Lagrangian $\mathcal{L}_m$ of Section 3 with SYMBOLS for the
    16 components of a field and their derivatives along the eight directions, and for
    the complex conjugates of all of them (sympy treats a symbol and its conjugate as
    independent letters, which is exactly how the Lagrangian uses them). The function
    `lagrangian(mass, M)` evaluates $\mathcal{L}_{\mathrm{mass}}$ on the field $M\chi$
    for a constant matrix $M$, where $\chi$ is the column of symbols. Then the cell

    - checks $\mathcal{L}_m[\Gamma\chi] + \mathcal{L}_{-m}[\chi] = 0$ for every value of
      the 16 components and their 128 derivatives (T1 for flat space, the Lagrangian
      level);
    - reads off the kernel $N$ of each Lagrangian: the coefficient of
      $\chi_A^*\,\partial_4\chi_C$ is $\frac{i}{2}N_{AC}$, so $N_{AC}$ is $-2i$ times
      that coefficient;
    - checks $N = B$ for $\mathcal{L}_m[\chi]$, $N = -B$ for the image Lagrangian
      $\mathcal{L}_m[\Gamma\chi]$, $N = +B$ for an independent universe
      $\mathcal{L}_{-m}[\chi]$, and the anticommutators $N^{-1} = B, -B, B$.
    """),
    code(r'''
    g = {a: sp.Matrix(fixture["gamma"][a - 1]) for a in range(1, 9)}  # exact gammas
    C_exact = g[8] * g[1] * g[2] * g[3]
    Gamma_exact = sp.Matrix(np.diag(diagonal))  # diag(-I8, I8)
    B_exact = -sp.I * C_exact * g[4]
    m = sp.Symbol("m", real=True)  # the mass: any real number
    field = sp.Matrix(sp.symbols("c1:17"))  # chi_A, A = 1, ..., 16
    field_conj = sp.Matrix(sp.symbols("cc1:17"))  # their complex conjugates chi_A^*
    # d[a] and d_conj[a]: the derivatives of chi and of chi^* along x_a
    d = {a: sp.Matrix(sp.symbols(f"d{a}c1:17")) for a in range(1, 9)}
    d_conj = {a: sp.Matrix(sp.symbols(f"d{a}cc1:17")) for a in range(1, 9)}


    def lagrangian(mass, M):
        """L_mass evaluated on the field M chi (M a constant real matrix)."""
        psi, psi_conj = M * field, M * field_conj  # M is real: (M chi)^* = M chi^*
        total = sp.Integer(0)
        for a in range(1, 9):
            kinetic = C_exact * g[a]  # the matrix C gamma^(x_a)
            dpsi, dpsi_conj = M * d[a], M * d_conj[a]
            total += sp.Rational(1, 2) * ((psi_conj.T * kinetic * dpsi)[0]
                                          - (dpsi_conj.T * kinetic * psi)[0])
        total -= mass * (psi_conj.T * C_exact * psi)[0]
        return sp.expand(total)


    def kernel(expression):
        """N_AC = -2 i times the coefficient of chi_A^* d4 chi_C."""
        return sp.Matrix(16, 16, lambda A, C_: -2 * sp.I * expression.coeff(
            field_conj[A] * d[4][C_]))


    L_field = lagrangian(m, sp.eye(16))  # L_m[chi]
    L_image = lagrangian(m, Gamma_exact)  # L_m[Gamma chi]: the same system, new variables
    L_independent = lagrangian(-m, sp.eye(16))  # L_-m[chi]: an independent universe
    say(f"number of terms of L_m[chi]: {len(L_field.args)}")
    identity_ok = sp.expand(L_image + L_independent) == 0
    check(identity_ok, "exact: L_m[Gamma chi] = -L_-m[chi] for all components and "
                       "derivatives")
    N_field, N_image, N_independent = map(kernel, (L_field, L_image, L_independent))
    kernels_ok = (N_field == B_exact and N_image == -B_exact
                  and N_independent == B_exact)
    say(f"kernels equal to B: field {N_field == B_exact}, image {N_image == B_exact}, "
        f"independent universe {N_independent == B_exact}; image kernel = -B: "
        f"{N_image == -B_exact}")
    check_record(kernels_ok,
                 "kernels: N = B (field), N = -B (image), N = +B (independent universe)",
                 record="Revision/pairing/reports/wolfram-pairing.json, check "
                        "Q_symplectic_kernel_grassmann")
    anticommutators = [N.inv() for N in (N_field, N_image, N_independent)]
    check_record(anticommutators[0] == B_exact and anticommutators[1] == -B_exact
                 and anticommutators[2] == B_exact,
                 "canonical rules N^(-1): {Psi,Psi^dag} = B, {chi,chi^dag} = -B, +B",
                 record="Revision/pairing/reports/python-pairing.json, check "
                        "Q.image_own_quantisation")
    '''),
    md(r"""
    ## 7. The field and its two images on a Fock space

    The next cell builds the fermionic Fock space of the second notebook of this
    chapter, here for any number of modes: a state is a dictionary `{pattern:
    amplitude}`, a pattern is a whole number whose binary digit $p$ is the occupation of
    mode $p$, `annihilate(p, state)` is $f_p$ and `create(p, state)` is $f_p^*$ (with
    the sign $(-1)^{\text{(occupied modes below } p)}$ that makes different modes
    anticommute). The field of one universe uses the 16 modes starting at the number
    `offset`: $\Psi_A = f_{A - 1 + \mathrm{offset}}$, with the canonical conjugate
    $\Psi^\dagger_A = \sum_C f^*_{C - 1 + \mathrm{offset}}B_{CA}$ (the positive
    realisation, so that $\{\Psi_A, \Psi^\dagger_C\} = B_{AC}$).

    For a matrix $M$ the image field is $(M\Psi)_A = \sum_D M_{AD}\Psi_D$ and its
    conjugate $((M\Psi)^\dagger)_A = \sum_D \Psi^\dagger_D M^*_{AD}$. The function
    `anticommutator_matrix(X, Y, state)` returns the matrix with entries
    $\langle\phi|\{X_i, Y_j\}|\phi\rangle$ for a normalised state $\phi$; when the
    anticommutators are numbers (as here), these entries ARE those numbers. The cell
    computes it for the image $\Gamma\Psi$ and for the mirror image
    $\gamma^{(x_8)}\Psi$.
    """),
    code(r'''
    def sign_below(n, p):
        """(-1) to the power of the number of occupied modes below mode p in pattern n."""
        return -1 if bin(n & ((1 << p) - 1)).count("1") % 2 else 1


    def annihilate(p, state):
        """f_p applied to a state {pattern: amplitude}."""
        result = {}
        for n, amplitude in state.items():
            if n >> p & 1:  # mode p is occupied in the pattern n
                new = n ^ (1 << p)  # the same pattern with mode p emptied
                result[new] = result.get(new, 0) + sign_below(n, p) * amplitude
        return result


    def create(p, state):
        """f_p^* (the Hilbert adjoint of f_p) applied to a state."""
        result = {}
        for n, amplitude in state.items():
            if not n >> p & 1:  # mode p is empty in the pattern n
                new = n | (1 << p)  # the same pattern with mode p filled
                result[new] = result.get(new, 0) + sign_below(n, p) * amplitude
        return result


    def add(*terms):
        """The state sum of coefficient * state over the pairs (coefficient, state)."""
        result = {}
        for coefficient, state in terms:
            for n, amplitude in state.items():
                result[n] = result.get(n, 0) + coefficient * amplitude
        return result


    def inner(left, right):
        """The positive inner product <left|right>."""
        return sum(np.conj(a) * right.get(n, 0) for n, a in left.items())


    def largest(state):
        """The largest size of an amplitude of the state (0 for the zero state)."""
        return max((abs(a) for a in state.values()), default=0.0)


    rng = np.random.default_rng(12345)  # random numbers with a fixed seed


    def random_state(patterns, modes):
        """A normalised superposition of a few random patterns of the given modes."""
        state = {}
        for n in rng.integers(0, 2 ** modes, size=patterns):
            state[int(n)] = complex(rng.normal(), rng.normal())
        length = np.sqrt(inner(state, state).real)
        return {n: a / length for n, a in state.items()}


    def field_op(offset):
        """The operators Psi_A (A = 1..16) of the universe whose modes start at offset."""
        return [lambda s, A=A: annihilate(A - 1 + offset, s) for A in range(1, 17)]


    def conjugate_op(offset):
        """Psi^dagger_A = sum_C f^*_(C-1+offset) B_CA (the canonical conjugate)."""
        return [lambda s, A=A: add(*[(B[C_ - 1, A - 1], create(C_ - 1 + offset, s))
                                     for C_ in range(1, 17) if B[C_ - 1, A - 1] != 0])
                for A in range(1, 17)]


    def mapped(M, ops):
        """The operators (M X)_A = sum_D M_AD X_D for a list X of 16 operators."""
        return [lambda s, A=A: add(*[(M[A - 1, D - 1], ops[D - 1](s))
                                     for D in range(1, 17) if M[A - 1, D - 1] != 0])
                for A in range(1, 17)]


    def mapped_conjugate(M, conj_ops):
        """((M Psi)^dagger)_A = sum_D Psi^dagger_D conj(M_AD)."""
        return mapped(M.conj(), conj_ops)


    def anticommutator_matrix(X, Y, state):
        """The matrix <state| {X_i, Y_j} |state> for two lists of operators."""
        result = np.zeros((len(X), len(Y)), dtype=complex)
        for i, x in enumerate(X):
            for j, y in enumerate(Y):
                both = add((1, x(y(state))), (1, y(x(state))))
                result[i, j] = inner(state, both)
        return result


    Psi, Psi_dagger = field_op(0), conjugate_op(0)  # one universe: modes 0, ..., 15
    phi = random_state(6, 16)
    own = anticommutator_matrix(Psi, Psi_dagger, phi)
    image = anticommutator_matrix(mapped(Gamma, Psi),
                                  mapped_conjugate(Gamma, Psi_dagger), phi)
    mirror = anticommutator_matrix(mapped(gamma[8], Psi),
                                   mapped_conjugate(gamma[8], Psi_dagger), phi)
    errors = [np.max(np.abs(own - B)), np.max(np.abs(image + B)),
              np.max(np.abs(mirror - B))]
    report("largest deviations from B, -B and +B", ", ".join(f"{e:.1e}" for e in errors))
    check(max(errors) < 1e-12,
          "Fock space: {Psi, Psi^dag} = B, image -B, mirror +B (256 entries each)")
    '''),
    md(r"""
    ## 8. One quantum system: $T \to -T$ and $J \to -J$ as operator identities

    The next cell takes a mass and a plane wave with momenta along all seven slice
    directions (also along the extra times) and builds, on the Fock space, four
    operators of the form $X^\dagger NX = \sum_{A,C}X^\dagger_AN_{AC}X_C$:

    - the energy of the field, $H_m[\Psi] = \Psi^\dagger h'_m\Psi$, and the energy that
      the mass $-m$ theory assigns to the image, $H_{-m}[\Gamma\Psi] =
      (\Gamma\Psi)^\dagger h'_{-m}(\Gamma\Psi)$;
    - the charge of the field, $Q[\Psi] = \Psi^\dagger B\Psi$, and the charge the
      theory assigns to the image, $Q[\Gamma\Psi] = (\Gamma\Psi)^\dagger B(\Gamma\Psi)$.

    It checks $H_m[\Psi] = -H_{-m}[\Gamma\Psi]$ and $Q[\Psi] = -Q[\Gamma\Psi]$ by
    applying both sides to 150 random states, and records the expectation values for
    the figure. Then it checks the quantum equation of motion of the image: with the
    energy $H = H_m[\Psi]$ of the system, $[H, (\Gamma\Psi)_c] = -(h_{-m}\Gamma\Psi)_c$
    with the mode Hamiltonian $h_{-m} = Bh'_{-m}$, so $i\,\partial_4(\Gamma\Psi) =
    h_{-m}\Gamma\Psi$: the image obeys the wave equation of mass $-m$, moved by the
    SAME energy operator.
    """),
    code(r'''
    m_value = 1.3  # any mass and momenta (here with momenta along the extra times too)
    k = {1: 0.4, 2: -0.7, 3: 0.2, 5: 0.9, 6: -0.3, 7: 0.5, 8: 1.1}


    def h_prime(mass):
        """The energy matrix h'_mass = mass C - i sum_a k_a C gamma^(x_a) of the wave."""
        return mass * C - 1j * sum(k_a * (C @ gamma[a]) for a, k_a in k.items())


    def bilinear(X_dagger, N, X, state):
        """sum_(A,C) X^dagger_A N_AC X_C applied to a state."""
        terms = []
        for C_ in range(16):
            lowered = X[C_](state)
            if lowered:
                terms += [(N[A, C_], X_dagger[A](lowered)) for A in range(16)
                          if N[A, C_] != 0]
        return add(*terms)


    image_field = mapped(Gamma, Psi)  # Gamma Psi
    image_conjugate = mapped_conjugate(Gamma, Psi_dagger)  # (Gamma Psi)^dagger
    worst_H, worst_Q, values = 0.0, 0.0, []
    for _ in range(150):
        state = random_state(4, 16)
        H_field = bilinear(Psi_dagger, h_prime(m_value), Psi, state)
        H_image = bilinear(image_conjugate, h_prime(-m_value), image_field, state)
        Q_field = bilinear(Psi_dagger, B, Psi, state)
        Q_image = bilinear(image_conjugate, B, image_field, state)
        worst_H = max(worst_H, largest(add((1, H_field), (1, H_image))))
        worst_Q = max(worst_Q, largest(add((1, Q_field), (1, Q_image))))
        values.append([inner(state, X).real for X in (H_field, H_image, Q_field,
                                                       Q_image)])
    values = np.array(values)  # columns: <H_m[Psi]>, <H_-m[Gamma Psi]>, <Q>, <Q image>
    report("largest |(H_m[Psi] + H_-m[Gamma Psi]) phi| over 150 states", f"{worst_H:.1e}")
    report("largest |(Q[Psi] + Q[Gamma Psi]) phi| over 150 states", f"{worst_Q:.1e}")
    check_record(worst_H < 1e-12 and worst_Q < 1e-12,
                 "operators: H_m[Psi] = -H_-m[Gamma Psi] and Q[Psi] = -Q[Gamma Psi]",
                 record="Revision/pairing/reports/wolfram-pairing.json, check "
                        "Q_generators_of_the_image_grassmann")

    h_mode_minus = B @ h_prime(-m_value)  # the mode Hamiltonian of mass -m
    worst = 0.0
    for c_ in range(16):
        H_after = bilinear(Psi_dagger, h_prime(m_value), Psi, image_field[c_](phi))
        H_before = image_field[c_](bilinear(Psi_dagger, h_prime(m_value), Psi, phi))
        commutator = add((1, H_after), (-1, H_before))  # [H, (Gamma Psi)_c] phi
        expected = add(*[(-h_mode_minus[c_, d_], image_field[d_](phi))
                         for d_ in range(16)])
        worst = max(worst, largest(add((1, commutator), (-1, expected))))
    report("largest violation of [H, (Gamma Psi)_c] = -(h_-m Gamma Psi)_c", f"{worst:.1e}")
    check(worst < 1e-12, "the image obeys i d4 (Gamma Psi) = h_-m Gamma Psi under the "
                         "same H")
    '''),
    md(r"""
    The Revision record states the same fact for the one-particle generators, exactly
    and for all momenta: a field of mass $-m$ moves with the generator $Bh'_{-m}$; its
    image under $\Gamma$ carries the metric $-B$ and the energy matrix $-h'_m$, and the
    two signs compensate, $(-B)(-h'_m) = \Gamma(Bh'_{-m})\Gamma = Bh'_m$. The next cell
    checks this with sympy for symbolic $m$ and $k_1, \dots, k_8$, together with
    $\Gamma h'_m\Gamma = -h'_{-m}$, and then draws the expectation values of the
    previous cell.
    """),
    code(r'''
    k_symbol = {a: sp.Symbol(f"k{a}", real=True) for a in (1, 2, 3, 5, 6, 7, 8)}


    def h_prime_exact(mass):
        """The exact energy matrix mass C - i sum_a k_a C gamma^(x_a)."""
        result = mass * C_exact
        for a, k_a in k_symbol.items():
            result = result - sp.I * k_a * C_exact * g[a]
        return result


    zero = sp.zeros(16, 16)
    own_data = (-B_exact) * (-h_prime_exact(m))  # the image: metric -B, energy -h'_m
    by_map = Gamma_exact * (B_exact * h_prime_exact(-m)) * Gamma_exact
    same = ((own_data - by_map).applyfunc(sp.expand) == zero
            and (own_data - B_exact * h_prime_exact(m)).applyfunc(sp.expand) == zero)
    energy_rule = (Gamma_exact * h_prime_exact(m) * Gamma_exact
                   + h_prime_exact(-m)).applyfunc(sp.expand) == zero
    check_record(same and energy_rule,
                 "exact: (-B)(-h'_m) = Gamma (B h'_-m) Gamma = B h'_m; "
                 "Gamma h'_m Gamma = -h'_-m",
                 record="Revision/pairing/reports/python-pairing.json, check "
                        "Q.image_generators_same_dynamics")

    fig, axes = plt.subplots(1, 2, figsize=(11.0, 4.4))
    panels = ((axes[0], 0, 1, BLUE, "energy",
               "$\\langle H_m[\\Psi]\\rangle$", "$\\langle H_{-m}[\\Gamma\\Psi]\\rangle$"),
              (axes[1], 2, 3, ORANGE, "charge",
               "$\\langle Q[\\Psi]\\rangle$", "$\\langle Q[\\Gamma\\Psi]\\rangle$"))
    for ax, x_col, y_col, colour, what, x_label, y_label in panels:
        ax.plot(values[:, x_col], values[:, y_col], "o", color=colour, markersize=4,
                label="150 random states")
        low, high = values[:, x_col].min() - 0.5, values[:, x_col].max() + 0.5
        ax.plot([low, high], [-low, -high], color=GREY, linewidth=1,
                label="the line $y = -x$")
        ax.set_xlabel(f"{what} of the field, {x_label}")
        ax.set_ylabel(f"{what} given to the image, {y_label}")
        ax.legend(fontsize=8)
    axes[0].set_title("$T \\to -T$ inside one system")
    axes[1].set_title("$J \\to -J$ inside one system")
    save_figure(fig, "one_system",
                "For 150 random states of the Fock space of one field: left, the "
                "expectation value of the energy $H_m[\\Psi] = \\Psi^\\dagger h'_m\\Psi$ "
                "of the field (horizontal axis) against the expectation value of the "
                "energy $H_{-m}[\\Gamma\\Psi]$ that the mass $-m$ theory assigns to the "
                "chirality image (vertical axis), for $m = 1.3$ and a plane wave with "
                "momenta along all seven slice directions; right, the same for the "
                "charges $Q = \\Psi^\\dagger B\\Psi$ and $Q[\\Gamma\\Psi]$. Axes in the "
                "units of $m$ (left) and pure numbers (right). Every point lies on the "
                "grey line $y = -x$: the reversal of the energy and of the charge "
                "under T1 is an identity between operators of ONE quantum system, not "
                "a statement about a second universe.")
    '''),
    md(r"""
    ## 9. Which images could be an independent universe?

    An independently quantised universe of mass $-m$ would be a field $\Psi_2$ with
    $\{\Psi_2, \Psi_2^\dagger\} = +B$ (its own Lagrangian, Section 6) that
    anticommutes with the first field: $\{\Psi_{2A}, \Psi_C^\dagger\} = 0$ and
    $\{\Psi_{2A}, \Psi_C\} = 0$. The next cell tests three candidates built from the
    first field $\Psi$:

    - the chirality image $\Gamma\Psi$ (T1);
    - the mirror image $\gamma^{(x_8)}\Psi$ (T2, here without the reflection of the
      hidden coordinate, which does not change the anticommutators at one point);
    - the conjugate field $\Psi^c = \Gamma\Psi^{\dagger T}$, that is
      $\Psi^c_A = \sum_D\Gamma_{AD}\Psi^\dagger_D$, the conjugation of the quantised
      field that keeps the canonical rule (it reverses the mass; second notebook of
      this chapter).

    For each it computes, on the Fock space, its own anticommutator matrix and the two
    cross matrices with the first field, and their ranks. Independence would need both
    cross matrices to be 0.
    """),
    code(r'''
    conjugate_field = mapped(Gamma, Psi_dagger)  # Psi^c_A = sum_D Gamma_AD Psi^dag_D
    # (Psi^c)^dagger_A = sum_D Gamma_AD Psi_D: Gamma is real and Psi^dagger^dagger = Psi
    # in the positive realisation only up to B, so build it from its definition:
    # Psi^dagger_D = sum_E chi_E B_ED, hence (Psi^dagger_D)^* = sum_E B*_ED Psi_E.
    conjugate_field_dagger = mapped(Gamma @ B.conj().T, Psi)
    candidates = {
        "Gamma Psi": (image_field, image_conjugate),
        "gamma8 Psi": (mapped(gamma[8], Psi), mapped_conjugate(gamma[8], Psi_dagger)),
        "Psi^c = Gamma Psi^dag T": (conjugate_field, conjugate_field_dagger),
    }
    phi = random_state(6, 16)
    results = {}
    for label, (X, X_dagger) in candidates.items():
        metric = anticommutator_matrix(X, X_dagger, phi)  # {X_A, X_C^dagger}
        cross_1 = anticommutator_matrix(X, Psi_dagger, phi)  # {X_A, Psi^dagger_C}
        cross_2 = anticommutator_matrix(X, Psi, phi)  # {X_A, Psi_C}
        sign = (1 if np.allclose(metric, B) else -1 if np.allclose(metric, -B) else 0)
        ranks = (np.linalg.matrix_rank(cross_1), np.linalg.matrix_rank(cross_2))
        results[label] = (sign, ranks, cross_1, cross_2)
        say(f"{label:24s} metric {sign:+d} B; rank of {{X, Psi^dag}} = {ranks[0]:2d}, "
            f"rank of {{X, Psi}} = {ranks[1]:2d}")
    chirality = results["Gamma Psi"]
    conjugate = results["Psi^c = Gamma Psi^dag T"]
    check_record(chirality[0] == -1 and chirality[1] == (16, 0)
                 and np.allclose(chirality[2], Gamma @ B),
                 "Gamma Psi: metric -B and {Gamma Psi, Psi^dag} = Gamma B of rank 16",
                 record="Revision/pairing/reports/wolfram-pairing.json, check "
                        "Q_no_identification_of_independent_universes")
    check_record(conjugate[0] == 1 and conjugate[1] == (0, 16)
                 and np.allclose(conjugate[3], -Gamma @ B),
                 "Psi^c keeps +B (Gamma B^T Gamma^dag = B) but {Psi^c, Psi} = -Gamma B",
                 record="Revision/lead_checks/reports/charge-conjugation-and-u1.json, "
                        "check quantum_charge_conjugation_unitary_type")
    check(results["gamma8 Psi"][0] == 1 and results["gamma8 Psi"][1] == (16, 0),
          "gamma8 Psi keeps +B; as an operator of the same field it is not independent")
    '''),
    md(r"""
    The result in words. The chirality image has the wrong canonical rule ($-B$
    instead of $+B$) AND does not anticommute with the first field (rank 16): it is the
    first universe in other variables. The mirror image and the conjugate field have
    the right rule $+B$, but they too are built from the operators of the first field
    and do not anticommute with it. The rule $+B$ of the mirror image matches the rule
    of an independently quantised mirror universe, so such a universe can be quantised
    as an ordinary copy (statement Q5 of the record); for the chirality image this is
    impossible (statement Q3). A second universe must therefore be a NEW field on a
    larger state space, which the next section builds.

    ## 10. Two independently quantised universes

    The next cell puts universe 1 (mass $+m$) on the modes 0 to 15 and universe 2 (mass
    $-m$) on the modes 16 to 31 of one Fock space, each with its own canonical
    conjugate. It computes the $32 \times 32$ anticommutator matrix of the combined
    list $(\Psi_1, \Psi_2)$ with $(\Psi_1^\dagger, \Psi_2^\dagger)$, which must be
    $\mathrm{diag}(B, B)$, and, for comparison, that of the list $(\Psi_1,
    \Gamma\Psi_1)$ with its conjugates, which must be the block matrix with $B$,
    $B\Gamma$, $\Gamma B$ and $-B$. Then it draws both.
    """),
    code(r'''
    Psi_1, Psi_1_dagger = field_op(0), conjugate_op(0)  # universe 1: modes 0..15
    Psi_2, Psi_2_dagger = field_op(16), conjugate_op(16)  # universe 2: modes 16..31
    phi_32 = random_state(6, 32)
    two_universes = anticommutator_matrix(Psi_1 + Psi_2, Psi_1_dagger + Psi_2_dagger,
                                          phi_32)
    image_pair = anticommutator_matrix(
        Psi_1 + mapped(Gamma, Psi_1),
        Psi_1_dagger + mapped_conjugate(Gamma, Psi_1_dagger), phi_32)
    zero_16 = np.zeros((16, 16))
    expected_two = np.block([[B, zero_16], [zero_16, B]])
    expected_image = np.block([[B, B @ Gamma], [Gamma @ B, -B]])
    cross_zero = np.max(np.abs(anticommutator_matrix(Psi_1, Psi_2, phi_32)))
    report("largest |{Psi_1, Psi_2}| (must be 0)", f"{cross_zero:.1e}")
    check(np.allclose(two_universes, expected_two) and cross_zero < 1e-12
          and np.allclose(image_pair, expected_image),
          "two universes: diag(B, B); field and image: blocks B, B Gamma, Gamma B, -B")

    fig, axes = plt.subplots(1, 2, figsize=(11.0, 5.0))
    draw_matrix(axes[0], two_universes.imag,
                "independent: $(\\Psi_1, \\Psi_2)$")
    image = draw_matrix(axes[1], image_pair.imag,
                        "one field and its image: $(\\Psi_1, \\Gamma\\Psi_1)$")
    for ax in axes:
        ax.axhline(15.5, color=GREY, linewidth=1)  # the border between the two halves
        ax.axvline(15.5, color=GREY, linewidth=1)
    fig.colorbar(image, ax=list(axes), shrink=0.75, label="imaginary part of the entry")
    save_figure(fig, "anticommutator_blocks",
                "The $32 \\times 32$ anticommutator matrices computed on the Fock space "
                "of 32 fermion modes (imaginary parts; the real parts are zero; red "
                "$+1$, blue $-1$, light grey 0; horizontal axis: column, vertical axis: "
                "row; grey lines separate the two halves). Left: two independently "
                "quantised universes $\\Psi_1$ (mass $+m$) and $\\Psi_2$ (mass $-m$): "
                "the diagonal blocks are both $+B$ and the off-diagonal blocks are "
                "empty, the universes anticommute. Right: a field and its chirality "
                "image $\\Gamma\\Psi_1$: the lower right block is $-B$ and the "
                "off-diagonal blocks $B\\Gamma$ and $\\Gamma B$ are full, so the image "
                "is not a second universe but the same one.")
    '''),
    md(r"""
    ## 11. The generators add: no cancellation

    The one-particle generator of the two independent universes is the block matrix
    $\mathrm{diag}(Bh'_m, Bh'_{-m})$. The next cell computes its exact eigenvalues
    with sympy at zero momentum (the record's case: $+m$ and $-m$, 16 times each), and
    then, with numbers, its eigenvalues for $m$ from $-3$ to $3$ at zero momentum and
    at the good-sector momentum $k_1 = 1.5$. In the second case they are
    $\pm\sqrt{m^2 + k_1^2}$ (16 each); in no case is an eigenvalue 0 for $m \neq 0$, so
    the total generator is not zero: the two universes do not cancel each other.
    """),
    code(r'''
    zero_momentum = {k_a: 0 for k_a in k_symbol.values()}
    block = sp.diag((B_exact * h_prime_exact(m)).subs(zero_momentum),
                    (B_exact * h_prime_exact(-m)).subs(zero_momentum))
    block_eigenvalues = block.eigenvals()  # {eigenvalue: how often}
    say(f"exact eigenvalues of diag(B h'_m, B h'_-m) at k = 0: {block_eigenvalues}")
    check_record(block_eigenvalues == {m: 16, -m: 16},
                 "block generator at k = 0: eigenvalues +m and -m, 16 each, none zero",
                 record="Revision/pairing/reports/python-pairing.json, check "
                        "Q.no_cancellation_independent_universes")


    def block_numbers(mass, k1):
        """The 32 eigenvalues of diag(B h'_mass, B h'_-mass) with momentum k1 along x1."""
        def energy(mu):  # the energy matrix of mass mu and momentum k1
            return mu * C - 1j * k1 * (C @ gamma[1])
        top, bottom = B @ energy(mass), B @ energy(-mass)
        values = np.concatenate([np.linalg.eigvals(top), np.linalg.eigvals(bottom)])
        return np.sort(values.real)


    masses = np.linspace(-3.0, 3.0, 121)
    spectra_0 = np.array([block_numbers(x, 0.0) for x in masses])
    spectra_k = np.array([block_numbers(x, 1.5) for x in masses])
    formula_k = np.sqrt(masses ** 2 + 1.5 ** 2)
    error_k = max(np.max(np.abs(spectra_k[:, 16:] - formula_k[:, None])),
                  np.max(np.abs(spectra_k[:, :16] + formula_k[:, None])))
    report("largest deviation from +-sqrt(m^2 + k1^2), 16 each", f"{error_k:.1e}")
    check(error_k < 1e-10 and np.min(np.abs(spectra_k)) >= 1.5 - 1e-10,
          "with k1 = 1.5 the 32 eigenvalues are +-sqrt(m^2 + k1^2): never 0")

    fig, axes = plt.subplots(1, 2, figsize=(11.0, 4.2), sharey=True)
    axes[0].plot(masses, spectra_0[:, [0, 31]], color=BLUE, linewidth=2)
    axes[0].set_title("zero momentum: $+m$ and $-m$, 16 each")
    axes[1].plot(masses, spectra_k[:, [0, 31]], color=GREEN, linewidth=2)
    axes[1].set_title("momentum $k_1 = 1.5$: $\\pm\\sqrt{m^2 + k_1^2}$, 16 each")
    for ax in axes:
        ax.axhline(0.0, color=GREY, linewidth=1)
        ax.set_xlabel("mass $m$ of universe 1 (universe 2 has $-m$)")
    axes[0].set_ylabel("eigenvalues of diag$(Bh'_m, Bh'_{-m})$")
    save_figure(fig, "block_generator",
                "The 32 eigenvalues (vertical axes, units of the momentum and mass) of "
                "the one-particle generator $\\mathrm{diag}(Bh'_m, Bh'_{-m})$ of two "
                "independently quantised universes of masses $+m$ and $-m$, against "
                "$m$ from $-3$ to $3$ (horizontal axes); each line carries 16 "
                "eigenvalues. Left: zero momentum, eigenvalues $+m$ and $-m$, which "
                "vanish only at $m = 0$. Right: the momentum $k_1 = 1.5$, eigenvalues "
                "$\\pm\\sqrt{m^2 + k_1^2}$, never 0. The generators of the two universes "
                "add; nothing in them cancels.")
    '''),
    md(r"""
    ## 12. One good-sector momentum in both universes

    The last computation repeats, for the two universes together, the positive Fock
    construction of the third notebook of this chapter, for the recorded good-sector
    momentum $m = 2$, $k = (1, 2, 0, 4)$ along $(x_1, x_2, x_3, x_8)$, $E = 5$.
    Universe 1 uses the orthonormal eigenvectors $u_s$ ($+E$) and $v_s$ ($-E$) of $h_m$;
    universe 2 uses $\Gamma u_s$ and $\Gamma v_s$, which are eigenvectors of $h_{-m} =
    \Gamma h_m\Gamma$ with the same eigenvalues. In each universe modes 0 to 7 of its
    half are particles and modes 8 to 15 antiparticles (created by $d^*$, so
    $\Psi = \sum_s(u_sb_s + v_sd_s^*)$ and $\Psi^\dagger = \chi B$, with $\chi$ the
    Hilbert adjoint). The cell checks the canonical rule in both universes, the vacuum
    energy $-8E$ of each, that every pattern is an energy and charge eigenstate with
    the normal-ordered total energy $E \times$(number of quanta) and the total charge
    (particles minus antiparticles), on 200 random patterns, and the pair state
    "particle in universe 1, antiparticle in universe 2".
    """),
    code(r'''
    def orthonormal_columns(P):
        """Orthonormal columns that span the range of P (Gram-Schmidt, done twice)."""
        basis = []
        for column in P.T:
            v = column.astype(complex)
            for _ in range(2):  # the second pass removes rounding errors
                for e in basis:
                    v = v - (e.conj() @ v) * e
            length = np.sqrt((v.conj() @ v).real)
            if length > 1e-8:
                basis.append(v / length)
        return np.array(basis).T


    def mode_hamiltonian(mass, momenta):
        """h = -i mass gamma^(x4) - gamma^(x4) sum_a k_a gamma^(x_a)."""
        h = -1j * mass * gamma[4]
        for a, k_a in momenta.items():
            h = h - k_a * (gamma[4] @ gamma[a])
        return h


    sample = {1: 1, 2: 2, 8: 4}  # the recorded good-sector momentum, with m = 2
    h_plus, h_minus = mode_hamiltonian(2, sample), mode_hamiltonian(-2, sample)
    E = 5.0  # sqrt(4 + 1 + 4 + 16)
    W1 = np.hstack([orthonormal_columns((I16 + h_plus / E) / 2),
                    orthonormal_columns((I16 - h_plus / E) / 2)])  # u_1..u_8, v_1..v_8
    W2 = Gamma @ W1  # the eigenvectors of h_-m = Gamma h_m Gamma
    check(np.allclose(h_minus @ W2[:, :8], E * W2[:, :8])
          and np.allclose(h_minus @ W2[:, 8:], -E * W2[:, 8:])
          and np.allclose(W2.conj().T @ W2, I16),
          "Gamma u_s and Gamma v_s are orthonormal eigenvectors of h_-m, energies +-E")


    def universe(W, offset):
        """Psi, chi (Hilbert adjoint) and Psi^dagger = chi B of one universe."""
        def F(p, s):  # b (particle modes) or d^* (antiparticle modes)
            return annihilate(p + offset, s) if p < 8 else create(p + offset, s)

        def F_star(p, s):  # the Hilbert adjoint of F_p
            return create(p + offset, s) if p < 8 else annihilate(p + offset, s)

        psi = [lambda s, A=A: add(*[(W[A, p], F(p, s)) for p in range(16)])
               for A in range(16)]
        chi = [lambda s, A=A: add(*[(np.conj(W[A, p]), F_star(p, s)) for p in range(16)])
               for A in range(16)]
        psi_dagger = mapped(B.T, chi)  # Psi^dagger_A = sum_C chi_C B_CA
        return psi, chi, psi_dagger


    psi_1, chi_1, psi_1_dagger = universe(W1, 0)
    psi_2, chi_2, psi_2_dagger = universe(W2, 16)
    phi_32 = random_state(4, 32)
    rule_1 = anticommutator_matrix(psi_1, psi_1_dagger, phi_32)
    rule_2 = anticommutator_matrix(psi_2, psi_2_dagger, phi_32)
    rule_12 = anticommutator_matrix(psi_1, psi_2_dagger, phi_32)
    check(np.allclose(rule_1, B) and np.allclose(rule_2, B) and np.allclose(rule_12, 0),
          "positive realisation: {Psi_1, Psi_1^dag} = {Psi_2, Psi_2^dag} = B, cross 0")


    def total_energy(state):
        """(H_1 + H_2) state, with H = chi h Psi in each universe."""
        return add((1, bilinear(chi_1, h_plus, psi_1, state)),
                   (1, bilinear(chi_2, h_minus, psi_2, state)))


    def total_charge(state):
        """(Q_1 + Q_2) state, with Q = Psi^dagger B Psi = chi Psi in each universe."""
        return add((1, bilinear(chi_1, I16, psi_1, state)),
                   (1, bilinear(chi_2, I16, psi_2, state)))


    VACUUM = {0: 1.0}
    vacuum_energy = inner(VACUUM, total_energy(VACUUM)).real
    vacuum_charge = inner(VACUUM, total_charge(VACUUM)).real
    report("vacuum energy and charge of the two universes",
           f"{vacuum_energy:.10f} and {vacuum_charge:.10f}")
    check_record(abs(vacuum_energy + 16 * E) < 1e-9 and abs(vacuum_charge - 16) < 1e-9,
                 "each universe has the sea energy -8E = -40 (total -80) and charge 8",
                 record="Revision/theory/reports/python-field-theory.json, check "
                        "good_sector_positive_fock_realisation")
    '''),
    md(r"""
    The next cell checks the eigenvalue statement on 200 random patterns, computes the
    pair state $b^*_{1}d^*_{2}|0\rangle$ (a particle in universe 1 and an antiparticle
    in universe 2), counts all $2^{32}$ patterns by the number of quanta and the total
    charge with the binomial numbers $\binom{8}{j}$ (four groups of 8 modes: particles
    and antiparticles of each universe), and draws the counts.
    """),
    code(r'''
    def quanta_and_charge(n):
        """(number of quanta, total charge) of the pattern n of the 32 modes."""
        groups = [bin((n >> shift) & 0xFF).count("1") for shift in (0, 8, 16, 24)]
        b_1, d_1, b_2, d_2 = groups  # particles and antiparticles of each universe
        return b_1 + d_1 + b_2 + d_2, b_1 - d_1 + b_2 - d_2


    eigen_ok = True
    for n in rng.integers(0, 2 ** 32, size=200):
        n = int(n)
        quanta, charge = quanta_and_charge(n)
        state = {n: 1.0}
        eigen_ok = eigen_ok and largest(add(
            (1, total_energy(state)), (-(E * quanta + vacuum_energy), state))) < 1e-9
        eigen_ok = eigen_ok and largest(add(
            (1, total_charge(state)), (-(charge + vacuum_charge), state))) < 1e-9
    check(eigen_ok, "200 random patterns: energy E (quanta) - 16E, charge (b - d) + 16")

    pair = create(24, create(0, VACUUM))  # b_1^* (mode 0), then d_2^* (mode 24)
    pair_energy = inner(pair, total_energy(pair)).real - vacuum_energy
    pair_charge = inner(pair, total_charge(pair)).real - vacuum_charge
    report("pair state: normal-ordered total energy and total charge",
           f"{pair_energy:.10f} and {pair_charge:.10f}")
    check(abs(pair_energy - 2 * E) < 1e-9 and abs(pair_charge) < 1e-9,
          "a particle in universe 1 and an antiparticle in universe 2: charge 0, "
          "energy 2E")

    counts = np.zeros((33, 33), dtype=np.int64)  # rows: quanta, columns: charge + 16
    for b_1 in range(9):
        for d_1 in range(9):
            for b_2 in range(9):
                for d_2 in range(9):
                    number = comb(8, b_1) * comb(8, d_1) * comb(8, b_2) * comb(8, d_2)
                    counts[b_1 + d_1 + b_2 + d_2, b_1 - d_1 + b_2 - d_2 + 16] += number
    zero_energy_states = int(counts[0].sum())
    zero_charge_lowest = min(q for q in range(33) if q > 0 and counts[q, 16] > 0)
    report("number of patterns", int(counts.sum()))
    report("patterns of zero normal-ordered energy", zero_energy_states)
    report("fewest quanta of a non-vacuum state of total charge 0", zero_charge_lowest)
    check(counts.sum() == 2 ** 32 and zero_energy_states == 1 and zero_charge_lowest == 2,
          "only the vacuum has energy 0; charge 0 needs at least 2 quanta (energy 2E)")

    fig, ax = plt.subplots(figsize=(7.5, 5.6))
    shown = np.where(counts > 0, np.log10(np.maximum(counts, 1)), np.nan)  # NaN: empty
    light_to_dark = LinearSegmentedColormap.from_list(
        "light_to_dark_blue", ["#cde2fb", "#2a78d6", "#0d366b"])
    image = ax.imshow(shown, origin="lower", cmap=light_to_dark, aspect="auto",
                      extent=(-16.5, 16.5, -0.5, 32.5))
    ax.annotate("vacuum: the only state of energy 0", (0, 0), xytext=(2.0, 1.5),
                fontsize=8, arrowprops={"arrowstyle": "->", "color": GREY})
    ax.annotate("pair of total charge 0: energy $2E$", (0, 2), xytext=(3.0, 5.5),
                fontsize=8, arrowprops={"arrowstyle": "->", "color": GREY})
    ax.set_xlabel("total charge (particles minus antiparticles, both universes)")
    ax.set_ylabel("number of quanta (total energy $= 5 \\times$ quanta)")
    ax.set_title("Two universes, one momentum: $2^{32}$ states")
    ax.grid(False)
    fig.colorbar(image, ax=ax, label="$\\log_{10}$ of the number of states")
    save_figure(fig, "two_universe_states",
                "All $2^{32}$ quantum states of two independently quantised universes "
                "of masses $+m$ and $-m$ for one good-sector momentum ($m = 2$, $k = (1, "
                "2, 0, 4)$, $E = 5$ in both), sorted by the total charge (horizontal "
                "axis) and the number of quanta (vertical axis; the normal-ordered total "
                "energy is $5$ times the number of quanta). The colour is the base-10 "
                "logarithm of the number of states in each square; white squares are "
                "empty. The energies of the two universes add: only the vacuum has "
                "total energy 0, every other state has a positive energy, and a pair of "
                "total charge 0 (a particle in one universe, an antiparticle in the "
                "other) has the energy $2E$, not 0.")
    '''),
    md(r"""
    ## 13. The last check

    The last cell checks that all five figure files exist in the folder
    Revision/textbook/figures and prints the number of checks that passed.
    """),
    code(r'''
    for name in ("10g_1_krein_metrics.png", "10g_2_one_system.png",
                 "10g_3_anticommutator_blocks.png", "10g_4_block_generator.png",
                 "10g_5_two_universe_states.png"):
        check(output_file(f"{FIGURE_FOLDER}/{name}").is_file(),
              f"the figure file {name} exists")
    all_checks_passed()
    '''),
    md(r"""
    ## 14. What this notebook showed

    - PROVED (exactly, for all field values, flat 4+4 space, $U = 0$):
      $\mathcal{L}_m[\Gamma\chi] = -\mathcal{L}_{-m}[\chi]$; the time-derivative kernels
      are $N = B$ for the field, $N = -B$ for its chirality image (the same system in
      the variable $\chi = \Gamma\Psi$) and $N = +B$ for an independent universe of
      mass $-m$, so the canonical rules are $+B$, $-B$ and $+B$ (REPRODUCED: the
      Revision checks of the image metric and of its own quantisation).
    - CHECKED on a Fock space: the chirality image carries $-B$, the mirror image keeps
      $+B$; $H_m[\Psi] = -H_{-m}[\Gamma\Psi]$ and $Q[\Psi] = -Q[\Gamma\Psi]$ as
      operators, and the image obeys the wave equation of mass $-m$ under the same
      energy operator. PROVED (exactly): $(-B)(-h'_m) = \Gamma(Bh'_{-m})\Gamma =
      Bh'_m$. So $T \to -T$ and $J \to -J$ of T1 are identities inside ONE quantum
      system: the field and its image are the same universe, and the image is not a
      universe of negative energy.
    - CHECKED: an independent second universe must anticommute with the first; the
      chirality image, the mirror image and the conjugate field $\Gamma\Psi^{\dagger T}$
      all fail this (cross anticommutators of rank 16). The chirality image also has
      the wrong rule $-B$, so it cannot be identified with an independently quantised
      mass $-m$ universe (REPRODUCED); a mirror universe has the rule $+B$ of an
      ordinary independent copy.
    - CHECKED (32 modes): two independently quantised universes of masses $+m$ and $-m$
      have the rules $+B$ each and anticommute. PROVED (exactly, zero momentum): their
      block generator has the eigenvalues $+m$ and $-m$, 16 each (REPRODUCED);
      COMPUTED: $\pm\sqrt{m^2 + k_1^2}$ with momentum. For one good-sector momentum
      the normal-ordered total energy of every state is $E$ times its number of
      quanta: only the vacuum has energy 0, and a pair of total charge 0 has energy
      $2E$. The energies of two universes ADD; there is no cancellation.
    - NOT ESTABLISHED by these computations: that any universe, or any pair of
      universes, is CREATED; any rate, amplitude or mechanism of creation; a positive
      state space for the whole field (the positive Fock spaces here are built for
      single good-sector momenta with frozen coefficients).
    """),
]

if __name__ == "__main__":
    raise SystemExit(run_builder(__file__))
