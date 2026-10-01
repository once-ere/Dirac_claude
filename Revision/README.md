# Revision — a new, separate record for the author's primordial gravitational field

This folder holds a COMPLETELY NEW record of the calculations the author requested on 2026-10-01 for the
primordial gravitational field given below. Nothing in it is copied from, or mixed with, the earlier
stages of the repository (`artifacts/`, `provenance/`, `studies/`, ...): every result here is computed
anew by code in this folder. The binding plan is [`SPEC.md`](SPEC.md).

## The author's task (verbatim, 2026-10-01)

> USE the metric tensor
> {{exp^(2 a4[x4]) Sin[6 H x8]^(1/3),0,0,0,0,0,0,0},{0,exp^(2 a4[x4]) Sin[6 H x8]^(1/3),0,0,0,0,0,0},{0,0,exp^(2 a4[x4]) Sin[6 H x8]^(1/3),0,0,0,0,0},{0,0,0,-1,0,0,0,0},{0,0,0,0,-exp^(-2 a4[x4]) Sin[6 H x8]^(1/3),0,0,0},{0,0,0,0,0,-exp^(-2 a4[x4]) Sin[6 H x8]^(1/3),0,0},{0,0,0,0,0,0,-exp^(-2 a4[x4]) Sin[6 H x8]^(1/3),0},{0,0,0,0,0,0,0,Cot[6 H x8]^2}}
> for the primordial Gravitational Field.
>
> Work in a (new) folder named 'Revision', and write completely new record of these new calculations.
> You must NOT mix old with new, or otherwise adulterate our new findings.
>
> Read, clearly understand and remember "Gmail - w = equation of state parameter =w = -0.764 = forcing
> the Unite supernova data by itself to fit a flat, non-evolving dark energy model.pdf". [...]
>
> YOU MUST remember that dirac16complex is a 16-component fermi spinor field whose components are complex
> valued, anti-commuting, objects, that transform under a 16-dimensional irreducible representation
> (irrep) of Pin(4,4); and for the determinant 1 transformations, transform under a direct sum of two
> inequivalent 8x8 irreps of Spin(4,4); Pin(4,4) is the double cover of the orthogonal groups O(4,4)
> (Spin(4,4) is the double cover of the orthogonal groups SO(4,4)). Quantize dirac16complex using
> canonical quantization, extended to 4+4 dimensions.
>
> YOU MUST remember that dirac16complex00 is a set of 16 scalar fields that transform as a Pin(4,4) spinor.
>
> Write out and record (also provide .md, .tex, and .pdf provenance files) for the Lagrangian for
> dirac16complex and the Lagrangian for dirac16complex00, the energy-momentum tensor operator for each of
> dirac16complex and dirac16complex00, the kinetic energy, potential energy, pressure and energy density
> and equations of state for the covariant field equations (i.e., the Euler-Lagrange equations for
> dirac16complex and the Euler-Lagrange equations for dirac16complex00) for the case of interaction with
> the above primordial Gravitational Field. For each case, calculate and record (with provenance) the
> field equations for a4[x4].
>
> For the case of dirac16complex interacting with this new primordial Gravitational Field, above, plan and
> employ a DFT-motivated approximation similar to the one that you already created (recall and remember,
> if you forgot), with a Kohn-Sham fermion-gas thermodynamic effective potential, that employs the DFT
> ground and first-excited-state computation, and
>
> Couple both dirac16complex and dirac16complex00 to the above primordial Gravitational Field using the
> canonical spin connection and the appropriate Lagrangian; i assume you know how to do this correctly.
> Correct me if i am wrong. Test and verify our two Lagrangians:
> [1]- the Lagrangian for dirac16complex must be non-trivial (i.e., the Euler-Lagrange equations for
> dirac16complex always possess non-zero contributions from gravity (through the canonical
> spin-connection, unless we are in flat 4+4 spacetime), must be self consistent, must be checked and
> verified).
> [2]- the Lagrangian for dirac16complex00 must be non-trivial (the same requirements).
>
> Hypothesis: dirac16complex provides a possible physical mechanism for a time-varying dark energy
> equation of state and/or a possible physical mechanism for a time-varying dark matter equation of
> state, both of which you will investigate.
> Hypothesis00: dirac16complex00 provides [the same], both of which you will investigate.
>
> [Documents: md, tex and pdf provenance files with the exact, correct field equations, the
> energy-momentum tensor operator, the kinetic energy, potential energy, pressure, energy density and
> equations of state, for the fermion dirac16complex field and for the 'semi-classical' dirac16complex00
> field, in the presence of the above primordial Gravitational Field.]
>
> PROVE that Universes of masses {+mass, -mass} are created in pairs for each case of the dirac16complex
> and the dirac16complex00 fields. Create new provenance markdown file, latex, and pdf files, that contain
> the exact, correct, proof results for both [fields].
>
> push 'Revision' and any other new files (not listed in .gitignore) to
> https://github.com/once-ere/Dirac_claude.git. Check and verify this repo. DO NOT TAKE SHORTCUTS. [...]

(Bracketed passages abridge repeated sentences of the original message; nothing was changed in meaning.)

## Answers given to the author before the work started (2026-10-01)

* The private PDF was read and understood (CPL w(a) = w0 + wa (1 - a); Unite constant-w fit w = -0.764;
  (w0, wa) = (-0.861, -0.60); quintessence formulas). One inconsistency in it is handled explicitly: its
  thawing/freezing table gives the signs of wa opposite to its own formula (thawing means wa < 0 in this
  convention). Its notation H (Hubble rate) and a (scale factor) differ from the metric's H and a4.
* Coupling through the canonical spin connection is correct for both fields (both are Pin(4,4)
  spinors). The non-trivial Lagrangian is the Dirac-type one with Psibar = Psi^dagger C; the notebook's
  real Majorana-type Lg[] is a total derivative for anticommuting fields. In this metric the
  time-direction spin-connection terms of the 3 inflating and 3 deflating directions cancel exactly,
  while a hidden-direction term proportional to H survives; non-triviality [1], [2] is proved exactly.
* Canonical quantisation in 4 + 4 forces an indefinite (Krein) inner product; this is stated.
* "PROVE that Universes ... are created in pairs": the exact pairing theorems are proved for both fields;
  no creation process, rate or amplitude follows from these equations, and the documents say so.

## Folders

| folder | content | state |
| --- | --- | --- |
| `gkd_lovelock/` | GKD (pure-Rust generalized Kronecker delta) and the three Lovelock tensors of this metric | computed (commit 3e81eeb), 19/19 checks; independent verification to be completed |
| `algebra/`, `theory/` | gammas, Pin/Spin facts, Lagrangians, field equations, EMT, quantisation (Wolfram + sympy) | to do |
| `field_equations_a4/` | the Einstein-Lovelock equations for a4[x4] with each field as source | to do |
| `kohn_sham/` | Kohn-Sham fermion gas in the deflating field (instantaneous states) | to do |
| `dark_sector/` | the two hypotheses against the Unite values | to do |
| `pairing/` | the pairing theorems for both fields | to do |
| `docs/` | md + tex + pdf documents | to do |
