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

# Ingredients from the author (AUTHOR)

## Coordinates and signature

The author's coordinates (notebook `Dirac_Einstein-Lovelock_4+4_Nash.nb`, `X = {x0[], x1[], ..., x7[]}`) are

$$
X = \{x_0, x_1, x_2, x_3, x_4, x_5, x_6, x_7\},\qquad z = 6Hx_0,\qquad 0 < z < \pi
$$

<!-- symbols: Xcoord, x0, x1, x2, x3, x4, x5, x6, x7, zvar, Hconst, pi -->
<!-- begin generated symbol list -->
**Symbols in this equation.**

- $X = \{x_0, \dots, x_7\}$: The author's coordinates of the eight-dimensional spacetime, $X = \{x_0, x_1, \dots, x_7\}$ with the hidden direction first; $X^M$ is the coordinate with the index $M$, $\mathrm{d}^8X = \mathrm{d}x_0\,\mathrm{d}x_1\cdots\mathrm{d}x_7$ the coordinate volume element and $X^\mu$ (four-dimensional index $\mu$) the observable coordinates $x_1, \dots, x_4$. Unit: length (each coordinate). Status: AUTHOR.
- $x_0$: The hidden space-like coordinate (listed first); the metric depends on it through $z = 6Hx_0$, periodically with the period $\pi/(6H)$. Unit: length. Status: AUTHOR.
- $x_1$: The first coordinate of ordinary 3-space. Unit: length. Status: AUTHOR.
- $x_2$: The second coordinate of ordinary 3-space. Unit: length. Status: AUTHOR.
- $x_3$: The third coordinate of ordinary 3-space (also the symmetry axis of the fast-flavour analysis). Unit: length. Status: AUTHOR.
- $x_4$: The time; dots denote $\mathrm{d}/\mathrm{d}x_4$. Unit: length (= time, c = 1). Status: AUTHOR.
- $x_5$: The first of the three extra time-like coordinates. Unit: length. Status: AUTHOR.
- $x_6$: The second of the three extra time-like coordinates. Unit: length. Status: AUTHOR.
- $x_7$: The third of the three extra time-like coordinates. Unit: length. Status: AUTHOR.
- $z$: The angle variable of the hidden direction, $z = 6Hx_0$; one period of $x_0$ is $0 < z < \pi$. Unit: dimensionless. Status: AUTHOR.
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the Lovelock couplings, the cosmological constant $\Lambda = -10H^2$ and the mass parameter $m_\Psi = H$. Unit: GeV (1/length). Value: 14.296 TeV (from the fit of $m_{\mathrm{W}}$ and $\rho_{\mathrm{EW},0}$). Status: AUTHOR.
- $\pi$: The number pi, the ratio of the circumference of a circle to its diameter. Unit: dimensionless. Value: 3.141592654. Status: STANDARD.

<!-- end generated symbol list -->

with $x_0$ a hidden space-like direction, $x_1, x_2, x_3$ ordinary space, $x_4$ the time and $x_5, x_6, x_7$ three extra
time-like directions; the interval $0 < z < \pi$ is one period of $x_0$, of length $\pi/(6H)$. The orthonormal frame
metric, with the frame directions aligned with $x_0, \dots, x_7$ in this order, is

$$
\eta_{ab} = \mathrm{diag}(+1, +1, +1, +1, -1, -1, -1, -1)
$$

<!-- symbols: eta, ia, ib, diag -->
<!-- begin generated symbol list -->
**Symbols in this equation.**

- $\eta_{ab}$: The flat metric of the frame, $\eta_{ab} = \mathrm{diag}(+1, +1, +1, +1, -1, -1, -1, -1)$ ($\eta^{ab}$ the same matrix). Unit: dimensionless. Status: AUTHOR.
- $a$: A frame (orthonormal) index running over $0, 1, \dots, 7$, aligned with $x_0, \dots, x_7$; raised and lowered with $\eta_{ab}$; a repeated index is summed (except in a sectional curvature $R^{ab}{}_{ab}$). Status: STANDARD.
- $b$: A frame index running over $0, \dots, 7$ (as $a$). Status: STANDARD.
- $\mathrm{diag}$: A diagonal matrix with the listed entries on its diagonal (in the order of the coordinates $x_0, x_1, \dots, x_7$ when it is a tensor in eight dimensions). Status: STANDARD.

<!-- end generated symbol list -->

## The primordial metric of the notebooks

The notebook `WaveFunctionUniverse-4+4-Einstein-Lovelock.nb` (the author's local notebook) gives the primordial metric

$$
\begin{aligned}
g_{\mathrm{nb}} = \mathrm{diag}\big(&\cot^2z,\ \mathrm{e}^{2a_4}(\sin^2z)^{1/6},\ \mathrm{e}^{2a_4}(\sin^2z)^{1/6},
 \ \mathrm{e}^{2a_4}(\sin^2z)^{1/6},\\
&-1,\ -\mathrm{e}^{-2a_4}(\sin^2z)^{1/6},\ -\mathrm{e}^{-2a_4}(\sin^2z)^{1/6},\ -\mathrm{e}^{-2a_4}(\sin^2z)^{1/6}\big)
\end{aligned}
$$

<!-- symbols: mod_gnb, diag, zvar, euler, a4 -->
<!-- begin generated symbol list -->
**Symbols in this equation.**

- $g_{\mathrm{nb}}$: The metric of the author's notebook (before the author's order of 2026-10-14 added the factor $b_4$ to the extra-time components), written as the diagonal matrix of its components in the order $x_0, x_1, \dots, x_7$; it is quoted for comparison only, the model uses the corrected metric $\bar g_{MN}$. Unit: dimensionless. Status: AUTHOR.
- $\mathrm{diag}$: A diagonal matrix with the listed entries on its diagonal (in the order of the coordinates $x_0, x_1, \dots, x_7$ when it is a tensor in eight dimensions). Status: STANDARD.
- $z$: The angle variable of the hidden direction, $z = 6Hx_0$; one period of $x_0$ is $0 < z < \pi$. Unit: dimensionless. Status: AUTHOR.
- $\mathrm{e}$: Euler's number, the base of the natural logarithm; $\mathrm{e}^{X}$ is the exponential of $X$. Unit: dimensionless. Value: 2.718281828. Status: STANDARD.
- $a_4$: The author's metric function of the time $x_4$ that scales ordinary 3-space: the scale factor of cosmology is $\mathrm{e}^{a_4}$. Unit: dimensionless. Status: AUTHOR.

<!-- end generated symbol list -->

with the vielbein $\mathrm{diag}\big(\cot z$, three times $\mathrm{e}^{a_4}(\sin^2z)^{1/12}$, $1$, three times
$\mathrm{e}^{-a_4}(\sin^2z)^{1/12}\big)$ and $a_4 = a_4(x_4)$. By the author's orders of 2026-10-14 a second function
$b_4(x_4) > 0$ multiplies the extra-time components ("b4 is a function of x4; b4 is NEVER 1"), and $(\sin z)^{1/3}$ means
$(\sin^2z)^{1/6}$, the positive branch, for every real $z$. The metric that UM-2 uses, the corrected metric of the Revision
record (FE-31), is written out in section 5.

## The Einstein-Lovelock equations, the weights and the cosmological term

The notebook writes the vacuum Einstein-Lovelock equations (after Lovelock and Rund) as

$$
0 = -10\,\delta^M_N + \frac{w_{(1)}}{H^2}\,\mathcal{E}_{(1)}{}^M{}_N + \frac{w_{(2)}}{H^4}\,\mathcal{E}_{(2)}{}^M{}_N
 + \frac{w_{(3)}}{H^6}\,\mathcal{E}_{(3)}{}^M{}_N,\qquad
w_{(1)} = 1,\quad w_{(2)} = \frac{1}{32},\quad w_{(3)} = \frac{1}{1152}
$$

<!-- symbols: delta, iM, iN, wL, Hconst, LovE -->
<!-- begin generated symbol list -->
**Symbols in this equation.**

- $\delta$: The Kronecker delta: with two indices $\delta^M_N = 1$ if $M = N$ and 0 otherwise (likewise $\delta_{\alpha e}$, $\delta_{l0}$, $\delta^{I3}$); with upper and lower index strings the generalised Kronecker delta $\delta^{M_1\cdots M_n}_{N_1\cdots N_n}$, the determinant of the $n \times n$ matrix of Kronecker deltas $\delta^{M_a}_{N_b}$ (+1 or -1 if the upper indices are an even or odd permutation of the lower ones, 0 otherwise). Status: STANDARD.
- $M$: A coordinate index of eight dimensions (also with a numbered copy $M_1, M_2, \dots$): it runs over $x_0, x_1, \dots, x_7$; a repeated index is summed. Status: STANDARD.
- $N$: A coordinate index of eight dimensions (also $N_1, N_2, \dots$), running over $x_0, \dots, x_7$; a repeated index is summed. Status: STANDARD.
- $w_{(p)}$: The author's Lovelock weights, $w_{(1)} = 1$, $w_{(2)} = 1/32$, $w_{(3)} = 1/1152$. Unit: dimensionless. Value: $(1, 1/32, 1/1152)$. Status: AUTHOR.
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the Lovelock couplings, the cosmological constant $\Lambda = -10H^2$ and the mass parameter $m_\Psi = H$. Unit: GeV (1/length). Value: 14.296 TeV (from the fit of $m_{\mathrm{W}}$ and $\rho_{\mathrm{EW},0}$). Status: AUTHOR.
- $\mathcal{E}_{(p)}{}^M{}_N$: The Lovelock tensor of order $p$, the metric variation of $\sqrt{\lvert g\rvert}\mathcal{L}_{(p)}$: $\mathcal{E}_{(1)}$ is the Einstein tensor $R^M{}_N - \frac12\delta^M_NR$; every $\mathcal{E}_{(p)}$ is divergence free. Unit: 1/$\mathrm{length}^{2p}$. Status: STANDARD.

<!-- end generated symbol list -->

where the notebook's tensor "Lovelock$p$" is the Lovelock tensor $\mathcal{E}_{(p)}{}^M{}_N$ of order $p$. In the notebook
`Dirac_Einstein-Lovelock_4+4_Nash.nb` (In[133] to In[136]) the author sets $w_{(1)} = 1$, $w_{(2)} = 1/2^5$ and solves the
vacuum equations on the history $a_4 = Hx_4$, $b_4 = 1$ of the notebook metric for $w_{(3)}$ and for the cosmological
number (In[134]); In[136] factors $1152 = 2^7\,3^2$; the Revision specification records the solution $w_{(3)} = 1/1152$
and the number $10$. Multiplying by $H^2$ and writing the equations as the Einstein-Lovelock equations with a source gives
the couplings and the cosmological constant of UM-2,

$$
\alpha_{(p)} = w_{(p)}\,H^{2-2p},\qquad \Lambda = -10H^2
$$

<!-- symbols: alphaL, wL, Hconst, ip, Lambda -->
<!-- begin generated symbol list -->
**Symbols in this equation.**

- $\alpha_{(p)}$: The Lovelock coupling of order $p$, $\alpha_{(p)} = w_{(p)}H^{2-2p}$ ($\alpha_{(1)} = 1$). Unit: $\mathrm{GeV}^{2-2p}$. Status: AUTHOR.
- $w_{(p)}$: The author's Lovelock weights, $w_{(1)} = 1$, $w_{(2)} = 1/32$, $w_{(3)} = 1/1152$. Unit: dimensionless. Value: $(1, 1/32, 1/1152)$. Status: AUTHOR.
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the Lovelock couplings, the cosmological constant $\Lambda = -10H^2$ and the mass parameter $m_\Psi = H$. Unit: GeV (1/length). Value: 14.296 TeV (from the fit of $m_{\mathrm{W}}$ and $\rho_{\mathrm{EW},0}$). Status: AUTHOR.
- $p$: The Lovelock order $p = 1, 2, 3$ (Einstein, Gauss-Bonnet, cubic). Status: STANDARD.
- $\Lambda$: The eight-dimensional cosmological constant, $\Lambda = -10H^2$. Unit: $\mathrm{GeV}^{2}$. Value: $-10H^2$. Status: AUTHOR.

<!-- end generated symbol list -->

which enter the action term IN-2 (section 6). With these couplings and the source of all matter, the notebook's equations
become the field equations of gravity of UM-2, with the Lovelock tensors written with the generalised Kronecker delta:

$$
\begin{aligned}
&\sum_{p=1}^{3}\alpha_{(p)}\,\mathcal{E}_{(p)}{}^M{}_N + \Lambda\,\delta^M_N = \kappa\,\mathcal{T}^M{}_N,\\
&\mathcal{E}_{(p)}{}^M{}_N = -\frac{1}{2^{p+1}}\,\delta^{MM_1N_1\cdots M_pN_p}_{NP_1Q_1\cdots P_pQ_p}\,
 R^{P_1Q_1}{}_{M_1N_1}\cdots R^{P_pQ_p}{}_{M_pN_p}
\end{aligned} \tag{FE-1}
$$

<!-- symbols: ip, alphaL, LovE, iM, iN, Lambda, delta, kappa, EMT, iP, iQ, Riemann -->
<!-- begin generated symbol list -->
**Symbols in (FE-1).**

- $p$: The Lovelock order $p = 1, 2, 3$ (Einstein, Gauss-Bonnet, cubic). Status: STANDARD.
- $\alpha_{(p)}$: The Lovelock coupling of order $p$, $\alpha_{(p)} = w_{(p)}H^{2-2p}$ ($\alpha_{(1)} = 1$). Unit: $\mathrm{GeV}^{2-2p}$. Status: AUTHOR.
- $\mathcal{E}_{(p)}{}^M{}_N$: The Lovelock tensor of order $p$, the metric variation of $\sqrt{\lvert g\rvert}\mathcal{L}_{(p)}$: $\mathcal{E}_{(1)}$ is the Einstein tensor $R^M{}_N - \frac12\delta^M_NR$; every $\mathcal{E}_{(p)}$ is divergence free. Unit: 1/$\mathrm{length}^{2p}$. Status: STANDARD.
- $M$: A coordinate index of eight dimensions (also with a numbered copy $M_1, M_2, \dots$): it runs over $x_0, x_1, \dots, x_7$; a repeated index is summed. Status: STANDARD.
- $N$: A coordinate index of eight dimensions (also $N_1, N_2, \dots$), running over $x_0, \dots, x_7$; a repeated index is summed. Status: STANDARD.
- $\Lambda$: The eight-dimensional cosmological constant, $\Lambda = -10H^2$. Unit: $\mathrm{GeV}^{2}$. Value: $-10H^2$. Status: AUTHOR.
- $\delta$: The Kronecker delta: with two indices $\delta^M_N = 1$ if $M = N$ and 0 otherwise (likewise $\delta_{\alpha e}$, $\delta_{l0}$, $\delta^{I3}$); with upper and lower index strings the generalised Kronecker delta $\delta^{M_1\cdots M_n}_{N_1\cdots N_n}$, the determinant of the $n \times n$ matrix of Kronecker deltas $\delta^{M_a}_{N_b}$ (+1 or -1 if the upper indices are an even or odd permutation of the lower ones, 0 otherwise). Status: STANDARD.
- $\kappa$: The eight-dimensional gravitational coupling, $\kappa = 8\pi G_8$. Unit: $\mathrm{GeV}^{-6}$. Value: $\kappa/V_\perp = 8\pi G_{\mathrm{N}}\mathcal{G}(K_*) = 2.328\times10^{-36}$ GeV$^{-2}$. Status: AUTHOR.
- $\mathcal{T}^M{}_N$: The energy-momentum tensor of all matter (every field except gravity, the stabiliser included), the source of gravity; defined by the change of the matter action under a change of the metric. Unit: $\mathrm{GeV}^{8}$. Status: STANDARD.
- $P$: A coordinate index of eight dimensions (also $P_1, P_2, \dots$), running over $x_0, \dots, x_7$; a repeated index is summed. Status: STANDARD.
- $Q$: A coordinate index of eight dimensions (also $Q_1, Q_2, \dots$), running over $x_0, \dots, x_7$; a repeated index is summed. Status: STANDARD.
- $R^{MN}{}_{PQ},\ R_{MN},\ R$: The curvature of the metric $g_{MN}$: with four indices the Riemann tensor, with two indices the Ricci tensor $R_{MN} = R^P{}_{MPN}$, without indices the Ricci (scalar) curvature $R = g^{MN}R_{MN}$; $R^{ab}{}_{ab}$ (no sum) is the sectional curvature of the coordinate plane $(a, b)$. Unit: 1/$\mathrm{length}^{2}$. Status: STANDARD.

<!-- end generated symbol list -->

That this normalisation reproduces the record's field equations (which were checked against the notebook) is verified
exactly by `um2_geometry.py` (checks `record_equation constraint_x4`, `record_equation space_x1_eq_x2_eq_x3`,
`record_equation hidden_and_extraTimes_x0_eq_x5_eq_x6_eq_x7`). UM-2 keeps the author's weights and $\Lambda$ unchanged; an
earlier model of this repository (UM-1) had changed $w_{(3)}$ and $\Lambda$.

## The gamma matrices of the Clifford algebra of signature (4, 4)

Both notebooks of the author named above build real $16\times16$ matrices in three steps. First, two real $4\times4$
matrices for each $h = 1, 2, 3$ (the notebook's arrays `s` and `t`, built as `Qa - Qb` and `Qa + Qb` from the Levi-Civita
array `Qa` and a second array `Qb` of Kronecker deltas):

$$
(\mathsf{s}_h)_{kq} = \epsilon_{\mathrm{LC}}^{hkq4} - \delta_{k4}\delta_{qh} + \delta_{kh}\delta_{q4},\qquad
(\mathsf{t}_h)_{kq} = \epsilon_{\mathrm{LC}}^{hkq4} + \delta_{k4}\delta_{qh} - \delta_{kh}\delta_{q4}
$$

<!-- symbols: mod_sh, mod_th, mod_ih, mod_ikq, mod_epsLC, delta -->
<!-- begin generated symbol list -->
**Symbols in this equation.**

- $\mathsf{s}_h$: The author's real antisymmetric $4\times4$ matrices $\mathsf{s}_h$ ($h = 1, 2, 3$; in the notebook $s_h = Q_a - Q_b$), the building blocks of the matrices $\mathsf{Z}_1$, $\mathsf{Z}_2$, $\mathsf{Z}_3$. Unit: dimensionless. Status: AUTHOR.
- $\mathsf{t}_h$: The author's real antisymmetric $4\times4$ matrices $\mathsf{t}_h$ ($h = 1, 2, 3$; in the notebook $t_h = Q_a + Q_b$), the building blocks of the matrices $\mathsf{Z}_6$, $\mathsf{Z}_5$, $\mathsf{Z}_4$. Unit: dimensionless. Status: AUTHOR.
- $h$: The label $h = 1, 2, 3$ of the author's real $4\times4$ matrices $\mathsf{s}_h$, $\mathsf{t}_h$ and of the $8\times8$ matrices $\mathsf{Z}_h$ and $\mathsf{Z}_{7-h}$ built from them. Status: AUTHOR.
- $k,\ q$: The row and column indices $k, q = 1, 2, 3, 4$ of the author's $4\times4$ matrices $\mathsf{s}_h$ and $\mathsf{t}_h$. Status: AUTHOR.
- $\epsilon_{\mathrm{LC}}^{hkq4}$: The Levi-Civita symbol of four indices: $+1$ if $(h, k, q, 4)$ is an even permutation of $(1, 2, 3, 4)$, $-1$ if it is an odd permutation, and 0 if two indices are equal. Unit: dimensionless. Status: STANDARD.
- $\delta$: The Kronecker delta: with two indices $\delta^M_N = 1$ if $M = N$ and 0 otherwise (likewise $\delta_{\alpha e}$, $\delta_{l0}$, $\delta^{I3}$); with upper and lower index strings the generalised Kronecker delta $\delta^{M_1\cdots M_n}_{N_1\cdots N_n}$, the determinant of the $n \times n$ matrix of Kronecker deltas $\delta^{M_a}_{N_b}$ (+1 or -1 if the upper indices are an even or odd permutation of the lower ones, 0 otherwise). Status: STANDARD.

<!-- end generated symbol list -->

Second, eight real $8\times8$ matrices and the matrix that pairs them (the notebook's arrays `zeta` and `tau`, which are
equal, and `sigma`; the identity $\mathbf{1}$ is $8\times8$ for $\mathsf{Z}_0$ and $4\times4$ inside $\mathsf{S}$):

$$
\mathsf{Z}_0 = \mathbf{1},\qquad
\mathsf{Z}_h = \begin{pmatrix}0 & \mathsf{s}_h\\ \mathsf{s}_h & 0\end{pmatrix},\qquad
\mathsf{Z}_{7-h} = \begin{pmatrix}0 & \mathsf{t}_h\\ -\mathsf{t}_h & 0\end{pmatrix},\qquad
\mathsf{Z}_7 = \mathsf{Z}_1\mathsf{Z}_2\mathsf{Z}_3\mathsf{Z}_4\mathsf{Z}_5\mathsf{Z}_6,\qquad
\mathsf{S} = \begin{pmatrix}0 & \mathbf{1}\\ \mathbf{1} & 0\end{pmatrix}
$$

<!-- symbols: mod_Za, identity, mod_ih, mod_sh, mod_th, mod_Ssf -->
<!-- begin generated symbol list -->
**Symbols in this equation.**

- $\mathsf{Z}_a$: The author's real $8\times8$ matrices $\mathsf{Z}_a$ ($a = 0, \dots, 7$; the notebook's $\zeta_A = \tau_A$): $\mathsf{Z}_0$ is the identity, $\mathsf{Z}_1, \mathsf{Z}_2, \mathsf{Z}_3$ and $\mathsf{Z}_6, \mathsf{Z}_5, \mathsf{Z}_4$ are built from $\mathsf{s}_h$ and $\mathsf{t}_h$, and $\mathsf{Z}_7 = \mathsf{Z}_1\cdots\mathsf{Z}_6$; they are the lower-left $8\times8$ blocks of the gamma matrices $\gamma^a$. Unit: dimensionless. Status: AUTHOR.
- $\mathbf{1}$: The identity matrix (of the size fixed by the context: 16 x 16 on spinors, 3 x 3 on the generations or flavours, 2 x 2 for the sigma field). Unit: dimensionless. Status: STANDARD.
- $h$: The label $h = 1, 2, 3$ of the author's real $4\times4$ matrices $\mathsf{s}_h$, $\mathsf{t}_h$ and of the $8\times8$ matrices $\mathsf{Z}_h$ and $\mathsf{Z}_{7-h}$ built from them. Status: AUTHOR.
- $\mathsf{s}_h$: The author's real antisymmetric $4\times4$ matrices $\mathsf{s}_h$ ($h = 1, 2, 3$; in the notebook $s_h = Q_a - Q_b$), the building blocks of the matrices $\mathsf{Z}_1$, $\mathsf{Z}_2$, $\mathsf{Z}_3$. Unit: dimensionless. Status: AUTHOR.
- $\mathsf{t}_h$: The author's real antisymmetric $4\times4$ matrices $\mathsf{t}_h$ ($h = 1, 2, 3$; in the notebook $t_h = Q_a + Q_b$), the building blocks of the matrices $\mathsf{Z}_6$, $\mathsf{Z}_5$, $\mathsf{Z}_4$. Unit: dimensionless. Status: AUTHOR.
- $\mathsf{S}$: The author's real $8\times8$ matrix with the $4\times4$ identity in its two off-diagonal blocks and zeros elsewhere (the notebook's $\sigma$); $\mathsf{S} = \mathsf{Z}_1\mathsf{Z}_2\mathsf{Z}_3 = \mathsf{Z}_4\mathsf{Z}_5\mathsf{Z}_6\mathsf{Z}_7$. Unit: dimensionless. Status: AUTHOR.

<!-- end generated symbol list -->

Third, the gamma matrices along the frame directions $a = 0, \dots, 7$ (the notebook's `T16`):

$$
\bar{\mathsf{Z}}_a = \mathsf{S}\,\mathsf{Z}_a^T\,\mathsf{S},\qquad
\gamma^a = \begin{pmatrix}0 & \bar{\mathsf{Z}}_a\\ \mathsf{Z}_a & 0\end{pmatrix}
$$

<!-- symbols: mod_Zbar, mod_Ssf, mod_Za, ia, transpose, gamma -->
<!-- begin generated symbol list -->
**Symbols in this equation.**

- $\bar{\mathsf{Z}}_a$: The partner matrices $\bar{\mathsf{Z}}_a = \mathsf{S}\,\mathsf{Z}_a^T\,\mathsf{S}$ of the author ($a = 0, \dots, 7$; the notebook's $\bar\tau_A$), the upper-right $8\times8$ blocks of the gamma matrices $\gamma^a$. Unit: dimensionless. Status: AUTHOR.
- $\mathsf{S}$: The author's real $8\times8$ matrix with the $4\times4$ identity in its two off-diagonal blocks and zeros elsewhere (the notebook's $\sigma$); $\mathsf{S} = \mathsf{Z}_1\mathsf{Z}_2\mathsf{Z}_3 = \mathsf{Z}_4\mathsf{Z}_5\mathsf{Z}_6\mathsf{Z}_7$. Unit: dimensionless. Status: AUTHOR.
- $\mathsf{Z}_a$: The author's real $8\times8$ matrices $\mathsf{Z}_a$ ($a = 0, \dots, 7$; the notebook's $\zeta_A = \tau_A$): $\mathsf{Z}_0$ is the identity, $\mathsf{Z}_1, \mathsf{Z}_2, \mathsf{Z}_3$ and $\mathsf{Z}_6, \mathsf{Z}_5, \mathsf{Z}_4$ are built from $\mathsf{s}_h$ and $\mathsf{t}_h$, and $\mathsf{Z}_7 = \mathsf{Z}_1\cdots\mathsf{Z}_6$; they are the lower-left $8\times8$ blocks of the gamma matrices $\gamma^a$. Unit: dimensionless. Status: AUTHOR.
- $a$: A frame (orthonormal) index running over $0, 1, \dots, 7$, aligned with $x_0, \dots, x_7$; raised and lowered with $\eta_{ab}$; a repeated index is summed (except in a sectional curvature $R^{ab}{}_{ab}$). Status: STANDARD.
- ${}^T$: The transpose: a row written with $^T$ is a column. Status: STANDARD.
- $\gamma^a,\ \gamma^M,\ \gamma^\mu$: The Dirac matrices: $\gamma^a$ with a frame index are the author's real $16 \times 16$ matrices of the Clifford algebra of signature $(4, 4)$; $\gamma^M = \mathbf{e}_a{}^M\gamma^a$ along a coordinate ($\gamma^{x_0}$, $\gamma^{x_4}$, ... the matrices along $x_0$, $x_4$, ...), $\gamma_M = g_{MN}\gamma^N$; $\gamma^\mu$ the matrices of the four observable directions in four-dimensional formulas. Unit: dimensionless. Status: AUTHOR.

<!-- end generated symbol list -->

They satisfy the Clifford algebra and the notebook identities (notebook Out[322] to Out[324]; the identity $\mathbf{1}$ is
$16\times16$ in the first relation and $8\times8$ in the second):

$$
\gamma^a\gamma^b + \gamma^b\gamma^a = 2\eta^{ab}\,\mathbf{1},\qquad
\tfrac12\big(\mathsf{Z}_a\bar{\mathsf{Z}}_b + \mathsf{Z}_b\bar{\mathsf{Z}}_a\big) = \eta_{ab}\,\mathbf{1},\qquad
\mathsf{S} = \mathsf{Z}_1\mathsf{Z}_2\mathsf{Z}_3 = \mathsf{Z}_4\mathsf{Z}_5\mathsf{Z}_6\mathsf{Z}_7
$$

<!-- symbols: gamma, ia, ib, eta, identity, mod_Za, mod_Zbar, mod_Ssf -->
<!-- begin generated symbol list -->
**Symbols in this equation.**

- $\gamma^a,\ \gamma^M,\ \gamma^\mu$: The Dirac matrices: $\gamma^a$ with a frame index are the author's real $16 \times 16$ matrices of the Clifford algebra of signature $(4, 4)$; $\gamma^M = \mathbf{e}_a{}^M\gamma^a$ along a coordinate ($\gamma^{x_0}$, $\gamma^{x_4}$, ... the matrices along $x_0$, $x_4$, ...), $\gamma_M = g_{MN}\gamma^N$; $\gamma^\mu$ the matrices of the four observable directions in four-dimensional formulas. Unit: dimensionless. Status: AUTHOR.
- $a$: A frame (orthonormal) index running over $0, 1, \dots, 7$, aligned with $x_0, \dots, x_7$; raised and lowered with $\eta_{ab}$; a repeated index is summed (except in a sectional curvature $R^{ab}{}_{ab}$). Status: STANDARD.
- $b$: A frame index running over $0, \dots, 7$ (as $a$). Status: STANDARD.
- $\eta_{ab}$: The flat metric of the frame, $\eta_{ab} = \mathrm{diag}(+1, +1, +1, +1, -1, -1, -1, -1)$ ($\eta^{ab}$ the same matrix). Unit: dimensionless. Status: AUTHOR.
- $\mathbf{1}$: The identity matrix (of the size fixed by the context: 16 x 16 on spinors, 3 x 3 on the generations or flavours, 2 x 2 for the sigma field). Unit: dimensionless. Status: STANDARD.
- $\mathsf{Z}_a$: The author's real $8\times8$ matrices $\mathsf{Z}_a$ ($a = 0, \dots, 7$; the notebook's $\zeta_A = \tau_A$): $\mathsf{Z}_0$ is the identity, $\mathsf{Z}_1, \mathsf{Z}_2, \mathsf{Z}_3$ and $\mathsf{Z}_6, \mathsf{Z}_5, \mathsf{Z}_4$ are built from $\mathsf{s}_h$ and $\mathsf{t}_h$, and $\mathsf{Z}_7 = \mathsf{Z}_1\cdots\mathsf{Z}_6$; they are the lower-left $8\times8$ blocks of the gamma matrices $\gamma^a$. Unit: dimensionless. Status: AUTHOR.
- $\bar{\mathsf{Z}}_a$: The partner matrices $\bar{\mathsf{Z}}_a = \mathsf{S}\,\mathsf{Z}_a^T\,\mathsf{S}$ of the author ($a = 0, \dots, 7$; the notebook's $\bar\tau_A$), the upper-right $8\times8$ blocks of the gamma matrices $\gamma^a$. Unit: dimensionless. Status: AUTHOR.
- $\mathsf{S}$: The author's real $8\times8$ matrix with the $4\times4$ identity in its two off-diagonal blocks and zeros elsewhere (the notebook's $\sigma$); $\mathsf{S} = \mathsf{Z}_1\mathsf{Z}_2\mathsf{Z}_3 = \mathsf{Z}_4\mathsf{Z}_5\mathsf{Z}_6\mathsf{Z}_7$. Unit: dimensionless. Status: AUTHOR.

<!-- end generated symbol list -->

The derived matrices that UM-2 uses (the matrix of the Dirac adjoint, the chirality of eight dimensions, the author's
operator that separates the two halves of dirac16complex, and the generators of frame rotations) are, with the author's
matrices,

$$
C = \gamma^{x_0}\gamma^{x_1}\gamma^{x_2}\gamma^{x_3} = \begin{pmatrix}-\mathsf{S} & 0\\ 0 & \mathsf{S}\end{pmatrix},\qquad
\Gamma_8 = \gamma^{x_0}\gamma^{x_1}\cdots\gamma^{x_7} = \begin{pmatrix}-\mathbf{1} & 0\\ 0 & \mathbf{1}\end{pmatrix},\qquad
\mathcal{B} = -\mathrm{i}C\gamma^{x_4},\qquad \mathcal{S}^{ab} = \tfrac14\big[\gamma^a, \gamma^b\big]
$$

<!-- symbols: Cmat, gamma, x0, x1, x2, x3, x7, mod_Ssf, mod_Gamma8, identity, calB, imag, x4, calS, ia, ib -->
<!-- begin generated symbol list -->
**Symbols in this equation.**

- $C$: The matrix of the Dirac adjoint, $C = \gamma^{x_0}\gamma^{x_1}\gamma^{x_2}\gamma^{x_3}$ ($\bar\Psi = \Psi^\dagger C$); in each block of the reduction $C = \varsigma_2\sigma_2$. Unit: dimensionless. Status: AUTHOR.
- $\gamma^a,\ \gamma^M,\ \gamma^\mu$: The Dirac matrices: $\gamma^a$ with a frame index are the author's real $16 \times 16$ matrices of the Clifford algebra of signature $(4, 4)$; $\gamma^M = \mathbf{e}_a{}^M\gamma^a$ along a coordinate ($\gamma^{x_0}$, $\gamma^{x_4}$, ... the matrices along $x_0$, $x_4$, ...), $\gamma_M = g_{MN}\gamma^N$; $\gamma^\mu$ the matrices of the four observable directions in four-dimensional formulas. Unit: dimensionless. Status: AUTHOR.
- $x_0$: The hidden space-like coordinate (listed first); the metric depends on it through $z = 6Hx_0$, periodically with the period $\pi/(6H)$. Unit: length. Status: AUTHOR.
- $x_1$: The first coordinate of ordinary 3-space. Unit: length. Status: AUTHOR.
- $x_2$: The second coordinate of ordinary 3-space. Unit: length. Status: AUTHOR.
- $x_3$: The third coordinate of ordinary 3-space (also the symmetry axis of the fast-flavour analysis). Unit: length. Status: AUTHOR.
- $x_7$: The third of the three extra time-like coordinates. Unit: length. Status: AUTHOR.
- $\mathsf{S}$: The author's real $8\times8$ matrix with the $4\times4$ identity in its two off-diagonal blocks and zeros elsewhere (the notebook's $\sigma$); $\mathsf{S} = \mathsf{Z}_1\mathsf{Z}_2\mathsf{Z}_3 = \mathsf{Z}_4\mathsf{Z}_5\mathsf{Z}_6\mathsf{Z}_7$. Unit: dimensionless. Status: AUTHOR.
- $\Gamma_8$: The chirality of eight dimensions, $\Gamma_8 = \gamma^{x_0}\gamma^{x_1}\cdots\gamma^{x_7}$, equal to $\mathrm{diag}(-\mathbf{1}, \mathbf{1})$ for the author's matrices; its eigenspaces (eigenvalues $-1$ and $+1$) are the two inequivalent 8-dimensional irreducible representations of Spin(4,4). Unit: dimensionless. Status: DERIVED.
- $\mathbf{1}$: The identity matrix (of the size fixed by the context: 16 x 16 on spinors, 3 x 3 on the generations or flavours, 2 x 2 for the sigma field). Unit: dimensionless. Status: STANDARD.
- $\mathcal{B}$: The author's operator $\mathcal{B} = -\mathrm{i}C\gamma^{x_4}$; its eigenvalues $\mp1$ define the halves $\Psi_A$ and $\Psi_B$, and it commutes with every interaction of the good sector. Unit: dimensionless. Status: AUTHOR.
- $\mathrm{i}$: The imaginary unit, $\mathrm{i}^2 = -1$. Unit: dimensionless. Status: STANDARD.
- $x_4$: The time; dots denote $\mathrm{d}/\mathrm{d}x_4$. Unit: length (= time, c = 1). Status: AUTHOR.
- $\mathcal{S}^{ab}$: The generators of frame rotations on spinors, $\mathcal{S}^{ab} = \frac14[\gamma^a, \gamma^b]$ (the commutator). Unit: dimensionless. Status: STANDARD.
- $a$: A frame (orthonormal) index running over $0, 1, \dots, 7$, aligned with $x_0, \dots, x_7$; raised and lowered with $\eta_{ab}$; a repeated index is summed (except in a sectional curvature $R^{ab}{}_{ab}$). Status: STANDARD.
- $b$: A frame index running over $0, \dots, 7$ (as $a$). Status: STANDARD.

<!-- end generated symbol list -->

All of these relations are verified exactly with the rebuilt matrices by `um2_algebra.py` (31 checks, among them
`tau_relations_of_the_notebook`, `notebook_identities_sigma`, `clifford_relations`, `identical_to_record_gammas`,
`C_is_sigma16`, `chirality_diag`); the matrices enter the action through IN-6 (section 6).

## The mass parameter, the $x_0$ mass idea and the dark-matter hypothesis

The mass of dirac16complex is written $m_\Psi = 3H\mathcal{M}$ in the author's notebooks (the action term IN-5). The orders
require every non-massless particle to get its mass from the dependence of its wave function on $x_0$, periodic with the
period $\pi/(6H)$, with the uncertainty relation of $x_0$ and its momentum as the physical reason, and state the hypothesis
that the quanta of dirac16complex represent dark matter (and ask for the validity of a dark-energy association to be
analysed).

# Ingredients from the Revision record (RECORD)

## The corrected primordial metric

The author's order of 2026-10-16: "a diagonal form for the metric of the primordial gravitational field is only
self-consistent if all off-diagonal terms of all source terms in the Einstein field equations ARE ZERO. This is not the
case here. I task you to: [1] find the simplest modification for the current metric of the primordial gravitational field
that is probably self-consistent with the Einstein field equations". The metric of 2026-10-14 (the notebook metric with
$b_4$) has an off-diagonal Lovelock component $\mathcal{E}_{(p)}{}^{x_4}{}_{x_0} \propto \cot z\,\dot b_4/b_4$ at every
Lovelock order $p$. The record examined the family of diagonal metrics with $g_{x_4x_4} = -1$ and

$$
\begin{aligned}
&g_{x_0x_0} = b_4^{2\mathfrak{p}}\,\mathrm{e}^{2\mathfrak{q}a_4}\cot^2z,\qquad
 g_{x_1x_1} = g_{x_2x_2} = g_{x_3x_3} = \mathrm{e}^{2a_4}(\sin^2z)^{3\mathfrak{a}},\\
&g_{x_5x_5} = g_{x_6x_6} = g_{x_7x_7} = -\mathrm{e}^{-2a_4}b_4\,(\sin^2z)^{3\mathfrak{b}}
\end{aligned}
$$

<!-- symbols: metric, x0, x1, x2, x3, x5, x6, x7, b4, prov_family, euler, a4, zvar -->
<!-- begin generated symbol list -->
**Symbols in this equation.**

- $g_{MN}$: The metric tensor of the eight-dimensional spacetime (signature $+,+,+,+,-,-,-,-$ in the order $x_0, \dots, x_7$): $g_{MN}\,\mathrm{d}X^M\mathrm{d}X^N$ is the squared interval; $g^{MN}$ is its inverse, $g^M{}_N = \delta^M_N$, and $\lvert g\rvert$ the absolute value of its determinant, so that $\sqrt{\lvert g\rvert}\,\mathrm{d}^8X$ is the proper volume element. Unit: dimensionless. Status: AUTHOR.
- $x_0$: The hidden space-like coordinate (listed first); the metric depends on it through $z = 6Hx_0$, periodically with the period $\pi/(6H)$. Unit: length. Status: AUTHOR.
- $x_1$: The first coordinate of ordinary 3-space. Unit: length. Status: AUTHOR.
- $x_2$: The second coordinate of ordinary 3-space. Unit: length. Status: AUTHOR.
- $x_3$: The third coordinate of ordinary 3-space (also the symmetry axis of the fast-flavour analysis). Unit: length. Status: AUTHOR.
- $x_5$: The first of the three extra time-like coordinates. Unit: length. Status: AUTHOR.
- $x_6$: The second of the three extra time-like coordinates. Unit: length. Status: AUTHOR.
- $x_7$: The third of the three extra time-like coordinates. Unit: length. Status: AUTHOR.
- $b_4$: The author's metric function of the time $x_4$ in the hidden and extra-time components, $b_4 > 0$. Unit: dimensionless. Status: AUTHOR.
- $\mathfrak{p},\ \mathfrak{q},\ \mathfrak{a},\ \mathfrak{b}$: The four exponents of the family of diagonal primordial metrics examined in the Revision record on 2026-10-16: $\mathfrak{p}$ and $\mathfrak{q}$ are the powers of $b_4$ and of $\mathrm{e}^{a_4}$ in the hidden component $g_{x_0x_0} = b_4^{2\mathfrak{p}}\mathrm{e}^{2\mathfrak{q}a_4}\cot^2z$, $\mathfrak{a}$ and $\mathfrak{b}$ the warp powers of ordinary 3-space and of the extra times, $(\sin^2z)^{3\mathfrak{a}}$ and $(\sin^2z)^{3\mathfrak{b}}$. The record's corrected metric has $\mathfrak{p} = \frac12$, $\mathfrak{q} = -1$, $\mathfrak{a} = 0$, $\mathfrak{b} = \frac16$. Unit: dimensionless. Value: $\mathfrak{p} = \frac12$, $\mathfrak{q} = -1$, $\mathfrak{a} = 0$, $\mathfrak{b} = \frac16$ for the metric used by UM-2. Status: RECORD.
- $\mathrm{e}$: Euler's number, the base of the natural logarithm; $\mathrm{e}^{X}$ is the exponential of $X$. Unit: dimensionless. Value: 2.718281828. Status: STANDARD.
- $a_4$: The author's metric function of the time $x_4$ that scales ordinary 3-space: the scale factor of cosmology is $\mathrm{e}^{a_4}$. Unit: dimensionless. Status: AUTHOR.
- $z$: The angle variable of the hidden direction, $z = 6Hx_0$; one period of $x_0$ is $0 < z < \pi$. Unit: dimensionless. Status: AUTHOR.

<!-- end generated symbol list -->

whose mixed curvature (3-space with the hidden direction, and the extra times with the hidden direction) vanishes for
every $a_4(x_4)$ and $b_4(x_4)$ only if

$$
\mathfrak{a}\Big((\mathfrak{q} - 1)\,\dot a_4 + \mathfrak{p}\,\frac{\dot b_4}{b_4}\Big) = 0,\qquad
\mathfrak{b}\Big((\mathfrak{q} + 1)\,\dot a_4 + \big(\mathfrak{p} - \tfrac12\big)\frac{\dot b_4}{b_4}\Big) = 0
$$

<!-- symbols: prov_family, a4dot, b4dot, b4 -->
<!-- begin generated symbol list -->
**Symbols in this equation.**

- $\mathfrak{p},\ \mathfrak{q},\ \mathfrak{a},\ \mathfrak{b}$: The four exponents of the family of diagonal primordial metrics examined in the Revision record on 2026-10-16: $\mathfrak{p}$ and $\mathfrak{q}$ are the powers of $b_4$ and of $\mathrm{e}^{a_4}$ in the hidden component $g_{x_0x_0} = b_4^{2\mathfrak{p}}\mathrm{e}^{2\mathfrak{q}a_4}\cot^2z$, $\mathfrak{a}$ and $\mathfrak{b}$ the warp powers of ordinary 3-space and of the extra times, $(\sin^2z)^{3\mathfrak{a}}$ and $(\sin^2z)^{3\mathfrak{b}}$. The record's corrected metric has $\mathfrak{p} = \frac12$, $\mathfrak{q} = -1$, $\mathfrak{a} = 0$, $\mathfrak{b} = \frac16$. Unit: dimensionless. Value: $\mathfrak{p} = \frac12$, $\mathfrak{q} = -1$, $\mathfrak{a} = 0$, $\mathfrak{b} = \frac16$ for the metric used by UM-2. Status: RECORD.
- $\dot a_4$: The time derivative $\mathrm{d}a_4/\mathrm{d}x_4$. Unit: GeV. Status: DERIVED.
- $\dot b_4$: The time derivative $\mathrm{d}b_4/\mathrm{d}x_4$. Unit: GeV. Status: DERIVED.
- $b_4$: The author's metric function of the time $x_4$ in the hidden and extra-time components, $b_4 > 0$. Unit: dimensionless. Status: AUTHOR.

<!-- end generated symbol list -->

Keeping the warp of the extra times ($\mathfrak{b} = 1/6$) forces $\mathfrak{a} = 0$, $\mathfrak{q} = -1$,
$\mathfrak{p} = 1/2$: the record's current metric, the order-0 metric of UM-2,

$$
\begin{aligned}
\bar g = \mathrm{diag}\Big(&\mathrm{e}^{-2a_4}b_4\cot^2z,\ \mathrm{e}^{2a_4},\ \mathrm{e}^{2a_4},\ 
 \mathrm{e}^{2a_4},\ -1,\\
&-\mathrm{e}^{-2a_4}b_4(\sin^2z)^{1/6},\ -\mathrm{e}^{-2a_4}b_4(\sin^2z)^{1/6},\ -\mathrm{e}^{-2a_4}b_4(
 \sin^2z)^{1/6}\Big),
 \qquad z = 6Hx_0
\end{aligned} \tag{FE-31}
$$

<!-- symbols: gbar, diag, euler, a4, b4, zvar, Hconst, x0 -->
<!-- begin generated symbol list -->
**Symbols in (FE-31).**

- $\bar g_{MN}$: The order-0 (background) metric of the power series: the corrected primordial metric in the author's coordinates, determined by the two functions $a_4(x_4)$ and $b_4(x_4)$; $\lvert\bar g\rvert$ is the absolute value of its determinant. Unit: dimensionless. Status: AUTHOR.
- $\mathrm{diag}$: A diagonal matrix with the listed entries on its diagonal (in the order of the coordinates $x_0, x_1, \dots, x_7$ when it is a tensor in eight dimensions). Status: STANDARD.
- $\mathrm{e}$: Euler's number, the base of the natural logarithm; $\mathrm{e}^{X}$ is the exponential of $X$. Unit: dimensionless. Value: 2.718281828. Status: STANDARD.
- $a_4$: The author's metric function of the time $x_4$ that scales ordinary 3-space: the scale factor of cosmology is $\mathrm{e}^{a_4}$. Unit: dimensionless. Status: AUTHOR.
- $b_4$: The author's metric function of the time $x_4$ in the hidden and extra-time components, $b_4 > 0$. Unit: dimensionless. Status: AUTHOR.
- $z$: The angle variable of the hidden direction, $z = 6Hx_0$; one period of $x_0$ is $0 < z < \pi$. Unit: dimensionless. Status: AUTHOR.
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the Lovelock couplings, the cosmological constant $\Lambda = -10H^2$ and the mass parameter $m_\Psi = H$. Unit: GeV (1/length). Value: 14.296 TeV (from the fit of $m_{\mathrm{W}}$ and $\rho_{\mathrm{EW},0}$). Status: AUTHOR.
- $x_0$: The hidden space-like coordinate (listed first); the metric depends on it through $z = 6Hx_0$, periodically with the period $\pi/(6H)$. Unit: length. Status: AUTHOR.

<!-- end generated symbol list -->

Every off-diagonal component of $\mathcal{E}_{(1)}$, $\mathcal{E}_{(2)}$, $\mathcal{E}_{(3)}$ vanishes identically for all
$a_4(x_4)$, $b_4(x_4) > 0$ and every real $z$ (record: sympy 14/14, Wolfram 13/13; re-derived in UM-2 by `um2_geometry.py`,
checks `y_chart_pair_diagonal`, `author_chart_pair_diagonal`, `charts_agree`). The alternative K of the record (hidden
component $\mathrm{e}^{2a_4}\cot^2z$, 3-space components $\mathrm{e}^{2a_4}(\sin^2z)^{1/6}$, extra-time components
$-\mathrm{e}^{-2a_4}b_4$) is also diagonal at every order; the record leaves the choice to the author, and UM-2 uses the
metric FE-31 (status AUTHOR in the inventory: the author's coordinates and functions, corrected by the record under his
order).

## The hidden coordinate, the fold and the regular tip

On every interval with $\sin z \ne 0$ the record introduces the hidden coordinate $y$ and the block scale $f$:

$$
\begin{aligned}
&y = \frac{\ln\lvert\sin z\rvert}{6H},\qquad \mathrm{d}y = \cot z\,\mathrm{d}x_0,\qquad \xi =
 \frac{y}{L}\in[-1, 0],\\
&\bar g_{MN}\,\mathrm{d}X^M\mathrm{d}X^N = \mathrm{e}^{2a_4}\big(\mathrm{d}x_1^2 + \mathrm{d}x_2^2 +
 \mathrm{d}x_3^2\big)
 - \mathrm{d}x_4^2 + f^2\Big[\mathrm{d}y^2 - \mathrm{e}^{2Hy}\big(\mathrm{d}x_5^2 + \mathrm{d}x_6^2 +
 \mathrm{d}x_7^2\big)\Big],\\
&f = \mathrm{e}^{-a_4}b_4^{1/2},\qquad K = \frac{1}{f^2},\qquad \mathcal{H} = \dot a_4,\qquad
 \mathcal{H}_f = \frac{\dot f}{f} = \frac{\dot b_4}{2b_4} - \dot a_4,\qquad \dot K = -2K\mathcal{H}_f,\\
&\sqrt{\lvert\bar g\rvert} = \mathrm{e}^{3a_4}f^4\lvert\cot z\rvert(\sin^2z)^{1/4}
 = \mathrm{e}^{3a_4}f^4\,\mathrm{e}^{3Hy}\Big\lvert\frac{\mathrm{d}y}{\mathrm{d}x_0}\Big\rvert
\end{aligned} \tag{FE-32}
$$

<!-- symbols: ycoord, zvar, Hconst, diff, x0, xi, Lcut, gbar, iM, iN, Xcoord, euler, a4, x1, x2, x3, x4, fblock, x5, x6, x7, b4, Kblock, Hubble, a4dot, Hf, fdot, b4dot, Kdot -->
<!-- begin generated symbol list -->
**Symbols in (FE-32).**

- $y$: The hidden coordinate of the $y$ chart, $y = \ln\lvert\sin z\rvert/(6H)$, with $y = 0$ at the fold ($z = \pi/2$) and $y = -L$ at the regular tip; each half of a period of $x_0$ is the interval $-L \le y \le 0$. Unit: length. Status: DERIVED.
- $z$: The angle variable of the hidden direction, $z = 6Hx_0$; one period of $x_0$ is $0 < z < \pi$. Unit: dimensionless. Status: AUTHOR.
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the Lovelock couplings, the cosmological constant $\Lambda = -10H^2$ and the mass parameter $m_\Psi = H$. Unit: GeV (1/length). Value: 14.296 TeV (from the fit of $m_{\mathrm{W}}$ and $\rho_{\mathrm{EW},0}$). Status: AUTHOR.
- $\mathrm{d}$: The differential: $\mathrm{d}X$ is an infinitesimal change of $X$, $\mathrm{d}X/\mathrm{d}Y$ the derivative of $X$ with respect to $Y$, $\mathrm{d}^nX$ the volume element of $n$ variables. Status: STANDARD.
- $x_0$: The hidden space-like coordinate (listed first); the metric depends on it through $z = 6Hx_0$, periodically with the period $\pi/(6H)$. Unit: length. Status: AUTHOR.
- $\xi$: The scaled hidden coordinate, $\xi = y/L$, running from $-1$ (tip) to $0$ (fold) on each half of a period. Unit: dimensionless. Status: DERIVED.
- $L$: The depth of the regular tip: each half of a period of $x_0$ ends at $y = -L$; $HL = 3$. Unit: length. Value: $L = 3/H$ ($fL = 8.926\times10^{-21}$ m at the stabilised block). Status: ASSUMED.
- $\bar g_{MN}$: The order-0 (background) metric of the power series: the corrected primordial metric in the author's coordinates, determined by the two functions $a_4(x_4)$ and $b_4(x_4)$; $\lvert\bar g\rvert$ is the absolute value of its determinant. Unit: dimensionless. Status: AUTHOR.
- $M$: A coordinate index of eight dimensions (also with a numbered copy $M_1, M_2, \dots$): it runs over $x_0, x_1, \dots, x_7$; a repeated index is summed. Status: STANDARD.
- $N$: A coordinate index of eight dimensions (also $N_1, N_2, \dots$), running over $x_0, \dots, x_7$; a repeated index is summed. Status: STANDARD.
- $X = \{x_0, \dots, x_7\}$: The author's coordinates of the eight-dimensional spacetime, $X = \{x_0, x_1, \dots, x_7\}$ with the hidden direction first; $X^M$ is the coordinate with the index $M$, $\mathrm{d}^8X = \mathrm{d}x_0\,\mathrm{d}x_1\cdots\mathrm{d}x_7$ the coordinate volume element and $X^\mu$ (four-dimensional index $\mu$) the observable coordinates $x_1, \dots, x_4$. Unit: length (each coordinate). Status: AUTHOR.
- $\mathrm{e}$: Euler's number, the base of the natural logarithm; $\mathrm{e}^{X}$ is the exponential of $X$. Unit: dimensionless. Value: 2.718281828. Status: STANDARD.
- $a_4$: The author's metric function of the time $x_4$ that scales ordinary 3-space: the scale factor of cosmology is $\mathrm{e}^{a_4}$. Unit: dimensionless. Status: AUTHOR.
- $x_1$: The first coordinate of ordinary 3-space. Unit: length. Status: AUTHOR.
- $x_2$: The second coordinate of ordinary 3-space. Unit: length. Status: AUTHOR.
- $x_3$: The third coordinate of ordinary 3-space (also the symmetry axis of the fast-flavour analysis). Unit: length. Status: AUTHOR.
- $x_4$: The time; dots denote $\mathrm{d}/\mathrm{d}x_4$. Unit: length (= time, c = 1). Status: AUTHOR.
- $f$: The block scale: the common scale factor of the hidden direction and the extra times, $f = \mathrm{e}^{-a_4}b_4^{1/2}$ (the block is $f^2$ times a four-dimensional space of constant curvature $-H^2$). Unit: dimensionless. Status: DERIVED.
- $x_5$: The first of the three extra time-like coordinates. Unit: length. Status: AUTHOR.
- $x_6$: The second of the three extra time-like coordinates. Unit: length. Status: AUTHOR.
- $x_7$: The third of the three extra time-like coordinates. Unit: length. Status: AUTHOR.
- $b_4$: The author's metric function of the time $x_4$ in the hidden and extra-time components, $b_4 > 0$. Unit: dimensionless. Status: AUTHOR.
- $K$: The block variable, $K = 1/f^2$. Unit: dimensionless. Status: DERIVED.
- $\mathcal{H}$: The expansion rate of ordinary 3-space, $\mathcal{H} = \dot a_4$ (the Hubble rate of the observer; in the hot Universe $\mathcal{H} = (8\pi^3g_\rho/90)^{1/2}T^2/M_{\mathrm{Pl}}$). Unit: GeV. Status: DERIVED.
- $\dot a_4$: The time derivative $\mathrm{d}a_4/\mathrm{d}x_4$. Unit: GeV. Status: DERIVED.
- $\mathcal{H}_f$: The expansion rate of the block, $\mathcal{H}_f = \dot f/f = \dot b_4/(2b_4) - \dot a_4$ (negative when the extra times and $x_0$ deflate). Unit: GeV. Status: DERIVED.
- $\dot f$: The time derivative $\mathrm{d}f/\mathrm{d}x_4$ of the block scale. Unit: GeV. Status: DERIVED.
- $\dot b_4$: The time derivative $\mathrm{d}b_4/\mathrm{d}x_4$. Unit: GeV. Status: DERIVED.
- $\dot K$: The time derivative $\mathrm{d}K/\mathrm{d}x_4$. Unit: GeV. Status: DERIVED.

<!-- end generated symbol list -->

The fold is $z = \pi/2$ ($y = 0$); the tips are $z \to 0^+$ and $z \to \pi^-$ ($y \to -\infty$). The record replaces each tip
by a regular cutoff at $y = -L$ with $HL = 3$, a chosen depth (the extended levels depend on it like those of a box of
proper length $fL$). UM-2 keeps $HL = 3$ (ASSUMED).

## The dirac16complex Lagrangian and the canonical spin connection

The specification of the record (under the author's orders) fixes the Dirac-type Lagrangian of dirac16complex with the
contact self-interaction and the canonical (vielbein-postulate, torsion-free) spin connection: the action term IN-5 with the
connection IN-7, written out in section 6. The record chose the Dirac-type form because the notebook's real Majorana-type
Lagrangian is a total derivative for anticommuting real fields (it has no field equations), and it uses the canonical
connection rather than the notebook's contraction of the mixed connection coefficients, which lacks a metric factor. The
field equation of the record is $\gamma^MD_M\Psi = (m_\Psi + \lambda\bar\Psi\Psi)\Psi$, the part of the dirac16complex field
equation FE-12 without the portals.

## Canonical quantisation and the Krein metric

With $x_4$ as the evolution time, the canonical anticommutator of $\Psi$ and $\Psi^\dagger$ on a slice $x_4 = $ const is the
matrix $\mathcal{B}$ times the Dirac delta function of the seven remaining coordinates divided by $\sqrt{\lvert g\rvert}$;
$\mathcal{B}$ has the eigenvalues $+1$ (8 times) and $-1$ (8 times), so the inner product is indefinite (a Krein space). The
record works in the good sector (no extra-time momentum), counts the positive-energy branch of every block as particles,
and evaluates the expectation values of bilinears with the Krein metric $\mathcal{B}$ inserted between the spinors of the
modes (`um2_algebra.py`, checks `B_hermitian_involution`, `B_signature_8_8`, `B_gamma4_gamma_a_hermitian`).

## The Kohn-Sham reduction

For the corrected metric the record reduces the 16-component field equation, in the eight blocks of the commuting
operators $\gamma^{x_0}\gamma^{x_1}\gamma^{x_4}$, $\gamma^{x_2}\gamma^{x_3}$, $\gamma^{x_5}\gamma^{x_6}$ (eigenvalues $\varsigma$,
$\mathrm{i}\varsigma_2$ and $\mathrm{i}\varsigma_3$, each sign $\pm1$), to $2\times2$ block Hamiltonians; UM-2 re-derived the
reduction exactly for all eight blocks and general $a_4$, $b_4$ (`um2_fields.py`, check `dirac_reduction_exact`;
`um2_algebra.py`, checks `block_basis_unitary` to `block_form B gamma^(x0) = j s2 sigma3`):

$$
\begin{aligned}
&\Psi = \mathrm{e}^{\mathrm{i}kx_1}\,\mathrm{e}^{-\frac32Hy}\,\mathrm{e}^{a_4/2}\,b_4^{-1}\,\mathcal{V}
 \chi(y, x_4):\\
&\gamma^MD_M\Psi - \big(M(y) - \mathrm{i}v(y)\gamma^{x_4}\big)\Psi
 = \mathrm{e}^{\mathrm{i}kx_1}\,\mathrm{e}^{-\frac32Hy}\,\mathrm{e}^{a_4/2}\,b_4^{-1}\,\gamma^{x_4}\mathcal{V}
 \big[\partial_{x_4}\chi + \mathrm{i}h\chi\big],\\
&h = \varsigma\Big[-\frac{\mathrm{i}}{f}\sigma_1\partial_y + M(y)\,\sigma_2 +
 \mathrm{e}^{-a_4}k\,\sigma_3\Big] + v(y),\qquad
 \mathrm{i}\,\partial_{x_4}\chi = h\chi;\\
&\text{in each block: }\gamma^{x_0} = \sigma_3,\qquad \mathcal{B} = \varsigma\varsigma_2,\qquad
 C = \varsigma_2\sigma_2,\qquad \Gamma_4 = -\varsigma\varsigma_2\sigma_3
\end{aligned} \tag{FE-56}
$$

<!-- symbols: Psi, euler, imag, kwave, x1, Hconst, ycoord, a4, b4, calV, chi, x4, gamma, iM, Dcov, Mfun, vpot, partial, hblock, varsigma, fblock, sigmaPauli, iy, x0, calB, varsigma2, Cmat, Gamma4 -->
<!-- begin generated symbol list -->
**Symbols in (FE-56).**

- $\Psi,\ \bar\Psi$: dirac16complex: the 16-component complex spinor field of eight dimensions of the record (the author's field), the source of the dark matter (its lowest odd level) and of the massless fold bands; $\bar\Psi = \Psi^\dagger C$ is its Dirac adjoint. Unit: $\mathrm{GeV}^{7/2}$. Status: RECORD.
- $\mathrm{e}$: Euler's number, the base of the natural logarithm; $\mathrm{e}^{X}$ is the exponential of $X$. Unit: dimensionless. Value: 2.718281828. Status: STANDARD.
- $\mathrm{i}$: The imaginary unit, $\mathrm{i}^2 = -1$. Unit: dimensionless. Status: STANDARD.
- $k$: The magnitude of the wave vector (the momentum, $\hbar = 1$) of a mode: in the reduction, the Kohn-Sham and the perturbation equations the comoving wavenumber (physical momentum $\mathrm{e}^{-a_4}k$); in the thermal integrals the momentum of a particle at the time considered (the variable of integration). Unit: GeV (1/length). Status: STANDARD.
- $x_1$: The first coordinate of ordinary 3-space. Unit: length. Status: AUTHOR.
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the Lovelock couplings, the cosmological constant $\Lambda = -10H^2$ and the mass parameter $m_\Psi = H$. Unit: GeV (1/length). Value: 14.296 TeV (from the fit of $m_{\mathrm{W}}$ and $\rho_{\mathrm{EW},0}$). Status: AUTHOR.
- $y$: The hidden coordinate of the $y$ chart, $y = \ln\lvert\sin z\rvert/(6H)$, with $y = 0$ at the fold ($z = \pi/2$) and $y = -L$ at the regular tip; each half of a period of $x_0$ is the interval $-L \le y \le 0$. Unit: length. Status: DERIVED.
- $a_4$: The author's metric function of the time $x_4$ that scales ordinary 3-space: the scale factor of cosmology is $\mathrm{e}^{a_4}$. Unit: dimensionless. Status: AUTHOR.
- $b_4$: The author's metric function of the time $x_4$ in the hidden and extra-time components, $b_4 > 0$. Unit: dimensionless. Status: AUTHOR.
- $\mathcal{V}$: The constant $16 \times 2$ matrix of the reduction ansatz that places the two-component spinor $\chi$ of one block into the 16 components of the eight-dimensional spinor. Unit: dimensionless. Status: DERIVED.
- $\chi,\ \chi_o,\ \chi_1,\ \chi_2$: The two-component spinor of one block of the reduction (a function of $y$ and $x_4$), $\chi = (\chi_1, \chi_2)^T = (a, \mathrm{i}b)^T$; $\chi_o$ the Kohn-Sham orbital $o$, normalised as $\int_{-L}^{0}\chi_o^\dagger\chi_o\,\mathrm{d}y = 1$. Unit: $\mathrm{GeV}^{1/2}$ (normalised orbital). Status: DERIVED.
- $x_4$: The time; dots denote $\mathrm{d}/\mathrm{d}x_4$. Unit: length (= time, c = 1). Status: AUTHOR.
- $\gamma^a,\ \gamma^M,\ \gamma^\mu$: The Dirac matrices: $\gamma^a$ with a frame index are the author's real $16 \times 16$ matrices of the Clifford algebra of signature $(4, 4)$; $\gamma^M = \mathbf{e}_a{}^M\gamma^a$ along a coordinate ($\gamma^{x_0}$, $\gamma^{x_4}$, ... the matrices along $x_0$, $x_4$, ...), $\gamma_M = g_{MN}\gamma^N$; $\gamma^\mu$ the matrices of the four observable directions in four-dimensional formulas. Unit: dimensionless. Status: AUTHOR.
- $M$: A coordinate index of eight dimensions (also with a numbered copy $M_1, M_2, \dots$): it runs over $x_0, x_1, \dots, x_7$; a repeated index is summed. Status: STANDARD.
- $D_M,\ D_\mu$: The covariant derivative: on a spinor $D_M = \partial_M + \Omega_M$ (spin connection), on a Standard-Model fermion with the gauge fields added; on the sigma field $D_\mu\Sigma$ with the $W$ and $B$ fields. Unit: 1/length. Status: STANDARD.
- $M(y)$: The mass function of the block Hamiltonian (the scalar potential): $M = \mu_{\psi i}$ for a Standard-Model fermion, $M = M_{\mathrm{eff}}$ for dirac16complex. Unit: GeV. Status: DERIVED.
- $v(y)$: The vector potential of the block Hamiltonian (the mean field along $\gamma^{x_4}$): for dirac16complex the contact term and the mean field of I11; zero for a Standard-Model fermion. Unit: GeV. Status: DERIVED.
- $\partial$: A partial derivative: $\partial_M$ is the derivative with respect to the coordinate $X^M$, $\partial_y$ with respect to $y$, $\partial_{x_4}$ with respect to the time $x_4$, $\partial X/\partial Y$ the derivative of $X$ with respect to $Y$ at fixed other variables. Status: STANDARD.
- $h$: The block Hamiltonian: the $2 \times 2$ differential operator of one block that generates the time evolution of $\chi$, $\mathrm{i}\,\partial_{x_4}\chi = h\chi$; its eigenvalues are the energies $\varepsilon$. Unit: GeV. Status: DERIVED.
- $\varsigma$: The first of the three signs $(\varsigma, \varsigma_2, \varsigma_3)$, each $\pm1$, that label the eight blocks of the reduction. Unit: dimensionless. Status: DERIVED.
- $f$: The block scale: the common scale factor of the hidden direction and the extra times, $f = \mathrm{e}^{-a_4}b_4^{1/2}$ (the block is $f^2$ times a four-dimensional space of constant curvature $-H^2$). Unit: dimensionless. Status: DERIVED.
- $\sigma_1,\ \sigma_2,\ \sigma_3$: The Pauli matrices acting on the two components of a block spinor $\chi$ ($\sigma_3 = \mathrm{diag}(1, -1)$). Unit: dimensionless. Status: STANDARD.
- $y$: The label $y$ in $\partial_y$: the derivative with respect to the hidden coordinate $y$. Status: STANDARD.
- $x_0$: The hidden space-like coordinate (listed first); the metric depends on it through $z = 6Hx_0$, periodically with the period $\pi/(6H)$. Unit: length. Status: AUTHOR.
- $\mathcal{B}$: The author's operator $\mathcal{B} = -\mathrm{i}C\gamma^{x_4}$; its eigenvalues $\mp1$ define the halves $\Psi_A$ and $\Psi_B$, and it commutes with every interaction of the good sector. Unit: dimensionless. Status: AUTHOR.
- $\varsigma_2$: The second sign that labels the blocks ($\pm1$). Unit: dimensionless. Status: DERIVED.
- $C$: The matrix of the Dirac adjoint, $C = \gamma^{x_0}\gamma^{x_1}\gamma^{x_2}\gamma^{x_3}$ ($\bar\Psi = \Psi^\dagger C$); in each block of the reduction $C = \varsigma_2\sigma_2$. Unit: dimensionless. Status: AUTHOR.
- $\Gamma_4$: The four-dimensional chirality matrix, $\Gamma_4 = \mathrm{i}\gamma^{x_1}\gamma^{x_2}\gamma^{x_3}\gamma^{x_4}$; a doublet zero mode has $\Gamma_4 = +1$ (left-handed), a singlet zero mode $\Gamma_4 = -1$ (right-handed). Unit: dimensionless. Status: DERIVED.

<!-- end generated symbol list -->

The record treats the contact interaction in the Hartree-plus-exchange (local) approximation; its mean fields are the
first terms of $M_{\mathrm{eff}}$ and $v$ in FE-64, to which UM-2 adds the mean fields of the portals I11, I12 and I13
(DERIVED):

$$
\begin{aligned}
&M_{\mathrm{eff}}(y) = m_\Psi + \frac{15}{16}\,\lambda\,n^{\mathrm{sc}}(y) +
 \frac{\langle\mathcal{F}\rangle}{\Lambda_\star^3},\qquad
 v(y) = -\frac{\lambda}{16}\,n(y) + \frac{c_{\mathrm{V}}}{\Lambda_\star^6}\sum_{i=1}^{3}\sum_\psi
 q_\psi\,n_{\psi i}(y),\\
&v_{\mathrm{b}}(y) = \frac{c_{\mathrm{A}}}{\Lambda_\star^6}\sum_{i=1}^{3}\sum_\psi q^{B}_\psi\,n_{\psi i}(y)
\end{aligned} \tag{FE-64}
$$

<!-- symbols: Meff, ycoord, mPsi, lambda, nsc, calF, LambdaStar, vpot, ndens, cV, ii, ipsi, qBL, vb, cA, qB -->
<!-- begin generated symbol list -->
**Symbols in (FE-64).**

- $M_{\mathrm{eff}}(y)$: The effective (scalar) mass field of the Kohn-Sham Hamiltonian: $m_\Psi$ plus the mean fields of the contact term and of I12. Unit: GeV. Status: DERIVED.
- $y$: The hidden coordinate of the $y$ chart, $y = \ln\lvert\sin z\rvert/(6H)$, with $y = 0$ at the fold ($z = \pi/2$) and $y = -L$ at the regular tip; each half of a period of $x_0$ is the interval $-L \le y \le 0$. Unit: length. Status: DERIVED.
- $m_\Psi$: The mass parameter of dirac16complex, $m_\Psi = 3H\mathcal{M} = H$. Unit: GeV. Value: 14.296 TeV. Status: RECORD.
- $\lambda$: The contact self-coupling of dirac16complex (the term $-\frac{\lambda}{2}(\bar\Psi\Psi)^2$ of the record). Unit: $\mathrm{GeV}^{-6}$. Value: not fixed; Kohn-Sham states computed for $\lambda = 0$ and $\pm7\times10^{-5}H^{-6}$; the fold-band radiation requires $\lvert\lambda\rvert \lesssim 1.4\times10^{-10}H^{-6}$ (for $\Delta N_{\mathrm{eff}} \le 0.001$). Status: RECORD.
- $n^{\mathrm{sc}},\ n^{\mathrm{sc}}_o$: The scalar density of dirac16complex (the Kohn-Sham expectation of $\bar\Psi\Psi$, per proper 7-volume) and $n^{\mathrm{sc}}_o$ the contribution of the orbital $o$. Unit: $\mathrm{GeV}^{7}$. Status: RECORD.
- $\mathcal{F}$: The gauge-kinetic operator of the portal I12, $\mathcal{F} = c_{\mathrm{G}}G^A_{MN}G^{AMN} + c_{\mathrm{W}}W^I_{MN}W^{IMN} + c_{\mathrm{B}}B_{MN}B^{MN}$; $\langle\mathcal{F}\rangle$ its mean value in an environment. Unit: $\mathrm{GeV}^{4}$. Status: INVENTED.
- $\Lambda_\star$: The scale of the portal operators I11, I12, I13. Unit: GeV. Value: only the combinations $c/\Lambda_\star^n$ enter. Status: INVENTED.
- $v(y)$: The vector potential of the block Hamiltonian (the mean field along $\gamma^{x_4}$): for dirac16complex the contact term and the mean field of I11; zero for a Standard-Model fermion. Unit: GeV. Status: DERIVED.
- $n,\ n_o,\ n_{\psi i},\ n_f,\ n_i$: A number density: $n(y)$ the particle density of dirac16complex in the Kohn-Sham equations and $n_o$ the contribution of the orbital $o$, $n_{\psi i}(y)$ the density of the Standard-Model fermion $\psi_i$ (per proper 7-volume of eight dimensions); $n_f$ the density of the fermion component $f$ and $n_i$ that of the neutrino mass state $i$ (per 3-volume of four dimensions). Unit: $\mathrm{GeV}^{7}$ (eight dimensions), $\mathrm{GeV}^{3}$ (four dimensions). Status: STANDARD.
- $c_{\mathrm{V}}$: The coefficient of the vector portal I11. Unit: dimensionless. Value: benchmark through $G_{\mathrm{V}} = 4.38\times10^{-17}$ GeV$^{-2}$. Status: INVENTED.
- $i$: The generation index ($i = 1, 2, 3$), which also labels the neutrino mass states $\nu_1, \nu_2, \nu_3$; a repeated index is not summed unless a sum sign is written. Status: STANDARD.
- $\psi$: The label of a Standard-Model multiplet: $\psi \in \{Q, u_R, d_R, \ell, e_R, \nu_R\}$ (quark doublet, up and down quark singlets, lepton doublet, charged-lepton singlet, right-handed neutrino); a sum over $\psi$ runs over the six. Status: STANDARD.
- $q_\psi,\ q_f$: The $B - L$ charge: $q_\psi$ of the multiplet $\psi$ ($q_Q = q_{u_R} = q_{d_R} = \frac13$, $q_\ell = q_{e_R} = q_{\nu_R} = -1$), $q_f$ of the fermion component $f$. Unit: dimensionless. Status: STANDARD.
- $v_{\mathrm{b}}(y)$: The mean field of I13 (baryon densities), acting on the lower component of $\chi$ only. Unit: GeV. Status: DERIVED.
- $c_{\mathrm{A}}$: The coefficient of the $x_0$-chiral vector portal I13. Unit: dimensionless. Value: fixed through $G_{\mathrm{A}} = 1.278\times10^{-9}$ GeV$^{-2}$ (dark-matter relic). Status: INVENTED.
- $q^B_\psi,\ q^B_f$: The baryon number of the multiplet $\psi$ or of the fermion component $f$ ($\frac13$ for quarks, 0 for leptons). Unit: dimensionless. Status: STANDARD.

<!-- end generated symbol list -->

The densities, the momentum shells, the normalisation volume of a cell and the occupations, and the Kohn-Sham energy, are
the record's (both parities at the fold are filled, each with the weight $\frac12$; the record's mass is $m_\Psi = 3H\mathcal{M}$
with $\mathcal{M} = 1/3$, i.e. $m_\Psi = H$, which UM-2 keeps, ASSUMED):

$$
\begin{aligned}
&n = \sum_o\tfrac12\,d_o\,\phi_o\,n_o,\qquad n^{\mathrm{sc}} =
 \sum_o\tfrac12\,d_o\,\phi_o\,n^{\mathrm{sc}}_o,\qquad
 n_o = \frac{\mathrm{e}^{-3Hy}}{\mathrm{Vol}_7}\,\chi_o^\dagger\chi_o,\\
&n^{\mathrm{sc}}_o = \frac{\mathrm{e}^{-3Hy}}{\mathrm{Vol}_7}\,\chi_o^\dagger\varsigma\sigma_2\chi_o,\qquad
 n^{\mathrm{t}}_o = \frac{\mathrm{e}^{-3Hy}}{\mathrm{Vol}_7}\,\chi_o^\dagger\varsigma\sigma_3\chi_o,\qquad
 d_o = 4\,r_3\big(\lvert\vec n_o\rvert^2\big),\qquad \vec k_o = k_{\mathrm{lat}}\,\vec n_o,\\
&\mathrm{Vol}_7 = \Big(\frac{2\pi}{k_{\mathrm{lat}}}\Big)^3v_{\mathrm{t}}\,f^4,\qquad
 \phi_o = \frac{1}{\mathrm{e}^{(\varepsilon_o - \mu_{\mathrm{chem}})/T} + 1}\ \ \text{(Mermin; or 0 and
 1 for the aufbau)}
\end{aligned} \tag{FE-65}
$$

<!-- symbols: ndens, io, ddeg, phiocc, nsc, euler, Hconst, ycoord, Vol7, chi, dagger, varsigma, sigmaPauli, nt, r3, nvec, kvec, klat, pi, vt, fblock, varepsilon, muchem, Temp -->
<!-- begin generated symbol list -->
**Symbols in (FE-65).**

- $n,\ n_o,\ n_{\psi i},\ n_f,\ n_i$: A number density: $n(y)$ the particle density of dirac16complex in the Kohn-Sham equations and $n_o$ the contribution of the orbital $o$, $n_{\psi i}(y)$ the density of the Standard-Model fermion $\psi_i$ (per proper 7-volume of eight dimensions); $n_f$ the density of the fermion component $f$ and $n_i$ that of the neutrino mass state $i$ (per 3-volume of four dimensions). Unit: $\mathrm{GeV}^{7}$ (eight dimensions), $\mathrm{GeV}^{3}$ (four dimensions). Status: STANDARD.
- $o$: The label of a Kohn-Sham orbital (a state of dirac16complex in the cell: block, momentum shell, fold parity and level); a sum over $o$ runs over the orbitals. Status: RECORD.
- $d_o,\ d_s$: A degeneracy: $d_o = 4r_3(\lvert\vec n_o\rvert^2)$ the number of states of the momentum shell of the orbital $o$; $d_s$ the number of internal states (spin, colour, particle and antiparticle) of the species $s$. Unit: dimensionless. Status: STANDARD.
- $\phi_o$: The occupation of the Kohn-Sham orbital $o$ (Fermi-Dirac for the Mermin functional, 0 or 1 for the aufbau). Unit: dimensionless. Status: RECORD.
- $n^{\mathrm{sc}},\ n^{\mathrm{sc}}_o$: The scalar density of dirac16complex (the Kohn-Sham expectation of $\bar\Psi\Psi$, per proper 7-volume) and $n^{\mathrm{sc}}_o$ the contribution of the orbital $o$. Unit: $\mathrm{GeV}^{7}$. Status: RECORD.
- $\mathrm{e}$: Euler's number, the base of the natural logarithm; $\mathrm{e}^{X}$ is the exponential of $X$. Unit: dimensionless. Value: 2.718281828. Status: STANDARD.
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the Lovelock couplings, the cosmological constant $\Lambda = -10H^2$ and the mass parameter $m_\Psi = H$. Unit: GeV (1/length). Value: 14.296 TeV (from the fit of $m_{\mathrm{W}}$ and $\rho_{\mathrm{EW},0}$). Status: AUTHOR.
- $y$: The hidden coordinate of the $y$ chart, $y = \ln\lvert\sin z\rvert/(6H)$, with $y = 0$ at the fold ($z = \pi/2$) and $y = -L$ at the regular tip; each half of a period of $x_0$ is the interval $-L \le y \le 0$. Unit: length. Status: DERIVED.
- $\mathrm{Vol}_7$: The normalisation volume of a Kohn-Sham cell, $\mathrm{Vol}_7 = (2\pi/k_{\mathrm{lat}})^3v_{\mathrm{t}}f^4$ (the proper seven-volume of a cell is $2\,\mathrm{Vol}_7(1 - \mathrm{e}^{-3HL})/(3H)$). Unit: $\mathrm{GeV}^{-6}$. Value: 34.27 in units $H = 1$, $v_{\mathrm{t}} = 1$, $f = f_*$. Status: RECORD.
- $\chi,\ \chi_o,\ \chi_1,\ \chi_2$: The two-component spinor of one block of the reduction (a function of $y$ and $x_4$), $\chi = (\chi_1, \chi_2)^T = (a, \mathrm{i}b)^T$; $\chi_o$ the Kohn-Sham orbital $o$, normalised as $\int_{-L}^{0}\chi_o^\dagger\chi_o\,\mathrm{d}y = 1$. Unit: $\mathrm{GeV}^{1/2}$ (normalised orbital). Status: DERIVED.
- ${}^\dagger$: Hermitian conjugation: the complex conjugate of the transpose of a matrix or spinor (for field operators the adjoint operator). Status: STANDARD.
- $\varsigma$: The first of the three signs $(\varsigma, \varsigma_2, \varsigma_3)$, each $\pm1$, that label the eight blocks of the reduction. Unit: dimensionless. Status: DERIVED.
- $\sigma_1,\ \sigma_2,\ \sigma_3$: The Pauli matrices acting on the two components of a block spinor $\chi$ ($\sigma_3 = \mathrm{diag}(1, -1)$). Unit: dimensionless. Status: STANDARD.
- $n^{\mathrm{t}}_o$: The density of the orbital $o$ along the momentum term ($\chi_o^\dagger\varsigma\sigma_3\chi_o$ times the weight $\mathrm{e}^{-3Hy}/\mathrm{Vol}_7$); it carries the 3-space pressure. Unit: $\mathrm{GeV}^{7}$. Status: RECORD.
- $r_3$: The number of representations of an integer as an ordered sum of three squares of integers (signs counted). Unit: dimensionless. Status: STANDARD.
- $\vec n_o$: The integer lattice vector of the momentum shell of the orbital $o$ ($\vec n \in \mathbb{Z}^3$). Unit: dimensionless. Status: RECORD.
- $\vec k,\ \vec k_o$: The wave vector (momentum) in ordinary 3-space; $\vec k_o$ that of the orbital $o$, a point of the lattice $k_{\mathrm{lat}}\vec n_o$. Unit: GeV. Status: STANDARD.
- $k_{\mathrm{lat}}$: The spacing of the momentum lattice of the Kohn-Sham cell. Unit: GeV. Value: $0.25\,H$. Status: RECORD.
- $\pi$: The number pi, the ratio of the circumference of a circle to its diameter. Unit: dimensionless. Value: 3.141592654. Status: STANDARD.
- $v_{\mathrm{t}}$: The coordinate volume of the compact extra times $x_5, x_6, x_7$. Unit: $\mathrm{GeV}^{-3}$. Value: not fixed; $v_{\mathrm{t}} = H^{-3}$ in the quoted conversions. Status: ASSUMED.
- $f$: The block scale: the common scale factor of the hidden direction and the extra times, $f = \mathrm{e}^{-a_4}b_4^{1/2}$ (the block is $f^2$ times a four-dimensional space of constant curvature $-H^2$). Unit: dimensionless. Status: DERIVED.
- $\varepsilon,\ \varepsilon_o$: The energy of a fermion mode (an eigenvalue of the block Hamiltonian; at $k = 0$ the four-dimensional mass); $\varepsilon_o$ the Kohn-Sham level of the orbital $o$. Unit: GeV. Status: DERIVED.
- $\mu_{\mathrm{chem}}$: The chemical potential of the Mermin occupations. Unit: GeV. Status: RECORD.
- $T$: The temperature of the plasma (of the photons and of every species in equilibrium with them); in the Mermin occupations the temperature of the Kohn-Sham state. Unit: GeV. Status: STANDARD.

<!-- end generated symbol list -->

$$
E_{\mathrm{KS}} = \sum_o d_o\,\phi_o\,\varepsilon_o -
 2\,\mathrm{Vol}_7\int_{-L}^{0}\mathrm{e}^{3Hy}\,e_{\mathrm{int}}\,\mathrm{d}y,
\qquad e_{\mathrm{int}} = \frac{15}{32}\,\lambda\,\big(n^{\mathrm{sc}}\big)^2 -
 \frac{1}{32}\,\lambda\,n^2 \tag{FE-66}
$$

<!-- symbols: EKS, io, ddeg, phiocc, varepsilon, Vol7, Lcut, euler, Hconst, ycoord, eint, diff, lambda, nsc, ndens -->
<!-- begin generated symbol list -->
**Symbols in (FE-66).**

- $E_{\mathrm{KS}}$: The Kohn-Sham energy of a cell. Unit: GeV. Status: RECORD.
- $o$: The label of a Kohn-Sham orbital (a state of dirac16complex in the cell: block, momentum shell, fold parity and level); a sum over $o$ runs over the orbitals. Status: RECORD.
- $d_o,\ d_s$: A degeneracy: $d_o = 4r_3(\lvert\vec n_o\rvert^2)$ the number of states of the momentum shell of the orbital $o$; $d_s$ the number of internal states (spin, colour, particle and antiparticle) of the species $s$. Unit: dimensionless. Status: STANDARD.
- $\phi_o$: The occupation of the Kohn-Sham orbital $o$ (Fermi-Dirac for the Mermin functional, 0 or 1 for the aufbau). Unit: dimensionless. Status: RECORD.
- $\varepsilon,\ \varepsilon_o$: The energy of a fermion mode (an eigenvalue of the block Hamiltonian; at $k = 0$ the four-dimensional mass); $\varepsilon_o$ the Kohn-Sham level of the orbital $o$. Unit: GeV. Status: DERIVED.
- $\mathrm{Vol}_7$: The normalisation volume of a Kohn-Sham cell, $\mathrm{Vol}_7 = (2\pi/k_{\mathrm{lat}})^3v_{\mathrm{t}}f^4$ (the proper seven-volume of a cell is $2\,\mathrm{Vol}_7(1 - \mathrm{e}^{-3HL})/(3H)$). Unit: $\mathrm{GeV}^{-6}$. Value: 34.27 in units $H = 1$, $v_{\mathrm{t}} = 1$, $f = f_*$. Status: RECORD.
- $L$: The depth of the regular tip: each half of a period of $x_0$ ends at $y = -L$; $HL = 3$. Unit: length. Value: $L = 3/H$ ($fL = 8.926\times10^{-21}$ m at the stabilised block). Status: ASSUMED.
- $\mathrm{e}$: Euler's number, the base of the natural logarithm; $\mathrm{e}^{X}$ is the exponential of $X$. Unit: dimensionless. Value: 2.718281828. Status: STANDARD.
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the Lovelock couplings, the cosmological constant $\Lambda = -10H^2$ and the mass parameter $m_\Psi = H$. Unit: GeV (1/length). Value: 14.296 TeV (from the fit of $m_{\mathrm{W}}$ and $\rho_{\mathrm{EW},0}$). Status: AUTHOR.
- $y$: The hidden coordinate of the $y$ chart, $y = \ln\lvert\sin z\rvert/(6H)$, with $y = 0$ at the fold ($z = \pi/2$) and $y = -L$ at the regular tip; each half of a period of $x_0$ is the interval $-L \le y \le 0$. Unit: length. Status: DERIVED.
- $e_{\mathrm{int}}$: The interaction energy density of the contact term in the Kohn-Sham energy and energy-momentum tensor. Unit: $\mathrm{GeV}^{8}$. Status: RECORD.
- $\mathrm{d}$: The differential: $\mathrm{d}X$ is an infinitesimal change of $X$, $\mathrm{d}X/\mathrm{d}Y$ the derivative of $X$ with respect to $Y$, $\mathrm{d}^nX$ the volume element of $n$ variables. Status: STANDARD.
- $\lambda$: The contact self-coupling of dirac16complex (the term $-\frac{\lambda}{2}(\bar\Psi\Psi)^2$ of the record). Unit: $\mathrm{GeV}^{-6}$. Value: not fixed; Kohn-Sham states computed for $\lambda = 0$ and $\pm7\times10^{-5}H^{-6}$; the fold-band radiation requires $\lvert\lambda\rvert \lesssim 1.4\times10^{-10}H^{-6}$ (for $\Delta N_{\mathrm{eff}} \le 0.001$). Status: RECORD.
- $n^{\mathrm{sc}},\ n^{\mathrm{sc}}_o$: The scalar density of dirac16complex (the Kohn-Sham expectation of $\bar\Psi\Psi$, per proper 7-volume) and $n^{\mathrm{sc}}_o$ the contribution of the orbital $o$. Unit: $\mathrm{GeV}^{7}$. Status: RECORD.
- $n,\ n_o,\ n_{\psi i},\ n_f,\ n_i$: A number density: $n(y)$ the particle density of dirac16complex in the Kohn-Sham equations and $n_o$ the contribution of the orbital $o$, $n_{\psi i}(y)$ the density of the Standard-Model fermion $\psi_i$ (per proper 7-volume of eight dimensions); $n_f$ the density of the fermion component $f$ and $n_i$ that of the neutrino mass state $i$ (per 3-volume of four dimensions). Unit: $\mathrm{GeV}^{7}$ (eight dimensions), $\mathrm{GeV}^{3}$ (four dimensions). Status: STANDARD.

<!-- end generated symbol list -->

Two reference states of the record (at $f = 1$, $a_4 = 0$: 8 particles in a cell with $\lambda = 157.7\,H^{-6}$, and 592
particles with $\lambda = 2.131\,H^{-6}$) serve as validation targets of the independent UM-2 solver: both are reproduced to
$10^{-13}$ in the energy, the highest occupied and the lowest unoccupied level and to $10^{-9}$ in the integrated hidden
pressure (`um2_ks_jobs.py validate`, checks `validate_N8_lamp1_a00`, `validate_N592_lamp1_a00`). The proper seven-volume of
a cell is $2\,\mathrm{Vol}_7(1 - \mathrm{e}^{-3HL})/(3H)$.

## Earlier work used only for comparison

The first universe model of this repository (UM-1, folder `Revision/universe_model`) is not an input of UM-2. UM-2 differs
from it in keeping the author's weights and $\Lambda$, in the electroweak sector, in the number of generations and in the
dark-matter candidate. Version 1 of UM-2 (2026-10-17, one generation) is superseded; its differences are item 21 of the
corrections.

# The action of UM-2 term by term, and the origin of each interaction

The action of UM-2 consists of the 18 interaction terms IN-1 to IN-18 below, each written out with its symbols and
followed by its origin. Varying the action with respect to every field gives the field equations FE-1 to FE-30; the other
field equations are their exact reductions on the static block and the equations of the four-dimensional effective theory
(section 8). The terms labelled INVENTED are the new phenomenological interactions that the author's orders require; for
each the reason for its form and its consistency with QCD and the electroweak model are stated.

## IN-1: the action

$$
\begin{aligned}
S ={}& S_{\mathrm{EL}} + S_{\mathrm{stab}} + S_\Psi + S_{\mathrm{gauge}} + S_{\mathrm{f}} + S_{\mathrm{tip}}
 + S_{\mathrm{I11}} + S_{\mathrm{I12}} + S_{\mathrm{I13}}
\end{aligned} \tag{IN-1}
$$

<!-- symbols: Saction, SEL, Sstab, SPsi, Sgauge, Sf, Stip, SI11, SI12, SI13 -->
<!-- begin generated symbol list -->
**Symbols in (IN-1).**

- $S$: The action of UM-2 (the integral of the Lagrangian density over spacetime); its variation with respect to every field gives the field equations. Unit: dimensionless ($\hbar = 1$). Status: ASSUMED.
- $S_{\mathrm{EL}}$: The Einstein-Lovelock action of gravity. Unit: dimensionless. Status: AUTHOR.
- $S_{\mathrm{stab}}$: The action of the block stabiliser (a vacuum energy of the block). Unit: dimensionless. Status: ASSUMED.
- $S_\Psi$: The action of the dirac16complex field (kinetic term with the canonical spin connection, mass term and contact self-interaction). Unit: dimensionless. Status: RECORD.
- $S_{\mathrm{gauge}}$: The action of the gauge fields of SU(3), SU(2) and U(1)$_Y$ in eight dimensions. Unit: dimensionless. Status: ASSUMED.
- $S_{\mathrm{f}}$: The action of the Standard-Model fermions of three generations (kinetic and bulk-mass terms). Unit: dimensionless. Status: ASSUMED.
- $S_{\mathrm{tip}}$: The action on the tip $y = -L$: the sigma field and the tip Yukawa couplings. Unit: dimensionless. Status: INVENTED.
- $S_{\mathrm{I11}}$: The action of the portal I11 (dirac16complex vector current times the $B - L$ current of the fermions). Unit: dimensionless. Status: INVENTED.
- $S_{\mathrm{I12}}$: The action of the portal I12 (scalar density of dirac16complex times the gauge kinetic invariants). Unit: dimensionless. Status: INVENTED.
- $S_{\mathrm{I13}}$: The action of the portal I13 (the $x_0$-chiral vector current of dirac16complex times the baryon-number current). Unit: dimensionless. Status: INVENTED.

<!-- end generated symbol list -->

**Origin (ASSUMED).** The choice of the terms is the model: the author's gravity (IN-2, IN-3); a stabiliser of the block
(IN-4); the record's dirac16complex field with its gamma matrices and its coupling to gravity (IN-5 to IN-7); the gauge
fields and the three generations of the Standard Model in eight dimensions (IN-8 to IN-12); the tip sigma field in place of
a Higgs field (IN-13 to IN-15); and three portals between dirac16complex and the Standard Model (IN-16 to IN-18). There is no
Higgs field: the orders exclude the Higgs particle. The chiral tip $Z$ portal I9 of version 1 is no longer part of the action
(its coefficients are zero; the end of this section).

## IN-2: Einstein-Lovelock gravity with the author's weights

$$
\begin{aligned}
S_{\mathrm{EL}} &= \frac{1}{2\kappa}\int\mathrm{d}^8X\,\sqrt{\lvert g\rvert}\,
 \Big(\sum_{p=1}^{3}\alpha_{(p)}\,\mathcal{L}_{(p)} - 2\Lambda\Big),\qquad \kappa = 8\pi G_8,\\
\alpha_{(p)} &= w_{(p)}\,H^{2-2p},\qquad w_{(1)} = 1,\quad w_{(2)} = \frac{1}{32},\quad w_{(3)} =
 \frac{1}{1152},
 \qquad \Lambda = -10H^2
\end{aligned} \tag{IN-2}
$$

<!-- symbols: SEL, kappa, diff, Xcoord, metric, ip, alphaL, Lov, Lambda, pi, G8, wL, Hconst -->
<!-- begin generated symbol list -->
**Symbols in (IN-2).**

- $S_{\mathrm{EL}}$: The Einstein-Lovelock action of gravity. Unit: dimensionless. Status: AUTHOR.
- $\kappa$: The eight-dimensional gravitational coupling, $\kappa = 8\pi G_8$. Unit: $\mathrm{GeV}^{-6}$. Value: $\kappa/V_\perp = 8\pi G_{\mathrm{N}}\mathcal{G}(K_*) = 2.328\times10^{-36}$ GeV$^{-2}$. Status: AUTHOR.
- $\mathrm{d}$: The differential: $\mathrm{d}X$ is an infinitesimal change of $X$, $\mathrm{d}X/\mathrm{d}Y$ the derivative of $X$ with respect to $Y$, $\mathrm{d}^nX$ the volume element of $n$ variables. Status: STANDARD.
- $X = \{x_0, \dots, x_7\}$: The author's coordinates of the eight-dimensional spacetime, $X = \{x_0, x_1, \dots, x_7\}$ with the hidden direction first; $X^M$ is the coordinate with the index $M$, $\mathrm{d}^8X = \mathrm{d}x_0\,\mathrm{d}x_1\cdots\mathrm{d}x_7$ the coordinate volume element and $X^\mu$ (four-dimensional index $\mu$) the observable coordinates $x_1, \dots, x_4$. Unit: length (each coordinate). Status: AUTHOR.
- $g_{MN}$: The metric tensor of the eight-dimensional spacetime (signature $+,+,+,+,-,-,-,-$ in the order $x_0, \dots, x_7$): $g_{MN}\,\mathrm{d}X^M\mathrm{d}X^N$ is the squared interval; $g^{MN}$ is its inverse, $g^M{}_N = \delta^M_N$, and $\lvert g\rvert$ the absolute value of its determinant, so that $\sqrt{\lvert g\rvert}\,\mathrm{d}^8X$ is the proper volume element. Unit: dimensionless. Status: AUTHOR.
- $p$: The Lovelock order $p = 1, 2, 3$ (Einstein, Gauss-Bonnet, cubic). Status: STANDARD.
- $\alpha_{(p)}$: The Lovelock coupling of order $p$, $\alpha_{(p)} = w_{(p)}H^{2-2p}$ ($\alpha_{(1)} = 1$). Unit: $\mathrm{GeV}^{2-2p}$. Status: AUTHOR.
- $\mathcal{L}_{(p)}$: The Lovelock density of order $p$ of the metric (a scalar built from $p$ Riemann tensors): $\mathcal{L}_{(1)} = R$ (Einstein-Hilbert), $\mathcal{L}_{(2)}$ the Gauss-Bonnet density, $\mathcal{L}_{(3)}$ the cubic Lovelock density. Unit: 1/$\mathrm{length}^{2p}$. Status: STANDARD.
- $\Lambda$: The eight-dimensional cosmological constant, $\Lambda = -10H^2$. Unit: $\mathrm{GeV}^{2}$. Value: $-10H^2$. Status: AUTHOR.
- $\pi$: The number pi, the ratio of the circumference of a circle to its diameter. Unit: dimensionless. Value: 3.141592654. Status: STANDARD.
- $G_8$: The eight-dimensional Newton constant ($\kappa = 8\pi G_8$). Unit: $\mathrm{GeV}^{-6}$. Status: AUTHOR.
- $w_{(p)}$: The author's Lovelock weights, $w_{(1)} = 1$, $w_{(2)} = 1/32$, $w_{(3)} = 1/1152$. Unit: dimensionless. Value: $(1, 1/32, 1/1152)$. Status: AUTHOR.
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the Lovelock couplings, the cosmological constant $\Lambda = -10H^2$ and the mass parameter $m_\Psi = H$. Unit: GeV (1/length). Value: 14.296 TeV (from the fit of $m_{\mathrm{W}}$ and $\rho_{\mathrm{EW},0}$). Status: AUTHOR.

<!-- end generated symbol list -->

**Origin (AUTHOR).** The author's Einstein-Lovelock action (section 4): the weights $w_{(p)}$ and the cosmological constant
$\Lambda = -10H^2$ are the author's, unchanged. Its metric variation is the left side of FE-1, verified by four routes
(pairing formula, Ricci tensor, explicit Gauss-Bonnet tensor, minisuperspace variation with a lapse), by the Bianchi
identities and against the record's equations (`um2_geometry.py`, 25 checks).

## IN-3: the Lovelock densities

$$
\begin{aligned}
\mathcal{L}_{(p)} &= \frac{1}{2^{p}}\,\delta^{M_1N_1\cdots M_pN_p}_{P_1Q_1\cdots P_pQ_p}\,
 R^{P_1Q_1}{}_{M_1N_1}\cdots R^{P_pQ_p}{}_{M_pN_p},\\
\mathcal{L}_{(1)} &= R,\qquad \mathcal{L}_{(2)} = R^2 - 4R_{MN}R^{MN} + R_{MNPQ}R^{MNPQ}
\end{aligned} \tag{IN-3}
$$

<!-- symbols: Lov, ip, delta, iM, iN, iP, iQ, Riemann -->
<!-- begin generated symbol list -->
**Symbols in (IN-3).**

- $\mathcal{L}_{(p)}$: The Lovelock density of order $p$ of the metric (a scalar built from $p$ Riemann tensors): $\mathcal{L}_{(1)} = R$ (Einstein-Hilbert), $\mathcal{L}_{(2)}$ the Gauss-Bonnet density, $\mathcal{L}_{(3)}$ the cubic Lovelock density. Unit: 1/$\mathrm{length}^{2p}$. Status: STANDARD.
- $p$: The Lovelock order $p = 1, 2, 3$ (Einstein, Gauss-Bonnet, cubic). Status: STANDARD.
- $\delta$: The Kronecker delta: with two indices $\delta^M_N = 1$ if $M = N$ and 0 otherwise (likewise $\delta_{\alpha e}$, $\delta_{l0}$, $\delta^{I3}$); with upper and lower index strings the generalised Kronecker delta $\delta^{M_1\cdots M_n}_{N_1\cdots N_n}$, the determinant of the $n \times n$ matrix of Kronecker deltas $\delta^{M_a}_{N_b}$ (+1 or -1 if the upper indices are an even or odd permutation of the lower ones, 0 otherwise). Status: STANDARD.
- $M$: A coordinate index of eight dimensions (also with a numbered copy $M_1, M_2, \dots$): it runs over $x_0, x_1, \dots, x_7$; a repeated index is summed. Status: STANDARD.
- $N$: A coordinate index of eight dimensions (also $N_1, N_2, \dots$), running over $x_0, \dots, x_7$; a repeated index is summed. Status: STANDARD.
- $P$: A coordinate index of eight dimensions (also $P_1, P_2, \dots$), running over $x_0, \dots, x_7$; a repeated index is summed. Status: STANDARD.
- $Q$: A coordinate index of eight dimensions (also $Q_1, Q_2, \dots$), running over $x_0, \dots, x_7$; a repeated index is summed. Status: STANDARD.
- $R^{MN}{}_{PQ},\ R_{MN},\ R$: The curvature of the metric $g_{MN}$: with four indices the Riemann tensor, with two indices the Ricci tensor $R_{MN} = R^P{}_{MPN}$, without indices the Ricci (scalar) curvature $R = g^{MN}R_{MN}$; $R^{ab}{}_{ab}$ (no sum) is the sectional curvature of the coordinate plane $(a, b)$. Unit: 1/$\mathrm{length}^{2}$. Status: STANDARD.

<!-- end generated symbol list -->

**Origin (STANDARD).** The Lovelock densities (Lovelock 1971), built with the generalised Kronecker delta (the definition of
the author's file `Generalized_Kronecker_Delta`, which is not committed). For the pair-diagonal curvature of the order-0
metric they reduce to the pairing formula FE-34 (DERIVED; `um2_geometry.py`, checks `einstein_from_ricci_equals_pairing_k1`,
`gauss_bonnet_tensor_equals_pairing_k2`).

## IN-4: the block stabiliser

$$
S_{\mathrm{stab}} = -\int\mathrm{d}^8X\,\sqrt{\lvert g\rvert}\;\rho_{\mathrm{stab}}(f),\qquad
\kappa\rho_{\mathrm{stab}}(f) = \kappa\rho_{\mathrm{stab}}(f_*)\Big(\frac{f_*}{f}\Big)^{8},\qquad
f = \mathrm{e}^{-a_4}\,b_4^{1/2} \tag{IN-4}
$$

<!-- symbols: Sstab, diff, Xcoord, metric, rhostab, fblock, kappa, fstar, euler, a4, b4 -->
<!-- begin generated symbol list -->
**Symbols in (IN-4).**

- $S_{\mathrm{stab}}$: The action of the block stabiliser (a vacuum energy of the block). Unit: dimensionless. Status: ASSUMED.
- $\mathrm{d}$: The differential: $\mathrm{d}X$ is an infinitesimal change of $X$, $\mathrm{d}X/\mathrm{d}Y$ the derivative of $X$ with respect to $Y$, $\mathrm{d}^nX$ the volume element of $n$ variables. Status: STANDARD.
- $X = \{x_0, \dots, x_7\}$: The author's coordinates of the eight-dimensional spacetime, $X = \{x_0, x_1, \dots, x_7\}$ with the hidden direction first; $X^M$ is the coordinate with the index $M$, $\mathrm{d}^8X = \mathrm{d}x_0\,\mathrm{d}x_1\cdots\mathrm{d}x_7$ the coordinate volume element and $X^\mu$ (four-dimensional index $\mu$) the observable coordinates $x_1, \dots, x_4$. Unit: length (each coordinate). Status: AUTHOR.
- $g_{MN}$: The metric tensor of the eight-dimensional spacetime (signature $+,+,+,+,-,-,-,-$ in the order $x_0, \dots, x_7$): $g_{MN}\,\mathrm{d}X^M\mathrm{d}X^N$ is the squared interval; $g^{MN}$ is its inverse, $g^M{}_N = \delta^M_N$, and $\lvert g\rvert$ the absolute value of its determinant, so that $\sqrt{\lvert g\rvert}\,\mathrm{d}^8X$ is the proper volume element. Unit: dimensionless. Status: AUTHOR.
- $\rho_{\mathrm{stab}}$: The energy density of the block stabiliser, a function of the block scale, $\rho_{\mathrm{stab}} \propto f^{-8}$; its value at the static block is $\rho_{\mathrm{stab}}(f_*)$. Unit: $\mathrm{GeV}^{8}$. Value: $\kappa\rho_{\mathrm{stab}}(f_*) = (26 + 4\sqrt{51})H^2 = 54.566\,H^2$. Status: ASSUMED.
- $f$: The block scale: the common scale factor of the hidden direction and the extra times, $f = \mathrm{e}^{-a_4}b_4^{1/2}$ (the block is $f^2$ times a four-dimensional space of constant curvature $-H^2$). Unit: dimensionless. Status: DERIVED.
- $\kappa$: The eight-dimensional gravitational coupling, $\kappa = 8\pi G_8$. Unit: $\mathrm{GeV}^{-6}$. Value: $\kappa/V_\perp = 8\pi G_{\mathrm{N}}\mathcal{G}(K_*) = 2.328\times10^{-36}$ GeV$^{-2}$. Status: AUTHOR.
- $f_*$: The block scale of the stabilised (static) block, $f_* = K_*^{-1/2}$. Unit: dimensionless. Value: 0.215556. Status: DERIVED.
- $\mathrm{e}$: Euler's number, the base of the natural logarithm; $\mathrm{e}^{X}$ is the exponential of $X$. Unit: dimensionless. Value: 2.718281828. Status: STANDARD.
- $a_4$: The author's metric function of the time $x_4$ that scales ordinary 3-space: the scale factor of cosmology is $\mathrm{e}^{a_4}$. Unit: dimensionless. Status: AUTHOR.
- $b_4$: The author's metric function of the time $x_4$ in the hidden and extra-time components, $b_4 > 0$. Unit: dimensionless. Status: AUTHOR.

<!-- end generated symbol list -->

**Origin (ASSUMED; its microscopic origin is OPEN).** Introduced in version 1 because the author's weights and $\Lambda$
admit no static block with attractive four-dimensional gravity without a source: the only sourceless static block with
$\mathcal{H} = 0$ has $K = 1/(4w_{(2)}) = 8$, where the coefficient of the four-dimensional Einstein-Hilbert term is
$\mathcal{G} = -1$ (repulsive), and it would need $\Lambda = -24H^2 \ne -10H^2$ (`um2_background.py`, checks
`static_vacuum_general`, `newton_factor_at_vacuum`). The stabiliser is conserved ($\rho_{\mathrm{stab}} \propto f^{-8}$),
four-dimensionally Lorentz invariant ($p_3 = -\rho_{\mathrm{stab}}$) and isotropic in the block ($p_0 = p_5$); its
normalisation is fixed by the static block (FE-43). The family in which the hidden pressure is $w_{\mathrm{stab}}$ times the
energy density, $p_0 = p_5 = w_{\mathrm{stab}}\rho_{\mathrm{stab}}$ with $\rho_{\mathrm{stab}} \propto f^{-4(1 + w_{\mathrm{stab}})}$,
was also computed at $w_{\mathrm{stab}} = 1/4, 1/2, 3/4, 1, 5/4, 3/2, 2, 3$: every member has a linearly stable block with
attractive gravity (check `block_stable_family`); UM-2 uses $w_{\mathrm{stab}} = 1$.

## IN-5: the dirac16complex field

$$
\begin{aligned}
S_\Psi &= \int\mathrm{d}^8X\,\sqrt{\lvert g\rvert}\,\Big[\tfrac12\big(\bar\Psi\gamma^MD_M\Psi
 - (D_M\bar\Psi)\gamma^M\Psi\big) - m_\Psi\,\bar\Psi\Psi - \frac{\lambda}{2}\big(\bar\Psi\Psi\big)^2\Big],\\
m_\Psi &= 3H\mathcal{M} = H\qquad (\mathcal{M} = 1/3)
\end{aligned} \tag{IN-5}
$$

<!-- symbols: SPsi, diff, Xcoord, metric, Psi, gamma, iM, Dcov, mPsi, lambda, Hconst, calM -->
<!-- begin generated symbol list -->
**Symbols in (IN-5).**

- $S_\Psi$: The action of the dirac16complex field (kinetic term with the canonical spin connection, mass term and contact self-interaction). Unit: dimensionless. Status: RECORD.
- $\mathrm{d}$: The differential: $\mathrm{d}X$ is an infinitesimal change of $X$, $\mathrm{d}X/\mathrm{d}Y$ the derivative of $X$ with respect to $Y$, $\mathrm{d}^nX$ the volume element of $n$ variables. Status: STANDARD.
- $X = \{x_0, \dots, x_7\}$: The author's coordinates of the eight-dimensional spacetime, $X = \{x_0, x_1, \dots, x_7\}$ with the hidden direction first; $X^M$ is the coordinate with the index $M$, $\mathrm{d}^8X = \mathrm{d}x_0\,\mathrm{d}x_1\cdots\mathrm{d}x_7$ the coordinate volume element and $X^\mu$ (four-dimensional index $\mu$) the observable coordinates $x_1, \dots, x_4$. Unit: length (each coordinate). Status: AUTHOR.
- $g_{MN}$: The metric tensor of the eight-dimensional spacetime (signature $+,+,+,+,-,-,-,-$ in the order $x_0, \dots, x_7$): $g_{MN}\,\mathrm{d}X^M\mathrm{d}X^N$ is the squared interval; $g^{MN}$ is its inverse, $g^M{}_N = \delta^M_N$, and $\lvert g\rvert$ the absolute value of its determinant, so that $\sqrt{\lvert g\rvert}\,\mathrm{d}^8X$ is the proper volume element. Unit: dimensionless. Status: AUTHOR.
- $\Psi,\ \bar\Psi$: dirac16complex: the 16-component complex spinor field of eight dimensions of the record (the author's field), the source of the dark matter (its lowest odd level) and of the massless fold bands; $\bar\Psi = \Psi^\dagger C$ is its Dirac adjoint. Unit: $\mathrm{GeV}^{7/2}$. Status: RECORD.
- $\gamma^a,\ \gamma^M,\ \gamma^\mu$: The Dirac matrices: $\gamma^a$ with a frame index are the author's real $16 \times 16$ matrices of the Clifford algebra of signature $(4, 4)$; $\gamma^M = \mathbf{e}_a{}^M\gamma^a$ along a coordinate ($\gamma^{x_0}$, $\gamma^{x_4}$, ... the matrices along $x_0$, $x_4$, ...), $\gamma_M = g_{MN}\gamma^N$; $\gamma^\mu$ the matrices of the four observable directions in four-dimensional formulas. Unit: dimensionless. Status: AUTHOR.
- $M$: A coordinate index of eight dimensions (also with a numbered copy $M_1, M_2, \dots$): it runs over $x_0, x_1, \dots, x_7$; a repeated index is summed. Status: STANDARD.
- $D_M,\ D_\mu$: The covariant derivative: on a spinor $D_M = \partial_M + \Omega_M$ (spin connection), on a Standard-Model fermion with the gauge fields added; on the sigma field $D_\mu\Sigma$ with the $W$ and $B$ fields. Unit: 1/length. Status: STANDARD.
- $m_\Psi$: The mass parameter of dirac16complex, $m_\Psi = 3H\mathcal{M} = H$. Unit: GeV. Value: 14.296 TeV. Status: RECORD.
- $\lambda$: The contact self-coupling of dirac16complex (the term $-\frac{\lambda}{2}(\bar\Psi\Psi)^2$ of the record). Unit: $\mathrm{GeV}^{-6}$. Value: not fixed; Kohn-Sham states computed for $\lambda = 0$ and $\pm7\times10^{-5}H^{-6}$; the fold-band radiation requires $\lvert\lambda\rvert \lesssim 1.4\times10^{-10}H^{-6}$ (for $\Delta N_{\mathrm{eff}} \le 0.001$). Status: RECORD.
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the Lovelock couplings, the cosmological constant $\Lambda = -10H^2$ and the mass parameter $m_\Psi = H$. Unit: GeV (1/length). Value: 14.296 TeV (from the fit of $m_{\mathrm{W}}$ and $\rho_{\mathrm{EW},0}$). Status: AUTHOR.
- $\mathcal{M}$: The record's dimensionless mass parameter of dirac16complex, $\mathcal{M} = 1/3$ ($m_\Psi = 3H\mathcal{M}$). Unit: dimensionless. Value: 1/3. Status: RECORD.

<!-- end generated symbol list -->

**Origin (RECORD).** The record's Dirac-type Lagrangian (section 5) with the author's form of the mass, $m_\Psi = 3H\mathcal{M}$,
and the record's value $\mathcal{M} = 1/3$, which UM-2 keeps (ASSUMED). The contact self-coupling $\lambda$ is the record's;
UM-2 does not fix it: the Kohn-Sham machinery is tested with $\lambda = 0$ and $\lambda = \pm7\times10^{-5}H^{-6}$, and the
fold-band radiation of the self-interaction channel (FE-135, FE-136) requires $\lvert\lambda\rvert \le 1.4\times10^{-10}H^{-6}$
for the coordinate volume $v_{\mathrm{t}} = H^{-3}$ of the extra times (ASSUMED bound; corrections, item 24).

## IN-6: the Clifford algebra, the Dirac adjoint and the two halves of dirac16complex

$$
\begin{aligned}
&\gamma^a\gamma^b + \gamma^b\gamma^a = 2\eta^{ab}\,\mathbf{1},\qquad
 \eta_{ab} = \mathrm{diag}(+1, +1, +1, +1, -1, -1, -1, -1),\qquad \gamma^M = \mathbf{e}_a{}^M\gamma^a,\\
&\bar\Psi = \Psi^\dagger C,\qquad C = \gamma^{x_0}\gamma^{x_1}\gamma^{x_2}\gamma^{x_3},\qquad
 \Gamma_4 = \mathrm{i}\gamma^{x_1}\gamma^{x_2}\gamma^{x_3}\gamma^{x_4},\qquad \mathcal{B} =
 -\mathrm{i}C\gamma^{x_4},\\
&\Psi = \Psi_A + \Psi_B,\qquad \mathcal{B}\Psi_A = -\Psi_A,\qquad \mathcal{B}\Psi_B = +\Psi_B
\end{aligned} \tag{IN-6}
$$

<!-- symbols: gamma, ia, ib, eta, identity, diag, iM, vielbein, Psi, dagger, Cmat, x0, x1, x2, x3, Gamma4, imag, x4, calB, PsiAB -->
<!-- begin generated symbol list -->
**Symbols in (IN-6).**

- $\gamma^a,\ \gamma^M,\ \gamma^\mu$: The Dirac matrices: $\gamma^a$ with a frame index are the author's real $16 \times 16$ matrices of the Clifford algebra of signature $(4, 4)$; $\gamma^M = \mathbf{e}_a{}^M\gamma^a$ along a coordinate ($\gamma^{x_0}$, $\gamma^{x_4}$, ... the matrices along $x_0$, $x_4$, ...), $\gamma_M = g_{MN}\gamma^N$; $\gamma^\mu$ the matrices of the four observable directions in four-dimensional formulas. Unit: dimensionless. Status: AUTHOR.
- $a$: A frame (orthonormal) index running over $0, 1, \dots, 7$, aligned with $x_0, \dots, x_7$; raised and lowered with $\eta_{ab}$; a repeated index is summed (except in a sectional curvature $R^{ab}{}_{ab}$). Status: STANDARD.
- $b$: A frame index running over $0, \dots, 7$ (as $a$). Status: STANDARD.
- $\eta_{ab}$: The flat metric of the frame, $\eta_{ab} = \mathrm{diag}(+1, +1, +1, +1, -1, -1, -1, -1)$ ($\eta^{ab}$ the same matrix). Unit: dimensionless. Status: AUTHOR.
- $\mathbf{1}$: The identity matrix (of the size fixed by the context: 16 x 16 on spinors, 3 x 3 on the generations or flavours, 2 x 2 for the sigma field). Unit: dimensionless. Status: STANDARD.
- $\mathrm{diag}$: A diagonal matrix with the listed entries on its diagonal (in the order of the coordinates $x_0, x_1, \dots, x_7$ when it is a tensor in eight dimensions). Status: STANDARD.
- $M$: A coordinate index of eight dimensions (also with a numbered copy $M_1, M_2, \dots$): it runs over $x_0, x_1, \dots, x_7$; a repeated index is summed. Status: STANDARD.
- $\mathbf{e}^a{}_M,\ \mathbf{e}_a{}^M$: The vielbein (frame field) of the metric: $g_{MN} = \eta_{ab}\,\mathbf{e}^a{}_M\mathbf{e}^b{}_N$; $\mathbf{e}_a{}^M$ is the inverse matrix. Unit: dimensionless. Status: STANDARD.
- $\Psi,\ \bar\Psi$: dirac16complex: the 16-component complex spinor field of eight dimensions of the record (the author's field), the source of the dark matter (its lowest odd level) and of the massless fold bands; $\bar\Psi = \Psi^\dagger C$ is its Dirac adjoint. Unit: $\mathrm{GeV}^{7/2}$. Status: RECORD.
- ${}^\dagger$: Hermitian conjugation: the complex conjugate of the transpose of a matrix or spinor (for field operators the adjoint operator). Status: STANDARD.
- $C$: The matrix of the Dirac adjoint, $C = \gamma^{x_0}\gamma^{x_1}\gamma^{x_2}\gamma^{x_3}$ ($\bar\Psi = \Psi^\dagger C$); in each block of the reduction $C = \varsigma_2\sigma_2$. Unit: dimensionless. Status: AUTHOR.
- $x_0$: The hidden space-like coordinate (listed first); the metric depends on it through $z = 6Hx_0$, periodically with the period $\pi/(6H)$. Unit: length. Status: AUTHOR.
- $x_1$: The first coordinate of ordinary 3-space. Unit: length. Status: AUTHOR.
- $x_2$: The second coordinate of ordinary 3-space. Unit: length. Status: AUTHOR.
- $x_3$: The third coordinate of ordinary 3-space (also the symmetry axis of the fast-flavour analysis). Unit: length. Status: AUTHOR.
- $\Gamma_4$: The four-dimensional chirality matrix, $\Gamma_4 = \mathrm{i}\gamma^{x_1}\gamma^{x_2}\gamma^{x_3}\gamma^{x_4}$; a doublet zero mode has $\Gamma_4 = +1$ (left-handed), a singlet zero mode $\Gamma_4 = -1$ (right-handed). Unit: dimensionless. Status: DERIVED.
- $\mathrm{i}$: The imaginary unit, $\mathrm{i}^2 = -1$. Unit: dimensionless. Status: STANDARD.
- $x_4$: The time; dots denote $\mathrm{d}/\mathrm{d}x_4$. Unit: length (= time, c = 1). Status: AUTHOR.
- $\mathcal{B}$: The author's operator $\mathcal{B} = -\mathrm{i}C\gamma^{x_4}$; its eigenvalues $\mp1$ define the halves $\Psi_A$ and $\Psi_B$, and it commutes with every interaction of the good sector. Unit: dimensionless. Status: AUTHOR.
- $\Psi_A,\ \Psi_B$: The two halves of dirac16complex, $\Psi = \Psi_A + \Psi_B$, the eigenspaces of $\mathcal{B}$ with the eigenvalues $-1$ and $+1$; each half carries one dark-matter species. Unit: $\mathrm{GeV}^{7/2}$. Status: AUTHOR.

<!-- end generated symbol list -->

**Origin (AUTHOR).** The author's real $16\times16$ matrices of section 4 and the matrices $C$, $\Gamma_4$, $\mathcal{B}$ derived
from them. The Clifford algebra, the reality, $C^T = C$ and $C^2 = \mathbf{1}$, the antisymmetry of $C\gamma^a$, the
irreducibility of the 16-dimensional representation of Pin(4,4), the two inequivalent halves of Spin(4,4) and the block forms
are verified exactly (`um2_algebra.py`, 31 checks). The halves $\Psi_A$ and $\Psi_B$ are the eigenspaces of $\mathcal{B}$;
$\mathcal{B}$ commutes with every interaction of the good sector, so the numbers of quanta of the two halves are conserved
separately (computed with the author's matrices: `um2_analysis.py`, check `B5_stability_and_neutrality`;
`um2_electroweak.py`, checks `B_lorentz_invariant`, `Gamma4_equals_minus_B_gamma0`).

## IN-7: the canonical spin connection

$$
\begin{aligned}
&D_M\Psi = \partial_M\Psi + \Omega_M\Psi,\qquad D_M\bar\Psi = \partial_M\bar\Psi - \bar\Psi\Omega_M,\qquad
 \Omega_M = \tfrac12\,\omega_{Mab}\,\mathcal{S}^{ab},\qquad \mathcal{S}^{ab} = \tfrac14\big[\gamma^a,
 \gamma^b\big],\\
&\omega_M{}^a{}_b = \mathbf{e}^a{}_N\big(\partial_M\mathbf{e}_b{}^N +
 \Gamma^N{}_{MP}\,\mathbf{e}_b{}^P\big),\qquad
 \omega_{Mab} = \eta_{ac}\,\omega_M{}^c{}_b,\qquad g_{MN} = \eta_{ab}\,\mathbf{e}^a{}_M\,\mathbf{e}^b{}_N,\\
&\Gamma^N{}_{MP} = \tfrac12\,g^{NQ}\big(\partial_Mg_{QP} + \partial_Pg_{QM} - \partial_Qg_{MP}\big)
\end{aligned} \tag{IN-7}
$$

<!-- symbols: Dcov, iM, Psi, partial, Omega, omega, ia, ib, calS, gamma, vielbein, iN, Christoffel, iP, eta, ic, metric, iQ -->
<!-- begin generated symbol list -->
**Symbols in (IN-7).**

- $D_M,\ D_\mu$: The covariant derivative: on a spinor $D_M = \partial_M + \Omega_M$ (spin connection), on a Standard-Model fermion with the gauge fields added; on the sigma field $D_\mu\Sigma$ with the $W$ and $B$ fields. Unit: 1/length. Status: STANDARD.
- $M$: A coordinate index of eight dimensions (also with a numbered copy $M_1, M_2, \dots$): it runs over $x_0, x_1, \dots, x_7$; a repeated index is summed. Status: STANDARD.
- $\Psi,\ \bar\Psi$: dirac16complex: the 16-component complex spinor field of eight dimensions of the record (the author's field), the source of the dark matter (its lowest odd level) and of the massless fold bands; $\bar\Psi = \Psi^\dagger C$ is its Dirac adjoint. Unit: $\mathrm{GeV}^{7/2}$. Status: RECORD.
- $\partial$: A partial derivative: $\partial_M$ is the derivative with respect to the coordinate $X^M$, $\partial_y$ with respect to $y$, $\partial_{x_4}$ with respect to the time $x_4$, $\partial X/\partial Y$ the derivative of $X$ with respect to $Y$ at fixed other variables. Status: STANDARD.
- $\Omega_M$: The spin connection acting on spinors, the matrix $\Omega_M = \frac12\omega_{Mab}\mathcal{S}^{ab}$. Unit: 1/length. Status: STANDARD.
- $\omega_M{}^a{}_b$: The coefficients of the spin connection of the vielbein (the Levi-Civita connection in the frame basis); $\omega_{Mab} = \eta_{ac}\,\omega_M{}^c{}_b$. Unit: 1/length. Status: STANDARD.
- $a$: A frame (orthonormal) index running over $0, 1, \dots, 7$, aligned with $x_0, \dots, x_7$; raised and lowered with $\eta_{ab}$; a repeated index is summed (except in a sectional curvature $R^{ab}{}_{ab}$). Status: STANDARD.
- $b$: A frame index running over $0, \dots, 7$ (as $a$). Status: STANDARD.
- $\mathcal{S}^{ab}$: The generators of frame rotations on spinors, $\mathcal{S}^{ab} = \frac14[\gamma^a, \gamma^b]$ (the commutator). Unit: dimensionless. Status: STANDARD.
- $\gamma^a,\ \gamma^M,\ \gamma^\mu$: The Dirac matrices: $\gamma^a$ with a frame index are the author's real $16 \times 16$ matrices of the Clifford algebra of signature $(4, 4)$; $\gamma^M = \mathbf{e}_a{}^M\gamma^a$ along a coordinate ($\gamma^{x_0}$, $\gamma^{x_4}$, ... the matrices along $x_0$, $x_4$, ...), $\gamma_M = g_{MN}\gamma^N$; $\gamma^\mu$ the matrices of the four observable directions in four-dimensional formulas. Unit: dimensionless. Status: AUTHOR.
- $\mathbf{e}^a{}_M,\ \mathbf{e}_a{}^M$: The vielbein (frame field) of the metric: $g_{MN} = \eta_{ab}\,\mathbf{e}^a{}_M\mathbf{e}^b{}_N$; $\mathbf{e}_a{}^M$ is the inverse matrix. Unit: dimensionless. Status: STANDARD.
- $N$: A coordinate index of eight dimensions (also $N_1, N_2, \dots$), running over $x_0, \dots, x_7$; a repeated index is summed. Status: STANDARD.
- $\Gamma^N{}_{MP}$: The Christoffel symbols (the Levi-Civita connection) of the metric, $\Gamma^N{}_{MP} = \frac12 g^{NQ}(\partial_Mg_{QP} + \partial_Pg_{QM} - \partial_Qg_{MP})$. Unit: 1/length. Status: STANDARD.
- $P$: A coordinate index of eight dimensions (also $P_1, P_2, \dots$), running over $x_0, \dots, x_7$; a repeated index is summed. Status: STANDARD.
- $\eta_{ab}$: The flat metric of the frame, $\eta_{ab} = \mathrm{diag}(+1, +1, +1, +1, -1, -1, -1, -1)$ ($\eta^{ab}$ the same matrix). Unit: dimensionless. Status: AUTHOR.
- $c$: A frame index running over $0, \dots, 7$ (as $a$). Status: STANDARD.
- $g_{MN}$: The metric tensor of the eight-dimensional spacetime (signature $+,+,+,+,-,-,-,-$ in the order $x_0, \dots, x_7$): $g_{MN}\,\mathrm{d}X^M\mathrm{d}X^N$ is the squared interval; $g^{MN}$ is its inverse, $g^M{}_N = \delta^M_N$, and $\lvert g\rvert$ the absolute value of its determinant, so that $\sqrt{\lvert g\rvert}\,\mathrm{d}^8X$ is the proper volume element. Unit: dimensionless. Status: AUTHOR.
- $Q$: A coordinate index of eight dimensions (also $Q_1, Q_2, \dots$), running over $x_0, \dots, x_7$; a repeated index is summed. Status: STANDARD.

<!-- end generated symbol list -->

**Origin (STANDARD; chosen by the record).** The canonical (vielbein-postulate, torsion-free) spin connection, the standard
coupling of a spinor to gravity, chosen by the record instead of the notebook's contraction of the mixed connection
coefficients (section 5); the order of 2026-10-17 asks for a non-trivial canonical spin connection. On the order-0 metric
it makes $\gamma^N$ covariantly constant, gives FE-13 and vanishes only in flat 4+4 space (`um2_geometry.py`, checks
`gamma_covariantly_constant`, `gamma_mu_Omega_mu`, `nontrivial_unless_flat`).

## IN-8: the gauge fields in eight dimensions

$$
S_{\mathrm{gauge}} = -\frac14\int\mathrm{d}^8X\,\sqrt{\lvert g\rvert}\,\Big(\frac{1}{\hat
 g_3^2}\,G^A_{MN}G^{AMN}
 + \frac{1}{\hat g_2^2}\,W^I_{MN}W^{IMN} + \frac{1}{\hat g_1^2}\,B_{MN}B^{MN}\Big) \tag{IN-8}
$$

<!-- symbols: Sgauge, diff, Xcoord, metric, ghat3, Ggluon, iA, iM, iN, ghat2, Wsu2, iI, ghat1, Bhyp -->
<!-- begin generated symbol list -->
**Symbols in (IN-8).**

- $S_{\mathrm{gauge}}$: The action of the gauge fields of SU(3), SU(2) and U(1)$_Y$ in eight dimensions. Unit: dimensionless. Status: ASSUMED.
- $\mathrm{d}$: The differential: $\mathrm{d}X$ is an infinitesimal change of $X$, $\mathrm{d}X/\mathrm{d}Y$ the derivative of $X$ with respect to $Y$, $\mathrm{d}^nX$ the volume element of $n$ variables. Status: STANDARD.
- $X = \{x_0, \dots, x_7\}$: The author's coordinates of the eight-dimensional spacetime, $X = \{x_0, x_1, \dots, x_7\}$ with the hidden direction first; $X^M$ is the coordinate with the index $M$, $\mathrm{d}^8X = \mathrm{d}x_0\,\mathrm{d}x_1\cdots\mathrm{d}x_7$ the coordinate volume element and $X^\mu$ (four-dimensional index $\mu$) the observable coordinates $x_1, \dots, x_4$. Unit: length (each coordinate). Status: AUTHOR.
- $g_{MN}$: The metric tensor of the eight-dimensional spacetime (signature $+,+,+,+,-,-,-,-$ in the order $x_0, \dots, x_7$): $g_{MN}\,\mathrm{d}X^M\mathrm{d}X^N$ is the squared interval; $g^{MN}$ is its inverse, $g^M{}_N = \delta^M_N$, and $\lvert g\rvert$ the absolute value of its determinant, so that $\sqrt{\lvert g\rvert}\,\mathrm{d}^8X$ is the proper volume element. Unit: dimensionless. Status: AUTHOR.
- $\hat g_3$: The eight-dimensional SU(3) coupling (it multiplies the gluon kinetic term as $1/\hat g_3^2$); $g_3^2 = \hat g_3^2/V_\perp$. Unit: $\mathrm{GeV}^{-2}$. Status: ASSUMED.
- $G^A_M,\ G_M,\ G_{MN},\ G^A_{MN}$: The gluon field (SU(3)), in the geometric normalisation of the action (couplings in front of the kinetic terms): the components $G^A_M$ ($A = 1, \dots, 8$), the matrix $G_M = G^A_Mt^A$, the field strength $G_{MN}$ (matrix) and its components $G^A_{MN}$; $G^A_{\mu\nu}$ are its components along the observable directions (the zero mode, flat in $x_0$). Unit: GeV (field), $\mathrm{GeV}^{2}$ (field strength). Status: ASSUMED.
- $A$: A colour (adjoint SU(3)) index running over $1, \dots, 8$; a repeated index is summed. Status: STANDARD.
- $M$: A coordinate index of eight dimensions (also with a numbered copy $M_1, M_2, \dots$): it runs over $x_0, x_1, \dots, x_7$; a repeated index is summed. Status: STANDARD.
- $N$: A coordinate index of eight dimensions (also $N_1, N_2, \dots$), running over $x_0, \dots, x_7$; a repeated index is summed. Status: STANDARD.
- $\hat g_2$: The eight-dimensional SU(2) coupling; $g_2^2 = \hat g_2^2/V_\perp$. Unit: $\mathrm{GeV}^{-2}$. Status: ASSUMED.
- $W^I_M,\ W_M,\ W_{MN},\ W^I_{MN}$: The SU(2) gauge field (geometric normalisation): the components $W^I_M$ ($I = 1, 2, 3$; $W^3$ the third component), the matrix $W_M = W^I_M\tau^I/2$, the field strength $W_{MN}$ and its components $W^I_{MN}$; with Greek indices the components along the observable directions. Unit: GeV (field), $\mathrm{GeV}^{2}$ (field strength). Status: ASSUMED.
- $I$: A weak-isospin (adjoint SU(2)) index running over $1, 2, 3$; a repeated index is summed. Status: STANDARD.
- $\hat g_1$: The eight-dimensional U(1)$_Y$ coupling; $g_1^2 = \hat g_1^2/V_\perp$. Unit: $\mathrm{GeV}^{-2}$. Status: ASSUMED.
- $B_M,\ B_{MN}$: The hypercharge gauge field U(1)$_Y$ (geometric normalisation) and its field strength. Unit: GeV (field), $\mathrm{GeV}^{2}$ (field strength). Status: ASSUMED.

<!-- end generated symbol list -->

**Origin (ASSUMED structure; STANDARD form).** The gauge group of the Standard Model, $SU(3)_c\times SU(2)_L\times U(1)_Y$, in
eight dimensions with the standard Yang-Mills action in the geometric normalisation (the couplings $1/\hat g_i^2$ in front
of the kinetic terms). The gauge structure is that of QCD and of the electroweak model; the zero modes of the gauge fields
are flat in $x_0$ and are the four-dimensional gauge fields with the couplings $g_i^2 = \hat g_i^2/V_\perp$ (FE-49). The
gluons and the photon stay exactly massless (`um2_spectra.py`, check `massless_zero_mode`).

## IN-9: the field strengths

$$
\begin{aligned}
&G_M = G^A_M\,t^A,\qquad G_{MN} = \partial_MG_N - \partial_NG_M - \mathrm{i}\big[G_M, G_N\big],\qquad
 G^A_{MN} = 2\,\mathrm{tr}\big(t^AG_{MN}\big),\\
&W_M = W^I_M\,\frac{\tau^I}{2},\qquad W_{MN} = \partial_MW_N - \partial_NW_M - \mathrm{i}\big[W_M,
 W_N\big],\qquad
 W^I_{MN} = \mathrm{tr}\big(\tau^IW_{MN}\big),\\
&B_{MN} = \partial_MB_N - \partial_NB_M
\end{aligned} \tag{IN-9}
$$

<!-- symbols: Ggluon, iM, iA, tgen, iN, partial, imag, trace, Wsu2, iI, tau, Bhyp -->
<!-- begin generated symbol list -->
**Symbols in (IN-9).**

- $G^A_M,\ G_M,\ G_{MN},\ G^A_{MN}$: The gluon field (SU(3)), in the geometric normalisation of the action (couplings in front of the kinetic terms): the components $G^A_M$ ($A = 1, \dots, 8$), the matrix $G_M = G^A_Mt^A$, the field strength $G_{MN}$ (matrix) and its components $G^A_{MN}$; $G^A_{\mu\nu}$ are its components along the observable directions (the zero mode, flat in $x_0$). Unit: GeV (field), $\mathrm{GeV}^{2}$ (field strength). Status: ASSUMED.
- $M$: A coordinate index of eight dimensions (also with a numbered copy $M_1, M_2, \dots$): it runs over $x_0, x_1, \dots, x_7$; a repeated index is summed. Status: STANDARD.
- $A$: A colour (adjoint SU(3)) index running over $1, \dots, 8$; a repeated index is summed. Status: STANDARD.
- $t^A$: The generators of SU(3) in the fundamental representation (the Gell-Mann matrices divided by 2), $\mathrm{tr}(t^At^B) = \frac12\delta^{AB}$. Unit: dimensionless. Status: STANDARD.
- $N$: A coordinate index of eight dimensions (also $N_1, N_2, \dots$), running over $x_0, \dots, x_7$; a repeated index is summed. Status: STANDARD.
- $\partial$: A partial derivative: $\partial_M$ is the derivative with respect to the coordinate $X^M$, $\partial_y$ with respect to $y$, $\partial_{x_4}$ with respect to the time $x_4$, $\partial X/\partial Y$ the derivative of $X$ with respect to $Y$ at fixed other variables. Status: STANDARD.
- $\mathrm{i}$: The imaginary unit, $\mathrm{i}^2 = -1$. Unit: dimensionless. Status: STANDARD.
- $\mathrm{tr}$: The trace of a matrix: the sum of its diagonal entries. Status: STANDARD.
- $W^I_M,\ W_M,\ W_{MN},\ W^I_{MN}$: The SU(2) gauge field (geometric normalisation): the components $W^I_M$ ($I = 1, 2, 3$; $W^3$ the third component), the matrix $W_M = W^I_M\tau^I/2$, the field strength $W_{MN}$ and its components $W^I_{MN}$; with Greek indices the components along the observable directions. Unit: GeV (field), $\mathrm{GeV}^{2}$ (field strength). Status: ASSUMED.
- $I$: A weak-isospin (adjoint SU(2)) index running over $1, 2, 3$; a repeated index is summed. Status: STANDARD.
- $\tau^I$: The Pauli matrices acting on weak-isospin doublets ($\tau^I/2$ the generators of SU(2); $\tau^3 = \mathrm{diag}(1, -1)$). Unit: dimensionless. Status: STANDARD.
- $B_M,\ B_{MN}$: The hypercharge gauge field U(1)$_Y$ (geometric normalisation) and its field strength. Unit: GeV (field), $\mathrm{GeV}^{2}$ (field strength). Status: ASSUMED.

<!-- end generated symbol list -->

**Origin (STANDARD).** The field strengths of the three gauge groups.

## IN-10: the physical electroweak fields

$$
\begin{aligned}
&W^\pm_M = \frac{W^1_M \mp \mathrm{i}W^2_M}{\sqrt2\,\hat g_2},\qquad
 Z_M = \frac{W^3_M - B_M}{\hat g_Z},\qquad A_M = \frac{\hat g_1^2\,W^3_M + \hat g_2^2\,B_M}{\hat g_1\hat
 g_2\hat g_Z},\\
&\hat g_Z = \sqrt{\hat g_2^2 + \hat g_1^2},\qquad \cos\theta_{\mathrm{W}} = \frac{\hat g_2}{\hat g_Z},\qquad
 \sin\theta_{\mathrm{W}} = \frac{\hat g_1}{\hat g_Z}
\end{aligned} \tag{IN-10}
$$

<!-- symbols: Wpm, iM, Wsu2, imag, ghat2, Zboson, Bhyp, ghatZ, Aphoton, ghat1, thetaW -->
<!-- begin generated symbol list -->
**Symbols in (IN-10).**

- $W^\pm_M,\ W^+,\ W^-$: The charged weak bosons, canonically normalised: $W^\pm_M = (W^1_M \mp \mathrm{i}W^2_M)/(\sqrt2\,\hat g_2)$; $W^+$ carries the electric charge $+e$ and $W^-$ the charge $-e$ (they are each other's antiparticles and have one mass). Unit: $\mathrm{GeV}^{3}$. Status: STANDARD.
- $M$: A coordinate index of eight dimensions (also with a numbered copy $M_1, M_2, \dots$): it runs over $x_0, x_1, \dots, x_7$; a repeated index is summed. Status: STANDARD.
- $W^I_M,\ W_M,\ W_{MN},\ W^I_{MN}$: The SU(2) gauge field (geometric normalisation): the components $W^I_M$ ($I = 1, 2, 3$; $W^3$ the third component), the matrix $W_M = W^I_M\tau^I/2$, the field strength $W_{MN}$ and its components $W^I_{MN}$; with Greek indices the components along the observable directions. Unit: GeV (field), $\mathrm{GeV}^{2}$ (field strength). Status: ASSUMED.
- $\mathrm{i}$: The imaginary unit, $\mathrm{i}^2 = -1$. Unit: dimensionless. Status: STANDARD.
- $\hat g_2$: The eight-dimensional SU(2) coupling; $g_2^2 = \hat g_2^2/V_\perp$. Unit: $\mathrm{GeV}^{-2}$. Status: ASSUMED.
- $Z_M$: The $Z$ boson field, canonically normalised, $Z_M = (W^3_M - B_M)/\hat g_Z$. Unit: $\mathrm{GeV}^{3}$. Status: STANDARD.
- $B_M,\ B_{MN}$: The hypercharge gauge field U(1)$_Y$ (geometric normalisation) and its field strength. Unit: GeV (field), $\mathrm{GeV}^{2}$ (field strength). Status: ASSUMED.
- $\hat g_Z$: The eight-dimensional coupling of the $Z$, $\hat g_Z = (\hat g_2^2 + \hat g_1^2)^{1/2}$. Unit: $\mathrm{GeV}^{-2}$. Status: STANDARD.
- $A_M$: The photon field, canonically normalised, $A_M = (\hat g_1^2W^3_M + \hat g_2^2B_M)/(\hat g_1\hat g_2\hat g_Z)$. Unit: $\mathrm{GeV}^{3}$. Status: STANDARD.
- $\hat g_1$: The eight-dimensional U(1)$_Y$ coupling; $g_1^2 = \hat g_1^2/V_\perp$. Unit: $\mathrm{GeV}^{-2}$. Status: ASSUMED.
- $\theta_{\mathrm{W}}$: The weak mixing angle of the couplings, $\cos\theta_{\mathrm{W}} = \hat g_2/\hat g_Z$, $\sin\theta_{\mathrm{W}} = \hat g_1/\hat g_Z$; fixed by the measured $W$ and $Z$ masses with $\rho_{\mathrm{EW},0}$. Unit: dimensionless. Value: $\cos^2\theta_{\mathrm{W}} = 0.776368$. Status: DERIVED.

<!-- end generated symbol list -->

**Origin (STANDARD).** The physical electroweak fields of the Standard Model, canonically normalised. $W^+$ carries the
electric charge $+e$ and $W^-$ the charge $-e$; $W^-$ is the antiparticle of $W^+$ (DERIVED: `um2_electroweak.py`, check
`W_charges`; the author's order "the W+ and W- bosons carry positive and negative electric charges. Do not forget this").
The angle of the couplings is fixed by the measured $W$ and $Z$ masses with the measured electroweak parameter (FE-55).

## IN-11: the Standard-Model fermions of three generations

$$
\begin{aligned}
S_{\mathrm{f}} &= \sum_{i=1}^{3}\sum_{\psi}\int\mathrm{d}^8X\,\sqrt{\lvert
 g\rvert}\,\Big[\tfrac12\big(\bar\psi_i\gamma^MD_M\psi_i
 - (D_M\bar\psi_i)\gamma^M\psi_i\big) - \mu_{\psi i}\,\bar\psi_i\psi_i\Big],\\
\psi &\in \{Q,\ u_R,\ d_R,\ \ell,\ e_R,\ \nu_R\},\qquad \mu_{\psi i} = \mu_Q\ (\psi = Q),\qquad
 \mu_{\psi i} = \mu_\ell\ (\psi = \ell)
\end{aligned} \tag{IN-11}
$$

<!-- symbols: Sf, ii, ipsi, diff, Xcoord, metric, psi, gamma, iM, Dcov, mubulk, Qdoublet, uR, dR, ldoublet, eR, nuR, muQ, muell -->
<!-- begin generated symbol list -->
**Symbols in (IN-11).**

- $S_{\mathrm{f}}$: The action of the Standard-Model fermions of three generations (kinetic and bulk-mass terms). Unit: dimensionless. Status: ASSUMED.
- $i$: The generation index ($i = 1, 2, 3$), which also labels the neutrino mass states $\nu_1, \nu_2, \nu_3$; a repeated index is not summed unless a sum sign is written. Status: STANDARD.
- $\psi$: The label of a Standard-Model multiplet: $\psi \in \{Q, u_R, d_R, \ell, e_R, \nu_R\}$ (quark doublet, up and down quark singlets, lepton doublet, charged-lepton singlet, right-handed neutrino); a sum over $\psi$ runs over the six. Status: STANDARD.
- $\mathrm{d}$: The differential: $\mathrm{d}X$ is an infinitesimal change of $X$, $\mathrm{d}X/\mathrm{d}Y$ the derivative of $X$ with respect to $Y$, $\mathrm{d}^nX$ the volume element of $n$ variables. Status: STANDARD.
- $X = \{x_0, \dots, x_7\}$: The author's coordinates of the eight-dimensional spacetime, $X = \{x_0, x_1, \dots, x_7\}$ with the hidden direction first; $X^M$ is the coordinate with the index $M$, $\mathrm{d}^8X = \mathrm{d}x_0\,\mathrm{d}x_1\cdots\mathrm{d}x_7$ the coordinate volume element and $X^\mu$ (four-dimensional index $\mu$) the observable coordinates $x_1, \dots, x_4$. Unit: length (each coordinate). Status: AUTHOR.
- $g_{MN}$: The metric tensor of the eight-dimensional spacetime (signature $+,+,+,+,-,-,-,-$ in the order $x_0, \dots, x_7$): $g_{MN}\,\mathrm{d}X^M\mathrm{d}X^N$ is the squared interval; $g^{MN}$ is its inverse, $g^M{}_N = \delta^M_N$, and $\lvert g\rvert$ the absolute value of its determinant, so that $\sqrt{\lvert g\rvert}\,\mathrm{d}^8X$ is the proper volume element. Unit: dimensionless. Status: AUTHOR.
- $\psi_i,\ \bar\psi_i$: A Standard-Model fermion field of eight dimensions: $\psi_i$ is the multiplet $\psi \in \{Q, u_R, d_R, \ell, e_R, \nu_R\}$ of the generation $i$, $\psi_f$ one fermion component $f$ (in four-dimensional formulas its zero mode); $\bar\psi = \psi^\dagger C$ the Dirac adjoint. Unit: $\mathrm{GeV}^{7/2}$ (eight dimensions), $\mathrm{GeV}^{3/2}$ (four dimensions). Status: ASSUMED.
- $\gamma^a,\ \gamma^M,\ \gamma^\mu$: The Dirac matrices: $\gamma^a$ with a frame index are the author's real $16 \times 16$ matrices of the Clifford algebra of signature $(4, 4)$; $\gamma^M = \mathbf{e}_a{}^M\gamma^a$ along a coordinate ($\gamma^{x_0}$, $\gamma^{x_4}$, ... the matrices along $x_0$, $x_4$, ...), $\gamma_M = g_{MN}\gamma^N$; $\gamma^\mu$ the matrices of the four observable directions in four-dimensional formulas. Unit: dimensionless. Status: AUTHOR.
- $M$: A coordinate index of eight dimensions (also with a numbered copy $M_1, M_2, \dots$): it runs over $x_0, x_1, \dots, x_7$; a repeated index is summed. Status: STANDARD.
- $D_M,\ D_\mu$: The covariant derivative: on a spinor $D_M = \partial_M + \Omega_M$ (spin connection), on a Standard-Model fermion with the gauge fields added; on the sigma field $D_\mu\Sigma$ with the $W$ and $B$ fields. Unit: 1/length. Status: STANDARD.
- $\mu_{\psi i}$: The bulk mass of a Standard-Model fermion: $\mu_{\psi i}$ of the multiplet $\psi$ of the generation $i$; with the hidden direction it fixes the localisation $c = f\mu L$ of the zero mode. Unit: GeV. Value: $\mu_{\psi i} = c/(fL)$ with the localisation $c$ of the zero mode (doublets: $\mu_Q = 5.2304\,H$, $\mu_\ell = 9.2055\,H$). Status: ASSUMED.
- $Q_i,\ \bar Q_i$: The quark doublet of the generation $i$ (left-handed up and down quark of one generation, three colours) and its Dirac adjoint. Unit: $\mathrm{GeV}^{7/2}$. Status: ASSUMED.
- $u_R,\ u_{Ri},\ \bar u_{Ri}$: The up-type quark singlet: $u_R$ the multiplet, $u_{Ri}$ that of the generation $i$ ($u_R$, $c_R$, $t_R$), $\bar u_{Ri}$ its Dirac adjoint. Unit: $\mathrm{GeV}^{7/2}$. Status: ASSUMED.
- $d_R,\ d_{Ri},\ \bar d_{Ri}$: The down-type quark singlet: $d_R$ the multiplet, $d_{Ri}$ that of the generation $i$ ($d_R$, $s_R$, $b_R$), $\bar d_{Ri}$ its Dirac adjoint. Unit: $\mathrm{GeV}^{7/2}$. Status: ASSUMED.
- $\ell_i,\ \bar\ell_i$: The lepton doublet of the generation $i$ (left-handed neutrino and charged lepton) and its Dirac adjoint. Unit: $\mathrm{GeV}^{7/2}$. Status: ASSUMED.
- $e_R,\ e_{Ri}$: The right-handed charged-lepton singlet: $e_R$ the multiplet, $e_{Ri}$ that of the generation $i$ ($e_R$, $\mu_R$, $\tau_R$). Unit: $\mathrm{GeV}^{7/2}$. Status: ASSUMED.
- $\nu_R,\ \nu_{Ri}$: The right-handed neutrino (a gauge singlet): $\nu_R$ the multiplet, $\nu_{Ri}$ that of the generation $i$; its zero modes give Dirac neutrino masses. Unit: $\mathrm{GeV}^{7/2}$. Status: ASSUMED.
- $\mu_Q$: The common bulk mass of the three quark doublets. Unit: GeV. Value: $5.2304\,H$ ($c_Q = 3.38230$). Status: DERIVED.
- $\mu_\ell$: The common bulk mass of the three lepton doublets. Unit: GeV. Value: $9.2055\,H$ ($c_\ell = 5.95288$). Status: DERIVED.

<!-- end generated symbol list -->

**Origin (ASSUMED).** Three generations of quarks and leptons (the author's choice (A) of 2026-10-18), each multiplet a
16-component spinor of the same Clifford algebra times its gauge indices, with bulk masses; one doublet bulk mass per
sector, $\mu_Q$ and $\mu_\ell$ (ASSUMED), and right-handed neutrinos $\nu_{Ri}$ for the Dirac masses of the neutrinos in the
$x_0$ mechanism (ASSUMED; the Majorana alternative without them is analysed). The hypercharges are those of the Standard
Model ($\frac16$, $\frac23$, $-\frac13$, $-\frac12$, $-1$, $0$ for $Q$, $u_R$, $d_R$, $\ell$, $e_R$, $\nu_R$), and every
generation is anomaly free (DERIVED: `um2_electroweak.py`, check `anomaly_cancellation`). The neutrinos of the lepton
doublets are the weak partners of the charged leptons (the flavours $\nu_e$, $\nu_\mu$, $\nu_\tau$), not the mass states
$\nu_1$, $\nu_2$, $\nu_3$.

## IN-12: the covariant derivative of a fermion and the electric charge

$$
D_M = \partial_M + \Omega_M - \mathrm{i}G^A_M\,t^A - \mathrm{i}W^I_M\,\frac{\tau^I}{2} - \mathrm{i}\,Y
 B_M,\qquad
Q_{\mathrm{em}} = T_3 + Y \tag{IN-12}
$$

<!-- symbols: Dcov, iM, partial, Omega, imag, Ggluon, iA, tgen, Wsu2, iI, tau, Yhyp, Bhyp, Qem, T3 -->
<!-- begin generated symbol list -->
**Symbols in (IN-12).**

- $D_M,\ D_\mu$: The covariant derivative: on a spinor $D_M = \partial_M + \Omega_M$ (spin connection), on a Standard-Model fermion with the gauge fields added; on the sigma field $D_\mu\Sigma$ with the $W$ and $B$ fields. Unit: 1/length. Status: STANDARD.
- $M$: A coordinate index of eight dimensions (also with a numbered copy $M_1, M_2, \dots$): it runs over $x_0, x_1, \dots, x_7$; a repeated index is summed. Status: STANDARD.
- $\partial$: A partial derivative: $\partial_M$ is the derivative with respect to the coordinate $X^M$, $\partial_y$ with respect to $y$, $\partial_{x_4}$ with respect to the time $x_4$, $\partial X/\partial Y$ the derivative of $X$ with respect to $Y$ at fixed other variables. Status: STANDARD.
- $\Omega_M$: The spin connection acting on spinors, the matrix $\Omega_M = \frac12\omega_{Mab}\mathcal{S}^{ab}$. Unit: 1/length. Status: STANDARD.
- $\mathrm{i}$: The imaginary unit, $\mathrm{i}^2 = -1$. Unit: dimensionless. Status: STANDARD.
- $G^A_M,\ G_M,\ G_{MN},\ G^A_{MN}$: The gluon field (SU(3)), in the geometric normalisation of the action (couplings in front of the kinetic terms): the components $G^A_M$ ($A = 1, \dots, 8$), the matrix $G_M = G^A_Mt^A$, the field strength $G_{MN}$ (matrix) and its components $G^A_{MN}$; $G^A_{\mu\nu}$ are its components along the observable directions (the zero mode, flat in $x_0$). Unit: GeV (field), $\mathrm{GeV}^{2}$ (field strength). Status: ASSUMED.
- $A$: A colour (adjoint SU(3)) index running over $1, \dots, 8$; a repeated index is summed. Status: STANDARD.
- $t^A$: The generators of SU(3) in the fundamental representation (the Gell-Mann matrices divided by 2), $\mathrm{tr}(t^At^B) = \frac12\delta^{AB}$. Unit: dimensionless. Status: STANDARD.
- $W^I_M,\ W_M,\ W_{MN},\ W^I_{MN}$: The SU(2) gauge field (geometric normalisation): the components $W^I_M$ ($I = 1, 2, 3$; $W^3$ the third component), the matrix $W_M = W^I_M\tau^I/2$, the field strength $W_{MN}$ and its components $W^I_{MN}$; with Greek indices the components along the observable directions. Unit: GeV (field), $\mathrm{GeV}^{2}$ (field strength). Status: ASSUMED.
- $I$: A weak-isospin (adjoint SU(2)) index running over $1, 2, 3$; a repeated index is summed. Status: STANDARD.
- $\tau^I$: The Pauli matrices acting on weak-isospin doublets ($\tau^I/2$ the generators of SU(2); $\tau^3 = \mathrm{diag}(1, -1)$). Unit: dimensionless. Status: STANDARD.
- $Y$: The hypercharge (the generator of U(1)$_Y$); $Y_\psi$ the hypercharge of the multiplet $\psi$ ($Q$: $\frac16$, $u_R$: $\frac23$, $d_R$: $-\frac13$, $\ell$: $-\frac12$, $e_R$: $-1$, $\nu_R$: 0). Unit: dimensionless. Status: STANDARD.
- $B_M,\ B_{MN}$: The hypercharge gauge field U(1)$_Y$ (geometric normalisation) and its field strength. Unit: GeV (field), $\mathrm{GeV}^{2}$ (field strength). Status: ASSUMED.
- $Q_{\mathrm{em}}$: The electric charge in units of the elementary charge, $Q_{\mathrm{em}} = T_3 + Y$; $Q^f_{\mathrm{em}}$ that of the fermion $f$. Unit: dimensionless. Status: STANDARD.
- $T_3$: The third component of the weak isospin ($+\frac12$ for the upper and $-\frac12$ for the lower member of a doublet, 0 for a singlet); $T_3^f$ that of the fermion $f$. Unit: dimensionless. Status: STANDARD.

<!-- end generated symbol list -->

**Origin (STANDARD).** The covariant derivative of the Standard Model with the spin connection; the electric charge
$Q_{\mathrm{em}} = T_3 + Y$ in every generation (`um2_electroweak.py`, checks `electric_charges`, `photon_coupling`,
`Z_coupling`).

## IN-13: the tip sigma field and the tip Yukawa couplings (no Higgs particle)

$$
\begin{aligned}
S_{\mathrm{tip}} &= \int_{y=-L}\mathrm{d}^7X_{\mathrm{tip}}\sqrt{\lvert g_{\mathrm{tip}}\rvert}\,\Big[
 -\frac{v_\Sigma^2}{4}\,\mathrm{tr}\big((D_\mu\Sigma)^\dagger D^\mu\Sigma\big) -
 \mathcal{L}_{\mathrm{Y}}\Big],\\
\mathcal{L}_{\mathrm{Y}} &=
 \sum_{i,j=1}^{3}\Big[\bar\ell_i\,\Sigma\begin{pmatrix}(\mathcal{Y}_\nu)_{ij}\,\nu_{Rj}\\
 (\mathcal{Y}_e)_{ij}\,e_{Rj}\end{pmatrix}
 + \bar Q_i\,\Sigma\begin{pmatrix}(\mathcal{Y}_u)_{ij}\,u_{Rj}\\ (\mathcal{Y}_d)_{ij}\,d_{Rj}
 \end{pmatrix}\Big]
 + \text{h.c.}
\end{aligned} \tag{IN-13}
$$

<!-- symbols: Stip, ycoord, Lcut, diff, Xtip, gtip, vSigma, trace, Dcov, imu, Sigma, dagger, LYuk, ii, ij, ldoublet, Yuk, nuR, eR, Qdoublet, uR, dR -->
<!-- begin generated symbol list -->
**Symbols in (IN-13).**

- $S_{\mathrm{tip}}$: The action on the tip $y = -L$: the sigma field and the tip Yukawa couplings. Unit: dimensionless. Status: INVENTED.
- $y$: The hidden coordinate of the $y$ chart, $y = \ln\lvert\sin z\rvert/(6H)$, with $y = 0$ at the fold ($z = \pi/2$) and $y = -L$ at the regular tip; each half of a period of $x_0$ is the interval $-L \le y \le 0$. Unit: length. Status: DERIVED.
- $L$: The depth of the regular tip: each half of a period of $x_0$ ends at $y = -L$; $HL = 3$. Unit: length. Value: $L = 3/H$ ($fL = 8.926\times10^{-21}$ m at the stabilised block). Status: ASSUMED.
- $\mathrm{d}$: The differential: $\mathrm{d}X$ is an infinitesimal change of $X$, $\mathrm{d}X/\mathrm{d}Y$ the derivative of $X$ with respect to $Y$, $\mathrm{d}^nX$ the volume element of $n$ variables. Status: STANDARD.
- $X_{\mathrm{tip}}$: The seven coordinates $x_1, \dots, x_7$ of the tip $y = -L$ of the hidden direction; $\mathrm{d}^7X_{\mathrm{tip}}$ is their coordinate volume element. Unit: length (each coordinate). Status: DERIVED.
- $g_{\mathrm{tip}}$: The metric induced on the seven-dimensional tip $y = -L$ (the metric $g_{MN}$ restricted to the tip directions $x_1, \dots, x_7$); $\lvert g_{\mathrm{tip}}\rvert$ is the absolute value of its determinant. Unit: dimensionless. Status: DERIVED.
- $v_\Sigma$: The scale of the tip sigma field (its kinetic term is $-\frac{v_\Sigma^2}{4}\mathrm{tr}((D_\mu\Sigma)^\dagger D^\mu\Sigma)$); on the static block it fixes the Robin parameter $\beta_{\mathrm{W}}$. Unit: $\mathrm{GeV}^{5/2}$. Value: fixed through $\beta_{\mathrm{W}} = 0.011912$. Status: INVENTED.
- $\mathrm{tr}$: The trace of a matrix: the sum of its diagonal entries. Status: STANDARD.
- $D_M,\ D_\mu$: The covariant derivative: on a spinor $D_M = \partial_M + \Omega_M$ (spin connection), on a Standard-Model fermion with the gauge fields added; on the sigma field $D_\mu\Sigma$ with the $W$ and $B$ fields. Unit: 1/length. Status: STANDARD.
- $\mu$: A four-dimensional coordinate index running over the observable coordinates $x_1, x_2, x_3, x_4$ (signature $+,+,+,-$); on the tip it runs over the tip directions; a repeated index is summed. Status: STANDARD.
- $\Sigma$: The tip sigma field: a unitary $2 \times 2$ matrix field on the tip ($\Sigma^\dagger\Sigma = \mathbf{1}$) that replaces the Higgs doublet; its three modes are the longitudinal $W^+$, $W^-$ and $Z$, and $\Sigma = \mathbf{1}$ is the unitary gauge. Unit: dimensionless. Status: INVENTED.
- ${}^\dagger$: Hermitian conjugation: the complex conjugate of the transpose of a matrix or spinor (for field operators the adjoint operator). Status: STANDARD.
- $\mathcal{L}_{\mathrm{Y}}$: The tip Yukawa Lagrangian: the couplings of the doublets to the singlets through the sigma field and the tip matrices $\mathcal{Y}$ (plus the Hermitian conjugate, h.c.). Unit: $\mathrm{GeV}^{7}$. Status: INVENTED.
- $i$: The generation index ($i = 1, 2, 3$), which also labels the neutrino mass states $\nu_1, \nu_2, \nu_3$; a repeated index is not summed unless a sum sign is written. Status: STANDARD.
- $j$: A second generation index ($j = 1, 2, 3$). Status: STANDARD.
- $\ell_i,\ \bar\ell_i$: The lepton doublet of the generation $i$ (left-handed neutrino and charged lepton) and its Dirac adjoint. Unit: $\mathrm{GeV}^{7/2}$. Status: ASSUMED.
- $\mathcal{Y}_\nu,\ \mathcal{Y}_e,\ \mathcal{Y}_u,\ \mathcal{Y}_d$: The complex $3 \times 3$ tip Yukawa matrices of the neutrino, charged-lepton, up-quark and down-quark sectors (generation indices $i, j$); on the static block they become the tip mixing matrices $\mathcal{K}$ (the normalisation of that relation is not fixed: OPEN). Unit: dimensionless. Status: INVENTED.
- $\nu_R,\ \nu_{Ri}$: The right-handed neutrino (a gauge singlet): $\nu_R$ the multiplet, $\nu_{Ri}$ that of the generation $i$; its zero modes give Dirac neutrino masses. Unit: $\mathrm{GeV}^{7/2}$. Status: ASSUMED.
- $e_R,\ e_{Ri}$: The right-handed charged-lepton singlet: $e_R$ the multiplet, $e_{Ri}$ that of the generation $i$ ($e_R$, $\mu_R$, $\tau_R$). Unit: $\mathrm{GeV}^{7/2}$. Status: ASSUMED.
- $Q_i,\ \bar Q_i$: The quark doublet of the generation $i$ (left-handed up and down quark of one generation, three colours) and its Dirac adjoint. Unit: $\mathrm{GeV}^{7/2}$. Status: ASSUMED.
- $u_R,\ u_{Ri},\ \bar u_{Ri}$: The up-type quark singlet: $u_R$ the multiplet, $u_{Ri}$ that of the generation $i$ ($u_R$, $c_R$, $t_R$), $\bar u_{Ri}$ its Dirac adjoint. Unit: $\mathrm{GeV}^{7/2}$. Status: ASSUMED.
- $d_R,\ d_{Ri},\ \bar d_{Ri}$: The down-type quark singlet: $d_R$ the multiplet, $d_{Ri}$ that of the generation $i$ ($d_R$, $s_R$, $b_R$), $\bar d_{Ri}$ its Dirac adjoint. Unit: $\mathrm{GeV}^{7/2}$. Status: ASSUMED.

<!-- end generated symbol list -->

**Origin (INVENTED for this geometry).** *Reason.* The orders exclude the Higgs particle, but $W^+$, $W^-$ and $Z$ are massive
and the quarks and leptons need their masses and mixing. UM-2 breaks the electroweak symmetry without a Higgs particle by a
unitary sigma field $\Sigma$ ($\Sigma^\dagger\Sigma = \mathbf{1}$: three Goldstone modes, which become the longitudinal
$W^+$, $W^-$ and $Z$, and no physical scalar) that lives only on the tip $y = -L$ of the $x_0$ cell. The concepts of
symmetry breaking by a non-linear sigma field and of fermion localisation in an extra dimension are STANDARD; their
realisation in this geometry is INVENTED. The tip Yukawa couplings $\mathcal{Y}_\nu$, $\mathcal{Y}_e$, $\mathcal{Y}_u$,
$\mathcal{Y}_d$ couple the doublets and the singlets at the tip; on the zero modes they become the tip mixing conditions
FE-30, whose tip matrices are the PMNS and the CKM matrices (ASSUMED values). *Consistency with the electroweak model and
QCD.* Every tip term is invariant under $SU(2)_L\times U(1)_Y$ for arbitrary complex tip matrices (DERIVED with random group
elements, deviation $1.1\times10^{-14}$: `um2_fields.py`, check `tip_terms_gauge_invariant`) and is a colour singlet; the
custodial symmetry of the sigma-field term gives $\rho_{\mathrm{EW}} = 1$ at leading order (`um2_spectra.py`, check
`custodial_leading_order`); the photon receives no tip term (IN-15). *Conflicts with data* (inherent in the specified
content, stated in every version): there is no Higgs boson, while one is observed at 125 GeV; without it the scattering of
longitudinal $W^+$ and $W^-$ violates perturbative unitarity near 1.2 TeV, far below the Kaluza-Klein scale of 121 TeV.

## IN-14: the covariant derivative of the sigma field and its gauge transformation

$$
D_\mu\Sigma = \partial_\mu\Sigma - \mathrm{i}W^I_\mu\,\frac{\tau^I}{2}\,\Sigma +
 \mathrm{i}B_\mu\,\Sigma\,\frac{\tau^3}{2},\qquad
\Sigma^\dagger\Sigma = \mathbf{1},\qquad \Sigma \to U_L\,\Sigma\,U_Y^\dagger,\qquad
U_Y = \mathrm{e}^{\mathrm{i}\vartheta\tau^3/2} \tag{IN-14}
$$

<!-- symbols: Dcov, imu, Sigma, partial, imag, Wsu2, iI, tau, Bhyp, dagger, identity, UL, UY, euler, vartheta -->
<!-- begin generated symbol list -->
**Symbols in (IN-14).**

- $D_M,\ D_\mu$: The covariant derivative: on a spinor $D_M = \partial_M + \Omega_M$ (spin connection), on a Standard-Model fermion with the gauge fields added; on the sigma field $D_\mu\Sigma$ with the $W$ and $B$ fields. Unit: 1/length. Status: STANDARD.
- $\mu$: A four-dimensional coordinate index running over the observable coordinates $x_1, x_2, x_3, x_4$ (signature $+,+,+,-$); on the tip it runs over the tip directions; a repeated index is summed. Status: STANDARD.
- $\Sigma$: The tip sigma field: a unitary $2 \times 2$ matrix field on the tip ($\Sigma^\dagger\Sigma = \mathbf{1}$) that replaces the Higgs doublet; its three modes are the longitudinal $W^+$, $W^-$ and $Z$, and $\Sigma = \mathbf{1}$ is the unitary gauge. Unit: dimensionless. Status: INVENTED.
- $\partial$: A partial derivative: $\partial_M$ is the derivative with respect to the coordinate $X^M$, $\partial_y$ with respect to $y$, $\partial_{x_4}$ with respect to the time $x_4$, $\partial X/\partial Y$ the derivative of $X$ with respect to $Y$ at fixed other variables. Status: STANDARD.
- $\mathrm{i}$: The imaginary unit, $\mathrm{i}^2 = -1$. Unit: dimensionless. Status: STANDARD.
- $W^I_M,\ W_M,\ W_{MN},\ W^I_{MN}$: The SU(2) gauge field (geometric normalisation): the components $W^I_M$ ($I = 1, 2, 3$; $W^3$ the third component), the matrix $W_M = W^I_M\tau^I/2$, the field strength $W_{MN}$ and its components $W^I_{MN}$; with Greek indices the components along the observable directions. Unit: GeV (field), $\mathrm{GeV}^{2}$ (field strength). Status: ASSUMED.
- $I$: A weak-isospin (adjoint SU(2)) index running over $1, 2, 3$; a repeated index is summed. Status: STANDARD.
- $\tau^I$: The Pauli matrices acting on weak-isospin doublets ($\tau^I/2$ the generators of SU(2); $\tau^3 = \mathrm{diag}(1, -1)$). Unit: dimensionless. Status: STANDARD.
- $B_M,\ B_{MN}$: The hypercharge gauge field U(1)$_Y$ (geometric normalisation) and its field strength. Unit: GeV (field), $\mathrm{GeV}^{2}$ (field strength). Status: ASSUMED.
- ${}^\dagger$: Hermitian conjugation: the complex conjugate of the transpose of a matrix or spinor (for field operators the adjoint operator). Status: STANDARD.
- $\mathbf{1}$: The identity matrix (of the size fixed by the context: 16 x 16 on spinors, 3 x 3 on the generations or flavours, 2 x 2 for the sigma field). Unit: dimensionless. Status: STANDARD.
- $U_L$: An SU(2) gauge transformation (a unitary $2 \times 2$ matrix acting on doublets from the left). Unit: dimensionless. Status: STANDARD.
- $U_Y$: A U(1)$_Y$ gauge transformation of the sigma field, $U_Y = \mathrm{e}^{\mathrm{i}\vartheta\tau^3/2}$. Unit: dimensionless. Status: STANDARD.
- $\mathrm{e}$: Euler's number, the base of the natural logarithm; $\mathrm{e}^{X}$ is the exponential of $X$. Unit: dimensionless. Value: 2.718281828. Status: STANDARD.
- $\vartheta$: The angle (gauge parameter) of a U(1)$_Y$ transformation. Unit: dimensionless. Status: STANDARD.

<!-- end generated symbol list -->

**Origin (INVENTED).** The covariant derivative of the sigma field with the gauge transformations of the electroweak model
($U_L$ an $SU(2)_L$ matrix, $U_Y$ the hypercharge rotation by the angle $\vartheta$); with it every tip term is gauge
invariant (DERIVED, as for IN-13; the hypercharge phase of a fermion is $\psi \to \mathrm{e}^{\mathrm{i}Y\vartheta}\psi$,
corrections, item 1).

## IN-15: the tip mass term of $W^+$, $W^-$ and $Z$

$$
-\frac{v_\Sigma^2}{4}\,\mathrm{tr}\big((D_\mu\Sigma)^\dagger D^\mu\Sigma\big)\Big\vert_{\Sigma = \mathbf{1}}
= -\frac{v_\Sigma^2}{8}\Big[2\hat g_2^2\,W^+_\mu W^-{}^\mu + \hat g_Z^2\,Z_\mu Z^\mu\Big] \tag{IN-15}
$$

<!-- symbols: vSigma, trace, Dcov, imu, Sigma, dagger, identity, ghat2, Wpm, ghatZ, Zboson -->
<!-- begin generated symbol list -->
**Symbols in (IN-15).**

- $v_\Sigma$: The scale of the tip sigma field (its kinetic term is $-\frac{v_\Sigma^2}{4}\mathrm{tr}((D_\mu\Sigma)^\dagger D^\mu\Sigma)$); on the static block it fixes the Robin parameter $\beta_{\mathrm{W}}$. Unit: $\mathrm{GeV}^{5/2}$. Value: fixed through $\beta_{\mathrm{W}} = 0.011912$. Status: INVENTED.
- $\mathrm{tr}$: The trace of a matrix: the sum of its diagonal entries. Status: STANDARD.
- $D_M,\ D_\mu$: The covariant derivative: on a spinor $D_M = \partial_M + \Omega_M$ (spin connection), on a Standard-Model fermion with the gauge fields added; on the sigma field $D_\mu\Sigma$ with the $W$ and $B$ fields. Unit: 1/length. Status: STANDARD.
- $\mu$: A four-dimensional coordinate index running over the observable coordinates $x_1, x_2, x_3, x_4$ (signature $+,+,+,-$); on the tip it runs over the tip directions; a repeated index is summed. Status: STANDARD.
- $\Sigma$: The tip sigma field: a unitary $2 \times 2$ matrix field on the tip ($\Sigma^\dagger\Sigma = \mathbf{1}$) that replaces the Higgs doublet; its three modes are the longitudinal $W^+$, $W^-$ and $Z$, and $\Sigma = \mathbf{1}$ is the unitary gauge. Unit: dimensionless. Status: INVENTED.
- ${}^\dagger$: Hermitian conjugation: the complex conjugate of the transpose of a matrix or spinor (for field operators the adjoint operator). Status: STANDARD.
- $\mathbf{1}$: The identity matrix (of the size fixed by the context: 16 x 16 on spinors, 3 x 3 on the generations or flavours, 2 x 2 for the sigma field). Unit: dimensionless. Status: STANDARD.
- $\hat g_2$: The eight-dimensional SU(2) coupling; $g_2^2 = \hat g_2^2/V_\perp$. Unit: $\mathrm{GeV}^{-2}$. Status: ASSUMED.
- $W^\pm_M,\ W^+,\ W^-$: The charged weak bosons, canonically normalised: $W^\pm_M = (W^1_M \mp \mathrm{i}W^2_M)/(\sqrt2\,\hat g_2)$; $W^+$ carries the electric charge $+e$ and $W^-$ the charge $-e$ (they are each other's antiparticles and have one mass). Unit: $\mathrm{GeV}^{3}$. Status: STANDARD.
- $\hat g_Z$: The eight-dimensional coupling of the $Z$, $\hat g_Z = (\hat g_2^2 + \hat g_1^2)^{1/2}$. Unit: $\mathrm{GeV}^{-2}$. Status: STANDARD.
- $Z_M$: The $Z$ boson field, canonically normalised, $Z_M = (W^3_M - B_M)/\hat g_Z$. Unit: $\mathrm{GeV}^{3}$. Status: STANDARD.

<!-- end generated symbol list -->

**Origin (DERIVED).** The sigma-field term of IN-13 in the unitary gauge: $W^+$ and $W^-$ share one mass (particle and
antiparticle), and the photon, the combination without a tip term, stays massless. On the static block the term becomes
the Robin condition FE-51 of the boson profiles (`um2_fields.py`, check `gauge_boundary_conditions`; `um2_spectra.py`,
checks `rho_fit`, `mZ_reproduced`). Its sign is that of the signature $(+,+,+,-)$ of $x_1, \dots, x_4$ (corrections, item 12).

## IN-16: portal I11, the vector contact portal to the $B - L$ currents

$$
\begin{aligned}
S_{\mathrm{I11}} &= \int\mathrm{d}^8X\,\sqrt{\lvert g\rvert}\;\frac{c_{\mathrm{V}}}{\Lambda_\star^6}\,
 \big(\mathrm{i}\bar\Psi\gamma^M\Psi\big)\,J^{B-L}_M,\qquad
 J^{B-L}_M = \sum_{i=1}^{3}\sum_{\psi} q_\psi\,\big(\mathrm{i}\bar\psi_i\gamma_M\psi_i\big),\\
q_Q &= q_{u_R} = q_{d_R} = \frac13,\qquad q_\ell = q_{e_R} = q_{\nu_R} = -1
\end{aligned} \tag{IN-16}
$$

<!-- symbols: SI11, diff, Xcoord, metric, cV, LambdaStar, imag, Psi, gamma, iM, JBL, ii, ipsi, qBL, psi -->
<!-- begin generated symbol list -->
**Symbols in (IN-16).**

- $S_{\mathrm{I11}}$: The action of the portal I11 (dirac16complex vector current times the $B - L$ current of the fermions). Unit: dimensionless. Status: INVENTED.
- $\mathrm{d}$: The differential: $\mathrm{d}X$ is an infinitesimal change of $X$, $\mathrm{d}X/\mathrm{d}Y$ the derivative of $X$ with respect to $Y$, $\mathrm{d}^nX$ the volume element of $n$ variables. Status: STANDARD.
- $X = \{x_0, \dots, x_7\}$: The author's coordinates of the eight-dimensional spacetime, $X = \{x_0, x_1, \dots, x_7\}$ with the hidden direction first; $X^M$ is the coordinate with the index $M$, $\mathrm{d}^8X = \mathrm{d}x_0\,\mathrm{d}x_1\cdots\mathrm{d}x_7$ the coordinate volume element and $X^\mu$ (four-dimensional index $\mu$) the observable coordinates $x_1, \dots, x_4$. Unit: length (each coordinate). Status: AUTHOR.
- $g_{MN}$: The metric tensor of the eight-dimensional spacetime (signature $+,+,+,+,-,-,-,-$ in the order $x_0, \dots, x_7$): $g_{MN}\,\mathrm{d}X^M\mathrm{d}X^N$ is the squared interval; $g^{MN}$ is its inverse, $g^M{}_N = \delta^M_N$, and $\lvert g\rvert$ the absolute value of its determinant, so that $\sqrt{\lvert g\rvert}\,\mathrm{d}^8X$ is the proper volume element. Unit: dimensionless. Status: AUTHOR.
- $c_{\mathrm{V}}$: The coefficient of the vector portal I11. Unit: dimensionless. Value: benchmark through $G_{\mathrm{V}} = 4.38\times10^{-17}$ GeV$^{-2}$. Status: INVENTED.
- $\Lambda_\star$: The scale of the portal operators I11, I12, I13. Unit: GeV. Value: only the combinations $c/\Lambda_\star^n$ enter. Status: INVENTED.
- $\mathrm{i}$: The imaginary unit, $\mathrm{i}^2 = -1$. Unit: dimensionless. Status: STANDARD.
- $\Psi,\ \bar\Psi$: dirac16complex: the 16-component complex spinor field of eight dimensions of the record (the author's field), the source of the dark matter (its lowest odd level) and of the massless fold bands; $\bar\Psi = \Psi^\dagger C$ is its Dirac adjoint. Unit: $\mathrm{GeV}^{7/2}$. Status: RECORD.
- $\gamma^a,\ \gamma^M,\ \gamma^\mu$: The Dirac matrices: $\gamma^a$ with a frame index are the author's real $16 \times 16$ matrices of the Clifford algebra of signature $(4, 4)$; $\gamma^M = \mathbf{e}_a{}^M\gamma^a$ along a coordinate ($\gamma^{x_0}$, $\gamma^{x_4}$, ... the matrices along $x_0$, $x_4$, ...), $\gamma_M = g_{MN}\gamma^N$; $\gamma^\mu$ the matrices of the four observable directions in four-dimensional formulas. Unit: dimensionless. Status: AUTHOR.
- $M$: A coordinate index of eight dimensions (also with a numbered copy $M_1, M_2, \dots$): it runs over $x_0, x_1, \dots, x_7$; a repeated index is summed. Status: STANDARD.
- $J^{B-L}_M$: The $B - L$ current of the Standard-Model fermions (baryon minus lepton number), summed over the generations. Unit: $\mathrm{GeV}^{7}$. Status: STANDARD.
- $i$: The generation index ($i = 1, 2, 3$), which also labels the neutrino mass states $\nu_1, \nu_2, \nu_3$; a repeated index is not summed unless a sum sign is written. Status: STANDARD.
- $\psi$: The label of a Standard-Model multiplet: $\psi \in \{Q, u_R, d_R, \ell, e_R, \nu_R\}$ (quark doublet, up and down quark singlets, lepton doublet, charged-lepton singlet, right-handed neutrino); a sum over $\psi$ runs over the six. Status: STANDARD.
- $q_\psi,\ q_f$: The $B - L$ charge: $q_\psi$ of the multiplet $\psi$ ($q_Q = q_{u_R} = q_{d_R} = \frac13$, $q_\ell = q_{e_R} = q_{\nu_R} = -1$), $q_f$ of the fermion component $f$. Unit: dimensionless. Status: STANDARD.
- $\psi_i,\ \bar\psi_i$: A Standard-Model fermion field of eight dimensions: $\psi_i$ is the multiplet $\psi \in \{Q, u_R, d_R, \ell, e_R, \nu_R\}$ of the generation $i$, $\psi_f$ one fermion component $f$ (in four-dimensional formulas its zero mode); $\bar\psi = \psi^\dagger C$ the Dirac adjoint. Unit: $\mathrm{GeV}^{7/2}$ (eight dimensions), $\mathrm{GeV}^{3/2}$ (four dimensions). Status: ASSUMED.

<!-- end generated symbol list -->

**Origin (INVENTED; version 1, with its charges fixed in version 3).** *Reason.* A contact coupling of the conserved vector
current of the gauge-singlet field $\Psi$ to a gauge-invariant conserved current of all quarks and leptons, so that
dirac16complex feels every Standard-Model fermion. *Consistency with QCD and the electroweak model.* Both currents are singlets
of $SU(3)_c\times SU(2)_L\times U(1)_Y$; the $B - L$ charge is flavour universal and conserved by every interaction of the
Standard Model (STANDARD; with the right-handed neutrinos it is free of anomalies), so the portal breaks no gauge symmetry and
leaves the Standard-Model interactions unchanged; the currents are the Hermitian currents $\mathrm{i}\bar\Psi\gamma^M\Psi$ and
$\mathrm{i}\bar\psi\gamma_M\psi$ (corrections, item 13). Its effects on the Standard Model are mean fields of relative size
$10^{-17}$ at most in the fermion equations FE-14 to FE-19. *Strength.* On the zero modes it is the contact interaction FE-70
with $G_{\mathrm{V}} = c_{\mathrm{V}}H/(2f^4v_{\mathrm{t}}\Lambda_\star^6)$, set to the benchmark
$G_{\mathrm{V}} = 4.38\times10^{-17}$ GeV$^{-2}$, at which the freeze-in of the fold bands from the highest temperature
$T_{\mathrm{max}} = 10$ TeV adds $\Delta N_{\mathrm{eff}} = 0.001$ (both ASSUMED; FE-129). Version 2 had left the charges
general and set $c_{\mathrm{V}} = 0$.

## IN-17: portal I12, the gauge-kinetic scalar portal

$$
S_{\mathrm{I12}} = -\int\mathrm{d}^8X\,\sqrt{\lvert
 g\rvert}\;\frac{\bar\Psi\Psi}{\Lambda_\star^3}\,\mathcal{F},\qquad
\mathcal{F} = c_{\mathrm{G}}\,G^A_{MN}G^{AMN} + c_{\mathrm{W}}\,W^I_{MN}W^{IMN} +
 c_{\mathrm{B}}\,B_{MN}B^{MN} \tag{IN-17}
$$

<!-- symbols: SI12, diff, Xcoord, metric, Psi, LambdaStar, calF, cG, Ggluon, iA, iM, iN, cW, Wsu2, iI, cB, Bhyp -->
<!-- begin generated symbol list -->
**Symbols in (IN-17).**

- $S_{\mathrm{I12}}$: The action of the portal I12 (scalar density of dirac16complex times the gauge kinetic invariants). Unit: dimensionless. Status: INVENTED.
- $\mathrm{d}$: The differential: $\mathrm{d}X$ is an infinitesimal change of $X$, $\mathrm{d}X/\mathrm{d}Y$ the derivative of $X$ with respect to $Y$, $\mathrm{d}^nX$ the volume element of $n$ variables. Status: STANDARD.
- $X = \{x_0, \dots, x_7\}$: The author's coordinates of the eight-dimensional spacetime, $X = \{x_0, x_1, \dots, x_7\}$ with the hidden direction first; $X^M$ is the coordinate with the index $M$, $\mathrm{d}^8X = \mathrm{d}x_0\,\mathrm{d}x_1\cdots\mathrm{d}x_7$ the coordinate volume element and $X^\mu$ (four-dimensional index $\mu$) the observable coordinates $x_1, \dots, x_4$. Unit: length (each coordinate). Status: AUTHOR.
- $g_{MN}$: The metric tensor of the eight-dimensional spacetime (signature $+,+,+,+,-,-,-,-$ in the order $x_0, \dots, x_7$): $g_{MN}\,\mathrm{d}X^M\mathrm{d}X^N$ is the squared interval; $g^{MN}$ is its inverse, $g^M{}_N = \delta^M_N$, and $\lvert g\rvert$ the absolute value of its determinant, so that $\sqrt{\lvert g\rvert}\,\mathrm{d}^8X$ is the proper volume element. Unit: dimensionless. Status: AUTHOR.
- $\Psi,\ \bar\Psi$: dirac16complex: the 16-component complex spinor field of eight dimensions of the record (the author's field), the source of the dark matter (its lowest odd level) and of the massless fold bands; $\bar\Psi = \Psi^\dagger C$ is its Dirac adjoint. Unit: $\mathrm{GeV}^{7/2}$. Status: RECORD.
- $\Lambda_\star$: The scale of the portal operators I11, I12, I13. Unit: GeV. Value: only the combinations $c/\Lambda_\star^n$ enter. Status: INVENTED.
- $\mathcal{F}$: The gauge-kinetic operator of the portal I12, $\mathcal{F} = c_{\mathrm{G}}G^A_{MN}G^{AMN} + c_{\mathrm{W}}W^I_{MN}W^{IMN} + c_{\mathrm{B}}B_{MN}B^{MN}$; $\langle\mathcal{F}\rangle$ its mean value in an environment. Unit: $\mathrm{GeV}^{4}$. Status: INVENTED.
- $c_{\mathrm{G}}$: The coefficient of the gluon term of the portal I12. Unit: dimensionless. Value: $c_{\mathrm{G}}/\Lambda_\star^3 = c_{\mathrm{I12}}/\Lambda_\star^3$. Status: INVENTED.
- $G^A_M,\ G_M,\ G_{MN},\ G^A_{MN}$: The gluon field (SU(3)), in the geometric normalisation of the action (couplings in front of the kinetic terms): the components $G^A_M$ ($A = 1, \dots, 8$), the matrix $G_M = G^A_Mt^A$, the field strength $G_{MN}$ (matrix) and its components $G^A_{MN}$; $G^A_{\mu\nu}$ are its components along the observable directions (the zero mode, flat in $x_0$). Unit: GeV (field), $\mathrm{GeV}^{2}$ (field strength). Status: ASSUMED.
- $A$: A colour (adjoint SU(3)) index running over $1, \dots, 8$; a repeated index is summed. Status: STANDARD.
- $M$: A coordinate index of eight dimensions (also with a numbered copy $M_1, M_2, \dots$): it runs over $x_0, x_1, \dots, x_7$; a repeated index is summed. Status: STANDARD.
- $N$: A coordinate index of eight dimensions (also $N_1, N_2, \dots$), running over $x_0, \dots, x_7$; a repeated index is summed. Status: STANDARD.
- $c_{\mathrm{W}}$: The coefficient of the SU(2) term of the portal I12. Unit: dimensionless. Value: $c_{\mathrm{W}}/\Lambda_\star^3 = c_{\mathrm{I12}}/\Lambda_\star^3$. Status: INVENTED.
- $W^I_M,\ W_M,\ W_{MN},\ W^I_{MN}$: The SU(2) gauge field (geometric normalisation): the components $W^I_M$ ($I = 1, 2, 3$; $W^3$ the third component), the matrix $W_M = W^I_M\tau^I/2$, the field strength $W_{MN}$ and its components $W^I_{MN}$; with Greek indices the components along the observable directions. Unit: GeV (field), $\mathrm{GeV}^{2}$ (field strength). Status: ASSUMED.
- $I$: A weak-isospin (adjoint SU(2)) index running over $1, 2, 3$; a repeated index is summed. Status: STANDARD.
- $c_{\mathrm{B}}$: The coefficient of the hypercharge term of the portal I12. Unit: dimensionless. Value: $c_{\mathrm{B}}/\Lambda_\star^3 = c_{\mathrm{I12}}/\Lambda_\star^3$. Status: INVENTED.
- $B_M,\ B_{MN}$: The hypercharge gauge field U(1)$_Y$ (geometric normalisation) and its field strength. Unit: GeV (field), $\mathrm{GeV}^{2}$ (field strength). Status: ASSUMED.

<!-- end generated symbol list -->

**Origin (INVENTED; version 1).** *Reason.* The coupling of the scalar density $\bar\Psi\Psi$ to the gauge-invariant kinetic
densities of the gluons and of the electroweak fields: the gauge-singlet field couples to the gauge bosons of all three
groups, its density makes the gauge couplings field dependent (FE-21), and the dark matter can annihilate into gauge bosons.
*Consistency with QCD and the electroweak model.* $G^A_{MN}G^{AMN}$, $W^I_{MN}W^{IMN}$ and $B_{MN}B^{MN}$ are gauge invariant
(the first is the operator of the QCD trace anomaly), so the portal preserves $SU(3)_c\times SU(2)_L\times U(1)_Y$ and keeps
the photon and the gluons exactly massless (`um2_coupled.py`, check `C5_WZ_and_photon`); the shifts of the couplings are at
most $1.7\times10^{-16}$ (FE-79). The power of the scale is $\Lambda_\star^3$ in the geometric normalisation (corrections,
item 10). *Strength.* The unitarity-safe benchmark $G_{\mathrm{I12}} = \pi/(2M_{\mathrm{DM}}^3)$ with the universal
coefficients $c_{\mathrm{G}} = c_{\mathrm{W}} = c_{\mathrm{B}} = c_{\mathrm{I12}}$ (ASSUMED; FE-127, FE-128). Version 2 found
that I12 alone cannot give the relic abundance within perturbative unitarity, because the operator annihilates a pair only
from the state $^3P_0$ (corrections, item 22); this led to I13.

## IN-18: portal I13, the $x_0$-chiral vector portal to the baryon-number current

$$
\begin{aligned}
S_{\mathrm{I13}} &= \int\mathrm{d}^8X\,\sqrt{\lvert g\rvert}\;\frac{c_{\mathrm{A}}}{\Lambda_\star^6}
 \sum_{M\ne x_0}\big(\mathrm{i}\bar\Psi\gamma^MP_b\Psi\big)\,J^{B}_M,\qquad P_b = \frac{1 - \gamma^{x_0}}{2},
 \qquad P_a = \frac{1 + \gamma^{x_0}}{2},\\
J^{B}_M &= \frac13\sum_{i=1}^{3}\big(\mathrm{i}\bar Q_i\gamma_MQ_i + \mathrm{i}\bar u_{Ri}\gamma_Mu_{Ri}
 + \mathrm{i}\bar d_{Ri}\gamma_Md_{Ri}\big)
\end{aligned} \tag{IN-18}
$$

<!-- symbols: SI13, diff, Xcoord, metric, cA, LambdaStar, iM, x0, imag, Psi, gamma, Pab, JB, ii, Qdoublet, uR, dR -->
<!-- begin generated symbol list -->
**Symbols in (IN-18).**

- $S_{\mathrm{I13}}$: The action of the portal I13 (the $x_0$-chiral vector current of dirac16complex times the baryon-number current). Unit: dimensionless. Status: INVENTED.
- $\mathrm{d}$: The differential: $\mathrm{d}X$ is an infinitesimal change of $X$, $\mathrm{d}X/\mathrm{d}Y$ the derivative of $X$ with respect to $Y$, $\mathrm{d}^nX$ the volume element of $n$ variables. Status: STANDARD.
- $X = \{x_0, \dots, x_7\}$: The author's coordinates of the eight-dimensional spacetime, $X = \{x_0, x_1, \dots, x_7\}$ with the hidden direction first; $X^M$ is the coordinate with the index $M$, $\mathrm{d}^8X = \mathrm{d}x_0\,\mathrm{d}x_1\cdots\mathrm{d}x_7$ the coordinate volume element and $X^\mu$ (four-dimensional index $\mu$) the observable coordinates $x_1, \dots, x_4$. Unit: length (each coordinate). Status: AUTHOR.
- $g_{MN}$: The metric tensor of the eight-dimensional spacetime (signature $+,+,+,+,-,-,-,-$ in the order $x_0, \dots, x_7$): $g_{MN}\,\mathrm{d}X^M\mathrm{d}X^N$ is the squared interval; $g^{MN}$ is its inverse, $g^M{}_N = \delta^M_N$, and $\lvert g\rvert$ the absolute value of its determinant, so that $\sqrt{\lvert g\rvert}\,\mathrm{d}^8X$ is the proper volume element. Unit: dimensionless. Status: AUTHOR.
- $c_{\mathrm{A}}$: The coefficient of the $x_0$-chiral vector portal I13. Unit: dimensionless. Value: fixed through $G_{\mathrm{A}} = 1.278\times10^{-9}$ GeV$^{-2}$ (dark-matter relic). Status: INVENTED.
- $\Lambda_\star$: The scale of the portal operators I11, I12, I13. Unit: GeV. Value: only the combinations $c/\Lambda_\star^n$ enter. Status: INVENTED.
- $M$: A coordinate index of eight dimensions (also with a numbered copy $M_1, M_2, \dots$): it runs over $x_0, x_1, \dots, x_7$; a repeated index is summed. Status: STANDARD.
- $x_0$: The hidden space-like coordinate (listed first); the metric depends on it through $z = 6Hx_0$, periodically with the period $\pi/(6H)$. Unit: length. Status: AUTHOR.
- $\mathrm{i}$: The imaginary unit, $\mathrm{i}^2 = -1$. Unit: dimensionless. Status: STANDARD.
- $\Psi,\ \bar\Psi$: dirac16complex: the 16-component complex spinor field of eight dimensions of the record (the author's field), the source of the dark matter (its lowest odd level) and of the massless fold bands; $\bar\Psi = \Psi^\dagger C$ is its Dirac adjoint. Unit: $\mathrm{GeV}^{7/2}$. Status: RECORD.
- $\gamma^a,\ \gamma^M,\ \gamma^\mu$: The Dirac matrices: $\gamma^a$ with a frame index are the author's real $16 \times 16$ matrices of the Clifford algebra of signature $(4, 4)$; $\gamma^M = \mathbf{e}_a{}^M\gamma^a$ along a coordinate ($\gamma^{x_0}$, $\gamma^{x_4}$, ... the matrices along $x_0$, $x_4$, ...), $\gamma_M = g_{MN}\gamma^N$; $\gamma^\mu$ the matrices of the four observable directions in four-dimensional formulas. Unit: dimensionless. Status: AUTHOR.
- $P_a,\ P_b$: The projectors on the two $x_0$-chiralities, $P_a = (1 + \gamma^{x_0})/2$ and $P_b = (1 - \gamma^{x_0})/2$ (in a block: the upper and the lower component). Unit: dimensionless. Status: INVENTED.
- $J^{B}_M$: The baryon-number current of the quarks (one third per quark), summed over the generations. Unit: $\mathrm{GeV}^{7}$. Status: STANDARD.
- $i$: The generation index ($i = 1, 2, 3$), which also labels the neutrino mass states $\nu_1, \nu_2, \nu_3$; a repeated index is not summed unless a sum sign is written. Status: STANDARD.
- $Q_i,\ \bar Q_i$: The quark doublet of the generation $i$ (left-handed up and down quark of one generation, three colours) and its Dirac adjoint. Unit: $\mathrm{GeV}^{7/2}$. Status: ASSUMED.
- $u_R,\ u_{Ri},\ \bar u_{Ri}$: The up-type quark singlet: $u_R$ the multiplet, $u_{Ri}$ that of the generation $i$ ($u_R$, $c_R$, $t_R$), $\bar u_{Ri}$ its Dirac adjoint. Unit: $\mathrm{GeV}^{7/2}$. Status: ASSUMED.
- $d_R,\ d_{Ri},\ \bar d_{Ri}$: The down-type quark singlet: $d_R$ the multiplet, $d_{Ri}$ that of the generation $i$ ($d_R$, $s_R$, $b_R$), $\bar d_{Ri}$ its Dirac adjoint. Unit: $\mathrm{GeV}^{7/2}$. Status: ASSUMED.

<!-- end generated symbol list -->

**Origin (INVENTED; version 3).** *Reason.* An s-wave annihilation of the dark matter into quarks, which gives the relic
abundance within partial-wave unitarity (FE-126 to FE-128). The $x_0$-chiral current $\mathrm{i}\bar\Psi\gamma^MP_b\Psi$ was
chosen because it is Hermitian for the seven directions $M \ne x_0$ (for $M = x_0$ the Hermitian conjugate of
$\mathrm{i}C\gamma^{x_0}P_b$ is $\mathrm{i}C\gamma^{x_0}P_a$, so the sum leaves that direction out; corrections, item 24), is
a four-dimensional vector, is diagonal in the halves on the zero modes and vanishes on the fold bands (to
$7\times10^{-14}$), so it cannot produce dark radiation; the baryon-number current was chosen because the $B - L$ current would
thermalise the right-handed neutrinos and add $\Delta N_{\mathrm{eff}} = 0.144$ (FE-131; corrections, item 23). *Consistency
with QCD and the electroweak model.* The baryon current is a colour singlet, flavour universal and invariant under
$SU(2)_L\times U(1)_Y$, and it is conserved in perturbation theory (STANDARD; its electroweak anomaly acts only through
non-perturbative processes); the algebra of the bilinear with the author's matrices is exact (`um2_coupled.py`, check
`C8_I13_algebra`). *Strength.* $G_{\mathrm{A}} = c_{\mathrm{A}}H/(2f^4v_{\mathrm{t}}\Lambda_\star^6) = 1.278\times10^{-9}$
GeV$^{-2}$, DERIVED from $\Omega_{\mathrm{DM}}h_{100}^2 = 0.120$; its physics accuracy is about 1 % (section 10).

## Removed and rejected operators

Removed in version 2 (corrections, item 21): the chiral tip $Z$ portal I9 of version 1,

$$
S_{\mathrm{I9}} = \int_{y=-L}\mathrm{d}^7X_{\mathrm{tip}}\sqrt{\lvert g_{\mathrm{tip}}\rvert}\;
 \big(c_{\mathrm{Z}} + \tilde c_{\mathrm{Z}}\,\varsigma_{\mathrm{t}}\big)\big(\mathrm{i}\bar\Psi\gamma^\mu P_L\Psi\big)\,
 \frac{\mathrm{i}v_\Sigma^2}{2}\,\mathrm{tr}\big(\Sigma^\dagger D_\mu\Sigma\,\tau^3\big),\qquad
c_{\mathrm{Z}} = \tilde c_{\mathrm{Z}} = 0
$$

<!-- symbols: mod_SI9, ycoord, Lcut, diff, Xtip, gtip, mod_cZ, mod_varsigmat, imag, Psi, gamma, imu, PLR, iL, vSigma, trace, Sigma, dagger, Dcov, tau -->
<!-- begin generated symbol list -->
**Symbols in this equation.**

- $S_{\mathrm{I9}}$: The action of the chiral tip $Z$ portal I9 of version 1, which coupled the four-dimensional left-handed current of dirac16complex to the $Z$ part of the current of the tip sigma field; removed from UM-2 in version 2 (its coefficients are set to zero). Unit: dimensionless (an action, $\hbar = 1$). Status: INVENTED (removed).
- $y$: The hidden coordinate of the $y$ chart, $y = \ln\lvert\sin z\rvert/(6H)$, with $y = 0$ at the fold ($z = \pi/2$) and $y = -L$ at the regular tip; each half of a period of $x_0$ is the interval $-L \le y \le 0$. Unit: length. Status: DERIVED.
- $L$: The depth of the regular tip: each half of a period of $x_0$ ends at $y = -L$; $HL = 3$. Unit: length. Value: $L = 3/H$ ($fL = 8.926\times10^{-21}$ m at the stabilised block). Status: ASSUMED.
- $\mathrm{d}$: The differential: $\mathrm{d}X$ is an infinitesimal change of $X$, $\mathrm{d}X/\mathrm{d}Y$ the derivative of $X$ with respect to $Y$, $\mathrm{d}^nX$ the volume element of $n$ variables. Status: STANDARD.
- $X_{\mathrm{tip}}$: The seven coordinates $x_1, \dots, x_7$ of the tip $y = -L$ of the hidden direction; $\mathrm{d}^7X_{\mathrm{tip}}$ is their coordinate volume element. Unit: length (each coordinate). Status: DERIVED.
- $g_{\mathrm{tip}}$: The metric induced on the seven-dimensional tip $y = -L$ (the metric $g_{MN}$ restricted to the tip directions $x_1, \dots, x_7$); $\lvert g_{\mathrm{tip}}\rvert$ is the absolute value of its determinant. Unit: dimensionless. Status: DERIVED.
- $c_{\mathrm{Z}},\ \tilde c_{\mathrm{Z}}$: The coefficients of the removed portal I9: $c_{\mathrm{Z}}$ of its part that is even under the fold reflection, $\tilde c_{\mathrm{Z}}$ of its oriented (odd) part; UM-2 sets both to zero. Unit: $\mathrm{GeV}^{-6}$. Value: 0. Status: ASSUMED.
- $\varsigma_{\mathrm{t}}$: The sign ($+1$ or $-1$) that distinguishes the two sides of a tip (the tips at $z \to 0^+$ and $z \to \pi^-$ of neighbouring periods), used only in the oriented part of the removed portal I9. Unit: dimensionless. Status: INVENTED (removed).
- $\mathrm{i}$: The imaginary unit, $\mathrm{i}^2 = -1$. Unit: dimensionless. Status: STANDARD.
- $\Psi,\ \bar\Psi$: dirac16complex: the 16-component complex spinor field of eight dimensions of the record (the author's field), the source of the dark matter (its lowest odd level) and of the massless fold bands; $\bar\Psi = \Psi^\dagger C$ is its Dirac adjoint. Unit: $\mathrm{GeV}^{7/2}$. Status: RECORD.
- $\gamma^a,\ \gamma^M,\ \gamma^\mu$: The Dirac matrices: $\gamma^a$ with a frame index are the author's real $16 \times 16$ matrices of the Clifford algebra of signature $(4, 4)$; $\gamma^M = \mathbf{e}_a{}^M\gamma^a$ along a coordinate ($\gamma^{x_0}$, $\gamma^{x_4}$, ... the matrices along $x_0$, $x_4$, ...), $\gamma_M = g_{MN}\gamma^N$; $\gamma^\mu$ the matrices of the four observable directions in four-dimensional formulas. Unit: dimensionless. Status: AUTHOR.
- $\mu$: A four-dimensional coordinate index running over the observable coordinates $x_1, x_2, x_3, x_4$ (signature $+,+,+,-$); on the tip it runs over the tip directions; a repeated index is summed. Status: STANDARD.
- $P_L,\ P_R$: The projectors on the four-dimensional chiralities, $P_L = (1 + \Gamma_4)/2$ (left-handed) and $P_R = (1 - \Gamma_4)/2$ (right-handed). Unit: dimensionless. Status: STANDARD.
- $L$: The chirality label L: the left-handed (doublet) zero mode, or the left-handed projection $P_L = (1 + \Gamma_4)/2$. Status: STANDARD.
- $v_\Sigma$: The scale of the tip sigma field (its kinetic term is $-\frac{v_\Sigma^2}{4}\mathrm{tr}((D_\mu\Sigma)^\dagger D^\mu\Sigma)$); on the static block it fixes the Robin parameter $\beta_{\mathrm{W}}$. Unit: $\mathrm{GeV}^{5/2}$. Value: fixed through $\beta_{\mathrm{W}} = 0.011912$. Status: INVENTED.
- $\mathrm{tr}$: The trace of a matrix: the sum of its diagonal entries. Status: STANDARD.
- $\Sigma$: The tip sigma field: a unitary $2 \times 2$ matrix field on the tip ($\Sigma^\dagger\Sigma = \mathbf{1}$) that replaces the Higgs doublet; its three modes are the longitudinal $W^+$, $W^-$ and $Z$, and $\Sigma = \mathbf{1}$ is the unitary gauge. Unit: dimensionless. Status: INVENTED.
- ${}^\dagger$: Hermitian conjugation: the complex conjugate of the transpose of a matrix or spinor (for field operators the adjoint operator). Status: STANDARD.
- $D_M,\ D_\mu$: The covariant derivative: on a spinor $D_M = \partial_M + \Omega_M$ (spin connection), on a Standard-Model fermion with the gauge fields added; on the sigma field $D_\mu\Sigma$ with the $W$ and $B$ fields. Unit: 1/length. Status: STANDARD.
- $\tau^I$: The Pauli matrices acting on weak-isospin doublets ($\tau^I/2$ the generators of SU(2); $\tau^3 = \mathrm{diag}(1, -1)$). Unit: dimensionless. Status: STANDARD.

<!-- end generated symbol list -->

With three neutrinos it has no role left: its even part is bounded by the invisible width of the $Z$, and its oriented part
would thermalise the fold band of $\Psi_A$ (item 21); setting both coefficients to zero is a modelling choice (ASSUMED; item
22). Considered and rejected: a dipole portal $\bar\Psi\mathcal{S}^{MN}\Psi B_{MN}$ (it would thermalise the sterile fold
bands through the photon: too much dark radiation) and any operator coupling the neutral $\Psi$ to a single $W^+$ or $W^-$
(none is gauge invariant).

## Parameter choices (ASSUMED)

$HL = 3$ and $m_\Psi = H$ (from the record); the tip mixing $\mathcal{K} = 1$ of one generation, i.e. unitary tip matrices of
three generations with $\mathcal{K}_e = \mathcal{K}_u = \mathbf{1}$, $\mathcal{K}_\nu = U$, $\mathcal{K}_d = V_{\mathrm{CKM}}$;
the doublet localisation $c_L$ of each sector fixed by its heaviest member ($c_R = -c_L$ for the tau and for the top quark);
the lightest neutrino mass $m_1 = 1$ meV and the normal ordering; the Kohn-Sham test value of the self-coupling,
$\lambda_{\mathrm{test}} = 7\times10^{-5}H^{-6}$ (mean fields below 5 % of $m_\Psi$ in the densest test state; it is only
the value with which the Kohn-Sham machinery is tested); the coordinate volume $v_{\mathrm{t}}$ of the extra times (it enters
only $V_\perp$ and the conversion of $c_{\mathrm{V}}$, $c_{\mathrm{A}}$ and $\lambda$ into $G_{\mathrm{V}}$, $G_{\mathrm{A}}$
and $G_\lambda$). Version 3: the I11 strength $G_{\mathrm{V}} = 4.38\times10^{-17}$ GeV$^{-2}$ and the highest temperature
$T_{\mathrm{max}} = 10$ TeV of the hot Universe; the I12 strength $G_{\mathrm{I12}} = \pi/(2M_{\mathrm{DM}}^3)$ with universal
coefficients (chosen to respect the $^3P_0$ unitarity bound up to $E_{\mathrm{cm}} = 2.4M_{\mathrm{DM}}$); the bound
$G_\lambda = \lambda H\tilde I_\lambda/(2f^4v_{\mathrm{t}}) \le 2.3\times10^{-15}$ GeV$^{-2}$ on the self-interaction channel
(from $\Delta N_{\mathrm{eff}} \le 0.001$; item 24). The I13 strength is not a choice: it is DERIVED from the relic density.

# Standard physics and measured values (STANDARD)

Every measured value enters UM-2 in one of three roles, never as a derived result: as the target of a fit (the $W^\pm$ and
$Z$ masses with $\rho_{\mathrm{EW},0}$, the twelve fermion masses, the two neutrino splittings with the chosen $m_1$, and
$\Omega_{\mathrm{DM}}h_{100}^2$ for the freeze-out requirement), as a direct input (the angles and phases of the PMNS and
CKM matrices, $G_{\mathrm{F}}$, the $\overline{\mathrm{MS}}$ weak angle in the $Z$ widths, $\alpha_3$, $\alpha_{\mathrm{em}}$,
the CMB temperature, the Planck 2018 parameters of the cosmology, the effective couplings and kernel factors of the
decoupling equations, the matter densities and the supernova parameters), or as a comparison (the $Z$ widths, the number of
light neutrinos, $N_{\mathrm{eff}}$, the BAO, the explosion statistics, the supernova dark-energy fits, the LZ limit).

| input | value used | source | status |
|:-----------------|:---------------------------------------|:--------------------------|:------------|
| $W^\pm$ mass | $m_{\mathrm{W}} = 80.3625 \pm 0.0077$ GeV | PDG 2026, OUR EVALUATION (pdgLive S043M) | verified |
| $Z$ mass | $m_{\mathrm{Z}} = 91.1879 \pm 0.0020$ GeV | PDG 2026, OUR AVERAGE (pdgLive S044M) | verified |
| weak angle ($\overline{\mathrm{MS}}$, at $m_{\mathrm{Z}}$) | $\sin^2\theta_{\overline{\mathrm{MS}}} = 0.23122 \pm 0.00004$ | PDG electroweak review | from memory |
| electroweak parameter | $\rho_{\mathrm{EW},0} - 1 = 0.00038 \pm 0.00020$ | PDG electroweak review (global fit) | from memory |
| charged-lepton masses | electron $m_{\mathrm{e}} = 0.51099895000$ MeV, muon $105.6583755$ MeV, tau $1776.93 \pm 0.09$ MeV | PDG 2025 summary tables | verified |
| light-quark masses ($\overline{\mathrm{MS}}$, 2 GeV) | $m_{\mathrm{u}} = 2.16 \pm 0.07$ MeV, $m_{\mathrm{d}} = 4.70 \pm 0.07$ MeV, $m_{\mathrm{s}} = 93.5 \pm 0.8$ MeV | PDG 2025 summary tables | verified |
| heavy-quark masses | $m_{\mathrm{c}}(m_{\mathrm{c}}) = 1.2730 \pm 0.0046$ GeV, $m_{\mathrm{b}}(m_{\mathrm{b}}) = 4.183 \pm 0.007$ GeV, $m_{\mathrm{t}} = 172.56 \pm 0.31$ GeV (direct) | PDG 2025 summary tables | verified |
| neutrino oscillation parameters (normal ordering) | $\sin^2\theta_{12} = 0.308$, $\sin^2\theta_{23} = 0.470$, $\sin^2\theta_{13} = 0.02215$, $\delta_{\mathrm{CP}} = 212^\circ$, $\Delta m_{21}^2 = 7.49\times10^{-5}$ eV$^2$, $\Delta m_{31}^2 = 2.513\times10^{-3}$ eV$^2$; the inverted ordering is disfavoured by $\Delta\chi_{\mathrm{fit}}^2 = 6.1$; largest possible $J_{\mathrm{CP}}$: $0.0333 \pm 0.0007$ | NuFIT 6.0, arXiv:2410.05380 (JHEP 12 (2024) 216), Table 1, IC24 with SK atmospheric data | verified |
| lightest neutrino mass | $m_1 = 1.000$ meV | chosen | ASSUMED |
| sum of the neutrino masses | $\sum_im_i < 0.064$ eV (95 %, $\Lambda$CDM) | DESI DR2 Results II, arXiv:2503.14738 | verified |
| CKM parameters | $s_{12} = 0.22501$, $s_{13} = 0.003732$, $s_{23} = 0.04183$, $\delta_{\mathrm{CP}} = 1.147$ rad; $J_{\mathrm{CP}} = 3.12\times10^{-5}$ | PDG 2024 review "CKM quark-mixing matrix", global fit | verified |
| strong coupling | $\alpha_3(m_{\mathrm{Z}}) = 0.1180$ | PDG world average | from memory |
| Fermi constant, electroweak scale | $G_{\mathrm{F}} = 1.1663788\times10^{-5}$ GeV$^{-2}$; 246.22 GeV | PDG | from memory |
| fine-structure constant | $1/\alpha_{\mathrm{em},0} = 137.035999$ | CODATA | from memory |
| number of light neutrinos | $N_\nu = 2.9963 \pm 0.0074$ | PDG 2025 (Janot and Jadach, Phys. Lett. B803 (2020) 135319) | verified |
| (superseded, version 1) | $N_\nu = 2.9840 \pm 0.0082$ | LEP/SLD, Phys. Rept. 427 (2006) 257 | verified |
| $Z$ width and branching fractions | $2495.5 \pm 2.3$ MeV; invisible 20.000 %, hadrons 69.911 %, one charged-lepton pair 3.3658 % | PDG 2025 $Z$ listing | verified |
| nucleon masses | $m_{\mathrm{p}} = 938.272$ MeV, $m_{\mathrm{n}} = 939.565$ MeV | PDG | from memory |
| $\hbar c$, Boltzmann and Avogadro constants | $1.973269804\times10^{-16}$ GeV m, $8.617333262\times10^{-5}$ eV/K, $6.02214076\times10^{23}$ | CODATA, SI | from memory |
| CMB temperature today | $T_\gamma = 2.7255$ K | Fixsen 2009 | from memory |
| $N_{\mathrm{eff}}$ in the Standard Model | $3.0432 \pm 0.0002$ (three flavours, oscillations, NLO) | Cielo, Escudero, Mangano, Pisanti, arXiv:2306.05460 | verified |
| $N_{\mathrm{eff}}$ by the method of temperatures | 3.000, 3.011, 3.010, 3.039, 3.049, 3.048 (Table 1); couplings $\tilde g^{\nu_e e}_L = 0.727$, $\tilde g^{\nu_e e}_R = 0.233$, $\tilde g^{\nu_\mu e}_L = -0.273$, $\tilde g^{\nu_\mu e}_R = 0.233$; $f_{\mathrm{a}} = 0.884$, $f_{\mathrm{s}} = 0.829$ | Escudero, arXiv:2001.04466 | verified (2026-10-18) |
| finite-temperature QED pressure | the second- and third-order pressures of the electron-photon plasma (FE-113, FE-114) | Bennett et al., arXiv:1911.04504 | from memory; massless limits reproduced to $10^{-16}$ |
| $N_{\mathrm{eff}}$ measured | $2.99 \pm 0.17$ (Planck 2018 + BAO); $2.86 \pm 0.13$ (ACT DR6) | Planck 2018 VI, A&A 641 (2020) A6; Calabrese et al., arXiv:2503.14454 | verified |
| Planck 2018 base parameters | $\Omega_{\mathrm{b}}h_{100}^2 = 0.02237$, $\Omega_{\mathrm{DM}}h_{100}^2 = 0.1200$, $100\,\theta_{\mathrm{MC}} = 1.04092$ (the angular acoustic scale of CosmoMC), optical depth $\tau_{\mathrm{reio}} = 0.0544$, $\ln(10^{10}A_{\mathrm{s}}) = 3.044$, $n_{\mathrm{s}} = 0.9649$ | Planck 2018 results VI, Table 2 | from memory |
| BAO | DESI DR2: 13 measurements of $d_{\mathrm{V}}/r_{\mathrm{d}}$, $d_{\mathrm{M}}/r_{\mathrm{d}}$, $d_{\mathrm{H}}/r_{\mathrm{d}}$ (table below) | DESI collaboration, arXiv:2503.14738; the values checked against Table 2 of arXiv:2603.26861 | values verified (2026-10-17); correlations from memory |
| dark-matter density | $\Omega_{\mathrm{DM}}h_{100}^2 = 0.120$ | Planck 2018 | from memory |
| Planck mass (freeze-out) | $M_{\mathrm{Pl}} = G_{\mathrm{N}}^{-1/2} = 1.22091\times10^{19}$ GeV | | from memory |
| reduced Planck mass (radion decay) | $\bar M_{\mathrm{Pl}} = (8\pi G_{\mathrm{N}})^{-1/2} = 2.435\times10^{18}$ GeV | | from memory |
| angle of the gauge couplings | $\cos^2\theta_{\mathrm{W}} = (m_{\mathrm{W}}^2/m_{\mathrm{Z}}^2)/\rho_{\mathrm{EW},0} = 0.776368$ (used for $\beta_{\mathrm{Z}} = \beta_{\mathrm{W}}/\cos^2\theta_{\mathrm{W}}$ and in $\rho_{\mathrm{EW}}$); the on-shell value $m_{\mathrm{W}}^2/m_{\mathrm{Z}}^2 = 0.776663$ for comparison | computed from the $W^\pm$ and $Z$ masses and $\rho_{\mathrm{EW},0}$ above | computed |
| solar electron density | $n_{\mathrm{e}} = 245$ times the Avogadro constant times $\exp(-10.54$ times the radius in solar radii$)$ per cm$^3$ outside the core, at most 100 times the Avogadro constant per cm$^3$ (exponential fit) | after Bahcall | ASSUMED profile |
| matter of the Earth | densities 2.6 (T2K), 2.84 (NOvA), 2.848 (DUNE), 2.8 g/cm$^3$ (resonance); electron fraction 0.5 | representative constant densities | ASSUMED |
| supernova envelope and neutrinospheres | density $10^4$ times the cube of ($10^9$ cm over the radius) g/cm$^3$, electron fraction 0.5; luminosities 6, 6 and $4\times10^{52}$ erg/s and mean energies 11, 14 and 15.5 MeV ($\nu_e$, $\bar\nu_e$, the other flavours); $n_{\nu_e} = 10^{32}$ to $10^{33}$ cm$^{-3}$ | representative values | ASSUMED |
| supernova explosion statistics with flavour conversion | failed fractions 25.6 % (no conversion), 50.8, 77.4, 93.3, 96.4 % (conversion above the densities $10^9$ to $10^{13}$ g/cm$^3$); Salpeter-weighted 27.0, 47.6, 61.9, 73.9, 88.3 % | Gogilashvili and Tamborra, arXiv:2605.16504 (the author's file) | verified (read 2026-10-18) |
| fast flavour instability criterion | instability if and only if the electron-lepton-number distribution has a crossing | Morinaga, Phys. Rev. D 105 (2022) L101301 | from memory |
| direct-detection limit | LZ: $2.2\times10^{-48}$ cm$^2$ at 40 GeV, scaled linearly with the mass | LZ 2024 | from memory; the extrapolation is an ESTIMATE |
| nucleon gluon content, low-scale strong coupling | $f_{\mathrm{TG}} = 0.92$, $\alpha_3 = 0.3$ | standard | from memory; ESTIMATE |
| dark-energy density | $\rho_{\mathrm{de}} \approx 2.5\times10^{-47}$ GeV$^4$ | | from memory |
| gluon condensate (version 3) | $0.012$ GeV$^4$ for $\alpha_3/\pi$ times the squared field strength of the canonically normalised gluon field | Shifman, Vainshtein, Zakharov | from memory |
| QCD interaction measure (version 3) | $\Theta_{\mathrm{QCD}}/T^4$ peaks at about 4 near 200 MeV (lattice) | lattice QCD (HotQCD and Wuppertal-Budapest) | from memory; the shape used is an ESTIMATE |
| nucleon sigma terms (version 3) | $\sigma_{\pi N} = 45$ MeV, $\sigma_{\mathrm{s}} = 40$ MeV | standard | from memory; ESTIMATE |
| electromagnetic coupling at $m_{\mathrm{Z}}$ (version 3) | $\alpha_{\mathrm{em}} = 1/127.95$ | PDG | from memory |
| baryon-to-photon ratio (version 3) | $\eta_{\mathrm{b}} = 6.1\times10^{-10}$ | Planck 2018, BBN | from memory |
| neutron-proton mass difference (version 3) | $m_{\mathrm{n}} - m_{\mathrm{p}} = 1.293$ MeV | PDG | from memory |
| hadron resonance gas (version 3) | pion (0.138, 3), kaon (0.4956, 4), eta (0.5479, 1), rho (0.7753, 9), omega (0.7827, 3), K-star (0.8917, 12), nucleon (0.9389, 8), eta-prime (0.9578, 1), phi (1.0195, 3), Lambda (1.1157, 4), Sigma (1.1932, 12), Delta (1.232, 32) (mass in GeV, number of states) | PDG | from memory |
| QCD crossover (version 3) | $T_{\mathrm{c}} = 155$ MeV, $T_{\mathrm{w}} = 15$ MeV (smooth switch) | lattice QCD | from memory; the switch is ASSUMED |
| $\sigma_8$ (version 3) | 0.811 | Planck 2018 | from memory |
| tensor-to-scalar ratio (version 3) | $r_{\mathrm{ts}} < 0.036$ (95 %) | BICEP/Keck 2021 | from memory |
| astrophysical bodies (version 3) | $G_{\mathrm{N}} = 6.67430\times10^{-11}$ m$^3$kg$^{-1}$s$^{-2}$; Sun $1.98892\times10^{30}$ kg, $6.957\times10^8$ m; Earth $5.9722\times10^{24}$ kg, $6.371\times10^6$ m; white dwarf 0.6 solar masses, 8700 km; neutron star 1.4 solar masses, 12 km, core density 0.3 fm$^{-3}$ with 10 % protons; Earth mean density 5.51 g/cm$^3$; solar core 150 g/cm$^3$; white dwarf $10^6$ g/cm$^3$ | standard | from memory; representative |
| supernova dark-energy fits | constant $w_{\mathrm{de}} = -0.764$; $(w_{\mathrm{de},0}, w_{\mathrm{de},a}) = (-0.861, -0.60)$ | the author's private file (not in the repository) | AUTHOR |

The DESI DR2 BAO measurements used (redshift; the three distance ratios; the correlation coefficient $r_{\mathrm{MH}}$ of the
measured $d_{\mathrm{M}}/r_{\mathrm{d}}$ and $d_{\mathrm{H}}/r_{\mathrm{d}}$):

| tracer | $z_{\mathrm{red}}$ | $d_{\mathrm{V}}/r_{\mathrm{d}}$ | $d_{\mathrm{M}}/r_{\mathrm{d}}$ | $d_{\mathrm{H}}/r_{\mathrm{d}}$ | $r_{\mathrm{MH}}$ |
| --- | --- | --- | --- | --- | --- |
| BGS | 0.295 | $7.942 \pm 0.075$ | | | |
| LRG1 | 0.510 | | $13.588 \pm 0.167$ | $21.863 \pm 0.425$ | $-0.459$ |
| LRG2 | 0.706 | | $17.351 \pm 0.177$ | $19.455 \pm 0.330$ | $-0.404$ |
| LRG3+ELG1 | 0.934 | | $21.576 \pm 0.152$ | $17.641 \pm 0.193$ | $-0.416$ |
| ELG2 | 1.321 | | $27.601 \pm 0.318$ | $14.176 \pm 0.221$ | $-0.434$ |
| QSO | 1.484 | | $30.512 \pm 0.760$ | $12.817 \pm 0.516$ | $-0.500$ |
| Lyman-alpha | 2.330 | | $38.988 \pm 0.531$ | $8.632 \pm 0.101$ | $-0.431$ |

The goodness of fit of a model is

$$
\chi_{\mathrm{BAO}}^2 = \sum_{\text{tracers}}\big(\mathbf{d} - \mathbf{d}^{\mathrm{th}}\big)^T\,\mathbf{C}^{-1}\,
 \big(\mathbf{d} - \mathbf{d}^{\mathrm{th}}\big)
$$

<!-- symbols: sol_chiBAO, sol_dvec, transpose, sol_Cmat -->
<!-- begin generated symbol list -->
**Symbols in this equation.**

- $\chi^2_{\mathrm{BAO}}$: The chi-squared of the model distances against the 13 DESI DR2 BAO measurements (the pairs of the anisotropic tracers with their correlations, and one point for BGS). Unit: dimensionless. Value: $31.49$ for UM-2 ($32.55$ for $\Lambda$CDM). Status: DERIVED.
- $\mathbf{d},\ \mathbf{d}^{\mathrm{th}}$: The measured pair $(d_{\mathrm{M}}/r_{\mathrm{d}}, d_{\mathrm{H}}/r_{\mathrm{d}})$ of an anisotropic BAO tracer, and the pair $\mathbf{d}^{\mathrm{th}}$ computed in the model. Unit: dimensionless. Status: STANDARD.
- ${}^T$: The transpose: a row written with $^T$ is a column. Status: STANDARD.
- $\mathbf{C}$: The covariance matrix of the measured pair of one BAO tracer, built from the published errors and the published correlation coefficient of the pair. Unit: dimensionless. Status: STANDARD.

<!-- end generated symbol list -->

where, for an anisotropic tracer, $\mathbf{d}$ is the measured pair of $d_{\mathrm{M}}/r_{\mathrm{d}}$ and
$d_{\mathrm{H}}/r_{\mathrm{d}}$, $\mathbf{d}^{\mathrm{th}}$ the computed pair and $\mathbf{C}$ the $2\times2$ covariance
matrix with the squared published errors on the diagonal and $r_{\mathrm{MH}}$ times the product of the errors off the
diagonal; for the isotropic tracer BGS, $\mathbf{d}$ is the single ratio $d_{\mathrm{V}}/r_{\mathrm{d}}$ and $\mathbf{C}$ its
squared error. The distances of a flat model with the Hubble rate $\mathcal{H}$ as a function of the redshift are

$$
d_{\mathrm{M}}(z_{\mathrm{red}}) = \int_0^{z_{\mathrm{red}}}\frac{\mathrm{d}\tilde z_{\mathrm{red}}}{\mathcal{H}(\tilde z_{\mathrm{red}})},
\qquad d_{\mathrm{H}}(z_{\mathrm{red}}) = \frac{1}{\mathcal{H}(z_{\mathrm{red}})},\qquad
d_{\mathrm{V}} = \big(z_{\mathrm{red}}\,d_{\mathrm{M}}^2\,d_{\mathrm{H}}\big)^{1/3},\qquad 1 + z_{\mathrm{red}} = \mathrm{e}^{-a_4}
$$

<!-- symbols: sol_Dist, sol_zred, diff, Hubble, euler, a4 -->
<!-- begin generated symbol list -->
**Symbols in this equation.**

- $d_{\mathrm{M}},\ d_{\mathrm{H}},\ d_{\mathrm{V}}$: The distances of the BAO analysis at the redshift $z_{\mathrm{red}}$ (flat space, $c = 1$): the comoving transverse distance $d_{\mathrm{M}}$, the Hubble distance $d_{\mathrm{H}} = 1/\mathcal{H}$ at that redshift, and the volume-averaged distance $d_{\mathrm{V}} = (z_{\mathrm{red}}d_{\mathrm{M}}^2d_{\mathrm{H}})^{1/3}$ (written with a lower-case $d$ because $D_M$ is the covariant derivative). Unit: length (Mpc). Status: STANDARD.
- $z_{\mathrm{red}},\ \tilde z_{\mathrm{red}}$: The cosmological redshift, $1 + z_{\mathrm{red}} = \mathrm{e}^{-a_4}$ with $a_4 = 0$ today (not $z = 6Hx_0$, the angle variable of the hidden direction); $\tilde z_{\mathrm{red}}$ is the redshift as the variable of an integral. Unit: dimensionless. Status: STANDARD.
- $\mathrm{d}$: The differential: $\mathrm{d}X$ is an infinitesimal change of $X$, $\mathrm{d}X/\mathrm{d}Y$ the derivative of $X$ with respect to $Y$, $\mathrm{d}^nX$ the volume element of $n$ variables. Status: STANDARD.
- $\mathcal{H}$: The expansion rate of ordinary 3-space, $\mathcal{H} = \dot a_4$ (the Hubble rate of the observer; in the hot Universe $\mathcal{H} = (8\pi^3g_\rho/90)^{1/2}T^2/M_{\mathrm{Pl}}$). Unit: GeV. Status: DERIVED.
- $\mathrm{e}$: Euler's number, the base of the natural logarithm; $\mathrm{e}^{X}$ is the exponential of $X$. Unit: dimensionless. Value: 2.718281828. Status: STANDARD.
- $a_4$: The author's metric function of the time $x_4$ that scales ordinary 3-space: the scale factor of cosmology is $\mathrm{e}^{a_4}$. Unit: dimensionless. Status: AUTHOR.

<!-- end generated symbol list -->

with the sound horizon $r_{\mathrm{d}}$ at the drag epoch from CAMB (`um2_cosmology.py`, check `bao_desi`).

Standard theory used: the Standard-Model gauge theory $SU(3)_c\times SU(2)_L\times U(1)_Y$ with three generations; QCD
confinement of the quarks into hadrons (protons and neutrons); the PMNS and CKM matrices in the standard parametrisation
(FE-61); the flavour evolution of neutrinos in matter (Wolfenstein, Mikheyev and Smirnov; FE-103 to FE-108), with
antineutrinos obtained by complex conjugation of the mixing matrix and a change of sign of the matter potential; the
tree-level partial widths of the $Z$ (section 10); the radiative decay $\mu \to e\gamma$ for Dirac neutrinos; the freeze-out
of a relic (Kolb and Turner) and its numerical Boltzmann solution with the relativistic thermal average (Gondolo and
Gelmini); the trace-anomaly nucleon matrix element; the Einstein-Boltzmann equations of linear cosmological perturbations in
the Newtonian gauge (Ma and Bertschinger), solved by CAMB; the linearised equations of a dense neutrino gas (fast flavour
conversion); neutrino decoupling by the method of temperatures (Escudero); Higgsless electroweak symmetry breaking by a
non-linear sigma field and fermion localisation in an extra dimension (concepts only, no numbers).

# The field equations and their origin

The 136 field equations of UM-2 are the variations of the action of section 6 (FE-1 to FE-30), their exact reductions on the order-0 metric and the static block (FE-31 to FE-86), and the equations of the four-dimensional effective theory: the metric series and the linear perturbations (FE-87 to FE-99), the neutrinos (FE-100 to FE-120) and the thermal history (FE-121 to FE-136). The table gives, for each, its title and status (as in the inventory of the field equations), how it was obtained and solved, and the checks that verify it. The checks are named by the report and their number in the catalogue of section 9: alg (`um2_algebra.py`), geo (`um2_geometry.py`), bg (`um2_background.py`), fld (`um2_fields.py`), mass (`um2_spectra.py`), flav (`um2_flavour.py`), nu (`um2_neutrino.py`), ksv, kss, ks8, ks592, ksdm, ksp, ksfb (`um2_ks_jobs.py` validate, spectrum, ground8, ground592, darkmatter, portals, feedback), ew (`um2_electroweak.py`), prim (`um2_primordial.py`), cos (`um2_cosmology.py`), ana (`um2_analysis.py`), th (`um2_thermal.py`), cpl (`um2_coupled.py`), ser (`um2_series.py`) and res (`um2_residuals.py`, version 4: res 1 to 26 are the residuals of the solution in its equations, res 27 to 52 the links in concert). The field equations that this document uses are written out where they are used (FE-1, FE-31, FE-32, FE-56, FE-64 to FE-66 in sections 4 and 5; FE-2, FE-47, FE-55, FE-67, FE-75, FE-76, FE-79, FE-102, FE-115, FE-120 to FE-123 and FE-131 in section 10).

| FE | field equation (status) | how it was obtained and solved | verified by |
|:------|:-------------------------|:----------------------------------------|:------------------------|
| FE-1 | The Einstein-Lovelock equations (AUTHOR) | metric variation of IN-2 and of the matter action: the author's notebook equations with a source (section 4); solved at order 0 through FE-38 to FE-40 and at order $\epsilon$ through FE-49 | geo 4-12, 16-18; res 1 |
| FE-2 | The energy-momentum tensor: definition and components (STANDARD) | definition (for spinors the variation with respect to the vielbein) | ks8 2; ks592 2 |
| FE-3 | The total source of gravity (DERIVED) | sum of the energy-momentum tensors of the terms of IN-1 | cpl 14; res 9, 11 |
| FE-4 | The energy-momentum tensor of the stabiliser (DERIVED) | metric variation of IN-4 with $\rho_{\mathrm{stab}} \propto f^{-8}$ | bg 10, 13, 15; res 1 |
| FE-5 | The energy-momentum tensor of dirac16complex (DERIVED) | symmetrised vielbein variation of IN-5; for Kohn-Sham states it is FE-67 | ks8 2, 3; ks592 2-4; ksdm 3; ana 20 |
| FE-6 | The energy-momentum tensor of the Standard-Model fermions (DERIVED) | vielbein variation of IN-11; used through ideal and degenerate gases with the $x_0$ masses | th 1; cpl 14 |
| FE-7 | The energy-momentum tensor of the gauge fields (STANDARD) | metric variation of IN-8 | bg 19; ks592 4 |
| FE-8 | The energy-momentum tensor of the tip (DERIVED) | metric variation of IN-13 at $y = -L$; its effect is part of the rest energies of $W^\pm$, $Z$ and the fermions | (no separate check) |
| FE-9 | The energy-momentum tensors of the portals I11 and I13 (DERIVED) | metric variation of IN-16 and IN-18 (the frame currents do not depend on the vielbein) | cpl 13 |
| FE-10 | The energy-momentum tensor of the portal I12 (DERIVED) | metric variation of IN-17 | cpl 15; res 12 |
| FE-11 | Conservation of the source (DERIVED) | diffeomorphism invariance: the Bianchi identities of the Lovelock tensors | geo 6-8; ks8 2; ks592 2 |
| FE-12 | The dirac16complex field equation with the canonical spin connection and the portals (DERIVED) | variation of IN-5 and IN-16 to IN-18 with respect to $\bar\Psi$; reduced exactly to FE-56 | fld 1; cpl 6; ksp 5 |
| FE-13 | The canonical spin connection on the order-0 metric (DERIVED) | IN-7 evaluated on FE-31 (sympy, both halves of a period) | geo 22-25 |
| FE-14 | The Dirac equation of the quark doublets $Q_i$ (DERIVED) | variation of IN-11, IN-13, IN-16, IN-18 with respect to $\bar Q_i$; solved by FE-56 to FE-60 | fld 1, 8, 12, 13; mass 11-13; flav 3 |
| FE-15 | The Dirac equation of the up-type quark singlets $u_{Ri}$ (right-handed up, charm and top quarks) (DERIVED) | as FE-14, with respect to $\bar u_{Ri}$ | fld 9, 12, 13; mass 11-13; flav 3 |
| FE-16 | The Dirac equation of the down-type quark singlets $d_{Ri}$ (right-handed down, strange and bottom quarks) (DERIVED) | as FE-14, with respect to $\bar d_{Ri}$; the tip matrix of the sector is the CKM matrix | fld 9, 12, 13; mass 11-13; flav 3 |
| FE-17 | The Dirac equation of the lepton doublets (left-handed neutrinos and charged leptons of three flavours) (DERIVED) | variation of IN-11, IN-13, IN-16 with respect to $\bar\ell_i$ (no I13 term) | fld 8, 12, 13; mass 11-13; flav 3, 7 |
| FE-18 | The Dirac equation of the right-handed charged leptons $e_{Ri}$ (electron, muon and tau) (DERIVED) | as FE-17, with respect to $\bar e_{Ri}$ | fld 9, 12, 13; mass 11-13 |
| FE-19 | The Dirac equation of the right-handed neutrinos $\nu_{Ri}$ (DERIVED) | as FE-17, with respect to $\bar\nu_{Ri}$ (gauge singlets) | mass 11, 13; flav 3; cpl 10 |
| FE-20 | The fermion currents of the gauge fields (STANDARD) | variation of IN-11 with respect to the gauge fields | ew 1-4 |
| FE-21 | The field-dependent gauge couplings produced by I12 (DERIVED) | IN-8 and IN-17 combined | cpl 15, 16; res 12 |
| FE-22 | The Yang-Mills equation of the gluons (DERIVED) | variation of IN-8, IN-11, IN-17 with respect to the gluon field | fld 14; mass 1, 3 |
| FE-23 | The Yang-Mills equation of the SU(2) field $W^I$ (matrix form) with the tip current (DERIVED) | variation of IN-8, IN-11, IN-13, IN-17 with respect to the SU(2) field, in the unitary gauge | fld 14, 15; mass 6-8 |
| FE-24 | The Yang-Mills equation of the hypercharge field $B$ (DERIVED) | as FE-23, with respect to the hypercharge field | fld 14, 15 |
| FE-25 | The $W^+$, $W^-$, $Z$ and photon field equations to linear order in the fields (I12 neglected) (DERIVED) | FE-23 and FE-24 at linear order with IN-10 | ew 2-4; mass 3, 7, 8 |
| FE-26 | The tip sigma field equation (the Noether identity of the gauge symmetry) (STANDARD) | variation of IN-13 with respect to $\Sigma$ (the Noether identity of the gauge symmetry) | fld 16 |
| FE-27 | The boundary conditions of gravity and the gauge fields at the fold and the tip (DERIVED) | boundary terms of the variation at the fold and at the tip | fld 15 |
| FE-28 | The boundary conditions of dirac16complex (DERIVED) | the record's fold and tip conditions; self-adjoint | fld 5, 7; kss 1 |
| FE-29 | The boundary conditions of the Standard-Model fermions (INVENTED) | selection projector chosen so that each doublet has one left-handed and each singlet one right-handed Weyl zero mode | fld 3-5, 8-10; ew 12 |
| FE-30 | The tip mixing conditions of one and of three generations (DERIVED) | IN-13 on the zero modes; self-adjoint for every complex matrix (sympy, 42 real variables); the tip matrices ASSUMED | fld 12, 13; flav 3, 4 |
| FE-31 | The order-0 metric in the author's coordinates (AUTHOR) | the record's corrected metric (section 5) in the author's coordinates | geo 1-3 |
| FE-32 | The hidden coordinate $y$, the block scale and the rates of the background (DERIVED) | change of chart to $y$ (section 5) | geo 1-3, 22 |
| FE-33 | The sectional curvatures of the order-0 metric (DERIVED) | Riemann tensor of FE-31 in both charts (sympy) | geo 1-3 |
| FE-34 | The Lovelock densities and tensors of a pair-diagonal curvature (DERIVED) | pairing formula, coefficients $2^pp!$ and $-2^{p-1}p!$ (sympy) | geo 4-12; bg 4 |
| FE-35 | The first Lovelock tensor (the Einstein tensor) of the order-0 metric (DERIVED) | FE-34 with FE-33 (sympy, four routes) | geo 4, 6, 10, 13; bg 1, 4 |
| FE-36 | The second Lovelock tensor (Gauss-Bonnet) of the order-0 metric (DERIVED) | as FE-35 | geo 5, 7, 11, 14; bg 2, 4 |
| FE-37 | The third Lovelock tensor of the order-0 metric (DERIVED) | as FE-35 | geo 8, 12, 15; bg 3, 4 |
| FE-38 | The background equation: the $x_4$ component (the constraint) (DERIVED) | FE-1 with FE-35 to FE-37, the author's weights and $\Lambda$ | geo 16, 19; prim 1; res 1, 3 |
| FE-39 | The background equation: the 3-space component (DERIVED) | as FE-38; integrated through the primordial era (DOP853) | geo 17, 20; bg 14; prim 1-5; res 1, 3 |
| FE-40 | The background equation: the hidden (block) component (DERIVED) | as FE-38; the $x_0$ and the extra-time components have the same left side, and the order-0 metric (one block scale) obeys their average with $\bar p$ | geo 18, 21; bg 1-3, 14; res 1, 3 |
| FE-41 | The conservation of the order-0 source (DERIVED) | FE-11 on FE-31 | bg 15; prim 1 |
| FE-42 | The static block (DERIVED) | FE-38 to FE-40 with $\mathcal{H}_f = 0$, $\dot{\mathcal{H}} = 0$ | geo 19-21; bg 5-9; res 1 |
| FE-43 | The stabilised block (DERIVED) | closed form (sympy) | bg 10-13, 15; res 1, 48 |
| FE-44 | The linearised block and the radion (DERIVED) | Jacobian of FE-39 and FE-40 at the static block | bg 16, 17; prim 2; ana 22; res 2, 47 |
| FE-45 | The response of the block to matter to first order (DERIVED) | linearisation with block-averaged sources | bg 18; res 2 |
| FE-46 | The coefficients of the first-order block response (DERIVED) | exact algebraic numbers (sympy) | bg 18, 19; res 46 |
| FE-47 | The adiabatic block response and the four-dimensional Friedmann acceleration equation (DERIVED) | FE-45 with the second time derivative of $\Delta K$ neglected | bg 19; ksfb 1; res 2, 9 |
| FE-48 | The four-dimensional reduction of the Lovelock action on the static block (DERIVED) | dimensional reduction on the static block (sympy) | bg 20-22; ksfb 2; ana 21; res 4 |
| FE-49 | The four-dimensional effective gravity and the four-dimensional couplings (DERIVED) | the reduced action and the zero modes of the gauge fields | bg 21, 22; ana 23; res 4, 37 |
| FE-50 | The $x_0$ eigenvalue equation of the gauge fields and the graviton (DERIVED) | reduction of FE-22 to FE-25 (and of FE-1 for the transverse-traceless graviton) on the static block | fld 14; mass 1-4; ana 1-7; ser 2; res 5 |
| FE-51 | The fold and tip conditions of the boson $x_0$ profiles (DERIVED) | natural boundary conditions of IN-15 | fld 15; mass 6, 7; res 5 |
| FE-52 | The boson eigenvalue conditions (DERIVED) | exact solution of FE-50: mpmath roots (30 to 60 digits), finite elements as a check | mass 1-5, 9; flav 5; ana 2; res 5 |
| FE-53 | The tower of Kaluza-Klein gravitons (the terms $n \ge 1$ of the metric series) (DERIVED) | exact eigenfunctions of FE-50 with $\beta = 0$ | mass 1, 2; ser 2; res 15 |
| FE-54 | The potential between two static masses with the Kaluza-Klein gravitons (DERIVED) | exchange of the tower between two static sources | ser 2; res 15 |
| FE-55 | The $W^\pm$ and $Z$ masses, the electroweak parameter and the Kaluza-Klein scale (DERIVED) | fit of $\beta_{\mathrm{W}}$ by bisection in $\ln\beta_{\mathrm{W}}$ (80 steps) | mass 7, 8, 10; res 5, 13, 29, 30 |
| FE-56 | The exact reduction of the eight-dimensional Dirac equation to the block Hamiltonian (DERIVED) | the record's reduction, re-derived exactly for all eight blocks with the author's matrices (sympy) | fld 1, 2; alg 19-29 |
| FE-57 | The chiral zero modes (massless four-dimensional fermions) (DERIVED) | exact solutions of FE-56 at $k = 0$ | fld 6-11; kss 2 |
| FE-58 | The tip values of the doublet and singlet solutions at $k = 0$ (DERIVED) | exact solutions of the doublet and singlet systems | mass 11-13 |
| FE-59 | The exact mass condition of one generation and its first-order root (DERIVED) | FE-58 in FE-30; mpmath roots, shooting (DOP853) as a check | mass 11-14; ana 8, 9; res 6 |
| FE-60 | The mass condition of three generations with the $3 \times 3$ tip matrices (DERIVED) | FE-58 in the three-generation FE-30; mpmath at 50 digits | flav 3, 4, 7; res 6 |
| FE-61 | The standard parametrisation of the mixing matrices (the tip matrices of UM-2) (STANDARD) | NuFIT 6.0 and PDG values (section 7) | flav 1, 2, 6; res 33 |
| FE-62 | The spectrum of dirac16complex on the static block (DERIVED) | exact solution of FE-56 with $M = m_\Psi$ | kss 1-3; ew 13; ana 12; res 7 |
| FE-63 | The Kohn-Sham equations of dirac16complex coupled to all fields (DERIVED) | the record's block Hamiltonian with the mean fields FE-64; Galerkin in the free basis, Anderson mixing, Richardson in the basis size | ksv 1, 2; ks8 1; ks592 1; cpl 1, 7; res 8 |
| FE-64 | The Kohn-Sham mean fields (DERIVED) | the record's Hartree-plus-exchange fields of the contact term and the portal mean fields of IN-16 to IN-18 | ksp 1-4; cpl 1, 7, 13; res 8, 10, 11 |
| FE-65 | The Kohn-Sham densities, shells, cell volume and occupations (RECORD) | the record's definitions | ksv 1, 2 |
| FE-66 | The Kohn-Sham energy (RECORD) | the record's functional | ks8 3; ks592 3; ksdm 1 |
| FE-67 | The energy-momentum tensor of a Kohn-Sham state (DERIVED) | FE-5 for Kohn-Sham states | ksdm 2, 3; ks592 4; ana 19; res 9, 28 |
| FE-68 | The energy identity and the $y$-conservation law of a Kohn-Sham state (DERIVED) | from FE-66, FE-67 and FE-11 | ks8 2, 3; ks592 2, 3; res 8 |
| FE-69 | The boundary conditions of the Kohn-Sham orbitals (DERIVED) | block form of FE-28 ($\gamma^{x_0} = \sigma_3$ in every block) | alg 20; fld 5; ew 13 |
| FE-70 | The portals I11 and I13 on the zero modes: the four-dimensional contact interactions (DERIVED) | reduction of IN-16 and IN-18 with the zero-mode profiles | cpl 1, 3, 5-7, 9; ksp 1-3; res 10, 40 |
| FE-71 | The portal I12 on the dark matter (DERIVED) | reduction of IN-17 with the dark-matter orbital | ksp 4; ana 17; res 10, 41 |
| FE-72 | The shift of a Kohn-Sham level by the mean fields of an environment (DERIVED) | first order in the mean fields (Hellmann-Feynman) | cpl 1, 2, 13; res 11 |
| FE-73 | The level shift of the dark matter in matter of protons, neutrons and electrons (DERIVED) | FE-72 for protons, neutrons and electrons | cpl 13; res 11 |
| FE-74 | The thermal gluon condensate from the trace anomaly (STANDARD) | trace anomaly (Shifman, Vainshtein, Zakharov) | cpl 13; res 11 |
| FE-75 | The QCD interaction measure (ESTIMATE) | lattice-like shape below 1 GeV, leading order above | cpl 13 |
| FE-76 | The thermal condensate of a massive vector boson and the order-$\alpha_{\mathrm{G}}$ condensate of a gauge plasma (STANDARD) | free part; Feynman-Hellmann at order $\alpha_{\mathrm{G}}$ | cpl 13; res 11, 22 |
| FE-77 | The running electroweak couplings without a Higgs particle (STANDARD) | one loop from the $\overline{\mathrm{MS}}$ values at $m_{\mathrm{Z}}$ | cpl 13 |
| FE-78 | The electroweak condensates of a hot plasma (ESTIMATE) | FE-76 with FE-77; thermal suppression below $m_{\mathrm{W}}$ | cpl 13 |
| FE-79 | dirac16complex acting on the Standard Model: the coupling shifts and the $x_0$ problem of $W^\pm$ and $Z$ (DERIVED) | FE-21 and FE-50 with the dark-matter scalar density; first-order perturbation theory (version 4) | cpl 15; res 12, 45 |
| FE-80 | Gravity in the coupled solution: the block response to every species (DERIVED) | FE-47 with all species, iterated with the masses | cpl 14; res 11 |
| FE-81 | The hidden pressure of matter and of the hot plasma (DERIVED) | $\bar p = \frac14\,\mathrm{d}p/\mathrm{d}\ln f$ at fixed temperature | cpl 14; res 11, 39 |
| FE-82 | The block dependence of a gauge coupling and the trace of an electroweak plasma (DERIVED) | $g_{\mathrm{G}}^2 \propto f^{-4}$, $m_{\mathrm{KK}} \propto 1/f$, one loop | cpl 14 |
| FE-83 | The block dependence of the QCD scale and of the nucleon mass (ESTIMATE) | one loop; nucleon sigma terms | cpl 12; res 52 |
| FE-84 | The block dependence of the QCD scale through the quark thresholds (ESTIMATE) | one-loop matching at the quark thresholds | cpl 12; res 52 |
| FE-85 | The block dependence of a fermion mass (DERIVED) | FE-59 with localisations proportional to $f$ | ana 11; cpl 12; res 52 |
| FE-86 | The densities of the environments of the coupled solution (ASSUMED) | net baryons in weak equilibrium; dark matter in equilibrium below $x = 40$ | cpl 13; res 11 |
| FE-87 | The metric as a power series of terms of decreasing magnitude (DERIVED) | magnitudes of the computed terms | ser 1-4; res 16 |
| FE-88 | The order-1, $n = 0$ term of the metric in the Newtonian gauge (eight dimensions) (DERIVED) | Newtonian gauge in eight dimensions | ser 1, 3; res 16 |
| FE-89 | The four-dimensional perturbed metric in conformal time (STANDARD) | Newtonian gauge (Ma and Bertschinger) | cos 3 |
| FE-90 | The linearised Einstein equations for a Fourier mode (STANDARD) | CAMB 2.0.5 (default accuracy, lensing) | cos 1, 3, 4, 8; res 14 |
| FE-91 | The perturbations of the dark matter (cold) (STANDARD) | CAMB; cold (a Kohn-Sham quantum at rest has zero pressure) | cos 3; ksdm 2 |
| FE-92 | The perturbations of the baryons (STANDARD) | CAMB | cos 3, 4 |
| FE-93 | The perturbations of the photons: density and velocity (STANDARD) | CAMB | cos 3 |
| FE-94 | The photon temperature hierarchy (STANDARD) | CAMB | cos 3 |
| FE-95 | The photon polarisation hierarchy (STANDARD) | CAMB | cos 3 |
| FE-96 | The hierarchy of each neutrino mass state (the cosmic neutrino background) (STANDARD) | CAMB, the three mass states separately (masses iterated) | cos 2, 6, 7; res 32, 34 |
| FE-97 | The background expansion, the neutrino temperature and the primordial spectrum (STANDARD) | Planck 2018 parameters; $N_{\mathrm{eff}} = 3.0432 + 0.0010$ | cos 1, 4, 6; res 35, 38 |
| FE-98 | The size of the first-order potentials: rms value, Poisson equation and large scales (STANDARD) | from the CAMB solution | cos 8; ser 1; res 14 |
| FE-99 | The amplitude of the matter fluctuations (STANDARD) | from the CAMB matter power spectrum | cos 8; res 50 |
| FE-100 | The three neutrino masses (ASSUMED) | $m_1$ and the ordering chosen, the splittings of NuFIT 6.0; $x_0$ eigenvalues of FE-59 | nu 1, 16; mass 11; res 32 |
| FE-101 | The four-fermion interactions at low energy (STANDARD) | exchange of $W^\pm$ and $Z$ far below their masses | nu 2-5; ew 6-11 |
| FE-102 | The Fermi constant and the neutral-current couplings (STANDARD) | tree level; the measured $G_{\mathrm{F}}$ | ew 4, 16, 18, 19; res 13, 30 |
| FE-103 | The matter potentials of forward scattering (STANDARD) | forward scattering in an unpolarised medium | nu 3-5, 11 |
| FE-104 | The flavour evolution in vacuum and in matter (STANDARD) | exact matrix exponentials; ordered products of layers | nu 2-5; res 17 |
| FE-105 | The vacuum oscillation probability, CPT and the T-odd difference (STANDARD) | analytic | nu 2; res 17 |
| FE-106 | The MSW resonances of the 1-3 and 1-2 sectors (STANDARD) | two-flavour conditions; the exact three-flavour root as a check | nu 3, 5; res 17 |
| FE-107 | The adiabatic survival probability of solar electron neutrinos (STANDARD) | adiabatic formula; numerical evolution as a check | nu 5; res 17 |
| FE-108 | The resonance density, the adiabaticity and the Landau-Zener jump probability (STANDARD) | two-flavour conditions | nu 11; res 17 |
| FE-109 | The thermal potential of the early Universe (STANDARD) | leading order in $T/m_{\mathrm{W}}$; Brent roots | nu 6; res 18 |
| FE-110 | The quantum kinetic equations of a neutrino gas (STANDARD) | linearised (FE-117) and momentum averaged (FE-111) | nu 8, 9, 12-14 |
| FE-111 | Neutrino decoupling: the temperature equations (STANDARD) | Escudero's method; LSODA from 20 MeV to 5 keV | nu 8, 9; res 19 |
| FE-112 | The energy transfer by collisions (STANDARD) | Escudero's kernels with the radiatively corrected couplings | nu 8, 9 |
| FE-113 | The finite-temperature QED pressure of the electron-photon plasma (STANDARD) | Bennett et al. | nu 7 |
| FE-114 | The integrals of the QED pressure (STANDARD) | Gauss-Legendre panels | nu 7 |
| FE-115 | The effective number of neutrino species and the common temperature (STANDARD) | from FE-111; the precision value 3.0432 is adopted | nu 8, 9; res 19, 35, 49 |
| FE-116 | The fast flavour instability: the electron-lepton-number distribution (STANDARD) | definitions; axially symmetric gas | nu 12, 13; res 20 |
| FE-117 | The fast flavour instability: the dispersion relation (STANDARD) | vectorised Newton iterations | nu 12, 13; res 20 |
| FE-118 | The axisymmetric and azimuthal branches of the dispersion relation (STANDARD) | analytic | nu 13 |
| FE-119 | The homogeneous mode and the mode $k_{\mathrm{f}} = \mathcal{I}_1$ (STANDARD) | 300-node discretisation; analytic growth | nu 12, 14, 15; res 20 |
| FE-120 | The cosmic neutrino background (STANDARD) | adaptive quadrature (to $3\times10^{-16}$ since version 4) | nu 10; res 21, 34 |
| FE-121 | The ideal-gas densities of a species of the plasma (STANDARD) | Gauss-Legendre quadrature with the $x_0$ masses | th 1; res 22, 31, 39 |
| FE-122 | The effective degrees of freedom and the Hubble rate of the hot Universe (STANDARD) | sums of FE-121 | th 1; res 22, 37 |
| FE-123 | The QCD crossover, the neutrino temperature after decoupling and the cooling of the plasma (ASSUMED) | smooth switch; instantaneous neutrino decoupling at 2 MeV | th 1; res 22, 38 |
| FE-124 | The Boltzmann equation of one dark-matter species (STANDARD) | implicit Radau on $\ln Y_{\mathrm{DM}}$ | th 3, 4; cpl 8; res 23 |
| FE-125 | The relativistic thermal average of the annihilation cross-section (STANDARD) | Gondolo and Gelmini; adaptive quadrature | th 2; res 23 |
| FE-126 | The relic density (STANDARD) | from FE-124 | th 3, 4; cpl 8; res 23, 36 |
| FE-127 | The annihilation cross-sections of the dark matter through I12 and I13 (DERIVED) | spin traces and polarisation sums of FE-70 and FE-71 | ana 13-16; cpl 8; res 23 |
| FE-128 | The partial-wave unitarity bounds (DERIVED) | partial waves $^3P_0$ and $^3S_1$ | th 5-7; ana 16; cpl 8 |
| FE-129 | The freeze-in of the fold bands through I11 (DERIVED) | FE-70 with Maxwell-Boltzmann statistics; trapezoid rule | cpl 4; res 24 |
| FE-130 | The dark radiation of the fold bands and their departure from equilibrium (DERIVED) | from FE-129 | cpl 4; cos 6, 7; res 24, 35 |
| FE-131 | The right-handed neutrinos if I13 coupled to $B - L$ (DERIVED) | Radau in the shifted variable $x - 2$ (version 4) | cpl 10; res 25 |
| FE-132 | The elastic scattering of right-handed neutrinos on the dark matter (ESTIMATE) | a Weyl $\nu_R$ on a heavy Dirac fermion | cpl 10; res 25 |
| FE-133 | The extra radiation of species that decouple early (DERIVED) | entropy conservation with the heating factor | cpl 10, 11; cos 5; res 49 |
| FE-134 | The production of right-handed neutrinos through I11 (with the baryon current in I13) (DERIVED) | ratio of the I11 and I13 rates | cpl 10; res 25 |
| FE-135 | The self-interaction channel of the dark matter into the fold bands (ESTIMATE) | IN-5 on the dark matter and the fold bands; Fierz coefficients not computed | cpl 11; res 10, 26 |
| FE-136 | The energy put into the fold bands by the self-interaction channel (DERIVED) | trapezoid rule from $T_{\mathrm{max}}$ to the freeze-out | cpl 11; res 26 |

# The computations and their verification (DERIVED)

All computations are Python scripts in the folder `universe_model_2/code`; each writes its numbers to
`universe_model_2/outputs` and a report of named checks (name, verdict, detail) to `universe_model_2/reports`, and exits with
code 0 only if every check passes. Two modules are shared: `um2_common.py` (the output folders, the report class, reading and
writing the JSON files) and `um2_constants.py` (the measured inputs of section 7). In total 287 checks in version 4: the
235 of version 3 (233 before the fixes of its independent review, item 24; 205 in version 2; 179 to 182 in version 1) and the
52 of the new residual analysis; none failed. In the table the prefix `um2_` of every script name is omitted.

| script | what it computes | method | output | checks |
|:----------------|:-----------------------------------------|:-------------------------|:--------------------|:------|
| algebra.py | the author's gamma matrices rebuilt from the notebook formulas; $C$, $\Gamma_8$, $\mathcal{B}$; the irreducibility of the representation of Pin(4,4); the two inequivalent halves of Spin(4,4); the $2\times2$ block basis and the block forms of every matrix the reductions use | sympy, exact | algebra.json | 31 |
| geometry.py | the Riemann tensor of the order-0 metric in two charts; the Lovelock tensors by four routes (pairing formula, Ricci tensor, explicit Gauss-Bonnet tensor, minisuperspace variation with a lapse); the Bianchi identities; the record's equations; the static block; the canonical spin connection | sympy, exact | geometry.json | 25 |
| background.py | the background equations in class form; the static block; the stabiliser and its family; the radion; the linear response of the block to matter sources; the dimensional reduction | sympy, exact; eigenvalues numerically | background.json | 22 |
| fields.py | the exact $x_0$ reduction of the eight-dimensional Dirac equation (all blocks, general $a_4$, $b_4$, $M$, $v$); boundary conditions; zero modes; tip mixing for one and three generations (self-adjoint with an arbitrary complex $3\times3$ matrix); the gauge $x_0$ operator; gauge invariance of the tip terms of three generations | sympy and numpy | fields.json | 16 |
| spectra.py | the $x_0$ spectra of the gauge bosons and the graviton; the $W^\pm$, $Z$ fit to $\rho_{\mathrm{EW},0}$ with the angle of the couplings fixed by the measured masses (both masses reproduced); the twelve fermion masses as exact $x_0$ eigenvalues | mpmath root finding; quadratic finite elements with Richardson; shooting | masses.json | 14 |
| flavour.py | the PMNS and CKM matrices; the exact tip determinant of three generations and its null vectors; a general complex tip matrix; the flavour-changing couplings of the Kaluza-Klein gauge modes; $\mu \to e\gamma$; lepton universality | mpmath (50 digits), numpy | flavour.json | 7 |
| neutrino.py | vacuum and matter oscillations, the MSW resonances, long-baseline appearance, the Sun, the onset of oscillations in the early Universe, neutrino decoupling and $N_{\mathrm{eff}}$, the CNB, supernova resonances, the fast flavour instability, the heating behind the shock; (version 3) the Majorana alternative | exact matrix exponentials and layer products; LSODA; Gauss-Legendre panels; Newton iterations; adaptive quadrature | neutrino.json | 16 |
| kohnsham.py, ks_jobs.py | Kohn-Sham (the solver library and its seven jobs): validation against the record (2 checks), free spectrum (3), interacting ground states of 8 (3) and of 592 particles (4), dark-matter quanta (3), portal responses with the three-generation sources (5), block feedback with the full adiabatic response (2) | Galerkin in the free basis, safeguarded Anderson self-consistency, Richardson in the basis size; single-threaded linear algebra (version 4) | ks/*.json (seven files) | 22 |
| electroweak.py | charges ($W^+$: $+e$, $W^-$: $-e$), anomalies of three generations, couplings, the chirality projector, $\Gamma_4 = -\mathcal{B}\gamma^{x_0}$, the chiral tip charges of $\Psi_A$ and $\Psi_B$, the number of light neutrinos, the removal of the tip $Z$ portal, the $Z$ widths of three generations and their scheme dependence | sympy and numerics | electroweak.json | 19 |
| primordial.py | the nonlinear primordial evolution, the basin, the separatrix, the radion oscillation | DOP853, bisection | primordial.json | 5 |
| cosmology.py | TT and EE spectra with three massive neutrinos, the BAO $\chi_{\mathrm{BAO}}^2$, $N_{\mathrm{eff}}$, helium, the variants with a thermalised fold band; (version 3) the model with the freeze-in fold bands, $\sigma_8$, the growth rate, the potential spectrum | CAMB 2.0.5 | cosmology.json | 8 |
| analysis.py | the $x_0$ decompositions and the uncertainty relation on the cell; the gap theorem; sum rules; the twelve fermions against the uncertainty estimate; the conservation of the halves; the relic of two species with I12 alone; direct detection; the condensate; the vacuum energy; the sensitivities to the block size; the block rate today; the radion decay | mpmath, numpy, sympy | analysis.json | 23 |
| thermal.py | (version 3) the degrees of freedom with the $x_0$ masses; the relativistic thermal average; the Boltzmann solver and its validation; the relic of I12 alone; partial-wave unitarity; the unitarity-safe I12 benchmark | Gauss-Legendre ideal-gas integrals; adaptive quadrature with scaled Bessel functions; implicit Radau; Brent root finding | thermal.json | 7 |
| coupled.py | (version 3) the portal overlaps with every zero mode and their Kohn-Sham checks; the screened response; the fold band under the portals; the freeze-in of the fold bands; direct detection; I13 (the algebra of its bilinear, fold-band blindness, relic with the unitarity cap, detection, annihilation today); the $B - L$ alternative; the self-interaction channel; the mean fields in ten environments; the full adiabatic block response to every species; the proton sensitivity; the $W$ eigenvalue with the kinetic function; the domain of validity | exact sympy matrices; self-consistent Kohn-Sham solutions with Richardson in the amplitude; Boltzmann equations; first-order perturbation theory (version 4) | coupled.json | 16 |
| series.py | (version 3) the magnitudes of the terms of the metric series: potentials, Kaluza-Klein gravitons (levels, norms, Yukawa strengths, orthogonality), the radion, order 2, the tensor bound | analytic eigenfunctions, finite elements, quadrature | series.json | 4 |
| residuals.py | (version 4) the residuals of the stored solution in 26 field equations (afresh by substitution where cheap), the sizes of the neglected terms, and 26 links in concert (section 10) | substitution (sympy, mpmath at 40 digits), independent quadratures and re-integrations | residuals.json | 52 |

## The catalogue of the 287 checks

The checks are listed by report, numbered in the order of the report; the names are those of the reports, spelled as in
the code. The field-equation table of section 8 refers to them by the abbreviation of the report and the number.

```{=latex}
\begingroup\raggedright
```

**alg** (`um2_algebra.py`, 31 checks, all passed): 1 `tau_relations_of_the_notebook`; 2 `notebook_identities_sigma`; 3 `clifford_relations`; 4 `gammas_real`; 5 `identical_to_record_gammas`; 6 `C_is_sigma16`; 7 `C_real_symmetric_involution`; 8 `C_gamma_antisymmetric`; 9 `chirality_diag`; 10 `B_hermitian_involution`; 11 `B_signature_8_8`; 12 `B_gamma4_gamma_a_hermitian`; 13 `pin44_irreducible`; 14 `spin44_commutant_dim_2`; 15 `spin44_preserves_chiral_halves`; 16 `chiral_halves_irreducible`; 17 `chiral_halves_inequivalent`; 18 `commuting_set`; 19 `block_basis_unitary`; 20 `block_form gamma^(x0) = sigma3`; 21 `block_form gamma^(x0)gamma^(x1) = -i sigma2`; 22 `block_form gamma^(x0)gamma^(x4) = j sigma1`; 23 `block_form B = j s2 (number)`; 24 `block_form C = s2 sigma2`; 25 `block_form J = j`; 26 `block_form K1 = i s2`; 27 `block_form K2 = i s3`; 28 `block_form gamma^(x4)gamma^(x1) = -j sigma3`; 29 `block_form B gamma^(x0) = j s2 sigma3`; 30 `product_of_4D_and_internal_chirality`; 31 `chirality_squares`.

**geo** (`um2_geometry.py`, 25 checks, all passed): 1 `y_chart_pair_diagonal`; 2 `author_chart_pair_diagonal`; 3 `charts_agree`; 4 `einstein_from_ricci_equals_pairing_k1`; 5 `gauss_bonnet_tensor_equals_pairing_k2`; 6 `bianchi_identity_k1`; 7 `bianchi_identity_k2`; 8 `bianchi_identity_k3`; 9 `lapse_metric_pair_diagonal`; 10 `minisuperspace_variation_k1`; 11 `minisuperspace_variation_k2`; 12 `minisuperspace_variation_k3`; 13 `hidden_equals_extra_times_k1`; 14 `hidden_equals_extra_times_k2`; 15 `hidden_equals_extra_times_k3`; 16 `record_equation constraint_x4`; 17 `record_equation space_x1_eq_x2_eq_x3`; 18 `record_equation hidden_and_extraTimes_x0_eq_x5_eq_x6_eq_x7`; 19 `static_block_constraint`; 20 `static_block_space`; 21 `static_block_hidden`; 22 `vielbein`; 23 `gamma_covariantly_constant`; 24 `gamma_mu_Omega_mu`; 25 `nontrivial_unless_flat`.

**bg** (`um2_background.py`, 22 checks, all passed): 1 `hidden_equals_extra_times_k1`; 2 `hidden_equals_extra_times_k2`; 3 `hidden_equals_extra_times_k3`; 4 `class_form_equals_full_tensor`; 5 `static_block_x4`; 6 `static_block_x0`; 7 `static_vacuum_general`; 8 `newton_factor_at_vacuum`; 9 `newton_factor_author_roots`; 10 `stabiliser_requirement`; 11 `casimir_type_static_blocks`; 12 `casimir_type_attractive_gravity`; 13 `casimir_type_positive_energy`; 14 `second_order_system_solvable`; 15 `static_point_is_a_solution`; 16 `block_stable_nu1`; 17 `block_stable_family`; 18 `sourced_radion_equation`; 19 `static_block_response`; 20 `internal_lovelock_densities`; 21 `reduction_newton_factor`; 22 `reduction_cosmological_term`.

**fld** (`um2_fields.py`, 16 checks, all passed): 1 `dirac_reduction_exact`; 2 `gamma4_block_form`; 3 `selection_operator_lorentz_invariant`; 4 `selected_blocks`; 5 `bc_lagrangian`; 6 `zero_mode_general_solution`; 7 `zero_modes_dirac16complex`; 8 `zero_modes_doublet`; 9 `zero_modes_singlet`; 10 `weyl_helicity_definite`; 11 `zero_mode_dispersion`; 12 `tip_mixing_self_adjoint`; 13 `tip_mixing_self_adjoint_three_generations`; 14 `gauge_x0_operator`; 15 `gauge_boundary_conditions`; 16 `tip_terms_gauge_invariant`.

**mass** (`um2_spectra.py`, 14 checks, all passed): 1 `unbroken_spectrum_exact`; 2 `fem_crosscheck_unbroken`; 3 `massless_zero_mode`; 4 `gap`; 5 `dirichlet_tip_bound`; 6 `custodial_leading_order`; 7 `rho_fit`; 8 `mZ_reproduced`; 9 `fem_crosscheck_W`; 10 `scales`; 11 `fermion_fit`; 12 `first_order_formula`; 13 `shooting_crosscheck`; 14 `localisation_lowers_mass`.

**flav** (`um2_flavour.py`, 7 checks, all passed): 1 `PMNS_unitary_and_Jarlskog`; 2 `CKM_unitary_and_Jarlskog`; 3 `three_generation_tip_condition_exact`; 4 `general_tip_matrix`; 5 `no_tree_level_FCNC_from_KK`; 6 `mu_to_e_gamma`; 7 `lepton_universality`.

**nu** (`um2_neutrino.py`, 16 checks, all passed): 1 `masses_and_cosmological_bound`; 2 `vacuum_oscillations`; 3 `MSW_resonance_13`; 4 `long_baseline_matter_and_CP`; 5 `solar_MSW`; 6 `early_universe_oscillation_onset`; 7 `plasma_integrals`; 8 `N_eff_method_validation`; 9 `N_eff_three_flavours`; 10 `CNB_three_mass_states`; 11 `supernova_MSW`; 12 `fast_flavour_solver_consistency`; 13 `fast_flavour_crossing_criterion`; 14 `fast_flavour_time_scale`; 15 `equipartition_reduces_heating`; 16 `N7_dirac_or_majorana`.

**ksv** (`um2_ks_jobs.py validate`, 2 checks, all passed): 1 `validate_N8_lamp1_a00`; 2 `validate_N592_lamp1_a00`.

**kss** (`um2_ks_jobs.py spectrum`, 3 checks, all passed): 1 `spectrum_exact_k0`; 2 `fold_band_massless`; 3 `j_mirror_k0`.

**ks8** (`um2_ks_jobs.py ground8`, 3 checks, all passed): 1 `ground_basis_convergence`; 2 `ground_y_conservation`; 3 `ground_energy_equals_integrated_rho`.

**ks592** (`um2_ks_jobs.py ground592`, 4 checks, all passed): 1 `ground_basis_convergence`; 2 `ground_y_conservation`; 3 `ground_energy_equals_integrated_rho`; 4 `fold_band_gas_radiation`.

**ksdm** (`um2_ks_jobs.py darkmatter`, 3 checks, all passed): 1 `dm_energy_bookkeeping`; 2 `dm_cold`; 3 `dm_hidden_pressure_identity`.

**ksp** (`um2_ks_jobs.py portals`, 5 checks, all passed): 1 `portal_HF I11 vector contact, electron density (v)`; 2 `portal_HF I11 vector contact, up-quark density (v)`; 3 `portal_HF I11 vector contact, neutrino density (v, left-chiral)`; 4 `portal_HF I12 gluon condensate <G G> (M, uniform)`; 5 `scalar_density_vanishes_at_tip`.

**ksfb** (`um2_ks_jobs.py feedback`, 2 checks, all passed): 1 `block_response`; 2 `friedmann_decoupled_from_block_shift`.

**ew** (`um2_electroweak.py`, 19 checks, all passed): 1 `electric_charges`; 2 `W_charges`; 3 `photon_coupling`; 4 `Z_coupling`; 5 `anomaly_cancellation`; 6 `P_plus_projector_hermitian`; 7 `P_plus_lorentz_invariant`; 8 `chiral_current_is_vector`; 9 `B_lorentz_invariant`; 10 `Gamma4_equals_minus_B_gamma0`; 11 `P_plus_block_form`; 12 `sm_zero_modes_in_psiA_blocks`; 13 `tip_condition_b_zero`; 14 `Z_charge_fold_band`; 15 `Z_charge_dark_matter`; 16 `Z_invisible_width`; 17 `tip_Z_portal_dropped`; 18 `Z_width_scheme`; 19 `Z_widths_three_generations`.

**prim** (`um2_primordial.py`, 5 checks, all passed): 1 `constraint_preserved`; 2 `radion_oscillation`; 3 `radion_dust_expansion`; 4 `basin_separatrix`; 5 `deflation_factor`.

**cos** (`um2_cosmology.py`, 8 checks, all passed): 1 `theta_star_matched`; 2 `three_massive_neutrinos`; 3 `cmb_spectra_close_to_lcdm`; 4 `bao_desi`; 5 `dark_radiation_variants`; 6 `neff_and_helium`; 7 `freeze_in_radiation`; 8 `sigma8_and_first_order_potential`.

**ana** (`um2_analysis.py`, 23 checks, all passed): 1 `A1_flat_form_identity`; 2 `A2_gap_theorem`; 3 `A3_sum_rules`; 4 `A3_uncertainty_relation_on_the_cell`; 5 `A3_zero_mode_localised_but_massless`; 6 `A3_W_mass_from_the_tip`; 7 `A3_heisenberg_bounds_excitations`; 8 `A3_fermions_far_below_heisenberg`; 9 `A3_sharper_localisation_lighter_fermion`; 10 `A4_coordinate_vs_proper`; 11 `A5_sensitivities`; 12 `B1_mass_cold_neutral`; 13 `B2_spin_trace`; 14 `B2_polarisation_sum`; 15 `B2_cross_section_formula`; 16 `B3_relic_requirement_and_unitarity`; 17 `B4_direct_detection`; 18 `B5_stability_and_neutrality`; 19 `C1_no_positive_energy_state_accelerates`; 20 `C2_condensate_not_dark_energy`; 21 `C3_vacuum_energy_and_tuning`; 22 `C4_radion_moduli_problem`; 23 `A6_block_frozen_today`.

**th** (`um2_thermal.py`, 7 checks, all passed): 1 `T1_degrees_of_freedom`; 2 `T2_thermal_average`; 3 `T3_boltzmann_solver`; 4 `T4_relic_numerical`; 5 `T5_unitarity_violated_by_effective_operator`; 6 `T5_unitarity_limited_relic`; 7 `T6_I12_benchmark`.

**cpl** (`um2_coupled.py`, 16 checks, all passed): 1 `C1_overlaps`; 2 `C1_screened_response`; 3 `C1_fold_band_massless`; 4 `C2_freeze_in_benchmark`; 5 `C3_direct_detection_I11`; 6 `C8_I13_algebra`; 7 `C8_I13_overlaps_and_fold_band`; 8 `C8_I13_relic`; 9 `C8_I13_direct_detection`; 10 `C9_B_minus_L_alternative_thermalises_nuR`; 11 `C10_self_interaction_channel`; 12 `C6_proton_sensitivity`; 13 `C4_mean_fields_in_environments`; 14 `C6_gravity_loop`; 15 `C5_WZ_and_photon`; 16 `C7_validity_domain`.

**ser** (`um2_series.py`, 4 checks, all passed): 1 `S2_first_order_n0`; 2 `S3_kaluza_klein_gravitons`; 3 `S4_radion`; 4 `S7_decreasing_magnitudes`.

**res** (`um2_residuals.py`, 52 checks, all passed): 1 `R_einstein_lovelock_background`; 2 `R_block_linear_response`; 3 `R_primordial_deflation_system`; 4 `R_four_dimensional_effective_gravity`; 5 `R_boson_x0_eigenvalue`; 6 `R_fermion_x0_tip_determinant`; 7 `R_dirac16complex_x0_spectrum`; 8 `R_kohn_sham_scf`; 9 `R_kohn_sham_in_gravity_block_response`; 10 `R_portal_overlaps_hellmann_feynman`; 11 `R_coupled_environment_mean_fields`; 12 `R_wz_x0_with_dark_matter_kinetic_function`; 13 `R_yang_mills_masses_and_widths`; 14 `R_linear_perturbations_cmb_bao`; 15 `R_graviton_tower`; 16 `R_metric_series_order2`; 17 `R_neutrino_flavour_evolution`; 18 `R_neutrino_thermal_potential`; 19 `R_neutrino_decoupling`; 20 `R_fast_flavour_dispersion`; 21 `R_cosmic_neutrino_background`; 22 `R_thermal_degrees_of_freedom`; 23 `R_boltzmann_relic`; 24 `R_freeze_in`; 25 `R_right_handed_neutrino_boltzmann`; 26 `R_self_interaction_channel`; 27 `L_ks_energy_density_in_block_response`; 28 `L_dark_matter_hidden_pressure`; 29 `L_z_mass_x0_vs_z_widths`; 30 `L_weak_angle_x0_vs_z_widths`; 31 `L_fermion_masses_x0_vs_thermal_history`; 32 `L_neutrino_masses_tip_matrices_vs_flavour_cnb_cmb`; 33 `L_pmns_tip_matrix_vs_flavour_evolution_and_cnb`; 34 `L_omega_nu_cnb_vs_camb`; 35 `L_neff_decoupling_plus_freeze_in_vs_camb`; 36 `L_relic_density_vs_cmb_omega_c`; 37 `L_hubble_rate_thermal_vs_four_dimensional_friedmann`; 38 `L_late_time_radiation_thermal_vs_cmb`; 39 `L_plasma_energy_density_thermal_vs_coupled_sources`; 40 `L_portal_responses_ks_jobs_vs_coupled_overlaps`; 41 `L_i12_response_O_across_scripts`; 42 `L_i12_benchmark_thermal_vs_coupled_mean_field`; 43 `L_dark_matter_mass_ks_vs_boltzmann`; 44 `L_relic_and_freeze_in_couplings_in_mean_fields`; 45 `L_w_eigenvalue_x0_vs_kinetic_function_problem`; 46 `L_block_response_coefficients_across_scripts`; 47 `L_radion_frequency_linear_vs_nonlinear`; 48 `L_static_block_f_star_across_scripts`; 49 `L_decoupling_heating_factor_F_h`; 50 `L_metric_series_vs_cosmology_coupled_masses`; 51 `L_freeze_out_temperature_relic_vs_environment`; 52 `L_block_sensitivities_x0_formula_vs_block_response`.

```{=latex}
\par\endgroup
```

## The principal numbers and where they come from

| quantity | value | script (output) |
|:------------------|:-----------------------------------------------|:--------------------------|
| static block | $K_* = 12 + \frac43\sqrt{51} = 21.5219$, $f_* = 0.215556$, $\mathcal{G}(K_*) = \frac{20}{3} + \sqrt{51} = 13.8081$, $\kappa\rho_{\mathrm{stab}}(f_*) = (26 + 4\sqrt{51})H^2$ | background (background.json) |
| radion | $\omega_{\mathrm{r}}^2/H^2 = 31552/2249 - 2416\sqrt{51}/6747 = 11.4721$, $\omega_{\mathrm{r}} = 3.387H = 48.42$ TeV | background, spectra (background.json, masses.json) |
| unbroken $x_0$ spectrum ($HL = 3$) | $\tilde m = 0$ (flat profile); first even level $\tilde m_1^2 = 30.1196$; first odd level $\tilde m^2 = 27.0890$; gap $9H^2L^2/4 = 20.25$ | spectra (masses.json) |
| $W^\pm$, $Z$ | $\beta_{\mathrm{W}} = 0.011912$, $\beta_{\mathrm{Z}} = 0.015343$ ($\cos^2\theta_{\mathrm{W}} = 0.776368$), $\tilde m_{\mathrm{W}}^2 = 1.32149\times10^{-5}$, $\tilde m_{\mathrm{Z}}^2 = 1.70150\times10^{-5}$, $\rho_{\mathrm{EW}} - 1 = 0.00038$, model $m_{\mathrm{Z}} = 91.1879$ GeV; Dirichlet bound of the tip $\tilde m^2 = 0.010016$ | spectra (masses.json) |
| scales | $m_{\mathrm{KK}} = 121.32$ TeV, $H = 14.296$ TeV, proper half cell $fL = 8.926\times10^{-21}$ m, $x_0$ period $7.227\times10^{-21}$ m, gap $3H/(2f) = 99.48$ TeV | spectra (masses.json) |
| fermion localisations ($\mathcal{K} = 1$) | doublets $c_L = 5.9529$ (leptons), $3.3823$ (quarks); singlets $c_R$: $\nu_1$ $-35.0452$, $\nu_2$ $-32.8481$, $\nu_3$ $-31.0702$, electron $-14.5539$, muon $-8.9809$, tau $-5.9529$, up $-15.4300$, charm $-8.7683$, top $-3.3823$, down $-14.6258$, strange $-11.5158$, bottom $-7.5005$ | spectra (masses.json) |
| three generations | the roots of the tip determinant equal the one-generation roots to $3.0\times10^{-42}$, the null vectors the columns of $\mathcal{K}$ to $1.1\times10^{-16}$; a general complex tip matrix: singular values to $3.5\times10^{-5}$ | flavour (flavour.json) |
| mixing | PMNS ($\theta_{12} = 33.71^\circ$, $\theta_{13} = 8.56^\circ$, $\theta_{23} = 43.28^\circ$, $\delta_{\mathrm{CP}} = 212^\circ$) unitary to $1.1\times10^{-16}$, $J_{\mathrm{CP}} = -0.01777$; CKM $J_{\mathrm{CP}} = 3.117\times10^{-5}$; Kaluza-Klein gauge overlaps $0.14434$ (leptons), $-0.30066$ (quarks), off-diagonal $1.0\times10^{-17}$; branching ratio of $\mu \to e\gamma$ $2.8\times10^{-55}$ | flavour (flavour.json) |
| neutrino masses | $m_1 = 1.000$, $m_2 = 8.712$, $m_3 = 50.140$ meV; $\sum_im_i = 0.0599$ eV | spectra, neutrino (masses.json, neutrino.json) |
| flavour conversion | 1-3 MSW resonance 11.135 GeV (exact 11.133 GeV) at 2.8 g/cm$^3$; solar 1-2 resonance 1.93 MeV; $\mathcal{P}(\nu_\mu\to\nu_e)$: T2K 0.0517, NOvA 0.0481, DUNE 0.0701 (antineutrinos 0.0313, 0.0236, 0.0195); solar $\mathcal{P}_{ee}$ from 0.5408 (pp) to 0.3043 ($^8$B, 15 MeV) | neutrino (neutrino.json) |
| early Universe | oscillation onset $T = 4.99$ MeV (atmospheric), 2.39 MeV (solar); $N_{\mathrm{eff}} = 3.0476$ (separate temperatures), 3.0485 (common); adopted 3.0432 | neutrino (neutrino.json) |
| CNB | $T_\nu = 1.9454$ K, 112.0 cm$^{-3}$ per mass state, $\bar v_i = 0.435133$, $0.0604083$, $0.0105352$; $\Omega_\nu h_{100}^2 = 6.38217\times10^{-4}$ (version 4: quadrature to $3\times10^{-16}$) | neutrino (neutrino.json, copied in cosmology.json) |
| supernovae | H resonance (20 MeV) at 1573 g/cm$^3$, adiabaticity $\gamma_{\mathrm{ad}} = 178$; $\mathcal{P}_{ee} = 0.02215$, antineutrinos 0.677; fast instability growth 0.0877 and 0.0979 in units of $\sqrt2G_{\mathrm{F}}n_{\nu_e}$, e-folding in $5.9\times10^{-10}$ to $5.9\times10^{-11}$ s; heating factors 0.884, 0.760 | neutrino (neutrino.json) |
| dirac16complex at $f_*$ | $c_\Psi = 0.646667$; $\varepsilon_{\mathrm{DM}} = 3.102204\,m_\Psi$ ($\varpi = 1.89901$, an $x_0$ wave number of $2.93661\,m_\Psi$); lowest even bulk level $4.959981\,m_\Psi$; $x_0$-momentum fraction 0.896 | ks_jobs spectrum (ks/spectrum.json) |
| dark matter | $M_{\mathrm{DM}} = 44.35$ TeV (both halves); $p_3/\rho = 0$; $p_0/\rho = 0.772034343 = -\mathrm{d}\ln\varepsilon_{\mathrm{DM}}/\mathrm{d}\ln f$ | ks_jobs darkmatter (ks/darkmatter.json) |
| portal responses | the dark-matter level per unit amplitude of the mean field: I11 electron density 0.824779, up-quark density 4.328803, neutrino density 1.252406; I12 gluon condensate 0.707196 ($= \mathcal{O}_{\mathrm{DM}}$); the fold-band gap changes by $7.9\times10^{-11}$, $3.0\times10^{-9}$, $-9.3\times10^{-11}$, $-1.4\times10^{-10}$ (zero in exact arithmetic; version 4) | ks_jobs portals (ks/portals.json) |
| tip $Z$ portal (removed) | $N_\nu = 3 + 2r_{\mathrm{Z}}^2$, $r_{\mathrm{Z}}^2 < 0.0056$; at the bound decoupling at 14.7 MeV and $\Delta N_{\mathrm{eff}} = 2.02$; oriented part $\Delta N_{\mathrm{eff}} = 0.0958$ to 0.1257 | electroweak (electroweak.json) |
| $Z$ widths | invisible 497.7 MeV (measured 499.1), total 2422.3 MeV at tree level, 2485.2 MeV with $1 + \alpha_3/\pi$ (measured 2495.5); hadronic ratio $R_\ell = 20.83$ (measured 20.77) | electroweak (electroweak.json) |
| primordial era | separatrix at $K = 2.6983$, 2.5991, 2.5301 (for the initial $\mathcal{H}_f = -H/2$, $-H/3$, $-H/10$); deflation factor up to 2.9166; radion frequency $3.3868H$ measured | primordial (primordial.json) |
| cosmology | UM-2 (version 3, $N_{\mathrm{eff}} = 3.0442$): $\mathcal{H}_0 = 67.38$ km/s/Mpc, $\Omega_{\mathrm{m}} = 0.3150$, $r_{\mathrm{d}} = 147.104$ Mpc, $\chi_{\mathrm{BAO}}^2 = 31.49$ (13 points; $\Lambda$CDM 32.55), TT and EE within $2.5\times10^{-4}$ and $2.7\times10^{-4}$ of $\Lambda$CDM; without the freeze-in fold bands ($N_{\mathrm{eff}} = 3.0432$): 67.37, 0.3151, 147.109 Mpc, 31.72, $2.8\times10^{-4}$ | cosmology (cosmology.json) |
| relic with I12 alone (version 2) | two species, $x_{\mathrm{f}} = 30.38$, $g_\rho = 105.75$, required $\langle\sigma v_{\mathrm{rel}}\rangle = 2.01\times10^{-25}$ cm$^3$/s per species, $G_{\mathrm{I12}} = (15.5\ \text{TeV})^{-3}$; the $^3P_0$ bound $\sqrt{\pi x_{\mathrm{f}}}/M_{\mathrm{DM}}^2 = 5.79\times10^{-26}$ cm$^3$/s exceeded 3.47 times ($v_{\mathrm{c}} = 0.263$, 79 % of the pairs above it): OPEN in version 2, resolved in version 3 by I13 | analysis (analysis.json) |
| direct detection (gluons only) | $\sigma_{\mathrm{SI}} = 6.3\times10^{-53}$ cm$^2$ against $2.4\times10^{-45}$ cm$^2$ | analysis (analysis.json) |
| dark energy | condensate tuned to $w_{\mathrm{de},0} = -1$: $w_{\mathrm{de},a} = -6$, energy zero at $z_{\mathrm{red}} = 0.260$; natural vacuum energy $5.5\times10^{64}$ times the observed one; $(\mathcal{H}_0/H)^2 = 1.0\times10^{-92}$ | analysis (analysis.json) |
| uncertainty relation | $m/m_{\mathrm{Heis}}$: first Kaluza-Klein level 7.49, first odd level 6.47, dark matter 2.29, $W^\pm$ $1.14\times10^{-3}$, $Z$ $1.29\times10^{-3}$, top quark $3.2\times10^{-3}$, electron $5.5\times10^{-9}$, $\nu_1$ $1.1\times10^{-17}$; $\langle k_\xi^2\rangle\Delta\xi^2$: photon zero mode 0.497, fold zero mode of $\Psi$ 0.097 ($\varrho_\xi(-1) = 0.489$); $\langle k_\xi^2\rangle^{1/2}\Delta\xi \ge (1 - \varrho_\xi(-1))/2$ for every tabulated state | analysis (analysis.json) |
| block sensitivities | logarithmic derivatives with respect to $\ln f$: Kaluza-Klein masses $-1$, $m_{\mathrm{W}}$ $-0.501$, fermions from $-6.8$ (top) to $-41.0$ ($\nu_1$), $m_{\mathrm{e}}$ $-20.5$, $M_{\mathrm{DM}}$ $-0.772$, $\alpha_{\mathrm{em}}$ and the gauge couplings $-4$, $G_{\mathrm{N}}$ $+2.05$; splittings $\Delta m_{21}^2$ $-77.5$, $\Delta m_{31}^2$ $-74.0$ | analysis (analysis.json) |
| block rate today (ESTIMATE) | $\lvert\mathcal{H}_f\rvert < 3.6\times10^{-8}\mathcal{H}_0$ (atomic clocks, change of $\alpha_{\mathrm{em}}$ below $10^{-17}$ per year), $< 7.1\times10^{-4}\mathcal{H}_0$ (lunar ranging, change of $G_{\mathrm{N}}$ below $10^{-13}$ per year) | analysis (analysis.json) |
| radion decay (ESTIMATE) | $\Gamma_{\mathrm{r}} = C_{\mathrm{r}}\,\omega_{\mathrm{r}}^3/(4\pi\bar M_{\mathrm{Pl}}^2)$, $T_{\mathrm{RH}} = (90/(\pi^2g_\rho))^{1/4}(\Gamma_{\mathrm{r}}\bar M_{\mathrm{Pl}})^{1/2}$ ($g_\rho = 10.75$): lifetime $0.43\,\text{s}/C_{\mathrm{r}}$, $T_{\mathrm{RH}} = 1.85\,C_{\mathrm{r}}^{1/2}$ MeV (below 4.7 MeV unless $C_{\mathrm{r}} > 6.5$) | analysis (analysis.json) |
| first-order block response | $\Xi_{f3} = 0.028666$, $\Xi_{fp} = 0.037320$, $\Xi_{f\rho} = -0.009555$; adiabatic $\Delta K = (0.035852\,\kappa\Delta\rho - 0.107556\,\kappa\Delta p_3 - 0.140028\,\kappa\Delta\bar p)/H^2$ (radiation drops out: $0.107556 = 3\times0.035852$); for the Kohn-Sham states $\Delta K/\kappa = 2.27\times10^{-6}$ (8 particles, $+\lambda_{\mathrm{test}}$), 0.0125 (592 particles, $+\lambda_{\mathrm{test}}$), 0 (free gas), in units $H = 1$ | background, ks_jobs feedback (background.json, ks/feedback.json) |
| thermal history (version 3) | $g_\rho = 105.75$ (5 TeV), 105.73 (1.42 TeV), 104.95 (200 GeV), 86.22 (10 GeV), 10.74 (3 MeV); today $g_s = 3.9091$, $g_\rho = 3.3626$, $s_0 = 2891.3$ cm$^{-3}$; the relativistic thermal average exceeds the non-relativistic one by about $3/x$ | thermal (thermal.json) |
| I12 relic and unitarity (version 3) | $G_{\mathrm{I12}} = (15.855\ \text{TeV})^{-3}$, $x_{\mathrm{f}} = 31.70$, $\langle\sigma v_{\mathrm{rel}}\rangle(x_{\mathrm{f}}) = 1.891\times10^{-25}$ cm$^3$/s; crossing of the $^3P_0$ bound at $E_{\mathrm{cm}} = 89510$ GeV, $v_{\mathrm{rel}} = 2\beta_{\mathrm{cm}} = 0.269$ (0.274 from the non-relativistic formula), 96 % of the rate and 75 % of the pairs above it; at the $^3P_0$ limit 0.0582 per species ($x_{\mathrm{f}} = 30.77$, $\langle\sigma v_{\mathrm{rel}}\rangle = 5.33\times10^{-26}$ against $\sqrt{\pi x}/M_{\mathrm{DM}}^2 = 5.84\times10^{-26}$ cm$^3$/s); benchmark fraction above its crossing $5.2\times10^{-4}$; capped: 0.1544, 0.1081, 0.0836, 0.0649, 0.0585; the benchmark $(38.2\ \text{TeV})^{-3}$ alone 8.0; $c_{\mathrm{I12}}/\Lambda_\star^3 = 1.106\times10^{-14}$ GeV$^{-3}$ | thermal (thermal.json) |
| I13 relic (version 3) | $\mathcal{S}_B = 16.351$; $G_{\mathrm{A}} = 1.278\times10^{-9}$ GeV$^{-2}$ (capped; $1.269\times10^{-9}$ without the cap); $x_{\mathrm{f}} = 31.23$; $\langle\sigma v_{\mathrm{rel}}\rangle(x_{\mathrm{f}})$: I13 $9.50\times10^{-26}$, I12 $9.9\times10^{-28}$ cm$^3$/s; bound reached above $v_{\mathrm{rel}} = 0.51$ (22 % of the rate; the uncapped cross-section crosses it above 0.52, 25 %); $B - L$ alternative: $G_{\mathrm{A}}^{B-L} = 1.072\times10^{-9}$ GeV$^{-2}$, $\nu_R$ at 0.999698 of equilibrium at $x = 40$, kinetic decoupling at $x = 24.4$, $\Delta N_{\mathrm{eff}} = 0.144$; with $J^B$ the $\nu_R$ production through I11 is $r_{\nu_R} = 2.0\times10^{-17}$ | coupled (coupled.json) |
| self-interaction channel (version 3) | $\tilde I_\lambda = 14.38$; $\Delta N_{\mathrm{eff}} = 1.83\times10^{26}\,G_\lambda^2$ GeV$^4$; bound $G_\lambda \le 2.3\times10^{-15}$ GeV$^{-2}$ ($1.8\times10^{-6}G_{\mathrm{A}}$); $\lambda_{\mathrm{test}}$ with $v_{\mathrm{t}} = H^{-3}$: $G_\lambda = 1.14\times10^{-9}$ GeV$^{-2}$, fold bands thermalised to 2.6 TeV, $\Delta N_{\mathrm{eff}} = 0.19$ | coupled (coupled.json) |
| freeze-in and detection (version 3) | $\sum_fN_{\mathrm{c}}(q_f\tilde I_{of})^2 = 126.85$; $\Delta N_{\mathrm{eff}} = 5.21\times10^{29}G_{\mathrm{V}}^2$ GeV$^4$; $G_{\mathrm{V}} = 4.38\times10^{-17}$ GeV$^{-2}$; production rate per fold quantum 0.012 of $\mathcal{H}$ at 10 TeV; xenon $\sigma_{\mathrm{SI}} = 4.01\times10^{-46}$ cm$^2$ (0.16 of LZ); $\langle\sigma v_{\mathrm{rel}}\rangle$ today $9.76\times10^{-26}$ cm$^3$/s | coupled (coupled.json) |
| coupled solution (version 3) | overlaps $\tilde I_Q = 8.2722$, $\tilde I^{(b)}_Q = 2.6135$ (dark matter); Kohn-Sham checks $3.1\times10^{-10}$, $2.3\times10^{-10}$; the I13 algebra exact; $\Delta\varepsilon_{\mathrm{DM}}/M_{\mathrm{DM}} \le 1.5\times10^{-6}$ (at the freeze-out, $T = 1.42$ TeV; thermal condensates $-8.1\times10^{12}$, $-5.0\times10^{11}$, $-2.6\times10^{10}$ GeV$^4$; Feynman-Hellmann against the trace anomaly $10^{-16}$); $\Delta\ln f \le 1.1\times10^{-34}$ (the hot plasma at the freeze-out; $7\times10^{-39}$ in the electroweak era, $9\times10^{-49}$ from nucleosynthesis on); loop gain $\le 1.1\times10^{-33}$; $\mathrm{d}\ln m_{\mathrm{p}}/\mathrm{d}\ln f = -46.1$; $A_{\mathrm{mf}} = 1.7\times10^{-16}$ at the freeze-out; $\mathrm{d}\ln\tilde m_{\mathrm{W}}^2/\mathrm{d}A_{\mathrm{mf}} = -0.111253$ (version 4; version 3: $-0.1126$); validity up to $T = 27.4$ TeV | coupled (coupled.json) |
| metric series and $\sigma_8$ (version 3) | $\Phi_{\mathrm{rms}} = 2.42\times10^{-5}$ ($k = 10^{-4}$ Mpc$^{-1}$) to $5.03\times10^{-8}$ (1 Mpc$^{-1}$); order 2: $5.8\times10^{-10}$; $D_+\mathrm{e}^{-a_4} = 0.7878$ today; graviton levels $\tilde m_n^2 = 30.1196$, 59.7284, 109.0764; Yukawa strengths $\mathcal{A}_n = 0.0728$, 0.1469, 0.1809 (two masses at the fold); range $1.63\times10^{-21}$ m; radion $\le 1.1\times10^{-34}$; $\sigma_8 = 0.8118$ (UM-2), 0.8119 (without the freeze-in fold bands), 0.8109 ($\Lambda$CDM) | series, cosmology (series.json, cosmology.json) |
| Majorana alternative (version 3) | $\mathcal{K}_{\mathrm{M}}^{(i)} = 5.63\times10^{-13}$, $4.90\times10^{-12}$, $2.82\times10^{-11}$; $m_{\beta\beta}$ from 0.84 to 4.41 meV | neutrino (neutrino.json) |
| residuals (version 4) | 26 field equations: residuals from $7.4\times10^{-14}$ to $2.4\times10^{-5}$, each within its tolerance; 26 links: five not zero (section 10) | residuals (residuals.json) |

## Methods

* **Exact checks.** Symbolic identities are verified with sympy by simplifying the difference to zero; matrix identities
  entry by entry, with the author's matrices.
* **Roots.** The transcendental eigenvalue conditions (FE-52, FE-59, FE-60, FE-62) are solved with mpmath at 30 to 60
  digits; the residual analysis measures each stored root by its implied relative error, the value of the condition divided
  by the eigenvalue times the derivative of the condition.
* **Richardson extrapolation.** A number computed with the discretisation size $\mathsf{n}$, $2\mathsf{n}$ and $4\mathsf{n}$ is
  extrapolated and its observed order measured by

$$
\mathsf{X}_\infty \simeq \mathsf{X}_{2\mathsf{n}} + \frac{\mathsf{X}_{2\mathsf{n}} - \mathsf{X}_{\mathsf{n}}}{\mathrm{e}^{p_{\mathrm{obs}}\ln2} - 1},
\qquad p_{\mathrm{obs}} = \frac{1}{\ln2}\,\ln\frac{\mathsf{X}_{\mathsf{n}} - \mathsf{X}_{2\mathsf{n}}}{\mathsf{X}_{2\mathsf{n}} - \mathsf{X}_{4\mathsf{n}}}
$$

<!-- symbols: prov_RichX, prov_Richn, euler, prov_pobs -->
<!-- begin generated symbol list -->
**Symbols in this equation.**

- $\mathsf{X}_{\mathsf{n}},\ \mathsf{X}_\infty$: A computed number (an eigenvalue, an energy, an integral of the Kohn-Sham stress, a derivative) obtained with the discretisation size $\mathsf{n}$, whose discretisation error is a constant times $\mathsf{n}^{-p_{\mathrm{obs}}}$; $\mathsf{X}_{\mathsf{n}}$, $\mathsf{X}_{2\mathsf{n}}$, $\mathsf{X}_{4\mathsf{n}}$ are its values for the sizes $\mathsf{n}$, $2\mathsf{n}$, $4\mathsf{n}$, and $\mathsf{X}_\infty$ is the value extrapolated to an infinite size (Richardson extrapolation). Unit: the unit of the computed quantity. Status: STANDARD.
- $\mathsf{n}$: The size of a discretisation that is doubled from one computation to the next: the number of free eigenfunctions per sector of the Kohn-Sham basis (60, 120, 240), the number of finite elements (100, 200, 400), or the inverse of the step of a finite difference. Unit: dimensionless. Status: STANDARD.
- $\mathrm{e}$: Euler's number, the base of the natural logarithm; $\mathrm{e}^{X}$ is the exponential of $X$. Unit: dimensionless. Value: 2.718281828. Status: STANDARD.
- $p_{\mathrm{obs}}$: The observed order of convergence of a sequence of computations with the sizes $\mathsf{n}$, $2\mathsf{n}$, $4\mathsf{n}$: the exponent of the discretisation error, which behaves as a constant times $\mathsf{n}^{-p_{\mathrm{obs}}}$ (not a pressure). Unit: dimensionless. Value: 4.96 for the Kohn-Sham energy of the stress state, 2.97 for its integrated hidden pressure, 4.01 for the finite-element eigenvalue of the $W$. Status: DERIVED.

<!-- end generated symbol list -->

* **Finite elements.** As a cross-check of the boson eigenvalues, quadratic finite elements on 100, 200 and 400 elements
  solve the weak form of FE-50 with the tip condition of FE-51; the eigenvalue is the Rayleigh quotient of the gradient
  form,

$$
\int_{-1}^{0}\mathrm{e}^{3HL\xi}\Big(\frac{\mathrm{d}F}{\mathrm{d}\xi}\Big)^2\mathrm{d}\xi + \beta\,\mathrm{e}^{-3HL}F(-1)^2
 = \tilde m^2\int_{-1}^{0}\mathrm{e}^{3HL\xi}F^2\,\mathrm{d}\xi
$$

<!-- symbols: diff, euler, Hconst, Lcut, xi, Fprof, betaRobin, mtilde -->
<!-- begin generated symbol list -->
**Symbols in this equation.**

- $\mathrm{d}$: The differential: $\mathrm{d}X$ is an infinitesimal change of $X$, $\mathrm{d}X/\mathrm{d}Y$ the derivative of $X$ with respect to $Y$, $\mathrm{d}^nX$ the volume element of $n$ variables. Status: STANDARD.
- $\mathrm{e}$: Euler's number, the base of the natural logarithm; $\mathrm{e}^{X}$ is the exponential of $X$. Unit: dimensionless. Value: 2.718281828. Status: STANDARD.
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the Lovelock couplings, the cosmological constant $\Lambda = -10H^2$ and the mass parameter $m_\Psi = H$. Unit: GeV (1/length). Value: 14.296 TeV (from the fit of $m_{\mathrm{W}}$ and $\rho_{\mathrm{EW},0}$). Status: AUTHOR.
- $L$: The depth of the regular tip: each half of a period of $x_0$ ends at $y = -L$; $HL = 3$. Unit: length. Value: $L = 3/H$ ($fL = 8.926\times10^{-21}$ m at the stabilised block). Status: ASSUMED.
- $\xi$: The scaled hidden coordinate, $\xi = y/L$, running from $-1$ (tip) to $0$ (fold) on each half of a period. Unit: dimensionless. Status: DERIVED.
- $F(\xi),\ F_n$: The $x_0$ profile of a boson mode on one half of the period (a function of $y$ or of $\xi = y/L$): of a gauge field (gauge $A_y = 0$) or of the transverse-traceless graviton; $F_n$ is the profile of the $n$-th Kaluza-Klein level of the graviton tower ($F_0 = 1$ the flat zero mode). Unit: dimensionless. Status: DERIVED.
- $\beta$: The Robin parameter of the tip condition of a boson profile, $\mathrm{d}F/\mathrm{d}\xi = \beta F$ at $\xi = -1$ (zero for the massless gauge fields and the graviton). Unit: dimensionless. Status: DERIVED.
- $\tilde m,\ \tilde m_n$: The dimensionless $x_0$ eigenvalue of a boson mode, $\tilde m = m\,fL$; $\tilde m_n$ the $n$-th even Kaluza-Klein level of the tower with $\beta = 0$ ($\tilde m_1$ the first). Unit: dimensionless. Value: $\tilde m_1^2 = 30.1196$, $\tilde m_2^2 = 59.7284$, $\tilde m_3^2 = 109.0764$ ($HL = 3$), i.e. $\tilde m_1 = 5.48813$, $\tilde m_2 = 7.72842$, $\tilde m_3 = 10.44397$. Status: DERIVED.

<!-- end generated symbol list -->

  extrapolated by Richardson (observed order 4.01; $\tilde m_{\mathrm{W}}^2$ reproduced to $3.1\times10^{-14}$).
* **Kohn-Sham.** The orbitals of FE-63 are expanded in the exact eigenfunctions of the free problem of each sector (60, 120 or
  240 functions, quadrature with ten points per function); the mean fields FE-64 are iterated to self-consistency (tolerance
  $10^{-13}$) with a safeguarded Anderson mixing and a fixed labelling of the occupied set. Checks: the energy identity and
  the $y$-conservation law FE-68, Richardson in the basis size, the Hellmann-Feynman theorem for every portal mean field
  (the response of a level to a mean-field amplitude equals the expectation value of the perturbation), and the reproduction
  of the record's two reference states. Since version 4 the linear algebra runs single-threaded, so that the results do not
  depend on the number of cores (section 10).
* **Background and primordial era.** The 3-space and hidden components FE-39, FE-40 are solved for the two rates
  $\dot{\mathcal{H}}$ and $\dot{\mathcal{H}}_f$, with $\dot K = -2K\mathcal{H}_f$ and the stabiliser (plus radiation where
  stated); the constraint FE-38 fixes the initial $\mathcal{H}$ and is monitored (residual below $6\times10^{-10}$); DOP853
  integration, the separatrix by bisection in the initial $K$.
* **Neutrinos.** The flavour evolution FE-104 by exact matrix exponentials (constant density) and ordered products of 20000 and
  40000 layers (the Sun); the decoupling equations FE-111 to FE-114 with LSODA from 20 MeV to 5 keV (relative tolerance
  $10^{-11}$), validated against the published values of the method; the dispersion relation FE-117 by vectorised Newton
  iterations from a grid of complex starting points, checked against the analytic growth of FE-119 and the eigenvalues of
  the discretised homogeneous equation (300 nodes); the CNB FE-120 by adaptive quadrature.
* **Cosmology.** CAMB 2.0.5 solves FE-89 to FE-99 with the Planck 2018 parameters, the acoustic angle fixed (so $\mathcal{H}_0$
  is an output), multipoles to 2600, lensing included. UM-2 has three massive mass states, each with the degeneracy
  $N_{\mathrm{eff}}/3 = 1.0144$; CAMB gives each the density of a Fermi-Dirac gas times the degeneracy, so the masses passed to
  it are the masses divided by the fourth root of the degeneracy; because CAMB recovers them by inverting the relativistic
  density from the neutrino density and the mass fractions, these are iterated (damped exponent 0.8, 13 iterations) until
  the masses agree to $7.8\times10^{-12}$. The comparison model is CAMB's default (one neutrino of 0.06 eV,
  $N_{\mathrm{eff}} = 3.044$). The cosmic variance of one multipole is the relative error $\sqrt{2/(2l + 1)}$; the binned
  full-sky goodness of fit uses bins of 50 multipoles.
* **Thermal history and relic.** The ideal-gas integrals FE-121 by 160-point Gauss-Legendre quadrature on 360 temperatures from
  $10^{-4.5}$ to $10^{4.3}$ GeV; the Boltzmann equation FE-124 for $\ln Y_{\mathrm{DM}}$ with the implicit Radau method (relative
  tolerance $10^{-10}$) from $x = 5$ to 2000; the thermal average FE-125 by adaptive quadrature in the kinetic energy of the pair
  with exponentially scaled Bessel functions, tabulated on 200 to 260 points in $x$ and interpolated by a cubic spline; the
  strengths for $\Omega_{\mathrm{DM}}h_{100}^2 = 0.060$ per species by Brent's method in the logarithm of the strength; the
  freeze-in FE-129 and the self-interaction channel FE-136 by the trapezoid rule on 600 and 800 logarithmic temperatures.
* **Determinism.** Every computation is deterministic: the Kohn-Sham scripts and the residual analysis fix the number of
  threads of the linear algebra to one (version 4); the document build writes no dates into the LaTeX sources, suppresses
  the PDF dates and trailer identifiers and fixes `SOURCE_DATE_EPOCH`.

# The residuals of the approximate solution, and the precision fixes of version 4

## The residual analysis

The order of 2026-10-18, 15:42, asks for the approximate solution to be analysed "usually in concert with other field
equation". Version 4 adds the computation `um2_residuals.py` (outputs `residuals.json`, report `residuals-checks.json`, 52
checks). For every field equation (or system) that the solution uses, it records the solution (exact formula, numerical
method, order of the approximation); a precisely defined residual, either taken from the stored outputs or computed afresh
by substituting the stored solution into the equation; the size of the terms that the approximation drops; and the links in
concert, in which the same quantity is compared in the two or more places where different field equations use it (each
input is read where the script that uses it reads it). Every equation (res 1 to 26) and every link (res 27 to 52) has a
named check with a tolerance fixed in the script with a one-line justification; where a residual or a link is not small it
is reported as it is, and the tolerance is set by what the physics justifies. The script reads every output and writes only
its own; its linear algebra is single-threaded, so it gives the same numbers on every machine. For a root of a
transcendental condition the residual is the implied relative error (the value of the condition at the stored root divided by
the root times the derivative of the condition); for a differential equation it is the stored solution substituted into the
printed equation; for an integral it is an independent quadrature.

| | field equations | residual of the stored solution | largest neglected term |
|:----|:----------------|:---------------------------------------------|:---------------------------------------|
| res 1 | FE-38 to FE-40, FE-42, FE-43 | the static block in the printed equations: $3.9\times10^{-13}$ (the printed equations equal the code's symbolic ones) | the matter sources against the stabiliser: $3.0\times10^{-32}$ at the freeze-out, $2.4\times10^{-93}$ today |
| res 2 | FE-44 to FE-47 | the adiabatic response in the nonlinear equations: $1.4\times10^{-7}$ (second order, as expected) | second order and the inertia of the block at the freeze-out: $2.3\times10^{-32}$, $3.4\times10^{-33}$ |
| res 3 | FE-38 to FE-41 (primordial era) | constraint and one-step defect of the stored trajectories: $1.3\times10^{-11}$ | radiation of zero modes: $1.0\times10^{-6}$ of the final block |
| res 4 | FE-48, FE-49 | $\Lambda_4(K_*)$ and the $K$-derivative of the $x_4$ balance: $6.9\times10^{-13}$ | the dark energy, $\Lambda_4/H^2 \sim 10^{-92}$ (tuned, OPEN) |
| res 5 | FE-50 to FE-52, FE-55 | implied relative error of the stored eigenvalues: $5.9\times10^{-12}$ ($W$), $1.4\times10^{-12}$ ($Z$) | the I12 shift of $\tilde m_{\mathrm{W}}^2$ at the freeze-out: $1.9\times10^{-17}$; Lovelock corrections to the graviton operator OPEN |
| res 6 | FE-58 to FE-60 | implied relative root error: $5.4\times10^{-11}$ ($\nu_1$); three generations $1.2\times10^{-11}$ | mixing with the Kaluza-Klein modes, largest for the top quark: $2.0\times10^{-6}$ |
| res 7 | FE-62 | the stored levels against the closed form: $8.5\times10^{-13}$ | the shift by the Standard-Model mean fields: $1.5\times10^{-6}$ (added in the coupled solution) |
| res 8 | FE-63 to FE-68 | a state re-solved, one more Kohn-Sham map, the energy identity: $7.4\times10^{-14}\,H$ | the self-interaction at the assumed bound: $2.7\times10^{-9}\,m_\Psi$; correlation beyond the local exchange OPEN |
| res 9 | FE-67 with FE-47 | $\Delta K$ recomputed from the Kohn-Sham integrals: $1.4\times10^{-12}$ | the block-shape source $p_0 - p_5$: NOT small, up to 4.00 times $\bar p$ (OPEN) |
| res 10 | FE-70, FE-71, FE-135 | the overlaps from the closed-form orbitals: $3.8\times10^{-12}$ | screening by the interacting gas: $3.5\times10^{-4}$ at $\lambda_{\mathrm{test}}$, $7.2\times10^{-10}$ at the bound |
| res 11 | FE-72 to FE-86 | every mean field and block response recomputed: $2.0\times10^{-11}$ | the loop gain $1.1\times10^{-33}$; second order in the mean fields $2.3\times10^{-12}$ |
| res 12 | FE-79 | the first-order coefficient afresh: $3.3\times10^{-12}$ (shooting agrees) | the physical shift at the freeze-out: $1.9\times10^{-17}$ |
| res 13 | FE-55, FE-102 and the $Z$ widths | widths and $m_{\mathrm{Z}}$ recomputed: $2.7\times10^{-12}$ | electroweak loop corrections $0.41$ %; bottom-quark mass $-0.13$ %; order $\alpha_3^2$ $0.13$ % |
| res 14 | FE-89 to FE-99 | the Poisson form against the Weyl potential: $1.5\times10^{-6}$; matter-era limit $4.4\times10^{-5}$ | order $\epsilon^2$ against order $\epsilon$: $2.4\times10^{-5}$ |
| res 15 | FE-53, FE-54 | the profiles in the operator: $1.2\times10^{-12}$; Yukawa strengths $5.2\times10^{-9}$ | the Kaluza-Klein correction to Newton's law at 50 micrometres: zero in double precision |
| res 16 | FE-87, FE-88 | the first omitted order against the kept one: $2.4\times10^{-5}$ | order 2 at a neutron star: 0.030 (outside the cosmological solution) |
| res 17 | FE-103 to FE-108 | unitarity, vacuum formula, accelerator and solar probabilities: $7.1\times10^{-12}$ | non-adiabatic effects on the solar $\mathcal{P}_{ee}$: $1.3\times10^{-3}$ |
| res 18 | FE-109 | the onset condition at the stored temperatures: $8.7\times10^{-12}$ | the CP-asymmetric potential: $1.1\times10^{-2}$ of the thermal one (ESTIMATE) |
| res 19 | FE-110 to FE-115 | the instantaneous limit recomputed: $2.7\times10^{-12}$; published values within $4.6\times10^{-4}$ | electron mass and momentum dependence: $4.4\times10^{-3}$ in $N_{\mathrm{eff}}$ |
| res 20 | FE-116 to FE-119 | moments, analytic growth, homogeneous matrix: $3.3\times10^{-13}$ | the vacuum term: $9.0\times10^{-6}$ of the self-interaction |
| res 21 | FE-120 | densities, energy densities, velocities, $\Omega_\nu h_{100}^2$: $2.9\times10^{-12}$ | the non-instantaneous heating: $1.1\times10^{-2}$ in $\Omega_\nu h_{100}^2$ (included in the CMB) |
| res 22 | FE-121 to FE-123 | $g_\rho$, $g_s$ by an independent quadrature: $5.0\times10^{-9}$ | the order-$\alpha$ plasma pressure: NOT small, $-5.4$ % at the freeze-out |
| res 23 | FE-124 to FE-128 | the relic re-solved, $\Omega_{\mathrm{DM}}h_{100}^2 = 0.060000000186$ per species; late-time identity $6.1\times10^{-9}$ | the order-$\alpha$ pressure: about $+2.7$ % in $\Omega_{\mathrm{DM}}h_{100}^2$ (ESTIMATE) |
| res 24 | FE-129, FE-130 | $\Delta N_{\mathrm{eff}}/G_{\mathrm{V}}^2$ re-integrated: $3.9\times10^{-5}$ | inverse processes: 0.012 of the Hubble rate at $T_{\mathrm{max}}$ |
| res 25 | FE-131 to FE-134 | the $\nu_R$ equation re-solved: $2.5\times10^{-12}$ | the elastic rate (ESTIMATE): $9.5\times10^{-6}$ in $\Delta N_{\mathrm{eff}}$ |
| res 26 | FE-135, FE-136 | $\Delta N_{\mathrm{eff}}/G_\lambda^2$ re-integrated: $1.1\times10^{-5}$ | inverse annihilation at the bound: 0.027 of the Hubble rate |

The 26 links in concert (the quantity, the field equations that share it, the difference):

| | quantity | shared by | difference |
|:----|:-----------------------------|:------------------------------|:---------------|
| res 27 | block averages of the Kohn-Sham states | FE-63 to FE-68, FE-45 to FE-47 | $3.4\times10^{-12}$ |
| res 28 | hidden pressure of the dark matter, $p_0/\rho = -\mathrm{d}\ln\varepsilon_{\mathrm{DM}}/\mathrm{d}\ln f$ | FE-67, FE-62, FE-81 | $6.1\times10^{-12}$ |
| res 29 | $m_{\mathrm{Z}}$ | FE-55, the $Z$ widths | $2.0\times10^{-12}$ |
| res 30 | the weak angle and the total $Z$ width | FE-55, FE-102, the $Z$ widths | NOT zero: $8.3\times10^{-3}$ |
| res 31 | the twelve fermion masses | FE-59, FE-60, FE-121 | $3.1\times10^{-12}$ |
| res 32 | $m_1$, $m_2$, $m_3$ and the splittings | FE-60, FE-104, FE-120, FE-96, FE-109 | $5.7\times10^{-12}$ |
| res 33 | the PMNS matrix | FE-60, FE-104, FE-120 | $8.2\times10^{-13}$ |
| res 34 | $\Omega_\nu h_{100}^2$ | FE-120, FE-96 | $1.9\times10^{-5}$ |
| res 35 | $N_{\mathrm{eff}} = 3.0432 + \Delta N_{\mathrm{eff}}$ | FE-115, FE-130, FE-97 | $5.4\times10^{-16}$ |
| res 36 | $\Omega_{\mathrm{DM}}h_{100}^2$ | FE-126, FE-90 | $3.1\times10^{-9}$ |
| res 37 | the Hubble rate at the freeze-out | FE-122, FE-124, FE-49, FE-129 | NOT zero: $1.7\times10^{-4}$ |
| res 38 | $g_\rho$ today | FE-122, FE-115, FE-97 | NOT zero: $5.9\times10^{-3}$ |
| res 39 | the plasma energy density at the freeze-out | FE-121, FE-81 | NOT zero: $1.3\times10^{-3}$ |
| res 40 | the portal responses of the dark-matter level | FE-70, FE-63, FE-72 | $3.0\times10^{-12}$ |
| res 41 | $\mathcal{O}_{\mathrm{DM}}$ | FE-71, FE-124, FE-72, FE-79 | $5.7\times10^{-6}$ (4 digits coded) |
| res 42 | $c_{\mathrm{I12}}/\Lambda_\star^3$ | FE-127, FE-72 | $1.6\times10^{-12}$ |
| res 43 | $M_{\mathrm{DM}}$ | FE-62, FE-63, FE-124, FE-72 | $8.1\times10^{-13}$ |
| res 44 | $G_{\mathrm{A}}$, $G_{\mathrm{V}}$ | FE-126, FE-129, FE-72 | $6.7\times10^{-13}$ |
| res 45 | $\tilde m_{\mathrm{W}}^2$ without the kinetic function | FE-52, FE-79 | $2.3\times10^{-6}$ (finite elements) |
| res 46 | $c_\rho$, $c_3$, $c_p$ | FE-46, FE-47, FE-80 | $2.0\times10^{-13}$ |
| res 47 | the radion frequency | FE-44, FE-39, FE-53, FE-87 | NOT zero: $7.9\times10^{-5}$ (finite oscillation) |
| res 48 | $f_*$ | FE-43, FE-52, FE-59, FE-62, FE-63 | $2.2\times10^{-12}$ |
| res 49 | the heating factor $F_{\mathrm{h}}$ | FE-115, FE-133 | $5.8\times10^{-7}$ (4 digits coded) |
| res 50 | $\Phi_{\mathrm{rms}}$, $\Delta\ln f$, $m_{\mathrm{KK}}$, $\sigma_8$ | FE-87, FE-53, FE-98, FE-80 | $4.7\times10^{-12}$ |
| res 51 | the freeze-out temperature | FE-126, FE-86, FE-136 | $2.1\times10^{-12}$ |
| res 52 | the block sensitivities of the masses | FE-85, FE-83, FE-84 | $4.5\times10^{-11}$ |

Every residual lies within its tolerance and every check passes. The radion frequency (res 47) differs because the nonlinear
value is measured from the zero crossings of a finite oscillation (relative amplitude $3\times10^{-3}$); the other links that
are not zero are findings, stated next.

## The findings that are not small

**1. The weak angle has two values.** The $x_0$ problem of $W^\pm$ and $Z$ fixes the angle of the couplings with the measured
electroweak parameter,

$$
\rho_{\mathrm{EW}} = \frac{\tilde m_{\mathrm{W}}^2}{\tilde m_{\mathrm{Z}}^2\cos^2\theta_{\mathrm{W}}} =
 \rho_{\mathrm{EW},0},\qquad
\cos^2\theta_{\mathrm{W}} = \frac{m_{\mathrm{W}}^2/m_{\mathrm{Z}}^2}{\rho_{\mathrm{EW},0}},\qquad
m_{\mathrm{KK}} = m_{\mathrm{W}}\,\frac{\tilde m_1}{\tilde m_{\mathrm{W}}},\qquad
m_{\mathrm{Z}} = m_{\mathrm{W}}\,\frac{\tilde m_{\mathrm{Z}}}{\tilde m_{\mathrm{W}}} \tag{FE-55}
$$

<!-- symbols: rhoEW, mtildeW, mtildeZ, thetaW, rhoEW0, mW, mZ, mKK, mtilde -->
<!-- begin generated symbol list -->
**Symbols in (FE-55).**

- $\rho_{\mathrm{EW}}$: The electroweak parameter, $\rho_{\mathrm{EW}} = \tilde m_{\mathrm{W}}^2/(\tilde m_{\mathrm{Z}}^2\cos^2\theta_{\mathrm{W}})$. Unit: dimensionless. Status: DERIVED.
- $\tilde m_{\mathrm{W}}$: The dimensionless $x_0$ eigenvalue of the lowest $W^\pm$ mode ($\beta = \beta_{\mathrm{W}}$). Unit: dimensionless. Value: $\tilde m_{\mathrm{W}}^2 = 1.32149\times10^{-5}$. Status: DERIVED.
- $\tilde m_{\mathrm{Z}}$: The dimensionless $x_0$ eigenvalue of the lowest $Z$ mode ($\beta = \beta_{\mathrm{Z}}$). Unit: dimensionless. Value: $\tilde m_{\mathrm{Z}}^2 = 1.70150\times10^{-5}$. Status: DERIVED.
- $\theta_{\mathrm{W}}$: The weak mixing angle of the couplings, $\cos\theta_{\mathrm{W}} = \hat g_2/\hat g_Z$, $\sin\theta_{\mathrm{W}} = \hat g_1/\hat g_Z$; fixed by the measured $W$ and $Z$ masses with $\rho_{\mathrm{EW},0}$. Unit: dimensionless. Value: $\cos^2\theta_{\mathrm{W}} = 0.776368$. Status: DERIVED.
- $\rho_{\mathrm{EW},0}$: The measured value of the electroweak parameter (PDG fit). Unit: dimensionless. Value: $1.00038$. Status: STANDARD.
- $m_{\mathrm{W}}$: The mass of $W^+$ and $W^-$. Unit: GeV. Value: 80.3625 GeV (measured, input). Status: STANDARD.
- $m_{\mathrm{Z}}$: The mass of the $Z$. Unit: GeV. Value: 91.1879 GeV (reproduced). Status: STANDARD.
- $m^{\mathrm{KK}}_n,\ m_{\mathrm{KK}}$: The mass of the $n$-th Kaluza-Klein graviton (and gauge) level, $m^{\mathrm{KK}}_n = \tilde m_n/(fL)$; $m_{\mathrm{KK}} = m^{\mathrm{KK}}_1$ is the Kaluza-Klein scale. Unit: GeV. Value: $m_{\mathrm{KK}} = 121.32$ TeV. Status: DERIVED.
- $\tilde m,\ \tilde m_n$: The dimensionless $x_0$ eigenvalue of a boson mode, $\tilde m = m\,fL$; $\tilde m_n$ the $n$-th even Kaluza-Klein level of the tower with $\beta = 0$ ($\tilde m_1$ the first). Unit: dimensionless. Value: $\tilde m_1^2 = 30.1196$, $\tilde m_2^2 = 59.7284$, $\tilde m_3^2 = 109.0764$ ($HL = 3$), i.e. $\tilde m_1 = 5.48813$, $\tilde m_2 = 7.72842$, $\tilde m_3 = 10.44397$. Status: DERIVED.

<!-- end generated symbol list -->

so that $\sin^2\theta_{\mathrm{W}} = 1 - 0.776368 = 0.223632$ (on shell); this angle also enters the tip condition of the $Z$
(FE-51), the $Z$ part of the electroweak condensates (FE-78) and the tree-level couplings

$$
\frac{G_{\mathrm{F}}}{\sqrt2} = \frac{g_2^2}{8m_{\mathrm{W}}^2},\qquad
\tilde g^f_L = T_3^f - Q_{\mathrm{em}}^f\sin^2\theta_{\mathrm{W}},\qquad \tilde g^f_R =
 -Q_{\mathrm{em}}^f\sin^2\theta_{\mathrm{W}},\qquad
\tilde g^f_V = \tilde g^f_L + \tilde g^f_R = T_3^f - 2Q_{\mathrm{em}}^f\sin^2\theta_{\mathrm{W}} \tag{FE-102}
$$

<!-- symbols: GF, g2, mW, gtilde, if, iL, T3, Qem, thetaW, iR, iV -->
<!-- begin generated symbol list -->
**Symbols in (FE-102).**

- $G_{\mathrm{F}}$: The Fermi constant. Unit: $\mathrm{GeV}^{-2}$. Value: $1.1663788\times10^{-5}$ GeV$^{-2}$ (measured). Status: STANDARD.
- $g_2$: The four-dimensional SU(2) coupling ($g_2^2 = 4\pi\alpha_2$). Unit: dimensionless. Value: $g_2^2 = 0.3781$ at $2M_{\mathrm{DM}}$. Status: DERIVED.
- $m_{\mathrm{W}}$: The mass of $W^+$ and $W^-$. Unit: GeV. Value: 80.3625 GeV (measured, input). Status: STANDARD.
- $\tilde g^f_L,\ \tilde g^f_R,\ \tilde g^f_V$: The neutral-current couplings of the fermion $f$ to the $Z$ (left-handed, right-handed and vector), $\tilde g^f_L = T_3^f - Q^f_{\mathrm{em}}\sin^2\theta_{\mathrm{W}}$. Unit: dimensionless. Status: STANDARD.
- $f$: The label of a fermion species: a Standard-Model multiplet of one generation (its $N_{\mathrm{c}}$ Weyl components share one zero-mode profile; the zero mode of each chirality) or a fermion of a medium (electron, proton, neutron); a sum over $f$ runs over these species. Status: STANDARD.
- $L$: The chirality label L: the left-handed (doublet) zero mode, or the left-handed projection $P_L = (1 + \Gamma_4)/2$. Status: STANDARD.
- $T_3$: The third component of the weak isospin ($+\frac12$ for the upper and $-\frac12$ for the lower member of a doublet, 0 for a singlet); $T_3^f$ that of the fermion $f$. Unit: dimensionless. Status: STANDARD.
- $Q_{\mathrm{em}}$: The electric charge in units of the elementary charge, $Q_{\mathrm{em}} = T_3 + Y$; $Q^f_{\mathrm{em}}$ that of the fermion $f$. Unit: dimensionless. Status: STANDARD.
- $\theta_{\mathrm{W}}$: The weak mixing angle of the couplings, $\cos\theta_{\mathrm{W}} = \hat g_2/\hat g_Z$, $\sin\theta_{\mathrm{W}} = \hat g_1/\hat g_Z$; fixed by the measured $W$ and $Z$ masses with $\rho_{\mathrm{EW},0}$. Unit: dimensionless. Value: $\cos^2\theta_{\mathrm{W}} = 0.776368$. Status: DERIVED.
- $R$: The chirality label R: the right-handed (singlet) zero mode or field, or the projection $P_R = (1 - \Gamma_4)/2$. Status: STANDARD.
- $V$: The label V of the vector coupling of a fermion to the $Z$, $\tilde g^f_V = \tilde g^f_L + \tilde g^f_R$. Status: STANDARD.

<!-- end generated symbol list -->

while the $Z$ widths, the running couplings (FE-77) and the couplings of the I12 benchmark use the measured
$\overline{\mathrm{MS}}$ value $\sin^2\theta_{\overline{\mathrm{MS}}} = 0.23122$ in the tree-level partial widths of the $Z$ into
massless fermions (with the factor $1 + \alpha_3/\pi$ for the hadronic widths),

$$
\Gamma_{\mathrm{Z}}^f = \frac{N_{\mathrm{col}}\,G_{\mathrm{F}}\,m_{\mathrm{Z}}^3}{6\sqrt2\,\pi}
 \Big[\big(T_3^f - 2Q_{\mathrm{em}}^f\sin^2\theta_{\overline{\mathrm{MS}}}\big)^2 + \big(T_3^f\big)^2\Big]
$$

<!-- symbols: sol_GammaZ, if, sol_Ncol, GF, mZ, pi, T3, Qem, thetaMS -->
<!-- begin generated symbol list -->
**Symbols in this equation.**

- $\Gamma_{\mathrm{Z}}^{f}$: The decay width of the $Z$ boson; with the fermion label $f$ it is the partial width into the pair of $f$ and its antiparticle (tree level, massless fermion). Unit: GeV (quoted in MeV). Value: total $2485.2$ MeV with $1 + \alpha_3/\pi$ on the quarks (measured $2495.5$ MeV). Status: DERIVED.
- $f$: The label of a fermion species: a Standard-Model multiplet of one generation (its $N_{\mathrm{c}}$ Weyl components share one zero-mode profile; the zero mode of each chirality) or a fermion of a medium (electron, proton, neutron); a sum over $f$ runs over these species. Status: STANDARD.
- $N_{\mathrm{col}}$: The number of colour components of a fermion multiplet: 3 for a quark, 1 for a lepton. Unit: dimensionless. Status: STANDARD.
- $G_{\mathrm{F}}$: The Fermi constant. Unit: $\mathrm{GeV}^{-2}$. Value: $1.1663788\times10^{-5}$ GeV$^{-2}$ (measured). Status: STANDARD.
- $m_{\mathrm{Z}}$: The mass of the $Z$. Unit: GeV. Value: 91.1879 GeV (reproduced). Status: STANDARD.
- $\pi$: The number pi, the ratio of the circumference of a circle to its diameter. Unit: dimensionless. Value: 3.141592654. Status: STANDARD.
- $T_3$: The third component of the weak isospin ($+\frac12$ for the upper and $-\frac12$ for the lower member of a doublet, 0 for a singlet); $T_3^f$ that of the fermion $f$. Unit: dimensionless. Status: STANDARD.
- $Q_{\mathrm{em}}$: The electric charge in units of the elementary charge, $Q_{\mathrm{em}} = T_3 + Y$; $Q^f_{\mathrm{em}}$ that of the fermion $f$. Unit: dimensionless. Status: STANDARD.
- $\theta_{\overline{\mathrm{MS}}}$: The weak mixing angle in the $\overline{\mathrm{MS}}$ scheme at $m_{\mathrm{Z}}$. Unit: dimensionless. Value: $\sin^2\theta_{\overline{\mathrm{MS}}} = 0.23122$. Status: STANDARD.

<!-- end generated symbol list -->

With the on-shell angle (and the $m_{\mathrm{Z}}$ of the $x_0$ problem) the total width would be 2505.73 MeV instead of 2485.23
MeV: $0.83$ % (0.82 % at tree level without the QCD factor, check `Z_width_scheme`). The difference is a scheme ambiguity of a
tree-level angle, of the size of the electroweak loop corrections that UM-2 does not compute (the measured total width is
0.41 % above the computed one); the status of the widths (a tree-level comparison) is unchanged.

**2. The Hubble rate of the thermal history leaves out the fold bands.** The Boltzmann equation of the dark matter uses the
Hubble rate of the thermal history,

$$
g_\rho = \frac{30}{\pi^2T^4}\sum_s\rho_s,\qquad g_s = \frac{45}{2\pi^2T^3}\sum_s s_s,\qquad
\mathcal{H} = \Big(\frac{8\pi^3g_\rho}{90}\Big)^{1/2}\frac{T^2}{M_{\mathrm{Pl}}} \tag{FE-122}
$$

<!-- symbols: grho, pi, Temp, is, rho, sentropy, Hubble, MPl -->
<!-- begin generated symbol list -->
**Symbols in (FE-122).**

- $g_\rho,\ g_s$: The effective numbers of relativistic degrees of freedom of the energy density and of the entropy density of the plasma. Unit: dimensionless. Value: 105.75 when every species of UM-2 in equilibrium is relativistic (no Higgs particle), 10.75 near 1 MeV, $g_s = 43/11$ today. Status: STANDARD.
- $\pi$: The number pi, the ratio of the circumference of a circle to its diameter. Unit: dimensionless. Value: 3.141592654. Status: STANDARD.
- $T$: The temperature of the plasma (of the photons and of every species in equilibrium with them); in the Mermin occupations the temperature of the Kohn-Sham state. Unit: GeV. Status: STANDARD.
- $s$: The label of a particle species of the plasma or of matter (photon, gluons, $W^\pm$, $Z$, quarks, leptons, nucleons, dark matter); a sum over $s$ runs over the species present. Status: STANDARD.
- $\rho$: An energy density: in eight dimensions $\rho = -\mathcal{T}^{x_4}{}_{x_4}$ (of the total source, or of the species named by a subscript; $\rho_s$ of the species $s$, $\rho_i$ of the neutrino mass state $i$); in the cosmological perturbation equations $\Delta\rho$ is the density perturbation summed over the species. Unit: $\mathrm{GeV}^{8}$ (eight dimensions), $\mathrm{GeV}^{4}$ (four dimensions). Status: STANDARD.
- $s,\ s_s$: The entropy density of the plasma, $s = 2\pi^2g_sT^3/45$; $s_s$ that of the species $s$. Unit: $\mathrm{GeV}^{3}$. Status: STANDARD.
- $\mathcal{H}$: The expansion rate of ordinary 3-space, $\mathcal{H} = \dot a_4$ (the Hubble rate of the observer; in the hot Universe $\mathcal{H} = (8\pi^3g_\rho/90)^{1/2}T^2/M_{\mathrm{Pl}}$). Unit: GeV. Status: DERIVED.
- $M_{\mathrm{Pl}}$: The Planck mass, $M_{\mathrm{Pl}} = G_{\mathrm{N}}^{-1/2}$. Unit: GeV. Value: $1.22091\times10^{19}$ GeV. Status: STANDARD.

<!-- end generated symbol list -->

whose $g_\rho$ counts the species of the Standard Model in equilibrium but not the fold bands produced by freeze-in. At the
freeze-out ($T = 1.42$ TeV) the fold bands carry $3.48\times10^{-4}$ of the energy density, so the four-dimensional Friedmann
equation with all species gives a Hubble rate larger by $1.7\times10^{-4}$; since the relic abundance is about proportional to
the Hubble rate at the freeze-out, it moves by about the same relative amount, about a factor 60 below the 1 % precision of the
measured $\Omega_{\mathrm{DM}}h_{100}^2$. The dark matter itself carries $1.1\times10^{-2}$ of the energy density at the start
of the Boltzmann integration ($x = 5$), where its abundance is the equilibrium one, and $7\times10^{-12}$ at the freeze-out.

**3. The thermal history decouples the neutrinos instantaneously.** Below 2 MeV the thermal history uses

$$
w_{\mathrm{QGP}}(T) = \frac12\Big[1 + \tanh\frac{T - T_{\mathrm{c}}}{T_{\mathrm{w}}}\Big],\qquad
\frac{T_\nu}{T} = \Big(\frac{g_{s,e\gamma}(T)}{11/2}\Big)^{1/3},\qquad
\frac{\mathrm{d}\ln T}{\mathrm{d}x_4} = -\frac{\mathcal{H}}{1 + \frac13\,\mathrm{d}\ln g_s/\mathrm{d}\ln
 T} \tag{FE-123}
$$

<!-- symbols: wQGP, Temp, Tcw, Tnu, gseg, diff, x4, Hubble, grho -->
<!-- begin generated symbol list -->
**Symbols in (FE-123).**

- $w_{\mathrm{QGP}}(T)$: The weight of the quark-gluon plasma in the model of the QCD crossover (1 above, 0 below). Unit: dimensionless. Status: ASSUMED.
- $T$: The temperature of the plasma (of the photons and of every species in equilibrium with them); in the Mermin occupations the temperature of the Kohn-Sham state. Unit: GeV. Status: STANDARD.
- $T_{\mathrm{c}},\ T_{\mathrm{w}}$: The temperature and the width of the QCD crossover. Unit: GeV. Value: 155 MeV and 15 MeV. Status: ASSUMED.
- $T_\nu$: The temperature of the relic neutrinos (one common temperature). Unit: GeV. Value: 1.9454 K today. Status: STANDARD.
- $g_{s,e\gamma}$: The entropy degrees of freedom of the electrons, positrons and photons only (after neutrino decoupling). Unit: dimensionless. Value: $11/2$ before and 2 after the annihilation of $e^\pm$. Status: STANDARD.
- $\mathrm{d}$: The differential: $\mathrm{d}X$ is an infinitesimal change of $X$, $\mathrm{d}X/\mathrm{d}Y$ the derivative of $X$ with respect to $Y$, $\mathrm{d}^nX$ the volume element of $n$ variables. Status: STANDARD.
- $x_4$: The time; dots denote $\mathrm{d}/\mathrm{d}x_4$. Unit: length (= time, c = 1). Status: AUTHOR.
- $\mathcal{H}$: The expansion rate of ordinary 3-space, $\mathcal{H} = \dot a_4$ (the Hubble rate of the observer; in the hot Universe $\mathcal{H} = (8\pi^3g_\rho/90)^{1/2}T^2/M_{\mathrm{Pl}}$). Unit: GeV. Status: DERIVED.
- $g_\rho,\ g_s$: The effective numbers of relativistic degrees of freedom of the energy density and of the entropy density of the plasma. Unit: dimensionless. Value: 105.75 when every species of UM-2 in equilibrium is relativistic (no Higgs particle), 10.75 near 1 MeV, $g_s = 43/11$ today. Status: STANDARD.

<!-- end generated symbol list -->

which gives $N_{\mathrm{eff}} = 3$ and $g_\rho = 3.362644$ today, while the CMB computation uses
$N_{\mathrm{eff}} = 3.0432 + 0.0010 = 3.0442$ from the decoupling equations with the precision value,

$$
N_{\mathrm{eff}} = \Big(\frac{11}{4}\Big)^{4/3}\Big[\Big(\frac{T_{\nu_e}}{T_\gamma}\Big)^4 +
 2\Big(\frac{T_{\nu_\mu}}{T_\gamma}\Big)^4\Big],
\qquad \frac{\mathrm{d}T_\nu}{\mathrm{d}x_4} = -\mathcal{H}T_\nu + \frac{C_{\nu_e} +
 2C_{\nu_\mu}}{3\,\mathrm{d}\rho_\nu/\mathrm{d}T_\nu} \tag{FE-115}
$$

<!-- symbols: Neff, Tnua, Tgamma, diff, Tnu, x4, Hubble, Cnua, rhonu -->
<!-- begin generated symbol list -->
**Symbols in (FE-115).**

- $N_{\mathrm{eff}}$: The effective number of neutrino species (the radiation beyond the photons in units of one neutrino species with $T_\nu/T_\gamma = (4/11)^{1/3}$); $\Delta N_{\mathrm{eff}}$ an addition to it. Unit: dimensionless. Value: 3.0432 (neutrinos) + 0.0010 (fold bands). Status: STANDARD.
- $T_{\nu_\alpha},\ T_{\nu_e},\ T_{\nu_\mu}$: The temperature of the neutrinos of the flavour $\alpha$ (of $\nu_e$, of $\nu_\mu$ and $\nu_\tau$) during decoupling. Unit: GeV. Status: STANDARD.
- $T_\gamma$: The temperature of the photons (equal to the plasma temperature $T$; the subscript is written where the neutrinos have their own temperature). Unit: GeV. Value: 2.7255 K today. Status: STANDARD.
- $\mathrm{d}$: The differential: $\mathrm{d}X$ is an infinitesimal change of $X$, $\mathrm{d}X/\mathrm{d}Y$ the derivative of $X$ with respect to $Y$, $\mathrm{d}^nX$ the volume element of $n$ variables. Status: STANDARD.
- $T_\nu$: The temperature of the relic neutrinos (one common temperature). Unit: GeV. Value: 1.9454 K today. Status: STANDARD.
- $x_4$: The time; dots denote $\mathrm{d}/\mathrm{d}x_4$. Unit: length (= time, c = 1). Status: AUTHOR.
- $\mathcal{H}$: The expansion rate of ordinary 3-space, $\mathcal{H} = \dot a_4$ (the Hubble rate of the observer; in the hot Universe $\mathcal{H} = (8\pi^3g_\rho/90)^{1/2}T^2/M_{\mathrm{Pl}}$). Unit: GeV. Status: DERIVED.
- $C_{\nu_\alpha},\ C_{\nu_e},\ C_{\nu_\mu}$: The energy transfer rate per volume into the neutrinos of the flavour $\alpha$ by collisions. Unit: $\mathrm{GeV}^{5}$. Status: STANDARD.
- $\rho_\nu,\ \rho_{\nu_\alpha}$: The energy density of one neutrino flavour (neutrinos and antineutrinos) at the common temperature $T_\nu$, $\frac78\frac{\pi^2}{15}T_\nu^4$ when massless; $\rho_{\nu_\alpha}$ that of the flavour $\alpha$ at its temperature $T_{\nu_\alpha}$. Unit: $\mathrm{GeV}^{4}$. Status: STANDARD.

<!-- end generated symbol list -->

and so $g_\rho = 3.382720$ today: 0.59 %. Below 2 MeV the thermal history enters only the entropy density today ($g_s = 43/11$,
the standard value) and the environment of nucleosynthesis (effects below $10^{-58}$), so the difference has no effect on a
result.

**4. The plasma energy density differs by 0.13 % between the thermal history and the block sources, by design.** The thermal
history sums the ideal gases with the $x_0$ masses,

$$
\rho_s = \frac{d_s}{2\pi^2}\int_0^\infty\frac{k^2E\,\mathrm{d}k}{\mathrm{e}^{E/T} \pm 1},\qquad
p_s = \frac{d_s}{6\pi^2}\int_0^\infty\frac{k^4\,\mathrm{d}k}{E\,(\mathrm{e}^{E/T} \pm 1)},\qquad
s_s = \frac{\rho_s + p_s}{T},\qquad E = \sqrt{k^2 + m_s^2} \tag{FE-121}
$$

<!-- symbols: rho, is, ddeg, pi, infty, kwave, Eenergy, diff, euler, Temp, pressure, sentropy, mmass -->
<!-- begin generated symbol list -->
**Symbols in (FE-121).**

- $\rho$: An energy density: in eight dimensions $\rho = -\mathcal{T}^{x_4}{}_{x_4}$ (of the total source, or of the species named by a subscript; $\rho_s$ of the species $s$, $\rho_i$ of the neutrino mass state $i$); in the cosmological perturbation equations $\Delta\rho$ is the density perturbation summed over the species. Unit: $\mathrm{GeV}^{8}$ (eight dimensions), $\mathrm{GeV}^{4}$ (four dimensions). Status: STANDARD.
- $s$: The label of a particle species of the plasma or of matter (photon, gluons, $W^\pm$, $Z$, quarks, leptons, nucleons, dark matter); a sum over $s$ runs over the species present. Status: STANDARD.
- $d_o,\ d_s$: A degeneracy: $d_o = 4r_3(\lvert\vec n_o\rvert^2)$ the number of states of the momentum shell of the orbital $o$; $d_s$ the number of internal states (spin, colour, particle and antiparticle) of the species $s$. Unit: dimensionless. Status: STANDARD.
- $\pi$: The number pi, the ratio of the circumference of a circle to its diameter. Unit: dimensionless. Value: 3.141592654. Status: STANDARD.
- $\infty$: Infinity: as a limit of an integral or a sum it means that the range has no upper bound. Status: STANDARD.
- $k$: The magnitude of the wave vector (the momentum, $\hbar = 1$) of a mode: in the reduction, the Kohn-Sham and the perturbation equations the comoving wavenumber (physical momentum $\mathrm{e}^{-a_4}k$); in the thermal integrals the momentum of a particle at the time considered (the variable of integration). Unit: GeV (1/length). Status: STANDARD.
- $E$: The energy of a particle: of the neutrino in the flavour equations, $E = (k^2 + m^2)^{1/2}$ of a particle of momentum $k$ in the thermal integrals. Unit: GeV. Status: STANDARD.
- $\mathrm{d}$: The differential: $\mathrm{d}X$ is an infinitesimal change of $X$, $\mathrm{d}X/\mathrm{d}Y$ the derivative of $X$ with respect to $Y$, $\mathrm{d}^nX$ the volume element of $n$ variables. Status: STANDARD.
- $\mathrm{e}$: Euler's number, the base of the natural logarithm; $\mathrm{e}^{X}$ is the exponential of $X$. Unit: dimensionless. Value: 2.718281828. Status: STANDARD.
- $T$: The temperature of the plasma (of the photons and of every species in equilibrium with them); in the Mermin occupations the temperature of the Kohn-Sham state. Unit: GeV. Status: STANDARD.
- $p$: A pressure: $p_M = \mathcal{T}^M{}_M$ (no sum) for the direction $M \ne x_4$, $p_s$ the pressure of the species $s$; $\Delta p$ the pressure perturbation in the cosmological perturbation equations; in the Feynman-Hellmann relation the pressure of a gauge plasma. Unit: $\mathrm{GeV}^{8}$ (eight dimensions), $\mathrm{GeV}^{4}$ (four dimensions). Status: STANDARD.
- $s,\ s_s$: The entropy density of the plasma, $s = 2\pi^2g_sT^3/45$; $s_s$ that of the species $s$. Unit: $\mathrm{GeV}^{3}$. Status: STANDARD.
- $m,\ m_s,\ m_i$: A four-dimensional mass: $m$ the mass of a mode (the eigenvalue of an $x_0$ problem) or of a fermion; $m_s$ the mass of the species $s$; $m_i$ the mass of the neutrino mass state $i$. Unit: GeV. Status: DERIVED.

<!-- end generated symbol list -->

($1.414292\times10^{14}$ GeV$^4$ with the equilibrium dark matter at the freeze-out), while the sources of the block response in
the coupled solution add the trace anomaly of the interacting plasma, the QCD interaction measure

$$
\begin{aligned}
&\frac{\Theta_{\mathrm{QCD}}}{T^4} = 4\exp\Big[-\frac{\ln^2(T/0.2\,\text{GeV})}{0.5}\Big]\ \ (T <
 1\,\text{GeV}),\qquad
 \frac{\Theta_{\mathrm{QCD}}}{T^4} = \frac{b_3}{3}\Big(1 +
 \frac{5N_{\mathrm{f}}}{12}\Big)\alpha_3^2\ \ (T > 1\,\text{GeV}),\\
&p_{\mathrm{QCD}} = \frac{8\pi^2}{45}T^4\Big[1 + \frac{21N_{\mathrm{f}}}{32}
 - \frac{15}{4}\Big(1 + \frac{5N_{\mathrm{f}}}{12}\Big)\frac{\alpha_3}{\pi}\Big],\qquad
 \frac{\mathrm{d}\alpha_3}{\mathrm{d}\ln T} = -\frac{b_3}{2\pi}\,\alpha_3^2,\qquad
 \Theta_{\mathrm{QCD}} = T^5\,\frac{\mathrm{d}}{\mathrm{d}T}\Big(\frac{p_{\mathrm{QCD}}}{T^4}\Big)
\end{aligned} \tag{FE-75}
$$

<!-- symbols: Theta, Temp, bcoef, Nf, alpha3, pQCD, pi, diff -->
<!-- begin generated symbol list -->
**Symbols in (FE-75).**

- $\Theta_{\mathrm{QCD}},\ \Theta_{\mathrm{G}},\ \Theta_V$: The trace $\rho - 3p$ of the energy-momentum tensor (interaction measure) of a plasma component: $\Theta_{\mathrm{QCD}}$ of the quark-gluon plasma or hadron gas, $\Theta_{\mathrm{G}}$ of the gauge plasma of the group G, $\Theta_V$ of the thermal gas of the massive vector $V$ ($\Theta_{\mathrm{W}}$ of $W^\pm$, $\Theta_{\mathrm{Z}}$ of $Z$). Unit: $\mathrm{GeV}^{4}$. Status: STANDARD.
- $T$: The temperature of the plasma (of the photons and of every species in equilibrium with them); in the Mermin occupations the temperature of the Kohn-Sham state. Unit: GeV. Status: STANDARD.
- $b_3,\ b_2,\ b_1,\ b_{\mathrm{G}}$: The one-loop coefficients of the running couplings, $\mathrm{d}\alpha/\mathrm{d}\ln\mu_{\mathrm{ren}} = -b\,\alpha^2/(2\pi)$: $b_3 = 11 - \frac23N_{\mathrm{f}}$ (SU(3)), $b_2 = \frac{10}{3}$ (SU(2) without a Higgs particle), $b_1 = -\frac{20}{3}$ (U(1)$_Y$), $b_{\mathrm{G}}$ that of the group G (not related to the metric function $b_4$). Unit: dimensionless. Status: STANDARD.
- $N_{\mathrm{f}}$: The number of active quark flavours (quarks lighter than the scale). Unit: dimensionless. Status: STANDARD.
- $\alpha_3$: The strong fine-structure constant, $\alpha_3 = g_3^2/(4\pi)$, at the scale given in brackets. Unit: dimensionless. Value: $\alpha_3(m_{\mathrm{Z}}) = 0.1180$; $\alpha_3(m_{\mathrm{KK}}) = 0.0606$. Status: STANDARD.
- $p_{\mathrm{QCD}}$: The pressure of the quark-gluon plasma (leading orders). Unit: $\mathrm{GeV}^{4}$. Status: ESTIMATE.
- $\pi$: The number pi, the ratio of the circumference of a circle to its diameter. Unit: dimensionless. Value: 3.141592654. Status: STANDARD.
- $\mathrm{d}$: The differential: $\mathrm{d}X$ is an infinitesimal change of $X$, $\mathrm{d}X/\mathrm{d}Y$ the derivative of $X$ with respect to $Y$, $\mathrm{d}^nX$ the volume element of $n$ variables. Status: STANDARD.

<!-- end generated symbol list -->

and the electroweak trace ($1.416139\times10^{14}$ GeV$^4$). The trace anomaly enters only $\rho - 3p_3$, which is what the block
responds to.

**5. The order-$\alpha$ pressure of the plasma is not in the thermal history.** The interaction part of the pressure of a gauge
plasma,

$$
\begin{aligned}
&\big\langle F^V_{\mu\nu}F^{V}{}^{\mu\nu}\big\rangle(T) = -2\,\Theta_V\ \ \text{(for $V = W^\pm, Z$)},\qquad
 \big\langle F_{\mathrm{geo}}^2\big\rangle = -4\,\frac{\partial p}{\partial\big(1/g_{\mathrm{G}}^2\big)}
 = 4g_{\mathrm{G}}^2\,p_{\alpha,\mathrm{G}},\\
&p_{\alpha,\mathrm{G}} = -\frac{g_{\mathrm{G}}^2T^4}{144}\,d_{\mathrm{adj}}\Big[C_{\mathrm{adj}} +
 \frac52\,T_{\mathrm{F}}N_{\mathrm{f}}\Big]
\end{aligned} \tag{FE-76}
$$

<!-- symbols: FV, imu, inu, Temp, Theta, Fgeo, partial, pressure, gG, palpha, dadj, Cadj, TF, Nf -->
<!-- begin generated symbol list -->
**Symbols in (FE-76).**

- $F^V_{\mu\nu}$: The field strength of the canonically normalised massive vector $V = W^\pm$ or $Z$, $F^V_{\mu\nu} = \partial_\mu V_\nu - \partial_\nu V_\mu$. Unit: $\mathrm{GeV}^{2}$. Status: STANDARD.
- $\mu$: A four-dimensional coordinate index running over the observable coordinates $x_1, x_2, x_3, x_4$ (signature $+,+,+,-$); on the tip it runs over the tip directions; a repeated index is summed. Status: STANDARD.
- $\nu$: A four-dimensional coordinate index running over $x_1, \dots, x_4$ (as $\mu$). Status: STANDARD.
- $T$: The temperature of the plasma (of the photons and of every species in equilibrium with them); in the Mermin occupations the temperature of the Kohn-Sham state. Unit: GeV. Status: STANDARD.
- $\Theta_{\mathrm{QCD}},\ \Theta_{\mathrm{G}},\ \Theta_V$: The trace $\rho - 3p$ of the energy-momentum tensor (interaction measure) of a plasma component: $\Theta_{\mathrm{QCD}}$ of the quark-gluon plasma or hadron gas, $\Theta_{\mathrm{G}}$ of the gauge plasma of the group G, $\Theta_V$ of the thermal gas of the massive vector $V$ ($\Theta_{\mathrm{W}}$ of $W^\pm$, $\Theta_{\mathrm{Z}}$ of $Z$). Unit: $\mathrm{GeV}^{4}$. Status: STANDARD.
- $F_{\mathrm{geo}}$: The field strength of the gauge group G in geometric normalisation; $\langle F_{\mathrm{geo}}^2\rangle$ is its condensate ($G^A_{\mu\nu}G^{A\mu\nu}$, $W^I_{\mu\nu}W^{I\mu\nu}$ or $B_{\mu\nu}B^{\mu\nu}$). Unit: $\mathrm{GeV}^{2}$. Status: STANDARD.
- $\partial$: A partial derivative: $\partial_M$ is the derivative with respect to the coordinate $X^M$, $\partial_y$ with respect to $y$, $\partial_{x_4}$ with respect to the time $x_4$, $\partial X/\partial Y$ the derivative of $X$ with respect to $Y$ at fixed other variables. Status: STANDARD.
- $p$: A pressure: $p_M = \mathcal{T}^M{}_M$ (no sum) for the direction $M \ne x_4$, $p_s$ the pressure of the species $s$; $\Delta p$ the pressure perturbation in the cosmological perturbation equations; in the Feynman-Hellmann relation the pressure of a gauge plasma. Unit: $\mathrm{GeV}^{8}$ (eight dimensions), $\mathrm{GeV}^{4}$ (four dimensions). Status: STANDARD.
- $g_{\mathrm{G}}$: The four-dimensional coupling of the gauge group G (one of $g_3$, $g_2$, $g_1$). Unit: dimensionless. Status: STANDARD.
- $p_{\alpha,\mathrm{G}},\ p_{\alpha,2},\ p_{\alpha,1}$: The order-$\alpha$ (interaction) part of the pressure of the gauge plasma of the group G; $p_{\alpha,2}$ of SU(2), $p_{\alpha,1}$ of U(1)$_Y$. Unit: $\mathrm{GeV}^{4}$. Status: STANDARD.
- $d_{\mathrm{adj}}$: The dimension of the adjoint representation of the gauge group (8, 3, 1). Unit: dimensionless. Status: STANDARD.
- $C_{\mathrm{adj}}$: The quadratic Casimir of the adjoint representation (3, 2, 0). Unit: dimensionless. Status: STANDARD.
- $T_{\mathrm{F}}$: The Dynkin index of the fermion representation ($\frac12$ per Dirac fundamental; for U(1)$_Y$ the sum of the squared hypercharges). Unit: dimensionless. Status: STANDARD.
- $N_{\mathrm{f}}$: The number of active quark flavours (quarks lighter than the scale). Unit: dimensionless. Status: STANDARD.

<!-- end generated symbol list -->

is $-5.4$ % of the ideal-gas pressure at the freeze-out (QCD $-4.7$ %, SU(2) $-0.7$ %, U(1)$_Y$ $-0.10$ %). The coupled solution
uses it for the condensates, but the ideal-gas thermal history, and so the Hubble rate and the entropy density of the
Boltzmann equation, leave it out: with it $\Omega_{\mathrm{DM}}h_{100}^2$ would rise by about 2.7 % at fixed strength, and the
strength $G_{\mathrm{A}}$ that gives the measured relic by about 1.4 % (ESTIMATE). The physics accuracy of
$G_{\mathrm{A}} = 1.278\times10^{-9}$ GeV$^{-2}$ is therefore about 1 %, not the $10^{-6}$ of its root finding (a precision
statement made in version 4; the value is unchanged).

**6. The block-shape source, quantified.** The order-0 metric has one block scale, so the block responds only to the hidden
pressure averaged over the block,

$$
\begin{aligned}
&\Delta S_{\mathrm{m}} = -\frac12\int\mathrm{d}^8X\,\sqrt{\lvert g\rvert}\;\mathcal{T}_{MN}\,\Delta
 g^{MN},\qquad
 \rho = -\mathcal{T}^{x_4}{}_{x_4},\qquad p_M = \mathcal{T}^M{}_M\quad \text{($M \ne x_4$, no sum)},\\
&\mathcal{T}^M{}_N = \mathrm{diag}\big(p_0,\ p_3,\ p_3,\ p_3,\ -\rho,\ p_5,\ p_5,\ p_5\big)\quad
 \text{(a diagonal source)},\qquad \bar p = \frac{p_0 + 3p_5}{4}
\end{aligned} \tag{FE-2}
$$

<!-- symbols: Delta, Sm, diff, Xcoord, metric, EMT, iM, iN, rho, x4, pressure, diag, p0, p3, p5, pbar -->
<!-- begin generated symbol list -->
**Symbols in (FE-2).**

- $\Delta$: The change (difference or small perturbation) of the quantity that follows: $\Delta K$, $\Delta\rho$, $\Delta p_3$ are first-order changes about the static block, $\Delta\varepsilon_o$ a level shift, $\Delta m^2_{21} = m_2^2 - m_1^2$ a difference of squared masses, $\Delta N_{\mathrm{eff}}$ an addition to $N_{\mathrm{eff}}$, $\Delta S_{\mathrm{m}}$ the change of an action under a change $\Delta g^{MN}$ of the metric. Status: STANDARD.
- $S_{\mathrm{m}}$: The matter action: all terms of the action except $S_{\mathrm{EL}}$ (the stabiliser included). Unit: dimensionless. Status: DERIVED.
- $\mathrm{d}$: The differential: $\mathrm{d}X$ is an infinitesimal change of $X$, $\mathrm{d}X/\mathrm{d}Y$ the derivative of $X$ with respect to $Y$, $\mathrm{d}^nX$ the volume element of $n$ variables. Status: STANDARD.
- $X = \{x_0, \dots, x_7\}$: The author's coordinates of the eight-dimensional spacetime, $X = \{x_0, x_1, \dots, x_7\}$ with the hidden direction first; $X^M$ is the coordinate with the index $M$, $\mathrm{d}^8X = \mathrm{d}x_0\,\mathrm{d}x_1\cdots\mathrm{d}x_7$ the coordinate volume element and $X^\mu$ (four-dimensional index $\mu$) the observable coordinates $x_1, \dots, x_4$. Unit: length (each coordinate). Status: AUTHOR.
- $g_{MN}$: The metric tensor of the eight-dimensional spacetime (signature $+,+,+,+,-,-,-,-$ in the order $x_0, \dots, x_7$): $g_{MN}\,\mathrm{d}X^M\mathrm{d}X^N$ is the squared interval; $g^{MN}$ is its inverse, $g^M{}_N = \delta^M_N$, and $\lvert g\rvert$ the absolute value of its determinant, so that $\sqrt{\lvert g\rvert}\,\mathrm{d}^8X$ is the proper volume element. Unit: dimensionless. Status: AUTHOR.
- $\mathcal{T}^M{}_N$: The energy-momentum tensor of all matter (every field except gravity, the stabiliser included), the source of gravity; defined by the change of the matter action under a change of the metric. Unit: $\mathrm{GeV}^{8}$. Status: STANDARD.
- $M$: A coordinate index of eight dimensions (also with a numbered copy $M_1, M_2, \dots$): it runs over $x_0, x_1, \dots, x_7$; a repeated index is summed. Status: STANDARD.
- $N$: A coordinate index of eight dimensions (also $N_1, N_2, \dots$), running over $x_0, \dots, x_7$; a repeated index is summed. Status: STANDARD.
- $\rho$: An energy density: in eight dimensions $\rho = -\mathcal{T}^{x_4}{}_{x_4}$ (of the total source, or of the species named by a subscript; $\rho_s$ of the species $s$, $\rho_i$ of the neutrino mass state $i$); in the cosmological perturbation equations $\Delta\rho$ is the density perturbation summed over the species. Unit: $\mathrm{GeV}^{8}$ (eight dimensions), $\mathrm{GeV}^{4}$ (four dimensions). Status: STANDARD.
- $x_4$: The time; dots denote $\mathrm{d}/\mathrm{d}x_4$. Unit: length (= time, c = 1). Status: AUTHOR.
- $p$: A pressure: $p_M = \mathcal{T}^M{}_M$ (no sum) for the direction $M \ne x_4$, $p_s$ the pressure of the species $s$; $\Delta p$ the pressure perturbation in the cosmological perturbation equations; in the Feynman-Hellmann relation the pressure of a gauge plasma. Unit: $\mathrm{GeV}^{8}$ (eight dimensions), $\mathrm{GeV}^{4}$ (four dimensions). Status: STANDARD.
- $\mathrm{diag}$: A diagonal matrix with the listed entries on its diagonal (in the order of the coordinates $x_0, x_1, \dots, x_7$ when it is a tensor in eight dimensions). Status: STANDARD.
- $p_0$: The pressure along the hidden direction $x_0$, $p_0 = \mathcal{T}^{x_0}{}_{x_0}$. Unit: $\mathrm{GeV}^{8}$. Status: STANDARD.
- $p_3$: The pressure of ordinary 3-space, $p_3 = \mathcal{T}^{x_1}{}_{x_1} = \mathcal{T}^{x_2}{}_{x_2} = \mathcal{T}^{x_3}{}_{x_3}$ for an isotropic source. Unit: $\mathrm{GeV}^{8}$. Status: STANDARD.
- $p_5$: The pressure along the extra times, $p_5 = \mathcal{T}^{x_5}{}_{x_5} = \mathcal{T}^{x_6}{}_{x_6} = \mathcal{T}^{x_7}{}_{x_7}$. Unit: $\mathrm{GeV}^{8}$. Status: STANDARD.
- $\bar p$: The hidden pressure, the pressure averaged over the block, $\bar p = (p_0 + 3p_5)/4$; for a species at fixed temperature $\bar p = \frac14\,\partial p/\partial\ln f$. Unit: $\mathrm{GeV}^{8}$ (or $\mathrm{GeV}^{4}$ for a four-dimensional density). Status: DERIVED.

<!-- end generated symbol list -->

through the adiabatic response

$$
\Delta K = \frac{c_\rho\,\kappa\Delta\rho + c_3\,\kappa\Delta p_3 + c_p\,\kappa\Delta\bar p}{H^2},\qquad
\Delta\ln f = -\frac{\Delta K}{2K_*},\qquad c_3 = -3c_\rho,\qquad
\Delta\dot{\mathcal{H}} = -\frac{\kappa(\Delta\rho + \Delta p_3)}{2\mathcal{G}(K_*)} \tag{FE-47}
$$

<!-- symbols: Delta, Kblock, crho, kappa, rho, c3, p3, cp, pbar, Hconst, fblock, Kstar, Hdot, GK -->
<!-- begin generated symbol list -->
**Symbols in (FE-47).**

- $\Delta$: The change (difference or small perturbation) of the quantity that follows: $\Delta K$, $\Delta\rho$, $\Delta p_3$ are first-order changes about the static block, $\Delta\varepsilon_o$ a level shift, $\Delta m^2_{21} = m_2^2 - m_1^2$ a difference of squared masses, $\Delta N_{\mathrm{eff}}$ an addition to $N_{\mathrm{eff}}$, $\Delta S_{\mathrm{m}}$ the change of an action under a change $\Delta g^{MN}$ of the metric. Status: STANDARD.
- $K$: The block variable, $K = 1/f^2$. Unit: dimensionless. Status: DERIVED.
- $c_\rho$: The coefficient of $\kappa\Delta\rho$ in the adiabatic block response $\Delta K$. Unit: dimensionless. Value: 0.0358521. Status: DERIVED.
- $\kappa$: The eight-dimensional gravitational coupling, $\kappa = 8\pi G_8$. Unit: $\mathrm{GeV}^{-6}$. Value: $\kappa/V_\perp = 8\pi G_{\mathrm{N}}\mathcal{G}(K_*) = 2.328\times10^{-36}$ GeV$^{-2}$. Status: AUTHOR.
- $\rho$: An energy density: in eight dimensions $\rho = -\mathcal{T}^{x_4}{}_{x_4}$ (of the total source, or of the species named by a subscript; $\rho_s$ of the species $s$, $\rho_i$ of the neutrino mass state $i$); in the cosmological perturbation equations $\Delta\rho$ is the density perturbation summed over the species. Unit: $\mathrm{GeV}^{8}$ (eight dimensions), $\mathrm{GeV}^{4}$ (four dimensions). Status: STANDARD.
- $c_3$: The coefficient of $\kappa\Delta p_3$ in the adiabatic block response, $c_3 = -3c_\rho$ (so radiation drops out). Unit: dimensionless. Value: -0.107556. Status: DERIVED.
- $p_3$: The pressure of ordinary 3-space, $p_3 = \mathcal{T}^{x_1}{}_{x_1} = \mathcal{T}^{x_2}{}_{x_2} = \mathcal{T}^{x_3}{}_{x_3}$ for an isotropic source. Unit: $\mathrm{GeV}^{8}$. Status: STANDARD.
- $c_p$: The coefficient of $\kappa\Delta\bar p$ in the adiabatic block response. Unit: dimensionless. Value: -0.140028. Status: DERIVED.
- $\bar p$: The hidden pressure, the pressure averaged over the block, $\bar p = (p_0 + 3p_5)/4$; for a species at fixed temperature $\bar p = \frac14\,\partial p/\partial\ln f$. Unit: $\mathrm{GeV}^{8}$ (or $\mathrm{GeV}^{4}$ for a four-dimensional density). Status: DERIVED.
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the Lovelock couplings, the cosmological constant $\Lambda = -10H^2$ and the mass parameter $m_\Psi = H$. Unit: GeV (1/length). Value: 14.296 TeV (from the fit of $m_{\mathrm{W}}$ and $\rho_{\mathrm{EW},0}$). Status: AUTHOR.
- $f$: The block scale: the common scale factor of the hidden direction and the extra times, $f = \mathrm{e}^{-a_4}b_4^{1/2}$ (the block is $f^2$ times a four-dimensional space of constant curvature $-H^2$). Unit: dimensionless. Status: DERIVED.
- $K_*$: The block variable of the stabilised block, $K_* = 12 + \frac43\sqrt{51}$ (the upper root $K_+$). Unit: dimensionless. Value: 21.5219. Status: DERIVED.
- $\dot{\mathcal{H}}$: The time derivative $\mathrm{d}\mathcal{H}/\mathrm{d}x_4$. Unit: $\mathrm{GeV}^{2}$. Status: DERIVED.
- $\mathcal{G}(K)$: The coefficient of the four-dimensional Einstein-Hilbert term on a static block, $\mathcal{G}(K) = 1 - 24w_{(2)}K + 72w_{(3)}K^2 = (K^2 - 12K + 16)/16$; four-dimensional gravity is attractive for $\mathcal{G} > 0$. Unit: dimensionless. Value: $\mathcal{G}(K_*) = 20/3 + \sqrt{51} = 13.8081$. Status: DERIVED.

<!-- end generated symbol list -->

while the difference $p_0 - p_5$ would drive a change of the shape of the block that the order-0 metric cannot describe (OPEN
since version 3, corrections item 14). For a Kohn-Sham state

$$
\begin{aligned}
&\rho = \sum_o\tfrac12\,d_o\phi_o\,\varepsilon_o\,n_o - e_{\mathrm{int}},\qquad
 p_3 = \sum_o\tfrac12\,d_o\phi_o\,\frac{\mathrm{e}^{-a_4}\lvert\vec k_o\rvert}{3}\,n^{\mathrm{t}}_o +
 e_{\mathrm{int}},
 \qquad p_5 = e_{\mathrm{int}},\\
&p_0 = \sum_o\tfrac12\,d_o\phi_o\Big[(\varepsilon_o - v)\,n_o - M_{\mathrm{eff}}\,n^{\mathrm{sc}}_o
 - \mathrm{e}^{-a_4}\lvert\vec k_o\rvert\,n^{\mathrm{t}}_o\Big] + e_{\mathrm{int}}
\end{aligned} \tag{FE-67}
$$

<!-- symbols: rho, io, ddeg, phiocc, varepsilon, ndens, eint, p3, euler, a4, kvec, nt, p5, p0, vpot, Meff, nsc -->
<!-- begin generated symbol list -->
**Symbols in (FE-67).**

- $\rho$: An energy density: in eight dimensions $\rho = -\mathcal{T}^{x_4}{}_{x_4}$ (of the total source, or of the species named by a subscript; $\rho_s$ of the species $s$, $\rho_i$ of the neutrino mass state $i$); in the cosmological perturbation equations $\Delta\rho$ is the density perturbation summed over the species. Unit: $\mathrm{GeV}^{8}$ (eight dimensions), $\mathrm{GeV}^{4}$ (four dimensions). Status: STANDARD.
- $o$: The label of a Kohn-Sham orbital (a state of dirac16complex in the cell: block, momentum shell, fold parity and level); a sum over $o$ runs over the orbitals. Status: RECORD.
- $d_o,\ d_s$: A degeneracy: $d_o = 4r_3(\lvert\vec n_o\rvert^2)$ the number of states of the momentum shell of the orbital $o$; $d_s$ the number of internal states (spin, colour, particle and antiparticle) of the species $s$. Unit: dimensionless. Status: STANDARD.
- $\phi_o$: The occupation of the Kohn-Sham orbital $o$ (Fermi-Dirac for the Mermin functional, 0 or 1 for the aufbau). Unit: dimensionless. Status: RECORD.
- $\varepsilon,\ \varepsilon_o$: The energy of a fermion mode (an eigenvalue of the block Hamiltonian; at $k = 0$ the four-dimensional mass); $\varepsilon_o$ the Kohn-Sham level of the orbital $o$. Unit: GeV. Status: DERIVED.
- $n,\ n_o,\ n_{\psi i},\ n_f,\ n_i$: A number density: $n(y)$ the particle density of dirac16complex in the Kohn-Sham equations and $n_o$ the contribution of the orbital $o$, $n_{\psi i}(y)$ the density of the Standard-Model fermion $\psi_i$ (per proper 7-volume of eight dimensions); $n_f$ the density of the fermion component $f$ and $n_i$ that of the neutrino mass state $i$ (per 3-volume of four dimensions). Unit: $\mathrm{GeV}^{7}$ (eight dimensions), $\mathrm{GeV}^{3}$ (four dimensions). Status: STANDARD.
- $e_{\mathrm{int}}$: The interaction energy density of the contact term in the Kohn-Sham energy and energy-momentum tensor. Unit: $\mathrm{GeV}^{8}$. Status: RECORD.
- $p_3$: The pressure of ordinary 3-space, $p_3 = \mathcal{T}^{x_1}{}_{x_1} = \mathcal{T}^{x_2}{}_{x_2} = \mathcal{T}^{x_3}{}_{x_3}$ for an isotropic source. Unit: $\mathrm{GeV}^{8}$. Status: STANDARD.
- $\mathrm{e}$: Euler's number, the base of the natural logarithm; $\mathrm{e}^{X}$ is the exponential of $X$. Unit: dimensionless. Value: 2.718281828. Status: STANDARD.
- $a_4$: The author's metric function of the time $x_4$ that scales ordinary 3-space: the scale factor of cosmology is $\mathrm{e}^{a_4}$. Unit: dimensionless. Status: AUTHOR.
- $\vec k,\ \vec k_o$: The wave vector (momentum) in ordinary 3-space; $\vec k_o$ that of the orbital $o$, a point of the lattice $k_{\mathrm{lat}}\vec n_o$. Unit: GeV. Status: STANDARD.
- $n^{\mathrm{t}}_o$: The density of the orbital $o$ along the momentum term ($\chi_o^\dagger\varsigma\sigma_3\chi_o$ times the weight $\mathrm{e}^{-3Hy}/\mathrm{Vol}_7$); it carries the 3-space pressure. Unit: $\mathrm{GeV}^{7}$. Status: RECORD.
- $p_5$: The pressure along the extra times, $p_5 = \mathcal{T}^{x_5}{}_{x_5} = \mathcal{T}^{x_6}{}_{x_6} = \mathcal{T}^{x_7}{}_{x_7}$. Unit: $\mathrm{GeV}^{8}$. Status: STANDARD.
- $p_0$: The pressure along the hidden direction $x_0$, $p_0 = \mathcal{T}^{x_0}{}_{x_0}$. Unit: $\mathrm{GeV}^{8}$. Status: STANDARD.
- $v(y)$: The vector potential of the block Hamiltonian (the mean field along $\gamma^{x_4}$): for dirac16complex the contact term and the mean field of I11; zero for a Standard-Model fermion. Unit: GeV. Status: DERIVED.
- $M_{\mathrm{eff}}(y)$: The effective (scalar) mass field of the Kohn-Sham Hamiltonian: $m_\Psi$ plus the mean fields of the contact term and of I12. Unit: GeV. Status: DERIVED.
- $n^{\mathrm{sc}},\ n^{\mathrm{sc}}_o$: The scalar density of dirac16complex (the Kohn-Sham expectation of $\bar\Psi\Psi$, per proper 7-volume) and $n^{\mathrm{sc}}_o$ the contribution of the orbital $o$. Unit: $\mathrm{GeV}^{7}$. Status: RECORD.

<!-- end generated symbol list -->

and for dark matter at rest without self-interaction ($e_{\mathrm{int}} = 0$, so $p_5 = 0$ and $\bar p = p_0/4$) the neglected
source is 4.00 times the kept one; for the self-interacting test states it is 0.90 times. Its absolute size is suppressed like
that of $\bar p$ ($\kappa p/\kappa\rho_{\mathrm{stab}} \le 3\times10^{-32}$ at the freeze-out), provided the shape mode is
stable, which remains OPEN.

**A rounding note.** The response of the four-dimensional cosmological term to a shift of the block vanishes at the stabilised
block,

$$
\frac{\mathrm{d}}{\mathrm{d}K}\Big[6H^2K\big(1 - 2w_{(2)}K\big) + \kappa\rho_{\mathrm{stab}}\Big]\Big\vert_{K = K_*} = 0
$$

<!-- symbols: diff, Kblock, Hconst, wL, kappa, rhostab, Kstar -->
<!-- begin generated symbol list -->
**Symbols in this equation.**

- $\mathrm{d}$: The differential: $\mathrm{d}X$ is an infinitesimal change of $X$, $\mathrm{d}X/\mathrm{d}Y$ the derivative of $X$ with respect to $Y$, $\mathrm{d}^nX$ the volume element of $n$ variables. Status: STANDARD.
- $K$: The block variable, $K = 1/f^2$. Unit: dimensionless. Status: DERIVED.
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the Lovelock couplings, the cosmological constant $\Lambda = -10H^2$ and the mass parameter $m_\Psi = H$. Unit: GeV (1/length). Value: 14.296 TeV (from the fit of $m_{\mathrm{W}}$ and $\rho_{\mathrm{EW},0}$). Status: AUTHOR.
- $w_{(p)}$: The author's Lovelock weights, $w_{(1)} = 1$, $w_{(2)} = 1/32$, $w_{(3)} = 1/1152$. Unit: dimensionless. Value: $(1, 1/32, 1/1152)$. Status: AUTHOR.
- $\kappa$: The eight-dimensional gravitational coupling, $\kappa = 8\pi G_8$. Unit: $\mathrm{GeV}^{-6}$. Value: $\kappa/V_\perp = 8\pi G_{\mathrm{N}}\mathcal{G}(K_*) = 2.328\times10^{-36}$ GeV$^{-2}$. Status: AUTHOR.
- $\rho_{\mathrm{stab}}$: The energy density of the block stabiliser, a function of the block scale, $\rho_{\mathrm{stab}} \propto f^{-8}$; its value at the static block is $\rho_{\mathrm{stab}}(f_*)$. Unit: $\mathrm{GeV}^{8}$. Value: $\kappa\rho_{\mathrm{stab}}(f_*) = (26 + 4\sqrt{51})H^2 = 54.566\,H^2$. Status: ASSUMED.
- $K_*$: The block variable of the stabilised block, $K_* = 12 + \frac43\sqrt{51}$ (the upper root $K_+$). Unit: dimensionless. Value: 21.5219. Status: DERIVED.

<!-- end generated symbol list -->

exactly (with $\kappa\rho_{\mathrm{stab}}$ proportional to $K^4$); the stored value $-6.3\times10^{-12}$ (`ks/feedback.json`, check
`friedmann_decoupled_from_block_shift`) is the rounding of the 12-digit $K_*$ and $\kappa\rho_{\mathrm{stab}}(f_*)$.

## The precision fixes of version 4 (commit `cc2d514`)

The residual analysis found five places where a stored number was limited by the numerics, not by the physics. Each was
fixed and the affected scripts rerun; every script exits with code 0 with all its checks.

**1. The response of the $W$ eigenvalue to the dark matter, by first-order perturbation theory.** Through I12 the scalar
density of the dark matter changes the gauge kinetic term along $x_0$:

$$
\begin{aligned}
&\frac{\Delta\alpha_3}{\alpha_3} = -4G_{\mathrm{g}}\,n_{\mathrm{DM,tot}},\qquad
 \frac{\Delta\alpha_2}{\alpha_2} = -4G_{\mathrm{W}}\,n_{\mathrm{DM,tot}},\qquad
 \frac{\Delta\alpha_1}{\alpha_1} = -4G_{\mathrm{B}}\,n_{\mathrm{DM,tot}},\\
&-\frac{1}{\Upsilon\,\mathrm{e}^{3HL\xi}}\,\frac{\mathrm{d}}{\mathrm{d}\xi}\Big(\Upsilon\,
 \mathrm{e}^{3HL\xi}\,\frac{\mathrm{d}F}{\mathrm{d}\xi}\Big)
 = \tilde m^2F,\qquad \Upsilon(\xi) = 1 + A_{\mathrm{mf}}\,n^{\mathrm{sc}}_{\mathrm{DM}},\qquad
 n^{\mathrm{sc}}_{\mathrm{DM}} = 2a_{\mathrm{DM}}b_{\mathrm{DM}},\\
&\frac{\mathrm{d}F}{\mathrm{d}\xi}(0) = 0,\qquad \Upsilon(-1)\,\frac{\mathrm{d}F}{\mathrm{d}\xi}(-1) =
 \beta_{\mathrm{W}}F(-1)
\end{aligned} \tag{FE-79}
$$

<!-- symbols: Delta, alpha3, Gg, nDMtot, alpha2, GW, alpha1, GB, Upsilon, euler, Hconst, Lcut, xi, diff, Fprof, mtilde, Amf, nscDM, abDM, betaW -->
<!-- begin generated symbol list -->
**Symbols in (FE-79).**

- $\Delta$: The change (difference or small perturbation) of the quantity that follows: $\Delta K$, $\Delta\rho$, $\Delta p_3$ are first-order changes about the static block, $\Delta\varepsilon_o$ a level shift, $\Delta m^2_{21} = m_2^2 - m_1^2$ a difference of squared masses, $\Delta N_{\mathrm{eff}}$ an addition to $N_{\mathrm{eff}}$, $\Delta S_{\mathrm{m}}$ the change of an action under a change $\Delta g^{MN}$ of the metric. Status: STANDARD.
- $\alpha_3$: The strong fine-structure constant, $\alpha_3 = g_3^2/(4\pi)$, at the scale given in brackets. Unit: dimensionless. Value: $\alpha_3(m_{\mathrm{Z}}) = 0.1180$; $\alpha_3(m_{\mathrm{KK}}) = 0.0606$. Status: STANDARD.
- $G_{\mathrm{g}}$: The coupling of a dark-matter pair to canonically normalised gluon pairs through I12. Unit: $\mathrm{GeV}^{-3}$. Value: $6.09\times10^{-15}$ GeV$^{-3}$ (benchmark). Status: DERIVED.
- $n_{\mathrm{DM,tot}}$: The total number density of dark-matter quanta: both species (the lowest odd levels of $\Psi_A$ and $\Psi_B$), particles and antiparticles, $n_{\mathrm{DM,tot}} = 2(n_{\mathrm{DM}} + \bar n_{\mathrm{DM}})$. Unit: $\mathrm{GeV}^{3}$. Status: STANDARD.
- $\alpha_2$: The SU(2) fine-structure constant, $\alpha_2 = g_2^2/(4\pi)$. Unit: dimensionless. Status: STANDARD.
- $G_{\mathrm{W}}$: The coupling of a dark-matter pair to canonically normalised SU(2) gauge pairs through I12. Unit: $\mathrm{GeV}^{-3}$. Value: $2.96\times10^{-15}$ GeV$^{-3}$. Status: DERIVED.
- $\alpha_1$: The hypercharge fine-structure constant, $\alpha_1 = g_1^2/(4\pi)$. Unit: dimensionless. Status: STANDARD.
- $G_{\mathrm{B}}$: The coupling of a dark-matter pair to canonically normalised hypercharge pairs through I12. Unit: $\mathrm{GeV}^{-3}$. Value: $1.08\times10^{-15}$ GeV$^{-3}$. Status: DERIVED.
- $\Upsilon(\xi)$: The factor by which the scalar density of the dark matter changes the gauge kinetic term along $x_0$ (I12), $\Upsilon = 1 + A_{\mathrm{mf}}n^{\mathrm{sc}}_{\mathrm{DM}}$. Unit: dimensionless. Status: DERIVED.
- $\mathrm{e}$: Euler's number, the base of the natural logarithm; $\mathrm{e}^{X}$ is the exponential of $X$. Unit: dimensionless. Value: 2.718281828. Status: STANDARD.
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the Lovelock couplings, the cosmological constant $\Lambda = -10H^2$ and the mass parameter $m_\Psi = H$. Unit: GeV (1/length). Value: 14.296 TeV (from the fit of $m_{\mathrm{W}}$ and $\rho_{\mathrm{EW},0}$). Status: AUTHOR.
- $L$: The depth of the regular tip: each half of a period of $x_0$ ends at $y = -L$; $HL = 3$. Unit: length. Value: $L = 3/H$ ($fL = 8.926\times10^{-21}$ m at the stabilised block). Status: ASSUMED.
- $\xi$: The scaled hidden coordinate, $\xi = y/L$, running from $-1$ (tip) to $0$ (fold) on each half of a period. Unit: dimensionless. Status: DERIVED.
- $\mathrm{d}$: The differential: $\mathrm{d}X$ is an infinitesimal change of $X$, $\mathrm{d}X/\mathrm{d}Y$ the derivative of $X$ with respect to $Y$, $\mathrm{d}^nX$ the volume element of $n$ variables. Status: STANDARD.
- $F(\xi),\ F_n$: The $x_0$ profile of a boson mode on one half of the period (a function of $y$ or of $\xi = y/L$): of a gauge field (gauge $A_y = 0$) or of the transverse-traceless graviton; $F_n$ is the profile of the $n$-th Kaluza-Klein level of the graviton tower ($F_0 = 1$ the flat zero mode). Unit: dimensionless. Status: DERIVED.
- $\tilde m,\ \tilde m_n$: The dimensionless $x_0$ eigenvalue of a boson mode, $\tilde m = m\,fL$; $\tilde m_n$ the $n$-th even Kaluza-Klein level of the tower with $\beta = 0$ ($\tilde m_1$ the first). Unit: dimensionless. Value: $\tilde m_1^2 = 30.1196$, $\tilde m_2^2 = 59.7284$, $\tilde m_3^2 = 109.0764$ ($HL = 3$), i.e. $\tilde m_1 = 5.48813$, $\tilde m_2 = 7.72842$, $\tilde m_3 = 10.44397$. Status: DERIVED.
- $A_{\mathrm{mf}}$: The amplitude of the I12 mean field in the $x_0$ problem of the gauge fields (a bookkeeping parameter: the result is linear in it). Unit: $\mathrm{GeV}^{-1}$ (with the orbital normalisation). Status: DERIVED.
- $n^{\mathrm{sc}}_{\mathrm{DM}}$: The scalar density of the dark-matter orbital, $n^{\mathrm{sc}}_{\mathrm{DM}} = 2a_{\mathrm{DM}}b_{\mathrm{DM}}$. Unit: GeV (normalised orbital). Status: DERIVED.
- $a_{\mathrm{DM}},\ b_{\mathrm{DM}}$: The upper and lower components of the dark-matter orbital (block spinor $(a, \mathrm{i}b)$, normalised on one half). Unit: $\mathrm{GeV}^{1/2}$. Status: DERIVED.
- $\beta_{\mathrm{W}}$: The Robin parameter of $W^+$ and $W^-$ (set by the tip mass term of the sigma field). Unit: dimensionless. Value: 0.011912 (fitted). Status: DERIVED.

<!-- end generated symbol list -->

With the weight $\Upsilon\,\mathrm{e}^{3HL\xi}$ on both sides, the eigenvalue is a Rayleigh quotient whose tip term does not
depend on $A_{\mathrm{mf}}$, so its derivative at $A_{\mathrm{mf}} = 0$ is, exactly,

$$
\frac{\mathrm{d}\tilde m^2}{\mathrm{d}A_{\mathrm{mf}}}\bigg\vert_{A_{\mathrm{mf}} = 0}
 = \frac{\displaystyle\int_{-1}^{0}n^{\mathrm{sc}}_{\mathrm{DM}}\,\mathrm{e}^{3HL\xi}\Big(\frac{\mathrm{d}F}{\mathrm{d}\xi}\Big)^2\mathrm{d}\xi
 - \tilde m^2\int_{-1}^{0}n^{\mathrm{sc}}_{\mathrm{DM}}\,\mathrm{e}^{3HL\xi}F^2\,\mathrm{d}\xi}
 {\displaystyle\int_{-1}^{0}\mathrm{e}^{3HL\xi}F^2\,\mathrm{d}\xi}
$$

<!-- symbols: diff, mtilde, Amf, nscDM, euler, Hconst, Lcut, xi, Fprof -->
<!-- begin generated symbol list -->
**Symbols in this equation.**

- $\mathrm{d}$: The differential: $\mathrm{d}X$ is an infinitesimal change of $X$, $\mathrm{d}X/\mathrm{d}Y$ the derivative of $X$ with respect to $Y$, $\mathrm{d}^nX$ the volume element of $n$ variables. Status: STANDARD.
- $\tilde m,\ \tilde m_n$: The dimensionless $x_0$ eigenvalue of a boson mode, $\tilde m = m\,fL$; $\tilde m_n$ the $n$-th even Kaluza-Klein level of the tower with $\beta = 0$ ($\tilde m_1$ the first). Unit: dimensionless. Value: $\tilde m_1^2 = 30.1196$, $\tilde m_2^2 = 59.7284$, $\tilde m_3^2 = 109.0764$ ($HL = 3$), i.e. $\tilde m_1 = 5.48813$, $\tilde m_2 = 7.72842$, $\tilde m_3 = 10.44397$. Status: DERIVED.
- $A_{\mathrm{mf}}$: The amplitude of the I12 mean field in the $x_0$ problem of the gauge fields (a bookkeeping parameter: the result is linear in it). Unit: $\mathrm{GeV}^{-1}$ (with the orbital normalisation). Status: DERIVED.
- $n^{\mathrm{sc}}_{\mathrm{DM}}$: The scalar density of the dark-matter orbital, $n^{\mathrm{sc}}_{\mathrm{DM}} = 2a_{\mathrm{DM}}b_{\mathrm{DM}}$. Unit: GeV (normalised orbital). Status: DERIVED.
- $\mathrm{e}$: Euler's number, the base of the natural logarithm; $\mathrm{e}^{X}$ is the exponential of $X$. Unit: dimensionless. Value: 2.718281828. Status: STANDARD.
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the Lovelock couplings, the cosmological constant $\Lambda = -10H^2$ and the mass parameter $m_\Psi = H$. Unit: GeV (1/length). Value: 14.296 TeV (from the fit of $m_{\mathrm{W}}$ and $\rho_{\mathrm{EW},0}$). Status: AUTHOR.
- $L$: The depth of the regular tip: each half of a period of $x_0$ ends at $y = -L$; $HL = 3$. Unit: length. Value: $L = 3/H$ ($fL = 8.926\times10^{-21}$ m at the stabilised block). Status: ASSUMED.
- $\xi$: The scaled hidden coordinate, $\xi = y/L$, running from $-1$ (tip) to $0$ (fold) on each half of a period. Unit: dimensionless. Status: DERIVED.
- $F(\xi),\ F_n$: The $x_0$ profile of a boson mode on one half of the period (a function of $y$ or of $\xi = y/L$): of a gauge field (gauge $A_y = 0$) or of the transverse-traceless graviton; $F_n$ is the profile of the $n$-th Kaluza-Klein level of the graviton tower ($F_0 = 1$ the flat zero mode). Unit: dimensionless. Status: DERIVED.

<!-- end generated symbol list -->

evaluated with the exact $W$ eigenfunction of the fold condition (its tip condition holds with the stored $\tilde m_{\mathrm{W}}^2$
to $6\times10^{-12}$)

$$
\begin{aligned}
&F(\xi) = \mathrm{e}^{-3HL\xi/2}\Big(\cosh\varkappa_{\mathrm{W}}\xi + \frac{3HL}{2\varkappa_{\mathrm{W}}}\sinh\varkappa_{\mathrm{W}}\xi\Big),
\qquad \frac{\mathrm{d}F}{\mathrm{d}\xi} = -\frac{\tilde m_{\mathrm{W}}^2}{\varkappa_{\mathrm{W}}}\,\mathrm{e}^{-3HL\xi/2}\sinh\varkappa_{\mathrm{W}}\xi,\\
&\varkappa_{\mathrm{W}} = \Big(\frac{9H^2L^2}{4} - \tilde m_{\mathrm{W}}^2\Big)^{1/2}
\end{aligned}
$$

<!-- symbols: Fprof, euler, Hconst, Lcut, xi, prov_varkappaW, diff, mtildeW -->
<!-- begin generated symbol list -->
**Symbols in this equation.**

- $F(\xi),\ F_n$: The $x_0$ profile of a boson mode on one half of the period (a function of $y$ or of $\xi = y/L$): of a gauge field (gauge $A_y = 0$) or of the transverse-traceless graviton; $F_n$ is the profile of the $n$-th Kaluza-Klein level of the graviton tower ($F_0 = 1$ the flat zero mode). Unit: dimensionless. Status: DERIVED.
- $\mathrm{e}$: Euler's number, the base of the natural logarithm; $\mathrm{e}^{X}$ is the exponential of $X$. Unit: dimensionless. Value: 2.718281828. Status: STANDARD.
- $H$: The author's constant (an inverse length) that fixes the period $\pi/(6H)$ of $x_0$, the Lovelock couplings, the cosmological constant $\Lambda = -10H^2$ and the mass parameter $m_\Psi = H$. Unit: GeV (1/length). Value: 14.296 TeV (from the fit of $m_{\mathrm{W}}$ and $\rho_{\mathrm{EW},0}$). Status: AUTHOR.
- $L$: The depth of the regular tip: each half of a period of $x_0$ ends at $y = -L$; $HL = 3$. Unit: length. Value: $L = 3/H$ ($fL = 8.926\times10^{-21}$ m at the stabilised block). Status: ASSUMED.
- $\xi$: The scaled hidden coordinate, $\xi = y/L$, running from $-1$ (tip) to $0$ (fold) on each half of a period. Unit: dimensionless. Status: DERIVED.
- $\varkappa_{\mathrm{W}}$: The decay constant of the exact $x_0$ profile of $W^+$ and $W^-$, whose eigenvalue lies below the gap $9H^2L^2/4$: $\varkappa_{\mathrm{W}} = (9H^2L^2/4 - \tilde m_{\mathrm{W}}^2)^{1/2}$ (for such a profile the wave number $\varpi$ of the oscillating profiles is imaginary, $\varpi = \mathrm{i}\varkappa_{\mathrm{W}}$). Unit: dimensionless. Value: 4.4999985 ($HL = 3$). Status: DERIVED.
- $\mathrm{d}$: The differential: $\mathrm{d}X$ is an infinitesimal change of $X$, $\mathrm{d}X/\mathrm{d}Y$ the derivative of $X$ with respect to $Y$, $\mathrm{d}^nX$ the volume element of $n$ variables. Status: STANDARD.
- $\tilde m_{\mathrm{W}}$: The dimensionless $x_0$ eigenvalue of the lowest $W^\pm$ mode ($\beta = \beta_{\mathrm{W}}$). Unit: dimensionless. Value: $\tilde m_{\mathrm{W}}^2 = 1.32149\times10^{-5}$. Status: DERIVED.

<!-- end generated symbol list -->

and the dark-matter orbital on the 800 Gauss nodes of the Kohn-Sham cell. Result:
$\mathrm{d}\ln\tilde m_{\mathrm{W}}^2/\mathrm{d}A_{\mathrm{mf}} = -0.111252909326$ (`coupled.json`, key
`WZ_kinetic_shift/dlnLambdaW_damp`), confirmed by shooting the perturbed problem (DOP853, Richardson in the amplitude) to
$3\times10^{-11}$. Version 3 quoted $-0.1126$ from finite differences of finite-element eigenvalues, which are dominated by
rounding. For the photon and the gluons the flat profile $F = 1$ solves the problem for every $\Upsilon$, so their eigenvalue
stays exactly zero (version 3: $-2.5\times10^{-11}$, rounding). The physical shift stays negligible: at the freeze-out, where
the amplitude is largest ($A_{\mathrm{mf}} = 1.7\times10^{-16}$), $\tilde m_{\mathrm{W}}^2$ moves by $1.9\times10^{-17}$ of itself.

**2. A robust integration of the right-handed neutrinos of the $B - L$ alternative.** The counterfactual of FE-131,

$$
\begin{aligned}
&G_{\mathrm{A}}^{B-L} = G_{\mathrm{A}}\Big[\frac{\mathcal{S}_B}{\mathcal{S}_{B-L}}\Big]^{1/2},\qquad
 \mathcal{S}_B = \sum_fN_{\mathrm{c}}\big(q^{B}_f\tilde I^{(b)}_{of}\big)^2,\qquad
 \mathcal{S}_{B-L} = \sum_fN_{\mathrm{c}}\big(q_f\tilde I^{(b)}_{of}\big)^2,\\
&\frac{\mathrm{d}n_{\nu_R}}{\mathrm{d}x_4} + 3\mathcal{H}n_{\nu_R} = \Gamma_\nu\Big(1 -
 \frac{n_{\nu_R}^2}{(n_{\nu_R}^{\mathrm{eq}})^2}\Big),\qquad
 \Gamma_\nu = 2\,n_{\mathrm{DM,eq}}\,\bar n_{\mathrm{DM,eq}}\,\frac{G_\nu^2M_{\mathrm{DM}}^2}{2\pi},\qquad
 G_\nu = G_{\mathrm{A}}^{B-L}\,\tilde I^{(b)}_{\nu_R},\\
&n_{\nu_R}^{\mathrm{eq}} = \frac34\,\frac{\zeta(3)}{\pi^2}\,T^3,\qquad
 n_{\mathrm{DM,eq}} = \bar n_{\mathrm{DM,eq}} = 2\Big(\frac{M_{\mathrm{DM}}T}{2\pi}\Big)^{3/2}\mathrm{e}^{-x}
\end{aligned} \tag{FE-131}
$$

<!-- symbols: GABL, GA, SB, if, Nc, qB, tildeIb, io, qBL, diff, nnuR, x4, Hubble, Gammanu, nDMeq, Gnu, MDM, pi, zeta3, Temp, euler, xMT -->
<!-- begin generated symbol list -->
**Symbols in (FE-131).**

- $G_{\mathrm{A}}^{B-L}$: The strength I13 would need if it coupled to the $B - L$ current (the same relic density). Unit: $\mathrm{GeV}^{-2}$. Status: DERIVED.
- $G_{\mathrm{A}}$: The four-dimensional strength of the portal I13 on the zero modes, $G_{\mathrm{A}} = c_{\mathrm{A}}H/(2f^4v_{\mathrm{t}}\Lambda_\star^6)$. Unit: $\mathrm{GeV}^{-2}$. Value: $1.278\times10^{-9}$ GeV$^{-2}$ (dark-matter relic density). Status: DERIVED.
- $\mathcal{S}_B,\ \mathcal{S}_{B-L}$: The colour-weighted sums of the squared I13 overlaps of the dark matter with the baryon-number and with the $B - L$ charges. Unit: dimensionless. Value: $\mathcal{S}_B = 16.351$, $\mathcal{S}_{B-L} = 22.92$. Status: DERIVED.
- $f$: The label of a fermion species: a Standard-Model multiplet of one generation (its $N_{\mathrm{c}}$ Weyl components share one zero-mode profile; the zero mode of each chirality) or a fermion of a medium (electron, proton, neutron); a sum over $f$ runs over these species. Status: STANDARD.
- $N_{\mathrm{c}}$: The number of Weyl components of a fermion multiplet that share its zero-mode profile and overlap (colour times isospin): 6 for a quark doublet, 3 for a quark singlet, 2 for a lepton doublet, 1 for a charged-lepton singlet. Unit: dimensionless. Status: STANDARD.
- $q^B_\psi,\ q^B_f$: The baryon number of the multiplet $\psi$ or of the fermion component $f$ ($\frac13$ for quarks, 0 for leptons). Unit: dimensionless. Status: STANDARD.
- $\tilde I^{(b)}_{of}$: The overlap of the lower component of the state $o$ with the zero mode of $f$, $\tilde I^{(b)}_{of} = H^{-1}\int_{-L}^{0}b_o^2\varrho_f\mathrm{e}^{-3Hy}\mathrm{d}y$ (the overlap of I13); $\tilde I^{(b)}_Q$, $\tilde I^{(b)}_{u_R}$, $\tilde I^{(b)}_{d_R}$, $\tilde I^{(b)}_{\nu_R}$ those of the dark matter. Unit: dimensionless. Value: dark matter: $\tilde I^{(b)}_Q = 2.6135$. Status: DERIVED.
- $o$: The label of a Kohn-Sham orbital (a state of dirac16complex in the cell: block, momentum shell, fold parity and level); a sum over $o$ runs over the orbitals. Status: RECORD.
- $q_\psi,\ q_f$: The $B - L$ charge: $q_\psi$ of the multiplet $\psi$ ($q_Q = q_{u_R} = q_{d_R} = \frac13$, $q_\ell = q_{e_R} = q_{\nu_R} = -1$), $q_f$ of the fermion component $f$. Unit: dimensionless. Status: STANDARD.
- $\mathrm{d}$: The differential: $\mathrm{d}X$ is an infinitesimal change of $X$, $\mathrm{d}X/\mathrm{d}Y$ the derivative of $X$ with respect to $Y$, $\mathrm{d}^nX$ the volume element of $n$ variables. Status: STANDARD.
- $n_{\nu_R},\ n_{\nu_R}^{\mathrm{eq}}$: The number density of the right-handed neutrinos (three generations) and its equilibrium value. Unit: $\mathrm{GeV}^{3}$. Status: DERIVED.
- $x_4$: The time; dots denote $\mathrm{d}/\mathrm{d}x_4$. Unit: length (= time, c = 1). Status: AUTHOR.
- $\mathcal{H}$: The expansion rate of ordinary 3-space, $\mathcal{H} = \dot a_4$ (the Hubble rate of the observer; in the hot Universe $\mathcal{H} = (8\pi^3g_\rho/90)^{1/2}T^2/M_{\mathrm{Pl}}$). Unit: GeV. Status: DERIVED.
- $\Gamma_\nu$: The production rate per volume of right-handed neutrinos in the counterfactual $B - L$ variant of I13. Unit: $\mathrm{GeV}^{4}$. Status: DERIVED.
- $n_{\mathrm{DM,eq}},\ \bar n_{\mathrm{DM,eq}}$: The equilibrium number densities of dark-matter particles and antiparticles of one species. Unit: $\mathrm{GeV}^{3}$. Status: STANDARD.
- $G_\nu$: The four-dimensional coupling of the dark matter to a right-handed neutrino in the $B - L$ variant of I13. Unit: $\mathrm{GeV}^{-2}$. Status: DERIVED.
- $M_{\mathrm{DM}}$: The mass of a dark-matter particle (the lowest odd level of dirac16complex). Unit: GeV. Value: 44.35 TeV. Status: DERIVED.
- $\pi$: The number pi, the ratio of the circumference of a circle to its diameter. Unit: dimensionless. Value: 3.141592654. Status: STANDARD.
- $\zeta$: The Riemann zeta function; only its value $\zeta(3)$ occurs, the sum of $1/n^3$ over the positive integers $n$. Unit: dimensionless. Value: $\zeta(3) = 1.2020569$. Status: STANDARD.
- $T$: The temperature of the plasma (of the photons and of every species in equilibrium with them); in the Mermin occupations the temperature of the Kohn-Sham state. Unit: GeV. Status: STANDARD.
- $\mathrm{e}$: Euler's number, the base of the natural logarithm; $\mathrm{e}^{X}$ is the exponential of $X$. Unit: dimensionless. Value: 2.718281828. Status: STANDARD.
- $x$: The ratio $x = M_{\mathrm{DM}}/T$ of the dark-matter mass to the temperature. Unit: dimensionless. Value: $x_{\mathrm{f}} = 31.23$ at the freeze-out. Status: STANDARD.

<!-- end generated symbol list -->

is integrated for the abundance $n_{\nu_R}/s$ from zero at $x = 2$. The equilibration from zero takes only about
$7\times10^{-11}$ in $x$ (the equilibrium abundance divided by its initial rate of growth); to resolve its start the error
control of the Radau method needs steps of about $7\times10^{-11}$ times the square root of the relative tolerance
($7\times10^{-15}$ at the version-3 tolerance $10^{-8}$), at or below the smallest step it allows at $x = 2$ (ten times the
spacing of the floating-point numbers, $4.4\times10^{-15}$), so the integration in $x$ could stop at its first step depending on
the last digits of the inputs. It now runs in the shifted variable $x - 2$ (from 0 to
38), where the steps are free, with a relative tolerance of $10^{-13}$: $n_{\nu_R}/n_{\nu_R}^{\mathrm{eq}} = 0.999697681992$ at
$x = 40$ (`coupled.json`, `I13_B_minus_L_alternative/Y_nuR_over_Yeq_at_x40`), stable to $3\times10^{-13}$ when the coupling is
changed by $\pm10^{-12}$ (check `R_right_handed_neutrino_boltzmann`). The version-3 statement (0.9997 of equilibrium,
$\Delta N_{\mathrm{eff}} = 0.144$) is unchanged.

**3. The integrals of the cosmic neutrino background to $3\times10^{-16}$.** The integrals of

$$
\begin{aligned}
&f_{\mathrm{FD}}(k) = \frac{1}{\mathrm{e}^{k/T_\nu} + 1},\qquad
 n_i = 2\int\frac{\mathrm{d}^3\vec k}{(2\pi)^3}\,f_{\mathrm{FD}} = \frac{3\zeta(3)}{2\pi^2}\,T_\nu^3,\qquad
 \rho_i = 2\int\frac{\mathrm{d}^3\vec k}{(2\pi)^3}\,\sqrt{k^2 + m_i^2}\,f_{\mathrm{FD}},\\
&\bar v_i = \frac{\int_0^\infty k^2\,\frac{k}{\sqrt{k^2 +
 m_i^2}}\,f_{\mathrm{FD}}\,\mathrm{d}k}{\int_0^\infty k^2\,f_{\mathrm{FD}}\,\mathrm{d}k},
 \qquad \text{flavour content of }\nu_i:\ \lvert U_{\alpha i}\rvert^2
\end{aligned} \tag{FE-120}
$$

<!-- symbols: fFD, kwave, euler, Tnu, ndens, ii, diff, kvec, pi, zeta3, rho, mmass, vbar, infty, nuflav, Upmns, ialpha -->
<!-- begin generated symbol list -->
**Symbols in (FE-120).**

- $f_{\mathrm{FD}}$: The Fermi-Dirac distribution of the relic neutrinos, $f_{\mathrm{FD}} = 1/(\mathrm{e}^{k/T_\nu} + 1)$. Unit: dimensionless. Status: STANDARD.
- $k$: The magnitude of the wave vector (the momentum, $\hbar = 1$) of a mode: in the reduction, the Kohn-Sham and the perturbation equations the comoving wavenumber (physical momentum $\mathrm{e}^{-a_4}k$); in the thermal integrals the momentum of a particle at the time considered (the variable of integration). Unit: GeV (1/length). Status: STANDARD.
- $\mathrm{e}$: Euler's number, the base of the natural logarithm; $\mathrm{e}^{X}$ is the exponential of $X$. Unit: dimensionless. Value: 2.718281828. Status: STANDARD.
- $T_\nu$: The temperature of the relic neutrinos (one common temperature). Unit: GeV. Value: 1.9454 K today. Status: STANDARD.
- $n,\ n_o,\ n_{\psi i},\ n_f,\ n_i$: A number density: $n(y)$ the particle density of dirac16complex in the Kohn-Sham equations and $n_o$ the contribution of the orbital $o$, $n_{\psi i}(y)$ the density of the Standard-Model fermion $\psi_i$ (per proper 7-volume of eight dimensions); $n_f$ the density of the fermion component $f$ and $n_i$ that of the neutrino mass state $i$ (per 3-volume of four dimensions). Unit: $\mathrm{GeV}^{7}$ (eight dimensions), $\mathrm{GeV}^{3}$ (four dimensions). Status: STANDARD.
- $i$: The generation index ($i = 1, 2, 3$), which also labels the neutrino mass states $\nu_1, \nu_2, \nu_3$; a repeated index is not summed unless a sum sign is written. Status: STANDARD.
- $\mathrm{d}$: The differential: $\mathrm{d}X$ is an infinitesimal change of $X$, $\mathrm{d}X/\mathrm{d}Y$ the derivative of $X$ with respect to $Y$, $\mathrm{d}^nX$ the volume element of $n$ variables. Status: STANDARD.
- $\vec k,\ \vec k_o$: The wave vector (momentum) in ordinary 3-space; $\vec k_o$ that of the orbital $o$, a point of the lattice $k_{\mathrm{lat}}\vec n_o$. Unit: GeV. Status: STANDARD.
- $\pi$: The number pi, the ratio of the circumference of a circle to its diameter. Unit: dimensionless. Value: 3.141592654. Status: STANDARD.
- $\zeta$: The Riemann zeta function; only its value $\zeta(3)$ occurs, the sum of $1/n^3$ over the positive integers $n$. Unit: dimensionless. Value: $\zeta(3) = 1.2020569$. Status: STANDARD.
- $\rho$: An energy density: in eight dimensions $\rho = -\mathcal{T}^{x_4}{}_{x_4}$ (of the total source, or of the species named by a subscript; $\rho_s$ of the species $s$, $\rho_i$ of the neutrino mass state $i$); in the cosmological perturbation equations $\Delta\rho$ is the density perturbation summed over the species. Unit: $\mathrm{GeV}^{8}$ (eight dimensions), $\mathrm{GeV}^{4}$ (four dimensions). Status: STANDARD.
- $m,\ m_s,\ m_i$: A four-dimensional mass: $m$ the mass of a mode (the eigenvalue of an $x_0$ problem) or of a fermion; $m_s$ the mass of the species $s$; $m_i$ the mass of the neutrino mass state $i$. Unit: GeV. Status: DERIVED.
- $\bar v_i$: The mean velocity of the relic neutrinos of the mass state $i$. Unit: dimensionless (c = 1). Value: 0.435, 0.0604, 0.0105 today. Status: STANDARD.
- $\infty$: Infinity: as a limit of an integral or a sum it means that the range has no upper bound. Status: STANDARD.
- $\nu_\alpha,\ \nu_i$: A left-handed neutrino: $\nu_\alpha$ of the flavour $\alpha = e, \mu, \tau$ ($\nu_e$, $\nu_\mu$, $\nu_\tau$), $\nu_i$ of the mass state $i$ (mass $m_i$). Unit: $\mathrm{GeV}^{3/2}$. Status: STANDARD.
- $U$: The PMNS matrix, the unitary $3 \times 3$ mixing matrix of the leptons, $\nu_\alpha = \sum_iU_{\alpha i}\nu_i$ (rows $\alpha = e, \mu, \tau$, columns the mass states $i$); in UM-2 $U = \mathcal{K}_e^\dagger\mathcal{K}_\nu$. Unit: dimensionless. Value: $\sin^2\theta_{12} = 0.308$, $\sin^2\theta_{13} = 0.02215$, $\sin^2\theta_{23} = 0.470$, $\delta_{\mathrm{CP}} = 212^\circ$ (NuFIT 6.0). Status: STANDARD.
- $\alpha$: A flavour index running over $e, \mu, \tau$ (the flavour states of the leptons and neutrinos). Status: STANDARD.

<!-- end generated symbol list -->

are of order $T_\nu^4 \approx 10^{-15}$ eV$^4$, far below the default absolute tolerance of the adaptive quadrature, which
therefore stopped at a relative error of $5.8\times10^{-7}$; with a relative tolerance only they are accurate to
$3\times10^{-16}$: $\Omega_\nu h_{100}^2 = 6.38217282098\times10^{-4}$; mean velocities 0.435132624815, 0.0604083086104,
0.0105351736626; energy densities $9.95804523965\times10^{-16}$, $7.51619688306\times10^{-15}$,
$4.31573842483\times10^{-14}$ eV$^4$ (`neutrino.json`, `CNB`, copied in `cosmology.json`). Every number quoted in version 3 is
unchanged at its quoted precision.

**4. Deterministic thread counts in the Kohn-Sham scripts.** The number of threads of the linear algebra (BLAS, LAPACK,
OpenMP) is now fixed to one in `um2_kohnsham.py`, `um2_ks_jobs.py`, `um2_coupled.py` and `um2_residuals.py`, before numpy is
imported: with two threads the energy of the 8-particle state with $\lambda_{\mathrm{test}}$ had differed by $5\times10^{-13}\,H$,
and the fresh-clone runs of versions 1 to 3 had found one Kohn-Sham integral differing by $1.1\times10^{-12}$ relative because
threaded sums are not taken in a fixed order. The rerun changed only quantities at the rounding level, among them quantities
that are zero in exact arithmetic: the changes of the fold-band gap per unit amplitude, $7.9\times10^{-11}$ (electron density),
$3.0\times10^{-9}$ (up-quark density), $-9.3\times10^{-11}$ (neutrino density), $-1.4\times10^{-10}$ (gluon condensate) and
$1.2\times10^{-13}$ (the I13 shift of the fold band); and the observed order of the Kohn-Sham energy of the stress state, now
4.956 (version 3: 4.95).

**5. A stale check text.** The text of the check `tip_Z_portal_dropped` of `um2_electroweak.py` still said "$c_{\mathrm{V}} = 0$
for I11" (version 2); it now states that I11 is kept with the freeze-in strength $G_{\mathrm{V}} = 4.38\times10^{-17}$
GeV$^{-2}$, at which the fold bands are produced only by freeze-in ($\Delta N_{\mathrm{eff}} = 0.001$). No number changed.

## What changed in the claims

No claim of version 3 changes; the status labels are those of version 3, and the conflicts with data stand (no Higgs boson;
the unitarity of $W^+W^-$ scattering near 1.2 TeV). Numbers changed by the precision fixes:
$\mathrm{d}\ln\tilde m_{\mathrm{W}}^2/\mathrm{d}A_{\mathrm{mf}} = -0.11125$ (was $-0.1126$), the photon's value exactly zero (was
$-2.5\times10^{-11}$), the observed order 4.96 (was 4.95), the rounding-level values listed in fix 4, and further digits of the
CNB. Statements made precise by the residual analysis: the two values of the weak angle and their 0.83 % effect on the
$Z$ width; the physics accuracy of about 1 % of $G_{\mathrm{A}}$; the block-shape source, now quantified (OPEN); the fold
bands missing from the Hubble rate of the thermal history ($1.7\times10^{-4}$); the instantaneous neutrino decoupling of the
thermal history (0.59 % in $g_\rho$ today, without effect on a result).

# The verification record

Version 1 was rerun from fresh clones of the repository on 2026-10-17 at commit `b3c3c1a` (179 of 179 checks) and on
2026-10-18 at the commits `fa7305f`, `9285bb6` (180 of 180) and `5b73d16` (182 of 182; every computation as a separate step,
the longest 247 s); version 2 on 2026-10-18 at commit `4a6421d` (205 of 205; every computation as a separate step, 1027 s in
all); version 3 on 2026-10-18 at commit `726997f` (233 of 233; every computation as a separate step, 1100 s in all, the
longest the primordial integration with 269 s) and again, after the fixes of its independent review, at commit `815db9e`
(235 of 235; 1116 s in all, the primordial integration 269 s). In every run every check passed and every stored number was
reproduced to a relative $10^{-9}$ or better; in the runs from `9285bb6` on all numbers were identical except the run times,
the texts of check details and one Kohn-Sham integral, which differed by $1.1\times10^{-12}$ relative because the threaded
linear algebra did not sum in a fixed order (version 4 fixes the thread count, section 10); and the LaTeX sources, the PDF
documents and the figures were rebuilt byte-identical. Between the two runs of version 2, `um2_analysis.py` gained the
$^3P_0$ unitarity bound of item 22 (new stored numbers, the same 23 checks). After the run of version 3 at `726997f` the fixes of
its independent review (item 24) changed `um2_thermal.py`, `um2_coupled.py`, `um2_series.py`, `um2_cosmology.py` and the
`feedback` job of `um2_ks_jobs.py`, which were rerun in dependency order before the run at `815db9e`.

Version 4: the precision fixes of commit `cc2d514` changed `um2_coupled.py`, `um2_electroweak.py`, `um2_kohnsham.py`,
`um2_ks_jobs.py` and `um2_neutrino.py`; the affected computations (the seven Kohn-Sham jobs, `um2_neutrino.py`,
`um2_electroweak.py`, `um2_cosmology.py`, `um2_coupled.py`) and the new `um2_residuals.py` were rerun, and every script exits
with code 0 with all its checks: 287 of 287 (the reports in `universe_model_2/reports`). A rerun of version 4 from a fresh
clone is not part of this record.

# Corrections made during the work

1. The gauge-invariance test of the tip terms first used the wrong sign of the hypercharge phase; with
   $\psi \to \mathrm{e}^{\mathrm{i}Y\vartheta}\psi$ every term is invariant to $4\times10^{-15}$.
2. The finite-element cross-check of $\tilde m_{\mathrm{W}}^2$ was first limited by rounding; the Rayleigh quotient of the
   gradient form with Richardson extrapolation (observed order 4.01) agrees with the exact value to $3\times10^{-14}$.
3. The Kohn-Sham basis convergence and the conservation law were first checked without extrapolation; Richardson in the
   basis size (observed orders 4.95 for the energy, 2.97 for the hidden pressure; 4.96 for the energy since the
   deterministic thread count of version 4) was added.
4. The self-consistency loop did not converge for 592 particles at the record's coupling; a fixed labelling of the
   occupied set and a safeguarded Anderson mixing were introduced, the test coupling $\lambda_{\mathrm{test}}$ was adopted,
   and the record's coupling is kept as a stress test, which now converges.
5. A first statement that every primordial start above the unstable static block reaches the stable one was false in
   detail; the separatrix (the threshold of the initial $K$ as a function of the initial $\mathcal{H}_f$) was computed by
   bisection instead.
6. The primordial figure was first sampled too coarsely (aliasing of the radion oscillation) and is now densely sampled.
7. The sum rules of the uncertainty analysis were first imprecise for the sharp fermion zero modes; exact mpmath
   normalisation and the tip term fixed them ($10^{-8}$).
8. The radion quantity was stored under a wrong sign label; it is now stored as $\omega_{\mathrm{r}}^2$, the determinant of
   the Jacobian of the block equations.
9. Portal names of the first universe model (P1 to P6) in two check texts were replaced by I9, I11, I12.
10. The gauge-kinetic portal was first written with the scale to the power 5, which is dimensionally wrong in the geometric
    normalisation of the gauge fields; it is $\bar\Psi\Psi\,\mathcal{F}/\Lambda_\star^3$ (IN-17), and the symbol of the portal
    scale was changed so that it no longer clashes with the Dirichlet bound of the tip.
11. Before publication every number of the documents was compared with the computed outputs; four statements were
    corrected (the dark-matter wave number $\varpi = 1.89901$, the finite-element agreement $5\times10^{-10}$, the TT and EE
    agreements of version 1, and the restriction $\mathcal{H} = 0$ of the sourceless static block).
12. The kinetic term of the tip sigma field was first written with the sign of the signature $(+,-,-,-)$; in the
    signature $(+,+,+,-)$ of $x_1, \dots, x_4$ it is $-\frac{v_\Sigma^2}{4}\mathrm{tr}\big((D_\mu\Sigma)^\dagger D^\mu\Sigma\big)$,
    which gives mass terms $-\frac12$ times the squared mass times the square of the vector field with a positive squared
    mass (the computations always used positive squared masses).
13. With the real matrices $C\gamma^a$ antisymmetric, $\bar\Psi\gamma^a\Psi$ is anti-Hermitian; the portal currents are now
    written as the Hermitian currents $\mathrm{i}\bar\Psi\gamma^M\Psi$ and the Standard-Model currents as
    $\mathrm{i}\bar\psi\gamma^M\psi$.
14. The block response to the hidden pressure of a Kohn-Sham state first used $p_0$ alone; the common block scale is driven
    by the block-averaged pressure $\bar p = (p_0 + 3p_5)/4$, and $p_0 - p_5$ drives a block-shape mode outside the order-0
    metric (OPEN; quantified in version 4, section 10). The linearised sourced equations were added (`um2_background.py`,
    2 checks); they first omitted the density, which enters at first order through $3\mathcal{G}(K_*)\mathcal{H}^2 =
    \kappa\Delta\rho$; with it the adiabatic response reproduces the four-dimensional Friedmann acceleration equation exactly.
15. The statement that the numbers of quanta of $\Psi_A$ and $\Psi_B$ are separately conserved was first recorded as an
    asserted check; it is now computed with the author's matrices (commutators of $\mathcal{B}$ with $C$, $\gamma^a$,
    $C\gamma^a$, $\mathcal{S}^{ab}$), which also shows that extra-time momenta, outside the good sector, would mix the halves.
16. The radion lifetime was first quoted as an unverified estimate; it is now computed (ESTIMATE, with the coupling factor
    $C_{\mathrm{r}}$ explicit), as is the bound on the block rate today.
17. Figures: the BAO legend showed the data label twice and two labels of the uncertainty figure overlapped; the condensate
    figure no longer draws the vertical lines where its equation of state diverges.
18. An independent review of the five documents of version 1 against the outputs found, and the documents were corrected:
    the first-order fermion mass formula (it needs $\mathcal{Z}(-c_R)$ for the singlet, $c_R < 0$; the code always used the
    absolute value); the gap statement, which holds for the boson operators but not for $\Psi$ (the dark matter, 44.35 TeV,
    lies below the boson gap of 99.5 TeV); the sensitivity of $G_{\mathrm{N}}$ to the block, which is
    $\mathrm{d}\ln G_{\mathrm{N}}/\mathrm{d}\ln f = -4 + 2K_*(\mathrm{d}\mathcal{G}/\mathrm{d}K)/\mathcal{G}$ at $K_*$, $= +2.05$, and
    not $-4$ (recomputed; the lunar-ranging bound becomes $7.1\times10^{-4}\mathcal{H}_0$); $\Delta N_{\mathrm{eff}}$ of a
    thermalised fold band (recomputed); a level spacing (0.25000); a rounding (1.948); the definitions of $\bar M_{\mathrm{Pl}}$,
    $M_{\mathrm{Pl}}$, the radion formulas, the spread $\Delta(fy)$ of the proper hidden length, the unitarity estimate and the
    cosmic-variance measure; the statement on proper and coordinate localisation; and several notational clashes (a letter
    then used for $\mathrm{e}^{-a_4}$ is now written out).
19. A second review of version 1 found, and the documents were corrected: the electroweak parameter was written with the
    measured masses, $m_{\mathrm{W}}^2/(m_{\mathrm{Z}}^2\cos^2\theta_{\mathrm{W}})$, next to the on-shell definition
    $\cos^2\theta_{\mathrm{W}} = m_{\mathrm{W}}^2/m_{\mathrm{Z}}^2$, which makes it identically 1; the computation always used
    $\rho_{\mathrm{EW}} = \tilde m_{\mathrm{W}}^2/(\tilde m_{\mathrm{Z}}^2\cos^2\theta_{\mathrm{W}})$. Checking the uncertainty relation
    for every state then showed that the bound $\langle k_\xi^2\rangle \ge 1/(4\Delta\xi^2)$ quoted for the hidden kinetic
    energy is not valid on the cell: the tip, where the cell ends, adds a boundary term, and the valid relation is
    $\langle k_\xi^2\rangle^{1/2}\Delta\xi \ge (1 - \varrho_\xi(-1))/2$ (the broad fold zero mode of $\Psi$ has
    $\langle k_\xi^2\rangle\Delta\xi^2 = 0.097$); a computed check of it was added. Further: the $\overline{\mathrm{MS}}$ angle in the
    $Z$ widths, the shooting accuracy, the normalisation volume $\mathrm{Vol}_7$ (not the proper seven-volume), the
    occupations $\phi_o$, the tip coupling matrices, and the notation (with a list of the symbols with more than one use in
    each document; version 4 replaces these lists by one meaning per symbol).
20. A third review of version 1 found, and the computations and documents were corrected: (a) the $W^\pm$, $Z$ fit set the
    angle of the gauge couplings equal to the on-shell angle of the measured masses and fitted the tree-level
    $\rho_{\mathrm{EW}} - 1$ to $\rho_{\mathrm{EW},0} - 1$, which put the model's $m_{\mathrm{Z}} = 91.1706$ GeV 17 MeV below the
    measured value; since $\rho_{\mathrm{EW},0}$ measures the custodial violation beyond the Standard-Model loops, the angle of the
    couplings is now fixed by the measured masses, $\cos^2\theta_{\mathrm{W}} = (m_{\mathrm{W}}^2/m_{\mathrm{Z}}^2)/\rho_{\mathrm{EW},0}
    = 0.776368$, and the model reproduces both masses (check `mZ_reproduced`); $\beta_{\mathrm{W}} = 0.011912$ and every scale in GeV
    moved by $+8.50\times10^{-4}$ ($m_{\mathrm{KK}} = 121.32$ TeV, $H = 14.296$ TeV, gap 99.48 TeV, radion 48.42 TeV,
    $M_{\mathrm{DM}} = 44.35$ TeV). The tree-level $Z$ widths with the angle of the couplings were added (check
    `Z_width_scheme`). (b) The familiar bound $\langle k_\xi^2\rangle \ge 1/(4\Delta\xi^2)$ is guaranteed only for profiles
    negligible at the tip. (c) Symbol lists and wording.
21. **Version 2 (2026-10-18): three generations and three neutrino flavours.** By the author's orders of 2026-10-18 (option
    A): (a) three generations of quarks and leptons with one doublet bulk mass per sector, the twelve masses as exact $x_0$
    eigenvalues and the PMNS and CKM matrices as the tip matrices, proved exact for three generations (`um2_flavour.py`, new;
    `um2_spectra.py`, `um2_fields.py` extended); (b) the flavour conversion of the three neutrinos (`um2_neutrino.py`, new):
    vacuum, matter, accelerators, the Sun, the early Universe and $N_{\mathrm{eff}}$, the CNB of three mass states,
    supernovae; (c) the chiral tip $Z$ portal I9 is removed: with three neutrinos it has no role left, its even part is
    bounded by the invisible width ($N_\nu = 3 + 2r_{\mathrm{Z}}^2$, $r_{\mathrm{Z}}^2 < 0.0056$) and would still keep the fold band in
    equilibrium to 14.7 MeV ($\Delta N_{\mathrm{eff}} = 2.02$), and its oriented part would thermalise the fold band through the
    decays of the odd $\Psi_A$ states ($\Delta N_{\mathrm{eff}} = 0.0958$ to 0.1257, 2.1 to 2.4 standard deviations above ACT DR6);
    consequently both halves of $\Psi$ keep an exact fold parity and the dark matter consists of the lightest odd states of
    both halves (two species, relic recomputed: $x_{\mathrm{f}} = 30.38$, $G_{\mathrm{I12}} = (15.5\ \text{TeV})^{-3}$); (d) the
    invisible width uses the PDG 2025 value $N_\nu = 2.9963 \pm 0.0074$ instead of the LEP 2006 value; (e) $N_{\mathrm{eff}}$ is
    computed for three flavours (3.0476 to 3.0485) and the precision value 3.0432 (Cielo et al.) replaces 3.044; (f) the
    cosmology has three massive neutrinos ($\sum_im_i = 0.0599$ eV) instead of one of 0.05 eV and no dark radiation; (g) the
    $Z$ widths of three generations (2485.2 MeV with the QCD factor) remove the one-generation conflict (1232 MeV); (h) the
    Kohn-Sham portal sources use the three-generation localisations. Errors found and corrected during the version-2 work:
    the 1-3 MSW resonance energy was first evaluated with a spurious factor $1/c_{13}^2$ (11.49 GeV); it is
    $E = \Delta m_{ee}^2\cos2\theta_{13}/(2V_{\mathrm{CC}}) = 11.135$ GeV with $\Delta m_{ee}^2 = c_{12}^2\Delta m_{31}^2 +
    s_{12}^2\Delta m_{32}^2$, confirmed by the exact three-flavour root 11.133 GeV (now a check); CAMB's built-in
    normal-hierarchy option put the mass in one mass state, so the three mass states are now set up explicitly with the
    iteration of section 9; a check of the analysis (fermions below the uncertainty estimate) first used a threshold that the
    muon and the strange quark exceed and now tests the documented statement ($m/m_{\mathrm{Heis}} < 0.01$ for every fermion);
    in the documents the muon eigenvalue ($\tilde\varepsilon = 4.7795\times10^{-6}$), the Landau-Zener bound
    ($\mathcal{P}_{\mathrm{LZ}} \le 2.6\times10^{-77}$) and the explanation of $\Omega_\nu h_{100}^2$ (the non-relativistic coefficient
    94.06 eV at the instantaneous-decoupling temperature, 93.14 eV with the heating) were corrected; the published values of
    the decoupling method were read from the source (Escudero 2020, Table 1) and the separate-temperature value 3.048 added
    to the validation.
22. **Independent review of version 2 (2026-10-18).** A review of the five documents of version 2 against the outputs found
    every computed number in agreement except three roundings, and found the following, all corrected in the documents: (a)
    the dark-matter relic: the operator $\bar\Psi_{\mathrm{DM}}\Psi_{\mathrm{DM}}$ times a squared field strength annihilates a
    pair only from the state $^3P_0$, so the unitarity bound on the spin-averaged cross-section is
    $\sigma \le \pi/(4k_{\mathrm{cm}}^2)$ and $\langle\sigma v_{\mathrm{rel}}\rangle \le \sqrt{\pi x_{\mathrm{f}}}/M_{\mathrm{DM}}^2 =
    5.79\times10^{-26}$ cm$^3$/s; the freeze-out requirement $2.01\times10^{-25}$ cm$^3$/s exceeds it 3.47 times (the documents had
    compared it with $(4\pi/M_{\mathrm{DM}}^2)\sqrt{x_{\mathrm{f}}/\pi} = 2.32\times10^{-25}$ cm$^3$/s, the bound of one helicity
    channel without the spin average, and called the requirement 87 % of it); the relic abundance of the dark matter is
    therefore OPEN in version 2, and the check `B3_relic_requirement_and_unitarity` of `um2_analysis.py` now computes the
    bound, its numerical thermal average, the crossing velocity $v_{\mathrm{c}} = 0.263$ and the fraction (79 %) of pairs
    above it; (b) "no tip operator reaches $\Psi_B$" holds only for chiral tip currents with $P_L$ and for operators built on
    $\bar\Psi\Psi$ (a non-chiral tip current would reach $\Psi_B$); (c) the fast-flavour dispersion relation is written with
    the shifts by the moments of the electron-lepton-number distribution (now $\mathcal{I}_0$, $\mathcal{I}_1$) and the stated
    metric $\mathrm{diag}(1, -1)$ on $(x_4, x_3)$; (d) $c_{\mathrm{Z}} = \tilde c_{\mathrm{Z}} = 0$ is a modelling choice (ASSUMED):
    the invisible width bounds the even part and $N_{\mathrm{eff}}$ disfavours, but does not exclude, the oriented part; (e)
    the coordinate rule: the flavour, decoupling and fast-flavour equations had written a letter $t$ for $x_4$ and $z$ for the
    symmetry axis $x_3$; (f) roundings: the adiabatic solar $\mathcal{P}_{ee}$ at 15 MeV (0.306), the bulk mass of the tau
    singlet ($-9.205H$), the Kohn-Sham accuracy ($2.2\times10^{-9}$ relative); (g) minor items: the largest possible
    $J_{\mathrm{CP}}$ computed from the best-fit angles (0.0335) against NuFIT's marginalised value ($0.0333 \pm 0.0007$); the
    conventions of the supernova resonances (two-flavour conditions); the tip matrices equal the mixing matrices only with
    $\mathcal{K}_e = \mathcal{K}_u = \mathbf{1}$ (ASSUMED); the three roles of the measured values; the sum rules of the
    uncertainty analysis (absolute $1.0\times10^{-8}$, relative $7.8\times10^{-4}$ and $6.0\times10^{-4}$ for $W^\pm$ and $Z$); the
    50-digit roots against the stored masses ($4.5\times10^{-11}$); the labels ESTIMATE and STANDARD; the strength required for a
    single species ($(17.6\ \text{TeV})^{-3}$ with $g_\rho = 105.75$, not a version-1 value); further notational clashes added
    to the symbol lists; (h) self-containment: equations and inputs used but not written in a document (the relic and
    $\Delta N_{\mathrm{eff}}$ formulas, the Einstein-Boltzmann equations, the BAO goodness of fit and data, the nonlinear background
    equations, the fermion equations with their boundary conditions, the decoupling equations, the CNB, Landau-Zener, adiabatic
    solar, condensate and pairing formulas, the Kohn-Sham equations behind the quoted equations of state) are now written out
    in every document that uses them.
23. **Version 3 (2026-10-18).** By the author's order for the coupled solution: (a) the computations `um2_thermal.py`,
    `um2_coupled.py` and `um2_series.py` (new), the matter power spectrum and the version-3 model in `um2_cosmology.py`, the
    Majorana alternative in `um2_neutrino.py`, and an optional potential on the lower component in the Kohn-Sham solver
    `um2_kohnsham.py` (the record's reference states reproduced again to $10^{-12}$); (b) the portal I13 was first coupled to
    the $B - L$ current; the computation C9 then showed that the annihilation of the dark matter into right-handed neutrinos
    and its inverse would thermalise them and add $\Delta N_{\mathrm{eff}} = 0.144$ (2.5 standard deviations above ACT DR6), so
    I13 couples to the baryon-number current ($G_{\mathrm{A}}$: $1.072 \to 1.278\times10^{-9}$ GeV$^{-2}$; xenon: 0.12 to 0.16 of
    LZ); (c) the first version of the C9 rates compared the production rate of three flavours with the equilibrium density of
    one; corrected (per flavour) before the result was recorded; (d) `um2_thermal.py` read a key of the analysis output that
    item 22 had renamed; corrected; (e) the early-Universe environments first put the whole net baryon density into protons;
    it is now shared by weak equilibrium, $n_{\mathrm{n}}/n_{\mathrm{p}} = \mathrm{e}^{-(m_{\mathrm{n}} - m_{\mathrm{p}})/T}$, and the
    QCD interaction measure had the wrong flavour thresholds in its perturbative branch and a special case at exactly 200 MeV
    (neither affected a stored number); (f) the text of the validity check C7 now refers to the benchmark strengths; (g) the
    thermal numerical result refines the version-2 statement on I12: a cross-section at the $^3P_0$ limit at every energy
    leaves $\Omega_{\mathrm{DM}}h_{100}^2 = 0.058$ per species, so I12 alone could give the relic only as a strongly coupled
    channel at the unitarity limit; (h) in MODEL a cross-reference to the neutrino decoupling pointed to section 9.4 instead
    of 10.4 (since version 2).
24. **Independent review of version 3 (2026-10-18).** A review of the five documents of version 3 at commit `726997f` against
    the outputs (2055 s, 74 tool calls) found every version-3 number in agreement with the stored outputs except the items
    below, and the following errors and omissions, all corrected in the computations and the documents (the affected scripts
    rerun; 235 checks, all passing): (a) the I13 bilinear $\mathrm{i}\bar\Psi\gamma^MP_b\Psi$ is Hermitian only for $M \ne x_0$,
    since the Hermitian conjugate of $\mathrm{i}C\gamma^{x_0}P_b$ is $\mathrm{i}C\gamma^{x_0}P_a$; the action now sums over
    $M = x_1, \dots, x_7$, and the new check `C8_I13_algebra` verifies with the author's matrices the Hermiticity, its failure for
    $x_0$, $CP_bC^{-1} = P_a$, the Lorentz property and the structure under $\mathcal{B}$ ($C\gamma^MP_b$ commutes with $\mathcal{B}$
    for $x_1, \dots, x_4$ and anticommutes with it for $x_5$, $x_6$, $x_7$, whose currents vanish for spinors in one half, so the
    Standard-Model zero modes, all in the half $\mathcal{B} = -1$, are not mixed); no number changes, since the zero-mode
    reduction uses the four-dimensional components only; (b) the block response of the coupled solution kept only the hidden
    pressure of non-relativistic matter and only the $\Delta\bar p$ term of the adiabatic response; it now uses the full
    response ($c_\rho$, $c_3 = -3c_\rho$, $c_p$) and the hidden pressure $\bar p = \frac14\,\partial p/\partial\ln f$ of every
    species, the hot plasma included (ideal gases with the $x_0$ masses, the QCD interaction measure with the block dependence
    of the QCD scale, the order-$\alpha$ electroweak pressure with the block dependence of the couplings): $\Delta\ln f$ at the
    freeze-out $5.6\times10^{-45} \to 1.1\times10^{-34}$ ($7\times10^{-39}$ in the electroweak era, at most $9\times10^{-49}$ from
    nucleosynthesis on), the loop gain $1.3\times10^{-44} \to 1.1\times10^{-33}$, the radion term of the metric series accordingly;
    the Kohn-Sham block feedback also reports the full response; the conclusion, a negligible back-reaction, is unchanged; (c)
    the thermal $W$, $Z$ condensates had only the free massive-vector part; the order-$\alpha$ interaction part (FE-76;
    Feynman-Hellmann; for QCD it reproduces the trace-anomaly condensate to $10^{-16}$, now part of check C4) dominates above
    $m_{\mathrm{W}}$: the $W$ condensate at the freeze-out is $-5.0\times10^{11}$ GeV$^4$; (d) the freeze-out environment used the
    version-2 $x_{\mathrm{f}} = 30.38$ ($T = 1.46$ TeV); it uses the version-3 $x_{\mathrm{f}} = 31.23$ ($T = 1.42$ TeV), and
    $\Delta\varepsilon_{\mathrm{DM}}/M_{\mathrm{DM}}$ there is $-1.5\times10^{-6}$ (was $-1.6\times10^{-6}$); the degrees-of-freedom
    table lists 1.42 TeV instead of 1.46 TeV; (e) the thermal history did not state $\lambda$: the self-interaction contains the
    channel in which two dark-matter particles become two fold quanta through the transition scalar density
    $n^{\mathrm{sc}}_{\mathrm{DF}} = a_{\mathrm{DM}}b_{\mathrm{fold}} + b_{\mathrm{DM}}a_{\mathrm{fold}}$; the new computation C10 gives
    $\Delta N_{\mathrm{eff}} = 1.83\times10^{26}G_\lambda^2$ GeV$^4$ and the bound $G_\lambda \le 2.3\times10^{-15}$ GeV$^{-2}$, now
    ASSUMED (the Kohn-Sham test value $\lambda_{\mathrm{test}}$ with $v_{\mathrm{t}} = H^{-3}$ would thermalise the fold bands and add
    0.19); (f) the elastic $\nu_R$ rate of the $B - L$ alternative used $\sigma_{\mathrm{el}} = G_\nu^2E^2/\pi$ instead of
    $G_\nu^2E^2/(2\pi)$ for a Weyl $\nu_R$ on a heavy Dirac fermion: kinetic decoupling at $x = 25.1 \to 24.4$
    ($T = 1769 \to 1816$ GeV), $\Delta N_{\mathrm{eff}} = 0.144$ unchanged; (g) the I11 production of $\nu_R$, quoted as $10^{-14}$ of
    the I13 rate without a source, is now computed: $2.0\times10^{-17}$; (h) the fractions of the annihilation rate above the
    unitarity crossings were integrated inaccurately (one of them exceeded 1): they are now computed by adaptive quadrature
    with the break points of the thermal weight (I12 at the relic strength: 96 %; the I12 benchmark $5.3 \to 5.2\times10^{-4}$;
    I13 uncapped $24.5 \to 24.8$ %, capped $19.0 \to 21.7$ %); the exact I12 crossing at $E_{\mathrm{cm}} = 89510$ GeV is quoted
    with its relative velocity $v_{\mathrm{rel}} = 2\beta_{\mathrm{cm}} = 0.269$ (0.274 is the non-relativistic formula); the
    relic at the $^3P_0$ limit compares the thermal average and $\sqrt{\pi x}/M_{\mathrm{DM}}^2$ at the same $x$ (5.33 against
    $5.84\times10^{-26}$ cm$^3$/s); (i) stale or mixed statements: "$c_{\mathrm{V}} = 0$" and "no dark radiation" or "no extra
    radiation" of version 2; the cosmology labels (UM-2 version 3 is the model with the freeze-in fold bands:
    $N_{\mathrm{eff}} = 3.0442$, $\sigma_8 = 0.8118$, $\chi_{\mathrm{BAO}}^2 = 31.49$, $\mathcal{H}_0 = 67.38$ km/s/Mpc; the model
    without them is the neutrino content of version 2); "relic OPEN" qualified as the result of version 2; the check counts of
    `um2_neutrino.py` (16) and `um2_cosmology.py` (8); the amplitude of the kinetic-function shift at the freeze-out
    ($1.7\times10^{-16}$, not below $10^{-50}$); "perturbative" made precise (22 % of the freeze-out rate at the bound of total
    angular momentum 1; $G_f^{-1/2} = 30$ TeV for the quark doublet, below $E_{\mathrm{cm}} \approx 89$ TeV); the $\nu_R$ couplings
    (the I11 coupling as well as the tip mixing); the dark matter is not counted in $g_\rho$, $g_s$ (as in the code); roundings
    ($\tilde I^{(b)}_{\nu_R} = 0.301$ to 0.308, $g_\rho = 104.95$ at 200 GeV, $D_+\mathrm{e}^{-a_4} = 0.7878$ today,
    $\Phi_{\mathrm{rms}} = 5.03\times10^{-8}$ at 1 Mpc$^{-1}$, the Poisson agreement $1.5\times10^{-6}$); the signature convention of
    the trace anomaly and of the Proca Lagrangian, written for $(+,-,-,-)$; the $\overline{\mathrm{MS}}$ angle in the running
    couplings; the Yukawa strengths $\mathcal{A}_n$ for two different profiles; the order-2 magnitude
    $(2.4\times10^{-5})^2 = 5.8\times10^{-10}$; a heading labelled DERIVED over estimates; (j) self-containment: the quark
    sensitivities to the block scale, the scale $2\pi T$ of $\alpha_3$, the densities of the environments, the hadron list,
    $\Omega_{\mathrm{m}}$, the symbols $N_{\mathrm{c}}$, $N_{\mathrm{fold}}$, $G_{\mathrm{A}}^{B-L}$, the factor 2 of the two dark-matter
    species, $g_{s,e\gamma}$, $K_1$, $K_2$, the squared centre-of-mass energy, $\beta_{\mathrm{cm}}$, the total angular momentum of a
    partial wave and the version-3 symbols are now stated in every document that uses them, and the variable
    $E_{\mathrm{cm}}^2/(4M_{\mathrm{DM}}^2) - 1$ is no longer written with the letter $z$ (in version 4 $z$ is only $6Hx_0$ and the
    redshift is $z_{\mathrm{red}}$).
25. **Version 4 (2026-10-18): the organisation and presentation ordered on 2026-10-18 at 15:42.** (a) *The presentation
    rules* S1 to S6 (section 2) for MODEL, FIELD_EQUATIONS, SOLUTION, ANALYSIS and PROVENANCE: every document starts with "How
    to read this document"; every display equation is followed by the complete list of its symbols; every field equation or
    interaction term that a document uses is written out there with its tag FE-$n$ or IN-$n$ and its symbols; a solution is
    presented as the field equation, the approximation (the small parameter and the size of what is neglected), the
    solution, its check in its own equation and in concert with the other field equations, and the status labels; the reader
    is never sent to another file; every change of a claim is stated here (commit `9dbc424`). (b) *The notation.* Version 3
    used many letters for several things ($k$, $s$, $M$, $H$, $p$, $a$, $\kappa$, $\Lambda$, $\delta$, $n$, $\mu$, $e$, $J$, $u$,
    $G$, $\beta$, $w$, $f$, $c$ and others); version 4 gives every meaning its own symbol, among them the block variable
    $K = 1/f^2$ (was $k$, now only a wave number); the Hubble rate $\mathcal{H}$ and the rate $\mathcal{H}_f$ of the block scale
    (were $H$ or $A$, and $h$; $H$ is only the author's constant); the Lovelock order as the index $p$ in brackets,
    $\alpha_{(p)}$, $w_{(p)}$, $\mathcal{L}_{(p)}$, $\mathcal{E}_{(p)}$; the energy-momentum tensor $\mathcal{T}^M{}_N$ (was $T$, now
    only the temperature); the pressure $p_5$ of the extra times and the stabiliser density $\rho_{\mathrm{stab}}$; the gauge
    couplings $g_3$, $g_2$, $g_1$ and $\hat g_3$, $\hat g_2$, $\hat g_1$ (were $g_s$, $g$, $g'$), so that $g$ is only the metric;
    the tip mixing matrices $\mathcal{K}$ and the tip Yukawa matrices $\mathcal{Y}_\nu$, $\mathcal{Y}_e$, $\mathcal{Y}_u$,
    $\mathcal{Y}_d$; the scalar density $n^{\mathrm{sc}}$ of dirac16complex; the mass parameter $m_\Psi$ and the record's
    parameter $\mathcal{M}$; the four-dimensional dark-matter and fold-band fields $\Psi_{\mathrm{DM}}$, $\Psi_{\mathrm{fold}}$
    ($\chi$ is now only the block spinor); the dimensionless boson eigenvalue $\tilde m^2$, its wave number $\varpi$ and the
    profiles $F$; the Newtonian-gauge potentials $\Phi$ and $\Psi_{\mathrm{N}}$; the gauge fields in the geometric normalisation
    ($G$, $W$, $B$) distinguished from the canonically normalised $W^\pm$, $Z$, $A$; the overlaps $\tilde I_{of}$ made
    dimensionless by an explicit factor $1/H$; Euler's number, the imaginary unit and the differential upright. The table of the
    decisions (the version-3 symbol and meaning, the version-4 symbol) is `docs_src/NOTATION.md` (commit `fd749e8`); this
    document applies it in every display, inline formula and sentence. (c) *The symbol registry and its check.* Every symbol
    of the documents has one entry (meaning in complete sentences, unit, value and status) in the registry
    `docs_src/symbols/*.json`: the core file with the symbols of the field equations (488 entries when the inventory was made,
    commit `fd749e8`) and one file per document (`provenance.json` for this document). `tools/symbols_tool.py` (commit
    `9dbc424`; extended in `fd749e8`: exponents of $\mathrm{e}$ and of brackets, evaluation bars and integral limits are
    expressions, not indices) writes the symbol list under every display equation from the registry and checks that every
    atom of every display (symbols, name subscripts, index letters, primes and daggers) is defined by a listed key, that every
    display has its list, and that no atom has two entries; since commit `1e264d0` it also checks that every display tagged
    FE-$n$ or IN-$n$ is written exactly as in the inventory, with the same keys. (d) *The inventory.*
    `docs_src/equations.json` lists the 136 field equations FE-1 to FE-136 and the 18 interaction terms IN-1 to IN-18 in the
    version-4 notation, each with its title, status, fields, the place where it is solved and the registry keys of all its
    symbols; a test document of all 154 equations passed the check and built with 0 overfull boxes (commit `fd749e8`). Commit
    `1e264d0` aligned it with the documents: FE-40, FE-42 and FE-43 now write the $x_0$ component (with $p_0$) and the
    extra-time components $x_5$, $x_6$, $x_7$ (with $p_5$) separately, next to the block-isotropic form with $\bar p$; FE-52 and
    FE-53 quote the squared eigenvalues $\tilde m_1^2$, $\tilde m_n^2$; FE-79 records the first-order result of fix 1 of
    section 10. (e) *The residual analysis.* The new
    computation `um2_residuals.py` (52 checks; 287 in all) measures the residual of the stored solution in 26 field equations
    and 26 links in concert; its findings are section 10 (commit `cc2d514`). (f) *The precision fixes:* the first-order
    perturbation theory for $\mathrm{d}\ln\tilde m_{\mathrm{W}}^2/\mathrm{d}A_{\mathrm{mf}}$, the robust integration of the right-handed
    neutrinos, the CNB quadrature, the deterministic thread counts in the Kohn-Sham scripts, and a stale check text (section
    10; commit `cc2d514`). (g) *Claims.* No claim of version 3 changes; the changed numbers and the statements made precise are
    listed at the end of section 10. (h) The documents of version 4: SOLUTION and ANALYSIS (commit `1e264d0`), MODEL,
    FIELD_EQUATIONS and PROVENANCE (this version).

# What is not in the repository, and why

By the author's instruction the following private inputs are never committed (they are git-ignored): the prompt files, the
author's private PDF with the supernova dark-energy fits, the folders `dirac-main/` and `vendor/`, the archive
`dirac-main_2.zip`, the files `Generalized_Kronecker_Delta.*`, and the notebook `WaveFunctionUniverse-4+4-Einstein-Lovelock.nb`
with its `.mx` files. The paper "Neutrino Flavor Conversion.pdf" (Gogilashvili and Tamborra, arXiv:2605.16504) is a
third-party publication and is not committed either; UM-2 cites its results. UM-2 uses from these inputs only what is written
out in this document (the notebook formulas of the metric and of the gamma matrices, the two supernova fits, the explosion
statistics).

# Reproduction

From the repository root, with Python 3 and the packages sympy, numpy, scipy, mpmath, matplotlib and camb installed
(`pip install sympy numpy scipy mpmath matplotlib camb`), the commands

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
python universe_model_2/code/um2_thermal.py
python universe_model_2/code/um2_coupled.py
python universe_model_2/code/um2_series.py
python universe_model_2/code/um2_residuals.py
python universe_model_2/tools/symbols_tool.py check
python universe_model_2/tools/build_docs.py
python universe_model_2/tools/compare_outputs.py
```

rerun every computation in dependency order (each exits with code 0 if and only if all its checks pass; the residual
analysis reads the outputs of all the others and must run last), check the symbol lists of the five documents against the
registry (the check must end with `symbols_check=OK`), rebuild the LaTeX and PDF documents from the Markdown sources (pandoc
and a TeX Live installation with the `lmodern` package are needed; every document must build with 0 overfull boxes), and
compare the regenerated files with the committed ones (numbers to a relative $10^{-9}$, run times and check texts listed
separately). The document build is deterministic: no dates in the LaTeX sources, PDF dates and trailer identifiers suppressed,
a fixed `SOURCE_DATE_EPOCH`.

Software used: Python 3.13.16, sympy 1.14.0, numpy 2.5.3, scipy 1.18.1, mpmath 1.3.0, matplotlib 3.11.2, camb 2.0.5, pandoc
3.1.3, pdfTeX 1.40.25 (TeX Live 2023).

# History in the repository

UM-2 was started on top of commit `0cb4916`. Version 1: its computations were committed in the order algebra and geometry
(`ca523d9`), background gravity (`0b3e10d`), field reductions (`6fc35a0`), mass spectra (`dcfd528`), Kohn-Sham (`2f3018e`),
electroweak sector (`2e4c48d`), primordial era (`a502e62`), cosmology (`717b46e`), analysis (`a06b55e`), followed by the
corrections listed above and the documents MODEL, PROVENANCE, FIELD_EQUATIONS, SOLUTION and ANALYSIS (Markdown, LaTeX and PDF
each); the fixes of the three independent reviews are in `b386446`, `fa7305f`, `b0e686e`, `9285bb6`, `d92a61b`, `c98de95`,
`1561566`, `df358db` and `5b73d16`; a checklist for manual reruns and the comparison tool are in `7b86239`. Version 2: three
generations and the masses and mixing (`94621af`), the neutrino flavour conversion (`a0d750a`), the electroweak sector of three
generations (`cf824d5`), the removal of the tip $Z$ portal and the cosmology with three massive neutrinos (`53c5139`), the dark
matter of both halves, the twelve-fermion tables and the three-generation tip and gauge checks (`b755990`), the corrected 1-3
resonance (`b999f57`), the documents MODEL (`9a5b92b`), FIELD_EQUATIONS (`79d9d31`), SOLUTION (`a3dcc6a`), ANALYSIS (`df6d94a`)
and PROVENANCE (`4a6421d`), and the fixes of the independent review of version 2 (item 22; `ecca926`). Version 3: the thermal
history, the coupled solution, I13, the metric series and $\sigma_8$ (`15c2aab`), I13 on the baryon-number current (`3fa1b49`),
the documents MODEL (`765f0b8`), FIELD_EQUATIONS (`41e921a`), SOLUTION (`df23013`), ANALYSIS (`19d2c06`) and PROVENANCE
(`726997f`), the fixes of the independent review of version 3 with the record of the fresh-clone verification of `726997f`
(item 24; `815db9e`), and the record of the fresh-clone verification of `815db9e` (`93e5c03`). Version 4: the presentation
rules and the symbol tool (`9dbc424`), the residual analysis and the precision fixes (`cc2d514`), the notation, the inventory
and the core registry (`fd749e8`), the documents SOLUTION and ANALYSIS of version 4 with the inventory aligned and the
extended symbol check (`1e264d0`), and the documents MODEL, FIELD_EQUATIONS and PROVENANCE of version 4 (this version).
