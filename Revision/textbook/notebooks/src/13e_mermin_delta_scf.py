#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
"""Builder of Notebook 13e, "Finite temperature (Mermin) and excited states (Delta-SCF)"
(textbook "Universes in Pairs", chapter 13).

The notebook Revision/textbook/notebooks/13e_mermin_delta_scf.ipynb is BUILT from this
file by Revision/textbook/tools/nbkit.py (never edit the .ipynb by hand):

    python Revision/textbook/tools/nbkit.py build \
        Revision/textbook/notebooks/src/13e_mermin_delta_scf.py --date YYYY-MM-DD
    python Revision/textbook/tools/nbkit.py check \
        Revision/textbook/notebooks/src/13e_mermin_delta_scf.py

The Gibbs principle (Klein's inequality) on the two-site model, the factorised Gibbs
state of non-interacting fermions, Fermi-Dirac occupations with the chemical potential
by bisection, the thermodynamics F, E, S, C_V of a two-level system and of a ladder of
levels, and Janak's theorem with the Delta-SCF integral formula.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools"))
from nbkit import code, md, run_builder  # noqa: E402

FIGURES = [
    "gibbs_principle", "fermi_dirac", "bisection", "two_level_thermo",
    "ladder_occupations", "ladder_thermo", "janak_delta_scf",
]

FACTS = {
    "id": "13e",
    "name": "13e_mermin_delta_scf",
    "title": "Finite temperature (Mermin) and excited states (Delta-SCF)",
    "purpose": (
        "It checks the Gibbs principle and Klein's inequality on the 16 states of the "
        "two-site model with 2000 random density operators, shows that the Gibbs state "
        "of non-interacting fermions factorises into independent orbitals with "
        "Fermi-Dirac occupations, finds the chemical potential by bisection (and reads "
        "the rule by which the Revision Kohn-Sham solver fixes it), computes "
        "the free energy, energy, entropy and heat capacity of a two-level system (the "
        "worked numbers 0.731059, 1.164406, -0.313262, 0.393224) and of a ladder of "
        "levels with checks of dF/dT = -S and of the variance formula for the heat "
        "capacity, and checks Janak's theorem and the Delta-SCF integral formula on a "
        "model energy, with seven teaching plots."
    ),
    "records": [
        ["Revision/kohn_sham/results/parameters.json",
         "the rule by which the Revision Kohn-Sham solver fixes the chemical potential "
         "(conventions, merminRoot: mu from sum g f = N, balancing thermal particles "
         "and holes), which the notebook reads and checks"],
    ],
    "packages": ["numpy", "matplotlib"],
    "needs_rust": [],
    "expected_seconds": 10,
    "timeout_seconds": 300,
    "files_written": ["Revision/textbook/figures/13e.captions.json"] + [
        f"Revision/textbook/figures/13e_{k}_{name}.png"
        for k, name in enumerate(FIGURES, 1)
    ],
    "final_lines": [
        "PASS the figure file 13e_7_janak_delta_scf.png exists",
        "ALL 24 CHECKS PASSED (notebook 13e)",
    ],
    "troubleshooting": [
        ["\"FileNotFoundError\" for `parameters.json`",
         "the notebook reads the file `Revision/kohn_sham/results/parameters.json` of "
         "the repository; it must be opened inside the folder "
         "`Revision/textbook/notebooks` of a complete clone of the repository, not as "
         "a single downloaded file."],
    ],
}

CELLS = [
    md(r"""
    ## 1. What this notebook computes

    Density functional theory at a temperature $T > 0$ (Mermin's theorem) and for
    excited states (Delta-SCF) rests on a few exact statements. This notebook checks
    each of them with numbers. It

    - checks the Gibbs principle: among all density operators of the two-site model,
      the Gibbs state $e^{-(\hat H - \mu\hat N)/T}/Z$ has the lowest grand potential
      $\Omega$, and $\Omega - \Omega_{Gibbs} = T\,D$ with Klein's $D \ge 0$ (2000 random
      density operators);
    - checks that the Gibbs state of non-interacting fermions is a product of
      independent orbitals, each occupied with the Fermi-Dirac probability;
    - draws the Fermi-Dirac function and finds the chemical potential by bisection;
    - computes the thermodynamics of a two-level system (the worked example of the
      chapter) and of a ladder of levels: free energy, energy, entropy, heat capacity,
      with the checks $dF/dT = -S$ and $C_V = T\,dS/dT = dE/dT \ge 0$;
    - checks Janak's theorem $\partial E/\partial f_a = \epsilon_a$ and the Delta-SCF
      formula $\Delta_{SCF} = \int_0^1 [\epsilon_L(\tau) - \epsilon_H(\tau)]\,d\tau$ on a
      model energy;
    - draws seven teaching plots.
    """),
    md(r"""
    ## 3. The words used in this notebook

    - **Temperature** $T$: measured as an energy (Boltzmann's constant is set to 1).
    - **Density operator** $\hat\rho$: a Hermitian matrix with eigenvalues between 0 and
      1 that add up to 1; it describes a mixture of states with these probabilities.
    - **Entropy** $S = -\mathrm{Tr}(\hat\rho\ln\hat\rho) = -\sum_i p_i\ln p_i$, where the
      $p_i$ are the eigenvalues of $\hat\rho$ (with $0\ln 0 = 0$).
    - **Chemical potential** $\mu$: the energy that fixes the average particle number.
    - **Grand potential** $\Omega[\hat\rho] = \mathrm{Tr}[\hat\rho(\hat H - \mu\hat N)]
      - T S$; **Gibbs state** $\hat\rho_0 = e^{-(\hat H - \mu\hat N)/T}/Z$ with
      $Z = \mathrm{Tr}\,e^{-(\hat H - \mu\hat N)/T}$; $\Omega[\hat\rho_0] = -T\ln Z$.
    - **Klein's inequality**: $D = \mathrm{Tr}[\hat\rho(\ln\hat\rho -
      \ln\hat\sigma)] \ge 0$ for two density operators, with equality only when they are
      equal.
    - **Fermi-Dirac occupation** $f(\epsilon) = 1/(e^{(\epsilon - \mu)/T} + 1)$: the
      probability that an orbital of energy $\epsilon$ is occupied.
    - **Free energy** $F = E - TS$; **heat capacity** $C_V = dE/dT$ at a fixed particle
      number.
    - **Bisection**: halving an interval that contains the root until it is small.
    - **Janak's theorem**: the derivative of the self-consistent energy with respect to
      the occupation $f_a$ of an orbital is its level $\epsilon_a$.
    - **Delta-SCF**: the excitation energy as the difference of two self-consistent
      energies, with one particle moved from the highest occupied orbital (H) to the
      lowest empty one (L).
    """),
    md(r"""
    ## 4. The physical and mathematical situation

    **Gibbs principle.** For every density operator $\hat\rho$ and the Gibbs state
    $\hat\rho_0$: since $\hat H - \mu\hat N = -T\ln\hat\rho_0 - T\ln Z$,

    $$\Omega[\hat\rho] = -T\ln Z + T\,\mathrm{Tr}[\hat\rho(\ln\hat\rho -
    \ln\hat\rho_0)] = \Omega[\hat\rho_0] + T\,D \ge \Omega[\hat\rho_0] .$$

    **Non-interacting fermions.** If $\hat H - \mu\hat N = \sum_a (\epsilon_a - \mu)\hat
    n_a$, the weight of the configuration $(n_0, n_1, \dots)$ in the Gibbs state is the
    product $\prod_a p_a(n_a)$ with $p_a(1) = f_a$, $p_a(0) = 1 - f_a$: the orbitals are
    independent. The entropy is then $S = -\sum_a [f_a\ln f_a + (1 - f_a)\ln(1 - f_a)]$.

    **Fixed particle number.** $\sum_a g_a f_a = N$ ($g_a$: the number of states of
    level $a$) increases strictly with $\mu$, so exactly one $\mu$ solves it; bisection
    finds it. Then $E = \sum g_a f_a\epsilon_a$, $F = E - TS$, and because $F$ is
    stationary in the occupations (envelope theorem), $dF/dT = -S$ and
    $C_V = dE/dT = T\,dS/dT$. With $w_a = g_a f_a(1 - f_a)$ one finds
    $C_V = \frac{1}{T^2}\big[\sum_a w_a(\epsilon_a - \mu)^2 - (\sum_a w_a(\epsilon_a -
    \mu))^2/\sum_a w_a\big] \ge 0$ (a weighted variance).

    **Janak and Delta-SCF.** For the model energy
    $E(f_H, f_L) = \epsilon_H^0 f_H + \epsilon_L^0 f_L + \tfrac{U}{2}(f_H^2 + f_L^2)$
    the levels are $\epsilon_a = \partial E/\partial f_a = \epsilon_a^0 + U f_a$. Moving
    a fraction $\tau$ from H to L ($f_H = 1 - \tau$, $f_L = \tau$) gives
    $dE/d\tau = \epsilon_L(\tau) - \epsilon_H(\tau)$, so
    $\Delta_{SCF} = E(0, 1) - E(1, 0) = \int_0^1[\epsilon_L(\tau) - \epsilon_H(\tau)]
    \,d\tau$.

    **Status.** Exact finite-dimensional statements (PROVED: they follow from the
    definitions; this notebook checks each one to rounding); toy numbers, no Revision
    number is reproduced. The Revision Kohn-Sham solver uses the same Mermin
    occupations with $\mu$ fixed by $\sum g f = N$; section 8 reads this rule from the
    solver's parameter file. That a Delta-SCF state approximates a true excited state
    is an ASSUMPTION of the method; Janak's theorem itself is exact.
    """),
    md(r"""
    ## 5. The Gibbs principle on the two-site model

    The next cell builds the 16 occupation-number states of four orbitals (L up, R up, L
    down, R down), the annihilation operators as $16 \times 16$ matrices (with the sign
    $(-1)^{\nu_p}$), the two-site Hamiltonian with hopping $t = 1$ and repulsion
    $U = 2$, and the particle-number operator.
    """),
    code(r'''
    import itertools  # loops over combinations

    import numpy as np  # arrays, matrices and linear algebra

    M, DIM = 4, 16  # four orbitals, sixteen occupation-number states
    a = []  # annihilation operators
    for p in range(M):
        matrix = np.zeros((DIM, DIM))
        for state in range(DIM):
            if (state >> p) & 1:  # orbital p is occupied in this state
                nu = sum((state >> q) & 1 for q in range(p))  # occupied before p
                matrix[state ^ (1 << p), state] = (-1) ** nu
        a.append(matrix)
    a_dag = [matrix.T for matrix in a]
    n_op = [a_dag[p] @ a[p] for p in range(M)]
    N_op = sum(n_op)  # the particle-number operator
    H = -(a_dag[0] @ a[1] + a_dag[1] @ a[0] + a_dag[2] @ a[3] + a_dag[3] @ a[2]) \
        + 2.0 * (n_op[0] @ n_op[2] + n_op[1] @ n_op[3])  # t = 1, U = 2
    check(np.allclose(H, H.T) and np.allclose(H @ N_op, N_op @ H),
          "H is symmetric and conserves the particle number")
    '''),
    md(r"""
    The next cell defines the matrix function $f(A) = \sum_i f(a_i)\,u_i u_i^\dagger$
    through the eigenvalues $a_i$ and eigenvectors $u_i$ of a Hermitian matrix, the
    entropy, and the grand potential. It builds the Gibbs state at $\mu = 1$, $T = 0.5$
    and checks $\Omega[\hat\rho_0] = -T\ln Z$.
    """),
    code(r'''
    MU, TEMPERATURE = 1.0, 0.5
    K = H - MU * N_op  # H - mu N


    def entropy(rho):
        """S = -sum p ln p over the eigenvalues p of rho (0 ln 0 = 0)."""
        p = np.clip(np.linalg.eigvalsh(rho), 0.0, None)
        p = p[p > 1e-300]
        return float(-np.sum(p * np.log(p)))


    def grand_potential(rho):
        """Omega = Tr[rho (H - mu N)] - T S."""
        return float(np.trace(rho @ K).real) - TEMPERATURE * entropy(rho)


    k_values, k_vectors = np.linalg.eigh(K)
    boltzmann = np.exp(-(k_values - k_values.min()) / TEMPERATURE)  # shifted weights
    Z_shifted = boltzmann.sum()
    rho_gibbs = (k_vectors * (boltzmann / Z_shifted)) @ k_vectors.T
    ln_Z = np.log(Z_shifted) - k_values.min() / TEMPERATURE  # undo the shift
    omega_gibbs = grand_potential(rho_gibbs)
    report("Omega of the Gibbs state", f"{omega_gibbs:.10f}")
    report("-T ln Z", f"{-TEMPERATURE * ln_Z:.10f}")
    check(abs(omega_gibbs + TEMPERATURE * ln_Z) < 1e-12, "Omega[Gibbs] = -T ln Z")
    '''),
    md(r"""
    The next cell makes 2000 random density operators: a random complex matrix $A$
    gives the density operator $AA^\dagger/\mathrm{Tr}(AA^\dagger)$ (Hermitian, with
    non-negative eigenvalues and trace 1); mixing it with the Gibbs state with a random
    weight $s$ gives states near and far from the minimum. For each it computes
    $\Omega - \Omega_0$ and Klein's $D = \mathrm{Tr}[\hat\rho(\ln\hat\rho -
    \ln\hat\rho_0)]$, and checks $\Omega - \Omega_0 = T D \ge 0$.
    """),
    code(r'''
    ln_rho_gibbs = (k_vectors * (-k_values / TEMPERATURE - ln_Z)) @ k_vectors.T


    def matrix_log(rho):
        """ln rho through the eigenvalues (all positive here)."""
        values, vectors = np.linalg.eigh(rho)
        return (vectors * np.log(values)) @ vectors.conj().T


    rng = np.random.default_rng(12345)  # fixed seed: the same numbers every run
    gaps, kleins = [], []
    for _ in range(2000):
        A = rng.normal(size=(DIM, DIM)) + 1j * rng.normal(size=(DIM, DIM))
        random_rho = A @ A.conj().T
        random_rho /= np.trace(random_rho).real
        s = rng.uniform(0.0, 1.0)  # how far from the Gibbs state
        rho = (1.0 - s) * rho_gibbs + s * random_rho
        gaps.append(grand_potential(rho) - omega_gibbs)
        kleins.append(np.trace(rho @ (matrix_log(rho) - ln_rho_gibbs)).real)
    gaps, kleins = np.array(gaps), np.array(kleins)
    say(f"smallest Omega - Omega_0 among 2000 states: {gaps.min():.3e}")
    check(np.all(gaps > 0.0), "every random density operator has Omega > Omega[Gibbs]")
    check(np.max(np.abs(gaps - TEMPERATURE * kleins)) < 1e-10,
          "Omega - Omega[Gibbs] = T D with Klein's D (identity)")
    '''),
    md(r"""
    The next cell draws the distribution of $\Omega - \Omega_0$ of the 2000 states as a
    histogram on a logarithmic axis.
    """),
    code(r'''
    fig, ax = plt.subplots()
    bins = np.logspace(np.floor(np.log10(gaps.min())), np.ceil(np.log10(gaps.max())), 40)
    ax.hist(gaps, bins=bins, color="tab:blue", edgecolor="black", lw=0.5)
    ax.set_xscale("log")
    ax.set_xlabel("$\\Omega[\\hat\\rho] - \\Omega[\\hat\\rho_0]$ (units of $t$)")
    ax.set_ylabel("number of random states")
    ax.set_title("The Gibbs state has the lowest grand potential")
    save_figure(fig, "gibbs_principle",
                "Histogram of the grand potential of 2000 random density operators of "
                "the two-site model ($t = 1$, $U = 2$, $\\mu = 1$, $T = 0.5$) minus "
                "that of the Gibbs state, on a logarithmic horizontal axis (units of "
                "$t$); the vertical axis counts the states in each bin. All 2000 "
                "differences are positive: no state beats the Gibbs state, as the "
                "Gibbs principle and Klein's inequality say. States mixed only "
                "slightly away from the Gibbs state have the smallest differences.")
    '''),
    md(r"""
    ## 6. Non-interacting fermions: independent orbitals

    The next cell takes three orbitals with energies $-0.5, 0.2, 1.0$, $\mu = 0.1$,
    $T = 0.4$, and compares the Gibbs weight $e^{-\sum_a(\epsilon_a - \mu)n_a/T}/Z$ of
    each of the 8 configurations with the product of the single-orbital probabilities
    $f_a$ or $1 - f_a$.
    """),
    code(r'''
    levels3 = np.array([-0.5, 0.2, 1.0])
    mu3, T3 = 0.1, 0.4
    configurations = list(itertools.product((0, 1), repeat=3))
    weights = np.array([np.exp(-np.dot(levels3 - mu3, c) / T3) for c in configurations])
    weights /= weights.sum()  # divide by Z
    f3 = 1.0 / (np.exp((levels3 - mu3) / T3) + 1.0)
    products = np.array([np.prod([f3[k] if c[k] else 1.0 - f3[k] for k in range(3)])
                         for c in configurations])
    for c, wgt, prod in zip(configurations, weights, products):
        say(f"occupations {c}: Gibbs weight {wgt:.6f}, product {prod:.6f}")
    check(np.max(np.abs(weights - products)) < 1e-15,
          "the Gibbs weights are products of independent Fermi-Dirac probabilities")
    '''),
    md(r"""
    ## 7. The Fermi-Dirac function

    The next cell defines $f$ in a form that a computer can evaluate for every
    argument: $e^{x}$ overflows (exceeds the largest number the computer can store,
    about $10^{308}$) for $x > 709$, so the cell uses $f = e^{-\ln(1 + e^{x})}$ with
    numpy's `logaddexp(0, x)` $= \ln(e^0 + e^x)$, which never overflows. It draws
    $f(\epsilon)$ for four temperatures around $\mu = 0$ and checks $f(\mu) = 1/2$ and
    the symmetry $f(\mu + \delta) = 1 - f(\mu - \delta)$ (a hole below $\mu$ is as
    likely as a particle above it).
    """),
    code(r'''
    def fermi(energy, mu, temperature):
        """The Fermi-Dirac occupation 1 / (exp(x) + 1), x = (energy - mu)/T, written
        as exp(-ln(1 + e^x)) so that no overflow can occur."""
        x = (np.asarray(energy, dtype=float) - mu) / temperature
        return np.exp(-np.logaddexp(0.0, x))


    eps = np.linspace(-2.0, 2.0, 801)
    check(abs(fermi(0.0, 0.0, 0.3) - 0.5) < 1e-15
          and np.allclose(fermi(eps, 0.0, 0.3), 1.0 - fermi(-eps, 0.0, 0.3), atol=1e-15),
          "f(mu) = 1/2 and f(mu + d) = 1 - f(mu - d)")
    fig, ax = plt.subplots()
    for temperature in (0.02, 0.1, 0.3, 1.0):
        ax.plot(eps, fermi(eps, 0.0, temperature), label=f"$T = {temperature}$")
    ax.axvline(0.0, color="gray", ls="--", lw=0.8)
    ax.set_xlabel("orbital energy $\\epsilon - \\mu$")
    ax.set_ylabel("occupation $f$")
    ax.set_title("The Fermi-Dirac occupation")
    ax.legend()
    save_figure(fig, "fermi_dirac",
                "The Fermi-Dirac occupation $f = 1/(e^{(\\epsilon - \\mu)/T} + 1)$ "
                "against the orbital energy measured from the chemical potential, for "
                "four temperatures (energies and temperatures in the same units). At "
                "low $T$ it is a step (occupied below $\\mu$, empty above: the aufbau "
                "rule); a higher $T$ smears the step over a width of a few $T$; at "
                "$\\epsilon = \\mu$ it is always 1/2.")
    '''),
    md(r"""
    ## 8. Two levels, one particle: the chemical potential by bisection

    Two levels $\epsilon_0 = 0$, $\epsilon_1 = 1$ (one state each), one particle,
    $T = 1/2$. The next cell finds $\mu$ by bisection on $f_0 + f_1 - 1$, recording the
    width of the interval at every step, and computes the worked numbers of the
    chapter. The bisection starts from an interval that surely contains $\mu$: from the
    lowest level minus $50T + 5$ to the highest level plus 5, here $[-30, 6]$. At its
    lower end every occupation is below $e^{-50}$, so the levels hold fewer than $N$
    particles; at its upper end they hold almost all their states (here nearly 2),
    more than $N = 1$. The entropy of one state of energy
    $\epsilon$ is $-f\ln f - (1 - f)\ln(1 - f)$; with $x = (\epsilon - \mu)/T$ it equals
    $\ln(1 + e^{-|x|}) + |x|\,f(|x|)$ (insert $f = 1/(e^x + 1)$ and simplify), a form
    without $\ln 0$ that the cell uses.
    """),
    code(r'''
    def chemical_potential(levels, degeneracies, N, temperature, history=None):
        """mu with sum g f = N, by bisection (the sum increases with mu)."""
        low, high = levels.min() - 50.0 * temperature - 5.0, levels.max() + 5.0
        for _ in range(100):
            middle = 0.5 * (low + high)
            if np.sum(degeneracies * fermi(levels, middle, temperature)) < N:
                low = middle  # too few particles: mu must rise
            else:
                high = middle
            if history is not None:
                history.append(high - low)
        return 0.5 * (low + high)


    def thermodynamics(levels, degeneracies, N, temperature):
        """mu, occupations, E, S, F of non-interacting levels at fixed N."""
        mu = chemical_potential(levels, degeneracies, N, temperature)
        f = fermi(levels, mu, temperature)
        x = np.abs(levels - mu) / temperature
        s_level = np.logaddexp(0.0, -x) + x * fermi(x, 0.0, 1.0)  # entropy of a state
        S = np.sum(degeneracies * s_level)
        E = np.sum(degeneracies * f * levels)
        return mu, f, E, S, E - temperature * S


    two_levels, ones = np.array([0.0, 1.0]), np.array([1.0, 1.0])
    widths = []
    chemical_potential(two_levels, ones, 1.0, 0.5, widths)
    mu2, f2, E2, S2, F2 = thermodynamics(two_levels, ones, 1.0, 0.5)
    report("mu", f"{mu2:.6f}")
    report("f_0, f_1", f"{f2[0]:.6f}, {f2[1]:.6f}")
    report("E, S, F", f"{E2:.6f}, {S2:.6f}, {F2:.6f}")
    check(abs(mu2 - 0.5) < 1e-12 and abs(f2[0] - 0.731059) < 1e-6
          and abs(f2[1] - 0.268941) < 1e-6,
          "mu = 1/2, f_0 = 0.731059, f_1 = 0.268941")
    check(abs(E2 - 0.268941) < 1e-6 and abs(S2 - 1.164406) < 1e-6
          and abs(F2 + 0.313262) < 1e-6, "E = 0.268941, S = 1.164406, F = -0.313262")
    '''),
    md(r"""
    The Revision Kohn-Sham solver of the dirac16complex field fixes its chemical
    potential by the same condition $\sum g f = N$. The next cell reads how from the
    solver's parameter file. With many particles the direct difference
    $\sum g f - N$ loses digits (two large, nearly equal numbers are subtracted), so the
    solver splits the levels at a dividing point and balances the thermally excited
    particles above it against the holes below it; a hole is counted with $f(-x)$,
    which equals $1 - f(x)$ (section 7) but is computed without a subtraction. It
    finds the root of this balance, written with logarithms (the form it calls
    LogBalance), by Newton steps safeguarded by bisection.
    """),
    code(r'''
    parameters = json.loads(repository_file(
        "Revision/kohn_sham/results/parameters.json").read_text(encoding="utf-8"))
    root_rule = parameters["conventions"]["merminRoot"]  # a sentence of the record
    root_form = parameters["numerics"]["merminRoot"]  # the name of the canonical form
    say(f"Revision solver: canonical root form {root_form}")
    check(root_rule.startswith("mu from sum g f = N")
          and "holes below a split of the levels" in root_rule
          and root_form == "LogBalance",
          "the Revision solver fixes mu by sum g f = N, balancing particles and holes "
          "(Revision/kohn_sham/results/parameters.json, conventions merminRoot)")
    '''),
    md(r"""
    The next cell computes $dF/dT$ and $dE/dT$ by central differences (with $\mu$ solved
    again at $T \pm 10^{-4}$), checks $dF/dT = -S$ and $C_V = dE/dT = T\,dS/dT$, and draws
    the bisection history.
    """),
    code(r'''
    def at(temperature, levels=two_levels, degeneracies=ones, N=1.0):
        return thermodynamics(levels, degeneracies, N, temperature)


    d = 1e-4
    dF_dT = (at(0.5 + d)[4] - at(0.5 - d)[4]) / (2 * d)
    dE_dT = (at(0.5 + d)[2] - at(0.5 - d)[2]) / (2 * d)
    T_dS_dT = 0.5 * (at(0.5 + d)[3] - at(0.5 - d)[3]) / (2 * d)
    report("dF/dT", f"{dF_dT:.6f}")
    report("C_V = dE/dT", f"{dE_dT:.6f}")
    check(abs(dF_dT + S2) < 1e-7, "dF/dT = -S (envelope theorem)")
    check(abs(dE_dT - 0.393224) < 1e-6 and abs(T_dS_dT - dE_dT) < 1e-7,
          "C_V = dE/dT = T dS/dT = 0.393224")
    fig, ax = plt.subplots()
    ax.semilogy(range(1, 51), widths[:50], "o-", ms=3)
    ax.set_xlabel("bisection step")
    ax.set_ylabel("width of the interval that contains $\\mu$")
    ax.set_title("Bisection halves the interval at every step")
    save_figure(fig, "bisection",
                "The width of the interval that contains the chemical potential during "
                "the bisection for two levels and one particle at $T = 1/2$, against "
                "the step number, on a logarithmic vertical axis (energy units). Every "
                "step halves the width (a straight line that falls by "
                "$\\log_{10} 2 = 0.30$ per step), from 18 after the first step to about "
                "$3 \\times 10^{-14}$ after 50 steps, which fixes $\\mu$ to 13 decimal "
                "places.")
    check(all(abs(b / a_ - 0.5) < 1e-12 for a_, b in zip(widths[:40], widths[1:41])),
          "every bisection step halves the interval")
    '''),
    md(r"""
    ## 9. The two-level system at all temperatures

    The next cell computes $E$, $S$, $F$ and $C_V = T\,dS/dT$ (by central differences)
    from $T = 0.02$ to $T = 3$, checks the limits ($S \to 0$ as $T \to 0$;
    $S \to \ln 4$ and $E \to 1/2$ as $T \to \infty$: the four configurations become
    equally likely) and draws them.
    """),
    code(r'''
    temperatures = np.linspace(0.02, 3.0, 150)
    table = np.array([at(T)[2:] for T in temperatures])  # columns E, S, F
    C_V = np.array([T * (at(T + d)[3] - at(T - d)[3]) / (2 * d) for T in temperatures])
    hot = at(1000.0)
    check(table[0, 1] < 1e-8 and abs(hot[3] - np.log(4.0)) < 1e-5
          and abs(hot[2] - 0.5) < 1e-3, "S -> 0 for T -> 0; S -> ln 4, E -> 1/2 for T "
          "-> infinity")
    check(np.all(C_V >= 0.0), "the heat capacity is never negative")
    fig, (left, right) = plt.subplots(1, 2, figsize=(10.0, 4.0))
    left.plot(temperatures, table[:, 0], label="energy $E$")
    left.plot(temperatures, temperatures * table[:, 1], label="$T S$")
    left.plot(temperatures, table[:, 2], color="black", label="free energy $F = E - TS$")
    left.set_xlabel("temperature $T$")
    left.set_ylabel("energy (level-spacing units)")
    left.legend(fontsize=8)
    right.plot(temperatures, C_V, color="tab:red")
    right.plot([0.5], [0.393224], "ko", label="$T = 1/2$: $C_V = 0.393224$")
    right.set_xlabel("temperature $T$")
    right.set_ylabel("heat capacity $C_V = dE/dT$")
    right.legend(fontsize=8)
    fig.suptitle("Two levels (0 and 1), one particle")
    save_figure(fig, "two_level_thermo",
                "Thermodynamics of one particle in two levels $\\epsilon_0 = 0$, "
                "$\\epsilon_1 = 1$ against the temperature (level-spacing units). "
                "Left: the energy $E$, the product $TS$ of temperature and entropy, "
                "and the free energy $F = E - TS$, which falls with $T$ at the rate "
                "$-S$. Right: the heat capacity $C_V = dE/dT$, which has a single peak "
                "(it vanishes at low $T$, where the upper level is almost never "
                "occupied, and at "
                "high $T$, where both levels are already equally occupied); the black "
                "point is the worked value at $T = 1/2$.")
    '''),
    md(r"""
    ## 10. A ladder of levels

    The next cell takes the levels $\epsilon_n = n + 1/2$ ($n = 0, \dots, 59$), two
    states each (two labels), with $N = 8$ particles: the trap of Notebook 13a without
    interaction. At low $T$ the four lowest levels are full and $\mu$ lies halfway
    between the highest full level 3.5 and the lowest empty level 4.5. The cell computes
    $\mu$, $E$, $S$ and $C_V$ (by central differences and by the variance formula of
    section 4) for 120 temperatures.
    """),
    code(r'''
    ladder = np.arange(60) + 0.5
    twos = 2.0 * np.ones(60)
    N_LADDER = 8.0


    def ladder_at(T):
        return thermodynamics(ladder, twos, N_LADDER, T)


    def variance_heat_capacity(T):
        """C_V = [sum w x^2 - (sum w x)^2 / sum w] / T^2, x = eps - mu, w = g f (1 - f)."""
        mu, f = ladder_at(T)[:2]
        w = twos * f * (1.0 - f)
        x = ladder - mu
        return (np.sum(w * x * x) - np.sum(w * x) ** 2 / np.sum(w)) / T ** 2


    T_ladder = np.linspace(0.05, 3.0, 120)
    mus = np.array([ladder_at(T)[0] for T in T_ladder])
    C_numeric = np.array([(ladder_at(T + d)[2] - ladder_at(T - d)[2]) / (2 * d)
                          for T in T_ladder])
    C_variance = np.array([variance_heat_capacity(T) for T in T_ladder])
    report("mu at T = 0.05", f"{mus[0]:.6f}")
    check(abs(mus[0] - 4.0) < 1e-6, "at low T, mu lies halfway between 3.5 and 4.5")
    check(np.max(np.abs(C_numeric - C_variance)) < 1e-5 * max(1.0, C_variance.max()),
          "the heat capacity equals the weighted-variance formula")
    check(np.all(C_variance >= 0.0), "the variance formula is never negative")
    '''),
    md(r"""
    The next cell draws the occupations of the ladder at four temperatures.
    """),
    code(r'''
    fig, ax = plt.subplots()
    for T, marker in ((0.05, "o"), (0.5, "s"), (1.0, "^"), (2.0, "v")):
        mu, f = ladder_at(T)[:2]
        ax.plot(ladder[:12], f[:12], marker + "-", ms=4,
                label=f"$T = {T}$, $\\mu = {mu:.3f}$")
    ax.set_xlabel("level $\\epsilon_n = n + 1/2$")
    ax.set_ylabel("occupation $f_n$ of each of the two states")
    ax.set_title("Eight particles in a ladder of levels")
    ax.legend(fontsize=8)
    save_figure(fig, "ladder_occupations",
                "The Fermi-Dirac occupation of the levels $\\epsilon_n = n + 1/2$ (two "
                "states each) holding eight particles, at four temperatures (energy "
                "units of the level spacing); the chemical potential of each "
                "temperature is in the legend. At $T = 0.05$ the four lowest levels are "
                "full and the others empty; as $T$ grows, particles move from below "
                "$\\mu$ to above it and $\\mu$ falls.")
    '''),
    md(r"""
    The next cell draws $\mu$ and $C_V$ of the ladder against the temperature.
    """),
    code(r'''
    fig, (left, right) = plt.subplots(1, 2, figsize=(10.0, 4.0))
    left.plot(T_ladder, mus, color="black")
    left.set_xlabel("temperature $T$")
    left.set_ylabel("chemical potential $\\mu$")
    right.plot(T_ladder, C_numeric, color="tab:red", label="$dE/dT$ (differences)")
    right.plot(T_ladder[::6], C_variance[::6], "ko", ms=3, label="variance formula")
    right.set_xlabel("temperature $T$")
    right.set_ylabel("heat capacity $C_V$")
    right.legend(fontsize=8)
    fig.suptitle("Ladder of levels, eight particles")
    save_figure(fig, "ladder_thermo",
                "Left: the chemical potential of eight particles in the ladder "
                "$\\epsilon_n = n + 1/2$ (two states per level) against the "
                "temperature; it starts at 4, halfway between the last full and the "
                "first empty level, and falls as $T$ grows. Right: the heat capacity "
                "from the difference quotient of $E(T)$ (line) and from the "
                "weighted-variance formula (points); they agree, and both are never "
                "negative. Temperatures and energies in units of the level spacing.")
    '''),
    md(r"""
    ## 11. Janak's theorem and Delta-SCF on a model energy

    The next cell takes the model energy of section 4 with $\epsilon_H^0 = 0$,
    $\epsilon_L^0 = 1$, $U = 0.2$, checks Janak's theorem by difference quotients,
    computes the Kohn-Sham gap $\Delta_{KS} = \epsilon_L - \epsilon_H$ of the ground
    state $(f_H, f_L) = (1, 0)$, the Delta-SCF energy $E(0, 1) - E(1, 0)$, the integral
    of the level difference over $\tau$ (Simpson's rule) and the transition-state value
    at $\tau = 1/2$.
    """),
    code(r'''
    EPS_H0, EPS_L0, U_MODEL = 0.0, 1.0, 0.2


    def model_energy(f_H, f_L):
        return EPS_H0 * f_H + EPS_L0 * f_L + 0.5 * U_MODEL * (f_H ** 2 + f_L ** 2)


    def model_levels(f_H, f_L):
        """Janak: eps_a = dE/df_a = eps_a^0 + U f_a."""
        return EPS_H0 + U_MODEL * f_H, EPS_L0 + U_MODEL * f_L


    h_step = 1e-6
    for f_H, f_L in ((1.0, 0.0), (0.5, 0.5), (0.3, 0.9)):
        dE_dfH = (model_energy(f_H + h_step, f_L) - model_energy(f_H - h_step, f_L)) \
            / (2 * h_step)
        dE_dfL = (model_energy(f_H, f_L + h_step) - model_energy(f_H, f_L - h_step)) \
            / (2 * h_step)
        check(np.allclose((dE_dfH, dE_dfL), model_levels(f_H, f_L), atol=1e-9),
              f"Janak: dE/df_a = eps_a at (f_H, f_L) = ({f_H}, {f_L})")
    taus = np.linspace(0.0, 1.0, 101)
    integrand = np.array([model_levels(1 - t, t)[1] - model_levels(1 - t, t)[0]
                          for t in taus])
    gap_KS = integrand[0]
    delta_SCF = model_energy(0.0, 1.0) - model_energy(1.0, 0.0)
    step = taus[1] - taus[0]
    janak_integral = step / 3 * (integrand[0] + integrand[-1]
                                 + 4 * integrand[1:-1:2].sum() + 2 * integrand[2:-1:2].sum())
    report("Kohn-Sham gap", f"{gap_KS:.6f}")
    report("Delta-SCF", f"{delta_SCF:.6f}")
    report("integral of eps_L - eps_H over tau", f"{janak_integral:.6f}")
    report("transition state (tau = 1/2)", f"{integrand[50]:.6f}")
    check(abs(gap_KS - 0.8) < 1e-12 and abs(delta_SCF - 1.0) < 1e-12
          and abs(janak_integral - delta_SCF) < 1e-12 and abs(integrand[50] - 1.0) < 1e-12,
          "gap 0.8, Delta-SCF 1.0 = the Janak integral = the transition state")
    check(abs(delta_SCF - gap_KS - U_MODEL) < 1e-12, "Delta-SCF - gap = U (relaxation)")
    '''),
    md(r"""
    The next cell draws the energy along the transfer and the level difference whose
    area is the Delta-SCF energy.
    """),
    code(r'''
    energies_tau = np.array([model_energy(1 - t, t) for t in taus])
    fig, (left, right) = plt.subplots(1, 2, figsize=(10.0, 4.0))
    left.plot(taus, energies_tau - energies_tau[0], color="black")
    left.set_xlabel("transferred fraction $\\tau$")
    left.set_ylabel("$E(\\tau) - E(0)$")
    left.set_title("energy along the transfer")
    right.fill_between(taus, 0.0, integrand, alpha=0.25, label="area = Delta-SCF = 1")
    right.plot(taus, integrand, color="black", label="$\\epsilon_L - \\epsilon_H$")
    right.plot([0.0], [gap_KS], "s", ms=8, label="Kohn-Sham gap 0.8")
    right.plot([0.5], [integrand[50]], "^", ms=8, label="transition state 1.0")
    right.set_ylim(0.0, 1.3)
    right.set_xlabel("transferred fraction $\\tau$")
    right.set_ylabel("level difference")
    right.legend(fontsize=8, loc="lower right")
    fig.suptitle("Janak's theorem and Delta-SCF ($\\epsilon_H^0 = 0$, "
                 "$\\epsilon_L^0 = 1$, $U = 0.2$)")
    save_figure(fig, "janak_delta_scf",
                "The model energy $E = \\epsilon_H^0 f_H + \\epsilon_L^0 f_L + "
                "(U/2)(f_H^2 + f_L^2)$ when a fraction $\\tau$ of a particle is moved "
                "from H to L (left: the energy gained, rising to 1), and the level "
                "difference $\\epsilon_L - \\epsilon_H = 0.8 + 0.4\\tau$, which is the "
                "slope of the left curve by Janak's theorem (right). The Kohn-Sham gap "
                "0.8 is the value at $\\tau = 0$; the area, the Delta-SCF energy 1.0, "
                "exceeds it by $U = 0.2$ (orbital relaxation), and the midpoint value "
                "(transition state) is exact here because the line is straight.")
    '''),
    md(r"""
    ## 12. The last check

    The last cell checks that all seven figure files exist and prints the number of
    checks that passed.
    """),
    code(r'''
    figure_names = ["gibbs_principle", "fermi_dirac", "bisection", "two_level_thermo",
                    "ladder_occupations", "ladder_thermo", "janak_delta_scf"]
    missing = [name for k, name in enumerate(figure_names, 1)
               if not output_file(f"{FIGURE_FOLDER}/13e_{k}_{name}.png").is_file()]
    check(missing == [], "all seven figure files exist")
    check(output_file(f"{FIGURE_FOLDER}/13e_7_janak_delta_scf.png").is_file(),
          "the figure file 13e_7_janak_delta_scf.png exists")
    all_checks_passed()
    '''),
    md(r"""
    ## 13. What this notebook showed

    - The Gibbs state has the lowest grand potential of all density operators; the
      excess of any other state is $T$ times Klein's $D \ge 0$ (2000 random states).
      This is the variational principle behind Mermin's finite-temperature DFT.
    - For non-interacting fermions the Gibbs state is a product of independent orbitals
      with the Fermi-Dirac occupations; the entropy is the sum of the orbital entropies.
    - The chemical potential is found by bisection from $\sum g f = N$; every step halves
      the interval.
    - Two levels at $T = 1/2$: $f_0 = 0.731059$, $E = 0.268941$, $S = 1.164406$,
      $F = -0.313262$, $dF/dT = -S$, $C_V = 0.393224$; the heat capacity has one peak.
    - For a ladder of levels the heat capacity from $dE/dT$ equals the weighted-variance
      formula, so it is never negative.
    - Janak's theorem holds, and the Delta-SCF excitation energy is the integral of the
      level difference over the transferred fraction; in the model it exceeds the
      Kohn-Sham gap by $U$.
    """),
]

if __name__ == "__main__":
    raise SystemExit(run_builder(__file__))
