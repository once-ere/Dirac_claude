---
title: "UM-2 manual tasks"
subtitle: "How to carry out by hand the two long tasks of the UM-2 work: the fresh-clone verification of every computation and document, and the independent review of the documents against the computed outputs"
author:
  - "Underlying theory: Patrick L. Nash"
  - "Written by Claude (Anthropic)"
  - "Manual tasks, version 1, 2026-10-18"
  - "Repository once-ere/Dirac_claude, folder universe_model_2"
---

# How to read this document

The author's rule for this work is that no individual calculation may take longer than 12 minutes and 3 seconds. Two
tasks of the UM-2 work broke that rule when they were run as single jobs:

* **Task 1, the fresh-clone verification**: all 16 computations and the document build, run as one job, took about
  16 minutes (953 s on 2026-10-18), although every individual computation takes at most about 4 minutes (the primordial
  integration, 248 s).
* **Task 2, the independent review**: a review agent that read the five documents, compared their statements with the
  computed outputs and recomputed key numbers independently ran for 19 minutes 16 seconds (71 tool calls).

This document describes both tasks completely and precisely, split into steps that each finish well within the limit, so
that they can be executed by hand and their results reported back for incorporation into the project. It is
self-contained: every command, every equation and every reference value it needs is written here. Wherever a value can
change when the computations are updated, the command that prints it from the repository is given instead of the value.

Conventions: the coordinates are the author's $x_0, x_1, \dots, x_7$ ($x_0$ the hidden space direction, $x_1, x_2, x_3$
space, $x_4$ the time, $x_5, x_6, x_7$ the extra times); $W^+$ carries the charge $+e$ and $W^-$ the charge $-e$.

# Requirements and set-up

The commands are for a Linux shell: Ubuntu under WSL on Windows (start "Ubuntu" from the Start menu), native Linux, or
the macOS terminal. Every block can be copied and pasted as a whole.

**Step S1 (once, about 5 minutes): system packages.** This installs git, Python, pandoc and the TeX Live parts the
document build needs (on macOS use Homebrew instead: `brew install git python pandoc` and the MacTeX distribution).

```text
sudo apt-get update
sudo apt-get install -y git python3 python3-venv python3-pip pandoc \
    texlive-latex-base texlive-latex-recommended texlive-latex-extra \
    texlive-fonts-recommended lmodern
```

**Step S2 (once, about 2 minutes): a Python environment with the packages of the computations.** A virtual environment
keeps these packages separate from the system Python.

```text
python3 -m venv ~/um2env
source ~/um2env/bin/activate
pip install sympy numpy scipy mpmath matplotlib camb
```

In every new terminal, activate it again with `source ~/um2env/bin/activate` before running the commands below.

The reference runs used Python 3.13.16, sympy 1.14.0, numpy 2.5.3, scipy 1.18.1, mpmath 1.3.0, matplotlib 3.11.2,
camb 2.0.5, pandoc 3.1.3 and pdfTeX 1.40.25 (TeX Live 2023). With other versions the numbers agree to the tolerance used
below, while the PDF and LaTeX files may differ in their bytes (not in their content).

# Task 1: the fresh-clone verification

**What it establishes.** Every stored number of UM-2 is reproduced from the code alone, every named check passes, every
computation finishes within its time limit, and the documents are rebuilt from their Markdown sources.

**Step 1.1 (about 1 minute): a fresh clone, separate from any working copy.**

```text
cd ~
rm -rf um2_check
git clone https://github.com/once-ere/Dirac_claude.git um2_check
cd ~/um2_check/universe_model_2
git log --oneline -1 > ~/um2_check_commit.txt
cat ~/um2_check_commit.txt
```

**Step 1.2 (once per terminal): a helper that runs one computation with a time limit and records its exit code and
duration.** Each computation is stopped if it runs longer than 423 s (7 minutes 3 seconds), well inside the 12-minute
limit; the exit code is 0 if and only if every named check of that computation passes.

```text
cd ~/um2_check/universe_model_2
run() {
  local t0=$(date +%s)
  timeout -k 5 423 python3 "$@" > ~/um2_log_$(echo "$*" | tr ' /' '__').txt 2>&1
  local rc=$?
  echo "$* exit=$rc $(( $(date +%s) - t0 )) s" | tee -a ~/um2_times.txt
}
: > ~/um2_times.txt
```

**Step 1.3: the computations, one block at a time, in this order** (each block depends on the outputs of the blocks
before it; the expected durations are those of the run of 2026-10-18).

| block | commands | expected time | checks |
| ---- | -------------------------------------------------- | ------------ | -------- |
| 1 | `run code/um2_algebra.py` | 53 s | 31 |
| 2 | `run code/um2_geometry.py` | 71 s | 25 |
| 3 | `run code/um2_background.py` | 126 s | 22 |
| 4 | `run code/um2_fields.py` | 50 s | 15 |
| 5 | `run code/um2_spectra.py` | 27 s | 14 |
| 6 | `run code/um2_ks_jobs.py validate` and `run code/um2_ks_jobs.py spectrum` | 77 s, 1 s | 2, 3 |
| 7 | `run code/um2_ks_jobs.py ground8` | 125 s | 3 |
| 8 | `run code/um2_ks_jobs.py ground592` | 129 s | 4 |
| 9 | `run code/um2_ks_jobs.py darkmatter`, `run code/um2_ks_jobs.py portals`, `run code/um2_ks_jobs.py feedback` | 15 s, 5 s, 0.4 s | 3, 5, 2 |
| 10 | `run code/um2_electroweak.py` | 1 s | 20 |
| 11 | `run code/um2_primordial.py` | 248 s | 5 |
| 12 | `run code/um2_cosmology.py` and `run code/um2_analysis.py` | 11 s, 4 s | 5, 23 |
| 13 | `run tools/build_docs.py` | 12 s | |

The check counts are those of the run of 2026-10-18; the counts in force are printed by step 1.4. For example, block 1:

```text
run code/um2_algebra.py
```

**Step 1.4 (seconds): the summary of the checks.** Every report must say `0 failed`; the last line gives the total.

```text
grep -h "checks, " ~/um2_log_*.txt
grep -h "checks, " ~/um2_log_*.txt | awk '{s += $2; f += $4} END {print "TOTAL", s, "checks,", f, "failed"}'
cat ~/um2_times.txt
```

**Step 1.5 (seconds): the comparison with the committed files.** The script lists every file the rerun changed and
compares the numbers of every changed JSON file with the committed values to a relative tolerance of $10^{-9}$.

```text
cd ~/um2_check
python3 universe_model_2/tools/compare_outputs.py
```

Expected result: `result: REPRODUCED`. In the run of 2026-10-18 only run times, the free-text details of two Kohn-Sham
validation checks (round-off at the $10^{-14}$ level) and one Kohn-Sham integral (a relative difference of
$1.1\times10^{-12}$, caused by threaded linear algebra that does not sum in a fixed order) differed; the LaTeX sources, the
PDF documents and the figures were byte-identical. With other software versions, files reported as `CHANGED (not JSON)`
(PDF, LaTeX, PNG) are expected and are not errors; open them to confirm that their content is the same.

**Step 1.6: what to report back.** The contents of `~/um2_check_commit.txt`, `~/um2_times.txt`, the output of steps 1.4
and 1.5, and, for any computation with a non-zero exit code, the last 40 lines of its log
(`tail -40 ~/um2_log_<name>.txt`).

# Task 2: the independent review of the documents

**What it establishes.** That the statements, equations and numbers of the five documents (MODEL, PROVENANCE,
FIELD_EQUATIONS, SOLUTION, ANALYSIS) agree with the computed outputs and with each other, that the mathematics written
in them is correct, and that each document is self-contained. The agent's assignment (2026-10-18) was a read-only review
of the changes since commit `fa7305f`, with six items; they are written out below as a procedure. Each item takes 5 to
10 minutes by hand. Work in the fresh clone of task 1 (step 1.1) or in any up-to-date clone:

```text
cd ~/um2_check/universe_model_2
```

**Item 2.1: the electroweak parameter and the $W^\pm$, $Z$ fit.** The tip term of the sigma field gives the $x_0$
eigenvalue problem of the $W^\pm$ and $Z$ profiles the tip coefficients $\beta_W$ and $\beta_Z = \beta_W/\cos^2\theta_W$, with
$\theta_W$ the angle of the gauge couplings; the eigenvalues $\Lambda_W$, $\Lambda_Z$ are the masses in units of the proper half
cell, $\Lambda = (m\,fL)^2$, and
$$ \rho = \frac{\Lambda_W}{\Lambda_Z\cos^2\theta_W},\qquad m_{KK} = m_W\sqrt{\Lambda_1/\Lambda_W},\qquad m_Z^{model} = m_W\sqrt{\Lambda_Z/\Lambda_W}, $$
with $\Lambda_1$ the first even Kaluza-Klein eigenvalue. Print what the code computes:

```text
python3 -c "import json; print(json.load(open('outputs/masses.json'))['WZ'])"
grep -n "c2 = \|rho_minus_1\|def LamW" code/um2_spectra.py
grep -n "rho = \|cos^2\\\\theta_W\|m_Z" MODEL.md SOLUTION.md ANALYSIS.md FIELD_EQUATIONS.md PROVENANCE.md
```

Check: (a) the angle the code uses (the variable `c2` in `code/um2_spectra.py`) is the angle the documents name; (b) the
documents' $\beta_W$, $\beta_Z$, $\Lambda_W$, $\Lambda_Z$, $\rho - 1$, $m_{KK}$ and $m_Z^{model}$ equal the printed values (rounded); (c) the
comparison of $m_Z^{model}$ with the measured $m_Z = 91.1879 \pm 0.0020$ GeV is stated and is correct.

**Item 2.2: the uncertainty relation on the cell.** With the scaled hidden coordinate $\xi = y/L \in [-1, 0]$ (fold at
$\xi = 0$, tip at $\xi = -1$), a normalised probability density $\varrho$ ($\int_{-1}^{0}\varrho\,d\xi = 1$), the spread
$\Delta\xi^2 = \int_{-1}^{0}\xi^2\varrho\,d\xi$ and the hidden kinetic term $\langle p^2\rangle$ (bosons: $\varrho = \tilde u^2/\!\int\tilde u^2$ with
$\tilde u = e^{3\eta\xi/2}u$ and $\langle p^2\rangle = \int\tilde u'^2/\!\int\tilde u^2$; fermions: $\varrho = |\chi|^2/\!\int|\chi|^2$ and
$\langle p^2\rangle = \int|\chi'|^2/\!\int|\chi|^2$; primes $d/d\xi$), the documents state
$$ \sqrt{\langle p^2\rangle}\,\Delta\xi \ge \frac{1 - \varrho(\text{tip})}{2}. $$
Verify the derivation by hand: integration by parts gives $1 = \int_{-1}^{0}\varrho\,d\xi = [\xi\varrho]_{-1}^{0} - \int_{-1}^{0}\xi\varrho'\,d\xi
= \varrho(-1) - \int_{-1}^{0}\xi\varrho'\,d\xi$; with $\varrho' = 2\tilde u\tilde u'/\!\int\tilde u^2$ (or $2\,\mathrm{Re}\,\chi^\dagger\chi'/\!\int|\chi|^2$) the
Cauchy-Schwarz inequality gives $\lvert\int\xi\varrho'\,d\xi\rvert \le 2\Delta\xi\sqrt{\langle p^2\rangle}$. Also verify the boson Rayleigh
quotient $(m\,fL)^2 = \big[\int e^{3\eta\xi}u'^2d\xi + \beta e^{-3\eta}u(-1)^2\big]/\!\int e^{3\eta\xi}u^2d\xi$ and its decomposition
$(m\,fL)^2 = \langle p^2\rangle + \tfrac{9\eta^2}{4} - \tfrac{3\eta}{2}\varrho(0) + (\tfrac{3\eta}{2} + \beta)\varrho(-1)$, which follows from
$e^{3\eta\xi}u'^2 = \tilde u'^2 + \tfrac94\eta^2\tilde u^2 - \tfrac32\eta(\tilde u^2)'$. Then compare the numbers:

```text
python3 - <<'EOF'
import json
d = json.load(open('outputs/analysis.json'))['decomposition']
for k, v in d.items():
    print('%-45s rho_tip %.4g  <p2>Dxi2 %.4g  lhs %.4f  bound %.4f' % (
        k, v['rho_tip'], v['p2_Dt2'], v['uncertainty_lhs'], v['uncertainty_bound']))
EOF
python3 -c "import json; [print(c['name'], c['passed']) for c in json.load(open('reports/analysis-checks.json'))['checks'] if 'uncertainty' in c['name']]"
```

Check: every state satisfies `lhs >= bound`; the table of ANALYSIS section 2.3 (columns $\varrho(\text{tip})$ and
$\langle p^2\rangle\Delta\xi^2$) shows these values; the documents do not claim that $\langle p^2\rangle \ge 1/(4\Delta\xi^2)$ holds for every state
(the broad fold zero mode of dirac16complex violates it).

**Item 2.3: notation and cross-references.** Search for leftovers of earlier notation (each command should print
nothing, or only lines where the symbol has the meaning given in the document's list of symbols with more than one use):

```text
grep -n 't = y/L\|\\eta t\|Delta t\b' *.md
grep -n 'wgf\\varepsilon\|wgf\[\|wgf\\big\|E_{KS} = \\sum g f\\varepsilon' *.md
grep -n 'r_3(n^2)' *.md
grep -n 'tau = 0.0544' *.md
grep -n '^#' MODEL.md FIELD_EQUATIONS.md ANALYSIS.md
```

Check: each document has a list of symbols with more than one use (near its beginning) whose claims are true for that
document; the section numbers cited in the documents match the numbering of the last command (pandoc numbers the
sections in order, "How to read this document" being section 1).

**Item 2.4: the cell volume.** On the static block the metric is
$ds^2 = e^{2a_4}d\vec x^{\,2} - dx_4^2 + f^2\big[dy^2 - e^{2Hy}d\vec x_t^{\,2}\big]$, so the proper volume element of a slice
$x_4 = \text{const}$ is $e^{3a_4}f^4e^{3Hy}\,dy\,d^3x\,d^3x_t$. With $\mathrm{Vol}_7 = (2\pi/\Delta k)^3v_tf^4$ (at $a_4 = 0$; $v_t$ the
coordinate volume of the extra times) the proper seven-volume of one cell (two halves) is
$2\,\mathrm{Vol}_7\int_{-L}^{0}e^{3Hy}dy = 2\,\mathrm{Vol}_7(1 - e^{-3\eta})/(3H)$, $\eta = HL$, and the transverse volume of the
four-dimensional reduction is $V_\perp = 2f^4v_t(1 - e^{-3\eta})/(3H)$. Check these statements in MODEL (Kohn-Sham section),
FIELD_EQUATIONS (section 7) and SOLUTION (step 3), and the number $\mathrm{Vol}_7 = 34.27$ ($\Delta k = 0.25H$, $v_t = 1$, $H = 1$):

```text
python3 -c "import json, math; f = json.load(open('outputs/background.json'))['casimir_type']['f_star']; print(f, (2*math.pi/0.25)**3 * f**4)"
```

**Item 2.5: the CMB statements.** The relative deviation of a spectrum is $\delta_\ell = C_\ell/C_\ell^{\Lambda CDM} - 1$, the cosmic
variance of one multipole $\sqrt{2/(2\ell + 1)}$. Print the stored values:

```text
python3 - <<'EOF'
import json
c = json.load(open('outputs/cosmology.json'))
for k in ('max_rel_dev_TT', 'max_rel_dev_EE', 'max_dev_in_cosmic_variance_units', 'PsiB_variant_max_rel_dev_TT',
          'PsiB_variant_max_dev_in_cosmic_variance_units', 'PsiB_variant_TT_chi2_cosmic_variance_full_sky'):
    print(k, c[k])
lcdm, um2, var = c['models']
for (l, a), (_, b) in zip(lcdm['cl_TT_l'], var['cl_TT_l']):
    print('l = %4d  variant/LCDM - 1 = %+.4f   cosmic variance %.4f' % (l, b / a - 1, (2 / (2 * l + 1)) ** 0.5))
EOF
```

Check: the maxima are taken over $30 \le \ell \le 2500$ (see `code/um2_cosmology.py`, the line `sel = (l >= 30) & (l <= 2500)`), and
the documents state that range; the cosmic-variance fraction quoted for UM-2 refers to TT (the code computes it for TT).

**Item 2.6: the built files.** Rebuild and inspect:

```text
python3 tools/build_docs.py
grep -c '\\\$' MODEL.tex PROVENANCE.tex FIELD_EQUATIONS.tex SOLUTION.tex ANALYSIS.tex
grep -n 'textbackslash' MODEL.tex PROVENANCE.tex FIELD_EQUATIONS.tex SOLUTION.tex ANALYSIS.tex
```

Check: every document reports `overfull boxes: 0`; there is no `\$` (an unparsed dollar sign) in the LaTeX files of the
five model documents (this document contains it once, in the text of this check);
`textbackslash` appears only inside `\texorpdfstring{...}{...}` (the plain-text PDF bookmarks of section titles).

**What to report back.** For each item: OK, or the file, the line, what is wrong and the proposed correction.

# The agent's findings of 2026-10-18 and their incorporation

The review agent reported four errors and ten minor items for the documents at commit `9285bb6`:

1. **The familiar uncertainty bound.** The documents said that $\langle p^2\rangle \ge 1/(4\Delta\xi^2)$ "holds only" for profiles
   negligible at the tip; states with a large tip density can satisfy it too (first even Kaluza-Klein mode: $\varrho(\text{tip}) = 0.655$,
   $\langle p^2\rangle\Delta\xi^2 = 4.59$). Correct wording: the bound is guaranteed only for such profiles.
2. **The symbol list of PROVENANCE** said that $\rho_0$ is the electroweak parameter (PROVENANCE uses $\rho$) and named the lattice
   vector $\vec n$, which PROVENANCE does not use, while $n$ is used there as a level index and as the basis size of the
   Richardson formula.
3. **Primes.** Lists stating that primes denote $d/d\xi$ overlooked $G'(k_*)$ and $U'(S)$ (ANALYSIS) and the reduced actions,
   whose $u'$ is $du/dy$ (FIELD_EQUATIONS section 6, MODEL section 6.1).
4. **The electroweak fit.** With the angle of the couplings set equal to the on-shell angle of the measured masses,
   $\cos^2\theta_W = m_W^2/m_Z^2$, a fit of $\rho - 1$ to the measured $\rho_0 - 1 = 0.00038$ makes the model's $m_Z = 91.1706$ GeV, 17 MeV
   below the measured $91.1879 \pm 0.0020$ GeV; the documents did not say so. ($\rho_0$ measures the custodial violation beyond
   the Standard-Model loops; in a tree-level model it is the tree-level $\rho$ with the angle of the couplings.)

Minor items: the probability density was defined twice in ANALYSIS (unnormalised in section 2.1); the largest TT
deviation of the thermalised-$\Psi_B$ variant lies at the edge $\ell = 2500$ of the range; the cosmic-variance fraction 0.011
refers to TT only (EE: 0.018); gaps in the lists of symbols; $\mathrm{Vol}_7$ not defined in PROVENANCE; the verification
statements credited an older commit; "true lower bound" wording for $m \ge m_H$, which is observed for the computed states,
not derived; the sign convention of $w_a$; old notation in the report texts of two checks; "every state" meaning every
tabulated state.

All four errors and the minor items were incorporated on 2026-10-18 (PROVENANCE, corrections, item 20). For error 4 the
computation was changed, not only the text: the angle of the couplings is now fixed by the measured masses and $\rho_0$,
$\cos^2\theta_W = (m_W^2/m_Z^2)/\rho_0 = 0.776368$, so that the model reproduces both $m_W$ and $m_Z$; every scale in GeV moved by
$+8.5\times10^{-4}$ ($m_{KK} = 121.32$ TeV, $H = 14.296$ TeV) and the dependent computations were rerun.
