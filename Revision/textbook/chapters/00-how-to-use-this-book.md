## 0. How to use this book

This chapter is the map of the book. It says what the book teaches, how every worked example comes with a complete Jupyter notebook that you can run yourself, which software you need, and how every statement of the book is labelled so that you always know whether it is proved, computed, assumed, a hypothesis or an open question. Its example is the first notebook of the book, Notebook 00a, which checks that your computer is ready. (This is a draft of the chapter; it is completed with the full honesty ledger when the other chapters are written.)

### 0.1 What this book teaches

The book is about a model of the very early universe proposed by the author. The universe of the model has eight directions instead of the four of everyday space and time. They are named $x_1$ to $x_8$, as the author names them. Three of them, $x_1$, $x_2$ and $x_3$, are the directions of ordinary space. One, $x_4$, is the time in which everything evolves. Three more, $x_5$, $x_6$ and $x_7$, behave like time as well; they are called the **extra times**. The last one, $x_8$, is a **hidden** space direction. The author's metric (the rule that gives the length of a small step in each direction, introduced from zero later in the book) makes ordinary space grow (inflate) and the three extra times shrink (deflate) exponentially as the time $x_4$ runs.

Two fields live in this universe. A **field** is a rule that attaches numbers to every point of space and time. The field **dirac16complex** attaches sixteen complex numbers of a special kind (anticommuting numbers, defined later) to every point; the field **dirac16complex00** attaches sixteen ordinary complex numbers. The book sets up the mathematics of both fields, derives their equations, introduces the density-functional (DFT) approximation and solves the equations as far as present knowledge allows. It then asks two questions honestly: do the equations prove that the big bang creates universes in pairs, and does the theory solve the puzzle of matter and antimatter? The answers, with complete proofs of what is proved and a precise list of what is not, are given in Part V.

### 0.2 Every example is a notebook

Every worked example of the book is a **Jupyter notebook**: a file that holds text and Python code in **cells**, together with everything the code printed and drew when it ran. The book prints every notebook in full, in three parts:

- a section "How to run Notebook NNx", where NN is the number of the chapter and x a letter, which gives the complete instructions for running the notebook on Windows, macOS and Linux, without sending you anywhere else;
- a section "Notebook NNx: complete text", which prints every cell of the notebook in order, with what each code cell printed and every figure it drew;
- a section "Line-by-line walk-through of Notebook NNx", which explains every line of every code cell.

Every notebook has the same numbered sections: what it computes, how to run it, the words it uses, the physical and mathematical situation, the computation in small steps, and what it showed. Every computation is followed by **checks**: statements that must be true. When a check is true the notebook prints a line that starts with PASS; when it is false the notebook stops with an error that names the check. A notebook that reproduces a number of the Revision record (the computations stored in the folder Revision of the repository) names the record file and its check in the PASS line.

Every notebook is built and checked by the book's tool nbkit: it is run twice, and the second run must reproduce the stored notebook and every file it writes exactly, byte for byte. Each notebook has a **provenance file** next to it (the same name with the ending `.PROVENANCE.md`), which records what the notebook computes, the complete instructions, the expected output, every file it writes, its run time and the computer it was run on.

### 0.3 The software you need

You need a computer with Windows 11, macOS or Linux, the program Git, Python 3.12 or newer, and nine Python packages at fixed versions (numpy, sympy, mpmath, matplotlib, jupyterlab, nbformat, nbclient, ipykernel and nbconvert). A few notebooks also need Rust, the language of the longest computations of the repository. You do not need Wolfram Mathematica or any other paid program. The complete installation instructions are printed before every notebook, in Section 0.6 for the first time; you follow them once, and every later notebook needs only the steps that start JupyterLab.

### 0.4 The five labels of every statement

Every statement of the book carries one of five labels, so that you always know how much it is worth:

| label | meaning |
| --- | --- |
| PROVED | exact; the book gives the complete proof, and a computer-algebra check confirms it (the check is named) |
| COMPUTED | a number from a numerical computation, with its measured uncertainty and the file that holds it |
| ASSUMED | an assumption that the book does not derive; everything that depends on it says so |
| HYPOTHESIS | an idea that is stated and examined but not established |
| OPEN | a question that nobody has answered yet |

The rule above every other rule of the book is honesty: it never writes "proved" for a statement that is not proved.

### 0.5 Example: checking the installation

The first notebook computes no physics. It checks that Python and the packages are installed at the right versions, prints the version of cargo (the Rust build program) when it is installed, does one small computation with each of the packages numpy, sympy and mpmath, and draws two teaching plots. Run it first: if it ends with the line ALL 9 CHECKS PASSED (notebook 00a), every notebook of the book can run on your computer.

<!-- NOTEBOOK 00a -->

### 0.8 Line-by-line walk-through of Notebook 00a

The notebook has ten code cells, In [1] to In [10]. This section explains every line of every one of them.

**In [1], the set-up cell.** Its first part is the complete run instructions of Section 0.6 again, as comment lines: every line that starts with `#` is a **comment**, which Python skips. They are there so that the notebook file carries its own instructions. The code starts after the line of `=` signs.

```python
import json  # reads and writes JSON files (text files that hold names and numbers)
import os  # reads the environment variable TEXTBOOK_OUTPUT_ROOT (explained below)
import textwrap  # breaks long printed text into lines of at most 89 characters
from pathlib import Path  # file and folder paths that work on Windows, macOS and Linux
```

`import` loads a **module** (a part of Python or of a package) so that the code can use it. `json`, `os`, `textwrap` and `pathlib` come with Python itself. `from pathlib import Path` takes the single name `Path` out of the module `pathlib`; a `Path` is the address of a file or folder, written the same way on every operating system.

```python
import matplotlib  # the plotting package
import matplotlib.pyplot as plt  # its drawing functions, called plt by convention
from IPython.display import Image, display  # shows a saved picture below a cell
```

These lines load the plotting package matplotlib and its drawing functions under the short name `plt`, and the two functions `Image` and `display` of IPython (the part of Jupyter that runs Python code), which show a picture file below a cell.

```python
NOTEBOOK_ID = "00a"  # this notebook: chapter 00, example a
```

A **variable** is a name for a value; this line gives the name `NOTEBOOK_ID` to the text `"00a"` (a text in quotes is called a **string**). The figure files of the notebook are named after it.

```python
def find_repository_root():
    here = Path.cwd().resolve()  # the folder in which this notebook runs
    for folder in [here, *here.parents]:  # this folder, its parent, its grandparent ...
        if (folder / "Revision" / "textbook" / "requirements.txt").is_file():
            return folder
    raise FileNotFoundError(
        "The repository folder was not found: open this notebook inside the folder "
        "Revision/textbook/notebooks of the repository Dirac_claude")
```

`def` defines a **function**: a named piece of code that runs when it is called. (The function in the notebook also has a **docstring**, the text in triple quotes below the `def` line, which says what it does; we leave it out here.) `Path.cwd()` is the folder in which the notebook runs, and `.resolve()` writes it as a complete address. `here.parents` lists the parent folder, its parent, and so on up to the top of the disk; `[here, *here.parents]` is the list that starts with `here` and continues with all of them. The `for` loop takes the folders of this list one after the other. The operator `/` joins a folder and a name into a longer path, and `.is_file()` is true when that file exists. The first folder that contains `Revision/textbook/requirements.txt` is the repository, and `return` hands it back. If no folder qualifies, `raise` stops the notebook with a `FileNotFoundError` whose message says what to do.

```python
REPO = find_repository_root()
OUTPUT_ROOT = Path(os.environ.get("TEXTBOOK_OUTPUT_ROOT", str(REPO)))
```

The first line calls the function and names its result `REPO`. The notebook never prints `REPO`, because the folder differs from computer to computer, while the printed output of a notebook must be the same everywhere. The second line chooses the folder below which the notebook writes its files. `os.environ` holds the **environment variables** of the running program (named texts that a program receives from the computer); `.get(name, default)` returns the value of the variable `TEXTBOOK_OUTPUT_ROOT` if it is set and the default `str(REPO)` (the repository folder as a string) otherwise. When you run the notebook the variable is not set, so the files go into the repository. The checking tool of the book sets it to a scratch folder, so that a check never changes the repository.

```python
def repository_file(relative):
    return REPO / relative


def output_file(relative):
    path = OUTPUT_ROOT / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    return path
```

Two small functions (their docstrings are left out here). `repository_file("Revision/...")` gives the full path of a file of the repository, for reading. `output_file("Revision/...")` gives the full path at which to write a file; `path.parent.mkdir(parents=True, exist_ok=True)` first creates the folder that will hold it, together with any missing folder above it, and does nothing if the folder exists.

```python
def say(text):
    print(textwrap.fill(str(text), width=89, subsequent_indent="    "))
```

`say` prints a text in lines of at most 89 characters, so that every printed line fits the width of a page of the book; `textwrap.fill` breaks the text at blanks, and every line after the first starts with four blanks.

```python
matplotlib.rcdefaults()  # ignore personal matplotlib settings: same figures everywhere
plt.rcParams.update({"figure.figsize": (7.0, 4.2), "font.size": 10.0,
                     "axes.grid": True, "grid.alpha": 0.3})
```

matplotlib reads personal settings from a file on your computer if you have one. `matplotlib.rcdefaults()` returns to the built-in settings, so that the figures are the same on every computer. `plt.rcParams.update({...})` then sets four settings for every figure of the notebook: the size of a figure (7.0 inches wide and 4.2 inches high), the size of its letters (10 points), and a faint grid of lines behind the curves (`grid.alpha` 0.3 means 30 per cent opaque). The braces `{...}` make a **dictionary**: pairs of a key and a value, written `key: value`.

```python
FIGURE_FOLDER = "Revision/textbook/figures"  # where the figures are saved
CAPTION_FILE = f"{FIGURE_FOLDER}/{NOTEBOOK_ID}.captions.json"  # their captions
FIGURE_NUMBERS = {}  # figure name -> its number k (file name <id>_<k>_<name>.png)
CAPTIONS = {}  # figure file name -> caption, written to CAPTION_FILE after every figure
output_file(CAPTION_FILE).write_text("{}\n", encoding="utf-8", newline="\n")
```

A string that starts with `f` is an **f-string**: every name in braces is replaced by its value, so `CAPTION_FILE` is `"Revision/textbook/figures/00a.captions.json"`. `FIGURE_NUMBERS` and `CAPTIONS` start as empty dictionaries. The last line writes the text `{}` and a line end into the captions file: an empty list of captions, which `save_figure` fills. `encoding="utf-8"` fixes how the letters are stored, and `newline="\n"` stores the same line end on every operating system.

```python
def save_figure(fig, name, caption):
    number = FIGURE_NUMBERS.setdefault(name, len(FIGURE_NUMBERS) + 1)
    file_name = f"{NOTEBOOK_ID}_{number}_{name}.png"
    relative = f"{FIGURE_FOLDER}/{file_name}"
    fig.savefig(output_file(relative), dpi=150, bbox_inches="tight",
                metadata={"Software": None})
    plt.close(fig)  # forget the figure, so that Jupyter does not draw it a second time
    CAPTIONS[file_name] = caption
    output_file(CAPTION_FILE).write_text(
        json.dumps(CAPTIONS, indent=1, sort_keys=True) + "\n", encoding="utf-8",
        newline="\n")
    display(Image(filename=str(output_file(relative))),
            metadata={"textbook_figure": file_name})  # the saved picture itself
    say(f"Figure {NOTEBOOK_ID}.{number} saved as {relative}")
```

This function (shown without its docstring and its three comment lines) saves a figure and shows it. `setdefault(name, value)` returns the number already stored for this figure name, or stores and returns `len(FIGURE_NUMBERS) + 1` (one more than the number of figures so far) for a new name; so the figures are numbered 1, 2, 3, ... and a cell that you run twice keeps the number of its figure. The file name is the notebook id, the number and the name, for example `00a_1_parabola_tangent.png`. `fig.savefig` writes the picture as a PNG file with 150 dots per inch (`dpi=150`), cuts away the empty margin (`bbox_inches="tight"`) and stores no program name in the file (`metadata={"Software": None}`), so that two runs write exactly the same bytes. `plt.close(fig)` removes the figure from memory, because Jupyter would otherwise draw it a second time at the end of the cell. The caption is stored in `CAPTIONS`, and the whole dictionary is written into the captions file (`json.dumps` turns it into JSON text, with one entry per line and the keys sorted). `display(Image(...))` shows the saved picture below the cell; the `metadata` entry tells the book's tools which file the picture is. The last line prints where the figure was saved.

```python
PASSED = []  # the names of the checks that passed, in order


def check(condition, name, record=None):
    if not condition:
        raise AssertionError(f"check failed: {name}")
    PASSED.append(name)
    say(f"PASS {name}")
    if record is not None:
        say(f"     reproduces {record}")
```

`PASSED` is an empty **list** (an ordered collection, written with square brackets). `check` is the function behind every check of the book. `condition` is a statement that is either true (`True`) or false (`False`). If it is false, `raise AssertionError(...)` stops the notebook with an error that names the check. (Python also has a statement `assert` for this; the book does not use it, because Python started with the option `-O` skips every `assert`.) If it is true, the name is appended to `PASSED` and a line `PASS name` is printed. `record=None` makes the third argument optional: a check that reproduces a number of the Revision record passes the record's file and check name, and `check` prints them on a second line.

```python
def report(label, value, unit=""):
    say(f"RESULT {label} = {value}" + (f" {unit}" if unit else ""))


def all_checks_passed():
    print(f"ALL {len(PASSED)} CHECKS PASSED (notebook {NOTEBOOK_ID})")


say(f"Set-up of notebook {NOTEBOOK_ID} complete: repository folder found, helpers "
    "defined.")
```

`report` prints a key number as a line that starts with RESULT; `(f" {unit}" if unit else "")` adds a blank and the unit when a unit is given and nothing otherwise. `all_checks_passed` prints the last line of every notebook; `len(PASSED)` is the number of checks that passed. The last statement prints the one line of output of In [1].

**In [2], Python.**

```python
import importlib.metadata  # reads the version numbers of installed packages
import platform  # reads the version number of Python

python_version = platform.python_version()  # a text such as "3.14.5"
say(f"Python version: {python_version}")
major, minor = (int(part) for part in python_version.split(".")[:2])
check((major, minor) >= (3, 12), "Python is version 3.12 or newer")
```

`platform.python_version()` returns the version of the running Python as a string, here `"3.14.5"`, which the next line prints. `python_version.split(".")` cuts the string at the dots into the list `["3", "14", "5"]`; `[:2]` keeps the first two entries; `int(part)` turns each into a whole number; and `major, minor = ...` names them 3 and 14. Python compares the pairs `(3, 14)` and `(3, 12)` like words in a dictionary: first numbers first, then, because they are equal, the second numbers; 14 is at least 12, so the condition is true and the check prints PASS Python is version 3.12 or newer.

**In [3], the packages.** The cell first writes the dictionary `PINNED` of the nine packages and their pinned versions (the versions with which the book was built). Then:

```python
for package, pinned in PINNED.items():
    installed = importlib.metadata.version(package)  # error if not installed
    say(f"{package:12} installed {installed:10} pinned {pinned}")
different = [p for p, v in PINNED.items() if importlib.metadata.version(p) != v]
check(different == [], "every package has its pinned version")
```

`PINNED.items()` gives the pairs (package, pinned version); the loop names them `package` and `pinned`. `importlib.metadata.version(package)` reads the installed version (and stops with an error if the package is not installed). In the f-string, `{package:12}` writes the name padded with blanks to 12 characters, so that the printed table has straight columns. The line `different = [...]` is a **list comprehension**: it collects every package `p` whose installed version differs from its pinned version `v` (`!=` means "is not equal to"). The check requires that this list is empty.

**In [4], cargo.**

```python
import shutil  # finds a program on the computer
import subprocess  # runs a program and reads what it prints

cargo = shutil.which("cargo")  # where cargo is, or None when it is not installed
if cargo is None:
    say("cargo is not installed; only the notebooks that run the Rust programs of "
        "the repository need it.")
else:
    completed = subprocess.run([cargo, "--version"], capture_output=True, text=True)
    say(f"cargo version: {completed.stdout.strip()}")
```

`shutil.which("cargo")` searches the folders where the computer looks for programs and returns the path of cargo, or the special value `None` if there is none. `if ... else` runs the first block when the condition is true and the second block otherwise. `subprocess.run([...])` runs cargo with the option that asks for its version (the two hyphens and the word version in the list); `capture_output=True, text=True` collects what it prints as a string in `completed.stdout`, and `.strip()` removes the line end. This cell prints but checks nothing, because most notebooks do not need cargo.

**In [5], numpy.**

```python
import numpy as np  # arrays of numbers, matrices, linear algebra

matrix = np.array([[1.0, 2.0], [3.0, 4.0]])  # the rows (1, 2) and (3, 4)
determinant = np.linalg.det(matrix)  # 1*4 - 2*3 = -2, up to rounding
report("determinant of the matrix with rows (1, 2) and (3, 4)", f"{determinant:.12f}")
check(abs(determinant - (-2.0)) < 1e-12, "numpy: the determinant is -2")
```

`np.array` makes a matrix from the list of its rows. `np.linalg.det` computes its determinant, $1 \cdot 4 - 2 \cdot 3 = -2$, in floating-point arithmetic, which keeps about 16 significant digits and may be wrong in the last one. `{determinant:.12f}` prints the number with 12 digits after the decimal point. `abs(...)` is the absolute value, and `1e-12` means $10^{-12}$: the check accepts the result when it differs from $-2$ by less than $10^{-12}$.

**In [6], sympy.**

```python
import sympy as sp  # exact algebra and calculus with symbols

x = sp.symbols("x")  # a symbol: a letter that stands for any number
derivative = sp.diff(sp.sin(x) ** 2, x)  # the derivative of sin(x)^2 with respect to x
say(f"d/dx sin(x)^2 = {derivative}")
check(sp.simplify(derivative - sp.sin(2 * x)) == 0,
      "sympy: the derivative of sin(x)^2 is sin(2x)")
```

`sp.symbols("x")` makes the symbol $x$. In Python `**` means "to the power", so `sp.sin(x) ** 2` is $\sin^2 x$, and `sp.diff(..., x)` differentiates it with respect to $x$; sympy prints the result as `2*sin(x)*cos(x)`. The check asks sympy to simplify $2 \sin x \cos x - \sin 2x$; the result is exactly 0 by the double-angle formula, and `== 0` tests that.

**In [7], mpmath.**

```python
import mpmath  # numbers with as many digits as we ask for

mpmath.mp.dps = 30  # dps = decimal places: work with 30 significant digits
pi_text = mpmath.nstr(mpmath.pi, 30)  # pi written with 30 significant digits
say(f"pi to 30 significant digits: {pi_text}")
check(pi_text == "3.14159265358979323846264338328", "mpmath: pi to 30 digits")
```

`mpmath.mp.dps = 30` tells mpmath to compute with 30 significant decimal digits. `mpmath.nstr(mpmath.pi, 30)` writes $\pi$ as a string with 30 significant digits, correctly rounded, and the check compares it with the known value letter by letter.

**In [8], the parabola and its tangent line.**

```python
x_values = np.linspace(-1.0, 3.0, 401)  # 401 equally spaced numbers from -1 to 3
parabola = x_values ** 2  # y = x^2 at each of these numbers
tangent = 2.0 * x_values - 1.0  # the tangent line y = 1 + 2 (x - 1) = 2x - 1
gap = parabola - tangent  # (x - 1)^2 at each number
```

`np.linspace(-1.0, 3.0, 401)` makes an **array** of 401 numbers from $-1$ to $3$ with equal steps of $4/400 = 0.01$. Arithmetic on an array acts on every number in it: `x_values ** 2` is the array of the 401 squares, and `2.0 * x_values - 1.0` the array of the 401 values of the tangent line. Their difference `gap` is $(x-1)^2$ at each point.

```python
fig, ax = plt.subplots()  # a new figure with one pair of axes
ax.plot(x_values, parabola, label="parabola $y = x^2$")
ax.plot(x_values, tangent, "--", label="tangent line $y = 2x - 1$")
ax.plot([1.0], [1.0], "o", color="black", label="the point $(1, 1)$")
ax.set_xlabel("$x$")  # the label of the horizontal axis
ax.set_ylabel("$y$")  # the label of the vertical axis
ax.set_title("A parabola and its tangent line at $x = 1$ (slope 2)")
ax.legend()  # the box that names the three curves
```

`plt.subplots()` makes a new figure `fig` with one pair of axes `ax`. `ax.plot(xs, ys)` draws a line through the points with these coordinates; the third argument of the second `ax.plot` line, a string of two hyphens, makes that line dashed, and `"o"` in the third one draws a dot instead of a line; `label=` is the name shown in the legend, and text between dollar signs is typeset as mathematics. The remaining lines label the axes, set the title and draw the legend.

```python
save_figure(fig, "parabola_tangent",
            "The parabola $y = x^2$ (solid line), its tangent line $y = 2x - 1$ at "
            ...)
check(gap.min() >= 0.0 and abs(gap[200]) < 1e-15,
      "the tangent line lies below the parabola and touches it at x = 1")
```

`save_figure` saves the figure as `00a_1_parabola_tangent.png` with its caption (the caption is printed in full in the notebook text above; Python joins the strings written next to each other into one). The check uses `gap.min()`, the smallest of the 401 numbers of `gap`, which must not be negative, and `gap[200]`, the entry number 200 counted from 0, which belongs to $x = -1 + 200 \cdot 0.01 = 1$ and must be 0.

**In [9], the two exponentials.**

```python
t = np.linspace(-2.0, 2.0, 401)  # 401 equally spaced numbers from -2 to 2
growing = np.exp(t)  # e^t
shrinking = np.exp(-t)  # e^(-t)
product = growing * shrinking  # e^t e^(-t), which is 1
```

`np.exp` is the exponential function, applied to every number of the array. The product of the two arrays is taken number by number. The plotting lines that follow work exactly as in In [8]; `":"` draws a dotted line. The cell saves the figure as `00a_2_growth_and_decay.png`, and its check

```python
check(np.max(np.abs(product - 1.0)) < 1e-14, "e^t times e^(-t) is 1 at every t")
```

computes the largest distance of the 401 products from 1 and requires it to be below $10^{-14}$: up to rounding, $e^{t} e^{-t} = 1$.

**In [10], the last check.**

```python
for name in ("00a_1_parabola_tangent.png", "00a_2_growth_and_decay.png"):
    check(output_file(f"{FIGURE_FOLDER}/{name}").is_file(),
          f"the figure file {name} exists")
all_checks_passed()
```

The loop checks that both figure files exist, and `all_checks_passed()` prints the last line, ALL 9 CHECKS PASSED (notebook 00a): one check in In [2], In [3], In [5], In [6], In [7], In [8] and In [9] each, and two in In [10].

### 0.9 The honesty ledger (draft)

The ledger lists the main statements of the book with their label and the record that verifies them. This draft holds the rows on pairs of universes and on matter and antimatter; the complete ledger is written when every chapter is finished. A report "with $n$ of $n$ checks passed" is a file of the Revision record in which a program has recorded $n$ checks, each with the verdict PASS.

| statement | label | where it is verified |
| --- | --- | --- |
| T1, T2 and Q: exact maps between the solutions of mass $+m$ and those of mass $-m$ (T2 with the Z2 mirror, which is ASSUMED) | PROVED | `Revision/pairing/reports/wolfram-pairing.json` (101 of 101 checks passed) and `Revision/pairing/reports/python-pairing.json` (66 of 66) |
| T3: the Kohn-Sham universes of mass $+M$ and $-M$ have equal energies and energy-momentum tensors | PROVED | `Revision/pairing/kohn_sham/reports/wolfram-t3.json` (10 of 10) and `Revision/pairing/kohn_sham/reports/python-t3.json` (13 of 13) |
| the big bang creates universes in pairs | OPEN: not proved; no creation process, rate or amplitude follows from the equations | Part V |
| the charge-conjugation matrices are $C$ and $\Gamma C$, and the U(1) charge is exactly conserved | PROVED | `Revision/lead_checks/reports/charge-conjugation-and-u1.json` (12 of 12) |
| the theory explains the excess of matter over antimatter | OPEN: the theory as built does not explain it | Part V |
| the Kohn-Sham history of $a_4$ is a prescribed background | ASSUMED: the recorded Kohn-Sham states are not admissible sources of the metric | `Revision/field_equations_a4/reports/ks-source-conditions.json` (5 of 5) |

### 0.10 What we proved, what we computed, what we assumed

- PROVED (in this chapter, by elementary algebra): the tangent line of $y = x^2$ at $x = 1$ is $y = 2x - 1$, it lies below the parabola because $x^2 - (2x - 1) = (x - 1)^2 \ge 0$, and $e^{t} e^{-t} = 1$ for every $t$.
- COMPUTED: Notebook 00a confirms both statements on 401 points each, up to rounding below $10^{-15}$ and $10^{-14}$, and computes a determinant, a derivative and 30 digits of $\pi$.
- ASSUMED: nothing.

### 0.11 Exercises

**Exercise 1.** The notebook checks that Python is 3.12 or newer by comparing the pairs (major, minor). Would the pair (4, 0) pass? Would (3, 9)?

*Answer.* Pairs are compared first by their first numbers. (4, 0): 4 is larger than 3, so (4, 0) is larger than (3, 12) and passes. (3, 9): the first numbers are equal, so the second numbers decide; 9 is smaller than 12, so (3, 9) is smaller than (3, 12) and fails.

**Exercise 2.** Find the tangent line of $y = x^2$ at $x = 2$ and show that it lies below the parabola.

*Answer.* The derivative of $x^2$ is $2x$, which is 4 at $x = 2$, and the parabola passes through $(2, 4)$. The line through $(2, 4)$ with slope 4 is $y = 4 + 4(x - 2) = 4x - 4$. Then $x^2 - (4x - 4) = x^2 - 4x + 4 = (x - 2)^2$, which is never negative and is zero only at $x = 2$.

**Exercise 3.** In In [8], which entry of the array `x_values` is $x = 0$?

*Answer.* The entries are $x = -1 + 0.01 k$ for $k = 0, 1, \dots, 400$. Setting $-1 + 0.01 k = 0$ gives $k = 100$: the entry `x_values[100]`.

**Exercise 4.** Compute the determinant of the matrix with rows $(2, 1)$ and $(4, 3)$ by hand, and say which line of In [5] you would change to let numpy check it.

*Answer.* $2 \cdot 3 - 1 \cdot 4 = 6 - 4 = 2$. Change the line `matrix = np.array([[1.0, 2.0], [3.0, 4.0]])` to `matrix = np.array([[2.0, 1.0], [4.0, 3.0]])`, and in the check replace `-2.0` by `2.0`.

**Exercise 5.** Show that $e^{a} e^{-a} = 1$ for every number $a$, and explain why this means that a length along ordinary space multiplied by $e^{a_4}$ and a length along an extra time multiplied by $e^{-a_4}$ change in opposite directions.

*Answer.* The exponential function turns sums into products, $e^{u} e^{v} = e^{u + v}$, so $e^{a} e^{-a} = e^{a - a} = e^{0} = 1$. When $a_4$ grows, $e^{a_4}$ grows; since the product of the two factors stays 1, $e^{-a_4} = 1 / e^{a_4}$ shrinks: ordinary space inflates while the extra times deflate.
