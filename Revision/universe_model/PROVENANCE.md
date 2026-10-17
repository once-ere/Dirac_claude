# UM-1 provenance: where every ingredient of the universe model comes from

Version 1.3 of 2026-10-17, for `MODEL.md` (the model), `FIELD_EQUATIONS.md` (its field equations), `SOLUTION.md` (an
approximate solution), `ANALYSIS.md` (the analysis of the mass mechanism and of the dark associations, section 7) and
`GAPS.md` (the gaps closed in version 1.3, section 8). Repository `https://github.com/once-ere/Dirac_claude`, folder `Revision/universe_model/`;
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
| the mass mechanism: four-dimensional masses as eigenvalues of the $x_0$ operators on the periodic cell; the uncertainty bound holds for the $x_0$ excitations and fails for the protected zero modes (1.2) | the AUTHOR's idea, made precise here; analysed in `ANALYSIS.md` | sections 4.4, 9 |
| the portal operators P1 to P5 | INVENTED | section 4.5 |
| the requirement of slow deflation after the primordial era | DERIVED requirement (mass constancy) | section 4.4, `SOLUTION.md` |
| (1.1) the cubic Lovelock weight $w_3 = 1/768$ and $\Lambda = -24H^2 + \delta\Lambda$ | CHANGED (forced by the solution: the author's weights give repulsive gravity in the only static vacuum) | section 4.1, `SOLUTION.md` section 3 |
| (1.1) the block stabiliser | ASSUMED (its origin OPEN) | section 4.1 |
| (1.1) the fold-reflection parity that keeps the odd-parity $\Psi$ dark matter stable | ASSUMED ((1.2) exact to $2\times10^{-27}$, `ANALYSIS.md` 8.3) | section 8, `SOLUTION.md` section 5 |
| (1.2) the end of the primordial deflation before nucleosynthesis; portal coefficients that differ between the $\Psi$ fold band and the $\Psi$ dark matter (or the one-half count) | DERIVED requirements (`ANALYSIS.md` sections 7 and 8.5) | section 8 |

## 5. Computations and tools

* Symbolic: Python 3.14.5, sympy 1.14.0 (`field_equations/derive_field_equations.py`).
* Numerical: numpy 2.4.6, no scipy; matplotlib 3.11.0 for the figures (`solution/`). The Kohn-Sham solution uses the
  record's reference solver `Revision/kohn_sham/reference/ks_fd.py` and its coefficients (`run_reference.py`)
  UNCHANGED (TAKEN), with the portal potentials added by a wrapper (`solution/ks_coupled.py`).
* Documents: the Markdown files are the sources; `tools/md2tex.py` converts each to LaTeX and `tools/build_pdfs.py`
  compiles it with pdflatex (MiKTeX 26.5), so the .md and the .pdf say the same thing.
* The analysis (1.2): `analysis/x0_mass_analysis.py` (sympy, numpy, matplotlib; about 30 s) and
  `analysis/dark_validity.py` (numpy, matplotlib; about 3 s), which also writes the tables of `ANALYSIS.md` section 12.
* Every calculation runs well within the limit of 423 s per calculation of this project.

## 6. Status

| deliverable | file | status |
| --- | --- | --- |
| the model | `MODEL.md`, `MODEL.pdf` | version 1.3 |
| this provenance | `PROVENANCE.md`, `PROVENANCE.pdf` | version 1.3 |
| the coupled field equations | `FIELD_EQUATIONS.md`, `.pdf`; `field_equations/` | version 1.1 (13/13) |
| an approximate solution | `SOLUTION.md`, `.pdf`; `solution/` | version 1.2 (checks in `solution/reports/solution-checks.json`) |
| the analysis of the $x_0$ mass mechanism and of the dark associations | `ANALYSIS.md`, `.pdf`; `analysis/` | version 1 (21/21 and 13/13 checks) |
| the gaps closed in version 1.3 | `GAPS.md`, `.pdf`; `analysis/gap_fixes.py` | version 1 (4/4 checks) |

## 7. Provenance of the analysis (`ANALYSIS.md`, version 1.2 of this provenance)

The author's request of 2026-10-17 (quoted): "in your documentations and provenances i want you to analyze the x0 mass
mechanism, and to analyze the validity of associating dark matter(and dark energy) with dirac16complex". The analysis
was done by Claude Opus 5.5 in this repository; its scripts are `analysis/x0_mass_analysis.py` and
`analysis/dark_validity.py`.

| ingredient | origin | label |
| --- | --- | --- |
| the $x_0$ operator, the measure, the fold conditions, the flat form, the factorisation $A^\dagger A$, the exact spectrum without cutoff, the spin-1/2 boundary identity, the tip-parameter scaling | derived here from the corrected metric (version 2) and the actions of `MODEL.md` (sympy) | DERIVED (checks A1) |
| the spectra, the gap theorem, the mass decompositions, the Heisenberg comparison, the sensitivities $d\ln m/d\ln f$ | computed here (two finite-element discretisations, numpy) | DERIVED (checks A2) |
| $W$, $Z$ tip parameters, fermion $c_f$, $m_{KK}$, $H$, $fL$ | `solution/outputs/masses.json` | TAKEN (from the solution) |
| the $\Psi$ levels, $g_F$, the dark-matter quanta ($w$, $p_0/\rho$, $p_t$, energies) | `solution/outputs/ks/spectrum.json`, `ks/dm_lam0.json`, `ks/dm_lam1.json` | TAKEN (from the solution) |
| $H_0$, $\delta\Lambda/H^2$, $h_4/A$, $M_{DM}$; $g_{*s}$ at the $\Psi$ decoupling and $\Delta N_{eff}$ | `solution/outputs/late_time.json`, `cosmology.json` | TAKEN (from the solution) |
| the effective equation of state on the history, the condensate law, the record's verdict on the gas | `Revision/dark_sector/dirac16complex/README.md` | TAKEN (from the record) |
| the vector-contact annihilation cross-section $G^2M^2/\pi$ | an explicit Dirac trace in `dark_validity.py` | DERIVED (check B2) |
| freeze-out ($x_f$ equation, $\Omega h^2 = 1.07\times10^9x_f/(\sqrt{g_*}M_{Pl}\langle\sigma v\rangle)$), the partial-wave unitarity limit, the neutrino-like decoupling estimate | Kolb and Turner; textbook unitarity; neutrino decoupling at about 1 MeV | STANDARD, FROM MEMORY |
| the LZ spin-independent limit, $2.2\times10^{-48}$ cm$^2$ at 40 GeV (4.2 tonne-years) | LZ collaboration, PRL 135, 011802 (2025), arXiv:2410.17036; the value read from the search results on 2026-10-17; the extrapolation to 50.9 TeV (linear in the mass) is ours | experimental, ESTIMATE for the extrapolation |
| atomic-clock limits $\dot\alpha/\alpha = (1.0\pm1.1)\times10^{-18}$/yr, $\dot\mu/\mu = (-8\pm36)\times10^{-18}$/yr | Lange et al., PRL 126, 011102 (2021) | FROM MEMORY |
| $G_F$, $m_N$, $\alpha_s(m_Z) = 0.1180$, the cluster bound $\sigma/M \lesssim 1$ cm$^2$/g, the Tremaine-Gunn bound | PDG and the literature | FROM MEMORY |

Every FROM MEMORY number is used only for orders of magnitude and for comparisons; none enters a DERIVED result. The
corrections that the analysis made to the other documents are listed in `ANALYSIS.md` section 10.

## 8. Provenance of the gap fixes (`GAPS.md`, UM-1 version 1.3)

The author's instruction of 2026-10-17 (quoted): "Then go ahead, fix the gaps and push". The fixes were made by Claude
Opus 5.5 in this repository; the script is `analysis/gap_fixes.py`.

| ingredient | origin | label |
| --- | --- | --- |
| the tip resolved as an $x_0$ layer (Dirichlet at its outer edge, stiffness $\beta e^{-3\eta}\delta$) and its equivalence to the Robin condition | derived and computed here (finite elements) | DERIVED equivalence; the layer's inner structure INVENTED |
| the self-adjoint mixing condition of the tip Yukawa coupling and the exact fermion eigenvalues | derived and computed here (transfer matrices, mpmath 50 digits) | DERIVED |
| the vector portal P1 restricted to the lepton multiplets $L$, $e_R$ | a choice of this model (gauge invariant multiplet by multiplet) | CHANGED, INVENTED |
| the overlap ratio, the relic requirement, the vector-contact cross-section, the decoupling estimate | `analysis/outputs/dark_validity.json` (`ANALYSIS.md`) | TAKEN (from the analysis) |
| the electron-loop (photon-mixing) coupling to protons, $b_p = (\alpha/3\pi)\,G\ln(\Lambda^2/m_e^2)$ | Kopp, Niro, Schwetz and Zupan 2009 (leptophilic dark matter) | STANDARD, FROM MEMORY |
| the CMB bound on energy injection, $p_{ann} < 3.2\times10^{-28}$ cm$^3$/s/GeV, and $f_{eff} \approx 0.6$ for $e^+e^-$ | Planck 2018 results VI; Slatyer 2016 | FROM MEMORY |
| the width of the QCD crossover used for the band of $\Omega h^2$ (120 to 180 MeV) | lattice QCD (pseudo-critical temperature about 155 MeV) | FROM MEMORY, ESTIMATE |
