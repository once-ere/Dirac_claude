#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
"""Builder of Notebook 15b, "Energy-momentum profiles and the conservation along the
hidden direction" (textbook "Universes in Pairs", chapter 15).

The notebook Revision/textbook/notebooks/15b_emt_profiles.ipynb is BUILT from this file by
Revision/textbook/tools/nbkit.py (never edit the .ipynb by hand):

    python Revision/textbook/tools/nbkit.py build \
        Revision/textbook/notebooks/src/15b_emt_profiles.py --date YYYY-MM-DD
    python Revision/textbook/tools/nbkit.py check \
        Revision/textbook/notebooks/src/15b_emt_profiles.py

The notebook runs the Revision Kohn-Sham solver (subcommand "single") to produce the
energy-momentum profiles of chosen states into Revision/kohn_sham/solver/target/
textbook_15b (ignored by git), checks them against the committed profiles, verifies the
conservation law along the hidden coordinate (p0' + 3H (p0 - p_t) = 0) and the
energy-change identity dE/da4 = -3 P3 + P_t + P0/3 along the deflating history (the
corrected metric of 2026-10-16), tests the source conditions of the a4 and b4 equations
on its own numbers, and draws seven figures.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools"))
from nbkit import code, md, run_builder  # noqa: E402

FIGURES = [
    "15b_1_proper_emt",
    "15b_2_coordinate_emt",
    "15b_3_y_conservation",
    "15b_4_energy_slopes",
    "15b_5_integrated_ratios",
    "15b_6_energy_spreading",
    "15b_7_interaction_terms",
]

FACTS = {
    "id": "15b",
    "name": "15b_emt_profiles",
    "title": "Energy-momentum profiles and the conservation law along the hidden direction",
    "purpose": (
        "It runs the Rust Kohn-Sham solver for chosen states of the Kohn-Sham gas of "
        "dirac16complex in the corrected metric, reads the profiles of the energy "
        "density and of the three pressures along the hidden coordinate, checks them "
        "against the committed Revision record, verifies the conservation law of the "
        "energy-momentum tensor along the hidden direction point by point and "
        "integrated, integrates the profiles to the total energy, and checks the "
        "energy-change identity along the deflating history: dE/da4 equals minus three "
        "times the integrated 3-space pressure plus the integrated extra-time pressure "
        "plus one third of the integrated hidden-direction pressure. It also tests, on "
        "its own numbers and on the committed profiles, the conditions that a source of "
        "the equations for a4 and b4 must meet, and reproduces the Revision record that "
        "shows that the Kohn-Sham states fail them (the history is a prescribed "
        "background). Before it runs the solver, the notebook builds it with cargo (a "
        "full build of about a minute when the program is missing, a second when it is "
        "up to date). The solver writes its output files (about 0.7 MB) into the folder "
        "`Revision/kohn_sham/solver/target/textbook_15b`, which git ignores."
    ),
    "records": [
        ["Revision/kohn_sham/results/ground/profiles",
         "the committed profiles of the 75 ground states"],
        ["Revision/kohn_sham/results/ground/emt-integrals.csv",
         "the integrated energy-momentum tensor of every ground state"],
        ["Revision/kohn_sham/results/ground/summary.csv",
         "the Kohn-Sham energies of the ground states"],
        ["Revision/kohn_sham/results/adiabatic/adiabaticity.csv",
         "the derivative dE/da4 from finite differences between slices"],
        ["Revision/kohn_sham/results/parameters.json",
         "the couplings of N = 592"],
        ["Revision/kohn_sham/ks-theory.json",
         "the formulas of the energy-momentum tensor and its two identities"],
        ["Revision/kohn_sham/reports/ks-rust-solver.json",
         "the solver checks emt_y_conservation and emt_energy_change_dE_da4"],
        ["Revision/field_equations_a4/reports/ks-source-conditions.json",
         "why the Kohn-Sham states are not an admissible source of the a4 and b4 "
         "equations"],
    ],
    "packages": ["numpy", "matplotlib"],
    "needs_rust": [{"manifest": "Revision/kohn_sham/solver/Cargo.toml",
                    "binaries": ["revision_ks_solver"], "build_minutes": 1}],
    "expected_seconds": 60,
    "timeout_seconds": 900,
    "files_written": ["Revision/textbook/figures/15b.captions.json"]
    + [f"Revision/textbook/figures/{name}.png" for name in FIGURES],
    "final_lines": [
        "PASS every figure file of this notebook exists",
        "ALL 20 CHECKS PASSED (notebook 15b)",
    ],
    "troubleshooting": [
        ["You want the disk space of the solver output back",
         "the folder `Revision/kohn_sham/solver/target/textbook_15b` holds only "
         "the raw output of the last run (21 files, about 0.7 MB), which git "
         "ignores; delete it at any time, the notebook writes it again."],
    ],
    "work_folders": ["Revision/kohn_sham/solver/target/textbook_15b"],
}

CELLS = [
    md(r"""
    ## 1. What this notebook computes

    A Kohn-Sham state of dirac16complex carries energy and momentum. The
    **energy-momentum tensor** of the state has four different diagonal components: the
    energy density $\rho$ and the pressures $p_3$ (along 3-space), $p_t$ (along the
    three extra times) and $p_0$ (along the hidden direction). They depend on the
    hidden coordinate $y$. This notebook

    - runs the Rust Kohn-Sham solver for two states and checks that the profiles it
      writes are those of the committed Revision record;
    - draws the four components, as proper densities and as the densities that are
      integrated over $y$, and shows that the free gas has $p_3 = \rho/3$ and
      $p_0 = p_t = 0$ at every point;
    - checks the **conservation law along the hidden direction**,
      $(e^{3Hy} p_0)' = 3H e^{3Hy} p_t$, point by point and integrated;
    - integrates the energy density to the total Kohn-Sham energy;
    - solves the free state $N = 592$ at 17 slices of the deflating history and checks
      the **energy-change identity**
      $dE/da_4 = -3P_3 + P_t + \tfrac13 P_0$ (with $P$ the integrated pressures), and
      checks it with interaction on all 75 ground states of the record;
    - shows how the interaction adds the same energy density to $p_3$, $p_t$ and $p_0$;
    - tests the conditions that a source of the equations for $a_4$ and $b_4$ must meet,
      and reproduces the Revision record that shows they fail.

    It draws seven figures and takes about a minute.
    """),
    md(r"""
    ## 3. The words used in this notebook

    - **Energy-momentum tensor** $T^\mu{}_\nu$: a table of $8 \times 8$ numbers at each
      point that says how much energy and momentum there is and how it flows. Its
      diagonal holds the **energy density** $\rho = -T^{x_4}{}_{x_4}$ and the
      **pressures** $p_\mu = T^{\mu}{}_{\mu}$ (no sum), the force per area in the
      direction $\mu$ (the sign convention of the Revision record).
    - $p_3$: the pressure along each of the three directions of 3-space ($x_1, x_2,
      x_3$); $p_t$: along each extra time ($x_5, x_6, x_7$); $p_0$: along the hidden
      direction.
    - **Interaction energy density** $e_{int} = \lambda(\tfrac{15}{32}S^2 -
      \tfrac{1}{32}n^2)$: the energy of the contact interaction per proper 7-volume.
    - **Proper density** (per proper 7-volume) and **coordinate density** (per unit of
      $y$ and of the coordinates $x_1 \dots x_7$; it is $\mathrm{Vol}_7\,e^{3Hy}$ times
      the proper density per unit coordinate volume of the cell, because the proper
      7-volume of the cell per unit of $y$ is $\mathrm{Vol}_7 e^{3Hy}$).
    - **Integrated pressure** $P = 2\,\mathrm{Vol}_7\int_{-L}^{0} e^{3Hy}p\,dy$: the
      pressure summed over the whole cell (both halves).
    - **Conservation law**: the statement $\nabla_\mu T^\mu{}_\nu = 0$ (the covariant
      divergence vanishes). In flat spacetime it says that energy and momentum are
      neither created nor destroyed, they only flow. In the author's metric, which
      depends on the time $x_4$ through $a_4$ and $b_4$, it is a local balance law: the
      energy is not conserved, it changes along the history (sections 4 and 9).
    - **Finite difference**: an approximation of a derivative from values at nearby
      points; the fourth-order formula
      $f'(y_i) \approx [f_{i-2} - 8 f_{i-1} + 8 f_{i+1} - f_{i+2}]/(12h)$ has an error
      proportional to $h^4$.
    - **Symmetric logarithmic axis**: logarithmic for large positive and negative values
      and linear near zero, so that both signs fit on one axis.
    - **Tangent**: the straight line that touches a curve at one point; its slope is the
      derivative there.
    - **Source conditions**: what the right-hand side of the field equations for $a_4$
      and $b_4$ must satisfy; a matter state that fails them cannot produce the history.
    """),
    md(r"""
    ## 4. The physical and mathematical situation

    **Geometry.** In the hidden coordinate $y$ (tip $y = -L = -3$, fold $y = 0$) the
    author's corrected metric reads (Revision record Revision/kohn_sham/ks-theory.json)

    $$ds^2 = e^{2a_4}(dx_1^2 + dx_2^2 + dx_3^2) - dx_4^2
    + f^2\left[dy^2 - e^{2Hy}(dx_5^2 + dx_6^2 + dx_7^2)\right], \qquad
    f = e^{-a_4}b_4^{1/2}.$$

    3-space ($x_1, x_2, x_3$) inflates with $e^{a_4}$ and has no warp; the three extra
    times ($x_5, x_6, x_7$) and the hidden direction deflate with $f$; the proper volume
    factor is $\sqrt{|g|} = e^{-a_4}b_4^2 e^{3Hy}$, so the proper 7-volume of the cell
    per unit of $e^{3Hy}\,dy$ is $\mathrm{Vol}_7 = \ell^3 v_t\,e^{-a_4}b_4^2 =
    \ell^3 v_t\,e^{(5/3)a_{4,0}}$ on the record's history $b_4 = e^{(4/3)a_4}$.

    **The tensor of a Kohn-Sham state** (ks-theory.json, emt; sums over the occupied
    levels with the weights $w g f$, $w = 1/2$; $n_o$, $s_o$, $t_o$ are the number,
    scalar and current densities of one orbital, $n_o = P(a^2 + b^2)$,
    $s_o = P\,j\,2ab$, $t_o = P\,j(a^2 - b^2)$, $P = e^{-3Hy}/\mathrm{Vol}_7$):

    $$\rho = \sum w g f\,\varepsilon\,n_o - e_{int}, \qquad
    p_3 = \sum w g f\,\tfrac{\kappa |k|}{3}\,t_o + e_{int}, \qquad p_t = e_{int},$$
    $$p_0 = \sum w g f\left[(\varepsilon - v)\,n_o - M s_o - \kappa|k|\,t_o\right]
    + e_{int} .$$

    The extra-time pressure contains no kinetic part: the states belong to the *good
    sector*, which has no momentum along the extra times. For a fold-band orbital
    $(a, b) = (e^{fMy}, 0)$ with $\varepsilon = \kappa k$ the bracket of $p_0$ is
    $(\kappa k - 0)a^2 - 0 - \kappa k\,a^2 = 0$ and $\varepsilon\,n_o = \kappa k\,t_o$:
    the free gas has $p_0 = p_t = 0$ and $p_3 = \rho/3$ exactly.

    **Conservation along $y$.** For a tensor that is diagonal and depends only on $y$,
    the $y$ component of $\nabla_\mu T^\mu{}_\nu = 0$ is

    $$\partial_y T^y{}_y + \Gamma^\mu{}_{\mu y} T^y{}_y
    - \sum_\nu \Gamma^\nu{}_{\nu y} T^\nu{}_\nu = 0$$

    (the index $\nu$ runs over the eight directions; the letter $\lambda$ is kept for
    the coupling). Line by line:
    $\Gamma^\mu{}_{\mu y} = \partial_y \ln\sqrt{|g|} = 3H$ (the derivative of $\ln
    e^{3Hy}$); $\Gamma^\nu{}_{\nu y} = \tfrac12 g^{\nu\nu}\partial_y g_{\nu\nu} = H$ for
    each of the three extra times (their $g_{\nu\nu}$ contains $e^{2Hy}$, and half the
    derivative of $\ln e^{2Hy}$ is $H$) and $0$ for 3-space (no warp), $x_4$ and $y$;
    the three warped terms are $3H p_t$; so

    $$p_0' + 3H p_0 - 3H p_t = 0, \quad\text{that is}\quad
    (e^{3Hy} p_0)' = 3H\,e^{3Hy}\,p_t,$$

    because $(e^{3Hy}p_0)' = e^{3Hy}(p_0' + 3Hp_0)$ (product and chain rule). Integrated
    from tip to fold: $[e^{3Hy}p_0]_{-L}^{0} = 3H \int_{-L}^{0} e^{3Hy}p_t\,dy$. The
    3-space pressure does not enter.

    **Energy change along the history.** The $x_4$ component of the same law, with
    $T^{x_4}{}_{x_4} = -\rho$, $\Gamma^\mu{}_{\mu x_4} = \partial_{x_4}\ln\sqrt{|g|} =
    -a_4' + 2b_4'/b_4$ and $\Gamma^\nu{}_{\nu x_4} = \tfrac12\partial_{x_4}\ln|g_{\nu\nu}|
    = a_4'$ (3-space), $h_4 = b_4'/(2b_4) - a_4'$ (each extra time and the hidden
    direction), $0$ ($x_4$), reads (ks-theory.json, emt.energyChange)
    $\partial_{x_4}\rho = -3a_4'(\rho + p_3) - 3h_4(\rho + p_t) - h_4(\rho + p_0)$. On the
    history $a_4' = AH$ and $b_4'/b_4 = \tfrac43 AH$, so $h_4 = -\tfrac13 AH$; with
    $\partial_{x_4} = a_4'\,\partial/\partial a_4$ and the total energy
    $E = 2\,\mathrm{Vol}_7\int e^{3Hy}\rho\,dy$, whose volume factor grows like
    $e^{(5/3)a_4}$, the terms with $\rho$ cancel and

    $$\frac{dE}{da_4} = -3P_3 + P_t + \tfrac13 P_0, \qquad
    P = 2\,\mathrm{Vol}_7\int_{-L}^{0} e^{3Hy}p\,dy .$$

    Read as work: when 3-space inflates by $da_4$, the gas loses $3P_3\,da_4$ (the work
    of its 3-space pressure); the three extra times and the hidden direction shrink by
    the factor $e^{-da_4/3}$ each, and the gas gains $P_t\,da_4$ and
    $\tfrac13P_0\,da_4$. The free gas has $P_t = P_0 = 0$ and $P_3 = E/3$, so
    $dE/da_4 = -E$: its energy falls exactly like $e^{-a_4}$.

    **Status.** The tensor is COMPUTED by the solver; the two identities are exact and
    are checked here numerically. The history $a_4 = A H x_4$, $b_4 = e^{(4/3)AHx_4}$ is
    a PRESCRIBED BACKGROUND: the Kohn-Sham tensor depends on $y$ (hence on $x_0$), and
    with interaction $p_0 \ne p_t$, so it is not an admissible source of the equations
    for $a_4$ and $b_4$ (Revision record
    Revision/field_equations_a4/reports/ks-source-conditions.json). Units: $H = m = 1$,
    $L = 3$, $\mathrm{Vol}_7(0) = (2\pi/0.25)^3$.
    """),
    md(r"""
    ## 5. Building the solver and producing two profiles

    The next cell builds the solver (`rust_program`, about a second when it is up to
    date) and defines a helper `solve_state` that runs the subcommand `single` for one
    state: `--m`, `--lambda`, `--a4`, `--N` give the mass, coupling, slice and particle
    number, `--out` names the JSON file of the results and `--profiles` the CSV file of
    the profiles. The files go into the folder `textbook_15b` inside the Rust build
    folder `target`, which git ignores. It also defines `vol7`, the proper 7-volume
    $\mathrm{Vol}_7$ of the cell per unit $e^{3Hy}$ at a slice. Then it solves the free
    state $N = 592$ at $a_{4,0} = 1$ and the strongly interacting state $N = 592$,
    $+\lambda_2$, at $a_{4,0} = 2$.
    """),
    code(r'''
    import csv  # reads the tables (CSV files)
    import math  # exp and pi for single numbers

    import numpy as np  # arrays of numbers

    program = rust_program("Revision/kohn_sham/solver/Cargo.toml", "revision_ks_solver")
    RUN_FOLDER = REPO / "Revision/kohn_sham/solver/target/textbook_15b"  # ignored by git
    RUN_FOLDER.mkdir(parents=True, exist_ok=True)
    PALETTE = ["#2a78d6", "#eb6834", "#1baf7a", "#eda100", "#e87ba4", "#008300",
               "#4a3aa7", "#e34948"]  # the colours of the figures, in a fixed order
    SLICE_SHADES = ["#86b6ef", "#5598e7", "#2a78d6", "#1c5cab", "#104281"]  # light->dark
    H = 1.0


    def vol7(a4):
        """The proper 7-volume of the cell per unit e^{3Hy}: (2 pi/0.25)^3 e^{(5/3) a4}."""
        return (2.0 * math.pi / 0.25) ** 3 * math.exp((2.0 * 4.0 / 3.0 - 1.0) * a4)


    def solve_state(name, n, lam, a4, profiles=False):
        """Run "revision_ks_solver single" for one state; return its JSON record."""
        out = RUN_FOLDER / f"{name}.json"
        command = [str(program), "single", "--root", str(REPO), "--m", "1",
                   "--lambda", repr(lam), "--a4", repr(a4), "--N", repr(float(n)),
                   "--out", str(out)]
        if profiles:
            command += ["--profiles", str(RUN_FOLDER / f"{name}.csv")]
        done = subprocess.run(command, capture_output=True, text=True)
        if done.returncode != 0 or done.stdout.strip().split("\n")[-1] != "SUCCESS":
            raise RuntimeError(f"the solver failed for {name}: {done.stderr[-500:]}")
        return json.loads(out.read_text(encoding="utf-8"))


    params = json.loads(repository_file("Revision/kohn_sham/results/parameters.json")
                        .read_text(encoding="utf-8"))
    LAMBDA2_592 = {int(c["N"]): c for c in params["couplingCalibration"]["values"]}[592][
        "lambda2"]  # the coupling lambda_2 of N = 592
    free_state = solve_state("N592_lam0_a10", 592, 0.0, 1.0, profiles=True)
    strong_state = solve_state("N592_lamp2_a20", 592, LAMBDA2_592, 2.0, profiles=True)
    say(f"solved N592_lam0_a10 ({free_state['iterations']} iteration) and N592_lamp2_a20 "
        f"({strong_state['iterations']} iterations, lambda = {LAMBDA2_592})")
    '''),
    md(r"""
    The next cell reads the two new profile files and the corresponding committed files
    of the record (`ground/profiles/N592_lam0_a10.csv` and `N592_lamp2_a20.csv`) and
    compares every column. The largest difference is measured relative to the largest
    value of the column's family: the densities $n$, $S$, $Q$; the potentials
    $M_{eff}$, $v_v$, $w_Q$; the components $e_{int}$, $\rho$, $p_3$, $p_t$, $p_0$ of
    the tensor (a column that vanishes, such as $p_0$ of the free state, holds only
    rounding values, so it is measured against its family). The tolerance $10^{-9}$ is
    far below the accuracy of the profiles themselves ($10^{-6}$, the tolerance of the
    record's refined comparison). Whether the files are byte-identical is printed as a
    RESULT line.
    """),
    code(r'''
    RECORD_PROFILES = "Revision/kohn_sham/results/ground/profiles"
    FAMILIES = [["y"], ["n", "S", "Q"], ["M_eff", "v_v", "w_Q"],
                ["e_int", "rho", "p3", "p_t", "p0"]]  # columns compared together


    def read_profile(path):
        """A profile table as a dictionary column -> numpy array."""
        data = np.genfromtxt(path, delimiter=",", names=True)
        return {name: data[name] for name in data.dtype.names}


    worst = 0.0
    identical = []
    for name in ("N592_lam0_a10", "N592_lamp2_a20"):
        new = read_profile(RUN_FOLDER / f"{name}.csv")
        old = read_profile(repository_file(f"{RECORD_PROFILES}/{name}.csv"))
        for family in FAMILIES:
            scale = max(max(float(np.max(np.abs(old[c]))) for c in family), 1e-300)
            for column in family:
                worst = max(worst, float(np.max(np.abs(new[column] - old[column]))) / scale)
        identical.append((RUN_FOLDER / f"{name}.csv").read_bytes()
                         == repository_file(f"{RECORD_PROFILES}/{name}.csv").read_bytes())
    say("columns: " + ", ".join(old))
    report("largest difference to the record, relative to the family", f"{worst:.1e}")
    report("profile files byte-identical to the record", identical)
    check(worst < 1e-9, "the new profiles equal the committed profiles within 1e-9",
          record=f"{RECORD_PROFILES}/N592_lam0_a10.csv and N592_lamp2_a20.csv")
    '''),
    md(r"""
    ## 6. The four components as proper densities

    The next cell draws $\rho$, $p_3$, $p_t$ and $p_0$ of the free state $N = 592$,
    $\lambda = 0$, $a_{4,0} = 1$ against $y$, on a logarithmic vertical axis for the two
    components that do not vanish. Section 4 showed that the free fold-band gas has
    $p_3 = \rho/3$ and $p_0 = p_t = 0$ at every point. The checks: $p_t = e_{int} = 0$
    exactly; $p_0$ vanishes to rounding and $p_3 = \rho/3$, both within $10^{-12}$ of
    the largest component.
    """),
    code(r'''
    prof = read_profile(RUN_FOLDER / "N592_lam0_a10.csv")
    y = prof["y"]
    step = float(y[1] - y[0])  # 0.02
    COMPONENTS = [("rho", "$\\rho$"), ("p3", "$p_3$"), ("p_t", "$p_t$"), ("p0", "$p_0$")]
    t_scale = max(float(np.max(np.abs(prof[c]))) for c, _ in COMPONENTS)  # max |T|
    fig, ax = plt.subplots()
    ax.semilogy(y, prof["rho"], color=PALETTE[0], lw=2.5, label="$\\rho$")
    ax.semilogy(y, prof["p3"], color=PALETTE[1], lw=2.5, label="$p_3$")
    ax.semilogy(y, prof["rho"] / 3.0, color="black", lw=1.0, ls=":", label="$\\rho/3$")
    ax.set_xlabel("hidden coordinate $y$ (tip at $-3$, fold at $0$)")
    ax.set_ylabel("proper density (units of $m^8$)")
    ax.set_title("Energy density and pressure, $N = 592$, $\\lambda = 0$, $a_{4,0} = 1$")
    ax.legend()
    p0_size = float(np.max(np.abs(prof["p0"]))) / t_scale  # p0 relative to max |T|
    eos_dev = float(np.max(np.abs(prof["p3"] - prof["rho"] / 3.0))) / t_scale
    save_figure(fig, "proper_emt",
                "The energy density $\\rho$ and the 3-space pressure $p_3$ of the free "
                "Kohn-Sham state $N = 592$, $\\lambda = 0$, $a_{4,0} = 1$ as proper "
                "densities (vertical axis, logarithmic, units of $m^8$) against the "
                "hidden coordinate $y$ (horizontal axis). Both are largest at the tip, "
                "where the proper volume is small, and $p_3$ lies on the dotted curve "
                "$\\rho/3$ at every point. The other two pressures are not drawn: "
                "$p_t = 0$ exactly and $p_0$ vanishes to rounding, because the "
                "fold-band orbitals carry no hidden kinetic pressure.")
    report("largest |p_t| and largest |p0| / max|T|",
           f"{float(np.max(np.abs(prof['p_t'])))}, {p0_size:.1e}")
    report("largest |p3 - rho/3| / max|T|", f"{eos_dev:.1e}")
    check(float(np.max(np.abs(prof["p_t"]))) == 0.0, "p_t = e_int = 0 when lambda = 0")
    check(p0_size < 1e-12 and eos_dev < 1e-12,
          "the free gas has p0 = 0 and p3 = rho/3 at every point, to 1e-12",
          record="Revision/field_equations_a4/reports/ks-source-conditions.json, check "
                 "ks_hidden_pressure_condition")
    '''),
    md(r"""
    ## 7. What is integrated: the coordinate densities

    Multiplying by $2\,\mathrm{Vol}_7\, e^{3Hy}$ turns a proper density into the amount
    per unit of $y$ in the whole cell. The next cell draws these densities of the free
    state (now on a linear axis) and integrates them with Simpson's rule on the 151
    points: the integral of the energy density must be the Kohn-Sham energy $E_{KS}$ of
    the solver's JSON record (and of the committed table `ground/summary.csv`), and the
    integrals of the energy density and of $p_3$ must agree with the committed table
    `ground/emt-integrals.csv`. The solver integrates on a finer grid (1801 points), so
    the comparison allows a relative difference of $10^{-6}$.
    """),
    code(r'''
    def simpson(values, h):
        """Simpson's rule on equally spaced points (an odd number of them)."""
        weights = np.full(len(values), 2.0)
        weights[1::2] = 4.0
        weights[0] = weights[-1] = 1.0
        return h / 3.0 * float(np.sum(weights * values))


    def read_rows(relative):
        """The rows of a committed CSV table of the record as a dictionary by id."""
        with open(repository_file(relative), newline="", encoding="utf-8") as handle:
            return {row["id"]: row for row in csv.DictReader(handle)}


    EMT_TABLE = "Revision/kohn_sham/results/ground/emt-integrals.csv"
    emt_rows = read_rows(EMT_TABLE)
    summary_rows = read_rows("Revision/kohn_sham/results/ground/summary.csv")
    weight = 2.0 * vol7(1.0) * np.exp(3.0 * H * y)  # 2 Vol_7 e^{3Hy} at a4,0 = 1
    fig, ax = plt.subplots()
    integrals = {}
    for colour, (column, label) in zip(PALETTE, COMPONENTS):
        ax.plot(y, weight * prof[column], color=colour, lw=2.0, label=label)
        integrals[column] = simpson(weight * prof[column], step)
    ax.axhline(0.0, color="0.4", lw=0.8)
    ax.set_xlabel("hidden coordinate $y$")
    ax.set_ylabel("$2\\,\\mathrm{Vol}_7\\, e^{3Hy} \\times$ component (units of $m$)")
    ax.set_title("The integrands: energy and pressures per unit $y$")
    ax.legend()
    save_figure(fig, "coordinate_emt",
                "The energy density and the pressures of the free state $N = 592$, "
                "$\\lambda = 0$, $a_{4,0} = 1$ multiplied by $2\\,\\mathrm{Vol}_7 "
                "e^{3Hy}$ (vertical axis, linear, units of $m$ per unit $y$) against "
                "$y$ (horizontal axis). In this form the energy and the 3-space "
                "pressure sit near the fold, and $p_t$ and $p_0$ lie on the zero line; "
                f"the area under $\\rho$ is the Kohn-Sham energy "
                f"$E_{{KS}} = {free_state['E_KS']:.3f}$, and the area under $p_3$ is a "
                "third of it.")
    row = emt_rows["N592_lam0_a10"]
    rel = lambda a, b: abs(a - b) / max(abs(b), 1e-300)
    worst_int = max(rel(integrals[c], float(row[f"int_{c}"])) for c in ("rho", "p3"))
    report("E_KS from the profile / from the solver",
           f"{integrals['rho']:.8f} / {free_state['E_KS']:.8f}")
    report("largest relative difference of the integrals to the record", f"{worst_int:.1e}")
    check(rel(free_state["E_KS"], float(summary_rows["N592_lam0_a10"]["E_KS"])) < 1e-12,
          "the solver's E_KS equals the record",
          record="Revision/kohn_sham/results/ground/summary.csv, N592_lam0_a10")
    check(rel(integrals["rho"], free_state["E_KS"]) < 1e-6 and worst_int < 1e-6,
          "Simpson's rule on the profile gives E_KS and the recorded integrals",
          record=f"{EMT_TABLE}, columns int_rho, int_p3")
    '''),
    md(r"""
    ## 8. The conservation law along the hidden direction

    For the free state both sides of $(e^{3Hy}p_0)' = 3H e^{3Hy} p_t$ vanish. The law
    becomes a real test with interaction: the next cell uses the strongly interacting
    state $N = 592$, $+\lambda_2$, $a_{4,0} = 2$, computes the left side by the
    fourth-order finite difference (one-sided fourth-order formulas at the two ends, as
    in the solver) and the right side, draws both, and draws their difference divided
    by the largest of the two sides. It also compares the jump
    $[e^{3Hy}p_0]_{-3}^{0}$ with the integral of the right side. The solver checked the
    same law on its fine grid (record checks `emt_y_conservation_pointwise` and
    `emt_y_conservation_integrated`); on the 151 points of the profile the finite
    difference is less accurate, so the tolerances here are $10^{-4}$ (point by point)
    and $10^{-6}$ (integrated). For the free state the cell checks that both sides
    vanish to rounding.
    """),
    code(r'''
    def derivative4(f, h):
        """Fourth-order finite-difference derivative (one-sided at the two ends)."""
        d = np.zeros(len(f))
        d[2:-2] = (f[:-4] - 8.0 * f[1:-3] + 8.0 * f[3:-1] - f[4:]) / (12.0 * h)
        d[0] = (-25 * f[0] + 48 * f[1] - 36 * f[2] + 16 * f[3] - 3 * f[4]) / (12.0 * h)
        d[1] = (-3 * f[0] - 10 * f[1] + 18 * f[2] - 6 * f[3] + f[4]) / (12.0 * h)
        d[-1] = (25 * f[-1] - 48 * f[-2] + 36 * f[-3] - 16 * f[-4] + 3 * f[-5]) / (12.0 * h)
        d[-2] = (3 * f[-1] + 10 * f[-2] - 18 * f[-3] + 6 * f[-4] - f[-5]) / (12.0 * h)
        return d


    def conservation(p):
        """(left side, right side, pointwise residual, integrated residual) of the law."""
        e3 = np.exp(3.0 * H * p["y"])
        left = derivative4(e3 * p["p0"], step)
        right = 3.0 * H * e3 * p["p_t"]
        scale = max(float(np.max(np.abs(left))), float(np.max(np.abs(right))))
        jump = e3[-1] * p["p0"][-1] - e3[0] * p["p0"][0]
        integral = simpson(right, step)
        return left, right, np.abs(left - right) / scale, abs(jump - integral) / abs(jump)


    sp = read_profile(RUN_FOLDER / "N592_lamp2_a20.csv")
    left, right, residual, integrated = conservation(sp)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10.0, 4.0), layout="constrained")
    ax1.plot(sp["y"], left, color=PALETTE[0], lw=3.0, label="$(e^{3Hy}p_0)'$")
    ax1.plot(sp["y"], right, color=PALETTE[1], lw=1.5, ls="--",
             label="$3H\\,e^{3Hy}p_t$")
    ax1.set_xlabel("hidden coordinate $y$")
    ax1.set_ylabel("units of $m^9$")
    ax1.set_title("The two sides of the law")
    ax1.legend()
    ax2.semilogy(sp["y"], np.maximum(residual, 1e-16), color=PALETTE[2], lw=1.5)
    ax2.axhline(1e-4, color="0.4", ls=":", lw=1.2, label="tolerance $10^{-4}$")
    ax2.set_xlabel("hidden coordinate $y$")
    ax2.set_ylabel("|left - right| / largest value")
    ax2.set_title("Relative residual on the 151 points")
    ax2.legend()
    save_figure(fig, "y_conservation",
                "Left: the two sides of the conservation law along the hidden "
                "direction, $(e^{3Hy}p_0)'$ (solid) and $3H e^{3Hy}p_t$ (dashed), for "
                "the interacting state $N = 592$, $+\\lambda_2$, $a_{4,0} = 2$ "
                "(vertical axis, units of $m^9$; horizontal axis $y$); the curves lie "
                "on top of each other. Right: their difference relative to the largest "
                "value (logarithmic), the error of the finite difference on the coarse "
                "profile grid, far below the tolerance.")
    free_e3 = np.exp(3.0 * H * y)
    free_sides = max(float(np.max(np.abs(derivative4(free_e3 * prof["p0"], step)))),
                     float(np.max(np.abs(3.0 * H * free_e3 * prof["p_t"])))) / t_scale
    report("largest pointwise residual / integrated residual",
           f"{float(np.max(residual)):.1e} / {integrated:.1e}")
    report("free state: largest side of the law / max|T|", f"{free_sides:.1e}")
    check(float(np.max(residual)) < 1e-4 and integrated < 1e-6,
          "(e^{3Hy} p0)' = 3H e^{3Hy} p_t holds for N592_lamp2_a20",
          record="Revision/kohn_sham/reports/ks-rust-solver.json, checks "
                 "emt_y_conservation_pointwise and emt_y_conservation_integrated")
    check(free_sides < 1e-10, "both sides of the law vanish for the free state")
    '''),
    md(r"""
    ## 9. The energy along the history and its slope

    The next cell solves the free state $N = 592$ at 17 slices,
    $a_{4,0} = 0, 0.125, 0.25, \dots, 2$ (about a second each), and reads from each
    JSON record the energy $E_{KS}$ and the integrals
    $2\,\mathrm{Vol}_7\int e^{3Hy}(\cdot)\,dy$ of $\rho$, $p_3$, $p_t$, $p_0$ that the
    solver computed on its fine grid. From them it forms the slope
    $-3P_3 + P_t + \tfrac13P_0$ of the energy-change identity. At the five slices of
    the canonical matrix the energies and integrals must equal the committed tables, and
    the slopes must equal the derivative $dE/da_4$ that the solver obtained by
    finite differences between neighbouring slices (column `dE_da4_finite_difference`
    of `adiabatic/adiabaticity.csv`).
    """),
    code(r'''
    DENSE = [i / 8.0 for i in range(17)]  # the slices 0, 0.125, ..., 2
    history = []
    for a4 in DENSE:
        record = solve_state(f"N592_lam0_dense_{round(1000 * a4):04d}", 592, 0.0, a4)
        ints = record["emtIntegrals_2Vol7_int_e3Hy"]  # 2 Vol_7 int e^{3Hy} (...) dy
        history.append({"a4": a4, "E": record["E_KS"], "rho": ints["rho"],
                        "p3": ints["p3"], "p_t": ints["p_t"], "p0": ints["p0"],
                        "slope": -3.0 * ints["p3"] + ints["p_t"] + ints["p0"] / 3.0})
    adiabatic_rows = read_rows("Revision/kohn_sham/results/adiabatic/adiabaticity.csv")
    worst_e, worst_slope = 0.0, 0.0
    say("a4,0       E_KS     dE/da4 (EMT)   dE/da4 (record, finite differences)")
    for item in history:
        if item["a4"] in (0.0, 0.5, 1.0, 1.5, 2.0):
            key = f"N592_lam0_a{round(10 * item['a4']):02d}"
            recorded_slope = float(adiabatic_rows[key]["dE_da4_finite_difference"])
            worst_e = max(worst_e, rel(item["E"], float(summary_rows[key]["E_KS"])),
                          rel(item["p3"], float(emt_rows[key]["int_p3"])))
            worst_slope = max(worst_slope, rel(item["slope"], recorded_slope))
            say(f"{item['a4']:4.2f}  {item['E']:10.5f}  {item['slope']:12.6f}"
                f"  {recorded_slope:12.6f}")
    report("largest relative difference of E and int p3 to the record", f"{worst_e:.1e}")
    report("largest relative difference of the slopes", f"{worst_slope:.1e}")
    check(worst_e < 1e-12, "E_KS and the integrals at the five slices equal the record",
          record="Revision/kohn_sham/results/ground/summary.csv and emt-integrals.csv")
    check(worst_slope < 1e-8, "dE/da4 = -3 P3 + P_t + P0/3 at the five slices",
          record="Revision/kohn_sham/results/adiabatic/adiabaticity.csv, column "
                 "dE_da4_finite_difference")
    '''),
    md(r"""
    The identity also holds between the slices. The next cell integrates the slopes over
    the whole history with Simpson's rule on the 17 slices (step $0.125$) and compares
    the result with the change of the energy itself, $E(2) - E(0)$: the energy lost by
    the gas along the history is exactly the work done by its pressures. The figure
    shows $E_{KS}$ at the 17 slices with short tangent lines whose slopes are computed
    from the pressures alone. The free gas checks only the term $-3P_3$; the cell
    therefore also evaluates $-3P_3 + P_t + \tfrac13P_0$ from the committed integrals of
    all 75 ground states, the 60 interacting ones included, and compares it with the
    recorded finite differences.
    """),
    code(r'''
    slopes = np.array([item["slope"] for item in history])
    energies = np.array([item["E"] for item in history])
    work = simpson(slopes, 0.125)  # integral of dE/da4 over the history
    change = energies[-1] - energies[0]
    fig, ax = plt.subplots()
    ax.plot(DENSE, energies, "o", color=PALETTE[0], ms=8, label="$E_{KS}$ (solver)")
    for a4, e, s in zip(DENSE, energies, slopes):
        ax.plot([a4 - 0.05, a4 + 0.05], [e - 0.05 * s, e + 0.05 * s], color=PALETTE[1],
                lw=2.5)
    ax.plot([], [], color=PALETTE[1], lw=2.0,
            label="slope $-3P_3 + P_t + P_0/3$ from the pressures")
    ax.set_xlabel("slice $a_{4,0}$ of the history")
    ax.set_ylabel("$E_{KS}$ (units of $m$)")
    ax.set_title("$N = 592$, $\\lambda = 0$: the pressures give the slope of the energy")
    ax.legend()
    save_figure(fig, "energy_slopes",
                "The Kohn-Sham energy $E_{KS}$ of $N = 592$ without interaction "
                "(vertical axis, units of $m$) at 17 slices $a_{4,0}$ of the history "
                "(horizontal axis), with short tangent lines whose slopes are computed "
                "from the pressures alone, $dE/da_4 = -3P_3 + P_t + P_0/3$: every line "
                f"touches the curve of the energies, which falls from ${energies[0]:.1f}$ "
                f"to ${energies[-1]:.1f}$, exactly like $e^{{-a_{{4,0}}}}$.")
    worst_law = 0.0  # the identity on the 75 recorded ground states
    for key, row in emt_rows.items():
        emt_slope = (-3.0 * float(row["int_p3"]) + float(row["int_p_t"])
                     + float(row["int_p0"]) / 3.0)
        recorded = float(adiabatic_rows[key]["dE_da4_finite_difference"])
        scale = max(abs(float(row["int_rho"])), 1.0)  # the energy scale of the state
        worst_law = max(worst_law, abs(emt_slope - recorded) / scale)
    report("E(2) - E(0) / integral of the slopes", f"{change:.6f} / {work:.6f}")
    report("largest |(-3 P3 + P_t + P0/3) - dE/da4| / max(E, 1), 75 recorded states",
           f"{worst_law:.1e}")
    check(rel(work, change) < 1e-5,
          "the integrated slope equals E(2) - E(0) within 1e-5 (relative)",
          record="Revision/kohn_sham/reports/ks-rust-solver.json, check "
                 "emt_energy_change_dE_da4")
    check(worst_law < 1e-8, "dE/da4 = -3 P3 + P_t + P0/3 in all 75 recorded ground states",
          record=f"{EMT_TABLE} and adiabatic/adiabaticity.csv")
    '''),
    md(r"""
    ## 10. The integrated pressures

    The next cell divides the integrated pressures by the integrated energy density.
    For the free gas section 4 gives $P_3/E = 1/3$ and $P_0 = P_t = 0$ at every slice,
    the integrated pressures of a gas of massless particles in 3-space: the fold-band
    levels are $\varepsilon = \kappa k$, linear in the momentum. With interaction the
    ratios move away from these values. The figure shows, from the committed table,
    $P_3/E$ (left) and $P_t/E$, $P_0/E$ (right) of $N = 592$ for the five couplings at
    the five slices. These ratios are integrated components only: what a 3-space
    observer would call an equation of state is not computed here (it needs the
    averaging over the hidden direction and the extra times, which is the subject of
    the Revision dark-sector work), and the history is a prescribed background.
    """),
    code(r'''
    ratio3 = np.array([item["p3"] / item["rho"] for item in history])
    free_dev = max(float(np.max(np.abs(ratio3 - 1.0 / 3.0))),
                   max(abs(item["p0"]) + abs(item["p_t"]) for item in history)
                   / min(item["rho"] for item in history))
    fig, (left, right) = plt.subplots(1, 2, figsize=(10.0, 4.0), layout="constrained")
    tags = [("lam0", "$0$"), ("lamp1", "$+\\lambda_1$"), ("lamm1", "$-\\lambda_1$"),
            ("lamp2", "$+\\lambda_2$"), ("lamm2", "$-\\lambda_2$")]
    signs_ok = True  # with interaction P_t/E and P_0/E have the sign of -lambda
    for colour, (tag, label) in zip(PALETTE, tags):
        keys = [f"N592_{tag}_a{round(10 * a):02d}" for a in (0.0, 0.5, 1.0, 1.5, 2.0)]
        e = [float(emt_rows[k]["int_rho"]) for k in keys]
        r3 = [float(emt_rows[k]["int_p3"]) / x for k, x in zip(keys, e)]
        rt = [float(emt_rows[k]["int_p_t"]) / x for k, x in zip(keys, e)]
        r0 = [float(emt_rows[k]["int_p0"]) / x for k, x in zip(keys, e)]
        left.plot([0, 0.5, 1, 1.5, 2], r3, "o-", color=colour, ms=6, lw=1.5, label=label)
        right.plot([0, 0.5, 1, 1.5, 2], rt, "s--", color=colour, ms=6, lw=1.2)
        right.plot([0, 0.5, 1, 1.5, 2], r0, "o-", color=colour, ms=6, lw=1.5)
        if tag != "lam0":
            sign = -1.0 if tag.startswith("lamp") else 1.0
            signs_ok = signs_ok and all(sign * v > 0.0 for v in rt + r0)
    left.axhline(1.0 / 3.0, color="0.4", ls=":", lw=1.2)
    left.set_xlabel("slice $a_{4,0}$")
    left.set_ylabel("$P_3 / E$")
    left.set_title("3-space pressure, $N = 592$ (dotted: $1/3$)")
    left.legend(fontsize=8)
    right.axhline(0.0, color="0.4", lw=0.8)
    right.plot([], [], "s--", color="0.4", label="$P_t / E$")
    right.plot([], [], "o-", color="0.4", label="$P_0 / E$")
    right.set_xlabel("slice $a_{4,0}$")
    right.set_ylabel("ratio of integrals")
    right.set_title("Extra-time and hidden pressures, $N = 592$")
    right.legend(fontsize=8)
    save_figure(fig, "integrated_ratios",
                "Left: the integrated 3-space pressure divided by the energy, "
                "$P_3/E$ (vertical axis, pure number), of $N = 592$ for the couplings "
                "$0$, $\\pm\\lambda_1$, $\\pm\\lambda_2$ at the five slices (horizontal "
                "axis), from the record; without interaction it is exactly $1/3$ "
                "(dotted), the value of massless particles. Right: $P_t/E$ (squares, "
                "dashed) and $P_0/E$ (circles), zero without interaction; with "
                "interaction both have the sign of $-\\lambda$. These are integrated "
                "components on a prescribed background, not an observed equation of "
                "state.")
    report("free gas: largest |P3/E - 1/3| and (|P_0| + |P_t|)/E at 17 slices",
           f"{free_dev:.1e}")
    check(free_dev < 1e-12, "the free gas has P3 = E/3 and P0 = P_t = 0 at all 17 slices",
          record=f"{EMT_TABLE}, columns int_rho, int_p3, int_p_t, int_p0")
    check(signs_ok, "with interaction P_t/E and P0/E have the sign of -lambda, N = 592")
    '''),
    md(r"""
    ## 11. Where the energy sits along the history

    The next cell reads the committed profiles of $N = 592$, $\lambda = 0$ at the five
    slices and draws the coordinate energy density divided by the total energy,
    $2\,\mathrm{Vol}_7 e^{3Hy}\rho(y)/E_{KS}$, whose area is 1. Every carrier of energy
    of the free gas is a fold-band orbital $e^{fMy}$, so this curve is exactly the
    normalised $e^{2fMy}$, $2fM\,e^{2fMy}/(1 - e^{-2fML})$, the same for every shell; as
    the hidden scale $f = e^{-a_{4,0}/3}$ shrinks, it spreads from the fold toward the
    tip. The check compares the curve with this formula and measures the spreading with
    the mean position $\langle y \rangle = \int y \cdot (\text{this density})\,dy$, which
    must decrease from slice to slice.
    """),
    code(r'''
    fig, ax = plt.subplots()
    means, worst_shape = [], 0.0
    for shade, a4 in zip(SLICE_SHADES, (0.0, 0.5, 1.0, 1.5, 2.0)):
        p = read_profile(repository_file(f"{RECORD_PROFILES}/N592_lam0_a"
                                         f"{round(10 * a4):02d}.csv"))
        density = 2.0 * vol7(a4) * np.exp(3.0 * H * p["y"]) * p["rho"]
        density = density / simpson(density, step)  # area 1
        fm = math.exp(-a4 / 3.0)  # f M with M = m = 1
        exact = 2.0 * fm * np.exp(2.0 * fm * p["y"]) / (1.0 - math.exp(-2.0 * fm * 3.0))
        worst_shape = max(worst_shape, float(np.max(np.abs(density - exact)))
                          / float(np.max(exact)))
        means.append(simpson(p["y"] * density, step))
        ax.plot(p["y"], density, color=shade, lw=2.0, label=f"$a_{{4,0}} = {a4}$")
    ax.set_xlabel("hidden coordinate $y$")
    ax.set_ylabel("$2\\,\\mathrm{Vol}_7 e^{3Hy}\\rho / E_{KS}$ (units of $m$)")
    ax.set_title("The energy spreads toward the tip along the history")
    ax.legend()
    save_figure(fig, "energy_spreading",
                "The energy per unit $y$ divided by the total energy, "
                "$2\\,\\mathrm{Vol}_7 e^{3Hy}\\rho(y)/E_{KS}$ (vertical axis, area 1), "
                "of $N = 592$ without interaction at the five slices $a_{4,0} = 0$ to "
                "$2$ (light to dark blue), against $y$ (horizontal axis). Each curve is "
                "the normalised square $2f\\,e^{2fy}/(1 - e^{-6f})$ of the fold-band "
                "orbital, with $f = e^{-a_{4,0}/3}$: the energy sits near the fold and "
                "spreads toward the tip as the hidden direction shrinks.")
    report("largest deviation from 2fM e^{2fMy}/(1 - e^{-2fML}), relative",
           f"{worst_shape:.1e}")
    report("mean position <y> of the energy at the five slices",
           ", ".join(f"{m:.4f}" for m in means))
    check(worst_shape < 1e-6 and all(means[i + 1] < means[i] for i in range(4)),
          "the energy follows e^{2fMy} and moves toward the tip from slice to slice")
    '''),
    md(r"""
    ## 12. The interaction terms

    With interaction the energy density $e_{int}$ enters every component: it is
    subtracted in $\rho$ and added to $p_3$, $p_0$ and, alone, forms $p_t$. The next
    cell uses the strongly interacting state $N = 592$, $+\lambda_2$, $a_{4,0} = 2$: it
    draws $e_{int}$ and its two parts $\tfrac{15}{32}\lambda S^2$ and
    $-\tfrac{1}{32}\lambda n^2$ (computed here from the profile columns $S$ and $n$) and
    checks that the column $e_{int}$ of the profile is this sum and that $p_t = e_{int}$
    exactly. Finally it reads, among the 60 interacting ground states of the committed
    table `ground/emt-integrals.csv`, the sign of the integrated extra-time pressure
    $P_t = 2\,\mathrm{Vol}_7\int e^{3Hy}p_t\,dy$: the exchange term $-\tfrac{1}{32}
    \lambda n^2$ dominates, so $P_t$ has the sign of $-\lambda$, and the deflation of the
    extra times takes energy from a repulsive gas and gives energy to an attractive one.
    """),
    code(r'''
    hartree = LAMBDA2_592 * 15.0 / 32.0 * sp["S"] ** 2  # (15/32) lambda S^2
    exchange = -LAMBDA2_592 / 32.0 * sp["n"] ** 2  # -(1/32) lambda n^2
    fig, ax = plt.subplots()
    ax.plot(sp["y"], sp["e_int"], color=PALETTE[0], lw=3.0, label="$e_{int} = p_t$")
    ax.plot(sp["y"], hartree, color=PALETTE[1], lw=1.5, ls="--",
            label="$\\frac{15}{32}\\lambda S^2$")
    ax.plot(sp["y"], exchange, color=PALETTE[2], lw=1.5, ls="--",
            label="$-\\frac{1}{32}\\lambda n^2$")
    ax.set_yscale("symlog", linthresh=1e-5)
    ax.set_xlabel("hidden coordinate $y$")
    ax.set_ylabel("proper energy density (units of $m^8$)")
    ax.set_title("Interaction energy density, $N = 592$, $+\\lambda_2$, $a_{4,0} = 2$")
    ax.legend()
    save_figure(fig, "interaction_terms",
                "The interaction energy density $e_{int}$, which is also the extra-time "
                "pressure $p_t$ (solid), and its two parts, the positive term "
                "$\\frac{15}{32}\\lambda S^2$ and the negative term "
                "$-\\frac{1}{32}\\lambda n^2$ (dashed), for $N = 592$ with the "
                "repulsive coupling $+\\lambda_2$ at $a_{4,0} = 2$ (vertical axis, "
                "symmetric logarithmic, proper units $m^8$; horizontal axis $y$). The "
                "exchange term dominates, so $e_{int} < 0$; the interaction lives near "
                "the tip, where the proper densities are large.")
    sum_error = float(np.max(np.abs(hartree + exchange - sp["e_int"]))) / float(
        np.max(np.abs(sp["e_int"])))
    report("largest |e_int - (15/32 lambda S^2 - 1/32 lambda n^2)| / max|e_int|",
           f"{sum_error:.1e}")
    check(sum_error < 1e-12 and bool(np.all(sp["p_t"] == sp["e_int"])),
          "e_int = lambda (15/32 S^2 - 1/32 n^2) and p_t = e_int")
    signs = [(float(row["lambda"]), float(row["int_p_t"])) for key, row in emt_rows.items()
             if "_lam0_" not in key]  # the 60 interacting ground states
    opposite = sum(1 for lam, value in signs if lam * value < 0.0)
    report("interacting states / states with P_t of the sign of -lambda",
           f"{len(signs)} / {opposite}")
    check(len(signs) == 60 and opposite == 60,
          "the integrated extra-time pressure has the sign of -lambda in all 60 states",
          record=f"{EMT_TABLE}, column int_p_t")
    '''),
    md(r"""
    ## 13. Why this tensor cannot drive the history

    The field equations for $a_4$ and $b_4$ (the Einstein-Lovelock equations of the
    author's corrected metric) accept a source only under conditions (Revision record
    Revision/field_equations_a4/reports/ks-source-conditions.json, key `conditions`):

    - (C1) every component of the source is independent of $x_0$, that is, of $y$;
    - (C2) $p_0 = p_t$ (the hidden and the extra-time components of every left-hand
      side are equal);
    - (C3) no off-diagonal component $T^{x_4}{}_{x_0}$ (the Kohn-Sham eigen-orbitals
      satisfy it);
    - (C4) on the history $a_4 = Hx_4$, $b_4 = e^{(4/3)Hx_4}$ with the author's weights,
      exactly the source that the history needs, an $x_0$-independent tensor with
      $p_0 = p_t$ whose energy density changes sign along the history.

    The next cell tests C1 and C2 on the 75 committed profiles and on this notebook's
    two states, and compares the free gas with the source of C4: it computes
    $(\max\rho - \min\rho)/\max|T|$ and $\max_y|p_0 - p_t|/\max|T|$ for every profile
    ($\max|T|$ is the largest of $|\rho|$, $|p_3|$, $|p_t|$, $|p_0|$ over $y$) and
    reproduces the smallest and largest values that the record prints (6 significant
    digits). C1 fails for every nonzero state; C2 holds for the free gas and fails with
    interaction; the ratios $P_3/E = 1/3$, $P_0 = P_t = 0$ of the free gas are far from
    the ratios the history needs. The Kohn-Sham gas is a test field on a PRESCRIBED
    BACKGROUND, not a source that would produce the deflating history.
    """),
    code(r'''
    import re  # finds the numbers inside the record's text

    SOURCE = "Revision/field_equations_a4/reports/ks-source-conditions.json"
    source = json.loads(repository_file(SOURCE).read_text(encoding="utf-8"))
    details = {item["name"]: item["detail"] for item in source["checks"]}


    def condition_ratios(p):
        """(C1 ratio, C2 ratio) of one profile, or None if its tensor vanishes."""
        scale = max(float(np.max(np.abs(p[c]))) for c in ("rho", "p3", "p_t", "p0"))
        if scale == 0.0:
            return None
        return ((float(np.max(p["rho"])) - float(np.min(p["rho"]))) / scale,
                float(np.max(np.abs(p["p0"] - p["p_t"]))) / scale)


    ratios = {}
    for path in sorted(repository_file(RECORD_PROFILES).glob("*.csv")):
        values = condition_ratios(read_profile(path))
        if values is not None:
            ratios[path.stem] = values
    c1_min = min(ratios, key=lambda k: ratios[k][0])
    free_c2 = max(v[1] for k, v in ratios.items() if "_lam0_" in k)
    lam_c2 = min((k for k in ratios if "_lam0_" not in k), key=lambda k: ratios[k][1])
    mine = {name: condition_ratios(p) for name, p in (("N592_lam0_a10", prof),
                                                       ("N592_lamp2_a20", sp))}
    number = r"(-?[0-9.]+(?:e[-+]?[0-9]+)?)"  # a number as the record prints it
    rec_c1 = re.search(rf"max\|T\| >= {number} \(smallest: (\w+)\)",
                       details["ks_profiles_depend_on_x0"])
    rec_c2 = re.search(rf"largest {number}\).*smallest: {number} at (\w+)\)",
                       details["ks_hidden_pressure_condition"])
    need = re.search(rf"a4,0 = 0 \(kk = 1\): kappa rho = {number}, p3/rho = {number}, "
                     rf"p0/rho = p_t/rho = {number}", details["ks_history_is_a_prescribed_"
                                                              "background"])
    late = re.search(rf"a4,0 = 2 \(kk = [0-9.]+\): kappa rho = {number}",
                     details["ks_history_is_a_prescribed_background"])
    same6 = lambda a, b: abs(a - float(b)) <= 5e-6 * abs(float(b))  # 6 digits
    report("nonzero profiles / with lambda = 0", f"{len(ratios)} / "
           f"{sum(1 for k in ratios if '_lam0_' in k)}")
    report("C1: smallest (max rho - min rho)/max|T| (state)",
           f"{ratios[c1_min][0]:.6g} ({c1_min})")
    report("C2: largest ratio with lambda = 0 / smallest with lambda != 0 (state)",
           f"{free_c2:.4e} / {ratios[lam_c2][1]:.6g} ({lam_c2})")
    report("this notebook's states: C1 and C2 ratios", "; ".join(
        f"{k}: {v[0]:.4f}, {v[1]:.2e}" for k, v in mine.items()))
    report("C4: the history needs at a4,0 = 0 kappa rho, p3/rho, p0/rho = p_t/rho",
           f"{need.group(1)}, {need.group(2)}, {need.group(3)}; kappa rho at 2: "
           f"{late.group(1)}")
    check(same6(ratios[c1_min][0], rec_c1.group(1)) and c1_min == rec_c1.group(2)
          and mine["N592_lam0_a10"][0] > 0.4 and mine["N592_lamp2_a20"][0] > 0.4,
          "C1 fails for every nonzero profile; the record's smallest ratio reproduced",
          record=f"{SOURCE}, check ks_profiles_depend_on_x0")
    check(free_c2 <= 1e-12 and same6(ratios[lam_c2][1], rec_c2.group(2))
          and lam_c2 == rec_c2.group(3) and mine["N592_lamp2_a20"][1] > 0.08,
          "C2 holds for lambda = 0 and fails for lambda != 0; the record reproduced",
          record=f"{SOURCE}, check ks_hidden_pressure_condition")
    check(float(need.group(1)) > 0.0 > float(late.group(1))
          and abs(float(need.group(2)) - 1.0 / 3.0) > 1.0 and free_dev < 1e-12,
          "C4 fails: the free gas has P3/E = 1/3, P0 = P_t = 0, the history needs others",
          record=f"{SOURCE}, check ks_history_is_a_prescribed_background")
    '''),
    md(r"""
    ## 14. The last check

    The last cell checks that every figure file of this notebook exists and prints the
    number of checks that passed.
    """),
    code(r'''
    NAMES = ["proper_emt", "coordinate_emt", "y_conservation", "energy_slopes",
             "integrated_ratios", "energy_spreading", "interaction_terms"]
    missing = [name for number, name in enumerate(NAMES, start=1)
               if not output_file(f"{FIGURE_FOLDER}/15b_{number}_{name}.png").is_file()]
    check(missing == [], "every figure file of this notebook exists")
    all_checks_passed()
    '''),
    md(r"""
    ## 15. What this notebook showed

    - The solver's profiles of the energy density and the three pressures are
      reproduced on this computer, and their integrals give the Kohn-Sham energy
      (COMPUTED).
    - The free fold-band gas has $p_3 = \rho/3$ and $p_0 = p_t = 0$ at every point, the
      pressures of massless particles in 3-space.
    - The conservation law along the hidden direction,
      $(e^{3Hy}p_0)' = 3H e^{3Hy}p_t$, holds point by point and integrated (an exact
      identity, checked numerically with interaction; without interaction both sides
      vanish).
    - Along the deflating history the energy of the gas changes exactly by the work of
      its pressures, $dE/da_4 = -3P_3 + P_t + \tfrac13P_0$: the 3-space pressure takes
      energy from the gas as 3-space inflates, and the extra-time and hidden pressures,
      zero without interaction and of the sign of $-\lambda$ with it, add or remove a
      little as the extra times and the hidden direction shrink. The free energy falls
      exactly like $e^{-a_4}$.
    - The energy sits near the fold and spreads toward the tip as the hidden direction
      shrinks.
    - The history is PRESCRIBED: these components are not an admissible source of the
      equations for $a_4$ and $b_4$ (they depend on $y$, with interaction
      $p_0 \ne p_t$, and the free gas is not the source the history needs; checked here
      on the notebook's own numbers and on the record), and no equation of state seen
      by an observer is claimed here.
    """),
]

if __name__ == "__main__":
    raise SystemExit(run_builder(__file__))
