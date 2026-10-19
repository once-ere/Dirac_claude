#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
"""Builder of Notebook 12b, "The source that the exponential histories require".

Textbook "Universes in Pairs", chapter 12 (the field equations for a4 and b4: Einstein and
Einstein-Lovelock).  The notebook Revision/textbook/notebooks/12b_required_source.ipynb is
BUILT from this file by Revision/textbook/tools/nbkit.py (never edit the .ipynb by hand):

    python Revision/textbook/tools/nbkit.py build \
        Revision/textbook/notebooks/src/12b_required_source.py --date YYYY-MM-DD
    python Revision/textbook/tools/nbkit.py check \
        Revision/textbook/notebooks/src/12b_required_source.py

It reads the Lovelock components of the Revision record
Revision/field_equations_a4/a4-equations.json (the corrected metric of 2026-10-16), derives
the source that every exponential history a4 = A H x4 + a0, b4 = b4(0) e^(beta A H x4)
requires, and explores it with plots versus the time, A, beta, alpha_2 and Lambda.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools"))
from nbkit import code, md, run_builder  # noqa: E402

FACTS = {
    "id": "12b",
    "name": "12b_required_source",
    "title": "The source that the exponential histories a4 = A H x4, b4 = e^(beta A H x4) "
             "require",
    "purpose": (
        "It reads the Lovelock components of the field equations for a4 and b4 of the "
        "corrected metric from the Revision record, derives the energy density and the "
        "pressures that every exponential history requires for every slope A, every "
        "ratio beta, every cosmological constant and every Lovelock coupling, follows "
        "the source of the record history a4 = H x4, b4 = e^(4 H x4/3) in Einstein "
        "gravity and with the author's weights, checks the symmetry A to minus A, the "
        "two null energy conditions, the Einstein-Gauss-Bonnet and the author's-weights "
        "vacua and the conditions on a homogeneous condensate of dirac16complex00, "
        "compares every result with the Revision records, and draws eight teaching "
        "plots."
    ),
    "records": [
        ["Revision/field_equations_a4/a4-equations.json",
         "the Lovelock components, the exponential-history formulas and the condensate "
         "statements of the a4 and b4 record"],
        ["Revision/field_equations_a4/reports/python-a4-report.json",
         "the sympy checks of the a4 and b4 record that the notebook reproduces"],
        ["Revision/field_equations_a4/reports/wolfram-a4-report.json",
         "the Wolfram checks of the a4 and b4 record that the notebook reproduces"],
        ["Revision/lead_checks/reports/einstein-gauss-bonnet-a4.json",
         "the independent Einstein checks that the notebook reproduces"],
        ["Revision/metric_warped/results/warped-metric.json",
         "the source of the record history written by the record of the corrected "
         "metric"],
        ["Revision/metric_warped/reports/wolfram-warped-metric-report.json",
         "the Wolfram check of that source that the notebook reproduces"],
        ["Revision/field_equations_a4/reports/ks-source-conditions.json",
         "the energy densities that the record history needs at five slices, reproduced"],
        ["Revision/field_equations_a4/ks_source/reports/ks-source-a4.json",
         "the record of where that energy density changes sign, reproduced"],
        ["Revision/dark_sector/dirac16complex00/reports/python-derive-eos.json",
         "the record that no condensate is the source of the record history"],
    ],
    "packages": ["numpy", "sympy", "matplotlib"],
    "needs_rust": [],
    "expected_seconds": 15,
    "timeout_seconds": 600,
    "files_written": [
        "Revision/textbook/figures/12b.captions.json",
        "Revision/textbook/figures/12b_1_einstein_source.png",
        "Revision/textbook/figures/12b_2_sign_symmetry.png",
        "Revision/textbook/figures/12b_3_beta_scan.png",
        "Revision/textbook/figures/12b_4_author_weights_source.png",
        "Revision/textbook/figures/12b_5_null_energy_map.png",
        "Revision/textbook/figures/12b_6_gauss_bonnet_vacuum.png",
        "Revision/textbook/figures/12b_7_author_weights_no_vacuum.png",
        "Revision/textbook/figures/12b_8_condensate_conditions.png",
    ],
    "final_lines": [
        "PASS all eight figure files exist",
        "ALL 23 CHECKS PASSED (notebook 12b)",
    ],
    "troubleshooting": [
        ["\"FileNotFoundError\" naming a4-equations.json",
         "the notebook reads the Revision record of the repository. Run it inside the "
         "folder Revision/textbook/notebooks of a complete copy of the repository made "
         "with git clone, not on a copy of the notebook file alone."],
    ],
}

CELLS = [
    md(r"""
    ## 1. What this notebook computes

    The author's corrected metric contains two unknown functions of the time,
    $a_4(x_4)$ and $b_4(x_4)$. The simplest choices are the **exponential histories**
    $a_4 = AHx_4 + a_0$, $b_4 = b_4(0)e^{\beta AHx_4}$: 3-space grows like
    $e^{AHx_4}$, and the hidden direction and the three extra times share the scale
    factor $e^{-a_4}b_4^{1/2} \propto e^{-(1 - \beta/2)AHx_4}$, which shrinks
    (deflates) when $A > 0$ and $\beta < 2$. The **record history** of the Revision
    record is $A = 1$, $\beta = 4/3$, $b_4(0) = 1$. The field equations then say exactly
    what source (energy density $\rho$ and pressures $p_3$, $p_0 = p_t$) must be
    present. This notebook

    - reads the Lovelock tensors from the Revision record and derives from them the
      required $\kappa\rho$, $\kappa p_3$ and $\kappa p_0 = \kappa p_t$ for every $A$,
      $\beta$, cosmological constant $\Lambda$ and Lovelock couplings, and compares
      them with the record;
    - shows that, as functions of $k = e^{2a_4}/b_4$, they contain $A$ only through
      $A^2$ (the sign of $A$ is a choice);
    - follows the source of the record history in Einstein gravity and with the
      author's weights, where the energy density changes sign;
    - shows that in Einstein gravity no exponential history has a source that
      satisfies both null energy conditions;
    - finds the Einstein-Gauss-Bonnet vacua and shows that the author's weights allow
      none;
    - states what a homogeneous condensate of dirac16complex00 would need to be the
      source;
    - draws eight teaching plots.
    """),
    md(r"""
    ## 3. The words used in this notebook

    - **Exponential history**: $a_4 = AHx_4 + a_0$, $b_4 = b_4(0)e^{\beta AHx_4}$ with
      constants $A$ (the **slope**), $\beta$ and $a_0$; then $a_4' = AH$,
      $u = b_4'/b_4 = \beta AH$, $a_4'' = v = 0$, and
      $k = e^{2a_4}/b_4 = k_0e^{(2 - \beta)AHx_4}$ changes in time unless $\beta = 2$
      or $A = 0$.
    - **Record history**: $A = 1$, $\beta = 4/3$, $a_0 = 0$, $b_4(0) = 1$, so
      $k = e^{(2/3)Hx_4}$; the scale factor of the hidden direction and of the extra
      times is $e^{-a_4}b_4^{1/2} = e^{-Hx_4/3}$.
    - **Source**: the matter whose energy-momentum tensor stands on the right-hand side
      of the field equations: energy density $\rho$, pressures $p_0$ (hidden direction),
      $p_3$ (3-space), $p_t$ (extra times). The corrected metric needs $p_0 = p_t$.
    - **Required source**: the $\rho$, $p_3$, $p_0$ that the field equations demand for
      a given history; we read them off the equations instead of assuming a kind of
      matter.
    - **Couplings**: $\alpha_1$ (Einstein), $\alpha_2$ (Gauss-Bonnet), $\alpha_3$ (third
      order); **Einstein gravity** is $\alpha_1 = 1$, $\alpha_2 = \alpha_3 = 0$; the
      **author's weights** are $\alpha_k = w_k/H^{2k}$, $w = (1, \tfrac1{32},
      \tfrac1{1152})$, with $\Lambda = -10$ in the record's convention; $\Lambda$ is the
      cosmological constant, $\kappa > 0$ the strength of gravity.
    - **Units**: the plots use $H = 1$ and $\kappa = 1$, so $\kappa\rho$, $\kappa p$
      and $\Lambda$ are in units of $H^2$.
    - **Null energy condition** (NEC) along a null direction: along $x_4 + x_0$ it is
      $\rho + p_0 \ge 0$, along $x_4 + x_1$ it is $\rho + p_3 \ge 0$. Ordinary matter
      satisfies both.
    - **Vacuum**: $\rho = p_3 = p_0 = 0$, no source at all.
    - **Condensate**: a configuration of the field dirac16complex00 that depends only on
      the time $x_4$; its source has equal pressures, $p_3 = p_t = p_0$.
    - **Status labels**: PROVED (an exact identity, checked here and in the record),
      ASSUMED (a choice made, not derived), OPEN (not established).
    """),
    md(r"""
    ## 4. The physical and mathematical situation

    For a source that does not depend on $x_0$ and has no mixed component, the
    Einstein-Lovelock field equations of the corrected metric reduce to three
    equations (the Revision record `a4-equations.json`):

    $$\sum_k \alpha_k E_{(k)}{}^{x_4}{}_{x_4} + \Lambda = -\kappa\rho,\qquad
    \sum_k \alpha_k E_{(k)}{}^{x_1}{}_{x_1} + \Lambda = \kappa p_3,\qquad
    \sum_k \alpha_k E_{(k)}{}^{x_0}{}_{x_0} + \Lambda = \kappa p_0 = \kappa p_t .$$

    Every component is a polynomial in $H$, $a_4'$, $a_4''$, $u$, $v$ and $k$. On an
    exponential history only $A$, $\beta$, $H$, $k$ and the couplings remain. The
    equations allow ANY history; what they fix is the source that this history needs.
    Whether a field supplies that source is a separate question (section 11 states
    what is known for one case).
    """),
    md(r"""
    ## 5. The Revision records this notebook reproduces

    The next cell defines the helpers that read the Revision records: `read_json`
    reads a JSON file of the repository, `record_verdict` finds a check by its name in
    a report, and `reproduces` is a check that passes only when this notebook's own
    result holds AND the record lists the named check with the verdict PASS; it
    collects its two printed lines (PASS and reproduces) in a text buffer and prints
    them with one call, so that they always stay together in the output.
    """),
    code(r'''
    import contextlib  # redirect_stdout: send printed lines into a buffer
    import io  # StringIO: a text buffer in memory

    PY = "Revision/field_equations_a4/reports/python-a4-report.json"  # sympy record
    WL = "Revision/field_equations_a4/reports/wolfram-a4-report.json"  # Wolfram record
    LEAD = "Revision/lead_checks/reports/einstein-gauss-bonnet-a4.json"  # lead check
    EQUATIONS = "Revision/field_equations_a4/a4-equations.json"  # the equations
    METRIC_RESULTS = "Revision/metric_warped/results/warped-metric.json"
    METRIC_WL = "Revision/metric_warped/reports/wolfram-warped-metric-report.json"
    KS = "Revision/field_equations_a4/reports/ks-source-conditions.json"
    KS_A4 = "Revision/field_equations_a4/ks_source/reports/ks-source-a4.json"
    EOS = "Revision/dark_sector/dirac16complex00/reports/python-derive-eos.json"


    def read_json(relative):
        """Read a JSON file of the repository (a Revision record)."""
        return json.loads(repository_file(relative).read_text(encoding="utf-8"))


    def record_verdict(report_file, name):
        """The verdict of the check name in a report ("PASS"), None if absent."""
        for entry in read_json(report_file)["checks"]:
            if entry["name"] == name:
                return entry["verdict"]
        return None


    def record_detail(report_file, name):
        """The detail text of the check name in a report."""
        for entry in read_json(report_file)["checks"]:
            if entry["name"] == name:
                return entry["detail"]
        return ""


    def reproduces(condition, name, report_file, record_name):
        """A check that also requires the record check record_name to be PASS.  Its
        printed lines (PASS and reproduces) are collected in a text buffer and printed
        by one print call, so that they always stay together in the cell's output."""
        found = record_verdict(report_file, record_name) == "PASS"
        lines = io.StringIO()  # a text buffer
        with contextlib.redirect_stdout(lines):  # print() now writes into the buffer
            check(condition and found, name, record=f"{report_file}, check {record_name}")
        print(lines.getvalue(), end="")  # all lines at once


    record = read_json(EQUATIONS)
    title = record["title"]  # the title stored in the record
    say(f"read {EQUATIONS}: {title}")
    '''),
    md(r"""
    ## 6. The required source of the exponential histories

    The record stores each Lovelock component as a text in the Wolfram Language
    (`ad1` stands for $a_4'$, `ad2` for $a_4''$, `uu` for $u$, `vv` for $v$, `kk` for
    $k$, `^` for a power). The next cell turns the stored components of $E_{(1)}$,
    $E_{(2)}$, $E_{(3)}$ into sympy expressions, forms the left-hand sides
    $\sum_k\alpha_kE_{(k)}$, and substitutes the exponential history
    $a_4' = AH$, $u = \beta AH$, $a_4'' = v = 0$. Then it reads off

    $$\kappa\rho = -\Big(\sum_k \alpha_k E_{(k)}{}^{x_4}{}_{x_4} + \Lambda\Big),\qquad
    \kappa p_3 = \sum_k \alpha_k E_{(k)}{}^{x_1}{}_{x_1} + \Lambda,$$

    and the same for $p_0$ (component $x_0$) and $p_t$ (component $x_5$).
    """),
    code(r'''
    import numpy as np  # arrays of numbers for the plots
    import sympy as sp  # exact algebra with symbols

    H = sp.symbols("H", positive=True)  # the constant H of the metric
    A, beta = sp.symbols("A beta", real=True)  # the exponential history
    ad1, ad2, uu, vv, kk = sp.symbols("ad1 ad2 uu vv kk", real=True)
    alpha1, alpha2, alpha3 = sp.symbols("alpha1 alpha2 alpha3", real=True)
    Lam, kappa = sp.symbols("Lam kappa", real=True)  # Lambda and kappa
    NAMES = {"ad1": ad1, "ad2": ad2, "uu": uu, "vv": vv, "kk": kk, "H": H, "AA": A,
             "be": beta, "alpha1": alpha1, "alpha2": alpha2, "alpha3": alpha3,
             "Lam": Lam, "kappa": kappa}


    def parse(text):
        """A Wolfram InputForm text of the record as a sympy expression."""
        return sp.sympify(text.replace("^", "**"), locals=NAMES)


    ALPHA = {1: alpha1, 2: alpha2, 3: alpha3}
    lovelock = record["lovelockTensors"]
    side = {key: sum(ALPHA[k] * parse(lovelock[f"E{k}"][key]["input"]) for k in (1, 2, 3))
            for key in ("x0x0", "x1x1", "x4x4", "x5x5")}  # sum_k alpha_k E_(k)
    EXPONENTIAL = {ad1: A * H, ad2: 0, uu: beta * A * H, vv: 0}
    kappa_rho = sp.expand(-(side["x4x4"] + Lam).subs(EXPONENTIAL))
    kappa_p3 = sp.expand((side["x1x1"] + Lam).subs(EXPONENTIAL))
    kappa_p0 = sp.expand((side["x0x0"] + Lam).subs(EXPONENTIAL))
    kappa_pt = sp.expand((side["x5x5"] + Lam).subs(EXPONENTIAL))
    say(f"Einstein part of kappa rho: {sp.factor(kappa_rho.coeff(alpha1))}")
    say(f"Einstein part of kappa p3: {sp.factor(kappa_p3.coeff(alpha1))}")
    say(f"Einstein part of kappa p0: {sp.factor(kappa_p0.coeff(alpha1))}")
    '''),
    md(r"""
    The next cell checks five things. (1) $p_0 = p_t$: the hidden component and the
    extra-time component of every left-hand side are one expression. (2) The source is
    a polynomial of degree at most 2 in $k$; the time enters only through
    $k = k_0e^{(2 - \beta)AHx_4}$, whose rate $dk/dx_4 = (2 - \beta)AH\,k$ vanishes only
    for $\beta = 2$ or $A = 0$: only then is the source constant. (3) It equals the
    record's formulas. (4) Written as functions of $k$, it contains $A$ only through
    $A^2$: every term has an even power of $A$. (5) Its Einstein parts (the
    coefficients of $\alpha_1$) equal the Einstein source that the record of the
    corrected metric writes for the exponential histories (with $e^{2AHx_4}
    e^{-\beta AHx_4}$ for $k$, at $b_4(0) = 1$, $a_0 = 0$).
    """),
    code(r'''
    reproduces(sp.expand(kappa_pt - kappa_p0) == 0,
               "the hidden and the extra-time pressures are equal: p0 = p_t",
               WL, "independent_components")
    degrees = [sp.Poly(value, kk).degree() for value in (kappa_rho, kappa_p3, kappa_p0)]
    x4 = sp.symbols("x4", real=True)
    k_rate = sp.diff(sp.exp((2 - beta) * A * H * x4), x4) / sp.exp((2 - beta) * A * H * x4)
    say(f"degrees in k: {degrees}; dk/dx4 = ({sp.factor(sp.simplify(k_rate))}) k")
    reproduces(max(degrees) <= 2 and sp.factor(sp.simplify(k_rate)) == -A * H * (beta - 2),
               "the source is a polynomial of degree <= 2 in k; constant iff beta = 2 or "
               "A = 0", PY, "exponential_history_required_source")
    required = record["exponentialHistory"]["requiredSource"]
    same = all(sp.expand(kappa * parse(required[key]["input"]) - value) == 0
               for key, value in (("rho", kappa_rho), ("p3", kappa_p3), ("p0", kappa_p0),
                                  ("pt", kappa_pt)))
    reproduces(same, "kappa rho, kappa p3, kappa p0, kappa p_t equal the record",
               PY, "json_exponential_history")
    check(all(sp.expand(value.subs(A, -A) - value) == 0
              for value in (kappa_rho, kappa_p3, kappa_p0)),
          "as functions of k the source contains A only through A^2")
    stored = read_json(METRIC_RESULTS)["history_source"]["einstein_kappaT_minus_Lambda"]
    names_e = {"A": A, "beta": beta, "H": H, "x4": x4, "exp": sp.exp}
    k_of_x4 = sp.exp((2 - beta) * A * H * x4)  # k at b4(0) = 1, a0 = 0
    mine = {"-rho": -kappa_rho.coeff(alpha1), "p3": kappa_p3.coeff(alpha1),
            "p0": kappa_p0.coeff(alpha1), "p_t": kappa_pt.coeff(alpha1)}
    same = all(sp.simplify(sp.sympify(stored[key], locals=names_e)
                           - (value.subs(Lam, 0)).subs(kk, k_of_x4)) == 0
               for key, value in mine.items())
    reproduces(same, "the alpha1 parts equal the Einstein source of the metric record",
               LEAD, "einstein_exponential_source_alpha1")
    '''),
    md(r"""
    ## 7. Einstein gravity

    With $\alpha_1 = 1$, $\alpha_2 = \alpha_3 = 0$ the required source is

    $$\kappa\rho = \tfrac32A^2H^2(\beta^2 - 2) - 6H^2k - \Lambda,\qquad
    \kappa p_3 = -\tfrac12A^2H^2(5\beta^2 - 12\beta + 10) + 6H^2k + \Lambda,$$
    $$\kappa p_0 = \kappa p_t = -\tfrac32A^2H^2(\beta^2 - \beta + 2) + 3H^2k + \Lambda .$$

    On the record history ($A = 1$, $\beta = \tfrac43$, $H = \kappa = 1$, $\Lambda = 0$)
    this is $\kappa\rho = -6k - \tfrac13$, $\kappa p_3 = 6k - \tfrac{13}9$,
    $\kappa p_0 = 3k - \tfrac{11}3$, with $k = e^{2x_4/3}$; at $x_4 = 0$ ($k = 1$):
    $\kappa\rho = -\tfrac{19}3$, $\kappa p_3 = \tfrac{41}9$, $\kappa p_0 =
    -\tfrac23$. The next cell checks these formulas against the record and against the
    Wolfram record of the corrected metric, which writes the source of the record
    history with `Exp[(2/3)*H*x4]` for $k$.
    """),
    code(r'''
    EINSTEIN = {alpha1: 1, alpha2: 0, alpha3: 0}
    rho_e, p3_e, p0_e = (sp.expand(value.subs(EINSTEIN))
                         for value in (kappa_rho, kappa_p3, kappa_p0))
    report("Einstein: kappa rho", sp.factor(rho_e))
    einstein_record = record["exponentialHistory"]["einstein"]
    same = all(sp.expand(kappa * parse(einstein_record[key]["input"]) - value) == 0
               for key, value in (("rho", rho_e), ("p3", p3_e), ("p0", p0_e)))
    reproduces(same, "Einstein: the required source equals the record",
               WL, "exponential_history_required_source")
    HISTORY = {A: 1, beta: sp.Rational(4, 3), H: 1, Lam: 0}  # record history, Lambda = 0
    history = {name: sp.expand(value.subs(HISTORY))
               for name, value in (("rho", rho_e), ("p3", p3_e), ("p0", p0_e))}
    for name, value in history.items():
        report(f"record history, Einstein, Lambda = 0: kappa {name}", value)
    at_start = {name: value.subs(kk, 1) for name, value in history.items()}
    report("at x4 = 0: kappa rho, kappa p3, kappa p0",
           f"{at_start['rho']}, {at_start['p3']}, {at_start['p0']}")
    check(at_start == {"rho": sp.Rational(-19, 3), "p3": sp.Rational(41, 9),
                       "p0": sp.Rational(-2, 3)},
          "record history at x4 = 0: kappa rho = -19/3, kappa p3 = 41/9, kappa p0 = -2/3")
    stored = read_json(METRIC_RESULTS)["history_source"]["einstein_A1_beta43_mathematica"]
    k_of_t = sp.exp(sp.Rational(2, 3) * x4)
    names_m = {"H": sp.Integer(1), "x4": x4}


    def from_wolfram(text):
        """A Wolfram text such as (1/3)*H^2*(18*Exp[(2/3)*H*x4] + 1) in sympy."""
        text = text.replace("Exp[", "exp(").replace("]", ")").replace("^", "**")
        return sp.sympify(text, locals=names_m)


    same = all(sp.simplify(from_wolfram(stored[key]) - value.subs(kk, k_of_t)) == 0
               for key, value in (("-rho", -history["rho"]), ("p3", history["p3"]),
                                  ("p0", history["p0"]), ("p_t", history["p0"])))
    reproduces(same, "the source of the record history equals the Wolfram record",
               METRIC_WL, "history_source_equals_sympy")
    '''),
    md(r"""
    The next cell draws the three components of the Einstein source along the record
    history for $0 \le x_4 \le 3$ ($\Lambda = 0$, $H = \kappa = 1$). All three grow like
    $k = e^{2x_4/3}$, because the curvature $-H^2k$ of the shrinking block grows. With
    $\Lambda = 0$ the energy density $\kappa\rho = -6k - \tfrac13$ is negative at every
    time; the cell checks this.
    """),
    code(r'''
    x_axis = np.linspace(0.0, 3.0, 301)  # the time x4 in units 1/H
    k_axis = np.exp(2.0 * x_axis / 3.0)  # k on the record history
    curves = {name: sp.lambdify(kk, value, "numpy")(k_axis) * np.ones_like(k_axis)
              for name, value in history.items()}
    check(bool(np.all(curves["rho"] < 0)),
          "Einstein, Lambda = 0: the energy density of the record history is negative")
    fig, ax = plt.subplots()
    ax.plot(x_axis, curves["rho"], label="$\\kappa\\rho = -6k - 1/3$")
    ax.plot(x_axis, curves["p3"], "--", label="$\\kappa p_3 = 6k - 13/9$")
    ax.plot(x_axis, curves["p0"], ":", label="$\\kappa p_0 = \\kappa p_t = 3k - 11/3$")
    ax.axhline(0.0, color="black", linewidth=0.8)
    ax.set_xlabel("time $x_4$ (units $1/H$)")
    ax.set_ylabel("required source (units of $H^2/\\kappa$)")
    ax.set_title("Einstein gravity, $\\Lambda = 0$: the source of the record history")
    ax.legend(fontsize=8)
    save_figure(fig, "einstein_source",
                "The source that the record history $a_4 = Hx_4$, $b_4 = e^{(4/3)Hx_4}$ "
                "requires in Einstein gravity with $\\Lambda = 0$, as a function of the "
                "time $x_4$ (units $1/H$), in units of $H^2/\\kappa$: the energy density "
                "$\\kappa\\rho = -6k - 1/3$ (solid), the 3-space pressure "
                "$\\kappa p_3 = 6k - 13/9$ (dashed) and the common pressure of the hidden "
                "direction and the extra times $\\kappa p_0 = \\kappa p_t = 3k - 11/3$ "
                "(dotted), with $k = e^{2x_4/3}$. All three grow with $k$; the energy "
                "density is negative at every time, and $p_3 \\neq p_0$: the source is "
                "anisotropic.")
    '''),
    md(r"""
    **The sign of $A$ is a choice.** As functions of $k$ the source contains only
    $A^2$, so the histories with $A$ and $-A$ (and the same $\beta$) need the same
    source at the same value of $k$. As functions of the time they are mirror images:
    $k = k_0e^{(2 - \beta)AHx_4}$ depends on $A$ and $x_4$ only through their product,
    so the source of $-A$ at the time $x_4$ is the source of $A$ at the time $-x_4$.
    The next cell checks both statements in Einstein gravity on $\beta = 4/3$
    ($\Lambda = 0$) and draws the energy density of $A = 1$ and $A = -1$ against $k$
    (left; the curves coincide) and against the time (right; mirror images).
    """),
    code(r'''
    rho_43 = sp.expand(rho_e.subs({beta: sp.Rational(4, 3), H: 1, Lam: 0}))
    k_time = {slope: sp.exp(sp.Rational(2, 3) * slope * x4) for slope in (1, -1)}
    rho_time = {slope: rho_43.subs(A, slope).subs(kk, k_time[slope]) for slope in (1, -1)}
    check(sp.expand(rho_43.subs(A, 1) - rho_43.subs(A, -1)) == 0
          and sp.simplify(rho_time[-1] - rho_time[1].subs(x4, -x4)) == 0,
          "A and -A: the same source at the same k, mirror images in time")
    fig, (left, right) = plt.subplots(1, 2, figsize=(11.0, 4.2))
    k_values = np.linspace(0.2, 5.0, 200)
    times = np.linspace(-3.0, 3.0, 301)
    for slope, style in ((1, "-"), (-1, "--")):
        rho_k = sp.lambdify(kk, rho_43.subs(A, slope), "numpy")
        left.plot(k_values, rho_k(k_values), style, label=f"$A = {slope}$")
        rho_t = sp.lambdify(x4, rho_time[slope], "numpy")
        right.plot(times, rho_t(times), style, label=f"$A = {slope}$")
    left.set_xlabel("$k = e^{2a_4}/b_4$")
    left.set_ylabel("$\\kappa\\rho$ (units $H^2$)")
    left.set_title("against $k$: the same curve")
    left.legend(fontsize=8)
    right.set_xlabel("time $x_4$ (units $1/H$)")
    right.set_ylabel("$\\kappa\\rho$ (units $H^2$)")
    right.set_title("against the time: mirror images")
    right.legend(fontsize=8)
    save_figure(fig, "sign_symmetry",
                "Einstein gravity, $\\beta = 4/3$, $\\Lambda = 0$: the energy density "
                "$\\kappa\\rho$ that the exponential histories with slope $A = 1$ "
                "(solid) and $A = -1$ (dashed) require, in units of $H^2$. Left, as a "
                "function of $k = e^{2a_4}/b_4$: the two curves coincide, because the "
                "source contains $A$ only through $A^2$. Right, as a function of the "
                "time $x_4$ (units $1/H$): the curves are mirror images under "
                "$x_4 \\to -x_4$, because $k = e^{(2/3)Ax_4}$ depends only on the "
                "product $Ax_4$. Whether 3-space inflates or deflates is an initial "
                "condition, not selected by the equations.")
    '''),
    md(r"""
    **The role of $\beta$.** At a moment where $k = 1$ (on the record history: at
    $x_4 = 0$) the Einstein source with $A = 1$, $\Lambda = 0$ depends on $\beta$ alone:
    $\kappa\rho = \tfrac32(\beta^2 - 2) - 6$, $\kappa p_3 = 6 - \tfrac12(5\beta^2 -
    12\beta + 10)$, $\kappa p_0 = 3 - \tfrac32(\beta^2 - \beta + 2)$ (units
    $H = \kappa = 1$). The next cell draws them for $0 \le \beta \le 4$, marks the record
    value $\beta = 4/3$ and the value $\beta = 2$ at which the block does not shrink
    (its scale factor $e^{-(1 - \beta/2)AHx_4}$ is constant) and the source is constant
    in time, and checks that the energy density is positive at $k = 1$ exactly for
    $\beta > \sqrt6$.
    """),
    code(r'''
    scan = {name: sp.expand(value.subs({A: 1, H: 1, Lam: 0, kk: 1}))
            for name, value in (("rho", rho_e), ("p3", p3_e), ("p0", p0_e))}
    positive = sp.solve_univariate_inequality(scan["rho"] > 0, beta, relational=False)
    say(f"k = 1, A = 1, Lambda = 0: kappa rho = {scan['rho']} > 0 for beta in {positive}")
    check(positive == sp.Union(sp.Interval.open(-sp.oo, -sp.sqrt(6)),
                               sp.Interval.open(sp.sqrt(6), sp.oo)),
          "k = 1: the Einstein energy density is positive exactly for |beta| > sqrt(6)")
    beta_axis = np.linspace(0.0, 4.0, 401)
    fig, ax = plt.subplots()
    for (name, value), style, label in zip(scan.items(), ("-", "--", ":"),
                                           ("$\\kappa\\rho$", "$\\kappa p_3$",
                                            "$\\kappa p_0 = \\kappa p_t$")):
        ax.plot(beta_axis, sp.lambdify(beta, value, "numpy")(beta_axis), style,
                label=label)
    ax.axvline(4.0 / 3.0, color="black", linestyle=":", linewidth=0.8)
    ax.axvline(2.0, color="grey", linestyle="--", linewidth=0.8)
    ax.text(4.0 / 3.0 + 0.03, 4.5, "record $\\beta = 4/3$", fontsize=8)
    ax.text(2.03, -9.5, "$\\beta = 2$: block constant", fontsize=8)
    ax.axhline(0.0, color="black", linewidth=0.8)
    ax.set_xlabel("$\\beta = u/a_4'$")
    ax.set_ylabel("required source at $k = 1$ (units $H^2$)")
    ax.set_title("Einstein gravity, $A = 1$, $\\Lambda = 0$: the source against $\\beta$")
    ax.legend(fontsize=8, loc="lower left")
    save_figure(fig, "beta_scan",
                "Einstein gravity with $A = 1$ and $\\Lambda = 0$: the source that an "
                "exponential history requires at a moment where $k = 1$, as a function "
                "of $\\beta = u/a_4'$ from 0 to 4, in units of $H^2/\\kappa$: the energy "
                "density $\\kappa\\rho = 3(\\beta^2 - 2)/2 - 6$ (solid), the 3-space "
                "pressure (dashed) and the common pressure of the hidden direction and "
                "the extra times (dotted). The dotted vertical line is the record value "
                "$\\beta = 4/3$, the dashed one $\\beta = 2$, where the block of the "
                "hidden direction and the extra times does not shrink and the source is "
                "constant in time. The energy density is positive only for "
                "$\\beta > \\sqrt{6}$.")
    '''),
    md(r"""
    ## 8. The author's weights

    With $\alpha_k = w_k/H^{2k}$, $w = (1, \tfrac1{32}, \tfrac1{1152})$, on the record
    history ($H = 1$) the source $\kappa T - \Lambda\delta$ is a polynomial in
    $k = e^{2x_4/3}$. With the record's $\Lambda = -10$ the next cell computes
    $\kappa\rho$, $\kappa p_3$ and $\kappa p_0$, compares the source with the record,
    computes the anisotropy $\kappa(p_3 - p_0)$ (a nonzero polynomial in $k$: no source
    with equal pressures can drive this history), finds the time at which $\kappa\rho$
    changes sign, and evaluates $\kappa\rho$ at the five slices $a_4 = 0, 0.5, 1, 1.5,
    2$ of the Kohn-Sham record, which the record of the source conditions prints with
    six significant digits.
    """),
    code(r'''
    import re  # regular expressions: find numbers in a text

    AUTHOR = {alpha1: 1, alpha2: sp.Rational(1, 32) / H ** 2,
              alpha3: sp.Rational(1, 1152) / H ** 4}
    RECORD_HISTORY = {A: 1, beta: sp.Rational(4, 3), H: 1}
    shifted = {name: sp.expand(value.subs(AUTHOR).subs(RECORD_HISTORY))
               for name, value in (("minus_rho", -kappa_rho - Lam), ("p3", kappa_p3 - Lam),
                                   ("p0", kappa_p0 - Lam))}  # kappa T - Lambda
    stored = record["exponentialHistory"]["authorWeights"]["historySource_kappaT_minus_Lam"]
    same = all(sp.expand(parse(stored[key]["input"]) - shifted[name]) == 0
               for key, name in (("minus_rho", "minus_rho"), ("p3", "p3"), ("p0", "p0"),
                                 ("pt", "p0")))
    reproduces(same, "the author's weights: kappa T - Lambda of the record history",
               PY, "author_weights_history_source")
    LAMBDA = -10  # the record's Lambda for the author's weights
    author = {"rho": sp.expand(-shifted["minus_rho"] - LAMBDA),
              "p3": sp.expand(shifted["p3"] + LAMBDA),
              "p0": sp.expand(shifted["p0"] + LAMBDA)}
    for name, value in author.items():
        report(f"author's weights, Lambda = -10: kappa {name}", value)
    anisotropy = sp.expand(author["p3"] - author["p0"])
    report("kappa (p3 - p0)", anisotropy)
    eos_text = record_detail(EOS, "condensate_cannot_source_history")
    reproduces(sp.expand(anisotropy - (-sp.Rational(9, 16) * kk ** 2
                                       + sp.Rational(1069, 432) * kk
                                       + sp.Rational(2015, 972))) == 0
               and "-9*kk**2/16 + 1069*kk/432 + 2015/972" in eos_text,
               "the history needs kappa (p3 - p0) = -9 k^2/16 + 1069 k/432 + 2015/972",
               EOS, "condensate_cannot_source_history")
    roots = [r for r in sp.Poly(author["rho"], kk).nroots() if r.is_real and r > 0]
    k_zero = min(roots)  # the value of k where kappa rho changes sign
    x_zero = 1.5 * float(sp.log(k_zero))  # k = e^(2 x4/3)
    report("kappa rho changes sign at k, x4", f"{float(k_zero):.6f}, {x_zero:.6f}")
    gas_text = record_detail(KS_A4, "C3_record_history_not_sourced_by_the_gas")
    reproduces(0.75 < x_zero < 0.8
               and "changes sign between the dense slices a4 = 0.75 and 0.8" in gas_text,
               "kappa rho changes sign between a4 = 0.75 and a4 = 0.8",
               KS_A4, "C3_record_history_not_sourced_by_the_gas")
    slices = [0.0, 0.5, 1.0, 1.5, 2.0]
    values = [float(author["rho"].subs(kk, np.exp(2.0 * a / 3.0))) for a in slices]
    printed = [f"{value:.6g}" for value in values]
    say("kappa rho at a4 = 0, 0.5, 1, 1.5, 2: " + ", ".join(printed))
    ks_text = record_detail(KS, "ks_history_is_a_prescribed_background")
    stated = re.findall(r"kappa rho = (\S+?),", ks_text)
    reproduces(stated == printed,
               "the five energy densities equal the record of the source conditions",
               KS, "ks_history_is_a_prescribed_background")
    '''),
    md(r"""
    The next cell draws the source of the record history with the author's weights
    ($\Lambda = -10$, $H = \kappa = 1$) for $0 \le x_4 \le 3$: the energy density starts
    positive, $\kappa\rho = 3.57407$, and changes sign near $x_4 = 0.78$; the five
    slices of the Kohn-Sham record are marked.
    """),
    code(r'''
    fig, ax = plt.subplots()
    for name, style, label in (("rho", "-", "$\\kappa\\rho$"), ("p3", "--", "$\\kappa p_3$"),
                               ("p0", ":", "$\\kappa p_0 = \\kappa p_t$")):
        function = sp.lambdify(kk, author[name], "numpy")
        ax.plot(x_axis, function(k_axis) * np.ones_like(k_axis), style, label=label)
    ax.plot(slices, values, "o", color="black", markersize=4,
            label="the five slices of the record")
    ax.axvline(x_zero, color="grey", linewidth=0.8)
    ax.axhline(0.0, color="black", linewidth=0.8)
    ax.set_xlabel("time $x_4$ (units $1/H$)")
    ax.set_ylabel("required source (units $H^2/\\kappa$)")
    ax.set_title("The author's weights, $\\Lambda = -10$: the source of the record history")
    ax.legend(fontsize=8)
    save_figure(fig, "author_weights_source",
                "The source that the record history $a_4 = Hx_4$, $b_4 = e^{(4/3)Hx_4}$ "
                "requires with the author's weights $\\alpha_k = w_k/H^{2k}$, "
                "$w = (1, 1/32, 1/1152)$, and $\\Lambda = -10$, as a function of the time "
                "$x_4$ (units $1/H$, $H = \\kappa = 1$): the energy density $\\kappa\\rho$ "
                "(solid), the 3-space pressure $\\kappa p_3$ (dashed) and the common "
                "pressure $\\kappa p_0 = \\kappa p_t$ (dotted). The energy density starts "
                "at "
                "$3.57407$ and changes sign at $x_4 = 0.78$ (grey line); the black dots "
                "are its values at the slices $a_4 = 0, 0.5, 1, 1.5, 2$ printed by the "
                "record of the source conditions. A source whose energy density changes "
                "sign is not ordinary matter.")
    '''),
    md(r"""
    ## 9. The two null energy conditions in Einstein gravity

    The record gives the null combinations (key `nullCombinations`). In Einstein
    gravity on an exponential history they are

    $$\kappa(\rho + p_0) = -\tfrac32H^2\big(2k + A^2(4 - \beta)\big),\qquad
    \kappa(\rho + p_3) = -A^2H^2(\beta - 2)(\beta - 4) .$$

    The NEC along $x_4 + x_1$ holds where $(\beta - 2)(\beta - 4) \le 0$, that is for
    $2 \le \beta \le 4$. The NEC along $x_4 + x_0$ needs $2k \le A^2(\beta - 4)$; since
    $k > 0$ this needs $\beta \ge 4 + 2k/A^2 > 4$. The two ranges do not meet: in
    Einstein gravity no exponential history has a source that satisfies both null
    energy conditions. The next cell checks the combinations against the record,
    derives the two ranges with sympy, and prints the two combinations on the record
    history with the author's weights.
    """),
    code(r'''
    null_record = record["generalSource"]["nullCombinations"]
    null_x0 = sp.expand((kappa_rho + kappa_p0).subs(EINSTEIN))
    null_x1 = sp.expand((kappa_rho + kappa_p3).subs(EINSTEIN))
    same = all(sp.expand(parse(null_record[key]["input"]).subs(EINSTEIN)
                         .subs(EXPONENTIAL) - value) == 0
               for key, value in (("kappa(rho+p0)", null_x0), ("kappa(rho+p3)", null_x1)))
    reproduces(same and sp.expand(null_x0 + sp.Rational(3, 2) * H ** 2
                                  * (2 * kk + A ** 2 * (4 - beta))) == 0
               and sp.expand(null_x1 + A ** 2 * H ** 2 * (beta - 2) * (beta - 4)) == 0,
               "Einstein, exponential: the two null combinations of the record",
               PY, "json_required_source_and_null_combinations")
    range_x1 = sp.solve_univariate_inequality(-(beta - 2) * (beta - 4) >= 0, beta,
                                              relational=False)
    kp, Ap = sp.symbols("kp Ap", positive=True)  # k > 0 and A^2 > 0
    beta_edge = sp.solve(2 * kp + Ap ** 2 * (4 - beta), beta)[0]  # rho + p0 = 0
    say(f"rho + p3 >= 0 for beta in {range_x1}; rho + p0 >= 0 needs beta >= {beta_edge}")
    check(range_x1 == sp.Interval(2, 4) and sp.simplify(beta_edge - 4) == 2 * kp / Ap ** 2,
          "Einstein: no exponential history satisfies both null energy conditions")
    author_null = {name: sp.expand(author["rho"] + author[name]) for name in ("p0", "p3")}
    report("author's weights: kappa (rho + p0)", author_null["p0"])
    report("author's weights: kappa (rho + p3)", author_null["p3"])
    '''),
    md(r"""
    The next cell draws the two conditions in the plane of $\beta$ (horizontal) and
    $k/A^2$ (vertical) for Einstein gravity: the NEC along $x_4 + x_1$ holds in the
    vertical band $2 \le \beta \le 4$, the NEC along $x_4 + x_0$ below the line
    $k/A^2 = (\beta - 4)/2$. Above $k = 0$ (where every history lies) the band and the
    region below the line do not overlap.
    """),
    code(r'''
    b_grid, k_grid = np.meshgrid(np.linspace(0.0, 7.0, 351), np.linspace(-2.0, 3.0, 251))
    nec_x0 = (2 * k_grid + (4 - b_grid)) <= 0  # A = 1
    nec_x1 = (b_grid - 2) * (b_grid - 4) <= 0
    region = np.where(nec_x0 & nec_x1, 3, np.where(nec_x0, 2, np.where(nec_x1, 1, 0)))
    fig, ax = plt.subplots()
    colours = matplotlib.colors.ListedColormap(["#f7f7f7", "#d1e5f0", "#fddbc7",
                                                "#b2182b"])
    ax.pcolormesh(b_grid, k_grid, region, cmap=colours, vmin=-0.5, vmax=3.5,
                  shading="auto")
    ax.plot(b_grid[0], (b_grid[0] - 4.0) / 2.0, color="black",
            label="$\\rho + p_0 = 0$: $k/A^2 = (\\beta - 4)/2$")
    ax.axhline(0.0, color="black", linewidth=1.2)
    ax.axvline(4.0 / 3.0, color="black", linestyle=":", label="record history")
    ax.text(3.0, 2.3, "$\\rho + p_3 \\geq 0$", ha="center", fontsize=9)
    ax.text(5.8, -1.2, "$\\rho + p_0 \\geq 0$", ha="center", fontsize=9)
    ax.text(1.0, 2.3, "both violated", ha="center", fontsize=9)
    ax.set_xlabel("$\\beta$")
    ax.set_ylabel("$k/A^2$")
    ax.set_title("Einstein gravity: the two null energy conditions")
    ax.legend(fontsize=8, loc="lower right")
    save_figure(fig, "null_energy_map",
                "Einstein gravity on the exponential histories: the plane of $\\beta$ "
                "(horizontal) and $k/A^2$ (vertical, $k = e^{2a_4}/b_4$). Blue: the null "
                "energy condition along $x_4 + x_1$, $\\rho + p_3 \\geq 0$, holds "
                "($2 \\leq \\beta \\leq 4$). Pink: the null energy condition along "
                "$x_4 + x_0$, $\\rho + p_0 \\geq 0$, holds (below the black line "
                "$k/A^2 = (\\beta - 4)/2$). Dark red: both hold, only where $k < 0$. "
                "Every history lies above the horizontal line "
                "$k = 0$, where the two regions do not overlap: no exponential history "
                "has a source that satisfies both conditions. The dotted line is the "
                "record history $\\beta = 4/3$, where both are violated.")
    '''),
    md(r"""
    ## 10. Vacua: Einstein-Gauss-Bonnet gravity and the author's weights

    A vacuum needs $\rho = p_3 = p_0 = 0$. Where $k$ changes in time ($\beta \ne 2$,
    $A \ne 0$) the three required components are polynomials in $k$ that must vanish
    for a whole interval of values of $k$, so every coefficient of $k^0$, $k^1$, $k^2$
    must vanish. The next cell writes these coefficients for Einstein-Gauss-Bonnet
    gravity ($\alpha_1 = 1$, $\alpha_3 = 0$; $\alpha_2$ and $\Lambda$ free) and computes
    a Groebner basis (a systematic elimination; a basis $[1]$ means that the equations
    have no common solution, not even a complex one). For constant $k = k_0$
    ($\beta = 2$) it solves the time and the hidden equations for $\alpha_2$ and
    $\Lambda$ and checks that the 3-space equation then holds:

    $$\alpha_2 = -\frac{1}{4H^2(A^2 - k_0)},\qquad
    \Lambda = \frac{3H^2(A^4 + 3A^2k_0 + k_0^2)}{A^2 - k_0}\qquad(k_0 \ne A^2).$$

    On these histories the block does not shrink: they are vacua, but not deflating
    ones.
    """),
    code(r'''
    GAUSS_BONNET = {alpha1: 1, alpha3: 0, H: 1}
    coefficients = []
    for value in (kappa_rho, kappa_p3, kappa_p0):
        polynomial = sp.Poly(sp.expand(value.subs(GAUSS_BONNET)), kk)
        coefficients += [c for c in polynomial.all_coeffs() if c != 0]
    basis = sp.groebner(coefficients, A, beta, alpha2, Lam, order="lex")
    say(f"Gauss-Bonnet, k varies: {len(coefficients)} coefficient equations, "
        f"Groebner basis {list(basis.exprs)}")
    reproduces(list(basis.exprs) == [1],
               "Einstein-Gauss-Bonnet: no vacuum exponential history where k varies",
               PY, "egb_no_vacuum_where_k_varies")
    k0 = sp.symbols("k0", positive=True)  # the constant k on beta = 2
    CONSTANT = {beta: 2, kk: k0}
    time_eq, space_eq, hidden_eq = (sp.expand(value.subs(GAUSS_BONNET).subs(CONSTANT))
                                    for value in (kappa_rho, kappa_p3, kappa_p0))
    branch = sp.solve([time_eq, hidden_eq], [alpha2, Lam], dict=True)[0]
    say(f"beta = 2: alpha2 = {sp.factor(branch[alpha2])}, Lambda = {sp.factor(branch[Lam])}")
    reproduces(sp.simplify(branch[alpha2] + 1 / (4 * (A ** 2 - k0))) == 0
               and sp.simplify(branch[Lam] - 3 * (A ** 4 + 3 * A ** 2 * k0 + k0 ** 2)
                               / (A ** 2 - k0)) == 0
               and sp.simplify(space_eq.subs(branch)) == 0,
               "Einstein-Gauss-Bonnet vacua on constant k: alpha2 and Lambda as recorded",
               PY, "egb_exponential_vacuum_branches")
    '''),
    md(r"""
    The next cell draws the Einstein-Gauss-Bonnet vacua for $A = 1$ as functions of
    $k_0$: the coupling $\alpha_2H^2 = -1/(4(1 - k_0))$ (negative for $k_0 < 1$,
    positive for $k_0 > 1$) and the cosmological constant $\Lambda/H^2$; at $k_0 = A^2$
    both diverge.
    """),
    code(r'''
    alpha2_f = sp.lambdify(k0, branch[alpha2].subs(A, 1), "numpy")
    lambda_f = sp.lambdify(k0, branch[Lam].subs(A, 1), "numpy")
    fig, (left, right) = plt.subplots(1, 2, figsize=(11.0, 4.2))
    for low, high in ((0.05, 0.9), (1.1, 4.0)):
        k_part = np.linspace(low, high, 200)
        left.plot(k_part, alpha2_f(k_part), color="tab:blue")
        right.plot(k_part, lambda_f(k_part), color="tab:orange")
    for ax in (left, right):
        ax.axvline(1.0, color="grey", linestyle="--", linewidth=0.8)
        ax.axhline(0.0, color="black", linewidth=0.8)
        ax.set_xlabel("$k_0/A^2$")
    left.set_ylim(-3.0, 3.0)
    right.set_ylim(-80.0, 80.0)
    left.set_ylabel("$\\alpha_2 H^2$ of the vacuum")
    right.set_ylabel("$\\Lambda/H^2$ of the vacuum")
    fig.suptitle("Einstein-Gauss-Bonnet gravity: the vacua on constant $k$ ($A = 1$)")
    save_figure(fig, "gauss_bonnet_vacuum",
                "The vacuum solutions of Einstein-Gauss-Bonnet gravity ($\\alpha_1 = 1$, "
                "$\\alpha_3 = 0$) among the exponential histories: they exist only for "
                "constant $k = k_0$ ($\\beta = 2$), here with $A = 1$. Left: the coupling "
                "$\\alpha_2 H^2 = -1/(4(A^2 - k_0))$; right: the cosmological constant "
                "$\\Lambda/H^2 = 3(A^4 + 3A^2k_0 + k_0^2)/(A^2 - k_0)$, both against "
                "$k_0/A^2$. Both diverge at $k_0 = A^2$ (dashed line). On these histories "
                "the scale factor $e^{-a_4}b_4^{1/2}$ of the hidden direction and the "
                "extra times is constant: they are vacua, but the extra times do not "
                "deflate.")
    '''),
    md(r"""
    **The author's weights allow no exponential vacuum.** With the author's weights and
    $\Lambda = -10$ the next cell repeats the elimination where $k$ varies (with the
    extra equation $1 - sA(\beta - 2) = 0$, which can hold only when $A \ne 0$ and
    $\beta \ne 2$). For constant $k$ on $\beta = 2$ the time and the 3-space equations
    coincide (the derivative of the constraint vanishes there), so a vacuum needs the
    time equation and the hidden equation, two polynomial equations in $A^2$ and $k_0$.
    The cell eliminates $A$ with a resultant: the values of $k_0$ at which the two
    equations share a root $A^2$ are the zeros of the resultant, and at each of them
    the shared root is negative, so $A$ is not real. On the static history $A = 0$
    there is no solution either.
    """),
    code(r'''
    AUTHOR_VACUUM = {alpha1: 1, alpha2: sp.Rational(1, 32), alpha3: sp.Rational(1, 1152),
                     Lam: LAMBDA, H: 1}
    s = sp.symbols("s")  # 1 - s A (beta - 2) = 0 makes A != 0 and beta != 2
    coefficients = []
    for value in (kappa_rho, kappa_p3, kappa_p0):
        polynomial = sp.Poly(sp.expand(value.subs(AUTHOR_VACUUM)), kk)
        coefficients += [c for c in polynomial.all_coeffs() if c != 0]
    basis = sp.groebner(coefficients + [1 - s * A * (beta - 2)], s, A, beta, order="lex")
    A2 = sp.symbols("A2", real=True)  # A^2
    time_k0 = sp.expand(16 * kappa_rho.subs(AUTHOR_VACUUM).subs(CONSTANT)).subs(A ** 2, A2)
    space_k0 = sp.expand(16 * kappa_p3.subs(AUTHOR_VACUUM).subs(CONSTANT)).subs(A ** 2, A2)
    hidden_k0 = sp.expand(16 * kappa_p0.subs(AUTHOR_VACUUM).subs(CONSTANT))
    hidden_k0 = hidden_k0.subs(A ** 4, A2 ** 2).subs(A ** 2, A2)
    resultant = sp.factor(sp.resultant(time_k0, hidden_k0, A2))
    shared = []  # (k0, the common root A^2) at every real zero k0 > 0 of the resultant
    for root in sp.Poly(resultant, k0).nroots():
        if root.is_real and root > 0:
            common = sp.solve(time_k0.subs(k0, root), A2)
            shared.append((float(root), float(common[0])))
    static = sp.solve([sp.expand(kappa_rho.subs(AUTHOR_VACUUM).subs(A, 0)),
                       sp.expand(kappa_p0.subs(AUTHOR_VACUUM).subs(A, 0))], kk)
    say(f"k varies: Groebner basis {list(basis.exprs)}")
    say("beta = 2, resultant in k0: " + str(resultant))
    say("its positive zeros k0 and the shared root A^2: "
        + ", ".join(f"({k_value:.4f}, {a_value:.4f})" for k_value, a_value in
                    sorted(set((round(a, 6), round(b, 6)) for a, b in shared))))
    reproduces(list(basis.exprs) == [1] and sp.expand(time_k0 + space_k0) == 0
               and all(a_value < 0 for _, a_value in shared) and static == [],
               "the author's weights: no exponential history is a vacuum",
               PY, "author_weights_no_exponential_vacuum")
    '''),
    md(r"""
    The next cell draws the two vacuum conditions of the author's weights on
    $\beta = 2$ in the plane of $k_0$ (horizontal) and $A^2$ (vertical): the curve on
    which the time equation holds and the curve on which the hidden equation holds.
    Real histories need $A^2 \ge 0$ (unshaded); the two curves meet only in the shaded
    region $A^2 < 0$.
    """),
    code(r'''
    k_grid, a_grid = np.meshgrid(np.linspace(0.05, 30.0, 600), np.linspace(-40.0, 40.0, 600))
    time_f = sp.lambdify((k0, A2), time_k0, "numpy")
    hidden_f = sp.lambdify((k0, A2), hidden_k0, "numpy")
    fig, ax = plt.subplots()
    ax.axhspan(-40.0, 0.0, color="grey", alpha=0.25)
    ax.contour(k_grid, a_grid, time_f(k_grid, a_grid), levels=[0.0], colors="tab:blue")
    ax.contour(k_grid, a_grid, hidden_f(k_grid, a_grid), levels=[0.0],
               colors="tab:red", linestyles="--")
    ax.plot([], [], color="tab:blue", label="time (and 3-space) equation: $\\rho = 0$")
    ax.plot([], [], color="tab:red", linestyle="--", label="hidden equation: $p_0 = 0$")
    ax.plot([k for k, _ in shared], [a for _, a in shared], "o", color="black",
            markersize=4, label="where both hold ($A^2 < 0$)")
    ax.set_xlabel("$k_0 = e^{2a_4}/b_4$ (constant)")
    ax.set_ylabel("$A^2$")
    ax.set_title("The author's weights, $\\beta = 2$: no real vacuum")
    ax.legend(fontsize=8, loc="upper right")
    save_figure(fig, "author_weights_no_vacuum",
                "The author's weights ($\\alpha_k = w_k/H^{2k}$, $w = (1, 1/32, 1/1152)$, "
                "$\\Lambda = -10$, $H = 1$) on the exponential histories with constant "
                "$k = k_0$ ($\\beta = 2$): in the plane of $k_0$ (horizontal) and $A^2$ "
                "(vertical) the solid curve is where the time equation (which equals the "
                "3-space equation there) holds with $\\rho = 0$, the dashed curve where "
                "the hidden equation holds with $p_0 = 0$. A vacuum needs both. They "
                "meet only at the black points, all in the grey region $A^2 < 0$, where "
                "the slope $A$ is not real: the author's weights allow no exponential "
                "vacuum.")
    '''),
    md(r"""
    ## 11. A homogeneous condensate of dirac16complex00 as the source

    The record proves that a homogeneous condensate $\Phi(x_4)$ of the commuting field
    has equal pressures, $p_3 = p_t = p_0 = SU'(S) - U(S)$, energy density
    $\rho = mS + U(S)$ and density $S = e^{a_4}b_4^{-2}S_0$, and that its off-diagonal
    components vanish when 24 three-gamma bilinears vanish. A source with equal
    pressures needs $\sum_k\alpha_k(E^{x_1}{}_{x_1} - E^{x_0}{}_{x_0}) = 0$. The next
    cell writes this condition on the exponential histories. In Einstein gravity it
    reads $3k = A^2(\beta - 4)(\beta - \tfrac12)$; the left side changes in time unless
    $\beta = 2$ or $A = 0$, and there the right side gives $k = -A^2$ or $k = 0$: no
    solution with $k > 0$. With the author's weights it holds where $k$ varies nowhere,
    and on constant $k$ exactly for $k_0 = (16 + 2A^2)/(2 + A^2)$ ($\beta = 2$) and
    $k_0 = 8$ ($A = 0$), where the block does not shrink.
    """),
    code(r'''
    equal = sp.expand((kappa_p3 - kappa_p0) / (H ** 2))  # must vanish
    einstein_equal = sp.factor(sp.expand(equal.subs(EINSTEIN)))
    k_needed = sp.solve(einstein_equal, kk)[0]
    say(f"Einstein: p3 = p0 needs k = {sp.factor(k_needed)}")
    reproduces(sp.expand(3 * k_needed - A ** 2 * (beta - 4) * (beta - sp.Rational(1, 2)))
               == 0 and sp.expand(k_needed.subs(beta, 2) + A ** 2) == 0,
               "Einstein: equal pressures on an exponential history need k = -A^2 or 0",
               PY, "condensate_source_equal_pressures")
    author_equal = sp.expand(equal.subs(AUTHOR).subs(H, 1))
    k_coefficients = [c for c in sp.Poly(author_equal, kk).all_coeffs() if c != 0]
    varying = sp.groebner(k_coefficients + [1 - s * A * (beta - 2)], s, A, beta,
                          order="lex")
    on_beta2 = sp.solve(sp.factor(author_equal.subs({beta: 2, kk: k0})), k0)
    static_k = sp.solve(author_equal.subs({A: 0}), kk)
    say(f"author's weights, beta = 2: k0 = {on_beta2}; A = 0: k = {static_k}")
    reproduces(list(varying.exprs) == [1]
               and any(sp.simplify(r - (16 + 2 * A ** 2) / (2 + A ** 2)) == 0
                       for r in on_beta2) and 8 in static_k,
               "the author's weights: equal pressures only for constant k",
               WL, "condensate_source_equal_pressures")
    '''),
    md(r"""
    The next cell draws the two results. Left (Einstein gravity): in the plane of
    $\beta$ and $k/A^2$ the curve $k/A^2 = (\beta - 4)(\beta - \tfrac12)/3$ on which the
    pressures would be equal at one moment; a history keeps a fixed point of this
    plane only where $k$ is constant, $\beta = 2$, and there the curve has
    $k/A^2 = -1 < 0$. Right (the author's weights): the constant values
    $k_0 = (16 + 2A^2)/(2 + A^2)$ against $A$; on these histories the scale factor of
    the hidden direction and the extra times, $k_0^{-1/2}$, is constant.
    """),
    code(r'''
    fig, (left, right) = plt.subplots(1, 2, figsize=(11.0, 4.2))
    beta_axis = np.linspace(-1.0, 6.0, 351)
    left.axhspan(-6.0, 0.0, color="grey", alpha=0.25, label="$k \\leq 0$")
    left.plot(beta_axis, (beta_axis - 4.0) * (beta_axis - 0.5) / 3.0,
              label="$k/A^2 = (\\beta - 4)(\\beta - 1/2)/3$")
    left.axvline(2.0, color="black", linestyle="--", linewidth=0.8,
                 label="$\\beta = 2$: $k$ constant")
    left.plot([2.0], [-1.0], "o", color="black")
    left.set_ylim(-6.0, 8.0)
    left.set_xlabel("$\\beta$")
    left.set_ylabel("$k/A^2$")
    left.set_title("Einstein gravity")
    left.legend(fontsize=8)
    slopes = np.linspace(0.0, 4.0, 200)
    right.plot(slopes, (16 + 2 * slopes ** 2) / (2 + slopes ** 2))
    right.set_xlabel("slope $A$")
    right.set_ylabel("$k_0$ with equal pressures")
    right.set_title("the author's weights, $\\beta = 2$")
    save_figure(fig, "condensate_conditions",
                "When can a source with equal pressures, such as a homogeneous condensate "
                "of dirac16complex00, drive an exponential history? Left, Einstein "
                "gravity: in the plane of $\\beta$ and $k/A^2$ the pressures would be equal "
                "on the curve $k/A^2 = (\\beta - 4)(\\beta - 1/2)/3$; only on $\\beta = 2$ "
                "(dashed) is $k$ constant in time, and there the curve has $k/A^2 = -1$, "
                "in the grey region $k \\leq 0$ where no history lies. Right, the author's "
                "weights: on $\\beta = 2$ the pressures are equal for "
                "$k_0 = (16 + 2A^2)/(2 + A^2)$, shown against the slope $A$; on these "
                "histories the hidden direction and the extra times do not deflate.")
    '''),
    md(r"""
    **What is established here.** The two statements above are PROVED consequences of
    the field equations for a source with equal pressures (Revision record, checks
    `condensate_source_equal_pressures`). The record history itself needs
    $\kappa(p_3 - p_0) \ne 0$ (section 8), so no condensate is its source (record check
    `condensate_cannot_source_history` of the dark-sector record). Whether a condensate
    can drive a history that is not exponential is not decided by the record; Notebook
    12d of this chapter examines the record's exact condensates on their own histories.
    """),
    md(r"""
    ## 12. The last check

    The last cell checks that the eight figure files exist in the folder
    Revision/textbook/figures and prints the number of checks that passed.
    """),
    code(r'''
    figure_names = ["einstein_source", "sign_symmetry", "beta_scan",
                    "author_weights_source", "null_energy_map", "gauss_bonnet_vacuum",
                    "author_weights_no_vacuum", "condensate_conditions"]
    paths = [output_file(f"{FIGURE_FOLDER}/12b_{k}_{name}.png")
             for k, name in enumerate(figure_names, 1)]
    check(all(path.is_file() for path in paths), "all eight figure files exist")
    all_checks_passed()
    '''),
    md(r"""
    ## 13. What this notebook showed

    - Every exponential history $a_4 = AHx_4 + a_0$, $b_4 = b_4(0)e^{\beta AHx_4}$
      needs a diagonal source with $p_0 = p_t$ whose entries are polynomials of degree
      at most 2 in $k = e^{2a_4}/b_4$; it is constant only for $\beta = 2$ or $A = 0$
      (PROVED, equal to the record).
    - As functions of $k$ the source contains $A$ only as $A^2$: the sign of $A$ is a
      choice, an initial condition (PROVED).
    - Einstein gravity, record history, $\Lambda = 0$: $\kappa\rho = -6k - \tfrac13 < 0$,
      $\kappa p_3 = 6k - \tfrac{13}9$, $\kappa p_0 = 3k - \tfrac{11}3$ (PROVED). With the
      author's weights and $\Lambda = -10$ the energy density starts at $3.57407$ and
      changes sign at $x_4 = 0.78/H$ (PROVED formula, COMPUTED zero; equal to the
      records).
    - Einstein gravity: no exponential history has a source that satisfies both null
      energy conditions (PROVED here from the record's null combinations).
    - Einstein-Gauss-Bonnet gravity has exponential vacua only on constant $k$, with
      $\alpha_2 = -1/(4H^2(A^2 - k_0))$; the author's weights allow none (PROVED).
    - A source with equal pressures (a homogeneous condensate) cannot drive an
      exponential history in Einstein gravity; with the author's weights only on
      constant $k$, where the block does not shrink (PROVED, as in the record).
    """),
]

if __name__ == "__main__":
    raise SystemExit(run_builder(__file__))
