"""Builder of the Revision notebook Revision/notebooks/dark_sector_hypotheses.ipynb.

The two dark-sector hypotheses of the Revision (SPEC sections 8 and 11) against the Supernovae Unite
values, for the corrected primordial metric of 2026-10-16 (version 2): Hypothesis (dirac16complex, the
Kohn-Sham gas along the deflating history a4 = H x4, b4 = b4(0) e^((4/3) H x4), recomputed with the Revision
Rust solver Revision/kohn_sham/solver, whose cell volume grows like e^((5/3) a4)) and Hypothesis00
(dirac16complex00, exact Fraction re-checks of the model tangents, the bound -4/9 of positive-energy models and
the ghost fraction the Unite w0 would need).  This file only DEFINES the cells; the tool
Revision/notebooks/tools/build_notebooks.py executes and normalises them:

    python Revision/notebooks/tools/build_notebooks.py build dark_sector_hypotheses
    python Revision/notebooks/tools/build_notebooks.py check dark_sector_hypotheses

Deterministic: the cells are fixed strings; the notebook prints no run time and no machine-specific
path.
"""

NAME = "dark_sector_hypotheses"
TITLE = "The dark-sector hypotheses of dirac16complex and dirac16complex00 against the Unite values"

_CELLS: list[tuple[str, str]] = []


def md(text: str) -> None:
    _CELLS.append(("markdown", text))


def code(text: str) -> None:
    _CELLS.append(("code", text))


def cells() -> list[tuple[str, str]]:
    return list(_CELLS)


# ------------------------------------------------------------------------------------------------
md(r"""
# The dark-sector hypotheses of dirac16complex and dirac16complex00 against the Unite values

*A Revision notebook of the repository Dirac_claude. It runs the Revision Rust Kohn-Sham solver
`Revision/kohn_sham/solver` along the deflating history of the corrected primordial metric,
recomputes the equation of state that a 3-space observer would infer, and checks every number against
the committed Revision record in `Revision/dark_sector/dirac16complex/` (Hypothesis) and
`Revision/dark_sector/dirac16complex00/` (Hypothesis00).*

## 1. What this notebook computes

The author asked (Revision/README.md) whether the 16-component fermion field dirac16complex
(**Hypothesis**) and the 16-component commuting field dirac16complex00 (**Hypothesis00**) provide a
possible physical mechanism for a time-varying dark-energy and/or dark-matter equation of state, and
how such an equation of state compares with the Supernovae Unite values quoted in Revision/README.md:
the constant-$w$ fit $w = -0.764$ and the CPL fit $w(a) = w_0 + w_a(1 - a)$ with
$(w_0, w_a) = (-0.861, -0.60)$. Neither hypothesis is established by the Revision record, and this
notebook does not establish either; it shows, step by step, what the record computed and re-checks it.

Everything here uses the corrected primordial metric of 2026-10-16 (version 2; `Revision/SPEC.md`
section 1), with the two functions $a_4(x_4)$ and $b_4(x_4)$ of the time ($b_4$ is never 1), in the author's
coordinates $x_0, \dots, x_7$. The earlier metrics (2026-10-14 and its version 1 of 2026-10-16) are
WITHDRAWN; they appear below only where a number is compared with them.

This notebook

1. builds the Revision Rust solver with `cargo build --release` and lets it recite its configuration
   (the metric forms and the theory coefficients it reads, the author's gamma matrices, the $2 \times 2$
   block reduction, the parameters of a run);
2. solves the Kohn-Sham gas of dirac16complex on the DENSE history $a_4 = 0, 0.05, \dots, 2$
   (41 slices) with $b_4 = b_4(0)\,e^{(4/3)a_4}$, for three series: N = 2352 and N = 592 without
   interaction, and N = 8 with the calibrated coupling $\hat\lambda = +\lambda_1$, held fixed while the cell
   volume grows like $e^{(5/3)a_4}$ (123 solver runs, with exactly the arguments of
   `Revision/dark_sector/dirac16complex/compute/run_ks_history.py`); it compares every row bit for bit
   with the committed `outputs/ks-history-dense.csv`;
3. recomputes the effective equations of state
   $w_\mathrm{eff}(A) = w_\mathrm{eff}(B) = P_3/E + (\frac{\beta}{2} - 1)(P_0 + 3P_t)/(3E)$ and
   $w_\mathrm{eff}(C) = w_\mathrm{eff}(A) - (4 - 2\beta)/3$ with $\beta = d\ln b_4/da_4 = 4/3$, the ratios
   $w_3, w_t, w_{x_0}$ and their derivatives exactly as `compute/compute_eos.py` does, and compares every
   row with `outputs/eos-history.csv`; it checks the conservation law with the terms of the deflating extra
   times and of the shrinking hidden direction;
4. recomputes the CPL tangents and least-squares CPL fits and compares them with
   `outputs/eos-summary.json`;
5. re-checks the condensate exactly with fractions ($\lambda S/m = -382/441$ gives the ratio $-0.764$
   exactly at one instant; on the history the ratio drifts with $w_a = -28077/12500$) and the closed
   formulas of `outputs/effective-formulas.json` with exact dual numbers;
6. recomputes the mixtures of the gas with a condensate and the scans with a drifting condensate in
   three definitions;
7. re-checks Hypothesis00 exactly with fractions: the CPL tangents of the models M2, M3 and M4 on the
   history, the bound $-4/9$ of positive-energy models, the ghost fraction $G \ge 3749/3000$ the Unite $w_0$
   would need, the absence of any crossing of $w = -1$ by M2 to M5, and the ANISOTROPIC source that the
   author's equations require on the history (it grows with $x_4$), from
   `Revision/dark_sector/dirac16complex00/eos-theory.json`;
8. quotes the check counts of the seven committed dark-sector reports (including the independent
   Wolfram verification) exactly as their JSON files give them;
9. draws four teaching figures (the $w_\mathrm{eff}$ histories under A, B and C; the mixtures; the
   dirac16complex00 populations against the Unite CPL line; all candidates in the $(w_0, w_a)$ plane);
10. ends with what it showed and what it did not show.

Every number printed comes either from the solver runs of this notebook or from the notebook's own
computation; where the two overlap with the committed record, an `assert` names the record file and the
check. The notebook stops with an error if any check fails. Every tuned parameter is labelled CHOSEN
(by construction, NOT a prediction); components of negative classical energy are labelled ghost-like.
""")

RUN_TEXT = r"""
## 2. How to run this notebook

These instructions assume a computer on which nothing has been installed yet. Type each command
into a terminal exactly as printed, one line at a time, and press Enter after each line. A
*terminal* is the window in which you type commands: on Windows 11 the app **Windows PowerShell**
(or **Terminal**), on macOS the app **Terminal** (shell zsh), on Linux any terminal (shell bash).

What you need: Git, Python 3.12 or newer (this notebook was built with Python 3.14.5), the Rust
toolchain (`cargo`), about 2 GB of free disk space and an internet connection for the
installation. The Python packages are pinned in `Revision/notebooks/requirements.txt`:
numpy 2.4.6, matplotlib 3.11.0, jupyterlab 4.4.10, nbformat 5.10.4, nbclient 0.10.2,
ipykernel 7.1.0 and nbconvert 7.16.6. The notebook does not need WolframScript, sympy or scipy (its
exact arithmetic uses Python's built-in `fractions` module).

### 2.1 Windows 11 (PowerShell)

1. Install Git from https://git-scm.com/download/win (the default choices are fine).
2. Install Python from https://www.python.org/downloads/ . In the installer's first window tick
   **Add python.exe to PATH**, then click **Install Now**.
3. Install Rust from https://rustup.rs : download and run `rustup-init.exe`. If it says that the
   Visual Studio C++ Build Tools are missing, let it install them (Rust needs their linker), then
   choose the default installation.
4. Close PowerShell, open a new one, and check the three tools (each prints a version number):

```text
git --version
python --version
cargo --version
```

5. Fetch the repository and enter it:

```text
cd $HOME
git clone https://github.com/once-ere/Dirac_claude.git
cd Dirac_claude
```

6. Create a private Python environment OUTSIDE the repository (so that nothing is installed
   system-wide and nothing is written into the repository), and install the pinned packages into it:

```text
python -m venv $HOME\venvs\revision-nb
$PY = "$HOME\venvs\revision-nb\Scripts\python.exe"
& $PY -m pip install --upgrade pip
& $PY -m pip install -r Revision/notebooks/requirements.txt
```

7. Start JupyterLab with this notebook (a browser window opens):

```text
& $PY -m jupyterlab Revision/notebooks/@NAME@.ipynb
```

### 2.2 macOS (Apple silicon, Terminal with zsh)

1. Install Apple's command-line tools (they contain Git and the linker that Rust needs):

```text
xcode-select --install
```

2. Install Python from https://www.python.org/downloads/ (the macOS 64-bit universal2 installer).
3. Install Rust, then load its settings into the open terminal:

```text
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source "$HOME/.cargo/env"
```

4. Check the tools, fetch the repository, create the environment outside it and install the pins:

```text
git --version
python3 --version
cargo --version
cd ~
git clone https://github.com/once-ere/Dirac_claude.git
cd Dirac_claude
python3 -m venv ~/venvs/revision-nb
PY=~/venvs/revision-nb/bin/python
$PY -m pip install --upgrade pip
$PY -m pip install -r Revision/notebooks/requirements.txt
```

5. Start JupyterLab with this notebook:

```text
$PY -m jupyterlab Revision/notebooks/@NAME@.ipynb
```

### 2.3 Linux (Debian or Ubuntu, bash)

1. Install Git, Python with its `venv` module, a C linker and curl (other distributions have
   equivalent packages):

```text
sudo apt update
sudo apt install -y git python3 python3-venv build-essential curl
```

   If `python3 --version` prints a version older than 3.12, install a newer Python first (from your
   distribution or from https://www.python.org/downloads/).
2. Install Rust, then load its settings into the open terminal:

```text
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source "$HOME/.cargo/env"
```

3. Fetch the repository, create the environment outside it and install the pins:

```text
cd ~
git clone https://github.com/once-ere/Dirac_claude.git
cd Dirac_claude
python3 -m venv ~/venvs/revision-nb
PY=~/venvs/revision-nb/bin/python
$PY -m pip install --upgrade pip
$PY -m pip install -r Revision/notebooks/requirements.txt
```

4. Start JupyterLab with this notebook:

```text
$PY -m jupyterlab Revision/notebooks/@NAME@.ipynb
```

### 2.4 Running the cells in JupyterLab

If JupyterLab asks for a kernel, choose **Python 3 (ipykernel)**. Click into the first code cell
and press **Shift+Enter** repeatedly: each press runs one cell and moves to the next. Or use the
menu Run, then Run All Cells. @DURATION@ JupyterLab must be started from a terminal in which
`cargo --version` works, because the notebook calls `cargo`.

### 2.5 Running it without a browser (headless)

From the repository folder, with `$PY` set as above (PowerShell: write `& $PY` instead of `$PY`):

```text
$PY -m nbconvert --to notebook --execute Revision/notebooks/@NAME@.ipynb --output-dir ../revision-nb-runs
```

This executes every cell and writes the executed copy into the folder `revision-nb-runs` next to the
repository (the committed notebook is not changed). To re-execute the notebook and compare it byte
for byte with the committed file:

```text
$PY Revision/notebooks/tools/build_notebooks.py check @NAME@
```

### 2.6 Where the notebook writes

Every result file the notebook writes goes into one output folder: the folder named by the
environment variable `REVISION_NB_OUT` if it is set, otherwise `build/revision_notebooks/@NAME@`
inside the repository (git ignores `build/`). @WHERE@

The Rust solver is compiled into a separate build folder, called `<cargo-target>` here: the folder
named by the environment variable `REVISION_NB_CARGO_TARGET` if it is set, otherwise the folder
`revision-nb-@NAME@-` followed by 12 hexadecimal digits in the temporary folder of your system
(the digits are the start of the sha256 of the path of `<output>`, so every output folder has its own
build folder). The build folder is kept outside the repository and short on purpose: on Windows the
Rust linker (`link.exe`) cannot open a file whose path is longer than 259 characters (the limit
MAX_PATH), and a build folder inside a repository placed in a deep folder exceeds it. The notebook
never deletes this folder; it holds only compiler output and can be deleted by hand after the run.
On macOS and Linux the notebook creates the default build folder readable and writable only by you
(mode 0700) and refuses to continue if a folder of that name already exists and is a symbolic link,
belongs to another user or can be written by group or others: its name is predictable, a shared
temporary folder such as `/tmp` can be written by every user, and the notebook runs the program built
there. On Windows the temporary folder belongs to you alone, and the build folder is used as it is. A
folder named by `REVISION_NB_CARGO_TARGET` is used as given: choose one of your own. A folder
`<output>/cargo-target` left in a reused output folder by an earlier version of this notebook (which
built there) is not listed among the written files at the end.
"""


def run_instructions(duration: str, where: str) -> str:
    return (RUN_TEXT.replace("@NAME@", NAME).replace("@DURATION@", duration)
            .replace("@WHERE@", where))


md(run_instructions(
    "The whole notebook takes well under a minute (about 15 s to 50 s on the computer on which it was "
    "built, depending on its load, including the build of the solver); the 123 solver runs are spread "
    "over up to eight parallel processes and take from a few hundredths of a second to about two seconds each.",
    "The 123 result files of the solver go to "
    "`<output>/ks_runs`, the two reproduced tables to `<output>/ks-history-dense-subset.csv` and "
    "`<output>/eos-history-subset.csv`, the figures to `<output>/figures`. The committed records "
    "`Revision/dark_sector/` and `Revision/kohn_sham/results/` are only read; the notebook refuses to "
    "write there. The notebook has no long mode: it never re-runs the complete dense history (615 states) "
    "or the independent implementations, whose committed reports it reads instead."))

md(r"""
## 3. The words used in this notebook

- **Metric** $g_{\mu\nu}$: the table that turns small coordinate steps into lengths and times. The
  author's metric is diagonal (section 4.1).
- **Coordinates** $x_0,\dots,x_7$: the author's coordinates, in the author's order. $x_0$ the hidden direction, $x_1, x_2, x_3$ ordinary space, $x_4$ the time,
  $x_5, x_6, x_7$ the three extra times (time-like; they **deflate exponentially**).
- **$a_4$, $b_4$**: the two metric functions of the time $x_4$. $a_4(x_4)$ sets the scale of ordinary space;
  $b_4(x_4)$ multiplies the hidden-direction and the extra-time parts of the metric. $b_4$ is a FUNCTION of $x_4$,
  never 1.
- **$\beta$**: $\beta = d\ln b_4/da_4$, how fast $b_4$ changes as $a_4$ grows. On the history of this notebook
  $\beta = 4/3$ (section 4.4).
- **Slice**: one fixed value of $a_4$ (and the value of $b_4$ that belongs to it on the history) at which
  the instantaneous state is computed. Run ids end in `_a000`, `_a005`, ..., `_a200` for
  $a_4 = 0, 0.05, \dots, 2$.
- **History**: the sequence of slices along $a_4 = H x_4$, $b_4 = b_4(0)\,e^{(4/3)Hx_4}$, a PRESCRIBED
  background (section 4.4).
- **Scale factor $a$**: the 3-space observer's scale factor $a = e^{a_4 - a_{4,\mathrm{today}}}$, equal to 1
  "today" ($b_4$ does not enter it). **$a_{4,\mathrm{today}}$** is a free parameter (CHOSEN: 0.5, 1, 1.5 or 2).
- **Kohn-Sham gas**: the dirac16complex particles of the Revision's density-functional model (each
  particle moves in the mean field of all the others), here at zero temperature with N = 8, 592 or 2352
  particles.
- **$\hat\lambda$, $\lambda_\mathrm{eff}$**: $\hat\lambda = \lambda b_4(0)^{-2}$ is the calibrated coupling of
  `Revision/kohn_sham/results/parameters.json`, the same at every slice; the solver's cell volume grows like
  $e^{(5/3)a_4}$, so the effective coupling falls like $e^{-(5/3)a_4}$: the state of slice $a_4$ is that of the
  fixed coordinate cell at $\lambda_\mathrm{eff} = \hat\lambda e^{-(5/3)a_4}$ with the same hidden scale $f$ and
  momentum weight $\kappa$ (section 4.5).
- **Fold band**: the levels $\varepsilon = e^{-a_4}|k|$ of the orbital $(e^{fMy}, 0)$; a gas whose occupied levels
  all lie on it has $P_3 = E/3$ and $P_t = P_0 = 0$ exactly (radiation-like).
- **EMT integrals** $E, P_3, P_t, P_0$: the energy and the pressures of ordinary space, of the extra
  times and of the hidden direction, integrated over the proper 7-volume of a slice.
- **Equation of state** $w$: a pressure divided by an energy density. A dust-like (cold matter) fluid
  has $w = 0$, radiation $w = 1/3$, a cosmological constant $w = -1$; **phantom** means $w < -1$.
- **Effective equation of state** $w_\mathrm{eff} = -1 - \tfrac13\,d\ln\rho_4/d\ln a$: the $w$ a
  4-dimensional observer infers from how the energy density $\rho_4$ dilutes as 3-space expands.
- **Normalisations A, B, C** (dirac16complex) and **N1, N2** (dirac16complex00): ASSUMPTIONS about how
  the observer turns the 8-dimensional energy into $\rho_4$ (section 4.3).
- **Ratio** $w_3 = P_3/E$, $w_t = P_t/E$, $w_{x_0} = P_0/E$: integrated pressure over integrated energy;
  the ratio does not depend on the normalisation.
- **CPL**: the Chevallier-Polarski-Linder form $w(a) = w_0 + w_a(1 - a)$. **Tangent**: $w_0 = w(1)$,
  $w_a = -dw/da$ at $a = 1$. **Fit**: least squares of $w(a)$ over $a \in [a_1, 1]$. **Thawing**: $w_a < 0$;
  **freezing**: $w_a > 0$ (the formula decides).
- **Condensate**: the exact homogeneous solution; its scalar density $S$ falls like $e^{a_4}b_4^{-2}$, on the
  history like $e^{-(5/3)a_4}$.
- **Mixture**: gas plus condensate; the **gas fraction** is the gas's share of the energy today.
- **Krein charge, ghost-like**: dirac16complex00 is a commuting field with a first-order Lagrangian;
  at every real frequency half of its modes carry negative classical energy. A component of negative
  classical energy is called **ghost-like**.
- **M1 ... M5**: the five illustrative populations of dirac16complex00 in `eos-theory.json`.
- **Fraction, dual number**: exact rational arithmetic (Python's `fractions`), and numbers
  $u + u'\varepsilon$ with $\varepsilon^2 = 0$, which carry an exact derivative along.
- **sha256**: a 64-character fingerprint of a file. **Rust, cargo**: the language of the solver and its
  build tool. **JupyterLab, kernel**: the program that shows this notebook, and the Python process that
  runs its cells.
""")

md(r"""
## 4. The physical and mathematical situation

### 4.1 The corrected metric and the deflating extra times

In the author's coordinates $x_0, x_1, \dots, x_7$, with $z = 6 H x_0$ real, the corrected primordial metric of
2026-10-16 (version 2; `Revision/SPEC.md` section 1) is

$$
g = \mathrm{diag}\big(e^{-2a_4}b_4\cot^2 z,\ e^{2a_4},\ e^{2a_4},\ e^{2a_4},\ -1,\
-e^{-2a_4}b_4(\sin^2 z)^{1/6},\ -e^{-2a_4}b_4(\sin^2 z)^{1/6},\ -e^{-2a_4}b_4(\sin^2 z)^{1/6}\big).
$$

$a_4$ and $b_4 > 0$ are functions of $x_4$; $b_4$ is never 1. As $a_4$ increases, ordinary space inflates with the
scale factor $e^{a_4}$ (no warp), the three extra times have the scale factor $e^{-a_4}b_4^{1/2}(\sin^2 z)^{1/12}$
and the hidden direction the scale factor $e^{-a_4}b_4^{1/2}|\cot z|$: both shrink together. The volume element
is $\sqrt{|g|} = e^{-a_4}b_4^2|\cot z|(\sin^2 z)^{1/4}$, so the proper 7-volume of a coordinate cell grows like
$e^{-a_4}b_4^2$.

### 4.2 Conservation along the history

For a diagonal energy-momentum tensor that depends on $x_4$ and $x_0$, the Revision derived from the
metric (`Revision/dark_sector/dirac16complex/outputs/effective-formulas.json`, sympy, 37 checks), with
$h_4 = b_4'/(2b_4) - a_4'$,

$$
\partial_{x_4}\rho = -3a_4'(\rho + p_3) - h_4(\rho + p_0) - 3h_4(\rho + p_t), \qquad \text{integrated:}\qquad
\frac{dE}{da_4} = -3P_3 - \Big(\frac{\beta}{2} - 1\Big)(P_0 + 3P_t) = -3P_3 + P_t + \frac13 P_0 ,
$$

with $E = \int \rho\sqrt{|g|}\,d^7x$ per unit coordinate volume and $\beta = 4/3$ in the last form. The gas loses
energy through the 3-space pressure and gains it through the pressures of the shrinking extra times and the
shrinking hidden direction; the next sections show that these terms are needed.

### 4.3 What the 3-space observer infers: an ASSUMPTION with three options

The extra times are time-like, so how a 4-dimensional observer turns the 8-dimensional energy into an
energy density $\rho_4$ is an ASSUMPTION. dirac16complex (`effective-formulas.json`, key `rho4`):
(A) the extra times and the hidden direction are compact with a fixed coordinate period (closed time-like
directions); (B) $\rho_4$ is taken per unit of their coordinate volume; (C) $\rho_4$ is taken per unit proper
7-volume. In general $\rho_4 \propto E\,e^{-3a_4}(e^{-4a_4}b_4^2)^{-s}$ with $s = 0$ (A, B) or $s = 1$ (C). With
$w_\mathrm{eff} = -1 - \tfrac13\,d\ln\rho_4/d\ln a$ and the conservation law, exactly:

$$
w_\mathrm{eff}(A) = w_\mathrm{eff}(B) = \frac{P_3}{E} + \Big(\frac{\beta}{2} - 1\Big)\frac{P_0 + 3P_t}{3E}, \qquad
w_\mathrm{eff}(C) = w_\mathrm{eff}(A) - \frac{4 - 2\beta}{3} .
$$

On the history ($\beta = 4/3$) $w_\mathrm{eff}(A) = P_3/E - (P_0 + 3P_t)/(9E)$ and the two readings differ by
exactly $(4 - 2\beta)/3 = 4/9$. dirac16complex00 uses the same two readings under the names N1 (= B) and N2
(= C): $w_\mathrm{eff}(N2) = w_\mathrm{eff}(N1) - 4/9$.

### 4.4 The history: a PRESCRIBED background

The numerical history of the Revision is

$$
a_4 = H x_4, \qquad b_4(x_4) = b_4(0)\,e^{(4/3) H x_4}, \qquad \beta = \frac43 ,
$$

kept from `Revision/SPEC.md` section 1; the extra-time scale factor is $e^{-a_4}b_4^{1/2} \propto e^{-a_4/3}$: the
extra times still deflate exponentially. In the corrected metric the field equations admit no off-diagonal
source and require equal hidden and extra-time pressures; with the author's Lovelock weights
($w_1 = 1$, $w_2 = 1/32$, $w_3 = 1/1152$, $\Lambda = -10$) this history needs an ANISOTROPIC source that grows with
$x_4$, with $k = e^{(2/3)Hx_4}$ ($H = 1$):

$$
\kappa(p_3 - p_0) = -\tfrac{9}{16}k^2 + \tfrac{1069}{432}k + \tfrac{2015}{972} ,\qquad
\kappa p_0 - \Lambda = \kappa p_t - \Lambda = \tfrac{79}{16}k - \tfrac{497}{144}
$$

(`eos-theory.json`, condensate `historyRequiredSource`; independently in Wolfram,
`Revision/dark_sector/reports/wolfram-dark-sector.json`, D6). Neither the Kohn-Sham gas nor the condensate is this
source: the history is a PRESCRIBED background.

### 4.5 The Kohn-Sham states in the corrected metric

In the corrected metric the good-sector state is $\Psi = e^{ik\cdot x}e^{-(3/2)Hy}e^{a_4/2}b_4^{-1}\chi$, and $\chi$
solves the slice Hamiltonian $h_j = j[-(i/f)\sigma_1\,d/dy + M_\mathrm{eff}\sigma_2 + \kappa k\sigma_3] + v_v$ with the
hidden scale $f = e^{-a_4}b_4^{1/2}$ ($= e^{-a_4/3}$ on the history) and the constant momentum weight
$\kappa = e^{-a_4}$ (`Revision/kohn_sham/ks-theory.json`). The cell volume enters through the densities: the
Kohn-Sham record (`Revision/kohn_sham`) works with $\hat\lambda = \lambda b_4(0)^{-2}$ and
$\mathrm{Vol}_7(a_4) = \ell^3 v_t e^{(2\beta - 1)a_4} = \ell^3 v_t e^{(5/3)a_4}$, so $b_4(0)$ never needs a value. A
state depends on the coupling and the cell volume only through their ratio (`ks-theory.json`,
`densities.couplingVolumeScaling`), so the same state is that of the fixed coordinate cell at

$$
\lambda_\mathrm{eff}(a_4) = \hat\lambda\,e^{-(5/3)a_4}
$$

with the same $f$ and $\kappa$. The run report checks this equivalence on 48 states (`lambda_eff_form_agrees`).
Without interaction the occupied orbitals are the fold-band orbitals $(e^{fMy}, 0)$ with $\varepsilon = e^{-a_4}|k|$
(and the $k = 0$ zero modes): the free gas is an exact fold-band gas.

### 4.6 What is assumed, what is chosen, what is open

- The history is a PRESCRIBED background: the Kohn-Sham gas is a test field without back-reaction; the
  recorded states are not admissible sources of the $a_4$ and $b_4$ equations
  (`Revision/field_equations_a4/reports/ks-source-conditions.json`). On this linear history the
  observer's expansion itself reads $w_\mathrm{exp} = -1$ exactly ($b_4$ does not enter $a$).
- Both fold conditions at the fold $z = \pi/2$, where the two halves of a cell meet, are filled (ASSUMED);
  the filling of the positive branch is the CONVENTION of `Revision/kohn_sham/ks-theory.json`; only $T = 0$
  states and $a_4 \in [0, 2]$ (the solver's validated range) are used.
- CHOSEN (by construction, NOT a prediction): $a_{4,\mathrm{today}}$; the gas fractions of the
  mixtures; the condensate value $\lambda S/m = -382/441$ (chosen so that the ratio equals $-0.764$ at one
  instant); every parameter of the dirac16complex00 models M2 to M5 (CHOSEN on the withdrawn $b_4 = 1$
  record, where M4 and M5 were solved to reproduce the Unite tangent or fit; they are kept unchanged so
  that the effect of the corrected metric is seen directly). The M5 component of negative classical energy is
  ghost-like.
- The comparison with the Unite numbers is an INTERPRETATION: it treats them as constraints on the
  dilution of a 4-dimensional effective density. There is no supernova likelihood here.
""")

# ------------------------------------------------------------------------------------------------
md(r"""
## 5. The driver: find the repository and build the Rust solver

### 5.1 Locate the repository and the output folder

The next cell imports the Python modules, finds the repository (the folder that contains
`Revision/SPEC.md`, searched upwards from the folder in which the notebook runs), fixes the output
folder and the Rust build folder `<cargo-target>` (section 2.6) and refuses to continue if either
would put files into a committed record. It prints no path of your computer, only names relative to
the repository, to `<output>` or to `<cargo-target>`.
""")

code(r'''
import concurrent.futures
import csv
import hashlib
import json
import math
import os
import shutil
import stat
import subprocess
import sys
import tempfile
from fractions import Fraction
from pathlib import Path

import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from IPython.display import Image, Markdown, display


def find_repository(start):
    for folder in (start, *start.parents):
        if (folder / "Revision" / "SPEC.md").is_file() and \
                (folder / "Revision" / "kohn_sham" / "solver" / "Cargo.toml").is_file():
            return folder
    raise RuntimeError("Open this notebook from inside the repository Dirac_claude "
                       "(for example from Dirac_claude/Revision/notebooks); see section 2.")


REPO = find_repository(Path.cwd().resolve())
KS = REPO / "Revision" / "kohn_sham"
CRATE = KS / "solver"
DS = REPO / "Revision" / "dark_sector" / "dirac16complex"
D00 = REPO / "Revision" / "dark_sector" / "dirac16complex00"
if os.environ.get("REVISION_NB_OUT"):
    OUT = Path(os.environ["REVISION_NB_OUT"]).resolve()
    OUT_LABEL = "the folder named by the environment variable REVISION_NB_OUT"
else:
    OUT = REPO / "build" / "revision_notebooks" / "dark_sector_hypotheses"
    OUT_LABEL = "build/revision_notebooks/dark_sector_hypotheses in the repository (ignored by git)"
RUN_DIR = OUT / "ks_runs"
FIG_DIR = OUT / "figures"
for protected in (REPO / "Revision" / "dark_sector", KS / "results", KS / "reports"):
    for folder in (OUT, RUN_DIR, FIG_DIR):
        if folder == protected or protected in folder.parents:
            raise RuntimeError("the output folder lies inside the committed record " +
                               protected.relative_to(REPO).as_posix() + ": choose another REVISION_NB_OUT")
# The Rust build folder <cargo-target> (section 2.6): by default short and outside the repository, because on
# Windows the linker cannot open paths longer than 259 characters (MAX_PATH).
if os.environ.get("REVISION_NB_CARGO_TARGET"):
    TARGET = Path(os.environ["REVISION_NB_CARGO_TARGET"]).resolve()
else:
    TARGET = Path(tempfile.gettempdir()).resolve() / (
        "revision-nb-dark_sector_hypotheses-" + hashlib.sha256(str(OUT).encode("utf-8")).hexdigest()[:12])
for protected in (REPO / "Revision" / "dark_sector", KS / "results", KS / "reports"):
    if TARGET == protected or protected in TARGET.parents:
        raise RuntimeError("the Rust build folder lies inside the committed record " +
                           protected.relative_to(REPO).as_posix() + ": choose another REVISION_NB_CARGO_TARGET")
if os.name == "posix" and not os.environ.get("REVISION_NB_CARGO_TARGET"):
    # The default name is predictable, a shared temporary folder such as /tmp can be written by every user, and
    # the notebook runs the program built there: create the folder private (mode 0o700) and refuse one that is not.
    os.makedirs(TARGET, mode=0o700, exist_ok=True)
    info = os.lstat(TARGET)
    if not stat.S_ISDIR(info.st_mode) or info.st_uid != os.getuid() or info.st_mode & 0o022:
        raise RuntimeError(f"the Rust build folder {TARGET} is not a private folder of the current user (a symbolic "
                           "link, owned by another user, or writable by group or others): delete it, or set "
                           "REVISION_NB_CARGO_TARGET to a folder of your own")
for folder in (OUT, RUN_DIR, FIG_DIR):
    folder.mkdir(parents=True, exist_ok=True)

CHECKS = []


def check(name, ok, detail):
    """Record one check of this notebook; stop the notebook if it fails."""
    CHECKS.append(name)
    print(("PASS" if ok else "FAIL"), "-", name + ":", detail)
    assert ok, f"check {name} failed: {detail}"


def shown(path):
    """A path as the notebook prints it: relative to <cargo-target>, to <output> or to the repository."""
    path = Path(path).resolve()
    for base, label in ((TARGET, "<cargo-target>"), (OUT, "<output>"), (REPO, "")):
        if path == base or base in path.parents:
            rel = path.relative_to(base).as_posix()
            return (label + "/" + rel if label else rel) if rel != "." else (label or ".")
    return path.name


def sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def load_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def write_lf(path, text):
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)


UNITE = {"w_const": -0.764, "w0": -0.861, "wa": -0.60}     # Revision/README.md
print("repository: found (the folder that contains Revision/SPEC.md)")
print("<output> =", OUT_LABEL)
print("<cargo-target> = the Rust build folder (section 2.6; by default a short folder in the system's temporary folder)")
print("Python", sys.version.split()[0], "| numpy", np.__version__, "| matplotlib", matplotlib.__version__)
print("Unite values (Revision/README.md): constant w =", UNITE["w_const"], "| CPL (w0, wa) =", (UNITE["w0"], UNITE["wa"]))
''')

md(r"""
### 5.2 Build the Rust solver and define one solver run

The next cell runs `cargo build --release` on the crate `Revision/kohn_sham/solver` (pure Rust, no
external crates) with the build folder `<cargo-target>` (section 2.6), so that nothing is written into
the crate's own `target` folder. The first build takes about half a minute. If `cargo` is not found,
install Rust (section 2) and restart JupyterLab from a new terminal.

The cell also defines `lambda_eff` ($\hat\lambda e^{-(2\beta - 1)a_4} = \hat\lambda e^{-(5/3)a_4}$, section 4.5; a column
of the record) and `run_one`, which runs the solver's command `single` for one state with EXACTLY the arguments of
`Revision/dark_sector/dirac16complex/compute/run_ks_history.py`
(`single --m 1 --lambda LAMBDA_HAT --a4 A --N N --out FILE`, no profiles; the solver takes $\beta$ from
`ks-theory.json` and uses the cell volume $\ell^3 v_t e^{(5/3)a_4}$ and the hidden scale $f = e^{-a_4/3}$), with the
repository as the
working folder (that is where the solver finds `Revision/kohn_sham/ks-theory.json` and
`Revision/algebra/gammas.json`). It requires exit status 0, the final line `SUCCESS` and only `PASS`
lines on the solver's error stream (its input checks).
""")

code(r'''
CARGO = shutil.which("cargo")
if CARGO is None:
    raise RuntimeError("cargo was not found: install Rust (section 2), then start JupyterLab again "
                       "from a terminal in which `cargo --version` works")
build = subprocess.run(
    [CARGO, "build", "--release", "--manifest-path", str(CRATE / "Cargo.toml"), "--target-dir", str(TARGET)],
    capture_output=True, text=True, encoding="utf-8", errors="replace")
if build.returncode != 0:
    print(build.stdout)
    print(build.stderr)
    raise RuntimeError("cargo build failed; the messages above say why")
EXE = TARGET / "release" / ("revision_ks_solver.exe" if os.name == "nt" else "revision_ks_solver")
warnings = [line for line in build.stderr.splitlines() if line.startswith("warning")]
print("$ cargo build --release --manifest-path Revision/kohn_sham/solver/Cargo.toml --target-dir <cargo-target>")
print("exit status:", build.returncode)
print("compiler warnings:", len(warnings))
print("program:", shown(EXE.parent) + "/revision_ks_solver", "(the file name ends in .exe on Windows)")
check("solver_built", EXE.is_file() and not warnings, "the release solver exists and the build printed no warning")

PARAMETERS = load_json(KS / "results" / "parameters.json")
LAMBDA1 = {int(v["N"]): v["lambda1"] for v in PARAMETERS["couplingCalibration"]["values"]}
SLICES = [round(0.05 * i, 10) for i in range(41)]          # as run_ks_history.py
SERIES = [(2352, "lam0", 0.0), (592, "lam0", 0.0), (8, "lamp1", LAMBDA1[8])]
BETA = 4.0 / 3.0                                           # d ln b4/d a4 on the history (section 4.4)


def lambda_eff(lam_hat, a4):
    """the coupling of the coordinate-cell form at slice a4: lambda_hat e^{-(2 beta - 1) a4} = lambda_hat e^{-(5/3) a4}"""
    return lam_hat * math.exp(-(2.0 * BETA - 1.0) * a4)


def rid_of(n, tag, a4):
    return f"N{n}_{tag}_a{int(round(a4 * 100)):03d}"


def run_one(n, tag, lam, a4):
    """One state with `revision_ks_solver single`, arguments exactly as run_ks_history.py."""
    rid = rid_of(n, tag, a4)
    out = RUN_DIR / f"{rid}.json"
    args = ["single", "--m", "1", "--lambda", repr(lam), "--a4", repr(a4), "--N", str(n),
            "--out", str(out)]
    proc = subprocess.run([str(EXE), *args], capture_output=True, text=True, encoding="utf-8",
                          errors="replace", cwd=str(REPO))
    lines = proc.stderr.splitlines()
    final = proc.stdout.strip().splitlines()[-1] if proc.stdout.strip() else ""
    others = [line for line in lines if not line.startswith("PASS")]
    ok = proc.returncode == 0 and final == "SUCCESS" and not others and out.is_file()
    return rid, args, lines, final, proc.returncode, ok
''')

# ------------------------------------------------------------------------------------------------
md(r"""
## 6. The solver recites its configuration

Before trusting any result, the solver checks its inputs and says what it reads: the forms of the
corrected metric that it implements and the coefficients of the Kohn-Sham functional from
`Revision/kohn_sham/ks-theory.json` ($\tfrac{15}{16} = 0.9375$ and $-\tfrac{1}{16} = -0.0625$), the author's gamma
matrices from `Revision/algebra/gammas.json`, and the exact reduction of the 16-component Hamiltonian to
$2 \times 2$ blocks. The next cell solves the first state of the dense history (N = 8, $\hat\lambda = +\lambda_1$,
$a_4 = 0$, where the cell volume is $\ell^3 v_t$), prints the command, the four input checks and the parameter
block of the result file, and checks the parameters against the committed
`Revision/kohn_sham/results/parameters.json` and the description of the committed run report
`Revision/dark_sector/dirac16complex/reports/ks-history-run.json` (its history, its $\beta$ and its coupling rule).
""")

code(r'''
RESULTS = {}
rid, args, lines, final, status, ok = run_one(8, "lamp1", LAMBDA1[8], 0.0)
print("$ revision_ks_solver", " ".join(shown(a) if (os.sep in a or "/" in a) else a for a in args))
print("the solver's own checks of its inputs (it prints them on its error stream):")
for line in lines:
    print("   ", line)
print(f"    -> {final}, exit status {status}")
assert ok, "the first solver run failed"
RESULTS[rid] = load_json(RUN_DIR / f"{rid}.json")
first = RESULTS[rid]
print()
print("producer:", first["producer"], "| numerics:", first["numerics"])
for key, value in first["parameters"].items():
    print(f"  {key:16s} {value}")
phys = PARAMETERS["physics"]
same = (first["parameters"]["H"], first["parameters"]["m"], first["parameters"]["L"], first["parameters"]["dk"],
        first["parameters"]["v_t"], first["parameters"]["tipTheta"], first["parameters"]["T"]) == \
       (phys["H"], phys["m"], phys["L_tipCutoff"], phys["dk"], phys["v_t"], phys["tipTheta"], 0.0)
RUN_REPORT = load_json(DS / "reports" / "ks-history-run.json")
check("parameters_equal_record", same and first["numerics"] == PARAMETERS["numerics"]["tag"]
      and RUN_REPORT["slices"] == SLICES and len(lines) == 4,
      f"H = {phys['H']}, m = {phys['m']}, L = {phys['L_tipCutoff']}, dk = {phys['dk']}, v_t = {phys['v_t']}, "
      f"tip theta = {phys['tipTheta']}, T = 0, numerics {PARAMETERS['numerics']['tag']} as in "
      "Revision/kohn_sham/results/parameters.json; the 41 slices equal those of reports/ks-history-run.json")
check("history_equals_record", RUN_REPORT["beta"] == "d ln b4/d a4 = 4/3"
      and "corrected primordial metric of 2026-10-16" in RUN_REPORT["metric"]
      and "b4(x4) = e^((4/3) H x4)" in RUN_REPORT["history"] and "PRESCRIBED BACKGROUND" in RUN_REPORT["history"]
      and "lambda_eff = lambda_hat e^(-(5/3) a4)" in RUN_REPORT["coupling"]
      and "Vol_7(a4) = ell^3 v_t e^((5/3) a4)" in RUN_REPORT["coupling"]
      and abs(first["parameters"]["beta"] - BETA) <= 1e-15 and first["parameters"]["Vol7"] == PARAMETERS["physics"]["Vol7AtA4Zero"]
      and first["parameters"]["f"] == 1.0
      and all(abs(lambda_eff(1.0, a4) - math.exp(-5.0 * a4 / 3.0)) <= 1e-15 for a4 in SLICES),
      "the committed run report states the corrected metric, the PRESCRIBED history a4 = H x4, b4(x4) = e^((4/3) H x4), "
      "beta = 4/3, the coupling lambda_hat with the cell volume Vol_7(a4) = ell^3 v_t e^((5/3) a4) and the equivalent "
      "lambda_eff = lambda_hat e^(-(5/3) a4); the solver ran with beta = 4/3 and, at a4 = 0, the hidden scale f = 1 and the "
      "cell volume Vol7AtA4Zero of results/parameters.json; this notebook's lambda_eff equals lambda_hat e^(-(5/3) a4) at "
      "all 41 slices (to 1e-15; checks cell_volume_follows_b4 and lambda_eff_form_agrees of the run report)")
print("lambda_hat = lambda_1 per N (results/parameters.json):", LAMBDA1)
print("committed run report, solver:", RUN_REPORT["solver"])
print("committed run report, history:", RUN_REPORT["history"])
print("committed run report, coupling:", RUN_REPORT["coupling"])
''')

# ------------------------------------------------------------------------------------------------
md(r"""
## 7. The Kohn-Sham gas on the dense history

### 7.1 The 123 runs

The committed record solved 15 series (N = 8, 592, 2352, each with $\lambda = 0, \pm\lambda_1, \pm\lambda_2$)
at the 41 slices $a_4 = 0, 0.05, \dots, 2$, 615 states. This notebook solves three of the series:
N = 2352 with $\lambda = 0$ (the largest gas), N = 592 with $\lambda = 0$, and N = 8 with $\lambda = +\lambda_1$
(only the $k = 0$ fold zero modes, interacting). The next cell runs the remaining 122 states, spread
over up to eight parallel solver processes (each run is independent; the order of the results does not
depend on which finishes first), and requires every run to succeed.
""")

code(r'''
TASKS = [(n, tag, lam, a4) for (n, tag, lam) in SERIES for a4 in SLICES]
todo = [t for t in TASKS if rid_of(t[0], t[1], t[3]) not in RESULTS]
workers = max(1, min(8, os.cpu_count() or 1))
with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as pool:
    outcomes = list(pool.map(lambda t: run_one(*t), todo))
bad = [o[0] for o in outcomes if not o[5]]
for rid, args, lines, final, status, ok in outcomes:
    if ok:
        RESULTS[rid] = load_json(RUN_DIR / f"{rid}.json")
check("all_runs_succeeded", not bad and len(RESULTS) == len(TASKS) == 123,
      f"{len(RESULTS)} runs (3 series x 41 slices): exit status 0, final line SUCCESS, only the 4 PASS input "
      f"checks on the error stream; failed: {bad}")
''')

md(r"""
### 7.2 Comparison with the committed dense history, bit for bit

`run_ks_history.py` wrote one row per state into `outputs/ks-history-dense.csv`: the id, N, the
coupling $\hat\lambda$, $a_4$, $b_4/b_4(0) = e^{(4/3)a_4}$, $\lambda_\mathrm{eff}$, the solver's $\beta$ and cell volume
$\mathrm{Vol}_7(a_4)$, $E_\mathrm{KS}$, the EMT integrals
$E = \int\rho$, $P_3$, $P_t$, $P_0$, the particle integral, the number of SCF iterations, the residual, the
Fermi level, the solver's two residuals of the hidden-direction conservation law, and a 16-character
fingerprint of the occupied level set (floats written as Python's shortest round-trip `repr`). The next
cell rebuilds each row from the new result file in exactly that way and requires the new TEXT to equal
the committed row character for character (equal text of a shortest round-trip float means the same
64-bit number). It also repeats three checks of the committed run report for these series: the occupied
set is the same at all 41 slices (so the instantaneous ground states are the adiabatically continued
state with fixed occupations, to which $dE/da_4 = -3P_3 + P_t + \frac13P_0$ applies), the hidden-direction
conservation residuals ($p_{0,y} + 3H(p_0 - p_t) = 0$), and the particle number.
""")

code(r'''
def occupied_signature(levels):
    occ = sorted((int(l[0]), int(l[1]), str(l[2]), int(l[3]), repr(float(l[6]))) for l in levels if float(l[6]) > 0)
    return hashlib.sha256(json.dumps(occ).encode()).hexdigest()[:16], len(occ)


DENSE_LINES = (DS / "outputs" / "ks-history-dense.csv").read_text(encoding="utf-8").splitlines()
HEADER = DENSE_LINES[0].split(",")
RECORD_ROW = {line.split(",")[0]: line for line in DENSE_LINES[1:]}
ROWS = {}
new_lines, identical = [DENSE_LINES[0]], 0
for n, tag, lam, a4 in TASKS:
    rid = rid_of(n, tag, a4)
    d = RESULTS[rid]
    emt = d["emtIntegrals_2Vol7_int_e3Hy"]
    sig, nocc = occupied_signature(d["levels_n2_j_parity_label_eps_deg_f"])
    row = {"id": rid, "N": n, "lambda_tag": tag, "lambda": lam, "a4": a4,
           "b4_over_b4_0": math.exp(BETA * a4), "lambda_eff": lambda_eff(lam, a4),
           "beta": d["parameters"]["beta"], "Vol7": d["parameters"]["Vol7"], "E_KS": d["E_KS"],
           "int_rho": emt["rho"], "int_p3": emt["p3"], "int_p_t": emt["p_t"], "int_p0": emt["p0"],
           "int_n": emt["n"], "iterations": d["iterations"], "residual": d["residual"],
           "fermi_level": d["mu_or_fermi_level"], "ycons_integrated_rel": d["yConservationIntegratedRel"],
           "ycons_pointwise_rel": d["yConservationPointwiseRel"], "occupied_signature": sig,
           "occupied_labels": nocc}
    assert list(row) == HEADER, "the columns of outputs/ks-history-dense.csv changed"
    ROWS[rid] = row
    line = ",".join(repr(row[c]) if isinstance(row[c], float) else str(row[c]) for c in HEADER)
    new_lines.append(line)
    identical += line == RECORD_ROW[rid]
write_lf(OUT / "ks-history-dense-subset.csv", "\n".join(new_lines) + "\n")
check("dense_rows_bit_identical", identical == 123,
      f"{identical} of 123 rows rebuilt from the new solver results equal the rows of "
      "Revision/dark_sector/dirac16complex/outputs/ks-history-dense.csv character for character "
      "(including b4/b4(0) = e^((4/3) a4), lambda_eff = lambda_hat e^(-(5/3) a4) and the solver's beta and Vol_7(a4))")
for n, tag, lam in SERIES:
    sigs = {ROWS[rid_of(n, tag, a4)]["occupied_signature"] for a4 in SLICES}
    nocc = {ROWS[rid_of(n, tag, a4)]["occupied_labels"] for a4 in SLICES}
    check(f"N{n}_{tag}_occupations_fixed", len(sigs) == 1 and len(nocc) == 1,
          f"the occupied set (fingerprint {sigs.pop()}, {nocc.pop()} occupied levels) is the same at all 41 slices "
          "(check occupied_labels_fixed_along_history of reports/ks-history-run.json)")
yc = max(max(r["ycons_integrated_rel"], r["ycons_pointwise_rel"]) for r in ROWS.values())
nmax = max(abs(r["int_n"] - r["N"]) / r["N"] for r in ROWS.values())
check("y_conservation_and_particle_number", yc <= 1e-6 and nmax <= 1e-12,
      f"p0_y + 3 H (p0 - p_t) = 0: largest relative residual of the solver {yc:.3e} (<= 1e-6); "
      f"max |int n - N|/N = {nmax:.3e} (<= 1e-12), as the checks of reports/ks-history-run.json require")
print("the reproduced rows are written to", shown(OUT / "ks-history-dense-subset.csv"),
      "| sha256", sha256(OUT / "ks-history-dense-subset.csv"))
''')

md(r"""
### 7.3 A look at the numbers

The next cell lists, for the three series at the slices $a_4 = 0, 0.5, 1, 1.5, 2$, the ratio $b_4/b_4(0)$,
the effective coupling $\lambda_\mathrm{eff} = \hat\lambda e^{-(5/3)a_4}$, the integrated energy $E$ and the
integrated pressures. The gas N = 2352 and N = 592 ($\lambda = 0$) occupies only fold-band levels
$\varepsilon = e^{-a_4}|k|$ (and the $k = 0$ zero modes): its energy falls exactly like $e^{-a_4}$ (its 3-momenta
redshift), $P_3 = E/3$, $P_t = P_0 = 0$. For N = 8 with $\hat\lambda = +\lambda_1$ only the $k = 0$ fold zero modes are
filled (their levels are $\varepsilon = 0$): $E$ is pure interaction energy, small and negative (the record:
$E < 0$ for $\lambda > 0$), $P_3 = P_t$, and $E$ falls as the effective coupling does, more slowly than
$e^{-(5/3)a_4}$ because the shrinking hidden direction concentrates the zero modes.
""")

code(r'''
rows = ["| series | $a_4$ | $b_4/b_4(0)$ | $\\lambda_\\mathrm{eff}$ | $E$ | $P_3$ | $P_t$ | $P_0$ |",
        "|---|---|---|---|---|---|---|---|"]
for n, tag, lam in SERIES:
    for a4 in (0.0, 0.5, 1.0, 1.5, 2.0):
        r = ROWS[rid_of(n, tag, a4)]
        rows.append(f"| N{n}_{tag} | {a4:.2f} | {r['b4_over_b4_0']:.6f} | {r['lambda_eff']:.6e} | {r['int_rho']:.9e} | "
                    f"{r['int_p3']:.9e} | {r['int_p_t']:.9e} | {r['int_p0']:.9e} |")
display(Markdown("\n".join(rows)))
''')

# ------------------------------------------------------------------------------------------------
md(r"""
## 8. The equation of state along the history

### 8.1 Recompute it as compute_eos.py does

For each series the next cell forms, at every slice, the effective equations of state of section 4.3 with
$\beta = 4/3$,

$$
w_\mathrm{eff}(A) = w_\mathrm{eff}(B) = \frac{P_3}{E} + \Big(\frac{\beta}{2} - 1\Big)\frac{P_0 + 3P_t}{3E}, \qquad
w_\mathrm{eff}(C) = w_\mathrm{eff}(A) - \frac{4 - 2\beta}{3},
$$

the ratios $w_3 = P_3/E$, $w_t = P_t/E$, $w_{x_0} = P_0/E$, and the derivatives $dw_\mathrm{eff}/da_4$ and
$dw_3/da_4$ with the fourth-order finite-difference stencil of `compute_eos.py` (central inside,
one-sided at the two ends; step 0.05). The functions `deriv`, `interp` (cubic Lagrange interpolation on
the grid) and `cpl_fit` (continuous least squares of $w(a)$ by $w_0 + w_a(1 - a)$, 32-point
Gauss-Legendre quadrature) are copied from that script, so that the same operations give the same
floating-point numbers. Each row is written with 15 significant digits after the point, as in
`outputs/eos-history.csv`, and compared character for character. The cell also checks the conservation
law of section 4.2, $dE/da_4 = -3P_3 + P_t + \frac13P_0$, in two ways (finite differences, and Simpson's rule for
$E(a_4) - E(0) = -\int_0^{a_4}(3P_3 - P_t - \frac13P_0)$), shows that the law $dE/da_4 = -3P_3$ of the inflating
3-space alone (without the terms of the shrinking extra times and hidden direction) FAILS for the interacting
series, and checks the identity
$\frac{d}{da_4}w_\mathrm{eff}(A) = \big(P_3' - \frac19(P_0' + 3P_t')\big)/E + w_\mathrm{eff}(A)\,(3P_3 - P_t - \frac13P_0)/E$,
which follows from $E' = -3P_3 + P_t + \frac13P_0$.
""")

code(r'''
H_STEP = 0.05


def deriv(f, h):
    """4th-order finite-difference derivative on a uniform grid (central inside, one-sided at the ends)"""
    n = len(f)
    d = np.empty(n)
    for i in range(n):
        if 2 <= i <= n - 3:
            d[i] = (f[i - 2] - 8 * f[i - 1] + 8 * f[i + 1] - f[i + 2]) / (12 * h)
        elif i < 2:
            s = f[i:i + 5]
            d[i] = ((-25 * s[0] + 48 * s[1] - 36 * s[2] + 16 * s[3] - 3 * s[4]) / (12 * h) if i == 0 else
                    (-3 * f[0] - 10 * f[1] + 18 * f[2] - 6 * f[3] + f[4]) / (12 * h))
        else:
            if i == n - 1:
                s = f[n - 5:]
                d[i] = (25 * s[4] - 48 * s[3] + 36 * s[2] - 16 * s[1] + 3 * s[0]) / (12 * h)
            else:
                d[i] = (3 * f[n - 1] + 10 * f[n - 2] - 18 * f[n - 3] + 6 * f[n - 4] - f[n - 5]) / (12 * h)
    return d


def interp(xg, fg, xq):
    """4-point Lagrange (cubic) interpolation on the uniform grid"""
    h = xg[1] - xg[0]
    out = []
    for x in np.atleast_1d(xq):
        i = int(math.floor((x - xg[0]) / h))
        i0 = min(max(i - 1, 0), len(xg) - 4)
        xs, fs = xg[i0:i0 + 4], fg[i0:i0 + 4]
        v = 0.0
        for j in range(4):
            lj = 1.0
            for m in range(4):
                if m != j:
                    lj *= (x - xs[m]) / (xs[j] - xs[m])
            v += fs[j] * lj
        out.append(v)
    return np.array(out)


GL_X, GL_W = np.polynomial.legendre.leggauss(32)


def cpl_fit(wfun, a1):
    """least squares of w(a) by w0 + wa (1 - a) on [a1, 1] (continuous L2 in a) and the constant-w fit"""
    a = 0.5 * (1 - a1) * GL_X + 0.5 * (1 + a1)
    wq = 0.5 * (1 - a1) * GL_W
    w = wfun(a)
    Lr = 1 - a1
    J0 = float(np.sum(wq * w))
    J1 = float(np.sum(wq * w * (1 - a)))
    Amat = np.array([[Lr, Lr ** 2 / 2], [Lr ** 2 / 2, Lr ** 3 / 3]])
    w0, wa = np.linalg.solve(Amat, np.array([J0, J1]))
    return float(w0), float(wa), J0 / Lr


EOS = {}
HIST_RECORD = {}
for line in (DS / "outputs" / "eos-history.csv").read_text(encoding="utf-8").splitlines()[1:]:
    p = line.split(",")
    HIST_RECORD[(p[0], p[3])] = line
hist_new = ["series,N,lambda_hat,a4,E,P3,Pt,P0,w_eff_A_B,w_eff_C,w3,wt,wx0,dw_eff_da4,dw3_da4"]
SHIFT_C = -(4.0 - 2.0 * BETA) / 3.0                       # w_eff(C) - w_eff(A) = -4/9 (compute_eos.py)
same_rows, worst_cons, worst_int, worst_dw, worst_3d = 0, 0.0, 0.0, 0.0, 0.0
for n, tag, lam in SERIES:
    sid = f"N{n}_{tag}"
    g = lambda c: np.array([ROWS[rid_of(n, tag, a4)][c] for a4 in SLICES])
    a4, E, P3, Pt, P0 = g("a4"), g("int_rho"), g("int_p3"), g("int_p_t"), g("int_p0")
    dE = deriv(E, H_STEP)
    scale = np.max(np.abs(E))
    src = 3 * P3 + (0.5 * BETA - 1.0) * (P0 + 3 * Pt)          # dE/da4 = -src
    dev = np.max(np.abs(dE + src)[2:-2]) / scale
    if lam != 0.0:
        worst_3d = max(worst_3d, float(np.max(np.abs(dE + 3 * P3)[2:-2]) / scale))
    integ, devint = 0.0, 0.0
    for i in range(0, 40, 2):
        integ += H_STEP / 3 * (src[i] + 4 * src[i + 1] + src[i + 2])
        devint = max(devint, abs(E[i + 2] - E[0] + integ) / scale)
    wA = P3 / E + (0.5 * BETA - 1.0) * (P0 + 3.0 * Pt) / (3.0 * E)
    wC = wA + SHIFT_C
    w3, wt, wx0 = P3 / E, Pt / E, P0 / E
    dwA = deriv(wA, H_STEP)
    dnum = deriv(P3, H_STEP) + (0.5 * BETA - 1.0) * (deriv(P0, H_STEP) + 3 * deriv(Pt, H_STEP)) / 3.0
    dwA_id = dnum / E + wA * src / E
    dw3 = deriv(w3, H_STEP)
    worst_cons, worst_int = max(worst_cons, dev), max(worst_int, devint)
    worst_dw = max(worst_dw, float(np.max(np.abs(dwA - dwA_id)[2:-2])))
    for i in range(41):
        vals = [lam, a4[i], E[i], P3[i], Pt[i], P0[i], wA[i], wC[i], w3[i], wt[i], wx0[i], dwA[i], dw3[i]]
        line = ",".join([sid, str(n)] + [f"{float(v):.15e}" for v in vals])
        hist_new.append(line)
        same_rows += HIST_RECORD.get((sid, f"{a4[i]:.15e}")) == line
    EOS[sid] = {"a4": a4, "E": E, "P3": P3, "Pt": Pt, "P0": P0, "wA": wA, "wC": wC, "w3": w3,
                "wt": wt, "wx0": wx0, "dwA": dwA, "dw3": dw3, "dE": dE, "dev": dev, "devint": devint, "lambda": lam}
write_lf(OUT / "eos-history-subset.csv", "\n".join(hist_new) + "\n")
check("eos_rows_identical", same_rows == 123,
      f"{same_rows} of 123 rows (E, P3, Pt, P0, w_eff(A, B), w_eff(C), w3, wt, wx0 and the two derivatives) equal "
      "the rows of Revision/dark_sector/dirac16complex/outputs/eos-history.csv character for character")
check("conservation_with_deflation_terms", worst_cons <= 1e-5 and worst_int <= 1e-5,
      f"max |dE/da4 + 3 P3 - Pt - P0/3|/max|E| = {worst_cons:.3e} (interior slices; <= 1e-5) and Simpson "
      f"{worst_int:.3e} (<= 1e-5), as checks conservation_identity and conservation_integrated_simpson of "
      "reports/eos-checks.json")
check("conservation_of_3_space_alone_fails", worst_3d >= 1e-3,
      f"the law dE/da4 = -3 P3 of the inflating 3-space alone misses the interacting series N = 8 by {worst_3d:.3e} of "
      "max|E|: the terms Pt + P0/3 of the shrinking extra times and hidden direction are needed")
check("derivative_two_ways", worst_dw <= 1e-5,
      f"d w_eff(A)/da4 by finite differences vs the identity (P3' - (P0' + 3 Pt')/9)/E + w_eff(A) (3 P3 - Pt - P0/3)/E "
      f"at the interior slices: max deviation {worst_dw:.3e} (<= 1e-5; check derivative_two_ways)")
print("the reproduced rows are written to", shown(OUT / "eos-history-subset.csv"),
      "| sha256", sha256(OUT / "eos-history-subset.csv"))
''')

md(r"""
### 8.2 What the numbers say

The next cell tabulates $w_\mathrm{eff}(A) = w_\mathrm{eff}(B)$, $w_\mathrm{eff}(C)$, $w_3$, $w_t$, $w_{x_0}$ and
$d\ln E/da_4$ at five slices, and checks the physical statements of `reports/eos-checks.json` for these
series: the gas (N = 2352 and 592, $\lambda = 0$) is an exact fold-band gas: $P_3 = E/3$, $P_t = P_0 = 0$ and
$E e^{a_4}$ constant, so $w_\mathrm{eff}(A) = 1/3$ EXACTLY at every slice (radiation-like; it does not fall toward 0,
dust). Under C the same gas reads $w_\mathrm{eff}(C) = 1/3 - 4/9 = -1/9$: not a dark-energy value. N = 8 with
$\hat\lambda = +\lambda_1$ (only the $k = 0$ zero modes, pure interaction energy at the coupling
$\hat\lambda e^{-(5/3)a_4}$): $E < 0$, $P_3 = P_t$, and the hidden-direction pressure $P_0$ is larger than $E$ in
magnitude, so $w_\mathrm{eff}(A) = P_3/E - (P_0 + 3P_t)/(9E)$ lies between 0.2 and 0.41.
""")

code(r'''
rows = ["| series | $a_4$ | $w_\\mathrm{eff}(A)=w_\\mathrm{eff}(B)$ | $w_\\mathrm{eff}(C)$ | $w_3$ | $w_t$ | $w_{x_0}$ | $d\\ln E/da_4$ |",
        "|---|---|---|---|---|---|---|---|"]
for sid, e in EOS.items():
    for i in (0, 10, 20, 30, 40):
        rows.append(f"| {sid} | {e['a4'][i]:.2f} | {e['wA'][i]:.6f} | {e['wC'][i]:.6f} | {e['w3'][i]:.6f} | "
                    f"{e['wt'][i]:.2e} | {e['wx0'][i]:.6f} | {e['dE'][i] / e['E'][i]:.6f} |")
display(Markdown("\n".join(rows)))
gas = [EOS["N2352_lam0"], EOS["N592_lam0"]]
fdev = max(max(float(np.max(np.abs(e["w3"] - 1.0 / 3.0))), float(np.max(np.abs(e["wt"]))),
               float(np.max(np.abs(e["wx0"])))) for e in gas)
edil = max(float(np.max(np.abs(e["E"] * np.exp(e["a4"]) / e["E"][0] - 1.0))) for e in gas)
wdev = max(float(np.max(np.abs(e["wA"] - 1.0 / 3.0))) for e in gas)
cdev = max(float(np.max(np.abs(e["wC"] + 1.0 / 9.0))) for e in gas)
check("gas_exact_fold_band", fdev <= 1e-12 and edil <= 1e-12 and wdev <= 1e-12,
      f"N = 2352 and 592, lambda = 0: P3/E = 1/3 and Pt/E = P0/E = 0 to {fdev:.1e}, E e^(a4) constant to {edil:.1e}: "
      f"w_eff(A) = 1/3 to {wdev:.1e} at every slice (radiation-like, it does not fall toward 0, dust; check "
      "free_gas_exact_fold_band of reports/eos-checks.json)")
check("gas_C_minus_one_ninth", cdev <= 1e-12,
      f"the same states under C: w_eff(C) = 1/3 - 4/9 = -1/9 to {cdev:.1e}: not a dark-energy value")
z = EOS["N8_lamp1"]
check("n8_interacting_zero_modes",
      np.max(np.abs(z["P3"] - z["Pt"])) <= 1e-12 * np.max(np.abs(z["E"])) and np.all(z["E"] < 0)
      and float(np.min(z["wA"])) > 0.2 and float(np.max(z["wA"])) < 0.41,
      f"N = 8, lambda_hat = +lambda_1: P3 = Pt at every slice, E < 0, E(2)/E(0) = {z['E'][-1] / z['E'][0]:.6f} "
      f"(e^(-10/3) = {math.exp(-10 / 3):.6f}: the zero modes are concentrated by the shrinking hidden direction), "
      f"P0/E in [{np.min(z['wx0']):.6f}, {np.max(z['wx0']):.6f}]: w_eff(A) in [{np.min(z['wA']):.6f}, "
      f"{np.max(z['wA']):.6f}] (check n8_interacting_states of reports/eos-checks.json)")
''')

# ------------------------------------------------------------------------------------------------
md(r"""
## 9. CPL tangents and fits

A supernova analysis summarises $w$ by the two CPL numbers $(w_0, w_a)$. The record gives them in two
ways, both recomputed by the next cell:

- the **tangent** at a CHOSEN "today" $a_{4,\mathrm{today}} \in \{0.5, 1, 1.5, 2\}$: $w_0 = w(1)$ and
  $w_a = -dw/da$ at $a = 1$, which is $-dw/da_4$ at $a_{4,\mathrm{today}}$ because $a = e^{a_4 - a_{4,\mathrm{today}}}$;
- the **least-squares fit** over $a \in [1/2, 1]$ and $[1/3, 1]$ (today $a_4 = 2$) and $[1/2, 1]$
  (today $a_4 = 1.5$), and the constant-$w$ fit (the mean of $w$ over the range).

Under C every value is the value under A minus $(4 - 2\beta)/3 = 4/9$; the slopes are the same. The cell
rebuilds the complete entry of each of the three series in `outputs/eos-summary.json` (ranges,
$d\ln E/da_4$ at the two ends, the sign of $E$, tangents, fits, conservation deviations; rounded to 13
significant digits as the record does) and requires it to EQUAL the committed entry. For the exact fold-band
gas $w$ is the constant 1/3 (A) or $-1/9$ (C), so its tangent and fitted $w_a$ vanish to rounding.
""")

code(r'''
TODAY = [0.5, 1.0, 1.5, 2.0]
FIT_RANGES = [(2.0, 0.5), (2.0, 1.0 / 3.0), (1.5, 0.5)]


def r12(v, n=12):
    """the deterministic rounding of compute_eos.py for its JSON outputs"""
    if v is None or (isinstance(v, float) and not math.isfinite(v)):
        return None
    if v == 0:
        return 0.0
    return float(f"{v:.{n}e}")


SUMMARY = load_json(DS / "outputs" / "eos-summary.json")
RECORD_SERIES = {s["series"]: s for s in SUMMARY["series"]}
CPL = {}
for sid, e in EOS.items():
    a4, wA, wC, w3, dwA, dw3 = e["a4"], e["wA"], e["wC"], e["w3"], e["dwA"], e["dw3"]
    tang = []
    for t in TODAY:
        i = int(round(t / H_STEP))
        tang.append({"a4_today": t, "w_eff_A_B": {"w0": r12(wA[i]), "wa": r12(-dwA[i])},
                     "w_eff_C": {"w0": r12(wC[i]), "wa": r12(-dwA[i])},
                     "ratio_w3": {"w0": r12(w3[i]), "wa": r12(-dw3[i])}})
    fits = []
    for t, a1 in FIT_RANGES:
        w0A, waA, wcA = cpl_fit(lambda aa, t=t: interp(a4, wA, t + np.log(aa)), a1)
        w0r, war, wcr = cpl_fit(lambda aa, t=t: interp(a4, w3, t + np.log(aa)), a1)
        fits.append({"a4_today": t, "a_range": [r12(a1), 1.0],
                     "w_eff_A_B": {"w0": r12(w0A), "wa": r12(waA), "w_const": r12(wcA)},
                     "w_eff_C": {"w0": r12(w0A + SHIFT_C), "wa": r12(waA), "w_const": r12(wcA + SHIFT_C)},
                     "ratio_w3": {"w0": r12(w0r), "wa": r12(war), "w_const": r12(wcr)}})
    E, dE = e["E"], e["dE"]
    mine = {"series": sid, "N": int(sid[1:].split("_")[0]), "lambda": e["lambda"],
            "w_eff_A_B_range": [r12(float(np.min(wA))), r12(float(np.max(wA)))],
            "w_eff_C_range": [r12(float(np.min(wC))), r12(float(np.max(wC)))],
            "ratio_w3_range": [r12(float(np.min(w3))), r12(float(np.max(w3)))],
            "ratio_wt_range": [r12(float(np.min(e["wt"]))), r12(float(np.max(e["wt"])))],
            "ratio_wx0_range": [r12(float(np.min(e["wx0"]))), r12(float(np.max(e["wx0"])))],
            "dlnE_da4_at_0_and_end": [r12(float(dE[0] / E[0])), r12(float(dE[-1] / E[-1]))],
            "sign_of_E": "positive" if np.all(E > 0) else ("negative" if np.all(E < 0) else "mixed"),
            "cplTangent": tang, "cplFits": fits,
            "conservation_rel_dev": r12(e["dev"], 3), "conservation_integrated_rel_dev": r12(e["devint"], 3)}
    CPL[sid] = mine
    check(f"{sid}_summary_equals_record", mine == RECORD_SERIES[sid],
          f"ranges, d ln E/d a4, sign of E ({mine['sign_of_E']}), 4 tangents, 3 fits and the conservation deviations "
          "equal the entry of Revision/dark_sector/dirac16complex/outputs/eos-summary.json")
rows = ["| series | today $a_4$ | tangent $w_0$ (C) | tangent $w_a$ |", "|---|---|---|---|"]
for sid in ("N2352_lam0", "N592_lam0", "N8_lamp1"):
    for t in CPL[sid]["cplTangent"]:
        rows.append(f"| {sid} | {t['a4_today']} | {t['w_eff_C']['w0']:.6f} | {t['w_eff_C']['wa']:.3e} |")
rows += ["", "| series | today $a_4$ | range of $a$ | fit $w_0$ (C) | fit $w_a$ | constant $w$ (C) |", "|---|---|---|---|---|---|"]
for sid in ("N2352_lam0", "N592_lam0", "N8_lamp1"):
    for f in CPL[sid]["cplFits"]:
        rows.append(f"| {sid} | {f['a4_today']} | [{f['a_range'][0]:.4f}, 1] | {f['w_eff_C']['w0']:.6f} | "
                    f"{f['w_eff_C']['wa']:.3e} | {f['w_eff_C']['w_const']:.6f} |")
display(Markdown("\n".join(rows)))
tan_wa = [t["w_eff_C"]["wa"] for s in ("N2352_lam0", "N592_lam0") for t in CPL[s]["cplTangent"]]
fit_wa = [f["w_eff_C"]["wa"] for s in ("N2352_lam0", "N592_lam0") for f in CPL[s]["cplFits"]]
check("gas_cpl_constant", max(abs(v) for v in tan_wa + fit_wa) <= 1e-9,
      f"gas N = 2352, 592 (lambda = 0): tangent wa in [{min(tan_wa):.3e}, {max(tan_wa):.3e}], fitted wa in "
      f"[{min(fit_wa):.3e}, {max(fit_wa):.3e}]: zero to rounding (the exact fold-band gas has the constant w_eff(C) = "
      "-1/9), far from the Unite 0.60 (check gas_cpl_far_from_unite of reports/eos-checks.json)")
''')

# ------------------------------------------------------------------------------------------------
md(r"""
## 10. The condensate and the closed formulas, exactly

### 10.1 The condensate drifts

The exact homogeneous solution (the condensate) has $S\,\mathrm{Vol}_7$ constant, $S = S_0e^{a_4}b_4^{-2}$ (it dilutes
with the proper 7-volume), $\rho = mS + \lambda S^2/2$ and $p_3 = p_t = p_0 = \lambda S^2/2$. Hence
$P_3/E = P_t/E = P_0/E = w_c$, the 8-dimensional ratio, which with $u = \lambda S/m$ is

$$
w_c = \frac{p_3}{\rho} = \frac{\lambda S^2/2}{mS + \lambda S^2/2} = \frac{u}{2 + u}, \qquad u \propto e^{a_4}b_4^{-2} \propto e^{-(5/3)a_4}.
$$

So $w_\mathrm{eff}(A) = w_c + (\frac{\beta}{2} - 1)\frac43 w_c = \frac{2\beta - 1}{3}w_c = \frac59 w_c$,
$w_\mathrm{eff}(C) = \frac59 w_c - \frac49$, and the ratio drifts: $w_a = -dw_c/da_4 = \frac{10}{3}u/(2+u)^2$. The next cell
evaluates this with Python's exact fractions at the CHOSEN value $u = -382/441$ (chosen so that the ratio equals
the Unite constant $w$ at one instant: by construction, NOT a prediction), checks the phantom window ($w_c < -1$
exactly for $-2 < u < -1$) on a grid of exact fractions, and compares with the condensate entries of
`outputs/eos-summary.json` and `outputs/effective-formulas.json`.
""")

code(r'''
FORMULAS = load_json(DS / "outputs" / "effective-formulas.json")
COND = SUMMARY["condensate"]
u = Fraction(-382, 441)
ratio = u / (2 + u)
wa_ratio = Fraction(10, 3) * u / (2 + u) ** 2
KA = Fraction(5, 9)                                        # w_eff(A) = ((2 beta - 1)/3) w_c at beta = 4/3
print("u = lambda S/m =", u, "| ratio u/(2 + u) =", ratio, "=", float(ratio), "| wa = (10/3) u/(2 + u)^2 =", wa_ratio, "=",
      float(wa_ratio))
check("condensate_ratio_exact", ratio == Fraction(-764, 1000) and Fraction(FORMULAS["condensate"]["ratio_equals_minus_0p764_at_lambdaS_over_m"]) == u
      and r12(float(u)) == COND["u_for_ratio_minus_0p764_today"] and COND["ratio_today"] == -0.764,
      "u = -382/441 gives the ratio -191/250 = -0.764 exactly (Fraction arithmetic); u equals the entry "
      "ratio_equals_minus_0p764_at_lambdaS_over_m of outputs/effective-formulas.json and u_for_ratio_minus_0p764_today of "
      "outputs/eos-summary.json (check condensate_ratio_value of reports/eos-checks.json)")
check("condensate_drift_exact", wa_ratio == Fraction(-28077, 12500) and r12(float(wa_ratio)) == COND["ratio_wa_at_that_u"]
      and r12(float(KA * wa_ratio)) == COND["wa_A_B_C_at_that_u"]
      and r12(float(KA * ratio)) == COND["w_eff_A_B_today_at_that_u"]
      and r12(float(KA * ratio - Fraction(4, 9))) == COND["w_eff_C_today_at_that_u"],
      f"on the history u ~ e^(-(5/3) a4): the ratio has wa = (10/3) u/(2 + u)^2 = {wa_ratio} = {float(wa_ratio):.6f} "
      f"(thawing sign); w_eff(A) = (5/9) w_c = {KA * ratio} and w_eff(C) = (5/9) w_c - 4/9 = {KA * ratio - Fraction(4, 9)}, "
      f"both with wa = {KA * wa_ratio}; equal to outputs/eos-summary.json (check condensate_drifts of reports/eos-checks.json)")
grid = [Fraction(k, 64) for k in range(-256, 129) if k != -128]
phantom = [v for v in grid if v / (2 + v) < -1]
check("condensate_phantom_window", len(phantom) > 0 and phantom == [v for v in grid if -2 < v < -1]
      and all((KA * v / (2 + v) - Fraction(4, 9) < -1) == (v / (2 + v) < -1) for v in grid),
      f"on the {len(grid)} exact fractions u = k/64 in [-4, 2] (u = -2 excluded): u/(2 + u) < -1 exactly for the "
      f"{len(phantom)} values with -2 < u < -1 and for no other; the observer's w_eff(C) = (5/9) w_c - 4/9 is below -1 "
      "for exactly the same values, and the drift u ~ a^(-5/3) carries u = -382/441 into the window toward the past, "
      f"from a = (382/441)^(3/5) = {(382 / 441) ** 0.6:.4f} to a = (191/441)^(3/5) = {(191 / 441) ** 0.6:.4f}")
check("condensate_effective_formulas", FORMULAS["condensate"]["w_eff_A"] == "((2 beta - 1)/3) w_c"
      and FORMULAS["condensate"]["w_eff_C"] == "A - (4 - 2 beta)/3"
      and FORMULAS["condensate"]["S"] == "S0 e^{a4} b4^{-2} (S Vol_7 constant)",
      "P3/E = Pt/E = P0/E = w_c: w_eff(A, B) = ((2 beta - 1)/3) w_c, w_eff(C) = w_eff(A) - (4 - 2 beta)/3, "
      "S = S0 e^(a4) b4^(-2), as recorded in outputs/effective-formulas.json")
''')

md(r"""
### 10.2 The closed formulas, with exact dual numbers

A **dual number** $u + u'\varepsilon$ with $\varepsilon^2 = 0$ carries an exact derivative along: for any
function built from $+, -, \times, \div$ (and square roots of perfect squares), $f(1 + \varepsilon) =
f(1) + f'(1)\,\varepsilon$ exactly; a power $a^q$ with a rational $q$ at $a = 1$ is $1 + q\varepsilon$ exactly.
With fractions as the two parts, the CPL tangent $w_0 = w(1)$, $w_a = -w'(1)$ of such a $w(a)$ is computed
EXACTLY. The next cell defines this tiny class and uses it to check the closed formulas of
`outputs/effective-formulas.json`:

- the free massive mode in the flat limit (labelled there as such), $q = 0$, which does not feel $b_4$:
  $w_\mathrm{eff}(A) = k^2/(3(M^2a^2 + k^2))$ has the tangent $w_0 = x/(3(1+x))$, $w_a = 2x/(3(1+x)^2)$ with
  $x = k^2/M^2$ (dark-matter-like: it falls from 1/3 to 0, so $w_a > 0$);
- the fold-band gas (radiation-like) plus a $\lambda = 0$ condensate (constant $E$ for every $a_4$, $b_4$) under A:
  $w = \tfrac13\,r/(1+r)$ with $r = r_0/a$ has $w_0 = r_0/(3(r_0+1))$, $w_a = r_0/(3(r_0^2 + 2r_0 + 1))$; under C
  $w_0 - (4 - 2\beta)/3$, which reaches $-0.861$ only for $\beta$ in $(417/2000, 1417/2000]$, not for the history's
  $\beta = 4/3$;
- the observer formula $w_\mathrm{eff} = P_3/E + (\beta/2 - 1)(P_0 + 3P_t)/(3E) - s(4 - 2\beta)/3$ used in section 8.
""")

code(r'''
class Dual:
    """u + u' eps with eps^2 = 0; both parts exact fractions."""

    def __init__(self, a, b=0):
        self.a, self.b = Fraction(a), Fraction(b)

    @staticmethod
    def lift(x):
        return x if isinstance(x, Dual) else Dual(x)

    def __add__(self, o):
        o = Dual.lift(o)
        return Dual(self.a + o.a, self.b + o.b)

    __radd__ = __add__

    def __neg__(self):
        return Dual(-self.a, -self.b)

    def __sub__(self, o):
        return self + (-Dual.lift(o))

    def __rsub__(self, o):
        return Dual.lift(o) - self

    def __mul__(self, o):
        o = Dual.lift(o)
        return Dual(self.a * o.a, self.a * o.b + self.b * o.a)

    __rmul__ = __mul__

    def __truediv__(self, o):
        o = Dual.lift(o)
        return Dual(self.a / o.a, (self.b * o.a - self.a * o.b) / (o.a * o.a))

    def __rtruediv__(self, o):
        return Dual.lift(o) / self

    def __pow__(self, k):
        out = Dual(1)
        for _ in range(k):
            out = out * self
        return out

    def powq(self, q):
        """exact a^q for a rational q; only at a = 1 (where it is 1 + q a' eps)"""
        assert self.a == 1, "a rational power is exact here only at a = 1"
        return Dual(1, Fraction(q) * self.b)

    def sqrt(self):
        """exact square root; the real part must be the square of a fraction"""
        p, q = self.a.numerator, self.a.denominator
        rp, rq = math.isqrt(p), math.isqrt(q)
        assert rp * rp == p and rq * rq == q, "not a perfect square"
        root = Fraction(rp, rq)
        return Dual(root, self.b / (2 * root))


def tangent(w):
    """exact CPL tangent (w0, wa) = (w(1), -w'(1)) of a function of the scale factor a"""
    d = w(Dual(1, 1))
    return d.a, -d.b


BETA_Q = Fraction(4, 3)
flat = FORMULAS["flatModeLabelled"]
mixf = FORMULAS["mixtures"]
ok_flat = flat["massive_w0"] == "x/(3*(x + 1))" and flat["massive_wa"] == "2*x/(3*(x + 1)**2)"
ok_mix = mixf["w0_A"] == "r0/(3*(r0 + 1))" and mixf["wa"] == "r0/(3*(r0**2 + 2*r0 + 1))"
samples = [Fraction(1, 7), Fraction(417, 583), Fraction(1), Fraction(5, 2), Fraction(40)]
for x in samples:
    w0, wa = tangent(lambda a: x / (3 * (a * a + x)))
    ok_flat = ok_flat and w0 == x / (3 * (x + 1)) and wa == 2 * x / (3 * (x + 1) ** 2) and wa > 0
    r0 = x
    w0, wa = tangent(lambda a: Fraction(1, 3) * (r0 / a) / (1 + r0 / a))
    ok_mix = ok_mix and w0 == r0 / (3 * (r0 + 1)) and wa == r0 / (3 * (r0 ** 2 + 2 * r0 + 1))
check("flat_mode_tangent_formulas", ok_flat,
      "massive flat-limit mode w = x/(3 (a^2 + x)): exact dual-number tangent equals the recorded w0 = x/(3*(x + 1)), "
      f"wa = 2*x/(3*(x + 1)**2) > 0 at x = {', '.join(str(s) for s in samples)} (outputs/effective-formulas.json, flatModeLabelled)")
need = Fraction(-861, 1000) + (4 - 2 * BETA_Q) / 3       # r0/(3 (1 + r0)) would have to equal this; it lies in [0, 1/3)
lo, hi = (4 - 3 * Fraction(1, 3) - 3 * Fraction(861, 1000)) / 2, (4 - 3 * Fraction(861, 1000)) / 2
check("fold_band_gas_condensate_mixture_formulas", ok_mix and not (0 <= need < Fraction(1, 3))
      and (lo, hi) == (Fraction(417, 2000), Fraction(1417, 2000))
      and mixf["betaRangeForW0CEqualMinus0p861"].startswith("(417/2000, 1417/2000]"),
      f"w = (1/3) r/(1 + r), r = r0/a: exact tangent equals the recorded w0 = r0/(3*(r0 + 1)), wa = r0/(3*(r0**2 + 2*r0 + 1)); "
      f"under C, w0 - (4 - 2 beta)/3 = -0.861 needs r0/(3 (1 + r0)) = -0.861 + (4 - 2 beta)/3 = {need} at beta = 4/3, outside "
      f"[0, 1/3): no such mixture on the history; it exists only for beta in ({lo}, {hi}] (check mixture_C_matching_w0_unite "
      "of reports/derivation-checks.json)")
check("observer_formulas", FORMULAS["wEff"]["general"] == "P3/E + (beta/2 - 1)(P0 + 3 Pt)/(3E) - s (4 - 2 beta)/3"
      and FORMULAS["conservation"]["integrated"].startswith("dE/da4 = -3 P3 - (beta/2 - 1)(P0 + 3 Pt)"),
      "outputs/effective-formulas.json: w_eff = P3/E + (beta/2 - 1)(P0 + 3 Pt)/(3E) - s (4 - 2 beta)/3, "
      "dE/da4 = -3 P3 - (beta/2 - 1)(P0 + 3 Pt): the formulas used in section 8 (check formulas_input_present of "
      "reports/eos-checks.json)")
''')

# ------------------------------------------------------------------------------------------------
md(r"""
## 11. Mixtures of the gas with a condensate

### 11.1 With a $\lambda = 0$ condensate

A $\lambda = 0$ condensate has no pressure and the constant energy $E_c = mS_0$ for every $a_4$, $b_4$; the gas
(N = 2352, $\lambda = 0$) has $P_{3,g} = E_g/3$ and $E_g \propto e^{-a_4}$, falling as the gas redshifts. The mixture
has $w_\mathrm{eff}(A) = P_{3,g}/(E_g + E_c)$ and $w_\mathrm{eff}(C) = w_\mathrm{eff}(A) - 4/9 \ge -4/9$. The next cell
recomputes, with today at $a_4 = 2$ (CHOSEN), the twelve mixtures of the record with gas fractions today
0.01 ... 1.0 (CHOSEN): tangents and fits, and the smallest $w_\mathrm{eff}(C)$ over 1000 gas fractions and all
slices; it requires each entry to equal `outputs/eos-summary.json`. Neither the Unite $w_0 = -0.861$ nor a
constant $-0.764$ is reached.
""")

code(r'''
g = EOS["N2352_lam0"]
a4g, Eg, P3g = g["a4"], g["E"], g["P3"]
t_today = float(a4g[-1])
it = len(a4g) - 1
MIX = []
for f0 in [0.01, 0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]:
    Ec = Eg[it] * (1 - f0) / f0                      # gas fraction f0 = E_g/(E_g + E_c) at a4_today = 2
    wmA = P3g / (Eg + Ec)
    dwm = deriv(wmA, H_STEP)
    entry = {"gas_fraction_today": f0, "w_eff_A_B": {"w0": r12(wmA[it]), "wa": r12(-dwm[it])},
             "w_eff_C": {"w0": r12(wmA[it] + SHIFT_C), "wa": r12(-dwm[it])}}
    for a1 in (0.5, 1.0 / 3.0):
        w0f, waf, wcf = cpl_fit(lambda aa, wm=wmA: interp(a4g, wm, t_today + np.log(aa)), a1)
        entry[f"fit_a1_{a1:.4f}"] = {"A_B": {"w0": r12(w0f), "wa": r12(waf), "w_const": r12(wcf)},
                                    "C": {"w0": r12(w0f + SHIFT_C), "wa": r12(waf), "w_const": r12(wcf + SHIFT_C)}}
    MIX.append(entry)
check("mixtures_equal_record", MIX == SUMMARY["mixtures_free_gas_today_last_slice"],
      "12 mixtures (gas fractions 0.01 ... 1.0, today a4 = 2): tangents and fits over [1/2, 1] and [1/3, 1] under "
      "A, B and C equal mixtures_free_gas_today_last_slice of outputs/eos-summary.json")
wC_min = min(float(np.min(P3g / (Eg + Eg[it] * (1 - f0) / f0))) for f0 in np.linspace(0.001, 1.0, 1000)) + SHIFT_C
check("mixture_C_cannot_reach_unite_w0", r12(wC_min) == SUMMARY["mixture_C_lambda0_condensate_min_w_eff_C"]
      and wC_min >= SHIFT_C - 1e-12,
      f"gas + lambda = 0 condensate under C: w_eff(C) >= {wC_min:.6f} >= -4/9 at every slice and gas fraction: neither "
      "-0.861 nor a constant -0.764 is reached (check mixture_C_cannot_reach_unite_w0_with_lambda0_condensate)")
''')

md(r"""
### 11.2 A drifting condensate of any ratio, in three definitions

A condensate with $\lambda \neq 0$ has the ratio $w_c = u/(2 + u)$ today and drifts with $u \propto e^{-(5/3)a_4}$:
$E_c = mS_0(1 + u/2)$, $P_c = mS_0\,u/2$ (in every direction), $E_c' = P_c' = -\frac56 mS_0\,u$. The next cell repeats
the record's scan (400 ratios $w_c \in [-3, 0.99]$ today, 201 gas fractions, today $a_4 \in \{0.5, 1, 1.5, 2\}$) for
the gas (N = 2352, $\lambda = 0$) plus such a condensate, in the ratio definition, under A, B and under C, and
requires the closest points to the Unite pair and the range of $w_a$ near the Unite $w_0$ to equal
`outputs/eos-summary.json` (`mixture_scan`).
""")

code(r'''
dEg, dP3g = deriv(Eg, H_STEP), deriv(P3g, H_STEP)
RATE = 1.0 - 2.0 * BETA                                  # d ln u/d a4 = -5/3 (compute_eos.py)
SCANS = {}
for definition in ("ratio", "A_B", "C"):
    best = {"distance": float("inf")}
    min_wa_near, max_wa_near = float("inf"), float("-inf")
    for t2 in TODAY:
        i2 = int(round(t2 / H_STEP))
        wcs = np.linspace(-3.0, 0.99, 400)
        uu = 2 * wcs / (1 - wcs)
        for f0 in np.linspace(0.0, 1.0, 201):
            eg, p3g = f0, f0 * P3g[i2] / Eg[i2]
            deg, dp3g = f0 * dEg[i2] / Eg[i2], f0 * dP3g[i2] / Eg[i2]
            ms0 = (1 - f0) / (1 + uu / 2)
            ec, pc = ms0 * (1 + uu / 2), ms0 * uu / 2
            dec = dpc = 0.5 * RATE * ms0 * uu
            den, dden = eg + ec, deg + dec
            if definition == "ratio":
                num, dnum, shift = p3g + pc, dp3g + dpc, 0.0
            else:
                # the numerator P3 + (beta/2 - 1)(P0 + 3 Pt)/3 of w_eff(A): the condensate has P3 = Pt = P0 = P_c
                num = p3g + pc + (0.5 * BETA - 1.0) * 4.0 * pc / 3.0
                dnum = dp3g + dpc + (0.5 * BETA - 1.0) * 4.0 * dpc / 3.0
                shift = 0.0 if definition == "A_B" else SHIFT_C
            w0 = num / den + shift
            wa = -(dnum * den - num * dden) / den ** 2
            dist = np.hypot(w0 - UNITE["w0"], wa - UNITE["wa"])
            j = int(np.argmin(dist))
            if dist[j] < best["distance"]:
                best = {"distance": float(dist[j]), "a4_today": t2, "w_c_today": float(wcs[j]),
                        "gas_fraction": float(f0), "w0": float(w0[j]), "wa": float(wa[j])}
            near = np.abs(w0 - UNITE["w0"]) <= 0.1
            if np.any(near):
                min_wa_near = min(min_wa_near, float(np.min(wa[near])))
                max_wa_near = max(max_wa_near, float(np.max(wa[near])))
    SCANS[definition] = {"min_wa_with_w0_within_0p1_of_unite": r12(min_wa_near),
                         "max_wa_with_w0_within_0p1_of_unite": r12(max_wa_near),
                         "closest": {k: (r12(v) if isinstance(v, float) else v) for k, v in best.items()}}
check("mixture_scan_equals_record", SCANS == SUMMARY["mixture_scan"],
      "closest points to (-0.861, -0.60): " + "; ".join(
          f"{k}: ({SCANS[k]['closest']['w0']}, {SCANS[k]['closest']['wa']}), distance {SCANS[k]['closest']['distance']}"
          for k in SCANS) + "; every mixture with |w0 + 0.861| <= 0.1 has wa in " + ", ".join(
          f"{k} [{SCANS[k]['min_wa_with_w0_within_0p1_of_unite']}, {SCANS[k]['max_wa_with_w0_within_0p1_of_unite']}]"
          for k in SCANS) + "; equal to mixture_scan of outputs/eos-summary.json (check mixture_scan_three_definitions)")
''')

# ------------------------------------------------------------------------------------------------
md(r"""
## 12. Hypothesis00: dirac16complex00, exactly

dirac16complex00 is a commuting field. Its record (`Revision/dark_sector/dirac16complex00/eos-theory.json`)
builds illustrative populations from adiabatic (WKB) plane-wave modes in the deflating field, an
APPROXIMATION stated there. On the history with $b_4 \propto a^{4/3}$ the proper density of every component
carries the common factor $e^{a_4}b_4^{-2}$; one component $i$ has $\varepsilon_i = w_\mathrm{eff}(N1)_i =
(k_p^2 + (1 - \beta/2)q_p^2)/(3\omega^2) \ge 0$ with $\omega^2 = m^2 + k_p^2 - q_p^2$, $k_p = k/a$ and
$q_p = q\,a\,b_4^{-1/2} \propto a^{1/3}$ (the extra-time momentum BLUESHIFTS as the extra times deflate); a
mixture has $w_\mathrm{eff}(N2) = -(4 - 2\beta)/3 + \sum_i \varepsilon_i\rho_i / \sum_i\rho_i = -4/9 + \dots$. Each
model is normalised to $\rho_\mathrm{tot}(1) = 1$ and keeps the parameters of the withdrawn $b_4 = 1$ record, where
they were CHOSEN to reproduce Unite numbers:

| model | components (parameters CHOSEN on the withdrawn record: by construction there, NOT predictions) |
| --- | --- |
| M2 | one shell of $q = 0$ modes, $k^2/(k^2 + m^2) = 417/1000$ at $a = 1$ |
| M3 | one $k = 0$ mode with $s = q_p^2/m^2 = 417/1417$ at $a = 1$ |
| M4 | condensate $1 - \Omega_q$ plus that kind of mode, $\Omega_q = 57963/264037$, $s = 264037/403037$ |
| M5 | condensate + mode + a **ghost-like** component (massless modes of NEGATIVE classical energy, $\rho_g = -G/a$, $G = 3/10$) |

The next cell computes the exact $N2$ tangents of M2, M3 and M4 with the dual numbers of section 10.2
(at $a = 1$ every square root in the model is $\sqrt{1}$ and $a^{2/3} = 1 + \frac23\varepsilon$, so the arithmetic
stays exact) and compares them with `eos-theory.json`.
""")

code(r'''
THEORY = load_json(D00 / "eos-theory.json")
MODELS = THEORY["models"]
W0U, WAU = Fraction(-861, 1000), Fraction(-3, 5)
EX = 2 - BETA_Q                                         # q_p^2 ~ s a^(2 - beta) = s a^(2/3)


def pw(a, q):
    """a^q: exact for a dual number at a = 1, floating point otherwise"""
    return a.powq(q) if isinstance(a, Dual) else a ** float(q)


def parts(comps, a, sqrt):
    """(rho_tot, sum eps_i rho_i, p3_tot) of a model as eos-theory.json defines it on the history (units m = 1)"""
    R = E = P3 = 0
    for kind, wgt, par in comps:
        if kind == "condensate":                        # lambda = 0: eps = 0, p3 = 0
            r, e, p3 = wgt, 0, 0
        elif kind == "kmode":                           # q = 0, rk = k^2/(k^2 + m^2) at a = 1 (no b4)
            c = par["r"] / (1 - par["r"])
            r = wgt * sqrt((c / (a * a) + 1) / (c + 1))
            e = (c / (a * a)) / (3 * (c / (a * a) + 1))
            p3 = r * e
        elif kind == "qmode":                           # k = 0, s = q_p^2/m^2 at a = 1, q_p^2 = s a^(2/3)
            s = par["s"]
            sa = s * pw(a, EX)
            r = wgt * sqrt((1 - sa) / (1 - s))
            e = (1 - BETA_Q / 2) * sa / (3 * (1 - sa))
            p3 = 0
        elif kind == "ghost":                           # massless k-mode of NEGATIVE energy: rho = -G/a, eps = 1/3
            r = -wgt / a
            e = Fraction(1, 3)
            p3 = r / 3
        R, E, P3 = R + r, E + e * r, P3 + p3
    return R, E, P3


SHIFT_N2 = -(4 - 2 * BETA_Q) / 3                        # w_eff(N2) - w_eff(N1) = -4/9 (eos-theory.json observer)


def wN2(comps, sqrt):
    return lambda a: SHIFT_N2 + parts(comps, a, sqrt)[1] / parts(comps, a, sqrt)[0]


p4 = MODELS["M4_condensate_plus_extra_time_mode"]["parameters"]
s4, Oq4 = Fraction(p4["s"]), Fraction(p4["Omega_q"])
EXACT_MODELS = {
    "M2_positive_good_sector_gas": [("kmode", Fraction(1), {"r": Fraction(417, 1000)})],
    "M3_positive_extra_time_mode": [("qmode", Fraction(1), {"s": Fraction(417, 1417)})],
    "M4_condensate_plus_extra_time_mode": [("condensate", 1 - Oq4, {}), ("qmode", Oq4, {"s": s4})],
}
rows = ["| model | exact $w_0$ (N2) | exact $w_a$ (N2) | decimal | eos-theory.json |", "|---|---|---|---|---|"]
TAN00 = {}
for name, comps in EXACT_MODELS.items():
    w0, wa = tangent(wN2(comps, Dual.sqrt))
    TAN00[name] = (w0, wa)
    rec = MODELS[name]["N2"]["CPL_tangent"]
    rows.append(f"| {name.split('_')[0]} | {w0} | {wa} | ({float(w0):.6f}, {float(wa):+.6f}) | ({rec['w0']}, {rec['wa']}) |")
display(Markdown("\n".join(rows)))
(m2w0, m2wa), (m3w0, m3wa), (m4w0, m4wa) = TAN00.values()
check("M2_tangent_exact", (m2w0, m2wa) == (Fraction(-2749, 9000), Fraction(81037, 500000))
      and str(m2w0) == MODELS["M2_positive_good_sector_gas"]["N2_tangent_exact"]["w0"]
      and str(m2wa) == MODELS["M2_positive_good_sector_gas"]["N2_tangent_exact"]["wa"] and m2wa > 0,
      f"M2: (w0, wa) = ({m2w0}, {m2wa}) exactly = N2_tangent_exact of eos-theory.json = (-4/9 + r/3, (2/3) r (1 - r)): "
      "FREEZING (check M2_tangent_exact of reports/python-derive-eos.json)")
check("M3_tangent_exact", (m3w0, m3wa) == (Fraction(-3583, 9000), Fraction(-196963, 4500000))
      and str(m3w0) == MODELS["M3_positive_extra_time_mode"]["N2_tangent_exact"]["w0"]
      and str(m3wa) == MODELS["M3_positive_extra_time_mode"]["N2_tangent_exact"]["wa"] and m3wa < 0,
      f"M3: (w0, wa) = ({m3w0}, {m3wa}) exactly = N2_tangent_exact of eos-theory.json: thawing sign, small because "
      "q_p grows only like a^(1/3) (check M3_tangent_exact)")
rec4 = MODELS["M4_condensate_plus_extra_time_mode"]["N2"]["CPL_tangent"]
check("M4_tangent_exact", abs(float(m4w0) - float(rec4["w0"])) < 1e-12 and abs(float(m4wa) - float(rec4["wa"])) < 1e-12
      and m4w0 > SHIFT_N2,
      f"M4 with the parameters of the withdrawn tuning (s = {s4}, Omega_q = {Oq4}): tangent ({m4w0}, {m4wa}) = "
      f"({float(m4w0):.12f}, {float(m4wa):.12f}), equal to eos-theory.json; no longer the Unite pair "
      "(check M4_former_tuning_on_the_history)")
''')

md(r"""
### 12.1 No model crosses $w = -1$; positive models stay above $-4/9$; the Unite $w_0$ needs a dominant ghost

With positive-energy components of real frequency only, $w_\mathrm{eff}(N2) = -4/9 + \sum\varepsilon_i\rho_i/\sum\rho_i
\ge -4/9$ at every $a$ at which these conditions hold (all $\varepsilon_i \ge 0$, $\rho_i \ge 0$). The extra-time
mode of M3, M4 and M5 has a real frequency only before its turning point $a_* = s^{-3/2}$ (M3: 6.264; M4: 1.886;
M5: 2.337), all beyond $a = 1$. A ghost component lowers $w_\mathrm{eff}(N2)(1)$ by at most $G/3$, so the Unite
$w_0 = -0.861$ needs $G \ge 3(0.861 - 4/9) = 3749/3000$, and then the total energy of condensate + ghost,
$(1 + G) - G/a$, vanishes at $a = G/(1 + G)$ inside $[1/2, 1]$. The next cell checks these statements in exact
arithmetic, checks that M5 (the withdrawn composition, $G = 3/10$) has no crossing of $-1$ on a fine grid, that
the Unite CPL line itself crosses $-1$ at $a = 461/600$, re-evaluates the four models in floating point at
$a = 1/3, 1/2, 3/4, 1$ against the recorded `w_at` values, and checks that the source the history requires is
anisotropic and grows, so that no condensate is it.
""")

code(r'''
m5 = MODELS["M5_with_ghost_component"]
G5, s5, Oq5, Oc5 = (Fraction(m5["parameters"][k]) for k in ("G", "s", "Omega_q", "Omega_c"))
Gmin = 3 * (Fraction(861, 1000) + SHIFT_N2)
check("unite_w0_requires_dominant_ghost", Gmin == Fraction(3749, 3000) and Fraction(1, 2) < Gmin / (1 + Gmin) < 1
      and Gmin / (1 + Gmin) == Fraction(3749, 6749) and "G >= 3749/3000" in m5["unite"],
      f"w_eff(N2)(1) >= -4/9 - G/3 for any ghost fraction G (positive components raise it): -0.861 needs G >= {Gmin}; for "
      f"condensate + ghost the total energy vanishes at a = G/(1 + G) = {Gmin / (1 + Gmin)} inside [1/2, 1] "
      "(check unite_w0_requires_dominant_ghost)")
inv_s = {"M3": Fraction(1417, 417), "M4": 1 / s4, "M5": 1 / s5}         # a_*^(2/3) = 1/s
astar = {k: float(v) ** 1.5 for k, v in inv_s.items()}
rec_astar = {"M3": float(MODELS["M3_positive_extra_time_mode"]["turning_point_a_star"]["decimal"]),
             "M4": float(MODELS["M4_condensate_plus_extra_time_mode"]["turning_point_a_star"]),
             "M5": float(MODELS["M5_with_ghost_component"]["turning_point_a_star"])}
ok_pos = 0 < 1 - Oq4 and 0 < 1 - Oq5 and all(v > 1 for v in inv_s.values())
check("positive_components_bounded", ok_pos and Oc5 == 1 - Oq5 + G5
      and all(abs(astar[k] - rec_astar[k]) <= 1e-10 for k in astar),
      "M2, M3, M4 and M5 without its ghost-like part: every weight > 0 and s a^(2/3) < 1 for a <= 1 (a_*^(2/3) = 1/s > 1; "
      "turning points a_* = s^(-3/2): " + ", ".join(f"{k} {astar[k]:.3f}" for k in astar) + ", equal to eos-theory.json), "
      "so on 0 < a <= 1 every rho_i > 0 and eps_i >= 0, hence w_eff(N2) >= -4/9 (theorem of eos-theory.json, section wkb; "
      "check positive_models_bounded_by_minus_four_ninths)")
FLOAT_MODELS = {
    "M2_positive_good_sector_gas": [("kmode", 1.0, {"r": 0.417})],
    "M3_positive_extra_time_mode": [("qmode", 1.0, {"s": 417 / 1417})],
    "M4_condensate_plus_extra_time_mode": [("condensate", 1 - 57963 / 264037, {}), ("qmode", 57963 / 264037, {"s": 264037 / 403037})],
    "M5_with_ghost_component": [("condensate", float(Oc5), {}), ("qmode", float(Oq5), {"s": float(s5)}), ("ghost", 0.3, {})],
}
grid5 = np.linspace(1 / 3, 1.0, 2001)
w5 = [-4 / 9 + parts(FLOAT_MODELS["M5_with_ghost_component"], float(x), math.sqrt)[1]
      / parts(FLOAT_MODELS["M5_with_ghost_component"], float(x), math.sqrt)[0] for x in grid5]
check("M5_no_crossing", min(w5) > -1 and m5["N2"]["crossings_of_minus_1_in_[1/3,1]"] == [],
      f"M5 with the withdrawn composition (G = 3/10): min of w_eff(N2) on 2001 points of [1/3, 1] = {min(w5):.6f} > -1, "
      "no crossing (the withdrawn b4 = 1 record had one at a = 0.779; check M5_former_composition_on_the_history)")
unite_cross = 1 + (1 + W0U) / WAU
check("unite_line_crossing", unite_cross == Fraction(461, 600) == Fraction(MODELS["unite"]["crossing_of_minus_1"]["a"])
      and W0U + WAU == Fraction(MODELS["unite"]["deep_past_w0_plus_wa"]),
      f"the Unite CPL line w0 + wa (1 - a) crosses -1 at a = {unite_cross} = {float(unite_cross):.6f}; w0 + wa = {W0U + WAU} "
      "(check unite_crossing_point)")
worst = 0.0
for name, comps in FLOAT_MODELS.items():
    for lab, av in (("1/3", 1 / 3), ("1/2", 0.5), ("3/4", 0.75), ("1", 1.0)):
        R, E, P3 = parts(comps, av, math.sqrt)
        for defn, val in (("N2", -4 / 9 + E / R), ("N1", E / R), ("ratio_p3_over_rho", P3 / R)):
            worst = max(worst, abs(val - float(MODELS[name][defn]["w_at"][lab])))
check("models_w_at_equal_record", worst <= 1e-10,
      f"M2 ... M5 at a = 1/3, 1/2, 3/4, 1 under N2, N1 and the ratio: largest difference from the w_at values of "
      f"eos-theory.json {worst:.2e} (<= 1e-10; the record gives 12 significant digits)")
import ast


def poly_kk(text):
    """exact coefficients (c0, c1, c2) of a recorded polynomial in kk (only +, -, *, /, ** and integers)"""
    def ev(node, kk):
        if isinstance(node, ast.Expression):
            return ev(node.body, kk)
        if isinstance(node, ast.Constant) and isinstance(node.value, int):
            return Fraction(node.value)
        if isinstance(node, ast.Name) and node.id == "kk":
            return kk
        if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.USub):
            return -ev(node.operand, kk)
        if isinstance(node, ast.BinOp):
            a, b = ev(node.left, kk), ev(node.right, kk)
            ops = {ast.Add: lambda: a + b, ast.Sub: lambda: a - b, ast.Mult: lambda: a * b, ast.Div: lambda: a / b,
                   ast.Pow: lambda: a ** int(b)}
            return ops[type(node.op)]()
        raise ValueError("not a polynomial in kk: " + text)
    tree = ast.parse(text, mode="eval")
    v0, v1, v2 = (ev(tree, Fraction(x)) for x in (0, 1, 2))
    c2 = (v2 - 2 * v1 + v0) / 2
    c1 = v1 - v0 - c2
    assert ev(tree, Fraction(3)) == v0 + 3 * c1 + 9 * c2, "not quadratic"
    return v0, c1, c2


src = THEORY["condensate"]["historyRequiredSource"]
mrho, p3s, pts, p0s = (poly_kk(src[k]) for k in ("minus_rho", "p3", "pt", "p0"))
aniso = tuple(x - y for x, y in zip(p3s, p0s))
check("history_required_source", aniso == (Fraction(2015, 972), Fraction(1069, 432), Fraction(-9, 16)) and pts == p0s
      and p3s[2] == mrho[2] == Fraction(-9, 16),
      "the source the author's equations need on the history (kappa T - Lambda, kk = e^((2/3) H x4)): kappa p0 - Lambda = "
      f"kappa p_t - Lambda = {src['p0']}, and the anisotropy kappa (p3 - p0) = {aniso[2]} kk^2 + {aniso[1]} kk + {aniso[0]}, "
      "not zero and growing with x4; every condensate has p3 = p_t = p0 and S ~ e^(-(5/3) a4) decays, so no condensate "
      "is that source (checks history_required_source and condensate_cannot_source_history of "
      "reports/python-derive-eos.json, D6_history_source_anisotropic of the Wolfram twin)")
print("ghost-like sector (eos-theory.json):", THEORY["ghost"][:250], "...")
''')

# ------------------------------------------------------------------------------------------------
md(r"""
## 13. The check counts of the committed dark-sector reports

This notebook re-runs three of the 15 series and none of the independent implementations. The next
cell reads the seven committed report files of the two hypotheses and asserts their counts exactly as the
files give them: `derivation-checks.json` (sympy derivation of the effective formulas in the corrected
metric), `ks-history-run.json` (the 615 solver runs), `eos-checks.json` (equation of state, CPL, mixtures),
`independent-checks.json` (an independent numpy implementation of the key numbers), for
dirac16complex00 `python-derive-eos.json` (implementation A) and `python-independent-numerics.json`
(implementation B: the 16-component field equation integrated in time), and `wolfram-dark-sector.json` (the
independent Wolfram verification in the corrected metric with the author's T16). The Wolfram twin of the
withdrawn metric, `wolfram-dark-sector-b4.json`, is kept as its record and is not used here.
""")

code(r'''
def counts(path):
    rep = load_json(path)
    listed = sum(c["verdict"] == "PASS" for c in rep["checks"])
    s = rep.get("summary")
    if isinstance(s, str):                               # dirac16complex00: "48/48 checks pass"
        passed, total = (int(v) for v in s.split()[0].split("/"))
        failed = total - passed
    elif s is None:                                      # the Wolfram report: checkCount, failedCount
        total, failed = rep["checkCount"], rep["failedCount"]
        passed = total - failed
    else:
        total, passed, failed = s["total"], s["pass"], s["fail"]
    return total, passed, failed, listed, len(rep["checks"])


EXPECTED = {DS / "reports" / "derivation-checks.json": 37, DS / "reports" / "ks-history-run.json": 8,
            DS / "reports" / "eos-checks.json": 13, DS / "reports" / "independent-checks.json": 10,
            D00 / "reports" / "python-derive-eos.json": 48, D00 / "reports" / "python-independent-numerics.json": 32,
            REPO / "Revision" / "dark_sector" / "reports" / "wolfram-dark-sector.json": 7}
print("record file                                                                 checks  passed  failed")
for path, n in EXPECTED.items():
    total, passed, failed, listed, length = counts(path)
    print(f"{shown(path):74s} {total:6d}  {passed:6d}  {failed:6d}")
    check(f"record_{path.name}", (total, passed, failed, listed, length) == (n, n, 0, n, n),
          f"{path.name}: {passed}/{total} checks pass, {failed} fail, {listed} listed checks with verdict PASS")
''')

# ------------------------------------------------------------------------------------------------
md(r"""
## 14. Teaching figures

Each figure is drawn from the computations of this notebook and is also saved as a PNG file in
`<output>/figures`.

### 14.1 Figure 1: the effective equation of state of the Kohn-Sham gas under A, B and C

Left: $w_\mathrm{eff}(A) = w_\mathrm{eff}(B)$ along the history for the three series, with the reference values
1/3 (radiation) and 0 (dust): the two gases lie exactly at 1/3 (fold-band gases); the interacting zero modes
(N = 8) lie between 0.24 and 0.41. Right: the same states under normalisation C,
$w_\mathrm{eff}(C) = w_\mathrm{eff}(A) - 4/9$, with the Unite constant $w = -0.764$, the Unite $w_0 = -0.861$ and
$w = -1$: the gas lies at $-1/9$, far above the Unite values. The two panels show the SAME states: only the
observer ASSUMPTION differs (by $(4 - 2\beta)/3 = 4/9$ on the history with $b_4 \propto e^{(4/3)a_4}$).
""")

code(r'''
def save_and_show(fig, name):
    path = FIG_DIR / name
    fig.savefig(path, format="png", dpi=100, metadata={"Software": None})
    plt.close(fig)
    display(Image(data=path.read_bytes()))
    print("figure saved:", shown(path), "| sha256", sha256(path))


STYLE = {"N2352_lam0": ("C0", "-"), "N592_lam0": ("C1", "--"), "N8_lamp1": ("C2", ":")}
LABEL = {"N2352_lam0": r"gas N = 2352, $\lambda$ = 0", "N592_lam0": r"gas N = 592, $\lambda$ = 0",
         "N8_lamp1": r"zero modes N = 8, $\hat\lambda = +\lambda_1$"}
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.4))
for sid, e in EOS.items():
    colour, ls = STYLE[sid]
    ax1.plot(e["a4"], e["wA"], color=colour, ls=ls, lw=2, label=LABEL[sid])
    ax2.plot(e["a4"], e["wC"], color=colour, ls=ls, lw=2, label=LABEL[sid])
ax1.axhline(1 / 3, color="k", lw=0.8, ls=":")
ax1.text(0.02, 1 / 3 + 0.01, "radiation 1/3", fontsize=8)
ax1.axhline(0, color="k", lw=0.8, ls=":")
ax1.text(0.02, 0.01, "dust 0", fontsize=8)
ax1.set_xlabel(r"slice $a_4$ (the extra times deflate as $e^{-a_4} b_4^{1/2} = e^{-a_4/3}$)")
ax1.set_ylabel(r"$w_\mathrm{eff}(A) = w_\mathrm{eff}(B)$")
ax1.set_title("normalisations A and B")
ax1.set_ylim(-0.05, 0.75)
ax1.legend(fontsize=8, loc="lower right")
ax1.grid(True, alpha=0.3)
for val, txt, col in ((-1.0, "w = -1", "k"), (UNITE["w0"], "Unite w0 = -0.861", "C3"), (UNITE["w_const"], "Unite constant w = -0.764", "C4")):
    ax2.axhline(val, color=col, lw=1, ls="-." if col != "k" else ":")
    ax2.text(1.1, val + 0.025, txt, fontsize=8, color=col)
ax2.axhline(0, color="k", lw=0.8, ls=":")
ax2.set_xlabel(r"slice $a_4$")
ax2.set_ylabel(r"$w_\mathrm{eff}(C) = w_\mathrm{eff}(A) - 4/9$")
ax2.set_title("normalisation C (the same states)")
ax2.set_ylim(-1.08, 0.45)
ax2.legend(fontsize=8, loc="center right")
ax2.grid(True, alpha=0.3)
fig.tight_layout()
save_and_show(fig, "figure1_w_eff_histories.png")
''')

md(r"""
### 14.2 Figure 2: mixtures of the gas with a condensate, against the Unite line

$w_\mathrm{eff}(C)$ of the gas (N = 2352, $\lambda = 0$) mixed with a $\lambda = 0$ condensate, against the observer's
scale factor $a = e^{a_4 - 2}$ (today $a_4 = 2$, CHOSEN), for several CHOSEN gas fractions today, and the drifting
condensate alone with the ratio $-0.764$ today ($w_\mathrm{eff}(C) = \frac59 w_c - \frac49$, section 10.1, with
$u = u_\mathrm{today}a^{-5/3}$). The condensate is drawn only for $a > (|u_\mathrm{today}|/2)^{3/5} = (191/441)^{3/5}
= 0.605$: there its energy $mS_0(1 + u/2)$ vanishes (dotted vertical line) and its $w$ diverges. The black line is
the Unite CPL line $w = -0.861 - 0.60(1 - a)$, which falls below $-1$ for $a < 461/600$. Every mixture with a
$\lambda = 0$ condensate stays above $-4/9$; the drifting condensate falls below $-1$ but with a slope far
steeper than the Unite line's.
""")

code(r'''
a_obs = np.exp(a4g - 2.0)
fig, ax = plt.subplots(figsize=(8.5, 4.8))
for k, f0 in enumerate((0.2, 0.4, 0.6, 0.8, 1.0)):
    Ec = Eg[it] * (1 - f0) / f0
    ax.plot(a_obs, P3g / (Eg + Ec) + SHIFT_C, color=plt.cm.viridis(0.15 + 0.17 * k), lw=1.8,
            label=f"gas fraction today {f0:.1f} (lambda = 0 condensate)")
a_pole = math.exp(-0.6 * math.log(2.0 / abs(float(u))))          # E_c = m S0 (1 + u/2) = 0: u = -2
a_fine = np.linspace(a_pole + 1e-3, 1.0, 400)
u_fine = float(u) * a_fine ** (-5.0 / 3.0)                         # u ~ e^(-(5/3) a4) = u_today a^(-5/3)
ax.plot(a_fine, (5 / 9) * u_fine / (2 + u_fine) - 4 / 9, color="C3", lw=2.5, ls="--",
        label=f"drifting condensate, ratio -0.764 today (energy 0 at a = {a_pole:.3f})")
ax.axvline(a_pole, color="C3", lw=0.8, ls=":")
aa = np.linspace(a_obs[0], 1.0, 200)
ax.plot(aa, UNITE["w0"] + UNITE["wa"] * (1 - aa), color="k", lw=2, label="Unite CPL line (-0.861, -0.60)")
ax.axhline(-1, color="k", lw=0.8, ls=":")
ax.axhline(-4 / 9, color="C7", lw=0.8, ls=":")
ax.axhline(UNITE["w_const"], color="C4", lw=1, ls="-.", label="Unite constant w = -0.764")
ax.set_xlabel(r"observer scale factor $a = e^{a_4 - 2}$ (today $a$ = 1)")
ax.set_ylabel(r"$w_\mathrm{eff}(C)$")
ax.set_ylim(-3.0, 0.2)
ax.set_title("normalisation C on the history of the corrected metric: mixtures stay above -4/9")
ax.legend(fontsize=7.5, loc="lower right")
ax.grid(True, alpha=0.3)
fig.tight_layout()
save_and_show(fig, "figure2_mixtures.png")
''')

md(r"""
### 14.3 Figure 3: the dirac16complex00 populations against the Unite CPL line

Left: $w_\mathrm{eff}(N2)$ of the four models M2 to M5 over $a \in [1/3, 1]$ on the history with $b_4 \propto a^{4/3}$
(the parameters of every model are those CHOSEN on the withdrawn record), the Unite CPL line, $w = -1$ and the bound
$-4/9$ of positive-energy content. No model reaches the Unite line or crosses $-1$; M5, with its ghost-like
component, dips below $-4/9$ but stays above $-1$. Right: the same models under N1 (= the reading B of
section 4.3): M2 is the dark-matter-like law from 1/3 toward 0.
""")

code(r'''
a3 = np.linspace(1 / 3, 1.0, 400)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11.5, 4.6))
names = {"M2_positive_good_sector_gas": "M2 good-sector gas", "M3_positive_extra_time_mode": "M3 extra-time mode",
         "M4_condensate_plus_extra_time_mode": "M4 condensate + mode",
         "M5_with_ghost_component": "M5 with a ghost-like part"}
for k, (name, comps) in enumerate(FLOAT_MODELS.items()):
    vals = [parts(comps, float(x), math.sqrt) for x in a3]
    ax1.plot(a3, [-4 / 9 + E / R for R, E, _ in vals], color=f"C{k}", lw=2, label=names[name])
    ax2.plot(a3, [E / R for R, E, _ in vals], color=f"C{k}", lw=2, label=names[name])
ax1.plot(a3, UNITE["w0"] + UNITE["wa"] * (1 - a3), color="k", lw=2, ls="--", label="Unite CPL line")
ax1.axhline(-1, color="k", lw=0.8, ls=":")
ax1.axhline(-4 / 9, color="C7", lw=0.8, ls=":")
ax1.text(0.35, -4 / 9 + 0.02, "-4/9: bound of positive-energy content", fontsize=8, color="C7")
ax1.set_xlabel("observer scale factor $a$")
ax1.set_ylabel(r"$w_\mathrm{eff}(N2)$")
ax1.set_title("dirac16complex00 populations under N2")
ax1.legend(fontsize=7.5, loc="lower right")
ax1.grid(True, alpha=0.3)
ax2.axhline(1 / 3, color="k", lw=0.8, ls=":")
ax2.axhline(0, color="k", lw=0.8, ls=":")
ax2.set_xlabel("observer scale factor $a$")
ax2.set_ylabel(r"$w_\mathrm{eff}(N1)$")
ax2.set_title("the same populations under N1 (colours as on the left)")
ax2.grid(True, alpha=0.3)
fig.tight_layout()
save_and_show(fig, "figure3_dirac16complex00_populations.png")
''')

md(r"""
### 14.4 Figure 4: every candidate in the $(w_0, w_a)$ plane

Each point is one $(w_0, w_a)$ pair computed or re-checked above, against the Unite pair $(-0.861, -0.60)$
(star). Blue: the Kohn-Sham gas under C (tangents at the four CHOSEN "todays" and the three fits). Purple: the
twelve gas + $\lambda = 0$ condensate mixtures under C (tangent, today $a_4 = 2$). Red: the closest points of the
drifting-condensate scans in the three definitions. Black: the drifting condensate with the ratio $-0.764$ today,
under C. Green: the dirac16complex00 models under N2 (exact tangents of M2, M3, M4; least-squares fits over
$[1/2, 1]$ of M2 to M5). Points below the dotted line $w_0 + w_a = -1$ have a CPL line that is phantom in the far
past. Nothing reaches the Unite pair.
""")

code(r'''
fig, ax = plt.subplots(figsize=(8.5, 5.6))
gas_t = [(t["w_eff_C"]["w0"], t["w_eff_C"]["wa"]) for s in ("N2352_lam0", "N592_lam0") for t in CPL[s]["cplTangent"]]
gas_f = [(f["w_eff_C"]["w0"], f["w_eff_C"]["wa"]) for s in ("N2352_lam0", "N592_lam0") for f in CPL[s]["cplFits"]]
ax.scatter(*zip(*gas_t), color="C0", marker="o", s=28, label="Kohn-Sham gas, C, tangents")
ax.scatter(*zip(*gas_f), color="C0", marker="^", s=28, label="Kohn-Sham gas, C, fits")
mixC = [(m["w_eff_C"]["w0"], m["w_eff_C"]["wa"]) for m in MIX]
ax.scatter(*zip(*mixC), color="C4", marker="D", s=22, label="gas + lambda = 0 condensate, C, tangents")
for k, (d, sc) in enumerate(SCANS.items()):
    ax.scatter([sc["closest"]["w0"]], [sc["closest"]["wa"]], color="C3", marker="x", s=48,
               label="drifting-condensate scans, closest points" if k == 0 else None)
ax.scatter([COND["w_eff_C_today_at_that_u"]], [COND["wa_A_B_C_at_that_u"]], color="k", marker="s", s=40,
           label="condensate (ratio -0.764 today), C")
TAN_LABEL_OFFSET = {"M2": (6, -10), "M3": (8, 3), "M4": (8, -11)}
for name, (w0, wa) in TAN00.items():
    short = name.split("_")[0]
    ax.scatter([float(w0)], [float(wa)], color="C2", marker="o", s=48)
    ax.annotate(short + " tangent", (float(w0), float(wa)), TAN_LABEL_OFFSET[short], textcoords="offset points",
                fontsize=8, color="C2")
FIT_LABEL_OFFSET = {"M2": (6, 2), "M3": (-46, 3), "M4": (-46, -11), "M5": (6, -12)}
for name in FLOAT_MODELS:
    fit = MODELS[name]["N2"]["fit_a_1/2_to_1"]
    short = name.split("_")[0]
    ax.scatter([float(fit["w0"])], [float(fit["wa"])], color="C2", marker="^", s=48)
    ax.annotate(short + " fit", (float(fit["w0"]), float(fit["wa"])), FIT_LABEL_OFFSET[short], textcoords="offset points",
                fontsize=8, color="C2")
ax.scatter([UNITE["w0"]], [UNITE["wa"]], color="C3", marker="*", s=260, zorder=5, label="Unite (-0.861, -0.60)")
ww = np.linspace(-1.1, 0.1, 10)
ax.plot(ww, -1 - ww, color="k", lw=0.8, ls=":", label="$w_0 + w_a = -1$")
ax.set_xlim(-1.08, 0.12)
ax.set_ylim(-2.0, 0.3)
ax.set_xlabel("$w_0$")
ax.set_ylabel("$w_a$")
ax.set_title("CPL pairs on the history of the corrected metric, against the Unite pair")
ax.legend(fontsize=7, loc="lower right")
ax.grid(True, alpha=0.3)
fig.tight_layout()
save_and_show(fig, "figure4_w0_wa_plane.png")
''')

md(r"""
### 14.5 Summary of this notebook's checks

The last code cell counts the checks of this notebook (each printed a PASS line above; a failure would
have stopped the notebook at that point) and lists the files written into `<output>` (the 123 result
files of the solver are summarised in one line).
""")

code(r'''
print(f"checks of this notebook: {len(CHECKS)} passed, 0 failed")
runs = sorted(RUN_DIR.glob("*.json"))
print(f"  <output>/ks_runs/*.json: {len(runs)} result files, {sum(p.stat().st_size for p in runs)} bytes")
for path in sorted(p for p in OUT.rglob("*") if p.is_file() and TARGET not in p.parents
                     and "cargo-target" not in p.relative_to(OUT).parts and p.parent != RUN_DIR):
    print(f"  {shown(path):48s} {path.stat().st_size:7d} bytes")
''')

md(r"""
## 15. What this notebook showed, and what it did not show

**Showed.**

- The Revision Kohn-Sham solver builds without warnings, checks its inputs and runs with the parameters
  of the committed record. 123 states of the dense history $a_4 = Hx_4$, $b_4(x_4) = b_4(0)e^{(4/3)Hx_4}$ of the
  corrected metric (N = 2352 and N = 592 without interaction, N = 8 with $+\lambda_1$; 41 slices each), solved anew
  with the arguments of `run_ks_history.py` (the cell volume grows like $e^{(5/3)a_4}$, the hidden scale is
  $f = e^{-a_4/3}$), reproduce the committed rows of `ks-history-dense.csv` character for character, with the same
  occupied levels at every slice.
- Recomputed exactly as `compute_eos.py` does, the equation-of-state rows equal `eos-history.csv`, and the
  CPL tangents, fits, ranges and conservation deviations of the three series equal `eos-summary.json`; the
  conservation law $dE/da_4 = -3P_3 + P_t + \frac13P_0$ holds to the stencil's truncation error, while the law of
  the inflating 3-space alone, $dE/da_4 = -3P_3$, fails for the interacting series.
- The free Kohn-Sham gas is an exact fold-band gas: $w_\mathrm{eff}(A) = w_\mathrm{eff}(B) = 1/3$ exactly
  (radiation-like) at every slice; under the normalisation C the same states read $w_\mathrm{eff}(C) = -1/9$ with
  $w_a = 0$, far from the Unite pair $(-0.861, -0.60)$. The interacting zero modes ($E < 0$) have
  $w_\mathrm{eff}(A)$ between 0.24 and 0.41.
- The condensate ratio equals $-0.764$ exactly at the CHOSEN $\lambda S/m = -382/441$ at one instant (by
  construction); on the history it drifts, with $w_a = -28077/12500$ exactly. Mixtures with a $\lambda = 0$
  condensate stay above $-4/9$ under C; the scans with a drifting condensate come closest to the Unite pair
  under C, at the distance 0.160 (the pure condensate with the ratio $-0.47$ today at $a_{4,\mathrm{today}} = 0.5$:
  $(w_0, w_a) = (-0.706, -0.640)$, CHOSEN, not a prediction). Under C the drifting $\lambda < 0$ condensate crosses
  $-1$ toward the past, from $a = (382/441)^{3/5} = 0.9174$ on, where its ratio enters the phantom window
  $-2 < \lambda S/m < -1$.
- For dirac16complex00 the tangents of M2 ($-2749/9000$, $+81037/500000$, freezing) and M3 ($-3583/9000$,
  $-196963/4500000$) are exact fractions; positive-energy models stay above $-4/9$; no model M2 to M5 crosses $-1$;
  the Unite $w_0$ would need a ghost fraction of at least $3749/3000$; the source the history requires is
  anisotropic, $\kappa(p_3 - p_0) = -\frac{9}{16}k^2 + \frac{1069}{432}k + \frac{2015}{972}$ with $k = e^{(2/3)Hx_4}$, and
  grows, so no condensate is it.
- The seven committed dark-sector reports record 37, 8, 13, 10, 48, 32 and 7 checks, all passed.

**Did not show.**

- Neither Hypothesis nor Hypothesis00 is established. Nothing computed here produces the Unite values from a
  state of the theory; on the withdrawn $b_4 = 1$ record they were reached only by models whose parameters were
  SOLVED to reach them, and those parameters are CHOSEN, not predicted.
- The observer normalisation (A, B or C; N1 or N2) is an ASSUMPTION; the verdict changes by exactly $4/9$
  between them on the history. $a_{4,\mathrm{today}}$ and the gas fractions are CHOSEN; $b_4(0)$ enters only
  through $\hat\lambda$.
- The history $a_4 = H x_4$, $b_4 \propto e^{(4/3)Hx_4}$ is prescribed: the Kohn-Sham gas is a test field without
  back-reaction and not an admissible source; on this history the observer's expansion reads
  $w_\mathrm{exp} = -1$ exactly. Both fold conditions are filled (ASSUMED) and the filling of the positive branch is
  a CONVENTION; only $T = 0$ and $a_4 \in [0, 2]$ are used.
- This notebook re-ran 3 of the 15 series; the other 12 series, the sympy derivation, the independent
  free-gas implementation, both dirac16complex00 implementations and the Wolfram verification are only quoted
  through their committed reports. The dirac16complex00 models rest on the WKB approximation stated in its
  record, and its growing modes (an ill-posed Cauchy problem) are not cured anywhere.
- There is no supernova likelihood: the "fits" are least squares of $w(a)$, not fits to data.
""")
