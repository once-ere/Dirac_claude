---
title: "UM-2 manual tasks"
subtitle: "How to carry out by hand the two long tasks of the UM-2 work: the fresh-clone verification of every computation and document, and the independent review of the documents against the computed outputs"
author:
  - "Underlying theory: Patrick L. Nash"
  - "Written by Claude (Anthropic)"
  - "Manual tasks, version 2, 2026-10-18 (version 1: 2026-10-18)"
  - "Repository once-ere/Dirac_claude, folder universe_model_2"
---

# How to read this document

Two tasks of the UM-2 work are long when they are run as single jobs:

* **Task 1, the fresh-clone verification**: all 19 computations of version 2 and the document build took 1027 s
  (about 17 minutes) on 2026-10-18 at commit `4a6421d`, although every individual computation takes at most about
  4.5 minutes (the primordial integration, 268 s).
* **Task 2, the independent review**: a review agent that read the five model documents of version 2, compared their
  statements with the computed outputs and recomputed key numbers independently ran for 31 minutes (1858 s, 82 tool calls).

When this document was first written the author's rule was that no individual calculation may take longer than
12 minutes and 3 seconds (later 7 minutes and 3 seconds); the author lifted the limit on 2026-10-18. The steps below are
still kept short, so that each can be executed by hand and its result reported back for incorporation into the project.
This document is self-contained: every command, every equation and every reference value it needs is written here.
Wherever a value can change when the computations are updated, the command that prints it from the repository is given
instead of the value.

Version 2 (2026-10-18) covers UM-2 version 2: three generations of quarks and leptons, three neutrino flavours with their
mixing and flavour conversion, and the dark matter of both halves of dirac16complex. It adds review items for these
(items 2.6 to 2.8) and records the findings of the review of version 2 and their incorporation.

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
before it; the expected durations are those of the run of 2026-10-18 at commit `4a6421d`).

| block | commands | expected time | checks |
| ---- | -------------------------------------------------- | ------------ | -------- |
| 1 | `run code/um2_algebra.py` | 54 s | 31 |
| 2 | `run code/um2_geometry.py` | 77 s | 25 |
| 3 | `run code/um2_background.py` | 133 s | 22 |
| 4 | `run code/um2_fields.py` | 54 s | 16 |
| 5 | `run code/um2_spectra.py` | 28 s | 14 |
| 6 | `run code/um2_flavour.py` and `run code/um2_neutrino.py` | 5 s, 31 s | 7, 15 |
| 7 | `run code/um2_ks_jobs.py validate` and `run code/um2_ks_jobs.py spectrum` | 37 s, 1 s | 2, 3 |
| 8 | `run code/um2_ks_jobs.py ground8` | 137 s | 3 |
| 9 | `run code/um2_ks_jobs.py ground592` | 137 s | 4 |
| 10 | `run code/um2_ks_jobs.py darkmatter`, `run code/um2_ks_jobs.py portals`, `run code/um2_ks_jobs.py feedback` | 16 s, 4 s, 0.5 s | 3, 5, 2 |
| 11 | `run code/um2_electroweak.py` | 1 s | 19 |
| 12 | `run code/um2_primordial.py` | 268 s | 5 |
| 13 | `run code/um2_cosmology.py` and `run code/um2_analysis.py` | 23 s, 4 s | 6, 23 |
| 14 | `run tools/build_docs.py` | 17 s | |

The check counts add up to 205; the counts in force are printed by step 1.4. For example, block 1:

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

Expected result: `result: REPRODUCED`. In the run of 2026-10-18 at commit `4a6421d` only the run times and one Kohn-Sham
integral (a relative difference of $1.1\times10^{-12}$, caused by threaded linear algebra that does not sum in a fixed order)
differed; the LaTeX sources, the PDF documents and the figures were byte-identical. With other software versions, files
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

**Item 2.8: the dark-matter relic and unitarity.** The operator $G\,\bar\chi\chi F_{\mu\nu}F^{\mu\nu}$ annihilates a Dirac pair in the p-wave,
$\sigma v = G^2s(s - 4M^2)/(4\pi) \to G^2M^4v^2/\pi$, and only from the state $^3P_0$ ($J = 0$); partial-wave unitarity averaged over the four
spin states then bounds $\sigma \le \pi/(4p^2)$, $p = Mv/2$, i.e. $\sigma v \le \pi/(M^2v)$, whose thermal average over $f(v) \propto v^2e^{-xv^2/4}$ is
$$ \Big\langle\frac{\pi}{M^2v}\Big\rangle = \frac{\sqrt{\pi x}}{M^2} . $$
Verify the average by hand (the integrals $\int_0^\infty v\,e^{-xv^2/4}dv = 2/x$ and $\int_0^\infty v^2e^{-xv^2/4}dv = 2\sqrt\pi\,x^{-3/2}$, with
$1\ \text{GeV}^{-2} = 1.1673\times10^{-17}$ cm$^3$/s for $\sigma v$), and print the stored values:

```text
python3 -c "import json; print(json.load(open('outputs/analysis.json'))['relic'])"
python3 -c "import json; [print(c['detail']) for c in json.load(open('reports/analysis-checks.json'))['checks'] if c['name'].startswith('B3')]"
grep -n "unitarity" MODEL.md SOLUTION.md ANALYSIS.md PROVENANCE.md
```

Check: the documents state that the freeze-out requirement (about $2.0\times10^{-25}$ cm$^3$/s per species) exceeds the bound
(about $5.8\times10^{-26}$ cm$^3$/s at $x_f = 30.4$, $M = 44.35$ TeV) about 3.5 times, so that the relic abundance is OPEN in version 2,
and that no document calls the candidate "viable" without this condition.

**Item 2.9: the built files.** Rebuild and inspect:

```text
python3 tools/build_docs.py
grep -c '\\\$' MODEL.tex PROVENANCE.tex FIELD_EQUATIONS.tex SOLUTION.tex ANALYSIS.tex
grep -n 'textbackslash' MODEL.tex PROVENANCE.tex FIELD_EQUATIONS.tex SOLUTION.tex ANALYSIS.tex
```

Check: every document reports `overfull boxes: 0`; there is no `\$` (an unparsed dollar sign) in the LaTeX files of the
five model documents (this document contains it once, in the text of this check);
`textbackslash` appears only inside `\texorpdfstring{...}{...}` (the plain-text PDF bookmarks of section titles).

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
