---
title: "UM-2 manual tasks"
subtitle: "How to carry out by hand the two long tasks of the UM-2 work: the fresh-clone verification of every computation and document, and the independent review of the documents against the computed outputs"
author:
  - "Underlying theory: Patrick L. Nash"
  - "Written by Claude (Anthropic)"
  - "Manual tasks, version 3, 2026-10-18 (versions 1 and 2: 2026-10-18)"
  - "Repository once-ere/Dirac_claude, folder universe_model_2"
---

# How to read this document

Two tasks of the UM-2 work are long when they are run as single jobs:

* **Task 1, the fresh-clone verification**: all 22 computations of version 4 and the document build took 1136 s
  (about 19 minutes) on 2026-10-18 at commit `cec385b`, although every individual computation takes at most about
  4.5 minutes (the primordial integration, 257 s).
* **Task 2, the independent review**: a review agent that read the five model documents of version 3, compared their
  statements with the computed outputs and recomputed key numbers independently ran for 2055 s (about 34 minutes, 74 tool
  calls) on 2026-10-18 at commit `726997f`.

When this document was first written the author's rule was that no individual calculation may take longer than
12 minutes and 3 seconds (later 7 minutes and 3 seconds); the author lifted the limit on 2026-10-18. The steps below are
still kept short, so that each can be executed by hand and its result reported back for incorporation into the project.
This document is self-contained: every command, every equation and every reference value it needs is written here.
Wherever a value can change when the computations are updated, the command that prints it from the repository is given
instead of the value.

Version 2 (2026-10-18) covered UM-2 version 2: three generations of quarks and leptons, three neutrino flavours with their
mixing and flavour conversion, and the dark matter of both halves of dirac16complex (review items 2.6 to 2.8). Version 3
(2026-10-18) covers UM-2 version 3: the portal I13, which gives the dark-matter relic within the unitarity limit, the
thermal history with the freeze-in of the fold bands, the coupled Kohn-Sham solution in ten environments and the metric as a
power series. It adds the computations `um2_thermal.py`, `um2_coupled.py` and `um2_series.py` to task 1, rewrites item 2.8, adds
items 2.10 to 2.12, and records the findings of the reviews of versions 1, 2 and 3 and their incorporation.

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

**What it establishes.** Every stored number of UM-2 is reproduced from the code alone, every named check passes, and
the documents are rebuilt from their Markdown sources.

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
duration.** Each computation is stopped if it runs longer than 900 s (15 minutes, three times the longest expected
duration); the exit code is 0 if and only if every named check of that computation passes.

```text
cd ~/um2_check/universe_model_2
run() {
  local t0=$(date +%s)
  timeout -k 5 900 python3 "$@" > ~/um2_log_$(echo "$*" | tr ' /' '__').txt 2>&1
  local rc=$?
  echo "$* exit=$rc $(( $(date +%s) - t0 )) s" | tee -a ~/um2_times.txt
}
: > ~/um2_times.txt
```

**Step 1.3: the computations, one block at a time, in this order** (each block depends on the outputs of the blocks
before it; the expected durations are those of the run of 2026-10-18 at commit `cec385b`).

| block | commands | expected time | checks |
| ---- | -------------------------------------------------- | ------------ | -------- |
| 1 | `run code/um2_algebra.py` | 54 s | 31 |
| 2 | `run code/um2_geometry.py` | 72 s | 25 |
| 3 | `run code/um2_background.py` | 133 s | 22 |
| 4 | `run code/um2_fields.py` | 53 s | 16 |
| 5 | `run code/um2_spectra.py` | 27 s | 14 |
| 6 | `run code/um2_flavour.py` and `run code/um2_neutrino.py` | 5 s, 30 s | 7, 16 |
| 7 | `run code/um2_ks_jobs.py validate` and `run code/um2_ks_jobs.py spectrum` | 39 s, 0.8 s | 2, 3 |
| 8 | `run code/um2_ks_jobs.py ground8` | 165 s | 3 |
| 9 | `run code/um2_ks_jobs.py ground592` | 142 s | 4 |
| 10 | `run code/um2_ks_jobs.py darkmatter`, `run code/um2_ks_jobs.py portals`, `run code/um2_ks_jobs.py feedback` | 17 s, 4 s, 0.4 s | 3, 5, 2 |
| 11 | `run code/um2_electroweak.py` | 1.1 s | 19 |
| 12 | `run code/um2_primordial.py` | 257 s | 5 |
| 13 | `run code/um2_cosmology.py` and `run code/um2_analysis.py` | 44 s, 3.5 s | 8, 23 |
| 14 | `run code/um2_thermal.py`, `run code/um2_coupled.py` and `run code/um2_series.py` | 13 s, 23 s, 0.4 s | 7, 17, 4 |
| 15 | `run code/um2_residuals.py` (the residuals of the solution and the links between the equations) | 9 s | 52 |
| 16 | `run tools/build_docs.py` | 43 s | |

The check counts add up to 288 (287 at the verification of commit `cec385b`; the consistency pass of version 4 added the check
`C11_I12_benchmark_direct_detection` of `um2_coupled.py`); the counts in force are printed by step 1.4. Afterwards check the symbol lists of the documents
(every display equation followed by the complete list of its symbols; about 10 seconds):

```text
python3 universe_model_2/tools/symbols_tool.py check
```

Expected last line: `symbols_check=OK (841 display equations, ...)`. For example, block 1:

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

Expected result: `result: REPRODUCED`. In the run of version 4 at commit `cec385b` only the run times differed (every stored
number identical); in the runs of version 3 at `726997f` and `815db9e` (as in the run of version 2 at `4a6421d`) also the texts of
two check details and one Kohn-Sham integral (a relative difference of $1.1\times10^{-12}$, caused by threaded linear algebra that
did not sum in a fixed order; version 4 fixes the thread count) differed; the LaTeX sources, the PDF documents and the figures
were byte-identical. With other software versions, files
reported as `CHANGED (not JSON)` (PDF, LaTeX, PNG) are expected and are not errors; open them to confirm that their content
is the same.

**Step 1.6: what to report back.** The contents of `~/um2_check_commit.txt`, `~/um2_times.txt`, the output of steps 1.4
and 1.5, and, for any computation with a non-zero exit code, the last 40 lines of its log
(`tail -40 ~/um2_log_<name>.txt`).

# Task 2: the independent review of the documents

**What it establishes.** That the statements, equations and numbers of the five model documents (MODEL, PROVENANCE,
FIELD_EQUATIONS, SOLUTION, ANALYSIS) agree with the computed outputs and with each other, that the mathematics written in
them is correct, and that each document is self-contained (every equation it uses is written in it, and it never sends
the reader to another document for content). Each item takes 5 to 15 minutes by hand. Work in the fresh clone of task 1
(step 1.1) or in any up-to-date clone:

```text
cd ~/um2_check/universe_model_2
```

**Item 2.1: the electroweak parameter, the $W^\pm$, $Z$ fit and the $Z$ widths.** The tip term of the sigma field gives the
$x_0$ eigenvalue problem of the $W^\pm$ and $Z$ profiles the tip coefficients $\beta_W$ and $\beta_Z = \beta_W/\cos^2\theta_W$, with $\theta_W$
the angle of the gauge couplings; the eigenvalues $\Lambda_W$, $\Lambda_Z$ are the masses in units of the proper half cell,
$\Lambda = (m\,fL)^2$, and
$$ \rho = \frac{\Lambda_W}{\Lambda_Z\cos^2\theta_W},\qquad \cos^2\theta_W = \frac{m_W^2/m_Z^2}{\rho_0},\qquad m_{KK} = m_W\sqrt{\Lambda_1/\Lambda_W},\qquad m_Z^{model} = m_W\sqrt{\Lambda_Z/\Lambda_W}, $$
with $\Lambda_1$ the first even Kaluza-Klein eigenvalue and $\rho_0 - 1 = 0.00038$ the measured value. The tree-level partial
widths are $\Gamma(Z\to f\bar f) = N_c\,G_Fm_Z^3(g_V^2 + g_A^2)/(6\sqrt2\pi)$, $g_V = T_3 - 2Q\sin^2\theta_W$, $g_A = T_3$, summed over the three
generations (the top quark excluded). Print what the code computes:

```text
python3 -c "import json; print(json.load(open('outputs/masses.json'))['WZ'])"
python3 -c "import json; e = json.load(open('outputs/electroweak.json')); print({k: e[k] for k in e if 'width' in k.lower() or 'N_nu' in k})"
grep -n "c2 = \|rho_minus_1\|def LamW" code/um2_spectra.py
grep -n "rho = \|cos^2\\\\theta_W\|m_Z" MODEL.md SOLUTION.md ANALYSIS.md FIELD_EQUATIONS.md PROVENANCE.md
```

Check: (a) the angle the code uses (the variable `c2` in `code/um2_spectra.py`) is the angle the documents name; (b) the
documents' $\beta_W$, $\beta_Z$, $\Lambda_W$, $\Lambda_Z$, $\rho - 1$, $m_{KK}$ and $m_Z^{model}$ equal the printed values (rounded), and $m_Z^{model}$ equals the
measured $91.1879$ GeV; (c) the $Z$ widths of the documents (invisible about 498 MeV, total about 2485 MeV with the factor
$1 + \alpha_s/\pi$ on the quarks) equal the printed values.

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

Check: every state satisfies `lhs >= bound`; the tables of the ANALYSIS section on the uncertainty relation (columns
$\varrho(\text{tip})$ and $\langle p^2\rangle\Delta\xi^2$) show these values; the documents do not claim that $\langle p^2\rangle \ge 1/(4\Delta\xi^2)$ holds for
every state (the broad fold zero mode of dirac16complex violates it).

**Item 2.3: notation, coordinates and cross-references.** Search for leftovers of earlier notation and for relabelled
coordinates (each command should print nothing, or only lines where the symbol has the meaning given in the document's
list of symbols with more than one use):

```text
grep -n 't = y/L\|\\eta t\|Delta t\b' *.md
grep -n 'd\\psi/dt\|/dt\b\|\\Omega t\|Kz\b' *.md
grep -n 'r_3(n^2)' *.md
grep -n '^#' MODEL.md FIELD_EQUATIONS.md SOLUTION.md ANALYSIS.md
```

Check: the time is always written $x_4$ (never $t$) and the symmetry axis of the fast-flavour analysis $x_3$ (never $z$, which
means $6Hx_0$); each document has a list of symbols with more than one use (near its beginning) whose claims are true for
that document; the section numbers cited in the documents match the numbering of the last command (pandoc numbers the
sections in order, "How to read this document" being section 1); no document sends the reader to another document for an
equation or a value.

**Item 2.4: the cell volume.** On the static block the metric is
$ds^2 = e^{2a_4}d\vec x^{\,2} - dx_4^2 + f^2\big[dy^2 - e^{2Hy}d\vec x_t^{\,2}\big]$, so the proper volume element of a slice
$x_4 = \text{const}$ is $e^{3a_4}f^4e^{3Hy}\,dy\,d^3x\,d^3x_t$. With $\mathrm{Vol}_7 = (2\pi/\Delta k)^3v_tf^4$ (at $a_4 = 0$; $v_t$ the
coordinate volume of the extra times) the proper seven-volume of one cell (two halves) is
$2\,\mathrm{Vol}_7\int_{-L}^{0}e^{3Hy}dy = 2\,\mathrm{Vol}_7(1 - e^{-3\eta})/(3H)$, $\eta = HL$, and the transverse volume of the
four-dimensional reduction is $V_\perp = 2f^4v_t(1 - e^{-3\eta})/(3H)$. Check these statements in the Kohn-Sham sections of
MODEL, FIELD_EQUATIONS and SOLUTION, and the number $\mathrm{Vol}_7 = 34.27$ ($\Delta k = 0.25H$, $v_t = 1$, $H = 1$):

```text
python3 -c "import json, math; f = json.load(open('outputs/background.json'))['casimir_type']['f_star']; print(f, (2*math.pi/0.25)**3 * f**4)"
```

**Item 2.5: the CMB statements.** The relative deviation of a spectrum is $\delta_\ell = C_\ell/C_\ell^{\Lambda CDM} - 1$, the cosmic
variance of one multipole $\sqrt{2/(2\ell + 1)}$. The stored models are, in this order, $\Lambda$CDM (CAMB defaults), UM-2 (three
massive neutrinos, no dark radiation) and two variants with a thermalised fold band of dirac16complex (decoupled above the
electroweak scale and above the QCD crossover). Print the stored values:

```text
python3 - <<'EOF'
import json
c = json.load(open('outputs/cosmology.json'))
for k in ('max_rel_dev_TT', 'max_rel_dev_EE', 'max_dev_in_cosmic_variance_units', 'UM2_max_rel_dev_TT',
          'dark_radiation_QCD_max_rel_dev_TT', 'dark_radiation_QCD_max_dev_in_cosmic_variance_units',
          'dark_radiation_QCD_TT_chi2_cosmic_variance_full_sky'):
    print(k, c[k])
lcdm, um2, var_ew, var_qcd = c['models']
for m in c['models']:
    print(m['name'], ' BAO chi2 =', m['bao_chi2'], ' H0 =', m['H0'])
for (l, a), (_, b) in zip(lcdm['cl_TT_l'], var_qcd['cl_TT_l']):
    print('l = %4d  QCD variant/LCDM - 1 = %+.4f   cosmic variance %.4f' % (l, b / a - 1, (2 / (2 * l + 1)) ** 0.5))
EOF
```

Check: the maxima are taken over $30 \le \ell \le 2500$ (see `code/um2_cosmology.py`, the line `sel = (l >= 30) & (l <= 2500)`), and
the documents state that range; the cosmic-variance fraction quoted for UM-2 refers to TT (the code computes it for TT);
the BAO $\chi^2$ of the documents (UM-2 31.72 for 13 points, $\Lambda$CDM 32.55) equal the printed values.

**Item 2.6: three generations, masses and mixing.** With one doublet localisation per sector ($c_L$ for the leptons, $c_Q$ for
the quarks) and a unitary tip matrix $\kappa$, the mass of each fermion is the root of
$$ D(e) = e^2s_Ls_R - (C_L - c_Ls_L)(C_R + c_Rs_R) = 0,\qquad s = \frac{\sinh w}{w},\quad C = \cosh w,\quad w = \sqrt{c^2 - e^2},\qquad e = m\,fL, $$
whose first-order solution is $e \simeq \zeta(c_L)\zeta(-c_R)$, $\zeta(c)^2 = c\,e^{-c}/\sinh c$; the mixing matrices are $U = \kappa_e^\dagger\kappa_\nu$ and
$V = \kappa_u^\dagger\kappa_d$, equal to $\kappa_\nu$ and $\kappa_d$ only with $\kappa_e = \kappa_u = 1$ (ASSUMED). Verify by hand that for $c \gg 1$
$\zeta(c)^2 \simeq 2c\,e^{-2c}$, and print the stored values:

```text
python3 - <<'EOF'
import json
m = json.load(open('outputs/masses.json'))['fermions']
for k, v in m.items():
    print('%-4s m = %.6g GeV  c_L = %.4f  c_R = %.4f  e_exact = %.6g  e_first_order = %.6g' % (
        k, v['m_GeV'], v['c_L'], v['c_R'], v['e_exact'], v['e_first_order']))
f = json.load(open('outputs/flavour.json'))
print('PMNS angles', f['PMNS']['angles_deg'], ' J =', f['PMNS']['J'], ' J_max =', f['PMNS']['J_max'])
print('CKM J =', f['CKM']['J'])
for k, v in f['three_generation_tip_condition'].items():
    print(k, 'null vectors vs kappa columns:', v['null_vector_deviation_from_kappa_columns'])
EOF
```

Check: the twelve masses, localisations and the mixing values of the documents equal the printed ones; the documents say
which $J_{max}$ is computed from the best-fit angles (about $0.0335$) and which is NuFIT's marginalised value ($0.0333 \pm 0.0007$); the
three-generation determinant is said to reproduce the one-generation roots (to $3.0\times10^{-42}$ in the 50-digit computation).

**Item 2.7: the flavour conversion of the three neutrinos.** The flavour amplitudes of a neutrino of energy $E$ evolve with
$i\,d\psi/dx_4 = [U\,\mathrm{diag}(m_1^2, m_2^2, m_3^2)U^\dagger/(2E) + \mathrm{diag}(V_{CC}, 0, 0)]\psi$, $V_{CC} = \sqrt2G_Fn_e$. Verify by hand: (a) the vacuum
probability $P(\nu_\alpha\to\nu_\beta) = \lvert\sum_iU_{\beta i}U^*_{\alpha i}e^{-im_i^2L/(2E)}\rvert^2$ and the T-odd difference
$P(\nu_\mu\to\nu_e) - P(\nu_e\to\nu_\mu) = -16J\sin\Delta_{21}\sin\Delta_{31}\sin\Delta_{32}$, $\Delta_{ij} = \Delta m^2_{ij}L/(4E)$; (b) the 1-3 resonance condition
$2EV_{CC} = \Delta m^2_{ee}\cos2\theta_{13}$, $\Delta m^2_{ee} = c_{12}^2\Delta m^2_{31} + s_{12}^2\Delta m^2_{32}$ (about 11.1 GeV at 2.8 g/cm$^3$, $Y_e = 0.5$);
(c) the adiabatic solar survival probability $P_{ee} = c_{13}^4(\frac12 + \frac12\cos2\theta_{12}\cos2\theta^m_{12}) + s_{13}^4$ with
$\cos2\theta^m_{12} = (\cos2\theta_{12} - A)/\sqrt{(\cos2\theta_{12} - A)^2 + \sin^22\theta_{12}}$, $A = 2EV_{CC}c_{13}^2/\Delta m^2_{21}$; (d) the CNB density
$n_i = 3\zeta(3)T_\nu^3/(2\pi^2)$ per mass state with $T_\nu = (4/11)^{1/3}T_{CMB}$ (about 112 cm$^{-3}$). Print the stored values:

```text
python3 - <<'EOF'
import json
n = json.load(open('outputs/neutrino.json'))
print('masses (eV)', n['masses_eV'], ' sum', n['sum_masses_eV'])
print('MSW', n['MSW_resonance'])
for k, v in n['long_baseline'].items():
    print(k, 'P(mu->e) =', v['P_mue_nu'], ' Pbar =', v['P_mue_antinu'], ' vacuum =', v['P_mue_nu_vacuum'])
for s in n['solar']:
    print('solar', s)
print('onset T (MeV)', n['oscillation_onset_T_MeV'])
print('N_eff computed', n['N_eff_UM2_computed'], ' adopted', n['N_eff_adopted']['value'])
print('CNB', {k: n['CNB'][k] for k in ('T_nu_K', 'n_per_mass_state_cm3', 'Omega_nu_h2')})
print('supernova', n['supernova_MSW']['P_ee_normal_ordering'], n['supernova_MSW']['Pbar_ee_normal_ordering'])
for k, v in n['fast_flavour_instability'].items():
    print(k, ' max growth', v['max_growth_any_k'], ' at k', v['k_at_max'])
EOF
```

Check: every number of the flavour-conversion sections of the documents equals the printed value (rounded); the adiabatic
and numerical solar values are distinguished; the fast-flavour dispersion relation is written with $\omega = \Omega - \Lambda^0$,
$k = K - \Lambda^3$ (upper indices) and $\eta^{\mu\nu} = \mathrm{diag}(1, -1)$ on $(x_4, x_3)$.

**Item 2.8: the dark-matter relic and unitarity.** The operator $G\,\bar\chi\chi F_{\mu\nu}F^{\mu\nu}$ (portal I12) annihilates a Dirac pair in the
p-wave, $\sigma v = G^2s(s - 4M^2)/(4\pi) \to G^2M^4v^2/\pi$, and only from the state $^3P_0$ ($J = 0$); partial-wave unitarity averaged over the four
spin states then bounds $\sigma \le \pi/(4p^2)$, $p = Mv/2$, i.e. $\sigma v \le \pi/(M^2v)$, whose thermal average over $f(v) \propto v^2e^{-xv^2/4}$ is
$$ \Big\langle\frac{\pi}{M^2v}\Big\rangle = \frac{\sqrt{\pi x}}{M^2} . $$
Verify the average by hand (the integrals $\int_0^\infty v\,e^{-xv^2/4}dv = 2/x$ and $\int_0^\infty v^2e^{-xv^2/4}dv = 2\sqrt\pi\,x^{-3/2}$, with
$1\ \text{GeV}^{-2} = 1.1673\times10^{-17}$ cm$^3$/s for $\sigma v$). Version 3 solves the Boltzmann equation numerically,
$$ \frac{dY}{dx} = -\frac{(1 + \delta)\,s\,\langle\sigma v\rangle}{2xH}\big(Y^2 - Y_{eq}^2\big),\qquad x = \frac{M}{T},\qquad
   1 + \delta = 1 + \frac13\frac{d\ln g_s}{d\ln T}, $$
for each of the two dark-matter species (particle plus antiparticle, $Y = n/s$, $H$ the Hubble rate of the plasma with $g_\rho(T)$, $s$ the entropy
density with $g_s(T)$), with the relativistic (Gondolo-Gelmini) thermal average
$\langle\sigma v\rangle = \int_{4M^2}^\infty \sigma(s)\,(s - 4M^2)\sqrt s\,K_1(\sqrt s/T)\,ds\,/\,\big(8M^4TK_2(M/T)^2\big)$, and finds: (a) with
I12 at the strength of the relic (an effective cross-section) the cross-section exceeds the $^3P_0$ bound above $\sqrt s = 89510$ GeV, i.e. above the
relative velocity $v = 2\beta = 0.269$, $\beta = \sqrt{1 - 4M^2/s}$ ($0.274$ from the non-relativistic formula $v_c = (\pi/(GM^3))^{2/3}$); 96 % of the annihilation rate
at freeze-out comes from collisions above the crossing and 75 % of the pairs of the non-relativistic Maxwell distribution are faster, so I12 alone
is not a perturbative relic mechanism; (b) at the bound itself each species
leaves $\Omega h^2 = 0.0582$, so even a maximal $^3P_0$ channel would give the relic only at the unitarity limit; (c) version 3 adds the s-wave
portal I13 (item 2.10), with which each species leaves $\Omega h^2 = 0.060$ (both together the measured $0.120$). Print the stored values:

```text
python3 - <<'EOF'
import json
t = json.load(open('outputs/thermal.json'))
print('unitarity', {k: t['unitarity'][k] for k in ('Omega_h2_per_species_unitarity_limited', 'fraction_of_pairs_above_vc_at_xf',
                                                   'fraction_of_rate_above_crossing_at_xf', 'v_crossing', 'v_crossing_exact',
                                                   'sqrt_s_crossing_GeV', 'x_f_unitarity_limited', 'sigma_v_bound_at_xf_cm3_s',
                                                   'sigma_v_bound_nonrel_at_xf_cm3_s')})
print('I12 benchmark', {k: t['I12_universal_benchmark'][k] for k in ('Lambda_eff_TeV', 'Lambda_star_over_c13_TeV',
                                                                     'Omega_h2_per_species_I12_alone', 'sqrt_s_unitarity_crossing_GeV')})
print('validation', t['validation_s_wave'])
EOF
python3 -c "import json; [print(c['name'], c['passed'], c['detail'][:160]) for c in json.load(open('reports/thermal-checks.json'))['checks']]"
grep -n "unitarity" MODEL.md SOLUTION.md ANALYSIS.md PROVENANCE.md FIELD_EQUATIONS.md | head -40
```

Check: (a) the Boltzmann solver reproduces the standard s-wave result (about $\Omega h^2 = 0.127$ for $\langle\sigma v\rangle = 4.4\times10^{-26}$
cm$^3$/s, check T3); (b) the documents state that I12 alone violates the $^3P_0$ bound at the relic strength, that the unitarity-limited relic is
$0.0582$ per species, and that the relic of version 3 comes from I13 with the I12 benchmark $\pi/(2M^3) = (38.2\ \text{TeV})^{-3}$, which stays
below the bound up to $\sqrt s = 2.40M$ (a fraction $5.2\times10^{-4}$ of the rate at $x = 30$ comes from above it); (c) no document calls the
version-2 relic viable; (d) the unitarity-limited relic compares $\langle\sigma v\rangle$ and $\sqrt{\pi x}/M^2$ at the same $x = 30.77$ ($5.33$ and $5.84\times10^{-26}$
cm$^3$/s).

**Item 2.9: the built files.** Rebuild and inspect:

```text
python3 tools/build_docs.py
grep -c '\\\$' MODEL.tex PROVENANCE.tex FIELD_EQUATIONS.tex SOLUTION.tex ANALYSIS.tex
grep -n 'textbackslash' MODEL.tex PROVENANCE.tex FIELD_EQUATIONS.tex SOLUTION.tex ANALYSIS.tex
```

Check: every document reports `overfull boxes: 0`; there is no `\$` (an unparsed dollar sign) in the LaTeX files of the
five model documents (this document contains it once, in the text of this check);
`textbackslash` appears only inside `\texorpdfstring{...}{...}` (the plain-text PDF bookmarks of section titles).

**Item 2.10: the portal I13 (version 3).** The coupling is
$$ S_{I13} = \int d^8x\,\sqrt{|g|}\;\frac{c_A}{\Lambda_\star^6}\sum_{M \ne x_0}(i\bar\Psi\gamma^MP_b\Psi)\,J^B_M,\qquad P_b = \frac{1 - \gamma^{x_0}}{2},\qquad
   J^B_M = \frac13\sum_{i=1}^{3}\sum_{\psi\in\{Q_i,\,u_{Ri},\,d_{Ri}\}}i\bar\psi\gamma_M\psi, $$
with $\bar\Psi = \Psi^\dagger C$ and $P_a = (1 + \gamma^{x_0})/2$. Verify by hand: (a) $\gamma^{x_0}$ anticommutes with every $\gamma^M$
($M \ne x_0$), so $P_a\gamma^M = \gamma^MP_b$; with $C\gamma^{x_0}C^{-1} = -\gamma^{x_0}$ this gives $CP_bC^{-1} = P_a$, and for real matrices
$(iC\gamma^MP_b)^\dagger = iC\gamma^MP_b$ (the bilinear is Hermitian) for $M \ne x_0$; for $M = x_0$, $\gamma^{x_0}$ commutes with $P_b$ and
$(iC\gamma^{x_0}P_b)^\dagger = iC\gamma^{x_0}P_a$, which is why the sum leaves out $x_0$ (the review of version 3 found this; check `C8_I13_algebra`
verifies it with the author's matrices); (b) in the block form of the Kohn-Sham reduction $\gamma^{x_0} = \sigma_3$,
so $P_b$ keeps the lower component $b$ of an orbital $(a, b)$, and the fold bands $(a, 0)$ do not couple; (c) on the zero modes the coupling becomes
$\mathcal L_4 = G_A\,q_f\,\tilde I^{(b)}_{of}\,(i\bar\chi_o\gamma^\mu\chi_o)(i\bar f\gamma_\mu f)$ with $\tilde I^{(b)}_{of} = \int_{-L}^{0}b_o^2\varrho_fe^{-3Hy}dy$,
$G_A = c_AH/(2f^4v_t\Lambda_\star^6)$ and $q_f = 1/3$; (d) the s-wave cross-section into one Weyl component $f$ with $N_c$ colours,
$$ \sigma = \frac{N_cG_f^2\,s\,(1 + 2M^2/s)}{24\pi\beta},\qquad \beta = \sqrt{1 - 4M^2/s},\qquad \sigma v \to \frac{N_cG_f^2M^2}{2\pi}, $$
and its unitarity bound $\sigma \le 3\pi/(4p^2)$ ($^3S_1$, $J = 1$, averaged over the four spin states). Print the stored values:

```text
python3 - <<'EOF'
import json
c = json.load(open('outputs/coupled.json'))
i = c['I13']
for k in ('G_A_GeV-2', 'G_A_effective_operator_GeV-2', 'sum_Nc_q2_Ib2', 'x_f_capped', 'v_crossing_capped', 'v_crossing',
          'fraction_of_rate_saturated_capped', 'fraction_of_rate_above_crossing_at_xf', 'Omega_h2_per_species_capped',
          'sigma_v_I13_at_xf_cm3_s', 'sigma_v_I12_at_xf_cm3_s', 'sigma_n_xenon_cm2', 'LZ_cm2'):
    print(k, i[k])
print('I13 algebra', c['I13_algebra'])
for x in c['I13_checks']:
    print(x['zero_mode'], ' overlap', x['overlap_b'], ' finite difference', x['finite_difference'], ' fold-band shift', x['fold_band_shift'])
print('B - L alternative', c['I13_B_minus_L_alternative'])
EOF
```

Check: (a) the overlaps $\tilde I^{(b)}$ equal the finite-difference derivatives of the self-consistent Kohn-Sham level (to about $10^{-10}$) and the fold
band does not move (shifts of order $10^{-13}$); (b) the documents give $G_A = 1.278\times10^{-9}$ GeV$^{-2}$ with the cap at the unitarity limit
($1.269\times10^{-9}$ without it), $\sum_fN_c(q_f\tilde I^{(b)}_f)^2 = 16.35$, $x_f = 31.2$, the crossing velocity $0.51$ (22 % of the freeze-out rate at the
bound; uncapped, 25 % above $v = 0.52$) and the direct-detection cross-section $4.0\times10^{-46}$ cm$^2$ (0.16 of the LZ limit at 44.3 TeV); (c) the reason
for the baryon-number current: with $B - L$ the right-handed neutrinos would be thermalised (kinetic decoupling at $M/T = 24.4$ with the elastic
cross-section $G^2E^2/(2\pi)$) and add $\Delta N_{eff} = 0.144$ ($N_{eff} = 3.19$); with $J^B$ their production through I11 is $2.0\times10^{-17}$ of the I13 rate.

**Item 2.11: the thermal history and the freeze-in of the fold bands.** The fold bands of dirac16complex couple only through I11 (vector,
$B - L$ charges $q_Q = q_{u_R} = q_{d_R} = 1/3$, $q_L = q_{e_R} = q_{\nu_R} = -1$), which produces them from the plasma (freeze-in) with the rate
density, for Maxwell-Boltzmann statistics,
$$ \gamma = \frac{4}{\pi^5}\,N_\chi\,G_V^2\,T^8\sum_fN_c\big(q_f\tilde I_f\big)^2, $$
each produced pair carrying the mean energy $8T$; with the benchmark $G_V = 4.38\times10^{-17}$ GeV$^{-2}$ and the highest temperature
$T_{max} = 10$ TeV this gives $\Delta N_{eff} = 0.001$ ($\Gamma/H = 0.012$ at $T_{max}$: never in equilibrium). Verify by hand the two Bessel moments
$\int_0^\infty x^6K_1(x)\,dx = 384$ and $\int_0^\infty x^7K_2(x)\,dx = 3072$ used in the rate and the mean energy, and that the energy injected into a
species that never thermalises scales as $\Delta N_{eff} \propto G_V^2T_{max}^3$. Print the stored values:

```text
python3 -c "import json; f = json.load(open('outputs/coupled.json'))['freeze_in']; print({k: f[k] for k in f if k != 'components'})"
python3 -c "import json; t = json.load(open('outputs/thermal.json')); print(t['g_star_table']); print('today', t['today'])"
```

The self-interaction $-\frac{\lambda}{2}(\bar\Psi\Psi)^2$ adds a second channel (check C10): the dark matter annihilates into fold pairs through the
transition scalar density $s_{DF} = a_Db_F + b_Da_F$, with $G_\lambda = \lambda H\tilde I_\lambda/(2f^4v_t)$, $\tilde I_\lambda = \int_{-L}^0s_{DF}^2e^{-3Hy}dy$ and the estimate
$\sigma v = G_\lambda^2M^2/(2\pi)$ per fold species; verify that the energy put into the fold bands while the dark matter is in equilibrium,
$d(\rho_{fold}a^4)/dx_4 = 2M\gamma_\lambda a^4$ with $\gamma_\lambda = \sum_{A,B}n_{\chi,eq}^2\sigma vN_F$, scales as $G_\lambda^2$. Print it:

```text
python3 -c "import json; print(json.load(open('outputs/coupled.json'))['self_interaction_channel'])"
```

Check: (a) the table of $\Delta N_{eff}$ against $T_{max}$ scales as $T_{max}^3$; (b) $g_\rho$ and $g_s$ equal 105.75 above the electroweak scale (three
generations, massive $W^\pm$, $Z$, no Higgs particle, no right-handed neutrinos, no fold bands; the dark matter is not counted), 10.75 at a few MeV
and $g_s = 43/11$ today; (c) the documents state that $T_{max}$, the benchmark strength and the bound $G_\lambda \le 2.3\times10^{-15}$ GeV$^{-2}$ are ASSUMED,
and that the Kohn-Sham value $\lambda_B$ with $v_t = H^{-3}$ would thermalise the fold bands ($\Delta N_{eff} = 0.19$).

**Item 2.12: the coupled Kohn-Sham solution in ten environments and the metric as a power series.** With the Standard-Model mean fields
(the thermal and vacuum gauge condensates, from the trace anomaly
$\langle\tfrac{\alpha_s}{\pi}G^2\rangle_T = \langle\tfrac{\alpha_s}{\pi}G^2\rangle_0 - \tfrac{8}{b}(\rho - 3p)$, $\langle\tfrac{\alpha_s}{\pi}G^2\rangle_0 = 0.012$ GeV$^4$ ($\alpha_s$ at $2\pi T$),
$\langle F^2\rangle_T = -2(\rho - 3p)$ for the free $W$ and $Z$ fields of a plasma and the order-$\alpha$ interaction part $\langle F_{geo}^2\rangle = 4g^2p_2$,
$p_2 = -(g^2T^4/144)d_A[C_A + \frac52T_FN_f]$ (Feynman-Hellmann; for QCD it reproduces the trace-anomaly value: verify this by hand with $d_A = 8$,
$C_A = 3$, $T_F = \frac12$)) and the fermion densities of each environment, the dark-matter level of the self-consistent Kohn-Sham solution moves by
$\delta\varepsilon/M \le 1.5\times10^{-6}$ (largest at freeze-out, $T = 1.42$ TeV) and by at most $10^{-16}$ from nucleosynthesis on; with the full adiabatic
response $\delta k = (c_\rho\kappa\delta\rho + c_3\kappa\delta p_3 + c_p\kappa\delta\bar p)/H^2$ ($c_3 = -3c_\rho$: radiation drops out) and the hidden pressure
$\bar p = \frac14\partial p/\partial\ln f$ of every species, the hot plasma included, the block moves by at most $\delta\ln f = 1.1\times10^{-34}$, and the gain of the
loop mass $\to$ source $\to$ block $\to$ mass is at most $1.1\times10^{-33}$. The metric is a series of terms of decreasing magnitude: the
background (1), the Newtonian potentials of bound objects (from $0.17$ at the surface of a neutron star down to the Earth) and the
cosmological potential ($\Delta_\Phi = 2.4\times10^{-5}$ on the largest scales, falling with $k$), the second order ($5.8\times10^{-10}$), the radion ($1.1\times10^{-34}$) and the Kaluza-Klein gravitons with the Yukawa range
$1.63\times10^{-21}$ m. The even graviton tower has the profiles $u_n = e^{-a\xi}(\cos n\pi\xi + (a/n\pi)\sin n\pi\xi)$ ($a = 3\eta/2$, $\xi = y/L$) with
the eigenvalues $\Lambda_n = 9\eta^2/4 + (n\pi)^2$ and the norms $N_n = (1 + a^2/q^2)/2$, $q = n\pi$; verify by hand that $u_n$ satisfies
$(e^{3\eta\xi}u')' = -\Lambda_ne^{3\eta\xi}u$ with $u'(0) = u'(-1) = 0$. Print the stored values:

```text
python3 - <<'EOF'
import json
c = json.load(open('outputs/coupled.json'))
for k, v in c['environments'].items():
    print('%-45s d_eps/M = %.3g  delta ln f = %.3g  loop gain = %.3g' % (k, v['d_eps_DM_over_M'], v['delta_ln_f'], v['loop_gain']))
print('proton', c['proton_sensitivity'])
print('block response', c['block_response_coefficients'], ' Feynman-Hellmann QCD', c['feynman_hellmann_qcd_rel_dev'])
s = json.load(open('outputs/series.json'))
for t in s['ordering']:
    print('%.3g  %s' % (t['magnitude'], t['term']))
for g in s['kaluza_klein_gravitons'][:4]:
    print('n =', g['n'], ' Lambda =', g['Lambda_n'], ' FEM', g['Lambda_n_fem'], ' alpha(fold) =', g['alpha_fold_point'], ' range (m)', g['range_m'])
EOF
```

Check: every number of the sections on the coupled solution and on the metric series of MODEL, FIELD_EQUATIONS and SOLUTION equals the printed
value (rounded); the magnitudes decrease from term to term; the documents label the tensor-mode bound and $\sigma_8$ of Planck 2018 as values quoted
from memory.

**What to report back.** For each item: OK, or the file, the line, what is wrong and the proposed correction.

# The findings of the review of version 1 and their incorporation

The review agent reported four errors and ten minor items for the documents of version 1 at commit `9285bb6`:

1. **The familiar uncertainty bound.** The documents said that $\langle p^2\rangle \ge 1/(4\Delta\xi^2)$ "holds only" for profiles
   negligible at the tip; states with a large tip density can satisfy it too (first even Kaluza-Klein mode: $\varrho(\text{tip}) = 0.655$,
   $\langle p^2\rangle\Delta\xi^2 = 4.59$). Correct wording: the bound is guaranteed only for such profiles.
2. **The symbol list of PROVENANCE** said that $\rho_0$ is the electroweak parameter (PROVENANCE uses $\rho$) and named the lattice
   vector $\vec n$, which PROVENANCE does not use, while $n$ is used there as a level index and as the basis size of the
   Richardson formula.
3. **Primes.** Lists stating that primes denote $d/d\xi$ overlooked $G'(k_*)$ and $U'(S)$ (ANALYSIS) and the reduced actions,
   whose $u'$ is $du/dy$ (FIELD_EQUATIONS and MODEL).
4. **The electroweak fit.** With the angle of the couplings set equal to the on-shell angle of the measured masses,
   $\cos^2\theta_W = m_W^2/m_Z^2$, a fit of $\rho - 1$ to the measured $\rho_0 - 1 = 0.00038$ makes the model's $m_Z = 91.1706$ GeV, 17 MeV
   below the measured $91.1879 \pm 0.0020$ GeV; the documents did not say so. ($\rho_0$ measures the custodial violation beyond
   the Standard-Model loops; in a tree-level model it is the tree-level $\rho$ with the angle of the couplings.)

Minor items: the probability density was defined twice in ANALYSIS (unnormalised in one section); the largest TT
deviation of a thermalised-fold-band variant lies at the edge $\ell = 2500$ of the range; the cosmic-variance fraction refers to
TT only; gaps in the lists of symbols; $\mathrm{Vol}_7$ not defined in PROVENANCE; the verification statements credited an older
commit; "true lower bound" wording for $m \ge m_H$, which is observed for the computed states, not derived; the sign convention of
$w_a$; old notation in the report texts of two checks; "every state" meaning every tabulated state.

All four errors and the minor items were incorporated on 2026-10-18. For error 4 the computation was changed, not only the
text: the angle of the couplings is now fixed by the measured masses and $\rho_0$, $\cos^2\theta_W = (m_W^2/m_Z^2)/\rho_0 = 0.776368$, so
that the model reproduces both $m_W$ and $m_Z$; every scale in GeV moved by $+8.5\times10^{-4}$ ($m_{KK} = 121.32$ TeV, $H = 14.296$ TeV)
and the dependent computations were rerun.

# The findings of the review of version 2 and their incorporation

The review agent (2026-10-18, 1858 s, 82 tool calls) read the five model documents of version 2, compared every computed
number with the outputs (all agree except three roundings) and recomputed key results independently (the mixing matrices,
the long-baseline and reactor probabilities, the resonances, the solar survival, the onset temperatures, the CNB, the $Z$
widths, the freeze-out, $\Delta N_{eff}$, the fast-flavour growth rates, the typed background equations against the stored symbolic
forms). It reported eight errors (A1 to A8), minor items (B) and gaps in the self-containment (C):

* **A1 (the most important).** The documents compared the freeze-out requirement of the gauge-kinetic portal,
  $\langle\sigma v\rangle = 2.01\times10^{-25}$ cm$^3$/s per species, with $(4\pi/M^2)\sqrt{x_f/\pi} = 2.32\times10^{-25}$ cm$^3$/s and called it 87 % of a unitarity
  estimate. The operator annihilates only from $^3P_0$; with the spin average the bound is $\sigma \le \pi/(4p^2)$ and
  $\langle\sigma v\rangle \le \sqrt{\pi x_f}/M^2 = 5.79\times10^{-26}$ cm$^3$/s, which the requirement exceeds 3.47 times. Incorporated: the computation
  (`um2_analysis.py`, check B3) now computes the bound, its numerical thermal average, the velocity $v_c = 0.263$ above which the
  effective cross-section exceeds it and the fraction (79 %) of pairs above $v_c$; all five documents state that the relic
  abundance of the dark matter is OPEN in version 2 (an additional annihilation channel or a non-thermal origin is needed), and
  the verdict on dark matter reads "a candidate without a relic mechanism".
* **A2.** "No tip operator reaches $\Psi_B$" holds only for chiral $P_+$ tip currents and for operators built on $\bar\Psi\Psi$; corrected.
* **A3.** The fast-flavour dispersion relation mixed lower- and upper-index shifts and did not state its metric; it is now written
  with $\Lambda^0$, $\Lambda^3$ and $\eta^{\mu\nu} = \mathrm{diag}(1, -1)$ on $(x_4, x_3)$ in every document (the growth rates were confirmed).
* **A4.** $c_Z = c'_Z = 0$ was labelled DERIVED or "required"; the invisible width bounds the even part and $N_{eff}$ disfavours, but does not
  exclude, the oriented part, so it is now ASSUMED everywhere.
* **A5.** The flavour, decoupling and fast-flavour equations wrote $t$ for the time $x_4$ and $z$ for the axis $x_3$; corrected
  throughout.
* **A6 to A8.** Roundings: the adiabatic solar $P_{ee}$ at 15 MeV is $0.306$ (the value $0.304$ is the numerical one); the $\tau$ singlet
  bulk mass is $-9.205H$; the Kohn-Sham Richardson errors are below $2.2\times10^{-9}$ relative.
* **B.** $J_{max}$ computed ($0.0335$) against NuFIT's value ($0.0333 \pm 0.0007$) now distinguished; the conventions of the supernova
  resonances stated (two-flavour conditions); the tip matrices equal the mixing matrices only with $\kappa_e = \kappa_u = 1$; the measured
  values enter as fit targets, direct inputs or comparisons; the single-species requirement $(17.6\ \text{TeV})^{-3}$ is a
  version-2 number; the sum rules are absolute ($1.0\times10^{-8}$; relative $7.8\times10^{-4}$ and $6.0\times10^{-4}$ for $W^\pm$ and $Z$); the
  50-digit roots are compared with the stored masses ($4.5\times10^{-11}$); the temperature of the neutrino spectrum in the
  cosmology; the difference $0.0044$ to $0.0053$ from the precision $N_{eff}$; the labels ESTIMATE and STANDARD; notational clashes
  ($H$ as the Hubble rate, $M_{Pl}$, $\Lambda_0$, $G(u)$, $\mu_N$, the portal amplitude $e$, $\alpha$, $F$ and $F_h$, the field names
  of PROVENANCE) added to the symbol lists; the dark-matter mass written $44.35$ TeV everywhere.
* **C.** Equations or inputs used but not written in the same document (among them the relic and $\Delta N_{eff}$ formulas, the
  Einstein-Boltzmann equations, the BAO $\chi^2$ and data, the nonlinear background equations, the fermion equations with their
  boundary conditions, the decoupling equations, the CNB, Landau-Zener, adiabatic solar, condensate and pairing formulas, the
  Kohn-Sham equations behind the quoted equations of state, the direct-detection inputs) are now written out in every
  document that uses them.

All items were incorporated on 2026-10-18; after the change of the analysis computation its 23 checks pass, and the
total remains 205.

# The findings of the review of version 3 and their incorporation

The review agent (2026-10-18, 2055 s, 74 tool calls) read the five model documents of version 3 at commit `726997f`, compared every
version-3 number with the outputs (all agree except the items below; the check counts 7, 14, 4, 8 and 16 and the total 233 were
right) and recomputed key results independently (the I13 algebra, the cross-sections and unitarity bounds, the thermal formulas, the
QCD condensates, the proton sensitivity, the Kaluza-Klein tower, the Majorana alternative, the $\nu_R$ alternative, the overlaps, $G_A$, the
direct detection, the potentials and the degrees of freedom). It reported eight errors (A1 to A8), minor items (B) and gaps (C):

* **A1.** The I13 bilinear $i\bar\Psi\gamma^MP_b\Psi$ is not Hermitian for $M = x_0$, $(iC\gamma^{x_0}P_b)^\dagger = iC\gamma^{x_0}P_a$, while the action summed over all
  eight directions. Incorporated: the sum runs over $M = x_1, \dots, x_7$ in every document, and the new check `C8_I13_algebra` verifies the
  algebra with the author's matrices (the $B$ structure included: $C\gamma^MP_b$ anticommutes with $B$ for the extra times, whose currents vanish on
  the zero modes). No number changed.
* **A2.** The block response of the coupled solution left out the dominant sources (the hot plasma) and the $\delta\rho$, $\delta p_3$ terms of the
  adiabatic response. Incorporated in the computation: the full response and the hidden pressure $\bar p = \frac14\partial p/\partial\ln f$ of every species;
  $\delta\ln f \le 1.1\times10^{-34}$ (was $5.6\times10^{-45}$), the loop gain $1.1\times10^{-33}$, the radion term of the metric series accordingly; the conclusion
  (a negligible back-reaction) is unchanged.
* **A3.** Stale statements of version 2 ("$c_V = 0$", "no dark radiation", "no extra radiation"): corrected to the freeze-in fold bands with
  $\Delta N_{eff} = 0.001$.
* **A4.** "Relic OPEN" without qualification: now "OPEN in version 2 (I12 alone); resolved in version 3 by I13".
* **A5.** The labels "UM-2" and "version 3" were mixed in the cosmology results: UM-2 version 3 is the model with the freeze-in fold bands
  ($N_{eff} = 3.0442$, $\sigma_8 = 0.8118$, BAO $\chi^2 = 31.49$, $H_0 = 67.38$); the model without them is the neutrino content of version 2.
* **A6.** The amplitude of the kinetic-function shift is $1.7\times10^{-16}$ at the freeze-out (not below $10^{-50}$); now computed and stated per
  environment.
* **A7.** "I11 produces the $\nu_R$ at $10^{-14}$ of the I13 rate" had no source: now computed, $2.0\times10^{-17}$.
* **A8.** The thermal history did not state $\lambda$: the self-interaction contains the channel $\chi\bar\chi \to$ fold pairs. Incorporated: the new check
  C10 and the bound $G_\lambda \le 2.3\times10^{-15}$ GeV$^{-2}$ (ASSUMED); $\lambda_B$ is only the Kohn-Sham test value.
* **B.** The check counts of `um2_neutrino.py` (16) and `um2_cosmology.py` (8) in SOLUTION; the crossing of I12 quoted with the exact relative
  velocity $2\beta = 0.269$ beside the non-relativistic $0.274$, and the numbers of the freeze-out formula (3.47, 0.263, 79 %) kept apart from the
  Boltzmann numbers; the rate fractions recomputed by adaptive quadrature (an inaccurate integration had given a fraction above 1); the elastic
  $\nu_R$ rate with $G^2E^2/(2\pi)$ (kinetic decoupling 24.4 instead of 25.1); the electroweak condensates with the order-$\alpha$ interaction part
  (Feynman-Hellmann); the dark matter not counted in $g_\rho$, $g_s$; "perturbative" made precise (22 % of the rate at the bound; the contact form
  needs a mediator above 30 TeV); roundings (0.301 to 0.308; 104.95); the same $x$ in the comparison at the $^3P_0$ limit; the freeze-out
  environment at the version-3 $x_f = 31.23$ ($T = 1.42$ TeV); the signature convention of the trace anomaly and of the Proca Lagrangian; the
  $\overline{MS}$ angle in the running couplings; $\alpha_n$ for two profiles; the order-2 magnitude $5.8\times10^{-10}$; the $\nu_R$ couplings (I11 as
  well); a heading labelled DERIVED over estimates.
* **C.** The quark sensitivities, the scale $2\pi T$ of $\alpha_s$, the densities of the environments, the hadron list, $\Omega_m$, and the symbols $N_c$,
  $N_\chi$, $G_A^{B-L}$, $\sum_{A,B}$, $g_{s,e\gamma}$, $K_1$, $K_2$, the Mandelstam $s$, $\beta$, $J$, $a$, $M$, $\delta$ are now stated in every document that uses
  them; the variable $s/(4M^2) - 1$ is no longer called $z$.

All items were incorporated on 2026-10-18 (PROVENANCE item 24): the computations `um2_thermal.py`, `um2_coupled.py`, `um2_series.py`,
`um2_cosmology.py` and the `feedback` job of `um2_ks_jobs.py` were changed and rerun, and the total is now 235 checks (two new: `C8_I13_algebra`
and `C10_self_interaction_channel`), all passing.
