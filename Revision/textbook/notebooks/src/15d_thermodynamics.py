#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
"""Builder of Notebook 15d, "Thermodynamics of the Kohn-Sham gas along the deflating
history" (textbook "Universes in Pairs", chapter 15).

The notebook Revision/textbook/notebooks/15d_thermodynamics.ipynb is BUILT from this file
by Revision/textbook/tools/nbkit.py (never edit the .ipynb by hand):

    python Revision/textbook/tools/nbkit.py build \
        Revision/textbook/notebooks/src/15d_thermodynamics.py --date YYYY-MM-DD
    python Revision/textbook/tools/nbkit.py check \
        Revision/textbook/notebooks/src/15d_thermodynamics.py

The notebook runs the Revision Kohn-Sham solver (subcommand "single" with "--T" and
"--mermin-levels") for the free thermal states N = 8 and N = 136 at the slices of the
history, writes its outputs into Revision/kohn_sham/solver/target/textbook_15d (ignored by
git), and recomputes from the solver's levels the chemical potential (at 40 digits with
mpmath and in double precision with the well-conditioned balance form), the energy, the
entropy, the free energy, the grand potential, the heat capacity, dN/dmu and the
sea-hole diagnostic of Revision/kohn_sham/results/thermo/thermodynamics.csv.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools"))
from nbkit import code, md, run_builder  # noqa: E402

FIGURES = [
    "15d_1_root_conditioning",
    "15d_2_chemical_potential",
    "15d_3_free_energy_entropy",
    "15d_4_heat_capacity",
    "15d_5_occupations",
    "15d_6_sea_holes",
    "15d_7_interaction_free_energy",
]

FACTS = {
    "id": "15d",
    "name": "15d_thermodynamics",
    "title": "Thermodynamics of the Kohn-Sham gas along the deflating history",
    "purpose": (
        "It builds the Rust Kohn-Sham solver with cargo (a full build of about a minute "
        "when the program is missing, a second when it is up to date), runs it for the "
        "free thermal states N = 8 and N = 136 "
        "of dirac16complex at the slices of the deflating history, recomputes from the "
        "solver's levels the chemical potential (at 40 digits and with the "
        "well-conditioned double-precision balance), the energy, entropy, free energy, "
        "grand potential, heat capacity and the sea-hole diagnostic of the committed "
        "Revision record, and draws the chemical potential, free energy, entropy and "
        "heat capacity as functions of the temperature. The solver writes its output "
        "files (about 0.6 MB) into the folder "
        "`Revision/kohn_sham/solver/target/textbook_15d`, which git ignores."
    ),
    "records": [
        ["Revision/kohn_sham/results/thermo/thermodynamics.csv",
         "the 135 Mermin states: mu, E, S, F, Omega, C_V, dN/dmu, rounding bound of mu, "
         "sea holes"],
        ["Revision/kohn_sham/results/ground/summary.csv",
         "the zero-temperature energies and gaps"],
        ["Revision/kohn_sham/results/parameters.json",
         "the temperatures and the thermal window"],
        ["Revision/kohn_sham/ks-theory.json",
         "the Mermin functional, the filling convention and its status"],
        ["Revision/kohn_sham/reports/ks-rust-solver.json",
         "the checks thermo_mu_well_conditioned_root, thermo_CV_identity, "
         "thermo_entropy_identity and thermo_sea_hole_diagnostic_computed"],
        ["Revision/kohn_sham/reports/ks-rust-mermin-roots.json",
         "the 40-digit roots of the Mermin condition"],
    ],
    "packages": ["numpy", "mpmath", "matplotlib"],
    "needs_rust": [{"manifest": "Revision/kohn_sham/solver/Cargo.toml",
                    "binaries": ["revision_ks_solver"], "build_minutes": 1}],
    "expected_seconds": 30,
    "timeout_seconds": 900,
    "files_written": ["Revision/textbook/figures/15d.captions.json"]
    + [f"Revision/textbook/figures/{name}.png" for name in FIGURES],
    "final_lines": [
        "PASS every figure file of this notebook exists",
        "ALL 15 CHECKS PASSED (notebook 15d)",
    ],
    "troubleshooting": [],
}

CELLS = [
    md(r"""
    ## 1. What this notebook computes

    At a temperature $T > 0$ the particles of the Kohn-Sham gas no longer fill exactly
    the lowest levels: each level is occupied with the **Fermi-Dirac** probability
    $f = 1/(1 + e^{(\varepsilon - \mu)/T})$, where the **chemical potential** $\mu$ is
    fixed by the particle number. This is Mermin's finite-temperature version of
    Kohn-Sham theory. The Revision record holds 135 such states (three particle numbers,
    three couplings, five slices of the history, three temperatures). This notebook

    - runs the Rust solver for the free states ($\lambda = 0$) of $N = 8$ and $N = 136$
      and reads its levels;
    - recomputes from these levels, in plain Python, $\mu$ (at 40 digits with mpmath),
      the energy $E$, the entropy $S$, the free energy $F = E - TS$, the grand
      potential $\Omega$, the heat capacity $C_V$ and $dN/d\mu$, and compares all of
      them with the record;
    - explains why the solver computes $\mu$ from a **balance of particles and holes**
      instead of the direct count, and shows the difference;
    - draws $\mu$, $F$, $S$ and $C_V$ as continuous functions of $T$, the occupations at
      three temperatures, the sea-hole diagnostic of the filling convention, and the
      effect of the interaction on $F$.

    It draws seven figures and takes about half a minute.
    """),
    md(r"""
    ## 3. The words used in this notebook

    - **Temperature** $T$: measured in units of the mass $m$ (Boltzmann's constant is
      1).
    - **Fermi-Dirac occupation** $f(x) = 1/(1 + e^{x})$ with $x = (\varepsilon - \mu)/T$:
      the probability that a level of energy $\varepsilon$ is occupied. It is 1 far below
      $\mu$, 0 far above, and $1/2$ at $\varepsilon = \mu$. A useful identity:
      $1 - f(x) = f(-x)$.
    - **Chemical potential** $\mu$: the number that makes the occupations add up to the
      particle number, $\sum g f = N$ ($g$ the degeneracy of a level).
    - **Entropy** $S = -\sum g[f\ln f + (1 - f)\ln(1 - f)]$: a measure of how many
      microscopic arrangements the gas can take.
    - **Free energy** $F = E - TS$ and **grand potential** $\Omega = F - \mu N$.
    - **Heat capacity** $C_V = dE/dT = T\,dS/dT$ at fixed $N$: how much energy one
      unit of temperature costs.
    - **Activated**: a gas whose lowest empty level lies a gap $\Delta$ above the
      highest occupied one; at $T \ll \Delta$ the thermal excitations are suppressed like
      $e^{-\Delta/(2T)}$.
    - **Hole**: an empty place in a level that is normally occupied.
    - **Sea**: the levels of the negative branch, which the filling CONVENTION of the
      record leaves out (normal ordering); **sea holes** would be thermal antiparticles.
    - **Double precision**: the computer's usual numbers, with about 16 significant
      digits; **40 digits**: mpmath's numbers with as many digits as asked for.
    - **Conditioning**: how strongly a result reacts to small errors of the input.
    """),
    md(r"""
    ## 4. The physical and mathematical situation

    The Kohn-Sham states of dirac16complex live in the author's metric, with 3-space
    $x_1, x_2, x_3$ inflating like $e^{a_4}$, the three extra times $x_5, x_6, x_7$
    deflating like $e^{-a_4}$, the time $x_4$ and the hidden direction $x_8$ (coordinate
    $y$). The history $a_4 = AHx_4$ is a PRESCRIBED BACKGROUND, and each thermal state
    is an instantaneous state at one slice $a_{4,0}$.

    **Mermin's functional** (Revision record ks-theory.json, thermodynamics): with the
    levels $\varepsilon_i$ (degeneracy $g_i$) of the Kohn-Sham Hamiltonian,

    $$\sum_i g_i f_i = N, \quad E = \sum_i g_i f_i\varepsilon_i -
    2\,\mathrm{Vol}_7\!\int e^{6Hy}e_{int}\,dy, \quad
    S = -\sum_i g_i[f_i\ln f_i + (1 - f_i)\ln(1 - f_i)],$$
    $$F = E - TS, \qquad \Omega = -T\sum_i g_i\ln(1 + e^{-(\varepsilon_i - \mu)/T})
    - 2\,\mathrm{Vol}_7\!\int e^{6Hy}e_{int}\,dy = F - \mu N .$$

    Without interaction ($\lambda = 0$) the levels do not depend on $T$ and $e_{int} = 0$,
    so everything follows from the levels. Then the heat capacity has a closed form:
    differentiating $\sum g f = N$ at fixed $N$ gives $d\mu/dT$, and inserting it into
    $dE/dT$ gives, with $w_i = g_i f_i(1 - f_i)$ and $d_i = \varepsilon_i - \mu$,

    $$C_V = \frac{1}{T^2}\left[\sum_i w_i d_i^2 - \frac{(\sum_i w_i d_i)^2}{\sum_i
    w_i}\right], \qquad \frac{dN}{d\mu} = \frac{1}{T}\sum_i w_i .$$

    (Line by line: $df/dx = -f(1-f)$; $dx_i/dT = -d_i/T^2 - (d\mu/dT)/T$; fixed $N$ means
    $\sum w_i\,dx_i/dT = 0$, so $d\mu/dT = -\sum w_i d_i/(T\sum w_i)$; then
    $dE/dT = -\sum w_i\varepsilon_i\,dx_i/dT$, and replacing $\varepsilon_i$ by $d_i$
    changes nothing because $\sum w_i\,dx_i/dT = 0$.)

    **The filling convention** (a CONVENTION whose justification is OPEN): particles fill
    only the positive branch and the zero modes; the negative branch (the sea) is never
    occupied thermally. The record measures how good this is: the **sea holes** that the
    sea's brane band would carry at the same $\mu$ and $T$.

    **Parameters**: $H = m = 1$, $L = 3$, $\Delta k = 0.25$, $T = 0.01, 0.02, 0.05$; $N$
    counts the doubled system (universe and Z2 image, the brane being ASSUMED).
    """),
    md(r"""
    ## 5. Building the solver and computing the free thermal states

    The next cell builds the solver and defines `thermal_state`, which runs
    `revision_ks_solver single` with `--T` (the temperature) and `--margin 0.2` (the
    label set of the canonical matrix, so that the state is exactly the recorded one),
    and with `--mermin-levels`, which writes the final levels as decimal numbers that
    read back into exactly the solver's numbers. It returns the solver's $\mu$, its
    levels with degeneracies, and the full level list (shell, block type, parity,
    label, energy, degeneracy, occupation). The cell then computes the 18 free states
    $N = 8, 136$, $a_{4,0} = 0, 1, 2$, $T = 0.01, 0.02, 0.05$, and two more for $N = 136$
    at $a_{4,0} = 0.5$ and $1.5$ ($T = 0.05$), and compares each $\mu$ with the record.
    """),
    code(r'''
    import csv  # reads the tables (CSV files)
    import math  # exp, log for single numbers

    import mpmath  # numbers with 40 digits
    import numpy as np  # arrays of numbers

    program = rust_program("Revision/kohn_sham/solver/Cargo.toml", "revision_ks_solver")
    RUN_FOLDER = REPO / "Revision/kohn_sham/solver/target/textbook_15d"  # git ignores it
    RUN_FOLDER.mkdir(parents=True, exist_ok=True)
    PALETTE = ["#2a78d6", "#eb6834", "#1baf7a", "#eda100", "#e87ba4", "#008300",
               "#4a3aa7", "#e34948"]  # the colours of the figures, in a fixed order
    SHADES = {0.0: "#86b6ef", 0.5: "#5598e7", 1.0: "#2a78d6", 1.5: "#1c5cab",
              2.0: "#104281"}  # one shade of blue per slice, light to dark
    TEMPS = (0.01, 0.02, 0.05)


    def state_id(n, a4, t, tag="lam0"):
        return f"N{n}_{tag}_a{round(10 * a4):02d}_T{round(1000 * t)}"


    def thermal_state(n, a4, t):
        """Run the solver for one free thermal state; (mu, eps, deg, levels)."""
        name = state_id(n, a4, t)
        out, lev = RUN_FOLDER / f"{name}.json", RUN_FOLDER / f"{name}-levels.json"
        done = subprocess.run(
            [str(program), "single", "--root", str(REPO), "--m", "1", "--lambda", "0",
             "--a4", repr(a4), "--N", repr(float(n)), "--T", repr(t), "--margin", "0.2",
             "--out", str(out), "--mermin-levels", str(lev)],
            capture_output=True, text=True)
        if done.returncode != 0:
            raise RuntimeError(f"the solver failed for {name}: {done.stderr[-500:]}")
        exact = json.loads(lev.read_text(encoding="utf-8"))
        full = json.loads(out.read_text(encoding="utf-8"))
        eps = [float(e) for e, _ in exact["levels_eps_deg"]]  # exactly the solver's
        deg = [float(g) for _, g in exact["levels_eps_deg"]]
        return float(exact["mu"]), eps, deg, full["levels_n2_j_parity_label_eps_deg_f"]


    THERMO = "Revision/kohn_sham/results/thermo/thermodynamics.csv"
    with open(repository_file(THERMO), newline="", encoding="utf-8") as handle:
        record = {row["id"]: row for row in csv.DictReader(handle)}
    states = {}
    for n in (8, 136):
        for a4 in (0.0, 1.0, 2.0):
            for t in TEMPS:
                states[(n, a4, t)] = thermal_state(n, a4, t)
    for a4 in (0.5, 1.5):
        states[(136, a4, 0.05)] = thermal_state(136, a4, 0.05)
    worst_mu = max(abs(mu - float(record[state_id(n, a4, t)]["mu"]))
                   for (n, a4, t), (mu, _, _, _) in states.items())
    report("free thermal states computed", len(states))
    report("largest |mu(solver now) - mu(record)|", f"{worst_mu:.1e}")
    check(worst_mu < 1e-12, f"the solver reproduces the recorded mu of {len(states)} states",
          record=f"{THERMO}, column mu")
    '''),
    md(r"""
    ## 6. The chemical potential at 40 digits, and the other functions of state

    The next cell solves $\sum g f = N$ again with mpmath at 40 significant digits
    (Newton's method started at the solver's $\mu$), so that rounding plays no role at
    all. The solver's $\mu$ must lie within its own **rounding bound** (column
    `mu_rounding_bound` of the record) of this exact root. Then it computes $E$, $S$,
    $F$, $\Omega$, $C_V$ (closed form) and $dN/d\mu$ in double precision at the solver's
    $\mu$ and compares them with the record. The record's $C_V$ is a numerical
    derivative $T\,dS/dT$ (Richardson differences), so the comparison allows
    $10^{-4}$; the others agree to $10^{-12}$.
    """),
    code(r'''
    def exact_root(eps, deg, n, t, guess):
        """The root of sum g f = N with 40 significant digits (Newton's method)."""
        with mpmath.workdps(40):
            levels = [(mpmath.mpf(e), mpmath.mpf(g)) for e, g in zip(eps, deg)]
            temp, mu = mpmath.mpf(t), mpmath.mpf(guess)
            for _ in range(60):
                occ = [(g, 1 / (1 + mpmath.exp((e - mu) / temp))) for e, g in levels]
                count = sum(g * f for g, f in occ) - n
                slope = sum(g * f * (1 - f) for g, f in occ) / temp  # dN/dmu
                step = count / slope
                mu -= step
                if abs(step) < mpmath.mpf(10) ** -36:
                    break
            return mu


    def functions_of_state(eps, deg, mu, t):
        """E, S, F, Omega, C_V, dN/dmu of a free state (double precision, stable forms)."""
        e, g = np.array(eps), np.array(deg)
        x = (e - mu) / t
        small = np.exp(-np.abs(x))  # e^{-|x|}, never overflows
        f_abs = small / (1.0 + small)  # f(|x|)
        f = np.where(x > 0, f_abs, 1.0 - f_abs)  # f(x)
        energy = float(np.sum(g * f * e))
        # -[f ln f + (1-f) ln(1-f)] = ln(1 + e^{-|x|}) + |x| f(|x|)
        entropy = float(np.sum(g * (np.log1p(small) + np.abs(x) * f_abs)))
        # ln(1 + e^{-x}) = max(-x, 0) + ln(1 + e^{-|x|})
        omega = -t * float(np.sum(g * (np.maximum(-x, 0.0) + np.log1p(small))))
        w = g * f_abs * (1.0 - f_abs)  # g f (1 - f), the same for x and -x
        d = e - mu
        cv = float((np.sum(w * d * d) - np.sum(w * d) ** 2 / np.sum(w)) / t ** 2)
        return energy, entropy, energy - t * entropy, omega, cv, float(np.sum(w) / t)


    rel = lambda a, b: abs(a - b) / max(abs(b), 1.0)  # relative to max(|b|, 1)
    worst = {"root": 0.0, "E S F Omega": 0.0, "C_V": 0.0, "dN/dmu": 0.0}
    for (n, a4, t), (mu, eps, deg, _) in states.items():
        row = record[state_id(n, a4, t)]
        root = exact_root(eps, deg, n, t, mu)
        worst["root"] = max(worst["root"],
                            float(abs(mu - root)) / float(row["mu_rounding_bound"]))
        e_, s_, f_, o_, cv, dn = functions_of_state(eps, deg, mu, t)
        worst["E S F Omega"] = max(worst["E S F Omega"], rel(e_, float(row["E"])),
                                   rel(s_, float(row["entropy"])), rel(f_, float(row["F"])),
                                   rel(o_, float(row["Omega_direct"])))
        worst["C_V"] = max(worst["C_V"], abs(cv / float(row["C_V"]) - 1.0))
        worst["dN/dmu"] = max(worst["dN/dmu"], abs(dn / float(row["dN_dmu"]) - 1.0))
    report("largest |mu - 40-digit root| / recorded rounding bound", f"{worst['root']:.2f}")
    for key in ("E S F Omega", "C_V", "dN/dmu"):
        report(f"largest relative difference, {key}", f"{worst[key]:.1e}")
    check(worst["root"] <= 1.0, "mu lies within its rounding bound of the 40-digit root",
          record="Revision/kohn_sham/reports/ks-rust-mermin-roots.json and "
                 f"{THERMO}, column mu_rounding_bound")
    check(worst["E S F Omega"] < 1e-12,
          f"E, S, F and Omega of {len(states)} states reproduced",
          record=f"{THERMO}, columns E, entropy, F, Omega_direct")
    check(worst["C_V"] < 1e-4, "the closed-form C_V reproduces the recorded T dS/dT",
          record=f"{THERMO}, column C_V")
    check(worst["dN/dmu"] < 1e-9, "dN/dmu reproduced", record=f"{THERMO}, column dN_dmu")
    '''),
    md(r"""
    ## 7. Why the solver uses a balance instead of the direct count

    Near a closed shell at low temperature almost every level is either full ($f
    \approx 1$) or empty ($f \approx 0$). The direct count $\sum g f - N$ then adds
    numbers close to 1 and subtracts $N$: in double precision the result is a multiple
    of the rounding step of $N$ (about $10^{-15}$), while the true value changes with
    $\mu$ only at the rate $dN/d\mu$, which for $N = 8$ at $a_{4,0} = 0$,
    $T = 0.01$ is about $1.2 \times 10^{-6}$. So the direct count cannot locate $\mu$
    better than about $10^{-15}/(1.2 \times 10^{-6})$, a few times $10^{-10}$ to
    $10^{-9}$ (the record found an error of $8.3 \times 10^{-10}$ in the solver's
    earlier version, which used the direct count). The solver
    instead balances the thermal **particles** above the filled levels against the
    thermal **holes** below them, $P = \sum_{above} g f(x)$ and $H_l = \sum_{below} g
    f(-x)$ (each hole factor computed as $f(-x)$, never as $1 - f$), and solves
    $\ln P = \ln H_l$; no large numbers are subtracted. The next cell computes the
    direct count in double precision and the exact count at 40 digits at 61 values of
    $\mu$ within $\pm 3 \times 10^{-9}$ of the root, and finds the root of the balance
    in double precision by bisection down to neighbouring numbers.
    """),
    code(r'''
    def balance_root(eps, deg, n, t):
        """mu from ln P = ln H (particles above = holes below the T = 0 filling)."""
        order = np.argsort(eps, kind="stable")
        e, g = np.array(eps)[order], np.array(deg)[order]
        filled = int(np.searchsorted(np.cumsum(g), n - 1e-9)) + 1  # T = 0 filling
        below_e, below_g, above_e, above_g = e[:filled], g[:filled], e[filled:], g[filled:]

        def log_sum(log_terms):  # ln(sum e^{t}) without overflow or underflow
            top = float(np.max(log_terms))
            return top + math.log(float(np.sum(np.exp(log_terms - top))))

        def log_f(x):  # ln f(x) = -ln(1 + e^{x}), stable for every x
            return -(np.maximum(x, 0.0) + np.log1p(np.exp(-np.abs(x))))

        def balance(mu):
            return (log_sum(np.log(above_g) + log_f((above_e - mu) / t))
                    - log_sum(np.log(below_g) + log_f(-(below_e - mu) / t)))

        lo, hi = float(e[0]) - 1.0, float(e[-1]) + 1.0
        while lo < 0.5 * (lo + hi) < hi:  # bisection down to neighbouring numbers
            mid = 0.5 * (lo + hi)
            lo, hi = (mid, hi) if balance(mid) < 0.0 else (lo, mid)
        return lo


    mu8, eps8, deg8, _ = states[(8, 0.0, 0.01)]
    root8 = exact_root(eps8, deg8, 8, 0.01, mu8)
    offsets = np.linspace(-3e-9, 3e-9, 61)
    direct, exact = [], []
    for off in offsets:
        x = (np.array(eps8) - (mu8 + off)) / 0.01
        direct.append(float(np.sum(np.array(deg8) / (1.0 + np.exp(x)))) - 8.0)
        with mpmath.workdps(40):
            m_ = mpmath.mpf(mu8) + mpmath.mpf(off)
            exact.append(float(sum(mpmath.mpf(g) / (1 + mpmath.exp((mpmath.mpf(e) - m_)
                                                                    / mpmath.mpf(0.01)))
                                   for e, g in zip(eps8, deg8)) - 8))
    fig, ax = plt.subplots()
    ax.plot(offsets * 1e9, direct, "s-", color=PALETTE[1], ms=4, lw=1.2,
            label="direct count, double precision")
    ax.plot(offsets * 1e9, exact, color=PALETTE[0], lw=2.0, label="exact count, 40 digits")
    ax.axvline(float(root8 - mu8) * 1e9, color="0.3", ls=":", lw=1.2, label="exact root")
    ax.axhline(0.0, color="0.6", lw=0.8)
    ax.set_xlabel("$\\mu$ minus the solver's $\\mu$ (units of $10^{-9}\\,m$)")
    ax.set_ylabel("$\\sum g f - N$")
    ax.set_title("$N = 8$, $a_{4,0} = 0$, $T = 0.01$: the direct count is too coarse")
    ax.legend(fontsize=8)
    zero_at = [off for off, value in zip(offsets, direct) if value == 0.0]  # direct = 0
    if zero_at:  # where the double-precision count says "exactly N particles"
        miss = min(abs(off - float(root8 - mu8)) for off in zero_at)  # nearest such point
        where = ("is zero only on a short interval that misses the true root by at "
                 f"least ${miss * 1e10:.0f} \\times 10^{{-10}}\\,m$")
        report("distance of the zeros of the direct count from the true root",
               f"at least {miss:.1e} m")
    else:  # (on another computer the rounding steps may fall differently)
        where = "is never exactly zero at the sampled points"
    save_figure(fig, "root_conditioning",
                "The particle-number condition $\\sum g f - N$ (vertical axis, of size "
                "$10^{-15}$) against $\\mu$ near its root (horizontal axis, in units of "
                "$10^{-9}\\,m$) for the activated state $N = 8$, $a_{4,0} = 0$, "
                "$T = 0.01$: computed directly in double precision it moves in steps of "
                f"the rounding unit of $N$ (orange squares) and {where}, while the exact "
                "count (blue line, 40 digits) crosses zero at one point, the true root, "
                "which the balance of particles and holes finds.")
    worst_balance = 0.0
    for (n, a4, t), (mu, eps, deg, _) in states.items():
        root = exact_root(eps, deg, n, t, mu)
        worst_balance = max(worst_balance, float(abs(balance_root(eps, deg, n, t) - root)))
    zero_width = (np.sum(np.array(direct) == 0.0)) * (offsets[1] - offsets[0])
    report("width of the interval where the double-precision direct count is 0",
           f"{zero_width:.1e} m")
    report(f"largest |balance root - 40-digit root| ({len(states)} states)",
           f"{worst_balance:.1e}")
    check(worst_balance < 1e-15, "the double-precision balance finds mu to 1e-15",
          record="Revision/kohn_sham/reports/ks-rust-solver.json, check "
                 "thermo_mu_well_conditioned_root")
    '''),
    md(r"""
    ## 8. The chemical potential as a function of temperature

    With `balance_root` the next cell computes $\mu$ at 49 temperatures from $0.002$ to
    $0.05$ for $N = 8$ at $a_{4,0} = 0$, $1$, $2$, using the level set of the solver at
    $T = 0.05$ (the largest window; at lower temperatures the extra levels are empty to
    far below the rounding). For $a_{4,0} = 0$ the two-level picture explains $\mu$:
    the eight zero modes ($\varepsilon = 0$) lose as many particles as the 24 orbitals of
    the first band level ($\varepsilon = \Delta = 0.4307$) gain, $8e^{-\mu/T} =
    24e^{-(\Delta - \mu)/T}$, so $\mu = \Delta/2 - (T/2)\ln 3$ (the logarithm of the
    ratio of degeneracies). The check compares this formula with the record at
    $T = 0.01$.
    """),
    code(r'''
    T_GRID = np.linspace(0.002, 0.05, 49)


    def curves(n, a4):
        """mu, E, S, F, C_V on T_GRID from the solver's T = 0.05 level set."""
        _, eps, deg, _ = states[(n, a4, 0.05)]
        rows = []
        for t in T_GRID:
            mu = balance_root(eps, deg, n, t)
            energy, entropy, free, _, cv, _ = functions_of_state(eps, deg, mu, t)
            rows.append((mu, energy, entropy, free, cv))
        return np.array(rows)  # columns: mu, E, S, F, C_V


    GROUND = "Revision/kohn_sham/results/ground/summary.csv"
    with open(repository_file(GROUND), newline="", encoding="utf-8") as handle:
        ground = {row["id"]: row for row in csv.DictReader(handle)}
    gap8 = float(ground["N8_lam0_a00"]["KS_gap"])
    two_level = gap8 / 2.0 - 0.5 * T_GRID * math.log(3.0)
    curve8 = {a4: curves(8, a4) for a4 in (0.0, 1.0, 2.0)}
    fig, ax = plt.subplots()
    for a4 in (0.0, 1.0, 2.0):
        ax.plot(T_GRID, curve8[a4][:, 0], color=SHADES[a4], lw=2.0,
                label=f"$a_{{4,0}} = {a4:.0f}$")
        ax.plot(TEMPS, [float(record[state_id(8, a4, t)]["mu"]) for t in TEMPS], "o",
                color=SHADES[a4], ms=8, markerfacecolor="white")
    ax.plot(T_GRID, two_level, "--", color=PALETTE[1], lw=1.5,
            label="$\\Delta/2 - (T/2)\\ln 3$, $a_{4,0} = 0$")
    ax.plot([], [], "o", color="0.4", markerfacecolor="white", label="record")
    ax.set_xlabel("temperature $T$ (units of $m$)")
    ax.set_ylabel("chemical potential $\\mu$ (units of $m$)")
    ax.set_title("$N = 8$, $\\lambda = 0$: the chemical potential")
    ax.legend(fontsize=8)
    save_figure(fig, "chemical_potential",
                "The chemical potential $\\mu$ (vertical axis, units of $m$) of the free "
                "state $N = 8$ against the temperature $T$ (horizontal axis, units of "
                "$m$) at the slices $a_{4,0} = 0$, $1$, $2$ (lines: this notebook; open "
                "circles: the record). At $T \\to 0$ the chemical potential sits in the "
                "middle of the gap, $\\Delta/2$, and falls linearly with the slope "
                "$-(\\ln 3)/2$ (dashed, the two-level formula); the gap and with it "
                "$\\mu$ shrink along the history.")
    formula = gap8 / 2.0 - 0.005 * math.log(3.0)
    recorded = float(record[state_id(8, 0.0, 0.01)]["mu"])
    report("mu of N8_lam0_a00_T10: two-level formula / record",
           f"{formula:.12f} / {recorded:.12f}")
    check(abs(formula - recorded) < 1e-8, "the two-level formula gives mu to 1e-8",
          record=f"{THERMO}, N8_lam0_a00_T10")
    '''),
    md(r"""
    ## 9. Free energy and entropy along the history

    The next cell computes the curves of $N = 136$ at the five slices and draws the
    free energy measured from the ground-state energy, $F(T) - E_0$, and the entropy
    $S(T)$; the record's values are the open circles. It also checks the thermodynamic
    identity $-dF/dT = S$ with central differences $[F(T + h) - F(T - h)]/(2h)$,
    $h = 10^{-3}T$, at every temperature of the grid.
    """),
    code(r'''
    curve136 = {a4: curves(136, a4) for a4 in (0.0, 0.5, 1.0, 1.5, 2.0)}
    fig, (left, right) = plt.subplots(1, 2, figsize=(10.0, 4.0), layout="constrained")
    for a4, values in curve136.items():
        e0 = float(ground[f"N136_lam0_a{round(10 * a4):02d}"]["E_KS"])
        left.plot(T_GRID, values[:, 3] - e0, color=SHADES[a4], lw=2.0,
                  label=f"$a_{{4,0}} = {a4}$")
        right.plot(T_GRID, values[:, 2], color=SHADES[a4], lw=2.0)
        if a4 in (0.0, 1.0, 2.0):
            ids = [state_id(136, a4, t) for t in TEMPS]
            left.plot(TEMPS, [float(record[i]["F"]) - e0 for i in ids], "o",
                      color=SHADES[a4], ms=7, markerfacecolor="white")
            right.plot(TEMPS, [float(record[i]["entropy"]) for i in ids], "o",
                       color=SHADES[a4], ms=7, markerfacecolor="white")
    left.set_xlabel("temperature $T$")
    left.set_ylabel("$F - E_0$ (units of $m$)")
    left.set_title("Free energy, $N = 136$, $\\lambda = 0$")
    left.legend(fontsize=8)
    right.set_xlabel("temperature $T$")
    right.set_ylabel("entropy $S$")
    right.set_title("Entropy (circles: record)")
    save_figure(fig, "free_energy_entropy",
                "Left: the free energy measured from the ground-state energy, "
                "$F - E_0$ (vertical axis, units of $m$), of the free state $N = 136$ at "
                "the five slices (light to dark blue) against the temperature (horizontal "
                "axis, units of $m$). Right: the entropy $S$ (pure number). Circles: the "
                "record. Along the history the levels crowd together, so the same "
                "temperature excites more particles: the entropy grows and the free "
                "energy falls faster.")
    _, eps, deg, _ = states[(136, 1.0, 0.05)]
    worst_fs = 0.0
    for t in T_GRID:
        h = 1e-3 * t
        f_plus = functions_of_state(eps, deg, balance_root(eps, deg, 136, t + h), t + h)[2]
        f_minus = functions_of_state(eps, deg, balance_root(eps, deg, 136, t - h), t - h)[2]
        s = functions_of_state(eps, deg, balance_root(eps, deg, 136, t), t)[1]
        worst_fs = max(worst_fs, abs(-(f_plus - f_minus) / (2 * h) - s) / s)
    report("largest relative |-dF/dT - S|, N = 136, a4,0 = 1", f"{worst_fs:.1e}")
    check(worst_fs < 1e-4, "-dF/dT = S along the whole temperature grid",
          record="Revision/kohn_sham/reports/ks-rust-solver.json, check "
                 "thermo_entropy_identity")
    rising = all(bool(np.all(np.diff(v[:, 2]) > 0)) and bool(np.all(np.diff(v[:, 3]) < 0))
                 for v in curve136.values())
    check(rising, "S rises and F falls with T at every slice")
    '''),
    md(r"""
    ## 10. The heat capacity

    The next cell draws $C_V(T)$ (closed form) for $N = 8$ at three slices (left) and
    $N = 136$ at five slices (right), on logarithmic vertical axes, with the record's
    values. For $N = 8$ at $a_{4,0} = 0$ the gas is **activated**: below $T \approx 0.02$
    the heat capacity is tiny, because the first excitation costs the gap $0.43\,m$.
    Along the history the gap closes and the heat capacity rises at lower temperatures.
    $N = 136$ has a much smaller gap ($0.083\,m$ at $a_{4,0} = 0$, $0.014\,m$ at $2$) and
    a large heat capacity already at $T = 0.01$.
    """),
    code(r'''
    fig, (left, right) = plt.subplots(1, 2, figsize=(10.0, 4.0), layout="constrained")
    for a4, values in curve8.items():
        left.plot(T_GRID, values[:, 4], color=SHADES[a4], lw=2.0,
                  label=f"$a_{{4,0}} = {a4:.0f}$")
        left.plot(TEMPS, [float(record[state_id(8, a4, t)]["C_V"]) for t in TEMPS], "o",
                  color=SHADES[a4], ms=7, markerfacecolor="white")
    for a4, values in curve136.items():
        right.plot(T_GRID, values[:, 4], color=SHADES[a4], lw=2.0,
                   label=f"$a_{{4,0}} = {a4}$")
        if a4 in (0.0, 1.0, 2.0):
            right.plot(TEMPS, [float(record[state_id(136, a4, t)]["C_V"]) for t in TEMPS],
                       "o", color=SHADES[a4], ms=7, markerfacecolor="white")
    for ax, n in ((left, 8), (right, 136)):
        ax.set_yscale("log")
        ax.set_xlabel("temperature $T$ (units of $m$)")
        ax.set_title(f"Heat capacity, $N = {n}$, $\\lambda = 0$")
        ax.legend(fontsize=8)
    left.set_ylabel("$C_V$ (pure number)")
    save_figure(fig, "heat_capacity",
                "The heat capacity $C_V = dE/dT$ (vertical axis, logarithmic, pure "
                "number) of the free states $N = 8$ (left, three slices) and $N = 136$ "
                "(right, five slices) against the temperature (horizontal axis, units "
                "of $m$); circles: the record. The gas $N = 8$ is activated across its "
                "gap of $0.43\\,m$ at $a_{4,0} = 0$; as the history closes the gaps, "
                "the heat capacity rises at ever lower temperatures.")
    positive = all(bool(np.all(v[:, 4] > 0)) for v in list(curve8.values())
                   + list(curve136.values()))
    check(positive, "C_V > 0 at every temperature and slice")
    '''),
    md(r"""
    ## 11. What the occupations look like

    The next cell draws the occupation $f$ of every level of $N = 136$ at
    $a_{4,0} = 1$ against its energy, at the three temperatures of the record, with the
    chemical potential marked: the step of the Fermi-Dirac function softens over a width
    of a few $T$. The check confirms that the occupations add up to $N = 136$.
    """),
    code(r'''
    fig, ax = plt.subplots()
    sums = []
    for colour, t in zip(PALETTE, TEMPS):
        mu, eps, deg, levels = states[(136, 1.0, t)]
        e = np.array(eps)
        f = 1.0 / (1.0 + np.exp(np.minimum((e - mu) / t, 700.0)))
        sums.append(float(np.sum(np.array(deg) * f)))
        order = np.argsort(e)
        ax.plot(e[order], f[order], "o-", color=colour, ms=4, lw=1.0, label=f"$T = {t}$")
        ax.axvline(mu, color=colour, ls=":", lw=1.2)
    ax.set_xlim(0.2, 0.5)
    ax.set_xlabel("level $\\varepsilon$ (units of $m$)")
    ax.set_ylabel("occupation $f$")
    ax.set_title("$N = 136$, $a_{4,0} = 1$: Fermi-Dirac occupations (dotted: $\\mu$)")
    ax.legend()
    save_figure(fig, "occupations",
                "The occupation $f$ of the levels of the free state $N = 136$ at "
                "$a_{4,0} = 1$ (vertical axis) against their energy (horizontal axis, "
                "units of $m$, near the Fermi level) at the temperatures $T = 0.01$, "
                "$0.02$, $0.05$; dotted lines: the chemical potentials. The step from "
                "full to empty widens with the temperature, over a few $T$.")
    report("sum g f at the three temperatures", ", ".join(f"{s:.12f}" for s in sums))
    check(max(abs(s - 136.0) for s in sums) < 1e-9, "the occupations add up to N = 136",
          record="Revision/kohn_sham/reports/ks-rust-solver.json, check "
                 "thermo_N_conservation")
    '''),
    md(r"""
    ## 12. The filling convention and its sea holes

    The convention fills only the positive branch. The sea's brane band (block type
    $j = -1$, even parity, label 0) has, without interaction, exactly the energies
    $-\varepsilon_{band}(n_2)$ of the brane band of $j = +1$ (the block Hamiltonians obey
    $h_{-1} = -h_{+1}$ when $v = 0$). If the sea were treated thermally, its levels would
    carry holes with the probability $1 - f(-\varepsilon_{band}) =
    1/(1 + e^{(\mu + \varepsilon_{band})/T})$. The next cell adds up
    $4 r_3(n_2)$ times this probability over the shells $n_2 \ge 1$ of the level set and
    compares with the record's column `sea_holes_excluded` for $N = 8$ at $T = 0.05$. The
    figure shows the record's number of sea holes per particle for $N = 8$ and $136$ at
    all slices and temperatures: above about 1 percent (dotted line) the particle-only
    ensemble is outside its range of validity, and a thermal treatment of the sea
    (particle-antiparticle pairs) would be needed.
    """),
    code(r'''
    def shell_sizes(largest):
        """r3(n2): the number of whole-number vectors with n2 = |n|^2, n2 <= largest."""
        reach = math.isqrt(largest) + 1
        sizes = {}
        for x in range(-reach, reach + 1):
            for y in range(-reach, reach + 1):
                for z in range(-reach, reach + 1):
                    s = x * x + y * y + z * z
                    if s <= largest:
                        sizes[s] = sizes.get(s, 0) + 1
        return sizes


    worst_sea, mine = 0.0, {}
    for a4 in (0.0, 1.0, 2.0):
        mu, _, _, levels = states[(8, a4, 0.05)]
        band = {lv[0]: lv[4] for lv in levels
                if lv[1] == 1 and lv[2] == "even" and lv[3] == 0 and lv[0] >= 1}
        sizes = shell_sizes(max(lv[0] for lv in levels))
        holes = sum(4 * sizes[n2] / (1.0 + math.exp((mu + band[n2]) / 0.05))
                    for n2 in sizes if n2 >= 1)
        mine[a4] = holes / 8.0
        recorded = float(record[state_id(8, a4, 0.05)]["sea_holes_excluded"])
        worst_sea = max(worst_sea, abs(holes / recorded - 1.0))
    fig, ax = plt.subplots()
    plotted = []  # every value drawn, to measure their range
    for marker, n in (("o", 8), ("s", 136)):
        for colour, t in zip(PALETTE, TEMPS):
            values = [float(record[state_id(n, a, t)]["sea_holes_over_N"])
                      for a in (0.0, 0.5, 1.0, 1.5, 2.0)]
            plotted += values
            ax.plot([0, 0.5, 1, 1.5, 2], np.maximum(values, 1e-60), marker + "-",
                    color=colour, ms=6, lw=1.2,
                    markerfacecolor=colour if n == 8 else "white",
                    label=f"$N = {n}$, $T = {t}$")
    ax.plot(list(mine), list(mine.values()), "x", color="black", ms=11, mew=2,
            label="this notebook, $N = 8$, $T = 0.05$")
    ax.axhline(0.01, color="0.3", ls=":", lw=1.2, label="1 percent")
    ax.set_yscale("log")
    ax.set_ylim(1e-60, 1e4)  # the smallest recorded value is about 2e-56
    ax.set_xlabel("slice $a_{4,0}$")
    ax.set_ylabel("sea holes per particle")
    ax.set_title("Diagnostic of the filling convention ($\\lambda = 0$)")
    ax.legend(fontsize=7, ncol=2, loc="lower right")
    smallest = min(v for v in plotted if v > 0.0)  # the smallest nonzero value
    powers = int(math.log10(max(plotted) / smallest))  # whole powers of ten spanned
    save_figure(fig, "sea_holes",
                "The number of thermal holes that the excluded sea brane band would "
                "carry, per particle (vertical axis, logarithmic), for $N = 8$ (filled) "
                "and $N = 136$ (open) at $T = 0.01$, $0.02$, $0.05$ against the slice "
                "(horizontal axis), from the record; crosses: recomputed here. The values "
                f"span more than {powers} powers of ten: at low temperature and early in "
                "the history the sea is practically full. Above the dotted 1 percent "
                "line, reached late in the history at the higher temperatures, the "
                "particle-only convention is outside its range of validity.")
    report("smallest and largest sea holes per particle drawn",
           f"{smallest:.2e}, {max(plotted):.2e}")
    report("sea holes per particle, N = 8, T = 0.05, a4,0 = 0, 1, 2",
           ", ".join(f"{v:.4g}" for v in mine.values()))
    check(worst_sea < 1e-9, "the sea-hole diagnostic reproduced",
          record=f"{THERMO}, column sea_holes_excluded")
    '''),
    md(r"""
    ## 13. The interaction at finite temperature

    The last figure uses only the record: the change of the free energy caused by the
    couplings $\pm\lambda_1$, $F(\lambda) - F(0)$, for $N = 8$, $136$ and $688$ at the
    first slice and the three temperatures. The two checks: the interaction changes $F$
    by less than $0.005\,m$; and repulsion ($+\lambda_1$) raises it for $N = 136$ and
    $688$ but lowers it for $N = 8$, attraction the other way round (the zero-mode state
    $N = 8$ has no scalar density without interaction, so to first order its
    interaction energy is the exchange term $-\tfrac{1}{32}\lambda n^2$, negative for
    $\lambda > 0$).
    """),
    code(r'''
    fig, ax = plt.subplots()
    shifts = []
    by_series = {}  # (N, tag) -> the three values of F(lambda) - F(0)
    for colour, n in zip(PALETTE, (8, 136, 688)):
        for tag, style in (("lamp1", "-"), ("lamm1", "--")):
            values = [float(record[state_id(n, 0.0, t, tag)]["F"])
                      - float(record[state_id(n, 0.0, t)]["F"]) for t in TEMPS]
            shifts += values
            by_series[(n, tag)] = values
            sign = "+" if tag == "lamp1" else "-"
            ax.plot(TEMPS, values, style, marker="o", color=colour, ms=6, lw=1.5,
                    label=f"$N = {n}$, ${sign}\\lambda_1$")
    ax.set_yscale("symlog", linthresh=1e-4)
    ax.axhline(0.0, color="0.5", lw=0.8)
    ax.set_xlabel("temperature $T$ (units of $m$)")
    ax.set_ylabel("$F(\\lambda) - F(0)$ (units of $m$)")
    ax.set_title("Effect of the interaction on the free energy, $a_{4,0} = 0$")
    ax.legend(fontsize=8, ncol=2)
    save_figure(fig, "interaction_free_energy",
                "The change of the free energy caused by the couplings $+\\lambda_1$ "
                "(solid) and $-\\lambda_1$ (dashed), $F(\\lambda) - F(0)$ (vertical axis, "
                "symmetric logarithmic, units of $m$), for $N = 8$, $136$, $688$ at "
                "$a_{4,0} = 0$ against the temperature (horizontal axis), from the "
                "record. The effect is small and changes only slowly with $T$ (for "
                "$N = 688$ it grows from $0.0033\\,m$ at $T = 0.01$ to $0.0045\\,m$ at "
                "$T = 0.05$); its sign follows the sign of the coupling, the other way "
                "round for $N = 8$.")
    report("largest |F(lambda) - F(0)| at a4,0 = 0", f"{max(abs(s) for s in shifts):.4f}")
    check(max(abs(s) for s in shifts) < 0.005,
          "the interaction changes F by less than 0.005 at a4,0 = 0",
          record=f"{THERMO}, column F")
    raises = all(v > 0.0 for n in (136, 688) for v in by_series[(n, "lamp1")]) and all(
        v < 0.0 for n in (136, 688) for v in by_series[(n, "lamm1")])
    lowers8 = all(v < 0.0 for v in by_series[(8, "lamp1")]) and all(
        v > 0.0 for v in by_series[(8, "lamm1")])
    check(raises and lowers8,
          "repulsion raises F for N = 136 and 688 and lowers it for N = 8",
          record=f"{THERMO}, column F")
    '''),
    md(r"""
    ## 14. The last check

    The last cell checks that every figure file of this notebook exists and prints the
    number of checks that passed.
    """),
    code(r'''
    NAMES = ["root_conditioning", "chemical_potential", "free_energy_entropy",
             "heat_capacity", "occupations", "sea_holes", "interaction_free_energy"]
    missing = [name for number, name in enumerate(NAMES, start=1)
               if not output_file(f"{FIGURE_FOLDER}/15d_{number}_{name}.png").is_file()]
    check(missing == [], "every figure file of this notebook exists")
    all_checks_passed()
    '''),
    md(r"""
    ## 15. What this notebook showed

    - From the solver's levels alone, plain Python reproduces the chemical potential,
      energy, entropy, free energy, grand potential, heat capacity and $dN/d\mu$ of the
      free thermal states of the record (COMPUTED).
    - The solver's chemical potential lies within its rounding bound of the 40-digit
      root; the direct count in double precision could not do this, which is why the
      solver balances thermal particles against thermal holes.
    - $\mu$ starts in the middle of the gap and falls with $T$; along the deflating
      history the gaps close, so the entropy rises, the free energy falls faster and the
      heat capacity rises at lower temperatures; $-dF/dT = S$ holds.
    - The particle-only filling is a CONVENTION; late in the history at the higher
      temperatures the excluded sea would carry many holes (up to 31 per particle for
      $N = 8$), and there the convention is outside its range of validity (OPEN: a
      thermal treatment of the sea).
    - These are instantaneous states on a PRESCRIBED background, with the brane
      ASSUMED.
    """),
]

if __name__ == "__main__":
    raise SystemExit(run_builder(__file__))
