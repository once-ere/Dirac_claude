#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
"""Builder of Notebook 13d, "Charge sloshing and mixing in the two-site model"
(textbook "Universes in Pairs", chapter 13).

The notebook Revision/textbook/notebooks/13d_charge_sloshing.ipynb is BUILT from this
file by Revision/textbook/tools/nbkit.py (never edit the .ipynb by hand):

    python Revision/textbook/tools/nbkit.py build \
        Revision/textbook/notebooks/src/13d_charge_sloshing.py --date YYYY-MM-DD
    python Revision/textbook/tools/nbkit.py check \
        Revision/textbook/notebooks/src/13d_charge_sloshing.py

The self-consistency loop of a two-site mean-field model reduced to one function of one
number: plain iteration, linear mixing, the convergence condition, Anderson mixing.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools"))
from nbkit import code, md, run_builder  # noqa: E402

FIGURES = [
    "reduced_map", "cobwebs", "error_histories", "convergence_factor",
    "long_run_diagram", "threshold_versus_u",
]

FACTS = {
    "id": "13d",
    "name": "13d_charge_sloshing",
    "title": "Charge sloshing and mixing in the two-site model",
    "purpose": (
        "It runs the self-consistency loop of a two-site mean-field model with two "
        "electrons (site energies -1 and +1, hopping 1, repulsion 4) by diagonalising "
        "its 2 x 2 Hamiltonian, checks the reduced map x_out = G(x), reproduces the "
        "tables of plain iteration (charge sloshing between the sites) and of linear "
        "mixing, finds the fixed point and the convergence condition of linear mixing "
        "0 < beta < 2/(1 - G'), compares plain iteration, linear mixing and Anderson "
        "mixing, maps the long-run behaviour against beta and the threshold against "
        "the repulsion, and draws six teaching plots."
    ),
    "records": [],
    "packages": ["numpy", "matplotlib"],
    "needs_rust": [],
    "expected_seconds": 10,
    "timeout_seconds": 300,
    "files_written": ["Revision/textbook/figures/13d.captions.json"] + [
        f"Revision/textbook/figures/13d_{k}_{name}.png"
        for k, name in enumerate(FIGURES, 1)
    ],
    "final_lines": [
        "PASS the figure file 13d_6_threshold_versus_u.png exists",
        "ALL 16 CHECKS PASSED (notebook 13d)",
    ],
    "troubleshooting": [],
}

CELLS = [
    md(r"""
    ## 1. What this notebook computes

    The self-consistency loop of density functional theory is a map from an input
    density to an output density, and a solution is a fixed point of this map. The
    simple loop "output becomes the next input" often fails. This notebook shows why,
    with a model small enough to understand completely: two electrons on two sites. It

    - runs the loop by diagonalising the $2 \times 2$ mean-field Hamiltonian and checks
      that it equals the reduced map $x_{out} = G(x)$ of one number;
    - reproduces the tables of plain iteration (the density jumps between the two sites
      forever: charge sloshing) and of linear mixing with $\beta = 1/2$ (it converges);
    - finds the fixed point by bisection, the slope $G'$ there, and the condition
      $0 < \beta < 2/(1 - G')$ under which linear mixing converges;
    - compares the error histories of plain iteration, several linear mixings and
      Anderson mixing;
    - maps the long-run behaviour of the loop against $\beta$ and the threshold against
      the repulsion $U$;
    - draws six teaching plots.
    """),
    md(r"""
    ## 3. The words used in this notebook

    - **Two-site model**: two places L and R with one orbital each; an electron can hop
      between them (hopping $t$); the site energies are $-\Delta/2$ (L) and $+\Delta/2$
      (R).
    - **Mean field**: each electron feels the other one only through its average
      density; here an electron on a site feels $U$ times the density of the other label
      on that site, i.e. $U n_L/2$ on L and $U n_R/2$ on R.
    - **Density** $n_L$, $n_R = 2 - n_L$: the expected number of electrons on each site.
    - **Fixed point** of a map $G$: a number $x^*$ with $G(x^*) = x^*$.
    - **Plain iteration**: $x \leftarrow G(x)$; **linear mixing**:
      $x \leftarrow (1 - \beta)\,x + \beta\,G(x)$ with the mixing parameter $\beta$.
    - **Charge sloshing**: the loop moves the charge back and forth between regions
      instead of settling.
    - **Error**: the distance $x - x^*$ from the fixed point; **convergence factor**: the
      number by which one step multiplies the error near the fixed point.
    - **Cobweb diagram**: a picture of an iteration: go vertically to the curve $G$,
      horizontally to the diagonal, vertically again, and so on.
    - **Anderson mixing**: a mixing that uses several earlier steps to estimate the
      slope of $G$ (for one variable it is close to the secant method).
    - **Bisection**: finding a root by halving an interval that contains it.
    """),
    md(r"""
    ## 4. The physical and mathematical situation

    Two electrons with opposite labels occupy the lowest orbital of the mean-field
    Hamiltonian

    $$h[n_L] = \begin{pmatrix} -\Delta/2 + U n_L/2 & -t \\ -t & \Delta/2 + U n_R/2
    \end{pmatrix}, \qquad n_R = 2 - n_L,$$

    so the output density is $n_L^{out} = 2|c_L|^2$, where $(c_L, c_R)$ is the
    normalised lowest eigenvector. For a real symmetric matrix
    $\begin{pmatrix} a & -t\\ -t & b\end{pmatrix}$ the lowest eigenvector has
    $|c_L|^2 = \tfrac12\big(1 + (b - a)/\sqrt{(b - a)^2 + 4t^2}\big)$, and here
    $b - a = \Delta + U(1 - n_L)$. With $x = n_L - 1$ (the excess on L) the whole loop is
    one function of one number:

    $$x_{out} = G(x) = \frac{\Delta - U x}{\sqrt{(\Delta - Ux)^2 + 4t^2}} .$$

    Near the fixed point $x^*$, $G(x^* + e) \approx x^* + G'(x^*)\,e$, so linear mixing
    multiplies the error by $1 - \beta(1 - G'(x^*))$ at every step, and it converges
    exactly when this number lies between $-1$ and $1$, i.e. for
    $0 < \beta < 2/(1 - G'(x^*))$. The slope is
    $G'(x) = -4Ut^2/((\Delta - Ux)^2 + 4t^2)^{3/2}$.

    **Numbers.** $\Delta = 2$, $t = 1$, $U = 4$ (energies in units of $t$), start
    $n_L = 2$ (both electrons on the low site). **Status:** exact mathematics of a model
    loop (COMPUTED here); the model shows the mechanism, not a physical system of the
    book.
    """),
    md(r"""
    ## 5. The loop and the reduced map

    The next cell defines one pass of the loop by diagonalising $h[n_L]$ with numpy, and
    the closed-form map $G$, and checks that they agree for 41 inputs between 0 and 2.
    """),
    code(r'''
    import numpy as np  # arrays, matrices and linear algebra

    DELTA, T_HOP, U = 2.0, 1.0, 4.0  # site-energy difference, hopping, repulsion


    def loop_pass(n_left, delta=DELTA, t=T_HOP, u=U):
        """One pass: the output density n_L of the lowest orbital of h[n_L]."""
        n_right = 2.0 - n_left
        h = np.array([[-delta / 2 + u * n_left / 2, -t],
                      [-t, delta / 2 + u * n_right / 2]])
        values, vectors = np.linalg.eigh(h)  # levels in increasing order
        return 2.0 * vectors[0, 0] ** 2  # two electrons, |c_L|^2 each


    def G(x, delta=DELTA, t=T_HOP, u=U):
        """The reduced map x_out = G(x), x = n_L - 1."""
        shift = delta - u * x
        return shift / np.sqrt(shift ** 2 + 4.0 * t * t)


    inputs = np.linspace(0.0, 2.0, 41)
    worst = max(abs(loop_pass(n) - 1.0 - G(n - 1.0)) for n in inputs)
    check(worst < 1e-12, "the 2 x 2 diagonalisation and the reduced map G agree")
    '''),
    md(r"""
    The next cell finds the fixed point $x^*$ by bisection on $x - G(x)$, which increases
    with $x$ (because $G$ decreases), computes the slope $G'(x^*)$ from the formula and
    from a difference quotient, and the largest and the best mixing parameters,
    $\beta_{max} = 2/(1 - G')$ and $\beta_{best} = 1/(1 - G')$ (which makes the factor
    zero).
    """),
    code(r'''
    def fixed_point(delta=DELTA, t=T_HOP, u=U):
        """x* with G(x*) = x*, by bisection on [-1, 1] (x - G(x) increases)."""
        low, high = -1.0, 1.0
        for _ in range(80):
            middle = 0.5 * (low + high)
            if middle - G(middle, delta, t, u) > 0.0:
                high = middle
            else:
                low = middle
        return 0.5 * (low + high)


    def slope(x, delta=DELTA, t=T_HOP, u=U):
        """G'(x) = -4 U t^2 / ((Delta - U x)^2 + 4 t^2)^(3/2)."""
        return -4.0 * u * t * t / ((delta - u * x) ** 2 + 4.0 * t * t) ** 1.5


    x_star = fixed_point()
    g_prime = slope(x_star)
    quotient = (G(x_star + 1e-6) - G(x_star - 1e-6)) / 2e-6
    beta_max, beta_best = 2.0 / (1.0 - g_prime), 1.0 / (1.0 - g_prime)
    report("fixed point n_L* = 1 + x*", f"{1.0 + x_star:.6f}")
    report("slope G'(x*)", f"{g_prime:.6f}")
    report("largest mixing parameter 2/(1 - G')", f"{beta_max:.6f}")
    report("best mixing parameter 1/(1 - G')", f"{beta_best:.6f}")
    check(abs(x_star - 0.326993) < 1e-6 and abs(g_prime + 1.687961) < 1e-6
          and abs(beta_max - 0.744058) < 1e-6,
          "x* = 0.326993, G'(x*) = -1.687961, beta_max = 0.744058")
    check(abs(quotient - g_prime) < 1e-6, "the slope formula equals a difference quotient")
    '''),
    md(r"""
    The next cell draws the output density against the input density, the diagonal
    $n^{out} = n^{in}$ (where the fixed point lies) and the fixed point.
    """),
    code(r'''
    n_in = np.linspace(0.0, 2.0, 401)
    fig, ax = plt.subplots(figsize=(6.0, 5.0))
    ax.plot(n_in, 1.0 + G(n_in - 1.0), color="black", lw=2.0,
            label="$n_L^{out} = 1 + G(n_L - 1)$")
    ax.plot(n_in, n_in, "--", color="gray", label="diagonal $n_L^{out} = n_L$")
    ax.plot([1.0 + x_star], [1.0 + x_star], "ro",
            label=f"fixed point $n_L^* = {1.0 + x_star:.6f}$")
    ax.set_xlabel("input density on the left site $n_L$")
    ax.set_ylabel("output density $n_L^{out}$")
    ax.set_title("The self-consistency map of the two-site model")
    ax.legend(fontsize=8)
    save_figure(fig, "reduced_map",
                "The output density on the left site produced by one pass of the "
                "mean-field loop, against the input density (both in electrons, from 0 "
                "to 2), for $\\Delta = 2$, $t = 1$, $U = 4$; the dashed diagonal marks "
                "equal input and output, and the red point is the self-consistent "
                "solution $n_L^\\ast = 1.326993$. The curve falls steeply through the "
                "diagonal (slope $-1.69$): more charge on the left pushes even more "
                "charge to the right.")
    '''),
    md(r"""
    ## 6. Plain iteration: charge sloshing

    The next cell runs plain iteration ($n_L \leftarrow n_L^{out}$) from $n_L = 2$, prints
    the first six passes, and then runs 2000 more passes: the input jumps between two
    values forever (a cycle of period 2), never reaching the fixed point.
    """),
    code(r'''
    def iterate(beta, start=2.0, passes=6):
        """Inputs and outputs of the loop with linear mixing (beta = 1: plain)."""
        n, history = start, []
        for _ in range(passes):
            out = loop_pass(n)
            history.append((n, out))
            n = (1.0 - beta) * n + beta * out
        return history, n


    plain, _ = iterate(1.0)
    say("step   n_L in     n_L out")
    for step, (n, out) in enumerate(plain):
        say(f"{step:4d}   {n:.6f}   {out:.6f}")
    expected_in = [2.000000, 0.292893, 1.923880, 0.353344, 1.916644, 0.359836]
    check(all(abs(n - e) < 1e-6 for (n, _), e in zip(plain, expected_in)),
          "plain iteration reproduces the table 2.000000, 0.292893, 1.923880, ...")
    _, late = iterate(1.0, passes=2000)
    cycle = sorted([late, loop_pass(late)])
    say(f"after 2000 passes the input alternates between {cycle[0]:.4f} and "
        f"{cycle[1]:.4f}")
    check(abs(loop_pass(loop_pass(late)) - late) < 1e-10 and cycle[1] - cycle[0] > 1.5,
          "plain iteration ends in a cycle of period 2 (about 0.3607 and 1.9157)")
    '''),
    md(r"""
    ## 7. Linear mixing with beta = 1/2

    The next cell prints the first six passes with $\beta = 1/2$ and counts the passes
    until the input and the output agree to $10^{-6}$.
    """),
    code(r'''
    mixed, _ = iterate(0.5)
    say("step   n_L in     n_L out")
    for step, (n, out) in enumerate(mixed):
        say(f"{step:4d}   {n:.6f}   {out:.6f}")
    expected_in = [2.000000, 1.146447, 1.361898, 1.314066, 1.331307, 1.325494]
    check(all(abs(n - e) < 1e-6 for (n, _), e in zip(mixed, expected_in)),
          "linear mixing with beta = 1/2 reproduces the table 2.000000, 1.146447, ...")
    long_history, _ = iterate(0.5, passes=40)
    agree = next(step for step, (n, out) in enumerate(long_history)
                 if abs(n - out) < 1e-6)
    report("passes until input and output agree to 1e-6 (beta = 1/2)", agree)
    check(agree == 13 and abs(long_history[-1][0] - 1.326993) < 1e-6,
          "beta = 1/2 converges to 1.326993; input and output agree after 13 passes")
    '''),
    md(r"""
    The next cell draws the two iterations as cobweb diagrams: from an input on the
    horizontal axis go up to the map curve (the output), then across to the mixed next
    input (for plain iteration: to the diagonal), and repeat.
    """),
    code(r'''
    def cobweb(ax, beta, passes):
        """Draw the cobweb of the loop with mixing beta on the axes ax."""
        ax.plot(n_in, 1.0 + G(n_in - 1.0), color="black", lw=1.5)
        ax.plot(n_in, n_in, "--", color="gray", lw=0.8)
        history, _ = iterate(beta, passes=passes)
        for n, out in history:
            n_next = (1.0 - beta) * n + beta * out
            ax.plot([n, n], [n, out], color="tab:red", lw=0.8)  # up to the curve
            ax.plot([n, n_next], [out, n_next], color="tab:blue", lw=0.8)  # across
        ax.plot([1.0 + x_star], [1.0 + x_star], "ko")
        ax.set_xlabel("input $n_L$")
        ax.set_ylabel("output $n_L^{out}$ and next input")


    fig, (left, right) = plt.subplots(1, 2, figsize=(10.0, 4.5))
    cobweb(left, 1.0, 12)
    left.set_title("plain iteration ($\\beta = 1$): sloshing")
    cobweb(right, 0.5, 12)
    right.set_title("linear mixing ($\\beta = 1/2$): converges")
    save_figure(fig, "cobwebs",
                "Cobweb diagrams of the first 12 passes of the two-site loop, starting "
                "at $n_L = 2$: the black curve is the map (output against input), the "
                "dashed line the diagonal, red segments go from an input to its output, "
                "blue segments from the output to the next input. Left, plain "
                "iteration: the path settles on a square around the fixed point (black "
                "dot), a cycle of period 2. Right, linear mixing with $\\beta = 1/2$: "
                "the path spirals into the fixed point.")
    '''),
    md(r"""
    ## 8. Error histories and the convergence factor

    The next cell runs the loop for $\beta = 1, 0.8, 0.5, 0.2$ and for the best value
    $\beta_{best} = 0.372$, and also with Anderson mixing (depth 6, $\beta = 0.4$, the
    settings of the Revision Kohn-Sham solver; for one variable Anderson mixing
    estimates the slope of $G$ from the last passes, like the secant method), and
    records the error $|n_L - n_L^*|$ of every input. It checks the measured ratio of
    successive errors for $\beta = 1/2$ against the predicted factor
    $1 - \beta(1 - G') = -0.344$.
    """),
    code(r'''
    def errors_linear(beta, passes=60):
        """|n_L - n_L*| of the inputs of linear mixing."""
        history, _ = iterate(beta, passes=passes)
        return np.array([abs(n - 1.0 - x_star) for n, _ in history])


    def errors_anderson(beta=0.4, depth=6, passes=60, tolerance=1e-14):
        """|n_L - n_L*| of the inputs of Anderson mixing (one variable)."""
        n, inputs, residuals, errors = 2.0, [], [], []
        for _ in range(passes):
            errors.append(abs(n - 1.0 - x_star))
            residual = loop_pass(n) - n
            if abs(residual) < tolerance:
                break
            inputs, residuals = (inputs + [n])[-depth:], (residuals + [residual])[-depth:]
            if len(inputs) == 1:
                n = n + beta * residual
                continue
            last = residuals[-1]
            differences = np.array([[r - last for r in residuals[:-1]]])  # 1 row
            theta = np.linalg.lstsq(differences, -np.array([last]), rcond=None)[0]
            c = np.append(theta, 1.0 - theta.sum())
            n = float(sum(ci * (ni + beta * ri)
                          for ci, ni, ri in zip(c, inputs, residuals)))
        return np.array(errors)


    histories = {beta: errors_linear(beta) for beta in (1.0, 0.8, 0.5, 0.2)}
    histories["best"] = errors_linear(beta_best)
    anderson_errors = errors_anderson()
    ratio = histories[0.5][11] / histories[0.5][10]  # the ratio of two error sizes
    predicted = 1.0 - 0.5 * (1.0 - g_prime)
    report("measured |error ratio| for beta = 1/2", f"{ratio:.6f}")
    report("predicted factor 1 - beta (1 - G')", f"{predicted:.6f}")
    check(abs(ratio - abs(predicted)) < 1e-4,
          "the error shrinks by the predicted factor |1 - beta(1 - G')| = 0.344")
    check(histories[1.0][-1] > 0.5 and histories[0.8][-1] > 0.1,
          "beta = 1 and beta = 0.8 (above 0.744) do not converge")
    check(len(anderson_errors) < 15 and anderson_errors[-1] < 1e-12,
          "Anderson mixing converges to 1e-12 in fewer than 15 passes")
    '''),
    md(r"""
    The next cell draws the error histories on a logarithmic vertical axis.
    """),
    code(r'''
    fig, ax = plt.subplots()
    for key, style in ((1.0, "o-"), (0.8, "s-"), (0.5, "^-"), (0.2, "v-")):
        label = "plain iteration" if key == 1.0 else f"linear, $\\beta = {key}$"
        ax.semilogy(histories[key][:40], style, ms=3, label=label)
    best = np.maximum(histories["best"][:12], 1e-16)  # rounding may give exactly 0
    ax.semilogy(best, "D-", ms=3, label=f"linear, best $\\beta = {beta_best:.3f}$")
    ax.semilogy(anderson_errors, "k*-", ms=6, label="Anderson, depth 6, $\\beta = 0.4$")
    ax.set_ylim(1e-15, 10.0)
    ax.set_xlabel("pass number")
    ax.set_ylabel("error $|n_L - n_L^*|$")
    ax.set_title("Error histories of the two-site loop")
    ax.legend(fontsize=7, loc="upper right", bbox_to_anchor=(1.0, 0.86))
    save_figure(fig, "error_histories",
                "The distance $|n_L - n_L^\\ast|$ of the input from the self-consistent "
                "density (logarithmic vertical axis, electrons) against the pass number "
                "for plain iteration and linear mixing with $\\beta = 0.8$ (both stay "
                "far away: sloshing), $\\beta = 0.5$ and $0.2$ (straight lines: the error "
                "shrinks by a fixed factor per pass), the best $\\beta = 0.372$ (very "
                "fast) and Anderson mixing with the Revision solver's settings (fast "
                "without knowing the slope in advance).")
    '''),
    md(r"""
    The next cell draws the predicted factor $|1 - \beta(1 - G')|$ against $\beta$; the
    loop converges where it is below 1.
    """),
    code(r'''
    betas = np.linspace(0.0, 1.0, 501)
    factor = np.abs(1.0 - betas * (1.0 - g_prime))
    fig, ax = plt.subplots()
    ax.plot(betas, factor, color="black", lw=2.0, label="$|1 - \\beta(1 - G')|$")
    ax.axhline(1.0, color="gray", ls="--")
    ax.axvspan(0.0, beta_max, alpha=0.15, color="green", label="converges")
    ax.axvline(beta_best, color="tab:blue", ls=":",
               label=f"best $\\beta = {beta_best:.3f}$")
    ax.set_xlabel("mixing parameter $\\beta$")
    ax.set_ylabel("error factor per pass")
    ax.set_title(f"Linear mixing converges for $\\beta < {beta_max:.4f}$")
    ax.legend()
    save_figure(fig, "convergence_factor",
                "The factor $|1 - \\beta(1 - G'(x^\\ast))|$ by which one pass of linear "
                "mixing multiplies the error near the fixed point, against the mixing "
                "parameter $\\beta$ (pure numbers), for $G'(x^\\ast) = -1.688$. The loop "
                "converges where the factor is below 1 (green band, "
                "$0 < \\beta < 0.744$); the factor is zero at the best value "
                "$\\beta = 0.372$, and plain iteration ($\\beta = 1$) has the factor "
                "1.688: the error grows.")
    '''),
    md(r"""
    ## 9. The long run against the mixing parameter

    The next cell runs the loop with 99 values of $\beta$ from 0.02 to 1 for 600
    passes each and keeps the last 30 inputs. Where the loop converges they are all the
    same number; where it does not, they alternate between two numbers.
    """),
    code(r'''
    beta_scan = np.linspace(0.02, 1.0, 99)
    tails = []
    for beta in beta_scan:
        history, _ = iterate(beta, passes=600)
        tails.append([n for n, _ in history[-30:]])
    tails = np.array(tails)
    spread = tails.max(axis=1) - tails.min(axis=1)
    check(np.all(spread[beta_scan < 0.72] < 1e-8) and np.all(spread[beta_scan > 0.77]
                                                            > 0.05),
          "the loop converges below beta = 0.744 and oscillates above it")
    fig, ax = plt.subplots()
    for beta, tail in zip(beta_scan, tails):
        ax.plot(np.full(len(tail), beta), tail, "k.", ms=2)
    ax.axvline(beta_max, color="tab:red", ls="--", label=f"$\\beta_{{max}} = "
               f"{beta_max:.4f}$")
    ax.set_xlabel("mixing parameter $\\beta$")
    ax.set_ylabel("last 30 inputs $n_L$")
    ax.set_title("Where the loop ends, against $\\beta$")
    ax.legend()
    save_figure(fig, "long_run_diagram",
                "The last 30 inputs $n_L$ (electrons) of 600 passes of the two-site loop "
                "for 99 mixing parameters $\\beta$ from 0.02 to 1 (horizontal axis). "
                "Below $\\beta_{max} = 0.744$ (dashed red line) all points coincide at "
                "the self-consistent density 1.327; above it the loop ends in a cycle "
                "of period 2 whose two values move apart as $\\beta$ grows, reaching "
                "0.36 and 1.92 for plain iteration.")
    '''),
    md(r"""
    ## 10. A weaker repulsion, and the threshold against U

    With $U = 2$ the slope at the fixed point is milder, and $\beta_{max} > 1$: even
    plain iteration converges (slowly, alternating). The next cell checks the numbers
    $x^* = 0.468990$, $G' = -0.688942$, $\beta_{max} = 1.184174$, and then computes
    $\beta_{max}$ for repulsions from 0.5 to 8, and finds by bisection the repulsion at
    which plain iteration stops converging ($\beta_{max} = 1$, i.e. $G'(x^*) = -1$).
    """),
    code(r'''
    x2 = fixed_point(u=2.0)
    g2 = slope(x2, u=2.0)
    report("U = 2: n_L*", f"{1.0 + x2:.6f}")
    report("U = 2: G'(x*)", f"{g2:.6f}")
    report("U = 2: beta_max", f"{2.0 / (1.0 - g2):.6f}")
    check(abs(x2 - 0.468990) < 1e-6 and abs(g2 + 0.688942) < 1e-6
          and abs(2.0 / (1.0 - g2) - 1.184174) < 1e-6,
          "U = 2: x* = 0.468990, G' = -0.688942, beta_max = 1.184174")
    n = 2.0
    for _ in range(200):  # plain iteration with U = 2
        n = loop_pass(n, u=2.0)
    check(abs(n - 1.0 - x2) < 1e-10, "U = 2: plain iteration converges")
    U_scan = np.linspace(0.5, 8.0, 76)
    beta_limits = np.array([2.0 / (1.0 - slope(fixed_point(u=u), u=u)) for u in U_scan])
    low, high = 2.0, 4.0  # beta_max(2) > 1 > beta_max(4)
    for _ in range(60):
        middle = 0.5 * (low + high)
        if 2.0 / (1.0 - slope(fixed_point(u=middle), u=middle)) > 1.0:
            low = middle
        else:
            high = middle
    U_critical = 0.5 * (low + high)
    report("repulsion where plain iteration stops converging", f"{U_critical:.6f}")
    check(abs(slope(fixed_point(u=U_critical), u=U_critical) + 1.0) < 1e-9,
          "at this repulsion the slope at the fixed point is exactly -1")
    '''),
    md(r"""
    The next cell draws $\beta_{max}$ against $U$.
    """),
    code(r'''
    fig, ax = plt.subplots()
    ax.plot(U_scan, beta_limits, color="black", lw=2.0, label="$\\beta_{max}(U)$")
    ax.axhline(1.0, color="gray", ls="--", label="plain iteration, $\\beta = 1$")
    ax.axvline(U_critical, color="tab:red", ls=":",
               label=f"$U = {U_critical:.3f}$: plain iteration fails beyond")
    ax.set_xlabel("repulsion $U$ (units of $t$)")
    ax.set_ylabel("largest convergent mixing parameter")
    ax.set_title("Stronger repulsion needs gentler mixing")
    ax.legend(fontsize=8)
    save_figure(fig, "threshold_versus_u",
                "The largest mixing parameter $\\beta_{max} = 2/(1 - G'(x^\\ast))$ for "
                "which linear mixing converges, against the repulsion $U$ (units of "
                "$t$; $\\Delta = 2$, $t = 1$). Below the dashed line $\\beta = 1$ plain "
                "iteration fails; this happens beyond the repulsion marked by the "
                "dotted line. The stronger the feedback of the density on its own "
                "potential, the smaller the step the loop may take.")
    '''),
    md(r"""
    ## 11. The last check

    The last cell checks that all six figure files exist and prints the number of
    checks that passed.
    """),
    code(r'''
    figure_names = ["reduced_map", "cobwebs", "error_histories", "convergence_factor",
                    "long_run_diagram", "threshold_versus_u"]
    missing = [name for k, name in enumerate(figure_names, 1)
               if not output_file(f"{FIGURE_FOLDER}/13d_{k}_{name}.png").is_file()]
    check(missing == [], "all six figure files exist")
    check(output_file(f"{FIGURE_FOLDER}/13d_6_threshold_versus_u.png").is_file(),
          "the figure file 13d_6_threshold_versus_u.png exists")
    all_checks_passed()
    '''),
    md(r"""
    ## 12. What this notebook showed

    - The whole self-consistency loop of the two-site mean-field model is one function
      $G(x) = (\Delta - Ux)/\sqrt{(\Delta - Ux)^2 + 4t^2}$ of one number, and its fixed
      point is the self-consistent density $n_L^* = 1.326993$.
    - Plain iteration fails: the charge jumps between the sites forever (a cycle of
      period 2 near 0.3607 and 1.9157), because the slope $G'(x^*) = -1.688$ is steeper
      than $-1$.
    - Linear mixing converges exactly for $0 < \beta < 2/(1 - G') = 0.744058$; each pass
      multiplies the error by $1 - \beta(1 - G')$ ($-0.344$ for $\beta = 1/2$), and
      $\beta = 1/(1 - G') = 0.372$ is the fastest.
    - Anderson mixing, which estimates the slope from earlier passes, converges in a
      few passes without tuning; the Revision Kohn-Sham solver of the dirac16complex
      field uses it (depth 6, $\beta = 0.4$).
    - The stronger the repulsion, the smaller the step the loop may take; for
      $\Delta = 2$, $t = 1$ plain iteration converges only for $U$ below the printed
      threshold (for example $U = 2$: $\beta_{max} = 1.184$).
    """),
]

if __name__ == "__main__":
    raise SystemExit(run_builder(__file__))
