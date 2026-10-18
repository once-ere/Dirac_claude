# universe_model_2 — UM-2, a 4+4 model of the Universe

UM-2 is a model of the Universe built on Patrick L. Nash's 4+4-dimensional theory: Einstein-Lovelock gravity with the
author's weights $w = (1, 1/32, 1/1152)$ and $\Lambda = -10H^2$, the dirac16complex quantised spinor field coupled to
gravity through the canonical spin connection, and three generations of the Standard Model without a Higgs particle —
photons, gluons, $W^+$ (charge $+e$), $W^-$ (charge $-e$), $Z$, the three neutrino flavours $\nu_e$, $\nu_\mu$, $\nu_\tau$ with their
mixing and flavour conversion, $e$, $\mu$, $\tau$, and the quarks $u$, $d$, $c$, $s$, $t$, $b$. Every mass comes from the dependence of
the wave functions on the hidden space coordinate $x_0$ (period $\pi/(6H)$). Coordinates are the author's
$\{x_0, x_1, \dots, x_7\}$: $x_0$ the hidden space direction, $x_1, x_2, x_3$ space, $x_4$ the time, $x_5, x_6, x_7$ the extra times.

Version 2 (2026-10-18) replaced the single generation of version 1 by three generations, by the author's order to include
three neutrino flavours with mixing and flavour conversion (option A: three full generations, anomaly free generation by
generation), and removed the chiral tip $Z$ portal of version 1.

## Documents (each as `.md`, `.tex` and `.pdf`, each self-contained)

| document | content |
| --- | --- |
| `MODEL` | the model: fields of three generations, metric power series, action, every interaction in equation form, the $x_0$ mass mechanism with the tip matrices, neutrino flavour conversion, gravity, the dark sector, parameters, assumptions and conflicts |
| `PROVENANCE` | where every ingredient, equation and number comes from; the orders; the computations and their 205 checks; corrections; reproduction |
| `FIELD_EQUATIONS` | the coupled field equations: energy-momentum tensors, matter equations with every interaction, boundary conditions, the exact background equations, the $x_0$ reductions, the Kohn-Sham equations, the flavour evolution of the neutrinos, the linear perturbations |
| `SOLUTION` | the approximate solution: static block and primordial deflation, all masses and the mixing matrices, Kohn-Sham states of dirac16complex coupled to gravity and to the Standard Model, electroweak sector, the flavour conversion of the three neutrinos (vacuum, matter, accelerators, the Sun, $N_{eff}$, the CNB, supernovae), CMB and BAO, dark-matter relic |
| `ANALYSIS` | the $x_0$ mass mechanism and the uncertainty relation for twelve fermions, the neutrinos as $x_0$ observables, the deflating extra times, dirac16complex as dark matter and as dark energy |
| `MANUAL_TASKS` | how to carry out by hand, in steps of a few minutes each, the fresh-clone verification and the independent review of the documents; the findings of the reviews |

## Principal results

* With a block stabiliser (assumed) the author's weights and $\Lambda$ give a stable block $k_* = 12 + \frac43\sqrt{51}$ with attractive
  four-dimensional gravity, $G(k_*) = \frac{20}{3} + \sqrt{51}$; the extra times deflate into it in a primordial era and then stay frozen;
  the radion has $m_r = 3.387H = 48.4$ TeV.
* Graviton, photon, gluons and the dirac16complex fold bands are exactly massless; $W^\pm$, $Z$ and the twelve fermions get their
  masses from the tip of the $x_0$ cell (one doublet localisation per sector, $c_L = 5.95$, $c_Q = 3.38$; the singlet localisations
  span $|c_R| = 3.4$ to $35$); the PMNS and CKM matrices are the tip matrices; $m_{KK} = 121$ TeV, $H = 14.3$ TeV.
* Neutrinos (normal ordering, $m_1 = 1$ meV chosen): $m = 1.0$, $8.7$, $50.1$ meV, $\sum m_\nu = 0.060$ eV; MSW resonances, long-baseline
  appearance (DUNE $P(\nu_\mu\to\nu_e) = 0.070$, $\bar P = 0.020$), solar $P_{ee}$ from $0.54$ (pp) to $0.30$ ($^8$B), $N_{eff}$ computed
  $3.048$ (precision value $3.0432$ adopted), a CNB of three mass states at $1.945$ K, supernova resonances and the fast flavour instability.
* Dark matter: the lightest odd quanta of both halves of dirac16complex, two degenerate Dirac fermions of $44.35$ TeV, cold, neutral,
  stable (conditional); their relic abundance is OPEN, because the gauge-kinetic portal would need a cross-section 3.5 times above
  the $^3P_0$ unitarity bound. Dark energy is not supported by dirac16complex.
* CMB TT and EE spectra within $2.8\times10^{-4}$ of Planck $\Lambda$CDM ($30 \le \ell \le 2500$); DESI DR2 BAO $\chi^2 = 31.7$ for 13 points.
* Tree-level $Z$ widths of three generations: $2485$ MeV with the QCD factor against the measured $2495.5$ MeV.
* Conflicts inherent in the specified content: no Higgs boson, $W^+W^-$ unitarity near 1.2 TeV.

## Computations

| script | checks | time (s) |
| --- | --- | --- |
| `code/um2_algebra.py` | 31/31 | 54 |
| `code/um2_geometry.py` | 25/25 | 77 |
| `code/um2_background.py` | 22/22 | 133 |
| `code/um2_fields.py` | 16/16 | 54 |
| `code/um2_spectra.py` | 14/14 | 28 |
| `code/um2_flavour.py` | 7/7 | 5 |
| `code/um2_neutrino.py` | 15/15 | 31 |
| `code/um2_ks_jobs.py validate, spectrum, ground8, ground592, darkmatter, portals, feedback` | 2/2, 3/3, 3/3, 4/4, 3/3, 5/5, 2/2 | 37, 1, 137, 137, 16, 4, 0.5 |
| `code/um2_electroweak.py` | 19/19 | 1 |
| `code/um2_primordial.py` | 5/5 | 268 |
| `code/um2_cosmology.py` | 6/6 | 23 |
| `code/um2_analysis.py` | 23/23 | 4 |
| `tools/build_docs.py` (all six PDFs) | | 17 |

Times are those of the verification run from a fresh clone of the repository (2026-10-18, commit `4a6421d`, every
computation run as a separate step, 1027 s in all): all 205 checks passed, every stored number was reproduced (identical
except the run times and one Kohn-Sham integral, which differs by $1.1\times10^{-12}$ relative), and the six PDFs, their LaTeX
sources and the figures were rebuilt byte-identical. After that run the independent review of version 2 led to the
$^3P_0$ unitarity bound in `code/um2_analysis.py` (the same 23 checks, all passing) and to corrections of the documents. `tools/compare_outputs.py` performs this comparison; `MANUAL_TASKS`
describes the whole verification step by step. Every script writes its numbers to `outputs/` and its named checks to
`reports/`, and exits with code 0 only if every check passes.

## Reproduce

Requirements: Python 3 with sympy, numpy, scipy, mpmath, matplotlib and camb (`pip install sympy numpy scipy mpmath
matplotlib camb`); for the documents, pandoc and TeX Live with the `lmodern` package. From the repository root:

```text
python universe_model_2/code/um2_algebra.py
python universe_model_2/code/um2_geometry.py
python universe_model_2/code/um2_background.py
python universe_model_2/code/um2_fields.py
python universe_model_2/code/um2_spectra.py
python universe_model_2/code/um2_flavour.py
python universe_model_2/code/um2_neutrino.py
python universe_model_2/code/um2_ks_jobs.py validate
python universe_model_2/code/um2_ks_jobs.py spectrum
python universe_model_2/code/um2_ks_jobs.py ground8
python universe_model_2/code/um2_ks_jobs.py ground592
python universe_model_2/code/um2_ks_jobs.py darkmatter
python universe_model_2/code/um2_ks_jobs.py portals
python universe_model_2/code/um2_ks_jobs.py feedback
python universe_model_2/code/um2_electroweak.py
python universe_model_2/code/um2_primordial.py
python universe_model_2/code/um2_cosmology.py
python universe_model_2/code/um2_analysis.py
python universe_model_2/tools/build_docs.py
```

The private inputs of the author (prompt files, the private PDF, `dirac-main/`, `vendor/`, `Generalized_Kronecker_Delta.*`,
the notebook `WaveFunctionUniverse-4+4-Einstein-Lovelock.nb` and its `.mx` files) and the third-party paper "Neutrino Flavor
Conversion.pdf" are not part of the repository.
