#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
"""Builder of Notebook 13c, "Slater determinants, second quantization and the two-site
model" (textbook "Universes in Pairs", chapter 13).

The notebook Revision/textbook/notebooks/13c_two_site_model.ipynb is BUILT from this
file by Revision/textbook/tools/nbkit.py (never edit the .ipynb by hand):

    python Revision/textbook/tools/nbkit.py build \
        Revision/textbook/notebooks/src/13c_two_site_model.py --date YYYY-MM-DD
    python Revision/textbook/tools/nbkit.py check \
        Revision/textbook/notebooks/src/13c_two_site_model.py

It builds creation and annihilation operators as matrices, checks the anticommutation
relations and Wick's theorem (including the identity <:S^2:> = (Tr C rho)^2 -
Tr(C rho C rho) of the Revision check hf_wick_contraction, here for a general Hermitian
vertex), and solves the two-site, two-electron model exactly and in Hartree-Fock.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools"))
from nbkit import code, md, run_builder  # noqa: E402

FIGURES = [
    "slater_determinants", "operator_matrices", "density_matrices",
    "two_site_energies", "double_occupancy", "hf_landscape", "density_map",
    "ks_inversion",
]

FACTS = {
    "id": "13c",
    "name": "13c_two_site_model",
    "title": "Slater determinants, second quantization and the two-site model",
    "purpose": (
        "It evaluates Slater determinants of two fermions (on three points and in a "
        "box), builds the creation and annihilation operators of four orbitals as "
        "16 x 16 matrices and checks their anticommutation relations, Wick's theorem "
        "for a determinant and for a thermal ensemble, the normal-ordered square of a "
        "one-body vertex and the energy formula of a determinant; it then solves the "
        "two-site model with two electrons exactly and in restricted and unrestricted "
        "Hartree-Fock (energies, correlation energy, double occupancy, the Hartree-Fock "
        "energy landscape), and shows the Hohenberg-Kohn map from the site-energy "
        "difference to the density and its exact Kohn-Sham inversion, with eight "
        "teaching plots."
    ),
    "records": [
        ["Revision/kohn_sham/reports/ks-theory-python.json",
         "the check hf_wick_contraction, whose identity for the normal-ordered square "
         "of a one-body vertex the notebook verifies for a general Hermitian vertex"],
    ],
    "packages": ["numpy", "matplotlib"],
    "needs_rust": [],
    "expected_seconds": 10,
    "timeout_seconds": 300,
    "files_written": ["Revision/textbook/figures/13c.captions.json"] + [
        f"Revision/textbook/figures/13c_{k}_{name}.png"
        for k, name in enumerate(FIGURES, 1)
    ],
    "final_lines": [
        "PASS the figure file 13c_8_ks_inversion.png exists",
        "ALL 30 CHECKS PASSED (notebook 13c)",
    ],
    "troubleshooting": [],
}

CELLS = [
    md(r"""
    ## 1. What this notebook computes

    This notebook turns the first half of many-body quantum mechanics into numbers that
    can be checked. It

    - evaluates the Slater determinant of two fermions on three points (every value,
      the normalisation and the density) and draws a two-fermion determinant in a box;
    - builds the creation and annihilation operators of four orbitals as $16 \times 16$
      matrices and checks the anticommutation relations;
    - checks Wick's theorem (every expectation value of a determinant is made of its
      density matrix) for a determinant and for a thermal ensemble, and the formula for
      the normal-ordered square of a one-body vertex that the Revision Kohn-Sham theory
      uses;
    - checks the energy formula of a determinant (direct minus exchange terms);
    - solves the model of two electrons on two sites exactly, and in restricted and
      unrestricted Hartree-Fock, and compares energies, correlation energy and double
      occupancy for all strengths of the repulsion;
    - shows the Hohenberg-Kohn theorem at work on two sites (the density determines the
      site-energy difference) and finds the exact Kohn-Sham potential by inverting the
      density;
    - draws eight teaching plots.
    """),
    md(r"""
    ## 3. The words used in this notebook

    - **Orbital**: a one-particle state; here either a function on a few points or one
      of a finite list of basis states.
    - **Slater determinant**: the antisymmetric state of $N$ fermions built from $N$
      orthonormal orbitals, $\Phi = \det[\phi_a(x_i)]/\sqrt{N!}$.
    - **Antisymmetric**: changing sign when two particles are exchanged.
    - **Occupation-number state** $|n_0 n_1 n_2 n_3\rangle$: the determinant that uses
      the orbitals $p$ with $n_p = 1$; there are $2^4 = 16$ of them for four orbitals.
    - **Creation operator** $a_p^\dagger$, **annihilation operator** $a_p$: add or
      remove a fermion in orbital $p$, with the sign $(-1)^{\nu_p}$, where $\nu_p$ is the
      number of occupied orbitals before $p$; on the 16 occupation-number states they
      are $16 \times 16$ matrices.
    - **Anticommutator** $\{A, B\} = AB + BA$.
    - **Density matrix** $\rho_{qp} = \langle a_p^\dagger a_q\rangle$; for a determinant
      its eigenvalues are 0 and 1, for a thermal ensemble the occupation probabilities.
    - **Wick's theorem**: $\langle a_p^\dagger a_q^\dagger a_s a_r\rangle =
      \rho_{rp}\rho_{sq} - \rho_{sp}\rho_{rq}$ for determinants and thermal ensembles of
      non-interacting fermions.
    - **Two-site model**: two places L and R, one orbital each, two labels (up, down);
      hopping $t$ between the sites, repulsion $U$ when both electrons sit on the same
      site.
    - **Hartree-Fock (HF)**: the best single determinant; **restricted** (both labels in
      the same orbital) or **unrestricted** (each label its own orbital).
    - **Correlation energy**: the exact ground-state energy minus the Hartree-Fock
      energy (never positive).
    - **Double occupancy**: the probability that both electrons sit on the same site.
    - **Hohenberg-Kohn theorem**: the ground-state density determines the external
      potential (up to a constant); **Kohn-Sham inversion**: finding the potential of
      NON-interacting electrons that gives the same density.
    """),
    md(r"""
    ## 4. The physical and mathematical situation

    **Determinants.** For two fermions in orthonormal orbitals $\phi_a$, $\phi_b$,
    $\Phi(x_0, x_1) = [\phi_a(x_0)\phi_b(x_1) - \phi_b(x_0)\phi_a(x_1)]/\sqrt2$. It is
    antisymmetric, vanishes when $x_0 = x_1$, is normalised, and its density is
    $|\phi_a|^2 + |\phi_b|^2$.

    **Operators.** With four orbitals the occupation-number states are the 16 numbers
    $0, \dots, 15$ written in binary: bit $p$ of the number is $n_p$. The matrix of
    $a_p$ maps a state with $n_p = 1$ to the state with $n_p = 0$, times
    $(-1)^{\nu_p}$; $a_p^\dagger$ is its transpose. The anticommutation relations
    $\{a_p, a_q^\dagger\} = \delta_{pq}$, $\{a_p, a_q\} = 0$ follow.

    **The two-site model.** The four orbitals are L up, R up, L down, R down (numbers 0,
    1, 2, 3). With site energies $-\Delta/2$ (L) and $+\Delta/2$ (R),

    $$\hat H = -t\sum_{\sigma}(a_{L\sigma}^\dagger a_{R\sigma} + a_{R\sigma}^\dagger
    a_{L\sigma}) + U(\hat n_{L\uparrow}\hat n_{L\downarrow} + \hat n_{R\uparrow}\hat
    n_{R\downarrow}) - \tfrac{\Delta}{2}\hat n_L + \tfrac{\Delta}{2}\hat n_R .$$

    For $\Delta = 0$ the exact ground-state energy of two electrons with opposite labels
    is $E_0 = \tfrac12(U - \sqrt{U^2 + 16t^2})$.

    **Hartree-Fock.** A determinant with the up orbital $(\cos\alpha, \sin\alpha)$ and
    the down orbital $(\cos\beta, \sin\beta)$ on (L, R) has the energy
    $E(\alpha, \beta) = -t(\sin 2\alpha + \sin 2\beta) + \tfrac{U}{2}(1 + \cos 2\alpha
    \cos 2\beta)$ (hopping energy of each orbital, plus $U$ times the double
    occupancy). Restricted HF ($\alpha = \beta = \pi/4$) gives $-2t + U/2$; the
    minimum over all $\alpha, \beta$ is $-2t + U/2$ for $U \le 2t$ and $-2t^2/U$ for
    $U > 2t$ (unrestricted).

    **Units.** All energies are in units of the hopping $t$ ($t = 1$).

    **Status.** Exact finite-dimensional mathematics (PROVED: every statement follows
    from the definitions; this notebook checks each one to rounding). No Revision number
    is reproduced; the Wick identity for the normal-ordered square is the one of the
    Revision check hf_wick_contraction.
    """),
    md(r"""
    ## 5. A Slater determinant on three points

    Space is three points $x = 0, 1, 2$; the orbitals are $\phi_0 = (1, 0, 0)$ and
    $\phi_1 = (0, 1, 1)/\sqrt2$. The next cell builds the $3 \times 3$ table of
    $\Phi(x_0, x_1)$, checks its values, its antisymmetry, its normalisation
    $\sum |\Phi|^2 = 1$ and its density $n(x) = 2\sum_{x_1}|\Phi(x, x_1)|^2 =
    (1, \tfrac12, \tfrac12)$.
    """),
    code(r'''
    import itertools  # loops over all combinations of indices

    import numpy as np  # arrays, matrices and linear algebra

    phi0 = np.array([1.0, 0.0, 0.0])
    phi1 = np.array([0.0, 1.0, 1.0]) / np.sqrt(2.0)
    # Phi[x0, x1] = (phi0(x0) phi1(x1) - phi1(x0) phi0(x1)) / sqrt(2)
    Phi = (np.outer(phi0, phi1) - np.outer(phi1, phi0)) / np.sqrt(2.0)
    for x0 in range(3):
        say("Phi(%d, x1) for x1 = 0, 1, 2: %s" % (x0, np.array2string(
            Phi[x0], precision=6, floatmode="fixed", suppress_small=True)))
    density_3 = 2.0 * np.sum(Phi ** 2, axis=1)  # n(x) = N sum_x1 |Phi(x, x1)|^2
    check(abs(Phi[0, 1] - 0.5) < 1e-15 and abs(Phi[1, 2]) < 1e-15,
          "Phi(0,1) = 1/2 and Phi(1,2) = 0")
    check(np.allclose(Phi, -Phi.T, atol=1e-15) and np.allclose(np.diag(Phi), 0.0),
          "Phi is antisymmetric and zero on the diagonal (Pauli)")
    check(abs(np.sum(Phi ** 2) - 1.0) < 1e-15
          and np.allclose(density_3, [1.0, 0.5, 0.5], atol=1e-15)
          and np.allclose(density_3, phi0 ** 2 + phi1 ** 2, atol=1e-15),
          "Phi is normalised and its density is (1, 1/2, 1/2) = phi0^2 + phi1^2")
    '''),
    md(r"""
    The next cell draws this table and, next to it, the determinant of the two lowest
    orbitals $\sqrt2\sin(\pi x)$ and $\sqrt2\sin(2\pi x)$ of a particle in the box
    $0 < x < 1$ as a heat map over the positions $(x_0, x_1)$ of the two fermions.
    """),
    code(r'''
    x_box = np.linspace(0.0, 1.0, 101)
    chi1 = np.sqrt(2.0) * np.sin(np.pi * x_box)
    chi2 = np.sqrt(2.0) * np.sin(2.0 * np.pi * x_box)
    Phi_box = (np.outer(chi1, chi2) - np.outer(chi2, chi1)) / np.sqrt(2.0)
    fig, (left, right) = plt.subplots(1, 2, figsize=(10.0, 4.2))
    image = left.imshow(Phi, origin="lower", cmap="coolwarm", vmin=-0.6, vmax=0.6)
    for x0, x1 in itertools.product(range(3), repeat=2):
        left.text(x1, x0, f"{Phi[x0, x1]:+.2f}", ha="center", va="center")
    left.set_xticks([0, 1, 2])
    left.set_yticks([0, 1, 2])
    left.set_xlabel("position $x_1$ of fermion 1")
    left.set_ylabel("position $x_0$ of fermion 0")
    left.set_title("three points")
    image = right.imshow(Phi_box, origin="lower", extent=(0, 1, 0, 1),
                         cmap="coolwarm")
    right.plot([0, 1], [0, 1], "k--", lw=0.8)
    right.set_xlabel("$x_1$")
    right.set_ylabel("$x_0$")
    right.set_title("two fermions in a box")
    fig.colorbar(image, ax=right, shrink=0.85)
    save_figure(fig, "slater_determinants",
                "Two Slater determinants of two fermions as heat maps (red positive, "
                "blue negative): left, $\\Phi(x_0, x_1)$ on three points for the "
                "orbitals $(1,0,0)$ and $(0,1,1)/\\sqrt2$ with its values written in; "
                "right, the determinant of the two lowest orbitals of a box "
                "$0 < x < 1$, against the positions $x_0$ (vertical) and $x_1$ "
                "(horizontal). Both change sign under the exchange $x_0$ and $x_1$ "
                "(mirror in the dashed diagonal) and vanish on the diagonal: two "
                "identical fermions are never at the same place.")
    check(np.allclose(Phi_box, -Phi_box.T, atol=1e-14), "the box determinant is "
          "antisymmetric")
    '''),
    md(r"""
    ## 6. Creation and annihilation operators as matrices

    The next cell builds the matrices $a_0, \dots, a_3$ on the 16 occupation-number
    states. The state number $s$ has $n_p = $ bit $p$ of $s$ (in Python `(s >> p) & 1`);
    removing the fermion of orbital $p$ gives the state number `s ^ (1 << p)` (bit $p$
    switched off), with the sign $(-1)^{\nu_p}$, $\nu_p = n_0 + \dots + n_{p-1}$. Then
    it checks all anticommutation relations.
    """),
    code(r'''
    M = 4  # orbitals
    DIM = 2 ** M  # occupation-number states


    def bit(state, p):
        """The occupation n_p (0 or 1) of orbital p in the state number state."""
        return (state >> p) & 1


    a = []  # a[p] is the 16 x 16 matrix of the annihilation operator a_p
    for p in range(M):
        matrix = np.zeros((DIM, DIM))
        for state in range(DIM):
            if bit(state, p) == 1:
                nu = sum(bit(state, q) for q in range(p))  # occupied before p
                matrix[state ^ (1 << p), state] = (-1) ** nu
        a.append(matrix)
    a_dag = [matrix.T for matrix in a]  # creation operators: the transposes
    identity = np.eye(DIM)
    worst = 0.0
    for p, q in itertools.product(range(M), repeat=2):
        worst = max(worst,
                    np.abs(a[p] @ a_dag[q] + a_dag[q] @ a[p] - (p == q) * identity).max(),
                    np.abs(a[p] @ a[q] + a[q] @ a[p]).max(),
                    np.abs(a_dag[p] @ a_dag[q] + a_dag[q] @ a_dag[p]).max())
    check(worst == 0.0, "{a_p, a_q^dag} = delta_pq and {a_p, a_q} = 0 exactly")
    number = sum(a_dag[p] @ a[p] for p in range(M))  # the particle-number operator
    check(np.array_equal(np.diag(number), [bin(s).count("1") for s in range(DIM)]),
          "the number operator counts the occupied orbitals of every state")
    '''),
    md(r"""
    The next cell draws two of these matrices. Every column of $a_1^\dagger$ has at most
    one nonzero entry ($\pm 1$): the operator moves a state to exactly one other state,
    and the sign records how many occupied orbitals it had to pass.
    """),
    code(r'''
    fig, axes = plt.subplots(1, 2, figsize=(9.0, 4.2))
    for ax, p in zip(axes, (1, 3)):
        image = ax.imshow(a_dag[p], cmap="coolwarm", vmin=-1, vmax=1)
        ax.set_title(f"creation operator $a_{p}^\\dagger$")
        ax.set_xlabel("state number before (column)")
        ax.set_ylabel("state number after (row)")
    fig.colorbar(image, ax=axes, shrink=0.8)
    save_figure(fig, "operator_matrices",
                "The creation operators $a_1^\\dagger$ (left) and $a_3^\\dagger$ "
                "(right) of four orbitals as $16 \\times 16$ matrices on the "
                "occupation-number states $0, \\dots, 15$ (bit $p$ of the state number "
                "is $n_p$); red $+1$, blue $-1$, grey 0. A column has one entry when "
                "orbital $p$ is empty in that state and none when it is occupied "
                "(Pauli); the sign is $(-1)^{\\nu_p}$, the parity of the number of "
                "occupied orbitals before $p$.")
    '''),
    md(r"""
    ## 7. Wick's theorem for a determinant and for a thermal ensemble

    The next cell mixes the four orbitals with a random unitary $4 \times 4$ matrix $U$
    (from the QR factorisation of a random complex matrix with a fixed seed), builds the
    new creation operators $a_p'^\dagger = \sum_k U_{kp}a_k^\dagger$, and the determinant
    $|\Phi\rangle = a_0'^\dagger a_1'^\dagger|0\rangle$ that occupies the new orbitals 0
    and 1. Its density matrix is $\rho = \sum_{a = 0, 1} U_{:,a}U_{:,a}^\dagger$. It
    then checks $\langle a_p^\dagger a_q\rangle = \rho_{qp}$ and all 256 four-operator
    expectation values against Wick's formula.
    """),
    code(r'''
    rng = np.random.default_rng(12345)  # fixed seed: the same numbers every run
    U_mix = np.linalg.qr(rng.normal(size=(M, M)) + 1j * rng.normal(size=(M, M)))[0]
    a_dag_new = [sum(U_mix[k, p] * a_dag[k] for k in range(M)) for p in range(M)]
    vacuum = np.zeros(DIM)
    vacuum[0] = 1.0  # state number 0: no fermion at all
    Phi_state = a_dag_new[0] @ a_dag_new[1] @ vacuum
    rho_det = sum(np.outer(U_mix[:, k], U_mix[:, k].conj()) for k in (0, 1))


    def wick_errors(expect, rho):
        """Largest errors of <a+_p a_q> = rho_qp and of the four-operator formula."""
        two = max(abs(expect(a_dag[p] @ a[q]) - rho[q, p])
                  for p, q in itertools.product(range(M), repeat=2))
        four = max(abs(expect(a_dag[p] @ a_dag[q] @ a[s] @ a[r])
                       - (rho[r, p] * rho[s, q] - rho[s, p] * rho[r, q]))
                   for p, q, r, s in itertools.product(range(M), repeat=4))
        return two, four


    def in_determinant(operator):
        """<Phi| operator |Phi> for the determinant Phi_state."""
        return np.vdot(Phi_state, operator @ Phi_state)


    check(abs(np.vdot(Phi_state, Phi_state) - 1.0) < 1e-14, "the determinant is "
          "normalised")
    two, four = wick_errors(in_determinant, rho_det)  # the largest errors (rounding)
    check(two < 1e-14 and four < 1e-14,
          "Wick's theorem holds for the determinant (all 16 + 256 values, to 1e-14)")
    check(np.allclose(rho_det @ rho_det, rho_det, atol=1e-14)
          and abs(np.trace(rho_det).real - 2.0) < 1e-14,
          "the density matrix of a determinant obeys rho^2 = rho, Tr rho = 2")
    '''),
    md(r"""
    For a **thermal ensemble** of non-interacting fermions with the orbital energies
    $\epsilon_p$ in the mixed orbitals, the density operator on the 16 states is
    $e^{-(\hat H_0 - \mu\hat N)/T}/Z$ with $\hat H_0 = \sum_p \epsilon_p
    a_p'^\dagger a_p'$. The next cell builds it (the exponential of a Hermitian matrix
    through its eigenvalues), and checks Wick's theorem with
    $\rho = \sum_p f_p U_{:,p}U_{:,p}^\dagger$ and the Fermi-Dirac occupations
    $f_p = 1/(e^{(\epsilon_p - \mu)/T} + 1)$.
    """),
    code(r'''
    energies = np.array([-1.0, -0.3, 0.4, 1.2])  # orbital energies (units of t)
    MU, TEMPERATURE = 0.0, 0.5
    H0 = sum(energies[p] * a_dag_new[p] @ a_dag_new[p].conj().T for p in range(M))
    K = H0 - MU * number  # H0 - mu N, a Hermitian 16 x 16 matrix
    k_values, k_vectors = np.linalg.eigh(K)
    weights = np.exp(-(k_values - k_values.min()) / TEMPERATURE)  # shifted: no overflow
    gibbs = (k_vectors * (weights / weights.sum())) @ k_vectors.conj().T
    f = 1.0 / (np.exp((energies - MU) / TEMPERATURE) + 1.0)  # Fermi-Dirac
    rho_thermal = sum(f[p] * np.outer(U_mix[:, p], U_mix[:, p].conj()) for p in range(M))
    two, four = wick_errors(lambda operator: np.trace(gibbs @ operator), rho_thermal)
    check(two < 1e-13 and four < 1e-13,
          "Wick's theorem holds for the thermal ensemble of non-interacting fermions "
          "(to 1e-13)")
    '''),
    md(r"""
    The interaction of the dirac16complex Kohn-Sham model is the square of a one-body
    quantity, $S = \sum_{pq}V_{pq}a_p^\dagger a_q$ (there with the vertex $V = C$ on 16
    spinor components). Its normal-ordered square
    $:S^2: = \sum V_{pq}V_{rs}\,a_p^\dagger a_r^\dagger a_s a_q$ has, by Wick's theorem,
    $\langle :S^2: \rangle = (\mathrm{Tr}\,V\rho)^2 - \mathrm{Tr}(V\rho V\rho)$: a Hartree
    part and an exchange part. The Revision record verified this identity on a two-mode
    state; the next cell checks it on the four orbitals for a random Hermitian vertex,
    in the determinant and in the thermal ensemble.
    """),
    code(r'''
    raw = rng.normal(size=(M, M)) + 1j * rng.normal(size=(M, M))
    V = (raw + raw.conj().T) / 2.0  # a random Hermitian vertex
    S_square = sum(V[p, q] * V[r, s] * a_dag[p] @ a_dag[r] @ a[s] @ a[q]
                   for p, q, r, s in itertools.product(range(M), repeat=4))
    for label, expect, rho in (("determinant", in_determinant, rho_det),
                               ("thermal", lambda o: np.trace(gibbs @ o), rho_thermal)):
        lhs = expect(S_square)
        rhs = np.trace(V @ rho) ** 2 - np.trace(V @ rho @ V @ rho)
        say(f"{label}: <:S^2:> = {lhs.real:.10f}, Hartree - exchange = {rhs.real:.10f}")
        check(abs(lhs - rhs) < 1e-12,
              f"<:S^2:> = (Tr V rho)^2 - Tr(V rho V rho) in the {label} state",
              record="Revision/kohn_sham/reports/ks-theory-python.json, check "
                     "hf_wick_contraction")
    '''),
    md(r"""
    The next cell draws the density matrix of the determinant (its absolute values) and
    the eigenvalues of both density matrices: a determinant has the occupations 1, 1, 0,
    0; the thermal ensemble has the Fermi-Dirac occupations $f_p$.
    """),
    code(r'''
    fig, (left, right) = plt.subplots(1, 2, figsize=(10.0, 4.0))
    image = left.imshow(np.abs(rho_det), cmap="viridis", vmin=0.0)
    left.set_title("$|\\rho_{qp}|$ of the determinant")
    left.set_xticks(range(M))
    left.set_yticks(range(M))
    left.set_xlabel("$p$")
    left.set_ylabel("$q$")
    fig.colorbar(image, ax=left, shrink=0.85)
    occupations_det = np.sort(np.linalg.eigvalsh(rho_det))[::-1]
    occupations_th = np.sort(np.linalg.eigvalsh(rho_thermal))[::-1]
    positions = np.arange(M)
    right.bar(positions - 0.2, occupations_det, width=0.4, label="determinant")
    right.bar(positions + 0.2, occupations_th, width=0.4, label="thermal, $T = 0.5$")
    right.set_xticks(positions)
    right.set_xlabel("eigenvalue number")
    right.set_ylabel("occupation (eigenvalue of $\\rho$)")
    right.legend()
    save_figure(fig, "density_matrices",
                "Left: the absolute values of the density matrix "
                "$\\rho_{qp} = \\langle a_p^\\dagger a_q \\rangle$ of a determinant of "
                "two fermions in four randomly mixed orbitals (heat map; $p$ and $q$ "
                "label the four basis orbitals). Right: the eigenvalues of the density "
                "matrices of this determinant (exactly 1, 1, 0, 0) and of a thermal "
                "ensemble of non-interacting fermions at $T = 0.5$ (the Fermi-Dirac "
                "occupations, between 0 and 1); in both cases Wick's theorem holds.")
    check(np.allclose(occupations_det, [1, 1, 0, 0], atol=1e-14)
          and np.allclose(occupations_th, np.sort(f)[::-1], atol=1e-14),
          "the occupations are 1, 1, 0, 0 and the Fermi-Dirac numbers")
    '''),
    md(r"""
    ## 8. The energy of a determinant: direct minus exchange

    With a one-body matrix $h_{pq}$ and two-body integrals $w_{pqrs}$ the Hamiltonian is
    $\hat H = \sum h_{pq}a_p^\dagger a_q + \tfrac12\sum w_{pqrs}a_p^\dagger a_q^\dagger
    a_s a_r$. For the determinant of the basis orbitals 0 and 1 its energy must be
    $\sum_{a} h_{aa} + \tfrac12\sum_{a,b}(w_{abab} - w_{abba})$ over $a, b \in \{0,
    1\}$. The next cell makes the integrals from four orthonormal orbitals on a grid of
    six points and a random symmetric interaction $W(x, x')$ (so that they have the
    symmetries of a real interaction) and compares.
    """),
    code(r'''
    chi = np.linalg.qr(rng.normal(size=(6, M)))[0]  # four orthonormal orbitals on 6 points
    W_raw = rng.normal(size=(6, 6))
    W_pair = (W_raw + W_raw.T) / 2.0  # a symmetric interaction W(x, x')
    h_raw = rng.normal(size=(M, M))
    h_one = (h_raw + h_raw.T) / 2.0  # a symmetric one-body matrix
    # w[p,q,r,s] = sum_{x,x'} chi_p(x) chi_q(x') W(x,x') chi_r(x) chi_s(x')
    w = np.einsum("xp,yq,xy,xr,ys->pqrs", chi, chi, W_pair, chi, chi)
    H_many = sum(h_one[p, q] * a_dag[p] @ a[q] for p, q in itertools.product(range(M),
                                                                             repeat=2))
    H_many = H_many + 0.5 * sum(w[p, q, r, s] * a_dag[p] @ a_dag[q] @ a[s] @ a[r]
                                for p, q, r, s in itertools.product(range(M), repeat=4))
    basis_det = a_dag[0] @ a_dag[1] @ vacuum  # occupies the basis orbitals 0 and 1
    direct = basis_det @ H_many @ basis_det
    formula = sum(h_one[k, k] for k in (0, 1)) + 0.5 * sum(
        w[k, l, k, l] - w[k, l, l, k] for k in (0, 1) for l in (0, 1))
    say(f"<Phi|H|Phi> = {direct:.10f};  sum h_aa + (1/2) sum (w_abab - w_abba) = "
        f"{formula:.10f}")
    check(abs(direct - formula) < 1e-12,
          "the energy of a determinant is one-body + direct - exchange")
    '''),
    md(r"""
    ## 9. The two-site model: exact solution

    The next cell builds the Hamiltonian of section 4 from the operator matrices (orbital
    0 = L up, 1 = R up, 2 = L down, 3 = R down), keeps the four states with one up and
    one down electron, and diagonalises it. It checks the closed form of $E_0$ and
    computes the double occupancy $\langle \hat n_{L\uparrow}\hat n_{L\downarrow} +
    \hat n_{R\uparrow}\hat n_{R\downarrow}\rangle$ of the ground state.
    """),
    code(r'''
    n_op = [a_dag[p] @ a[p] for p in range(M)]  # occupation operators
    DOUBLE = n_op[0] @ n_op[2] + n_op[1] @ n_op[3]  # both electrons on one site
    # The states with exactly one up (orbital 0 or 1) and one down (2 or 3) electron:
    SECTOR = [s for s in range(DIM) if bit(s, 0) + bit(s, 1) == 1
              and bit(s, 2) + bit(s, 3) == 1]


    def two_site(t, U, delta=0.0):
        """Ground-state energy, double occupancy and n_L of the two-site model."""
        H = -t * (a_dag[0] @ a[1] + a_dag[1] @ a[0] + a_dag[2] @ a[3] + a_dag[3] @ a[2])
        H = H + U * DOUBLE - 0.5 * delta * (n_op[0] + n_op[2]) \
            + 0.5 * delta * (n_op[1] + n_op[3])
        block = H[np.ix_(SECTOR, SECTOR)]  # the 4 x 4 block of the sector
        values, vectors = np.linalg.eigh(block)
        ground = vectors[:, 0]
        occupancy = ground @ DOUBLE[np.ix_(SECTOR, SECTOR)] @ ground
        n_left = ground @ (n_op[0] + n_op[2])[np.ix_(SECTOR, SECTOR)] @ ground
        return values[0], occupancy, n_left


    say(f"the sector holds the states {SECTOR}")
    for U in (2.0, 4.0):
        E0, occupancy, n_left = two_site(1.0, U)
        report(f"U = {U:.0f}: exact E_0", f"{E0:.6f}")
        report(f"U = {U:.0f}: exact double occupancy", f"{occupancy:.6f}")
        check(abs(E0 - 0.5 * (U - np.sqrt(U ** 2 + 16.0))) < 1e-12
              and abs(n_left - 1.0) < 1e-12,
              f"U = {U:.0f}: E_0 = (U - sqrt(U^2 + 16 t^2))/2 and n_L = 1")
    '''),
    md(r"""
    ## 10. Hartree-Fock: restricted and unrestricted

    The next cell first checks the energy formula $E(\alpha, \beta)$ of section 4
    against the Fock-space expectation value of the determinant
    $(\cos\alpha\,a_{L\uparrow}^\dagger + \sin\alpha\,a_{R\uparrow}^\dagger)
    (\cos\beta\,a_{L\downarrow}^\dagger + \sin\beta\,a_{R\downarrow}^\dagger)|0\rangle$
    at a few angles, then minimises $E(\alpha, \beta)$ on a fine grid of angles for many
    values of $U$. With $\beta = \pi/2 - \alpha$ and $s = \sin 2\alpha$ the energy is
    $-2ts + \tfrac{U}{2}s^2$ (a parabola in $s \in [0, 1]$), whose minimum gives the
    closed forms checked below.
    """),
    code(r'''
    def hf_energy(alpha, beta, U, t=1.0):
        """E(alpha, beta) of the determinant with up (cos a, sin a), down (cos b, sin b)."""
        return (-t * (np.sin(2 * alpha) + np.sin(2 * beta))
                + 0.5 * U * (1.0 + np.cos(2 * alpha) * np.cos(2 * beta)))


    H_test = -(a_dag[0] @ a[1] + a_dag[1] @ a[0] + a_dag[2] @ a[3] + a_dag[3] @ a[2]) \
        + 3.0 * DOUBLE  # t = 1, U = 3
    worst = 0.0
    for alpha, beta in ((0.3, 1.1), (0.7, 0.2), (np.pi / 4, np.pi / 4)):
        det = (np.cos(alpha) * a_dag[0] + np.sin(alpha) * a_dag[1]) @ (
            np.cos(beta) * a_dag[2] + np.sin(beta) * a_dag[3]) @ vacuum
        worst = max(worst, abs(det @ H_test @ det - hf_energy(alpha, beta, 3.0)))
    check(worst < 1e-12, "the Hartree-Fock energy formula equals <Phi|H|Phi>")
    angles = np.linspace(0.0, np.pi / 2, 1001)
    A, B = np.meshgrid(angles, angles, indexing="ij")
    U_values = np.linspace(0.0, 8.0, 33)
    E_exact = np.array([two_site(1.0, U)[0] for U in U_values])
    D_exact = np.array([two_site(1.0, U)[1] for U in U_values])
    E_rhf = -2.0 + 0.5 * U_values  # restricted: alpha = beta = pi/4
    E_uhf = np.array([hf_energy(A, B, U).min() for U in U_values])  # grid minimum
    U_safe = np.where(U_values > 2.0, U_values, 1.0)  # avoids dividing by U = 0
    E_closed = np.where(U_values <= 2.0, -2.0 + 0.5 * U_values, -2.0 / U_safe)
    check(np.max(np.abs(E_uhf - E_closed)) < 1e-5,
          "the minimum over all determinants is -2t + U/2 (U <= 2t) and -2t^2/U")
    check(np.all(E_exact <= E_uhf + 1e-12) and np.all(E_uhf <= E_rhf + 1e-12),
          "variational order: exact <= unrestricted HF <= restricted HF")
    E_c = E_exact - E_closed  # correlation energy
    report("U = 2: correlation energy E_0 - E_HF", f"{E_c[8]:.6f}")
    fine_U = np.linspace(2.0, 8.0, 60001)  # closed forms on a fine grid of U > 2t
    fine_c = 0.5 * (fine_U - np.sqrt(fine_U ** 2 + 16.0)) + 2.0 / fine_U
    report("U of the largest correlation energy (in size)",
           f"{fine_U[np.argmin(fine_c)]:.3f}")
    '''),
    md(r"""
    The next cell draws the three energies and the correlation energy against $U/t$.
    """),
    code(r'''
    fig, (left, right) = plt.subplots(1, 2, figsize=(10.0, 4.0))
    left.plot(U_values, E_rhf, "--", label="restricted HF $-2t + U/2$")
    left.plot(U_values, E_closed, "-.", label="unrestricted HF")
    left.plot(U_values, E_exact, color="black", lw=2.0, label="exact $E_0$")
    left.axvline(2.0, color="gray", lw=0.8)
    left.set_xlabel("repulsion $U/t$")
    left.set_ylabel("ground-state energy ($t$)")
    left.legend(fontsize=8)
    right.plot(U_values, E_c, "o-", ms=3, color="black")
    right.set_xlabel("repulsion $U/t$")
    right.set_ylabel("correlation energy $E_0 - E_{HF}$ ($t$)")
    fig.suptitle("Two electrons on two sites: exact versus Hartree-Fock")
    save_figure(fig, "two_site_energies",
                "Left: the ground-state energy of two electrons on two sites against "
                "the repulsion $U/t$: exact (black), restricted Hartree-Fock "
                "$-2t + U/2$ (dashed) and the best determinant, unrestricted for "
                "$U > 2t$ (dash-dotted; the grey line marks $U = 2t$); energies in "
                "units of the hopping $t$. Right: the correlation energy, exact minus "
                "best Hartree-Fock energy, which no single determinant can capture; "
                "its size grows from zero, is largest at about $U = 3.3t$ (beyond the "
                "point $U = 2t$ where restricted and unrestricted Hartree-Fock "
                "separate) and then falls slowly.")
    '''),
    md(r"""
    The next cell draws the probability that both electrons sit on the same site. The
    restricted determinant always gives $1/2$; the exact state avoids double occupancy
    more and more as $U$ grows; the unrestricted determinant gives
    $\tfrac12(1 + \cos 2\alpha\cos 2\beta) = 2t^2/U^2$ for $U > 2t$, by breaking the
    left-right symmetry of each label.
    """),
    code(r'''
    D_uhf = np.where(U_values <= 2.0, 0.5, 2.0 / U_safe ** 2)
    fig, ax = plt.subplots()
    ax.plot(U_values, 0.5 * np.ones_like(U_values), "--", label="restricted HF: 1/2")
    ax.plot(U_values, D_uhf, "-.", label="unrestricted HF: $2t^2/U^2$ for $U > 2t$")
    ax.plot(U_values, D_exact, color="black", lw=2.0, label="exact")
    ax.set_xlabel("repulsion $U/t$")
    ax.set_ylabel("double occupancy")
    ax.set_title("How often both electrons sit on the same site")
    ax.legend()
    save_figure(fig, "double_occupancy",
                "The probability that both electrons sit on the same site (double "
                "occupancy, a pure number) against $U/t$: exact ground state (black), "
                "restricted Hartree-Fock (always 1/2, dashed) and unrestricted "
                "Hartree-Fock (dash-dotted). The exact electrons avoid each other while "
                "keeping each label shared equally between the sites; a single "
                "determinant can lower the double occupancy only by breaking that "
                "symmetry, and then overshoots.")
    check(abs(D_exact[8] - 0.276393) < 1e-6 and abs(D_exact[16] - 0.146447) < 1e-6,
          "exact double occupancy 0.276393 at U = 2t and 0.146447 at U = 4t")
    check(np.all(np.diff(D_exact) < 0), "the exact double occupancy falls as U grows")
    '''),
    md(r"""
    The next cell draws the Hartree-Fock energy $E(\alpha, \beta)$ at $U = 4t$ as a
    contour map. The restricted point $\alpha = \beta = \pi/4$ is a saddle; the two
    lowest points (unrestricted solutions) lie on the line $\beta = \pi/2 - \alpha$.
    """),
    code(r'''
    E_map = hf_energy(A, B, 4.0)
    index = np.unravel_index(np.argmin(E_map), E_map.shape)
    fig, ax = plt.subplots(figsize=(6.0, 5.0))
    contours = ax.contourf(A, B, E_map, levels=30, cmap="viridis")
    fig.colorbar(contours, ax=ax, label="$E(\\alpha, \\beta)$ ($t$)")
    ax.plot([np.pi / 4], [np.pi / 4], "wx", ms=10, label="restricted (saddle)")
    ax.plot([angles[index[0]], angles[index[1]]], [angles[index[1]], angles[index[0]]],
            "r*", ms=12, label="unrestricted minima")
    ax.set_xlabel("$\\alpha$ (up orbital)")
    ax.set_ylabel("$\\beta$ (down orbital)")
    ax.set_title("Hartree-Fock energy landscape at $U = 4t$")
    ax.legend(loc="upper right", fontsize=8)
    save_figure(fig, "hf_landscape",
                "The energy $E(\\alpha, \\beta)$ of the determinant with the up orbital "
                "$(\\cos\\alpha, \\sin\\alpha)$ and the down orbital "
                "$(\\cos\\beta, \\sin\\beta)$ on the sites (L, R), for $U = 4t$, as a "
                "contour map over the two angles (radians; colors in units of $t$). "
                "The restricted determinant $\\alpha = \\beta = \\pi/4$ (white cross) is "
                "a saddle; the two minima (red stars), mirror images of each other, "
                "put the up electron mostly on one site and the down electron mostly "
                "on the other, with energy $-2t^2/U = -0.5t$.")
    check(abs(E_map.min() + 0.5) < 1e-5 and abs(hf_energy(np.pi / 4, np.pi / 4, 4.0)
                                                 - 0.0) < 1e-12,
          "at U = 4t: minimum -0.5 t, restricted value 0")
    '''),
    md(r"""
    ## 11. The Hohenberg-Kohn map and the exact Kohn-Sham potential on two sites

    Give the sites the energies $\mp\Delta/2$. For every $\Delta$ the exact ground state
    has a density $n_L$ on the left site ($n_R = 2 - n_L$). The Hohenberg-Kohn theorem
    says that different $\Delta$ give different $n_L$: the map $\Delta \to n_L$ is
    one-to-one, so $n_L$ determines $\Delta$. The next cell computes $n_L(\Delta)$ for
    $U = 0, 2, 4$ and checks that it strictly increases.

    Kohn and Sham ask: which site-energy difference $\Delta_s$ makes NON-interacting
    electrons have the same $n_L$? For two non-interacting electrons in the lowest
    orbital of $\begin{pmatrix}-\Delta_s/2 & -t\\ -t & \Delta_s/2\end{pmatrix}$,
    $n_L - 1 = \Delta_s/\sqrt{\Delta_s^2 + 4t^2}$, which inverts to
    $\Delta_s = 2t\,(n_L - 1)/\sqrt{1 - (n_L - 1)^2}$. The difference $\Delta_s -
    \Delta$ is the exact Hartree-exchange-correlation potential difference between the
    sites.
    """),
    code(r'''
    deltas = np.linspace(-4.0, 4.0, 81)
    density_maps = {U: np.array([two_site(1.0, U, d)[2] for d in deltas])
                    for U in (0.0, 2.0, 4.0)}
    for U, n_left in density_maps.items():
        check(np.all(np.diff(n_left) > 0),
              f"U = {U:.0f}: n_L increases strictly with Delta (one-to-one map)")


    def kohn_sham_delta(n_left, t=1.0):
        """The site-energy difference of non-interacting electrons with density n_L."""
        excess = n_left - 1.0
        return 2.0 * t * excess / np.sqrt(1.0 - excess ** 2)


    def free_density(delta_s, t=1.0):
        """n_L of two non-interacting electrons with the site energies -+delta_s/2."""
        values, vectors = np.linalg.eigh(np.array([[-delta_s / 2, -t],
                                                   [-t, delta_s / 2]]))
        return 2.0 * vectors[0, 0] ** 2


    delta_s = {U: kohn_sham_delta(n) for U, n in density_maps.items()}
    rebuilt = max(abs(free_density(ds) - n) for U in density_maps
                  for ds, n in zip(delta_s[U], density_maps[U]))
    check(rebuilt < 1e-12, "the Kohn-Sham site energies reproduce the exact densities")
    check(np.max(np.abs(delta_s[0.0] - deltas)) < 1e-12,
          "without interaction the Kohn-Sham potential is the true one")
    '''),
    md(r"""
    The next cell draws the density map $n_L(\Delta)$ for the three repulsions.
    """),
    code(r'''
    fig, ax = plt.subplots()
    for U, style in ((0.0, ":"), (2.0, "--"), (4.0, "-")):
        ax.plot(deltas, density_maps[U], style, label=f"$U = {U:.0f}t$")
    ax.axhline(1.0, color="gray", lw=0.8)
    ax.set_xlabel("site-energy difference $\\Delta$ ($t$)")
    ax.set_ylabel("exact density on the left site $n_L$")
    ax.set_title("Hohenberg-Kohn on two sites: the potential determines the density")
    ax.legend()
    save_figure(fig, "density_map",
                "The exact ground-state density $n_L$ on the left site of the two-site "
                "model against the site-energy difference $\\Delta$ (units of $t$), "
                "for $U = 0$, $2t$ and $4t$. Every curve rises strictly, so each "
                "density belongs to exactly one $\\Delta$ (the Hohenberg-Kohn theorem "
                "on two sites); the repulsion flattens the curves, because it opposes "
                "piling both electrons on one site.")
    '''),
    md(r"""
    For comparison the next cell also computes the potential of the mean-field
    (Hartree plus exchange, restricted) approximation, in which each electron feels $U$
    times the density of the other label on each site: its site-energy difference is
    $\Delta - U(n_L - 1)$, with $n_L$ solved self-consistently (by bisection on the
    equation $n_L - 1 = G(n_L - 1)$ with $G(x) = (\Delta - Ux)/\sqrt{(\Delta - Ux)^2 +
    4t^2}$; the left side minus the right side increases with $x$, so the root is
    unique). Then it draws the exact Kohn-Sham $\Delta_s$ and the mean-field one.
    """),
    code(r'''
    def mean_field_excess(delta, U, t=1.0):
        """The self-consistent x = n_L - 1 of restricted Hartree + exchange."""
        low, high = -1.0, 1.0
        for _ in range(80):  # bisection on x - G(x), which increases with x
            middle = 0.5 * (low + high)
            shifted = delta - U * middle
            if middle - shifted / np.sqrt(shifted ** 2 + 4 * t * t) > 0:
                high = middle
            else:
                low = middle
        return 0.5 * (low + high)


    mf_delta_s = np.array([d - 4.0 * mean_field_excess(d, 4.0) for d in deltas])
    fig, ax = plt.subplots()
    ax.plot(deltas, deltas, ":", color="gray", label="$\\Delta_s = \\Delta$ ($U = 0$)")
    ax.plot(deltas, delta_s[2.0], "--", label="exact Kohn-Sham, $U = 2t$")
    ax.plot(deltas, delta_s[4.0], color="black", lw=2.0, label="exact Kohn-Sham, "
            "$U = 4t$")
    ax.plot(deltas, mf_delta_s, "-.", label="mean field (Hartree + exchange), $U = 4t$")
    ax.set_xlabel("true site-energy difference $\\Delta$ ($t$)")
    ax.set_ylabel("Kohn-Sham site-energy difference $\\Delta_s$ ($t$)")
    ax.set_title("The exact Kohn-Sham potential of two sites")
    ax.legend(fontsize=8)
    save_figure(fig, "ks_inversion",
                "The site-energy difference $\\Delta_s$ that makes non-interacting "
                "electrons reproduce the exact density of the two-site model, against "
                "the true difference $\\Delta$ (both in units of $t$): exact "
                "Kohn-Sham for $U = 2t$ (dashed) and $U = 4t$ (black), the "
                "non-interacting line $\\Delta_s = \\Delta$ (dotted) and the restricted "
                "mean-field value for $U = 4t$ (dash-dotted). The interaction screens "
                "the potential ($|\\Delta_s| < |\\Delta|$); the gap between the black "
                "and the dash-dotted curve is the correlation part of the exact "
                "Kohn-Sham potential.")
    nonzero = np.abs(deltas) > 1e-9  # every Delta except 0
    check(np.all(np.abs(delta_s[4.0][nonzero]) < np.abs(deltas[nonzero])),
          "the repulsion screens the potential: |Delta_s| < |Delta|")
    '''),
    md(r"""
    ## 12. The last check

    The last cell checks that all eight figure files exist and prints the number of
    checks that passed.
    """),
    code(r'''
    figure_names = ["slater_determinants", "operator_matrices", "density_matrices",
                    "two_site_energies", "double_occupancy", "hf_landscape",
                    "density_map", "ks_inversion"]
    missing = [name for k, name in enumerate(figure_names, 1)
               if not output_file(f"{FIGURE_FOLDER}/13c_{k}_{name}.png").is_file()]
    check(missing == [], "all eight figure files exist")
    check(output_file(f"{FIGURE_FOLDER}/13c_8_ks_inversion.png").is_file(),
          "the figure file 13c_8_ks_inversion.png exists")
    all_checks_passed()
    '''),
    md(r"""
    ## 13. What this notebook showed

    - A Slater determinant is antisymmetric, vanishes when two fermions meet, is
      normalised, and its density is the sum of its orbital densities.
    - Creation and annihilation operators are ordinary matrices on the occupation-number
      states; their anticommutation relations hold exactly.
    - Wick's theorem holds for determinants and for thermal ensembles of non-interacting
      fermions; in particular $\langle :S^2:\rangle = (\mathrm{Tr}\,V\rho)^2 -
      \mathrm{Tr}(V\rho V\rho)$, the Hartree-minus-exchange identity that the Revision
      Kohn-Sham theory uses with the vertex $C$.
    - The energy of a determinant is the one-body energy plus the direct minus the
      exchange terms.
    - For two electrons on two sites: $E_0 = \tfrac12(U - \sqrt{U^2 + 16t^2})$, the best
      determinant gives $-2t + U/2$ ($U \le 2t$) or $-2t^2/U$ ($U > 2t$, unrestricted,
      symmetry broken), and the correlation energy is what no determinant captures. At
      $U = 2t$: $E_0 = -1.236068\,t$, $E_{HF} = -t$, double occupancy 0.276393 versus
      1/2.
    - The density determines the site-energy difference (Hohenberg-Kohn on two sites),
      and the exact Kohn-Sham potential exists and screens the true one; mean-field
      theory misses part of the screening (the correlation part).
    """),
]

if __name__ == "__main__":
    raise SystemExit(run_builder(__file__))
