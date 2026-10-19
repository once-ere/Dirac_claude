---
title: "UM-2 solution"
subtitle: "An accurate approximate solution of the coupled field equations: Einstein-Lovelock gravity, Kohn-Sham theory for the dirac16complex field coupled to gravity and to every Standard-Model field, three generations of quarks and leptons, the flavour conversion of the three neutrinos, and the CMB, CNB and BAO"
author:
  - "Underlying theory: Patrick L. Nash"
  - "Derived and verified by Claude (Anthropic)"
  - "Solution, version 4, 2026-10-18"
  - "Versions 3 and 2: 2026-10-18; version 1: 2026-10-17"
  - "Repository once-ere/Dirac_claude, folder universe_model_2"
---

# How to read this document

**What it contains.** This document presents the accurate approximate solution of the coupled field equations of the
universe model UM-2, in ten steps that follow the hierarchy of the problem: (1) the background and the primordial era;
(2) the masses from the $x_0$ dependence of the wave functions; (3) the Kohn-Sham states of dirac16complex coupled to all
fields and their back-reaction on gravity; (4) the electroweak sector; (5) the flavour conversion of the three neutrinos,
$N_{\mathrm{eff}}$ and the cosmic neutrino background (CNB); (6) the cosmic microwave background (CMB), the CNB and the
baryon acoustic oscillations (BAO); (7) the dark-matter relic and its detection; (8) the coupled solution in ten
environments; (9) the thermal history and the relic with the portal I13; (10) the terms of the metric power series. Before
the steps, "The coupled system" lists every field equation with its fields and the step that solves it, and "The
approximation scheme" states the small parameters. After the steps, "Accuracy of the solution" collects in one table, for
every equation, the method, the measured residual, the neglected terms and the checks in concert with the other field
equations; the last section states what the solution does not reproduce and what is open.

**How every step is presented.** Each step has five parts: (1) *the field equations*: every field equation (tag FE-$n$)
and every interaction term of the action (tag IN-$n$) that the step solves or uses, written out in full with its list of
symbols, also when an earlier step has already written it, so that every definition stands next to the equation that
uses it; (2) *the approximation*: the small parameter and the size of what is neglected, as equations with their symbol
lists; (3) *the solution*: formulas and numbers; (4) *the check*: the residual or the measured error of the solution in
its own equation, and its consistency with the other field equations that contain the same fields (in concert); (5) *the
status* of each result. The tags FE-$n$ and IN-$n$ are one numbering, shared by all documents of UM-2, of the 136 field
equations and the 18 interaction terms of the model.

**Symbols.** Every display equation is followed by the complete list of its symbols: every quantity, field, coupling,
constant, operator, index (with the values it takes) and special mark, with its meaning, its unit, its value where it has
one, and its status. Typography needs no definition (digits, $+$, $-$, $=$, brackets, fractions, roots, $\cdot$, $\dots$,
$\le$, $\approx$, $\sim$, $\times$, the standard functions sin, cos, tan, cot, sinh, cosh, tanh, exp, ln, log, det, min,
max, lim and the signs of sums, products and integrals; their index letters and integration variables are symbols and are
listed). A symbol has one meaning throughout the document, in the displays, in the inline formulas and in the text.
Euler's number is written $\mathrm{e}$, the imaginary unit $\mathrm{i}$ and the differential $\mathrm{d}$.

**Status labels.** Every result carries one of these labels:

* **AUTHOR**: taken from the author's notebooks (the coordinates, the metric, the Lovelock weights, the gamma matrices,
  the mass parameter);
* **RECORD**: taken from the Revision record of this repository (the dirac16complex Lagrangian, the Kohn-Sham reference
  states);
* **STANDARD**: textbook physics or a measured value used as an input;
* **ASSUMED**: a choice made for this model;
* **INVENTED**: a new phenomenological ingredient of this model (the tip sigma field, the portals I11, I12, I13);
* **DERIVED**: computed and verified in this work (symbolically or numerically); the verification is stated with the
  result;
* **ESTIMATE**: an order-of-magnitude evaluation, not a precision computation;
* **OPEN**: not resolved in this version.

**Units and conventions.** $\hbar = c = 1$. In the numerical work on the block the author's constant is $H = 1$ and the mass
of dirac16complex is $m_\Psi = H$, unless a physical unit is given; the physical scale is $H = 14.296$ TeV (step 2). The
coordinates are the author's $X = \{x_0, x_1, \dots, x_7\}$: $x_0$ the hidden space-like direction, listed first, periodic
with the period $\pi/(6H)$; $x_1, x_2, x_3$ ordinary space; $x_4$ the time; $x_5, x_6, x_7$ the three extra time-like
directions. $W^+$ carries the electric charge $+e$ and $W^-$ the charge $-e$; UM-2 contains no Higgs particle.

**The numbers.** Every number is taken from the outputs of the computations of UM-2 (the scripts in
`universe_model_2/code/`, which write `universe_model_2/outputs/` and `universe_model_2/reports/`; the residuals of this
version are computed by `universe_model_2/code/um2_residuals.py`) and is quoted with the precision of the output. These
files are named for reproduction only: everything the reader needs (every equation, every definition and every argument)
is written in this document.

**Versions.** Version 1 (2026-10-17) had one generation. Version 2 (2026-10-18) has three generations of quarks and
leptons and three neutrino flavours with their mixing (step 5), and removes the chiral tip $Z$ portal of version 1 (step 4).
Version 3 (2026-10-18), by the author's order to find and document an accurate approximate solution of the coupled field
equations, added the coupled solution in environments (step 8), the thermal history and the relic with the portal I13 (step
9), the terms of the metric power series (step 10), the Majorana alternative (step 5) and the matter power spectrum (step 6);
after its independent review the I13 sum leaves out the direction $x_0$, the coupled solution uses the full adiabatic block
response with the hot plasma and the order-$\alpha$ electroweak condensates, and step 9 has the self-interaction channel of
the dark matter. **Version 4** (2026-10-18), by the author's order of 2026-10-18, 15:42, reorganises the presentation: every
field equation is written out with its symbols wherever it is used, every step states its approximation, its solution and
its check in concert with the other field equations, every symbol has one meaning (several letters of version 3 had more
than one), and the residuals of the solution in its equations are computed anew (the check of every step and the table
"Accuracy of the solution"). The physics and the claims of version 3 are unchanged; every number is taken from the
computations as refined for version 4 (precision fixes changed a few values in their last digits, and each change is stated
where the value appears), and the residual computation adds 52 checks to the 235 of version 3 (287 in all).
