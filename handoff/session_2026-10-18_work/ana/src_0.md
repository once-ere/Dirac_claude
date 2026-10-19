---
title: "UM-2 analysis"
subtitle: "The $x_0$ mass mechanism, and the validity of associating dark matter and dark energy with the dirac16complex field"
author:
  - "Underlying theory: Patrick L. Nash"
  - "Derived and verified by Claude (Anthropic)"
  - "Analysis, version 4, 2026-10-18 (versions 1 to 3: 2026-10-17 and 2026-10-18)"
  - "Repository once-ere/Dirac_claude, folder universe_model_2"
---

# How to read this document {-}

**What it contains.** On 2026-10-18 the author ordered two analyses of the universe model UM-2: "analyze the $x_0$ mass
mechanism, and ... analyze the validity of associating dark matter (and dark energy) with dirac16complex". This document
carries out both. Part A analyses the mechanism by which every non-massless particle receives its mass from the dependence
of its wave function on the hidden space coordinate $x_0$, periodic with the period $\pi/(6H)$, with the uncertainty relation
as its physical reason; it states the author's argument as equations, shows what it gives quantitatively and where it
fails, writes out the exact $x_0$ eigenvalue equations of every field, and explains the hierarchy of the masses, the
mixing matrices and the massless zero modes. Part B analyses dirac16complex as dark matter (the candidate, the portals
that produce it, its relic density from the Boltzmann equation, its detection, the bound on its self-interaction and the
cosmological tests) and as dark energy (why this association is not supported). The last two sections collect the
conditions, the open problems, the conflicts with data and the closing assessment.

**Version 4.** Version 4 (2026-10-18) re-presents version 3. The physics and the numbers are those of version 3, taken
from the current outputs of the computations of the repository (after the precision fixes of the commit of 2026-10-18 that
added the residual analysis of the solution: 287 checks in all), with the results of that residual analysis where they
concern this document. What is new is the presentation, ordered by the author: every equation that is used is written out
here, every field equation and interaction term with the tag of the inventory of the field equations of UM-2, (FE-$n$) or
(IN-$n$), and every display equation is followed by the list of all of its symbols with their meanings, units, values and
status. A symbol has one meaning throughout (the notation of version 4: for example $\tilde m^2$ is the dimensionless boson
eigenvalue, $\tilde\varepsilon$ the dimensionless fermion eigenvalue, $K = 1/f^2$ the block variable, $\mathcal{H}$ the
Hubble rate and $H$ always the author's constant). The reader never needs another document: every equation, definition
and argument used is in this one. The repository files that hold the computations are named only for reproduction.
Besides the re-presentation, two elementary consequences of version-3 results are made explicit (the lower bound that the
uncertainty relation sets on a localised state, never below 11.05 TeV, and the asymptotic sensitivity of a zero-mode mass to its
localisation), the trace anomaly of the direct-detection estimate is written in the geometric normalisation of the gluon field
(the number is unchanged), and the accuracy statements of the residual analysis are added.

**Status labels.** AUTHOR (the author's notebooks and orders), RECORD (the Revision record of this repository), STANDARD
(textbook physics or a measured value), ASSUMED (a choice made in UM-2), INVENTED (a new interaction or structure of UM-2),
DERIVED (computed and verified in UM-2; the verification is stated), ESTIMATE (an order-of-magnitude evaluation), OPEN (not
solved). A measured bound that is quoted from memory, not re-read from its source, is marked FROM MEMORY, as in version 3.

**Units and conventions.** Natural units $\hbar = c = 1$ (the reduced Planck constant $\hbar$ is shown where the author's
relations contain it). The coordinates are the author's $X = \{x_0, x_1, \dots, x_7\}$, the hidden direction first: $x_0$
the hidden space-like direction, $x_1, x_2, x_3$ ordinary space, $x_4$ the time, $x_5, x_6, x_7$ the three extra times. $W^+$
carries the electric charge $+e$ and $W^-$ the charge $-e$. UM-2 contains no Higgs particle: the tip sigma field gives the
$W^\pm$ and $Z$ masses. A derivative with respect to $\xi$ is always written $\mathrm{d}/\mathrm{d}\xi$, a dot is
$\mathrm{d}/\mathrm{d}x_4$, and $\Delta$ is a change, a difference or (in an uncertainty relation) the root-mean-square
spread of the quantity that follows.

**Where the numbers come from.** The scripts in the folder `code` of `universe_model_2` write the outputs in the folder
`outputs`, with named checks in the folder `reports`: `analysis.json` (the uncertainty analysis, the sensitivities, the
condensate), `masses.json`, `flavour.json` and `series.json` (the $x_0$ spectra and the Kaluza-Klein tower), `thermal.json` and
`coupled.json` (the thermal history, the relic, the portals, the coupled solution), `neutrino.json` and `cosmology.json` (the
neutrinos, $N_{\mathrm{eff}}$, the CMB) and `residuals.json` (the residuals of the solution in every field equation and in
concert).

**Summary of the verdicts.**

| question | verdict |
| ------------ | ------------------------------------------------------------ |
| Can every mass come from the $x_0$ dependence of wave functions periodic with period $\pi/(6H)$? | YES (DERIVED): every four-dimensional mass of UM-2 ($W^\pm$, $Z$, the twelve fermions of three generations, the dark matter, the Kaluza-Klein modes) is an eigenvalue of an $x_0$ operator; the graviton, the photon, the gluons and the fold bands of dirac16complex are exactly massless |
| Is the uncertainty relation the reason for the masses? | ONLY FOR THE HEAVY STATES: the uncertainty estimate $m_{\mathrm{Heis}}$ lies below the masses of the computed Kaluza-Klein and odd excitations and of the dark matter (by factors 2.3 to 7.5), but the light masses ($W^\pm$, $Z$ and all twelve fermions) lie $3.2\times10^{-3}$ (top quark) to $1.1\times10^{-17}$ (lightest neutrino) below it and come from the tip of the $x_0$ cell |
| Why must the light fermions be zero modes? | The hidden kinetic energy of any profile that is negligible at the tip is at least that of a mass $m_{\mathrm{Heis}} \ge 1/(2fL) = 11$ TeV (DERIVED); a mass of 173 GeV or less needs an exact cancellation of it by the other terms of the $x_0$ operator, which happens only for the zero modes of that operator; their mass is then the small mixing of two chiral zero modes at the tip |
| Are the neutrino masses and their mixing $x_0$ effects? | YES for the masses, NO for the mixing angles: the three neutrino masses are $x_0$ eigenvalues (the most block-sensitive of all eigenvalues), the PMNS matrix is the tip matrix $\mathcal{K}_\nu$, an input; given both, the flavour conversion follows |
| Do the extra times deflate to irrelevance? | IN THE PRIMORDIAL ERA, then FROZEN: they deflate by up to a factor 2.9 into the stabilised block; a continuing deflation is excluded because every mass and coupling depends on the block size |
| Is dirac16complex dark matter? | YES, CONDITIONALLY: the lightest odd quanta of its two halves $\Psi_A$ and $\Psi_B$ (two degenerate Dirac fermions of 44.35 TeV) are cold, neutral and stable (DERIVED, conditional); the gauge-kinetic portal I12 alone cannot produce their relic abundance within perturbative unitarity, but with the s-wave portal I13 (INVENTED) they freeze out with $\Omega_{\mathrm{DM}}h_{100}^2 = 0.060$ each (physics accuracy of the needed coupling about 1 %), and their scattering on xenon is 0.16 of the present LZ limit (testable); the massless fold bands are radiation ($\Delta N_{\mathrm{eff}} = 0.001$ by freeze-in), not dark matter |
| Is dirac16complex dark energy? | NOT SUPPORTED: no positive-energy state has a negative equation of state; a negative-coupling condensate runs away; the dark energy of UM-2 is a tuned four-dimensional cosmological term |
| Does the $x_0$ mechanism fix the nucleon mass? | INDIRECTLY: the nucleon mass is QCD binding energy, proportional to $\Lambda_{\mathrm{QCD}}$, which is set by the gauge coupling at the Kaluza-Klein scale, itself an $x_0$ quantity; $\mathrm{d}\ln m_{\mathrm{p}}/\mathrm{d}\ln f = -46.1$ makes it the most block-sensitive mass of UM-2 |
