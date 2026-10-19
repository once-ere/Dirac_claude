---
title: "UM-2 field equations"
subtitle: 'The coupled field equations of Einstein-Lovelock gravity, the dirac16complex field, three generations of quarks and leptons, the gluons, the photon and the $W^+$, $W^-$ and $Z$ bosons (no Higgs particle), the tip sigma field and the block stabiliser, with every interaction'
author:
  - "Underlying theory: Patrick L. Nash"
  - "Derived and verified by Claude (Anthropic)"
  - "Field equations, version 4, 2026-10-18 (versions 1 to 3: 2026-10-17 and 2026-10-18)"
  - "Repository once-ere/Dirac_claude, folder universe_model_2"
---

# How to read this document

## What this document contains

This document states the complete set of coupled field equations of the universe model UM-2, derives them from one action,
and explains every term. It is self-contained: every equation that it uses is written in it, and every symbol of every
equation is defined right after the equation. The sections are:

* **The action** (IN-1 to IN-18): every term of the action, written out and explained: what it couples, and why it is
  consistent with QCD and with the electroweak theory.
* **Gravity** (FE-1 to FE-11): the Einstein-Lovelock equations, the energy-momentum tensor of every field and its
  conservation.
* **The matter fields** (FE-12 to FE-30): the field equations of dirac16complex, of the three generations of quarks and
  leptons, of the gauge fields (gluons, $W^\pm$, $Z$, photon), of the tip sigma field, and their boundary conditions.
* **The background** (FE-31 to FE-49): the exact order-0 equations of the metric, the static block and its stabiliser, the
  radion, the response of the block to matter and four-dimensional gravity.
* **The masses from the hidden coordinate** (FE-50 to FE-62): the $x_0$ eigenvalue problems that give every particle its
  mass (the gauge bosons, the graviton tower, the twelve fermions with their mixing, dirac16complex).
* **dirac16complex coupled to all fields** (FE-63 to FE-86): the Kohn-Sham equations of dirac16complex with the mean fields
  of every other field, the portals on the zero modes, the condensates of the Standard-Model plasma, and the block response
  that closes the loop.
* **The linear perturbations** (FE-87 to FE-99): the metric as a power series, the Einstein-Boltzmann equations of the CMB,
  the CNB and the BAO.
* **The three neutrino flavours** (FE-100 to FE-120): the neutrino masses, the four-fermion interactions, the flavour
  evolution in vacuum, in matter, in the early Universe and in dense neutrino gases.
* **The thermal history** (FE-121 to FE-136): the degrees of freedom, the Boltzmann equations of the dark matter, of the
  fold bands of dirac16complex and of the right-handed neutrinos.
* **The coupled system**: which fields appear in which equations, and how the system is solved, step by step.
* **What was verified**: the 287 checks of the computations and the residuals of the solution in 26 of the equations.

## The status labels

Every equation and every result carries one of the labels

* **AUTHOR**: from the author's notebooks (the metric, the coordinates, the Lovelock weights, the field dirac16complex);
* **RECORD**: from the Revision record of this repository (the dirac16complex Lagrangian and its Kohn-Sham treatment);
* **STANDARD**: textbook physics;
* **ASSUMED**: a choice made in UM-2 without derivation;
* **INVENTED**: a new interaction or construction of UM-2 (the tip sigma field, the portals I11, I12, I13);
* **DERIVED**: computed and verified in UM-2 (the verification is stated);
* **ESTIMATE**: an order-of-magnitude evaluation;
* **OPEN**: not settled.

## Every equation is followed by its symbols

Every display equation is followed by the list "Symbols in (FE-n)" (or "Symbols in this equation" for a display without a
tag) of EVERY symbol that appears in it: every quantity, field, coupling, constant and operator, every index letter with the
values it takes, every mark (prime, dagger, transpose, star), the imaginary unit, Euler's number and the differential. Each
item gives the meaning, the unit (natural units $\hbar = c = 1$), the value where one exists, and the status. A field
equation carries the tag FE-1 to FE-136 and an interaction term of the action the tag IN-1 to IN-18; the numbering is that of
the inventory of UM-2 and is the same in every UM-2 document. Displays without a tag are steps of a derivation.

## Coordinates, signature and units

The author's coordinates are $X = \{x_0, x_1, \dots, x_7\}$, always with the hidden direction first: $x_0$ is the hidden
space-like coordinate, on which the metric depends periodically with the period $\pi/(6H)$ through the angle $z = 6Hx_0$;
$x_1, x_2, x_3$ are ordinary space, $x_4$ is the time, and $x_5, x_6, x_7$ are three extra time-like coordinates. The
signature is $(+,+,+,+,-,-,-,-)$ in this order; the four observable coordinates $x_1, \dots, x_4$ have the signature
$(+,+,+,-)$. $H = 14.296$ TeV is the author's constant (an inverse length). Units are natural, $\hbar = c = 1$; in eight
dimensions a fermion field has the dimension GeV$^{7/2}$ and the gravitational coupling $\kappa = 8\pi G_8$ the dimension
GeV$^{-6}$. A dot is the derivative with respect to the time $x_4$; a prime is used only in the cosmological perturbation
equations, for the derivative with respect to the conformal time.

## The fields of UM-2

The author orders a model universe with the following coupled fields; UM-2 adds the tip sigma field (which replaces the
Higgs field) and the stabiliser of the block.

| field | symbol | what it is | it couples to | field equations |
| ----------------- | ---------- | ---------------------- | ------------------------ | ------------------------ |
| Einstein-Lovelock gravity | $g_{MN}$ | the metric of eight dimensions | every field | FE-1 to FE-11, FE-31 to FE-49, FE-87 to FE-99 |
| dirac16complex | $\Psi$ | the author's 16-component spinor field; its odd level is the dark matter | gravity, itself, every fermion (I11, I13), every gauge field (I12) | FE-5, FE-12, FE-13, FE-28, FE-62 to FE-73 |
| left-handed neutrinos (three flavours) | $\nu_e$, $\nu_\mu$, $\nu_\tau$ in $\ell_i$ | the upper members of the lepton doublets | gravity, $W^\pm$, $Z$, $\Sigma$ (masses with $\nu_R$), $\Psi$ (I11) | FE-17, FE-19, FE-100 to FE-120 |
| left-handed electrons and the right-handed electron singlet, with the muon and tau generations | $\ell_i$, $e_{Ri}$ | the lower members of the lepton doublets and the charged-lepton singlets | gravity, $W^\pm$, $Z$, photon, $\Sigma$, $\Psi$ (I11) | FE-17, FE-18 |
| three quark generations | $Q_i$, $u_{Ri}$, $d_{Ri}$ | the quark doublets and singlets | gravity, gluons, $W^\pm$, $Z$, photon, $\Sigma$, $\Psi$ (I11, I13) | FE-14 to FE-16 |
| gluons | $G^A_M$ | the gauge field of SU(3) | quarks, $\Psi$ (I12), gravity | FE-7, FE-22, FE-74, FE-75 |
| photon | $A_M$ | the massless combination of $W^3$ and $B$ | charged fermions, gravity | FE-24, FE-25, FE-50 to FE-52 |
| $W^+$, $W^-$, $Z$ | $W^\pm_M$, $Z_M$ | the massive weak bosons | fermions, $\Sigma$, $\Psi$ (I12), gravity | FE-23 to FE-25, FE-51, FE-55 |
| no Higgs particle | | | | |
| tip sigma field | $\Sigma$ | a unitary $2 \times 2$ matrix field on the tip: the longitudinal $W^\pm$, $Z$ | $W$, $B$, every fermion at the tip | FE-8, FE-26, FE-30 |
| block stabiliser | $\rho_{\mathrm{stab}}$ | a vacuum energy of the block | gravity | FE-4, FE-43 |

The gauge fields of the action are the SU(3) field $G$, the SU(2) field $W$ (components $W^1$, $W^2$, $W^3$) and the hypercharge
field $B$; $W^+$, $W^-$, $Z$ and the photon $A$ are their physical combinations (IN-10). The right-handed neutrinos $\nu_R$ are
gauge singlets: they give the neutrinos Dirac masses at the tip and are never thermalised.

## Conventions of version 4

Version 4 changes the presentation of version 3, not its physics. Every symbol has one meaning in the whole document (the
symbols of version 3 that had several meanings are replaced); Euler's number is $\mathrm{e}$, the imaginary unit $\mathrm{i}$, the
differential $\mathrm{d}$; a word or a particle name in a subscript is upright ($M_{\mathrm{Pl}}$, $m_{\mathrm{W}}$, $n_{\mathrm{e}}$), an italic letter in
a subscript is an index. $\Delta$ denotes a change (a variation, a first-order perturbation, a level shift), $\delta$ the Kronecker
delta and $\delta_{\mathrm{D}}$ the Dirac delta function. The gauge fields $G$, $W$, $B$ are in the geometric normalisation (the couplings
stand in front of their kinetic terms), in eight and in four dimensions; $W^\pm$, $Z$, $A$ and $F^V_{\mu\nu}$ are canonically normalised.
$W^+$ carries the electric charge $+e$ and $W^-$ the charge $-e$. Two equations of version 3 are written more explicitly: the
block components of the background equations (FE-40, FE-42, FE-43) show the pressure $p_0$ of the hidden direction and the
pressure $p_5$ of the extra times separately (version 3 wrote only their average $\bar p$, and in one place $p_0$; section
"The background", subsection "The block pressures"), and the overlap integrals of the portals carry their factor $1/H$
explicitly (FE-70, FE-135). No number of version 3 changes.
