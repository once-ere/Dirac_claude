# UM-1 provenance: where every ingredient of the universe model comes from

Version 1 of 2026-10-17, for `MODEL.md` (the model), `FIELD_EQUATIONS.md` (its field equations) and `SOLUTION.md` (an
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
| up, down quark masses ($\overline{MS}$, 2 GeV) | $m_u = 2.16$ MeV, $m_d = 4.67$ MeV | PDG (as above) |
| $W$ and $Z$ masses | $m_W = 80.37$ GeV, $m_Z = 91.1876$ GeV | PDG (as above) |
| electroweak scale, fine-structure constant | $v = 246.22$ GeV, $\alpha^{-1} = 137.036$ | PDG (as above) |
| neutrino mass splittings | $\Delta m^2_{21} = 7.5\times10^{-5}$ eV$^2$, $|\Delta m^2_{31}| = 2.5\times10^{-3}$ eV$^2$ | PDG (as above) |
| CMB temperature | $T_0 = 2.7255$ K | Fixsen 2009 (as above) |
| cosmological parameters | $\Omega_bh^2 = 0.02237$, $\Omega_ch^2 = 0.1200$, $H_0 = 67.36$ km/s/Mpc, $N_{eff} = 3.044$, $z_* = 1089.92$, $z_{drag} = 1059.94$, $r_{drag} = 147.09$ Mpc, $100\,\theta_* = 1.04110$ | Planck 2018 results VI, Table 2 (as above); used for COMPARISON only |
| QCD: confinement of $u, d$ into $p, n$; nucleon masses | $m_p = 938.272$ MeV, $m_n = 939.565$ MeV | PDG (as above) |
| the electroweak chiral Lagrangian (Higgsless symmetry breaking) and boundary-condition symmetry breaking in extra dimensions | textbook and review literature on Higgsless models and on fermion localisation in extra dimensions | concepts only; no numbers |

All standard numbers are quoted from memory (no network access was used); they are labelled as such in the outputs
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

## 5. Computations and tools

* Symbolic: Python 3.14.5, sympy 1.14.0 (`field_equations/derive_field_equations.py`).
* Numerical: numpy 2.4.6, no scipy (`solution/solve_model.py`).
* Documents: the Markdown files are the sources; `tools/md2tex.py` converts each to LaTeX and `tools/build_pdfs.sh`
  compiles it with pdflatex (MiKTeX 26.5), so the .md and the .pdf say the same thing.
* Every calculation runs well within the limit of 423 s per calculation of this project.

## 6. Status

| deliverable | file | status |
| --- | --- | --- |
| the model | `MODEL.md`, `MODEL.pdf` | version 1 |
| this provenance | `PROVENANCE.md`, `PROVENANCE.pdf` | version 1 |
| the coupled field equations | `FIELD_EQUATIONS.md`, `.pdf`; `field_equations/` | see that document |
| an approximate solution | `SOLUTION.md`, `.pdf`; `solution/` | see that document |
