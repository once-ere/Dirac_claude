#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
"""Builder of Notebook 10f, "The Krein structure along the deflating history"
(textbook "Universes in Pairs", chapter 10: canonical quantisation in 4+4, the Krein
space and the good sector).

The notebook Revision/textbook/notebooks/10f_krein_along_history.ipynb is BUILT from
this file by Revision/textbook/tools/nbkit.py (never edit the .ipynb by hand):

    python Revision/textbook/tools/nbkit.py build \
        Revision/textbook/notebooks/src/10f_krein_along_history.py --date YYYY-MM-DD
    python Revision/textbook/tools/nbkit.py check \
        Revision/textbook/notebooks/src/10f_krein_along_history.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools"))
from nbkit import code, md, run_builder  # noqa: E402

FACTS = {
    "id": "10f",
    "name": "10f_krein_along_history",
    "title": "The Krein structure along the deflating history",
    "purpose": (
        "Along the prescribed history a4 = A H x4, b4 = b4(0) e to the beta a4 of the "
        "Revision Kohn-Sham record (A = H = m = 1, beta = 4/3, b4(0) = 1) it takes the "
        "scale factors of the corrected metric of the author from the Revision theory "
        "record and turns the coordinate momenta of a wave along the hidden direction "
        "x0, along x1 and along the extra time x5 into frame momenta (the hidden and the "
        "extra-time ones grow like e to the a4/3, because the hidden direction shrinks "
        "together with the deflating extra times; the one along x1 shrinks), proves "
        "exactly that the local mode Hamiltonian of every instant squares to w(x4)^2 "
        "times the identity, that w^2 = m^2 + q1^2 e to the -2 a4 minus (e to the 2 a4 "
        "over b4) times D with D = (sin^2 z) to the -1/6 times q5^2 minus tan^2 z times "
        "q0^2, so that a wave turns from oscillation to growth exactly when D is "
        "positive (always without hidden momentum), and that its departure from "
        "Hermiticity and its mixing of the two sectors of B grow like e to the a4/3; it "
        "computes the onset time of growth, follows the eigenvalues and the Krein "
        "inertia of the eigenspaces through it ((4, 4) before, Krein-neutral after), "
        "maps which waves still oscillate at each time and which waves ever grow, shows "
        "that the good sector keeps a Hermitian mode Hamiltonian, the Krein inertia "
        "(4, 4) and a positive instantaneous energy at every time, checks that the "
        "masses +m and -m have the same onset, and draws five teaching figures."
    ),
    "records": [
        ["Revision/kohn_sham/results/parameters.json",
         "the prescribed history a4 = A H x4, b4 = b4(0) e to the beta a4 (A = 1, "
         "beta = 4/3, b4(0) = 1, H = 1, m = 1), its status as a prescribed background "
         "and the five slices a4,0 of the Kohn-Sham record (read)"],
        ["Revision/theory/field-theory.json",
         "formula vielbein_diagonal, the scale factors of the eight directions of the "
         "corrected metric (read and reproduced)"],
        ["Revision/algebra/gammas.json", "the author's gamma matrices (read)"],
        ["Revision/theory/reports/python-field-theory.json",
         "checks mode_hamiltonian_B_selfadjoint_dispersion, extra_time_modes_grow and "
         "good_sector_spectrum_and_B_sectors (reproduced along the history)"],
        ["Revision/pairing/reports/python-pairing.json",
         "checks Q.one_particle_Krein_inertia_proof, "
         "Q.one_particle_complex_frequency_Krein_neutral and Q.one_particle_maps "
         "(reproduced along the history)"],
    ],
    "packages": ["numpy", "sympy", "matplotlib"],
    "needs_rust": [],
    "expected_seconds": 20,
    "timeout_seconds": 300,
    "files_written": [
        "Revision/textbook/figures/10f.captions.json",
        "Revision/textbook/figures/10f_1_hermiticity_defect.png",
        "Revision/textbook/figures/10f_2_eigenvalues_along_history.png",
        "Revision/textbook/figures/10f_3_inertia_along_history.png",
        "Revision/textbook/figures/10f_4_onset_map.png",
        "Revision/textbook/figures/10f_5_good_sector_energies.png",
    ],
    "final_lines": [
        "PASS the figure file 10f_5_good_sector_energies.png exists",
        "ALL 21 CHECKS PASSED (notebook 10f)",
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
    ],
}

CELLS = [
    md(r"""
    ## 1. What this notebook computes

    The earlier notebooks of this chapter studied one wave of dirac16complex with
    momenta that do not change. In the author's metric (the corrected metric of
    2026-10-16) they DO change: the three extra times $x_5, x_6, x_7$ deflate
    exponentially (scale factor $e^{-a_4}b_4^{1/2}(\sin^2 z)^{1/12}$), the hidden
    direction $x_0$ shrinks together with them (scale factor $e^{-a_4}b_4^{1/2}|\cot
    z|$), and 3-space inflates (scale factor $e^{a_4}$, no warp). On the prescribed
    history of the Revision record, $a_4 = AHx_4$ and $b_4 = b_4(0)e^{\beta a_4}$ with
    $\beta = 4/3$, the factor $e^{-a_4}b_4^{1/2}$ is proportional to $e^{-a_4/3}$. A
    wave with a fixed coordinate momentum along an extra time therefore has a frame
    momentum that GROWS like $e^{a_4/3}$, and so does a wave with a fixed coordinate
    momentum along the hidden direction. This notebook follows the quantum structure of
    the chapter along this history. It

    - reads the scale factors from the Revision theory record and turns coordinate
      momenta into frame momenta;
    - proves exactly that the mode Hamiltonian $h(x_4)$ of every instant satisfies
      $h(x_4)^2 = w(x_4)^2I_{16}$ with $w^2 = m^2 + q_1^2e^{-2a_4} - (e^{2a_4}/b_4)D$
      and $D = (\sin^2 z)^{-1/6}q_5^2 - \tan^2 z\,q_0^2$, and that its departure from
      Hermiticity and its mixing of the two eigenspaces of $B$ both grow like
      $e^{a_4/3}$;
    - shows that a wave turns from oscillation into growth exactly when $D > 0$: always
      for a wave with extra-time momentum and no hidden momentum, never for a wave
      whose hidden momentum is large enough;
    - computes the time at which a wave starts to grow, the *onset time*;
    - follows the eigenvalues and the Krein inertia of the eigenspaces through that
      time: inertia $(4, 4)$ before, Krein-neutral after;
    - maps which waves still have a real frequency at each time, and which waves ever
      grow;
    - shows that the good sector (no extra-time momentum) keeps a Hermitian mode
      Hamiltonian, the inertia $(4, 4)$ and a positive energy for every quantum at
      every time;
    - checks that the masses $+m$ and $-m$ have the same onset of growth;
    - draws five teaching figures.

    Status of the inputs: the history is a PRESCRIBED BACKGROUND (it is not solved from
    the field equations for $a_4$ and $b_4$), and every statement here is made in the
    *local-frame model*: at each instant the coefficients of the wave equation are
    evaluated at that instant and at one hidden position, as the Revision record does
    for its statement that every extra-time mode eventually grows.
    """),
    md(r"""
    ## 3. The words used in this notebook

    - **Scale factor** $f_a$: the factor by which the author's metric stretches the
      coordinate $x_a$; a coordinate distance $dx_a$ has the proper length $f_a\,dx_a$.
      For 3-space $f = e^{a_4}$, for the extra times $f = e^{-a_4}b_4^{1/2}(\sin^2
      z)^{1/12}$, for the hidden direction $f = e^{-a_4}b_4^{1/2}\cot z$ (with $z =
      6Hx_0$; its sign does not matter here), for the time $f = 1$.
    - **Prescribed history**: the time dependence $a_4 = AHx_4$, $b_4 =
      b_4(0)e^{\beta a_4}$ with $A = 1$, $\beta = 4/3$, $b_4(0) = 1$; as $x_4$ grows,
      3-space inflates like $e^{a_4}$, and the extra times and the hidden direction
      shrink like $e^{-a_4/3}$.
    - **Coordinate momentum** $q_a$ and **frame momentum** $k_a$: a wave $e^{iq_ax_a}$
      has the coordinate momentum $q_a$; measured with proper lengths its momentum is
      $k_a = q_a/f_a$, the frame momentum.
    - **Hidden position** $z$: the value of $z = 6Hx_0$ at which the coefficients are
      taken, between 0 and the fold $z = \pi/2$ where the two halves of a cell meet.
      The Kohn-Sham record measures it by $y = \ln(\sin z)/(6H)$, so that $(\sin^2
      z)^{1/12} = e^{Hy}$; the fold is $y = 0$. At the fold $(\sin^2 z)^{1/12} = 1$ and
      $\tan z$ is infinite, so waves with a hidden momentum are taken at $z < \pi/2$.
    - **Local-frame model**: at the instant $x_4$ and the position $z$ the wave equation
      is written with the coefficients of that instant and that position; the change of
      the coefficient $\tan z$ along $x_0$ and the spin-connection term are left out
      (the notebook on the curved good sector studies them).
    - **Mode Hamiltonian** $h$: the $16 \times 16$ matrix with $i\,du/dx_4 = hu$; its
      eigenvalues $\pm w$ are the frequencies.
    - **Growth number** $D$: $D = (\sin^2 z)^{-1/6}q_5^2 - \tan^2 z\,q_0^2$, built from
      the coordinate momenta of the extra time and of the hidden direction.
    - **Onset time** $x_4^\ast$: the time at which $w^2$ changes from positive (the wave
      oscillates) to negative (the wave grows).
    - **Hermitian part, anti-Hermitian part**: every matrix is $h = h_H + h_A$ with
      $h_H = \frac12(h + h^\dagger)$ Hermitian and $h_A = \frac12(h - h^\dagger)$
      anti-Hermitian ($h_A^\dagger = -h_A$).
    - **Size of a matrix (spectral norm)**: the largest factor by which the matrix
      stretches the length of a column; in code `np.linalg.norm(M, 2)`.
    - **Krein inertia, Krein-neutral**: as in the first notebook of this chapter, the
      numbers of positive, negative and zero eigenvalues of the Krein form $u^\dagger Bv$
      on a subspace; neutral means that the form vanishes on it.
    - **Good sector**: waves without extra-time momentum, $q_5 = q_6 = q_7 = 0$.
    - **Instantaneous**: computed with the coefficients of one instant, as if they did
      not change.
    """),
    md(r"""
    ## 4. The physical and mathematical situation

    **The wave equation of one instant, line by line.** The field equation of
    dirac16complex in the author's metric (Revision theory record, formula
    `field_equation`, $U = 0$) is

    $$e^{a_4}b_4^{-1/2}\tan z\,\gamma^{(x_0)}\partial_0\Psi + e^{-a_4}\sum_{i=1}^{3}
    \gamma^{(x_i)}\partial_i\Psi + \gamma^{(x_4)}\partial_4\Psi +
    \frac{e^{a_4}}{b_4^{1/2}(\sin^2 z)^{1/12}}\sum_{t=5}^{7}\gamma^{(x_t)}\partial_t\Psi
    + c_g\gamma^{(x_0)}\Psi + v_g\gamma^{(x_4)}\Psi = m\Psi ,$$

    with $c_g = \frac32He^{a_4}b_4^{-1/2}$ and $v_g = b_4'/b_4 - a_4'/2$. Each
    derivative $\partial_a$ is divided by the scale factor $f_a$ of its direction. In
    the local-frame model take a wave $\Psi = e^{a_4/2}b_4^{-1}u(x_4)\,e^{i(q_0x_0 +
    q_1x_1 + q_5x_5)}$ at one hidden position, and leave out the term
    $c_g\gamma^{(x_0)}\Psi$ and the change of $\tan z$ along $x_0$. The factor
    $e^{a_4/2}b_4^{-1}$ changes at the rate $-v_g$, so it removes the term
    $v_g\gamma^{(x_4)}\Psi$ exactly. Then $\partial_0$ becomes $iq_0$, $\partial_1$
    becomes $iq_1$ and $\partial_5$ becomes $iq_5$:

    $$ik_0\gamma^{(x_0)}u + ik_1\gamma^{(x_1)}u + \gamma^{(x_4)}\frac{du}{dx_4} +
    ik_5\gamma^{(x_5)}u = mu$$

    with the frame momenta

    $$k_0 = q_0e^{a_4}b_4^{-1/2}\tan z,\qquad k_1 = q_1e^{-a_4},\qquad
    k_5 = q_5e^{a_4}b_4^{-1/2}(\sin^2 z)^{-1/12} .$$

    Multiply from the left by $\gamma^{(x_4)}$, use $(\gamma^{(x_4)})^2 = -1$, solve for
    $du/dx_4$ and multiply by $i$ (exactly the steps of the first notebook of this
    chapter):

    $$i\frac{du}{dx_4} = h(x_4)\,u,\qquad h(x_4) = -im\gamma^{(x_4)} -
    k_0\gamma^{(x_4)}\gamma^{(x_0)} - k_1\gamma^{(x_4)}\gamma^{(x_1)} -
    k_5\gamma^{(x_4)}\gamma^{(x_5)} .$$

    On the history $e^{a_4}b_4^{-1/2} = b_4(0)^{-1/2}e^{ra_4}$ with $r = 1 - \beta/2 =
    1/3$. So $k_1 = q_1e^{-AHx_4}$ SHRINKS (3-space inflates), while $k_5$ and $k_0$
    both GROW like $e^{AHx_4/3}$ (the extra times deflate, and the hidden direction
    shrinks with them).

    **The squared frequency.** By the identity $h^2 = w^2I_{16}$ of the first notebook
    of this chapter (space-like momenta enter with $+$, extra-time momenta with $-$), at
    every instant

    $$w^2 = m^2 + k_0^2 + k_1^2 - k_5^2 .$$

    Insert the frame momenta. The two growing ones carry the same factor
    $e^{2a_4}/b_4$:

    $$k_5^2 - k_0^2 = \frac{e^{2a_4}}{b_4}\big((\sin^2 z)^{-1/6}q_5^2 - \tan^2 z\,
    q_0^2\big) = \frac{e^{2a_4}}{b_4}\,D ,$$

    so that

    $$w^2 = m^2 + q_1^2e^{-2a_4} - \frac{e^{2a_4}}{b_4}\,D .$$

    **Which waves grow, line by line.** On the history $e^{2a_4}/b_4 =
    e^{2ra_4}/b_4(0)$ grows without bound and $e^{-2a_4}$ falls to 0.

    - If $D \leq 0$, the last term $-(e^{2a_4}/b_4)D$ is never negative, so $w^2 \geq m^2
      > 0$ at every time: the wave oscillates for ever.
    - If $D > 0$, the derivative $dw^2/dx_4 = -2AHq_1^2e^{-2a_4} -
      2rAH(e^{2a_4}/b_4)D$ is negative, so $w^2$ falls all the time, and because the
      last term grows without bound, $w^2$ becomes negative after a finite time, exactly
      once: the onset time $x_4^\ast$. After it the wave grows.

    So a wave eventually grows exactly when $D > 0$. Without hidden momentum ($q_0 =
    0$) every wave with $q_5 \neq 0$ has $D > 0$: every extra-time wave grows, as the
    Revision record states. A hidden momentum with $\tan^2 z\,q_0^2 \geq (\sin^2
    z)^{-1/6}q_5^2$ keeps the wave oscillating: the hidden direction is space-like, its
    frame momentum grows at the same rate as the extra-time one and enters $w^2$ with
    the opposite sign.

    **The onset time.** Write $X = e^{2ra_4} > 0$. With $r = 1/3$, $e^{-2a_4} =
    X^{-1/r} = X^{-3}$, and $w^2 = 0$ reads $m^2 + q_1^2X^{-3} - (D/b_4(0))X = 0$.
    Multiply by $X^3$:

    $$\frac{D}{b_4(0)}X^4 - m^2X^3 - q_1^2 = 0 .$$

    For $D > 0$ the left side of the equation before the multiplication falls strictly
    as $X$ grows, from $+\infty$ to $-\infty$, so this quartic has exactly one positive
    root $X^\ast$, and $x_4^\ast = \ln X^\ast/(2rAH)$. For $q_1 = 0$ the root is
    $X^\ast = m^2b_4(0)/D$. At the fold $z = \pi/2$, without hidden momentum, $D =
    q_5^2$, and with the record's values $x_4^\ast = 3\ln(m/q_5)$: the onset comes when
    the growing frame momentum $k_5$ reaches the mass.

    **Hermitian and anti-Hermitian parts.** The matrices $-i\gamma^{(x_4)}$,
    $\gamma^{(x_4)}\gamma^{(x_0)}$ and $\gamma^{(x_4)}\gamma^{(x_1)}$ are Hermitian and
    commute with $B$, while $\gamma^{(x_4)}\gamma^{(x_5)}$ is anti-Hermitian and
    anticommutes with $B$ (first notebook of this chapter). Hence
    $h_A = -k_5\gamma^{(x_4)}\gamma^{(x_5)}$, and since $(\gamma^{(x_4)}
    \gamma^{(x_5)})^2 = -(\gamma^{(x_4)})^2(\gamma^{(x_5)})^2 = -I$,

    $$h_A^\dagger h_A = -h_A^2 = k_5^2 I_{16} .$$

    So $h_A$ stretches every column by exactly the factor $k_5$: the size of the
    anti-Hermitian part is $k_5$, which grows like $e^{a_4/3}$. In the same way
    $Bh - hB = 2Bh_A$ has the size $2k_5$ ($B$ keeps lengths, because $B^\dagger B =
    B^2 = I$). Both vanish at every time in the good sector, $q_5 = 0$; the hidden
    momentum does not enter them.

    **Krein inertia at each instant.** At each instant $h(x_4)$ is the mode Hamiltonian
    of the first notebook of this chapter with real frame momenta, so the Revision
    proof applies instant by instant: while $w^2 > 0$ each eigenspace has Krein inertia
    $(4, 4)$; once $w^2 < 0$ each eigenspace is Krein-neutral.
    """),
    md(r"""
    ## 5. The prescribed history of the Revision record

    The next cell reads the parameters of the Revision Kohn-Sham record: the constant
    $H$, the mass $m$, the history constants $A$, $\beta$ and $b_4(0)$ and the five
    slices $a_{4,0}$ at which that record computes its instantaneous Kohn-Sham states.
    It prints the first words of the record's own statement of the status of the
    history and checks the values $A = H = m = 1$, $\beta = 4/3$, $b_4(0) = 1$. It also
    defines `check_record` (the PASS line and the line naming the reproduced Revision
    record are printed in one piece, because Jupyter sends printed text to the screen in
    pieces whose boundaries depend on timing) and the colours of the figures.
    Before it checks anything, `check_record` asks the helper `record_says_pass` whether
    the cited record still says PASS: for a record name of the form
    `<report file>, check <check name>` it opens that report (each file once, kept in
    the dictionary `REPORT_CHECKS`) and stops the notebook with an error unless a check
    of that name exists there with the verdict PASS; a record name without `, check `
    names a data entry that the notebook reads and compares itself.
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


    BLUE, ORANGE, GREEN, GREY = "#2a78d6", "#eb6834", "#1baf7a", "#52514e"
    parameters = json.loads(repository_file(
        "Revision/kohn_sham/results/parameters.json").read_text(encoding="utf-8"))
    physics = parameters["physics"]
    H = physics["H"]  # the author's constant H
    mass = physics["m"]  # the mass m
    A = physics["historyA"]  # a4 = A H x4
    beta = physics["historyBeta"]  # b4 = b4(0) e^(beta a4)
    b4_start = physics["historyB4AtZero"]  # b4(0)
    slices = physics["slicesA4"]  # the values a4,0 of the record
    say("status of the history: "
        + parameters["conventions"]["history"].split(": ")[0] + ".")
    say(f"history: A = {A}, beta = {beta:.6f}, b4(0) = {b4_start}, H = {H}, m = {mass}")
    say(f"slices a4,0 of the Kohn-Sham record: {slices}")
    check_record(A == 1.0 and abs(beta - 4 / 3) < 1e-12 and b4_start == 1.0
                 and H == 1.0 and mass == 1.0,
                 "the history a4 = A H x4, b4 = b4(0) e^(beta a4): A = 1, beta = 4/3, "
                 "b4(0) = 1, H = m = 1",
                 record="Revision/kohn_sham/results/parameters.json, physics.historyA, "
                        "physics.historyBeta, physics.historyB4AtZero, physics.H, "
                        "physics.m")
    rate = 1 - beta / 2  # r = 1 - beta/2 = 1/3: e^a4 b4^(-1/2) = b4(0)^(-1/2) e^(r a4)


    def a4_of(x4):
        """The prescribed history a4 = A H x4."""
        return A * H * x4


    def b4_of(x4):
        """The prescribed history b4 = b4(0) e^(beta a4)."""
        return b4_start * np.exp(beta * a4_of(x4))
    '''),
    md(r"""
    ## 6. Frame momenta from the scale factors of the record

    The Revision theory record `Revision/theory/field-theory.json` stores the scale
    factors $f_a$ of the eight directions (formula key `vielbein_diagonal`) in the
    notation of the Wolfram Language, for example
    `(Sqrt[b4[x4]]*(Sin[6*H*x0]^2)^(1/12))/E^a4[x4]`. The next cell translates this text
    into sympy (`Sqrt[b4[x4]]` becomes `sqrt(b4)`, `E^a4[x4]` becomes `exp(a4)`,
    `Sin[6*H*x0]` becomes `sin(z)`, `Cot[6*H*x0]` becomes `cot(z)`, `^` becomes `**`,
    curly brackets become square brackets), and checks EXACTLY that it equals
    $e^{-a_4}b_4^{1/2}\cot z$ for $x_0$, $e^{a_4}$ for $x_1, x_2, x_3$, 1 for $x_4$ and
    $e^{-a_4}b_4^{1/2}(\sin^2 z)^{1/12}$ for the extra times. (sympy writes
    $(\sin^2 z)^{1/12}$ as $|\sin z|^{1/6}$, the same positive number.) Then it defines
    the frame momenta $k_0 = q_0/f_0$, $k_1 = q_1/f_1$ and $k_5 = q_5/f_5$ at the time
    $x_4$ and the hidden position $z$; the default position is the fold $z = \pi/2$
    (only for waves without hidden momentum).
    """),
    code(r'''
    theory = json.loads(repository_file("Revision/theory/field-theory.json").read_text(
        encoding="utf-8"))
    text = next(f["wl"] for f in theory["formulas"] if f["key"] == "vielbein_diagonal")
    a4_symbol, b4_symbol = sp.symbols("a4 b4", positive=True)
    z_symbol = sp.Symbol("z", real=True)
    translated = (text.replace("Sqrt[b4[x4]]", "sqrt(b4)").replace("E^a4[x4]", "exp(a4)")
                  .replace("Sin[6*H*x0]", "sin(z)").replace("Cot[6*H*x0]", "cot(z)")
                  .replace("^", "**").replace("{", "[").replace("}", "]"))
    f_record = sp.sympify(translated, locals={"a4": a4_symbol, "b4": b4_symbol,
                                              "z": z_symbol})
    shrink_symbol = sp.exp(-a4_symbol) * sp.sqrt(b4_symbol)  # e^-a4 b4^(1/2)
    twelfth_root = (sp.sin(z_symbol) ** 2) ** sp.Rational(1, 12)  # (sin^2 z)^(1/12)
    f_expected = ([shrink_symbol * sp.cot(z_symbol)] + [sp.exp(a4_symbol)] * 3
                  + [sp.Integer(1)] + [shrink_symbol * twelfth_root] * 3)  # x0, ..., x7
    same = all(sp.simplify(r - e) == 0 for r, e in zip(f_record, f_expected))
    say(f"scale factor of x0: {f_record[0]}")
    say(f"scale factor of x1: {f_record[1]}")
    say(f"scale factor of x5: {f_record[5]}")
    check_record(len(f_record) == 8 and same,
                 "the record's scale factors: e^-a4 b4^(1/2) cot z, e^a4 (x3), 1, "
                 "e^-a4 b4^(1/2) (sin^2 z)^(1/12) (x3)",
                 record="Revision/theory/field-theory.json, formula vielbein_diagonal")
    FOLD = np.pi / 2  # the fold z = pi/2 (y = 0), where (sin^2 z)^(1/12) = 1


    def frame_momenta(x4, q0, q1, q5, z=FOLD):
        """(k0, k1, k5) of the wave exp(i (q0 x0 + q1 x1 + q5 x5)) at the time x4 and
        the hidden position z (z < pi/2 when q0 is not 0)."""
        shrink = np.exp(-a4_of(x4)) * np.sqrt(b4_of(x4))  # e^-a4 b4^(1/2) = e^(-a4/3)
        k0 = q0 * np.tan(z) / shrink  # q0 / f_0: grows, the hidden direction shrinks
        k1 = q1 / np.exp(a4_of(x4))  # q1 / f_1: shrinks, 3-space inflates
        k5 = q5 / (shrink * (np.sin(z) ** 2) ** (1 / 12))  # q5 / f_5: grows
        return k0, k1, k5
    '''),
    md(r"""
    ## 7. The mode Hamiltonian of each instant, exactly

    The next cell reads the gammas, builds $B$ and the chirality $\Gamma$, and defines
    the mode Hamiltonian `mode_hamiltonian(x4, q0, q1, q5, z, m)` of Section 4 as a
    numpy matrix and `w_squared` for $w^2$. Then it repeats the algebra of Section 4
    EXACTLY with sympy, with symbols for $m$, $q_0$, $q_1$, $q_5$, $H$, $b_4(0)$, the
    time $x_4$, $t = \tan z$ and $\sigma = (\sin^2 z)^{-1/12}$ (so the statements hold
    at every instant and every hidden position), on the history with the record's $A =
    1$ and $\beta = 4/3$ (checked in Section 5):

    - $h(x_4)^2 = (m^2 + k_0^2 + k_1^2 - k_5^2)I_{16}$;
    - $w^2 = m^2 + q_1^2e^{-2a_4} - (e^{2a_4}/b_4)D$ with $D = \sigma^2q_5^2 -
      t^2q_0^2$, and $dw^2/dx_4 = -2Hq_1^2e^{-2a_4} - \frac23H(e^{2a_4}/b_4)D$ (the
      two facts of the growth criterion);
    - the anti-Hermitian part is $h_A = -k_5\gamma^{(x_4)}\gamma^{(x_5)}$,
      $h_A^\dagger h_A = k_5^2I_{16}$ and $Bh - hB = 2Bh_A$;
    - in the good sector ($q_5 = 0$) $h$ is Hermitian and commutes with $B$ at every
      time.
    """),
    code(r'''
    fixture = json.loads(repository_file("Revision/algebra/gammas.json").read_text(
        encoding="utf-8"))
    gamma = {a: np.array(fixture["gamma"][a], dtype=float) for a in range(8)}
    C = gamma[0] @ gamma[1] @ gamma[2] @ gamma[3]  # the author's sigma16
    B = -1j * (C @ gamma[4])  # B = -i C gamma^(x4)
    Gamma = (gamma[0] @ gamma[1] @ gamma[2] @ gamma[3] @ gamma[4] @ gamma[5]
             @ gamma[6] @ gamma[7])  # the chirality matrix


    def mode_hamiltonian(x4, q0, q1, q5, z=FOLD, m=mass):
        """h(x4) = -i m g4 - k0 g4 g0 - k1 g4 g1 - k5 g4 g5 at the time x4."""
        k0, k1, k5 = frame_momenta(x4, q0, q1, q5, z)
        return (-1j * m * gamma[4] - k0 * (gamma[4] @ gamma[0])
                - k1 * (gamma[4] @ gamma[1]) - k5 * (gamma[4] @ gamma[5]))


    def w_squared(x4, q0, q1, q5, z=FOLD, m=mass):
        """w^2 = m^2 + k0^2 + k1^2 - k5^2 at the time x4."""
        k0, k1, k5 = frame_momenta(x4, q0, q1, q5, z)
        return m ** 2 + k0 ** 2 + k1 ** 2 - k5 ** 2


    g = {a: sp.Matrix(fixture["gamma"][a]) for a in range(8)}  # exact gammas
    B_exact = -sp.I * g[0] * g[1] * g[2] * g[3] * g[4]
    m_s, q0_s, q1_s, q5_s = sp.symbols("m q0 q1 q5", real=True)
    x4_s, H_s, b0_s, t_s, sigma_s = sp.symbols("x4 H b0 t sigma", positive=True)
    a4_s = H_s * x4_s  # the history a4 = A H x4 with the record's A = 1
    b4_s = b0_s * sp.exp(sp.Rational(4, 3) * a4_s)  # b4 = b4(0) e^(4 a4/3)
    shrink_s = b0_s ** sp.Rational(1, 2) * sp.exp(-a4_s / 3)  # = e^-a4 b4^(1/2)
    k0_s = q0_s * t_s / shrink_s  # t = tan z
    k1_s = q1_s * sp.exp(-a4_s)
    k5_s = q5_s * sigma_s / shrink_s  # sigma = (sin^2 z)^(-1/12)
    h_s = (-sp.I * m_s * g[4] - k0_s * g[4] * g[0] - k1_s * g[4] * g[1]
           - k5_s * g[4] * g[5])
    zero = sp.zeros(16, 16)
    w2_s = m_s ** 2 + k0_s ** 2 + k1_s ** 2 - k5_s ** 2
    shrink_ok = sp.simplify(shrink_s ** 2 - sp.exp(-2 * a4_s) * b4_s) == 0
    square_ok = (h_s * h_s - w2_s * sp.eye(16)).applyfunc(sp.expand) == zero
    D_s = sigma_s ** 2 * q5_s ** 2 - t_s ** 2 * q0_s ** 2  # the growth number D
    w2_form = m_s ** 2 + q1_s ** 2 * sp.exp(-2 * a4_s) - sp.exp(2 * a4_s) / b4_s * D_s
    form_ok = sp.simplify(w2_s - w2_form) == 0
    slope_ok = sp.simplify(sp.diff(w2_form, x4_s) - (
        -2 * H_s * q1_s ** 2 * sp.exp(-2 * a4_s)
        - sp.Rational(2, 3) * H_s * sp.exp(2 * a4_s) / b4_s * D_s)) == 0
    h_A = ((h_s - h_s.H) / 2).applyfunc(sp.expand)  # the anti-Hermitian part
    part_ok = (h_A + k5_s * g[4] * g[5]).applyfunc(sp.expand) == zero
    size_ok = (h_A.H * h_A - k5_s ** 2 * sp.eye(16)).applyfunc(sp.expand) == zero
    mixing_ok = (B_exact * h_s - h_s * B_exact - 2 * B_exact * h_A).applyfunc(
        sp.expand) == zero
    good = h_s.subs(q5_s, 0)  # the good sector
    good_ok = ((good - good.H).applyfunc(sp.expand) == zero
               and (B_exact * good - good * B_exact).applyfunc(sp.expand) == zero)
    check_record(shrink_ok and square_ok,
                 "exact: h(x4)^2 = (m^2 + k0^2 + k1^2 - k5^2) I at every instant",
                 record="Revision/theory/reports/python-field-theory.json, check "
                        "mode_hamiltonian_B_selfadjoint_dispersion")
    check(form_ok and slope_ok,
          "exact: w^2 = m^2 + q1^2 e^(-2 a4) - (e^(2 a4)/b4) D and its falling slope")
    check(part_ok and size_ok and mixing_ok,
          "exact: h_A = -k5 g4 g5, h_A^dagger h_A = k5^2 I, B h - h B = 2 B h_A")
    check_record(good_ok,
                 "exact: good sector, h(x4) Hermitian and commuting with B at all times",
                 record="Revision/theory/reports/python-field-theory.json, check "
                        "good_sector_spectrum_and_B_sectors")
    '''),
    md(r"""
    ## 8. Departure from Hermiticity and mixing of the two sectors of $B$

    The next cell measures, with numbers, the size of the anti-Hermitian part $h_A$ and
    of the commutator $Bh - hB$ (`np.linalg.norm(M, 2)`, the largest stretching factor)
    for three extra-time momenta $q_5 = 0.01$, $0.05$, $0.2$ (with $q_1 = 0.5$, no
    hidden momentum, at the fold $z = \pi/2$) at the times $x_4 = 0, 1.5, \dots, 18$,
    compares them with the formulas $k_5 = q_5e^{a_4}b_4^{-1/2} = q_5e^{x_4/3}$ and
    $2k_5$ of Section 4, and draws them on a logarithmic scale, where an exponential is
    a straight line. In the good sector both sizes are 0 at every time, and a hidden
    momentum (here $q_0 = 0.3$ at $z = \pi/4$) does not change the size of $h_A$.
    """),
    code(r'''
    times = np.linspace(0.0, 18.0, 13)  # 0, 1.5, ..., 18
    curve_times = np.linspace(0.0, 18.0, 241)
    measured, worst = {}, 0.0
    for q5 in (0.01, 0.05, 0.2):
        sizes = []
        for x4 in times:
            h = mode_hamiltonian(x4, 0.0, 0.5, q5)
            h_anti = (h - h.conj().T) / 2
            sizes.append((np.linalg.norm(h_anti, 2), np.linalg.norm(B @ h - h @ B, 2)))
            k5 = frame_momenta(x4, 0.0, 0.5, q5)[2]
            worst = max(worst, abs(sizes[-1][0] - k5) / k5,
                        abs(sizes[-1][1] - 2 * k5) / (2 * k5))
        measured[q5] = np.array(sizes)
    good_sizes = [np.linalg.norm(mode_hamiltonian(x4, 0.0, 0.5, 0.0)
                                 - mode_hamiltonian(x4, 0.0, 0.5, 0.0).conj().T, 2)
                  for x4 in times]
    hidden = mode_hamiltonian(6.0, 0.3, 0.5, 0.05, z=np.pi / 4)  # with q0 = 0.3
    hidden_size = np.linalg.norm((hidden - hidden.conj().T) / 2, 2)
    k5_hidden = frame_momenta(6.0, 0.3, 0.5, 0.05, z=np.pi / 4)[2]
    report("largest relative difference from k5 and 2 k5", f"{worst:.1e}")
    check(worst < 1e-12 and max(good_sizes) == 0.0
          and abs(hidden_size - k5_hidden) < 1e-12 * k5_hidden,
          "sizes of h_A and of B h - h B are k5 = q5 e^(x4/3) and 2 k5; 0 if q5 = 0")

    fig, axes = plt.subplots(1, 2, figsize=(11.0, 4.2), sharey=True)
    for q5, colour in ((0.01, BLUE), (0.05, ORANGE), (0.2, GREEN)):
        k5_curve = frame_momenta(curve_times, 0.0, 0.5, q5)[2]
        axes[0].plot(curve_times, k5_curve, color=colour, linewidth=2,
                     label=f"$q_5 = {q5}$")
        axes[0].plot(times, measured[q5][:, 0], "o", color=colour, markersize=5)
        axes[1].plot(curve_times, 2 * k5_curve, color=colour, linewidth=2,
                     label=f"$q_5 = {q5}$")
        axes[1].plot(times, measured[q5][:, 1], "o", color=colour, markersize=5)
    for ax in axes:
        ax.set_yscale("log")
        ax.axhline(mass, color=GREY, linestyle=":", linewidth=1)
        ax.set_xlabel("time $x_4$ (units of $1/m$)")
        ax.legend(loc="lower right", fontsize=8)
    axes[0].set_ylabel("size (units of $m$)")
    axes[0].set_title("anti-Hermitian part $h_A$: size $k_5 = q_5e^{x_4/3}$")
    axes[1].set_title("mixing of the $B$ sectors: size of $Bh - hB$")
    save_figure(fig, "hermiticity_defect",
                "Along the prescribed history $a_4 = x_4$, $b_4 = e^{4x_4/3}$ ($H = m = "
                "1$), at the fold $z = \\pi/2$, for a wave with the coordinate momenta "
                "$q_1 = 0.5$ and $q_5 = 0.01$, $0.05$, $0.2$ (blue, orange, green): "
                "left, the size of the anti-Hermitian part of the mode Hamiltonian; "
                "right, the size of the commutator $Bh - hB$, which mixes the two "
                "eigenspaces of $B$. Horizontal axes: the time $x_4$ in units of $1/m$; "
                "vertical axes: the size in units of $m$, logarithmic. Dots: measured "
                "matrices; lines: the formulas $k_5 = q_5e^{a_4}b_4^{-1/2} = "
                "q_5e^{x_4/3}$ and $2k_5$; dotted grey line: the mass. The straight "
                "lines show exponential growth: the deflation of the extra times drives "
                "every wave with extra-time momentum ever further from a Hermitian, "
                "sector-preserving evolution. In the good sector, $q_5 = 0$, both sizes "
                "are 0 at every time.")
    '''),
    md(r"""
    ## 9. One wave through the onset: eigenvalues and Krein inertia

    The next cell defines the onset time of Section 4: it computes $D$, solves the
    quartic $(D/b_4(0))X^4 - m^2X^3 - q_1^2 = 0$ with `np.roots` (the roots of a
    polynomial from its coefficients, highest power first), keeps the one positive real
    root and returns $x_4^\ast = \ln X^\ast/(2rAH)$. It checks this against a numerical
    root search for 48 waves with $D > 0$ (three hidden positions with a fitting hidden
    momentum, four values of $q_1$, four of $q_5$). The search is *bisection*: start
    with an interval of times in which $w^2$ changes sign and halve it 200 times, always
    keeping the half in which the sign changes. It also checks the short form
    $x_4^\ast = 3\ln(m/q_5)$ for $q_1 = q_0 = 0$ at the fold.
    """),
    code(r'''
    def growth_number(q0, q5, z=FOLD):
        """D = (sin^2 z)^(-1/6) q5^2 - tan^2 z q0^2 (the hidden term only if q0 != 0)."""
        hidden_term = np.tan(z) ** 2 * q0 ** 2 if q0 != 0 else 0.0
        return (np.sin(z) ** 2) ** (-1 / 6) * q5 ** 2 - hidden_term


    def onset_time(q0, q1, q5, z=FOLD):
        """The time at which w^2 = 0, for D > 0: the one positive root X of
        (D/b4(0)) X^4 - m^2 X^3 - q1^2 = 0, with X = e^(2 r a4)."""
        D = growth_number(q0, q5, z)
        roots = np.roots([D / b4_start, -mass ** 2, 0.0, 0.0, -q1 ** 2])
        positive = [x.real for x in roots if abs(x.imag) <= 1e-9 * abs(x) and x.real > 0]
        if len(positive) != 1:
            raise ValueError("the quartic must have exactly one positive root")
        return np.log(positive[0]) / (2 * rate * A * H)


    def bisection(q0, q1, q5, z=FOLD, low=-40.0, high=80.0):
        """The time at which w^2 changes sign, by halving [low, high] 200 times."""
        for _ in range(200):
            middle = (low + high) / 2
            if w_squared(middle, q0, q1, q5, z) > 0:  # still oscillating: onset later
                low = middle
            else:
                high = middle
        return (low + high) / 2


    waves = [(q0, q1, q5, z)
             for z, q0 in ((FOLD, 0.0), (np.pi / 4, 0.005), (np.pi / 6, 0.005))
             for q1 in (0.0, 0.5, 1.0, 3.0) for q5 in (0.01, 0.05, 0.1, 0.4)]
    positive_D = all(growth_number(q0, q5, z) > 0 for q0, q1, q5, z in waves)
    worst = max(abs(onset_time(*wave) - bisection(*wave)) for wave in waves)
    report("largest difference, onset time from the quartic minus bisection (48 waves)",
           f"{worst:.1e}")
    check(positive_D and worst < 1e-9
          and abs(onset_time(0.0, 0.0, 0.05) - 3 * np.log(1 / 0.05)) < 1e-12,
          "the onset time from the quartic agrees with bisection; q1 = q0 = 0: "
          "3 ln(m / q5)")
    onset = onset_time(0.0, 0.5, 0.05)  # the wave followed below
    report("onset time of the wave q1 = 0.5, q5 = 0.05 at the fold", f"{onset:.6f}")
    '''),
    md(r"""
    The Revision theory record names the exact sample $m = 1$ with the frame momentum
    $k_5 = 2$ (and no other momentum): the eigenvalues are $\pm i\sqrt3$, eight of each.
    Along the history this sample is an INSTANT: a wave with $q_1 = 0$ and $q_5 = 0.05$
    at the fold has $k_5 = 0.05\,e^{x_4/3} = 2$ at $x_4 = 3\ln 40$. The next cell checks
    that the mode Hamiltonian of that instant has exactly the recorded eigenvalues, and
    that the same wave at $x_4 = 0$ (where $k_5 = 0.05$) still oscillates.
    """),
    code(r'''
    instant = np.log(2 / 0.05 * np.sqrt(b4_start)) / (rate * A * H)  # k5 = 2: 3 ln 40
    k5_instant = frame_momenta(instant, 0.0, 0.0, 0.05)[2]
    eigenvalues = np.linalg.eigvals(mode_hamiltonian(instant, 0.0, 0.0, 0.05))
    plus = int(np.sum(np.abs(eigenvalues - 1j * np.sqrt(3)) < 1e-9))
    minus = int(np.sum(np.abs(eigenvalues + 1j * np.sqrt(3)) < 1e-9))
    early = np.linalg.eigvals(mode_hamiltonian(0.0, 0.0, 0.0, 0.05))
    report("the time 3 ln 40 and the frame momentum k5 there",
           f"{instant:.6f} and {k5_instant:.12f}")
    report("eigenvalues +i sqrt(3) and -i sqrt(3), how many", f"{plus} and {minus}")
    largest_imaginary = np.max(np.abs(early.imag))  # 0 up to rounding: oscillation
    report("largest imaginary part of an eigenvalue at x4 = 0", f"{largest_imaginary:.1e}")
    check_record(abs(k5_instant - 2) < 1e-12 and (plus, minus) == (8, 8)
                 and largest_imaginary < 1e-12,
                 "the recorded sample m = 1, k5 = 2 (+-i sqrt 3) is reached at x4 = 3 ln 40",
                 record="Revision/theory/reports/python-field-theory.json, check "
                        "extra_time_modes_grow")
    '''),
    md(r"""
    The next cell follows the wave $q_1 = 0.5$, $q_5 = 0.05$ (no hidden momentum, at the
    fold) from $x_4 = 0$ to $x_4 = 15$: it computes the 16 eigenvalues of $h(x_4)$ at
    251 times, compares them with $\pm w(x_4)$ (eight each) away from the onset (where
    the matrix cannot be diagonalised and numerical eigenvalues are inaccurate), and
    draws their real and imaginary parts.
    """),
    code(r'''
    scan_times = np.linspace(0.0, 15.0, 251)
    real_parts, imaginary_parts, worst = [], [], 0.0
    for x4 in scan_times:
        eigenvalues = np.linalg.eigvals(mode_hamiltonian(x4, 0.0, 0.5, 0.05))
        real_parts.append(np.sort(eigenvalues.real))
        imaginary_parts.append(np.sort(eigenvalues.imag))
        w2 = w_squared(x4, 0.0, 0.5, 0.05)
        if abs(w2) > 0.05:  # away from the onset
            w = np.sqrt(complex(w2))  # real, or i kappa after the onset
            predicted = np.array([w] * 8 + [-w] * 8)
            worst = max(worst,
                        np.max(np.abs(np.sort(eigenvalues.real) - np.sort(predicted.real))),
                        np.max(np.abs(np.sort(eigenvalues.imag) - np.sort(predicted.imag))))
    report("largest difference from +-w(x4) away from the onset", f"{worst:.1e}")
    check(worst < 1e-10, "at every instant the eigenvalues of h(x4) are +-w(x4), 8 each")

    fig, axes = plt.subplots(1, 2, figsize=(10.0, 4.0), sharex=True)
    axes[0].plot(scan_times, np.array(real_parts), color=BLUE, linewidth=2)
    axes[1].plot(scan_times, np.array(imaginary_parts), color=ORANGE, linewidth=2)
    for ax, what in ((axes[0], "real part"), (axes[1], "imaginary part")):
        ax.axvline(onset, color=GREY, linestyle=":", linewidth=1)
        ax.set_xlabel("time $x_4$ (units of $1/m$)")
        ax.set_ylabel(f"{what} of the eigenvalues (units of $m$)")
    axes[0].set_title("oscillation before the onset")
    axes[1].set_title("growth after the onset")
    save_figure(fig, "eigenvalues_along_history",
                "The 16 eigenvalues of the mode Hamiltonian $h(x_4)$ of a wave with the "
                "coordinate momenta $q_1 = 0.5$, $q_5 = 0.05$ (no hidden momentum, at "
                "the fold $z = \\pi/2$) along the prescribed history $a_4 = x_4$, $b_4 "
                "= e^{4x_4/3}$ ($H = m = 1$): real parts (left, blue) and imaginary "
                "parts (right, orange), each curve carrying eight eigenvalues; "
                "horizontal axes: the time $x_4$ in units of $1/m$, vertical axes in "
                "units of $m$. Before the onset time $x_4^\\ast = 8.987$ (dotted line) "
                "the eigenvalues are the real frequencies $\\pm w(x_4)$, which shrink "
                "as the extra-time frame momentum grows; at the onset they meet at 0 "
                "and then move onto the imaginary axis as $\\pm i\\kappa(x_4)$, and the "
                "growth rate $\\kappa$ keeps increasing.")
    '''),
    md(r"""
    The next cell computes the Krein inertia of the eigenspace of $+w$ (for $w^2 < 0$:
    of $+i\kappa$) at the same 251 times, with the projector and Gram-matrix method of
    the first notebook of this chapter, skipping the times closer than 0.1 to the
    onset. The Revision proof says: $(4, 4, 0)$ at every time before the onset,
    $(0, 0, 8)$ (neutral) at every time after it. The cell checks this and draws it.
    """),
    code(r'''
    def orthonormal_basis(P):
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


    def eigenspace(h, w2, sign):
        """Orthonormal basis of the eigenspace of sign * w of h (w = sqrt(w2))."""
        w = np.sqrt(complex(w2))
        return orthonormal_basis((np.eye(16) + sign * h / w) / 2)


    def krein_inertia(V):
        """(positive, negative, zero) eigenvalues of the Gram matrix V^dagger B V."""
        values = np.linalg.eigvalsh(V.conj().T @ B @ V)
        return (int(np.sum(values > 1e-8)), int(np.sum(values < -1e-8)),
                int(np.sum(np.abs(values) <= 1e-8)))


    kept = [x4 for x4 in scan_times if abs(x4 - onset) > 0.1]
    inertias = [krein_inertia(eigenspace(mode_hamiltonian(x4, 0.0, 0.5, 0.05),
                                         w_squared(x4, 0.0, 0.5, 0.05), +1))
                for x4 in kept]
    before = {c for x4, c in zip(kept, inertias) if x4 < onset}
    after = {c for x4, c in zip(kept, inertias) if x4 > onset}
    say(f"inertia before the onset: {sorted(before)}; after the onset: {sorted(after)}")
    check_record(before == {(4, 4, 0)},
                 "every instant before the onset: inertia (4, 4) (real frequency)",
                 record="Revision/pairing/reports/python-pairing.json, check "
                        "Q.one_particle_Krein_inertia_proof")
    check_record(after == {(0, 0, 8)},
                 "every instant after the onset: the eigenspace is Krein-neutral",
                 record="Revision/pairing/reports/python-pairing.json, check "
                        "Q.one_particle_complex_frequency_Krein_neutral")

    counts = np.array(inertias)
    fig, ax = plt.subplots()
    width = 0.0615  # a little wider than the step 0.06 between the times (no gaps)
    ax.bar(kept, counts[:, 0], width=width, color=BLUE,
           label="positive charge $u^\\dagger B u > 0$")
    ax.bar(kept, counts[:, 1], width=width, bottom=counts[:, 0], color=ORANGE,
           label="negative charge $u^\\dagger B u < 0$")
    ax.bar(kept, counts[:, 2], width=width, bottom=counts[:, 0] + counts[:, 1],
           color=GREEN, label="neutral")
    ax.axvline(onset, color=GREY, linestyle=":", linewidth=1)
    ax.set_xlabel("time $x_4$ (units of $1/m$)")
    ax.set_ylabel("directions in the $+w$ eigenspace")
    ax.set_yticks(range(0, 9))
    ax.set_ylim(0.0, 10.5)  # room for the legend above the bars
    ax.set_title("Krein inertia of one wave along the deflating history")
    ax.legend(loc="upper center", ncol=3, fontsize=8)
    save_figure(fig, "inertia_along_history",
                "The Krein inertia of the eigenspace of $+w$ of the mode Hamiltonian "
                "of the wave $q_1 = 0.5$, $q_5 = 0.05$ (no hidden momentum, at the fold) "
                "at each time $x_4$ of the prescribed history $a_4 = x_4$, $b_4 = "
                "e^{4x_4/3}$ (horizontal axis, units of $1/m$). Each thin bar splits the "
                "eight directions of the eigenspace (vertical axis) into positive "
                "charge (blue), negative charge (orange) and neutral (green). Before "
                "the onset time $x_4^\\ast = 8.987$ (dotted line) the split is 4 and 4 "
                "at every instant; after it the whole eigenspace is neutral. The "
                "deflation of the extra times moves the wave from the first kind to the "
                "second at a definite time.")
    '''),
    md(r"""
    ## 10. Which waves still oscillate, and which waves ever grow: the onset map

    The next cell draws two maps. The left one is for waves without hidden momentum
    ($q_1 = 0.5$, at the fold): it computes the sign of $w^2$ on a grid of 241 times
    from 0 to 24 and 121 extra-time momenta $q_5$ from $10^{-3}$ to 1 (equally spaced
    in $\log_{10} q_5$), checks that the sign agrees everywhere with the onset time
    ($w^2 > 0$ exactly when $x_4 < x_4^\ast(q_5)$), computes the Krein inertia directly
    at the grid points of every fourth momentum and every 60th time (skipping those
    closer than 0.15 to the onset), and draws the map with the onset curve and the five
    slices $a_{4,0}$ of the Kohn-Sham record. For every $q_5 > 0$ the onset time is
    finite: no extra-time wave without hidden momentum keeps a real frequency for ever.

    The right map is for waves WITH hidden momentum, at the hidden position $z = \pi/4$
    ($\tan z = 1$, $(\sin^2 z)^{-1/6} = 2^{1/6}$, so $D = 2^{1/6}q_5^2 - q_0^2$), with
    $q_1 = 0.5$, on a grid of 101 by 101 coordinate momenta $q_0$ and $q_5$ from 0 to 1.
    Where $D > 0$ it computes the onset time and checks that $w^2$ changes sign there;
    where $D \leq 0$ it checks that $w^2 \geq m^2$ at all 241 times: the criterion of
    Section 4 on 10201 waves.
    """),
    code(r'''
    map_times = np.linspace(0.0, 24.0, 241)
    exponents = np.linspace(-3.0, 0.0, 121)  # log10 of q5
    q5_values = 10.0 ** exponents
    real_frequency = np.array([w_squared(map_times, 0.0, 0.5, q5) > 0
                               for q5 in q5_values])  # rows: q5, columns: x4
    onsets = np.array([onset_time(0.0, 0.5, q5) for q5 in q5_values])
    agree = np.array_equal(real_frequency, map_times[None, :] < onsets[:, None])
    sampled, sample_ok = 0, True
    for i in range(0, 121, 4):
        for j in range(0, 241, 60):
            x4, q5 = map_times[j], q5_values[i]
            if abs(x4 - onsets[i]) < 0.15:
                continue  # too close to the onset
            w2 = w_squared(x4, 0.0, 0.5, q5)
            found = krein_inertia(eigenspace(mode_hamiltonian(x4, 0.0, 0.5, q5), w2, +1))
            sample_ok = sample_ok and found == ((4, 4, 0) if w2 > 0 else (0, 0, 8))
            sampled += 1
    report("grid points sampled for the inertia", sampled)
    report("onset time for q5 = 0.001 and for q5 = 1",
           f"{onsets[0]:.4f} and {onsets[-1]:.4f}")
    check(agree and sample_ok and np.all(np.isfinite(onsets)),
          "the map agrees with the onset; (4, 4) before it, neutral after it")

    plane = np.linspace(0.0, 1.0, 101)  # q0 (columns) and q5 (rows) from 0 to 1
    quarter = np.pi / 4  # the hidden position of the right map: tan z = 1
    onset_plane = np.full((101, 101), np.nan)  # NaN: the wave never grows
    criterion_ok = True
    for i, q5 in enumerate(plane):
        for j, q0 in enumerate(plane):
            if growth_number(q0, q5, quarter) > 0:  # D > 0: an onset must exist
                t = onset_time(q0, 0.5, q5, quarter)
                onset_plane[i, j] = t
                criterion_ok = criterion_ok and (
                    w_squared(t - 0.01, q0, 0.5, q5, quarter) > 0
                    > w_squared(t + 0.01, q0, 0.5, q5, quarter))
            else:  # D <= 0: the wave must oscillate at every time
                criterion_ok = criterion_ok and bool(np.all(
                    w_squared(map_times, q0, 0.5, q5, quarter) >= mass ** 2))
    growing = int(np.sum(np.isfinite(onset_plane)))
    report("waves of the right map with D > 0 (they grow) and D <= 0 (they never grow)",
           f"{growing} and {101 * 101 - growing}")
    check(criterion_ok,
          "a wave grows exactly when D = (sin^2 z)^(-1/6) q5^2 - tan^2 z q0^2 > 0")

    from matplotlib.colors import ListedColormap  # a colour scale with chosen colours

    fig, axes = plt.subplots(1, 2, figsize=(12.0, 4.8))
    ax = axes[0]
    ax.pcolormesh(map_times, exponents, real_frequency.astype(float),
                  cmap=ListedColormap(["#f6c9b5", "#bcd6f5"]), vmin=0, vmax=1,
                  shading="nearest")
    inside = onsets <= map_times[-1]  # the part of the onset curve inside the map
    ax.plot(onsets[inside], exponents[inside], color=GREY, linewidth=2,
            label="onset time $x_4^\\ast$")
    ax.set_xlim(map_times[0], map_times[-1])
    for a4_slice in slices:
        ax.axvline(a4_slice / (A * H), color=GREEN, linestyle="--", linewidth=1)
    ax.plot([], [], "--", color=GREEN, label="slices $a_{4,0}$ of the Kohn-Sham record")
    ax.text(3.0, -2.6, "real frequency:\ninertia (4, 4)", color=BLUE, fontsize=9)
    ax.text(15.0, -0.6, "imaginary frequency:\nKrein-neutral", color=ORANGE, fontsize=9)
    ax.set_xlabel("time $x_4$ (units of $1/m$)")
    ax.set_ylabel("$\\log_{10}$ of the extra-time momentum $q_5$")
    ax.set_title("Which waves still oscillate? ($q_0 = 0$, $q_1 = 0.5$)")
    ax.legend(loc="lower right", fontsize=8)
    ax.grid(False)
    ax = axes[1]
    ax.pcolormesh(plane, plane, np.isnan(onset_plane).astype(float),
                  cmap=ListedColormap(["#ffffff", "#bcd6f5"]), vmin=0, vmax=1,
                  shading="nearest")  # light blue: never grows
    image = ax.pcolormesh(plane, plane, np.minimum(onset_plane, 24.0), cmap="Oranges_r",
                          vmin=0.0, vmax=24.0, shading="nearest")
    ax.plot(plane, plane * 2 ** (-1 / 12), color=GREY, linewidth=2,
            label="$D = 0$: $q_5 = 2^{-1/12}q_0$")
    ax.set_xlim(0.0, 1.0)
    ax.set_ylim(0.0, 1.0)
    ax.text(0.55, 0.12, "D < 0: never grows", color=BLUE, fontsize=9)
    ax.set_xlabel("hidden coordinate momentum $q_0$ (units of $m$)")
    ax.set_ylabel("extra-time coordinate momentum $q_5$ (units of $m$)")
    ax.set_title("Which waves ever grow? ($z = \\pi/4$, $q_1 = 0.5$)")
    ax.legend(loc="upper left", fontsize=8)
    ax.grid(False)
    fig.colorbar(image, ax=ax, label="onset time $x_4^\\ast$ (24 or later: palest)")
    save_figure(fig, "onset_map",
                "Left: waves without hidden momentum, $q_1 = 0.5$, $q_5$ from $10^{-3}$ "
                "to 1 (vertical axis: $\\log_{10}q_5$), at the fold, along the history "
                "$a_4 = x_4$, $b_4 = e^{4x_4/3}$ (horizontal axis: the time $x_4$, units "
                "of $1/m$): light blue where the frequency is real (inertia (4, 4)), "
                "light orange where it is imaginary (Krein-neutral, growth); grey "
                "curve: the onset time; green dashed lines: the five slices $a_{4,0}$ "
                "of the Kohn-Sham record. Right: waves with the coordinate momenta $q_0$ "
                "(horizontal axis) and $q_5$ (vertical axis), $q_1 = 0.5$, at $z = "
                "\\pi/4$: where $D = 2^{1/6}q_5^2 - q_0^2 > 0$ (above the grey line) "
                "the colour is the onset time, darker for earlier; where $D \\leq 0$ "
                "(light blue) the wave never grows. Without hidden momentum every "
                "extra-time wave grows; a large enough hidden momentum prevents it.")
    '''),
    md(r"""
    ## 11. The good sector along the history

    In the good sector ($q_5 = 0$) the mode Hamiltonian of every instant is Hermitian
    and commutes with $B$ (Section 7), with the energies $\pm E(x_4)$,

    $$E(x_4) = \sqrt{m^2 + k_0^2 + k_1^2} = \sqrt{m^2 + q_1^2e^{-2a_4} +
    q_0^2\tan^2 z\,e^{2a_4}/b_4} .$$

    Without hidden momentum it falls towards $m$ as 3-space inflates and its frame
    momentum shrinks; with a hidden momentum it eventually grows like $e^{a_4/3}$,
    because the hidden direction shrinks. In both cases it is real and positive. At
    each instant the positive Fock space of the previous notebooks can be built with
    the coefficients of that instant (an *instantaneous* Fock space): the filled sea has
    the value $\sum_s v_s^\dagger hv_s = -8E(x_4)$, and a particle and an antiparticle
    have the normal-ordered energies $u_s^\dagger hu_s = +E(x_4)$ and $-v_s^\dagger
    hv_s = +E(x_4)$. The next cell checks, at the five slices of the Kohn-Sham record,
    for four momenta $q_1 = 0.5, 1, 2, 4$ (no hidden momentum, at the fold) and for the
    wave $q_0 = 0.5$, $q_1 = 1$ at $z = \pi/4$: $h$ Hermitian, $Bh = hB$, eight
    eigenvalues $+E$ and eight $-E$, the Krein inertia $(4, 4)$ of both eigenspaces, the
    sea value $-8E$ and the quantum energies $+E$. Then it draws $E(x_4)$ and the sea
    value. (In this local-frame model the term $c_g\gamma^{(x_0)}$ is left out; the
    notebook on the curved good sector shows what it does.)
    """),
    code(r'''
    good_waves = [(0.0, q1, FOLD) for q1 in (0.5, 1.0, 2.0, 4.0)] + [(0.5, 1.0, np.pi / 4)]
    slice_ok, table = True, []
    for q0, q1, z in good_waves:
        for a4_slice in slices:
            x4 = a4_slice / (A * H)  # the time of the slice
            h = mode_hamiltonian(x4, q0, q1, 0.0, z)
            E = np.sqrt(w_squared(x4, q0, q1, 0.0, z))
            U_plus = eigenspace(h, E ** 2, +1)  # the 8 particle columns u_s
            V_minus = eigenspace(h, E ** 2, -1)  # the 8 antiparticle columns v_s
            sea = sum((v.conj() @ h @ v).real for v in V_minus.T)
            particle = [(u.conj() @ h @ u).real for u in U_plus.T]
            antiparticle = [-(v.conj() @ h @ v).real for v in V_minus.T]
            slice_ok = (slice_ok and np.allclose(h, h.conj().T) and np.allclose(B @ h, h @ B)
                        and U_plus.shape[1] == 8 and V_minus.shape[1] == 8
                        and krein_inertia(U_plus) == (4, 4, 0)
                        and krein_inertia(V_minus) == (4, 4, 0)
                        and abs(sea + 8 * E) < 1e-12
                        and np.allclose(particle, E) and np.allclose(antiparticle, E))
            table.append((q0, q1, a4_slice, E, sea))
    say("q0    q1    a4,0    E(x4)      sea value -8E")
    for q0, q1, a4_slice, E, sea in table:
        if q1 == 4.0 or q0 == 0.5:  # print two of the five waves
            say(f"{q0:3.1f}   {q1:3.1f}   {a4_slice:3.1f}   {E:9.6f}   {sea:11.6f}")
    check_record(slice_ok,
                 "good sector at all 5 slices: Hermitian, [B, h] = 0, +-E, (4, 4), sea -8E",
                 record="Revision/theory/reports/python-field-theory.json, check "
                        "good_sector_spectrum_and_B_sectors")

    energy_times = np.linspace(0.0, 6.0, 241)
    fig, axes = plt.subplots(1, 2, figsize=(11.0, 4.2))
    styles = [(BLUE, "-"), (ORANGE, "-"), (GREEN, "-"), (GREY, "-"), (ORANGE, "--")]
    for (q0, q1, z), (colour, line) in zip(good_waves, styles):
        E_curve = np.sqrt(w_squared(energy_times, q0, q1, 0.0, z))
        label = f"$q_1 = {q1}$" if q0 == 0 else f"$q_0 = {q0}$, $q_1 = {q1}$, $z = \\pi/4$"
        axes[0].plot(energy_times, E_curve, line, color=colour, linewidth=2, label=label)
        axes[1].plot(energy_times, -8 * E_curve, line, color=colour, linewidth=2,
                     label=label)
        dots = [(a4_slice, E, sea) for p0, p1, a4_slice, E, sea in table
                if (p0, p1) == (q0, q1)]
        axes[0].plot([d[0] for d in dots], [d[1] for d in dots], "o", color=colour)
        axes[1].plot([d[0] for d in dots], [d[2] for d in dots], "o", color=colour)
    axes[0].axhline(mass, color=GREY, linestyle=":", linewidth=1)
    axes[1].axhline(-8 * mass, color=GREY, linestyle=":", linewidth=1)
    axes[0].set_ylabel("energy $E(x_4)$ of one quantum (units of $m$)")
    axes[1].set_ylabel("value $-8E(x_4)$ of the filled sea (units of $m$)")
    axes[0].set_title("particles and antiparticles: $+E(x_4) > 0$")
    axes[1].set_title("the instantaneous vacuum")
    for ax in axes:
        ax.set_xlabel("time $x_4$ (units of $1/m$)")
        ax.legend(fontsize=8)
    save_figure(fig, "good_sector_energies",
                "The good sector along the prescribed history $a_4 = x_4$, $b_4 = "
                "e^{4x_4/3}$ ($H = m = 1$) for the coordinate momenta $q_1 = 0.5$, 1, "
                "2, 4 without hidden momentum (blue, orange, green, grey, at the fold) "
                "and for $q_0 = 0.5$, $q_1 = 1$ at $z = \\pi/4$ (orange dashed); "
                "horizontal axes: the time $x_4$ in units of $1/m$. Left: the "
                "normal-ordered energy $E(x_4) = \\sqrt{m^2 + k_0^2 + k_1^2}$ of one "
                "particle or one antiparticle of the instantaneous Fock space; without "
                "hidden momentum it falls towards the mass $m$ (dotted line) as 3-space "
                "inflates, with hidden momentum it rises again because the hidden "
                "direction shrinks; right: the value $-8E(x_4)$ of the filled sea. "
                "Vertical axes in units of $m$. Dots: computed from the eigenvectors at "
                "the five slices of the Kohn-Sham record. In the good sector every "
                "quantum has a positive energy at every time, and the Krein inertia "
                "stays (4, 4).")
    '''),
    md(r"""
    ## 12. The universes of masses $+m$ and $-m$ along the history

    At every instant the mode Hamiltonian of the history is a mode Hamiltonian of the
    first notebook of this chapter, so the identity $\Gamma h_m\Gamma = h_{-m}$ of the
    Revision pairing record holds at every time ($\Gamma$ anticommutes with
    $\gamma^{(x_4)}$ and commutes with $\gamma^{(x_4)}\gamma^{(x_0)}$,
    $\gamma^{(x_4)}\gamma^{(x_1)}$ and $\gamma^{(x_4)}\gamma^{(x_5)}$). The mass enters
    $w^2$ only as $m^2$, so the two universes have the same frequencies, the same onset
    time and the same Krein inertia at every instant. The next cell checks the identity
    at 25 times from 0 to 18 for the wave $q_0 = 0.02$, $q_1 = 0.5$, $q_5 = 0.05$ at
    $z = \pi/4$ (which has $D > 0$ and its onset at about $x_4 = 9.04$), and that the
    eigenvalues for $+m$ and $-m$ agree.
    """),
    code(r'''
    pair_ok, worst = True, 0.0
    for x4 in np.linspace(0.0, 18.0, 25):
        h_plus = mode_hamiltonian(x4, 0.02, 0.5, 0.05, z=np.pi / 4, m=mass)
        h_minus = mode_hamiltonian(x4, 0.02, 0.5, 0.05, z=np.pi / 4, m=-mass)
        pair_ok = pair_ok and np.allclose(Gamma @ h_plus @ Gamma, h_minus, atol=1e-14)
        values_plus = np.linalg.eigvals(h_plus)
        values_minus = np.linalg.eigvals(h_minus)
        # compare the sorted real parts and the sorted imaginary parts separately
        worst = max(worst,
                    np.max(np.abs(np.sort(values_plus.real) - np.sort(values_minus.real))),
                    np.max(np.abs(np.sort(values_plus.imag) - np.sort(values_minus.imag))))
    report("onset time of this wave", f"{onset_time(0.02, 0.5, 0.05, np.pi / 4):.4f}")
    report("largest difference of the eigenvalues for +m and -m", f"{worst:.1e}")
    check_record(pair_ok and worst < 1e-9,
                 "Gamma h_m(x4) Gamma = h_-m(x4) at every time: same spectra and onset",
                 record="Revision/pairing/reports/python-pairing.json, check "
                        "Q.one_particle_maps")
    '''),
    md(r"""
    ## 13. The last check

    The last cell checks that all five figure files exist in the folder
    Revision/textbook/figures and prints the number of checks that passed.
    """),
    code(r'''
    for name in ("10f_1_hermiticity_defect.png", "10f_2_eigenvalues_along_history.png",
                 "10f_3_inertia_along_history.png", "10f_4_onset_map.png",
                 "10f_5_good_sector_energies.png"):
        check(output_file(f"{FIGURE_FOLDER}/{name}").is_file(),
              f"the figure file {name} exists")
    all_checks_passed()
    '''),
    md(r"""
    ## 14. What this notebook showed

    - REPRODUCED from the Revision records: the prescribed history $a_4 = AHx_4$, $b_4 =
      b_4(0)e^{\beta a_4}$ with $A = H = m = 1$, $\beta = 4/3$, $b_4(0) = 1$ and its
      status, and the scale factors of the corrected metric; a wave
      $e^{i(q_0x_0 + q_1x_1 + q_5x_5)}$ has the frame momenta $k_0 =
      q_0e^{a_4}b_4^{-1/2}\tan z$ and $k_5 = q_5e^{a_4}b_4^{-1/2}(\sin^2 z)^{-1/12}$,
      both growing like $e^{a_4/3}$ (the hidden direction shrinks with the deflating
      extra times), and $k_1 = q_1e^{-a_4}$, shrinking (3-space inflates).
    - PROVED (exactly, at every instant of the local-frame model): $h(x_4)^2 =
      w(x_4)^2I_{16}$ with $w^2 = m^2 + k_0^2 + k_1^2 - k_5^2 = m^2 + q_1^2e^{-2a_4} -
      (e^{2a_4}/b_4)D$, $D = (\sin^2 z)^{-1/6}q_5^2 - \tan^2 z\,q_0^2$; the
      anti-Hermitian part of $h(x_4)$ has the size $k_5$ and the mixing of the two
      eigenspaces of $B$ the size $2k_5$, both growing like $e^{a_4/3}$; in the good
      sector $h(x_4)$ is Hermitian and commutes with $B$ at every time.
    - PROVED (from the exact form of $w^2$ and its slope): a wave turns from oscillation
      to growth exactly when $D > 0$, once, at the onset time; without hidden momentum
      every wave with $q_5 \neq 0$ does, and a hidden momentum with $\tan^2 z\,q_0^2
      \geq (\sin^2 z)^{-1/6}q_5^2$ prevents it. COMPUTED: the onset of the wave $q_1 =
      0.5$, $q_5 = 0.05$ at the fold is $x_4^\ast = 8.987$; the recorded sample $m = 1$,
      $k_5 = 2$ (eigenvalues $\pm i\sqrt3$) is the instant $x_4 = 3\ln 40$ of the wave
      $q_5 = 0.05$; the Krein inertia is $(4, 4)$ at every instant before the onset and
      the eigenspaces are Krein-neutral at every instant after it; the criterion holds
      on all 10201 waves of the right map.
    - COMPUTED (at the five slices of the Kohn-Sham record): in the good sector the
      instantaneous Fock space has the sea value $-8E(x_4)$ and quanta of energy
      $+E(x_4) > 0$.
    - PROVED (at every instant): the masses $+m$ and $-m$ have identical one-particle
      spectra, onset times and Krein inertia.
    - ASSUMED: the history is a prescribed background, not a solution of the field
      equations for $a_4$ and $b_4$ with this field as the source; the local-frame model
      evaluates the coefficients at one instant and one hidden position and leaves out
      the change of $\tan z$ along $x_0$ and the spin-connection term.
    - OPEN (not computed here): the evolution of the quantum state through the changing
      background (whether the instantaneous vacuum of one time contains quanta of a
      later time); a positive state space for the extra-time sector, whose waves with
      $D > 0$ all become Krein-neutral.
    """),
]

if __name__ == "__main__":
    raise SystemExit(run_builder(__file__))
