# UM-1 provenance: where every ingredient of the universe model comes from

Version 1.1 of 2026-10-17, for `MODEL.md` (the model), `FIELD_EQUATIONS.md` (its field equations) and `SOLUTION.md` (an
approximate solution). Repository `https://github.com/once-ere/Dirac_claude`, folder `Revision/universe_model/`;
the model was started on top of commit `13f9fb9`.

## 1. The order

The author's order of 2026-10-17 (summarised; the quoted words are the author's): create "a new model of the
Universe" that includes Einstein-Lovelock gravity and "the dirac16complex quantized spinor field (which is
hypothesied to represent dark matter)", coupled to gravity "using a non-trivial canonical spin connection", with "new
CRITICAL interactions" of these fields with photons, neutrinos, electrons, up and down quarks and the $W$ and $Z$
bosons, "do NOT include the Higgs particle"; able to model the CMB, the CNB and BAO, so that the metric must be "very
general, but perhaps expressible as a power series of terms of decreasing magnitude"; new phenomenological
interactions "consistent with qcd and electro-weak models"; and, CRITICALLY, mass is to be given to all non-massless
particles (all except the graviton, the photon "and perhaps the quanta of the dirac16complex field") "by appropriate
wave function dependence on the space coordinate x0 (either explicit, derived, or assumed), which must be periodic in
x0 with period $\pi/(6H)$", with the uncertainty relation $\Delta x_0\,\Delta p_{x_0} \geq \hbar/2$ as the reason.
Then: push the model with provenance (.md and .pdf), compute the coupled field equations, compute an accurate
approximate solution, document each (.md and .pdf), and complete the open stages.

The mass-from-$x_0$ idea and the periodicity requirement are the AUTHOR's. The assembly of the model, the choices
labelled ASSUMED and INVENTED in `MODEL.md`, the derivations and the numerics are by Claude Opus 5.5 working in this
repository.

## 2. Ingredients taken from the Revision record (TAKEN)

| ingredient | source in this repository | status there |
| --- | --- | --- |
| the author's coordinates $x_0, \dots, x_7$ and the corrected primordial metric (version 2) | `Revision/SPEC.md` section 1; `Revision/metric_warped/`; `Revision/docs/METRIC_SELF_CONSISTENCY.md` | sympy 14/14, Wolfram 13/13 |
| the Einstein-Lovelock equations with a general diagonal source, the author's weights $w = (1, 1/32, 1/1152)$, $\Lambda = -10H^2$ | `Revision/field_equations_a4/a4-equations.json` (keys generalSource, einstein) | Wolfram 57/57, sympy 69/69 |
| the Lovelock tensors of the corrected metric | `Revision/gkd_lovelock/results/lovelock-tensors.json` | W4 |
| the dirac16complex Lagrangian and the $\gamma$ matrices of $Cl(4,4)$ in the author's order | `Revision/SPEC.md` section 3; `Revision/algebra/gammas.json` | exact |
| the canonical spin connection, $\gamma^M\Omega_M = \frac32 He^{a_4}b_4^{-1/2}\gamma^{x_0} + (u - \frac12\dot a_4)\gamma^{x_4}$ | `Revision/lead_checks/emt_divergence_and_spin_connection.py` | 10/10 |
| the reduction to $2\times2$ blocks, $h_j = j[-(i/f)\sigma_1\partial_y + M\sigma_2 + \kappa k\sigma_3] + v$, the fold and tip conditions, the exact $k = 0$ spectra | `Revision/kohn_sham/ks-theory.json` | Wolfram 51/51, sympy 61/61 |
| the fold-band quanta $\varepsilon = e^{-a_4}|k|$ (massless), the bulk band $\varepsilon \geq m$ | `Revision/kohn_sham/results/`, `Revision/kohn_sham/tip_convergence/` | 45/45, 7/7 |
| the condensate law $S = S_0e^{a_4}b_4^{-2}$ | `Revision/field_equations_a4/a4-equations.json` (fields) | exact |
| theorem T3 (the map $\chi \to \sigma_2\chi$, $M \to -M$, $\theta \to \pi - \theta$) | `Revision/pairing/kohn_sham/t3-theory.json` | exact |
| the dark-sector findings for the corrected metric (free gas $w_{eff} = 1/3$, condensate $w_{eff} = \frac59 w_c$, bulk band) | drafts of phase W6, `handoff/drafts_2026-10-17/w6/` | drafts (37/37, 13/13, 10/10), not yet the record |

The Kohn-Sham cross-check of the record was NOT complete when this model was started: `HANDOFF.md` 0.10, "W5 STATE
AT THE STOP OF 2026-10-17". Nothing of the model depends on the three failing comparisons, which concern numbers at
the $10^{-10}$ level.

## 3. Standard physics used as input (STANDARD)

| input | value used | source |
| --- | --- | --- |
| electron mass | $m_e = 0.51099895$ MeV | Particle Data Group (from memory of the PDG tables; to be checked against the current edition) |
| up, down quark masses ($\overline{MS}$, 2 GeV) | $m_u = 2.16$ MeV, $m_d = 4.70$ MeV | PDG (as above) |
| $W$ and $Z$ masses | $m_W = 80.3692$ GeV, $m_Z = 91.1880$ GeV | PDG 2024 (as above) |
| the electroweak $\rho$ parameter | $\rho_0 = 1.00038 \pm 0.00020$ | PDG electroweak review (as above); the target of the $m_{KK}$ fit of `SOLUTION.md` |
| the neutrino mass of the one generation | $m_\nu = 0.05$ eV | chosen at $\sqrt{|\Delta m^2_{31}|}$ (ASSUMED) |
| electroweak scale, fine-structure constant | $v = 246.22$ GeV, $\alpha^{-1} = 137.036$ | PDG (as above) |
| neutrino mass splittings | $\Delta m^2_{21} = 7.5\times10^{-5}$ eV$^2$, $|\Delta m^2_{31}| = 2.5\times10^{-3}$ eV$^2$ | PDG (as above) |
| CMB temperature | $T_0 = 2.7255$ K | Fixsen 2009 (as above) |
| cosmological parameters | $\Omega_bh^2 = 0.02237$, $\Omega_ch^2 = 0.1200$, $H_0 = 67.36$ km/s/Mpc, $N_{eff} = 3.044$, $z_* = 1089.92$, $z_{drag} = 1059.94$, $r_{drag} = 147.09$ Mpc, $100\,\theta_* = 1.04110$; with $N_{eff}$ free: $N_{eff} = 2.99 \pm 0.17$ | Planck 2018 results VI, Table 2 (as above); $\theta_*$ is the target of the $h$ fit, the rest COMPARISON |
| BAO | the 12 BAO-only consensus measurements of eBOSS DR16, $z = 0.15$ to $2.33$ | Alam et al. 2021 (PRD 103, 083533); the table of `https://www.sdss4.org/science/final-bao-and-rsd-measurements/`, read on 2026-10-17 |
| fitting formulae | $z_*$ (Hu and Sugiyama 1996), $z_{drag}$ (Eisenstein and Hu 1998), the first-peak shift $\phi_1$ (Hu, Fukugita, Zaldarriaga and Tegmark 2001), $N_{eff} = 3.044$ for three species (Bennett et al. 2021) | literature (from memory), calibrated on Planck $\Lambda$CDM in `solution/cosmology.py` |
| QCD: confinement of $u, d$ into $p, n$; nucleon masses | $m_p = 938.272$ MeV, $m_n = 939.565$ MeV | PDG (as above) |
| the electroweak chiral Lagrangian (Higgsless symmetry breaking) and boundary-condition symmetry breaking in extra dimensions | textbook and review literature on Higgsless models and on fermion localisation in extra dimensions | concepts only; no numbers |

All standard numbers are quoted from memory, except the eBOSS DR16 table (read from the SDSS page above); they are labelled as such in the outputs
and are used only as targets of fits and as comparisons, never as derived results.

## 4. Ingredients new in this model (ASSUMED or INVENTED in `MODEL.md`)

| ingredient | label | where |
| --- | --- | --- |
| the metric as a power series around the corrected primordial metric, with the bookkeeping parameter $\epsilon \sim 10^{-5}$ | ASSUMED | `MODEL.md` section 3 |
| the Standard-Model fields as eight-dimensional fields of $SU(3)_c \times SU(2)_L \times U(1)_Y$ on the cell, including the gluons | ASSUMED | section 4.3 |
| the chiral zero modes from the bulk masses $\mu_\psi$ and the fold conditions $\theta_\psi$ | INVENTED (built on the record's fold conditions) | section 4.3 |
| no Higgs field; the tip sigma field $\Sigma$ (non-linear, no radial mode) and its couplings $v_\Sigma$, $\lambda_f$ | INVENTED | section 4.3 |
| the mass mechanism: four-dimensional masses as eigenvalues of the $x_0$ operators on the periodic cell, with the uncertainty bound | the AUTHOR's idea, made precise here | section 4.4 |
| the portal operators P1 to P5 | INVENTED | section 4.5 |
| the requirement of slow deflation after the primordial era | DERIVED requirement (mass constancy) | section 4.4, `SOLUTION.md` |
| (1.1) the cubic Lovelock weight $w_3 = 1/768$ and $\Lambda = -24H^2 + \delta\Lambda$ | CHANGED (forced by the solution: the author's weights give repulsive gravity in the only static vacuum) | section 4.1, `SOLUTION.md` section 3 |
| (1.1) the block stabiliser | ASSUMED (its origin OPEN) | section 4.1 |
| (1.1) the fold-reflection parity that keeps the odd-parity $\Psi$ dark matter stable | ASSUMED | section 8, `SOLUTION.md` section 5 |

## 5. Computations and tools

* Symbolic: Python 3.14.5, sympy 1.14.0 (`field_equations/derive_field_equations.py`).
* Numerical: numpy 2.4.6, no scipy; matplotlib 3.11.0 for the figures (`solution/`). The Kohn-Sham solution uses the
  record's reference solver `Revision/kohn_sham/reference/ks_fd.py` and its coefficients (`run_reference.py`)
  UNCHANGED (TAKEN), with the portal potentials added by a wrapper (`solution/ks_coupled.py`).
* Documents: the Markdown files are the sources; `tools/md2tex.py` converts each to LaTeX and `tools/build_pdfs.sh`
  compiles it with pdflatex (MiKTeX 26.5), so the .md and the .pdf say the same thing.
* Every calculation runs well within the limit of 423 s per calculation of this project.

## 6. Status

| deliverable | file | status |
| --- | --- | --- |
| the model | `MODEL.md`, `MODEL.pdf` | version 1.1 |
| this provenance | `PROVENANCE.md`, `PROVENANCE.pdf` | version 1.1 |
| the coupled field equations | `FIELD_EQUATIONS.md`, `.pdf`; `field_equations/` | see that document |
| an approximate solution | `SOLUTION.md`, `.pdf`; `solution/` | version 1 (checks in `solution/reports/solution-checks.json`) |
