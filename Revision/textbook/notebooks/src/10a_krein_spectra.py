#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
"""Builder of Notebook 10a, "One-particle spectra and Krein signatures" (textbook
"Universes in Pairs", chapter 10: canonical quantisation in 4+4, the Krein space and the
good sector).

The notebook Revision/textbook/notebooks/10a_krein_spectra.ipynb is BUILT from this file
by Revision/textbook/tools/nbkit.py (never edit the .ipynb by hand):

    python Revision/textbook/tools/nbkit.py build \
        Revision/textbook/notebooks/src/10a_krein_spectra.py --date YYYY-MM-DD
    python Revision/textbook/tools/nbkit.py check \
        Revision/textbook/notebooks/src/10a_krein_spectra.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools"))
from nbkit import code, md, run_builder  # noqa: E402

FACTS = {
    "id": "10a",
    "name": "10a_krein_spectra",
    "title": "One-particle spectra and Krein signatures",
    "purpose": (
        "It builds the Krein matrix B from the author's gamma matrices, the one-particle "
        "mode Hamiltonian h of a plane wave in flat 4+4 space, proves exactly with sympy "
        "that h squared is the squared frequency times the identity and that B h equals "
        "h dagger B, computes the eigenvalues of h as the momentum along an extra time "
        "grows, the Krein inertia of every eigenspace (4 positive and 4 negative "
        "directions at every real frequency, none at an imaginary frequency), checks "
        "that the universes of masses +m and -m have the same one-particle spectrum, "
        "reproduces the recorded samples of the Revision pairing record, and draws six "
        "teaching figures."
    ),
    "records": [
        ["Revision/algebra/gammas.json",
         "the author's gamma matrices and the matrix B (read; B is recomputed and compared)"],
        ["Revision/theory/reports/python-field-theory.json",
         "checks B_properties, mode_hamiltonian_B_selfadjoint_dispersion and "
         "good_sector_spectrum_and_B_sectors (reproduced)"],
        ["Revision/theory/reports/wolfram-field-theory.json",
         "checks mode_hamiltonian_good_sector and mode_hamiltonian_Krein_selfadjoint "
         "(reproduced)"],
        ["Revision/pairing/pairing-theory.json",
         "the eight recorded one-particle samples, data entry one_particle_flat (read and "
         "reproduced)"],
        ["Revision/pairing/reports/python-pairing.json",
         "checks Q.one_particle_maps, Q.one_particle_Krein_inertia, "
         "Q.one_particle_Krein_inertia_proof and "
         "Q.one_particle_complex_frequency_Krein_neutral (reproduced)"],
        ["Revision/pairing/reports/wolfram-pairing.json",
         "checks Q_one_particle_flat_dispersion, Q_one_particle_maps, "
         "Q_one_particle_Krein_signatures and "
         "Q_one_particle_complex_and_zero_frequencies_Krein_neutral (reproduced)"],
    ],
    "packages": ["numpy", "sympy", "matplotlib"],
    "needs_rust": [],
    "expected_seconds": 15,
    "timeout_seconds": 300,
    "files_written": [
        "Revision/textbook/figures/10a.captions.json",
        "Revision/textbook/figures/10a_1_gamma4_c_and_b.png",
        "Revision/textbook/figures/10a_2_frequency_squared.png",
        "Revision/textbook/figures/10a_3_eigenvalue_flow.png",
        "Revision/textbook/figures/10a_4_krein_inertia_scan.png",
        "Revision/textbook/figures/10a_5_krein_gram_matrices.png",
        "Revision/textbook/figures/10a_6_plus_minus_mass_spectra.png",
    ],
    "final_lines": [
        "PASS the figure file 10a_6_plus_minus_mass_spectra.png exists",
        "ALL 28 CHECKS PASSED (notebook 10a)",
    ],
    "troubleshooting": [
        ["\"FileNotFoundError\" for a file below the folder Revision",
         "the notebook reads files of the Revision record: the data it starts from and "
         "the report files whose checks it reproduces (each cited check must still "
         "exist there with the verdict PASS). It must be opened inside the folder "
         "Revision/textbook/notebooks of a complete copy of the repository (a notebook "
         "copied alone to another folder cannot find them). Clone the repository again "
         "and open the notebook there."],
        ["\"AssertionError: the cited record check is missing or not PASS\"",
         "a report file of the Revision record no longer holds the check that the "
         "notebook names, or holds it with another verdict: the copy of the repository "
         "is incomplete or was changed. Clone the repository again and open the "
         "notebook there."],
        ["\"Jupyter command `jupyter-lab` not found\" or \"Jupyter command "
         "`jupyter-nbconvert` not found\" after a command that starts with "
         "`python -m jupyter`",
         "that form still has to find the programs jupyter-lab and jupyter-nbconvert in "
         "the folders where the terminal looks for programs, and it did not find them "
         "there. Do Step 4 and type `jupyter` again. Or start the two "
         "programs through Python itself, in the folder of the notebook: the first "
         "command below does what `jupyter lab` does in Step 5, the second what "
         "`jupyter nbconvert` does in Step 6.",
         ["python -m jupyterlab 10a_krein_spectra.ipynb",
          "python -m nbconvert --to notebook --execute --inplace "
          "10a_krein_spectra.ipynb"]],
    ],
}

CELLS = [
    md(r"""
    ## 1. What this notebook computes

    This notebook studies ONE wave of the field dirac16complex at a time: a plane wave
    with fixed momenta along the seven directions of a slice $x_4 = $ const, in flat
    4+4 space (or in the frozen-coefficient model of the author's universe, which has
    the same equation but is an ASSUMPTION; section 4 says exactly what it leaves out).
    It

    - builds, from the author's gamma matrices, the matrix $B = -iC\gamma^{(x_4)}$ that
      appears in the charge density $\Psi^\dagger B \Psi$ and later in the canonical
      anticommutator, and checks that $B$ is Hermitian, squares to 1 and has eight
      eigenvalues $+1$ and eight eigenvalues $-1$;
    - writes the field equation of one plane wave as $i\,du/dx_4 = h\,u$ with a
      $16 \times 16$ matrix $h$, the *mode Hamiltonian*;
    - proves with exact algebra (sympy) that $h^2 = w^2 I_{16}$ with
      $w^2 = m^2 + k_1^2 + k_2^2 + k_3^2 + k_8^2 - k_5^2 - k_6^2 - k_7^2$, and that
      $B h = h^\dagger B$;
    - follows the eigenvalues of $h$ as the momentum $k_5$ along the extra time $x_5$
      grows: they are real (oscillation) while $w^2 > 0$ and imaginary (growth) when
      $w^2 < 0$;
    - computes the *Krein inertia* of every eigenspace: how many directions of positive
      and of negative charge it contains. The answer is 4 and 4 at every real
      frequency, and 0 and 0 (a *neutral* eigenspace) at every imaginary frequency;
    - checks that the masses $+m$ and $-m$ give the SAME one-particle spectrum;
    - reproduces every recorded number of the Revision record that it touches, and
      draws six teaching figures.
    """),
    md(r"""
    ## 3. The words used in this notebook

    - **Matrix, entry, identity**: a matrix is a table of numbers; $M_{AB}$ is the entry
      in row $A$ and column $B$. $I_{16}$ (in code `np.eye(16)`) is the $16 \times 16$
      identity matrix: 1 on the diagonal, 0 elsewhere.
    - **Complex conjugate, transpose, dagger**: $z^*$ changes $i$ into $-i$; $M^T$
      exchanges rows and columns; $M^\dagger = (M^T)^*$ is the *conjugate transpose*
      (in code `M.conj().T`). For a column $u$, $u^\dagger$ is the row of the
      conjugated entries, and $u^\dagger v = \sum_A u_A^* v_A$.
    - **Hermitian**: $M^\dagger = M$. A Hermitian matrix has real eigenvalues.
    - **Eigenvalue, eigenvector, eigenspace**: if $M u = \lambda u$ with $u \neq 0$,
      then $\lambda$ is an eigenvalue and $u$ an eigenvector; all eigenvectors of one
      eigenvalue (with the zero column) form its eigenspace.
    - **Projector**: a matrix $P$ with $P^2 = P$. It maps every column into one
      subspace (its *range*) and leaves the columns of that subspace unchanged.
    - **Trace**: $\mathrm{tr}\,M$, the sum of the diagonal entries; it equals the sum
      of the eigenvalues.
    - **Krein form**: the number $u^\dagger B v$ for two columns $u, v$. Because $B$ is
      Hermitian, $u^\dagger B u$ is real, but it can be positive, negative or zero. In
      the theory it is the charge of the wave $u$.
    - **Signature, inertia**: a Hermitian matrix with $p$ positive, $n$ negative and $z$
      zero eigenvalues has inertia $(p, n, z)$; the signature of $B$ is $(8, 8)$. The
      *Krein inertia of a subspace* is the inertia of the Krein form restricted to it.
    - **Neutral subspace**: a subspace on which $u^\dagger B v = 0$ for all $u, v$ in it.
    - **Plane wave, momentum, frequency**: $\Psi = u\,e^{i(k\cdot x - w x_4)}$ with a
      constant column $u$; the numbers $k_a$ are the momenta (wave numbers) along the
      slice directions and $w$ is the frequency. A real $w$ means oscillation, an
      imaginary $w = i\kappa$ means growth like $e^{\kappa x_4}$.
    - **Good sector**: waves that do not depend on the extra times $x_5, x_6, x_7$,
      that is $k_5 = k_6 = k_7 = 0$.
    - **Chirality** $\Gamma = \gamma^{(x_8)}\gamma^{(x_1)}\cdots\gamma^{(x_7)}$: the
      product of all eight gammas in the author's order.
    - **sympy, numpy**: sympy computes EXACTLY with symbols (a proof for all values);
      numpy computes with floating-point numbers (about 16 digits), so its checks
      allow a tiny tolerance such as $10^{-10}$.
    """),
    md(r"""
    ## 4. The physical and mathematical situation

    The author's coordinates are $x_1, x_2, x_3$ (ordinary 3-space), $x_4$ (the time),
    $x_5, x_6, x_7$ (the three EXTRA TIMES, which deflate exponentially in the author's
    metric) and $x_8$ (the hidden space direction). The frame metric is
    $\eta = \mathrm{diag}(+1, +1, +1, -1, -1, -1, -1, +1)$ in the order $x_1, \dots, x_8$:
    the gammas obey $\gamma^{(a)}\gamma^{(b)} + \gamma^{(b)}\gamma^{(a)} =
    2\eta^{ab} I_{16}$, so $(\gamma^{(a)})^2 = +1$ for $x_1, x_2, x_3, x_8$ and $-1$
    for $x_4, \dots, x_7$.

    **From the field equation to the mode Hamiltonian, line by line.** With $U = 0$ and
    without gravity (flat 4+4 space, or the frozen-coefficient model described below)
    the field equation of dirac16complex is

    $$\gamma^{(x_4)}\partial_4\Psi + \sum_{a \neq 4}\gamma^{(x_a)}\partial_a\Psi = m\Psi .$$

    Multiply from the left by $\gamma^{(x_4)}$ and use $(\gamma^{(x_4)})^2 = -1$:

    $$-\partial_4\Psi + \sum_{a \neq 4}\gamma^{(x_4)}\gamma^{(x_a)}\partial_a\Psi =
    m\gamma^{(x_4)}\Psi .$$

    Move $\partial_4\Psi$ to the right-hand side and everything else to the left, then
    exchange the two sides:

    $$\partial_4\Psi = -m\gamma^{(x_4)}\Psi + \sum_{a \neq 4}
    \gamma^{(x_4)}\gamma^{(x_a)}\partial_a\Psi .$$

    For a plane wave $\Psi = u(x_4)\,e^{i\sum_{a \neq 4} k_a x_a}$ every $\partial_a$
    with $a \neq 4$ becomes the factor $i k_a$ (the derivative of $e^{ik_a x_a}$ is
    $ik_a e^{ik_a x_a}$); cancel the common exponential:

    $$\frac{du}{dx_4} = -m\gamma^{(x_4)}u + i\sum_{a \neq 4} k_a
    \gamma^{(x_4)}\gamma^{(x_a)}u .$$

    Multiply by $i$ (and use $i \cdot i = -1$):

    $$i\frac{du}{dx_4} = h\,u,\qquad h = -im\gamma^{(x_4)} - \gamma^{(x_4)}
    \sum_{a \neq 4} k_a\gamma^{(x_a)} .$$

    **Frame momenta and the deflating extra times.** The numbers $k_a$ are momenta in
    the local frame. In the author's metric the field equation contains the derivative
    along $x_a$ divided by the scale factor $f_a$ of that direction (Revision theory
    record): $f_a = e^{a_4}\sin^{1/6}z$ for $x_1, x_2, x_3$ and $f_a =
    e^{-a_4}\sin^{1/6}z$ for the extra times $x_5, x_6, x_7$. A wave $e^{iq_ax_a}$
    with the coordinate momentum $q_a$ therefore has the frame momentum $k_a = q_a/f_a$:
    along 3-space $k_a = q_ae^{-a_4}\sin^{-1/6}z$ shrinks as 3-space inflates, and along
    an extra time $k_a = q_ae^{a_4}\sin^{-1/6}z$ GROWS as the extra times deflate
    ($a_4$ increasing). The *frozen-coefficient model* evaluates these factors at one
    time $x_4$ and one hidden position, so that the wave equation of that instant has
    constant coefficients, AND it leaves out the two terms of the hidden direction that
    the author's field equation also contains: the derivative $\tan z\,
    \gamma^{(x_8)}\partial_8\Psi$ with its coefficient that changes along $x_8$, and the
    spin-connection term $3H\gamma^{(x_8)}\Psi$ (Revision theory record, formula
    `field_equation`). The model is therefore an ASSUMPTION. Kept in the equation, the
    connection term would add $3iH\gamma^{(x_4)}\gamma^{(x_8)}$ to the matrix $h$ above;
    that matrix commutes with $B$ and is anti-Hermitian, so it would spoil the identity
    $Bh = h^\dagger B$ that this notebook proves, and the frequencies could become
    complex. The extra times are not static: the notebook "The Krein structure along the
    deflating history" of this chapter follows the frame momenta, and everything this
    notebook computes, along the deflating history.

    **The Krein form is conserved.** The charge density of the field is
    $\Psi^\dagger B\Psi$ with $B = -iC\gamma^{(x_4)}$, $C = \gamma^{(x_8)}\gamma^{(x_1)}
    \gamma^{(x_2)}\gamma^{(x_3)}$ (the author's sigma16). From $i\,du/dx_4 = hu$ we get
    $du/dx_4 = -ihu$ and, taking the dagger, $du^\dagger/dx_4 = i u^\dagger h^\dagger$.
    By the product rule

    $$\frac{d}{dx_4}(u^\dagger B u) = i u^\dagger h^\dagger B u - i u^\dagger B h u =
    i\,u^\dagger(h^\dagger B - B h)u ,$$

    which is zero for every $u$ exactly when $B h = h^\dagger B$. The notebook proves
    this identity. The ordinary squared length $u^\dagger u$, on the other hand, is
    conserved only when $h$ is Hermitian.

    **Krein inertia.** Because $h^2 = w^2 I_{16}$, for $w \neq 0$ the two matrices
    $P_\pm = \frac12(I_{16} \pm h/w)$ are projectors onto the eigenspaces of $\pm w$
    (check: $P_\pm^2 = \frac14(I \pm 2h/w + h^2/w^2) = \frac14(2I \pm 2h/w) = P_\pm$,
    and $hP_\pm = \frac12(h \pm w^2/w) = \pm w P_\pm$). The Krein inertia of an
    eigenspace tells how many of its independent waves carry positive and how many
    negative charge. Every statement here is a statement about one-particle waves; the
    quantum field built from them is the subject of the later notebooks of this chapter.
    """),
    md(r"""
    ## 5. The gamma matrices and the Krein matrix $B$

    The next cell reads the author's gamma matrices from the Revision record
    `Revision/algebra/gammas.json` (16 x 16 matrices of whole numbers), stores them as
    `gamma[1]`, ..., `gamma[8]` so that `gamma[a]` is $\gamma^{(x_a)}$, and checks the
    64 Clifford relations exactly (whole numbers, no rounding).

    It also defines `check_record(condition, name, record)`. It does what
    `check(condition, name, record=record)` of the set-up cell does (stop with an error
    if the condition is false, otherwise print the PASS line and the line naming the
    Revision record that the check reproduces), but it first collects the two printed
    lines and then prints them in one piece. Jupyter sends printed text to the screen
    in pieces whose boundaries depend on timing; printing the two lines in one piece
    keeps them together in every run, so that the stored output of the notebook is the
    same every time. Before it checks anything, `check_record` asks the helper
    `record_says_pass(record)` whether the cited record still says what the notebook
    claims: a record name of the form `<report file>, check <check name>` names a check
    of a Revision report, and the helper opens that report (each file only once, kept
    in the dictionary `REPORT_CHECKS`) and answers True only if a check of that name
    exists there with the verdict PASS. If not, the notebook stops with an error
    instead of printing an outdated claim. A record name without `, check ` names a data
    entry of a file that the notebook reads and compares itself.
    """),
    code(r'''
    import contextlib  # lets a block of code print into a text buffer
    import io  # the text buffer
    import sys  # the screen output, sys.stdout

    import numpy as np  # numbers, arrays and matrices
    import sympy as sp  # exact algebra with symbols


    REPORT_CHECKS = {}  # report file -> {check name: verdict}; each file is read once


    def record_says_pass(record):
        """True if the cited report check exists today with the verdict PASS."""
        path, separator, check_name = record.partition(", check ")
        if not separator:  # a data entry of a record file that the notebook reads itself
            return True
        if path not in REPORT_CHECKS:
            checks = json.loads(repository_file(path).read_text(encoding="utf-8"))["checks"]
            REPORT_CHECKS[path] = {c["name"]: c["verdict"].upper() for c in checks}
        return REPORT_CHECKS[path].get(check_name) == "PASS"


    def check_record(condition, name, record):
        """check(condition, name, record=record), printed in one piece."""
        if not record_says_pass(record):  # the cited check must exist and say PASS
            raise AssertionError("the cited record check is missing or not PASS: " + record)
        buffer = io.StringIO()
        with contextlib.redirect_stdout(buffer):  # what check prints goes to buffer
            check(condition, name, record=record)
        sys.stdout.write(buffer.getvalue())  # one single piece of output


    fixture = json.loads(repository_file("Revision/algebra/gammas.json").read_text(
        encoding="utf-8"))
    # gamma[a] is the matrix gamma^(x_a) of the coordinate x_a, a = 1, ..., 8.
    gamma = {a: np.array(fixture["gamma"][a - 1], dtype=int) for a in range(1, 9)}
    eta = {a: fixture["eta"][a - 1] for a in range(1, 9)}  # +1 space-like, -1 time-like
    identity = np.eye(16, dtype=int)
    say(f"eta = {[eta[a] for a in range(1, 9)]} for x1, ..., x8")
    clifford_ok = all(
        np.array_equal(gamma[a] @ gamma[b] + gamma[b] @ gamma[a],
                       2 * (eta[a] if a == b else 0) * identity)
        for a in range(1, 9) for b in range(1, 9))  # all 64 pairs (a, b)
    check(clifford_ok,
          "the 64 Clifford relations hold exactly (eta = diag(+,+,+,-,-,-,-,+))")
    '''),
    md(r"""
    The next cell builds $C = \gamma^{(x_8)}\gamma^{(x_1)}\gamma^{(x_2)}\gamma^{(x_3)}$
    and $B = -iC\gamma^{(x_4)}$ (in Python the imaginary unit is written `1j`), and
    compares $B$ with the matrix `B` stored in the same record (its real and imaginary
    parts are stored separately). Then it checks the four properties of $B$ that the
    chapter uses: $B$ is purely imaginary, $B^\dagger = B$, $B^2 = I_{16}$, and its
    trace is 0. Since $B^2 = I$, every eigenvalue $\lambda$ obeys $\lambda^2 = 1$, so it is
    $+1$ or $-1$; the trace 0 (the sum of the eigenvalues) then forces eight of each:
    the signature $(8, 8)$. The cell confirms this by computing the eigenvalues.
    """),
    code(r'''
    C = gamma[8] @ gamma[1] @ gamma[2] @ gamma[3]  # the author's sigma16
    B = -1j * (C @ gamma[4])  # B = -i C gamma^(x4), a complex 16 x 16 matrix
    B_file = np.array(fixture["B"]["re"]) + 1j * np.array(fixture["B"]["im"])
    check_record(np.array_equal(B, B_file),
                 "B = -i C gamma^(x4) equals the matrix B of the record",
                 record="Revision/algebra/gammas.json, entry B")
    purely_imaginary = np.all(B.real == 0)  # every entry is 0, +i or -i
    hermitian = np.array_equal(B, B.conj().T)  # B^dagger = B
    squares_to_one = np.array_equal(B @ B, np.eye(16))  # B^2 = I
    trace_B = np.trace(B)  # the sum of the diagonal entries
    eigenvalues_B = np.linalg.eigvalsh(B)  # the 16 real eigenvalues, sorted
    n_plus = int(np.sum(eigenvalues_B > 0.5))  # how many are +1
    n_minus = int(np.sum(eigenvalues_B < -0.5))  # how many are -1
    report("trace of B", int(round(abs(trace_B))))
    report("eigenvalues of B equal to +1 and to -1", f"{n_plus} and {n_minus}")
    check_record(purely_imaginary and hermitian and squares_to_one and trace_B == 0
                 and (n_plus, n_minus) == (8, 8),
                 "B is imaginary and Hermitian, B^2 = I, tr B = 0, signature (8, 8)",
                 record="Revision/theory/reports/python-field-theory.json, check "
                        "B_properties")
    '''),
    md(r"""
    The next cell defines the colours of all figures of this notebook (a blue, an
    orange and a green that stay distinguishable for colour-blind readers, and a
    blue-grey-red colour scale for matrices: blue for $-1$, light grey for 0, red for
    $+1$) and a small function that draws a matrix as a coloured square grid, a *heat
    map*. It checks what the picture will show: $\gamma^{(x_4)}$ is antisymmetric
    ($M^T = -M$), $C$ is symmetric ($M^T = M$), the imaginary part of $B$ is
    antisymmetric, and each of the three has exactly one nonzero entry in every row
    and every column. Why the imaginary part of $B$ must be antisymmetric: write
    $B = iY$ with a real matrix $Y$; then $B^\dagger = (iY)^{*T} = -iY^T$, and
    $B^\dagger = B$ means $-iY^T = iY$, that is $Y^T = -Y$. Then it draws
    $\gamma^{(x_4)}$, $C$ and the imaginary part of $B$ side by side.
    """),
    code(r'''
    from matplotlib.colors import LinearSegmentedColormap  # colour scales

    BLUE, ORANGE, GREEN, GREY = "#2a78d6", "#eb6834", "#1baf7a", "#52514e"
    # A diverging colour scale: dark blue (negative), light grey (zero), red (positive).
    DIVERGING = LinearSegmentedColormap.from_list(
        "blue_grey_red", ["#184f95", "#f0efec", "#e34948"])
    # A sequential colour scale for sizes: almost white (zero) to dark blue (large).
    SEQUENTIAL = LinearSegmentedColormap.from_list(
        "white_blue", ["#fcfcfb", "#86b6ef", "#184f95"])


    def draw_matrix(ax, matrix, title, cmap=DIVERGING, vmin=-1.0, vmax=1.0):
        """Draw a real matrix as a heat map with rows and columns numbered from 1."""
        image = ax.imshow(matrix, cmap=cmap, vmin=vmin, vmax=vmax)
        size = matrix.shape[0]
        ticks = list(range(0, size, 3))  # every third row and column is labelled
        ax.set_xticks(ticks, [str(t + 1) for t in ticks])
        ax.set_yticks(ticks, [str(t + 1) for t in ticks])
        ax.grid(False)  # no grid lines on top of the squares
        ax.set_title(title)
        return image


    # A purely imaginary B = i Y (Y real) is Hermitian exactly when -i Y^T = i Y,
    # that is when Y^T = -Y: the imaginary part of B must be antisymmetric.
    one_per_row = all(np.count_nonzero(M, axis=1).tolist() == [1] * 16
                      and np.count_nonzero(M, axis=0).tolist() == [1] * 16
                      for M in (gamma[4], C, B.imag))  # signed permutation matrices
    check(np.array_equal(gamma[4].T, -gamma[4]) and np.array_equal(C.T, C)
          and np.array_equal(B.imag.T, -B.imag) and one_per_row,
          "gamma^(x4) and Im B are antisymmetric, C is symmetric, all signed permutations")

    fig, axes = plt.subplots(1, 3, figsize=(11.0, 4.0))
    draw_matrix(axes[0], gamma[4], "$\\gamma^{(x_4)}$ (real, antisymmetric)")
    draw_matrix(axes[1], C, "$C$ (real, symmetric)")
    image = draw_matrix(axes[2], B.imag, "imaginary part of $B = -iC\\gamma^{(x_4)}$")
    fig.colorbar(image, ax=list(axes), shrink=0.8, label="entry")
    save_figure(fig, "gamma4_c_and_b",
                "Heat maps of three 16 by 16 matrices: the time gamma $\\gamma^{(x_4)}$ "
                "(left), the matrix $C = \\gamma^{(x_8)}\\gamma^{(x_1)}\\gamma^{(x_2)}"
                "\\gamma^{(x_3)}$ (middle) and the imaginary part of $B = -iC"
                "\\gamma^{(x_4)}$ (right; its real part is zero). Horizontal axis: "
                "column number, vertical axis: row number; red is $+1$, blue is $-1$, "
                "light grey is 0. Each row and each column has exactly one nonzero "
                "entry: all three are signed permutation matrices, so $B$ is $i$ times "
                "a real signed permutation. $C$ is symmetric about the diagonal; "
                "$\\gamma^{(x_4)}$ and the imaginary part of $B$ are antisymmetric "
                "(mirror entries have opposite colours), as they must be: a Hermitian "
                "matrix whose entries are purely imaginary is $i$ times a real "
                "antisymmetric matrix.")
    '''),
    md(r"""
    ## 6. The mode Hamiltonian and its square

    The next cell defines two functions. `mode_hamiltonian(m, k)` returns the numpy
    matrix $h = -im\gamma^{(x_4)} - \gamma^{(x_4)}\sum_a k_a\gamma^{(x_a)}$, where `k` is a
    dictionary that gives the momentum $k_a$ for some of the slice directions
    $a = 1, 2, 3, 5, 6, 7, 8$ (missing directions have momentum 0).
    `frequency_squared(m, k)` returns $w^2 = m^2 + \sum_a \eta_{aa}k_a^2$: the
    space-like momenta enter with $+$, the extra-time momenta with $-$.
    """),
    code(r'''
    def mode_hamiltonian(m, k):
        """h = -i m gamma^(x4) - gamma^(x4) sum_a k_a gamma^(x_a), a numpy matrix;
        k is a dictionary {a: k_a} for some of the directions a = 1, 2, 3, 5, 6, 7, 8."""
        h = -1j * m * gamma[4]
        for a, k_a in k.items():
            h = h - k_a * (gamma[4] @ gamma[a])
        return h


    def frequency_squared(m, k):
        """w^2 = m^2 + k1^2 + k2^2 + k3^2 + k8^2 - k5^2 - k6^2 - k7^2."""
        return m ** 2 + sum(eta[a] * k_a ** 2 for a, k_a in k.items())


    example = {1: 0.3, 2: -1.1, 3: 0.7, 5: 0.4, 6: 0.2, 7: -0.9, 8: 1.3}  # any numbers
    h_example = mode_hamiltonian(1.7, example)
    w2_example = frequency_squared(1.7, example)
    report("w^2 for m = 1.7 and the example momenta", f"{w2_example:.6f}")
    error = np.max(np.abs(h_example @ h_example - w2_example * np.eye(16)))
    report("largest entry of h^2 - w^2 I (rounding only)", f"{error:.1e}")
    check(error < 1e-12, "numerical example: h^2 = w^2 I at one generic point")
    '''),
    md(r"""
    A numerical example is not a proof. The next cell repeats the computation EXACTLY
    with sympy, for symbols $m, k_1, k_2, k_3, k_5, k_6, k_7, k_8$ that stand for any
    real numbers. It checks two identities for all values at once:

    - $h^2 = w^2 I_{16}$ (so every eigenvalue of $h$ is $+w$ or $-w$);
    - $B h = h^\dagger B$ (so the Krein form $u^\dagger B u$ of every wave is conserved,
      as Section 4 showed).

    Why $h^2 = w^2 I$ holds: $(-im\gamma^{(x_4)})^2 = -m^2(\gamma^{(x_4)})^2 = m^2$;
    $(\gamma^{(x_4)}\gamma^{(x_a)})^2 = -(\gamma^{(x_4)})^2(\gamma^{(x_a)})^2 = \eta_{aa}$
    for $a \neq 4$ (move the second $\gamma^{(x_4)}$ to the left past $\gamma^{(x_a)}$,
    which costs a sign); and all mixed terms cancel in pairs because the matrices
    $\gamma^{(x_4)}$ and $\gamma^{(x_4)}\gamma^{(x_a)}$ anticommute with each other.
    """),
    code(r'''
    g = {a: sp.Matrix(fixture["gamma"][a - 1]) for a in range(1, 9)}  # exact gammas
    C_exact = g[8] * g[1] * g[2] * g[3]
    B_exact = -sp.I * C_exact * g[4]
    m = sp.Symbol("m", real=True)  # the mass: any real number
    k_sym = {a: sp.Symbol(f"k{a}", real=True) for a in (1, 2, 3, 5, 6, 7, 8)}


    def mode_hamiltonian_exact(mass, k):
        """The same h as mode_hamiltonian, as an exact sympy matrix."""
        h = -sp.I * mass * g[4]
        for a, k_a in k.items():
            h = h - k_a * g[4] * g[a]
        return h


    zero = sp.zeros(16, 16)
    h_sym = mode_hamiltonian_exact(m, k_sym)
    w2_sym = m ** 2 + sum(eta[a] * k_sym[a] ** 2 for a in k_sym)
    say(f"w^2 = {w2_sym}")
    square_ok = (h_sym * h_sym - w2_sym * sp.eye(16)).applyfunc(sp.expand) == zero
    check_record(square_ok, "exact: h^2 = w^2 I for all real m and k",
                 record="Revision/pairing/reports/wolfram-pairing.json, check "
                        "Q_one_particle_flat_dispersion")
    krein_ok = (B_exact * h_sym - h_sym.H * B_exact).applyfunc(sp.expand) == zero
    check_record(krein_ok,
                 "exact: B h = h^dagger B for all real m and k (Krein self-adjoint)",
                 record="Revision/theory/reports/python-field-theory.json, check "
                        "mode_hamiltonian_B_selfadjoint_dispersion")
    '''),
    md(r"""
    When is $h$ Hermitian, and when does it commute with $B$? The next cell computes
    the exact matrices $h - h^\dagger$ and $Bh - hB$ and lists the symbols that appear
    in them. Only $k_5, k_6, k_7$ appear: both matrices vanish exactly when there is no
    momentum along the extra times, the *good sector*. (The reason: $\gamma^{(x_4)}
    \gamma^{(x_a)}$ is Hermitian for the space-like directions and anti-Hermitian for
    the extra times, and it commutes with $B$ for $a = 1, 2, 3, 8$ and anticommutes
    with $B$ for $a = 5, 6, 7$.)
    """),
    code(r'''
    not_hermitian_part = (h_sym - h_sym.H).applyfunc(sp.expand)
    commutator = (B_exact * h_sym - h_sym * B_exact).applyfunc(sp.expand)
    symbols_1 = sorted(str(s) for s in not_hermitian_part.free_symbols)
    symbols_2 = sorted(str(s) for s in commutator.free_symbols)
    say(f"symbols in h - h^dagger: {symbols_1}")
    say(f"symbols in B h - h B:    {symbols_2}")
    good_sector = {k_sym[5]: 0, k_sym[6]: 0, k_sym[7]: 0}  # no extra-time momentum
    check_record(symbols_1 == ["k5", "k6", "k7"]
                 and not_hermitian_part.subs(good_sector) == zero,
                 "exact: h is Hermitian exactly in the good sector k5 = k6 = k7 = 0",
                 record="Revision/theory/reports/wolfram-field-theory.json, check "
                        "mode_hamiltonian_good_sector")
    check_record(symbols_2 == ["k5", "k6", "k7"]
                 and commutator.subs(good_sector) == zero,
                 "exact: B h = h B exactly in the good sector",
                 record="Revision/theory/reports/python-field-theory.json, check "
                        "good_sector_spectrum_and_B_sectors")
    '''),
    md(r"""
    ## 7. The three cases: real, zero and imaginary frequency

    Since $h^2 = w^2 I_{16}$, everything depends on the sign of
    $w^2 = m^2 + k_s^2 - k_t^2$, where $k_s^2 = k_1^2 + k_2^2 + k_3^2 + k_8^2$ collects the
    space-like momenta and $k_t^2 = k_5^2 + k_6^2 + k_7^2$ the extra-time momenta:

    - $w^2 > 0$: the frequencies $\pm w$ are real and the wave oscillates;
    - $w^2 = 0$: $h^2 = 0$ and the wave grows linearly in $x_4$;
    - $w^2 < 0$: the frequencies are $\pm i\kappa$ with $\kappa = \sqrt{-w^2}$, and one
      half of the waves grows like $e^{\kappa x_4}$.

    The next cell draws $w^2$ against $k_5$ (the only extra-time momentum here) for
    $m = 1$ and three values of $k_s$, and checks that the zero crossing lies at
    $k_5 = \sqrt{m^2 + k_s^2}$.
    """),
    code(r'''
    k5_values = np.linspace(0.0, 3.0, 301)  # 301 values of k5 from 0 to 3
    fig, ax = plt.subplots()
    for k_s, colour in ((0.0, BLUE), (1.0, ORANGE), (2.0, GREEN)):
        w2_curve = [frequency_squared(1.0, {1: k_s, 5: k5}) for k5 in k5_values]
        ax.plot(k5_values, w2_curve, color=colour, linewidth=2,
                label=f"$k_s = {k_s:.0f}$")
        crossing = np.sqrt(1.0 + k_s ** 2)  # where w^2 = 0
        ax.plot([crossing], [0.0], "o", color=colour, markersize=8)
    ax.axhline(0.0, color=GREY, linewidth=1)
    ax.text(0.1, 3.0, "$w^2 > 0$: real frequency, the wave oscillates", color=GREY)
    ax.text(0.1, -6.0, "$w^2 < 0$: imaginary frequency, the wave grows", color=GREY)
    ax.set_xlabel("momentum $k_5$ along the extra time $x_5$")
    ax.set_ylabel("$w^2 = m^2 + k_s^2 - k_5^2$")
    ax.set_title("The squared frequency of a plane wave, $m = 1$")
    ax.legend(title="space-like momentum")
    save_figure(fig, "frequency_squared",
                "The squared frequency $w^2 = m^2 + k_s^2 - k_5^2$ of a plane wave with "
                "mass $m = 1$, plotted against the momentum $k_5$ along the extra time "
                "$x_5$ (horizontal axis, units of $m$) for the space-like momentum "
                "$k_s = 0$, 1 and 2 (the three curves). Vertical axis: $w^2$ in units "
                "of $m^2$. Above the grey line the frequency is real and the wave "
                "oscillates; below it the frequency is imaginary and the wave grows. "
                "The dots mark $k_5 = \\sqrt{m^2 + k_s^2}$, where the wave changes "
                "from oscillation to growth: a large enough extra-time momentum always "
                "wins.")
    check(all(abs(frequency_squared(1.0, {1: k_s, 5: np.sqrt(1.0 + k_s ** 2)})) < 1e-12
              for k_s in (0.0, 1.0, 2.0)),
          "w^2 = 0 exactly at k5 = sqrt(m^2 + k_s^2)")
    '''),
    md(r"""
    ## 8. The eigenvalues as the extra-time momentum grows

    The next cell computes the 16 eigenvalues of $h$ numerically (numpy's
    `np.linalg.eigvals`) for $m = 1$, no space-like momentum, and $k_5$ from 0 to 3, and
    plots their real and imaginary parts. The formula predicts eight eigenvalues
    $+\sqrt{1 - k_5^2}$ and eight $-\sqrt{1 - k_5^2}$ for $k_5 < 1$, and eight $+i\kappa$
    and eight $-i\kappa$ with $\kappa = \sqrt{k_5^2 - 1}$ for $k_5 > 1$. At $k_5 = 1$
    exactly the matrix cannot be diagonalised and the numerical eigenvalues are only
    accurate to about $10^{-8}$, so the check leaves out the points with
    $|w^2| < 0.05$.
    """),
    code(r'''
    real_parts, imaginary_parts, worst = [], [], 0.0
    for k5 in k5_values:
        eigenvalues = np.linalg.eigvals(mode_hamiltonian(1.0, {5: k5}))
        real_parts.append(np.sort(eigenvalues.real))
        imaginary_parts.append(np.sort(eigenvalues.imag))
        w2 = 1.0 - k5 ** 2
        if abs(w2) > 0.05:  # away from the point where h cannot be diagonalised
            w = np.sqrt(complex(w2))  # sqrt of a negative number is imaginary
            predicted = np.array([w] * 8 + [-w] * 8)
            # compare the sorted real parts and the sorted imaginary parts separately
            worst = max(worst,
                        np.max(np.abs(np.sort(eigenvalues.real) - np.sort(predicted.real))),
                        np.max(np.abs(np.sort(eigenvalues.imag) - np.sort(predicted.imag))))
    report("largest difference from the formula +-w (8 times each)", f"{worst:.1e}")
    check(worst < 1e-10, "the 16 eigenvalues of h are +w and -w, eight times each")

    fig, axes = plt.subplots(1, 2, figsize=(10.0, 4.0), sharex=True)
    axes[0].plot(k5_values, np.array(real_parts), color=BLUE, linewidth=2)
    axes[1].plot(k5_values, np.array(imaginary_parts), color=ORANGE, linewidth=2)
    for ax, what in ((axes[0], "real part"), (axes[1], "imaginary part")):
        ax.axvline(1.0, color=GREY, linestyle=":", linewidth=1)
        ax.set_xlabel("momentum $k_5$ along the extra time $x_5$ ($m = 1$)")
        ax.set_ylabel(f"{what} of the eigenvalues of $h$")
    axes[0].set_title("oscillation: real frequencies $\\pm w$")
    axes[1].set_title("growth: imaginary frequencies $\\pm i\\kappa$")
    save_figure(fig, "eigenvalue_flow",
                "The 16 eigenvalues of the mode Hamiltonian $h$ for mass $m = 1$ and "
                "only the extra-time momentum $k_5$ (horizontal axis, units of $m$): "
                "their real parts (left, blue) and imaginary parts (right, orange), "
                "vertical axes in units of $m$; each curve carries eight eigenvalues. "
                "For $k_5 < 1$ the eigenvalues are the real numbers $\\pm\\sqrt{1 - "
                "k_5^2}$, which move together and meet at 0 at $k_5 = 1$ (dotted line); "
                "for $k_5 > 1$ they leave the real axis as $\\pm i\\sqrt{k_5^2 - 1}$, "
                "and the waves with $+i\\kappa$ grow like $e^{\\kappa x_4}$.")
    '''),
    md(r"""
    ## 9. Krein inertia of the eigenspaces: the recorded samples

    The next cell defines three functions.

    - `orthonormal_basis(P)` returns an orthonormal basis of the range of a matrix $P$
      by the Gram-Schmidt method: take the columns of $P$ in order, remove from each
      its parts along the basis vectors found so far, and keep it (divided by its
      length) if something is left. The procedure is repeated once to remove rounding
      errors.
    - `eigenspace(m, k, sign)` returns such a basis of the eigenspace of $+w$
      (`sign = +1`) or $-w$ (`sign = -1`), as the range of the projector
      $P_\pm = \frac12(I \pm h/w)$ of Section 4. For $w^2 < 0$ the number $w$ is
      $i\kappa$, and the same formula gives the eigenspaces of $\pm i\kappa$.
    - `krein_inertia(V)` computes the Gram matrix $G = V^\dagger B V$ (entry $(i, j)$ is
      the Krein form of the basis vectors $i$ and $j$) and counts its positive,
      negative and zero eigenvalues (zero means smaller than $10^{-8}$). It also returns
      the smallest size of a nonzero eigenvalue, to show that no eigenvalue is close
      to the borderline $10^{-8}$.
    """),
    code(r'''
    def orthonormal_basis(P):
        """Orthonormal columns that span the range of P (Gram-Schmidt, done twice)."""
        basis = []
        for column in P.T:  # the columns of P, in order
            v = column.astype(complex)
            for _ in range(2):  # the second pass removes rounding errors
                for e in basis:
                    v = v - (e.conj() @ v) * e  # remove the part of v along e
            length = np.sqrt((v.conj() @ v).real)
            if length > 1e-8:  # v is not a combination of the earlier columns
                basis.append(v / length)
        return np.array(basis).T  # the basis vectors as the columns of a matrix


    def eigenspace(m, k, sign):
        """Orthonormal basis of the eigenspace of h for the eigenvalue sign * w."""
        h = mode_hamiltonian(m, k)
        w = np.sqrt(complex(frequency_squared(m, k)))  # w, or i kappa when w^2 < 0
        P = (np.eye(16) + sign * h / w) / 2  # the projector P_+ or P_-
        return orthonormal_basis(P)


    def krein_inertia(V):
        """(positive, negative, zero) eigenvalues of V^dagger B V, and the smallest
        size of a nonzero one (None when all are zero)."""
        G = V.conj().T @ B @ V  # the Krein form on the span of the columns of V
        values = np.linalg.eigvalsh(G)
        nonzero = np.abs(values[np.abs(values) > 1e-8])
        counts = (int(np.sum(values > 1e-8)), int(np.sum(values < -1e-8)),
                  int(np.sum(np.abs(values) <= 1e-8)))
        return counts, (float(nonzero.min()) if nonzero.size else None)
    '''),
    md(r"""
    The Revision pairing record `Revision/pairing/pairing-theory.json` stores eight
    samples (entry `data`, `one_particle_flat`, `samples`): for each a mass $m$, a
    momentum list $(k_1, \dots, k_8)$ (the entry $k_4$ is not used), the frequency $w$
    (written in the notation of the Wolfram Language, for example `Sqrt[2]`), the
    dimensions of the two eigenspaces and their Krein inertia. The next cell reads them,
    recomputes every number, prints one line per sample and checks that everything
    agrees.
    """),
    code(r'''
    pairing = json.loads(repository_file("Revision/pairing/pairing-theory.json")
                         .read_text(encoding="utf-8"))
    samples = pairing["data"]["one_particle_flat"]["samples"]
    all_agree = True
    say("   m  nonzero momenta         w      dims   inertia(+w)  inertia(-w)")
    for sample in samples:
        m_value, k_list = sample["m"], sample["k"]
        k = {a: k_list[a - 1] for a in (1, 2, 3, 5, 6, 7, 8) if k_list[a - 1] != 0}
        # "Sqrt[2]" (Wolfram notation) -> the number sqrt(2)
        w_recorded = float(sp.sympify(sample["w"].replace("Sqrt[", "sqrt(")
                                      .replace("]", ")")))
        w = np.sqrt(frequency_squared(m_value, k))
        found = []
        for sign in (+1, -1):
            V = eigenspace(m_value, k, sign)
            counts, _ = krein_inertia(V)
            found.append((V.shape[1], counts))
        agree = (abs(w - w_recorded) < 1e-12
                 and found[0][0] == sample["dim_plus_w"]
                 and found[1][0] == sample["dim_minus_w"]
                 and list(found[0][1][:2]) == sample["B_inertia_plus_w"]
                 and list(found[1][1][:2]) == sample["B_inertia_minus_w"]
                 and found[0][1][2] == 0 and found[1][1][2] == 0)
        all_agree = all_agree and agree
        momenta = ", ".join(f"k{a}={v}" for a, v in k.items()) or "none"
        say(f"{m_value:4d}  {momenta:22s} {w:7.4f}   {found[0][0]},{found[1][0]}    "
            f"{found[0][1][:2]}       {found[1][1][:2]}")
    check_record(all_agree,
                 "all 8 recorded samples: w, dimensions 8 and 8, Krein inertia (4, 4)",
                 record="Revision/pairing/pairing-theory.json, data one_particle_flat")
    '''),
    md(r"""
    Two more recorded statements. The sympy pairing verifier uses the sample $m = 1$,
    $k_1 = 2$, $k_8 = 2$ (so $w = \sqrt{1 + 4 + 4} = 3$). Its imaginary-frequency samples
    are $m = 1$ with $k_5 = 2$ ($w^2 = -3$) and with $k_1 = 1$, $k_5 = 2$ ($w^2 = -2$):
    there both eigenspaces must be *neutral*, inertia $(0, 0, 8)$. For $m = 1$, $k_5 = 1$
    the frequency is zero: $h^2 = 0$, the range of $h$ has dimension 8, and since
    $(hx)^\dagger B (hy) = x^\dagger h^\dagger B h y = x^\dagger B h^2 y = 0$, the range of
    $h$ is neutral as well. The next cell checks all of this.
    """),
    code(r'''
    sample_3 = {1: 2, 8: 2}
    inertias_3 = [krein_inertia(eigenspace(1, sample_3, s))[0] for s in (+1, -1)]
    report("w for m = 1, k1 = 2, k8 = 2", f"{np.sqrt(frequency_squared(1, sample_3)):.6f}")
    say(f"inertia of the +w and -w eigenspaces: {inertias_3}")
    check_record(inertias_3 == [(4, 4, 0), (4, 4, 0)],
                 "m = 1, k1 = 2, k8 = 2 (w = 3): inertia (4, 4) on both eigenspaces",
                 record="Revision/pairing/reports/python-pairing.json, check "
                        "Q.one_particle_Krein_inertia")
    neutral_ok = True
    for k in ({5: 2}, {1: 1, 5: 2}):
        spaces = [eigenspace(1, k, s) for s in (+1, -1)]
        inertias = [krein_inertia(V)[0] for V in spaces]
        say(f"m = 1, momenta {k}: w^2 = {frequency_squared(1, k)}, dimensions "
            f"{[V.shape[1] for V in spaces]}, inertia {inertias}")
        neutral_ok = neutral_ok and inertias == [(0, 0, 8), (0, 0, 8)]
    h_zero = mode_hamiltonian(1, {5: 1})  # w^2 = 1 - 1 = 0
    rank_h = int(np.linalg.matrix_rank(h_zero))
    nilpotent = np.max(np.abs(h_zero @ h_zero)) < 1e-12  # h^2 = 0
    range_neutral = np.max(np.abs(h_zero.conj().T @ B @ h_zero)) < 1e-12
    say(f"m = 1, k5 = 1: w^2 = 0, h^2 = 0: {nilpotent}, rank of h = {rank_h}, "
        f"range of h neutral: {range_neutral}")
    check_record(neutral_ok and nilpotent and rank_h == 8 and range_neutral,
                 "imaginary and zero frequencies: the eigenspaces are Krein-neutral",
                 record="Revision/pairing/reports/python-pairing.json, check "
                        "Q.one_particle_complex_frequency_Krein_neutral")
    '''),
    md(r"""
    ## 10. Why the inertia is (4, 4) at EVERY real frequency

    Samples are not a proof. The Revision record proves the statement for every real
    frequency in three steps, which the next cells repeat.

    **Step (i).** For real $w > 0$: $P_+^\dagger B P_- = 0$ and $P_+^\dagger B P_+ =
    BP_+$. Line by line, with $P_\pm = \frac12(I \pm h/w)$ and $P_+^\dagger = \frac12(I +
    h^\dagger/w)$ ($w$ is real):

    $$4w^2\,P_+^\dagger B P_- = (wI + h^\dagger)B(wI - h) = w^2 B - wBh + wh^\dagger B -
    h^\dagger B h .$$

    Use $h^\dagger B = Bh$ twice: the two middle terms cancel, and $h^\dagger B h = B h h
    = w^2 B$, so the right-hand side is $w^2B - w^2B = 0$. Hence the two eigenspaces
    are Krein-orthogonal: a wave of frequency $+w$ and one of $-w$ have zero mixed
    Krein form. Since $B$ is invertible and the two eigenspaces together span all 16
    directions, $B$ cannot vanish on either of them (it is *nondegenerate* on each).

    **Step (ii).** In the good sector $Bh = hB$, so $\mathrm{tr}(BP_\pm) = \frac12
    \mathrm{tr}B \pm \frac{1}{2w}\mathrm{tr}(Bh)$, and both traces are 0. The trace of
    $BP_+$ is the sum of the eigenvalues of $B$ on the $+w$ eigenspace (in the good
    sector $B$ maps this eigenspace into itself), each $+1$ or $-1$; a sum of eight
    such numbers is 0 only with four of each: inertia $(4, 4)$.

    **Step (iii).** Turning on the extra-time momenta slowly at fixed $m, k_1, k_2, k_3,
    k_8$ keeps $w^2$ positive as long as $k_t^2 < m^2 + k_s^2$, the projectors change
    continuously, and the Krein form stays nondegenerate on their ranges by step (i).
    An eigenvalue of the Gram matrix could change sign only by passing through 0, which
    nondegeneracy forbids: the inertia stays $(4, 4)$ at every real frequency.

    The next cell checks the identities of steps (i) and (ii) exactly with sympy. The
    letter $w$ is a positive symbol, and after expanding, every $w^2$ is replaced by
    $m^2 + k_s^2 - k_t^2$.
    """),
    code(r'''
    w = sp.Symbol("w", positive=True)
    I16 = sp.eye(16)


    def replace_w_squared(matrix):
        """Expand every entry and replace w^2 by m^2 + k_s^2 - k_t^2."""
        return matrix.applyfunc(lambda e: sp.expand(sp.expand(e).subs(w ** 2, w2_sym)))


    step_i_a = replace_w_squared((w * I16 + h_sym.H) * B_exact * (w * I16 - h_sym))
    step_i_b = replace_w_squared((w * I16 + h_sym.H) * B_exact * (w * I16 + h_sym)
                                 - 2 * w * B_exact * (w * I16 + h_sym))
    check_record(step_i_a == zero and step_i_b == zero,
                 "exact step (i): 4 w^2 P+^dagger B P- = 0 and P+^dagger B P+ = B P+",
                 record="Revision/pairing/reports/python-pairing.json, check "
                        "Q.one_particle_Krein_inertia_proof")
    trace_B_h = sp.expand((B_exact * h_sym).trace())
    say(f"exact: tr B = {B_exact.trace()}, tr(B h) = {trace_B_h}")
    check(B_exact.trace() == 0 and trace_B_h == 0,
          "exact step (ii): tr B = tr(B h) = 0, so tr(B P+) = tr(B P-) = 0")
    '''),
    md(r"""
    Step (iii) is a statement about continuity. The next cell shows it at work: for
    $m = 1$, the space-like momentum $k_1 = 0.5$ and the extra-time momentum $k_5$ from 0
    to 2.5 it computes the Krein inertia of the $+w$ eigenspace. The threshold is
    $k_5 = \sqrt{1.25} \approx 1.118$; points closer than 0.02 to it are skipped (there
    the eigenspaces merge). Below the threshold the inertia must be $(4, 4, 0)$ at every
    point, above it $(0, 0, 8)$. The cell also records the smallest size of a nonzero
    eigenvalue of the Gram matrix: it shrinks towards the threshold but never reaches 0
    before it.
    """),
    code(r'''
    threshold = np.sqrt(1.25)
    scan = [k5 for k5 in np.linspace(0.0, 2.5, 251) if abs(k5 - threshold) > 0.02]
    counts_scan, margins = [], []
    for k5 in scan:
        counts, margin = krein_inertia(eigenspace(1.0, {1: 0.5, 5: k5}, +1))
        counts_scan.append(counts)
        if margin is not None:
            margins.append(margin)
    below = [c for k5, c in zip(scan, counts_scan) if k5 < threshold]
    above = [c for k5, c in zip(scan, counts_scan) if k5 > threshold]
    report("points below and above the threshold", f"{len(below)} and {len(above)}")
    report("smallest nonzero Gram eigenvalue below the threshold", f"{min(margins):.4f}")
    check(set(below) == {(4, 4, 0)} and set(above) == {(0, 0, 8)},
          "scan: inertia (4, 4) at every real frequency, (0, 0, 8) at every imaginary "
          "one")

    counts_array = np.array(counts_scan)  # one row (positive, negative, zero) per k5
    fig, ax = plt.subplots()
    width = 0.0105  # a little wider than the step 0.01 between the k5 values (no gaps)
    # Stacked bars: the blue part (positive directions) starts at 0, the orange part
    # (negative directions) on top of it, the green part (neutral) on top of both.
    ax.bar(scan, counts_array[:, 0], width=width, color=BLUE,
           label="positive charge $u^\\dagger B u > 0$")
    ax.bar(scan, counts_array[:, 1], width=width, bottom=counts_array[:, 0],
           color=ORANGE, label="negative charge $u^\\dagger B u < 0$")
    ax.bar(scan, counts_array[:, 2], width=width,
           bottom=counts_array[:, 0] + counts_array[:, 1], color=GREEN,
           label="neutral (the form vanishes)")
    ax.axvline(threshold, color=GREY, linestyle=":", linewidth=1)
    ax.set_xlabel("momentum $k_5$ along the extra time ($m = 1$, $k_1 = 0.5$)")
    ax.set_ylabel("directions in the $+w$ eigenspace")
    ax.set_yticks(range(0, 9))
    ax.set_ylim(0.0, 10.5)  # room for the legend above the bars
    ax.set_title("Krein inertia of one eigenspace across the threshold")
    ax.legend(loc="upper center", ncol=3, fontsize=8)
    save_figure(fig, "krein_inertia_scan",
                "The Krein inertia of the eigenspace of $+w$ of the mode Hamiltonian "
                "for $m = 1$, $k_1 = 0.5$ and the extra-time momentum $k_5$ from 0 to "
                "2.5 (horizontal axis, units of $m$). Each thin bar splits the eight "
                "independent directions of the eigenspace (vertical axis) into those "
                "of positive charge (blue), negative charge (orange) and zero charge "
                "for every pair (green). Left of the threshold $k_5 = \\sqrt{1.25}$ "
                "(dotted line) the frequency is real and the split is always 4 and 4; "
                "right of it the frequency is imaginary and the whole eigenspace is "
                "neutral: the growing waves carry no charge.")
    '''),
    md(r"""
    ## 11. Three pictures of the Krein form on the eigenvectors

    The next cell puts the 8 basis vectors of the $+w$ eigenspace and the 8 of the $-w$
    eigenspace side by side as the 16 columns of a matrix $W$, and draws the sizes of the
    entries of the Gram matrix $W^\dagger B W$ for three waves:

    - the good-sector sample $m = 2$, $k = (1, 2, 0, 4)$ along $(x_1, x_2, x_3, x_8)$,
      $w = 5$;
    - $m = 2$ with the extra-time momentum $k_5 = 1$: still a real frequency,
      $w = \sqrt3$;
    - $m = 1$, $k_5 = 2$: an imaginary frequency, $w = i\sqrt3$.

    In the first two pictures only the two diagonal $8 \times 8$ blocks are nonzero
    (the eigenspaces are Krein-orthogonal, step (i)); in the third the diagonal blocks
    vanish (each eigenspace is neutral) and only the off-diagonal blocks remain: a
    growing wave has nonzero Krein form only with a decaying one.
    """),
    code(r'''
    cases = [(2, {1: 1, 2: 2, 8: 4}, "$m = 2$, $k = (1, 2, 0, 4)$: $w = 5$"),
             (2, {5: 1}, "$m = 2$, $k_5 = 1$: $w = \\sqrt{3}$"),
             (1, {5: 2}, "$m = 1$, $k_5 = 2$: $w = i\\sqrt{3}$")]
    fig, axes = plt.subplots(1, 3, figsize=(12.0, 4.2))
    block_sizes = []
    for ax, (m_value, k, title) in zip(axes, cases):
        W = np.hstack([eigenspace(m_value, k, +1), eigenspace(m_value, k, -1)])
        gram = np.abs(W.conj().T @ B @ W)  # sizes of the Krein form between columns
        image = draw_matrix(ax, gram, title, cmap=SEQUENTIAL, vmin=0.0, vmax=1.0)
        ax.axhline(7.5, color=GREY, linewidth=1)  # the border between the two
        ax.axvline(7.5, color=GREY, linewidth=1)  # eigenspaces (rows/columns 8 and 9)
        diagonal_blocks = max(gram[:8, :8].max(), gram[8:, 8:].max())
        off_blocks = max(gram[:8, 8:].max(), gram[8:, :8].max())
        block_sizes.append((diagonal_blocks, off_blocks))
        say(f"case {len(block_sizes)}: largest entry in the diagonal blocks "
            f"{diagonal_blocks:.3f}; off-diagonal blocks below 1e-12: {off_blocks < 1e-12}")
    fig.colorbar(image, ax=list(axes), shrink=0.8, label="size of the entry")
    save_figure(fig, "krein_gram_matrices",
                "Sizes of the entries of the Gram matrix $W^\\dagger B W$, where the "
                "first 8 columns of $W$ span the eigenspace of $+w$ and the last 8 that "
                "of $-w$ (horizontal and vertical axes: column and row number; white is "
                "0, dark blue is 1; grey lines separate the two eigenspaces). Left: a "
                "good-sector wave with $w = 5$; middle: a wave with extra-time momentum "
                "and real $w = \\sqrt{3}$; right: a wave with imaginary $w = "
                "i\\sqrt{3}$. For real frequencies only the diagonal blocks are filled: "
                "the two eigenspaces are Krein-orthogonal. For the imaginary frequency "
                "the diagonal blocks are empty: each eigenspace is neutral.")
    check(block_sizes[0][1] < 1e-12 and block_sizes[1][1] < 1e-12
          and block_sizes[2][0] < 1e-12 and block_sizes[2][1] > 0.1,
          "real w: the eigenspaces are Krein-orthogonal; imaginary w: each is neutral")
    '''),
    md(r"""
    ## 12. The universes of masses $+m$ and $-m$

    The pairing theorem T1 of the Revision record relates the field of mass $m$ to the
    field of mass $-m$ through the chirality matrix $\Gamma$. At the one-particle level
    the record proves (statement Q4 of the quantum reading):

    - $\Gamma h_m(k)\Gamma = h_{-m}(k)$, because $\Gamma$ anticommutes with
      $\gamma^{(x_4)}$ and commutes with every product $\gamma^{(x_4)}\gamma^{(x_a)}$;
    - $\gamma^{(x_8)} h_m(k)\gamma^{(x_8)} = h_{-m}(R_8 k)$, where $R_8$ reverses the
      hidden momentum $k_8$.

    Since $\Gamma^2 = I$ and $(\gamma^{(x_8)})^2 = I$, these are *similarity*
    transformations: $h_{-m}$ has exactly the eigenvalues of $h_m$. The one-particle
    spectra of the two universes are IDENTICAL, not opposite. The next cell checks both
    identities exactly.
    """),
    code(r'''
    Gamma_exact = g[8] * g[1] * g[2] * g[3] * g[4] * g[5] * g[6] * g[7]
    h_minus = mode_hamiltonian_exact(-m, k_sym)  # the same momenta, mass -m
    k_reflected = dict(k_sym)
    k_reflected[8] = -k_sym[8]  # R_8: k8 -> -k8
    h_minus_reflected = mode_hamiltonian_exact(-m, k_reflected)
    chirality_ok = (Gamma_exact * h_sym * Gamma_exact - h_minus).applyfunc(
        sp.expand) == zero
    mirror_ok = (g[8] * h_sym * g[8] - h_minus_reflected).applyfunc(sp.expand) == zero
    check_record(Gamma_exact * Gamma_exact == I16 and chirality_ok,
                 "exact: Gamma h_m(k) Gamma = h_-m(k)",
                 record="Revision/pairing/reports/python-pairing.json, check "
                        "Q.one_particle_maps")
    check_record(mirror_ok, "exact: gamma^(x8) h_m(k) gamma^(x8) = h_-m(R_8 k)",
                 record="Revision/pairing/reports/wolfram-pairing.json, check "
                        "Q_one_particle_maps")
    '''),
    md(r"""
    The Revision theory record also states how the good-sector spectrum splits between
    the two eigenspaces of $B$. In the good sector $B$ commutes with $h$, so the
    projector $P_B = \frac12(I + B)$ onto the eigenvalue $+1$ of $B$ (8 directions)
    commutes with $h$, and $h$ acts inside that 8-dimensional space. For the exact
    example $m = 2$, $k = (1, 2, 0, 4)$, $w = 5$, the matrix $P_B h P_B$ must have the
    eigenvalue $+5$ four times, $-5$ four times and $0$ eight times (the 0 belongs to the
    other 8 directions, which $P_B$ removes). The next cell checks this and then draws
    the spectra of $h_m$ and $h_{-m}$ for $m = 2$ against $k_1$ and, at fixed $k_1 = 1$,
    against $m$ from $-3$ to $3$.
    """),
    code(r'''
    h_sample = mode_hamiltonian(2, {1: 1, 2: 2, 8: 4})
    P_B = (np.eye(16) + B) / 2  # projector onto the eigenvalue +1 of B
    sector_values = np.round(np.linalg.eigvals(P_B @ h_sample @ P_B).real, 10)
    multiplicities = {v: int(np.sum(sector_values == v)) for v in (5.0, -5.0, 0.0)}
    say(f"eigenvalues of P_B h P_B and how often each occurs: {multiplicities}")
    check_record(multiplicities == {5.0: 4, -5.0: 4, 0.0: 8},
                 "good sector, m = 2, k = (1, 2, 0, 4): on B = +1 energies +5, -5 (4 each)",
                 record="Revision/theory/reports/python-field-theory.json, check "
                        "good_sector_spectrum_and_B_sectors")

    k1_values = np.linspace(0.0, 4.0, 41)
    plus_spectra = [np.sort(np.linalg.eigvals(mode_hamiltonian(2.0, {1: x})).real)
                    for x in k1_values]
    minus_spectra = [np.sort(np.linalg.eigvals(mode_hamiltonian(-2.0, {1: x})).real)
                     for x in k1_values]
    mass_values = np.linspace(-3.0, 3.0, 61)
    mass_spectra = [np.sort(np.linalg.eigvals(mode_hamiltonian(x, {1: 1.0})).real)
                    for x in mass_values]
    difference = np.max(np.abs(np.array(plus_spectra) - np.array(minus_spectra)))
    report("largest difference between the spectra of m = 2 and m = -2", f"{difference:.1e}")
    check(difference < 1e-10, "numerical: the spectra of h_m and h_-m coincide")

    fig, axes = plt.subplots(1, 2, figsize=(10.0, 4.0))
    axes[0].plot(k1_values, np.array(plus_spectra)[:, [0, 15]], color=BLUE, linewidth=2)
    axes[0].plot(k1_values, np.array(minus_spectra)[:, [0, 15]], "o", color=ORANGE,
                 markersize=5, fillstyle="none")
    axes[0].plot([], [], color=BLUE, linewidth=2, label="$m = +2$ (line)")
    axes[0].plot([], [], "o", color=ORANGE, fillstyle="none", label="$m = -2$ (circles)")
    axes[0].set_xlabel("momentum $k_1$ (with $m = \\pm 2$)")
    axes[0].set_ylabel("eigenvalues $\\pm w$ of $h$")
    axes[0].set_title("same spectrum for $+m$ and $-m$")
    axes[0].legend(loc="center left")
    axes[1].plot(mass_values, np.array(mass_spectra)[:, [0, 15]], color=GREEN,
                 linewidth=2)
    axes[1].set_xlabel("mass $m$ (with $k_1 = 1$)")
    axes[1].set_ylabel("eigenvalues $\\pm\\sqrt{m^2 + k_1^2}$ of $h$")
    axes[1].set_title("the spectrum is even in $m$")
    save_figure(fig, "plus_minus_mass_spectra",
                "Left: the eigenvalues $\\pm w = \\pm\\sqrt{m^2 + k_1^2}$ of the mode "
                "Hamiltonian for $m = +2$ (blue lines) and $m = -2$ (orange circles), "
                "computed separately, against the momentum $k_1$ (horizontal axis); "
                "the circles sit exactly on the lines. Right: the same eigenvalues at "
                "$k_1 = 1$ against the mass $m$ from $-3$ to $3$ (horizontal axis); "
                "the green curves are mirror images in the vertical axis $m = 0$. "
                "Vertical axes: eigenvalue (same units as $m$). The universes of "
                "masses $+m$ and $-m$ have identical, not opposite, one-particle "
                "spectra.")
    '''),
    md(r"""
    ## 13. The last check

    The last cell checks that all six figure files exist in the folder
    Revision/textbook/figures and prints the number of checks that passed.
    """),
    code(r'''
    for name in ("10a_1_gamma4_c_and_b.png", "10a_2_frequency_squared.png",
                 "10a_3_eigenvalue_flow.png", "10a_4_krein_inertia_scan.png",
                 "10a_5_krein_gram_matrices.png", "10a_6_plus_minus_mass_spectra.png"):
        check(output_file(f"{FIGURE_FOLDER}/{name}").is_file(),
              f"the figure file {name} exists")
    all_checks_passed()
    '''),
    md(r"""
    ## 14. What this notebook showed

    - PROVED (exactly, with sympy, for all real $m$ and momenta): the mode Hamiltonian
      of a plane wave obeys $h^2 = w^2 I_{16}$ with $w^2 = m^2 + k_1^2 + k_2^2 + k_3^2 +
      k_8^2 - k_5^2 - k_6^2 - k_7^2$, and $Bh = h^\dagger B$, so the Krein form
      $u^\dagger B u$ (the charge) of every wave is conserved, also of a growing one;
      $h$ is Hermitian and commutes with $B$ exactly in the good sector.
    - PROVED (steps (i) and (ii) exactly, step (iii) by continuity; flat 4+4 space or
      in the frozen-coefficient model, an ASSUMPTION): every eigenspace of a REAL
      frequency has Krein inertia
      $(4, 4)$; every eigenspace of an imaginary
      frequency, and the range of $h$ at zero frequency, is Krein-neutral. So the
      positive and negative charges are mixed half and half at every real frequency;
      the good sector does not remove this indefiniteness of the one-particle waves.
    - PROVED (exactly): $\Gamma h_m\Gamma = h_{-m}$ and $\gamma^{(x_8)}h_m(k)\gamma^{(x_8)}
      = h_{-m}(R_8k)$: the universes of masses $+m$ and $-m$ have identical
      one-particle spectra.
    - REPRODUCED: the properties of $B$ (signature $(8, 8)$), the eight recorded
      samples of the pairing record, the recorded Krein inertia and neutrality samples,
      and the good-sector split $+5$ (4 times), $-5$ (4 times) on $B = +1$.
    - These are statements about one-particle waves in flat 4+4 space or in the
      frozen-coefficient model, which leaves out the hidden-direction terms of the
      author's field equation (an ASSUMPTION). How a positive quantum state space is
      built from them (and where that is possible) is the subject of the next notebooks
      of this chapter.
    """),
]

if __name__ == "__main__":
    raise SystemExit(run_builder(__file__))
