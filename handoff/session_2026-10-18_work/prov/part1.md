---
title: "UM-2 provenance"
subtitle: "Where every ingredient, interaction, field equation and number of the universe model UM-2 comes from, how it was computed, and how it was verified"
author:
  - "Underlying theory: Patrick L. Nash"
  - "Derived and verified by Claude (Anthropic)"
  - "Provenance, version 4, 2026-10-18"
  - "Versions 3 and 2: 2026-10-18; version 1: 2026-10-17"
  - "Repository once-ere/Dirac_claude, folder universe_model_2"
---

# How to read this document

**What it contains.** This document records the provenance of UM-2, a model of the Universe built on the author's
4+4-dimensional Einstein-Lovelock theory and his dirac16complex field, coupled to gravity and to every field of the Standard
Model without a Higgs particle. It states, for every ingredient, where it comes from (the author's orders and notebooks,
the Revision record of this repository, standard physics and measured values, or the choices and inventions of UM-2),
writes it out as an equation, names the computation that produced or used it and the checks that verify it. The sections
are: the author's orders, quoted (section 2); who did what (section 3); the ingredients taken from the author (section 4)
and from the Revision record (section 5); the action of UM-2 term by term, each of the 18 interaction terms IN-1 to IN-18
written out with its origin, and for every invented term the reason and its consistency with QCD and the electroweak
model (section 6); the measured values and standard physics used, with their sources (section 7); the origin of every one
of the 136 field equations FE-1 to FE-136 in one table (section 8); the computations, their outputs and their 287 checks
(section 9); the residuals of the approximate solution in its field equations and in concert, and the precision fixes of
version 4 (section 10); the verification record (section 11); the history of the corrections (section 12); what is not in
the repository (section 13); the reproduction (section 14); and the history of UM-2 in the repository (section 15).

**Status labels.** Every ingredient and result carries one of these labels:

* **AUTHOR**: taken from the author's Mathematica notebooks or from the author's written orders;
* **RECORD**: taken from the Revision record of this repository (earlier work carried out under the author's orders,
  with its own verification);
* **STANDARD**: textbook physics or a measured value; a measured value is marked *verified* (read from the source on
  2026-10-17 or 2026-10-18) or *from memory* (quoted from memory of the standard tables, to be checked against the current
  editions);
* **ASSUMED**: a modelling choice made for UM-2;
* **INVENTED**: a new phenomenological interaction or ingredient of UM-2;
* **DERIVED**: computed and verified in UM-2; the verification is named with the result;
* **ESTIMATE**: an order-of-magnitude evaluation, not a precision computation;
* **OPEN**: not resolved in this version.

**Equations and symbols.** Every display equation is followed by the complete list of its symbols: every quantity,
field, coupling, constant, operator, index (with the values it takes) and special mark, with its meaning, its unit, its
value where it has one, and its status. Typography needs no definition (digits, $+$, $-$, $=$, brackets, fractions,
roots, $\cdot$, $\dots$, $\le$, $\approx$, $\sim$, $\times$, the standard functions sin, cos, tan, cot, sinh, cosh, tanh,
exp, ln, log, det, min, max, lim and the signs of sums, products and integrals; their index letters and integration
variables are symbols and are listed). The tags IN-$n$ and FE-$n$ are one numbering, shared by all documents of UM-2, of
the 18 interaction terms of the action and of the 136 field equations; an interaction term or a field equation that this
document uses is written out here with its tag and its symbols. A symbol has one meaning throughout the document, in the
displays, in the inline formulas and in the text. Euler's number is written $\mathrm{e}$, the imaginary unit $\mathrm{i}$
and the differential $\mathrm{d}$. Names of the computations' checks are quoted literally in typewriter type, in the
spelling of the code.

**Units and conventions.** $\hbar = c = 1$. $H$ is the author's constant (an inverse length); in the numerical work on the
block $H = 1$ unless a physical unit is given, and its physical value is $H = 14.296$ TeV. The coordinates are always the
author's $X = \{x_0, x_1, \dots, x_7\}$: $x_0$ the hidden space-like direction, listed first, periodic with the period
$\pi/(6H)$; $x_1, x_2, x_3$ ordinary space; $x_4$ the time; $x_5, x_6, x_7$ the three extra time-like directions. $W^+$
carries the electric charge $+e$ and $W^-$ the charge $-e$. UM-2 contains no Higgs particle.

**The numbers.** Every number is taken from the outputs of the computations of UM-2 (the scripts in
`universe_model_2/code/`, which write `universe_model_2/outputs/` and `universe_model_2/reports/`) and is quoted with the
precision of the output; section 9 names the output that holds it. These files are named for reproduction only: every
equation, definition and argument that the reader needs is written in this document.

**Versions.** Version 1 (2026-10-17) had one generation of quarks and leptons. Version 2 (2026-10-18) has three generations
and three neutrino flavours with their mixing and flavour conversion, ordered by the author on 2026-10-18, and removes the
chiral tip $Z$ portal of version 1 (corrections, item 21; its independent review, item 22). Version 3 (2026-10-18) answers
the author's order to find and document an accurate approximate solution of the coupled field equations with Kohn-Sham
theory for dirac16complex coupled to gravity and to every Standard-Model field: the portal I13, the benchmark strengths of
I11 and I12, the coupled solution in environments, the thermal history and the dark-matter relic, the magnitudes of the
terms of the metric series, $\sigma_8$ and the Majorana alternative (item 23; its independent review, item 24). **Version
4** (2026-10-18) answers the author's order of 2026-10-18, 15:42, to organise and present the solution better: one
notation in which every symbol has one meaning, a registry of every symbol with its meaning and unit, an inventory of the
136 field equations and 18 interaction terms, every equation followed by its symbols, the residuals of the approximate
solution in each of its field equations and in concert (52 new checks, 287 in all), and five precision fixes of the
computations (item 25). The physics and the claims of version 3 are unchanged; every changed number is stated in item 25
and in section 10.

# The orders

## The order of 2026-10-17

The model answers the author's order of 2026-10-17. Its key parts, in the author's words: "Create a new model of the
Universe that includes [a] gravity (Einstein-Lovelock gravity); [b] the dirac16complex quantized spinor field (which is
hypothesied to represent dark matter); the dirac16complex is coupled to gravity using a non-trivial canonical spin
connection; ... interactions of gravity and dirac16complex with SOME of the following Standard Model particles: [c]
photons; [d] neutrinos; [e] electrons; [f] quarks (only up and down, for the protons and neutrons); [g] the 3 weak
interaction gauge bosons, the W and Z 'particles'. However do NOT include the Higgs particle. You must invent/create
new phenomenological interactions ... consistent with qcd and electro-weak models. You want to be able to model: CMB,
CNB, BAO, so your model for the metric tensor ... must be very general, but perhaps expressible as a power series of
terms of decreasing magnitude. Put each and every interaction in equation form, and explain and analyze it in
documentation and provenance files; these should be both markdown and latex file types; compile all latex to pdf.
NEVER refer the reader to some other file! PUT EVERY EQUATION you create and/or use IN THESE FILES. CRITICALLY
IMPORTANT: Mass will be given to all non-massless particles, (except the massless particles: graviton, photon and
perhaps the quanta of the dirac16complex field), by appropriate wave function dependence on the space coordinate x0
... periodic in x0 with period pi/(6H). Localization with respect to x0 implies, using Heisenberg ... Delta x0 * Delta
(p)x0 >= hbar/2 ... [2] push your new, improved, model ... along with provenance (both .md and .pdf files). [3] Compute
the coupled field equations and push to repo; create concomitant documention (both .md and .pdf files) and push. [4]
Compute an accurate approximate solution to the coupled field equations (use Kohn-Sham theory for the dirac16complex
field, which couples to all other fields) and push ... Check and verify this repo."

Further orders of the same day: "analyze the x0 mass mechanism, and ... analyze the validity of associating dark matter
(and dark energy) with dirac16complex"; "the W+ and W- bosons carry positive and negative electric charges. Do not forget
this"; the coordinates are always the author's $\{x_0, x_1, \dots, x_7\}$ of the notebook
`Dirac_Einstein-Lovelock_4+4_Nash.nb`, never relabelled; every verified result is pushed to the repository as soon as it
is obtained; no single calculation runs longer than 7 minutes and 3 seconds (423 s) (this limit was lifted on
2026-10-18).

## The orders of 2026-10-18: three neutrino flavours

On 2026-10-18 the author stated that neutrino flavour and flavour conversion are critically important in this project and
asked that the paper of Gogilashvili and Tamborra on neutrino flavour conversion in core-collapse supernovae (his file
"Neutrino Flavor Conversion.pdf", arXiv:2605.16504; not committed, it is a third-party paper) be read, understood and
remembered (paraphrase). He then ordered (08:02), in his words: "correct universe model 2 to include three neutrino
flavors with mixing and flavor conversion. this is your first and only priority!! ... do correct universe model 2 to
include three neutrino flavors with mixing and flavor conversion NOW." Two ways were put to him: (A) three full
generations of quarks and leptons, anomaly free generation by generation; (B) three lepton generations with the single
quark generation of version 1, whose gauge anomalies would have to be cancelled by an added Wess-Zumino term. His answer
(08:24): "NOT (B). USE (A)!!!". Version 2 implements (A). A flavour is defined by the charged lepton produced with the
neutrino in a charged-current process, so three neutrino flavours require the muon and the tau; with them, anomaly freedom
requires the second and third quark generations (a single quark generation would leave the mixed $SU(2)^2U(1)_Y$ anomaly
coefficient $-1$ and the $U(1)_Y^3$ coefficient $3/2$; DERIVED).

## The order of 2026-10-18 for version 3

After the three-flavour correction the author ordered (09:48), in his words (excerpts): "find and document (with
provenance) an accurate approximate solution for your new model universe, i.e., of the coupled field equations, with
Kohn-Sham theory for the dirac16complex field coupled to gravity and to all of the Standard-Model fields; coupled fields
include gravity (Einstein-Lovelock gravity, which couples to all fields), the dirac16complex quantized fermion spinor field
(which couples to all other fields), the three-flavour version of left-handed neutrinos, the usual left-handed electrons,
the usual singlet right-handed electron, three quark generations, gluons, photons, the 3 weak interaction gauge bosons, the
W^(+), W^(-), and Z 'particles'. However do NOT include the Higgs particle. You must invent/create and document new
phenomenological interactions for these standard model particles that should be consistent with qcd and electro-weak
models. You want to be able to model: CMB ..., CNB ..., BAO ..., so your model for the metric tensor of the gravitation
field must be very general, but perhaps expressible as a power series of terms of decreasing magnitude. CRITICALLY
IMPORTANT: Mass will be given to all non-massless particles ... by appropriate wave function dependence on the space
coordinate x0 ..., which must be periodic in x0 with period pi/(6H). ... Put each and every interaction in equation form,
and explain and analyze it in documentation and provenance files; these should be both markdown and latex file types;
compile all latex to pdf. NEVER refer the reader to some other file! PUT EVERY EQUATION you create and/or use IN THESE
FILES. In your documentations and provenances i want you to analyze the x0 mass mechanism, and to analyze the validity of
associating dark matter (and dark energy) with dirac16complex. [2] push your new, improved, model of the Universe to the
repo, along with provenance (both .md and .pdf files). [3] Compute the coupled field equations and push to repo ... [4]
Compute an accurate approximate solution to the coupled field equations (use Kohn-Sham theory for the dirac16complex field,
which couples to all other fields) and push to repo ... Check and verify this repo. DO NOT TAKE SHORTCUTS. ... [5] Continue
and Complete and push all stages that are still open". Version 3 keeps the three generations of version 2 (with
right-handed neutrinos for the Dirac masses of the $x_0$ mechanism; the Majorana alternative without them is analysed) and
adds the items listed in section 1.

## The order of 2026-10-18, 15:42, for version 4

The author's order of 2026-10-18 at 15:42, in his words:

> "STOP or PAUSE everything. We need to organize and present your solution better. ... precisely, but approximately,
> solve the coupled field equations and find and document (with provenance) an accurate approximate solution for your
> new model universe, i.e., of the coupled field equations, with Kohn-Sham theory for the dirac16complex field coupled to
> gravity and to all of the Standard-Model fields; coupled fields include gravity (Einstein-Lovelock gravity, which couples
> to all fields), the dirac16complex quantized fermion spinor field (which couples to all other fields), the three-flavour
> version of left-handed neutrinos, the usual left-handed electrons, the usual singlet right-handed electron, three quark
> generations, gluons, photons, the 3 weak interaction gauge bosons, the W^(+), W^(-), and Z 'particles'. However do NOT
> include the Higgs particle. You must invent/create and document new phenomenological interactions for these standard
> model particles that should be consistent with qcd and electro-weak models.
> For each and every field equation that you use, you must clearly state, write down, document the field equation itself,
> define each and every symbol that appears in the field equation EVEN if you have done this before. This a command not a
> request. I do NOT want students struggling to find definitions, when they should be finding (numerical or analytical)
> solutions. Analyze your approximate solution (usually in concert with other field equation) in a documentation
> presentation (markdown and latex, compiled to pdf versions, ALWAYS).
> You want to be able to model: CMB, CNB, BAO, so your model for the metric tensor of the gravitation field must be very
> general, but perhaps expressible as a power series of terms of decreasing magnitude.
> CRITICALLY IMPORTANT: Mass will be given to all non-massless particles (except the massless particles: graviton, photon
> and perhaps the quanta of the dirac16complex field), by appropriate wave function dependence on the space coordinate x0
> (either explicit, derived, or assumed), which must be periodic in x0 with period pi/(6H). Localization with respect to
> x0 implies, using Heisenberg Uncertainty Principle, Delta x0 * Delta (p)x0 >= hbar/2 (here (p)x0 is the x0 th component
> of momentum), and you can think of momentum as being proportional to mass, and you can think of kinetic energy as being
> proportional to momentum-squared divided by mass, hence giving rise to an (effective) mass for all particles whose wave
> function is periodic in space coordinate x0. This is true, except for the graviton, photon and perhaps the quanta of the
> dirac16complex field.
> Put each and every interaction in equation form, and explain and analyze it in documentation and provenance files;
> these should be both markdown and latex file types; compile all latex to pdf.
> NEVER refer the reader to some other file! PUT EVERY EQUATION you create and/or use IN THESE FILES.
> In your documentations and provenances i want you to analyze the x0 mass mechanism, and to analyze the validity of
> associating dark matter (and dark energy) with dirac16complex."

Two minutes later (15:44): "do not forget to push results as soon as they are completed and verified".

Version 4 answers the order with six binding rules for all documents of UM-2: (S1) every display equation is followed by
the complete list of its symbols, generated from one registry, and every field equation or interaction term that a
document uses is written out there with its tag and its symbols; (S2) one symbol, one meaning, across all documents (the
notation of version 4 resolves every symbol that version 3 used for several things); (S3) the registry of the symbols and
the inventory of the field equations and interaction terms; (S4) every document starts with "How to read this document",
and a solution is presented as the field equation, the approximation, the solution, its check in its own equation and in
concert with the other field equations, and the status labels; (S5) the reader is never sent to another file; (S6) the
status labels and the conflicts with data stay as in version 3, and every change of a claim is stated here. How each rule
was implemented, and what was computed anew for it, is item 25 of the corrections and section 10.

# Who did what

* The 4+4 framework, the coordinates, the primordial metric of the notebooks, the Einstein-Lovelock action with its
  weights and its cosmological term, the dirac16complex field and its real $16\times16$ gamma matrices of the Clifford
  algebra of signature $(4, 4)$, the mass parameter, the idea that masses come from the $x_0$ dependence of wave functions
  periodic with the period $\pi/(6H)$, the dark-matter hypothesis, the demand for three neutrino flavours with mixing and
  flavour conversion and the presentation rules of version 4 are the AUTHOR's (Patrick L. Nash).
* The corrected primordial metric, the regular tip cutoff, the Dirac-type Lagrangian with the canonical spin connection,
  the $2\times2$ block reduction of the Kohn-Sham problem and its conventions are RECORD items: produced earlier in this
  repository under the author's orders and verified there.
* Everything labelled ASSUMED, INVENTED or DERIVED below, all the code of UM-2 and all its documents are by Claude
  (Anthropic), working in this repository on 2026-10-17 (version 1) and 2026-10-18 (versions 2, 3 and 4).

