---
title: "UM-2: a 4+4 model of the Universe"
subtitle: "Einstein-Lovelock gravity, the dirac16complex field, three generations of quarks and leptons with three neutrino flavours, their mixing and their flavour conversion, photons, gluons, and the $W^+$, $W^-$ and $Z$ bosons without a Higgs particle; every mass from the $x_0$ dependence of wave functions"
author:
  - "Underlying theory: Patrick L. Nash"
  - "Derived and verified by Claude (Anthropic)"
  - "Model definition, version 4, 2026-10-18"
  - "Versions 3 and 2: 2026-10-18; version 1: 2026-10-17"
  - "Repository once-ere/Dirac_claude, folder universe_model_2"
---

# How to read this document

This document DEFINES the model universe UM-2: its space and coordinates, its metric (a power series of terms of decreasing
magnitude), its fields exactly as the author lists them, every interaction among them, the mechanism that gives the particles
their masses through the hidden coordinate $x_0$, and what follows for gravity, for the dirac16complex field, for the three
neutrino flavours, for the dark sector and for the cosmology (CMB, CNB, BAO). It is self-contained: every equation it uses is
written here, and every symbol of every display equation is defined right below that equation. The computations that produced
its numbers are the scripts in `universe_model_2/code/` and their outputs in `universe_model_2/outputs/` (287 named checks, all
passing); they are named only so that the results can be reproduced.

**Status labels.** Every statement carries one of these labels:

* **AUTHOR**: taken from the author's notebooks (the coordinates, the metric, the Lovelock weights, the gamma matrices, the
  mass parameter of dirac16complex);
* **RECORD**: taken from the Revision record of this repository (a choice made there and kept, such as the regular tip and
  the self-interaction of dirac16complex);
* **STANDARD**: textbook physics or a measured value used as an input;
* **ASSUMED**: a choice made for this model;
* **INVENTED**: a new phenomenological ingredient of this model (an interaction that the Standard Model does not contain);
* **DERIVED**: computed and verified in this work (the verification is stated with the result);
* **ESTIMATE**: an order-of-magnitude evaluation, not a precision computation;
* **OPEN**: not resolved in this version.

**Every equation is followed by its symbols.** Every display equation is followed by the list of all of its symbols ("Symbols
in (FE-n)." or "Symbols in this equation."), each with its meaning, its unit, its value and its status where these apply. A
FIELD EQUATION carries the tag (FE-n) and a term of the ACTION (an interaction term) the tag (IN-n); the numbers are those of
the one inventory of UM-2 (FE-1 to FE-136, IN-1 to IN-18), shared by all documents of UM-2. Whenever a field equation or an
interaction term is used, it is written out again, with its tag and its complete symbol list, so that a reader never has to
search for a definition. One symbol has one meaning throughout (version 3 used several letters for several things; version 4
gives every meaning its own symbol).

**Units and conventions.** Natural units $\hbar = c = 1$ (the uncertainty argument keeps $\hbar$ visible). The coordinates are the
author's $X = \{x_0, x_1, \dots, x_7\}$, always with the hidden direction first: $x_0$ the hidden space-like direction, $x_1$,
$x_2$, $x_3$ ordinary space, $x_4$ the time, $x_5$, $x_6$, $x_7$ three extra time-like directions. Capital indices $M, N, P, Q$
run over $x_0, \dots, x_7$, frame indices $a, b, c, d$ over $0, \dots, 7$, Greek indices $\mu, \nu$ over the observable
coordinates $x_1, \dots, x_4$. A dot is $\mathrm{d}/\mathrm{d}x_4$. $W^+$ carries the electric charge $+e$ and $W^-$ the charge $-e$.
There is no Higgs particle.

**Versions.** Version 1 (2026-10-17) contained one Standard-Model generation. Version 2 (2026-10-18) contains three full
generations of quarks and leptons, anomaly free generation by generation, with three neutrino flavours, their masses, their
mixing and their flavour conversion; the chiral tip $Z$ portal of version 1 was removed. Version 3 (2026-10-18) added the portal
I13 (which gives the dark matter its relic abundance), definite benchmark strengths of the portals I11 and I12, the coupled
Kohn-Sham solution in ten environments, the thermal history, the magnitudes of the terms of the metric series, $\sigma_8$, the
Majorana alternative and the corrections of an independent review. Version 4 (2026-10-18), by the author's order of
2026-10-18 (15:42) to organise and present the solution better, contains the physics of version 3, re-presented: every field
equation and every interaction term is written out with its tag and its complete symbol list wherever it is used; every
interaction is explained (what it couples and why it is consistent with QCD and the electroweak model) and analysed (its
strength and its bounds); the $x_0$ mass mechanism is presented first as the author's uncertainty argument and then through the
exact $x_0$ eigenvalue equations; and every symbol has one meaning. Version 4 quotes the refined outputs of the precision fixes
made with the residual analysis of 2026-10-18 (52 further checks): the response of the $W$ eigenvalue to the I12 mean field of the
dark matter is $-0.11125$ per unit amplitude (version 3: $-0.1126$, limited by the rounding of finite elements) and that of the photon
exactly zero. The residual analysis also quantifies the places where two equations use the same quantity with different
approximations and the neglected terms that are not small (stated where they occur and collected in the last section).

# Summary

1. **Spacetime.** Eight dimensions with the author's coordinates $X = \{x_0, x_1, \dots, x_7\}$ and the frame signature
   $(+,+,+,+,-,-,-,-)$ in this order. The metric depends on $x_0$ only through $z = 6Hx_0$, periodically with the period $\pi$
   in $z$, i.e. with the period $\pi/(6H)$ in $x_0$ ($H$ the author's constant, $H = 14.296$ TeV in UM-2).
2. **Gravity.** Einstein-Lovelock gravity in eight dimensions with the author's weights $w_{(1)} = 1$, $w_{(2)} = 1/32$,
   $w_{(3)} = 1/1152$ and the cosmological constant $\Lambda = -10H^2$, kept unchanged; it couples to every field. A block
   stabiliser (a vacuum energy of the hidden block, ASSUMED) gives a stable static block at $K_* = 12 + \tfrac43\sqrt{51}$ on which
   four-dimensional gravity is attractive: its Einstein-Hilbert coefficient is $\mathcal{G}(K_*) = \tfrac{20}{3} + \sqrt{51} = 13.81 > 0$
   (DERIVED).
3. **The deflating extra times.** In the primordial era the extra times $x_5$, $x_6$, $x_7$ (and $x_0$ with them) deflate at rates
   up to $\lvert\mathcal{H}_f\rvert = 2.63H$ into the stabilised block; then the block oscillates with the radion frequency $3.387H$
   while 3-space keeps expanding (DERIVED, full nonlinear equations).
4. **dirac16complex** $\Psi$: a 16-component complex anticommuting spinor of the Clifford algebra of signature $(4,4)$ (Pin(4,4)
   irreducible; two inequivalent 8-dimensional irreducible representations of Spin(4,4)), coupled to gravity through the
   canonical spin connection, which is non-trivial, $\gamma^M\Omega_M = \tfrac32(H/f)\gamma^{x_0} + (\dot b_4/b_4 - \tfrac12\dot a_4)\gamma^{x_4}$,
   and to every other field through its self-interaction and the three portals. It splits into two Lorentz-invariant halves,
   $\Psi_A$ ($\mathcal{B} = -1$) and $\Psi_B$ ($\mathcal{B} = +1$), with $\mathcal{B} = -\mathrm{i}C\gamma^{x_4}$ the author's (Krein) operator.
5. **Standard-Model content (three generations, no Higgs particle).** Photon, gluons, $W^+$ (charge $+e$), $W^-$ (charge $-e$), $Z$
   (neutral); three generations of quarks (up and down, charm and strange, top and bottom); three generations of leptons, the
   left-handed doublets $\ell_1$, $\ell_2$, $\ell_3$ (the three-flavour left-handed neutrinos $\nu_e$, $\nu_\mu$, $\nu_\tau$ with the
   left-handed electron, muon and tau), the right-handed singlets of the electron, muon and tau, and a right-handed neutrino in
   each generation. The gauge
   anomalies cancel generation by generation. Electroweak symmetry is broken at the regular tip of the hidden direction by a
   non-linear sigma field $\Sigma \in SU(2)$ that has no radial mode, hence no Higgs particle.
6. **Masses and mixing.** Every four-dimensional mass is the eigenvalue of an $x_0$ operator acting on a wave function periodic in
   $x_0$ with the period $\pi/(6H)$. Massless: the graviton, the photon, the gluons (flat $x_0$ profiles) and the fold bands of
   $\Psi$ (chiral zero modes). Massive: $W^\pm$ and $Z$ (profiles bent at the tip), the twelve fermions (a doublet zero mode and a
   singlet zero mode of each fermion mixed at the tip by a $3\times3$ tip matrix in each sector), the bulk band of $\Psi$ and every
   Kaluza-Klein mode (DERIVED spectra, fitted to the measured masses with order-one parameters). The doublet bulk mass is common
   to the three generations of a sector; then the mixing matrices are $U = \mathcal{K}_e^\dagger\mathcal{K}_\nu$ and
   $V_{\mathrm{CKM}} = \mathcal{K}_u^\dagger\mathcal{K}_d$ (DERIVED, exact); with $\mathcal{K}_e = \mathcal{K}_u = \mathbf{1}$ (ASSUMED) they are the tip
   matrices $\mathcal{K}_\nu$ and $\mathcal{K}_d$, whose values are the measured PMNS and CKM matrices (STANDARD inputs). The author's
   uncertainty argument explains the heavy masses; the light masses come from the tip of the hidden cell.
7. **Three neutrino flavours.** Dirac neutrinos with the masses $1.000$, $8.712$ and $50.140$ meV (normal ordering, the NuFIT 6.0
   splittings, the lightest mass ASSUMED) and the PMNS mixing of NuFIT 6.0 (Dirac phase $212^\circ$). Their flavour conversion is
   computed in vacuum, in matter (the MSW effect), in the Sun, at accelerators, in the early Universe (where it accompanies
   neutrino decoupling, $N_{\mathrm{eff}} = 3.0432$), in the cosmic neutrino background (three mass eigenstates) and in supernovae (the
   MSW resonances of the envelope, the fast flavour instability of the dense neutrino gas and its effect on the explosions).
8. **New interactions (INVENTED).** Besides the tip sigma field, three portals couple $\Psi$ to the Standard Model: the
   gauge-kinetic portal I12 couples $\bar\Psi\Psi$ to pairs of gauge bosons ($W^+W^-$, $ZZ$, $Z\gamma$, $\gamma\gamma$, gluon pairs;
   benchmark strength $(38.2\ \text{TeV})^{-3}$, unitarity safe); the weak vector contact portal I11 couples the whole field to the
   $B - L$ fermion currents (benchmark $G_{\mathrm{V}} = 4.38\times10^{-17}$ GeV$^{-2}$: it produces the massless fold bands by freeze-in,
   $\Delta N_{\mathrm{eff}} = 0.001$); and the $x_0$-chiral vector portal I13 couples the current $\mathrm{i}\bar\Psi\gamma^MP_b\Psi$ ($M \ne x_0$),
   which vanishes on the fold bands, to the baryon-number current ($G_{\mathrm{A}} = 1.278\times10^{-9}$ GeV$^{-2}$). Every new
   interaction is invariant under $SU(3)_c\times SU(2)_L\times U(1)_Y$.
9. **The dark sector.** The lightest odd states of the two halves $\Psi_A$ and $\Psi_B$, two degenerate Dirac fermions of mass
   $3.1022\,m_\Psi = 44.35$ TeV ($m_\Psi = H$), are electrically and weakly neutral, stable by the fold parity, cold, and together the
   dark matter. I12 alone cannot produce their relic abundance within perturbative unitarity; with I13 they annihilate in the
   s-wave into quark pairs and freeze out with $\Omega_{\mathrm{DM}}h_{100}^2 = 0.060$ each, $0.120$ together (Boltzmann equation with the
   thermal history of the model; DERIVED); their scattering on xenon nuclei, $4.0\times10^{-46}$ cm$^2$ per nucleon, is 0.16 of the
   present LZ limit. The self-interaction of $\Psi$ must be weak, $G_\lambda \le 2.3\times10^{-15}$ GeV$^{-2}$ (ASSUMED), or the dark
   matter would thermalise the fold bands. No state of $\Psi$ is dark energy; the dark energy of UM-2 is a tuned four-dimensional
   cosmological term.
10. **Cosmology.** The four-dimensional effective theory of the stabilised block is exact general relativity, so the CMB, the CNB
    and the BAO follow from the standard Einstein-Boltzmann equations with the UM-2 particle content; $\sigma_8 = 0.812$. The metric is
    a power series of terms of decreasing magnitude: the order-one cosmological potentials are $2.4\times10^{-5}$ and smaller, the
    order-two terms $6\times10^{-10}$, the radion $10^{-34}$, and the Kaluza-Klein gravitons act only below $10^{-21}$ m.
11. **The coupled solution.** The Kohn-Sham equations of dirac16complex, coupled to gravity (the block response) and to the mean
    fields of every Standard-Model field (I11, I12, I13), are solved self-consistently from the cosmic mean density to neutron-star
    cores and through the early Universe: the back-reactions are small (the dark-matter level moves by at most $1.5\times10^{-6}$ of
    its mass, at the dark-matter freeze-out; the block by $\Delta\ln f \le 1.1\times10^{-34}$, pushed by the hot plasma at the
    freeze-out, and by at most $10^{-48}$ from nucleosynthesis on), so the solution is the stabilised background with the $x_0$
    spectra, the Kohn-Sham states and the linear cosmological perturbations, and the coupled corrections are computed.

