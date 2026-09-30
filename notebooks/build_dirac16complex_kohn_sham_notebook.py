#!/usr/bin/env python3
"""Author (and optionally execute) notebooks/dirac16complex_kohn_sham.ipynb deterministically.

Origin and licence
------------------
Adapted from the Stage-3 builder notebooks/build_dirac16complex_notebook.py of
this repository, which is itself adapted from the notebook builder of the
rustSolveIt engine, planet_Mercury/notebook/build_notebook.py in
https://github.com/once-ere/rustSolveIt_Win11_SUNDIALS_7_8_0 at commit
a8fdff459adfe181573d7924b18bffbdf378fdb3 (author: once-ere; BSD-3-Clause, as
declared in the rustSolveIt Cargo manifests).  See NOTICE, section 2d.

Kept from the originals: the md()/code() cell helpers, the nbformat-4.5 layout
with the "Python 3 (ipykernel)" kernel, the find_binary()/run() driver with
the last-line SUCCESS contract, the gauntlet of asserts, the deterministic
figure writer (Agg, fixed dpi, no software stamp), and the rule that every
number quoted in the markdown is re-read and asserted by the gauntlet.

Changed for Stage 4 (the Kohn-Sham study of studies/dirac16complex_kohn_sham):
every cell is new; the numbers quoted in the prose are NOT typed by hand: the
builder executes the notebook's own data-loading cell (DATA_CODE) against the
committed outputs under artifacts/dirac16complex/kohn-sham/ and fills every
<<key>> placeholder (written with guillemets) from an expression evaluated
there, so re-running this builder after the outputs change refreshes every
number; the gauntlet cell re-evaluates the same expressions and asserts that
the prose still matches.  Heavy subcommands of the Rust solver are not re-run
inside the notebook (a full "all" run takes hours); the notebook re-runs
print-config and the spectrum subcommand (about a minute) into a scratch
folder and compares the spectrum files byte for byte with the committed ones.
Inputs that are absent (a summary being regenerated, the cross-checker report)
are reported as SKIP lines, never as passing checks.

Usage (from the repository root):
    python notebooks/build_dirac16complex_kohn_sham_notebook.py            # write the un-executed notebook
    python notebooks/build_dirac16complex_kohn_sham_notebook.py --execute  # write it and execute it in place (nbclient)
    python notebooks/build_dirac16complex_kohn_sham_notebook.py --output PATH [--execute]
Execution needs nbformat, nbclient and ipykernel (kernel "python3"); it runs
with the repository root as working directory and records no cell timings.
Exit code 0 only if the build (and, with --execute, every cell) succeeded.
Re-running the builder on unchanged inputs produces the identical file.
"""

import argparse
import json
import os
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
NOTEBOOK_NAME = "dirac16complex_kohn_sham.ipynb"
DEFAULT_OUTPUT = REPO / "notebooks" / NOTEBOOK_NAME

# ---------------------------------------------------------------------------
# The notebook's data cell.  It is executed by the builder (to fill the numbers
# quoted in the prose) and it is the first computational cell of the notebook.
# It only reads committed files; it never runs a program.
# ---------------------------------------------------------------------------
DATA_CODE = r'''
import csv
import hashlib
import json
import math
import os
import re
from pathlib import Path

import numpy as np


def find_repo():
    here = Path.cwd().resolve()
    for folder in (here, *here.parents):
        if (folder / "studies" / "dirac16complex_kohn_sham" / "Cargo.toml").is_file():
            return folder
    raise RuntimeError("start the notebook inside the Dirac_claude repository "
                       "(the folder that contains studies/dirac16complex_kohn_sham)")


REPO = find_repo()
KSDIR = REPO / "artifacts" / "dirac16complex" / "kohn-sham"
RUST = KSDIR / "rust"
REFDIR = KSDIR / "reference"
FIGDIR = KSDIR / "figures"
FIXTURE = REPO / "artifacts" / "dirac16complex" / "arbitrary-field" / "algebra-fixture.json"
SUBCOMMANDS = ("spectrum", "scf", "excited", "thermo", "emt")
LAMBDA_NAMES = ("lamm2", "lamm1", "lam0", "lamp1", "lamp2")
SMEARED = "m1_L3_N1016_lamm2_T0"          # the level-crossing run (section 9.3)


def load_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def optional_json(path):
    """(parsed JSON or None, status): 'present', 'absent' or 'unreadable' (being rewritten)."""
    path = Path(path)
    if not path.is_file():
        return None, "absent"
    try:
        return load_json(path), "present"
    except (OSError, ValueError):
        return None, "unreadable"


def load_csv(path):
    """A CSV with one header row -> {column name: numpy float array}; 'nan' is allowed."""
    path = Path(path)
    with open(path, encoding="utf-8", newline="") as handle:
        header = handle.readline().rstrip("\n").split(",")
    data = np.loadtxt(path, delimiter=",", skiprows=1, ndmin=2)
    if data.size == 0:
        data = np.zeros((0, len(header)))
    return {name: data[:, j] for j, name in enumerate(header)}


def sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


LABEL_RE = re.compile(r"^m(?P<m>[0-9p]+)_L(?P<L>[0-9p]+)_N(?P<N>\d+)_(?P<lam>lam[a-z0-9]+)_T(?P<T>[0-9p]+)"
                      r"(?P<extra>(?:_[a-z0-9p]+)*)$")


def label_number(text):
    return float(text.replace("p", "."))


def parse_label(label):
    """m1_L3_N112_lamp1_T0p3[_a40p5|_g601|_dk0p125...] -> parameters encoded in a run label."""
    match = LABEL_RE.match(label)
    if match is None:
        return None
    d = match.groupdict()
    return {"m": label_number(d["m"]), "L": label_number(d["L"]), "N": int(d["N"]), "lam": d["lam"],
            "T": label_number(d["T"]), "extra": d["extra"]}


def run_labels(sub):
    base = RUST / sub
    return sorted(p.name for p in base.iterdir() if p.is_dir()) if base.is_dir() else []


def runs_of(sub):
    """{label: run.json} of the finished runs of one subcommand."""
    out = {}
    for label in run_labels(sub):
        path = RUST / sub / label / "run.json"
        if path.is_file():
            out[label] = load_json(path)
    return out


# ---- the committed exact theory and the Rust outputs ------------------------
THEORY = load_json(KSDIR / "kohn-sham-theory.json")
EXTABLE = load_json(KSDIR / "exchange-table.json")
WOLFRAM, WOLFRAM_STATUS = optional_json(KSDIR / "wolfram-kohn-sham-report.json")
PYTHEORY, PYTHEORY_STATUS = optional_json(KSDIR / "python-theory-report.json")
GEOM = load_json(RUST / "spectrum" / "geometry.json")
REDUCTION = load_json(RUST / "spectrum" / "reduction.json")
AGREE = load_json(RUST / "spectrum" / "theory-agreement.json")
SUMMARY, SUMMARY_STATUS = {}, {}
for _sub in SUBCOMMANDS:
    SUMMARY[_sub], SUMMARY_STATUS[_sub] = optional_json(RUST / _sub / "summary.json")
SPEC = SUMMARY["spectrum"]
DET, DET_STATUS = optional_json(RUST / "determinism-report.json")
SCF = runs_of("scf")
THERMO = runs_of("thermo")
EMT = runs_of("emt")
EXCITED_LABELS = run_labels("excited")
EXCITATIONS = load_csv(RUST / "excited" / "excitations.csv")
THERMO_TABLE = load_csv(RUST / "thermo" / "thermodynamics.csv")
EMT_TABLE = load_csv(RUST / "emt" / "emt-summary.csv")
CLOSED_SHELLS = load_csv(RUST / "spectrum" / "closed-shells-m1-L3.csv")


def par(label, key):
    """A parameter of an scf run (run.json 'parameters')."""
    return SCF[label]["parameters"][key]


def excited_row(label):
    """The excitations.csv row of an excited run: {column: value}.  The table has no
    label column; the row is the one with the scf run's N and lambda_hat."""
    N, lam = par(label, "N"), par(label, "lambdaHat")
    hit = [i for i in range(len(EXCITATIONS["N"]))
           if EXCITATIONS["N"][i] == N and abs(EXCITATIONS["lambda_hat"][i] - lam) <= 1e-14 * max(abs(lam), 1e-300)]
    if len(hit) != 1:
        raise KeyError(f"excitations.csv has {len(hit)} rows for {label}")
    return {key: float(col[hit[0]]) for key, col in EXCITATIONS.items()}


def exc(label, column):
    return excited_row(label)[column]


EXC_RECORDS = {r["label"]: r for r in (SUMMARY["excited"] or {}).get("runs", []) if isinstance(r, dict)}
EXCITED_MAIN = [label for label in EXCITED_LABELS if label in SCF]      # the 15 runs with an scf twin
EXCITED_EXTRA = [label for label in EXCITED_LABELS if label not in SCF]  # e.g. a 601-point grid twin


def excited_record(label):
    """An excited run's record: from excited/summary.json when present, else rebuilt from
    excitations.csv and particle-hole.csv (possible for the runs with an scf twin)."""
    if label in EXC_RECORDS:
        return EXC_RECORDS[label]
    row = excited_row(label)
    ph = load_csv(RUST / "excited" / label / "particle-hole.csv")["excitation"]
    return {"label": label, "N": row["N"], "lambdaHat": row["lambda_hat"], "E0": row["E0"], "mu": row["mu"],
            "ksGap": row["ks_gap"], "deltaScf": row["delta_scf"], "E1": row["E1"],
            "lowestParticleHole": float(ph[0]), "parameters": SCF[label]["parameters"], "rebuilt": True}


def lam_hat(N, name, m=1, L=3):
    """lambda_hat of the (m, L, N) configuration for a series name (read from the scf run)."""
    return par(f"m{m}_L{L}_N{N}_{name}_T0", "lambdaHat")


def thermo_row(series, N, T):
    t = THERMO_TABLE
    hit = [i for i in range(len(t["N"])) if t["series"][i] == series and t["N"][i] == N and abs(t["T"][i] - T) < 1e-12]
    if len(hit) != 1:
        raise KeyError((series, N, T))
    return {key: float(col[hit[0]]) for key, col in t.items()}


_LEVELS_CACHE = {}


def levels(sub, label, name="levels.csv"):
    """levels.csv (or levels-excited.csv) of a run, read once."""
    key = (sub, label, name)
    if key not in _LEVELS_CACHE:
        _LEVELS_CACHE[key] = load_csv(RUST / sub / label / name)
    return _LEVELS_CACHE[key]


def fractional_levels(sub, label, floor=1e-12, tol=1e-9):
    """Particle levels with floor < f < 1 - floor, grouped by eps (within tol) and k:
    [{'eps', 'k', 'mult', 'count', 'f', 'rows'}] sorted by eps; 'count' = sum mult f
    (the particles in the group), 'f' = count/mult (the rows of one exactly degenerate
    level differ by round-off in eps and therefore by ~1e-9 in f)."""
    lv = levels(sub, label)
    sel = (lv["branch"] > 0) & (lv["f"] > floor) & (lv["f"] < 1.0 - floor)
    rows = sorted(zip(lv["eps"][sel], lv["k"][sel], lv["multiplicity"][sel], lv["f"][sel]))
    groups = []
    for eps, k, mult, f in rows:
        if groups and eps - groups[-1]["eps"] <= tol and abs(k - groups[-1]["k"]) < 1e-12:
            groups[-1]["mult"] += float(mult)
            groups[-1]["count"] += float(mult * f)
            groups[-1]["rows"] += 1
        else:
            groups.append({"eps": float(eps), "k": float(k), "mult": float(mult), "count": float(mult * f),
                           "rows": 1})
    for g in groups:
        g["f"] = g["count"] / g["mult"]
    return groups


FRACTIONAL = fractional_levels("scf", SMEARED)
BAND = max(FRACTIONAL, key=lambda g: g["mult"])            # the 192-fold k = 0.935 band
KZERO = min(FRACTIONAL, key=lambda g: g["k"])              # the 8-fold k = 0 level
MOVED = BAND["mult"] - BAND["count"]                       # particles moved out of the band


def particle_hole_list(sub, label, floor=1e-12, count=12):
    """The particle-hole rule of both solvers: holes f > floor, particles f < 1 - floor
    (particle branch), pairs with eps_particle > eps_hole, the lowest `count`."""
    lv = levels(sub, label)
    part = lv["branch"] > 0
    occ = part & (lv["f"] > floor)
    emp = part & (lv["f"] < 1.0 - floor)
    diff = lv["eps"][emp][None, :] - lv["eps"][occ][:, None]
    return np.sort(diff[diff > 0])[:count]


PH_SMEARED = particle_hole_list("scf", SMEARED)
CHECKREP, CHECKREP_STATUS = optional_json(KSDIR / "python-check-report.json")
print("data loaded: theory, exchange table, Rust summaries",
      {sub: SUMMARY_STATUS[sub] for sub in SUBCOMMANDS},
      f"| runs: scf {len(SCF)}, excited {len(EXCITED_LABELS)}, thermo {len(THERMO)}, emt {len(EMT)}",
      f"| determinism report {DET_STATUS} | cross-check report {CHECKREP_STATUS}")
'''

# ---------------------------------------------------------------------------
# Numbers quoted in the markdown prose.  q(key, fmt, expr) registers a quote:
# the builder evaluates expr in the DATA_CODE namespace and prints it with the
# format fmt; the gauntlet re-evaluates expr inside the notebook and asserts
# that fmt.format(value) is still the printed text.
# ---------------------------------------------------------------------------
_NS = None
QUOTES = {}


def _namespace():
    global _NS
    if _NS is None:
        cwd = os.getcwd()
        os.chdir(REPO)
        try:
            ns = {"__name__": "__builder__"}
            import contextlib
            import io
            with contextlib.redirect_stdout(io.StringIO()):
                exec(compile(DATA_CODE, "<DATA_CODE>", "exec"), ns)
            _NS = ns
        finally:
            os.chdir(cwd)
    return _NS


def q(key, fmt, expr):
    """Register a quoted number and return its placeholder."""
    if key in QUOTES and QUOTES[key][:2] != (fmt, expr):
        raise ValueError(f"quote {key} registered twice with different definitions")
    value = eval(expr, _namespace())
    text = fmt.format(value)
    QUOTES[key] = (fmt, expr, text)
    return "«" + key + "»"


_USED_KEYS = {}


def _fill(text):
    def repl(match):
        _USED_KEYS[match.group(1)] = True
        return QUOTES[match.group(1)][2]

    return re.sub("«(\\w+)»", repl, text)


def md(text):
    return {"cell_type": "markdown", "metadata": {}, "source": _fill(text.strip("\n")).splitlines(keepends=True)}


def code(text):
    return {"cell_type": "code", "execution_count": None, "metadata": {}, "outputs": [],
            "source": text.strip("\n").splitlines(keepends=True)}


CELLS = []

# ===========================================================================
# 1. What this notebook computes
# ===========================================================================
q("n_mid", "{:.0f}", 'SPEC["reference"]["nMid"]')
q("n_large", "{:.0f}", 'SPEC["reference"]["nLarge"]')
q("c_theory", "{:.10f}", 'float(AGREE["checks"]["theory_zero_mode_splitting"]["detail"].split("theory c = ")[1].split()[0])')
q("gap8_L3", "{:.7f}", 'SCF["m1_L3_N8_lam0_T0"]["ksGap"]')
q("E0_112", "{:.6f}", 'SCF["m1_L3_N112_lam0_T0"]["energy"]')
q("E0_1016", "{:.6f}", 'SCF["m1_L3_N1016_lam0_T0"]["energy"]')
q("bf_8", "{:.3f}", 'EMT["m1_L3_N8_lam0_T0"]["emt"]["braneFraction_within_1_over_H"]')
q("bf_112", "{:.3f}", 'EMT["m1_L3_N112_lam0_T0"]["emt"]["braneFraction_within_1_over_H"]')
q("bf_1016", "{:.3f}", 'EMT["m1_L3_N1016_lam0_T0"]["emt"]["braneFraction_within_1_over_H"]')
q("bf_m3", "{:.3f}", 'SCF["m3_L3_N112_lam0_T0"]["emt"]["braneFraction_within_1_over_H"]')
q("kappa_112", "{:.0f}", 'EMT["m1_L3_N112_lam0_T0"]["emt"]["kappaNeeded"]')
q("kappa_1016", "{:.1f}", 'EMT["m1_L3_N1016_lam0_T0"]["emt"]["kappaNeeded"]')
q("rho_req", "{:.0f}", 'GEOM["rhoRequired_kappa1"]')
q("p_req", "{:+.0f}", 'GEOM["pRequired_kappa1_y_x1_x2_x3_x5_x6_x7"][0]')
q("ricci", "{:.0f}", 'GEOM["ricciScalar"]')
q("E_T1_N8", "{:.1f}", 'thermo_row(0, 8, 1.0)["E"]')
q("maxlamS_m2", "{:.2f}", 'SCF[SMEARED]["maxLambdaSOverM"]')
q("maxvx_m2", "{:.2f}", 'SCF[SMEARED]["maxVxOverM"]')

CELLS.append(md(r"""
# dirac16complex Kohn-Sham DFT in the primordial gravitational field: ground and first excited states

## 1. What this notebook computes

The **dirac16complex** field is a 16-component, complex, Grassmann-odd spinor
field $\Psi = (\Psi_0,\dots,\Psi_{15})^T$ of Pin(4,4) on an eight-dimensional
spacetime with four space-like and four time-like directions.  The
coordinates are $x_0,\dots,x_7$: $x_0$ is the hidden space direction
(replaced below by the proper coordinate $y$), $x_1,x_2,x_3$ are ordinary
3-space, $x_4$ is the time and $x_5,x_6,x_7$ are three extra time
directions.  This notebook is the complete numerical documentation of
**Stage 4**: a gas of $N$ dirac16complex quanta, bound to the static
primordial gravitational field of the original notebook, treated with
**Kohn-Sham density-functional theory** (Mermin's finite-temperature form),
for the ground state, the first excited state and the thermodynamics.

The question, in one line: *which self-consistent many-fermion state does the
field form in the primordial geometry, how is it localised, what energy and
pressure does it carry, and can it be the source that the geometry requires?*

**Where the numbers come from.** Every eigenvalue problem is solved by the Rust
program `studies/dirac16complex_kohn_sham` (CVODE shooting in $y$ on the
pure-Rust SUNDIALS 7.8.0 engine of rustSolveIt, Anderson-mixed
self-consistency).  A complete run of all its subcommands takes about four
hours, so this notebook does **not** repeat the heavy runs.  It

1. starts the program for its configuration (`print-config`) and re-runs the
   one-minute `spectrum` subcommand into a scratch folder, and checks that
   every file it writes is **byte-identical** to the committed one in
   `artifacts/dirac16complex/kohn-sham/rust/spectrum/`;
2. reads the committed canonical outputs (`artifacts/dirac16complex/kohn-sham/rust/`)
   with numpy;
3. **recomputes the key quantities independently in the cells**: the exact
   2x2 block reduction from the gamma matrices, the exchange closed form
   against the tabulated double quadrature, the analytic $k=0$ box spectrum
   and the chiral zero mode, the particle number from the level weights and
   from the density, the total energy $E=\sum f\varepsilon - E_H - E_x$,
   the pseudo-potential identities, the entropy and free energy, the
   energy-momentum tensor averages and the brane fraction;
4. compares the Rust results with the **independent Python reference solver**
   (a staggered-grid matrix method, `scripts/ks_reference_solver.py`) run by
   run, with the tolerances of the cross-checker
   `scripts/check_dirac16complex_kohn_sham.py`;
5. draws 14 figures into `artifacts/dirac16complex/kohn-sham/figures/`
   (matplotlib, Agg backend, fixed dpi, no software stamp: reproducible bytes);
6. ends in a gauntlet of asserts, including one that re-reads every number
   quoted in this prose from the committed files.

**The short answer, stated honestly.**

- Without interaction the spectrum has **brane zero modes**: at $k=0$ an
  exactly zero-energy chiral mode per block, localised at the $Z_2$ brane
  $y=0$; for $k\neq0$ it becomes the band $\varepsilon=\pm ck$ with
  $c$ = «c_theory» (closed form, section 4.5; recomputed in section 7).  The closed shells used below
  are $N = 8$ (the zero modes), «n_mid» and «n_large».  The Kohn-Sham gap of
  $N=8$ at $L=3$ is «gap8_L3» $m$.
- The ground states are **brane-localised**: the fraction of the particles
  within one Hubble length $1/H$ of the brane is «bf_8» ($N=8$),
  «bf_112» ($N$ = «n_mid») and «bf_1016» ($N$ = «n_large»), and «bf_m3» for
  $m=3H$, $N$ = «n_mid».  Free ground-state energies: «E0_112» $m$
  ($N$ = «n_mid») and «E0_1016» $m$ ($N$ = «n_large»).
- The self-consistent pseudo-potential stays inside the planned window except
  for the strongest attractive run ($N$ = «n_large», $-\hat\lambda_2$:
  $\max|\lambda S_p|/m$ = «maxlamS_m2», $\max|v_x|/m$ = «maxvx_m2»), which
  is also the one run whose exact $T=0$ occupation does not converge (a
  level crossing at the Fermi level; section 10.2 states exactly what was
  computed instead).
- **The Kohn-Sham gas cannot be the source the geometry needs.**  The field
  requires $\rho_\text{req}$ = «rho_req» $H^2/\kappa$ (negative) and
  $p_\text{req}$ = «p_req» $H^2/\kappa$ (curvature $R$ = «ricci» $H^2$).
  Every state with bulk levels carries $\langle\rho\rangle>0$, so the energy
  condition alone would need $\kappa$ = «kappa_112» ($N$ = «n_mid») or
  «kappa_1016» ($N$ = «n_large»), i.e. $\kappa<0$; the two static-field
  sourcing conditions of STAGE4_SPEC E4.1 are met in no run (section 12).
- At $T = m$ the state is a thermal particle-antiparticle plasma
  ($E$ = «E_T1_N8» $m$ for $N = 8$, section 11).

Units: $H = 1$ (the constant of the primordial field), energies in units of the
mass $m$ (mostly $m = H$; also $m = 3H$), $\kappa$ the 8D gravitational
coupling where it appears.
"""))

# ===========================================================================
# 2. How to run
# ===========================================================================
CELLS.append(md(r"""
## 2. How to run this notebook

One-time setup, from the repository root (the folder that contains
`studies/` and `notebooks/`):

1. **Fetch the solver engine** (git-ignored, pinned commit): PowerShell 7
   `pwsh -NoProfile -File scripts/setup_solver.ps1 -Platform win11`, or in Git
   Bash, macOS or Linux `bash scripts/setup_solver.sh win11`.  Only the Windows 11
   engine (`a8fdff45`) reproduces the committed outputs byte for byte; with
   the macOS or Linux engine every physics check still passes but the
   gauntlet line `fresh_spectrum_byte_identical` fails.
2. **Build the Kohn-Sham program**:
   `cd studies/dirac16complex_kohn_sham` then `cargo build --release`
   (the repository-root `.cargo/config.toml` adds `-C target-feature=+fma`,
   which the committed outputs assume).  Install Rust from https://rustup.rs
   if `cargo` is missing.
3. **Python** 3.11 or newer with `numpy` and `matplotlib`; for executing the
   notebook headless also `nbformat`, `nbclient` and `ipykernel`; for the
   interactive route `jupyterlab`.

Then choose one of three ways to run it:

* **Interactive**: `jupyter lab notebooks/dirac16complex_kohn_sham.ipynb`
  (or `python -m jupyterlab ...`).  If asked for a kernel, choose
  **Python 3 (ipykernel)**.  Click the first cell and press **Shift+Enter**
  repeatedly, or use Run, Run All Cells.
* **Headless with Jupyter's executor (nbclient)**, rebuilding the notebook
  first: `python notebooks/build_dirac16complex_kohn_sham_notebook.py --execute`
  (writes the executed notebook in place; this is how the committed copy was made).
* **Headless with the standard-library runner** of Stage 3:
  `python notebooks/run_notebook.py notebooks/dirac16complex_kohn_sham.ipynb`
  (writes the outputs back only if every cell succeeds).

Afterwards the audit
`python notebooks/check_dirac16complex_kohn_sham_notebook.py notebooks/dirac16complex_kohn_sham.ipynb --report artifacts/dirac16complex/kohn-sham/notebook-report.json`
checks the structure, the execution, the figures and the gauntlet and writes
the report.  **Edit the builder, not the `.ipynb`**: the builder reads the
committed outputs and fills in every number quoted in this text, so after the
outputs change, re-running the builder refreshes the prose; the gauntlet
refuses a notebook whose prose no longer matches the files.

The notebook finds the program through the environment variable
`DIRAC16KS_BIN` first, then
`studies/dirac16complex_kohn_sham/target/release/dirac16complex_kohn_sham`
(`.exe` on Windows).  `DIRAC16KS_NB_OUTPUT` changes the scratch output folder
(default `build/notebook-kohn-sham`, git-ignored); `DIRAC16KS_NB_SPECTRUM=0`
skips the one-minute spectrum re-run (the gauntlet then prints a SKIP line
for it, which the audit reports).  The whole notebook runs in a few minutes.

**Where this notebook comes from.** Its driver pattern (the builder's
`md()`/`code()` helpers, `find_binary()` and `run()` with the rule that the
program's last printed line must be `SUCCESS`, a gauntlet of asserts, the
standard-library executor and the structure audit) is adapted from the
rustSolveIt engine's `planet_Mercury/notebook/` (BSD-3-Clause, once-ere;
NOTICE, section 2d) through the Stage-3 notebook of this repository.
"""))

# ===========================================================================
# 3. Glossary
# ===========================================================================
CELLS.append(md(r"""
## 3. The words and symbols used in this notebook

Counting starts at 0 everywhere (coordinates $x_0..x_7$, frame indices
$a,b = 0..7$, spinor components $0..15$, blocks $0..7$).

**Geometry**

- $\eta = \mathrm{diag}(+1,+1,+1,+1,-1,-1,-1,-1)$: flat metric; $x_4$ is THE time.
- $y = \ln(\sin z)/(6H) \in (-\infty,0]$ with $z = 6Hx_0$: the proper hidden-space
  coordinate.  $y = 0$ ($z=\pi/2$) is the **brane**, $y=-L$ the **tip cutoff**
  ($L \in \{2,3,4\}/H$).
- $W(y) = e^{Hy}$: warp factor; $\sqrt{|g|} = W^6 = e^{6Hy}$: proper 7-volume
  per coordinate volume ("volume factor").  $a_4$: the (constant) primordial
  profile; $a_4 = 0$ except in one rescaling check.
- $\kappa(y) = e^{-Hy-a_4}$: the factor that converts the coordinate
  3-momentum $k$ into the local momentum (not the gravitational coupling
  $\kappa$ of Einstein's equations, which appears only in $\rho_\text{req}$
  and $p_\text{req}$).
- $\ell$: side of the 3-torus; $\Delta k = 2\pi/\ell = 0.25\,m$; the shells are
  $k^2 = \Delta k^2 n_2$ with $n_2 = n_x^2+n_y^2+n_z^2$ (CSV column `n2`).

**Field and algebra**

- $\gamma^a$: the 16x16 real gamma matrices of the original notebook;
  $C = \gamma^0\gamma^1\gamma^2\gamma^3$; $B = -iC\gamma^4$ (Hermitian, $B^2=1$).
- Expectation-value rule: for a Hilbert-normalised one-particle mode $u$,
  $\langle\Psi^\dagger M\Psi\rangle = u^\dagger BMu$.  Number density
  $u^\dagger u$, scalar density $u^\dagger BCu$.
- $\chi(y)$: the reduced two-component block spinor, $\chi = (\chi_1,\chi_2)$;
  the Rust program writes $\chi = (a, ib)$ with real $a, b$.
- $j = \pm1$: the block type of the exact theory (eigenvalue of
  $J = \gamma^0\gamma^1\gamma^4$ in its basis); both solvers label the type by
  $s = -j$ (CSV column `s`; recorded in `rust/spectrum/theory-agreement.json`
  and re-measured in section 7).
- Parity $\pm$: the boundary condition at the brane ($\chi_2(0) = 0$ or
  $\chi_1(0) = 0$).

**Kohn-Sham quantities**

- $\varepsilon$: Kohn-Sham single-particle energy; $f$: occupation;
  $w = f$ (particle branch) or $w = -(1-f)$ (Dirac-sea branch, thermal
  antiparticles): the weight with which a level enters $N$ and the densities.
  Branch $+1$/$-1$ (CSV column `branch`) is decided by continuity from $\lambda=0$.
- $n_p$, $S_p$: proper number and scalar densities; $n_c = e^{6Hy}n_p$,
  $S_c = e^{6Hy}S_p$: the same per unit $y$ (flat measure).
- $\lambda$: contact coupling of $U(S) = \frac{\lambda}{2}S^2$;
  $\hat\lambda = \lambda m^6$ its dimensionless value.  $\hat\lambda_1$,
  $\hat\lambda_2$: the couplings at which the first-order pseudo-potential
  reaches $0.1\,m$ and $1\,m$; run labels `lam0`, `lamp1` ($+\hat\lambda_1$),
  `lamm1` ($-\hat\lambda_1$), `lamp2`, `lamm2`, `lamh` (hot-calibrated).
- $M_\text{eff}(y)$, $v_x(y)$: the Kohn-Sham pseudo-potential pair (section 4.6).
- $E_H$, $E_x$: Hartree and exchange energies; $E$: total energy; $S$ (as a
  thermodynamic quantity, CSV `S_entropy`): entropy; $F = E - TS$;
  $C_V$: heat capacity; $\mu$: chemical potential.
- HOMO/LUMO: highest occupied / lowest unoccupied particle level; KS gap
  $\varepsilon_\text{LUMO}-\varepsilon_\text{HOMO}$; $\Delta$SCF: $E_1 - E_0$
  of the self-consistent state with one particle promoted.
- $\rho$, $p_y$, $p_3$, $p_t$: energy density and the pressures along $y$,
  3-space and the extra times; $w_y = \langle p_y\rangle/\langle\rho\rangle$,
  $w_3$, $w_t$; $\langle X\rangle$ = proper-volume average.
- Run labels: `m1_L3_N112_lamp1_T0p3` = $m = 1$, $L = 3$, $N = 112$,
  $+\hat\lambda_1$, $T = 0.3\,m$; suffixes `_g601` (601-point grid),
  `_dk0p125` ($\Delta k = 0.125\,m$), `_a40p5` ($a_4 = 0.5$).
"""))

# ===========================================================================
# 4. The physics
# ===========================================================================
q("einstein_y", "{:.0f}", 'GEOM["einsteinMixed_y_x1_x2_x3_x4_x5_x6_x7"][0]')
q("einstein_4", "{:.0f}", 'GEOM["einsteinMixed_y_x1_x2_x3_x4_x5_x6_x7"][4]')
q("ext_K", "{:.0f}", 'GEOM["extrinsicK_x1_x2_x3_x4_x5_x6_x7"][0]')
q("th_metric", "{}", 'THEORY["geometry"]["metric"]["tex"]')
q("th_rho_brane", "{}", 'THEORY["geometry"]["extensions"]["E2_Z2mirror"]["braneEnergyDensity"]')
q("th_p_brane", "{}", 'THEORY["geometry"]["extensions"]["E2_Z2mirror"]["branePressure"]')
q("th_stress", "{}", 'THEORY["geometry"]["extensions"]["E2_Z2mirror"]["braneStress"]')
q("th_israel", "{}", 'THEORY["geometry"]["extensions"]["E2_Z2mirror"]["israelConvention"]')
q("th_w_req", "{}", 'THEORY["geometry"]["requiredSource"]["w"]')

CELLS.append(md(r"""
## 4. The physics

### 4.1 The static primordial field in the warped $y$-chart

The primordial field of the original notebook, with its profile $a_4$ held
constant (the static member of the family, needed for a stationary ground
state), becomes in the proper hidden-space coordinate $y = \ln(\sin z)/(6H)$
a warped product (exact theory, `artifacts/dirac16complex/kohn-sham/kohn-sham-theory.json`):

$$«th_metric»$$

so $ds^2 = dy^2 - dx_4^2 + e^{2Hy}\bigl[e^{2a_4}d\vec x^{\,2} - e^{-2a_4}d\vec y^{\,2}\bigr]$
with $\vec x = (x_1,x_2,x_3)$ and $\vec y = (x_5,x_6,x_7)$.  The warp factor
is $W = e^{Hy}$ and the proper volume element per coordinate volume is
$\sqrt{|g|} = W^6 = e^{6Hy}$: the transverse space pinches off towards the
"tip" $y\to-\infty$.  The curvature is constant: $R$ = «ricci» $H^2$ and
$G^\mu{}_\nu = \mathrm{diag}(15,15,15,15,21,15,15,15)H^2$ (order
$y,x_1,x_2,x_3,x_4,x_5,x_6,x_7$; the program re-derives
$G^y{}_y$ = «einstein_y» $H^2$ and $G^4{}_4$ = «einstein_4» $H^2$ from the
Christoffel symbols).  With $G^\mu{}_\nu = \kappa T^\mu{}_\nu$,
$\rho = -T^4{}_4$ and $p_{(i)} = T^i{}_i$, 8D Einstein gravity therefore
requires the source

$$\rho_\text{req} = -21\,H^2/\kappa < 0,\qquad p_\text{req} = +15\,H^2/\kappa
\ \text{(all seven transverse directions)},$$

(`«th_w_req»`).  This is STAGE4_SPEC erratum E4.3: the sign of $p_\text{req}$
is $+$, not the $-15$ of the original specification.

### 4.2 The $Z_2$ brane and the tip

The notebook's "pair of universes" is the $Z_2$ mirror extension
$W = e^{-H|y|}$: two copies of the patch glued at $y = 0$.  The extrinsic
curvature of the surfaces $y = $ const is $K^i{}_j = H\delta^i_j$ on the six
warped directions («ext_K» $H$ measured) and 0 on $x_4$, so the gluing carries
an Israel brane stress.  With the convention `«th_israel»` the exact
theory gives `«th_stress»`, i.e. `«th_rho_brane»` and `«th_p_brane»`.
The brane is not a pure tension.  At the other end the
numerical domain is cut at $y = -L$ (the "tip cutoff"), $L \in \{2, 3, 4\}/H$;
the tip is a genuine singular end ($W^6\to0$), and the $L$-dependence is
reported in section 14.

### 4.3 The Kohn-Sham ansatz and the reduced equation

Only modes independent of the extra times ($x_5, x_6, x_7$) are used (the
"good sector": modes with extra-time momentum are unstable, Stage 1 and
Stage 3 EXP-5).  3-space is a coordinate torus of side $\ell$, so
$\vec k \in (2\pi/\ell)\mathbb{Z}^3$, and by rotational symmetry
$\vec k = (k,0,0)$.  The ansatz

$$\Psi = e^{-i\varepsilon x_4}\,e^{i\vec k\cdot\vec x}\,W(y)^{-3}\,\chi(y)$$

removes the spin-connection term $\gamma^\mu\Omega_\mu = 3H\gamma^0$ exactly and
makes the measure flat in $y$ ($\sqrt{|g|}\Psi^\dagger\Psi\,d^8x = \chi^\dagger\chi\,dy\,d^7x$).
The field equation becomes

$$\gamma^0\chi' + i\kappa(y)k\gamma^1\chi - i(\varepsilon - v_v(y))\gamma^4\chi = M_\text{eff}(y)\chi,
\qquad \kappa(y) = e^{-Hy-a_4},$$

a first-order system in $y$ whose "momentum term" $\kappa k$ grows towards
the tip: 3-momentum confines the modes towards the brane.

### 4.4 Eight 2x2 blocks

The matrices $\gamma^0$, $\gamma^0\gamma^1$, $\gamma^0\gamma^4$, $B$ and $C$
are simultaneously block-diagonal in an explicit basis (columns: Gaussian
integers of norm$^2$ 8, recorded in `kohn-sham-theory.json`, printed and
re-verified in section 6.1).  The blocks are labelled by the eigenvalues
$(j, s_2, s_3)$ of the commuting operators $J = \gamma^0\gamma^1\gamma^4$,
$K_1 = \gamma^2\gamma^3$, $K_2 = \gamma^5\gamma^6$.  In every block
$\gamma^0\to\sigma_3$, $\gamma^0\gamma^1\to -i\sigma_2$,
$\gamma^0\gamma^4\to j\sigma_1$, $B\to j s_2$, $C\to s_2\sigma_2$,
$BC\to j\sigma_2$, and the 16-component equation becomes eight copies of

$$\chi' = \bigl[M_\text{eff}\,\sigma_3 - \kappa k\,\sigma_2 + i j(\varepsilon - v_v)\,\sigma_1\bigr]\chi,$$

equivalently $h_j\chi = \varepsilon\chi$ with
$h_j = j\bigl[-i\sigma_1\partial_y + M_\text{eff}\sigma_2 + \kappa k\sigma_3\bigr] + v_v$.
There are **two inequivalent block types**, $j = +1$ (blocks 0-3) and $j = -1$
(blocks 4-7); at fixed $\vec k$ each level is **4-fold** (the four blocks of
one type), and $h_{-1} - v_v = -(h_{+1} - v_v)$: the $j=-1$ blocks carry the
negated spectrum.  8-fold degeneracy holds at $k = 0$ and over a closed shell
$\{\vec k, -\vec k\}$ (STAGE4_SPEC erratum E4.4).  With $\chi = (a, ib)$ the
Rust program integrates the real system
$a' = Ma + (s\varepsilon - \kappa k)b$, $b' = -(s\varepsilon + \kappa k)a - Mb$
with $s = -j$.  The number, scalar and $y$-current densities of a block orbital
are $\chi^\dagger\chi$, $j\chi^\dagger\sigma_2\chi$ and $j\chi^\dagger\sigma_1\chi$
(times $e^{-6Hy}/\ell^3$ for the proper densities).

### 4.5 Boundary conditions

The $y$-current matrix after the expectation rule is $A_4 = \gamma^0\gamma^4$
($j\sigma_1$ in a block; erratum E4.5); $\chi^\dagger A_4\chi$ is constant in
$y$ for every solution, so each end must kill it.  At the brane the two
**parities** $\chi_2(0) = 0$ (even, "parity +") and $\chi_1(0) = 0$ (odd,
"parity -") are used, both computed; at the tip the chiral-bag condition
$(1 - Q(\theta))\chi(-L) = 0$, $Q = \cos\theta\,\sigma_3 + \sin\theta\,\sigma_2$,
with $\theta = 0$, i.e. $\chi_2(-L) = 0$.  Each condition makes
$\chi^\dagger\sigma_1\chi = 2\,\mathrm{Re}(\chi_1^*\chi_2)$ vanish.  (The
reflection $\Psi(-y) = \pm\gamma^0\Psi(y)$ is a symmetry of the reduced
equation only for an odd mass function; the two parities are therefore
boundary conditions, not symmetries: erratum E4.6.)  Consequences that are
checked numerically below: for $k = 0$, constant $M$ and parity + the exact
spectrum is $\varepsilon = 0$ (the **chiral zero mode** $\chi = (e^{My}, 0)$,
localised at the brane) and $\varepsilon = \pm\sqrt{M^2 + (n\pi/L)^2}$,
$n = 1, 2, \dots$; for parity - the levels are $\varepsilon = \pm\sqrt{M^2+p^2}$
with $\tan(pL) = -p/M$.  For $k\neq0$ the zero mode splits linearly,
$\varepsilon = jck + O(k^3)$ (the branch is odd in $k$: $\sigma_3$ maps $(k, j)$
onto $(-k, -j)$ and $h_{-1} = -h_{+1}$ at $v_v = 0$), with the closed form
(Hellmann-Feynman)

$$c = e^{-a_4}\,\frac{2M}{2M - H}\,\frac{1 - e^{-(2M-H)L}}{1 - e^{-2ML}}.$$

### 4.6 The Kohn-Sham fermion-gas thermodynamics pseudo-potential

The interaction is the contact term $U(S) = \frac{\lambda}{2}S^2$ with
$S = \bar\Psi\Psi$, normal ordered with respect to the free Dirac sea.

* **Hartree** (the mean field): the mass shift $\lambda S_p(y)$ with the
  proper scalar density $S_p = e^{-6Hy}\sum f\,\chi^\dagger(j\sigma_2)\chi/\ell^3$.
* **Exchange** (Fock) of the contact interaction is **exactly local**: for the
  uniform 8-fold gas at every temperature the angular average kills the
  $\vec p\cdot\vec q$ term of the exchange kernel and the double momentum
  integral collapses to
  $$e_x(n, S) = -\frac{\lambda}{32}\bigl(n^2 + S^2\bigr),\qquad
  v_v = \frac{\partial e_x}{\partial n} = -\frac{\lambda}{16}n,\qquad
  v_s = \frac{\partial e_x}{\partial S} = -\frac{\lambda}{16}S$$
  (erratum E4.7; a filled shell of 8 states gives $E_x = -E_H/8$).  The table
  `exchange-table.json` of the finite-temperature uniform gas $e_x(n, T)$
  (double Gauss-Legendre quadrature) is therefore a cross-check of the closed
  form, recomputed in section 6.2, not an input.
* **The pseudo-potential** is the local pair
  $$M_\text{eff}(y) = m + \lambda S_p + v_s = m + \tfrac{15}{16}\lambda S_p(y),\qquad
  v_x(y;\,n_p, T) = v_v = -\tfrac{\lambda}{16}\,n_p(y),$$
  built from the thermodynamics of the uniform dirac16complex gas through
  Mermin's finite-temperature functional
  $F = \sum_n f_n\langle h_0\rangle_n - TS_\text{ent}[f] + E_H + E_x$; its
  stationarity gives the block equation of 4.4 with these potentials
  ($\varepsilon\to\varepsilon - v_x$ locally) and Fermi-Dirac occupations
  $f_n = 1/(e^{(\varepsilon_n-\mu)/T}+1)$.  The temperature enters through
  the occupations.  The gravitational terms are the $W^{-3}$ factor (which
  absorbs $3H\gamma^0$), $\kappa(y)k$ and the boundary conditions.
* **No correlation term**: a contact interaction beyond Hartree-Fock is not
  renormalisable in eight dimensions, so there is no controlled correlation
  functional; the Kohn-Sham functional here is exactly Hartree-Fock-local.

### 4.7 Self-consistency, occupations and energies

The Rust program solves every level by Pruefer-angle shooting with CVODE from
$y = -L$ to $0$ (Sturm-type oscillation count, so no level in the window is
missed), fills the states of the 3-torus shells by $\varepsilon$ with
Fermi-Dirac occupations ($\mu$ by bisection; at $T = 0$ the aufbau, a
straddling shell filled as an ensemble), rebuilds $n_p$, $S_p$,
$M_\text{eff}$, $v_x$ on a 301-point grid, and iterates with Anderson mixing
until the density changes by less than $10^{-10}$.  Normal ordering: particle
levels enter with weight $w = f$, Dirac-sea levels with $w = -(1-f)$
(thermal antiparticles), the branch being decided by continuity from
$\lambda = 0$.  The energies are

$$E = \sum_n w_n\varepsilon_n - E_H - E_x,\quad
E_H = \int\!\frac{\lambda}{2}S_p^2\,dV_p,\quad
E_x = -\int\!\frac{\lambda}{32}(n_p^2 + S_p^2)\,dV_p,\quad
dV_p = \ell^3 e^{6Hy}dy,$$

$F = E - TS_\text{ent}$, and the particle number $N = \sum_n w_n = \int n_p\,dV_p$.
The couplings are set per configuration $(m, L, N)$ from the free ground
state: $\hat\lambda_1$ and $\hat\lambda_2$ make the first-order
pseudo-potential $\max_y\max(\frac{15}{16}|\lambda S_p|, |v_x|)$ equal to
$0.1\,m$ and $1\,m$.  Excited states: the KS gap, the particle-hole list (holes
with $f > 10^{-12}$, particles with $f < 1 - 10^{-12}$; the rule of both
solvers) and $\Delta$SCF, the self-consistent state with one particle moved
from the HOMO to the LUMO, $E_1 - E_0$.

### 4.8 The energy-momentum tensor of the Kohn-Sham state

Evaluated on the Kohn-Sham orbitals with the expectation rule (Stage-2
formulas, reduced exactly in the theory file), with $L_s = e_H + e_x$ the
on-shell interaction Lagrangian:
$\rho(y) = \sum f(\varepsilon - v_v)n - \frac{\lambda}{2}S_p^2 - v_sS_p + e_x$,
$p_y = \sum f(\varepsilon n - ms - \kappa k t) - e_H - e_x$,
$p_3 = \sum f\bigl(\frac13\kappa k t + (M_\text{eff}-m)s + v_v n\bigr) - e_H - e_x$ and
$p_t = \sum f\bigl((M_\text{eff}-m)s + v_v n\bigr) - e_H - e_x$
($n$, $s$, $t$: number, scalar and $k$-current densities per orbital).  Two
exact consequences are checked from the profiles: $\int\rho\,dV_p = E$, and the
conservation law $p_y' + 6Hp_y - 3Hp_3 - 3Hp_t = 0$.
"""))

# ===========================================================================
# 5. How this notebook talks to the solver
# ===========================================================================
CELLS.append(md(r"""
## 5. How this notebook talks to the solver

### 5.1 Reading the committed outputs

The next cell only **reads files**.  It locates the repository (the folder
that contains `studies/dirac16complex_kohn_sham`), loads the exact theory
(`kohn-sham-theory.json`, `exchange-table.json`), the `summary.json` of every
subcommand of the Rust program, the `run.json` of every run, and the tables
`excitations.csv`, `thermodynamics.csv`, `emt-summary.csv` and
`closed-shells-m1-L3.csv`.  A file that is absent or unreadable (for example
a summary that is being regenerated) is recorded as such and reported by the
gauntlet as a SKIP, never as a pass.  The same cell is executed by the
notebook builder to fill in the numbers quoted in this text.
"""))

CELLS.append(code(DATA_CODE))

CELLS.append(md(r"""
### 5.2 The driver: finding and running the program

`find_binary()` locates the built program (environment variable
`DIRAC16KS_BIN` first, then
`studies/dirac16complex_kohn_sham/target/release/dirac16complex_kohn_sham`,
`.exe` on Windows; otherwise it tells you to build it).  `run()` starts one
subcommand from the repository root, streams everything the program prints
into the cell output, and raises an error unless the process exits with code
0 **and** its last printed line is `SUCCESS` (the planet_Mercury contract).
The cell also sets up the deterministic figure writer (`save_figure`: Agg
backend, `dpi=DPI`, `metadata={"Software": None}`, then the SHA-256 of the PNG
is printed) and the dictionaries `NB` (the notebook's own recomputed
measurements) and `SKIPPED` (checks whose inputs are absent).  Finally the
program recites its configuration (`print-config`): what is verified below is
what the program says it runs, not a number remembered by hand.
"""))

CELLS.append(code(r'''
import subprocess
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

CRATE = REPO / "studies" / "dirac16complex_kohn_sham"
_out_env = os.environ.get("DIRAC16KS_NB_OUTPUT", "")
OUT = Path(_out_env).resolve() if _out_env else (REPO / "build" / "notebook-kohn-sham").resolve()
FIGDIR.mkdir(parents=True, exist_ok=True)


def find_binary():
    env = os.environ.get("DIRAC16KS_BIN", "")
    if env and Path(env).is_file():
        return Path(env)
    names = (("dirac16complex_kohn_sham.exe", "dirac16complex_kohn_sham")
             if os.name == "nt" else ("dirac16complex_kohn_sham",))
    for name in names:
        candidate = CRATE / "target" / "release" / name
        if candidate.is_file():
            return candidate
    raise RuntimeError("dirac16complex_kohn_sham binary not found - build it first: "
                       "scripts/setup_solver.ps1 (or scripts/setup_solver.sh), then "
                       "cd studies/dirac16complex_kohn_sham && cargo build --release")


RUNS = []


def _stream(command, label):
    proc = subprocess.Popen(command, cwd=str(REPO), stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                            text=True, encoding="utf-8", bufsize=1)
    lines = []
    for line in proc.stdout:
        print(line, end="")
        lines.append(line.rstrip("\n"))
    proc.wait()
    RUNS.append({"command": label, "exit": proc.returncode, "last": lines[-1] if lines else ""})
    return proc.returncode, lines


def run(*args, output=None):
    command = [str(find_binary()), *args]
    if output is not None:
        command += ["--output", str(output)]
    code, lines = _stream(command, "dirac16complex_kohn_sham " + " ".join(args))
    if code != 0 or not lines or lines[-1] != "SUCCESS":
        raise RuntimeError(f"dirac16complex_kohn_sham {' '.join(args)} ended in FAILURE (exit {code}) "
                           "- read the output above")
    return lines


NB = {}          # the notebook's own recomputed measurements
SKIPPED = {}     # check name -> why it could not be computed

# ---- deterministic figures --------------------------------------------------------
PALETTE = ["#2a78d6", "#eb6834", "#1baf7a", "#eda100", "#e87ba4", "#008300", "#4a3aa7", "#e34948"]
INK, INK2, MUTED = "#0b0b0b", "#52514e", "#898781"
GRID, AXIS, SURFACE = "#e1e0d9", "#c3c2b7", "#fcfcfb"
plt.rcParams.update({
    "figure.facecolor": SURFACE, "axes.facecolor": SURFACE, "savefig.facecolor": SURFACE,
    "axes.edgecolor": AXIS, "axes.labelcolor": INK2, "axes.titlecolor": INK,
    "xtick.color": INK2, "ytick.color": INK2, "text.color": INK,
    "axes.grid": True, "grid.color": GRID, "grid.linewidth": 0.6,
    "axes.spines.top": False, "axes.spines.right": False,
    "font.size": 8.5, "axes.titlesize": 9.5, "axes.titleweight": "bold",
    "legend.frameon": False, "legend.fontsize": 7.5,
    "lines.linewidth": 1.6, "lines.markersize": 4,
    "axes.prop_cycle": matplotlib.cycler(color=PALETTE),
    "svg.hashsalt": "dirac16complex",
})
DPI = 100
FIGURES = []


def show_png(path):
    hook = globals().get("__nb_display_png__")      # provided by notebooks/run_notebook.py
    if hook is not None:
        hook(str(path))
        return
    try:
        get_ipython  # noqa: F821 - defined inside a Jupyter kernel
    except NameError:
        return
    from IPython.display import Image, display
    display(Image(filename=str(path)))


def save_figure(fig, name):
    path = FIGDIR / name
    fig.savefig(path, dpi=DPI, metadata={"Software": None})
    plt.close(fig)
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    FIGURES.append({"file": path.relative_to(REPO).as_posix(), "sha256": digest, "bytes": path.stat().st_size})
    print(f"figure {name} sha256 {digest}")
    show_png(path)


def simpson(y, values):
    """Composite Simpson rule on a uniform grid; with an odd number of intervals the last
    interval is a trapezoid (the convention of the program's own quadrature, shooting.rs)."""
    n = len(y) - 1
    assert n >= 2, "at least two intervals"
    h = (y[-1] - y[0]) / n
    m = n - (n % 2)                                  # intervals covered by Simpson pairs
    w = np.zeros(n + 1)
    w[0:m + 1:2] = 2.0
    w[1:m:2] = 4.0
    w[0] = 1.0
    w[m] = 1.0
    total = float(np.dot(w, values) * h / 3.0)
    if m < n:
        total += 0.5 * h * float(values[-2] + values[-1])
    return total


def rel(a, b):
    return abs(a - b) / max(abs(a), abs(b), 1e-300)


binary = find_binary()
print("repository : found (the folder that contains studies/dirac16complex_kohn_sham;"
      " its name is not printed, so the output does not depend on it)")
print("program    :", binary.relative_to(REPO).as_posix() if binary.is_relative_to(REPO) else binary)
print("fresh runs :", "DIRAC16KS_NB_OUTPUT" if _out_env else "build/notebook-kohn-sham",
      "| committed outputs: artifacts/dirac16complex/kohn-sham/rust")
CONFIG_LINES = run("print-config")
CONFIG = {k.strip(): v.strip() for k, v in (line.split("=", 1) for line in CONFIG_LINES if "=" in line)}
'''))

CELLS.append(md(r"""
### 5.3 Re-running the spectrum subcommand

The `spectrum` subcommand is the cheapest part of the program (about a minute
on 24 threads): it re-derives the geometry and the exact block reduction,
checks the exchange closed form against the tabulated uniform gas, computes
the free spectra for $m\in\{1,3\}$, $L\in\{2,3,4\}$, the closed shells and the
couplings, and compares with the exact theory file.  The next cell runs it
into the scratch folder and compares **every file it lists** byte for byte
with the committed copy.  The heavier subcommands (`scf`, `excited`,
`thermo`, `emt`; hours in total) are not re-run here: their committed outputs
are read, and their reproducibility is the job of
`rust/determinism-report.json` (a repeat run byte-identical, a
refined-tolerance run converged), whose verdict the gauntlet asserts.
"""))

CELLS.append(code(r'''
FRESH = None
if os.environ.get("DIRAC16KS_NB_SPECTRUM", "1") == "0":
    SKIPPED["fresh_spectrum_byte_identical"] = "the spectrum re-run was switched off (DIRAC16KS_NB_SPECTRUM=0)"
    print("spectrum re-run skipped (DIRAC16KS_NB_SPECTRUM=0)")
else:
    OUT.mkdir(parents=True, exist_ok=True)
    SPECTRUM_LINES = run("spectrum", output=OUT)
    names = list(SPEC["files"])
    same = [n for n in names if (OUT / "spectrum" / n).is_file()
            and (OUT / "spectrum" / n).read_bytes() == (RUST / "spectrum" / n).read_bytes()]
    FRESH = {"files": len(names), "identical": len(same), "different": sorted(set(names) - set(same))}
    print(f"\n{len(same)}/{len(names)} freshly written spectrum files are byte-identical to "
          f"artifacts/dirac16complex/kohn-sham/rust/spectrum/" +
          (f"; different: {FRESH['different']}" if FRESH["different"] else ""))
'''))

# ===========================================================================
# 6. The exact reduction and the pseudo-potential, checked in numbers
# ===========================================================================
CELLS.append(md(r"""
## 6. The exact reduction and the pseudo-potential, checked in numbers

### 6.1 The explicit 2x2 block basis

The next cell loads the exact integer gamma matrices of the algebra fixture
(`artifacts/dirac16complex/arbitrary-field/algebra-fixture.json`), re-verifies
the Clifford relations and $B = -iC\gamma^4$, reads the explicit basis of the
theory file (sixteen columns $v_+, v_-$ per block, Gaussian integers with
$|v|^2 = 8$, $v_- = \gamma^0\gamma^1 v_+$), normalises it by $1/\sqrt8$ and
checks, in floating point: that it is unitary; that
$\gamma^0$, $\gamma^0\gamma^1$, $\gamma^0\gamma^4$, $B$, $C$, $BC$,
$\gamma^4\gamma^1$ and $J = \gamma^0\gamma^1\gamma^4$ are block-diagonal in it;
that every 2x2 block equals both the matrix stored per block in the theory
file and the closed formula with the block labels $(j, s_2)$; and that the
full 16-component operator of the reduced equation,
$\gamma^0\bigl[M - i\kappa k\gamma^1 + i(\varepsilon - v)\gamma^4\bigr]$,
becomes $M\sigma_3 - \kappa k\sigma_2 + ij(\varepsilon - v)\sigma_1$ in every
block (for random values of $M$, $\kappa k$, $\varepsilon - v$).  The figure
shows the pattern: the $y$-current matrix $\gamma^0\gamma^4$ in the original
basis and in the block basis, and the full operator in the block basis.
"""))

CELLS.append(code(r'''
from fractions import Fraction

FIX = load_json(FIXTURE)
FIX_SHA = sha256(FIXTURE)
GAMMA = np.array(FIX["gamma"], dtype=float)                        # gamma^a, a = 0..7
CMAT = np.array(FIX["C"], dtype=float)                             # C = sigma16
BMAT = np.array(FIX["B"]["real"], dtype=float) + 1j * np.array(FIX["B"]["imag"], dtype=float)
ETA = np.diag([1.0, 1.0, 1.0, 1.0, -1.0, -1.0, -1.0, -1.0])
I16 = np.eye(16)
G0, G1, G4 = GAMMA[0], GAMMA[1], GAMMA[4]
ALG = {
    "clifford": max(np.abs(GAMMA[a] @ GAMMA[b] + GAMMA[b] @ GAMMA[a] - 2 * ETA[a, b] * I16).max()
                    for a in range(8) for b in range(8)),
    "C_is_gamma0123": np.abs(GAMMA[0] @ GAMMA[1] @ GAMMA[2] @ GAMMA[3] - CMAT).max(),
    "B_is_minus_i_C_gamma4": np.abs(-1j * CMAT @ G4 - BMAT).max(),
    "B_squared_is_1": np.abs(BMAT @ BMAT - I16).max(),
}


def gauss(entry):
    """[re, im] rational strings -> complex."""
    return complex(float(Fraction(entry[0])), float(Fraction(entry[1])))


BD = THEORY["reduction"]["blockDiagonalisation"]
BASIS_INT = np.array([[gauss(e) for e in row] for row in BD["basisMatrixUnnormalised"]])
U = BASIS_INT / math.sqrt(8.0)
BLOCKS = BD["blocks"]
OPS = {"A0": G0, "A1": G0 @ G1, "A4": G0 @ G4, "B": BMAT, "C": CMAT, "BC": BMAT @ CMAT,
       "gamma4gamma1": G4 @ G1, "J": G0 @ G1 @ G4}
S1 = np.array([[0, 1], [1, 0]], dtype=complex)
S2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
S3 = np.array([[1, 0], [0, -1]], dtype=complex)
I2 = np.eye(2, dtype=complex)


def closed_form(name, j, s2):
    return {"A0": S3, "A1": -1j * S2, "A4": j * S1, "B": j * s2 * I2, "C": s2 * S2, "BC": j * S2,
            "gamma4gamma1": -j * S3, "J": j * I2}[name]


def block(T, b):
    return T[2 * b:2 * b + 2, 2 * b:2 * b + 2]


mask = np.kron(np.eye(8), np.ones((2, 2))) > 0
unitary = np.abs(U.conj().T @ U - I16).max()
off_block, vs_theory, vs_formula = 0.0, 0.0, 0.0
for name, X in OPS.items():
    T = U.conj().T @ X @ U
    off_block = max(off_block, np.abs(T[~mask]).max())
    for b, blk in enumerate(BLOCKS):
        j, s2 = int(blk["j"]), int(blk["s2"])
        if name in blk:
            stored = np.array([[gauss(e) for e in row] for row in blk[name]])
            vs_theory = max(vs_theory, np.abs(block(T, b) - stored).max())
        vs_formula = max(vs_formula, np.abs(block(T, b) - closed_form(name, j, s2)).max())

rng = np.random.default_rng(20260930)
ode_dev = 0.0
for _ in range(5):
    M, kk, ev = rng.normal(size=3)
    N16 = G0 @ (M * I16 - 1j * kk * G1 + 1j * ev * G4)
    T = U.conj().T @ N16 @ U
    off_block = max(off_block, np.abs(T[~mask]).max())
    for b, blk in enumerate(BLOCKS):
        j = int(blk["j"])
        ode_dev = max(ode_dev, np.abs(block(T, b) - (M * S3 - kk * S2 + 1j * j * ev * S1)).max())
NB.update(alg_max=max(ALG.values()), basis_unitary=unitary, basis_off_block=off_block,
          basis_vs_theory=vs_theory, basis_vs_formula=vs_formula, block_ode=ode_dev,
          block_types=sorted({int(b["j"]) for b in BLOCKS}),
          blocks_per_type={jj: sum(int(b["j"]) == jj for b in BLOCKS) for jj in (1, -1)})

fmt = {1: "1", -1: "-1", 1j: "i", -1j: "-i", 0: "0"}
print("fixture sha256:", FIX_SHA)
for key, value in ALG.items():
    print(f"algebra check {key:24s} max deviation = {value:.1e}")
print("\nblock basis (theory file): column 2b = v+, 2b+1 = v- of block b; entries x 1/sqrt(8)")
for b, blk in enumerate(BLOCKS):
    for c, tag in ((2 * b, "v+"), (2 * b + 1, "v-")):
        entries = " ".join(f"{fmt[complex(v)]:>2s}" for v in BASIS_INT[:, c])
        print(f"block {b} (j={int(blk['j']):+d}, s2={int(blk['s2']):+d}, s3={int(blk['s3']):+d}) {tag}: [{entries}]")
print(f"\nunitary: max|U^dag U - 1| = {unitary:.1e}")
print(f"largest off-block entry over {len(OPS)} operators and 5 random ODE matrices: {off_block:.1e}")
print(f"blocks vs the theory file's stored 2x2 matrices: {vs_theory:.1e}")
print(f"blocks vs the closed forms (A0 = s3, A1 = -i s2, A4 = j s1, B = j s2, C = s2 s2, BC = j s2, g4g1 = -j s3, J = j): {vs_formula:.1e}")
print(f"block ODE matrix M s3 - kk s2 + i j (eps - v) s1: {ode_dev:.1e}")
print("block types j:", NB["block_types"], "| blocks per type:", NB["blocks_per_type"])

seq = matplotlib.colors.LinearSegmentedColormap.from_list("seq", [SURFACE, PALETTE[0]])
fig, axes = plt.subplots(1, 3, figsize=(10.5, 3.6))
M_demo, kk_demo, ev_demo = 1.0, 0.7, 0.4
panels = [(np.abs(G0 @ G4), "gamma^0 gamma^4 (y-current), original basis"),
          (np.abs(U.conj().T @ G0 @ G4 @ U), "gamma^0 gamma^4 in the block basis"),
          (np.abs(U.conj().T @ (G0 @ (M_demo * I16 - 1j * kk_demo * G1 + 1j * ev_demo * G4)) @ U),
           "reduced-equation operator, block basis")]
for ax, (mat, title) in zip(axes, panels):
    ax.imshow(mat, cmap=seq, vmin=0, vmax=max(1.0, mat.max()))
    ax.set_title(title, fontsize=8.5)
    ax.set_xticks(range(0, 16, 2))
    ax.set_yticks(range(0, 16, 2))
    ax.grid(False)
    for b in range(1, 8):
        ax.axhline(2 * b - 0.5, color=GRID, lw=0.5)
        ax.axvline(2 * b - 0.5, color=GRID, lw=0.5)
axes[0].set_ylabel("row (spinor component)")
for ax in axes:
    ax.set_xlabel("column")
fig.suptitle("Eight 2x2 blocks: |matrix entries| (white = 0); operator shown for M = 1, kappa k = 0.7, eps - v = 0.4",
             fontsize=9)
fig.tight_layout()
save_figure(fig, "block_structure.png")
'''))

q("ex_rows_d4", "{:d}", 'len(EXTABLE["tables"]["d4"]["rows"])')
q("ex_rows_d3", "{:d}", 'len(EXTABLE["tables"]["d3"]["rows"])')
q("ex_tmax", "{:.1f}", 'max(EXTABLE["tables"]["d4"]["temperatureGrid"])')

CELLS.append(md(r"""
### 6.2 The exchange closed form against the tabulated uniform gas

`exchange-table.json` (written by the independent sympy/mpmath checker
`scripts/check_dirac16complex_kohn_sham_theory.py`) tabulates the uniform
8-fold gas at densities $n$ from $10^{-4}$ to $10^3$ and temperatures $T$
from 0 to «ex_tmax» $m$: «ex_rows_d4» rows for momenta in the four spatial
directions of the Kohn-Sham problem (`d4`, the primary table, $n$ in $m^4$)
and «ex_rows_d3» rows for 3-space momenta only (`d3`).  Each row holds the
chemical potential, the scalar density $S_u(n, T)$, and the exchange energy
density $e_x/\lambda$ from the full double momentum quadrature of the
Hartree-Fock exchange kernel.  The cell recomputes the closed form
$-(n^2 + S^2)/32$ from the tabulated $n$ and $S$ and compares it with the
quadrature, checks the LDA potentials $v_v/\lambda = -n/16$,
$v_s/\lambda = -S/16$ and the $n$-only variant
$v_x/\lambda = -(n + S\,dS/dn)/16$, and the rest-gas limit ($S\to n$,
$e_x\to -e_H/8$).  The exact identity is what the Kohn-Sham programs use.
"""))

CELLS.append(code(r'''
def table_rows(dim):
    t = EXTABLE["tables"][dim]
    return {c: np.array([r[c] for r in t["rows"]], dtype=float) for c in t["columns"] if c != "momentsErrorEstimate"}


EXT = {dim: table_rows(dim) for dim in ("d4", "d3")}
ex_dev = {}
for dim, t in EXT.items():
    closed = -(t["n"] ** 2 + t["S"] ** 2) / 32.0
    ex_dev[dim] = {
        "quadrature_vs_closed": float(np.max(np.abs(t["exOverLambda_quadrature"] - closed) / np.abs(closed))),
        "table_closed_column": float(np.max(np.abs(t["exOverLambda_closedForm"] - closed) / np.abs(closed))),
        "v_v": float(np.max(np.abs(t["vvOverLambda"] + t["n"] / 16.0) / (t["n"] / 16.0))),
        "v_s": float(np.max(np.abs(t["vsOverLambda"] + t["S"] / 16.0) / np.maximum(t["S"] / 16.0, 1e-300))),
        "v_x_n_only": float(np.max(np.abs(t["vxOverLambda_nOnly"] + (t["n"] + t["S"] * t["dSdn"]) / 16.0)
                                   / ((t["n"] + t["S"] * t["dSdn"]) / 16.0))),
    }
    print(dim, {k: f"{v:.1e}" for k, v in ex_dev[dim].items()})
t4 = EXT["d4"]
rest = (t4["T"] == 0.0) & (t4["n"] == t4["n"].min())
ratio_rest = float((-t4["exOverLambda_quadrature"][rest] / (t4["S"][rest] ** 2 / 2.0))[0])
NB.update(ex_quadrature=max(d["quadrature_vs_closed"] for d in ex_dev.values()),
          ex_potentials=max(max(d["v_v"], d["v_s"], d["v_x_n_only"], d["table_closed_column"]) for d in ex_dev.values()),
          ex_rest_ratio=ratio_rest, ex_rest_S_over_n=float((t4["S"][rest] / t4["n"][rest])[0]))
print(f"rest-gas limit (T = 0, n = {t4['n'].min():g}): S/n = {NB['ex_rest_S_over_n']:.6f}, "
      f"-e_x/e_H = {ratio_rest:.6f} (1/8 = 0.125 exactly as S -> n)")
print(f"Rust cross-check of the same table: {SPEC['exchangeTable']['status'][:60]}...")

fig, axes = plt.subplots(1, 2, figsize=(10, 3.8))
for i, T in enumerate((0.0, 0.3, 1.0, 2.0)):
    sel = t4["T"] == T
    axes[0].loglog(t4["n"][sel], (t4["n"][sel] ** 2 + t4["S"][sel] ** 2) / 32.0, color=PALETTE[i], lw=1.4,
                   label=f"closed form, T = {T:g} m")
    axes[0].loglog(t4["n"][sel], -t4["exOverLambda_quadrature"][sel], "o", ms=3.5, mfc="none",
                   color=PALETTE[i])
axes[0].set_xlabel("number density n  [m^4]")
axes[0].set_ylabel("-e_x / lambda  [m^8]")
axes[0].set_title("Uniform 8-fold gas: exchange energy density (markers: quadrature)")
axes[0].legend(loc="upper left")
for i, dim in enumerate(("d4", "d3")):
    t = EXT[dim]
    closed = -(t["n"] ** 2 + t["S"] ** 2) / 32.0
    dev = np.abs(t["exOverLambda_quadrature"] - closed) / np.abs(closed)
    axes[1].semilogy(np.arange(len(dev)), np.maximum(dev, 1e-18), "o", ms=2.5, color=PALETTE[i],
                     label=f"table {dim} ({len(dev)} rows)")
axes[1].axhline(1e-12, color=MUTED, lw=1, ls="--")
axes[1].text(2, 1.6e-12, "1e-12", color=INK2, fontsize=7.5)
axes[1].set_xlabel("table row (T outer, n inner)")
axes[1].set_ylabel("|quadrature - closed form| / |closed form|")
axes[1].set_title("e_x = -(lambda/32)(n^2 + S^2) holds at every n and T")
axes[1].legend(loc="upper right")
fig.tight_layout()
save_figure(fig, "exchange_uniform_gas.png")
'''))

# ===========================================================================
# 7. The free spectrum
# ===========================================================================
q("gap8_L2", "{:.7f}", 'SCF["m1_L2_N8_lam0_T0"]["ksGap"]')
q("gap8_L4", "{:.7f}", 'SCF["m1_L4_N8_lam0_T0"]["ksGap"]')
q("c_rust", "{:.10f}", 'float(AGREE["checks"]["theory_zero_mode_splitting"]["detail"].split(") = ")[1].split()[0])')
q("free_rows_m1L3", "{:d}", 'len(load_csv(RUST / "spectrum" / "free-spectrum-m1-L3.csv")["eps"])')

CELLS.append(md(r"""
## 7. The free spectrum ($\lambda = 0$) and its analytic checks

`rust/spectrum/free-spectrum-m{1,3}-L{2,3,4}.csv` list every level of the
free problem in the window $|\varepsilon| < 4\,m$ for the shells
$n_2 \le 16$ (columns `n2`, `k`, `multiplicity`, `parity`, `s`, Pruefer
`index`, `eps`, the scalar and pressure charges and the shooting residuals;
«free_rows_m1L3» rows for $m = 1$, $L = 3$).  The next cell checks them
against four exact statements:

1. **The $k = 0$ box spectrum.**  Parity +: $\varepsilon = 0$ and
   $\pm\sqrt{M^2 + (n\pi/L)^2}$; parity -: $\pm\sqrt{M^2 + p^2}$ with
   $\tan(pL) = -p/M$ (roots found here by bisection).  Every $k = 0$ row of
   all six files is matched.
2. **The chiral zero mode and its splitting.**  The zero mode is exactly
   $\varepsilon = 0$ with vanishing scalar charge.  Its slope $d\varepsilon/dk$
   at $k\to0$ is recomputed **independently in the cell**: a vectorised
   fourth-order Runge-Kutta shooting of the real block system
   $a' = Ma + (s\varepsilon - \kappa k)b$, $b' = -(s\varepsilon + \kappa k)a - Mb$
   from the tip ($b(-L) = 0$) to the brane ($b(0) = 0$) at $k = 10^{-4}$,
   with a secant search for $\varepsilon$; it is compared with the closed
   form $c$ of section 4.5 for all six $(m, L)$ and both block types, and the
   sign identifies the solvers' label $s$ as $-j$.  (The torus shells
   $k\ge0.25\,m$ are far from the linear regime at $m = 1$: there
   $\kappa(-L)k = e^{L}k$ is of order 5, which is why the slope is measured at
   $k = 10^{-4}$ and not read off the band.)  The program's own
   Hellmann-Feynman slope is «c_rust» against the theory value «c_theory».
3. **Mirror spectra (E4.4).**  At fixed $(n_2, \text{parity})$ the $s = -1$
   levels are the negated $s = +1$ levels.
4. **Multiplicities.**  Every row carries $4\times r_3(n_2)$ states, $r_3$ the
   number of lattice vectors with $n_x^2 + n_y^2 + n_z^2 = n_2$ (counted here
   by brute force): each level is 4-fold per block type at fixed $\vec k$.

The KS gap of the $N = 8$ ground state (the zero modes filled, the first
brane-band shell empty) converges quickly with the cutoff: «gap8_L2»,
«gap8_L3», «gap8_L4» $m$ for $L = 2, 3, 4$.  The figure shows the free
spectrum ($m = 1$, $L = 3$) and, for comparison, the self-consistent spectrum
of the strongly repulsive $N$ = «n_mid», $+\hat\lambda_2$ ground state, per
parity and block type.
"""))

CELLS.append(code(r'''
FREE = {(m, L): load_csv(RUST / "spectrum" / f"free-spectrum-m{m}-L{L}.csv") for m in (1, 3) for L in (2, 3, 4)}
H = 1.0


def box_levels(M, L, parity, emax):
    """Exact k = 0 levels (eps >= 0 branch) of the constant-mass block with the tip bag b(-L) = 0."""
    out = [0.0] if parity == 1 else []
    n = 1
    while True:
        if parity == 1:
            p = n * math.pi / L
        else:                                   # M sin(pL) + p cos(pL) = 0 in ((n - 1/2) pi/L, n pi/L)
            lo, hi = (n - 0.5) * math.pi / L + 1e-15, n * math.pi / L - 1e-15
            g = lambda p: M * math.sin(p * L) + p * math.cos(p * L)
            for _ in range(200):
                mid = 0.5 * (lo + hi)
                if g(lo) * g(mid) <= 0:
                    hi = mid
                else:
                    lo = mid
            p = 0.5 * (lo + hi)
        eps = math.sqrt(M * M + p * p)
        if eps > emax:
            return np.array(out)
        out.append(eps)
        n += 1


box_dev, box_count_bad, zero_dev = 0.0, 0, 0.0
for (m, L), d in FREE.items():
    emax = float(np.max(np.abs(d["eps"])))
    for parity in (1, -1):
        exact = box_levels(float(m), float(L), parity, emax)
        exact = np.concatenate([-exact[exact > 0][::-1], exact])
        for s in (1, -1):
            sel = (d["n2"] == 0) & (d["parity"] == parity) & (d["s"] == s)
            got = np.sort(d["eps"][sel])
            if len(got) != len(exact):
                box_count_bad += 1
                continue
            box_dev = max(box_dev, float(np.max(np.abs(got - exact))))
    zm = (d["n2"] == 0) & (d["parity"] == 1) & (np.abs(d["eps"]) < 1e-6)
    zero_dev = max(zero_dev, float(np.max(np.abs(d["eps"][zm]))), float(np.max(np.abs(d["scalar_charge"][zm]))))
    assert zm.sum() == 2, "one zero mode per block type"
NB.update(box_dev=box_dev, box_count_bad=box_count_bad, zero_mode=zero_dev)
print(f"k = 0 box spectrum: max |eps_Rust - eps_exact| = {box_dev:.2e} over 6 (m, L) x 2 parities x 2 types; "
      f"count mismatches {box_count_bad}; zero modes |eps|, |scalar charge| <= {zero_dev:.1e}")


def c_closed(M, L, a4=0.0):
    return math.exp(-a4) * (2 * M / (2 * M - H)) * (1 - math.exp(-(2 * M - H) * L)) / (1 - math.exp(-2 * M * L))


def shoot(eps, M, k, L, s, steps=4000):
    """Vectorised RK4 of a' = M a + (s eps - kappa k) b, b' = -(s eps + kappa k) a - M b from
    y = -L (a, b) = (1, 0) to y = 0; returns b(0)/|(a, b)(0)| (zero on a parity + level)."""
    h = L / steps
    y, a, b = -L.copy(), np.ones_like(eps), np.zeros_like(eps)

    def f(y, a, b):
        kk = np.exp(-H * y) * k
        return M * a + (s * eps - kk) * b, -(s * eps + kk) * a - M * b
    for _ in range(steps):
        k1a, k1b = f(y, a, b)
        k2a, k2b = f(y + h / 2, a + h / 2 * k1a, b + h / 2 * k1b)
        k3a, k3b = f(y + h / 2, a + h / 2 * k2a, b + h / 2 * k2b)
        k4a, k4b = f(y + h, a + h * k3a, b + h * k3b)
        a = a + h / 6 * (k1a + 2 * k2a + 2 * k3a + k4a)
        b = b + h / 6 * (k1b + 2 * k2b + 2 * k3b + k4b)
        y = y + h
    return b / np.hypot(a, b)


cases = [(m, L, s) for m in (1, 3) for L in (2, 3, 4) for s in (1, -1)]
Mv = np.array([c[0] for c in cases], dtype=float)
Lv = np.array([c[1] for c in cases], dtype=float)
sv = np.array([c[2] for c in cases], dtype=float)
kq = 1e-4
e0, e1 = np.full(len(cases), -1e-5), np.full(len(cases), 1e-5)
g0, g1 = shoot(e0, Mv, kq, Lv, sv), shoot(e1, Mv, kq, Lv, sv)
for _ in range(30):                              # secant iteration, all cases at once
    e2 = e1 - g1 * (e1 - e0) / (g1 - g0)
    e0, g0, e1 = e1, g1, e2
    g1 = shoot(e1, Mv, kq, Lv, sv)
    if np.max(np.abs(e1 - e0)) < 1e-16:
        break
slope = e1 / kq
c_ref = np.array([c_closed(m, L) for m, L, s in cases])
NB["c_shoot"] = float(np.max(np.abs(np.abs(slope) - c_ref) / c_ref))
NB["s_is_minus_j"] = bool(np.all(np.sign(slope) == -sv))
NB["c_rust_vs_closed"] = abs(float(AGREE["checks"]["theory_zero_mode_splitting"]["detail"].split(") = ")[1].split()[0]) + c_closed(1, 3))
for (m, L, s), sl, cr in zip(cases, slope, c_ref):
    print(f"m = {m}, L = {L}, s = {s:+d}: d eps0/dk (RK4 shooting, k = 1e-4) = {sl:+.9f}   closed form c = {cr:.9f}")
print(f"max relative deviation {NB['c_shoot']:.1e}; slope sign = -s in every case (s = -j): {NB['s_is_minus_j']}")


def r3(n2):
    r = int(math.isqrt(n2))
    return sum(1 for a in range(-r, r + 1) for b in range(-r, r + 1) for c in range(-r, r + 1)
               if a * a + b * b + c * c == n2)


mirror_dev, mirror_bad, mult_bad = 0.0, 0, 0
for (m, L), d in FREE.items():
    emax = float(np.max(np.abs(d["eps"])))
    for n2 in sorted(set(d["n2"].astype(int))):
        rows = d["n2"] == n2
        mult_bad += int(np.any(d["multiplicity"][rows] != 4 * r3(n2)))
        for parity in (1, -1):
            a = np.sort(d["eps"][rows & (d["parity"] == parity) & (d["s"] == 1)])
            b = np.sort(-d["eps"][rows & (d["parity"] == parity) & (d["s"] == -1)])
            inner = lambda x: x[np.abs(x) < emax - 0.05]
            a, b = inner(a), inner(b)
            if len(a) != len(b):
                mirror_bad += 1
                continue
            if len(a):
                mirror_dev = max(mirror_dev, float(np.max(np.abs(a - b))))
NB.update(mirror_dev=mirror_dev, mirror_bad=mirror_bad, mult_bad=mult_bad)
print(f"mirror spectra s = -1 vs -(s = +1): max deviation {mirror_dev:.1e}, count mismatches {mirror_bad}; "
      f"multiplicity != 4 r3(n2) in {mult_bad} shells")

d = FREE[(1, 3)]
INT_LABEL = "m1_L3_N112_lamp2_T0"
lv = levels("scf", INT_LABEL)
fig, axes = plt.subplots(2, 2, figsize=(10, 7.2), sharex=True, sharey=True)
kline = np.linspace(0, 0.3, 50)
for row, parity in enumerate((1, -1)):
    for col, (src, title) in enumerate(((d, "free, m = 1, L = 3"),
                                        (lv, f"self-consistent {INT_LABEL} (+lambda_hat_2)"))):
        ax = axes[row, col]
        for i, (s, marker) in enumerate(((1, "o"), (-1, "^"))):
            sel = (src["parity"] == parity) & (src["s"] == s) & (np.abs(src["eps"]) < 3.0)
            ax.plot(src["k"][sel] + (0.006 if s < 0 else -0.006), src["eps"][sel], marker, ms=3.4,
                    mfc="none", color=PALETTE[i], label=f"block type s = {s:+d} (j = {-s:+d})")
        if parity == 1 and col == 0:
            c13 = c_closed(1, 3)
            ax.plot(kline, c13 * kline, "--", color=MUTED, lw=1)
            ax.plot(kline, -c13 * kline, "--", color=MUTED, lw=1)
            ax.text(0.31, c13 * 0.3, "+-c k", color=INK2, fontsize=7.5, va="center")
        if col == 1:
            ax.axhline(SCF[INT_LABEL]["mu"], color=PALETTE[2], lw=1, ls=":")
            ax.text(1.0, SCF[INT_LABEL]["mu"] + 0.05, "mu", color=INK2, fontsize=7.5, ha="right")
        ax.set_title(f"parity {'+' if parity == 1 else '-'}: {title}", fontsize=8.5)
        if row == 1:
            ax.set_xlabel("k  [m]  (shells k^2 = (0.25 m)^2 n2)")
        if col == 0:
            ax.set_ylabel("eps  [m]")
axes[0, 0].legend(loc="lower left")
fig.suptitle("Kohn-Sham spectrum eps_n(k) per parity and block type (|eps| < 3 m; the two types offset by +-0.006 in k)",
             fontsize=9)
fig.tight_layout()
save_figure(fig, "ks_spectrum.png")
'''))

# ===========================================================================
# 8. Ground states: densities and the pseudo-potential
# ===========================================================================
q("n_scf_runs", "{:d}", 'len(SCF)')
q("lh1_8", "{:.4e}", 'lam_hat(8, "lamp1")')
q("lh1_112", "{:.4e}", 'lam_hat(112, "lamp1")')
q("lh1_1016", "{:.4e}", 'lam_hat(1016, "lamp1")')
q("maxlamS_112p2", "{:.2f}", 'SCF["m1_L3_N112_lamp2_T0"]["maxLambdaSOverM"]')
q("maxvx_112p2", "{:.2f}", 'SCF["m1_L3_N112_lamp2_T0"]["maxVxOverM"]')

CELLS.append(md(r"""
## 8. Ground states: densities and the pseudo-potential

The `scf` subcommand wrote «n_scf_runs» self-consistent runs
(`rust/scf/<label>/`: `levels.csv` every Kohn-Sham level with its occupation
and weight, `profiles.csv` the densities, potentials and energy-momentum
tensor on the 301-point grid, `history.csv` the iteration history, `run.json`
the energies and diagnostics).  The couplings are per configuration:
$\hat\lambda_1$ = «lh1_8», «lh1_112», «lh1_1016» for $N = 8$, «n_mid»,
«n_large» ($m = 1$, $L = 3$; $\hat\lambda_2 = 10\hat\lambda_1$).  One global
coupling cannot serve all $N$: the proper densities near the tip grow like
$e^{6HL}$ and with $N$.

For **every** scf, thermo and emt run the next cell recomputes from the files:

* $N$ from the level weights, $\sum_n\text{mult}_n w_n$, and from the density,
  $\ell^3\int n_p e^{6Hy}dy$ (Simpson);
* $E_H$, $E_x$ from the profiles and $E = \sum\text{mult}\,w\,\varepsilon - E_H - E_x$
  from the levels, against `run.json`;
* the pseudo-potential formulas $M_\text{eff} = m + \frac{15}{16}\lambda S_p$ and
  $v_x = -\frac{\lambda}{16}n_p$ on the grid (the written potentials are those
  of the last iteration, so the difference measures the self-consistency);
* the columns $n_c = e^{6Hy}n_p$, the volume factor $e^{6Hy}$ and $z = \arcsin e^{6Hy}$.

The figure shows the densities per unit $y$ ($n_c$) and per proper volume
($n_p$), the scalar density $S_p$, the pseudo-potential pair
$(M_\text{eff} - m, v_x)$ for the strongest couplings, and the HOMO orbital
$|\chi|^2$ against the notebook's own coordinate $z = 6Hx_0$.  The strongest
repulsive $N$ = «n_mid» run reaches $\max|\lambda S_p|/m$ = «maxlamS_112p2»
and $\max|v_x|/m$ = «maxvx_112p2».
"""))

CELLS.append(code(r'''
def check_run(sub, label, r):
    """In-cell recomputations for one run directory; returns a dict of deviations."""
    p = r["parameters"]
    P = load_csv(RUST / sub / label / "profiles.csv")
    lv = levels(sub, label)
    lam, vol, m, N = p["lambda"], p["ell"] ** 3, p["m"], p["N"]
    y, vf = P["y"], P["volume_factor"]
    scale = max(abs(r["energy"]), N * m)
    n_w = float(np.sum(lv["multiplicity"] * lv["weight"]))
    n_d = simpson(y, P["n_p"] * vf) * vol
    e_h = simpson(y, 0.5 * lam * P["S_p"] ** 2 * vf) * vol
    e_x = simpson(y, -lam / 32.0 * (P["n_p"] ** 2 + P["S_p"] ** 2) * vf) * vol
    ks = float(np.sum(lv["multiplicity"] * lv["weight"] * lv["eps"]))
    pot = max(float(np.max(np.abs(P["M_eff"] - m))), float(np.max(np.abs(P["v_x"]))), 1e-300)
    meff_dev = np.abs(P["M_eff"] - (m + 15.0 / 16.0 * lam * P["S_p"]))
    out = {
        "N_weights": abs(n_w - N) / N,
        "N_density": abs(n_d - N) / N,
        "N_density_vs_rust": abs(n_d - r["nFromDensity"]) / N,
        "E_H": abs(e_h - r["hartreeEnergy"]) / scale,
        "E_x": abs(e_x - r["exchangeEnergy"]) / scale,
        "ksSum": abs(ks - r["ksSum"]) / scale,
        "E": abs(ks - e_h - e_x - r["energy"]) / scale,
        "M_eff": float(np.max(meff_dev)) / pot if lam else float(np.max(meff_dev)),
        "M_eff_at_y": float(y[int(np.argmax(meff_dev))]),
        "v_x": float(np.max(np.abs(P["v_x"] + lam * P["n_p"] / 16.0))) / pot if lam else float(np.max(np.abs(P["v_x"]))),
        "columns": max(float(np.max(np.abs(vf - np.exp(6 * H * y)))),
                       float(np.max(np.abs(P["n_c"] - P["n_p"] * vf)) / max(np.max(np.abs(P["n_c"])), 1e-300)),
                       float(np.max(np.abs(P["z"] - np.arcsin(np.exp(6 * H * y)))))),
    }
    return out, P, lv


RECOMP = {}
PROFILES = {}
for sub, runs in (("scf", SCF), ("thermo", THERMO), ("emt", EMT)):
    for label, r in runs.items():
        RECOMP[(sub, label)], PROFILES[(sub, label)], _ = check_run(sub, label, r)
worst = {}
for key, dev in RECOMP.items():
    for name, value in dev.items():
        if name.endswith("_at_y"):
            continue
        if value >= worst.get(name, (-1.0, None))[0]:
            worst[name] = (value, "/".join(key))
NB["recompute"] = {name: value for name, (value, _) in worst.items()}
print(f"recomputed {len(RECOMP)} runs (scf {len(SCF)}, thermo {len(THERMO)}, emt {len(EMT)}); worst deviations:")
for name, (value, where) in sorted(worst.items()):
    print(f"  {name:20s} {value:.2e}  at {where}")
where = worst["M_eff"][1].split("/")
print(f"the largest pseudo-potential mismatch sits at y = {RECOMP[tuple(where)]['M_eff_at_y']:+.2f} "
      "(towards the tip the proper densities carry the factor e^(-6Hy) of the convergence residual)")

SERIES_N = {8: PALETTE[0], 112: PALETTE[1], 1016: PALETTE[2]}
fig, axes = plt.subplots(2, 3, figsize=(12, 7))
for N, color in SERIES_N.items():
    P = PROFILES[("scf", f"m1_L3_N{N}_lam0_T0")]
    axes[0, 0].semilogy(P["y"], np.maximum(P["n_c"], 1e-30), color=color, label=f"N = {N}")
    axes[0, 1].semilogy(P["y"], np.maximum(P["n_p"], 1e-30), color=color, label=f"N = {N}")
    axes[1, 2].plot(P["z"], P["homo_a"] ** 2 + P["homo_b"] ** 2, color=color, label=f"N = {N} HOMO")
for N in (112, 1016):
    for name, ls in (("lam0", "-"), ("lamp2", "--"), ("lamm2", ":")):
        P = PROFILES[("scf", f"m1_L3_N{N}_{name}_T0")]
        axes[0, 2].plot(P["y"], P["S_p"], ls, color=SERIES_N[N], label=f"N = {N}, {name}")
for N in (8, 112, 1016):
    for name, ls in (("lamp2", "--"), ("lamm2", ":")):
        P = PROFILES[("scf", f"m1_L3_N{N}_{name}_T0")]
        axes[1, 0].plot(P["y"], P["M_eff"] - 1.0, ls, color=SERIES_N[N], label=f"N = {N}, {name}")
        axes[1, 1].plot(P["y"], P["v_x"], ls, color=SERIES_N[N], label=f"N = {N}, {name}")
axes[0, 0].set_title("n_c = e^{6Hy} n_p: particles per unit y")
axes[0, 1].set_title("n_p: proper number density")
axes[0, 2].set_title("S_p: proper scalar density")
axes[0, 2].set_yscale("symlog", linthresh=1e-2)
axes[1, 0].set_title("M_eff - m = (15/16) lambda S_p   [m]")
axes[1, 1].set_title("v_x = -(lambda/16) n_p   [m]")
axes[1, 2].set_title("HOMO orbital |chi|^2 against z = 6Hx0")
for ax in axes.flat[:5]:
    ax.set_xlabel("y  (brane at 0, tip cutoff at -L = -3)")
axes[1, 2].set_xlabel("z = arcsin(e^{6Hy})  (brane at pi/2)")
axes[1, 2].set_ylabel("a^2 + b^2 (normalised: int dy = 1)")
for ax in axes.flat:
    ax.legend(loc="best", fontsize=6.5)
fig.suptitle("Self-consistent ground states, m = 1, L = 3 (solid: lambda = 0, dashed: +lambda_hat_2, dotted: -lambda_hat_2)",
             fontsize=9.5)
fig.tight_layout()
save_figure(fig, "density_profiles.png")
'''))

CELLS.append(md(r"""
### 8.1 Self-consistency histories

`history.csv` records, per Anderson iteration, the density residuals
$\max|\Delta n_c|/D$ and $\max|\Delta S_c|/D$ ($D = \max(\max|n_c|, \max|S_c|)$),
$\mu$, $E$, $F$ and the work done.  The figure shows the residual for the
strongest couplings.  The attractive $N$ = «n_large» run needed the coupling
continuation of section 10.2 (its history restarts at every continuation step).
"""))

CELLS.append(code(r'''
HIST = {label: load_csv(RUST / "scf" / label / "history.csv") for label in SCF}
fig, axes = plt.subplots(1, 2, figsize=(10, 3.8), sharey=True)
for ax, name, sign in ((axes[0], "lamp2", "+"), (axes[1], "lamm2", "-")):
    for N, color in SERIES_N.items():
        h = HIST[f"m1_L3_N{N}_{name}_T0"]
        ax.semilogy(h["iteration"], np.maximum(h["residual_n"], 1e-16), "o-", ms=2.5, color=color,
                    label=f"N = {N} ({len(h['iteration'])} iterations)")
    ax.axhline(1e-10, color=MUTED, ls="--", lw=1)
    ax.text(0.5, 1.6e-10, "tolerance 1e-10", color=INK2, fontsize=7.5)
    ax.set_title(f"{sign}lambda_hat_2: density residual max|dn_c|/D")
    ax.set_xlabel("iteration")
    ax.legend(loc="upper right")
axes[0].set_ylabel("residual")
fig.tight_layout()
save_figure(fig, "scf_history.png")
conv = {label: (r["converged"], r["finalResidualN"], r["finalResidualS"]) for label, r in SCF.items()}
NB["scf_all_converged"] = all(c[0] and c[1] < 1e-10 and c[2] < 1e-10 for c in conv.values())
print(f"all {len(conv)} scf runs converged with both residuals < 1e-10: {NB['scf_all_converged']}")
'''))

# ===========================================================================
# 9. Ground-state energy against N
# ===========================================================================
CELLS.append(md(r"""
## 9. The ground-state energy against $N$

At $\lambda = 0$ the ground-state energy of a closed shell is the sum of the
lowest $N$ particle levels.  The next cell performs this aufbau **in the
cell**, from `free-spectrum-m1-L3.csv` alone: it sorts the particle levels
($\varepsilon \ge 0$; the $k = 0$ zero modes count as particles, the negative
brane band $-ck$ as Dirac sea), finds every closed shell whose top lies below
the lowest level of the largest shell in the file (the brane band rises with
$k$, so no level of an absent shell can come lower), and compares the shell
list with `closed-shells-m1-L3.csv` and $E_0(N)$ with the self-consistent
$\lambda = 0$ runs ($m = 1$ and $m = 3$).  For the interacting runs it
compares $E_0(\hat\lambda) - E_0(0)$ with the first-order (Hellmann-Feynman)
value $\lambda\,\partial E/\partial\lambda|_0 = \lambda\int[S_p^2/2 - (n_p^2+S_p^2)/32]dV_p$
evaluated on the free densities.
"""))

CELLS.append(code(r'''
def aufbau(d):
    """Closed shells of the free spectrum: [(N, eps_homo, E0)] below the guard."""
    part = d["eps"] >= -1e-12
    eps, mult = d["eps"][part], d["multiplicity"][part]
    order = np.argsort(eps, kind="stable")
    eps, mult = eps[order], mult[order]
    top_shell = d["n2"].max()
    guard = float(np.min(d["eps"][(d["n2"] == top_shell) & part]))
    shells, count, energy, i = [], 0.0, 0.0, 0
    while i < len(eps):
        j = i
        while j + 1 < len(eps) and eps[j + 1] - eps[i] <= 1e-9:
            j += 1
        if eps[j] >= guard:
            break
        count += float(np.sum(mult[i:j + 1]))
        energy += float(np.sum(mult[i:j + 1] * eps[i:j + 1]))
        shells.append((count, float(eps[j]), energy))
        i = j + 1
    return shells, guard


SHELLS, GUARD = aufbau(FREE[(1, 3)])
SHELLS3, GUARD3 = aufbau(FREE[(3, 3)])
cs = {int(n): e for n, e in zip(CLOSED_SHELLS["N"], CLOSED_SHELLS["eps_homo"])}
mine = {int(n): e for n, e, _ in SHELLS}
common = sorted(set(cs) & set(mine))
missing = [n for n in cs if cs[n] < GUARD and n not in mine]
NB["shell_list_dev"] = max(abs(cs[n] - mine[n]) for n in common)
NB["shell_list_missing"] = missing
E0_free = {int(n): E for n, _, E in SHELLS}
E0_free3 = {int(n): E for n, _, E in SHELLS3}
e0_dev = []
for m, table in ((1, E0_free), (3, E0_free3)):
    for N in (8, 112, 1016):
        label = f"m{m}_L3_N{N}_lam0_T0"
        if label in SCF and N in table:
            e0_dev.append(abs(SCF[label]["energy"] - table[N]) / max(abs(table[N]), N * m))
            print(f"{label}: aufbau E0 = {table[N]:.9f}   scf E0 = {SCF[label]['energy']:.9f}")
NB["aufbau_E0"] = max(e0_dev)
print(f"closed shells below the guard eps < {GUARD:.4f} m: {len(common)} match closed-shells-m1-L3.csv "
      f"(max |d eps_homo| = {NB['shell_list_dev']:.1e}); missing {missing}; max relative |E0 aufbau - E0 scf| = {NB['aufbau_E0']:.1e}")


def first_order(N, m=1, L=3):
    """lambda-derivative of E at lambda = 0 per unit lambda: int [S^2/2 - (n^2 + S^2)/32] dV_p (free densities)."""
    r = SCF[f"m{m}_L{L}_N{N}_lam0_T0"]
    P = PROFILES[("scf", f"m{m}_L{L}_N{N}_lam0_T0")]
    vf = P["volume_factor"]
    return simpson(P["y"], (0.5 * P["S_p"] ** 2 - (P["n_p"] ** 2 + P["S_p"] ** 2) / 32.0) * vf) * r["parameters"]["ell"] ** 3


FO = {}
for N in (8, 112, 1016):
    d1 = first_order(N)
    for name in LAMBDA_NAMES:
        label = f"m1_L3_N{N}_{name}_T0"
        lam = SCF[label]["parameters"]["lambda"]
        FO[(N, name)] = (SCF[label]["energy"] - SCF[f"m1_L3_N{N}_lam0_T0"]["energy"], lam * d1)
        if name != "lam0":
            de, est = FO[(N, name)]
            print(f"N = {N:5d} {name:6s}: E0(lambda) - E0(0) = {de:+.6e}   first order = {est:+.6e}   "
                  f"ratio {de / est:.4f}")
NB["first_order_lh1"] = max(abs(FO[(N, n)][0] / FO[(N, n)][1] - 1.0) for N in (8, 112, 1016) for n in ("lamp1", "lamm1"))

fig, axes = plt.subplots(1, 2, figsize=(10.5, 3.9))
Ns = np.array([n for n, _, _ in SHELLS])
axes[0].plot(Ns, [E for _, _, E in SHELLS], "o-", ms=3, color=PALETTE[0], label="free closed shells (aufbau in this cell)")
for i, name in enumerate(("lamp2", "lamm2")):
    xs = [N for N in (8, 112, 1016)]
    axes[0].plot(xs, [SCF[f"m1_L3_N{N}_{name}_T0"]["energy"] for N in xs], "s" if i == 0 else "^", ms=6,
                 mfc="none", color=PALETTE[1 + i], label=f"self-consistent, {name}")
axes[0].set_xscale("log")
axes[0].set_yscale("symlog", linthresh=1e-2)
axes[0].set_xlabel("N")
axes[0].set_ylabel("E_0  [m]")
axes[0].set_title("Ground-state energy, m = 1, L = 3")
axes[0].legend(loc="upper left")
xi = {"lamm2": -10, "lamm1": -1, "lam0": 0, "lamp1": 1, "lamp2": 10}
for N, color in SERIES_N.items():
    xs = [xi[n] for n in LAMBDA_NAMES]
    axes[1].plot(xs, [FO[(N, n)][0] for n in LAMBDA_NAMES], "o-", color=color, ms=4, label=f"N = {N}: self-consistent")
    axes[1].plot(xs, [FO[(N, n)][1] for n in LAMBDA_NAMES], "--", color=color, lw=1, label=f"N = {N}: first order")
axes[1].set_xscale("symlog", linthresh=1)
axes[1].set_yscale("symlog", linthresh=1e-4)
axes[1].set_xlabel("lambda_hat / lambda_hat_1  (-10, -1, 0, 1, 10)")
axes[1].set_ylabel("E_0(lambda) - E_0(0)  [m]")
axes[1].set_title("Interaction energy: SCF against first-order Hellmann-Feynman")
axes[1].legend(loc="upper left", fontsize=6.5)
fig.tight_layout()
save_figure(fig, "ground_state_energy.png")
'''))

# ===========================================================================
# 10. First excited states
# ===========================================================================
_rows = []
for _N in (8, 112, 1016):
    for _name in ("lamm2", "lamm1", "lam0", "lamp1", "lamp2"):
        _lab = f"m1_L3_N{_N}_{_name}_T0"
        q(f"ex_E0_{_N}_{_name}", "{:.6f}", f'exc("{_lab}", "E0")')
        q(f"ex_gap_{_N}_{_name}", "{:.7f}", f'exc("{_lab}", "ks_gap")')
        q(f"ex_dscf_{_N}_{_name}", "{:.7f}", f'exc("{_lab}", "delta_scf")')
        q(f"ex_lh_{_N}_{_name}", "{:+.4e}", f'exc("{_lab}", "lambda_hat")')
        _rows.append(f"| {_N} | `{_name}` | «ex_lh_{_N}_{_name}» | «ex_E0_{_N}_{_name}» | «ex_gap_{_N}_{_name}» "
                     f"| «ex_dscf_{_N}_{_name}» |")
EXC_TABLE_MD = "\n".join(_rows)

CELLS.append(md(r"""
## 10. First excited states: KS gap, particle-hole excitations and $\Delta$SCF

The `excited` subcommand re-solves the ground state of every $m = 1$, $L = 3$
configuration ($N$ = 8, «n_mid», «n_large»; five couplings each) and writes
`levels.csv` (the ground state), `particle-hole.csv` (the lowest 12
particle-hole excitations $\varepsilon_a - \varepsilon_i$),
`levels-excited.csv` (the $\Delta$SCF state: one particle moved from the HOMO
level to the LUMO level and the densities re-converged with these fixed
occupations) and the table `excitations.csv`:

| $N$ | coupling | $\hat\lambda$ | $E_0$ [m] | KS gap [m] | $\Delta$SCF $= E_1 - E_0$ [m] |
|---|---|---|---|---|---|
""" + EXC_TABLE_MD + r"""

(The `m1_L3_N1016_lamm2_T0` row is the smeared ensemble of section 10.2.)
The next cell recomputes from the level files: the KS gap
($\varepsilon_\text{LUMO} - \varepsilon_\text{HOMO}$, HOMO the highest particle
level with $f\ge\frac12$, LUMO the lowest with $f < \frac12$) against the run
records (`excited/summary.json`), the scf `run.json` and `excitations.csv`; $\Delta$SCF $= E_1 - E_0$; that the excited
subcommand's ground state is the scf ground state (same levels file, same
$E_0$); that the $\Delta$SCF state differs from the ground state by exactly
one particle moved upwards; and that $\Delta$SCF equals the KS gap at
$\lambda = 0$, where orbital relaxation vanishes.
"""))

CELLS.append(code(r'''
def gap_from_levels(lv):
    part = lv["branch"] > 0
    homo = float(np.max(lv["eps"][part & (lv["f"] >= 0.5)]))
    lumo = float(np.min(lv["eps"][part & (lv["f"] < 0.5)]))
    return lumo - homo, homo, lumo


def promoted(label):
    """(particles added, particles removed) between the ground state and the Delta-SCF state."""
    g = levels("excited", label)
    e = levels("excited", label, "levels-excited.csv")
    key = lambda d, i: (d["n2"][i], d["parity"][i], d["s"][i], d["index"][i])
    wg = {key(g, i): g["multiplicity"][i] * g["weight"][i] for i in range(len(g["eps"]))}
    we = {key(e, i): e["multiplicity"][i] * e["weight"][i] for i in range(len(e["eps"]))}
    diff = [we.get(k, 0.0) - wg.get(k, 0.0) for k in set(wg) | set(we)]
    return sum(x for x in diff if x > 1e-9), -sum(x for x in diff if x < -1e-9)


EXC = {}
for label in EXCITED_LABELS:
    rec = excited_record(label)
    gap, homo, lumo = gap_from_levels(levels("excited", label))
    twin = label in SCF
    same_levels = twin and ((RUST / "excited" / label / "levels.csv").read_bytes()
                            == (RUST / "scf" / label / "levels.csv").read_bytes())
    up, down = promoted(label)
    EXC[label] = {"gap": gap, "homo": homo, "lumo": lumo, "rec": rec, "row": excited_row(label) if twin else None,
                  "sameLevels": same_levels, "up": up, "down": down}
MAIN = {k: v for k, v in EXC.items() if v["row"] is not None}
NB["gap_vs_record"] = max(abs(v["gap"] - v["rec"]["ksGap"]) for v in EXC.values())
NB["gap_vs_run"] = max(abs(v["gap"] - SCF[k]["ksGap"]) for k, v in MAIN.items())
NB["gap_vs_table"] = max(abs(v["gap"] - v["row"]["ks_gap"]) for v in MAIN.values())
NB["dscf_identity"] = max(abs(v["rec"]["E1"] - v["rec"]["E0"] - v["rec"]["deltaScf"]) for v in EXC.values())
NB["record_vs_table"] = max(abs(v["rec"][a] - v["row"][b]) for v in MAIN.values()
                            for a, b in (("E0", "E0"), ("mu", "mu"), ("ksGap", "ks_gap"), ("deltaScf", "delta_scf"), ("E1", "E1")))
NB["excited_ground_is_scf"] = all(v["sameLevels"] and v["row"]["E0"] == SCF[k]["energy"] for k, v in MAIN.items())
NB["one_particle_promoted"] = max(max(abs(v["up"] - 1.0), abs(v["down"] - 1.0)) for v in EXC.values())
NB["dscf_equals_gap_free"] = max(abs(v["row"]["delta_scf"] - v["row"]["ks_gap"]) for k, v in MAIN.items()
                                 if parse_label(k)["lam"] == "lam0")
print(f"{len(EXC)} excited runs ({len(MAIN)} with an scf twin; records from "
      f"{'excited/summary.json' if SUMMARY['excited'] else 'excitations.csv (summary absent)'}): KS gap from levels vs "
      f"record {NB['gap_vs_record']:.1e}, vs scf run.json {NB['gap_vs_run']:.1e}, vs excitations.csv {NB['gap_vs_table']:.1e}")
print(f"records vs excitations.csv {NB['record_vs_table']:.1e}; E1 - E0 - DeltaSCF {NB['dscf_identity']:.1e}")
print(f"excited ground state = scf ground state (levels.csv byte-identical, same E0): {NB['excited_ground_is_scf']}")
print(f"Delta-SCF state = ground state with exactly one particle moved up: max deviation {NB['one_particle_promoted']:.1e}")
print(f"lambda = 0: |Delta-SCF - KS gap| <= {NB['dscf_equals_gap_free']:.1e}")
for label in EXCITED_EXTRA:
    v = EXC[label]
    print(f"additional run {label}: KS gap {v['rec']['ksGap']:.9f}, Delta-SCF {v['rec']['deltaScf']:.9f}, "
          f"E0 {v['rec']['E0']:.9f}, lowest particle-hole {v['rec']['lowestParticleHole']:.3e}")

xi = {"lamm2": -10, "lamm1": -1, "lam0": 0, "lamp1": 1, "lamp2": 10}
fig, axes = plt.subplots(1, 2, figsize=(10.5, 3.9))
for N, color in SERIES_N.items():
    labs = [f"m1_L3_N{N}_{n}_T0" for n in LAMBDA_NAMES]
    xs = [xi[n] for n in LAMBDA_NAMES]
    axes[0].plot(xs, [EXC[l]["row"]["ks_gap"] for l in labs], "o-", color=color, ms=4, label=f"N = {N}: KS gap")
    axes[0].plot(xs, [EXC[l]["row"]["delta_scf"] for l in labs], "s--", mfc="none", color=color, ms=6, lw=1,
                 label=f"N = {N}: Delta-SCF")
    axes[1].plot(xs, [EXC[l]["row"]["delta_scf"] - EXC[l]["row"]["ks_gap"] for l in labs], "o-", color=color, ms=4,
                 label=f"N = {N}")
sm = EXC[SMEARED]["row"]
axes[0].annotate("smeared ensemble\n(section 10.2)", xy=(-10, sm["ks_gap"]), xytext=(-6, 0.2), fontsize=7,
                 color=INK2, arrowprops={"arrowstyle": "->", "color": MUTED, "lw": 0.8})
for ax in axes:
    ax.set_xscale("symlog", linthresh=1)
    ax.set_xlabel("lambda_hat / lambda_hat_1  (-10, -1, 0, 1, 10)")
axes[0].set_yscale("log")
axes[0].set_ylabel("excitation energy  [m]")
axes[0].set_title("KS gap and Delta-SCF, m = 1, L = 3")
axes[0].legend(loc="center right", fontsize=6.5)
axes[1].set_yscale("symlog", linthresh=1e-6)
axes[1].set_ylabel("Delta-SCF - KS gap  [m]")
axes[1].set_title("Orbital relaxation (zero at lambda = 0)")
axes[1].legend(loc="upper left")
fig.tight_layout()
save_figure(fig, "ks_gap_delta_scf.png")
'''))

CELLS.append(md(r"""
### 10.1 The particle-hole lists

Both solvers form the particle-hole pairs of a $T = 0$ run with an
**occupation floor of $10^{-12}$**: a hole is a particle level with
$f > 10^{-12}$, a particle one with $f < 1 - 10^{-12}$ (a fractionally
occupied level belongs to both sets), a pair needs
$\varepsilon_\text{particle} > \varepsilon_\text{hole}$, and the lowest 12
excitations are listed.  For exact $T = 0$ occupations the floor changes
nothing; for the smeared run of section 10.2 it keeps the Fermi-Dirac tails
out of the list.  The next cell rebuilds every list from the ground-state
`levels.csv` with this rule and compares it entry by entry with
`particle-hole.csv` (and its first entry with the run record).
"""))

CELLS.append(code(r'''
ph_dev, ph_bad = 0.0, []
for label in EXCITED_LABELS:
    mine = particle_hole_list("excited", label)
    theirs = load_csv(RUST / "excited" / label / "particle-hole.csv")["excitation"]
    first = EXC[label]["rec"]["lowestParticleHole"]
    if len(mine) != len(theirs) or abs(first - theirs[0]) > 1e-12:
        ph_bad.append(label)
        continue
    dev = float(np.max(np.abs(mine - theirs)))
    ph_dev = max(ph_dev, dev)
    if dev > 1e-12:
        ph_bad.append(label)
    print(f"{label:26s} lowest excitations {mine[0]:.6e} {mine[1]:.6e} {mine[2]:.6e}   max |mine - file| = {dev:.1e}")
NB.update(ph_dev=ph_dev, ph_bad=ph_bad)
print(f"particle-hole lists recomputed: max deviation {ph_dev:.1e}; runs that differ: {ph_bad}")
'''))

q("band_k", "{:.3f}", 'BAND["k"]')
q("band_eps", "{:.4f}", 'BAND["eps"]')
q("band_mult", "{:.0f}", 'BAND["mult"]')
q("band_f", "{:.3f}", 'BAND["f"]')
q("k0_eps", "{:.4f}", 'KZERO["eps"]')
q("k0_mult", "{:.0f}", 'KZERO["mult"]')
q("k0_f", "{:.3f}", 'KZERO["f"]')
q("k0_rows", "{:d}", 'KZERO["rows"]')
q("moved", "{:.1f}", 'MOVED')
q("smear", "{:g}", 'par(SMEARED, "occupationSmearing")')
q("exact_occ", "{}", 'str(SCF[SMEARED]["exactZeroTemperatureOccupations"]).lower()')
q("fallback", "{:d}", 'par(SMEARED, "zeroTemperatureFallbackStage")')
q("sm_iter", "{:d}", 'SCF[SMEARED]["iterations"]')
q("sm_gap", "{:.6f}", 'exc(SMEARED, "ks_gap")')
q("sm_dscf", "{:.5f}", 'exc(SMEARED, "delta_scf")')
q("sm_lumo", "{:.4f}", 'float(np.min(levels("scf", SMEARED)["eps"][(levels("scf", SMEARED)["branch"] > 0) & (levels("scf", SMEARED)["f"] < 0.5)]))')
q("sm_ph0", "{:.1e}", 'PH_SMEARED[0]')
q("sm_ph1", "{:.2e}", 'PH_SMEARED[1]')
q("sm_cs_eps", "{:.4f}", '[e for n, e in zip(CLOSED_SHELLS["N"], CLOSED_SHELLS["eps_homo"]) if n == 1016][0]')
q("sm_F_minus_E", "{:.1e}", 'abs(SCF[SMEARED]["freeEnergy"] - SCF[SMEARED]["energy"])')

CELLS.append(md(r"""
### 10.2 The level-crossing run: $N$ = «n_large» at $-\hat\lambda_2$

At $N$ = «n_large» with the attractive coupling $-\hat\lambda_2$ the exact
$T = 0$ aufbau does **not** converge.  The aufbau count itself closes exactly:
the free closed shell $N$ = «n_large» ends with the «band_mult»-fold band at
$k$ = «band_k» $m$ (free $\varepsilon_\text{HOMO}$ = «sm_cs_eps» $m$,
`closed-shells-m1-L3.csv`).  Under self-consistency this band
($\varepsilon$ = «band_eps» $m$) and the «k0_mult»-fold $k = 0$ level
($\varepsilon$ = «k0_eps» $m$) **cross at the Fermi level**: whichever of the
two is filled last, the self-consistent potential it creates moves the other
one below it, so the exact-occupation iteration oscillates.  The ground state
was therefore converged with **occupation smearing** of «smear» $m$ at the
physical temperature $T = 0$ (`run.json`: `occupationSmearing` = «smear»,
`exactZeroTemperatureOccupations` = «exact_occ», `zeroTemperatureFallbackStage`
= «fallback»: coupling continuation with a smeared result, «sm_iter»
iterations in the last step), and its free energy is its energy ($|F - E|$ =
«sm_F_minus_E»).  The smeared ensemble moves about «moved» particles from the
band (occupation $f$ = «band_f») into the $k = 0$ level ($f$ = «k0_f»).

Everything reported for this run refers to that ensemble: its KS gap
(«sm_gap» $m$, from the fractionally occupied $k = 0$ level to the next level
at «sm_lumo» $m$) and its $\Delta$SCF («sm_dscf» $m$; the promoted particle
leaves the $k = 0$ level).  Its particle-hole list starts **inside** the
fractionally occupied levels: first a zero-energy rearrangement between the
two numerically split halves of the exactly degenerate $k = 0$ level (the
level is stored as «k0_rows» rows whose energies differ by round-off:
«sm_ph0» $m$ here, i.e. zero), then «sm_ph1» $m$ from the band into the
$k = 0$ level.  This is a level crossing of the self-consistent problem at
the Fermi level, not an open shell of the aufbau.
"""))

G601 = "m1_L3_N1016_lamm2_T0_g601"
if G601 in _namespace()["EXC_RECORDS"]:
    q("g601_gap", "{:.8f}", f'EXC_RECORDS["{G601}"]["ksGap"]')
    q("g601_dscf", "{:.7f}", f'EXC_RECORDS["{G601}"]["deltaScf"]')
    q("g301_gap", "{:.8f}", 'exc(SMEARED, "ks_gap")')
    q("g301_dscf", "{:.7f}", 'exc(SMEARED, "delta_scf")')
    q("g601_dscf_diff", "{:.1e}", f'abs(EXC_RECORDS["{G601}"]["deltaScf"] - exc(SMEARED, "delta_scf"))')
    q("g601_ph0", "{:.1e}", f'EXC_RECORDS["{G601}"]["lowestParticleHole"]')
    CELLS.append(md(r"""
The `excited` subcommand also solves this ensemble on the 601-point grid
(`m1_L3_N1016_lamm2_T0_g601`, a run without an scf twin): KS gap «g601_gap»
$m$ against «g301_gap» $m$ on 301 points, $\Delta$SCF «g601_dscf» $m$ against
«g301_dscf» $m$ (a change of «g601_dscf_diff» $m$: the grid sensitivity of
the promoted ensemble; section 15 compares both with the reference solver).
Its particle-hole list again starts with the round-off split of the $k = 0$
level («g601_ph0» $m$).
"""))

CELLS.append(code(r'''
lv0 = levels("scf", "m1_L3_N1016_lam0_T0")
lvs = levels("scf", SMEARED)
frac = fractional_levels("scf", SMEARED)
print("fractionally occupied particle levels of the smeared ensemble (floor 1e-12):")
for g in frac:
    print(f"  eps = {g['eps']:.10f} m, k = {g['k']:.6f} m, states = {g['mult']:.0f} ({g['rows']} rows), f = {g['f']:.6f}")
N_sm = float(np.sum(lvs["multiplicity"] * lvs["weight"]))
NB["smeared"] = {"N": N_sm, "moved": MOVED, "into_k0": KZERO["mult"] * KZERO["f"] - 0.0,
                 "k0_split": float(np.ptp(lvs["eps"][(lvs["n2"] == 0) & (np.abs(lvs["eps"] - KZERO["eps"]) < 1e-9)])),
                 "occ_band_and_k0": len(frac) == 2 and frac[0]["mult"] == BAND["mult"]}
filled_below = float(np.sum((lvs["multiplicity"] * lvs["weight"])[(lvs["branch"] > 0) & (lvs["eps"] < BAND["eps"] - 1e-9)]))
print(f"particles below the band {filled_below:.6f}; in the band {BAND['mult'] * BAND['f']:.6f}; in the k = 0 level "
      f"{KZERO['mult'] * KZERO['f']:.6f}; total {N_sm:.9f}")
print(f"the two rows of the k = 0 level differ by {NB['smeared']['k0_split']:.1e} m (the first particle-hole entry)")
NB["smeared"]["balance"] = abs(filled_below + BAND["mult"] * BAND["f"] + KZERO["mult"] * KZERO["f"] - N_sm)

fig, axes = plt.subplots(1, 2, figsize=(10.5, 4.0), sharey=True)
seq = matplotlib.colors.LinearSegmentedColormap.from_list("occ", ["#dce9f8", PALETTE[0], "#0b2e59"])
for ax, lv, title in ((axes[0], lv0, "free (lambda = 0), N = 1016: exact aufbau"),
                      (axes[1], lvs, f"{SMEARED}: smeared ensemble (T = 0, smearing 1e-3 m)")):
    sel = (lv["branch"] > 0) & (lv["eps"] > 1.25) & (lv["eps"] < 1.55)
    sc = ax.scatter(lv["k"][sel], lv["eps"][sel], c=lv["f"][sel], cmap=seq, vmin=0, vmax=1,
                    s=10 + 0.25 * lv["multiplicity"][sel], edgecolors=INK2, linewidths=0.4)
    ax.set_title(title, fontsize=8.5)
    ax.set_xlabel("k  [m]")
axes[0].set_ylabel("eps  [m]  (particle levels near the Fermi level)")
axes[1].axhline(SCF[SMEARED]["mu"], color=PALETTE[1], lw=1, ls="--")
axes[1].text(0.02, SCF[SMEARED]["mu"] + 0.004, "mu", color=INK2, fontsize=7.5)
axes[1].annotate(f"band k = {BAND['k']:.3f}: {BAND['mult']:.0f} states, f = {BAND['f']:.3f}",
                 xy=(BAND["k"], BAND["eps"]), xytext=(0.30, 1.30), fontsize=7, color=INK2,
                 arrowprops={"arrowstyle": "->", "color": MUTED, "lw": 0.8})
axes[1].annotate(f"k = 0 level: {KZERO['mult']:.0f} states, f = {KZERO['f']:.3f}",
                 xy=(0.0, KZERO["eps"]), xytext=(0.05, 1.50), fontsize=7, color=INK2,
                 arrowprops={"arrowstyle": "->", "color": MUTED, "lw": 0.8})
cb = fig.colorbar(sc, ax=axes, shrink=0.85, pad=0.02)
cb.set_label("occupation f")
fig.suptitle("The level crossing at the Fermi level (marker area ~ number of states)", fontsize=9.5)
save_figure(fig, "fermi_level_N1016_lamm2.png")
'''))

# ===========================================================================
# 11. Thermodynamics
# ===========================================================================
q("F_01", "{:.5f}", 'thermo_row(0, 8, 0.1)["F"]')
q("F_03", "{:.4f}", 'thermo_row(0, 8, 0.3)["F"]')
q("F_1", "{:.2f}", 'thermo_row(0, 8, 1.0)["F"]')
q("CV_01", "{:.2f}", 'thermo_row(0, 8, 0.1)["C_V"]')
q("CV_03", "{:.1f}", 'thermo_row(0, 8, 0.3)["C_V"]')
q("CV_1", "{:.4g}", 'thermo_row(0, 8, 1.0)["C_V"]')
q("states_T1", "{:.0f}", 'thermo_row(0, 8, 1.0)["states"]')
q("lh_hot", "{:.4e}", 'THERMO["m1_L3_N8_lamh_T1"]["parameters"]["lambdaHat"]')
q("lh_hot_S", "{:.3f}", 'THERMO["m1_L3_N8_lamh_T1"]["maxLambdaSOverM"]')
q("n_thermo", "{:d}", 'len(THERMO)')
q("fo_T1", "{:.0f}", 'SUMMARY["thermo"]["series"][0]["firstOrderPseudoPotential_lambdaHat1"][3] if SUMMARY["thermo"] else float("nan")')

CELLS.append(md(r"""
## 11. Thermodynamics: $F$, $E$, $S$, $C_V$ against $T$

The `thermo` subcommand solves Mermin's finite-temperature Kohn-Sham problem
for $N = 8$ and $N$ = «n_mid» at $T/m \in \{0, 0.1, 0.3, 1\}$ in three series
(«n_thermo» runs; `thermodynamics.csv`, column `series`): `lam0` (free),
`lamp1` (the $T = 0$ coupling $\hat\lambda_1$; its $T = m$ point is not run,
because the thermal pair plasma would push its first-order pseudo-potential
to about «fo_T1» $m$, far outside the window; recorded in
`thermo/summary.json: skippedRuns`) and `lamh` (a hot-calibrated coupling,
$\hat\lambda$ = «lh_hot» for $N = 8$, whose pseudo-potential reaches
$\max|\lambda S_p|/m$ = «lh_hot_S» at $T = m$).  Occupations are Fermi-Dirac
with thermal antiparticles (holes in the Dirac sea, weight $-(1-f)$); the
heat capacity is the self-consistent central difference $dE/dT|_N$ for
$T\le0.3\,m$ and the fixed-spectrum derivative above.

For $N = 8$ and $\lambda = 0$: $F$ = «F_01», «F_03», «F_1» $m$ and $C_V$ =
«CV_01», «CV_03», «CV_1» at $T/m$ = 0.1, 0.3, 1.  At $T = m$ the state is a
thermal particle-antiparticle plasma of «states_T1» Kohn-Sham levels; $N = 8$
and $N$ = «n_mid» then have nearly the same $E$, $F$ and $S$.  The
`levels.csv` of every thermo run is the Kohn-Sham quasi-particle excitation
spectrum at that temperature (the finite-$T$ excitation spectrum of the
specification); the last panel of the figure shows its occupations.

The next cell recomputes, for every run with $T > 0$, the entropy
$S = -\sum\text{mult}\,[f\ln f + (1-f)\ln(1-f)]$ from the levels, $F = E - TS$,
and (with section 8) $N$ and $E$; it checks that the two fixed-spectrum forms
of $C_V$ agree and that at $\lambda = 0$ the central difference agrees with the
fixed-spectrum value to its truncation error.
"""))

CELLS.append(code(r'''
TH = {}
for label, r in THERMO.items():
    T = r["parameters"]["T"]
    if T <= 0:
        continue
    lv = levels("thermo", label)
    f = lv["f"]
    ok = (f > 0) & (f < 1)
    S = float(-np.sum(lv["multiplicity"][ok] * (f[ok] * np.log(f[ok]) + (1 - f[ok]) * np.log1p(-f[ok]))))
    TH[label] = {"T": T, "S": S, "S_dev": abs(S - r["entropy"]) / max(r["entropy"], 1.0),
                 "F_dev": abs(r["energy"] - T * r["entropy"] - r["freeEnergy"]) / max(abs(r["energy"]), r["parameters"]["N"]),
                 "levels": len(f),
                 "lv": lv if label in ("m1_L3_N8_lam0_T0p1", "m1_L3_N8_lam0_T0p3", "m1_L3_N8_lam0_T1") else None}
NB["thermo_S"] = max(v["S_dev"] for v in TH.values())
NB["thermo_F"] = max(v["F_dev"] for v in TH.values())
t = THERMO_TABLE
fin = np.isfinite(t["C_V_fd"]) & (t["T"] > 0)
free = fin & (t["series"] == 0)
NB["cv_fixed_forms"] = float(np.nanmax(np.abs(t["C_V_fixed_spectrum"] - t["C_V_fixed_spectrum_entropy"])
                                       / np.maximum(np.abs(t["C_V_fixed_spectrum"]), 1e-300)))
NB["cv_fd_vs_fixed_free"] = float(np.max(np.abs(t["C_V_fd"][free] - t["C_V_fixed_spectrum"][free]) / t["C_V_fd"][free]))
NB["thermo_monotone"] = all(
    np.all(np.diff(t["F"][(t["series"] == s) & (t["N"] == N)]) < 0) and np.all(np.diff(t["S_entropy"][(t["series"] == s) & (t["N"] == N)]) > 0)
    for s in (0, 1, 2) for N in (8, 112))
print(f"{len(TH)} runs with T > 0: entropy from the levels vs run.json {NB['thermo_S']:.1e}; |E - TS - F| {NB['thermo_F']:.1e}")
print(f"C_V: the two fixed-spectrum forms agree to {NB['cv_fixed_forms']:.1e}; lambda = 0 central difference vs "
      f"fixed spectrum {NB['cv_fd_vs_fixed_free']:.1e} (truncation O(delta^2) of the central difference)")
print(f"F decreases and S increases with T in every series: {NB['thermo_monotone']}")
print("\nseries N    T      mu          E              F               S            C_V         KS gap")
for i in range(len(t["T"])):
    print(f"{int(t['series'][i]):4d} {int(t['N'][i]):4d} {t['T'][i]:5.2f} {t['mu'][i]:+.6f} {t['E'][i]:14.6f} "
          f"{t['F'][i]:15.6f} {t['S_entropy'][i]:12.4f} {t['C_V'][i]:12.4f} {t['ks_gap'][i]:.6f}")

fig, axes = plt.subplots(2, 3, figsize=(12, 6.8))
names = {0: "lam0", 1: "lamp1", 2: "lamh"}
markers = {0: "o-", 1: "s--", 2: "^:"}
for N, color in ((8, PALETTE[0]), (112, PALETTE[1])):
    for s in (0, 1, 2):
        sel = (t["series"] == s) & (t["N"] == N)
        for ax, col in zip(axes.flat[:5], ("E", "F", "S_entropy", "C_V", "ks_gap")):
            ax.plot(t["T"][sel], t[col][sel], markers[s], color=color, ms=4, mfc="none" if s else color,
                    label=f"N = {N}, {names[s]}")
for ax, title in zip(axes.flat[:5], ("E  [m]", "F = E - TS  [m]", "S (entropy)", "C_V = dE/dT", "KS gap  [m]")):
    ax.set_title(title)
    ax.set_xlabel("T  [m]")
    if title != "KS gap  [m]":
        ax.set_yscale("symlog", linthresh=1.0)
axes[0, 0].legend(loc="upper left", fontsize=6.5)
ax = axes[1, 2]
for i, label in enumerate(("m1_L3_N8_lam0_T0p1", "m1_L3_N8_lam0_T0p3", "m1_L3_N8_lam0_T1")):
    lv = TH[label]["lv"]
    order = np.argsort(lv["eps"])
    ax.plot(lv["eps"][order], lv["f"][order], ".", ms=1.5, color=PALETTE[i],
            label=f"T = {THERMO[label]['parameters']['T']:g} m, mu = {THERMO[label]['mu']:+.4f}")
ax.set_xlim(-4, 4)
ax.set_xlabel("eps  [m]  (sea levels eps < 0: holes = thermal antiparticles)")
ax.set_ylabel("occupation f")
ax.set_title("Finite-T excitation spectrum, N = 8, lambda = 0")
ax.legend(loc="lower left", fontsize=6.5, markerscale=5)
fig.suptitle("Mermin-Kohn-Sham thermodynamics, m = 1, L = 3 (filled: lam0; open: lamp1, lamh)", fontsize=9.5)
fig.tight_layout()
save_figure(fig, "thermodynamics.png")
'''))

# ===========================================================================
# 12. Energy-momentum tensor and the Einstein source
# ===========================================================================
q("wy_112", "{:.3f}", 'EMT["m1_L3_N112_lam0_T0"]["emt"]["wY"]')
q("wy_1016", "{:.3f}", 'EMT["m1_L3_N1016_lam0_T0"]["emt"]["wY"]')
q("w3_112", "{:.3f}", 'EMT["m1_L3_N112_lam0_T0"]["emt"]["w3"]')
q("w3_1016", "{:.3f}", 'EMT["m1_L3_N1016_lam0_T0"]["emt"]["w3"]')
q("rho_112", "{:.5f}", 'EMT["m1_L3_N112_lam0_T0"]["emt"]["rhoAvg"]')
q("rho_1016", "{:.4f}", 'EMT["m1_L3_N1016_lam0_T0"]["emt"]["rhoAvg"]')
q("rho_8p1", "{:.2e}", 'EMT["m1_L3_N8_lamp1_T0"]["emt"]["rhoAvg"]')
q("kappa_8p1", "{:.2e}", 'EMT["m1_L3_N8_lamp1_T0"]["emt"]["kappaNeeded"]')
q("kappa_8p1_mass", "{:.2e}", 'EMT["m1_L3_N8_lamp1_T0"]["emt"]["E41_sourcingConditions"]["kappaFromMassCondition"]')
q("lhneed_112", "{:.0f}", 'EMT["m1_L3_N112_lam0_T0"]["emt"]["E41_sourcingConditions"]["lambdaHatNeededFirstOrder"]')
q("lhneed_1016", "{:.1f}", 'EMT["m1_L3_N1016_lam0_T0"]["emt"]["E41_sourcingConditions"]["lambdaHatNeededFirstOrder"]')
q("n_emt", "{:d}", 'len(EMT)')
q("sp_112", "{:.3e}", 'EMT["m1_L3_N112_lam0_T0"]["emt"]["sPAvg"]')
q("sp_1016", "{:.3e}", 'EMT["m1_L3_N1016_lam0_T0"]["emt"]["sPAvg"]')
q("emt_met", "{:d}", 'sum(bool(r["emt"]["E41_sourcingConditions"]["met"]) for r in EMT.values())')

CELLS.append(md(r"""
## 12. The energy-momentum tensor and the Einstein source

The `emt` subcommand («n_emt» runs) evaluates the energy-momentum tensor of
the Kohn-Sham state (section 4.8) on the grid: $\rho$, $p_y$, $p_3$ (3-space,
rotationally averaged) and $p_t$ (extra times), their proper-volume averages
$\langle X\rangle = \int X e^{6Hy}dy/\int e^{6Hy}dy$, the ratios
$w_y = \langle p_y\rangle/\langle\rho\rangle$, $w_3$, $w_t$, and the comparison
with the source the geometry needs.  Without interaction $w_y$ = «wy_112»,
«wy_1016» and $w_3$ = «w3_112», «w3_1016» ($N$ = «n_mid», «n_large»); $p_t$
comes from the interaction alone ($p_t = L_s$).

**The mismatch with the required source.**  The geometry needs
$\rho_\text{req}$ = «rho_req» $H^2/\kappa < 0$ with $p_\text{req}$ = «p_req»
$H^2/\kappa$.  The Kohn-Sham states carry $\langle\rho\rangle$ = «rho_112»
($N$ = «n_mid») and «rho_1016» ($N$ = «n_large») $m^8$: positive, so
$G = \kappa T$ would need the negative coupling $\kappa$ = «kappa_112» and
«kappa_1016».  For $N = 8$ the specification's expectation of a positive
Kohn-Sham energy density fails (measured): the $k = 0$ zero modes have
$\varepsilon = 0$, so $\langle\rho\rangle = 0$ at $\lambda = 0$, and
$\langle\rho\rangle$ = «rho_8p1» at $+\hat\lambda_1$; this sign is compatible
with $\kappa > 0$ ($\kappa$ = «kappa_8p1»), but the first E4.1 condition
$mS = -36H^2/\kappa$ then needs $\kappa$ = «kappa_8p1_mass», of the opposite
sign.  The two static-field sourcing conditions of STAGE4_SPEC E4.1,
$mS = -36H^2/\kappa$ and $\lambda S^2 = 30H^2/\kappa$ (together
$\lambda S/m = -5/6$, $mS < 0$), are met in «emt_met» of the «n_emt» runs; at
first order they would need $\hat\lambda\approx$ «lhneed_112» ($N$ = «n_mid»)
or «lhneed_1016» ($N$ = «n_large»), $10^3$ to $10^4$ times $\hat\lambda_2$.
The average scalar density of these states is negative
($\langle S_p\rangle$ = «sp_112» and «sp_1016» $m^7$ at $\lambda = 0$): the
brane band $\varepsilon = +ck$ carries negative scalar charge, so the mass
condition alone would even give $\kappa > 0$, while $\langle\rho\rangle$ needs
$\kappa < 0$.

The next cell recomputes from `profiles.csv`, for every emt run: $\int\rho\,dV_p$
against $E$; the proper volume against its closed form
$\ell^3(1 - e^{-6HL})/(6H)$; the averages, the three $w$'s, the identity
$p_t = L_s = \frac{\lambda}{2}S_p^2 - \frac{\lambda}{32}(n_p^2 + S_p^2)$; the
conservation law $(e^{6Hy}p_y)' = 3He^{6Hy}(p_3 + p_t)$ with a fourth-order
stencil; $\kappa_\text{needed} = \rho_\text{req}/\langle\rho\rangle$ and the E4.1
quantities, against `run.json`.
"""))

CELLS.append(code(r'''
def conservation(P):
    y, vf = P["y"], P["volume_factor"]
    Py, P3, Pt = vf * P["p_y"], vf * P["p_3"], vf * P["p_t"]
    h = y[1] - y[0]
    dPy = (-Py[4:] + 8 * Py[3:-1] - 8 * Py[1:-3] + Py[:-4]) / (12 * h)
    res = dPy - 3.0 * H * (P3 + Pt)[2:-2]
    inner = slice(1, -1)
    scale = max(float(np.max(np.abs(dPy[inner]))), float(np.max(np.abs(3 * (P3 + Pt)[2:-2][inner]))),
                6.0 * float(np.max(np.abs(Py[2:-2][inner]))), 1e-300)
    return float(np.max(np.abs(res[inner])) / scale)


EMTR = {}
for label, r in EMT.items():
    p, e = r["parameters"], r["emt"]
    P = PROFILES[("emt", label)]
    y, vf, vol, lam, m, N = P["y"], P["volume_factor"], p["ell"] ** 3, p["lambda"], p["m"], p["N"]
    V = simpson(y, vf) * vol
    avg = {k: simpson(y, P[c] * vf) * vol / V for k, c in (("rho", "rho"), ("p_y", "p_y"), ("p_3", "p_3"),
                                                            ("p_t", "p_t"), ("S_p", "S_p"), ("n_p", "n_p"))}
    e_rho = simpson(y, P["rho"] * vf) * vol
    L_s = 0.5 * lam * P["S_p"] ** 2 - lam / 32.0 * (P["n_p"] ** 2 + P["S_p"] ** 2)
    rscale = max(float(np.max(np.abs(P["rho"]))), 1e-300)
    ww = {k: (avg[k] / avg["rho"] if avg["rho"] else 0.0) for k in ("p_y", "p_3", "p_t")}
    kappa = GEOM["rhoRequired_kappa1"] / avg["rho"] if avg["rho"] else 0.0
    lS = lam * avg["S_p"] / m
    k_mass = -36.0 / (m * avg["S_p"]) if avg["S_p"] else float("nan")
    k_coup = 30.0 / (lam * avg["S_p"] ** 2) if lam and avg["S_p"] else float("nan")
    s41 = e["E41_sourcingConditions"]
    EMTR[label] = {
        "E_rho": abs(e_rho - r["energy"]) / max(abs(r["energy"]), N * m),
        "volume": abs(V - vol * (1 - math.exp(-6 * H * p["L"])) / (6 * H)) / V,
        "averages": max(abs(avg["rho"] - e["rhoAvg"]), abs(avg["p_y"] - e["pYAvg"]), abs(avg["p_3"] - e["p3Avg"]),
                        abs(avg["p_t"] - e["pTAvg"])) / max(abs(avg["rho"]), abs(avg["p_y"]), 1e-300),
        "w": max(abs(ww["p_y"] - e["wY"]), abs(ww["p_3"] - e["w3"]), abs(ww["p_t"] - e["wT"])) if avg["rho"] else 0.0,
        "Ls": max(float(np.max(np.abs(P["L_s"] - L_s))), float(np.max(np.abs(P["p_t"] - P["L_s"])))) / rscale,
        "conservation": conservation(P),
        "kappa": abs(kappa - e["kappaNeeded"]) / max(abs(kappa), 1.0),
        "E41": (max(abs(lS - s41["lambdaSAvgOverM"]) / max(abs(lS), 1e-300),
                    rel(k_mass, s41["kappaFromMassCondition"]) if lam else 0.0) if avg["S_p"] else 0.0),
        "E41_met": bool(s41["met"]), "rho": avg["rho"], "kappaNeeded": kappa, "lambdaS": lS,
        "sign_S": int(np.sign(avg["S_p"])),
    }
NB["emt"] = {k: max(v[k] for v in EMTR.values()) for k in ("E_rho", "volume", "averages", "w", "Ls", "conservation",
                                                           "kappa", "E41")}
NB["emt_conservation_rust"] = max(r["emt"]["conservationResidualMax_normalised"] for r in EMT.values())
NB["emt_none_met"] = not any(v["E41_met"] for v in EMTR.values())
NB["emt_bulk_positive"] = all(v["rho"] > 0 for k, v in EMTR.items() if parse_label(k)["N"] > 8)
print(f"{len(EMTR)} emt runs; worst deviations: " + ", ".join(f"{k} {v:.1e}" for k, v in NB["emt"].items()))
print(f"<rho> > 0 for every N > 8 run: {NB['emt_bulk_positive']}; E4.1 conditions met in no run: {NB['emt_none_met']}")
print("\nrun                        <rho>          kappa needed    w_y      w_3     lambda<S_p>/m (need -5/6)")
for label, v in EMTR.items():
    e = EMT[label]["emt"]
    print(f"{label:26s} {v['rho']:+.6e} {v['kappaNeeded']:+.6e} {e['wY']:+.4f} {e['w3']:+.4f} {v['lambdaS']:+.3e}")

fig, axes = plt.subplots(2, 2, figsize=(11, 7))
for ax, label in ((axes[0, 0], "m1_L3_N112_lamp1_T0"), (axes[0, 1], "m1_L3_N1016_lamp1_T0")):
    P = PROFILES[("emt", label)]
    for i, (col, name) in enumerate((("rho", "rho"), ("p_y", "p_y"), ("p_3", "p_3 (3-space)"), ("p_t", "p_t (extra times)"))):
        ax.plot(P["y"], P[col], color=PALETTE[i], label=name)
    ax.set_yscale("symlog", linthresh=1e-3)
    ax.set_title(f"{label}: proper densities  [m^8]")
    ax.set_xlabel("y")
    ax.legend(loc="upper left")
ax = axes[1, 0]
for i, label in enumerate(("m1_L3_N112_lamp1_T0", "m1_L3_N1016_lamp1_T0")):
    P = PROFILES[("emt", label)]
    safe = np.where(P["rho"] != 0, P["rho"], np.nan)
    ax.plot(P["y"], P["p_y"] / safe, color=PALETTE[i], label=f"w_y(y), N = {parse_label(label)['N']}")
    ax.plot(P["y"], P["p_3"] / safe, "--", color=PALETTE[i], label=f"w_3(y), N = {parse_label(label)['N']}")
ax.axhline(15.0 / -21.0, color=PALETTE[7], lw=1, ls=":")
ax.text(-2.9, 15.0 / -21.0 + 0.05, "w_req = p_req/rho_req = -5/7", color=INK2, fontsize=7.5)
ax.set_ylim(-1.0, 1.1)
ax.set_title("local equation of state p/rho")
ax.set_xlabel("y")
ax.legend(loc="lower right", fontsize=6.5)
ax = axes[1, 1]
for i, label in enumerate(("m1_L3_N112_lamp1_T0", "m1_L3_N1016_lamp1_T0")):
    P = PROFILES[("emt", label)]
    ax.semilogy(P["y"], np.maximum(P["rho"] * P["volume_factor"], 1e-30), color=PALETTE[i],
                label=f"rho e^(6Hy), N = {parse_label(label)['N']}")
ax.set_title("where the energy sits: rho per unit y")
ax.set_xlabel("y")
ax.legend(loc="upper left")
fig.suptitle("Energy-momentum tensor of the Kohn-Sham ground state (+lambda_hat_1, m = 1, L = 3)", fontsize=9.5)
fig.tight_layout()
save_figure(fig, "emt_profiles.png")

labels = list(EMTR)
fig, axes = plt.subplots(1, 3, figsize=(12.5, 4.2), sharey=True)
ypos = np.arange(len(labels))
axes[0].plot([EMTR[l]["rho"] for l in labels], ypos, "o", color=PALETTE[0], label="<rho> of the KS state")
axes[0].axvline(GEOM["rhoRequired_kappa1"], color=PALETTE[7], ls="--", lw=1)
axes[0].text(GEOM["rhoRequired_kappa1"] * 0.8, len(labels) - 0.6, "rho_req (kappa = 1)", color=INK2, fontsize=7.5)
axes[0].set_xscale("symlog", linthresh=1e-7)
axes[0].set_title("proper-volume average <rho>  [m^8]")
axes[1].plot([EMTR[l]["kappaNeeded"] for l in labels], ypos, "s", color=PALETTE[1])
axes[1].axvline(0, color=MUTED, lw=1)
axes[1].set_xscale("symlog", linthresh=1.0)
axes[1].set_title("kappa = rho_req/<rho> it would need")
axes[2].plot([abs(EMTR[l]["lambdaS"]) for l in labels], ypos, "^", color=PALETTE[2], label="|lambda <S_p>/m|")
axes[2].axvline(5.0 / 6.0, color=PALETTE[7], ls="--", lw=1)
axes[2].text(5.0 / 6.0 * 0.05, len(labels) - 0.6, "E4.1 needs 5/6", color=INK2, fontsize=7.5)
axes[2].set_xscale("log")
axes[2].set_title("E4.1: |lambda <S_p>/m| against 5/6")
axes[0].set_yticks(ypos)
axes[0].set_yticklabels(labels, fontsize=7)
fig.suptitle("The Kohn-Sham state against the source the static field requires (rho_req = -21 H^2/kappa, p_req = +15 H^2/kappa)",
             fontsize=9.5)
fig.tight_layout()
save_figure(fig, "einstein_source.png")
'''))

# ===========================================================================
# 13. Brane localisation
# ===========================================================================
CELLS.append(md(r"""
## 13. Brane localisation

How much of the gas sits near the $Z_2$ brane?  The cumulative fraction
$F(d) = \int_{-d}^0 n_c\,dy \big/ \int_{-L}^0 n_c\,dy$ of the particles within
the proper distance $d$ of the brane is computed here from `profiles.csv` for
every scf run and compared at $d = 1/H$ with the program's
`braneFraction_within_1_over_H` (and at the other end with the fraction within
$1/H$ of the tip cutoff).  The zero modes $\chi = (e^{My}, 0)$ make the
localisation stronger for heavier fields: $n_c \propto e^{2My}$.
"""))

CELLS.append(code(r'''
def cumulative_fraction(P):
    y, nc = P["y"], P["n_c"]
    seg = 0.5 * (nc[1:] + nc[:-1]) * np.diff(y)                 # trapezoid pieces from the tip to the brane
    from_brane = np.concatenate([[0.0], np.cumsum(seg[::-1])])  # integral from -d to 0
    return -y[::-1], from_brane / from_brane[-1]


def fraction_within(P, d, tip=False):
    y, nc = P["y"], P["n_c"]
    total = simpson(y, nc)
    ii = (y <= y[0] + d + 1e-12) if tip else (y >= -d - 1e-12)
    return simpson(y[ii], nc[ii]) / total


bf_dev, tip_dev = 0.0, 0.0
for label, r in SCF.items():
    P = PROFILES[("scf", label)]
    bf_dev = max(bf_dev, abs(fraction_within(P, 1.0) - r["emt"]["braneFraction_within_1_over_H"]))
    tip_dev = max(tip_dev, abs(fraction_within(P, 1.0, tip=True) - r["emt"]["tipFraction_within_1_over_H_of_cutoff"]))
NB.update(brane_fraction=bf_dev, tip_fraction=tip_dev)
print(f"brane fraction within 1/H recomputed for {len(SCF)} scf runs: max deviation {bf_dev:.1e}; tip fraction {tip_dev:.1e}")

fig, axes = plt.subplots(1, 2, figsize=(10.5, 3.9))
for i, (label, name) in enumerate((("m1_L3_N8_lam0_T0", "N = 8, m = 1"), ("m1_L3_N112_lam0_T0", "N = 112, m = 1"),
                                   ("m1_L3_N1016_lam0_T0", "N = 1016, m = 1"), ("m3_L3_N112_lam0_T0", "N = 112, m = 3"))):
    d, F = cumulative_fraction(PROFILES[("scf", label)])
    axes[0].plot(d, F, color=PALETTE[i], label=f"{name}: F(1/H) = {SCF[label]['emt']['braneFraction_within_1_over_H']:.3f}")
axes[0].axvline(1.0, color=MUTED, ls="--", lw=1)
axes[0].set_xlabel("distance from the brane d = -y  [1/H]")
axes[0].set_ylabel("fraction of the particles within d")
axes[0].set_title("Cumulative brane localisation (lambda = 0, L = 3)")
axes[0].legend(loc="lower right", fontsize=7)
groups = [("m1_L3_N8", PALETTE[0]), ("m1_L3_N112", PALETTE[1]), ("m1_L3_N1016", PALETTE[2]), ("m3_L3_N112", PALETTE[3])]
for g, color in groups:
    labs = [l for l in SCF if l.startswith(g + "_lam") and l.endswith("_T0")]
    xs = [{"lamm2": -10, "lamm1": -1, "lam0": 0, "lamp1": 1, "lamp2": 10}[parse_label(l)["lam"]] for l in labs]
    order = np.argsort(xs)
    axes[1].plot(np.array(xs)[order], [SCF[labs[i]]["emt"]["braneFraction_within_1_over_H"] for i in order], "o-",
                 color=color, ms=4, label=g.replace("_", ", "))
axes[1].set_xscale("symlog", linthresh=1)
axes[1].set_xlabel("lambda_hat / lambda_hat_1")
axes[1].set_ylabel("fraction within 1/H of the brane")
axes[1].set_title("Brane fraction against the coupling")
axes[1].legend(loc="lower left", fontsize=7)
fig.tight_layout()
save_figure(fig, "brane_localisation.png")
'''))

# ===========================================================================
# 14. Convergence
# ===========================================================================
q("E_L2", "{:.6f}", 'SCF["m1_L2_N112_lam0_T0"]["energy"]')
q("E_L3", "{:.6f}", 'SCF["m1_L3_N112_lam0_T0"]["energy"]')
q("E_L4", "{:.6f}", 'SCF["m1_L4_N112_lam0_T0"]["energy"]')
q("E_g601_diff", "{:.1e}", 'abs(SCF["m1_L3_N112_lamp1_T0_g601"]["energy"] - SCF["m1_L3_N112_lamp1_T0"]["energy"])')
q("E_a4_diff", "{:.1e}", 'abs(SCF["m1_L3_N112_lamp1_T0_a40p5"]["energy"] - SCF["m1_L3_N112_lamp1rescaled_T0_dk0p15163266492815836"]["energy"])')
q("E_a4", "{:.6f}", 'SCF["m1_L3_N112_lamp1_T0_a40p5"]["energy"]')
q("det_files", "{:d}", 'DET["measurements"]["repeatFilesCompared"] if DET else -1')
q("det_refE", "{:.1e}", 'DET["measurements"]["refinedMaxRelativeEnergy"] if DET else float("nan")')
q("det_refEps", "{:.1e}", 'DET["measurements"]["refinedMaxAbsEps"] if DET else float("nan")')

CELLS.append(md(r"""
## 14. Convergence: tip cutoff $L$, grid, momentum lattice, $a_4$, tolerances

* **Tip cutoff $L$.**  The tip is a genuine singular end of the geometry
  ($W^6\to0$), so the problem is regularised by $L$.  The brane-localised
  ground state hardly notices it: for $N$ = «n_mid», $\lambda = 0$,
  $E_0$ = «E_L2», «E_L3», «E_L4» $m$ for $L = 2, 3, 4$, and the change from
  3 to 4 is far smaller than from 2 to 3 (the gauntlet asserts this trend for
  $E_0$ and the KS gap of all eight $L$-series runs).
* **Grid.**  The 601-point run of $N$ = «n_mid», $+\hat\lambda_1$ changes
  $E_0$ by «E_g601_diff» $m$ against the 301-point run.
* **Momentum lattice.**  `m1_L3_N896_lamp1_T0_dk0p125` halves $\Delta k$ at
  the same particle density (8 N particles on a torus 8 times larger); its
  energy per particle and brane fraction are printed below (different shells
  are filled, so it is a different finite system, not a refinement of the
  same one).
* **The $a_4$ rescaling.**  $a_4$ enters only through $\kappa = e^{-Hy-a_4}$,
  i.e. $k\to ke^{-a_4}$: the $a_4 = 0.5$ run and its exactly equivalent
  $a_4 = 0$ partner (torus larger by $e^{0.5}$ per side, $\hat\lambda_1e^{1.5}$)
  agree to «E_a4_diff» $m$ in $E_0$ («E_a4» $m$); the cell compares them level
  by level.
* **Tolerances and determinism.**  `rust/determinism-report.json`: a repeat
  run is byte-identical over «det_files» files; a run with all tolerances
  divided by 10 agrees to «det_refE» (relative, energies) and «det_refEps»
  $m$ (eigenvalues).  The gauntlet checks that this report still describes the
  committed summaries (its SHA-256 records).
"""))

CELLS.append(code(r'''
LSER = {}
print("series            L = 2          L = 3          L = 4         (E0 [m]; KS gap [m]; brane fraction)")
trend_ok = True
for N in (8, 112):
    for name in ("lam0", "lamp1"):
        labs = [f"m1_L{L}_N{N}_{name}_T0" for L in (2, 3, 4)]
        E = [SCF[l]["energy"] for l in labs]
        G = [SCF[l]["ksGap"] for l in labs]
        B = [SCF[l]["emt"]["braneFraction_within_1_over_H"] for l in labs]
        LSER[(N, name)] = (E, G, B)
        for X in (E, G):
            trend_ok = trend_ok and abs(X[2] - X[1]) <= abs(X[1] - X[0])
        print(f"N = {N:4d} {name:6s} E0 " + "  ".join(f"{x:13.8f}" for x in E))
        print(f"{'':16s} gap " + "  ".join(f"{x:13.8f}" for x in G))
        print(f"{'':16s} bf  " + "  ".join(f"{x:13.8f}" for x in B))
NB["l_trend"] = trend_ok
base, g601 = SCF["m1_L3_N112_lamp1_T0"], SCF["m1_L3_N112_lamp1_T0_g601"]
NB["grid"] = max(rel(g601["energy"], base["energy"]), abs(g601["ksGap"] - base["ksGap"]))
dk = SCF["m1_L3_N896_lamp1_T0_dk0p125"]
print(f"\ngrid 601 vs 301: relative dE0 {rel(g601['energy'], base['energy']):.1e}, d gap {abs(g601['ksGap'] - base['ksGap']):.1e}")
print(f"Delta k = 0.125 m, N = 896: E0/N = {dk['energy'] / 896:.6f} m (Delta k = 0.25 m, N = 112: {base['energy'] / 112:.6f} m); "
      f"brane fraction {dk['emt']['braneFraction_within_1_over_H']:.4f} ({base['emt']['braneFraction_within_1_over_H']:.4f})")

A, Bp = "m1_L3_N112_lamp1_T0_a40p5", "m1_L3_N112_lamp1rescaled_T0_dk0p15163266492815836"
la, lb = levels("scf", A), levels("scf", Bp)
key = lambda d, i: (d["n2"][i], d["parity"][i], d["s"][i], d["index"][i])
ma = {key(la, i): la["eps"][i] for i in range(len(la["eps"]))}
mb = {key(lb, i): lb["eps"][i] for i in range(len(lb["eps"]))}
common = set(ma) & set(mb)
NB["a4_levels"] = max(abs(ma[k] - mb[k]) for k in common)
NB["a4_energy"] = rel(SCF[A]["energy"], SCF[Bp]["energy"])
NB["a4_common"] = (len(common), len(ma), len(mb))
print(f"a4 = 0.5 vs its a4 = 0 partner: {len(common)} common levels (of {len(ma)}, {len(mb)}), "
      f"max |d eps| = {NB['a4_levels']:.1e}, relative dE0 = {NB['a4_energy']:.1e}")
if DET is not None:
    m_ = DET["measurements"]
    print(f"determinism report: repeat byte-identical over {m_['repeatFilesCompared']} files "
          f"(differing: {m_['repeatDifferingFiles']}); refined: {m_['refinedRunsCompared']} runs, max relative energy "
          f"{m_['refinedMaxRelativeEnergy']:.1e}, max |d eps| {m_['refinedMaxAbsEps']:.1e}")

fig, axes = plt.subplots(1, 3, figsize=(12.5, 3.9))
Ls = [2, 3, 4]
for i, (N, name) in enumerate(((8, "lam0"), (8, "lamp1"), (112, "lam0"), (112, "lamp1"))):
    E, G, B = LSER[(N, name)]
    style = "o-" if name == "lam0" else "s--"
    axes[0].plot(Ls, G, style, color=SERIES_N[N], mfc="none" if name != "lam0" else SERIES_N[N], label=f"N = {N}, {name}")
    if N == 112 or name == "lamp1":
        axes[1].semilogy(Ls[:2], [abs(E[0] - E[2]), abs(E[1] - E[2])], style, color=SERIES_N[N],
                         mfc="none" if name != "lam0" else SERIES_N[N], label=f"N = {N}, {name}")
axes[0].set_title("KS gap against the tip cutoff")
axes[0].set_xlabel("L  [1/H]")
axes[0].set_ylabel("KS gap  [m]")
axes[0].set_yscale("log")
axes[0].legend(loc="center right", fontsize=7)
axes[1].set_title("|E0(L) - E0(L = 4)|")
axes[1].set_xlabel("L  [1/H]")
axes[1].set_ylabel("[m]")
axes[1].set_xticks([2, 3])
axes[1].legend(loc="upper right", fontsize=7)
for i, L in enumerate(Ls):
    P = PROFILES[("scf", f"m1_L{L}_N112_lamp1_T0")]
    axes[2].semilogy(P["y"], np.maximum(P["n_c"], 1e-30), color=PALETTE[i], label=f"L = {L}")
axes[2].set_title("n_c(y), N = 112, +lambda_hat_1")
axes[2].set_xlabel("y")
axes[2].legend(loc="upper left")
fig.tight_layout()
save_figure(fig, "convergence.png")
'''))

# ===========================================================================
# 15. Rust against the independent reference solver
# ===========================================================================
CELLS.append(md(r"""
## 15. The Rust program against the independent reference solver

`scripts/ks_reference_solver.py` solves the same Kohn-Sham problems by a
completely different method: a staggered (Yee) grid on which the block
Hamiltonian is a real symmetric matrix without fermion doublers, diagonalised
with numpy on three grids ($N_0$, $2N_0$, $4N_0$ with $N_0 = 60$) and
extrapolated; it derives its own couplings from its own free states.  Its
results are in `artifacts/dirac16complex/kohn-sham/reference/<label>/`
(`run.json`, `spectrum.csv`, `profiles.csv`).  The cross-checker
`scripts/check_dirac16complex_kohn_sham.py` compares the two trees run by run
and writes `python-check-report.json`.

This notebook does the run-by-run comparison **itself**, with the checker's
own comparison function (`compare_canonical`, imported from the checker so the
rules and tolerances are identical) applied to the two committed trees: the
couplings, the eigenvalues per shell, parity and block type (with branch and
$T = 0$ occupation), $E_0$ (corrected to first order for the tiny difference
of the independently derived couplings), $\mu$, the KS gap, $\Delta$SCF, the
lowest particle-hole excitation, the density, potential and EMT profiles on
the common nodes, the EMT averages and brane fractions, the E4.1 verdict, and
at $T > 0$ the thermodynamics after the correction for the Rust level window.
If `excited/summary.json` is absent (being regenerated), the excited records
are rebuilt from `excitations.csv` and `particle-hole.csv`.  The comparison is
therefore available whether or not the checker's report is present; when the
report is present, the gauntlet additionally requires that it is **current**
(its recorded SHA-256 of the reference summary, the reference solver, the
checker, the theory file and the Rust summaries equal the files on disk) and
that it has no failed check.  The figure shows, per run, the deviation divided
by its tolerance (below 1 = agreement).
"""))

CELLS.append(code(r'''
import contextlib
import io

sys.path.insert(0, str(REPO / "scripts"))
with contextlib.redirect_stdout(io.StringIO()):
    import check_dirac16complex_kohn_sham as CK

REFSUM_STATUS = optional_json(REFDIR / "reference-summary.json")[1]
XREG = None
if REFSUM_STATUS != "present":
    SKIPPED["rust_vs_reference"] = f"reference/reference-summary.json is {REFSUM_STATUS}"
    print("reference summary", REFSUM_STATUS, "- the run-by-run comparison is skipped")
else:
    XSUM = CK.rust_summaries(str(RUST))
    XRUNS = CK.rust_runs(str(RUST), XSUM)
    have = {(r["sub"], r["label"]) for r in XRUNS}
    rebuilt = []
    for label in EXCITED_LABELS:
        if ("excited", label) in have or label not in SCF:
            continue
        record = excited_record(label)
        params = dict(next(r["params"] for r in XRUNS if r["sub"] == "scf" and r["label"] == label))
        params["inheritedFrom"] = "scf/" + label
        XRUNS.append({"sub": "excited", "label": label, "dir": str(RUST / "excited" / label), "run": None,
                      "record": record, "params": params})
        rebuilt.append(label)
    XREG = CK.Registry()
    CK.compare_canonical(XREG, str(REFDIR), XRUNS)
    compared = XREG.measurements.get("canonicalCompared", [])
    print(f"Rust runs: {len(XRUNS)} ({'excited records rebuilt from the CSV files: ' + str(len(rebuilt)) if rebuilt else 'excited records from summary.json'}); "
          f"compared with a reference run of the same label: {len(compared)}; without one: "
          f"{XREG.measurements.get('canonicalWithoutReferenceRun', [])}")
    for name, ok in sorted(XREG.checks.items()):
        print(f"{'agree' if ok else 'DIFFER'}  {name}: {XREG.measurements.get(name + '_detail', '')}")

# ---- the checker's own report, if present, and whether it is current -------------
CHECK_CURRENT = None
if CHECKREP is not None:
    src = CHECKREP.get("sourceSha256", {})
    files = {"referenceSummary": REFDIR / "reference-summary.json",
             "referenceSolver": REPO / "scripts" / "ks_reference_solver.py",
             "checker": REPO / "scripts" / "check_dirac16complex_kohn_sham.py",
             "theoryJson": KSDIR / "kohn-sham-theory.json"}
    files.update({f"rust_{sub}": RUST / sub / "summary.json" for sub in SUBCOMMANDS})
    stale = [k for k, p in files.items() if k in src and (not p.is_file() or sha256(p) != src[k])]
    missing = [k for k in files if k not in src]
    CHECK_CURRENT = {"stale": stale, "notRecorded": missing, "failed": CHECKREP.get("failed", []),
                     "checkCount": CHECKREP.get("checkCount"), "failedCheckCount": CHECKREP.get("failedCheckCount")}
    print(f"\npython-check-report.json: {CHECK_CURRENT['checkCount']} checks, {CHECK_CURRENT['failedCheckCount']} failed "
          f"{CHECK_CURRENT['failed']}; inputs changed since it was written: {stale}; not recorded: {missing}")
else:
    print(f"\npython-check-report.json is {CHECKREP_STATUS}: only the in-notebook comparison above is available")

if XREG is not None:
    TOLX = CK.TOL
    groups = {}
    for name, entry in XREG.comparisons.items():
        if not name.startswith("canonical_") or entry.get("status") != "ran":
            continue
        rec = entry["detail"]
        sub, label = name[len("canonical_"):].split("_", 1)
        ratios = {}
        for q_ in ("E0", "mu", "ksGap", "deltaSCF"):
            x = rec.get(q_)
            if isinstance(x, dict) and x.get("tolerance"):
                ratios[q_] = x["deviation"] / x["tolerance"]
        ev = rec.get("eigenvalues") or {}
        if ev.get("compared"):
            ratios["eigenvalues"] = ev["maxDeviationOverTolerance"]
        prof = rec.get("profiles") or {}
        interior = [v["interior"] for k, v in prof.items() if isinstance(v, dict) and "interior" in v]
        if interior:
            ratios["profiles (interior)"] = max(interior) / TOLX["profileInterior"]
        th = rec.get("thermo") or {}
        tvals = [v["deviation"] / v["tolerance"] for k, v in th.items()
                 if isinstance(v, dict) and v.get("tolerance") and "deviation" in v]
        if tvals:
            ratios["thermodynamics"] = max(tvals)
        groups[(sub, label)] = ratios
    order = sorted(groups, key=lambda k: (CK.SUBCOMMANDS.index(k[0]), k[1]))
    quantities = ["E0", "mu", "ksGap", "deltaSCF", "eigenvalues", "profiles (interior)", "thermodynamics"]
    markers = ["o", "s", "^", "D", "v", "P", "X"]
    fig, ax = plt.subplots(figsize=(12.5, 4.6))
    for qi, qn in enumerate(quantities):
        xs = [i for i, k in enumerate(order) if qn in groups[k]]
        ys = [max(groups[order[i]][qn], 1e-6) for i in xs]
        if xs:
            ax.plot(xs, ys, markers[qi], ms=4.5, mfc="none", color=PALETTE[qi], label=qn)
    ax.axhline(1.0, color=PALETTE[7], lw=1.2, ls="--")
    ax.text(0.5, 1.25, "tolerance", color=INK2, fontsize=7.5)
    ax.set_yscale("log")
    ax.set_ylim(1e-6, max(10.0, 3 * max((max(v.values()) for v in groups.values() if v), default=1.0)))
    bounds = [i for i in range(1, len(order)) if order[i][0] != order[i - 1][0]]
    for b in bounds:
        ax.axvline(b - 0.5, color=AXIS, lw=0.8)
    starts = [0] + bounds
    for s0 in starts:
        ax.text(s0, ax.get_ylim()[1] * 0.5, order[s0][0], color=INK2, fontsize=8, va="top")
    ax.set_xlabel("run (grouped by subcommand, labels sorted)")
    ax.set_ylabel("deviation / tolerance  (profiles: / 2e-5)")
    ax.set_title("Rust against the independent reference solver, run by run (tolerances of check_dirac16complex_kohn_sham.py)")
    ax.legend(loc="upper right", ncol=4, fontsize=7)
    fig.tight_layout()
    save_figure(fig, "rust_vs_reference.png")
    worst_rows = sorted(((max(v.values()), k) for k, v in groups.items() if v), reverse=True)[:8]
    print("\nlargest deviation/tolerance per run:")
    for value, (sub, label) in worst_rows:
        print(f"  {value:9.3g}  {sub}/{label}  " + ", ".join(f"{k} {x:.2g}" for k, x in groups[(sub, label)].items()))
'''))

# ===========================================================================
# 16. The verification gauntlet
# ===========================================================================
FIGURE_DESCRIPTIONS = {
    "block_structure.png": "Eight 2x2 blocks: |entries| of the y-current matrix gamma^0 gamma^4 in the original "
                           "spinor basis and in the explicit block basis of kohn-sham-theory.json, and of the full "
                           "reduced-equation operator in the block basis (section 6.1).",
    "exchange_uniform_gas.png": "Uniform 8-fold gas: -e_x/lambda against n at T = 0, 0.3, 1, 2 m from the double "
                                "quadrature of exchange-table.json (markers) and the closed form -(n^2+S^2)/32 "
                                "(lines); relative deviation of every row of the d4 and d3 tables (section 6.2).",
    "ks_spectrum.png": "Kohn-Sham spectrum eps_n(k) per parity (rows) and block type s = -j (markers): free "
                       "spectrum m = 1, L = 3 with the zero-mode band +-ck, and the self-consistent spectrum of "
                       "m1_L3_N112_lamp2_T0 with its chemical potential (section 7).",
    "density_profiles.png": "Ground-state profiles against y (m = 1, L = 3): n_c, n_p for N = 8, 112, 1016 at "
                            "lambda = 0; S_p; the pseudo-potential pair M_eff - m and v_x at +-lambda_hat_2; the HOMO "
                            "orbital |chi|^2 against z = 6Hx0 (section 8).",
    "scf_history.png": "Self-consistency histories: density residual per Anderson iteration for N = 8, 112, 1016 "
                       "at +lambda_hat_2 and -lambda_hat_2 (section 8.1).",
    "ground_state_energy.png": "Ground-state energy against N: free closed shells from the in-cell aufbau with the "
                               "self-consistent +-lambda_hat_2 points; interaction energy E0(lambda) - E0(0) against "
                               "the first-order Hellmann-Feynman value (section 9).",
    "ks_gap_delta_scf.png": "KS gap and Delta-SCF against lambda_hat/lambda_hat_1 for N = 8, 112, 1016, and their "
                            "difference (orbital relaxation); the smeared N = 1016, -lambda_hat_2 ensemble is marked "
                            "(section 10).",
    "fermi_level_N1016_lamm2.png": "The level crossing at the Fermi level: particle levels near mu with their "
                                   "occupations for the free N = 1016 state (exact aufbau) and the smeared "
                                   "-lambda_hat_2 ensemble (192-fold band at k = 0.935, 8-fold k = 0 level) "
                                   "(section 10.2).",
    "thermodynamics.png": "E, F, S, C_V and the KS gap against T for N = 8, 112 in the series lam0, lamp1, lamh, "
                          "and the occupations of the finite-T Kohn-Sham excitation spectrum (section 11).",
    "emt_profiles.png": "Energy-momentum tensor of the +lambda_hat_1 ground states (N = 112, 1016): rho, p_y, p_3, "
                        "p_t against y, the local p/rho with w_req = -5/7, and rho e^{6Hy} (section 12).",
    "einstein_source.png": "Per emt run: <rho> against rho_req = -21 H^2/kappa, the kappa it would need, and "
                           "|lambda <S_p>/m| against the E4.1 value 5/6 (section 12).",
    "brane_localisation.png": "Cumulative fraction of the particles within a distance d of the brane (N = 8, 112, "
                              "1016 at m = 1; N = 112 at m = 3) and the fraction within 1/H against the coupling "
                              "(section 13).",
    "convergence.png": "Tip-cutoff convergence L = 2, 3, 4: KS gap, |E0(L) - E0(4)| and n_c(y) of N = 112 at "
                       "+lambda_hat_1 (section 14).",
    "rust_vs_reference.png": "Rust against the independent reference solver, run by run: deviation/tolerance of "
                             "E0, mu, KS gap, Delta-SCF, eigenvalues, interior profiles and thermodynamics, with the "
                             "tolerances of check_dirac16complex_kohn_sham.py (section 15).",
}
REQUIRED_FIGURES = sorted(FIGURE_DESCRIPTIONS)

q("wl_checks", "{:d}", 'len(WOLFRAM["checks"])')
q("py_checks", "{:d}", 'len(PYTHEORY["checks"])')

_QUOTE_LINES = None  # filled in main(), after every quote has been registered

GAUNTLET_CODE = r'''
GAUNTLET = []


def gauntlet(name, ok, detail):
    ok = bool(ok)
    GAUNTLET.append({"name": name, "status": "PASS" if ok else "FAIL", "detail": detail})
    print(("PASS - " if ok else "FAIL - ") + name + ": " + detail)


def skip(name, why):
    GAUNTLET.append({"name": name, "status": "SKIP", "detail": why})
    print("SKIP - " + name + ": " + why)


R = NB["recompute"]
# ---- the program, its self-checks and its reproducibility -----------------------------
gauntlet("program_runs_success", RUNS and all(r["exit"] == 0 and r["last"] == "SUCCESS" for r in RUNS),
         f"{len(RUNS)} program runs (print-config, spectrum), every one exited 0 with SUCCESS as its last line")
present = {sub: s for sub, s in SUMMARY.items() if s is not None}
gauntlet("fixture_hash_consistent", CONFIG.get("fixture sha256") == FIX_SHA and
         all(s["fixture"]["sha256"] == FIX_SHA for s in present.values()),
         f"print-config and {len(present)} summaries name the algebra fixture sha256 {FIX_SHA[:16]}...")
if FRESH is None:
    skip("fresh_spectrum_byte_identical", SKIPPED.get("fresh_spectrum_byte_identical", "not run"))
else:
    gauntlet("fresh_spectrum_byte_identical", FRESH["identical"] == FRESH["files"],
             f"{FRESH['identical']}/{FRESH['files']} files of the re-run spectrum subcommand equal the committed ones"
             + (f"; different: {FRESH['different']}" if FRESH["different"] else ""))
for sub in SUBCOMMANDS:
    s = SUMMARY[sub]
    if s is None:
        skip(f"rust_{sub}_self_checks", f"rust/{sub}/summary.json is {SUMMARY_STATUS[sub]} (being regenerated?)")
    else:
        gauntlet(f"rust_{sub}_self_checks", s["verdict"] == "SUCCESS" and all(s["checks"].values()),
                 f"{sum(s['checks'].values())}/{len(s['checks'])} checks of the program true, verdict {s['verdict']}")
if DET is None:
    skip("determinism_report_current", f"rust/determinism-report.json is {DET_STATUS}")
else:
    det_path = lambda k: CRATE / k if k.startswith("tools/") else RUST / k
    stale = [k for k, h in DET["sourceSha256"].items() if not det_path(k).is_file() or sha256(det_path(k)) != h]
    gauntlet("determinism_report_current", all(DET["checks"].values()) and not stale,
             f"repeat byte identity and refined convergence {sorted(k for k, v in DET['checks'].items() if v)}; "
             f"summaries changed since the report was written: {stale}")
for name, rep, status in (("wolfram", WOLFRAM, WOLFRAM_STATUS), ("python_sympy", PYTHEORY, PYTHEORY_STATUS)):
    if rep is None:
        skip(f"exact_theory_{name}", f"report {status}")
    else:
        gauntlet(f"exact_theory_{name}", all(rep["checks"].values()),
                 f"{sum(rep['checks'].values())}/{len(rep['checks'])} exact checks of {rep['producer']} true")

# ---- the exact reduction and the pseudo-potential ---------------------------------------
gauntlet("algebra_relations_exact", NB["alg_max"] == 0.0,
         "Clifford relations, C = g0g1g2g3, B = -iCg4, B^2 = 1 from the integer fixture: exact (0.0)")
gauntlet("block_basis_exact", max(NB["basis_unitary"], NB["basis_off_block"], NB["basis_vs_theory"], NB["basis_vs_formula"]) < 1e-14
         and NB["block_types"] == [-1, 1] and NB["blocks_per_type"] == {1: 4, -1: 4},
         f"unitary {NB['basis_unitary']:.1e}, off-block {NB['basis_off_block']:.1e}, vs stored blocks "
         f"{NB['basis_vs_theory']:.1e}, vs closed forms {NB['basis_vs_formula']:.1e}; two types j = +-1, 4 blocks each")
gauntlet("block_ode_exact", NB["block_ode"] < 1e-14,
         f"g0[M - i kk g1 + i(eps - v) g4] -> M s3 - kk s2 + i j (eps - v) s1 in every block: {NB['block_ode']:.1e}")
gauntlet("exchange_closed_form", NB["ex_quadrature"] < 1e-12 and NB["ex_potentials"] < 1e-12,
         f"double quadrature vs -(n^2 + S^2)/32: {NB['ex_quadrature']:.1e}; v_v, v_s, n-only v_x columns: "
         f"{NB['ex_potentials']:.1e}")

# ---- the free spectrum --------------------------------------------------------------------
gauntlet("box_spectrum_analytic", NB["box_dev"] < 1e-8 and NB["box_count_bad"] == 0,
         f"k = 0 levels of 6 (m, L) x 2 parities x 2 types vs sqrt(M^2 + (n pi/L)^2), tan(pL) = -p/M: {NB['box_dev']:.1e}")
gauntlet("chiral_zero_mode", NB["zero_mode"] <= 1e-12, f"eps = 0 and zero scalar charge: {NB['zero_mode']:.1e}")
gauntlet("zero_mode_splitting", NB["c_shoot"] < 1e-6 and NB["s_is_minus_j"] and NB["c_rust_vs_closed"] < 1e-8,
         f"in-cell RK4 shooting slope vs closed-form c: {NB['c_shoot']:.1e} (12 cases); sign = -s (s = -j); "
         f"program's Hellmann-Feynman slope vs closed form {NB['c_rust_vs_closed']:.1e}")
gauntlet("mirror_spectra_and_multiplicities", NB["mirror_dev"] < 1e-8 and NB["mirror_bad"] == 0 and NB["mult_bad"] == 0,
         f"s = -1 levels = -(s = +1 levels): {NB['mirror_dev']:.1e}; multiplicity 4 r3(n2) everywhere")

# ---- ground states ---------------------------------------------------------------------------
gauntlet("particle_number", R["N_weights"] < 1e-9 and R["N_density"] < 1e-6 and R["N_density_vs_rust"] < 1e-12,
         f"{len(RECOMP)} runs: sum of weights {R['N_weights']:.1e}, density integral {R['N_density']:.1e} "
         f"(vs the program's own {R['N_density_vs_rust']:.1e})")
gauntlet("energy_recomputed", max(R["E_H"], R["E_x"], R["ksSum"], R["E"]) < 1e-12,
         f"E_H {R['E_H']:.1e}, E_x {R['E_x']:.1e}, sum w eps {R['ksSum']:.1e}, E = sum w eps - E_H - E_x {R['E']:.1e}")
gauntlet("pseudo_potential_formula", R["M_eff"] < 1e-5 and R["v_x"] < 1e-5,
         f"M_eff = m + (15/16) lambda S_p: {R['M_eff']:.1e}, v_x = -lambda n_p/16: {R['v_x']:.1e} "
         "(relative to the potential scale; self-consistency of the last iteration)")
gauntlet("profile_columns", R["columns"] < 1e-12, f"n_c = e^(6Hy) n_p, volume factor, z = arcsin e^(6Hy): {R['columns']:.1e}")
gauntlet("scf_converged", NB["scf_all_converged"], f"all {len(SCF)} scf runs converged, residuals < 1e-10")
gauntlet("closed_shells_and_aufbau", NB["shell_list_dev"] < 1e-8 and not NB["shell_list_missing"] and NB["aufbau_E0"] < 1e-8,
         f"closed shells from the free spectrum vs closed-shells-m1-L3.csv {NB['shell_list_dev']:.1e}; "
         f"aufbau E0 vs scf lambda = 0: {NB['aufbau_E0']:.1e}")
gauntlet("first_order_coupling", NB["first_order_lh1"] < 0.05,
         f"+-lambda_hat_1: |(E0(lambda) - E0(0)) / (lambda dE/dlambda|0) - 1| = {NB['first_order_lh1']:.3f} < 0.05")

# ---- excited states ----------------------------------------------------------------------
gauntlet("ks_gap_recomputed", max(NB["gap_vs_record"], NB["gap_vs_run"], NB["gap_vs_table"], NB["record_vs_table"]) < 1e-12,
         f"LUMO - HOMO from levels.csv vs the run records {NB['gap_vs_record']:.1e}, vs scf run.json {NB['gap_vs_run']:.1e}, "
         f"vs excitations.csv {NB['gap_vs_table']:.1e}; records vs excitations.csv {NB['record_vs_table']:.1e}")
gauntlet("delta_scf_bookkeeping", NB["dscf_identity"] < 1e-9 and NB["excited_ground_is_scf"] and NB["one_particle_promoted"] < 1e-9,
         f"E1 - E0 = Delta-SCF {NB['dscf_identity']:.1e}; excited ground state = scf ground state; exactly one "
         f"particle moved up {NB['one_particle_promoted']:.1e}")
gauntlet("delta_scf_equals_gap_free", NB["dscf_equals_gap_free"] < 1e-9,
         f"lambda = 0: Delta-SCF = KS gap to {NB['dscf_equals_gap_free']:.1e}")
gauntlet("particle_hole_lists", not NB["ph_bad"] and NB["ph_dev"] < 1e-12,
         f"{len(EXCITED_LABELS)} lists rebuilt with the 1e-12 occupation floor: max deviation {NB['ph_dev']:.1e}; "
         f"differing runs {NB['ph_bad']}")
sm = SCF[SMEARED]
gauntlet("level_crossing_run_as_documented",
         sm["parameters"]["occupationSmearing"] == 1e-3 and sm["exactZeroTemperatureOccupations"] is False
         and sm["parameters"]["T"] == 0.0 and sm["freeEnergy"] == sm["energy"] and NB["smeared"]["occ_band_and_k0"]
         and BAND["mult"] == 192 and KZERO["mult"] == 8 and KZERO["k"] == 0.0
         and abs(NB["smeared"]["N"] - 1016) < 1e-9 and NB["smeared"]["balance"] < 1e-9
         and any(n == 1016 and abs(e - BAND["eps"]) < 0.01 for n, e in zip(CLOSED_SHELLS["N"], CLOSED_SHELLS["eps_homo"])),
         f"smearing 1e-3 m at T = 0, F = E, exact occupations false; fractional levels = the 192-fold band "
         f"(f = {BAND['f']:.4f}) and the 8-fold k = 0 level (f = {KZERO['f']:.4f}); {MOVED:.3f} particles moved; "
         "N = 1016 is a closed shell of the free aufbau")

# ---- thermodynamics ------------------------------------------------------------------------
gauntlet("entropy_and_free_energy", NB["thermo_S"] < 1e-10 and NB["thermo_F"] < 1e-12,
         f"S from the occupations vs run.json {NB['thermo_S']:.1e}; |E - TS - F| {NB['thermo_F']:.1e}")
gauntlet("heat_capacity_forms", NB["cv_fixed_forms"] < 1e-10 and NB["cv_fd_vs_fixed_free"] < 1e-2,
         f"fixed-spectrum forms {NB['cv_fixed_forms']:.1e}; lambda = 0 central difference vs fixed spectrum "
         f"{NB['cv_fd_vs_fixed_free']:.1e} < 1e-2 (the checker's tolerance)")
gauntlet("thermodynamic_monotonicity", NB["thermo_monotone"], "F decreases and S increases with T in all six series")

# ---- energy-momentum tensor ------------------------------------------------------------------
E_ = NB["emt"]
gauntlet("emt_recomputed", E_["E_rho"] < 1e-7 and max(E_["volume"], E_["averages"], E_["w"], E_["Ls"], E_["kappa"]) < 1e-12
         and E_["E41"] < 1e-10,
         f"int rho dV = E {E_['E_rho']:.1e}; volume {E_['volume']:.1e}; averages {E_['averages']:.1e}; w {E_['w']:.1e}; "
         f"p_t = L_s {E_['Ls']:.1e}; kappa needed {E_['kappa']:.1e}; E4.1 {E_['E41']:.1e}")
gauntlet("emt_conservation", E_["conservation"] < 1e-2,
         f"(e^(6Hy) p_y)' = 3H e^(6Hy)(p_3 + p_t), fourth-order stencil: {E_['conservation']:.1e} < 1e-2 "
         f"(program's own measure {NB['emt_conservation_rust']:.1e})")
gauntlet("einstein_source_mismatch", NB["emt_bulk_positive"] and NB["emt_none_met"]
         and EMT["m1_L3_N112_lam0_T0"]["emt"]["sPAvg"] < 0 and EMT["m1_L3_N1016_lam0_T0"]["emt"]["sPAvg"] < 0
         and GEOM["rhoRequired_kappa1"] == -21.0,
         "rho_req = -21 H^2/kappa < 0 while <rho> > 0 for every N > 8 run (kappa < 0 needed); E4.1 met in no run; "
         "<S_p> < 0 at lambda = 0")
gauntlet("brane_fraction", NB["brane_fraction"] < 1e-12 and NB["tip_fraction"] < 1e-12,
         f"within 1/H of the brane recomputed for {len(SCF)} runs: {NB['brane_fraction']:.1e}; tip {NB['tip_fraction']:.1e}")

# ---- convergence ------------------------------------------------------------------------------
gauntlet("l_convergence_trend", NB["l_trend"], "|X(L=4) - X(L=3)| <= |X(L=3) - X(L=2)| for E0 and the KS gap, 4 series")
gauntlet("grid_convergence", NB["grid"] < 1e-8, f"601 vs 301 grid points: {NB['grid']:.1e}")
gauntlet("a4_rescaling_exact", NB["a4_levels"] < 1e-8 and NB["a4_energy"] < 1e-10
         and NB["a4_common"][0] == NB["a4_common"][1] == NB["a4_common"][2],
         f"a4 = 0.5 vs its a4 = 0 partner: levels {NB['a4_levels']:.1e}, E0 {NB['a4_energy']:.1e}")

# ---- Rust against the reference ------------------------------------------------------------
if XREG is None:
    skip("rust_vs_reference", SKIPPED.get("rust_vs_reference", "not run"))
else:
    for name, ok in sorted(XREG.checks.items()):
        gauntlet("rust_vs_reference_" + name[len("canonical_"):], ok, XREG.measurements.get(name + "_detail", ""))
if CHECK_CURRENT is None:
    skip("python_check_report", f"artifacts/dirac16complex/kohn-sham/python-check-report.json is {CHECKREP_STATUS}")
else:
    gauntlet("python_check_report", not CHECK_CURRENT["stale"] and not CHECK_CURRENT["notRecorded"]
             and CHECK_CURRENT["failedCheckCount"] == 0,
             f"{CHECK_CURRENT['checkCount']} checks, failed {CHECK_CURRENT['failed']}; inputs changed since it was "
             f"written: {CHECK_CURRENT['stale']}; not recorded: {CHECK_CURRENT['notRecorded']}")

# ---- figures and quoted numbers ----------------------------------------------------------
REQUIRED_FIGURES = REQUIRED_FIGURES_LIST
names = sorted(Path(f["file"]).name for f in FIGURES)
gauntlet("figures_written", names == REQUIRED_FIGURES and
         all(hashlib.sha256((REPO / f["file"]).read_bytes()).hexdigest() == f["sha256"] for f in FIGURES),
         f"{len(FIGURES)} of {len(REQUIRED_FIGURES)} PNG figures in artifacts/dirac16complex/kohn-sham/figures, "
         f"hashes re-read" + (f"; missing {sorted(set(REQUIRED_FIGURES) - set(names))}" if names != REQUIRED_FIGURES else ""))
QUOTED = [
QUOTE_LINES
]
bad = []
for key, fmt_, fn, text in QUOTED:
    try:
        now = fmt_.format(fn())
    except Exception as exc:  # noqa: BLE001 - a quote whose source vanished is a mismatch
        now = f"<{type(exc).__name__}>"
    if now != text:
        bad.append((key, text, now))
gauntlet("prose_numbers_match_files", not bad,
         f"{len(QUOTED)} numbers and strings quoted in the markdown re-read from the committed files"
         + (f"; mismatches (key, prose, files): {bad}" if bad else ""))

failed = [g["name"] for g in GAUNTLET if g["status"] == "FAIL"]
skipped = [g["name"] for g in GAUNTLET if g["status"] == "SKIP"]
print(f"\ngauntlet: {len(GAUNTLET)} checks, {len(GAUNTLET) - len(failed) - len(skipped)} passed, "
      f"{len(failed)} failed, {len(skipped)} skipped")
if failed:
    raise AssertionError("gauntlet failed: " + ", ".join(failed))
if skipped:
    print("ALL COMPUTED CHECKS PASSED; SKIPPED (inputs absent): " + ", ".join(skipped))
else:
    print("ALL CHECKS PASSED")
'''

CELLS.append(md(r"""
## 16. The verification gauntlet

Every acceptance criterion in one place: the program runs and the byte
identity of the re-run spectrum; the self-checks of the five subcommands; the
determinism report (and that it still describes the committed summaries);
the exact theory reports (Wolfram «wl_checks» checks, sympy «py_checks»
checks); every in-cell recomputation of sections 6 to 14 against tolerances
stated in the check; the run-by-run comparison with the reference solver
(every quantity of the cross-checker); the cross-checker's report when
present (current and without failures); the figures; and every number quoted
in this text, re-read from the files.  A check whose input file is absent
prints `SKIP` with the reason (the audit treats a skip as incomplete, never
as a pass).  If any check fails, the cell ends with an error after printing
all of them: there is no "mostly passed".
"""))

GAUNTLET_CELL_INDEX = len(CELLS)
CELLS.append(None)  # the gauntlet code cell, completed in main() after every quote is registered

# ===========================================================================
# 17. Conclusions
# ===========================================================================
CELLS.append(md(r"""
## 17. Conclusions

**Established (numerically, within the model, with the checks above):**

- The Kohn-Sham problem of the dirac16complex gas in the static primordial
  field reduces exactly to eight 2x2 blocks of two inequivalent types
  ($j = \pm1$, four blocks each, opposite spectra); the reduction was verified
  here in floating point from the integer gamma matrices.
- The free spectrum has the exact chiral brane zero modes and their linear
  band $\pm ck$ ($c$ = «c_theory» for $m = H$, $L = 3/H$), the analytic
  $k = 0$ box levels, the mirror spectra of the two block types and the
  4-fold degeneracy per type; closed shells $N$ = 8, «n_mid», «n_large».
- The exchange of the contact interaction is exactly local,
  $e_x = -(\lambda/32)(n^2 + S^2)$ at every temperature (the tabulated double
  quadrature agrees to round-off), so the Kohn-Sham pseudo-potential is the
  exact local Hartree-Fock pair $(M_\text{eff}, v_x)$ with no correlation term.
- The self-consistent ground states are brane-localised (fractions «bf_8»,
  «bf_112», «bf_1016» within $1/H$ for $N$ = 8, «n_mid», «n_large»), insensitive
  to the tip cutoff, and agree with an independent matrix solver run by run
  (section 15).
- Their energy density is positive wherever bulk levels are filled, while the
  primordial field needs $\rho_\text{req}$ = «rho_req» $H^2/\kappa$: the
  Kohn-Sham gas cannot be the source of the static field (it would need
  $\kappa$ = «kappa_112», «kappa_1016» $< 0$), and the two static-field
  sourcing conditions of STAGE4_SPEC E4.1 are met in no run.
- One run, $N$ = «n_large» at $-\hat\lambda_2$, has a level crossing at the
  Fermi level; its results refer to the smeared $T = 0$ ensemble described
  in section 10.2.

**Model-dependent or assumed:** the $Z_2$ brane with the two parity
conditions and the $\theta = 0$ chiral bag at the tip cutoff; the static
profile ($a_4$ constant); the 3-torus with $\Delta k = 0.25\,m$ and closed
shells; the per-configuration couplings; Hartree-Fock-local exchange without
correlation (a contact interaction beyond Hartree-Fock is not renormalisable
in 8D); the good sector without extra-time momentum; the positive-norm
quantisation with the expectation rule $u^\dagger BMu$.

**Not established:** a Kohn-Sham state that sources the primordial geometry.
The E4.1 conditions need $\lambda S/m = -5/6$ with $mS < 0$; the mirror sector
of the $\gamma^8$ map ($m\to-m$) maps the problem onto one with identical
energies and $S\to-S$, so $mS$ and $\lambda S^2$, and hence the verdict, are
unchanged there (the program's `emt` module derives this).
"""))

CELLS.append(md(r"""
## 18. What we learned

1. **Write the conventions down and measure them.** The exact theory labels
   the block types by $j$, both solvers by $s$; the zero-mode slope measured in
   section 7 fixes $s = -j$ without argument.
2. **An exact identity beats a table.** The finite-temperature exchange table
   was planned as the input of the LDA; the exact theory showed that the
   angular average makes the exchange local and closed-form.  The table
   survived as an independent check (section 6.2), not as data to interpolate.
3. **Probe the regime before reading off a slope.** The torus shells start at
   $k = 0.25\,m$, where $e^{L}k$ is already of order 5 at the tip: the linear
   zero-mode band is only visible at $k\to0$, so the slope was recomputed by
   shooting at $k = 10^{-4}$ instead of fitting the band.
4. **A degenerate crossing at the Fermi level can defeat the exact aufbau.**
   Whichever of two nearly degenerate levels is filled last, the potential it
   creates moves the other below it.  The honest fix is to converge a
   documented smeared ensemble at $T = 0$, to say exactly what its gap,
   $\Delta$SCF and particle-hole list refer to, and to give the
   particle-hole rule an occupation floor so that Fermi-Dirac tails do not
   count as holes.
5. **Local residuals are amplified by the geometry.** Convergence is measured
   on $n_c = e^{6Hy}n_p$; the proper densities, and with them the written
   pseudo-potential, carry the residual times $e^{-6Hy}$ towards the tip
   (section 8).
6. **Compare with one set of rules.** The run-by-run comparison with the
   reference solver calls the cross-checker's own function, so the notebook
   and the checker cannot disagree about tolerances.
7. **Do not re-run hours inside a notebook; prove reproducibility instead.**
   A one-minute subcommand re-run byte for byte, plus a determinism report
   that is checked to still describe the committed summaries.
8. **Numbers in prose rot unless they are generated and asserted.** Every
   number in this text is filled in by the builder from the files and
   re-checked by the gauntlet.
"""))


# ===========================================================================
# Assembly, writing and execution
# ===========================================================================
def build_notebook():
    """The un-executed notebook as a dict (deterministic)."""
    cells = list(CELLS)
    quote_lines = "\n".join(f"    ({key!r}, {fmt!r}, lambda: {expr}, {text!r}),"
                            for key, (fmt, expr, text) in QUOTES.items())
    gauntlet_code = (GAUNTLET_CODE.replace("QUOTE_LINES", quote_lines)
                     .replace("REQUIRED_FIGURES_LIST", repr(REQUIRED_FIGURES)))
    cells[GAUNTLET_CELL_INDEX] = code(gauntlet_code)
    markdown = "".join("".join(c["source"]) for c in cells if c["cell_type"] == "markdown")
    unused = sorted(k for k, (_, _, text) in QUOTES.items() if not _USED_KEYS.get(k))
    if unused:
        raise RuntimeError(f"quotes registered but never used in the markdown: {unused}")
    if "«" in markdown or "»" in markdown:
        raise RuntimeError("an unfilled placeholder is left in the markdown")
    out = []
    for i, cell in enumerate(cells):
        cell = dict(cell)
        cell["id"] = f"ks-{i:03d}"
        out.append(cell)
    return {
        "cells": out,
        "metadata": {
            "kernelspec": {"display_name": "Python 3 (ipykernel)", "language": "python", "name": "python3"},
            "language_info": {"name": "python"},
        },
        "nbformat": 4,
        "nbformat_minor": 5,
    }


def notebook_text(nb):
    return json.dumps(nb, indent=1, ensure_ascii=False, sort_keys=True) + "\n"


def execute(path, timeout=7200):
    """Execute the notebook in place with nbclient (kernel python3, cwd = repository root).
    Returns True if every cell ran; the executed notebook is written in either case."""
    import nbformat
    from nbclient import NotebookClient
    from nbclient.exceptions import CellExecutionError

    nb = nbformat.read(str(path), as_version=4)
    client = NotebookClient(nb, timeout=timeout, startup_timeout=600, kernel_name="python3",
                            record_timing=False, coalesce_streams=True,
                            resources={"metadata": {"path": str(REPO)}})
    ok = True
    try:
        client.execute()
    except CellExecutionError as exc:
        ok = False
        print("FAIL: a cell raised an error during execution:")
        print(str(exc)[-4000:])
    text = nbformat.writes(nb)
    if not text.endswith("\n"):
        text += "\n"
    Path(path).write_text(text, encoding="utf-8", newline="\n")
    return ok


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--output", default=str(DEFAULT_OUTPUT), help="where to write the notebook")
    parser.add_argument("--execute", action="store_true", help="execute it in place with nbclient afterwards")
    parser.add_argument("--timeout", type=int, default=7200, help="per-cell timeout in seconds for --execute")
    args = parser.parse_args(argv)
    nb = build_notebook()
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(notebook_text(nb), encoding="utf-8", newline="\n")
    n_code = sum(c["cell_type"] == "code" for c in nb["cells"])
    print(f"wrote {out} ({len(nb['cells'])} cells, {n_code} code cells, {len(QUOTES)} quoted numbers, "
          f"{len(REQUIRED_FIGURES)} figures)")
    if args.execute:
        ok = execute(out, args.timeout)
        print(("executed " if ok else "execution FAILED for ") + str(out))
        return 0 if ok else 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
