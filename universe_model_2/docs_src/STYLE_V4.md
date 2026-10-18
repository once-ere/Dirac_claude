# UM-2 version 4: the presentation rules (binding for every writer of the UM-2 documents)

Version 4 of UM-2 (2026-10-18) reorganises and re-presents the model, its coupled field equations and their approximate
solution. The physics and the computations are those of version 3 (235 checks; the code in `universe_model_2/code/` and
its outputs in `universe_model_2/outputs/`), unless a task says otherwise. What changes is the organisation and the
presentation, ordered by the author on 2026-10-18 at 15:42:

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

## The documents

`MODEL`, `FIELD_EQUATIONS`, `SOLUTION`, `ANALYSIS`, `PROVENANCE` (and `MANUAL_TASKS`), each as `NAME.md`, `NAME.tex` and
`NAME.pdf` in `universe_model_2/`, built by `python universe_model_2/tools/build_docs.py NAME` (pandoc, then pdflatex;
0 overfull boxes required). The `.md` is the source; never edit a `.tex` or `.pdf` by hand.

## Rule S1: every display equation is followed by the complete list of its symbols

Every display equation (`$$ ... $$`) of the five documents is followed, after at most one blank line, by a marker line

```text
<!-- symbols: key1, key2, key3 -->
```

that names the registry entries of EVERY symbol in the equation: every quantity, field, coupling, constant, operator
(partial derivative, covariant derivative, Dirac adjoint), every index letter (with the values it takes), every special
mark (prime, dagger, transpose, star), the imaginary unit, Euler's number and the differential. Then run

```text
python universe_model_2/tools/symbols_tool.py expand NAME     # writes the list under every marker from the registry
python universe_model_2/tools/symbols_tool.py check NAME      # must end with symbols_check=OK (0 problems)
```

`expand` writes, under each marker, the block "Symbols in (FE-n)." with one bullet per key (the symbol, its meaning, its
unit, its value and status where the registry has them). `check` extracts every atom of every display equation and
reports any atom that no listed key defines, any display without a marker, unknown keys and out-of-date lists. Typography
needs no definition: digits, + - = ( ) [ ] | , and the like, \frac, \sqrt, spacing, \cdot, \dots, \le, \ge, \approx,
\sim, \times, \pm, the standard functions sin, cos, tan, cot, sinh, cosh, tanh, exp, ln, log, det, min, max, lim, and the
signs of sums, products and integrals (but their index letters and integration variables are symbols and need entries).
Use `python universe_model_2/tools/symbols_tool.py atoms "LATEX"` to see the atoms of a formula.

A FIELD EQUATION carries a tag: `\tag{FE-n}` with the number of the inventory `universe_model_2/docs_src/equations.json`
(see Rule S3). Whenever a field equation is used in a document (to solve it, to analyse it, to combine it with another),
it is WRITTEN OUT AGAIN with the same tag and the same marker, so that its complete symbol list stands right there. The
reader never has to look anywhere else for a definition: "EVEN if you have done this before".

## Rule S2: one symbol, one meaning

Across all five documents a symbol has exactly one meaning. The registry enforces this: every atom belongs to one entry.
Version 3 used many symbols for several things (k, s, M, H, p, a, kappa, Lambda, delta, n, mu, e, J, u, G, beta, w, f, c,
...); version 4 gives each meaning its own symbol. The table of these decisions is `universe_model_2/docs_src/NOTATION.md`
(old symbol and meaning, new symbol). When text of version 3 is reused, translate it to the new symbols.

Typography: Euler's number is `\mathrm{e}` (so `\mathrm{e}^{2a_4}`), the imaginary unit `\mathrm{i}`, the differential
`\mathrm{d}` (so `\mathrm{d}x_0`, `\frac{\mathrm{d}f}{\mathrm{d}x_4}`); a word in a subscript or superscript is upright,
`m_{\mathrm{eff}}`, `M_{\mathrm{Pl}}`, `\delta_{\mathrm{tip}}`. The coordinates are the author's X = {x_0, x_1, ..., x_7}:
x_0 the hidden space-like direction, listed first, period pi/(6H); x_1, x_2, x_3 ordinary space; x_4 the time; x_5, x_6,
x_7 the extra times. Never x_8, never a list with the hidden direction last. W^+ carries the electric charge +e and W^-
the charge -e. No Higgs particle.

## Rule S3: the registry and the inventory

* The registry is the set of JSON files `universe_model_2/docs_src/symbols/*.json` (keys unique over all files). An
  entry: `{"tex": "g_{MN}", "atoms": ["g"], "meaning": "...", "units": "...", "value": "...", "status": "..."}`; `value`
  and `status` optional. `meaning` is one or more complete plain sentences that a student understands without any other
  page: what the symbol is; for a derived quantity also its defining formula in terms of other symbols; for a field what
  it describes; for an index the values it takes. `units` is the unit or dimension in natural units (hbar = c = 1;
  "GeV", "1/length", "dimensionless"), "" for operators and indices. Math in `meaning` is written in `$...$`.
* `core.json` holds the symbols of the field equations (written by the inventory). Every other writer adds new symbols
  only to the file named for its document (`model.json`, `solution.json`, `analysis.json`, `provenance.json`); a symbol
  that two documents need goes into `core.json` (the lead merges at the end). Never change another file's entry; if a
  core entry is wrong, report it.
* The inventory `universe_model_2/docs_src/equations.json` lists every field equation: `{"id": "FE-1", "title": "...",
  "latex": "... \\tag{FE-1}", "keys": [...], "status": "...", "fields": [...], "solved_in": "..."}`. The field
  equations are numbered in the order of FIELD_EQUATIONS.

## Rule S4: the order of a document and the presentation of a solution

* Every document starts with "How to read this document" (what it contains, the status labels AUTHOR, RECORD, STANDARD,
  ASSUMED, INVENTED, DERIVED, ESTIMATE, OPEN, and the rule that every equation is followed by its symbols).
* A solution is presented as: (1) the field equation, written out with its tag and symbol list; (2) the approximation
  (what is neglected, the small parameter, the size of the neglected terms); (3) the solution (formula or numbers) with
  its own display equations and symbol lists; (4) the check of the solution in its own equation (residual or error,
  measured) and in concert with the other field equations that contain the same fields (e.g. the Kohn-Sham states in the
  gravitational equation: the block response; the masses in the electroweak widths; the neutrino masses in N_eff and the
  CMB); (5) status labels.
* Every number is taken from the outputs of the computations (`universe_model_2/outputs/*.json`, `reports/*.json`) and
  quoted with its precision; PROVENANCE says which output holds it. A new computation (if a task asks for one) is a script
  in `universe_model_2/code/` that writes `outputs/` and `reports/` with named checks and exits 0 only if all pass.

## Rule S5: the reader is never sent elsewhere

"NEVER refer the reader to some other file! PUT EVERY EQUATION you create and/or use IN THESE FILES." A document may
name the repository files that hold the computations (for reproduction), but never asks the reader to look into another
document for an equation, a definition or an argument; everything the reader needs is written in the document itself.

## Rule S6: honesty

The status labels stay as in version 3 (what is DERIVED and verified, what is ASSUMED or INVENTED, what is an ESTIMATE,
what is OPEN, the conflicts with data: no Higgs boson, W+W- unitarity near 1.2 TeV). Version 4 changes the presentation,
not the claims; every change of a claim must be stated in PROVENANCE.
