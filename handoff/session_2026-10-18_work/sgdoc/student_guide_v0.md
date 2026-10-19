# A student's guide to the Kohn–Sham computation of dirac16complex

## Installing, deriving, running and checking the Stage-4 solvers for the ground and first excited states in the primordial gravitational field on Windows, macOS and Linux

## Abstract

{{abstract}}

## 1. What you will compute and why

### 1.1 The question

The dirac16complex project studies a new fermion field, a 16-component complex Grassmann spinor field in eight dimensions with four space-like and four time-like directions. Stages 1 and 2 derived its physics in a general and in the author's primordial gravitational field; Stage 3 solved its equations for a single mode in homogeneous backgrounds.

Stage 4 asks a many-particle question: **what is the ground state, and what is the first excited state, of $N$ dirac16complex particles held in the primordial gravitational field, when the particles repel or attract each other?** The tool is Kohn–Sham density-functional theory (Section 6.2) with an interaction potential derived from the thermodynamics of the uniform dirac16complex gas (Section 6.3). The answers, in one paragraph (the main document `provenance/DIRAC16COMPLEX_KOHN_SHAM_PRIMORDIAL` gives them in full):

- the particles collect at a membrane, the brane, where two copies of the field are glued together: 87 % to 96 % of them lie within one unit of length of it (Section 6.4);
- the lowest levels form a "brane band" whose energy grows linearly with the momentum along 3-space, $\varepsilon=ck$ with $c=1.9051482536$;
- the first excited state moves one particle across the gap between two momentum shells of the finite periodic 3-space; the interaction changes it by less than 3 %, except in one case where two levels cross at the Fermi level and the program has to use a smeared occupation (Section 7.5);
- the energy density of these states is positive, while the field, if Einstein gravity produced it, would need a negative one: the states cannot be the source of the field.

### 1.2 What the computation consists of

| part | program | what it does |
| --- | --- | --- |
| exact theory | `wolfram/Dirac16ComplexKohnSham.wl` with `scripts/verify_dirac16complex_kohn_sham.wls`; `scripts/check_dirac16complex_kohn_sham_theory.py` | derives the geometry, the reduction to $2\times2$ blocks, the exchange and the functional exactly (125 Wolfram checks, 157 independent sympy checks) |
| Rust solver | `studies/dirac16complex_kohn_sham` | solves the Kohn–Sham equations by CVODE shooting; five subcommands `spectrum`, `scf`, `excited`, `thermo`, `emt` (397 self-checks) |
| reference solver | `scripts/ks_reference_solver.py` | solves the same problems independently by a matrix method in numpy |
| cross-checker | `scripts/check_dirac16complex_kohn_sham.py` | compares the two solvers run by run and checks many identities |
| determinism tool | `studies/dirac16complex_kohn_sham/tools/compare_runs.py` | compares a repeated and a tighter-tolerance Rust run with the committed one |
| summary | `studies/dirac16complex_kohn_sham/tools/build_kohn_sham_summary.py` | collects every check count and key number into `kohn-sham-summary.json` |
| Jupyter notebook | `notebooks/dirac16complex_kohn_sham.ipynb` | reruns parts, recomputes key numbers, draws the figures, 60 checks |
| Mathematica notebook | `notebooks/Dirac16ComplexKohnSham.nb` | an independent symbolic and numerical cross-check (optional) |
| gate | `scripts/verify_stage4_kohn_sham.ps1` and `.sh` | reruns and compares everything; ends with `stage4_kohn_sham_verification=OK` |

All outputs are under `artifacts/dirac16complex/kohn-sham/`.

### 1.3 What you will have at the end

1. A built Rust program that answers `print-config` with `SUCCESS` and reproduces the committed spectrum files byte for byte (Sections 5 and 8).
2. Your own runs of the cheap computations (the spectrum, the quick parameter matrix, the reference solver's quick mode, the theory checker), checked against the committed results.
3. The knowledge to read every output file (Section 9), to run the checkers and notebooks (Sections 10 to 13) and, if you have a fast computer and a few hours, the complete gate (Section 14).
4. The understanding to change a parameter, predict the result and check the prediction (Section 16).

### 1.4 What the results do not say

Stage 4 computes the static member of the primordial field, with frozen extra times. On 2026-09-30, after Stage 4 had been specified, the author corrected the model: the three extra times deflate exponentially. The static member is therefore not a model of the author's field; the folder `Revision/` treats the author's field anew. Stage 4 is documented here as specified and completed (Section 6.4; main document, Section 12).

## 2. How to use this guide

### 2.1 Conventions

- **Everything is counted from 0**: coordinates $x_0,\dots,x_7$, spinor components $\Psi_0,\dots,\Psi_{15}$, the first entry of a list is entry 0.
- A box contains commands. Type or paste them one line at a time into a terminal and press Enter after each line; the prompt of the terminal is not shown. The sentence before a box says which terminal it is for. **PowerShell** means PowerShell 7 on Windows; **Git Bash** the bash of Git for Windows; **macOS** and **Linux** the Terminal with bash or zsh. Commands marked "bash" work in Git Bash, macOS and Linux.
- **Repository root** means the folder `Dirac_claude` that `git clone` creates. Unless a box starts with `cd`, run it from the repository root.
- On Windows the commands write `python`; on macOS and Linux write `python3` if `python` is not found, or activate the virtual environment of Section 3.3, inside which `python` works.
- **Run labels.** A Rust or reference run is named like `m1_L3_N112_lamp1_T0`: mass $m/H=1$, tip cutoff $L=3$, particle number $N=112$, coupling `lamp1` $=+\hat\lambda_1$ (`lam0` is $\lambda=0$, `lamm1` $-\hat\lambda_1$, `lamp2` $+\hat\lambda_2$, `lamm2` $-\hat\lambda_2$, `lamh` the hot coupling of Section 7.8), temperature `T0` ($T=0$; `T0p1`, `T0p3`, `T1` are $T/m=0.1$, $0.3$, $1$). Suffixes: `_g601` a grid of 601 points, `_a40p5` the run with $a_4=0.5$, `_dk0p125` a momentum step of $0.125m$.
- "Expected output" shows what a command prints when everything works. Check counts and file counts must match exactly; run times depend on your computer.

### 2.2 Terminals

- **Windows, PowerShell 7**: Start menu, type `pwsh`, Enter.
- **Windows, Git Bash**: Start menu, type `Git Bash`, Enter.
- **macOS**: Applications, Utilities, Terminal. **Linux**: your terminal (often Ctrl+Alt+T).

`cd FOLDER` changes folder, `cd ..` goes up, `pwd` prints where you are, `ls` lists the folder.

## 3. Installing the tools

### 3.1 What you need

| tool | needed for | required? |
| --- | --- | --- |
| Git | the code and the solver engine | yes |
| Rust (rustup, rustc, cargo) with rustfmt and clippy | the Rust solver | yes |
| a C linker (MSVC Build Tools, Xcode Command Line Tools or build-essential) | linking the Rust program | yes |
| Python 3.11 or newer with numpy, sympy, mpmath, matplotlib | the reference solver, the checkers, the notebook | yes |
| nbformat, nbclient, nbconvert, ipykernel | executing the Jupyter notebook | for Section 12 |
| WolframScript (Wolfram Engine or Mathematica) | the exact theory verifier and the Mathematica notebook | optional |
| a TeX distribution (MiKTeX, MacTeX or TeX Live) | rebuilding the PDFs | optional |

The tools are the same as for Stage 3. The Stage-3 student guide (`provenance/DIRAC16COMPLEX_STUDENT_GUIDE`, Section 3) explains each installer in detail, including the order of the Windows installers and the failure messages; the short form follows. Installers change your computer; they were not executed for this guide (Section 2.3).

### 3.2 Windows 11, macOS and Linux

**Windows (PowerShell).** First the C++ build tools that Rust needs, then the other tools; close every terminal afterwards and open a new one:

```
$id = "Microsoft.VisualStudio.2022.BuildTools"
$vs = "--wait --passive --add Microsoft.VisualStudio.Workload.VCTools"
winget install --id $id -e --override "$vs --includeRecommended"
winget install --id Git.Git -e
winget install --id Microsoft.PowerShell -e
winget install --id Rustlang.Rustup -e
winget install --id Python.Python.3.14 -e
```

Optional: `winget install --id MiKTeX.MiKTeX -e` and `winget install --id WolframResearch.WolframEngine -e` (activate it once with `wolframscript -activate`). Then, in a new terminal:

```
rustup default stable
rustup component add rustfmt clippy
```

**macOS (Terminal).** `xcode-select --install`, then Rust and Python:

```
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source "$HOME/.cargo/env"
```

and Python 3 from https://www.python.org/downloads/ (or `brew install python`).

**Linux (Ubuntu or Debian).**

```
sudo apt update
sudo apt install -y git curl build-essential python3 python3-venv python3-pip
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source "$HOME/.cargo/env"
```

Optional for the PDFs: `sudo apt install -y texlive-latex-base texlive-latex-recommended lmodern`.

### 3.3 The Python packages

The committed Stage-4 files were produced on Windows with Python 3.14.5 and the package versions of `requirements-stage3.txt` (numpy 2.4.6, matplotlib 3.11.0, sympy 1.14.0, nbformat 5.10.4, nbclient 0.10.2, ipykernel 7.1.0), plus mpmath and nbconvert. **Windows:**

```
python -m pip install -r requirements-stage3.txt
python -m pip install mpmath nbconvert
```

**macOS and Linux:** recent systems refuse `pip install` outside a virtual environment, so create one outside the repository and activate it in every new terminal:

```
python3 -m venv ~/.venvs/dirac16
source ~/.venvs/dirac16/bin/activate
python -m pip install -r requirements-stage3.txt
python -m pip install mpmath nbconvert
```

(Run the two `pip` lines from the repository root after Section 4.2, where the file `requirements-stage3.txt` is.) With other versions every check still passes, but the last digits of files that Python writes and the bytes of the figures can differ.

### 3.4 Checking the installation

```
git --version
rustc --version
cargo --version
python --version
python -c "import numpy, sympy, mpmath, matplotlib; print('OK')"
python -c "import nbformat, nbclient, nbconvert, ipykernel; print('OK')"
```

Each prints a version number or `OK`. A command-not-found message means that the tool is missing (Section 17).

## 4. Getting the code and the solver engine

### 4.1 Clone the repository

Choose a folder with a short path and no spaces (on Windows, for example, `C:\src`). Then, in PowerShell or bash:

```
git clone https://github.com/once-ere/Dirac_claude.git
cd Dirac_claude
```

The clone downloads about 300 MB (the repository history) and checks out about 700 MB of files; it took 34 s in the test of Section 2.3. Every later command runs in this folder, the repository root.

### 4.2 Fetch the solver engine

The Rust program is built on a pure-Rust port of SUNDIALS 7.8.0 (the CVODE solver), the rustSolveIt engine. It is not part of the repository; the setup script clones it, at a pinned commit, into the git-ignored folder `vendor/rustSolveIt`. The committed outputs were produced with the Windows 11 engine, and that engine also reproduces them byte for byte on Linux, so use it on every platform. PowerShell:

```
.\scripts\setup_solver.ps1 -Platform win11
```

bash:

```
bash scripts/setup_solver.sh win11
```

Expected output, at the end:

```
solver_platform=win11
solver_commit=a8fdff459adfe181573d7924b18bffbdf378fdb3
solver_setup=OK
```

Check the pin at any time with `git -C vendor/rustSolveIt rev-parse HEAD`, which must print the commit above. The engines for macOS and Linux (`-Platform macos` / `linux`) carry a different mathematical library: the program works with them, but its results then agree with the committed ones only to the solver tolerances, not byte for byte.

### 4.3 A map of the Stage-4 files

| path | content |
| --- | --- |
| `studies/dirac16complex_kohn_sham/` | the Rust solver (crate); `README.md` documents it, `src/` holds the modules (`shooting.rs`, `scf.rs`, `runs.rs`, `exchange.rs`, `emt.rs`, `blocks.rs`, `geometry.rs`, ...), `tools/` the determinism and summary tools |
| `scripts/ks_reference_solver.py` | the independent reference solver |
| `scripts/check_dirac16complex_kohn_sham.py` | the cross-checker |
| `scripts/check_dirac16complex_kohn_sham_theory.py` | the independent sympy theory checker |
| `wolfram/Dirac16ComplexKohnSham.wl`, `scripts/verify_dirac16complex_kohn_sham.wls` | the exact Wolfram theory and its verifier |
| `notebooks/dirac16complex_kohn_sham.ipynb` and `notebooks/build_dirac16complex_kohn_sham_notebook.py`, `notebooks/run_notebook.py`, `notebooks/check_dirac16complex_kohn_sham_notebook.py` | the Jupyter notebook, its builder, runner and auditor; `notebooks/dirac16complex_kohn_sham.PROVENANCE.md` documents it in detail |
| `notebooks/Dirac16ComplexKohnSham.nb` with `scripts/build_dirac16complex_ks_mathematica_notebook.wls` and `scripts/verify_dirac16complex_ks_mathematica_notebook.wls` | the Mathematica notebook, its builder and verifier |
| `artifacts/dirac16complex/kohn-sham/` | every output: the exact reports, `rust/`, `reference/`, the checker and notebook reports, `figures/` |
| `scripts/verify_stage4_kohn_sham.ps1`, `.sh`, `scripts/verify_stage4_kohn_sham_audit.py` | the Stage-4 gate |
| `handoff/specs/STAGE4_SPEC.md` | the binding specification with its errata E4.1 to E4.14 |

## 5. Building and testing the Rust program

### 5.1 Build

PowerShell or bash:

```
cd studies/dirac16complex_kohn_sham
cargo build --release
cd ../..
```

The first build compiles the engine and the program and takes between half a minute and a few minutes; it ends with

```
Finished `release` profile [optimized] target(s) in 36.06s
```

(the time is that of the test of Section 2.3). The program is `studies/dirac16complex_kohn_sham/target/release/dirac16complex_kohn_sham` (with `.exe` on Windows). **Run it from the repository root**: its default output folder `artifacts/dirac16complex/kohn-sham/rust` and the input files it reads are relative paths.

**The FMA note.** The repository's `.cargo/config.toml` tells the compiler to use the fused multiply-add instruction (`+fma`) of x86-64 processors. The committed outputs were produced that way; a build without it gives results that agree to the solver tolerances but not byte for byte. Cargo finds the file from any folder inside the repository.

### 5.2 Test

```
cd studies/dirac16complex_kohn_sham
cargo test --release
cargo clippy --release --all-targets -- -D warnings
cargo fmt --check
cd ../..
```

`cargo test` runs the unit tests of the crate: block reduction, geometry, exchange identities, the free box spectra against the analytic ones, Hellmann–Feynman identities, Anderson mixing, the free filling, determinism of a repeated solve, the energy-momentum tensor and the sign of the scalar charge, the theory and exchange-table cross-checks, and the tests of the Stage-5 extension that lives in the same crate. The expected summary line is given in Section 2.3 with its run time; some tests solve small self-consistent problems and take more than a minute each on a slow computer. `clippy` and `fmt --check` print nothing when the code is clean.

## 6. The physics you need, from zero

This section explains what the programs compute. It needs school algebra, derivatives and complex numbers; everything else is introduced here. The scientific document `provenance/DIRAC16COMPLEX_KOHN_SHAM_PRIMORDIAL` (called "the main document" below) gives the full derivations and every result; this section gives the ideas and the equations exactly as the programs use them.

### 6.1 Fermions, levels and the Pauli principle

A quantum field describes particles. dirac16complex is a **fermion** field: its particles obey the **Pauli principle**, so no two of them can be in the same single-particle state. A single-particle state is called a **level** (or an **orbital**); it has an energy $\varepsilon$. If $N$ fermions do not interact, the state of lowest total energy, the **ground state**, puts one particle into each of the $N$ lowest levels. This filling rule is called the **aufbau** (German for "building up"). The total energy is then the sum of the occupied level energies.

Levels often come in groups of equal energy (a **degenerate** group, or **shell**). If the $N$-th particle completes a shell, $N$ is a **closed shell**; then the next level up is empty and the energy needed to move one particle up, the **gap**, is the distance to the next shell. If $N$ ends inside a shell, the shell is **open**: the last particles can be spread over the degenerate levels in many ways at no cost.

The **first excited state** is the state of next-lowest energy. Without interaction it is obtained by moving one particle from the highest occupied level (**HOMO**) to the lowest empty level (**LUMO**); its excitation energy is the gap $\varepsilon_{\mathrm{LUMO}}-\varepsilon_{\mathrm{HOMO}}$.

When the particles interact, every particle feels all the others, and the levels themselves depend on how the others are distributed. That is the many-body problem; for more than a few particles it cannot be solved exactly.

### 6.2 Density-functional theory in one page

Density-functional theory (DFT) turns the many-body problem into a sequence of one-body problems. Its three ideas, with the names of their discoverers:

1. **Hohenberg and Kohn (1964).** The ground-state energy is a functional of the particle density alone: the density, a function of position, determines everything else.
2. **Kohn and Sham (1965).** Replace the interacting particles by fictitious *non-interacting* particles that move in an effective potential chosen so that they have the same density. That potential depends on the density, which depends on the levels in the potential: the equations must be solved **self-consistently**, by iteration. These are the **Kohn–Sham (KS) equations**, and their levels are the KS levels.
3. **The local-density approximation (LDA).** The part of the effective potential that is not simply the average (Hartree) potential of the other particles is called the exchange (and correlation) potential. The LDA takes it from the **uniform gas**: at each point it uses the value that an infinite, uniform gas of the same density would have.

**Mermin (1965)** extended DFT to a temperature $T>0$: one minimises the free energy $F=E-TS_{\mathrm{ent}}$ ($S_{\mathrm{ent}}$ is the entropy), and the levels are occupied with the Fermi–Dirac probabilities

$$
f(\varepsilon)=\frac{1}{e^{(\varepsilon-\mu)/T}+1},
$$

where the **chemical potential** $\mu$ is chosen so that the occupations add up to $N$. At $T=0$ this becomes the aufbau: $f=1$ below $\mu$, $f=0$ above.

**What is special here.** dirac16complex is a relativistic field with 16 complex components, and its interaction $U=\tfrac\lambda2S^2$ depends on the **scalar density** $S=\bar\Psi\Psi$, not only on the number density $n$. So two densities enter, $n$ and $S$. For this contact interaction the exchange energy of the uniform gas can be computed *exactly*, at every temperature (main document, Section 6.3):

$$
e_x(n,S)=-\frac{\lambda}{32}\bigl(n^2+S^2\bigr).
$$

No correlation term is added: in 8 dimensions the coupling $\lambda$ has the dimension $\mathrm{mass}^{-6}$, and the theory beyond this level is not renormalisable, so there is no meaningful correlation energy to add. The sign convention: $\lambda>0$ is repulsive, $\lambda<0$ attractive.

### 6.3 Why the thermodynamics of a fermion gas gives a pseudo-potential

Think of a uniform gas of dirac16complex particles with number density $n$ and scalar density $S$, at temperature $T$. Its energy per volume contains the direct (Hartree) interaction $\tfrac\lambda2S^2$ and the exchange energy $e_x(n,S)$ above. The derivative of an energy density with respect to a density is the energy that one more particle costs, which acts on that particle like a potential. Differentiating gives two potentials:

$$
v_s=\frac{\partial e_x}{\partial S}=-\frac{\lambda}{16}S\quad(\text{acts like a change of mass}),\qquad v_v=\frac{\partial e_x}{\partial n}=-\frac{\lambda}{16}n\quad(\text{acts like a shift of energy}).
$$

In the gravitational field the densities depend on the position $y$ (Section 6.4). The LDA uses these gas formulas at each point, with the local **proper** densities $n_p(y)$ and $S_p(y)$ (densities per proper volume, Section 6.6). The result is the pair of local potentials that every particle feels,

$$
M_{\mathrm{eff}}(y)=m+\lambda S_p(y)+v_s(y)=m+\tfrac{15}{16}\,\lambda S_p(y),\qquad v_x(y)=-\tfrac1{16}\,\lambda\,n_p(y).
$$

$M_{\mathrm{eff}}$ replaces the mass $m$ in the equation of a level, and $v_x$ is subtracted from its energy, $\varepsilon\to\varepsilon-v_x$. Because the pair is computed from the thermodynamics of the uniform fermion gas and then used as a potential for single particles, the project calls it the **Kohn–Sham fermion-gas thermodynamics pseudo-potential**. The temperature enters only through the densities. (A side remark for experts: the specification of Stage 4 had recommended a variant with a single potential; because $e_x$ depends exactly on both densities, the programs use both derivatives, which is what the minimisation of the energy gives. The main document, Section 6.4, records this.)

The total energy is not the sum of the KS level energies: that sum counts the interaction twice. The exact bookkeeping (main document, Section 6.5) is

$$
E=\sum_i\mathrm{mult}_i\,w_i\,\varepsilon_i-E_H-E_x,\qquad E_H=\frac\lambda2\int S_p^2\,dV_7,\qquad E_x=-\frac\lambda{32}\int\bigl(n_p^2+S_p^2\bigr)dV_7,
$$

with the weights $w_i$ of Section 6.7 and the proper volume element $dV_7=e^{6Hy}\ell^3dy$ of Section 6.6.

### 6.4 The primordial field in plain words

The field lives in eight dimensions $x_0,\dots,x_7$ (counted from 0): $x_0$ is a hidden space direction, $x_1,x_2,x_3$ are ordinary 3-space, $x_4$ is the time, and $x_5,x_6,x_7$ are three extra times. The author's notebook gives a gravitational field, the **primordial field**. Stage 4 uses its **static member**, in which a parameter $a_4$ is a constant ($a_4=0$ in the runs). With the hidden coordinate rewritten as $y=\ln(\sin 6Hx_0)/(6H)\le0$ the distances are

$$
ds^2=dy^2-dx_4^2+e^{2Hy}\bigl[e^{2a_4}(dx_1^2+dx_2^2+dx_3^2)-e^{-2a_4}(dx_5^2+dx_6^2+dx_7^2)\bigr].
$$

$H$ is a constant rate; the programs use units with $H=1$. The factor $e^{2Hy}$ shrinks 3-space and the extra times as $y$ decreases. Two places matter:

- the **brane** at $y=0$, where the notebook's coordinates end. Following the notebook's idea of a pair of universes, a mirror copy is glued on at $y=0$; then $y=0$ is a membrane (brane) between the two copies, and the particles collect near it;
- the **tip** at $y\to-\infty$, where the six warped directions shrink to nothing. It cannot be reached numerically, so the programs stop at $y=-L$ (the **tip cutoff**; $L=3$ in most runs, also 2 and 4).

The 3-space is made finite by making it periodic with period $\ell$ in each direction (a **torus**), so the momenta along 3-space are discrete: $\vec k=(2\pi/\ell)(n_1,n_2,n_3)$ with integers $n_i$. The programs choose $\ell$ so that the momentum step is $\Delta k=2\pi/\ell=0.25m$.

An important caveat for reading the results. After Stage 4 was specified, the author corrected the model on 2026-09-30: the three extra times deflate exponentially in time ("x5, x6, x7 are the three extra times that exponentially deflate"). The static member, with frozen extra times, is therefore not a model of the author's field; the author's field is treated anew in the folder `Revision/` (its Kohn–Sham record is `Revision/kohn_sham/`). This guide documents the Stage-4 computation as it was specified and completed, for the static member (main document, Section 12).

### 6.5 From 16 components to two: the reduced equation

The field has 16 complex components. For a level of energy $\varepsilon$ and 3-momentum $\vec k$, the programs write

$$
\Psi=e^{-i\varepsilon x_4}\,e^{i\vec k\cdot\vec x}\,e^{-3Hy}\,\chi(y).
$$

The factor $e^{-3Hy}$ removes the term that the curved space adds to the field equation (the spin connection) exactly. The spectrum depends only on $|\vec k|$, so the programs take $\vec k=(k,0,0)$. Then only three $16\times16$ matrices appear, and three further matrices that commute with them split the 16 components into **eight independent blocks of two components** (main document, Section 5.4). In each block the field equation becomes a pair of first-order differential equations in $y$:

$$
\chi'=\bigl[M_{\mathrm{eff}}(y)\,\sigma_3-\kappa(y)\,k\,\sigma_2+ij\,\bigl(\varepsilon-v_x(y)\bigr)\sigma_1\bigr]\chi,\qquad\kappa(y)=e^{-Hy-a_4},
$$

where $\chi=(\chi_1,\chi_2)$ has two components, the prime is $d/dy$, $\sigma_1,\sigma_2,\sigma_3$ are the Pauli matrices and $j=\pm1$ is the **block type**: four of the eight blocks have $j=+1$, four have $j=-1$. The momentum $k$ enters with the weight $\kappa(y)$, which grows toward the tip: moving along 3-space costs more energy far from the brane, so the particles are pushed toward $y=0$.

With $\chi=(a,\,ib)$ and real $a$, $b$ the equations are real. The programs label the block type by $s=-j$ (Section 6.7), and the equations they integrate are

$$
a'=M_{\mathrm{eff}}\,a+\bigl(s(\varepsilon-v_x)-\kappa k\bigr)\,b,\qquad b'=-\bigl(s(\varepsilon-v_x)+\kappa k\bigr)\,a-M_{\mathrm{eff}}\,b .
$$

The program prints exactly this system with `print-config` (Section 8.1). The $s=-1$ problem is the $s=+1$ problem with $\varepsilon\to-\varepsilon$ and $v_x\to-v_x$, so the levels of the two block types are mirror images when $v_x=0$.

### 6.6 Boundary conditions, normalisation and densities

A differential equation needs conditions at the ends:

- **At the brane** ($y=0$) the mirror construction allows two **parities**: the even parity $b(0)=0$ and the odd parity $a(0)=0$. Both are solved, and their levels are filled together as one system.
- **At the tip cutoff** ($y=-L$) the programs use the **bag condition** $b(-L)=0$.

These conditions make the current of particles through the ends vanish, which makes the problem well posed: the levels are real numbers, and different levels are orthogonal. A solution exists only for special values of $\varepsilon$, the levels.

A level is **normalised** by $\int_{-L}^0(a^2+b^2)\,dy=1$ (the curved-space volume factor cancels against $e^{-3Hy}$, so the ordinary measure $dy$ is the right one). Its contribution to the densities is, per unit coordinate 3-volume $\ell^3$:

$$
n_c(y)=\frac{a^2+b^2}{\ell^3},\qquad S_c(y)=\frac{-2s\,ab}{\ell^3}\quad(\text{coordinate densities}),\qquad n_p=e^{-6Hy}n_c,\quad S_p=e^{-6Hy}S_c\quad(\text{proper densities}).
$$

The coordinate density $n_c$ counts particles per unit $y$; the proper density $n_p$ counts particles per unit of real (proper) volume, which shrinks toward the tip like $e^{6Hy}$. The **proper volume element** is $dV_7=e^{6Hy}\ell^3dy$, so $\int n_p\,dV_7=N$.

### 6.7 The state layout, index by index

Every level found by the programs carries the following labels; they are the first columns of every `levels.csv` file (Section 9):

| label | column | meaning |
| --- | --- | --- |
| shell | `n2` | $n_1^2+n_2^2+n_3^2$; the momentum is $k=\Delta k\sqrt{n_2}$ |
| momentum | `k` | $k$ in units of $m$ |
| multiplicity | `multiplicity` | $4r_3(n_2)$: the number of states in this level |
| parity | `parity` | $+1$ even ($b(0)=0$), $-1$ odd ($a(0)=0$) |
| block type | `s` | the program label $s=\pm1$; the theory's $j$ is $-s$ |
| Prüfer index | `index` | an integer that numbers the levels of one $(n_2,\text{parity},s)$ (Section 7.1) |
| branch | `branch` | $+1$ particle state, $-1$ Dirac-sea state (Section 7.3) |
| occupation | `f` | the Fermi–Dirac or aufbau occupation |
| weight | `weight` | $w=f$ (particle) or $w=-(1-f)$ (sea) |

Here $r_3(n_2)$ is the number of integer vectors $(n_1,n_2,n_3)$ with $n_1^2+n_2^2+n_3^2=n_2$: $r_3=1,6,12,8,6,24,24,0,12,30,24,24,8,24,48,0,6$ for $n_2=0,\dots,16$ ($n_2=7$ and 15 are not sums of three squares). The factor 4 counts the four blocks of one type. At $k\ne0$ the two block types have different levels, so each level holds $4r_3$ states; at $k=0$ the two types coincide, and the programs list them as two rows of 4 states each.

**Example: the free spectrum and the closed shells.** For $m=H=1$, $L=3$ and $\lambda=0$ the lowest particle levels are (from `artifacts/dirac16complex/kohn-sham/rust/spectrum/free-spectrum-m1-L3.csv`):

```text
n2      k  parity   s  index        eps  multiplicity  cumulative  what
 0  0.000      +1  -1      0  0.0000000             4           4  zero modes
 0  0.000      +1  +1      0  0.0000000             4           8  zero modes
 1  0.250      +1  -1      0  0.4307337            24          32  brane band
 2  0.354      +1  -1      0  0.5879569            48          80  brane band
 3  0.433      +1  -1      0  0.7040996            32         112  brane band
 4  0.500      +1  -1      0  0.7996458            24         136  brane band
 ...
11  0.829      +1  -1      0  1.2471125            96         688  brane band
 0  0.000      -1  -1     -1  1.2922928             4         692  bulk level
 0  0.000      -1  +1      0  1.2922928             4         696  bulk level
12  0.866      +1  -1      0  1.2955254            32         728  brane band
13  0.901      +1  -1      0  1.3417057            96         824  brane band
14  0.935      +1  -1      0  1.3859192           192        1016  brane band
```

The **closed shells** are the values of `cumulative` at the end of a shell: $N=8$, 32, 80, 112, ..., 1016. The programs use $N=8$, 112 and 1016. The ground state of $N=112$ therefore holds the eight zero modes and the three band shells $n_2=1,2,3$; its HOMO is $0.7040996$, and its LUMO is the next shell, $0.7996458$, so its gap is $0.0955462$.

### 6.8 Exact solutions to test against

Three results can be derived with pencil and paper (main document, Section 5.7); you will use them in the exercises (Section 16) and the programs check against them.

1. **The zero modes.** For $k=0$, a constant mass $M$, $v_x=0$ and the even parity, $\chi=(e^{My},0)$ with $\varepsilon=0$ solves the equations and satisfies $b(0)=b(-L)=0$. It is concentrated at the brane: the fraction of it within $1/H$ of the brane is $(1-e^{-2M/H})/(1-e^{-2ML})$.
2. **The box levels.** For $k=0$, constant $M$ and $v_x=0$ the other even-parity levels are $\varepsilon=\pm\sqrt{M^2+(n\pi/L)^2}$, $n=1,2,\dots$, and the odd-parity levels solve $\tan(pL)=-p/M$ with $p^2=\varepsilon^2-M^2$.
3. **The brane band.** For small $k\ne0$ the zero modes move to $\varepsilon=\pm ck$ with

$$
c=e^{-a_4}\,\frac{2M}{2M-H}\,\frac{1-e^{-(2M-H)L}}{1-e^{-2ML}},
$$

which is $c=2/(1+e^{-3})=1.9051482536$ for $M=H=1$, $L=3$, $a_4=0$. The $+ck$ levels belong to $j=+1$ ($s=-1$).

## 7. How the computer solves it

### 7.1 Shooting, the Prüfer angle and root finding

**Shooting.** To find the levels of the two-component equation of Section 6.5 for one shell, parity and block type, the Rust program guesses an energy $\varepsilon$, starts at the tip with a vector that satisfies the tip condition $b(-L)=0$, integrates the equations to the brane $y=0$, and checks whether the brane condition holds there. If it does not, $\varepsilon$ is changed and the integration repeated, like aiming a cannon at a target.

**The Prüfer angle.** Instead of $a$ and $b$ the program follows the angle $\theta$ and the logarithm of the length $r$ of the vector $(a,-b)$: $a=r\cos\theta$, $b=-r\sin\theta$. The equations become

$$
\theta'=\bigl(\varepsilon-v_x\bigr)+\kappa k\cos2\theta-M_{\mathrm{eff}}\sin2\theta,\qquad(\ln r)'=M_{\mathrm{eff}}\cos2\theta+\kappa k\sin2\theta,
$$

with $\theta(-L)=0$, which is the tip condition $b(-L)=0$. This form has two advantages. The amplitude $r$, which can grow or shrink by many orders of magnitude, drops out of the angle equation. And because $\partial\theta'/\partial\varepsilon=1>0$, the end angle $\Theta(\varepsilon)=\theta(0;\varepsilon)$ grows strictly with $\varepsilon$. The even-parity levels are exactly the energies with $\Theta(\varepsilon)=n\pi$ ($b(0)=0$) and the odd-parity levels those with $\Theta(\varepsilon)=\pi/2+n\pi$ ($a(0)=0$), one level for every integer $n$. The integer $n$ is the **Prüfer index** of Section 6.7; a level cannot be missed, because every $n$ between the values of $\Theta$ at the two ends of an energy window gives exactly one level.

**Root finding.** For each target value the program brackets the root by doubling a step in $\varepsilon$ until $\Theta-\text{target}$ changes sign, and then refines it with the **Illinois method**, a regula falsi: draw the straight line through the two bracketing points, take its zero as the next guess, keep the bracket, and halve the stored function value at an end point that has been kept twice in a row, which prevents the slow one-sided convergence of the plain regula falsi. The result is checked by integrating the actual linear system once more: its matching residual at the brane, the number of sign changes of the profile and the Prüfer index must agree (columns `matching_residual`, `winding_residual`, `sign_changes`, `theta_residual` of `levels.csv`).

**CVODE.** Each integration in $y$ is done by CVODE, the variable-step, variable-order solver of the SUNDIALS suite, here in its pure-Rust port (the engine `vendor/rustSolveIt`). CVODE chooses its own step sizes to keep the local error below the tolerances $\mathrm{rtol}=10^{-12}$ (relative) and $\mathrm{atol}=10^{-14}$ (absolute), with a maximum step of $0.05$ in $y$; it uses the Adams method where the problem is not stiff and the BDF method where it is (large $\kappa k$ near the tip makes it stiff). The potentials $M_{\mathrm{eff}}(y)$ and $v_x(y)$ are known on a grid of 301 points and interpolated between them by natural cubic splines.

### 7.2 Profiles, normalisation and densities

When a level is found, the program integrates the linear system for $(a,b)$ once more together with the running integrals $\int(a^2+b^2)$, $\int(-2ab)$ and $\int(-\kappa k(a^2-b^2))$, and divides by $\sqrt{\int(a^2+b^2)}$ so that the level is normalised (Section 6.6). Whenever the amplitude leaves $[10^{-40},10^{40}]$ the solution is rescaled and CVODE restarted, so that nothing overflows. From the normalised levels it forms the coordinate densities $n_c$ and $S_c$ on the 301-point grid, weighted by multiplicity and weight (Section 7.3), and from them the proper densities and the potentials. Integrals over $y$ use the Simpson rule.

### 7.3 Filling the levels: branches, the aufbau, open shells and temperature

**Particles and the Dirac sea.** A relativistic field has negative-energy levels, the **Dirac sea**, which in the vacuum are all filled. The programs count every quantity relative to the free vacuum (normal ordering): a full sea contributes nothing, a particle level contributes its occupation $f$, and an empty sea level (a **hole**, which is an antiparticle) contributes $-(1-f)$. Each level is assigned to the particle or the sea branch by continuity from $\lambda=0$: it is a particle level if the level with the same shell, parity, block type and Prüfer index of the free problem has $\varepsilon\ge0$ (column `branch`, column `eps_free`). The interacting energy itself is not used for this: a repulsive interaction moves the zero modes slightly below zero, and they must stay particle levels.

**$T=0$.** The particle levels are filled in the order of $\varepsilon$ until $N$ particles are placed, and the sea stays full. If $N$ ends inside a degenerate level, that level is filled equally and fractionally (an ensemble of the degenerate configurations). The HOMO is the highest occupied particle level and the LUMO the lowest empty one.

**$T>0$.** Every level gets its Fermi–Dirac occupation, and the chemical potential is found by **bisection**: start with an interval of $\mu$ in which the net particle number $\sum\mathrm{mult}\cdot w$ is too small at one end and too large at the other, halve it, keep the half that contains $N$, and repeat until it is small enough. At high temperature many particle-antiparticle pairs are created thermally; the net number stays $N$. The energy window is extended upward until the neglected occupations are below $f_{\mathrm{cut}}=10^{-8}$.

### 7.4 Self-consistency and Anderson mixing

The KS loop is:

1. start from the free densities (or those of a related run);
2. build $M_{\mathrm{eff}}(y)$ and $v_x(y)$ from the densities (Section 6.3);
3. find all levels in these potentials (Section 7.1) and fill them (Section 7.3);
4. compute the new densities $n_c$, $S_c$;
5. stop if the new densities agree with the old ones to the tolerance $10^{-10}$ (relative to the largest density); otherwise mix them and go to step 2.

Taking the new densities directly as the next input often oscillates. **Anderson mixing** (also called Pulay mixing) remembers the last few inputs and outputs (here 6), finds the combination of them whose output-minus-input residual is smallest, and moves from it a fraction $\beta=0.4$ toward its output. The program stops a loop as stagnant if the residual has not improved by a factor 2 in 20 iterations. The histories of every run are in `history.csv`; without interaction the loop needs 3 iterations, with interaction 10 to 20, and 44 in the hardest case (Section 7.5).

### 7.5 When the aufbau fails: a level crossing at the Fermi level

For $N=1016$ with the attractive coupling $-\hat\lambda_2$ the exact $T=0$ loop does not converge. In the free state the HOMO is the 192-fold band shell at $\varepsilon=1.3859$, and an 8-fold $k=0$ level lies at $1.4480$. The attraction pulls the $k=0$ level down strongly (it has a large positive scalar density), and under self-consistency the two levels meet at the Fermi level. Then whichever of them is filled last, the new potential moves the *other* one below it: the occupations flip at every iteration (charge sloshing), and no mixing parameter cures this.

The program then defines the ground state as the self-consistent state connected to $\lambda=0$: it increases the coupling in four steps ($\lambda/4$, $\lambda/2$, $3\lambda/4$, $\lambda$), each started from the previous solution with gentler mixing ($\beta/4$), first with exact occupations and, where they slosh, with a small **occupation smearing**: Fermi–Dirac occupations with the width $10^{-3}m$ (then $10^{-2}m$ if needed), while the energy is still evaluated at $T=0$. With the smearing $10^{-3}m$ the loop converges. In the converged ensemble about 4.21 of the 192 band particles have moved into the $k=0$ level, which is then about half full ($f=0.527$; the band has $f=0.978$). This is not an open shell of the aufbau, which closes exactly at the band; it is the self-consistent ensemble of a degenerate crossing, and its gap and excitation energies refer to that ensemble (main document, Section 9.3). The file `run.json` records the path: `occupationSmearing` $0.001$, `zeroTemperatureFallbackStage` 1, `exactZeroTemperatureOccupations` false.

### 7.6 The first excited state: KS gap, particle-hole list and $\Delta$SCF

The programs report three estimates:

1. the **KS gap** $\varepsilon_{\mathrm{LUMO}}-\varepsilon_{\mathrm{HOMO}}$;
2. the **particle-hole list**: every pair (hole in an occupied level, particle in an empty level) with its energy difference, sorted. In a $T=0$ run a level counts as occupied (a possible hole) if $f>10^{-12}$ and as empty (a possible particle) if $f<1-10^{-12}$, so that the Fermi–Dirac tails of a smeared run do not count;
3. **$\Delta$SCF** ("delta self-consistent field"): keep the occupations of the ground state, identified by the level labels, move one particle from the HOMO level to the LUMO level, and solve the KS loop again with these fixed occupations; $\Delta\mathrm{SCF}=E_1-E_0$. It includes the relaxation of all the other levels.

Without interaction all three agree. With interaction they differ slightly; for $N=1016$ at $-\hat\lambda_2$ the list starts with the zero-energy rearrangement inside the half-filled $k=0$ level, then $3.69\times10^{-3}m$ from the band into that level, then the gap.

### 7.7 The independent reference solver: a matrix method

`scripts/ks_reference_solver.py` solves the same problem in a completely different way, so that an error in one program would show up as a disagreement. It puts the two components on a **staggered grid**: one component on the points $y_j=-L+jh$, the other halfway between them, $h=L/N_0$. The derivative then becomes a matrix of differences, and the levels are the eigenvalues of a real symmetric matrix, computed by numpy. This scheme has no spurious extra solutions (no "fermion doubling"). Its error decreases like $h^2$. To remove the error, every quantity is computed on three grids ($N_0$, $2N_0$, $4N_0$ points) and **extrapolated** (Richardson extrapolation): if $X(h)=X_0+c_2h^2+c_3h^3$, three values determine $X_0$. The canonical grids are $N_0=60$, 120, 240 (every coarse point is also a point of the Rust grid), and $N_0=120$, 240, 480 for $m=3$ and for the smeared run of Section 7.5. It has its own loop, mixing, filling and couplings.

### 7.8 Temperature, energy-momentum tensor and the coupling values

**Thermodynamics.** At $T>0$ the programs report the energy $E$, the entropy $S_{\mathrm{ent}}=-\sum\mathrm{mult}[f\ln f+(1-f)\ln(1-f)]$, the free energy $F=E-TS_{\mathrm{ent}}$ and the heat capacity $C_V=dE/dT$ at fixed $N$, computed by a central difference ($T\pm0.05T$) up to $T=0.3m$ and from the derivative of the occupations in a fixed spectrum at every $T$.

**Energy-momentum tensor.** From the levels the programs compute the energy density $\rho(y)$ and the pressures $p_y$ (hidden direction), $p_3$ (each 3-space direction) and $p_t$ (each extra time), their averages over the proper volume and the ratios $w=p/\rho$, and compare them with the source $\rho_{\mathrm{req}}=-21H^2/\kappa$ that Einstein gravity would need to produce the field (main document, Section 11).

**Couplings.** The interaction strength is set separately for each configuration $(m,L,N)$ (main document, Section 7.1): the program computes the free state, finds the largest value of $\max(\tfrac{15}{16}|S_p|,n_p/16)$ over $y$ (the size of the pseudo-potential per unit coupling), and sets $\hat\lambda_1=0.1/\text{that}$ and $\hat\lambda_2=1/\text{that}$, so that the pseudo-potential reaches $0.1m$ and $1m$ to first order. The labels `lamp1`, `lamm1`, `lamp2`, `lamm2` stand for $+\hat\lambda_1$, $-\hat\lambda_1$, $+\hat\lambda_2$, $-\hat\lambda_2$. The temperature series use one more value, the hot coupling `lamh`, $\hat\lambda_{\mathrm{hot}}=0.1/(\text{the same strength of the free state at }T=m)$, about $2.37\times10^{-5}$, so that the pseudo-potential stays near $0.1m$ even in the hot plasma (main document, Section 10.1).

## 8. Running the Rust program

### 8.1 The command line

```
dirac16complex_kohn_sham SUBCOMMAND [--output DIR] [--refined] [--quick] [--rtol X] [--atol X]
```

| subcommand | what it does |
| --- | --- |
| `print-config` | prints the configuration and the equations, checks nothing heavy, ends with `SUCCESS` |
| `spectrum` | the reduction, geometry and exchange checks, the free spectra, the closed shells and the couplings |
| `scf` | the 33 self-consistent ground states (main document, Section 7.6) |
| `excited` | the KS gaps, particle-hole lists and $\Delta$SCF energies |
| `thermo` | the finite-temperature series |
| `emt` | the energy-momentum tensor and the comparison with the required source |
| `all` | the five subcommands above, one after another |

Options: `--output DIR` writes into `DIR/<subcommand>/` instead of the committed folder (always use it for your own runs, so that the committed files stay untouched); `--refined` divides the CVODE tolerances by 10 and halves the maximum step; `--quick` runs a reduced matrix ($N\in\{8,112\}$, $\hat\lambda\in\{0,\hat\lambda_1\}$, $T\le0.3m$; for smoke tests, not the canonical files); `--rtol`, `--atol` override the tolerances. Every check prints `PASS - name: detail` or `FAIL - name: detail`, and the last line is `SUCCESS` or `FAILURE` (exit code 0 or 1).

### 8.2 print-config

PowerShell:

```
.\studies\dirac16complex_kohn_sham\target\release\dirac16complex_kohn_sham.exe print-config
```

bash (on Windows Git Bash add `.exe`):

```
./studies/dirac16complex_kohn_sham/target/release/dirac16complex_kohn_sham print-config
```

Expected output:

```text
study            = dirac16complex-kohn-sham
engine           = sundials_rs 7.8.0 CVODE (pure Rust, vendor/rustSolveIt)
fixture          = artifacts/dirac16complex/arbitrary-field/algebra-fixture.json
fixture sha256   = 8b4f15462ca4d61ef6ec0e72f04c8a77d23ce8bcabc9b6ce19f921c90e02653b
fixture source   = fixture
output root      = artifacts/dirac16complex/kohn-sham/rust
rtol override    = none
atol override    = none
refined          = false
quick            = false
geometry         = static primordial field, y = ln(sin z)/(6H) in [-L, 0], H = 1, Z2
                   brane at y = 0
reduction        = eight 2x2 blocks (s, c1, c2); real system a' = M a + (s eps - kappa k)
                   b, b' = -(s eps + kappa k) a - M b
boundary         = parity +/-: b(0) = 0 / a(0) = 0; bag: b(-L) = 0 (gamma^0 chi = +chi)
eigenvalues      = Pruefer shooting (CVODE), theta(0; eps) = n pi (+pi/2), bracket +
                   Illinois
exchange         = e_x = -lambda (n^2 + S^2)/32 (exact uniform gas, any T); v_s = -lambda
                   S/16, v_x = -lambda n/16
pseudo-potential = M_eff = m + (15/16) lambda S_p, eps -> eps - v_x(y); S_p, n_p proper
                   (e^{-6Hy})
occupations      = Fermi-Dirac, normal ordering (sea holes = antiparticles), mu by
                   bisection; window tail f_cut 1e-8
T = 0 fallback   = exact aufbau; a stagnant level crossing is re-solved by continuation
                   in lambda (lambda/4, ..., lambda), exact occupations first, then
                   occupation smearing 1e-3 m, 1e-2 m (recorded in run.json)
couplings        = per (m, L, N): lambda_hat_1 = 0.1/strength, lambda_hat_2 =
                   1.0/strength, strength = max_y max((15/16)|S_p|, n_p/16)/m^7 of the
                   free ground state
mixing           = Anderson (beta 0.4, history 6), tolerance 1e-10 on (n_c, S_c)
matrix           = L in {2,3,4}, m/H in {1,3}, Delta k = 0.25 m, a4_0 in {0, 0.5}, T/m in
                   {0, 0.1, 0.3, 1}
tolerances       = rtol 1e-12 atol 1e-14 max_step 0.05
threads          = 2
all              = spectrum, scf, excited, thermo, emt
SUCCESS
```

Long lines are wrapped here to the width of the page; the program prints each entry on one line. The line `threads` shows the number of worker threads, which is the number of processors of your computer (2 in the test of Section 2.3, which produced this output); the results do not depend on it. The line `reduction` is the real system of Section 6.5 (with $\varepsilon$ written for $\varepsilon-v_x$).

### 8.3 Your first runs

Write into a scratch folder outside the committed tree. bash:

```
B=./studies/dirac16complex_kohn_sham/target/release/dirac16complex_kohn_sham
$B spectrum --output build/my-runs
```

PowerShell:

```
$B = ".\studies\dirac16complex_kohn_sham\target\release\dirac16complex_kohn_sham.exe"
& $B spectrum --output build/my-runs
```

The run prints its 33 checks and ends with

```text
spectrum: solver_steps=39152872 rhs_evaluations=47587645 files=15 verdict=SUCCESS
SUCCESS
```

Compare the 15 files with the committed ones; every one must be identical. bash:

```
for f in $(ls artifacts/dirac16complex/kohn-sham/rust/spectrum); do
  cmp -s artifacts/dirac16complex/kohn-sham/rust/spectrum/$f build/my-runs/spectrum/$f \
    && echo "same $f" || echo "DIFFERENT $f"
done
```

PowerShell:

```
Get-ChildItem artifacts/dirac16complex/kohn-sham/rust/spectrum | ForEach-Object {
  $a = (Get-FileHash $_.FullName).Hash
  $b = (Get-FileHash "build/my-runs/spectrum/$($_.Name)").Hash
  if ($a -eq $b) { "same $($_.Name)" } else { "DIFFERENT $($_.Name)" } }
```

The quick matrix of all five subcommands is the next step (bash; in PowerShell use `& $B` as above):

```
$B all --quick --output build/my-quick
```

{{quickresult}}

### 8.4 The canonical runs and their run times

The canonical files were produced by `all` without `--quick`. That takes hours, mostly in `thermo`, whose hot runs ($T=m$) contain about 75000 levels. Measured wall times on the machine that produced the committed files (Intel Core Ultra 9 275HX, 24 cores, Windows 11; the subcommands running as concurrent processes, as the gate runs them):

{{walltimes}}

Run a single subcommand into a scratch folder with, for example, `$B scf --output build/my-runs`.

### 8.5 Determinism and tolerance convergence

A repeated run must give identical bytes, and a run with tighter tolerances must agree within tolerance. Produce a second complete tree with `all --output DIR2` and a refined tree with `all --refined --output DIR3`, then compare them with the committed tree:

```
python studies/dirac16complex_kohn_sham/tools/compare_runs.py --canonical artifacts/dirac16complex/kohn-sham/rust --repeat DIR2 --refined DIR3 --report build/my-determinism.json
```

The tool compares every file listed by the summaries byte for byte (repeat) and the energies (relative $10^{-7}$) and eigenvalues (absolute $10^{-7}$) of every run (refined), prints `check_<name>=true|false` and exits with code 1 on any failure. The committed report is `artifacts/dirac16complex/kohn-sham/rust/determinism-report.json` (main document, Section 13.2).

## 9. Reading the output files

### 9.1 The file format

Every CSV file starts with a header line of column names, separated by commas; every number is written with 17 significant digits in exponential form (for example `4.30733678637911455e-01`), lines end with LF, and there are no timings or absolute paths, so that a repeated run gives identical bytes. JSON files use 2-space indentation and a fixed key order. The canonical tree is `artifacts/dirac16complex/kohn-sham/rust/`, with one folder per subcommand; a run label such as `m1_L3_N112_lamp1_T0` is decoded in Section 2.1. Energies, momenta and temperatures are in units of $H=1$, which equals $m$ for the $m=1$ runs; for the $m=3$ runs they are in units of $H=m/3$.

### 9.2 The spectrum folder (15 files)

| file | content |
| --- | --- |
| `reduction.json` | the block labels and the defects of the numerical block reduction (all at round-off) |
| `geometry.json` | curvature, Einstein tensor, required source, extrinsic curvature and brane stress, re-derived numerically |
| `exchange-check.json` | the exchange kernel, closed form and filled-shell identities, with their defects |
| `exchange-table-check.json` | the comparison with the exchange table of the sympy checker |
| `theory-agreement.json` | the comparison with the exact theory file, including the block-label relation |
| `uniform-gas-table.csv` | the uniform gas at $T/m=0$, 0.1, 0.3, 1 and five target densities $10^{-4}$ to 1 each (the program's own quadrature; at the lowest temperatures its fixed rule does not resolve the Fermi edge, so `n` differs from `n_target`): columns `T`, `n_target`, `mu`, `n`, `S`, `energy_density`, `pressure`, `e_x_over_lambda` |
| `free-spectrum-m1-L2.csv` ... `free-spectrum-m3-L4.csv` | the free levels for $m=1,3$ and $L=2,3,4$ with $|\varepsilon|<4m$ on the shells $n_2\le16$, in the 17 columns of Section 9.3 |
| `closed-shells-m1-L3.csv`, `closed-shells-m3-L3.csv` | the closed shells: columns `N` and `eps_homo` |
| `summary.json` | the verdict, the 33 checks, the closed shells and the couplings of every configuration |

### 9.3 Per-run files of scf, thermo and emt

Each run folder (for example `rust/scf/m1_L3_N112_lamp1_T0/`) holds four files.

**`levels.csv`**, one row per level (17 columns):

| column | meaning |
| --- | --- |
| `n2`, `k` | shell and momentum, $k=\Delta k\sqrt{n_2}$ |
| `multiplicity` | number of states, $4r_3(n_2)$ |
| `parity` | brane parity, $+1$ or $-1$ |
| `s` | program block type ($j=-s$) |
| `index` | Prüfer index |
| `eps` | the level energy $\varepsilon$ |
| `branch` | $+1$ particle, $-1$ sea ($0$ in the free-spectrum files, which are not filled) |
| `eps_free` | the energy of the same level at $\lambda=0$ (defines the branch) |
| `f`, `weight` | occupation $f$ and weight $w$ (Section 7.3) |
| `scalar_charge` | $\int(-2s\,ab)\,dy$ of the normalised level |
| `pressure_charge` | $\int(-s\kappa k(a^2-b^2))\,dy$ |
| `matching_residual`, `winding_residual`, `sign_changes`, `theta_residual` | quality of the level: brane condition of the linear solution, node count and Prüfer angle |

**`profiles.csv`**, one row per grid point $y_i=-L+iL/300$ (301 rows, 17 columns): `y`; `z` $=\arcsin e^{6Hy}$ (the notebook's hidden coordinate, $\pi/2$ at the brane); `n_c`, `n_p`, `S_c`, `S_p` (coordinate and proper densities); `M_eff`, `v_x` (the pseudo-potential); `L_s` (the interaction density $\tfrac\lambda2S_p^2+e_x$); `rho`, `p_y`, `p_3`, `p_t` (energy density and pressures); `conservation_residual` (the local residual of $p_y'+6Hp_y-3Hp_3-3Hp_t=0$); `homo_a`, `homo_b` (the normalised HOMO level); `volume_factor` $=e^{6Hy}$.

**`history.csv`**, one row per SCF iteration: `iteration`, `residual_n`, `residual_S` (the relative density changes), `mu`, `E`, `F`, `states` (levels found), `integrations` (CVODE integrations).

**`run.json`**: the parameters (`parameters`: $H$, $m$, $a_{4,0}$, $L$, grid points, $\Delta k$, $\ell$, $\hat\lambda$, $\lambda$, $T$, the occupation smearing, $N$, $f_{\mathrm{cut}}$, mixing, tolerances, the fallback stage), convergence (`converged`, `iterations`, `finalResidualN`, `finalResidualS`), the filling (`mu`, `epsHomo`, `epsLumo`, `ksGap`, `seaTop`, `particleBottom`, `branchOverlap`, `nTotal`, `nFromDensity`), the energies (`ksSum` $=\sum\mathrm{mult}\,w\varepsilon$, `hartreeEnergy`, `exchangeEnergy`, `energy` $=E$, `entropy`, `freeEnergy`, `grandPotential`, `scalarTotal` $=\int S_p\,dV_7$), the size of the pseudo-potential (`maxLambdaSOverM`, `maxVxOverM`), the window and solver statistics, and the block `emt` (Section 9.6).

**`summary.json`** of each subcommand: `verdict` (`SUCCESS` or `FAILURE`), `checks` (name: true/false), `runs` (one record per run with the numbers of its `run.json`), `files` (every file written, which is exactly what the determinism check compares), `solverTotals` and the reference couplings.

### 9.4 The excited folder

Per run: `levels.csv` (the ground state, as in Section 9.3), `levels-excited.csv` (the $\Delta$SCF state, same columns) and `particle-hole.csv` (columns `excitation`, `eps_hole`, `eps_particle`, `k_hole`, `k_particle`, sorted by excitation energy). The table `excitations.csv` has one row per run of the $m=1$, $L=3$ matrix: `N`, `lambda_hat`, `E0`, `mu`, `ks_gap`, `delta_scf`, `E1`, `max_lambda_S_over_m`. The 601-point run `m1_L3_N1016_lamm2_T0_g601` is in the summary but not in `excitations.csv`.

### 9.5 The thermo folder

Per run as in Section 9.3; there `levels.csv` is the excitation spectrum at that $T$ (column `f` the Fermi–Dirac occupation). The table `thermodynamics.csv` has one row per run (23 columns): `series` (0 `lam0`, 1 `lamp1`, 2 `lamh`), `N`, `lambda_hat`, `T`, `mu`, `E`, `F`, `S_entropy`, `C_V` (the reported heat capacity), `C_V_fd` (central difference, `nan` where not computed), `C_V_fixed_spectrum` and `C_V_fixed_spectrum_entropy` (the two fixed-spectrum forms), `dmu_dT_fixed_spectrum`, `ks_gap`, `states`, `shells`, `w_y`, `w_3`, `brane_fraction`, `occupation_smearing`, `max_lambda_S_over_m`, `max_v_x_over_m`, `iterations`.

### 9.6 The emt folder

Per run as in Section 9.3. The `emt` block of `run.json` and the table `emt-summary.csv` (30 columns: `N`, `lambda_hat`, `T`, `rho_avg`, `p_y_avg`, `p_3_avg`, `p_t_avg`, `w_y`, `w_3`, `w_t`, `brane_fraction`, `tip_fraction`, `E`, `E_from_rho`, `conservation_residual`, `rho_required_kappa1`, `kappa_needed`, `rho_max`, `rho_min`, `S_p_avg`, `n_p_avg`, `S_p_min`, `S_p_max`, `lambda_S_avg_over_m`, `kappa_mass_condition`, `kappa_coupling_condition`, `sourcing_conditions_met`, `lambda_hat_needed_first_order`, `rho_sign`, `sourcing_three_conditions_met`) hold the proper-volume averages, the equations of state, the fractions of the particles within $1/H$ of the brane and of the tip cutoff, the check $\int\rho\,dV_7=E$, and the comparison with the required source and with the sourcing conditions of erratum E4.1.

### 9.7 The reference solver's files

`artifacts/dirac16complex/kohn-sham/reference/` holds `reference-summary.json` (56 runs, the method, the conventions, the couplings, `complete`) and one folder per run with `spectrum.csv` (columns `q` $=n_2$, `r3`, `k`, `parity`, `type` (the block type), `index`, `branch`, `mult`, `f`, `w`, `eps_level0`, `eps_level1`, `eps_level2` (the three grids), `eps_extrapolated`, `interpolated` (1 for a level from the Chebyshev tail)), `profiles.csv` (`y`, `z`, `W6` $=e^{6Hy}$, `n_c`, `S_c`, `n_p`, `S_p`, `M_eff`, `v_x`, `rho`, `p_y`, `p_3`, `p_t`, `L_s` on the coarse grid, extrapolated), `scf-history-level0.csv` to `level2.csv` (one per grid) and `run.json` (parameters, extrapolated energies, order estimates, gap, particle-hole list, $\Delta$SCF, energy-momentum averages).

## 10. The exact theory and its two verifiers

The exact theory (main document, Sections 4 to 6) is derived twice, independently.

**The Wolfram verifier** (needs WolframScript). It loads `wolfram/Dirac16ComplexKohnSham.wl`, proves 125 statements exactly (geometry and brane, the reduction to the $2\times2$ blocks with the explicit basis, the current matrices and boundary conditions, the exchange identities, the functional derivatives of the Mermin functional and the reduction of the energy-momentum tensor) and writes the report and the theory file `kohn-sham-theory.json` with every explicit matrix. WolframScript 1.14 drops every argument that follows `--`, so the report path is given directly:

```
wolframscript -file scripts/verify_dirac16complex_kohn_sham.wls build/my-theory/wolfram-kohn-sham-report.json
```

It prints one line `check_<name>=true` per check and one `measurement_<name>=...` per measurement, then `check_count=125`, `failed_check_count=0`, the elapsed time and the paths of the report and the theory file (tens of seconds; 45 s and 10 s were measured in two gate runs on the 24-core computer). The theory file is written next to the report; compare it with the committed one: `git diff --no-index --stat artifacts/dirac16complex/kohn-sham/kohn-sham-theory.json build/my-theory/kohn-sham-theory.json` prints nothing when they are identical.

**The independent sympy checker** derives the same theory with sympy and numpy only, compares 20 of its results with the Wolfram theory file and builds the exchange table (Section 6.3 of the main document):

```
python scripts/check_dirac16complex_kohn_sham_theory.py --output build/my-theory/python-theory-report.json --table build/my-theory/exchange-table.json
```

It prints `check_count=157` and `failed_check_count=0` and the time spent per family of checks; building the exchange table takes most of the time (167.5 s of 219.7 s in the test of Section 2.3, on a loaded two-core computer; the gate header records 171 s and 50 s for the whole checker on the 24-core computer under different loads). On the computer that produced the committed files (Windows, Python 3.14.5, numpy 2.4.6) the report and the table are reproduced byte for byte. With other versions of Python and numpy (Python 3.13 with numpy 2.5.3 in the Linux test) all 157 checks pass and the two files differ only in round-off: one recorded maximum deviation ($7.8\times10^{-15}$ instead of $5.1\times10^{-15}$) and the last digits of the quadrature error estimates of the table. The gate accepts such files value by value (relative $10^{-9}$, absolute $10^{-12}$) and logs which rule matched.

Without the options `--output` and `--table` the checker overwrites the committed files `artifacts/dirac16complex/kohn-sham/python-theory-report.json` and `exchange-table.json`; restore them with `git checkout -- artifacts` if you did that by accident.

## 11. The reference solver and the cross-check

### 11.1 The reference solver

The complete canonical reference run (every run of `reference-summary.json` on its three grids) takes several hours with 8 to 12 worker processes; one run alone, the smeared $N=1016$ run on the grids 120/240/480, took 4.5 hours on the 24-core computer (16179.7 s measured on 2026-09-30, {{r1time}} measured on 2026-10-18). Its quick mode runs the self-tests and four small runs on coarse grids in about a minute:

```
python scripts/ks_reference_solver.py --quick --output build/my-reference-quick
```

It first prints its self-tests (in the test of Section 2.3: `analytic k = 0 spectra: max error 2.181e-07`), the closed shells (`N_mid = 112, N_big = 1016, N_mid(m = 3) = 112`) and its own coupling for $(m,L,N)=(1,3,8)$, then the iterations of the four quick runs (`m1_L3_N8_lam0_T0`, `m1_L3_N8_lamp1_T0`, `m1_L3_N8_lam0_T0p3` and the single-parity run `L2-free-N8-p-1`), and ends with a line of the form

```text
wrote build/my-reference-quick/reference-summary.json in 66.3 s (4 runs, failed: [])
```

The quick grids are coarse ($N_0=30$, 60), so its numbers agree with the canonical ones only to a few digits (for example the KS gap of $N=8$, $0.4307405$ on the quick grids against $0.4307337$); the quick mode tests the program, not the results. The gate checks that the quick summary is complete, that the self-tests are present and that every run converged.

The options: `--output DIR` (default: the committed folder `artifacts/dirac16complex/kohn-sham/reference`, which you should not overwrite), `--quick`, `--runs NAME,...` (only the named runs), `--workers W` (parallel processes; default half the processors, at most 12), `--resume` (keep the runs already in the output folder and recompute only missing or outdated ones), `--skip-self-tests`, and `--config FILE` (one run from a JSON parameter file; this is how the smeared run was recomputed).

### 11.2 The cross-checker

`scripts/check_dirac16complex_kohn_sham.py` compares the reference and the Rust trees run by run, with tolerances stated once in the program (the reference eigenvalues are good to about $10^{-7}m$ after extrapolation, the Rust eigenvalues to about $10^{-9}m$; where a Rust run has a 601-point partner, the measured grid change of each level is added to its tolerance, erratum E4.14). It also checks many identities of each tree: particle-number conservation, energy from the energy density, the energy-momentum conservation, current-free ends, the Hellmann–Feynman stationarity of the functional by small self-consistent reference runs, and it re-solves one Rust parameter set with exactly the Rust coupling. With the repeat and refined trees of Section 8.5 it also checks determinism. Full form, as for the committed report:

```
python scripts/check_dirac16complex_kohn_sham.py --repeat DIR2 --refined DIR3 --report build/my-check-report.json
```

Without `--repeat` and `--refined` those two comparisons are recorded as not run. The program prints `check_<name>=true|false` lines, `check_count` and `failed_check_count`, and exits with code 1 if any check fails. The committed report `artifacts/dirac16complex/kohn-sham/python-check-report.json` {{checkerresult}}

### 11.3 The summary file

`studies/dirac16complex_kohn_sham/tools/build_kohn_sham_summary.py` copies (never recomputes) every check count and the key physics numbers from the committed reports into one file, and refuses inputs that are stale (a report whose recorded input hashes do not match the files):

```
python studies/dirac16complex_kohn_sham/tools/build_kohn_sham_summary.py --output build/my-summary.json
```

The output must be identical to the committed `artifacts/dirac16complex/kohn-sham/kohn-sham-summary.json` ({{summaryresult}}).

## 12. The Jupyter notebook

### 12.1 What it is

`notebooks/dirac16complex_kohn_sham.ipynb` is the numerical documentation in executable form: markdown explanations, a driver cell that finds the Rust program and runs `print-config` and `spectrum` (into the scratch folder `build/notebook-kohn-sham`), cells that read every committed output, recompute key quantities independently (the box spectrum, the zero mode and the band slope, particle numbers, energies, the exchange formula, the gaps, the energy-momentum averages), compare the Rust and reference trees with the cross-checker's own comparison function, draw the 14 figures of the main document into `artifacts/dirac16complex/kohn-sham/figures/`, and end with a **gauntlet** of 60 checks. It is generated by `notebooks/build_dirac16complex_kohn_sham_notebook.py`; never edit it by hand. Its own provenance file, `notebooks/dirac16complex_kohn_sham.PROVENANCE.md`, documents every input and output, every run of its verification and a table of failure messages; read it for anything this section leaves out.

### 12.2 Running it headless

Three executors are available; each takes one to two minutes (most of it the `spectrum` re-run). **Route A**, Jupyter's executor, writes an executed copy and leaves the committed notebook untouched (recommended for a first run):

```
python -m nbconvert --to notebook --execute notebooks/dirac16complex_kohn_sham.ipynb --output-dir build/nbconvert
```

**Route B**, the repository's runner (standard library only; it writes the executed notebook back in place, and only if every cell succeeds):

```
python notebooks/run_notebook.py notebooks/dirac16complex_kohn_sham.ipynb
```

**The audit** checks an executed notebook (structure, no error outputs, the gauntlet passed, every figure present with the hash it printed, the cells equal to the builder's output) and can compare two executed copies:

```
python notebooks/check_dirac16complex_kohn_sham_notebook.py notebooks/dirac16complex_kohn_sham.ipynb --also build/nbconvert/dirac16complex_kohn_sham.ipynb --report build/my-notebook-report.json
```

{{notebookresult}}

Every route rewrites the 14 figures. On Windows with the pinned packages 13 of them are rewritten with identical bytes and only the figure that compares the two solvers changes when its inputs change; on Linux all 14 PNG files get other bytes (the same pixels, compressed by a different zlib). Restore the committed figures with `git checkout -- artifacts/dirac16complex/kohn-sham/figures`.

### 12.3 Interactively

`python -m jupyterlab notebooks/dirac16complex_kohn_sham.ipynb` opens it in your browser (needs `python -m pip install jupyterlab`); choose the kernel Python 3 (ipykernel) and Run, Run All Cells. JupyterLab saves the notebook automatically, so restore it afterwards with `git checkout -- notebooks/dirac16complex_kohn_sham.ipynb`.

## 13. The Mathematica notebook (optional)

`notebooks/Dirac16ComplexKohnSham.nb` is generated by `scripts/build_dirac16complex_ks_mathematica_notebook.wls` and evaluated headless by its verifier, which writes `artifacts/dirac16complex/kohn-sham/mathematica-report.json` and the six figures of `artifacts/dirac16complex/kohn-sham/figures/mathematica/`. It derives the reduced equations symbolically, solves the $k=0$ box exactly, shoots the free spectra with `NDSolve` (2818 levels compared with the Rust files), runs its own small self-consistent loop in Wolfram Language for $N=8$ at $+\hat\lambda_2$ and compares it with the Rust run, and runs the Rust program (`print-config`) to check its printed equations. It needs WolframScript and the built Rust program:

```
wolframscript -file scripts/verify_dirac16complex_ks_mathematica_notebook.wls
```

It prints `check_count=94`, `failed_check_count=0`, the numbers of evaluated cells, failed evaluations and messages, and finally `dirac16complex_ks_mathematica_notebook=OK`; the report records 94 of 94 checks true and the verdict `SUCCESS` (main document, Section 13.3). The verifier rewrites the committed report and figures; on the computer that produced them the figures are rewritten byte for byte, and the report differs only in the platform-specific path of the Rust binary (`engine.binary`). Without WolframScript skip this section: the gate then skips the two Wolfram steps and says so.

## 14. The Stage-4 gate

The gate reruns and compares everything that can be rerun in a few hours and ends with `stage4_kohn_sham_verification=OK`. PowerShell 7:

```
pwsh -NoProfile -File scripts/verify_stage4_kohn_sham.ps1
```

bash:

```
bash scripts/verify_stage4_kohn_sham.sh
```

Its 37 steps (`stage4-00` to `stage4-36`) are listed, with the measured wall time of each, in the header of the PowerShell script; `-DryRun` (PowerShell) or `--dry-run` (bash) prints them without running anything, and `-Steps 03,04` / `--steps 03,04` runs a selection (the last line is then `PARTIAL`, never `OK`). In short, the gate:

1. copies the committed Stage-4 files aside (step 00), sets up and checks the engine (01, 02);
2. reruns the exact theory (Wolfram, if available, and sympy) and requires identical files (03 to 05), regenerates the Rust constants (06 to 08);
3. runs `cargo fmt --check`, `clippy`, `test` and `build` (09 to 12) and `print-config` (13);
4. reruns **every** Rust subcommand into `build/stage4/run-a` and the refined spectrum, scf, excited and emt into `build/stage4/refined`, as concurrent processes (14), requires every file listed by the committed summaries to be byte-identical (15) and checks determinism and tolerance convergence (16, 17);
5. runs the reference solver's quick mode (18, 19) and the full cross-checker against the fresh trees (20, 21);
6. rebuilds the summary file and requires identical bytes (22, 23);
7. executes the Jupyter notebook by both executors, audits it and requires the figures to be rewritten byte for byte (24 to 29), evaluates the Mathematica notebook if WolframScript is available (30, 31);
8. rebuilds both PDFs in verify mode (32, 33), requires every committed file to be unchanged (34), runs the unit tests `python -m unittest discover -s tests -p "test_d16c_kohn_sham*.py" -v` (35) and checks that its outputs are fresh (36).

What it does **not** rerun is the canonical reference solver run (hours with many processes); the committed reference tree is compared with the fresh Rust tree instead. The gate takes {{gatetime}} on the 24-core computer, almost all of it in step 14 (the `thermo` subcommand). It stops at the first failing step and prints `stage4_failed_step`, the log file and `stage4_kohn_sham_verification=FAILED`. Never run two gates at once: both would rewrite `build/stage4`.

## 15. Rebuilding the PDF documents (optional)

The documents are written in Markdown and converted to LaTeX and PDF by one command each (needs pdflatex; both use the developer layout of the builder, with breakable code and ragged table columns):

```
python scripts/build_provenance_pdf.py --developer-layout provenance/DIRAC16COMPLEX_KOHN_SHAM_PRIMORDIAL.md
python scripts/build_provenance_pdf.py --developer-layout provenance/DIRAC16COMPLEX_KOHN_SHAM_STUDENT_GUIDE.md
```

The builder writes the `.tex` twice with different hash seeds and requires identical bytes, runs pdflatex three times in two fresh folders, requires a warning-free log and two byte-identical PDFs, and in this verify mode compares page count and SHA-256 with the edition registered in `provenance/pdf-specifications.json`. The registered PDFs were built with MiKTeX on Windows; another TeX distribution produces a PDF with the same text and other bytes, so there the registry checks report false while every other check passes.

## 16. Exercises with answers

Each exercise can be done with a pocket calculator or a few lines of Python; the answers quote the committed files, so you can check yourself.

**Exercise 16.1 (the box levels at $\lambda=0$).** For $k=0$, $M=m=1$, $L=3$ and $v_x=0$ predict the first two even-parity levels and the first odd-parity level (Section 6.8), and find them in `artifacts/dirac16complex/kohn-sham/rust/spectrum/free-spectrum-m1-L3.csv` (rows with `n2` $=0$).

*Answer.* Even parity: $\sqrt{1+(\pi/3)^2}=1.4479719$ and $\sqrt{1+(2\pi/3)^2}=2.3208815$. Odd parity: the smallest root of $\tan(3p)=-p$ is $p=0.8185480$, so $\varepsilon=\sqrt{1+p^2}=1.2922928$. The file has $1.44797193040558$, $2.32088148017552$ and $1.29229282806805$; the root can be found by bisection:

```python
import math
lo, hi = 0.6, 1.0
g = lambda p: math.tan(3 * p) + p
for _ in range(100):
    mid = (lo + hi) / 2
    lo, hi = (lo, mid) if g(lo) * g(mid) <= 0 else (mid, hi)
print(math.sqrt(1 + mid * mid))   # 1.2922928280685...
```

**Exercise 16.2 (the brane band).** Compute the slope $c$ for $M=H=1$, $L=3$, $a_4=0$ and the linear estimate $c\,\Delta k$ of the first band level. Why is the computed level $0.4307337$ lower?

*Answer.* $c=2/(1+e^{-3})=1.9051483$ and $c\cdot0.25=0.4763$. The band $\varepsilon=ck+O(k^2)$ bends down at larger $k$: the $O(k^2)$ term is negative here. (The Rust program measures the slope $-1.9051482525$ for its $s=+1$ blocks near $k=0$, the theory's $-c$ for $j=-1$, and the Mathematica notebook finds the closed form to $1.6\times10^{-7}$ with its own shooting; main document, Section 5.7.)

**Exercise 16.3 (closed shells).** Using only the multiplicities $4r_3(n_2)$ of Section 6.7 and the fact that the lowest particle levels are the zero modes and then the band shells $n_2=1,2,3,\dots$ in order, predict the first four closed shells. Which closed shell first contains a level that is not on the brane band?

*Answer.* $8$, $8+24=32$, $32+48=80$, $80+32=112$. The first bulk level, the $k=0$ odd-parity level at $1.2922928$, completes $N=696$ (Section 6.7 table). Check with `closed-shells-m1-L3.csv`.

**Exercise 16.4 (brane localisation).** What fraction of the $N=8$ zero modes lies within $1/H$ of the brane for $L=2$, 3 and 4? Compare with the column `brane_fraction` of the $\lambda=0$, $N=8$ runs (or `run.json`, key `emt.braneFraction_within_1_over_H`).

*Answer.* $(1-e^{-2})/(1-e^{-2L})=0.8808$, $0.8668$, $0.8650$ for $L=2,3,4$; the runs give $0.8807971$, $0.8668133$ and $0.8649564$.

**Exercise 16.5 (changing $T$: the chemical potential).** At $T=0.1m$ the $N=8$, $\lambda=0$ state has $\mu=0.1304195$. Model it with the zero modes (8 states at 0), the first band shell (24 states at $0.4307337$) and its mirror sea level (24 states at $-0.4307337$, whose holes count $-(1-f)$), and find $\mu$ by bisection on $N=8$. Then add the next two band shells and their mirrors (48 states at $\pm0.5879569$, 32 at $\pm0.7040996$).

*Answer.* The three-level model gives $\mu=0.1564$, the seven-level model $0.1340$, the full calculation $0.1304$: thermal excitation reaches several shells already at $T=0.1m$, which is why the program keeps every level with $f>10^{-8}$.

**Exercise 16.6 (changing $N$).** Without running anything, predict the KS gap of the free $N=32$ state and of the free $N=80$ state.

*Answer.* For $N=32$ the HOMO is the shell $n_2=1$ ($0.4307337$) and the LUMO $n_2=2$ ($0.5879569$): gap $0.1572232$. For $N=80$: $0.7040996-0.5879569=0.1161427$. (This is also the finite-temperature KS gap of $N=112$ at $T=0.1m$ in `thermodynamics.csv`, where the shell $n_2=3$ has dropped below half filling.)

**Exercise 16.7 ($m=3$: a constant shift).** For $M=3H$ the zero mode $(e^{My},0)$ has the proper density $e^{(2M-6H)y}$, a constant. Show that the exchange potential is then a constant $v_x$, that the zero modes sit at $\varepsilon=v_x$, and that $E_0=Nv_x/2$. Check with `rust/scf/m3_L3_N8_lamp1_T0/run.json`.

*Answer.* With $S_p=0$ only $v_x=-\lambda n_p/16$ acts; a constant shift moves the zero mode to $\varepsilon=v_x$ without changing it, and $E=N v_x-E_x$ with $E_x=\tfrac12\int v_xn_p\,dV_7=Nv_x/2$. The file has $\mu=\varepsilon_{\mathrm{HOMO}}=-0.3$ (in units of $H$; $v_x=-0.1m$) and $E_0=-1.2=8\times(-0.3)/2$.

**Exercise 16.8 (attraction against repulsion for $N=8$).** The $N=8$ energies are $E_0=-0.000986833163$ at $+\hat\lambda_1$ and $+0.000986833163$ at $-\hat\lambda_1$. Explain the exact antisymmetry.

*Answer.* Changing the sign of $\lambda$, of $v_x$ and of $S_p$ and exchanging the two block types maps the KS equations onto themselves with every level negated ($h_{-j}(M,-v)=-h_j(M,v)$); for $N=8$ the eight occupied zero modes map onto themselves, and every term of $E=\sum f\varepsilon-E_H-E_x$ changes sign (main document, Section 8.4).

**Exercise 16.9 (first-order interaction energy).** The first-order change of the ground-state energy is $\hat\lambda\int\bigl(\tfrac{15}{32}S_p^2-\tfrac1{32}n_p^2\bigr)dV_7$ on the free state. Evaluate it with the Simpson rule from `rust/scf/m1_L3_N112_lam0_T0/profiles.csv` (columns `y`, `n_p`, `S_p`; $dV_7=e^{6y}\ell^3dy$, $\ell^3=(8\pi)^3$) and compare with the self-consistent $E_0(+\hat\lambda_1)-E_0(0)$.

*Answer.* $dE_0/d\hat\lambda=2.3321$, so the first-order shift at $\hat\lambda_1=9.5678\times10^{-3}$ is $0.022313$; the self-consistent shift is $61.113212-61.090723=0.022489$, 0.8 % larger.

**Exercise 16.10 (tolerances).** Run `spectrum --refined` into a scratch folder (Section 8.3) and compare the free levels with the committed ones. How large are the differences?

*Answer.* The refined run tightens the CVODE tolerances by a factor 10 and halves the maximum step; the committed determinism report records that over all 65 runs of the refined tree the eigenvalues change by at most $2.8\times10^{-8}$ (Section 8.5), so the free levels agree far below the printed 7 decimals.

## 17. Troubleshooting

| what you see | cause | what to do |
| --- | --- | --- |
| `git`, `cargo` or `python` "is not recognized" / "command not found" | the tool is missing, or the terminal was opened before it was installed | open a new terminal; install the tool (Section 3) |
| `error: failed to load manifest for dependency cvode_rs` | the solver engine was not fetched | run Section 4.2, then build again |
| `vendor/rustSolveIt is at ..., expected ...` | another or an interrupted engine download | delete `vendor/rustSolveIt` and run Section 4.2 again |
| `linker link.exe not found` (Windows) or `linker cc not found` (Linux) | the C build tools are missing | install them (Section 3.2) and build again |
| `LNK1104: cannot open file ... .rlib` (Windows) | the folder path is too long | clone into a short folder such as `C:\src` |
| the program writes into `artifacts/...` | you forgot `--output` | restore with `git checkout -- artifacts` and use `--output build/...` |
| a spectrum file is `DIFFERENT` from the committed one | another engine (`linux`, `macos`), or a build without `.cargo/config.toml` (FMA) | use `win11` in Section 4.2 and build inside the repository |
| `error: externally-managed-environment` (pip, Linux or macOS) | pip outside a virtual environment | create and activate the environment of Section 3.3 |
| `ModuleNotFoundError: No module named 'nbformat'` (or `nbclient`, `nbconvert`, `ipykernel`, `mpmath`) | a Python package is missing in the Python you used | install it (Section 3.3) into the same Python or environment |
| `No such kernel named python3` | `ipykernel` is missing in the environment that runs nbconvert | install it into that environment |
| `RuntimeError: dirac16complex_kohn_sham binary not found` (notebook) | the Rust program was not built | build it (Section 5.1) |
| the Wolfram steps of the gate print `stage4_skipped_step=...` | WolframScript is not installed | expected; the gate still passes without them and names what was not run |
| a Wolfram step fails with a licence or kernel message | the Wolfram Engine is not activated, or another kernel is running | `wolframscript -activate`; close other Wolfram sessions (the gate retries such steps up to three times) |
| the PDF build reports `registeredSha256=false` | a TeX distribution other than the one that registered the PDF | expected outside the registering computer; every other check must pass |
| the gate stops at step 14 after hours | a Rust process failed or ran out of memory | read its log `build/logs/stage4-14-rust-runs-...-<subcommand>.log`; rerun with `-SequentialRust` / `--sequential-rust` on a small computer |

## 18. Glossary

| term | meaning |
| --- | --- |
| aufbau | filling the lowest levels one after another; the $T=0$ ground state of non-interacting fermions |
| band (brane band) | the levels $\varepsilon\approx\pm ck$ that grow out of the zero modes; they hold most particles |
| block, block type $j$ ($s=-j$) | one of the eight independent two-component systems; four blocks of each type $j=\pm1$ |
| brane | the membrane at $y=0$ where two copies of the field are glued (the notebook's pair of universes) |
| bulk level | a level that is not on the brane band, for example the massive $k=0$ levels |
| chemical potential $\mu$ | the energy at which the Fermi–Dirac occupation is $\tfrac12$; fixed by the particle number |
| closed / open shell | $N$ completes / does not complete a degenerate group of levels |
| CVODE | the variable-step ODE solver of SUNDIALS, here in a pure-Rust port |
| $\Delta$SCF | the excitation energy from a self-consistent state with one particle moved |
| Dirac sea | the negative-energy levels of a relativistic field, full in the vacuum; an empty sea level is an antiparticle |
| exchange | the part of the interaction energy that comes from the antisymmetry of fermion states; here $e_x=-(\lambda/32)(n^2+S^2)$ |
| gap (KS gap) | $\varepsilon_{\mathrm{LUMO}}-\varepsilon_{\mathrm{HOMO}}$ |
| Hartree term | the average interaction of a particle with all others, $\tfrac\lambda2S^2$ |
| HOMO / LUMO | highest occupied / lowest unoccupied level |
| Kohn–Sham equations | single-particle equations in density-dependent potentials whose solution has the density of the interacting system |
| LDA | local-density approximation: the uniform-gas formula used at each point |
| Mermin functional | the free energy $F=E-TS_{\mathrm{ent}}$ minimised at temperature $T$ |
| normal ordering | counting energies and densities relative to the free vacuum |
| occupation smearing | Fermi–Dirac occupations with a small width, used to converge a degenerate crossing at $T=0$ |
| particle-hole excitation | moving one particle from an occupied to an empty level |
| proper / coordinate density | per unit real volume / per unit coordinate $y$; they differ by $e^{6Hy}$ |
| Prüfer angle, Prüfer index | the angle of the vector $(a,-b)$; the integer that numbers the levels by the winding of that angle |
| pseudo-potential | the local pair $M_{\mathrm{eff}}$, $v_x$ computed from the uniform-gas thermodynamics |
| regula falsi (Illinois) | root finding by straight-line interpolation inside a bracket, with the Illinois correction |
| Richardson extrapolation | removing the leading grid errors from results on several grids |
| scalar density $S$ | $\bar\Psi\Psi$; enters the Hartree mass shift and the exchange |
| self-consistent field (SCF) | the iteration potentials, levels, densities, potentials until nothing changes |
| shell $n_2$ | the lattice momenta with $n_1^2+n_2^2+n_3^2=n_2$, all with the same $|k|$ |
| tip, tip cutoff $L$ | the end $y\to-\infty$ where the warped directions pinch off; the program stops at $y=-L$ |
| torus | the periodic 3-space of size $\ell$; makes the momenta discrete |
| zero mode | the $k=0$ level $\chi=(e^{My},0)$ at $\varepsilon=0$, concentrated at the brane |

## 19. Credits, licences and verified facts

The repository is licensed under GPL-3.0-or-later. The pure-Rust SUNDIALS 7.8.0 engine (rustSolveIt, author once-ere) is BSD-3-Clause per its Cargo manifests and is fetched, not copied, into `vendor/`. The notebook runner and auditor are adapted from the rustSolveIt planet_Mercury notebook tools (BSD-3-Clause); `studies/dirac16complex_kohn_sham/src/driver.rs` and `output.rs` are copies of the Stage-3 crate of this repository. The PDF builder derives from `scripts/build_dissertation_tex.py` of https://github.com/once-ere/dirac (GPL-3.0-or-later).

**Verified facts quoted in this guide.** Every number in this guide was copied from a committed file or printed by a command that was executed while the guide was written (Section 2.3). The committed numbers of the scientific results are those of the main document; the check counts are: Wolfram 125, sympy 157, Rust 397 (spectrum 33, scf 137, excited 65, thermo 102, emt 60), Mathematica 94, {{verifiedcounts}}.
