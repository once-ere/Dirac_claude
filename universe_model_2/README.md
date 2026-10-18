# universe_model_2 — UM-2, a 4+4 model of the Universe

UM-2 is a model of the Universe built on Patrick L. Nash's 4+4-dimensional theory: Einstein-Lovelock gravity with the
author's weights $w = (1, 1/32, 1/1152)$ and $\Lambda = -10H^2$, the dirac16complex quantised spinor field coupled to
gravity through the canonical spin connection, and one generation of the Standard Model without a Higgs particle —
photons, gluons, $W^+$ (charge $+e$), $W^-$ (charge $-e$), $Z$, $\nu$, $e$, $u$, $d$. Every mass comes from the dependence
of the wave functions on the hidden space coordinate $x_0$ (period $\pi/(6H)$). Coordinates are the author's
$\{x_0, x_1, \dots, x_7\}$: $x_0$ the hidden space direction, $x_1, x_2, x_3$ space, $x_4$ the time, $x_5, x_6, x_7$ the extra times.

## Documents (each as `.md`, `.tex` and `.pdf`, each self-contained)

| document | content |
| --- | --- |
| `MODEL` | the model: fields, metric power series, action, every interaction in equation form, the $x_0$ mass mechanism, gravity, the dark sector, parameters, assumptions and conflicts |
| `PROVENANCE` | where every ingredient, equation and number comes from; the computations and their 180 checks; corrections; reproduction |
| `FIELD_EQUATIONS` | the coupled field equations: energy-momentum tensors, matter equations with every interaction, boundary conditions, the exact background equations, the $x_0$ reductions, the Kohn-Sham equations, the linear perturbations |
| `SOLUTION` | the approximate solution: static block and primordial deflation, all masses, Kohn-Sham states of dirac16complex coupled to gravity and to the Standard Model, electroweak sector, $N_{eff}$ and CNB, CMB and BAO, dark-matter relic |
| `ANALYSIS` | the $x_0$ mass mechanism and the uncertainty relation, the deflating extra times, dirac16complex as dark matter and as dark energy |

## Principal results

* With a block stabiliser (assumed) the author's weights and $\Lambda$ give a stable block $k_* = 12 + \frac43\sqrt{51}$ with attractive
  four-dimensional gravity, $G(k_*) = \frac{20}{3} + \sqrt{51}$; the extra times deflate into it in a primordial era and then stay frozen;
  the radion has $m_r = 3.387H = 48.4$ TeV.
* Graviton, photon, gluons and the dirac16complex fold bands are exactly massless; $W^\pm$, $Z$, $e$, $\nu$, $u$, $d$ get their masses
  from the tip of the $x_0$ cell; $m_{KK} = 121$ TeV, $H = 14.3$ TeV.
* Dark matter: the lightest odd quantum of the $\Psi_B$ half of dirac16complex, $44.3$ TeV, cold, neutral, stable (conditional);
  dark energy is not supported by dirac16complex.
* $N_{eff} = 3.044$; CNB of $\nu_e$ and two massless $\Psi_A$ species; CMB TT and EE spectra within $2.2\times10^{-4}$ and
  $3.7\times10^{-4}$ of Planck $\Lambda$CDM ($30 \le \ell \le 2500$); DESI DR2 BAO $\chi^2 = 30.3$ for 13 points.
* Conflicts inherent in the specified content: no Higgs boson, $W^+W^-$ unitarity near 1.2 TeV, one-generation $Z$ width.

## Computations

| script | checks | time (s) |
| --- | --- | --- |
| `code/um2_algebra.py` | 31/31 | 48 |
| `code/um2_geometry.py` | 25/25 | 68 |
| `code/um2_background.py` | 22/22 | 123 |
| `code/um2_fields.py` | 15/15 | 51 |
| `code/um2_spectra.py` | 13/13 | 25 |
| `code/um2_ks_jobs.py validate, spectrum, ground8, ground592, darkmatter, portals, feedback` | 2/2, 3/3, 3/3, 4/4, 3/3, 5/5, 2/2 | 38, 1, 125, 124, 15, 4, 0.4 |
| `code/um2_electroweak.py` | 19/19 | 1 |
| `code/um2_primordial.py` | 5/5 | 247 |
| `code/um2_cosmology.py` | 5/5 | 9 |
| `code/um2_analysis.py` | 23/23 | 4 |
| `tools/build_docs.py` (all five PDFs) | | 11 |

Times are those of the verification run from a fresh clone of the repository (2026-10-17, commit `b3c3c1a`): every
stored number was reproduced to $10^{-9}$ relative or better, and the five PDFs and their LaTeX sources were rebuilt
byte-identical. Every script writes its numbers to `outputs/` and its named checks to `reports/`, exits with code 0 only if every check
passes, and finishes within 423 s.

## Reproduce

Requirements: Python 3 with sympy, numpy, scipy, mpmath, matplotlib and camb (`pip install sympy numpy scipy mpmath
matplotlib camb`); for the documents, pandoc and TeX Live with the `lmodern` package. From the repository root:

```text
python universe_model_2/code/um2_algebra.py
python universe_model_2/code/um2_geometry.py
python universe_model_2/code/um2_background.py
python universe_model_2/code/um2_fields.py
python universe_model_2/code/um2_spectra.py
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
the notebook `WaveFunctionUniverse-4+4-Einstein-Lovelock.nb` and its `.mx` files) are not part of the repository.
