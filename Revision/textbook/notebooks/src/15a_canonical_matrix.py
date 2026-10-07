#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
"""Builder of Notebook 15a, "Running the Rust Kohn-Sham solver over the canonical matrix"
(textbook "Universes in Pairs", chapter 15).

The notebook Revision/textbook/notebooks/15a_canonical_matrix.ipynb is BUILT from this
file by Revision/textbook/tools/nbkit.py (never edit the .ipynb by hand):

    python Revision/textbook/tools/nbkit.py build \
        Revision/textbook/notebooks/src/15a_canonical_matrix.py --date YYYY-MM-DD
    python Revision/textbook/tools/nbkit.py check \
        Revision/textbook/notebooks/src/15a_canonical_matrix.py

The notebook builds the Revision Kohn-Sham solver (Revision/kohn_sham/solver) with cargo,
runs its subcommand "all" (the canonical matrix of 75 ground states and 135 thermal states)
into the folder Revision/kohn_sham/solver/target/textbook_15a (ignored by git), compares
every result with the committed Revision record Revision/kohn_sham/results and the report
Revision/kohn_sham/reports/ks-rust-solver.json, and draws eight teaching figures.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools"))
from nbkit import code, md, run_builder  # noqa: E402

FIGURES = [
    "15a_1_levels_history",
    "15a_2_gaps_history",
    "15a_3_delta_scf",
    "15a_4_energy_history",
    "15a_5_densities",
    "15a_6_potentials",
    "15a_7_scf_convergence",
    "15a_8_particle_hole",
]

FACTS = {
    "id": "15a",
    "name": "15a_canonical_matrix",
    "title": "Running the Rust Kohn-Sham solver over the canonical matrix",
    "purpose": (
        "It builds the Rust Kohn-Sham solver of the repository with cargo (a full build "
        "of about a minute when the program is missing, a second when it is up to "
        "date), runs it over the whole "
        "canonical matrix (75 ground states and 135 thermal states of the Kohn-Sham gas "
        "of dirac16complex along the deflating history), checks that the new results "
        "agree with the committed Revision record within tolerances fixed in advance, "
        "and draws the Kohn-Sham levels, the gaps, the energies, the densities, the "
        "self-consistent potentials, the convergence of the self-consistent loop and the "
        "particle-hole excitations. "
        "The solver writes its raw output (about 6 MB) into the folder "
        "`Revision/kohn_sham/solver/target/textbook_15a`, which git ignores."
    ),
    "records": [
        ["Revision/kohn_sham/results",
         "the committed canonical matrix (243 result files and the manifest of their "
         "sha256 fingerprints) that the new run must reproduce"],
        ["Revision/kohn_sham/reports/ks-rust-solver.json",
         "the 42 checks of the solver, all PASS"],
        ["Revision/kohn_sham/reports/ks-rust-determinism.json",
         "the tolerances fixed in advance for comparing two runs of the solver"],
        ["Revision/kohn_sham/ks-theory.json",
         "the formulas the solver implements and the brane-band slope c"],
    ],
    "packages": ["numpy", "matplotlib"],
    "needs_rust": [{"manifest": "Revision/kohn_sham/solver/Cargo.toml",
                    "binaries": ["revision_ks_solver"], "build_minutes": 1}],
    "expected_seconds": 240,
    "timeout_seconds": 1800,
    "files_written": ["Revision/textbook/figures/15a.captions.json"]
    + [f"Revision/textbook/figures/{name}.png" for name in FIGURES],
    "final_lines": [
        "PASS every figure file of this notebook exists",
        "ALL 24 CHECKS PASSED (notebook 15a)",
    ],
    "troubleshooting": [
        ["The cell that runs the canonical matrix shows the label with the star for "
         "several minutes",
         "this is normal. The solver computes 210 states and uses up to 22 processor "
         "cores; on a computer with 4 cores it needs about 10 minutes. Wait until the "
         "label shows a number."],
        ["An AssertionError names one of the comparisons with the record",
         "the notebook prints the largest difference just above the error. Differences "
         "far below the tolerance are rounding effects of another computer; a larger "
         "difference means that the solver or its input files were changed. Get the "
         "stored versions back and run the notebook again.",
         ["git checkout -- Revision/kohn_sham"]],
        ["You want the disk space of the solver output back",
         "the folder `Revision/kohn_sham/solver/target/textbook_15a` holds only the raw "
         "output of the last run (ignored by git); delete it at any time, the notebook "
         "writes it again."],
    ],
}

CELLS = [
    md(r"""
    ## 1. What this notebook computes

    This notebook runs the **Rust Kohn-Sham solver** of the repository over its whole
    **canonical matrix**: the Kohn-Sham states of the fermion field dirac16complex in
    the author's primordial gravitational field, for three particle numbers, five
    couplings and five instants of the deflating history (75 ground states), and for
    135 states at three temperatures. Then it

    - checks that the solver reports all 42 of its own checks as PASS;
    - compares every new result with the committed Revision record (the folder
      Revision/kohn_sham/results), number by number, with tolerances that were fixed in
      advance;
    - prints the energies and gaps of the ground states along the history;
    - draws eight figures: the Kohn-Sham levels along the history, the gaps, the
      Delta-SCF excitation energies, the total energies, the densities, the
      self-consistent potentials, the convergence of the self-consistent loop and the
      particle-hole excitations.

    The run takes about two to three minutes on a computer with many processor cores
    (longer on a laptop). Everything it writes outside the folder of the figures goes
    into the Rust build folder `Revision/kohn_sham/solver/target/textbook_15a`, which
    git ignores.
    """),
    md(r"""
    ## 3. The words used in this notebook

    - **Kohn-Sham state**: an approximate state of many identical fermions, built from
      one-particle wave functions (*orbitals*) that each solve a one-particle equation
      in a common *effective potential*; the potential depends on the densities of the
      occupied orbitals, so the equations must be solved *self-consistently*.
    - **Level**: an allowed energy $\varepsilon$ of the one-particle equation. A level is
      **occupied** if particles sit in it ($f = 1$) and **empty** if not ($f = 0$).
    - **Degeneracy** $g$: the number of different orbitals that share one level.
    - **HOMO, LUMO, Kohn-Sham gap**: the highest occupied and the lowest unoccupied
      level, and their difference $\Delta_{KS} = \varepsilon_{LUMO} - \varepsilon_{HOMO}$.
    - **Delta-SCF**: the energy of the first excited state minus the energy of the
      ground state, both computed self-consistently (SCF = self-consistent field).
    - **Slice** $a_{4,0}$: one instant of the history, the value of the metric function
      $a_4$ at that instant. The **history** is $a_4 = A H x_4$ with $A = 1$.
    - **Canonical matrix**: the fixed list of states the solver computes: particle
      numbers $N = 8, 136, 688$; couplings $\lambda = 0, \pm\lambda_1, \pm\lambda_2$;
      slices $a_{4,0} = 0, 0.5, 1, 1.5, 2$; and temperatures $T = 0.01, 0.02, 0.05$
      (in units of the mass $m$) for $\lambda = 0, \pm\lambda_1$.
    - **Proper density**: a number of particles (or an energy) per unit of proper
      7-volume. **Coordinate density**: the same per unit of the coordinate $y$ (it
      contains the volume factor $e^{6Hy}$).
    - **Brane** and **tip**: the two ends $y = 0$ and $y = -L = -3$ of the hidden
      coordinate.
    - **Shell** $n_2$: the 3-space momenta form a lattice $\vec k = \Delta k\,\vec n$
      with $\vec n$ a vector of three whole numbers; a shell collects the $r_3(n_2)$
      vectors with the same $n_2 = |\vec n|^2$, so $|\vec k| = \Delta k \sqrt{n_2}$.
    - **Residual**: in the self-consistent loop, the largest change of the potential
      from one iteration to the next; the loop stops when it is below $10^{-11}$.
    - **Anderson mixing**: a rule that builds the next potential from several earlier
      ones; it converges much faster than simple mixing.
    - **Manifest, sha256**: the solver writes a list (the manifest) of all its files
      with a 64-digit *fingerprint* (sha256) of each; two files with the same
      fingerprint are identical byte for byte.
    - **Tolerance**: the largest difference that a comparison accepts; the tolerances
      used here were fixed in advance in the Revision record.
    """),
    md(r"""
    ## 4. The physical and mathematical situation

    **The field and the metric.** The author's metric has eight coordinates $x_1$ to
    $x_8$. The directions $x_1, x_2, x_3$ are ordinary 3-space, with the scale factor
    $e^{a_4} \sin^{1/6} z$; $x_4$ is the time; $x_5, x_6, x_7$ are the three **extra
    times**, with the scale factor $e^{-a_4} \sin^{1/6} z$, so they **deflate
    exponentially** while $a_4$ grows; $x_8$ is the hidden space direction, with
    $z = 6 H x_8$ between $0$ and $\pi/2$. The Kohn-Sham model uses the hidden
    coordinate $y = \ln(\sin z)/(6H)$, which runs from the tip $y = -L$ (the model cuts
    the space there, with $L = 3$) to the brane $y = 0$ (the end $z = \pi/2$ of the
    patch).

    **The equation the solver solves.** For one 3-momentum $k = |\vec k|$ and one of
    two block types $j = \pm 1$ the 16-component field reduces exactly to a pair of
    real functions $a(y), b(y)$ (an orbital) with

    $$a' = M a - (\kappa k + j(\varepsilon - v))\, b, \qquad
    b' = (j(\varepsilon - v) - \kappa k)\, a - M b,$$

    where the prime is $d/dy$, $\kappa = e^{-Hy - a_{4,0}}$, $M(y) = m + \tfrac{15}{16}
    \lambda S(y)$ is the effective mass and $v(y) = -\tfrac{1}{16} \lambda n(y)$ the
    effective potential, with $n$ and $S$ the proper number and scalar densities of
    the occupied orbitals. The slice $a_{4,0}$ enters only through $\kappa$: along the
    history every 3-momentum is **redshifted**, $k \to k e^{-a_{4,0}}$.

    **Boundary conditions.** At the tip $b(-L) = 0$ (a regular tip, a choice). At the
    brane the Z2 mirror, which is ASSUMED: $b(0) = 0$ (even parity) or $a(0) = 0$ (odd
    parity).

    **Status of the history.** The history $a_4 = A H x_4$ with $A = 1$ is a PRESCRIBED
    BACKGROUND: it is not solved for, and the Kohn-Sham states are not an admissible
    source of the equations for $a_4$ (the Revision record
    Revision/field_equations_a4/reports/ks-source-conditions.json). The states are
    **instantaneous** (adiabatic) states at each slice.

    **Parameters** (units $H = m = 1$): $L = 3$, $\Delta k = 0.25$, $N = 8$ (the eight
    zero modes at $k = 0$), $N = 136$ and $N = 688$ (closed shells of the brane band),
    and per $N$ the couplings $\lambda_1, \lambda_2$ that make the first-order
    potential $0.1\,m$ and $0.3\,m$ (Revision/kohn_sham/results/parameters.json).
    Particles fill the positive branch and the zero modes, a CONVENTION whose
    justification is OPEN. $N$ counts the particles of the doubled system (universe and
    Z2 image); one patch holds $N/2$.

    All numbers of this notebook are COMPUTED by the solver; the notebook checks that
    they agree with the committed record.
    """),
    md(r"""
    ## 5. Building the solver

    The next cell imports the packages of this notebook and builds the Rust program
    `revision_ks_solver` with cargo (the helper `rust_program` of the set-up cell runs
    `cargo build --release` for the crate; the first build takes about a minute, later
    builds a second). `PALETTE` holds the colours of the figures: eight distinct hues in
    a fixed order, and five shades of blue for the five slices of the history (light
    for the earliest, dark for the latest).
    """),
    code(r'''
    import csv  # reads the tables (CSV files) that the solver writes
    import math  # exp, sqrt and pi for single numbers

    import numpy as np  # arrays of numbers

    SOLVER_MANIFEST = "Revision/kohn_sham/solver/Cargo.toml"  # the crate of the solver
    program = rust_program(SOLVER_MANIFEST, "revision_ks_solver")  # build it, get its path

    PALETTE = ["#2a78d6", "#eb6834", "#1baf7a", "#eda100", "#e87ba4", "#008300",
               "#4a3aa7", "#e34948"]  # blue, orange, aqua, yellow, magenta, green, ...
    SLICE_SHADES = ["#86b6ef", "#5598e7", "#2a78d6", "#1c5cab", "#104281"]  # light->dark
    SLICES = [0.0, 0.5, 1.0, 1.5, 2.0]  # the five slices a4,0 of the history
    say("Packages imported; colours defined.")
    '''),
    md(r"""
    ## 6. Running the canonical matrix

    The next cell runs `revision_ks_solver all`. The option `--root` tells the program
    where the repository is (it reads the theory file `Revision/kohn_sham/ks-theory.json`,
    the gamma matrices `Revision/algebra/gammas.json` and one fixture file from there);
    `--out` and `--report` name the folder of the results and the file of the check
    report. Both go into the folder `textbook_15a` inside the Rust build folder `target`,
    so the committed record is never touched. A folder left over from an interrupted
    run is removed first (the solver refuses to write into a folder without its
    manifest). The solver prints one line per check on its error stream and `SUCCESS` as
    its last line on its output stream; the cell counts those lines. This cell takes two
    to three minutes (up to ten on a laptop).
    """),
    code(r'''
    RUN_FOLDER = REPO / "Revision/kohn_sham/solver/target/textbook_15a"  # git ignores it
    NEW_RESULTS = RUN_FOLDER / "results"  # the new canonical matrix
    NEW_REPORT = RUN_FOLDER / "ks-rust-solver.json"  # the new check report
    RUN_FOLDER.mkdir(parents=True, exist_ok=True)
    if NEW_RESULTS.exists() and not (NEW_RESULTS / "manifest.json").exists():
        shutil.rmtree(NEW_RESULTS)  # remains of an interrupted run
    completed = subprocess.run(
        [str(program), "all", "--root", str(REPO), "--out", str(NEW_RESULTS),
         "--report", str(NEW_REPORT)],
        capture_output=True, text=True, encoding="utf-8", errors="replace")
    stdout_lines = completed.stdout.strip().split("\n")  # what it printed on stdout
    stderr_lines = completed.stderr.split("\n")  # its check lines and timings
    pass_count = sum(1 for line in stderr_lines if line.startswith("PASS - "))
    fail_count = sum(1 for line in stderr_lines if line.startswith("FAIL - "))
    say(f"exit code {completed.returncode}, last line {stdout_lines[-1]!r}, "
        f"{pass_count} PASS lines, {fail_count} FAIL lines")
    check(completed.returncode == 0 and stdout_lines[-1] == "SUCCESS" and fail_count == 0,
          "the solver ran the whole canonical matrix and reported SUCCESS")
    '''),
    md(r"""
    ## 7. The solver's own check report

    The solver writes its checks into a JSON report. The next cell reads the new report
    and the committed one, prints how many checks of each group there are (the group
    is the first word of the check name, for example `ground` or `thermo`), and checks
    that all 42 pass and that the new report lists the same checks, in the same order,
    as the committed report. Whether the two reports are identical byte for byte is
    printed as a RESULT line: on the computer that built this book they are; on another
    computer the last digits of some reported deviations may differ.
    """),
    code(r'''
    RECORD_REPORT = "Revision/kohn_sham/reports/ks-rust-solver.json"
    new_report = json.loads(NEW_REPORT.read_text(encoding="utf-8"))
    old_report = json.loads(repository_file(RECORD_REPORT).read_text(encoding="utf-8"))
    groups = {}  # first word of a check name -> [number of checks, number of PASS]
    for item in new_report["checks"]:
        group = item["name"].split("_")[0]
        groups.setdefault(group, [0, 0])
        groups[group][0] += 1
        groups[group][1] += item["verdict"] == "PASS"  # True counts as 1
    for group, (count, passed) in groups.items():
        say(f"  {group:10} {count:2d} checks, {passed:2d} PASS")
    new_names = [item["name"] for item in new_report["checks"]]
    old_names = [item["name"] for item in old_report["checks"]]
    check(new_report["summary"] == {"checks": 42, "pass": 42, "fail": 0},
          "the new report holds 42 checks, all PASS",
          record=f"{RECORD_REPORT}, summary 42 of 42 PASS")
    check(new_names == old_names, "the new report has the same checks as the record")
    report("new report byte-identical to the record",
           NEW_REPORT.read_bytes() == repository_file(RECORD_REPORT).read_bytes())
    '''),
    md(r"""
    ## 8. Comparing every result file with the record

    The solver's manifest lists every result file with its sha256 fingerprint. The next
    cell checks that the new run wrote exactly the same set of files as the record and
    counts how many have the same fingerprint (byte-identical files).
    """),
    code(r'''
    RECORD_RESULTS = "Revision/kohn_sham/results"


    def manifest_of(folder):
        """{file path: sha256} of the manifest.json in folder."""
        data = json.loads((folder / "manifest.json").read_text(encoding="utf-8"))
        return {entry["path"]: entry["sha256"] for entry in data["files"]}


    old_manifest = manifest_of(repository_file(RECORD_RESULTS))
    new_manifest = manifest_of(NEW_RESULTS)
    check(sorted(old_manifest) == sorted(new_manifest),
          f"the new run wrote the same {len(old_manifest)} result files as the record",
          record=f"{RECORD_RESULTS}/manifest.json")
    same = sum(1 for path in old_manifest if new_manifest[path] == old_manifest[path])
    report("result files byte-identical to the record", f"{same} of {len(old_manifest)}")
    '''),
    md(r"""
    Byte identity can fail on another computer only through the last digit of a number
    (operating systems compute $e^x$ and $\ln x$ with slightly different rounding). The
    meaningful comparison is therefore numerical. The next cell reads four tables of the
    new run and of the record and computes the largest difference of their key columns:
    the energies $E_{KS}$ of the 75 ground states (relative to $\max(|E|, 1)$), their
    HOMO, LUMO and gap (absolute, in units of $m$), the Delta-SCF energies, the
    chemical potential $\mu$, energy, entropy and free energy of the 135 thermal states,
    and the adiabaticity measure $Q_{max}$. The tolerances are those fixed in advance in
    Revision/kohn_sham/reports/ks-rust-determinism.json: $10^{-8}$ for eigenvalues,
    energies and thermodynamics, $10^{-6}$ for derived quantities.
    """),
    code(r'''
    def read_table(folder, name):
        """The rows of the CSV table folder/name as a dictionary id -> row."""
        with open(folder / name, newline="", encoding="utf-8") as handle:
            return {row["id"]: row for row in csv.DictReader(handle)}


    def worst(table, columns, relative):
        """Largest difference between the new run and the record in these columns."""
        new = read_table(NEW_RESULTS, table)
        old = read_table(repository_file(RECORD_RESULTS), table)
        assert sorted(new) == sorted(old), f"{table}: the state lists differ"
        largest = 0.0
        for key in old:
            for column in columns:
                a, b = float(new[key][column]), float(old[key][column])
                scale = max(abs(b), 1.0) if relative else 1.0
                largest = max(largest, abs(a - b) / scale)
        return largest


    COMPARISONS = [  # (table, columns, relative?, tolerance, what)
        ("ground/summary.csv", ["E_KS"], True, 1e-8, "ground-state energies"),
        ("ground/summary.csv", ["HOMO", "LUMO", "KS_gap"], False, 1e-8,
         "HOMO, LUMO and gaps"),
        ("excited/summary.csv", ["delta_SCF"], False, 1e-8, "Delta-SCF energies"),
        ("thermo/thermodynamics.csv", ["mu", "E", "entropy", "F"], True, 1e-8,
         "thermodynamics"),
        ("adiabatic/adiabaticity.csv", ["Q_max"], True, 1e-6, "adiabaticity Q_max"),
    ]
    for table, columns, relative, tolerance, what in COMPARISONS:
        largest = worst(table, columns, relative)
        report(f"largest difference, {what}", f"{largest:.1e}")
        check(largest <= tolerance, f"{what} agree with the record within {tolerance:.0e}",
              record=f"{RECORD_RESULTS}/{table}")
    '''),
    md(r"""
    ## 9. The ground states along the history

    From here on the notebook reads the NEW results (which equal the record). The next
    cell prints, for the three particle numbers without interaction ($\lambda = 0$),
    the energy $E_{KS}$, the HOMO, the LUMO and the gap at the five slices.
    """),
    code(r'''
    ground = read_table(NEW_RESULTS, "ground/summary.csv")  # the 75 ground states
    excited = read_table(NEW_RESULTS, "excited/summary.csv")  # their Delta-SCF


    def state_id(n, tag, a4):
        """The solver's name of a state, e.g. N136_lam0_a10 for N = 136, a4,0 = 1."""
        return f"N{n}_{tag}_a{round(10 * a4):02d}"


    say("   N  a4,0        E_KS        HOMO        LUMO     KS gap")
    for n in (8, 136, 688):
        for a4 in SLICES:
            row = ground[state_id(n, "lam0", a4)]
            say(f"{n:4d}  {a4:4.1f}  {float(row['E_KS']):10.5f}  {float(row['HOMO']):10.6f}"
                f"  {float(row['LUMO']):10.6f}  {float(row['KS_gap']):9.6f}")
    report("KS gap of N = 8 at a4,0 = 0, 1, 2", ", ".join(
        f"{float(ground[state_id(8, 'lam0', a)]['KS_gap']):.7f}" for a in (0, 1, 2)))
    '''),
    md(r"""
    ## 10. The Kohn-Sham levels along the history

    The next cell reads, for $N = 136$ and $\lambda = 0$, the level tables of the five
    slices. Each level has a **key**: its shell $n_2$, block type $j$, parity and
    Pruefer label $l$ (the label numbers the levels of one sector in the order of their
    energies, and a level keeps its label when the potentials change continuously, so
    the label identifies the same level at every slice). The figure follows each key across
    the slices: the **brane band** (the lowest even level of $j = +1$ in each shell
    $n_2 \ge 1$) comes down as the history proceeds, while the levels at $k = 0$ do not
    move at all, because $a_{4,0}$ enters only through $\kappa k$. The dashed line is
    the small-$k$ law $\varepsilon \approx c\, k\, e^{-a_{4,0}}$ for the first shell
    ($k = 0.25$), with the slope $c = 1.9051482536$ of Revision/kohn_sham/ks-theory.json.

    The checks: every $k = 0$ level is the same at all five slices (to $10^{-12}$), and
    every brane-band level present at all slices decreases strictly along the history.
    """),
    code(r'''
    def read_levels(n, tag, a4):
        """{key: (eps, f)} of one state; key = (n2, j, parity, label)."""
        path = NEW_RESULTS / "ground/levels" / f"{state_id(n, tag, a4)}.csv"
        with open(path, newline="", encoding="utf-8") as handle:
            return {(int(r["n2"]), int(r["j"]), r["parity"], int(r["label"])):
                    (float(r["eps"]), float(r["f"])) for r in csv.DictReader(handle)}


    levels = [read_levels(136, "lam0", a4) for a4 in SLICES]  # one dictionary per slice
    THEORY = json.loads(repository_file("Revision/kohn_sham/ks-theory.json").read_text(
        encoding="utf-8"))  # the theory file of the solver
    C_SLOPE = float(THEORY["checksNumeric"]["braneBandSlope_M1_H1_L3_a0"])  # c
    fig, ax = plt.subplots(figsize=(7.5, 5.0))
    all_keys = sorted(set().union(*levels))
    for key in all_keys:
        points = [(a4, lv[key]) for a4, lv in zip(SLICES, levels) if key in lv]
        xs = [p[0] for p in points]
        es = [p[1][0] for p in points]
        if min(es) > 1.6:
            continue  # only the part of the spectrum near the Fermi level
        band = key[1] == 1 and key[2] == "even" and key[3] == 0 and key[0] >= 1
        colour = PALETTE[0] if band else ("black" if key[0] == 0 else "0.6")
        ax.plot(xs, es, "-", color=colour, lw=1.0, alpha=0.8)
        for x, (e, f) in points:
            ax.plot([x], [e], "o", ms=5, color=colour,
                    markerfacecolor=colour if f > 0.5 else "white")
    a_fine = np.linspace(0.0, 2.0, 101)
    ax.plot(a_fine, C_SLOPE * 0.25 * np.exp(-a_fine), "--", color=PALETTE[1], lw=1.5,
            label="$c\\,k\\,e^{-a_{4,0}}$ for $k = 0.25$")
    ax.plot([], [], "o-", color=PALETTE[0], label="brane band ($j=+1$, even, $l=0$)")
    ax.plot([], [], "o-", color="black", label="levels at $k = 0$")
    ax.plot([], [], "o-", color="0.6", label="other levels")
    ax.plot([], [], "o", color="0.3", markerfacecolor="white", label="open: empty")
    ax.set_ylim(-0.05, 1.6)
    ax.set_xlabel("slice $a_{4,0}$ of the history")
    ax.set_ylabel("level $\\varepsilon$ (units of $m$)")
    ax.set_title("Kohn-Sham levels of $N = 136$, $\\lambda = 0$, along the history")
    ax.legend(fontsize=8, loc="center right")
    save_figure(fig, "levels_history",
                "Kohn-Sham levels $\\varepsilon$ (vertical axis, units of $m$) of the "
                "state $N = 136$, $\\lambda = 0$ at the five slices $a_{4,0} = 0$ to $2$ "
                "(horizontal axis), each level followed by its key; filled dots are "
                "occupied, open dots empty. The brane band (blue) comes down as the "
                "3-momenta redshift like $k e^{-a_{4,0}}$, the dashed curve is the "
                "small-$k$ law for the first shell, and the levels at $k = 0$ (black) do "
                "not move.")
    k0_keys = [key for key in levels[0] if key[0] == 0]
    k0_spread = max(abs(lv[key][0] - levels[0][key][0]) for lv in levels for key in k0_keys)
    band_keys = [key for key in all_keys if all(key in lv for lv in levels)
                 and key[1] == 1 and key[2] == "even" and key[3] == 0 and key[0] >= 1]
    decreasing = all(levels[i + 1][key][0] < levels[i][key][0]
                     for key in band_keys for i in range(4))
    report("number of brane-band levels followed through all five slices", len(band_keys))
    check(k0_spread <= 1e-12, "the k = 0 levels are the same at every slice")
    check(decreasing, "every brane-band level decreases strictly along the history")
    '''),
    md(r"""
    ## 11. The gaps along the history

    The next cell draws the Kohn-Sham gap of $N = 8$, $136$ and $688$ (without
    interaction) against the slice on a logarithmic vertical axis, together with dashed
    lines proportional to $e^{-a_{4,0}}$ through the first point of each curve. Every gap
    shrinks along the history, somewhat more slowly than $e^{-a_{4,0}}$: the gap is the
    distance between two brane-band levels (for $N = 688$ at $a_{4,0} = 0$ between a band
    level and the bulk level at $k = 0$), and the band levels approach the straight line
    $c\,k\,e^{-a_{4,0}}$ only when the redshifted momenta $k e^{-a_{4,0}}$ are small.
    Without interaction the levels do not change when one particle is
    moved, so the Delta-SCF energy must equal the gap exactly; the solver recorded this
    as its check `excited_delta_scf_free_equals_gap`.
    """),
    code(r'''
    fig, ax = plt.subplots()
    for colour, n in zip(PALETTE, (8, 136, 688)):
        gaps = [float(ground[state_id(n, "lam0", a4)]["KS_gap"]) for a4 in SLICES]
        ax.plot(SLICES, gaps, "o-", color=colour, lw=1.5, label=f"$N = {n}$")
        ax.plot(a_fine, gaps[0] * np.exp(-a_fine), "--", color=colour, lw=1.0)
    ax.set_yscale("log")
    ax.set_xlabel("slice $a_{4,0}$ of the history")
    ax.set_ylabel("Kohn-Sham gap $\\Delta_{KS}$ (units of $m$)")
    ax.set_title("The gap closes along the history (dashed: $\\propto e^{-a_{4,0}}$)")
    ax.legend()
    save_figure(fig, "gaps_history",
                "Kohn-Sham gap $\\Delta_{KS}$ (vertical axis, logarithmic, units of $m$) "
                "of the states $N = 8$, $136$ and $688$ without interaction at the five "
                "slices $a_{4,0}$ (horizontal axis). Dashed lines fall like "
                "$e^{-a_{4,0}}$ from the first point of each curve: every gap shrinks "
                "along the history, somewhat more slowly than this, because the levels "
                "that bound it belong to the brane band, whose momenta redshift like "
                "$k e^{-a_{4,0}}$ but whose energy is linear in the momentum only for "
                "small momenta.")
    free_dscf = max(abs(float(excited[state_id(n, "lam0", a)]["delta_SCF_minus_gap"]))
                    for n in (8, 136, 688) for a in SLICES)
    report("largest |Delta-SCF - gap| without interaction", f"{free_dscf:.1e}")
    check(free_dscf <= 1e-10, "Delta-SCF equals the gap without interaction",
          record=f"{RECORD_REPORT}, check excited_delta_scf_free_equals_gap")
    shrinking = all(float(ground[state_id(n, "lam0", SLICES[i + 1])]["KS_gap"])
                    < float(ground[state_id(n, "lam0", SLICES[i])]["KS_gap"])
                    for n in (8, 136, 688) for i in range(4))
    check(shrinking, "every gap shrinks from slice to slice")
    '''),
    md(r"""
    With interaction the orbitals relax when a particle is moved, and Delta-SCF differs
    from the gap. The next cell draws the difference $\Delta_{SCF} - \Delta_{KS}$ for
    the four couplings $\pm\lambda_1$, $\pm\lambda_2$ and the three particle numbers. The
    vertical axis is *symmetric logarithmic*: logarithmic for large positive and
    negative values and linear near zero (between $-10^{-9}$ and $10^{-9}$), so values of
    both signs and very different sizes fit on one axis.
    """),
    code(r'''
    fig, axes = plt.subplots(1, 3, figsize=(10.0, 3.8), sharey=True,
                             layout="constrained")
    for ax, n in zip(axes, (8, 136, 688)):
        for colour, tag, label in zip(PALETTE, ("lamp1", "lamm1", "lamp2", "lamm2"),
                                      ("$+\\lambda_1$", "$-\\lambda_1$", "$+\\lambda_2$",
                                       "$-\\lambda_2$")):
            diff = [float(excited[state_id(n, tag, a)]["delta_SCF_minus_gap"])
                    for a in SLICES]
            ax.plot(SLICES, diff, "o-", color=colour, lw=1.5, label=label)
        ax.set_yscale("symlog", linthresh=1e-9)
        ax.set_title(f"$N = {n}$")
        ax.set_xlabel("slice $a_{4,0}$")
    axes[0].set_ylabel("$\\Delta_{SCF} - \\Delta_{KS}$ (units of $m$)")
    axes[0].legend(fontsize=8)
    save_figure(fig, "delta_scf",
                "Orbital relaxation: the Delta-SCF excitation energy minus the Kohn-Sham "
                "gap (vertical axis, symmetric logarithmic, units of $m$) for the "
                "couplings $\\pm\\lambda_1$ and $\\pm\\lambda_2$ at the five slices "
                "(horizontal axis), for $N = 8$, $136$ and $688$. It is small everywhere; "
                "it is largest, about $5 \\times 10^{-4}$, for $N = 688$ at "
                "$a_{4,0} = 0$, where the lowest empty level is a bulk level at $k = 0$.")
    largest_relax = max(abs(float(excited[i]["delta_SCF_minus_gap"])) for i in excited)
    report("largest |Delta-SCF - gap| over the 75 states", f"{largest_relax:.3e}")
    check(largest_relax < 1e-3, "the orbital relaxation is below 0.001 m in every state")
    '''),
    md(r"""
    ## 12. The total energy along the history

    The next cell draws $E_{KS}$ of $N = 136$ and $688$ without interaction (left) and
    the change of $E_{KS}$ caused by the interaction, $E_{KS}(\lambda) - E_{KS}(0)$, for
    $N = 136$ (right). The energy of the gas falls along the history because the brane
    band redshifts. A repulsive coupling ($\lambda > 0$) raises the energy and an
    attractive one lowers it, for $N = 136$ and $N = 688$; the check confirms this order
    at every slice. (For $N = 8$ the order is reversed: the eight zero modes have no
    scalar density $S$, so to first order in $\lambda$ the only interaction energy is
    the exchange term $-\tfrac{1}{32}\lambda n^2$, which is negative for $\lambda > 0$.)
    """),
    code(r'''
    fig, (left, right) = plt.subplots(1, 2, figsize=(10.0, 4.0), layout="constrained")
    for colour, n in zip(PALETTE, (136, 688)):
        energies = [float(ground[state_id(n, "lam0", a)]["E_KS"]) for a in SLICES]
        left.plot(SLICES, energies, "o-", color=colour, lw=1.5, label=f"$N = {n}$")
    left.set_yscale("log")
    left.set_xlabel("slice $a_{4,0}$")
    left.set_ylabel("$E_{KS}$ (units of $m$)")
    left.set_title("Energy without interaction")
    left.legend()
    tags = ("lamp2", "lamp1", "lamm1", "lamm2")
    labels = ("$+\\lambda_2$", "$+\\lambda_1$", "$-\\lambda_1$", "$-\\lambda_2$")
    for colour, tag, label in zip(PALETTE, tags, labels):
        shift = [float(ground[state_id(136, tag, a)]["E_KS"])
                 - float(ground[state_id(136, "lam0", a)]["E_KS"]) for a in SLICES]
        right.plot(SLICES, shift, "o-", color=colour, lw=1.5, label=label)
    right.axhline(0.0, color="0.4", lw=0.8)
    right.set_xlabel("slice $a_{4,0}$")
    right.set_ylabel("$E_{KS}(\\lambda) - E_{KS}(0)$ (units of $m$)")
    right.set_title("Interaction energy shift, $N = 136$")
    right.legend(fontsize=8)
    save_figure(fig, "energy_history",
                "Left: the Kohn-Sham energy $E_{KS}$ (vertical axis, logarithmic, units "
                "of $m$) of $N = 136$ and $N = 688$ without interaction at the five "
                "slices; it falls along the history as the brane band redshifts. Right: "
                "the energy shift caused by the couplings $\\pm\\lambda_1$ and "
                "$\\pm\\lambda_2$ for $N = 136$ (vertical axis, units of $m$): repulsion "
                "raises and attraction lowers the energy, by at most $0.032\\,m$ out of "
                "$12$ to $80\\,m$.")
    ordered = all(
        float(ground[state_id(n, "lamp2", a)]["E_KS"])
        > float(ground[state_id(n, "lamp1", a)]["E_KS"])
        > float(ground[state_id(n, "lam0", a)]["E_KS"])
        > float(ground[state_id(n, "lamm1", a)]["E_KS"])
        > float(ground[state_id(n, "lamm2", a)]["E_KS"])
        for n in (136, 688) for a in SLICES)
    check(ordered, "E(+lambda2) > E(+lambda1) > E(0) > E(-lambda1) > E(-lambda2), "
                   "N = 136 and 688")
    falling = all(float(ground[state_id(n, "lam0", SLICES[i + 1])]["E_KS"])
                  < float(ground[state_id(n, "lam0", SLICES[i])]["E_KS"])
                  for n in (136, 688) for i in range(4))
    check(falling, "the energy of N = 136 and 688 falls from slice to slice")
    '''),
    md(r"""
    ## 13. Where the particles are: the densities

    The solver writes for every ground state the **profiles**: the densities and the
    energy-momentum tensor at the 151 points $y = -3, -2.98, \dots, 0$. The next cell
    reads the proper number density $n(y)$ of $N = 136$ without interaction at the
    slices $0$, $1$ and $2$ and draws it (left, logarithmic) together with the number of
    particles per unit of $y$, $2\,\mathrm{Vol}_7\, e^{6Hy} n(y)$ (right), where
    $\mathrm{Vol}_7 = (2\pi/\Delta k)^3$ is the proper 7-volume of the box per unit of
    $e^{6Hy}$. The proper density is largest at the tip (the proper volume
    $e^{6Hy}$ is tiny there), but the particles themselves sit near the brane; along the
    history they spread toward the tip.

    The integral of the right-hand curve over $y$ must be $N = 136$. It is computed with
    **Simpson's rule** on the 151 points (step $h = 0.02$): $\int f\,dy \approx
    \tfrac{h}{3}(f_0 + 4 f_1 + 2 f_2 + 4 f_3 + \dots + 4 f_{149} + f_{150})$.
    """),
    code(r'''
    VOL7 = (2.0 * math.pi / 0.25) ** 3  # proper 7-volume per unit e^{6Hy} (v_t = 1)


    def read_profile(n, tag, a4):
        """The profile table of one state as a dictionary column -> numpy array."""
        path = NEW_RESULTS / "ground/profiles" / f"{state_id(n, tag, a4)}.csv"
        data = np.genfromtxt(path, delimiter=",", names=True)
        return {name: data[name] for name in data.dtype.names}


    def simpson(values, step):
        """Simpson's rule for equally spaced values (an odd number of points)."""
        weights = np.full(len(values), 2.0)
        weights[1::2] = 4.0
        weights[0] = weights[-1] = 1.0
        return step / 3.0 * float(np.sum(weights * values))


    fig, (left, right) = plt.subplots(1, 2, figsize=(10.0, 4.0), layout="constrained")
    counts = []
    for shade, a4 in zip((SLICE_SHADES[0], SLICE_SHADES[2], SLICE_SHADES[4]), (0, 1, 2)):
        prof = read_profile(136, "lam0", a4)
        y = prof["y"]
        per_y = 2.0 * VOL7 * np.exp(6.0 * y) * prof["n"]  # particles per unit y
        counts.append(simpson(per_y, y[1] - y[0]))
        left.plot(y, prof["n"], color=shade, lw=1.8, label=f"$a_{{4,0}} = {a4}$")
        right.plot(y, per_y, color=shade, lw=1.8, label=f"$a_{{4,0}} = {a4}$")
    left.set_yscale("log")
    left.set_xlabel("hidden coordinate $y$ (tip at $-3$, brane at $0$)")
    left.set_ylabel("proper density $n(y)$")
    left.set_title("Proper number density")
    right.set_xlabel("hidden coordinate $y$")
    right.set_ylabel("particles per unit $y$")
    right.set_title("$2\\,\\mathrm{Vol}_7\\, e^{6Hy} n(y)$, area $= N$")
    right.legend()
    save_figure(fig, "densities",
                "Left: the proper number density $n(y)$ (vertical axis, logarithmic, "
                "particles per unit proper 7-volume) of $N = 136$ without interaction "
                "at $a_{4,0} = 0$, $1$, $2$ against the hidden coordinate $y$ (horizontal "
                "axis). Right: the particles per unit $y$, "
                "$2\\,\\mathrm{Vol}_7 e^{6Hy} n(y)$, whose area is $N = 136$. The particles "
                "sit near the brane $y = 0$ and spread toward the tip along the history; "
                "the proper density is largest at the tip, where the proper volume is "
                "small.")
    report("particle number from the profiles at a4,0 = 0, 1, 2",
           ", ".join(f"{c:.6f}" for c in counts))
    check(max(abs(c - 136.0) for c in counts) < 1e-5,
          "Simpson's rule on the profiles gives N = 136 at every slice",
          record=f"{RECORD_REPORT}, check ground_N_conservation")
    '''),
    md(r"""
    ## 14. The self-consistent potentials

    With interaction the effective mass $M(y) = m + \tfrac{15}{16}\lambda S(y)$ and the
    potential $v(y) = -\tfrac{1}{16}\lambda n(y)$ differ from $m$ and $0$. The next cell
    draws $M - m$ and $v$ for $N = 136$ with the repulsive coupling $+\lambda_2$ at the
    five slices. Both are largest in the tip region and become much larger along the
    history (the largest $|v|$ grows at every slice; the largest $|M - m|$ grows up to
    $a_{4,0} = 1.5$ and is a little smaller at $a_{4,0} = 2$), because the redshifted
    brane-band orbitals spread toward the tip, where the proper densities are large.
    This is why the couplings were calibrated over the whole history (so that the
    first-order potential stays below $0.3\,m$ at every slice).
    The check compares, for each slice, the largest $|M - m|$ on the 151 profile points
    with the value `max_abs_Meff_minus_m` that the solver recorded on its fine grid of
    1801 points (every profile point is also a point of the fine grid): the profile
    value cannot be larger, and since the maximum lies between two profile points it
    is smaller by a little, at most 0.2 percent.
    """),
    code(r'''
    fig, (left, right) = plt.subplots(1, 2, figsize=(10.0, 4.0), layout="constrained")
    ratios = []  # profile maximum / recorded maximum, one per slice
    for shade, a4 in zip(SLICE_SHADES, SLICES):
        prof = read_profile(136, "lamp2", a4)
        left.plot(prof["y"], prof["M_eff"] - 1.0, color=shade, lw=1.8,
                  label=f"$a_{{4,0}} = {a4}$")
        right.plot(prof["y"], prof["v_v"], color=shade, lw=1.8)
        recorded = float(ground[state_id(136, "lamp2", a4)]["max_abs_Meff_minus_m"])
        ratios.append(float(np.max(np.abs(prof["M_eff"] - 1.0))) / recorded)
    left.set_xlabel("hidden coordinate $y$")
    left.set_ylabel("$M(y) - m$ (units of $m$)")
    left.set_title("Mass shift, $N = 136$, $+\\lambda_2$")
    left.legend(fontsize=8)
    right.set_xlabel("hidden coordinate $y$")
    right.set_ylabel("$v(y)$ (units of $m$)")
    right.set_title("Exchange potential, $N = 136$, $+\\lambda_2$")
    save_figure(fig, "potentials",
                "The self-consistent mass shift $M(y) - m$ (left) and potential $v(y)$ "
                "(right), vertical axes in units of $m$, of $N = 136$ with the repulsive "
                "coupling $+\\lambda_2$ at the five slices (light blue: $a_{4,0} = 0$, "
                "dark blue: $a_{4,0} = 2$) against the hidden coordinate $y$. Both are "
                "concentrated in the tip region and become much larger along the "
                "history: the largest $|M - m|$ grows from $0.008\\,m$ at "
                "$a_{4,0} = 0$ to $0.355\\,m$ at $a_{4,0} = 1.5$ ($0.310\\,m$ at "
                "$a_{4,0} = 2$), the largest $|v|$ from $0.015\\,m$ to $0.242\\,m$; "
                "both stay below $0.4\\,m$.")
    report("profile maximum / recorded maximum of |M - m|",
           ", ".join(f"{r:.5f}" for r in ratios))
    check(all(0.998 <= r <= 1.0 + 1e-12 for r in ratios),
          "the profile maxima of |M - m| lie within 0.2 percent below the recorded ones",
          record=f"{RECORD_RESULTS}/ground/summary.csv, column max_abs_Meff_minus_m")
    m_max = [float(ground[state_id(136, "lamp2", a4)]["max_abs_Meff_minus_m"])
             for a4 in SLICES]  # the solver's largest |M - m| at each slice
    v_max = [float(ground[state_id(136, "lamp2", a4)]["max_abs_v_v"]) for a4 in SLICES]
    report("largest |M - m| at the five slices", ", ".join(f"{v:.3f}" for v in m_max))
    report("largest |v| at the five slices", ", ".join(f"{v:.3f}" for v in v_max))
    check(all(v_max[i + 1] > v_max[i] for i in range(4)) and max(m_max + v_max) < 0.4,
          "the largest |v| grows at every slice; both potentials stay below 0.4 m",
          record=f"{RECORD_RESULTS}/ground/summary.csv, columns max_abs_Meff_minus_m "
                 "and max_abs_v_v")
    '''),
    md(r"""
    ## 15. How fast the self-consistent loop converges

    The file `ground/runs.json` records for every ground state the residual of each
    iteration of the self-consistent loop. The next cell draws it for the strongest
    couplings $\pm\lambda_2$ at the last slice $a_{4,0} = 2$ (the hardest cases), with
    the tolerance $10^{-11}$ as a dashed line, and checks that all 75 ground states
    converged directly (path `direct`: no fallback was needed) with a final residual at
    or below the tolerance (zero for $\lambda = 0$, where one iteration suffices).
    """),
    code(r'''
    runs = json.loads((NEW_RESULTS / "ground/runs.json").read_text(encoding="utf-8"))
    by_id = {run["id"]: run for run in runs}
    fig, ax = plt.subplots()
    styles = {"lamp2": "-", "lamm2": "--"}
    for colour, n in zip(PALETTE, (8, 136, 688)):
        for tag, style in styles.items():
            history = by_id[state_id(n, tag, 2.0)]["scfHistory_iteration_residual_E"]
            ax.plot([h[0] for h in history], [h[1] for h in history], style, marker="o",
                    ms=4, color=colour, lw=1.5,
                    label=f"$N = {n}$, {'+' if tag == 'lamp2' else '-'}$\\lambda_2$")
    ax.axhline(1e-11, color="0.3", ls=":", lw=1.2, label="tolerance $10^{-11}$")
    ax.set_yscale("log")
    ax.set_xlabel("iteration")
    ax.set_ylabel("residual: largest change of the potential (units of $m$)")
    ax.set_title("Anderson mixing, $a_{4,0} = 2$, couplings $\\pm\\lambda_2$")
    ax.legend(fontsize=8, ncol=2)
    save_figure(fig, "scf_convergence",
                "Convergence of the self-consistent loop with Anderson mixing: the "
                "residual (vertical axis, logarithmic, units of $m$) at each iteration "
                "(horizontal axis) for $N = 8$, $136$, $688$ with the couplings "
                "$+\\lambda_2$ (solid) and $-\\lambda_2$ (dashed) at $a_{4,0} = 2$; the "
                "dotted line is the tolerance $10^{-11}$. The residual falls by about one "
                "order of magnitude per iteration, and every loop ends below the "
                "tolerance after at most 17 iterations. For $N = 8$ the curves of "
                "$+\\lambda_2$ and $-\\lambda_2$ coincide, a consequence of an exact "
                "symmetry of the zero-mode state.")
    direct = all(run["path"] == "direct" for run in runs)
    final = max(run["scfHistory_iteration_residual_E"][-1][1] for run in runs)
    longest = max(run["iterations"] for run in runs)
    report("largest final residual / largest number of iterations",
           f"{final:.2e} / {longest}")
    check(len(runs) == 75 and direct and final <= 1e-11,
          "all 75 ground states converged directly below the tolerance 1e-11",
          record=f"{RECORD_REPORT}, check ground_scf_converged")
    '''),
    md(r"""
    ## 16. The excitations of the gas along the history

    For every ground state the solver also lists its lowest **particle-hole
    excitations** (up to 24, in the files `excited/particle-hole/<state>.csv`): one
    particle is taken out of an occupied level (the *hole*) and put into an empty level
    (the *particle*); the excitation energy is $\Delta\varepsilon =
    \varepsilon_{particle} - \varepsilon_{hole}$, and the *multiplicity* is the number
    of ways to do it, $g_{hole} \times g_{particle}$. Each excitation is named by its
    two levels, written `n2:j:parity:label`. The next cell draws the excitations of
    $N = 136$ without interaction at the five slices and makes three checks over all
    75 states: (1) the lowest excitation is the Kohn-Sham gap; (2) every excitation
    listed at all five slices of a series gets cheaper from slice to slice; (3) none of
    the listed excitations stays inside one *sector* (the same shell $n_2$, block type
    $j$ and parity). The third point matters for the history: the exact evolution
    along $a_4 = AHx_4$ keeps the momentum, the block type and the parity of every
    orbital, so the history alone cannot create any of these excitations. It can only
    cause jumps inside a sector; the cell prints the energy of the jump with the
    largest adiabaticity number $Q$ of each state (column `Q_max_delta_eps` of
    `adiabatic/adiabaticity.csv`), which is much larger.
    """),
    code(r'''
    TAGS = ("lam0", "lamp1", "lamm1", "lamp2", "lamm2")  # the five couplings


    def read_pairs(n, tag, a4):
        """{(hole, particle): (energy, multiplicity, same sector?)} of one state."""
        path = NEW_RESULTS / "excited/particle-hole" / f"{state_id(n, tag, a4)}.csv"
        with open(path, newline="", encoding="utf-8") as handle:
            return {(r["hole_levels"], r["particle_levels"]):
                    (float(r["delta_eps"]), float(r["multiplicity"]), r["same_sector"])
                    for r in csv.DictReader(handle)}


    lists = {(n, tag, a4): read_pairs(n, tag, a4)
             for n in (8, 136, 688) for tag in TAGS for a4 in SLICES}  # 75 states
    fig, ax = plt.subplots()
    for a4 in SLICES:
        values = list(lists[(136, "lam0", a4)].values())
        ax.scatter([a4] * len(values), [v[0] for v in values],
                   s=[v[1] / 40.0 for v in values],  # marker area ~ multiplicity
                   color=PALETTE[0], alpha=0.3, edgecolors=PALETTE[0])
    lowest = [min(v[0] for v in lists[(136, "lam0", a4)].values()) for a4 in SLICES]
    ax.plot(SLICES, lowest, "o-", color=PALETTE[1], lw=1.8, ms=5,
            label="lowest excitation (the Kohn-Sham gap)")
    ax.plot(a_fine, lowest[0] * np.exp(-a_fine), "--", color="0.4", lw=1.0,
            label="$\\propto e^{-a_{4,0}}$")
    ax.scatter([], [], s=60, color=PALETTE[0], alpha=0.3, edgecolors=PALETTE[0],
               label="excitations (area: multiplicity)")
    ax.set_yscale("log")
    ax.set_xlabel("slice $a_{4,0}$ of the history")
    ax.set_ylabel("excitation energy $\\Delta\\varepsilon$ (units of $m$)")
    ax.set_title("Particle-hole excitations of $N = 136$, $\\lambda = 0$")
    ax.legend(fontsize=8, loc="lower left")
    save_figure(fig, "particle_hole",
                "The lowest particle-hole excitation energies (vertical axis, "
                "logarithmic, units of $m$) of the free state $N = 136$ at the five "
                "slices $a_{4,0}$ (horizontal axis); the area of a marker is proportional "
                "to the multiplicity of the excitation. Orange: the lowest excitation, "
                "which is the Kohn-Sham gap; dashed: a fall like $e^{-a_{4,0}}$ from the "
                "first gap. The whole ladder moves down along the history because the "
                "brane-band levels on both sides of each excitation redshift; none of "
                "these excitations stays inside one sector, so the history alone cannot "
                "create them.")
    lowest_is_gap = all(
        abs(min(v[0] for v in lists[key].values())
            - float(ground[state_id(*key)]["KS_gap"])) <= 1e-12 for key in lists)
    cheaper = True
    for n in (8, 136, 688):
        for tag in TAGS:
            series = [lists[(n, tag, a4)] for a4 in SLICES]
            common = set(series[0]).intersection(*series[1:])  # listed at every slice
            cheaper = cheaper and all(series[i + 1][key][0] < series[i][key][0]
                                      for key in common for i in range(4))
    count = sum(len(pairs) for pairs in lists.values())
    inside = sum(1 for pairs in lists.values() for v in pairs.values() if v[2] != "false")
    jumps = [float(row["Q_max_delta_eps"]) for row in
             read_table(NEW_RESULTS, "adiabatic/adiabaticity.csv").values()
             if row["Q_max_delta_eps"] != "null"]  # null: no jump (N = 8)
    report("particle-hole excitations listed / inside one sector", f"{count} / {inside}")
    report("lowest excitation of N = 136 at a4,0 = 0 and 2",
           f"{lowest[0]:.5f}, {lowest[-1]:.5f}")
    report("energy of the largest-Q jump inside a sector (smallest, largest)",
           f"{min(jumps):.3f}, {max(jumps):.3f}")
    check(lowest_is_gap, "in all 75 states the lowest particle-hole energy is the KS gap",
          record=f"{RECORD_RESULTS}/excited/particle-hole and ground/summary.csv")
    check(cheaper, "every excitation listed at all five slices gets cheaper along the "
                   "history")
    check(count == 1610 and inside == 0,
          "none of the 1610 listed excitations stays inside one sector",
          record=f"{RECORD_RESULTS}/excited/particle-hole, column same_sector")
    '''),
    md(r"""
    ## 17. The last check

    The last cell checks that every figure file of this notebook exists in the folder
    Revision/textbook/figures and prints the number of checks that passed.
    """),
    code(r'''
    NAMES = ["levels_history", "gaps_history", "delta_scf", "energy_history",
             "densities", "potentials", "scf_convergence",
             "particle_hole"]  # the figures, in order
    missing = [name for number, name in enumerate(NAMES, start=1)
               if not output_file(f"{FIGURE_FOLDER}/15a_{number}_{name}.png").is_file()]
    check(missing == [], "every figure file of this notebook exists")
    all_checks_passed()
    '''),
    md(r"""
    ## 18. What this notebook showed

    - The Rust solver, built on this computer, reproduces the whole canonical matrix of
      the Revision record: the same files, all 42 of its own checks PASS, and every key
      number within the tolerances fixed in advance (COMPUTED).
    - Along the deflating history the brane band redshifts like $k e^{-a_{4,0}}$, the
      levels at $k = 0$ stay where they are, the gaps close at nearly the rate
      $e^{-a_{4,0}}$, and the energy of the gas falls.
    - Without interaction Delta-SCF equals the gap exactly; with interaction the orbital
      relaxation stays below $10^{-3}\,m$. The lowest particle-hole excitation is the
      gap, every listed excitation gets cheaper along the history, and none of them
      stays inside one sector, so the history alone cannot create them.
    - The particles sit near the brane, the proper densities and the self-consistent
      potentials are largest at the tip, and the self-consistent loop converges in at
      most 17 iterations.
    - These are instantaneous states on a PRESCRIBED background; the brane is ASSUMED;
      the filling is a CONVENTION; whether the gas really follows the instantaneous
      states along the history is the question of adiabaticity, which the solver
      measures with the number $Q_{max}$ compared above.
    """),
]

if __name__ == "__main__":
    raise SystemExit(run_builder(__file__))
