#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
"""Builder of Notebook 19a, "The Rust Kohn-Sham solver for the universes of mass +M and -M"
(textbook "Universes in Pairs", chapter 19: T3, the Kohn-Sham universes of mass +M and -M).

The notebook Revision/textbook/notebooks/19a_t3_rust_pairs.ipynb is BUILT from this file by
Revision/textbook/tools/nbkit.py (never edit the .ipynb by hand):

    python Revision/textbook/tools/nbkit.py build \
        Revision/textbook/notebooks/src/19a_t3_rust_pairs.py --date YYYY-MM-DD
    python Revision/textbook/tools/nbkit.py check \
        Revision/textbook/notebooks/src/19a_t3_rust_pairs.py

The notebook builds the Revision Kohn-Sham solver (Revision/kohn_sham/solver) with cargo and
runs its subcommand "single" for the universe of mass +M (m, lambda, tip angle 0), its T3
partner of mass -M (-m, +lambda, tip angle pi), the negative control with the untransformed
tip (-m, +lambda, tip angle 0) and the wrong partner (-m, -lambda, tip angle pi): at N = 8,
136 and 688, along the deflating history, for five couplings and at three temperatures. It
reproduces the solver's T3 self-test of Revision/kohn_sham/reports/ks-rust-solver.json and
the committed canonical states of Revision/kohn_sham/results, and draws ten overlay figures.
The solver's raw output goes into Revision/kohn_sham/solver/target/textbook_19a (ignored by
git).
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools"))
from nbkit import code, md, run_builder  # noqa: E402

FIGURES = [
    "19a_1_level_ladder",
    "19a_2_level_differences",
    "19a_3_density_profiles",
    "19a_4_mass_and_potential",
    "19a_5_emt_profiles",
    "19a_6_zero_modes_n8",
    "19a_7_history_energy",
    "19a_8_history_agreement",
    "19a_9_coupling_scan",
    "19a_10_thermal_states",
]

FACTS = {
    "id": "19a",
    "name": "19a_t3_rust_pairs",
    "title": "The Rust Kohn-Sham solver for the universes of mass +M and -M",
    "purpose": (
        "It builds the Rust Kohn-Sham solver of the repository with cargo (about a "
        "minute when the program is missing, a second when it is up to date) and solves "
        "the Kohn-Sham problem of dirac16complex in the deflating primordial field for "
        "the universe of mass +M (bare mass m, coupling lambda, tip angle 0), for its "
        "partner of theorem T3 (bare mass -m, the same coupling, tip angle pi), for the "
        "negative control with the untransformed tip (bare mass -m, tip angle 0) and for "
        "the wrong partner with the reversed coupling (-m, -lambda, tip angle pi). It "
        "does this for 8, 136 and 688 particles, at the five instants of the deflating "
        "history, for five couplings and at three temperatures (59 runs). It checks that "
        "the partners have the same levels, occupations, energies and energy-momentum "
        "profiles and the opposite scalar density, that the controls differ, that the "
        "+M runs reproduce the committed canonical states, and that the solver's own T3 "
        "self-test is reproduced number by number, and it draws ten overlay figures. "
        "The solver writes its raw output (about 2 MB) into the folder "
        "`Revision/kohn_sham/solver/target/textbook_19a`, which git ignores."
    ),
    "records": [
        ["Revision/kohn_sham/reports/ks-rust-solver.json",
         "the 42 checks of the solver; its check t3_block_map_solver_selftest is "
         "reproduced number by number"],
        ["Revision/kohn_sham/results/parameters.json",
         "the parameters of the canonical matrix and the couplings lambda_1 and "
         "lambda_2 for each particle number"],
        ["Revision/kohn_sham/results/ground",
         "the committed canonical ground states (summary, levels, profiles and "
         "energy-momentum integrals) that the +M runs must reproduce"],
        ["Revision/kohn_sham/results/thermo/thermodynamics.csv",
         "the committed thermal states that the +M runs at temperature T must "
         "reproduce"],
        ["Revision/pairing/kohn_sham/t3-theory.json",
         "theorem T3 with its hypotheses, its statement and what it does not establish"],
        ["Revision/pairing/kohn_sham/reports/wolfram-t3.json",
         "the 10 exact Wolfram checks of the proof of T3, all PASS"],
        ["Revision/pairing/kohn_sham/reports/python-t3.json",
         "the 13 independent sympy checks of T3, all PASS"],
    ],
    "packages": ["numpy", "matplotlib"],
    "needs_rust": [{"manifest": "Revision/kohn_sham/solver/Cargo.toml",
                    "binaries": ["revision_ks_solver"], "build_minutes": 1}],
    "expected_seconds": 120,
    "timeout_seconds": 900,
    "files_written": ["Revision/textbook/figures/19a.captions.json"]
    + [f"Revision/textbook/figures/{name}.png" for name in FIGURES],
    "final_lines": [
        "PASS every figure file of this notebook exists",
        "ALL 31 CHECKS PASSED (notebook 19a)",
    ],
    "troubleshooting": [
        ["A cell shows the label with the star for a minute or more",
         "this is normal for the cells that run the history and the coupling scan: they "
         "start the Rust program 15 to 20 times, each run takes about a second on a "
         "fast computer and up to five seconds on a laptop. Wait until the label shows "
         "a number."],
        ["RuntimeError: the solver failed for a state",
         "the error message ends with the last lines the solver printed. The solver and "
         "its input files must be the committed versions; get them back and run the "
         "notebook again.",
         ["git checkout -- Revision/kohn_sham Revision/algebra/gammas.json"]],
        ["An AssertionError names a comparison with the record",
         "the line above the error prints the largest difference. Differences in the "
         "last two or three digits are rounding effects of another computer and stay "
         "far below the tolerance; a larger difference means that the solver or its "
         "input files were changed."],
        ["You want the disk space of the solver output back",
         "the folder `Revision/kohn_sham/solver/target/textbook_19a` holds only the raw "
         "output of the last run (ignored by git); delete it at any time, the notebook "
         "writes it again."],
    ],
}

CELLS = [
    md(r"""
    ## 1. What this notebook computes

    Theorem **T3** of the Revision record says: in the Kohn-Sham model of the fermion
    field dirac16complex in the author's deflating primordial field, every
    self-consistent state of the universe with the bare mass $+m$, the coupling
    $\lambda$ and the tip angle $\theta$ has an exact partner in the universe with the
    bare mass $-m$, the **same** coupling $+\lambda$ and the tip angle $\pi - \theta$,
    with the same levels, occupations, energies and energy-momentum profiles and the
    opposite scalar density. T3 is PROVED by exact algebra (Wolfram 10 of 10 checks,
    sympy 13 of 13). This notebook does not prove it again; it **watches it happen**
    in the Rust Kohn-Sham solver of the repository, which knows nothing about T3 and
    simply solves each universe on its own.

    The notebook

    - builds the Rust program `revision_ks_solver` with cargo;
    - solves four kinds of universes: A (mass $+m$, tip angle $0$; the canonical
      state of the record), B (mass $-m$, coupling $+\lambda$, tip angle $\pi$; the T3
      partner of A), C (mass $-m$, coupling $+\lambda$, tip angle $0$; the **negative
      control** with the untransformed tip) and D (mass $-m$, coupling $-\lambda$, tip
      angle $\pi$; the **wrong partner** with the reversed coupling);
    - reproduces, number by number, the solver's own T3 self-test stored in the
      record `Revision/kohn_sham/reports/ks-rust-solver.json`;
    - compares A and B level by level and point by point, for 8, 136 and 688
      particles, at the five instants of the deflating history, for five couplings and
      at three temperatures (59 runs of the solver), and shows that C and D differ;
    - checks that every A run reproduces the committed canonical state of the record;
    - draws ten figures that put the universes on top of each other.

    It takes about one to two minutes (longer on a laptop).
    """),
    md(r"""
    ## 3. The words used in this notebook

    - **Coordinates** (the author's names): $x_1, x_2, x_3$ = ordinary 3-space, which
      inflates (scale factor $e^{a_4}\sin^{1/6}z$); $x_4$ = the time; $x_5, x_6, x_7$ =
      the three **extra times**, which **deflate exponentially** (scale factor
      $e^{-a_4}\sin^{1/6}z$); $x_8$ = the hidden space direction, $z = 6Hx_8$ between
      $0$ and $\pi/2$.
    - **Hidden coordinate** $y = \ln(\sin z)/(6H)$: it runs from the **tip** $y = -L$
      (the model cuts the hidden direction there, $L = 3$) to the **brane** $y = 0$.
    - **Slice** $a_{4,0}$: one instant of the history $a_4 = AHx_4$ ($A = 1$), the value
      of $a_4$ at that instant. The slices are $a_{4,0} = 0, 0.5, 1, 1.5, 2$.
    - **Kohn-Sham state**: an approximate state of $N$ identical fermions built from
      one-particle wave functions (**orbitals**) that each solve a one-particle equation
      in a common **effective potential**; the potential depends on the densities of the
      occupied orbitals, so the equations are solved **self-consistently** (repeat until
      nothing changes).
    - **Level** $\varepsilon$: an allowed energy of the one-particle equation;
      **occupation** $f$: how many particles sit in an orbital of that level ($0$ to
      $1$); **degeneracy** $g$: how many orbitals share the level.
    - **Block type** $j = \pm 1$ and **brane parity** (even or odd): labels of the
      orbitals (explained in section 4).
    - **Bare mass** $m$: the mass in the Lagrangian; **effective mass** $M_{eff}(y)$:
      the mass seen by an orbital, $m$ plus the mean-field term.
    - **Coupling** $\lambda$: the strength of the self-interaction $U = (\lambda/2)S^2$.
      $\lambda_1$ and $\lambda_2$ are the two calibrated couplings of the record.
    - **Densities**: the particle density $n(y)$, the scalar density $S(y)$ and the
      density $Q(y)$; **proper** means per unit of proper 7-volume.
    - **Energy-momentum profiles**: the energy density $\rho(y)$ and the pressures
      $p_3(y)$ (3-space), $p_t(y)$ (extra times), $p_8(y)$ (hidden direction).
    - **Tip angle** $\theta$: the angle of the boundary condition at the tip.
    - **Partner**: the image of a state under the map of theorem T3. **Negative
      control**: a computation that must FAIL to agree; it shows that the agreement is
      not automatic.
    - **Relative difference**: $|a - b|/\max(|a|, 1)$; numbers that agree to the last
      digits of a computer have relative differences near $10^{-15}$.
    - Status labels: PROVED (exact), COMPUTED (numerical), ASSUMED (a choice),
      HYPOTHESIS, OPEN (not known).
    - Units: $H = 1$ and $|m| = 1$; energies, momenta and temperatures in units of
      $|m|$, lengths in units of $1/H$.
    """),
    md(r"""
    ## 4. The physical and mathematical situation

    **The geometry.** In the hidden coordinate $y$ the author's metric is
    $ds^2 = e^{2Hy}[e^{2a_4}(dx_1^2 + dx_2^2 + dx_3^2) - e^{-2a_4}(dx_5^2 + dx_6^2 +
    dx_7^2)] - dx_4^2 + dy^2$. While $a_4$ grows, 3-space inflates by $e^{a_4}$ and the
    three extra times deflate by $e^{-a_4}$; the proper 7-volume factor
    $e^{3a_4} e^{-3a_4} e^{6Hy} = e^{6Hy}$ does not change, because the deflation of the
    extra times exactly compensates the inflation of 3-space. Along the history every
    3-space momentum is redshifted: an orbital with momentum $k$ feels
    $\kappa(y)\,k$ with $\kappa = e^{-Hy - a_{4,0}}$.

    **The Kohn-Sham problem** (record `Revision/kohn_sham/ks-theory.json`). The 16
    components of the field split exactly into eight blocks of two components
    $\chi(y) = (\chi_1, \chi_2)$, labelled by $j = \pm 1$ and two more signs. In a block
    of type $j$ an orbital with 3-momentum $k$ and level $\varepsilon$ solves

    $$h_j\chi = \varepsilon\chi,\qquad h_j = j\Big[-i\sigma_1\frac{d}{dy}
    + M_{eff}(y)\,\sigma_2 + \kappa(y)\,k\,\sigma_3\Big] + v_v(y),$$

    with the Pauli matrices $\sigma_1, \sigma_2, \sigma_3$, the effective mass
    $M_{eff} = m + \frac{15}{16}\lambda S$ and the potential $v_v = -\frac{1}{16}\lambda n$
    (Hartree plus the exact exchange of the uniform gas; no correlation).

    **Boundary conditions.** At the brane $y = 0$ the $Z_2$ mirror, which is ASSUMED:
    even parity $\chi_2(0) = 0$ or odd parity $\chi_1(0) = 0$; both parities are solved
    and filled together. At the tip $y = -L$ a chosen condition
    $(1 - Q(\theta))\chi(-L) = 0$ with $Q(\theta) = \cos\theta\,\sigma_3 +
    \sin\theta\,\sigma_2$: for $\theta = 0$ it says $\chi_2(-L) = 0$, for $\theta = \pi$
    it says $\chi_1(-L) = 0$.

    **Theorem T3** (PROVED; records `Revision/pairing/kohn_sham/t3-theory.json`,
    `wolfram-t3.json`, `python-t3.json`). The map $(\chi, j) \to (\sigma_2\chi, -j)$ at
    the same momentum (in 16 components: the chirality matrix $\Gamma$), with the two
    brane parities exchanged and $\theta \to \pi - \theta$, sends every self-consistent
    Kohn-Sham state with $(m, \lambda, \theta)$ to a self-consistent state with
    $(-m, +\lambda, \pi - \theta)$: equal levels with degeneracies, occupations, chemical
    potential, entropy, Kohn-Sham energy $E_{KS}$, grand potential and free energy,
    equal $n$, $\rho$, $p_3$, $p_t$, $p_8$; opposite $S$, $Q$ and $M_{eff}$. With
    $(-m, -\lambda)$ the map fails, and with the untransformed tip it fails too.

    **The four universes of this notebook** ($m = 1$):

    | name | bare mass | coupling | tip angle | role |
    | --- | --- | --- | --- | --- |
    | A | $+1$ | $+\lambda$ | $0$ | the canonical state of the record |
    | B | $-1$ | $+\lambda$ | $\pi$ | the T3 partner of A |
    | C | $-1$ | $+\lambda$ | $0$ | negative control: tip not transformed |
    | D | $-1$ | $-\lambda$ | $\pi$ | wrong partner: coupling reversed |

    **What is assumed and what is not shown.** The $Z_2$ brane is ASSUMED; the tip is
    a chosen cutoff; the states are instantaneous (adiabatic) mean-field states; the
    history $a_4 = AHx_4$ is a PRESCRIBED BACKGROUND (the Kohn-Sham states are not an
    admissible source of the $a_4$ equations). T3 maps solutions onto solutions; it
    does not create anything: no creation process, rate or amplitude of a pair of
    universes follows from it, and nothing here says that the partner exists. Every
    number in this notebook is COMPUTED by the solver; the agreement of A and B is a
    numerical confirmation of T3, not its proof.
    """),
    md(r"""
    ## 5. Building the solver and a helper that runs it

    The next cell imports the packages, builds the Rust program with cargo (the helper
    `rust_program` of the set-up cell; the first build takes about a minute, later
    builds a second) and defines the colours of the figures: blue for A, orange for B,
    aqua for C and yellow for D, always in this order.
    """),
    code(r'''
    import csv  # reads the tables (CSV files) of the record
    import math  # pi and a few functions of single numbers
    import re  # regular expressions: reads numbers out of the record's text

    import numpy as np  # arrays of numbers

    SOLVER_MANIFEST = "Revision/kohn_sham/solver/Cargo.toml"  # the crate of the solver
    program = rust_program(SOLVER_MANIFEST, "revision_ks_solver")  # build it, get path
    RUN_FOLDER = REPO / "Revision/kohn_sham/solver/target/textbook_19a"  # git ignores it
    RUN_FOLDER.mkdir(parents=True, exist_ok=True)

    COLOUR = {"A": "#2a78d6", "B": "#eb6834", "C": "#1baf7a", "D": "#eda100"}
    NAME = {"A": "A: $+m$, $+\\lambda$, $\\theta = 0$",
            "B": "B: $-m$, $+\\lambda$, $\\theta = \\pi$ (T3 partner)",
            "C": "C: $-m$, $+\\lambda$, $\\theta = 0$ (control)",
            "D": "D: $-m$, $-\\lambda$, $\\theta = \\pi$ (wrong partner)"}
    say("Packages imported, solver ready, colours defined.")
    '''),
    md(r"""
    The next cell defines `solve`, which runs the solver once. The subcommand `single`
    solves one Kohn-Sham state with the options `--m` (bare mass), `--lambda`, `--a4`
    (the slice), `--N` (particle number), `--tip-theta` (tip angle), `--margin` (how
    far above the highest occupied level the solver keeps empty levels; the record
    uses $0.25 + 2\sigma$ with $\sigma = 0$, $0.1$, $0.3$ for $\lambda = 0$,
    $\pm\lambda_1$, $\pm\lambda_2$) and optionally `--T` (temperature). It writes a JSON
    file (levels, energies, integrals) and, with `--profiles`, a table of the profiles
    at the 151 points $y = -3, -2.98, \dots, 0$. `--root` tells it where the
    repository is (it reads `ks-theory.json` and the gamma matrices from there).
    `solve` returns a dictionary with the JSON record, its levels as a list of tuples
    $(n_2, j, \text{parity}, \text{label}, \varepsilon, g, f)$ and the profiles as
    numpy arrays. The four universes are made by `universe`.
    """),
    code(r'''
    TIP = {"A": 0.0, "B": math.pi, "C": 0.0, "D": math.pi}  # tip angle of each kind
    MASS = {"A": 1.0, "B": -1.0, "C": -1.0, "D": -1.0}  # bare mass of each kind
    SIGN = {"A": 1.0, "B": 1.0, "C": 1.0, "D": -1.0}  # D reverses the coupling


    def read_profile(path):
        """A profile table as a dictionary: column name -> numpy array (151 values)."""
        data = np.genfromtxt(path, delimiter=",", names=True)
        return {name: data[name] for name in data.dtype.names}


    def solve(label, m, lam, a4, N, theta, margin, T=None):
        """Run "revision_ks_solver single" for one state and return its results."""
        out = RUN_FOLDER / f"{label}.json"  # the solver's record of this state
        table = RUN_FOLDER / f"{label}.csv"  # its profiles
        command = [str(program), "single", "--root", str(REPO), "--m", repr(m),
                   "--lambda", repr(lam), "--a4", repr(a4), "--N", repr(float(N)),
                   "--tip-theta", repr(theta), "--margin", repr(margin),
                   "--out", str(out), "--profiles", str(table)]
        if T is not None:
            command += ["--T", repr(T)]  # a thermal (Mermin) state
        done = subprocess.run(command, capture_output=True, text=True,
                              encoding="utf-8", errors="replace")
        last = (done.stdout.strip().split("\n") or [""])[-1]  # SUCCESS or FAILURE
        if done.returncode != 0 or last != "SUCCESS":
            raise RuntimeError(f"the solver failed for {label}: {done.stderr[-400:]}")
        state = json.loads(out.read_text(encoding="utf-8"))
        state["levels"] = [tuple(level) for level in
                           state["levels_n2_j_parity_label_eps_deg_f"]]
        state["profile"] = read_profile(table)
        return state


    def universe(kind, lam, a4, N, margin, T=None):
        """Solve universe A, B, C or D with the coupling lam (D uses -lam)."""
        label = f"{kind}_N{N}_lam{lam:+.4g}_a{a4:g}" + ("" if T is None else f"_T{T:g}")
        return solve(label, MASS[kind], SIGN[kind] * lam, a4, N, TIP[kind], margin, T)


    say("solve and universe defined; outputs go to the folder "
        "Revision/kohn_sham/solver/target/textbook_19a")
    '''),
    md(r"""
    ## 6. What the record says: the solver's own T3 self-test

    The solver's check report contains a check named `t3_block_map_solver_selftest`.
    It solved A, B and C at the slice $a_{4,0} = 1$ with the coupling $\lambda_1$ for
    $N = 8$ and $N = 136$ and recorded the energies, the number of levels and the
    largest differences. The next cell reads the couplings of the record
    (`parameters.json`) and this check, and pulls its numbers out of its text with a
    regular expression (a pattern that matches text).
    """),
    code(r'''
    SOLVER_REPORT = "Revision/kohn_sham/reports/ks-rust-solver.json"
    PARAMETERS = "Revision/kohn_sham/results/parameters.json"
    SELFTEST = "t3_block_map_solver_selftest"
    solver_report = json.loads(repository_file(SOLVER_REPORT).read_text(encoding="utf-8"))
    parameters = json.loads(repository_file(PARAMETERS).read_text(encoding="utf-8"))
    LAMBDA = {int(entry["N"]): (entry["lambda1"], entry["lambda2"])
              for entry in parameters["couplingCalibration"]["values"]}
    for N, (l1, l2) in LAMBDA.items():
        say(f"N = {N:3d}: lambda_1 = {l1}, lambda_2 = {l2}")
    selftest = next(c for c in solver_report["checks"] if c["name"] == SELFTEST)
    PATTERN = re.compile(r"N = (\d+), lambda = (\S+), a4,0 = 1: E_KS (\S+) vs (\S+); "
                         r"(\d+) levels; .*?untransformed tip b\(-L\) = 0\): "
                         r"E_KS = (\S+) vs")
    RECORD = {}  # N -> the recorded numbers of the self-test
    for part in selftest["detail"].split(" | "):
        found = PATTERN.search(part)
        RECORD[int(found.group(1))] = {
            "lambda": float(found.group(2)), "E_A": float(found.group(3)),
            "E_B": float(found.group(4)), "levels": int(found.group(5)),
            "E_C": float(found.group(6))}
    for N, entry in RECORD.items():
        say(f"record, N = {N}: E_KS(A) = {entry['E_A']:.12e}, "
            f"E_KS(B) = {entry['E_B']:.12e}, {entry['levels']} levels, "
            f"control E_KS(C) = {entry['E_C']:.10e}")
    check(selftest["verdict"] == "PASS" and sorted(RECORD) == [8, 136]
          and all(RECORD[N]["lambda"] == LAMBDA[N][0] for N in RECORD),
          "the record holds the passing self-test for N = 8 and 136 at lambda_1",
          record=f"{SOLVER_REPORT}, check {SELFTEST}")
    '''),
    md(r"""
    ## 7. Reproducing the self-test: A, B and C for N = 8 and N = 136

    The next cell solves the three universes A, B, C for $N = 8$ and $N = 136$ at the
    slice $a_{4,0} = 1$ with the coupling $\lambda_1$ and the record's margin $0.45$
    (six runs of the solver). Then it compares, as the self-test does: the sorted lists
    of $(\varepsilon, g, f)$ of A and B, the energies $E_{KS}$, the integrals of
    $\rho, p_3, p_t, p_8$ over the hidden direction and the scalar densities
    ($S_A + S_B$ must vanish). It prints each largest difference.
    """),
    code(r'''
    SELF = {}  # (N, kind) -> state
    for N in (8, 136):
        for kind in "ABC":
            SELF[(N, kind)] = universe(kind, LAMBDA[N][0], 1.0, N, 0.45)


    def sorted_levels(state):
        """The levels as a sorted list of (eps, g, f), as the self-test compares them."""
        return sorted((level[4], level[5], level[6]) for level in state["levels"])


    def level_difference(first, second):
        """Largest difference of the sorted (eps, g, f) lists of two states."""
        pairs = zip(sorted_levels(first), sorted_levels(second))
        return max(max(abs(x - y) for x, y in zip(p, q)) for p, q in pairs)


    def integral_difference(first, second):
        """Largest relative difference of the four integrated EMT components."""
        a, b = first["emtIntegrals_2Vol7_int_e6Hy"], second["emtIntegrals_2Vol7_int_e6Hy"]
        return max(abs(a[c] - b[c]) / max(abs(a[c]), 1.0) for c in ("rho", "p3", "p_t",
                                                                    "p8"))


    def scalar_sum(first, second):
        """max|S_A + S_B| / max|S_A| on the 151 profile points."""
        sa, sb = first["profile"]["S"], second["profile"]["S"]
        return float(np.max(np.abs(sa + sb)) / max(np.max(np.abs(sa)), 1e-300))


    for N in (8, 136):
        A, B, C = SELF[(N, "A")], SELF[(N, "B")], SELF[(N, "C")]
        say(f"N = {N}: E_KS(A) = {A['E_KS']:.12e}, E_KS(B) = {B['E_KS']:.12e}, "
            f"{len(A['levels'])} and {len(B['levels'])} levels")
        say(f"    levels (eps, g, f): {level_difference(A, B):.2e}; EMT integrals: "
            f"{integral_difference(A, B):.2e}; |S_A + S_B|/max|S|: "
            f"{scalar_sum(A, B):.2e}; control E_KS(C) = {C['E_KS']:.10e}")
    '''),
    md(r"""
    The next cell turns these numbers into checks. For each $N$: A and B have the
    recorded number of levels; every difference between A and B is below the
    self-test's tolerance $10^{-9}$; the energies agree with the energies printed in
    the record within $10^{-9}$ (relative); the control C has the recorded energy and
    differs from A by more than $1$. The tolerance $10^{-9}$ is the one fixed in the
    record before its comparison; differences of a few $10^{-15}$ are the rounding of
    the computer.
    """),
    code(r'''
    TOL = 1e-9  # the tolerance of the self-test, fixed in the record
    REC = f"{SOLVER_REPORT}, check {SELFTEST}"


    def close(a, b, tol=TOL):
        """True when a and b agree within tol relative to max(|a|, 1)."""
        return abs(a - b) <= tol * max(abs(a), 1.0)


    for N in (8, 136):
        A, B, C = SELF[(N, "A")], SELF[(N, "B")], SELF[(N, "C")]
        rec = RECORD[N]
        check(len(A["levels"]) == len(B["levels"]) == rec["levels"]
              and level_difference(A, B) < TOL and integral_difference(A, B) < TOL
              and scalar_sum(A, B) < TOL and close(A["E_KS"], B["E_KS"]),
              f"N = {N}: A and B have equal levels, energies, EMT integrals, S_B = -S_A",
              record=REC)
        check(close(A["E_KS"], rec["E_A"]) and close(B["E_KS"], rec["E_B"])
              and close(C["E_KS"], rec["E_C"]) and abs(C["E_KS"] - A["E_KS"]) > 1.0,
              f"N = {N}: the energies of A, B and the control C are those of the record",
              record=REC)
    '''),
    md(r"""
    ## 8. A is the canonical state of the record

    Universe A at $N = 136$, $\lambda_1$, $a_{4,0} = 1$ is the state `N136_lamp1_a10` of
    the committed canonical matrix. The next cell reads its row of
    `ground/summary.csv`, its row of `ground/emt-integrals.csv` and its profile file,
    and compares them with the new run: the energy, the highest occupied level (HOMO),
    the lowest empty level (LUMO), the Kohn-Sham gap, the four EMT integrals, and every
    column of the profile at every point (relative to the column's largest value). It
    also prints whether the new profile file is identical byte for byte to the
    committed one (on the computer that built this book it is; on another computer the
    last digit of a few numbers may differ).
    """),
    code(r'''
    GROUND = "Revision/kohn_sham/results/ground"


    def read_rows(relative):
        """A CSV file of the record as {id: row}."""
        with repository_file(relative).open(encoding="utf-8", newline="") as handle:
            return {row["id"]: row for row in csv.DictReader(handle)}


    summary = read_rows(f"{GROUND}/summary.csv")
    integrals = read_rows(f"{GROUND}/emt-integrals.csv")
    A = SELF[(136, "A")]
    occupied = [lv[4] for lv in A["levels"] if lv[6] > 0.5]  # levels with f = 1
    empty = [lv[4] for lv in A["levels"] if lv[6] < 0.5]  # levels with f = 0
    new = {"E_KS": A["E_KS"], "HOMO": max(occupied), "LUMO": min(empty),
           "KS_gap": min(empty) - max(occupied)}
    row = summary["N136_lamp1_a10"]
    worst_scalar = max(abs(new[key] - float(row[key])) for key in new)
    emt_row = integrals["N136_lamp1_a10"]
    worst_integral = max(abs(A["emtIntegrals_2Vol7_int_e6Hy"][c] - float(emt_row[f"int_{c}"]))
                         / max(abs(float(emt_row[f"int_{c}"])), 1.0)
                         for c in ("rho", "p3", "p_t", "p8", "n"))
    committed = read_profile(repository_file(f"{GROUND}/profiles/N136_lamp1_a10.csv"))
    worst_profile = max(float(np.max(np.abs(A["profile"][c] - committed[c]))
                              / max(np.max(np.abs(committed[c])), 1e-300))
                        for c in committed)
    for key in new:
        say(f"{key:7}: new {new[key]: .15e}   record {float(row[key]): .15e}")
    say(f"largest differences: scalars {worst_scalar:.1e}, integrals "
        f"{worst_integral:.1e}, profile columns {worst_profile:.1e}")
    same_bytes = ((RUN_FOLDER / "A_N136_lam+0.0009298_a1.csv").read_bytes()
                  == repository_file(f"{GROUND}/profiles/N136_lamp1_a10.csv").read_bytes())
    report("new profile file byte-identical to the record", same_bytes)
    check(worst_scalar < TOL and worst_integral < TOL and worst_profile < TOL,
          "A reproduces the canonical state N136_lamp1_a10 of the record",
          record=f"{GROUND}/summary.csv, emt-integrals.csv and profiles, N136_lamp1_a10")
    '''),
    md(r"""
    ## 9. The two spectra, level by level

    T3 does more than say that the sorted lists agree: it says WHICH level goes where.
    The orbital of block type $j$ and brane parity $p$ goes to block type $-j$ and the
    other parity, at the same momentum shell $n_2$ (the momentum $k = \Delta k
    \sqrt{n_2}$) and with the same level. The next cell checks this for $N = 136$: for
    every level of A it looks for a level of B in the shell $n_2$, with $-j$ and the
    other parity, at the same $\varepsilon$ (within $10^{-9}$), and checks that the
    pairing uses every level of B exactly once. It also prints how the solver's labels
    (the Pruefer numbers that count the levels inside a sector) are shifted by the map.
    """),
    code(r'''
    OTHER = {"even": "odd", "odd": "even"}  # the brane parity is exchanged


    def level_map(first, second, tol=TOL):
        """Pair every level (n2, j, p, l, eps, g, f) of first with a level of second in
        (n2, -j, other p) at the same eps; return the pairs (None if one is missing)."""
        unused = list(second["levels"])
        pairs = []
        for lv in sorted(first["levels"]):
            match = [w for w in unused if w[0] == lv[0] and w[1] == -lv[1]
                     and w[2] == OTHER[lv[2]] and abs(w[4] - lv[4]) <= tol]
            if not match:
                return None
            best = min(match, key=lambda w: abs(w[4] - lv[4]))
            unused.remove(best)
            pairs.append((lv, best))
        return pairs


    pairs136 = level_map(SELF[(136, "A")], SELF[(136, "B")])
    shifts = {}
    for lv, w in pairs136:
        key = f"j = {lv[1]:+d}, {lv[2]:4}"
        shifts.setdefault(key, set()).add(w[3] - lv[3])  # label of B minus label of A
    for key in sorted(shifts):
        say(f"A levels with {key}: partner in j = opposite, other parity; label shift "
            f"{sorted(shifts[key])}")
    worst = max(abs(lv[4] - w[4]) for lv, w in pairs136)
    report("largest |eps_A - eps_B| of the paired levels, N = 136", f"{worst:.2e}")
    check(pairs136 is not None and len(pairs136) == len(SELF[(136, "B")]["levels"])
          and all(lv[5] == w[5] and lv[6] == w[6] for lv, w in pairs136),
          "every level of A has its partner in B with -j and the other brane parity",
          record="Revision/pairing/kohn_sham/t3-theory.json, statement S1")
    check(level_map(SELF[(136, "A")], SELF[(136, "C")]) is None,
          "the control C has no such partner levels (the pairing fails)")
    '''),
    md(r"""
    The next cell draws the three spectra side by side for $N = 136$ (a **level
    ladder**): every level is a short horizontal line, coloured when it is occupied
    ($f = 1$) and grey when it is empty; the dashed line is the Fermi level (the
    highest occupied level). Only the levels below $1.3$ are drawn. A and B look the
    same, C does not.
    """),
    code(r'''
    fig, ax = plt.subplots(figsize=(7.0, 4.6))
    for x, kind in enumerate("ABC"):
        state = SELF[(136, kind)]
        for lv in state["levels"]:
            if lv[4] > 1.3:
                continue  # only the lower part of the spectrum
            full = lv[6] > 0.5  # occupied?
            ax.plot([x - 0.32, x + 0.32], [lv[4], lv[4]],
                    color=COLOUR[kind] if full else "0.7", lw=2.0 if full else 1.0)
        ax.plot([x - 0.42, x + 0.42], [state["mu_or_fermi_level"]] * 2, color="0.2",
                ls="--", lw=1.0)
    ax.set_xticks([0, 1, 2])
    ax.set_xticklabels(["A: $+m$, $\\theta = 0$", "B: $-m$, $\\theta = \\pi$",
                        "C: $-m$, $\\theta = 0$ (control)"])
    ax.set_xlim(-0.6, 2.6)
    ax.set_ylabel("Kohn-Sham level $\\varepsilon$ (units of $|m|$)")
    ax.set_title("$N = 136$, $\\lambda = \\lambda_1$, slice $a_{4,0} = 1$")
    ax.grid(axis="x", visible=False)
    save_figure(fig, "level_ladder",
                "Level ladders of the three universes A (bare mass $+m$, tip angle 0), B "
                "(bare mass $-m$, the same coupling, tip angle $\\pi$: the T3 partner) "
                "and C (bare mass $-m$, tip angle 0: the control) for $N = 136$ "
                "particles, $\\lambda = \\lambda_1$, slice $a_{4,0} = 1$, all solved "
                "independently by the Rust solver. Each short line is one Kohn-Sham "
                "level (vertical axis, units of $|m|$), coloured when occupied and grey "
                "when empty; the dashed line is the Fermi level. A and B are the same "
                "ladder; C, with the untransformed tip, is a different one.")
    '''),
    md(r"""
    The next cell draws the level-by-level differences on a logarithmic axis: for the
    $i$-th level of the sorted lists, $|\varepsilon_{A,i} - \varepsilon_{B,i}|$ (A
    against its partner) and $|\varepsilon_{A,i} - \varepsilon_{C,i}|$ (A against the
    control). A difference that is exactly zero cannot be drawn on a logarithmic axis;
    it is drawn at $10^{-17}$.
    """),
    code(r'''
    FLOOR = 1e-17  # where exact zeros are drawn on the logarithmic axis
    eps = {kind: np.array([e for e, g, f in sorted_levels(SELF[(136, kind)])])
           for kind in "ABC"}
    index = np.arange(1, len(eps["A"]) + 1)
    fig, ax = plt.subplots()
    ax.semilogy(index, np.maximum(np.abs(eps["A"] - eps["B"]), FLOOR), "o",
                color=COLOUR["B"], ms=4, label="A against B (T3 partner)")
    ax.semilogy(index, np.maximum(np.abs(eps["A"] - eps["C"]), FLOOR), "^",
                color=COLOUR["C"], ms=4, label="A against C (control)")
    ax.axhline(TOL, color="0.3", ls="--", lw=1.0, label="tolerance $10^{-9}$")
    ax.set_xlabel("level number $i$ (levels sorted by energy)")
    ax.set_ylabel("$|\\varepsilon_{A,i} - \\varepsilon_{X,i}|$ (units of $|m|$)")
    ax.set_title("$N = 136$, $\\lambda = \\lambda_1$, $a_{4,0} = 1$: 160 levels")
    ax.legend(fontsize=8, loc="center right")
    save_figure(fig, "level_differences",
                "Level-by-level differences between universe A and its T3 partner B "
                "(orange circles) and between A and the control C (aqua triangles), "
                "for $N = 136$, $\\lambda = \\lambda_1$, $a_{4,0} = 1$; horizontal axis "
                "the number of the level in the sorted list, vertical axis the absolute "
                "difference in units of $|m|$ (logarithmic; exact zeros drawn at "
                "$10^{-17}$). The partner agrees to about $10^{-13}$, the rounding of "
                "the computer, far below the tolerance $10^{-9}$ (dashed); the control "
                "differs by $10^{-4}$ to $1$.")
    max_partner = float(np.max(np.abs(eps["A"] - eps["B"])))
    max_control = float(np.max(np.abs(eps["A"] - eps["C"])))
    report("largest level difference A - B", f"{max_partner:.2e}")
    report("largest level difference A - C", f"{max_control:.3g}")
    '''),
    md(r"""
    ## 10. The densities and the potentials, point by point

    T3 says that the particle density $n(y)$ and the potential $v_v(y)$ of B are those
    of A, while the scalar density $S(y)$, the density $Q(y)$ and the effective mass
    $M_{eff}(y)$ change sign. The next cell checks this at the 151 points of the
    profiles for $N = 8$ and $N = 136$ (relative to the largest value of each column)
    and also checks the interaction energy density $e_{int}$, which contains $S$ only as
    $S^2$.
    """),
    code(r'''
    EVEN = ("n", "v_v", "e_int", "rho", "p3", "p_t", "p8")  # unchanged by the map
    ODD = ("S", "Q", "M_eff")  # change sign under the map


    def profile_mismatch(first, second):
        """Largest relative mismatch of the T3 rule (even columns equal, odd opposite)."""
        worst = 0.0
        for column in EVEN + ODD:
            sign = -1.0 if column in ODD else 1.0
            a, b = first["profile"][column], second["profile"][column]
            scale = max(float(np.max(np.abs(a))), 1e-300)
            worst = max(worst, float(np.max(np.abs(b - sign * a))) / scale)
        return worst


    for N in (8, 136):
        mismatch = profile_mismatch(SELF[(N, "A")], SELF[(N, "B")])
        control = profile_mismatch(SELF[(N, "A")], SELF[(N, "C")])
        say(f"N = {N}: T3 rule for B: {mismatch:.2e}; the same rule for C: {control:.3g}")
        check(mismatch < TOL and control > 0.1,
              f"N = {N}: n, v_v, e_int, rho, p3, p_t, p8 equal; S, Q, M_eff opposite",
              record="Revision/pairing/kohn_sham/t3-theory.json, statements S3 and S4")
    '''),
    md(r"""
    The next cell draws the densities for $N = 136$. Left: the proper particle density
    $n(y)$ (logarithmic axis) of A, B and C; A and B lie on top of each other (B is
    dashed). Right: the scalar density $S(y)$; B is the mirror image of A, $S_B = -S_A$.
    """),
    code(r'''
    y = SELF[(136, "A")]["profile"]["y"]  # the 151 points from the tip to the brane
    fig, (left, right) = plt.subplots(1, 2, figsize=(9.0, 3.8))
    STYLE = {"A": dict(lw=2.6), "B": dict(lw=1.6, ls="--"), "C": dict(lw=1.4, ls=":")}
    for kind in "ABC":
        prof = SELF[(136, kind)]["profile"]
        left.semilogy(y, prof["n"], color=COLOUR[kind], label=NAME[kind], **STYLE[kind])
        right.plot(y, prof["S"], color=COLOUR[kind], label=NAME[kind], **STYLE[kind])
    left.set_xlabel("hidden coordinate $y$ (tip $-3$, brane $0$)")
    left.set_ylabel("proper particle density $n(y)$")
    left.legend(fontsize=7, loc="upper right")
    right.set_xlabel("hidden coordinate $y$")
    right.set_ylabel("proper scalar density $S(y)$")
    right.axhline(0.0, color="0.3", lw=0.8)
    fig.suptitle("$N = 136$, $\\lambda = \\lambda_1$, $a_{4,0} = 1$", fontsize=10)
    fig.tight_layout()
    save_figure(fig, "density_profiles",
                "Left: the proper particle density $n(y)$ of the universes A (blue), B "
                "(orange, dashed) and C (aqua, dotted) for $N = 136$, "
                "$\\lambda = \\lambda_1$, $a_{4,0} = 1$, against the hidden coordinate $y$ "
                "from the tip $y = -3$ to the brane $y = 0$ (logarithmic vertical axis, "
                "units $|m|^7$). Right: the proper scalar density $S(y)$. The density of "
                "B is that of A, and its scalar density is the mirror image "
                "$S_B = -S_A$, as T3 states; the control C has its own densities.")
    '''),
    md(r"""
    The next cell draws the effective mass $M_{eff}(y) = \pm m + \frac{15}{16}\lambda S$
    (left) and the potential $v_v(y) = -\frac{1}{16}\lambda n$ (right) of A, B and C.
    For B the mass is $-M_{eff}$ of A at every point; the potential is the same.
    """),
    code(r'''
    fig, (left, right) = plt.subplots(1, 2, figsize=(9.0, 3.8))
    for kind in "ABC":
        prof = SELF[(136, kind)]["profile"]
        left.plot(y, prof["M_eff"], color=COLOUR[kind], label=NAME[kind], **STYLE[kind])
        right.plot(y, prof["v_v"], color=COLOUR[kind], label=NAME[kind], **STYLE[kind])
    left.set_xlabel("hidden coordinate $y$")
    left.set_ylabel("effective mass $M_{eff}(y)$ (units of $|m|$)")
    left.legend(fontsize=7, loc="center right")
    right.set_xlabel("hidden coordinate $y$")
    right.set_ylabel("potential $v_v(y)$ (units of $|m|$)")
    fig.suptitle("$N = 136$, $\\lambda = \\lambda_1$, $a_{4,0} = 1$", fontsize=10)
    fig.tight_layout()
    save_figure(fig, "mass_and_potential",
                "Left: the self-consistent effective mass $M_{eff}(y)$ of A (blue), B "
                "(orange, dashed) and C (aqua, dotted) for $N = 136$, "
                "$\\lambda = \\lambda_1$, $a_{4,0} = 1$ (units of $|m|$). Right: the "
                "self-consistent potential $v_v(y)$ (units of $|m|$). B has exactly the "
                "opposite mass of A at every point and the same potential: this is why "
                "the bare mass must change sign while the coupling keeps its sign. The "
                "control C has the mass $-m$ but its own, different mean field.")
    '''),
    md(r"""
    ## 11. The energy-momentum profiles

    The energy density and the three pressures are the source terms that the gravity
    equations would need. The next cell draws $\rho$, $p_3$, $p_t$ and $p_8$ for
    $N = 136$, each multiplied by the volume factor $e^{6Hy}$ (so the area under each
    curve is proportional to the integral over the hidden direction). The cell also
    checks the identity $p_8' + 6Hp_8 = 3H(p_3 + p_t)$ (the conservation law along
    $y$), which the solver measures for every state, for B.
    """),
    code(r'''
    weight = np.exp(6.0 * y)  # the proper-volume factor e^{6 H y}, H = 1
    fig, axes = plt.subplots(2, 2, figsize=(9.0, 6.0), sharex=True)
    for ax, column, title in zip(axes.flat, ("rho", "p3", "p_t", "p8"),
                                 ("energy density $\\rho$", "pressure $p_3$ (3-space)",
                                  "pressure $p_t$ (extra times)",
                                  "pressure $p_8$ (hidden direction)")):
        for kind in "ABC":
            prof = SELF[(136, kind)]["profile"]
            ax.plot(y, weight * prof[column], color=COLOUR[kind], label=NAME[kind],
                    **STYLE[kind])
        ax.set_title(title, fontsize=9)
        ax.set_ylabel("$e^{6Hy}$ times the component")
    for ax in axes[1]:
        ax.set_xlabel("hidden coordinate $y$")
    axes[0, 0].legend(fontsize=7, loc="upper left")
    fig.tight_layout()
    save_figure(fig, "emt_profiles",
                "The energy-momentum profiles of A (blue), B (orange, dashed) and C "
                "(aqua, dotted) for $N = 136$, $\\lambda = \\lambda_1$, $a_{4,0} = 1$: "
                "energy density $\\rho$, pressures $p_3$ (3-space), $p_t$ (the "
                "deflating extra times) and $p_8$ (hidden direction), each times the "
                "volume factor $e^{6Hy}$, against the hidden coordinate $y$ (units "
                "$|m|^8$ with $H = 1$). The four profiles of the partner B coincide "
                "with those of A at every point (T3, statement S4); the control C "
                "differs.")
    for N in (8, 136):
        B = SELF[(N, "B")]
        say(f"N = {N}, B: y-conservation, integrated {B['yConservationIntegratedRel']:.1e},"
            f" pointwise {B['yConservationPointwiseRel']:.1e} (relative)")
        check(B["yConservationIntegratedRel"] < 1e-8 and B["yConservationPointwiseRel"] < 1e-6,
              f"N = {N}: the partner B obeys p8' + 6H p8 = 3H (p3 + p_t)",
              record=f"{SOLVER_REPORT}, checks emt_y_conservation_integrated, pointwise")
    '''),
    md(r"""
    ## 12. N = 8: where the zero modes live

    For $N = 8$ the particles sit in the eight zero modes of momentum $k = 0$. For A the
    zero mode is $\chi = (e^{my}, 0)$, largest at the brane. Its T3 image is
    $\sigma_2\chi = (0, i e^{my})$, again largest at the brane, and with the tip angle
    $\pi$ it is allowed in B. In the control C (mass $-m$, tip angle $0$) the zero mode
    is $(e^{-my}, 0)$: it lives at the TIP, where the proper volume is tiny and the
    proper density huge (factor $e^{6HL}$). The next cell draws $n(y)$ of the three
    $N = 8$ universes and checks where each density is largest.
    """),
    code(r'''
    fig, ax = plt.subplots()
    for kind in "ABC":
        prof = SELF[(8, kind)]["profile"]
        ax.semilogy(y, weight * prof["n"], color=COLOUR[kind], label=NAME[kind],
                    **STYLE[kind])
    ax.set_xlabel("hidden coordinate $y$ (tip $-3$, brane $0$)")
    ax.set_ylabel("coordinate particle density $e^{6Hy}\\,n(y)$")
    ax.set_title("$N = 8$ (the zero modes), $\\lambda = \\lambda_1$, $a_{4,0} = 1$")
    ax.legend(fontsize=8, loc="center right")
    save_figure(fig, "zero_modes_n8",
                "The coordinate particle density $e^{6Hy}n(y)$ (the density per unit of "
                "$y$; logarithmic vertical axis) of the $N = 8$ universes A (blue), B "
                "(orange, dashed) and C (aqua, dotted) at $\\lambda = \\lambda_1$, "
                "$a_{4,0} = 1$, against the hidden coordinate $y$. A and B hold their "
                "particles in the zero modes at the brane $y = 0$; with the "
                "untransformed tip (C) the zero modes move to the tip $y = -3$. This is "
                "why the control has a completely different energy.")
    ratio = {kind: float(SELF[(8, kind)]["profile"]["n"][-1] * weight[-1]
                         / (SELF[(8, kind)]["profile"]["n"][0] * weight[0]))
             for kind in "ABC"}
    for kind in "ABC":
        say(f"{kind}: coordinate density at the brane / at the tip = {ratio[kind]:.3e}")
    check(ratio["A"] > 1e4 and ratio["B"] > 1e4 and ratio["C"] < 1e-4,
          "N = 8: A and B live at the brane, the control C at the tip")
    '''),
    md(r"""
    ## 13. T3 along the deflating history

    T3 holds at every slice of the history, because the slice $a_{4,0}$ enters only
    through $\kappa = e^{-Hy - a_{4,0}}$, which the map does not touch. The next cell
    solves A, B and C at the five slices $a_{4,0} = 0, 0.5, 1, 1.5, 2$ for $N = 136$
    and $N = 688$, each with its coupling $\lambda_1$ (27 new runs; the slice
    $a_{4,0} = 1$ of $N = 136$ was solved above), and checks at every slice: A
    reproduces the energy of the record, B has the energy of A, C does not.
    """),
    code(r'''
    SLICES = [0.0, 0.5, 1.0, 1.5, 2.0]
    HIST = {}  # (N, kind, a4) -> state
    for N in (136, 688):
        for a4 in SLICES:
            for kind in "ABC":
                if N == 136 and a4 == 1.0:
                    HIST[(N, kind, a4)] = SELF[(N, kind)]  # already solved
                else:
                    HIST[(N, kind, a4)] = universe(kind, LAMBDA[N][0], a4, N, 0.45)
    ok_record, ok_partner, ok_control = True, True, True
    for N in (136, 688):
        for a4 in SLICES:
            A, B, C = (HIST[(N, kind, a4)] for kind in "ABC")
            record_energy = float(summary[f"N{N}_lamp1_a{round(10 * a4):02d}"]["E_KS"])
            ok_record &= close(A["E_KS"], record_energy)
            ok_partner &= (close(A["E_KS"], B["E_KS"]) and level_difference(A, B) < TOL
                           and profile_mismatch(A, B) < TOL)
            ok_control &= abs(A["E_KS"] - C["E_KS"]) > 0.1
            say(f"N = {N:3d}, a4,0 = {a4:3.1f}: E_KS A {A['E_KS']:.10f}, "
                f"B {B['E_KS']:.10f}, C {C['E_KS']:.6f}")
    check(ok_record, "A reproduces the recorded E_KS at all 10 states of the history",
          record=f"{GROUND}/summary.csv, N136_lamp1_a00 to a20, N688_lamp1_a00 to a20")
    check(ok_partner, "B has the levels, energy and profiles of A at every slice")
    check(ok_control, "the control C differs from A at every slice")
    '''),
    md(r"""
    The next cell draws the Kohn-Sham energy along the history. As the extra times
    deflate and 3-space inflates, every 3-momentum is redshifted and the energy of the
    gas falls; A and B fall together, the control C on its own curve.
    """),
    code(r'''
    fig, axes = plt.subplots(1, 2, figsize=(9.0, 3.8))
    MARK = {"A": dict(marker="o", ms=7, lw=2.2), "B": dict(marker="s", ms=4, lw=1.4,
                                                           ls="--"),
            "C": dict(marker="^", ms=6, lw=1.2, ls=":")}
    for ax, N in zip(axes, (136, 688)):
        for kind in "ABC":
            ax.plot(SLICES, [HIST[(N, kind, a4)]["E_KS"] for a4 in SLICES],
                    color=COLOUR[kind], label=NAME[kind], **MARK[kind])
        ax.set_xlabel("slice $a_{4,0}$ of the history $a_4 = Hx_4$")
        ax.set_ylabel("Kohn-Sham energy $E_{KS}$ (units of $|m|$)")
        ax.set_title(f"$N = {N}$, $\\lambda = \\lambda_1$", fontsize=10)
    axes[0].legend(fontsize=7, loc="upper right")
    fig.tight_layout()
    save_figure(fig, "history_energy",
                "The Kohn-Sham energy $E_{KS}$ (units of $|m|$) of A (blue circles), B "
                "(orange squares, dashed) and C (aqua triangles, dotted) at the five "
                "slices $a_{4,0} = 0$ to $2$ of the deflating history, for $N = 136$ "
                "(left) and $N = 688$ (right) at the coupling $\\lambda_1$ of each $N$. "
                "The energy falls because the 3-momenta are redshifted as 3-space "
                "inflates and the extra times deflate; the T3 partner B follows A at "
                "every slice, the control C does not.")
    '''),
    md(r"""
    The next cell draws the same comparison as relative differences on a logarithmic
    axis: $|E_A - E_B|/|E_A|$ (partner) and $|E_A - E_C|/|E_A|$ (control) at every
    slice, for both particle numbers.
    """),
    code(r'''
    fig, ax = plt.subplots()
    for N, marker in ((136, "o"), (688, "s")):
        for kind in "BC":
            values = [max(abs(HIST[(N, "A", a4)]["E_KS"] - HIST[(N, kind, a4)]["E_KS"])
                          / abs(HIST[(N, "A", a4)]["E_KS"]), FLOOR) for a4 in SLICES]
            ax.semilogy(SLICES, values, marker=marker, color=COLOUR[kind],
                        ls="--" if kind == "B" else ":",
                        label=f"$N = {N}$, A against {kind}")
    ax.axhline(TOL, color="0.3", lw=1.0, label="tolerance $10^{-9}$")
    ax.set_xlabel("slice $a_{4,0}$ of the history")
    ax.set_ylabel("relative difference of $E_{KS}$")
    ax.legend(fontsize=7, loc="center right")
    save_figure(fig, "history_agreement",
                "Relative differences of the Kohn-Sham energy between A and its T3 "
                "partner B (orange) and between A and the control C (aqua) at the five "
                "slices of the history, for $N = 136$ (circles) and $N = 688$ (squares); "
                "logarithmic vertical axis, exact zeros drawn at $10^{-17}$. The "
                "partner agrees to $10^{-15}$ or better at every slice: T3 holds slice "
                "by slice along the deflating history. The control is off by $2$ to "
                "$10$ percent.")
    '''),
    md(r"""
    ## 14. The coupling must keep its sign

    T3 pairs $(m, \lambda)$ with $(-m, +\lambda)$. What about $(-m, -\lambda)$, the
    parameter change of the classical theorem T1? The next cell solves, for $N = 136$ at
    $a_{4,0} = 1$, the five couplings $\lambda = -\lambda_2, -\lambda_1, 0, +\lambda_1,
    +\lambda_2$ for all four universes A, B, C, D (with the record's margins $0.85$,
    $0.45$, $0.25$). It checks: A reproduces the record at every coupling; B equals A;
    D at $\lambda$ equals A at $-\lambda$ (that is T3 applied to the state with
    $-\lambda$), so D differs from A whenever $\lambda \ne 0$; C differs from A.
    """),
    code(r'''
    l1, l2 = LAMBDA[136]
    COUPLINGS = [("lamm2", -l2, 0.85), ("lamm1", -l1, 0.45), ("lam0", 0.0, 0.25),
                 ("lamp1", l1, 0.45), ("lamp2", l2, 0.85)]  # tag, lambda, margin
    SCAN = {}  # (tag, kind) -> state
    for tag, lam, margin in COUPLINGS:
        for kind in "ABCD":
            if tag == "lamp1" and kind in "ABC":
                SCAN[(tag, kind)] = SELF[(136, kind)]  # already solved
            else:
                SCAN[(tag, kind)] = universe(kind, lam, 1.0, 136, margin)
    MIRROR = {"lamm2": "lamp2", "lamm1": "lamp1", "lam0": "lam0", "lamp1": "lamm1",
              "lamp2": "lamm2"}  # the tag of -lambda
    ok_record, ok_partner, ok_mirror, ok_wrong = True, True, True, True
    for tag, lam, margin in COUPLINGS:
        E = {kind: SCAN[(tag, kind)]["E_KS"] for kind in "ABCD"}
        ok_record &= close(E["A"], float(summary[f"N136_{tag}_a10"]["E_KS"]))
        ok_partner &= close(E["A"], E["B"]) and level_difference(
            SCAN[(tag, "A")], SCAN[(tag, "B")]) < TOL
        ok_mirror &= close(E["D"], SCAN[(MIRROR[tag], "A")]["E_KS"])
        ok_wrong &= (lam == 0.0) or abs(E["D"] - E["A"]) > 1e-4
        say(f"lambda = {lam:+.4e}: A {E['A']:.10f}  B {E['B']:.10f}  "
            f"C {E['C']:.6f}  D {E['D']:.10f}")
    check(ok_record, "A reproduces the recorded E_KS for all five couplings",
          record=f"{GROUND}/summary.csv, N136_lamm2_a10 to N136_lamp2_a10")
    check(ok_partner, "B = A for every coupling: the partner keeps +lambda")
    check(ok_mirror and ok_wrong,
          "D(lambda) = A(-lambda), so (-m, -lambda) is not the partner for lambda != 0",
          record="Revision/pairing/kohn_sham/reports/python-t3.json, check "
                 "T3.mean_field_map (control)")
    '''),
    md(r"""
    The next cell draws the energies of the scan. Left: $E_{KS} - E_{KS}(\lambda = 0)$
    of A, B and D against $\lambda/\lambda_1$; D is the mirror image of A. Right: the
    energies of A and the control C, which lies far below.
    """),
    code(r'''
    x = [lam / l1 for tag, lam, margin in COUPLINGS]
    E0 = SCAN[("lam0", "A")]["E_KS"]
    fig, (left, right) = plt.subplots(1, 2, figsize=(9.0, 3.8))
    for kind in "ABD":
        left.plot(x, [SCAN[(tag, kind)]["E_KS"] - E0 for tag, lam, margin in COUPLINGS],
                  color=COLOUR[kind], label=NAME[kind],
                  **(MARK[kind] if kind in MARK else dict(marker="D", ms=5, lw=1.4)))
    left.set_xlabel("coupling $\\lambda/\\lambda_1$")
    left.set_ylabel("$E_{KS} - E_{KS}(\\lambda = 0)$ (units of $|m|$)")
    left.axhline(0.0, color="0.3", lw=0.8)
    left.legend(fontsize=7, loc="upper left")
    for kind in "AC":
        right.plot(x, [SCAN[(tag, kind)]["E_KS"] for tag, lam, margin in COUPLINGS],
                   color=COLOUR[kind], label=NAME[kind], **MARK[kind])
    right.set_xlabel("coupling $\\lambda/\\lambda_1$")
    right.set_ylabel("$E_{KS}$ (units of $|m|$)")
    right.legend(fontsize=7, loc="center right")
    fig.suptitle("$N = 136$, slice $a_{4,0} = 1$", fontsize=10)
    fig.tight_layout()
    save_figure(fig, "coupling_scan",
                "Left: the interaction part of the Kohn-Sham energy, $E_{KS}$ minus its "
                "value at $\\lambda = 0$ (units of $|m|$), against the coupling "
                "$\\lambda/\\lambda_1$ for $N = 136$, $a_{4,0} = 1$: universe A (blue), "
                "its T3 partner B with the same coupling (orange, dashed, on top of A) "
                "and D with the reversed coupling (yellow diamonds), which is the "
                "mirror image of A. Right: $E_{KS}$ of A and of the control C (aqua), "
                "about $3$ lower at every coupling. Only $(-m, +\\lambda)$ with the "
                "transformed tip is the partner of $(m, \\lambda)$.")
    '''),
    md(r"""
    ## 15. Thermal states: equal occupations, chemical potential and free energy

    At a temperature $T > 0$ the occupations are the Fermi (Mermin) occupations
    $f = 1/(1 + e^{(\varepsilon - \mu)/T})$, with the chemical potential $\mu$ fixed by
    the particle number. Since the levels of B are those of A, so are $f$, $\mu$, the
    entropy and the free energy $F = E - T S_{ent}$. The next cell solves A, B, C for
    $N = 136$, $\lambda_1$, $a_{4,0} = 1$ at the three temperatures of the record
    $T = 0.01, 0.02, 0.05$ (margin $0.4$, as the record's thermal states), checks that A
    reproduces the record's $\mu$, $E$, entropy and $F$, that B equals A and that C does
    not.
    """),
    code(r'''
    THERMO = read_rows("Revision/kohn_sham/results/thermo/thermodynamics.csv")
    TEMPS = [0.01, 0.02, 0.05]
    WARM = {}  # (T, kind) -> state
    ok_record, ok_partner, ok_control = True, True, True
    for T in TEMPS:
        for kind in "ABC":
            WARM[(T, kind)] = universe(kind, l1, 1.0, 136, 0.4, T=T)
        A, B, C = (WARM[(T, kind)] for kind in "ABC")
        F = {kind: WARM[(T, kind)]["E_KS"] - T * WARM[(T, kind)]["entropy"]
             for kind in "ABC"}  # free energy F = E - T S
        row = THERMO[f"N136_lamp1_a10_T{round(1000 * T)}"]
        ok_record &= (close(A["mu_or_fermi_level"], float(row["mu"]))
                      and close(A["E_KS"], float(row["E"]))
                      and close(A["entropy"], float(row["entropy"]))
                      and close(F["A"], float(row["F"])))
        ok_partner &= (close(A["mu_or_fermi_level"], B["mu_or_fermi_level"])
                       and close(A["entropy"], B["entropy"]) and close(F["A"], F["B"])
                       and level_difference(A, B) < TOL)
        ok_control &= abs(F["A"] - F["C"]) > 0.1
        say(f"T = {T:.2f}: mu A {A['mu_or_fermi_level']:.12f} B "
            f"{B['mu_or_fermi_level']:.12f} C {C['mu_or_fermi_level']:.6f}; "
            f"F A {F['A']:.9f} B {F['B']:.9f} C {F['C']:.5f}")
    check(ok_record, "A reproduces mu, E, entropy and F of the three thermal states",
          record="Revision/kohn_sham/results/thermo/thermodynamics.csv, "
                 "N136_lamp1_a10_T10, T20, T50")
    check(ok_partner, "B has the occupations, mu, entropy and F of A at every T",
          record="Revision/pairing/kohn_sham/t3-theory.json, statement S4")
    check(ok_control, "the control C has a different free energy at every T")
    '''),
    md(r"""
    The next cell draws, for $T = 0.05$, the occupation $f$ of every level of A, B and
    C against its energy (left; the curve is the Fermi function of A), and the free
    energy $F$ against the temperature (right).
    """),
    code(r'''
    fig, (left, right) = plt.subplots(1, 2, figsize=(9.0, 3.8))
    T = 0.05
    DOTS = {"A": dict(marker="o", ms=7, ls="none", mfc="none", mew=1.6),
            "B": dict(marker="x", ms=5, ls="none", mew=1.4),
            "C": dict(marker="^", ms=4, ls="none")}
    for kind in "ABC":
        lv = WARM[(T, kind)]["levels"]
        left.plot([v[4] for v in lv], [v[6] for v in lv], color=COLOUR[kind],
                  label=NAME[kind], **DOTS[kind])
    mu = WARM[(T, "A")]["mu_or_fermi_level"]
    grid = np.linspace(-0.3, 1.0, 400)
    left.plot(grid, 1.0 / (1.0 + np.exp((grid - mu) / T)), color="0.4", lw=1.0,
              label="Fermi function of A")
    left.set_xlim(-0.3, 1.0)
    left.set_xlabel("level $\\varepsilon$ (units of $|m|$)")
    left.set_ylabel("occupation $f$")
    left.set_title(f"$T = {T}$", fontsize=10)
    left.legend(fontsize=6, loc="lower left")
    for kind in "ABC":
        right.plot(TEMPS, [WARM[(t, kind)]["E_KS"] - t * WARM[(t, kind)]["entropy"]
                           for t in TEMPS], color=COLOUR[kind], label=NAME[kind],
                   **MARK[kind])
    right.set_xlabel("temperature $T$ (units of $|m|$)")
    right.set_ylabel("free energy $F = E - TS_{ent}$ (units of $|m|$)")
    fig.suptitle("$N = 136$, $\\lambda = \\lambda_1$, $a_{4,0} = 1$", fontsize=10)
    fig.tight_layout()
    save_figure(fig, "thermal_states",
                "Thermal Kohn-Sham states for $N = 136$, $\\lambda = \\lambda_1$, "
                "$a_{4,0} = 1$. Left: the occupation $f$ of every level against its "
                "energy (units of $|m|$) at $T = 0.05$ for A (blue rings), B (orange "
                "crosses) and C (aqua triangles); the grey curve is the Fermi function "
                "of A. Every cross of B sits in a ring of A. Right: the free energy "
                "$F = E - TS_{ent}$ against the temperature $T$ (units of $|m|$); A and "
                "B coincide, the control C lies about $3$ lower.")
    '''),
    md(r"""
    ## 16. The last check

    The last cell checks that the ten figure files exist in the folder
    Revision/textbook/figures, prints how many times the solver was run, and prints
    the number of checks that passed.
    """),
    code(r'''
    runs = len({id(state) for state in [*SELF.values(), *HIST.values(), *SCAN.values(),
                                        *WARM.values()]})
    report("runs of the Rust solver in this notebook", runs)
    names = ["level_ladder", "level_differences", "density_profiles",
             "mass_and_potential", "emt_profiles", "zero_modes_n8", "history_energy",
             "history_agreement", "coupling_scan", "thermal_states"]
    paths = [output_file(f"{FIGURE_FOLDER}/19a_{k}_{name}.png")
             for k, name in enumerate(names, 1)]
    check(runs == 59 and all(path.is_file() for path in paths),
          "every figure file of this notebook exists")
    all_checks_passed()
    '''),
    md(r"""
    ## 17. What this notebook showed

    - COMPUTED (59 independent runs of the Rust Kohn-Sham solver): the universe of mass
      $-m$ with the same coupling $+\lambda$ and the transformed tip angle $\pi$ (B) has
      the same Kohn-Sham levels, level by level with the block type and the brane
      parity exchanged, the same occupations, chemical potential, entropy, energy and
      free energy, and the same particle density, potential and energy-momentum
      profiles $\rho$, $p_3$, $p_t$, $p_8$ as the universe of mass $+m$ (A), while its
      scalar density, density $Q$ and effective mass are exactly opposite; the
      differences are about $10^{-13}$ or smaller, the rounding of the computer.
      This holds for 8, 136 and 688 particles, at every slice of the deflating history,
      for every coupling and at every temperature computed.
    - COMPUTED: the solver's own T3 self-test of the record
      (`ks-rust-solver.json`, check `t3_block_map_solver_selftest`) is reproduced, and
      every A run reproduces the committed canonical state.
    - COMPUTED (negative controls): with the untransformed tip (C) the zero modes move
      to the tip and every energy differs; with the reversed coupling (D) the energy is
      that of A at $-\lambda$, not at $\lambda$.
    - PROVED elsewhere (records `wolfram-t3.json`, `python-t3.json`): theorem T3
      itself. The runs here confirm it numerically; they are not its proof.
    - ASSUMED: the $Z_2$ brane; the tip is a chosen cutoff and T3 needs the transformed
      tip angle; the history is a PRESCRIBED BACKGROUND; mean field without correlation.
    - NOT shown: that a universe is created, in pairs or otherwise. T3 maps solutions
      onto solutions; it gives no creation process, rate or amplitude, and it does not
      force the partner to exist.
    """),
]

if __name__ == "__main__":
    raise SystemExit(run_builder(__file__))
