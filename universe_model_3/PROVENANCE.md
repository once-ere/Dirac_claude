---
title: "UM-3 provenance"
subtitle: 'Where every input of UM-3 comes from, every decision taken, every computation and its checks, the external data and software, and how to reproduce all of it'
author:
  - "Underlying theory: Patrick L. Nash"
  - "Recorded by Claude (Anthropic)"
  - "Provenance of UM-3, 2026-10-24"
  - "Repository once-ere/Dirac_claude, folder universe_model_3"
---

# How to read this document

This document records the origin of everything in the universe model UM-3: the author's inputs and orders, the decisions taken
while building the model, the computations that verify every derived statement (each a Python script that checks itself), the
external measurements and software that were used, and the commands that reproduce every result and every document. It is a
record of origins, decisions and computations, not of the model itself, and so it contains no equations.

The status labels used throughout UM-3: **AUTHOR** (from the author), **RECORD** (from the record of this repository),
**STANDARD** (textbook physics or a published measurement), **ASSUMED** (a choice without derivation), **INVENTED** (a new
interaction: the portals of dirac16complex), **DERIVED** (computed and verified), **ESTIMATE** (an order of magnitude),
**OPEN** (not settled).

# The author's inputs

| input | content and place |
| ---------------------- | ------------------------------------------------------------ |
| the order of 2026-10-24, 17:02 PDT | stop every earlier stage permanently; a new revision folder; read `4+4.nb` and verify its eight real $16 \times 16$ Dirac matrices; the new metric with $b_4^2$ ($b_4$ a function of the time $x_4$ in the extra-time components of the metric, never identically 1); the complete coupled field equations of the listed fields (Einstein-Lovelock gravity, the Higgs doublet with the ad hoc vacuum, three generations of lepton doublets, the right-handed electron, muon and tau, $W^1, W^2, W^3, B$, three generations of quark doublets, the gluons, dirac16complex coupled to gravity with a non-trivial spin connection and with its left- and right-handed halves coupled to every Standard-Model field, only the left-handed half to the Higgs field); new phenomenological interactions; an accurate approximate Kohn-Sham solution; the CMB, the CNB and the BAO with the metric as a power series; the $x_0$ mass mechanism; dark matter and dark energy; every equation and every symbol in every document, never a reference to another file; Markdown, LaTeX and PDF; push as soon as verified. In the author's private prompt file (not committed). |
| the notebook 4+4.nb | the author's notebook "eight, real-valued, 16 by 16, Dirac Matrices" (Wolfram 15.0) with the matrices `T16^A[0..8]`; copied unchanged into the folder `author_inputs` of UM-3 (its sha256 is given below) |
| the notebook of the record | `Dirac_Einstein-Lovelock_4+4_Nash.nb` in the root of the repository: the coordinates $X = \{x_0, \dots, x_7\}$ (Section DEFCHART: $x_0$ the hidden direction, $x_1, x_2, x_3$ ordinary space, $x_4$ the time, $x_5, x_6, x_7$ the extra times) and the Lovelock weights $w = (1, 1/32, 1/1152)$ of the Einstein, Gauss-Bonnet and cubic terms with the cosmological-constant parameter $\Lambda_{\mathrm{N}} = 10$ of the notebook ($\Lambda = -10H^2$; In[134]) |
| the decision of 17:32 | "rather have three $\nu_{\mathrm{R}}$": three right-handed neutrinos, Dirac masses (in the conversation) |
| the reason of 17:34 | Gogilashvili and Tamborra, "Neutrino Flavor Conversion Shapes the Rate of Failed Core-collapse Supernovae", arXiv:2605.16504: why the flavour conversion of UM-3 must be correct (a third-party paper on the author's computer, read, not committed) |

The sha256 of the author's notebook `4+4.nb` as received and committed:

```text
7ec1709a0028bce0b443f116cf27b5d3e670de7aa195659a9c3274527270429d
```

The author's private files (his prompt files, his notes, the third-party paper, his scratch notebook of 2026-10-16 with its
`.mx` files and the files `Generalized_Kronecker_Delta.*`) are never committed; the repository's `.gitignore` excludes them.

# The decisions taken in UM-3

| decision | reason | status |
| ------ | ------ | ------ |
| the proper coordinate $\sigma$ of the hidden direction; the fold at $z = \pi/2$ ($z = 6Hx_0$, the angle on which the metric depends) | the author's metric has a kink in $\sigma$ there, which the junction conditions turn into a thin source | DERIVED |
| the Standard Model on the fold, dirac16complex in the bulk | species in the bulk have different limiting speeds and neutrino profiles would spoil flavour conversion | ASSUMED (motivated by the DERIVED limiting speeds) |
| right-handed quark singlets and Yukawa couplings | masses of the quarks and cancellation of the anomalies (defaults of the notification of 17:20; the author answered only on the neutrinos) | ASSUMED |
| three right-handed neutrinos | the author's decision of 17:32 | AUTHOR |
| the induced gravity of the fold | bulk gravitons move faster than light and have no time-kinetic term at the author's vacuum | ASSUMED |
| the fold fluid and the stabiliser | the kink at the fold and the static late-time bulk need sources | ASSUMED (values DERIVED) |
| the responding bulk medium (the radion mode) | a rigid medium would change the expansion law of the fold | ASSUMED |
| the portals of dirac16complex | the author's request for couplings of both halves to every Standard-Model field, only the left-handed half to the Higgs field | INVENTED |
| the pure-gauge $W^2$ of the ad hoc vacuum | the Gauss law of $SU(2)$ | DERIVED |
| no dependence of any field on the extra times | such fields are tachyonic | ASSUMED |
| the lightest neutrino mass zero, the Dirac phase zero | not fixed by the specification | ASSUMED |
| the primordial spectrum, the optical depth and the densities from Planck 2018 | the primordial era is not computed to this precision | ASSUMED |

# The computations

Every derived statement rests on one of these scripts in `universe_model_3/code/`. Each computes, checks itself and writes its
results to `universe_model_3/outputs/` and its checks to `universe_model_3/reports/`.

| script | what it computes | checks |
| ------ | ------ | ------ |
| `um3_gammas.py` | the author's Dirac matrices, rebuilt from `4+4.nb` (a library) | |
| `um3_dirac_matrices.py` | reality, Clifford relations, Spin(4,4) and Pin(4,4), chiral projectors, agreement with every stored output of the notebook | 55 |
| `um3_dirac_matrices_doc.py` | the document `dirac matrices` from the checked results | |
| `um3_lovelock.py` | the Lovelock tensors by the generalised Kronecker delta (a library) | |
| `um3_geometry.py` | the exact curvature and Einstein-Lovelock equations of the author's metric, the author's vacuum, the spin connection | 26 |
| `um3_fold.py` | the proper chart, the general warped metric, the junction potential and the fold sources, the conservation law at the fold | 13 |
| `um3_bulk.py` | the zero modes and the speeds of the bulk fields | 10 |
| `um3_fields.py` | the bilinears of dirac16complex, the Krein operator, the electroweak vacuum with the ad hoc component, the anomalies | 16 |
| `um3_spectra.py` | the bound states of dirac16complex with the exact matrices | 5 |
| `um3_neutrino.py` | the flavour blindness of the portals, the matter conversion, the crossing criterion, the equipartition, the cosmic neutrino background (CNB) | 5 |
| `um3_background.py` | the histories of the background, the energy conditions, the ad hoc vacuum as a gauge rotation | 6 |
| `um3_series.py` | the first-order terms of the power series of the metric, the radion condition | 6 |
| `um3_kohnsham.py` | the self-consistent Kohn-Sham states of dirac16complex in three regimes and at a weakly bound point | KS_NCHECKS |
| `um3_flavour.py` | the neutrino flavours in the Sun and in supernovae | 4 |
| `um3_thermal.py` | the degrees of freedom, the relic density, the portals and direct detection, the right-handed neutrinos | 6 |
| `um3_cosmology.py` | the cosmic microwave background (CMB), the CNB and the baryon acoustic oscillations (BAO) with the Boltzmann code CAMB and an independent background, against Planck 2018 and DESI DR2 (the second data release of the Dark Energy Spectroscopic Instrument) | 6 |

The documents are written in Markdown and built with `universe_model_3/tools/build_docs.py` (pandoc to LaTeX, pdflatex to PDF,
deterministic). `universe_model_3/docs_src/registry.py` holds the meaning, unit, value and status of every symbol;
`universe_model_3/tools/make_inventory.py` writes the inventory of the tagged equations from `FIELD_EQUATIONS.md`, and
`universe_model_3/tools/symbols_tool.py` copies every tagged equation into the other documents (`sync`), writes the symbol list
after every display (`expand`) and checks that every symbol of every display is defined and every tagged equation is written
identically in every document (`check`).

# External measurements and software

| source | used for |
| ------ | ------ |
| Planck Collaboration, Planck 2018 results VI, A&A 641, A6 (2020), Table 2 (TT,TE,EE+lowE+lensing) | the cosmological parameters and the derived quantities of the CMB |
| Planck 2018 plik-lite likelihood files (Planck Legacy Archive), via github.com/heatherprince/planck-lite-py | the CMB spectra (downloaded at run time into `universe_model_3/external/`, not redistributed) |
| DESI Collaboration, DESI DR2 Results II, arXiv:2503.14738, Table IV | the BAO distances; the 2.3 and 3.1 standard-deviation statements of its abstract |
| ACT Collaboration (Atacama Cosmology Telescope), DR6 constraints on extended cosmological models, arXiv:2503.14454 | $N_{\mathrm{eff}} = 2.86 \pm 0.13$ and $2.89 \pm 0.11$, $\sum m_\nu < 0.082$ eV |
| Borexino Collaboration, Nature 562, 505 (2018) | the survival probabilities of solar neutrinos |
| the global fit NuFIT 5.2 of the neutrino oscillation data (Esteban, Gonzalez-Garcia, Maltoni, Schwetz and Zhou, JHEP 09 (2020) 178; version 5.2 of November 2022 at www.nu-fit.org), normal ordering with the Super-Kamiokande atmospheric data | $\sin^2\theta_{12} = 0.303$, $\sin^2\theta_{13} = 0.02203$, $\sin^2\theta_{23} = 0.572$, $\Delta m^2_{21} = 7.41\times10^{-5}$ eV$^2$, $\Delta m^2_{31} = 2.511\times10^{-3}$ eV$^2$ |
| Particle Data Group, Review of Particle Physics (2022) | the masses of the Higgs boson (125.25 GeV), of the quarks and charged leptons and of the nucleon, the Fermi constant $1.1663788\times10^{-5}$ GeV$^{-2}$ and $v = 246.22$ GeV, the fine-structure constant |
| DESI Collaboration, DESI DR2 Results II, arXiv:2503.14738 | the bound $\sum m_\nu < 0.064$ eV (95%, DESI DR2 with the CMB, cosmological-constant model) |
| LUX-ZEPLIN (LZ) Collaboration, Phys. Rev. Lett. 135, 011802 (2025), arXiv:2410.17036 version 3 (4.2 tonne-years) | the limit $2.2\times10^{-48}$ cm$^2$ at 40 GeV (90% confidence) on spin-independent scattering |
| Long, Lunardini and Sabancilar, arXiv:1405.7654 | the capture rate of the CNB on tritium (4 and 8 per year per 100 g for Dirac and Majorana neutrinos) |
| Gogilashvili and Tamborra, arXiv:2605.16504 (version 3) | the flavour equipartition (the equal sharing of the three flavours that fast flavour conversion produces) and its effect on the explosions of massive stars |
| Bahcall's exponential solar density profile; Petcov's crossing probability; Keil, Raffelt and Janka's spectral shape; Izaguirre, Raffelt and Tamborra's dispersion relation; Morinaga's crossing theorem; Ma and Bertschinger's Boltzmann equations | the standard physics named in the documents |
| CAMB 2.0.5 (Lewis, Challinor and Lasenby) | the Boltzmann hierarchy and the CMB spectra |
| Python 3.13.17 with numpy 2.5.3, scipy 1.18.1, sympy 1.14.0, matplotlib 3.11.2; pandoc 3.1.3; pdfTeX (TeX Live 2023) | every computation and document |

# How to reproduce

From the root of a clone of the repository, with the software above installed:

```text
python universe_model_3/code/um3_dirac_matrices.py
python universe_model_3/code/um3_geometry.py
python universe_model_3/code/um3_fold.py
python universe_model_3/code/um3_bulk.py
python universe_model_3/code/um3_fields.py
python universe_model_3/code/um3_spectra.py
python universe_model_3/code/um3_neutrino.py
python universe_model_3/code/um3_background.py
python universe_model_3/code/um3_series.py
python universe_model_3/code/um3_flavour.py
python universe_model_3/code/um3_thermal.py
python universe_model_3/code/um3_cosmology.py
python universe_model_3/code/um3_kohnsham.py
python universe_model_3/docs_src/registry.py
python universe_model_3/tools/make_inventory.py
python universe_model_3/tools/symbols_tool.py check
python universe_model_3/tools/build_docs.py
```

Every script prints one line per check and ends with "n/n checks passed"; `um3_series.py` reads the output of `um3_fold.py`,
`um3_cosmology.py` downloads the Planck files once (about 7 MB), and `um3_kohnsham.py` runs for about an hour on two processor
cores. The documents are rebuilt identically (no dates in the LaTeX, fixed PDF metadata).
