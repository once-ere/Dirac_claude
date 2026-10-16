#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
"""Builder of Notebook 22b, "The dark-sector hypotheses: what the record finds"
(textbook "Universes in Pairs", chapter 22, "Open problems and how a student could attack
them").

The notebook Revision/textbook/notebooks/22b_dark_sector.ipynb is BUILT from this file by
Revision/textbook/tools/nbkit.py (never edit the .ipynb by hand):

    python Revision/textbook/tools/nbkit.py build \
        Revision/textbook/notebooks/src/22b_dark_sector.py --date YYYY-MM-DD
    python Revision/textbook/tools/nbkit.py check \
        Revision/textbook/notebooks/src/22b_dark_sector.py

The notebook reads the committed outputs and reports of the Revision dark-sector record
for the author's metric with b4(x4) (Revision/dark_sector/dirac16complex and
Revision/dark_sector/dirac16complex00, history a4 = H x4, b4 = b4(0) e^((4/3) H x4)) and
reproduces its key numbers: the energy balance with the b4 term, the observer identities
w_eff(A) = w_eff(B) = X/E + (beta/2) Pt/E and w_eff(C) = w_eff(A) - 1 + beta/2 on the
Kohn-Sham history, the radiation-like band of the gas, its CPL tangents, the
dark-matter-like bulk band, the drifting condensate, the gas-condensate mixtures and the
models M2 to M5 of dirac16complex00 against the Unite CPL values.  Every reproduced
number is asserted against its record file and check.  No Rust is needed.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools"))
from nbkit import code, md, run_builder  # noqa: E402

FIGURES = [
    "22b_1_gas_three_definitions",
    "22b_2_bulk_and_brane_bands",
    "22b_3_condensate_ratio",
    "22b_4_mixtures_against_unite",
    "22b_5_models_against_unite",
]

D16 = "Revision/dark_sector/dirac16complex"
D00 = "Revision/dark_sector/dirac16complex00"

FACTS = {
    "id": "22b",
    "name": "22b_dark_sector",
    "title": "The dark-sector hypotheses: what the Revision record finds",
    "purpose": (
        "It reads the committed outputs and reports of the Revision dark-sector record "
        "for dirac16complex and dirac16complex00, computed for the author's metric with "
        "the function b4(x4) on the history b4 = b4(0) e^((4/3) H x4), and reproduces "
        "their key numbers: the energy balance with the b4 term, the observer identities "
        "w_eff(A) = w_eff(B) = X/E + (beta/2) Pt/E and w_eff(C) = w_eff(A) - 1 + beta/2 "
        "on the Kohn-Sham history, the radiation-like band of the Kohn-Sham gas and its "
        "CPL tangents, the dark-matter-like law of the massive bulk band, the drifting "
        "condensate, the gas and condensate mixtures, and the models M2 to M5 of "
        "dirac16complex00 against the Unite CPL values, every tuned parameter labelled "
        "CHOSEN. Every reproduced number is checked against its record file and check, "
        "and five teaching figures are drawn."
    ),
    "records": [
        [f"{D16}/outputs/eos-history.csv",
         "E, P3, Pt, w_eff and dw_eff/da4 of the 14 Kohn-Sham series with energy, 41 "
         "slices each, along the prescribed history with b4(x4)"],
        [f"{D16}/outputs/eos-summary.json",
         "the CPL tangents, the condensate, the mixtures and the scans of dirac16complex"],
        [f"{D16}/outputs/independent-free-gas.json",
         "the bulk-band and brane-band levels of the independent free-gas computation"],
        [f"{D16}/reports/derivation-checks.json",
         "the 39 exact checks of the observer identities with b4, the condensate and the "
         "mixtures"],
        [f"{D16}/reports/ks-history-run.json",
         "the 7 checks of the 615 Kohn-Sham solver runs along the prescribed history"],
        [f"{D16}/reports/eos-checks.json",
         "the 15 checks of the equation of state of the Kohn-Sham gas"],
        [f"{D16}/reports/independent-checks.json",
         "the 10 checks of the independent free-gas computation"],
        [f"{D00}/eos-theory.json",
         "the models M1 to M5 of dirac16complex00, their parameters and the Unite "
         "values"],
        [f"{D00}/results/independent-numerics.json",
         "the field-equation runs of implementation B"],
        [f"{D00}/reports/python-derive-eos.json",
         "the 49 checks of implementation A of dirac16complex00"],
        [f"{D00}/reports/python-independent-numerics.json",
         "the 32 checks of implementation B of dirac16complex00"],
        ["Revision/dark_sector/reports/wolfram-dark-sector-b4.json",
         "the 8 checks of the independent Wolfram verification with b4"],
    ],
    "packages": ["numpy", "matplotlib"],
    "needs_rust": [],
    "expected_seconds": 15,
    "timeout_seconds": 300,
    "files_written": ["Revision/textbook/figures/22b.captions.json"]
    + [f"Revision/textbook/figures/{name}.png" for name in FIGURES],
    "final_lines": [
        "PASS every figure file of this notebook exists",
        "ALL 35 CHECKS PASSED (notebook 22b)",
    ],
    "troubleshooting": [],
}

CELLS = [
    md(r"""
    ## 1. What this notebook computes

    The author asked that two hypotheses be investigated: that dirac16complex
    (Hypothesis) and dirac16complex00 (Hypothesis00) provide a possible physical
    mechanism for a time-varying dark-energy and/or dark-matter equation of state. The
    Revision record has investigated them for the author's metric with the function
    $b_4(x_4)$, in the folders `Revision/dark_sector/dirac16complex` and
    `Revision/dark_sector/dirac16complex00`. This notebook reads the committed outputs
    and reports of that record and reproduces its key numbers, each one checked against
    its record file and check:

    - the energy balance $dE/da_4 = -3X - \frac{3}{2}\beta P_t$ with the $b_4$ term, and
      the observer identities $w_{\rm eff}(A) = w_{\rm eff}(B) = X/E + \frac{\beta}{2}P_t/E$
      and $w_{\rm eff}(C) = w_{\rm eff}(A) - 1 + \frac{\beta}{2}$, tested on the computed
      Kohn-Sham history ($\beta = 4/3$);
    - the Kohn-Sham gas of dirac16complex: radiation-like, $w_{\rm eff}(A)$ rising toward
      $1/3$, close to 0 under C, and its CPL tangents (small, thawing sign);
    - the massive bulk band, which shows the dark-matter-like fall from about $1/3$
      toward 0, and the brane band, which does not;
    - the condensate: its ratio $p/\rho = u/(2 + u)$ with $u = \lambda S/m$, the value of
      $u$ CHOSEN to give the Unite constant $w = -0.764$ at one instant, and its drift;
    - mixtures of the gas with a condensate: never the Unite values;
    - the models M2 to M5 of dirac16complex00 on the history with $b_4(x_4)$: their
      tangents and fits against the Unite CPL line, the bound $-1/3$ of positive-energy
      models, and the ghost-like component the Unite $w_0$ would need.

    It draws five figures and needs no Rust. Units: $H = m = 1$, as in the record.
    """),
    md(r"""
    ## 3. The words used in this notebook

    - **Equation of state** $w$: a pressure divided by an energy density. **Observer**:
      someone who, like us, measures only the three space directions $x_1, x_2, x_3$
      and the time $x_4$.
    - **$b_4$, $\beta$**: $b_4(x_4)$ is the second metric function of the author's metric,
      a factor of the three extra-time entries; it is a function of $x_4$, never 1.
      $\beta = d\ln b_4/da_4$; on the history of the record $\beta = 4/3$.
    - **$\rho_4$**: the energy density that this observer assigns to 3-space. It is NOT
      fixed by the field equations; the record states three definitions: (A) the extra
      times are closed with a fixed coordinate period, $\rho_4 \propto E e^{-3a_4}$;
      (B) $\rho_4$ per unit extra-time coordinate volume, $\rho_4 \propto E e^{-3a_4}$;
      (C) $\rho_4$ per unit proper 7-volume, $\rho_4 \propto E b_4^{-3/2}$. This is an
      ASSUMPTION about the observer.
    - **$E, P_3, P_t$**: the energy and the integrated pressures of 3-space and of the
      extra times of one state; **$X = P_3 - P_t$**.
    - **$w_{\rm eff}$**: the equation of state the observer infers from how fast
      $\rho_4$ thins out, $w_{\rm eff} = -1 - \frac{1}{3}\,d\ln\rho_4/d\ln a$, with the
      observer's scale factor $a = e^{a_4 - a_{4,\rm today}}$.
    - **Radiation-like**: $w_{\rm eff} = 1/3$; **dust-like** (dark-matter-like):
      $w_{\rm eff} = 0$; **cosmological-constant-like**: $w = -1$; **phantom**:
      $w < -1$.
    - **CPL**: $w(a) = w_0 + w_a(1 - a)$. **Tangent**: $w_0 = w(1)$ and
      $w_a = -dw/da$ at $a = 1$. **Fit**: the least-squares straight line in $1 - a$
      over a range of $a$. **Thawing**: $w_a < 0$; **freezing**: $w_a > 0$.
    - **Unite values**: the supernova fits quoted by the record, $w = -0.764$ (constant
      $w$) and $(w_0, w_a) = (-0.861, -0.60)$.
    - **CHOSEN**: a parameter fixed so that a model reproduces a Unite number; that
      number is then an input, NOT a prediction.
    - **Ghost-like component**: a component of negative classical energy.
    """),
    md(r"""
    ## 4. The physical and mathematical situation

    The author's metric has the 3-space scale factor $e^{a_4}\sin^{1/6}z$ and the
    extra-time scale factor $e^{-a_4}b_4^{1/2}\sin^{1/6}z$. The record's history is
    $a_4 = Hx_4$ and $b_4 = b_4(0)\,e^{(4/3)Hx_4}$ (the branch that the author's Lovelock
    weights allow for a source without a mixed $x_4 x_0$ component), so
    $\beta = d\ln b_4/da_4 = 4/3$ and the extra times still deflate, like $e^{-a_4/3}$. The
    proper 7-volume element is $b_4^{3/2}\cos z$, and for a homogeneous source the
    conservation law gives exactly (record `derivation-checks.json`)
    $$\frac{dE}{da_4} = -3X - \frac{3}{2}\beta P_t, \qquad X = P_3 - P_t .$$
    With $\rho_4 \propto E e^{-3a_4}(e^{-3a_4}b_4^{3/2})^{-s}$ ($s = 0$ for A and B,
    $s = 1$ for C) and $d\ln a = da_4$:
    $$w_{\rm eff} = \frac{X}{E} - s + \frac{\beta}{2}\Big(\frac{P_t}{E} + s\Big) .$$
    On the history the definitions differ by $1 - \beta/2 = 1/3$. The Kohn-Sham states are
    instantaneous ground states along this PRESCRIBED BACKGROUND (a test field without
    back-reaction), with the ASSUMED Z2 brane, solved at the coupling
    $\hat\lambda e^{-2a_4}$ that $b_4$ implies. The models of dirac16complex00 are
    adiabatic (WKB) gases of plane-wave modes, an APPROXIMATION that the record measures
    with a second implementation.
    """),
    md(r"""
    ## 5. The records

    The next cell loads the modules, reads the seven check reports of the dark-sector
    record and checks that every one of their checks is PASS, then reads the table of
    the Kohn-Sham history and the four output files whose numbers the later cells
    reproduce.
    """),
    code(r'''
    import csv  # reads the CSV tables of the Revision record
    from fractions import Fraction  # exact fractions such as -382/441

    import numpy as np  # arrays of numbers and their arithmetic

    D16 = "Revision/dark_sector/dirac16complex"  # the record of dirac16complex
    D00 = "Revision/dark_sector/dirac16complex00"  # the record of dirac16complex00
    BETA = 4 / 3  # d ln b4/d a4 on the history b4 = b4(0) e^((4/3) a4)
    PALETTE = ["#2a78d6", "#eb6834", "#1baf7a", "#eda100", "#e87ba4", "#008300",
               "#4a3aa7", "#e34948"]  # the colours of the figures, in a fixed order


    def read_json(relative):
        """Read a JSON record of the repository into a Python dictionary."""
        return json.loads(repository_file(relative).read_text(encoding="utf-8"))


    REPORTS = {"derive": f"{D16}/reports/derivation-checks.json",
               "history": f"{D16}/reports/ks-history-run.json",
               "eos": f"{D16}/reports/eos-checks.json",
               "independent": f"{D16}/reports/independent-checks.json",
               "derive00": f"{D00}/reports/python-derive-eos.json",
               "numerics00": f"{D00}/reports/python-independent-numerics.json",
               "wolfram": "Revision/dark_sector/reports/wolfram-dark-sector-b4.json"}
    EXPECTED = {"derive": 39, "history": 7, "eos": 15, "independent": 10,
                "derive00": 49, "numerics00": 32, "wolfram": 8}  # checks per report
    for key, relative in REPORTS.items():
        entries = read_json(relative)["checks"]
        passed = [entry for entry in entries if entry["verdict"] == "PASS"]
        say(f"{relative}: {len(passed)} of {len(entries)} checks PASS")
        check(len(passed) == len(entries) == EXPECTED[key],
              f"all {EXPECTED[key]} checks of the report {key} are PASS",
              record=f"{relative}, all checks")

    with open(repository_file(f"{D16}/outputs/eos-history.csv"), newline="",
              encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    COLUMNS = ["N", "a4", "E", "P3", "Pt", "dw_eff_da4"]
    SERIES = {}  # series name -> {column name: numpy array over the slices}
    for name in sorted({row["series"] for row in rows}):
        mine = [row for row in rows if row["series"] == name]
        SERIES[name] = {column: np.array([float(row[column]) for row in mine])
                        for column in COLUMNS}
    GAS = [name for name in SERIES if SERIES[name]["N"][0] in (136, 688)]
    summary = read_json(f"{D16}/outputs/eos-summary.json")
    free_gas = read_json(f"{D16}/outputs/independent-free-gas.json")
    theory00 = read_json(f"{D00}/eos-theory.json")
    numerics00 = read_json(f"{D00}/results/independent-numerics.json")
    say(f"{len(rows)} rows read: {len(SERIES)} series, {len(GAS)} of them with "
        "N = 136 or 688")
    check(all(len(SERIES[name]["a4"]) == 41 for name in SERIES)
          and all(np.all(np.diff(SERIES[name]["a4"]) > 0) for name in SERIES),
          "every series has 41 slices in increasing order of a4")
    '''),
    md(r"""
    ## 6. The observer's equation of state on the Kohn-Sham gas

    The next cell tests the energy balance $dE/da_4 = -3X - \frac{3}{2}\beta P_t$ on the
    computed history (fourth-order differences of $E$ against $X$ and $P_t$ from the
    solver's integrals) and shows that the law without the $b_4$ term fails. It then
    computes $w_{\rm eff}$ directly from its definition, by differentiating
    $\ln\rho_4$ for the definitions A, B and C, and compares with the identities. It
    checks the band of $w_{\rm eff}(A)$ over all gas series, that it rises with $a_4$,
    and the zero modes of $N = 8$, and draws the histories (Figure 1).
    """),
    code(r'''
    def w_eff_A(name):
        """w_eff(A) = (X + (beta/2) Pt)/E of one series at its 41 slices."""
        s = SERIES[name]
        return (s["P3"] - s["Pt"] + 0.5 * BETA * s["Pt"]) / s["E"]


    gas = SERIES["N688_lam0"]  # the gas of N = 688 quanta with lambda = 0
    a4, E = gas["a4"], gas["E"]
    X = gas["P3"] - gas["Pt"]
    h = a4[1] - a4[0]  # the step 0.05 between two slices


    def derivative(f):
        """df/da4 at the slices 2 to 38: fourth-order central differences."""
        return (f[:-4] - 8 * f[1:-3] + 8 * f[3:-1] - f[4:]) / (12 * h)


    worst, worst_without = 0.0, 0.0  # largest relative violations, with and without b4
    for name, s in SERIES.items():
        X_n, Pt_n, scale = s["P3"] - s["Pt"], s["Pt"], np.max(np.abs(s["E"]))
        rate = derivative(s["E"])
        with_b4 = rate + 3 * X_n[2:-2] + 1.5 * BETA * Pt_n[2:-2]
        worst = max(worst, np.max(np.abs(with_b4)) / scale)
        if not name.endswith("lam0"):  # the interacting series have Pt != 0
            without = rate + 3 * X_n[2:-2]
            worst_without = max(worst_without, np.max(np.abs(without)) / scale)
    report("largest |dE/da4 + 3X + 2Pt|/max|E| over the 14 series", f"{worst:.3e}")
    report("largest |dE/da4 + 3X|/max|E| over the interacting series",
           f"{worst_without:.3e}")
    check(f"{worst:.3e}" == "6.351e-06",
          "the energy balance dE/da4 = -3X - 2Pt on the data",
          record=f"{D16}/reports/eos-checks.json, check conservation_with_b4_term")
    check(f"{worst_without:.3e}" == "1.630e+00",
          "the law dE/da4 = -3X without the b4 term fails",
          record=f"{D16}/reports/eos-checks.json, "
                 "check conservation_without_b4_term_fails")

    error = 0.0  # the largest |w_eff from the dilution - w_eff from the identity|
    for name, s in SERIES.items():
        rho4_AB = np.abs(s["E"]) * np.exp(-3 * s["a4"])  # A and B: E e^(-3 a4)
        rho4_C = np.abs(s["E"]) * np.exp(-1.5 * BETA * s["a4"])  # C: E b4^(-3/2)
        w_AB = -1 - derivative(np.log(rho4_AB)) / 3  # -1 - (1/3) d ln rho4/d ln a
        w_C = -1 - derivative(np.log(rho4_C)) / 3
        identity = w_eff_A(name)[2:-2]
        error = max(error, np.max(np.abs(w_AB - identity)),
                    np.max(np.abs(w_C - (identity - 1 + BETA / 2))))
    report("largest difference between dilution and identity", f"{error:.1e}")
    check(error < 1e-6, "w_eff(A) = w_eff(B) = X/E + (2/3) Pt/E and "
          "w_eff(C) = w_eff(A) - 1/3 on the data of all 14 series",
          record=f"{D16}/reports/derivation-checks.json, checks "
                 "w_eff_A_b4 and w_eff_C_b4")

    band = np.concatenate([w_eff_A(name) for name in GAS])
    report("w_eff(A) of N688_lam0 at a4 = 0 and a4 = 2", f"{X[0] / E[0]:.4f}, "
           f"{X[-1] / E[-1]:.4f}")
    report("w_eff(A) over all gas series, smallest and largest",
           f"{band.min():.6f}, {band.max():.6f}")
    report("w_eff(C) over all gas series, smallest and largest",
           f"{band.min() - 1 / 3:.6f}, {band.max() - 1 / 3:.6f}")
    check(f"{band.min():.6f}" == "0.292903" and f"{band.max():.6f}" == "0.326429",
          "the gas is radiation-like: w_eff(A) in [0.292903, 0.326429]",
          record=f"{D16}/reports/eos-checks.json, check gas_radiation_like_band")
    check(all(np.all(np.diff(w_eff_A(name)) > 0) for name in GAS),
          "w_eff(A) rises with a4 in every gas series (toward 1/3, not toward 0)",
          record=f"{D16}/reports/eos-checks.json, "
                 "check gas_X_over_E_rises_toward_one_third")

    ZERO = [name for name in SERIES if name.startswith("N8_")]  # interacting, N = 8
    falls = [SERIES[name]["E"][-1] / SERIES[name]["E"][0] for name in ZERO]
    pt_e = np.concatenate([SERIES[name]["Pt"] / SERIES[name]["E"] for name in ZERO])
    report("N = 8, lambda != 0: E(2)/E(0), smallest and largest",
           f"{min(falls):.6f}, {max(falls):.6f}")
    check(all(np.max(np.abs(SERIES[name]["P3"] - SERIES[name]["Pt"]))
              <= 1e-12 * np.max(np.abs(SERIES[name]["E"])) for name in ZERO)
          and f"{min(falls):.6f}" == "0.018402" and f"{max(falls):.6f}" == "0.019031"
          and f"{pt_e.min():.6f}" == "0.931316" and f"{pt_e.max():.6f}" == "0.999997",
          "the zero modes of N = 8 have X = 0 and E falling almost like e^(-2 a4)",
          record=f"{D16}/reports/eos-checks.json, "
                 "check n8_interacting_zero_modes_dilute_with_b4")

    fig, (left, right) = plt.subplots(1, 2, figsize=(9.0, 3.8))
    for colour, name in zip(PALETTE, ["N136_lam0", "N688_lam0", "N688_lamp2"]):
        left.plot(SERIES[name]["a4"], w_eff_A(name), color=colour, label=name)
        right.plot(SERIES[name]["a4"], w_eff_A(name) - 1 / 3, color=colour,
                   label=name)
    left.axhline(1 / 3, color="black", linestyle="--", linewidth=0.8,
                 label="radiation, 1/3")
    right.axhline(0.0, color="black", linestyle="--", linewidth=0.8,
                  label="1/3 - 1/3 = 0")
    right.axhline(-0.861, color=PALETTE[7], linestyle=":", linewidth=1.0,
                  label="Unite $w_0 = -0.861$")
    right.set_ylim(-1.0, 0.1)
    left.set_title("A and B: $w_{eff} = X/E + (2/3)P_t/E$")
    right.set_title("C: $w_{eff} = w_{eff}(A) - 1/3$")
    for ax in (left, right):
        ax.set_xlabel("$a_4$ along the prescribed history")
        ax.legend(fontsize=8)
    left.set_ylabel("$w_{eff}$")
    save_figure(fig, "gas_three_definitions",
                "The equation of state $w_{eff}$ that a 3-space observer infers from "
                "the thinning of the Kohn-Sham gas of dirac16complex along the "
                "prescribed history with $b_4 = b_4(0)e^{(4/3)a_4}$, for three "
                "recorded series; horizontal axis $a_4$ from 0 to 2 (one unit is one "
                "e-fold of inflation of 3-space), vertical axis $w_{eff}$ (a pure "
                "number). Left, definitions A and B of the observer density: "
                "$w_{eff}$ rises from about 0.29 toward the radiation value 1/3 "
                "(dashed). Right, definition C: the same curves moved down by exactly "
                "$1 - \\beta/2 = 1/3$, between about $-0.040$ and $-0.007$, close to "
                "0 and far from the Unite $w_0 = -0.861$ (dotted). The observer "
                "assumption moves the verdict by 1/3; no definition gives dark energy.")
    '''),
    md(r"""
    ## 7. The CPL tangents of the gas

    The observer's scale factor is $a = e^{a_4 - a_{4,\rm today}}$, so at $a = 1$ the
    slope $dw/da$ equals $dw/da_4$ and the tangent is $w_0 = w(a_{4,\rm today})$,
    $w_a = -dw_{\rm eff}/da_4$. The next cell reads $dw_{\rm eff}/da_4$ from the record's
    table at the four values of $a_{4,\rm today}$ that the record uses, prints the
    tangents of the gas N688_lam0 under definition C, and checks them and the range of
    the tangents of all gas series.
    """),
    code(r'''
    TODAY = [0.5, 1.0, 1.5, 2.0]  # the four choices of a4,today of the record
    index = [int(round(t / h)) for t in TODAY]  # their positions in the slice list
    recorded = {entry["series"]: entry for entry in summary["series"]}
    w_C_gas = w_eff_A("N688_lam0") - 1 + BETA / 2  # w_eff(C) of the gas N688_lam0
    say("a4,today   w0 under C   wa (every definition)")
    differences = []
    for t, i, entry in zip(TODAY, index, recorded["N688_lam0"]["cplTangent"]):
        w0 = w_C_gas[i]  # w_eff(C) today
        wa = -gas["dw_eff_da4"][i]  # w_a = -dw/da at a = 1, and da = da4 there
        say(f"{t:8.1f}   {w0:10.4f}   {wa:12.5f}")
        differences += [abs(w0 - entry["w_eff_C"]["w0"]), abs(wa - entry["w_eff_C"]["wa"])]
    check(max(differences) < 1e-12, "the CPL tangents of N688_lam0",
          record=f"{D16}/outputs/eos-summary.json, key cplTangent of N688_lam0")

    tangents = [-SERIES[name]["dw_eff_da4"][i] for name in GAS for i in index]
    report("tangent wa of every gas series, smallest and largest",
           f"{min(tangents):.6f}, {max(tangents):.6f}")
    check(f"{min(tangents):.6f}" == "-0.017766" and f"{max(tangents):.6f}" == "-0.009043"
          and f"{band.min() - 1 / 3:.6f}" == "-0.040430"
          and f"{band.max() - 1 / 3:.6f}" == "-0.006905",
          "every gas tangent wa is negative (thawing sign) and far below 0.60; "
          "w_eff(C) of the gas lies between -0.040430 and -0.006905",
          record=f"{D16}/reports/eos-checks.json, checks gas_cpl_thawing_sign_small "
                 "and gas_C_near_zero_on_b4_history")
    '''),
    md(r"""
    ## 8. The bulk band and the brane band

    The occupied levels of the computed ground states lie on the brane band, which is
    massless at zero 3-momentum. The record's independent free-gas computation also
    follows one level of the massive bulk band (odd brane parity) and one brane-band
    level of the same 3-momentum shell over $a_4$ from $-3$ to $4$. A free gas has no
    mean field and $P_t = 0$, so $b_4$ does not enter it. The next cell reads their
    $w_{\rm eff}(A)$, checks the dark-matter-like fall of the bulk level and the
    radiation-like value of the brane level, and draws both with the gas (Figure 2).
    """),
    code(r'''
    bulk = free_gas["bulkBand_n2_1"]  # the lowest massive (odd-parity) level, shell 1
    brane = free_gas["braneBand_n2_1"]  # the brane-band level of the same shell
    a4_band = np.array([point["a4"] for point in bulk])
    w_bulk = np.array([point["w_eff_A_B"] for point in bulk])
    w_brane = np.array([point["w_eff_A_B"] for point in brane])
    report("w_eff(A) of the bulk level at a4 = -3 and a4 = 4",
           f"{w_bulk[0]:.6f}, {w_bulk[-1]:.3e}")
    report("ratio w(4)/w(3.75) of the bulk level", f"{w_bulk[-1] / w_bulk[-2]:.6f}")
    report("w_eff(A) of the brane level, smallest and largest",
           f"{w_brane.min():.6f}, {w_brane.max():.6f}")
    check(a4_band[0] == -3 and a4_band[-1] == 4 and np.all(np.diff(w_bulk) < 0)
          and f"{w_bulk[0]:.6f}" == "0.239626" and f"{w_bulk[-1]:.3e}" == "2.268e-03",
          "the bulk level falls from 0.239626 to 2.268e-03 (dark-matter-like)",
          record=f"{D16}/reports/independent-checks.json, check bulk_band_dark_matter_law")
    check(f"{w_brane.min():.6f}" == "0.291594" and f"{w_brane.max():.6f}" == "0.333275",
          "the brane level stays between 0.291594 and 0.333275 (radiation-like)",
          record=f"{D16}/reports/independent-checks.json, check brane_band_radiation_law")

    fig, ax = plt.subplots(figsize=(7.0, 4.2))
    ax.plot(a4_band, w_bulk, "o-", color=PALETTE[1], markersize=3,
            label="bulk band (massive), one level")
    ax.plot(a4_band, w_brane, "s-", color=PALETTE[0], markersize=3,
            label="brane band (massless at k = 0), one level")
    ax.plot(a4, X / E, color=PALETTE[2], linewidth=2.5, label="the gas N688_lam0")
    ax.axhline(1 / 3, color="black", linestyle="--", linewidth=0.8)
    ax.axhline(0.0, color="black", linestyle=":", linewidth=0.8)
    ax.set_xlabel("$a_4$")
    ax.set_ylabel("$w_{eff}$ under definitions A and B")
    ax.legend(fontsize=8)
    save_figure(fig, "bulk_and_brane_bands",
                "Which quanta of dirac16complex behave like dark matter. Horizontal "
                "axis $a_4$ from $-3$ to 4, vertical axis $w_{eff}$ under definitions "
                "A and B (a pure number; a free gas has $P_t = 0$, so $b_4$ does not "
                "enter). Orange: one level of the massive bulk band "
                "falls from 0.24 toward the dust value 0 (dotted), the "
                "dark-matter-like law. Blue: a brane-band level of the same shell "
                "tends to the radiation value 1/3 (dashed). Green, thick: the computed "
                "Kohn-Sham gas, which fills only the brane band and is radiation-like. "
                "The computed ground states do not populate the bulk band.")
    '''),
    md(r"""
    ## 9. The condensate

    A homogeneous condensate is an exact solution of both fields, with
    $\rho = mS + \lambda S^2/2$ and $p_3 = p_t = p_0 = \lambda S^2/2$; with $b_4(x_4)$ its
    scalar density dilutes, $b_4^{3/2}S$ is constant. So $X = 0$ and $P_t/E$ equals its
    ratio $p/\rho = u/(2 + u)$ with $u = \lambda S/m$, and on the history
    $u \propto b_4^{-3/2} \propto e^{-2a_4}$: the ratio drifts. The next cell computes,
    with exact fractions, the value $u = -382/441$ that the record CHOSE so that the
    ratio equals $-0.764$ today, the drift $w_a = 4u/(2 + u)^2$ there, the observer's
    values, checks the phantom window and where the drifting condensate crosses $-1$
    under C, and draws the ratio and its drift (Figure 3).
    """),
    code(r'''
    u = Fraction(-382, 441)  # lambda S/m today, CHOSEN so that the ratio is -0.764
    ratio = u / (2 + u)  # p/rho = (lambda S^2/2)/(m S + lambda S^2/2) = u/(2 + u)
    drift = 4 * u / (2 + u) ** 2  # w_a = -d ratio/d a4, because du/da4 = -2u
    w_C_today = -1 + Fraction(2, 3) * (1 + ratio)  # -1 + (beta/2)(1 + ratio)
    report("the ratio u/(2 + u) at u = -382/441", f"{ratio} = {float(ratio)}")
    report("its drift wa = 4u/(2 + u)^2", f"{drift} = {float(drift)}")
    report("w_eff(C) = -1 + (2/3)(1 + ratio) and its wa",
           f"{w_C_today}, {Fraction(2, 3) * drift}")
    condensate = summary["condensate"]
    check(ratio == Fraction(-764, 1000)
          and abs(float(u) - condensate["u_for_ratio_minus_0p764_today"]) < 1e-12,
          "the condensate ratio is -0.764 at u = -382/441 (one CHOSEN parameter)",
          record=f"{D16}/reports/derivation-checks.json, "
                 "check condensate_ratio_equal_unite_constant_w")
    check(drift == Fraction(-84231, 31250)
          and abs(float(drift) - condensate["ratio_wa_at_that_u"]) < 1e-12
          and w_C_today == Fraction(-316, 375)
          and abs(float(Fraction(2, 3) * drift) - condensate["wa_A_B_C_at_that_u"]) < 1e-12,
          "with b4(x4) the ratio drifts: wa = -84231/31250, and w_eff(C) = -316/375",
          record=f"{D00}/reports/python-derive-eos.json, "
                 "check condensate_ratio_drift_at_unite_value")

    grid = np.linspace(-3.0, 1.0, 4001)
    grid = grid[np.abs(grid + 2) > 1e-9]  # leave out the pole u = -2
    below = grid / (2 + grid) < -1  # where the ratio is phantom
    check(np.array_equal(below, (grid > -2) & (grid < -1)),
          "the ratio is below -1 exactly for -2 < u < -1",
          record=f"{D00}/reports/python-derive-eos.json, "
                 "check condensate_phantom_interval")

    a_cross_squared = -u  # u(a) = u a^(-2) equals -1 where a^2 = -u
    u_there = u / a_cross_squared  # = -1: the ratio enters the phantom window
    w_C_there = -1 + Fraction(2, 3) * (1 + u_there / (2 + u_there))
    report("the drifting condensate reaches u = -1 at a",
           f"sqrt({a_cross_squared}) = {float(a_cross_squared) ** 0.5:.6f}")
    check(u_there == -1 and w_C_there == -1,
          "under C this condensate crosses w = -1 at a^2 = 382/441, toward the past")

    fig, (left, right) = plt.subplots(1, 2, figsize=(9.0, 3.8))
    for part in (grid[grid < -2], grid[grid > -2]):
        left.plot(part, part / (2 + part), color=PALETTE[0])
    left.axvspan(-2, -1, color=PALETTE[7], alpha=0.12, label="phantom, -2 < u < -1")
    left.plot([float(u)], [float(ratio)], "o", color=PALETTE[1],
              label="CHOSEN: u = -382/441")
    left.set_ylim(-4.0, 4.0)
    left.set_xlabel("$u = \\lambda S/m$")
    left.set_ylabel("ratio $p/\\rho$")
    left.legend(fontsize=8, loc="lower right")
    a_pole = float(np.sqrt(-float(u) / 2))  # u(a) = u a^(-2) reaches -2 here
    a_history = np.linspace(a_pole + 0.02, 1.5, 300)
    u_history = float(u) / a_history**2  # u ~ e^(-2 a4) = a^(-2) times its value today
    ratio_history = u_history / (2 + u_history)
    right.plot(a_history, ratio_history, color=PALETTE[0], label="ratio $p/\\rho$")
    right.plot(a_history, -1 / 3 + 2 / 3 * ratio_history, color=PALETTE[2],
               label="$w_{eff}$, definition C")
    right.axhline(-0.764, color="black", linestyle=":", linewidth=0.8,
                  label="Unite constant $w = -0.764$")
    right.axvline(1.0, color="black", linewidth=0.6)
    right.set_ylim(-4.0, 0.5)
    right.set_xlabel("observer scale factor $a$ ($a = 1$ today)")
    right.legend(fontsize=8, loc="lower right")
    save_figure(fig, "condensate_ratio",
                "The ratio $p/\\rho = u/(2 + u)$ of a homogeneous condensate. Left: "
                "against $u = \\lambda S/m$ (horizontal axis, a pure number; the ratio "
                "has a pole at $u = -2$); the orange point is the value "
                "$u = -382/441$ CHOSEN so that the ratio equals the Unite constant "
                "$w = -0.764$: one parameter for one number, not a prediction; the red "
                "band is the phantom window. Right: with $b_4(x_4)$ the condensate "
                "dilutes, $u \\propto a^{-2}$, so the ratio (blue) drifts along the "
                "observer scale factor $a$; it equals $-0.764$ (dotted) only today, "
                "$a = 1$, and falls without bound toward the past, where the "
                "condensate's energy reaches 0 at $a = 0.658$. The observer's "
                "$w_{eff}$ under C (green) is $-1/3 + (2/3)$ times the ratio; it "
                "crosses $-1$ at $a = 0.931$, where the ratio enters the phantom "
                "window.")
    '''),
    md(r"""
    ## 10. Mixtures of the gas with a condensate

    For a radiation-like gas ($X = E/3$, $P_t = 0$, $E \propto 1/a$) plus a condensate
    with $\lambda = 0$ ($X = P_t = 0$, $E$ constant for every $b_4$) with energy ratio
    $r = r_0/a$, the record derives exactly $w_{\rm eff}(A) = \frac{1}{3}r/(1 + r)$, so
    $w_0 = r_0/(3(r_0 + 1))$ and $w_a = r_0/(3(r_0 + 1)^2) > 0$, and under C
    $w_0 - 1 + \beta/2 = w_0 - 1/3 \ge -1/3$. The next cell checks this law, mixes the
    computed gas N688_lam0 with such a condensate (today $a_{4,\rm today} = 2$) for 1000
    gas shares, compares one recorded mixture, reproduces the closest point of the
    record's scans with a drifting condensate, and draws mixtures against the Unite
    line (Figure 4).
    """),
    code(r'''
    r0 = Fraction(417, 583)  # the gas/condensate energy CHOSEN on the withdrawn record
    w0_A = r0 / (3 * (r0 + 1))  # w_eff(A) today: 139/1000
    w0_C = w0_A - 1 + Fraction(2, 3)  # under C on the history: w0_A - 1/3
    wa_exact = r0 / (3 * (r0 + 1) ** 2)  # w_a of the exact law: positive (freezing)
    need = Fraction(139, 1000) - Fraction(2, 3)  # r0/(3 (1 + r0)) needed for -0.861
    report("exact law at r0 = 417/583: w0 under C and wa",
           f"{w0_C}, {float(wa_exact):.6f}")
    report("r0/(3 (1 + r0)) that w0(C) = -0.861 would need", f"{need}")
    check(w0_C == Fraction(-583, 3000) and f"{float(wa_exact):.6f}" == "0.081037"
          and need < 0,
          "radiation plus condensate: w0(C) >= -1/3, so -0.861 is not reachable",
          record=f"{D16}/reports/derivation-checks.json, "
                 "check mixture_C_matching_w0_unite_b4")


    def mixture_w_C(share):
        """w_eff(C) of the gas N688_lam0 plus a lambda = 0 condensate along the
        history; the gas has the energy share "share" today (a4 = 2)."""
        condensate_energy = E[-1] * (1 - share) / share  # constant for every b4
        return X / (E + condensate_energy) - 1 + BETA / 2


    lowest = min(float(np.min(mixture_w_C(share)))
                 for share in np.linspace(0.001, 1.0, 1000))
    report("smallest w_eff(C) over 1000 gas shares and 41 slices", f"{lowest:.6f}")
    check(f"{lowest:.6f}" == "-0.333015"
          and abs(lowest - summary["mixture_C_lambda0_condensate_min_w_eff_C"]) < 1e-12,
          "no gas share reaches -0.861 or a constant -0.764 under C",
          record=f"{D16}/reports/eos-checks.json, "
                 "check mixture_C_cannot_reach_unite_w0_with_lambda0_condensate")

    w_half = mixture_w_C(0.5)  # gas share one half today
    # w_a = -dw/da4 at a4 = 2, one-sided fourth-order differences (as the record)
    wa_half = -(3 * w_half[-5] - 16 * w_half[-4] + 36 * w_half[-3] - 48 * w_half[-2]
                + 25 * w_half[-1]) / (12 * h)
    recorded_half = [entry for entry in summary["mixtures_N688_lam0_today_a4_2"]
                     if entry["gas_fraction_today"] == 0.5][0]["w_eff_C"]
    report("gas share 0.5: w0 and wa under C", f"{w_half[-1]:.6f}, {wa_half:.6f}")
    check(abs(w_half[-1] - recorded_half["w0"]) < 1e-12
          and abs(wa_half - recorded_half["wa"]) < 1e-10 and wa_half > 0,
          "the recorded mixture with gas share 0.5 (freezing)",
          record=f"{D16}/outputs/eos-summary.json, key mixtures_N688_lam0_today_a4_2")

    w_c = Fraction(-37, 100)  # the ratio today of the record's closest point under C
    u_c = 2 * w_c / (1 - w_c)  # from w_c = u/(2 + u)
    closest_w0 = -1 + Fraction(2, 3) * (1 + w_c)
    closest_wa = Fraction(2, 3) * 4 * u_c / (2 + u_c) ** 2
    distance = float(np.hypot(float(closest_w0) + 0.861, float(closest_wa) + 0.6))
    best = summary["mixture_scan"]["C"]["closest"]
    report("closest point under C (pure drifting condensate)",
           f"({closest_w0}, {closest_wa}), distance {distance:.6f}")
    check(best["gas_fraction"] == 0.0 and best["w_c_today"] == -0.37
          and abs(float(closest_wa) - best["wa"]) < 1e-12
          and abs(distance - best["distance"]) < 1e-12,
          "no mixture with a drifting condensate comes closer than 0.291 to the Unite pair",
          record=f"{D16}/reports/eos-checks.json, check mixture_scan_three_definitions_b4")

    a_obs = np.exp(a4 - 2.0)  # the observer scale factor, a = 1 today (a4 = 2)
    fig, ax = plt.subplots(figsize=(7.0, 4.2))
    for colour, part in zip(PALETTE, [0.25, 0.5, 0.75, 1.0]):
        ax.plot(a_obs, mixture_w_C(part), color=colour,
                label=f"gas share today {part:.2f}")
    a_pure = np.linspace(float(np.sqrt(-float(u_c) / 2)) + 0.02, 1.0, 200)
    u_pure = float(u_c) / a_pure**2  # the drifting condensate of the closest point
    ax.plot(a_pure, -1 / 3 + 2 / 3 * u_pure / (2 + u_pure), color=PALETTE[6],
            linewidth=2.0, label="drifting condensate, ratio -0.37 today")
    ax.plot(a_obs, -0.861 - 0.60 * (1 - a_obs), "k--", label="Unite CPL line")
    ax.axhline(-1.0, color="black", linestyle=":", linewidth=0.8)
    ax.axhline(-1 / 3, color="grey", linestyle=":", linewidth=0.8)
    ax.set_ylim(-2.0, 0.1)
    ax.set_xlabel("observer scale factor $a = e^{a_4 - 2}$")
    ax.set_ylabel("$w_{eff}$ under definition C")
    ax.legend(fontsize=8, loc="lower right")
    save_figure(fig, "mixtures_against_unite",
                "Mixtures of the computed Kohn-Sham gas N688_lam0 with a condensate, "
                "under definition C on the history with $b_4(x_4)$, against the "
                "observer scale factor $a$ (horizontal axis, $a = 1$ today, taken at "
                "$a_4 = 2$); vertical axis $w_{eff}$ (a pure number). Each coloured "
                "curve with a $\\lambda = 0$ condensate has another gas share today; "
                "all of them lie between $-1/3$ (grey dotted) and 0. The violet curve "
                "is the drifting condensate alone with the ratio $-0.37$ today, the "
                "point of the record's scans closest to the Unite pair (distance "
                "0.291); it falls steeply toward the past. The Unite CPL line (dashed) "
                "is reached by none of them.")
    '''),
    md(r"""
    ## 11. The models M2 to M5 of dirac16complex00

    Each component of an adiabatic (WKB) gas of dirac16complex00 has an energy density
    $\rho_i$ and $\varepsilon_i = (k_p^2 + (1 - \beta/2)q_p^2)/(3\omega_i^2) \ge 0$ with
    $\omega^2 = m^2 + k_p^2 - q_p^2$, $k_p = k/a$ and $q_p = q\,a\,b_4^{-1/2} \propto
    a^{1/3}$; a mixture has $w_{\rm eff}(C) = -1 + \beta/2 + \sum_i\varepsilon_i\rho_i/
    \sum_i\rho_i \ge -1/3$ when every $\rho_i \ge 0$. The record keeps the models of the
    withdrawn $b_4 = 1$ record with their parameters (normalised to total energy 1 at
    $a = 1$): M2 a good-sector gas ($q = 0$), M3 one extra-time mode ($k = 0$), M4 a
    condensate plus an extra-time mode, M5 the same plus a GHOST-LIKE component of
    negative energy $-G/a$. The next cell rebuilds them on the history with $b_4(x_4)$,
    checks their tangents, the M5 fit, the bound $-1/3$, the absence of crossings and
    the ghost share the Unite $w_0$ would need, and draws them (Figure 5).
    """),
    code(r'''
    def model(a, components):
        """The total energy density and the sum of eps_i rho_i of a WKB model at a
        (a number or an array).  Each component is (kind, weight at a = 1, s)."""
        a = np.asarray(a, dtype=float)
        rho_total, eps_rho = np.zeros_like(a), np.zeros_like(a)
        for kind, weight, s in components:
            if kind == "condensate":  # lambda = 0: rho b4^(3/2) constant, eps = 0
                rho, eps = weight + 0 * a, 0 * a
            elif kind == "kmode":  # q = 0 and s = k^2/(k^2 + m^2) at a = 1
                r = s / (1 - s)  # k^2/m^2
                rho = weight * np.sqrt((r / a**2 + 1) / (r + 1))  # omega(a)/omega(1)
                eps = (r / a**2) / (3 * (r / a**2 + 1))
            elif kind == "qmode":  # k = 0, s = q_p^2/m^2 at a = 1, q_p^2 ~ a^(2/3)
                s_a = s * a ** (2 - BETA)
                rho = weight * np.sqrt((1 - s_a) / (1 - s))
                eps = (1 - BETA / 2) * s_a / (3 * (1 - s_a))
            else:  # "ghost": massless modes of NEGATIVE classical energy
                rho, eps = -weight / a, 1 / 3 + 0 * a
            rho_total = rho_total + rho
            eps_rho = eps_rho + eps * rho
        return rho_total, eps_rho


    def w_model(a, components):
        """w_eff under definition C: -1 + beta/2 + sum eps_i rho_i / sum rho_i."""
        rho_total, eps_rho = model(a, components)
        return eps_rho / rho_total - 1 + BETA / 2


    def tangent(components, d=1e-3):
        """CPL tangent w0 = w(1), wa = -dw/da at a = 1 (fourth-order differences)."""
        f = [float(w_model(1 + k * d, components)) for k in (-2, -1, 1, 2)]
        slope = (f[0] - 8 * f[1] + 8 * f[2] - f[3]) / (12 * d)  # dw/da at a = 1
        return float(w_model(1.0, components)), -slope


    M5_RECORD = theory00["models"]["M5_with_ghost_component"]
    G = float(Fraction(M5_RECORD["parameters"]["G"]))  # ghost share 3/10, a choice
    s5 = float(M5_RECORD["parameters"]["s"])  # CHOSEN with q5 on the withdrawn record
    q5 = float(M5_RECORD["parameters"]["Omega_q"])
    c5 = float(M5_RECORD["parameters"]["Omega_c"])
    MODELS = {"M2": [("kmode", 1.0, 417 / 1000)],  # s CHOSEN on the withdrawn record
              "M3": [("qmode", 1.0, 417 / 1417)],  # s CHOSEN on the withdrawn record
              "M4": [("condensate", 1 - 57963 / 264037, 0.0),  # both CHOSEN on the
                     ("qmode", 57963 / 264037, 264037 / 403037)],  # withdrawn record
              "M5": [("condensate", c5, 0.0), ("qmode", q5, s5), ("ghost", G, 0.0)]}
    EXACT = {"M2": (Fraction(-583, 3000), Fraction(81037, 500000)),
             "M3": (Fraction(-287, 1000), Fraction(-196963, 4500000)),
             "M4": (Fraction(-287, 1000), Fraction(-1, 15))}
    RECORD_CHECK = {"M2": "M2_tangent_exact_b4", "M3": "M3_tangent_exact_b4",
                    "M4": "M4_withdrawn_tuning_on_b4_history"}
    for name in ("M2", "M3", "M4"):
        w0, wa = tangent(MODELS[name])
        report(f"{name} tangent (w0, wa) under C", f"({w0:.6f}, {wa:.6f})")
        check(abs(w0 - float(EXACT[name][0])) < 1e-12
              and abs(wa - float(EXACT[name][1])) < 1e-8,
              f"the tangent of {name}: ({EXACT[name][0]}, {EXACT[name][1]})",
              record=f"{D00}/reports/python-derive-eos.json, check {RECORD_CHECK[name]}")

    a_fit = np.linspace(0.5, 1.0, 101)  # 101 points of a in [1/2, 1], as the record
    wa_fit, w0_fit = np.polyfit(1 - a_fit, w_model(a_fit, MODELS["M5"]), 1)
    fit_record = M5_RECORD["N2"]["fit_a_1/2_to_1"]
    report("M5 least-squares fit over a in [1/2, 1]", f"({w0_fit:.6f}, {wa_fit:.6f})")
    check(abs(w0_fit - float(fit_record["w0"])) < 1e-10
          and abs(wa_fit - float(fit_record["wa"])) < 1e-10,
          "the M5 fit, far from the Unite pair now",
          record=f"{D00}/reports/python-derive-eos.json, "
                 "check M5_withdrawn_composition_on_b4_history")

    fine = np.arange(1, 301) / 300  # a = 1/300, 2/300, ..., 1
    lowest_models = {name: float(np.min(w_model(fine, MODELS[name])))
                     for name in ("M2", "M3", "M4")}
    M4_RECORD = theory00["models"]["M4_condensate_plus_extra_time_mode"]
    report("lowest w_eff(C) of M2, M3, M4 for a = 1/300 to 1",
           ", ".join(f"{value:.12f}" for value in lowest_models.values()))
    check(all(value >= -1 / 3 for value in lowest_models.values())
          and abs(lowest_models["M4"] - float(M4_RECORD["min_w_N2_on_(0,1]"])) < 1e-11,
          "positive-energy models stay above -1 + beta/2 = -1/3",
          record=f"{D00}/reports/python-derive-eos.json, "
                 "check positive_models_bounded_by_minus_one_third")

    points = np.linspace(1 / 3, 1, 401)
    lowest_M5 = float(np.min(w_model(points, MODELS["M5"])))
    crossings_B = numerics00["models"]["M5_with_ghost_component"]["crossings_N2"]
    report("lowest w_eff(C) of M5 for a = 1/3 to 1", f"{lowest_M5:.6f}")
    check(lowest_M5 > -1 and crossings_B == 0
          and M5_RECORD["N2"]["crossings_of_minus_1_in_[1/3,1]"] == [],
          "no model crosses -1 on 1/3 <= a <= 1, M5 included (A and B)",
          record=f"{D00}/reports/python-independent-numerics.json, "
                 "check B_vs_A_M5_crossing")

    G_min = 3 * (Fraction(861, 1000) - Fraction(1, 3))  # w(1) >= -1/3 - G/3
    report("ghost share needed for w0(C) = -0.861", f"{G_min} (M5 has {Fraction(3, 10)})")
    check(G_min == Fraction(1583, 1000) and G_min / (1 + G_min) == Fraction(1583, 2583),
          "the Unite w0 would need a ghost-like share G >= 1583/1000",
          record=f"{D00}/reports/python-derive-eos.json, "
                 "check unite_w0_requires_dominant_ghost")

    a_plot = np.linspace(1 / 3, 1.0, 300)
    fig, (left, right) = plt.subplots(1, 2, figsize=(9.0, 3.8))
    LABELS = {"M2": "M2, gas", "M3": "M3, extra-time mode", "M4": "M4",
              "M5": "M5 (ghost-like part)"}
    for colour, name in zip(PALETTE, MODELS):
        left.plot(a_plot, w_model(a_plot, MODELS[name]), color=colour,
                  label=LABELS[name])
    left.plot(a_plot, -0.861 - 0.60 * (1 - a_plot), "k--", label="Unite CPL line")
    left.axhline(-1.0, color="black", linestyle=":", linewidth=0.8)
    left.axhline(-1 / 3, color="grey", linestyle=":", linewidth=0.8)
    left.set_xlabel("observer scale factor $a$")
    left.set_ylabel("$w_{eff}$ under definition C")
    left.legend(fontsize=7)
    PARTS = [("condensate", MODELS["M5"][0]), ("extra-time mode", MODELS["M5"][1]),
             ("ghost-like part", MODELS["M5"][2])]
    for colour, (label, component) in zip(PALETTE[4:], PARTS):
        right.plot(a_plot, model(a_plot, [component])[0], color=colour, label=label)
    right.plot(a_plot, model(a_plot, MODELS["M5"])[0], "k-", label="total")
    right.axhline(0.0, color="black", linewidth=0.6)
    right.set_xlabel("observer scale factor $a$")
    right.set_ylabel("energy density, M5")
    right.legend(fontsize=7)
    fig.subplots_adjust(wspace=0.3)  # room between the two panels
    save_figure(fig, "models_against_unite",
                "The models of dirac16complex00 under definition C on the history "
                "with $b_4 \\propto a^{4/3}$, against the observer scale factor $a$ "
                "from 1/3 to 1 (horizontal axes); their parameters are those CHOSEN "
                "on the withdrawn $b_4 = 1$ record. Left: $w_{eff}$ (a pure number) of "
                "M2 to M5, the Unite CPL line (dashed), $-1$ (black dotted) and the "
                "bound $-1/3$ of positive-energy content (grey dotted). M2, M3 and M4 "
                "stay above $-1/3$; M5, with its ghost-like part, dips below it toward "
                "the past but stays far above $-1$. No model comes near the Unite line "
                "and none crosses $-1$. Right: the energy densities of the three parts "
                "of M5 (total 1 at $a = 1$); the ghost-like part is negative, "
                "$-0.3/a$.")
    '''),
    md(r"""
    ## 12. The comparison with the Unite values

    The next cell prints, for each Unite value, what the record finds on the history
    with $b_4(x_4)$, checks the Unite values and the scale factor at which their CPL line
    crosses $-1$, and checks that every figure file exists.
    """),
    code(r'''
    unite = theory00["models"]["unite"]
    w0_u, wa_u = Fraction(unite["w0"]), Fraction(unite["wa"])
    crossing_u = 1 + (1 + w0_u) / wa_u  # w0 + wa (1 - a) = -1 solved for a
    TABLE = [("w = -0.764", "condensate ratio at u = -382/441, one instant (drifts)"),
             ("w0 = -0.861", "not reached under C without a ghost share G >= 1.583"),
             ("(w0, wa) = (-0.861, -0.60)", "not reached; closest scan point 0.291"),
             ("crossing of -1, a = 0.7683",
              "no Kohn-Sham state, no model M2 to M5; a drifting lambda < 0 "
              "condensate does (a = 0.9307 for u = -382/441 today)")]
    say("Unite value | what the record finds with b4(x4)")
    for row in TABLE:
        say(" | ".join(row))
    report("the Unite CPL line crosses w = -1 at a", f"{crossing_u}")
    check(w0_u == Fraction(-861, 1000) and wa_u == Fraction(-3, 5)
          and crossing_u == Fraction(unite["crossing_of_minus_1"]["a"])
          and crossing_u == Fraction(461, 600),
          "the Unite values and their crossing a = 461/600",
          record=f"{D00}/reports/python-derive-eos.json, check unite_crossing_point")
    files = [f"{FIGURE_FOLDER}/{NOTEBOOK_ID}_{number}_{name}.png"
             for name, number in FIGURE_NUMBERS.items()]
    check(len(files) == 5 and all(output_file(path).is_file() for path in files),
          "every figure file of this notebook exists")
    all_checks_passed()
    '''),
    md(r"""
    ## 13. What this notebook showed

    - The observer's density $\rho_4$ is an ASSUMPTION. On the computed history with
      $b_4(x_4)$ the dilution gives exactly $w_{\rm eff} = X/E + \frac{2}{3}P_t/E$ under A
      and B and that minus $1/3$ under C; the energy balance needs the $b_4$ term.
    - The Kohn-Sham gas of dirac16complex is radiation-like: $w_{\rm eff}(A)$ between
      0.292903 and 0.326429, rising toward $1/3$; under C it lies between $-0.040430$ and
      $-0.006905$, close to 0, with small tangent slopes of thawing sign ($w_a$ between
      $-0.017766$ and $-0.009043$), far from the Unite values.
    - The dark-matter-like fall from about $1/3$ toward 0 belongs to the massive bulk
      band (0.239626 to 0.002268), which the computed ground states do not populate.
    - A condensate has the ratio $-0.764$ only at the CHOSEN $u = -382/441$ and only at
      one instant: with $b_4(x_4)$ it drifts, $w_a = -84231/31250$, and under C it
      crosses $-1$ toward the past at $a = 0.9307$, where its ratio enters the phantom
      window. Mixtures with a $\lambda = 0$ condensate stay above $-1/3$ under C; the
      scans with a drifting condensate never come closer than 0.291 to the Unite pair.
    - The dirac16complex00 models, with the parameters CHOSEN on the withdrawn record,
      no longer reproduce the Unite tangent or fit; positive-energy content stays above
      $-1/3$, no model crosses $-1$, and the Unite $w_0$ would need a ghost-like share
      $G \ge 1583/1000$.
    - OPEN: which $\rho_4$ describes a real observer; a self-consistent history with an
      admissible source (the record's history needs a constant source that neither the
      gas nor a condensate supplies); populated bulk-band or thermal states; a fit to
      supernova data.
    """),
]

if __name__ == "__main__":
    raise SystemExit(run_builder(__file__))
