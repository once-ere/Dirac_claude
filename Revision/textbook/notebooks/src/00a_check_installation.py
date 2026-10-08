#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
"""Builder of Notebook 00a, "Checking the installation" (textbook "Universes in Pairs").

The notebook Revision/textbook/notebooks/00a_check_installation.ipynb is BUILT from this
file by Revision/textbook/tools/nbkit.py (never edit the .ipynb by hand):

    python Revision/textbook/tools/nbkit.py build \
        Revision/textbook/notebooks/src/00a_check_installation.py --date YYYY-MM-DD
    python Revision/textbook/tools/nbkit.py check \
        Revision/textbook/notebooks/src/00a_check_installation.py

The table of pinned versions inside the notebook is generated here from the [direct]
block of Revision/textbook/requirements.txt, so it always equals the pins.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools"))
from nbkit import code, md, run_builder  # noqa: E402
from run_instructions import load_pins  # noqa: E402

DIRECT, _ = load_pins()
# Eight blanks: four for the indentation of the cell text in this file (removed by
# dedent) and four for the entries of the dictionary in the notebook.
PINNED_LINES = "\n".join(f'        "{name}": "{version}",' for name, version in DIRECT)

FACTS = {
    "id": "00a",
    "name": "00a_check_installation",
    "title": "Checking the installation",
    "purpose": (
        "It prints the version of Python, of every Python package of the notebooks and "
        "of cargo (when cargo is installed), checks that every package has its pinned "
        "version, does one small computation with each of numpy, sympy and mpmath, and "
        "draws two teaching plots (a parabola with its tangent line, and a growing and "
        "a shrinking exponential)."
    ),
    "records": [],
    "packages": ["numpy", "sympy", "mpmath", "matplotlib"],
    "needs_rust": [],
    "expected_seconds": 10,
    "timeout_seconds": 120,
    "files_written": [
        "Revision/textbook/figures/00a.captions.json",
        "Revision/textbook/figures/00a_1_parabola_tangent.png",
        "Revision/textbook/figures/00a_2_growth_and_decay.png",
    ],
    "final_lines": [
        "PASS the figure file 00a_2_growth_and_decay.png exists",
        "ALL 9 CHECKS PASSED (notebook 00a)",
    ],
    "troubleshooting": [
        ["\"AssertionError: check failed: every package has its pinned version\"",
         "the table printed just above the error names each package with the installed "
         "and the pinned version; install the pinned versions again with the pip "
         "commands of Step 3 (with the environment active) and run the notebook again."],
        ["\"AssertionError: check failed: Python is version 3.12 or newer\"",
         "the environment was made with an older Python; delete the folder "
         "dirac-book-env in your home folder and repeat Step 3 with Python 3.12 or "
         "newer."],
        ["\"Jupyter command `jupyter-lab` not found\" or \"Jupyter command "
         "`jupyter-nbconvert` not found\" after a command that starts with "
         "`python -m jupyter`",
         "that form still has to find the programs jupyter-lab and jupyter-nbconvert in "
         "the folders where the terminal looks for programs, and it did not find them "
         "there. Do Step 4 and type `jupyter` again. Or start the two "
         "programs through Python itself, in the folder of the notebook: the first "
         "command below does what `jupyter lab` does in Step 5, the second what "
         "`jupyter nbconvert` does in Step 6.",
         ["python -m jupyterlab 00a_check_installation.ipynb",
          "python -m nbconvert --to notebook --execute --inplace "
          "00a_check_installation.ipynb"]],
    ],
}

CELLS = [
    md(r"""
    ## 1. What this notebook computes

    This is the first notebook of the book. It computes no physics. It checks that your
    computer has everything that the notebooks of the book need, and it shows how every
    notebook of the book works. It

    - prints the version of Python and of every Python package that the notebooks use,
      and checks that each package has exactly the version with which the book was
      built (its *pinned* version);
    - prints the version of cargo, the program that builds the Rust programs of the
      repository, when cargo is installed (only a few notebooks need it);
    - does one small computation with each of the packages numpy, sympy and mpmath and
      checks the results;
    - draws two teaching plots and saves them as picture files;
    - prints a line that starts with PASS for every check that passes, and as its last
      line the number of checks that passed.
    """),
    md(r"""
    ## 3. The words used in this notebook

    - **Python**: the programming language of the notebooks. A *version number* such as
      3.14.5 names one release of a program: the first number (3) changes rarely, the
      second (14) for new features, the third (5) for corrections.
    - **Package**: a collection of Python code that someone else wrote and that we
      *import* (load) to use it: numpy (arrays of numbers and matrices), sympy (exact
      algebra and calculus with symbols), mpmath (numbers with as many digits as we
      want), matplotlib (plots).
    - **Pinned version**: the exact version of a package with which the book was built.
      Another version may print slightly different numbers or pictures.
    - **Private environment**: a folder with its own copy of Python and of the packages,
      so that installing them changes nothing else on the computer.
    - **Notebook, cell, kernel**: a notebook is a file made of *cells*. A *markdown
      cell* (like this one) holds text; a *code cell* holds Python code. The *kernel* is
      the running Python program that executes the code cells one after the other;
      what a code cell prints appears below it.
    - **Check**: a statement that must be true. The helper `check(condition, name)` of
      the set-up cell stops the notebook with an *AssertionError* when the condition is
      false, and prints `PASS name` when it is true.
    - **Figure, plot, axis**: a figure is a picture; a plot draws numbers as points or
      lines; the horizontal axis and the vertical axis are the two number lines of the
      plot. **PNG** is the file format in which the figures are saved.
    - **Rust, cargo**: Rust is a second programming language used for the longest
      computations of the repository; cargo is the program that turns Rust code into a
      program that the computer can run (it *builds* it).
    """),
    md(r"""
    ## 4. The physical and mathematical situation

    There is no physics in this notebook. The two plots are warm-ups for ideas that the
    book uses again and again.

    The first plot shows the parabola $y = x^2$ and its tangent line at the point
    $(1, 1)$. The slope of the tangent line is the derivative of $x^2$ at $x = 1$,
    namely $2x = 2$, so the line is $y = 1 + 2(x - 1) = 2x - 1$. The difference
    $x^2 - (2x - 1) = (x - 1)^2$ is never negative and is zero only at $x = 1$: the
    line touches the parabola at one point and lies below it everywhere else.

    The second plot shows a growing exponential $e^{t}$ and a shrinking exponential
    $e^{-t}$. Their product is $e^{t} e^{-t} = e^{t - t} = e^{0} = 1$ for every $t$. The
    author's metric has this pattern: lengths along the three directions of ordinary
    space carry the factor $e^{a_4}$ and lengths along the three extra times the factor
    $e^{-a_4}$, so when $a_4$ grows, ordinary space inflates and the extra times
    deflate.
    """),
    md(r"""
    ## 5. Python

    The next cell reads the version of Python that runs this notebook, prints it, and
    checks that it is 3.12 or newer.
    """),
    code(r'''
    import importlib.metadata  # reads the version numbers of installed packages
    import platform  # reads the version number of Python

    python_version = platform.python_version()  # a text such as "3.14.5"
    say(f"Python version: {python_version}")
    # The first two numbers of the version, as whole numbers: "3.14.5" -> 3 and 14.
    major, minor = (int(part) for part in python_version.split(".")[:2])
    # Pairs of numbers are compared like words in a dictionary: first the first number,
    # then, if they are equal, the second one.
    check((major, minor) >= (3, 12), "Python is version 3.12 or newer")
    '''),
    md(r"""
    ## 6. The packages and their versions

    The dictionary `PINNED` below holds, for each package, the version with which the
    book was built. The loop prints the installed and the pinned version of every
    package, one line each; then the check compares them.
    """),
    code(r'''
    PINNED = {  # package name -> the version with which the book was built
    @@PINNED@@
    }
    for package, pinned in PINNED.items():
        installed = importlib.metadata.version(package)  # error if not installed
        # {package:12} pads the name with blanks to 12 characters: aligned columns.
        say(f"{package:12} installed {installed:10} pinned {pinned}")
    # The packages whose installed version differs from the pinned one (a list):
    different = [p for p, v in PINNED.items() if importlib.metadata.version(p) != v]
    check(different == [], "every package has its pinned version")
    '''.replace("    @@PINNED@@", PINNED_LINES)),
    md(r"""
    ## 7. Rust (cargo)

    The next cell looks for the program cargo. If it is installed, the cell prints its
    version; if it is not, the cell says so. This is not a check: only the notebooks
    that run the Rust programs of the repository need cargo, and they say so in their
    instructions.
    """),
    code(r'''
    import shutil  # finds a program on the computer
    import subprocess  # runs a program and reads what it prints

    cargo = shutil.which("cargo")  # where cargo is, or None when it is not installed
    if cargo is None:
        say("cargo is not installed; only the notebooks that run the Rust programs of "
            "the repository need it.")
    else:
        completed = subprocess.run([cargo, "--version"], capture_output=True, text=True)
        say(f"cargo version: {completed.stdout.strip()}")
    '''),
    md(r"""
    ## 8. Three small computations

    **numpy.** The determinant of the $2 \times 2$ matrix with rows $(1, 2)$ and
    $(3, 4)$ is $1 \cdot 4 - 2 \cdot 3 = -2$. numpy computes it with floating-point
    numbers (numbers with about 16 significant digits), so the result may differ from
    $-2$ in the last digit; the check therefore allows a difference of $10^{-12}$.
    """),
    code(r'''
    import numpy as np  # arrays of numbers, matrices, linear algebra

    matrix = np.array([[1.0, 2.0], [3.0, 4.0]])  # the rows (1, 2) and (3, 4)
    determinant = np.linalg.det(matrix)  # 1*4 - 2*3 = -2, up to rounding
    report("determinant of the matrix with rows (1, 2) and (3, 4)", f"{determinant:.12f}")
    check(abs(determinant - (-2.0)) < 1e-12, "numpy: the determinant is -2")
    '''),
    md(r"""
    **sympy.** sympy computes exactly, with symbols. The derivative of $\sin^2 x$ is
    $2 \sin x \cos x$ by the chain rule, and $2 \sin x \cos x = \sin 2x$ by the
    double-angle formula. sympy prints the derivative in its own notation (`*` means
    times, `**` means power), and the check asks sympy to simplify the difference to
    zero.
    """),
    code(r'''
    import sympy as sp  # exact algebra and calculus with symbols

    x = sp.symbols("x")  # a symbol: a letter that stands for any number
    derivative = sp.diff(sp.sin(x) ** 2, x)  # the derivative of sin(x)^2 with respect to x
    say(f"d/dx sin(x)^2 = {derivative}")
    check(sp.simplify(derivative - sp.sin(2 * x)) == 0,
          "sympy: the derivative of sin(x)^2 is sin(2x)")
    '''),
    md(r"""
    **mpmath.** mpmath computes with as many digits as we ask for. The number $\pi$
    begins 3.141592653589793238462643383279502884. Its 30th significant digit is a 7
    and its 31st is a 9; because 9 is 5 or more, rounding to 30 significant digits
    raises the 7 to an 8: $\pi$ to 30 significant digits is
    3.14159265358979323846264338328.
    """),
    code(r'''
    import mpmath  # numbers with as many digits as we ask for

    mpmath.mp.dps = 30  # dps = decimal places: work with 30 significant digits
    pi_text = mpmath.nstr(mpmath.pi, 30)  # pi written with 30 significant digits
    say(f"pi to 30 significant digits: {pi_text}")
    check(pi_text == "3.14159265358979323846264338328", "mpmath: pi to 30 digits")
    '''),
    md(r"""
    ## 9. Two teaching plots

    The next cell draws the parabola $y = x^2$, its tangent line $y = 2x - 1$ at the
    point $(1, 1)$, and the point itself, for $x$ from $-1$ to $3$. `np.linspace(a, b,
    n)` makes $n$ equally spaced numbers from $a$ to $b$; arithmetic on such an array
    acts on every number of it. The check confirms that the parabola minus the line,
    $(x - 1)^2$, is never negative and is zero at $x = 1$.
    """),
    code(r'''
    x_values = np.linspace(-1.0, 3.0, 401)  # 401 equally spaced numbers from -1 to 3
    parabola = x_values ** 2  # y = x^2 at each of these numbers
    tangent = 2.0 * x_values - 1.0  # the tangent line y = 1 + 2 (x - 1) = 2x - 1
    gap = parabola - tangent  # (x - 1)^2 at each number

    fig, ax = plt.subplots()  # a new figure with one pair of axes
    ax.plot(x_values, parabola, label="parabola $y = x^2$")
    ax.plot(x_values, tangent, "--", label="tangent line $y = 2x - 1$")
    ax.plot([1.0], [1.0], "o", color="black", label="the point $(1, 1)$")
    ax.set_xlabel("$x$")  # the label of the horizontal axis
    ax.set_ylabel("$y$")  # the label of the vertical axis
    ax.set_title("A parabola and its tangent line at $x = 1$ (slope 2)")
    ax.legend()  # the box that names the three curves
    save_figure(fig, "parabola_tangent",
                "The parabola $y = x^2$ (solid line), its tangent line $y = 2x - 1$ at "
                "the point $(1, 1)$ (dashed line) and the point itself (black dot), for "
                "$x$ from $-1$ to $3$; horizontal axis $x$, vertical axis $y$ (pure "
                "numbers, no units). The line touches the parabola only at $(1, 1)$ "
                "and lies below it everywhere else; its slope $2$ is the derivative "
                "$2x$ of $x^2$ at $x = 1$.")
    check(gap.min() >= 0.0 and abs(gap[200]) < 1e-15,
          "the tangent line lies below the parabola and touches it at x = 1")
    '''),
    md(r"""
    The next cell draws $e^{t}$, $e^{-t}$ and their product for $t$ from $-2$ to $2$,
    and checks that the product equals 1 at all 401 points up to rounding (a
    difference of at most $10^{-14}$).
    """),
    code(r'''
    t = np.linspace(-2.0, 2.0, 401)  # 401 equally spaced numbers from -2 to 2
    growing = np.exp(t)  # e^t
    shrinking = np.exp(-t)  # e^(-t)
    product = growing * shrinking  # e^t e^(-t), which is 1

    fig, ax = plt.subplots()
    ax.plot(t, growing, label="$e^{t}$ (grows)")
    ax.plot(t, shrinking, "--", label="$e^{-t}$ (shrinks)")
    ax.plot(t, product, ":", color="black", label="the product $e^{t} e^{-t} = 1$")
    ax.set_xlabel("$t$")
    ax.set_ylabel("value")
    ax.set_title("A growing and a shrinking exponential")
    ax.legend()
    save_figure(fig, "growth_and_decay",
                "The growing exponential $e^{t}$ (solid line), the shrinking "
                "exponential $e^{-t}$ (dashed line) and their product (dotted line) "
                "for $t$ from $-2$ to $2$; horizontal axis $t$, vertical axis the value "
                "(pure numbers, no units). Each of the two curves is the mirror image "
                "of the other in the vertical axis $t = 0$, and their product is "
                "exactly $1$ at every $t$: what one factor gains, the other loses.")
    check(np.max(np.abs(product - 1.0)) < 1e-14, "e^t times e^(-t) is 1 at every t")
    '''),
    md(r"""
    ## 10. The last check

    The last cell checks that both figure files exist in the folder
    Revision/textbook/figures and prints the number of checks that passed.
    """),
    code(r'''
    for name in ("00a_1_parabola_tangent.png", "00a_2_growth_and_decay.png"):
        check(output_file(f"{FIGURE_FOLDER}/{name}").is_file(),
              f"the figure file {name} exists")
    all_checks_passed()
    '''),
    md(r"""
    ## 11. What this notebook showed

    - Python, the pinned packages and (when it is installed) cargo work on this
      computer: every notebook of the book can run here.
    - Every notebook of the book has the same form: numbered sections, a markdown cell
      before every code cell, checks that print PASS lines, figures saved with
      `save_figure`, and a last line that counts the checks.
    - A tangent line touches a parabola at one point and its slope is the derivative.
    - A growing and a shrinking exponential with opposite exponents have the product 1:
      the pattern of the author's metric, in which ordinary space inflates with
      $e^{a_4}$ while the three extra times deflate with $e^{-a_4}$.
    """),
]

if __name__ == "__main__":
    raise SystemExit(run_builder(__file__))
